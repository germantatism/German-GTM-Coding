# REVENUECAT | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: RevenueCat
═══════════════════════════════════════

Logo: https://cdn.brandfetch.io/revenuecat.com/w/512/h/512/logo
Nombre merchant: RevenueCat

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Stripe-Only Web Billing
Tittle_Pain Point_2: App Store Fee Dependency
Tittle_Pain Point_3: No Multi-Acquirer Routing
Tittle_Pain Point_4: Limited Web APM Coverage
Tittle_Pain Point_5: Cross-Border Subscriber Loss

Desc_Pain Point_1: RevenueCat Web Billing uses Stripe as its sole payment processor. If Stripe declines a charge, there is no fallback. For 70,000+ apps relying on RevenueCat, every failed web payment is a lost subscriber with no retry path.
Desc_Pain Point_2: RevenueCat's core business routes through Apple App Store (30% fee) and Google Play (15-30% fee). The Epic v. Apple ruling (April 2025) now allows web checkout, but RevenueCat only supports Stripe + Paddle, limiting APM options for global developers.
Desc_Pain Point_3: Web Billing relies on a single Stripe connection with no intelligent routing. High-value subscription renewals for apps in 190+ countries flow through one acquirer regardless of the subscriber's issuing bank, geography, or card type.
Desc_Pain Point_4: RevenueCat Web Billing supports cards, Apple Pay, and Google Pay via Stripe. Developers with subscribers in Brazil, India, Mexico, or Southeast Asia cannot offer Pix, UPI, OXXO, or local wallets through RevenueCat's checkout.
Desc_Pain Point_5: Developers using RevenueCat serve subscribers globally, but web billing only processes through US/EU Stripe corridors. Subscribers in emerging markets face cross-border declines, pushing them back to the 30% App Store fee path.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (Web Billing)
PSP_2: Paddle (Web Billing)
PSP_3: Apple App Store (IAP)
PSP_4: Google Play (IAP)
PSP_5: Amazon Appstore (IAP)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: UPI
Local_M_3: OXXO
Local_M_4: GCash
Local_M_5: BLIK
Local_M_6: Boleto
Local_M_7: DANA
Local_M_8: KakaoPay
Local_M_9: Konbini
Local_M_10: PSE

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each web subscription payment to the optimal acquirer for that subscriber's card BIN, issuing bank, and country. RevenueCat powers 70,000+ apps globally. Even a 3% auth uplift across web billing translates to thousands of recovered subscribers monthly.
Desc_Yuno_Cap2: Automatic cascade across multiple acquirers when Stripe declines a web subscription charge. Yuno reroutes in milliseconds to a backup processor, recovering up to 50% of soft declines. Critical for subscription renewals where a single failure triggers churn.
Desc_Yuno_Cap3: Enable RevenueCat developers to accept Pix in Brazil, UPI in India, OXXO in Mexico, GCash in Philippines, BLIK in Poland, Konbini in Japan, and KakaoPay in Korea through web billing. One API, 1,000+ methods, bypassing App Store fees entirely.
Desc_Yuno_Cap4: One dashboard unifying RevenueCat's fragmented Stripe + Paddle + App Store + Google Play settlement streams. Real-time approval monitoring across web and mobile, centralized reconciliation, per-app and per-geography performance analytics.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**RevenueCat at a glance:**
- In-app subscription management platform powering 70,000+ mobile apps
- Revenue: ~$20M ARR (2024), growing rapidly post-Series C
- Valuation: $522M (post-money, May 2025 Series C)
- Total funding: $100M (Series C led by Bain Capital Ventures)
- Rejected $500M acquisition offer, signaling confidence in independent path
- Key product: Web Billing (launched 2024) using Stripe as payment processor
- Also supports Paddle Billing integration (launched June 2025)
- Covers Apple App Store, Google Play, Amazon Appstore, Stripe, Paddle
- Private company, headquartered San Francisco
- Key customers: apps across gaming, fitness, productivity, media, dating verticals

**Epic v. Apple impact (April 2025):**
- US District Court ruling allows iOS apps to link to external web checkout flows
- RevenueCat launched Web Purchase Button and Web Billing to capitalize on this
- Developers can now save up to 30% in App Store fees by routing to web checkout
- This creates massive demand for better web payment infrastructure

**Confirmed PSPs:**
- Stripe: sole processor for RevenueCat Web Billing (confirmed in privacy policy and docs)
- Paddle: secondary billing integration (announced June 2025 via TechCrunch)
- Apple App Store: iOS in-app purchases
- Google Play: Android in-app purchases
- Amazon Appstore: Kindle/Fire in-app purchases
- No payment orchestrator detected

**Fee structure:**
- RevenueCat fee: 1% for Pro users ($2,500+ MTR)
- Stripe: 2.9% + $0.30 per transaction
- vs. Apple/Google: 15-30% commission
- Web billing saves developers 12-27% per transaction vs. App Store

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (largest developer + subscriber base)
  Currently offer: Cards, Apple Pay, Google Pay (via Stripe)
  Missing: ACH, Cash App Pay, Venmo
  US subscribers increasingly prefer wallet-based payments for digital subscriptions.

MARKET 2: Brazil
  Currently offer: International cards only (via Stripe)
  Missing: Pix, Boleto
  Pix handles 70%+ of Brazilian digital payments. App developers lose Brazilian subscribers who cannot pay via web billing.

MARKET 3: India
  Currently offer: International cards only (via Stripe)
  Missing: UPI, RuPay, net banking
  UPI dominates Indian digital payments. Without UPI, web billing is inaccessible to the vast majority of Indian subscribers.

MARKET 4: Mexico
  Currently offer: International cards only (via Stripe)
  Missing: OXXO, SPEI
  60%+ unbanked/underbanked. OXXO cash payments are standard for digital services.

MARKET 5: Southeast Asia (Philippines, Indonesia)
  Currently offer: International cards only (via Stripe)
  Missing: GCash, Maya, DANA, OVO, GrabPay
  Single-digit credit card penetration. Mobile wallets are the primary digital payment method.

**Key meeting angles:**
1. **Epic v. Apple gold rush** | Web billing demand is exploding; developers need global payment coverage beyond Stripe + Paddle
2. **70,000 apps, one processor** | Every app using Web Billing runs through a single Stripe connection with no failover
3. **30% fee arbitrage** | The value proposition of web billing collapses if cross-border declines push subscribers back to App Store
4. **Platform play** | RevenueCat is the infrastructure layer; adding Yuno makes every app on the platform payment-optimized
5. **Emerging market opportunity** | Pix, UPI, OXXO could unlock millions of subscribers currently blocked from web checkout
6. **Subscription renewal protection** | Failed renewals trigger immediate churn in subscription apps. Smart retry = subscriber retention

**Sources:**
- [RevenueCat Web Billing Overview](https://www.revenuecat.com/docs/web/web-billing/overview)
- [RevenueCat Stripe Integration](https://www.revenuecat.com/docs/web/integrations/stripe)
- [RevenueCat Paddle Integration](https://www.revenuecat.com/docs/web/integrations/paddle)
- [RevenueCat Billing Product Page](https://www.revenuecat.com/billing)
- [RevenueCat Privacy Policy](https://www.revenuecat.com/privacy)
- [RevenueCat Press Kit](https://www.revenuecat.com/press-kit/)
- [Brandfetch: RevenueCat Logo](https://brandfetch.com/revenuecat.com)
- [TechCrunch: RevenueCat $50M Series C](https://techcrunch.com/2025/05/22/revenuecat-raises-50m-as-it-expands-beyond-mobile-app-monetization/)
- [TechCrunch: RevenueCat x Paddle](https://techcrunch.com/2025/06/04/revenuecat-and-paddle-team-up-to-help-app-developers-profit-from-web-payments/)
- [TechCrunch: RevenueCat $12M Series C](https://techcrunch.com/2024/04/25/revenuecat-raises-12m-series-c-as-it-expands-its-subscription-management-to-the-web/)
- [OnlyCFO: RevenueCat Rejects $500M](https://www.onlycfo.io/p/revenuecat-rejects-500m-acquisition)
- [RevenueCat: Epic v. Apple Blog](https://www.revenuecat.com/blog/engineering/can-you-use-stripe-for-in-app-purchases/)
- [RevenueCat External Payment Integrations](https://www.revenuecat.com/docs/web/payment-integrations)
