"""Relevant connections per country that are NOT in the customer sheet (status != Yes). python3 missing_list.py <gaps.json> [out.md]"""
import json, sys, collections
G = json.load(open(sys.argv[1]))
ORDER = ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Mexico', 'Peru', 'Uruguay', 'Bolivia', 'Costa Rica', 'Dominican Republic', 'Ecuador', 'El Salvador', 'Guatemala',
         'Honduras', 'Nicaragua', 'Panama', 'Paraguay', 'Indonesia', 'Malaysia', 'Philippines', 'Singapore', 'Thailand', 'Vietnam', 'Myanmar', 'Israel']
TAG = {'No': 'not on Yuno', 'In catalog, other countries': 'in Yuno catalog for other countries only', 'Not connected (possible via live provider)': 'not listed; a live provider here claims it',
       'Partial': 'partial', 'Yes (via provider)': 'processed via provider, no entry in the sheet', 'Yes (connection built; not listed on y.uno/integrations)': 'built, not on public directory'}
out = []; tot = collections.Counter()
for c in ORDER:
    rs = [r for r in G if r['country'] == c and r['on'] != 'Yes']
    if not rs: continue
    out.append(f"\n**{c}**")
    for r in sorted(rs, key=lambda r: ({'High': 0, 'Medium': 1}.get(r['relevance'], 2), r['type'], r['name'].lower())):
        tag = TAG.get(r['on'], r['on']); tot[tag] += 1
        extra = f" → {r['entry']}" if r['entry'] and r['on'] != 'No' else ''
        out.append(f"- {r['name']} ({r['type'].replace('Acquirer/PSP', 'processor').lower()}, {r['relevance'].lower()} relevance): {tag}{extra}")
txt = '\n'.join(out)
print(txt); print('\nTOTALS:', dict(tot))
if len(sys.argv) > 2: open(sys.argv[2], 'w').write('# adidas · relevant connections missing from the customer sheet (14 Oct 2026)\n' + txt + '\n')
