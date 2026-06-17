# ELEVENLABS | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: ElevenLabs
=======================================

Logo: https://upload.wikimedia.org/wikipedia/commons/2/2a/ElevenLabs_Logo_01.svg
Nombre merchant: ElevenLabs

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Enterprise Scaling Strain
Tittle_Pain Point_2: Single Processor Ceiling
Tittle_Pain Point_3: LatAm/Asia APM Gap
Tittle_Pain Point_4: Payout Reconciliation Drag
Tittle_Pain Point_5: Mobile IAP Fee Bleed

Desc_Pain Point_1: Revenue shifting to 60/40 enterprise by end 2026. Deutsche Telekom, Revolut, Meta require custom invoicing and multi-currency settlement that single Stripe Billing cannot handle at $330M+ ARR.
Desc_Pain Point_2: Stripe processes all subscriptions, API credits, and enterprise invoices. At $330M ARR, any degradation blocks renewals and voice credits across 14 global offices simultaneously.
Desc_Pain Point_3: Offices opened in Brazil, Mexico, India, Japan, Korea with local sales teams. India usage grew 50% in 3 months. Zero local APMs: no Pix, OXXO, UPI, Konbini, or KakaoPay.
Desc_Pain Point_4: Stripe Connect handles Voice Library payouts; Stripe Billing handles subscriptions. Two Stripe products create dual reconciliation for one lifecycle: subscriber pays, creator earns.
Desc_Pain Point_5: App Store and Google Play subscriptions lose 15-30% to commissions. 41% of Fortune 500 use ElevenLabs. Web billing with local APMs protects margin on consumer plans.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe Billing (subscriptions, API credits)
PSP_2: Stripe Connect (Voice Library payouts)
PSP_3: Apple App Store (iOS subscriptions)
PSP_4: Google Play (Android subscriptions)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix (Brazil)
Local_M_2: UPI (India)
Local_M_3: KakaoPay (South Korea)
Local_M_4: Konbini (Japan)
Local_M_5: OXXO (Mexico)
Local_M_6: SPEI (Mexico)
Local_M_7: BLIK (Poland)
Local_M_8: Boleto (Brazil)
Local_M_9: iDEAL (Netherlands)
Local_M_10: SEPA Direct Debit (EU)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each renewal, API purchase, and enterprise invoice to the optimal acquirer by card BIN and currency. At $330M ARR with 41% Fortune 500 penetration, a 3% auth uplift recovers $10M+ annually across 14 global offices.
Desc_Yuno_Cap2: Automatic cascade eliminates single-Stripe dependency for Billing and Connect. When Stripe declines, Yuno reroutes in milliseconds. Up to 50% recovery on failed transactions, protecting voice revenue and creator payouts simultaneously.
Desc_Yuno_Cap3: Activates local rails each office needs: Pix in Brazil (Sao Paulo), OXXO in Mexico (Mexico City), UPI in India (Bengaluru, 50% growth), KakaoPay in Korea (Seoul), Konbini in Japan (Tokyo). One API, 1,000+ payment methods.
Desc_Yuno_Cap4: One dashboard unifying Stripe Billing, Stripe Connect, App Store, and Google Play. Real-time monitoring across subscriptions, invoices, API credits, and payouts. NOVA fraud engine with 75% fewer false positives.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**ElevenLabs at a glance:**
- Founded: 2022 by Piotr Dabkowski and Mati Staniszewski (Polish founders)
- Headquarters: London, UK (with global offices)
- Valuation: $11B (Series D, Feb 2026); up from $3.3B (Series C, Jan 2025)
- Revenue: $330M ARR (end 2025), 175% YoY growth from $120M (end 2024)
- Total Funding: $811M across 8 rounds (largest: $500M Series D, led by Sequoia)
- Enterprise/Consumer Split: 50/50 as of Dec 2025, shifting to 60/40 by Dec 2026
- Fortune 500 Penetration: 41% of Fortune 500 companies use ElevenLabs
- IPO: Actively building toward IPO (stated in Series D announcement)

**Products:**
- Text-to-Speech (TTS): Core product, industry-leading voice synthesis
- ElevenAgents: AI voice agents for customer support, sales, commerce
- ElevenCreative: Creative tools for media production
- Voice Library: Marketplace for voice clones (with Stripe Connect payouts)
- ElevenReader: Audiobook/article reader app
- Speech-to-Speech: Real-time voice transformation
- Dubbing Studio: Automated video dubbing in 29+ languages
- API: Usage-based pricing for developers
- Subscription Tiers: Free, Starter ($5/mo), Creator ($22/mo), Pro ($99/mo), Scale ($330/mo), Enterprise (custom)

**Confirmed PSPs / Payment Rails:**
- Stripe Billing: Primary processor for all subscriptions and API credits (confirmed in Stripe case study)
- Stripe Connect: Processes reward payouts to Voice Library creators
- Stripe Optimized Checkout Suite: Custom subscription sign-up page
- Apple App Store: iOS subscriptions
- Google Play: Android subscriptions
- No secondary acquirer or payment orchestrator detected

**Global Office Network (14 cities):**
- London (HQ), New York, San Francisco, Warsaw
- Tokyo, Seoul, Singapore, Bengaluru, Sydney
- Sao Paulo, Mexico City
- Berlin, Paris, Dublin
- Locally embedded go-to-market teams support enterprise adoption of ElevenAgents and ElevenCreative

**Key Enterprise Customers:**
- Deutsche Telekom: Customer support voice agents
- Revolut: Voice-powered customer engagement
- Meta: Voice infrastructure for products
- Salesforce: Voice experiences
- Square: Voice-enabled commerce
- Ukrainian Government: Citizen engagement
- Washington Post, TIME: Media production
- HarperCollins: Publishing
- Paradox Interactive: Gaming

**Key Payment Challenges:**
- Single processor handling subscription billing AND creator payouts creates reconciliation complexity
- 14 global offices with local sales teams but no local payment acceptance
- India showing 50% usage growth in 3 months but no UPI or local rails
- Enterprise shift (60/40 by 2026) requires invoicing, PO management, multi-currency settlement
- Voice Library payout + subscription billing = dual Stripe product dependency
- Mobile IAP commissions erode margin on consumer subscriptions

**Key Meeting Angles:**
1. **$11B valuation, IPO trajectory** | Payment infrastructure maturity is critical for investor and underwriter scrutiny as ElevenLabs builds toward public offering.
2. **14 offices, zero local APMs** | Go-to-market teams in Brazil, Mexico, India, Japan, Korea are selling enterprise deals without local payment acceptance in their own markets.
3. **Enterprise shift from 50/50 to 60/40** | Doubling enterprise revenue requires invoicing, usage metering, and multi-currency billing that outgrows single-Stripe-Billing dependency.
4. **India 50% growth in 3 months** | Fastest-growing market by usage. UPI handles 75%+ of Indian digital payments. No UPI = monetization ceiling on India growth.
5. **Dual Stripe dependency** | Stripe Billing + Stripe Connect creates two failure surfaces. Creator payouts and subscriber billing share a single provider with no failover on either stream.
6. **41% Fortune 500 adoption** | Enterprise customers like Deutsche Telekom, Meta, Salesforce expect multi-acquirer resilience and local payment acceptance as standard.
7. **Voice Library marketplace** | Creator economy with payouts + subscriptions is exactly the two-sided billing model that payment orchestration was built for.

**Sources:**
- [ElevenLabs Series D ($500M at $11B) (Blog)](https://elevenlabs.io/blog/series-d)
- [ElevenLabs + Stripe Case Study (Stripe)](https://stripe.com/customers/elevenlabs)
- [ElevenLabs $11B Valuation (CNBC)](https://www.cnbc.com/2026/02/04/nvidia-backed-ai-startup-elevenlabs-11-billion-valuation.html)
- [ElevenLabs Series C ($180M at $3.3B) (Blog)](https://elevenlabs.io/blog/series-c)
- [ElevenLabs Revenue and Valuation (Sacra)](https://sacra.com/c/elevenlabs/)
- [ElevenLabs Statistics (Electroiq)](https://electroiq.com/stats/elevenlabs-statistics/)
- [ElevenLabs Statistics (Fueler)](https://fueler.io/blog/elevenlabs-usage-revenue-valuation-growth-statistics)
- [ElevenLabs IPO Plans (Tech.eu)](https://tech.eu/2026/02/04/elevenlabs-raises-500m-says-building-towards-ipo/)
- [ElevenLabs Brand Assets (Official)](https://elevenlabs.io/brand)
- [ElevenLabs Payment Methods FAQ (Help Center)](https://help.elevenlabs.io/hc/en-us/articles/13416538053905-What-kind-of-payment-is-accepted)
- [ElevenLabs Subscription Management (Help Center)](https://help.elevenlabs.io/hc/en-us/articles/40570893074449-Managing-Your-ElevenLabs-Subscription-Mobile-App-vs-Website)
- [ElevenLabs Voice Library Payouts (Docs)](https://elevenlabs.io/docs/creative-platform/voices/payouts)
- [ElevenLabs Pricing (Flexprice)](https://flexprice.io/blog/elevenlabs-pricing-breakdown)
- [ElevenLabs $200M ARR (LinkedIn/Mati)](https://www.linkedin.com/posts/matiii_we-dont-often-share-numbers-but-with-yesterday-activity-7371289071534428161-fPME)
- [ElevenLabs Funding (Tracxn)](https://tracxn.com/d/companies/elevenlabs/__Tvkv2vcQvT5RiO80KqXicawZyFtA-r7-J533YWuiDrM/funding-and-investors)
- [ElevenLabs Logo (Wikimedia Commons)](https://commons.wikimedia.org/wiki/File:ElevenLabs_Logo_01.svg)
