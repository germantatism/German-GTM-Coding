# -*- coding: utf-8 -*-
"""One-off (23 Oct 2026): on the v3 copy of the short deck, replace the flat $7,500 platform fee on the proposal slide with the launch ramp
German dictated: $3,000 month 1, $4,000 month 2, $5,500 month 3, $7,500 from month 4 (pricing v5, pending Justo's OK). Everything else on the
slide (tranche ladder, included $500K block, tiles at $2M and $4.5M) is unchanged. Usage: python3 apply_ramp_v3.py [dry]"""
import sys, warnings; warnings.filterwarnings('ignore')
import gs_engine as E
PID = '1qmkK4eFBaq_Hsp_EA3r-QngFNJp3XIupHUrJt2gPfqo'   # Carry1st + Yuno_Oct 2026v3 (ramp), copy of 1D1HwXY1... made 23 Oct 2026
SLIDE = 'n22r1_g3f77215683c_2_2968'
DRY = 'dry' in sys.argv
RAMP = [('MONTH 1', '$3,000'), ('MONTH 2', '$4,000'), ('MONTH 3', '$5,500'), ('MONTH 4+', '$7,500')]
TXT = {
 'n22r1_e002': 'A platform fee that ramps up over the first three months, then a share of sales that falls as Carry1st grows.',
 'n22r1_e004': 'A platform fee rising from $3,000 in month 1 to $7,500 from month 4, covering the first $500K of monthly sales, plus a share of sales above it: $21,000 a month at $4.5M, 47 bps.',
 'simp_e004': '$3,000',
 'simp_e005': 'in month 1',
 'simp_e006': '60 bps of sales',
 'simp_e022': 'The platform fee ramps with the launch, from $3,000 in month 1 to $7,500 from month 4. No fixed fee per transaction, and the rate falls as Carry1st grows.',
 'n22r1_e098': 'Platform fee billed monthly. Usage billed monthly in arrears on successful transactions, net 30. Rates locked, tranches reviewed annually as volume grows. All figures in USD.',
}
DELETE = ['n22r1_e028', 'n22r1_e029', 'n22r1_e030']           # big "$7,500", "/ month", "$90,000 a year..." sub
SHIFT = 14.0                                                  # WHAT IT INCLUDES block moves down to make room for the ramp
INCLUDES = ['n22r1_e031'] + [f'n22r1_e{n:03d}' for n in (32,33,34,35,36,37,38,39,40,41,44,45,46,47)] + ['pci_lab', 'pci_val']
NOTES = ("The proposal in one slide. The platform fee ramps up with the launch: $3,000 in month 1, $4,000 in month 2, $5,500 in month 3 and "
 "$7,500 a month from month 4, and it always covers the first $500K of monthly sales. Above that block, a share of what you sell: 40 basis points "
 "to $2M, 30 to $5M, 20 to $10M, 10 above, each band on the volume inside it, only on approved payments, never a fee per transaction. At launch "
 "you pay $3,000 and nothing else; at the $4.5M run rate the all-in cost is $21,000 a month, 47 bps of sales, under five cents on a $10 purchase. "
 "Orchestration, smart routing, Monitors, the vault, the dashboard and a dedicated team are inside the platform fee; network tokens and 3DS are "
 "billed on usage and quoted separately.")

deck = E.Deck(PID); P = deck.fetch()
sl = next(s for s in P['slides'] if s['objectId'] == SLIDE)
els = {el['objectId']: el for el, _ in E.elements(sl)}
for k in list(TXT) + DELETE + INCLUDES: assert k in els, k
# fit guard on the replaced copy (same boxes, same sizes)
checks = [('n22r1_e002', 20, 617, True, 2), ('n22r1_e004', 8, 662, False, 1), ('simp_e022', 8.5, 240.4, True, 3), ('n22r1_e098', 6.5, 662, False, 2)]
for oid, size, w, b, mx in checks:
    n = E.wrap_count(TXT[oid], size, w, b); assert n <= mx, (oid, n); print(f'fit {oid}: {n} lines')
reqs = []
for oid, t in TXT.items(): reqs += E.replace_text_requests(els[oid], t)
reqs += [{'deleteObject': {'objectId': o}} for o in DELETE]
reqs += [{'updatePageElementTransform': {'objectId': o, 'applyMode': 'RELATIVE',
          'transform': {'scaleX': 1, 'scaleY': 1, 'shearX': 0, 'shearY': 0, 'translateX': 0, 'translateY': E.emu(SHIFT), 'unit': 'EMU'}}} for o in INCLUDES]
print('text + delete + shift requests:', len(reqs))
if DRY: print('dry ok'); sys.exit(0)
deck.run(reqs, 'ramp: texts, delete flat fee, shift includes')
# the ramp strip inside the middle card (x 225.8 .. 406.2)
sb = E.SB(deck, SLIDE, 'ramp')
X, W = 225.8, 180.4; cw = W / 4
sb.text(X, 134.6, W, 10, 'RAMPS UP WITH THE LAUNCH', size=6.5, bold=True, color=E.INK, ls=100)
for i, (m, v) in enumerate(RAMP):
    x = X + i * cw
    sb.text(x, 145.2, cw, 10, m, size=6.5, bold=True, color=E.GREY, ls=100)
    sb.text(x, 154.7, cw, 16, v, size=11, bold=True, color=E.BLUE, ls=100)
sb.text(X, 172.2, W, 20, 'Then $7,500 a month from month 4, covering the first $500K of monthly sales. This is what covers the stack.', size=7, color=E.INK, ls=110)
sb.flush('ramp strip')
deck.set_notes(SLIDE, NOTES)
# verify
P = deck.fetch(); sl = next(s for s in P['slides'] if s['objectId'] == SLIDE)
print('--- slide 12 after:')
for el, tr in E.elements(sl):
    t = E.text_of(el).strip()
    if t:
        x, y, w, h = E.geom(el, tr); print(f"  {el['objectId']:14s} y={y:6.1f} x={x:6.1f} | {t[:110]!r}")
left = [(i+1, E.text_of(el)[:60]) for i, s in enumerate(P['slides']) for el, _ in E.elements(s) if '7,500 a month covering' in E.text_of(el) or '$90,000' in E.text_of(el)]
print('old wording left:', left)
