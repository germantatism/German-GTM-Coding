# Acebet call notes, Tue 27-Oct-2026 (Yuno <> Acebet, 11:00 PT)

Attendees: Boris (co-founder, Acebet), German Tatis (led), Justo, Sean, Melissa Pottenger. Referral: Trevor at Coinflow recommended Yuno.

## What we learned
- Social-casino (sweepstakes) operator, today on a direct integration with one acquirer. Wants to orchestrate and split volume across several providers.
- Volume: about $25M/month, about 700K tx/month, average ticket $30 to $50 (implied ~$36).
- Goal is leverage and redundancy, not approval uplift: Breeze approval rate is "in the 90s". Wants simple random percentage allocation across acquirers, plus cascading.
- Most volume is Apple Pay and Google Pay, so cascading and routing must work for wallets. On the call we said there are no limitations for cascading, retries or different payment IDs (to verify with SE).
- Geography: US ~98%, Germany ramping (EU sweepstakes). Expansion: Canada (Interac), Australia, France, Spain. No local entities, prefers cross-border acquiring; France-specific setup and 3DS later.
- Entity: Cyprus. Breeze and Coinflow MoR setups are convenient for that; Worldpay cannot support the non-US entity. No payment-agent setup.
- Providers: Breeze (run with Breeze), Coinflow next, Whop agreement in place (they use Whop for payouts; API edge cases; instant bank transfer requires a regular transfer first; non-US company support still in progress), Checkout available. Whop is not a Yuno provider today: ticket needed.
- Competitors evaluated: PaymentIQ (~$0.04/tx), Spreedly (~$0.015/tx), Gr4vy. Expects our proposal to land inside that range.
- Decision path: pricing first, then API docs, then product quality, integrated acquirers and references.
- Reconciliation: they reconcile Breeze crypto settlements manually today and expect the same with Coinflow; automated recon is interesting.
- Integration: wants hosted fields; expects 1 to 2 weeks of tech work after agreement. We offered a 2-week max per new acquirer (with credentials), contractually; competitor quoted 6 weeks.
- Acquirer intros welcome: we proposed North (US high-risk acquirer) and more contacts in the follow-up.

## Commitments from Yuno
1. Pricing proposal today or tomorrow (platform fee + per successful tx, retries charged once, integrations included).
2. WhatsApp group and a Slack channel; add Ben Lee (sales engineer) and Berna.
3. Sandbox access to Boris (he forwards to dev team).
4. Acquirer intros (North + others).
5. Dashboard / orchestration demo if wanted (optional, he is focused on pricing, API docs, acquirer coverage).
6. Internal: add Whop and Breeze as connections in the dashboard; raise a ticket to integrate Whop as a provider (pull Whop API docs).

No go-live date; integration starts after an acceptable proposal and API review. Boris prefers email, WhatsApp or Telegram and wants to move fast.
