# -*- coding: utf-8 -*-
"""One-off (26 Oct 2026): German: put the SpaceX logo back and never remove it. Re-creates the logo on the v4 logo wall (slide 16) from the
same element in v2 (1D1HwXY1...), and moves row 2 back to its template positions. Usage: python3 restore_spacex_v4.py"""
import warnings; warnings.filterwarnings('ignore')
import gs_engine as E
SRC, PID, OID = '1D1HwXY1TRczJxtqDKWi_JgJT-cKqSXhuH-6rRn1BIQ4', '17-dirMLGwFpXBgknXjkvt95rvDW1zNJ7QiaXDvWI8yA', 'h1b68c47cebe3197d_10_0'
src_sl = E.Deck(SRC).fetch()['slides'][-1]
src = next(el for el, _ in E.elements(src_sl) if el['objectId'] == OID)
deck = E.Deck(PID); P = deck.fetch(); sl = P['slides'][-1]
g = {el['objectId']: E.geom(el, tr) for el, tr in E.elements(sl)}
assert OID not in g
HOME = {'n16_g3f76accd9b2_0_5': (196.3, 224.4), 'n16_g3f769a0f446_0_8230': (305.7, 220.6),
        'n16_g3f769a0f446_0_8231': (445.1, 225.0), 'n16_g3f769a0f446_0_8232': (583.3, 225.0)}   # template positions (pre-QA dump)
reqs = [{'createImage': {'objectId': OID, 'url': src['image']['contentUrl'],
         'elementProperties': {'pageObjectId': sl['objectId'], 'size': src['size'], 'transform': src['transform']}}}]
for oid, (hx, hy) in HOME.items():
    x, y, w, h = g[oid]
    reqs.append({'updatePageElementTransform': {'objectId': oid, 'applyMode': 'RELATIVE', 'transform': {'scaleX': 1, 'scaleY': 1, 'shearX': 0, 'shearY': 0,
                 'translateX': E.emu(hx - x), 'translateY': E.emu(hy - y), 'unit': 'EMU'}}})
deck.run(reqs, 'restore SpaceX logo and row 2'); print('ok')
