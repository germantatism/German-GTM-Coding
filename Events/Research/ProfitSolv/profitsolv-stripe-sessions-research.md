# PROFITSOLV | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: ProfitSolv
=======================================

Logo: https://media.licdn.com/dms/image/v2/C4E0BAQGpK4qFq0MXGQ/company-logo_200_200/company-logo_200_200/0/1630596588875/profitsolv_logo?e=2147483647&v=beta&t=profitsolv
Nombre merchant: ProfitSolv

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Fragmented Payment Stack
Tittle_Pain Point_2: IOLTA Compliance Risk
Tittle_Pain Point_3: Card Fee Margin Erosion
Tittle_Pain Point_4: No Cross-Border Rails
Tittle_Pain Point_5: Single Processor Exposure

Desc_Pain Point_1: CosmoLexPay, TimeSolvPay, Tabs3Pay, and LexCharge each run separate payment integrations. No unified routing layer connects the four brands. Reconciling $20B in annual invoicing across siloed stacks creates operational drag.
Desc_Pain Point_2: Every U.S. state enforces different IOLTA trust account rules. Misrouted funds trigger bar disciplinary action. Processing client retainers through generic gateways without automated trust/operating splits exposes 21,000 firms to compliance violations.
Desc_Pain Point_3: Credit card fees of 1.5% to 3.5% per transaction eat into law firm margins on high-value invoices. 68% of legal professionals cite payment collection as their biggest hurdle. No smart routing to steer volume toward lower-cost ACH or eCheck rails.
Desc_Pain Point_4: ProfitSolv serves firms on 4 continents but offers only U.S.-centric payment rails: credit cards, ACH, and eCheck. International clients paying cross-border invoices face wire transfer fees of $15 to $50, with no local APM alternatives available.
Desc_Pain Point_5: LexCharge underpins all four payment brands with a single processing backbone. Any degradation blocks payments for 21,000 firms processing $20B in invoicing annually. No failover processor exists if LexCharge experiences downtime or declines.

SLIDE 1: PSP TOPOLOGY

PSP_1: LexCharge (core payment processor for all brands)
PSP_2: LawPay (CosmoLex integration partner)
PSP_3: ACH/eCheck (via LexCharge)
PSP_4: Credit/Debit Cards (via LexCharge)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix (Brazil)
Local_M_2: SEPA Direct Debit (EU)
Local_M_3: iDEAL (Netherlands)
Local_M_4: UPI (India)
Local_M_5: Bancontact (Belgium)
Local_M_6: BLIK (Poland)
Local_M_7: PayPay (Japan)
Local_M_8: Boleto (Brazil)
Local_M_9: OXXO (Mexico)
Local_M_10: GiroPay (Germany)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each invoice payment to the lowest-cost rail by amount and method. Steer high-value invoices to ACH (0.5% to 1.5%) instead of cards (1.5% to 3.5%), recovering margin across $20B in annual invoicing. Per-transaction routing optimizes every payment across all four brands.
Desc_Yuno_Cap2: Automatic cascade eliminates single-LexCharge dependency. When the primary processor declines, Yuno reroutes in milliseconds to a backup acquirer. Up to 50% recovery on failed transactions ensures 21,000 firms never miss a client payment.
Desc_Yuno_Cap3: Activates the APMs international clients demand: SEPA DD across Europe, Pix in Brazil, UPI in India, iDEAL in Netherlands, BLIK in Poland, PayPay in Japan, Boleto in Brazil, OXXO in Mexico. One API, 1,000+ methods, zero per-market builds for firms on 4 continents.
Desc_Yuno_Cap4: One dashboard unifying CosmoLexPay, TimeSolvPay, Tabs3Pay, and LexCharge into a single view. IOLTA-compliant trust/operating splits automated in real time. NOVA fraud engine with 75% fewer false positives. Centralized analytics across all 21,000 client firms.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**ProfitSolv at a glance:**
- Founded: 2020 by Lightyear Capital and Greater Sum Ventures
- Headquarters: Knoxville, Tennessee (2035 Lakeside Centre Way)
- CEO: Kelley Castell (20 years experience, ex-First Data, Bluefin Payment Systems)
- Employees: ~157 across 4 continents (North America, Asia, Europe)
- Funding: $89.3M raised (FTV Capital, Ares Management, Lightyear Capital)
- Clients: 21,000+ professional services firms across the United States
- Invoicing Volume: $20B+ processed annually
- Revenue: Estimated $25M to $100M annually

**Product Portfolio (9 brands):**
- CosmoLex: Cloud-based law practice management with CosmoLexPay
- Rocket Matter: Legal billing and practice management
- Tabs3: Legacy practice management with Tabs3Pay
- TimeSolv: Legal billing and timekeeping with TimeSolvPay
- LexCharge: Core payment processing platform (acquired with Rocket Matter in 2020)
- Law Ruler: Legal CRM
- Clear View Social: Social media platform for professionals
- TitleTap: Website design and marketing for law firms
- ImagineTime: Practice management for accounting firms
- Orion: Practice management platform

**Confirmed PSPs / Payment Rails:**
- LexCharge: Core payment processor powering CosmoLexPay, TimeSolvPay, Tabs3Pay
- LawPay: Integration partner with CosmoLex (included in subscription)
- Credit/Debit Cards: Visa, Mastercard accepted across all brands
- ACH Payments: Bank-to-bank transfers (0.5% to 1.5% fees)
- eCheck: Electronic check processing via ACH network
- No payment orchestrator detected
- No international/local APMs detected

**Market Context:**
- Legal practice management software market: $2.68B in 2025, growing at 11.9% CAGR
- U.S. legal services market: $1.08 trillion in 2026
- Industry is highly fragmented, no vendor holds more than 5% market share
- 68% of legal professionals report payment collection as their biggest challenge
- Over 60% of clients prefer electronic payment options

**Key Payment Challenges:**
- Fragmented payment stack: Four separate payment brands (CosmoLexPay, TimeSolvPay, Tabs3Pay, LexCharge) with no unified orchestration
- IOLTA compliance: Every U.S. state has different trust account rules; misrouted funds trigger bar disciplinary action
- Card processing fees: 1.5% to 3.5% per transaction on high-value legal invoices
- No international payment rails: Only U.S.-centric methods (cards, ACH, eCheck)
- Wire transfer costs: $15 to $50 per international transaction
- Single processor risk: LexCharge is the backbone for all payment brands

**Recent Developments (2025-2026):**
- June 2025: Secured strategic investment co-led by FTV Capital and existing investor Lightyear Capital
- April 2025: CosmoLex and Rocket Matter debuted automated workflows
- Strategy focus: Product innovation, strengthening payments, and accretive M&A
- Lightyear explored selling ProfitSolv before deciding to retain with FTV co-investment

**Key Meeting Angles:**
1. **$20B invoicing, fragmented payment stack** | Four separate payment brands with no unified routing. Orchestration could consolidate into a single dashboard with smart routing.
2. **21,000 firms, single-processor dependency** | All payment brands rely on LexCharge. Any outage blocks payments for the entire client base with no failover.
3. **IOLTA compliance automation** | Automated trust/operating splits with real-time compliance monitoring eliminates bar violation risk across 50 states.
4. **Card fee margin recovery** | Smart routing from cards (3.5%) to ACH (1.5%) on high-value invoices could save millions across $20B in annual volume.
5. **International expansion opportunity** | Operations on 4 continents but zero local APMs. European, LATAM, and Asian clients lack native payment options.
6. **M&A-driven growth needs scalable payments** | Acquisition strategy adds new brands; orchestration layer unifies payments across any future acquisition instantly.

**Sources:**
- [ProfitSolv Official Website](https://www.profitsolv.com/)
- [ProfitSolv Legal Payments](https://www.profitsolv.com/legal/payments/)
- [ProfitSolv Strategic Investment (Yahoo Finance)](https://finance.yahoo.com/news/profitsolv-secures-strategic-investment-co-120000250.html)
- [ProfitSolv Strategic Investment (LawNext)](https://www.lawnext.com/2025/06/profitsolv-parent-to-multiple-law-practice-management-platforms-secures-substantial-strategic-investment.html)
- [FTV Capital Investment in ProfitSolv](https://ftvcapital.com/2025/profitsolv-secures-strategic-investment-co-led-by-ftv-capital-and-existing-investor-lightyear-capital/)
- [ProfitSolv Formation (BusinessWire)](https://www.businesswire.com/news/home/20200924005195/en/Lightyear-Capital-Announces-the-Formation-of-ProfitSolv)
- [CosmoLex and Rocket Matter Workflows (BusinessWire)](https://www.businesswire.com/news/home/20250401068118/en/CosmoLex-and-Rocket-Matter-Debut-Automated-Workflows-for-Busy-Law-Firms)
- [CosmoLexPay Details](https://www.cosmolex.com/blog/a-detailed-look-at-cosmolexpay/)
- [TimeSolvPay](https://www.timesolv.com/timesolvpay/)
- [Legal Practice Management Market Report](https://www.researchandmarkets.com/reports/5954691/legal-practice-management-software-market-report)
- [ProfitSolv Crunchbase](https://www.crunchbase.com/organization/profitsolv)
- [ProfitSolv LeadIQ](https://leadiq.com/c/profitsolv/612675e24f9095de4c8ffd36)
- [TitleTap Acquisition](https://titletap.com/articles/titletap-acquired-by-profitsolv/)
- [Tabs3 Acquisition (LawNext)](https://www.lawnext.com/2021/07/another-stealth-practice-management-acquisition-this-time-of-tabs3.html)
