# GUSTO | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Gusto
═══════════════════════════════════════

Logo: https://upload.wikimedia.org/wikipedia/commons/5/5a/Gusto%2C_Inc._logo.svg
Nombre merchant: Gusto

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Cross-Border Payout Lag
Tittle_Pain Point_2: ACH Single-Rail Risk
Tittle_Pain Point_3: Fraud at Scale
Tittle_Pain Point_4: Embedded Partner Churn
Tittle_Pain Point_5: 120-Country Coverage Gaps

Desc_Pain Point_1: International payouts take 2-5 days via legacy wires. Wise/stablecoin same-day covers select corridors; many of 120+ countries still on slow $15+ wires.
Desc_Pain Point_2: US payroll runs on a single ACH path with no failover. A rejected debit triggers $100/day penalties, blocks the payroll run, and freezes accounts.
Desc_Pain Point_3: 400K+ SMBs process payroll, benefits, and Bill Pay on one platform. SymphonyAI partnership confirms fraud/AML risk requires enterprise-grade AI detection.
Desc_Pain Point_4: Gusto Embedded powers payroll for U.S. Bank (1.4M SMB clients) and vertical SaaS. Any payment failure reflects on the partner brand, amplifying churn.
Desc_Pain Point_5: 120+ countries served but most corridors lack local instant rails. Contractors forced onto USD wires with FX markup while Deel offers native local payouts.

SLIDE 1: PSP TOPOLOGY

PSP_1: Internal ACH Processing
PSP_2: Plaid (bank account verification)
PSP_3: Wise (international payouts)
PSP_4: Zerohash (stablecoin rails)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: UPI
Local_M_3: SPEI
Local_M_4: BLIK
Local_M_5: M-Pesa
Local_M_6: GCash
Local_M_7: Interac
Local_M_8: iDEAL
Local_M_9: SEPA Instant
Local_M_10: PromptPay

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing by corridor, amount, and payout type. With $500M+ revenue and 400K+ SMBs across 120+ countries, routing each disbursement to the best rail per market delivers 3-10% cost reduction and faster settlement.
Desc_Yuno_Cap2: Automatic cascade when ACH debits fail or wires bounce. Instead of blocking payroll and charging $100/day, Yuno retries through the next best processor in milliseconds. Up to 50% recovery on failed transactions prevents payroll disruption.
Desc_Yuno_Cap3: Activates instant local payout rails: Pix in Brazil, UPI in India, SPEI in Mexico, M-Pesa in Kenya, GCash in Philippines, iDEAL in Netherlands, Interac in Canada. One API, 1,000+ methods. Same-day settlement without stablecoin complexity.
Desc_Yuno_Cap4: One dashboard unifying ACH, Wise, Zerohash stablecoins, and wire transfers. Real-time disbursement monitoring per corridor, centralized reconciliation across Embedded partners, and NOVA fraud detection (75% reduction) protecting 400K+ accounts.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Gusto at a glance:**
- Founded: 2011 (as ZenPayroll). HQ: San Francisco, CA
- Valuation: $9.3B (June 2025 tender offer led by Ontario Teachers' Pension Plan)
- Revenue: $500M+ annually (2023 figure, likely higher post-growth)
- Employees: ~4,369 (March 2026)
- Customers: 400K+ direct SMB clients, 700K+ via embedded partners
- Key products: Payroll, Benefits, HR, Gusto Money (Bill Pay, Payroll Bridge credit, Invoicing), Gusto Wallet (debit card, early pay, savings), Gusto Embedded (white-label payroll API), Global Contractor Payments (120+ countries)
- Growth: 401(k) services grew 50% YoY in 2024; Gusto Money expanded 140% YoY
- Recent acquisitions: Mosey (April 2026, compliance automation), Guideline (August 2025, retirement plans)
- U.S. Bank partnership (Sept 2025): Gusto Embedded powers payroll for U.S. Bank's 1.4M small business clients

**Confirmed Payment Stack:**
- Internal ACH processing: Primary rail for US payroll (next-day, 2-day, and 4-day speeds)
- Plaid: Bank account verification and linking (processor token integration)
- Wise: International contractor payouts (same-day via Wise multi-currency account, launched March 2026)
- Zerohash: Stablecoin (USDC) payouts for global contractors (launched January 2026)
- Wire transfers: Fallback for international payouts and high-value US payroll ($100K+ tax liability)
- Paper checks: Legacy option for employers without direct deposit
- Clair: On-demand pay (earned wage access) via Gusto Wallet
- SymphonyAI: Financial crime detection (fraud, AML, sanctions monitoring)
- Melio: Bill Pay integration (launched May 2025)
- Parafin: Payroll Bridge credit product (launched September 2025)
- No third-party payment orchestrator detected

**Key Competitive Landscape:**
- Deel: Strongest in global EOR and international contractor payments (150+ countries)
- Rippling: Dominant mid-market with unified HR/IT/Finance stack and global payroll
- Check (formerly Checkhq): API-first payroll infrastructure competitor for embedded
- ADP/Paychex: Legacy incumbents in US payroll
- Gusto differentiator: #1 SMB focus (88% of G2 reviewers are SMBs) + embedded distribution

**Top 5 Pain Point Evidence:**

1. CROSS-BORDER PAYOUT LAG
   - Traditional international payments take 3-7 days to settle
   - Wire transfer fees: $15 minimum for payments under $1,000, 1-1.5% for larger
   - Gusto's own announcement admits "creating cash flow challenges for contractors and administrative friction for employers"
   - Same-day options (Wise, USDC) only cover select corridors; many countries still on slow rails

2. ACH SINGLE-RAIL RISK
   - Failed ACH debit = $100/day penalty per failed transaction
   - Payroll blocked until recovery case resolved manually
   - "If funds are swept after the debit date, processing will be blocked until the re-debit clears"
   - Faster payroll speeds (next-day, 2-day) suspended after failures
   - Bank compatibility issues documented with certain institutions rejecting Gusto ACH IDs

3. FRAUD AT SCALE
   - SymphonyAI partnership (Nov 2025) to protect 400K+ clients
   - "Massive transaction volumes" across payroll, benefits, Bill Pay, and invoicing
   - Gusto moving billions in payroll annually for SMBs that lack in-house fraud teams
   - Platform processes employer tax deposits, benefits premiums, and vendor payments

4. EMBEDDED PARTNER RISK
   - Gusto Embedded serves banks and vertical SaaS as white-label payroll
   - U.S. Bank launch (Sept 2025) exposes 1.4M SMB clients to Gusto's payment rails
   - Any payment failure reflects on the partner brand, not just Gusto
   - Embedded fintech transactions projected to exceed $7T by end of 2026

5. 120-COUNTRY COVERAGE GAPS
   - Gusto serves 120+ countries but lacks local instant payout rails in most
   - Competitors like Deel offer native local currency payouts with broader method coverage
   - Many corridors force contractors onto USD wires with FX markup
   - 11% of U.S. small businesses employed international contractors in 2025; 75% plan to grow global headcount

**Key meeting angles:**
1. **$9.3B fintech processing payroll for 400K+ SMBs** | Scale demands resilient, multi-rail payment infrastructure
2. **Embedded distribution amplifies risk** | Payment failures on Gusto rails damage U.S. Bank and vertical SaaS partner brands
3. **ACH single point of failure** | $100/day penalties and blocked payrolls when debits fail, with no automatic failover
4. **Global expansion bottleneck** | 120+ countries but most still on slow, expensive wire rails
5. **Gusto Money creates new payment flows** | Bill Pay, Invoicing, Payroll Bridge credit all need robust payment orchestration
6. **Fraud protection gap** | SymphonyAI partnership proves fraud risk is critical; Yuno's NOVA adds another layer
7. **Competitor pressure** | Deel and Rippling offer more complete global payment infrastructure natively

**Sources:**
- [Gusto: Global Contractor Payments](https://gusto.com/product/global/gcp)
- [Gusto: Same-Day International Payments](https://gusto.com/resources/company-news/same-day-international-contractor-payments)
- [Gusto Help: Payment Methods for Employees](https://support.gusto.com/article/999903851000000)
- [Gusto Help: International Contractors](https://support.gusto.com/article/106622337100000)
- [Gusto Help: Wire Transfers](https://support.gusto.com/article/120456825100000)
- [Gusto Help: Fix Payroll Blockers](https://support.gusto.com/article/106621966100000)
- [Gusto Embedded Payroll API](https://embedded.gusto.com/product/payroll-api)
- [Gusto Docs: Bank Errors](https://docs.gusto.com/embedded-payroll/docs/bank-errors)
- [Gusto Docs: Recovery Cases](https://docs.gusto.com/embedded-payroll/docs/recovery-cases-1)
- [Gusto Docs: Payroll Processing Speeds](https://docs.gusto.com/embedded-payroll/docs/2-day-vs-4-day)
- [Plaid Docs: Gusto Auth Partnership](https://plaid.com/docs/auth/partnerships/gusto/)
- [Sacra: Gusto Revenue & Valuation](https://sacra.com/c/gusto/)
- [Finovate: Gusto Stablecoin Payouts](https://finovate.com/gusto-unveils-global-stablecoin-payout-capabilities/)
- [CoinDesk: Gusto Zerohash Partnership](https://www.coindesk.com/business/2026/01/16/hr-services-provider-gusto-taps-zerohash-to-speed-up-global-payouts-with-stablecoins/)
- [SymphonyAI: Gusto Financial Crime Partnership](https://www.symphonyai.com/news/financial-services/gusto-ai-financial-protection/)
- [Embedded Finance Review: Gusto Money Launch](https://www.embeddedfinancereview.com/gusto-launches-gusto-money-payroll-provider-expands-into-embedded-finance-with-credit-bill-pay-and-i/)
- [Fondo: Gusto vs Rippling vs Deel](https://fondo.com/blog/gusto-vs-rippling-vs-deel)
- [Sacra: Gusto vs Rippling vs Deel vs Check](https://sacra.com/p/gusto-vs-rippling-vs-deel-vs-check/)
