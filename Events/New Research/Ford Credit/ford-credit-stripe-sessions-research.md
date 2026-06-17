# FORD CREDIT | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Ford Credit
=======================================

Logo: https://upload.wikimedia.org/wikipedia/commons/a/a0/Ford_Motor_Company_Logo.svg
Nombre merchant: Ford Credit

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Stripe-Only E-Commerce
Tittle_Pain Point_2: Fragmented Global Billing
Tittle_Pain Point_3: Dealer Payment Friction
Tittle_Pain Point_4: Limited Consumer APMs
Tittle_Pain Point_5: Cross-Border FX Drag

Desc_Pain Point_1: Ford's five-year Stripe deal (signed 2022) handles all e-commerce: vehicle orders, reservations, EV charging, and Ford Pro commercial financing. Single PSP dependency for digital retail across North America and Europe with no acquirer redundancy on billions in transaction volume.
Desc_Pain Point_2: Ford Credit operates across 20+ countries with separate systems: Stripe for e-commerce, FCE Bank for European auto finance, local bank transfers for loan repayments. No unified orchestration layer connecting $13.3B in annual revenue across consumer, dealer, and commercial segments.
Desc_Pain Point_3: Stripe Connect routes e-commerce payments to 3,000+ Ford and Lincoln dealers, but dealer wholesale floorplan financing ($21.9B non-consumer receivables) still runs on legacy bank rails. Dealers in emerging markets lack digital payment acceptance entirely.
Desc_Pain Point_4: Auto loan and lease repayments limited to ACH bank transfer, check, wire (MoneyGram/Western Union), and payroll deduction in the US. No debit card payments, no digital wallets (Apple Pay, Google Pay), no real-time payment options for 4.4M+ active contracts.
Desc_Pain Point_5: FCE Bank processes SEPA payments in Europe, but cross-border dealer wholesale financing between US, UK, and EU markets incurs multi-day settlement delays and FX conversion fees through correspondent banking. No real-time multi-currency settlement capability.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (e-commerce: vehicle orders, reservations, EV charging)
PSP_2: Stripe Connect (dealer payment routing, 3,000+ dealers)
PSP_3: FCE Bank plc (European auto finance, SEPA)
PSP_4: ACH / bank transfers (US loan repayments)
PSP_5: MoneyGram / Western Union (wire transfers)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Apple Pay
Local_M_2: Google Pay
Local_M_3: RTP / FedNow (US)
Local_M_4: Open Banking (UK)
Local_M_5: Pix (Brazil)
Local_M_6: UPI (India)
Local_M_7: BLIK (Poland)
Local_M_8: iDEAL (Netherlands)
Local_M_9: Bancontact (Belgium)
Local_M_10: OXXO (Mexico)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each vehicle order, loan repayment, and dealer settlement to the highest-performing acquirer by country, card BIN, and payment type. With $13.3B in annual Ford Credit revenue across 20+ countries, even a 3% approval uplift on digital transactions recovers hundreds of millions in previously lost or delayed payments.
Desc_Yuno_Cap2: Automatic cascade removes Ford's sole Stripe dependency for e-commerce. When Stripe declines a vehicle reservation or EV charging payment, Yuno reroutes to the next best acquirer in milliseconds. Up to 50% recovery on soft declines across millions of annual digital transactions spanning North America and Europe.
Desc_Yuno_Cap3: Activates the payment methods Ford Credit's global customer base needs: Apple Pay and Google Pay for US loan repayments, Open Banking in the UK, Pix in Brazil, UPI in India, iDEAL in Netherlands, BLIK in Poland. One API, 1,000+ payment methods. No engineering sprints per market.
Desc_Yuno_Cap4: One dashboard consolidating Stripe e-commerce, FCE Bank European finance, ACH loan collections, and dealer wholesale settlements into a unified view. Real-time approval rate monitoring across all 20+ markets, centralized reconciliation for $150B+ in managed assets. Full payment visibility across Ford Credit's consumer, commercial, and dealer portfolios.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Ford Credit at a glance:**
- Ford Motor Credit Company LLC, wholly-owned subsidiary of Ford Motor Company, founded 1959
- HQ: Dearborn, Michigan. ~6,400 employees worldwide
- Revenue: $13.27B (FY2025). EBT: $2.557B (FY2025, up from $1.654B in FY2024)
- Total managed assets: $150B+ (finance receivables + operating leases)
- Consumer receivables: $43.0B. Non-consumer (dealer wholesale): $21.9B (Q2 2025)
- 4.4M+ active retail and lease contracts (estimated)
- Operations in 20+ countries across North America, Europe, Asia Pacific, and Latin America
- FCE Bank plc: European subsidiary, UK-domiciled, operates branches across France, Spain, Ireland, Germany, Italy
- Ford Pro FinSimple: commercial customer financing arm
- Credit ratings: investment grade (Moody's, S&P, Fitch)
- Parent Ford Motor Company: $185B+ revenue (FY2025), NYSE: F

**Confirmed PSPs and Infrastructure:**
- Stripe: primary e-commerce payment processor (five-year deal signed January 2022)
- Stripe Connect: routes customer payments to correct local Ford/Lincoln dealer
- Stripe Identity: customer verification for vehicle orders
- Stripe Radar: fraud prevention for e-commerce
- FCE Bank plc: European auto finance (SEPA Credit Transfers, SEPA Instant, SEPA Direct Debit)
- ACH: US loan and lease repayments via linked bank account
- MoneyGram / Western Union: wire transfer payment option
- Payroll deduction: available for Ford employees and government workers
- Check/mail payments: traditional paper-based option
- No payment orchestrator detected
- No multi-acquirer routing for e-commerce
- Ford Credit app: iOS and Android for payment management

**Accepted payment methods (consumer loan/lease repayments):**
- Bank account (ACH direct debit) via Account Manager or Guest Pay
- Wire transfer via MoneyGram or Western Union
- Payroll deduction (Ford employees, government employees)
- Check by mail
- Third-party bill pay services (doxo: credit card, debit card, bank account)
- NO direct debit card acceptance on ford.com
- NO Apple Pay or Google Pay for loan payments
- NO real-time payment options (RTP, FedNow)

**Accepted payment methods (e-commerce / vehicle orders):**
- Credit/debit cards via Stripe (Visa, Mastercard, Amex)
- Bank transfers via Stripe
- Ford.com vehicle reservations and deposits processed through Stripe

**Ford Credit Europe (FCE Bank) payment methods:**
- SEPA Credit Transfer
- SEPA Instant Transfer
- SEPA Direct Debit
- Local bank transfers by country
- Operations: UK, France, Germany, Spain, Italy, Ireland, and additional markets

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (core market, ~75% of portfolio)
  Accepted: ACH, wire transfer, check, payroll deduction
  Missing: Apple Pay, Google Pay, RTP, FedNow, debit card direct
  Note: 4M+ US contracts. No modern payment methods for recurring loan payments

MARKET 2: United Kingdom (major European market)
  Accepted: SEPA DD (via FCE Bank), bank transfer
  Missing: Open Banking, Faster Payments for instant repayment, Apple Pay
  Note: FCE Bank is UK-domiciled. Open Banking adoption is high in UK auto finance

MARKET 3: Germany (largest EU auto market)
  Accepted: SEPA DD, SEPA Credit Transfer
  Missing: Giropay, Klarna installments, PayPal
  Note: Card penetration only 35% in Germany. Bank-based payments dominate

MARKET 4: Brazil (growing Ford market)
  Accepted: Local bank transfer (limited)
  Missing: Pix, Boleto, BRL installments
  Note: Pix handles 70%+ of digital payments. Ford sells vehicles in Brazil

MARKET 5: Mexico (USMCA market)
  Accepted: Limited local options
  Missing: OXXO, SPEI, MXN local billing
  Note: OXXO cash payments essential for unbanked auto buyers

**Key meeting angles:**
1. **Stripe dependency expiring** | Five-year Stripe deal signed January 2022 expires ~January 2027. Ford will evaluate payment infrastructure as contract renewal approaches
2. **$150B+ managed assets, fragmented payments** | Consumer loans, dealer wholesale, e-commerce all on separate rails. No unified orchestration across segments
3. **Legacy repayment methods** | ACH, check, and wire transfer are the only direct options for US auto loan payments. No digital wallets, no real-time payments for 4M+ contracts
4. **Dealer payment complexity** | 3,000+ Ford/Lincoln dealers. Stripe Connect handles e-commerce routing, but wholesale floorplan financing uses legacy bank rails
5. **Europe already on SEPA** | FCE Bank processes SEPA but operates as a separate silo from North American Stripe infrastructure
6. **Ford Pro commercial opportunity** | FinSimple commercial financing could benefit from multi-rail payment orchestration for fleet operators across markets

**Sources:**
- [Stripe: Ford-Stripe Agreement](https://stripe.com/newsroom/news/stripe-ford-agreement)
- [CNBC: Ford Signs Five-Year Payments Deal with Stripe](https://www.cnbc.com/2022/01/17/ford-signs-five-year-payments-deal-with-stripe-for-e-commerce-drive.html)
- [Ford Credit Ways to Pay](https://www.ford.com/finance/ways-to-pay/)
- [Ford Credit Payment Options FAQ](https://www.ford.com/finance/customer-support/payments/what-payment-options-are-available/)
- [Ford Credit Wikipedia](https://en.wikipedia.org/wiki/Ford_Credit)
- [Ford Credit Investor Center](https://www.ford.com/finance/investor-center/)
- [Ford Q4 2025 Earnings Press Release](https://s205.q4cdn.com/882619693/files/doc_financials/2025/q4/Ford-Q4-2025-Earnings-Press-Release.pdf)
- [Ford Credit Europe (FCE Bank)](https://www.fcebank.com/about-ford-credit.html)
- [Ford Credit Corporate Page](https://corporate.ford.com/operations/ford-credit/)
- [Stripe Blog: Auto Industry Disruption](https://stripe.com/blog/the-disruption-the-auto-industry-has-been-waiting-for)
- [Ford Authority: Ford E-Commerce with Stripe](https://fordauthority.com/2022/01/ford-to-build-modern-e-commerce-payment-system-with-stripe/)
- [JD Power 2025 Auto Finance Satisfaction Study](https://www.jdpower.com/business/press-releases/2025-us-automotive-financing-satisfaction-study)
