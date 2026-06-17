# THRYV | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Thryv
=======================================

Logo: https://brandfetch.com/thryv.com
Nombre merchant: Thryv

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Fragmented Processor Mix
Tittle_Pain Point_2: US-Centric Payment Stack
Tittle_Pain Point_3: No Processor Failover
Tittle_Pain Point_4: SMB International Friction
Tittle_Pain Point_5: Recurring Payment Leakage

Desc_Pain Point_1: Thryv lets SMBs connect ThryvPay, Stripe, PayPal, or Square independently, but offers no unified layer to route between them. Each processor operates as a silo with separate dashboards, separate reconciliation, and no cross-processor optimization or analytics.
Desc_Pain Point_2: ThryvPay processes credit cards, ACH, Apple Pay, and Google Pay, but lacks non-card local methods for international markets. With the Keap acquisition expanding into Europe and Australia, SMB clients in those regions need SEPA, BECS, iDEAL, and local bank transfers.
Desc_Pain Point_3: Each SMB connects one payment processor at a time. If ThryvPay or Stripe declines a card or goes down, there is no automatic retry through an alternative processor. Every failed transaction requires the customer to manually retry or use a different payment method.
Desc_Pain Point_4: ThryvPay charges international credit card rates of 1.75% + $0.30, but only supports card-based payments globally. SMBs serving international customers lack Pix, UPI, OXXO, or other local methods that dominate non-US markets, capping conversion at card penetration rates.
Desc_Pain Point_5: Thryv supports recurring payments and installment plans through stored card and ACH, but declined renewals rely on basic retry logic within each processor. No cross-processor cascade or intelligent dunning to recover failed subscription charges across 100K+ SMB clients.

SLIDE 1: PSP TOPOLOGY

PSP_1: ThryvPay (native processor, credit cards + ACH + Apple Pay + Google Pay)
PSP_2: Stripe (integrated option for card payments)
PSP_3: PayPal / Braintree (integrated option)
PSP_4: Square (integrated option)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: SEPA Direct Debit
Local_M_2: iDEAL
Local_M_3: BECS Direct Debit
Local_M_4: Pix
Local_M_5: Boleto
Local_M_6: OXXO
Local_M_7: SPEI
Local_M_8: UPI
Local_M_9: BLIK
Local_M_10: Bancontact

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover Recovery
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Dashboard

Desc_Yuno_Cap1: Per-transaction routing optimizes every SMB payment across ThryvPay, Stripe, PayPal, and Square based on card BIN, issuer, and amount. With 100K+ SaaS clients processing invoices and recurring charges, even 3% auth uplift across the platform recovers significant revenue from declined payments.
Desc_Yuno_Cap2: Automatic cascade across Thryv's four connected processors. When ThryvPay declines a card charge, Yuno reroutes to Stripe or PayPal in milliseconds. Up to 50% recovery on failed transactions, directly reducing involuntary churn for SMBs running subscription and installment billing.
Desc_Yuno_Cap3: One API activates the local methods Thryv's international SMBs need post-Keap expansion: SEPA DD and iDEAL for Europe, BECS for Australia, Pix and Boleto for Brazil, UPI for India. 1,000+ payment methods, no per-market integration. SMBs accept how their customers prefer to pay.
Desc_Yuno_Cap4: Replaces Thryv's siloed processor dashboards with one unified view. Real-time approval rates across ThryvPay, Stripe, PayPal, and Square. Centralized reconciliation for invoices, subscriptions, and installments. NOVA intelligence delivers 75% faster fraud detection across all SMB payment flows.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Thryv at a glance:**
- Public company: NASDAQ: THRY
- Founded: Originally Dex Media/SuperMedia; SaaS launched 2015
- CEO & Chairman: Joe Walsh (joined 2014, previously Yellowbook CEO for 20+ years)
- President: Grant Freeman (promoted September 2023)
- Headquarters: Dallas, TX
- Employees: ~3,000+
- SaaS clients: 100,000+ (end of Q4 2025)
- Revenue: $480.7M total (FY2024), SaaS revenue grew 34% YoY in FY2025
- SaaS now contributes 62%+ of total revenue
- SaaS gross margins: 73% (Q3 2025)
- Net Revenue Retention: 94% (seasoned)
- Strategic pivot: Fully transitioning from Marketing Services to SaaS-only by 2028
- Acquisition: Keap (Infusion Software) for $80M cash (closed October 2024), expanding into Europe and Australia
- Products: CRM, appointment scheduling, ThryvPay, social media management, marketing automation, website builder, reputation management

**Confirmed PSPs:**
- ThryvPay: Native processor (credit cards at 2.6% + $0.30 in-person, 2.9% + $0.30 online; ACH at 1% min $1 max $9; international at 1.75% + $0.30)
- Stripe: Integrated option (cards, Apple Pay, Google Pay)
- PayPal / Braintree: Integrated option (e-wallet)
- Square: Integrated option (in-person and online)
- Apple Pay and Google Pay via ThryvPay and Stripe
- No payment orchestrator detected
- Plaid integration for ACH bank verification

**Payment challenges identified:**
- Four payment processors operate as independent silos with no unified routing or reconciliation
- ThryvPay is card/ACH-only; no local payment methods for international markets
- International expansion (post-Keap: Europe, Australia) requires local methods not currently supported
- No automatic failover between ThryvPay, Stripe, PayPal, and Square
- International card processing at premium rates (1.75% + $0.30) with no local alternatives
- Recurring payment recovery relies on individual processor retry logic, no cross-processor cascade
- SMBs serving international customers capped at card penetration rates in each market

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (primary market, 100K+ SMB clients)
  Accepted: Visa/MC/Amex/Discover, ACH, Apple Pay, Google Pay, PayPal
  Missing: Venmo (standalone), Cash App Pay
  Well-covered for US market. ACH and digital wallets serve most SMB use cases.

MARKET 2: Europe (expansion via Keap acquisition)
  Accepted: International cards via Stripe/PayPal
  Missing: SEPA Direct Debit, iDEAL, Bancontact, BLIK, Giropay, Przelewy24
  SEPA DD essential for European recurring billing. Keap clients in Europe need local methods.

MARKET 3: Australia (expansion via Keap acquisition)
  Accepted: International cards via Stripe/PayPal
  Missing: BECS Direct Debit, POLi, PayTo
  BECS DD is standard for Australian subscription billing. Key Keap market.

MARKET 4: Canada (North American market)
  Accepted: Cards via Stripe/PayPal/ThryvPay
  Missing: Interac e-Transfer, Interac Online
  Interac is Canada's dominant domestic payment method for SMB transactions.

MARKET 5: Latin America (emerging SMB market)
  Accepted: International cards via Stripe
  Missing: Pix, Boleto, OXXO, SPEI, PSE
  Pix handles 70%+ of Brazil digital payments. LatAm SMBs need local methods.

**Key meeting angles:**
1. **100K+ SMB platform** | Orchestration at platform level multiplies across entire client base; per-transaction routing lifts revenue for all SMBs
2. **Post-Keap international expansion** | Europe and Australia markets acquired but payment infrastructure not yet localized
3. **Four processors, zero orchestration** | ThryvPay/Stripe/PayPal/Square operate as silos; Yuno unifies routing and analytics
4. **SaaS transition momentum** | 34% SaaS growth, pivoting from legacy Marketing Services by 2028; payments infrastructure needs to match SaaS ambition
5. **Public company pressure** | NASDAQ: THRY under investor scrutiny; payment conversion improvements directly impact reported revenue
6. **Recurring billing at scale** | Subscriptions, installments, and recurring invoices across 100K+ SMBs need intelligent failover
7. **CEO buying stock** | Joe Walsh acquired 15K shares at $2.91 in March 2026, signaling confidence in turnaround

**Sources:**
- [Thryv Features](https://www.thryv.com/features/)
- [Thryv Payments](https://www.thryv.com/features/payments/)
- [ThryvPay](https://www.thryv.com/features/thryvpay/)
- [Thryv Compare Payment Processors](https://learn.thryv.com/hc/en-us/articles/360002070591-Compare-Payment-Processors-in-Thryv-Business-Center)
- [Thryv Accept Payments via Stripe](https://learn.thryv.com/hc/en-us/articles/360024504172-Accept-Payments-via-Stripe)
- [ThryvPay International FAQs](https://learn.thryv.com/hc/en-us/articles/9470641727757-ThryvPay-International-FAQs)
- [Thryv FY2025 SaaS Revenue Growth (BusinessWire)](https://www.businesswire.com/news/home/20260226660000/en/Thryv-Achieves-SaaS-Revenue-Growth-of-34-in-Full-Year-2025-Shifts-Focus-to-AI-Enabled-Market-Sell-Grow-Platform-to-Empower-SMBs)
- [Thryv Keap Acquisition (Investor Relations)](https://investor.thryv.com/news/news-details/2024/Thryv-Holdings-Announces-Closing-of-Strategic-Acquisition-of-Keap/default.aspx)
- [Thryv CEO Joe Walsh](https://www.thryv.com/about/corporate/joe-walsh/)
- [Thryv Grant Freeman Promotion](https://www.thryv.com/news/thryv-announces-promotion-of-grant-freeman-to-new-role-of-thryv-president/)
- [Thryv SEC 10-K Filing](https://www.sec.gov/Archives/edgar/data/1556739/000155673925000015/thry-20241231.htm)
- [Thryv Wikipedia](https://en.wikipedia.org/wiki/Thryv)
