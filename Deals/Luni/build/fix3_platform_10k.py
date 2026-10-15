# -*- coding: utf-8 -*-
"""German, 15-oct-2026: platform fee down to $10,000. Touches the pricing slide (header, commercial terms, right card at 40,000,
today's bill in the sub-line) and the cost line on the Total Impact slide. model.py already carries PLATFORM = 10_000.
Usage: python3 fix3_platform_10k.py [dry]"""
import sys, json
from common import *
from model import *
assert PLATFORM == 10_000, 'set PLATFORM = 10_000 in model.py first'
DRY = 'dry' in sys.argv
R = 'g3f8f3224ab6_2_'; B = 'g3fa1128e0cb_1_'
s = svc(); P = s.presentations().get(presentationId=PID).execute()
json.dump(P, open(f'{WORK}/deck_before_fix3.json', 'w'))
idx = {el['objectId']: (el, tr) for sl in P['slides'] for el, tr in elements(sl)}
reqs = []
def txt(oid, markup): reqs.extend(fmt_requests(idx[oid][0], markup)[0])
TX = CUT2; var_, total = monthly(TX); v0, t0 = monthly(APPROVED); v60, t60 = monthly(SCEN['60%'])
txt(R + '114', f'A rate per successful transaction of {int(P1*100)} cents on the first {CUT1:,} a month and {int(P2*100)} cents on the next {CUT2-CUT1:,}, with orchestration, smart routing, monitors and the PCI token vault included, on a flat platform fee of **${PLATFORM:,} a month**. You are charged only on transactions that get approved.')
txt(R + '173', f'${PLATFORM:,} / month flat')
txt(R + '191', f'${PLATFORM:,}'); txt(R + '192', f'${PLATFORM*12:,}')
txt(R + '195', f'${total:,.0f}'); txt(R + '196', f'${total*12:,.0f}')
txt(R + '197', f'${total/TX:.2f}')
txt(R + '198', f"per successful trx, all-in at this volume. Today, at {APPROVED:,} successful ({ATTEMPTS:,} attempts at {int(APPROVAL*100)}%), the bill is ${t0:,.0f} a month; the platform fee is most of it, so it barely moves as approvals climb.")
txt(B + '2512', f'of average identifiable **annual value** across the four levers, within a {T(cons)} to {T(opt)} range, on {ATTEMPTS:,} monthly attempts at an ${TICKET} ticket, against about ${t0*12/1e3:.0f}K to ${t60*12/1e3:.0f}K a year on the proposal that follows.')
print('requests:', len(reqs), f'| at {TX:,}: ${var_:,.0f} + ${PLATFORM:,} = ${total:,.0f}/mo ${total*12:,.0f}/yr ${total/TX:.4f}/trx | today ${t0:,.0f}/mo ${t0*12:,.0f}/yr | 60% ${t60*12:,.0f}/yr')
if DRY: sys.exit(0)
run(s, PID, reqs, label='fix3 platform 10k')
Q = s.presentations().get(presentationId=PID).execute(); json.dump(Q, open(f'{WORK}/deck_after_fix3.json', 'w'))
ids = [x['objectId'] for x in Q['slides']]
thumbs(s, Q, [ids.index('h4623285e90de4e9f_0_118') + 1, ids.index(B + '1995') + 1], 'fix3'); print('thumbs done')
