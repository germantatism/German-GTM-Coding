# FLEXPORT | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Flexport
═══════════════════════════════════════

Logo: https://www.flexport.com/company/logo/
Nombre merchant: Flexport

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Multi-Currency Invoicing
Tittle_Pain Point_2: Single Acquirer for Cards
Tittle_Pain Point_3: No Local B2B Methods
Tittle_Pain Point_4: Customs Duty Friction
Tittle_Pain Point_5: Disbursement Fee Overhead

Desc_Pain Point_1: $3.3B+ revenue from 10K+ customers in 112 countries but payment acceptance limited to ACH, cards, and PayPal. International shippers paying USD invoices face FX costs and cross-border wire complexity for every shipment settlement.
Desc_Pain Point_2: Stripe processes card payments with no failover acquirer. For a logistics platform handling high-value freight invoices and customs duties globally, a single card processing path creates concentration risk on every transaction.
Desc_Pain Point_3: Zero local payment methods for international shippers: no SEPA Instant for EU forwarders, no Pix for Brazilian importers, no UPI for Indian manufacturers. 20%+ of customers are outside the US and have limited payment options.
Desc_Pain Point_4: Customs duties require separate ACH setup with 7-10 day processing. Shippers without direct CBP ACH accounts pay disbursement fees for Flexport to front duties on their behalf, adding cost and friction to every import.
Desc_Pain Point_5: Flexport charges disbursement service fees when advancing customs duties and taxes on behalf of clients. International clients without US banking access disproportionately absorb these fees due to limited payment method availability.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe
PSP_2: PayPal
PSP_3: Plaid (bank auth)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: SEPA Instant
Local_M_2: Pix
Local_M_3: UPI
Local_M_4: BACS Direct Debit
Local_M_5: iDEAL
Local_M_6: Boleto
Local_M_7: Konbini
Local_M_8: SPEI
Local_M_9: Bancontact
Local_M_10: PayNow

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across Stripe and PayPal based on invoice amount, customer country, and payment method. With $3.3B+ revenue from freight invoices averaging thousands of dollars each, even a 3% auth uplift on card payments recovers millions in faster collections.
Desc_Yuno_Cap2: Automatic cascade breaks Flexport's single-Stripe card dependency. When Stripe declines a high-value freight payment, Yuno reroutes to the next best acquirer in milliseconds, ensuring shipment-critical payments clear without delay. Up to 50% recovery on failed transactions.
Desc_Yuno_Cap3: Activates B2B payment methods across Flexport's 112-country network: SEPA Instant for EU freight partners, Pix for Brazilian importers, UPI for Indian manufacturers, BACS DD for UK logistics, Konbini for Japanese shippers. One API, 1,000+ methods. Reduces disbursement fee friction.
Desc_Yuno_Cap4: One dashboard unifying Stripe cards, ACH via Plaid, PayPal, and future local methods across freight, fulfillment, and customs billing. Real-time payment monitoring for $3.3B+ in annual transactions across 112 countries. NOVA intelligence provides 75% faster anomaly detection on high-value logistics payments.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Flexport at a glance:**
- Revenue: $3.3B+ annually; targeting organic profitability in 2026
- 10,000+ customers across 112 countries; 40,000+ cumulative customers served
- ~$19B of merchandise moved through platform historically
- 2,800+ employees across 89 countries
- Fulfillment: 5 US centers (NJ, LA, Dallas, Atlanta, Chicago)
- CEO: Ryan Petersen (Founder, returned September 2023 after Dave Clark departure)
- CFO: Stuart Leung; President International: Sanne Manders; CRO customs/trade: Nader Kabbani
- Total funding: $2.7B from SoftBank, a16z, Shopify, Founders Fund
- Valuation: ~$2.5B (secondary market May 2025), down from $8B peak (Feb 2022)
- Shopify holds 17% stake after Flexport acquired Shopify Logistics in 2023
- E-commerce fulfillment doubled revenue in early 2025 due to tariff-driven demand
- Partners: Shopify, Walmart, SHEIN Marketplace; HK Air Cargo for Asia expansion
- Parcel delivery to 200+ countries

**Confirmed PSPs:**
- Stripe: primary card processor and user authentication (confirmed via help docs)
- PayPal: accepted payment method
- Plaid: bank login/verification for ACH payments
- ACH Direct Debit: for freight invoices and customs duties
- No SEPA, no local methods, no wire transfer acceptance
- No payment orchestrator detected

**Payment methods accepted:**
- ACH direct debit (via Plaid + Stripe micro-deposit verification)
- Credit/debit cards (via Stripe)
- PayPal
- NOT accepted: prepaid cards, direct wire transfers

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (80% of customers)
  Accepted: ACH, Visa/MC/Amex via Stripe, PayPal
  Missing: Same-day ACH, real-time payments (RTP/FedNow)
  High-value freight invoices benefit from instant settlement options.

MARKET 2: Netherlands (4.3% of customers, EU logistics hub)
  Accepted: Cards via Stripe, PayPal
  Missing: SEPA Instant, iDEAL
  Rotterdam is Europe's largest port. Dutch freight partners need SEPA for B2B payments.

MARKET 3: Canada (3.9% of customers)
  Accepted: Cards via Stripe, PayPal
  Missing: Interac e-Transfer, PAD (pre-authorized debit)
  Cross-border US-Canada freight is massive; local debit methods reduce friction.

MARKET 4: China/Hong Kong (major origin market for freight)
  Accepted: Cards via Stripe, PayPal
  Missing: Alipay, WeChat Pay, UnionPay
  Chinese manufacturers and exporters are key origin shippers. Local methods accelerate collections.

MARKET 5: Germany/UK (European freight markets)
  Accepted: Cards via Stripe, PayPal
  Missing: SEPA DD, BACS DD, Giropay
  B2B freight payments in Europe default to bank transfers; SEPA DD enables automated recurring billing.

**Key meeting angles:**
1. **High-value B2B transactions** | Freight invoices average thousands of dollars; auth rate optimization on large transactions has outsized impact
2. **112-country coverage gap** | Global logistics company with only ACH + cards + PayPal for 112 markets
3. **Customs duty payment friction** | Disbursement fees charged when clients lack US ACH; local methods reduce this cost
4. **Profitability pressure** | Targeting organic profitability in 2026; payment efficiency directly impacts margin
5. **Shopify logistics integration** | Fulfillment business doubling; growing e-commerce payments volume needs scalable infra
6. **Ryan Petersen's tech-first vision** | CEO who built API-first logistics platform will appreciate orchestration-layer pitch
7. **Competitor comparison** | Traditional freight forwarders (Kuehne+Nagel, DHL) offer more B2B payment flexibility

**Sources:**
- [Flexport Help: Payment Methods FAQ](https://support.portal.flexport.com/hc/en-us/articles/4421201578007)
- [Flexport Help: Billing Portal](https://support.portal.flexport.com/hc/en-us/articles/115003185313)
- [Flexport Help: Customs Duties ACH](https://www.flexport.com/help/31-customs-duties-payment-ach/)
- [Flexport Help: Disbursement Fee](https://support.portal.flexport.com/hc/en-us/articles/22605334891287)
- [Flexport Payment Terms](https://www.flexport.com/terms-and-conditions/payment_terms_and_conditions/)
- [Flexport About Us](https://www.flexport.com/company/about-us/)
- [Flexport Logo](https://www.flexport.com/company/logo/)
- [Sacra: Flexport Revenue & Valuation](https://sacra.com/c/flexport/)
- [Yahoo Finance: Flexport 2025 Profit from Convoy](https://finance.yahoo.com/news/flexport-projects-2025-profit-convoy-153000509.html)
- [Contrary Research: Flexport](https://research.contrary.com/company/flexport)
- [Flexport Wikipedia](https://en.wikipedia.org/wiki/Flexport)
- [Flexport Products Launch](https://www.prnewswire.com/news-releases/flexport-unveils-20-tech-and-ai-powered-products-to-modernize-global-supply-chains-302383593.html)
