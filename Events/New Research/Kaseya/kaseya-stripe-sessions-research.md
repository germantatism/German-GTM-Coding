# KASEYA | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Kaseya
=======================================

Logo: https://cdn.brandfetch.io/kaseya.com/w/512/h/512/logo
Nombre merchant: Kaseya

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: 170-Country Billing Gap
Tittle_Pain Point_2: MSP Collection Delays
Tittle_Pain Point_3: No Failover on Renewals
Tittle_Pain Point_4: Card-Only International
Tittle_Pain Point_5: Multi-Product Bill Stack

Desc_Pain Point_1: 50,000 MSPs in 170+ countries, only cards and US ACH. Germany, Japan, India, Brazil lack SEPA, Konbini, UPI, Boleto. $1.5B+ ARR at friction risk.
Desc_Pain Point_2: ConnectBooster cuts collection to 1.4 days for MSP clients, but Kaseya's own billing relies on cards/ACH. Failed charges on $1.5B ARR = material impact.
Desc_Pain Point_3: $1.5B+ ARR across Datto, IT Glue, Unitrends, ConnectBooster. Each failed renewal is lost revenue. No cascade retries via alternative processors.
Desc_Pain Point_4: Offices in 20+ countries, customers in 170+, but international billing is card-only. Low-card markets push MSPs to competitors with local methods.
Desc_Pain Point_5: 20+ products create fragmented billing. MSPs with multi-product subs face reconciliation complexity across different payment rails and invoices.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe
PSP_2: ConnectBooster (own platform)
PSP_3: ACH Direct Debit

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: SEPA Direct Debit
Local_M_2: UPI
Local_M_3: Boleto
Local_M_4: Konbini
Local_M_5: BACS Direct Debit
Local_M_6: iDEAL
Local_M_7: BLIK
Local_M_8: Bancontact
Local_M_9: PIX
Local_M_10: Sofort

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each MSP subscription renewal to the best-performing acquirer for that card BIN, issuer, and geography. With $1.5B+ ARR across 50,000 MSPs in 170+ countries, even a 3% auth uplift on renewals protects $45M+ in annual recurring revenue from involuntary churn.
Desc_Yuno_Cap2: When Stripe declines a Kaseya 365 or Datto renewal, Yuno cascades to an alternative processor in milliseconds. Up to 50% recovery on soft declines. At $1.5B+ ARR with 20+ products, each recovered renewal protects a multi-product MSP relationship.
Desc_Yuno_Cap3: Unlock MSP billing globally: SEPA for EU, UPI for India, Boleto for Brazil, Konbini for Japan, BACS for UK. One API, 1,000+ methods. Remove procurement friction that pushes MSPs in 170+ countries toward competitors with localized billing options.
Desc_Yuno_Cap4: One dashboard for Kaseya billing across Datto, IT Glue, Unitrends, ConnectBooster, and 20+ products. Real-time approval monitoring per geography, product line, and MSP tier. Unified reconciliation replacing fragmented multi-rail billing.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Kaseya at a glance:**
- Leading global provider of AI-powered IT management and cybersecurity software
- Founded: 2000, headquartered in Miami, Florida (701 Brickell Avenue)
- Private company (IPO under consideration per S&P Global Ratings 2025 report)
- ARR: $1.5B+ as of 2025; annual revenue estimated at $5B (February 2026)
- Employees: ~5,000 (January 2026), with recent layoffs of ~450 in late 2025 to early 2026
- Serves 50,000 MSPs and IT departments in 170+ countries
- Offices in 20+ countries: US, Australia, Canada, India, Ireland, Netherlands, UK, Germany
- CEO: Rania Succar (2025, replacing Fred Voccola)
- Refinanced $4B in debt from 2022 Datto acquisition

**Product portfolio (20+ products):**
- Kaseya 365: unified platform for IT management
- Datto: backup, disaster recovery, networking (acquired 2022)
- IT Glue: documentation management
- Unitrends: backup and continuity
- ConnectBooster: MSP billing and payment automation
- Spanning Cloud Apps: SaaS backup
- RapidFire Tools: IT assessment and compliance
- Datto Autotask: PSA (professional services automation)

**ConnectBooster (Kaseya's billing product for MSPs):**
- Acquired by Kaseya, fully integrated with Kaseya BMS and Datto Autotask
- Reduces MSP collection from 60+ days to 1.4 days average
- Supports: credit cards, debit cards, ACH (US bank accounts)
- 74% of users reduce AR aging by 30+ days
- ACH discount feature to lower processing fees
- PCI-compliant customer vault for stored payment methods
- No documented international/multi-currency support

**Confirmed PSPs:**
- Stripe: integrated with Kaseya Quote Manager for credit card payments
- ConnectBooster: proprietary billing/payment platform for MSP customer billing
- ACH: supported for US bank accounts
- No payment orchestrator detected

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (HQ, largest market)
  Currently offer: Credit cards, ACH
  Missing: Apple Pay, Google Pay for quick renewals
  US MSPs expect seamless subscription management. ACH coverage is good but mobile payment options are missing.

MARKET 2: Europe (Germany, Netherlands, UK, Ireland offices)
  Currently offer: Credit cards
  Missing: SEPA Direct Debit, iDEAL, Bancontact, BACS DD, Sofort, BLIK
  35% card penetration in Germany. European MSPs strongly prefer SEPA DD for recurring IT infrastructure spend. Missing SEPA is a significant barrier.

MARKET 3: India (office presence)
  Currently offer: International credit cards (USD)
  Missing: UPI, RuPay, net banking, INR invoicing
  India has a growing MSP market. UPI processes 75%+ of digital payments. Card-only USD billing creates unnecessary friction for Indian IT service providers.

MARKET 4: Australia (office presence)
  Currently offer: Credit cards
  Missing: BPAY, PayTo, direct debit
  BPAY is the standard for Australian B2B recurring payments. Missing it means MSPs must use cards for SaaS subscriptions, adding procurement friction.

MARKET 5: Brazil/Latin America
  Currently offer: Credit cards
  Missing: Boleto, PIX, PSE
  Latin America has a growing MSP market. Boleto and PIX are essential for Brazilian IT service providers who cannot easily use international credit cards.

**Key meeting angles:**
1. **$1.5B+ ARR at risk** | Every failed subscription renewal across 20+ products is lost recurring revenue. Smart retry logic directly protects ARR at scale
2. **170+ countries, card-only** | 50,000 MSPs globally but only credit card and US ACH billing. Local methods remove procurement barriers in the majority of markets
3. **Multi-product complexity** | Datto + IT Glue + Unitrends + ConnectBooster creates fragmented billing. Orchestration unifies payment flows across the entire portfolio
4. **IPO consideration** | S&P noted Kaseya is considering an IPO. Clean, scalable payment infrastructure supports public market readiness
5. **ConnectBooster synergy** | Kaseya already operates a billing platform (ConnectBooster) for MSPs. Yuno orchestration could enhance ConnectBooster's payment routing capabilities
6. **$4B debt refinancing** | Capital efficiency matters post-refinancing. Reducing payment failures and processing costs directly improves margins

**Sources:**
- [Kaseya Official Website](https://www.kaseya.com/)
- [Kaseya Company Page](https://www.kaseya.com/company/)
- [Kaseya Brand Assets](https://www.kaseya.com/brand/)
- [Kaseya Wikipedia](https://en.wikipedia.org/wiki/Kaseya)
- [Kaseya Quote Manager Payments](https://help.quotemanager.kaseya.com/help/Content/3-manage/payments.htm)
- [ConnectBooster MSP Billing Software](https://www.kaseya.com/products/msp-billing-software/)
- [ConnectBooster Payment Methods](https://help.cb.kaseya.com/help/Content/payment-methods.htm)
- [KaseyaOne Payment Management](https://help.one.kaseya.com/help/Content/2_Features/Payment-Management.htm)
- [Kaseya ConnectBooster Integration Press Release](https://www.kaseya.com/press-release/kaseya-makes-billing-painless-for-its-msp-customers-through-connectbooster-integration/)
- [ChannelE2E: MSP Profitability 2025](https://www.channele2e.com/analysis/new-kaseya-study-profitability-is-a-top-focus-for-msps-in-2025)
- [Brandfetch: Kaseya Logo](https://brandfetch.com/kaseya.com)
- [Built In: Kaseya Growth 2026](https://builtin.com/company/kaseya/faq/stability-growth)
- [Owler: Kaseya Revenue](https://www.owler.com/company/kaseya)
