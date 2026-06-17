# FLEXPAY (REVALY) | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: FlexPay (Revaly)
═══════════════════════════════════════

Logo: https://brandfetch.com/flexpay.io
Nombre merchant: FlexPay (Revaly)

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: 39% Generic Declines
Tittle_Pain Point_2: Single-Gateway Recovery
Tittle_Pain Point_3: No Pre-Auth Optimization
Tittle_Pain Point_4: Limited APM Retries
Tittle_Pain Point_5: Fragmented PSP Data

Desc_Pain Point_1: 39% of failed subscriptions return "generic decline" with no actionable reason. Revaly must guess the cause. Multi-acquirer routing surfaces clearer data.
Desc_Pain Point_2: Retries go through the same gateway that declined. Without multi-PSP failover, soft declines one acquirer rejects could pass elsewhere. 50% recoverable.
Desc_Pain Point_3: Revaly intervenes after auth fails. No pre-auth BIN routing or issuer optimization before the first attempt. Prevention is cheaper than recovery.
Desc_Pain Point_4: When card recovery fails, only card rails are retried. No fallback to ACH, wallets, or BNPL for recurring billing. 27% of subscribers cancel after a failure.
Desc_Pain Point_5: 115+ gateways send different decline codes and metadata. No unified layer normalizes data across PSPs to identify systemic patterns across the portfolio.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (gateway integration)
PSP_2: Adyen (gateway integration)
PSP_3: Checkout.com (gateway integration)
PSP_4: PayPal (gateway integration)
PSP_5: Authorize.Net (gateway integration)
PSP_6: Worldpay (gateway integration)
PSP_7: USA ePay (gateway integration)
PSP_8: Chase (gateway integration)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: ACH Direct Debit
Local_M_2: SEPA Direct Debit
Local_M_3: iDEAL
Local_M_4: Bancontact
Local_M_5: BLIK
Local_M_6: PayPal Recurring
Local_M_7: Apple Pay Recurring
Local_M_8: Google Pay Recurring
Local_M_9: Boleto Recorrente
Local_M_10: UPI Autopay

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across 8+ gateways before the first auth attempt. Instead of declining and recovering, Smart Routing sends each charge to the highest-approval acquirer for that BIN and issuer. 3-10% uplift means fewer declines to recover.
Desc_Yuno_Cap2: Automatic cascade across processors when the primary gateway declines. Yuno reroutes to Adyen, Checkout.com, or Worldpay in milliseconds. Up to 50% recovery on soft declines, complementing Revaly's AI with multi-rail routing.
Desc_Yuno_Cap3: When card recovery fails, Yuno activates non-card rails for recurring billing: ACH Direct Debit, SEPA, iDEAL, BLIK, Apple Pay recurring, Google Pay recurring, UPI Autopay. One API, 1,000+ methods. Converts the 27% of subscribers who would otherwise cancel after a card failure.
Desc_Yuno_Cap4: One dashboard normalizing decline data across 115+ gateways. Real-time approval rates per PSP, per decline reason, per merchant. Centralized analytics replace fragmented reporting. NOVA (75% fraud reduction) flags suspicious retries.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**FlexPay (Revaly) at a glance:**
- Founded: 2016 (originally as FlexPay). Rebranded to Revaly in November 2025
- HQ: Montreal, Quebec, Canada (4238 Boulevard Saint-Laurent)
- Founder & CEO: Darryl Hicks
- Total funding: $4.53M (Seed round investors: Anges Quebec, BMO Capital Partners, Impression Ventures). Additional $5M Seed round in October 2023
- Employees: ~37 (estimated based on LinkedIn/similar company data)
- PCI DSS Level 1 compliant
- Integrates with 115+ payment gateways and 16+ billing/CRM platforms
- Revenue model: Revenue share on recovered payments
- Key clients: LegalZoom, Young Living, TrulyFree, Special Olympics, Hooked on Phonics, ClinicSense

**Why the rebrand:**
- "We spent nine years perfecting recovery, but kept seeing the same preventable declines over and over" (Darryl Hicks, CEO)
- Expanded from post-decline recovery to full payment lifecycle: pre-authorization optimization, real-time payment intelligence, and customer engagement
- Launched "Payment Performance Management" as a new category

**Confirmed Payment Stack / Integrations:**

Billing & CRM Integrations:
- Recurly, Chargebee, Zuora, Stripe Billing, Recharge, Maxio, Aria, Evergent, OrderGrove, AdvantageCS, ROI Solutions, Sticky IO, Response CRM, Sublytics, By Design, Fosdick

Payment Gateway Integrations:
- Stripe, Adyen, Checkout.com, PayPal, Authorize.Net, Shopify, USA ePay, Worldpay, Chase, FIS, and 100+ more

Partnership: FlexPay and Spreedly expanded partnership for failed payment recovery

**Products:**
1. Invisible Recovery: AI-powered recovery working directly with payment systems. Customer never knows their payment was declined. Recovers most failed payments quickly
2. Engaged Recovery: Behavioral science-driven customer engagement when automated recovery fails. Persuades customers to update payment info and keep subscriptions active

**Performance Metrics:**
- Recovers up to 75% of failed payments
- Extends customer lifecycle by up to 45% after recovery
- Clients earn up to 33% additional annual revenue from recovery
- ClinicSense case study: 69% increase in recovery after integrating with Stripe Billing
- Hooked on Phonics: Outperformed internal recovery system by 150%

**Industry Context (Subscription Payment Failures):**
- Average transaction failure rate across industries: 7.9%
- Subscription businesses face 18-20% decline rates due to expired/invalid cards
- 50% of churn in subscription retail comes from declined card payments
- 27% of subscribers cancel immediately after a payment failure
- 39% of all failed subscription payments return "generic decline" (no actionable reason)
- Insufficient funds: 26% of payment failures
- For every $1 in actual fraud, $25 of genuine payments are falsely declined
- 62% of users who encounter a payment error never return
- Subscription businesses lose 10-20% of ARR to involuntary churn
- AI-driven recovery can recapture up to 70% of failed payments
- 60-70% of card declines are recoverable through retries

**Competitive Landscape:**
- Churnkey: Retention platform with payment recovery features
- Butter Payments: AI-powered failed payment recovery
- Slicker: AI payment recovery for Stripe subscriptions
- FlyCode: Payment recovery with dunning management
- Gravy Solutions: Failed payment recovery with human outreach
- Chargebee Retention: Built-in recovery for Chargebee users
- ProfitWell Retain (Paddle): Automated payment recovery

**Top 5 Pain Point Evidence:**

1. 39% GENERIC DECLINES
   - 39% of all failed subscription payments return a "generic decline" with no specific reason
   - 26% cite "insufficient funds" but the real cause is often miscategorized
   - Different gateways return different decline codes for the same failure type
   - Without multi-acquirer routing, Revaly cannot test whether another processor would approve

2. SINGLE-GATEWAY RECOVERY
   - Recovery retries go back through the same PSP that declined the original charge
   - No cross-processor cascade or failover during retry sequences
   - Soft declines (temporary holds, velocity limits, issuer timeouts) are gateway-specific
   - Up to 50% of declined transactions are recoverable with multi-rail retries

3. NO PRE-AUTH OPTIMIZATION
   - Revaly historically intervenes after authorization failure
   - New "Payment Performance Management" category aims to address this but is early stage
   - No BIN-level routing, issuer preference optimization, or network tokenization before first attempt
   - Preventing a decline costs less than recovering one

4. LIMITED APM RETRIES
   - When card recovery fails, Engaged Recovery asks customers to update card info
   - No automatic fallback to ACH, SEPA, digital wallets, or BNPL for recurring billing
   - 27% of subscribers cancel after a payment failure from frustration
   - Alternative payment methods would retain subscribers who cannot resolve card issues

5. FRAGMENTED PSP DATA
   - 115+ gateway integrations, each with proprietary decline codes and metadata formats
   - No unified analytics layer normalizing data across processors
   - Cannot identify systemic patterns (e.g., all Amex declines on Chase gateway) across portfolio
   - Merchants see recovery rates per-gateway but not cross-gateway optimization opportunities

**Key meeting angles:**
1. **115+ gateways, zero orchestration** | Yuno adds routing intelligence before and after the first authorization attempt
2. **39% generic declines** | Multi-acquirer routing surfaces real decline reasons by testing across PSPs
3. **Recovery + prevention** | Smart Routing prevents declines; Failover recovers them. Revaly gets both
4. **27% cancel after failure** | Non-card APMs (ACH, wallets) give subscribers alternatives before they churn
5. **Spreedly partnership precedent** | Revaly already works with orchestration platforms; Yuno is a natural expansion
6. **$5M+ raised, Montreal-based** | Canadian fintech with US-focused subscription clients needs global payment reach
7. **ClinicSense + Stripe Billing** | Proven Stripe ecosystem integration; Yuno complements this stack

**Sources:**
- [FlexPay (Revaly): Official Website](https://www.revaly.co/)
- [FlexPay: Failed Payment Recovery](https://flexpay.io/)
- [FlexPay Rebrands as Revaly (Yahoo Finance)](https://finance.yahoo.com/news/flexpay-rebrands-revaly-launches-payment-140700703.html)
- [FlexPay Rebrands as Revaly (Newswire)](https://www.newswire.ca/news-releases/flexpay-rebrands-as-revaly-launches-payment-performance-management-category-873438068.html)
- [FlexPay: Crunchbase Profile](https://www.crunchbase.com/organization/flexpay-6dbe)
- [Revaly: About Us](https://www.revaly.co/about-us)
- [Revaly: Integrations](https://www.revaly.co/integration)
- [FlexPay: Payment Gateway Integrations](https://flexpay.io/integrations/payment-gateway-integrations)
- [FlexPay and Spreedly Partnership](https://www.spreedly.com/blog/flexpay-and-spreedly-expand-partnership)
- [FlexPay: Invisible Recovery](https://flexpay.io/products/invisible-recovery/)
- [FlexPay: Engaged Recovery PR](https://www.prnewswire.com/news-releases/flexpay-announces-the-launch-of-engaged-recovery-301546032.html)
- [FlexPay: Capterra Reviews](https://www.capterra.com/p/238031/FlexPay/)
- [Top Payment Recovery Platforms 2026 (FlyCode)](https://www.flycode.com/blog/top-payment-recovery-platforms-2026-comparison-chart-success-rate-stats)
- [2025 Failed Payment Benchmarks (Slicker)](https://www.slickerhq.com/blog/2025-failed-payment-benchmarks-b2c-subscription-ecommerce-ai-recovery)
- [Card Decline Statistics 2026 (CoinLaw)](https://coinlaw.io/card-decline-statistics/)
- [Subscription Payment Statistics 2025 (Kaplan Group)](https://www.kaplancollectionagency.com/news/subscription-facts-55-saas-and-b2b-payment-statistics-for-2025/)
- [State of Retention 2025 (Churnkey)](https://churnkey.co/reports/state-of-retention-2025)
- [Brandfetch: FlexPay](https://brandfetch.com/flexpay.io)
