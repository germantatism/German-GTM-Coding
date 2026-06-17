# MOCHI HEALTH | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Mochi Health
=======================================

Logo: https://joinmochi.com/cdn/shop/files/mochi-health-logo.png
Nombre merchant: Mochi Health

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: High-Risk Merchant Status
Tittle_Pain Point_2: Chargeback Epidemic
Tittle_Pain Point_3: Dual Subscription Confusion
Tittle_Pain Point_4: Single PSP Fragility
Tittle_Pain Point_5: Pharmacy Billing Splits

Desc_Pain Point_1: GLP-1 telehealth is high-risk for card networks: recurring billing, prescription drugs, regulatory scrutiny. Stripe can freeze accounts once volume scales.
Desc_Pain Point_2: 1,285 BBB complaints in 3 years, most billing-related. Auto-renewals and dual subscriptions generate chargebacks that threaten processing privileges.
Desc_Pain Point_3: Two independent subscriptions: $79/mo membership and $99-$199/mo medication. Patients cancel one but not the other, triggering unwanted charges and disputes.
Desc_Pain Point_4: 100K+ patients at $79-$278/mo flow through a single processor. Any account freeze or compliance flag blocks recurring revenue across all 15 US states.
Desc_Pain Point_5: Membership fees go to Mochi; medication charges route through pharmacy partners. Reconciling two revenue streams and split refunds creates complexity.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (confirmed, primary billing)
PSP_2: Not confirmed
PSP_3: Not confirmed
PSP_4: Not confirmed

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: HSA/FSA Direct Pay
Local_M_2: ACH Bank Transfer
Local_M_3: Affirm
Local_M_4: Klarna
Local_M_5: Afterpay
Local_M_6: CareCredit
Local_M_7: Cash App Pay
Local_M_8: Venmo
Local_M_9: Apple Pay
Local_M_10: Google Pay

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each recurring charge to the optimal acquirer by card BIN, issuer, and amount. With 100K+ patients paying $79-$278/mo, a 3% auth uplift recovers thousands of renewals. InDrive achieved 90% approval via Yuno routing.
Desc_Yuno_Cap2: Automatic cascade eliminates single-PSP dependency. When Stripe declines a renewal or flags the account, Yuno reroutes to a backup acquirer in milliseconds, keeping patient subscriptions active. Up to 50% recovery on failed transactions, critical for high-risk telehealth billing.
Desc_Yuno_Cap3: Adds ACH for lower-cost recurring billing, Apple Pay and Google Pay for mobile app checkout, and BNPL options (Affirm, Klarna) that let patients split $99-$199/mo medication costs. One API, 1,000+ methods, reducing payment friction that causes churn.
Desc_Yuno_Cap4: One dashboard unifying membership and medication billing streams, real-time chargeback monitoring, and centralized refund management. NOVA AI recovers 75% of failed renewals via automated outreach, reducing the support burden from 1,285+ billing complaints per year.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Mochi Health at a glance:**
- Founded: 2022, HQ: San Francisco, California
- Founder & CEO: Dr. Myra Ahmad (MD, University of Washington; research at UCSF, MIT Koch Institute, MIT Sloan)
- Employees: ~273 (as of October 2025)
- Patients: 100,000+ active community
- Revenue: under $10M reported, but 100K patients at $79-$278/mo implies significantly higher implied ARR
- Growth: 500% year-over-year
- Milestone: patients have collectively lost 3M+ pounds
- Seed funding: $500K-$650K (AngelList, 2022); no publicly disclosed Series A
- Operates in 15 US states: AZ, CO, FL, GA, IL, MA, MD, MN, NY, OR, PA, RI, TX, VA, WA
- Expanding beyond obesity to comprehensive digital health platform (15 new care categories added November 2025)
- App available on iOS and Android

**Pricing model:**
- Membership: $79/mo (intro $39/mo first month), covers video visits, dietitian access, 24/7 support
- Subscription options: 1-month ($69), 3-month ($169), 12-month plans
- Compounded Semaglutide: +$99/mo (flat rate, all doses)
- Compounded Tirzepatide: +$199/mo (flat rate, all doses)
- Total cost: $178-$278/mo per patient

**Confirmed PSPs:**
- Stripe: confirmed as primary payment processor (patient portal references Stripe billing)
- No secondary PSP detected
- No payment orchestrator detected
- High-risk merchant classification means Stripe could restrict or shut down the account at scale

**Payment and billing complaints (evidence):**
- 1,285 BBB complaints in 3 years (Better Business Bureau)
- 15,000+ Trustpilot reviews (4.4/5 average, but billing complaints common)
- Key issue: dual subscription model (membership + medication billed separately) causes confusion
- Patients report charges continuing after cancellation because only one subscription was canceled
- $79 membership is non-refundable after 24 hours
- Disputed charges through credit card companies automatically flag the account, preventing Mochi from processing refunds
- March 2025: primary pharmacy partner Aequita shut down by Washington State for sterile compounding violations
- 2025: Eli Lilly lawsuit over compounded tirzepatide marketing (dismissed by federal court)

**High-risk merchant context:**
- GLP-1 telehealth classified as high-risk by card networks
- Chargeback potential, regulatory scrutiny, and card brand restrictions
- Low-risk processors (Stripe, Square) not built for regulated medical services at scale
- Account shutdowns common once volume scales or gets flagged
- Industry-wide: billing is #1 complaint category across all GLP-1 telehealth platforms in 2026

**Key meeting angles:**
1. **100K+ patients, single Stripe dependency** | All recurring revenue flows through one processor classified as high-risk for GLP-1 telehealth. One freeze stops everything.
2. **1,285 BBB complaints, most billing-related** | Dual subscription confusion, auto-renewals, and chargeback management need orchestration-level tooling.
3. **500% YoY growth amplifies payment risk** | Rapidly scaling patient base on a single PSP increases likelihood of compliance flags and account reviews.
4. **Pharmacy billing reconciliation** | Split billing between Mochi membership and pharmacy medication charges requires unified dashboard visibility.
5. **BNPL opportunity** | $178-$278/mo is a significant healthcare expense. Affirm, Klarna, or CareCredit installments could reduce churn and improve conversion.
6. **Mobile-first checkout** | App-based patients expect Apple Pay and Google Pay. Adding wallet methods reduces friction in mobile onboarding flow.
7. **Stripe relationship preserved** | Yuno sits on top of Stripe, adding backup acquirers and routing intelligence without requiring PSP migration or re-integration.

**Sources:**
- [Mochi Health Official Website](https://joinmochi.com/)
- [Mochi Health FAQ](https://joinmochi.com/faqs)
- [Mochi Health BBB Complaints](https://www.bbb.org/us/ca/san-francisco/profile/health-care/mochi-health-1116-955238/complaints)
- [Mochi Health Trustpilot](https://www.trustpilot.com/review/joinmochi.com)
- [Mochi Health ConsumerAffairs](https://www.consumeraffairs.com/health/mochi-health.html)
- [Mochi Health Crunchbase](https://www.crunchbase.com/organization/mochi)
- [Mochi Health CBInsights](https://www.cbinsights.com/company/mochi-health)
- [Mochi Health App Store](https://apps.apple.com/us/app/mochi-health-weight-loss-care/id6479331846)
- [GLP-1.com: Mochi Health Review](https://glp-1.com/providers/mochi-health)
- [US News: Mochi Health Review](https://health.usnews.com/best-diet/medication/mochi-health)
- [Telehealth Ally: Mochi Health Review](https://telehealthally.com/reviews/mochi-health)
- [Yahoo Finance: Mochi Health Platform Launch](https://finance.yahoo.com/news/mochi-health-launches-enhanced-online-232600908.html)
- [Mochi Health Blog: 3M Pounds Lost](https://joinmochi.com/blogs/mochi-health-patients-lose-over-3-million-pounds-combined)
- [Vector Payments: GLP-1 Payment Processing](https://www.vectorpayments.com/glp-1-payment-processing/)
- [Corepay: GLP-1 Payment Compliance](https://corepay.net/articles/glp-1-payment-compliance-for-medspas/)
- [Medical Foundation NC: GLP-1 Billing Guide](https://medicalfoundationofnc.org/glp1-telehealth-billing-and-cancellation-guide/)
- [HLTH Podcast: Dr. Myra Ahmad](https://hlth.com/insights/podcasts/building-affordable-transparent-consumer-healthcare-with-dr-myra-ahmad-ceo-of-mochi-health-2026-04-01)
- [Mochi Health Lawsuit 2026](https://lawfold.com/mochi-health-lawsuit/)
