# -*- coding: utf-8 -*-
"""One-off (26 Oct 2026): German asked to make explicit on v4 slide 12 that the tranches are marginal (each rate only on the sales inside its
band; at $3M it is not 30 bps on all $3M). Rewrites the grey note in the transaction-fee card and the card subtitle. Usage: python3 clarify_bands_v4.py [dry]"""
import sys, warnings; warnings.filterwarnings('ignore')
import gs_engine as E
PID, SLIDE = '17-dirMLGwFpXBgknXjkvt95rvDW1zNJ7QiaXDvWI8yA', 'n22r1_g3f77215683c_2_2968'
TXT = {
 'n22r1_e007': "Above $500K, from month 1. Each rate applies only to the sales inside its band",
 'n22r1_e025': "Example at $3M: 40 bps on $500K to $2M and 30 bps on $2M to $3M, never 30 bps on all $3M. No setup fee, no fee per transaction, declines not billed.",
}
deck = E.Deck(PID); P = deck.fetch()
sl = next(s for s in P['slides'] if s['objectId'] == SLIDE)
pairs = {el['objectId']: (el, tr) for el, tr in E.elements(sl)}
for oid, t in TXT.items():
    el, tr = pairs[oid]; x, y, w, h = E.geom(el, tr)
    run = next(te['textRun']['style'] for te in el['shape']['text']['textElements'] if 'textRun' in te)
    size = run.get('fontSize', {}).get('magnitude', 8); bold = run.get('bold', False)
    old = E.wrap_count(E.text_of(el).strip(), size, w - 2 * E.INSET_X, bold); new = E.wrap_count(t, size, w - 2 * E.INSET_X, bold)
    print(f'{oid}: {size}pt, lines old {old} new {new}'); assert new <= old, (oid, new, old)
if 'dry' in sys.argv: sys.exit(0)
reqs = []
for oid, t in TXT.items(): reqs += E.replace_text_requests(pairs[oid][0], t)
deck.run(reqs, 'marginal bands made explicit'); print('ok')
