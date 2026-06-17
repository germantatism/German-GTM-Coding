# HEYGEN | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: HeyGen
=======================================

Logo: https://cdn.prod.website-files.com/6606f42832a184e5d85b4197/6606f42832a184e5d85b41f1_heygen-logo-dark.svg
Nombre merchant: HeyGen

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: SMB Conversion Ceiling
Tittle_Pain Point_2: Single Acquirer Dependency
Tittle_Pain Point_3: 190-Country Card Gap
Tittle_Pain Point_4: Credit System Complexity
Tittle_Pain Point_5: Auth Rate Leakage

Desc_Pain Point_1: 70% of 85K+ customers are SMBs across 190+ countries. Small businesses in emerging markets rarely hold international cards. Card-only checkout blocks free-to-paid conversion in LatAm, SE Asia, Africa.
Desc_Pain Point_2: Stripe is the sole processor for all web billing. At $100M ARR, any degradation blocks 100% of subscriptions, upgrades, and credit purchases for 85K+ customers across 190+ countries.
Desc_Pain Point_3: 230+ avatars in 140 languages serve 190+ countries, but payment stops at cards plus limited Stripe wallets. A platform built for localization has zero localized payment acceptance.
Desc_Pain Point_4: GenCredits (200-2,000/mo by tier) layer on subscriptions. Metering credits, overages, and add-ons through a single Stripe Checkout grows complex as tiers expand.
Desc_Pain Point_5: Stripe professional services boosted auth rates 21%, confirming cross-border decline problems existed. Even after optimization, international SMB cards remain the weakest point.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (primary, web billing + Checkout)
PSP_2: Apple App Store (iOS)
PSP_3: Google Play (Android)
PSP_4: Stripe Optimized Checkout Suite

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix (Brazil)
Local_M_2: UPI (India)
Local_M_3: OXXO (Mexico)
Local_M_4: Boleto (Brazil)
Local_M_5: KakaoPay (South Korea)
Local_M_6: GCash (Philippines)
Local_M_7: BLIK (Poland)
Local_M_8: Konbini (Japan)
Local_M_9: PSE (Colombia)
Local_M_10: SPEI (Mexico)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each subscription and credit purchase to the optimal acquirer by card BIN and market. HeyGen proved sensitivity with 21% Stripe auth lift. Multi-acquirer routing pushes further. A 3% additional uplift on $100M ARR recovers $3M+ annually.
Desc_Yuno_Cap2: Automatic cascade eliminates single-Stripe dependency. When Stripe declines, Yuno reroutes renewals and credit purchases in milliseconds. Up to 50% recovery on failed transactions, building on the 21% auth gain already achieved.
Desc_Yuno_Cap3: Activates local rails for 190 countries: Pix in Brazil, UPI in India, OXXO in Mexico, KakaoPay in Korea, Konbini in Japan, GCash in Philippines, BLIK in Poland, PSE in Colombia. One API, 1,000+ methods matching content localization.
Desc_Yuno_Cap4: One dashboard unifying Stripe, App Store, and Google Play. Real-time monitoring across Creator, Business, Pro, Enterprise tiers plus GenCredit metering. NOVA fraud engine with 75% fewer false positives for 85K+ global customers.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**HeyGen at a glance:**
- Founded: 2020 by Joshua Xu (CEO) and Wayne Liang
- Headquarters: Los Angeles, CA
- Revenue: $95-100M ARR (Sep-Oct 2025), up from $57.5M (end 2024), up from $1M (early 2023)
- Valuation: $500M (Series A, Jun 2024)
- Total Funding: $65.6M across 2 rounds (led by Benchmark; Conviction, Bond Capital, Thrive Capital)
- Customers: 85,000+ globally across 190+ countries
- Employees: ~157
- Customer Mix: 70% SMBs, growing enterprise segment
- Profitability: Achieved profitability early in lifecycle

**Products:**
- AI Avatar Videos: 230+ digital avatars, text-to-video generation
- Video Translate: Automated video translation in 140+ languages
- Streaming Avatar: Real-time interactive AI avatars
- Creative Studio: Full video production suite
- GenCredits: Advanced AI feature credits (tiered allocation)
- Free Plan: $0 (1 credit)
- Creator Plan: $29/mo (200 credits)
- Business Plan: $99/mo (1,000 credits, shared pool)
- Pro Plan: $149/mo (2,000 credits)
- Enterprise Plan: $330+/mo (custom)

**Confirmed PSPs / Payment Rails:**
- Stripe: Primary processor (confirmed via Stripe case study, Stripe Optimized Checkout Suite)
- Stripe Professional Services: Engaged to boost auth rates by 21%
- Credit cards, US bank account, Cash App, Google Pay, Klarna, Link by Stripe accepted
- Apple App Store: iOS subscriptions
- Google Play: Android subscriptions
- HSBC: Multi-million pound facility for UK growth (Jan 2025, banking not payment processing)
- No secondary acquirer detected
- No payment orchestrator detected

**Key Stripe Integration Details:**
- HeyGen has been using Stripe since 2023
- Implemented Stripe's Optimized Checkout Suite with embeddable prebuilt payment form
- Stripe professional services engagement specifically to reduce fraud and boost authorization rates
- Achieved 21% auth rate improvement (confirms pre-existing cross-border decline problem)
- Stripe powers subscriptions, credit purchases, and plan management

**Market and Growth Context:**
- 190+ countries served
- 230+ digital avatars, 140+ languages
- E-learning, marketing, corporate communications primary use cases
- SMB-heavy (70% of customer base)
- Enterprise adoption accelerating in Fortune 500
- UK expansion backed by HSBC facility
- Competing with Synthesia, D-ID, and emerging Chinese competitors

**Key Payment Challenges:**
- Auth rate problems severe enough to require Stripe professional services intervention
- 21% auth improvement still leaves significant cross-border decline residual
- 70% SMB customer base in 190+ countries = high proportion of cards from emerging markets with low international acceptance
- GenCredit metering adds billing complexity on top of subscription tiers
- No local APMs despite serving 140 languages (content localization without payment localization)
- Team plan discontinued Jan 2026, indicating billing model in flux

**Key Meeting Angles:**
1. **21% auth improvement proves the pain** | HeyGen already invested in Stripe professional services to fix auth rates. This confirms cross-border decline is a known, measured problem. Multi-acquirer routing is the next step.
2. **190 countries, 140 languages, zero local APMs** | HeyGen built the most localized AI video platform in the world with zero payment localization. Content speaks 140 languages, checkout speaks only card.
3. **70% SMB in emerging markets** | SMBs in LatAm, SE Asia, and Africa rarely hold international cards. Local APMs are the only path to converting this massive free-to-paid funnel.
4. **$100M ARR to $200M+ trajectory** | Rapid growth means payment infrastructure must scale ahead of revenue, not catch up after failures.
5. **GenCredit complexity** | Subscription + credit metering + overage billing through a single Stripe integration creates reconciliation bottlenecks at scale.
6. **Stripe-only creates ceiling** | Already maxed out Stripe-native optimization (professional services). Next auth rate gains require multi-acquirer routing that Stripe alone cannot provide.
7. **Enterprise expansion** | Growing Fortune 500 adoption requires multi-acquirer resilience, enterprise invoicing, and local payment acceptance as table stakes.

**Sources:**
- [HeyGen + Stripe Case Study (21% Auth Boost)](https://stripe.com/customers/heygen)
- [HeyGen Pricing Plans (Official)](https://www.heygen.com/pricing)
- [HeyGen Billing FAQ (Help Center)](https://help.heygen.com/en/articles/9204682-heygen-pricing-plans-and-subscriptions-explained-what-you-need-to-know)
- [HeyGen Billing, Payments & Invoices (Help Center)](https://help.heygen.com/en/articles/9999710-billing-payments-invoices)
- [HeyGen Series A ($60M at $500M) (Blog)](https://www.heygen.com/blog/announcing-our-series-a)
- [HeyGen Revenue and Valuation (Sacra)](https://sacra.com/c/heygen/)
- [HeyGen $100M Revenue (GetLatka)](https://getlatka.com/companies/heygen)
- [HeyGen Statistics (WorldMetrics)](https://worldmetrics.org/heygen-statistics/)
- [HeyGen Statistics (QuantumRun)](https://www.quantumrun.com/consulting/heygen-ai-statistics/)
- [HeyGen Wikipedia](https://en.wikipedia.org/wiki/HeyGen)
- [HeyGen Revenue Model (Miracuves)](https://miracuves.com/blog/heygen-revenue-model/)
- [HeyGen Business Breakdown (Contrary Research)](https://research.contrary.com/company/heygen)
- [HeyGen Brand Kit (Official)](https://www.heygen.com/brand-kit)
- [HeyGen Funding (Tracxn)](https://tracxn.com/d/companies/heygen/__P9ntSZJZGrYxYW3EjY13X-Z2YEpHcCPx1Glu86tKclA/funding-and-investors)
