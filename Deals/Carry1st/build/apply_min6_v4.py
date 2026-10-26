# -*- coding: utf-8 -*-
"""One-off (26 Oct 2026): on the v4 copy of the v3 ramp deck, replace the platform-fee ramp on the proposal slide with the scenario German set
after the 26 Oct call with Cordel: months 1 to 6 no platform fee, the first $500K of monthly sales at 50 bps with a $2,500 monthly minimum;
from month 7 a $7,500 platform fee that includes the first $500K (0 bps). The 40/30/20/10 ladder above $500K is unchanged, so the run rate is
unchanged ($21,000 a month at $4.5M). Pending Justo's OK. Usage: python3 apply_min6_v4.py [dry]"""
import sys, warnings; warnings.filterwarnings('ignore')
import gs_engine as E
PID = '17-dirMLGwFpXBgknXjkvt95rvDW1zNJ7QiaXDvWI8yA'   # Carry1st + Yuno_Oct 2026v4 (6-month minimum), copy of v3 1qmkK4eF... made 26 Oct 2026
SLIDE = 'n22r1_g3f77215683c_2_2968'
DRY = 'dry' in sys.argv
TXT = {
 'n22r1_e002': 'A $2,500 monthly minimum for the first six months, then a platform fee and a share of sales that falls as Carry1st grows.',
 'n22r1_e004': 'Months 1 to 6: a $2,500 minimum, 50 bps on the first $500K. From month 7: $7,500 a month covering the first $500K. Same ladder above: $21,000 a month at $4.5M.',
 'simp_e004': '$2,500',
 'simp_e005': 'in months 1 to 6',
 'simp_e006': '50 bps of sales',
 'simp_e012': 'from month 7',
 'ramp_e001': 'MINIMUM FIRST, THEN THE PLATFORM FEE',
 'ramp_e010': 'Six months at a $2,500 minimum, then $7,500 a month from month 7 with the first $500K included.',
 'n22r1_e009': 'FIRST $500K',
 'n22r1_e010': '50 then 0',
 'n22r1_e011': '50 bps in months 1 to 6, included from month 7',
 'n22r1_e098': 'Minimum and platform fee billed monthly. Usage billed monthly in arrears on successful transactions, net 30. Rates locked, tranches reviewed annually. All figures in USD.',
}
OLD_CELLS = [f'ramp_e{n:03d}' for n in range(2, 10)]           # the 4-month ramp cells from v3
DROP = ['simp_e021', 'simp_e022', 'simp_e023']                 # 'what it means' prose: the card keeps only the three you-pay tiles
CARD, CARD_H = 'n22r1_e054', 152.0                             # right card shrinks to the tiles (was 252.4)
NEW_CELLS = [('MONTHS 1 TO 6', '$2,500 min.'), ('MONTH 7+', '$7,500')]
NOTES = ("The proposal in one slide. For the first six months there is no platform fee: the first $500K of monthly sales is billed at 50 basis "
 "points with a $2,500 monthly minimum, so Carry1st commits to the volume, not to a fixed cost, while it sets its baseline over Black Friday, "
 "December and the first quarter. From month 7 the platform fee is $7,500 a month and it includes the first $500K of monthly sales. Above "
 "$500K the share of sales is the same throughout: 40 basis points to $2M, 30 to $5M, 20 to $10M, 10 above, each band on the volume inside it, "
 "only on approved payments, never a fee per transaction. At $2M in months 1 to 6 Carry1st pays $8,500; from month 7, $13,500 at $2M and $21,000 "
 "at the $4.5M run rate, 47 bps of sales. Orchestration, smart routing, Monitors, the vault, the dashboard and a dedicated team are included; "
 "network tokens and 3DS are billed on usage and quoted separately.")

deck = E.Deck(PID); P = deck.fetch()
sl = next(s for s in P['slides'] if s['objectId'] == SLIDE)
pairs = E.elements(sl)
els = {el['objectId']: el for el, _ in pairs}
for k in TXT: assert k in els, k
for k in OLD_CELLS + DROP + [CARD]: assert k in els, k
# fit guard: same boxes and sizes as v3
checks = [('n22r1_e002', 20, 617, True, 2), ('n22r1_e004', 8, 662, False, 1), ('n22r1_e098', 6.5, 662, False, 2)]
for oid, size, w, b, mx in checks:
    n = E.wrap_count(TXT[oid], size, w, b); assert n <= mx, (oid, n); print(f'fit {oid}: {n} lines')
n = E.wrap_count(TXT['ramp_e010'], 7, 180.4, False); assert n <= 2, ('strip footer', n); print('fit strip footer:', n, 'lines')
reqs = []
for oid, t in TXT.items(): reqs += E.replace_text_requests(els[oid], t)
reqs += [{'deleteObject': {'objectId': o}} for o in OLD_CELLS + DROP]
t = {'scaleX': 1, 'scaleY': 1, 'shearX': 0, 'shearY': 0, 'translateX': 0, 'translateY': 0, **els[CARD]['transform']}
t['scaleY'] *= CARD_H / E.geom(els[CARD], els[CARD]['transform'])[3]
reqs += [{'updatePageElementTransform': {'objectId': CARD, 'applyMode': 'ABSOLUTE', 'transform': {**t, 'unit': 'EMU'}}}]
print('requests:', len(reqs))
if DRY: print('dry ok'); sys.exit(0)
deck.run(reqs, 'min6: texts, drop 4-month ramp cells')
# two cells instead of four in the strip (x 225.8 .. 406.2), same rows as v3
sb = E.SB(deck, SLIDE, 'min6')
X, W = 225.8, 180.4; cw = W / 2
for i, (m, v) in enumerate(NEW_CELLS):
    x = X + i * cw
    sb.text(x, 145.2, cw, 10, m, size=6.5, bold=True, color=E.GREY, ls=100)
    sb.text(x, 154.7, cw, 16, v, size=11, bold=True, color=E.BLUE, ls=100)
sb.flush('min6 strip')
deck.set_notes(SLIDE, NOTES)
# verify
P = deck.fetch(); sl = next(s for s in P['slides'] if s['objectId'] == SLIDE)
print('--- slide 12 after:')
for el, tr in E.elements(sl):
    t = E.text_of(el).strip()
    if t:
        x, y, w, h = E.geom(el, tr); print(f"  {el['objectId']:22s} y={y:6.1f} x={x:6.1f} w={w:6.1f} | {t[:110]!r}")
left = [(i+1, E.text_of(el)[:70]) for i, s in enumerate(P['slides']) for el, _ in E.elements(s)
        if any(k in E.text_of(el) for k in ('$3,000', 'month 4', '$5,500', 'ramps up'))]
print('old wording left:', left)
