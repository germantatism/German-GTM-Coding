# GOODLEAP | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: GoodLeap
═══════════════════════════════════════

Logo: https://asset.brandfetch.io/id2S3eDSiG/idYmtbM1Qd.svg
Nombre merchant: GoodLeap

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Single Acquirer Lock-In
Tittle_Pain Point_2: Contractor Payout Delays
Tittle_Pain Point_3: Duplicate Payment Errors
Tittle_Pain Point_4: ACH Failure Recovery Gap
Tittle_Pain Point_5: No Payment Orchestration

Desc_Pain Point_1: Stripe is the sole card acquirer for GoodLeap Payments. Any Stripe outage or rate dip blocks all credit card, Apple Pay, Google Pay, and Samsung Pay transactions across the entire contractor payment platform with zero fallback processor.
Desc_Pain Point_2: 69% of contractors still rely on paper checks. GoodLeap Payments was built to fix this, but routing all digital payments through a single processor creates bottleneck risk for the 1M+ homeowner loans and contractor disbursements the platform supports.
Desc_Pain Point_3: GoodLeap's own support confirms recurring duplicate payment issues in the borrower app. Customer service tells affected users refunds take up to 30 days, creating cash flow disruption and trust erosion among homeowners making $200+/month loan payments.
Desc_Pain Point_4: ACH and eCheck payments flow through a single processing path. When bank returns or NSF events occur on loan repayments, there is no automated cascade to retry via an alternate rail, leaking recoverable revenue on a $32B+ loan portfolio.
Desc_Pain Point_5: GoodLeap manages contractor payments (Stripe), loan servicing (ACH), and homeowner billing across disconnected systems. No unified orchestration layer connects card payments, ACH transfers, and eCheck processing into a single real-time view.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe
PSP_2: ACH (Direct Bank)
PSP_3: Apple Pay
PSP_4: Google Pay
PSP_5: Samsung Pay

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Venmo
Local_M_2: Cash App Pay
Local_M_3: PayPal
Local_M_4: Zelle
Local_M_5: Affirm
Local_M_6: Klarna
Local_M_7: Afterpay
Local_M_8: RTP (Real-Time Payments)
Local_M_9: FedNow
Local_M_10: Pay by Bank (Open Banking)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route every contractor payment, loan disbursement, and homeowner billing charge to the best performing acquirer by card BIN, bank, and transaction type. With $361M+ revenue and $32B+ loans originated, a 3% auth uplift on card transactions recovers significant revenue without touching checkout UX.
Desc_Yuno_Cap2: When Stripe declines a contractor payment or homeowner card charge, Yuno cascades to an alternate acquirer in milliseconds. Recovers up to 50% of failed charges, directly reducing the duplicate payment errors and 30-day refund cycles that frustrate GoodLeap users today.
Desc_Yuno_Cap3: Adds the payment methods GoodLeap's contractor and homeowner base demands: Venmo, Cash App Pay, PayPal, and Pay by Bank for homeowners; instant RTP and FedNow rails for contractor disbursements. One API, 1,000+ payment methods, zero engineering sprints per method.
Desc_Yuno_Cap4: Single dashboard consolidating Stripe card processing, ACH loan servicing, Apple Pay, Google Pay, Samsung Pay, and eCheck into one view. Real-time auth rate monitoring across every processor and payment rail, centralized reconciliation, and millisecond anomaly detection via NOVA.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**GoodLeap at a glance:**
- Founded: 2018 (originally as Loanpal, rebranded to GoodLeap in 2021)
- CEO/Founder: Hayes Barnard
- Headquarters: Roseville, CA (additional offices in San Francisco, Irvine, Phoenix, Kansas City, Bentonville)
- Valuation: $12B (at peak 2021 funding); current valuation estimated lower
- Total funding raised: $1.1B+ across multiple rounds (latest: $800M Growth Equity II, October 2021)
- Key investors: Mubadala Investment Company, Riverstone Energy, Brookfield Growth, Davidson Kempner Capital Management
- Revenue: ~$361M in 2025 (down from ~$500M peak in 2024)
- Employees: ~1,235 (as of January 2026)
- Loans originated: $32B+ since 2018, serving 1M+ homeowners across 50 states
- Products: Solar loans (Standard, Flexpay, Go Green Refi), home improvement loans, GoodLeap Payments (contractor payment platform), GoodGrid (virtual power plant)
- Loan terms: 5 to 25 years, APR 4.99% to 8.99%, minimum credit score 600
- Market: US only, $450B+ annual sustainable home upgrade market
- Securitizations: 24 completed totaling $909M+ in 2025 alone ($386M Feb, $523M Dec)
- Recognition: Fortune 2025 Change the World List
- Nonprofit arm: GivePower (clean water/electricity in Africa, Asia, South America)

**Confirmed PSPs:**
- Stripe: primary card acquirer for GoodLeap Payments contractor platform (confirmed via job listings: "integrated with Stripe and other payment gateways")
- ACH: direct bank transfers for homeowner loan repayments and contractor disbursements
- Apple Pay / Google Pay / Samsung Pay: digital wallet options on GoodLeap Payments
- eCheck: electronic check scanning for contractor payments
- QuickBooks: accounting integration (not a PSP but key financial system)
- No payment orchestrator detected
- No international payment methods detected (US-only operations)

**Payment issues documented:**
- BBB: 1,076 complaints in last 3 years; 443 closed in last 12 months alone
- Complaint breakdown: order problems (346), service/repair issues (297), billing disputes (229)
- Duplicate payments: app has recurring issue processing duplicate payments; refunds take up to 30 days
- Late payment penalties: customer reported $179.05 interest charge for payment allegedly one day late
- Declined payments: users must verify funds and contact their bank to authorize payments
- Portal access issues: login and connectivity problems with online payment portal
- One customer reported accidentally making 10 payments; company refused full refund
- WalletHub rating: mixed reviews across 286 user ratings
- PissedConsumer: multiple complaints about billing and customer service

**Technology stack:**
- Full-stack: Node.js, TypeScript, NestJS, React, HTML, CSS, Flutter
- Infrastructure: AWS cloud, PostgreSQL, microservices architecture
- Integrations: Stripe API, QuickBooks, RESTful APIs
- Mobile: tap-to-pay on existing devices, no additional hardware required

**Key meeting angles:**
1. **Contractor payment modernization**: 69% of contractors still use paper checks; GoodLeap Payments needs resilient multi-processor infrastructure to drive adoption
2. **Duplicate payment crisis**: App-level duplicate payment bugs compound when there is no orchestration layer to detect and prevent double charges
3. **$32B loan portfolio protection**: ACH-only loan servicing with no automated retry/cascade means every failed bank debit is a manual recovery effort
4. **Scale demands orchestration**: 1M+ homeowners, thousands of contractors, $361M revenue. Single-acquirer architecture does not match this scale
5. **BNPL opportunity**: Home improvement loans at 5-9% APR compete with Affirm/Klarna at checkout; adding BNPL options could capture price-sensitive homeowners
6. **Real-time payments**: FedNow and RTP rails could eliminate the contractor payout delays that GoodLeap Payments was built to solve

**Sources:**
- [GoodLeap Wikipedia](https://en.wikipedia.org/wiki/GoodLeap)
- [GoodLeap Launches Next-Generation Payment Solution (PRNewswire)](https://www.prnewswire.com/news-releases/goodleap-launches-next-generation-payment-solution-to-modernize-how-contractors-get-paid-302471371.html)
- [GoodLeap Introduces Payments Product for Contractors (PYMNTS)](https://www.pymnts.com/news/payments-innovation/2025/goodleap-introduces-payments-product-for-contractors/)
- [GoodLeap BBB Complaints](https://www.bbb.org/us/ca/roseville/profile/construction-loans/goodleap-llc-1156-33013909/complaints)
- [GoodLeap Bill Payment Methods](https://cms.nucleusnetwork.com/urban-beat/goodleap-bill-payment-phone-number-and-easy-methods-1767647234)
- [GoodLeap Solar Loan Review (SolarReviews)](https://www.solarreviews.com/blog/goodleap-solar-loans)
- [GoodLeap Revenue (Sacra)](https://sacra.com/research/goodleap)
- [GoodLeap $523M Securitization (Fintech Global)](https://fintech.global/2025/12/15/goodleap-closes-523m-home-improvement-solutions-trust-2025-3/)
- [GoodLeap Fortune Change the World List](https://www.goodleap.com/press-releases/goodleap-named-to-fortunes-2025-change-the-world-list)
- [GoodLeap Tracxn Profile](https://tracxn.com/d/companies/goodleap/__RJuv95j0hblOOa_7Akg_ndozJnGr3dymZBKV-_Oyd8Y)
- [GoodLeap Staff Engineer Job (Payment Stack)](https://jobs.lever.co/goodleap/d54353d8-3f47-4fa3-9906-48af23432340)
- [GoodLeap Logo (Brandfetch)](https://brandfetch.com/goodleap.com)
- [GoodLeap PissedConsumer Reviews](https://goodleap.pissedconsumer.com/review.html)
- [GoodLeap Charge Identifier (Slash)](https://www.slash.com/charge-identifier/goodleap)
