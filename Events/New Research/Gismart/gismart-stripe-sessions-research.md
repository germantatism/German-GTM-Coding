# GISMART | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Gismart
=======================================

Logo: https://asset.brandfetch.io/idOhL1P_FW/id7cwFY_lX.svg
Nombre merchant: Gismart

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: App Store Fee Burden
Tittle_Pain Point_2: No DTC Web Shop
Tittle_Pain Point_3: Ad Revenue Dependency
Tittle_Pain Point_4: Limited Sub Retention
Tittle_Pain Point_5: No Cross-Border APMs

Desc_Pain Point_1: Apple (30%) and Google (15-30%) commissions consume a massive share of subscription and IAP revenue across 1B+ downloads. With regulatory shifts enabling alternative billing (Epic v. Apple, Google Play reforms), Gismart leaves margin on the table by not routing payments through lower-cost processors.
Desc_Pain Point_2: Gismart has no direct-to-consumer web store to bypass app store commissions. Competitors like Supercell, Scopely, and MiHoYo already operate web shops processing payments at 2-3% vs 30% app store fees. For subscription-heavy wellness apps (Luvly, Dancebit), a DTC web billing channel could 10x net margins on renewals.
Desc_Pain Point_3: Gismart shifted from IAP-first to ad-driven monetization via Pangle rewarded video. Over-reliance on ad revenue exposes the company to CPM volatility and ad market downturns. Diversifying into direct subscription billing via web reduces dependence on both ad networks and app store billing.
Desc_Pain Point_4: Wellness apps (Luvly, Dancebit, Mood Balance) run weekly, monthly, and annual subscriptions billed through App Store and Google Play. No direct billing relationship with subscribers means no multi-acquirer retry on failed renewals, no smart routing, and no ability to reduce involuntary churn.
Desc_Pain Point_5: 1B+ downloads span 190+ countries, with proven success in US, China, UK, Russia, France, Canada, and Germany. Subscription checkout is limited to cards, PayPal, Apple Pay, and Google Pay. No Pix, UPI, SEPA DD, GCash, M-Pesa, or local wallets for emerging markets where card penetration is low.

SLIDE 1: PSP TOPOLOGY

PSP_1: Apple App Store (iOS IAP and subscriptions)
PSP_2: Google Play Billing (Android IAP and subs)
PSP_3: PayPal (web and in-app alternative)
PSP_4: Pangle / TikTok (ad monetization partner)
PSP_5: Credit/Debit Cards (direct via web)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix (Brazil)
Local_M_2: UPI (India)
Local_M_3: SEPA Direct Debit (EU)
Local_M_4: GCash (Philippines)
Local_M_5: M-Pesa (Africa)
Local_M_6: GrabPay (Southeast Asia)
Local_M_7: BLIK (Poland)
Local_M_8: iDEAL (Netherlands)
Local_M_9: Boleto (Brazil)
Local_M_10: OVO / DANA (Indonesia)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each subscription renewal and web shop purchase to the highest-performing acquirer by card BIN, country, and payment type. With 1B+ downloads across 190+ countries, even a 3% approval uplift on subscription renewals recovers significant revenue. Smart Routing maximizes authorization in emerging markets where cross-border processing underperforms local acquiring.
Desc_Yuno_Cap2: Automatic cascade across acquirers when a subscription renewal or DTC web purchase fails. When a Luvly or Dancebit subscription renewal declines, Yuno reroutes to the next best processor in milliseconds. Up to 50% recovery on soft declines. Essential for reducing involuntary churn on wellness app subscriptions where retention directly drives LTV.
Desc_Yuno_Cap3: Activates the payment methods Gismart's global user base needs: Pix in Brazil, UPI in India, SEPA DD in Europe, GCash in Philippines, M-Pesa in Africa, GrabPay and OVO in Southeast Asia, BLIK in Poland. One API, 1,000+ payment methods. Converts free users to paid subscribers in card-light markets where 70%+ of the population prefers local APMs.
Desc_Yuno_Cap4: One dashboard consolidating App Store IAP, Google Play Billing, web shop payments, PayPal, and ad monetization revenue into a unified view. Real-time subscription analytics across all payment rails, centralized reconciliation for 28+ apps across wellness, music, and gaming verticals. Full visibility to optimize ARPU and LTV across Gismart's entire product portfolio.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Gismart at a glance:**
- Mobile app developer and publisher specializing in Health & Wellness, Utilities, Music, and Games
- Founded 2013 by Alex Minets, Alexander Skalabanov, Artem Legonkow, and Dmitri Lipnitsky
- HQ: London, UK. Additional offices: Kyiv (Ukraine), Minsk (Belarus). Remote-first global company
- CEO: Mykola Tymkiv. CPO: Marina Klimenka (co-founder of Luvly app)
- ~300 employees across 5 continents
- Revenue: estimated $10-63M (sources vary). Minimal external funding ($266K seed, Oct 2020)
- 1B+ cumulative downloads worldwide
- 28+ apps across three verticals: wellness (7 apps), music (21 apps), games
- Flagship apps: Luvly (face yoga/beauty), Dancebit (dance fitness/weight loss), Mood Balance, DJ it!, Beat Maker Go, Piano Keyboard, Cool Goal, Domino Smash, Oil Tycoon
- Partnership with Snap Games (Snapchat integration)
- Partnership with TIDAL (music streaming in DJ it!)
- Global monetization partner: Pangle (TikTok/ByteDance ad network)
- Launching Gismart Academy in 2026

**Key markets by download volume:**
- United States (~20%+ of downloads)
- China (significant via Pangle partnership)
- United Kingdom
- Russia
- France
- Canada
- Germany
- Additional: Southeast Asia, Latin America, Africa, India

**Confirmed PSPs and Infrastructure:**
- Apple App Store: iOS in-app purchases and subscription billing
- Google Play Billing: Android in-app purchases and subscription billing
- PayPal: accepted payment method (web and app)
- Credit/debit cards: accepted via Apple Pay, Google Pay
- Apple Pay: accepted payment method
- Google Pay: accepted payment method
- Pangle: ad monetization partner (rewarded video, interstitial ads)
- No DTC web store detected
- No payment orchestrator detected
- No alternative billing implementation detected (despite regulatory changes)

**Accepted payment methods:**
- Credit/debit cards (via app stores and direct)
- PayPal
- Apple Pay
- Google Pay
- App Store billing (iOS)
- Google Play billing (Android)
- All subscription management through platform-specific settings
- Refunds must be processed through Apple/Google, not Gismart directly

**Subscription model:**
- Weekly, monthly, and annual billing cycles
- Auto-renewal with 24-hour advance charge
- Freemium model: free tier with ads, premium tier unlocks features
- Validation charges applied and immediately refunded
- US residents (CA/CT): 3-day full refund right
- EU residents: cooling-off period refund right

**Monetization mix:**
- Ad revenue: primary for games (Pangle rewarded video, interstitial)
- Subscription revenue: primary for wellness apps (Luvly, Dancebit, Mood Balance)
- In-app purchases: secondary for games
- No DTC web billing (leaving 27-28% margin on the table vs app stores)

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (core market, ~20%+ of downloads)
  Accepted: Visa/MC/Amex, PayPal, Apple Pay, Google Pay
  Missing: Cash App Pay, Venmo, ACH for web billing
  Note: Well served via app stores. DTC web shop opportunity post-Epic v. Apple ruling

MARKET 2: Europe (UK, France, Germany, major markets)
  Accepted: Visa/MC, PayPal, Apple Pay, Google Pay
  Missing: SEPA DD, iDEAL (NL), BLIK (PL), Bancontact (BE), Klarna, local wallets
  Note: SEPA DD for recurring wellness subscriptions would reduce churn significantly

MARKET 3: Brazil / Latin America (growing mobile gaming market)
  Accepted: Visa/MC (cross-border via app stores)
  Missing: Pix, Boleto, OXXO (Mexico), BRL pricing
  Note: Pix handles 70%+ of digital payments. Essential for subscription conversion

MARKET 4: India (massive mobile user base)
  Accepted: Visa/MC, Google Pay (via Play Store)
  Missing: UPI, RuPay, Paytm, PhonePe, INR-optimized pricing
  Note: UPI has 14B+ monthly transactions. Huge freemium-to-paid conversion opportunity

MARKET 5: Southeast Asia (high mobile gaming adoption)
  Accepted: Visa/MC (cross-border via app stores)
  Missing: GCash (PH), GrabPay, OVO (ID), DANA (ID), PromptPay (TH)
  Note: Card penetration below 20% in most SEA markets. Local wallets dominate

**Key meeting angles:**
1. **App store commission drain** | 30% Apple / 15-30% Google commission on every subscription dollar. Post-Epic v. Apple and Google Play reforms, DTC web billing at 2-3% is now legally viable in the US
2. **1B+ downloads, no DTC payment infrastructure** | Massive user base but zero direct billing capability. Web shop with payment orchestration could transform unit economics
3. **Wellness subscription opportunity** | Luvly, Dancebit, Mood Balance are subscription-first products. Moving recurring billing off app stores to a web-based orchestrated checkout multiplies net revenue per subscriber
4. **Global user base, US-only payment methods** | Downloads span 190+ countries but checkout options are card-centric. Local APMs in Brazil, India, SEA, and Africa would lift paid conversion from freemium
5. **Regulatory tailwind** | Epic v. Apple (US), EU DMA, Google Play reforms all open alternative billing. Gismart needs payment infrastructure to capitalize on this window
6. **Bootstrapped efficiency** | Only $266K raised with 1B+ downloads. Payment cost optimization has outsized impact on profitability for a capital-efficient company

**Sources:**
- [Gismart Official Website](https://gismart.com/)
- [Gismart Products](https://gismart.com/products/)
- [Gismart Terms of Service](https://gismart.com/terms-of-services/)
- [Gismart Brandfetch Logo](https://brandfetch.com/gismart.com)
- [Pangle: Gismart Monetization Success](https://www.pangleglobal.com/resource/27809)
- [Crunchbase: Gismart Profile](https://www.crunchbase.com/organization/gismart)
- [Tracxn: Gismart Profile](https://tracxn.com/d/companies/gismart/__mp8usaW0045Ke1daY6G8K1kGKMorZNNxJD5YmssKkV4)
- [Craft.co: Gismart Executives](https://craft.co/gismart/executives)
- [Amrop: Inside Gismart's Growth Model](https://www.amrop.com/news-insights/articles/from-apps-to-ventures-inside-gismart-s-growth-model/)
- [TechRound: Mykola Tymkiv Interview](https://techround.co.uk/interviews/a-chat-with-mykola-tymkiv-wellness/)
- [Game Developer: Beat Maker Go Case Study](https://www.gamedeveloper.com/audio/case-study-how-developer-gismart-achieved-success-in-china-usa-and-europe-with-the-25m-downloaded-beat-maker-go-mobile-game)
- [Neon Commerce: Alternative Payments for Mobile Games](https://www.neonpay.com/blog/the-complete-guide-to-alternative-payments-for-mobile-games-in-the-u-s)
- [Stripe Blog: Next Wave of App Monetization](https://stripe.com/blog/building-for-the-next-wave-of-app-monetization)
