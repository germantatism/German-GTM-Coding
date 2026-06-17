# APPLE | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Apple
=======================================

Logo: https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Apple_logo_black.svg/800px-Apple_logo_black.svg.png
Nombre merchant: Apple

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Subscription Churn Leak
Tittle_Pain Point_2: Cross-Border Decline Rates
Tittle_Pain Point_3: APM Coverage Gaps
Tittle_Pain Point_4: Outage Vulnerability
Tittle_Pain Point_5: DMA Compliance Cost

Desc_Pain Point_1: Failed recurring payments cost subscription businesses $129B+ in 2025. Apple's 1B+ paid subscriptions face involuntary churn from expired cards, issuer blocks, and cross-border declines across 175 regions.
Desc_Pain Point_2: International card failures run 2x to 3x higher than domestic. With 57% of Apple revenue outside the Americas, cross-border acquiring adds FX markup and issuer friction across every market.
Desc_Pain Point_3: App Store supports 200+ methods but key gaps remain. No Pix in Brazil (42% of e-commerce), no UPI in India (75% of digital payments), no OXXO in Mexico. Billions in addressable spend unreachable.
Desc_Pain Point_4: May 2025 global outage hit Apple Pay, Apple Cash, Apple Card, and Wallet simultaneously. 3,000+ reports in one hour. Single-stack architecture left zero fallback for merchants and users.
Desc_Pain Point_5: EU fined Apple $580M for DMA violations. Alternative payment providers now mandated. Managing 5%+ Core Technology Commission across multiple PSPs and marketplaces adds operational complexity.

SLIDE 1: PSP TOPOLOGY

PSP_1: Apple Internal (StoreKit/IAP)
PSP_2: JPMorgan Chase (Apple Card)
PSP_3: Green Dot Bank (Apple Cash)
PSP_4: Mastercard (Network)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: UPI
Local_M_3: OXXO
Local_M_4: PSE
Local_M_5: Nequi
Local_M_6: SPEI
Local_M_7: GCash
Local_M_8: DANA
Local_M_9: Bizum
Local_M_10: M-Pesa

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Recovery
Tittle_Yuno_Cap3: 1,000+ Payment Methods
Tittle_Yuno_Cap4: NOVA Fraud Intelligence

Desc_Yuno_Cap1: Per-transaction routing across multiple acquirers optimized by card BIN, issuer, and market. With $109B in services revenue and 1B+ paid subscriptions across 175 regions, even a 3% authorization uplift on recurring billing translates to billions in recovered revenue. InDrive achieved 90% approval rates using Yuno's intelligent routing across 10 LATAM markets.
Desc_Yuno_Cap2: Automatic cascade when primary processor declines or goes offline. Eliminates the single-point-of-failure exposed in the May 2025 global outage. Failed subscription renewals retry through the next best acquirer in milliseconds. Yuno clients recover up to 50% of initially declined transactions. McDonald's uses this for always-on payment availability.
Desc_Yuno_Cap3: One API activates every local payment method Apple's services currently miss: Pix in Brazil (70%+ of digital payments), UPI in India (10B+ monthly transactions), OXXO and SPEI in Mexico, GCash in Philippines, M-Pesa in Africa. No per-market engineering sprints. Rappi leverages Yuno to offer hyper-local methods with zero added integration time.
Desc_Yuno_Cap4: AI-powered fraud detection analyzing 5,000+ data points per transaction. Apple blocked $2B in App Store fraud in 2024 alone; NOVA augments existing defenses with cross-network intelligence, reducing false declines by up to 75%. Wingo reduced fraudulent transactions significantly while maintaining frictionless user experience.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Apple at a glance:**
- $416B total revenue FY2025 ($109B from Services, a 13.5% YoY increase, all-time high)
- 1B+ paid subscriptions across all services (App Store, iCloud, Apple Music, Apple TV+, Apple Arcade, Apple News+, Apple Fitness+)
- 850M weekly App Store users across 175 regions
- 818M+ Apple Pay users globally (2025), processing $7.6T+ in transaction volume
- Apple Pay accepted at 90% of US retailers, live in 89 markets, supported by 11,000+ banks
- CEO transition: John Ternus succeeding Tim Cook (September 2026), Tim Cook becomes Executive Chairman
- Jennifer Bailey: VP of Apple Pay and Apple Wallet, leads all payment and commerce services globally
- Apple Pay blocked $1B+ in fraud in 2025; App Store prevented $9B+ in fraud over five years

**Revenue by region (FY2025):**
- Americas: $178.35B (42.86%)
- Europe: $111.03B (26.69%)
- Greater China: $64.38B (15.48%)
- Japan: $28.70B (6.90%)
- Rest of Asia Pacific: $33.70B (8.10%)

**Confirmed PSPs and partners:**
- Apple Internal (StoreKit/IAP): proprietary end-to-end payment processing for App Store, in-app purchases, subscriptions. Handles decryption, token validation, and settlement across 175 regions
- JPMorgan Chase: new Apple Card issuer (replacing Goldman Sachs, transition through 2027). $20B+ in card balances transferred at $1B discount
- Goldman Sachs: outgoing Apple Card partner, still provides Apple Savings accounts
- Green Dot Bank: provides Apple Cash services (peer-to-peer transfers)
- Mastercard: payment network for Apple Card
- Klarna: BNPL partner integrated into Apple Pay (October 2024, expanded to in-store September 2025)
- No external payment orchestrator detected
- Yuno is listed as an official Apple Pay payment platform partner on Apple's developer documentation

**Apple Services ecosystem:**
- App Store: $24B+ estimated revenue (30% commission standard, 15% small business program, 17% reduced tier under new US guidelines)
- Apple Music: 78M subscribers (9% growth YoY)
- iCloud: bundled storage subscriptions across 175 regions
- Apple TV+: streaming service competing for global subscribers
- Apple Pay: $9.4B revenue contribution (3.4% of total Apple revenue)
- Apple Card: transitioning from Goldman Sachs to JPMorgan Chase

**Top 5 markets gap analysis:**

MARKET 1: United States (42.86% of revenue)
  Confirmed: Visa/MC/Amex/Discover, Apple Pay, Apple Card, Apple Cash, PayPal, Klarna, Affirm
  Missing: Venmo standalone, Cash App Pay, ACH direct debit
  Note: Strongest coverage. DMA-style external payment mandates now apply after US court ruling (May 2025).

MARKET 2: Europe (26.69% of revenue)
  Confirmed: Visa/MC, Apple Pay, carrier billing, iDEAL (NL), Bancontact (BE), BLIK (PL), PayPal
  Missing: Bizum (Spain), MB Way (Portugal), Twint (Switzerland), SEPA instant for subscriptions
  Note: DMA mandates alternative PSPs. 5% Core Technology Commission adds cost complexity.

MARKET 3: Greater China (15.48% of revenue)
  Confirmed: Visa/MC, UnionPay, Alipay, WeChat Pay, Apple Pay
  Missing: Limited gaps in China specifically; strong local method coverage
  Note: Revenue declining (3.85% YoY). Regulatory pressure and local competition (Huawei, Xiaomi ecosystems).

MARKET 4: Japan (6.90% of revenue)
  Confirmed: Visa/MC/JCB, Apple Pay (Suica/PASMO), carrier billing (Docomo, SoftBank, au)
  Missing: Konbini, PayPay (dominant QR wallet), LINE Pay
  Note: Low credit card usage among younger demographics. Konbini cash payments remain significant.

MARKET 5: Rest of Asia Pacific (8.10% of revenue)
  Confirmed: Visa/MC, Apple Pay (select markets), GoPay, DANA, kakaopay, Naver Pay
  Missing: UPI (India), GCash (Philippines), ShopeePay, GrabPay, TrueMoney (Thailand)
  Note: India expansion critical. Apple Pay expected to launch in India mid-2026. UPI processes 10B+ transactions monthly.

MARKET 6 (Emerging): Latin America
  Confirmed: Visa/MC, carrier billing (Mexico), Apple Pay (Brazil, Mexico, Colombia, Chile, and others)
  Missing: Pix (Brazil), OXXO (Mexico), SPEI (Mexico), PSE (Colombia), Nequi (Colombia), Mercado Pago
  Note: Pix overtook credit cards in Brazil (42% of e-commerce in 2025). OXXO does not accept Apple Pay.

MARKET 7 (Emerging): Africa
  Confirmed: Limited. Apple Pay available in South Africa, Israel
  Missing: M-Pesa (Kenya, Tanzania, 50M+ users), Airtel Money, MTN Mobile Money, Flutterwave, Paystack
  Note: Apple expanding services to African countries. Mobile money is the dominant payment rail; card penetration under 10% in most markets.

**Payment outage history:**
- May 16, 2025: Major global outage affecting Apple Pay, Apple Cash, Apple Card, and Wallet. 3,000+ reports in first hour. 9% of US users affected, ~600 UK users. "Account services unavailable" errors across all Apple payment platforms
- January 29, 2025: Mastercard integration issue prevented card additions to Apple Pay (~1 hour)
- January 2025: Apple Cash crashed for hours affecting peer-to-peer transfers
- June 2024: Hungary central bank ordered reimbursement for 780,000 erroneous Apple Pay charges totaling $5.43M in one night
- Multiple smaller outages documented on Apple System Status page throughout 2024-2025

**Regulatory and DMA developments:**
- March 2024: EU Commission investigation into Apple's payment steering
- April 2025: EU found Apple in breach of DMA obligations, $580M fine
- May 2025: Apple updated US App Store guidelines allowing external payment links (Epic v. Apple ruling)
- June 2025: Apple introduced Core Technology Commission (5% on all digital goods sales) replacing Core Technology Fee
- January 2026: Transition to single EU business model with CTC across App Store, Web Distribution, and alternative marketplaces
- Fortnite returned to iOS with external payments (May 2025)

**Key meeting angles:**
1. **CEO transition window** | John Ternus taking over from Tim Cook creates strategic review moment. New leadership may reassess payment infrastructure and vendor relationships
2. **DMA multi-PSP mandate** | EU now requires alternative payment systems. Apple needs orchestration to manage multiple PSPs, commissions, and compliance across marketplaces
3. **$109B services engine** | Services grew 13.5% to all-time high. Protecting subscription renewal rates across 1B+ subscriptions is existential. Smart routing and failover directly protect this revenue
4. **Emerging market expansion** | Apple pivoting to India, Southeast Asia, Africa for growth. These markets require local payment methods (UPI, GCash, M-Pesa) that Apple's current infrastructure does not fully support
5. **Outage resilience** | May 2025 global outage exposed single-point-of-failure risk. Payment orchestration with automatic failover eliminates this vulnerability
6. **Goldman to Chase transition** | Apple Card moving to JPMorgan Chase over 24 months creates payment infrastructure complexity. Orchestration simplifies multi-issuer management
7. **Yuno is already an Apple Pay partner** | Yuno is listed on Apple's official payment platforms page, establishing existing trust and technical compatibility

**Subscription churn and billing recovery:**
- Failed card payments cost subscription businesses $129B+ in 2025 (Recurly)
- Involuntary churn accounts for 20-40% of all subscription churn
- Apple's Billing Grace Period feature recovers 15-20% more subscriptions
- Average chargeback values surged 48% YoY to $361.31 in Q1 2025
- Yuno reference: InDrive achieved 4.5%+ transaction recovery rate; Livelo saw +5% approval rate and 50% transaction recovery

**Sources:**
- [Apple Newsroom: Chase Apple Card](https://www.apple.com/newsroom/2026/01/chase-to-become-new-issuer-of-apple-card/)
- [Apple Newsroom: CEO Transition](https://www.apple.com/newsroom/2026/04/tim-cook-to-become-apple-executive-chairman-john-ternus-to-become-apple-ceo/)
- [Apple Newsroom: DMA Impacts](https://www.apple.com/newsroom/2025/09/the-digital-markets-acts-impacts-on-eu-users/)
- [Apple Newsroom: App Store Fraud Prevention](https://www.apple.com/newsroom/2025/05/the-app-store-prevented-more-than-9-billion-usd-in-fraudulent-transactions/)
- [Apple Developer: Payment Platforms](https://developer.apple.com/apple-pay/payment-platforms/)
- [Apple Developer: In-App Purchase](https://developer.apple.com/in-app-purchase/)
- [Apple Developer: Reducing Involuntary Churn](https://developer.apple.com/documentation/storekit/reducing-involuntary-subscriber-churn)
- [Apple Support: Payment Methods](https://support.apple.com/en-us/111741)
- [Apple Support: Apple Pay Countries](https://support.apple.com/en-us/102775)
- [Apple Cash Terms: Green Dot](https://applecash.greendot.com/termsconditions/)
- [JPMorgan Chase: Apple Card Issuer](https://www.jpmorganchase.com/ir/news/2026/chase-to-become-new-issuer-of-apple-card/)
- [CNBC: Apple Pay Outage May 2025](https://www.cnbc.com/2025/05/16/apple-pay-outage.html)
- [9to5Mac: Apple Pay Outage](https://9to5mac.com/2025/05/16/apple-pay-and-apple-cash-are-down-for-many-iphone-users/)
- [PYMNTS: Apple Pay Fraud Prevention](https://www.pymnts.com/apple/2025/apple-pay-and-apple-wallet-gain-users-and-add-capabilities)
- [Crowdfund Insider: Jennifer Bailey VP](https://www.crowdfundinsider.com/2025/10/255101-apple-pay-vp-jennifer-bailey-talks-wallet-more/)
- [Klarna: Apple Pay Integration](https://www.klarna.com/international/press/klarna-payment-options-now-available-at-checkout-on-apple-pay-in-app-and-online/)
- [Payments Dive: Apple Klarna BNPL](https://www.paymentsdive.com/news/apple-pay-klarna-bnpl-checkout-payment-expansion/730249/)
- [Bullfincher: Apple Revenue by Geography](https://bullfincher.io/companies/apple/revenue-by-geography)
- [Bullfincher: Apple Revenue by Segment](https://bullfincher.io/companies/apple/revenue-by-segment)
- [Business of Apps: Apple Statistics](https://www.businessofapps.com/data/apple-statistics/)
- [Chargebacks911: Apple Pay Statistics](https://chargebacks911.com/apple-pay-statistics/)
- [CoinLaw: Apple Pay Statistics](https://coinlaw.io/apple-pay-statistics/)
- [Recurly: Failed Payments $129B](https://recurly.com/press/failed-payments-could-cost-subscription-companies-more-than-129-billion-in-2025-us/)
- [Adapty: Stripe In-App Purchases](https://adapty.io/blog/can-you-use-stripe-for-in-app-purchases/)
- [RevenueCAT: Apple DMA EU Update](https://www.revenuecat.com/blog/growth/apple-eu-dma-update-june-2025/)
- [Similarweb: apple.com](https://www.similarweb.com/website/apple.com/)
- [Karmactive: Apple Pay Outage](https://www.karmactive.com/apple-pay-global-outage-hits-3000-users-as-53-of-americans-rely-on-digital-wallets/)
- [GR4VY: Apple Pay Orchestration](https://gr4vy.com/posts/apple-pay-for-businesses-how-payment-orchestration-enhances-transactions/)
- [Yuno: Local Payment Methods](https://y.uno/post/how-to-offer-the-right-local-payment-methods-in-new-markets)
