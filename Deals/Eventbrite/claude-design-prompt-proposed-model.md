# Prompt Claude Design: slide "THE PROPOSED MODEL" para Eventbrite (2026-08-17)

---

You are fixing ONE existing slide in the Eventbrite deck, the one labeled "THE PROPOSED MODEL" (currently showing placeholder content built for Suno: title "Stripe alone leaks revenue at four points, and a second PSP only fixes one", body text about Suno's subscribers and Series D). Replace ALL of its text content with the Eventbrite content below. Do not touch any other slide.

## DESIGN RULES (ABSOLUTE)

1. Visually identical to the current slide: same slide master, fonts, colors, header style (grey caps section label top-left, yuno logo top-right), same big blue title style, same footer/page number.
2. Same comparison-table layout: 4-column table (row-label column + TODAY + OPTION A + OPTION B), header row with the rightmost "OPTION B" column highlighted in dark blue, red X / orange tilde / green check icons per cell, same divider lines between rows, same bottom full-width dark-blue takeaway bar, same small grey source line under the bar.
3. No new colors, icons or fonts. US English. No em-dashes. No " - " as punctuation. No dollar figures or numeric estimates anywhere on this slide, this version is about the model, not the business case.

## SLIDE CONTENT

Section label (top-left, grey caps): "THE PROPOSED MODEL"

Title: "Six rails already exist. A pay-in-only orchestrator still leaves payouts exactly where they are."

Subtitle (regular text under title): "Eventbrite already runs six rails in parallel. What's missing isn't another processor, it's orchestration that spans pay-in and payout together."

### TABLE HEADER ROW

- Left header: "FOUR PAYMENT-FRICTION GAPS" / sub: "Where the current setup breaks"
- Column 1 header: "TODAY" / sub: "Six rails, self-built"
- Column 2 header: "OPTION A" / sub: "+ a pay-in orchestrator"
- Column 3 header (highlighted dark blue): "OPTION B" / sub: "+ Yuno orchestration"

### ROW 1

Row label: "Local methods missing"
Row sub-label (small grey): "Pix, Boleto, OXXO, SEPA Direct Debit, Bizum, Klarna"

- TODAY (red X): "Limited to what each of the six rails supports natively. A new market means a new integration."
- OPTION A (orange tilde): "Adds method coverage, but only on the pay-in side. Payout for those methods still runs separately."
- OPTION B (green check): "Full local method depth per market, pay-in and payout together, through one API."

### ROW 2

Row label: "Six rails, no routing or failover"
Row sub-label: "Stripe, Braintree, J.P. Morgan, Adyen, Wells Fargo, Mercado Pago run in parallel"

- TODAY (red X): "Self-built failover only. No BIN-based routing, no least-cost debit routing, no smart retries."
- OPTION A (orange tilde): "Adds routing and failover across the rails it connects to. Payout stays a separate system."
- OPTION B (green check): "Smart routing, cascading failover and retries across all six rails, one control plane."

### ROW 3

Row label: "Pay-in and payout, never tied together"
Row sub-label: "Collusion fraud tracing, LatAm entity payouts, 12,000+ creators"

- TODAY (red X): "No system links pay-in data to payout data. Collusion gets caught manually, after the fact."
- OPTION A (red X): "Solves pay-in routing at best. Payout stays exactly where it is today."
- OPTION B (green check): "One ledger ties every pay-in to its payout, across every rail, including the LatAm entities being exited."

### ROW 4

Row label: "LatAm entities, one more portal"
Row sub-label: "Brazil, Argentina, Mexico, Colombia via EBANX/Braintree"

- TODAY (red X): "EBANX reachable only through Braintree, no unified reporting, its own portal to manage."
- OPTION A (red X): "Adds another integration, and likely another portal. No path out of the funds flow."
- OPTION B (green check): "One dashboard across every rail and every MoR partner, with a path to exit the LatAm entities."

### BOTTOM TAKEAWAY BAR (full-width, dark blue)

"Option A adds a second integration and narrows the pay-in gaps. Option B adds one integration and closes all four, pay-in and payout together, while keeping every rail Eventbrite runs today live."

### FOOTNOTE (small grey)

"Source: Eventbrite call, August 4, 2026 (Paul Pasion); Eventbrite FY2025 10-K, filed 2026-03-12 (SEC)."

## WHAT NOT TO DO

- Do not modify any other slide in the deck.
- Do not invent additional figures or dollar estimates; use only the content above.
- Do not soften row 3's Option A cell into a partial fix (no orange tilde there), it must read as a red X: a pay-in-only orchestrator does not touch this gap at all, that is the whole point of the row.
