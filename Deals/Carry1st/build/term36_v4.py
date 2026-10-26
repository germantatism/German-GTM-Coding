# -*- coding: utf-8 -*-
"""One-off (26 Oct 2026): German asked to state a 36-month contract term on v4 slide 12. It leads the footer line, in bold; nothing else moves.
Usage: python3 term36_v4.py"""
import warnings; warnings.filterwarnings('ignore')
import gs_engine as E
PID, SLIDE, OID = '17-dirMLGwFpXBgknXjkvt95rvDW1zNJ7QiaXDvWI8yA', 'n22r1_g3f77215683c_2_2968', 'n22r1_e098'
LEAD = '36-month contract term.'
TEXT = LEAD + ' Minimum and platform fee billed monthly. Usage billed monthly in arrears on successful transactions, net 30. Rates locked, tranches reviewed annually. All figures in USD.'
deck = E.Deck(PID); P = deck.fetch()
sl = next(s for s in P['slides'] if s['objectId'] == SLIDE)
el, tr = next((e, t) for e, t in E.elements(sl) if e['objectId'] == OID)
x, y, w, h = E.geom(el, tr)
n = E.wrap_count(TEXT, 6.5, w - 2 * E.INSET_X, False); assert n == 1, n; print('footer lines:', n)
reqs = E.replace_text_requests(el, TEXT)
reqs.append({'updateTextStyle': {'objectId': OID, 'style': {'bold': True}, 'fields': 'bold', 'textRange': {'type': 'FIXED_RANGE', 'startIndex': 0, 'endIndex': len(LEAD)}}})
deck.run(reqs, '36-month term in footer'); print('ok')
