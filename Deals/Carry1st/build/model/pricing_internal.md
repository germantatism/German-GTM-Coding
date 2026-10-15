# INTERNAL · Pricing approval memo · Carry1st LatAm Shop (for Justo Benetti and Finance, 15 Oct 2026)

Never in the deck, never shared with Carry1st. Prepared by German Tatis with the numbers agent. Policy reference: Yuno Products Pricing Policy (Finance, Laura Galan, DRAFT WIP, read 21 Sep 2026) and the pricing calculator; re-check the live doc before Salesforce.

## 1. The structure we want to quote

- Platform fee: $7,500 a month, billed annually ($90,000), including the first 50,000 successful transactions each month (single-month allotment, no rollover).
- Usage above the block, % of billable TPV in tranches (ladder): 0.45% on monthly TPV to $2M; 0.35% from $2M to $4M; 0.30% above $4M. Billable TPV = TPV x max(0, 1 minus 50,000 / transactions), i.e. the TPV of the transactions above the block at the month's average ticket (order-independent, easy to bill).
- Billable event: successful pay-in. Declines, verification attempts and sandbox never billed. Usage monthly in arrears, net 30. Add-ons (network tokens, 3DS) on usage, quoted separately.
- Segmentation: gaming = M3 (healthy margin). Volume: V2 at launch (50K a month), V3 by the opportunity (450K a month by end 2027). Policy says size by the opportunity, so treat as V3.

## 2. Equivalent $ per transaction by tranche, and the zone it lands in

Pay-ins catalog: list $0.10 per successful transaction, minimum $0.01. Using the proportions of the policy's own example (list $0.030, minimum $0.020: green $0.030 to $0.024, yellow $0.023 to $0.020), the green band runs from $0.10 down to about $0.046 and yellow from about $0.045 to $0.01. The calculator gives the real zones for a V3 x M3 merchant; the table below is the pre-check.

| Tranche | Rate, % of TPV | $ per tx at $10 avg ticket | Zone at $10 | $ per tx at $5 median | Zone at $5 | Ticket at which the rate hits $0.01 |
|---|---|---|---|---|---|---|
| 1 ($0 to $2M) | 0.45% | $0.045 | yellow (top edge) | $0.0225 | yellow | $2.22 |
| 2 ($2M to $4M) | 0.35% | $0.035 | yellow | $0.0175 | yellow | $2.86 |
| 3 (above $4M) | 0.30% | $0.030 | yellow | $0.015 | yellow | $3.33 |

Blended all-in per successful transaction (platform fee + usage): at a $10 ticket $0.150 at 50K, $0.098 at 100K, $0.071 at 200K, $0.051 at 450K; at a $5 ticket $0.150, $0.086, $0.054, $0.036. Every blended figure is above the $0.01 minimum and, at 50K to 100K, at or above list because the platform fee dominates. Usage-only per transaction at the $5 median: $0.011 at 100K, $0.017 at 200K, $0.019 at 450K, all above $0.01.

Exposure to flag: a % of TPV price falls below the $0.01 per-transaction minimum when the average ticket of the billable volume drops under $2.22 (tranche 1), $2.86 (tranche 2) or $3.33 (tranche 3). Carry1st's average is $10 and median $5, so the exposure is a tail risk (a promotional month of very small top-ups). Options for Finance: (a) accept, given the platform fee carries the blended figure well above the minimum; (b) a contract clause "usage is billed at the tranche rate or $0.01 per successful transaction, whichever is higher", which is internal protection, never a customer-facing number; (c) a rate review trigger if the monthly average ticket falls under $5 for two consecutive months.

## 3. Platform fee against the catalog

| Reading | Figure | Comparison | Zone |
|---|---|---|---|
| V2 sizing (launch, 25K to 100K tx) | $7,500 | List $7,000, minimum $4,000 | above list, green |
| V3 sizing (opportunity, 100K to 1M tx) | $7,500 | List $10,000, minimum $4,000 | below list, above minimum, yellow |
| Included 50,000 transactions valued at the tranche 1 rate ($0.5M x 0.45%) | $2,250 a month | Platform fee net of the allotment: $5,250 | still above the $4,000 minimum |
| Included 50,000 transactions valued at $0.01 | $500 a month | $7,000 (V2 list) + $500 = $7,500 | the allotment is priced at the minimum, the fee at V2 list |

The policy accepts an allotment of included transactions on the platform fee ("not preferred, single-month, no rollover"), so the structure is inside the toolkit but needs the manual review that yellow implies. Billing annual upfront is standard; if Carry1st asks for monthly billing of the platform fee, that is a second yellow item.

Deal size check: "overall deal size cannot be under 10k" (the draft does not say monthly or annual). At launch the monthly bill is $7,500 ($90,000 a year); the monthly bill crosses $10,000 at about 105,000 transactions ($1.05M TPV). If Finance reads the rule as monthly, ask for the exception on the strength of the ramp to $22,750 a month.

## 4. Why % of TPV is within policy as the price basis

- Pay-ins page: price basis may be fixed $ or % of TPV; models Flat, Tranches (default) or Tiers; ranges in transactions or in TPV. We use % of TPV with tranches by TPV: the default model on an allowed basis.
- TPV definition matches the policy: net TPV of successful transactions, no declines, no chargebacks.
- Why we need it for this merchant: average ticket $10, median $5, with a reseller margin on GMV (take rate about 15%, to validate). A fixed $0.05 per transaction is 1.0% of TPV at the median ticket and about 7% of Carry1st's contribution on that sale; $0.10 is 2.0% and about 13%. Cordel named fixed fees as the sensitivity on the discovery call (15 Oct 2026). The % basis keeps Yuno's share of the sale constant and keeps the deal.
- Where it lands against the brief's corridor: Justo asked for about 0.5 to 0.7% of TPV all-in at 450K. We land at 0.51% ($22,750 a month). The low end was chosen on purpose: at 0.51% the conservative business case (25 bps, +1.5 pts, +0.5%) is cost-neutral at the run rate (+$0.5K a month); at 0.6% it would be negative in every tier, which we could not show to a CFO-type buyer.

## 5. What needs sign-off (all yellow, nothing red at the quoted numbers)

| Item | Why | Approver per policy | SLA |
|---|---|---|---|
| Platform fee $7,500 with a 50,000-transaction allotment | Allotment is "not preferred"; fee below V3 list | RevOps / Sales Ops / GM (yellow) | 2 business days |
| Usage rates 0.45% / 0.35% / 0.30% | Equivalent $0.045 / $0.035 / $0.030 at $10, inside the yellow band | RevOps / Sales Ops / GM (yellow) | 2 business days |
| % of TPV basis with tranches by TPV | Allowed basis, default model; confirm the calculator reads it the same way for V3 x M3 | Finance (Laura Galan) | with the above |
| Small-ticket exposure under $2.22 to $3.33 | Rate can fall under $0.01 per tx on a very low ticket month | Finance view: accept, clause, or review trigger | with the above |
| Monthly instead of annual platform billing (only if Carry1st asks) | Yellow by policy | RevOps / Sales Ops / GM | 2 business days |
| Deal size under $10K a month at launch (if read monthly) | $7,500 a month until about 105K tx | Finance | with the above |

Red would only be triggered if the tranche rates were cut below the equivalent of $0.01 per transaction at the quoted ticket, or the platform fee below $4,000. Neither is proposed.

## 6. Fallback if the % basis is refused

Option F1, fixed $ tranches with the same yield at the $10 ticket (keeps the included block): first 50,000 transactions included in the $7,500 platform fee; $0.045 per successful transaction from 50,001 to 200,000; $0.035 from 200,001 to 400,000; $0.030 above 400,000. At 450K this bills the same $22,750 a month. The cost: at the $5 median the fee becomes 0.9% / 0.7% / 0.6% of TPV, exactly the fixed-fee shape Cordel objected to; expect pushback and a request for lower cents.

Option F2, % of TPV with an internal per-transaction safeguard: the same 0.45% / 0.35% / 0.30%, with the contract defining usage as "the tranche rate, or $0.01 per successful transaction, whichever is higher". Customer-facing text stays as in the proposal slide; the clause appears only in the contract's billing definitions. This answers the minimum-price concern without changing the quoted shape.

Option F3, tiers (cliff) instead of tranches: not recommended; the policy says tiers cede more margin and the small-ticket argument does not need them.

Option F4, if Finance wants the allotment out: platform fee $7,000 (V2 list) with no included block, usage from the first transaction at the same rates. At 50K that bills $7,000 + $2,250 = $9,250 a month (1.85% of TPV), worse for the launch story Justo asked for; use only as a last resort.

## 7. Business case numbers Finance will ask about (base case, contribution view)

- Yuno revenue: $7,500 a month at 50K; $9,750 at 100K; $14,250 at 200K; $22,750 at 450K ($273,000 a year). Over the modeled 13-month ramp (Dec 2026 to Dec 2027, linear): $203,500.
- Carry1st net benefit after Yuno's fee: ($1,125) a month at 50K; +$1,762 at 100K; +$7,538 at 200K; +$24,862 at 450K ($298K a year). Break-even about 69,500 transactions a month; cumulative payback Feb 2027 on the linear ramp.
- Switch "Net incremental GMV of processing cost" to 0 (GMV x take rate, the simpler view) and the base case covers the $7,500 at about 48,000 transactions, +$250 a month at 50K and +$35,000 a month at 450K. We keep the netted view as the default because a CFO-type buyer will net it anyway.
- Option A vs Option B all-in at 450K, base: $202,500 vs $202,750 a month. The pitch to Carry1st is "same cost line, with failover, a second provider and local methods included; the levers are the upside", not "cheaper processing".

## 8. Open items before Salesforce

- EBANX and dLocal rates through Yuno in BR, AR, MX, CO; Bolivia pay-in coverage (owner Justo / partnerships). Never quote them to Carry1st.
- Cordel's EBANX direct quote: replaces the 4.5% baseline on the Inputs sheet (first thing to swap).
- Volumes by country and launch scope (BR only vs all five) change the V-segment and the ramp.
- Confirm with Laura Galan whether tranche ranges in TPV with a transaction-count allotment is acceptable as written, or whether the allotment must also be expressed in TPV ($500,000 at the $10 ticket).
