# PHOREST SOFTWARE | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Phorest Software
=======================================

Logo: https://cdn.brandfetch.io/phorest.com/w/512/h/512/theme/dark/icon.jpeg
Nombre merchant: Phorest Software

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Single Stripe Dependency
Tittle_Pain Point_2: No BNPL for Premium Svcs
Tittle_Pain Point_3: Limited Local APMs
Tittle_Pain Point_4: No Smart Routing Layer
Tittle_Pain Point_5: Cross-Border Complexity

Desc_Pain Point_1: PhorestPay runs entirely on Stripe across all 10 countries (previously Bancard in the US, now migrated to Stripe). 11,000+ salons and 155,000+ professionals depend on a single PSP for card terminals, online payments, cardless checkout, deposits, and gift vouchers. No failover processor exists. Stripe outages or declines directly impact salon revenue with no alternative routing path.
Desc_Pain Point_2: Med spa treatments, hair extensions, bridal packages, and premium wellness services range from $200 to $5,000+. No BNPL option exists for clients who want to finance high-value treatments. Salons lose premium bookings when clients cannot afford full upfront payment. Klarna, Affirm, or Afterpay would increase average transaction value and booking conversion.
Desc_Pain Point_3: Phorest operates in UK, Ireland, Germany, Netherlands, Finland, US, Canada, Australia, and UAE but the payment stack only supports card schemes (Visa, MC, Amex, Maestro) and digital wallets (Apple Pay, Google Pay, Samsung Pay). No iDEAL for Netherlands, no Bancontact for Belgium expansion, no SEPA for recurring memberships, no local wallets for UAE or Australia.
Desc_Pain Point_4: Despite processing payments for 11,000+ salons across 10 countries via Stripe, Phorest has no intelligent routing layer. Every transaction follows the same Stripe path regardless of card issuer, BIN, geography, or decline history. Stripe Connect handles multi-market distribution but does not optimize per-transaction routing for auth rate maximization.
Desc_Pain Point_5: PhorestPay card terminals are available in 15 Stripe Terminal countries but Phorest only actively operates in 10. Each market has different card scheme preferences, local payment methods, and regulatory requirements. Germany needs Giropay, Finland needs MobilePay, UAE needs Mada and local wallets. No orchestration layer to manage per-market payment optimization.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (primary, powers PhorestPay globally)
PSP_2: Stripe Connect (multi-market distribution)
PSP_3: Stripe Terminal (card terminals)
PSP_4: Bancard (legacy US, migrating to Stripe)
PSP_5: None identified

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: iDEAL (Netherlands)
Local_M_2: Klarna (BNPL)
Local_M_3: Bancontact
Local_M_4: SEPA Direct Debit
Local_M_5: Giropay (Germany)
Local_M_6: Afterpay
Local_M_7: PayPal
Local_M_8: Mada (UAE)
Local_M_9: MobilePay (Finland)
Local_M_10: Clearpay (UK)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Recovery
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across processors for every salon payment, deposit, membership charge, and gift voucher sale. Each transaction routed to the highest performing acquirer for that card BIN, issuer, and market. Across 11,000+ salons in 10 countries processing appointments, deposits, and retail sales, smart routing delivers +3 to 10% auth uplift. With 335% payments revenue growth on Stripe, even small auth improvements unlock significant incremental revenue.
Desc_Yuno_Cap2: Automatic cascade eliminates PhorestPay's single-Stripe dependency. When Stripe declines a deposit charge or card-on-file payment, Yuno reroutes to an alternative processor in milliseconds. Up to 50% recovery on soft declines via instant retry. NOVA AI recovers up to 75% of failed transactions. For salons enforcing no-show and late cancellation fees, a declined stored card means lost revenue protection.
Desc_Yuno_Cap3: Activates the APMs Phorest needs for each market: iDEAL for Dutch salons, Giropay for German salons, MobilePay for Finnish clients, SEPA Direct Debit for recurring memberships across Europe, Mada for UAE salons, Clearpay for UK clients, Klarna and Afterpay for BNPL on premium treatments ($200-$5,000+). One API, 1,000+ payment methods across all 10 Phorest markets.
Desc_Yuno_Cap4: One dashboard replacing PhorestPay's Stripe-only stack with unified real-time visibility across all markets. Centralized approval rate monitoring for 11,000+ salons, automated reconciliation for deposits, tips (PhorestTips), memberships, and retail sales. Millisecond anomaly detection via Monitors across all 10 countries. Enables Phorest to scale to new markets without building per-country Stripe Terminal integrations.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Phorest at a glance:**
- Model: Salon and med spa management SaaS (booking, marketing, POS, payments, CRM)
- Industry: Beauty and wellness technology
- Users: 155,000+ hair, beauty, and clinic professionals
- Businesses: 11,000+ salons, spas, and med spas
- Appointments: 7 million per month
- Countries: 10 (UK, Ireland, Germany, Netherlands, Finland, US, Canada, Australia, UAE, and more)
- Employees: 471 (as of Feb 2026)
- Headquarters: Dublin, Ireland (US HQ: Philadelphia)
- Founded: 2003 (by Ronan Perceval)
- CEO & Founder: Ronan Perceval
- Co-founder: Jamie Mysercough
- Revenue: $50M (2024), up from $23M (2021)
- Revenue growth: ~40% annually during growth phase
- Total funding: $49.4M over 5 rounds
- Key investors: Susquehanna Growth Equity ($20M in 2018), Enterprise Ireland, AIB Seed Capital Fund
- Payments revenue growth: 335% after unifying online and in-person payments on Stripe

**Core Products:**
- Salon Management: Scheduling, calendar, client management, stock, reporting, rotas
- Online Booking: 24/7 widget for website, social media, branded app
- PhorestPay: Integrated payment processing powered by Stripe
- PhorestPay Card Terminals: Touchscreen, wireless, Stripe Terminal powered
- Cardless Checkout: Stored card, "Uber-like" checkout experience
- PhorestTips: Integrated card-based tipping (~25% tip increase)
- Marketing Suite: Email, SMS, social media advertising
- Branded App: Custom salon app for clients
- Online Store: Gift vouchers (~$60 average), retail products
- Membership Billing: Recurring revenue programs
- AI Features: AI-powered management platform

**Recent Developments:**
- 2025: Digital Loyalty program (fully digital rewards tracking)
- 2025: Referrals feature (shareable referral links)
- Migrating US users from Bancard to Stripe
- Stripe Terminal card terminals launched across markets
- 335% payments revenue boost from unifying online + in-person payments

**Payments Infrastructure:**
- Stripe: Primary PSP powering PhorestPay globally
- Stripe Connect: Multi-market payment distribution across 10 countries
- Stripe Terminal: Card terminal hardware (touchscreen, wireless)
- Bancard / International Bancard: Legacy US processor (migrating to Stripe)
- PCI-DSS compliant, SSL encryption
- 1 working day payouts

**Payment Methods (Current):**
- Card terminals: Visa, Mastercard, Amex, Maestro
- Digital wallets: Apple Pay, Google Pay, Samsung Pay
- Cardless Checkout: Stored card-on-file payments
- Online payments: Deposits, gift vouchers
- Virtual Terminal: Phone payments
- No PayPal
- No BNPL
- No local European payment methods (iDEAL, SEPA, Giropay)
- No local UAE or Australian payment methods

**Payment Features:**
- Custom deposits per booking (configurable by service and client risk level)
- No-show and late cancellation fee enforcement via stored cards
- Automatic transaction syncing with POS
- Live transaction status tracking
- Refund processing linked to client profiles
- Online gift vouchers (average $60 spend)
- Membership recurring billing
- PhorestTips integration (~25% tip increase)

**Top 5 Markets Gap Analysis:**

MARKET 1: United Kingdom & Ireland (core market, largest salon base)
  Currently offer: Visa/MC/Amex/Maestro, Apple Pay, Google Pay, Samsung Pay
  Missing: Open Banking, Clearpay (Afterpay UK), PayPal, Klarna
  UK salons increasingly need BNPL for premium treatments. Open Banking reduces card fees.

MARKET 2: Germany (growth market)
  Currently offer: Visa/MC/Amex, Apple Pay, Google Pay
  Missing: Giropay, SEPA Direct Debit, Klarna, PayPal
  German consumers strongly prefer Giropay and SEPA. Klarna originated in the Nordics and is widely used.

MARKET 3: Netherlands (active market)
  Currently offer: Visa/MC, Apple Pay, Google Pay
  Missing: iDEAL (dominant, 70%+ of online payments), Bancontact, SEPA
  iDEAL is essential for Dutch consumers. Without it, online deposits and gift voucher sales lose significant conversion.

MARKET 4: United States & Canada (expansion market, US HQ in Philadelphia)
  Currently offer: Visa/MC/Amex/Discover, Apple Pay, Google Pay (migrating from Bancard to Stripe)
  Missing: Klarna, Affirm, Afterpay, PayPal, Venmo
  US med spa market is booming. Premium treatments ($500-$5,000+) need BNPL. PayPal is expected at checkout.

MARKET 5: Australia & UAE (newer markets)
  Currently offer: Visa/MC, Apple Pay, Google Pay
  Missing: Afterpay (dominant BNPL in Australia), BPAY, Mada (UAE), local UAE wallets
  Afterpay is the default BNPL in Australian beauty. UAE requires Mada card network support.

**Payment Pain Points:**
1. Single Stripe dependency across all 10 countries with no failover
2. No BNPL for premium treatments ($200-$5,000+ med spa, bridal, extensions)
3. No iDEAL in Netherlands (70%+ of Dutch online payments)
4. No Giropay or SEPA for German market
5. No Open Banking for UK salons (lower fees than card processing)
6. No PayPal despite being universally expected at checkout
7. No Afterpay in Australia (dominant beauty BNPL)
8. No smart routing to optimize auth rates across 10 countries
9. Stored card declines (no-show fees, deposits) have no failover path
10. Membership recurring billing limited to card-on-file with no SEPA alternative

**Key Meeting Angles:**
1. **11,000+ salons, 10 countries, single PSP**: PhorestPay runs entirely on Stripe. Yuno adds failover and smart routing while preserving the Stripe Connect architecture
2. **335% payments revenue growth**: Phorest is aggressively monetizing payments. Yuno maximizes this by improving auth rates +3-10% and adding BNPL that increases average transaction value
3. **BNPL for premium beauty**: Med spas, bridal packages, and wellness treatments ($200-$5,000+) need financing. Klarna and Affirm via Yuno increase conversion. Zero current BNPL exists
4. **Dutch market gap**: iDEAL handles 70%+ of Dutch online payments. Phorest operates in Netherlands without it. Yuno activates iDEAL via single API
5. **Stored card vulnerability**: No-show fees and deposits rely on card-on-file charges. When Stripe declines, the salon loses its revenue protection. Yuno's failover recovers up to 50% of soft declines
6. **Scale opportunity**: $50M revenue, 155,000+ professionals, 7M appointments/month. McDonald's gained +4.7% auth rate with Yuno. InDrive achieved 90% approval across 10 markets

**Sources:**
- [Phorest](https://www.phorest.com/)
- [PhorestPay Payment Processing](https://www.phorest.com/features/salon-payment-processing/)
- [PhorestPay Card Terminals Launch](https://www.phorest.com/updates/introducing-phorestpay-card-terminals/)
- [Phorest About Us](https://www.phorest.com/us/about/)
- [Stripe Customer: Phorest](https://stripe.com/customers/phorest)
- [PhorestPay Bancard to Stripe Migration](https://support.phorest.com/hc/en-us/articles/10889233110802)
- [PhorestPay Cardless Checkout](https://support.phorest.com/hc/en-us/articles/4403948650770)
- [PhorestPay Card Terminal Setup](https://support.phorest.com/hc/en-us/articles/5423341386642)
- [Phorest Wikipedia](https://en.wikipedia.org/wiki/Phorest)
- [Phorest SGE Investment (Irish Times)](https://www.irishtimes.com/business/technology/phorest-software-raises-20m-from-us-investment-firm-1.3532257)
- [Phorest US HQ (Philadelphia Inquirer)](https://www.inquirer.com/business/phorest-salon-software-sge-susquehanna-international-20190812.html)
- [SGE: Phorest](https://www.sgep.com/company/phorest)
- [Crunchbase: Phorest](https://www.crunchbase.com/organization/phorest)
- [Tracxn: Phorest](https://tracxn.com/d/companies/phorest/)
- [Capterra: Phorest](https://www.capterra.com/p/113530/Phorest-Salon-Software/)
