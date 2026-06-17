# GROW THERAPY | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Grow Therapy
═══════════════════════════════════════

Logo: https://asset.brandfetch.io/id0qMNb3wP/idwCXxKdpV.svg
Nombre merchant: Grow Therapy

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Stripe-Only Processing
Tittle_Pain Point_2: Overcharge & Duplicate Fees
Tittle_Pain Point_3: Delayed Copay Billing
Tittle_Pain Point_4: No Payment Alternatives
Tittle_Pain Point_5: Provider Payout Friction

Desc_Pain Point_1: Stripe is the sole payment processor for all client charges and provider payouts across 26,000+ therapists and 7M+ annual visits. Any Stripe outage or rate dip blocks copay collection, cash-pay sessions, and therapist direct deposits simultaneously.
Desc_Pain Point_2: BBB complaints document clients being overcharged or charged multiple times for the same session. With $1B+ in annual revenue flowing through a single processor, duplicate charge errors create billing disputes that damage patient trust and increase support load.
Desc_Pain Point_3: Insurance adjudication delays convert expected $10 copays into larger surprise balances weeks after sessions. Automatic card charges for adjusted amounts trigger disputes and chargebacks when clients do not recognize the delayed, higher-than-expected charge.
Desc_Pain Point_4: Grow Therapy accepts only credit/debit cards (including HSA/FSA cards) through Stripe. No PayPal, no Apple Pay, no Google Pay, no ACH direct debit. Clients paying $150+ per cash-pay session or large deductibles have limited payment flexibility.
Desc_Pain Point_5: 26,000+ providers connect individual Stripe accounts to receive weekly direct deposit payouts. Any Stripe Connect disruption delays therapist earnings, and providers report lack of transparency around payment timing and amounts.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (client charges)
PSP_2: Stripe Connect (provider payouts)
PSP_3: Insurance Claims (125+ plans)
PSP_4: HSA/FSA Cards (via Stripe)
PSP_5: N/A

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: PayPal
Local_M_2: Apple Pay
Local_M_3: Google Pay
Local_M_4: ACH Direct Debit
Local_M_5: Venmo
Local_M_6: Cash App Pay
Local_M_7: Affirm
Local_M_8: Klarna
Local_M_9: Afterpay
Local_M_10: Pay by Bank (Open Banking)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route every copay, deductible, and cash-pay charge to the best performing acquirer by card BIN, issuing bank, and charge amount. With $1B+ in annual revenue and 7M+ sessions, a 3% auth uplift recovers millions in copays and self-pay charges that would otherwise fail.
Desc_Yuno_Cap2: When a client's card declines for a copay or session charge, Yuno cascades to an alternate acquirer in milliseconds. Recovers up to 50% of failed charges automatically, eliminating the duplicate charge errors and manual follow-up cycles documented in BBB complaints.
Desc_Yuno_Cap3: Adds the payment flexibility Grow Therapy's 220M covered lives need: PayPal and Venmo for clients preferring wallet payments, Apple Pay and Google Pay for mobile-first checkout, ACH Direct Debit for large deductibles, Affirm/Klarna for cash-pay clients spreading $150+ session costs. One API, 1,000+ methods.
Desc_Yuno_Cap4: Single dashboard consolidating client copay charges, cash-pay billing, insurance claim reconciliation, provider Stripe Connect payouts, and HSA/FSA card processing into one view. Real-time auth monitoring, anomaly detection via NOVA, and centralized reconciliation across 125+ insurance partners.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Grow Therapy at a glance:**
- Founded: 2020
- CEO/Co-Founder: Jake Cooper
- Headquarters: New York City, NY
- Employees: ~2,745 (as of January 2026)
- Total funding: $328M across multiple rounds (Series A $30M, Series B $75M, Series C $88M, Series D $150M)
- Series D: $150M (March 2026) led by TCV and Growth Equity at Goldman Sachs Alternatives
- Valuation: $3B (Series D, March 2026)
- Key investors: TCV, Goldman Sachs, Sequoia, SignalFire, Transformation Capital, BCI, Menlo Ventures
- Revenue: $1B+ annual run rate (2025)
- Annual therapy visits: 7M+ (2025)
- Active providers: 26,000+ therapists and psychiatrists
- Insurance partners: 125+ health plans (up from 75), including Medicare and Medicaid in most states
- Lives covered: ~220M in the US
- Products: Therapy marketplace, EHR software, AI clinical notetaker, Care Coordination program, enterprise EAP integration
- AI notetaker: reduces documentation time by 70%; 80% of clients show measurable symptom improvement within 30 days
- Acquisition: Neosync (data privacy company, September 2025)
- Market: US only; $4.39B online therapy services market (2025) projected to reach $14.1B by 2034
- Enterprise: companies can offer Grow Therapy through redesigned mental health benefit program (March 2026)

**Confirmed PSPs:**
- Stripe: sole payment processor for all client charges (copays, deductibles, cash-pay sessions)
- Stripe Connect: provider payout platform (26,000+ individual connected accounts)
- HSA/FSA cards: accepted as debit cards through Stripe
- Insurance claims: 125+ health plan partnerships (separate from payment processing)
- Credit/debit cards: required on file for all clients (except Kaiser/Medicaid)
- Automatic card updater: Stripe partnership auto-updates expired cards from same bank
- No payment orchestrator detected
- No digital wallets detected (no Apple Pay, Google Pay, PayPal)
- No ACH/bank transfer option for clients

**Payment issues documented:**
- BBB complaints: overcharges and duplicate charges reported by multiple clients
- Delayed insurance adjudication: expected $10 copays convert to larger surprise balances weeks later
- No-show/late cancellation fee: up to $200, not covered by insurance, auto-charged to card
- No phone support: all billing inquiries handled via messaging/chat (often bot-answered)
- Provider transparency: providers report lack of clarity on payment timing and amounts
- Trustpilot: 4.8/5 overall (5,000+ reviews), but billing complaints are the most common negative theme
- Resolution: most BBB complaints eventually resolved, but process is slow

**Key meeting angles:**
1. **$1B+ revenue, single processor**: Every dollar of revenue flows through Stripe. At this scale, even 1% of failed charges = $10M+ in at-risk revenue annually
2. **26,000+ provider payouts**: Stripe Connect manages individual accounts for every therapist. Any disruption delays earnings for the entire provider network
3. **Duplicate charge crisis**: BBB-documented overcharge/duplicate issues would be caught and prevented by Yuno's intelligent routing and anomaly detection
4. **Cash-pay opportunity**: $150+/session cash-pay clients need BNPL options (Affirm, Klarna) and digital wallets to reduce payment friction
5. **Insurance complexity**: Delayed adjudication creates surprise charges; better payment orchestration can smooth the billing experience and reduce disputes
6. **Enterprise expansion**: Companies offering Grow Therapy as a benefit need enterprise-grade payment infrastructure with multi-processor resilience

**Sources:**
- [Grow Therapy Official Website](https://growtherapy.com/)
- [Grow Therapy Series D Announcement](https://growtherapy.com/blog/series-d/)
- [Grow Therapy $1B Revenue, $150M Series D (BHB)](https://bhbusiness.com/2026/03/03/with-1b-in-revenue-grow-therapy-lands-150m-series-d/)
- [Grow Therapy $3B Valuation (Bloomberg)](https://www.bloomberg.com/news/articles/2026-03-03/mental-health-startup-grow-therapy-hits-3-billion-valuation)
- [Grow Therapy Connect Stripe Account (Help Center)](https://help.growtherapy.com/en/articles/5598970-connect-a-stripe-account)
- [Grow Therapy Payout & Earnings FAQ](https://help.growtherapy.com/en/articles/5574668-payout-earnings-faq)
- [Grow Therapy Authorized Charging Practices](https://help.growtherapy.com/clients/en/articles/9740949-authorized-charging-practices)
- [Grow Therapy Session Payment and Refunds](https://help.growtherapy.com/en/articles/11066672-session-payment-and-refunds)
- [Grow Therapy Update Billing Information](https://help.growtherapy.com/clients/en/articles/8012232-update-your-billing-information)
- [Grow Therapy HSA/FSA/EAP Coverage](https://growtherapy.com/therapy-basics/paying-for-therapy/hsa-fsa-eap-coverage/)
- [Grow Therapy Insurance Coverage](https://growtherapy.com/therapy-basics/paying-for-therapy/insurance-coverage/)
- [Grow Therapy BBB Complaints](https://www.bbb.org/us/ny/new-york/profile/medical-business-administration/grow-therapy-0121-87145848/complaints)
- [Grow Therapy Trustpilot Reviews](https://www.trustpilot.com/review/www.growtherapy.com)
- [Grow Therapy Review (Choosing Therapy)](https://www.choosingtherapy.com/grow-therapy-review/)
- [Grow Therapy Review (Healthline)](https://www.healthline.com/health/grow-therapy)
- [Grow Therapy PRNewswire Series D](https://www.prnewswire.com/news-releases/grow-therapy-raises-150-million-in-series-d-as-it-solidifies-new-flagship-partnerships-302702388.html)
- [Grow Therapy Tracxn](https://tracxn.com/d/companies/grow-therapy/__Jgzd-gCt4roTSkuUCfH-arN4r01bA3I89mxZSKM-dlA)
- [Grow Therapy Logo (Brandfetch)](https://brandfetch.com/growtherapy.co)
