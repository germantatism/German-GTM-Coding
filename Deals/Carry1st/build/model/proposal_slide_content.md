# Proposal slide · Carry1st + Yuno (customer-facing text, one slide, three-card format)

Eyebrow: **06 · Proposal**
Title (action title): **One platform fee that already covers the first $500K of monthly volume, then a share of volume that falls as Carry1st grows**
Sub-line (grey, one line): "A $7,500 monthly platform fee that covers the first $500K of monthly volume, plus a percentage of the volume above it: $21,000 a month at 450,000 transactions, 0.47% of TPV, $0.047 per transaction."

## Left card · TRANSACTION FEE

Sub-line (grey): "A percentage of the month's volume above the included block, pooled across Brazil, Argentina, Mexico, Bolivia and Colombia"

| Label | Range (monthly volume) | Rate |
|---|---|---|
| INCLUDED | First $500K of monthly volume | **$0** |
| TRANCHE 1 | $500K to $2M | **0.40%** |
| TRANCHE 2 | $2M to $5M | **0.30%** |
| TRANCHE 3 | $5M to $10M | **0.20%** |
| TRANCHE 4 | Above $10M | **0.10%** |

Note box (light grey): "No setup fee. No fixed amount per transaction. Volume means successful transactions only: declines and card verification attempts are not billed. Each tranche applies only to the volume inside it, so Carry1st's highest volume always pays the lowest rate. At a $10 ticket, 0.40% is $0.040 per transaction; at a $5 ticket, $0.020."

## Middle card · PLATFORM FEE

Big figure (Yuno blue): **$7,500** with "/ month" in grey.
Sub-line: "$90,000 / year. Covers the first $500K of monthly volume. This is what covers the stack."

**WHAT IT INCLUDES**

| Label | Value |
|---|---|
| Orchestration & rules engine | **Included** |
| Smart routing & retries | **Included** |
| Monitors & auto-failover | **Included** |
| Payment methods, PSPs and fraud solutions | **1,000+** |
| Checkout & SDKs (web, iOS, Android) | **Included** |
| PCI token vault | **Included** |
| Dashboard & insights | **Included** |
| Dedicated KAM and TAM | **Included** |

**ADD-ONS** box (white inner box; grey sub-line "Billed on usage, quoted separately, not in the totals on this slide."):

| Label | Value |
|---|---|
| Network tokens | On usage |
| 3DS authentication | On usage |

Last line (small grey): "Every integration maintained by Yuno. Adding dLocal, a local acquirer or a new local method later is a routing change, not a new project."

## Right card (blue) · WHAT IT MEANS FOR CARRY1ST

Sub-line: "At a $10 average ticket, across the five markets"

| LINE | 50,000 tx / month | 200,000 tx / month | 450,000 tx / month |
|---|---|---|---|
| Volume a month | $0.5M | $2.0M | $4.5M |
| Platform fee | $7,500 | $7,500 | $7,500 |
| Usage · tranche 1 | $0 | $6,000 | $6,000 |
| Usage · tranche 2 | $0 | $0 | $7,500 |
| **Total a month** | **$7,500** | **$13,500** | **$21,000** |
| Total a year | $90,000 | $162,000 | $252,000 |
| Share of volume | 1.50% | 0.68% | 0.47% |
| Per successful transaction | $0.150 | $0.068 | $0.047 |

Callout box (darker blue, bold white): "At launch Carry1st pays the platform fee and nothing per transaction. At the run rate the all-in cost is 0.47% of volume, falling as volume grows."

Paragraph under it: "Usage at the $5 median ticket is $0.020 per transaction in tranche 1 and $0.005 in tranche 4, where a fixed fee would stay at the same dollar amount whatever the ticket. The business case in this deck returns about $47.7K a month in savings and contribution at the run rate (base case), 2.3x this cost."

## Footer (small grey, bottom left)

"Platform fee billed annually. Usage billed monthly in arrears on successful transactions, net 30. Rates locked for the term, tranches reviewed annually as volume grows. All figures in USD."

## Build notes for the content agent (not on the slide)

- Three cards: left white with light border (about 28% of content width), middle light panel (about 30%), right solid Yuno blue with white text (about 32%), the same card language as German's previous three-card proposal slides.
- Only the quoted price appears. Apply the forbidden-word rule in CONTEXT.md to every figure on the slide. The platform fee is simply the platform fee, never phrased as a commitment threshold. Nothing beyond the quoted structure goes on the slide: no alternative block size, no term length, no launch-month variation.
- If the eight rows plus the add-ons box do not fit at body size, merge "Monitors & auto-failover" and "PCI token vault" into one row "Monitors, auto-failover & PCI token vault · Included". Never go below the body size used on the business-case slides.
- Numbers must match `bc_model.xlsx` Pricing sheet (average-ticket block) exactly: $7,500 / $13,500 / $21,000; 1.50% / 0.68% / 0.47%; $0.150 / $0.068 / $0.047; at 200K tranche 1 = $1.5M x 0.40% = $6,000; at 450K tranche 1 $1.5M x 0.40% = $6,000 + tranche 2 $2.5M x 0.30% = $7,500.
- "1,000+" is the y.uno figure for payment methods, PSPs and fraud solutions combined; do not split it into separate provider and method counts.
- No em dashes and no spaced hyphens as punctuation anywhere. Use "·", commas, colons.
