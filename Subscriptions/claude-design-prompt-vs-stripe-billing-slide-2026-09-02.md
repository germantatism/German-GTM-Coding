# Prompt for Claude Design: "Yuno Subscriptions vs Stripe Billing" comparison slide (2026-09-02, v2 — adds pricing)

Paste this into the **Yuno Design System** Claude Design project (the one with `CLAUDE.md`, `tokens.json`, `colors_and_type.css` and `slides/` already uploaded). This is a new, standalone slide, not an edit to an existing deck. If you already generated a v1 of this slide, edit that file in place rather than forking a new one.

## What to build

One slide using the **Table template** (`slides/TableSlide.html`) — read that file first, don't invent new chrome. Register it as `asset: "Slide — Subscriptions vs Stripe Billing"`.

- **Eyebrow:** Subscriptions
- **Headline:** Recurring billing without the single-processor lock-in
- **Table super-header** (spans all 3 columns): Yuno Subscriptions vs. Stripe Billing — Sept 2026
- **Column headers:** Capability | Yuno Subscriptions | Stripe Billing

## Rows (exact content, don't add or invent rows beyond these five)

1. **Processor architecture**
   - Yuno Subscriptions: Multi-PSP orchestration — Stripe, Adyen, Braintree and more, all under one subscriptions engine. Adding a processor is one connection, zero extra integration work.
   - Stripe Billing: Wired to Stripe only. Adding another processor means the merchant builds and maintains that integration themselves, outside Billing.

2. **Per-transaction fee**
   - Yuno Subscriptions: First $50,000 in monthly processing free, then $0.05 per transaction — on top of payment processing.
   - Stripe Billing: $0.07 per transaction, on top of payment processing.

3. **Subscription + first payment**
   - Yuno Subscriptions: One call creates the charge and the subscription together. If the payment fails, no subscription is created.
   - Stripe Billing: Subscription starts as `incomplete`; the customer has 23 hours to pay before it expires (`incomplete_expired`).

4. **Local recurring rails**
   - Yuno Subscriptions: Native Pix Automático support in Brazil — D-4 scheduling and a rail-specific 3-attempt retry ladder built into the engine.
   - Stripe Billing: Recurring retry coverage limited to ACH, ACSS, BECS (AU/NZ), BACS and SEPA — no Pix, no LatAm APMs.

5. **Integration surface**
   - Yuno Subscriptions: 8 subscription statuses, one object to track.
   - Stripe Billing: Status is spread across three linked objects — Subscription, Invoice and PaymentIntent — each with its own state.

## Footer

- **Notes (left):** Source: Yuno pricing and product documentation (docs.y.uno/docs/payment-features/subscriptions); Stripe Billing documentation (docs.stripe.com/billing), reviewed Sept 2026.
- **summary-label:** Per-transaction fee
- **summary-value:** $0.05 vs $0.07
- Five rows is more than the four-row pricing-table example in `TableSlide.html` — if body cell padding makes the table run long, tighten `tbody td` padding slightly (e.g. 32px → 24px vertical) rather than shrinking the headline or footer. Keep everything else on the established grid.

## Design-system compliance

- Follow `CLAUDE.md` exactly: Geist only, monochromatic indigo + neutral palette (no green/red for "win/lose" framing — don't add checkmarks or colored good/bad indicators, keep it a plain factual table), lowercase `yuno` wordmark from `assets/logo/`, no emoji, 8-pt grid.
- This is a comparison, not a scorecard — no ✓/✗ icons, no highlight color to declare a "winner" per row. Let the copy itself carry the contrast. You may use `.hl` (the existing highlight span class already in `TableSlide.html`) sparingly on the Yuno column's key phrases (e.g. "$0.05 per transaction", "one connection, zero extra integration work") if it reads clean, but don't overuse it.
- Canvas 1920×1080, same edge rule + purple tick treatment as every other template.
