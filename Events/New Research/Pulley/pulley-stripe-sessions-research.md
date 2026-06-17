# PULLEY | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Pulley
=======================================

Logo: https://asset.brandfetch.io/idp6E2jCXm/idqIWsBF6S.png
Nombre merchant: Pulley

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: US-Only ACH Payments
Tittle_Pain Point_2: Single Processor Risk
Tittle_Pain Point_3: Wire Transfer Friction
Tittle_Pain Point_4: Multi-Currency Gap
Tittle_Pain Point_5: Exercise Payment Delays

Desc_Pain Point_1: ACH option exercise is restricted to U.S. bank accounts only. International employees holding vested stock options cannot exercise digitally through Pulley. Global teams must fall back to manual wire transfers, creating friction at scale.
Desc_Pain Point_2: Stripe is the sole payment processor for all Pulley billing and ACH option exercises. Any Stripe degradation blocks subscription revenue and employee option exercises simultaneously. No backup acquirer exists for the platform.
Desc_Pain Point_3: International option exercises require manual wire instructions. Employees must coordinate bank details offline, send wires costing $15 to $50 per transaction, and wait for manual confirmation. This friction discourages timely exercises.
Desc_Pain Point_4: Pulley supports equity grants for international employees but processes all payments in USD only. Employees in Europe, Asia, and LATAM pay FX conversion fees on every exercise. No local currency settlement reduces their net equity value.
Desc_Pain Point_5: ACH transfers take 5 to 7 business days to settle. During volatile markets, employees cannot exercise and sell quickly. Slow settlement creates a window where stock value can shift significantly before the transaction completes.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (primary processor, billing and ACH)
PSP_2: Plaid (bank account linking for senders)
PSP_3: Wire Transfer (manual, international fallback)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: SEPA Instant (EU)
Local_M_2: Pix (Brazil)
Local_M_3: UPI (India)
Local_M_4: iDEAL (Netherlands)
Local_M_5: BLIK (Poland)
Local_M_6: PayPay (Japan)
Local_M_7: Bancontact (Belgium)
Local_M_8: KakaoPay (South Korea)
Local_M_9: OXXO (Mexico)
Local_M_10: GiroPay (Germany)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each subscription payment and option exercise to the optimal acquirer by currency and geography. For a platform serving 4,600+ companies with global shareholders, smart routing maximizes approval rates on every transaction. 3% to 10% auth uplift on cross-border payments.
Desc_Yuno_Cap2: Automatic cascade eliminates single-Stripe dependency. When Stripe declines, Yuno reroutes in milliseconds to a backup processor. Option exercises and SaaS renewals convert instead of failing. Up to 50% recovery on failed transactions across all payment flows.
Desc_Yuno_Cap3: Activates the local rails international employees need to exercise options: SEPA Instant in Europe, Pix in Brazil, UPI in India, KakaoPay in Korea, PayPay in Japan, iDEAL in Netherlands. One API, 1,000+ methods, replacing manual wire transfers entirely.
Desc_Yuno_Cap4: One dashboard unifying Stripe billing, ACH exercises, and international wire transfers. Real-time monitoring across SaaS subscriptions and equity transactions. NOVA fraud engine with 75% fewer false positives. Multi-currency settlement in a single view.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Pulley at a glance:**
- Founded: 2019 by Yin Wu (three-time YC alum, ex-Microsoft principal engineer)
- Headquarters: Oakland, California
- CEO: Yin Wu; COO: Grant Oladipo
- Employees: ~50 to 80 (estimated, growing rapidly in 2025-2026)
- Funding: $50.1M total raised
  - Series A: $10M led by Stripe
  - Series B: $40M led by Founders Fund (July 2022, $250M valuation)
  - Other investors: General Catalyst, 8VC, Caffeinated Capital, Elad Gil
- Customers: 4,600+ companies (as of early 2023, growing to 1,700+ active scaling accounts)
- 70% of recent YCombinator graduates use Pulley
- Pricing: Free for early-stage; $10/stakeholder/month at scale

**Products:**
- Cap Table Management: Full equity tracking (ISOs, NSOs, RSUs, RSAs, warrants, SAFEs)
- 409A Valuations: 3-day turnaround, in-house valuation team, IRS/AICPA/SEC compliant
- Scenario Modeling: Fundraising round modeling, waterfall analysis
- SBC Reporting: ASC 718 compliance, GAAP and IFRS support
- Employee Portal: Self-serve equity view, option exercise requests
- Investor Portal: Fundraising document issuance, wire collection
- Token Cap Tables: Crypto/Web3 equity management

**Confirmed PSPs / Payment Rails:**
- Stripe: Primary payment processor for all billing and ACH option exercises
- Plaid: Bank account linking for senders (ACH)
- ACH: Digital transfers for U.S. bank accounts only, 5-7 day settlement
- Wire Transfer: Manual fallback for international exercises
- No payment orchestrator detected
- No local APMs detected

**Stripe as Investor:**
- Stripe led Pulley's $10M Series A in October 2020
- Stripe participated again in the $40M Series B in 2022
- Stripe is both an investor and the sole payment processor, deepening lock-in

**Key Payment Challenges:**
- U.S.-only ACH: International employees cannot exercise options digitally
- Manual wire transfers: Costly ($15-$50), slow, require offline coordination
- Single-currency settlement: All payments processed in USD, international employees bear FX costs
- 5-7 day ACH settlement: Slow for time-sensitive option exercises
- Single-processor dependency: Stripe handles all billing and payment flows
- No local payment methods for global shareholders

**Competitive Landscape:**
- Carta: Market leader, deeper feature set, higher pricing (30-50% more expensive)
- AngelList Stack: Fund administration focus, migrating equity customers
- Shareworks (Morgan Stanley): Enterprise and pre-IPO companies
- Ledgy: European-focused alternative with multi-currency support
- Cake Equity: APAC-focused challenger
- Eqvista: Budget alternative

**Key Meeting Angles:**
1. **Stripe-backed, Stripe-dependent** | Stripe led both funding rounds and is the sole processor. Yuno adds optionality without replacing Stripe, creating redundancy for a strategic investor relationship.
2. **4,600+ companies, U.S.-only payments** | Global employees holding equity cannot exercise digitally. Local APMs would unlock instant option exercises in every market.
3. **70% YC penetration = global footprint** | YC companies operate worldwide. Their international employees need local payment rails for equity transactions.
4. **Wire transfer elimination** | Replacing $15-$50 manual wires with instant local methods (SEPA, Pix, UPI) dramatically improves the exercise experience.
5. **Multi-currency settlement** | Processing exercises in local currency eliminates FX losses for international shareholders.
6. **5-7 day settlement risk** | Instant payment rails reduce settlement windows from days to seconds during volatile market conditions.

**Sources:**
- [Pulley Official Website](https://pulley.com/)
- [Pulley Help Center: Payment Methods](https://help.pulley.com/en/articles/5225575-how-can-i-pay-on-pulley)
- [Pulley Help Center: Exercise Requests](https://help.pulley.com/en/articles/4781388-how-to-set-up-exercise-requests-for-your-company-on-pulley)
- [Stripe Invests in Pulley (Fortune)](https://fortune.com/2020/10/21/pulley-cap-table-startup-series-a-carta-stripe/)
- [Pulley Series B (TechCrunch)](https://techcrunch.com/2022/07/13/founders-fund-pulley-series-b-equity/)
- [Pulley Crunchbase](https://www.crunchbase.com/organization/pulley)
- [Pulley YCombinator Profile](https://www.ycombinator.com/companies/pulley)
- [Pulley vs Carta (VC Beast)](https://vcbeast.com/pulley-vs-carta)
- [Pulley Business Breakdown (Contrary Research)](https://research.contrary.com/company/pulley)
- [Pulley Competitors (CB Insights)](https://www.cbinsights.com/research/pulley-competitors-carta-angellist-shareworks-capshare-trica/)
- [Pulley Mercury Partnership](https://mercury.com/raise/software-stack/tools/pulley)
- [Pulley Brandfetch Logo](https://brandfetch.com/pulley.com)
- [Pulley Pricing](https://pulley.com/pricing)
- [Pulley TechCrunch Disrupt 2025](https://pulley2025.pulley.com/blog-posts/make-equity-your-motivation-engine-techcrunch-disrupt-2025)
