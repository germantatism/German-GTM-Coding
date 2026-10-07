# Value model: levers, formulas, defaults, guardrails

Contents: [Choosing levers](#choosing-levers) · [Lever catalog](#lever-catalog) · [Default parameters](#default-parameters-conservative) · [Guardrails](#guardrails-these-came-from-real-mistakes) · [Scenarios, floor and return](#scenarios-floor-and-return) · [Appendix pages to generate](#appendix-pages-to-generate)

The numbers must survive a payments lead with a spreadsheet. Build the model in a scratch script or sheet so every slide figure is computed, not typed. If German also wants the Excel, pass the same assumptions to `/business-case`.

## Choosing levers

Pick 3-4 that fit how this merchant makes money. More levers dilute credibility.

| Merchant model | Usually the strongest levers |
|---|---|
| Consumer subscription / AI / SaaS, global | Local methods (audience expansion) · local acquiring on the cross-border slice · renewal recovery · processing cost |
| Creator / marketplace / platform | Approval + renewal on existing book · cross-border reclassification · local methods · payouts orchestration |
| Gaming / apps with store fees | Channel mix (store → direct) · international monetization gap · approval · payouts |
| Airline / travel / ticketing | Resilience (cost of outage) · approval by decline code · processing cost via multi-acquirer leverage · reconciliation |
| Mid-market multi-PSP | Routing + retries · conversion from missing methods · cost (bps) · run-ops (FTE, reconciliation) |
| High-dispute merchants | Redundancy as insurance against scheme monitoring · dispute tooling · approval |

## Lever catalog

**L1 · Audience expansion through local payment methods**
`Incremental users = Demand base × (conversion with local methods − conversion today)`
`Value = Incremental users × ARPU`
- Demand base = active users or checkout starts in the market, not population.
- If the merchant already offers the main local method through their PSP, the uplift is small (+0.5-1.0pp); the play becomes recurring-native versions (Pix Automático, UPI AutoPay, SEPA DD) and local acquiring.
- Distinguish recurring-native methods from acquisition-only methods (Konbini, OXXO, cash vouchers).
- Use localized ARPU; a US list price is too high for most emerging markets.

**L2 · Authorization uplift through local acquiring and routing**
`Value = Card volume on the cross-border slice × avoidable decline gap × recoverable share`
- First apply it to the **existing** cross-border card volume (their current book), then to any incremental card attempts created by L1.
- The ~+10pp first-attempt lift applies only to the slice moved from cross-border to local routes. Net effect on total international volume is typically **+2-3%**, and lower when the baseline is already above 90%. Put the reconciliation in a footnote.
- Adding a second/third acquirer on a local route: +1-3pp and lower variance.

**L3 · Renewal continuity (retries, network tokens, account updater, cross-PSP fallback)**
`Value = Paid base × monthly involuntary failure rate × incremental recovery × remaining value per saved renewal`
- Baseline: the incumbent's own smart retries already recover a share (Stripe cites ~38% at default). Only the increment counts. If the architecture removes the incumbent's retries (e.g. a billing bridge), you must first replace that baseline.
- Apply to the existing subscriber book first.

**L4 · Processing cost**
- Cross-border → domestic reclassification: ~60 bps on the reclassified volume.
- Shift of international volume to cheaper local methods: ~300 bps on the shifted share (assume ~10% of international).
- Level 2/3 data on commercial cards: ~40 bps on ~7.5% of volume.
- Multi-acquirer negotiating leverage: 7.5-12.5 bps on total volume (mid-market).
- Unbundled processor add-ons the merchant pays today (billing %, tax %, optimization %, per-3DS, per-token) where Yuno's price is lower; large merchants are on custom pricing, so ask before claiming.

**L5 · Channel mix (gaming / apps)**
`Value = Bookings shifted from store to direct (pts) × bookings × (store fee − direct cost)`. The store fee itself is not Yuno-addressable; Yuno's surface is making direct rails performant enough that users complete there. Say this in a guardrail box.

**L6 · Payouts orchestration**: FX margin + per-payout fees + ops across the payout providers, on the payout flow only.

**L7 · Resilience**: `Revenue per hour at peak × expected outage hours avoided`. Anchor on a real incident if one is known (theirs or their processor's).

**L8 · Build vs buy / run-ops**: engineers avoided × fully loaded cost + infra/compliance + time-to-value. Anchor on their disclosed engineering headcount and what they say engineers should be working on. Mid-market: 3-5 FTE. Large enterprise build: 25-45 engineers, 12-18 months before value.

**L9 · Reconciliation and finance ops**: hours saved, close time, leakage found. Often the wedge for smaller US deals.

## Default parameters (conservative)

Use merchant data whenever it exists. These are fallbacks; label them [A] or [Y] and put them in the appendix.

| Parameter | Default | Basis |
|---|---|---|
| Smart retry recovery | 0.5% of GMV | Samuel's conservative framework |
| Multi-acquirer retry recovery | 0.3% of GMV | same |
| 3DS flow optimization | 0.2% on 3DS-required volume | same |
| Account updater lift | 1.0% on renewal volume | same |
| Network-token approval lift | +1-2pp on tokenized card volume | Yuno decks; verify current figure |
| Net auth uplift on international book | +1% / +2% / +3% (cons./base/upside), capped on >90% baselines | Roblox case |
| Cross-border → local first-attempt lift | ~+10pp on the moved slice (83% → 93%) | Yuno performance dashboard, 24-month aggregate [Y] |
| 2nd/3rd acquirer | +1-3pp (93 / 94 / 96%) | same [Y] |
| Free→paid conversion today | EM 0.5-1.5% · DM 2-3% | subscription benchmarks [A] |
| Conversion uplift from local methods | EM full-stack +1.5-2.0pp · mature/APM-led +1.0pp · where main method already live +0.5pp | Conservative end of Germán's range; his AI decks used +3-5.5pp, treat that as upside |
| Monthly involuntary renewal failure | DM 2.5% · EM 3.5% (conservative); benchmarks cite 5-7%+ | [A] |
| Incremental renewal recovery | 40% of failed renewals rescued × 0.78 incrementality, or +25pp over baseline | [A] |
| Contribution margin when claiming profit | ask; else ~55% for digital goods | [A] |
| Mid-market conversion / routing uplift | +0.5-1.0% / +0.75-1.0% | Flair proposal |

Retry recovery by decline code (Yuno US domestic data, Mar 2026, 2nd / 3rd attempt) for airline and US card cases: DO_NOT_HONOR 14.7% / 1.9% · INSUFFICIENT_FUNDS 3.2% / 0.5% · INVALID_SECURITY_CODE 47.4% / 12.7% · EXPIRED_CARD 19.6% / 11.2% · USER_RESTRICTION 14.7% / 0.7% · PROVIDER_INTERNAL_ERROR 63.2% / 6.5% · ACQUIRER_CONTINGENCY 62.6% / 19.4%. Fraud / pick-up / lost-stolen are hard declines: no recovery. Ask German for a refresh if the data is more than six months old.

## Guardrails (these came from real mistakes)

1. **Existing book first.** Sizing approval and renewal levers only on modeled new subscribers made a $700M-revenue merchant's auth lever look like $1.3M. One point on their existing cross-border book was worth more than the whole lever. Always compute "1 point of approval / renewal recovery on the current book = $X" and show it.
2. **Sequential, not additive.** L2 uses the post-L1 base, L3 the post-L1+L2 base. Print the WATERFALL LOGIC note.
3. **Same units as the evidence.** A cited "7-12% relative lift" cannot justify a fivefold conversion jump. If the model needs +2pp absolute on a 0.5% base, cite evidence for that, or lower it.
4. **No headline the merchant's own facts disprove.** If most of their revenue is already international, don't say paid users abroad are "near zero".
5. **Match the revenue mix.** If most revenue is B2B, a consumer-only model contradicts your own industry slide. Size the self-serve business volume too, and exclude invoiced enterprise volume.
6. **State what's not addressable**: store fees, sanctioned markets, volume Yuno cannot process, the incumbent's home markets where performance is already strong (show these as upside outside the base case).
7. **Gross vs net.** Label revenue as "preliminary gross". When claiming profit impact, net out contribution margin, local-method fees, MoR fees and Yuno's cost.
8. **Show the headline as a % of their revenue.** Under ~1% may not move an executive; over ~10% needs very strong evidence. Either way, know it and say it.
9. **One number per fact.** Market counts, MAU, hero number and lever subtotals must be identical on every slide; subtotals must sum to the total.
10. **Sanity-check volumes.** Transactions ≈ revenue / average ticket. A proposal sized at 300K transactions for a business that implies over a million gets noticed.
11. **Pricing is never invented.** Use what German gives you or what is approved for this deal (deal folder, Slack, Gmail). With no deal-specific pricing, use Yuno's standard pricing and label it as standard: the first $50,000 processed is free, then $0.05 per transaction. Never invent tiers or variations of it.
12. **Published Yuno stats only.** "+12% authorization uplift" and "20-30% decline recovery" have no public source and failed deck QA on six decks. Yuno-wide figures are the published 7% authorization uplift and 30% recovered revenue (y.uno), or verified client results (McDonald's +4.7% acceptance across 18 markets, $3.2M additional revenue). Cross-PSP reconciliation is roadmap, not GA: footnote it.
13. **Client-reported metrics win.** If the prospect stated a number (average ticket, TPV, transactions), use it everywhere; a derived number that contradicts it looks inflated (Palco: reported ticket $37.09, a derived $163 had to be undone across the whole deck). Raise the discrepancy with German as a discovery question.
14. **USD only.** No local-currency amounts anywhere, country pages included; use currency-free metrics instead of converting.
15. **Omit, don't fabricate.** A lever, market or stat you cannot source is cut, not padded with a default. Defaults from the table above are allowed only when labeled [A] and listed in the appendix.

## Scenarios, floor and return

- **Three cases**: conservative / base / upside, varying only the two or three swing parameters. Show which lever dominates the base case.
- **Floor**: the subset of levers provable on their data within the sprint or pilot (usually approval + renewal + payouts). The gap between floor and full range is "unlocked by <their data>".
- **Return** (pricing known): `Net benefit = value − all-in Yuno cost`, `ROI = value / cost`, `Payback = cost / (value/12)`. Size Yuno's cost on Yuno-addressable transactions only.
- **Sensitivity** line in the appendix: what the total becomes if the key assumption moves (e.g. MAU ±30%, uplift at +1.0pp vs +3.5pp).
- **Swing variables** slide: name the 3-4 assumptions and the exact data file that settles each (channel-mix split; ISO-8583 decline file by BIN and country; renewal failure and recovery by country; plan mix and ARPU by country).

## Appendix pages to generate

- "How to read the numbers in this deck": working-assumptions table (parameter, value, basis) + caveats and positioning language + sensitivity.
- Lever methodology pages: steps 1-n, the formula in one line, a worked example for the biggest market, an IMPORTANT box ("This is not a claim that every UPI user is incremental...").
- Lever ranking table by market with portfolio total and concentration (top 3, top 10).
- Country pages (see `slide-library.md`).
