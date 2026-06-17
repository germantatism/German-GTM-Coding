# UDEMY | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Udemy
═══════════════════════════════════════

Logo: https://upload.wikimedia.org/wikipedia/commons/e/e3/Udemy_logo.svg
Nombre merchant: Udemy

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Auth Rate Leakage
Tittle_Pain Point_2: Subscription Churn Gap
Tittle_Pain Point_3: Limited APM Coverage
Tittle_Pain Point_4: FX Conversion Drag
Tittle_Pain Point_5: No Failover Layer

Desc_Pain Point_1: 67% of learners outside the US face cross-border card declines. African and LatAm banks block international USD charges. Card declines cost conversions daily.
Desc_Pain Point_2: 340K+ Personal Plan subscribers on recurring billing. Subscription revenue is 74% of total, rising to 75%+ in 2026. Failed charges erode the sub-first pivot.
Desc_Pain Point_3: Pix, Boleto, OXXO, UPI accepted in select markets, but no BLIK, GCash, M-Pesa, PSE, or SEPA DD. Europe has zero local APMs beyond cards and PayPal.
Desc_Pain Point_4: USD/EUR processing for 180+ countries adds FX markup. Banks in some countries refuse international currency transactions entirely, blocking purchases.
Desc_Pain Point_5: Single payment processor for card billing with no cascade. Any processor outage or decline spike blocks all course purchases and subscription activations globally.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (primary, inferred)
PSP_2: PayPal
PSP_3: Apple App Store
PSP_4: Google Play
PSP_5: Tipalti (instructor payouts)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: BLIK
Local_M_2: GCash
Local_M_3: M-Pesa
Local_M_4: SEPA Direct Debit
Local_M_5: iDEAL
Local_M_6: Bancontact
Local_M_7: PSE
Local_M_8: Nequi
Local_M_9: Przelewy24
Local_M_10: Sofort/Klarna

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing optimized by card BIN, issuer, and market. With $796M+ revenue (Q1-Q3 2025) and the subscription pivot demanding maximum conversion, even a 3% auth uplift translates to $24M+ in recovered annual revenue across 82M learners.
Desc_Yuno_Cap2: Automatic cascade eliminates single-processor dependency. When a card decline occurs, Yuno reroutes to the next best acquirer in milliseconds, recovering both one-time course purchases and recurring Personal Plan renewals. Up to 50% recovery on soft declines.
Desc_Yuno_Cap3: Extends Udemy's existing Pix/Boleto/OXXO/UPI coverage to the full 1,000+ APM catalog: SEPA DD across Europe, BLIK in Poland, GCash in Philippines, M-Pesa in Africa, iDEAL in Netherlands, PSE in Colombia. One API. No per-market engineering.
Desc_Yuno_Cap4: One dashboard consolidating web billing, PayPal, Apple IAP, Google Play, and Tipalti instructor payouts. Real-time approval rate monitoring by country and plan type, centralized reconciliation, and anomaly detection via Monitors across all revenue streams.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Udemy at a glance:**
- 82M registered learners (2025), 870M+ course enrollments to date, 180+ countries
- Revenue: $796M (Q1-Q3 2025); Q2 2026 revenue: $221M (+14% YoY)
- NASDAQ: UDMY
- Founded 2010 by Eren Bali, Oktay Caglar, Gagan Biyani. HQ: San Francisco
- 272,000+ courses from 85,000 instructors
- Subscription pivot: Personal Plan now 74% of revenue, targeting 75%+ in 2026
- 340,000+ paid Personal Plan subscribers (end Q4 2025), adding ~50K in Q4 alone
- Udemy Business: 15,700+ enterprise clients (Adidas, TCS, Apple, Fortune 500)
- Consumer subscription revenue grew 44% YoY in FY2025
- Two-thirds of customers are outside the US

**Confirmed PSPs:**
- Stripe: likely primary card processor (inferred from checkout patterns; not publicly confirmed)
- PayPal: accepted globally for course purchases
- Apple App Store / Google Play: mobile IAP
- Tipalti: instructor payout processor (replaced PayPal/Payoneer in 2025)
- Pix and Boleto: accepted in Brazil
- OXXO: accepted in Mexico
- UPI and wallets: accepted in India
- No payment orchestrator detected

**Top 5 Markets Gap Analysis:**

MARKET 1: India (22% of traffic, 15.81% of users)
  Accepted: Visa/MC, UPI, wallets, net banking (some), PayPal
  Missing: RuPay (limited), EMI installments (limited)
  Note: India is Udemy's largest traffic source. UPI acceptance is a strength vs competitors. RBI auto-debit mandate may affect Personal Plan renewals.

MARKET 2: United States (15.86% of users)
  Accepted: Visa/MC/Amex/Discover/JCB, PayPal, Apple Pay, Google Pay
  Missing: ACH, Cash App, Venmo (direct)
  Note: Primary revenue market. Well served via cards/PayPal.

MARKET 3: Brazil (5.62% of users)
  Accepted: Visa/MC, Pix, Boleto, PayPal
  Missing: Local installment cards (parcelamento)
  Note: Pix and Boleto acceptance is a competitive advantage. Boleto expires in 5 days; Pix confirmation can take up to 24 hours.

MARKET 4: Turkey (5% of traffic)
  Accepted: Visa/MC, PayPal (limited)
  Missing: Bank transfer, local debit networks, installment plans
  Note: High inflation market. Local currency pricing helps, but local acquiring and installment support are missing.

MARKET 5: Europe (major collective market)
  Accepted: Visa/MC, PayPal
  Missing: SEPA DD, iDEAL, Bancontact, BLIK, Sofort, Przelewy24, Giropay
  Note: Zero European local APMs. SEPA DD critical for recurring Personal Plan billing. iDEAL handles 70%+ of Dutch e-commerce.

**Payment issues documented:**
- Dedicated "Troubleshooting Payment Failures" support article
- "Why Is My Card Declined on Udemy?" is common enough to generate third-party guides
- Temporary authorization holds after declined transactions cause user confusion (2-4 day hold, up to 30 days)
- International transaction blocks from local banks in Africa and parts of Asia
- Pix/Boleto purchase confirmation delays (up to 24 hours) create friction

**Key meeting angles:**
1. **Subscription-first pivot** | 74% of revenue now from subscriptions, growing to 75%+. Recurring billing infrastructure is existential
2. **67% international, basic APMs** | Two-thirds of users outside US, but only Pix/Boleto/OXXO/UPI in select markets
3. **Europe APM desert** | Major revenue region with ZERO local payment methods beyond cards and PayPal
4. **340K+ paid subscribers** | Rapid Personal Plan growth (50K added in Q4 alone) means involuntary churn scales with every new subscriber
5. **Auth rate at scale** | $796M+ revenue with 82M learners. Cross-border card declines are a direct drag on the subscription pivot
6. **Instructor payout complexity** | Tipalti migration shows payment infrastructure is actively evolving; orchestration is the logical next step
7. **Competitor precedent** | Coursera (UPI + EMI in India), Skillshare (multi-PSP), LinkedIn Learning (Microsoft payment stack)

**Sources:**
- [Udemy Help: Payment Methods](https://support.udemy.com/hc/en-us/articles/360000165907)
- [Udemy Help: Troubleshooting Payment Failures](https://support.udemy.com/hc/en-us/articles/229604828)
- [Udemy Help: Pix FAQ](https://support.udemy.com/hc/en-us/articles/4412686017303)
- [Udemy Help: Purchasing with OXXO](https://support.udemy.com/hc/en-us/articles/22165948892951)
- [Udemy Help: International Transaction Fees](https://support.udemy.com/hc/en-us/articles/17880222183575)
- [Udemy Help: Currencies FAQ](https://support.udemy.com/hc/en-us/articles/229232707)
- [Udemy Help: Tipalti Instructor Payouts](https://support.udemy.com/hc/en-us/articles/29780701031831)
- [Udemy Investors: Q4 and FY2025 Results](https://investors.udemy.com/news-releases/news-release-details/udemy-reports-fourth-quarter-and-full-year-2025-results)
- [Udemy Blog: Q3 2025 Results](https://blog.udemy.com/udemy-q3-2025-results-and-beyond/)
- [Seeking Alpha: Udemy 2026 Subscription Growth](https://seekingalpha.com/news/4510970-udemy-outlines-near-double-digit-subscription-revenue-growth-for-2026-amid-accelerated)
- [Class Central: Udemy Subscription Pivot](https://www.classcentral.com/report/udemy-subscription-pivot/)
- [Class Central: Udemy By the Numbers](https://www.classcentral.com/report/udemy-by-the-numbers/)
- [Prosperity for America: Udemy Statistics 2025](https://www.prosperityforamerica.org/udemy-statistics/)
- [ThinkImpact: Udemy Statistics 2025](https://www.thinkimpact.com/udemy-users/)
- [ElectroIQ: Udemy Statistics 2025](https://electroiq.com/stats/udemy-statistics/)
- [Udemy Teach: Personal Plan Markets](https://teach.udemy.com/personal-plan-markets/)
- [EverTry: Why Card Declined on Udemy](https://evertry.co/blog/why-is-my-card-declined-on-udemy-and-how-to-fix-it/)
- [Wikipedia: Udemy](https://en.wikipedia.org/wiki/Udemy)
