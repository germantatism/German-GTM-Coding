# SUNBIT | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Sunbit
═══════════════════════════════════════

Logo: https://brandfetch.com/sunbit.com
Nombre merchant: Sunbit

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: US Only, No Global Rails
Tittle_Pain Point_2: Single Issuer Dependency
Tittle_Pain Point_3: Card Lockout Failures
Tittle_Pain Point_4: No Real Time Failover
Tittle_Pain Point_5: Fragmented Regulation

Desc_Pain Point_1: 20,000+ locations locked into US only. Global BNPL growing 22% CAGR but Sunbit has zero international presence. No LatAm, Europe, or APAC infrastructure.
Desc_Pain Point_2: TAB Bank is sole issuer and loan originator for all products. Any disruption halts 100% of Sunbit Card transactions and financing approvals instantly.
Desc_Pain Point_3: Users report cards locked without warning for 24 to 48 hours. No alternate routing when the processor rejects. Merchants lose sales while customers wait.
Desc_Pain Point_4: When Stripe or TAB Bank rails decline, no automatic cascade to a backup processor. Zero retry logic across BNPL and card products loses recoverable volume.
Desc_Pain Point_5: CFPB dropped BNPL enforcement while New York enacted sweeping licensing laws. State by state patchwork creates growing compliance burden for expansion.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (merchant checkout integration partner, Sep 2024)
PSP_2: TAB Bank (sole card issuer and loan originator, Visa license)
PSP_3: Visa Network (sole card network for Sunbit Card)
PSP_4: J.P. Morgan / Mizuho / Waterfall (debt warehouse facility)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: OXXO
Local_M_3: PSE
Local_M_4: Boleto
Local_M_5: SPEI
Local_M_6: Nequi
Local_M_7: UPI
Local_M_8: SEPA Direct Debit
Local_M_9: iDEAL
Local_M_10: Mercado Pago

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each BNPL disbursement and card transaction to the best acquirer by BIN, issuer, and geography. With $260M+ revenue and 20,000+ locations, a 3 to 10% auth uplift recovers millions in lost volume annually across auto, dental, and optical verticals.
Desc_Yuno_Cap2: Automatic cascade when TAB Bank or Visa rails decline. Sunbit has zero retry logic and users report 24 to 48 hour card lockouts. Yuno reroutes failed transactions to alternate acquirers in milliseconds, recovering up to 50% of soft declines.
Desc_Yuno_Cap3: Unlocks international markets Sunbit cannot reach today: Pix in Brazil, OXXO and SPEI in Mexico, PSE in Colombia, UPI in India, SEPA in Europe, Mercado Pago across Latin America. One API, 1,000+ payment methods. No per market engineering build needed.
Desc_Yuno_Cap4: Single dashboard replacing Sunbit's fragmented Stripe + TAB Bank + Visa + J.P. Morgan stack. NOVA anti fraud engine reduces chargebacks by up to 75%. Real time approval monitoring, centralized reconciliation, and millisecond anomaly detection across all providers and geographies.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Sunbit at a glance:**
- BNPL / point of sale lending fintech, private, HQ Los Angeles, California
- Founded: 2016 by Arad Levertov (CEO), Ornit Dweck-Maizel (CTO), Tal Riesenfeld (CRO), Tamir Hazan (AI/ML)
- Revenue: $260M (2024 annualized per Latka), $191M (2023), $129M (2022). Three year revenue growth: 1,021%
- Valuation: $1.1B (unicorn status since Series D, May 2021)
- Equity funding: $251.7M total raised. Series D: $130M led by Group 11 and Zeev Ventures
- Debt facilities: $355M warehouse (J.P. Morgan, Mizuho, Waterfall, Nov 2024) + $310M (Citi, Ares, Jan 2024) + $250M (Credit Suisse, Waterfall) + $200M ABS (Aug 2025)
- Employees: ~500 (2025)
- Merchants: 20,000+ brick and mortar locations, 7,300 customers
- 130,000+ service professionals certified to offer Sunbit
- Forbes Fintech 50: 3 consecutive years (2024, 2025, 2026)
- Inc. 5000: 4 consecutive years (2022 through 2025)
- 90%+ approval rate, 30 second application, no fees of any kind
- Products: POS BNPL (3 to 72 months), Sunbit Card (no fee Visa credit card via TAB Bank), Co branded cards (Ollie's Bargain Outlet Visa)

**Confirmed PSPs and Partners:**
- Stripe: strategic integration partner since September 2024. Merchants on Stripe can toggle Sunbit BNPL on their dashboard. Stripe redirects customers to Sunbit for installment plan selection
- TAB Bank (Transportation Alliance Bank): sole card issuer and loan originator for all financing products, pursuant to Visa U.S.A. license
- Visa: sole card network for Sunbit Card and co branded card products
- J.P. Morgan, Mizuho Bank, Waterfall Asset Management: $355M debt warehouse facility partners
- Citi, Ares Management: $310M debt facility partners
- No payment orchestrator detected

**Key verticals served:**
- Auto dealerships: ~5,000 service centers, endorsed by 7 OEMs (Acura, Honda, Infiniti, Kia, Mercedes-Benz, Nissan, Volkswagen). 18 of top 25 auto groups. 40%+ market penetration
- Dental: 9,000+ locations, fastest growing and second largest dental patient financing solution
- Optical / eyewear: significant presence
- Veterinary: growing segment
- Retail: co branded cards with Ollie's Bargain Outlet, expanding retail partnerships
- Healthcare / medspa / home services: newer verticals via Stripe integration

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (100% of revenue, sole market)
  Supported: Visa card rails, POS BNPL via Stripe integration, direct merchant integrations
  Missing: No alternative card networks (Mastercard, Amex, Discover), no ACH based alternatives
  Note: Sunbit operates exclusively in the US across 46 states

MARKET 2: Mexico (zero presence, high potential)
  Supported: None
  Missing: OXXO, SPEI, CoDi, local debit cards, Mercado Pago
  Note: OXXO serves 50M+ unbanked Mexicans. Auto service and dental are massive markets

MARKET 3: Brazil (zero presence, high potential)
  Supported: None
  Missing: Pix, Boleto, local installment cards, Mercado Pago
  Note: Pix handles 70%+ of digital payments. BNPL for dental and auto is underserved

MARKET 4: Colombia (zero presence, high potential)
  Supported: None
  Missing: PSE, Nequi, Efecty, Daviplata, local installment cards
  Note: PSE dominates online payments. Dental and auto services growing fast

MARKET 5: Europe (zero presence)
  Supported: None
  Missing: SEPA Direct Debit, iDEAL, Sofort, Bancontact, Giropay
  Note: BNPL regulation maturing in EU. Dental and optical financing markets are large

**Leadership team (key contacts):**
- Arad Levertov: Co-founder and CEO. Former COO at Enova International ($800M business). Israeli Navy Seals Major. MBA Duke Fuqua
- Ornit Dweck-Maizel: Co-founder and CTO. 15+ years R&D at Intel. BSc Ben-Gurion, MBA Tel Aviv University
- Tal Riesenfeld: Co-founder and Chief Revenue Officer. Former VP Sales at Eyeview. Roles at Google and HP. MBA Harvard
- Shai Terem: CFO. Former President/CEO of Markforged (NYSE: MKFG). MBA University of Chicago Booth
- Shachar G. Scott: CMO. 25+ years at Meta, Bumble, Snap, Apple. VP Global Marketing at Meta Reality Labs
- James Paris: Chief Capital Officer. Former CEO/EVP at Avant. Managing Director at BMO, UBS, Barclays. JD Harvard Law
- Bill Walsh: Chief Customer Officer. Former General Manager at LendingClub. MIT graduate
- Oded Vakrat: VP Platform Partnerships. Former CEO of Earny (50M+ transactions)
- Katey Berman: VP Customer Success. Leads 100 person team supporting 10K+ merchants and 1M customers
- Jay Letwat: VP Dental. 20+ years in disruptive tech

**Key competitive vulnerabilities:**
- 100% US market, zero international infrastructure while competitors like Klarna operate in 45 countries
- Single bank dependency (TAB Bank) for all card and lending products
- Stripe partnership makes Sunbit a payment method, not a processor. Sunbit depends on Stripe for merchant distribution
- Card lockout complaints: users report 24 to 48 hour lockouts with no alternate processing path
- BNPL regulatory fragmentation: NY licensing law, CA CFL compliance, MD loan classification, each state adds complexity
- Co branded card strategy (Ollie's) requires Visa rails only, limiting payment diversity
- No orchestration layer: each vertical (auto, dental, optical) runs on same TAB Bank + Visa stack with no redundancy

**Key meeting angles:**
1. **Stripe dependency paradox** | Sunbit is a payment method inside Stripe, not a standalone processor. Yuno orchestration gives Sunbit control of its own transaction routing independent of any single PSP
2. **TAB Bank single point of failure** | One bank, one card network for a $260M revenue unicorn. Yuno multi acquirer routing eliminates this concentration risk
3. **International expansion unlock** | 20,000+ US locations but zero global presence. Yuno enables instant expansion to Latin America with Pix, OXXO, PSE, Boleto via single API
4. **Card lockout recovery** | 24 to 48 hour lockouts with no failover. Yuno automatic retry and cascade recovers up to 50% of soft declines in milliseconds
5. **BNPL regulatory shield** | State by state patchwork (NY, CA, MD) demands flexible payment routing. Yuno routes transactions through compliant corridors per jurisdiction
6. **OEM endorsed scale** | 7 auto OEMs, 18 of top 25 auto groups, 5,000 dealerships. Adding Yuno APMs (Pix, OXXO) to this network unlocks LatAm auto service financing
7. **Debt facility optimization** | $1.1B+ in debt facilities from J.P. Morgan, Citi, Ares. Higher approval rates via Smart Routing directly improve loan portfolio performance

**Sources:**
- [Sunbit Homepage](https://sunbit.com/)
- [Sunbit Leadership Team](https://sunbit.com/leadership/)
- [Sunbit Card / TAB Bank Issuing](https://sunbit.com/card/)
- [Sunbit + Stripe Partnership (Sep 2024)](https://www.pymnts.com/bnpl/2024/stripe-and-sunbit-team-to-expand-in-person-bnpl-offerings/)
- [Stripe Documentation: Sunbit Payments](https://docs.stripe.com/payments/sunbit)
- [Sunbit Partners with Stripe (BusinessWire)](https://www.businesswire.com/news/home/20240924204309/en/Sunbit-Partners-with-Stripe-to-Bring-Buy-Now-Pay-Later-to-More-In-Person-Services)
- [Sunbit $130M Series D, $1.1B Valuation](https://sunbit.com/knowledge-center/eyewear/sunbit-announces-130m-series-d-round-and-a-1-billion-valuation/)
- [Sunbit $355M Debt Facility (J.P. Morgan)](https://fintech.global/2024/11/05/sunbit-partners-with-j-p-morgan-for-a-355m-debt-facility/)
- [Sunbit $310M Debt Facility (Citi, Ares)](https://fintech.global/2024/01/29/sunbit-a-fintech-pioneer-bags-310m-from-citi-and-ares-to-fuel-bnpl-growth/)
- [Sunbit $200M ABS Milestone](https://labusinessjournal.com/finance/sunbit-lands-200-million-abs-milestone/)
- [Sunbit Inc. 5000 (1,021% Growth)](https://sunbit.com/knowledge-center/press/sunbit-makes-second-appearance-on-the-inc-5000-at-no-576-in-2023-with-three-year-revenue-growth-of-1021-percent/)
- [Sunbit Forbes Fintech 50 2026](https://sunbit.com/knowledge-center/press/forbes-2026-fintech-50/)
- [Sunbit Forbes Fintech 50 2024](https://sunbit.com/knowledge-center/press/the-future-of-personal-finance-fintech-50-2024/)
- [Sunbit Inc. 5000 2025 (4th Year)](https://www.businesswire.com/news/home/20250812678015/en/Sunbit-is-on-the-2025-Inc.-5000-List-of-Americas-Fastest-Growing-Private-Companies-for-4th-Consecutive-Year)
- [Sunbit 7 OEM Endorsements](https://sunbit.com/knowledge-center/auto/endorsed/)
- [Sunbit 5,000 Auto Dealerships](https://sunbit.com/knowledge-center/auto/sunbit-now-offered-in-nearly-5000-auto-dealerships/)
- [Sunbit 20,000+ Locations](https://sunbit.com/knowledge-center/press/sunbits-point-of-sale-technology-is-now-available-in-more-than-20000-brick-and-mortar-service-providers-in-the-us/)
- [Sunbit Revenue $260M (Latka)](https://getlatka.com/companies/sunbit)
- [Sunbit BBB Complaints](https://www.bbb.org/us/ca/los-angeles/profile/consumer-finance-companies/sunbit-inc-1216-1268871/complaints)
- [Sunbit WalletHub Reviews](https://wallethub.com/profile/sunbit-15194023i)
- [Sunbit Brand Assets (Brandfetch)](https://brandfetch.com/sunbit.com)
- [Sunbit Co-Branded Cards (Ollie's)](https://sunbit.com/knowledge-center/the-sunbit-card/ollies-partners-with-sunbit-to-offer-a-new-co-branded-visa-credit-card/)
- [CFPB BNPL Rule Rescission 2025](https://www.consumerfinancemonitor.com/2025/06/20/cfpb-will-not-issue-revised-bnpl-rule/)
- [New York BNPL Regulation 2026](https://www.gtlaw.com/en/insights/2025/6/new-york-enacts-landmark-buy-now-pay-later-regulation-amid-federal-regulatory-recalibration)
- [BNPL Regulatory Patchwork (Payments Dive)](https://www.paymentsdive.com/news/regulatory-patchwork-vexes-bnpl/806120/)
- [Sunbit Crunchbase Profile](https://www.crunchbase.com/organization/sunbit)
- [Sunbit CBInsights Profile](https://www.cbinsights.com/company/sunbit)
