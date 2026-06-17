# CRUNCHYROLL | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Crunchyroll
═══════════════════════════════════════

Logo: https://upload.wikimedia.org/wikipedia/commons/4/47/Crunchyroll_Logo.svg
Nombre merchant: Crunchyroll

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Subscription Churn
Tittle_Pain Point_2: GCash Removal Fallout
Tittle_Pain Point_3: Cross-Border Declines
Tittle_Pain Point_4: Single Acquirer Lock-In
Tittle_Pain Point_5: LATAM Payment Gaps

Desc_Pain Point_1: 1.4-star Trustpilot rating across 2,800+ reviews. 400+ BBB complaints in 3 years, dominated by billing disputes and failed renewals. Payment failures directly drive involuntary churn on 17M+ subscribers.
Desc_Pain Point_2: GCash dropped as payment method in Feb 2025. Philippines users with no alternative local wallet face forced cancellation. Zero automated migration to replacement method for affected subscribers.
Desc_Pain Point_3: 200+ countries served but majority of subscribers outside the US pay via cross-border card transactions. Local banks decline international charges; Visa cards explicitly rejected in some markets.
Desc_Pain Point_4: Stripe confirmed as primary payment processor (Stripe Sessions 2025 speaker). No evidence of secondary acquirer or failover. Any Stripe disruption blocks 100% of web subscription renewals globally.
Desc_Pain Point_5: Brazil installments only available for annual plans. No Pix for monthly subs. Mexico lacks OXXO integration despite massive anime fanbase. Colombia and Peru have only prepaid code workarounds.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (primary processor)
PSP_2: PayPal
PSP_3: Apple App Store (iOS IAP)
PSP_4: Google Play (Android IAP)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix (monthly)
Local_M_2: OXXO
Local_M_3: UPI
Local_M_4: GCash (removed)
Local_M_5: Maya
Local_M_6: BLIK
Local_M_7: Konbini
Local_M_8: SEPA Direct Debit
Local_M_9: iDEAL
Local_M_10: PSE

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each subscription renewal to the highest performing acquirer by card BIN, issuer, and geography. With 17M+ paid subscribers across 200+ countries and recent $2/month price increases, even a 3% auth uplift recovers millions in annual recurring revenue from prevented churn.
Desc_Yuno_Cap2: Automatic cascade eliminates Crunchyroll's single Stripe dependency. When Stripe declines a renewal, Yuno reroutes to the next best acquirer in milliseconds. Up to 50% recovery on failed transactions. Directly reduces the involuntary churn driving 400+ BBB complaints.
Desc_Yuno_Cap3: Activates the methods Crunchyroll's global anime fanbase demands: Pix monthly in Brazil, OXXO in Mexico, UPI in India, GCash/Maya replacement in Philippines, Konbini in Japan, BLIK in Poland. One API, 1,000+ methods. No engineering sprints per market.
Desc_Yuno_Cap4: Single dashboard replacing Crunchyroll's fragmented Stripe + PayPal + Apple IAP + Google Play settlement streams. Real-time approval rate monitoring per market, centralized reconciliation across all providers. Millisecond anomaly detection prevents billing cascades before they trigger mass churn.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Crunchyroll at a glance:**
- Anime streaming platform, subsidiary of Sony Pictures Entertainment (Sony Group)
- 17M+ paid subscribers (Q1 2025), 120M+ registered users, available in 200+ countries/248 territories
- Revenue: estimated ~$2.8B+ annually (15% of Sony Pictures revenue, plus nine-figure merchandising)
- Crunchyroll surpassed $2B in cumulative user spending on mobile apps
- Subscription tiers: Fan ($7.99/mo), Mega Fan ($13.99/mo), Ultimate ($15.99/mo) after Feb 2026 price increase
- Ended free ad-supported streaming Dec 31, 2025; all content now behind paywall
- Expanding into gaming, ecommerce, collectibles, theatrical, digital manga
- Sony planning USD stablecoin (Sony Bank) potentially for PlayStation and Crunchyroll payments
- Crunchyroll presented at Stripe Sessions 2025 ("Show Me the Money" panel), confirming Stripe relationship
- Sony expects Crunchyroll to drive 40% of Sony Pictures operating profit growth

**Confirmed PSPs and Partners:**
- Stripe: primary payment processor (confirmed via Stripe Sessions 2025 speaker appearance)
- PayPal: secondary payment option on web
- Apple App Store: iOS in-app purchases
- Google Play: Android in-app purchases
- Amazon Prime: channel subscription
- YouTube Premium: channel access
- Roku: platform billing
- GCash: REMOVED as payment method (Feb 2025)
- No payment orchestrator detected

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (largest market by traffic)
  Supported: Visa/MC/Amex/Discover, PayPal, Apple Pay, Google Pay
  Missing: Cash App Pay, Venmo, ACH for annual plans
  Note: Core market with highest ARPU; price increase to $13.99 Mega Fan

MARKET 2: Brazil (2nd largest market, fastest growing)
  Supported: Credit cards, installments (annual plans only), Pix (limited)
  Missing: Pix for monthly subscriptions, Boleto, local debit cards
  Note: Anime viewership exploding; Pix is 70%+ of digital payments. Monthly Pix = massive unlock

MARKET 3: India (3rd globally in anime viewership, 41% penetration)
  Supported: Credit/debit cards (cross-border)
  Missing: UPI, RuPay, Paytm, PhonePe, carrier billing
  Note: Hindi dubs surpass English for top titles. UPI is 75%+ of digital payments. Card penetration under 5%

MARKET 4: Germany (3rd largest web traffic market)
  Supported: Credit cards, PayPal
  Missing: SEPA Direct Debit, Sofort, Giropay
  Note: ~35% credit card penetration. SEPA DD is backbone of German subscription billing

MARKET 5: Philippines (major anime market, SE Asia)
  Supported: Credit cards only (GCash removed Feb 2025)
  Missing: GCash, Maya, GrabPay, ShopeePay
  Note: Credit card penetration ~6%. GCash had 60M+ users. Removing it forces mass cancellation

**Key issues and vulnerabilities:**
- 1.4-star Trustpilot across ~2,800 reviews; billing complaints dominant
- 400+ BBB complaints in 3 years, primarily payment and billing related
- GCash removal in Philippines with no replacement local wallet
- Visa cards explicitly rejected in some international markets
- Prepaid cards cannot be used for subscriptions, only gift cards
- Price increase backlash (all tiers +$2 in Feb 2026) on top of free tier removal
- Cross-border card declines for majority-international subscriber base

**Key meeting angles:**
1. **Stripe Sessions alumni** | Crunchyroll presented at Stripe Sessions 2025. They know payments matter and are actively thinking about optimization
2. **17M subscribers, 200+ countries** | Global scale with single-acquirer infrastructure. Classic orchestration opportunity
3. **India anime explosion** | 41% viewership penetration, Hindi dubs overtaking English. Zero local payment methods = massive TAM locked out
4. **GCash removal** | Dropping a major APM without replacement signals infrastructure rigidity. Yuno prevents this with instant APM switching
5. **Sony stablecoin play** | Sony Bank USD stablecoin signals payment innovation ambition. Orchestration layer is foundational
6. **Involuntary churn** | Payment failures are the #1 complaint category. Failover + smart retry directly attacks subscriber retention
7. **LATAM fandom growth** | Brazil and Mexico are fastest-growing markets. Pix monthly and OXXO are table stakes for anime fans

**Sources:**
- [Crunchyroll Logo (Wikimedia SVG)](https://commons.wikimedia.org/wiki/File:Crunchyroll_Logo.svg)
- [Crunchyroll at Stripe Sessions 2025](https://stripe.com/sessions/2025/show-me-the-money)
- [Crunchyroll 17M Subscribers](https://animebythenumbers.substack.com/p/crunchyroll-17m-subscribers)
- [Crunchyroll Statistics 2026](https://expandedramblings.com/index.php/crunchyroll-facts-statistics/)
- [Crunchyroll Wikipedia](https://en.wikipedia.org/wiki/Crunchyroll)
- [Crunchyroll $2B User Spending](https://appmagic.rocks/blog/crunchyroll-two-billion)
- [Crunchyroll Payment Methods](https://help.crunchyroll.com/hc/en-us/articles/18812304848148)
- [Crunchyroll LATAM Payment Methods](https://help.crunchyroll.com/hc/en-us/articles/22315535682708)
- [Crunchyroll GCash Removed](https://help.crunchyroll.com/hc/en-us/articles/35315613381780)
- [Crunchyroll Card Declined](https://help.crunchyroll.com/hc/en-us/articles/18505284848148)
- [Crunchyroll Price 2026 Increase](https://studentdiscount.io/blog/crunchyroll-price-2026-increase-saving-guide)
- [Sony Stablecoin for PlayStation/Crunchyroll](https://www.ccn.com/news/business/sony-stablecoin-usd-payments-playstation-crunchyroll/)
- [Crunchyroll 40% of Sony Pictures Profits](https://www.thepopverse.com/tv-crunchyroll-to-make-up-40-percent-of-sony-pictures-operating-profits-anime-growth)
- [India Ranks 3rd in Anime Viewership](https://respawn.outlookindia.com/pop-culture/pop-culture-news/india-ranks-among-top-three-global-anime-viewership-markets)
- [Crunchyroll SimilarWeb Traffic](https://www.similarweb.com/website/crunchyroll.com/)
- [Crunchyroll Installments](https://help.crunchyroll.com/hc/en-us/articles/40622821530644)
