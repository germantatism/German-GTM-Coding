# -*- coding: utf-8 -*-
"""One-off (26 Oct 2026): German found the dark summary box on v4 slide 12 hard to read; plain-language rewrite, same box. Usage: python3 simplify_box_v4.py"""
import warnings; warnings.filterwarnings('ignore')
import gs_engine as E
PID, SLIDE, OID = '17-dirMLGwFpXBgknXjkvt95rvDW1zNJ7QiaXDvWI8yA', 'n22r1_g3f77215683c_2_2968', 'simp_e022'
TEXT = 'First 6 months: $2,500 a month covers your first $500K of sales. From month 7: $7,500 a month. Sales above $500K pay the tranche rates from month 1.'
assert E.wrap_count(TEXT, 8.5, 240.4, True) <= 3
deck = E.Deck(PID); P = deck.fetch()
sl = next(s for s in P['slides'] if s['objectId'] == SLIDE)
el = next(e for e, _ in E.elements(sl) if e['objectId'] == OID)
deck.run(E.replace_text_requests(el, TEXT), 'plain-language summary box'); print('ok')
