# WORKSPOT | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Workspot
═══════════════════════════════════════

Logo: https://cdn.brandfetch.io/workspot.com/w/512/h/512/logo
Nombre merchant: Workspot

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: USD-Only Billing
Tittle_Pain Point_2: No Local Payment Methods
Tittle_Pain Point_3: No Failover on Renewals
Tittle_Pain Point_4: Marketplace Billing Split
Tittle_Pain Point_5: Manual Invoice Overhead

Desc_Pain Point_1: All subscriptions billed in USD. Global clients like Siemens Energy (90 countries) absorb FX costs each cycle, adding procurement friction.
Desc_Pain Point_2: No SEPA, UPI, PIX, or local bank transfers. Per-user annual billing with zero local methods blocks international expansion.
Desc_Pain Point_3: Annual billing on contract anniversary. One acquirer decline suspends cloud desktops for the entire org. No retry cascade exists.
Desc_Pain Point_4: Three billing channels (Azure, AWS, direct) each with separate payment flows. No unified dashboard across revenue streams.
Desc_Pain Point_5: Net 30 invoices with 1.5% late fees. Mid-cycle user additions prorated monthly. No multi-currency invoicing for global accounts.

SLIDE 1: PSP TOPOLOGY

PSP_1: Credit Card (direct billing)
PSP_2: Azure Marketplace
PSP_3: AWS Marketplace
PSP_4: Invoice / Net 30 (enterprise)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: SEPA Direct Debit
Local_M_2: iDEAL
Local_M_3: UPI
Local_M_4: PIX
Local_M_5: Boleto
Local_M_6: Konbini
Local_M_7: BLIK
Local_M_8: BACS Direct Debit
Local_M_9: ACH Direct Debit
Local_M_10: Bancontact

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each annual enterprise renewal to the highest-performing acquirer for that card BIN, issuer, and geography. With per-user SaaS pricing across customers in 15+ countries, even a 3% authorization uplift on renewals directly protects recurring cloud desktop revenue.
Desc_Yuno_Cap2: Automatic retry cascades across multiple acquirers protect Workspot's annual renewal cycle. When a charge fails on anniversary day, Yuno reroutes in milliseconds to a backup processor, recovering up to 50% of soft declines and preventing desktop interruptions.
Desc_Yuno_Cap3: Unlock enterprise billing across Workspot's global footprint: SEPA Direct Debit for EU customers like Siemens Energy and Rohm, UPI for India cloud regions, BACS for UK, ACH for US enterprises. One API, 1,000+ methods, zero engineering sprints per market.
Desc_Yuno_Cap4: One dashboard consolidating Workspot's fragmented billing: direct enterprise contracts, Azure Marketplace transactions, and AWS Marketplace orders. Real-time approval monitoring per geography, centralized reconciliation, and churn analytics tied to payment failures.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Workspot at a glance:**
- Enterprise-class SaaS platform delivering Windows 10/11 Cloud PCs and workstations on Microsoft Azure, Google Cloud, and AWS
- Founded: 2012 by Amitabh Sinha, Puneet Chawla, and Ty Wang
- Headquarters: Campbell, California (1999 South Bascom Avenue)
- Employees: ~125 across 3 continents (North America, Europe, Asia)
- Total funding: $106M through Series E
- Key investors: Kleiner Perkins, Qualcomm Ventures, Helion Ventures, Presidio Ventures, Translink Capital, Stoic VC
- Estimated annual revenue: $16M-$40M (private company, varying estimates)
- Multi-cloud: only enterprise VDI SaaS platform natively supporting Azure, AWS, and Google Cloud
- Key differentiator: 100% cloud-native architecture; pilots launch in 1 day, production in 45 days
- Cost savings: 50% on software, 67% on operational expenses vs. on-premises VDI
- Industries served: manufacturing, financial services, healthcare, legal, AEC (architecture, engineering, construction), life sciences, higher education

**Confirmed Payment Infrastructure:**
- Enterprise billing: annual subscription, per-user pricing, billed on contract anniversary
- Mid-cycle additions: prorated, billed in the next calendar month
- Payment terms: Net 30 invoicing; late fee of 1.5% per month
- Currency: all fees quoted and payable in USD (per enterprise subscription agreement)
- Marketplace channels: Azure Marketplace and AWS Marketplace (separate payment flows per marketplace)
- Credit card processing: uses third-party credit card processing company (specific processor not disclosed)
- No payment orchestrator detected
- No multi-currency billing capability documented

**Key Enterprise Customers:**
- Siemens Energy: global VDI transformation across 90 countries, 94,000 employees, on Google Cloud
- Hyundai: automotive manufacturing cloud desktop deployment
- JBS: world's largest cattle feeder, globetrotting workforce cloud access
- Teleperformance: global customer experience management
- Advisor 360: financial services, remote developers
- Mead & Hunt: engineering firm, 400+ employees, 30+ locations
- Poyner Spruill: law firm, Azure deployment
- Houston Eye Associates: healthcare, 29 locations
- Rohm: manufacturing (German company)
- Wood Rogers, OHM, Smallwood, Ramaker, Hanson, Dudek, C&S Companies, AGDATA, Hydradyne, Barge Design, Sherwood Design, Moffatt & Nichol, Global Finishing Solutions, Chaitons

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (~60% of revenue)
  Currently offer: Credit card, invoice (Net 30)
  Missing: ACH Direct Debit, wire transfer automation
  Enterprise clients spending $100K+ annually on per-user cloud desktop subscriptions prefer ACH. Credit card billing creates procurement friction for large deployments.

MARKET 2: Germany / DACH / EU (~15% of revenue)
  Currently offer: USD credit card, invoice
  Missing: SEPA Direct Debit, Sofort, invoice in EUR
  Siemens Energy and Rohm are German-headquartered enterprises. SEPA DD is standard for recurring B2B SaaS billing in Europe. USD-only invoicing adds FX overhead.

MARKET 3: United Kingdom (~8% of revenue)
  Currently offer: USD credit card, invoice
  Missing: BACS Direct Debit, Open Banking, GBP invoicing
  UK engineering and professional services firms are a core Workspot vertical. BACS DD is standard for UK enterprise SaaS subscriptions.

MARKET 4: Japan / APAC (~8% of revenue)
  Currently offer: USD credit card, invoice
  Missing: Konbini, bank transfer (furikomi), JCB optimization
  Workspot deploys cloud desktops from Azure Japan, Azure India, and Azure Australia regions. Zero local payment methods despite active cloud region presence.

MARKET 5: Brazil / LATAM (~5% of revenue)
  Currently offer: USD credit card, invoice
  Missing: PIX, Boleto, local bank transfer
  JBS (Brazilian headquarters) and other LATAM manufacturers represent expanding demand. USD-only billing creates unnecessary barriers for regional enterprise sales.

**Competitive Landscape:**
- Microsoft Azure Virtual Desktop (AVD): 62% enterprise DaaS adoption, native Azure billing
- VMware/Omnissa Horizon: legacy VDI, subscription shift causing 300% price hikes
- Citrix DaaS: mature HDX protocol, premium pricing, complex licensing
- Amazon WorkSpaces: pay-as-you-go, quick global reach, AWS billing integration
- Key industry pain: VDI licensing costs surging, legacy platforms underperforming, Teams integration failures

**Key meeting angles:**
1. **Annual renewal risk** | Per-user SaaS billing on contract anniversary creates a single point of failure; one declined charge can suspend cloud desktops for an entire organization
2. **Multi-cloud, single billing rail** | Workspot deploys across Azure, AWS, and Google Cloud globally but bills everything through USD-only credit card or invoice
3. **Global enterprise customers** | Siemens Energy (90 countries), JBS (Brazil HQ), Rohm (Germany), Hyundai (Korea) all pay in USD despite operating in local currency markets
4. **Marketplace fragmentation** | Revenue flowing through Azure Marketplace, AWS Marketplace, and direct contracts requires three separate reconciliation workflows
5. **Venture-backed growth stage** | $106M raised through Series E; optimizing payment costs and reducing involuntary churn directly impacts unit economics and path to profitability
6. **VDI market disruption** | As Citrix and VMware face pricing backlash, Workspot is winning enterprise migrations; payment infrastructure must scale with customer acquisition

**Sources:**
- [Workspot Homepage](https://www.workspot.com/)
- [Workspot Enterprise Subscription Agreement](https://www.workspot.com/legal/workspot-enterprise-subscription-agreement/)
- [Workspot Privacy Policy](https://www.workspot.com/legal/privacy-policy/)
- [Workspot Customers](https://www.workspot.com/customers/)
- [Workspot Company Page](https://www.workspot.com/company/)
- [Workspot Per-User Licensing Model](https://docs.workspot.com/docs/per-user-licensing-model-enterprise-and-enterprise-plus)
- [Workspot Global Desktops Overview](https://docs.workspot.com/docs/workspot-global-desktops-overview)
- [Siemens Energy x Workspot Press Release](https://www.workspot.com/press/siemens-energy-chooses-workspot-and-google-cloud-for-global-vdi-transformation/)
- [Workspot on Azure Marketplace](https://marketplace.microsoft.com/en-us/product/saas/workspot.sol-19199-uli)
- [Workspot Case Study (Google Cloud)](https://cloud.google.com/customers/workspot)
- [Workspot Crunchbase](https://www.crunchbase.com/organization/workspot)
- [Workspot ZoomInfo](https://www.zoominfo.com/c/workspot-inc/347226504)
- [Workspot CBInsights](https://www.cbinsights.com/company/workspot)
- [Workspot Capterra](https://www.capterra.com/p/195242/Workspot/)
- [Workspot G2 Reviews](https://www.g2.com/products/workspot-enterprise-desktop-cloud/reviews)
- [Brandfetch: Workspot Logo](https://brandfetch.com/workspot.com)
- [VDI Market 2025 Buyer's Guide (IronOrbit)](https://www.ironorbit.com/vdi-solution-providers-2025-guide/)
- [Citrix Alternatives 2026 (CheckThat)](https://checkthat.ai/brands/citrix/alternatives)
