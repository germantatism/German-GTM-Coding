# HEVO DATA | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Hevo Data
=======================================

Logo: https://cdn.brandfetch.io/hevodata.com/w/512/h/512/logo
Nombre merchant: Hevo Data

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Credit Card Only Billing
Tittle_Pain Point_2: No Failover on Renewals
Tittle_Pain Point_3: India Revenue at Risk
Tittle_Pain Point_4: Usage Spike Bill Shock
Tittle_Pain Point_5: FX Settlement Overhead

Desc_Pain Point_1: Only cards and wire (annual). Customers in India, Germany, Japan cannot pay via UPI, SEPA, Konbini. Creates procurement friction for teams spending $3,600+/yr.
Desc_Pain Point_2: Event-based pricing at $299+/mo, no overage cap. Failed Stripe renewals compound with metered overages. No retry cascade recovers declined charges on alt rails.
Desc_Pain Point_3: HQ in Bangalore with large Indian base, yet Indians pay USD via international cards. UPI and INR invoicing would cut friction in Hevo's home market.
Desc_Pain Point_4: High-change-rate tables spike bills unpredictably. Overage charges hitting card limits get declined with no retry or alternative routing to capture revenue.
Desc_Pain Point_5: USD-only billing globally. India, EU, UK, Japan absorb FX every cycle. Fivetran and Airbyte offer localized billing, creating a switching incentive.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe
PSP_2: Wire Transfer (annual plans only)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: UPI
Local_M_2: SEPA Direct Debit
Local_M_3: ACH Direct Debit
Local_M_4: iDEAL
Local_M_5: Konbini
Local_M_6: BLIK
Local_M_7: Boleto
Local_M_8: Bancontact
Local_M_9: BACS Direct Debit
Local_M_10: Sofort

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each renewal and overage charge to the best acquirer by card BIN, issuer, and geography. With 2,000+ data teams in 45+ countries on event-based pricing, a 3% auth uplift on renewals protects significant MRR from involuntary churn.
Desc_Yuno_Cap2: When Stripe declines a subscription or overage charge, Yuno cascades to an alternative processor in milliseconds. Up to 50% recovery on soft declines, especially critical during usage-spike cycles where charges exceed normal thresholds and trigger bank flags.
Desc_Yuno_Cap3: Unlock billing globally: UPI for India (home market), SEPA for EU data teams, ACH for US enterprises, Konbini for Japan. One API, 1,000+ methods, zero engineering sprints per market. Remove procurement friction that pushes teams to competitors.
Desc_Yuno_Cap4: One dashboard consolidating Hevo's subscription billing and overage charges across all processors and payment methods. Real-time approval monitoring per geography and plan tier, centralized reconciliation, and churn analytics tied directly to payment failures by customer segment.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Hevo Data at a glance:**
- No-code, bi-directional data pipeline platform (ETL, ELT, Reverse ETL)
- Founded: 2017 by Manish Jethani and Sourabh Agarwal
- Dual HQ: San Francisco, CA and Bengaluru, India (primary office: 1177, 5th Main Rd, HSR Layout, Bengaluru)
- Revenue: ~$46.9M (October 2024 estimate)
- Employees: ~241 as of March 2026
- Total funding: $83M (latest: $40M Series B, December 2021)
- 2,000+ data teams in 45+ countries
- 150+ pre-built connectors with automatic schema detection
- 4.9/5 stars (200+ ratings)
- Pricing: Starter from $299/month, event-based with metered overages
- Competitors: Fivetran, Airbyte, Integrate.io, Informatica

**Product details:**
- Ingestion, transformation (dbt, SQL, Hevo Transformer), and destination sync
- Change Data Capture (CDC) support
- Saves ~10 hours engineering time per week and 10x faster reporting
- Setup in ~5 minutes for standard connectors
- Supports PostgreSQL, MySQL, MongoDB, Salesforce, HubSpot, Google Analytics, Facebook Ads, Shopify, Stripe, BigQuery, Redshift, and more

**Confirmed PSPs:**
- Stripe: primary payment gateway for website signups
- Wire transfer: available only for annual plans
- Accepts: Visa, Mastercard, Amex, Discover, JCB, Diners Club
- No payment orchestrator detected
- AWS Marketplace billing available (with option to switch to Stripe-based invoicing)

**Customer industries:**
- Information Technology and Services: 28%
- Computer Software: 17%
- Financial Services: 7%
- Internet: 6%
- 50% medium-sized companies, 15% large (1,000+ employees), 28% small (<50)

**Top 5 Markets Gap Analysis:**

MARKET 1: India (Home market, HQ in Bengaluru)
  Currently offer: International credit cards (USD billing)
  Missing: UPI, RuPay, net banking, INR invoicing
  UPI processes 75%+ of Indian digital payments. Indian SaaS buyers paying $3,600+/year in USD face unnecessary FX costs and card friction.

MARKET 2: United States (Primary revenue market)
  Currently offer: Credit cards, wire transfer (annual only)
  Missing: ACH Direct Debit, Apple Pay
  US enterprise data teams prefer ACH for recurring SaaS spend. Wire-only alternatives for non-card payments limit flexibility.

MARKET 3: Europe (Germany, Netherlands, France)
  Currently offer: Credit cards
  Missing: SEPA Direct Debit, iDEAL, Bancontact, Sofort, BLIK
  35% card penetration in Germany. European IT teams strongly prefer SEPA DD for recurring data infrastructure spend.

MARKET 4: United Kingdom
  Currently offer: Credit cards
  Missing: BACS Direct Debit, Open Banking
  BACS DD is the standard for UK B2B SaaS subscriptions. Missing it creates procurement friction for UK data teams.

MARKET 5: Japan
  Currently offer: Credit cards
  Missing: Konbini, bank transfer (furikomi), JCB optimization
  Japanese enterprise procurement requires local payment methods. Data teams at Japanese firms face internal approval barriers with USD card-only billing.

**Key meeting angles:**
1. **Event-based pricing risk** | Usage spikes cause unexpected charges that fail on card limits. Smart retry logic captures revenue that would otherwise be lost
2. **India is the home market** | Hevo HQ is in Bengaluru but Indian customers cannot pay with UPI or INR. Localizing payments in the home market is low-hanging fruit
3. **2,000+ teams in 45+ countries** | Global customer base with only credit card billing. Local payment methods remove procurement friction across geographies
4. **Overage charges compound** | No cap on metered overages means high-value charges at risk of decline. Failover protects the most valuable billing events
5. **Competitive pressure** | Fivetran and Airbyte offer localized billing. Payment friction is a switching trigger for price-sensitive data teams
6. **AWS Marketplace dependency** | Some customers bill through AWS to avoid Stripe. Yuno orchestration could reduce this leakage by offering local methods directly

**Sources:**
- [Hevo Data Official Website](https://hevodata.com/)
- [Hevo Data Billing Documentation](https://docs.hevodata.com/account-management/billing/setting-up-plan-billing-payments/)
- [Hevo Data Pricing Plans](https://docs.hevodata.com/account-management/billing/pricing-plans/)
- [Hevo Data Billing FAQs](https://docs.hevodata.com/faqs/billing/)
- [Hevo Switching to Stripe-Based Invoicing](https://docs.hevodata.com/getting-started/subscribing-via-aws-mktplace/switching-to-stripe/)
- [Hevo Data Stripe Source Connector](https://docs.hevodata.com/sources/fna-analytics/stripe/)
- [Hevo Data Customer Stories](https://hevodata.com/customers/)
- [Hevo Data Design/Brand Guidelines](https://design.hevodata.com/)
- [Brandfetch: Hevo Data Logo](https://brandfetch.com/hevodata.com)
- [Growjo: Hevo Data Revenue](https://growjo.com/company/Hevo_Data)
- [GetLatka: Hevo Data Revenue](https://getlatka.com/companies/hevo-data)
- [Integrate.io: Hevo Data Review](https://www.integrate.io/blog/hevo-data-review/)
- [Enlyft: Hevo Data Market Share](https://enlyft.com/tech/products/hevo-data)
