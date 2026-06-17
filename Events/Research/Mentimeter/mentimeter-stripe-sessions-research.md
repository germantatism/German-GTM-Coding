# MENTIMETER | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Mentimeter
═══════════════════════════════════════

Logo: https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Mentimeter_Logo.png/600px-Mentimeter_Logo.png
Nombre merchant: Mentimeter

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Single Stripe Dependency
Tittle_Pain Point_2: Card-Only Checkout
Tittle_Pain Point_3: Zero Local APMs
Tittle_Pain Point_4: USD-Only Billing
Tittle_Pain Point_5: Enterprise Renewal Risk

Desc_Pain Point_1: Stripe is the sole processor with zero failover. Any disruption blocks subscriptions for 280M+ users and 80,000 paying customers across 100+ countries.
Desc_Pain Point_2: Only credit cards accepted. No PayPal, no wallets, no bank transfers, no BNPL. A platform used by 95% of Fortune 500 with a single payment method.
Desc_Pain Point_3: 100+ countries, zero local APMs. No SEPA DD for EU universities, no UPI for India, no Pix for Brazil, no Swish in the home market of Sweden. Cards only.
Desc_Pain Point_4: All subs charged in USD only. EU, Asian, and LATAM customers absorb FX at their bank, raising effective cost and triggering cross-border card declines.
Desc_Pain Point_5: Enterprise accounts (45% YoY growth) renew annually. Each declined corporate card risks losing a multi-seat deal with no cascade retry to recover it.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (sole processor)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: SEPA Direct Debit
Local_M_2: iDEAL
Local_M_3: UPI
Local_M_4: Pix
Local_M_5: BLIK
Local_M_6: Bancontact
Local_M_7: Swish
Local_M_8: OXXO
Local_M_9: Konbini
Local_M_10: GCash

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each subscription purchase to the highest-performing acquirer for that card BIN, issuer, and country. With $38M+ revenue, 80,000 customers, and 45% YoY enterprise growth across 100+ countries, a 3% auth uplift directly recovers significant ARR that currently declines.
Desc_Yuno_Cap2: Automatic cascade eliminates Mentimeter's single-Stripe risk. When an annual enterprise renewal declines, Yuno retries through alternate processors in milliseconds. Converts hard renewal failures into recovered multi-seat contracts. Up to 50% recovery on soft declines.
Desc_Yuno_Cap3: Activate SEPA DD for European universities and enterprises, Swish for Sweden (home market), iDEAL for Netherlands, UPI for India, Pix for Brazil, BLIK for Poland, Konbini for Japan. One API, 1,000+ methods. Global teams pay natively.
Desc_Yuno_Cap4: One dashboard providing real-time approval rates by geography and plan type. Centralized reconciliation for individual, team, and enterprise subscriptions. Anomaly detection catches auth rate drops before they impact renewal cycles.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Mentimeter at a glance:**
- Private company; HQ: Stockholm, Sweden (Tulegatan 11, 113 86)
- Founded: 2012
- Revenue: $38M (2024)
- 80,000 paying customers; 280M+ total users across 100+ countries
- 350 employees (95 sales reps, 79 engineers, 23 marketers)
- Total funding: $42.9M
- 45% YoY growth in enterprise accounts
- 95% of Fortune 500 are customers; majority of world's leading universities
- 8% global interactive presentation market share (behind Poll Everywhere 12%, Microsoft Teams 20%)
- Employees across 5 continents (Europe, North America, Oceania)
- Plans: Free (limited), Basic ($11.99/mo), Pro ($24.99/mo), Enterprise (custom, 10+ licenses)
- Education pricing: Basic ($8.99/mo), Pro ($14.99/mo)

**Confirmed PSPs:**
- Stripe: sole payment processor (confirmed in payment security documentation)
- Previously mentioned Braintree in older documentation, but current docs confirm Stripe only
- No PayPal option available
- No payment orchestrator detected
- No multi-acquirer failover; complete single-processor dependency

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (largest enterprise market)
  Accepted: Credit cards (via Stripe)
  Missing: ACH, PayPal, Apple Pay, Google Pay, Cash App Pay
  Note: 95% of Fortune 500 as customers but only credit cards accepted. Enterprise procurement often prefers ACH or virtual cards.

MARKET 2: Sweden (home market, HQ)
  Accepted: Credit cards (via Stripe)
  Missing: Swish, Bankgirot, Klarna
  Note: Swish has 8.5M+ users in Sweden (85% penetration). A Swedish company not accepting Swish is a notable gap.

MARKET 3: United Kingdom/Europe (major university + enterprise market)
  Accepted: Credit cards (via Stripe)
  Missing: SEPA Direct Debit, iDEAL (NL), Open Banking, Bancontact (BE), Sofort (DE), BLIK (PL)
  Note: SEPA DD is the standard for European SaaS subscriptions. Universities often require Direct Debit for procurement.

MARKET 4: India (large educator and enterprise market)
  Accepted: Credit cards (cross-border, USD)
  Missing: UPI, RuPay, NetBanking, Paytm
  Note: 75%+ of Indian digital payments use UPI. Educators and corporate trainers need local payment options.

MARKET 5: Brazil (growing education tech market)
  Accepted: Credit cards (cross-border, USD)
  Missing: Pix, Boleto, local installments
  Note: Pix handles 70%+ of Brazilian digital payments. Brazilian universities and enterprises increasingly adopt SaaS tools.

**Key payment challenges:**
- Single PSP (Stripe only) with absolutely no fallback processor
- Card-only checkout in 2026 is extremely limiting for a SaaS platform with 280M+ users
- USD-only billing in 100+ countries means every non-US customer pays a hidden FX premium
- No PayPal even as a secondary option (unusual for any SaaS at this scale)
- Swedish HQ but no Swish support is a credibility gap in their home market
- Enterprise annual renewals on single processor create concentrated renewal risk
- Trustpilot rating of 2.7/5 with complaints about refund policies and billing practices

**Key meeting angles:**
1. **Swedish company, no Swish**: not supporting the #1 payment method in your own home market signals payment infrastructure underinvestment
2. **95% of Fortune 500**: enterprise customers expect procurement-friendly payment options (ACH, SEPA DD, virtual cards)
3. **45% enterprise growth**: rapidly growing enterprise base increases renewal concentration risk on single Stripe
4. **University procurement**: universities across EU require SEPA DD and invoice workflows; card-only blocks institutional deals
5. **280M users, 1 payment method**: the gap between user reach and payment coverage is extreme
6. **Competitor benchmark**: Slido (Cisco) supports enterprise billing; Poll Everywhere accepts PayPal and invoicing; Kahoot accepts multiple methods

**Sources:**
- [Mentimeter Payment Security](https://help.mentimeter.com/en/articles/410617-payment-security)
- [Mentimeter Privacy Policy](https://www.mentimeter.com/trust/legal/privacy-policy)
- [Mentimeter Terms](https://www.mentimeter.com/trust/legal/terms)
- [Mentimeter Security Policy](https://www.mentimeter.com/trust/legal/security-policy)
- [Mentimeter Pricing](https://www.mentimeter.com/plans)
- [Mentimeter Enterprise](https://www.mentimeter.com/enterprise)
- [Mentimeter University Buyers Guide](https://www.mentimeter.com/campaigns/university-buyers-guide)
- [Mentimeter Wikipedia](https://en.wikipedia.org/wiki/Mentimeter)
- [Mentimeter Revenue & Customers (Latka)](https://getlatka.com/companies/mentimeter)
- [Mentimeter Crunchbase](https://www.crunchbase.com/organization/mentimeter)
- [Mentimeter Product Strategy (NextSprints)](https://nextsprints.com/guide/mentimeter-product-strategy-guide)
- [Mentimeter Review (Wooclap)](https://www.wooclap.com/en/blog/mentimeter-review/)
- [Mentimeter Pricing Analysis (Vendr)](https://www.vendr.com/buyer-guides/mentimeter)
- [Mentimeter LeadIQ Profile](https://leadiq.com/c/mentimeter/5a1da8bb2300005e009cb570)
- [Mentimeter G2 Reviews](https://www.g2.com/products/mentimeter/reviews)
- [Mentimeter Investor Page](https://www.mentimeter.com/investors)
