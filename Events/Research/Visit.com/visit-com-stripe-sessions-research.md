# VISIT GROUP (Visit.com) | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Visit Group (Visit.com)
=======================================

Logo: https://cdn.brandfetch.io/visitgroup.com/w/512/h/512/theme/dark/icon.jpeg
Nombre merchant: Visit Group (Visit.com)

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Multi-PSP Fragmentation
Tittle_Pain Point_2: Nordic Payment Lock-In
Tittle_Pain Point_3: Cross-Border Checkout Gap
Tittle_Pain Point_4: Package Payment Friction
Tittle_Pain Point_5: No Smart Routing Layer

Desc_Pain Point_1: Visit Group runs Nets, Adyen, Klarna, and Swedbank Pay across iTicket, Citybreak, and BookVisit with no unified orchestration. Each platform manages its own PSP relationships independently, creating fragmented approval rate data across 2,200+ customers in 25+ countries and 258M SEK in annual revenue.
Desc_Pain Point_2: Swedbank Pay and Nets dominate Visit Group's checkout, limiting international tourists who need non-Nordic payment methods. The Softpay partnership adds tap-to-phone but only supports Visa, Mastercard, Dankort, and BankAxept. Chinese, Indian, and Latin American tourists visiting Nordic attractions cannot pay with their preferred wallets.
Desc_Pain Point_3: With 2,200+ customers across 25+ countries and global expansion plans under new CEO Richard Wiegmann, Visit Group's payment stack remains Nordic-centric. Hotels, theme parks, and ski resorts serving international visitors lack local APMs for key inbound tourist segments. No Alipay, WeChat Pay, UPI, or Pix at checkout.
Desc_Pain Point_4: iTicket and Citybreak enable complex packaging (hotels + tickets + activities + transport) but the checkout handles multi-supplier payments through fragmented PSP integrations. When a guest books a package spanning multiple suppliers, reconciliation and settlement across different PSPs creates operational overhead.
Desc_Pain Point_5: Despite integrating Adyen, Nets, Klarna, and Swedbank Pay, Visit Group has no intelligent routing layer to send each transaction to the optimal acquirer. Approval rates vary by card issuer, BIN, and market, but transactions follow static PSP assignments rather than dynamic optimization across the four providers.

SLIDE 1: PSP TOPOLOGY

PSP_1: Adyen (primary PSP, Citybreak + iTicket)
PSP_2: Nets (Nordic card processing)
PSP_3: Swedbank Pay (Nordic payments)
PSP_4: Klarna (BNPL)
PSP_5: Softpay (tap-to-phone POS)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Alipay
Local_M_2: WeChat Pay
Local_M_3: UPI
Local_M_4: Pix
Local_M_5: iDEAL
Local_M_6: Bancontact
Local_M_7: Cartes Bancaires
Local_M_8: GrabPay
Local_M_9: Mercado Pago
Local_M_10: Toss Pay

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Recovery
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across Adyen, Nets, Swedbank Pay, and Klarna for every booking, ticket, and package sale. Each transaction routed to the highest performing acquirer for that card BIN, issuer, and market. Across 2,200+ customers processing hotel reservations, theme park tickets, ski passes, and ferry bookings, smart routing delivers +3 to 10% auth uplift, recovering significant revenue on failed transactions.
Desc_Yuno_Cap2: Automatic cascade across Visit Group's four PSPs eliminates single-processor dependency. When Adyen declines, Yuno reroutes to Nets or Swedbank Pay in milliseconds. Up to 50% recovery on soft declines via instant retry. NOVA AI recovers up to 75% of failed transactions. For time-sensitive bookings (ski passes, theme park entries, ferry departures), a failed payment means an empty seat.
Desc_Yuno_Cap3: Activates the APMs Visit Group needs for international tourism: Alipay and WeChat Pay for Chinese tourists visiting Nordic attractions, UPI for Indian visitors, Pix for Brazilian travelers, iDEAL for Dutch guests, Cartes Bancaires for French tourists, Bancontact for Belgian visitors, GrabPay for Southeast Asian travelers. One API, 1,000+ payment methods across the entire ecosystem.
Desc_Yuno_Cap4: One dashboard replacing Visit Group's fragmented Adyen + Nets + Swedbank Pay + Klarna + Softpay stack across iTicket, Citybreak, and BookVisit. Real-time approval rate monitoring across 2,200+ customers in 25+ countries, centralized reconciliation for multi-supplier packages, and millisecond anomaly detection via Monitors. Simplifies payment operations as Visit Group scales globally under new leadership.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Visit Group at a glance:**
- Model: Hospitality SaaS ecosystem (e-commerce, ticketing, booking, packaging, distribution)
- Domain: Visit.com redirects to visitgroup.com
- Annual Revenue: 258M SEK (~$25M USD) as of December 2023
- Customers: 2,200+ across 25+ countries
- Employees: 350+ across 10+ countries
- Headquarters: Gothenburg, Sweden (offices in Stockholm, Nantes, Belgrade, Riga)
- Founded: 1999 by Magnus Emilson (Founder & Executive Chairman)
- CEO: Richard Wiegmann (appointed February 2026, previously at Amadeus, Sabre, Travelport, Expedia, Dertour)
- COO: James Dixon (former CEO)
- Funding: 100M+ EUR strategic growth investment from PSG Equity (January 2024)
- Previous investor: Standout Capital (Nordic technology investor)
- PSG's first platform investment in Sweden and Norway, 24th in Europe
- 20+ years of industry experience

**Core Products:**
- Citybreak: Central reservation system, multi-product packaging, distribution to 300+ operators with 100+ external inventory platforms
- iTicket: Cloud-based ticketing and packaging for attractions, tours, theme parks (100+ customers)
- BookVisit: Fastest growing accommodation distribution platform in the Nordics (est. 2012)
- VisBook: Hotel property management system
- Olery: Reputation management and analytics
- GODO: Hospitality software (acquired, leading vendor in Iceland)
- Travia: B2B connection platform for travel agencies and hotels

**Recent Developments:**
- February 2026: Richard Wiegmann appointed CEO (from Amadeus, Sabre, Travelport, Expedia background; led 19 company acquisitions)
- December 2025: Merged BookVisit and iTicket into unified booking flow (hotels + attractions in one checkout)
- 2024: Acquired GODO (leading hospitality software vendor in Iceland)
- January 2024: 100M+ EUR investment from PSG Equity (majority stake acquisition)
- Softpay partnership: Tap-to-phone payment integration for travel and hospitality

**Notable Customers:**
- Liseberg (Gothenburg theme park)
- Universeum (science center)
- Stromma Group (sightseeing operator)
- Flamsbana (scenic railway)
- Alpinco (ski resorts)
- SkiStar (ski resorts)
- Viking Line (ferries)
- DFDS (ferries)
- Hemavan (ski resort)
- Tree Hotel, Icehotel (unique accommodations)
- Visit Tromso (DMO)
- Wasaline (ferry operator)
- Moominworld (theme park)

**Distribution Network:**
- 15,000+ registered partners including Expedia, GetYourGuide, TripAdvisor, and tour operators
- 300+ Citybreak operators
- 100+ external inventory platform integrations

**Payments Infrastructure:**
- Adyen: Primary PSP integrated with Citybreak and iTicket
- Nets: Nordic card processing
- Swedbank Pay: Nordic payment solution
- Klarna: BNPL option
- Softpay: Tap-to-phone POS (Visa, Mastercard, Dankort, BankAxept, Discover, Diners Club, Amex, Apple Pay, Google Pay, Samsung Pay)
- No unified payment orchestration across platforms
- No smart routing between PSPs

**Payment Methods (Current):**
- Credit/debit cards: Visa, Mastercard, Amex, Discover, Diners Club
- Nordic cards: Dankort (Denmark), BankAxept (Norway)
- Digital wallets: Apple Pay, Google Pay, Samsung Pay (via Softpay)
- BNPL: Klarna
- No international tourist wallets (Alipay, WeChat Pay, UPI)

**Top 5 Markets Gap Analysis:**

MARKET 1: Nordics (Sweden, Norway, Denmark, Finland, Iceland - primary market)
  Currently offer: Visa/MC/Amex, Dankort, BankAxept, Klarna, Swedbank Pay, Apple Pay, Google Pay
  Missing: Vipps (Norway), MobilePay (Denmark), Swish direct integration
  Strong in local Nordic methods but fragmented across PSPs with no orchestration layer.

MARKET 2: Central Europe (Germany, Netherlands, Belgium, France - key tourist source markets)
  Currently offer: Visa/MC/Amex via Adyen
  Missing: iDEAL (Netherlands), Bancontact (Belgium), Cartes Bancaires (France), Giropay/EPS, SEPA
  European tourists visiting Nordic attractions and hotels need their local payment methods.

MARKET 3: United Kingdom (major inbound tourism to Nordics)
  Currently offer: Visa/MC via Adyen
  Missing: Open Banking, PayPal, Clearpay/Afterpay
  UK is a top source market for Nordic tourism. British tourists booking hotels and experiences need familiar checkout.

MARKET 4: Asia-Pacific (Chinese, Indian, Southeast Asian tourists)
  Currently offer: Visa/MC only
  Missing: Alipay (1.3B+ users), WeChat Pay (900M+ users), UPI (500M+ users), GrabPay, LINE Pay
  Chinese tourists are a fast-growing segment in Nordic tourism (Northern Lights, Icehotel). Zero Asian APM support.

MARKET 5: Americas (US, Brazil, Latin America tourists)
  Currently offer: Visa/MC/Amex
  Missing: Pix (Brazil, 150M+ users), Venmo, PayPal, Mercado Pago, OXXO
  US and Brazilian tourists visiting Nordic destinations. No LATAM payment methods for growing tourist segment.

**Payment Pain Points:**
1. Multi-PSP fragmentation (Adyen, Nets, Swedbank Pay, Klarna, Softpay) with no orchestration
2. Nordic-centric payment stack limits international tourist conversion
3. No smart routing across PSPs to optimize auth rates
4. Complex package payments (hotel + ticket + activity) settled across different PSPs
5. No Alipay/WeChat Pay for Chinese tourists visiting Nordic attractions
6. No UPI for Indian visitors to Nordic destinations
7. Static PSP assignments rather than dynamic transaction routing
8. Softpay adds POS flexibility but only supports card schemes, not Asian/LATAM wallets
9. Global expansion under new CEO requires payment infrastructure beyond Nordic PSPs
10. 15,000+ distribution partners need consistent checkout regardless of source channel

**Key Meeting Angles:**
1. **2,200+ customers, no orchestration**: Adyen, Nets, Swedbank Pay, and Klarna operate independently across iTicket, Citybreak, and BookVisit. Yuno unifies all PSPs under one routing layer
2. **Global expansion imperative**: New CEO Richard Wiegmann (Amadeus, Sabre, Expedia background) is driving international growth. Payment infrastructure must scale beyond Nordic PSPs. Yuno provides 1,000+ APMs via single API
3. **International tourism gap**: Nordic attractions (Liseberg, Icehotel, Northern Lights tours) attract Chinese, Indian, and European tourists who cannot pay with Alipay, WeChat Pay, UPI, or iDEAL. Revenue leakage on high-value bookings
4. **Package complexity**: Hotels + tickets + activities + transport in one checkout across multiple PSPs. Yuno provides unified reconciliation and settlement
5. **PSG-backed growth**: 100M+ EUR investment demands operational efficiency. Yuno reduces payment ops complexity. InDrive achieved 90% approval across 10 markets with Yuno
6. **Smart routing on multi-PSP stack**: Adyen, Nets, and Swedbank Pay already in place. Yuno routes each transaction to the optimal acquirer. McDonald's gained +4.7% auth rate with Yuno

**Sources:**
- [Visit Group](https://www.visitgroup.com/)
- [Visit Group Ecosystem](https://www.visitgroup.com/explore-the-visit-group-ecosystem)
- [iTicket](https://iticket.com/)
- [Visit Group + Softpay Partnership](https://www.visitgroup.com/visit-group-and-softpay-partner-digitize-payments-travel-and-hospitality-industry)
- [Richard Wiegmann CEO Appointment](https://www.visitgroup.com/richard-wiegmann-joins-visit-group-ceo-drive-next-phase-growth)
- [Visit Group Connects Hotels + Attractions](https://www.visitgroup.com/visit-connects-stays-and-attractions-one-booking-flow)
- [PSG Equity Investment (BusinessWire)](https://www.businesswire.com/news/home/20240122579024/en/)
- [PhocusWire: Visit Group PSG Investment](https://www.phocuswire.com/Visit-Group-PSG-Equity-travel-software-investment)
- [Visit Group GODO Acquisition](https://airguide.info/visit-group-acquires-godo-to-expand-in-nordic-market/)
- [Brandfetch: Visit Group](https://brandfetch.com/visitgroup.com)
- [Tracxn: Visit Group](https://tracxn.com/d/companies/visit-group/)
- [CB Insights: Visit Group](https://www.cbinsights.com/company/visit-group)
- [Citybreak Release Notes Nov 2024](https://www.visitgroup.com/citybreak-release-notes-26-november-2024)
- [BookVisit](https://bookvisit.com/about-us/)
