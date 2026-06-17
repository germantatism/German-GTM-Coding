# COURSERA | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Coursera
═══════════════════════════════════════

Logo: https://upload.wikimedia.org/wikipedia/commons/9/97/Coursera-Logo_600x600.svg
Nombre merchant: Coursera

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Auth Rate Bleed
Tittle_Pain Point_2: Africa Payment Wall
Tittle_Pain Point_3: Fragmented Billing
Tittle_Pain Point_4: Subscription Churn
Tittle_Pain Point_5: FX Revenue Leak

Desc_Pain Point_1: 2.3M+ learners faced payment issues last year. Indian cards fail on international charges; African banks block USD debits. Declines erode a 197M-learner funnel.
Desc_Pain Point_2: Nigerian, Ghanaian, and Kenyan banks block international card transactions. Africa's fast-growing learner base cannot pay. Virtual USD cards are the only fix.
Desc_Pain Point_3: Billing split across direct web, Apple IAP, Google Play, Flywire, and enterprise invoicing. No unified dashboard to track approval rates or churn.
Desc_Pain Point_4: Revenue per user declining (learners +17% YoY, revenue only +9%). Failed recurring charges on Coursera Plus compound the user growth vs monetization gap.
Desc_Pain Point_5: USD pricing in 230+ countries forces FX conversion on every transaction. India gets INR pricing but most markets pay cross-border rates, adding 2-4% friction.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (primary)
PSP_2: PayPal
PSP_3: Apple App Store
PSP_4: Google Play
PSP_5: Flywire (degree programs)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: M-Pesa
Local_M_3: Boleto
Local_M_4: OXXO
Local_M_5: BLIK
Local_M_6: GCash
Local_M_7: PSE
Local_M_8: SPEI
Local_M_9: Nequi
Local_M_10: Bancontact

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across Stripe, PayPal, and local acquirers optimized by card BIN, issuer, and country. With $757M in annual revenue and 197M learners, even a 3% auth uplift translates to $22M+ in recovered annual revenue from reduced declines.
Desc_Yuno_Cap2: Automatic cascade when primary processor declines. Yuno reroutes to the next best acquirer in milliseconds, recovering subscription renewals that would otherwise churn. Up to 50% recovery on soft declines. Critical for Coursera Plus retention at scale.
Desc_Yuno_Cap3: Activates learners Coursera cannot reach: M-Pesa in Kenya, Pix in Brazil, OXXO in Mexico, Boleto in Brazil, GCash in Philippines, PSE in Colombia. One API, 1,000+ payment methods. Removes the card-only barrier in Africa and Latin America.
Desc_Yuno_Cap4: One dashboard unifying Coursera's fragmented billing: direct web (Stripe), PayPal, Apple IAP, Google Play, Flywire degrees, and enterprise invoicing. Real-time approval rate monitoring by market, centralized reconciliation, and anomaly detection via Monitors.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Coursera at a glance:**
- 197M registered learners (Q4 2025), 6.8M new learners added in Q4 alone
- Revenue: $757M (2025), up ~9% YoY. Q4 2025: $197M (Consumer $131.5M +12%, Enterprise $65.4M +5%)
- 2026 guidance: $805M to $815M revenue
- NYSE: COUR. Market cap ~$2.5B
- Founded 2012 by Andrew Ng and Daphne Koller (Stanford). HQ: Mountain View, CA
- 230+ countries and territories served
- Content: 7,000+ courses from 300+ university/industry partners (Google, IBM, Meta, Yale, Stanford)
- Degrees and certificates increasingly drive revenue (Flywire for degree tuition payments)

**Confirmed PSPs:**
- Stripe: primary card processor for web checkout (inferred from checkout flow and tech stack signals)
- PayPal: accepted for direct purchases
- Apple App Store / Google Play: mobile IAP
- Flywire: payment processor for degree program tuition (international wire transfers, local currency)
- UPI accepted in India (via Stripe India or Razorpay integration)
- EMI, Netbanking, digital wallets accepted in India
- No payment orchestrator detected

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (27.7M learners)
  Accepted: Visa/MC/Amex/Discover, PayPal, Apple Pay
  Missing: ACH, Cash App, Venmo (direct)
  Note: Primary market well served. Enterprise billing via invoicing.

MARKET 2: India (24.6M learners, #1 globally)
  Accepted: Visa/MC, UPI, RuPay, EMI, Netbanking, digital wallets, INR pricing
  Missing: Limited coverage but relatively well localized
  Note: India is Coursera's most advanced local payments market. 53% learn on mobile. RBI mandate still causes UPI auto-debit issues reported in support forums.

MARKET 3: Europe (24.5M learners combined)
  Accepted: Visa/MC, PayPal
  Missing: SEPA DD, iDEAL, Sofort, Bancontact, BLIK, Przelewy24
  Note: 46% of European learners are women. No European local APMs beyond cards and PayPal. SEPA DD critical for subscription billing.

MARKET 4: Brazil (large LatAm market)
  Accepted: Visa/MC, PayPal
  Missing: Pix, Boleto, local installment cards
  Note: Pix handles 70%+ of Brazil digital payments. No confirmed Pix support. Boleto essential for unbanked learners.

MARKET 5: Nigeria/Africa (fast-growing market)
  Accepted: Visa/MC (international-enabled only)
  Missing: Bank transfer, M-Pesa, Flutterwave local methods, MTN Mobile Money
  Note: Nigerian banks block international card charges. "2.3M+ learners faced payment issues in the past year." Virtual USD cards the only workaround.

**Payment issues documented:**
- 2.3M+ learners experienced payment issues in the past year
- Indian users report UPI payments not showing up in Coursera purchases
- African users face near-total card block from local banks
- Revenue-per-user declining despite learner growth (monetization gap)
- Coursera introduced one-time payment options as alternative to subscriptions (signal of subscription billing friction)

**Key meeting angles:**
1. **197M learners, basic payments** | Massive global user base with limited payment localization outside India
2. **Africa lockout** | Fastest-growing education market, but banks block international card charges entirely
3. **Revenue-per-user decline** | Learner growth outpacing revenue; better payment conversion directly improves monetization
4. **India success template** | UPI/EMI/Netbanking in India proves Coursera will localize payments when pressed. Yuno accelerates this globally
5. **Subscription billing friction** | One-time payment launch signals recurring billing challenges; Yuno failover reduces involuntary churn
6. **Degree program opportunity** | Flywire handles degree tuition; Yuno can orchestrate both consumer and institutional billing
7. **Competitor precedent** | Udemy (multi-PSP, Boleto, local methods), edX (PayPal + Cybersource)

**Sources:**
- [Coursera Brand Guide (Logo)](https://about.coursera.org/brand-guide)
- [Coursera Help: Accepted Payment Methods](https://www.coursera.support/s/article/learner-000001349)
- [Coursera Help: Solve Problems With Payments](https://www.coursera.support/s/article/learner-000001518)
- [Coursera Help: UPI Payment Issues](https://www.coursera.support/s/question/0D51U00003BlXcWSAV)
- [Coursera Blog: India Opportunities](https://blog.coursera.org/new-year-new-opportunities-for-learners-in-india/)
- [Coursera Blog: 2025 Learner Outcomes Report](https://blog.coursera.org/introducing-courseras-2025-learner-outcomes-report-global-findings-show-measurable-career-impact-for-online-learners/)
- [Class Central: Coursera Q4 2025 Review](https://www.classcentral.com/report/coursera-q4-2025-review/)
- [Class Central: Coursera One-Time Payment](https://www.classcentral.com/report/coursera-one-time-payment/)
- [ElectroIQ: Coursera Statistics 2025](https://electroiq.com/stats/coursera-statistics/)
- [Open2Study: Coursera Statistics 2026](https://www.open2study.com/statistics/coursera-statistics/)
- [BusinessToday: India Coursera Second Largest Market](https://www.businesstoday.in/latest/story/india-becomes-courseras-second-largest-market-with-136-million-users-311723-2021-11-09)
- [EverTry: How to Pay for Coursera in Africa](https://evertry.co/blog/how-to-pay-for-coursera-courses-in-africa-the-reliable-way/)
- [MicroEPay: Coursera Nigeria Payment Guide](https://microepay.com/blog/how-to-pay-for-coursera-courses-in-nigeria-without-payment-failures-the-complete-2025-guide/)
- [Wikipedia: Coursera](https://en.wikipedia.org/wiki/Coursera)
- [WallStreetZen: Coursera Statistics 2026](https://www.wallstreetzen.com/stocks/us/nyse/cour/statistics)
