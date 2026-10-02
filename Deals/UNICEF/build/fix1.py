# -*- coding: utf-8 -*-
"""Second pass after the visual review: S11 advantages (third one wrapped to four lines and touched the fourth), platform fee value alignment.
Usage: python3 fix1.py [dry]"""
import sys, json
from common import *
DRY = 'dry' in sys.argv
G = 'g3fb7d86b358_4_'
s = svc(); P = s.presentations().get(presentationId=PID).execute()
idx = {el['objectId']: (el, tr) for sl in P['slides'] for el, tr in elements(sl)}
reqs = []
def txt(oid, markup): reqs.extend(fmt_requests(idx[oid][0], markup)[0])
def put(oid, x=None, y=None, w=None, h=None):
    el, tr = idx[oid]; x0, y0, w0, h0 = geom(el, tr)
    reqs.append(box_req(el, x0 if x is None else x, y0 if y is None else y, w0 if w is None else w, h0 if h is None else h))
txt('g3c99cf7678e_0_28726', 'Reintentos automáticos y configurables')
for oid in ('g3c99cf7678e_0_28735', 'g3c99cf7678e_0_28722', 'g3c99cf7678e_0_28726', 'g3c99cf7678e_0_28731'): put(oid, w=114)
put(G+'665', x=362.7)
print('requests:', len(reqs))
if DRY: sys.exit(0)
run(s, PID, reqs, label='fix1')
