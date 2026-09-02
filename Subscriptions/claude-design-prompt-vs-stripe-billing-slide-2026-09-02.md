# Prompt for Claude Design: "Yuno Subscriptions vs Stripe Billing" comparison slide (2026-09-02)

Paste this into the **Yuno Design System** Claude Design project (the one with `CLAUDE.md`, `tokens.json`, `colors_and_type.css` and `slides/` already uploaded). This is a new, standalone slide, not an edit to an existing deck.

## What to build

One slide using the **Table template** (`slides/TableSlide.html`) — read that file first, don't invent new chrome. Register it as `asset: "Slide — Subscriptions vs Stripe Billing"`.

- **Eyebrow:** Subscriptions
- **Headline:** Recurring billing without the single-processor lock-in
- **Table super-header** (spans all 3 columns): Yuno Subscriptions vs. Stripe Billing — Sept 2026
- **Column headers:** Capability | Yuno Subscriptions | Stripe Billing

## Rows (exact content, don't add or invent rows beyond these four)

1. **Processor architecture**
   - Yuno Subscriptions: Multi-PSP orchestration — Stripe, Adyen, Braintree and more, all under one subscriptions engine. Adding a processor is one connection, zero extra integration work.
   - Stripe Billing: Wired to Stripe only. Adding another processor means the merchant builds and maintains that integration themselves, outside Billing.

2. **Subscription + first payment**
   - Yuno Subscriptions: One call creates the charge and the subscription together. If the payment fails, no subscription is created.
   - Stripe Billing: Subscription starts as `incomplete`; the customer has 23 hours to pay before it expires (`incomplete_expired`).

3. **Local recurring rails**
   - Yuno Subscriptions: Native Pix Automático support in Brazil — D-4 scheduling and a rail-specific 3-attempt retry ladder built into the engine.
   - Stripe Billing: Recurring retry coverage limited to ACH, ACSS, BECS (AU/NZ), BACS and SEPA — no Pix, no LatAm APMs.

4. **Integration surface**
   - Yuno Subscriptions: 8 subscription statuses, one object to track.
   - Stripe Billing: Status is spread across three linked objects — Subscription, Invoice and PaymentIntent — each with its own state.

## Footer

- **Notes (left):** Source: Yuno product documentation (docs.y.uno/docs/payment-features/subscriptions) and Stripe Billing documentation (docs.stripe.com/billing), reviewed Sept 2026.
- Drop the `summary-label` / `summary-value` pair from the template (there's no single stat to headline here) — let the notes column take the full footer width instead.

## Design-system compliance

- Follow `CLAUDE.md` exactly: Geist only, monochromatic indigo + neutral palette (no green/red for "win/lose" framing — don't add checkmarks or colored good/bad indicators, keep it a plain factual table), lowercase `yuno` wordmark from `assets/logo/`, no emoji, 8-pt grid.
- This is a comparison, not a scorecard — no ✓/✗ icons, no highlight color to declare a "winner" per row. Let the copy itself carry the contrast. You may use `.hl` (the existing highlight span class already in `TableSlide.html`) sparingly on the Yuno column's key phrases (e.g. "one connection, zero extra integration work") if it reads clean, but don't overuse it.
- Canvas 1920×1080, same edge rule + purple tick treatment as every other template.
