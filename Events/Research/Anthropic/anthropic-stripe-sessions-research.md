# ANTHROPIC | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Anthropic
=======================================

Logo: https://upload.wikimedia.org/wikipedia/commons/7/78/Anthropic_logo.svg
Nombre merchant: Anthropic

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Cross-Border Card Blocks
Tittle_Pain Point_2: Single Acquirer Risk
Tittle_Pain Point_3: APM Coverage Gap
Tittle_Pain Point_4: Usage Billing Complexity
Tittle_Pain Point_5: Asia-Pac Conversion Loss

Desc_Pain Point_1: 80% of Claude usage is outside the U.S. Local banks flag Anthropic charges as cross-border. VPN + AVS mismatches trigger Stripe false declines at scale.
Desc_Pain Point_2: Stripe is the sole processor for Pro, Team, Enterprise, and API billing. Any degradation blocks 100% of subscriptions and credit top-ups for 30M MAU.
Desc_Pain Point_3: Korea, Japan, India are top 3 APAC markets with zero local APMs. No KakaoPay, no Konbini, no UPI. Only cards, PayPal, and Apple Pay accepted.
Desc_Pain Point_4: Enterprise shifted to per-token billing in 2026. Metering millions of API calls across 300K+ businesses through one processor creates reconciliation drag.
Desc_Pain Point_5: APAC revenue grew 10x in one year. Korea, Japan, India are 3 of top 5 Claude markets. Card-only checkout blocks users who pay via local wallets and rails.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (primary processor, all billing)
PSP_2: PayPal (Claude.ai checkout)
PSP_3: Apple Pay (via Stripe)
PSP_4: Cash App Pay (via Stripe)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: KakaoPay (South Korea)
Local_M_2: Konbini (Japan)
Local_M_3: UPI (India)
Local_M_4: Pix (Brazil)
Local_M_5: BLIK (Poland)
Local_M_6: Naver Pay (South Korea)
Local_M_7: PayPay (Japan)
Local_M_8: OXXO (Mexico)
Local_M_9: iDEAL (Netherlands)
Local_M_10: SEPA Direct Debit (EU)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each subscription and API credit purchase to the optimal acquirer by card BIN and currency. At $30B ARR across 150+ countries, a 3% auth uplift recovers hundreds of millions. Per-transaction routing maximizes approval on every payment.
Desc_Yuno_Cap2: Automatic cascade eliminates single-Stripe dependency. When Stripe declines, Yuno reroutes in milliseconds. API credits and renewals convert instead of failing. Up to 50% recovery on failed transactions across all billing streams.
Desc_Yuno_Cap3: Activates the APMs top markets demand: KakaoPay in Korea, Konbini in Japan, UPI in India, Pix in Brazil, BLIK in Poland, iDEAL in Netherlands, OXXO in Mexico, SEPA DD across Europe. One API, 1,000+ methods, zero per-market builds.
Desc_Yuno_Cap4: One dashboard unifying Stripe, PayPal, Apple Pay, and Cash App. Real-time monitoring across Pro, Team, Enterprise, and API billing. NOVA fraud engine with 75% fewer false positives. Centralized analytics for 300K+ business customers.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Anthropic at a glance:**
- Founded: 2021 by Dario Amodei and Daniela Amodei (ex-OpenAI VP Research)
- Headquarters: San Francisco, CA
- Valuation: $380B (Series G, Feb 2026); reportedly attracting offers at $800B+
- Revenue: $30B annualized run-rate (up from $9B at year-end 2025, up from $1B just 14 months prior)
- Claude Code: $2.5B ARR alone (Feb 2026), authors 4% of all public GitHub commits
- Monthly Active Users: 30M+, nearly 88M website visitors
- Web traffic: 287.93M visits (Feb 2026), 4th among AI platforms globally
- Business Customers: 300,000+, including 500+ spending over $1M/year; 8 of the Fortune 10
- Employees: ~1,500 (expanding rapidly across global offices)
- Cash burn: ~$3B projected for 2025; cash-flow break-even targeted for 2028

**Products:**
- Claude.ai: Consumer and business AI assistant (Pro at $20/mo, Team at $25/user/mo, Enterprise custom)
- Claude API: Usage-based billing ($3/$15 per 1M tokens for Opus 4, prepaid credit system)
- Claude Code: Agentic coding tool ($2.5B ARR, fastest-growing product)
- Claude Enterprise: Per-user + per-token hybrid billing (2026 pricing shift)
- Max Plan: $100/mo and $200/mo tiers for power users

**Confirmed PSPs / Payment Rails:**
- Stripe: Primary and sole payment processor for all Claude products (confirmed via Stripe case study and help center)
- PayPal: Secondary option on Claude.ai
- Apple Pay: Supported via Stripe integration
- Cash App Pay: Supported via Stripe integration
- ACH bank transfers: Available for monthly-invoiced enterprise accounts
- Apple App Store / Google Play: Mobile IAP for Claude mobile apps
- No payment orchestrator detected

**Geographic Expansion (2025-2026):**
- 80% of Claude usage comes from outside the United States
- Top 5 global users: 3 are in Asia (Korea, Japan, India)
- APAC run-rate revenue grew 10x in the past year
- New offices: Seoul (early 2026), Bengaluru (early 2026), Tokyo (existing), Dublin, London, Zurich
- 25%+ of Claude Code users from APAC countries
- Korea shows "particularly strong growth" per Anthropic leadership

**Key Payment Challenges:**
- Cross-border declines: U.S.-incorporated charges trigger fraud flags on international cards
- VPN + AVS conflicts: Stripe fraud detection compares IP vs. billing address, causing false declines for global users
- Unsupported regions: Cards from certain countries are automatically blocked by BIN
- Multiple troubleshooting guides exist for "Claude card declined" errors
- Enterprise invoicing via ACH is manual and separate from self-serve billing

**Key Meeting Angles:**
1. **$30B ARR, single-processor dependency** | All revenue flows through Stripe with no failover. At this scale, any Stripe incident directly impacts tens of millions in daily billing.
2. **80% international usage, card-only checkout** | Korea, Japan, and India are top markets with zero local APMs. These countries have dominant non-card payment methods (KakaoPay, Konbini, UPI).
3. **APAC 10x revenue growth** | Fastest-growing region needs local payment rails to sustain momentum. India alone has 75%+ digital payments via UPI.
4. **Usage-based billing shift** | Moving 300K+ enterprise customers to per-token billing requires sophisticated metering and reconciliation across multiple payment channels.
5. **$800B+ valuation trajectory** | Payment infrastructure resilience becomes critical for investor confidence and potential IPO preparation.
6. **Claude Code at $2.5B ARR** | Developer billing (API credits, prepaid accounts) is a distinct payment flow that benefits from orchestrated routing and failover.
7. **Card decline epidemic** | Widespread "Claude card declined" troubleshooting content signals systemic payment friction for international users.

**Sources:**
- [Anthropic Series G Funding ($30B at $380B)](https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation)
- [Anthropic $14B ARR (SaaStr)](https://www.saastr.com/anthropic-just-hit-14-billion-in-arr-up-from-1-billion-just-14-months-ago/)
- [Anthropic Passed OpenAI in Revenue (SaaStr)](https://www.saastr.com/anthropic-just-passed-openai-in-revenue-while-spending-4x-less-to-train-their-models/)
- [Anthropic $800B Valuation Offers (HeyGoTrade)](https://www.heygotrade.com/en/news/anthropic-valuation-800-billion/)
- [Anthropic AI Statistics 2026 (GetPanto)](https://www.getpanto.ai/blog/anthropic-ai-statistics)
- [How Anthropic Built a Scalable Revenue Model (Stripe)](https://stripe.com/customers/anthropic)
- [Claude Card Declined FAQ (Claude Help Center)](https://support.claude.com/en/articles/9402418-why-was-my-card-declined)
- [Claude Billing FAQs (Claude Help Center)](https://support.claude.com/en/articles/8325618-paid-plan-billing-faqs)
- [Claude Payment Error Guide (ClaudeLab)](https://claudelab.net/en/articles/claude-ai/claude-payment-error-complete-guide)
- [Anthropic Seoul Office Expansion](https://www.anthropic.com/news/seoul-becomes-third-anthropic-office-in-asia-pacific)
- [Anthropic India Office Expansion](https://www.anthropic.com/news/expanding-global-operations-to-india)
- [Anthropic Global Hiring (CNBC)](https://www.cnbc.com/2025/09/26/anthropic-global-ai-hiring-spree.html)
- [Anthropic Series G (CNBC)](https://www.cnbc.com/2026/02/12/anthropic-closes-30-billion-funding-round-at-380-billion-valuation.html)
- [Anthropic Usage-Based Billing (PYMNTS)](https://www.pymnts.com/artificial-intelligence-2/2026/anthropic-switches-to-usage-based-billing-for-enterprise-customers/)
- [Anthropic Payment Methods 2026 (CrazyRouter)](https://crazyrouter.com/en/blog/anthropic-payment-methods-2026)
- [Anthropic Logo (Wikimedia Commons)](https://commons.wikimedia.org/wiki/File:Anthropic_logo.svg)
- [Claude 2026 Statistics (Incremys)](https://www.incremys.com/en/resources/blog/claude-statistics)
