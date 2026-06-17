# HANDSHAKE (SHOPIFY) | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Handshake (Shopify)
=======================================

Logo: https://upload.wikimedia.org/wikipedia/commons/0/0e/Shopify_logo_2018.svg
Nombre merchant: Handshake (Shopify)

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Credit Card Only Checkout
Tittle_Pain Point_2: U.S. Only Market Lock
Tittle_Pain Point_3: No Net Terms at Scale
Tittle_Pain Point_4: B2B Fraud Blind Spot
Tittle_Pain Point_5: Single Gateway Dependency

Desc_Pain Point_1: Handshake's wholesale checkout only supports credit card payments through a single direct payment provider. B2B buyers expect ACH, bank wire, and local payment methods. Forcing credit cards on wholesale orders with $1,000+ AOVs inflates processing costs by 2 to 3% per transaction and drives buyers to competitors like Faire.
Desc_Pain Point_2: Handshake operates exclusively in the United States. Shopify serves merchants in 170+ countries and its B2B GMV grew 140% in 2024, yet Handshake cannot process cross-border wholesale orders. European, LATAM, and APAC retailers have zero access to the marketplace's 65,000+ brands.
Desc_Pain Point_3: Wholesale buyers expect Net 30, Net 60, and custom payment terms. While Shopify Plus offers native net terms for B2B, Handshake's marketplace checkout lacks integrated trade credit or deferred payment workflows. This forces brands to manage invoicing manually outside the platform, breaking the ordering experience.
Desc_Pain Point_4: B2B transactions carry higher fraud risk due to large order values and new buyer relationships. Handshake has no dedicated fraud screening layer for wholesale transactions. Without real-time risk scoring on $1,000+ orders from first-time retailers, brands absorb chargeback losses that erode wholesale margins.
Desc_Pain Point_5: Payments route through Shopify Payments (powered by Stripe) as the sole gateway. If Stripe experiences downtime or declines a transaction, there is no fallback acquirer or cascade logic. Every failed payment on a wholesale order risks losing the entire cart with no automatic retry.

SLIDE 1: PSP TOPOLOGY

PSP_1: Shopify Payments (native gateway)
PSP_2: Stripe (payment processor powering Shopify Payments)
PSP_3: Visa / Mastercard (card networks)
PSP_4: PayPal (alternative checkout option on Shopify)
PSP_5: Shop Pay (Shopify's accelerated checkout)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: ACH / Bank Transfer (U.S.)
Local_M_2: SEPA Direct Debit (EU)
Local_M_3: Open Banking (UK/EU)
Local_M_4: iDEAL (Netherlands)
Local_M_5: Bancontact (Belgium)
Local_M_6: Pix (Brazil)
Local_M_7: SPEI (Mexico)
Local_M_8: Boleto Bancario (Brazil)
Local_M_9: OXXO (Mexico)
Local_M_10: UPI (India)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each wholesale transaction through the optimal payment rail by order value, buyer geography, and payment method. With B2B AOVs exceeding $1,000, shifting high-value orders from credit card (2.9% + $0.30) to ACH or bank transfer saves 60 to 80% on processing fees per transaction. Smart Routing delivers +3 to 10% authorization uplift across all payment paths.
Desc_Yuno_Cap2: Automatic cascade eliminates single-gateway dependency on Shopify Payments/Stripe. When a wholesale order declines on the primary processor, Yuno reroutes instantly through an alternate acquirer. Up to 50% recovery on failed transactions, protecting high-value B2B carts that brands cannot afford to lose.
Desc_Yuno_Cap3: Unlocks the cross-border wholesale expansion Handshake needs beyond the U.S.: SEPA Direct Debit and Open Banking for European retailers, Pix and Boleto for Brazil, SPEI and OXXO for Mexico, iDEAL for Netherlands, UPI for India. One API, 1,000+ payment methods, opening the marketplace to Shopify's 170+ country footprint.
Desc_Yuno_Cap4: One dashboard unifying Shopify Payments, Stripe, PayPal, Shop Pay, and any future acquirers into a single reconciliation layer for wholesale transactions. Real-time monitoring across all B2B orders, NOVA fraud engine with 75% fewer false positives providing the dedicated wholesale fraud screening that high-AOV transactions demand.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Handshake / Shopify at a glance:**
- Founded: Handshake Corp (2011, New York, NY) by Glen Coates and Mike Elmgreen
- Acquired: By Shopify in May 2019 for under $100M
- Pre-acquisition funding: $39M over 5 rounds (Boldstart Ventures, Emergence Capital, SoftTech VC, Point Nine)
- Platform: B2B wholesale marketplace connecting DTC brands with qualified retailers
- Brands/Retailers: 65,000+ retailers, thousands of curated brands
- Status: Phased down in Oct 2023 after Shopify invested in Faire; domain redirects to Shopify wholesale supplier discovery
- Parent company: Shopify (SHOP on NYSE/TSX)
- Shopify Revenue: $11.6B FY2025 (+30% YoY)
- Shopify GMV: $378.4B FY2025 (+29.5% YoY)
- Shopify B2B GMV Growth: +140% in 2024, +101% in Q2 2025 YoY
- Shopify Employees: ~17,000+
- Shopify Merchants: 4.6M+ across 170+ countries

**Key 2025/2026 milestones:**
- Shopify B2B GMV grew 140% in 2024, then another 101% YoY in Q2 2025
- Shopify Payments enabled in 23+ countries, with 11 new countries added recently
- $2B free cash flow and $2B share repurchase program launched
- Shopify Plus B2B features: Company accounts, custom pricing, net terms (Net 15/30/60)
- Handshake domain now redirects to Shopify wholesale supplier discovery tool
- Faire became Shopify's recommended wholesale marketplace partner

**Product suite (Handshake/Shopify B2B):**
- Handshake Marketplace: Wholesale discovery and ordering (U.S. only)
- Shopify B2B Channel: Native wholesale for Shopify Plus merchants
- Shop Pay: Accelerated checkout (B2C focused)
- Shopify Payments: Native gateway powered by Stripe
- Shopify Markets: Cross-border selling infrastructure
- Shopify POS: In-person wholesale ordering

**Confirmed PSPs / Payment Rails:**
- Shopify Payments: Native payment gateway (powered by Stripe)
- Stripe: Underlying payment processor for Shopify Payments
- Visa / Mastercard / Amex: Card networks
- PayPal: Alternative payment option
- Shop Pay: Accelerated checkout
- Apple Pay / Google Pay: Digital wallets (via Shopify Payments)
- Manual payment methods: Checks, invoices, bank transfers (Shopify Plus B2B only)
- No payment orchestrator detected
- No ACH integration in Handshake marketplace checkout

**Payment Processing Details:**
- Handshake marketplace: Credit card only at checkout
- Shopify Payments rates: ~2.9% + $0.30 (Basic), lower for Plus
- Third-party gateway surcharge: 2% additional if not using Shopify Payments
- B2B net terms: Available on Shopify Plus (Net 15/30/60) but not in Handshake checkout
- International: Shopify Payments available in 23+ countries
- Local APMs: iDEAL, Bancontact, Sofort, SEPA Direct Debit (EU markets only via Shopify Payments)

**Key Meeting Angles:**
1. **Credit card only checkout kills B2B margin** | Wholesale orders at $1,000+ AOV paying 2.9% card fees when ACH costs pennies; Handshake has no bank transfer option
2. **U.S. only while Shopify is global** | Shopify serves 170+ countries and B2B GMV grew 140%, but Handshake cannot process a single cross-border wholesale order
3. **140% B2B growth needs payment infrastructure** | Shopify's fastest-growing segment runs on basic card processing with no orchestration, failover, or multi-acquirer routing
4. **Single gateway dependency** | All payments route through Shopify Payments/Stripe; one outage blocks all wholesale revenue with no fallback
5. **No wholesale fraud layer** | High-AOV B2B orders from new buyers have no dedicated risk scoring; brands absorb chargebacks
6. **Net terms gap in marketplace** | Shopify Plus supports net terms, but Handshake's marketplace checkout does not, pushing invoicing offline
7. **Faire competitive threat** | Faire ($5.2B valuation, $3B GMV) offers integrated B2B payments, trade credit, and international reach
8. **$378B GMV platform, basic payment stack** | Shopify's ecosystem processes over a third of a trillion dollars annually with minimal payment optimization

**Sources:**
- [Shopify Q4 2025 Financial Results (Shopify News)](https://www.shopify.com/news/shopify-q4-2025-financial-results)
- [Shopify Revenue and GMV 2025 (Digital Commerce 360)](https://www.digitalcommerce360.com/article/shopify-revenue-gmv/)
- [Shopify Revenue B2B Sales AI 2025 (Digital Commerce 360)](https://www.digitalcommerce360.com/2026/02/12/shopify-revenue-b2b-sales-ai-2025/)
- [Shopify Q4 2025 Earnings (CNBC)](https://www.cnbc.com/2026/02/11/shopify-shop-earnings-q4-2025.html)
- [Shopify Acquired Handshake (TechCrunch)](https://techcrunch.com/2019/05/23/shopify-quietly-acquired-handshake-an-e-commerce-platform-for-b2b-wholesale-purchasing/)
- [Shopify Acquires Handshake (BetaKit)](https://betakit.com/shopify-acquires-handshake-marking-its-third-acquisition-in-six-months/)
- [Handshake Crunchbase Profile](https://www.crunchbase.com/organization/handshake-5)
- [Shopify Handshake Guide (Dario Markovic)](https://dariomarkovic.com/shopify-handshake)
- [Handshake B2B Marketplace (Radiant)](https://byradiant.com/blog/handshake-shopifys-new-wholesale-marketplace)
- [B2B Wholesale Marketplace Comparison 2026 (Catalist)](https://catalistgroup.co/blog/b2b-wholesale-marketplace-comparison-2026/)
- [Shopify Payments Supported Countries](https://help.shopify.com/en/manual/payments/shopify-payments/supported-countries)
- [Shopify Local Payment Methods](https://help.shopify.com/en/manual/payments/shopify-payments/local-payment-methods)
- [Shopify B2B Payment Terms](https://help.shopify.com/en/manual/b2b/checkout-and-orders/payment-terms)
- [Shopify B2B Payment Methods](https://help.shopify.com/en/manual/b2b/checkout-and-orders/payment-methods)
- [Faire Revenue and Valuation (Sacra)](https://sacra.com/c/faire/)
- [Shopify Stripe Case Study (Stripe)](https://stripe.com/customers/shopify)
- [Shopify Logo (Wikimedia Commons)](https://commons.wikimedia.org/wiki/File:Shopify_logo_2018.svg)
- [Handshake Wholesale Reviews (Wholesale In a Box)](https://www.wholesaleinabox.com/growingsteadyblog/handshake-wholesale-reviews-and-maker-tips)
