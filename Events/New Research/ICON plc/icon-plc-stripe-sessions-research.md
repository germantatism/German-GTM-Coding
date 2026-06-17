# ICON PLC | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: ICON plc
=======================================

Logo: https://cdn.brandfetch.io/iconplc.com/w/512/h/512/logo
Nombre merchant: ICON plc

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: 53-Country Payout Maze
Tittle_Pain Point_2: Investigator Pay Delays
Tittle_Pain Point_3: VAT Reclaim Leakage
Tittle_Pain Point_4: Multi-Currency Overhead
Tittle_Pain Point_5: No Routing Optimization

Desc_Pain Point_1: Investigator payments in 53 countries via APECS, 130+ staff. Each country has different rails, regulations, methods. No orchestration to optimize routing.
Desc_Pain Point_2: Targets 90%+ payments within 30 days, but 400+ active studies create validation delays. Failed transfers in India, Brazil, Japan need manual rerouting.
Desc_Pain Point_3: 800+ regulatory reports/yr for Sunshine/EFPIA. VAT reclaim saves sponsors 20% of payment value but fragmented rails across 53 countries add overhead.
Desc_Pain Point_4: $1B+ in payouts over 3 years, 53 countries, dozens of currencies. Each corridor has different fees, settlement times, compliance rules compounding costs.
Desc_Pain Point_5: $300M+/yr in investigator payments with no smart routing for lowest-cost rails. 1% routing improvement at this volume = $3M+ in annual savings.

SLIDE 1: PSP TOPOLOGY

PSP_1: APECS (proprietary platform)
PSP_2: Bank wire transfers
PSP_3: Stripe (likely for digital/SaaS tools)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: UPI (India)
Local_M_2: PIX (Brazil)
Local_M_3: SEPA Instant (Europe)
Local_M_4: Konbini (Japan)
Local_M_5: PromptPay (Thailand)
Local_M_6: BLIK (Poland)
Local_M_7: SPEI (Mexico)
Local_M_8: PayNow (Singapore)
Local_M_9: FPS (Hong Kong)
Local_M_10: DuitNow (Malaysia)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each investigator payment to the lowest-cost, fastest-settling rail for that country and currency. With $300M+ annually across 53 countries, optimizing routing by 3-5% on bank fees alone could save ICON $9-15M per year while accelerating settlement times for research sites.
Desc_Yuno_Cap2: When a bank transfer fails in India, Brazil, or Japan, Yuno automatically retries through alternative local rails in milliseconds. Up to 50% recovery on failed payouts protects ICON's 90%+ on-time payment target and preserves critical relationships with research sites globally.
Desc_Yuno_Cap3: Replace slow international wires with local rails: UPI for India, PIX for Brazil, SEPA Instant for Europe, PromptPay for Thailand. One API, 1,000+ methods. Investigators get funds faster in local currency, improving site retention across 400+ studies.
Desc_Yuno_Cap4: One dashboard for ICON's investigator payments across 53 countries, all currencies, all rails. Real-time status tracking by study, site, and country. Centralized Sunshine/EFPIA compliance reporting, reducing the 800+ annual regulatory reports burden.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**ICON plc at a glance:**
- World-leading clinical research organization (CRO) for pharmaceutical, biotech, and medical device companies
- Founded: 1990 by John Climax and Ronan Lambe in Dublin, Ireland
- Public company: NASDAQ: ICLR
- Revenue: $8.282B (FY2024); Q1 2025 revenue: $2.001B
- 2025 guidance: $7.75B-$8.15B (later withdrawn due to accounting investigation)
- Adjusted EBITDA: $1.736B or 21.0% of revenue (FY2024)
- Employees: ~40,100 (December 2025) across 97 locations in 55 countries
- Service delivery in 93 countries total through local staff and partners
- 11,000+ oncology and haematology specialists
- 840+ oncology studies in the past five years

**Investigator Payments division:**
- 130+ staff processing payments in 53 countries
- 400+ active studies across all therapeutic areas
- 200,000+ payments totaling $1B+ processed in last 3 years
- Payment managers average 12+ years experience
- Target: 90%+ payments within 30 days of invoice receipt
- Technology: APECS platform for complex trial payment designs
- 800+ regulatory reports annually (Sunshine Law, EFPIA)
- In-house VAT management saving sponsors up to 20% of payment value

**Confirmed PSPs / Payment infrastructure:**
- APECS: proprietary investigator payment platform
- Bank wire transfers: primary method for investigator payments globally
- Stripe: likely used for internal SaaS tools and digital subscriptions
- No payment orchestrator detected for investigator payment flows

**Recent developments (caution):**
- Audit Committee investigation initiated October 2025 into accounting practices
- Focus on revenue recognition in fiscal years 2023-2025
- Previously issued 2025 guidance withdrawn
- Q1 2025 revenue still strong at $2.001B

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (largest revenue market)
  Currently offer: Bank wire, ACH
  Missing: Instant ACH, payment status tracking for sites
  US investigator sites expect fast, transparent payments. Manual wire processes create delays and support overhead.

MARKET 2: India (growing clinical trial market)
  Currently offer: International bank wire (USD)
  Missing: UPI, IMPS, NEFT, INR local rails
  India is the fastest-growing clinical trial destination. UPI enables instant settlement at near-zero cost compared to international wires.

MARKET 3: Europe (28+ countries)
  Currently offer: SEPA Credit Transfer, bank wire
  Missing: SEPA Instant, local instant payment rails per country
  SEPA Instant settles in seconds vs. 1-2 days for standard SEPA. Investigators in 27+ EU countries would benefit from real-time payments.

MARKET 4: Brazil (emerging CRO market)
  Currently offer: International bank wire
  Missing: PIX, TED, local bank transfer
  PIX processes instantly and is free for recipients. Brazilian investigator sites receiving international wires face 3-5 day delays and high bank fees.

MARKET 5: Japan (major pharma market)
  Currently offer: Bank wire (furikomi)
  Missing: Faster Payments, optimized local bank routing
  Japan is the third-largest pharmaceutical market. Optimized local routing could reduce settlement times and fees for Japanese research sites.

**Key meeting angles:**
1. **$1B+ in payouts** | ICON processed over $1B in investigator payments in 3 years across 53 countries. Even 1% routing optimization is $3M+ in savings
2. **90% on-time target** | Failed bank transfers require manual rerouting. Failover automation protects the on-time KPI that drives site relationships
3. **53-country complexity** | Each country has different rails, currencies, and regulations. Orchestration reduces the operational burden on 130+ payment staff
4. **VAT reclaim opportunity** | Up to 20% of payment value recoverable through VAT management. Better payment routing data improves reclaim accuracy
5. **Accounting investigation** | ICON is under scrutiny for revenue recognition. Transparent, auditable payment flows become even more critical
6. **Competitive CRO landscape** | Competitors like IQVIA, Parexel, and Covance investing in payment modernization. Slow investigator payments are a site retention risk

**Sources:**
- [ICON plc Official Website](https://www.iconplc.com/)
- [ICON Investigator Payments](https://www.iconplc.com/solutions/clinical-scientific-operations/investigator-payments)
- [ICON Facts and Figures](https://www.iconplc.com/news-events/mediakit/facts-and-figures)
- [ICON Q4/FY2024 Results](https://www.iconplc.com/news-events/press-releases/icon-reports-fourth-quarter-and-full-year-2024-results)
- [ICON Q1 2025 Results](https://www.iconplc.com/news-events/press-releases/icon-report-first-quarter-2025-results)
- [ICON Q3 2025 Results](https://www.iconplc.com/news-events/press-releases/icon-reports-third-quarter-2025-results)
- [ICON Accounting Investigation Update](https://www.iconplc.com/news-events/press-releases/icon-plc-provides-update-timing-fourth-quarter-and-full-year-2025)
- [ICON Wikipedia](https://en.wikipedia.org/wiki/ICON_PLC)
- [ICON Asia Pacific](https://www.iconplc.com/about/icon-in-asia-pacific)
- [ICON at a Glance](https://www.iconplc.com/about/icon-glance)
- [Brandfetch: ICON plc Logo](https://brandfetch.com/iconplc.com)
- [MacroTrends: ICON Revenue](https://www.macrotrends.net/stocks/charts/ICLR/icon/revenue)
