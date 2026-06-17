# Coursiv | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-28*

```
=======================================
DATABASE FIELDS: Coursiv
=======================================

Logo: https://app.coursiv.io/favicon.ico
Nombre merchant: Coursiv

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Recurring Renewal Failures
Tittle_Pain Point_2: Card-Only Web Checkout
Tittle_Pain Point_3: No LATAM Local Methods
Tittle_Pain Point_4: No Asia Local Wallets
Tittle_Pain Point_5: Apple/Google Tax Pressure

Desc_Pain Point_1: Coursiv runs 7-day, 28-day, and 12-week cycles. BBB and ComplaintsBoard threads show repeated renewal disputes. Failed renewals on 800K+ users hit MRR.
Desc_Pain Point_2: Coursiv docs list only Visa, MC, Amex, PayPal, and Apple Pay on web. Once a subscription is active, the payment method cannot be changed.
Desc_Pain Point_3: Coursiv's mobile-first audience extends across LATAM. PIX, Boleto, OXXO, SPEI, Mercado Pago, and Pago Efectivo are absent. Card declines cap LATAM activation.
Desc_Pain Point_4: Coursiv targets a global multilingual audience. APAC wallets (PayPay, KakaoPay, NaverPay, UPI, GrabPay, GCash, DANA) are absent. Card auth depresses renewals.
Desc_Pain Point_5: App Store and Google Play take 15 to 30% on IAP, while web checkout is card-only. At $30 to $40 ARPU, app-funneled subscribers erode margin vs local web rails.

SLIDE 1: PSP TOPOLOGY

PSP_1: Card Acquirer (Visa, MC, Amex)
PSP_2: PayPal
PSP_3: Apple Pay (web + iOS IAP)
PSP_4: Google Play Billing (Android IAP)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: PIX (Brazil)
Local_M_2: Boleto (Brazil)
Local_M_3: OXXO (Mexico)
Local_M_4: SPEI (Mexico)
Local_M_5: Mercado Pago (LATAM)
Local_M_6: UPI (India)
Local_M_7: PayPay (Japan)
Local_M_8: KakaoPay (South Korea)
Local_M_9: GCash (Philippines)
Local_M_10: GrabPay (SE Asia)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing Engine
Tittle_Yuno_Cap2: Failover + NOVA Recovery
Tittle_Yuno_Cap3: 1,000+ Local APMs
Tittle_Yuno_Cap4: Unified Subscription Vault

Desc_Yuno_Cap1: Route every 7-day, 28-day, and 12-week renewal to the optimal acquirer per BIN, issuer, and country. On 800K+ users at $30 to $40 ARPU, a 3 to 10% auth lift recovers millions in MRR and lowers dispute volume.
Desc_Yuno_Cap2: When a card or PayPal renewal fails, Yuno cascades instantly to a backup acquirer or method. NOVA AI recovers up to 75% of soft declines before users see a billing issue. Livelo recovered 50% of failed transactions this way.
Desc_Yuno_Cap3: Activate PIX, OXXO, SPEI, UPI, PayPay, KakaoPay, GCash, and GrabPay via one API. Subscription apps use Yuno to expand globally without per-country builds. Coursiv can open 50+ markets without rebuilding checkout.
Desc_Yuno_Cap4: One vault, one dashboard across web and in-app subscribers. Track auth, churn, and disputes by country and cohort. Cut reliance on Apple and Google IAP fees by strengthening the web checkout funnel.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Coursiv at a glance:**
- Mobile-first AI learning platform. Founded 2023
- Reported 800,000+ paid users worldwide
- Top 10 EdTech app in the US (per company materials)
- Parent: Zimran (Limassol, Cyprus). Founded 2021 by Eduard Tupikov, Zhanibek Sydykov, Arman Nurgaziyev. Tech accelerator focused on EdTech and lifestyle products
- Core product: 15-minute AI micro-lessons covering ChatGPT, automation, prompting, AI tools (30+), and online career skills
- Subscription cycles: 1-week, 4-week (28-day), 12-week plans
- Pricing: roughly $19.99 intro, ~$39.99 to $49.99 recurring; ~$30 to $40 USD per month average ARPU per public sources
- Apps: Coursiv on Google Play and Apple App Store. Approximately 50K Android downloads with $70K monthly Android revenue (Nov 2025 estimate)
- Web: home.coursiv.io, coursiv.io, app.coursiv.io, coursiv.com

**Confirmed PSPs and Payment Infrastructure:**
- Web checkout: Visa, Mastercard, American Express, PayPal, Apple Pay
- Mobile: Apple In-App Purchase (App Store) and Google Play Billing (Android)
- PSP/orchestrator not publicly disclosed
- Once a subscription is active, the payment method cannot be changed without canceling and resubscribing (per Coursiv support docs)
- Bank statement descriptors include "Coursiv", "Vcoursiv", "thecoursiv", "CORSIV SERVICE"
- No Google Pay on web checkout. No SEPA, no iDEAL, no PIX, no UPI, no PayPay confirmed
- No published payment orchestration platform (no Spreedly, Primer, Gr4vy, CellPoint, APEXX, or Yuno)

**Payment Methods by Region:**

REGION: Americas (US, Canada, LATAM)
  Accepted: Visa, Mastercard, Amex, PayPal, Apple Pay (web). IAP via App Store and Google Play (mobile)
  Missing: PIX (Brazil), Boleto, OXXO, SPEI, Mercado Pago, Pago Efectivo, Cash App Pay, Venmo, Cabal, Naranja
  Note: Web checkout is card-and-PayPal only across all Americas markets

REGION: EMEA
  Accepted: Visa, Mastercard, Amex, PayPal, Apple Pay
  Missing: SEPA Direct Debit, iDEAL (Netherlands), BLIK (Poland), Bancontact (Belgium), MB Way (Portugal), Trustly (Nordics), Open Banking (UK)
  Note: Multilingual content suggests strong EU presence but no local APMs to support recurring billing

REGION: Asia (Japan, Korea, India, SE Asia)
  Accepted: Visa, Mastercard, Amex, PayPal, Apple Pay
  Missing: PayPay (Japan, 70M+ users), Konbini cash, LINE Pay, Rakuten Pay, KakaoPay, NaverPay, Toss, UPI (India, 350M+ users), GrabPay, DANA, GCash, Alipay/WeChat Pay
  Note: Mobile-first global product with no local APMs in highest-conversion APAC markets

**Payment Issues and Incidents:**
- Unauthorized renewal complaints: BBB and ComplaintsBoard threads describe multiple unexpected charges of $19.99 and $39.99 across 28-day cycles. Many users state they did not realize the trial converted into a recurring subscription
- Cancellation friction: Apple Community and Chargeback.com guides describe difficulty locating cancellation flows, especially for users who lost access to their account email
- Refund policy windows: Coursiv refund policy ties money-back guarantees to specific usage thresholds per plan length. Personal dissatisfaction outside those thresholds is not covered
- Payment method lock-in: Coursiv documentation explicitly states the payment method cannot be changed on an active subscription without canceling and resubscribing. This worsens involuntary churn when a card expires
- Bank charge confusion: Multiple statement descriptors ("Vcoursiv", "thecoursiv", "CORSIV SERVICE") increase chargeback risk because users do not recognize the merchant name
- App Store / Play Store fees: 15 to 30% platform tax on IAP subscriptions vs lower-cost web checkout. With limited APMs on web, mobile-first users default to IAP, eroding margin on $30 to $40 ARPU plans

**Key meeting angles:**
1. **800K+ paid users on a card-only stack** | Coursiv's 800K+ paid base runs on Visa, Mastercard, Amex, PayPal, and Apple Pay only. NOVA AI could recover up to 75% of soft declines before users see a billing failure that triggers a BBB complaint or chargeback.
2. **Mobile-first global ambition with zero local APMs** | Coursiv ships in multiple languages and targets a global audience, yet no PIX, OXXO, UPI, PayPay, or KakaoPay exists at checkout. Yuno activates 1,000+ local methods through one API, opening high-growth markets without rebuilding checkout.
3. **Short subscription cycles need orchestrated retries** | 7-day, 28-day, and 12-week plans renew constantly. Without smart routing or cascading failover, every issuer decline becomes a churn event. Livelo recovered 50% of failed transactions using exactly this approach.
4. **Apple and Google take 15 to 30%; web checkout could be the margin lever** | Mobile-first means most subscribers default to IAP, which carries platform fees. A localized web checkout with PIX, UPI, and PayPay would shift volume off-platform and raise contribution margin per subscriber.
5. **BBB and ComplaintsBoard exposure is a payments-stack problem** | Repeated unauthorized charge complaints reflect a billing engine that retries on default cards without intelligent routing or alternative cascade. Smart Routing plus Failover plus a unified vault reduces both involuntary churn and dispute load.

**Coursiv Leadership and Parent (Zimran):**
- Eduard Tupikov: Co-founder, Zimran
- Zhanibek Sydykov: Co-founder, Zimran
- Arman Nurgaziyev: Co-founder, Zimran
- Coursiv operates as a Zimran-portfolio EdTech app
- No publicly listed CFO, VP Payments, or VP Subscriptions for Coursiv specifically

**Recent corporate developments:**
- 2026: Coursiv crossed 800K paid users globally
- 2026: TIME named America's Top EdTech Companies (mobile-first AI learning category referenced)
- 2025 to 2026: Mobile EdTech expansion across multilingual markets per company commentary
- 2025: Launch of dedicated support portal (support.coursiv.io) with cancellation and refund FAQs
- 2025: Apollo Technical reported updated billing flow ("Coursiv Billing 2026: What Changed and Why It Matters")

**Sources:**
- [Coursiv Home (Coursiv)](https://home.coursiv.io/)
- [Coursiv About (Coursiv)](https://coursiv.com/about)
- [Coursiv App (Coursiv)](https://app.coursiv.io/)
- [Coursiv Google Play (Google)](https://play.google.com/store/apps/details?id=io.zimran.coursiv)
- [Coursiv Payment Methods (Support)](https://support.coursiv.io/en/support/solutions/articles/73000619522-what-payment-methods-do-you-accept-)
- [Coursiv Subscription and Payments (Support)](https://support.coursiv.io/en/support/solutions/73000349744)
- [Coursiv Will I Be Charged Every Month (Support)](https://support.coursiv.io/en/support/solutions/articles/73000622399-will-i-be-charged-every-month-)
- [Coursiv Refund Policy (Support)](https://support.coursiv.io/en/support/solutions/articles/73000622759-what-is-your-refund-policy-)
- [Coursiv How to Apply for a Refund (Support)](https://support.coursiv.io/en/support/solutions/articles/73000619523-how-can-i-apply-for-a-refund-)
- [Coursiv How Does It Work (Support)](https://support.coursiv.io/en/support/solutions/articles/73000622400-how-does-coursiv-work-)
- [Coursiv How to Unsubscribe (Support)](https://support.coursiv.io/en/support/solutions/articles/73000621190-how-do-i-unsubscribe-)
- [Coursiv Why Was I Charged (Support)](https://support.coursiv.io/en/support/solutions/articles/73000621192-why-was-i-charged-)
- [Coursiv Bank Charge Page (Coursiv)](https://coursiv.com/bank-charge)
- [Coursiv BBB Profile (BBB)](https://www.bbb.org/us/nv/las-vegas/profile/training-program/coursiv-limited-1086-90091500/complaints)
- [Coursiv Fraudulent Site Complaint (ComplaintsBoard)](https://www.complaintsboard.com/coursiv-coursiv-is-a-fraudulent-site-becarefull-c1993164)
- [Coursiv Cancel Subscription Guide (Chargeback)](https://www.joinchargeback.com/cancels/how-to-cancel-coursiv)
- [Coursiv Refund Guide (Chargeback)](https://www.joinchargeback.com/refunds/how-to-get-a-coursiv-refund)
- [CORSIV SERVICE Charge (Chargeback)](https://www.joinchargeback.com/whats-this-charge/coursiv.org/CORSIV-SERVICE)
- [Coursiv Billing 2026 Changes (Apollo Technical)](https://www.apollotechnical.com/coursiv-billing-2025-what-changed-in-billing-and-why-it-matters/)
- [Mobile EdTech Coursiv Profile (Techloy)](https://www.techloy.com/mobile-edtech-how-coursiv-is-revolutionising-learning-for-a-global-workforce-with-ai/)
- [Zimran Crunchbase Profile (Crunchbase)](https://www.crunchbase.com/organization/zimran)
- [Zimran Tracxn Profile (Tracxn)](https://tracxn.com/d/companies/zimran/__iDcdst_yWfOlHHfoMJTxP4qv_f9ubN7KzZZ0-fcE2R8)
- [Coursiv Android Revenue (TrendApps)](https://trendapps.dev/app/android/io-zimran-coursiv/)
- [Coursiv LinkedIn (LinkedIn)](https://www.linkedin.com/company/coursivapp)
- [TIME America's Top EdTech 2026 (TIME)](https://time.com/article/2026/04/22/america-top-edtech-companies-2026/)
