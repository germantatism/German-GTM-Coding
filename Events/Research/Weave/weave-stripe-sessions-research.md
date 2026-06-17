# WEAVE | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Weave
=======================================

Logo: https://cdn.brandfetch.io/idkoMXMVjH/w/512/h/512/theme/dark/icon.jpeg
Nombre merchant: Weave

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Single PSP Lock-In
Tittle_Pain Point_2: High Processing Costs
Tittle_Pain Point_3: Limited Payment Reach
Tittle_Pain Point_4: Billing Collection Gaps
Tittle_Pain Point_5: No Smart Routing

Desc_Pain Point_1: Weave runs 100% of payment volume through Stripe Connect with no alternative processor. A multi-year exclusive agreement locks 40,000 locations into a single acquirer. If Stripe experiences downtime or declines a transaction, there is zero fallback. For healthcare practices where every patient payment matters, single-PSP dependency creates invisible revenue leakage.
Desc_Pain Point_2: Weave resells Stripe processing at a flat-rate markup, meaning practices pay significantly more than interchange-plus pricing. With $239M in ARR and payments as a growing revenue line, the cost structure flows down to dental, optometry, and veterinary offices. Practices report fees are too high compared to direct processing alternatives, but switching means losing integrated communications.
Desc_Pain Point_3: Weave Payments operates only in the United States and Canada, supporting credit/debit cards, ACH, Apple Pay, Google Pay, and Stripe Link. No support for international patient wallets, no BNPL beyond third-party Sunbit integration, no local European or Latin American methods. As healthcare tourism grows and multi-location groups expand internationally, the payment gap widens.
Desc_Pain Point_4: Nearly half of healthcare providers identify timely patient collections as their primary revenue cycle concern. 67% of providers see patients delaying care due to cost. Weave offers Text to Pay and payment plans, but lacks intelligent retry logic for failed payments, no automated dunning optimization, and payment writebacks to practice management systems like Open Dental frequently fail.
Desc_Pain Point_5: With only Stripe processing all transactions, Weave has no ability to route payments to the best-performing acquirer per transaction. No BIN-level optimization, no issuer-based routing, no geographic routing for Canadian vs. US cards. Every declined transaction is a lost patient payment with no automatic retry across alternative processors.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe Connect (primary, exclusive processor)
PSP_2: Stripe Terminal / Verifone (in-office)
PSP_3: Sunbit (third-party BNPL partner)
PSP_4: CareCredit (third-party financing)
PSP_5: N/A

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Interac (Canada)
Local_M_2: PayPal
Local_M_3: Klarna
Local_M_4: Affirm
Local_M_5: Afterpay
Local_M_6: Venmo
Local_M_7: Alipay
Local_M_8: WeChat Pay
Local_M_9: iDEAL
Local_M_10: Pix

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Recovery
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing that breaks Weave's single-PSP lock-in. Instead of sending every patient payment exclusively through Stripe, Yuno routes each transaction to the highest-performing acquirer for that card BIN, issuer, and geography. Across 40,000 healthcare locations processing patient payments daily, smart routing delivers +3 to 10% authorization uplift, recovering revenue on declined copays, treatment plans, and recurring payment plans.
Desc_Yuno_Cap2: Eliminates the zero-fallback risk of Stripe-only processing. When Stripe declines a patient payment, Yuno automatically cascades to alternative processors in milliseconds. Up to 50% recovery on soft declines via instant retry. NOVA AI recovers up to 75% of failed transactions. For healthcare practices where a failed payment delays treatment or disrupts cash flow, failover is critical infrastructure.
Desc_Yuno_Cap3: Unlocks the payment methods Weave's Stripe-only stack cannot offer: Interac for Canadian practices, PayPal and Venmo for patient convenience, Klarna and Affirm for BNPL on high-value dental and veterinary procedures, Alipay and WeChat Pay for medical tourism patients. One API, 1,000+ payment methods. 31% of healthcare patients already use payment plans; native BNPL increases that adoption.
Desc_Yuno_Cap4: One dashboard replacing Weave's Stripe-only dependency with a multi-acquirer layer. Real-time approval rate monitoring across 40,000 locations, centralized reconciliation for patient payments, refunds, and payment plans, millisecond anomaly detection via Monitors. Weave keeps its communications platform while Yuno optimizes the payment layer underneath, reducing the processing cost markup that practices currently absorb.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Weave at a glance:**
- Model: All-in-one patient communications, engagement, and payments SaaS platform for healthcare practices
- Verticals: Dental (primary), optometry, veterinary, specialty medical, multi-location groups
- Revenue: $239.0M (FY2025), up 17% YoY from $204.3M (FY2024)
- Q4 2025 Revenue: $63.4M (+17% YoY)
- Net Loss: $28.1M (FY2025); accumulated deficit of $319.1M
- Locations: ~40,000 (as of December 31, 2025)
- Customers: 30,000+
- Net New Locations Added (2025): 4,628
- Employees: 904
- Market Cap: ~$383M (NYSE: WEAV)
- TAM: $10B domestic, $22B international (post-TrueLark acquisition)
- Founded: 2008, Lehi, Utah
- CEO: Brett White (appointed August 2022; former CFO/COO at Mindbody, senior finance at Oracle)
- CTO: Ashish Chaudhary
- CFO: Jason Christiansen
- CRO: Matt Hyde
- CPO: Branden Neish
- CMO: Chris Baird
- CLO: Erin Goodsell

**TrueLark Acquisition (May 2025):**
- Acquired for $35M ($25M cash + $10M equity)
- AI-powered virtual receptionist and front-desk automation
- Handles scheduling, rescheduling, and inquiries via SMS and web chat 24/7
- Expanded Weave's TAM from $10B to $22B internationally
- Completed May 19, 2025

**ADA Endorsement:**
- Selected as American Dental Association's endorsed Patient Engagement solution
- Exclusive co-marketing access to ADA's 160,000 members

**Payments Infrastructure:**
- Stripe Connect: exclusive payment processor (multi-year agreement)
- Stripe Terminal: Verifone P400 for in-office payments (tap, dip, swipe)
- Mobile Tap to Pay: launched for mobile payment collection
- Payment processing volume growing at average 37% month over month
- Text to Pay: SMS-based remote payment collection
- Online Bill Pay: patient portal payments
- ACH Direct Debit: launched January 2024 for lower-cost bank transfers
- Card on File: stored payment credentials
- Scan to Pay: QR code payments
- Payment Plans: recurring installment schedules
- Apple Pay, Google Pay, Stripe Link: digital wallets
- Sunbit: third-party BNPL integration
- CareCredit: third-party patient financing
- Surcharging: up to 3% passthrough to patients (per Visa rules)
- No alternative PSP; no payment orchestration

**Payment Methods Supported:**
- Credit/debit cards: Visa, Mastercard, Amex, Discover
- ACH direct debit
- Apple Pay
- Google Pay
- Stripe Link
- Sunbit (BNPL, third-party)
- CareCredit (financing, third-party)

**Geographic Coverage:**
- United States (primary market, ~95%+ of revenue)
- Canada (expanded in 2019)
- No other international markets

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (primary, 40,000 locations)
  Currently offer: Visa/MC/Amex/Discover, ACH, Apple Pay, Google Pay, Stripe Link, Sunbit
  Missing: PayPal, Venmo, Klarna, Affirm, Afterpay, native BNPL
  67% of patients delay care due to cost. Native BNPL on dental ($2K-10K procedures) and veterinary ($1K-5K surgeries) increases conversion.

MARKET 2: Canada (expansion market)
  Currently offer: Visa/MC, Apple Pay, Google Pay
  Missing: Interac (Canada's dominant debit network), Interac e-Transfer, PayPal
  Interac processes 18M+ transactions daily in Canada. Not offering it for Canadian practices is a major gap.

MARKET 3: Medical Tourism Patients (growing segment)
  Currently offer: Visa/MC only
  Missing: Alipay, WeChat Pay, UPI, Pix, GrabPay
  Dental tourism is a $5.8B global market. US dental practices increasingly serve international patients who need their local wallets.

MARKET 4: Multi-Location Enterprise Groups (DSOs, veterinary chains)
  Currently offer: Stripe-only flat rate
  Missing: Multi-acquirer routing, volume-based pricing, centralized treasury
  Dental Service Organizations (DSOs) manage 100-500+ locations. Single-PSP lock-in prevents cost optimization at scale.

MARKET 5: Specialty Medical (dermatology, cosmetic, fertility)
  Currently offer: Cards, ACH, Sunbit
  Missing: CareCredit native integration, Klarna, Affirm, Afterpay, custom payment plans
  High-value elective procedures ($5K-50K) require flexible BNPL. Third-party redirects lose conversion.

**Payment Pain Points:**
1. Single-PSP lock-in with Stripe (no fallback, no negotiation leverage)
2. Flat-rate processing markup makes Weave more expensive than direct processing
3. No payment orchestration or smart routing
4. ACH writebacks to Open Dental and other PMS systems frequently fail
5. No native BNPL (relies on third-party Sunbit/CareCredit redirects)
6. Limited to US and Canada only
7. No Interac support for Canadian practices
8. Patient collections remain top revenue cycle challenge (50%+ time on admin tasks)
9. No intelligent retry or dunning optimization for failed payments
10. Support disappears post-onboarding; payment issues go unresolved

**Key Meeting Angles:**
1. **40,000 locations, single PSP**: Every patient payment flows through Stripe with zero failback. Yuno adds multi-acquirer routing without replacing Weave's platform
2. **Payment processing as growth engine**: Weave's payments volume grows 37% MoM. As volume scales, single-PSP pricing becomes increasingly expensive. Yuno's routing optimizes cost per transaction
3. **BNPL opportunity for healthcare**: 67% of patients delay care due to cost, 31% already use payment plans. Native Klarna/Affirm via Yuno converts more patients than third-party Sunbit redirects
4. **Canadian market gap**: No Interac support for Canada's dominant payment network. Yuno unlocks Interac and 1,000+ local methods
5. **DSO and enterprise scale**: Multi-location groups need multi-acquirer routing to optimize costs. InDrive achieved 90% approval across 10 markets with Yuno
6. **Medical tourism opportunity**: Dental tourism is a $5.8B market. Alipay, WeChat Pay, and UPI via Yuno serve international patients. McDonald's gained +4.7% auth rate with Yuno
7. **CEO has payments DNA**: Brett White was CFO/COO at Mindbody (also a Stripe customer). He understands payment infrastructure deeply and knows the limitations of single-PSP dependency
8. **AI + Payments convergence**: TrueLark acquisition shows Weave investing in AI automation. Yuno's NOVA AI (75% recovery on failed transactions) aligns with their AI-first strategy

**Sources:**
- [Stripe Customer Story: Weave](https://stripe.com/customers/weave)
- [Weave Payments](https://www.getweave.com/weave-payments/)
- [Weave Healthcare Payment Processing](https://www.getweave.com/use-cases/healthcare-payment-processing/)
- [Weave ACH Direct Debit Launch](https://www.businesswire.com/news/home/20240110426036/en/Weave-Brings-ACH-Direct-Debit-to-Payments-Suite)
- [Weave Deepens Partnership with Stripe](https://www.businesswire.com/news/home/20230328005204/en/Weave-Deepens-Partnership-with-Stripe-Adding-New-Features-for-Small-Businesses)
- [Weave FY2025 Financial Results](https://www.businesswire.com/news/home/20260218591820/en/Weave-Announces-Fourth-Quarter-and-Full-Year-2025-Financial-Results)
- [Weave 10-K SEC Filing 2025](https://www.stocktitan.net/sec-filings/WEAV/10-k-weave-communications-inc-files-annual-report-237a68ecdf5f.html)
- [Weave TrueLark Acquisition](https://www.businesswire.com/news/home/20250505777895/en/Weave-Communications-to-Acquire-TrueLark-Accelerating-AI-Powered-Front-Office-Automation)
- [Weave Payment Processing Service Terms](https://www.getweave.com/legal/payments/)
- [Weave Payments Review (Merchant Cost Consulting)](https://merchantcostconsulting.com/lower-credit-card-processing-fees/weave-payments-review/)
- [Weave Mobile Tap to Pay Launch](https://www.getweave.com/weave-expands-payment-product-suite-with-mobile-tap-to-pay/)
- [Weave Investor Relations](https://investors.getweave.com/)
- [Capterra: Weave Reviews](https://www.capterra.com/p/141842/Weave/reviews/)
- [PYMNTS: Weave ACH Direct Debit](https://www.pymnts.com/healthcare/2024/weave-introduces-ach-direct-debit-payments-for-patients/)
