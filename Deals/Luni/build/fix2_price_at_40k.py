# -*- coding: utf-8 -*-
"""German, 15-oct-2026 (after seeing the slide): remove the 'AS APPROVALS CLIMB' scenario block from the left card and show the
'What it means for Luni' table at 40,000 successful transactions (both tranches in use). Left card = two tranches + note.
Usage: python3 fix2_price_at_40k.py [dry]"""
import sys, json
from common import *
from model import *
DRY = 'dry' in sys.argv
R = 'g3f8f3224ab6_2_'
s = svc(); P = s.presentations().get(presentationId=PID).execute()
json.dump(P, open(f'{WORK}/deck_before_fix2.json', 'w'))
idx = {el['objectId']: (el, tr) for sl in P['slides'] for el, tr in elements(sl)}
reqs = []
def txt(oid, markup, src=None): reqs.extend(fmt_requests(idx[src or oid][0], markup, oid=oid)[0])
def put(oid, x=None, y=None, w=None, h=None, src=None):
    el, tr = idx[src or oid]; x0, y0, w0, h0 = geom(el, tr)
    reqs.append(box_req(el, x0 if x is None else x, y0 if y is None else y, w0 if w is None else w, h0 if h is None else h, oid=oid))
def rm(*oids):
    for o in oids:
        if o in idx: reqs.append({'deleteObject': {'objectId': o}})
# left card: drop the scenario block, note moves up under tranche 2
rm('lu_h1', 'lu_h2', 'lu_sep0', *[R + str(n) for n in range(129, 140)])
put(R + '140', y=212.0, h=24.8); put(R + '141', y=216.5, h=18.0)
# right card at 40,000 successful: two tranche rows in the space of the old single row
TX = CUT2; v1, v2 = CUT1 * P1, (CUT2 - CUT1) * P2; var_, total = monthly(TX)
txt(R + '177', f'At {TX:,} successful transactions / month, with both tranches in use')
txt(R + '182', f'Tranche 1: {CUT1:,} trx at ${P1:.2f}'); txt(R + '183', f'${v1:,.0f}'); txt(R + '184', f'${v1*12:,.0f}')
for o in ('182', '183', '184'): put(R + o, h=12.0)
for src, new in (('182', 'lu_r2_lbl'), ('183', 'lu_r2_m'), ('184', 'lu_r2_a')):
    reqs.append({'duplicateObject': {'objectId': R + src, 'objectIds': {R + src: new}}})
txt('lu_r2_lbl', f'Tranche 2: {CUT2-CUT1:,} trx at ${P2:.2f}', src=R + '182'); txt('lu_r2_m', f'${v2:,.0f}', src=R + '183'); txt('lu_r2_a', f'${v2*12:,.0f}', src=R + '184')
put('lu_r2_lbl', y=151.8, h=12.0, src=R + '182'); put('lu_r2_m', y=151.8, h=12.0, src=R + '183'); put('lu_r2_a', y=151.8, h=12.0, src=R + '184')
txt(R + '187', f'${var_:,.0f}'); txt(R + '188', f'${var_*12:,.0f}')
txt(R + '195', f'${total:,.0f}'); txt(R + '196', f'${total*12:,.0f}')
txt(R + '197', f'${total/TX:.2f}')
v0, t0 = monthly(APPROVED)
txt(R + '198', f"per successful trx, all-in at this volume. Today, at {APPROVED:,} successful ({ATTEMPTS:,} attempts at {int(APPROVAL*100)}%), the bill is ${t0:,.0f} a month; the platform fee is most of it, so it barely moves as approvals climb.")
print('requests:', len(reqs), f'| at {TX:,}: tranches ${v1:,.0f} + ${v2:,.0f} = ${var_:,.0f}, total ${total:,.0f}/mo ${total*12:,.0f}/yr, ${total/TX:.4f} per trx | today ${t0:,.0f}')
if DRY: sys.exit(0)
run(s, PID, reqs, label='fix2 price at 40k')
Q = s.presentations().get(presentationId=PID).execute(); json.dump(Q, open(f'{WORK}/deck_after_fix2.json', 'w'))
n = [x['objectId'] for x in Q['slides']].index('h4623285e90de4e9f_0_118') + 1
thumbs(s, Q, [n], 'fix2'); print('thumb slide', n)
