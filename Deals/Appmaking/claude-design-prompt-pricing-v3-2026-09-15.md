# Prompt Claude Design: AppMaking + Yuno, update the pricing slide to pricing v3 (2026-09-15)

Target: the deck **"Proposal - AppMaking + Yuno"** (18 slides, already open in the canvas). Edit **slide 13, "Proposal · Platform fee plus usage"** in place. Keep its layout, typography, card language and color system exactly as they are; only the content described below changes. Also make one small fix on slide 11. Do not touch any other slide.

## Why this changes

After the September 15 call with Tatsiana: they own their MIDs, they want Yuno fully separate from Solidgate, their ramp stays 20K to 150K by month 7 (they may extend to 200K later), and they asked to see how the price works at 20,000 and at 50,000 transactions. Pricing moves up one step: the first band now lands at $12,000 all-in and fully ramped at $17,500. The subscriptions engine is now priced at Yuno's standard instead of "Pending", and monitors are included.

## Slide 13 content

**TRANSACTION FEE block.** Keep the header "Charged only on transactions that get approved". Replace the tier rows with exactly these five, same row style as today (band label, range, platform fee, per transaction, all-in at the top of the band):

| Band | Successful transactions / month | Platform fee | Per successful transaction | All-in at top of band |
|---|---|---|---|---|
| Band 1 | 0 to 25,000 | $6,000 | $0.24 | $12,000 |
| Band 2 | 25,001 to 50,000 | $6,500 | $0.15 | $14,000 |
| Band 3 | 50,001 to 100,000 | $7,500 | $0.09 | $16,500 |
| Band 4 | 100,001 to 150,000 | $8,500 | $0.06 | $17,500 |
| Fully ramped | Above 150,000 | $8,500 | $0.05 | $18,500 at 200,000 · $21,000 at 250,000 |

Give the "Fully ramped" row the highlighted treatment used for the top tier today. Footnote under the table, small grey: "The band is set by the month's successful transactions and applies to the whole month. Declines cost nothing. No setup fee. Every step lowers the cost per transaction."

**PLATFORM FEE card** becomes **"Fully ramped: $17,500 / month"** with the sub-line "$210,000 / year at 150,000 successful transactions. This is what covers the stack."

**WHAT IT INCLUDES** (same row style, label left, value right in Yuno blue):
- Dedicated account management team (KAM and TAM) · Included
- Payment methods · +1,000
- Payment providers · +450
- Anti-fraud tools · +50
- Orchestration & rules engine · Included
- Smart routing & retries · Included
- Monitors & alerts · Included
- Sub-line in grey: "Every connector maintained by Yuno. Adding a provider later is a routing change, not a new fee."

**SUBSCRIPTIONS ENGINE** (new priced row, placed between "What it includes" and "Pending review", same row style, value in Yuno blue): "Subscriptions engine (standalone) · First $50,000 processed free, then $0.05 per transaction through the engine."

**PENDING REVIEW** (values in grey italic "Pending"):
- Reconciliation · Pending
- Token vault & network tokens · Pending
- Verifi & Ethoca alerts · Pending
- Sub-line: "Scope and pricing to be reviewed together once the phase 1 providers are set."

**WHAT IT MEANS FOR APPMAKING.** Sub-line: "On the ramp you shared on September 8". Replace the current lines with exactly these:
- Month 1 at 20,000: $10,800 ($0.54 per transaction)
- At 50,000: $14,000 ($0.28)
- Month 7 at 150,000: $17,500 ($0.117)
- Months 1 to 7: $97,200 for 520,000 successful transactions ($0.187)
- Year 1: $184,700 for about 1.27M successful transactions ($0.145)
- One grey line under the block: "Cost per transaction falls every month on your curve: $0.54, $0.37, $0.29, $0.21, $0.17, $0.13, $0.12."

If the slide has an "Expected" column or month labels next to the bands, set them to: Band 1 · Month 1; Band 2 · Months 2 to 3; Band 3 · Months 4 to 5; Band 4 · Months 6 to 7; Fully ramped · Month 8 onward.

If the slide still carries a "Minimum monthly billing" line or a contract term line, remove them. Neither has been agreed.

## Slide 11 fix

Remove the two bullets inherited from the FlightHub deck: "Your routing platform stays, Yuno extends it" and "Network tokens across all seven providers". Do not add replacements.

## What NOT to do

- Do not keep any of the previous numbers ($5,000 + $0.20, $5,500 + $0.12, $6,500 + $0.065, $7,500 + $0.05, $15,000 fully ramped, $155,575 year 1). All are replaced.
- Do not add a first-month-free line, a volume commitment, a 250K scenario as a condition, or a contract term. Those are conversation levers, not slide content.
- Do not invent prices for reconciliation, token vault, network tokens, Verifi or Ethoca. They stay "Pending" with no number.
- Do not name Solidgate or any PSP on this slide.
- Do not add claims about Appmaking's approval rates, savings or comparisons with other pricing structures.
- Do not change, round or reformat the numbers above.
- Do not use em-dashes anywhere in the copy.
