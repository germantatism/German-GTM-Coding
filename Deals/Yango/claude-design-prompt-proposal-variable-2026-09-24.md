# Prompt Claude Design: Yango + Yuno, rebuild the "06 · Proposal" slides on a variable rate (2026-09-24)

Target: the deck **"Business Case Yango + Yuno"** (39 slides, open in the canvas). Section **06 · Proposal** already exists: slide 35 is the divider, slide 36 the pricing slide, slide 37 the country view, and the agenda on slide 2 already lists "06. PROPOSAL". Keep slide 35 and the agenda exactly as they are. **Rebuild the content of slides 36 and 37** with the model below, keeping the deck's visual system exactly: Titillium Web, Yuno blue #3E4FE0, the light panels and the solid blue panel used on slides 15, 16, 31 and 32, eyebrow / title / footer structure, page number bottom left, Yuno wordmark top right. Do not redesign anything and do not touch any other slide except the two cleanups at the end.

## Why the model changes

Yango asked for a variable rate. On the August 19 call, Alejandro Sanabria said their average recharge ticket is low ($1.50 to $3.50) so any fixed amount per transaction hurts them, and that for a global agreement they strongly prefer variable-only pricing. The current slide 36 charges dollars per recharge and adds a monthly minimum, which is the opposite of what they asked. The new proposal charges a percentage of approved recharge volume, has no fixed fee per transaction and no monthly minimum, and keeps a single platform fee. Volumes are the same ones the business case already uses (slide 31, Yango's own data, monthly = annual / 12): $7,305,025 in approved recharges and 3,241,304 transactions a month across the four markets, blended ticket $2.25.

## Slide 36: the pricing slide

Eyebrow: **Proposal**
Title, Yuno blue, same size as slide 31: **Proposal · Platform fee plus a variable rate on approved recharges**
Sub-line under the title (grey, one line): "One flat platform fee plus a percentage of approved recharge volume that drops as the four markets pool: $47,873 a month at full volume, 0.66% of volume, $0.015 per recharge."

Three cards with the same card language as slides 31 and 32: left card white with a light border, middle card light lavender, right card solid Yuno blue with white text (left ≈ 28%, middle ≈ 30%, right ≈ 32% of the content width).

### Left card · TRANSACTION FEE

Sub-line (grey): "A percentage of the month's approved recharge volume, pooled across Colombia, Peru, Bolivia and Venezuela"

Three rows, small bold label on top, range under it, rate big and bold on the right:

| Label | Range | Rate |
|---|---|---|
| TRANCHE 1 | $0 to $2.5M a month | **0.60%** |
| TRANCHE 2 | $2.5M to $5M | **0.50%** |
| TRANCHE 3 | Above $5M | **0.45%** |

Note box at the bottom of the card (light grey box, regular text): "No setup fee. No fixed fee per transaction. No monthly minimum. Declines and card verification attempts cost nothing. Each tranche applies only to the volume inside it, so Yango's highest volume always pays the lowest rate."

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

**ADD-ONS** box (white inner box, small caps bold title, grey sub-line "Billed on usage, on top of the fees above."):

| Label | Value |
|---|---|
| Network tokens | **$0.05** per token created, **$0.01** per update |
| Reconciliation | *Pending review* (grey italic, no number) |

Last line of the card, small grey: "Every integration maintained by Yuno. Adding a provider or a local rail later is a routing change, not a new fee."

Fit rule: if the nine rows plus the add-ons box do not fit at the body size, merge "Monitors & auto-failover" and "PCI token vault" into one row "Monitors, auto-failover & PCI token vault · Included". Never go below the body size used on slide 31.

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

Footer (small grey, bottom left next to the page number): "3 year term, rates locked, tranches reviewed annually as volume grows. All figures in USD."

## Slide 37: country by country, as each market goes live

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

Source line (small grey, bottom): "Source: Yango's own recharge data, shared August 2026, monthly. Declines and card verification attempts are not billed. Add-ons billed on usage and not included."

## Two cleanups on existing slides

1. Slides 34, 36 and 37 each contain a stray small text box that reads "$ 75.56". Delete all three.
2. Slide 31, source line: change "Source: Yango's own recharge data, July 2026." to "Source: Yango's own recharge data for July 2026, shared August 2026." Change nothing else on that slide.

## What NOT to do

- Do not add a monthly minimum, a volume commitment, a first-month-free line or any fixed amount per transaction anywhere. Those were removed on purpose.
- Do not change, round or reformat any number above. Do not add a per-country allocation of the full-volume cost on slide 36; the country view lives on slide 37 only, and it shows what each market adds, not a split of the total.
- Do not put a price on reconciliation. It is "Pending review", no number, no asterisk.
- Do not add words like "from", "starting at", "up to", "list price", "minimum" or "discount" next to any price.
- Do not name Unlimit, Inswitch, PayU, Cobre or any provider on these slides, and do not add approval-rate, savings or uptime claims beyond the two figures quoted from this deck ($3.21M and $0.88M).
- Do not use em-dashes or " - " as punctuation anywhere. Use "·" or commas.
- Slides 1 to 35 (other than the two cleanups), 38 and 39 stay identical.
