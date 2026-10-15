# Luni x Yuno · BDM intro call (2026-10-15, 11:15 COT, 30 min)

Attendees: Artsiom Kalianchuk (Luni, artsiom@luni.app; product side, "my role plus our growth managers" own the decision), German Tatis, Susana Awad (SDR, organizer).
Transcript: Google Doc 1g_v1wa2HduI-EwLtUBuUk9vuM2Cor5gKqlcFQq_LWEU (attached to the calendar event). Gong summary pasted by German the same day.

## Company (public, 15-oct-2026)
- Luni: Bordeaux-based mobile app studio founded 2017; founder and CEO Adrien Miniatti; offices Bordeaux and Paris. Self-described "France's largest independent iOS app publisher"; bootstrapped to about EUR 35M revenue in three years and 250K+ daily downloads (company pages, not independently verified).
- Apps named publicly: Shorts, Astro Club, Scanner, Mindlift (also cited: Fitness Coach, Meditation Nest, Photo Editor, Omada). Job listings: "most of our revenue comes from in-app subscriptions in the US".
- Logo: black wordmark on transparent (teamtailor CDN); white version via images.weserv.nl negate filter in the deck.

## Payment stack and numbers (Artsiom, September data)
- PSPs: Stripe US (main), Stripe France, Paddle. PayPal US integration in progress. Methods: cards, Apple Pay, Google Pay, "a few local options". Checkout is "super straightforward" (basic).
- Attempts, not approvals: Stripe US ~40K attempts at 37% success; Stripe France ~1.5K at 68%; third account ~1.5K, high acceptance. Total a little over 40K attempts, weighted success "a little bit more than 40%" (he will double check).
- Average ticket: German said $18, Artsiom confirmed.
- Why approval is low (his reading): heavy retry logic on unrecoverable declines (insufficient funds, do not honor) inflates attempts; geo and card diversification; cross-border processing. A Spanish card today is processed cross-border, not through the French entity. Legal entities: US and France only (France intended to cover the EU).
- Mix: ~95% subscriptions. New telecom-direction app on one-time purchases, AOV a bit above $10, planned ~$20 next year; expected mix in a year 85 to 90% subscriptions, 10 to 15% one-time.
- Geography: focused on English-speaking markets (US, Canada, UK). Not acquiring in Spain, Netherlands, Asia, LatAm because the setup "wouldn't be super reliable".

## What they want
- A middleware / orchestration layer: route by geo and card factors, extra retry logic, more PSPs, local processing (merchant of record where it helps), better checkout. He is "pretty sure we could double the success rate". German on the call: "from 37 we could for sure go beyond 50".
- Timing: no urgency, but "as soon as possible" once a strong proposal is in; open to a small start and renegotiating at higher volume.
- Decision: product team (Artsiom + growth managers) is the biggest stakeholder; finance and the founder for the financial part (not a blocker); frontend/technical team for integration. Technical call offered by German.
- Commercial framing by German: platform fee + fee per successful transaction, minimums around $15K/month, sweet spot 120K+ tx/month; warned that low volume means a higher effective rate. Artsiom: send the numbers, they simulate uplift scenarios vs cost and decide on net margin.

## Demo shown
Parent account with sub-accounts (US, France); marketplace (1,200+ methods, 450+ providers incl. acquirers, gateways, MoR, 50+ anti-fraud); connect a provider with credentials, set costs, assign to account; routing with conditions (country = France -> Yuno 3DS -> Adyen -> fallback), decline-type grouping so insufficient funds is not retried; Smart Routing optimizing conversion + cost or conversion + latency.

## Next steps
- German: commercial proposal with pricing scenarios (this deck) and a 15-minute follow-up next week.
- Artsiom: updated decline breakdown by category.
