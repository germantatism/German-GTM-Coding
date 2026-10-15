# INTERNAL · Pricing approval memo · Carry1st LatAm Shop (for Justo Benetti and Finance, 15 Oct 2026, pricing v3)

Never in the deck, never shared with Carry1st. Prepared by German Tatis with the numbers agent. Policy references: Yuno Products Pricing Policy (Finance, Laura Galan, DRAFT WIP, read 21 Sep 2026), the Finance cheatsheet and the Pricing Calculator. Re-check the live documents before Salesforce.

## 0. Caveats relayed from German's other session (read first)

- The Finance Pricing Calculator (Google Sheet 1YtGixylPmxoZPe0v1YZnNlejFFcUUfcrrAZPUHofKR0) refused access to the agent. German must run V3 x gaming margin band (M3) himself before any number is quoted; the zone table in section 2 is a pre-check from the policy's own example, not the calculator's output.
- The Finance cheatsheet lists pay-ins at list $0.10 / minimum $0.08 per transaction overall, which contradicts the $0.01 minimum recorded from the pricing-policy document. Section 2 shows the zones under both readings; which one Finance applies decides whether this ladder is yellow or red. Resolve with Laura Galan before quoting.
- An included-TPV allotment on the platform fee is a listed but "not preferred" structure in the policy. It needs Salesforce approval before the quote goes out; do not send the proposal slide before that approval.
- Pocket concessions, kept off every slide: included block widened to $1M (worth $1,500 a month once volume passes it); launch credit $3,750 x 3 months (Dec 2026 to Feb 2027, $11,250 in total, billing start 1 Dec 2026); the 30 to 25 bps step moved from $3M to $2M (worth $500 a month once volume passes $3M); a 3-year rate lock. Section 7 prices each one.

## 1. The structure we want to quote (v3, German's decision 15 Oct 2026)

- Platform fee: $7,500 a month flat, billed annually ($90,000), including the first $500K of monthly Net TPV (single month, no rollover). Net TPV = successful transactions only, no declines, no chargebacks.
- Usage on monthly Net TPV above the block, ladder (each band on the volume inside it): 30 bps from $500K to $3M; 25 bps from $3M to $6M; 20 bps above $6M.
- Billable event: successful pay-in. Declines, verification attempts and sandbox never billed. Usage monthly in arrears, net 30. Add-ons (network tokens, 3DS) on usage, quoted separately.
- Segmentation: gaming = M3 (healthy margin). Volume: V2 at launch (50K a month), V3 by the opportunity (450K a month by end 2027). Policy says size by the opportunity, so treat as V3.
- Check figures at a $10 ticket: 50,000 tx / $0.5M = $7,500 (1.50%, $0.150 per tx); 100,000 tx / $1.0M = $9,000 (0.90%, $0.090 per tx); 200,000 tx / $2.0M = $12,000 (0.60%, $0.060 per tx); 450,000 tx / $4.5M = $18,750 (0.42%, $0.042 per tx). Annual at 450K: $225,000.

## 2. Equivalent $ per transaction by tranche, and the zone it lands in

Reading A (pricing-policy document): list $0.10, minimum $0.01. Using the proportions of the policy's own example (list $0.030, minimum $0.020: green $0.030 to $0.024, yellow $0.023 to $0.020), green runs from $0.10 down to about $0.046 and yellow from about $0.045 to $0.01. Reading B (Finance cheatsheet): list $0.10, minimum $0.08, so green about $0.10 to $0.088 and yellow $0.087 to $0.080; anything under $0.08 is red.

| Tranche | Rate (bps) | $ per tx at $10 avg | Zone A ($0.01 min) | Zone B ($0.08 min) | $ per tx at $5 median | Zone A | Zone B | Ticket at which the rate equals $0.01 |
|---|---|---|---|---|---|---|---|---|
| 1 ($500K to $3M) | 30 | $0.030 | yellow | red | $0.015 | yellow | red | $3.33 |
| 2 ($3M to $6M) | 25 | $0.025 | yellow | red | $0.0125 | yellow | red | $4.00 |
| 3 (above $6M) | 20 | $0.020 | yellow | red | $0.010 | on the minimum | red | $5.00 |

Blended all-in per successful transaction (platform fee + usage): at a $10 ticket $0.150 at 50,000, $0.090 at 100,000, $0.060 at 200,000, $0.0417 at 450,000; at a $5 ticket $0.150 at 50,000, $0.075 at 100,000, $0.045 at 200,000, $0.0283 at 450,000. Usage-only per transaction at the $5 median: $0.000 at 50,000, $0.000 at 100,000, $0.0075 at 200,000, $0.0117 at 450,000.

Exposure under reading A: the 20 bps band equals $0.010 per transaction exactly at a $5 ticket and falls under $0.01 whenever the average ticket of the billable volume is below $5.00; the 25 bps band crosses at $4.00 and the 30 bps band at $3.33. Carry1st's median is $5, so this is not a tail case for tranche 3. The contract therefore needs the safeguard in section 6 (option F2): usage billed at the tranche rate or $0.01 per successful transaction, whichever is higher. Under reading B every tranche is under the $0.08 minimum per transaction and the whole ladder is red (Global Controller / CFO + CRO, 5 business days), unless Finance evaluates a bps-on-TPV price against a TPV-based minimum instead; ask Laura Galan which scale applies to the % basis.

## 3. Platform fee against the catalog

| Reading | Figure | Comparison | Zone |
|---|---|---|---|
| V2 sizing (launch, 25K to 100K tx) | $7,500 | List $7,000, minimum $4,000 | above list, green |
| V3 sizing (opportunity, 100K to 1M tx) | $7,500 | List $10,000, minimum $4,000 | below list, above minimum, yellow |
| Included $500K valued at the tranche 1 rate | $1,500 a month | Platform fee net of the allotment: $6,000 | above the $4,000 minimum, below V2 list |
| Pocket concession: included $1M valued at the tranche 1 rate | $3,000 a month | Platform fee net of the allotment: $4,500 | above the $4,000 minimum, below V2 list |

The policy accepts an allotment on the platform fee ("not preferred, single-month, no rollover"), so the structure is inside the toolkit but needs the manual review that yellow implies and Salesforce approval before the quote leaves Yuno. Billing annual upfront is standard; monthly billing of the platform fee, if Carry1st asks, is a second yellow item.

Deal size check: "overall deal size cannot be under 10k" (the draft does not say monthly or annual). At launch the monthly bill is $7,500 ($90,000 a year); the monthly bill crosses $10,000 at about 133,333 transactions ($1.33M TPV). If Finance reads the rule as monthly, ask for the exception on the strength of the ramp to $18,750 a month.

## 4. Why bps on Net TPV is within policy as the price basis

- Pay-ins page: price basis may be fixed $ or % of TPV; models Flat, Tranches (default) or Tiers; ranges in transactions or in TPV. We use % of TPV with tranches by TPV: the default model on an allowed basis.
- TPV definition matches the policy: Net TPV of successful transactions, no declines, no chargebacks.
- Units match (Justo's rule): the included block is in TPV because the usage is in bps on TPV. An allotment in transactions on a bps price is not billable without an average-ticket conversion, which is why v1 was dropped.
- Why we need it for this merchant: average ticket $10, median $5, with a reseller margin on GMV (take rate about 15%, to validate). A fixed $0.05 per transaction is 1.0% of TPV at the median ticket and about 7% of Carry1st's contribution on that sale; $0.10 is 2.0% and about 13%. Cordel named fixed fees as the sensitivity on the discovery call (15 Oct 2026).
- Where it lands against the brief's corridor: Justo asked for about 0.5 to 0.7% of TPV all-in at 450K. v3 lands at 0.42% (41.7 bps), below the corridor, which is what makes the conservative business case break even at about 269K transactions a month instead of only at the run rate.

## 5. What needs sign-off

| Item | Why | Approver per policy | SLA |
|---|---|---|---|
| Platform fee $7,500 with a $500K Net TPV allotment | Allotment is "not preferred"; fee below V3 list; Salesforce approval required before the quote | RevOps / Sales Ops / GM (yellow) | 2 business days |
| Usage rates 30 / 25 / 20 bps | Equivalent $0.030 / $0.025 / $0.020 at $10 and $0.015 / $0.0125 / $0.010 at $5: yellow under the $0.01 reading, red under the $0.08 reading | RevOps / Sales Ops / GM (yellow) or Global Controller / CFO + CRO (red) | 2 or 5 business days |
| bps-on-TPV basis with tranches by TPV | Allowed basis, default model; confirm the calculator reads it the same way for V3 x M3 and which per-transaction minimum applies | Finance (Laura Galan) | with the above |
| Small-ticket exposure at and under a $5 ticket | 20 bps = $0.010 at $5, below $0.01 under it | Finance: contract-side safeguard (section 6, F2) | with the above |
| Monthly instead of annual platform billing (only if Carry1st asks) | Yellow by policy | RevOps / Sales Ops / GM | 2 business days |
| Deal size under $10K a month at launch (if read monthly) | $7,500 a month at launch | Finance | with the above |
| Launch credit $3,750 x 3 months (only if used) | Credits allowed against the platform fee for named months, written in contract, no rollover; above a size threshold needs sign-off | Finance | with the above |

## 6. Fallback if the % basis is refused

Option F1, fixed $ tranches with the same yield at the $10 ticket (on a fixed-$ price the allotment must also be a transaction count, Justo's unit rule): the $500K block converted at the $10 ticket (50,000 tx) as the allotment on the $7,500 platform fee; $0.030 per successful transaction to 300,000; $0.025 to 600,000; $0.020 above. At 450K this bills the same $18,750 a month. The cost: at the $5 median the fee becomes 0.60% / 0.50% / 0.40% of TPV, exactly the fixed-fee shape Cordel objected to; expect pushback and a request for lower cents.
Option F2, bps on Net TPV with an internal per-transaction safeguard: the same 30 / 25 / 20 bps, with the contract defining usage as "the tranche rate, or $0.01 per successful transaction, whichever is higher". Customer-facing text stays as in the proposal slide; the clause appears only in the contract's billing definitions. This answers the $0.01 reading; it does not answer the $0.08 reading.
Option F3, tiers (cliff) instead of tranches: not recommended; the policy says tiers cede more margin and the small-ticket argument does not need them.
Option F4, if Finance wants the allotment out: platform fee $7,000 (V2 list) with no included block, usage from the first dollar at the same rates. At 50K that bills $7,000 + $1,500 = $8,500 a month (1.70% of TPV), worse for the launch story Justo asked for; use only as a last resort.

## 7. Pocket concessions, priced (internal only)

| Concession | Yuno revenue given a month | Where it bites | Carry1st base net at 450K | Base break-even |
|---|---|---|---|---|
| As quoted (v3): $500K included, step at $3M | 0 | reference | +$29.1K | about 65.3K |
| Included block to $1M | $1,500 once TPV passes $1M | 100K tier: Yuno $7,500 instead of $9,000; 450K: $17,250 | +$30.6K | about 60.7K |
| 30 to 25 bps step moved from $3M to $2M | $500 once TPV passes $3M | 450K: Yuno $18,250 | +$29.6K | about 65.3K |
| Launch credit $3,750 x 3 months | $11,250 in total (Dec 2026 to Feb 2027) | ramp only; Yuno over the ramp $162.2K instead of $173.4K | payback Dec 2026 instead of Jan 2027 | n/a |
| 3-year rate lock | none today; forgoes the annual tranche review | contract term | n/a | n/a |

## 8. Business case numbers Finance will ask about (base case, contribution view)

- Yuno revenue: $7,500 a month at 50,000; $9,000 a month at 100,000; $12,000 a month at 200,000; $18,750 a month at 450,000 ($225,000 a year). Over the modeled 13-month ramp (Dec 2026 to Dec 2027, linear): $173,417.
- Carry1st net benefit after Yuno's fee: ($1,125) at 50,000; $2,550 at 100,000; $9,900 at 200,000; $29,063 at 450,000 ($348,750 a year at 450K). Break-even about 65.3K transactions a month; cumulative payback Jan 2027 on the linear ramp. Conservative: break-even about 269K, payback not within the ramp. Optimistic: break-even about 28.7K, payback Dec 2026.
- Switch "Net incremental GMV of processing cost" to 0 (GMV x take rate, the simpler view) and the base case covers the $7,500 at about 48.0K transactions, $250 a month at 50K and $39,000 a month at 450K. We keep the netted view as the default because a CFO-type buyer will net it anyway.
- Option A vs Option B all-in at 450K, base: $202,500 vs $198,750 a month ($45.0 vs $44.2 per $1,000 TPV). The pitch to Carry1st is "a lower cost line with failover, a second provider and local methods included; the revenue levers are on top".

## 9. Open items before Salesforce

- Run the Pricing Calculator for V3 x M3 (German, access refused to the agent) and confirm the per-transaction minimum that applies to a bps-on-TPV price.
- EBANX and dLocal rates through Yuno in BR, AR, MX, CO; Bolivia pay-in coverage (owner Justo / partnerships). Never quote them to Carry1st.
- Cordel's EBANX direct quote: replaces the 4.5% baseline on the Inputs sheet (first thing to swap).
- Volumes by country and launch scope (BR only vs all five) change the V-segment and the ramp.
- Confirm with Laura Galan that an included block expressed in Net TPV on a bps price is acceptable as written, and that the allotment is approved in Salesforce before the slide is shown.
- If bc_model.xlsx ever leaves Yuno, delete Inputs section 9 (launch credit switch) and this memo stays internal.
