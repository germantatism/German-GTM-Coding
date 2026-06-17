# FRONTDOOR | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Frontdoor
=======================================

Logo: https://asset.brandfetch.io/idPkL21xgN/idK5KXIKR5.svg
Nombre merchant: Frontdoor

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Past-Due Premium Invoices
Tittle_Pain Point_2: Multi-Brand Billing Sprawl
Tittle_Pain Point_3: Contractor Payout Friction
Tittle_Pain Point_4: Renewal Card Decay
Tittle_Pain Point_5: No Local Payment Methods

Desc_Pain Point_1: Frontdoor engaged Stripe Professional Services specifically to reduce past-due premium invoices, achieving only 1.84% improvement. With $2.1B revenue and 2.1M active warranties, past-due invoices represent significant recurring revenue leakage that a single PSP optimization engagement cannot fully solve.
Desc_Pain Point_2: Frontdoor operates 6 brands (AHS, HSA, OneGuard, Landmark, 2-10 HBW, ProConnect) after the $585M acquisition of 2-10 HBW in December 2024. Each brand runs its own billing flows. No orchestration layer unifies payment processing across the multi-brand portfolio for consolidated reporting and routing.
Desc_Pain Point_3: 17,000 independent contractor firms handle 3.8M annual service requests. Contractor payments flow through direct deposit and other rails. Managing payouts to thousands of contractor firms alongside 2.1M consumer premium collections creates dual-sided payment complexity without unified orchestration.
Desc_Pain Point_4: 76% of revenue comes from existing customer renewals. Annual and monthly plans auto-renew to saved cards. Card expiration, reissuance, and account updates cause silent payment failures. BBB and consumer complaints confirm customers charged after cancellation and billing disputes requiring bank intervention.
Desc_Pain Point_5: Frontdoor accepts credit/debit cards, PayPal, and checking account. No Apple Pay, Google Pay, or digital wallets natively in the AHS app despite 2M+ members. ProConnect (on-demand home services in 35 markets) lacks modern checkout options that consumers expect for on-demand service payments.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (primary card processor, confirmed via Stripe case study)
PSP_2: PayPal (alternative payment method for premium billing)
PSP_3: ACH / Checking Account (direct debit for monthly/annual premiums)
PSP_4: Direct Deposit (contractor firm payouts)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Apple Pay
Local_M_2: Google Pay
Local_M_3: Venmo
Local_M_4: Cash App Pay
Local_M_5: Affirm / BNPL
Local_M_6: Samsung Pay
Local_M_7: Zelle
Local_M_8: Amazon Pay
Local_M_9: ACH Push (consumer-initiated)
Local_M_10: Digital Wallets (Stripe Link)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing by card BIN, issuer, and geography. With 2.1M active warranties generating monthly/annual premium renewals, routing each charge to the optimal acquirer delivers 3-10% authorization uplift. Stripe's own advisory achieved only 1.84% improvement; multi-processor routing unlocks the remaining uplift.
Desc_Yuno_Cap2: Automatic cascade when a premium renewal card is declined. Instead of generating a past-due invoice and risking policy lapse, Yuno retries through the next best processor in milliseconds. Up to 50% recovery on failed transactions. With 76% of $2.1B revenue from renewals, each recovered charge protects recurring revenue.
Desc_Yuno_Cap3: Adds wallets Frontdoor's 2.1M members expect: Apple Pay, Google Pay, Venmo for premium payments. Cash App Pay and Affirm for ProConnect on-demand service fees. One API, 1,000+ methods. Modernizes checkout for a consumer base that manages home services from their phones.
Desc_Yuno_Cap4: One dashboard unifying Stripe card processing, PayPal, ACH premium billing, and contractor payouts across 6 brands (AHS, HSA, OneGuard, Landmark, 2-10 HBW, ProConnect). Real-time monitoring of renewal success rates per brand, post-acquisition billing consolidation, and NOVA fraud detection (75% reduction) protecting 3.8M annual transactions.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Frontdoor at a glance:**
- Founded: 2018 (spun off from ServiceMaster)
- HQ: Memphis, Tennessee
- Chairman & CEO: Bill Cobb
- Public: NASDAQ: FTDR
- Revenue: $2.099B (FY2025), up 14% YoY (record)
- Q4 2025: $433M revenue, up 13% YoY
- Net Income: $255M (FY2025)
- Adjusted EBITDA: $553M (FY2025), up 25% YoY
- Free Cash Flow: Up 69% YoY
- EPS: $0.23 (Q4 2025), beat forecast of $0.13
- Active Warranties: ~2.1M
- Builder Partners: ~20,000
- Contractor Network: ~17,000 independent firms (including 4,200 preferred contractors)
- Service Requests: ~3.8M annually
- Employees: ~1,000-1,700
- Revenue Mix: 76% from existing customer renewals
- Brands: American Home Shield (AHS), HSA, OneGuard, Landmark, 2-10 HBW, ProConnect, Streem
- Key Acquisitions: Streem (AR/AI diagnostics, Dec 2019), 2-10 Home Buyers Warranty ($585M cash, Dec 2024)
- Credit Facility: $1.47B (December 2024)
- Partnership: Moen (Flo Smart Water Monitor, exclusive agreement, 21 states)
- Technology: SkySlope partnership (AHS integration, April 2026)
- ProConnect: On-demand home services expanded to 35 markets

**Confirmed Payment Stack:**
- Stripe: Primary card processor. Confirmed via Stripe Professional Services case study. Frontdoor engaged Stripe for Revenue Optimization Advisory to improve authorization rates on past-due premium invoices
- Stripe Optimizations: Correctly labeling off-session payments, customer notification via webhooks and card fingerprints, Stripe Radar rule adjustments. Result: 1.84% reduction in past-due invoices
- PayPal: Alternative payment method for premium billing
- ACH/Checking Account: Direct debit for monthly/annual premium payments
- Credit/Debit Cards: Visa, MC, Amex for premium and service fee payments
- doxo: Third-party bill payment platform (Apple Pay available through doxo, not natively)
- Direct Deposit: Contractor payout method
- No payment orchestrator detected
- No Apple Pay or Google Pay native integration
- No multi-processor failover beyond Stripe

**Payment Method Gaps (Consumer Evidence):**
- Stripe case study confirms Frontdoor needed help with authorization rates on premium invoices
- BBB complaints: Customers charged after cancellation, unable to stop auto-renewals
- PissedConsumer: 4.8K reviews, 48% cite customer service issues
- Medium article: "The American Home Shield & Frontdoor Inc. Scam" details billing disputes
- Auto-renewal converts month-to-month to annual contracts without clear notice
- "Once automatic withdrawal information is provided, it cannot be removed"
- Service fee ($100+) collected per service request, in addition to monthly/annual premium
- No native Apple Pay or Google Pay in AHS app despite 2M+ mobile-first members

**Top Business Context:**

SEGMENT 1: Home Warranty Renewals (76% of revenue)
  Current: Stripe card processing + ACH direct debit + PayPal
  Gap: Card decay, expired cards, and insufficient-funds failures create past-due invoices
  Opportunity: Multi-processor failover + intelligent retry + wallet payments (Apple/Google Pay) reduce involuntary churn

SEGMENT 2: New Customer Acquisition
  Current: Online checkout and phone enrollment
  Gap: Limited payment options may reduce conversion at point of sale
  Opportunity: Modern checkout with wallets and BNPL options for annual plan commitments ($400-$700+ annually)

SEGMENT 3: Service Fee Collection ($100+ per request)
  Current: Card on file charged at service request
  Gap: Same card decay issues as premiums
  Opportunity: 3.8M annual service requests. Wallet payments and multi-method checkout reduce friction

SEGMENT 4: ProConnect On-Demand (35 markets, growing)
  Current: On-demand home repair marketplace
  Gap: Consumer expectations for modern checkout (Apple Pay, BNPL) in on-demand services
  Opportunity: ProConnect competes with Thumbtack, Angi. Modern payment UX is table stakes

SEGMENT 5: Contractor Payouts (17,000 firms)
  Current: Direct deposit
  Gap: No unified visibility across consumer collections and contractor disbursements
  Opportunity: Orchestration layer connects both sides of the marketplace payment flow

**Key meeting angles:**
1. **$2.1B revenue, Stripe-confirmed** | Stripe is the primary PSP. Frontdoor already engaged Stripe Professional Services for auth optimization but achieved only 1.84% improvement. Multi-processor routing unlocks additional uplift
2. **76% renewal revenue at risk** | Three-quarters of revenue comes from auto-renewing warranties. Card decay, expiration, and failed charges create past-due invoices. Intelligent retry and failover protect recurring revenue at scale
3. **Post-acquisition billing consolidation** | $585M acquisition of 2-10 HBW (Dec 2024) added a 5th warranty brand. No orchestration layer to unify billing across AHS, HSA, OneGuard, Landmark, and 2-10 HBW
4. **2.1M members, no Apple Pay** | Mobile-first home warranty members manage everything from the AHS app. No Apple Pay, Google Pay, or wallet payments native to the app. Consumer expectations for modern checkout are unmet
5. **3.8M service requests annually** | Each request triggers a $100+ service fee charge to the card on file. Failed service fee charges delay contractor dispatch and damage member satisfaction
6. **ProConnect marketplace expansion** | On-demand home services in 35 markets competing with Thumbtack and Angi. Modern payment experience (wallets, BNPL) is table stakes for on-demand marketplaces
7. **Contractor payout complexity** | 17,000 firms receiving payouts for 3.8M service requests. Unified orchestration connects consumer premium/fee collection with contractor disbursement

**Sources:**
- [Stripe: Frontdoor Professional Services Case Study](https://stripe.com/customers/frontdoor-professional-services)
- [Frontdoor: Record Full-Year 2025 Financial Results](https://www.businesswire.com/news/home/20260226042868/en/Frontdoor-Announces-Record-Full-Year-2025-Financial-Results)
- [Frontdoor: 10-K Annual Report 2025](https://www.stocktitan.net/sec-filings/FTDR/10-k-frontdoor-inc-files-annual-report-3f9879ae43b7.html)
- [Frontdoor: 2-10 HBW Acquisition Completion](https://www.businesswire.com/news/home/20241219129865/en/Frontdoor-Inc.-Completes-Acquisition-of-2-10-Home-Buyers-Warranty)
- [Frontdoor: ProConnect Expansion to 35 Markets](https://www.nasdaq.com/press-release/frontdoor-expands-on-demand-home-services-to-35-markets-with-american-home-shield)
- [Frontdoor: Streem Acquisition](https://www.businesswire.com/news/home/20191205005459/en/Frontdoor-Acquires-Streem-Leader-Advanced-Technology-Transform)
- [Frontdoor: Moen Partnership](https://www.businesswire.com/news/home/20240625770671/en/Frontdoor-Inc.-Signs-Exclusive-Agreement-With-Moen)
- [AHS: SkySlope Technology Partnership](https://www.rismedia.com/2026/04/16/ahs-expandstech-partnership-skyslope/)
- [AHS: FAQs](https://www.ahs.com/faqs/)
- [AHS: Supplier Support](https://www.ahs.com/suppliers/)
- [MacroTrends: Frontdoor Revenue](https://www.macrotrends.net/stocks/charts/FTDR/frontdoor/revenue)
- [MacroTrends: Frontdoor Employees](https://www.macrotrends.net/stocks/charts/FTDR/frontdoor/number-of-employees)
- [Seeking Alpha: Frontdoor Q4 2025 Earnings Transcript](https://seekingalpha.com/article/4875500-frontdoor-inc-ftdr-q4-2025-earnings-call-transcript)
- [BBB: American Home Shield Complaints](https://www.bbb.org/us/tn/memphis/profile/home-warranty-plans/american-home-shield-0543-22001027/complaints)
- [PissedConsumer: American Home Shield Reviews](https://american-home-shield.pissedconsumer.com/review.html)
- [Brandfetch: Frontdoor Logo](https://brandfetch.com/frontdoor.com)
- [Frontdoor: Investor Relations](https://investors.frontdoorhome.com/)
