# BOLD COMMERCE (Bold.One) | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Bold Commerce (Bold.One)
=======================================

Logo: https://cdn.brandfetch.io/boldcommerce.com/w/512/h/512/theme/dark/icon.jpeg
Nombre merchant: Bold Commerce (Bold.One)

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Multi-PSP Fragmentation
Tittle_Pain Point_2: Checkout Conversion Leak
Tittle_Pain Point_3: No Orchestration Layer
Tittle_Pain Point_4: BNPL Coverage Gaps
Tittle_Pain Point_5: Global APM Blind Spots

Desc_Pain Point_1: Bold Checkout supports 15+ payment gateways (Stripe, Braintree, Adyen, PayPal, Cybersource, WorldPay, Moneris, Authorize.net, and more) but merchants choose one or two at a time. No intelligent routing across these PSPs exists. Each merchant configures static gateway assignments, missing the opportunity to route each transaction to the highest performing acquirer for that card BIN and market.
Desc_Pain Point_2: Bold's own data shows 17% of shoppers abandon checkout due to limited payment options. The Payment Booster addresses this with dynamic payment method display, but without smart routing behind the scenes, showing the right payment method does not guarantee the best approval rate. For 90,000+ brands processing through Bold Checkout, even 1% auth improvement at the gateway level drives significant revenue recovery.
Desc_Pain Point_3: Bold positions itself as the headless checkout layer between merchants and PSPs but does not provide payment orchestration. Merchants see payment methods at the front end (Apple Pay, Google Pay, PayPal, BNPL) but have no transaction-level routing, failover cascading, or real-time acquirer optimization. Bold's value stops at checkout UX, leaving payment performance on the table.
Desc_Pain Point_4: Bold supports BNPL through Braintree PayLater and PayPal Pay Later but coverage is limited to specific markets and PSP relationships. No direct Klarna, Affirm, or Afterpay integration in Bold Checkout. For enterprise merchants like Vera Bradley, Harry Rosen, and Staples Canada selling $100-$1,000+ items, comprehensive BNPL availability directly impacts conversion and average order value.
Desc_Pain Point_5: Bold supports Adyen for 40+ countries and Stripe for major markets but merchants configuring Bold Checkout cannot easily activate local payment methods like iDEAL, Bancontact, Pix, UPI, or Alipay. The Payment Booster's "region-specific payment solutions" promise requires per-gateway configuration rather than unified APM activation across all processors.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (preferred gateway)
PSP_2: Braintree (free tier available)
PSP_3: PayPal Complete Payments (free tier)
PSP_4: Adyen (40+ countries)
PSP_5: Cybersource / WorldPay / Moneris

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Klarna (direct)
Local_M_2: Affirm (direct)
Local_M_3: Afterpay (direct)
Local_M_4: iDEAL
Local_M_5: Pix
Local_M_6: UPI
Local_M_7: Alipay
Local_M_8: WeChat Pay
Local_M_9: Bancontact
Local_M_10: GrabPay

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Recovery
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across Bold's 15+ supported PSPs for every checkout. Each transaction routed to the highest performing acquirer for that card BIN, issuer, and market. Across 90,000+ brands using Bold Checkout on Shopify, Adobe Commerce, BigCommerce, and commercetools, smart routing delivers +3 to 10% auth uplift. For enterprise clients like Vera Bradley and Staples Canada, this translates to millions in recovered revenue annually.
Desc_Yuno_Cap2: Automatic cascade across Bold's payment gateways eliminates static single-gateway dependency. When Stripe declines, Yuno reroutes to Adyen or Braintree in milliseconds. Up to 50% recovery on soft declines via instant retry. NOVA AI recovers up to 75% of failed transactions. Bold's own data shows 17% checkout abandonment from payment friction. Failover turns declines into completed orders.
Desc_Yuno_Cap3: Activates the APMs Bold's merchants need globally: Klarna, Affirm, and Afterpay for BNPL (55% of shoppers have used BNPL), iDEAL for Dutch shoppers, Pix for Brazilian customers, UPI for Indian consumers, Alipay and WeChat Pay for Chinese shoppers, Bancontact for Belgian buyers, GrabPay for Southeast Asian markets. One API, 1,000+ payment methods across all Bold-powered checkouts.
Desc_Yuno_Cap4: One orchestration layer behind Bold's headless checkout, providing real-time routing intelligence across Stripe, Braintree, Adyen, PayPal, Cybersource, WorldPay, and Moneris. Centralized approval rate monitoring across all merchants, automated reconciliation, and millisecond anomaly detection via Monitors. Yuno complements Bold's front-end checkout UX with back-end payment optimization that Bold does not provide today.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Bold Commerce at a glance:**
- Model: Headless checkout and commerce platform (SaaS, checkout optimization, subscriptions, pricing)
- Domain: boldcommerce.com (bold.one is the parent company/brand)
- Merchants: 760,000+ have installed Bold apps; 90,000+ brands and retailers actively using
- Notable clients: Vera Bradley, Harry Rosen, Staples Canada, Pepsi, Mars, Pharrell Williams' Humanrace
- Countries: 170+ countries served
- Employees: 201-500 (200+ per Bold.One site)
- Headquarters: Winnipeg, Manitoba, Canada (50 Fultz Blvd); also Austin, Texas
- Founded: 2012 by Yvan Boisjoli, Eric Boisjoli, Jay Myers, Stefan Maynard
- CEO: Peter Karpas (appointed November 2022; previously PayPal, Intuit, First Data/Fiserv)
- Co-founder: Yvan Boisjoli
- Revenue: ~$75M annually (estimated August 2025)
- Total funding: $44M USD ($57M CAD) over multiple rounds
- Series B: $27M (January 2021), led by OMERS Ventures
- Key investors: OMERS Ventures, Whitecap Venture Partners, Round13 Capital
- Awards: Deloitte Tech Fast 50, E&Y Entrepreneur of the Year, CBInsights Retail Tech 100

**Core Products:**
- Bold Checkout: Headless, composable checkout with API-first architecture
- Bold Booster: Advanced checkout for Adobe Commerce, OpenCart, Gravity Forms (PayPal Fastlane, Apple Pay, Google Pay, Venmo)
- Payment Booster: Dynamic payment method display, A/B testing, audience-based payment flows
- Bold Subscriptions: Recurring billing and subscription management
- Bold Custom Pricing: Wholesale, VIP, customer-specific pricing
- Bold Upsell: AI-powered cross-sell and upsell
- rePete: AI-powered reorder sales agent (new, partnered with Node March 2026)
- Agentic Checkout: Headless endpoints for AI agents to process payments

**Platform Compatibility:**
- Shopify (primary, 760,000+ app installs)
- Adobe Commerce / Magento 2
- BigCommerce
- commercetools
- OpenCart
- Gravity Forms
- Custom headless implementations via API

**Recent Developments:**
- March 2026: rePete + Node partnership (convert guest checkout to repeat customers)
- NRF 2026: Featured at Shopify's NRF recap ("Commerce Favors the Bold")
- Agentic Checkout launch: AI agent-ready headless endpoints
- Peter Karpas CEO (PayPal, Intuit veteran) driving enterprise and payments strategy

**Payments Infrastructure:**
- Bold Checkout Supported Gateways:
  - Stripe (preferred, credit card + Apple Pay + Google Pay)
  - Braintree (credit card, Apple Pay, Google Pay, PayLater, PayPal, fraud management)
  - PayPal Complete Payments (credit/debit card, PayLater, PayPal)
  - Adyen (40+ countries)
  - Cybersource
  - Moneris
  - Authorize.net
  - GiveX
- Bold Cashier Additional Gateways:
  - WorldPay, Bambora North America, Elavon, Fat Zebra, MiGS, Payflow Pro, QuickPay V10, Sage Pay, SecurePay Australia, USAePay, Qualpay
- Free checkout when using PayPal Complete Payments or Braintree
- External Payments framework for custom integrations
- No payment orchestration or smart routing

**Payment Methods (Current via Gateways):**
- Credit/debit cards: Visa, Mastercard, Amex, Discover
- Digital wallets: Apple Pay, Google Pay, Samsung Pay
- PayPal, Venmo (via PayPal/Braintree)
- PayPal Pay Later / Braintree PayLater (BNPL, limited markets)
- Amazon Pay
- No direct Klarna integration
- No direct Affirm integration
- No direct Afterpay integration
- Local APMs depend on gateway configuration (Adyen enables some)

**Key Statistics (Bold's own data):**
- 17% abandon checkout due to limited payment options
- 55% of shoppers have used BNPL
- 29% utilize digital wallets
- Harry Rosen: 4X online revenue increase after launching 4 new payment methods

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (largest merchant base, enterprise clients)
  Currently offer: Visa/MC/Amex, Apple Pay, Google Pay, PayPal, Venmo, PayPal Pay Later
  Missing: Klarna, Affirm, Afterpay (direct), Amazon Pay (limited), ACH
  Bold's enterprise US merchants need comprehensive BNPL. 55% of shoppers have used BNPL.

MARKET 2: Canada (headquarters market, Staples Canada, Harry Rosen)
  Currently offer: Visa/MC/Amex, Apple Pay, Google Pay, PayPal, Moneris
  Missing: Interac, Klarna, Afterpay, Affirm
  Canadian merchants need Interac and BNPL. Harry Rosen saw 4X revenue with more payment methods.

MARKET 3: United Kingdom & Europe (Adyen-powered, 40+ countries)
  Currently offer: Visa/MC, Apple Pay, Google Pay, PayPal (via Adyen)
  Missing: iDEAL (direct activation), Bancontact, Klarna, Clearpay, Open Banking, SEPA
  European local APMs require per-gateway configuration rather than unified activation.

MARKET 4: Latin America (growing ecommerce, Pepsi/Mars global brands)
  Currently offer: Visa/MC via Adyen
  Missing: Pix (Brazil), Mercado Pago, OXXO (Mexico), PSE (Colombia), Boleto
  Global brands using Bold need LATAM APMs. Brazil and Mexico are massive ecommerce markets.

MARKET 5: Asia-Pacific (global brand expansion)
  Currently offer: Visa/MC via Adyen/Stripe
  Missing: Alipay, WeChat Pay, UPI, GrabPay, LINE Pay, Toss Pay
  Chinese, Indian, and Southeast Asian consumers need local wallets. Zero direct Asian APM activation.

**Payment Pain Points:**
1. 15+ supported gateways but no intelligent routing across them
2. Static gateway assignment per merchant, no per-transaction optimization
3. No failover cascading when primary gateway declines
4. 17% checkout abandonment from limited payment options (Bold's own data)
5. No direct Klarna, Affirm, or Afterpay integration
6. Local APM activation requires per-gateway configuration, not unified
7. Payment Booster optimizes front-end display but not back-end routing
8. Bold stops at checkout UX; no payment performance optimization
9. No real-time acquirer selection based on BIN, issuer, or geography
10. Enterprise merchants (Vera Bradley, Staples, Pepsi) need global APMs not available through Bold

**Key Meeting Angles:**
1. **90,000+ brands, 15+ gateways, no orchestration**: Bold Checkout connects to Stripe, Adyen, Braintree, PayPal, and more, but cannot route between them. Yuno adds the orchestration layer behind Bold's headless checkout
2. **Payment Booster + Yuno = full stack**: Bold optimizes which payment methods to show (front end). Yuno optimizes which processor handles the transaction (back end). Together they create a complete checkout optimization solution
3. **CEO from PayPal and Intuit**: Peter Karpas understands payment infrastructure deeply. He knows the value of routing, failover, and APM coverage. Yuno speaks his language
4. **17% abandonment, 55% BNPL demand**: Bold's own data proves the payment gap. Yuno provides 1,000+ APMs including Klarna, Affirm, and Afterpay that Bold does not directly offer. McDonald's gained +4.7% auth rate with Yuno
5. **Agentic commerce requires payment resilience**: As Bold launches Agentic Checkout for AI agents, payment reliability becomes even more critical. AI agents cannot handle failed payments gracefully. Yuno's failover ensures 50% soft decline recovery
6. **Enterprise client proof points**: Harry Rosen saw 4X revenue with more payment methods. Yuno can replicate this across all Bold merchants. InDrive achieved 90% approval across 10 markets with Yuno

**Sources:**
- [Bold Commerce](https://boldcommerce.com/)
- [Bold.One](https://bold.one/)
- [Bold Commerce About Us](https://boldcommerce.com/about-us)
- [Bold Payment Booster](https://boldcommerce.com/use-cases/payment-booster)
- [Bold Checkout](https://boldcommerce.com/product/headless-checkout)
- [Bold Booster](https://boldcommerce.com/checkout-home)
- [Bold Agentic Checkout](https://boldcommerce.com/agentic-checkout)
- [Bold Supported Gateways](https://developer.boldcommerce.com/guides/checkout/resources/supported-platforms-gateways)
- [Bold Connect Payment Processor](https://support.boldcommerce.com/hc/en-us/articles/16255433403156)
- [Bold Cashier Gateways](https://support.boldcommerce.com/hc/en-us/articles/115004452243)
- [Bold + PayPal Integration](https://www.businesswire.com/news/home/20230406005142/en/)
- [Bold CEO Peter Karpas](https://boldcommerce.com/press-releases/bold-commerce-names-peter-karpas-ceo-as-it-scales-composable-checkout)
- [Bold Series B (BusinessWire)](https://www.businesswire.com/news/home/20210119005627/en/)
- [Bold Series B (BetaKit)](https://betakit.com/bold-commerce-raises-35-million-cad-series-b-backed-by-omers/)
- [rePete + Node Partnership](https://salestechstar.com/partner-management-channel-enablement/repete-by-bold-commerce-partners-with-node-to-kill-the-guest-checkout-revenue-gap/)
- [Crunchbase: Bold Commerce](https://www.crunchbase.com/organization/bold-innovation-group-ltd)
- [Tracxn: Bold Commerce](https://tracxn.com/d/companies/bold-commerce/)
- [NRF 2026: Shopify + Bold](https://www.shopify.com/enterprise/blog/nrf-2026-recap)
