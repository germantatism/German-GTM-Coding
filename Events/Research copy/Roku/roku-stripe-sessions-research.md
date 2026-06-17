# ROKU | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Roku
═══════════════════════════════════════

Logo: https://upload.wikimedia.org/wikipedia/commons/1/13/Roku_logo.svg
Nombre merchant: Roku

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Card-Only Limitation
Tittle_Pain Point_2: International ARPU Gap
Tittle_Pain Point_3: Payment Update Friction
Tittle_Pain Point_4: No Failover Processing
Tittle_Pain Point_5: LATAM Method Gaps

Desc_Pain Point_1: Roku Pay accepts only Visa, MC, Amex, Discover, and PayPal. No debit cards, no local wallets, no bank transfers. In markets like Mexico (5.8% of accounts) and Brazil (4.1%), card penetration is too low for this approach.
Desc_Pain Point_2: ARPU stuck at $41.49 despite 100M+ streaming households. International accounts growing 37.8% YoY but generate fraction of US ARPU. No local payment methods means lower conversion and higher churn outside North America.
Desc_Pain Point_3: Users report entering card details 20+ times with repeated "card processor will not accept" errors. Region mismatch between account and billing country systematically blocks valid cards.
Desc_Pain Point_4: Roku Billing Services processes 100% of Roku Pay transactions through a single card processor. Zero acquirer redundancy: any processor disruption blocks all subscription renewals and channel purchases globally.
Desc_Pain Point_5: Mexico and Brazil are top 2 international markets (combined ~10% of accounts, growing 47% YoY). Neither has Pix, OXXO, Boleto, or SPEI. Only credit cards accepted in cash-preferred economies.

SLIDE 1: PSP TOPOLOGY

PSP_1: Roku Billing Services (proprietary)
PSP_2: PayPal (developer payouts)
PSP_3: Visa/MC/Amex/Discover networks
PSP_4: Apple (Roku devices sold via Apple retail)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: OXXO
Local_M_3: SPEI
Local_M_4: Boleto
Local_M_5: SEPA Direct Debit
Local_M_6: iDEAL
Local_M_7: Interac
Local_M_8: UPI
Local_M_9: BLIK
Local_M_10: Konbini

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each Roku Pay subscription renewal and channel purchase to the highest performing acquirer by card BIN, issuer, and geography. With $4.7B revenue, 100M+ households, and $41.49 ARPU, a 3% auth uplift translates to $140M+ in recovered annual revenue.
Desc_Yuno_Cap2: Automatic cascade eliminates Roku's single billing processor dependency. When the primary acquirer declines, Yuno reroutes to the next best processor in milliseconds. Up to 50% recovery on failed renewals. Directly addresses the "card processor will not accept" errors flooding user forums.
Desc_Yuno_Cap3: Unlocks Roku's fastest-growing international markets: Pix and Boleto in Brazil (4.1% of accounts, 47% growth), OXXO and SPEI in Mexico (5.8%), SEPA in Germany (4.8%), Interac in Canada (3.0%), UPI in India. One API, 1,000+ methods. No per-market build.
Desc_Yuno_Cap4: Single dashboard across Roku Billing Services, PayPal developer payouts, and all card networks. Real-time ARPU analytics per market, centralized reconciliation of 100M+ household subscriptions. Millisecond anomaly detection via Monitors to catch billing cascades before mass churn.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Roku at a glance:**
- Streaming devices and platform company, NASDAQ: ROKU, HQ San Jose, California
- Revenue: $4.737B (2025), up 15.18% YoY. Platform revenue: $4.145B (85-90% of total). Q4 2025: $1.224B platform revenue (first time above $1.2B)
- 2026 guidance: $5.5B total revenue (+16%), $4.89B platform revenue (+18%), $635M adjusted EBITDA (+50% YoY)
- 100M+ streaming households (crossed April 2026), up from 89.8M end of 2024
- ARPU: $41.49, targeting $45 annually
- The Roku Channel: #2 free ad-supported streaming app in US (6.3% of all TV streaming, Dec 2025)
- Average daily streaming: 4.2 hours per household
- International growth: non-US accounts +37.8% YoY vs. +6.5% domestic
- Roku Pay: proprietary billing system, 20% revenue share from developers, handles all card processing, currency conversion, taxes
- 45 OEM brand partnerships across 17 countries
- Swung to profitability in Q4 2025

**Confirmed PSPs and Partners:**
- Roku Billing Services: proprietary payment processor for all Roku Pay transactions
- PayPal: developer payout mechanism (developers receive sales revenue via PayPal)
- Card networks: Visa, Mastercard, American Express, Discover
- Credit cards must have billing address from: US, Mexico, China, Israel, Singapore, UK, Canada, Australia, Germany, Brazil
- No payment orchestrator detected
- No secondary acquirer or failover processor identified

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (68.2% of active accounts)
  Supported: Visa/MC/Amex/Discover, PayPal
  Missing: ACH, Cash App Pay, Venmo, Apple Pay on platform
  Note: Highest ARPU market; 4.2 hours daily streaming per household

MARKET 2: Mexico (5.8% of accounts, top-selling TV OS)
  Supported: Credit cards, Mexican peso billing
  Missing: OXXO, SPEI, CoDi, Mercado Pago
  Note: #1 international market. Cash and OXXO dominate; credit card penetration ~25%

MARKET 3: Germany (4.8% of accounts, 51.1% YoY growth)
  Supported: Credit cards
  Missing: SEPA Direct Debit, Sofort, Giropay, iDEAL
  Note: Fastest-growing European market. ~35% credit card penetration; SEPA backbone of subscriptions

MARKET 4: Brazil (4.1% of accounts, 47.2% YoY growth)
  Supported: Credit cards, BRL billing
  Missing: Pix, Boleto, local installment cards
  Note: Pix handles 70%+ of Brazilian digital payments. Without it, Roku cannot convert the mass market

MARKET 5: United Kingdom (3.4% of accounts)
  Supported: Credit/debit cards
  Missing: Open Banking, Faster Payments, Direct Debit
  Note: Vestel partnership driving Roku TV adoption. Direct Debit is UK subscription standard

**Key issues and vulnerabilities:**
- Card-only payment model in markets where cards are not dominant (Mexico, Brazil, Germany)
- ARPU stagnation ($41.49, only +3.9% YoY) despite 100M+ households
- User complaints about "card processor will not accept" errors spanning years of community forums
- Region/billing address mismatch blocks valid international cards
- Prepaid, gift, and some debit cards not accepted
- 20% developer revenue share is high vs. Apple (15-30%) and Google (15-30%) but without the APM breadth
- International ARPU significantly below US ARPU, limiting platform revenue growth per household

**Key meeting angles:**
1. **100M household milestone** | Just crossed 100M streaming households globally. Payment infrastructure has not kept pace with device footprint
2. **International is the growth engine** | Non-US accounts growing 37.8% YoY vs. 6.5% domestic. But no local APMs in any international market
3. **ARPU unlock** | $41.49 ARPU stuck because international households convert and retain at lower rates. Local payment methods directly lift both metrics
4. **Mexico #1 international market** | Top-selling TV OS in Mexico but only accepts credit cards in a cash-dominant economy. OXXO and SPEI are table stakes
5. **Brazil explosive growth** | 47.2% YoY growth but no Pix. 70%+ of Brazilian digital payments via Pix. Massive conversion gap
6. **Developer ecosystem** | 20% rev share but zero multi-acquirer routing. Developers lose revenue to Roku's single-processor billing failures
7. **Profitability protection** | Just achieved profitability. Payment failures and international churn threaten the margin expansion narrative

**Sources:**
- [Roku Logo (Wikimedia SVG)](https://commons.wikimedia.org/wiki/File:Roku_logo.svg)
- [Roku Q4 2025 Earnings (Variety)](https://variety.com/2026/tv/news/roku-q4-2025-earnings-2026-revenue-forecast-1236660031/)
- [Roku Q4 2025 Earnings (TheDesk)](https://thedesk.net/2026/02/roku-q4-2025-earnings-report/)
- [Roku 100M Active Households](https://thedesk.net/2026/04/roku-100-million-households/)
- [Roku Active Accounts Statistics 2026](https://www.apprupt.com/roku-active-accounts-statistics)
- [Roku International ARPU Growth (Quartz)](https://qz.com/roku-s-international-footprint-expands-can-arpu-growth-accelerate)
- [Roku Revenue History (MacroTrends)](https://www.macrotrends.net/stocks/charts/ROKU/roku/revenue)
- [Roku Key Stats](https://stockdividendscreener.com/entertainment/roku-active-accounts-streaming-hours-and-arpu-numbers/)
- [How Roku Pay Works (Developer)](https://developer.roku.com/docs/developer-program/roku-pay/how-roku-pay-works.md)
- [Roku Billing Services Overview](https://wwwimg.roku.com/docs/roku_billing_services_program_overview.pdf)
- [Roku Payment Issues (Community)](https://community.roku.com/t5/Account-payments-subscriptions/Billing-Dispute-Customer-Service/td-p/942783)
- [Roku Card Declined (Community)](https://community.roku.com/t5/Accounts-Billing-Orders/Credit-Card-Declined/td-p/524430)
- [Roku Payment Update Issues](https://support.roku.com/article/360012288753)
- [Roku Growth Strategy (PortersFiveForce)](https://portersfiveforce.com/blogs/growth-strategy/roku)
- [Roku Shareholder Letter Q4 2024](https://image.roku.com/c3VwcG9ydC1B/4Q24-Shareholder-Letter.pdf)
