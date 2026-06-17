# NAVAN | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Navan
=======================================

Logo: https://cdn.brandfetch.io/idSzFMbVJT/w/512/h/512/theme/dark/icon.jpeg
Nombre merchant: Navan

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Multi-PSP Complexity
Tittle_Pain Point_2: Cross-Border Card Costs
Tittle_Pain Point_3: Limited Travel APMs
Tittle_Pain Point_4: Reimbursement Friction
Tittle_Pain Point_5: Auth Rate Gaps

Desc_Pain Point_1: Navan runs Stripe Issuing for card programs, Stripe Payments for travel bookings, Adyen for EU/UK/US card issuance, Celtic Bank for US card banking, and Modern Treasury for reimbursements. Five providers with no unified orchestration layer. Each processor operates independently with separate dashboards and reconciliation streams.
Desc_Pain Point_2: Navan cards are issued in USD, GBP, and EUR but corporate travelers book across 100+ countries. Cross-border card transactions on $7.6B gross bookings incur FX markup on every non-local currency transaction. With a take rate under 10%, even small FX inefficiencies eat directly into Navan's margins.
Desc_Pain Point_3: Navan supports only card payments (Visa/MC/Amex) and corporate card rails for travel bookings. No local payment methods for hotels in Asia (Alipay, WeChat Pay), no BNPL for high-value trips, no real-time bank transfers in Europe (iDEAL, Bancontact) or LATAM (Pix, PSE) for travel spend.
Desc_Pain Point_4: Employee reimbursements run through Modern Treasury across 6 bank payment methods. Processing times vary by country and bank, creating inconsistent reimbursement experiences for a global workforce. Employees in LATAM and APAC wait longer than US/EU counterparts.
Desc_Pain Point_5: With $3.7B in corporate card payment volume flowing through Stripe and Adyen separately, Navan cannot dynamically route each transaction to the highest performing acquirer per BIN and issuer. On 10,000+ corporate customers booking travel globally, smart routing delivers material auth uplift.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (Payments + Issuing)
PSP_2: Adyen (EU/UK/US card issuance)
PSP_3: Celtic Bank (US card issuer)
PSP_4: Modern Treasury (reimbursements)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Alipay
Local_M_2: WeChat Pay
Local_M_3: iDEAL
Local_M_4: Bancontact
Local_M_5: Pix
Local_M_6: PSE
Local_M_7: Klarna
Local_M_8: GrabPay
Local_M_9: Toss Pay
Local_M_10: UPI

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Recovery
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across Stripe and Adyen for every corporate card charge and travel booking. Each transaction routed to the highest performing acquirer for that card BIN, issuer, and merchant category. On $7.6B gross bookings and $3.7B card payment volume, smart routing delivers +3 to 10% auth uplift, recovering millions in failed travel purchases per year.
Desc_Yuno_Cap2: Automatic cascade between Stripe and Adyen eliminates single-processor dependency for critical corporate travel bookings. When one processor declines, Yuno reroutes in milliseconds. Up to 50% recovery on soft declines via instant retry. NOVA AI recovers up to 75% of failed transactions. A declined corporate card during a business trip is a high-severity experience failure.
Desc_Yuno_Cap3: Activates the local APMs Navan lacks for global travel: Alipay and WeChat Pay for China travel bookings, iDEAL in Netherlands, Bancontact in Belgium, Pix in Brazil, PSE in Colombia, Klarna for BNPL on high-value trips, GrabPay in Southeast Asia, Toss Pay in South Korea, UPI in India. One API, 1,000+ payment methods across every travel market.
Desc_Yuno_Cap4: One dashboard replacing Navan's fragmented Stripe + Adyen + Celtic Bank + Modern Treasury stack. Real-time approval rate monitoring across all travel and expense transactions, centralized reconciliation for card issuance, travel bookings, and employee reimbursements, and millisecond anomaly detection via Monitors. Single view of $7.6B in gross bookings.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Navan at a glance:**
- Model: Corporate travel management + expense management + corporate cards (SaaS + transaction fees + interchange)
- Revenue: $537M (FY2025, +33% YoY); trailing 12-month revenue $613M (+32%)
- Gross Bookings: $7.6B (+34% YoY)
- Corporate Card Payment Volume: $3.7B (+35% YoY)
- Customers: 10,000+
- IPO: October 2025, Nasdaq (NAVN), raised $923M at $6.2B valuation
- Previous valuation: $9.2B (Series G, October 2022)
- Total funding raised: $1.6B+
- Founded: 2015 (as TripActions), Palo Alto. Rebranded to Navan in 2023
- CEO & Co-Founder: Ariel Cohen
- CTO & Co-Founder: Ilan Twig
- President: Michael Sindicich (leads Navan Expense, 200% YoY transaction volume growth)
- COO: Nina Herold
- CPO Payments & Expense: Yuval Refua
- EVP Engineering: Ofer Ben-David
- Offices: San Francisco, New York, London, Amsterdam, Tel Aviv, Bengaluru, Singapore, Sydney

**Revenue Model:**
- Travel booking commissions on flights, hotels, car rentals, trains
- SaaS subscription for expense management platform
- Interchange fees on Navan corporate card transactions
- Take rate under 10% on gross bookings

**Payments Infrastructure:**
- Stripe Payments: core travel booking payment processing (since founding)
- Stripe Issuing + Stripe Connect: corporate card program (launched 2019 as TripActions Liquid)
- Adyen N.V.: card issuance in EU (via Adyen Netherlands), US (via Adyen SF Branch), UK (via Adyen London Branch)
- Celtic Bank: US card issuing bank (Member FDIC)
- Stripe Technology Europe Limited: EU card operations
- Stripe Payments UK Limited: UK card operations
- Modern Treasury: employee reimbursement payments across 6 bank payment methods
- Navan Expense grew 80x in volume from 2019 to 2022
- Navan corporate cards issued in USD, GBP, and EUR
- No payment orchestrator detected

**Payment Methods Currently Supported:**
- Navan Corporate Cards: Visa-network physical and virtual cards
- Navan Connect: compatible with existing Visa, MC, Amex corporate cards
- Employee reimbursement via ACH/bank transfer (varies by country)
- Brex partnership: joint global cards and travel management solution
- Citizens Financial Group partnership: integrated card and travel tools
- No local digital wallets (Alipay, WeChat Pay, GrabPay)
- No BNPL options
- No real-time bank transfers (iDEAL, Pix)

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (primary market, largest revenue share)
  Currently offer: Navan Card (Visa), MC/Amex via Connect, ACH reimbursement
  Missing: Venmo/Zelle for employee reimbursement, Affirm (BNPL for high-value trips)
  Faster reimbursement rails would improve employee satisfaction scores.

MARKET 2: United Kingdom (established market, London office)
  Currently offer: Navan Card (GBP), Stripe/Adyen processing
  Missing: Open Banking (Faster Payments), PayPal, Klarna
  UK Open Banking adoption is growing 60%+ YoY. Real-time reimbursement via Faster Payments would differentiate.

MARKET 3: Netherlands / EU (Amsterdam office, Adyen HQ)
  Currently offer: Navan Card (EUR), Adyen processing
  Missing: iDEAL, Bancontact, SEPA instant, Klarna
  iDEAL processes 70%+ of Dutch online payments. EU travelers expect local methods for personal travel expenses.

MARKET 4: India (Bengaluru office, large tech workforce)
  Currently offer: Card payments via Stripe/Adyen
  Missing: UPI (500M+ users), Paytm, PhonePe, RuPay
  UPI processes 12B+ transactions per month in India. Corporate travel in India is one of the fastest growing segments globally.

MARKET 5: Singapore / APAC (Singapore office)
  Currently offer: Card payments via Stripe/Adyen
  Missing: GrabPay, PayNow, Alipay, WeChat Pay, LINE Pay
  Southeast Asia is a mobile-wallet-first market. Chinese business travelers need Alipay/WeChat Pay acceptance.

**Payment Pain Points:**
1. Five payment providers (Stripe, Adyen, Celtic Bank, Modern Treasury, bank partners) with no orchestration
2. Corporate cards only in three currencies (USD, GBP, EUR) despite global travel to 100+ countries
3. No local payment methods for travel bookings in Asia, LATAM, or Middle East
4. Employee reimbursement speed varies by country and bank, creating uneven experience
5. Hotels sometimes decline Navan virtual cards, requiring employees to pay out-of-pocket
6. No BNPL option for high-value corporate trips
7. Cross-border FX markup on non-local currency card transactions
8. Price inflation reported: Navan prices often higher than direct booking with providers
9. No smart routing between Stripe and Adyen for optimal acquirer selection
10. Card activation issues reported in customer complaints

**Key Meeting Angles:**
1. **$7.6B GBV, fragmented stack**: Five payment providers with no orchestration. Yuno unifies Stripe, Adyen, Celtic Bank, and Modern Treasury under one routing layer
2. **Post-IPO growth pressure**: At $6.2B valuation and 33% revenue growth, Navan needs to maintain margins. Smart routing on $3.7B card volume delivers immediate P&L impact
3. **Corporate travel = high-value, high-stakes payments**: A declined corporate card during a business trip is a critical failure. Failover between Stripe and Adyen ensures zero declined trips. InDrive achieved 90% approval across 10 markets with Yuno
4. **APAC and LATAM expansion needs local APMs**: With offices in Singapore, Bengaluru, and Sydney, Navan is aggressively expanding into markets that demand UPI, GrabPay, Pix, and Alipay. McDonald's gained +4.7% auth rate with Yuno orchestration
5. **CPO Payments & Expense is a dedicated role**: Yuval Refua leads payments strategy. This is not a side function, Navan treats payments as a core product pillar
6. **Competitive pressure**: SAP Concur, Brex, Ramp, and Amex GBT all invest in payment innovation. Yuno's 1,000+ APMs and smart routing provide an unfair advantage
7. **Employee reimbursement speed**: Yuno can route reimbursements through the fastest local rail per country, improving the employee experience that drives Navan's NPS
8. **200% YoY transaction volume growth**: Payment volume is scaling faster than infrastructure. Orchestration prevents scaling bottlenecks

**Sources:**
- [Stripe Customer Story: Navan Uses Stripe Issuing](https://stripe.com/customers/navan)
- [Navan Product: Payments](https://navan.com/product/payments)
- [Modern Treasury: Navan Customer Story](https://www.moderntreasury.com/customers/navan)
- [CNBC: Navan Files for IPO](https://www.cnbc.com/2025/09/19/navan-files-for-ipo-public-offering.html)
- [CNBC: Navan Not Far From IPO](https://www.cnbc.com/2024/05/20/navan-is-not-far-from-ipo-on-track-for-2024-profitability-ceo-says.html)
- [Sacra: Navan Revenue and Valuation](https://sacra.com/c/navan/)
- [GetLatka: Navan $537M Revenue](https://getlatka.com/companies/navan.com)
- [Calcalist: Navan IPO at $6.2B](https://www.calcalistech.com/ctechnews/article/skmvcdgjbl)
- [Navan Blog: What Happened in 2024](https://navan.com/blog/what-happened-at-navan-in-2024)
- [Navan Blog: Navan Complaints](https://navan.com/blog/navan-complaints)
- [Navan: Leadership Team](https://navan.com/about/leadership)
- [The Org: Navan Leadership](https://theorg.com/org/navan/teams/leadership-team-1)
- [Navan Press: TripActions Liquid Launches in Europe](https://navan.com/about/press/tripactions-liquid-launches-in-europe)
- [Navan Help: Supported Payment Methods](https://app.navan.com/app/helpcenter/articles/travel/admin/company-payment-methods/supported-payment-methods)
- [Wikipedia: Navan Inc.](https://en.wikipedia.org/wiki/Navan,_Inc.)
- [Mostly Metrics: Navan IPO S1 Breakdown](https://www.mostlymetrics.com/p/navan-ipo-s1-breakdown)
- [Navan Blog: Brex + Navan Partnership](https://navan.com/blog/brex-navan-reimagining-global-cards-and-travel-management)
