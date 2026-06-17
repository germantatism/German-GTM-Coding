# TRIP.COM GROUP | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Trip.com Group
=======================================

Logo: https://logo.clearbit.com/trip.com
Nombre merchant: Trip.com Group

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Multi-PSP Fragmentation
Tittle_Pain Point_2: Local APM Coverage Gaps
Tittle_Pain Point_3: Cross-Border FX Drag
Tittle_Pain Point_4: Auth Rate Blind Spots
Tittle_Pain Point_5: Payment Reconciliation Load

Desc_Pain Point_1: Trip.com runs Worldline, Checkout.com (since March 2026), and additional processors across Ctrip, Qunar, Skyscanner, and Trip.com with no unified orchestration. Each brand manages its own payment stack independently, creating routing silos across RMB 1.1T in gross bookings (2025).
Desc_Pain Point_2: Trip.com accepts cards, PayPal, Apple Pay, Google Pay, and Alipay/WeChat Pay (China only), but lacks critical local APMs in growth markets. No Pix in Brazil, no iDEAL in Netherlands, no Bizum in Spain, no BLIK in Poland, no UPI on Trip.com (only Ctrip), no GrabPay in SEA. International bookings grew 60% YoY yet checkout coverage lags.
Desc_Pain Point_3: Operating in 39 countries with 24 languages, Trip.com processes bookings in dozens of currencies. On RMB 1.1T (~$155B) gross bookings, unoptimized FX routing on cross-border hotel and flight payments creates margin erosion on every international transaction, especially as outbound bookings hit 140% of 2019 levels.
Desc_Pain Point_4: Users report card declines and payment failures across Trustpilot and community forums. Transactions fail without smart retry or cascade to alternate processors. With Worldline providing "automated rerouting" on only part of the stack, the rest of Trip.com's volume lacks failover coverage.
Desc_Pain Point_5: Four brands (Ctrip, Trip.com, Qunar, Skyscanner), multiple PSPs (Worldline, Checkout.com, others), and crypto payments via Triple-A create a complex settlement web. Reconciling hotel payouts, airline BSP, and refunds across all processors without a unified layer generates operational overhead at scale.

SLIDE 1: PSP TOPOLOGY

PSP_1: Worldline
PSP_2: Checkout.com
PSP_3: Triple-A (crypto)
PSP_4: PayPal

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix (Brazil)
Local_M_2: iDEAL (Netherlands)
Local_M_3: Bizum (Spain)
Local_M_4: BLIK (Poland)
Local_M_5: UPI (India)
Local_M_6: GrabPay (SEA)
Local_M_7: Mercado Pago (LATAM)
Local_M_8: OXXO (Mexico)
Local_M_9: DANA (Indonesia)
Local_M_10: Bancontact (Belgium)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Recovery
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Per-transaction routing across Worldline, Checkout.com, and all processors. Each hotel booking, flight purchase, and package tour payment routed to the highest performing acquirer for that card BIN, issuer, and market. On RMB 1.1T gross bookings across 39 countries, smart routing delivers +3 to 10% auth uplift. InDrive achieved 90% approval across 10 markets with Yuno.
Desc_Yuno_Cap2: Automatic cascade across Trip.com's multiple PSPs eliminates single-processor dependency. When Worldline declines, Yuno reroutes to Checkout.com in milliseconds. Up to 50% recovery on soft declines via instant retry. NOVA AI recovers up to 75% of failed transactions. Critical for high-value flight and hotel bookings where a single decline means lost revenue.
Desc_Yuno_Cap3: Activates the APMs Trip.com still lacks in growth markets: Pix in Brazil (150M+ users), iDEAL in Netherlands (70% share), Bizum in Spain (25M+ users), BLIK in Poland (17M+ users), UPI in India (400M+ users), GrabPay and DANA in SEA. One API, 1,000+ payment methods, no custom integration per market. International bookings grew 60% YoY but checkout still blocks non-card travelers.
Desc_Yuno_Cap4: One dashboard unifying Ctrip, Trip.com, Qunar, and Skyscanner payment flows. Real-time approval monitoring across all PSPs and brands, centralized reconciliation for hotel payouts, airline settlements, and refunds in 40+ currencies. McDonald's gained +4.7% auth rate ($3.2M impact) with Yuno. Rappi integrated with zero implementation friction. Wingo achieved +14% auth rate improvement.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Trip.com Group at a glance:**
- China's largest and world's second-largest online travel agency by revenue
- Brands: Ctrip (China domestic), Trip.com (international), Qunar (China meta-search), Skyscanner (global flights)
- Revenue: RMB 62.4B (~$8.9B) FY 2025, +17% YoY
- Gross Bookings (OTA): ~RMB 1.1T (~$155B) in 2025
- International OTA bookings: +60% YoY growth in 2025
- Inbound travel bookings: +100% YoY
- Outbound bookings: 140% of 2019 pre-COVID levels
- Operating profit margin: ~33% (Q3 2025)
- Net income: RMB 19.9B (Q3 2025, includes investment gain)
- Operates in 39 countries/regions, 24 languages, 200+ country coverage
- 5,000+ cities, 3M+ routes, accommodation across Asia, Europe, North America
- NASDAQ: TCOM, HKEX: 9961, market cap ~$35B+
- Founded: 1999, Shanghai. CEO: Jane Sun (since 2016). Chairman: James Jianzhang Liang

**Revenue by Segment (FY 2025):**
- Accommodation: RMB 26.1B ($3.7B), +21% YoY, 42% of revenue
- Transportation Ticketing: RMB 22.5B ($3.2B), +11% YoY, 36% of revenue
- Packaged Tours: RMB 4.7B ($670M), +8% YoY
- Corporate Travel: RMB 2.8B ($405M), +13% YoY

**Leadership:**
- James Jianzhang Liang: Co-founder and Executive Chairman
- Jane Sun (Jie Sun): CEO since November 2016
- Xing Xiong: COO
- Cindy Xiaofan Wang: CFO
- Wang Zhe: VP, Trip.com Group (quoted in Checkout.com partnership announcement)
- Tao Song: CTO of Trip.Biz division, also CEO of Trip.Biz
- No dedicated VP of Payments identified publicly

**Confirmed PSPs and Payment Partners:**
- Worldline: Strategic partner for cross-border payments. Provides card payments, eWallets, prepaid cards, bank transfers, real-time banking, and automated rerouting for declined payments. Supports SEA and LATAM expansion
- Checkout.com: Partnership announced March 2026. Digital card payment services in UK, Japan, Saudi Arabia. Plans to expand to North America, Europe, Australia, New Zealand. Standalone 3DS, Vault, IDV, issuing solutions
- Triple-A: Crypto payment processor. Supports USDT and USDC stablecoins across Ethereum, Tron, Polygon, Solana, Arbitrum One, and TON (launched December 2025)
- PayPal: Direct integration as payment method
- No payment orchestrator detected across the group's four brands

**Payment Methods Currently Supported:**
- Credit/Debit cards: Visa, Mastercard, Amex, JCB, UnionPay, Discover, Diners Club International
- Digital wallets: PayPal, Apple Pay, Google Pay
- China-specific: Alipay, WeChat Pay (primarily Ctrip/Chinese mainland users)
- BNPL: Afterpay, Zip Pay, Klarna (referenced)
- Loyalty: Trip Coins, Gift Cards
- Crypto: USDT, USDC (via Triple-A)
- Samsung Financing: TD Bank (referenced for Samsung, not Trip.com)

**Missing Local Payment Methods (Gap Analysis):**

MARKET 1: Brazil (LATAM growth market)
  Currently offer: Cards, PayPal
  Missing: Pix, Boleto Bancario, Mercado Pago
  Pix has 150M+ users and processes 60%+ of Brazilian e-commerce. Essential for travel bookings.

MARKET 2: India (massive outbound travel market)
  Currently offer: Cards, PayPal (Trip.com). UPI available on Ctrip only
  Missing: UPI on Trip.com, Paytm, PhonePe, Netbanking
  UPI has 400M+ active users. India is one of the fastest growing outbound travel markets.

MARKET 3: Southeast Asia (key expansion region)
  Currently offer: Cards, PayPal, Apple Pay, Google Pay
  Missing: GrabPay, DANA, OVO, GCash, PromptPay, MoMo, ShopeePay
  Digital wallets dominate SEA payments. Thailand, Malaysia, Indonesia are Trip.com's fastest growing source markets.

MARKET 4: Europe (expansion via Skyscanner + Checkout.com)
  Currently offer: Cards, PayPal, Klarna
  Missing: iDEAL (NL, 70% share), Bizum (ES, 25M users), BLIK (PL, 17M users), Bancontact (BE), Giropay (DE)
  Bank-based and mobile payments dominate European travel bookings.

MARKET 5: Mexico/Colombia (LATAM)
  Currently offer: Cards, PayPal
  Missing: OXXO, SPEI, Mercado Pago, PSE, Nequi
  OXXO handles 55%+ of Mexican e-commerce cash payments. PSE covers 60%+ of Colombian online payments.

MARKET 6: Japan (Checkout.com implementation market)
  Currently offer: Cards, JCB
  Missing: Konbini, PayPay (62M users), LINE Pay (40M users), Rakuten Pay
  Konbini (convenience store) payments used by 35%+ of Japanese online shoppers.

**Payment Pain Points (documented):**
1. Card declines: Trustpilot reviews and forums document payment failures across Trip.com
2. Currency discrepancy: Users charged different amounts than displayed (Turkish lira example, January 2025)
3. Refund delays: Complex multi-PSP refund flows across airlines, hotels, and payment processors
4. China vs. international payment gap: Alipay and WeChat Pay only on Ctrip/Chinese users. Trip.com international lacks these
5. No unified failover: Worldline has "automated rerouting" but only for its own transactions. No cross-PSP cascade
6. Checkout.com only just launched (March 2026): UK, Japan, Saudi Arabia. Still expanding. Integration incomplete
7. Crypto payments niche: USDT/USDC via Triple-A serves a small segment, not mainstream travelers

**Key Meeting Angles:**
1. **RMB 1.1T gross bookings, no orchestration**: Four brands, 3+ PSPs, crypto, and no unified routing layer. Yuno provides single-API orchestration across all channels
2. **60% international booking growth demands local APMs**: Fastest growing segment lacks Pix, iDEAL, Bizum, UPI, GrabPay. Yuno's 1,000+ APMs via single API unlocks conversion
3. **Checkout.com just started (March 2026)**: Integration is incomplete and limited to 3 markets. Yuno can accelerate global payment coverage immediately
4. **Worldline provides partial rerouting only**: No cross-PSP failover. Yuno cascades across all processors. NOVA AI recovers up to 75% of failed transactions
5. **High-value transactions**: Average flight + hotel bookings are $500+. Each declined transaction is significant lost revenue. Smart routing + failover maximizes recovery
6. **Multi-brand unification**: Ctrip + Trip.com + Qunar + Skyscanner all running separate stacks. One Yuno dashboard for real-time monitoring and reconciliation
7. **SEA is top growth region**: Thailand, Malaysia, Indonesia are fastest growing source markets but Trip.com lacks GrabPay, DANA, OVO. Wingo gained +14% auth with Yuno

**Sources:**
- [Trip.com FY 2025 Financial Results](https://investors.trip.com/news-releases/news-release-details/tripcom-group-limited-reports-unaudited-fourth-quarter-and-5)
- [Trip.com FY 2025 Results (PR Newswire)](https://www.prnewswire.com/news-releases/tripcom-group-limited-reports-unaudited-fourth-quarter-and-full-year-of-2025-financial-results-302696643.html)
- [Trip.com FY 2024 Financial Results](https://investors.trip.com/news-releases/news-release-details/tripcom-group-limited-reports-unaudited-fourth-quarter-and-4)
- [Trip.com Q3 2025 Results](https://ctripcominternationalltd.gcs-web.com/news-releases/news-release-details/tripcom-group-limited-reports-unaudited-third-quarter-2025)
- [Trip.com + Checkout.com Partnership (Checkout.com)](https://www.checkout.com/newsroom/trip-com-teams-up-with-checkout-com-to-simplify-payments-for-global-travelers)
- [Trip.com + Checkout.com (PR Newswire)](https://www.prnewswire.com/apac/news-releases/tripcom-teams-up-with-checkoutcom-to-simplify-payments-for-global-travelers-302723427.html)
- [Trip.com + Worldline Partnership](https://worldline.com/en/home/main-navigation/resources/all-customer-stories/trip-com-customer-story)
- [Trip.com Payment Methods](https://www.trip.com/ask/questions/trip.com-payment-methods.html)
- [Trip.com Stablecoin Payments (ChainCatcher)](https://www.chaincatcher.com/en/article/2232620)
- [Trip.com Leadership](https://group.trip.com/about/leadership)
- [Trip.com Investor Relations](https://investors.trip.com/)
- [Trip.com Wikipedia](https://en.wikipedia.org/wiki/Trip.com)
- [Skift: Trip.com Q1 2025 Inbound Boom](https://skift.com/2025/05/20/trip-com-group-rides-ai-inbound-boom-and-older-travelers-to-strong-quarter/)
- [ChinaTravelNews: Trip.com 2025 Results](https://www.chinatravelnews.com/article/189360)
- [Trip.com International Expansion: 1,100 Positions in 23 Countries](https://equalocean.com/news/2025061321573)
- [247 Wall St: Trip.com Q4 2025](https://247wallst.com/investing/2026/02/26/trip-com-has-15-billion-in-cash-and-a-25-ytd-loss-that-math-doesnt-add-up/)
- [Fintech Singapore: Trip.com + Checkout.com](https://fintechnews.sg/128110/payments/trip-com-checkout-com/)
- [Trustpilot: Trip.com Reviews](https://www.trustpilot.com/review/trip.com)
- [MacroTrends: Trip.com Profit Margins](https://www.macrotrends.net/stocks/charts/TCOM/trip-group/profit-margins)
