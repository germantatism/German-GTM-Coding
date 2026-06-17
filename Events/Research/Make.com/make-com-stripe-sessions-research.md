# MAKE.COM | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Make.com
=======================================

Logo: https://images.ctfassets.net/un655fb4fvg9/1FmkSLVjgiWeyQsOgaK9q2/d6b22c38e58a18db759c7c42b8c86749/make-logo-on-light.svg
Nombre merchant: Make.com

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Europe Home Market Gap
Tittle_Pain Point_2: LatAm & Asia Blind Spot
Tittle_Pain Point_3: Single Acquirer Exposure
Tittle_Pain Point_4: Recovery Revenue at Risk
Tittle_Pain Point_5: Enterprise Billing Lag

Desc_Pain Point_1: Czech-founded company with 500K+ users in 200+ countries, yet no SEPA Direct Debit, no iDEAL, no BLIK, no Bancontact. European subscribers forced onto international card rails in a region where 60%+ prefer local methods.
Desc_Pain Point_2: Zero local APMs for Brazil (no Pix), India (no UPI), Japan (no Konbini), Mexico (no OXXO). Automation is a global category but Make's checkout is US-centric with Apple Pay, Google Pay, and Cash App Pay only.
Desc_Pain Point_3: Stripe is the sole payment processor powering all Core, Pro, and Teams subscriptions. Make recovered $1.2M with Stripe recovery tools, but any Stripe outage blocks 100% of signups and renewals with no failover.
Desc_Pain Point_4: Make publicly recovered $1.2M using Stripe's auth and recovery tools, proving significant revenue leakage from failed payments. Without multi-PSP routing, the ceiling on recovery is limited to what Stripe alone can optimize.
Desc_Pain Point_5: Enterprise invoicing handled manually through Account Managers. No self-service enterprise billing, no PO-based payment, no automated reconciliation for large accounts scaling across Celonis's enterprise customer base.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe
PSP_2: Apple Pay (via Stripe)
PSP_3: Google Pay (via Stripe)
PSP_4: Klarna (via Stripe)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: SEPA Direct Debit
Local_M_2: iDEAL
Local_M_3: BLIK
Local_M_4: Pix
Local_M_5: UPI
Local_M_6: Bancontact
Local_M_7: Konbini
Local_M_8: Boleto
Local_M_9: OXXO
Local_M_10: PayPal

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each subscription renewal to the optimal acquirer by card BIN, issuer, and geography. Make already proved $1.2M in recoverable revenue with Stripe alone. Multi-PSP Smart Routing unlocks the next tier: +3 to 10% auth uplift across 200+ countries and $52M+ revenue.
Desc_Yuno_Cap2: Automatic cascade when Stripe declines. Yuno reroutes to the next best acquirer in milliseconds, pushing recovery beyond what Stripe's built-in tools can achieve alone. Up to 50% recovery on soft declines, directly protecting Make's subscription ARR.
Desc_Yuno_Cap3: Activates the methods Make's global automation community expects: SEPA DD for the EU home market, Pix for Brazil, UPI for India, iDEAL for Netherlands, BLIK for Poland, Konbini for Japan. One API, 1,000+ methods, zero per-market engineering sprints.
Desc_Yuno_Cap4: Single dashboard replacing Make's Stripe-only plus manual enterprise invoicing stack. Real-time approval monitoring across all plans, centralized settlement, and NOVA anti-fraud reducing false declines by up to 75% across Core, Pro, Teams, and Enterprise tiers.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Make.com at a glance:**
- Founded 2012 as Integromat in Prague, Czech Republic. Rebranded to Make in 2022
- Acquired by Celonis (Munich-based process mining unicorn) in October 2020 for $100M+
- Revenue: $52.6M (2025). ~680 employees across 6 continents
- 500K+ users, 350K+ organizations, 200+ countries
- Visual no-code/low-code automation (iPaaS). Connects 3,000+ apps
- Plans: Free, Core ($10.59/mo), Pro ($18.82/mo), Teams ($29/mo), Enterprise (custom)
- Competes directly with Zapier, n8n, Workato, Power Automate
- Forbes Cloud 100 and iPaaS category leader

**Confirmed PSPs:**
- Stripe: sole payment processor (confirmed via Stripe case study: "Make Recovers $1.2 Million in Revenue with Stripe Authorization and Recovery Tools")
- Uses Stripe Billing, Optimized Checkout Suite, Stripe Elements
- Apple Pay, Google Pay, Amazon Pay, Cash App Pay: enabled via Stripe checkout
- Klarna: BNPL option via Stripe
- ACH Direct Debit: US bank accounts only
- Link: Stripe's one-click checkout
- No payment orchestrator detected

**Accepted payment methods (current):**
- Credit/debit cards (Visa, MC, Amex)
- Apple Pay, Google Pay, Amazon Pay, Cash App Pay (via Stripe)
- Link (Stripe one-click checkout)
- Klarna (installments)
- ACH Direct Debit (US only, monthly and annual subs)
- Enterprise: manual invoicing through Account Managers
- NO PayPal, NO SEPA DD, NO European local methods, NO LatAm/Asia APMs

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (~35% of users)
  Accepted: Cards, Apple Pay, Google Pay, Amazon Pay, Cash App Pay, ACH, Klarna, Link
  Missing: PayPal, Venmo (direct)
  Note: Best-served market with multiple US-centric wallets and BNPL. PayPal absence still notable.

MARKET 2: Europe / DACH + CEE (HQ region, ~30% of users)
  Accepted: Cards, Apple Pay, Google Pay
  Missing: SEPA Direct Debit, iDEAL (NL), BLIK (PL), Bancontact (BE), Sofort, Giropay
  Note: Czech-founded company with zero European payment methods. SEPA DD is the standard for EU subscription billing. BLIK is essential for Poland (Make's backyard).

MARKET 3: Brazil / Latin America (~8%)
  Accepted: Cards only (wallets may not be available by region)
  Missing: Pix, Boleto, OXXO, PSE
  Note: Pix handles 70%+ of Brazilian digital payments. Growing automation demand in LatAm has zero local payment support.

MARKET 4: India / South Asia (~5%)
  Accepted: Cards only
  Missing: UPI, RuPay, Paytm, PhonePe
  Note: 75%+ of Indian digital payments use UPI. India's developer and SMB automation market is huge but unreachable with card-only checkout.

MARKET 5: Japan / Asia Pacific (~5%)
  Accepted: Cards only
  Missing: Konbini, PayPay, JCB optimization, carrier billing
  Note: 20%+ of Japanese online payments at convenience stores. Zero APAC-specific payment support.

**Key meeting angles:**
1. **Proven revenue leakage** | Make publicly recovered $1.2M with Stripe's tools alone. Multi-PSP routing unlocks the next recovery tier beyond what one processor can optimize.
2. **European paradox** | Czech-founded, Celonis-owned (Munich), yet zero European payment methods. SEPA DD and iDEAL would immediately improve EU conversion.
3. **Celonis enterprise ambitions** | Parent company serves Fortune 500. Make's manual enterprise invoicing limits the cross-sell motion.
4. **Stripe dependency at scale** | 100% of subscription revenue routes through one PSP. At $52M+ revenue and growing, failover is a business continuity issue.
5. **Zapier competitive pressure** | Direct competitor may optimize payments first. Payment experience becomes a differentiator in a commoditizing iPaaS market.
6. **Global automation demand** | 200+ countries but US-centric payments. Local APMs unlock the long tail of international automation users.

**Sources:**
- [Stripe Case Study: Make Recovers $1.2M](https://stripe.com/en-mx/customers/make)
- [Make.com Payment Details Help Center](https://help.make.com/change-payment-details)
- [Make.com Pricing](https://www.make.com/en/pricing)
- [Make.com About Page](https://www.make.com/en/about)
- [Make.com Brand Guidelines](https://www.make.com/en/brand-guidelines.pdf)
- [GetLatka: Make Revenue](https://getlatka.com/companies/make.com)
- [Sacra: Make Revenue & Funding](https://sacra.com/c/make/)
- [CBInsights: Make Company Profile](https://www.cbinsights.com/company/make-3)
- [Celonis Wikipedia (Acquisition)](https://en.wikipedia.org/wiki/Celonis)
- [Zapier: Make.com Pricing Review](https://zapier.com/blog/make-com-pricing/)
