# TD AMERITRADE (CHARLES SCHWAB) | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: TD Ameritrade (Charles Schwab)
=======================================

Logo: https://upload.wikimedia.org/wikipedia/commons/5/5c/Charles_Schwab_Corporation_logo.svg
Nombre merchant: TD Ameritrade (Charles Schwab)

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Legacy Platform Fragility
Tittle_Pain Point_2: USD-Only Deposit Bottleneck
Tittle_Pain Point_3: Wire Transfer Fee Drag
Tittle_Pain Point_4: Single-Rail Card Routing
Tittle_Pain Point_5: Fraud Stack Fragmentation

Desc_Pain Point_1: The thinkorswim platform inherited from TD Ameritrade suffers recurring outages, frozen orders, and system maintenance blackouts every Friday through Monday open. With 46.5M accounts and $11.9T in assets, even brief downtime during market hours can trigger cascading trade failures and client attrition.
Desc_Pain Point_2: Schwab International accepts deposits only in USD via wire transfer or check. Clients across 100+ eligible countries cannot fund accounts using local rails like SEPA, Open Banking, or Pix, forcing costly FX conversions with markups up to 3% before funds even arrive.
Desc_Pain Point_3: International wire transfers cost $15 to $25 per transaction and take 2 to 7 business days. Correspondent bank fees add hidden costs. For a platform managing $519B in annual net new assets, slow and expensive funding rails create friction that competitors with instant local deposits exploit.
Desc_Pain Point_4: The Schwab Bank Visa Platinum Debit Card routes exclusively through a single Visa path. With no multi-acquirer routing or automatic retry logic, every soft decline on the 46.5M account base is a lost transaction with zero recovery opportunity across the $15,000 daily purchase limit.
Desc_Pain Point_5: Schwab inherited TD Ameritrade's Veo ecosystem of 180+ fintech integrations but runs fraud prevention separately from payment processing. The 2023 MOVEit breach exposed client data across both legacy systems. No unified fraud layer across brokerage, banking, and card transactions.

SLIDE 1: PSP TOPOLOGY

PSP_1: Charles Schwab Bank (issuing bank, FDIC member)
PSP_2: Visa (debit card network)
PSP_3: ACH / Fedwire (deposit/withdrawal rails)
PSP_4: BNY Mellon (transfer agency services)
PSP_5: DTCC (securities clearing)
PSP_6: Schwab Clearing (self-clearing broker-dealer)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: SEPA Instant (EU)
Local_M_2: Open Banking (UK/EU)
Local_M_3: iDEAL (Netherlands)
Local_M_4: Bancontact (Belgium)
Local_M_5: BLIK (Poland)
Local_M_6: Pix (Brazil)
Local_M_7: SPEI (Mexico)
Local_M_8: UPI (India)
Local_M_9: PayNow (Singapore)
Local_M_10: GrabPay (Southeast Asia)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each deposit, withdrawal, and card transaction through the optimal rail by amount, speed, and geography. With $519B in annual net new assets and 46.5M accounts, shifting international deposits from $25 wire transfers to lower-cost local rails saves millions in funding friction. Smart Routing delivers +3 to 10% authorization uplift on Visa debit transactions.
Desc_Yuno_Cap2: Automatic cascade eliminates single-acquirer card dependency. When a Visa Platinum debit transaction declines on the primary path, Yuno reroutes instantly through an alternate acquirer. Up to 50% recovery on failed transactions, protecting the spending experience for millions of Schwab checking account holders.
Desc_Yuno_Cap3: Activates the local deposit rails Schwab needs for its 100+ country international client base: SEPA Instant and Open Banking for EU, iDEAL for Netherlands, Pix for Brazil, SPEI for Mexico, UPI for India, PayNow for Singapore. One API, 1,000+ payment methods, eliminating the USD-only bottleneck.
Desc_Yuno_Cap4: One dashboard unifying Schwab Bank checking, brokerage deposits, Visa debit card, ACH rails, and wire transfers into a single reconciliation layer. Real-time transaction monitoring across all entities, NOVA fraud engine with 75% fewer false positives replacing the fragmented fraud stack inherited from the TD Ameritrade merger.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**TD Ameritrade / Charles Schwab at a glance:**
- Founded: TD Ameritrade (1975, Omaha, NE); acquired by Charles Schwab (est. 1971) for $26B in Oct 2020
- Platform transition: All TD Ameritrade accounts migrated to Schwab by Q2 2024; TD Ameritrade platform shut down May 2024
- Public: SCHW on NYSE
- Revenue: $23.9B FY2025 (record, +22% YoY)
- Net Income: $2.5B in Q4 2025 alone; $1.33 EPS ($1.39 adjusted)
- Total Client Assets: $11.9T (record, end of 2025)
- Client Accounts: 46.5M (+6% YoY)
- Net New Assets: $519B in 2025 (5.1% organic growth rate)
- Employees: ~32,100 (2025)
- International presence: 100+ eligible countries for international brokerage accounts

**Key 2025/2026 milestones:**
- TD Ameritrade full integration completed: 17M accounts, $1.9T in assets migrated
- TD Bank divested its 10.1% stake in Schwab (early 2025)
- Forge acquisition: $660M deal for private market access (Nov 2025)
- Wealth.com investment: AI-powered estate planning integration (Apr 2025)
- Record $519B in core net new assets, 5.1% organic growth
- Rick Wurster named new CEO

**Product suite:**
- Schwab Brokerage: Commission-free stocks, ETFs, options, futures, forex
- thinkorswim: Advanced trading platform (desktop, web, mobile) inherited from TD Ameritrade
- Schwab Bank Investor Checking: No monthly fees, 0.40% APY, unlimited ATM fee rebates worldwide
- Schwab Bank Investor Savings: Linked savings with Visa debit access
- Visa Platinum Debit Card: Contactless, no foreign transaction fees, Apple/Google/Samsung Pay
- Schwab Intelligent Portfolios: Robo-advisory
- Schwab Clearing: Self-clearing broker-dealer

**Confirmed PSPs / Payment Rails:**
- Charles Schwab Bank, SSB: FDIC-insured issuing bank for checking, savings, debit card
- Visa: Platinum Debit Card network (contactless)
- ACH Network: Electronic fund transfers (Schwab MoneyLink)
- Fedwire: Domestic wire transfers
- SWIFT: International wire transfers ($15 online, $25 phone)
- DTCC: Securities clearing and settlement (direct participant)
- BNY Mellon: Transfer agency services for Schwab Investment Management
- Schwab Clearing: In-house self-clearing for brokerage operations
- No payment orchestrator detected

**Deposit Methods & Fees:**
- ACH (Schwab MoneyLink): Free, 1 to 3 business days
- Domestic wire: Free incoming; $25 outgoing
- International wire: $15 online, $25 phone; 2 to 7 business days
- Check deposit: Free (mail or mobile)
- FX conversion markup: Up to 3% of principal (300 basis points)
- International deposits: USD only (no local currency accepted)

**Key Meeting Angles:**
1. **$11.9T in assets, USD-only international deposits** | Clients in 100+ countries forced through costly wire transfers; local rails would unlock faster, cheaper funding
2. **46.5M accounts, single-rail Visa debit** | No multi-acquirer routing means every soft decline is unrecoverable revenue
3. **TD Ameritrade integration debt** | thinkorswim instability (outages, frozen orders) reflects deeper infrastructure fragmentation that extends to payment processing
4. **3% FX markup on international transfers** | Competitors like Interactive Brokers offer multi-currency accounts; Schwab's USD-only model bleeds international clients
5. **$519B net new assets need faster rails** | Record asset gathering constrained by 2 to 7 day international wire settlement
6. **MOVEit breach exposed fragmented security** | Unified payment orchestration with integrated fraud engine replaces patchwork vendor security
7. **Self-clearing but payment-outsourced** | Schwab built in-house clearing; payment orchestration is the logical next infrastructure layer
8. **Competitor pressure** | Interactive Brokers (95 exchanges, multi-currency), Fidelity (instant deposits), Robinhood (commission-free + crypto)

**Sources:**
- [Schwab Reports Record 4Q and Full Year 2025 Results (Press Release)](https://pressroom.aboutschwab.com/press-releases/press-release/2026/Schwab-Reports-Record-4Q-and-Full-Year-2025-Results/default.aspx)
- [Charles Schwab Revenue 2012-2025 (MacroTrends)](https://www.macrotrends.net/stocks/charts/SCHW/charles-schwab/revenue)
- [Schwab Record Revenue and Earnings Q3 2025 (PDF)](https://content.schwab.com/web/retail/public/about-schwab/schwab_q3_2025_earnings_release.pdf)
- [Schwab Record 2025 Results (InvestmentNews)](https://www.investmentnews.com/ria-news/schwab-posts-record-2025-results-but-still-just-shy-of-wall-street-estimates/264916)
- [Charles Schwab Number of Employees (MacroTrends)](https://www.macrotrends.net/stocks/charts/SCHW/charles-schwab/number-of-employees)
- [Charles Schwab Statistics 2026 (InvestingInTheWeb)](https://investingintheweb.com/brokers/charles-schwab-statistics/)
- [Charles Schwab International Account FAQ](https://international.schwab.com/faqs)
- [Schwab International Wire Transfer Fees (Wise)](https://wise.com/us/blog/international-transfer-charles-schwab-us)
- [Schwab Visa Platinum Debit Card](https://www.schwab.com/checking/debit-card)
- [Schwab Checking Account](https://www.schwab.com/checking)
- [Schwab $26B Acquisition of TD Ameritrade (Davis Polk)](https://www.davispolk.com/experience/schwab-26-billion-acquisition-td-ameritrade)
- [TD Ameritrade Transition Celebration (Financial Planning)](https://www.financial-planning.com/list/charles-schwab-celebrates-successful-uneventful-1-3-trillion-td-ameritrade-account-transition)
- [Thinkorswim Clients Report Tech Problems (ThinkAdvisor)](https://www.thinkadvisor.com/2025/02/10/thinkorswim-clients-report-tech-problems/)
- [Schwab MOVEit Data Breach (ThinkAdvisor)](https://www.thinkadvisor.com/2023/08/24/schwab-td-ameritrade-hit-with-class-action-suit-over-moveit-hack/)
- [BNY Mellon x Schwab Transfer Agency (BNY)](https://www.bny.com/corporate/global/en/about-us/newsroom/press-release/bny-mellon-selected-by-charles-schwab-investment-management-to-provide-transfer-agency-services-130181.html)
- [DTCC Participant Report (PDF)](https://www.dtcc.com/-/media/Files/Downloads/client-center/DTC/DTC-Participant-in-Alphabetical-Listing-1.pdf)
- [Schwab MoneyLink Terms](https://www.schwab.com/legal/schwab-moneylink-terms-and-conditions)
- [Charles Schwab Corporation Logo (Wikimedia Commons)](https://commons.wikimedia.org/wiki/File:Charles_Schwab_Corporation_logo.svg)
- [Charles Schwab 2025 Annual Report](https://www.aboutschwab.com/annual-report)
- [Schwab Forge Acquisition (The Motley Fool)](https://www.fool.com/investing/2026/04/01/what-im-watching-with-charles-schwab-to-see-if-the/)
