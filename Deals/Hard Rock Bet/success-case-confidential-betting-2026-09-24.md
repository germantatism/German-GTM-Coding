# Success case for Hard Rock Bet: confidential sports betting client

Built 2026-09-24. Merchant anonymized on purpose. Every figure below is verified in Slack (go-live post, KAM performance threads, TAM results post, finance billing) and in y.uno published content. Provenance table at the end. Do not add numbers that are not in that table.

## Version A: email (third touch, unnamed client, plain text, impact bullets)

Hi ((contact_name)),

Hope you had a chance to go over my last emails. To keep adding value, I wanted to share a recent success in the sports betting industry, a licensed sportsbook operator processing more than 600,000 deposits a month through Yuno.

With our payment infrastructure, they now benefit from:

3 providers connected under one integration, with automatic fallback.

Approval rate from 82% to over 88%.

Transactions up 17% and average ticket up 22%.

World Cup peak: deposited value up 22% with approval above 88%.

Fraud and provider error rejections below 0.1% of volume.

Live in under four months, compliance review included.

We would love to do the same for Hard Rock Bet!

What do you think we meet for 20 minutes next week and discuss the ideas we have?

All the best,
German

Note: "under three months" is not accurate (contract 2025-11-19, live 2026-03-05). Keep "under four months".

## Version B: talk track for a call (pain of Hard Rock Bet, what we did for the confidential client, proof)

1. Five vendors on the money path and no orchestration; provider choice is a hardcoded flag. We put three instant bank transfer providers behind one integration with automatic fallback; the third provider only receives the hard cases. Proof: three active providers in the June 2026 analysis with the cascade order visible in the data.
2. Credit cards removed in July 2026, so all deposit volume now rides debit, pay by bank and wallets. Our client runs 100% of deposits on one instant bank rail and we still moved approval from 82% to over 88%. Proof: TAM results post, 18 June 2026.
3. Peak events. Opening days of the 2026 World Cup: daily transactions plus 17%, deposited value plus 22%, approval above 88% every one of the first four match days; the worst day of the following week was still 85.8% and the cause (expired QR codes on one provider) was identified the same day. Proof: KAM performance threads, 15 and 22 June 2026.
4. Withdrawals are where Hard Rock breaks (closed loop, 1 to 5 days, Trustpilot 1.3). We are extending the same routing layer to payouts with two routes and fallback; bank transfer payouts are already live for another betting operator we serve in Mexico. Proof: payout rollout thread September 2026; Mexico operator on SPEI deposits and payouts.
5. Expansion (Ontario live since July 2026, chairman has said publicly he wants Brazil). Our client is a licensed operator in Brazil and we run its PIX volume at scale, so a Brazil entry would land on rails we already operate. Proof: go-live post, 5 March 2026.
6. Time to value: contract signed 19 November 2025, live 5 March 2026, including compliance and legal review for the betting vertical.

## Optional supporting line (different client, published on y.uno, gaming studio not betting)

A global gaming studio on Yuno lifted approval rates 11%, recovered 30 million dollars from failed transactions, cut PSP onboarding time 90% and entered 10 new markets in under three months. Use only as a second reference; it is not the betting client above.

## Provenance (internal, never customer facing)

| Claim | Real merchant | Source |
|---|---|---|
| Licensed sports betting operator, LatAm, PIX, high volume routing | Aposta Ganha (Brazil) | #go-live, Andyara Pedrosa, 2026-03-05 |
| More than 600K instant bank transfer tx per month | Aposta Ganha | #finance-merchants billing: 720,924 PIX pay-in Jun-26; 644,045 Jul-26; 644,672 Aug-26 |
| Three providers with fallback (Pagsmile, StarkBank, OKTO as third fallback) | Aposta Ganha | #aposta-ganha_yuno, Benjamin Lee, 2026-06-22 analysis; #general 2026-06-12 |
| Approval 82% to over 88%, ticket +22%, tx +17% | Aposta Ganha | #general, Sarah Santiago, 2026-06-18 (after Pagsmile webhook feature + StarkBank) |
| World Cup: daily tx +17.3%, value +22.0%, AR above 88% on 11 to 14 June; 19 June 85.84% due to EXPIRED_BY_PROVIDER | Aposta Ganha | #aposta-ganha_yuno, Benjamin Lee, 2026-06-15 and 2026-06-22 |
| Weekly performance reviews with the merchant | Aposta Ganha | Weekly "Semanal: Aposta Ganha <> Yuno" invites, KAM analyses cc merchant (Victor Sales, Rony Silva) |
| Payouts being extended, two payout routes | Aposta Ganha | #aposta-ganha_yuno and #product-tech, Sept 2026 (PIX_PAYOUT Safeway tests; go-live targeted Monday 2026-09-28). NOT live yet as of 2026-09-24 |
| Bank transfer deposits and payouts live for a betting operator in Mexico | Betcris | #product-tech: STP SPEI pay-in and SPEI dispersion payouts, 2025 to 2026 |
| Contract to live in under four months incl. compliance (3.5 months; do not say under three) | Aposta Ganha | Salesforce contract signed 2025-11-19 (#salesops-legal); live 2026-03-05 (#go-live credits Compliance & Legal) |
| Fraud and provider error rejections below 0.1% | Aposta Ganha | #aposta-ganha_yuno, Benjamin Lee, 2026-06-22: FRAUD_VALIDATION 0.03%, PROVIDER_INTERNAL_ERROR 0.03% of 220,515 tx |
| Gaming studio +11% / $30M / 90% / 10 markets | Unnamed, published | y.uno post "Why orchestration is now mission critical for gaming companies" |

Things deliberately NOT claimed: zero downtime during the World Cup (not verified), real time monitors as delivered value (monitors were configured in June 2026 but had issues), casino product for the client (not verified), payouts as live for the Brazilian client (in rollout).

Hard Rock Bet context used for Version B comes from Magdalena Torrealba's brief with Payments Concierge in #roberto-ai on 2026-09-24 (stack: Paysafe, Braintree, Trustly, Nuvei via Mazooma, Sightline; no orchestration; no credit cards since July 2026; Ontario live 22 July 2026; Director of Payments Blair Ramsey). That brief notes the account sits with Samuel Carreño by industry; flag before outreach.
