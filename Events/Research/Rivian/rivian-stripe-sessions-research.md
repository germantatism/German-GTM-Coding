# RIVIAN | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Rivian
=======================================

Logo: https://companieslogo.com/img/orig/RIVN_BIG-f4a75de9.png?t=1752312076
Nombre merchant: Rivian

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Dual PSP, No Orchestrator
Tittle_Pain Point_2: DTC High-Value Declines
Tittle_Pain Point_3: EU Launch Without APMs
Tittle_Pain Point_4: Subscription Billing Gap
Tittle_Pain Point_5: Fleet Payment Complexity

Desc_Pain Point_1: Stripe and Braintree both active but with no orchestration. If one declines a $75K+ order, there is no automatic cascade. Manual failover only.
Desc_Pain Point_2: 100% DTC model means every payment failure is Rivian's loss. $75K+ transactions trigger issuer fraud blocks and velocity checks at high rates.
Desc_Pain Point_3: R2 launch across 10 EU countries planned for 2027 with zero local APMs in place: no SEPA DD, no iDEAL, no Klarna, no Swish.
Desc_Pain Point_4: Autonomy+ subscription launching Apr 2026, plus Connect+, FleetOS, insurance. Recurring billing on dual processors with no unified retry.
Desc_Pain Point_5: Amazon fleet of tens of thousands of Rivian vans needs enterprise billing, reconciliation, and payout management at commercial scale.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe
PSP_2: Braintree (PayPal)
PSP_3: Rivian Financial Services (captive financing)
PSP_4: Rivian Wallet (stored value)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: SEPA Direct Debit
Local_M_2: iDEAL
Local_M_3: Bancontact
Local_M_4: Klarna
Local_M_5: Swish
Local_M_6: BLIK
Local_M_7: Sofort
Local_M_8: EPS
Local_M_9: MobilePay
Local_M_10: Trustly

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each vehicle deposit, subscription charge, and accessory purchase to the best acquirer for that card BIN and market. With $5.39B in 2025 revenue and high-value transactions, a 3% auth uplift translates to millions in recovered vehicle sales annually.
Desc_Yuno_Cap2: When Stripe declines a $75K vehicle purchase, Yuno cascades to Braintree (or the next best acquirer) in milliseconds. The buyer completes checkout on first attempt. Up to 50% of failed high-value transactions recovered without customer friction.
Desc_Yuno_Cap3: Activates the APMs European R2 buyers expect: SEPA DD in Germany, iDEAL in Netherlands, Bancontact in Belgium, Klarna across EU, Swish in Sweden, BLIK in Poland, MobilePay in Denmark. One API, 1,000+ methods, 10-country EU launch with zero per-market integration.
Desc_Yuno_Cap4: Single dashboard orchestrating Rivian's Stripe + Braintree + Rivian Wallet + Rivian Financial Services streams. Real-time monitoring across vehicle sales, Autonomy+ subscriptions, FleetOS billing, and accessory purchases. NOVA detects anomalies in milliseconds.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Rivian at a glance:**
- Founded 2009, HQ Irvine, CA. Public: NASDAQ RIVN
- Revenue: $5.39B (FY2025), up 8.4% YoY. First consolidated gross profit: $144M
- Software and services revenue: $1.56B (2025), up from $484M (2024). Gross profit: $576M
- Delivered 51,579 vehicles in 2025. 2026 guidance: 62,000 to 67,000 vehicles (47% to 59% increase)
- VW joint venture: up to $5.8B total. Rivian supplies electrical architecture and software stack
- Manufacturing: Normal, IL (current). Georgia plant planned for 2026 with 400,000-unit capacity
- R2 (mid-size SUV, ~$45K): production starting 2026, European launch 2027
- European country pages live: UK, Germany, Belgium, Netherlands, Switzerland, Denmark, Spain, France, Italy, Sweden
- Amazon fleet: tens of thousands of electric delivery vans with FleetOS
- Autonomy+ paid subscription: launching April 2026
- CEO: RJ Scaringe (founder)

**Confirmed PSPs:**
- Stripe: primary payment processor (confirmed in privacy policy and payment terms)
- Braintree: secondary processor (confirmed in privacy policy)
- Both process deposits, vehicle purchases, and accessory orders
- Rivian Wallet: stored-value account for in-ecosystem purchases
- Rivian Financial Services: captive auto financing
- No payment orchestrator detected despite having two PSPs

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (sole current market for vehicle sales)
  OK Currently offer: Credit/debit card (Stripe/Braintree), Rivian Wallet, Rivian Financial Services
  Missing: Apple Pay checkout, BNPL (Affirm, Klarna), ACH direct
  Note: $75K+ average transaction value; high-value declines significant

MARKET 2: Germany (primary EU launch market for R2, 2027)
  OK Currently offer: Not yet live
  Missing: SEPA Direct Debit, Sofort, Klarna, GiroPay
  Note: ~35% credit card penetration. SEPA DD essential for subscriptions and accessories

MARKET 3: United Kingdom (confirmed R2 market)
  OK Currently offer: Not yet live
  Missing: Open Banking, Klarna UK, PayPal local
  Note: UK has strong card adoption but Open Banking growing fast for high-value transactions

MARKET 4: Netherlands (confirmed R2 market)
  OK Currently offer: Not yet live
  Missing: iDEAL (75%+ of Dutch payments), Bancontact
  Note: iDEAL is non-negotiable for Dutch market entry

MARKET 5: Sweden/Denmark (confirmed R2 markets)
  OK Currently offer: Not yet live
  Missing: Swish (Sweden), MobilePay (Denmark), Klarna
  Note: Nordic mobile wallets dominate; card-only checkout would limit R2 adoption

**Key meeting angles:**
1. **Two PSPs, zero orchestration** | Stripe and Braintree already in place but no intelligent routing between them. Classic Yuno use case.
2. **$1.56B software revenue** | Subscription billing (Autonomy+, Connect+, FleetOS) needs multi-market recurring payment infrastructure
3. **10-country EU launch** | R2 European entry in 2027 requires local APMs from day one across all 10 confirmed markets
4. **VW relationship** | $5.8B joint venture validates Rivian's tech platform; payment orchestration would further professionalize the stack
5. **Amazon fleet scale** | Tens of thousands of commercial vehicles need enterprise-grade billing, reconciliation, and payout management
6. **DTC model vulnerability** | No dealer network to absorb payment failures. Every declined transaction is a lost Rivian sale.

**Sources:**
- [Rivian Privacy Policy](https://rivian.com/privacy)
- [Rivian Payment Terms](https://rivian.com/en-CA/legal/payment)
- [Rivian Payment Terms Canada](https://rivian.com/legal/payment-canada)
- [Rivian Financing and Payments](https://rivian.com/support/financing-and-payments)
- [Rivian Deposits and Refunds](https://rivian.com/support/deposits-and-refunds)
- [Rivian Q4/FY2025 Results](https://rivian.com/newsroom/article/rivian-releases-fourth-quarter-full-year-2025-financial-results)
- [Rivian Software Revenue (TechCrunch)](https://techcrunch.com/2026/02/12/rivian-was-saved-by-software-in-2025/)
- [Rivian Software Revenue Target $2.5B](https://eletric-vehicles.com/rivian/rivian-targets-2-5-billion-in-software-revenue-for-2026-on-vw-deal-autonomy/)
- [Rivian European Expansion](https://www.carscoops.com/2025/09/rivians-r2-will-start-brands-global-expansion/)
- [Rivian R2 Europe 2027](https://electricdrives.tv/when-is-rivian-coming-to-europe/)
- [Rivian Sales Statistics](https://tridenstechnology.com/rivian-sales-statistics/)
- [Rivian Logo](https://companieslogo.com/rivian/logo/)
