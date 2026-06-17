# APPLOVIN | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: AppLovin
=======================================

Logo: https://companieslogo.com/img/orig/APP_BIG-50063fef.png?t=1752312076
Nombre merchant: AppLovin

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Single Acquirer Risk
Tittle_Pain Point_2: E-Commerce Billing Gap
Tittle_Pain Point_3: Global APM Blind Spots
Tittle_Pain Point_4: Cross-Border FX Drag
Tittle_Pain Point_5: Advertiser Card Declines

Desc_Pain Point_1: Axon Ads Manager runs on one card processor with no failover. A single outage freezes daily billing for 600+ e-commerce advertisers globally.
Desc_Pain Point_2: Self-serve platform launched Oct 2025 billing only cards. No ACH, SEPA, or local wallets. 57% go-live conversion signals checkout friction.
Desc_Pain Point_3: Expanding into Japan, Korea, Germany, and Brazil with zero local payment acceptance. No Konbini, KakaoPay, SEPA DD, or Pix available.
Desc_Pain Point_4: All billing settles in USD. Non-US advertisers across 30+ countries absorb FX markup on every daily charge cycle, inflating campaign costs.
Desc_Pain Point_5: Every failed card charge halts live campaigns instantly. No automatic retry across processors; up to 2 backup cards are the only fallback.

SLIDE 1: PSP TOPOLOGY

PSP_1: Tipalti (publisher payouts)
PSP_2: Credit/Debit Card Processor (advertiser billing, name undisclosed)
PSP_3: PayPal (publisher payouts)
PSP_4: ACH Direct Deposit (publisher payouts)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Konbini
Local_M_2: KakaoPay
Local_M_3: SEPA Direct Debit
Local_M_4: Pix
Local_M_5: iDEAL
Local_M_6: Boleto
Local_M_7: BLIK
Local_M_8: Bancontact
Local_M_9: OXXO
Local_M_10: PayPay

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each advertiser charge to the highest-performing acquirer for that card BIN and geography. With $5.48B in 2025 revenue and daily billing cycles for thousands of advertisers, even a 3% auth uplift recovers millions in unfrozen campaign spend annually.
Desc_Yuno_Cap2: When the primary processor declines a daily pre-charge, Yuno cascades to the next best acquirer in milliseconds. Campaigns stay live, ad delivery stays uninterrupted, and up to 50% of failed charges are recovered automatically.
Desc_Yuno_Cap3: Unlocks the APMs AppLovin's advertisers need: Konbini and PayPay in Japan, KakaoPay in South Korea, SEPA DD in Germany, Pix in Brazil, iDEAL in Netherlands, BLIK in Poland. One API, 1,000+ methods, no engineering sprint per market.
Desc_Yuno_Cap4: Single dashboard replacing AppLovin's fragmented Tipalti + card processor + PayPal + ACH payout streams. Real-time approval monitoring across all advertiser billing and publisher payouts, centralized reconciliation, millisecond anomaly detection via NOVA.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**AppLovin at a glance:**
- Founded 2012, HQ Palo Alto, CA. Public: NASDAQ APP
- Revenue: $5.48B (FY2025), up 70% YoY. Q4 2025: $1.66B, up 66% YoY
- Q1 2026 guidance: $1.745B to $1.775B (60% YoY growth)
- Transformed from gaming + ad-tech hybrid into pure advertising software platform
- Divested gaming studios (Lions Studios) to Tripledot Studios for $800M (closed June 2025)
- AXON: AI-powered ad engine, rebranded Oct 2025, powering both app install and e-commerce campaigns
- E-commerce now generates $1B+ annually across 600+ advertisers
- Self-serve Axon Ads Manager launched Oct 2025 (referral-only), global GA planned H1 2026
- Key offices: Palo Alto, Dublin, Berlin, Tokyo, Seoul, Beijing
- Market cap: ~$100B+ (2026)

**Confirmed PSPs / Payment Infrastructure:**
- Tipalti: primary publisher payout provider (ACH, wire, check, PayPal)
- Axon Ads Manager: credit/debit card only for advertiser billing (processor name undisclosed)
- Daily billing model: card charged at 0:00 UTC for next day's budget; additional charges for intraday budget increases
- Advertisers can add up to 2 backup cards for failover
- No payment orchestrator detected
- Publisher minimum payout: $100 (NET 15 schedule)

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (primary market)
  OK Currently offer: Credit/debit card billing for advertisers
  Missing: ACH billing, real-time payment options for large enterprise advertisers
  Note: Self-serve now driving Shopify-based e-commerce advertiser onboarding

MARKET 2: Japan (key non-English expansion market for 2026)
  OK Currently offer: Credit/debit card billing
  Missing: Konbini, PayPay, JCB local acquiring, bank transfer
  Note: AppLovin has Tokyo office; Japan is a top-priority expansion market

MARKET 3: South Korea (key non-English expansion market for 2026)
  OK Currently offer: Credit/debit card billing
  Missing: KakaoPay, Naver Pay, Samsung Pay local, bank transfer
  Note: Seoul office active; Korean mobile gaming is a core vertical

MARKET 4: Germany / EU (European expansion hub)
  OK Currently offer: Credit/debit card billing
  Missing: SEPA Direct Debit, Sofort, iDEAL (NL), Bancontact (BE), BLIK (PL)
  Note: Berlin office; EU e-commerce advertisers need local billing options

MARKET 5: Brazil (LatAm growth opportunity)
  OK Currently offer: Credit/debit card billing
  Missing: Pix, Boleto, local installment cards
  Note: Brazil's e-commerce market is top 10 globally; Pix handles 70%+ of digital payments

**Key meeting angles:**
1. **E-commerce billing bottleneck** | 57% go-live conversion means 43% of qualified advertisers fail to activate. Payment friction is a likely contributor.
2. **Daily pre-charge vulnerability** | Single processor failure halts all live campaigns. No automatic cascade, only manual backup cards.
3. **International self-serve launch** | Global GA in H1 2026 requires local payment acceptance in Japan, Korea, EU, LatAm.
4. **$5.48B revenue at stake** | At this scale, even 1% auth improvement translates to $50M+ in protected advertiser spend.
5. **Competitor gap** | Meta accepts local payments in every market. AppLovin's card-only billing is a competitive disadvantage for global advertisers.
6. **Publisher payout fragmentation** | Tipalti + PayPal + ACH streams lack unified monitoring and reconciliation.

**Sources:**
- [AppLovin Axon Payments (Tipalti)](https://support.axon.ai/en/max/max-dashboard/account/payments)
- [AppLovin Monetization Payment FAQ](https://support.axon.ai/en/max/faq/faq-applovin-monetization-payment/)
- [AppLovin Axon Billing](https://support.axon.ai/en/growth/ad-accounts/how-billing-works-on-axon)
- [AppLovin Privacy Policy](https://legal.applovin.com/privacy/)
- [AppLovin Q4 2025 Earnings](https://wmediaresearch.com/2026/02/13/applovin-q4-2025-earnings-stunning-numbers-but-meta-threat-looms/)
- [AppLovin E-Commerce Expansion](https://finance.yahoo.com/markets/stocks/articles/applovins-e-commerce-expansion-could-175200968.html)
- [AppLovin Self-Serve Launch](https://mlq.ai/news/applovins-e-commerce-push-hinges-on-self-serve-launch-and-creative-automation-in-first-half-of-2026/)
- [AppLovin International Expansion](https://finance.yahoo.com/news/applovins-international-expansion-poised-supercharge-143500497.html)
- [AppLovin Wikipedia](https://en.wikipedia.org/wiki/AppLovin)
- [Stripe Case Study: Lime (Stripe as PSP)](https://stripe.com/customers/lime)
- [AppLovin Logo](https://companieslogo.com/applovin/logo/)
