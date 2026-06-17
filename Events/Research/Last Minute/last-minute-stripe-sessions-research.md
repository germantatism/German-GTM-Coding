# LAST MINUTE (lastminute.com) | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: lastminute.com
=======================================

Logo: https://upload.wikimedia.org/wikipedia/commons/4/4e/Lastminute.com_Group_Logo.png
Nombre merchant: lastminute.com

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Multi PSP Fragmentation
Tittle_Pain Point_2: European APM Gaps
Tittle_Pain Point_3: Checkout Drop Off Rate
Tittle_Pain Point_4: Multi Brand Payment Silos
Tittle_Pain Point_5: BNPL Coverage Limits

Desc_Pain Point_1: Checkout.com processes card acquiring, Adyen handles virtual card issuing for supplier payouts, TrueLayer powers open banking, and Klarna runs BNPL separately. Four payment providers with no unified routing or failover between them. Each integration was added independently, creating reconciliation overhead across 40+ markets.
Desc_Pain Point_2: lastminute.com operates in 40+ countries and 17 languages, yet local payment method coverage is thin. iDEAL is absent for Dutch travelers, Bancontact missing for Belgium, Giropay/EPS absent for DACH, Bizum missing for Spain, MB Way missing for Portugal. European travelers default to cards when preferred local rails are unavailable.
Desc_Pain Point_3: Customer forums document repeated checkout failures: payments charged but bookings unconfirmed, duplicate authorizations, and card declines with no fallback. During a payment outage, open banking via TrueLayer saw a massive spike, proving customers need alternative payment paths when primary card rails fail.
Desc_Pain Point_4: The group operates lastminute.com, Volagratis, Bravofly, Rumbo, Jetcost, weg.de, and Hotelscan across 58 countries. Each brand site runs its own checkout flow. Payment method availability, routing logic, and acceptance rates vary by brand rather than being centrally optimized across the portfolio.
Desc_Pain Point_5: Klarna BNPL is available in select markets (UK, Germany, France, Italy, Spain, Netherlands) but is absent from Nordic countries, Eastern Europe, and non EU markets. Scalapay, Alma, and Oney are missing entirely. For a travel OTA with high average order values, installment coverage gaps directly reduce conversion.

SLIDE 1: PSP TOPOLOGY

PSP_1: Checkout.com
PSP_2: Adyen (Issuing + APMs)
PSP_3: TrueLayer (Open Banking)
PSP_4: Klarna (BNPL)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: iDEAL (Netherlands)
Local_M_2: Bancontact (Belgium)
Local_M_3: Giropay (Germany)
Local_M_4: EPS (Austria)
Local_M_5: Bizum (Spain)
Local_M_6: MB Way (Portugal)
Local_M_7: Satispay (Italy)
Local_M_8: Blik (Poland)
Local_M_9: Swish (Sweden)
Local_M_10: MobilePay (Denmark)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing Engine
Tittle_Yuno_Cap2: Failover & Cascade Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration Layer

Desc_Yuno_Cap1: Route each transaction to the best performing acquirer by market, card BIN, and currency in real time. With over 43M monthly unique users booking across 40+ countries, even a 1% authorization uplift on lastminute.com's estimated transaction volume translates to millions in recovered bookings. Smart Routing dynamically selects between Checkout.com and Adyen per transaction instead of static splits.
Desc_Yuno_Cap2: When Checkout.com declines a UK card or Adyen rejects a European transaction, Yuno automatically cascades to the next processor in milliseconds. TrueLayer's own data proved that during a payment outage, open banking usage spiked massively. Yuno makes this failover automatic: if cards fail, route to bank transfer. If one acquirer is down, cascade to another.
Desc_Yuno_Cap3: One API activates iDEAL for the Netherlands, Bancontact for Belgium, Giropay for Germany, EPS for Austria, Bizum for Spain, MB Way for Portugal, Blik for Poland, Swish for Sweden, and Satispay for Italy. Yuno connects 1,000+ payment methods across 40+ countries. No per market engineering sprints, no separate contracts. Instant activation for every lastminute.com brand.
Desc_Yuno_Cap4: Replace fragmented reconciliation across Checkout.com (card acquiring), Adyen (issuing + APMs), TrueLayer (open banking), and Klarna (BNPL) with a single dashboard. Real time approval rate monitoring across all 7+ brands and 40+ markets. Centralized settlement, unified analytics, and millisecond anomaly detection. One integration powering lastminute.com, Volagratis, Bravofly, Rumbo, and Jetcost simultaneously.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**lastminute.com at a glance:**
- Founded: 1998 by Martha Lane Fox and Brent Hoberman. Acquired by Bravofly Rumbo Group in 2015, rebranded as lastminute.com Group
- Headquarters: Chiasso, Switzerland
- CEO: Alessandro Petazzi (appointed January 2025)
- Listed on SIX Swiss Exchange as LMN
- Revenue: EUR 313.7M (FY2024), ~$407M trailing 12 months (Dec 2025)
- Gross Profit: EUR 130.9M (2024, +4% YoY)
- Adjusted EBITDA: EUR 41.2M (2024, +4% YoY)
- Net Profit: EUR 15.7M (2024, more than doubled from EUR 7M in 2023)
- 43 million monthly unique users
- Operates in 58 countries, 17 languages, 40+ active markets
- Brands: lastminute.com, Volagratis (Italy), Bravofly, Rumbo (Spain), Jetcost (metasearch, 38 countries), weg.de (Germany), Hotelscan, Crocierissime.it
- Core product: Dynamic Holiday Packages (flights + hotels)
- Largest European markets: UK, France, Germany, Italy, Spain

**Confirmed PSPs and payment partners:**

| Provider | Role | Region |
|----------|------|--------|
| Checkout.com | Primary card acquiring, global payment processing | All markets (appointed Nov 2024) |
| Adyen | Virtual card issuing for supplier payments, 4 new APMs integrated in 2025 | All markets |
| TrueLayer | Open banking / Pay by bank | UK, select EU markets |
| Klarna | BNPL (Pay Later, Pay in 3/4) | UK, Germany, France, Italy, Spain, Netherlands |
| Visa / Mastercard | Card networks | All markets |
| American Express | Card network | Select markets |
| Apple Pay | Mobile wallet | Select markets |
| Revolut | Digital banking card | Select markets |

**No payment orchestrator detected.** Each provider operates independently with no unified routing or failover.

**Key payment performance metrics:**
- Checkout.com integration delivered 1.9% increase in authorization rates
- Adyen integration reduced payment method launch time by 70% and costs by 60%
- Adyen virtual card issuing accelerated supplier payments by 2 to 3 days, reduced reconciliation time by 5%
- TrueLayer Pay by bank delivered 20% higher AOV vs other payment methods
- TrueLayer: 85% of open banking transactions come from returning customers
- During a payment outage, open banking saw a "massive spike" proving need for payment resilience

**Customer reported payment issues:**
- Checkout failures: payments charged but bookings unconfirmed for extended periods
- Duplicate authorizations: multiple charges for single bookings
- Card declines with no alternative payment path offered
- Poor communication after payment failures (emails ignored, weeks between responses)
- Sitejabber rating: 1.5 stars from 896 reviews, with payment and refund issues as top complaints
- MoneySavingExpert and TripAdvisor forums document persistent booking/payment mismatches

**Top Market Gap Analysis:**

MARKET 1: United Kingdom (largest market)
  Accepted: Visa, MC, Amex, Apple Pay, Klarna, TrueLayer (Pay by bank)
  Missing: Google Pay, Revolut Pay (standalone), Clearpay/Afterpay UK
  Insight: UK is best covered. TrueLayer open banking drives 20% higher AOV

MARKET 2: Germany (weg.de brand)
  Accepted: Visa, MC, Klarna
  Missing: Giropay, SEPA direct debit, PayPal, EPS (Austria), Sofort
  Insight: Germany's credit card penetration is low. Without Giropay and SEPA, significant share of German travelers cannot use preferred payment rails

MARKET 3: Italy (Volagratis brand)
  Accepted: Visa, MC, Klarna
  Missing: Satispay, Bancomat Pay, PostePay, PayPal
  Insight: PostePay is Italy's most used prepaid card. Satispay growing rapidly as mobile wallet

MARKET 4: Spain (Rumbo brand)
  Accepted: Visa, MC, Klarna
  Missing: Bizum (30M+ users in Spain), PayPal, Financiation options (Cetelem)
  Insight: Bizum dominates P2P and increasingly e-commerce in Spain. Missing it on a Spanish travel site is a major gap

MARKET 5: France
  Accepted: Visa, MC (Carte Bancaire via cobadge), Klarna
  Missing: Alma (BNPL), Oney (installments), PayPal
  Insight: French consumers expect installment options for travel. Alma and Oney are the local BNPL leaders

MARKET 6: Netherlands
  Accepted: Visa, MC, Klarna
  Missing: iDEAL (used for 70%+ of Dutch online payments), PayPal
  Insight: Not offering iDEAL in the Netherlands is like not accepting cards in the US. It is the dominant online payment method

MARKET 7: Poland (Jetcost)
  Accepted: Visa, MC
  Missing: Blik (90%+ of Polish mobile payments), PayPo (BNPL), P24 (Przelewy24)
  Insight: Blik processed 3.8B transactions in 2024. Without it, Polish travelers face unnecessary friction

**Key meeting angles:**
1. **Four PSPs, zero orchestration** | Checkout.com, Adyen, TrueLayer, and Klarna each run independently. No unified routing means no automatic failover when one provider goes down. The TrueLayer outage spike proves customers need it
2. **40+ markets, minimal localization** | Operating in 58 countries but missing iDEAL (NL), Giropay (DE), Bizum (ES), Blik (PL), MB Way (PT). Yuno activates all from a single API
3. **Multi brand complexity** | 7+ brands with separate checkout flows. A centralized orchestrator normalizes payment logic across lastminute.com, Volagratis, Bravofly, Rumbo, Jetcost, weg.de
4. **High AOV = high decline impact** | Travel bookings average EUR 500+. Every declined transaction is a lost holiday. Smart routing and cascade retries directly recover these high value sales
5. **1.9% auth uplift with Checkout.com alone** | If adding one PSP lifted auth rates 1.9%, intelligent routing across multiple processors can compound that further
6. **Supplier payment innovation** | Adyen issuing for virtual cards shows lastminute.com is actively modernizing payment infrastructure. Orchestration is the natural next step
7. **20% higher AOV via open banking** | TrueLayer proved that non card payment methods drive higher basket sizes. Expanding local methods market by market amplifies this effect

**Sources:**
- [Checkout.com: lastminute.com Appointment as Payment Provider (Nov 2024)](https://www.checkout.com/newsroom/lastminute-appoints-checkout-as-payments-provider)
- [Adyen: lastminute.com Virtual Card Issuing Partnership (Apr 2026)](https://www.adyen.com/press-and-media/adyen-expands-its-partnership-with-lastminute-com-with-adyen-issuing)
- [Adyen: lastminute.com Global Payment Upgrade Case Study](https://www.adyen.com/knowledge-hub/lastminute-global-payment-upgrade)
- [TrueLayer: lastminute.com Pay by Bank Case Study (20% Higher AOV)](https://truelayer.com/customers/customer-story-lastminute-com/)
- [Klarna: lastminute.com Pay Later (UK)](https://www.klarna.com/uk/store/11418eeb-b3f2-45c7-827c-d84ff4d73c3d/Lastminute.com/pay-with-klarna/)
- [Klarna: lastminute.com Pay Later (Ireland)](https://www.klarna.com/ie/store/0e335e19-b774-44a4-9031-4aa7539e8d72/lastminute.com/pay-with-klarna/)
- [lastminute.com Flexible Payment Options (Book Now Pay Later)](https://www.lastminute.com/holidays/deposit.html)
- [lastminute.com Q4 2024 & FY24 Preliminary Results](https://www.marketscreener.com/quote/stock/LASTMINUTE-COM-N-V-16268052/news/Lastminute-com-N-Q4-2024-FY24-Preliminary-unaudited-results-49042965/)
- [lastminute.com Revenue (Stock Analysis)](https://stockanalysis.com/quote/swx/LMN/revenue/)
- [lastminute.com Financial Releases](https://corporate.lastminute.com/investors/financial-releases/)
- [lastminute.com Executive Management](https://corporate.lastminute.com/investors/governance/executive-management/)
- [lastminute.com Wikipedia](https://en.wikipedia.org/wiki/Lastminute.com)
- [lastminute.com Group Wikipedia](https://en.wikipedia.org/wiki/Lastminute.com_Group)
- [Which Payment Types Does lastminute.com Accept](https://www.whoacceptsit.com/companies/lastminute.com/534/)
- [MoneySavingExpert: lastminute.com Problems](https://forums.moneysavingexpert.com/discussion/6038155/problem-with-lastminute-com)
- [TripAdvisor: lastminute.com Problems](https://www.tripadvisor.co.uk/ShowTopic-g1-i10702-k7138636-o10-Lastminute_com_problems-Air_Travel.html)
- [Sitejabber: lastminute.com Reviews](https://www.sitejabber.com/reviews/lastminute.com)
- [Colt: lm group Brands Overview](https://www.colt.net/customer-stories/lm-group-lastminute-com-volagratis-rumbo-weg-de-bravofly-jetcost-e-hotelscan)
- [lastminute.com Logo (Wikimedia Commons)](https://commons.wikimedia.org/wiki/Category:Lastminute.com)
