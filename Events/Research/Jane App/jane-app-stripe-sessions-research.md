# JANE APP | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Jane App
═══════════════════════════════════════

Logo: https://asset.brandfetch.io/idaPQBs64k/idvQ18zcdg.svg
Nombre merchant: Jane App

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Single PSP Lock-In
Tittle_Pain Point_2: Card-Only Patient Checkout
Tittle_Pain Point_3: Cross-Border Decline Wall
Tittle_Pain Point_4: No Payment Failover
Tittle_Pain Point_5: Chargeback Blind Spot

Desc_Pain Point_1: 100% of payment volume routes through Stripe with zero acquirer diversification. 50,000 clinics on a single processor means any Stripe outage or rate increase impacts the entire platform with no alternative path.
Desc_Pain Point_2: Jane Payments only accepts credit/debit cards plus Apple Pay and Google Pay. No PayPal, no SEPA, no Pix, no bank transfers for patients. UK clinics lack terminal support, limiting in-person collection options.
Desc_Pain Point_3: International patients visiting North American clinics face cross-border card declines. Users report trying multiple cards from different countries without success. 3D Secure friction adds another dropout layer.
Desc_Pain Point_4: When a patient card declines, there is no cascade or retry through a second processor. The clinic must manually request a different card or chase payment offline, increasing no-show revenue loss.
Desc_Pain Point_5: Clinics absorb fraud losses with no advanced fraud scoring. One documented case: practitioner defrauded of $880 with no platform protection. Jane submits dispute docs but offers no proactive prevention.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe Express (Canada and US clinic billing)
PSP_2: Stripe Standard (UK and international clinic billing)
PSP_3: Stripe (Clinic Financing / Capital product)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: PayPal
Local_M_2: SEPA Direct Debit
Local_M_3: iDEAL
Local_M_4: Pix
Local_M_5: Boleto
Local_M_6: BLIK
Local_M_7: Bancontact
Local_M_8: Interac Online
Local_M_9: OXXO
Local_M_10: Klarna

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each clinic transaction by card BIN, issuer country, and patient geography. With ~$100M ARR flowing through 50,000 clinics, optimizing per-market routing delivers 3-10% auth uplift. Even a 3% gain on card-present and card-not-present volume translates to millions in recovered revenue for the platform.
Desc_Yuno_Cap2: Automatic cascade when Stripe declines a patient card. Instead of asking the patient for another card or chasing payment offline, Yuno retries through the next best processor in milliseconds. Up to 50% recovery on failed transactions reduces no-show revenue leakage and involuntary churn on memberships.
Desc_Yuno_Cap3: Activate methods Jane's global patient base needs: PayPal across markets, SEPA DD for UK/EU clinics, iDEAL in Netherlands, BLIK in Poland, Pix in Brazil, Klarna for patient installments, Interac Online in Canada. One API, 1,000+ methods. No per-market engineering sprints required.
Desc_Yuno_Cap4: One dashboard unifying Stripe Express (North America), Stripe Standard (international), and Clinic Financing into a single view. Real-time approval monitoring per country, centralized reconciliation across 50,000 clinics, and NOVA fraud detection (75% reduction) protecting practitioners from chargeback losses.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Jane App at a glance:**
- Founded: 2012 (as a side project). HQ: North Vancouver, British Columbia, Canada
- Founders: Alison Taylor and Trevor Johnston
- Valuation: $1.8B (2025 secondary financing round)
- Total funding: Less than $10M in primary capital raised
- Secondary rounds: $100M at $600M valuation (2021); $500M at $1.8B valuation (2025)
- Secondary investors: TCV, JMI Equity, Tidemark Management
- Revenue: ~$100M ARR (confirmed "centaur" status)
- Practitioners: 200,000+ across 50,000+ clinics
- Countries: Canada, United States, United Kingdom, Australia
- Employees: 550
- Profitable from the outset; 80% of new business from referrals (2023)
- Data centers: USA, Canada, UK, Australia
- Pricing: Base ($54/mo), Essential ($79/mo), Complete ($99/mo) per practitioner
- AI Scribe launched in 2025 for real-time charting
- Health and wellness verticals: physiotherapy, chiropractic, psychology, massage therapy, naturopathy, counseling, occupational therapy, speech therapy, and more

**Confirmed Payment Stack:**
- Stripe Express: Primary PSP for Canada and US clinics
- Stripe Standard: International clinics (UK and other Stripe-supported countries)
- Stripe Capital: Clinic Financing product (US only)
- Jane Payments Terminal: Available in Canada and US; NOT available in UK
- Interac Debit: Canada only, terminal-only
- Apple Pay / Google Pay: Digital wallets via Stripe
- Accepted cards: Visa, Mastercard, Amex, Discover, Diners Club, UnionPay
- No PayPal, no SEPA, no bank transfers for patients
- No payment orchestrator detected
- No multi-acquirer setup; 100% through Stripe

**Processing Fees:**
- Canada Online: 2.75% per transaction
- Canada Terminal: 2.50% + $0.10 (Interac)
- US Online: 2.85% + $0.25 per transaction
- US Terminal: 2.6% + $0.10 per transaction
- UK Online/Terminal: 1.5% + 0.20 GBP per transaction

**Payment Method Gaps (Evidence):**
- PayPal: Not accepted. Patients cannot pay via PayPal for appointments or memberships.
- Bank transfers: Not supported as a patient payment method
- SEPA DD: Not available for UK/EU patients despite being the standard for recurring health payments in Europe
- Klarna/BNPL: No installment options for patients facing high out-of-pocket costs
- Interac Online: Only terminal Interac debit in Canada; no online Interac option
- HSA/FSA cards: May experience restrictions through Jane Payments

**Top 5 Markets Gap Analysis:**

MARKET 1: Canada (largest market, home base)
  Accepted: Visa/MC/Amex/Discover/UnionPay, Apple Pay, Google Pay, Interac Debit (terminal)
  Missing: PayPal, Interac Online, Interac e-Transfer, Klarna
  Note: 80%+ of clinics are Canadian. Interac is Canada's dominant debit network but only works on terminal.

MARKET 2: United States (growth market)
  Accepted: Visa/MC/Amex/Discover/UnionPay, Apple Pay, Google Pay
  Missing: PayPal, Venmo, HSA/FSA optimization, CareCredit integration, Klarna, Affirm
  Note: US insurance billing is a known pain point. 60% of patients use Medicare or private insurance.

MARKET 3: United Kingdom (expansion market)
  Accepted: Visa/MC/Amex/Discover/UnionPay (online only, no terminal)
  Missing: PayPal, Open Banking, SEPA DD, Klarna, Apple Pay (terminal), Google Pay (terminal)
  Note: UK clinics cannot use Jane Payments Terminal. Limited to online card payments only.

MARKET 4: Australia (expansion market)
  Accepted: Visa/MC/Amex/Discover/UnionPay
  Missing: PayPal, BPAY, POLi, Afterpay, Zip Pay
  Note: BPAY and POLi are dominant bill payment methods in Australia. Afterpay widely used for health services.

MARKET 5: Europe / International (future expansion)
  Accepted: Cross-border card processing via Stripe Standard
  Missing: iDEAL (Netherlands), SEPA DD, Bancontact (Belgium), Giropay (Germany), BLIK (Poland)
  Note: Jane has regional data centers but limited payment method coverage outside core markets.

**Key meeting angles:**
1. **$100M ARR on a single PSP** | Zero acquirer diversification across 50,000 clinics creates systemic platform risk
2. **Card-only checkout in healthcare** | Patients increasingly expect PayPal, BNPL, and local methods for out-of-pocket health expenses
3. **UK market crippled** | No terminal support, no local methods. UK clinics are second-class citizens on the platform.
4. **Chargeback vulnerability** | No fraud scoring, no proactive prevention. Practitioners absorb losses on disputed transactions.
5. **Cross-border patient declines** | International patients visiting North American clinics face card failures with no fallback
6. **Membership/recurring billing risk** | When a patient card declines on membership renewal, there is no retry cascade. Silent churn.
7. **Competitor pressure** | Mindbody, Cliniko, WellnessLiving, and SimplePractice all expanding payment capabilities

**Sources:**
- [Jane Payments Features](https://jane.app/features/jane-payments)
- [Jane Payments FAQ](https://jane.app/guide/jane-payments-faq)
- [Jane: Understanding Payment Processing Fees](https://jane.app/blog/understanding-your-payment-processing-fees)
- [Jane: Setting Up Jane Payments](https://jane.app/guide/step-1-setting-up-jane-payments)
- [Jane: Multiple Payment Methods](https://jane.app/guide/multiple-payment-methods)
- [Jane: Chargebacks & Disputes](https://jane.app/guide/chargebacks-payment-disputes)
- [Jane: Failed Payouts](https://jane.app/guide/failed-jane-payments-payouts)
- [Jane: Why Did My Client's Card Decline](https://jane.app/guide/why-did-my-client-s-card-decline)
- [Jane: Memberships FAQ](https://jane.app/guide/memberships-faq)
- [Jane: Brand Assets](https://jane.app/guide/jane-s-brand-assets)
- [Jane: Pricing](https://jane.app/pricing)
- [Jane: About](https://jane.app/about)
- [Jane: Our Story](https://jane.app/story)
- [Stripe Customer Story: Jane](https://stripe.com/customers/jane-trevor-johnston)
- [Stripe Partner Directory: Jane](https://stripe.partners/directory/jane)
- [Jane: Clinic Financing by Stripe](https://jane.app/guide/clinic-financing-by-stripe)
- [Techcouver: Jane Software $1.8B Valuation](https://techcouver.com/2025/05/26/jane-software-hits-billion-valuation-secondary-deal/)
- [BetaKit: Jane App Centaur Status](https://betakit.com/jane-app-co-founder-reveals-companys-centaur-status-at-betakit-town-hall-vancouver/)
- [Silicon Valley Invest Club: Jane $500M Secondary](https://investclub.sv/2025/05/27/jane-software-to-raise-500-million-at-a-1-8-billion-valuation/)
- [GetLatka: Jane App Revenue](https://getlatka.com/companies/janeapp)
- [Growjo: Jane App Revenue](https://growjo.com/company/Jane.App)
- [WellnessLiving: Why Jane Clients Are Switching](https://www.wellnessliving.com/blog/find-out-why-jane-app-clients-are-switching-software/)
- [Helcim: Reduce Jane Payment Processing Fees](https://www.helcim.com/guides/reduce-jane-payment-processing-fees/)
- [Capterra: Jane Reviews](https://www.capterra.com/p/178984/Jane-App/reviews/)
- [Brandfetch: Jane App Logo](https://brandfetch.com/jane.app)
