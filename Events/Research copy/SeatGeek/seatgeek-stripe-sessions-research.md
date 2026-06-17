# SEATGEEK | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: SEATGEEK
=======================================

Logo: https://brandfetch.com/seatgeek.com
Nombre merchant: SEATGEEK

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Stripe Single PSP Lock-In
Tittle_Pain Point_2: Intl Payment Walls
Tittle_Pain Point_3: No Local APMs at Checkout
Tittle_Pain Point_4: Cross Border Decline Rates
Tittle_Pain Point_5: Fee Pressure Margin Squeeze

Desc_Pain Point_1: SeatGeek runs its entire marketplace and enterprise ticketing payment infrastructure on Stripe Connect as the sole payment processor. Every ticket purchase, seller payout, and Affirm BNPL transaction routes through Stripe. If Stripe declines a transaction or experiences downtime, there is no cascade to a second acquirer. With 500+ enterprise clients including Dallas Cowboys and half the Premier League, a single PSP failure impacts millions of fans.
Desc_Pain Point_2: SeatGeek operates across the US, UK, Netherlands, Australia, and Israel, but only accepts US, Mexico, and Canadian credit and debit cards for most purchases. Partnered Teams can accept international cards, but the standard marketplace blocks fans in Europe, Asia, and LATAM from buying tickets. A Liverpool supporter in Germany or a Manchester City fan in Japan cannot easily purchase through SeatGeek.
Desc_Pain Point_3: SeatGeek checkout accepts Visa, Mastercard, Amex, and Affirm BNPL. No iDEAL for Dutch fans (despite SeatGeek's Dutch Football Association partnership with 15+ clubs). No SEPA for German or French ticket buyers. No Pix for Brazilian fans. No local wallet payments anywhere. SeatGeek powers half the Premier League but cannot process local European payment methods.
Desc_Pain Point_4: SeatGeek's previous payment provider had "relatively low authorization rates due to false declines." Stripe's Adaptive Acceptance improved auth rates by over 1%, but cross-border tickets still face higher decline rates. A fan in the UK buying Dallas Cowboys tickets processes through a single acquirer path with no BIN-level optimization for the international card. Each declined ticket is an empty seat.
Desc_Pain Point_5: The FTC now requires all-in pricing, and SeatGeek's buyer fees of 10-48% are visible upfront. Seller commissions run 10-15%. StubHub's market share grew to 30-40% by competing on transparency. Payment processing cost optimization through smart routing could reduce SeatGeek's cost per transaction, enabling either better margins or lower fees to compete against StubHub and Ticketmaster.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe Connect (sole payment processor)
PSP_2: Affirm (BNPL via Stripe Payments)
PSP_3: Stripe Adaptive Acceptance (auth optimization)
PSP_4: Stripe Identity (seller KYC/onboarding)
PSP_5: Stripe Tax (1099-K reporting)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: iDEAL (Netherlands)
Local_M_2: SEPA Direct Debit (EU)
Local_M_3: Bancontact (Belgium)
Local_M_4: Pix (Brazil)
Local_M_5: Klarna (EU/US BNPL)
Local_M_6: Giropay (Germany)
Local_M_7: GrabPay (SEA)
Local_M_8: Mada (Saudi Arabia)
Local_M_9: Boleto (Brazil)
Local_M_10: PayPal (global wallet)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing Engine
Tittle_Yuno_Cap2: Failover Cascade Retries
Tittle_Yuno_Cap3: 1,000+ Payment Methods
Tittle_Yuno_Cap4: Marketplace Orchestration

Desc_Yuno_Cap1: Route every ticket payment to the optimal acquirer by fan card BIN, currency, and buyer country in real time. SeatGeek's Stripe Adaptive Acceptance improved auth rates by 1%, but true multi-acquirer routing pushes 3-10% uplift by selecting the best processor per transaction. With 500+ enterprise clients and millions of ticket transactions, each percentage point in authorization recovery translates to thousands of additional tickets sold.
Desc_Yuno_Cap2: When Stripe declines a fan's card or returns a soft decline, Yuno cascades to the next best processor in milliseconds. A fan buying $200 Cowboys playoff tickets who hits a payment decline will not wait or retry. With Yuno, the transaction automatically retries through an alternative acquirer before the fan sees a failure. Every recovered authorization is a filled seat and revenue for both SeatGeek and its enterprise partners.
Desc_Yuno_Cap3: One API activates iDEAL for Dutch fans (SeatGeek has 15+ Dutch football clubs), SEPA and Giropay for German ticket buyers, Bancontact for Belgium, Pix for Brazil, Klarna for additional BNPL, Mada for Saudi Arabia, and GrabPay across SEA. Yuno connects 1,000+ local payment methods across 40+ countries. SeatGeek's Premier League and European partners get instant local payment access for their fans.
Desc_Yuno_Cap4: Add a multi-acquirer orchestration layer on top of Stripe Connect without replacing it. Yuno routes marketplace transactions across Stripe and additional processors, providing authorization uplift, failover resilience, and local acquiring in every market where SeatGeek operates. Unified fraud scoring (NOVA, 75% fraud reduction), centralized settlement across all PSPs, and real time dashboards spanning every enterprise client from the Dallas Cowboys to Liverpool FC.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**SEATGEEK at a glance:**
- Founded: 2009 in Philadelphia by Jack Groetzinger (CEO) and Russell D'Souza, with Eric Waller as third co-founder
- Headquarters: New York City
- International offices: UK, Israel, Netherlands, Australia, Italy
- Revenue: $184.1M (2023, most recent available)
- Valuation: $1.2B
- Total funding: $398M over 10 rounds from 47 investors (Accel, Founder Collective, Glynn Capital)
- ~785 employees (as of March 2026)
- Private company (planned SPAC merger in 2021 was withdrawn)
- Dual business: consumer ticket marketplace + SeatGeek Enterprise (primary ticketing technology)
- SeatGeek Enterprise: 500+ clients across 4 continents
- Official ticketing partner of MLS
- TopTix acquisition (2017, $56M) for EMEA expansion

**Enterprise ticketing clients (selected):**
- NFL: Dallas Cowboys, Arizona Cardinals, New Orleans Saints, Baltimore Ravens
- NBA: Cleveland Cavaliers, New Orleans Pelicans
- NHL: Florida Panthers
- English Premier League: Liverpool FC, Manchester City FC, and majority of EPL clubs
- Dutch Football Association (15+ participating clubs)
- MLS: Official partner + Philadelphia Union (2026), Minnesota United, Portland Timbers
- Venues: AT&T Stadium, Rocket Mortgage FieldHouse, Lord's Cricket Ground
- Entertainment: Andrew Lloyd Webber Theatre Group (London West End)

**Confirmed PSPs and payment partners:**

| Provider | Role | Scope |
|----------|------|-------|
| Stripe Connect | Sole payment processor for marketplace + enterprise | Global |
| Affirm | BNPL via Stripe Payments | US |
| Stripe Adaptive Acceptance | Authorization optimization | Global |
| Stripe Identity | Seller KYC and onboarding verification | Global |
| Stripe Tax | 1099-K tax reporting for sellers | US |

**Payment methods accepted:**
- Visa, Mastercard, American Express (US, Mexico, Canada debit/credit cards for most purchases)
- Affirm (BNPL, US only)
- Partnered Teams: can accept international cards via app/web
- No PayPal, no Apple Pay, no Google Pay at checkout (confirmed)
- No local European payment methods (no iDEAL, no SEPA, no Giropay, no Bancontact)
- No LATAM or Asia payment methods
- Seller payouts: bank transfer only

**Stripe partnership performance metrics:**
- Affirm BNPL: conversion rates increased by up to 2%
- Affirm order values: up to 50% higher than other payment methods
- Affirm share of sales doubled when messaging added to event detail page
- Adaptive Acceptance: authorization rates increased by over 1%
- Previous payment provider had "relatively low authorization rates due to false declines"

**Fee structure (post-FTC all-in pricing mandate, May 2025):**
- Buyer fees: 10-48% (now disclosed upfront)
- Seller commission: 10-15% of sale price
- FTC rule requires total cost displayed before payment
- Expected ~10% revenue dip industry-wide from upfront fee transparency

**Competitive landscape:**
- Ticketmaster/Live Nation: dominant primary ticketing (DOJ antitrust lawsuit filed)
- StubHub: market share grew to 30-40% (was 10-15% during pandemic)
- Vivid Seats, Gametime: rising competitors
- CTS Eventim: European dominant player
- Key SeatGeek differentiator: open API platform, modern technology, enterprise partnerships

**Key meeting angles:**
1. **500+ enterprise clients at stake** | SeatGeek powers ticketing for the Dallas Cowboys, Liverpool FC, half the Premier League, and MLS. Payment orchestration improves authorization for every enterprise partner simultaneously, translating to more filled seats and higher GMV
2. **Stripe single-point-of-failure** | Every ticket transaction runs through Stripe Connect exclusively. No failover, no cascade, no multi-acquirer routing. Yuno adds resilience and optimization on top of Stripe without replacing it
3. **European expansion blind spot** | SeatGeek is the primary ticketer for half the Premier League and 15+ Dutch football clubs but cannot accept iDEAL, SEPA, or Giropay at checkout. European fans must use cards only. Yuno's 1,000+ APMs unlock local payment for every European partner
4. **Auth rate headroom** | Stripe's Adaptive Acceptance delivered 1% auth uplift. Multi-acquirer smart routing delivers 3-10%. On millions of ticket transactions, the incremental 2-9% gap is worth substantial revenue. Each recovered decline is a ticket sold
5. **Fee pressure solution** | With FTC all-in pricing and StubHub gaining share, SeatGeek needs cost efficiency. Smart routing to the cheapest acquirer per transaction reduces processing costs, enabling fee competitiveness against StubHub and Ticketmaster
6. **BNPL success proves APM value** | Affirm drove 2% conversion uplift and 50% higher AOV. If one BNPL method delivers this impact, adding iDEAL, SEPA, Klarna, Pix, and 1,000+ more methods through Yuno would compound the effect across every market
7. **$1.2B valuation, growth mode** | SeatGeek is positioning for global expansion with enterprise deals across 4 continents. Payment orchestration is the infrastructure that enables seamless international ticketing without per-market PSP integrations

**Sources:**
- [SeatGeek + Stripe Connect Case Study (Stripe)](https://stripe.com/customers/seatgeek)
- [SeatGeek + Affirm BNPL Partnership (Payments Dive)](https://www.paymentsdive.com/news/seatgeek-taps-affirm-for-event-bnpl-payments/627329/)
- [Affirm Lifts Conversion for SeatGeek (Affirm Blog)](https://www.affirm.com/business/blog/affirm-lifts-conversion-and-average-order-value-for-seatgeek-while-reaching-valuable-consumers)
- [SeatGeek Affirm FAQs (Help Center)](https://support.seatgeek.com/hc/en-us/articles/6052316160659-Paying-with-Affirm-FAQs)
- [SeatGeek Payment Options (Help Center)](https://seatgeek.com/help/articles/8985524266515-Account-and-payment-options)
- [SeatGeek + Dallas Cowboys Partnership](https://seatgeek.com/press/seatgeek-announces-industry-shifting-primary-ticketing-partnership-with-dallas-cowboys)
- [SeatGeek + Manchester City FC (Press)](https://seatgeek.com/press/seatgeek-announces-new-ticketing-partnership-with-manchester-city-fc)
- [SeatGeek UK EPL Influence (Boardroom)](https://boardroom.tv/seatgeek-uk-peter-joyce-interview/)
- [SeatGeek Open Platform (ChairNerd)](https://chairnerd.seatgeek.com/announcing-seatgeek-open-the-platform-powering-the-future-of-ticketing/)
- [SeatGeek Enterprise Page](https://seatgeek.com/enterprise)
- [SeatGeek on AWS (.NET platform)](https://aws.amazon.com/solutions/case-studies/seatgeek/)
- [SeatGeek Wikipedia](https://en.wikipedia.org/wiki/SeatGeek)
- [SeatGeek on Crunchbase](https://www.crunchbase.com/organization/seatgeek)
- [SeatGeek on Tracxn](https://tracxn.com/d/companies/seatgeek/__hHr24QyuMnSsi9oGgSUeVliezRnJNCn9S3KgiMX5zRA)
- [SeatGeek Revenue (Latka)](https://getlatka.com/companies/seatgeek.com)
- [SeatGeek + StubHub All-In Pricing (Digital Music News)](https://www.digitalmusicnews.com/2025/05/14/seatgeek-stubhub-all-in-ticket-pricing/)
- [FTC Ticket Pricing Rule (CNBC)](https://www.cnbc.com/2025/05/13/ftcs-new-rule-on-ticket-prices-wont-bring-costs-down-experts-say.html)
- [StubHub vs Ticketmaster vs SeatGeek (Sportico)](https://www.sportico.com/business/commerce/2025/ticketmaster-vs-stubhub-sports-tickets-buying-online-1234789624/)
- [SeatGeek Contrary Research](https://research.contrary.com/company/seatgeek)
- [SeatGeek Logo (Brandfetch)](https://brandfetch.com/seatgeek.com)
