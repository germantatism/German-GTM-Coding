# RALPH LAUREN | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Ralph Lauren
=======================================

Logo: https://companieslogo.com/img/orig/RL-40b19360.png
Nombre merchant: Ralph Lauren

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Single Acquirer Dependency
Tittle_Pain Point_2: No Local APMs in Growth Mkts
Tittle_Pain Point_3: Checkout Session Errors
Tittle_Pain Point_4: BNPL Exclusions on Premium
Tittle_Pain Point_5: Asia Digital Gap at 35% Growth

Desc_Pain Point_1: Adyen confirmed as Ralph Lauren's payment processor globally. No secondary acquirer or orchestration layer detected. A single processor dependency across 30+ country sites creates systemic risk for a brand generating $7.1B in annual revenue, with DTC as the growth engine.
Desc_Pain Point_2: RalphLauren.com US accepts Visa, Mastercard, Amex, Discover, PayPal, and Klarna. European and Asian sites rely on cards and PayPal only. No iDEAL in Netherlands, no BLIK in Poland, no PIX in Brazil, no KakaoPay in Korea. Each missing method caps conversion in high growth markets.
Desc_Pain Point_3: Users report checkout failures where clicking the payment button triggers no action or auto scrolls back to the payment section. Browser cache issues, session timeouts, and card declines with no alternative offered. BBB complaints document order placement failures on ralphlauren.com.
Desc_Pain Point_4: Klarna is available at checkout but explicitly excludes Collection, Double RL, Purple Label, luxury accessories, footwear, limited editions, and new arrivals. The highest AOV items have no BNPL option, precisely where installment payments would most impact conversion.
Desc_Pain Point_5: Asia digital commerce grew 35% in Q1 FY2026, China alone up 20%+ YoY. But Asian sites lack Alipay, WeChat Pay, KakaoPay, NaverPay, and PayPay. The fastest growing region has the weakest local payment coverage, creating a conversion ceiling as digital scales.

SLIDE 1: PSP TOPOLOGY

PSP_1: Adyen PSP_2: PayPal PSP_3: Klarna PSP_4: Afterpay/Zip (limited)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: iDEAL (Netherlands)
Local_M_2: BLIK (Poland)
Local_M_3: PIX (Brazil)
Local_M_4: Boleto (Brazil)
Local_M_5: KakaoPay (South Korea)
Local_M_6: NaverPay (South Korea)
Local_M_7: PayPay (Japan)
Local_M_8: Alipay (China)
Local_M_9: WeChat Pay (China)
Local_M_10: Bancontact (Belgium)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing Engine
Tittle_Yuno_Cap2: Failover + NOVA Recovery
Tittle_Yuno_Cap3: 1,000+ Local APMs
Tittle_Yuno_Cap4: Unified Global Dashboard

Desc_Yuno_Cap1: Route each Ralph Lauren DTC transaction to the optimal acquirer per card BIN, issuer, and market. With $7.1B in annual revenue and DTC comparable sales up 13%, even a 1% auth uplift recovers tens of millions. Smart Routing analyzes real time PSP performance per corridor, boosting approval 3 to 10%.
Desc_Yuno_Cap2: Add secondary acquirers alongside Adyen with automatic cascade in milliseconds. When a processor declines or slows, Yuno reroutes instantly. NOVA AI recovers up to 75% of soft declines, eliminating checkout dead ends where the payment button fails silently. Livelo recovered 50% of failed transactions.
Desc_Yuno_Cap3: Activate iDEAL in Netherlands, BLIK in Poland, PIX in Brazil, Alipay and WeChat Pay in China, KakaoPay in South Korea, and PayPay in Japan. One API integration, no per market engineering. InDrive launched 10 LATAM markets in under 8 months using Yuno's single connection.
Desc_Yuno_Cap4: Replace siloed per region Adyen configurations with one real time dashboard across 30+ country sites. Centralized approval rate monitoring for North America (43%), Europe (33%), and Asia (24%) revenue streams. Millisecond anomaly detection catches payment issues before they impact luxury checkout experiences.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Ralph Lauren at a glance:**
- NYSE: RL. Global luxury lifestyle brand
- FY2025 (ending March 2025) Total Revenue: $7.1B (up 12.6% CAGR from FY2021)
- FY2025 Gross Profit: $4.85B (record, 68.6% gross margin)
- FY2025 Operating Income: $932M (record, 13.0% operating margin, up from 4.5% in FY2021)
- Q3 FY2025 (Holiday): $2.41B (up 12.25% YoY). Double digit growth across all regions
- Q1 FY2026: $1.72B (up 14% YoY). DTC comparable sales up 13%
- Digital Commerce Growth: North America +19%, Europe +11%, Asia +35% (Q1 FY2026)
- Revenue by Region FY2025: North America 43.1%, Europe ~33% ($2.17B), Asia 24.15%
- 5.9M new customers added across digital and store platforms in FY2025
- RalphLauren.com annual online sales: $649M (2025, up 20 to 50% YoY)
- Key City Ecosystem model: flagships + ecommerce + localized marketing
- Predictive buying now deployed across 25% of international DTC business
- May 2025: Appointed first Global Chief Digital Officer (Kiran Seshadri)

**Confirmed PSPs and Payment Infrastructure:**
- Adyen: Confirmed as payment processor for Ralph Lauren. Listed alongside H&M, SHEIN, Foot Locker, L'Oreal as Adyen clients per Business of Payments and Adyen marketing materials
- PayPal: Confirmed for US and European sites. Digital wallet option at checkout
- Klarna: Confirmed for US (Pay in 4, interest free, bi weekly installments). Also available in UK/EU. Excludes Collection, Double RL, Purple Label, luxury accessories, footwear, limited editions, new arrivals
- Afterpay: Listed on Afterpay merchant directory for Ralph Lauren US. Pay in 4 over 6 weeks
- Zip: Listed on Zip store directory for Ralph Lauren US. Pay in 4 over 6 weeks
- Credit/Debit Cards: Visa, Mastercard, American Express, Discover (US). Visa, Mastercard (Europe, Asia)
- Ralph Lauren Gift Cards: Accepted online and in store
- No Apple Pay, Google Pay confirmed at ralphlauren.com checkout
- No payment orchestration platform confirmed (Spreedly, Primer, Gr4vy, CellPoint, APEXX, or Yuno)

**Payment Methods by Region:**

REGION: United States (43.1% of revenue)
  Accepted: Visa, Mastercard, Amex, Discover, PayPal, Klarna (Pay in 4), Afterpay, Zip, gift cards
  Missing: Apple Pay, Google Pay, Cash App Pay, Venmo
  Note: BNPL excludes highest value items (Purple Label, Collection, luxury accessories)

REGION: Europe (33% of revenue, $2.17B)
  Accepted: Visa, Mastercard, PayPal, Klarna (UK/EU)
  Missing: iDEAL (Netherlands, 60%+ of online transactions), BLIK (Poland, 15M+ users), Bancontact (Belgium), Giropay (Germany), MB Way (Portugal), Trustly (Nordics)
  Note: Europe revenue grew 16% to $555M in Q1 FY2026 with digital up 11%. Local APMs would accelerate growth

REGION: Asia (24.15% of revenue)
  Accepted: Visa, Mastercard, PayPal (where available)
  Missing: Alipay (China), WeChat Pay (China), KakaoPay (South Korea), NaverPay (South Korea), PayPay (Japan), LINE Pay (Japan), UPI (India)
  Note: Asia digital grew 35% in Q1 FY2026, China alone 20%+. Missing local wallets despite being the fastest growing region

REGION: Latin America
  Accepted: Visa, Mastercard
  Missing: PIX (Brazil, 150M+ users), Boleto, MercadoPago, local installments
  Note: Ralph Lauren has limited LATAM DTC presence but expanding

**Payment Issues and Incidents:**
- Checkout session failures: Users report clicking the payment button triggers no action, with the browser auto scrolling back to the payment section. Occurs when logged into account. Clearing cache or using incognito mode is the only documented workaround
- Card decline with no alternative: When a card is declined at checkout, no automatic suggestion to try PayPal, Klarna, or another method. User must manually navigate to change payment method
- BBB complaints: Better Business Bureau profile shows complaints related to order placement failures, billing issues, and inability to complete purchases on ralphlauren.com
- Klarna exclusions confusion: Customers attempt to use Klarna at checkout for luxury items only to discover it is excluded. No alternative BNPL suggested. This creates friction precisely on the highest AOV purchases where BNPL is most impactful
- International card issues: Cross border shoppers report card declines when using cards from countries outside the site's primary market

**Key meeting angles:**
1. **Adyen only, no orchestration** | Ralph Lauren processes through Adyen globally with no secondary acquirer or orchestration layer. At $7.1B revenue and 13% DTC growth, single processor dependency creates risk and limits routing optimization. Yuno adds multi acquirer intelligence alongside Adyen without replacing the incumbent.
2. **Fastest growing region has weakest payment coverage** | Asia digital grew 35% in Q1 FY2026. China up 20%+. Yet no Alipay, WeChat Pay, KakaoPay, or PayPay on Asian sites. These methods account for 85%+ of digital transactions in their markets. Yuno activates all via one API with no per market engineering.
3. **BNPL gap on luxury items** | Klarna excludes Purple Label, Collection, luxury accessories, and limited editions. These are $500 to $5,000+ items where installment payments most drive conversion. Yuno can route BNPL eligibility across multiple providers (Klarna, Affirm, Afterpay) to maximize coverage across all price tiers.
4. **5.9M new digital customers, zero local APMs** | Ralph Lauren added 5.9M new customers across digital and stores in FY2025. First time buyers from Poland, Netherlands, South Korea, and Japan must pay by card. Local APMs reduce first purchase friction. One iDEAL or BLIK integration could meaningfully lift conversion in those corridors.
5. **Chief Digital Officer hired, payment stack ready for evolution** | Kiran Seshadri appointed as first ever Global CDO in May 2025. Digital commerce is now a CEO level priority. An orchestration layer aligns with the CDO mandate to modernize DTC infrastructure across 30+ markets.

**Ralph Lauren Leadership:**
- Patrice Louvet: President and CEO (since 2017). Former P&G executive
- Justin Picicci: CFO. Oversees financial operations and revenue reporting
- Kiran Seshadri: Global Chief Digital Officer (appointed May 2025). First CDO in company history. Focused on digital acceleration
- David Lauren: Vice Chairman and Chief Innovation Officer. Son of Ralph Lauren
- Ralph Lauren: Executive Chairman and Chief Creative Officer
- No dedicated VP of Payments identified in public sources

**Recent corporate developments:**
- May 2025: Kiran Seshadri appointed as first Global Chief Digital Officer
- Q1 FY2026 (June 2025): Revenue $1.72B (up 14%). DTC comparable sales up 13%. North America digital +19%, Europe digital +11%, Asia digital +35%
- FY2025: Revenue $7.1B (record). Gross profit $4.85B (record). Operating income $932M (record, 13.0% margin)
- Q3 FY2025 (Holiday): Revenue $2.41B (up 12.25%). Raised full year outlook
- FY2025: 5.9M new customers added across digital and store platforms
- FY2025: Predictive buying deployed across 25% of international DTC business
- Store expansion: Shanghai, Beijing, San Francisco flagships
- Tariff strategy: Agile supply chain adjustments for US tariff environment

**Sources:**
- [Ralph Lauren FY2025 Full Year Results (Investor Relations)](https://investor.ralphlauren.com/news-releases/news-release-details/ralph-lauren-reports-fourth-quarter-and-full-year-fiscal-2025)
- [Ralph Lauren Q1 FY2026 Results (Corporate)](https://corporate.ralphlauren.com/pr_250807_Q1FY26_EarningsResults.html)
- [Ralph Lauren Q2 FY2026 Results (Corporate)](https://corporate.ralphlauren.com/pr_251106_Q2FY26_EarningsResults.html)
- [Ralph Lauren Q3 FY2025 Results (Corporate)](https://corporate.ralphlauren.com/pr_250205_Q3FY25_EarningsResults.html)
- [Ralph Lauren Q3 FY2026 Results (Corporate)](https://corporate.ralphlauren.com/pr_260205_Q3FY26_EarningsResults.html)
- [Ralph Lauren Digital DTC Sales Power Growth (Digital Commerce 360)](https://www.digitalcommerce360.com/2026/02/06/ralph-lauren-dtc-digital-sales-q3-revenue-fy25/)
- [Ralph Lauren Statistics 2026 (Bayelsawatch)](https://bayelsawatch.com/ralph-lauren-statistics/)
- [Ralph Lauren Revenue (Bullfincher)](https://bullfincher.io/companies/ralph-lauren-corporation/revenue)
- [Ralph Lauren Revenue by Geography (Bullfincher)](https://bullfincher.io/companies/ralph-lauren-corporation/revenue-by-geography)
- [Ralph Lauren eCommerce Revenue (ecdb)](https://ecdb.com/resources/sample-data/retailer/ralphlauren)
- [Ralph Lauren Global CDO Appointment (Digital Commerce 360)](https://www.digitalcommerce360.com/2025/05/23/ralph-lauren-global-chief-digital-officer-seshadri/)
- [Ralph Lauren Digital Strategy (National CIO Review)](https://nationalcioreview.com/articles-insights/cio-field-notes/polo-and-predictive-tech-ralph-laurens-digital-strategy-propels-growth/)
- [Ralph Lauren Tariffs Supply Chain (Supply Chain Dive)](https://www.supplychaindive.com/news/ralph-lauren-tariffs-supply-chain/749685/)
- [Ralph Lauren Accepted Payment Methods US](https://www.ralphlauren.com/support?a=Payment-Methods---id--IhSE27qZRzirsDfmzmgAQg)
- [Ralph Lauren Payment Methods EU](https://support.ralphlauren.eu/hc/en-gb/articles/21677957036189-What-payment-methods-do-you-accept)
- [Ralph Lauren Klarna (ralphlauren.com)](https://www.ralphlauren.com/paying-with-klarna/cs-order-klarna.html)
- [Ralph Lauren Klarna EU](https://support.ralphlauren.eu/hc/en-gb/articles/21789445093405-Klarna)
- [Ralph Lauren PayPal](https://www.ralphlauren.com/support?a=PayPal---id--McccKB37R6qS7ei15Nlopg)
- [Ralph Lauren Afterpay](https://www.afterpay.com/en-US/stores/ralph-lauren-39627)
- [Ralph Lauren Zip](https://zip.co/us/store/ralph-lauren)
- [Ralph Lauren BBB Complaints](https://www.bbb.org/us/ny/new-york/profile/designer-apparel/ralph-lauren-0121-340/complaints)
- [Adyen Clients Including Ralph Lauren (Business of Payments)](https://businessofpayments.substack.com/p/business-of-payments-november-2025)
- [Adyen Review 2026 (The Retail Exec)](https://theretailexec.com/tools/adyen-review/)
- [Ralph Lauren Q3 FY2025 Growth (Fashion Dive)](https://www.fashiondive.com/news/ralph-lauren-q3-2025-revenue-beats-projections/739441/)
- [Ralph Lauren Logo (CompaniesLogo)](https://companieslogo.com/ralph-lauren/logo/)
