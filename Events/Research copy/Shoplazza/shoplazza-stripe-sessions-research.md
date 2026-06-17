# SHOPLAZZA | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: SHOPLAZZA
=======================================

Logo: https://brandfetch.com/shoplazza.com
Nombre merchant: SHOPLAZZA

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Stripe Single PSP Dependency
Tittle_Pain Point_2: LATAM Payment Blind Spot
Tittle_Pain Point_3: China Merchant PSP Fragmt
Tittle_Pain Point_4: Smart Routing Still Basic
Tittle_Pain Point_5: Middle East Coverage Gap

Desc_Pain Point_1: Shoplazza Payments runs on Stripe Connect as its sole payment infrastructure for merchants in the US, Canada, UK, EU, and Hong Kong. If Stripe declines a transaction or experiences an outage, there is no cascade to a second acquirer. With 650,000+ merchants depending on Shoplazza Payments, a single PSP failure cascades across the entire platform. No failover path exists.
Desc_Pain Point_2: Shoplazza merchants sell into 180+ countries, but Shoplazza Payments supports zero Latin American local payment methods. No Pix (Brazil), no OXXO (Mexico), no Mercado Pago, no Boleto. With LATAM digital payment revenue projected to reach $0.3T by 2027 and 94% of LATAM shoppers preferring local methods, Shoplazza merchants lose sales on every transaction into the region.
Desc_Pain Point_3: Shoplazza's core merchant base is Chinese cross border sellers, served by a fragmented set of China focused PSPs: PingPong, Motonpay, iPasspay, UseePay, and Payoneer. Each PSP has its own dashboard, settlement schedule, and fraud rules. Chinese merchants managing 3 to 4 PSPs simultaneously waste operational bandwidth and lack a unified view of payment performance across providers.
Desc_Pain Point_4: Shoplazza announced "smart routing and automatic retries" in April 2025, but the routing operates within a single PSP (Stripe). True smart routing requires multiple acquirers competing per transaction, selecting the best path by card BIN, currency, and issuing bank. Shoplazza's routing optimizes within Stripe's network rather than across independent processors.
Desc_Pain Point_5: Shoplazza merchants expanding into the Middle East have no access to Mada (Saudi Arabia), Knet (Kuwait), Benefit (Bahrain), or Fawry (Egypt) through Shoplazza Payments. The platform's supported regions stop at US, Canada, UK, EU, and Hong Kong. Merchants selling into the fastest growing ecommerce region in the world must integrate regional PSPs manually or lose the sale.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe Connect (Shoplazza Payments: US, CA, UK, EU, HK)
PSP_2: Payoneer Checkout (cross border cards, 120+ currencies)
PSP_3: PingPong (Chinese merchant collections)
PSP_4: Worldpay (UK merchants)
PSP_5: UseePay (cross border credit card)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix (Brazil)
Local_M_2: OXXO (Mexico)
Local_M_3: Boleto (Brazil)
Local_M_4: Mercado Pago (LATAM)
Local_M_5: Mada (Saudi Arabia)
Local_M_6: Knet (Kuwait)
Local_M_7: Fawry (Egypt)
Local_M_8: GrabPay (SEA)
Local_M_9: DANA (Indonesia)
Local_M_10: Paytm/UPI (India)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Multi Acquirer Smart Routing
Tittle_Yuno_Cap2: Failover Cascade Retries
Tittle_Yuno_Cap3: 1,000+ Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration Layer

Desc_Yuno_Cap1: Route every transaction across Stripe, Worldpay, Payoneer, and additional acquirers simultaneously, selecting the optimal path by card BIN, currency, and destination country. With 650,000+ merchants and 180+ countries, even a 3% authorization uplift translates to massive GMV recovery. True smart routing means processors compete per transaction, not static assignment to a single PSP like Stripe Connect.
Desc_Yuno_Cap2: When Stripe declines a card in the US or Worldpay rejects a UK transaction, Yuno cascades to the next best processor in milliseconds. Shoplazza's current infrastructure has no failover: a Stripe decline is a lost sale. With Yuno, if one acquirer goes down or returns a soft decline, the payment retries through an alternative route automatically. 650,000+ merchants never lose a sale while a viable path exists.
Desc_Yuno_Cap3: One API activates Pix and Boleto for Brazil, OXXO for Mexico, Mercado Pago for LATAM, Mada for Saudi Arabia, Knet for Kuwait, Fawry for Egypt, GrabPay across SEA, DANA for Indonesia, and UPI for India. Yuno connects 1,000+ local payment methods across 40+ countries. Shoplazza merchants expanding beyond North America and Europe get instant local payment access without per market integrations.
Desc_Yuno_Cap4: Replace Shoplazza's fragmented payment stack (Stripe for Western markets, PingPong and Motonpay for Chinese merchants, Payoneer for cross border, Worldpay for UK) with a single orchestration layer. Centralized reporting across all PSPs, unified settlement, consolidated fraud scoring, and one integration that scales from Shanghai to Sao Paulo. A white label orchestrator that makes Shoplazza Payments globally competitive with Shopify Payments.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**SHOPLAZZA at a glance:**
- Founded: 2017 in Shenzhen, China by Jeff Li (Founder & CEO)
- Headquarters: Dual HQ in Shenzhen, China and Markham/Toronto, Canada (global strategy)
- Co-Founder & COO: Alyson Zhang (Head of Internationalization)
- VP of Development: Yang Zhenzong
- Revenue: $52.5M (2024), up from $46.6M prior year, $29.6M in 2023
- Total funding: $160M over 2 rounds (investors: Sky9 Capital, SoftBank Vision Fund)
- 650,000+ merchants across 180+ countries and regions
- ~194-300 employees (sources vary)
- Positioned as "Shopify of China" / purpose built for cross border DTC sellers
- Products: AI-powered online store builder, POS, CRM, marketing automation, multi-language/multi-currency
- Jeff Li: Fortune China 40 Under 40 (2022), former head of Baidu internationalization
- AI-native commerce OS launched April 2026 with unified AI agents (store builder, ad management, content creation)
- Nearly 90% of marketing and operational plugins are free

**Shoplazza Payments details (proprietary, launched 2025):**
- Powered by Stripe Connect
- Available in: US, Canada, UK, EU, Hong Kong
- Supported cards: Visa, Mastercard, Amex, Discover, Diners Club, JCB, UnionPay
- Digital wallets: Apple Pay, Google Pay
- BNPL: Klarna, Afterpay, Affirm
- European local methods: iDEAL, EPS, Bancontact, Przelewy24
- Settlement: T+2 (US/CA), T+3 (HK)
- AI features announced: smart routing, automatic retries (April 2025)

**Confirmed PSPs and payment partners:**

| Provider | Role | Region |
|----------|------|--------|
| Stripe Connect | Powers Shoplazza Payments (primary infrastructure) | US, CA, UK, EU, HK |
| Payoneer Checkout | Cross border card payments in 120+ currencies | Global |
| PingPong | Chinese merchant cross border collections | China focused |
| Worldpay | Credit card processing for UK merchants | UK |
| UseePay | Cross border credit card processing | Global (China merchants) |
| iPasspay | International credit card collection | Global (China merchants) |
| Motonpay | Cross border payment solutions | Global (China merchants) |
| PayPal | External payment provider | Global |
| Amazon Pay | External payment provider | Global |
| Adyen | Payment gateway option | Global |

**Key competitive gaps vs Shopify:**
- Shopify Payments (powered by Stripe) available in 20+ countries with 100+ APMs natively
- Shopify offers Shop Pay, Afterpay, Klarna, Affirm, local bank transfers across markets
- Shoplazza Payments limited to 5 market regions with no LATAM, Middle East, or SEA local methods
- Chinese merchants on Shoplazza manage 3-4 fragmented PSPs with no unified dashboard

**Cart abandonment data (cited by Shoplazza):**
- 65% of cart abandonment occurs after customers enter checkout (Nuvei data)
- 23% due to failed payments
- 21% from payment detail entry hesitation
- Case study: Premium brand saw 50%+ YoY sales increase during BFCM 2024 after implementing diverse payment options

**Key meeting angles:**
1. **Platform-level deal** | Shoplazza is a SaaS commerce platform with 650,000+ merchants. One orchestration integration benefits every merchant simultaneously. One deal, 650K merchant reach
2. **Stripe single-point-of-failure** | Shoplazza Payments runs entirely on Stripe Connect. No failover, no cascade, no multi-acquirer routing. Yuno adds resilience and authorization uplift without replacing Stripe
3. **LATAM and Middle East gap** | Zero local payment methods in the two fastest growing ecommerce regions. Pix, OXXO, Mada, and Knet are completely absent. Yuno's 1,000+ APM library fills this immediately
4. **Chinese merchant pain** | Core merchant base manages PingPong, Motonpay, iPasspay, and UseePay in parallel. Yuno unifies all providers under one orchestration layer with centralized reporting
5. **Smart routing is incomplete** | Shoplazza's announced "smart routing" operates within Stripe only. True multi-acquirer routing requires an orchestration layer that routes across processors. Yuno enables this
6. **White-label opportunity** | Yuno can power Shoplazza Payments as a white-label orchestrator, making it globally competitive with Shopify Payments without Shoplazza building infrastructure
7. **$52.5M revenue scaling fast** | SoftBank-backed, 650K merchants, AI-native OS. Payment infrastructure is the bottleneck to global growth. Orchestration unlocks LATAM, MEA, and SEA

**Sources:**
- [Shoplazza Partners with Stripe (PRNewswire, Sep 2024)](https://www.prnewswire.com/news-releases/shoplazza-partners-with-stripe-to-revolutionize-e-commerce-payment-solutions-302244825.html)
- [Shoplazza Launches Upgraded Payment Solution (PRNewswire, Apr 2025)](https://www.prnewswire.com/news-releases/shoplazza-launches-upgraded-payment-solution-to-boost-global-e-commerce-conversion-rates-302419449.html)
- [Shoplazza Payments Overview (Help Center)](https://helpcenter.shoplazza.com/hc/en-us/articles/30709573098649-Shoplazza-Payments-Overview)
- [Shoplazza Third-Party Payment Providers (Help Center)](https://helpcenter.shoplazza.com/hc/en-us/articles/13958042148121-Third-party-payment-providers)
- [Shoplazza Payment Service Provider (Help Center)](https://helpcenter.shoplazza.com/hc/en-us/articles/4842598862617-Payment-Service-Provider)
- [Shoplazza + Payoneer Checkout (Payoneer)](https://www.payoneer.com/checkout/shoplazza-integration/)
- [Shoplazza + Payoneer 360K Merchants (PRNewswire)](https://www.prnewswire.com/news-releases/shoplazza-to-bring-payoneer-checkout-to-its-360-000-merchants-301558480.html)
- [Shoplazza Revenue $52.5M (Latka)](https://getlatka.com/companies/shoplazza)
- [Shoplazza C1 Financing $150M (Sky9 Capital)](https://www.sky9capital.com/news/12203.html)
- [Shoplazza on Crunchbase](https://www.crunchbase.com/organization/shoplazza)
- [Shoplazza Adopts Agentic Commerce Architecture (PRNewswire, Apr 2026)](https://www.prnewswire.com/news-releases/shoplazza-adopts-agentic-commerce-architecture-to-power-ai-driven-e-commerce-operations-302715409.html)
- [Shoplazza AI Store Builder (PRNewswire, Apr 2026)](https://www.manilatimes.net/2026/04/15/tmt-newswire/pr-newswire/shoplazza-launches-ai-store-builder-delivering-ready-to-sell-storefronts-through-a-single-agent/2321019)
- [Jeff Li Interview (Shoplazza Blog)](https://www.shoplazza.com/blog/interview-with-jeff-li)
- [Jeff Li, Business Chief Asia](https://businesschief.asia/leadership-and-strategy/5-mins-with-jeff-li-founder-and-ceo-of-shoplazza)
- [Shoplazza Payment Page](https://www.shoplazza.com/payment-2)
- [Shoplazza Logo (Brandfetch)](https://brandfetch.com/shoplazza.com)
