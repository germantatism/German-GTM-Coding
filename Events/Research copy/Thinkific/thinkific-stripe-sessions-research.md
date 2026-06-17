# THINKIFIC | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Thinkific
═══════════════════════════════════════

Logo: https://www.thinkific.com/wp-content/uploads/2025/03/thinkific-vector-logo.png
Nombre merchant: Thinkific

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Single Stripe Dependency
Tittle_Pain Point_2: One-Currency Lock
Tittle_Pain Point_3: APM Blind Spots
Tittle_Pain Point_4: Subscription Recovery Gap
Tittle_Pain Point_5: Third-Party Fee Penalty

Desc_Pain Point_1: Thinkific Payments runs 100% on Stripe with zero failover. Any Stripe incident blocks course purchases, subscriptions, and payment plans for 60K+ creators.
Desc_Pain Point_2: Each site charges one base currency only. Global creators force students to pay cross-border, increasing decline rates and FX friction in every market.
Desc_Pain Point_3: Only cards, Apple Pay, Google Pay, and Klarna/Afterpay. Zero local APMs in Brazil, India, Mexico, or SE Asia despite supporting 150+ display currencies.
Desc_Pain Point_4: Failed subscription and payment plan charges have no cascade retry. Each soft decline triggers involuntary churn with no recovery through alternate processors.
Desc_Pain Point_5: Creators using their own Stripe pay 2 to 5% surcharge. This pushes everyone toward Thinkific Payments but removes processor flexibility and failover.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (via Thinkific Payments)
PSP_2: Stripe (custom gateway)
PSP_3: PayPal

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: UPI
Local_M_3: OXXO
Local_M_4: Boleto
Local_M_5: iDEAL
Local_M_6: BLIK
Local_M_7: GCash
Local_M_8: Bancontact
Local_M_9: Konbini
Local_M_10: SPEI

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each course transaction to the best-performing acquirer by card BIN, issuer, and geography. With $73.2M in platform revenue and 60,000+ active creators, a 3% auth rate improvement translates to significant recovered GMV across every creator storefront.
Desc_Yuno_Cap2: Automatic cascade when Stripe declines. Failed payment plan installments and subscription renewals retry through alternate acquirers in milliseconds, recovering revenue that currently drops to involuntary churn. Up to 50% recovery on soft declines.
Desc_Yuno_Cap3: Activate Pix in Brazil, UPI in India, OXXO in Mexico, iDEAL in Netherlands, BLIK in Poland, GCash in Philippines, Konbini in Japan. One API, 1,000+ payment methods. Students pay locally, creators convert globally.
Desc_Yuno_Cap4: One dashboard unifying Thinkific's fragmented Stripe + PayPal settlement. Real-time approval rate monitoring by market, centralized reconciliation, and automated payout tracking. Eliminates the need for creators to manage multiple processor accounts.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Thinkific at a glance:**
- Publicly traded: TSX: THNC (Thinkific Labs Inc.)
- 2025 revenue: $73.2M (up 9% YoY); ARR: $61M (Q4 2025)
- Q1 2026 guidance: $18.6M to $18.9M revenue
- 60,000+ active creators; creators earned $340M+ in 2023
- Net income: $1.3M in 2025 (vs. $0.2M net loss in 2024); Adjusted EBITDA: $4.1M (6% margin)
- Commerce revenue surged 77% to $10.2M in 2024
- Thinkific Plus (enterprise): $15.7M revenue, 29% growth
- HQ: Vancouver, Canada
- Thinkific Payments available in US, Canada, UK, EU, Switzerland, Norway, Singapore, Hong Kong, Australia, New Zealand
- Supports 150+ display currencies but only one charge currency per site

**Confirmed PSPs:**
- Stripe: powers Thinkific Payments (built on Stripe)
- Stripe: also available as custom/direct gateway integration
- PayPal: available as external gateway
- No payment orchestrator detected
- No multi-acquirer routing or failover

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (largest creator base)
  Accepted: Visa/MC/Amex, PayPal, Apple Pay, Google Pay, Klarna, Afterpay
  Missing: ACH, Cash App Pay
  Note: Well served for cards; BNPL adoption drives 7.5% revenue lift for creators using it.

MARKET 2: Canada (HQ market)
  Accepted: Visa/MC/Amex, PayPal, Apple Pay, Google Pay, Klarna
  Missing: Interac Online, Interac e-Transfer
  Note: Interac is Canada's dominant debit network with 300M+ transactions/month.

MARKET 3: United Kingdom (Thinkific Payments supported)
  Accepted: Visa/MC/Amex, PayPal, Apple Pay, Google Pay, Klarna, Clearpay
  Missing: Open Banking (Pay by Bank), Direct Debit
  Note: UK Open Banking adoption growing 50%+ YoY for recurring payments.

MARKET 4: Germany/Netherlands (EU Thinkific Payments)
  Accepted: Visa/MC, PayPal, Apple Pay, Google Pay
  Missing: iDEAL (NL), SEPA Direct Debit, Sofort, Giropay
  Note: iDEAL handles 70%+ of Dutch e-commerce. SEPA DD is backbone of German recurring billing. Credit card penetration ~35% in Germany.

MARKET 5: Brazil/India (NOT supported by Thinkific Payments)
  Accepted: International cards only (via custom Stripe)
  Missing: Pix, Boleto, UPI, RuPay, PhonePe, local installments
  Note: Creators in these markets cannot use Thinkific Payments at all. Students face cross-border card declines.

**Key payment challenges:**
- Single currency per site forces global creators to pick USD or lose local conversion
- 2 to 5% third-party gateway surcharge penalizes creators who want processor diversity
- Subscription fee increase (0.5% to 0.7%) in March 2026 signals rising payment infrastructure costs
- Failed student payments documentation exists but no automated intelligent retry
- PSD2 SCA compliance required for EU; adds friction without smart authentication routing

**Key meeting angles:**
1. **Public company margin pressure**: 6% EBITDA margin means every basis point of payment cost matters
2. **Commerce revenue surge**: 77% commerce growth signals payments are becoming a core revenue driver
3. **Single-currency trap**: 150+ display currencies but one charge currency creates a false sense of globalization
4. **BNPL proof point**: 7.5% revenue lift from Klarna/Afterpay proves APM optionality drives revenue
5. **EU expansion opportunity**: Thinkific Payments launched in EU but missing iDEAL, SEPA DD, Sofort
6. **Competitor comparison**: Teachable (Hotmart) has LATAM roots; Kajabi expanding to EU; both outpacing Thinkific on APMs

**Sources:**
- [Thinkific Payments Supported Countries](https://support.thinkific.com/hc/en-us/articles/1500012376321-Thinkific-Payments-Supported-Countries-and-Transaction-Fees)
- [Thinkific Payments Overview](https://support.thinkific.com/hc/en-us/articles/360062084913-Thinkific-Payments)
- [Thinkific Payments FAQs](https://support.thinkific.com/hc/en-us/articles/1500010218301-Thinkific-Payments-FAQs)
- [Thinkific Third-Party Gateway Fee](https://support.thinkific.com/hc/en-us/articles/22383950439575-Third-Party-Payment-Gateway-Fee-FAQ)
- [Thinkific Multiple Currencies](https://support.thinkific.com/hc/en-us/articles/360030737273-Can-I-sell-in-multiple-currencies)
- [Thinkific Accept Payments with Stripe](https://support.thinkific.com/hc/en-us/articles/360030723513-Integrate-with-Stripe)
- [Thinkific PSD2 Compliance](https://support.thinkific.com/hc/en-us/articles/360034425174-EU-s-Revised-Payment-Service-Directive-PSD2)
- [Thinkific Failed Student Payments](https://support.thinkific.com/hc/en-us/articles/5964503973271-Thinkific-Payments-Failed-Student-Payments)
- [Thinkific Q4/FY2025 Results](https://www.newswire.ca/news-releases/thinkific-announces-fourth-quarter-and-full-year-2025-financial-results-827221860.html)
- [Thinkific Q1 2025 Results](https://investors.thinkific.com/2025-05-06-Thinkific-Announces-First-Quarter-2025-Financial-Results)
- [Thinkific Q2 2025 Results (Yahoo Finance)](https://finance.yahoo.com/news/thinkific-announces-second-quarter-2025-201500425.html)
- [Thinkific Statistics (ElectroIQ)](https://electroiq.com/stats/thinkific-statistics/)
- [Thinkific 2025 Revenue Benchmarks](https://www.thinkific.com/resources/revenue-generation-benchmarks/)
- [Thinkific Payment Gateways (SupplyGem)](https://supplygem.com/thinkific-payment-gateways/)
