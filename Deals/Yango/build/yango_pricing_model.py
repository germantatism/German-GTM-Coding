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


# ---------------------------------------------------------------------------------------------------------------
# LIVE MODEL (deck version of 2026-09-22 23:26, reviewed 2026-09-24): per-transaction tranches pooled across the
# four markets + $10,000 platform fee + "monthly minimum billing $25,000" (slide 36). The % model above is the
# 22-sep alternative that stays in the pocket.
# ---------------------------------------------------------------------------------------------------------------
LIVE_TRANCHES = [(500_000, 0.023), (500_000, 0.020), (500_000, 0.017), (500_000, 0.014), (1_000_000, 0.011), (float('inf'), 0.008)]
LIVE_MIN_INVOICE = 25_000          # slide 36 wording: "Monthly minimum billing: $25,000" (whether it includes the platform fee is not stated)
RECON_LIVE = (2_000, 500_000, 0.0003)   # $2,000/mo for the first 500K reconciled tx, then $0.0003/tx (slide 36 add-ons)
RECON_POLICY_MIN = (1_500, 0.0085)      # Pricing Policy minimum: $1,500/mo + $0.0085 per reconciled tx

def live_tx_fee(T):
    fee, rem, rows = 0.0, T, []
    for width, rate in LIVE_TRANCHES:
        take = min(rem, width); fee += take * rate; rows.append((take, rate, take * rate)); rem -= take
        if rem <= 0: break
    return fee, rows

print("\n==================== LIVE MODEL (per-transaction tranches, deck 22-sep 23:26) ====================")
lf, lrows = live_tx_fee(tot_t)
for take, r, x in lrows: print(f"  {take:>12,.0f} tx @ ${r:.3f} = {x:>10,.2f}/mo  {x*12:>12,.2f}/yr")
ltot = lf + PLATFORM_FEE
print(f"  tx fee {lf:,.2f}  platform {PLATFORM_FEE:,}  TOTAL {ltot:,.2f}/mo  {ltot*12:,.2f}/yr")
print(f"  all-in per tx {ltot/tot_t:.5f}  all-in % of TPV {ltot/tot_v*100:.3f}%  effective tx rate {lf/tot_t:.5f}/tx = {lf/tot_v*100:.3f}% of TPV")
print(f"  card-rail case / cost = {CARD_RAIL_CASE/(ltot*12):.2f}x ; MDR lever {MDR_LEVER:,} vs cost {ltot*12:,.0f}")

print("\nLive rollout, cumulative (Colombia -> +Peru -> +Bolivia -> +Venezuela), with the $25,000 minimum:")
V = T = 0; prev = 0
for c in order:
    v, t, k = monthly[c]; V += v; T += t
    f, _ = live_tx_fee(T); tot = f + PLATFORM_FEE; billed = max(tot, LIVE_MIN_INVOICE)
    print(f"  +{c:10} tx {T:10,.0f} | tx fee {f:10,.2f} | computed {tot:10,.2f} | billed {billed:10,.2f} | added {tot-prev:9,.2f} | per tx {tot/T:.4f} | {tot/V*100:.3f}% of vol")
    prev = tot

print("\nLive allocation at full volume by share of transactions (slide 37):")
s = 0
for c, (v, t, k) in monthly.items():
    sh = t / tot_t; a = lf * sh; p = PLATFORM_FEE * sh; s += a + p
    print(f"  {c:10} share {sh*100:5.2f}%  tx fee {a:10,.2f}  platform {p:8,.2f}  total {a+p:10,.2f}  per tx {(a+p)/t:.4f}  {(a+p)/v*100:.3f}% of its volume")
print(f"  sum {s:,.2f}")

fixed, first, rate = RECON_LIVE
rec_live = fixed + max(0, tot_t - first) * rate
rec_min = RECON_POLICY_MIN[0] + tot_t * RECON_POLICY_MIN[1]
print(f"\nReconciliation add-on at full volume: deck {rec_live:,.2f}/mo  vs policy minimum {rec_min:,.2f}/mo  (pack 3M tx = 30,000/mo) -> {rec_min/rec_live:.1f}x below minimum")
for c, (v, t, k) in monthly.items():
    print(f"  {c:10} ticket ${k:.2f}: $0.023 = {0.023/k*100:.2f}% of ticket ; $0.008 = {0.008/k*100:.2f}%")


# ---------------------------------------------------------------------------------------------------------------
# FINAL MODEL (deck as read 2026-09-24 afternoon, after German's adjustments): % of approved recharge volume,
# four tranches pooled across the four markets, $12,000 platform fee, no monthly minimum. Sent-candidate.
# ---------------------------------------------------------------------------------------------------------------
FINAL_PF = 12_000
FINAL_TRANCHES = [(1_500_000, 0.0025), (1_500_000, 0.0020), (1_500_000, 0.0015), (float('inf'), 0.0010)]

def final_tx_fee(V):
    f, rem = 0.0, V
    for w, r in FINAL_TRANCHES:
        take = min(rem, w); f += take * r; rem -= take
        if rem <= 0: break
    return f

print("\n==================== FINAL MODEL (% of volume, deck 24-sep) ====================")
ff = final_tx_fee(tot_v); ftot = ff + FINAL_PF
print(f"  tx fee {ff:,.2f}  platform {FINAL_PF:,}  TOTAL {ftot:,.2f}/mo  {ftot*12:,.2f}/yr  per tx {ftot/tot_t:.5f}  {ftot/tot_v*100:.3f}% of volume  card-rail case {CARD_RAIL_CASE/(ftot*12):.1f}x")
V = T = 0; prev = 0
for c in order:
    v, t, k = monthly[c]; V += v; T += t; x = final_tx_fee(V) + FINAL_PF
    print(f"  +{c:10} total {x:10,.2f}/mo  added {x-prev:9,.2f}  per recharge {x/T:.4f}")
    prev = x
print("  per-tx equivalents at $2.25 ticket:", [round(r * tot_v / tot_t, 5) for _, r in FINAL_TRANCHES], "| Doc minimum $0.01/tx")
