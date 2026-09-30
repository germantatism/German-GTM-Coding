# -*- coding: utf-8 -*-
"""Build 'Propuesta - Línea Directa + Yuno' on the Drive copy of the Palco deck (Slides API, service account).
Usage: python3 build_ld.py dry -> simulate, report missing ids and forbidden tokens | python3 build_ld.py -> apply + thumbnails"""
import sys, json
from common import *
from content_ld import T, DELETE, DELETE_CHARS, MOVE, LOGO, LOGOS, FORBID
DRY = 'dry' in sys.argv
s = svc(); P = s.presentations().get(presentationId=PID).execute()
json.dump(P, open(f'{WORK}/deck_before_build.json', 'w'))
idx = {}; slide_of = {}
for n, sl in enumerate(P['slides'], 1):
    for el, tr in elements(sl): idx[el['objectId']] = (el, tr); slide_of[el['objectId']] = n
need = list(T) + DELETE + list(DELETE_CHARS) + list(MOVE) + [l[0] for l in LOGOS]
print('MISSING ids:', [k for k in need if k not in idx])
reqs = []; sim = {}
for oid, markup in T.items():
    r, text = fmt_requests(idx[oid][0], markup); reqs += r; sim[oid] = text
for oid, (a, b) in DELETE_CHARS.items():
    t = text_of(idx[oid][0]); sim[oid] = t[:a] + t[b:]
    reqs.append({'deleteText': {'objectId': oid, 'textRange': {'type': 'FIXED_RANGE', 'startIndex': a, 'endIndex': b}}})
for oid in DELETE: reqs.append({'deleteObject': {'objectId': oid}}); sim[oid] = ''
for oid, (x, y, w, h) in MOVE.items():
    el, tr = idx[oid]; x0, y0, w0, h0 = geom(el, tr)
    reqs.append(box_req(el, x0 if x is None else x, y0 if y is None else y, w0 if w is None else w, h0 if h is None else h))
for old, new, (x, y, w, h) in LOGOS:
    page = P['slides'][slide_of[old] - 1]['objectId']
    reqs.append({'deleteObject': {'objectId': old}})
    reqs.append({'createImage': {'objectId': new, 'url': LOGO, 'elementProperties': {'pageObjectId': page,
        'size': {'width': {'magnitude': w * 12700, 'unit': 'EMU'}, 'height': {'magnitude': h * 12700, 'unit': 'EMU'}},
        'transform': {'scaleX': 1, 'scaleY': 1, 'shearX': 0, 'shearY': 0, 'translateX': x * 12700, 'translateY': y * 12700, 'unit': 'EMU'}}}})
bad = []
for n, sl in enumerate(P['slides'], 1):
    if sl['objectId'] == 'ld_methods': continue          # built by build_methods.py
    for el, tr in elements(sl):
        t = text_of(el).strip()
        if not t: continue
        chk = sim.get(el['objectId'], t)
        for f in FORBID:
            if f in chk: bad.append((n, el['objectId'], f, chk[:70]))
print('FORBIDDEN tokens in final text:'); [print('  S%d %s [%s] %s' % b) for b in bad]
print('requests:', len(reqs), '| text elements replaced:', len(sim))
if DRY: print('dry run, nothing changed'); sys.exit(0)
run(s, PID, reqs, label='linea directa build')
Q = s.presentations().get(presentationId=PID).execute(); json.dump(Q, open(f'{WORK}/deck_after_build.json', 'w'))
changed = sorted({slide_of[o] for o in list(sim) + list(MOVE)} | {1, len(Q['slides'])})
thumbs(s, Q, changed, 'after'); print('thumbs:', changed)
