# -*- coding: utf-8 -*-
"""Carry1st Shop LatAm: pricing arithmetic v3 (15-oct-2026). Platform fee $7,500 flat that INCLUDES the first $500K of monthly Net TPV (German; $1M kept as pocket concession)
(Justo: give them volume for free, but in TPV, never in trx),
pay-ins billed in bps on monthly Net TPV (successful tx only, no declines / chargebacks), tranches (ladder).
Client inputs (Cordel, call w/ JP 15-oct-2026): $4-5M/month LatAm TPV by end-2027 (to be aligned), avg ticket ~$10, median ~$5.
Zones (green/yellow/red) must be confirmed in Finance's Pricing Calculator for V3 x gaming margin band before sending."""
PLATFORM = 7_500
INCLUDED = 500_000                        # monthly Net TPV included in the platform fee (single month, no rollover)
LADDER = [(INCLUDED, 0.0), (3_000_000, 0.0030), (6_000_000, 0.0025), (float("inf"), 0.0020)]   # (upper bound, rate); 0 / 30 / 25 / 20 bps
LADDER_V1 = [(2_000_000, 0.0030), (5_000_000, 0.0025), (float("inf"), 0.0020)]              # v1, no allotment, kept for reference
AVG_TICKET, MEDIAN_TICKET = 10.0, 5.0
CREDIT, CREDIT_MONTHS = 3_750, 3          # optional launch lever: Dec-2026 to Feb-2027 (billing start 1-Dec-2026)

def usage(tpv, ladder=None):
    fee, lo = 0.0, 0.0
    for hi, rate in (ladder or LADDER):
        if tpv > lo:
            fee += (min(tpv, hi) - lo) * rate
        lo = hi
    return fee

def monthly(tpv, credit=0):
    u = usage(tpv)
    return u, u + PLATFORM - credit

def bps(x, tpv):
    return x / tpv * 1e4 if tpv else float("nan")

if __name__ == "__main__":
    print(f"platform ${PLATFORM:,} incl. first ${INCLUDED/1e6:g}M TPV | ladder " + " / ".join(f"{r*1e4:.0f} bps to ${hi/1e6:g}M" if hi != float('inf') else f"{r*1e4:.0f} bps above" for hi, r in LADDER[1:]))
    print(f"{'TPV/mo':>9} {'trx@$10':>8} {'usage':>9} {'eff bps':>8} {'all-in':>9} {'all-in bps':>10} {'$/avg trx':>10} {'$/median':>9} {'annual':>11}")
    for tpv in (500_000, 1_000_000, 2_000_000, 3_000_000, 4_000_000, 4_500_000, 5_000_000, 8_000_000, 10_000_000):
        u, t = monthly(tpv)
        trx = tpv / AVG_TICKET
        print(f"{tpv/1e6:>8.1f}M {trx:>8,.0f} {u:>9,.0f} {bps(u,tpv):>8.1f} {t:>9,.0f} {bps(t,tpv):>10.1f} {t/trx:>10.4f} {u/tpv*MEDIAN_TICKET:>9.4f} {t*12:>11,.0f}")
    # fixed-fee comparison at $4.5M / 450K trx
    tpv = 4_500_000; trx = tpv / AVG_TICKET
    print("\nfixed-fee alternative at $4.5M (450K trx):")
    for p in (0.05, 0.04, 0.03):
        print(f"  ${p:.2f}/trx -> usage ${p*trx:,.0f}  ({bps(p*trx,tpv):.0f} bps)  on $5 = {p/5*100:.2f}%  on $2 = {p/2*100:.2f}%")
    u, t = monthly(tpv)
    print(f"  ladder     -> usage ${u:,.0f}  ({bps(u,tpv):.1f} bps)  on $5 = {bps(u,tpv)/100:.3f}%  on $2 = same")
    # break-even: extra approved sales needed to cover the all-in bill, by gross margin
    print(f"\nall-in at $4.5M = {bps(t,tpv):.1f} bps; break-even conversion uplift by gross margin:")
    for m in (0.05, 0.10, 0.15, 0.20, 0.30):
        print(f"  margin {m:>4.0%}: need +{bps(t,tpv)/1e4/m*100:.2f}% more approved sales  (Yuno published uplift 7%)")
    # launch ramp with credits
    print(f"\nlaunch lever: ${CREDIT:,} credit x {CREDIT_MONTHS} months = ${CREDIT*CREDIT_MONTHS:,} total")
    for label, tpv in (("Dec-26", 300_000), ("Jan-27", 500_000), ("Feb-27", 800_000), ("Mar-27", 1_200_000)):
        c = CREDIT if label != "Mar-27" else 0
        u, t = monthly(tpv, c)
        print(f"  {label} TPV ${tpv/1e6:.1f}M -> usage ${u:,.0f} + platform ${PLATFORM-c:,} = ${t:,.0f}")
