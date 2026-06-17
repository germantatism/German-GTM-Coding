# DOORDASH | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: DoorDash
═══════════════════════════════════════

Logo: https://upload.wikimedia.org/wikipedia/commons/6/6a/DoorDash_Logo.svg
Nombre merchant: DoorDash

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: 3 Stacks, Zero Orchestrator
Tittle_Pain Point_2: Double Charges at Scale
Tittle_Pain Point_3: DashPass Billing Failures
Tittle_Pain Point_4: 30+ Markets, Fragmented APMs
Tittle_Pain Point_5: Cross-Border Payout Drag

Desc_Pain Point_1: DoorDash is merging three payment stacks (DoorDash, Wolt, Deliveroo) across 40+ countries in 2026 with no orchestration layer. CEO Xu calls it "several hundred million dollars" in costs.
Desc_Pain Point_2: Widespread double charge complaints flood Reddit, Trustpilot, and TikTok. Chargebacks911 published a dedicated DoorDash merchant chargeback guide. At $100B+ GOV, even 0.5% error rate costs hundreds of millions.
Desc_Pain Point_3: Cancel buttons grayed out, Error 503 on iOS, charges continuing months after cancellation. 35M+ DashPass/Wolt+/Deliveroo Plus subscribers exposed to involuntary churn from billing failures.
Desc_Pain Point_4: Wolt serves 27+ markets each needing local APMs (BLIK, iDEAL, Bancontact, MobilePay). Deliveroo adds UK Open Banking, Carte Bancaire, PostePay. Each requires individual PSP integration work.
Desc_Pain Point_5: DoorDash settles primarily in USD across 40+ countries. Wolt entities span 31 countries with local currency requirements. FX markup and delayed settlement erode margins on every international order.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe
PSP_2: PayPal
PSP_3: Klarna
PSP_4: Marqeta

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: BLIK
Local_M_2: iDEAL
Local_M_3: Bancontact
Local_M_4: Carte Bancaire
Local_M_5: PostePay
Local_M_6: Open Banking (UK)
Local_M_7: Przelewy24
Local_M_8: Satispay
Local_M_9: Mada
Local_M_10: Pix

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Unified Stack Orchestration
Tittle_Yuno_Cap2: Smart Routing + Failover
Tittle_Yuno_Cap3: No-Code Local APM Activation
Tittle_Yuno_Cap4: Real-Time Payment Monitors

Desc_Yuno_Cap1: One API unifying DoorDash + Wolt + Deliveroo payment stacks across 40+ countries. Instead of spending several hundred million dollars on a multi-year platform merge, Yuno's orchestration layer sits on top of all three stacks with a single integration. InDrive scaled 10 LATAM markets in under 8 months with 90% approval rates through Yuno.
Desc_Yuno_Cap2: Per-transaction routing across Stripe, PayPal, Klarna and any future acquirer. Each DashPass renewal and food order routed to the highest performing processor for that card BIN, issuer, and market. Automatic cascade eliminates single-PSP dependency. Up to 50% recovery on failed transactions, directly reducing the double-charge and chargeback volume flooding consumer review sites.
Desc_Yuno_Cap3: Activates the APMs DoorDash is missing across Europe and MENA: BLIK in Poland, iDEAL in Netherlands, Bancontact in Belgium, Carte Bancaire in France, PostePay in Italy, Mada in UAE, Open Banking in UK. One API, 1,000+ payment methods, instant geo-routing. No engineering sprints per market. Wingo (airline, 10+ countries) achieved a 14% approval rate increase with Yuno.
Desc_Yuno_Cap4: Rappi (delivery super-app, 20+ PSPs) used Yuno Monitors to cut response time to payment anomalies from 10 minutes to milliseconds, preventing thousands of rejected transactions. For DoorDash at 903M quarterly orders, millisecond anomaly detection versus manual monitoring means millions in recovered revenue. Analyst time reduced by 80%.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**DoorDash at a glance:**
- NASDAQ: DASH | HQ: San Francisco, CA | CEO: Tony Xu
- FY2025 Revenue: $13.7B (up 28% YoY from $10.7B in 2024)
- FY2025 GAAP Net Income: $935M (up from $123M in 2024)
- Q4 2025 Total Orders: 903M (up 32% YoY)
- Q4 2025 Marketplace GOV: $29.7B (up 39% YoY)
- Q1 2026 Guidance: Marketplace GOV $31.0B to $31.8B, Adjusted EBITDA $675M to $775M
- 56M+ monthly active users (MAU), 35M+ DashPass/Wolt+/Deliveroo Plus subscribers
- Operations in 40+ countries via three brands: DoorDash (US/CA/AU/NZ), Wolt (27+ European/Asian markets), Deliveroo (UK/France/Italy/Belgium/Ireland/UAE/Kuwait/Hong Kong)
- Deliveroo acquired May 2025 for $3.9B; Wolt acquired 2022 for $8.1B
- 2026 flagged as "high investment intensity" year: CEO Xu committing "several hundred million dollars more" to merge three tech stacks into one
- R&D costs jumped 41% in Q4 2025; Sales & Marketing up 31%

**Key leadership (payments relevant):**
- Liangxiao Zhu, VP of Engineering (New Verticals): former Senior Engineering Director at Meta leading Payments across Facebook, Instagram, WhatsApp, and Oculus. Launched Facebook Pay.
- Ryan Sokol, VP Head of Engineering: joined from Uber, where he led Uber Eats engineering (200+ engineers)
- No dedicated VP/Head of Payments identified. Payments likely sits under engineering leadership.

**Confirmed PSPs and payment infrastructure:**
- Stripe Connect: primary PSP for DoorDash (US/CA/AU) and Wolt (Europe). Named in merchant portal documentation, source code.
- Stripe (Deliveroo): Deliveroo was a major Stripe customer before acquisition. 90%+ of Deliveroo's payment volume ran through Stripe in 2020, with 96.98% card authorization rates.
- PayPal: confirmed in US checkout (consumer payments)
- Venmo: confirmed in US checkout (via PayPal)
- Klarna: BNPL integration launched March 2025 (Pay in 4, Pay Later). Also active in Germany (Wolt + Klarna bundled billing).
- Marqeta: card issuing infrastructure for Dasher payment cards
- Hyperwallet (PayPal): Dasher payout processing
- VGS (Very Good Security): card data vaulting detected in Wolt source code
- Wolt License Services Oy: Wolt's own payment institution in Finland (employee benefits card)
- Tempo (Stripe-backed blockchain): announced April 2026 for stablecoin-powered merchant/driver payouts across 40+ countries. Not yet live.
- No third-party payment orchestrator detected (no Spreedly, Primer, Gr4vy, CellPoint, APEXX, or Yuno)

**Payment methods by market:**

US: Visa, Mastercard, Amex, Discover, Apple Pay, Google Pay, PayPal, Venmo, Klarna (Pay in 4, Pay Later), Afterpay, Zip, SNAP/EBT (grocery only), DoorDash Gift Cards, Cash (select markets)

Germany (Wolt): Credit/debit cards, PayPal, Klarna (monthly bundled billing), Google Pay, Apple Pay

Finland (Wolt): Credit/debit cards, MobilePay, Apple Pay, Google Pay, Klarna, Edenred, Smartum, Epassi

Czech Republic (Wolt): Credit/debit cards, Apple Pay, Google Pay, Cash, Lunch benefit cards

Slovakia (Wolt): Credit/debit cards, Ticket Restaurant card, Google Pay, Apple Pay, Cash

Romania (Wolt): Credit/debit cards, Google Pay, Apple Pay, Cash

Hungary (Wolt): Credit/debit cards, Google Pay, Apple Pay, Cash

Kazakhstan (Wolt): Credit/debit cards, Kaspi app, Cash

Israel (Wolt): Credit cards (Israeli-issued), corporate budgets, Wolt credits

UK (Deliveroo): Credit/debit cards, Apple Pay, Google Pay, PayPal

Belgium (Deliveroo): Credit/debit cards, Apple Pay, Google Pay, PayPal

**Missing local APMs (blind spots across DoorDash/Wolt/Deliveroo):**

| # | APM | Market | Why It Matters |
|---|-----|--------|----------------|
| 1 | BLIK | Poland (Wolt) | 90%+ of Polish bank customers use BLIK. Dominant mobile payment. Not offered on Wolt Poland. |
| 2 | iDEAL | Netherlands | Handles 50%+ of all Dutch online transactions. Neither Wolt nor Deliveroo operates in NL currently, but expansion likely. |
| 3 | Bancontact | Belgium (Deliveroo) | 17M+ cards in circulation, more popular than global card networks in Belgium. Not confirmed on Deliveroo Belgium. |
| 4 | Carte Bancaire | France (Deliveroo) | Dominant card network in France. Deliveroo France relies on Stripe but local Carte Bancaire routing improves auth rates. |
| 5 | PostePay | Italy (Deliveroo) | Leading prepaid card/digital wallet in Italy. Critical for non-banked Italian consumers. Not confirmed on Deliveroo Italy. |
| 6 | Open Banking (UK) | UK (Deliveroo) | Account-to-account payments growing rapidly in UK. Lower fees than card-on-file. Not detected on Deliveroo UK. |
| 7 | Przelewy24 | Poland (Wolt) | Leading Polish online bank transfer system. Complements BLIK for desktop users. |
| 8 | Satispay | Italy (Deliveroo) | Mobile payment app with 5M+ users in Italy. Popular for food delivery and small purchases. |
| 9 | Mada | UAE (Deliveroo) | National debit card scheme in Saudi Arabia/UAE region. Critical for Gulf market localization. |
| 10 | Pix | Future LATAM expansion | Handles 70%+ of digital payments in Brazil. If DoorDash ever enters LATAM, Pix is non-negotiable. |

**Payment complaints and outage history:**
- 241+ outages tracked by StatusGator over 3+ years
- July 2025: mass outage, 5,500+ reports, lasted 5.5 hours
- April 2026: orders not processing, error messages suggesting alternative payment methods
- January 2026: cart and checkout pages not loading
- Double charges: widespread and recurring across Reddit, Trustpilot, TikTok, JustAnswer, ConsumerGravity
- DashPass billing: cancel buttons grayed out, Error 503 on iOS, charges after cancellation, charges after account deletion
- Chargebacks: Chargebacks911 published dedicated DoorDash merchant chargeback guide (systemic issue)
- No pro-rated refunds on DashPass ($96 annual subscription, no refund even 2 days after charge)

**Key strategic developments (2025-2026):**
1. Three-stack merge: DoorDash + Wolt + Deliveroo tech consolidation in 2026. CEO Xu: "several hundred million dollars more" in investment. "Massive and expensive undertaking."
2. Deliveroo acquisition (May 2025, $3.9B): adds UK, France, Italy, Belgium, Ireland, UAE, Kuwait, Qatar, Hong Kong, Singapore
3. SevenRooms acquisition ($1.2B): restaurant CRM/reservation platform
4. Market exits (Feb 2026): winding down Japan, Qatar, Singapore, Uzbekistan
5. Stablecoin payouts: Tempo (Stripe + Paradigm blockchain, $5B valuation) partnership announced April 2026 for merchant/driver payouts. Settlement under 1 second. Not yet live.
6. Grocery/retail verticals growing 2x rate of core food delivery; 30%+ MAUs engaging with non-restaurant categories
7. 87.7% of revenue from US ($9.4B in 2024); international is 12.3% but growing at 54%+ YoY

**Yuno case references for the meeting:**

INDRIVE: Scaled 10 LATAM markets in under 8 months. Achieved 90% payment approval rate. Enhanced payment recovery rates to 4.5%+. Smart Routing + real-time monitoring via single API.

RAPPI: Delivery super-app with 20+ payment providers. Yuno Monitors cut response time to payment anomalies from 10 minutes to milliseconds. Analyst time reduced by 80%. New provider implementation time reduced to zero.

MCDONALD'S: Global Yuno client across 200+ countries. Payment orchestration at massive quick-service restaurant scale.

WINGO: Colombian low-cost airline, 37 routes, 10+ countries. 14% approval rate increase with Yuno. Smart Routing enables automatic retries through multiple providers. Access to 1,000+ payment methods via single integration.

**Key meeting angles:**

1. **Three-stack merge is THE moment**: DoorDash is spending several hundred million to merge DoorDash/Wolt/Deliveroo platforms. Yuno sits on top of all three stacks via single API. This is a build-vs-buy conversation at the perfect time.

2. **Delivery competitor already on Yuno**: Rappi (LATAM delivery super-app) uses Yuno for orchestration and real-time monitoring. Competitive intelligence angle.

3. **Double charges + chargebacks are public and painful**: Trustpilot reviews, TikTok videos, Chargebacks911 guides. Smart routing and failover directly reduce these issues. Quantifiable ROI.

4. **European APM localization debt**: Wolt operates in 27+ European markets. Deliveroo adds more. Each market has dominant local APMs not being served. BLIK alone covers 90%+ of Polish bank customers.

5. **DashPass recurring billing optimization**: 35M+ subscribers. Orchestration-level retry logic across multiple PSPs can recover failed renewals before they become cancellations or chargebacks.

6. **Payments leadership from Meta**: Liangxiao Zhu built Facebook Pay and led payments across all Meta properties. She understands payment orchestration at scale. Speak her language.

7. **Stablecoin play signals openness to innovation**: The Tempo partnership shows DoorDash is actively exploring new payment rails. They are not locked into a single provider mentality.

**Sources:**
- [DoorDash FY2025 Financial Results (IR)](https://ir.doordash.com/news/news-details/2026/DoorDash-Releases-Fourth-Quarter-and-Full-Year-2025-Financial-Results/default.aspx)
- [DoorDash FY2025 Results (BusinessWire)](https://www.businesswire.com/news/home/20260218361601/en/DoorDash-Releases-Fourth-Quarter-and-Full-Year-2025-Financial-Results)
- [DoorDash FY2025 Results (StockTitan 8-K)](https://www.stocktitan.net/sec-filings/DASH/8-k-door-dash-inc-reports-material-event-50fb5cee286d.html)
- [DoorDash Q4 Earnings Analysis (Kavout)](https://www.kavout.com/market-lens/doordash-s-q4-report-strong-growth-but-a-profitability-puzzle)
- [DoorDash 2026 Platform Investment (Seeking Alpha)](https://seekingalpha.com/news/4516777-doordash-outlines-major-2026-tech-platform-investment-and-new-product-launches-amid)
- [DoorDash Integration Costs 2026 (MLQ.ai)](https://mlq.ai/news/doordash-signals-major-international-platform-integration-costs-for-2026/)
- [DoorDash Revenue by Geography (Bullfincher)](https://bullfincher.io/companies/doordash/revenue-by-geography)
- [DoorDash Statistics 2026 (DemandSage)](https://www.demandsage.com/doordash-statistics/)
- [DoorDash Statistics (Business of Apps)](https://www.businessofapps.com/data/doordash-statistics/)
- [DoorDash Merchant Portal / Stripe](https://merchants.doordash.com/en-us/learning-center/prevent-payment-delays-stripe)
- [DoorDash Payments Engineering Blog](https://careersatdoordash.com/blog/eight-things-we-learned-from-implementing-payments-in-the-doordash-android-app/)
- [DoorDash Liangxiao Zhu VP Engineering](https://careersatdoordash.com/blog/6-questions-with-doordashs-new-vp-of-engineering-liangxiao-zhu/)
- [DoorDash Klarna BNPL (CNBC)](https://www.cnbc.com/2025/03/20/klarna-lands-buy-now-pay-later-deal-with-doordash-ahead-of-ipo.html)
- [DoorDash Tempo Stablecoin (CoinDesk)](https://www.coindesk.com/business/2026/04/21/doordash-is-bringing-stablecoin-payments-to-masses-with-stripe-backed-blockchain)
- [DoorDash Tempo (PYMNTS)](https://www.pymnts.com/blockchain/2026/doordash-turns-to-tempo-to-offer-stablecoin-payments/)
- [DoorDash Tempo (Benzinga)](https://www.benzinga.com/crypto/cryptocurrency/26/04/51944154/stripe-and-paradigms-tempo-blockchain-valued-at-5b-lands-doordash-partnership)
- [DoorDash Deliveroo Acquisition (Tech.eu)](https://tech.eu/2025/05/06/doordash-expands-european-presence-with-ps24b-deliveroo-acquisition/)
- [DoorDash Market Exits Feb 2026 (IR)](https://ir.doordash.com/news/news-details/2026/DoorDash-to-Wind-Down-Deliveroo-and-Wolt-Operations-in-Four-Countries/default.aspx)
- [DoorDash Growth Strategy (42signals)](https://www.42signals.com/blog/doordash-growth-strategy-2025/)
- [Deliveroo + Stripe Case Study](https://stripe.com/customers/deliveroo)
- [Wolt Entities List](https://explore.wolt.com/en/fin/wolt-entities-list)
- [Wolt Payment Card (Embedded Finance Review)](https://www.embeddedfinancereview.com/wolt-launches-employee-benefits-platform-in-finland-with-its-own-payment-card/)
- [Wolt Klarna Germany](https://wolt.com/en/deu/ulm/article/wolt-klarna-deu)
- [Wolt Finland Payment Methods](https://wolt.com/en/fin/ii/article/helsinki-welcome-to-wolt)
- [Wolt Czech Republic](https://wolt.com/en/cze)
- [DoorDash Payment Methods (Financial Panther)](https://financialpanther.com/doordash-payment-methods/)
- [DoorDash Payment Methods (Ridester)](https://www.ridester.com/doordash-payment-methods/)
- [DoorDash Double Charges (ConsumerGravity)](https://consumergravity.com/doordash-charged-me-twice/)
- [DoorDash Chargebacks (Chargebacks911)](https://chargebacks911.com/doordash-chargeback/)
- [DoorDash DashPass Billing (Threads)](https://www.threads.com/@canerdianeh/post/DCfHUw6yize?hl=en)
- [DoorDash DashPass Cancel Issues (JoinChargeback)](https://www.joinchargeback.com/blogs/how-to-cancel-your-dashpass-subscription)
- [DoorDash Outages (StatusGator)](https://statusgator.com/services/doordash)
- [DoorDash SNAP/EBT Expansion (IR)](https://ir.doordash.com/news/news-details/2025/DoorDash-and-Dollar-General-Partner-to-Unlock-Unprecedented-Food-Access-for-SNAP-Customers/)
- [DoorDash Unauthorized Charges 2026 (Consumoteca)](https://consumoteca.com.co/articles/en/doordash-account-charged-without-order-2026-stepbystep-fix-and-refund-guide)
- [Yuno InDrive Case Study](https://y.uno/success-cases/indrive)
- [Yuno Rappi Case Study](https://y.uno/success-cases/rappi)
- [Yuno Wingo Case Study](https://y.uno/newsroom/wingo-improves-payment-efficiency-with-yuno-as-strategic-partner)
- [Yuno Platform Overview](https://y.uno/)
- [European Local Payment Methods (Noda)](https://noda.live/articles/payment-methods-in-europe)
- [European APMs (TrueLayer)](https://truelayer.com/reports/alternative-payments/european-tour/)
- [Food Delivery Market Share 2026 (OysterLink)](https://oysterlink.com/spotlight/food-delivery-market-share-statistics/)
