# JOBBER | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Jobber
=======================================

Logo: https://cdn.brandfetch.io/getjobber.com/w/512/h/512/theme/dark/icon.jpeg
Nombre merchant: Jobber

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Stripe Single PSP Lock-In
Tittle_Pain Point_2: US/Canada Payment Ceiling
Tittle_Pain Point_3: No BNPL for Large Jobs
Tittle_Pain Point_4: ACH US-Only Limitation
Tittle_Pain Point_5: No Smart Routing Layer

Desc_Pain Point_1: Jobber Payments is powered entirely by Stripe with no failover processor. All 300,000+ service professionals depend on a single PSP for credit card processing, instant payouts, and Stripe Capital financing. If Stripe experiences downtime or declines a transaction, there is no cascade to an alternative acquirer. On $167.5M+ annual revenue with growing payment volume, single-PSP dependency creates concentration risk.
Desc_Pain Point_2: Jobber operates in the US, Canada, and UK but payment infrastructure remains heavily US-centric. ACH bank payments are US-only. Tap to Pay and card reader features support Visa, Mastercard, and Amex but lack local payment methods for UK (Open Banking), Canadian (Interac), and international expansion markets. 60+ countries use Jobber with limited payment localization.
Desc_Pain Point_3: Home service jobs range from $200 lawn care to $15,000+ HVAC installations and renovations. No BNPL option exists for homeowners who need to finance large jobs. Service professionals lose high-value jobs when clients cannot afford full upfront payment. Klarna, Affirm, or Afterpay integration would increase average job value and conversion on premium services.
Desc_Pain Point_4: ACH bank payments charge only 1% versus 2.9% + $0.30 for credit cards, saving service professionals significant processing fees. But ACH is limited to the US market only with 7 business day settlement times. Canadian and UK users have no bank transfer option. No SEPA for European expansion. No real-time bank payment alternatives like FedNow or Open Banking.
Desc_Pain Point_5: Despite processing payments for 300,000+ service professionals, Jobber has no intelligent routing layer. Every transaction follows the same path through Stripe regardless of card issuer, BIN, geography, or decline history. No ability to route to alternative acquirers for higher approval rates. Square and Authorize.net integrations exist but cannot run simultaneously with Jobber Payments.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (primary, powers Jobber Payments)
PSP_2: Square (alternative integration)
PSP_3: Authorize.net (alternative integration)
PSP_4: Stripe Capital (embedded financing)
PSP_5: Visa Direct (instant payouts)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Interac (Canada)
Local_M_2: Open Banking (UK)
Local_M_3: Klarna (BNPL)
Local_M_4: Affirm (BNPL)
Local_M_5: PayPal
Local_M_6: SEPA Direct Debit
Local_M_7: iDEAL
Local_M_8: Afterpay
Local_M_9: Clearpay (UK)
Local_M_10: Pix

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Recovery
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across Stripe, Square, and Authorize.net for every invoice payment, in-field collection, and online checkout. Each transaction routed to the highest performing acquirer for that card BIN, issuer, and market. Across 300,000+ service professionals processing payments in US, Canada, and UK, smart routing delivers +3 to 10% auth uplift. On a $15,000 HVAC job, recovering a declined payment saves the entire sale.
Desc_Yuno_Cap2: Automatic cascade across Jobber's three payment integrations eliminates single-Stripe dependency. When Stripe declines, Yuno reroutes to Square or Authorize.net in milliseconds. Up to 50% recovery on soft declines via instant retry. NOVA AI recovers up to 75% of failed transactions. For field service professionals collecting payment at the job site, a decline means awkward client interactions and delayed cash flow.
Desc_Yuno_Cap3: Activates the APMs Jobber needs for market expansion: Interac for Canadian service professionals, Open Banking and Clearpay for UK users, Klarna and Affirm for BNPL on large home service jobs ($5K-$15K+ HVAC, roofing, renovations), PayPal for homeowner convenience, SEPA for European expansion. One API, 1,000+ payment methods across all Jobber markets.
Desc_Yuno_Cap4: One dashboard replacing Jobber's fragmented Stripe + Square + Authorize.net options with unified real-time visibility. Centralized approval rate monitoring across 300,000+ service professionals in 60+ countries, automated reconciliation for instant payouts and standard settlements, and millisecond anomaly detection via Monitors. Enables Jobber to scale payments internationally without building per-market PSP integrations.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Jobber at a glance:**
- Model: Field service management SaaS (scheduling, invoicing, CRM, payments)
- Industry: Home services technology
- Users: 300,000+ service professionals
- Customers: 100,000+ businesses
- Properties served: 27M+
- Industries: 50+ (landscaping, HVAC, cleaning, plumbing, carpentry, electrical)
- Countries: 60+ (primary: US 82%, Canada 12%, UK 3%)
- Employees: 1,267
- Headquarters: Edmonton, Alberta, Canada (Mercer Warehouse)
- Founded: 2011
- CEO & Co-founder: Sam Pillar
- CTO & Co-founder: Forrest Zeisler
- CRO: Shawn Chadeau
- CMO: Julie Haddon
- CPO: Sara Cooper
- Revenue: $167.5M (2024), up from $143.2M (2023), $100M (2022)
- Revenue growth: ~17% YoY (2024)
- Total funding: $191M over 6 rounds
- Valuation: $300-400M (2021 estimate)
- Key investors: General Atlantic (led $100M Series D, Feb 2023), OMERS Ventures, Summit Partners, Version One Ventures, Point Nine
- Pricing: $29-$149/month

**Core Products:**
- Jobber Core: Scheduling, dispatching, route optimization, CRM, quoting, invoicing
- Jobber Payments: Stripe-powered credit card processing (online + in-field)
- Jobber Money: Embedded financial account with Visa debit card
- Jobber Capital: Stripe Capital-powered business financing
- AI Receptionist: 24/7 call/text answering (launched Aug 2025)
- Marketing Suite: AI-powered marketing tools
- Jobber Copilot: AI recommendations and insights

**Recent Developments:**
- 2026: Jobber Now event (route optimization, AI Marketing Suite, website builder, AI receptionist chat widget)
- January 2026: Offline mode for job forms and time tracking
- August 2025: AI Receptionist launch
- Hundreds of millions in lifetime Stripe Capital financing originations
- 100% increase in Capital originations after embedded promotional cards

**Payments Infrastructure:**
- Stripe: Primary payment processor powering all Jobber Payments
- Stripe Connect: Platform-level payment processing for service professionals
- Stripe Capital: Embedded business financing
- Visa Direct: Instant payouts (funds in seconds, 1% fee)
- Square: Alternative payment integration (cannot run simultaneously with Jobber Payments)
- Authorize.net: Alternative payment integration (cannot run simultaneously)
- Only one payment integration can be active at a time

**Payment Methods (Current):**
- Credit/debit cards: Visa, Mastercard, Amex, Discover
- Apple Pay (via Tap to Pay and client hub)
- Google Pay (via Tap to Pay and client hub)
- Samsung Pay (via Tap to Pay)
- ACH bank payments (US only, 1% fee, 7 business day settlement)
- Tap to Pay on smartphone (contactless, no hardware needed)
- Jobber card reader (swipe, tap, chip; lower fees for card-present)
- No PayPal
- No BNPL
- No international bank transfers
- No local payment methods

**Processing Fees:**
- Credit card: 2.9% + $0.30 per transaction
- ACH: 1% per transaction (US only)
- Instant payouts: 1% fee
- Card reader (card-present): Lower than standard credit card rate

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (82% of users, primary market)
  Currently offer: Visa/MC/Amex/Discover, Apple Pay, Google Pay, ACH
  Missing: PayPal, Klarna, Affirm, Afterpay, Venmo
  No BNPL for large home service jobs ($5K-$15K+). BNPL increases conversion 20-40% on premium services.

MARKET 2: Canada (12% of users, headquarters market)
  Currently offer: Visa/MC/Amex, Apple Pay, Google Pay
  Missing: Interac (dominant Canadian debit network), Interac e-Transfer, ACH equivalent
  Interac is used by 90%+ of Canadians. No bank transfer option for Canadian users (ACH is US-only).

MARKET 3: United Kingdom (3% of users, growing market)
  Currently offer: Visa/MC/Amex, Apple Pay, Google Pay
  Missing: Open Banking, Clearpay (Afterpay UK), PayPal, Direct Debit
  UK homeowners expect Open Banking and PayPal. No BNPL for large trade jobs.

MARKET 4: Australia/New Zealand (emerging market)
  Currently offer: Visa/MC via Stripe
  Missing: Afterpay (dominant BNPL), BPAY, POLi, bank transfers
  Afterpay originated in Australia and is the default BNPL for trades. Zero local APM support.

MARKET 5: Europe (expansion opportunity)
  Currently offer: Visa/MC via Stripe
  Missing: SEPA Direct Debit, iDEAL, Bancontact, Klarna, Giropay
  European home service markets are large but require local payment methods. No SEPA for recurring billing.

**Payment Pain Points:**
1. Single Stripe dependency for all payment processing with no failover
2. Only one payment integration can be active at a time (no multi-PSP)
3. ACH bank payments limited to US only (1% fee vs 2.9% card)
4. No BNPL for large home service jobs ($5K-$15K+ HVAC, roofing)
5. No Interac for Canadian users (90%+ Canadian debit usage)
6. No Open Banking for UK market
7. No PayPal despite being homeowner preferred payment method
8. 7 business day ACH settlement delays cash flow
9. No smart routing across processors to optimize approval rates
10. 60+ countries using Jobber with US-centric payment infrastructure

**Key Meeting Angles:**
1. **300,000+ users, single PSP**: Jobber Payments runs entirely on Stripe. Yuno adds failover to Square and Authorize.net, enabling multi-PSP routing without disrupting the Stripe relationship
2. **BNPL for premium services**: HVAC, roofing, and renovation jobs ($5K-$15K+) need financing. Klarna and Affirm via Yuno increase conversion and average job value. No current BNPL option exists
3. **Canadian market gap**: 12% of users are in Canada but have no Interac or bank transfer option. Yuno enables Interac alongside card payments via single API
4. **UK expansion**: 3% and growing. Open Banking, Clearpay, and PayPal are essential for UK homeowners. Yuno provides local APMs as Jobber scales internationally
5. **Stripe Capital relationship**: Jobber has deep Stripe partnership (Capital, Connect, Visa Direct). Yuno orchestrates alongside Stripe without replacing it. McDonald's gained +4.7% auth rate with Yuno while keeping existing PSPs
6. **Revenue at scale**: $167.5M revenue, 17% growth. Even 1% auth rate improvement on growing payment volume recovers significant revenue. InDrive achieved 90% approval across 10 markets with Yuno

**Sources:**
- [Jobber](https://www.getjobber.com/)
- [Jobber Payments](https://www.getjobber.com/features/field-service-credit-card-processing/)
- [Jobber Payment Integrations](https://help.getjobber.com/hc/en-us/articles/115009787248-Payment-Integrations)
- [Jobber Payments Basics](https://help.getjobber.com/hc/en-us/articles/115009571387-Jobber-Payments-Basics)
- [Jobber ACH](https://help.getjobber.com/hc/en-us/articles/1500004781762-Bank-Payments-ACH)
- [Jobber Tap to Pay](https://help.getjobber.com/hc/en-us/articles/34647042014615-Tap-to-Pay)
- [Jobber Card Reader](https://help.getjobber.com/hc/en-us/articles/360036932273-Jobber-Card-Reader)
- [Jobber Money](https://help.getjobber.com/hc/en-us/articles/12946420294807-Jobber-Money)
- [Stripe + Jobber Partnership](https://stripe.com/newsroom/news/jobber)
- [Stripe Customer: Jobber](https://stripe.com/customers/jobber)
- [Jobber Series D (PRNewswire)](https://www.prnewswire.com/news-releases/jobber-raises-100-million-growth-round-301739689.html)
- [Jobber Series D (BetaKit)](https://betakit.com/jobber-closes-100-million-usd-series-d-amid-strong-demand-for-home-services/)
- [Jobber Revenue (Latka)](https://getlatka.com/companies/jobber)
- [Jobber Revenue (Sacra)](https://sacra.com/c/jobber/)
- [Jobber Home Service Report 2025](https://www.getjobber.com/home-service-reports/feb-2025/)
- [Crunchbase: Jobber](https://www.crunchbase.com/organization/jobber)
- [CB Insights: Jobber](https://www.cbinsights.com/company/octopusapp)
