# SPEECHIFY | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Speechify
=======================================

Logo: https://upload.wikimedia.org/wikipedia/commons/1/19/Speechify-logo.svg
Nombre merchant: Speechify

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: IAP Fee Dependency
Tittle_Pain Point_2: Auth Rate Leakage
Tittle_Pain Point_3: Zero Local APMs
Tittle_Pain Point_4: Single PSP Dependency
Tittle_Pain Point_5: Chargeback Exposure

Desc_Pain Point_1: Premium subscriptions at $29/mo flow primarily through Apple/Google IAP, surrendering 15 to 30% per transaction. With $17.6M ARR and 50M+ users, millions are lost to platform fees annually.
Desc_Pain Point_2: Users report accidental annual charges ($139 to $287) and failed payment processing. International card declines block conversions across 200 countries and 60+ language markets.
Desc_Pain Point_3: 50M+ users across 200 countries, yet web checkout only accepts credit cards and PayPal. No Pix, UPI, iDEAL, BLIK, or local wallets in any market.
Desc_Pain Point_4: Terms reference a single unnamed "third party payment processor." No failover, no routing optimization. One PSP outage blocks all web subscription revenue.
Desc_Pain Point_5: Trustpilot reviews show billing disputes: surprise annual charges, trial to paid conversions without notice, difficulty canceling. High dispute rates increase processing costs.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe [INFERENCE]
PSP_2: Apple App Store
PSP_3: Google Play
PSP_4: PayPal

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: UPI
Local_M_3: iDEAL
Local_M_4: BLIK
Local_M_5: Boleto
Local_M_6: OXXO
Local_M_7: SEPA Direct Debit
Local_M_8: Konbini
Local_M_9: GCash
Local_M_10: KakaoPay

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each Speechify Premium renewal through the optimal acquirer per card BIN, issuer, and market. With $17.6M ARR and 50M+ users across 200 countries, even 3% auth uplift recovers $530K+ annually. Web checkout recaptures IAP margin.
Desc_Yuno_Cap2: Eliminate single PSP dependency. When the primary processor declines, Yuno cascades to the next best acquirer in milliseconds. Up to 50% recovery on failed transactions. NOVA AI re-engages churned subscribers, recovering up to 75%.
Desc_Yuno_Cap3: Activate Pix in Brazil, UPI in India, iDEAL in Netherlands, BLIK in Poland, SEPA DD in Germany, Konbini in Japan, GCash in Philippines. One API, 1,000+ methods across 200+ countries. Matches Speechify's 60+ language footprint.
Desc_Yuno_Cap4: One dashboard unifying the web PSP, Apple IAP, Google Play, and PayPal into a single view. Real time approval rate monitoring, centralized reconciliation across all providers and currencies, millisecond anomaly detection via Monitors.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Speechify at a glance:**
- Revenue: $17.6M ARR (July 2025 estimate)
- 50M+ users across 200 countries
- 160 employees, fully remote (no office)
- Products: Text to Speech app (#1 TTS globally), Voiceover Studio, Voice Cloning, Dubbing, API for developers
- Pricing: Free tier + Premium at $29/mo or $139/year (~$11.58/mo)
- 200+ AI voices in 60+ languages
- CEO: Cliff Weitzman (Founder, dyslexia advocate)
- CTO: Azeem Ahmad
- Funding: $10M at $100M valuation (Jan 2024), plus $768K seed (Oct 2025)
- Apple Design Award winner (WWDC 2025)
- 11M+ Google Play downloads, 100K+ 5 star reviews

**Confirmed PSPs:**
- Apple App Store: iOS IAP (confirmed via app store listing and terms)
- Google Play: Android IAP (confirmed via Google Play listing and terms)
- PayPal: accepted for web checkout (confirmed in help center)
- Unnamed "third party payment processor" for credit cards (Terms & Conditions reference). [INFERENCE: likely Stripe based on industry pattern, but not confirmed]
- No payment orchestrator detected

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (primary market, largest English TTS audience)
  Currently offer: Visa/MC, PayPal, Apple Pay (via IAP), Google Pay (via IAP)
  Missing: ACH, Cash App Pay, Venmo (outside IAP)
  Core market well served on mobile; web checkout limited to cards + PayPal.

MARKET 2: India (massive English learning + accessibility market)
  Currently offer: Visa/MC, Apple/Google IAP
  Missing: UPI, RuPay, Paytm, PhonePe
  75%+ of Indian digital payments use UPI. TTS for education/accessibility has huge demand in India.

MARKET 3: Brazil (growing accessibility + language learning market)
  Currently offer: Visa/MC, Apple/Google IAP
  Missing: Pix, Boleto
  Pix handles 70%+ of Brazilian digital payments. Web conversion is near zero without it.

MARKET 4: Germany/Netherlands/EU (strong accessibility regulation markets)
  Currently offer: Visa/MC, PayPal, Apple/Google IAP
  Missing: SEPA Direct Debit, iDEAL, Sofort, BLIK
  EU accessibility mandates drive TTS adoption. SEPA DD is standard for European subscription billing.

MARKET 5: Japan/South Korea (high TTS adoption for language learning)
  Currently offer: Visa/MC, Apple/Google IAP
  Missing: Konbini, PayPay, KakaoPay, Naver Pay
  Alternative payments dominate in both markets. Without local methods, web subscriptions suffer.

**Payment issues documented:**
- Trustpilot reviews report accidental annual charges of $139 to $287
- Users charged after trial without clear notice
- Difficulty canceling subscriptions on the website
- Some refund requests denied or delayed for weeks
- Mixed reviews: some report fast refunds within 1 hour, others wait a month

**Key meeting angles:**
1. **IAP fee arbitrage** | $29/mo Premium subscriptions on mobile lose 15 to 30% to Apple/Google. Web checkout with Yuno recaptures that margin
2. **200 countries, zero local APMs** | Speechify's 60+ language support covers markets where cards are not dominant, yet only cards and PayPal available
3. **Apple Design Award = growth signal** | WWDC 2025 recognition will accelerate international user acquisition
4. **Single PSP risk** | Terms reference one unnamed processor. No failover, no routing. One outage blocks all web revenue
5. **Accessibility regulation wave** | EU and global accessibility mandates drive TTS adoption; SEPA/iDEAL critical for EU conversion
6. **Competitor precedent** | Duolingo (multi PSP), Grammarly use optimized payment stacks for global subscription billing
7. **API product = B2B billing** | Speechify API for developers needs enterprise billing capabilities

**Sources:**
- [Speechify Pricing](https://speechify.com/pricing/)
- [Speechify Terms & Conditions](https://speechify.com/terms/)
- [Speechify Receipt/Charge Info](https://speechify.com/receipt/)
- [Speechify Payment Help](https://speechify.com/blog/how-can-i-view-my-subscription-details-and-change-my-payment-method-on-the-computer/)
- [Speechify Voiceover Subscription](https://speechify.com/blog/how-can-i-purchase-a-voiceover-subscription/)
- [Speechify Revenue (GetLatka)](https://getlatka.com/companies/speechify.com)
- [Speechify Funding (Crunchbase)](https://www.crunchbase.com/organization/speechify)
- [Speechify $10M Raise](https://speechify.com/news/speechify-raises-10M-100M-valuation/)
- [Speechify Trustpilot Reviews](https://www.trustpilot.com/review/speechify.com)
- [SimilarWeb: Speechify Traffic](https://www.similarweb.com/website/speechify.com/)
- [Speechify Brand Kit](https://speechify.com/brand-kit/)
- [Speechify Logo (Wikimedia)](https://commons.wikimedia.org/wiki/File:Speechify-logo.svg)
- [Speechify Languages](https://speechify.com/blog/what-speechify-languages-are-available/)
- [Cliff Weitzman Wikipedia](https://en.wikipedia.org/wiki/Cliff_Weitzman)
- [Speechify Google Play](https://play.google.com/store/apps/details?id=com.cliffweitzman.speechify2)
