# SIRIUS AI | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Sirius AI
=======================================

Logo: https://cdn.brandfetch.io/siriusai.com/w/512/h/512/logo
Nombre merchant: Sirius AI

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Consulting Revenue Cycle
Tittle_Pain Point_2: Cross-Border Billing Gap
Tittle_Pain Point_3: No Platform Monetization
Tittle_Pain Point_4: Client Payment Diversity
Tittle_Pain Point_5: FX Settlement Overhead

Desc_Pain Point_1: 75+ employees across New York and Gurugram. Six-to-seven-figure consulting engagements rely on manual invoicing and wire, causing cash flow delays.
Desc_Pain Point_2: India delivery + US/UK/APAC clients = multi-currency complexity. Paying INR teams while billing USD banks creates FX overhead and settlement delays.
Desc_Pain Point_3: Hosted AI Platform lacks self-service billing. Financial services clients cannot subscribe or scale usage without manual procurement workflows.
Desc_Pain Point_4: Bank and fintech clients have strict procurement rules: some need ACH, others SEPA, wire, or PO. Manual accommodation does not scale globally.
Desc_Pain Point_5: USD billing to US clients, INR payroll in India. Without optimized FX routing, currency conversion costs erode margins on every engagement.

SLIDE 1: PSP TOPOLOGY

PSP_1: Wire Transfer (enterprise invoicing)
PSP_2: ACH (US client billing)
PSP_3: Direct invoicing (manual)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: SEPA Direct Debit (Europe)
Local_M_2: BACS Direct Debit (UK)
Local_M_3: UPI (India)
Local_M_4: ACH Direct Debit (US)
Local_M_5: iDEAL (Netherlands)
Local_M_6: Konbini (Japan)
Local_M_7: BLIK (Poland)
Local_M_8: PIX (Brazil)
Local_M_9: PayNow (Singapore)
Local_M_10: SPEI (Mexico)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each payment through the optimal processor by client geography, bank, and currency. As Sirius AI scales its Hosted Platform to 10+ countries, Smart Routing maximizes collection rates on enterprise billing.
Desc_Yuno_Cap2: When a payment fails, Yuno cascades to a backup processor in milliseconds. Up to 50% recovery on soft declines. For firms transitioning to SaaS, payment reliability protects the recurring revenue base.
Desc_Yuno_Cap3: Let clients pay via preferred local method: SEPA in Europe, BACS in UK, ACH in US, UPI in India. One API, 1,000+ methods. Removes procurement friction for banks and fintechs.
Desc_Yuno_Cap4: One dashboard for consulting invoices, platform subscriptions, cross-border payments, and vendor payouts. Real-time cash flow visibility across NY and Gurugram with centralized multi-currency reconciliation.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Sirius AI at a glance:**
- AI consulting and solutions firm for financial services ("AI-First. FS-Native. Outcome-Driven.")
- Focus verticals: Banking, Payments, Fintech, Wealth & Asset Management
- Founded: 2023 by Sanjay Ojha, Narendra Mulani, Abhinav Vij, Tommy Marshall
- Headquarters: 111 Town Square Place, Suite #1203, Jersey City, NJ 07310
- India office: Gurugram (delivery and engineering)
- Team: 75+ employees across US and India
- Funding: unfunded/bootstrapped (no disclosed external funding)
- SOC 2 Compliant, ISO Certified, ANAB Accredited
- Technology partners: AWS, Microsoft, Dun & Bradstreet, GBA

**Leadership backgrounds:**
- Sanjay Ojha (CEO): Former IBM Consulting Senior Partner, Accenture Managing Director, GE/Genpact VP
- Narendra Mulani (Chairman): Founded Accenture Analytics, board member at multiple AI firms
- Abhinav Vij (Chief Client Officer): Former IBM Consulting Partner, Accenture MD, ICICI Bank Analytics Lead
- Tommy Marshall (CRO): Former Accenture Fintech Lead, Capco Partner

**Key services:**
- Agentic AI for Operations (85% automation of customer correspondence at fintech client)
- Next Best Action (2X product uptake growth in payments)
- Suspicious Activity Reporting (80% productivity gains in SAR investigation)
- Conversational AI for Business Intelligence (95% faster BI access)
- Data Platform for Scaling AI
- Risk Modeling
- Fully Hosted AI Platform (cloud-based, self-hosted option)
- Customer Feedback Analytics

**Confirmed PSPs & billing infrastructure:**
- Manual enterprise invoicing (consulting engagements)
- Wire transfer and ACH for US client billing
- No self-service payment infrastructure detected for platform product
- No Stripe, Adyen, or payment gateway references found publicly
- No payment orchestrator detected

**Business model:**
- Consulting engagements (six to seven figure deals with financial institutions)
- Fully Hosted AI Platform (emerging SaaS/platform revenue)
- Delivery from India (Gurugram) for cost optimization

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (primary market, HQ in Jersey City)
  Currently offer: Wire transfer, ACH, manual invoicing
  Missing: Automated ACH Direct Debit, credit card for platform subscriptions
  US banks and fintechs expect automated billing for SaaS platforms, not manual invoicing.

MARKET 2: United Kingdom (major financial services market)
  Currently offer: Wire transfer, manual invoicing
  Missing: BACS Direct Debit, GBP invoicing, Open Banking
  UK financial institutions (HSBC, Barclays, Lloyds) require BACS DD for recurring vendor payments.

MARKET 3: India (delivery center, domestic fintech market)
  Currently offer: Local bank transfer (Gurugram operations)
  Missing: UPI for domestic client billing, NEFT automation
  Indian fintechs and banks increasingly expect UPI-based billing for SaaS platforms.

MARKET 4: Europe (growing financial services AI market)
  Currently offer: Wire transfer, manual invoicing
  Missing: SEPA Direct Debit, iDEAL, EUR invoicing
  European banks (Deutsche Bank, BNP Paribas, ING) require SEPA DD and local invoicing.

MARKET 5: Singapore / APAC (wealth management hub)
  Currently offer: Wire transfer, manual invoicing
  Missing: PayNow, FAST, SGD invoicing
  Singapore wealth managers and banks expect local payment rails.

**Key meeting angles:**
1. **Consulting to SaaS transition** | Sirius AI is building a Hosted AI Platform. Self-service payment infrastructure is essential for this transition from consulting revenue to recurring SaaS revenue.
2. **Financial services DNA** | Their clients ARE banks and payment companies. They understand payment complexity intimately and will appreciate Yuno's orchestration capabilities.
3. **Cross-border operations** | US billing + India delivery = constant FX management. Optimized payment routing reduces costs on every cross-border transaction.
4. **75+ and growing** | Bootstrapped with 75+ employees signals strong revenue. As they scale, manual invoicing becomes unsustainable. Payment automation is a natural next step.
5. **Accenture/IBM pedigree** | Founders come from Big 4 consulting. They understand enterprise procurement and will value a solution that meets diverse client payment requirements.
6. **Payments vertical expertise** | Sirius AI specifically serves the payments industry (80% SAR productivity gain). Yuno partnership could also become a client reference.

**Sources:**
- [Sirius AI Homepage](https://www.siriusai.com/)
- [Sirius AI Services](https://www.siriusai.com/services)
- [Sirius AI Our Team](https://www.siriusai.com/our-team)
- [Sirius AI Contact](https://www.siriusai.com/contact-us)
- [Sirius AI LinkedIn](https://www.linkedin.com/company/sirius-ai-inc)
- [Sirius AI Tracxn](https://tracxn.com/d/companies/sirius-ai/__Pbpc4J2wdHMo3aNQ93SCWBPXCSRdXDYgByXztbd-4Kg)
- [Sirius AI ZoomInfo](https://www.zoominfo.com/c/sirius-ai-inc/452160790)
- [Sirius AI Crunchbase](https://www.crunchbase.com/organization/siriusai)
