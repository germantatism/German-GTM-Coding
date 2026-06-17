# PARAFIN | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Parafin
=======================================

Logo: https://asset.brandfetch.io/id2qn_KQNF/idRJfMFP3_.svg
Nombre merchant: Parafin

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Single Acquirer Dependency
Tittle_Pain Point_2: US-Only Disbursement Rails
Tittle_Pain Point_3: No Local Payout Methods
Tittle_Pain Point_4: ACH Settlement Delays
Tittle_Pain Point_5: Card Program Rigidity

Desc_Pain Point_1: All merchant cash advance repayments and platform settlements flow through a single processor. Any outage or decline disrupts collections across DoorDash, Amazon, Walmart, and dozens of other platform partners simultaneously.
Desc_Pain Point_2: Parafin powers financial services for global platforms like DoorDash and Amazon, yet capital disbursements and repayments are limited to US ACH and wire rails. No infrastructure to serve sellers operating in LATAM, Europe, or APAC.
Desc_Pain Point_3: Merchant repayments rely solely on ACH debit and card-on-file. No Pix for Brazilian sellers, no SEPA DD for European merchants, no UPI for Indian sellers. Limits platform partners from launching capital programs internationally.
Desc_Pain Point_4: ACH-based capital disbursements take 3 to 5 business days to reach merchants. Competing embedded finance providers like Shopify Capital offer same-day funding, creating a disadvantage in partner acquisition.
Desc_Pain Point_5: Spend cards are issued exclusively through Marqeta on Visa rails via Column N.A. No multi-network issuance, no Mastercard fallback, and no local debit scheme support for international expansion of the Spend product.

SLIDE 1: PSP TOPOLOGY

PSP_1: Column N.A. (banking partner)
PSP_2: Marqeta (card issuing)
PSP_3: Modern Treasury (payments/ledger)
PSP_4: Visa (card network)
PSP_5: Celtic Bank (lending partner)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: SEPA Direct Debit
Local_M_3: UPI
Local_M_4: SPEI
Local_M_5: iDEAL
Local_M_6: BLIK
Local_M_7: Boleto
Local_M_8: OXXO
Local_M_9: Bancontact
Local_M_10: PSE (Colombia)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route every merchant repayment and capital disbursement through the optimal rail per country, bank, and amount. With $25B+ in offers extended and $100M+ ARR, even a 3% improvement in collection success recovers millions annually across the entire partner network.
Desc_Yuno_Cap2: When a merchant repayment via ACH fails, Yuno cascades to an alternate debit method or processor in milliseconds. Recovers up to 50% of failed collections, protecting revenue share for Parafin and its platform partners.
Desc_Yuno_Cap3: Unlocks international capital programs for global platform partners: Pix in Brazil, SEPA DD in Europe, UPI in India, SPEI in Mexico. One API, 1,000+ payment methods, enabling Parafin to launch embedded finance in any market without building local rails.
Desc_Yuno_Cap4: Single dashboard consolidating Column N.A., Marqeta, Modern Treasury, and Celtic Bank flows into one view. Real-time monitoring of disbursement success rates, repayment collections, and card program performance. NOVA provides millisecond anomaly detection across all rails.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Parafin at a glance:**
- Founded: 2020 in San Francisco, CA (301 Howard St. Suite 1800)
- Co-Founders: Sahill Poddar (CEO), Vineet Goel, Ralph Furman (CFO)
- Valuation: $750M (Series C, December 2024)
- Total funding raised: $518M+ (equity + debt); $100M Series C from Ribbit Capital, Thrive Capital, GIC, Notable Capital, Redpoint Ventures
- Debt facilities: $93M from Jefferies & Trinity Capital; up to $360M forward-flow from Cross River Bank
- Revenue: $100M+ ARR (surpassed in 2025); one source cites $75M in 2024 revenue
- Employees: ~129 (as of January 2026)
- Products: Capital (MCA, term loans, flex loans), Spend (business cards), Pay Over Time (installments)
- Banking partner: Column N.A. (FDIC-insured); Card issuing: Marqeta on Visa rails; Lending: Celtic Bank
- Payments infrastructure: Modern Treasury (ACH, ledgering)
- Extended $25B+ in offers to hundreds of thousands of small businesses
- Recognition: #15 on 2025 Inc. 5000, #10 on Deloitte Fast 500, 2026 Forbes Fintech 50

**Major Platform Partners:**
- Amazon, Walmart, DoorDash, Worldpay, TikTok
- NMI (1M+ merchants via 4,000 channel partners)
- Fullsteam ($125M+ in capital financing)
- 360 Payments ($100M in originations, 3,000+ advances, 900+ businesses)
- Kajabi (Kajabi Capital for creators)
- accept.blue (Gateway Capital)
- Jobber, Mindbody, Gusto

**Confirmed PSPs/Financial Infrastructure:**
- Column N.A.: Banking-as-a-service partner for deposit accounts and card issuance (FDIC insured)
- Marqeta: Card issuing platform for Spend product (Visa network)
- Modern Treasury: Payment operations, ACH origination, ledgering
- Celtic Bank: Lending/loan issuance partner
- Visa: Card network for Spend cards
- No payment orchestrator detected
- Primarily US market; no evidence of international payment rails

**Key pain points and gaps identified:**
- US-only focus: All products (Capital, Spend, Pay Over Time) operate exclusively in the US despite serving global platforms like Amazon and DoorDash
- ACH dependency: Disbursements and repayments rely on ACH (3 to 5 day settlement), no instant/same-day alternatives at scale
- Single card network: Spend cards only on Visa via Marqeta; no multi-network or local debit scheme support
- No international payment rails: Cannot support non-US sellers on partner platforms despite global footprint of partners
- Competitors like Shopify Capital and Square Loans offer faster disbursement and international coverage

**Top Markets Gap Analysis:**

MARKET 1: United States (100% of current operations)
  Offer: ACH debit/credit, Visa card (Marqeta), wire transfers
  Missing: Real-time payments (RTP/FedNow), Cash App Pay, Venmo disbursement
  All products are US-only; expansion requires new rails

MARKET 2: Brazil (DoorDash, Amazon partner markets)
  Offer: None (not operational)
  Missing: Pix, Boleto, TED transfers
  Brazil is DoorDash's largest international market; Parafin cannot serve Brazilian sellers

MARKET 3: Mexico (Amazon, DoorDash partner markets)
  Offer: None (not operational)
  Missing: SPEI, OXXO, CoDi
  Major gap given platform partners' significant Mexican operations

MARKET 4: Europe (Amazon, Worldpay partner markets)
  Offer: None (not operational)
  Missing: SEPA DD, SEPA Instant, iDEAL, BLIK, Bancontact, Giropay
  Worldpay processes for European merchants but Parafin cannot serve them

MARKET 5: India (Amazon partner market)
  Offer: None (not operational)
  Missing: UPI, NEFT, IMPS, Paytm
  Amazon India has millions of sellers; embedded capital opportunity is massive

**Key meeting angles:**
1. **International expansion enabler**: Parafin's platform partners (Amazon, DoorDash, Worldpay) operate globally but Parafin is US-only. Yuno's 1,000+ APMs unlock international capital programs.
2. **Collection success rates**: ACH failures on repayments directly impact revenue. Smart Routing and Failover recover failed collections.
3. **Speed to market**: Instead of building local rails country-by-country, one Yuno integration enables disbursements and collections across LATAM, Europe, and APAC.
4. **Competitive differentiation**: Shopify Capital and Square Loans are expanding internationally. Parafin needs global payment infrastructure to compete.
5. **Platform retention**: Platforms choose embedded finance providers based on geographic coverage. Broader payment method support helps Parafin win and retain platform partnerships.
6. **Scale economics**: With $25B+ in offers extended and 100M+ ARR, even small improvements in collection/disbursement efficiency create outsized financial impact.

**Sources:**
- [Parafin Official Website](https://www.parafin.com/)
- [Parafin About Page](https://www.parafin.com/about)
- [Parafin 2025 Year in Review](https://www.parafin.com/blog/2025-a-defining-year-for-embedded-financing-and-small-business-growth)
- [Parafin Series C Announcement - BusinessWire](https://www.businesswire.com/news/home/20241217769188/en/Parafin-Raises-%24100M-Series-C-to-Redefine-Small-Business-Financial-Services)
- [Parafin + NMI Partnership - BusinessWire](https://www.businesswire.com/news/home/20251209744522/en/Parafin-and-NMI-Partner-to-Bring-Embedded-Financing-to-Over-One-Million-Merchants)
- [Parafin + Kajabi Partnership - BusinessWire](https://www.businesswire.com/news/home/20251211973141/en/Parafin-Partners-With-Kajabi-to-Launch-Kajabi-Capital-Empowering-Experts-With-Access-to-Flexible-Funding)
- [360 Payments Case Study](https://www.parafin.com/blog/case-study-360-payments-parafin-100-million-embedded-financing-program)
- [Parafin + Fullsteam $125M Milestone](https://www.parafin.com/blog/parafin-and-fullsteam-capital-surpass-125-million-in-capital-financing)
- [Parafin + Cross River Bank $360M](https://www.parafin.com/blog/parafin-secures-up-to-360-million-with-forward-flow-commitment-from-cross-river-bank)
- [Parafin + Modern Treasury](https://www.moderntreasury.com/customers/parafin)
- [Parafin Revenue - Getlatka](https://getlatka.com/companies/parafin.com)
- [Parafin - Fintech Futures](https://www.fintechfutures.com/venture-capital-funding/us-embedded-finance-fintech-parafin-secures-100m-in-series-c-funding-round)
- [Why We Invested in Parafin - Notable Capital](https://www.notablecap.com/blog/why-we-invested-in-parafin)
- [Parafin Pay Over Time Launch - BusinessWire](https://www.businesswire.com/news/home/20250922880810/en/Parafin-Expands-Embedded-Financing-Suite-With-AI-powered-Pay-Over-Time-for-Small-Businesses)
- [Brandfetch: Parafin Logo](https://brandfetch.com/parafin.com)
- [Parafin - Tracxn](https://tracxn.com/d/companies/parafin/__3xBIfIsoFsZ7Vwy2nCzJJOq6183LRPEiy0-ww9LuZAM)
