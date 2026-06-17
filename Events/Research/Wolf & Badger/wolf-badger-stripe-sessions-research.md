# WOLF & BADGER | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Wolf & Badger
═══════════════════════════════════════

Logo: https://upload.wikimedia.org/wikipedia/commons/a/ae/Wolf_%26_Badger_logo.svg
Nombre merchant: Wolf & Badger

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: 30+ EU Markets, Few APMs
Tittle_Pain Point_2: Brand Payouts Take 7+ Days
Tittle_Pain Point_3: Cross Border FX Drag
Tittle_Pain Point_4: No PSP Failover
Tittle_Pain Point_5: Refund Reconciliation Chaos

Desc_Pain Point_1: Wolf & Badger ships to 30+ EU countries plus US, UK, Canada, Australia but relies primarily on cards and Klarna. No iDEAL, Bancontact, BLIK, Swish, or SEPA Direct Debit despite covering all major EU markets.
Desc_Pain Point_2: Brand partner payouts happen within 7 days of each statement date. 2,000+ independent brands across 30+ countries wait a week for settlement. No instant or same day payout option. Competitors offer faster payouts.
Desc_Pain Point_3: Brands ship from dozens of countries (US, Italy, UK, France). Buyers pay in local currency. FX conversion, duties, and tax inclusion across 30+ markets create settlement complexity with no unified orchestration layer.
Desc_Pain Point_4: No confirmed backup processor or orchestration layer. If the primary PSP experiences an outage, all global transactions halt. $95M GMV in 2024 with zero failover protection.
Desc_Pain Point_5: Each order may ship from a different brand in a different country. Returns across 30+ markets require refund coordination between Wolf & Badger, the brand, and the payment processor. 0% complaint resolution rate on ComplaintsBoard.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe [INFERENCE]
PSP_2: Klarna
PSP_3: Clearpay/Afterpay
PSP_4: N/A

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: iDEAL
Local_M_2: Bancontact
Local_M_3: BLIK
Local_M_4: Swish
Local_M_5: SEPA Direct Debit
Local_M_6: Przelewy24
Local_M_7: MobilePay
Local_M_8: Open Banking (UK)
Local_M_9: Bizum (Spain)
Local_M_10: MB WAY (Portugal)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing for Luxury
Tittle_Yuno_Cap2: Pan European APM Layer
Tittle_Yuno_Cap3: Multi Brand Payout Orchestr.
Tittle_Yuno_Cap4: Real Time Payment Monitors

Desc_Yuno_Cap1: Route each Wolf & Badger transaction across the best performing PSP by card BIN, issuer, country, and currency. High AOV luxury items mean every declined transaction is significant lost revenue. Wingo achieved +14% approval with Yuno Smart Routing.
Desc_Yuno_Cap2: Activate iDEAL, Bancontact, BLIK, Swish, SEPA, Przelewy24, MobilePay, Open Banking, Bizum, and MB WAY via one API across all 30+ EU markets. 1,000+ payment methods, no engineering sprints per country. InDrive scaled 10 markets in under 8 months.
Desc_Yuno_Cap3: One orchestration layer managing payouts to 2,000+ brands across 30+ countries. Unified reconciliation of commissions, membership fees, refunds, and FX. Rappi (20+ PSPs) cut analyst time by 80% and reconciliation by up to 90% with Yuno.
Desc_Yuno_Cap4: Rappi used Yuno Monitors to cut anomaly response from 10 minutes to milliseconds. For Wolf & Badger processing $95M+ GMV across thousands of brands, real time detection prevents refund errors and checkout failures before they escalate.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Wolf & Badger at a glance:**
- HQ: London, UK | Stores: London, New York, Los Angeles | Founded: 2010
- Co founders: George Graham (CEO) and Henry Graham (Creative Director)
- B Corp certified global marketplace for independent, ethical, and sustainable brands
- FY2024: ~$50M net revenue, $95M GMV, second consecutive profitable year
- US sales: grew from $3M (2019) to $45M+ (2024). US now accounts for nearly half of total sales.
- 2,000+ independent brand partners across fashion, homeware, beauty, and accessories
- Ships to 30+ countries with duties/taxes included (UK, US, AU, CA, all EU member states)
- Business model: brands pay $375/month membership + commission on each sale. Asset light: brands handle packing and shipping.
- 77M+ customers reached in 2024

**Key leadership (payments relevant):**
- George Graham, CEO and co founder: selected for Raconteur 50 CEO list. Actively involved in technology and AI strategy. Publicly noted interest in Stripe's agentic commerce protocol.
- Henry Graham, co founder and Creative Director
- Alex Crawley, CTO: oversees technology and engineering (18 person IT team)
- No dedicated VP/Head of Payments identified

**Confirmed PSPs and payment infrastructure:**
- Stripe [INFERENCE]: CEO George Graham publicly discussed Stripe's agentic commerce protocol. W&B is a technology platform for independent brands, consistent with Stripe Connect marketplace model. Not explicitly confirmed.
- Klarna: confirmed for US and UK (3 installment payments)
- Clearpay: confirmed for UK (4 fortnightly installments)
- Afterpay: confirmed for US and Australia
- Zip: confirmed for US (4 installment payments)
- Credit/debit cards: Visa, Mastercard, Amex, Discover confirmed
- Cartes Bancaires: confirmed (French card network)
- China UnionPay: confirmed
- JCB (Japan Credit Bureau): confirmed
- Apple Pay: confirmed
- No payment orchestrator detected

**Payment methods by region:**

Global: Visa, Mastercard, Amex, Discover, Apple Pay, Cartes Bancaires, China UnionPay, JCB

UK: above + Klarna (3 installments), Clearpay (4 fortnightly)

US: above + Klarna (3 installments), Afterpay (4 fortnightly), Zip (4 installments)

Australia: above + Afterpay

**Missing local APMs (blind spots across 30+ markets):**

| # | APM | Market | Why It Matters |
|---|-----|--------|----------------|
| 1 | iDEAL | Netherlands | 50%+ of Dutch online transactions. W&B ships to NL with duties included but no iDEAL. |
| 2 | Bancontact | Belgium | 17M+ cards. W&B ships to Belgium with duties included. |
| 3 | BLIK | Poland | 90%+ of Polish bank customers. W&B ships to Poland. |
| 4 | Swish | Sweden | 8M+ users. W&B ships to Sweden. |
| 5 | SEPA Direct Debit | Eurozone | Standard for recurring Euro payments. Relevant for brand membership billing. |
| 6 | Przelewy24 | Poland | Leading Polish bank transfer system. Complements BLIK. |
| 7 | MobilePay | Denmark | Leading Danish mobile payment. W&B ships to Denmark. |
| 8 | Open Banking (UK) | UK | Account to account. Lower fees than card for W&B's UK market (47% of revenue). |
| 9 | Bizum | Spain | 27M+ users. W&B ships to Spain with duties included. |
| 10 | MB WAY | Portugal | 5M+ users. W&B ships to Portugal. |

**Payment complaints and issues:**
- Trustpilot: generally positive but mixed. Refund complaints are a recurring theme.
- ComplaintsBoard: 0% resolution rate on 10 complaints. Refund disputes for $846+ unresolved.
- Sitejabber: 64 reviews, inconsistent refund experiences
- Multi brand shipping creates refund complexity: one order can contain items from different brands in different countries
- 7 day payout cycle to brands: slower than competitors

**Key strategic developments (2025 to 2026):**
1. US growth: from $3M to $45M+ in 5 years. US now ~50% of sales.
2. Profitability: second consecutive profitable year in 2024
3. Agentic commerce: CEO publicly exploring Stripe's agentic commerce protocol for AI driven shopping
4. B Corp certification: ethical and sustainable brand positioning
5. 2,000+ brand partners growing globally
6. AI integration: CEO hands on with AI projects across product and technology

**Yuno case references for the meeting:**

INDRIVE: Marketplace scaled 10 LATAM markets in under 8 months. 90% approval rate. 4.5%+ recovery. Similar multi country marketplace model.

RAPPI: 20+ PSPs orchestrated. 80% analyst reduction. Reconciliation cut by up to 90%. Relevant to W&B's multi brand, multi country reconciliation needs.

WINGO: 14% approval rate increase across 10+ countries. Shows multi market activation speed.

MCDONALD'S: +4.7% approval across 18 markets. Shows high volume multi market routing at scale.

**Key meeting angles:**

1. **30+ EU markets with only cards and BNPL**: Wolf & Badger ships to every EU country with duties included but offers no local European APMs. iDEAL, Bancontact, BLIK, Swish are all missing. Yuno activates all via one API.

2. **CEO already thinking about Stripe + agentic commerce**: George Graham publicly discussed Stripe's agentic protocol. He understands payment infrastructure innovation. Yuno conversation aligns with his tech forward mindset.

3. **2,000 brand payouts need orchestration**: Each brand gets paid monthly after commission and fee deductions. 7 day settlement across 30+ countries creates reconciliation complexity. Yuno's unified dashboard cuts analyst time by 80%.

4. **US growth demands payment optimization**: US went from $3M to $45M+ in 5 years and is now nearly 50% of revenue. Smart routing maximizes approval rates for this critical growth market.

5. **High AOV luxury marketplace**: Independent designer items are premium priced. Every declined transaction represents significant lost revenue. Smart routing + failover recovers up to 50% of failures.

6. **Marketplace peer comparison**: InDrive (marketplace, multi country) achieved 90% approval with Yuno. Rappi (marketplace, 20+ PSPs) cut reconciliation by 90%.

**Sources:**
- [Wolf & Badger FAQs (Payment Methods)](https://www.wolfandbadger.com/global/pages/help/faqs/)
- [Wolf & Badger Payment Methods (WhoAcceptsIt)](https://www.whoacceptsit.com/companies/wolf-and-badger/2087/)
- [Wolf & Badger Klarna US](https://www.klarna.com/us/store/fae5d85c-20bd-49b2-a327-be23acdc4669/Wolf-Badger/pay-with-klarna/)
- [Wolf & Badger Zip US](https://zip.co/us/store/wolf-badger)
- [Wolf & Badger Delivery (Shipping Countries)](https://www.wolfandbadger.com/us/pages/help/delivery)
- [Wolf & Badger Seller Terms](https://www.wolfandbadger.com/eu/pages/sellerterms/)
- [Wolf & Badger 2023 Year End Results (PR Newswire)](https://www.prnewswire.com/news-releases/wolf--badger-announces-strong-year-end-results-for-2023-championing-independent-brands-and-ethical-provenance-302032602.html)
- [Wolf & Badger Revenue (ecdb)](https://ecdb.com/resources/sample-data/retailer/wolfandbadger)
- [Wolf & Badger $100M+ Sales (Entrepreneur)](https://www.entrepreneur.com/starting-a-business/brothers-started-a-business-that-sees-100m-in-annual-sales/498923)
- [Wolf & Badger US Growth (Modern Retail)](https://www.modernretail.co/operations/marketplace-briefing-how-wolf-badger-is-winning-u-s-shoppers-despite-luxury-retails-slowdown/)
- [Wolf & Badger Luxury E Commerce (BoF)](https://www.businessoffashion.com/articles/technology/the-start-ups-defying-the-luxury-e-commerce-slump/)
- [Wolf & Badger Revenue (Yahoo Finance)](https://finance.yahoo.com/news/record-breaking-revenue-london-founded-152415573.html)
- [George Graham CEO Interview (Computer Weekly)](https://www.computerweekly.com/news/366638991/Interview-Wolf-Badger-CEO-George-Graham-on-getting-hands-on-with-AI)
- [George Graham Crunchbase](https://www.crunchbase.com/person/george-graham-2)
- [Wolf & Badger Leadership (Craft.co)](https://craft.co/wolf-badger/executives)
- [Wolf & Badger Guinness Ventures](https://www.guinnessgi.com/wolf-badger-ltd)
- [Wolf & Badger Trustpilot](https://www.trustpilot.com/review/www.wolfandbadger.com)
- [Wolf & Badger Sitejabber](https://www.sitejabber.com/reviews/wolfandbadger.com)
- [Wolf & Badger ComplaintsBoard](https://www.complaintsboard.com/wolf-badger-b137261)
- [Wolf & Badger Wikipedia](https://en.wikipedia.org/wiki/Wolf_&_Badger)
- [Wolf & Badger Crunchbase](https://www.crunchbase.com/organization/wolf-badger)
- [Yuno InDrive Case Study](https://y.uno/success-cases/indrive)
- [Yuno Rappi Case Study](https://y.uno/success-cases/rappi)
- [Yuno Wingo Case Study](https://y.uno/newsroom/wingo-improves-payment-efficiency-with-yuno-as-strategic-partner)
- [Yuno Platform Overview](https://y.uno/)
