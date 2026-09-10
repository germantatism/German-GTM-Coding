# Prompt Claude Design: Appmaking + Yuno pricing proposal, ramp-up fixed fee (2026-09-10)

Build one 16:9 pricing slide (1920x1080): **"Proposal · Ramp-up fixed fee"**, for the commercial proposal **Appmaking + Yuno**. Use the attached FlightHub pricing slide (page 15 of "Proposal - FlightHub + Yuno") as the exact visual reference: replicate its layout, typography and color system, only the content and the block structure described below change. All figures in USD, monthly billing, copy in English.

## Visual system (match the reference exactly)

- Background: light lavender grey (#E9E9F3). Ink text (#20222A). Yuno blue (#3B4BF9) for fees and accents.
- "⠿ yuno" wordmark top right in Yuno blue, thin horizontal divider under the header area, small "Pricing" page label, slide number bottom left.
- Three blocks: a wide left block for the fee ladder, a right column with the "fully ramped" card and the pending list, and a full-width band at the bottom with what it means for Appmaking.

## Left block: the fee ladder

1. Boxed title (thin dark border, uppercase, large, exactly like the reference): **"A FIXED FEE THAT GROWS SLOWER THAN YOUR VOLUME"**
2. Under the title, one line in regular weight: "One monthly fee, all-in. It steps up as you ramp and stops at 150,000. Your cost per successful transaction falls at every step."
3. A white rounded table with five columns: **Step | Successful transactions / month | Expected | Fixed fee / month | All-in per successful txn**. Fees in Yuno blue, bold. Rows, exactly these values:

| Step | Successful transactions / month | Expected | Fixed fee / month | All-in per successful txn |
|---|---|---|---|---|
| 1 | 0 to 25,000 | Months 1 to 3 | $6,500 | $0.26 |
| 2 | 25,001 to 50,000 | Months 4 to 5 | $8,000 | $0.16 |
| 3 | 50,001 to 100,000 | Months 6 to 7 | $10,000 | $0.10 |
| 4 | 100,001 to 150,000 | Months 8 to 9 | $13,000 | $0.087 |
| Fully ramped | Above 150,000 | Month 10 onward | $13,000 + $0.03 per successful txn above 150,000 | Falls toward $0.03 |

   The "Fully ramped" row gets the light blue filled treatment used for the highlighted row in the reference. The "All-in per successful txn" column is the fee divided by the top of the band; label it in the header sub-line as "at the top of the band".
4. Small grey footnote under the table: "The step is set by successful transactions in the month, not by the calendar. Declines cost nothing. No setup fee. Expected months follow Appmaking's ramp plan."

## Right column: fully ramped card + pending items

1. **Fully ramped card** (light rounded card, the dollar figure large and bold, same style as the Platform Fee card in the reference): **"Fully ramped: $13,000 / month"**. Sub-line: "$156,000 / year at 150,000 successful transactions. This is what covers the stack."
2. Under the figure, a **"WHAT IT INCLUDES"** list in the same row style as the reference (label left, value right in Yuno blue):
   - Dedicated KAM and TAM · Included
   - Payment methods · +1,000
   - Payment providers · +450
   - Anti-fraud tools · +50
   - Orchestration & rules engine · Included
   - Smart routing & retries · Included
   - One grey sub-line under the block: "Every connector maintained by Yuno. Adding a provider later is a routing change, not a new fee."
3. Below, a stacked list under a small header **"PENDING SCOPING"**, values in grey italic "Pending":
   - Subscriptions engine (standalone) · Pending
   - Token vault & network tokens · Pending
   - Reconciliation · Pending
   - Verifi & Ethoca alerts · Pending
   - One grey sub-line: "Priced separately once scoped together. Not part of the fixed fee."

## Bottom band: what it means for Appmaking

Full-width light band, same style as the "WHAT IT MEANS FOR FLIGHTHUB" block in the reference. Header: **"WHAT IT MEANS FOR APPMAKING"**, sub-header: "On the ramp plan above". Three short stat columns:

- **Months 1 to 9:** $81,500 for about 600,000 successful transactions, about $0.14 each
- **Months 10 to 12:** $39,000 at 150,000 successful transactions per month, $0.087 each
- **Year 1:** $120,500 for about 1.05M successful transactions, about $0.115 each

One grey line under the three stats: "Volumes are Appmaking's projected ramp. The fee follows actual successful transactions each month."

⚠️ Before generating: if Appmaking's email gives a different month-by-month ramp, replace the "Expected" column and recompute the three bottom stats from it. Do not change the fee ladder.

## What NOT to do

- Do not add a per-transaction fee inside steps 1 to 4. The ramp is fixed fee only; the only per-transaction line is the $0.03 overage above 150,000.
- Do not add a minimum monthly billing line, a contract term, a setup fee, a "$50K processed free" line, or a smart routing / NOVA AI priced row. Nothing beyond the ladder, the fully ramped card, the includes list, the pending list and the bottom band.
- Do not name any PSP (Stripe, Solidgate, Ecompay, etc.) anywhere on the slide.
- Do not invent prices for the pending items. They stay as "Pending" with no number.
- Do not add any claims about Appmaking's approval rates, savings, revenue or comparisons to other pricing structures.
- Do not change, round or reformat the numbers given above.
- Do not use em-dashes anywhere in the copy.
