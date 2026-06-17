# RECURLY | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Recurly
═══════════════════════════════════════

Logo: https://asset.brandfetch.io/idqIMAfv2h/idL4Ky1Wwv.svg
Nombre merchant: Recurly

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Gateway Routing Ceiling
Tittle_Pain Point_2: LATAM & APAC APM Gaps
Tittle_Pain Point_3: Own Gateway Limits
Tittle_Pain Point_4: Token Migration Friction
Tittle_Pain Point_5: Fraud Rate Climbing

Desc_Pain Point_1: Routes across 18 gateways but lacks real-time per-transaction optimization. Static routing rules leave 3-10% in auth uplift unrealized on $15B annual volume.
Desc_Pain Point_2: SEPA and iDEAL work in Europe, but LATAM and APAC rely on Ebanx alone. Pix Automatico and UPI AutoPay are new with limited merchant adoption.
Desc_Pain Point_3: Own US gateway handles basic card processing but cannot match Stripe or Adyen on global reach, local acquiring, or 3DS optimization for 549 merchants.
Desc_Pain Point_4: Merchants adding gateways face token migration complexity. Moving credentials between Stripe, Adyen, and Braintree risks declined renewals during cutover.
Desc_Pain Point_5: Fraud rose 29% YoY across Recurly's merchants. APM transactions show 1.5% lower fraud declines vs. cards, but most merchants lack local APM coverage.

SLIDE 1: PSP TOPOLOGY

PSP_1: Recurly Gateway (own)
PSP_2: Stripe
PSP_3: Adyen
PSP_4: Braintree
PSP_5: Worldpay
PSP_6: Cybersource
PSP_7: Checkout.com
PSP_8: PayPal Complete
PSP_9: GoCardless
PSP_10: Ebanx

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix (native, not Ebanx)
Local_M_2: OXXO
Local_M_3: PSE
Local_M_4: Nequi
Local_M_5: GCash
Local_M_6: Maya
Local_M_7: KakaoPay
Local_M_8: LINE Pay
Local_M_9: Mada
Local_M_10: STC Pay

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing Layer
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: 1,000+ Local APMs
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Sits between Recurly and its 18 gateways as a real-time routing engine. Per-transaction decisioning by card BIN, issuer, country, and historical success rate. Across $15B in annual volume, a 3% auth uplift recovers $450M+ in approved payments for Recurly's merchants.
Desc_Yuno_Cap2: When any gateway declines, Yuno cascades to the next best acquirer in milliseconds. With 100M active subscribers renewing across Recurly, recovering even 50% of failed charges directly reduces the $129B involuntary churn problem Recurly's own research quantifies.
Desc_Yuno_Cap3: Adds OXXO, PSE, Nequi, GCash, Maya, KakaoPay, LINE Pay, Mada, and hundreds more that Recurly's current stack cannot reach. One integration, instant coverage in 40+ markets. Fills the LATAM/APAC gap without adding individual gateway contracts.
Desc_Yuno_Cap4: Single dashboard unifying all of Recurly's gateways (Stripe, Adyen, Braintree, Worldpay, Cybersource, Checkout.com, and more). Real-time auth monitoring, centralized reconciliation, and NOVA anomaly detection across every processor and market at millisecond speed.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Recurly at a glance:**
- Subscription management and recurring billing SaaS platform
- Founded: 2010 by Dan Burkhart, Tim Van Loan, Isaac Hall. HQ: San Francisco, CA
- Majority owned by Accel-KKR (PE, since August 2020)
- Annual payment volume: $15B (2025)
- Active subscribers managed: ~100M across 2,200+ brands
- Employees: ~350 (2025), up to ~1,100 including contractors/extended team
- Total funding: $39.2M over 7 rounds (Seed through Series C + Accel-KKR majority investment)
- Recent acquisitions: Redfast (May 2025, now Recurly Engage) and Prive (May 2025, Shopify subscription platform)
- Key product: Recurly Subscription Management (RSM), Recurly Compass (AI growth engine)
- Pricing: Starter $249/mo + 0.9% overage; Enterprise from $1,200/mo + negotiated rates; 1.25% + $0.10 per card/PayPal/Amazon transaction

**Notable customers:**
- Streaming/Media: Paramount+, Twitch, Vice Media
- Consumer: BarkBox, Nuuly, Calm
- SaaS: HubSpot, GitLab, Lucidchart, Braze, Bazaarvoice
- Gaming: Epic Games, Roblox (reported)
- Education: Coursera
- Other: Alaska Airlines, VMware/Broadcom
- 549 companies total, 34 with $1B+ revenue

**Confirmed PSP integrations (18 gateways):**
- Recurly Gateway (own, US-only, basic card processing)
- Stripe, Adyen, Braintree, Worldpay, Cybersource, Checkout.com
- PayPal Complete, Amazon Pay, GoCardless
- Ebanx (LATAM/India specialist)
- Commerce Hub (Fiserv/First Data), Chase Paymentech Orbital, TSYS
- CardConnect, Check Commerce, FreedomPay, Nuvei

**Payment methods supported:**
- Cards: Visa, MC, Amex, Discover, JCB, Diners, UnionPay
- Wallets: Apple Pay, Google Pay, Amazon Pay, PayPal
- Direct Debit: SEPA, ACH, BECS (AU), Bacs (UK) via GoCardless
- Local EU: iDEAL, Sofort, Bancontact
- LATAM: Pix Automatico, Mercado Pago (via Ebanx, limited)
- APAC: UPI AutoPay (via Ebanx, limited)
- BNPL: Not natively offered

**Geographic distribution of Recurly's customers:**
- United States: 373 (68%)
- United Kingdom: 39 (7%)
- Canada: 27 (5%)
- India: 14, Australia: 10, Germany: 7, France: 7
- Rest of world: ~72

**Key market gaps for Recurly's merchant base:**

MARKET 1: Latin America (Brazil, Mexico, Colombia)
  Have: Pix Automatico and Mercado Pago via Ebanx (limited adoption)
  Missing: OXXO, SPEI, PSE, Nequi, Boleto (offline), PIX native routing
  Recurly's LATAM coverage depends entirely on a single provider (Ebanx)

MARKET 2: Asia Pacific (India, Philippines, Japan, Korea)
  Have: UPI AutoPay via Ebanx (recent, limited)
  Missing: GCash, Maya, Konbini, KakaoPay, LINE Pay, Paytm, PhonePe
  APAC is the fastest growing subscription market. Recurly has minimal coverage

MARKET 3: Middle East (UAE, Saudi Arabia)
  Have: Nothing local
  Missing: Mada, STC Pay, Apple Pay (local), Tabby
  Zero gateway or APM coverage in the Gulf region

MARKET 4: Europe (mature but gaps remain)
  Have: SEPA, iDEAL, Sofort, Bancontact, GoCardless for direct debit
  Missing: Swish (Sweden), MobilePay (Denmark), Vipps (Norway), Twint (Switzerland)
  Nordics and Switzerland lack local APM coverage despite high subscription adoption

MARKET 5: Africa
  Have: Nothing
  Missing: M-Pesa, Airtel Money, MTN Mobile Money, Flutterwave, Paystack
  Zero coverage in a continent with 600M+ mobile money users

**Recurly's own data on failed payments:**
- $129B estimated industry cost of involuntary churn in 2025 (Recurly research)
- 100% of subscription businesses impacted by failed payments
- 48% of subscribers would cancel due to billing issues
- Recurly recovers 55.4% of failed transactions via ML retries (industry leading)
- Free trial conversion declined from 46% (2021) to 33% (2024)
- Customer acquisition rate dropped from 4.1% (2021) to 2.8% (2024)
- Fraud increased 29% YoY across Recurly's merchant base
- APM transactions show 1.5% lower fraud decline rate vs. cards
- 119% revenue lift when merchants enable PayPal; 154% lift with SEPA
- 19% annual growth in APM usage across Recurly's merchant base

**Key meeting angles:**
1. **Partnership play**: Yuno as a routing/orchestration layer underneath Recurly's billing, not competing but enhancing. Yuno routes, Recurly bills
2. **$15B volume opportunity**: Even 1% auth uplift across $15B = $150M in recovered payments for Recurly's merchants. Smart Routing can deliver 3-10%
3. **LATAM/APAC gap fill**: Recurly's Ebanx dependency for LATAM and APAC is a single point of failure. Yuno adds 300+ connections in those regions
4. **Involuntary churn reduction**: Recurly's own research quantifies $129B in losses. Yuno failover adds a second and third acquirer path for every renewal
5. **AI + Smart Routing synergy**: Recurly Compass does AI for engagement; Yuno does AI for payment routing. Complementary, not competitive
6. **Merchant value add**: Recurly's 549 merchants become Yuno's distribution channel. Every merchant that activates Yuno gets better auth rates through Recurly
7. **Token portability**: Yuno handles token migration across gateways, solving the friction that locks Recurly merchants into suboptimal routing

**Recent news and developments:**
- May 2025: Acquired Redfast (subscriber engagement) and Prive (Shopify subscriptions)
- October 2025: Appointed Matt Schurk as Chief Revenue Officer
- July 2025: Appointed Eric Steele as CFO
- October 2025: Launched Recurly Compass (AI-powered growth engine) with 50+ new tools
- December 2025: Deepened Shopify partnership for ecommerce subscription management
- Won SubSummit "Best Subscription Management Platform 2025" award

**Sources:**
- [Recurly Official Website](https://recurly.com/)
- [Recurly Payment Gateways Documentation](https://docs.recurly.com/recurly-subscriptions/docs/payment-gateways-1)
- [Recurly Payment Methods](https://docs.recurly.com/docs/payment-methods)
- [Recurly Alternative Payment Methods](https://recurly.com/product/alternative-payment-methods/)
- [Recurly Payment Orchestration](https://recurly.com/product/payments-orchestration/)
- [Recurly Pricing](https://recurly.com/pricing/)
- [Recurly Customers](https://recurly.com/customers/)
- [Recurly Global Expansion](https://recurly.com/product/global-expansion/)
- [Recurly $129B Failed Payments Report](https://recurly.com/press/failed-payments-could-cost-subscription-companies-more-than-129-billion-in-2025-us/)
- [Recurly Redfast/Prive Acquisitions](https://www.businesswire.com/news/home/20250507475204/en/)
- [Recurly AI Launch](https://www.businesswire.com/news/home/20251016445471/en/)
- [Recurly Shopify Partnership](https://www.businesswire.com/news/home/20251209297490/en/)
- [Recurly Accel-KKR Investment](https://recurly.com/blog/recurly-secures-majority-equity-investment-from-accel-kkr/)
- [ElectroIQ: Recurly Statistics 2025](https://electroiq.com/stats/recurly-statistics/)
- [Growjo: Recurly Revenue](https://growjo.com/company/Recurly)
- [Crunchbase: Recurly](https://www.crunchbase.com/organization/recurly)
- [Brandfetch: Recurly Logo](https://brandfetch.com/recurly.com)
- [Enlyft: Companies Using Recurly](https://enlyft.com/tech/products/recurly)
