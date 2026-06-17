# VISTA GROUP | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Vista Group
=======================================

Logo: https://cdn.brandfetch.io/idM-JsXpVf/w/512/h/512/theme/dark/icon.jpeg
Nombre merchant: Vista Group

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Single Acquirer Dependency
Tittle_Pain Point_2: Global APM Coverage Gaps
Tittle_Pain Point_3: Fragmented Legacy Stack
Tittle_Pain Point_4: Concession Revenue Leakage
Tittle_Pain Point_5: Cloud Migration Friction

Desc_Pain Point_1: Vista Payments launched in January 2026 with Adyen as its exclusive payment partner. Four pilot clients are live, but 5,500+ cinemas in 80+ countries will depend on a single acquirer for both online ticketing and in-venue POS. If Adyen experiences regional downtime or declines, there is no fallback processor. For time-sensitive movie ticket purchases, a failed payment means an empty seat.
Desc_Pain Point_2: Cinema audiences are global. Chinese tourists (180M+ outbound travelers), Indian moviegoers (1.4B population), Latin American audiences, and Southeast Asian markets all have dominant local wallets. Vista's Adyen-only integration limits APM availability to what Adyen supports in each market. Cinemas in 80+ countries cannot offer Pix, UPI, GrabPay, or Dana without additional integrations.
Desc_Pain Point_3: 65% of Vista's enterprise client sites (2,900+ cinemas) still run Vista Classic, the on-premise legacy system. These sites manage payments through a patchwork of local acquirers, bank terminals, and regional processors with no centralized orchestration. Each cinema chain negotiates its own processing rates, manages its own PCI compliance, and reconciles payments independently.
Desc_Pain Point_4: Cinemas earn 40-50% of revenue from concessions (food, drinks, merchandise). In-venue concession payments at kiosks and counters often run on separate POS terminals disconnected from the ticketing system. No unified view of per-customer spend across tickets and concessions. Cash still represents 10% of transactions, slowing lines and increasing reconciliation complexity.
Desc_Pain Point_5: Vista is migrating 4,400+ remaining sites from Vista Classic to Vista Cloud. Each migration requires payment infrastructure reconfiguration. Cinema chains moving to cloud must reconnect payment terminals, recertify PCI compliance, and renegotiate processor contracts. Vista Payments with Adyen is the intended solution, but single-acquirer lock-in during migration creates risk.

SLIDE 1: PSP TOPOLOGY

PSP_1: Adyen (Vista Payments, exclusive)
PSP_2: Windcave (Veezi, independent cinemas)
PSP_3: Legacy local acquirers (per-market)
PSP_4: Regional bank terminals (in-venue)
PSP_5: N/A

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Alipay
Local_M_2: WeChat Pay
Local_M_3: Pix
Local_M_4: UPI
Local_M_5: GrabPay
Local_M_6: Dana
Local_M_7: OXXO
Local_M_8: Mercado Pago
Local_M_9: Toss Pay
Local_M_10: TrueMoney

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Recovery
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across Adyen, Windcave, and legacy local acquirers for every ticket and concession purchase. Each transaction routed to the highest-performing acquirer for that card BIN, issuer, and market. Across 5,500+ cinemas in 80+ countries processing millions of ticket sales, smart routing delivers +3 to 10% authorization uplift. For a $164M revenue business projecting $15M in payment revenue, even 3% uplift generates significant incremental volume.
Desc_Yuno_Cap2: Automatic cascade across Vista's multiple payment partners eliminates single-acquirer risk. When Adyen declines a ticket purchase, Yuno reroutes to Windcave or a local acquirer in milliseconds. Up to 50% recovery on soft declines via instant retry. NOVA AI recovers up to 75% of failed transactions. For time-sensitive cinema purchases (showtime in 30 minutes), a failed payment means an unsold seat with zero recovery opportunity.
Desc_Yuno_Cap3: Activates the APMs Vista's cinema network needs across 80+ countries: Alipay and WeChat Pay for Chinese moviegoers (world's largest box office market), Pix for Brazilian cinemas, UPI for India's 500M+ digital payment users, GrabPay and Dana for Southeast Asian theaters, OXXO and Mercado Pago for Mexican and Latin American audiences, Toss Pay for South Korean cinemas. One API, 1,000+ payment methods across every market Vista serves.
Desc_Yuno_Cap4: One dashboard replacing Vista's fragmented Adyen + Windcave + legacy acquirer stack. Real-time approval rate monitoring across 5,500+ cinema sites in 80+ countries, centralized reconciliation for ticket sales, concessions, refunds, and group bookings, millisecond anomaly detection via Monitors. Simplifies the Vista Classic to Vista Cloud migration by providing a processor-agnostic payment layer that works regardless of the underlying cinema platform version.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Vista Group at a glance:**
- Model: Cinema management software (ticketing, scheduling, concessions, payments, analytics, film distribution)
- Products: Vista Cloud, Vista Classic, Veezi (independent cinemas), Movio (data analytics), Maccs (film distribution), Numero (box office reporting), Powster (creative studio), Flicks (moviegoer guide)
- Revenue: $164.3M (FY2025, record), up 10% YoY
- Recurring Revenue: $147.2M (90% of total), up 9%
- SaaS Revenue: $69.7M, up 25%
- ARR: $163M, up 12%
- EBITDA: $28.2M, up 31%; 17.2% margin (up from 14.4%)
- Operating Cashflow: $27.8M, up 65%
- Net Profit: $2.6M (return to profitability after $600K loss in FY2024)
- 2026 Guidance: $176M to $182M revenue (10-13% growth); EBITDA margin 18-20%
- Cinemas Served: 5,500+ in 80+ countries
- Large Cinema Market Share: 38%
- Vista Cloud Sites Live: 1,557 (35% of enterprise client sites)
- Enterprise Client Sites Total: ~4,400+
- Founded: 1996, Auckland, New Zealand by Murray Holdaway
- Listed: NZX and ASX (ticker: VGL)
- Market Cap: ~NZ$564M
- CEO: Stuart Dickinson (appointed April 2023, 25+ years tech leadership)
- CTO: Chris South
- CFO: Matt Cawte
- Co-Founder: Murray Holdaway (2024 NZ Hi-Tech "Flying Kiwi" Award winner)

**Vista Payments (Launched January 2026):**
- Embedded payment solution natively integrated into Vista's platform
- Exclusive partnership with Adyen for payment processing and acquiring
- Covers both online (Card Not Present) and in-venue (Point of Sale) transactions
- Four pilot clients contracted, two already transacting
- Further go-lives scheduled throughout 2026
- Expected to contribute $15M in annual recurring revenue (net of processing fees)
- Agency accounting basis (net take rate recognized as revenue)
- Features: end-to-end encryption, PSD2 and PCI DSS compliance, card-testing protection, matched refunds, granular reporting via Horizon analytics
- Industry-leading payment terminals, hardware proven and rigorously tested

**Vista Cloud Migration:**
- 1,557 sites live (35% of enterprise client base)
- Major commitments: ODEON Cinemas Group (312 sites), Kinepolis (109 sites), Village Cinemas Australia (24 sites)
- Target: accelerate onboarding through 2026
- Mission-critical workflows: ticketing, scheduling, concessions, payments
- 65% of sites still on Vista Classic (on-premise legacy system)

**Veezi (Independent Cinemas):**
- Cloud-based cinema management for small to medium cinemas (under 20 screens)
- Uses Windcave as payment gateway (not Adyen)
- Modular pricing, no setup fees, no contracts

**Payments Infrastructure:**
- Adyen: exclusive payment processor for Vista Payments (online + in-venue)
- Windcave: payment gateway for Veezi (independent cinemas)
- Legacy local acquirers: various regional processors for Vista Classic sites
- No payment orchestration across multiple acquirers
- No smart routing between Adyen, Windcave, and local acquirers

**Payment Methods (via Adyen):**
- Credit/debit cards: Visa, Mastercard, Amex
- Apple Pay, Google Pay (via Adyen)
- Local methods limited to Adyen's per-market availability
- Cinemark (Adyen client example): cards, Apple Pay, Google Pay, PayPal, Venmo, Sezzle BNPL

**Top 5 Markets Gap Analysis:**

MARKET 1: Europe (ODEON 312 sites, Kinepolis 109 sites, major market)
  Currently offer: Visa/MC, Apple Pay, Google Pay (via Adyen)
  Missing: Cartes Bancaires (France), iDEAL (Netherlands), Bancontact (Belgium), Bizum (Spain), MB WAY (Portugal), Klarna, Open Banking
  ODEON operates in UK, Ireland, Portugal, Spain. Kinepolis across Belgium, France, Netherlands, Spain. Local APMs are critical for European moviegoers.

MARKET 2: Asia Pacific (largest box office region, China #1 market)
  Currently offer: Visa/MC via local acquirers
  Missing: Alipay (1.3B+ users), WeChat Pay (900M+ users), GrabPay, GCash, Dana, TrueMoney, Toss Pay, KakaoPay
  China is the world's largest box office market. Southeast Asian cinemas need GrabPay, Dana, GCash. South Korean cinemas need Toss Pay and KakaoPay.

MARKET 3: Latin America (growing cinema market, Cinepolis presence)
  Currently offer: Visa/MC via local acquirers
  Missing: Pix (Brazil, 150M+ users), OXXO (Mexico), Mercado Pago, PSE (Colombia), Nequi
  Latin America's cinema market is one of the fastest growing globally. Mexican and Brazilian moviegoers rely on local payment methods.

MARKET 4: India (world's largest cinema-going population)
  Currently offer: Visa/MC, local bank terminals
  Missing: UPI (500M+ users), Paytm, PhonePe, RuPay
  India sells 1.5B+ cinema tickets annually, more than any other country. UPI dominates digital payments.

MARKET 5: Middle East / Africa (growing theatrical markets)
  Currently offer: Visa/MC via local acquirers
  Missing: Mada (Saudi Arabia), Fawry (Egypt), M-Pesa (Kenya/East Africa), Benefit Pay (Bahrain)
  Saudi Arabia and UAE are investing heavily in cinema infrastructure. VOX Cinemas, AMC, and Cinepolis expanding across the region.

**Payment Pain Points:**
1. Single-acquirer dependency on Adyen for Vista Payments (no failover)
2. 65% of sites on legacy Vista Classic with fragmented local payment setups
3. No orchestration across Adyen, Windcave, and regional acquirers
4. Cinema concession payments often disconnected from ticketing payments
5. Cash still 10% of transactions, slowing lines and complicating reconciliation
6. No BNPL for premium cinema experiences (VIP screens, event cinema, private bookings)
7. Limited local APMs for Asian, Latin American, and African markets
8. Cloud migration requires payment infrastructure reconfiguration per site
9. No smart routing to optimize authorization rates across markets
10. Each cinema chain independently manages PCI compliance and processor contracts

**Key Meeting Angles:**
1. **5,500+ cinemas, 80+ countries, single acquirer**: Vista Payments launched with Adyen-only. Yuno adds multi-acquirer routing without replacing Adyen, providing failover and optimization from day one
2. **$15M payment revenue opportunity**: Vista projects $15M ARR from embedded payments. Yuno's smart routing (+3-10% auth uplift) directly increases the transaction volume that generates that revenue
3. **World's largest box office markets need local APMs**: China (Alipay, WeChat Pay), India (UPI), Brazil (Pix), Mexico (OXXO). Yuno's 1,000+ APMs via one API unlocks these markets. McDonald's gained +4.7% auth rate with Yuno
4. **Vista Classic to Vista Cloud migration**: 2,900+ sites migrating need a processor-agnostic payment layer. Yuno works regardless of underlying platform version, simplifying migration
5. **Concession + ticketing unification**: One orchestration layer for both ticket sales and in-venue concessions. InDrive achieved 90% approval across 10 markets with Yuno
6. **Cinema is time-sensitive commerce**: Movie starts in 30 minutes, payment fails, seat stays empty. Failover (50% recovery on soft declines) and NOVA AI (75% recovery) are critical for cinema
7. **38% global market share**: Vista is the dominant cinema software provider. Adding payment orchestration strengthens their competitive moat against NCR, Arts Alliance, and other competitors
8. **Co-founder is a New Zealand tech icon**: Murray Holdaway won the 2024 NZ Hi-Tech "Flying Kiwi" Award. Vista has deep roots in New Zealand tech innovation

**Sources:**
- [Vista Group Homepage](https://vista.co/)
- [Vista Payments](https://vista.co/vista-payments)
- [Vista Group 2025 Results](https://vista.co/insights/vista-group-2025-results)
- [Vista Group Investor Centre](https://vistagroup.co.nz/investor-centre)
- [Vista Group Board and Management](https://vistagroup.co.nz/board-management)
- [Vista Group Wikipedia](https://en.wikipedia.org/wiki/Vista_Group)
- [Vista Group Embedded Payments Partnership (Reseller News)](https://www.reseller.co.nz/article/4040075/vista-group-finalises-embedded-payments-partnership-to-boost-revenue-by-15m.html)
- [Adyen and Vista Partnership](https://www.adyen.com/partners/vista)
- [Adyen Powers Cinemark Omnichannel Payments](https://www.adyen.com/press-and-media/adyen-to-power-omnichannel-payments-at-cinemark)
- [PYMNTS: Adyen Cinemark Payment Methods](https://www.pymnts.com/news/payment-methods/2024/adyen-offers-cinemark-moviegoers-more-payment-options)
- [ODEON Signs for Vista Cloud](https://vista.co/insights/odeon-cinemas-group-signs-for-vista-cloud)
- [Kinepolis Vista Cloud Agreement](https://www.dcinematoday.com/dc/pr?newsID=6509)
- [Windcave and Veezi Integration](https://windcave.com/Veezi.html)
- [Vista Group Companies](https://vistagroup.co.nz/group-companies)
- [Edgar Dunn: Cinema Industry Payments](https://www.edgardunn.com/articles/cinema-industry-payments-innovations-challenges-and-strategies)
- [Capterra: Vista Cinema](https://www.capterra.com/p/67393/Vista-Cinema/)
- [Scoop: Vista Group 2025 Results](https://www.scoop.co.nz/stories/BU2602/S00422/vista-group-reports-record-2025-results-as-client-onboarding-accelerates.htm)
- [Murray Holdaway Flying Kiwi Award](https://vistagroup.co.nz/blog/vista-group-co-founder-and-director-wins-nz-hi-techs-flying-kiwi-award)
