# WIX.COM | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
════════════════��══════════════════════
DATABASE FIELDS: Wix.com
═════════════════════���═════════════════

Logo: https://upload.wikimedia.org/wikipedia/commons/7/76/Wix.com_website_logo.svg
Nombre merchant: Wix.com

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Stripe Single-Rail Lock
Tittle_Pain Point_2: LATAM/APAC APM Blindspot
Tittle_Pain Point_3: Merchant Conversion Leak
Tittle_Pain Point_4: Cross-Border Card Declines
Tittle_Pain Point_5: Subscription Renewal Churn

Desc_Pain Point_1: Wix Payments is a Stripe white-label in 17+ countries. 100% of card volume through one acquirer, no failover. Stripe decline = lost sale for merchant and lost fee for Wix.
Desc_Pain Point_2: 8.5M live sites in 190+ countries but Wix Payments covers 17 markets. SEA, Africa, most of LATAM have no native solution. No OXXO, no M-Pesa, no Dana, no SPEI.
Desc_Pain Point_3: Merchants lose conversions when international shoppers lack local APMs. Brazil has Pix via MercadoPago, but Colombia, Mexico, Philippines have no local path.
Desc_Pain Point_4: International card declines are the top payment complaint. Banks flag cross-border transactions, 3D Secure adds friction, regional cards are rejected systematically.
Desc_Pain Point_5: 6.1M premium subscribers drive 65% of $1.99B revenue. Failed renewals have no multi-acquirer retry. Wix retries via Stripe only; unrecovered declines are lost forever.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (via Wix Payments)
PSP_2: PayPal
PSP_3: Stripe (direct connect)
PSP_4: MercadoPago (Brazil)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: OXXO
Local_M_2: PSE
Local_M_3: SPEI
Local_M_4: Nequi
Local_M_5: M-Pesa
Local_M_6: Dana
Local_M_7: GrabPay
Local_M_8: TrueMoney
Local_M_9: Fawry
Local_M_10: Bizum

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across Stripe and any additional acquirer based on card BIN, issuer, and geography. With $1.99B in revenue, 6.1M premium subscribers, and billions in merchant GMV, even a 3% auth uplift across Wix Payments recovers tens of millions in annual revenue for both merchants and the platform.
Desc_Yuno_Cap2: Automatic cascade when Stripe declines a card. Yuno reroutes to the next best acquirer in milliseconds, turning failed merchant checkouts and platform renewals into recovered revenue. Up to 50% recovery on soft declines, directly reducing involuntary churn on the 6.1M subscriber base that drives 65% of revenue.
Desc_Yuno_Cap3: Activates APMs beyond Wix Payments' 17-country footprint: OXXO and SPEI in Mexico, PSE and Nequi in Colombia, M-Pesa in Kenya, Dana in Indonesia, GrabPay in SEA, TrueMoney in Thailand, Fawry in Egypt. One API, 1,000+ payment methods. Merchants sell globally without per-market integrations.
Desc_Yuno_Cap4: One dashboard replacing Wix's fragmented Stripe + PayPal + MercadoPago + 80+ third-party provider ecosystem. Real-time approval rate monitoring, centralized reconciliation across all commerce and subscription revenue streams, millisecond anomaly detection via NOVA. 75% reduction in payment operations complexity.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Wix.com at a glance:**
- 304M+ registered users, 8.5M live websites, 6.1M premium subscribers, 190+ countries
- Revenue: $1.99B (FY2025), up 13.2% YoY. Q4 2025: $524M (up 14% YoY)
- 2026 guidance: mid-teens % growth on revenue and bookings. Free cash flow margin: low-to-mid 20% range
- Premium subscriptions: 65% of total revenue. International revenue: 53% of total
- North America: 43% of revenue. LATAM + SEA: 22% of new user acquisition
- Base44 (AI site builder): reached $100M ARR in first year post-launch
- CMS market share grew 32.6% YoY. Powers 4.3% of all websites globally
- Public company (NASDAQ: WIX). ~6,200 employees

**Confirmed PSPs:**
- Stripe: powers Wix Payments (white-label) across 17+ countries. Partnership since 2014, processing billions annually
- PayPal: secondary payment option across all markets
- Stripe (direct connect): merchants can also connect Stripe directly
- MercadoPago: Brazil-specific integration
- 80+ additional third-party payment providers available via marketplace
- No payment orchestrator detected

**Wix Payments (Stripe White-Label) Available In:**
- North America: US, Canada
- Europe: UK, Austria, Belgium, Finland, Germany, Italy, Lithuania, Netherlands, Portugal, Spain, Switzerland, Ireland
- APAC: planned expansion
- Brazil: separate "Wix Payments Brazil" offering via MercadoPago
- NOT available in most of LATAM, Africa, Middle East, or Southeast Asia

**Payment Methods Currently Accepted (via Wix Payments):**
- Cards: Visa, Mastercard, Amex, Discover, Diners Club, JCB, Maestro, UnionPay
- Wallets: Apple Pay, Google Pay, PayPal
- BNPL: Afterpay/Clearpay, Klarna, Affirm
- Bank: iDEAL (Netherlands), ACH (US)
- In-person: Tap to Pay on iPhone/Android
- Additional methods via 80+ third-party integrations (varies by country)

**Top Markets:**
- United States: ~1.1M Wix sites (13%), largest revenue market (43% of revenue from North America)
- United Kingdom: ~485K sites
- Brazil: ~232K sites (Wix Payments Brazil via MercadoPago)
- Germany: ~202K sites
- Canada: ~189K sites
- India: top 3 by traffic, 22% new user acquisition from LATAM + SEA

**Payment Issues Documented:**
- International card declines are top complaint in Wix community forums
- Banks flagging cross-border transactions as fraud
- 3D Secure authentication adding friction at checkout
- Merchants report customers unable to complete checkout due to missing country/region shipping rules
- Payment processing can take up to 40 days in some edge cases
- Wix Payments not available in most developing markets where new user growth is strongest

**Key Meeting Angles:**
1. **Platform scale**: Yuno orchestration improves payments for millions of Wix merchants simultaneously, multiplying revenue impact
2. **White-label precedent**: Wix already white-labels Stripe. Adding Yuno orchestration behind Wix Payments is architecturally aligned
3. **International revenue majority**: 53% of revenue from outside North America, but Wix Payments only covers 17 countries
4. **LATAM + SEA growth engine**: 22% of new users from these regions, yet payment infrastructure lags behind acquisition
5. **Subscription economics**: 6.1M premium subscribers, 65% of revenue. Every failed renewal compounds. Multi-acquirer failover protects the base
6. **Merchant enablement**: Adding OXXO, PSE, M-Pesa to Wix stores unlocks buyer segments, increasing GMV and Wix take rate
7. **Stripe EMEA expansion**: Wix just expanded Stripe white-label to 11 EMEA countries. Yuno can accelerate further expansion

**Sources:**
- [Wix Design Assets & Guidelines](https://www.wix.com/about/design-assets)
- [Wix: About Wix Payments](https://support.wix.com/en/article/about-wix-payments)
- [Wix: Available Payment Providers by Country](https://support.wix.com/en/article/available-payment-providers-in-your-country)
- [Wix: Accepting Payments Overview](https://support.wix.com/en/article/accepting-payments-an-overview)
- [Wix: Troubleshooting Issues for Accepting Payments](https://support.wix.com/en/article/troubleshooting-issues-for-accepting-payments)
- [Wix: Transaction Declined Reasons](https://support.wix.com/en/article/wix-payments-transaction-declined)
- [Wix: Connecting Stripe as a Payment Provider](https://support.wix.com/en/article/connecting-stripe-as-a-payment-provider)
- [Stripe: Wix Payments Grows EMEA Coverage](https://stripe.com/customers/wix-announcement)
- [Stripe: Wix Partnership Expansion](https://stripe.com/newsroom/stories/wix-and-stripe)
- [Embedded Finance Review: Wix Expands White-Label Payments](https://www.embeddedfinancereview.com/wix-expands-white-label-payments-to-11-emea-countries-with-stripe/)
- [Wix FY2025 Financial Results](https://www.wix.com/press-room/home/post/wix-reports-fourth-quarter-and-full-year-2025-results)
- [GlobeNewsWire: Wix FY2025 Results](https://www.globenewswire.com/news-release/2026/03/04/3249040/0/en/Wix-Reports-Fourth-Quarter-and-Full-Year-2025-Results.html)
- [WiserReview: Wix Statistics 2026](https://wiserreview.com/blog/wix-statistics/)
- [MageComp: Wix Statistics 2026](https://magecomp.com/blog/wix-statistics/)
- [Colorlib: Wix Statistics 2026](https://colorlib.com/wp/wix-statistics/)
- [Wikimedia: Wix.com Logo](https://commons.wikimedia.org/wiki/File:Wix.com_website_logo.svg)
