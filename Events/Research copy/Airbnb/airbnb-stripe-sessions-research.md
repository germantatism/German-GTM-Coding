# AIRBNB | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Airbnb
=======================================

Logo: https://cdn.brandfetch.io/idU7_ew4SI/w/512/h/512/theme/dark/icon.jpeg?c=1id1ycuFj710000c00
Nombre merchant: Airbnb

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Multi-PSP Complexity
Tittle_Pain Point_2: Auth Rate Blind Spots
Tittle_Pain Point_3: Payout Delays
Tittle_Pain Point_4: Cross-Border FX Drag
Tittle_Pain Point_5: APM Integration Debt

Desc_Pain Point_1: Airbnb operates Stripe, Adyen, Braintree, and PayPal as separate integrations with no unified orchestration layer. Engineering blog confirms each new processor "required rebuilding from scratch" with zero code reuse across 24+ payment routes.
Desc_Pain Point_2: Operating in 191 countries and 70+ currencies, Airbnb lacks smart routing to steer each transaction to the highest performing acquirer per BIN and market. On $81.8B GBV (2024), even 1% auth uplift recovers $818M in booking value annually.
Desc_Pain Point_3: Hosts report payout delays of 10+ days in Airbnb Community forums (2024/2025). Multi-processor settlement reconciliation across JPMorgan, Wells Fargo, Deutsche Bank, and Barclays creates fragmented cash flow visibility.
Desc_Pain Point_4: Guest payments in 70+ currencies settled through USD intermediaries add FX markup on every cross-border transaction. LATAM revenue grew 19.7% YoY to $1.16B (2025), amplifying currency conversion costs at scale.
Desc_Pain Point_5: Airbnb rolled out 20+ local payment methods in 14 months but their engineering blog notes "each local payment vendor exposes different APIs," requiring custom integration per method. Key markets still lack critical APMs.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe
PSP_2: Adyen
PSP_3: Braintree (PayPal)
PSP_4: PayPal

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Mercado Pago
Local_M_2: OXXO
Local_M_3: SPEI
Local_M_4: DANA
Local_M_5: OVO
Local_M_6: Toss Pay
Local_M_7: LINE Pay
Local_M_8: TrueMoney
Local_M_9: PSE
Local_M_10: Efecty

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Recovery
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across Stripe, Adyen, and Braintree. Each booking routed to the highest performing acquirer for that card BIN, issuer, and market. On $81.8B GBV across 191 countries and 70+ currencies, smart routing delivers +3 to 10% auth uplift, translating to hundreds of millions in recovered booking value per year.
Desc_Yuno_Cap2: Automatic cascade across Airbnb's four PSPs eliminates single-processor dependency. When Stripe declines, Yuno reroutes to Adyen or Braintree in milliseconds. Up to 50% recovery on soft declines via instant retry. NOVA AI recovers up to 75% of failed transactions with intelligent retry logic.
Desc_Yuno_Cap3: Activates the APMs Airbnb still lacks: Mercado Pago and OXXO in Mexico (130M+ potential guests), DANA and OVO in Indonesia, Toss Pay in South Korea, LINE Pay in Japan and Thailand, PSE and Efecty in Colombia. One API, 1,000+ payment methods, no custom integration per vendor.
Desc_Yuno_Cap4: One dashboard replacing Airbnb's fragmented Stripe + Adyen + Braintree + PayPal settlement streams. Real-time approval rate monitoring across all 24+ payment routes, centralized reconciliation in 70+ currencies, and millisecond anomaly detection via Monitors. Eliminates the payout reconciliation gaps hosts currently experience.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Airbnb at a glance:**
- Marketplace model: Merchant of Record (MoR) for all transactions globally
- Revenue: $11.1B (2024, +12.1% YoY); ~$12.2B (2025 estimated based on regional growth)
- GBV: $81.8B (2024), 491M+ Nights and Experiences Booked
- 2025 bookings: ~533M Nights and Experiences Booked (+8% YoY)
- Average Daily Rate (ADR): ~$175 globally
- Operates in 220+ markets, 191 countries, 70+ currencies, 24+ payment routes
- NASDAQ: ABNB, market cap ~$80B+
- Founded: 2008, San Francisco. CEO: Brian Chesky

**Revenue by Region (2025):**
- North America: $5.20B (42.5%, +3.8% YoY)
- EMEA: $4.73B (38.6%)
- Latin America: $1.16B (9.5%, +19.7% YoY, fastest growing)
- Asia Pacific: $1.16B (9.5%, +16.5% YoY)

**Key European Markets:** France (159M guest nights), Spain (141M), Italy (107M) collectively = 55% of EU guest nights

**Payments Leadership:**
- Tara Bunch: oversees Community Support, Trust, and Payments teams (220+ countries, 63 currencies). Former VP of AppleCare at Apple (8 years)
- Sam Shrauger: Former VP, Global Head of Payments and Chairman/CEO of Airbnb Payments Inc. (now COO at Skipify). Previously SVP Digital and Consumer Products at Visa, VP Global Product at PayPal
- Mike Liberatore: CFO of Airbnb Payments, Inc. (since July 2016)
- Multiple open roles: Sr. Software Engineer Payments, Sr. SE Payments Platform, Sr. SE Payments Infrastructure, SE Payments, Sr. SE Payments Post Transaction Risk

**Confirmed PSPs:**
- Stripe: credit card processing and host payouts (confirmed via Stripe newsroom partnership + Medium analysis)
- Adyen: multi-currency transaction processing across numerous countries (confirmed via Medium/MoR analysis)
- Braintree: original PSP from 2010/2011, still in use for specific routes (confirmed via Quora/Paylosophy sources)
- PayPal: alternative payment method for guest bookings (confirmed via Help Center)
- Banking partners: JPMorgan Chase, Wells Fargo (US payouts), Deutsche Bank (EU), Barclays (UK)
- No payment orchestrator detected
- Actively hiring 5+ payments engineering roles (gateway platform, infrastructure, post-transaction risk)

**Payment Infrastructure Details (from Airbnb Engineering Blog):**
- Built three standalone systems: Billing Interface API, Payments Gateway, Financial Data Pipeline
- Payments Gateway provides "a unified API that supports bi-directional transactions across all processors"
- Uses append-only data recording and Kafka-based event distribution
- Financial pipeline: Spark + Scala, double-entry bookkeeping
- Job postings confirm: "design and build a payments gateway platform that is fast and easy to integrate with, reliable for money movements, smart to route business cost-effectively, resilient to any external processor downtime"
- Config-driven approach using YAML-based Payment Method Config as single source of truth
- Multi-Step Transactions (MST) framework for processor-agnostic payment flows
- PSP Emulator for testing without sandbox dependencies

**Local Payment Methods Currently Supported:**
- Global: Visa, Mastercard, Amex, JCB, Discover, Apple Pay, Google Pay, PayPal
- US: Bank account transfers, Klarna (BNPL)
- Brazil: Pix, Elo, Hipercard
- China: Alipay, WeChat Pay
- India: UPI, Netbanking
- South Korea: Naver Pay, KakaoPay
- Indonesia: GoPay
- Netherlands: iDEAL
- Germany: Sofort
- France: Cartes Bancaires
- Poland: BLIK
- Philippines: GCash
- Malaysia: FPX
- Kenya: M-PESA
- Ghana/Uganda: MTN
- Belgium: Payconiq
- Norway: Vipps
- Denmark/Finland: MobilePay
- Portugal: MBWay
- Switzerland: Twint
- Thailand: PromptPay
- Australia: Eftpos
- Czech Republic/Slovakia: Online Banking
- Canada: Klarna

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (45% of revenue, $5.2B)
  Currently offer: Visa/MC/Amex/Discover, PayPal, Apple Pay, Google Pay, Klarna, Bank transfers
  Missing: Venmo (standalone), Cash App Pay, Affirm
  Cash App has 57M+ US users; Venmo has 90M+ users. Both overlap with Airbnb's guest demographic.

MARKET 2: Mexico (key LATAM growth market)
  Currently offer: Visa/MC, PayPal
  Missing: OXXO, SPEI, Mercado Pago, CoDi, Kueski Pay
  OXXO processes 55%+ of e-commerce cash payments in Mexico. Mercado Pago dominates digital wallets across LATAM. SPEI is the national real-time bank transfer rail.

MARKET 3: Indonesia (key APAC growth market)
  Currently offer: GoPay
  Missing: DANA, OVO, ShopeePay, QRIS (national QR standard)
  GoPay is only one of four major e-wallets. DANA has 135M+ users, OVO has 120M+ users. QRIS is the government-mandated interoperable QR code system.

MARKET 4: South Korea (mature market, high digital adoption)
  Currently offer: Naver Pay, KakaoPay
  Missing: Toss Pay, Samsung Pay (online), PAYCO
  Toss has 22M+ MAU in a country of 52M. Samsung Pay is used by 14M+ Koreans. PAYCO is a top-5 mobile payment service.

MARKET 5: Colombia (emerging LATAM market)
  Currently offer: Visa/MC, PayPal
  Missing: PSE, Efecty, Nequi, Daviplata
  PSE (online banking) processes 60%+ of Colombian e-commerce. Efecty is the leading cash payment network. Nequi has 18M+ users (fastest growing wallet in Colombia).

MARKET 6: Japan (27% domestic trip growth in 2024)
  Currently offer: JCB, Visa/MC
  Missing: Konbini, PayPay, LINE Pay, Rakuten Pay
  Konbini (convenience store payments) is used by 35%+ of Japanese online shoppers. PayPay has 62M+ users. LINE Pay has 40M+ users in Japan.

MARKET 7: Thailand (APAC expansion)
  Currently offer: PromptPay
  Missing: TrueMoney, LINE Pay (TH), RabbitPay
  TrueMoney Wallet has 30M+ users in Thailand. LINE Pay has significant adoption as a secondary wallet.

**Payment Pain Points (from community forums and help center):**
1. Recurring guest payment declines: "Airbnb keeps declining my payments" threads across Community forums
2. Host payout delays: "Airbnb not sending Payouts 2024/2025" with delays of 10+ days reported
3. Multi-method failures: Users unable to use credit cards, PayPal, AND Google Pay simultaneously
4. 3DS authentication failures causing booking abandonment
5. "Do not honor" bank errors with no smart retry or cascade
6. Currency mismatch errors: "Can't complete this payment in your currency"
7. Alipay only works on desktop/browser, not in Airbnb app
8. 102+ outages tracked by StatusGator since January 2024
9. AWS outage (October 2025) blocked all Airbnb services including payments
10. "You have reached your Airbnb access quota" blocks during peak booking periods

**Key Meeting Angles:**
1. **Build vs. Buy**: Airbnb is hiring 5+ payments engineers to build what Yuno provides out of the box. Their engineering blog admits "integration of new payment processors was time-consuming and continued to increase code complexity"
2. **LATAM is #1 growth region** (+19.7% YoY) but Mexico, Colombia, Argentina all lack critical local APMs (OXXO, Mercado Pago, PSE, Efecty)
3. **$81.8B GBV at stake**: Smart routing on this volume delivers massive auth uplift. InDrive achieved 90% approval across 10 markets with Yuno
4. **Multi-PSP without orchestration**: Running Stripe + Adyen + Braintree separately is exactly the problem Yuno solves. McDonald's gained +4.7% auth rate ($3.2M revenue impact) with Yuno orchestration
5. **40 local payment methods in 14 months, but still gaps**: Yuno's 1,000+ APMs via single API eliminates per-vendor integration debt
6. **Sam Shrauger's departure** (to Skipify, mid-2024): Payments leadership transition creates opportunity for new vendor conversations
7. **Host satisfaction**: Payout delays directly impact host retention. Unified reconciliation across all processors improves cash flow predictability
8. **Competitor pressure**: Booking.com and Vrbo both invest heavily in local payment methods. Airbnb cannot afford checkout friction in high-growth markets

**Sources:**
- [Airbnb Help Center: Payment Methods Accepted](https://www.airbnb.com/help/article/126)
- [Airbnb Help Center: Why Payment Is Declined](https://www.airbnb.com/help/article/98)
- [Airbnb Help Center: Something Went Wrong](https://www.airbnb.com/help/article/2512)
- [Airbnb Engineering: Scaling Payment Platform](https://medium.com/airbnb-engineering/scaling-airbnbs-payment-platform-43ebfc99b324)
- [Airbnb Engineering: Pay As a Local](https://medium.com/airbnb-engineering/pay-as-a-local-bef469b72f32)
- [Medium: How Airbnb Manages Payments as MoR](https://medium.com/@r.b.srikanth/behind-the-stay-how-airbnb-manages-payments-as-mor-1725537c8f83)
- [Stripe Newsroom: Airbnb Partners with Stripe](https://stripe.com/newsroom/news/airbnb-and-stripe)
- [Airbnb Careers: Sr. SE Payments](https://careers.airbnb.com/positions/6912212/)
- [Airbnb Careers: Sr. SE Payments Platform](https://careers.airbnb.com/positions/7512075/)
- [Airbnb Careers: Sr. SE Payments Infrastructure](https://careers.airbnb.com/positions/7514185/)
- [Airbnb Careers: SE Payments](https://careers.airbnb.com/positions/7237254/)
- [Airbnb Careers: Sr. SE Post Transaction Risk](https://careers.airbnb.com/positions/7624302/)
- [The Org: Sam Shrauger, VP Global Head of Payments](https://theorg.com/org/airbnb/org-chart/sam-shrauger)
- [Fintech Futures: Skipify Names Former Airbnb Payments Chief](https://www.fintechfutures.com/paytech/skipify-names-former-airbnb-payments-chief-sam-shrauger-as-new-coo)
- [Airbnb Community: Payment Not Processing](https://community.withairbnb.com/t5/Support-with-your-bookings/Payment-Not-Processing-for-Booking/m-p/1952085)
- [Airbnb Community: Keeps Declining Payments](https://community.withairbnb.com/t5/Support-with-your-bookings/Airbnb-keeps-declining-my-payments/td-p/2132682)
- [Airbnb Community: Payout Delays 2024/2025](https://community.withairbnb.com/t5/Help-with-your-business/Airbnb-not-sending-Payouts-2024-2025-getting-nervous/m-p/2038961)
- [Airbnb Q4 2024 Financial Results](https://news.airbnb.com/airbnb-q4-2024-financial-results/)
- [Bullfincher: Airbnb Revenue by Region](https://bullfincher.io/companies/airbnb/revenue-by-geography)
- [Business of Apps: Airbnb Statistics 2026](https://www.businessofapps.com/data/airbnb-statistics/)
- [Airbnb 10-K 2024 (SEC Filing)](https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm)
- [StatusGator: Airbnb Outages](https://statusgator.com/services/airbnb)
- [Rental Scale-Up: Airbnb Payment Terms 2025](https://www.rentalscaleup.com/airbnb-payment-terms-update-for-hosts/)
