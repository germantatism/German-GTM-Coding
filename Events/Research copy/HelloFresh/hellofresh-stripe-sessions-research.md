# HELLOFRESH | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: HelloFresh
=======================================

Logo: https://cdn.brandfetch.io/idZbYETkpR/w/512/h/512/theme/dark/icon.jpeg
Nombre merchant: HelloFresh

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Subscription Auth Decay
Tittle_Pain Point_2: Multi-Market Complexity
Tittle_Pain Point_3: Failed Payment Recovery
Tittle_Pain Point_4: Limited APM Coverage
Tittle_Pain Point_5: Cross-Border FX Drag

Desc_Pain Point_1: HelloFresh processes recurring subscription charges across 7M+ customers in 18 markets. Card-on-file transactions face natural auth decay from expired cards, lost cards, and issuer declines. On billions in annual subscription revenue, even 1% involuntary churn from failed payments represents tens of millions in lost recurring revenue per year.
Desc_Pain Point_2: HelloFresh operates in 18 countries across North America and Europe with Adyen as primary PSP. Each market has unique payment preferences: SEPA in Germany, Cartes Bancaires in France, iDEAL in Netherlands, PayPal in UK. Managing subscription billing, dunning, and local payment compliance across 18 regulatory environments creates operational overhead.
Desc_Pain Point_3: HelloFresh's subscription model means meal boxes are sometimes delivered before payment is collected. The payments team uses email, SMS, letters, Tikkie (Netherlands), and collection agencies to recover outstanding funds. Each failed recovery is product shipped without revenue collected.
Desc_Pain Point_4: While HelloFresh accepts SEPA, Klarna, and PayPal in Germany, many international markets lack local payment methods. No BNPL in most markets despite being a subscription product. No Pix in Brazil-like expansion markets. No mobile wallets beyond Apple Pay and Google Pay in most countries.
Desc_Pain Point_5: With FY2025 revenue of EUR 6.8B across 18 countries in two currencies (EUR and USD primary), cross-border card processing on international customer acquisition campaigns incurs FX markup. The 9% constant currency revenue decline makes cost optimization critical.

SLIDE 1: PSP TOPOLOGY

PSP_1: Adyen (primary global PSP)
PSP_2: PayPal (alternative method)
PSP_3: Klarna (Germany, select markets)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Afterpay
Local_M_2: Open Banking (UK)
Local_M_3: Swish
Local_M_4: Vipps
Local_M_5: MobilePay
Local_M_6: Twint
Local_M_7: EPS
Local_M_8: Bizum
Local_M_9: Alma
Local_M_10: POLi

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Recovery
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across Adyen and additional acquirers for every subscription charge and new customer acquisition. Each recurring payment routed to the highest performing acquirer for that card BIN, issuer, and market. On EUR 6.8B revenue across 18 countries, smart routing delivers +3 to 10% auth uplift on subscription renewals, directly reducing involuntary churn.
Desc_Yuno_Cap2: Automatic cascade across Adyen and secondary processors eliminates single-PSP dependency for critical subscription charges. When Adyen declines a recurring payment, Yuno reroutes in milliseconds. Up to 50% recovery on soft declines via instant retry. NOVA AI recovers up to 75% of failed transactions. For a subscription business, every recovered payment is a retained customer.
Desc_Yuno_Cap3: Activates the APMs HelloFresh lacks in key markets: Afterpay for BNPL in Australia and UK, Open Banking in UK for instant debits, Swish in Sweden (8M+ users), Vipps in Norway (4M+ users), MobilePay in Denmark, Twint in Switzerland, EPS in Austria, Bizum in Spain, Alma in France. One API, 1,000+ payment methods across all 18 markets.
Desc_Yuno_Cap4: One dashboard replacing HelloFresh's Adyen-centric view with multi-acquirer analytics across 18 countries. Real-time approval rate monitoring for subscription renewals, first-payment conversions, and dunning recovery, centralized reconciliation across meal kit and ready-to-eat product lines, and millisecond anomaly detection via Monitors. Single view of the entire recurring revenue engine.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**HelloFresh at a glance:**
- Model: Subscription-based meal kit and ready-to-eat (Factor) D2C e-commerce
- Revenue: EUR 7.66B (FY2024, +0.9% cc); EUR 6.8B (FY2025, -9% cc, -11.8% reported)
- Adjusted EBITDA: EUR 399M (FY2024); improved margins in FY2025
- Meal Kit AEBITDA margin: 13.5% (FY2025, highest since pandemic, +4pp YoY)
- Free Cash Flow: EUR 18.9M (FY2025, highest since 2021)
- Active Customers: ~7M (peak); declining as company focuses on profitable cohorts
- Close to 1 billion meals delivered globally (2024)
- Orders: ~27.5M per quarter (Q3 2024)
- Brands: HelloFresh (meal kits), Factor (ready-to-eat), Green Chef, EveryPlate, Chefs Plate (Canada)
- RTE Revenue: EUR 2.0B (FY2025, -1.4% cc)
- Frankfurt Stock Exchange: HFG, market cap ~EUR 1.5B
- Founded: 2011, Berlin. CEO: Dominik Richter (Founder)
- CEO International: Thomas Griesel (Founder)
- CFO: Fabien Simon (since September 2025, replacing Christian Gartner)
- General Counsel: Christian Ries
- Head of Payments NA: Jake Hershman (ex-American Express, ex-Mastercard)
- Senior Payments Manager: Elaine Nguyen

**Markets (18 countries, 2 segments):**
- North America: United States, Canada
- International: Germany (HQ), United Kingdom, Netherlands, Belgium, Luxembourg, France, Austria, Switzerland, Denmark, Norway, Sweden, Ireland, Australia, New Zealand, Italy (liquidating Jan 2026), Spain (closing Jan 2026)

**Revenue by Segment (FY2024):**
- North America: ~EUR 5.0B+ (~65%)
- International: ~EUR 2.6B+ (~35%)

**Strategic Initiatives:**
- $70M investment in AI-driven menu expansion (US: from 45 to 100+ weekly recipes)
- Factor "ReFresh" initiative: doubled weekly menu options (H2 2025)
- European Factor production hub launching Q1 2026 across 5 EU markets
- Focus on smaller but more profitable customer base
- $7.5M legal settlement for deceptive subscription practices in California

**Payments Infrastructure:**
- Adyen: primary global PSP for all markets (confirmed via Adyen knowledge hub and Jake Hershman interview)
- Adyen RevenueAccelerate: subscription optimization tool
- Adyen RealTime Account Updater: card-on-file maintenance
- Adyen local acquiring in Canada (early pilot partner)
- Network tokenization deployed for recurring payments
- Merchant-initiated transaction (MIT) flags for subscription billing
- 3DS 2.0 compliance in European markets
- PayPal: accepted in US, UK, and select markets
- Klarna: accepted in Germany (invoice payments)
- SEPA Direct Debit: Germany, with Sofort for initial signup converted to SEPA mandate
- Tikkie: Netherlands (payment recovery tool)
- Collection agencies: last-resort recovery for unpaid deliveries
- No payment orchestrator detected
- Dedicated payments team with cross-departmental integration (Finance, CS, Marketing)

**Payment Methods by Key Market:**
- US: Visa, MC, Amex, Discover, PayPal, Apple Pay, Google Pay
- Germany: Visa, MC, Amex, PayPal, SEPA Direct Debit, Sofort, Klarna
- UK: Visa, MC, Amex, Maestro, PayPal
- Netherlands: Visa, MC, PayPal, Tikkie (recovery), iDEAL (likely via Adyen)
- Australia: Visa, MC, PayPal

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (~65% of revenue, ~EUR 5B)
  Currently offer: Visa/MC/Amex/Discover, PayPal, Apple Pay, Google Pay
  Missing: Klarna (US), Affirm, Afterpay, Venmo, Cash App Pay
  BNPL for a $60-80/week subscription reduces friction for new customer acquisition. 45% BNPL adoption in US e-commerce.

MARKET 2: Germany (HQ market, largest international)
  Currently offer: Visa/MC/Amex, PayPal, SEPA, Sofort, Klarna
  Missing: giropay replacement, Google Pay (broader integration)
  Germany is well-covered. Opportunity is in routing optimization between Adyen and local acquirers.

MARKET 3: United Kingdom (major international market)
  Currently offer: Visa/MC/Amex/Maestro, PayPal
  Missing: Open Banking (Faster Payments), Klarna, Clearpay (Afterpay UK)
  UK Open Banking growing 60%+ YoY. Direct debit via Open Banking would reduce subscription churn vs card-on-file.

MARKET 4: Australia (established market)
  Currently offer: Visa/MC, PayPal
  Missing: Afterpay (12M+ AU users), eftpos, POLi, BPAY
  Afterpay has massive adoption in Australia. Missing BNPL in a market where 30%+ of online shoppers use it.

MARKET 5: Nordics (Denmark, Norway, Sweden)
  Currently offer: Visa/MC, PayPal
  Missing: MobilePay (Denmark), Vipps (Norway, 4M+ users), Swish (Sweden, 8M+ users)
  Nordic markets are mobile-wallet-first. Swish alone processes 50%+ of Swedish P2P and e-commerce payments.

MARKET 6: Switzerland
  Currently offer: Visa/MC, PayPal
  Missing: Twint (5M+ users, 55%+ mobile payment share), PostFinance
  Twint is the dominant mobile payment method in Switzerland.

MARKET 7: France
  Currently offer: Visa/MC, PayPal
  Missing: Cartes Bancaires (explicit routing), Alma (French BNPL), Bancontact (Belgian border)
  Factor RTE launching in France via EU hub. New product = new customer acquisition = need for local APMs.

**Payment Pain Points:**
1. Subscription auth decay: expired cards, lost cards, issuer declines on recurring charges
2. Adyen single-PSP dependency across 18 countries with no failover
3. Meals delivered before payment collected (subscription timing gap)
4. Recovery process is manual: email, SMS, letters, Tikkie, collection agencies
5. No BNPL in US, UK, Australia (largest markets outside Germany)
6. No mobile wallets for Nordics (Swish, Vipps, MobilePay)
7. No Open Banking in UK for subscription direct debit
8. $7.5M legal settlement for subscription billing practices raises regulatory scrutiny
9. FY2025 revenue declining 9% makes cost optimization and churn reduction critical
10. Italy and Spain market exits show payment infrastructure must be flexible for market entry/exit

**Key Meeting Angles:**
1. **Subscription auth decay is the #1 pain**: Every failed recurring charge is a churned customer. Smart routing across Adyen and a secondary acquirer recovers failed renewals. InDrive achieved 90% approval across 10 markets with Yuno
2. **EUR 6.8B revenue, single PSP**: Adyen handles everything. No failover. For a subscription business, a PSP outage during billing cycle means mass involuntary churn
3. **18 countries need local APMs**: Swish in Sweden, Vipps in Norway, MobilePay in Denmark, Twint in Switzerland, Open Banking in UK. Yuno activates 1,000+ methods via single API. McDonald's gained +4.7% auth rate with Yuno
4. **Head of Payments is dedicated role**: Jake Hershman (ex-Amex, ex-Mastercard) leads payments strategy in NA. He understands payment optimization and will appreciate orchestration value
5. **Factor RTE expansion creates new payment needs**: European Factor hub launching Q1 2026 across 5 markets. New product in new markets = new local payment methods needed
6. **Revenue is declining, margins matter more**: At -9% revenue growth, every basis point of auth uplift and churn reduction is critical. Smart routing on EUR 6.8B delivers material P&L impact
7. **Involuntary churn recovery**: NOVA AI can recover up to 75% of failed subscription charges. Current recovery (email, SMS, collection agencies) is slow and expensive
8. **BNPL for customer acquisition**: $60-80/week meal kit subscriptions are ideal for BNPL. Klarna and Afterpay reduce the barrier for first-box conversion

**Sources:**
- [Adyen Knowledge Hub: A Fresh Take on Payments with HelloFresh](https://www.adyen.com/knowledge-hub/a-fresh-take-on-payments-with-hellofresh)
- [Adyen Twitter: Jake Hershman Interview](https://x.com/Adyen/status/1115727612368678912)
- [PaymentGenes: HelloFresh Payments Team](https://www.paymentgenes.com/articles/hello-freshs-payments-team-in-a-meal-kit-company)
- [HelloFresh Group: FY2024 Press Release](https://assets.ctfassets.net/irplh84t0tdt/41EFHSHF6emItr6p6BtEge/bf4cb8bd67fa5cf69cd7e8000e9ccece/250313_HelloFresh_Group_Press_Release_FY_Q4_2024_EN.pdf)
- [HelloFresh Group: FY2025 Press Release](https://assets.ctfassets.net/irplh84t0tdt/KsN160DAmoiGZDlgY1q4J/97be2657dcfd6aaa47abb50e0710606f/HelloFresh_Group_Press_Release_Q4_FY_2025.pdf)
- [HelloFresh IR: Publications](https://ir.hellofreshgroup.com/publications)
- [HelloFresh Group: Capital Markets Day 2025](https://assets.ctfassets.net/irplh84t0tdt/1mgaP7kD2Dhh4rPtzWjzZG/573a856a73dce7d9f90eb7ff853a60bb/HelloFresh_Group_Press_release_Capital_Markets_Day_2025.pdf)
- [HelloFresh USA: What Payment Methods Does HelloFresh Accept](https://support.hellofresh.com/hc/en-us/articles/360000489687-What-payment-methods-does-HelloFresh-accept-)
- [HelloFresh UK: Payment Methods](https://support.hellofresh.co.uk/hc/en-us/articles/115007718828-What-payment-methods-do-you-accept-)
- [LA County DA: HelloFresh $7.5M Settlement](https://da.lacounty.gov/media/news/hellofresh-pay-75-million-deceptive-subscription-practices-consumer-protection-lawsuit)
- [Wikipedia: HelloFresh](https://en.wikipedia.org/wiki/HelloFresh)
- [Statista: HelloFresh Revenue Worldwide](https://www.statista.com/statistics/655060/hellofresh-net-revenue-worldwide/)
- [Ada Insights: HelloFresh Back to Growth with RTE](https://adainsights.com/blog/hellofresh-back-to-growth-with-ready-to-eat-products)
- [HelloFresh Careers: Leadership](https://careers.hellofresh.com/global/en/leadership-at-hellofresh)
- [Grocery Gazette: HelloFresh CFO Step Down](https://www.grocerygazette.co.uk/2025/06/04/hellofresh-cfo-step-down/)
- [Companies Market Cap: HelloFresh Revenue](https://companiesmarketcap.com/hellofresh/revenue/)
- [HelloFresh Group: Newsroom](https://hellofreshgroup.com/en/newsroom/press-releases/)
