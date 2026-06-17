# PREZI | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Prezi
=======================================

Logo: https://asset.brandfetch.io/id7Jy0VJSB/idJEt5v2bK.svg
Nombre merchant: Prezi

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Cards + PayPal Only
Tittle_Pain Point_2: No Bank Debit for Subs
Tittle_Pain Point_3: Billing Complaint Crisis
Tittle_Pain Point_4: Single Acquirer Lock-In
Tittle_Pain Point_5: No Local APMs Globally

Desc_Pain Point_1: Prezi accepts only credit/debit cards and PayPal for subscriptions. No digital wallets, no bank transfers, no local APMs. Users in markets where cards are secondary (India, Brazil, Poland) hit a paywall when upgrading from the free tier.
Desc_Pain Point_2: 160M+ users across 190+ countries but no SEPA DD for European teams, no ACH for US organizations, no UPI for India. Annual billing on a single card creates renewal risk. Failed cards trigger 10-day retry loops with no alternate method.
Desc_Pain Point_3: BBB rating of F. Trustpilot 3.2/5 with billing complaints dominating negative reviews. Users report unauthorized renewals, failed cancellations, and Error 500 on cancellation pages. Payment infrastructure gaps amplify refund and chargeback volume.
Desc_Pain Point_4: All subscription charges run through a single payment processor. Any outage blocks 100% of new signups and renewals across Standard, Plus, Premium, and Teams plans. No fallback acquirer for failed charges.
Desc_Pain Point_5: Prezi has offices in Budapest, San Francisco, Riga, and Berlin, serving 160M+ users globally. Yet checkout offers zero local payment methods. No Pix in Brazil, no iDEAL in Netherlands, no BLIK in Poland, no Konbini in Japan.

SLIDE 1: PSP TOPOLOGY

PSP_1: Card Processor (likely Stripe)
PSP_2: PayPal
PSP_3: Apple App Store (iOS IAP)
PSP_4: Google Play (Android IAP)
PSP_5: (none detected)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: SEPA Direct Debit
Local_M_2: UPI
Local_M_3: Pix
Local_M_4: iDEAL
Local_M_5: BLIK
Local_M_6: Bancontact
Local_M_7: Giropay
Local_M_8: Boleto
Local_M_9: Konbini
Local_M_10: OXXO

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route every subscription charge and renewal to the best performing acquirer per card BIN, country, and issuer. With $53M+ revenue and 160M+ users, a 3-10% auth uplift on annual renewals recovers millions and reduces the chargeback volume driving the BBB F rating.
Desc_Yuno_Cap2: When the primary processor declines a subscription renewal, Yuno cascades to an alternate acquirer in milliseconds instead of retrying the same failing card for 10 days. Recovers up to 50% of failed charges, cutting involuntary churn across all plan tiers.
Desc_Yuno_Cap3: Unlocks the local methods 160M+ users demand: SEPA DD in Europe (Prezi's HQ region), UPI in India, Pix in Brazil, iDEAL in Netherlands, BLIK in Poland, Konbini in Japan, Bancontact in Belgium. One API, 1,000+ payment methods, zero per-market engineering.
Desc_Yuno_Cap4: Single dashboard consolidating the card processor, PayPal, App Store, and Google Play into one view. Real-time auth rate monitoring across every market, centralized reconciliation, and NOVA provides millisecond anomaly detection to catch billing failures before they become BBB complaints.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Prezi at a glance:**
- Founded: 2009 in Budapest, Hungary
- Co-Founders: Adam Somlai-Fischer, Peter Halacsy, Peter Arvai (Executive Chairman)
- CEO: Jim Szafranski (since July 2020)
- HQ: Budapest, Hungary; Offices: San Francisco, Riga (Latvia), Berlin
- Total funding raised: $73.1M (investors: Spectrum Equity, Accel, Heartcore Capital, Cinco Capital)
- Revenue: $53.7M in 2024 (up from ~$46M)
- Users: 160M+ worldwide; 400M+ presentations created
- Employees: ~262 (84 engineers, 21 sales reps, 19 marketing)
- Products: Prezi Present (zoomable canvas), Prezi Video (virtual presentations), Prezi Design (infographics/data viz, built on Infogram acquisition)
- Prezi AI: AI-powered prompt-to-presentation (launched 2024)
- Acquisition: Infogram (data visualization, Latvia, 2017)
- Pricing: Free ($0), Standard ($7/mo), Plus ($15/mo), Premium ($25/mo), Teams ($39/user/mo); Education from $3/mo
- All paid plans billed annually; 14-day free trial available
- Notable customers: Clinton Foundation, Lufthansa, IBM, Salesforce, Marriott, TED/SXSW

**Confirmed PSPs:**
- Card processor: Likely Stripe or Braintree (not explicitly confirmed; payment data not stored by Prezi)
- PayPal: Secondary payment option for subscriptions
- Apple App Store: iOS in-app purchase for mobile
- Google Play: Android in-app purchase for mobile
- No payment orchestrator detected
- No local APMs detected on web checkout

**Billing details:**
- Accepted: Credit/debit cards (Visa, Mastercard, likely Amex) and PayPal
- Billing cycle: Annual (all paid plans)
- Currency: USD primary; local currency conversion via card network
- Failed payments: Multiple retry attempts within 10 days; then subscription suspended
- Refund policy: Denied after 14 days (widely complained about)
- No bank debit (ACH, SEPA DD) option
- No digital wallets (Apple Pay, Google Pay) on web checkout

**Payment issues documented:**
- BBB rating: F with multiple unresolved complaints
- Trustpilot: 3.2/5 from 578 reviews; billing complaints dominate negative reviews
- Common complaints: Unauthorized renewals after cancellation, Error 500 on cancellation pages, difficulty obtaining refunds
- Users report being charged after free trials without clear notice
- Prezi "almost universally denies refunds after 14 days"
- Users advised to file credit card disputes as primary recourse

**Top Markets Gap Analysis:**

MARKET 1: United States (largest revenue market)
  Offer: Visa/MC, PayPal
  Missing: ACH Direct Debit, Apple Pay, Google Pay (web)
  No bank debit option for annual enterprise subscriptions

MARKET 2: Hungary / Europe (HQ in Budapest, offices in Berlin, Riga)
  Offer: Visa/MC, PayPal
  Missing: SEPA Direct Debit, iDEAL, Bancontact, Giropay, BLIK
  European SaaS standard is SEPA DD for recurring; Prezi offers none

MARKET 3: India (large user base, education market)
  Offer: Visa/MC, PayPal
  Missing: UPI, Netbanking, Paytm, RuPay
  UPI dominates Indian digital payments; education pricing exists but UPI does not

MARKET 4: Brazil (growing SaaS market)
  Offer: Visa/MC, PayPal
  Missing: Pix, Boleto
  Pix processes 45B+ transactions/year; essential for conversion in Brazil

MARKET 5: Japan (presentation culture, enterprise market)
  Offer: Visa/MC, PayPal
  Missing: Konbini, PayPay, LINE Pay, JCB
  Japan's unique payment preferences make local methods critical

**Key meeting angles:**
1. **BBB F rating / billing crisis**: Unauthorized renewal complaints stem from rigid billing with no alternate payment methods. Better orchestration with SEPA DD, UPI, and local methods reduces involuntary charges and chargebacks.
2. **160M users, cards-only checkout**: Massive user base but minimal payment diversity. Adding local APMs lifts free-to-paid conversion in every non-US market.
3. **European company, no European payments**: Budapest HQ, Berlin and Riga offices, strong EU user base, but no SEPA DD. This is the most obvious quick win.
4. **10-day retry on same card**: Failed renewal recovery is primitive. Failover to alternate acquirer recovers up to 50% of failures immediately.
5. **Education market opportunity**: Prezi is strong in education ($3/mo plans, ConnectED initiative). Students in India, Brazil, and emerging markets prefer UPI and Pix.
6. **Competitive pressure from Canva**: Canva accepts 50+ local payment methods globally. Prezi's cards+PayPal approach puts it at a conversion disadvantage in every market.

**Sources:**
- [Prezi Official Website](https://prezi.com/)
- [Prezi About Page](https://prezi.com/about/)
- [Prezi Pricing Page](https://prezi.com/gts/pricing/)
- [Prezi Payments Support Center](https://support.prezi.com/hc/en-us/sections/360000761553-Payments)
- [Prezi Changing Payment Information](https://support.prezi.com/hc/en-us/articles/360011202813-Changing-payment-information)
- [Prezi Payment Failures](https://support.prezi.com/hc/en-us/articles/360054588414-Why-did-my-payment-fail)
- [Prezi Automatic Renewals](https://support.prezi.com/hc/en-us/articles/360059557613-How-are-automatic-renewal-payments-made)
- [Prezi Revenue $53.7M - Getlatka](https://getlatka.com/companies/prezi)
- [Prezi Wikipedia](https://en.wikipedia.org/wiki/Prezi)
- [Prezi BBB Complaints](https://www.bbb.org/us/ca/oakland/profile/computer-software-developers/prezi-inc-1116-389230/complaints)
- [Prezi $57M Funding - TechCrunch](https://techcrunch.com/2014/11/19/prezi-secures-57m-growth-round-from-spectrum-and-accel-passes-50m-users/)
- [Prezi Review 2025 - Skywork](https://skywork.ai/blog/prezi-review-2025-2/)
- [Prezi AI Review 2026](https://max-productive.ai/ai-tools/prezi/)
- [Prezi - Tracxn](https://tracxn.com/d/companies/prezi/__SHytg-drLnw3WkdRMST909Dc_l7yn4gdAS0E-Z9mn_4)
- [Prezi - Crunchbase](https://www.crunchbase.com/organization/prezi)
- [Prezi Pricing - Costbench](https://costbench.com/software/ai-presentations/prezi/)
- [Brandfetch: Prezi Logo](https://brandfetch.com/prezi.com)
