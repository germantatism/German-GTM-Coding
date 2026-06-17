# SHOPLINE | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: SHOPLINE
=======================================

Logo: https://brandfetch.com/shoplineapp.com
Nombre merchant: SHOPLINE

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Platform PSP Dependency
Tittle_Pain Point_2: Cross Border Auth Gaps
Tittle_Pain Point_3: Limited APM Coverage
Tittle_Pain Point_4: Merchant Churn Risk
Tittle_Pain Point_5: US Expansion Payment Gap

Desc_Pain Point_1: SHOPLINE Payments is built on Adyen for Platforms in Singapore, Malaysia, and Hong Kong. Outside these markets, merchants must self integrate with Stripe, Omise, Payoneer, or Asiabill. This creates a two tier experience: SHOPLINE Payments merchants get unified commerce, while the rest manage fragmented PSP setups on their own.
Desc_Pain Point_2: 600,000+ merchants sell cross border, but SHOPLINE's payment stack lacks intelligent routing. A Malaysian merchant selling to a UK buyer processes through a single PSP path with no BIN level optimization. Failed cross border transactions have no cascade to a second acquirer, meaning lost sales on high value international orders.
Desc_Pain Point_3: SHOPLINE Payments supports Visa, MC, Amex, JCB, UnionPay, Apple Pay, Google Pay, FPS, Alipay HK, WeChat Pay, and PayMe. But for merchants selling into Europe, LATAM, or the Middle East, critical local methods are absent: no iDEAL, no Pix, no SEPA, no Klarna, no Mada. Merchants expanding beyond Asia hit a payment wall.
Desc_Pain Point_4: Shopify is SHOPLINE's biggest competitor, and Shopify now offers Shop Pay, Shopify Payments (powered by Stripe), and 100+ APMs out of the box globally. SHOPLINE merchants who outgrow Asia and need European or LATAM payment coverage face a reason to migrate. Payment breadth is becoming a platform retention lever.
Desc_Pain Point_5: SHOPLINE launched in the US market in 2025 with accelerator programs and Goodie Nation partnerships. But US payment infrastructure is thin: SHOPLINE Payments US supports cards and basic wallets. Missing are ACH, Affirm, Cash App Pay, Afterpay, Venmo, and Amazon Pay. US merchants expect these at checkout.

SLIDE 1: PSP TOPOLOGY

PSP_1: Adyen (SHOPLINE Payments: SG, MY, HK)
PSP_2: Stripe (merchant self-integration)
PSP_3: Omise (Thailand)
PSP_4: Payoneer Checkout (cross border)
PSP_5: Asiabill (cross border)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: iDEAL (Netherlands)
Local_M_2: Pix (Brazil)
Local_M_3: SEPA Direct Debit (EU)
Local_M_4: Klarna (EU/US BNPL)
Local_M_5: Mada (Saudi Arabia)
Local_M_6: Affirm (US BNPL)
Local_M_7: Boleto (Brazil)
Local_M_8: GrabPay (SEA)
Local_M_9: DANA (Indonesia)
Local_M_10: Mercado Pago (LATAM)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing Engine
Tittle_Yuno_Cap2: Failover & Cascade Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration Layer

Desc_Yuno_Cap1: Route every cross border transaction to the optimal acquirer by destination country, card BIN, and currency in real time. With 600,000+ merchants and 680M+ customers transacting globally, even a 2% authorization uplift on cross border volumes translates to massive GMV recovery. Smart Routing dynamically selects between Adyen, Stripe, Omise, and Payoneer per transaction instead of static PSP assignments.
Desc_Yuno_Cap2: When Adyen declines a card in Singapore or Stripe rejects a US transaction, Yuno cascades to the next best processor in milliseconds. For cross border merchants, a single PSP failure means a lost international sale. With Yuno, if one acquirer goes down or returns a soft decline, the payment automatically retries through an alternative route. SHOPLINE merchants never lose a sale while a viable path exists.
Desc_Yuno_Cap3: One API activates iDEAL for the Netherlands, Pix and Boleto for Brazil, SEPA for Europe, Klarna and Affirm for BNPL, Mada for Saudi Arabia, GrabPay across SEA, DANA for Indonesia, and Mercado Pago for LATAM. Yuno connects 1,000+ payment methods across 40+ countries. SHOPLINE merchants expanding beyond Asia get instant local payment access without per market integrations.
Desc_Yuno_Cap4: Replace SHOPLINE's fragmented payment stack (Adyen in SG/MY/HK, Stripe for self serve, Omise in Thailand, Payoneer and Asiabill for cross border) with a single orchestration layer. Real time approval rate dashboards across all merchants and markets. Centralized settlement, unified fraud scoring, and one integration that scales from Hong Kong to Houston. A white label orchestrator that makes SHOPLINE Payments globally competitive with Shopify Payments.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**SHOPLINE at a glance:**
- Founded: 2013 in Hong Kong by Tony Wong (Founder & CEO)
- Headquarters: Singapore (relocated for global expansion)
- Offices: Hong Kong, Singapore, Kuala Lumpur, Ho Chi Minh City, Shenzhen, US
- Revenue: $420.1M (2025)
- Total funding: $48.2M over 6 rounds (investors: Alibaba Entrepreneurs Fund, 500 Global, Huanju Times Group)
- 600,000+ merchants globally (primarily Asia)
- 680M+ customers served through merchant stores
- ~2,000 employees (some sources cite ~957 as of Feb 2026)
- SaaS platform offering: e-commerce, social commerce, POS, CRM, B2B management, omnichannel retail
- Positioned as "Shopify of Asia"
- Key brands using SHOPLINE: Lush, Heinemann Asia Pacific, Angliss, Lyde Bikes, In The Style, Peter Jackson, Sunnystep
- US expansion in 2025: Plug and Play Innovation Accelerator, Goodie Nation partnership for diverse founders
- Competitors: Shopify (dominant), WooCommerce, EasyStore, Boutir, 91APP

**Confirmed PSPs and payment partners:**

| Provider | Role | Region |
|----------|------|--------|
| Adyen (for Platforms) | Powers SHOPLINE Payments: card acquiring, POS, KYC, PCI compliance | Singapore, Malaysia, Hong Kong |
| Stripe | Third party gateway (merchant self integration) | Global (where available) |
| Omise | Payment gateway | Thailand |
| Payoneer Checkout | Cross border card payments in 120+ currencies | Global |
| Asiabill | Cross border payment solutions | Global (China focused merchants) |
| PayPal | Digital wallet | Global |
| Atome | BNPL | SEA markets |

**SHOPLINE Payments supported methods (built in):**
- Visa, Mastercard, American Express, JCB, Diners Club, UnionPay
- Apple Pay, Google Pay
- FPS (Faster Payment System, Hong Kong)
- Alipay HK, WeChat Pay, PayMe (Hong Kong wallets)
- COD (Cash on Delivery)
- Custom payment methods (merchant configured)

**No payment orchestrator detected.** SHOPLINE Payments runs on Adyen in 3 markets; outside those, merchants self integrate with third party PSPs.

**Adyen partnership details (announced Sep 2022, expanded 2025):**
- Adyen for Platforms powers SHOPLINE Payments in SG, MY, HK
- One contract for all 3 markets, single technical integration
- Adyen POS terminals for in store payments
- Automated KYC for merchant onboarding
- PCI compliance through Adyen's encryption solutions
- Settlement periods reduced by 2 days after integration
- In 2025: integrated 4 new payment methods, reduced launch times by ~70%, lowered costs by ~60%
- Executive: Amadea Choo (SHOPLINE Singapore), Priyanka Gargav (Adyen)

**Key competitive gaps vs Shopify:**
- Shopify Payments (powered by Stripe) available in 20+ countries with 100+ APMs
- Shopify offers Shop Pay, Afterpay, Klarna, Affirm, local bank transfers natively
- SHOPLINE Payments limited to 3 markets with ~15 payment methods
- Merchants expanding beyond Asia face payment coverage disadvantage on SHOPLINE

**Key meeting angles:**
1. **Platform level orchestration** | SHOPLINE is a SaaS commerce platform, not a single merchant. Integrating an orchestrator benefits all 600,000+ merchants simultaneously. One deal, 600K merchant reach
2. **Adyen dependency risk** | SHOPLINE Payments relies on Adyen as sole infrastructure. No failover if Adyen has an outage. An orchestration layer adds resilience and routing optionality
3. **Cross border blind spot** | 600K+ merchants selling globally, but local payment methods stop at Asia. European, LATAM, and Middle East APMs are entirely absent. Yuno's 1,000+ APM library fills this
4. **US expansion = payment gap** | SHOPLINE is actively entering the US market. American merchants expect ACH, Affirm, Cash App Pay, Venmo at minimum. SHOPLINE Payments US needs to match Shopify Payments
5. **Merchant retention lever** | Shopify offers 100+ APMs globally. SHOPLINE merchants who outgrow Asia may churn to Shopify for payment breadth. Orchestration makes SHOPLINE Payments competitive
6. **$420M revenue at stake** | SHOPLINE's revenue model includes payment transaction fees. Better auth rates and broader APM coverage directly increase platform GMV and SHOPLINE's take rate
7. **White label opportunity** | Yuno can power "SHOPLINE Payments" as a white label orchestrator, giving SHOPLINE a globally competitive payment product without building it in house

**Sources:**
- [Adyen: Expands Partnership with SHOPLINE (Sep 2022)](https://www.adyen.com/press-and-media/adyen-expands-partnership-with-shopline-to-supercharge-smart-commerce)
- [Adyen: lastminute.com Global Payment Upgrade (Adyen for Platforms reference)](https://www.adyen.com/knowledge-hub/lastminute-global-payment-upgrade)
- [SHOPLINE Payment Partners Page](https://www.shopline.com/payment-partner)
- [SHOPLINE Payments Page](https://www.shopline.com/payments)
- [SHOPLINE Payments FAQ](https://help.shopline.com/hc/en-001/articles/900004922406-SHOPLINE-Payments-FAQ)
- [SHOPLINE Payments for the United States](https://help.shopline.com/hc/en-001/articles/26022470787609-SHOPLINE-Payments-for-the-United-States)
- [SHOPLINE Payments for Hong Kong](https://help.shopline.com/hc/en-001/articles/20402969353497-SHOPLINE-Payments-for-Hong-Kong)
- [SHOPLINE Payment Options Introduction](https://support.shoplineapp.com/hc/en-us/articles/204906335-Payment-options-introduction-)
- [SHOPLINE Checkout and Payment Products](https://www.shopline.com/products/checkout-payment)
- [Payoneer: SHOPLINE Integration](https://www.payoneer.com/checkout/shopline-integration/)
- [SHOPLINE About Us](https://www.shopline.com/about)
- [SHOPLINE Singapore HQ Expansion](https://www.ecommerceexpoasia.com/exhibitor-press-releases/shopline-positions-itself-global-expansion-establishing-headquarters-singapore)
- [SHOPLINE + Plug and Play Accelerator (2025)](https://www.prnewswire.com/news-releases/shopline-and-plug-and-play-launch-innovation-accelerator-to-empower-emerging-consumer-brands-in-the-us-302501211.html)
- [SHOPLINE + Goodie Nation Partnership (Aug 2025)](https://www.prnewswire.com/news-releases/shopline-and-goodie-nation-partner-to-expand-e-commerce-access-and-equity-for-diverse-founders-across-the-us-302540661.html)
- [SHOPLINE on Crunchbase](https://www.crunchbase.com/organization/shopline)
- [SHOPLINE on Tracxn](https://tracxn.com/d/companies/shopline/__ywDpy1waJlo4Ru9Z0NR3VWY1l37Yd0khtFyY2IvyBPY)
- [SHOPLINE Revenue (Growjo)](https://growjo.com/company/SHOPLINE)
- [SHOPLINE Market Share (6sense)](https://6sense.com/tech/ecommerce-platform/shopline-market-share)
- [SHOPLINE Cross Border Solutions (HK)](https://shopline.hk/en/enterprise/cross-border)
- [SHOPLINE Logo (Brandfetch)](https://brandfetch.com/shoplineapp.com)
