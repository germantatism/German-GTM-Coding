# Carry1st x Yuno · LatAm Shop launch · deck-ready numbers (15 Oct 2026, pricing v4)

Source model: `bc_model.xlsx` (formula-linked; every figure here is generated from `model_numbers.json`, the Python mirror of the workbook). All figures USD, monthly unless stated. Option A = EBANX direct. Option B = EBANX primary + dLocal second MoR through Yuno. Average ticket $10 (Carry1st, Cordel, Oct 2026, estimate). Contribution view nets the take rate (15%, ESTIMATE) and the Option B processing cost on every dollar of incremental GMV; the GMV view counts the full incremental GMV. Rounding: $ in K with one decimal; cost per $1,000 TPV with one decimal; Yuno share of TPV with two decimals because the figures sit under 1%.

## Section A · Four tiers, both options, three scenarios

Option A is the same in every scenario: 4.5% of TPV (ESTIMATE, range 3 to 6%, to be replaced by EBANX's quote), i.e. $45.0 per $1,000 TPV: $22.5K at 50,000, $45.0K at 100,000, $90.0K at 200,000, $202.5K at 450,000 transactions a month.

Yuno line (identical in every scenario; $7,500 flat including the first $500K of monthly Net TPV, then 40 / 30 / 20 / 10 bps on the Net TPV above it with steps at $2M, $5M and $10M): $7.5K at 50,000 · $9.5K at 100,000 · $13.5K at 200,000 · $21.0K at 450,000 (1.50% · 0.95% · 0.68% · 0.47% of TPV; $0.150 · $0.095 · $0.068 · $0.047 per transaction).

### Base scenario (MDR 50 bps · approval +3.0 pts · local methods +1.0% of TPV · 5 markets x 3 weeks + 2 integrations avoided + 0.50 FTE maintenance)

| Tx / month | TPV | Option A cost | Option A per $1,000 | Option B cost (provider + Yuno) | of which Yuno | Option B per $1,000 | Option B per $1,000 after levers | Net benefit, contribution | Net benefit, GMV view |
|---|---|---|---|---|---|---|---|---|---|
| 50,000 | $0.5M | $22.5K | $45.0 | $27.5K | $7.5K | $55.0 | $37.1 | +$4.0K | +$26.6K |
| 100,000 | $1.0M | $45.0K | $45.0 | $49.5K | $9.5K | $49.5 | $37.9 | +$7.1K | +$52.1K |
| 200,000 | $2.0M | $90.0K | $45.0 | $93.5K | $13.5K | $46.8 | $38.3 | +$13.4K | +$103.1K |
| 450,000 | $4.5M | $202.5K | $45.0 | $201.0K | $21.0K | $44.7 | $37.9 | +$31.8K | +$233.1K |

Break-even: about 12.3K successful transactions a month (about $0.12M TPV).

### Conservative scenario (MDR 25 bps · approval +1.5 pts · local methods +0.5% of TPV · 5 markets x 2 weeks + 1 integration avoided + 0.25 FTE maintenance)

| Tx / month | Option A per $1,000 | Option B cost | Option B per $1,000 | Option B per $1,000 after levers | Net benefit, contribution | Net benefit, GMV view |
|---|---|---|---|---|---|---|
| 50,000 | $45.0 | $28.8K | $57.5 | $48.5 | ($1.8K) | +$9.6K |
| 100,000 | $45.0 | $52.0K | $52.0 | $46.2 | ($1.2K) | +$21.3K |
| 200,000 | $45.0 | $98.5K | $49.3 | $45.1 | ($0.1K) | +$44.8K |
| 450,000 | $45.0 | $212.3K | $47.2 | $43.9 | +$5.2K | +$106.1K |

Break-even: about 206K transactions a month. Reading: in the conservative case Yuno is cost-neutral well before the run rate; what Carry1st buys for $1.8K a month net at launch is failover, a second provider in play and the local-method coverage.

### Optimistic scenario (MDR 75 bps · approval +5.0 pts · local methods +2.0% of TPV · 5 markets x 4 weeks + 3 integrations avoided + 1.00 FTE maintenance)

| Tx / month | Option A per $1,000 | Option B cost | Option B per $1,000 | Option B per $1,000 after levers | Net benefit, contribution | Net benefit, GMV view |
|---|---|---|---|---|---|---|
| 50,000 | $45.0 | $26.3K | $52.5 | $19.4 | +$12.8K | +$51.9K |
| 100,000 | $45.0 | $47.0K | $47.0 | $25.7 | +$19.3K | +$97.0K |
| 200,000 | $45.0 | $88.5K | $44.3 | $28.9 | +$32.2K | +$187.2K |
| 450,000 | $45.0 | $189.8K | $42.2 | $30.1 | +$67.1K | +$415.1K |

Break-even: about 5.0K transactions a month. The approval uplift of 5 points stays under Yuno's published 7% authorization uplift.

## Section B · Scenario summary at launch (50K) and at run rate (450K)

### Monthly

| | Conservative | Base | Optimistic |
|---|---|---|---|
| Gross benefit at 50K | $5.7K | $11.5K | $20.3K |
| Yuno cost at 50K | $7.5K | $7.5K | $7.5K |
| Net at 50K (contribution) | ($1.8K) | +$4.0K | +$12.8K |
| Net at 50K (GMV view) | +$9.6K | +$26.6K | +$51.9K |
| Gross benefit at 450K | $26.2K | $52.8K | $88.1K |
| Yuno cost at 450K | $21.0K | $21.0K | $21.0K |
| Net at 450K (contribution) | +$5.2K | +$31.8K | +$67.1K |
| Net at 450K (GMV view) | +$106.1K | +$233.1K | +$415.1K |
| Gross benefit / Yuno cost at 450K | 1.2x | 2.5x | 4.2x |
| Break-even, tx a month | about 206K | about 12.3K | about 5.0K |
| Payback month on the ramp (cumulative net turns positive) | Sep 2027 | Dec 2026 | Dec 2026 |

### Annual (x12 at the volume shown)

| | Conservative | Base | Optimistic |
|---|---|---|---|
| Net a year at 50K (contribution) | ($21.1K) | +$47.5K | +$153.7K |
| Net a year at 450K (contribution) | +$61.8K | +$381.4K | +$805.7K |
| Net a year at 450K (GMV view) | $1.27M | $2.8M | $4.98M |
| Yuno cost a year at 450K | $252.0K | $252.0K | $252.0K |
| Option A cost a year at 450K | $2.43M | $2.43M | $2.43M |
| Option B cost a year at 450K (provider + Yuno) | $2.55M | $2.41M | $2.28M |
| Cumulative net over the 13-month ramp (Dec 2026 to Dec 2027, linear 50K to 450K, ESTIMATE) | +$16.3K | +$226.5K | +$513.6K |
| Yuno cost over the 13-month ramp | $190.8K | $190.8K | $190.8K |

### Lever breakdown (monthly, contribution view; GMV in brackets where the lever is a GMV effect)

| Lever | Cons. 50K | Base 50K | Opt. 50K | Cons. 450K | Base 450K | Opt. 450K |
|---|---|---|---|---|---|---|
| L1 · MDR reduction (100% contribution) | $1.3K | $2.5K | $3.8K | $11.3K | $22.5K | $33.8K |
| L2 · retries and routing recovery | $0.9K [$10.0K GMV] | $1.9K [$20.0K GMV] | $3.3K [$33.3K GMV] | $9.3K [$90.0K GMV] | $19.0K [$180.0K GMV] | $32.4K [$300.0K GMV] |
| L3 · local-method coverage | $0.2K [$2.5K] | $0.5K [$5.0K] | $1.0K [$10.0K] | $2.3K [$22.5K] | $4.7K [$45.0K] | $9.7K [$90.0K] |
| L4 (deck L2) · integrations avoided (per-market EBANX work and later integrations over 24 months, plus maintenance), monthly | $3.3K | $6.6K | $12.3K | $3.3K | $6.6K | $12.3K |
| Gross benefit | $5.7K | $11.5K | $20.3K | $26.2K | $52.8K | $88.1K |

L1 is the lever that matters most for a reseller: a processing saving is 100% contribution, while incremental GMV is worth take rate minus processing cost (about 11 cents per dollar at a 15% take rate). In the base case L1 is 42.6% of the gross benefit at 450K.

## Section C · Small-ticket sensitivity (why bps on Net TPV is the right shape)

Same transactions, three tickets. Yuno total = $7,500 platform fee (first $500K of monthly Net TPV included) + usage on the Net TPV above the block (0.40% to $2M, 0.30% $2M to $5M, 0.20% $5M to $10M, 0.10% above $10M).

| Ticket · line | 50,000 tx | 100,000 tx | 200,000 tx | 450,000 tx |
|---|---|---|---|---|
| $5 (median) · TPV | $0.25M | $0.5M | $1.0M | $2.25M |
| $5 · Yuno total | $7.5K | $7.5K | $9.5K | $14.3K |
| $5 · Yuno, % of TPV | 3.00% | 1.50% | 0.95% | 0.63% |
| $5 · Yuno, $ per transaction | $0.150 | $0.075 | $0.048 | $0.032 |
| $5 · Yuno usage only, $ per transaction | $0.000 | $0.000 | $0.010 | $0.015 |
| $5 · a fixed $0.05 per transaction | $2.5K (1.00%) | $5.0K (1.00%) | $10.0K (1.00%) | $22.5K (1.00%) |
| $5 · a fixed $0.10 per transaction | $5.0K (2.00%) | $10.0K (2.00%) | $20.0K (2.00%) | $45.0K (2.00%) |
| $10 (average) · Yuno total | $7.5K | $9.5K | $13.5K | $21.0K |
| $10 · Yuno, % of TPV | 1.50% | 0.95% | 0.68% | 0.47% |
| $10 · Yuno, $ per transaction | $0.150 | $0.095 | $0.068 | $0.047 |
| $10 · a fixed $0.05 / $0.10 per transaction, % of TPV | 0.50% / 1.00% | 0.50% / 1.00% | 0.50% / 1.00% | 0.50% / 1.00% |
| $15 · Yuno total | $8.5K | $11.5K | $16.5K | $26.0K |
| $15 · Yuno, % of TPV | 1.13% | 0.77% | 0.55% | 0.39% |
| $15 · a fixed $0.05 / $0.10 per transaction, % of TPV | 0.33% / 0.67% | 0.33% / 0.67% | 0.33% / 0.67% | 0.33% / 0.67% |

Reading for the slide: a fixed fee is blind to the ticket, so when the ticket halves the fee doubles as a share of what Carry1st sells ($0.05 becomes 1.0% of TPV at a $5 median, $0.10 becomes 2.0%). Yuno's usage is a share of Net TPV, so at a $5 median the usage rate is $0.020 per transaction in tranche 1, $0.015 in tranche 2, $0.010 in tranche 3 and $0.005 in tranche 4, and the all-in cost at 450K is 0.63% of TPV against 1.0% or 2.0% for the fixed fees. The platform fee is the one fixed element, which is why the first $500K of monthly volume sits inside it: at launch Carry1st pays $7,500 and nothing per transaction. Be upfront that at 50K transactions and a $5 ticket the platform fee alone is 3.00% of TPV; the structure pays off as volume ramps, not in month one.

### Take rate sensitivity (base scenario, contribution view)

| Take rate on GMV | Net at 50K / month | Net at 450K / month | Net at 450K / year | Gross / Yuno at 450K |
|---|---|---|---|---|
| 10% | +$2.7K | +$20.5K | +$246.4K | 2.0x |
| 15% (default, ESTIMATE) | +$4.0K | +$31.8K | +$381.4K | 2.5x |
| 25% | +$6.5K | +$54.3K | +$651.4K | 3.6x |

### Baseline provider cost sensitivity (base scenario, 450K)

| Baseline all-in cost | Option A per $1,000 | Option B per $1,000 (provider + Yuno) | Option B per $1,000 after levers | Net a month | Net a year |
|---|---|---|---|---|---|
| 3.0% | $30.0 | $29.7 | $22.2 | +$35.2K | +$421.9K |
| 4.5% (default, ESTIMATE) | $45.0 | $44.7 | $37.9 | +$31.8K | +$381.4K |
| 6.0% | $60.0 | $59.7 | $53.7 | +$28.4K | +$340.9K |

The MDR lever is a gap between two routes (bps), so the baseline level moves both options together; the net benefit changes only through the processing cost netted on incremental GMV.

## Section D · Assumptions, as they should appear on the "Risks and assumptions" slide

1. Volumes: 50K, 100K, 200K and 450K successful transactions a month at a $10 average ticket ($0.5M to $4.5M TPV). Run rate: Carry1st estimate, Cordel, Oct 2026, not yet aligned internally. Launch volume: OPEN, owner Cordel.
2. Baseline provider cost (EBANX direct, cross-border MoR all-in incl. FX and local taxes passed through): 4.5% of TPV, ESTIMATE, range 3 to 6%. Public anchors: dLocal revenue / TPV 2.68% in 2025 (blended, FXC Intelligence, Mar 2026); EBANX merchant review about 5% per transaction (Capterra, 2021); FX spread 1 to 3% (Nuvei, 2026); Brazil IOF 3.5% on FX (Decree 12,466/2025). Replaced by EBANX's quote to Carry1st as soon as it arrives.
3. Carry1st take rate on GMV: 15%, ESTIMATE, TO VALIDATE with Cordel (reseller margins on mainstream gift cards 5 to 15% above wholesale, public guides 2026). Contribution on incremental GMV = GMV x (take rate minus Option B processing cost).
4. L1 MDR reduction with a second MoR in play and routing share to the cheaper route: 25 / 50 / 75 bps of TPV (Yuno estimate; EBANX and dLocal rates through Yuno OPEN, owner Justo).
5. L2 baseline approval on a single MoR route: 75% blended, ESTIMATE, range 70 to 85% (Mexico local 80%+ vs cross-border 50 to 60%, Nuvei 2026; Brazil cross-border cards under 60%, Antom 2025; 10 to 20 point gap by setup, Rapyd 2026). Uplift from retries, failover and second-provider routing: +1.5 / +3.0 / +5.0 points on attempted volume (Yuno estimate; ceiling = Yuno published 7% authorization uplift). Proxy to validate: Carry1st's Saudi and Africa approval rates, owner Cordel.
6. L3 local-method coverage: +0.5% / +1.0% / +2.0% of TPV as incremental GMV, ESTIMATE. Methods carried through Yuno via dLocal and not on the EBANX connection (docs.y.uno, 14 Oct 2026): MODO, Rapipago, Pago Facil (Argentina); Bre-B, Nequi, PSE, Efecty (Colombia); Multipago, Pago al Paso (Bolivia); CoDi, Paynet, 7-Eleven (Mexico). EBANX direct coverage per country TO VALIDATE against its quote.
7. L4 integrations avoided (deck lever L2), three parts at $2,000 per loaded engineer-week (ESTIMATE between Cape Town market pay and LatAm loaded cost of $87.5K to $100.8K a year, Second Talent 2026): (a) per-market EBANX direct work, 5 markets x 2 / 3 / 4 engineer-weeks (country enablement, per-country sandbox tests and certification, local methods; EBANX enables countries during onboarding, each country passes sandbox tests and an Integration Review before production), one-time; (b) later direct integrations avoided, 1 / 2 / 3 (second MoR, local acquirer, Phase 2 local processors) x 4 / 6 / 8 engineer-weeks (4 to 8 weeks per server-to-server PSP integration, spd.tech 2026), one-time; (c) ongoing maintenance of the direct integrations (API changes, certifications, incident handling), 0.25 / 0.5 / 1.0 FTE a year at $104K (52 x $2,000). One-time items spread over 24 months, so the yearly value is one-time / 2 + maintenance. Through Yuno: one integration ready for every market, Yuno maintains the connections. The launch integration itself is not counted.
8. Yuno cost: $7,500 a month flat platform fee that includes the first $500K of monthly Net TPV (successful transactions only, no declines, no chargebacks; single month, no rollover); usage on the Net TPV above it at 0.40% ($500K to $2M), 0.30% ($2M to $5M), 0.20% ($5M to $10M), 0.10% (above $10M), each band on the volume inside it. Declines not billed. Add-ons (network tokens, 3DS) on usage, not in these totals.
9. Ramp for payback: linear from 50K at Black Friday 2026 to 450K by Dec 2027, Yuno ESTIMATE; replaced by Cordel's written projections by country.
10. Levers are modeled on the same TPV and are additive by construction (a cost saving, two GMV effects netted of processing cost, one engineering saving); nothing is double counted. Yuno-wide figures are used only as guardrails: 7% authorization uplift and 30% recovered revenue (y.uno).

## Section E · The 12 numbers for the executive summary

1. $4.5M a month of TPV at the end-2027 run rate (450K transactions at a $10 ticket), Carry1st estimate, Cordel, Oct 2026.
2. Option A (EBANX direct) at run rate: $202.5K a month, $45.0 per $1,000 TPV (4.5% all-in, ESTIMATE until EBANX's quote).
3. Option B (EBANX + dLocal through Yuno) at run rate, base: $201.0K a month, $44.7 per $1,000 TPV, i.e. the same cost line with failover, a second provider and local methods included.
4. Yuno at run rate: $21,000 a month, 0.47% of TPV, $0.047 per successful transaction ($252,000 a year).
5. Yuno at launch (50K): $7,500 a month and nothing per transaction; the first $500K of monthly volume is inside the platform fee.
6. Base net benefit at run rate: $31.8K a month, $381.4K a year (contribution view, net of Yuno's fee).
7. Base gross benefit $633.4K a year against $252.0K of Yuno fees: 2.5x.
8. Break-even: about 12.3K successful transactions a month ($0.12M TPV), base case.
9. Payback on the ramp: cumulative net benefit turns positive in Dec 2026 (base); the optimistic case turns positive in Dec 2026; the conservative case turns positive in Sep 2027.
10. GMV view at run rate, base: $2.8M a year of incremental GMV and savings ($233.1K a month).
11. Small ticket: at the $5 median, Yuno's usage is $0.020 per transaction in tranche 1, $0.015 in tranche 2, $0.010 in tranche 3 and $0.005 in tranche 4 against $0.05 or $0.10 for a fixed fee; at 450K transactions Yuno all-in is 0.63% of TPV against 1.0% or 2.0%.
12. Scenario range at run rate: conservative +$5.2K a month, base +$31.8K, optimistic +$67.1K a month (+$805.7K a year).

## Section F · Break-even by gross margin (run rate)

All-in Yuno cost at the $4.5M run rate: $21,000 a month = 46.7 bps of TPV (0.47%). The question a CFO asks: how much more approved volume does Carry1st need for the fee to pay for itself out of its own margin? Incremental approved sales needed = all-in bps / gross margin.

| Carry1st gross margin on GMV | Incremental approved sales needed to cover the Yuno fee |
|---|---|
| 10% | about +4.7% |
| 15% | about +3.1% |
| 20% | about +2.3% |
| 30% | about +1.6% |

Yuno's published authorization uplift of 7% (y.uno) covers every one of these thresholds; the base case in this deck uses +3 points on a 75% baseline, i.e. +4.0% more approved volume, before the MDR and local-method levers.

Marginal Yuno usage on a median $5 purchase: $0.020 in tranche 1 (40 bps), $0.015 in tranche 2 (30 bps), $0.010 in tranche 3 (20 bps), $0.005 in tranche 4 (10 bps). On the $10 average purchase: $0.040, $0.030, $0.020, $0.010.

## Inputs to swap when Carry1st's data arrives (Inputs sheet, yellow cells)

| Input | Today | Replace with | Owner |
|---|---|---|---|
| Baseline provider all-in cost | 4.5% ESTIMATE | EBANX's quoted all-in rate to Carry1st by country (incl. FX and taxes) | Cordel |
| Volumes by tier and ramp | 50K / 100K / 200K / 450K, linear ramp | Written volume projections by country | Cordel |
| Average and median ticket | $10 / $5 | Shop data by country | Cordel |
| Take rate on GMV | 15% | Carry1st Shop margin on top-ups and gift cards | Cordel |
| Baseline approval | 75% | Saudi / Africa approval and method mix as proxy, then LatAm actuals | Cordel, Yuno |
| Local-method uplift | 0.5 / 1 / 2% | Method mix by country once live; EBANX direct coverage per country | German, research |
| Engineer-weeks, maintenance and loaded cost | 2 / 3 / 4 weeks per market, 4 / 6 / 8 weeks per later integration, 0.25 / 0.5 / 1.0 FTE maintenance, $2,000 a week | Fatih's estimate for EBANX per-market work, a direct PSP integration, upkeep and his team cost | Fatih |
| Net incremental GMV of processing cost | 1 (yes) | Keep at 1 for a CFO audience; 0 shows the simpler GMV x take rate view (base break-even moves to about 7.3K) | German |
