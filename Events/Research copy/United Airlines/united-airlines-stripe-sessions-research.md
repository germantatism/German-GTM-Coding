# UNITED AIRLINES | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: United Airlines
=======================================

Logo: https://companieslogo.com/img/orig/UAL-acde1709.png
Nombre merchant: United Airlines

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Checkout Error Black Hole
Tittle_Pain Point_2: Intl Card Decline Pattern
Tittle_Pain Point_3: No Orchestration Layer
Tittle_Pain Point_4: Local APM Gaps Worldwide
Tittle_Pain Point_5: BNPL Limited to Uplift

Desc_Pain Point_1: Travelers report persistent "error processing payment" on united.com and the United app, regardless of payment method. FlyerTalk threads document users unable to complete bookings with any card. No retry logic or automatic cascade to an alternative. YouTube tutorials address the issue, signaling chronic volume.
Desc_Pain Point_2: United flies to 151 international destinations in 74 countries, but foreign issued cards are frequently declined on united.com. Banks flag airline transactions as high risk cross border purchases. Billing address mismatches between card country and booking origin trigger automatic rejections with no recovery path.
Desc_Pain Point_3: No payment orchestration platform publicly confirmed for United Airlines. With $59.1B in 2025 revenue and 130M+ MileagePlus members transacting across 74 countries, the absence of smart routing and failover means each declined ticket is hundreds of dollars in lost revenue with no automatic retry.
Desc_Pain Point_4: United.com accepts cards, PayPal, Apple Pay, Google Pay, and Uplift BNPL for US bookings. But travelers booking from Brazil, Poland, Netherlands, Japan, and South Korea cannot use PIX, BLIK, iDEAL, PayPay, or KakaoPay. Competitors like KLM accept iDEAL, PIX, and WeChat Pay natively.
Desc_Pain Point_5: United partners with Uplift for monthly installments (up to 11 months, 0 to 36% APR). No Afterpay, Klarna, or Zip at checkout. Uplift is US only. With PS5 level ticket prices ($300 to $2,000+), international travelers have no BNPL option, limiting conversion on high value bookings.

SLIDE 1: PSP TOPOLOGY

PSP_1: Undisclosed Acquirer(s) PSP_2: PayPal PSP_3: Uplift (BNPL) PSP_4: UATP

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: PIX (Brazil)
Local_M_2: BLIK (Poland)
Local_M_3: iDEAL (Netherlands)
Local_M_4: Boleto (Brazil)
Local_M_5: KakaoPay (South Korea)
Local_M_6: PayPay (Japan)
Local_M_7: WeChat Pay (China)
Local_M_8: Alipay (China)
Local_M_9: Trustly (Europe)
Local_M_10: MB Way (Portugal)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing Engine
Tittle_Yuno_Cap2: Failover + NOVA Recovery
Tittle_Yuno_Cap3: 1,000+ Local APMs
Tittle_Yuno_Cap4: Unified Global Dashboard

Desc_Yuno_Cap1: Route each flight booking transaction to the optimal acquirer per card BIN, issuer, and booking origin country. With $59.1B in annual revenue across 74 countries and average ticket values of $300 to $2,000+, even a 1% auth uplift recovers hundreds of millions. Smart Routing boosts approval rates 3 to 10%.
Desc_Yuno_Cap2: When a card is declined during flight checkout, Yuno cascades instantly to an alternative acquirer or payment method. NOVA AI recovers up to 75% of soft declines, replacing dead end error pages with automatic retry. Livelo recovered 50% of failed transactions with this exact approach. Wingo airline uses Yuno for flight payments.
Desc_Yuno_Cap3: Activate PIX in Brazil, BLIK in Poland, iDEAL in Netherlands, KakaoPay in South Korea, PayPay in Japan, and WeChat Pay/Alipay for Chinese travelers. One API integration, no per market engineering. InDrive launched 10 LATAM markets in under 8 months via Yuno's single connection.
Desc_Yuno_Cap4: Replace siloed regional payment configurations with one real time dashboard across all 74 booking markets. Centralized approval rate monitoring for 130M+ MileagePlus members worldwide. Millisecond anomaly detection catches payment issues before they cascade during peak booking periods, holiday surges, and fare sales.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**United Airlines at a glance:**
- NASDAQ: UAL. Largest US airline by international destinations
- FY2025 Total Operating Revenue: $59.1B (up 3.5% YoY, record annual revenue)
- Q1 2026 Total Operating Revenue: $14.6B (up 10.6% YoY, exceeded analyst estimates)
- Q1 2026 EPS: $2.14 (up 85% YoY). Adjusted EPS: $1.19 (up 31%, beat consensus)
- Q1 2026 Pre tax Earnings: $0.9B, 6.0% pre tax margin (up 2.3pp YoY)
- Loyalty Revenue Q4 2025: $1.5B (up 9% YoY). Full year loyalty up 9%
- MileagePlus Members: 130M+
- International Destinations: 151 in 74 countries
- Fleet: 8 hubs (Denver, Chicago O'Hare, Newark, Houston, San Francisco, Washington Dulles, Los Angeles, Guam)
- 760+ weekly transatlantic flights (most of any US airline)
- Q1 2026 domestic unit revenue up 7.9% to $7.9B
- Adjusted FY2026 EPS guidance: $7 to $11 (lowered from $12 to $14 due to fuel costs and geopolitical uncertainty)

**Confirmed PSPs and Payment Infrastructure:**
- Acquirer(s): Not publicly disclosed. United likely uses one or more major acquirers (Cybersource/Visa, Adyen, or WorldPay are common in airlines) but no confirmation found
- PayPal: Confirmed for flight bookings on united.com
- Apple Pay: Confirmed in United app for US billing addresses
- Google Pay: Confirmed for online bookings
- Uplift: BNPL partner. Pay monthly over up to 11 months. 0% to 36% APR. Available for US to any United destination bookings. Transactions $100 to $25,000
- UATP (Universal Air Travel Plan): Industry payment network for airline tickets
- United TravelBank: Prepaid travel credit account
- MileagePlus Awards: Miles can be used for ticket purchases
- Chase United Co Brand Cards: Co branded credit cards via Chase bank
- No Klarna, Afterpay, Zip, or Affirm directly at checkout
- No payment orchestration platform confirmed (Spreedly, Primer, Gr4vy, CellPoint, APEXX, or Yuno)

**Payment Methods by Booking Origin:**

MARKET: United States (primary, ~$7.9B domestic unit revenue Q1 alone)
  Accepted: Visa, Mastercard, Amex, Discover, PayPal, Apple Pay, Google Pay, Uplift BNPL, MileagePlus, TravelBank
  Coverage: Strong. Multiple payment options and BNPL available

MARKET: Europe (760+ weekly transatlantic flights)
  Accepted: Visa, Mastercard, PayPal
  Missing: iDEAL (Netherlands), BLIK (Poland), Giropay (Germany), Bancontact (Belgium), Trustly, MB Way (Portugal)
  Note: KLM accepts iDEAL, PIX, and multiple local methods. United does not

MARKET: Brazil (Houston hub connections to LATAM)
  Accepted: Visa, Mastercard
  Missing: PIX (150M+ users), Boleto Bancario, local credit installments
  Note: PIX is now accepted by KLM, Air France, and Emirates for Brazilian travelers

MARKET: Japan (San Francisco/LA hub connections)
  Accepted: Visa, Mastercard
  Missing: PayPay (70M+ users), LINE Pay, Rakuten Pay, Konbini
  Note: Japanese travelers increasingly prefer local wallets for large purchases

MARKET: South Korea
  Accepted: Visa, Mastercard
  Missing: KakaoPay, NaverPay, Toss
  Note: Korean local wallets dominate online transactions

MARKET: China (routes from SFO/LAX)
  Accepted: Visa, Mastercard, UnionPay (likely)
  Missing: Alipay, WeChat Pay
  Note: Air France and KLM accept Alipay and WeChat Pay natively

**Payment Issues and Incidents:**
- United.com checkout errors: FlyerTalk forums document users receiving "error processing payment" regardless of card used (Visa, Amex, Mastercard all fail). No specific error code given. Users report the issue persisting across browsers and devices
- United App payment processing errors (2025): Widespread enough that a YouTube tutorial was published in August 2025 specifically addressing how to fix payment processing errors on the United Airlines app
- International card declines: Travelers report cards being declined on united.com when booking from outside the US. Banks flag airline purchases as high risk cross border transactions. Billing address country must often match booking region
- Miles and Money booking failures: Users report inability to complete mixed payment (miles + card) bookings, with the system freezing during payment processing. No alternative offered
- Held/duplicate charges: United support documents cases of held funds, pending, or duplicate charges appearing when payment processing encounters delays

**Key meeting angles:**
1. **$59.1B revenue, 74 countries, no orchestration** | United is the largest US international airline, flying to 151 destinations. Every declined booking is $300 to $2,000+ in lost revenue. Smart routing and failover could recover millions from soft declines that currently result in dead end error pages.
2. **Competitors already accept local APMs** | KLM accepts iDEAL, PIX, WeChat Pay, and Alipay. Air France accepts WeChat Pay, Alipay, and KakaoPay. Etihad accepts UPI and iDEAL. United accepts none of these. Travelers from key international markets face cards only, creating a conversion ceiling vs European carriers.
3. **130M MileagePlus members, loyalty revenue growing 9%** | Loyalty revenue hit $1.5B in Q4 2025. MileagePlus members booking with miles + card face payment processing freezes. An orchestration layer ensures the payment portion of mixed transactions processes reliably, protecting loyalty program engagement.
4. **BNPL gap for international travelers** | Uplift is US only with variable APR (0 to 36%). Klarna, Afterpay, and Zip are absent. Wingo (Yuno client) offers seamless BNPL for flight bookings. With ticket prices from $300 to $2,000+, international BNPL could unlock bookings from price sensitive markets.
5. **Peak booking surges amplify failures** | Holiday surges, fare sales, and route launches drive booking spikes. Without smart routing to distribute load across acquirers, peak periods increase decline rates. Yuno's real time routing optimizes processor selection during volume spikes, maintaining auth rates under pressure.

**United Airlines Leadership:**
- Scott Kirby: CEO, United Airlines Holdings
- Andrew Nocella: President, United Airlines
- Mike Leskinen: EVP and CFO (since 2024, previously SVP of Corporate Development)
- Brett Hart: Vice Chairman and Chief Administrative Officer
- Linda Jojo: EVP and Chief Customer Officer. Previously CIO, leading digital transformation
- Jason Birnbaum: SVP and CIO (since 2023)
- No dedicated VP of Payments identified in public sources

**Recent corporate developments:**
- April 2026: Q1 2026 results beat estimates. Revenue $14.6B (up 10.6%), EPS $2.14 (up 85%). Lowered full year guidance to $7 to $11 per share due to fuel costs and geopolitical risks
- FY2025: Record annual revenue of $59.1B (up 3.5%). Loyalty revenue up 9% for the year
- 2025: Enhanced MileagePlus, offering up to 2x miles per dollar for primary cardholders, 10%+ off award tickets
- 2025: 130M+ MileagePlus members
- United plans to expand free fast Wi Fi to entire fleet by end of 2027 for MileagePlus members
- United operates 760+ weekly transatlantic flights, most of any US airline
- Strategic focus: "Winning brand loyal customers" per CEO Scott Kirby

**Sources:**
- [United Airlines Q1 2026 Earnings (CNBC)](https://www.cnbc.com/2026/04/21/united-airlines-ual-q1-2026-earnings.html)
- [United Airlines Q1 2026 Strong Quarter (Travel and Tour World)](https://www.travelandtourworld.com/news/article/united-airlines-reports-strong-first-quarter-in-2026-with-record-revenue-and-enhanced-customer-experience-amid-rising-fuel-costs-and-expanded-fleet-initiatives/)
- [United Airlines Q1 2026 Earnings Release (PR Newswire)](https://www.prnewswire.com/news-releases/uniteds-long-term-strategy-remains-focused-on-winning-brand-loyal-customers-boosted-by-q1-growth-in-earnings-and-margins-302749229.html)
- [United Airlines 2025 Record Revenue (Aerotime)](https://www.aerotime.aero/articles/united-2025-earnings-record-revenue-2026-outlook)
- [United Airlines Q4 FY2025 Earnings (IR)](https://ir.united.com/static-files/a37e057c-8ccf-41a8-ac93-4263f0527cc1)
- [United Airlines Q1 2026 (TIKR)](https://www.tikr.com/blog/united-airlines-rallied-from-its-march-lows-what-q1-earnings-mean-for-united-airlines-in-2026)
- [United Airlines 2026 Outlook Cut (Yahoo Finance)](https://finance.yahoo.com/markets/stocks/articles/united-airlines-cuts-2026-earnings-204252734.html)
- [United Airlines Revenue (MacroTrends)](https://www.macrotrends.net/stocks/charts/UAL/united-airlines-holdings-inc/revenue)
- [United Airlines Payment Methods (united.com)](https://www.united.com/en/us/fly/travel/trip-planning/payment-methods.html)
- [United Airlines Uplift BNPL (united.com)](https://www.united.com/ual/en/us/fly/booking/flight/uplift.html)
- [United Fly Now Pay Later (Alternative Airlines)](https://www.alternativeairlines.com/fly-now-pay-later-united-airlines)
- [United Airlines BNPL Options (Gerald)](https://joingerald.com/blog/united-airlines-buy-now-pay-later)
- [United Airlines Uplift (UATP)](https://uatp.com/news/united-airlines-uplift-offer-fly-now-pay-later-option/)
- [United Airlines Checkout Error (FlyerTalk)](https://www.flyertalk.com/forum/united-airlines-mileageplus/2018998-error-booking-united-com-when-processing-payment-any-form.html)
- [United Airlines App Payment Error Fix (YouTube)](https://www.youtube.com/watch?v=Pyr1PkOAXq0)
- [United Airlines Payment Declined (Sociomix)](https://www.sociomix.com/c/stories/what-to-do-if-united-airlines-doesn-t-accept-your-payment/1759873624)
- [United Airlines MileagePlus (The Points Guy)](https://thepointsguy.com/loyalty-programs/know-united-mileageplus/)
- [United Airlines Loyalty vs Rewards (PYMNTS)](https://www.pymnts.com/news/loyalty-and-rewards-news/2026/united-airlines-distinguishes-between-loyalty-rewards-programs)
- [United Airlines Routes (FlightConnections)](https://www.flightconnections.com/route-map-united-airlines-ua)
- [United Airlines Top 20 International Routes (Aviation A2Z)](https://aviationa2z.com/index.php/2025/04/09/united-top-20-busiest-international-routes-2025/)
- [KLM Payment Methods](https://www.klm.co.uk/information/ticket-services/payment-methods)
- [Air France Payment Methods](https://wwws.airfrance.fr/en/information/legal/moyens-de-paiement)
- [Etihad Payment Options](https://www.etihad.com/en/manage/payment-options)
- [Emirates Payment Options](https://www.emirates.com/us/english/book/about-booking-online/payment-options/)
- [Airline Credit Card Model (Cranky Flier)](https://crankyflier.com/2025/03/24/how-the-airline-credit-card-financial-model-works-very-well-thanks-for-asking/)
- [Adyen Airlines Landing (Adyen)](https://www.adyen.com/landing/airlines)
- [United Airlines Logo (CompaniesLogo)](https://companieslogo.com/united-airlines/logo/)
