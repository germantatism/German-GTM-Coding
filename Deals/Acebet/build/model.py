# -*- coding: utf-8 -*-
"""Acebet: pricing arithmetic for the proposal slide. No business case (German, 27-oct-2026).
Client-reported inputs (Boris, call 27-oct-2026): ~$25M a month, ~700,000 transactions a month, average ticket $30 to $50.
Pricing (German, 27-oct-2026): $10,000 platform fee + 4 tranches per successful transaction, about 2.5 cents average at today's
volume, the top tranche at Spreedly's ~1.5 cents so the rate falls as Acebet expands (Canada, Australia, France, Spain)."""
TX = 700_000                 # successful transactions / month today (reported)
TPV = 25_000_000             # monthly volume (reported)
PLATFORM = 10_000
CUTS = [250_000, 500_000, 1_000_000, None]          # upper bound of each tranche; None = no cap
RATES = [0.030, 0.025, 0.020, 0.015]
GROWTH = [700_000, 1_000_000, 1_500_000, 2_000_000]  # illustrative volumes, not forecasts
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
