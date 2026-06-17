# ZAPIER | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Zapier
=======================================

Logo: https://cdn.zapier.com/zapier/images/logos/zapier-logo.svg
Nombre merchant: Zapier

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: PayPal Backup Mandate
Tittle_Pain Point_2: Europe Local Method Gap
Tittle_Pain Point_3: Single Processor Lock-In
Tittle_Pain Point_4: LatAm & Asia Blind Spot
Tittle_Pain Point_5: High-Value Churn Leak

Desc_Pain Point_1: PayPal accepted but requires a backup bank or card. This two-step friction adds abandonment risk at checkout. For a $400M+ revenue platform with 3M+ users, every extra step in the payment flow costs conversions.
Desc_Pain Point_2: No SEPA Direct Debit, no iDEAL, no BLIK, no Bancontact for European subscribers. Bank transfer available but manual. 3M+ global users forced through card or PayPal in markets where 60%+ prefer local recurring methods.
Desc_Pain Point_3: Stripe is the primary processor. Zapier reported a 4% auth uplift and $3M in recovered revenue after switching to Stripe, but remains locked into a single acquirer with no failover for $400M+ in subscription revenue.
Desc_Pain Point_4: Zero local APMs for Brazil (no Pix), India (no UPI), Japan (no Konbini), Mexico (no OXXO). Automation demand is global but Zapier's checkout is limited to cards, PayPal, and bank transfers.
Desc_Pain Point_5: With $400M+ revenue and 100K+ paying customers, involuntary churn from failed card renewals at scale represents tens of millions in annual leakage. 3D Secure friction adds another decline vector in regulated markets.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe
PSP_2: PayPal
PSP_3: Bank Transfer (manual)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: SEPA Direct Debit
Local_M_2: iDEAL
Local_M_3: Pix
Local_M_4: UPI
Local_M_5: BLIK
Local_M_6: Bancontact
Local_M_7: Konbini
Local_M_8: Boleto
Local_M_9: OXXO
Local_M_10: GCash

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each subscription renewal to the optimal acquirer by card BIN, issuer, and geography. Zapier already proved 4% auth uplift with Stripe alone. Multi-PSP routing unlocks the next tier: +3 to 10% additional uplift on $400M+ revenue translates to $12M+ recovered annually.
Desc_Yuno_Cap2: Automatic cascade when Stripe declines. Yuno reroutes to the next best acquirer in milliseconds, pushing recovery beyond what a single PSP can optimize. Up to 50% recovery on soft declines that currently churn 100K+ paying subscribers.
Desc_Yuno_Cap3: Activates methods Zapier's global automation community expects: SEPA DD for Europe, Pix for Brazil, UPI for India, iDEAL for Netherlands, BLIK for Poland, Konbini for Japan. One API, 1,000+ payment methods, zero per-market engineering sprints.
Desc_Yuno_Cap4: Single dashboard unifying Stripe plus PayPal plus manual bank transfer settlement into one reconciliation stream. Real-time approval monitoring across Free, Professional, Team, and Enterprise tiers, with NOVA anti-fraud reducing false declines by up to 75%.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Zapier at a glance:**
- Founded 2011, HQ San Francisco (100% remote since founding). CEO: Wade Foster (co-founder)
- Revenue: $310M (2024), projected $400M+ (2025/2026), 37% CAGR
- Valuation: ~$5B (latest secondary sale)
- 3M+ total users, 100K+ paying customers
- 1,433 employees across 40 countries, 17 time zones (fully remote)
- 8,000+ app integrations, 25M+ Zaps created, 81B+ tasks automated
- Raised only $2.68M total (extreme capital efficiency: 100x ARR/funding ratio)
- Plans: Free, Professional ($19.99/mo), Team ($69/mo), Enterprise (custom)
- iPaaS market leader, competing with Make.com, n8n, Workato, Power Automate

**Confirmed PSPs:**
- Stripe: primary processor (confirmed via Stripe case study: "4% uplift in authorization rates and an extra $3M in revenue" after switching to Stripe in 2021)
- PayPal: secondary (accepted, but requires backup bank/card as funding source)
- Bank Transfer: available (manual process)
- 3D Secure: supported for fraud prevention on card payments
- No payment orchestrator detected

**Accepted payment methods (current):**
- Credit/debit cards (Visa, MC, Amex, likely Discover)
- PayPal (with mandatory backup bank/card)
- Bank transfers (manual)
- NO Apple Pay, NO Google Pay, NO local APMs
- NO SEPA DD, NO Pix, NO UPI, NO Konbini

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (~40% of users)
  Accepted: Cards, PayPal, bank transfer
  Missing: ACH (direct debit), Apple Pay, Google Pay, Cash App Pay
  Note: Core market decently served. Missing modern wallet options that competitors like Make.com already offer.

MARKET 2: Europe / UK (~25% of users)
  Accepted: Cards, PayPal, bank transfer (manual)
  Missing: SEPA Direct Debit, iDEAL (NL), BLIK (PL), Bancontact (BE), Sofort, Open Banking
  Note: Major European user base with zero local payment rails. Manual bank transfers are not a scalable recurring method.

MARKET 3: India (~5%)
  Accepted: Cards, PayPal
  Missing: UPI, RuPay, Paytm, PhonePe
  Note: 75%+ of Indian digital payments use UPI. Growing SMB and developer automation demand has no local payment support.

MARKET 4: Brazil / Latin America (~5%)
  Accepted: Cards, PayPal
  Missing: Pix, Boleto, OXXO, PSE
  Note: Pix handles 70%+ of Brazilian digital payments. Zero LatAm-specific payment support.

MARKET 5: Japan / Asia Pacific (~5%)
  Accepted: Cards, PayPal
  Missing: Konbini, PayPay, JCB optimization, carrier billing
  Note: 20%+ of Japanese online payments at convenience stores. No APAC payment support.

**Key meeting angles:**
1. **Proven auth leakage** | Zapier already documented 4% uplift and $3M recovery with Stripe alone. Multi-PSP routing unlocks the next optimization tier that single-PSP can never reach.
2. **$5B valuation at risk** | At this scale and valuation, single-PSP dependency is a board-level risk. Failover is table stakes for a $400M+ revenue platform.
3. **Make.com competitive gap** | Direct competitor Make.com already offers Apple Pay, Google Pay, Amazon Pay, Cash App Pay, Klarna, and ACH. Zapier's payment stack is falling behind.
4. **European blind spot** | ~25% of users in Europe with zero local payment methods. SEPA DD and iDEAL are standard for European SaaS subscriptions.
5. **Capital efficiency story** | Zapier built to $400M+ on $2.68M raised. Payment optimization is the highest-leverage revenue lever with zero CAC cost.
6. **Enterprise billing gap** | Enterprise tier is custom-priced but billing is still cards/PayPal. Enterprise buyers expect ACH, wire, PO-based invoicing.

**Sources:**
- [Stripe Case Study: Zapier](https://stripe.com/customers/zapier)
- [Zapier Help: How to Pay](https://help.zapier.com/hc/en-us/articles/8496292353037-How-to-pay-for-your-Zapier-account)
- [Zapier Billing Help Center](https://help.zapier.com/hc/en-us/sections/14037087245837-Billing)
- [Zapier Pricing](https://zapier.com/pricing)
- [Zapier Press/Newsroom](https://zapier.com/press)
- [Zapier Brand Assets](https://community.zapier.com/show-tell-5/zapier-brand-assets-13956)
- [Sacra: Zapier Revenue & Valuation](https://sacra.com/c/zapier/)
- [GetLatka: Zapier $310M Revenue](https://getlatka.com/companies/zapier)
- [Fueler: Zapier Statistics 2026](https://fueler.io/blog/zapier-usage-revenue-valuation-growth-statistics)
- [ElectroIQ: Zapier Statistics 2025](https://electroiq.com/stats/zapier-statistics/)
- [SQ Magazine: Zapier Statistics 2026](https://sqmagazine.co.uk/zapier-statistics/)
- [Zapier Wikipedia](https://en.wikipedia.org/wiki/Zapier)
- [Zapier Community: Payment Methods](https://community.zapier.com/how-do-i-3/can-zapier-manage-other-modes-of-payment-aside-from-credit-card-payment-via-stripe-21120)
