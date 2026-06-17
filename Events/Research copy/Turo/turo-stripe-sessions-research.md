# TURO | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Turo
=======================================

Logo: https://cdn.brandfetch.io/idmSMp4EBq/w/512/h/512/theme/dark/icon.jpeg
Nombre merchant: Turo

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Single-PSP Dependency
Tittle_Pain Point_2: Host Payout Delays
Tittle_Pain Point_3: Limited APM Coverage
Tittle_Pain Point_4: Cross-Border FX Drag
Tittle_Pain Point_5: Auth Rate Blind Spots

Desc_Pain Point_1: Turo consolidated its entire payment stack onto Stripe (pay-ins, payouts, and insurance claims) after previously running three separate providers. While consolidation reduced complexity, it created single-point-of-failure risk on $2.5B GBV across five countries with zero failover capability.
Desc_Pain Point_2: Host payouts take 3 business days to initiate after a trip ends plus 3 to 5 additional days for bank settlement. With 170,000+ active hosts earning $1.5B annually, payout speed directly impacts host retention and fleet supply. Faster payouts via local rails would be a competitive advantage over traditional rental companies.
Desc_Pain Point_3: Turo accepts only credit cards, debit cards, Apple Pay, and Google Pay. No PayPal, no BNPL, no local wallets. In the UK and France, missing key local methods (Open Banking, Bancontact, Cartes Bancaires) limits conversion among the 3.5M active guests booking across five countries.
Desc_Pain Point_4: Turo operates in US, Canada, UK, Australia, and France with expansion planned for Germany and Spain. Each cross-border booking (tourist renting abroad) incurs FX conversion costs. On $2.5B GBV, even 50bps of FX drag on international bookings erodes margins for a company that already saw gross margin fall to 46%.
Desc_Pain Point_5: With $958M revenue and $2.5B GBV flowing through a single PSP, Turo has no ability to A/B test acquirer performance by BIN, issuer, or market. Smart routing across multiple processors would surface auth rate uplift that a single-PSP setup cannot achieve.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (pay-ins)
PSP_2: Stripe Connect (payouts)
PSP_3: Stripe (insurance claims)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: PayPal
Local_M_2: Klarna
Local_M_3: Afterpay
Local_M_4: Cartes Bancaires
Local_M_5: Open Banking (UK)
Local_M_6: iDEAL
Local_M_7: Bancontact
Local_M_8: giropay
Local_M_9: SOFORT
Local_M_10: Interac (Canada)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Recovery
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across Stripe and additional acquirers. Each rental booking routed to the highest performing processor for that card BIN, issuer, and market. On $2.5B GBV across five countries, smart routing delivers +3 to 10% auth uplift, translating to tens of millions in recovered booking value per year. Eliminates the auth rate blind spot of running a single PSP.
Desc_Yuno_Cap2: Automatic cascade eliminates Turo's single-point-of-failure risk on Stripe. When Stripe declines, Yuno reroutes to a secondary acquirer in milliseconds. Up to 50% recovery on soft declines via instant retry. NOVA AI recovers up to 75% of failed transactions with intelligent retry logic. Critical for a marketplace where a failed payment means a lost trip.
Desc_Yuno_Cap3: Activates the APMs Turo still lacks: PayPal (400M+ accounts globally), Klarna and Afterpay for BNPL in US/UK/AU, Cartes Bancaires in France, Open Banking in UK, iDEAL for Netherlands expansion, giropay and SOFORT for Germany launch, Interac in Canada. One API, 1,000+ payment methods, no per-market integration.
Desc_Yuno_Cap4: One dashboard replacing Turo's Stripe-only view with multi-acquirer analytics across all five markets. Real-time approval rate monitoring by country, BIN, and card type, centralized reconciliation for guest pay-ins and host payouts, and millisecond anomaly detection via Monitors. Accelerates host payout visibility and reduces the 3 to 5 day settlement gap.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Turo at a glance:**
- Model: Peer-to-peer car sharing marketplace (commission-based)
- Revenue: ~$958M (2024, +9% YoY); on track for $1B (2025)
- Gross Booking Value: $2.5B (2024)
- Host Payouts: $1.5B annually to 170,000+ active hosts
- Active Guests: 3.5M across five countries
- Listed Vehicles: ~340,000 spanning 1,600 makes/models across 16,000+ cities
- Gross Margin: 46% (2024, down from 51% in 2023)
- EBITDA-positive for four consecutive years
- IPO withdrawn February 2025 after three years of S-1 preparation
- 15% workforce reduction (~150 employees) following IPO withdrawal
- Founded: 2010, San Francisco. CEO: Andre Haddad
- CTO: Avinash Gangadharan (ex-PayPal)
- CPO: Tom Wang
- CDO: Shwetank Kumar
- CLO: Michelle Fang

**Markets:**
- United States (primary market, ~80%+ of GBV)
- Canada (launched 2016-2017, Alberta, Ontario, Quebec)
- United Kingdom (launched 2016)
- Australia (launched 2022)
- France (active market)
- Planned expansion: Germany, Spain (2025-2026)

**Payments Infrastructure:**
- Consolidated from three separate providers to Stripe-only stack
- Stripe Payments: processes all guest pay-ins
- Stripe Connect: unified platform for host payouts across 170,000+ connected accounts
- Stripe handles insurance claims payouts as well
- Self-serve onboarding for hosts via Stripe Connect
- KYC/identity verification through Stripe
- No payment orchestrator detected
- No secondary PSP or failover capability

**Payment Methods Currently Supported:**
- Credit cards: Visa, Mastercard, Amex, Discover
- Debit cards: accepted with limitations
- Apple Pay: available across all markets
- Google Pay: US and Canada (mobile only)
- NOT accepted: PayPal, Venmo, Cash App, Bitcoin, checks, cash
- Off-platform payments strictly prohibited

**Host Payout Details:**
- US: Direct deposit via ACH (Stripe Connect)
- International: Bank transfer via Stripe Connect (118+ countries supported)
- Timeline: Payment initiated 3 business days after trip ends, then 3-5 business days for bank settlement
- Total delay: 6-8 business days from trip end to funds received

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (~80% of GBV, ~$2B)
  Currently offer: Visa/MC/Amex/Discover, Apple Pay, Google Pay
  Missing: PayPal (400M+ accounts), Klarna, Affirm, Afterpay, Venmo, Cash App Pay
  No BNPL for an average booking of $80-120/day. BNPL adoption in US travel hit 45% in 2024.

MARKET 2: United Kingdom (established market since 2016)
  Currently offer: Visa/MC, Apple Pay
  Missing: PayPal, Klarna, Open Banking (Faster Payments), Clearpay (Afterpay UK)
  Open Banking adoption in UK growing 60%+ YoY. PayPal is the #1 alternative payment method in UK.

MARKET 3: France (active market)
  Currently offer: Visa/MC, Apple Pay
  Missing: Cartes Bancaires (70%+ of French card payments), PayPal, Bancontact (Belgian travelers), Alma (French BNPL)
  Not routing to Cartes Bancaires means higher interchange on every French domestic card transaction.

MARKET 4: Canada (since 2016-2017)
  Currently offer: Visa/MC, Apple Pay, Google Pay
  Missing: Interac Online/Debit, PayPal, Afterpay (Clearpay), Sezzle
  Interac processes 70%+ of Canadian debit transactions. Missing Interac means debit card users face higher friction.

MARKET 5: Australia (launched 2022)
  Currently offer: Visa/MC, Apple Pay
  Missing: Afterpay (12M+ AU users, born in Australia), PayPal, POLi, BPAY, eftpos
  Afterpay has massive penetration in Australia. 30%+ of Australian online shoppers have used BNPL.

MARKET 6: Germany (planned expansion 2025-2026)
  Will need: Klarna (home market, 150M+ global users), giropay, SOFORT, PayPal, SEPA instant
  Germany is Europe's largest e-commerce market. Klarna and PayPal together account for 50%+ of German online payments.

MARKET 7: Spain (planned expansion 2025-2026)
  Will need: Bizum (30M+ users in Spain), PayPal, Klarna, Cofidis (BNPL)
  Bizum is Spain's dominant P2P and e-commerce wallet with 80%+ of banked population enrolled.

**Payment Pain Points:**
1. Single PSP (Stripe) with zero failover or cascade capability
2. Host payouts take 6-8 business days from trip end to funds received
3. No PayPal acceptance despite PayPal having 400M+ global accounts
4. No BNPL options despite car rental being a natural fit for installments
5. Google Pay limited to US and Canada mobile only
6. Payment failures trigger security protocols that lock user accounts
7. No Cartes Bancaires routing in France (higher interchange on local cards)
8. No local payment methods for UK, Australia, or Canada markets
9. No Interac support in Canada (70%+ of Canadian debit transactions)
10. Planned Germany and Spain expansion will require significant APM buildout

**Key Meeting Angles:**
1. **Single-PSP risk is real**: Turo consolidated from three providers to Stripe only. One Stripe outage blocks all bookings, host payouts, and insurance claims simultaneously. Yuno adds failover without adding integration complexity
2. **IPO withdrawal + margin pressure**: Gross margin fell from 51% to 46%. Every basis point of auth uplift and FX savings improves the P&L ahead of a potential re-IPO
3. **$2.5B GBV, no smart routing**: A single PSP cannot optimize auth rates by BIN, issuer, or market. InDrive achieved 90% approval across 10 markets with Yuno
4. **BNPL is a massive gap**: Car rentals ($80-120/day) are perfect for installments. Competitors (Hertz, Getaround) are adding BNPL. Yuno connects Klarna, Afterpay, Affirm via single API
5. **Host retention depends on payout speed**: 170,000 hosts earning $1.5B want faster payouts. Yuno's orchestration can route payouts through the fastest local rail per market
6. **Germany and Spain expansion needs local APMs**: Klarna in Germany, Bizum in Spain. Building per-market integrations is exactly the problem Yuno solves. McDonald's gained +4.7% auth rate with Yuno orchestration
7. **CTO is ex-PayPal**: Avinash Gangadharan spent 2+ years at PayPal. He understands payment infrastructure complexity and the value of orchestration
8. **Marketplace dynamics**: Both sides (guests and hosts) need payment reliability. A failed guest payment = lost booking + unhappy host. Rappi uses Yuno to orchestrate payments across its entire marketplace

**Sources:**
- [Stripe Customer Story: Turo Reduces Costs](https://stripe.com/customers/turo)
- [Turo Help: Payment Methods Accepted](https://help.turo.com/en_us/payment-methods-turo-accepts-B1kfEutwee)
- [Turo Help: Getting Paid (US Hosts)](https://help.turo.com/en_us/getting-paid-SyALrVeN9)
- [Turo Help: Setting Up Payout Account](https://help.turo.com/en_us/setting-up-an-account-to-get-paid-HJVvHNeNq)
- [Sacra: Turo at $958M Revenue](https://sacra.com/research/turo-at-958m-revenue/)
- [Sacra: Turo Revenue, Valuation & Funding](https://sacra.com/c/turo/)
- [TechCrunch: Turo IPO Ready But Growth Cratered](https://techcrunch.com/2024/03/08/turo-car-rental-ipo-profitable-growth/)
- [EBC Financial: Turo IPO Cancelled](https://www.ebc.com/forex/turo-ipo-why-it-was-cancelled-and-what-comes-next)
- [Wikipedia: Turo](https://en.wikipedia.org/wiki/Turo_(company))
- [Turo Blog: New CTO and CDO](https://turo.com/blog/news/turo-brings-on-new-chief-data-and-chief-technology-officers/)
- [JoinKudos: Does Turo Take Apple Pay](https://www.joinkudos.com/blog/does-turo-take-apple-pay)
- [BBB: Turo Complaints](https://www.bbb.org/us/ca/san-francisco/profile/auto-renting-and-leasing/turo-1116-378793/complaints)
- [Rentalero: When Does Turo Pay Out](https://www.rentalero.com/turo-payout/)
- [Turo: Meet the Team](https://turo.com/us/en/meet-the-team)
