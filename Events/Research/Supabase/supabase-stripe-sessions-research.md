# SUPABASE | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Supabase
═══════════════════════════════════════

Logo: https://supabase.com/brand-assets/supabase-logo-wordmark--dark.svg
Nombre merchant: Supabase

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Card-Only Limitation
Tittle_Pain Point_2: USD-Only Billing
Tittle_Pain Point_3: Developer Conversion Gap
Tittle_Pain Point_4: Single Acquirer Risk
Tittle_Pain Point_5: Tax Rollout Complexity

Desc_Pain Point_1: Only 6 card brands accepted. No bank transfers, no wallets, no local APMs. Developers in low card-penetration markets cannot upgrade from Free to Pro.
Desc_Pain Point_2: All billing in USD from Singapore entity. 5M+ devs worldwide pay cross-border FX markups on every charge, increasing involuntary churn on $25/mo plans.
Desc_Pain Point_3: 5M+ developers but Free to Pro jump requires an intl credit card. In India, Brazil, and Southeast Asia, most developers lack such cards.
Desc_Pain Point_4: Stripe is the sole processor with no failover. At $70M+ ARR across 150 countries, any degradation blocks Pro upgrades and usage-based overages.
Desc_Pain Point_5: Tax collection rollout in May 2026 across international markets adds billing complexity. Tax errors compound with payment failures without backup.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe
PSP_2: Stripe Billing (invoicing)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: UPI
Local_M_2: Pix
Local_M_3: SEPA Direct Debit
Local_M_4: BLIK
Local_M_5: GoPay
Local_M_6: GCash
Local_M_7: iDEAL
Local_M_8: Boleto
Local_M_9: OXXO
Local_M_10: Konbini

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each Pro plan subscription and usage-based overage to the optimal acquirer for that card BIN and market. At $70M+ ARR growing 250% YoY, a 3% auth uplift recovers $2.1M+ annually. Smart Routing maximizes conversion on every recurring charge.
Desc_Yuno_Cap2: Automatic cascade when Stripe declines a subscription renewal or overage charge. Yuno reroutes to the next best processor in milliseconds. For a developer running production databases, a failed payment means potential service disruption. Up to 50% recovery rate.
Desc_Yuno_Cap3: Opens the door for 5M+ developers worldwide: UPI in India, Pix in Brazil, SEPA DD across Europe, BLIK in Poland, GoPay in Indonesia, iDEAL in Netherlands, OXXO in Mexico. One API, 1,000+ methods. Convert free-tier developers into paying customers.
Desc_Yuno_Cap4: One dashboard consolidating all payment flows: subscriptions, usage-based overages, and the upcoming international tax rollout. Real-time approval monitoring across 150 countries, centralized reconciliation, and instant anomaly detection.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Supabase at a glance:**
- 5M+ developers, 11.2M total databases created, 100,000+ API calls per second
- Revenue: $70M ARR (2025), up 250% YoY from $30M (end 2024)
- Valuation: $5B (Series E, October 2025, $100M raised). Seeking $10B in next round (April 2026)
- Total funding: $500M+ since 2020 founding
- Open-source Firebase alternative: Postgres database, auth, storage, edge functions, realtime
- Pricing: Free (50K MAUs), Pro ($25/mo), Team ($599/mo)
- Partnership with AWS (December 2025) for developer infrastructure
- Billing entity in Singapore. Tax rollout May-June 2026
- HQ: San Francisco. ~230 employees (2025)
- Payment methods: Visa, MC, Amex, JCB, CUP, Cartes Bancaires only

**Confirmed PSPs:**
- Stripe: sole payment processor (confirmed in privacy policy and Stripe case study)
- Stripe Billing: handles subscription invoicing and usage-based charges
- Open-source stripe-sync-engine for data synchronization
- No secondary processor or payment orchestrator detected
- Card-only acceptance; no bank transfers, no wallets, no local APMs

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (largest developer market)
  Accepted: Visa/MC/Amex (USD)
  Missing: ACH for subscriptions
  Note: Primary revenue market. Card payments work well but ACH would reduce interchange costs.

MARKET 2: India (fast-growing developer hub)
  Accepted: Visa/MC (international USD)
  Missing: UPI, RuPay, NetBanking
  Note: India's developer community is one of the fastest growing. Most Indian developers lack international credit cards. UPI is essential.

MARKET 3: Europe (Frankfurt, London regions)
  Accepted: Visa/MC/Amex, Cartes Bancaires (France)
  Missing: SEPA Direct Debit, iDEAL, BLIK, Sofort, Bancontact
  Note: GDPR compliance makes EU a key market. SEPA DD is standard for European SaaS subscriptions.

MARKET 4: Southeast Asia (Singapore billing entity, strong presence)
  Accepted: Visa/MC
  Missing: GoPay, OVO, GCash, GrabPay, DANA
  Note: Singapore is Supabase's billing entity. SEA developers face low card penetration (5-15%).

MARKET 5: Brazil/LATAM (growing developer market)
  Accepted: Visa/MC (USD)
  Missing: Pix, Boleto, OXXO, PSE
  Note: Pix handles 70%+ of Brazilian digital payments. Zero local options for LATAM developers.

**Key meeting angles:**
1. **$10B valuation pursuit** | Payment infrastructure maturity matters to investors at this scale
2. **Card-only is the bottleneck** | 5M developers but only 6 card brands accepted. No wallets, no bank transfers, no local APMs.
3. **Free to Pro conversion** | The $25/mo Pro plan requires a card most global developers lack. Local APMs directly increase conversion.
4. **250% YoY growth** | Payment failures scale with growth. Smart routing and failover become critical at $70M+ ARR.
5. **Tax rollout May 2026** | Adding international tax collection increases billing complexity. Multi-processor support reduces risk.
6. **AWS partnership** | December 2025 AWS partnership expands global reach. Payment methods should match infrastructure footprint.
7. **Open-source DNA** | Supabase built an open-source stripe-sync-engine, showing they value payment data transparency.

**Sources:**
- [Supabase Privacy Policy](https://supabase.com/privacy)
- [Supabase Pricing](https://supabase.com/pricing)
- [Supabase Billing FAQ](https://supabase.com/docs/guides/platform/billing-faq)
- [Supabase Brand Assets](https://supabase.com/brand-assets)
- [Stripe Customer Story: Supabase](https://stripe.com/customers/supabase)
- [Supabase Stripe Sync Engine](https://supabase.com/blog/stripe-sync-engine-integration)
- [TechCrunch: Supabase $5B Valuation](https://techcrunch.com/2025/10/03/supabase-nabs-5b-valuation-four-months-after-hitting-2b/)
- [Fortune: Supabase $100M at $5B](https://fortune.com/2025/10/03/exclusive-supabase-raises-100-million-at-5-billion-valuation-as-vibe-coding-soars/)
- [Sacra: Supabase Revenue & Valuation](https://sacra.com/c/supabase/)
- [GetLatka: Supabase Revenue](https://getlatka.com/companies/supabase.com)
- [TapTwice: Supabase Statistics](https://taptwicedigital.com/stats/supabase)
- [AWS: Supabase Partnership](https://press.aboutamazon.com/2025/12/supabase-and-aws-empower-app-developers-to-build-in-a-weekend-scale-to-millions)
- [Supabase Available Regions](https://supabase.com/docs/guides/platform/regions)
- [Pulumi: Supabase Case Study](https://www.pulumi.com/case-studies/supabase/)
