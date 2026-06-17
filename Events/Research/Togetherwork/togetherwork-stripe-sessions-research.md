# TOGETHERWORK | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Togetherwork
=======================================

Logo: https://brandfetch.com/togetherwork.com
Nombre merchant: Togetherwork

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Legacy Processor Sprawl
Tittle_Pain Point_2: Cross-Product Silos
Tittle_Pain Point_3: US-Only Payment Rails
Tittle_Pain Point_4: Dues Collection Friction
Tittle_Pain Point_5: Fraud Across Verticals

Desc_Pain Point_1: Togetherwork consolidated 20+ legacy payment processors into Stripe, but the migration is phased and ongoing. Some product lines still run on legacy processors with separate dashboards, reconciliation, and merchant risk management, creating operational overhead across the portfolio.
Desc_Pain Point_2: 16+ acquired companies across associations, camps, pet care, Greek life, faith, sports, and municipalities. Each product line (OmegaFi, Fonteva, CommunityPass, Protech) integrated Stripe independently with different architectures, limiting cross-portfolio payment optimization.
Desc_Pain Point_3: Togetherpay and Stripe integration focuses on US domestic payments. As Togetherwork expands internationally (Fonteva serves associations globally, SCA compliance mentioned), the platform lacks local payment methods for European, LatAm, and APAC members paying dues and fees.
Desc_Pain Point_4: OmegaFi has collected $6.8B in dues, rent, and fees across hundreds of Greek chapters. Declined card payments on recurring dues create collection gaps for fraternities and sororities. Single-processor retry limits recovery options for failed membership charges.
Desc_Pain Point_5: 9+ verticals (associations, camps, pet care, faith, Greek, municipalities, nonprofits, studios, wellness) each have different fraud profiles. A single Stripe integration cannot optimize fraud rules per vertical, risking either too many false declines or insufficient protection.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (primary, consolidated from 20+ legacy processors, Stripe Connect platform)
PSP_2: Togetherpay (internal payment platform built on Stripe for cross-portfolio payments)
PSP_3: Legacy processors (remaining product lines not yet migrated)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: SEPA Direct Debit
Local_M_2: iDEAL
Local_M_3: Bancontact
Local_M_4: BLIK
Local_M_5: Pix
Local_M_6: OXXO
Local_M_7: UPI
Local_M_8: BECS Direct Debit
Local_M_9: GrabPay
Local_M_10: Konbini

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Recovery
Tittle_Yuno_Cap3: Global Payment Methods
Tittle_Yuno_Cap4: Vertical-Aware Intelligence

Desc_Yuno_Cap1: Per-transaction routing optimizes every dues payment, camp registration, and membership renewal across Togetherwork's entire portfolio. With $6.8B+ in lifetime collections through OmegaFi alone, even 3% auth uplift on recurring charges recovers significant revenue from failed dues across all verticals.
Desc_Yuno_Cap2: Automatic cascade across acquirers breaks single-Stripe dependency for 16+ product lines. When Stripe declines a fraternity dues charge or camp registration payment, Yuno reroutes to the next best acquirer in milliseconds. Up to 50% recovery on failed transactions across all verticals.
Desc_Yuno_Cap3: One API activates 1,000+ local payment methods for Togetherwork's international association members: SEPA DD for European associations, iDEAL for Dutch members, BECS for Australian chapters, Pix for Brazil. No per-market integration. Global members pay dues using their preferred local methods.
Desc_Yuno_Cap4: NOVA intelligence delivers vertical-specific fraud optimization across Togetherwork's 9+ segments. Different risk profiles for Greek dues, camp registrations, pet care bookings, and association events. 75% faster fraud detection with rules calibrated per vertical, reducing false declines without increasing exposure.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Togetherwork at a glance:**
- Founded: 2015
- CEO: Neil Platt (previously built CashEdge, sold to Fiserv for $465M; former CRO of Payoneer)
- Headquarters: Austin, TX (1221 S Congress Ave, Suite 300); previously New York/Atlanta
- Employees: 700+, with 250 new jobs planned in Austin innovation center
- Revenue: ~$145M annually
- Ownership: GI Partners (acquired March 2018 from Aquiline Capital Partners)
- Funding: $74.6M raised (Series B July 2024) from GI Partners, Park Square Capital, Golub Capital
- Acquisitions: 16 completed, including Fonteva, Protech, OmegaFi, PetExec, Gingr, Revelation Pets, Doubleknot, CircuiTree, CommunityPass
- Key brands: OmegaFi (Greek life), Fonteva (Salesforce AMS), Protech (Dynamics 365 AMS), CommunityPass (municipalities), DanceStudio-Pro
- Verticals: Associations, camps, Greek life, faith, pet care, municipalities, nonprofits, studios/wellness, sports

**Confirmed payment stack:**
- Stripe: Primary processor (consolidated from 20+ legacy processors, Stripe Connect platform, Stripe professional services engagement)
- Togetherpay: Internal payment platform built on Stripe infrastructure, used across Togetherwork operating companies
- Stripe Banking-as-a-Service: OmegaFi uses Financial Accounts and Issuing for fraternity/sorority cards and accounts
- Legacy processors: Some product lines still in migration
- SCA compliance mentioned for international transactions
- No payment orchestrator detected

**Payment scale and metrics:**
- OmegaFi: $6.8B lifetime dues, rent, and fees collected; $511M in payments processed
- Fonteva: 350+ client organizations
- Pet care portfolio: 7,000+ customers across PetExec, Gingr, Revelation Pets
- Hundreds of Greek chapters using OmegaFi for dues collection

**Payment challenges identified:**
- 20+ legacy processors being consolidated into Stripe in phased approach, not yet complete
- Each acquired company integrated Stripe with different architectures
- International payment methods missing despite global association membership
- Single-processor dependency for recurring dues collection across all verticals
- 9+ verticals with different fraud profiles running through one Stripe integration
- Greek dues collection heavily card-dependent, declined cards create chapter funding gaps
- Phased migration means some products still on legacy processors with separate reconciliation

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (primary market, all verticals)
  Accepted: Visa/MC/Amex via Stripe, ACH, Apple Pay, Google Pay
  Missing: Cash App Pay, Venmo
  Well-covered for domestic. ACH handles recurring dues effectively.

MARKET 2: Europe (Fonteva global associations, SCA compliance)
  Accepted: International cards via Stripe
  Missing: SEPA Direct Debit, iDEAL, Bancontact, BLIK, Giropay
  European association members need SEPA DD for recurring dues. SCA compliance adds card friction.

MARKET 3: Australia (Fonteva/association members)
  Accepted: International cards via Stripe
  Missing: BECS Direct Debit, PayTo, POLi
  BECS DD standard for Australian recurring payments. Association chapters need local rails.

MARKET 4: Canada (association/camp/Greek chapters)
  Accepted: Cards via Stripe
  Missing: Interac e-Transfer, Interac Online
  Canadian chapters need Interac for domestic dues collection.

MARKET 5: Latin America (emerging association market)
  Accepted: International cards via Stripe
  Missing: Pix, Boleto, OXXO, SPEI, PSE
  Growing association presence in LatAm requires local payment support.

**Key meeting angles:**
1. **Payment CEO** | Neil Platt built CashEdge (sold to Fiserv $465M) and was CRO at Payoneer; deeply understands payment infrastructure
2. **20+ processor consolidation** | Already invested in unifying payments; orchestration is the logical next layer on top of Stripe
3. **$6.8B in dues collected** | OmegaFi's scale proves recurring payment volume is massive; smart routing and failover directly impact collections
4. **16 acquired companies** | Each acquisition adds payment complexity; orchestration normalizes across the entire portfolio
5. **Multi-vertical fraud challenge** | Greek dues, camp registrations, pet bookings, and association events need different fraud rules
6. **International expansion** | Fonteva serves global associations but payment infrastructure is US-centric
7. **GI Partners PE backing** | Portfolio company with growth mandate; payment optimization directly impacts EBITDA

**Sources:**
- [Stripe Customer Story: Togetherwork](https://stripe.com/customers/togetherwork)
- [Togetherwork Homepage](https://www.togetherwork.com/)
- [Togetherwork Associations Solutions](https://www.togetherwork.com/vertical-solutions/associations/)
- [GI Partners: Togetherwork Portfolio](https://www.gipartners.com/private-equity/portfolio/togetherwork)
- [Togetherwork Acquired by GI Partners](https://www.prnewswire.com/news-releases/togetherwork-acquired-by-gi-partners-300612878.html)
- [Togetherwork Acquires Protech](https://protechassociates.com/togetherwork-acquires-protech-associates-the-leading-association-software-built-on-microsoft-dynamics-365/)
- [Fonteva Acquired by Togetherwork](https://fonteva.com/fonteva-acquired-by-togetherwork/)
- [Togetherwork Acquires PetExec](https://www.prweb.com/releases/togetherwork-acquires-petexec-expanding-its-industry-leading-footprint-in-serving-pet-care-businesses-with-quality-software-and-payments-solutions-302335963.html)
- [OmegaFi Homepage](https://www.omegafi.com/)
- [OmegaFi Financial Management](https://www.omegafi.com/solutions/financial-management)
- [Togetherpay (Doubleknot)](https://www.doubleknot.com/blog/togetherpay)
- [Togetherpay ICS](https://www.omegafi.com/ics-togetherpay)
- [Neil Platt Crunchbase Profile](https://www.crunchbase.com/person/neil-platt)
- [Togetherwork Tracxn](https://tracxn.com/d/companies/togetherwork/__F-TBws-Jj3OmHy9_E7Ys4xe6ACxQkqiAlE-BeNxFNxA)
- [CircuiTree Moving to Stripe](https://support.circuitree.com/payment-processing-moving-to-stripe/)
