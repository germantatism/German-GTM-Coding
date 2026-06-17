# SIFT | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Sift
=======================================

Logo: https://cdn.brandfetch.io/sift.com/w/512/h/512/logo
Nombre merchant: Sift

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: SaaS Billing Complexity
Tittle_Pain Point_2: 41% International Clients
Tittle_Pain Point_3: No Failover on Renewals
Tittle_Pain Point_4: Enterprise Invoice Limits
Tittle_Pain Point_5: Churn on Failed Payments

Desc_Pain Point_1: Usage-based SaaS scoring 1T events/year. Variable billing by API volume, events, and modules creates complexity a single processor cannot handle.
Desc_Pain Point_2: 41.5% of 5,857 customers are non-US: 1,165 in Saudi Arabia (22.9%), 302 in UK (5.9%). No local payment methods exist for these international clients.
Desc_Pain Point_3: $35M in revenue across 700+ subscriptions. A card decline or processor error on a $50K-$500K renewal has no multi-acquirer cascade to protect it.
Desc_Pain Point_4: Saudi clients (22.9%) need MADA/SADAD. UK clients need BACS. Enterprise procurement rules vary by country. Manual invoicing cannot scale globally.
Desc_Pain Point_5: Usage-based invoices with variable amounts are prone to decline. Even 2% involuntary churn on $35M revenue = $700K recoverable annual revenue.

SLIDE 1: PSP TOPOLOGY

PSP_1: Credit Card (SaaS billing)
PSP_2: Wire Transfer (enterprise contracts)
PSP_3: Direct invoicing (usage-based)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: MADA (Saudi Arabia)
Local_M_2: SADAD (Saudi Arabia)
Local_M_3: BACS Direct Debit (UK)
Local_M_4: SEPA Direct Debit (Europe)
Local_M_5: ACH Direct Debit (US)
Local_M_6: UPI (India)
Local_M_7: iDEAL (Netherlands)
Local_M_8: Bancontact (Belgium)
Local_M_9: BLIK (Poland)
Local_M_10: PIX (Brazil)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each renewal and usage charge to the best acquirer by card BIN, geography, and amount. With 700+ clients across 30+ countries, Smart Routing improves approval rates 3-10%, recovering $1M-$3.5M in declined charges yearly.
Desc_Yuno_Cap2: When a $200K usage invoice declines, Yuno reroutes in milliseconds to a backup processor. Up to 50% recovery on soft declines, reducing involuntary churn on Sift's highest-value enterprise accounts.
Desc_Yuno_Cap3: MADA/SADAD for Saudi Arabia (22.9% of clients), BACS for UK (5.9%), SEPA for Europe, ACH for US. One API, 1,000+ methods. Removes procurement friction in every market where Sift fights fraud.
Desc_Yuno_Cap4: One dashboard for SaaS billing across all processors, methods, and geographies. Real-time renewal health by tier, usage charge approval rates, revenue distribution, and churn-correlated payment failures.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Sift at a glance:**
- AI-powered digital fraud prevention and trust & safety platform
- Products: Payment Protection, Account Defense, Content Integrity, Dispute Management
- Founded: 2011 (originally Sift Science)
- Headquarters: San Francisco, California
- Employees: ~278-322 (as of Q1 2026)
- Revenue: $35M (2025), up from $30.3M (2024)
- Valuation: $1B+ (as of April 2021 Series E)
- Total funding: $162-208M across 10 rounds
- Key investors: Insight Partners (lead), Union Square Ventures, Stripes Group
- CEO: Marc Friend
- 700+ enterprise customers
- 34,000+ sites and apps on the platform
- 1 trillion events scored annually
- 40+ patents granted or allowed by USPTO
- #1 in Fraud Detection on G2 Grid (Winter 2026)

**Key customers:**
- DoorDash, Yelp, Poshmark, Wayfair, StitchFix, Harry's, Everlane

**Geographic customer distribution:**
- United States: 2,973 customers (58.5%)
- Saudi Arabia: 1,165 customers (22.9%)
- United Kingdom: 302 customers (5.9%)
- Rest of world: 12.7% across Europe, APAC, LATAM

**Leadership team:**
- Marc Friend (CEO)
- Raj Jain (Chief Product Officer)
- Johannes Hoech (Chief Marketing Officer)
- Ada Johnson (Chief Financial Officer)
- Brent Sapiro (Chief Revenue Officer)
- Ajay Gopal (Chief Strategy Officer)
- Jason Fama (SVP Engineering)
- Kevin Lee (Field CTO)

**Technology partners (payment-related):**
- Stripe (dispute data integration)
- Adyen (dispute data integration)
- Braintree / PayPal (dispute data integration)
- Checkout.com (dispute data integration)
- Magento / Adobe Commerce (e-commerce platform)
- Okta / Auth0 (identity)
- Ping Identity (authentication)
- Telesign (SMS verification)
- Zendesk (support)

**Confirmed PSPs & billing infrastructure:**
- SaaS subscription billing (usage-based + fixed components)
- Credit card as primary payment method for SaaS subscriptions
- Enterprise contracts via wire transfer and invoicing
- Zendesk-powered billing support portal
- No payment orchestrator detected
- Sift integrates WITH payment processors (Stripe, Adyen, Braintree, Checkout.com) as a fraud layer, but uses separate billing infrastructure for its own SaaS subscriptions

**Business model:**
- Usage-based SaaS pricing (per event scored, per API call)
- Module-based packaging (Payment Protection, Account Defense, Content Integrity)
- Enterprise contracts for large accounts
- Partner/reseller channel (Global Channel Sales under Leslie Lorenco)

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (58.5% of customers, ~2,973 accounts)
  Currently offer: Credit card, wire transfer, enterprise invoicing
  Missing: ACH Direct Debit for automated recurring billing
  US enterprise clients (DoorDash, Yelp, Poshmark) prefer ACH for recurring SaaS spend. Credit card limits on usage-based billing create payment failures.

MARKET 2: Saudi Arabia (22.9% of customers, ~1,165 accounts)
  Currently offer: Credit card, wire transfer
  Missing: MADA (local debit network), SADAD (bill payment), SAR invoicing
  Saudi Arabia is Sift's second-largest market by customer count. MADA processes 85%+ of card transactions in KSA. USD billing without MADA/SADAD creates procurement friction.

MARKET 3: United Kingdom (5.9% of customers, ~302 accounts)
  Currently offer: Credit card, wire transfer
  Missing: BACS Direct Debit, Open Banking, GBP invoicing
  UK enterprises expect BACS DD for recurring SaaS billing. GBP invoicing is a procurement requirement for UK-based fraud teams.

MARKET 4: Europe (Germany, France, Netherlands, Nordics)
  Currently offer: Credit card, wire transfer
  Missing: SEPA Direct Debit, iDEAL, Bancontact, EUR invoicing
  European e-commerce companies using Sift for fraud prevention expect SEPA DD for recurring vendor payments.

MARKET 5: APAC (Australia, Japan, Singapore, India)
  Currently offer: Credit card, wire transfer
  Missing: BPAY (AU), Konbini (JP), PayNow (SG), UPI (IN)
  APAC is a growing fraud prevention market. Local payment rails are expected for enterprise SaaS billing.

**Key meeting angles:**
1. **Saudi Arabia = 22.9% of customers** | Second-largest market with zero local payment infrastructure. MADA and SADAD support would unlock growth in the Kingdom's booming digital economy.
2. **$35M revenue, usage-based billing** | Variable invoices are harder to collect than fixed subscriptions. Smart routing optimizes charge success on fluctuating amounts.
3. **Fraud experts understand payment pain** | Sift's entire business is built on understanding payment fraud and chargebacks. They will deeply appreciate payment orchestration value.
4. **1 trillion events/year** | Scale of operations means billing infrastructure must handle high-volume, variable-amount charges across 30+ countries.
5. **Technology partner ecosystem** | Sift already integrates with Stripe, Adyen, Braintree, Checkout.com. Yuno as their billing orchestrator creates a natural complement to their existing payment partnerships.
6. **Competitive pressure** | Forter, Riskified, and Signifyd offer localized billing. Sift needs payment parity to compete for international enterprise accounts.

**Sources:**
- [Sift Homepage](https://sift.com/)
- [Sift Company Page](https://sift.com/company/)
- [Sift Platform Overview](https://sift.com/platform/)
- [Sift Payment Protection](https://sift.com/platform/payment-protection/)
- [Sift Technology Partners](https://sift.com/partners/technology/)
- [Sift Help Center: Billing](https://siftscience.zendesk.com/hc/en-us/sections/200803198-Billing-Pricing)
- [Sift + Stripe Integration](https://siftscience.zendesk.com/hc/en-us/articles/206212678-Does-Sift-work-with-Stripe)
- [Sift $50M Raise (TechCrunch)](https://techcrunch.com/2021/04/22/fraud-prevention-platform-sift-raises-50m-at-over-1b-valuation-eyes-acquisitions/)
- [Sift Revenue (Latka)](https://getlatka.com/companies/sift)
- [Sift Market Share (6Sense)](https://6sense.com/tech/financial-fraud-detection/sift-science-market-share)
- [Sift Crunchbase](https://www.crunchbase.com/organization/sift-science)
- [Sift CBInsights](https://www.cbinsights.com/company/sift-science)
- [Brandfetch: Sift Logo](https://brandfetch.com/sift.com)
