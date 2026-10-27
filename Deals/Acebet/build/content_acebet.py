# -*- coding: utf-8 -*-
"""Acebet proposal: text per element ID on the Drive copy of 'Proposal - Luni + Yuno' (21 slides; business case section removed).
Markup: **x** = bold run of the original element. Numbers come from model.py.
Client data: call 27-oct-2026 (Boris, co-founder). Pricing: German, 27-oct-2026 ($10K platform, 4 tranches, ~2.5 cents average)."""
from model import *
K1 = 'g3c99cf7678e_0_'      # cover, S11, close
A = 'g3caca0138e4_0_'       # agenda, S5
R = 'g3f8f3224ab6_2_'       # pricing
H = 'h4623285e90de4e9f_0_'  # agenda item 03, footer
b = bands(TX); V, TOT = var(TX), total(TX)
c = lambda r: f'${r:.3f}'
grow = ', '.join(f'${total(t)/t:.3f} at {t:,}' for t in GROWTH[1:])
T = {
# S1 cover
K1+'1': 'POWERING SEAMLESS GLOBAL MONEY MOVEMENT FOR ACEBET',
# S2 agenda: business case out, proposal becomes 02
A+'5': 'PROPOSAL',
# S5 why partner
A+'2155': 'Why we believe Yuno is the right partner for Acebet',
A+'2160': 'A DEDICATED TEAM FOR ACEBET',
# S11 key advantages
K1+'28715': 'Yuno is the global payment partner to scale Acebet',
K1+'28719': '**Global payment method coverage** and **leading capabilities for payment routing and orchestration** position Yuno as a best-in-class partner for Acebet',
K1+'28722': 'Breeze, Coinflow and new acquirers, one integration',
K1+'28726': 'Volume split and cascading across acquirers',
K1+'28735': 'Leverage and redundancy',
# pricing
R+'114': f'A rate per successful transaction that steps down from {RATES[0]*100:g} cents to {RATES[-1]*100:g} cents across four tranches, about {V/TX*100:.1f} cents on average at today\'s {TX:,} transactions a month, on a flat platform fee of **${PLATFORM:,} a month**. You are charged only on approved transactions; a payment that is retried or cascaded counts once.',
R+'117': 'Tranche pricing: each tranche is billed at its own rate within the month. Declines and retries cost nothing.',
R+'121': 'TRANCHE 1', R+'122': rng(0),
R+'125': 'TRANCHE 2', R+'126': rng(1),
R+'141': f'No setup fee. Every transaction above {CUTS[2]:,} a month is billed at {c(RATES[3])} as Acebet expands into new markets.',
R+'157': 'Volume split, cascading & retries',
R+'166': 'Hosted fields & sandbox',
R+'173': f'${PLATFORM:,} / month flat',
R+'174': 'Integrations included: a new acquirer is a routing change, not a new fee.',
R+'176': 'WHAT IT MEANS FOR ACEBET',
R+'177': f"At {TX:,} successful transactions / month, today's volume",
R+'182': f'Tranche 1: {b[0][0]:,} trx at {c(b[0][1])}', R+'183': f'${b[0][2]:,.0f}', R+'184': f'${b[0][2]*12:,.0f}',
'lu_r2_lbl': f'Tranche 2: {b[1][0]:,} trx at {c(b[1][1])}', 'lu_r2_m': f'${b[1][2]:,.0f}', 'lu_r2_a': f'${b[1][2]*12:,.0f}',
R+'187': f'${V:,.0f}', R+'188': f'${V*12:,.0f}',
R+'191': f'${PLATFORM:,}', R+'192': f'${PLATFORM*12:,}',
R+'195': f'${TOT:,.0f}', R+'196': f'${TOT*12:,.0f}',
R+'197': c(V/TX),
R+'198': f'average rate per successful transaction at this volume, before the platform fee ({c(TOT/TX)} all-in).',
R+'200': 'Payouts and reconciliation below are not in these totals.',
R+'203': 'PAYOUTS',
R+'206': 'Payouts on the same platform, routed across providers from **one integration**.',
R+'207': "Scope and pricing to be reviewed together, depending on Acebet's interest. **Not included** in the totals above.",
R+'212': 'One reconciliation view across **Breeze, Coinflow, Whop and Checkout** instead of one process per provider.',
}
T2 = {R+'123': (c(RATES[0]), '/trx'), R+'127': (c(RATES[1]), '/trx')}
# duplicated objects: new_id -> (source_id, (x, y, w, h), markup or (head, tail) for two-run boxes, None = shape)
DUP = {
 'ab_t3_l': (R+'121', (43.0, 211.0, None, None), 'TRANCHE 3'), 'ab_t3_r': (R+'122', (43.0, 218.0, None, None), rng(2)),
 'ab_t3_p': (R+'123', (178.0, 211.0, None, None), (c(RATES[2]), '/trx')), 'ab_sep3': (R+'128', (43.0, 235.5, None, None), None),
 'ab_t4_l': (R+'121', (43.0, 241.0, None, None), 'TRANCHE 4'), 'ab_t4_r': (R+'122', (43.0, 248.0, None, None), rng(3)),
 'ab_t4_p': (R+'123', (178.0, 241.0, None, None), (c(RATES[3]), '/trx')), 'ab_sep4': (R+'128', (43.0, 266.0, None, None), None),
 'ab_r3_lbl': (R+'182', (None, 164.0, None, 12.0), f'Tranche 3: {b[2][0]:,} trx at {c(b[2][1])}'),
 'ab_r3_m': (R+'183', (None, 164.0, None, 12.0), f'${b[2][2]:,.0f}'), 'ab_r3_a': (R+'184', (None, 164.0, None, 12.0), f'${b[2][2]*12:,.0f}'),
 'ab_grow': (R+'198', (480.0, 274.0, 197.0, 34.0), f'**As Acebet grows.** Above {CUTS[2]:,} a month every transaction is billed at {c(RATES[3])}. All-in, the rate falls from {c(TOT/TX)} today to {grow} transactions a month.'),
}
SHIFT = {R + n: 12.0 for n in ('185', '186', '187', '188', '189', '190', '191', '192', '193', '194', '195', '196', '197', '198')}
MOVE = {R+'140': (None, 274.0, None, 25.0), R+'141': (None, 277.5, None, 18.0), R+'198': (None, None, None, 22.0)}
DELETE = [H+'945', H+'946', 'h4ac5cf136a655f18_1_0', 'h4ac5cf136a655f18_1_1']   # agenda item 03, Luni wordmarks (cover, close)
SLIDES_DELETE = ['g3caca0138e4_0_2759', 'g3fa1128e0cb_1_1468', 'g3fa1128e0cb_1_1995']  # business case divider + two slides
REPLACE_ALL = [('German Tatis - Business', 'German Tatis, Business')]
FORBID = ['Luni', 'LUNI', 'Stripe', 'Paddle', 'Artsiom', 'PayPal US', 'subscription engine', 'SUBSCRIPTIONS ENGINE', '40,000', '16,000', ' — ', ' - ']
