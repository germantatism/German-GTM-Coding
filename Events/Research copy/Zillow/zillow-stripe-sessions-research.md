# ZILLOW | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Zillow
═══════════════════════════════════════

Logo: https://commons.wikimedia.org/wiki/Special:Redirect/file/Zillow_logo.svg
Nombre merchant: Zillow

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Card Fee Revenue Drain
Tittle_Pain Point_2: Single Processor Lock-In
Tittle_Pain Point_3: ACH-Only Free Payments
Tittle_Pain Point_4: Failed Payment Recovery
Tittle_Pain Point_5: First Payment Decline Spike

Desc_Pain Point_1: Renters paying by credit card face 2.95% fees; debit costs $9.95 flat. With $630M rentals revenue (+39% YoY) and growing payment volume, these fees suppress card adoption and push renters toward slower ACH, delaying landlord payouts.
Desc_Pain Point_2: Stripe is the sole payment processor for the entire Zillow Payments platform. All rent, deposit, and utility payments flow through one provider. Any Stripe disruption blocks rent collection for landlords and credit reporting for 140K+ renters.
Desc_Pain Point_3: ACH is the only free payment method. Free ACH takes 5 business days (7-10 for first payment). Landlords waiting nearly two weeks for initial deposits face cash flow gaps. No instant or same-day settlement option exists.
Desc_Pain Point_4: Failed rent payments are not auto-retried by the system. Renters must manually retry or add a new method. Each failed payment risks late rent, damages renter credit scores, and creates landlord-tenant friction on a platform managing millions of transactions.
Desc_Pain Point_5: First-time Zillow payments frequently declined because banks do not recognize the charge and block it as suspected fraud. This creates a poor onboarding experience for renters and delays initial landlord deposits by additional days.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe
PSP_2: Plaid (bank auth)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Real-Time Payments (RTP)
Local_M_2: FedNow
Local_M_3: Zelle
Local_M_4: Venmo
Local_M_5: Cash App Pay
Local_M_6: Apple Pay
Local_M_7: Google Pay
Local_M_8: Interac (Canada)
Local_M_9: Affirm/Klarna BNPL
Local_M_10: PayPal

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across Stripe and additional acquirers based on payment type, card BIN, and transaction amount. With $630M rentals revenue and 221M monthly users, routing rent payments to the highest-performing processor per transaction recovers millions in failed charges annually.
Desc_Yuno_Cap2: Automatic cascade eliminates Zillow's single-Stripe dependency. When Stripe declines a rent payment, Yuno reroutes to the next best acquirer in milliseconds instead of requiring manual renter retry. Protects credit reporting for 140K+ enrolled renters. Up to 50% recovery on failed transactions.
Desc_Yuno_Cap3: Activates payment methods renters already use: Venmo, Cash App, Apple Pay, Google Pay, PayPal. Real-time payment rails (RTP/FedNow) enable same-day rent deposits for landlords, eliminating the 5-10 day ACH delay. One API, 1,000+ methods. Faster deposits, better renter experience.
Desc_Yuno_Cap4: One dashboard unifying Stripe card/ACH processing, Plaid bank auth, and future payment rails across rent, deposits, utilities, and listing fees. Real-time monitoring for $2.6B total revenue across Rentals, For Sale, and Mortgages segments. NOVA intelligence provides 75% faster fraud detection on high-value rent transactions.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Zillow at a glance:**
- Revenue: $2.6B (FY2025), up 16% YoY; Q4 $654M (+18% YoY)
- Adjusted EBITDA: $622M (FY2025), 24% margin
- Rentals revenue: $630M (FY2025), up 39% YoY; Q1 2025 alone was $129M (+33%)
- Mortgages revenue: $199M (+37% YoY); purchase loan origination up 53%
- 221M average monthly unique users (Q4 2025); ~2.1B quarterly visits
- 63% share of US rental listings (up from 54% in 2024)
- CEO: Jeremy Wacksman (since August 2024); Co-Executive Chairs: Rich Barton, Lloyd Frink
- SVP Rentals: Jon Lim; CPO: Christopher Roberts
- Cash and investments: $1.3B
- Public: NASDAQ: Z / ZG. Market cap ~$18B+
- Network: Zillow, Trulia, StreetEasy, HotPads
- US-only focus (CEO confirmed "no plans to go international"); limited Canada listings
- 140K+ renters enrolled in credit reporting (CreditClimb launched Nov 2025)

**Confirmed PSPs:**
- Stripe: sole payment processor for Zillow Payments platform (confirmed via Stripe Express tax forms, help docs)
- Plaid: bank account verification/authentication for ACH setup
- No secondary processor, no payment orchestrator detected
- Stripe handles rent payments, deposits, utility payments, and listing fee charges

**Payment methods accepted:**
- ACH (free for tenants; 5 business day settlement, 7-10 for first payment)
- Credit cards: Visa, MC, Amex, Discover (2.95% fee to tenant)
- Debit cards: $9.95 flat fee for rent, $4.95 for other charges
- NOT accepted: prepaid cards, government debit cards, PayPal, Venmo, Cash App, Apple Pay, Google Pay

**Advertising/listing payments:**
- Credit/debit card only via third-party processor
- Premium listing upgrade: $39.99 flat fee

**Top 5 Markets Gap Analysis:**

MARKET 1: US Major Metros (primary market, 80%+ of activity)
  Accepted: ACH, Visa/MC/Amex/Discover (cards with fees)
  Missing: Venmo, Cash App, Zelle, Apple Pay, Google Pay, RTP/FedNow
  Renters aged 18-34 overwhelmingly use Venmo and Cash App. Not offering them for rent creates friction.

MARKET 2: US Multifamily Segment (62% revenue growth in Q3 2025)
  Accepted: ACH, cards
  Missing: Real-time payment rails, integrated BNPL for security deposits
  Property managers need instant settlement. 5-day ACH delays create cash flow gaps.

MARKET 3: US Mortgage Segment ($199M revenue, 53% origination growth)
  Accepted: ACH for mortgage-related payments
  Missing: Instant bank verification, real-time disbursement
  Faster payment processing accelerates closing timelines for Zillow Home Loans.

MARKET 4: Canada (limited listings in Vancouver, Calgary, Toronto)
  Accepted: Cards via Stripe
  Missing: Interac e-Transfer, PAD (pre-authorized debit)
  Interac is Canada's dominant P2P and rent payment method.

MARKET 5: US Landlord Payout Market
  Accepted: ACH deposits (3-5 business days, up to 10 for first)
  Missing: Instant payouts, same-day settlement, real-time notifications
  Competing platforms (Apartments.com, Avail) offer faster payout options.

**Key meeting angles:**
1. **$630M rentals revenue rocket** | Fastest-growing segment (+39% YoY) with payment volume scaling rapidly
2. **Single-Stripe risk at scale** | 221M monthly users, all payments through one processor
3. **Failed payment gap** | No auto-retry means every declined rent payment requires manual renter action
4. **First-payment fraud blocks** | Banks blocking initial Zillow charges creates terrible onboarding experience
5. **Card fee suppression** | 2.95% credit / $9.95 debit fees push users to slow ACH, hurting landlord cash flow
6. **Missing modern rails** | No Venmo, Cash App, Apple Pay, Google Pay for a platform serving millennial/Gen-Z renters
7. **Real-time settlement opportunity** | RTP/FedNow could replace 5-10 day ACH delays, differentiating Zillow vs. competitors
8. **Credit reporting dependency** | 140K+ renters building credit; failed payments directly harm their scores

**Sources:**
- [Zillow Q4/FY2025 Earnings](https://investors.zillowgroup.com/investors/news-and-events/news/news-details/2026/Zillow-Group-Reports-Fourth-Quarter-and-Full-Year-2025-Financial-Results/default.aspx)
- [HousingWire: Zillow 2025 Profit](https://www.housingwire.com/articles/zillow-revenue-profit-2025/)
- [Zillow Help: Payment Forms and Fees](https://zillow.zendesk.com/hc/en-us/articles/360000603628)
- [Zillow Help: Failed Payment Notice](https://zillow.zendesk.com/hc/en-us/articles/360000603828)
- [Zillow Help: Payment Declined](https://help.zillowrentalmanager.com/hc/en-us/articles/360000595847)
- [Zillow Help: Payment Set Up](https://zillow.zendesk.com/hc/en-us/articles/32876589716627)
- [Zillow Rental Manager: Collect Rent](https://www.zillow.com/rental-manager/collect-rent-online/)
- [Zillow Rental Manager: Online Payments FAQ](https://www.zillow.com/rental-manager/online-payments-faq/)
- [Stripe Support: 1099 for Zillow Rental Managers](https://support.stripe.com/express/questions/guide-to-1099-tax-forms-for-zillow-rental-managers)
- [Zillow Group Leaders](https://www.zillowgroup.com/about-us/our-leaders/)
- [Zillow Group: CreditClimb](https://www.zillowgroup.com/news/renters-deserve-credit-for-paying-rent-and-zillow-is-delivering/)
- [Zillow MediaRoom Logos](https://zillow.mediaroom.com/logos)
- [iPropertyManagement: Zillow Statistics](https://ipropertymanagement.com/research/zillow-statistics)
- [Zillow Wikipedia](https://en.wikipedia.org/wiki/Zillow)
