# THOMSON REUTERS | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Thomson Reuters
=======================================

Logo: https://upload.wikimedia.org/wikipedia/commons/9/95/Thomson_Reuters_logo.svg
Nombre merchant: Thomson Reuters

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Fragmented Billing Stack
Tittle_Pain Point_2: Global E-Invoice Sprawl
Tittle_Pain Point_3: Slow Quoting Cycles
Tittle_Pain Point_4: LATAM Payment Gaps
Tittle_Pain Point_5: Multi-Currency Friction

Desc_Pain Point_1: Westlaw, CoCounsel, UltraTax, ONESOURCE across 126 offices in 75+ countries. Each product manages its own billing with no unified orchestration across $7.5B.
Desc_Pain Point_2: Pagero connects 90K customers to 14M companies for e-invoicing, but payment collection depends on fragmented local banking rails. 80+ countries mandate it.
Desc_Pain Point_3: Enterprise clients report slow response and long quoting cycles. Multi-year contracts with 15-22% maintenance fees plus implementation fees slow renewals.
Desc_Pain Point_4: LATAM drives CoCounsel and Tax growth, but the region needs Pix, Boleto, OXXO, PSE. Card-only billing creates friction for firms in Brazil, Mexico, Colombia.
Desc_Pain Point_5: 75+ countries but 75% US revenue means international billing in EUR, GBP, JPY, BRL faces elevated declines. US acquirers trigger foreign BIN flags from issuers.

SLIDE 1: PSP TOPOLOGY

PSP_1: Kotapay (ACH and credit card processing) PSP_2: Stripe (estimated for digital products) PSP_3: Enterprise invoicing (direct bank transfers) PSP_4: Pagero (e-invoicing network, 14M companies)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix (Brazil)
Local_M_2: Boleto (Brazil)
Local_M_3: OXXO (Mexico)
Local_M_4: PSE (Colombia)
Local_M_5: SEPA Direct Debit (EU)
Local_M_6: BACS Direct Debit (UK)
Local_M_7: UPI (India)
Local_M_8: Konbini (Japan)
Local_M_9: iDEAL (Netherlands)
Local_M_10: Bancontact (Belgium)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing Engine
Tittle_Yuno_Cap2: Failover + NOVA Recovery
Tittle_Yuno_Cap3: 1,000+ Local APMs
Tittle_Yuno_Cap4: Unified Global Dashboard

Desc_Yuno_Cap1: Route each renewal across Westlaw, CoCounsel, UltraTax, and ONESOURCE to the optimal acquirer by card BIN, issuer, and currency. With $7.5B across 75+ countries, even 1% auth uplift recovers $75M+. Smart Routing delivers +3-10% improvement.
Desc_Yuno_Cap2: When the primary processor declines a renewal or goes down, Yuno cascades to alternative acquirers in ms. NOVA AI recovers 75% of soft declines before they trigger subscription lapses. Livelo recovered 50% of failed transactions via Yuno.
Desc_Yuno_Cap3: Unlock Pix and Boleto for Brazil (LATAM growth driver), SEPA for EU enterprise clients, BACS for UK law firms, UPI for India, Konbini for Japan. One API activates every local method across 75+ markets. InDrive deployed 10 markets via Yuno.
Desc_Yuno_Cap4: Replace siloed billing across Kotapay, enterprise invoicing, and Pagero with one real-time dashboard. Monitor approval rates per product line, region, and method. Detect anomalies before they cascade into revenue loss across the $7.5B portfolio.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Thomson Reuters at a glance:**
- NYSE/TSX: TRI. Global provider of professional information services and software
- FY2025 Revenue: $7.476B (3% YoY growth); 2026 outlook: 7.5-8% organic growth
- Adjusted EBITDA margin: 39.2% (2025); targeting ~42% Q1 2026
- 26,000+ employees across 126 offices in 75+ countries
- Headquarters: Toronto, Ontario (Bay Adelaide Centre, 19 Duncan Street)
- ~75% of revenue generated in the US
- "Big 3" segments: Legal Professionals, Corporates, Tax & Accounting Professionals (9% organic growth in 2025)
- CoCounsel AI: 1M+ active professional users across 107 countries (Feb 2026)
- Pagero (ONESOURCE E-Invoicing): 90,000 customers connected to 14M companies globally
- $10B allocated for inorganic growth through 2027

**Confirmed PSPs / Payment Infrastructure:**
- Kotapay: partner for integrated ACH and credit card processing for Thomson Reuters firms
- Enterprise invoicing: direct bank transfers for large enterprise contracts
- Pagero: e-invoicing network connecting 90,000 customers to 14M companies (acquired for ~$800M)
- myPay Solutions: payroll processing platform (sold to IRIS Software Group)
- No third-party payment orchestrator detected
- Specific PSP for digital subscription products (Westlaw, CoCounsel) not publicly disclosed

**Key Pain Points:**
1. **Fragmented billing across product lines**: Each product (Westlaw, CoCounsel, UltraTax, ONESOURCE, Practical Law) likely manages its own billing stack. No unified orchestration visible across the portfolio.
2. **Global e-invoicing vs. payment collection gap**: Pagero handles e-invoicing for 80+ countries but payment collection from those invoices relies on fragmented local banking rails
3. **LATAM expansion without local methods**: Latin America is a stated growth driver for CoCounsel and Tax segments, but card-only billing creates friction in markets where Pix, Boleto, and OXXO dominate
4. **Enterprise billing complexity**: Multi-year contracts with maintenance fees (15-22%), implementation fees ($50K+ for enterprise), and tiered pricing create manual billing overhead
5. **Cross-border authorization challenges**: 25% of revenue is international, processed through what are likely US-based acquirers, causing elevated decline rates from foreign issuer BIN flags

**Missing Payment Methods / Regional Gaps:**
- LATAM: Pix, Boleto (Brazil, growth market), OXXO (Mexico), PSE (Colombia)
- Europe: SEPA Direct Debit (standard for B2B SaaS), iDEAL, Bancontact, Bizum
- UK: BACS Direct Debit (standard for recurring B2B payments in Thomson Reuters' London operations)
- Asia Pacific: UPI (India, major operations center), Konbini (Japan), bank transfer
- Middle East/Africa: local bank transfers, M-Pesa

**Key meeting angles:**
1. **CoCounsel global monetization**: 1M+ users across 107 countries need localized payment acceptance. Yuno enables CoCounsel subscriptions to be paid via SEPA in EU, Pix in Brazil, UPI in India, without building per-market billing infrastructure.
2. **Pagero payment completion**: Pagero delivers e-invoices to 14M companies, but getting paid on those invoices requires local payment acceptance. Yuno closes the loop from invoice issuance to payment collection with 1,000+ APMs.
3. **LATAM growth acceleration**: Latin America drives organic growth for CoCounsel and Tax segments. Yuno has proven LATAM infrastructure (InDrive: 10 markets, Rappi: zero implementation cost) and activates Pix, Boleto, OXXO, and PSE instantly.
4. **$10B M&A integration**: Thomson Reuters allocated $10B for acquisitions through 2027 ($850M deployed in 2025 alone). Each acquisition brings a new billing stack. Yuno provides a unified orchestration layer to consolidate payment operations across acquired entities.
5. **Enterprise billing simplification**: Complex multi-year contracts with tiered pricing and maintenance fees create manual overhead. Yuno's unified dashboard automates billing visibility and retry logic across all product lines and geographies.
6. **Cross-border auth optimization**: 25% of revenue is international. Smart Routing to local acquirers in each market eliminates foreign BIN flags and delivers +3-10% authorization improvement on international subscriptions.

**Thomson Reuters Leadership:**
- Steve Hasker: President and CEO
- Mike Eastwood: CFO
- David Wong: EVP and President, Legal Professionals
- Elizabeth Falk: EVP and President, Tax & Accounting Professionals
- Kirsty Roth: Chief Operations & Technology Officer
- Board Chair: David K.R. Thomson

**Recent corporate developments:**
- Feb 2026: CoCounsel reaches 1 million active professional users across 107 countries
- Feb 2026: Full-year 2025 results: $7.476B revenue, 9% organic growth in "Big 3" segments
- 2026 Outlook: 7.5-8% organic growth, ~100 basis points EBITDA margin expansion
- Sep 2025: Acquired Additive AI (AI-powered tax document processing)
- 2025: Acquired SafeSend; ~$850M deployed in strategic acquisitions
- Jan 2024: Acquired majority interest in Pagero (~$800M) for global e-invoicing
- 2024: Launched ONESOURCE E-Invoicing platform
- 2024: Deloitte strategic alliance for end-to-end global e-invoicing and e-reporting
- Ongoing: $10B allocated for M&A through 2027; $1B share repurchase in 2025
- Ongoing: myPay Solutions sold to IRIS Software Group

**Competitive Context:**
- Competes with LexisNexis (RELX), Wolters Kluwer, Bloomberg Law for legal/tax SaaS
- Pagero competes with Tungsten Network, Basware, Coupa for e-invoicing
- CoCounsel AI competes with Harvey AI, Luminance, Ironclad for legal AI
- All competitors face similar global billing challenges across 100+ countries

**Sources:**
- [Thomson Reuters FY2025 Results (PR Newswire)](https://www.prnewswire.com/news-releases/thomson-reuters-reports-fourth-quarter-and-full-year-2025-results-302680103.html)
- [Thomson Reuters Q3 2025 Results (PR Newswire)](https://www.prnewswire.com/news-releases/thomson-reuters-reports-third-quarter-2025-results-302603936.html)
- [CoCounsel Reaches 1M Users (PR Newswire)](https://www.prnewswire.com/news-releases/one-million-professionals-turn-to-cocounsel-as-thomson-reuters-scales-ai-for-regulated-industries-302694903.html)
- [CoCounsel 1M Users (LawSites)](https://www.lawnext.com/2026/02/three-years-after-launching-as-first-ai-legal-assistant-cocounsel-reaches-1-million-users-and-thomson-reuters-teases-whats-ahead.html)
- [Thomson Reuters Pagero Acquisition (PR Newswire)](https://www.prnewswire.com/news-releases/thomson-reuters-corporation-acquires-majority-interest-in-pagero--a-world-leader-in-e-invoicing-302034456.html)
- [Pagero E-Invoicing (Pagero)](https://www.pagero.com/)
- [Thomson Reuters ONESOURCE E-Invoicing (Insightful Accountant)](https://insightfulaccountant.com/accounting-tech/vendor-news/thomson-reuters-unveils-onesource-einvoicing/)
- [Deloitte + Thomson Reuters Alliance (Deloitte)](https://www.deloitte.com/global/en/about/press-room/deloitte-and-thomson-reuters-launch-a-strategic-alliance-to-support-end-to-end-global-e-invoicing-and-e-reporting.html)
- [Kotapay + Thomson Reuters Partnership](https://www.kotapay.com/thomsonreuters)
- [Thomson Reuters Revenue (MacroTrends)](https://www.macrotrends.net/stocks/charts/TRI/thomson-reuters-corp/revenue)
- [Thomson Reuters Wikipedia](https://en.wikipedia.org/wiki/Thomson_Reuters)
- [Thomson Reuters Global Offices (HighPerformr)](https://www.highperformr.ai/company/thomson-reuters)
- [Thomson Reuters Subscription Pricing (Vendr)](https://www.vendr.com/marketplace/thomson-reuters)
- [Thomson Reuters Customer Stories (Conga)](https://conga.com/customer-stories/thomson-reuters)
- [Thomson Reuters Logo (Wikimedia)](https://commons.wikimedia.org/wiki/File:Thomson_Reuters_logo.svg)
