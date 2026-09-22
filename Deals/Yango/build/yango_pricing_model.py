# -*- coding: utf-8 -*-
"""Yango pricing model (2026-09-22). Source volumes: Yango's own recharge data (Javier Patiño's team, Aug 2026),
as used in the live deck 'Business Case Yango + Yuno' (slide 31). Annual figures / 12 = monthly."""
ANNUAL = {  # country: (cashless GMV / year USD, transactions / year, avg ticket)
    'Colombia':  (23_155_176, 6_615_768, 3.50),
    'Peru':      (21_553_152, 6_735_360, 3.20),
    'Bolivia':   (32_968_452, 21_978_972, 1.50),
    'Venezuela': (9_983_520, 3_565_548, 2.80),
}
PLATFORM_FEE = 10_000
TRANCHES = [(2_500_000, 0.0060), (2_500_000, 0.0050), (float('inf'), 0.0045)]  # (width of band, rate on approved recharge volume)
CARD_RAIL_CASE = 3_210_000   # $/yr, deck slide 30: $2.33M acceptance + $0.88M MDR
MDR_LEVER = 880_000

def tx_fee(V):
    fee, rem = 0.0, V
    for width, rate in TRANCHES:
        take = min(rem, width); fee += take * rate; rem -= take
        if rem <= 0: break
    return fee

monthly = {c: (g/12, t/12, k) for c, (g, t, k) in ANNUAL.items()}
tot_v = sum(v for v, _, _ in monthly.values()); tot_t = sum(t for _, t, _ in monthly.values())
print(f"{'country':10} {'GMV/mo':>14} {'tx/mo':>12} {'ticket':>7}")
for c, (v, t, k) in monthly.items(): print(f"{c:10} {v:14,.2f} {t:12,.1f} {k:7.2f}")
print(f"{'TOTAL':10} {tot_v:14,.2f} {tot_t:12,.1f} {tot_v/tot_t:7.4f}")

print("\nTranche equivalents at blended ticket", round(tot_v/tot_t,4))
for w, r in TRANCHES: print(f"  {r*100:.2f}% -> ${r*tot_v/tot_t:.5f} per tx")

print("\nFully ramped (all four markets):")
fee = tx_fee(tot_v); total = fee + PLATFORM_FEE
bands = []; rem = tot_v
for w, r in TRANCHES:
    take = min(rem, w); bands.append((take, r, take*r)); rem -= take
    if rem <= 0: break
for take, r, f in bands: print(f"  band {r*100:.2f}% on {take:,.0f}: {f:,.2f}/mo  {f*12:,.2f}/yr")
print(f"  tx fee {fee:,.2f}/mo  platform {PLATFORM_FEE:,}  TOTAL {total:,.2f}/mo  {total*12:,.2f}/yr")
print(f"  all-in per tx {total/tot_t:.5f}  all-in % of TPV {total/tot_v*100:.4f}%  effective tx rate {fee/tot_v*100:.4f}%")
print(f"  card-rail case / cost = {CARD_RAIL_CASE/(total*12):.2f}x ; MDR lever {MDR_LEVER:,} vs cost {total*12:,.0f}")

print("\nRollout, cumulative (Colombia -> +Peru -> +Bolivia -> +Venezuela):")
order = ['Colombia','Peru','Bolivia','Venezuela']; V=0; T=0; prev=0
for c in order:
    v,t,k = monthly[c]; V+=v; T+=t
    f = tx_fee(V); tot = f + PLATFORM_FEE
    print(f"  +{c:10} vol {V:12,.0f} tx {T:10,.0f} | tx fee {f:10,.2f} total {tot:10,.2f}/mo ({tot*12:11,.2f}/yr) | added {tot-prev:9,.2f} | all-in/tx {tot/T:.4f} | {tot/V*100:.3f}% of vol")
    prev = tot

print("\nAllocation at blended effective rate (all four live):")
eff = fee/tot_v
for c,(v,t,k) in monthly.items(): print(f"  {c:10} {v*eff:10,.2f}/mo  ({v*eff/t:.4f}/tx, {eff*100:.3f}%)")
print(f"  sum {sum(v*eff for v,_,_ in monthly.values()):,.2f}")

print("\nAlternative A, per-transaction tranches (FlightHub style) for the doc:")
ALT = [(1_000_000, 0.015), (1_000_000, 0.012), (1_000_000, 0.011), (float('inf'), 0.010)]
rem=tot_t; f=0
for w,r in ALT:
    take=min(rem,w); f+=take*r; rem-=take
    if rem<=0: break
print(f"  tx fee {f:,.2f}  total {f+PLATFORM_FEE:,.2f}/mo  {(f+PLATFORM_FEE)*12:,.2f}/yr  per tx {(f+PLATFORM_FEE)/tot_t:.4f}  % {(f+PLATFORM_FEE)/tot_v*100:.3f}")
