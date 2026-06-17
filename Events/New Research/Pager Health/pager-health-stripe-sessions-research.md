# PAGER HEALTH | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Pager Health
═══════════════════════════════════════

Logo: https://asset.brandfetch.io/idKq0Tso6s/idvjIrJsLG.svg
Nombre merchant: Pager Health

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Copay Collection Failure
Tittle_Pain Point_2: Single-Processor Risk
Tittle_Pain Point_3: LATAM Payment Gaps
Tittle_Pain Point_4: B2B Invoice Complexity
Tittle_Pain Point_5: No Payment Orchestration

Desc_Pain Point_1: Nearly 60% of healthcare bad debt is self-pay copays after insurance. With 26M+ members, Pager Health's platform collects patient copays through limited payment methods. No digital wallets, no pay-by-bank, no BNPL health options to reduce friction and recover revenue.
Desc_Pain Point_2: Pager Health processes patient payments and enterprise B2B invoices through undisclosed third-party processors. A single-processor architecture means any degradation impacts payment collection across 26M+ members and all enterprise clients simultaneously, with no failover.
Desc_Pain Point_3: Pager Health serves 4M+ lives in Latin America with dedicated regional leadership. Yet no local LATAM payment methods are offered: no Pix for Brazil, no SPEI/OXXO for Mexico, no PSE for Colombia. Members in the region face friction paying for virtual care services.
Desc_Pain Point_4: Enterprise clients (health plans, providers, employers) require complex B2B invoicing: multi-entity billing, PO-based procurement, net-30/60 terms, and split-payer reconciliation. Current billing infrastructure lacks the flexibility for diverse enterprise payment workflows.
Desc_Pain Point_5: No payment orchestration layer exists across Pager Health's payment flows. Patient copays, enterprise invoices, LATAM billing, and insurance reimbursements all run through disconnected systems with no unified routing, monitoring, or reconciliation dashboard.

SLIDE 1: PSP TOPOLOGY

PSP_1: Undisclosed Payment Processor(s)
PSP_2: Insurance Claims (600+ Plans)
PSP_3: Medicare/Medicaid
PSP_4: Google Cloud (AI Infrastructure)
PSP_5: Credit/Debit Cards

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: SPEI
Local_M_3: OXXO
Local_M_4: PSE (Colombia)
Local_M_5: Apple Pay
Local_M_6: Google Pay
Local_M_7: Pay by Bank (ACH Instant)
Local_M_8: HSA/FSA Card Integration
Local_M_9: CareCredit / BNPL Health
Local_M_10: Nequi

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route every patient copay and enterprise invoice to the optimal acquirer by member geography, card type, and payer mix. With 26M+ members and enterprise clients across the US and LATAM, a 3-10% auth rate improvement recovers millions in patient payments and accelerates B2B collections.
Desc_Yuno_Cap2: When the primary payment processor fails, Yuno cascades to an alternate acquirer in milliseconds. Recovers up to 50% of failed patient copays and subscription charges. For a platform serving 26M members, payment continuity is critical to care delivery and revenue integrity.
Desc_Yuno_Cap3: Unlock Pix and Boleto for 4M+ Brazilian members, SPEI and OXXO for Mexican members, Apple Pay and Google Pay for US members, and HSA/FSA integration for health-specific payments. One API, 1,000+ payment methods, enabling Pager Health's goal of reaching 100M members globally.
Desc_Yuno_Cap4: Consolidate patient copays, enterprise B2B invoices, LATAM billing, and insurance reimbursement flows into one real-time dashboard. NOVA anomaly detection (75% fraud reduction) protects across all payment channels, while unified reconciliation replaces fragmented multi-system management.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Pager Health at a glance:**
- Founded: 2014 in New York City
- CEO: Walter Jin (Chairman and CEO)
- Co-Founders: Gaspard de Dreuzy, Philip Eytan, Oscar Salazar (former Uber CTO)
- HQ: New York, New York
- Total Funding: $132.6M+ (latest: $70M in Sep 2025)
- Revenue: Estimated $25-100M (some sources cite $100-250M range)
- Members: 26M+ across US and Latin America (4M+ in LATAM)
- Employees: ~363-369 across 6 continents
- VP Latin America: Fabian Alvarez
- Key Investors: Lux Capital, Goodwater Capital, Health Catalyst Capital Management, Horizon Healthcare Services, Silicon Valley Bank
- Google Cloud Partnership: Generative AI applications for healthcare (Apr 2024)
- Protera Health Partnership: Virtual MSK care (May 2025)
- Goal: Provide care for 100M people through payer partnerships

**Platform (Pager 360 / Enterprise 360):**
- AI-powered care orchestration platform
- Nurse triage, telehealth, e-prescribing, follow-up care, customer service
- Omnichannel communication: chat, voice, video
- Agent-to-agent functionality for multi-disciplinary care teams
- Generative AI applications (built on Google Cloud): Chat Summation, FAQ Bot, Sentiment Analysis
- Member navigation platform (industry first, end-to-end)
- Covers 30+ specialties, 600+ insurance plans including Medicare and Medicaid

**Confirmed Payment Infrastructure:**
- Third-party payment processors (undisclosed in privacy policy)
- Credit/debit card acceptance for patient copays
- Insurance billing across 600+ payer plans
- B2B enterprise invoicing for health plans, providers, and employers
- No payment orchestrator detected

**Competitive Landscape:**
- Direct competitors: Innovaccer, IKS Health, WellSky, MDLive, CirrusMD, HealthTap
- Differentiation: AI-powered connected health platform (not just telehealth), Google Cloud GenAI partnership, 26M+ member scale
- Strength: Oscar Salazar co-founder (Uber CTO pedigree), Lux Capital backing, LATAM presence
- Weakness: Undisclosed payment infrastructure, no local LATAM payment methods despite 4M+ LATAM members

**Top Market Gap Analysis:**

MARKET 1: United States (primary market, 22M+ members)
  Offer: Credit/debit cards, insurance copay billing
  Missing: Apple Pay, Google Pay, Pay by Bank, HSA/FSA integration, CareCredit/BNPL
  Patient payment friction drives bad debt and member dissatisfaction

MARKET 2: Brazil (LATAM expansion)
  Offer: Unknown (likely card-only)
  Missing: Pix, Boleto Bancario
  Pix handles 45B+ transactions/year in Brazil; essential for healthcare payments

MARKET 3: Mexico (LATAM expansion)
  Offer: Unknown (likely card-only)
  Missing: SPEI, OXXO, CoDi
  60%+ unbanked population needs cash-based and instant transfer options

MARKET 4: Colombia (LATAM expansion)
  Offer: Unknown
  Missing: PSE, Nequi, Daviplata
  PSE is mandatory for online payments in Colombia

MARKET 5: Argentina (potential LATAM)
  Offer: None
  Missing: Mercado Pago, Rapipago, Pago Facil
  High inflation makes local currency billing and instant payment critical

**Key meeting angles:**
1. **26M members, undisclosed PSP**: A platform serving 26M lives cannot afford payment opacity. Orchestration adds visibility, resilience, and optimization.
2. **LATAM payment gap**: 4M+ LATAM members with no local payment methods. Pix, SPEI, OXXO, and PSE are table stakes for healthcare payments in the region.
3. **Copay recovery**: 60% of healthcare bad debt is copays. Adding Apple Pay, Google Pay, and BNPL reduces patient friction and recovers revenue at scale.
4. **100M member goal**: Pager Health targets 100M members. Payment infrastructure must scale ahead of growth, not catch up to it.
5. **Oscar Salazar (Uber CTO)**: Co-founder who built Uber's payment infrastructure understands orchestration value intimately.
6. **Google Cloud GenAI synergy**: AI-first company culture aligns with intelligent payment routing and NOVA analytics.

**Sources:**
- [Pager Health Official Website](https://www.pagerhealth.com/)
- [Pager Health About Us](https://www.pagerhealth.com/about-us)
- [Pager Health Enterprise 360](https://www.pagerhealth.com/solutions/enterprise-360)
- [Pager Health Privacy Policy](https://www.pagerhealth.com/privacy)
- [Pager Health $70M Funding](https://www.pagerhealth.com/press/pager-secures-70m-in-funding-to-drive-expansion-of-virtual-care-in-united-states-latin-america-and-worldwide-lnj2w)
- [Pager Health Google Cloud GenAI](https://www.prnewswire.com/news-releases/pager-health-unveils-new-generative-ai-applications-with-google-cloud-to-improve-payer-productivity-and-enhance-member-experiences-302106172.html)
- [Pager Health Protera Partnership](https://www.pagerhealth.com/press/pager-healthand-protera-health-team-up-to-expand-access-to-value-based-virtual-first-msk-care)
- [Pager Health Member Navigation Launch](https://www.prnewswire.com/news-releases/pager-health-sm-launches-industrys-first-end-to-end-member-navigation-platform-302481951.html)
- [Pager Health Agent-to-Agent Launch](https://www.prnewswire.com/news-releases/pager-health-launches-innovative-agent-to-agent-functionality-and-emerges-as-groundbreaking-connected-health-platform-company-on-major-rebrand-302168687.html)
- [Pager Wikipedia](https://en.wikipedia.org/wiki/Pager_(company))
- [Pager Health Crunchbase](https://www.crunchbase.com/organization/pager)
- [Pager Health Tracxn](https://tracxn.com/d/companies/pagerhealth/__IE-xGeKp3HbZNACIWLfB7CbSFZtf0iesGSf7qypn1kg)
- [Fierce Healthcare: AI Agent for Wellness](https://www.fiercehealthcare.com/ai-and-machine-learning/pager-health-rolls-out-new-ai-agent-guide-health-plan-members-through)
- [MobiHealthNews: GenAI Apps](https://www.mobihealthnews.com/news/pager-health-announces-three-new-generative-ai-apps)
