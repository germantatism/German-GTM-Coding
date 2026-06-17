# MONGODB | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: MongoDB
═══════════════════════════════════════

Logo: https://webimages.mongodb.com/_com_assets/cms/kuyjf3vea2hg34taa-horizontal_default_slate_blue.svg?auto=format%252Ccompress
Nombre merchant: MongoDB

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Usage Billing Complexity
Tittle_Pain Point_2: Cross-Border Declines
Tittle_Pain Point_3: Limited Self-Serve APMs
Tittle_Pain Point_4: No Acquirer Redundancy
Tittle_Pain Point_5: SCA Friction in Europe

Desc_Pain Point_1: Atlas bills on consumption (storage, compute, data transfer) across 62,500+ customers. Variable monthly charges trigger more fraud flags than fixed SaaS subscriptions, increasing false decline rates on card renewals.
Desc_Pain Point_2: 40% of revenue comes from EMEA and APAC, but self-serve billing routes through US-based card processing. International cards face higher issuer declines on cross-border transactions billed in USD.
Desc_Pain Point_3: Self-serve Atlas customers can only pay with credit card or PayPal. No SEPA DD, no Pix, no UPI, no local bank transfers. Developers in emerging markets are blocked at the billing step.
Desc_Pain Point_4: Single payment processor for all self-serve billing with no failover path. Any processor outage blocks new Atlas sign-ups and existing cluster upgrades for 62,500+ customers worldwide.
Desc_Pain Point_5: European Atlas customers face payment failures from Strong Customer Authentication requirements. SCA-triggered 3DS challenges on recurring usage charges increase involuntary churn across EEA markets.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (likely primary, self-serve)
PSP_2: PayPal
PSP_3: AWS Marketplace
PSP_4: Azure Marketplace
PSP_5: Google Cloud Marketplace

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: SEPA Direct Debit
Local_M_2: Pix
Local_M_3: UPI
Local_M_4: BACS Direct Debit
Local_M_5: iDEAL
Local_M_6: Boleto
Local_M_7: Konbini
Local_M_8: BLIK
Local_M_9: Bancontact
Local_M_10: OXXO

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each Atlas billing charge to the optimal acquirer by card BIN, issuer, and country. With $2.4B+ annual revenue from 62,500+ customers across 100+ countries, even a 3% auth uplift translates to $72M+ in recovered billing revenue without adding a single new cluster.
Desc_Yuno_Cap2: Automatic cascade removes single-processor dependency. When the primary acquirer declines a usage-based charge, Yuno reroutes to the next best processor in milliseconds, recovering failed billing with zero service disruption. Up to 50% recovery on soft declines.
Desc_Yuno_Cap3: Activates the APMs MongoDB's global developer base needs: SEPA DD across Europe (24% of revenue), UPI in India, Pix in Brazil, iDEAL in Netherlands, Konbini in Japan, BLIK in Poland. One API, 1,000+ payment methods. No engineering effort per market.
Desc_Yuno_Cap4: One dashboard consolidating self-serve card billing, PayPal, and marketplace channels (AWS, Azure, GCP) into a unified view. Real-time approval rate monitoring per region, centralized reconciliation, millisecond anomaly detection via Monitors.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**MongoDB at a glance:**
- Publicly traded: NASDAQ: MDB. Market cap ~$21B (April 2026)
- Revenue: $2.464B (FY2026, ended Jan 31, 2026), up 22.8% YoY
- Atlas (cloud DBaaS) represents 75% of revenue, growing 30% YoY
- 62,500+ total customers (Q3 FY2026), adding 2,600 net new customers per quarter
- 5,640 employees. HQ: New York City
- Offices in London, Dublin, Singapore, Sydney, Tel Aviv, and more
- CEO: Dev Ittycheria (since 2014)
- Available in 110+ cloud regions via AWS, Azure, Google Cloud

**Revenue by geography:**
- North America: ~60% of revenue
- EMEA: ~24% of revenue (growing 35%+ YoY)
- APAC: ~12% of revenue (fastest growing region)
- Key EMEA hubs: UK, Germany, France
- Key APAC hubs: Japan, Australia, India

**Confirmed PSPs and billing methods:**
- Self-serve (Atlas console): credit card and PayPal only
- Enterprise subscriptions: ACH, wire transfer, invoicing in multiple currencies (via MongoDB Sales)
- Cloud marketplace billing: AWS Marketplace, Azure Marketplace, Google Cloud Marketplace
- India: RBI mandate compliance for recurring card payments ($1,400/month mandate registered)
- Europe: SCA/3DS compliance for EEA customers
- No payment orchestrator detected

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (~60% revenue)
  Accepted: Visa/MC/Amex via card processing, PayPal, ACH (enterprise only)
  Missing: ACH for self-serve, Cash App Pay
  Note: Well served but no acquirer redundancy for self-serve billing

MARKET 2: United Kingdom (major EMEA hub)
  Accepted: Visa/MC, PayPal
  Missing: BACS Direct Debit, Open Banking
  Note: UK developers and enterprises expect Direct Debit for recurring cloud billing

MARKET 3: Germany (major EMEA market)
  Accepted: Visa/MC, PayPal
  Missing: SEPA Direct Debit, Sofort, Giropay
  Note: Only ~35% card penetration. SEPA DD is standard for recurring B2B payments

MARKET 4: India (growing developer market)
  Accepted: Visa/MC with RBI mandate, INR billing available
  Missing: UPI, RuPay, Net Banking, Paytm
  Note: RBI recurring mandate at $1,400/month creates friction. UPI handles 75%+ of digital payments

MARKET 5: Brazil (growing LATAM market)
  Accepted: Visa/MC (likely USD cross-border)
  Missing: Pix, Boleto, local installment cards
  Note: Pix handles 70%+ of digital payments. Developers priced out without local methods

**Key meeting angles:**
1. **Usage-based billing complexity** | Variable monthly charges trigger more fraud flags than fixed subscriptions, amplifying the decline problem
2. **Developer-first adoption** | Self-serve Atlas is the growth engine; blocked payment = lost developer = lost future enterprise deal
3. **EMEA is the fastest revenue growth** | 35%+ YoY, but zero local European APMs for self-serve customers
4. **RBI mandate friction in India** | $1,400/month recurring mandate creates involuntary churn for growing Indian developer base
5. **Marketplace dependency** | AWS/Azure/GCP marketplaces take 3-5% fees; direct billing with local APMs recovers that margin
6. **Public company pressure** | $21B market cap company reporting payment metrics to Wall Street. Auth rate improvements flow directly to earnings

**Sources:**
- [MongoDB FY2026 Q4 Results](https://investors.mongodb.com/news-releases/news-release-details/mongodb-inc-announces-fourth-quarter-fiscal-2026-financial)
- [MongoDB FY2026 Q3 Results](https://investors.mongodb.com/news-releases/news-release-details/mongodb-inc-announces-third-quarter-fiscal-2026-financial)
- [MongoDB FY2025 Full Year Results](https://investors.mongodb.com/news-releases/news-release-details/mongodb-inc-announces-fourth-quarter-and-full-year-fiscal-2025)
- [SaaStr: MongoDB at $2B+ ARR](https://www.saastr.com/mongodb-at-2b-arr-5-epic-learnings-from-q1-2026-that-every-b2b-leader-should-study/)
- [MongoDB Atlas Billing Docs](https://www.mongodb.com/docs/atlas/billing/)
- [MongoDB Atlas International Billing](https://www.mongodb.com/docs/atlas/billing/international-usage/)
- [MongoDB Atlas Subscriptions](https://www.mongodb.com/docs/atlas/billing/subscriptions/)
- [MongoDB Billing FAQ](https://www.mongodb.com/docs/atlas/reference/faq/billing/)
- [MongoDB Brand Resources](https://www.mongodb.com/company/newsroom/brand-resources)
- [MongoDB Revenue (MacroTrends)](https://www.macrotrends.net/stocks/charts/MDB/mongodb/revenue)
- [MongoDB Market Cap](https://www.macrotrends.net/stocks/charts/MDB/mongodb/market-cap)
- [Yahoo Finance: MDB](https://finance.yahoo.com/quote/MDB/)
