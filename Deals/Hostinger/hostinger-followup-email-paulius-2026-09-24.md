# Follow-up email to Paulius after the Sep 24, 2026 demo (v2)

**Status:** Gmail draft v2 created Sep 24, 2026 as a reply in the thread "Hostinger + Yuno | Demo" (to Paulius; cc Antoine, Dirk, Justo, Piotr, TJ, Ivvy). Review and send. v1 (which described the migration data and the network token registration step) was deleted after Dirk shared his own token-migration note; German's email now opens and hands off to Dirk.
**Sequence agreed:** German's recap first; Dirk's token-migration note follows in the same thread (draft saved in hostinger-dirk-token-migration-email-draft-2026-09-24.md, with three issues to fix before it goes); TJ sends the India answer separately.

---

Subject: Re: Hostinger + Yuno | Demo

Hi Paulius,

Thank you for this morning. A short recap and how we follow up.

What we took from the session

- India first: Razorpay and BillDesk under one integration, with routing and token storage that meet local requirements. Vaulting as a service runs as a separate track.
- Token migration is the question to answer with precision: a couple of million tokens, network tokens under your own name, scheme transaction IDs preserved, no dip in authorization rates.
- Your billing engine stays in house. What you want from us is execution of each charge, fallback across providers and retry timing inside your dunning window, not a new plan catalog.

How we follow up

1. Token migration: Dirk replies in this thread with the process step by step, what we take from your current provider, how network transaction IDs and network tokens are handled, and how we protect the authorization rate wave by wave.
2. India: TJ, Antoine and our India team are working through what is possible under RBI rules for card tokens and UPI Autopay mandates held at Razorpay and BillDesk, including production references. TJ comes back to you in writing within two weeks.
3. Retry timing for charges initiated by your billing engine: what can move inside your window and what cannot, in a separate written note this week.
4. Once the mutual NDA is in place, a working session with your team to go through the migration on your own data.

On your side, the mutual NDA when ready. Ivvy is copied and will turn it around quickly.

Best,
German

---

## Notes behind the wording

- "Two weeks" for India: Antoine in Slack (Sep 24, 06:52 COT): "we are discussing India local reg with Elizabeth Sargeant and the team. This is not straightforward and will require quite some work. Give us a couple of weeks."
- Network tokens are deliberately not characterised in German's email. Antoine (Slack, Sep 24): Hostinger has its own TRID, paperwork to make Yuno the TR-TSP, "we can import their tokens." Dirk's draft: not portable, fresh tokens under a Yuno-operated requestor ID. Dirk and Antoine align before Dirk's note goes out.
- Retry timing for merchant-initiated charges: open since Sep 3 (Dirk). On the call Piotr answered "Exactly" when Paulius asked whether smart routing could delay an MIT created on Hostinger's side. German's email commits only to a written answer this week; owner to be confirmed (Dirk or Product).
- Subscription engine payment methods stated on the call by German (cards, Pix Automático, Apple Pay, Google Pay, PayPal, UPI Autopay "finishing") are not repeated in writing: docs.y.uno list CARD, PAYPAL_ENROLLMENT and PIX_AUTOMATIC.
