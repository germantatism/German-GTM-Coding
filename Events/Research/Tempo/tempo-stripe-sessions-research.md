# TEMPO | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Tempo
═══════════════════════════════════════

Logo: https://asset.brandfetch.io/idBjq2vPcr/idkJ8dx_XI.svg
Nombre merchant: Tempo

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Single Acquirer Lock-In
Tittle_Pain Point_2: US-Only Revenue Ceiling
Tittle_Pain Point_3: Subscription Churn Leak
Tittle_Pain Point_4: Checkout Abandonment Drag
Tittle_Pain Point_5: No Payment Intelligence

Desc_Pain Point_1: All card transactions flow through Stripe with no failover. Any acquirer outage blocks $2,495 Studio purchases and $39/mo renewals for the entire subscriber base with zero cascade to recover revenue.
Desc_Pain Point_2: Tempo ships hardware only in the US and bills exclusively in USD. No international checkout or local currency pricing to tap the $15.5B global home fitness market growing at 7.5% CAGR.
Desc_Pain Point_3: 20-40% of subscription churn is involuntary from declined cards. With $39/mo recurring billing and a mandatory 12-month commitment, every failed renewal erodes the $15M ARR base with no retry logic.
Desc_Pain Point_4: $2,495 Studio and $395 Move bundles rely on Affirm alone for installments with no bank debit or BNPL alternatives. Buyers without eligible credit face friction that kills hardware conversion.
Desc_Pain Point_5: Equipment, subscriptions, and apparel run on separate Shopify storefronts with no unified payment dashboard. No centralized view of auth rates or decline reasons to optimize revenue.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe
PSP_2: Shopify Payments
PSP_3: Affirm
PSP_4: PayPal
PSP_5: Apple Pay
PSP_6: Google Pay
PSP_7: Shop Pay
PSP_8: Meta Pay
PSP_9: Flex (HSA/FSA)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: ACH Direct Debit
Local_M_2: Klarna
Local_M_3: Afterpay
Local_M_4: Venmo
Local_M_5: Cash App Pay
Local_M_6: SEPA Direct Debit
Local_M_7: iDEAL
Local_M_8: Pix
Local_M_9: OXXO
Local_M_10: BLIK

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route every $39/mo subscription renewal and high-ticket equipment purchase to the best performing acquirer per card BIN, issuer, and amount. With a $15M ARR base and premium hardware averaging $1,400+, a 3-10% auth uplift recovers significant revenue on every transaction.
Desc_Yuno_Cap2: When Stripe declines a subscription renewal or equipment charge, Yuno cascades to an alternate acquirer in milliseconds. Recovers up to 50% of failed recurring charges, directly reducing the involuntary churn that erodes the 12-month commitment subscriber base.
Desc_Yuno_Cap3: Unlocks international expansion without engineering sprints: ACH and Venmo for US direct debit, SEPA DD and iDEAL for Europe, Pix for Brazil, OXXO for Mexico. One API, 1,000+ payment methods, ready for when Tempo launches outside the US.
Desc_Yuno_Cap4: Single dashboard consolidating Stripe, Shopify Payments, Affirm, and all wallets into one view. Real-time auth rate monitoring, centralized reconciliation, and anomaly detection via NOVA. Full visibility across equipment, subscriptions, and apparel channels.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Tempo at a glance:**
- Founded: 2015 (originally as SmartSpot), San Francisco, CA
- Y Combinator: Winter 2015 batch
- CEO & Co-Founder: Moawia Eldeeb (Columbia University CS graduate, former personal trainer)
- CTO & Co-Founder: Josh Augustin (Columbia classmate of Eldeeb)
- Total funding raised: ~$298.8M across 4 rounds
- Key round: $220M Series C (April 2021) led by SoftBank Vision Fund 2
- Other investors: General Catalyst, Norwest Venture Partners, DCM, Bling Capital, Steadfast Capital Ventures
- Post-Series B valuation: $250M (July 2020); Series C valuation not disclosed but reportedly more than tripled
- Revenue: ~$15M ARR (June 2024, per GetLatka)
- Employees: ~223 (2024); experienced layoffs of 10% (March 2022) and 30% (October 2022)
- Products: Tempo Studio ($2,495), Tempo Move ($395), app-only membership ($39/mo)
- Subscription: $39/mo (12-month minimum commitment), sharable with up to 6 household members
- Financing: 12, 24, or 48-month plans via Affirm at 0% APR
- International: US only. No international shipping. No timeline announced for global expansion
- Competitors: Peloton, Tonal, Apple Fitness+, Lululemon Mirror (discontinued hardware late 2023)

**Confirmed PSPs & Payment Stack:**
- Stripe: primary card acquirer, confirmed in Terms of Service ("We use Stripe as our third party service provider for payment services")
- Shopify Payments: e-commerce platform is Shopify (tempofit.myshopify.com), supporting Visa, Mastercard, Amex, Discover, Elo, JCB
- Affirm: BNPL financing for hardware purchases (12, 24, 48-month terms)
- PayPal: accepted for apparel and equipment purchases
- Apple Pay: digital wallet at checkout
- Google Pay: digital wallet at checkout
- Shop Pay: Shopify accelerated checkout
- Meta Pay: accepted for apparel purchases
- Flex: HSA/FSA payment processor for equipment bundles (not subscriptions)
- 3D Secure: enabled in checkout configuration
- No payment orchestrator detected

**Payment issues documented:**
- BBB: Not accredited. Complaints about mandatory 12-month subscription commitments, cancellation difficulties, and billing disputes
- Trustpilot: 4.8/5 across 500+ reviews (mostly positive), but negative reviews center on billing and subscription lock-in
- Customers report unexpected renewal charges after cancellation requests
- Cancellation requires action at least 3 days before billing cycle end
- No refunds for partial months or unused subscription periods during commitment windows
- Order fulfillment delays documented (e.g., March 2024 order with multi-month Squat Rack backorder)
- Some customers filed FTC and BBB complaints citing deceptive billing practices
- Wi-Fi connectivity issues causing mid-workout interruptions

**Top Markets Gap Analysis:**

MARKET 1: United States (only market, hardware + subscription)
  Offer: Visa/MC/Amex/Discover/JCB via Stripe + Shopify, PayPal, Apple Pay, Google Pay, Shop Pay, Meta Pay, Affirm, Flex HSA/FSA
  Missing: ACH Direct Debit, Venmo, Cash App Pay, Klarna, Afterpay
  Strong card and wallet coverage but no direct bank debit for $39/mo recurring billing. Missing popular BNPL alternatives beyond Affirm.

MARKET 2: International (not yet launched)
  Offer: None (no international shipping or checkout)
  Missing: Everything. SEPA DD, iDEAL, BLIK, Bancontact, Pix, Boleto, OXXO, SPEI, UPI, Konbini, Mada
  $15.5B global home fitness market at 7.5% CAGR. Any international expansion will require full local APM infrastructure from day one.

**Key meeting angles:**
1. **Involuntary churn protection**: With $39/mo mandatory 12-month subscriptions, every failed renewal costs $468 in committed revenue. Failover and smart retries can recover up to 50% of declines, directly protecting the subscriber base.
2. **High-ticket conversion**: Studio bundles at $2,495 are high-consideration purchases. Offering more BNPL options (Klarna, Afterpay) alongside Affirm and adding direct bank debit widens the payment funnel for premium hardware.
3. **International readiness**: Tempo is US-only today but raised nearly $300M to scale. When international expansion comes, Yuno provides instant access to 1,000+ local payment methods via one API integration, not country-by-country builds.
4. **Unified payment visibility**: Equipment (shop.tempo.fit), apparel (apparel.tempo.fit), and subscriptions run on different Shopify instances. Yuno consolidates all PSPs into a single dashboard with real-time auth rate monitoring and anomaly detection.
5. **Competitive parity**: Peloton accepts more payment methods globally. Tonal offers its own financing. As Mirror exits and the market consolidates, payment flexibility becomes a differentiator for surviving players.
6. **Post-pandemic recovery narrative**: Revenue dropped from pandemic peak; now at $15M ARR with a leaner team. Maximizing auth rates and reducing payment friction is critical to recover growth without adding headcount.

**Sources:**
- [Tempo Official Website](https://tempo.fit/)
- [Tempo Terms of Service (Stripe confirmed)](https://tempo.fit/terms-of-service)
- [Tempo Payments & FAQs](https://support.tempo.fit/support/solutions/articles/151000154598-payments-faqs)
- [Tempo Apparel FAQs (payment methods)](https://support.tempo.fit/support/solutions/articles/151000154614-tempo-apparel-faqs)
- [Tempo Updating Payment Information](https://support.tempo.fit/support/solutions/articles/151000154597-updating-payment-information)
- [Tempo Pricing Page](https://tempo.fit/pricing)
- [Tempo Shop (Shopify)](https://shop.tempo.fit/)
- [Tempo International Shipping FAQ](https://support.tempo.fit/support/solutions/articles/151000154604-does-tempo-ship-internationally-)
- [Tempo Membership FAQs](https://support.tempo.fit/support/solutions/articles/151000204613-membership-faqs)
- [Tempo BBB Complaints](https://www.bbb.org/us/ca/san-francisco/profile/online-shopping/tempo-1116-925814/complaints)
- [Tempo Trustpilot Reviews](https://www.trustpilot.com/review/tempo.fit)
- [Tempo Revenue & Financials (GetLatka)](https://getlatka.com/companies/tempo.fit)
- [Tempo Revenue (CBInsights)](https://www.cbinsights.com/company/tempo-fit/financials)
- [Tempo Crunchbase Profile](https://www.crunchbase.com/organization/trainwithpivot)
- [TechCrunch: Tempo Raises $220M Series C](https://techcrunch.com/2021/04/13/home-gym-startup-tempo-raises-220m-to-meet-surge-in-demand-for-its-workout-device/)
- [SignalFire: Moawia Eldeeb Founder Story](https://www.signalfire.com/blog/tempo-raises-220m)
- [Athletech News: Tempo CEO Interview](https://athletechnews.com/ceo-corner-moawia-eldeeb-tempo-fitness-ai-exclusive-interview/)
- [Tempo Y Combinator Profile](https://www.ycombinator.com/companies/tempo)
- [Affirm: Tempo Case Study](https://www.affirm.com/business/blog/affirm-increases-sales-tempo-fitness)
- [Tempo Partners with Flex for HSA/FSA](https://www.globenewswire.com/news-release/2024/09/10/2943685/0/en/AI-Personal-Fitness-Startup-Tempo-Partners-with-Flex-to-Bring-More-Payment-Options-to-its-Customers.html)
- [Athletech News: Tempo + Flex Partnership](https://athletechnews.com/tempo-teams-flex-accept-hsafsa/)
- [Brandfetch: Tempo Logo](https://brandfetch.com/tempo.fit)
- [Tempo App (Apple App Store)](https://apps.apple.com/us/app/tempo-home-workout-fitness/id1501671678)
- [Tempo App (Google Play)](https://play.google.com/store/apps/details?id=com.coretechfitness.tempo)
- [Home Fitness Market Size (FutureDataStats)](https://www.futuredatastats.com/home-fitness-solutions-market)
- [Smart Fitness Market Size (Precedence Research)](https://www.precedenceresearch.com/smart-fitness-market)
