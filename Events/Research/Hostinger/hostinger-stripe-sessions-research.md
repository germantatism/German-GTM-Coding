# HOSTINGER | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Hostinger
═══════════════════════════════════════

Logo: https://upload.wikimedia.org/wikipedia/commons/8/82/Hostinger_logo_black.svg
Nombre merchant: Hostinger

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Fragmented PSP Sprawl
Tittle_Pain Point_2: No Routing Intelligence
Tittle_Pain Point_3: 3DS Auth Drop-Off
Tittle_Pain Point_4: Renewal Churn at Scale
Tittle_Pain Point_5: Emerging Market Gaps

Desc_Pain Point_1: Multiple payment processors across 150+ countries with no unified orchestration layer. Each PSP integration managed separately, creating reconciliation overhead and inconsistent auth rates across regions.
Desc_Pain Point_2: 4.6M customers in 150+ countries but no smart routing to direct each transaction to the best-performing acquirer. A Brazilian Pix payment and a German Klarna payment follow static paths with no real-time optimization.
Desc_Pain Point_3: European customers face "3D Secure Verification Failed" errors frequently enough for Hostinger to maintain a dedicated support article. SCA-triggered session timeouts kill conversions at checkout.
Desc_Pain Point_4: Hosting plans are 1-4 year prepaid subscriptions. Each renewal is a high-value transaction. Failed renewal = lost customer for years. With 4.6M customers and 35% annual growth, renewal volume compounds fast.
Desc_Pain Point_5: Top markets include India, Brazil, Indonesia, Pakistan, and Nigeria. Despite offering some local APMs, key gaps remain: no GCash (Philippines), no Dana (Indonesia), no Easypaisa (Pakistan), no M-Pesa (Africa).

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (Website Builder payments)
PSP_2: PayPal
PSP_3: Cryptocurrency processor
PSP_4: Local PSP (LATAM: Pix, Boleto, OXXO, SPEI)
PSP_5: Local PSP (Asia: UPI, QRIS, OVO, JazzCash)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: GCash
Local_M_2: Dana
Local_M_3: Easypaisa
Local_M_4: M-Pesa
Local_M_5: SEPA Direct Debit
Local_M_6: GrabPay
Local_M_7: KakaoPay
Local_M_8: PromptPay
Local_M_9: Mercado Pago
Local_M_10: MoMo

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each transaction to the highest-performing acquirer by payment method, BIN, and country. With 4.6M customers across 150+ markets and high-value prepaid renewals, even a 3% auth uplift on EUR 275M+ revenue recovers EUR 8M+ annually without a single new sign-up.
Desc_Yuno_Cap2: Automatic cascade across Hostinger's multiple PSPs. When one processor declines a renewal, Yuno reroutes to the next best acquirer in milliseconds, turning failed prepaid renewals into recovered multi-year customers. Up to 50% recovery on soft declines.
Desc_Yuno_Cap3: Fills the remaining APM gaps in Hostinger's top growth markets: GCash in Philippines, Dana in Indonesia, M-Pesa in Africa, GrabPay in Southeast Asia, SEPA DD in Europe. One API, 1,000+ payment methods. Plug gaps without new integrations.
Desc_Yuno_Cap4: One dashboard replacing Hostinger's fragmented multi-PSP setup across 150+ countries. Real-time approval rate monitoring per market, centralized reconciliation across all processors and payment methods, millisecond anomaly detection via Monitors.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Hostinger at a glance:**
- Web hosting and website builder platform, founded 2004 in Kaunas, Lithuania
- HQ: Vilnius, Lithuania ("Cyber City" campus). ~1,000 employees, hiring 200-300 more in 2026
- Revenue: EUR 275.4M (2025), up 51% YoY. Fourth consecutive year of 50%+ growth
- 4.6M customers across 150+ countries, growing 35% annually
- Ranked 2nd in Financial Times "Long-term Growth Champions: Europe 2026"
- Private, profitable, never raised traditional VC. No IPO plans (dividend recapitalization in Nov 2025)
- Key products: Shared Hosting, Cloud Hosting, VPS, WordPress Hosting, Website Builder, Hostinger Horizons (AI app builder, 800K+ users), Hostinger Reach (AI email marketing, 150K users)
- 13 data centers across Asia, Europe, North and South America
- CEO: Not publicly named in search results

**Top 10 markets by users:** India, Brazil, USA, Indonesia, France, Pakistan, UK, Spain, Mexico, Colombia

**Confirmed PSPs and payment methods (comprehensive):**
- Cards: Visa, Mastercard, Amex, Discover, JCB, Diners Club, Maestro, RuPay (India), UnionPay (HK), Carnet (Mexico)
- Wallets: PayPal, Apple Pay, Google Pay, AliPay
- Germany: Klarna
- Poland: BLIK
- Brazil: Pix, Boleto Bancario, Nubank (installments up to 12 months)
- Mexico: OXXO, SPEI (installments 3-12 months)
- India: UPI
- Indonesia: Bank Transfer (BCA, Mandiri, BRI, BNI), OVO, QRIS
- Pakistan: JazzCash
- Nigeria: OPay
- Egypt/UAE: Fawry
- Philippines: Globe Cash
- Lithuania: PaySera
- Argentina/Colombia: Local installment cards
- Crypto: Multiple cryptocurrencies accepted
- PCI-DSS Level 1 compliant

**Top 5 Markets Gap Analysis:**

MARKET 1: India (#1 market by users)
  Accepted: Cards, RuPay, UPI, PayPal
  Missing: Paytm, PhonePe, Net Banking
  Note: Well served with UPI. Room for wallet expansion

MARKET 2: Brazil (#2 market)
  Accepted: Cards, Pix, Boleto, Nubank, PayPal, installments
  Missing: Mercado Pago, PicPay
  Note: Strong local coverage. Installments are key differentiator

MARKET 3: Indonesia (#4 market)
  Accepted: Cards, Bank Transfer, OVO, QRIS, PayPal
  Missing: Dana, GoPay, ShopeePay, LinkAja
  Note: QRIS covers some wallets but direct integrations would improve UX

MARKET 4: Pakistan (#6 market)
  Accepted: Cards, JazzCash
  Missing: Easypaisa, bank transfer, SadaPay
  Note: Only 6% card penetration. JazzCash helps but Easypaisa has comparable reach

MARKET 5: Nigeria (#significant African market)
  Accepted: Cards, OPay
  Missing: Paystack, Flutterwave, bank transfer, USSD
  Note: Low card penetration. OPay is good start but more methods needed

**Payment incident history:**
- October 2025: Service disruption affecting payments (linked to AWS outage)
- Dedicated support article for "3D Secure Verification Failed" errors
- Payment processing delays documented (up to 24 hours for some gateways)

**Key meeting angles:**
1. **Orchestration over integration** | Hostinger already has 20+ payment methods across 150+ countries but lacks unified routing intelligence
2. **Prepaid renewal economics** | 1-4 year hosting plans mean each renewal is worth $48-$576. Failed renewal = years of lost revenue
3. **50%+ growth compounding** | 35% customer growth means renewal volume doubles every 2 years. Payment infrastructure must scale
4. **Emerging market dominance** | Top markets are India, Brazil, Indonesia, Pakistan. These are Yuno's strongest markets for APM coverage
5. **3DS drop-off** | European SCA compliance causing measurable checkout abandonment. Smart 3DS routing would reduce friction
6. **No orchestration layer** | Multiple PSPs, multiple APMs, but no intelligent routing between them. Classic orchestration use case

**Sources:**
- [Hostinger Payment Methods](https://www.hostinger.com/payments)
- [Hostinger Payment Methods by Region (Support)](https://www.hostinger.com/support/1583236-what-payment-methods-are-available-at-hostinger/)
- [Hostinger Financial Results 2025](https://www.hostinger.com/blog/financial-results-2025)
- [Hostinger 51% Revenue Growth](https://webhosting.today/2026/02/18/hostinger-reports-51-revenue-growth-in-2025-reaches-e275-4-million/)
- [Hostinger FT Long-term Growth Champions](https://www.hostinger.com/blog/long-term-champions-ft)
- [Hostinger Payment Issues Support](https://www.hostinger.com/support/billing/issues-with-payment/)
- [Hostinger 3DS Error Support](https://support.hostinger.com/en/articles/5402772-3d-secure-verification-failed-error-while-making-a-payment)
- [Hostinger October 2025 Payment Outage](https://isdown.app/status/hostinger/incidents/460851-payment-processing-service-disruption)
- [Hostinger Wikipedia](https://en.wikipedia.org/wiki/Hostinger)
- [Hostinger Employee Stock Options Payout](https://webhosting.today/2026/03/18/hostinger-pays-out-e11-8-million-in-employee-stock-options-and-the-numbers-behind-it-tell-a-bigger-story/)
- [Hostinger Product Updates 2026](https://www.hostinger.com/blog/product-updates-2026)
