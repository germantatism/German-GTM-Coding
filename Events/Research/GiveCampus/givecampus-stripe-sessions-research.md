# GIVECAMPUS | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: GiveCampus
=======================================

Logo: https://seeklogo.com/images/G/givecampus-logo-C89F34BC4A-seeklogo.com.png
Nombre merchant: GiveCampus

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Stripe-Only Processing
Tittle_Pain Point_2: US-Centric Payment Stack
Tittle_Pain Point_3: Giving Day Spike Risk
Tittle_Pain Point_4: Cross-Border Donor Loss
Tittle_Pain Point_5: High Processing Fees

Desc_Pain Point_1: All payments on GiveCampus are processed through Stripe. No acquirer redundancy for 1,500+ educational institutions processing $5B+ in cumulative donations. A single Stripe outage during a Giving Day could cost a university its entire annual fundraising target in hours.
Desc_Pain Point_2: Payment stack built for US donors: Visa, MC, Amex, Discover, ACH, PayPal, Venmo, Cash App Pay, Apple Pay, Google Pay, Stripe Link, and DAFpay. International alumni in Europe, Asia, and LATAM are limited to cross-border card payments with FX markups and no local payment methods.
Desc_Pain Point_3: Giving Days generate massive traffic spikes where thousands of donations arrive in minutes. Single-processor dependency creates a bottleneck. If Stripe throttles or experiences latency, completed donations drop and schools lose momentum in time-sensitive campaigns.
Desc_Pain Point_4: Universities have alumni in 180+ countries. International donors face cross-border card fees, FX conversion charges (PayPal adds 1.5% spread), and no local payment options. No SEPA DD for European alumni, no Pix for Brazilian alumni, no UPI for Indian alumni.
Desc_Pain Point_5: Per-transaction processing fees on donations reduce net fundraising proceeds. ACH offers lower fees but is US-only. International card transactions incur higher cross-border interchange. No local acquiring in non-US markets means every international donation pays premium processing rates.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (sole payment processor, all transactions)
PSP_2: PayPal (digital wallet, FX conversion)
PSP_3: Venmo (US mobile wallet)
PSP_4: Chariot (Donor-Advised Fund integration)
PSP_5: Stripe Link (accelerated checkout, 1-click)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: SEPA Direct Debit (EU alumni)
Local_M_2: Pix (Brazil)
Local_M_3: UPI (India)
Local_M_4: iDEAL (Netherlands)
Local_M_5: BACS Direct Debit (UK)
Local_M_6: Bancontact (Belgium)
Local_M_7: BLIK (Poland)
Local_M_8: Boleto (Brazil)
Local_M_9: Konbini (Japan)
Local_M_10: Open Banking (UK/EU)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each donation to the highest-performing acquirer by donor card BIN, issuer, and country. With 1,500+ institutions processing millions of annual donations, even a 3% approval uplift means thousands more successful gifts per campaign. Smart Routing maximizes authorization rates for international alumni giving from cross-border cards.
Desc_Yuno_Cap2: Automatic cascade removes GiveCampus's sole Stripe dependency. During Giving Day traffic spikes, if Stripe experiences latency or declines, Yuno reroutes to the next best acquirer in milliseconds. Up to 50% recovery on soft declines. Critical for time-sensitive campaigns where every failed transaction means a lost donor gift.
Desc_Yuno_Cap3: Activates the payment methods global alumni need: SEPA DD for European graduates, BACS DD for UK alumni, Pix in Brazil, UPI in India, iDEAL in Netherlands, Konbini in Japan, BLIK in Poland. One API, 1,000+ payment methods. Converts international alumni from lapsed donors to active givers by removing payment friction.
Desc_Yuno_Cap4: One dashboard consolidating Stripe, PayPal, Venmo, Chariot DAF, Cash App Pay, and cryptocurrency donations into a unified view. Real-time donation monitoring across all payment rails, centralized reconciliation for 1,500+ institutions. Full campaign-level visibility during high-stakes Giving Days and capital campaigns.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**GiveCampus at a glance:**
- Digital fundraising and engagement platform for non-profit educational institutions
- Founded 2014 by Kestrel Linder (CEO) and Michael Kong
- HQ: Washington, DC. ~130-150 employees across North America and Asia
- Y Combinator alumnus (W15 batch)
- Total funding: $50.8M. $50M Series A led by Silversmith Capital Partners (2022)
- Notable investors: Claire Hughes Johnson (Stripe executive), Michael Seibel (YC Managing Director)
- $5B+ in cumulative charitable giving facilitated since 2015
- 1,500+ colleges, universities, and K-12 schools on the platform
- Millions of donors served
- Profitable since 2016
- Revenue: ~$20M+ estimated annual (2022 figure)
- Products: Online Giving, Giving Days, Crowdfunding, P2P Fundraising, Volunteer Management, Texting, Personalized Video, Events, Wealth Analytics, GC Connect (in-person), WebPay

**Confirmed PSPs and Infrastructure:**
- Stripe: sole payment processor (all transactions)
- Stripe Link: accelerated checkout / 1-click payment
- PayPal: digital wallet integration (includes 1.5% FX spread on international)
- Venmo: US mobile wallet donations
- Cash App Pay: recently added partnership (2025)
- Apple Pay: mobile and desktop donations
- Google Pay: digital wallet integration
- Chariot: Donor-Advised Fund (DAF) grant integration
- DAFpay: DAF donation widget
- Cryptocurrency: crypto donation acceptance
- GC Connect: in-person tap-to-pay card reader
- WebPay: browser-saved payment method checkout
- No payment orchestrator detected
- No multi-acquirer routing identified

**Accepted payment methods:**
- Credit/debit cards: Visa, Mastercard, Amex, Discover (+ international premium brands)
- ACH bank transfer (US only, lower fees)
- PayPal
- Venmo
- Cash App Pay
- Apple Pay
- Google Pay
- Stripe Link (1-click checkout)
- DAFpay (Donor-Advised Funds)
- Chariot (DAF grants)
- Cryptocurrency donations
- Check and cash (offline, added to online totals)
- In-person: tap-to-pay via GC Connect card reader

**Fee structure:**
- Competitive per-transaction rate, billed monthly (pay-as-you-go)
- Up to 12.5% discount by prepaying processing fees based on projected fundraising
- Donor-covered fees option: donors can add processing cost to their gift
- 100% of donations go directly to institution via connected account merchant agreements
- ACH transactions have lower fees than card transactions
- International transactions incur FX conversion (PayPal adds 1.5% spread)

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (core market, ~90%+ of transactions)
  Accepted: Visa/MC/Amex/Discover, ACH, PayPal, Venmo, Cash App Pay, Apple Pay, Google Pay, Link
  Missing: Zelle (direct bank integration)
  Note: Excellent coverage. WebPay and Link reduce checkout friction significantly

MARKET 2: United Kingdom (major alumni market)
  Accepted: Visa/MC/Amex (cross-border, USD)
  Missing: BACS Direct Debit, Open Banking, GBP pricing, Faster Payments
  Note: UK universities and US schools with UK alumni need local payment methods

MARKET 3: Europe/EU (alumni diaspora)
  Accepted: Visa/MC (cross-border, USD)
  Missing: SEPA Direct Debit, iDEAL (NL), Bancontact (BE), BLIK (PL), EUR pricing
  Note: Recurring SEPA DD would enable sustained annual giving from EU alumni

MARKET 4: India (large international student alumni base)
  Accepted: Visa/MC (cross-border, USD)
  Missing: UPI, RuPay, Net Banking, INR pricing
  Note: UPI has 14B+ monthly transactions. Indian alumni could give via UPI with minimal friction

MARKET 5: Brazil / Latin America (growing alumni base)
  Accepted: Visa/MC (cross-border, USD)
  Missing: Pix, Boleto, BRL pricing, OXXO (Mexico)
  Note: Pix handles 70%+ of Brazilian digital payments. Local methods unlock LATAM giving

**Key meeting angles:**
1. **Stripe-only for $5B+ cumulative** | Every donation flows through a single processor. Zero redundancy during high-stakes Giving Days where hourly volume can 10x
2. **Stripe executive is an investor** | Claire Hughes Johnson (Stripe COO) invested in GiveCampus. Strong Stripe relationship but creates PSP lock-in
3. **Giving Day vulnerability** | Traffic spikes during Giving Days are extreme. A processor outage during a 24-hour campaign is catastrophic. Multi-acquirer failover is existential insurance
4. **Global alumni, US-only payments** | 1,500+ schools have alumni worldwide but payment stack is designed for US donors. International alumni face FX markups and card-only checkout
5. **Processing fee sensitivity** | Non-profit sector is extremely fee-conscious. Local acquiring for international donations would reduce cross-border interchange costs
6. **Profitable, mission-driven** | Profitable since 2016, mission-aligned to education. Payment cost savings directly increase net fundraising proceeds for schools

**Sources:**
- [GiveCampus Payment Processing](https://go.givecampus.com/capabilities/payment-processing/)
- [GiveCampus Payment Methods Guide](https://support.givecampus.com/hc/en-us/articles/39409824986647-Payment-methods-on-GiveCampus-a-complete-guide)
- [GiveCampus Digital Wallets and Crypto](https://go.givecampus.com/capabilities/digital-wallets/)
- [GiveCampus Cash App Pay Partnership](https://go.givecampus.com/about-us/awards-press-media/givecampus-announces-partnership-with-cash-app-pay/)
- [GiveCampus WebPay](https://support.givecampus.com/hc/en-us/articles/29182728722071-Introducing-WebPay)
- [GiveCampus Stripe Payment States](https://support.givecampus.com/hc/en-us/articles/29095516568983-What-do-the-various-Stripe-payment-states-mean)
- [GiveCampus Pricing](https://go.givecampus.com/pricing/)
- [GiveCampus Y Combinator Profile](https://www.ycombinator.com/companies/givecampus)
- [Crunchbase: GiveCampus $50M Raise](https://news.crunchbase.com/edtech/venture-capital-fundraising-schools-startups/)
- [GiveCampus Leadership Team](https://go.givecampus.com/mission/our-team/)
- [Tracxn: GiveCampus Profile](https://tracxn.com/d/companies/givecampus/__TNh4WvKK5LQXZ9VXCR3pQKIGnZJYs2ojuPLFZvDypUM)
- [GiveCampus Cryptocurrency Donations](https://support.givecampus.com/hc/en-us/articles/29183861759895-Cryptocurrency-Donations-on-GiveCampus)
