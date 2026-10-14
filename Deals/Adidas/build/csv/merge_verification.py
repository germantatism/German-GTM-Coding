"""Apply the 14 Oct 2026 official-source verification (research/result_D*.json) to coverage_final.json.
A (provider, country) pair stays only if the pass kept it; drops and unverified pairs are removed.
Usage: python3 merge_verification.py <research_dir> <coverage_final.json>"""
import json, sys, os, glob
RD, COV = sys.argv[1], sys.argv[2]
cov = json.load(open(COV))
removed = {}
for f in sorted(glob.glob(os.path.join(RD, 'result_D*.json'))):
    for r in json.load(open(f)):
        p = r['provider']
        gone = set(r.get('drop', [])) | set(r.get('unverified', []))
        if p in cov and gone:
            before = cov[p]
            cov[p] = [c for c in before if c not in gone]
            removed[p] = {'dropped': r.get('drop', []), 'unverified': r.get('unverified', []), 'evidence': r.get('evidence_url', ''), 'note': r.get('note', '')}
json.dump(cov, open(COV, 'w'), indent=1)
json.dump(removed, open(os.path.join(os.path.dirname(COV), 'verification_removed.json'), 'w'), indent=1)
print(sum(len(v) for v in cov.values()), 'pairs kept;', sum(len(v['dropped']) + len(v['unverified']) for v in removed.values()), 'removed across', len(removed), 'providers')
for p, v in removed.items(): print(f"  {p}: drop={v['dropped']} unverified={v['unverified']}")
