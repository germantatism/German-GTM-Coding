# AMPLITUDE | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Amplitude
═══════════════════════════════════════

Logo: https://cdn.brandfetch.io/amplitude.com/w/512/h/512/logo
Nombre merchant: Amplitude

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Credit Card Only Billing
Tittle_Pain Point_2: Global Enterprise Gap
Tittle_Pain Point_3: No Failover on Renewals
Tittle_Pain Point_4: FX Settlement Overhead
Tittle_Pain Point_5: Involuntary Churn Risk

Desc_Pain Point_1: Amplitude accepts only credit cards for its Plus plans. Enterprise clients in India (8.2% of customers), Germany, and Japan cannot pay via UPI, SEPA, or Konbini, creating friction for the 698 accounts paying $100K+ ARR.
Desc_Pain Point_2: 42% of Amplitude's customer base is outside the US, spanning UK, India, APAC, and Europe. Yet billing infrastructure offers zero local payment methods, forcing international enterprise buyers through USD card rails.
Desc_Pain Point_3: With $366M ARR and auto-renewing annual contracts, a single acquirer decline on renewal day means lost enterprise accounts. No documented cascade or retry logic exists to recover failed subscription charges.
Desc_Pain Point_4: Amplitude bills in USD globally. Enterprise customers in EUR, GBP, INR, and JPY markets absorb FX conversion costs on every invoice. This adds procurement friction and makes competitors with local billing more attractive.
Desc_Pain Point_5: SaaS involuntary churn from failed card payments averages 3-5% of MRR. On $366M ARR, even 1% involuntary churn equals $3.7M in recoverable revenue through smarter retry logic and payment routing.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe
PSP_2: Credit Card (direct)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: SEPA Direct Debit
Local_M_2: UPI
Local_M_3: iDEAL
Local_M_4: Konbini
Local_M_5: BLIK
Local_M_6: Boleto
Local_M_7: ACH Direct Debit
Local_M_8: Wire Transfer / Invoice
Local_M_9: Bancontact
Local_M_10: Sofort

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each enterprise renewal to the best-performing acquirer for that card BIN, issuer, and geography. With $366M ARR across 4,800 customers in 30+ countries, even a 3% auth uplift on renewals recovers $11M+ in otherwise lost annual recurring revenue.
Desc_Yuno_Cap2: Automatic retry cascades across multiple acquirers protect Amplitude's high-value renewal cycle. When Stripe declines an annual contract charge, Yuno reroutes in milliseconds to a backup processor. Up to 50% recovery on soft declines, directly reducing involuntary churn.
Desc_Yuno_Cap3: Unlock enterprise billing across Amplitude's global footprint: SEPA Direct Debit for EU, UPI for India (8.2% of customers), Konbini for Japan, ACH for US enterprises, Boleto for Brazil. One API, 1,000+ methods, zero engineering sprints per market.
Desc_Yuno_Cap4: One dashboard consolidating Amplitude's subscription billing across all processors and payment methods. Real-time approval monitoring per geography and plan tier, centralized reconciliation, cohort-level churn analytics tied to payment failures.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Amplitude at a glance:**
- AI-powered digital analytics platform for product intelligence
- Revenue: $366M ARR as of Q4 2025 (17% YoY growth)
- Public company: NASDAQ: AMPL
- ~4,800 paying customers; 698 customers at $100K+ ARR (18% YoY growth)
- 27% of Fortune 100 are Amplitude customers (Ford, Burger King, Gap, etc.)
- Enterprise and multi-product customers = 74% of total ARR
- 700+ employees across US, UK, France, Singapore
- Founded 2012, headquartered San Francisco
- Plans: Starter (free), Plus ($49/mo), Growth, Enterprise (custom)
- Growth plan starts at ~$49K/year

**Geographic customer distribution:**
- United States: 57.8% (13,313 customers)
- India: 8.2% (1,892 customers)
- United Kingdom: 8.1% (1,855 customers)
- Rest of world: 25.9% across Europe, APAC, LATAM

**Confirmed PSPs:**
- Stripe: confirmed via privacy policy reference to Stripe for payment processing and billing
- Stripe Dashboard integration exists (tracks payment metrics within Amplitude product)
- Credit card only for self-serve plans
- Enterprise plans: likely invoice/wire for large contracts
- No payment orchestrator detected

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (57.8% of customers)
  Currently offer: Visa/MC/Amex (credit card)
  Missing: ACH Direct Debit, wire transfer automation
  US enterprises strongly prefer ACH for SaaS billing. $100K+ contracts paid by card create unnecessary procurement friction.

MARKET 2: India (8.2% of customers)
  Currently offer: International credit cards (USD billing)
  Missing: UPI, RuPay, net banking, INR invoicing
  UPI processes 75%+ of Indian digital payments. Forcing USD card payments on Indian enterprises adds cost and complexity.

MARKET 3: United Kingdom (8.1% of customers)
  Currently offer: Visa/MC/Amex (credit card)
  Missing: BACS Direct Debit, Open Banking, GBP invoicing
  BACS DD is the standard for UK B2B SaaS subscriptions.

MARKET 4: Germany / DACH
  Currently offer: Visa/MC/Amex (credit card)
  Missing: SEPA Direct Debit, Sofort, invoice payment
  ~35% card penetration. German enterprises strongly prefer SEPA DD or invoice for recurring SaaS spend.

MARKET 5: Japan
  Currently offer: Visa/MC/Amex (credit card)
  Missing: Konbini, bank transfer (furikomi), JCB optimization
  Japanese enterprise procurement often requires local bank transfer or Konbini for payment.

**Key meeting angles:**
1. **$366M ARR at risk** | Every failed renewal = lost annual contract. Smart retry logic directly protects ARR
2. **42% international customers** | Zero local payment methods despite nearly half of revenue coming from outside the US
3. **Enterprise-heavy mix** | 74% of ARR from enterprise; these buyers have strict procurement/payment requirements
4. **India = 8.2% of base** | Second-largest market with zero local payment infrastructure
5. **Involuntary churn** | Industry average 3-5% of MRR lost to payment failures. On $366M ARR, this is a $11-18M annual problem
6. **Competitive pressure** | Competitors like Mixpanel, Heap, and Google Analytics offer localized billing, creating switching incentive

**Sources:**
- [Amplitude Q4 FY2025 Results](https://investors.amplitude.com/news-releases/news-release-details/amplitude-announces-fourth-quarter-and-fiscal-year-2025)
- [Amplitude Privacy Notice](https://amplitude.com/privacy)
- [Amplitude Pricing](https://amplitude.com/pricing)
- [Amplitude Plus Plan Billing FAQ](https://gethelp.amplitude.com/hc/en-us/articles/34807172360603-FAQ-Plus-Plan-Billing)
- [Amplitude Company Page](https://amplitude.com/company)
- [Amplitude Customers](https://amplitude.com/customers)
- [Amplitude Press Kit / Brand](https://brand.amplitude.com/press-kit)
- [Brandfetch: Amplitude Logo](https://brandfetch.com/amplitude.com)
- [Amplitude Revenue (Stock Analysis)](https://stockanalysis.com/stocks/ampl/revenue/)
- [Amplitude Revenue (MacroTrends)](https://www.macrotrends.net/stocks/charts/AMPL/amplitude/revenue)
- [6Sense: Amplitude Market Share](https://6sense.com/tech/analytics/amplitude-market-share)
- [ElectroIQ: Amplitude Statistics](https://electroiq.com/stats/amplitude-statistics/)
