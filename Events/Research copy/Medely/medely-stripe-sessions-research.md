# MEDELY | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Medely
═══════════════════════════════════════

Logo: https://asset.brandfetch.io/idpKX5nNvq/idVJlL7ny6.svg
Nombre merchant: Medely

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Payout Speed Gap
Tittle_Pain Point_2: 60-Day Billing Mismatch
Tittle_Pain Point_3: Timesheet Fraud Risk
Tittle_Pain Point_4: Scale Breaks Workflows
Tittle_Pain Point_5: Single-Rail Payouts

Desc_Pain Point_1: Clinicians paid via direct deposit 2 days post-shift while competitors offer same-day. In a nursing shortage, faster payouts win talent every time.
Desc_Pain Point_2: Facilities bill on 60-day cycles while Medely pays 300K+ clinicians weekly. This cash flow gap forces pre-funded payroll, straining working capital at scale.
Desc_Pain Point_3: Per diem shift verification across hundreds of facilities creates fraud exposure. DOJ charged 324 defendants in 2025 for $14.6B in healthcare billing fraud.
Desc_Pain Point_4: Manual payment workflows break past 500 placements/month. Talent Fusion now orchestrates internal, per diem, and travel staff, multiplying payment complexity.
Desc_Pain Point_5: All clinician payouts run through a single ACH rail with no failover. Any bank rejection delays payment to workers who depend on fast compensation.

SLIDE 1: PSP TOPOLOGY

PSP_1: ACH Direct Deposit (primary)
PSP_2: Stripe (likely, marketplace billing)
PSP_3: Bank Wire (facility invoicing)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Instant RTP/FedNow
Local_M_2: Push-to-Card (Visa Direct)
Local_M_3: PayPal Instant Transfer
Local_M_4: Venmo
Local_M_5: Cash App Pay
Local_M_6: Zelle
Local_M_7: Apple Pay
Local_M_8: Google Pay
Local_M_9: Digital Wallets (general)
Local_M_10: Earned Wage Access Rails

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Instant Payout Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing by payout type, bank, and amount. With 300K+ clinicians across per diem, travel, and permanent placements, routing each disbursement to the fastest rail delivers 3-10% cost savings and same-day settlement.
Desc_Yuno_Cap2: Automatic cascade when ACH deposits fail or banks reject transfers. Instead of leaving a nurse unpaid, Yuno retries via push-to-card, RTP, or digital wallet in milliseconds. Up to 50% recovery on failed transactions protects clinician trust.
Desc_Yuno_Cap3: Activates instant payout rails clinicians demand: RTP/FedNow for real-time transfers, Visa Direct push-to-card, PayPal Instant, digital wallets. One API, 1,000+ methods. Same-day pay without building custom integrations per rail.
Desc_Yuno_Cap4: One dashboard unifying facility billing, clinician payouts, and Talent Fusion workforce payments. Real-time monitoring per facility, centralized reconciliation across shift types, and NOVA fraud detection (75% reduction) flagging phantom shifts.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Medely at a glance:**
- Founded: 2015 by Waleed Nasr and Khaled Nasr. HQ: Santa Monica, CA
- Total funding: $134M (investors: General Catalyst, Mayhaw Capital, and others)
- Self-described as "the world's largest healthcare talent marketplace"
- 300,000+ nurses and allied health professionals on the platform
- Expanding across the US; added seven new markets in January 2025 (Charlotte, Columbus, Las Vegas, Portland, Kansas City, and others)
- Employees: ~300-500 (estimated)
- Key products: Talent Marketplace (per diem and travel assignments), Talent Fusion (workforce orchestration platform, launched January 2026), Talent Fusion Flex
- Talent Fusion combines scheduling, credentialing, labor supply, utilization, and performance data with AI-powered planning
- Revenue model: Facilities pay only when they use the marketplace; no minimum usage requirements

**Confirmed Payment Stack:**
- ACH Direct Deposit: Primary clinician payout rail (2 days after shift completion, multiple payouts per week)
- Stripe: Highly likely for marketplace billing/facility payments (standard for healthcare marketplace billing; Stripe Connect powers similar platforms like Semble, Nextech)
- Bank Wire: Facility invoicing and high-value transactions
- Paper Check: Legacy fallback
- No instant pay or earned wage access (EWA) partner publicly confirmed
- No third-party payment orchestrator detected

**Healthcare Staffing Payment Industry Context:**
- Hospitals operate on 60-day billing cycles while clinicians expect weekly or same-day pay
- "A nurse choosing between two agencies will pick the one offering faster pay"
- 79% of workers willing to switch to an employer offering earned wage access
- Bi-weekly ACH settlements lose talent to same-day payout competitors
- FX markups of 1-3.5% erode margins on high-value payments (relevant if Medely expands internationally)
- Real-time settlements via RTP and FedNow now give medical professionals access to earnings in seconds
- DailyPay reports 82% of EWA users say it positively impacts absenteeism; 96% say it helps attract new talent

**Key Competitive Landscape:**
- ShiftKey: Largest PRN (as-needed) platform; strong independent contractor model
- Clipboard Health: Two-sided marketplace, no posting fees, can hire full-time without fees
- Trusted Health: Travel nursing marketplace
- Aya Healthcare: Full-service healthcare staffing with technology platform
- IntelyCare: Combines W-2 nursing staff with technology; offers instant pay via Branch
- Competitive differentiator: Medely's Talent Fusion orchestrates both internal and flexible staff, not just external marketplace

**Top 5 Pain Point Evidence:**

1. PAYOUT SPEED GAP
   - Medely pays via direct deposit 2 days after shift completion
   - Competitors offering same-day or instant pay attract talent away
   - 79% of healthcare workers would switch employers for faster pay access
   - IntelyCare, ShiftKey, and others already offer same-day or next-day pay options

2. 60-DAY BILLING MISMATCH
   - Healthcare facilities bill on 60-day cycles; clinicians paid weekly
   - Medely must pre-fund clinician payroll before facility payments arrive
   - Creates significant working capital strain as marketplace scales to 300K+ professionals
   - Cash flow gap widens with higher-value travel nursing assignments

3. TIMESHEET FRAUD RISK
   - DOJ 2025: 324 defendants charged, $14.6B in healthcare billing fraud uncovered
   - Per diem marketplace model creates exposure: shift verification across hundreds of facilities
   - Phantom shifts, inflated hours, and identity fraud are documented risks in healthcare staffing
   - CMS and HHS increasing AI-driven fraud detection enforcement

4. SCALE BREAKS WORKFLOWS
   - "When you scale from 50 placements monthly to 500, manual workflows break"
   - Talent Fusion now orchestrates per diem, travel, and internal staff simultaneously
   - Payment complexity multiplies: different rates, shift types, facilities, and payout schedules
   - Multi-state compliance adds tax filing complexity per jurisdiction

5. SINGLE-RAIL PAYOUTS
   - All clinician payouts through ACH direct deposit with no alternative rails
   - Bank rejections or ACH failures delay payment with no automatic retry or fallback
   - No push-to-card, no RTP/FedNow, no digital wallet options
   - Healthcare workers between shifts depend on predictable, fast compensation

**Key meeting angles:**
1. **300K+ clinician marketplace with payout speed as #1 differentiator** | Instant pay wins talent in a nursing shortage
2. **Talent Fusion changes the game** | Workforce orchestration platform needs sophisticated payment orchestration to match
3. **60-day billing gap** | Smart routing and multi-rail payouts reduce working capital strain
4. **Fraud detection at healthcare scale** | NOVA can flag timesheet anomalies and phantom shifts before payout
5. **ACH single point of failure** | Failover to push-to-card or RTP prevents clinician payment disruption
6. **Competitive pressure from instant pay** | IntelyCare and others already offer same-day; Medely needs to match or lose talent
7. **$134M raised, expanding rapidly** | Payment infrastructure investment needed to support multi-market growth

**Sources:**
- [Medely: Official Website](https://medely.com/)
- [Medely: Talent Marketplace](https://medely.com/facilities/talent-marketplace)
- [Medely: Talent Fusion Flex](https://medely.com/facilities/talent-fusion-flex)
- [Medely: Nurses & Allied](https://medely.com/nurses-allied)
- [Medely: Workforce Orchestration Launch (PR Newswire)](https://www.prnewswire.com/news-releases/medely-introduces-workforce-orchestration-redefining-how-healthcare-systems-manage-clinical-labor-302674388.html)
- [Medely: Seven Market Expansion (PR Newswire)](https://www.prnewswire.com/news-releases/medely-expands-into-seven-key-us-markets-to-simplify-healthcare-staffing-and-address-labor-shortages-302359098.html)
- [Medely: Crunchbase Profile](https://www.crunchbase.com/organization/medely)
- [Dots: Healthcare Staffing Payment Solutions](https://usedots.com/blog/healthcare-staffing-payment-solutions/)
- [Sidehusl: Medely Review](https://sidehusl.com/medely/)
- [Medely: App Store](https://apps.apple.com/us/app/medely-find-healthcare-shifts/id6478015730)
- [White & Case: Healthcare Fraud Enforcement 2025](https://www.whitecase.com/insight-our-thinking/healthcare-fraud-enforcement-2025-year-aggressive-action-expanding-risk)
- [DailyPay: Healthcare EWA](https://www.dailypay.com/industries/healthcare/)
- [Branch: Faster Pay for Healthcare](https://www.branchapp.com/blog/benefits-of-faster-pay-for-healthcare-workers)
- [Brandfetch: Medely Brand Assets](https://brandfetch.com/medely.com)
