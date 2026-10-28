# -*- coding: utf-8 -*-
"""Acebet: pricing arithmetic for the proposal slide. No business case (German, 27-oct-2026).
Client-reported inputs (Boris, call 27-oct-2026): ~$25M a month, ~700,000 transactions a month, average ticket $30 to $50.
Pricing (German, 27-oct-2026): $10,000 platform fee + 4 tranches per successful transaction, about 2.5 cents average at today's
volume, the top tranche at Spreedly's ~1.5 cents so the rate falls as Acebet expands (Canada, Australia, France, Spain)."""
TX = 680_000                 # successful transactions / month: last 30 days to 27-oct-2026 = 678,498 deposits, $22.77M (internal data via German), rounded; Boris said ~700K
TPV = 22_770_000             # last 30 days (Boris said ~$25M); avg deposit $33.42 on Breeze
PLATFORM = 0   # v7 (German, 27-oct): platform fee removed, usage only
CUTS = [1_000_000, 2_000_000, None]   # v6 (German, 27-oct): 0-1M / 1M-2M / 2M+
RATES = [0.020, 0.015, 0.010]          # v8 (German, 27-oct): 2 cents avg at 680K, no platform fee; 1 cent = policy floor
GROWTH = [680_000, 1_000_000, 1_500_000, 2_000_000]  # illustrative volumes, not forecasts
def bands(tx):
    out, lo = [], 0
    for cut, r in zip(CUTS, RATES):
        hi = tx if cut is None else min(tx, cut)
        n = max(hi - lo, 0); out.append((n, r, n * r))
        if cut is None or tx <= cut: lo = tx; continue
        lo = cut
    return out
def var(tx): return sum(b[2] for b in bands(tx))
def total(tx): return var(tx) + PLATFORM
def rng(i):
    lo = 0 if i == 0 else CUTS[i - 1] + 1
    return f'{lo:,} to {CUTS[i]:,}' if CUTS[i] else f'Above {CUTS[i-1]:,}'
if __name__ == '__main__':
    for tx in GROWTH:
        print(f"{tx:>9,} trx: usage ${var(tx):,.0f} (avg ${var(tx)/tx:.4f}/trx) + platform = ${total(tx):,.0f}/mo, ${total(tx)*12:,.0f}/yr, all-in ${total(tx)/tx:.4f}/trx")
    print([b for b in bands(TX)])
