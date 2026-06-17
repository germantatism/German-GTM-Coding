# PEEK | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Peek
=======================================

Logo: https://cdn.brandfetch.io/id3TlSdZ8z/w/512/h/512/theme/dark/icon.jpeg
Nombre merchant: Peek

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Multi-PSP Fragmentation
Tittle_Pain Point_2: Operator Payout Delays
Tittle_Pain Point_3: Limited Consumer APMs
Tittle_Pain Point_4: Global Scale Complexity
Tittle_Pain Point_5: Chargeback Exposure

Desc_Pain Point_1: Peek integrates with Stripe, Worldpay, Braintree, PayPal, and Klarna across its operator network but lacks a unified orchestration layer. Each operator may run a different processor, creating inconsistent checkout experiences and fragmented approval rate data across $1.5B+ in annual bookings.
Desc_Pain Point_2: Peek processes daily payouts to 4,000+ operators across 195 countries via Tipalti. Before automation, payout processing consumed 6 hours daily. Operators report delayed payments taking up to 15 days to resolve, with chargeback disputes going unanswered. 20% of support volume was payments-related.
Desc_Pain Point_3: Consumer checkout on Peek.com supports only credit/debit cards, Apple Pay, Google Pay, and Stripe Link. No PayPal at consumer level, no BNPL for high-value experiences, no local wallets for international tourists booking activities in the US or Europe. 150M+ consumers reached with limited payment options.
Desc_Pain Point_4: With $7B+ cumulative bookings across museums, theme parks, tours, and cultural attractions in multiple countries, Peek processes payments for vastly different operator types. 40% of operators still lack online booking tools, meaning payment infrastructure must be simple enough for non-technical merchants.
Desc_Pain Point_5: Peek's terms allow indefinite payout delays and modified payout plans for operators with excessive chargebacks. The dispute team is criticized for ignoring emails and failing to respond to chargeback evidence. Without smart fraud detection and routing, operators bear the chargeback burden.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (primary consumer processing)
PSP_2: Worldpay (operator option)
PSP_3: Braintree (operator option)
PSP_4: PayPal (operator option)
PSP_5: Tipalti (operator payouts)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Alipay
Local_M_2: WeChat Pay
Local_M_3: Klarna (consumer)
Local_M_4: iDEAL
Local_M_5: Bancontact
Local_M_6: Cartes Bancaires
Local_M_7: Pix
Local_M_8: GrabPay
Local_M_9: Toss Pay
Local_M_10: UPI

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Recovery
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across Stripe, Worldpay, Braintree, and PayPal for every experience booking. Each transaction routed to the highest performing acquirer for that card BIN, issuer, and market. On $1.5B+ annual bookings across museums, theme parks, tours, and attractions, smart routing delivers +3 to 10% auth uplift, recovering millions in failed bookings per year.
Desc_Yuno_Cap2: Automatic cascade across Peek's multiple PSPs eliminates single-processor dependency. When Stripe declines, Yuno reroutes to Worldpay or Braintree in milliseconds. Up to 50% recovery on soft declines via instant retry. NOVA AI recovers up to 75% of failed transactions. For time-sensitive experience bookings (tours departing in hours), a failed payment means an empty seat.
Desc_Yuno_Cap3: Activates the APMs Peek needs for international tourists: Alipay and WeChat Pay for Chinese tourists (180M+ outbound travelers), Klarna for BNPL on premium experiences, iDEAL for Dutch visitors, Cartes Bancaires for French tourists, Pix for Brazilian guests, GrabPay for Southeast Asian travelers, UPI for Indian visitors. One API, 1,000+ payment methods.
Desc_Yuno_Cap4: One dashboard replacing Peek's fragmented Stripe + Worldpay + Braintree + PayPal + Tipalti stack. Real-time approval rate monitoring across all 4,000+ operators and 150M+ consumers, centralized reconciliation for bookings, refunds, and operator payouts, and millisecond anomaly detection via Monitors. Reduces the 20% support volume driven by payment inquiries.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Peek at a glance:**
- Model: Experiences marketplace (Peek.com) + SaaS booking software (Peek Pro) + ticketing (ACME, Connect&GO)
- Annual Bookings: $1.5B+
- Cumulative Bookings: $7B+
- Consumer Reach: 150M+ across museums, theme parks, tours, activities, cultural attractions
- Operators: 4,000+ active partners receiving payouts
- 30,000+ monthly invoices processed
- Payouts across 195 countries
- TAM: $330B experiences industry
- Total funding: $193.5M+ (including $70M Series D, November 2025)
- Key investors: WestCap, Goldman Sachs Alternatives, Eric Schmidt, Paul English (Kayak founder), Jack Dorsey, Springcoast Partners
- Founded: 2012, San Francisco. CEO: Ruzwana Bashir (Co-founder)
- CTO: Oskar Bruening (Co-founder)
- CRO: Josiah Filler
- Awards: Arival 2024 Industry Innovation Award (Peek Copilot)

**Recent Acquisitions (November 2025):**
- ACME Ticketing: ticketing infrastructure, memberships, donations for cultural institutions
- Connect&GO: attraction management platform, RFID technology, visitor tools
- Combined reach: 150M+ consumers

**AI & Product:**
- Peek Copilot: AI platform delivering 5-20% revenue growth via Dynamic Pricing
- Hundreds of AI Agents working 24/7 on fraud detection, data analysis, operations
- 40% of operators still lack online booking tools (massive digitization opportunity)

**Notable Customers:**
- MoMA, Whitney Museum, Seattle Aquarium, Bryant Park, Looping Group, Museum of Ice Cream

**Payments Infrastructure:**
- Stripe: primary consumer-facing payment processor on Peek.com
- Stripe Link: digital wallet checkout on Peek.com
- Worldpay: available as operator payment processor option
- Braintree: available as operator payment processor option
- PayPal: available as operator payment processor option
- Klarna: available as operator integration
- Tipalti: operator payout platform (daily payouts to 4,000+ partners across 195 countries)
- No unified payment orchestration across PSPs

**Payment Methods (Consumer on Peek.com):**
- Credit and debit cards: Visa, Mastercard, Amex, Discover
- Apple Pay
- Google Pay
- Stripe Link (digital wallet)
- Payment methods vary by operator, device, and region

**Operator Payment Processing:**
- Booking fees: 6% to 8% per online booking (variable)
- Merchant service fees: 2.3% + $0.30 per ticket
- No monthly subscription fee
- Daily payout frequency to operators
- Before Tipalti: payout processing took 6 hours daily
- After Tipalti: reduced to 30 minutes daily
- 110 hours/week saved across 4-person finance team
- 20% of support volume was payment-related inquiries

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (primary market, majority of bookings)
  Currently offer: Visa/MC/Amex/Discover, Apple Pay, Google Pay, Stripe Link
  Missing: PayPal (consumer level), Klarna (consumer BNPL), Affirm, Afterpay, Venmo
  No BNPL for premium experiences ($100-500+ per person). BNPL increases average booking value 20-40%.

MARKET 2: United Kingdom / Europe (international market)
  Currently offer: Visa/MC, Apple Pay, Google Pay
  Missing: iDEAL, Bancontact, Cartes Bancaires, Klarna, Open Banking, SEPA
  European tourists booking US experiences need local payment methods. EU attractions need local APMs.

MARKET 3: Inbound Chinese Tourists (180M+ outbound travelers globally)
  Currently offer: Visa/MC only
  Missing: Alipay (1.3B+ users), WeChat Pay (900M+ users), UnionPay
  Chinese tourists spend $250B+ annually abroad. Alipay and WeChat Pay are essential for this segment.

MARKET 4: Inbound Indian Tourists (fastest growing outbound market)
  Currently offer: Visa/MC only
  Missing: UPI (500M+ users), RuPay, Paytm
  Indian outbound tourism growing 20%+ YoY. UPI is the default payment method for India's digital population.

MARKET 5: Latin America (growing tourism markets)
  Currently offer: Visa/MC only
  Missing: Pix (Brazil, 150M+ users), PSE (Colombia), Mercado Pago, OXXO (Mexico)
  LATAM outbound tourism rebounding strongly post-pandemic. Brazilian tourists are the #1 LATAM outbound segment.

**Payment Pain Points:**
1. Multi-PSP fragmentation (Stripe, Worldpay, Braintree, PayPal) with no orchestration
2. Operator payout delays: up to 15 days reported, with dispute team unresponsive
3. No BNPL at consumer level for premium experiences
4. No local payment methods for international tourists (Chinese, Indian, Brazilian)
5. Chargeback exposure: operators face indefinite payout delays for excessive chargebacks
6. Booking fee opacity: operators cannot predict fee percentages accurately
7. 20% of support volume driven by payment-related questions
8. 40% of operators lack online booking tools, payment UX must be simple
9. No smart routing across PSPs to optimize auth rates
10. Variable payment method availability by operator, device, and region

**Key Meeting Angles:**
1. **$1.5B+ annual bookings, no orchestration**: Stripe, Worldpay, Braintree, and PayPal operate independently. Yuno unifies all PSPs under one routing layer with real-time optimization
2. **150M+ consumers, limited payment options**: Chinese tourists (Alipay), Indian visitors (UPI), Brazilian guests (Pix) cannot pay with their preferred methods. Yuno's 1,000+ APMs via single API unlocks these segments
3. **$330B TAM, 40% not yet digital**: As Peek digitizes the experiences industry, payment infrastructure must scale. Yuno simplifies payment integration for non-technical operators
4. **Chargeback and fraud exposure**: NOVA AI provides intelligent fraud detection and dispute management, reducing the chargeback burden that causes operator payout delays
5. **Post-acquisition integration**: ACME and Connect&GO bring museums and theme parks. These venues serve international tourists who need Alipay, WeChat Pay, and European wallets. McDonald's gained +4.7% auth rate with Yuno
6. **Operator payout experience**: 4,000+ operators across 195 countries. Faster, more reliable payouts improve operator retention. InDrive achieved 90% approval across 10 markets with Yuno
7. **BNPL for premium experiences**: Museum passes, adventure tours, and multi-day experiences ($100-500+) are natural BNPL candidates. Klarna, Affirm, and Afterpay increase conversion and AOV
8. **CEO is WEF recognized**: Ruzwana Bashir is a World Economic Forum speaker. She understands global market dynamics and the importance of local payment methods

**Sources:**
- [Peek.com](https://www.peek.com/)
- [Peek Pro](https://www.peekpro.com/)
- [Peek Support: Payment Methods Accepted](https://support.peek.com/hc/en-us/articles/18556808085012-Payment-Methods-Accepted)
- [Tipalti: Peek Customer Story](https://tipalti.com/resources/customer-stories/peek/)
- [PRNewswire: Peek Acquires ACME and Connect&GO, Raises $70M](https://www.prnewswire.com/news-releases/peek-acquires-acme-ticketing-and-connectgo-raises-70m-to-double-down-on-ai-for-the-travel-and-experiences-industry-302621253.html)
- [TechCrunch: Peek Raises $80M at $2B Bookings](https://techcrunch.com/2021/11/23/peek-raises-80m-as-its-travel-experiences-software-and-marketplace-business-passes-2b-in-bookings/)
- [Skift: Peek Acquisitions](https://skift.com/2025/11/20/peek-acquisitions-experiences-growth/)
- [PYMNTS: Peek Raises $70M](https://www.pymnts.com/acquisitions/2025/peek-raises-70-million-for-experiences-industry-platform-and-acquires-2-companies/)
- [CB Insights: Peek Financials](https://www.cbinsights.com/company/peek-travel)
- [Crunchbase: Peek](https://www.crunchbase.com/organization/peek-com)
- [Capterra: Peek Pro Reviews](https://www.capterra.com/p/142459/Peek-PRO-Tour-Operator-Software/reviews/)
- [Bokun: Peek Pro Pricing Guide](https://www.bokun.io/peek-pro-pricing)
- [Wikipedia: Ruzwana Bashir](https://en.wikipedia.org/wiki/Ruzwana_Bashir)
- [Peek About](https://www.peek.com/about)
- [Peek Pro Terms of Service](https://www.peekpro.com/terms)
