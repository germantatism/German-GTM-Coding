# TEACHABLE | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Teachable
═══════════════════════════════════════

Logo: https://cdn.prod.website-files.com/687904fb2b26c434698c47e9/68daba31282892b31e937809_teachable-logo-color.svg
Nombre merchant: Teachable

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Single Acquirer Lock-In
Tittle_Pain Point_2: Creator Payout Lag
Tittle_Pain Point_3: APM Coverage Gap
Tittle_Pain Point_4: Cross-Border Declines
Tittle_Pain Point_5: Subscription Churn Leak

Desc_Pain Point_1: Teachable:pay runs 100% on Stripe with zero failover. Any Stripe outage blocks course purchases for 100,000+ creators and students across 188 countries.
Desc_Pain Point_2: Monthly Gateway pays creators via PayPal only, once per month. Creators outside US/CA/UK absorb 2.5%+ FX loss on every single USD payout cycle.
Desc_Pain Point_3: Students in 188 countries pay by card, Apple Pay, Google Pay, or PayPal only. Zero local APMs in Brazil, India, Mexico, or SE Asia where card use is below 30%.
Desc_Pain Point_4: International students pay USD by default with FX at their bank. Cross-border card declines from LATAM and Asian issuers reduce conversion on course purchases.
Desc_Pain Point_5: Failed subscription renewals churn with no smart retry or cascade. Each soft decline is a lost student and lost recurring revenue for the creator.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (via Teachable:pay)
PSP_2: PayPal (Monthly Payment Gateway)
PSP_3: Stripe (Custom Payment Gateway)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: UPI
Local_M_3: OXXO
Local_M_4: Boleto
Local_M_5: SPEI
Local_M_6: GCash
Local_M_7: BLIK
Local_M_8: Konbini
Local_M_9: DANA
Local_M_10: PSE

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route every course purchase to the highest-performing acquirer for that card BIN, issuer, and country. With $10B+ in creator GMV flowing through Hotmart Group and students in 188 countries, even a 3% auth uplift unlocks millions in recovered course sales annually.
Desc_Yuno_Cap2: Automatic cascade across acquirers when Stripe declines. Failed subscription renewals retry through alternate processors in milliseconds, converting involuntary churn into recovered recurring revenue. Up to 50% recovery on soft declines.
Desc_Yuno_Cap3: Activate Pix for Brazil, UPI for India, OXXO and SPEI for Mexico, GCash for Philippines, BLIK for Poland, Konbini for Japan. One API, 1,000+ payment methods, geo-routed checkout. Students pay how they prefer, creators earn more.
Desc_Yuno_Cap4: One dashboard replacing Teachable's fragmented Stripe + PayPal settlement streams. Centralized reconciliation across all processors, real-time approval rate monitoring per market, and unified payout visibility for creators worldwide.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Teachable at a glance:**
- Parent company: Hotmart Group (acquired 2020 for ~$250M)
- 100,000+ creators on the platform; $10B+ in lifetime creator earnings (across Hotmart + Teachable)
- Students from 188 countries; 30M+ products sold
- Creator plans: Builder ($39/mo), Growth ($119/mo), Advanced ($199/mo), Business ($665/mo)
- Teachable:pay available in 80+ countries; accepts 130+ currencies
- BNPL options: Klarna (US/UK) and Afterpay
- Key growth metric: creators using BNPL, gifting, upsells, and cart abandonment saw 10%+ sales increase in 2024
- 2M+ AI-generated content pieces by creators in 2024

**Confirmed PSPs:**
- Stripe: primary processor powering Teachable:pay and custom payment gateways
- PayPal: Monthly Payment Gateway (USD only), also available as custom gateway
- No payment orchestrator detected
- No failover or multi-acquirer routing in place

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (largest creator + student market)
  Accepted: Visa/MC/Amex/Discover, PayPal, Apple Pay, Google Pay, Klarna, Afterpay, Stripe Link
  Missing: ACH direct debit, Cash App Pay, Venmo standalone
  Note: US market is well covered; international markets are the blind spot.

MARKET 2: Brazil (Hotmart Group HQ market, massive creator base)
  Accepted: International cards via Stripe
  Missing: Pix, Boleto, local installment cards (parcelamento)
  Note: Pix handles 70%+ of digital payments in Brazil. Hotmart's own platform supports Pix; Teachable does not.

MARKET 3: India (large English-speaking student population)
  Accepted: International cards via Stripe
  Missing: UPI, RuPay, Paytm, PhonePe, NetBanking
  Note: 75%+ of Indian digital payments use UPI. Card penetration below 5% for credit cards.

MARKET 4: Mexico (growing LATAM creator economy)
  Accepted: International cards via Stripe
  Missing: OXXO, SPEI, local debit cards
  Note: 60%+ of Mexican e-commerce uses cash or bank transfer methods. OXXO alone processes millions of digital payments monthly.

MARKET 5: Philippines (high English-speaking student demand)
  Accepted: International cards via Stripe
  Missing: GCash, Maya, GrabPay, DragonPay
  Note: Credit card penetration ~6%. GCash has 60M+ users. Without mobile wallets, most students cannot purchase courses.

**Key payment challenges:**
- PayPal USD-only payout forces international creators to absorb FX fees on every monthly payout
- As of November 2025, Stripe processing and platform fees are no longer returned on refunds
- Teachable:pay is unavailable in many LATAM and Asian countries, forcing creators to use PayPal Monthly Gateway
- No smart retry logic for failed subscription payments; students simply lose access

**Key meeting angles:**
1. **Hotmart paradox**: parent company supports Pix and LATAM methods natively; Teachable does not
2. **188-country student base, ~6 payment methods**: massive gap between reach and payment coverage
3. **Creator payout friction**: monthly PayPal-only payouts with FX loss hurt international creator retention
4. **Subscription recovery**: no cascade retry means every soft decline is lost recurring revenue
5. **BNPL success signal**: 10%+ revenue lift from payment optionality proves demand for more methods
6. **Competitor gap**: Hotmart supports 20+ APMs; Udemy accepts local methods in multiple markets

**Sources:**
- [Teachable: Get Started with Payments](https://support.teachable.com/en/articles/11682554-get-started-with-payments)
- [Teachable:pay](https://support.teachable.com/en/articles/11682555-teachable-pay)
- [Teachable Monthly Payment Gateway](https://support.teachable.com/en/articles/11682557-monthly-payment-gateway)
- [Teachable Pay (Marketing)](https://www.teachable.com/pay)
- [Teachable Fees](https://support.teachable.com/en/articles/11682553-teachable-fees)
- [Teachable Payments Full List (SupplyGem)](https://supplygem.com/teachable-payments/)
- [Stripe Case Study: Teachable](https://stripe.com/customers/teachable)
- [Teachable + Hotmart Announcement](https://www.teachable.com/blog/teachable-hotmart)
- [Hotmart Acquires Teachable (TechCrunch)](https://techcrunch.com/2020/03/16/edtech-notches-a-win-as-teachable-is-acquired-by-hotmart/)
- [Teachable Statistics (ElectroIQ)](https://electroiq.com/stats/teachable-statistics/)
- [Teachable Checkout Issues](https://support.teachable.com/en/articles/11682435-student-guide-checkout-payment-issues)
- [Teachable Digital Tax Handling](https://support.teachable.com/en/articles/11682575-digital-content-tax-handling-outside-europe-and-the-united-states)
- [Thinkific vs Teachable International (Learniverse)](https://www.learniverse.app/blog/thinkific-vs-teachable-international)
