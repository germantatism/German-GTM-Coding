# SUREPOINT TECHNOLOGIES | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: SurePoint Technologies
=======================================

Logo: https://cdn.brandfetch.io/surepoint.com/w/512/h/512/theme/dark/icon.jpeg
Nombre merchant: SurePoint Technologies

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Single PSP Dependency
Tittle_Pain Point_2: IOLTA Compliance Risk
Tittle_Pain Point_3: Aged Receivables Drain
Tittle_Pain Point_4: Limited Payment Methods
Tittle_Pain Point_5: No Cross-Border Support

Desc_Pain Point_1: SurePoint relies on Payload as its sole payment processor for 100,000+ legal professionals. No failover or smart routing exists. If Payload experiences downtime or declines, law firms cannot collect client payments. A single PSP dependency on a niche legal processor limits optimization options and creates approval rate blind spots across the entire SurePoint ecosystem.
Desc_Pain Point_2: Legal payments require strict IOLTA trust account separation where processing fees must never touch trust funds. SurePoint's Payload integration handles compliance, but without payment orchestration, firms lack redundancy if compliance rules change by state or jurisdiction. 50 US states with different bar association rules, one processor handling all trust logic.
Desc_Pain Point_3: Law firms forfeit approximately 4,000 billed hours per $1M in revenue through write-offs on aged receivables. SurePoint's "Pay Now by Invoice" service helps, but limited payment options (primarily cards and ACH) reduce collection rates. Clients who prefer digital wallets, BNPL, or international payment methods cannot pay their preferred way.
Desc_Pain Point_4: SurePoint Payment Services accepts credit/debit cards, ACH, Apple Pay, and Google Pay. No PayPal, no BNPL options for large legal invoices, no international wallets. Law firms with multinational clients collecting five and six-figure invoices from Europe, Asia, and Latin America offer no local payment methods for those clients.
Desc_Pain Point_5: SurePoint mentions "international currencies" but provides no specific cross-border payment infrastructure. Mid-size US law firms increasingly serve international clients (cross-border M&A, immigration, IP) who need to pay in EUR, GBP, or local methods like SEPA, iDEAL, or wire alternatives. No multi-currency checkout or local APM support exists.

SLIDE 1: PSP TOPOLOGY

PSP_1: Payload (primary payment processor)
PSP_2: LawPay (integration partner)
PSP_3: None identified
PSP_4: None identified
PSP_5: None identified

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: PayPal
Local_M_2: SEPA Direct Debit
Local_M_3: iDEAL
Local_M_4: Klarna (BNPL)
Local_M_5: Affirm (BNPL)
Local_M_6: Wire transfer alternatives
Local_M_7: Pix
Local_M_8: Alipay
Local_M_9: Open Banking (UK)
Local_M_10: Bancontact

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Recovery
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across multiple processors for every legal invoice payment. Each transaction routed to the highest performing acquirer for that card BIN, issuer, and market. For a platform processing payments from 100,000+ legal professionals across mid-size law firms, smart routing delivers +3 to 10% auth uplift. On five and six-figure legal invoices, even 1% improvement in approval rates recovers substantial revenue.
Desc_Yuno_Cap2: Automatic cascade eliminates SurePoint's single-processor dependency on Payload. When Payload declines a transaction, Yuno reroutes to an alternative processor in milliseconds. Up to 50% recovery on soft declines via instant retry. NOVA AI recovers up to 75% of failed transactions. For law firms collecting large retainers and settlement payments, a failed transaction means delayed cash flow and client frustration.
Desc_Yuno_Cap3: Activates the payment methods SurePoint's law firm clients need for international collections: SEPA Direct Debit for European corporate clients, iDEAL for Dutch companies, Open Banking for UK clients, Pix for Brazilian entities, Alipay for Chinese corporations. BNPL options (Klarna, Affirm) enable payment plans on large legal invoices. One API, 1,000+ payment methods.
Desc_Yuno_Cap4: One dashboard providing SurePoint with real-time visibility across all payment processors. Centralized reconciliation for trust account payments, operating account collections, and retainer deposits. Millisecond anomaly detection via Monitors ensures IOLTA compliance is never compromised. Reduces aged receivables by offering clients their preferred payment method while maintaining full ABA compliance.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**SurePoint Technologies at a glance:**
- Model: Legal practice management SaaS (practice, finance, growth solutions)
- Industry: Legal Technology
- Users: 100,000+ legal professionals
- Target: Mid-size law firms
- Employees: 51-200
- Headquarters: Austin, Texas (Arboretum Plaza One, 9442 N Capital of Texas Hwy, Suite 400)
- Founded: 1982 (as Rippe & Kingston, rebranded to SurePoint in 2020)
- CEO: Eric Thurston (appointed April 2023)
- CTO: Ryan Anderson
- CFO: Tyler Zacharias
- CPO: Jamie Nawrocki
- Chief Brand Officer: Olivia Mockel
- Chief Commercial Officer: Dan Hurley
- Head of Payments: Brian DuCharme
- GM Leopard Solutions: Laura Leopard
- Total funding: $92.9M
- Investors: Aquiline Capital Partners (majority stake, June 2021), ParkerGale Capital (minority, 2018-2021)
- 40+ years in the legal industry

**Core Products (SurePoint Legal Suite, launched August 2025):**
- Practice Pro (formerly ZenCase): Front-office matter management, timekeeping, document automation
- Finance Pro: Cloud-native billing and financial management
- Finance Core (formerly Coyote Analytics): Accounting for smaller teams
- Finance Enterprise (formerly LMS): Distributed accounting for larger firms
- CRM (formerly ContactEase): Client relationship management
- Legal Insights (formerly Leopard Solutions): Competitive market intelligence
- Payment Services: Embedded payment processing via Payload
- SurePoint Pro Platform: Unified platform (launched February 2026)

**Recent Acquisitions:**
- January 2025: ZenCase (practice management, now Practice Pro)
- 2024: Leopard Solutions (competitive market intelligence, legal talent data)
- 2022: ContactEase (legal CRM)
- 2022: Coyote Analytics (legal ERP/accounting)

**Recent Developments:**
- February 2026: SurePoint Pro platform debut (unified practice + finance + intelligence)
- September 2025: Billables AI integration (AI-powered timekeeping)
- August 2025: SurePoint Legal Suite launch
- January 2025: ZenCase acquisition

**Payments Infrastructure:**
- Payload: Primary payment processor (discovered via surepointpay.com redirect to Payload checkout)
- LawPay: Integration partner (LawPay Link integration with SurePoint LMS)
- PCI-DSS Level 2 compliant
- IOLTA and ABA compliant (trust account separation)
- Payment Services branded as "SurePoint PAY" (surepointpay.com)

**Payment Methods (Current):**
- Credit/debit cards: Visa, Mastercard, Amex, Discover
- ACH / electronic checks
- Apple Pay
- Google Pay
- QR code payments
- "International currencies" (claimed but unspecified)
- No PayPal
- No BNPL options
- No European local payment methods
- No Asian payment methods

**Payload Platform Details:**
- API-first payment processor for legal platforms
- RESTful APIs with SDKs (Python, Node.js, Go, Ruby, Java, .NET)
- White-label checkout and payment forms
- IOLTA trust account separation (fees never touch trust accounts)
- PCI-DSS and SOC-2 compliant
- ACH, Same Day ACH, Real Time Payments, FedNow
- KYC/AML screening capabilities
- Fraud prevention and dispute management

**Payment Pain Points:**
1. Single PSP dependency on Payload with no failover
2. No smart routing to optimize approval rates on high-value legal invoices
3. Limited payment methods (cards and ACH primarily)
4. No BNPL for large legal invoices ($10K-$500K+)
5. No European local payment methods (SEPA, iDEAL, Open Banking)
6. No Asian payment methods (Alipay, WeChat Pay, UPI)
7. No PayPal despite being the most recognized digital wallet globally
8. International "currencies" claimed but no specific cross-border infrastructure
9. Aged receivables: firms forfeit ~4,000 billed hours per $1M revenue in write-offs
10. IOLTA compliance managed by single processor with no redundancy

**Key Meeting Angles:**
1. **100,000+ legal professionals, single PSP**: Payload is the only processor. Yuno adds failover, smart routing, and multi-PSP redundancy while maintaining IOLTA compliance
2. **High-value invoices, low payment options**: Legal invoices range from $5K to $500K+. BNPL (Klarna, Affirm) enables payment plans that increase collection rates. Firms forfeit ~4,000 billed hours per $1M in write-offs
3. **International client collections**: Mid-size firms serve cross-border M&A, immigration, and IP clients. European clients need SEPA, iDEAL. Asian clients need Alipay. Yuno enables 1,000+ APMs via single API
4. **Aquiline-backed growth**: PE-backed with $92.9M in funding and four acquisitions since 2022. Payment infrastructure must scale with the platform. InDrive achieved 90% approval across 10 markets with Yuno
5. **SurePoint Pro platform launch**: February 2026 unified platform creates a natural inflection point to upgrade payment infrastructure. Yuno integrates via single API without disrupting existing Payload flows
6. **IOLTA compliance at scale**: 50 US states, different bar association rules. Yuno's orchestration layer maintains trust account separation while routing to multiple processors. McDonald's gained +4.7% auth rate with Yuno

**Sources:**
- [SurePoint Technologies](https://surepoint.com/)
- [SurePoint Payment Services](https://surepoint.com/payment-services/)
- [SurePoint About Us](https://surepoint.com/about-us/)
- [SurePoint PAY](https://surepointpay.com/)
- [Payload for Legal Platforms](https://payload.com/articles/payload-for-legal-platforms)
- [SurePoint + LawPay Integration](https://www.lawpay.com/partners/surepoint/)
- [SurePoint Q&A Brian DuCharme](https://surepoint.com/resources/blog/a-q-and-a-about-surepoint-payment-services-with-brian-ducharme/)
- [SurePoint Aquiline Investment (PRNewswire)](https://www.prnewswire.com/news-releases/surepoint-technologies-announces-investment-from-aquiline-capital-partners-301304297.html)
- [SurePoint ZenCase Acquisition (BusinessWire)](https://www.businesswire.com/news/home/20250123781892/en/)
- [SurePoint Legal Suite Launch](https://www.leopardsolutions.com/in-the-news/surepoint-introduces-surepoint-legal-suite-uniting-leading-legal-technology-solutions/)
- [SurePoint Pro Platform](https://surepoint.com/surepoint-pro/)
- [SurePoint + Billables AI](https://www.lawnext.com/2025/09/watch-surepoint-and-billables-ai-announce-integration-to-transform-timekeeping-and-billing-for-law-firms.html)
- [Crunchbase: SurePoint](https://www.crunchbase.com/organization/rippe-kingston)
- [CB Insights: SurePoint](https://www.cbinsights.com/company/rippe-kingston)
- [Tracxn: SurePoint](https://tracxn.com/d/companies/surepoint/)
