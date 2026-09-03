# Prompt Claude Design: add two Business Case slides to the FlightHub proposal (2026-09-03)

Target: the deck **"Proposal - FlightHub + Yuno"** (the one open in the canvas). Add a **Business Case section with two slides**, inserted right before the "Proposal" section divider (before the pricing slide). Also add "Business Case" to the agenda slide between "Why Yuno?" and "Proposal", and create a section divider slide for it matching the existing divider style. Match the deck's visual system exactly: Yuno blue (#3B4BF9), dark ink text, "⠿ yuno" wordmark, same fonts and card language. All figures in USD, copy in English. Do not use em-dashes anywhere in the copy.

Audience note: the reader is a quantitative product manager who built FlightHub's internal routing platform, plus a CFO whose two stated KPIs are "lower my cost and accept more." Every claim below is framed as a testable lift on a stated baseline, never as a capability boast, and nothing implies their internal build was a mistake. Keep that tone.

## Slide 1 of 2: Value levers

Replicate this exact layout (it is the standard Yuno value-levers slide): blue vertical accent bar top left, a blue "With Yuno" pill, wordmark top right, headline in Yuno blue, then a four-column matrix with numbered circular badges, and three impact rows at the bottom of each column.

**Headline:** "On $4.9B of annual volume, small performance lifts compound into meaningful impact"

**Two group headers above the columns:** "Operational levers" spanning columns 1 and 2, "Cost levers" spanning columns 3 and 4. Light lilac header tabs with a blue underline, exactly like the reference style.

**The four columns.** Each has: badge number, lever name in blue, a large bold metric, and a short description. Row labels on the left edge: "Lever", "How it works", then "Conservative", "Average", "Optimistic".

**Column 1: Conversion uplift**
- Metric: **+1.5-2.5%**
- Description: "FlightHub processes on raw encrypted PANs today, with no network tokens. Issuing network tokens across all seven providers and routing each transaction to the best-approving acquirer lifts card approval rates and wins back good customers declined at checkout."
- Conservative: **+$11.0M/yr** · Average: **+$14.6M/yr** · Optimistic: **+$18.3M/yr**

**Column 2: Smart Routing & Retries**
- Metric: **+0.75-1.25%**
- Description: "Today a decline falls to the next processor in a fixed order. Yuno extends the routing rules FlightHub already built with real-time retries across all seven providers, on 50+ dimensions such as BIN, issuer country and currency, recovering valid transactions that stop at a single provider."
- Conservative: **+$5.5M/yr** · Average: **+$7.3M/yr** · Optimistic: **+$9.1M/yr**

**Column 3: Processing cost reduction**
- Metric: **7.5-12.5 bps**
- Description: "FlightHub already processes locally through multiple entities to cut cost. Yuno automates that logic per transaction and unifies cost visibility across all seven providers, adding the volume leverage to renegotiate acquirer rates and compress the effective MDR."
- Conservative: **+$3.7M/yr** · Average: **+$4.9M/yr** · Optimistic: **+$6.1M/yr**

**Column 4: Run-ops reduction**
- Metric: **4-5 FTE**
- Description: "Seven provider integrations are maintained in-house today, with Wex landing next, and one person reconciles pay-ins and payouts manually across a multi-MID model. Yuno maintains every integration and reconciles all providers into one ledger, so the team keeps owning routing strategy instead of plumbing."
- Conservative: **+$0.40M/yr** · Average: **+$0.45M/yr** · Optimistic: **+$0.50M/yr**

Impact-row styling like the reference: Conservative row on a near-white tint, Average row highlighted on a light blue tint (#EEF0FF), Optimistic row plain. Values in Yuno blue, bold.

**Assumptions band** (small type, light neutral band, under the matrix): "Assumptions: Base case 700K monthly transactions (est., pending FlightHub confirmation), $580 average ticket (stated range $500 to 700), $406M monthly TPV, $4.87B annual. Approval levers valued at net level: incremental approved volume x ~15% travel-OTA net take benchmark; a +2% approval lift is ≈$97M/yr in recovered gross bookings. Cost levers at full value. Illustrative ±25% ranges; +3% total approval uplift split 2% conversion / 1% retries. Run-ops: 4 to 5 FTE avoided at ~$100K fully loaded. To be calibrated with FlightHub's real volumes and baseline approval rate."

**Bottom banner** (centered, Yuno blue, bold, thin blue rule above it): "The estimated annual value can be monetized much earlier than with alternative solutions thanks to an expected time to market of 4-6 weeks leveraging Yuno's existing capabilities"

## Slide 2 of 2: Total Impact

**Title:** "Total Impact"

**Left, about two thirds of the width: the scenario table.** White rounded table, header row with the four levers and a Total column. The Total column emphasized in Yuno blue.

| Scenario | L1 Conversion uplift | L2 Routing & Retries | L3 Cost reduction | L4 Run-ops | Total annual |
|---|---|---|---|---|---|
| Conservative | $11.0M | $5.5M | $3.7M | $0.40M | **$20.60M** |
| Average | $14.6M | $7.3M | $4.9M | $0.45M | **$27.25M** |
| Optimistic | $18.3M | $9.1M | $6.1M | $0.50M | **$34.00M** |

**Right, about one third: the parameters panel.** A card titled "Parameters", stacked label/value rows:

| Parameter | Value |
|---|---|
| Transactions / Month | 700,000 (est.) |
| Average Ticket | $580 (stated: $500 to 700) |
| TPV / Month | $406,000,000 |
| Annual TPV | $4.87B |
| Live payment providers | 7, plus Wex incoming |
| Network tokens today | None (raw encrypted PAN) |
| Baseline approval rate | To be measured together |

**Footnote** (small grey, under the table): "Net-level impacts per the assumptions on the previous slide. Volume figures are Yuno estimates pending FlightHub confirmation; the case recalibrates once real volumes and baseline approval rate are shared."

## One fix while you are in the deck

The "Why we believe Yuno is the right partner" slide in the Why Yuno? section currently reads "the right partner for **CPD**" in its title, a leftover from another deck. Change "CPD" to "FlightHub". Touch nothing else on that slide.

## What NOT to do

- Do not change the numbers above; every row and total is precomputed so the table sums exactly.
- Do not add an ROI line, a payback line, or any comparison against Yuno's fees on these two slides.
- Do not claim FlightHub's current approval rate, MDR, or processing cost; none was shared, which is why the parameters panel says "to be measured together".
- Do not imply the internal routing platform is inadequate or should be replaced; the framing is always augmentation of what they built.
- Do not touch the pricing slide or any other existing slide beyond the CPD fix above.
- Do not use em-dashes or the phrase "no small feat" anywhere.
