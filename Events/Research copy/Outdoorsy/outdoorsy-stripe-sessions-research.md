# OUTDOORSY | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Outdoorsy
=======================================

Logo: https://cdn.brandfetch.io/id2kQcGeJx/w/512/h/512/theme/dark/icon.jpeg
Nombre merchant: Outdoorsy

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Single-PSP Dependency
Tittle_Pain Point_2: Host Payout Delays
Tittle_Pain Point_3: High-Value Auth Holds
Tittle_Pain Point_4: Limited Global APMs
Tittle_Pain Point_5: Cross-Border FX Costs

Desc_Pain Point_1: Outdoorsy runs its entire payment stack on Stripe for pay-ins, host payouts, security deposit holds, and insurance claims. With $3B+ cumulative transactions across 11 countries, a single Stripe outage blocks all bookings, payouts, and claims simultaneously. No failover or secondary processor exists.
Desc_Pain Point_2: Host payouts are released 48 hours after the trip starts and then take 3 to 5 additional business days for bank settlement. RV owners investing $50K to $200K+ in their vehicles need faster cash flow. Payout speed directly impacts host supply and fleet quality on the platform.
Desc_Pain Point_3: RV rentals average $150 to $300/day with security deposits of $500 to $2,500. These high-value authorization holds trigger frequent false declines, especially for international guests using foreign cards. Each declined booking is $1,000+ in lost transaction value for the marketplace.
Desc_Pain Point_4: Outdoorsy operates in 11 countries including US, Canada, UK, France, and Australia, with European expansion planned for Germany, Italy, Spain, Belgium, Austria, and Switzerland. Only credit cards, PayPal, Apple Pay, and Google Pay are supported. No local European wallets or bank transfers.
Desc_Pain Point_5: International guests booking RVs abroad pay in foreign currencies with cross-border FX markup. On a marketplace targeting $8B in cumulative transactions by 2029, FX inefficiency on cross-border bookings compounds into significant margin erosion.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (pay-ins)
PSP_2: Stripe (host payouts)
PSP_3: PayPal (Pay in 4 BNPL)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: iDEAL
Local_M_2: Bancontact
Local_M_3: Cartes Bancaires
Local_M_4: Klarna
Local_M_5: giropay
Local_M_6: SOFORT
Local_M_7: Afterpay
Local_M_8: Interac
Local_M_9: EPS
Local_M_10: Twint

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Recovery
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across Stripe and additional acquirers for high-value RV bookings. Each rental payment routed to the highest performing acquirer for that card BIN, issuer, and market. On $150 to $300/day average bookings with $500 to $2,500 security deposits across 11 countries, smart routing delivers +3 to 10% auth uplift, recovering hundreds of thousands in declined high-value bookings.
Desc_Yuno_Cap2: Automatic cascade eliminates Outdoorsy's single-point-of-failure on Stripe. When Stripe declines a high-value security deposit hold, Yuno reroutes to a secondary acquirer in milliseconds. Up to 50% recovery on soft declines via instant retry. NOVA AI recovers up to 75% of failed transactions. Critical for a marketplace where each failed booking represents $1,000+ in lost GMV.
Desc_Yuno_Cap3: Activates the APMs Outdoorsy needs for European expansion: iDEAL in Netherlands, Bancontact in Belgium, Cartes Bancaires in France, Klarna for BNPL across Europe, giropay and SOFORT in Germany, Afterpay in Australia, Interac in Canada, EPS in Austria, Twint in Switzerland. One API, 1,000+ payment methods, no per-market integration.
Desc_Yuno_Cap4: One dashboard unifying Outdoorsy's Stripe pay-ins, host payouts, PayPal BNPL, and Roamly insurance claims across 11 countries. Real-time approval rate monitoring for high-value RV bookings, centralized reconciliation of security deposits and host settlements, and millisecond anomaly detection via Monitors. Single view of the entire outdoor travel payment ecosystem.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Outdoorsy at a glance:**
- Model: Peer-to-peer RV rental marketplace + insurance (Roamly) + destinations network
- All-time Transactions: $3B+ (as of September 2024)
- Target: $8B in cumulative transactions by 2029
- Company Revenue: ~$28M to $34M (platform fees, varies by source)
- Achieved profitability: 2023
- Operates in: 11 countries, 4,800+ cities
- 7M+ guest nights booked since launch
- 95% of US professional RV rental hosts use Wheelbase (Outdoorsy's fleet management software)
- Target Market: 92M outdoor-loving American households
- Total funding: $195M to $295M (varies by source)
- Employees: ~256
- Founded: 2015, Austin, TX. CEO: Jeff Cavins (Co-founder)
- Co-founder & CMO: Jennifer Young
- CTO: Arpan Nanavati (ex-Walmart Labs, ex-PayPal, ex-Zynga)
- CFO: Marc Zimmermann
- Inc. 5000 list company

**Business Units:**
- Outdoorsy.com: RV rental marketplace (P2P)
- Roamly: Digital insurance and travel protection (Lloyd's Coverholder)
- Outdoorsy Destination Network: Campgrounds and glamping properties

**International Presence:**
- US (primary market, ~80%+ of transactions)
- Canada
- United Kingdom
- France
- Australia
- Additional countries through marketplace (11 total)
- Planned European expansion: Germany, Italy, Spain, Belgium, Austria, Switzerland
- Directors appointed for each European market

**Payments Infrastructure:**
- Stripe: primary PSP for all payment processing (pay-ins, payouts, security deposits)
- PayPal: accepted as alternative payment method
- PayPal Pay in 4: BNPL option for bookings up to $1,500
- PayPal Pay Monthly: 6 or 12 interest-free monthly payments
- Apple Pay: accepted
- Google Pay: accepted
- Host payouts via Stripe to bank accounts (ACH in US)
- Security deposits collected 2 days before trip via card authorization hold
- No payment orchestrator detected
- No secondary PSP for failover

**Payment Methods Currently Supported:**
- Credit cards: Visa, Mastercard, Amex, Discover
- Debit cards: accepted
- Apple Pay
- Google Pay
- PayPal (standard, Pay in 4, Pay Monthly)
- 50% split payment option (credit card only)

**Fee Structure:**
- Host service fee: 20% to 25% of booking subtotal (new hosts start at 25%)
- Guest service fee: included in booking price
- Security deposit: set by host ($500 to $2,500 typical for RVs)
- Security Deposit Waiver: optional, covers up to $1,500 deductible

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (primary market, ~80%+ of transactions)
  Currently offer: Visa/MC/Amex/Discover, Apple Pay, Google Pay, PayPal, PayPal Pay in 4/Monthly
  Missing: Klarna, Affirm, Afterpay, Venmo, Cash App Pay
  Additional BNPL options would increase conversion for high-value RV bookings ($150-300/day).

MARKET 2: United Kingdom (established market)
  Currently offer: Visa/MC, Apple Pay, Google Pay, PayPal
  Missing: Open Banking (Faster Payments), Klarna, Clearpay (Afterpay UK)
  UK Open Banking growing 60%+ YoY. Klarna widely adopted for travel and leisure.

MARKET 3: France (established market, expansion priority)
  Currently offer: Visa/MC, Apple Pay, Google Pay, PayPal
  Missing: Cartes Bancaires (70%+ of French cards), Bancontact (Belgian travelers), Alma (French BNPL)
  Not routing to Cartes Bancaires means higher interchange on French domestic card transactions.

MARKET 4: Canada (established market)
  Currently offer: Visa/MC, Apple Pay, Google Pay, PayPal
  Missing: Interac Online/Debit (70%+ Canadian debit), Afterpay, Sezzle
  Interac is the dominant Canadian debit network. Missing it limits debit card bookings.

MARKET 5: Australia (established market)
  Currently offer: Visa/MC, Apple Pay, Google Pay, PayPal
  Missing: Afterpay (12M+ AU users), eftpos, POLi, BPAY
  Afterpay was born in Australia. 30%+ of AU online shoppers use BNPL.

MARKET 6: Germany (planned expansion)
  Will need: Klarna (home market), giropay, SOFORT, SEPA instant, PayPal
  Germany is Europe's largest e-commerce market. Klarna + PayPal = 50%+ of German online payments.

MARKET 7: Switzerland (planned expansion)
  Will need: Twint (5M+ users in a 9M population), PostFinance, SEPA
  Twint dominates Swiss mobile payments with 55%+ penetration.

**Payment Pain Points:**
1. Single PSP (Stripe) with zero failover across 11 countries
2. High-value security deposits ($500-$2,500) trigger frequent false declines
3. Host payouts take 5-7+ business days from trip start
4. No local European payment methods despite active UK/France operations and EU expansion
5. No Interac in Canada (70%+ of Canadian debit)
6. No Afterpay in Australia (12M+ users in Afterpay's home market)
7. PayPal Pay in 4 capped at $1,500, insufficient for many RV bookings
8. Insurance claims payouts (Roamly) delayed per BBB complaints
9. Cross-border FX on international guest bookings
10. European expansion (6 new markets) will require massive APM buildout

**Key Meeting Angles:**
1. **$3B+ transactions, single PSP**: Stripe handles everything. No failover. Yuno adds multi-acquirer resilience without integration complexity
2. **High-value transactions are uniquely vulnerable**: $150-300/day rentals with $500-2,500 deposits. Smart routing to the best acquirer per BIN reduces false declines. InDrive achieved 90% approval across 10 markets with Yuno
3. **European expansion is the growth story**: 6 new markets (Germany, Italy, Spain, Belgium, Austria, Switzerland) each need local APMs. Yuno activates 1,000+ methods via single API. McDonald's gained +4.7% auth rate with Yuno
4. **CTO is ex-PayPal**: Arpan Nanavati spent time at PayPal. He understands payment infrastructure and the value of orchestration
5. **Roamly insurance creates payment complexity**: Claims payouts, premium collection, and rental payments all flowing through one PSP. Orchestration layer simplifies the multi-product payment stack
6. **Host retention depends on payout speed**: RV owners investing $50K-200K+ need fast, reliable payouts. Yuno can route to the fastest local rail per market
7. **BNPL expansion opportunity**: RV rentals ($1,000-5,000+ per booking) are perfect for installments. PayPal's $1,500 cap is too low. Klarna, Affirm, and Afterpay offer higher limits
8. **$8B transaction target by 2029**: Scaling from $3B to $8B across 15+ countries requires payment infrastructure that scales globally. Yuno was built for exactly this

**Sources:**
- [PRNewswire: Outdoorsy Group Exceeds $3B in Sales](https://www.prnewswire.com/news-releases/the-outdoorsy-group-exceeds-3-billion-in-sales-plans-european-expansion-302255696.html)
- [PRNewswire: Outdoorsy Closes $50M Funding Round](https://www.prnewswire.co.uk/news-releases/outdoorsy-closes-50m-funding-round-as-growth-soars-and-company-expands-in-major-global-markets-865244167.html)
- [PRNewswire: Outdoorsy Launches PayPal Pay in 4](https://www.prnewswire.com/news-releases/outdoorsy-launches-two-new-features-to-make-travel-easier-with-new-trip-cancellation-coverage-and-paypal-pay-in-4-offering-301551055.html)
- [Digital Transactions: Outdoorsy Picks PayPal's Pay in 4](https://www.digitaltransactions.net/outdoorsy-picks-paypals-pay-in-4-and-other-digital-transactions-news-briefs-from-5-20-22/)
- [Outdoorsy Blog: New Executives (CTO, Board)](https://www.outdoorsy.com/blog/outdoorsy-announces-new-executives)
- [Outdoorsy Blog: European Expansion Leadership](https://www.outdoorsy.com/blog/amid-rapid-european-expansion-outdoorsy-announces-additions-senior-leadership-team-executives-tesla-mercedes-benz-ebay-airbnb-google-expedia)
- [Outdoorsy Help: Fee Structure and Payouts](https://support.outdoorsy.com/hc/en-us/articles/37916164272283-What-is-your-fee-structure-And-how-do-I-get-paid)
- [Outdoorsy Help: Security Deposit](https://support.outdoorsy.com/hc/en-us/articles/37455537111835-What-is-the-security-deposit-How-does-it-work-for-my-listing)
- [Outdoorsy Terms of Service](https://www.outdoorsy.com/help/outdoorsy-terms-of-service)
- [BBB: Outdoorsy Complaints](https://www.bbb.org/us/tx/austin/profile/camper-rental/outdoorsy-inc-0825-1000146342/complaints)
- [CB Insights: Outdoorsy Financials](https://www.cbinsights.com/company/outdoorsy/financials)
- [GetLatka: Outdoorsy Revenue](https://getlatka.com/companies/outdoorsy.com)
- [Insurance Business: Outdoorsy Expansion Plan](https://www.insurancebusinessmag.com/us/news/travel/the-outdoorsy-group-reveals-expansion-plan-507073.aspx)
- [Outdoorsy Group: About](https://www.outdoorsy.com/about/outdoorsy-group)
- [Consumer Affairs: Outdoorsy Reviews](https://www.consumeraffairs.com/automotive/outdoorsy.html)
