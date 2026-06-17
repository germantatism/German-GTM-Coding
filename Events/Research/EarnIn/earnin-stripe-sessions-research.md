# EARNIN | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: EarnIn
=======================================

Logo: https://asset.brandfetch.io/idBqm7m3Qx/idGjX5XDz7.svg
Nombre merchant: EarnIn

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Single PSP Bottleneck
Tittle_Pain Point_2: Instant Transfer Costs
Tittle_Pain Point_3: US-Only Payment Rails
Tittle_Pain Point_4: Repayment Failure Risk
Tittle_Pain Point_5: Regulatory Fee Pressure

Desc_Pain Point_1: EarnIn relies on TabaPay as its primary instant disbursement rail and Evolve Bank & Trust as its banking-as-a-service partner. No acquirer redundancy means a single outage or partner disruption freezes Cash Out, Early Pay, and Balance Shield for 1.3M+ active users.
Desc_Pain Point_2: Lightning Speed transfers cost users $2.99 to $5.99 per transaction, generating significant revenue but creating churn pressure. High per-transaction fees to TabaPay and card networks for push-to-card compress margins on the 57% of users who tip voluntarily.
Desc_Pain Point_3: All disbursements and repayments limited to US ACH and Visa/Mastercard debit rails. No support for real-time payment networks (RTP, FedNow) at scale, no international rails for planned UK/Canada/Australia expansion. 19M+ app downloads but zero non-US monetization.
Desc_Pain Point_4: Automatic paycheck deductions depend on employer direct deposit timing. When users switch banks, change employers, or experience payroll delays, repayment fails. No multi-rail retry or alternative collection path exists beyond the single linked checking account.
Desc_Pain Point_5: CFPB scrutiny and six federal court rulings classifying EWA as loans threaten the tip-based model. If tips are reclassified as interest, Lightning Speed fees face APR disclosure requirements. Payment infrastructure must support compliant fee structures across evolving state regulations.

SLIDE 1: PSP TOPOLOGY

PSP_1: TabaPay (instant push-to-card disbursements)
PSP_2: Evolve Bank & Trust (BaaS, EarnIn Card issuer)
PSP_3: Plaid (bank account linking and verification)
PSP_4: Visa Direct / Mastercard Send (card rails)
PSP_5: Cross River Bank (credit facility provider)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: RTP (Real-Time Payments)
Local_M_2: FedNow
Local_M_3: Open Banking (UK)
Local_M_4: Faster Payments (UK)
Local_M_5: BACS Direct Debit (UK)
Local_M_6: Interac e-Transfer (Canada)
Local_M_7: NPP/PayID (Australia)
Local_M_8: SEPA Instant (EU)
Local_M_9: Apple Pay disbursements
Local_M_10: PayPal/Venmo payouts

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each Cash Out disbursement and repayment collection to the optimal rail by user bank, card BIN, and transfer type. With 1.3M+ active users generating millions of monthly transactions, even a 3% improvement in successful first-attempt transfers saves hundreds of thousands in retry costs and reduces user friction that drives churn.
Desc_Yuno_Cap2: Automatic cascade across TabaPay, Visa Direct, Mastercard Send, and ACH when the primary disbursement rail fails. When a push-to-card attempt declines, Yuno reroutes to the next best rail in milliseconds. Up to 50% recovery on failed disbursements across 1.3M+ active Cash Out users.
Desc_Yuno_Cap3: Unlocks the payment rails EarnIn needs for international expansion: Faster Payments and Open Banking in the UK, Interac in Canada, NPP/PayID in Australia. Domestically, activates RTP and FedNow for true real-time transfers without card network fees. One API, 1,000+ payment methods.
Desc_Yuno_Cap4: One dashboard consolidating TabaPay disbursements, Evolve Bank operations, Plaid verifications, and ACH repayments into a unified view. Real-time success rate monitoring across all rails, centralized reconciliation for CFPB compliance, millisecond anomaly detection. Full visibility as EarnIn scales toward $150M+ in annual disbursement volume.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**EarnIn at a glance:**
- Earned wage access (EWA) and financial wellness platform, founded 2013 as Activehours
- HQ: Palo Alto, California. ~585 employees across 5 continents
- Revenue: $93.6M (2025)
- Total funding: $190.1M (equity). Additional $225M in credit facilities (Cross River $150M, MUFG $75M)
- Valuation: ~$527M (estimated, based on 2020 round)
- 19M+ app downloads, 3.8M+ total users, 1.3M active Cash Out users
- $15B+ in earnings accessed to date. $1B+ in overdraft fees avoided for users
- CEO/Founder: Ram Palaniappan
- Products: Cash Out ($750/pay period), Early Pay, Balance Shield, Tip Yourself, Credit Monitoring
- EarnIn Card issued by Evolve Bank & Trust via Visa license
- Rebranded from Earnin to EarnIn in January 2023

**Confirmed PSPs and Infrastructure:**
- TabaPay: primary instant disbursement processor (push-to-card via Visa Direct and Mastercard Send)
- Evolve Bank & Trust: banking-as-a-service partner, EarnIn Card issuer, deposit account provider
- Lead Bank: secondary banking partner (member FDIC)
- Plaid: bank account linking, income verification, transaction data
- Cross River Bank: $150M revolving credit facility (September 2025)
- MUFG: $75M revolving credit facility for real-time pay products
- Visa Direct / Mastercard Send: card-level instant transfer rails
- ACH: standard free transfers (1-2 business days)
- No payment orchestrator detected
- No multi-acquirer routing identified

**Accepted payment methods / transfer rails:**
- Push-to-card: Visa debit, Mastercard debit (via Lightning Speed, $2.99-$5.99)
- ACH bank transfer: free, 1-2 business day delivery
- EarnIn Card: Visa-branded debit card via Evolve Bank
- Repayment: automatic ACH deduction from linked checking account on payday
- No support for: prepaid accounts, savings accounts, Venmo, Cash App accounts
- US-only operations (no international payment rails)

**Revenue Model:**
- Lightning Speed instant transfer fees: $2.99-$5.99 per transaction
- Voluntary tips: users choose $0-$14 per Cash Out (57% tip, 43% do not)
- Average tip is less than $4.68 (average out-of-network ATM fee)
- Zero fees charged to employers
- Early Pay expedited deposit: $2.99 fee
- Balance Shield auto-transfer: $3.99 expedited fee

**Top Market Gap Analysis:**

MARKET 1: United States (sole market, 100% of revenue)
  Current rails: Visa Direct, Mastercard Send (push-to-card), ACH
  Missing: RTP (The Clearing House), FedNow, Zelle integration
  Note: Domestic-only but missing real-time bank rails that eliminate card network fees

MARKET 2: United Kingdom (planned expansion)
  Current rails: None
  Missing: Faster Payments, Open Banking, BACS Direct Debit, GBP disbursements
  Note: UK EWA market growing rapidly. Wagestream, Hastee already established

MARKET 3: Canada (planned expansion)
  Current rails: None
  Missing: Interac e-Transfer, EFT, CAD disbursements
  Note: Similar legal framework. Payfare, Dayforce already offer EWA

MARKET 4: Australia (planned expansion)
  Current rails: None
  Missing: NPP/PayID, BPAY, AUD disbursements
  Note: High smartphone penetration, strong digital banking, EWA demand growing

MARKET 5: Europe (future opportunity)
  Current rails: None
  Missing: SEPA Instant, iDEAL, Swish, EUR disbursements
  Note: PSD2/Open Banking creates regulatory tailwinds for EWA models

**Key meeting angles:**
1. **Single-rail dependency** | TabaPay is the sole instant disbursement processor. Any disruption freezes 1.3M active users with no fallback
2. **International expansion blocked** | UK, Canada, Australia identified as targets but zero non-US payment infrastructure exists today
3. **Margin compression on instant transfers** | Card network fees on push-to-card eat into Lightning Speed revenue. Real-time bank rails (RTP, FedNow) would reduce per-transaction cost
4. **Regulatory compliance complexity** | CFPB and six federal courts scrutinizing tip model. Payment infrastructure must adapt to potential reclassification of tips as interest
5. **Repayment failure loop** | Single-bank ACH deduction with no retry path. Multi-rail collection would recover failed repayments and reduce write-offs
6. **Competitive pressure** | Dave, Chime, DailyPay, Payactiv all scaling EWA with multi-rail infrastructure. EarnIn's single-processor setup is a competitive disadvantage

**Sources:**
- [Contrary Research: EarnIn Business Breakdown](https://research.contrary.com/company/earnin)
- [EarnIn Wikipedia](https://en.wikipedia.org/wiki/Earnin)
- [EarnIn About Page](https://www.earnin.com/about)
- [Cross River $150M Credit Facility](https://www.businesswire.com/news/home/20250910488023/en/Cross-River-Provides-$150-Million-Credit-Facility-to-EarnIn-to-Expand-Access-to-On-Demand-Pay)
- [MUFG $75M Financing](https://www.stocktitan.net/news/MUFG/mufg-announces-75-million-financing-for-earn-f44zawgmp8tj.html)
- [GetLatka: EarnIn Revenue](https://getlatka.com/companies/earnin.com)
- [TabaPay Customers](https://www.cbinsights.com/company/tabapay/customers)
- [EarnIn Help Center: Lightning Speed](https://help.earnin.com/hc/en-us/articles/224458568-What-is-Lightning-Speed-and-how-can-I-get-it)
- [EarnIn Help Center: How the App Works](https://help.earnin.com/hc/en-us/articles/213412087-How-does-the-app-work)
- [CFPB EWA Advisory Opinion](https://www.consumerfinanceinsights.com/2026/01/12/cfpb-brings-clarity-to-earned-wage-access-products/)
- [Tracxn: EarnIn Profile](https://tracxn.com/d/companies/earnin/__S4AJErWK9TY0GeDRKxCitHQ9xtyGbLoqYBytsoU9kt0)
- [EarnIn Brandfetch Logo](https://brandfetch.com/earnin.com)
