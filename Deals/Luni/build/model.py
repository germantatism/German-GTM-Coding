# -*- coding: utf-8 -*-
"""Luni: business case + pricing arithmetic. Every figure on the business case (S13, S14) and pricing (S16) slides comes from here.
Client-reported inputs (Artsiom Kalianchuk, call 15-oct-2026): ~40,000 payment attempts in September (Stripe US ~40K at 37%,
Stripe France ~1.5K at 68%, third account ~1.5K), blended ~40% approval, $18 average ticket (German's figure, acknowledged on the call).
Ranges = Yuno modelling assumptions, to be recalibrated with the decline breakdown Artsiom is sending."""
ATTEMPTS = 40_000            # payment attempts / month (September, reported)
APPROVAL = 0.40              # blended approval (reported, "a little bit more than 40% weighted")
TICKET = 18                  # average ticket USD (acknowledged on the call)
APPROVED = int(ATTEMPTS * APPROVAL)                 # 16,000 approved payments / month today
TPV = APPROVED * TICKET * 12                        # approved volume / year ≈ $3.46M
# L1 approval uplift via routing, local route for EU cards and decline-type retries: +8 pts conservative, +16 pts optimistic
# (v1 was +10 / +20; German asked for a slightly more conservative case on 15-oct)
L1_PTS = (0.08, 0.16)
L1 = tuple(ATTEMPTS * p * TICKET * 12 for p in L1_PTS)
L1_PAY = tuple(int(ATTEMPTS * p) for p in L1_PTS)   # +4,000 / +8,000 approved payments a month
# L2 checkout & payment methods (PayPal, local methods, better checkout): +2% to +4% more approved payments on today's base (v1: +2% / +5%)
L2_PCT = (0.02, 0.04)
L2 = tuple(APPROVED * p * TICKET * 12 for p in L2_PCT)
# L3 processing cost (cross-border fees avoided, cheapest provider at equal approval): 20 to 40 bps of approved volume (v1: 25 / 50)
L3_BPS = (20, 40)
L3 = tuple(TPV * b / 10_000 for b in L3_BPS)
# L4 integrations avoided: PayPal US (in progress) + EU acquirer + local processing/MoR + methods for new markets
NEW, CUR, FTE = (2, 3), 3, 80_000                    # new integrations (cons, opt; v1 was 3 / 4); current = Stripe US, Stripe FR, Paddle; $80K per engineer
WEEKS = (NEW[0] * 8 + (NEW[0] + CUR) * 8 * 0.20, NEW[1] * 12 + (NEW[1] + CUR) * 12 * 0.30)
L4 = tuple(w / 52 * FTE for w in WEEKS)
LEV = [L1, L2, L3, L4]
cons, opt = sum(l[0] for l in LEV), sum(l[1] for l in LEV)
avg = [(l[0] + l[1]) / 2 for l in LEV]
mid = (cons + opt) / 2
# Pricing (German, 15-oct-2026): platform fee $10,000 flat (opened at $12,000, lowered the same day) + $0.06 on the first 30,000 successful trx + $0.05 on the next 10,000
PLATFORM, P1, P2, CUT1, CUT2 = 10_000, 0.06, 0.05, 30_000, 40_000   # platform $12K -> $10K (German, 15-oct, same day)
def var(tx):
    return min(tx, CUT1) * P1 + max(min(tx, CUT2) - CUT1, 0) * P2
def monthly(tx):
    v = var(tx); return v, v + PLATFORM
SCEN = {  # label -> successful trx / month ('cons' / 'opt' follow the L1 scenarios; '50%' / '60%' kept for the earlier fixes)
    'today': APPROVED, 'cons': int(ATTEMPTS * (APPROVAL + L1_PTS[0])), 'opt': int(ATTEMPTS * (APPROVAL + L1_PTS[1])),
    '50%': int(ATTEMPTS * 0.50), '60%': int(ATTEMPTS * 0.60), 'full': CUT2}
def M(v):   # $1.73M / $864K / $8.6K
    if v >= 1e6: return f"${v/1e6:.2f}M"
    if v >= 100e3: return f"${round(v/1e3):,.0f}K"
    return f"${v/1e3:.1f}K"
def M1(v):
    return f"${v/1e6:.1f}M" if v >= 1e6 else f"${round(v/1e3):,.0f}K"
if __name__ == '__main__':
    print(f"approved today {APPROVED:,}/mo | TPV ${TPV:,.0f}/yr | attempted gross ${ATTEMPTS*TICKET*12:,.0f}/yr")
    for i, l in enumerate(LEV, 1): print(f"L{i}: {l[0]:,.0f} / {l[1]:,.0f} / avg {avg[i-1]:,.0f} -> {M(l[0])} / {M(l[1])} / {M(avg[i-1])}")
    print(f"L1 payments: +{L1_PAY[0]:,} / +{L1_PAY[1]:,} per month | weeks L4 {WEEKS}")
    print(f"total: {cons:,.0f} / {opt:,.0f} / mid {mid:,.0f} -> {M(cons)} / {M(opt)} / {M(mid)} | L1 share of mid {avg[0]/mid:.1%}")
    for k, tx in SCEN.items():
        v, t = monthly(tx); print(f"{k:6s} {tx:>6,} trx: var ${v:,.0f} total ${t:,.0f}/mo ${t*12:,.0f}/yr all-in ${t/tx:.3f} | platform share {PLATFORM/t:.0%}")
    print(f"+4,000 payments/mo at ${TICKET} = ${L1_PAY[0]*TICKET:,.0f}/mo; +8,000 = ${L1_PAY[1]*TICKET:,.0f}/mo")
def K(v):   # lever values: $1.73M / $864K / $69K / $8.6K
    if v >= 1e6: return f"${v/1e6:.2f}M"
    if v >= 10e3: return f"${round(v/1e3):,.0f}K"
    return f"${v/1e3:.1f}K"
def T(v):   # totals: $0.99M / $1.51M / $2.03M
    return f"${v/1e6:.2f}M"
