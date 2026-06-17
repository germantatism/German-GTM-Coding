# REMITLY | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Remitly
=======================================

Logo: https://companieslogo.com/img/orig/RELY-fad5c4f3.png
Nombre merchant: Remitly

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Payout Partner Fragility
Tittle_Pain Point_2: Prefunding Capital Drag
Tittle_Pain Point_3: Corridor Speed Gaps
Tittle_Pain Point_4: Funding Method Limits
Tittle_Pain Point_5: Fraud Loss at Scale

Desc_Pain Point_1: Remitly disburses to 4.2B bank accounts, 1.2B mobile wallets, and 460K cash points across 170+ countries. Each payout partner is a separate integration. One partner outage in a top corridor (Philippines, India, Mexico) blocks thousands of transfers instantly.
Desc_Pain Point_2: Remitly prefunds local payout partner balances to enable fast settlement. At $74.9B annual send volume, working capital tied up in prefunding exposes the company to FX risk and limits how quickly new corridors can scale without additional capital.
Desc_Pain Point_3: Guaranteed delivery times are a key brand promise, but user reviews cite frequent delays. Bank deposit payouts in some corridors take 2 to 5 days. Real-time local rails (Pix, SPEI, UPI) are not universally activated across all 5,100 corridors.
Desc_Pain Point_4: Bank account funding is only available in U.S., UK, Canada, and Australia. Senders in 20+ European countries can only fund via card or SEPA. No Open Banking, Klarna, or local debit rails in most send-from markets, limiting conversion.
Desc_Pain Point_5: Transaction loss rate guidance is 9 to 13 basis points for 2026. At $74.9B send volume, that is $67M to $97M in annual fraud losses. ML models reduced intervention by 25%, but multi-rail fraud orchestration across card, ACH, and wallet rails does not exist.

SLIDE 1: PSP TOPOLOGY

PSP_1: Bridge / Stripe (stablecoin payouts)
PSP_2: Circle (USDC treasury/wallet)
PSP_3: ACH / SEPA (fiat funding rails)
PSP_4: Visa / Mastercard (card funding)
PSP_5: Local payout banks (170+ countries)
PSP_6: Mobile money networks (M-Pesa, GCash, etc.)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Open Banking (UK/EU send)
Local_M_2: Pix Instant (Brazil payout)
Local_M_3: SPEI Instant (Mexico payout)
Local_M_4: UPI (India payout)
Local_M_5: OXXO (Mexico cash)
Local_M_6: Nequi (Colombia)
Local_M_7: FPS Instant (UK send)
Local_M_8: PayNow (Singapore)
Local_M_9: BLIK (Poland send)
Local_M_10: Mercado Pago (LatAm)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each remittance through the optimal payout partner by corridor, speed, and cost. At $74.9B send volume across 5,100 corridors, selecting the cheapest and fastest disbursement rail per transaction recovers basis points on every transfer. Smart Routing delivers +3 to 10% improvement on payout success rates.
Desc_Yuno_Cap2: Automatic cascade across payout partners eliminates single-partner dependency. When a bank payout fails in the Philippines or India, Yuno reroutes to the next available disbursement partner in milliseconds. Up to 50% recovery on failed payouts, protecting Remitly's guaranteed delivery promise to 9.3M active customers.
Desc_Yuno_Cap3: Activates real-time local rails on both send and receive sides: Open Banking and FPS for UK senders, BLIK for Poland, Pix Instant for Brazil payouts, SPEI for Mexico, UPI for India, Nequi for Colombia, Mercado Pago across LatAm. One API, 1,000+ payment methods, accelerating corridor speed without per-partner builds.
Desc_Yuno_Cap4: One dashboard unifying card funding, ACH/SEPA deposits, Bridge stablecoin payouts, Circle USDC treasury, mobile money networks, and 170+ country bank disbursements into a single reconciliation layer. Real-time corridor monitoring, centralized compliance reporting, NOVA fraud engine with 75% fewer false positives across all rails.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Remitly at a glance:**
- Founded: 2011 by Matt Oppenheimer, Josh Hug, and Shivaas Gulati in Seattle, WA
- Public: RELY on Nasdaq (IPO September 2021)
- Revenue: $1.6B FY2025 (+29% YoY); Q4 2025: $442.2M (+26% YoY)
- Send Volume: $74.9B FY2025 (+37% YoY); Q4: $20.8B (+35%)
- Active Customers: 9.3M (+19% YoY)
- Adjusted EBITDA: $267M FY2025; Q4: $88.6M (+98% YoY)
- First full year of GAAP profitability in 2025
- Countries: 170+, corridors: 5,100+
- Network: 4.2B bank accounts, 1.2B mobile wallets, 460K+ cash pickup locations
- Employees: ~2,800

**2026 Guidance:**
- Q1 revenue: $436M to $438M (+21% YoY)
- Full year: 19 to 20% revenue growth ($1.9B to $1.96B)
- Adjusted EBITDA: Higher YoY with normalized fraud loss rate of 9 to 13 bps

**Medium-term outlook (2028):**
- Revenue: $2.6B to $3.0B
- Adjusted EBITDA: $575M to $600M (20 to 22% margin)

**Key products:**
- Remitly Core: Cross-border remittance platform (consumer)
- Remitly Business: International business payments from U.S.
- Passbook (ex-Rewire): Digital banking for immigrants (acquired 2023 for $80M)
- Stablecoin payouts: USDC payouts to Argentina and Nigeria via Bridge/Stripe
- USDC treasury: Internal stablecoin treasury operations with Circle
- ChatGPT integration: Rate checking and corridor comparison (launched April 2026)

**Confirmed PSPs / Payment Rails:**
- Bridge (Stripe company): Stablecoin payout rails, blockchain-based disbursement
- Circle: USDC stablecoin partner for treasury and wallet operations
- ACH: Bank account funding (U.S. only)
- SEPA: Bank transfer funding (European senders)
- Visa / Mastercard: Card-based funding across all send markets
- Apple Pay / Google Pay: Mobile wallet funding
- Bancontact: EU card funding (Belgium)
- iDEAL: EU bank transfer funding (Netherlands)
- Klarna/Sofort: EU bank transfer funding
- Local payout banks: 170+ country banking network
- Mobile money: M-Pesa (Kenya, Tanzania), GCash (Philippines), Maya (Philippines), bKash (Bangladesh), MTN Mobile Money (Africa), Airtel Money (Africa), eSewa (Nepal), JazzCash (Pakistan)
- No payment orchestrator detected
- No multi-partner routing/failover identified

**Stablecoin strategy:**
- September 2025: Launched stablecoin payout rails via Bridge (Stripe company)
- Live corridors: U.S. to Argentina, U.S. to Nigeria
- USDC integrated into internal treasury operations for 24/7 value movement
- Goal: Reduce settlement delays and intermediary fees by up to 50% in high-volume corridors
- Multi-rail vision: Combining traditional banking, mobile money, and stablecoin rails

**Rewire/Passbook integration:**
- Acquired January 2023 for $80M (cash + stock)
- Israeli fintech for migrant worker financial services
- 2026: Cut 110 Israel staff, closed R&D hub, retained only sales/business roles
- Focus shifted back to core remittance business and expanded financial services

**Key Meeting Angles:**
1. **$74.9B send volume, fragmented payout stack** | 170+ country network with no orchestration layer across disbursement partners
2. **Prefunding capital exposure** | Working capital tied up in payout partner balances creates FX risk and scaling constraints
3. **Corridor speed inconsistency** | Real-time rails (Pix, SPEI, UPI) not activated across all corridors despite "guaranteed delivery" brand promise
4. **Send-side APM gaps** | Open Banking, FPS, and BLIK missing for European senders limits funding conversion
5. **Bridge/Stripe dependency** | Stablecoin payouts only in 2 corridors (Argentina, Nigeria); Yuno could extend to all LatAm via local rails
6. **$67M to $97M annual fraud loss** | Unified fraud orchestration across card, ACH, SEPA, wallet, and stablecoin rails could significantly reduce loss rate
7. **ChatGPT integration signals AI-first strategy** | Payment orchestration with ML-powered routing aligns with Remitly's AI investment thesis
8. **2028 target: $3B revenue** | Scaling from $1.6B to $3B requires infrastructure that reduces per-transaction cost at every step

**Sources:**
- [Remitly Q4 & FY2025 Results (Investor Relations)](https://ir.remitly.com/news-releases/news-release-details/remitly-reports-fourth-quarter-and-full-year-2025-results-above)
- [Remitly 2026 Revenue Guidance (Seeking Alpha)](https://seekingalpha.com/news/4553792-remitly-outlines-2026-revenue-guidance-of-up-to-1_96b-as-new-products-and-ai-boost-expansion)
- [Remitly Medium-Term Outlook (Investor Relations)](https://ir.remitly.com/news-releases/news-release-details/remitly-unveils-medium-term-outlook-setting-course-durable)
- [Remitly Stablecoin Payouts (Remitly Newsroom)](https://news.remitly.com/innovation/remitly-harnesses-stablecoins/)
- [Remitly USDC Payout How-To (Remitly Blog)](https://www.remitly.com/blog/money-transfer/how-to-send-stablecoin-payouts-with-remitly/)
- [Remitly Multi-Rail Highway (Tearsheet)](https://tearsheet.co/payments/remitlys-next-act-building-a-multi-rail-highway-for-global-money/)
- [Remitly Infrastructure Scaling (AInvest)](https://www.ainvest.com/news/remitly-infrastructure-bet-scaling-global-cross-border-payments-platform-proven-tech-leader-board-2604/)
- [Remitly Rewire Acquisition (Investor Relations)](https://ir.remitly.com/news-releases/news-release-details/remitly-acquire-rewire-expand-complementary-geographies-account)
- [Remitly Israel Office Cuts (Calcalist)](https://www.calcalistech.com/ctechnews/article/bkxy2fwv11g)
- [Remitly Fraud ML (Remitly Newsroom)](https://news.remitly.com/company-and-product-news/how-remitly-is-tackling-fraud-and-reducing-interventions-with-machine-learning/)
- [Remitly Q4 2025 Earnings Summary (Yahoo Finance)](https://finance.yahoo.com/news/remitly-global-inc-q4-2025-133000407.html)
- [Remitly ChatGPT Integration (GlobeNewsWire)](https://www.globenewswire.com/news-release/2026/04/16/3275684/0/en/Remitly-App-Launches-in-ChatGPT.html)
- [Remitly Business Model Canvas (DCF Modeling)](https://www.dcfmodeling.com/products/rely-business-model-canvas)
- [Remitly Send from U.S. (Remitly)](https://www.remitly.com/us/en)
- [Remitly UK Guide (Remitly)](https://www.remitly.com/gb/en/landing/clear-guide-to-using-remitly)
- [Stablecoin Remittances Explained (Stripe)](https://stripe.com/resources/more/stablecoin-remittances-explained)
- [Remitly Logo (CompaniesLogo)](https://companieslogo.com/remitly/logo/)
