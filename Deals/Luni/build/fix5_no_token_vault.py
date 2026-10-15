# -*- coding: utf-8 -*-
"""German, 15-oct-2026: "quita el PCI token vault de lo que incluye el fee". Removes the 'PCI token vault · Included' row from
'What the rate covers' (the two rows below move up one slot) and drops it from the header sentence. Usage: python3 fix5_no_token_vault.py [dry]"""
import sys, json
from common import *
from model import *
DRY = 'dry' in sys.argv
R = 'g3f8f3224ab6_2_'
s = svc(); P = s.presentations().get(presentationId=PID).execute()
json.dump(P, open(f'{WORK}/deck_before_fix5.json', 'w'))
idx = {el['objectId']: (el, tr) for sl in P['slides'] for el, tr in elements(sl)}
reqs = []
def txt(oid, markup): reqs.extend(fmt_requests(idx[oid][0], markup)[0])
def put(oid, x=None, y=None, w=None, h=None):
    el, tr = idx[oid]; x0, y0, w0, h0 = geom(el, tr)
    reqs.append(box_req(el, x0 if x is None else x, y0 if y is None else y, w0 if w is None else w, h0 if h is None else h))
txt(R + '114', f'A rate per successful transaction of {int(P1*100)} cents on the first {CUT1:,} a month and {int(P2*100)} cents on the next {CUT2-CUT1:,}, with orchestration, smart routing and monitors included, on a flat platform fee of **${PLATFORM:,} a month**. You are charged only on transactions that get approved.')
# row 'PCI token vault' (label 163, value 164) and the separator under it (162) go; Dashboard and Account team rows move up one slot
for o in ('163', '164', '162'): reqs.append({'deleteObject': {'objectId': R + o}})
put(R + '166', y=208.4); put(R + '167', y=208.4)
put(R + '165', y=220.5)
put(R + '168', y=223.4); put(R + '169', y=223.4)
print('requests:', len(reqs))
if DRY: sys.exit(0)
run(s, PID, reqs, label='fix5 no token vault')
Q = s.presentations().get(presentationId=PID).execute(); json.dump(Q, open(f'{WORK}/deck_after_fix5.json', 'w'))
n = [x['objectId'] for x in Q['slides']].index('h4623285e90de4e9f_0_118') + 1
thumbs(s, Q, [n], 'fix5'); print('thumb slide', n)
