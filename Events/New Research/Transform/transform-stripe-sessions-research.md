# TRANSFORM (dbt Labs) | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Transform
=======================================

Logo: https://cdn.brandfetch.io/getdbt.com/w/512/h/512/logo
Nombre merchant: Transform (dbt Labs)

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Card-Only SaaS Billing
Tittle_Pain Point_2: No Failover on Renewals
Tittle_Pain Point_3: Global Billing Gap
Tittle_Pain Point_4: FX Settlement Friction
Tittle_Pain Point_5: Involuntary Churn Risk

Desc_Pain Point_1: dbt Cloud bills Starter customers via credit card only. Enterprise clients in 43 countries spanning Europe, APAC, and LATAM cannot pay with SEPA, UPI, or Boleto. With $100M+ ARR at stake, forcing global buyers onto USD card rails adds unnecessary procurement friction.
Desc_Pain Point_2: At $100M+ ARR on auto-renewing annual contracts, a single acquirer decline on renewal day means lost enterprise revenue. No documented retry cascade exists to recover failed subscription charges across dbt Cloud's self-serve and enterprise tiers.
Desc_Pain Point_3: 27% YoY growth in international markets means more customers outside the US each quarter. Yet billing offers zero local payment methods for EU, India, or LATAM buyers, creating friction for the 5,000+ customer base now spanning 43 countries.
Desc_Pain Point_4: dbt Cloud bills exclusively in USD. Enterprise buyers in EUR, GBP, INR, and BRL markets absorb FX conversion costs on every monthly or annual invoice. Competitors offering local currency billing gain a procurement advantage at renewal time.
Desc_Pain Point_5: SaaS involuntary churn from failed card payments averages 3-5% of MRR. On $100M+ ARR, even 1% involuntary churn equals $1M+ in recoverable revenue through smarter retry logic and intelligent payment routing across acquirers.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (confirmed via billing documentation)
PSP_2: Credit Card (self-serve plans)
PSP_3: Invoice / Wire (enterprise contracts)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: SEPA Direct Debit
Local_M_2: ACH Direct Debit
Local_M_3: UPI
Local_M_4: iDEAL
Local_M_5: Boleto
Local_M_6: BLIK
Local_M_7: Konbini
Local_M_8: Bancontact
Local_M_9: OXXO
Local_M_10: PIX

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each enterprise renewal to the best-performing acquirer by card BIN, issuer, and geography. With $100M+ ARR across 5,000+ customers in 43 countries, even a 3% auth uplift on renewals recovers $3M+ in otherwise lost annual recurring revenue per year.
Desc_Yuno_Cap2: Automatic retry cascades across multiple acquirers protect dbt Cloud's high-value renewal cycle. When Stripe declines an annual enterprise charge, Yuno reroutes in milliseconds to a backup processor, recovering up to 50% of soft declines and reducing involuntary churn.
Desc_Yuno_Cap3: Unlock enterprise billing across dbt Labs' 43-country footprint: SEPA Direct Debit for EU, UPI for India, Boleto/PIX for Brazil, ACH for US enterprises, Konbini for Japan. One API, 1,000+ methods, zero engineering sprints per market.
Desc_Yuno_Cap4: One dashboard consolidating dbt Cloud's subscription billing across all processors and methods. Real-time approval monitoring per geography and plan tier, centralized reconciliation, and cohort-level churn analytics tied to payment failures across self-serve and enterprise.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Transform / dbt Labs at a glance:**
- Transform was a metrics store/semantic layer company, acquired by dbt Labs in February 2023
- dbt Labs is the creator of dbt (data build tool), the standard for data transformation
- Revenue: $100M+ ARR as of February 2025 (scaled from $2M to $100M+ in four years)
- Valuation: $4.2B (Series D, February 2022); merging with Fivetran for combined ~$600M revenue
- Total funding: $414.4M across multiple rounds; Series D of $222M led by Altimeter Capital
- 5,000+ paying customers; 85% YoY growth in Fortune 500 adoption
- 1,015 employees as of January 2026
- Customers in 43 countries with 27% YoY growth in international markets
- Offices in Philadelphia (HQ), Austin, and Dublin
- Plans: Developer (free), Starter ($100/user/month), Enterprise, Enterprise+ (custom)
- Notable customers: Conde Nast, HubSpot, Nasdaq, Siemens

**MetricFlow / Transform integration:**
- Transform's MetricFlow was merged into the dbt Semantic Layer after acquisition
- Enables centralized metric definitions (revenue, churn, customer count) across all analytics tools
- Transform's founding team (ex-Airbnb Data Platform) joined dbt Labs
- Transform had raised $29M from Index Ventures and Redpoint before acquisition

**Confirmed PSPs:**
- Credit card billing confirmed for Starter plan (monthly, self-serve)
- Enterprise plans: annual invoice billing
- Usage-based overages calculated in arrears
- No payment orchestrator detected
- Marketplace transactions via AWS, GCP growing 190%+ YoY

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (~55% of customers)
  Currently offer: Credit card (Visa/MC/Amex)
  Missing: ACH Direct Debit, wire transfer automation
  US enterprises strongly prefer ACH for SaaS billing. $100K+ contracts paid by card create unnecessary procurement friction.

MARKET 2: United Kingdom / Ireland (significant EU hub)
  Currently offer: Credit card (USD billing)
  Missing: BACS Direct Debit, Open Banking, GBP invoicing
  Dublin office serves EU operations. UK/Ireland enterprises expect BACS DD or Open Banking for recurring SaaS spend.

MARKET 3: Germany / DACH
  Currently offer: Credit card (USD billing)
  Missing: SEPA Direct Debit, Sofort, EUR invoicing
  ~35% card penetration in Germany. Enterprises strongly prefer SEPA DD for recurring payments.

MARKET 4: India / APAC (expansion focus)
  Currently offer: Credit card (USD billing)
  Missing: UPI, RuPay, INR invoicing, net banking
  APAC expansion is a strategic priority. UPI processes 75%+ of Indian digital payments.

MARKET 5: Brazil / LATAM
  Currently offer: Credit card (USD billing)
  Missing: PIX, Boleto, BRL invoicing
  LATAM data teams are rapidly adopting dbt. PIX is now Brazil's dominant payment method.

**Key meeting angles:**
1. **$100M+ ARR renewal protection** | Every failed renewal charge means lost annual contracts. Smart retry cascades directly protect ARR.
2. **43-country footprint with zero local methods** | 27% YoY international growth without local payment infrastructure creates conversion friction.
3. **Fivetran merger = scale leap** | Combined $600M revenue entity needs consolidated global payment orchestration from day one.
4. **Fortune 500 enterprise mix** | 85% YoY growth in F500 means procurement teams demanding ACH, SEPA, and invoice workflows.
5. **Marketplace transactions growing 190%+** | Multi-channel billing complexity (direct + AWS/GCP) needs unified reconciliation.
6. **Competitive pressure** | Snowflake, Databricks offer localized billing in multiple currencies. dbt Cloud risks losing deals on procurement friction.

**Sources:**
- [dbt Labs $100M ARR Milestone](https://www.getdbt.com/blog/dbt-labs-100m-arr-milestone)
- [dbt Labs Acquires Transform](https://www.getdbt.com/blog/dbt-acquisition-transform)
- [dbt Labs Press Release: Transform Acquisition](https://www.prnewswire.com/news-releases/dbt-labs-signs-definitive-agreement-to-acquire-transform-accelerating-development-of-the-dbt-semantic-layer-301741620.html)
- [dbt Cloud Billing Documentation](https://docs.getdbt.com/docs/cloud/billing)
- [dbt Cloud Pricing](https://www.getdbt.com/pricing)
- [dbt Labs About Us](https://www.getdbt.com/about-us)
- [dbt Labs Global Partner Program](https://finance.yahoo.com/news/dbt-labs-launches-reimagined-global-130000542.html)
- [TechCrunch: dbt Acquires Transform](https://techcrunch.com/2023/02/08/dbt-acquires-transform/)
- [Sacra: dbt Labs Revenue](https://sacra.com/c/dbt/)
- [Brandfetch: dbt Labs Logo](https://brandfetch.com/dbt.com)
- [Tracxn: dbt Labs Profile](https://tracxn.com/d/companies/dbt-labs/__uetvGc5wXa2wwZOwATP8qaOeg7oS0Dcnlxf8-bQRXS4)
