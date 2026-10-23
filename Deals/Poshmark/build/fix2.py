# -*- coding: utf-8 -*-
"""Fix pass 2 (23 Oct 2026): slide 8 tax_id pills to the front (the row background strip was covering them);
cover wordmark moved left so the lockup reads 'yuno + POSHMARK' without the gap left by the OnlyFans icon."""
import json, time
import gs_lib as g
from build_vault_deck import DECK, S, LOGO_ASPECT
s = g.svc(); pid = DECK
P = s.presentations().get(presentationId=pid).execute()
json.dump(P, open('backup_poshmark_prefix2_' + time.strftime('%H%M%S') + '.json', 'w'))
R = []
for oid in ('posh_taxid_pii', 'posh_taxid_tok'):
    R.append({'updatePageElementsZOrder': {'pageElementObjectIds': [oid], 'operation': 'BRING_TO_FRONT'}})
# cover: logo box was x=157 (after the OnlyFans icon); the '+' ends near x=108, so start the wordmark at 118
cov = g.slide(P, S['cover'])
e = next(e for e in g.walk(cov['pageElements']) if e['objectId'] == 'posh_cover_logo')
tr = e['transform']
R.append({'updatePageElementTransform': {'objectId': 'posh_cover_logo', 'applyMode': 'ABSOLUTE', 'transform': {
    'scaleX': tr.get('scaleX', 1), 'scaleY': tr.get('scaleY', 1), 'shearX': 0, 'shearY': 0,
    'translateX': 118 * g.PT, 'translateY': tr['translateY'], 'unit': 'EMU'}}})
g.run(s, pid, R, 'fix2')
print('fix2 done')
