# Prompt Claude Design: Yango + Yuno, add the "Proposal" section (2026-09-22)

Target: the deck **"Business Case Yango + Yuno"** (36 slides, already open in the canvas). Add a new section **06 · Proposal** made of three slides, inserted **after slide 34 ("LATAM - Development costs savings") and before slide 35 ("Powering the future of financial infrastructure")**, and add the section to the agenda on slide 2. Match the deck's existing visual system exactly: Titillium Web, Yuno blue #3E4FE0, the light panels and the solid blue panel already used on slides 15, 16, 31 and 32, the eyebrow / title / footer structure, the small page number bottom left and the Yuno wordmark top right. Do not redesign anything and do not touch any other slide.

## Why this changes

Javier Patiño reviewed the business case and could not find how much Yuno would cost. This section answers that with one pricing model across Colombia, Peru, Bolivia and Venezuela, built on the same volumes the business case already uses (slide 31, Yango's own August 2026 data, monthly = annual / 12). Yango asked for a variable rate, not a fixed fee per transaction, because their average recharge ticket is $2.25, so the transaction fee is a percentage of approved recharge volume.

## 1. Slide 2, "Agenda": add one line

Under "05. BUSINESS CASE" add, in the same style and spacing: **06.** and **PROPOSAL**.

## 2. New slide 35: section divider

Duplicate slide 29 (the "05 · Business Case" divider) and change only the text: **06** and **Proposal**. Same gradient, same rule, same wordmark.

## 3. New slide 36: the pricing slide

Eyebrow: **Proposal** (same light grey eyebrow as "Business Case" on slide 31).
Title, Yuno blue, same size as slide 31: **Proposal · Platform fee plus a variable rate on approved recharges**

Three columns with the same card language as slides 31 and 32: left card white with a light border, middle card light lavender, right card solid Yuno blue with white text. Same proportions as a three column proposal slide (left ≈ 28%, middle ≈ 30%, right ≈ 32% of the content width).

### Left card · TRANSACTION FEE

Sub-line (grey): "A percentage of the month's approved recharge volume, across Colombia, Peru, Bolivia and Venezuela"

Three rows, small bold label on top, range under it, rate big and bold on the right:

| Label | Range | Rate |
|---|---|---|
| TRANCHE 1 | $0 to $2.5M a month | **0.60%** |
| TRANCHE 2 | $2.5M to $5M | **0.50%** |
| TRANCHE 3 | Above $5M | **0.45%** |

Note box at the bottom of the card (light grey box, regular text): "No setup fee. No fixed fee per transaction. Declines and card verification attempts cost nothing. Each tranche applies only to the volume inside it, so Yango's highest volume always pays the lowest rate."

### Middle card · PLATFORM FEE

Big figure in Yuno blue: **$10,000** with "/ month" in grey next to it.
Sub-line: "$120,000 / year. This is what covers the stack."

**WHAT IT INCLUDES** (label left in dark regular, value right in bold):

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
| Reporting & dashboard | **Included** |

**ADD-ONS** box (white inner box, small caps bold title, grey sub-line "Billed on usage, on top of the fees above."), three rows, values in bold Yuno blue:

| Label | Value |
|---|---|
| Network tokens | **$0.05** per token created, **$0.01** per update |
| Reconciliation | *Pending review* (grey italic) |
| Nova recovery for failed top-ups | *Pending review* (grey italic) |

Last line of the card, small grey: "Every integration maintained by Yuno. Adding a provider or a local rail later is a routing change, not a new fee."

Fit rule: if the nine included rows plus the add-ons box do not fit at the body size, merge "Monitors & auto-failover" and "PCI token vault" into one row "Monitors, auto-failover & PCI token vault · Included". Never go below the body size used on slide 31.

### Right card (blue) · WHAT IT MEANS FOR YANGO

Sub-line: "At $7.3M in approved recharges a month across the four markets (3.24M transactions, Yango's own August 2026 data)"

Column headers: LINE · MONTHLY · YEARLY

| LINE | MONTHLY | YEARLY |
|---|---|---|
| Tranche 1 · $2.5M at 0.60% | $15,000 | $180,000 |
| Tranche 2 · $2.5M at 0.50% | $12,500 | $150,000 |
| Tranche 3 · $2.3M at 0.45% | $10,373 | $124,471 |
| Platform fee | $10,000 | $120,000 |
| **Total** | **$47,873** | **$574,471** |

Callout box inside the blue card (slightly darker blue, bold white): "$0.015 all-in per approved recharge, 0.66% of recharge volume, falling as volume grows."

Paragraph under it, exactly: "Colombia and Peru first: $31,128 a month on $3.7M in recharges. All four markets: $47,873. The card-rail case in this deck, $3.21M a year, is 5.6 times this cost, and the $0.88M estimated on processing cost alone exceeds it. Add-ons are billed on usage and are not in these totals."

### Footer (small grey, bottom left next to the page number)

"3 year term, rates locked, tranches reviewed annually as volume grows. All figures in USD."

## 4. New slide 37: country by country

Eyebrow: **Proposal**
Title, Yuno blue: **Country by country: what each market adds as it goes live**

Intro band (the light grey box used under the title on slide 31): "The tranches pool the four markets, so each new market lands on a lower rate. Sequence shown as Yango proposed it: Colombia and Peru first, then Bolivia and Venezuela. Any order works, and the total at full volume does not change."

Four country cards, same style as the four cards on slide 31 (flag + country name, blue underline, small caps labels, big figures), one per column, in this order:

| | Colombia | Peru | Bolivia | Venezuela |
|---|---|---|---|---|
| Step label (small, blue) | STEP 1 · GOES LIVE FIRST | STEP 2 | STEP 3 | STEP 4 |
| APPROVED RECHARGES / MONTH | $1.93M | $1.80M | $2.75M | $0.83M |
| TRANSACTIONS / MONTH | 551K | 561K | 1.83M | 297K |
| AVG RECHARGE TICKET | $3.50 | $3.20 | $1.50 | $2.80 |
| ADDED MONTHLY COST (big figure) | $21,578 | +$9,551 | +$13,000 | +$3,744 |
| Small line under it | $11,578 transaction fee at 0.60% plus the $10,000 platform fee | Part at 0.60%, the rest at 0.50% | Part at 0.50%, the rest at 0.45% | All of it at 0.45% |
| RUNNING TOTAL | $21,578 / month · $0.039 per recharge | $31,128 / month · $0.028 per recharge | $44,129 / month · $0.015 per recharge | $47,873 / month · $0.015 per recharge |

Blue band under the cards (same as "FOUR MARKETS, COMBINED" on slide 31), four stats:
**FOUR MARKETS, COMBINED** · **$47,873** a month · **$574,471** a year · **$0.015** per approved recharge · **0.66%** of recharge volume

Source line (small grey, bottom): "Source: Yango's own recharge data, August 2026, monthly. Declines and card verification attempts are not billed. Add-ons billed on usage and not included."

## Everything else stays identical

Slides 1 to 34 (other than the agenda line on slide 2) and the two closing slides do not change. Page numbers of the closing slides shift to 38 and 39.

## What NOT to do

- Do not change, round or reformat any number above. Do not add a per-country allocation of the full-volume cost on slide 36 (the country view lives on slide 37 only).
- Do not put a price on reconciliation or Nova. They are "Pending review", no number, no asterisk.
- Do not add words like "from", "starting at", "up to", "list price", "minimum" or "discount" next to any price.
- Do not name Unlimit, Inswitch, PayU, Cobre or any provider on these slides, and do not add approval-rate, savings or uptime claims beyond the two figures quoted from this deck ($3.21M and $0.88M).
- Do not add a monthly minimum, a volume commitment or a first-month-free line. Those are conversation levers, not slide content.
- Do not use em-dashes or " - " as punctuation anywhere. Use "·" or commas.
