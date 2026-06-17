# MGM RESORTS INTERNATIONAL | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: MGM Resorts International
=======================================

Logo: https://upload.wikimedia.org/wikipedia/commons/2/8a/MGM_Resorts_International_logo.svg
Nombre merchant: MGM Resorts International

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Fragmented Payment Stack
Tittle_Pain Point_2: Cyber Breach Aftermath
Tittle_Pain Point_3: iGaming Payout Delays
Tittle_Pain Point_4: Multi Market Complexity
Tittle_Pain Point_5: Loyalty Wallet Friction

Desc_Pain Point_1: FreedomPay handles POS across 28 US properties, Nuvei processes BetMGM online deposits, and Macau runs an entirely separate acquiring stack. No single layer unifies hotel, gaming, and digital payments. Reconciliation is siloed by channel and geography.
Desc_Pain Point_2: The September 2023 ransomware attack knocked out credit card processing, ATMs, POS terminals, and room keys for 10 days. MGM lost $100M in Q3 2023. Manual cash fallback exposed how dependent 28 properties are on a single payment path with zero failover.
Desc_Pain Point_3: BetMGM players across 29 US states report 3 to 5 day withdrawal waits. Real time payouts via Nuvei RTP cover only select banks. ACH and card cashouts still batch process overnight. In a market where DraftKings offers instant PayPal, slow payouts cost retention.
Desc_Pain Point_4: US resorts run FreedomPay POS on Oracle OPERA. BetMGM UK operates through LeoVegas on separate rails. MGM China uses local Macau acquirers. Japan (opening 2030) will need JCB, PayPay, and Konbini. Each market is a standalone payment island.
Desc_Pain Point_5: MGM Rewards spans 40M+ members across hotels, casinos, BetMGM, and dining. Yet payment data is not unified. A guest who spends on property cannot seamlessly link that to their BetMGM wallet. No single view of customer payment behavior across touchpoints.

SLIDE 1: PSP TOPOLOGY

PSP_1: FreedomPay
PSP_2: Nuvei
PSP_3: LeoVegas (Entain/BetMGM UK)
PSP_4: Visa/MC Direct (Macau)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: PayPay (Japan)
Local_M_2: Konbini (Japan)
Local_M_3: JCB (Japan online)
Local_M_4: Alipay+ (Macau tourists)
Local_M_5: WeChat Pay (Macau tourists)
Local_M_6: Pix (Brazil, BetMGM expansion)
Local_M_7: Skrill (BetMGM UK)
Local_M_8: Neteller (BetMGM UK)
Local_M_9: Trustly (Open Banking)
Local_M_10: Cash App Pay (US digital)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing Engine
Tittle_Yuno_Cap2: Failover & Cascade Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration Layer

Desc_Yuno_Cap1: Route every transaction to the optimal acquirer by channel, geography, and card type in real time. With $17.5B annual revenue flowing through hotels, casinos, dining, and iGaming, even a 2% authorization uplift recovers hundreds of millions. Smart Routing replaces static processor assignments with dynamic, data driven decisions across FreedomPay, Nuvei, and regional rails.
Desc_Yuno_Cap2: When FreedomPay POS declines a card or Nuvei rejects a BetMGM deposit, Yuno cascades to the next viable processor in milliseconds. The 2023 cyberattack proved a single point of failure is catastrophic. With Yuno, if one processor goes down, transactions reroute automatically. No guest sees a declined payment while a working path exists.
Desc_Yuno_Cap3: One API activates PayPay and Konbini for MGM Osaka (2030), Alipay+ and WeChat Pay for Macau tourist spend, Skrill and Neteller for BetMGM UK, Pix for future Brazil iGaming, and Trustly open banking across Europe. Yuno connects 1,000+ payment methods across 40+ countries, eliminating per market engineering sprints.
Desc_Yuno_Cap4: Replace siloed reconciliation across FreedomPay (28 US hotels), Nuvei (BetMGM US), LeoVegas (BetMGM UK), and Macau local acquirers with one dashboard. Real time approval rates by property, channel, and market. Centralized settlement across hospitality, gaming, and digital. Perfectly timed for MGM Osaka: one Yuno integration covers all payment rails from day one.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**MGM Resorts International at a glance:**
- Founded 1986 (as Grand Name Co.), renamed MGM Grand Inc. in 1987, became MGM Resorts International in 2010
- Headquarters: Las Vegas, Nevada, USA
- CEO: Bill Hornbuckle (President & CEO)
- 18 casino hotel properties: 16 in the US (Bellagio, MGM Grand, Mandalay Bay, ARIA, Park MGM, Luxor, Excalibur, New York New York, etc.) and 2 in Macau (MGM Macau, MGM Cotai)
- 77,000+ employees across all properties
- Revenue: $17.5B (FY2025), $17.2B (FY2024, record year driven by MGM China rebound)
- Las Vegas Strip Resorts: $8.82B (2024). Regional Operations: $3.72B. MGM Digital: $552M
- Consolidated Adjusted EBITDA: $2.41B (2024)
- BetMGM: Joint venture with Entain Plc, live in 29 US states, launched UK operations via LeoVegas in 2023
- BetMGM reported 34% revenue growth Q1 2025, 36% growth Q2 2025
- MGM Osaka integrated resort targeting 2030 opening, described as "world's largest integrated resort"
- MGM Rewards loyalty program: 40M+ members spanning hotels, casinos, dining, and BetMGM
- Listed on NYSE as MGM

**Confirmed PSPs and payment partners:**

| Provider | Role | Region |
|----------|------|--------|
| FreedomPay | POS commerce platform, EMV, NFC, P2PE encryption, integrated with Oracle OPERA PMS | All US properties (28 hotels) |
| Nuvei | BetMGM payment provider: deposits, payouts, payment orchestration, smart routing, RTP | BetMGM US (29 states) |
| LeoVegas / Entain | BetMGM UK payment processing | UK |
| Visa / Mastercard | Direct acquiring | All markets |
| PayPal | Digital wallet deposits and withdrawals | BetMGM US and UK |
| Venmo | Instant deposits | BetMGM US |
| Apple Pay | Mobile wallet | BetMGM US (iOS), hotel properties |
| Coupa | Accounts payable / procurement platform (not consumer facing) | Corporate |

**No unified payment orchestrator detected across hotel + gaming + digital channels.**

**BetMGM Accepted Payment Methods (US):**
- Visa, Mastercard, Discover, American Express (credit/debit)
- ACH / VIP Preferred e-Check
- PayPal, Venmo, Apple Pay
- BetMGM prepaid gift cards (sold at 7-Eleven and others)
- MGM Rewards Mastercard (no annual fee, no cash advance fee)
- Casino cage cash deposits
- Wire transfers

**BetMGM Accepted Payment Methods (UK):**
- Visa, Mastercard (debit only, credit cards banned for UK gambling)
- PayPal
- Apple Pay
- Bank transfers
- Not accepted: Skrill, Neteller (major gap for UK iGaming)

**September 2023 Cyberattack Impact:**
- ALPHV/Scattered Spider ransomware attack via social engineering of IT help desk
- 10 day outage: credit card processing, ATMs, POS, digital room keys, slot machines, Wi-Fi all down
- Guests forced to use cash; rooms could not process card payments
- $100M total Q3 2023 loss ($84M lost revenue + $10M consulting/legal + $6M remediation)
- MGM committed $50M to cybersecurity upgrades post incident
- MGM did not pay the ransom

**Key meeting angles:**
1. **Post breach resilience** | The 2023 attack proved MGM has zero payment failover. An orchestration layer with automatic cascade to backup processors would prevent total payment blackout across 28 properties
2. **FreedomPay + Nuvei = two isolated stacks** | Hotel POS and iGaming payments share no data, no routing logic, no unified dashboard. Yuno bridges both with a single integration
3. **BetMGM payout speed** | 3 to 5 day withdrawals lose players to DraftKings and FanDuel who offer instant PayPal. Orchestrated payout routing can unlock faster cash out paths
4. **Japan 2030 = greenfield** | MGM Osaka needs JCB, PayPay, Konbini, Line Pay from launch. Building with an orchestrator avoids replicating the US silo problem
5. **UK missing Skrill/Neteller** | Two of the most popular UK iGaming wallets are absent from BetMGM UK. Yuno's 1,000+ APM library fills this instantly
6. **40M loyalty members, zero payment unification** | MGM Rewards connects hotels, casinos, dining, and BetMGM, but payment data stays siloed. One orchestration layer enables cross channel payment analytics
7. **$17.5B revenue scale** | Even marginal auth rate improvements across hotel, casino, and digital transactions translate to nine figure revenue recovery

**Sources:**
- [FreedomPay: MGM Resorts Case Study](https://corporate.freedompay.com/case-study/mgm-resorts-international/)
- [FreedomPay: MGM Deployment Press Release](https://corporate.freedompay.com/about-us/press-release/freedompay-deploys-commerce-platform-at-mgm-resorts-international-properties)
- [Nuvei: Selected as BetMGM Payment Provider (Oct 2021)](https://investors.nuvei.com/English/news/news-details/2021/Nuvei-Selected-as-New-Payment-Provider-for-BetMGM/default.aspx)
- [Nuvei: BetMGM Partnership Announcement](https://www.nuvei.com/posts/nuvei-selected-as-new-payment-provider-for-betmgm)
- [BetMGM Casino Payment Methods Guide](https://casino.betmgm.com/en/blog/guides/online-casino-payment-methods/)
- [BetMGM UK Payment Methods](https://help.betmgm.co.uk/hc/en-gb/articles/12184730187538-What-payment-methods-does-BetMGM-accept)
- [BetMGM US Deposit Methods 2026](https://www.aceodds.com/payment-methods/deposit/betmgm/us.html)
- [BetMGM UK Deposit Methods 2026](https://www.aceodds.com/payment-methods/deposit/betmgm/uk.html)
- [MGM Resorts Q4 and Full Year 2024 Results](https://www.prnewswire.com/news-releases/mgm-resorts-international-reports-fourth-quarter-and-record-full-year-2024-results-302375211.html)
- [MGM Resorts Q3 2025 Results](https://www.prnewswire.com/news-releases/mgm-resorts-international-reports-third-quarter-2025-financial-and-operating-results-302597342.html)
- [BetMGM FY 2025 Business Update](https://www.prnewswire.com/news-releases/betmgm-fy-2025-business-update-302678465.html)
- [MGM CEO: Digital as Top Focus 2025](https://cdcgaming.com/mgm-resorts-ceo-cites-digital-as-top-focus-in-2025/)
- [MGM Resorts Digital Transformation 2024 Report](https://www.globenewswire.com/news-release/2024/07/04/2908727/0/en/MGM-Resorts-International-Accelerates-Digital-Innovation-Through-Strategic-Technology-Initiatives-2024-Report.html)
- [Cisco x MGM Multi Year Agreement (Nov 2024)](https://newsroom.cisco.com/c/r/newsroom/en/us/a/y2024/m11/cisco-and-mgm-resorts-international-sign-multi-year-agreement.html)
- [MGM Resorts Cyberattack: Costs & Recovery](https://inszoneinsurance.com/blog/cyberattack-mgm-resort-explained)
- [MGM Cyber Attack Overview (Netwrix)](https://netwrix.com/en/resources/blog/mgm-cyber-attack/)
- [MGM Cyber Attack Timeline (CSHub)](https://www.cshub.com/attacks/news/a-full-timeline-of-the-mgm-resorts-cyber-attack)
- [MGM Wikipedia](https://en.wikipedia.org/wiki/MGM_Resorts_International)
- [MGM Resorts Logo (Wikimedia SVG)](https://commons.wikimedia.org/wiki/Category:MGM_Resorts_International)
- [iGaming Business: MGM Record Revenue 2024](https://igamingbusiness.com/finance/full-year-results/china-drives-mgm-record-revenue-2024/)
- [MGM China Q4 2025 Performance](https://agbrief.com/news/macau/06/02/2026/mgm-china-crushed-it-in-4q25-mgm-resorts-cfo/)
- [Facebook: MGM Rewards Payment Issues](https://www.facebook.com/groups/mgmrewards/posts/1207673873628677/)
- [BetMGM Deposit Troubleshooting](https://bettinghero.com/help/betmgm/deposit/troubleshooting-guide-for-depositing-issues-on-the-betmgm-app/)
