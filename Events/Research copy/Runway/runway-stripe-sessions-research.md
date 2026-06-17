# RUNWAY | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Runway
=======================================

Logo: https://cdn.prod.website-files.com/6228fdbc6c971401d02a9c42/62a2024b84a7e7644e7afe6d_Runway_logo.svg
Nombre merchant: Runway

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Credit Burn Rate Friction
Tittle_Pain Point_2: Single Acquirer Risk
Tittle_Pain Point_3: Non-US Market Gap
Tittle_Pain Point_4: Enterprise Billing Limits
Tittle_Pain Point_5: iOS Fee Drain

Desc_Pain Point_1: Credits reset monthly with no rollover. Users exhaust mid-cycle and need instant top-ups to keep generating. Any payment friction at that moment interrupts creative workflows for 500K+ weekly creators.
Desc_Pain Point_2: Stripe is the sole processor for subscriptions, credits, and API billing. At $265M projected 2026 revenue, any degradation blocks 100% of sign-ups, renewals, and top-ups for 4M users.
Desc_Pain Point_3: 55% of revenue is international (Europe 30%, APAC 18%, RoW 7%). Checkout offers only cards, Apple Pay, Cash App Pay, and Link. Zero local APMs in Europe, Asia, or LatAm.
Desc_Pain Point_4: Scaling from creators to enterprise with Gen-4.5 and API. Enterprise needs invoicing, procurement workflows, and multi-seat billing that Stripe consumer checkout cannot deliver.
Desc_Pain Point_5: iOS subscriptions lose 15-30% to App Store commission. With 5M+ mobile downloads, a material portion of subscribers pay Apple instead of cheaper direct web billing.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (primary, all web billing)
PSP_2: Apple App Store (iOS)
PSP_3: Apple Pay (via Stripe)
PSP_4: Cash App Pay (via Stripe)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: iDEAL (Netherlands)
Local_M_2: SEPA Direct Debit (EU)
Local_M_3: Pix (Brazil)
Local_M_4: UPI (India)
Local_M_5: KakaoPay (South Korea)
Local_M_6: Konbini (Japan)
Local_M_7: BLIK (Poland)
Local_M_8: Bancontact (Belgium)
Local_M_9: Sofort (Germany/Austria)
Local_M_10: OXXO (Mexico)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each subscription renewal and credit top-up through the optimal acquirer by card BIN, issuer, and currency. With $265M projected 2026 revenue and 55% international mix, even a 3% auth uplift on cross-border transactions recovers $4M+ annually. Smart routing ensures Gen-4.5 credits convert at the moment creators need them most.
Desc_Yuno_Cap2: Automatic cascade eliminates Runway's single-Stripe dependency. When Stripe declines or experiences latency, Yuno reroutes to the next best acquirer in milliseconds. Subscription renewals, credit top-ups, and API billing convert instead of failing. Up to 50% recovery on failed transactions, protecting creator workflow continuity for 500K+ weekly active users.
Desc_Yuno_Cap3: Activates the local rails Runway's international creator base demands: iDEAL and SEPA DD in Europe (30% of revenue), Pix in Brazil, UPI in India, KakaoPay in Korea, Konbini in Japan, BLIK in Poland, Bancontact in Belgium, Sofort in Germany, OXXO in Mexico. One API, 1,000+ payment methods, matching Runway's global creative community with local payment acceptance.
Desc_Yuno_Cap4: One dashboard unifying Stripe web billing, Apple App Store iOS billing, and API metering into a single reconciliation layer. Real-time monitoring across Standard, Pro, Unlimited, and Enterprise tiers plus credit consumption tracking. NOVA fraud engine with 75% fewer false positives. Centralized analytics replacing fragmented Stripe + Apple billing for 4M+ registered users.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Runway at a glance:**
- Founded: 2018 by Cristobal Valenzuela (CEO), Alejandro Matamala, and Anastasis Germanidis
- Headquarters: New York, NY
- Valuation: $5.3B (Series E, Feb 2026); up from $3.3B (Series D, Apr 2025)
- Revenue: $265M projected for 2026; $90M annualized as of Jun 2025 (up from $70M end 2024)
- Total Funding: $859M across multiple rounds
- Registered Users: 4M; Monthly Active Users: 1.2M; Weekly Active Creators: 500K+
- Mobile Downloads: 5M+
- Customers: 300K+ paying, 150K+ paying subscribers (2025)
- Employees: ~140 (expanding post-Series E)

**Products:**
- Gen-4.5: Latest AI video generation model (HD video from text prompts, native audio, multi-shot, character consistency)
- Gen-3 Alpha Turbo: Previous generation model (still available)
- Third-party Models: Veo 3.1, Kling 3.0 Pro integrated into platform
- API: Developer access for video generation
- Free Tier: 125 one-time credits
- Standard Plan: $12/mo annual ($15/mo monthly), 625 credits
- Pro Plan: $28/mo annual ($35/mo monthly), 2,250 credits
- Unlimited Plan: $76/mo annual ($95/mo monthly), unlimited generations
- Enterprise Plan: Custom pricing
- Credit System: Monthly reset, no rollover, add-on purchases available
- Annual Billing: 20% discount

**Confirmed PSPs / Payment Rails:**
- Stripe: Primary and sole web payment processor (confirmed via Stripe case study "Runway Protects Developer Time with No-Code Solutions from Stripe")
- Apple Pay: Supported via Stripe
- Cash App Pay: Supported via Stripe
- Link (Stripe): Accelerated checkout
- Apple App Store: iOS subscription billing
- No secondary acquirer detected
- No payment orchestrator detected

**Revenue Geographic Split (2025):**
- North America: 45%
- Europe: 30%
- Asia-Pacific: 18%
- Rest of World: 7%
- 55% of revenue is international (non-North American)

**Recent Strategic Developments:**
- Series E: $315M raised Feb 2026 led by General Atlantic
- Gen-4.5 launch: Major model upgrade with native audio, long-form, multi-shot capabilities
- $10M venture fund: Launched Apr 2026 to support AI/media/simulation startups
- Enterprise scaling: Using Series E funds to expand 140-person team across research, engineering, and go-to-market
- Lionsgate partnership: First major Hollywood studio collaboration
- Academy Award recognition: "Shadow Play" (short film made with Runway) won Best Short Film, Live Action at 97th Academy Awards

**Key Payment Challenges:**
- Credit system with no rollover creates urgent mid-cycle top-up needs where any payment friction = workflow interruption
- 55% international revenue with card-only checkout (no European bank transfers, no Asian wallets)
- Europe is 30% of revenue with zero SEPA DD, iDEAL, Bancontact, or Sofort
- iOS billing through Apple takes 15-30% commission on 5M+ mobile app installs
- API billing for enterprise clients requires capabilities beyond Stripe consumer checkout
- Scaling from creator tool to enterprise platform requires multi-acquirer payment infrastructure

**Key Meeting Angles:**
1. **Credit urgency = payment sensitivity** | Runway's no-rollover credit system means users need instant top-ups mid-creative-workflow. Any payment decline at that moment breaks the creative process and drives churn.
2. **55% international, card-only** | More than half of Runway's revenue is international. Europe (30%) is the largest non-US region with zero local bank payment methods (iDEAL, SEPA DD, Sofort).
3. **$5.3B valuation, scaling to enterprise** | Series E funds are earmarked for enterprise expansion. Enterprise procurement requires invoicing, multi-acquirer resilience, and local payment acceptance.
4. **$859M total funding, 140 employees** | Extremely capital-efficient team. Payment optimization directly accelerates the path to profitability that investors expect from Series E onward.
5. **Gen-4.5 + third-party models** | Platform evolution from single-model tool to multi-model marketplace increases billing complexity (different credit costs per model).
6. **iOS fee arbitrage** | 5M+ mobile downloads. Routing web subscribers through local APMs instead of App Store eliminates 15-30% platform fees.
7. **Hollywood validation** | Lionsgate partnership and Academy Award win signal enterprise-grade creative tool. Enterprise customers expect enterprise-grade payment infrastructure.

**Sources:**
- [Runway Series E $315M at $5.3B (TechCrunch)](https://techcrunch.com/2026/02/10/ai-video-startup-runway-raises-315m-at-5-3b-valuation-eyes-more-capable-world-models/)
- [Runway Series D $308M (TechCrunch)](https://techcrunch.com/2025/04/03/runway-best-known-for-its-video-generating-models-raises-308m/)
- [Runway + Stripe Case Study (Stripe)](https://stripe.com/customers/runway)
- [Runway Revenue and Valuation (Sacra)](https://sacra.com/c/runway/)
- [Runway Statistics 2026 (Fueler)](https://fueler.io/blog/runway-usage-revenue-valuation-growth-statistics)
- [Runway Statistics (BayelsaWatch)](https://bayelsawatch.com/runway-ml-statistics/)
- [Runway $300M Revenue (GetLatka)](https://getlatka.com/companies/runwayml.com)
- [Runway Payment Methods (Help Center)](https://help.runwayml.com/hc/en-us/articles/30657959470483-What-payment-methods-are-available)
- [Runway API Billing (Docs)](https://docs.dev.runwayml.com/usage/autobilling/)
- [Runway Pricing (Official)](https://runwayml.com/pricing)
- [Runway Brand Guidelines (Official)](https://runwayml.com/brand-guidelines)
- [Runway Wikipedia](https://en.wikipedia.org/wiki/Runway_(company))
- [Runway $10M Fund (AI Insider)](https://theaiinsider.tech/2026/04/02/runway-launches-10m-fund-to-expand-ai-video-and-world-model-ecosystem/)
- [Runway SWOT Analysis (DeepResearchGlobal)](https://www.deepresearchglobal.com/p/runway-swot-analysis)
- [Runway Pricing 2026 (Somake)](https://www.somake.ai/blog/runway-ai-pricing)
