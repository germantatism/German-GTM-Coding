# REMOTE | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Remote
=======================================

Logo: https://asset.brandfetch.io/idR3duQxYl/idVWz1BPFG.svg
Nombre merchant: Remote

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Cross-Border FX Costs
Tittle_Pain Point_2: Multi-Rail Complexity
Tittle_Pain Point_3: Payment Speed Variance
Tittle_Pain Point_4: Billing Method Limits
Tittle_Pain Point_5: Compliance Fragmentation

Desc_Pain Point_1: Remote disburses salaries in 70+ currencies across 80+ countries. Each cross-border transfer incurs FX conversion costs. Non-local currency payroll adds $50/month per employee surcharge. Optimizing FX routing could save millions annually.
Desc_Pain Point_2: Remote operates licensed payment entities in Europe (DNB), UK (FCA), and Canada (FINTRAC) plus third-party providers globally. Managing multiple payment rails across jurisdictions creates reconciliation overhead for 400K+ business customers.
Desc_Pain Point_3: Payroll settlement times vary wildly by country and payment method. SWIFT transfers are slow and expensive. Some countries mandate local bank account disbursement. Employees in emerging markets wait days longer than those in mature banking systems.
Desc_Pain Point_4: Customer billing accepts SEPA, ACH, BACS, and cards, but cards carry a 3.5% surcharge. No local payment methods like Pix, UPI, or KakaoPay for customers in LATAM, India, or Asia paying their Remote invoices.
Desc_Pain Point_5: Each country requires different payroll tax withholding, social contributions, and statutory payments in local currency using government-mandated exchange rates. A single payment error triggers compliance violations in that jurisdiction.

SLIDE 1: PSP TOPOLOGY

PSP_1: RPS Europe BV (DNB-regulated, EU payments)
PSP_2: RPS UK Ltd (FCA-regulated, UK payments)
PSP_3: RPS Canada (Bank of Canada, FINTRAC-registered)
PSP_4: Third-party payment providers (global payroll)
PSP_5: ACH / SEPA / BACS (customer billing)
PSP_6: Credit/Debit Cards (customer billing, 3.5% surcharge)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix (Brazil)
Local_M_2: UPI (India)
Local_M_3: KakaoPay (South Korea)
Local_M_4: PayPay (Japan)
Local_M_5: OXXO (Mexico)
Local_M_6: Boleto (Brazil)
Local_M_7: GiroPay (Germany)
Local_M_8: Bancontact (Belgium)
Local_M_9: BLIK (Poland)
Local_M_10: Naver Pay (South Korea)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each payroll disbursement and customer invoice to the lowest-cost rail by currency and geography. For a platform processing salaries in 70+ currencies across 80+ countries, optimizing FX routing on every transaction recovers millions in conversion costs annually.
Desc_Yuno_Cap2: Automatic cascade across multiple payment providers. When one rail fails, Yuno reroutes in milliseconds to an alternative. Payroll never misses a deadline. Up to 50% recovery on failed transactions, ensuring 400K+ businesses always pay employees on time.
Desc_Yuno_Cap3: Activates the local payment methods customers need to pay Remote invoices: Pix in Brazil, UPI in India, KakaoPay in Korea, PayPay in Japan, OXXO in Mexico, Boleto in Brazil. One API, 1,000+ methods, eliminating the 3.5% card surcharge for global clients.
Desc_Yuno_Cap4: One dashboard unifying RPS Europe, RPS UK, RPS Canada, and third-party providers. Real-time monitoring across EOR, contractor, and payroll billing. NOVA fraud engine with 75% fewer false positives. Centralized analytics for all 80+ country payment flows.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Remote at a glance:**
- Founded: 2019 by Job van der Voort (CEO, ex-VP Product at GitLab) and Marcelo Lebre (CTO)
- Headquarters: Amsterdam, Netherlands (fully remote company)
- Employees: ~1,500+ (14,569 reported by Tracxn including EOR-managed workforce)
- Funding: $506M total raised
  - Series B: $150M (July 2021, $1B+ valuation)
  - Series C: $300M (April 2022, $3B valuation)
  - Investors: Accel, Sequoia Capital, Index Ventures, Two Sigma Ventures, General Catalyst
- Revenue: $100M+ ARR (surpassed in 2025)
- Customers: 400,000+ businesses
- Countries: 80+ with owned legal entities; 170+ total coverage
- Currencies: 70+ supported for payroll disbursement

**Products:**
- Employer of Record (EOR): $599/month per employee (80+ countries, owned entities)
- Contractor Management: $29/month per contractor (localized contracts, IP protection)
- Global Payroll: $29/month per employee (70+ countries)
- Contractor of Record: Legal responsibility management (launched Jan 2025)
- Remote HR Management (HRIS): Free plan available
- Remote Payment Services (RPS): Licensed payment infrastructure
- Expense Management: Acquired Atlas (January 2026)
- Recent acquisition: Bravas (April 2026)

**Confirmed PSPs / Payment Rails:**
- RPS Europe BV: DNB-regulated payment services provider (EU)
- RPS UK Ltd: FCA-regulated payment services provider (UK)
- RPS Canada: Bank of Canada registered, FINTRAC MSB (Canada)
- Third-party payment providers: Global payroll disbursement
- ACH Direct Debit: U.S. customer billing
- SEPA Direct Debit: European customer billing
- BACS Direct Debit: UK customer billing
- Credit/Debit Cards: Customer billing (3.5% surcharge)
- Bank Wire Transfer: Customer invoices
- No payment orchestrator detected

**Customer Billing Methods:**
- SEPA Direct Debit (EU): Auto-pay supported
- ACH Direct Debit (US): Auto-pay supported
- BACS Direct Debit (UK): Auto-pay supported
- Credit/Debit Cards: Manual trigger, 3.5% surcharge
- Bank Transfer: Manual payment

**Key Payment Challenges:**
- FX conversion costs: 70+ currencies, each cross-border transfer incurs conversion fees
- Non-local currency surcharge: $50/month per employee for non-local salary arrangements
- SWIFT payment slowness: International wire transfers are expensive and slow
- Card surcharge: 3.5% added cost for card-paying customers
- Multi-entity reconciliation: Licensed entities in EU, UK, Canada plus third-party providers
- Settlement time variance: Days-long delays in emerging markets vs. instant in mature systems
- Compliance complexity: Each country's payroll taxes use government-mandated exchange rates

**Competitive Landscape:**
- Deel: Largest competitor, 150+ countries, modular pricing, AI-powered
- Oyster HR: 180+ countries, emphasis on employee experience
- Papaya Global: 160+ countries, fintech-focused payroll
- Velocity Global (Pebl): AI-powered, rebranded Sept 2025
- Rippling: Wider HR/IT/finance stack with EOR module
- Globalization Partners (G-P): Enterprise EOR pioneer

**Key Meeting Angles:**
1. **$506M raised, 70+ currency payroll** | Every FX conversion costs money. Smart routing to optimal payment rails per currency could save millions across 400K+ business customers.
2. **3.5% card surcharge** | Customers paying Remote invoices via card pay a significant premium. Local APMs (Pix, UPI, SEPA) eliminate this surcharge entirely.
3. **Licensed multi-entity payment structure** | RPS Europe, UK, and Canada plus third-party providers create reconciliation complexity. Unified orchestration simplifies into one dashboard.
4. **80+ countries, variable settlement speed** | Employees in emerging markets wait days for salary. Instant local rails (Pix, UPI) deliver same-day payroll in critical markets.
5. **$100M+ ARR, rapid acquisition pace** | Atlas (Jan 2026) and Bravas (Apr 2026) acquisitions add payment complexity. Orchestration unifies payment flows across any acquired entity.
6. **Competitor pressure from Deel** | Deel's AI-powered platform is the primary threat. Superior payment infrastructure (faster, cheaper, more methods) is a competitive differentiator.

**Sources:**
- [Remote Official Website](https://remote.com)
- [Remote About Page](https://remote.com/about)
- [Remote Global Payroll Payments](https://remote.com/global-hr/payroll-payments)
- [Remote Payment Methods (Help Center)](https://support.remote.com/hc/en-us/articles/4407227515405-What-payment-methods-are-available)
- [Remote Invoice Payment (Help Center)](https://support.remote.com/hc/en-us/articles/4411287893901-How-to-pay-your-invoice)
- [Remote Payment Processing (Help Center)](https://support.remote.com/hc/en-us/articles/35946254925709-How-does-Remote-process-payments-through-the-Payroll-Payments-Service)
- [Remote Payment Services RPS (Help Center)](https://support.remote.com/hc/en-us/articles/41961147728525-Get-started-with-Remote-Payment-Services-RPS)
- [Remote Non-Local Currency Payments](https://support.remote.com/hc/en-us/articles/4549153424781-In-what-countries-are-non-local-currency-salary-payments-offered)
- [Remote $300M Series C (TechCrunch)](https://techcrunch.com/2022/04/05/remote-payroll-hr-workforce-3-billion/)
- [Remote $150M Series B (TechCrunch)](https://techcrunch.com/2021/07/13/remote-raises-150m-on-a-1b-valuation-to-manage-payroll-and-more-for-organizations-global-workforces/)
- [Remote Pricing 2026 (WhichPayroll)](https://whichpayroll.com/pricing/remote)
- [Remote Pricing 2026 (HireInSouth)](https://www.hireinsouth.com/post/remote-pricing)
- [Remote vs Deel (Remote Blog)](https://remote.com/blog/payroll/deel-vs-remote)
- [Remote Contrary Research](https://research.contrary.com/company/remote)
- [Remote Tracxn Profile](https://tracxn.com/d/companies/remote/__G9a_iB-tkLD4i6M27U3GsIb3i0WSL6B872-d51NWz1Y)
- [Remote Brandfetch Logo](https://brandfetch.com/remote.com)
- [Job van der Voort (Mercury Blog)](https://mercury.com/blog/job-van-der-voort-built-remote-global-employment)
