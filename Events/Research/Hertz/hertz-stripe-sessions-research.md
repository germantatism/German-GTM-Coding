# HERTZ | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Hertz
=======================================

Logo: https://cdn.brandfetch.io/id2ZsMelvt/w/512/h/512/theme/dark/icon.jpeg
Nombre merchant: Hertz

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Legacy Stack Migration
Tittle_Pain Point_2: Auth Hold Friction
Tittle_Pain Point_3: Siloed Brand Payments
Tittle_Pain Point_4: Cross-Border FX Costs
Tittle_Pain Point_5: Limited Digital Wallets

Desc_Pain Point_1: Hertz migrated its entire payment stack to Stripe in 2024 across 3,000+ locations but still operates legacy systems in franchisee markets across 160 countries. Franchisees in LATAM, Asia, and the Middle East run independent payment rails with no unified orchestration or routing logic.
Desc_Pain Point_2: Car rental requires extended authorization holds ($200 to $500 per booking) that frequently trigger false declines and freeze customer credit limits. Hertz processes 150M+ transaction days annually, and even 1% false decline rate on a $57 RPD means millions in lost bookings per year.
Desc_Pain Point_3: Hertz, Dollar, and Thrifty operate as three brands under one corporation, but payment reconciliation across brands, channels (online, app, counter), and 11,000+ locations creates fragmented settlement streams. Stripe Terminal covers corporate locations, but franchisee networks remain disconnected.
Desc_Pain Point_4: International RAC revenue hit $1.65B in 2024 across Europe, Australia, New Zealand, and franchisee markets in Asia, LATAM, and the Middle East. Cross-border card transactions settled through USD intermediaries add FX markup that erodes margins on a company already posting a $2.86B net loss.
Desc_Pain Point_5: Hertz only launched Apple Pay for US customers in 2024. Google Pay, Samsung Pay, and PayPal are limited to counter contactless. No BNPL, no local digital wallets in Europe or Asia, and no alternative payment methods for online bookings in any international market.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe
PSP_2: Stripe Terminal (in-person)
PSP_3: Legacy processors (franchisee markets)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: iDEAL
Local_M_2: Bancontact
Local_M_3: Cartes Bancaires
Local_M_4: OXXO
Local_M_5: SPEI
Local_M_6: Mercado Pago
Local_M_7: Klarna
Local_M_8: Toss Pay
Local_M_9: PayPay
Local_M_10: GrabPay

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Recovery
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across Stripe and franchisee processors. Each rental payment routed to the highest performing acquirer for that card BIN, issuer, and market. On $9B+ total revenue across 160 countries, smart routing delivers +3 to 10% auth uplift, directly reducing the false declines that plague extended authorization holds in car rental.
Desc_Yuno_Cap2: Automatic cascade across Stripe and local acquirers eliminates single-processor dependency. When Stripe declines an extended authorization hold, Yuno reroutes to a local acquirer in milliseconds. Up to 50% recovery on soft declines via instant retry. NOVA AI recovers up to 75% of failed transactions with intelligent retry logic.
Desc_Yuno_Cap3: Activates the APMs Hertz still lacks globally: iDEAL in Netherlands, Bancontact in Belgium, Cartes Bancaires in France, OXXO and Mercado Pago in Mexico, Klarna across Europe, Toss Pay in South Korea, PayPay in Japan, GrabPay in Southeast Asia. One API, 1,000+ payment methods, no per-market integration required.
Desc_Yuno_Cap4: One dashboard unifying Hertz, Dollar, and Thrifty payment streams across 11,000+ locations in 160 countries. Real-time approval rate monitoring across corporate Stripe locations and franchisee processors, centralized reconciliation for all three brands, and millisecond anomaly detection via Monitors. Eliminates the fragmented settlement streams between brands and channels.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Hertz at a glance:**
- Brands: Hertz, Dollar, Thrifty (and Firefly in select markets)
- Revenue: $9.05B (FY2024, -3.4% YoY); $8.5B (FY2025)
- Net Loss: $2.86B (FY2024); $747M (FY2025, improved $2B+ YoY)
- Transaction Days: ~150.6M (FY2024)
- Revenue Per Transaction Day: ~$57.10 (Q4 2024)
- Average Fleet Size: ~533,000 vehicles (Q4 2024)
- Locations: 11,000+ rental locations in 160 countries
- Company-operated locations in: US, Canada, Australia, Belgium, Czech Republic, France, Germany, Italy, Luxembourg, Netherlands, New Zealand, Slovakia, Spain, UK
- Franchisee locations in: LATAM, Asia, Middle East, Africa, Caribbean
- NYSE: HTZ, market cap ~$1.5B
- Founded: 1918. CEO: Gil West (since April 2024)
- CFO: Scott Haralson (since June 2024, ex-Spirit Airlines)
- COO: Mike Moore (since October 2025)

**Revenue by Segment (FY2024):**
- Americas RAC: $7.40B (81.7%)
- International RAC: $1.65B (18.3%)
- International RAC Segment Revenue (Q3 2025): $568M

**2025 / 2026 Outlook:**
- "Back-to-Basics" strategy driving sequential improvement
- Net Promoter Score increased nearly 50% YoY in 2025
- Mid-single digit revenue growth expected Q1 2026
- Adjusted Corporate EBITDA improved $1B+ YoY in 2025

**Payments Leadership & Strategy:**
- Gil West (CEO): driving digital transformation as core of Back-to-Basics strategy
- Stripe partnership announced March 2024, making Stripe the standard payment infrastructure across Hertz, Dollar, and Thrifty
- Stripe Terminal deployed at ~3,000 corporate locations (US, Canada, Europe, Australia, New Zealand)
- Custom product roadmap with Stripe: extended authorizations for weekly/monthly rentals
- Eileen O'Mara (Stripe CRO): "Customers expect fast, simple, and reliable car rentals"

**Confirmed PSPs:**
- Stripe: primary PSP for all corporate-owned locations, online and in-person
- Stripe Terminal: BBPOS WisePOS E readers at ~3,000 locations
- Legacy processors: still active in franchisee markets (160 countries minus corporate territories)
- No payment orchestrator detected
- Stripe Card Account Updater and Adaptive Acceptance deployed to reduce false declines

**Payment Methods Currently Supported:**
- Global: Visa, Mastercard, Amex, Discover, JCB
- US: Apple Pay (launched 2024 via Stripe), Google Pay (counter only), Samsung Pay (counter only), PayPal (counter only)
- Europe: Debit cards accepted at corporate locations in 10 countries (Belgium, Czech Republic, France, Germany, Italy, Luxembourg, Netherlands, Slovakia, Spain, UK)
- No BNPL options (Klarna, Affirm, Afterpay)
- No local digital wallets for online bookings in any international market

**Top 5 Markets Gap Analysis:**

MARKET 1: United States ($7.4B Americas revenue)
  Currently offer: Visa/MC/Amex/Discover, Apple Pay, Google Pay (counter), Samsung Pay (counter), PayPal (counter)
  Missing: Klarna, Affirm, Afterpay (BNPL), Venmo, Cash App Pay
  No BNPL option for a $57/day average rental. BNPL adoption in US travel hit 45% in 2024.

MARKET 2: Germany (largest European corporate market)
  Currently offer: Visa/MC, debit cards
  Missing: iDEAL (cross-border Dutch travelers), Klarna, giropay/Paydirekt, SEPA instant
  Klarna is used by 150M+ consumers globally. Germany is Klarna's home market.

MARKET 3: France (corporate-operated locations)
  Currently offer: Visa/MC, debit cards
  Missing: Cartes Bancaires (domestic scheme, 70%+ of French card payments), PayLib, Bancontact (Belgian border traffic)
  Cartes Bancaires processes the majority of French card transactions. Not routing to CB means higher interchange on local French cards.

MARKET 4: Mexico (franchisee market, Hertz Mexico / Avasa)
  Currently offer: Visa/MC (via franchisee processor)
  Missing: OXXO, SPEI, Mercado Pago, CoDi, Kueski Pay
  OXXO handles 55%+ of Mexico e-commerce cash payments. Hertz Mexico partnership with Aeromexico drives significant digital booking volume.

MARKET 5: Japan (franchisee market)
  Currently offer: Visa/MC/JCB (via franchisee processor)
  Missing: PayPay (62M+ users), LINE Pay (40M+ users), Konbini, Rakuten Pay
  PayPay dominates Japanese mobile payments. Inbound tourism to Japan hit record 35M+ visitors in 2024.

MARKET 6: South Korea (franchisee market)
  Currently offer: Visa/MC (via franchisee processor)
  Missing: Toss Pay (22M+ MAU), KakaoPay, Samsung Pay (online), Naver Pay
  South Korea has 95%+ smartphone penetration. Mobile wallets account for 40%+ of online payments.

MARKET 7: Australia (corporate-operated)
  Currently offer: Visa/MC (via Stripe)
  Missing: Afterpay (12M+ AU users), eftpos, POLi, BPAY
  Afterpay was born in Australia and has massive penetration. BNPL is standard for travel bookings.

**Payment Pain Points:**
1. Extended authorization holds ($200-$500) frequently trigger false declines
2. Debit card users face higher deposits and longer refund windows (7-15 business days)
3. No BNPL options despite car rental being a natural fit for installment payments
4. Franchisee markets in 100+ countries operate independent payment rails with no orchestration
5. Apple Pay only available in US, not in any international market
6. No local payment methods for online bookings in Europe, LATAM, or Asia
7. $168M settlement for falsely reporting stolen vehicles indicates systemic operational issues
8. Three-brand reconciliation (Hertz/Dollar/Thrifty) across 11,000+ locations
9. Authorization hold amounts not disclosed until after reservation
10. FX costs on $1.65B international revenue with no smart routing to local acquirers

**Key Meeting Angles:**
1. **$9B+ revenue, single PSP dependency**: Stripe is the sole processor for corporate locations. No failover, no cascade, no multi-PSP routing. One Stripe outage blocks all payments across 3,000 locations
2. **160 countries, fragmented stack**: Corporate locations on Stripe, franchisees on legacy processors. Yuno orchestrates both under one dashboard
3. **Extended auth holds are a unique pain**: Car rental authorization holds are the #1 source of false declines. Smart routing to the best acquirer per BIN reduces hold failures. InDrive achieved 90% approval across 10 markets with Yuno
4. **$1.65B international revenue with no local APMs**: France lacks Cartes Bancaires, Germany lacks Klarna, Mexico lacks OXXO, Japan lacks PayPay. Each gap is lost revenue
5. **Three brands, one orchestrator**: Hertz, Dollar, Thrifty need unified payment analytics. McDonald's gained +4.7% auth rate ($3.2M revenue impact) with Yuno orchestration
6. **Back-to-Basics + digital transformation**: New CEO Gil West (April 2024) is focused on operational efficiency. Payment orchestration directly supports NPS improvement and cost reduction
7. **BNPL is missing entirely**: $57/day average rental with no Klarna, Affirm, or Afterpay option. BNPL adoption in travel is growing 40%+ YoY
8. **Net loss company needs margin recovery**: At $2.86B net loss (2024), every basis point of auth uplift and FX savings matters. Smart routing on $9B revenue delivers material P&L impact

**Sources:**
- [Stripe Newsroom: Hertz Partners with Stripe](https://stripe.com/newsroom/news/hertz-stripe)
- [Stripe Customer Story: Hertz Unifies Commerce](https://stripe.com/customers/hertz)
- [Finance Magnates: Stripe Transforms Car Rental Payments with Hertz](https://www.financemagnates.com/fintech/stripe-drives-transformation-in-car-rental-payments-with-hertz-collaboration/)
- [Hertz Newsroom: Q4 and Full Year 2024 Results](https://newsroom.hertz.com/press-releases/press-release-details/hertz-reports-fourth-quarter-and-full-year-2024-results/)
- [Hertz Newsroom: Transformation Drives Structural Revenue Gains (2025)](https://newsroom.hertz.com/press-releases/press-release-details/hertz-transformation-drives-structural-revenue-gains-and-builds-sustainable-momentum/)
- [PRNewswire: Hertz Q4 and FY2024 Results](https://www.prnewswire.com/news-releases/hertz-reports-fourth-quarter-and-full-year-2024-results-302376014.html)
- [Hertz Support: Payment Methods](https://www.hertz.com/supporthub/topic/payment-methods)
- [Hertz Blog: How to Pay for Your Car Rental](https://www.hertz.com/us/en/blog/resources/how-to-pay-for-your-car-rental)
- [JoinKudos: Does Hertz Take Apple Pay 2026](https://www.joinkudos.com/blog/does-hertz-take-apple-pay-2025-guide)
- [Hertz Newsroom: Debit Cards in Europe](https://newsroom.hertz.com/press-releases/press-release-details/hertz-dollar-and-thrifty-welcome-debit-cards-in-europe-offering-customers-greater-choice-a/)
- [Hertz Newsroom: Aeromexico Partnership](https://newsroom.hertz.com/news-releases/news-release-details/hertz-and-aeromexico-sign-exclusive-global-partnership-to-offer-hertz-dollar-thrifty-and-f/)
- [Hertz Newsroom: Localiza Partnership (LATAM)](https://newsroom.hertz.com/press-releases/press-release-details/hertz-launches-strategic-partnership-with-localiza-south-america-s-largest-rental-car-comp/)
- [Hertz IR: Leadership Team](https://ir.hertz.com/governance/leadership-team/default.aspx)
- [TradingView: Hertz 10-K Report](https://www.tradingview.com/news/tradingview:c810edb6981b7:0-hertz-global-holdings-inc-sec-10-k-report/)
- [Wikipedia: Hertz Global Holdings](https://en.wikipedia.org/wiki/Hertz_Global_Holdings)
