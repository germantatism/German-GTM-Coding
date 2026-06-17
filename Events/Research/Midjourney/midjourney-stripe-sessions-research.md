# MIDJOURNEY | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Midjourney
=======================================

Logo: https://upload.wikimedia.org/wikipedia/commons/e/e6/Midjourney_Emblem.svg
Nombre merchant: Midjourney

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: USD-Only Pricing Wall
Tittle_Pain Point_2: Single Acquirer Exposure
Tittle_Pain Point_3: Emerging Market Lockout
Tittle_Pain Point_4: No Wallet or Bank Options
Tittle_Pain Point_5: Enterprise Billing Gap

Desc_Pain Point_1: All plans billed in USD only. 60% of users are international, paying FX fees every renewal. Korea (8.3%), Brazil (4.75%), and India (4.65%) absorb 2-4% markup per billing cycle.
Desc_Pain Point_2: Stripe is the sole processor for all subscriptions. At $500M+ revenue and 20M users, any Stripe outage blocks 100% of new sign-ups, renewals, and upgrades across all markets.
Desc_Pain Point_3: India, Turkey, Russia, and parts of Africa and Middle East face BIN-level payment blocks. Users resort to virtual cards and crypto workarounds to subscribe.
Desc_Pain Point_4: Only cards plus limited wallets (Apple Pay, Google Pay, Alipay in some regions). No PayPal or bank transfers. Korea has no KakaoPay, Brazil no Pix, India no UPI.
Desc_Pain Point_5: Enterprise plans launching in 2026 for creative agencies targeting $600M ARR. Enterprise needs invoicing and multi-seat billing that Stripe consumer checkout cannot deliver.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (sole processor, all billing)
PSP_2: Apple Pay (via Stripe, limited regions)
PSP_3: Google Pay (via Stripe, limited regions)
PSP_4: Alipay (via Stripe, limited regions)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: KakaoPay (South Korea)
Local_M_2: Pix (Brazil)
Local_M_3: UPI (India)
Local_M_4: Konbini (Japan)
Local_M_5: BLIK (Poland)
Local_M_6: OXXO (Mexico)
Local_M_7: Boleto (Brazil)
Local_M_8: GCash (Philippines)
Local_M_9: SEPA Direct Debit (EU)
Local_M_10: iDEAL (Netherlands)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each subscription to the optimal acquirer by card BIN and issuer. At $500M+ revenue across 20M users in 100+ countries, a 3% auth uplift recovers $15M+ yearly. Smart routing eliminates FX-triggered declines for 60% international base.
Desc_Yuno_Cap2: Automatic cascade eliminates total Stripe dependency. When Stripe declines, Yuno reroutes in milliseconds. Renewals convert instead of churning. Up to 50% recovery on failed transactions, protecting GPU-time revenue across all tiers.
Desc_Yuno_Cap3: Activates local rails for global creators: KakaoPay in Korea (#2 market), Pix in Brazil (#4), UPI in India (#5), Konbini in Japan, BLIK in Poland, OXXO in Mexico, GCash in Philippines, SEPA DD and iDEAL in Europe. One API, 1,000+ methods.
Desc_Yuno_Cap4: One dashboard for subscription, enterprise invoicing, and credit billing. Real-time approval monitoring by market and tier. NOVA fraud engine with 75% fewer false positives, replacing Stripe-only detection blocking legitimate users.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Midjourney at a glance:**
- Founded: 2021 by David Holz (ex-Leap Motion co-founder)
- Headquarters: San Francisco, CA (independent research lab)
- Revenue: $500M in 2025 (up from $300M in 2024); ARR forecast $500M-$600M for 2026
- Valuation: $10.5B (private market estimate); zero external funding raised
- Registered Users: ~19.83M (Jan 2026), projected 21M-25M by end of 2026
- Employees: ~40 (extremely lean operation for revenue scale)
- Profitability: Profitable since early operations with zero venture funding
- Billing model: GPU-time based subscriptions ($10-$120/mo across 4 tiers)

**Products:**
- Midjourney v6/v7: Text-to-image generation (core product)
- Web Application: Standalone platform (reducing Discord dependency)
- Basic Plan: $10/mo (3.3 fast GPU hours)
- Standard Plan: $30/mo (15 fast GPU hours)
- Pro Plan: $60/mo (30 fast GPU hours)
- Mega Plan: $120/mo (60 fast GPU hours)
- Enterprise Plans: New tier launching 2026 for creative agencies
- Annual billing: 20% discount (selected by default)

**Confirmed PSPs / Payment Rails:**
- Stripe: Sole payment processor (PCI Level 1, confirmed in Midjourney docs)
- Apple Pay: Supported via Stripe in select regions
- Google Pay: Supported via Stripe in select regions
- Amazon Pay: Mentioned in some documentation
- Alipay: Available in select regions via Stripe
- Link (Stripe): Accelerated checkout
- No PayPal accepted
- No bank transfers accepted
- No BNPL options
- No payment orchestrator detected

**Geographic Distribution (Top Markets by Traffic):**
- #1 United States: 17.24%
- #2 South Korea: 8.30% (strong creative/design market)
- #3 United Kingdom: 4.24%
- #4 Brazil: 4.75%
- #5 India: 4.65%
- #6 Germany: 4.01%
- 60% of users are international (outside the U.S.)
- Transitioning from Discord-only to standalone web app to lower entry barriers

**Key Payment Challenges:**
- USD-only billing forces international users to pay FX conversion fees on every transaction
- India, Turkey, Russia, parts of Africa/Middle East face Stripe BIN-level blocks
- "Unsuccessful Payments" is a dedicated help page indicating systemic decline issues
- Users openly resort to virtual cards and crypto workarounds to subscribe
- No PayPal option forces card-only checkout globally
- Enterprise tier launch requires billing capabilities Stripe consumer checkout cannot provide

**Key Meeting Angles:**
1. **$500M revenue, zero external funding, 40 employees** | Midjourney is uniquely profitable and lean. Every basis point of payment optimization flows directly to the bottom line.
2. **60% international, USD-only** | Majority of revenue comes from users paying cross-border FX markups. Local currency pricing via orchestration unlocks pricing flexibility.
3. **Korea is #2 market with zero KakaoPay** | 8.3% of traffic from a market where 90%+ of mobile payments use KakaoPay or Naver Pay. Massive conversion gap.
4. **Emerging market lockout** | India, Turkey, and other high-growth creative markets are systematically blocked by Stripe BIN restrictions. These are Midjourney's natural growth markets.
5. **Enterprise tier launching 2026** | New creative agency plans need invoicing, PO management, and multi-seat billing. Orchestration layer enables enterprise-grade billing without rebuilding infrastructure.
6. **Zero VC pressure, pure upside** | No investors to satisfy means Midjourney can evaluate payment optimization purely on revenue impact, not board mandates.
7. **Discord to web migration** | Moving to standalone web app is the perfect moment to upgrade payment infrastructure alongside the platform transition.

**Sources:**
- [Midjourney Accepted Payment Methods (Docs)](https://docs.midjourney.com/hc/en-us/articles/27868831972365-Accepted-Payment-Methods)
- [Midjourney Payment Currency (Docs)](https://docs.midjourney.com/hc/en-us/articles/27868831424525-Payment-Currency)
- [Midjourney Unsuccessful Payments (Docs)](https://docs.midjourney.com/hc/en-us/articles/27868801964045-Unsuccessful-Payments)
- [Midjourney Comparing Plans (Docs)](https://docs.midjourney.com/hc/en-us/articles/27870484040333-Comparing-Midjourney-Plans)
- [Midjourney Billing Model (Dodo Payments)](https://dodopayments.com/blogs/midjourney-billing-model)
- [Midjourney Statistics 2026 (DemandSage)](https://www.demandsage.com/midjourney-statistics/)
- [Midjourney Revenue $500M (GetLatka)](https://getlatka.com/companies/midjourney)
- [Midjourney Revenue and Valuation (Sacra)](https://sacra.com/c/midjourney/)
- [Midjourney Statistics 2026 (TwinStrata)](https://www.twinstrata.com/midjourney-statistics/)
- [Midjourney Traffic Analytics (SimilarWeb)](https://www.similarweb.com/website/midjourney.com/)
- [Midjourney Statistics (WorldMetrics)](https://worldmetrics.org/midjourney-statistics/)
- [Midjourney Payment Problems Fix (EliteAIPrompts)](https://www.eliteaiprompts.com/trouble-with-midjourney-subscription-payment-heres-how-to-fix-it/)
- [Midjourney Logo (Wikimedia Commons)](https://commons.wikimedia.org/wiki/File:Midjourney_Emblem.svg)
