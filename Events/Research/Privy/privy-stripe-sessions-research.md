# PRIVY | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Privy
=======================================

Logo: https://asset.brandfetch.io/iddT6Fxmxo/idCvGYBqoU.svg
Nombre merchant: Privy

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Cards-Only Billing Wall
Tittle_Pain Point_2: USD-Only Pricing
Tittle_Pain Point_3: No Local APMs for SMBs
Tittle_Pain Point_4: Single Acquirer Exposure
Tittle_Pain Point_5: Merchant Checkout Gaps

Desc_Pain Point_1: Privy accepts only Visa, Mastercard, Amex, and Discover via Stripe, plus Shopify billing. No PayPal, no bank debit, no digital wallets. Merchants in 180 countries who prefer local methods must use a US credit card or route through Shopify billing.
Desc_Pain Point_2: Privy bills exclusively in USD. Merchants in Europe, LATAM, Asia, and the Middle East absorb FX markup on every monthly charge. For a $30/mo Starter plan, the real cost can be 3-5% higher in local currency, creating churn risk among price-sensitive SMBs.
Desc_Pain Point_3: Privy's 100K+ merchants operate in 180 countries, many selling to consumers who prefer local payment methods. Yet the marketing platform itself has no framework for helping merchants optimize their checkout with Pix, UPI, or SEPA DD through Privy-powered flows.
Desc_Pain Point_4: Stripe processes all non-Shopify credit card payments. Any Stripe outage blocks signups and renewals for the entire non-Shopify merchant base. No secondary processor exists to catch failed charges or cascade retries.
Desc_Pain Point_5: Privy drives $10B+ in merchant sales via popups, email, and SMS, but the merchants' own checkout pages often lack local APMs. Privy could deepen its value prop by helping merchants accept local methods through integrated payment orchestration.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (credit card processor)
PSP_2: Shopify Billing (Shopify merchants)
PSP_3: (none detected)
PSP_4: (none detected)
PSP_5: (none detected)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: SEPA Direct Debit
Local_M_2: Pix
Local_M_3: UPI
Local_M_4: iDEAL
Local_M_5: BLIK
Local_M_6: Bancontact
Local_M_7: Boleto
Local_M_8: OXXO
Local_M_9: Giropay
Local_M_10: PayPal

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route every merchant subscription charge to the best performing acquirer per card BIN, country, and issuer. With 100K+ merchants in 180 countries, a 3-10% auth uplift on monthly subscription renewals recovers significant revenue and reduces involuntary churn across the entire merchant base.
Desc_Yuno_Cap2: When Stripe declines a merchant's subscription renewal, Yuno cascades to an alternate acquirer in milliseconds. Recovers up to 50% of failed charges, keeping paying merchants active and protecting recurring revenue that funds Privy's acquisition-driven growth strategy.
Desc_Yuno_Cap3: Unlocks local payment methods for Privy's own billing and for its merchants' checkout flows: SEPA DD in Europe, Pix in Brazil, UPI in India, iDEAL in Netherlands, BLIK in Poland. One API, 1,000+ payment methods. Becomes a differentiator for Privy vs. Klaviyo and Mailchimp.
Desc_Yuno_Cap4: Single dashboard consolidating Stripe and Shopify billing into one view. Real-time monitoring of subscription success rates across 180 countries, centralized reconciliation for all merchant billing, and NOVA provides millisecond anomaly detection across both payment channels.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Privy at a glance:**
- Founded: 2011 in Boston, MA (originally as local marketing startup, pivoted to ecommerce)
- Founder: Ben Jabbawy (Founding CEO, now investor)
- Current CEO: Alex Persson (joined 2023 post-divestment from Attentive)
- CTO: Spencer Norman
- VP of Sales: Craig Langan
- VP of Marketing: Katie Samuelson
- Investors: Canaan Partners (CRV), Stripes, 500 Startups, Atlas Ventures; individual investor Mike Volpe (Founding CMO, HubSpot)
- Total funding raised: ~$10M+ (original Privy); acquired by Attentive for $120M (June 2021); divested from Attentive in 2023; now independent
- Revenue: Not publicly disclosed; estimated from 100K+ paying merchants at $30-100+/mo avg
- Merchants: 100K+ paying customers (previously reported as 500K+ including free); 180 countries
- Sales driven: $10B+ in ecommerce sales for merchants
- Employees: 80+
- App Store reviews: 19K+ five-star reviews; 4,800+ Shopify App Store reviews (#1 reviewed Email/SMS app)
- Products: Email Marketing, SMS Marketing, Onsite Displays (popups), Marketing Automation (Flows), Segmentation
- Platform integrations: Shopify, Shopify Plus, WooCommerce, BigCommerce, Squarespace, Weebly, Wix
- Acquisitions: Emotive (conversational SMS, 2025), Sendlane (email/SMS automation, Feb 2026)
- Combined platform: 10,000+ ecommerce brands post-Emotive merger

**Confirmed PSPs:**
- Stripe: Processes all credit card payments (Visa, Mastercard, Amex, Discover)
- Shopify Billing: Direct billing through Shopify merchant accounts for Shopify-installed apps
- No secondary card processor detected
- No payment orchestrator detected
- No PayPal, no digital wallets, no bank debit detected

**Billing details:**
- Payment methods: Credit cards (Visa, MC, Amex, Discover) via Stripe; Shopify billing
- Currency: USD only
- Billing cycle: Monthly (standard); Annual available (non-refundable)
- Contact-based auto-scaling: Billing adjusts automatically based on highest mailable/textable contact count per cycle
- Refund eligibility: 10 days from charge date; annual plans non-refundable
- Shopify billing may show split line items (base + usage)

**Pricing plans:**
- Free: Basic popups, up to 100 mailable contacts
- Convert: Onsite displays only (no email/SMS), syncs leads to external platforms
- Starter: From $30/month, unlimited email sends, email automation, welcome + abandoned cart flows
- Growth: Email + SMS, contact-based pricing, advanced segmentation
- Enterprise/Custom: Available for larger merchants
- Shopify App: From $24/mo for up to 10K monthly pageviews

**Key payment gaps identified:**
- Credit cards only (no PayPal, no wallets, no bank debit) for subscription billing
- USD-only billing creates FX drag for merchants in 179 non-US countries
- No local payment methods offered or recommended to merchants for their own checkout
- Single processor dependency (Stripe) for all non-Shopify billing
- 10-day refund window combined with auto-scaling creates billing surprise risk
- Competitors (Klaviyo, Mailchimp) accept broader payment methods and bill in local currencies

**Top Markets Gap Analysis:**

MARKET 1: United States (primary market)
  Offer: Visa/MC/Amex/Discover via Stripe, Shopify billing
  Missing: ACH Direct Debit, PayPal, Apple Pay
  Best-served market but still no bank debit option

MARKET 2: United Kingdom / Europe (Shopify merchants in EU)
  Offer: Visa/MC via Stripe (USD billing, FX markup)
  Missing: SEPA Direct Debit, GBP/EUR pricing, iDEAL, Bancontact
  European merchants pay FX on every monthly charge; no local currency

MARKET 3: Brazil (growing ecommerce market)
  Offer: Visa/MC via Stripe (USD billing, FX markup)
  Missing: Pix, Boleto, BRL pricing
  Brazilian Shopify merchants need Pix for their own customers and for SaaS subscriptions

MARKET 4: India (large Shopify merchant community)
  Offer: Visa/MC via Stripe (USD billing, FX markup)
  Missing: UPI, Netbanking, INR pricing
  UPI dominates Indian digital payments; no option for Indian merchants to pay via UPI

MARKET 5: Mexico / LATAM (Shopify expansion market)
  Offer: Visa/MC via Stripe (USD billing, FX markup)
  Missing: OXXO, SPEI, MXN pricing
  Cash-heavy markets where merchants may not have international credit cards

**Key meeting angles:**
1. **100K+ merchants in 180 countries, USD cards only**: Massive global footprint but minimal payment diversity. Adding SEPA DD, Pix, UPI at billing reduces churn among international merchants.
2. **Acquisition-driven growth**: Emotive + Sendlane acquisitions expand the platform. Payment orchestration is the logical next infrastructure layer to support a growing, diverse merchant base.
3. **$10B+ in merchant sales**: Privy drives massive checkout volume for its merchants. Integrating payment orchestration into merchant checkout flows (not just Privy billing) creates a new product category.
4. **Post-Attentive independence**: Divested from Attentive in 2023, now building independently. Payment infrastructure is a strategic decision that defines the next growth phase.
5. **Shopify ecosystem leadership**: #1 reviewed email/SMS app on Shopify. Shopify merchants increasingly sell globally and need local payment methods. Privy can become the bridge.
6. **Competitive differentiation**: Klaviyo (public, $690M+ revenue) and Mailchimp (Intuit) have broader payment acceptance. Privy needs to match or exceed to compete at scale.

**Sources:**
- [Privy Official Website](https://www.privy.com/)
- [Privy About Us](https://www.privy.com/about-us)
- [Privy Pricing Page](https://www.privy.com/pricing)
- [Privy Shopify App Store](https://apps.shopify.com/privy)
- [Privy Billing, Payments, and Refunds](https://help.privy.com/docs/learn/account-settings-and-billing/account-settings/billing-payments-and-refunds)
- [Privy Acquires Emotive](https://www.privy.com/blog/emotive-joins-privy)
- [Privy Acquires Sendlane - PRWeb](https://www.prweb.com/releases/privy-acquires-sendlane-to-strengthen-its-position-as-an-ecommerce-growth-platform-302671952.html)
- [Attentive Acquires Privy - Ecommerce Fastlane](https://ecommercefastlane.com/privy-has-been-acquired-by-attentive/)
- [Privy $120M Exit - Ben Jabbawy](https://markmacleod.me/ben-jabbawy/)
- [Privy Shopify Partner Profile](https://www.shopify.com/plus/partners/privy)
- [Privy Beyond the Build - Shopify](https://www.shopify.com/partners/blog/beyond-the-build-privy)
- [Ben Jabbawy About](https://benjabbawy.com/about)
- [Privy Review 2026 - ATTN Agency](https://www.attnagency.com/blog/privy-shopify-review)
- [What is Privy 2026 - FireBear](https://firebearstudio.com/blog/what-is-privy.html)
- [Brandfetch: Privy Logo](https://brandfetch.com/privy.com)
