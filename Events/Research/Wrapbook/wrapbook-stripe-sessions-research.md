# WRAPBOOK | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Wrapbook
=======================================

Logo: https://cdn.brandfetch.io/wrapbook.com/w/512/h/512/logo
Nombre merchant: Wrapbook

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Check-Based Agent Payouts
Tittle_Pain Point_2: No Failover on ACH
Tittle_Pain Point_3: USD-Only Processing
Tittle_Pain Point_4: Payroll Float Risk
Tittle_Pain Point_5: Studio Payment Friction

Desc_Pain Point_1: Wrapbook pays talent agents exclusively via mailed paper checks. In an industry processing billions in production payroll annually, check-based payouts create 5-7 day settlement delays, manual reconciliation overhead, and poor talent agent experience compared to instant digital methods.
Desc_Pain Point_2: Production payroll is time-sensitive. When ACH or wire transfers fail for crew payments on wrap day, there is no documented backup acquirer or retry cascade. For productions processing payroll for hundreds of crew members simultaneously, a single failure creates cascading delays.
Desc_Pain Point_3: With 1,000+ production companies as clients and the entertainment industry increasingly global, Wrapbook processes exclusively in USD. International productions shooting abroad need local currency payouts for crew in UK (GBP), EU (EUR), Canada (CAD), and Australia (AUD).
Desc_Pain Point_4: Production payroll creates concentrated payment spikes. Studios fund millions in crew payments within narrow windows (weekly wraps). Processing these bulk payroll transfers through a single payment rail creates float risk and settlement concentration.
Desc_Pain Point_5: Four major studios use Wrapbook. Studio payment workflows require invoice reconciliation, purchase order matching, and multi-department approvals. Without flexible payment rails, funding production accounts creates unnecessary friction for finance teams at scale.

SLIDE 1: PSP TOPOLOGY

PSP_1: ACH / Direct Deposit (crew payroll)
PSP_2: Paper Check (agent commissions)
PSP_3: Wire Transfer (studio funding)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Instant ACH / Same-Day ACH
Local_M_2: Real-Time Payments (RTP)
Local_M_3: SEPA Credit Transfer
Local_M_4: Faster Payments (UK)
Local_M_5: BACS Direct Credit
Local_M_6: Interac e-Transfer (Canada)
Local_M_7: NPP/PayID (Australia)
Local_M_8: PIX (Brazil)
Local_M_9: Push-to-Card (Visa Direct)
Local_M_10: Digital Wallet Payouts

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each production payroll batch to the optimal payment rail by amount, urgency, and geography. For productions processing crew payments across multiple states and unions, smart routing selects the fastest, cheapest rail per transaction, reducing payroll processing costs.
Desc_Yuno_Cap2: Automatic retry cascades across multiple payment rails protect production payroll timing. When a crew ACH transfer fails on wrap day, Yuno reroutes to a backup processor in milliseconds. Up to 50% recovery on failed transfers ensures crew gets paid on time every time.
Desc_Yuno_Cap3: Unlock global production payroll: SEPA for European shoots, Faster Payments for UK crew, Interac for Canadian productions, Push-to-Card for instant crew payments. One API, 1,000+ methods, enabling Wrapbook to serve international productions without building local payment infrastructure.
Desc_Yuno_Cap4: One dashboard consolidating Wrapbook's payroll disbursements across ACH, wire, check, and future local rails. Real-time settlement monitoring per production, centralized reconciliation across studios, and cost analytics per payment method for the 1,000+ production company base.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Wrapbook at a glance:**
- Unified platform for entertainment payroll, accounting, cost-tracking, and reporting
- Valuation: $750M (equity financing round, September 2024)
- Total funding: $151M over 4 rounds; latest $20M from Bessemer Venture Partners
- 402 employees as of March 2026 (growing from 250+)
- 1,000+ production companies as clients
- 50% YoY revenue growth since Series A (2021)
- Founded 2018, headquartered in Los Angeles/San Francisco
- Approved payroll vendor for 4 major production studios
- Competing against Cast & Crew and Entertainment Partners (PE-owned incumbents)

**Notable customers:**
- 4 major production studios (approved vendor)
- CAA and WME (talent agencies, track payment progress)
- SMUGGLER, Greenpoint, Picture North, Dress Code (commercial production)
- London Alley Great Guns (international production)
- Ghost Robot (creative studio)

**Confirmed PSPs / Payment methods:**
- ACH / Direct Deposit for crew payroll
- Paper checks for talent agent commission payments
- Wire transfer for studio funding
- Timecards trigger automatic payroll calculations
- No payment orchestrator detected
- No international payment rails detected

**Product capabilities:**
- Production payroll (union and non-union)
- Production accounting
- Cost tracking and reporting
- Digital onboarding (I-9, W-4, start paperwork)
- Workers' compensation
- Employer of Record services

**Market context:**
- US entertainment industry spends $50B+ annually on production costs
- Payroll represents 40-60% of total production budgets
- Cast & Crew (PE-owned) is the dominant incumbent
- Entertainment Partners (PE-owned) is the second largest
- Wrapbook is the leading digital-native challenger
- Global production increasingly shoots internationally (UK, Canada, Australia, EU)

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (primary market, all operations)
  Currently offer: ACH, wire transfer, paper check
  Missing: Same-Day ACH, RTP, Push-to-Card (Visa Direct)
  Crew expects faster payments. Same-day and instant options would differentiate vs. Cast & Crew.

MARKET 2: United Kingdom (international productions)
  Currently offer: Wire transfer (USD)
  Missing: Faster Payments, BACS Direct Credit, GBP payroll
  UK is the second-largest film/TV production market. Local GBP payroll is essential for UK crew.

MARKET 3: Canada (international productions)
  Currently offer: Wire transfer (USD)
  Missing: Interac e-Transfer, CAD payroll, Canadian direct deposit
  Vancouver and Toronto are major production hubs. Canadian crew expects local payment methods.

MARKET 4: EU / Germany (international productions)
  Currently offer: Wire transfer (USD)
  Missing: SEPA Credit Transfer, EUR payroll
  European productions shooting in Germany, France, and Spain need local EUR payroll capabilities.

MARKET 5: Australia (international productions)
  Currently offer: Wire transfer (USD)
  Missing: NPP/PayID, AUD payroll
  Australian production market is growing. Local payment infrastructure needed for crew payments.

**Key meeting angles:**
1. **$750M valuation, 50% YoY growth** | Rapid scaling without payment diversification creates growing operational risk for payroll-critical infrastructure.
2. **Paper checks in 2026** | Agent commissions via mailed paper checks is an obvious modernization opportunity. Digital payouts would save days per cycle.
3. **4 major studios** | Studio-approved vendor status means high-volume, high-stakes payroll. A single payment failure on wrap day cascades across hundreds of crew members.
4. **International production expansion** | Global shoots in UK, Canada, EU, and Australia need local currency payroll. Current USD-only limits Wrapbook's addressable market.
5. **Cast & Crew disruption** | Wrapbook's competitive advantage is being digital-native. Offering instant payouts and global payment rails extends this moat vs. PE-owned incumbents.
6. **Payroll is time-critical** | Unlike typical SaaS billing, production payroll failures have immediate workforce consequences. Failover is not optional.

**Sources:**
- [Wrapbook Homepage](https://www.wrapbook.com)
- [Wrapbook $750M Valuation](https://www.prnewswire.com/news-releases/wrapbook-raises-equity-financing-at-a-750m-valuation-plus-launch-of-secondary-tender-offer-for-employees-from-bessemer-venture-partners-302256240.html)
- [Wrapbook $20M Raise (Hollywood Reporter)](https://www.hollywoodreporter.com/business/business-news/wrapbook-fund-bessemer-venture-partners-1236009642/)
- [Wrapbook on Bessemer](https://www.bvp.com/news/wrapbook-the-unified-platform-for-entertainment-payroll-accounting-cost-tracking-and-reporting)
- [Wrapbook 2026 Production Finance Report](https://www.prnewswire.com/news-releases/wrapbook-releases-2026-state-of-production-finance--accounting-report-302703092.html)
- [Wrapbook Payments Help](https://help.wrapbook.com/docs/about-payments-worker)
- [Wrapbook Payment Setup](https://help.wrapbook.com/docs/how-to-set-up-your-payment-method)
- [AlleyWatch: Wrapbook Funding](https://alleywatch.com/2024/09/wrapbook-finance-payroll-production-platform-entertainment-industry-employer-of-record-cameron-woodward/)
- [Contrary Research: Wrapbook](https://research.contrary.com/company/wrapbook)
- [Brandfetch: Wrapbook Logo](https://brandfetch.com/wrapbook.com)
- [Tracxn: Wrapbook Profile](https://tracxn.com/d/companies/wrapbook/__YkZjgygbtL2LnYqRLCCB9zIv9_dMWQLqDcLQZs-ovSE)
