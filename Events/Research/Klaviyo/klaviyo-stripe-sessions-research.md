# KLAVIYO | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: KLAVIYO
=======================================

Logo: https://brandfetch.com/klaviyo.com
Nombre merchant: KLAVIYO

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Merchant Payment Blindspot
Tittle_Pain Point_2: Cross Border Cart Drops
Tittle_Pain Point_3: Platform Dependency Risk
Tittle_Pain Point_4: No Checkout Optimization
Tittle_Pain Point_5: Multi PSP Data Silos

Desc_Pain Point_1: Klaviyo powers marketing for 193,000+ ecommerce brands across 80+ countries, but has zero control over how those brands process payments. Merchants on Shopify use Stripe, BigCommerce uses Braintree, WooCommerce uses dozens of gateways. Klaviyo sees abandoned carts but cannot influence whether the underlying payment succeeds or fails.
Desc_Pain Point_2: 35% of Klaviyo's revenue now comes from EMEA and APAC merchants, growing 43% YoY. These merchants sell cross border, but checkout conversion depends entirely on their ecommerce platform's payment stack. A German merchant selling to Brazil has no Pix option. A UK merchant selling to the Netherlands has no iDEAL. Klaviyo tracks the abandonment but cannot fix the cause.
Desc_Pain Point_3: Klaviyo's deepest integration is with Shopify, which uses Stripe as its sole payment infrastructure for Shopify Payments. If Stripe has an outage or declines a transaction, Klaviyo's abandoned cart flows trigger after the sale is already lost. Klaviyo's $1.23B revenue depends on merchant GMV it cannot protect at the payment layer.
Desc_Pain Point_4: Klaviyo abandoned cart flows generate $3.65 revenue per recipient on average, but this is recovery after failure. The platform lacks any mechanism to optimize checkout before abandonment happens: no smart routing, no payment method localization, no acquirer failover. Klaviyo optimizes the email after the sale is lost, not the payment before it fails.
Desc_Pain Point_5: Klaviyo integrates with Stripe, Chargebee, Recurly, Recharge, and other billing platforms, each feeding separate payment event data. A merchant using Stripe for cards and PayPal for wallets sends fragmented data to Klaviyo. No unified payment layer means incomplete customer profiles, inaccurate LTV calculations, and broken attribution.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (primary via Shopify Payments)
PSP_2: Braintree/PayPal (BigCommerce default)
PSP_3: Adyen (enterprise merchant choice)
PSP_4: Chargebee (subscription billing)
PSP_5: Recurly (subscription billing)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix (Brazil)
Local_M_2: iDEAL (Netherlands)
Local_M_3: Bancontact (Belgium)
Local_M_4: SEPA Direct Debit (EU)
Local_M_5: Klarna (EU/US BNPL)
Local_M_6: Boleto (Brazil)
Local_M_7: OXXO (Mexico)
Local_M_8: Mada (Saudi Arabia)
Local_M_9: GrabPay (SEA)
Local_M_10: Mercado Pago (LATAM)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing Engine
Tittle_Yuno_Cap2: Failover Cascade Retries
Tittle_Yuno_Cap3: 1,000+ Payment Methods
Tittle_Yuno_Cap4: Unified Data Orchestration

Desc_Yuno_Cap1: Route every transaction to the optimal acquirer by card BIN, currency, and destination country in real time. With 193,000+ merchants across 80+ countries depending on Klaviyo for revenue growth, even a 3% authorization uplift on cross border volumes translates to millions in recovered GMV. Smart Routing selects the best processor per transaction instead of static gateway assignments on Shopify, BigCommerce, or WooCommerce.
Desc_Yuno_Cap2: When Stripe declines a card or Braintree returns a soft decline, Yuno cascades to the next best processor in milliseconds. Klaviyo's abandoned cart flows currently activate after the payment fails. With Yuno, the payment retries through an alternative route before the customer ever sees a decline. Fewer failed payments means fewer abandoned cart triggers and higher checkout conversion for Klaviyo merchants.
Desc_Yuno_Cap3: One API activates Pix for Brazil, iDEAL for the Netherlands, Bancontact for Belgium, SEPA for Europe, Klarna and Afterpay for BNPL, OXXO for Mexico, Mada for Saudi Arabia, GrabPay across SEA, and Mercado Pago for LATAM. Yuno connects 1,000+ local payment methods across 40+ countries. Klaviyo's EMEA and APAC merchants get instant local payment access, reducing the cart abandonment that drives their recovery flows today.
Desc_Yuno_Cap4: Replace fragmented payment data from Stripe, Braintree, Chargebee, Recurly, and PayPal with a single orchestration layer that feeds unified transaction events to Klaviyo. Every payment attempt, approval, decline, and retry flows through one integration. Klaviyo gets complete customer payment profiles: accurate LTV, precise attribution, and real time payment status. One data source instead of five, powering smarter segmentation and higher performing flows.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**KLAVIYO at a glance:**
- Founded: 2012 in Boston by Andrew Bialecki (Co-Founder & Co-CEO) and Ed Hallen (Co-Founder)
- Headquarters: Boston, Massachusetts
- Co-CEOs: Andrew Bialecki (product & AI vision) and Chano Fernandez (GTM & operations, appointed January 2026)
- Revenue: $1.23B (FY 2025, 32% YoY growth); Q4 2025: $350.2M (30% YoY)
- FY 2026 outlook raised
- IPO: NYSE under ticker KVYO (September 2023)
- 193,000+ paying customers across 80+ countries
- ~2,844 employees (as of Feb 2026)
- 350+ pre-built integrations
- Net revenue retention rate: 110%
- Positioned as autonomous B2C CRM and AI marketing platform
- Products: Email, SMS, RCS, WhatsApp, Mobile Push, Reviews, Customer Hub, Marketing Analytics, Klaviyo Data Platform
- SMS available in 19 countries across North America, EMEA, and APAC
- Platform supports 7 languages

**International expansion metrics:**
- EMEA and APAC: 35% of total revenue, growing 43% YoY (Q3 2025)
- Brands using Klaviyo and Shopify together: 73% revenue growth over 3 years
- Dublin office opened in 2024 for European expansion
- Germany, China, and US are top adoption markets
- Deepened Shopify Markets integration (March 2026) for Locale Aware Catalogs

**Confirmed PSPs and payment integration partners (via merchant ecommerce platforms):**

| Provider | Role | Context |
|----------|------|---------|
| Stripe | Primary payment data integration; powers Shopify Payments | Core Shopify ecosystem |
| Braintree/PayPal | Default gateway for BigCommerce merchants | BigCommerce ecosystem |
| Adyen | Enterprise merchant choice across platforms | Multi-platform |
| Chargebee | Subscription billing integration (trials, renewals, failed payments) | SaaS/subscription merchants |
| Recurly | Subscription billing integration | SaaS/subscription merchants |
| Recharge | Subscription management for Shopify | Shopify subscriptions |
| Mollie | European payment gateway (WooCommerce, Wix, BigCommerce, Magento, Shopify, SFCC) | European merchants |
| Square | POS and online payments | Square Online merchants |

**Key observation:** Klaviyo does NOT process payments itself. It is a marketing automation and CRM platform that ingests payment event data from merchant ecommerce platforms and PSPs. Klaviyo's revenue depends entirely on merchant GMV generated through third-party payment infrastructure.

**Abandoned cart flow performance:**
- Average RPR (revenue per recipient): $3.65
- Top 10% of brands: $28.89 RPR
- Flows trigger after checkout abandonment, not before payment failure
- Cross-device tracking is a known gap (different devices = different profiles)

**Competitive landscape:**
- Primary competitors: Braze, HubSpot, Mailchimp (Intuit), Attentive, Postscript
- Klaviyo's moat: deep ecommerce data integration + AI-powered segmentation
- Key risk: AI-native competitors replicating Klaviyo's context through APIs

**Key meeting angles:**
1. **Platform-level impact** | Klaviyo touches 193,000+ merchant payment flows. An orchestration layer for Klaviyo's merchant ecosystem would improve checkout conversion across every brand, directly increasing the GMV that powers Klaviyo's revenue model
2. **Abandoned cart root cause** | Klaviyo's highest-value automated flows (abandoned cart, failed payment) exist because payments fail. Smart Routing and Failover reduce the failures that trigger those flows. Less abandonment = higher merchant GMV = higher Klaviyo retention
3. **Cross border blind spot** | 35% of revenue from EMEA/APAC merchants selling globally, but payment method coverage depends entirely on the ecommerce platform. Yuno's 1,000+ APMs fill the gap at checkout, where Klaviyo cannot reach
4. **Unified payment data** | Merchants feed Klaviyo fragmented data from Stripe, Braintree, Chargebee, and others. An orchestration layer normalizes payment events into a single stream, giving Klaviyo cleaner data for segmentation, attribution, and LTV
5. **Shopify dependency** | Shopify is Klaviyo's largest channel. Shopify Payments runs exclusively on Stripe. Any Stripe disruption cascades through Klaviyo's merchant base. Orchestration adds resilience and routing alternatives
6. **$1.23B revenue at stake** | Klaviyo monetizes on active profiles and usage, both of which correlate with merchant transaction volume. Higher checkout conversion = more transactions = more customer profiles = more Klaviyo revenue

**Sources:**
- [Klaviyo FY2025 Earnings (BusinessWire)](https://www.businesswire.com/news/home/20260210069244/en/Klaviyo-Delivers-Outstanding-2025-Results-32-Revenue-Growth-Record-Fourth-Quarter-and-Raised-Fiscal-Year-2026-Outlook)
- [Klaviyo Investor Relations](https://investors.klaviyo.com/news/news-details/2026/Klaviyo-Delivers-Outstanding-2025-Results-32-Revenue-Growth-Record-Fourth-Quarter-and-Raised-Fiscal-Year-2026-Outlook/default.aspx)
- [Klaviyo Appoints Co-CEO Chano Fernandez (BusinessWire)](https://www.businesswire.com/news/home/20251209387836/en/Klaviyo-Appoints-Chano-Fernndez-as-co-CEO-Joining-Co-Founder-and-co-CEO-Andrew-Bialecki)
- [Klaviyo + Shopify Deepen Integration (March 2026)](https://www.klaviyo.com/newsroom/klaviyo-shopify-integration)
- [Klaviyo Boosts EMEA Growth (CMOTech)](https://cmotech.uk/story/klaviyo-boosts-emea-growth-names-europe-based-co-ceo)
- [Klaviyo Q1 2025 Revenue Growth (Investing.com)](https://www.investing.com/news/company-news/klaviyo-q1-2025-slides-revenue-jumps-33-international-expansion-accelerates-93CH-4026021)
- [Klaviyo ARR Learnings (SaaStr)](https://www.saastr.com/5-interesting-learnings-from-klaviyo-at-1-2-billion-in-arr/)
- [Klaviyo Stripe Integration (Help Center)](https://help.klaviyo.com/hc/en-us/articles/115005082267)
- [Klaviyo Ecommerce Integrations (Help Center)](https://help.klaviyo.com/hc/en-us/articles/360020698171)
- [Klaviyo Abandoned Cart Flow (Help Center)](https://help.klaviyo.com/hc/en-us/articles/115002779411)
- [Klaviyo Billing (Help Center)](https://help.klaviyo.com/hc/en-us/articles/115000976672)
- [Klaviyo + Mollie Integration](https://www.mollie.com/integrations/klaviyo)
- [Klaviyo on Tracxn](https://tracxn.com/d/companies/klaviyo/__a3CbbINSRMVrdfW-jgtWtBmw5pTden8hW7uXPkbmnQw)
- [Klaviyo Revenue (StockAnalysis)](https://stockanalysis.com/stocks/kvyo/revenue/)
- [Klaviyo Logo (Brandfetch)](https://brandfetch.com/klaviyo.com)
