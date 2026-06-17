# OPENLOOP | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: OpenLoop
═══════════════════════════════════════

Logo: https://asset.brandfetch.io/idGxMQSXZh/idH-3wIBq-.svg
Nombre merchant: OpenLoop

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Single Payment Processor
Tittle_Pain Point_2: Copay Collection Friction
Tittle_Pain Point_3: No Local Methods Abroad
Tittle_Pain Point_4: RCM Revenue Leakage
Tittle_Pain Point_5: White-Label Payment Gaps

Desc_Pain Point_1: OpenLoop relies on a single payment processor for all patient and client billing across 170+ organizations. With $502M+ in revenue and 3M+ patient visits annually, any processor downtime or degradation cascades across the entire white-label network with no failover.
Desc_Pain Point_2: Copay collection in telehealth is notoriously difficult. Nearly 60% of bad debt is self-pay copays after insurance. OpenLoop's platform handles payments but lacks dynamic payment method options like pay-by-bank, digital wallets, or BNPL that reduce patient payment friction.
Desc_Pain Point_3: OpenLoop operates across all 50 US states and is expanding into international telehealth. No local payment methods exist for cross-border patient billing: no SEPA for European patients, no Pix for Brazil, no UPI for India, limiting global virtual care delivery.
Desc_Pain Point_4: With 600+ insurance plans (including Medicare and Medicaid), claim denials and delayed reimbursements create revenue cycle gaps. No intelligent routing exists to optimize which payment rail (insurance claim vs. patient self-pay) collects fastest per visit type.
Desc_Pain Point_5: OpenLoop white-labels its platform to 170+ organizations. Each client needs customized payment flows, but the current infrastructure offers limited flexibility to configure payment methods, currencies, and checkout experiences per white-label instance.

SLIDE 1: PSP TOPOLOGY

PSP_1: Undisclosed Payment Processor
PSP_2: Insurance Claims (600+ Plans)
PSP_3: Medicare/Medicaid
PSP_4: Credit/Debit Cards
PSP_5: BlueJeans by Verizon (Tech Partner)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Apple Pay
Local_M_2: Google Pay
Local_M_3: Pay by Bank (ACH Instant)
Local_M_4: HSA/FSA Card Integration
Local_M_5: CareCredit / BNPL Health
Local_M_6: Pix
Local_M_7: SEPA Direct Debit
Local_M_8: UPI
Local_M_9: PayPal
Local_M_10: Interac (Canada)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route every patient payment and B2B client invoice to the optimal acquirer based on transaction type, card BIN, and payer mix. With $502M+ revenue across 170+ white-label clients and 3M+ annual visits, a 3-10% auth rate uplift recovers millions in patient copays and subscription fees.
Desc_Yuno_Cap2: When the primary payment processor fails, Yuno cascades to an alternate acquirer in milliseconds. Recovers up to 50% of failed transactions. For a platform powering 170+ healthcare organizations, processor downtime cannot mean system-wide payment outages.
Desc_Yuno_Cap3: Add Apple Pay, Google Pay, Pay by Bank, and HSA/FSA integration to reduce patient payment friction. For international expansion, unlock Pix in Brazil, SEPA in Europe, and UPI in India. One API, 1,000+ payment methods, zero per-market engineering effort.
Desc_Yuno_Cap4: Consolidate all payment processors, insurance billing, and white-label client payment flows into one dashboard. NOVA anomaly detection (75% fraud reduction) flags suspicious transactions across 170+ client instances, while real-time monitoring replaces fragmented per-client payment management.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**OpenLoop at a glance:**
- Founded: 2019 in Des Moines, Iowa
- CEO: Dr. Jon Lensing, MD (Co-Founder, rural Iowa native, University of Iowa grad)
- COO: Christian Williams (Co-Founder)
- HQ: Des Moines, Iowa (OpenLoop Tower, downtown headquarters)
- Total Funding: $120M+ raised
- Valuation: $1B+ (unicorn status)
- Revenue: $502.4M
- Patients: 3M+ annually
- Clinician Network: 20,000+ across all 50 states, 30+ specialties, 15+ languages
- Active Clients: 170+ organizations
- Employees: 414 (255% team growth in 2025)
- NCQA Certified
- Named to TIME's list of World's Top HealthTech Companies (2025)
- Recent M&A: Acquired Season Health (food-as-medicine startup, April 2026)
- Key Investors: Panoramic Ventures, ManchesterStory Group, Highland Capital Partners, SpringTide Ventures, Oak HC/FT, Primetime Partners, UnityPoint Health Ventures, Portage Ventures, Greg Brockman (OpenAI co-founder)

**Confirmed Payment Infrastructure:**
- Undisclosed primary payment processor (privacy policy references "third-party payment processors" without naming them)
- Credit/debit card acceptance for patient payments
- Insurance billing across 600+ payer plans including Medicare and Medicaid
- Revenue Cycle Management (RCM) as a service offering
- Platform includes built-in payments alongside scheduling, ePrescribing, and SOAP notes
- No payment orchestrator detected

**Platform Capabilities:**
- White-label EHR/EMR system
- Synchronous and asynchronous telehealth
- API-driven platform with easy integrations
- Booking and payments
- ePrescribing and eLabs
- Note charting and clinician management
- Usage reporting and analytics
- AI-enabled workflow tools
- Payer Coverage + RCM service

**Key Healthcare Payment Challenges:**
- Nearly 60% of bad debt is self-pay copays after insurance (industry-wide)
- Payer policies are not standardized; each insurer sets its own rules
- In-office copay collection processes become complicated in telehealth
- Payment processing failures cause patient drop-off during virtual visit checkouts
- Multiple billing streams (insurance claims, patient self-pay, B2B client invoices) fragment reconciliation

**Competitive Landscape:**
- Competitors: Wheel, Bicycle Health, Iris Telehealth, SteadyMD
- Differentiation: Full-stack white-label (not just clinician marketplace), NCQA certification, 50-state coverage
- Strength: Scale (170+ clients, 20K+ clinicians, $502M revenue, unicorn valuation)
- Weakness: Payment infrastructure opacity, single-processor dependency, limited international payment support

**Key meeting angles:**
1. **Unicorn scale, undisclosed payments**: $502M revenue and $1B+ valuation running on an unnamed single payment processor. The payment infrastructure needs to match the company's scale.
2. **White-label payment customization**: 170+ organizations each need flexible payment flows. Orchestration enables per-client payment method configuration without engineering effort.
3. **Copay recovery**: 60% of healthcare bad debt is uncollected copays. Adding Apple Pay, Google Pay, and Pay by Bank reduces patient friction and recovers revenue.
4. **International expansion enabler**: As telehealth goes global, OpenLoop needs local payment rails in each market. One API integration versus per-country builds.
5. **Season Health synergy**: The nutrition therapy acquisition adds subscription-based meal programs that need recurring payment optimization and smart routing.
6. **Greg Brockman invested**: OpenAI's co-founder backing signals AI-first infrastructure thinking. Payment orchestration with AI-driven routing aligns with their technology DNA.

**Sources:**
- [OpenLoop Official Website](https://openloophealth.com/)
- [OpenLoop Technology Platform](https://openloophealth.com/technology-platform)
- [OpenLoop Team Page](https://openloophealth.com/team)
- [OpenLoop 2025 Year in Review](https://openloophealth.com/blog/openloops-2025-end-of-year-recap)
- [OpenLoop CEO 2026 Predictions](https://openloophealth.com/blog/openloop-ceo-predicts-whats-next-for-digital-health-in-2026)
- [OpenLoop $15M Series A](https://openloophealth.com/news/openloop-raises-15-million-series-a)
- [OpenLoop Season Health Acquisition](https://endpoints.news/openloop-health-has-acquired-nutrition-startup-season-health/)
- [OpenLoop NCQA Certification](https://openloophealth.com/news/openloop-receives-ncqa-certification)
- [OpenLoop BlueJeans Partnership](https://openloophealth.com/news/openloop-health-partners-with-bluejeans-by-verizon)
- [OpenLoop Privacy Policy](https://openloophealth.com/website-privacy-policy)
- [SpringTide: How OpenLoop Powers Telehealth](https://www.springtide.com/company-highlights/how-openloop-is-powering-the-future-of-telehealth)
- [Jon Lensing: Building a $1B Telehealth Company](https://alejandrocremades.com/jon-lensing/)
- [OpenLoop Crunchbase](https://www.crunchbase.com/organization/openloop)
- [OpenLoop Tracxn](https://tracxn.com/d/companies/openloop/__9Y2fUdcsUd3v7UZmbAeNPjM-1gjpRdJzkXgr6GsHlmY)
- [Brandfetch: OpenLoop Logo](https://brandfetch.com/openloophealth.com)
- [Luqra: Telehealth Payment Friction](https://www.luqra.com/blog/reducing-friction-patient-billing-telehealth/)
- [OpenLoop Tower HQ](https://www.businessrecord.com/openloop-healths-downtown-headquarters-renamed-openloop-tower/)
