# RIPPLING | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Rippling
═══════════════════════════════════════

Logo: https://rippling2.imgix.net/wordmark-1320.svg
Nombre merchant: Rippling

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Single PSP Lock-In
Tittle_Pain Point_2: Global Billing Gaps
Tittle_Pain Point_3: Auth Rate Erosion
Tittle_Pain Point_4: No Failover Layer
Tittle_Pain Point_5: FX Revenue Leakage

Desc_Pain Point_1: Stripe is the sole payment processor handling all subscription billing across US, Canada, UK, and Australia. Zero acquirer redundancy means every Stripe incident blocks 100% of new sign-ups and renewals.
Desc_Pain Point_2: Rippling operates in 100+ countries but accepts only card payments via Stripe. No local APMs in LATAM, APAC, or EMEA markets where card penetration remains below 40%.
Desc_Pain Point_3: Cross-border card transactions from 80+ EOR countries route through US-based Stripe accounts. International cards see higher decline rates from issuer blocks on foreign merchants.
Desc_Pain Point_4: With Stripe as the only acquirer, any outage or rate spike has no automatic cascade path. Failed renewals from 20,000+ customers have no retry route through an alternate processor.
Desc_Pain Point_5: $570M+ ARR billed in USD across global markets. Customers in Brazil, India, UK, and Australia absorb FX markups, increasing churn risk on a per-employee monthly billing model.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe
PSP_2: Plaid (bank connectivity)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: UPI
Local_M_3: SEPA Direct Debit
Local_M_4: BACS Direct Debit
Local_M_5: Boleto
Local_M_6: OXXO
Local_M_7: iDEAL
Local_M_8: Bancontact
Local_M_9: PayNow
Local_M_10: BLIK

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each subscription renewal to the highest-performing acquirer by card BIN, issuer, and country. With $570M+ ARR from 20,000+ companies across 100+ countries, even a 3% auth uplift recovers $17M+ in annual revenue without adding a single new customer.
Desc_Yuno_Cap2: Automatic cascade removes Rippling's single Stripe dependency. When Stripe declines a renewal, Yuno reroutes to the next best acquirer in milliseconds, recovering failed transactions with zero customer friction. Up to 50% recovery on soft declines.
Desc_Yuno_Cap3: Activates the APMs Rippling's global customers need: SEPA DD across Europe, BACS DD in the UK, Pix in Brazil, UPI in India, iDEAL in the Netherlands, BLIK in Poland. One API, 1,000+ payment methods. No engineering sprints per market.
Desc_Yuno_Cap4: One dashboard consolidating Stripe billing across US, CA, GB, and AU into a single view. Real-time approval rate monitoring, centralized reconciliation, millisecond anomaly detection. Full visibility across every processor and currency.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Rippling at a glance:**
- Unified HR, IT, and Finance platform for workforce management
- $570M+ ARR (2025), growing 30%+ YoY
- Valuation: $16.8B (Series G, May 2025); secondary market implies $20.8B (Dec 2025)
- 20,000+ customers, 15,000+ startups on the platform
- 2,000+ employees across San Francisco (HQ), Dublin (EMEA HQ), Sydney (APAC), Bengaluru
- EOR in 80 countries, HRIS localized in 100+ countries, global payroll in 10 countries
- CEO: Parker Conrad (co-founder). No near-term IPO plans; targeting 2027+
- Key products: Payroll, HRIS, IT Management, Spend Management, Bill Pay, Corporate Cards

**Confirmed PSPs:**
- Stripe: primary billing processor (confirmed via live publishable keys for US, CA, GB, AU in app config)
- Stripe Issuing: used for corporate card program
- Plaid: bank account connectivity layer
- No payment orchestrator detected
- No secondary card acquirer identified

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (core market, ~80% of customers)
  Accepted: Visa/MC/Amex via Stripe, ACH (for Bill Pay outbound)
  Missing: ACH for inbound subscription billing, Cash App Pay
  Note: US market well served but no acquirer redundancy

MARKET 2: United Kingdom (EMEA HQ in Dublin, dedicated Stripe billing key)
  Accepted: Visa/MC via Stripe (GBP pricing)
  Missing: BACS Direct Debit, Open Banking payments
  Note: UK B2B SaaS billing heavily relies on Direct Debit for recurring payments

MARKET 3: Australia (dedicated Stripe billing key, APAC HQ in Sydney)
  Accepted: Visa/MC via Stripe (AUD pricing)
  Missing: BECS Direct Debit, PayTo, POLi
  Note: Australian businesses prefer direct debit for recurring SaaS subscriptions

MARKET 4: Brazil (EOR market, payroll in BRL since Jan 2026)
  Accepted: Cards via Stripe (likely USD cross-border)
  Missing: Pix, Boleto, local installment cards
  Note: Pix handles 70%+ of digital payments in Brazil

MARKET 5: India (1,000+ Rippling employees, major EOR market)
  Accepted: Cards via Stripe (likely USD cross-border)
  Missing: UPI, RuPay, Net Banking, Paytm
  Note: 75%+ of Indian digital payments use UPI. B2B adoption growing rapidly

**Key meeting angles:**
1. **Per-employee billing model** | Monthly recurring charges across 20,000+ companies means even tiny auth improvements yield massive revenue recovery
2. **Global expansion vs. single PSP** | Operating in 100+ countries but billing through one processor creates compounding friction
3. **B2B Direct Debit opportunity** | Enterprise customers in UK, EU, Australia expect Direct Debit for SaaS subscriptions
4. **Stripe Issuing dependency** | Rippling's corporate card product runs on Stripe Issuing, deepening single-vendor risk
5. **Competitor pressure** | Deel ($12B valuation) and Gusto are aggressive on global payments; payment reliability is a differentiator
6. **Pre-IPO infrastructure** | No near-term IPO, but $570M ARR company will face underwriter scrutiny on payment resilience

**Sources:**
- [Rippling Privacy / App Config (Stripe keys confirmed)](https://app.rippling.com/legal/privacy)
- [Rippling Pricing Page](https://www.rippling.com/pricing)
- [Rippling Global Payroll](https://www.rippling.com/global-payroll-and-hiring)
- [Rippling EOR in 80 Countries](https://www.rippling.com/blog/eor-updates-march)
- [CNBC: Rippling $16.8B Valuation](https://www.cnbc.com/2025/05/09/rippling-valued-at-16point8-billion-in-450-million-funding-round.html)
- [TechCrunch: Rippling Series G, 20K+ Customers](https://techcrunch.com/2025/05/09/rippling-raises-450m-at-a-16-8b-valuation-reveals-yc-is-a-customer/)
- [Sacra: Rippling Revenue Analysis](https://sacra.com/c/rippling/)
- [ARR Club: Rippling $570M ARR](https://www.arr.club/signal/rippling-arr-hits-570m)
- [Contrary Research: Rippling Breakdown](https://research.contrary.com/company/rippling)
- [Rippling Blog: Stripe Alternatives](https://www.rippling.com/blog/stripe-alternatives)
- [Rippling Bill Pay](https://www.rippling.com/bill-pay)
- [Forge: Rippling IPO Outlook](https://forgeglobal.com/rippling_ipo/)
