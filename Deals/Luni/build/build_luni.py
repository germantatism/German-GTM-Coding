# -*- coding: utf-8 -*-
"""Build 'Proposal - Luni + Yuno' on the Drive copy of the FlightHub deck (Slides API, service account).
Usage: python3 build_luni.py dry -> simulate, report missing ids and forbidden tokens | python3 build_luni.py -> apply + thumbnails"""
import sys, json
from common import *
from content_luni import T, T2, DUP, DELETE, SLIDES_DELETE, MOVE, LOGO, LOGOS, FORBID, RANGES, RANGES_SLIDE
DRY = 'dry' in sys.argv
s = svc(); P = s.presentations().get(presentationId=PID).execute()
print('deck:', P.get('title'), '| slides:', len(P['slides']))
json.dump(P, open(f'{WORK}/deck_before_build.json', 'w'))
idx = {}; slide_of = {}
for n, sl in enumerate(P['slides'], 1):
    for el, tr in elements(sl): idx[el['objectId']] = (el, tr); slide_of[el['objectId']] = n
need = list(T) + list(T2) + DELETE + list(MOVE) + [l[0] for l in LOGOS] + [d[0] for d in DUP.values()]
print('MISSING ids:', [k for k in need if k not in idx])
print('MISSING slides:', [k for k in SLIDES_DELETE if k not in [x['objectId'] for x in P['slides']]])
reqs = []; sim = {}
# 1. duplicates (same slide as the source), then their text + box
for new, (src, box, markup) in DUP.items():
    reqs.append({'duplicateObject': {'objectId': src, 'objectIds': {src: new}}})
    el, tr = idx[src]
    if markup is not None:
        r, text = fmt_requests(el, markup, oid=new); reqs += r; sim[new] = text
    reqs.append(box_req(el, *box, oid=new))
# 2. texts
for oid, markup in T.items():
    r, text = fmt_requests(idx[oid][0], markup); reqs += r; sim[oid] = text
for oid, (head, tail) in T2.items():
    r, text = two_run(idx[oid][0], head, tail); reqs += r; sim[oid] = text
# 3. moves
for oid, (x, y, w, h) in MOVE.items():
    el, tr = idx[oid]; x0, y0, w0, h0 = geom(el, tr)
    reqs.append(box_req(el, x0 if x is None else x, y0 if y is None else y, w0 if w is None else w, h0 if h is None else h))
# 4. logos
for old, new, (x, y, w, h) in LOGOS:
    page = P['slides'][slide_of[old] - 1]['objectId']
    reqs.append({'deleteObject': {'objectId': old}})
    reqs.append(image_req(new, page, LOGO, x, y, w, h))
# 4b. appendix ranges without en-dashes
for a, z in RANGES: reqs.append({'replaceAllText': {'containsText': {'text': a, 'matchCase': True}, 'replaceText': z, 'pageObjectIds': [RANGES_SLIDE]}})
# 5. deletes (elements, then slides)
for oid in DELETE: reqs.append({'deleteObject': {'objectId': oid}}); sim[oid] = ''
for sid in SLIDES_DELETE: reqs.append({'deleteObject': {'objectId': sid}})
# scan final text for forbidden tokens (skipping the slides that go away)
bad = []
for n, sl in enumerate(P['slides'], 1):
    if sl['objectId'] in SLIDES_DELETE: continue
    for el, tr in elements(sl):
        t = text_of(el).strip()
        if not t: continue
        chk = sim.get(el['objectId'], t)
        for f in FORBID:
            if f in chk: bad.append((n, el['objectId'], f, chk[:80]))
print('FORBIDDEN tokens in final text:'); [print('  S%d %s [%s] %s' % b) for b in bad]
print('requests:', len(reqs), '| text elements replaced:', len(sim))
if DRY: print('dry run, nothing changed'); sys.exit(0)
run(s, PID, reqs, label='luni build')
Q = s.presentations().get(presentationId=PID).execute(); json.dump(Q, open(f'{WORK}/deck_after_build.json', 'w'))
newmap = {sl['objectId']: n for n, sl in enumerate(Q['slides'], 1)}
changed = sorted({newmap[P['slides'][slide_of[o] - 1]['objectId']] for o in list(T) + list(T2) + list(MOVE) + DELETE + [l[0] for l in LOGOS]
                  if P['slides'][slide_of[o] - 1]['objectId'] in newmap})
thumbs(s, Q, changed, 'after'); print('slides now:', len(Q['slides']), '| thumbs:', changed)
