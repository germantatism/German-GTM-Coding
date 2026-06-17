# NEXHEALTH | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: NexHealth
═══════════════════════════════════════

Logo: https://brandfetch.com/nexhealth.com
Nombre merchant: NexHealth

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Single PSP Dependency
Tittle_Pain Point_2: 2% Statement Response
Tittle_Pain Point_3: No Payment Failover
Tittle_Pain Point_4: Limited BNPL Options
Tittle_Pain Point_5: EHR Sync Bottleneck

Desc_Pain Point_1: 10,000+ practices on Stripe Connect with zero backup. If Stripe declines spike or goes down, no failover exists. One outage blocks revenue for thousands.
Desc_Pain Point_2: Paper statements get 2% response. Even with text-to-pay, 37% of patients delay treatment over cost uncertainty. Declined payments mean lost chair time.
Desc_Pain Point_3: Card decline at terminal or text-to-pay has no auto-retry or cascade to a second processor. Staff must manually follow up, adding admin burden and delay.
Desc_Pain Point_4: Only Affirm for financing. No CareCredit, Sunbit, or Cherry. Sunbit reports 90% approval and 70% conversion. Missing these loses high-value procedures.
Desc_Pain Point_5: Ledger sync works for 4 EHRs only. Practices on other systems collect payments but cannot auto-reconcile, creating manual entry and errors.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe Connect (primary, all practices)
PSP_2: Affirm (BNPL, patient financing)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: CareCredit
Local_M_2: Sunbit
Local_M_3: Cherry
Local_M_4: PayPal
Local_M_5: Venmo
Local_M_6: HSA/FSA Direct Pay
Local_M_7: ACH Bank Transfer
Local_M_8: Klarna
Local_M_9: Afterpay
Local_M_10: Zip (QuadPay)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across multiple processors for 10,000+ dental practices. Each patient payment routed to the highest-approval acquirer for that BIN and issuer. 3-10% auth uplift recovers thousands of declined payments monthly.
Desc_Yuno_Cap2: Automatic cascade when Stripe declines a patient card. Instead of manual follow-up, Yuno retries via a secondary processor in milliseconds. Up to 50% recovery on soft declines. Critical for high-value dental procedures where re-engagement costs chair time and staff hours.
Desc_Yuno_Cap3: Activates patient financing options dental patients demand: CareCredit, Sunbit (90% approval), Cherry, PayPal, Venmo, HSA/FSA, ACH. One API, 1,000+ payment methods. Reduces treatment abandonment from cost uncertainty.
Desc_Yuno_Cap4: One dashboard replacing single-PSP dependency across 10,000+ practices. Real-time approval rates per practice, centralized reconciliation with EHR ledger sync, NOVA fraud detection (75% reduction) flagging friendly fraud.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**NexHealth at a glance:**
- Founded: 2017 by Alamin Uddin. HQ: San Francisco, CA (additional office in Draper, UT)
- Total funding: $177M across 6 rounds (Series C: $125M in April 2022)
- Valuation: $1B (unicorn status by end of 2022)
- Employees: ~209 (as of January 2026)
- 10,000+ dental and medical practice customers
- Revenue: $7.83M ARR reported in FY 2021 (current revenue likely significantly higher post-Series C)
- Core product: Patient experience platform (scheduling, forms, messaging, payments, insurance verification)
- Developer platform: Synchronizer API connects to 20+ dental Practice Management Systems
- Expanding beyond dental into broader medical practices

**Confirmed Payment Stack:**
- Stripe Connect: Primary payment processor for all 10,000+ practices (confirmed via Stripe case study)
- Payment Element: Stripe's embeddable UI component supporting multiple payment methods
- Affirm: BNPL option for patient financing (pay-over-time)
- Apple Pay: Supported (20% of patients chose it in first week of availability)
- Google Pay: Supported
- HSA/FSA cards: Accepted via card-on-file
- ACH: Available through Stripe integration
- Terminal: In-office payment terminals synced to EHR ledger
- Text-to-pay: Remote payment collection via SMS/email links
- Pricing: In-office terminal 2.6% + $0.07; Text-to-pay 2.9% + $0.30

**Payment Industry Context (Healthcare/Dental):**
- 65% of dental practices say delayed or rejected claims are their #1 source of lost revenue
- 80% of dental practices experience financial concerns from billing challenges
- 37% of patients delay or decline treatment due to cost uncertainty
- Mailed paper statements get only 2% response rate
- 18+ states passed 30+ laws in 2025 targeting dental payment pain points
- Friendly fraud in dental: patients not recognizing practice name on bank statement
- Sunbit achieves 90% approval and 70% conversion for dental financing
- CareCredit has 270,000+ healthcare practices in its network

**Competitive Landscape:**
- Weave: Integrated VoIP + patient engagement + payment processing (primary competitor)
- Rectangle Health: Payment and patient engagement for healthcare
- Birdeye: Marketing/review platform with payment features
- Solutionreach: Patient engagement and communications
- RevenueWell: Practice marketing and patient communication
- Carepatron: Practice management software
- NexHealth differentiator: API-first platform with deep EHR integration and real-time ledger sync

**Top 5 Pain Point Evidence:**

1. SINGLE PSP DEPENDENCY
   - All 10,000+ practices route through Stripe Connect exclusively
   - No secondary processor or failover mechanism
   - Stripe case study confirms NexHealth chose Connect for simplicity, not redundancy
   - Any Stripe outage or policy change impacts every practice simultaneously

2. 2% STATEMENT RESPONSE
   - NexHealth's own research: mailed paper statements get 2% response rate
   - Text-to-pay improves this but 37% of patients still delay treatment over cost
   - Each abandoned payment represents lost chair time and procedure revenue
   - Practices jump between systems, re-enter payments, reconcile reports, and fix errors manually

3. NO PAYMENT FAILOVER
   - When a card declines at terminal or via text-to-pay, no automatic retry exists
   - Practice staff must manually contact patient for alternative payment
   - False declines cost merchants $25 for every $1 of actual fraud
   - 62% of users who encounter a payment error never return to the merchant

4. LIMITED BNPL OPTIONS
   - Only Affirm available for patient financing through NexHealth
   - Sunbit: 90% approval, 70% conversion, fees as low as 1.9% for practices
   - CareCredit: 270,000+ practices, $25,000 revolving credit lines
   - Cherry: Preferred by 80% of practices, instant approval, up to $50,000 loans
   - Missing these options means high-value procedures go unscheduled

5. EHR SYNC BOTTLENECK
   - LedgerSync works with only 4 systems: Open Dental, Dentrix, Eaglesoft, Dentrix Enterprise
   - Practices on other EHRs collect payments but cannot auto-reconcile
   - Manual data entry creates errors, duplicate entries, and reconciliation delays
   - Refund support varies by EHR (Dentrix maps refunds as adjustments)

**Key meeting angles:**
1. **10,000+ practices on a single PSP** | Smart routing adds processor redundancy without rebuilding the integration
2. **20% Apple Pay adoption in week one** | Patients want payment choice; Yuno unlocks 1,000+ methods via one API
3. **Unicorn-stage company ($177M raised)** | Payment infrastructure must match growth ambitions
4. **37% treatment abandonment** | More financing options (Sunbit, CareCredit, Cherry) convert hesitant patients
5. **EHR ledger sync is the moat** | Yuno orchestration complements the sync without replacing it
6. **Dental fraud is rising** | NOVA fraud detection catches friendly fraud patterns before chargebacks hit
7. **Competitive pressure from Weave** | Payment UX is a battleground; multi-processor routing is a differentiator

**Sources:**
- [Stripe: NexHealth Case Study](https://stripe.com/customers/nexhealth)
- [NexHealth: Payments Feature Page](https://www.nexhealth.com/features/payments)
- [NexHealth: Payments Processing Cost](https://www.nexhealth.com/help-center/nexhealth-payments-processing-cost)
- [NexHealth: HSA/FSA/Debit/Credit Card Help](https://help.nexhealth.com/en/articles/11146340)
- [NexHealth: The 2% Problem (Text-to-Pay)](https://www.nexhealth.com/resources/text-to-pay-customer-success)
- [NexHealth: Synchronizer API](https://www.nexhealth.com/api)
- [NexHealth: Crunchbase Profile](https://www.crunchbase.com/organization/nexhealth)
- [NexHealth: Culture / About Page](https://www.nexhealth.com/culture)
- [NexHealth: Pricing Page](https://www.nexhealth.com/pricing)
- [NexHealth: Winter Release 2025](https://www.nexhealth.com/resources/winter-release-2025)
- [NexHealth: Payment Disputes Help](https://www.nexhealth.com/help/how-do-i-refund-a-patient-payment)
- [NexHealth vs Birdeye](https://www.nexhealth.com/compare/birdeye)
- [Brandfetch: NexHealth Brand Assets](https://brandfetch.com/nexhealth.com)
- [Sunbit: Dental Financing](https://sunbit.com/merchant-benefits/dental/)
- [Cherry: Dental BNPL](https://withcherry.com/blog/sunbit-vs-carecredit)
- [Outsource Strategies: Dental Billing Challenges 2025](https://www.outsourcestrategies.com/blog/top-dental-billing-challenges-solutions-2025/)
- [DOCS Education: Dental Insurance Reform 2025](https://www.docseducation.com/blog/why-dental-insurance-reform-2025-was-turning-point)
- [Curve Dental: Why Practices Lose Money on Payments](https://www.curvedental.com/blog/why-do-dental-practices-lose-money-on-payments-and-how-to-stop-it)
