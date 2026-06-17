# LIME | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Lime
=======================================

Logo: https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Lime_%28transportation_company%29_logo.svg/520px-Lime_%28transportation_company%29_logo.svg.png
Nombre merchant: Lime

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Single PSP Dependency
Tittle_Pain Point_2: Cash Market Exclusion
Tittle_Pain Point_3: Local Wallet Gap
Tittle_Pain Point_4: Cross-Border FX Leakage
Tittle_Pain Point_5: Ride-Start Auth Friction

Desc_Pain Point_1: Stripe is the sole processor for 280+ cities across 30 countries. Any Stripe incident blocks ride starts globally, stranding riders and vehicles.
Desc_Pain Point_2: PayNearMe cash option is US-only. In LatAm, EU, and Middle East markets where cash or wallets dominate, riders without cards cannot use Lime.
Desc_Pain Point_3: No Pix in Brazil, no iDEAL in Netherlands, no Bancontact in Belgium, no BLIK in Poland. Card penetration under 40% in many Lime cities.
Desc_Pain Point_4: Riders in 30 countries pay cross-border card fees on $1 to $5 micro-rides. FX markup makes Lime costlier than local competitors in every market.
Desc_Pain Point_5: Pre-auth on every ride start triggers high decline rates on cross-border micro-amounts, especially with prepaid cards and European debit cards.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe
PSP_2: PayPal
PSP_3: Apple Pay (via Stripe)
PSP_4: Google Pay (via Stripe)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: iDEAL
Local_M_3: Bancontact
Local_M_4: BLIK
Local_M_5: Swish
Local_M_6: MobilePay
Local_M_7: Vipps
Local_M_8: Boleto
Local_M_9: SEPA Direct Debit
Local_M_10: Sofort

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each ride-start authorization to the best-performing acquirer for that rider's card BIN and city. With $686M in 2024 revenue, 24M+ riders, and micro-transactions across 30 countries, a 3% auth uplift directly reduces ride-start failures and lost revenue.
Desc_Yuno_Cap2: When Stripe declines a ride-start pre-auth, Yuno cascades to the next acquirer in milliseconds. Riders unlock scooters on the first tap, not the third. Up to 50% of failed micro-authorizations recovered without rider friction or manual retry.
Desc_Yuno_Cap3: Activates local APMs riders already use: Pix in Brazil, iDEAL in Netherlands, Bancontact in Belgium, BLIK in Poland, Swish in Sweden, MobilePay in Denmark, Vipps in Norway. One API, 1,000+ methods, instant market coverage.
Desc_Yuno_Cap4: Single dashboard replacing Lime's fragmented Stripe + PayPal + Apple Pay + Google Pay + PayNearMe streams. Real-time approval monitoring per city and country, centralized reconciliation across 280+ markets, anomaly detection via NOVA with 75% faster resolution.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Lime at a glance:**
- Founded 2017 (as LimeBike), HQ San Francisco, CA. Private (IPO expected 2026)
- Revenue: $686M net revenue (2024), up 32% YoY. Gross bookings: $810M (2024)
- Free cash flow positive for 2 consecutive years (2023, 2024)
- IPO preparation: Goldman Sachs + JPMorgan hired as underwriters
- Operations: 280+ cities, ~30 countries, 270K+ e-bikes and scooters
- 24M+ riders served in 2024
- Backed by Uber (integration allows Lime rentals in Uber app)
- TIME 2025 Top 100 Most Influential Companies
- CEO: Wayne Ting

**Confirmed PSPs:**
- Stripe: primary payment processor (confirmed via Stripe case study)
- Stripe Data Pipeline sends complete payment data to Snowflake
- PayPal: secondary (named in payment options)
- Apple Pay, Google Pay: wallet options (likely via Stripe)
- PayNearMe: US-only cash alternative (7-Eleven, Walgreens, CVS)
- Prepaid credit/debit cards accepted
- Uber gift cards accepted (via Uber integration)
- No payment orchestrator detected

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (largest market)
  OK Currently offer: Visa/MC/Amex, PayPal, Apple Pay, Google Pay, PayNearMe (cash)
  Missing: ACH, Cash App Pay, Venmo direct
  Note: Cash via PayNearMe at 1,000+ retail locations for equity/access

MARKET 2: Germany (largest European market for micromobility)
  OK Currently offer: Credit/debit cards, Apple Pay, Google Pay
  Missing: SEPA Direct Debit, Sofort, PayPal local
  Note: Credit card penetration ~35%. Majority of German riders prefer debit/SEPA

MARKET 3: France (key European market)
  OK Currently offer: Credit/debit cards, Apple Pay, Google Pay
  Missing: Carte Bancaire local routing, Bancontact (Belgium border cities)
  Note: Carte Bancaire processed locally yields higher auth rates than cross-border

MARKET 4: Netherlands (active Lime market)
  OK Currently offer: Credit/debit cards
  Missing: iDEAL (75%+ of Dutch online payments), Bancontact
  Note: iDEAL is the dominant payment method; card-only creates massive conversion gap

MARKET 5: Brazil (LatAm expansion)
  OK Currently offer: Credit/debit cards
  Missing: Pix, Boleto, local installment cards
  Note: Pix handles 70%+ of Brazilian digital payments. Without it, Lime excludes the majority of potential riders

**Key meeting angles:**
1. **IPO readiness** | Payment infrastructure diversity and resilience will be scrutinized by Goldman/JPMorgan underwriters
2. **Micro-transaction economics** | $1 to $5 ride charges amplify cross-border fees as a % of transaction value
3. **Ride-start reliability** | Every declined pre-auth = stranded rider + idle vehicle + lost revenue
4. **European wallet gap** | Operating in 15+ European countries with zero local APMs is a competitive liability
5. **Uber integration** | Lime rides booked via Uber app still process through Lime's payment stack
6. **Equity and access** | Local APMs extend Lime's equity mission beyond US PayNearMe to unbanked riders globally

**Sources:**
- [Stripe Case Study: Lime](https://stripe.com/customers/lime)
- [Lime Privacy Notice](https://www.li.me/legal/privacy-policy)
- [Lime Payment Methods Guide](https://www.levyelectric.com/resources/your-guide-to-payment-methods-for-lime-scooters:-ride-smoothly!)
- [Lime Access Program](https://www.li.me/why/community/lime-access)
- [Lime IPO (Yahoo Finance)](https://finance.yahoo.com/news/limes-long-awaited-ipo-finally-010106629.html)
- [Lime IPO Banks (Bloomberg)](https://www.bnnbloomberg.ca/business/company-news/2025/06/24/uber-backed-electric-bike-startup-lime-hires-banks-for-us-ipo-sources-say/)
- [Lime 2024 Financial Results](https://www.li.me/blog/lime-becomes-the-first-shared-electric-vehicle-company-to-achieve-a-full-profitable-year)
- [Lime End of Year Reports](https://www.li.me/about/end-of-year-reports)
- [Lime Wikipedia](https://en.wikipedia.org/wiki/Lime_(transportation_company))
- [Lime Logo (Wikimedia)](https://commons.wikimedia.org/wiki/File:Lime_(transportation_company)_logo.svg)
