# SUBSTACK | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Substack
═══════════════════════════════════════

Logo: https://upload.wikimedia.org/wikipedia/commons/e/e3/Substack_logo.svg
Nombre merchant: Substack

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Stripe Single Dependency
Tittle_Pain Point_2: India Payment Collapse
Tittle_Pain Point_3: APM Coverage Gaps
Tittle_Pain Point_4: Involuntary Churn Leak
Tittle_Pain Point_5: Cross-Border FX Drag

Desc_Pain Point_1: 100% of payments run through Stripe with zero alternative acquirer. Any outage blocks all 5M+ paid subscriptions globally. No failover, no backup processor.
Desc_Pain Point_2: Stripe stopped onboarding Indian businesses. Creators charge INR only, banks reject cross-border cards, tokenization breaks renewals. 3rd market, broken rails.
Desc_Pain Point_3: Only cards, Apple Pay, and limited EU bank payments across 13 currencies. No Pix, UPI, BLIK, or GCash. LATAM, APAC, and Africa have zero local payment coverage.
Desc_Pain Point_4: Failed renewals get retried then a 2 week grace period before cancellation. Creators report subscribers "disappearing" with no recovery beyond email reminders.
Desc_Pain Point_5: Only 13 currencies supported. Readers in Turkey, Nigeria, Colombia and 170+ other markets see USD prices with no local currency option. FX fees add friction.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe
PSP_2: Apple IAP (iOS)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: UPI
Local_M_3: BLIK
Local_M_4: GCash
Local_M_5: Konbini
Local_M_6: OXXO
Local_M_7: Boleto
Local_M_8: Maya
Local_M_9: PSE
Local_M_10: Google Pay

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing optimized by card BIN, issuer, and market. With $450M+ in annual creator revenue and 5M+ paid subscriptions, even a 3% auth rate uplift translates to $13M+ in recovered creator earnings. Each routed renewal is a subscriber retained.
Desc_Yuno_Cap2: Automatic cascade eliminates Substack's total Stripe dependency. When Stripe declines a renewal, Yuno reroutes to the next best acquirer in milliseconds. Up to 50% recovery on soft declines, directly solving the "disappearing subscriber" problem creators report.
Desc_Yuno_Cap3: Activates APMs readers need: Pix in Brazil (BRL supported), UPI in India (3rd market), BLIK in Poland (PLN supported), GCash in Philippines, Konbini in Japan, OXXO in Mexico. One API, 1,000+ methods, zero engineering sprints.
Desc_Yuno_Cap4: One dashboard replacing the Stripe-only black box. Real-time approval rate monitoring per market, centralized reconciliation across all providers and 13+ currencies, millisecond anomaly detection via NOVA. 75% reduction in payment operations overhead for a lean team.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Substack at a glance:**
- 20M+ monthly active subscribers, 5M+ paid subscriptions (up from 2M in 2023)
- 35M+ active subscriptions total, 17,000+ paid writers, 50+ creators earning $1M+/year
- Annual creator revenue: $450M+; platform revenue: ~$45M (10% take rate)
- 125M monthly website visitors, 47.6M unique visitors (Sep 2025, +66% YoY)
- Valuation: $1.1B (Series C, $100M raised Jul 2025, led by BOND + TCG Ventures)
- Unicorn status achieved; total funding ~$200M
- 13 supported currencies: USD, CAD, GBP, AUD, EUR, BRL, MXN, NZD, CHF, DKK, NOK, SEK, PLN

**Confirmed PSPs:**
- Stripe: sole payment processor (Stripe Connect powers all creator payments and payouts)
- Apple IAP: iOS in-app subscription purchases
- No PayPal, no secondary acquirer, no payment orchestrator detected
- Stripe explicitly named in help center, privacy policy, and official case study

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (~50% of traffic)
  Accepted: Visa/MC/Amex/Discover, Apple Pay
  Missing: Google Pay, PayPal, ACH, Venmo
  Note: No Google Pay or PayPal despite being the world's largest newsletter market.

MARKET 2: United Kingdom (~8%)
  Accepted: Visa/MC, Apple Pay, SEPA (via EUR)
  Missing: Google Pay, Open Banking (Pay by Bank)
  Note: Open Banking growing fast for UK recurring payments.

MARKET 3: India (~6%)
  Accepted: Visa/MC (INR only for Indian creators, USD for international)
  Missing: UPI, RuPay, Paytm, PhonePe
  Note: Stripe stopped onboarding new Indian businesses. Banks reject cross-border cards. Tokenization issues cause silent renewal failures. Creators call India a "broken" market on Substack.

MARKET 4: Canada (~5%)
  Accepted: Visa/MC, Apple Pay (CAD supported)
  Missing: Interac, Google Pay
  Note: Interac is Canada's dominant payment rail.

MARKET 5: Germany (~4%)
  Accepted: Visa/MC, SEPA DD, Sofort (EUR)
  Missing: Giropay, Google Pay
  Note: EU bank payments recently added but only for publications that enable them manually.

**Payment failure patterns:**
- When subscription renewal fails, Substack retries then gives 2-week grace period before cancellation
- Creators report subscribers "disappearing" with failed renewals and no recovery mechanism
- Indian creators face systemic failures: banks block transactions, tokenization breaks, INR-only pricing limits international reach
- No smart retry logic, no processor cascade, no alternative payment path

**Key meeting angles:**
1. **Total Stripe dependency**: Zero backup processor for $450M+ in annual creator revenue
2. **India black hole**: 3rd largest traffic source with fundamentally broken payment rails
3. **Unicorn pressure**: $1.1B valuation demands robust global payment infrastructure
4. **Creator retention = payment reliability**: Creators leave platforms where subscribers can't pay
5. **Low-hanging fruit**: BRL, MXN, PLN currencies already supported but no local APMs activated
6. **Competitor differentiation**: Ghost, Beehiiv, Patreon all competing; payment reliability is a moat

**Sources:**
- [Substack Help: Payment Methods](https://support.substack.com/hc/en-us/articles/18687769631252-How-can-readers-pay-for-a-subscription-on-my-Substack-publication)
- [Substack Help: Stripe Setup](https://support.substack.com/hc/en-us/articles/4405482746132-How-do-I-set-up-my-Stripe-account-on-Substack-to-start-receiving-payments)
- [Substack Help: Payouts](https://support.substack.com/hc/en-us/articles/360037833691-How-do-payouts-work-on-Substack)
- [Substack Help: Supported Currencies](https://support.substack.com/hc/en-us/articles/16523703337108-Can-readers-pay-for-subscriptions-using-their-local-currency-on-Substack)
- [Substack Help: Countries Supported](https://support.substack.com/hc/en-us/articles/360041314672-Are-there-any-countries-or-geographies-you-don-t-support)
- [Substack Help: Failed Payments](https://support.substack.com/hc/en-us/articles/360037463732-What-happens-when-a-subscriber-s-payment-fails-on-my-Substack)
- [Substack Help: Direct Debit Verification](https://support.substack.com/hc/en-us/articles/19104876788500-What-do-I-need-to-do-if-Stripe-requires-extra-verification-to-accept-direct-debit-or-non-credit-card-payment-methods-on-my-Substack)
- [Substack Help: No PayPal](https://support.substack.com/hc/en-us/articles/360037862551-I-can-t-use-Stripe-Do-you-accept-PayPal-crypto-clamshells-etc)
- [Stripe Case Study: Substack](https://stripe.com/customers/substack)
- [TechCrunch: Substack International Payments](https://techcrunch.com/2024/01/29/substack-introduces-new-payment-methods-for-international-markets/)
- [PYMNTS: Substack International Currencies](https://www.pymnts.com/news/international/2024/substack-rolls-out-payment-support-international-currencies/)
- [Substack Has Failed Indian Creators](https://blog.codingconfessions.com/p/substack-has-failed-indian-creators)
- [Axios: Substack $100M Unicorn](https://www.axios.com/2025/07/17/substack-newsletter-funding-creator-economy)
- [Fueler: Substack Stats 2026](https://fueler.io/blog/substack-usage-revenue-valuation-growth-statistics)
- [SimilarWeb: substack.com Traffic](https://www.similarweb.com/website/substack.com/)
- [Substack Brand Assets](https://substack.com/brand)
