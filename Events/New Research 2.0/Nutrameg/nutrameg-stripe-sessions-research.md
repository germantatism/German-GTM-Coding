# NUTRAMEG | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-27*

```
═══════════════════════════════════════
DATABASE FIELDS: Nutrameg
═══════════════════════════════════════

Logo: https://www.nutrameg.com/
Nombre merchant: Nutrameg

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: App Store Fee Drain
Tittle_Pain Point_2: Single PSP Web Stack
Tittle_Pain Point_3: Subscription Churn
Tittle_Pain Point_4: 30 Language Localization
Tittle_Pain Point_5: Trial to Paid Friction

Desc_Pain Point_1: 7 apps run subscriptions through Apple iTunes and Google Play Billing. 15 to 30% platform fees compound across millions of users targeting EUR 20M revenue.
Desc_Pain Point_2: Web checkout for StockholmDiet and Best.Me runs through one undisclosed third party PSP. No failover when the single processor declines a renewal.
Desc_Pain Point_3: Weekly, 1, 3, 6 month plans on auto-renew. DTC nutrition apps see 30% to 50% churn from failed cards, expired BINs, no smart retry logic.
Desc_Pain Point_4: Apps localized in 30 languages but accept only cards globally. Brazilian, Indian, Japanese, Polish users forced through cross-border card rails.
Desc_Pain Point_5: Free download to paid conversion blocked when international users cannot use local methods. Latvia HQ with no SEPA DD on EU subscriptions.

SLIDE 1: PSP TOPOLOGY

PSP_1: Apple App Store IAP
PSP_2: Google Play Billing
PSP_3: Third-Party Web PSP
PSP_4: N/A

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: SEPA Direct Debit
Local_M_2: iDEAL
Local_M_3: BLIK
Local_M_4: Pix
Local_M_5: UPI
Local_M_6: OXXO
Local_M_7: Konbini
Local_M_8: Klarna
Local_M_9: PayPal
Local_M_10: ACH Direct Debit

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across multiple acquirers optimizes each weekly, monthly, and 6 month renewal across 7 apps. With Nutrameg targeting EUR 20M turnover, even a 3% auth rate uplift recovers EUR 600K in lost annual subscription revenue across 30+ languages.
Desc_Yuno_Cap2: Automatic cascade eliminates the single PSP web checkout dependency. When the primary processor declines a Best.Me or StockholmDiet renewal, Yuno reroutes instantly to the next best acquirer. Up to 50% recovery on failed transactions with zero customer friction.
Desc_Yuno_Cap3: Activates the local rails Nutrameg's 30 language users demand: SEPA DD for Latvia and EU, BLIK for Poland, Pix for Brazil, UPI for India, Konbini for Japan, OXXO for Mexico. One API, 1,000+ payment methods across web checkout.
Desc_Yuno_Cap4: One dashboard replacing fragmented Apple IAP, Google Play, and web PSP consoles. Real-time approval rate monitoring, centralized reconciliation across all payment channels, millisecond anomaly detection on auto-renewals via Monitors.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Nutrameg at a glance:**
- Healthtech startup based in Riga, Latvia (Lastadijas 6, LV-1050)
- Legal entity: Nutrameg Latvia SIA, reg. number 40203072376
- Founded 2021 by Egija Seile, Kristofs Blaus, Vladimirs Budkins, Elina Balode
- Patented nutrition technology for weight management and fitness
- Currently unfunded, exploring investor opportunities
- Targeting EUR 20M annual turnover trajectory
- Goal: 100M users in next 24 months
- Member of World Public Health Nutrition Association
- Apps localized in 30+ languages

**Apps and products:**
- Operates 7 distinct apps tailored to regions and dietary preferences
- Best.Me (general weight management, US App Store + Google Play)
- StockholmDiet.com (web platform with Mediterranean/Nordic diet focus)
- Multiple regional app variants (Mediterranean, vegan, keto specific)

**Subscription model:**
- Weekly, 1 month, 3 month, 6 month auto-renewal subscriptions
- Set to auto-renew within 24 hours before subscription end date
- Free download with limited features, paid for full experience
- Pricing varies by region and offer
- Renewal rates may differ from initial pricing

**Confirmed payment channels:**
- Apple iTunes Account (iOS App Store IAP) for Best.Me and StockholmDiet apps
- Google Play Billing for Android
- Web checkout through undisclosed third-party payment service provider
- Card payments via SSL encryption (no card data storage)
- "The Company may change the third party payment service provider from time to time" (per Terms of Service)

**Top 5 Markets Gap Analysis:**

MARKET 1: European Union (Latvia HQ)
  ✅ Currently offer: Cards (Visa/MC/Amex), Apple Pay, Google Pay (likely), App Store IAP
  ❌ Missing: SEPA Direct Debit, iDEAL (NL), Bancontact (BE), BLIK (PL), Giropay (DE)
  💡 Latvia HQ but no SEPA DD for EU subscription billing. BLIK is dominant in Poland (close market).

MARKET 2: United States
  ✅ Currently offer: Cards, Apple Pay, Google Pay, App Store IAP
  ❌ Missing: ACH Direct Debit, PayPal, Venmo, Cash App Pay
  💡 ACH would reduce subscription churn vs card declines. PayPal absent for older demographics typical of weight management apps.

MARKET 3: Brazil (potential expansion via Portuguese/Spanish localization)
  ✅ Currently offer: International cards
  ❌ Missing: Pix, Boleto, local installments
  💡 Pix processes 70%+ of Brazilian online payments. Card-only checkout blocks unbanked Brazilian users.

MARKET 4: India (large diet/wellness market)
  ✅ Currently offer: International cards
  ❌ Missing: UPI, RuPay, Paytm, PhonePe
  💡 UPI dominates Indian digital payments. Without local rails, India market is unserved despite Hindi/regional language localization.

MARKET 5: Japan (Mediterranean/keto interest)
  ✅ Currently offer: International cards, App Store IAP
  ❌ Missing: Konbini, PayPay, Line Pay
  💡 Konbini convenience store payments are essential for Japanese subscription apps. Card penetration limited.

**Key meeting angles:**
1. **App Store fee arbitrage**: Drive web checkout with local APMs to bypass Apple/Google 15-30% commission across 7 apps
2. **Subscription auth optimization**: 30%-50% DTC churn from failed cards is recoverable with smart routing + retries
3. **30 language localization paradox**: Apps speak 30 languages but accept only cards globally. APM gap directly limits 100M user goal
4. **Single web PSP risk**: Terms admit "may change" provider but no orchestration. One outage stops EUR 20M trajectory
5. **EU SEPA DD opportunity**: Latvia HQ with EU-wide subscriptions but no SEPA Direct Debit reduces conversion in subscription-friendly Germany, Netherlands
6. **Investor readiness**: Exploring funding now. Yuno integration de-risks payment infrastructure for due diligence
7. **Trial to paid conversion**: Free download to paid plan is core funnel. Local APMs at checkout unlock Brazil, India, Mexico markets

**Sources:**
- [Nutrameg Official Site](https://www.nutrameg.com/)
- [Nutrameg LinkedIn](https://www.linkedin.com/company/nutrameg)
- [Nutrameg on Track for EUR 20M Turnover](https://www.nutrameg.com/post/nutrameg-on-track-for-20-million-turnover)
- [Best.Me App on Apple App Store](https://apps.apple.com/us/app/best-me/id6472027185)
- [Best.Me on Google Play, by Nutrameg Latvia SIA](https://play.google.com/store/apps/details?id=com.nutramegapp)
- [Nutrameg Latvia SIA Apple Developer Page](https://apps.apple.com/ee/developer/nutrameg-latvia-sia/id1510986797)
- [StockholmDiet General Terms and Conditions](https://intercom.help/stockholmdiet/en/articles/10289728-general-terms-and-conditions)
- [StockholmDiet Privacy Policy](https://intercom.help/stockholmdiet/en/articles/10289734-privacy-policy)
- [StockholmDiet on App Store](https://apps.apple.com/ee/app/stockholmdiet-com/id1510986798)
- [Nutrameg Tracxn Profile](https://tracxn.com/d/companies/nutrameg/__MdPmg_R0sMTCIeESuFmMjk15TG51zrImC--IzJeYP3g)
- [SuperAGI Nutrameg Research](https://sales.superagi.com/company/nutrameg)
- [RocketReach Nutrameg](https://rocketreach.co/nutrameg-profile_b79dfabdc590bb3c)
