# SERVICENOW | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: ServiceNow
=======================================

Logo: https://cdn.brandfetch.io/servicenow.com/w/512/h/512/logo
Nombre merchant: ServiceNow

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: USD-Only Store Billing
Tittle_Pain Point_2: 37% Non-US Revenue Gap
Tittle_Pain Point_3: No Failover on Renewals
Tittle_Pain Point_4: Enterprise Invoice Limits
Tittle_Pain Point_5: APAC Payment Friction

Desc_Pain Point_1: Store charges USD only via credit card. Enterprise clients paying $1M+ subscriptions face card limits, FX surcharges, and procurement violations.
Desc_Pain Point_2: 37% of $13.28B revenue is non-US ($3.4B EMEA, $1.53B APAC) with no local payment methods. International clients forced through USD card or manual PO.
Desc_Pain Point_3: 8,800+ enterprise renewals at $1.5M avg ACV. A single card decline or processing error risks losing a client. No multi-acquirer failover exists.
Desc_Pain Point_4: 603 accounts at $5M+ ACV need automated local invoicing and multi-currency settlement. Manual PO processes cannot scale for global enterprises.
Desc_Pain Point_5: APAC is fastest-growing (+23% YoY, $1.53B). Japan expects Konbini, India needs UPI, Australia prefers BPAY. USD-only billing limits growth.

SLIDE 1: PSP TOPOLOGY

PSP_1: Credit Card (ServiceNow Store)
PSP_2: Purchase Order / Wire Transfer (enterprise)
PSP_3: AWS Marketplace (indirect channel)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: SEPA Direct Debit (Europe)
Local_M_2: Konbini (Japan)
Local_M_3: UPI (India)
Local_M_4: BPAY (Australia)
Local_M_5: iDEAL (Netherlands)
Local_M_6: Boleto (Brazil)
Local_M_7: BACS Direct Debit (UK)
Local_M_8: Bancontact (Belgium)
Local_M_9: BLIK (Poland)
Local_M_10: PIX (Brazil)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each renewal to the best acquirer by card BIN, geography, and currency. With $13.28B subscription revenue across 8,800+ clients in 50+ countries, a 3% auth uplift recovers $400M+ in at-risk recurring revenue.
Desc_Yuno_Cap2: When a $5M+ ACV renewal declines, Yuno reroutes in milliseconds to a backup processor. Up to 50% recovery on soft declines, protecting the subscription base driving 98%+ of ServiceNow's revenue.
Desc_Yuno_Cap3: SEPA for the $3.4B EMEA region, Konbini for Japan, UPI for India, BPAY for Australia. One API, 1,000+ methods, zero engineering per market. Removes procurement friction for 37% of revenue outside North America.
Desc_Yuno_Cap4: One dashboard for subscription billing across all processors, methods, and geographies. Real-time approval monitoring per region, centralized reconciliation in 50+ countries, renewal health analytics by ACV tier.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**ServiceNow at a glance:**
- Cloud computing platform for automated business workflows (ITSM, ITOM, HR, CSM, SecOps)
- NYSE: NOW | S&P 100 and S&P 500 constituent
- Revenue: $13.28B (FY2025, +20.8% YoY); forecasted $15B+ for 2026
- Q1 2026: revenue growth accelerated to 22% YoY
- Founded: 2003 by Fred Luddy
- Headquarters: Santa Clara, California
- Employees: 29,732 (Q1 2026); 9,556 in R&D
- Customers: 8,800+ globally, including 85% of Fortune 500
- 603 customers with $5M+ ACV (Q2 2025)
- 2,109 customers with $1M+ ACV (average $5M ACV)
- Projected: 3,066 customers with $1M+ ACV by 2026
- "Rule of 50" score: 54% (only company in peer group exceeding this benchmark)
- Recognized as leader by Gartner, Forrester, and IDC across multiple categories

**Revenue by geography (FY2025):**
- North America: $8.35B (63%)
- EMEA: $3.40B (26%)
- Asia Pacific & Other: $1.53B (11%, fastest growing at +23% YoY)

**Revenue by product (FY2025):**
- Technology Workflows: 47%
- Customer & Employee Workflows: 31%
- Creator Workflows & Others: 22%

**Confirmed PSPs & billing infrastructure:**
- ServiceNow Store: credit card payments in USD only (12-month minimum subscription)
- Enterprise procurement: Purchase Order (PO) process with manual quote-to-PO workflow
- AWS Marketplace: available as indirect billing channel
- Zuora: likely subscription billing platform (based on industry patterns and Zuora/ServiceNow ecosystem references)
- No payment orchestrator detected
- No public mention of Stripe, Adyen, or specific payment gateway

**How customers pay:**
- Credit card (ServiceNow Store, USD only)
- Purchase Order with invoice (enterprise, manual process)
- AWS Marketplace billing (cloud commitment credits)
- Capchase financing (third-party SaaS payment plans)

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (63% of revenue, ~$8.35B)
  Currently offer: Credit card, purchase order, wire transfer
  Missing: ACH Direct Debit for automated subscription billing
  Fortune 500 CFOs prefer ACH over credit card for $1M+ annual SaaS subscriptions. Manual PO process does not scale.

MARKET 2: United Kingdom & Ireland (~$1B+ estimated)
  Currently offer: Credit card (USD), purchase order
  Missing: BACS Direct Debit, Open Banking, GBP invoicing
  UK enterprises (HSBC, BP, Rolls-Royce) require GBP billing and BACS DD for recurring SaaS spend. USD credit card creates procurement friction.

MARKET 3: Germany / DACH (~$800M+ estimated)
  Currently offer: Credit card (USD), purchase order
  Missing: SEPA Direct Debit, Sofort, EUR invoicing, Lastschrift
  German enterprises (Siemens, SAP, Allianz) strongly prefer SEPA DD or invoice payment. Credit card penetration is ~35% in DACH.

MARKET 4: Japan (~$500M+ estimated)
  Currently offer: Credit card (USD), purchase order
  Missing: Konbini, bank transfer (furikomi), JCB optimization, JPY invoicing
  Japanese enterprise procurement requires local bank transfer or dedicated invoice. USD card billing violates many corporate payment policies.

MARKET 5: Australia (~$400M+ estimated)
  Currently offer: Credit card (USD), purchase order
  Missing: BPAY, Direct Debit, AUD invoicing
  BPAY is the standard for Australian B2B payments. AUD invoicing is expected for recurring enterprise SaaS contracts.

**Key meeting angles:**
1. **$13.28B subscription machine** | 98%+ of revenue is recurring subscription. Payment infrastructure directly impacts the renewability of the entire revenue base.
2. **37% international revenue** | $4.93B from non-US markets with no local payment methods. Each market has preferred rails that ServiceNow ignores.
3. **603 accounts at $5M+ ACV** | A single failed renewal on these accounts = $5M+ at risk. Multi-acquirer failover is essential at this contract size.
4. **APAC is fastest growing** | +23% YoY in a region that demands Konbini (Japan), UPI (India), and BPAY (Australia). Payment localization unlocks further growth.
5. **Fortune 500 procurement** | 85% of Fortune 500 are customers. These companies have strict payment policies: local currency, SEPA/BACS DD, purchase order integration.
6. **Competitive pressure** | Salesforce, SAP, Oracle all offer localized billing. ServiceNow's USD-only Store is a competitive disadvantage for international procurement.

**Sources:**
- [ServiceNow Wikipedia](https://en.wikipedia.org/wiki/ServiceNow)
- [ServiceNow Statistics 2026](https://cyntexa.com/blog/servicenow-statistics/)
- [ServiceNow FY2025 Results](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-Reports-Fourth-Quarter-and-Full-Year-2025-Financial-Results-Board-of-Directors-Authorizes-Additional-5B-for-Share-Repurchase-Program/default.aspx)
- [ServiceNow Q1 2026 Revenue Growth](https://www.investing.com/news/company-news/servicenow-q1-2026-slides-revenue-growth-accelerates-to-22-yy-93CH-4630999)
- [ServiceNow Revenue by Geography](https://stockanalysis.com/stocks/now/metrics/revenue-by-geography/)
- [ServiceNow Revenue (MacroTrends)](https://www.macrotrends.net/stocks/charts/NOW/servicenow/revenue)
- [ServiceNow Store](https://store.servicenow.com/store)
- [ServiceNow Store: How to Buy](https://www.alphaservesp.com/blog/exploring-the-servicenow-store-how-to-find-try-buy-and-install-apps)
- [Brandfetch: ServiceNow Logo](https://brandfetch.com/servicenow.com)
- [ServiceNow Q2 2025 Results (SEC)](https://www.sec.gov/Archives/edgar/data/1373715/000137371525000274/erq2fy25.htm)
- [ServiceNow AWS Marketplace](https://aws.marketplace.pp/prodview-ruxchcof6gjpg)
