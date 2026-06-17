# PERPLEXITY AI | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Perplexity AI
=======================================

Logo: https://upload.wikimedia.org/wikipedia/commons/1/1d/Perplexity_AI_logo.svg
Nombre merchant: Perplexity AI

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Card-Only Global Checkout
Tittle_Pain Point_2: Single Processor Risk
Tittle_Pain Point_3: SE Asia Mobile Gap
Tittle_Pain Point_4: Telco Billing Friction
Tittle_Pain Point_5: API Credit Reconciliation

Desc_Pain Point_1: 100M+ MAU across 238 countries with only cards accepted. Indonesia is #1 (24.78%) with 92% mobile traffic and zero local wallets. No GoPay, OVO, or Dana to convert free users to Pro.
Desc_Pain Point_2: Stripe processes all subscriptions and API credits with no failover. At $500M+ revenue and 100M MAU, any Stripe issue blocks Pro upgrades and API top-ups for the entire global user base.
Desc_Pain Point_3: Top markets Indonesia and India are mobile-dominant with under 5% and 7% card penetration. No GoPay, OVO, UPI, or Paytm accepted. 640% India growth via Airtel cannot monetize.
Desc_Pain Point_4: Airtel (India) and Telkomsel (Indonesia) partnerships drive millions of new users who lack international cards. Converting telecom-acquired users requires local wallets or carrier billing.
Desc_Pain Point_5: Five subscription tiers plus Sonar API, Agentic Research API, and prepaid credits all metered through one Stripe pipe. Multi-product reconciliation grows complex at scale.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (primary, all web billing)
PSP_2: Apple App Store (iOS subscriptions)
PSP_3: Google Play (Android subscriptions)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: GoPay (Indonesia)
Local_M_2: UPI (India)
Local_M_3: OVO (Indonesia)
Local_M_4: Dana (Indonesia)
Local_M_5: Pix (Brazil)
Local_M_6: KakaoPay (South Korea)
Local_M_7: BLIK (Poland)
Local_M_8: Konbini (Japan)
Local_M_9: Paytm (India)
Local_M_10: OXXO (Mexico)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each Pro, Max, and Enterprise subscription to the optimal acquirer by card BIN and geography. At $500M+ revenue across 238 countries, a 3% auth uplift recovers $15M+ annually. Smart routing maximizes every renewal.
Desc_Yuno_Cap2: Automatic cascade eliminates single-Stripe dependency. When Stripe declines, Yuno reroutes in milliseconds. Pro renewals, Max upgrades, API top-ups convert instead of churning. Up to 50% recovery on failed transactions across all tiers.
Desc_Yuno_Cap3: Activates local rails top markets demand: GoPay, OVO, Dana in Indonesia (#1 market), UPI in India (#2), KakaoPay in Korea, Konbini in Japan, Pix in Brazil, BLIK in Poland, OXXO in Mexico. One API, 1,000+ methods.
Desc_Yuno_Cap4: One dashboard unifying Stripe, App Store, and Google Play billing. Real-time monitoring across Pro, Max, Enterprise, and API streams. NOVA fraud engine with 75% fewer false positives. Centralized analytics for 5 tiers plus API metering.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Perplexity AI at a glance:**
- Founded: 2022 by Aravind Srinivas (CEO), Denis Yarats, Johnny Ho, Andy Konwinski
- Headquarters: San Francisco, CA
- Valuation: $21.21B (Series E-6, early 2026)
- Revenue: $500M annualized (April 2026), up 335% YoY from $232M in 2025; targeting $656M by end of 2026
- Monthly Active Users: 100M+ (search and agent tools combined)
- Funding: $1.22B raised across 9 rounds
- Enterprise Customers: Tens of thousands, including major telecom partnerships
- Available in: 238 countries, 46 languages

**Products:**
- Perplexity Search: AI-powered answer engine (free tier)
- Perplexity Pro: $20/mo or $200/year (advanced models, unlimited Pro searches)
- Perplexity Max: $200/mo (power user tier, launched July 2025)
- Enterprise Pro: ~$40/mo per seat ($400/year)
- Enterprise Max: Custom pricing
- Sonar API: Pay-per-use developer search API
- Agentic Research API: Advanced multi-step research capability
- API Credits: Prepaid system; Pro subscribers get $5/mo credit offset

**Confirmed PSPs / Payment Rails:**
- Stripe: Primary processor for all web subscriptions and API billing (confirmed via billing FAQ and Stripe portal access)
- Apple App Store: iOS subscription billing
- Google Play: Android subscription billing
- No PayPal, no local wallets, no bank transfers detected
- No payment orchestrator detected

**Geographic Distribution and Key Markets:**
- #1 Indonesia: 24.78% of traffic, 92.53% mobile usage; Telkomsel partnership (178M subscribers, May 2025)
- #2 India: 22.16% of traffic; Airtel partnership drove 640% user growth in Q2 2025; 2.8M app downloads in Q2 2025 alone; $400M India investment committed for 2026
- #3 United States: 16.22% of traffic
- #4 South Korea: 92.32% desktop usage, high engagement market
- Mobile vs. desktop varies dramatically by region
- Snapchat partnership (Jan 2026): Perplexity powers AI search inside Snapchat for ~1B MAU

**Key Payment Challenges:**
- Card-only checkout in card-poor markets: Indonesia (<5% card penetration), India (~7% card penetration)
- Massive telco-acquired user bases with no local payment conversion path
- USD-only pricing with no local currency options in most markets
- API prepaid credit system adds billing complexity on top of subscriptions
- Mobile IAP via App Store/Google Play takes 15-30% commission vs. direct web billing

**Key Meeting Angles:**
1. **#1 market has <5% card penetration** | Indonesia is the largest Perplexity market by traffic and 92% mobile. Without GoPay, OVO, or Dana, the vast majority cannot convert to Pro.
2. **India 640% growth, zero local rails** | Airtel partnership drove explosive user acquisition, but UPI handles 75%+ of Indian digital payments. Card-only checkout creates a monetization ceiling.
3. **$500M ARR through single processor** | All web revenue flows through Stripe with no failover. At this growth velocity, processor dependency is a board-level risk.
4. **5 subscription tiers + API credits** | Complex multi-product billing across consumer, enterprise, and developer segments needs orchestration, not a single-pipe processor.
5. **Telco partnerships as conversion wedge** | Carrier billing integration through Yuno would let Airtel (India) and Telkomsel (Indonesia) users subscribe directly from their mobile plan.
6. **$656M 2026 target** | Revenue target requires converting massive free user bases in markets where cards simply are not the primary payment method.
7. **Mobile IAP fee arbitrage** | Routing web subscribers through local APMs instead of App Store/Play Store eliminates 15-30% platform commission.

**Sources:**
- [Perplexity AI Wikipedia](https://en.wikipedia.org/wiki/Perplexity_AI)
- [Perplexity $200M at $20B Valuation (TechCrunch)](https://techcrunch.com/2025/09/10/perplexity-reportedly-raised-200m-at-20b-valuation/)
- [Perplexity AI Statistics 2026 (DemandSage)](https://www.demandsage.com/perplexity-ai-statistics/)
- [Perplexity AI Statistics (GetPanto)](https://www.getpanto.ai/blog/perplexity-ai-statistics)
- [Perplexity Revenue and Valuation (Sacra)](https://sacra.com/c/perplexity/)
- [Perplexity Statistics (AffiliateboOster)](https://www.affiliatebooster.com/perplexity-ai-statistics/)
- [Perplexity 2025-2026 Trends (Incremys)](https://www.incremys.com/en/resources/blog/perplexity-statistics)
- [Perplexity Billing FAQ (Help Center)](https://www.perplexity.ai/help-center/en/articles/10353002-billing-faq-for-pro-plan-subscribers)
- [Perplexity API Billing (Help Center)](https://www.perplexity.ai/help-center/en/articles/10354847-api-payment-and-billing)
- [Perplexity Subscription Plans (Help Center)](https://www.perplexity.ai/help-center/en/collections/18799292-subscription-plans-billing)
- [Perplexity Statistics (SeoProfy)](https://seoprofy.com/blog/perplexity-ai-statistics/)
- [Perplexity AI Statistics (Index.dev)](https://www.index.dev/blog/perplexity-statistics)
- [Perplexity Logo (Wikimedia Commons)](https://commons.wikimedia.org/wiki/File:Perplexity_AI_logo.svg)
