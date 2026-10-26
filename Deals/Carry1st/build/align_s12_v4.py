# -*- coding: utf-8 -*-
"""One-off (26 Oct 2026): align slide 12 of v4. The strip in the platform-fee card was built with SB.text (text starts at the visual x), while
the template boxes keep the 7.2 pt inset, so the strip sat 7.2 pt left of 'PLATFORM FEE' and 'WHAT IT INCLUDES'. Move it onto the card's text
column (233.0 .. 399.0 pt) and split that column in two equal cells. Usage: python3 align_s12_v4.py"""
import warnings; warnings.filterwarnings('ignore')
import gs_engine as E
PID, SLIDE = '17-dirMLGwFpXBgknXjkvt95rvDW1zNJ7QiaXDvWI8yA', 'n22r1_g3f77215683c_2_2968'
deck = E.Deck(PID); P = deck.fetch()
sl = next(s for s in P['slides'] if s['objectId'] == SLIDE)
pairs = {el['objectId']: (el, tr) for el, tr in E.elements(sl)}
hx, _, hw, _ = E.geom(*pairs['n22r1_e027'])                 # 'PLATFORM FEE' box: its text column is the target
COL_X, COL_W = hx + E.INSET_X, hw - 2 * E.INSET_X
half = COL_W / 2
FOOT = '$2,500 minimum for six months, then $7,500. Tranches above $500K apply from month 1.'
n = E.wrap_count(FOOT, 7, COL_W, False); assert n <= 2, n; print('footer lines at', round(COL_W, 1), 'pt:', n)
target = {  # objectId: (visual text x, visual text width)
 'ramp_e001': (COL_X, COL_W), 'ramp_e010': (COL_X, COL_W),
 'min6_e001': (COL_X, half), 'min6_e002': (COL_X, half),
 'min6_e003': (COL_X + half, half), 'min6_e004': (COL_X + half, half),
}
reqs = E.replace_text_requests(pairs['ramp_e010'][0], FOOT)
for oid, (x, w) in target.items():
    el, tr = pairs[oid]
    base_w = el['size']['width']['magnitude']
    t = {'scaleX': 1, 'scaleY': 1, 'shearX': 0, 'shearY': 0, 'translateX': 0, 'translateY': 0, **el['transform']}
    t['translateX'] = E.emu(x - E.INSET_X); t['scaleX'] = E.emu(w + 2 * E.INSET_X) / base_w
    reqs.append({'updatePageElementTransform': {'objectId': oid, 'applyMode': 'ABSOLUTE', 'transform': {**t, 'unit': 'EMU'}}})
deck.run(reqs, 'align strip to card text column')
P = deck.fetch(); sl = next(s for s in P['slides'] if s['objectId'] == SLIDE)
for el, tr in E.elements(sl):
    if el['objectId'] in target or el['objectId'] in ('n22r1_e027', 'n22r1_e031'):
        x, y, w, h = E.geom(el, tr); print(f"{el['objectId']:12s} text x={x + E.INSET_X:6.1f} w={w - 2 * E.INSET_X:6.1f} | {E.text_of(el).strip()[:60]!r}")
