# SUPER.COM | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Super.com
=======================================

Logo: https://logo.clearbit.com/super.com
Nombre merchant: Super.com

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Fragmented Card Issuing
Tittle_Pain Point_2: USD Only Limitation
Tittle_Pain Point_3: Travel Checkout Gaps
Tittle_Pain Point_4: Auth Rate Blind Spots
Tittle_Pain Point_5: Chargeback Exposure

Desc_Pain Point_1: Super.com runs Qolo for card acquiring and issuing, MRV Banks as card issuer for SuperCash Mastercard, Republic Bank for the Charge Card, ACH via Qolo, and separate integrations for PayPal, Venmo, and CashApp funding. Multiple banking partners with no unified routing layer across acquiring and card programs.
Desc_Pain Point_2: All Super+ membership fees and card transactions are charged in USD. With 30M+ users globally and travel bookings across 100+ countries, every non-US transaction carries FX friction. On $1B+ annual travel GMV, cross-border conversion costs compress already thin OTA margins.
Desc_Pain Point_3: Super.com travel checkout supports cards and limited digital wallets (PayPal, Venmo, CashApp for funding). No local payment methods for hotel bookings in Europe (iDEAL, Bancontact), LATAM (Pix, PSE, OXXO), or Asia (Alipay, WeChat Pay, GrabPay). Limits international booking conversion.
Desc_Pain Point_4: With $1B+ travel GMV flowing through a single processor (Qolo), Super.com has no ability to route transactions across multiple acquirers per card BIN and issuer. No failover path exists when Qolo declines. On a platform where 60-70% of users pay with debit, every decline is a lost booking.
Desc_Pain Point_5: BBB complaints surged in 2025 over unauthorized Super+ charges. Users report involuntary enrollment and difficulty canceling, leading to chargebacks. High dispute rates increase processing costs and risk merchant account penalties. Over 4,600 complaints logged on PissedConsumer alone.

SLIDE 1: PSP TOPOLOGY

PSP_1: Qolo (card acquiring + issuing platform)
PSP_2: MRV Banks (SuperCash Mastercard issuer)
PSP_3: Republic Bank & Trust (Charge Card issuer)
PSP_4: Mastercard (card network)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: iDEAL
Local_M_2: Bancontact
Local_M_3: Pix
Local_M_4: PSE
Local_M_5: OXXO
Local_M_6: Alipay
Local_M_7: WeChat Pay
Local_M_8: GrabPay
Local_M_9: Klarna
Local_M_10: UPI

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Recovery
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across acquiring partners for every travel booking and card charge. Each transaction routed to the highest performing acquirer for that card BIN, issuer, and merchant category. On $1B+ annual travel GMV with 60-70% debit card users, smart routing delivers +3 to 10% auth uplift. InDrive achieved 90% approval across 10 markets with Yuno. For a debit-heavy user base, every recovered decline converts directly to revenue.
Desc_Yuno_Cap2: Automatic cascade across acquirers eliminates single-processor dependency on Qolo. When one processor declines, Yuno reroutes in milliseconds. Up to 50% recovery on soft declines via instant retry. NOVA AI recovers up to 75% of failed transactions. A declined hotel booking at checkout means a lost customer and a lost Super+ membership conversion.
Desc_Yuno_Cap3: Activates the local APMs Super.com lacks for global travel: iDEAL in Netherlands, Bancontact in Belgium, Pix in Brazil, PSE in Colombia, OXXO in Mexico, Alipay and WeChat Pay for Chinese travelers, GrabPay in Southeast Asia, Klarna for BNPL on high-value trips, UPI in India. One API, 1,000+ payment methods across every travel market. Wingo expanded to 10 LATAM APMs with Yuno.
Desc_Yuno_Cap4: One dashboard replacing Super.com's fragmented Qolo + MRV Banks + Republic Bank + PayPal/Venmo/CashApp stack. Real-time approval rate monitoring across all travel bookings, card transactions, and fund inflows. Centralized reconciliation for card issuing, travel purchases, and membership billing. Single view of $1B+ in travel GMV. Rappi unified its multi-country payment operations with Yuno orchestration.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Super.com at a glance:**
- Model: Travel booking (OTA) + fintech super app + membership (Super+) + card issuing + cash advances + credit building
- Revenue: ~$200M annualized (July 2025, Sacra estimate)
- Travel GMV: $1B+ annual (surpassed in 2024)
- Total Sales Processed: $2B+ since launch
- Users: 30M+ worldwide; 5M+ SuperCash card users
- Employees: ~225 (2025)
- Total Funding: ~$152M across Seed ($1.2M, 2016), Series A ($8M, 2017), Series B ($85M, 2021), Series C ($85M, 2023)
- Valuation: Not disclosed (private); last round led by iNovia Capital and Lion Capital
- Founded: April 2016 (as SnapTravel), rebranded to Super.com October 2022
- HQ: San Francisco, CA + Toronto, Canada
- CEO & Co-Founder: Hussein Fazal (prev. AdParlor, bootstrapped to $100M rev, acquired by AdKnowledge)
- CTO & COO: Henry Shi (Co-Founder)
- CFO: Daniel Weisenfeld
- GM, Payments & Fintech Innovation: Rick Galasieski (leads payment strategy, card programs, Qolo integration)
- VP, Engineering: Ryan Fox (prev. Google SWE/SRE)
- Notable Investors: Steph Curry, Harley Finkelstein (Shopify President), Neha Narkhede, iNovia Capital, Titanium Ventures, Acrew Capital, Lightbank, Lion Capital

**Revenue Model:**
- Travel booking commissions (OTA model, wholesale/agent hotel pricing)
- Super+ membership: $15/month subscription fee
- Card interchange: SuperCash Mastercard and Charge Card
- Cash advance fees ($20 to $250 range)
- Credit building service fees
- Partner offers and in-app earnings marketplace (games, surveys, videos)
- 62% of US hotel bookings come from Super+ members

**Payments Infrastructure:**
- Qolo: Primary omnichannel payments platform handling card acquiring, ACH fund inflows, and card issuing
- Co-operative Authorization: Qolo receives network transactions and manages top-level auth logic; Super.com retains control over card-level, MCC, merchant, and transaction type decisions
- MRV Banks: Issuer for SuperCash Secured Mastercard (Member FDIC)
- Republic Bank & Trust Company: Issuer for Super.com Charge Card (Mastercard network)
- Mastercard: Card network for all Super.com card products
- PayPal, Venmo, CashApp: Accepted for funding Super deposit accounts
- ACH transfers: Accepted for account funding
- Debit card: Accepted for "Just in Time" funding
- Triple-digit YoY growth in Qolo processing volume
- No payment orchestrator detected
- No multi-acquirer routing or failover capability detected

**Payment Methods Currently Supported:**
- SuperCash Secured Mastercard (issued by MRV Banks)
- Super.com Charge Card (issued by Republic Bank)
- Debit card for funding
- ACH transfer
- PayPal
- Venmo
- CashApp
- No Apple Pay, Google Pay, or Samsung Pay detected at checkout
- No BNPL options
- No local payment methods (iDEAL, Pix, Alipay, etc.)

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (primary market, 183M target users with low-to-mid FICO)
  Currently offer: SuperCash Mastercard, Charge Card, PayPal, Venmo, CashApp, ACH, debit
  Missing: Apple Pay, Google Pay, Affirm/Klarna (BNPL for high-value travel), Zelle
  60-70% of travel customers pay with debit. Mobile wallets at checkout would boost conversion.

MARKET 2: Canada (Toronto office, founders are Canadian)
  Currently offer: Card payments via Qolo, standard digital wallets for funding
  Missing: Interac e-Transfer, Interac Debit, Apple Pay/Google Pay at checkout
  Interac is the dominant payment rail in Canada. Missing it means friction for Canadian travelers.

MARKET 3: Europe (travel bookings for international hotels)
  Currently offer: Card payments (Mastercard network)
  Missing: iDEAL, Bancontact, SEPA Instant, Klarna, Trustly, Sofort
  European travelers booking via Super.com face USD conversion and no local payment options.

MARKET 4: Latin America (growing travel market, Yuno's home territory)
  Currently offer: Card payments only
  Missing: Pix, PSE, OXXO, Mercado Pago, Nequi, SPEI
  LATAM is mobile-first and debit-heavy, matching Super.com's user profile. Massive untapped demand.

MARKET 5: Asia-Pacific (hotel supply, growing traveler base)
  Currently offer: Card payments only
  Missing: Alipay, WeChat Pay, GrabPay, UPI, LINE Pay, Toss Pay, PayNow
  Chinese and Indian travelers are the fastest growing segments. Without local wallets, bookings are lost.

**Payment Pain Points (Extended):**
1. Single processor dependency (Qolo) for all card acquiring with no redundancy or failover
2. All pricing and billing in USD only, creating FX friction for international users
3. No local payment methods for travel bookings outside the US
4. 60-70% debit card user base amplifies decline impact (no credit line buffer)
5. No Apple Pay or Google Pay at checkout despite mobile-first app model
6. Chargeback spike from involuntary Super+ enrollment (BBB complaints surging since May 2025)
7. No smart routing between acquirers; every decline is terminal with no retry path
8. Card issuing split between two banks (MRV Banks + Republic Bank) with no unified view
9. Customer service and cancellation difficulties increase dispute rates
10. Hotel partners sometimes do not honor Super.com bookings, causing downstream chargebacks

**Competitive Landscape:**
- Direct competitors: Hopper, Priceline, Booking.com, Hotels.com, Expedia
- Fintech competitors: Cash App, Chime ($1.7B revenue), Dave ($347M revenue), Klarna, Rocket Money
- Cashback competitors: Rakuten ($15B revenue), Swagbucks, Mistplay
- Credit building competitors: Chime Credit Builder, Self Financial, Grow Credit
- Key differentiator: Super.com bundles travel, cashback, credit building, and cash advances in one membership

**Key Meeting Angles:**
1. **$1B+ Travel GMV, single-processor risk**: All travel bookings flow through Qolo with no failover. Yuno's multi-acquirer orchestration ensures zero booking failures. InDrive achieved 90% approval rates across 10 markets with Yuno
2. **Debit-heavy user base = decline-sensitive**: 60-70% of users pay with debit cards. Smart routing optimizes each transaction per BIN and issuer. On this volume, +3 to 10% auth uplift translates to millions in recovered bookings
3. **Rick Galasieski is the payments decision-maker**: GM of Payments & Fintech Innovation directly owns Qolo relationship and card programs. He speaks at fintech conferences about card infrastructure. He is the ideal contact for an orchestration conversation
4. **International travel, USD only**: Super.com books hotels globally but processes everything in USD. Yuno's local acquiring and 1,000+ APMs unlock local currency processing in every travel market. Wingo expanded to 10 LATAM payment methods with Yuno
5. **Chargeback crisis from Super+ enrollment**: BBB and PissedConsumer complaints are escalating. High dispute rates threaten merchant account health. Yuno's fraud prevention and Monitors provide real-time anomaly detection to flag subscription billing issues before they become chargebacks
6. **Mobile-first app with no mobile wallets**: Super.com is a mobile app serving 30M+ users but does not support Apple Pay or Google Pay at checkout. Yuno enables all major mobile wallet integrations through a single API
7. **Post-Series C growth pressure**: $152M raised with $200M revenue target. Expanding payment methods and improving auth rates are the highest-leverage growth levers for a travel OTA
8. **LATAM and APAC hotel supply untapped**: Pix alone processes 150M+ daily transactions in Brazil. Without local methods, Super.com cannot convert price-sensitive travelers in the world's fastest growing travel markets

**Sources:**
- [Wikipedia: Super.com](https://en.wikipedia.org/wiki/Super.com)
- [Sacra: Super.com Revenue and Valuation](https://sacra.com/c/super/)
- [Sacra: Hussein Fazal Interview](https://sacra.com/research/hussein-fazal-super-paycheck-for-paycheck-super-app/)
- [Qolo Case Study: How Super.com is Changing the Payments Game](https://qolo.io/case-studies/how-super-com-is-changing-the-payments-game/)
- [NerdWallet: Super.com Card Review](https://www.nerdwallet.com/credit-cards/reviews/super-card)
- [CreditCards.com: SuperCash Secured Mastercard Review](https://www.creditcards.com/reviews/supercash-mastercard-review/)
- [BetaKit: How Super Raised $85M After Rebranding](https://betakit.com/how-super-raised-85-million-usd-after-rebranding-from-snapcommerce/)
- [Super.com Press: Snapcommerce Raises $85M](https://landing.super.com/press/snapcommerce-message-driven-mobile-commerce-platform-raises-85m-usd-in-funding-led-by-inovia-capital-and-lion-capital)
- [Super.com Press: Launches Debit-Credit Hybrid Card](https://www.super.com/press/super-launches-debit-credit-hybrid-card-with-2-back)
- [Super.com Press: Rebranding from Snapcommerce](https://landing.super.com/press/snapcommerce-grabs-its-cape-and-becomes-super)
- [Super.com: About Page](https://landing.super.com/about)
- [Super.com: Legal Terms](https://www.super.com/legal)
- [The Org: Super.com Leadership](https://theorg.com/org/super-com)
- [Crunchbase: Super.com](https://www.crunchbase.com/organization/superdotcom)
- [BBB: Super.com Complaints](https://www.bbb.org/us/ca/san-francisco/profile/mobile-apps/supercom-1116-881071/complaints)
- [PissedConsumer: Super.com Reviews](https://super-com.pissedconsumer.com/review.html)
- [Trustpilot: Super.com Reviews](https://www.trustpilot.com/review/super.com)
- [Bright Money: Super.com/MRV Banks](https://www.brightmoney.co/card/super-com-mrv-banks)
- [Inovia Capital: Super.com](https://www.inovia.vc/active-companies/super/)
- [TechCrunch: Snapcommerce Becomes Super](https://techcrunch.com/2022/10/18/snapcommerce-grabs-its-cape-and-becomes-super/)
- [BadCredit.org: Super.com Products](https://www.badcredit.org/news/super-com-empowers-consumers-to-save-money-and-build-credit/)
- [Qwoted: Rick Galasieski Profile](https://app.qwoted.com/sources/rick-galasieski)
- [US Fintech Symposium: Rick Galasieski Speaker](https://www.fintechsymposium.com/news/new-speaker-announcement-rick-galasieski-from-supercom)
- [EquityZen: Invest in Super.com](https://equityzen.com/company/superdotcom/)
