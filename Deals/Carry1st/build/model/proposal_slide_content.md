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

Paragraph under it: "Usage at the $5 median ticket is $0.020 per transaction in tranche 1 and $0.005 in tranche 4, where a fixed fee would stay at the same dollar amount whatever the ticket. The business case in this deck returns about $81.3K a month in savings and contribution at the run rate (base case), 3.9x this cost."

## Footer (small grey, bottom left)

"Platform fee billed annually. Usage billed monthly in arrears on successful transactions, net 30. Rates locked for the term, tranches reviewed annually as volume grows. All figures in USD."

## Build notes for the content agent (not on the slide)

- Three cards: left white with light border (about 28% of content width), middle light panel (about 30%), right solid Yuno blue with white text (about 32%), the same card language as German's previous three-card proposal slides.
- Only the quoted price appears. Apply the forbidden-word rule in CONTEXT.md to every figure on the slide. The platform fee is simply the platform fee, never phrased as a commitment threshold. Nothing beyond the quoted structure goes on the slide: no alternative block size, no term length, no launch-month variation.
- If the eight rows plus the add-ons box do not fit at body size, merge "Monitors & auto-failover" and "PCI token vault" into one row "Monitors, auto-failover & PCI token vault · Included". Never go below the body size used on the business-case slides.
- Numbers must match `bc_model.xlsx` Pricing sheet (average-ticket block) exactly: $7,500 / $13,500 / $21,000; 1.50% / 0.68% / 0.47%; $0.150 / $0.068 / $0.047; at 200K tranche 1 = $1.5M x 0.40% = $6,000; at 450K tranche 1 $1.5M x 0.40% = $6,000 + tranche 2 $2.5M x 0.30% = $7,500.
- "1,000+" is the y.uno figure for payment methods, PSPs and fraud solutions combined; do not split it into separate provider and method counts.
- No em dashes and no spaced hyphens as punctuation anywhere. Use "·", commas, colons.

## v3 deck (23 Oct 2026, pending Justo's OK): platform fee ramps with the launch

Applied on the copy "Carry1st + Yuno_Oct 2026v3 (ramp)", Slides id `1qmkK4eFBaq_Hsp_EA3r-QngFNJp3XIupHUrJt2gPfqo`, by `apply_ramp_v3.py`; only the proposal slide changes.
Trigger: Cordel, 20 Oct 2026: "fixed costs at launch may ultimately lead to a no-go".

- Title: "A platform fee that ramps up over the first three months, then a share of sales that falls as Carry1st grows."
- Sub-line: platform fee from $3,000 in month 1 to $7,500 from month 4, covering the first $500K of monthly sales, plus the share of sales above it ($21,000 a month at 450,000 transactions, 47 bps).
- Middle card: the big "$7,500 / month" figure is replaced by a four-column strip "RAMPS UP WITH THE LAUNCH": MONTH 1 $3,000 · MONTH 2 $4,000 · MONTH 3 $5,500 · MONTH 4+ $7,500, then "Then $7,500 a month from month 4, covering the first $500K of monthly sales. This is what covers the stack." The includes list moves down 14pt.
- Right card, first tile: $0.5M of monthly sales, you pay $3,000 in month 1, 60 bps of sales. Tiles at $2M and $4.5M unchanged. Callout: "The platform fee ramps with the launch, from $3,000 in month 1 to $7,500 from month 4. No fixed fee per transaction, and the rate falls as Carry1st grows."
- Footer: "Platform fee billed monthly." (monthly billing of the platform fee is a yellow-zone item in the pricing policy; Justo to confirm).
- Internal: year-1 platform fee $80,000 instead of $90,000, concession $10,000, cheaper than the v4 credit lever ($3,750 x 3 = $11,250). Bookable as $7,500 with launch credits of $4,500 / $3,500 / $2,000.
