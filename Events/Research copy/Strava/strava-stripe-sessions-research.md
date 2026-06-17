# STRAVA | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Strava
═══════════════════════════════════════

Logo: https://asset.brandfetch.io/id2S-kXbuY/idEkax5rMT.svg
Nombre merchant: Strava

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Low Conversion to Paid
Tittle_Pain Point_2: Single Acquirer Fragility
Tittle_Pain Point_3: APM Gaps in Key Markets
Tittle_Pain Point_4: Cross-Border FX Drag
Tittle_Pain Point_5: IPO-Grade Visibility Gap

Desc_Pain Point_1: Only 2-5% of 195M registered users convert to paid subscriptions. Every percentage point of auth failure at checkout costs millions in lost subscribers on a $500M ARR base heading into IPO.
Desc_Pain Point_2: Web subscriptions flow through a single acquirer with no cascade. Any outage or rate dip blocks renewals for millions of paying athletes across 185+ countries with zero failover path.
Desc_Pain Point_3: Pix was added in Brazil (market #2), but no OXXO/SPEI in Mexico, no UPI in India, no BLIK in Poland, no iDEAL in Netherlands. Key growth markets still lack local payment rails.
Desc_Pain Point_4: Strava bills in USD for most markets outside the US. Athletes in Europe, LATAM, and Asia absorb cross-border FX markup on every $79.99/yr renewal, increasing effective price and churn.
Desc_Pain Point_5: Confidential IPO filing targets $3B valuation. Investors will scrutinize payment KPIs: auth rates, involuntary churn, revenue retention. No orchestration layer means no centralized metrics.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe
PSP_2: PayPal
PSP_3: Apple Pay
PSP_4: Google Pay
PSP_5: App Store / Google Play (IAP)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: OXXO
Local_M_2: SPEI
Local_M_3: UPI
Local_M_4: iDEAL
Local_M_5: BLIK
Local_M_6: Bancontact
Local_M_7: SEPA Direct Debit
Local_M_8: Konbini
Local_M_9: Boleto
Local_M_10: Mada

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route every subscription charge and renewal to the best performing acquirer per card BIN, country, and issuer. With $500M ARR and 195M+ users, a 3% auth uplift at checkout directly increases paid conversion rate and recovers tens of millions annually.
Desc_Yuno_Cap2: When the primary acquirer declines a subscription renewal, Yuno cascades to an alternate acquirer in milliseconds. Recovers up to 50% of failed recurring charges, protecting the 80-90% subscriber retention rate critical to Strava's IPO narrative.
Desc_Yuno_Cap3: Extends Strava's Pix success in Brazil to every growth market: OXXO/SPEI in Mexico, UPI in India (500M+ users), iDEAL in Netherlands, BLIK in Poland, Konbini in Japan, SEPA DD in Europe. One API, 1,000+ payment methods, zero engineering sprints per country.
Desc_Yuno_Cap4: Single dashboard consolidating all PSPs and app store billing into one view. Real-time auth rate monitoring across every market and acquirer, centralized reconciliation, and millisecond anomaly detection via NOVA. IPO-ready payment intelligence from day one.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Strava at a glance:**
- Founded: 2009 in San Francisco, CA
- CEO: Michael Martin (ex-Google/YouTube executive, appointed December 2023)
- Co-Founders: Michael Horvath and Mark Gainey (both stepped back)
- Valuation: $2.2B (May 2025 funding round); targeting $3B+ at IPO
- Total funding raised: $228.5M (latest round led by Sequoia Capital)
- Revenue: ~$415-500M ARR in 2025, ~50% YoY growth
- Revenue mix: ~90% subscriptions, rest from sponsored challenges and Metro (city planning data)
- Registered users: 195M+ across 185+ countries
- Monthly active users: ~50M
- Paid subscribers: estimated 2-5% of registered base (~4-10M paying athletes)
- Subscriber retention: 80-90%
- Subscription pricing: $11.99/mo or $79.99/yr; Family Plan: $139.99/yr
- IPO: Confidentially filed S-1 (January 2026), Goldman Sachs as lead underwriter
- Employees: ~400-500

**Confirmed PSPs:**
- Stripe: primary card acquirer for web subscriptions (attending Stripe Sessions)
- PayPal: accepted for web subscriptions
- Apple Pay / Google Pay: digital wallet options
- App Store (Apple) / Google Play: in-app purchase billing for mobile subscribers
- Pix: integrated in Brazil (second-largest market) for local payment access
- No payment orchestrator detected

**Payment issues documented:**
- Trustpilot rating: 1.5/5 stars
- BBB: 80+ complaints in three years related to billing and subscription issues
- Users report unexpected annual charges when expecting monthly billing
- Payment processing occurs but subscription access not granted (Apple IAP sync issues)
- Community forums document billing disputes and slow support response times
- Free trial to paid conversion confusion generates complaints

**Top Markets Gap Analysis:**

MARKET 1: United States (largest market)
  Offer: Visa/MC/Amex via Stripe, PayPal, Apple Pay, Google Pay
  Missing: ACH Direct Debit, Cash App Pay, Venmo
  Solid coverage but no direct bank debit for recurring billing

MARKET 2: Brazil (second-largest market)
  Offer: Visa/MC via Stripe, Pix (recently added)
  Missing: Boleto Bancario
  Pix integration is a strong signal that Strava prioritizes local APMs; Boleto is the next gap

MARKET 3: United Kingdom (major European market)
  Offer: Visa/MC via Stripe, PayPal
  Missing: Open Banking, PayByBank
  Running and cycling culture drives strong adoption; direct bank payments could boost conversion

MARKET 4: Germany (key European market)
  Offer: Visa/MC via Stripe, PayPal
  Missing: SEPA Direct Debit, Giropay
  ~35% credit card penetration. SEPA DD is standard for subscription billing in DACH

MARKET 5: Mexico (growing LATAM market)
  Offer: Visa/MC via cross-border acquiring
  Missing: OXXO, SPEI, CoDi
  60%+ unbanked. OXXO processes 55M+ transactions/month. No cash voucher = no mass market conversion

**Key meeting angles:**
1. **IPO readiness**: $3B target valuation. Payment orchestration provides centralized KPIs investors demand: auth rates, retry recovery, market-level performance
2. **Conversion optimization**: 2-5% paid conversion on 195M users. Every basis point of checkout improvement at scale is worth millions in new ARR
3. **Pix precedent**: Strava already proved local APM integration drives conversion in Brazil. Yuno scales that playbook to every market via one API
4. **Subscriber retention**: 80-90% retention is elite but fragile on a single acquirer. Failover protects the retention metric that anchors IPO valuation
5. **Global growth engine**: 185+ countries, 50M MAU, but most markets still cards-only. Local APMs in top 10 markets would unlock the next wave of paid conversion
6. **Competitive moat**: Garmin Connect and Apple Fitness+ accept local APMs in multiple markets. Strava needs payment parity to defend its social fitness network

**Sources:**
- [Strava Subscription Pricing FAQ](https://support.strava.com/hc/en-us/articles/13013167258381-Subscription-Pricing-FAQ)
- [Strava Managing Billing Information](https://support.strava.com/hc/en-us/articles/216918917-Managing-your-Billing-Information)
- [Strava Pix Integration in Brazil](https://press.strava.com/articles/strava-strengthens-its-presence-in-brazil-and-expands-access-to-the)
- [Strava Revenue & Statistics - Business of Apps](https://www.businessofapps.com/data/strava-statistics/)
- [Strava Revenue - Sacra](https://sacra.com/c/strava/)
- [Strava Revenue - GetLatka](https://getlatka.com/companies/strava)
- [Strava IPO Filing Analysis - 5K Runner](https://the5krunner.com/2026/01/09/strava-ipo-filing-3-billion-valuation-analysis/)
- [Strava Confidential IPO Filing - SiliconANGLE](https://siliconangle.com/2026/01/08/strava-makes-confidential-ipo-filing-amid-subscription-revenue-growth/)
- [Strava IPO Goldman Sachs - Fintool](https://fintool.com/news/strava-ipo-confidential-filing-goldman)
- [PYMNTS: Strava $2.2B Valuation](https://www.pymnts.com/news/investment-tracker/2025/funding-round-boosts-fitness-app-stravas-valuation-to-2-2-billion/)
- [Fortune: Strava CEO IPO Plans](https://fortune.com/2025/10/13/strava-ipo-ceo-michael-martin-gen-z-running-clubs-marathons-dating-apps/)
- [Fortune: How Strava Ran Toward a Comeback](https://fortune.com/2026/01/13/how-strava-ran-toward-a-comeback-ipo/)
- [Strava Trustpilot Reviews](https://www.trustpilot.com/review/strava.com)
- [Strava StackShare Profile](https://stackshare.io/strava/strava)
- [Brandfetch: Strava Logo](https://brandfetch.com/strava.com)
