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

# compact per-country view (for chat): High first, then Medium; short tags
SHORT = {'No': 'not on Yuno', 'In catalog, other countries': 'in catalog for other countries only', 'Not connected (possible via live provider)': 'confirm via live provider',
         'Partial': 'partial', 'Yes (via provider)': 'processed via provider but absent from the sheet', 'Yes (connection built; not listed on y.uno/integrations)': 'built, not on public directory'}
import re
print('\n\n===== COMPACT =====')
for c in ORDER:
    rs = [r for r in G if r['country'] == c and r['on'] not in ('Yes', 'n/a')]
    if not rs: continue
    parts = []
    for rel in ('High', 'Medium'):
        items = []
        for r in sorted([r for r in rs if r['relevance'] == rel], key=lambda r: (r['type'], r['name'].lower())):
            tag = SHORT.get(r['on'], r['on'])
            if r['on'] == 'Not connected (possible via live provider)':
                provs = r['entry'].split(' is live')[0]; tag = f"confirm via {provs}"
            elif r['on'] == 'Yes (via provider)':
                provs = re.sub(r'^Processed through ', '', r['entry']).split(' (')[0]; tag = f"processed via {provs}, not in the sheet"
            elif r['on'] == 'In catalog, other countries': tag = 'in Yuno catalog for other countries only'
            items.append(f"{r['name']} [{tag}]")
        if items: parts.append(f"{rel}: " + '; '.join(items))
    print(f"**{c}** · " + ' | '.join(parts))
