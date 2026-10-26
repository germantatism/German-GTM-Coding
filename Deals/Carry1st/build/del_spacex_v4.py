# -*- coding: utf-8 -*-
"""One-off (26 Oct 2026): pre-send QA on v4, the trusted-by logo wall (slide 16) still carries the SpaceX logo that CONTEXT.md forbids for this deck.
Deletes the image near x 80.7, y 229.1 (w 74.2, h 9.1) on the last slide. Usage: python3 del_spacex_v4.py [dry]"""
import sys, warnings; warnings.filterwarnings('ignore')
import gs_engine as E
deck = E.Deck('17-dirMLGwFpXBgknXjkvt95rvDW1zNJ7QiaXDvWI8yA'); P = deck.fetch()
sl = P['slides'][-1]
hits = []
for el, tr in E.elements(sl):
    if 'image' not in el: continue
    x, y, w, h = E.geom(el, tr)
    if abs(x - 80.7) < 3 and abs(y - 229.1) < 3: hits.append(el['objectId'])
    print(f"{el['objectId']:28s} x={x:6.1f} y={y:6.1f} w={w:5.1f} h={h:5.1f}")
print('match:', hits); assert len(hits) == 1
if 'dry' in sys.argv: sys.exit(0)
deck.run([{'deleteObject': {'objectId': hits[0]}}], 'delete SpaceX logo'); print('ok')
# second pass (same day): row 2 is left with four logos, so centre them between the five column centres of row 1
