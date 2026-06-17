# Dribbble | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-28*

```
=======================================
DATABASE FIELDS: Dribbble
=======================================

Logo: https://cdn.dribbble.com/assets/dribbble-ball-mark-2bd45f09c2fb58dbbfb44766d5d1d07c5a012323a4541bd3a833d62cdc78fd9c.svg
Nombre merchant: Dribbble

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Single PSP Dependency
Tittle_Pain Point_2: Limited APMs at Checkout
Tittle_Pain Point_3: No Smart Routing
Tittle_Pain Point_4: Marketplace Payout Friction
Tittle_Pain Point_5: Pro Renewal Decline Risk

Desc_Pain Point_1: Dribbble runs Pro, Marketplace, and Projects through Stripe alone. A single PSP is a single point of failure for renewals, fees, and designer payouts.
Desc_Pain Point_2: Dribbble docs state cards and PayPal only for subscriptions. ACH, wires, and "any other method" are explicitly not supported. PIX, UPI, iDEAL, BLIK absent.
Desc_Pain Point_3: With Stripe as sole acquirer, there is no acquirer-level smart routing per BIN, issuer, or country. A failed renewal or Project payment ends the transaction.
Desc_Pain Point_4: Dribbble runs Projects and Outbound Proposals globally. Designers in LATAM and SE Asia receive USD via Stripe Connect. No PIX, UPI, or local payout rails.
Desc_Pain Point_5: Pro Annual $96 and Pro Monthly $16 renew on schedule. Without orchestration, a single issuer decline kills renewal. Designers churn, dragging Tiny ARR.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (Subscriptions + Marketplace)
PSP_2: PayPal
PSP_3: Apple Pay / Google Pay (via Stripe)
PSP_4: Stripe Connect (Designer Payouts)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: PIX (Brazil)
Local_M_2: Boleto (Brazil)
Local_M_3: OXXO (Mexico)
Local_M_4: UPI (India)
Local_M_5: iDEAL (Netherlands)
Local_M_6: BLIK (Poland)
Local_M_7: SEPA Direct Debit (EU)
Local_M_8: PayPay (Japan)
Local_M_9: KakaoPay (South Korea)
Local_M_10: GrabPay (SE Asia)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing Engine
Tittle_Yuno_Cap2: Failover + NOVA Recovery
Tittle_Yuno_Cap3: 1,000+ Local APMs
Tittle_Yuno_Cap4: Multi-PSP Resilience

Desc_Yuno_Cap1: Route every Pro renewal and every Project payment to the optimal acquirer per BIN, issuer, and country. Yuno keeps Stripe in the mix while adding a second and third acquirer for redundancy. Smart Routing lifts authorization 3 to 10% on global designer subscriptions.
Desc_Yuno_Cap2: When a Stripe renewal fails, Yuno cascades instantly to a backup acquirer or alternative method. NOVA AI recovers up to 75% of soft declines before the designer sees a churn flag. Livelo recovered 50% of failed transactions using cascading retries.
Desc_Yuno_Cap3: Open PIX, Boleto, OXXO, UPI, iDEAL, BLIK, PayPay, and KakaoPay for Dribbble Pro and Marketplace via one API. InDrive launched 10 LATAM markets in under 8 months. Dribbble can bring local payment methods to designers across 50+ countries without rebuilding checkout.
Desc_Yuno_Cap4: Yuno orchestrates across multiple PSPs and acquirers. Dribbble keeps Stripe and adds resilience: a second acquirer in EU, a regional acquirer in LATAM, and APM rails in APAC. One vault, one dashboard, one integration. No vendor lock-in for Tiny's Creative Platform segment.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Dribbble at a glance:**
- Online community and marketplace for designers and creative professionals
- Acquired by Tiny Ltd (TSX-V: TINY) in January 2017 for $5.5M (70% stake)
- Tiny FY2024 Revenue: $194.2M (up 5% YoY). Recurring revenue $38.7M (up 30%)
- Dribbble core: Shot portfolios, design feedback, job board, Pro subscriptions, Marketplace, Projects (client transactions)
- Reported 12M+ users (post Creative Market acquisition era)
- Dribbble Pro Annual: $96/year (or $16/month for Monthly plan). 0% Designer Platform Fees on Projects with Pro Annual
- Marketplace fee: 3.5% standard platform fee on services
- 2026 launch: Outbound Proposals enable transactions outside the platform with no platform fee, using Dribbble's contracts, payments, and workflow features
- Tiny's Creative Platform segment includes Dribbble plus Creative Market (digital assets marketplace)

**Confirmed PSPs and Payment Infrastructure:**
- Stripe: Confirmed primary PSP for subscriptions, marketplace, and project payments. Dribbble support docs explicitly state "Dribbble processes payments through Stripe"
- PayPal: Accepted for most subscription products
- Apple Pay / Google Pay: Available via Stripe at checkout where supported
- Stripe Connect: Used for designer payouts (Project payouts and Outbound Proposals)
- Not accepted: ACH bank transfers, money wires, "any other payment method" (per Dribbble support)
- No payment orchestration platform (no Spreedly, Primer, Gr4vy, CellPoint, APEXX, or Yuno)

**Payment Methods by Region:**

REGION: Americas (US, Canada, Brazil, Mexico, Argentina)
  Accepted: Visa, Mastercard, Amex, Discover (via Stripe), PayPal, Apple Pay / Google Pay (where supported)
  Missing: PIX (Brazil), Boleto, OXXO (Mexico), SPEI, Mercado Pago, Cash App Pay, Venmo
  Note: LATAM designer base relies on international cards. No local rails for paying or receiving payouts

REGION: EMEA
  Accepted: Visa, Mastercard, Amex, PayPal, Apple Pay / Google Pay
  Missing: SEPA Direct Debit (recurring), iDEAL (Netherlands), BLIK (Poland), Bancontact (Belgium), Trustly (Nordics), Open Banking, Twint (Switzerland)
  Note: Stripe supports many of these; Dribbble's checkout configuration historically limits to cards plus PayPal

REGION: Asia (Japan, India, SE Asia, Korea)
  Accepted: Visa, Mastercard, Amex, PayPal, Apple Pay / Google Pay
  Missing: PayPay (Japan), Konbini, KakaoPay, NaverPay, Toss, UPI (India), GrabPay, GCash, DANA, Alipay/WeChat Pay
  Note: Significant designer talent base in India and SE Asia with no local rails for Pro subscriptions

**Payment Issues and Incidents:**
- Single PSP risk: With Stripe as the sole acquirer, any issuer-level decline ends the transaction. No cascade to a secondary processor
- Limited recurring methods: Dribbble explicitly states ACH, wires, and "any other payment method" are not accepted for subscriptions, capping payment options vs orchestrated competitors
- Subscription expiration: Pro expiration removes 0% Designer Platform Fee benefit. Designers who churn lose marketplace economics, raising churn cost
- Payment method changes locked between billing cycles per support docs ("Changing Your Pro Subscription Billing between Monthly and Annual")
- Marketplace transaction friction: Project payments rely on Stripe rails; cross-border payouts to designers in LATAM and SE Asia subject to FX, withdrawal fees, and Stripe Connect availability per country

**Key meeting angles:**
1. **Single-PSP risk on Tiny's recurring revenue line** | Dribbble drives Tiny's $38.7M (and growing 30%) recurring revenue. With Stripe as the sole acquirer, every issuer decline becomes lost ARR. NOVA AI recovers up to 75% of soft declines. Adding orchestration protects Tiny's fastest growing segment.
2. **Pro and Marketplace need local rails to expand globally** | Dribbble has 12M+ users globally but checkout is card and PayPal only. PIX, UPI, OXXO, BLIK, and PayPay are missing. Yuno activates 1,000+ local methods through one API.
3. **Designer payouts: cash flow is the product** | Outbound Proposals (2026) and Projects depend on fast, low-friction payouts. Stripe Connect alone limits FX and rail options. Yuno enables localized payout flows alongside acquirer redundancy.
4. **Tiny's public reporting requires resilience** | Tiny is publicly listed. A Stripe outage or issuer block hits Dribbble's reported recurring revenue. Multi-PSP orchestration is a board-level operational hedge.
5. **3.5% marketplace fee is real margin; auth uplift compounds** | Marketplace contribution is fee-based on volume. A 3 to 10% auth lift via Smart Routing directly increases the volume on which fees are charged, expanding GMV without new acquisition spend.

**Dribbble & Tiny Leadership:**
- Andrew Wilkinson: Founder and Chairman, Tiny Ltd. Architect of Tiny's HoldCo strategy
- Chris Sparling: Co-founder, Tiny Ltd
- Constantin Koshcheev: CEO, Dribbble (current per LinkedIn)
- Tiny is publicly traded on TSX-V under ticker TINY
- A. Wilkinson Holdings Ltd owns ~29.7% of Tiny shares (as of July 29, 2025)

**Recent corporate developments:**
- April 2026: Dribbble Stories "Work In Progress, Part 16" published. Active product roadmap commentary
- 2026: Outbound Proposals launched, allowing transactions with off-platform clients using Dribbble's contracts, payments, and workflow
- April 2025: Tiny raised $20M through bought deal offering
- FY2024: Tiny Ltd revenue $194.2M (up 5%). Recurring revenue $38.7M (up 30%)
- 2017: Dribbble acquired by Tiny ($5.5M for 70%)
- 2020: Dribbble acquired Creative Market, growing to 12M+ users

**Sources:**
- [Dribbble Pro (Dribbble)](https://dribbble.com/pro)
- [Dribbble Work In Progress Part 16 (Dribbble)](https://dribbble.com/stories/2026/04/07/work-in-progress-part-16)
- [Dribbble Payment Methods (Support)](https://support.dribbble.com/hc/en-us/articles/360056372934-What-payment-methods-do-you-accept)
- [Dribbble Pricing and Refund Policies (Support)](https://support.dribbble.com/hc/en-us/articles/25939443069335-Dribbble-Pricing-and-Refund-Policies)
- [Dribbble Billing (Support)](https://support.dribbble.com/hc/en-us/sections/360011281953-Billing)
- [Dribbble Making Payments (Support)](https://support.dribbble.com/hc/en-us/articles/25975529530391-Making-Payments-on-Dribbble)
- [Dribbble Payout Options for Projects (Support)](https://support.dribbble.com/hc/en-us/articles/27466606224535-Payout-Options-for-Dribbble-Projects)
- [Dribbble Changing Pro Billing (Support)](https://support.dribbble.com/hc/en-us/articles/360056676154-Changing-Your-Pro-Subscription-Billing-between-Monthly-and-Annual)
- [Dribbble Pro Subscription Expiration (Support)](https://support.dribbble.com/hc/en-us/articles/360056674914-What-happens-when-my-Pro-subscription-expires)
- [Dribbble Pro Pricing 2026 (ITQlick)](https://www.itqlick.com/dribbble/pricing)
- [Pay with Stripe Dribbble Blog (Dribbble)](https://dribbble.com/stories/2013/03/07/pay-with-stripe)
- [Dribbble Acquires Creative Market (TechCrunch)](https://techcrunch.com/2020/04/30/dribbble-a-bootstrapped-linkedin-for-designers-acquires-creative-market-grows-to-12m-users/)
- [Dribbble Business Model (Vizologi)](https://vizologi.com/business-strategy-canvas/dribbble-business-model-canvas/?lang=en)
- [Dribbble Insights (Accio)](https://www.accio.com/business/dribbble)
- [Dribbble 2026 Company Profile (Tracxn)](https://tracxn.com/d/companies/dribbble/__Egibn7XgaSOanDzkDqMM9UvnPIqw5lAwOJaOvJJf-eg)
- [Tiny Acquisition of Dribbble (Capital Buddha)](https://capitalbuddha.substack.com/p/tiny-acquisition-of-dribbble-yes)
- [Tiny Capital Financial Teardown (SBO)](https://sbo.financial/blog/financial-teardowns/tiny-capital-financial-teardown/)
- [Tiny Securities Disposition Plan (StockTitan)](https://www.stocktitan.net/news/TNYZF/tiny-announces-the-establishment-of-an-automatic-securities-jpqixg1ayd0i.html)
- [Dribbble's New Features Client Transaction (DesignMonks)](https://www.designmonks.co/blog/dribbbles-new-features-client-transaction)
