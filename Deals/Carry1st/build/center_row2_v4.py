# -*- coding: utf-8 -*-
"""One-off (26 Oct 2026): after deleting SpaceX from the v4 logo wall (slide 16), row 2 has four logos; centre each on the midpoint between two
row-1 column centres so the row reads as intentional. Usage: python3 center_row2_v4.py"""
import warnings; warnings.filterwarnings('ignore')
import gs_engine as E
deck = E.Deck('17-dirMLGwFpXBgknXjkvt95rvDW1zNJ7QiaXDvWI8yA'); P = deck.fetch()
sl = P['slides'][-1]
g = {el['objectId']: (el, E.geom(el, tr)) for el, tr in E.elements(sl) if 'image' in el}
row1 = ['n16_g3f769a0f446_0_8223', 'n16_g3f769a0f446_0_8224', 'n16_g3f769a0f446_0_8225', 'n16_g3f76accd9b2_0_2', 'n16_g3f769a0f446_0_8227']
row2 = ['n16_g3f76accd9b2_0_5', 'n16_g3f769a0f446_0_8230', 'n16_g3f769a0f446_0_8231', 'n16_g3f769a0f446_0_8232']
Y0 = {'n16_g3f76accd9b2_0_5': 224.4, 'n16_g3f769a0f446_0_8230': 220.6, 'n16_g3f769a0f446_0_8231': 225.0, 'n16_g3f769a0f446_0_8232': 225.0}  # template y
c1 = [g[o][1][0] + g[o][1][2] / 2 for o in row1]
mids = [(a + b) / 2 for a, b in zip(c1, c1[1:])]
reqs = []
for oid, cx in zip(row2, mids):
    el, (x, y, w, h) = g[oid]
    # some logos sit in groups, so move by a page-space delta (RELATIVE) instead of writing an absolute transform
    dx, dy = (cx - w / 2) - x, Y0[oid] - y
    reqs.append({'updatePageElementTransform': {'objectId': oid, 'applyMode': 'RELATIVE', 'transform': {'scaleX': 1, 'scaleY': 1, 'shearX': 0, 'shearY': 0,
                 'translateX': E.emu(dx), 'translateY': E.emu(dy), 'unit': 'EMU'}}})
    print(oid, f'x {x:.1f} y {y:.1f} -> centre {cx:.1f} y {Y0[oid]}')
deck.run(reqs, 'centre logo row 2'); print('ok')
