# UPGRADE | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Upgrade
═══════════════════════════════════════

Logo: https://logotyp.us/file/upgrade.svg
Nombre merchant: Upgrade

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Single-Bank Dependency
Tittle_Pain Point_2: Disbursement Speed Gap
Tittle_Pain Point_3: BNPL Fraud Exposure
Tittle_Pain Point_4: Cross-Border Ceiling
Tittle_Pain Point_5: Card Payment Leakage

Desc_Pain Point_1: Cross River powers cards, ACH, deposits, and lending. One bank across $42B+ in credit creates concentration risk with no failover if systems fail.
Desc_Pain Point_2: Loan disbursements use batch ACH (2 to 3 day settlement). SoFi offers same-day funding. Without real-time rails, Upgrade loses borrowers needing instant funds.
Desc_Pain Point_3: Flex Pay handles $1K to $10K+ travel BNPL across 750+ merchants. Fraud exposure scales with ticket size, and no multi-layer fraud orchestration exists.
Desc_Pain Point_4: Flex Pay only operates in U.S. and Canada. Global airlines and cruise partners serve worldwide travelers, but LatAm, Europe, and Asia have zero BNPL access.
Desc_Pain Point_5: Upgrade Card and OneCard route through one Visa path via Cross River. No multi-acquirer routing means every soft decline is a lost transaction with no retry.

SLIDE 1: PSP TOPOLOGY

PSP_1: Cross River Bank (issuer + processor)
PSP_2: Visa Network (card rails)
PSP_3: ACH / Nacha (disbursements)
PSP_4: Sutton Bank (co-issuer)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix (Brazil)
Local_M_2: SPEI (Mexico)
Local_M_3: OXXO (Mexico)
Local_M_4: PSE (Colombia)
Local_M_5: Nequi (Colombia)
Local_M_6: iDEAL (Netherlands)
Local_M_7: Bancontact (Belgium)
Local_M_8: BLIK (Poland)
Local_M_9: Mercado Pago (LatAm)
Local_M_10: UPI (India)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each Flex Pay BNPL transaction and card payment to the optimal processor by merchant category, value, and geography. With $42B+ originated and 750+ merchants, a 3% auth uplift recovers millions in approved volume annually.
Desc_Yuno_Cap2: Automatic cascade eliminates single-bank dependency. When Cross River declines a card transaction or disbursement fails, Yuno reroutes instantly to the next best path. Up to 50% recovery on failed transactions, protecting Flex Pay conversion.
Desc_Yuno_Cap3: Unlocks Flex Pay BNPL globally: Pix in Brazil, SPEI and OXXO in Mexico, PSE and Nequi in Colombia, iDEAL in Netherlands, BLIK in Poland. One API, 1,000+ payment methods. 750+ travel partners gain global checkout without per-market builds.
Desc_Yuno_Cap4: One dashboard consolidating Cross River cards, ACH disbursements, Flex Pay BNPL, and Upgrade Card payments. Real-time approval monitoring, centralized reconciliation across all products, NOVA intelligence for 75% faster anomaly detection.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Upgrade at a glance:**
- Founded: 2016 in San Francisco by Renaud Laplanche (former LendingClub CEO)
- Valuation: $7.3B (Series G, October 2025). Total equity raised: $750M
- Revenue: $1B+ annualized run rate (reached May 2025), cash flow positive for 3+ years
- Customers: 7.5M+ served, $42B+ in credit originated since inception
- Employees: ~1,950 across San Francisco, Phoenix, Montreal, Atlanta, Irvine
- IPO timeline: CEO stated "12 to 18 months away" as of October 2025
- Fastest-growing U.S. credit card within two years of launch

**Product suite:**
- Personal Loans: $1K to $50K, 24 to 84 month terms, 7.99% to 35.99% APR
- Upgrade Card / OneCard: Hybrid credit card with "Pay Now" and "Pay Later" modes (launched 2019/2022)
- Flex Pay (formerly Uplift): Travel BNPL with 750+ merchant partners, 3 to 24 month terms. Acquired for $100M in July 2023, rebranded December 2024. Revenue doubled post-acquisition
- Auto Loans: Surpassed $1B in originations by mid-2025
- Home Improvement Financing: Surpassed $1B in originations by December 2024
- Personal Credit Line: Up to $50K, no collateral required
- Rewards Checking Plus: Up to 2% cash back, high-yield savings
- Boost Money: High-yield savings + secured credit cards

**Confirmed PSPs and Banking Partners:**
- Cross River Bank: primary banking partner since 2019. Powers card issuance, payment APIs, ACH infrastructure, deposit accounts, and loan origination. Partnership has facilitated $32B+ in consumer loans
- Sutton Bank: co-issuer for card programs (also serves Cash App, Robinhood, Brex)
- WebBank: additional lending partner for loan origination
- Visa Network: card transaction rails for Upgrade Card and OneCard
- ACH / Nacha: primary disbursement rail for loan funding
- No payment orchestrator detected
- No multi-acquirer or smart routing capability identified

**Key Flex Pay merchant partners:**
- Expedia Group (cruise bookings, March 2025 partnership)
- JetBlue Vacations (flight + hotel packages)
- 750+ travel and retail brands across airlines, hotels, resorts, cruise lines, rental cars
- U.S. and Canada only (no international markets announced)

**Top Pain Points Detail:**

1. **Single-bank concentration**: Cross River powers 4 of Upgrade's 6 product lines. Card issuance, payment APIs, ACH, deposits, and lending all flow through one bank. Cross River also recently expanded a revolving credit facility to $250M for Upgrade. This deep dependency creates systemic risk.

2. **Disbursement speed disadvantage**: Upgrade loan disbursements use batch ACH (2 to 3 day settlement). SoFi and other competitors offer same-day or next-day funding. Real-time payment rails (RTP, FedNow) could solve this but require orchestration infrastructure.

3. **Flex Pay international ceiling**: Global airlines and cruise lines serve travelers worldwide, but Flex Pay only operates in U.S. and Canada. A Brazilian traveler booking a cruise on Expedia cannot use Flex Pay. Local APMs in Latin America, Europe, and Asia would unlock massive incremental volume.

4. **Fraud at scale**: Flex Pay handles high-value travel transactions ($1K to $10K+). Friendly fraud and chargeback rates in travel BNPL are above average. Without multi-layer fraud orchestration, each dispute is costly and manual.

5. **Card routing limitations**: Upgrade Card transactions flow through a single Visa path via Cross River. No ability to retry declines through alternate acquirers. Soft declines on recurring card payments directly cause involuntary churn.

**Key meeting angles:**
1. **$7.3B pre-IPO fintech** | Payment infrastructure modernization is critical before public market scrutiny
2. **$42B+ originated, single bank** | Concentration risk at scale is an underwriter concern
3. **Flex Pay international unlock** | 750+ travel merchant partners serve global travelers, but checkout is U.S./Canada only
4. **Disbursement speed** | Real-time payments would differentiate against SoFi and LendingClub
5. **Card auth optimization** | Smart routing across multiple acquirers recovers failed Upgrade Card transactions
6. **Fraud orchestration** | High-value BNPL travel transactions need multi-layer fraud prevention
7. **IPO readiness** | Diversified payment infrastructure signals operational maturity to investors
8. **Competitor precedent** | SoFi (multi-bank), Klarna (multi-PSP), Affirm (global BNPL expansion)

**Sources:**
- [Upgrade Official Website](https://www.upgrade.com/)
- [Upgrade Wikipedia](https://en.wikipedia.org/wiki/Upgrade,_Inc.)
- [Cross River Bank x Upgrade Case Study](https://www.crossriver.com/case-study/upgrade)
- [CNBC: Upgrade Valued at $7.3B](https://www.cnbc.com/2025/10/16/fintech-startup-upgrade-valued-at-7point3-billion-in-new-funding-round.html)
- [Finovate: Upgrade Raises $165M](https://finovate.com/upgrade-raises-165-million-sees-valuation-rise-to-7-3-billion/)
- [Fintech Futures: Upgrade Series G](https://www.fintechfutures.com/venture-capital-funding/upgrade-raises-165m-series-g-at-reported-7-3bn-valuation/)
- [Upgrade: Acquires Uplift for $100M](https://www.upgrade.com/press/releases/upgrade-acquires-uplift-for-100-million-in-cash-and-stock/)
- [Upgrade: Uplift Rebrands to Flex Pay](https://www.upgrade.com/press/releases/uplift-rebrands-to-flex-pay-reflecting-growth-and-expanded-opportunities/)
- [Upgrade: Personal Credit Line Launch](https://www.upgrade.com/press/releases/upgrade-introduces-personal-credit-line/)
- [Skift: Upgrade $165M Fundraise, BNPL Pressure](https://skift.com/2025/10/23/upgrades-165-million-fundraise-comes-as-buy-now-pay-later-sector-faces-pressure/)
- [Expedia x Flex Pay Cruise Partnership](https://www.upgrade.com/press/memos/expedia-group-to-introduce-flex-pay-for-cruise-bookings/)
- [JetBlue x Flex Pay Partnership](https://www.fintechlaunches.com/announcements/jetblue-vacations-flex-pay-monthly-payment-option-travel-financing-flight-hotel-packages/)
- [Banking Dive: Upgrade Acquires Uplift](https://www.bankingdive.com/news/upgrade-acquires-bnpl-uplift-fintech-renaud-laplanche/689173/)
- [American Banker: Renaud Laplanche Profile](https://www.americanbanker.com/news/renaud-laplanches-journey-from-scandal-to-second-act)
- [The Financial Brand: Upgrade Expands Product Lineup](https://thefinancialbrand.com/news/fintech-banking/upgrade-interview-165619)
- [Upgrade Logo (Logotyp.us)](https://logotyp.us/logo/upgrade/)
