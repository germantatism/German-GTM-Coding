# -*- coding: utf-8 -*-
"""Second pass after the visual review of S16: the bottom boxes overflowed (tag wrapped onto the separator, body lines wrapped onto
the next row). Shorter copy, tag = 'Pending review' on both boxes. Usage: python3 fix1_bottom_boxes.py [dry]"""
import sys, json
from common import *
DRY = 'dry' in sys.argv
R = 'g3f8f3224ab6_2_'
s = svc(); P = s.presentations().get(presentationId=PID).execute()
json.dump(P, open(f'{WORK}/deck_before_fix1.json', 'w'))
idx = {el['objectId']: (el, tr) for sl in P['slides'] for el, tr in elements(sl)}
reqs = []
def txt(oid, markup): reqs.extend(fmt_requests(idx[oid][0], markup)[0])
txt(R + '204', 'Pending review')
txt(R + '206', "Plans, trials, **smart retries on failed renewals** and past-due recovery, on Yuno's recurring billing engine.")
txt(R + '207', "Scope and pricing to be reviewed together, depending on Luni's interest. **Not included** in the totals above.")
txt(R + '212', 'One reconciliation view across **Stripe US, Stripe France, Paddle and PayPal** instead of four dashboards.')
txt(R + '213', 'Scope, timing and pricing to be reviewed together. **Not included** in the totals above.')
print('requests:', len(reqs))
if DRY: sys.exit(0)
run(s, PID, reqs, label='fix1 bottom boxes')
Q = s.presentations().get(presentationId=PID).execute(); json.dump(Q, open(f'{WORK}/deck_after_fix1.json', 'w'))
n = [x['objectId'] for x in Q['slides']].index('h4623285e90de4e9f_0_118') + 1
thumbs(s, Q, [n], 'fix1'); print('thumb slide', n)
