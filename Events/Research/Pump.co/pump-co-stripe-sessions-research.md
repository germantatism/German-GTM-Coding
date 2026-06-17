# PUMP.CO | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Pump.co
=======================================

Logo: https://asset.brandfetch.io/id_x3LhOH/idMf4Qqv7p.png
Nombre merchant: Pump.co

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Revenue Tied to AWS Only
Tittle_Pain Point_2: Global Billing Gaps
Tittle_Pain Point_3: Free Model Cash Lag
Tittle_Pain Point_4: Single Processor Risk
Tittle_Pain Point_5: Multi-Cloud Payout Drag

Desc_Pain Point_1: 100% of Pump's revenue comes from AWS volume discounts. As GCP and Azure customers grow, Pump needs payment infrastructure that handles multi-cloud billing across providers with different payout cycles and currencies.
Desc_Pain Point_2: Pump serves 200+ customers globally but processes all billing through U.S.-centric rails. International startups paying for cloud optimization lack local payment methods. No Pix, SEPA, or UPI option exists for non-U.S. customers.
Desc_Pain Point_3: Pump monetizes by capturing a percentage of savings delivered. Revenue recognition lags behind cloud consumption cycles. Payment collection from international clients adds FX conversion fees that compress already thin margins.
Desc_Pain Point_4: Stripe handles all subscription billing for the platform. Any Stripe degradation blocks revenue collection from the entire 200+ customer base. No backup processor exists to maintain billing continuity during outages.
Desc_Pain Point_5: Expanding from AWS to GCP and Azure means reconciling payouts from three cloud providers across different billing cycles. Without unified payment orchestration, finance teams manually track revenue splits across providers and currencies.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (primary billing processor)
PSP_2: AWS Consolidated Billing (group buying mechanism)
PSP_3: ACH (U.S. bank transfers)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix (Brazil)
Local_M_2: SEPA Direct Debit (EU)
Local_M_3: UPI (India)
Local_M_4: iDEAL (Netherlands)
Local_M_5: BLIK (Poland)
Local_M_6: Boleto (Brazil)
Local_M_7: KakaoPay (South Korea)
Local_M_8: OXXO (Mexico)
Local_M_9: Bancontact (Belgium)
Local_M_10: PayPay (Japan)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each billing transaction to the optimal acquirer by customer geography and currency. As Pump scales past $15M ARR with global customers, smart routing maximizes approval rates on every subscription charge. 3% to 10% auth uplift on cross-border payments.
Desc_Yuno_Cap2: Automatic cascade eliminates single-Stripe dependency. When Stripe declines, Yuno reroutes in milliseconds to a backup processor. Subscription renewals convert instead of churning. Up to 50% recovery on failed transactions across all billing streams.
Desc_Yuno_Cap3: Activates the local rails global startups prefer: Pix in Brazil, SEPA DD across Europe, UPI in India, iDEAL in Netherlands, BLIK in Poland, KakaoPay in Korea. One API, 1,000+ methods, zero per-market builds for customers on every continent.
Desc_Yuno_Cap4: One dashboard unifying Stripe billing, AWS payouts, and multi-cloud revenue reconciliation. Real-time monitoring across GCP, Azure, and AWS billing streams. NOVA fraud engine with 75% fewer false positives. Centralized analytics for 200+ customer accounts.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Pump.co at a glance:**
- Founded: March 2022 by Spandana Nakka (ex-founder of Sleek, acquired by Snackpass in 2021)
- Headquarters: San Francisco, California
- CEO: Spandana Nakka
- Employees: 76 to 81
- Y Combinator batch company
- Forbes AI 50: Named among America's 50 most promising AI companies
- AWS Advanced Tier Partner (fewer than 1,000 companies worldwide)
- Revenue: $15.2M (as of April 2025)
- ARR: $10M+ within two years of founding
- Valuation: $1.5B (2025)
- Customers: 200+ (including 50+ YC companies)
- Customer savings: $12M+ collectively saved on cloud expenses
- Funding: $14M raised (investors include DG Daiwa Ventures, Failup Ventures, Leonis Investissement, OneValley)

**Products:**
- AWS Cost Optimization: Group buying for reserved instances and savings plans (20-60% savings)
- GCP Cost Optimization: Extending group buying model to Google Cloud
- Azure Cost Optimization: Multi-cloud expansion
- Cloud Infrastructure Pricing Calculator: Free tool comparing AWS, GCP, Azure pricing
- AI-Powered Analytics: Continuous scanning and optimization of cloud usage

**Business Model:**
- Free for customers: No subscription fees, no engineering effort required
- Revenue from cloud providers: Pump captures a small percentage of volume discount savings
- Group buying mechanism: Pools customer spend to unlock enterprise-tier pricing
- Customers save 20-40% on average (up to 60% on compute)
- AWS credits compatibility: Free credits last longer through Pump, plus 1-year extension on expiry

**Confirmed PSPs / Payment Rails:**
- Stripe: Primary billing processor for all customer subscriptions
- AWS Consolidated Billing: Group buying mechanism for pooled commitments
- ACH: U.S. bank transfers for domestic customers
- No payment orchestrator detected
- No international/local APMs detected

**Key Payment Challenges:**
- Single-revenue-source dependency: 100% of revenue comes from AWS volume discounts
- U.S.-centric billing: Global customers lack local payment options
- Thin margin compression: FX fees on international collections eat into savings-based revenue
- Single-processor risk: All billing flows through Stripe with no failover
- Multi-cloud billing complexity: GCP and Azure expansion requires reconciling three payout streams
- Revenue lag: Savings-based model means revenue follows cloud consumption cycles

**Competitive Landscape:**
- Antimetal: Direct competitor in group-buying cloud savings
- Cledara: SaaS spending management platform
- CloudZero: Enterprise cloud cost optimization
- CostSage: AI-powered AWS cost reduction (30-65% savings)
- nOps: AWS resource management and automation
- DoiT: Cloud analytics and optimization services

**Key Meeting Angles:**
1. **$15.2M ARR, single-processor dependency** | All revenue flows through Stripe. At $1.5B valuation, payment resilience is critical for investor confidence and growth trajectory.
2. **200+ global customers, U.S.-only billing** | International startups using Pump lack local payment methods. Adding Pix, SEPA, UPI unlocks frictionless billing in key markets.
3. **Multi-cloud expansion needs unified billing** | Moving from AWS-only to GCP and Azure creates three separate billing streams. Orchestration unifies all revenue into one dashboard.
4. **Forbes AI 50 growth trajectory** | Rapid scaling from $10M to $15M+ ARR demands payment infrastructure that grows with the business.
5. **Savings-based revenue model** | Thin margins from percentage-of-savings require minimizing payment processing costs through smart routing.
6. **YC network effect** | 50+ YC companies already on Pump. YC startups operate globally and expect local payment methods.

**Sources:**
- [Pump.co Official Website](https://www.pump.co/)
- [Pump.co YCombinator Profile](https://www.ycombinator.com/companies/pump-co)
- [Pump.co Revenue (GetLatka)](https://getlatka.com/companies/pump.co)
- [Pump.co Crunchbase](https://www.crunchbase.com/organization/pump-b398)
- [How Pump Works (Help Center)](https://help.pump.co/getting-started/how-pump-works)
- [Pump.co AWS Partner Page](https://partners.amazonaws.com/partners/0018W00001wuP0XQAU/Pump)
- [Pump.co Review (Gold Penguin)](https://goldpenguin.org/blog/pump-co-aws-savings-review/)
- [Pump.co Group Buying (NY Weekly)](https://nyweekly.com/tech/pump-co-the-groupon-of-cloud-spend-is-here/)
- [Pump.co Forbes AI 50 (PRWeb)](https://www.prweb.com/releases/Introducing_Pump_co_The_Fastest_way_to_save_60_on_AWS_Spend/prweb19432241.htm)
- [Cloud Cost Optimization Blog (Pump)](https://www.pump.co/blog/cloud-cost-optimization)
- [Pump.co Revenue & Market Share (AEO)](https://aeo.sig.ai/brands/pumpco)
- [Pump Brandfetch Logo](https://brandfetch.com/pump.today)
- [Spandana Nakka LinkedIn](https://www.linkedin.com/in/spndn07)
