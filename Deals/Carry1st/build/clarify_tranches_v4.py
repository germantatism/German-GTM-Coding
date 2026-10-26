# -*- coding: utf-8 -*-
"""One-off (26 Oct 2026): German flagged that the tranches above $500K apply from month 1 (e.g. $3M in month 2 already reaches tranche 2),
so the v4 slide 12 must not read as if the $2,500 minimum were all Carry1st pays in months 1 to 6. Text-only edit. Usage: python3 clarify_tranches_v4.py"""
import warnings; warnings.filterwarnings('ignore')
import gs_engine as E
PID, SLIDE = '17-dirMLGwFpXBgknXjkvt95rvDW1zNJ7QiaXDvWI8yA', 'n22r1_g3f77215683c_2_2968'
TXT = {
 'ramp_e010': '$2,500 minimum for six months, then $7,500 a month. Tranches above $500K apply from month 1.',
 'simp_e022': 'A $2,500 minimum for six months, then $7,500 a month. The tranches above $500K apply from month 1, and the rate falls as Carry1st grows.',
 'n22r1_e007': "A share of the month's sales above $500K, from month 1, pooled across the five markets",
}
FIT = {'ramp_e010': (7, 180.4, False, 2), 'simp_e022': (8.5, 240.4, True, 3), 'n22r1_e007': (8, 168.4, False, 2)}
NOTES_ADD = (" The tranches apply from month 1: if Carry1st sells $3M in month 2, it pays the $2,500 on the first $500K, 40 bps on $500K to $2M "
 "($6,000) and 30 bps on $2M to $3M ($3,000), $11,500 in total.")
for k, (sz, w, b, mx) in FIT.items():
    n = E.wrap_count(TXT[k], sz, w, b); assert n <= mx, (k, n); print('fit', k, n)
deck = E.Deck(PID); P = deck.fetch()
sl = next(s for s in P['slides'] if s['objectId'] == SLIDE)
els = {el['objectId']: el for el, _ in E.elements(sl)}
reqs = []
for k, t in TXT.items(): reqs += E.replace_text_requests(els[k], t)
deck.run(reqs, 'clarify tranches from month 1')
notes = E.text_of(next(el for el in sl['slideProperties']['notesPage']['pageElements'] if 'shape' in el and E.text_of(el).strip())).strip()
if 'month 2' not in notes: deck.set_notes(SLIDE, notes + NOTES_ADD)
print('ok')
