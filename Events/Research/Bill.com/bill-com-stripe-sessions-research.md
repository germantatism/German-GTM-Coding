# BILL.COM | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Bill.com
═══════════════════════════════════════

Logo: https://companieslogo.com/img/orig/BILL-4e498e91.png
Nombre merchant: Bill.com

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Wire-Only Int'l Rails
Tittle_Pain Point_2: Single-Issuer Card Risk
Tittle_Pain Point_3: Payment Complaint Surge
Tittle_Pain Point_4: Activist Cost Pressure
Tittle_Pain Point_5: Fragmented Channel Rails

Desc_Pain Point_1: 137 countries, 106 currencies, but vendor payments rely on wires and limited Local Transfers. No Pix, UPI, SPEI, or SEPA DD confirmed for outbound AP.
Desc_Pain Point_2: Divvy cards issued by Cross River Bank, processed by Marqeta on Visa. Zero redundancy: any partner disruption halts 498K+ business card programs.
Desc_Pain Point_3: Trustpilot 2.8 to 3.1/5 across 540+ reviews. Complaints: held funds, unauthorized charges, unresponsive support. Service quality dropped post layoffs.
Desc_Pain Point_4: Starboard (8.5%), Elliott (5%+), Barington all push for profitability. Hellman and Friedman buyout talks (Feb 2026) signal payment cost audit ahead.
Desc_Pain Point_5: NetSuite, Acumatica, Paychex partnerships embed BILL AP into new channels. Each amplifies the same limited international payment rails with no optimization.

SLIDE 1: PSP TOPOLOGY

PSP_1: JPMorgan Chase
PSP_2: Cross River Bank
PSP_3: Marqeta
PSP_4: Wise

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: UPI
Local_M_3: SPEI
Local_M_4: SEPA Instant
Local_M_5: M-Pesa
Local_M_6: GCash
Local_M_7: iDEAL
Local_M_8: BLIK
Local_M_9: PromptPay
Local_M_10: PSE

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing by corridor, amount, and vendor location. With $380B+ annual payment volume across 137 countries, routing each disbursement to the lowest cost local rail delivers measurable savings. At BILL's scale, even 1 basis point = $38M/year.
Desc_Yuno_Cap2: Automatic cascade when ACH debits fail or wires bounce. Instead of triggering $100/day penalties and blocking payroll runs, Yuno retries through the next best rail in milliseconds. Up to 50% recovery on failed transactions prevents business disruption.
Desc_Yuno_Cap3: Activates instant local payout rails: Pix in Brazil, UPI in India, SPEI in Mexico, M-Pesa in Kenya, GCash in Philippines, iDEAL in Netherlands, SEPA Instant in Europe. One API, 1,000+ methods. Same-day settlement replacing $14.99 USD wire fees.
Desc_Yuno_Cap4: One dashboard unifying JPMorgan ACH, Cross River/Marqeta cards, Wise international, and wire transfers. Real-time monitoring per corridor, centralized reconciliation across NetSuite/Acumatica/Paychex channels. NOVA fraud detection (75% reduction).
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Bill.com at a glance:**
- Founded: 2006, HQ: San Jose, CA. Public company (NYSE: BILL)
- Revenue: $1.46B (FY2025, +13% YoY). Q2 FY2026: $414.7M (+14% YoY)
- Core revenue: $375M in Q2 2026 (+17% YoY)
- Payment volume: $95B per quarter (~$380B annualized)
- Businesses served: 498,500 (Q2 FY2026, +4% YoY)
- Network members (suppliers): 7.1M+
- Transactions: 35M per quarter (+16% YoY)
- International payments: 137 countries, 106 currencies
- Products: AP Automation, AR Automation, Spend and Expense (Divvy), Invoice2go
- Potential acquisition: Hellman and Friedman buyout talks (Feb 2026, ~$4.2B+ value)
- Activist investors: Starboard Value (8.5%), Elliott (5%+), Barington Capital
- Board reshuffle Oct 2025: 4 new directors after activist pressure
- Employees: ~2,200 to 2,400

**Confirmed Payment Stack:**
- JPMorgan Chase: primary banking partner for ACH/wire (press release confirmed)
- Cross River Bank: FDIC member, card issuer for Divvy (case study confirmed)
- Marqeta: card processor for Divvy/Spend and Expense (press release confirmed)
- Visa: primary card network for Divvy cards
- Wise: international payouts (partnership for select corridors)
- Zerohash: stablecoin (USDC) payouts for global contractors
- Internal ACH processing: primary rail for US payments
- Paper checks: legacy option
- No third-party payment orchestrator detected

**Confirmed Payment Methods:**
- ACH ($0.59 per transaction)
- Check ($1.99 per transaction)
- Virtual Card (free)
- Pay By Card: Visa, MC, Amex, Discover (2.9%)
- International Wire ($14.99 USD, free in local currency)
- Local Transfer (select countries, up to 4 days faster than wire)
- Instant Transfer (1.0 to 1.49%)

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (~85 to 90% of traffic)
  Currently offer: ACH, wire, virtual card, credit/debit cards, checks
  Missing: Real-time payments (RTP), FedNow integration
  Impact: ACH is next-day at best. RTP/FedNow enables instant settlement for time-critical payments.

MARKET 2: International Vendor Payments (137 countries)
  Currently offer: Wire transfer, Local Transfer (limited), USDC stablecoins (via Zerohash)
  Missing: Pix, UPI, SPEI, SEPA DD, M-Pesa, GCash, iDEAL
  Impact: Wire fees $14.99 per USD payment. Local rails deliver same-day at fraction of cost.

MARKET 3: Canada (FMSB licensed)
  Currently offer: Wire transfers
  Missing: Interac e-Transfer
  Impact: Interac is the dominant P2B payment method in Canada. Wire-only is friction for Canadian vendors.

MARKET 4: Australia (Invoice2go subsidiary, Cimrid Pty Ltd)
  Currently offer: Wire transfers
  Missing: PayTo, BPAY, NPP (New Payments Platform)
  Impact: Invoice2go has Australian roots but no local payment rails confirmed for outbound AP.

MARKET 5: United Kingdom (estimated traffic)
  Currently offer: Wire transfers
  Missing: Open Banking, Faster Payments, BACS Direct Debit
  Impact: UK Open Banking enables instant, low-cost bank transfers replacing expensive international wires.

**Payment complaint evidence:**
- Trustpilot: 2.8 to 3.1/5 (540+ reviews)
- BBB complaints: held funds, unauthorized charges
- Service quality decline linked to 2025 layoffs
- SmartCustomer/Capterra: hidden fees (ACH, integration, per-user)
- Reddit/Quora: customer support unresponsive
- QuickBooks sync failures affecting reconciliation

**Key meeting angles:**
1. **$380B+ annual volume with activist pressure for margin improvement** | Every basis point in routing optimization translates to millions at this scale
2. **PE buyout imminent** | Hellman and Friedman talks mean payment infrastructure audit is likely. Cost optimization is the first thing PE examines
3. **Wire-only international rails** | 137 countries served but no local APMs for outbound AP payments. $14.99 per wire adds up fast
4. **Single-issuer Divvy dependency** | Cross River Bank + Marqeta with zero failover for 498K+ businesses
5. **ERP channel amplification** | NetSuite, Acumatica, Paychex all embedding BILL's limited rails. One Yuno integration upgrades all channels
6. **Growing complaint volume** | Post-layoff service quality decline makes automated payment orchestration more valuable, not less
7. **Stablecoin early adopter** | Zerohash USDC integration shows willingness to innovate on payment rails

**Sources:**
- [BILL: International Payments](https://www.bill.com/product/international-payments)
- [BILL: Payments Product](https://www.bill.com/product/payments)
- [BILL: Pricing](https://www.bill.com/product/pricing/)
- [BILL: Security](https://www.bill.com/product/security)
- [BILL: Q1 FY2026 Earnings](https://investor.bill.com/news/news-details/2025/BILL-Reports-First-Quarter-Fiscal-Year-2026-Financial-Results/default.aspx)
- [BILL: Q2 FY2026 Presentation](https://www.investing.com/news/company-news/bill-com-q2-2026-presentation-slides-17-core-revenue-growth-despite-market-headwinds-93CH-4489209)
- [BILL: NetSuite Partnership](https://investor.bill.com/news/news-details/2025/NetSuite-and-BILL-Partner-to-Accelerate-Accounts-Payable-Processes-2025-SUx212Ie36/default.aspx)
- [JPMorgan Chase: BILL Partnership](https://www.bill.com/press-release/jpmorgan-chase-simplify-sending-and-receiving-business-payments)
- [Marqeta: BILL Partnership](https://investors.marqeta.com/news-releases/news-release-details/marqeta-and-billcom-partner-power-new-commercial-card-programs)
- [Cross River: Divvy Case Study](https://www.crossriver.com/case-study/divvy)
- [Hellman and Friedman Buyout Talks](https://finance.yahoo.com/news/hellman-friedman-reportedly-discussions-buy-091742285.html)
- [Payments Dive: Activist Investors](https://www.paymentsdive.com/news/bill-ceo-defends-company-performance-activist-Elliott-management-starboard-value/759878/)
- [Payments Dive: Path to Profits](https://www.paymentsdive.com/news/bill-weighs-the-best-path-to-profits/812067/)
- [Trustpilot: Bill.com](https://www.trustpilot.com/review/bill.com)
- [BBB: Bill.com Complaints](https://www.bbb.org/us/ca/alviso/profile/payment-processing-services/billcom-llc-1216-1000005293/complaints)
- [BILL: International Payment FAQ](https://help.bill.com/direct/s/article/360006829991)
