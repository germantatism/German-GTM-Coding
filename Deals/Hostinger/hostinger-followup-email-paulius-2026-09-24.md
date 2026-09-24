# Follow-up email to Paulius after the Sep 24, 2026 demo

**Status:** Gmail draft created Sep 24, 2026 as a reply in the thread "Hostinger + Yuno | Demo" (to Paulius; cc Antoine, Dirk, Justo, Piotr, TJ, Ivvy). Review and send.
**Division of labour agreed in the Slack group "Hostinger" (Sep 24):** German sends the summary and next steps; TJ sends the India migration follow-up separately; Dirk sends the token migration overview.

---

Subject: Re: Hostinger + Yuno | Demo

Hi Paulius,

Thank you for this morning. A short recap and the next steps we committed to.

What we took from the session

- India first: Razorpay and BillDesk under one integration, with routing and token storage that meet local requirements. Vaulting as a service runs as a separate track.
- Token migration is the question to answer with precision: a couple of million tokens, network tokens under your own name, scheme transaction IDs preserved, no drop in authorization rates.
- Your billing engine stays in house. What you want from us is execution of each charge, fallback across providers and retry timing inside your dunning window, not a new plan catalog.

Next steps on our side

1. India: TJ, Antoine and our India team are working through what is possible under RBI rules for card tokens and UPI Autopay mandates held at Razorpay and BillDesk, including production references. TJ comes back to you in writing within two weeks.
2. Token migration: Dirk sends a step-by-step overview in the coming days: data taken from your current provider, what we request from the schemes, how network tokens under your name are reused and the registration step that requires, and how authorization rates are protected during cutover.
3. Retry timing for charges initiated by your billing engine: what can move inside your window, in writing, in the same note.
4. Once the mutual NDA is in place, a working session with your team to walk through the migration flow on real data.

On your side, the mutual NDA when ready. Ivvy is copied and will turn it around quickly.

Best,
German

---

## Notes behind the wording

- "Two weeks" for India comes from Antoine in Slack (Sep 24, 06:52 COT): "we are discussing India local reg with Elizabeth Sargeant and the team. This is not straightforward and will require quite some work. Give us a couple of weeks."
- "Registration step" for network tokens comes from Antoine (Sep 24, 06:55 COT): Hostinger holds its own TRID ("all NTs are under our name", Dirk); "they need to do some paperwork to make us the TR-TSP, but nothing ground breaking; we can import their tokens."
- Retry timing for merchant-initiated charges is still the open item from Sep 3 (Dirk). On the call Piotr answered "Exactly" when Paulius asked whether smart routing could delay an MIT charge created on Hostinger's side. The email commits only to a written answer, not to the capability.
- Subscription engine payment methods stated on the call by German (cards, Pix Automático, Apple Pay, Google Pay, PayPal, UPI Autopay "finishing") are not repeated in writing: docs.y.uno list CARD, PAYPAL_ENROLLMENT and PIX_AUTOMATIC.
