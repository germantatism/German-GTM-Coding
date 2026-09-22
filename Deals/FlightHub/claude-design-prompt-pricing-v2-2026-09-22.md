# Prompt Claude Design: FlightHub + Yuno, pricing slide v2 (2026-09-22)

Target: the deck **"Proposal - FlightHub + Yuno"** (21 slides, already open in the canvas). Edit **slide 16, "Proposal · Platform fee plus usage"** (section label "Business Case - Pricing") **in place**. Keep its layout, typography, card language and color system exactly as they are. Only the text and numbers listed below change. Do not touch any other slide.

## Why this changes

The proposal was reviewed in person with FlightHub on September 22. This version lowers the platform fee and the first tier, moves monitors and the token vault into the included list, prices network tokens, reconciliation and chargeback and fraud alerts as usage add-ons, and leaves only Nova AI pending. The slide keeps the same five blocks so the two versions compare side by side.

## 1. TRANSACTION FEE (top-left block)

Sub-line stays: "Charged only on transactions that get approved".

| Tier | Range | Fee |
|---|---|---|
| TIER 1 | 0 to 175,000 | **$0.055** (was $0.06) |
| TIER 2 | 175,001 to 350,000 | **$0.05** (unchanged) |
| TIER 3 | 350,001 and above | **$0.04** (unchanged) |

The note under the tiers stays exactly: "No setup fee. Declines cost nothing. Tier count and boundaries scale with FlightHub's volume, including seasonal peaks."

## 2. PLATFORM FEE

- Big figure: **$9,000/ month** (was $10,000/ month)
- Sub-line: "$108,000 / year. This is what covers the stack."

## 3. WHAT IT INCLUDES

Today this list has 7 rows. Replace it with these 9 rows, same row style (label in regular dark text, value in bold Yuno blue on the right):

| Label | Value |
|---|---|
| Dedicated KAM and TAM | **Included** |
| Payment methods | **+1,000** |
| Payment providers | **+450** |
| Anti-fraud tools | **+50** |
| Orchestration & rules engine | **Included** |
| Smart routing & retries | **Included** |
| Monitors & auto-failover | **Included** |
| PCI token vault | **Included** |
| Minimum monthly billing | **$25,000** |

Notes: the row that today reads "Orchestration, NT & rules engine" loses the "NT", because network tokens are now priced in the add-ons box. "Monitors & auto-failover" and "PCI token vault" are new rows. "Minimum monthly billing $25,000" stays as the last row.

Fit rule: if 9 rows do not fit at the current font size, merge two rows into "Smart routing, retries & monitors · Included" and keep "PCI token vault · Included" as its own row. Never go below the current body size.

## 4. PENDING REVIEW box becomes ADD-ONS

Today this box reads: "PENDING REVIEW · Nova AI, reconciliation, and monitors, are not in this rate. Scope and pricing to be reviewed together." followed by "Every integration maintained by Yuno. Adding a provider later is a routing change, not a new fee." If the canvas shows an older version of this box that also mentions "network tokens & vault", ignore it and build from the text below.

Replace the box content with:

**Box title** (same small caps bold style as "PENDING REVIEW" today): **ADD-ONS**

**Sub-line** next to the title (same grey regular style as today's sub-line): "Billed on usage, on top of the platform and transaction fees."

**Rows** (label in regular dark text, values in bold Yuno blue, same treatment as the values in WHAT IT INCLUDES):

| Label | Value |
|---|---|
| Network tokens | **$0.005** per token created · **$0.01** per token update |
| Reconciliation | **$1,500 / month** with 200,000 reconciled transactions included, then **$0.032** per additional transaction |
| Chargeback & fraud alerts | **$15** per matched alert, through Ethoca and Verifi. Unmatched alerts are not billed. |
| Nova AI | *Pending review* (grey italic, no number) · Scope and pricing to be reviewed together. |

Only the bolded parts are bold Yuno blue; the connecting words stay regular dark text.

**Last line of the box** (keep it, same style as today): "Every integration maintained by Yuno. Adding a provider later is a routing change, not a new fee."

**Fit rules for this box:**
- The box keeps its current position, width and height, aligned with the blocks around it as today.
- Title and sub-line share the first line. The four rows go underneath, one row per line, at the same font size as the body text of WHAT IT INCLUDES. Never go below that size.
- If a row does not fit on one line, use these shorter wordings instead of wrapping or shrinking: "Network tokens · **$0.005** per token, **$0.01** per update" and "Reconciliation · **$1,500 / month** incl. 200,000 reconciled trx, then **$0.032** each" and "Chargeback & fraud alerts · **$15** per matched alert" and "Nova AI · *Pending review*".
- If it still does not fit, drop the sub-line first, then the "Every integration maintained by Yuno" sentence. Never drop a priced row.
- Nothing overlaps and nothing touches the box border. Keep the same inner padding as today.

## 5. WHAT IT MEANS FOR FLIGHTHUB

Header stays: "At 602,000 successful transactions / month". Column headers stay: LINE · MONTHLY · YEARLY. Replace the rows with exactly these numbers:

| LINE | MONTHLY | YEARLY |
|---|---|---|
| Tier 1 · 175,000 at $0.055 | $9,625 | $115,500 |
| Tier 2 · 175,000 at $0.05 | $8,750 | $105,000 |
| Tier 3 · 252,000 at $0.04 | $10,080 | $120,960 |
| Platform fee | $9,000 | $108,000 |
| **Total** | **$37,455** | **$449,460** |

Line under the table: "$0.062 all-in per successful transaction, falling as volume grows."

Paragraph under it, exactly: "602,000 successful is 700,000 attempts at the 86% baseline. At 430,000 (low season): $30,575 /mo · $366,900 /yr ≈ $0.071. At 688,000 (peak): $40,895 /mo · $490,740 /yr ≈ $0.059. The $25,000 minimum applies below 302,500 successful transactions. Add-ons are billed on usage and are not in these totals."

## 6. Footer

Stays exactly: "3 year term, rates locked, tiers reviewed annually as volume grows"

## Everything else on the slide stays identical

Slide title, section label, block titles, positions, colors and the Yuno wordmark. Do not move, restyle or renumber anything. Slides 1 to 15 and 17 to 21 stay untouched.

## What NOT to do

- Do not change the tier boundaries, the $25,000 minimum, the 3 year term or the slide title.
- Do not put a price on the token vault or on monitors. Both are "Included", with no number, no asterisk and no condition.
- Do not estimate token counts or reconciled volumes, and do not add network token or reconciliation amounts into the WHAT IT MEANS table or its totals.
- Do not add words like "from", "starting at", "up to", "list price", "minimum" or "discount" next to any price.
- Do not leave the word "Pending" anywhere on the slide except the Nova AI row.
- Do not mention Visa, Mastercard, TRID, token requestor, ConnexPay or any payment provider by name in the add-ons box. Ethoca and Verifi are the only names allowed, in the alerts row.
- Do not add a monthly fee, a minimum, a volume range or a second price to the alerts row. One price per matched alert, nothing for unmatched alerts.
- Do not add claims about approval rates, savings, uptime or comparisons with other vendors.
- Do not change, round or reformat any number given above.
- Do not use em-dashes or " - " as punctuation anywhere in the copy. Use "·" or commas.
