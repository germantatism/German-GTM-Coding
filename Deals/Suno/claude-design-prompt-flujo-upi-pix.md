# Prompt Claude Design: slide de flujos UPI/Pix (Stripe vs Yuno) (2026-08-06)

---

You are adding ONE new slide to the existing Google Slides deck "Business Case - Suno + Yuno". This slide goes in the section THE PROPOSED MODEL, immediately after the architecture slide ("Keep Stripe direct. Add the orchestration layer alongside it.").

## DESIGN RULES (ABSOLUTE)

1. The slide must be visually indistinguishable from the rest of the deck: same slide master, same fonts, same color palette, same header style (section label top-left in grey caps, yuno logo top-right), same title style (large blue title), same footer and page number style, same box/card style and same arrow style already used in the architecture slide and the decision-frame slide.
2. Reuse the exact box components the deck already uses (same corner radius, same fill colors, same stroke). Do not introduce any new color, gradient, icon set, or font.
3. US English. No em-dashes. No " - " as punctuation.

## SLIDE CONTENT

Section label (top-left, grey caps): "THE PROPOSED MODEL"

Title (deck's blue title style): "The same local rails, with fewer hops in between"

Subtitle (one line, small): "Every intermediary in the chain stacks fees and hides decline data. Orchestration connects to the local rail at the shortest path."

Layout: two horizontal comparison panels stacked vertically, each panel split in two rows (TODAY vs WITH YUNO). All flow boxes are the same size; arrows between boxes use the deck's arrow style.

### PANEL 1: UPI (India)
Panel label: "UPI · India"
Row 1, labeled "TODAY VIA STRIPE" (4 hops):
[Suno] → [Stripe] → [EBANX] → [Razorpay] → [UPI]
Small caption under the row: "Four hops between Suno and the rail"
Row 2, labeled "WITH YUNO" (2 hops):
[Suno] → [Yuno] → [Razorpay] → [UPI]
Small caption under the row: "Direct connection to Razorpay"

### PANEL 2: PIX (Brazil)
Panel label: "Pix · Brazil"
Row 1, labeled "TODAY VIA STRIPE" (3 hops):
[Suno] → [Stripe] → [EBANX] → [Pix]
Small caption under the row: "Three hops between Suno and the rail"
Row 2, labeled "WITH YUNO" (direct):
[Suno] → [Yuno] → [Pix]
Small caption under the row: "Direct connection to Pix"

Visual treatment: in each panel, the TODAY row uses the deck's neutral/grey card fill; the WITH YUNO row uses the deck's highlight fill (the same one used for the Option B column in the decision-frame slide). The intermediary boxes that disappear in the Yuno row (EBANX in panel 1 seen as extra, Stripe in both) should NOT be crossed out or styled differently; the contrast comes only from the shorter chain.

Bottom takeaway bar (same style as the decision-frame slide's bottom bar): "Fewer intermediaries per transaction: lower stacked fees, full decline visibility, and direct commercial terms with each local provider."

Footnote (small, grey): "Illustrative provider chains for local rail connectivity; exact routing varies by market and configuration."

## WHAT NOT TO DO
- Do not add cost percentages or fee numbers to the arrows (no verified figures for the hops).
- Do not modify any other slide.
- Do not use red X marks or green checks on this slide; the architecture comparison stays neutral and factual.
