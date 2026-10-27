# -*- coding: utf-8 -*-
"""Build 'Proposal - Acebet + Yuno' on the Drive copy of the Luni deck (Slides API, service account).
Usage: python3 build_acebet.py dry -> simulate (ACEBET_PID=<Luni deck id> to dry-run before the copy is shared) | python3 build_acebet.py -> apply + thumbnails"""
import sys, json
from common import *
from content_acebet import T, T2, DUP, SHIFT, MOVE, DELETE, SLIDES_DELETE, REPLACE_ALL, FORBID
DRY = 'dry' in sys.argv
s = svc(); P = s.presentations().get(presentationId=PID).execute()
print('deck:', P.get('title'), '| slides:', len(P['slides']))
json.dump(P, open(f'{WORK}/deck_before_build.json', 'w'))
idx = {}; slide_of = {}
for n, sl in enumerate(P['slides'], 1):
    for el, tr in elements(sl): idx[el['objectId']] = (el, tr); slide_of[el['objectId']] = n
need = list(T) + list(T2) + DELETE + list(MOVE) + list(SHIFT) + [d[0] for d in DUP.values()]
print('MISSING ids:', [k for k in need if k not in idx])
print('MISSING slides:', [k for k in SLIDES_DELETE if k not in [x['objectId'] for x in P['slides']]])
reqs = []; sim = {}
def place(el, tr, x, y, w, h, oid=None):
    x0, y0, w0, h0 = geom(el, tr)
    return box_req(el, x0 if x is None else x, y0 if y is None else y, w0 if w is None else w, h0 if h is None else h, oid=oid)
for new, (src, box, markup) in DUP.items():
    el, tr = idx[src]
    reqs.append({'duplicateObject': {'objectId': src, 'objectIds': {src: new}}})
    if isinstance(markup, tuple): r, text = two_run(el, *markup, oid=new); reqs += r; sim[new] = text
    elif markup is not None: r, text = fmt_requests(el, markup, oid=new); reqs += r; sim[new] = text
    reqs.append(place(el, tr, *box, oid=new))
for oid, markup in T.items():
    r, text = fmt_requests(idx[oid][0], markup); reqs += r; sim[oid] = text
for oid, (head, tail) in T2.items():
    r, text = two_run(idx[oid][0], head, tail); reqs += r; sim[oid] = text
for oid, dy in SHIFT.items():
    el, tr = idx[oid]; x0, y0, w0, h0 = geom(el, tr); m = MOVE.get(oid, (None,) * 4)
    reqs.append(box_req(el, x0, y0 + dy, w0, m[3] or h0))
for oid, box in MOVE.items():
    if oid not in SHIFT: el, tr = idx[oid]; reqs.append(place(el, tr, *box))
for a, z in REPLACE_ALL: reqs.append({'replaceAllText': {'containsText': {'text': a, 'matchCase': True}, 'replaceText': z}})
for oid in DELETE: reqs.append({'deleteObject': {'objectId': oid}}); sim[oid] = ''
for sid in SLIDES_DELETE: reqs.append({'deleteObject': {'objectId': sid}})
bad = []
for n, sl in enumerate(P['slides'], 1):
    if sl['objectId'] in SLIDES_DELETE: continue
    for el, tr in elements(sl):
        t = text_of(el).strip()
        if not t: continue
        chk = sim.get(el['objectId'], t)
        for a, z in REPLACE_ALL: chk = chk.replace(a, z)
        for f in FORBID:
            if f in chk: bad.append((n, el['objectId'], f, chk[:90]))
for new, t in sim.items():
    if new in DUP:
        for f in FORBID:
            if f in t: bad.append((0, new, f, t[:90]))
print('FORBIDDEN tokens in final text:'); [print('  S%d %s [%s] %s' % x) for x in bad]
print('requests:', len(reqs), '| texts:', len(sim))
for k in ('g3f8f3224ab6_2_114', 'ab_grow', 'g3f8f3224ab6_2_198'): print(' ', k, '=>', sim[k])
if DRY: print('dry run, nothing changed'); sys.exit(0)
run(s, PID, reqs, label='acebet build')
Q = s.presentations().get(presentationId=PID).execute(); json.dump(Q, open(f'{WORK}/deck_after_build.json', 'w'))
thumbs(s, Q, range(1, len(Q['slides']) + 1), 'after'); print('slides now:', len(Q['slides']))
