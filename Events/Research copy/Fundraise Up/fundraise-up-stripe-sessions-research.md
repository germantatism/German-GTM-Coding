# FUNDRAISE UP | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Fundraise Up
═══════════════════════════════════════

Logo: https://brandfetch.com/fundraiseup.com
Nombre merchant: Fundraise Up

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: LATAM/APAC APM Blind Spot
Tittle_Pain Point_2: Stripe Single Acquirer
Tittle_Pain Point_3: Donor Abandonment
Tittle_Pain Point_4: Recurring Gift Failures
Tittle_Pain Point_5: FX Settlement Limits

Desc_Pain Point_1: Zero local APMs in LATAM, Africa, or Asia. No Pix, UPI, OXXO, GCash, M-Pesa. Aid nonprofits fundraise globally but collect only via cards and few EU/ANZ debits.
Desc_Pain Point_2: Stripe is the sole acquirer for cards, wallets, and bank debits. No failover. Any Stripe disruption blocks donations for 1,000+ nonprofits at once.
Desc_Pain Point_3: 13% of donors abandon checkout when preferred method is missing. In India, Brazil, Mexico, card-only checkout means most potential donors cannot give.
Desc_Pain Point_4: Monthly donors are the highest-value segment. When renewals fail, no cascade to another processor. PayPal billing cancellations silently break recurring plans.
Desc_Pain Point_5: Stripe payouts in only 30+ countries. Nonprofits outside cannot receive funds directly. 135 currencies accepted but settlement is limited, adding complexity.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe
PSP_2: PayPal
PSP_3: Gemini (crypto)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: UPI
Local_M_3: OXXO
Local_M_4: GCash
Local_M_5: M-Pesa
Local_M_6: Boleto
Local_M_7: BLIK
Local_M_8: PSE
Local_M_9: Maya
Local_M_10: Konbini

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across Stripe and PayPal by card BIN, issuer, geography. Fundraise Up already achieves 28% conversion (2x industry). Smart routing pushes higher by ensuring every donation reaches the optimal acquirer. 3% uplift = massive recovered giving.
Desc_Yuno_Cap2: Automatic cascade eliminates single Stripe dependency. When Stripe declines a recurring donation, Yuno reroutes in milliseconds. Up to 50% recovery on soft declines. For monthly giving (highest LTV), every recovered renewal compounds over the donor lifecycle.
Desc_Yuno_Cap3: Activates the APMs global donors need: Pix in Brazil, UPI in India, M-Pesa in Kenya, OXXO in Mexico, GCash in Philippines, BLIK in Poland, PSE in Colombia, Konbini in Japan. One API, 1,000+ payment methods. Eliminates the 13% donor abandonment caused by missing payment options.
Desc_Yuno_Cap4: One dashboard unifying Stripe + PayPal + Gemini settlements. Real-time approval monitoring per market, reconciliation across 135+ currencies, anomaly detection via NOVA. 75% ops reduction. Single compliance view for global nonprofit audits.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Fundraise Up at a glance:**
- AI-powered nonprofit digital fundraising platform, founded 2017
- 1,000+ nonprofit organizations across 4 core countries (US, Canada, UK, Australia)
- Funding: $82M total raised ($70M Series B led by Summit Partners, Dec 2024)
- Business model: 4% per donation + payment processor fees; no setup fees, no contracts
- 28% average conversion rate (2x industry average of 12%)
- 86% of donors opt to cover transaction fees (92% when prompted)
- Never lost an enterprise-level nonprofit customer in 7 years of operation
- 135+ currencies accepted, 25 language localizations
- Growing team ~50% in 2025

**Notable nonprofit clients:**
- UNICEF USA (recurring upsell generated $3M additional annual revenue, 82% fee coverage)
- Canadian Red Cross (48% donation increase, 64% revenue increase, saved ~$1M in card fees in 9 months)
- The Salvation Army UK
- American Heart Association
- Community FoodBank of New Jersey (71% annual revenue increase)
- International Justice Mission UK (140% increase in new monthly donor value)

**Confirmed PSPs:**
- Stripe: primary processor (cards, Apple Pay, Google Pay, ACH, SEPA, BACS, BECS, PADs, iDEAL)
- PayPal: secondary (PayPal wallet + Venmo US only)
- Gemini: cryptocurrency donations
- Official Stripe partner (Stripe Partner Directory)
- Stripe fee: 2.2% + $0.30 per transaction

**Donor Payment Methods Currently Supported:**
- Cards: Visa, MC, Amex, Discover (US/CA), Diners, JCB (Asia), Cartes Bancaires (EU), China UnionPay (Asia)
- Wallets: Apple Pay, Google Pay, PayPal, Venmo (US)
- Bank debits: ACH (US), PADs (Canada), BACS (UK), SEPA (EU), BECS (Australia)
- Bank redirects: iDEAL (Netherlands)
- Crypto: via Gemini

**Top Markets Gap Analysis:**

MARKET 1: United States (primary market)
  Accepted: Visa/MC/Amex/Discover, Apple Pay, Google Pay, PayPal, Venmo, ACH
  Missing: Cash App Pay
  Note: Best covered market. ACH + wallets + cards provide strong US coverage.

MARKET 2: United Kingdom
  Accepted: Visa/MC/Amex, Apple Pay, Google Pay, PayPal, BACS DD
  Missing: Open Banking (Pay by Bank)
  Note: Salvation Army UK is a customer. Open Banking growing for UK recurring giving.

MARKET 3: Canada
  Accepted: Visa/MC/Amex/Discover, Apple Pay, Google Pay, PayPal, PADs
  Missing: Interac
  Note: Canadian Red Cross is a top customer. Interac is Canada's dominant payment rail.

MARKET 4: Australia
  Accepted: Visa/MC/Amex, Apple Pay, Google Pay, PayPal, BECS DD
  Missing: BPAY, POLi
  Note: BECS coverage is good. BPAY used for larger recurring payments.

MARKET 5: Global/Emerging Markets (India, Brazil, Mexico, Kenya, Philippines)
  Accepted: Visa/MC (cards only)
  Missing: Pix, UPI, OXXO, M-Pesa, GCash, Boleto, PSE, Maya
  Note: This is the critical gap. International aid organizations need to collect donations from the very populations they serve. Zero local APMs available.

**Key pain points documented:**
- 13% of donors abandon checkout when preferred payment method unavailable
- Adding local payment methods drives 46% lift in conversion
- PayPal billing agreement cancellations cause silent recurring plan failures
- Some countries with low-value currencies hit character limits in payment processing
- 20% of donors use PayPal, showing demand for non-card methods

**Key meeting angles:**
1. **$70M Series B, expansion mode**: Fundraise Up is investing heavily in global growth; payment coverage must match
2. **28% conversion rate can go higher**: They already 2x the industry; local APMs + smart routing pushes further
3. **International aid paradox**: Nonprofits serving India, Brazil, Kenya cannot collect donations from those populations due to missing APMs
4. **Recurring giving is the crown jewel**: Monthly donors are highest LTV; payment resilience directly impacts lifetime value
5. **1,000+ nonprofits at risk on single acquirer**: Stripe outage = donations blocked for UNICEF USA, Red Cross, Salvation Army simultaneously
6. **86% fee coverage = cost sensitivity**: Nonprofits care deeply about payment costs; smart routing optimizes processing fees across acquirers
7. **Never lost an enterprise customer**: Payment infrastructure quality is a retention lever they already value

**Sources:**
- [Fundraise Up Payment Methods (Docs)](https://fundraiseup.com/docs/payment-methods/)
- [Fundraise Up Payment Methods (Platform)](https://fundraiseup.com/platform/payment-methods/)
- [Fundraise Up Global Fundraising](https://fundraiseup.com/features/global-fundraising/)
- [Fundraise Up Currencies](https://fundraiseup.com/features/currencies/)
- [Fundraise Up Payment Methods FAQ](https://fundraiseup.com/support/payment-methods-faq/)
- [Fundraise Up Stripe Integration (Docs)](https://fundraiseup.com/docs/stripe/)
- [Fundraise Up Pricing](https://fundraiseup.com/pricing/)
- [Fundraise Up Case Studies](https://fundraiseup.com/case-studies/)
- [Fundraise Up UNICEF USA Case Study](https://fundraiseup.com/case-studies/unicef-usa/)
- [Fundraise Up Canadian Red Cross Case Study](https://fundraiseup.com/case-studies/canadian-red-cross/)
- [Stripe Partner Directory: Fundraise Up](https://stripe.partners/directory/fundraise-up)
- [Stripe Case Study: Fundraise Up](https://stripe.com/in/customers/fundraiseup)
- [AlleyWatch: Fundraise Up $70M](https://alleywatch.com/2025/02/fundraise-up-non-profit-online-donation-fundraising-platform-peter-byrnes/)
- [Fundraise Up Payment Localization Blog](https://fundraiseup.com/blog/payment-localization/)
- [Fundraise Up Nonprofit Payment Processing Blog](https://fundraiseup.com/blog/nonprofit-payment-processing-options/)
- [Fundraise Up Identity Guidelines](https://fundraiseup.com/identity-guidelines/)
- [Fundraise Up Pulse of the Donor 2026](https://fundraiseup.com/reports/pulse-of-the-donor/)
