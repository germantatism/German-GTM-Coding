# -*- coding: utf-8 -*-
"""German, 15-oct-2026: "haz un poquito más conservador todo el business case". model.py now carries +8 / +16 pts (was +10 / +20),
+2% / +4% (was +2% / +5%), 20 / 40 bps (was 25 / 50) and 2 to 3 integrations (was 3 to 4). This re-applies every S13 / S14 text
from content_luni.T (single source of truth) so the slides follow the model. Usage: python3 fix4_bc_conservative.py [dry]"""
import sys, json
from common import *
from model import *
from content_luni import T, B
assert L1_PTS == (0.08, 0.16), 'model.py not on the conservative assumptions'
DRY = 'dry' in sys.argv
s = svc(); P = s.presentations().get(presentationId=PID).execute()
json.dump(P, open(f'{WORK}/deck_before_fix4.json', 'w'))
idx = {el['objectId']: (el, tr) for sl in P['slides'] for el, tr in elements(sl)}
keys = [k for k in T if k.startswith(B) and k in idx]
missing = [k for k in T if k.startswith(B) and k not in idx]
reqs = []
for k in keys: reqs.extend(fmt_requests(idx[k][0], T[k])[0])
print('S13/S14 elements:', len(keys), '| missing:', missing, '| requests:', len(reqs))
print(f'totals {T[B+"2483"]} / {T[B+"2495"]} / {T[B+"2508"]} | L1 {T[B+"1972"]} / {T[B+"1984"]} | headline: {T[B+"2704"]}')
if DRY: sys.exit(0)
run(s, PID, reqs, label='fix4 bc conservative')
Q = s.presentations().get(presentationId=PID).execute(); json.dump(Q, open(f'{WORK}/deck_after_fix4.json', 'w'))
ids = [x['objectId'] for x in Q['slides']]
thumbs(s, Q, [ids.index(B + '1468') + 1, ids.index(B + '1995') + 1], 'fix4'); print('thumbs done')
