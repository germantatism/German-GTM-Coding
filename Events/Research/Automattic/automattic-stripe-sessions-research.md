# AUTOMATTIC | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Automattic
=======================================

Logo: https://upload.wikimedia.org/wikipedia/commons/0/09/Automattic_logo.svg
Nombre merchant: Automattic

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: 39-Country WooPayments Cap
Tittle_Pain Point_2: Ecommerce Decline Rates
Tittle_Pain Point_3: Stripe-Only Dependency
Tittle_Pain Point_4: LATAM/APAC APM Gaps
Tittle_Pain Point_5: Multi-Product Fragmentation

Desc_Pain Point_1: WooPayments is only available in 39 countries. Merchants in all of Latin America, Africa, most of Asia, and Eastern Europe cannot use WooPayments at all. 4M+ WooCommerce stores globally but the native payment solution excludes most emerging markets.
Desc_Pain Point_2: Ecommerce authorization declines average 17%. WooCommerce merchants lose sales on every failed transaction with no smart retry or cascade. At $30-35B annual GMV across the ecosystem, even 1% recovery equals $300M+ in unlocked revenue for merchants.
Desc_Pain Point_3: WooPayments is built entirely on Stripe Express accounts. No secondary acquirer, no failover path. If Stripe experiences degradation, all WooPayments merchants lose payment processing simultaneously across 39 countries.
Desc_Pain Point_4: WooPayments lists only 10 local payment methods (iDEAL, Bancontact, P24, EPS, GrabPay, Alipay, WeChat Pay, Multibanco, SEPA DD, Affirm/Klarna). Zero coverage for Pix, UPI, SPEI, OXXO, GCash, OVO, Boleto, or M-Pesa across the fastest-growing ecommerce regions.
Desc_Pain Point_5: Automattic runs WordPress.com, WooCommerce, Tumblr, Jetpack, and 15+ products. Each has separate billing and payment flows. No unified payment orchestration layer, no consolidated analytics across the $710M revenue portfolio.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (WooPayments backbone, WordPress.com billing)
PSP_2: PayPal (WooCommerce PayPal Payments plugin)
PSP_3: Apple/Google IAP (mobile apps)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: UPI
Local_M_3: SPEI
Local_M_4: OXXO
Local_M_5: GCash
Local_M_6: OVO/DANA
Local_M_7: Boleto
Local_M_8: M-Pesa
Local_M_9: Konbini
Local_M_10: BLIK

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each WooCommerce transaction through the optimal acquirer based on card BIN, merchant country, and buyer geography. With $30-35B in ecosystem GMV and 17% average ecommerce decline rates, smart routing recovering even 3% translates to $900M+ in additional approved transactions across 4M+ stores annually.
Desc_Yuno_Cap2: Automatic cascade when Stripe declines a charge. Yuno reroutes to the next best acquirer in milliseconds, recovering up to 50% of soft declines. For WooCommerce merchants losing 17% of transactions to declines, failover directly converts abandoned carts into completed sales.
Desc_Yuno_Cap3: Unlocks the APMs WooCommerce merchants need worldwide: Pix in Brazil, UPI in India, SPEI/OXXO in Mexico, GCash in Philippines, OVO in Indonesia, Boleto in Brazil, M-Pesa in Africa, BLIK in Poland. One API, 1,000+ payment methods, instant geo-routing. Extends WooPayments beyond the 39-country limit.
Desc_Yuno_Cap4: One orchestration layer unifying Automattic's fragmented payment stack across WordPress.com, WooCommerce, Tumblr, and Jetpack. Real-time approval rates, centralized reconciliation across all providers, millisecond anomaly detection via NOVA. 75% reduction in payment operations overhead across a $710M revenue business.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Automattic at a glance:**
- Founded 2005 by Matt Mullenweg; HQ San Francisco (fully distributed, all remote)
- 2,007 employees (Automatticians) in 97 countries, 123 languages
- Revenue: $710M annually (2024), 11.2% YoY growth
- Valuation: $7.5B (last primary round, Feb 2021); some secondary trading at lower valuations
- Total funding: $896M-$998M from Tiger Global, Insight Partners, True Ventures, Salesforce Ventures, and others
- CEO: Matt Mullenweg
- Product portfolio: WordPress.com, WooCommerce, Tumblr, Jetpack, Simplenote, Day One, Pocket Casts, Longreads, Beeper, Akismet, Gravatar, WPScan, Newspack, WordPress VIP, and more
- 2024 acquisitions: Beeper (messaging), Harper (grammar), WPAI (AI plugin)
- WordPress powers 43%+ of all websites globally

**WooCommerce Scale:**
- 4M+ live WooCommerce stores worldwide
- 33-39% market share of all ecommerce platforms globally
- $30-35B estimated annual GMV across ecosystem
- #1 most widely used ecommerce platform globally
- Generates ~$250-300M annually for Automattic (extensions, WooPayments, hosting referrals)
- WooPayments (Stripe-based) serves 15-20% of WooCommerce stores
- Recently experienced -3.2% YoY decline as merchants migrate to hosted solutions (Shopify +8.2%, Wix +12.1%)
- Named launch partner for Stripe's Agentic Commerce Platform (Oct 2024)

**Confirmed PSPs:**
- Stripe: Primary processor. WooPayments built entirely on Stripe Express/Connect accounts. WordPress.com also uses Stripe for subscription billing. Deep strategic partnership.
- PayPal: WooCommerce PayPal Payments plugin (APMs, Venmo US, Pay Later). WordPress.com accepts PayPal for plan purchases.
- Apple/Google IAP: Mobile app purchases across WordPress.com, Tumblr apps
- Third-party gateways: WooCommerce supports 100+ payment gateway plugins (Authorize.net, Square, Mollie, Adyen, etc.) but these are merchant-installed, not Automattic-managed
- No payment orchestrator detected

**WooPayments Accepted Methods:**
- Cards: Visa, Mastercard, Amex, Discover, JCB, Diners Club, Cartes Bancaires, UnionPay, eftpos Australia
- Express checkout: Apple Pay, Google Pay, Amazon Pay, Link by Stripe, WooPay
- BNPL: Affirm, Afterpay/Clearpay, Klarna
- Local methods: iDEAL/Wero, Bancontact, EPS, Przelewy24, GrabPay, Alipay, WeChat Pay, Multibanco, SEPA DD (closed beta)
- HSA/FSA cards for qualified merchants

**WooPayments Country Availability (39 countries only):**
- Europe (30): Austria, Belgium, Bulgaria, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, Ireland, Italy, Latvia, Lithuania, Luxembourg, Malta, Netherlands, Norway, Poland, Portugal, Romania, Slovakia, Slovenia, Spain, Sweden, Switzerland, UK
- Asia-Pacific (5): Australia, Hong Kong, Japan, New Zealand, Singapore
- North America (2): Canada, United States
- Middle East (1): UAE
- NOT available: All of Latin America, Africa, India, Indonesia, Philippines, Thailand, Malaysia, South Korea, Russia, Turkey, and 150+ other countries

**WordPress.com Top Markets by Traffic:**
- United States: 15.2%
- India: 8.1%
- Germany: 5.1%
- United Kingdom: 4.1%
- Japan: 4.1%
- Rest of world: 63.4%

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (15.2% of WordPress.com traffic, largest WooCommerce market ~400K stores)
  WooPayments Accepted: All cards, Apple Pay, Google Pay, Amazon Pay, Affirm, Afterpay, Klarna
  Missing: ACH for subscriptions, Cash App Pay, Zelle
  Note: Best-served market. BNPL and express checkout well covered.

MARKET 2: India (8.1% of WordPress.com traffic, massive WordPress user base)
  WooPayments: NOT AVAILABLE in India
  Missing: UPI, RuPay, Paytm, PhonePe, Netbanking, EMI options
  Note: India is the #2 WordPress market. WooCommerce merchants in India cannot use WooPayments at all. UPI processes 12B+ monthly transactions.

MARKET 3: Brazil (large WooCommerce presence in LATAM)
  WooPayments: NOT AVAILABLE in Brazil
  Missing: Pix, Boleto, local debit (Elo, Hipercard), installments (parcelamento)
  Note: Pix is the dominant payment method with 4B+ monthly transactions. WooCommerce merchants in Brazil forced to use third-party gateways.

MARKET 4: Mexico (growing LATAM ecommerce)
  WooPayments: NOT AVAILABLE in Mexico
  Missing: SPEI, OXXO, CoDi, Kueski Pay
  Note: 60%+ population unbanked/underbanked. OXXO cash payments at 20,000+ stores are critical for ecommerce conversion.

MARKET 5: Indonesia (5th largest internet population)
  WooPayments: NOT AVAILABLE in Indonesia
  Missing: GoPay, OVO, DANA, ShopeePay, bank transfers, QRIS
  Note: Card penetration under 10%. E-wallets dominate. WordPress.com even accepts cards from Indonesian digital banks (Jenius, Jago) but no local wallets.

**Payment Challenges:**
- Ecommerce authorization decline rates average 17% industry-wide
- Subscription services report ~15% failed payment rates
- WooPayments limited to 39 countries, excluding all of LATAM, Africa, India, most of APAC
- No smart retry or cascade logic in WooPayments beyond Stripe's default behavior
- Cross-border transactions incur Stripe's 1.5% international card fee + 1% currency conversion
- PayPal does not support BRL, IDR, INR, or TRY currencies on WordPress.com
- WooCommerce seeing -3.2% YoY decline; payment friction is a cited factor in merchant migration to Shopify

**Key meeting angles:**
1. **Massive global footprint, limited payment reach**: 4M+ stores worldwide but WooPayments only works in 39 countries. India (#2 market), Brazil, Mexico, Indonesia all excluded.
2. **Ecosystem GMV at stake**: $30-35B in annual GMV. At 17% decline rates, $5-6B in transactions fail annually. Smart routing + failover recovers a material portion.
3. **Competitive threat from Shopify**: Shopify Payments covers 175+ countries and growing. WooCommerce's 39-country limit is a competitive disadvantage driving merchant migration (-3.2% YoY).
4. **Multi-product orchestration opportunity**: 15+ products (WordPress.com, WooCommerce, Tumblr, Jetpack) each with separate billing. One orchestration layer unifies payment ops for a $710M revenue company.
5. **Stripe dependency risk**: Single acquirer across the entire payment stack. One Stripe outage impacts WooPayments merchants across 39 countries plus WordPress.com subscriber billing.
6. **Emerging market expansion**: India, Brazil, Mexico, Indonesia represent billions in ecommerce TAM. Unlocking local APMs (UPI, Pix, OXXO, GoPay) would open WooCommerce to markets Shopify already serves.

**Sources:**
- [WooPayments Payment Methods](https://woocommerce.com/document/woopayments/payment-methods/)
- [WooPayments & Stripe Partnership](https://woocommerce.com/document/woopayments/account-management/partnership-with-stripe/)
- [WooPayments Country Availability](https://woocommerce.com/document/woopayments/compatibility/countries/)
- [Stripe: WordPress.com Case Study](https://stripe.com/customers/wordpress)
- [Stripe: WooCommerce Case Study](https://stripe.com/customers/woo)
- [WooCommerce Payment Gateways](https://woocommerce.com/product-category/woocommerce-extensions/payment-gateways/)
- [WooCommerce Understanding Failed Payments](https://woocommerce.com/document/stripe/troubleshooting/understanding-failed-payments/)
- [WooCommerce Developer Blog: 2025 Roadmap](https://developer.woocommerce.com/2024/12/12/woocommerce-in-2025/)
- [Automattic Wikipedia](https://en.wikipedia.org/wiki/Automattic)
- [Automattic Revenue (Latka)](https://getlatka.com/companies/automattic)
- [WooCommerce Market Share 2026](https://redstagfulfillment.com/what-is-woocommerces-market-share/)
- [WooCommerce GMV Insights](https://redstagfulfillment.com/woocommerces-gross-merchandise-volume/)
- [WooCommerce Store Count](https://redstagfulfillment.com/how-many-woocommerce-stores-are-live/)
- [State of WooCommerce 2026](https://storeleads.app/reports/woocommerce)
- [WooCommerce Statistics (Colorlib)](https://colorlib.com/wp/woocommerce-statistics/)
- [WordPress.com Payment Methods](https://wordpress.com/support/payment/)
- [WordPress.com Pricing](https://wordpress.com/pricing/)
- [SimilarWeb: wordpress.com Traffic](https://www.similarweb.com/website/wordpress.com/)
- [Decline Rates by Industry 2025](https://wallid.co/blog/tpost/7j3z2hljp1-payment-decline-rates-by-industry)
- [Automattic Logo (Wikimedia)](https://commons.wikimedia.org/wiki/File:Automattic_logo.svg)
- [WooCommerce Stripe Agentic Commerce](https://www.therepository.email/woocommerce-named-launch-partner-as-stripe-debuts-agentic-commerce-suite)
- [Automattic Press](https://automattic.com/press/)
