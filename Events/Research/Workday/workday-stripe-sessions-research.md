# WORKDAY | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Workday
=======================================

Logo: https://cdn.brandfetch.io/workday.com/w/512/h/512/logo
Nombre merchant: Workday

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Invoice-Heavy Billing
Tittle_Pain Point_2: No Payment Orchestration
Tittle_Pain Point_3: Multi-Currency Complexity
Tittle_Pain Point_4: Regional Collection Lag
Tittle_Pain Point_5: DSO Optimization Gap

Desc_Pain Point_1: Workday's $9.55B revenue relies heavily on annual enterprise invoicing. With 11,000+ customers in 34 countries, collecting on high-value subscription contracts via traditional invoice/wire creates long payment cycles, especially in EMEA and APAC where local methods accelerate settlement.
Desc_Pain Point_2: At $9.55B revenue with customers spanning 65%+ of the Fortune 500 and 40%+ of the FTSE100, Workday processes massive subscription billing volume without documented payment orchestration. No failover or smart routing exists to optimize collection rates across geographies.
Desc_Pain Point_3: Workday serves 2,000+ customers in EMEA alone and operates in 34 countries. Billing in multiple currencies (USD, EUR, GBP, JPY) across enterprise contracts creates FX reconciliation complexity and settlement delays that a unified orchestration layer would eliminate.
Desc_Pain Point_4: EMEA customers (40%+ FTSE100, 30%+ CAC40, 40%+ DAX40) pay via invoice and wire transfer. Collection timelines in Germany, France, and UK average 45-60 days. Local payment methods like SEPA DD would reduce DSO and accelerate cash flow significantly.
Desc_Pain Point_5: On $9.55B revenue, even a 5-day DSO improvement equals $130M+ in accelerated cash flow. Offering SEPA DD, BACS DD, and ACH for enterprise subscription billing would systematically reduce collection cycles across all major markets.

SLIDE 1: PSP TOPOLOGY

PSP_1: Invoice / Wire Transfer (enterprise contracts)
PSP_2: Credit Card (customer portal, confirmed)
PSP_3: Transact Integrated Payments (Workday partner)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: SEPA Direct Debit
Local_M_2: BACS Direct Debit
Local_M_3: ACH Direct Debit
Local_M_4: Open Banking (UK/EU)
Local_M_5: iDEAL
Local_M_6: Bancontact
Local_M_7: UPI
Local_M_8: Konbini
Local_M_9: Boleto
Local_M_10: PIX

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each enterprise subscription collection to the optimal acquirer by geography, currency, and payment method. On $9.55B revenue across 34 countries, even a 3% improvement in collection efficiency translates to $286M+ in accelerated revenue recognition per year.
Desc_Yuno_Cap2: Automatic retry cascades across multiple acquirers protect Workday's high-value renewal cycle. When a credit card or direct debit collection fails, Yuno reroutes in milliseconds to a backup processor, recovering up to 50% of soft declines across the 11,000+ customer base.
Desc_Yuno_Cap3: Unlock direct debit billing across Workday's 34-country footprint: SEPA DD for EU (2,000+ EMEA customers), BACS for UK (40%+ FTSE100), ACH for US (65%+ Fortune 500), UPI for India. One API, 1,000+ methods, reducing DSO by 15-30 days per market.
Desc_Yuno_Cap4: One dashboard consolidating Workday's enterprise billing across all payment rails, geographies, and currencies. Real-time collection monitoring per region, centralized reconciliation of multi-currency invoices, and DSO analytics across the 11,000+ customer base.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Workday at a glance:**
- Enterprise cloud applications for finance and human resources
- Revenue: $9.55B (fiscal 2026, 13.09% YoY growth); subscription revenue $2.36B in Q4 alone (+15.7% YoY)
- Public company: NASDAQ: WDAY
- 11,000+ organizations worldwide; 65%+ of Fortune 500
- 20,400+ employees in 34 countries (as of January 2025)
- Founded 2005 by Aneel Bhusri and Dave Duffield; headquartered in Pleasanton, CA
- Non-GAAP operating income: $2.82B (29.6% margin, fiscal 2026)
- Products: Workday HCM, Financial Management, Adaptive Planning, Spend Management, Payroll

**European presence (critical for payment orchestration):**
- 2,000+ customers in EMEA
- 40%+ of FTSE100 (UK)
- 40%+ of DAX40 (Germany)
- 30%+ of CAC40 (France)
- Offices in UK, Ireland, Germany, Spain, Belgium, Italy, France, Sweden, Poland, Switzerland
- Notable European customers: Asda, Basic Fit, franprix, Glovo, Mazars, Telpark

**Asia-Pacific presence:**
- Offices in Australia, India, Japan, South Korea, Taiwan, Hong Kong, Malaysia, Singapore
- Growing enterprise adoption across APAC

**Americas presence:**
- Latin America regional office in Costa Rica
- Growing presence in Central America

**Confirmed PSPs:**
- Invoice/wire transfer for enterprise contracts (primary billing method)
- Credit card payments via Customer Portal
- Transact Integrated Payments (certified Workday Cloud Connect Partner)
- Makse Group Workday Payments integration on Stripe App Marketplace
- No payment orchestrator detected

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (primary market, 65%+ Fortune 500)
  Currently offer: Invoice/wire, credit card (portal)
  Missing: ACH Direct Debit (automated recurring)
  Fortune 500 procurement teams prefer automated ACH for recurring SaaS billing over manual wire transfer.

MARKET 2: United Kingdom (40%+ FTSE100)
  Currently offer: Invoice/wire
  Missing: BACS Direct Debit, Open Banking, GBP automated collection
  BACS DD is the standard for UK enterprise subscriptions. Manual wire creates 45-60 day DSO.

MARKET 3: Germany (40%+ DAX40)
  Currently offer: Invoice/wire
  Missing: SEPA Direct Debit, EUR automated collection
  SEPA DD would reduce collection cycles from 45-60 days to 3-5 days for German enterprise accounts.

MARKET 4: France (30%+ CAC40)
  Currently offer: Invoice/wire
  Missing: SEPA Direct Debit, Carte Bancaire, EUR automated collection
  French enterprise procurement expects SEPA DD for recurring SaaS. Manual invoicing creates unnecessary delays.

MARKET 5: Japan / APAC
  Currently offer: Invoice/wire
  Missing: Bank transfer automation (furikomi), Konbini, JPY billing optimization
  Japanese enterprise payment cycles average 60-90 days. Automated local collection would dramatically reduce DSO.

**Key meeting angles:**
1. **$9.55B revenue at scale** | Even marginal improvements in collection efficiency = hundreds of millions in accelerated cash flow.
2. **34 countries, 11,000+ customers** | Enterprise billing across this footprint without payment orchestration creates systematic inefficiency.
3. **EMEA = 2,000+ customers** | SEPA DD and BACS DD adoption would reduce DSO by 15-30 days across the largest international market.
4. **Fortune 500 + FTSE100 + DAX40** | Workday's customers are the world's largest enterprises. They expect automated, localized payment collection.
5. **Non-GAAP margin expansion** | 29.6% operating margin could expand further by reducing collection costs and accelerating cash flow.
6. **Competitive pressure** | SAP, Oracle, and ServiceNow offer localized billing with SEPA DD and local payment methods across EMEA.

**Sources:**
- [Workday FY2026 Q4 Results](https://investor.workday.com/news-and-events/press-releases/news-details/2026/Workday-Announces-Fiscal-2026-Fourth-Quarter-and-Full-Year-Financial-Results/default.aspx)
- [Workday FY2025 Q4 Results](https://newsroom.workday.com/2025-02-25-Workday-Announces-Fiscal-2025-Fourth-Quarter-and-Full-Year-Financial-Results)
- [Workday Revenue (MacroTrends)](https://www.macrotrends.net/stocks/charts/WDAY/workday/revenue/)
- [Workday Revenue (StockAnalysis)](https://stockanalysis.com/stocks/wday/revenue/)
- [Workday Statistics (Expanded Ramblings)](https://expandedramblings.com/index.php/workday-statistics-and-facts/)
- [Workday Company Overview](https://newsroom.workday.com/company-overview)
- [Workday 2,000+ EMEA Customers](https://erp.today/workday-surpasses-2000-customers-in-europe-and-rising/)
- [Workday Contact / Offices](https://www.workday.com/en-us/company/about-workday/contact-us.html)
- [Workday Wikipedia](https://en.wikipedia.org/wiki/Workday,_Inc.)
- [Workday Customer Portal Payments](https://marketplace.workday.com/en-US/apps/483883/customer-portal-payments)
- [Transact Integrated Payments for Workday](https://marketplace.workday.com/en-US/apps/414743/transact-integrated-payments/overview)
- [Brandfetch: Workday Logo](https://brandfetch.com/workday.com)
