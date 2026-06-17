# ELECTRONIC ARTS | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Electronic Arts
=======================================

Logo: https://media.contentapi.ea.com/content/dam/ea/publisher-portal/ea-logo-black.svg
Nombre merchant: Electronic Arts

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Multi-PSP Silos
Tittle_Pain Point_2: Cross-Border Auth Loss
Tittle_Pain Point_3: Checkout Decline Loops
Tittle_Pain Point_4: Zero Failover Logic
Tittle_Pain Point_5: LATAM/APAC APM Gaps

Desc_Pain Point_1: Ingenico/Worldline (global), BoaCompra (LATAM), KCP (Korea) run as isolated stacks. No unified routing across $4.4B in annual microtransaction volume. Each PSP managed independently.
Desc_Pain Point_2: Brazil and Mexico contracts run through EA Swiss Sarl (Geneva) with no local entities. Cross-border acquiring from Switzerland inflates decline rates and processing costs in key LATAM markets.
Desc_Pain Point_3: Users report "payment method declined" errors, double charges, and PayPal failures across EA Forums and Trustpilot. No in-flow retry, no APM fallback, no decline recovery automation.
Desc_Pain Point_4: Ingenico is the sole global card acquirer with no cascade. Oct 2025 outage hit all EA services. 57+ outages in 4 months. Zero automated rerouting to backup processors.
Desc_Pain Point_5: No Pix in Brazil, no UPI in India, no OXXO in Mexico, no Konbini in Japan. Forum users explicitly request local methods. 60% of revenue is international yet APM coverage is minimal.

SLIDE 1: PSP TOPOLOGY

PSP_1: Ingenico / Worldline
PSP_2: BoaCompra (PagSeguro)
PSP_3: KCP (Korea)
PSP_4: Klarna (US, intermittent)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: UPI
Local_M_3: OXXO
Local_M_4: Boleto
Local_M_5: Konbini
Local_M_6: PayPay
Local_M_7: SPEI
Local_M_8: GrabPay
Local_M_9: DANA
Local_M_10: GCash

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing Engine
Tittle_Yuno_Cap2: Failover + Retry Recovery
Tittle_Yuno_Cap3: 1,000+ Local APMs
Tittle_Yuno_Cap4: Unified Orchestration Layer

Desc_Yuno_Cap1: Route each of EA's ~440M+ annual microtransactions to the optimal acquirer per card BIN, issuer, and market. With $4.4B in live services revenue, even a 1% auth uplift recovers ~$44M. Real-time performance scoring across Ingenico, BoaCompra, and KCP eliminates guesswork. InDrive achieved 90% approval rates.
Desc_Yuno_Cap2: Automatic cascade across Ingenico, BoaCompra, and KCP. When one acquirer declines or goes down (Oct 2025 outage), Yuno reroutes in milliseconds. NOVA AI recovers up to 75% of soft declines. Livelo recovered 50% of failed transactions. Turns EA's broken Klarna and PayPal errors into completed purchases.
Desc_Yuno_Cap3: Activate missing methods across EA's 60+ country footprint: Pix and Boleto in Brazil, UPI in India, OXXO and SPEI in Mexico, Konbini and PayPay in Japan, GrabPay and DANA in Southeast Asia. One API, zero per-market engineering sprints. InDrive launched 10 LATAM markets in under 8 months.
Desc_Yuno_Cap4: Replace EA's siloed Ingenico + BoaCompra + KCP stacks with one real-time dashboard. Centralized approval monitoring, unified reconciliation across all providers and currencies, millisecond anomaly detection. Rappi cut analyst resolution time by 80%. One integration to rule the entire payment stack.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Electronic Arts at a glance:**
- NASDAQ: EA. Global video game publisher headquartered in Redwood City, California
- FY2025 Revenue: $7.463B total ($3.08B North America / 41%, $4.39B International / 59%)
- FY2025 Net Bookings: $7.355B. FY2026 Guidance: $7.6B to $8.0B
- Live Services Revenue: ~$4.4B (75% of net bookings), of which Ultimate Team alone approaches ~$1B annually
- 78% of total game units sold in FY2025 were digital
- 200M+ game downloads in 2025, leading all PC/console publishers
- Mobile segment: $1.1B in net revenue (15% of total)
- $55B acquisition by PIF/Silver Lake/Affinity Partners announced September 2025, expected close Q2 2026. Largest gaming buyout in history.
- CEO goal: increase microtransaction spend 10 to 20% using AI personalization
- Net Income FY2025: $1.121B
- Key upcoming titles: Battlefield 6, Project Rene (The Sims mobile first), skate.
- EA Sports FC franchise: record net bookings in FY25. American Football franchise exceeded $1B in net bookings
- 36 offices across 18+ countries

**Confirmed PSPs:**
- Ingenico / Worldline (formerly GlobalCollect): primary global card processing gateway. "Ingenico Hosted Card" listed on EA Help
- BoaCompra (PagSeguro/UOL): LATAM card processing. "BoaCompra Credit Card" listed on EA Help
- KCP (Korea Credit Card Processing): Korean local acquiring. "KCP Credit Card" listed on EA Help
- Klarna: US BNPL (intermittent availability, multiple forum threads report it not appearing at checkout)
- Platform operators: Sony PlayStation Store, Microsoft Store, Apple App Store, Google Play, Steam (for console/mobile/PC platform purchases)
- EA FC Mobile Webstore: operated by Coda (Codashop), with Carry1st and DevCo as third-party providers
- No payment orchestrator detected (searched Spreedly, Primer, Gr4vy, CellPoint, APEXX, Yuno)

**Legal Entities and Cross-Border Risk:**
- EA Inc. (Redwood City, CA): US headquarters
- EA Swiss Sarl (Geneva): contracting entity for EEA, UK, Brazil, Mexico, Hong Kong, Russia
- EA Canada (Vancouver), EA UK (Guildford), Codemasters (Southam), EA Germany (Cologne), DICE (Stockholm), EA Spain (Madrid), Firemonkeys (Melbourne), Electronic Arts Korea LLC (Seoul)
- CROSS-BORDER RISK: Brazil and Mexico have NO local entities. EA Swiss Sarl handles contracts from Geneva, meaning cross-border acquiring with elevated decline rates

**Confirmed Payment Methods (28+):**
- Cards: Visa, Visa Debit, Visa Electron, Mastercard, Amex, Discover, JCB (Japan), UnionPay (China), Carte Bancaire (France)
- Wallets: PayPal, Apple Pay (regional), EA Wallet Balance, EA Cash Card / Gift Cards, Gold Wallet
- Bank: iDEAL, iDEAL SEPA, SEPA Direct Debit, Trustly (Europe), Dotpay (Poland)
- BNPL: Klarna (US, intermittent/broken)
- Russia/CIS: Qiwi, Webmoney, Yandex, Yandex Credit Card, Yandex Qiwi
- LATAM: BoaCompra Credit Card
- Korea: KCP Credit Card
- FC Mobile Webstore: bKash and Robi (Bangladesh), Etisalat (UAE, currently maintenance), card payment, PayPal

**Top 5 Markets Gap Analysis:**

MARKET 1: United States (41% of revenue, #1 traffic)
  Currently offer: Visa/MC/Amex/Discover, PayPal, Apple Pay, Klarna (broken), EA Wallet
  Missing: Cash App Pay, Venmo (standalone), ACH for subscriptions
  Note: Klarna integration is broken per multiple EA Forum threads. Lost BNPL conversion on higher-value purchases.

MARKET 2: United Kingdom (#2 traffic, major entity)
  Currently offer: Visa/MC, PayPal, Trustly, SEPA
  Missing: Open Banking (UK Faster Payments), Revolut Pay, Clearpay
  Note: UK is a dominant FC/FIFA market. Open Banking adoption growing rapidly.

MARKET 3: Germany (#3 traffic, local entity in Cologne)
  Currently offer: Visa/MC, PayPal, SEPA, Trustly
  Missing: Sofort/Klarna SOFORT, Giropay
  Note: Credit card penetration ~35% in Germany. Bank transfer methods are critical for conversion.

MARKET 4: Brazil (#5 traffic, NO local entity)
  Currently offer: BoaCompra Credit Card
  Missing: Pix, Boleto Bancario, Mercado Pago, local installment cards
  Note: Pix handles 70%+ of digital payments in Brazil. Cross-border acquiring from Switzerland. Massive gap.

MARKET 5: Japan (#10 traffic, local entity)
  Currently offer: JCB, Visa/MC
  Missing: Konbini (convenience store payments), PayPay, LINE Pay, Rakuten Pay
  Note: Japan is a top gaming market globally. Konbini is essential for unbanked/young gamers who buy FC Points.

**EA FC Mobile Webstore Coverage (60+ countries via Coda):**
Africa: Egypt, Kenya, Morocco, Nigeria, South Africa
Americas: Argentina, Bolivia, Brazil, Canada, Chile, Colombia, Ecuador, Guatemala, Mexico, Paraguay, Peru, US, Uruguay
Central Asia: Kazakhstan, Mongolia
East Asia: Hong Kong, Japan, Taiwan
Europe: Austria, Czech Republic, Denmark, Finland, France, Germany, Greece, Hungary, Ireland, Italy, Netherlands, Norway, Poland, Portugal, Romania, Slovakia, Spain, Sweden, Switzerland, UK
Middle East: Bahrain, Iraq, Kuwait, Qatar, Saudi Arabia, Turkey, UAE
Oceania: Australia, New Zealand
South Asia: Bangladesh, India, Nepal, Pakistan, Sri Lanka
Southeast Asia: Cambodia, Indonesia, Laos, Malaysia, Myanmar, Philippines, Singapore, Thailand, Timor-Leste

**Customer Payment Complaints:**
- Double charges: recurring on Trustpilot (2024 to 2026)
- Refund denials: high volume on Trustpilot for EA Play and broken games
- Saved cards declined / PayPal failures: recurring across EA Forums and Trustpilot
- Klarna not appearing at checkout: multiple EA Forum threads (2025 to 2026)
- No UPI / debit card options: Indian users explicitly requesting local methods on EA Forums
- Region mismatch errors: "payment method's issued country doesn't match your store region" is a widespread complaint
- 57+ outages in 4 months tracked by StatusGator (EA Game service)
- Oct 2025 major outage affected all EA games/services (AWS related)

**Key Leadership:**
- Andrew Wilson: CEO
- Stuart Canfield: CFO (joined EA 2003, became CFO July 2023, 14 different roles at EA)
- David Tinson: Chief Experiences Officer (leads Commercial, Marketing, Fan Growth, new Ventures)
- No dedicated VP/Head of Payments identified publicly. Payment operations likely under CFO or CTO org.

**Key Meeting Angles:**
1. **$55B Privatization** | PIF/Silver Lake will scrutinize every cost center. Payment processing on $4.4B+ digital revenue is one of the largest controllable cost lines.
2. **Multi-PSP without orchestration** | Managing Ingenico, BoaCompra, KCP independently across 18+ countries. No unified routing, no failover, no consolidated analytics.
3. **$44M per 1% auth uplift** | At $4.4B in digital transactions, even 1% improvement = ~$44M recovered. CEO wants 10 to 20% microtxn growth; approval rate optimization is the fastest path.
4. **Brazil/Mexico cross-border bleeding** | Both processed from Switzerland via EA Swiss Sarl. No Pix, no Boleto, no OXXO, no SPEI. Local acquiring through Yuno could dramatically improve approval rates.
5. **60+ country mobile footprint** | FC Mobile Webstore already operates in 60+ countries. Orchestration would unify payment logic across EA App, webstore, and mobile.
6. **Broken integrations** | Klarna intermittently disappearing, PayPal failures, region mismatch errors. Orchestration layer ensures every method works consistently.
7. **Competitor precedent** | Roblox uses multi-PSP. Steam accepts 100+ methods. EA lags behind in payment sophistication relative to transaction volume.

**Sources:**
- [EA Help: Buying EA Games](https://help.ea.com/en/help/account/buying-ea-games/)
- [EA Help: Fix Payment Issues](https://help.ea.com/en/articles/technical-issues/fix-payment-issues/)
- [EA Help: Payment Error Codes](https://help.ea.com/en/articles/technical-issues/ea-app-payment-coupon-error-codes/)
- [EA Help: Buy FC Points](https://help.ea.com/en/articles/ea-sports-fc/buy-fc-points/)
- [EA FC Mobile Webstore](https://store.fcm.ea.com/international)
- [EA FC Mobile Webstore Launch](https://www.ea.com/games/battlefield/news/fc-mobile-webstore-launch)
- [EA Executives](https://www.ea.com/executives)
- [EA IR: Annual Reports](https://ir.ea.com/financials/annual-reports-and-proxy-information/default.aspx)
- [EA IR: Q1 FY26 Results](https://www.ea.com/news/electronic-arts-reports-q1-fy26-results)
- [EA IR: Q3 FY25 Pre-Announcement](https://ir.ea.com/press-releases/press-release-details/2025/Electronic-Arts-Pre-Announces-Preliminary-Q3-FY25-Results/default.aspx)
- [EA User Agreement](https://help.ea.com/en/help/account/ea-user-agreement/)
- [EA Forums: Region Mismatch](https://forums.ea.com/discussions/ea-app-general-discussion-en/the-payment-methods-issued-country-doesnt-match-your-store-region-/7532601)
- [EA Forums: Outage Oct 2025](https://forums.ea.com/discussions/ea-forums-general-discussion-en/resolved-outage-affecting-ea-gamesservices-oct-20-2025/12796867)
- [EA Revenue by Region (Bullfincher)](https://bullfincher.io/companies/electronic-arts/revenue-by-geography)
- [EA Revenue (MacroTrends)](https://www.macrotrends.net/stocks/charts/EA/electronic-arts/revenue)
- [EA Extra Content Revenue (Statista)](https://www.statista.com/statistics/274761/electronic-arts-ea-extra-content-revenues/)
- [EA FY25 Analysis (GamesMarket)](https://www.gamesmarket.global/electronic-arts-ea-lower-revenue-and-net-income-in-fy2025-cautious-outlook-for-fy2026-despite-battlefield-e8b658e8eef46838f934b4c80c0e61b9/)
- [EA Live Services Record (Variety)](https://variety.com/2024/gaming/news/ea-sports-fc-electronic-arts-earnings-1235890705/)
- [StatusGator: EA Game](https://statusgator.com/services/ea-game)
- [Codashop: EA FC Mobile BD](https://www.codashop.com/en-bd/ea-sports-fc-mobile)
- [EA FC Mobile Webstore UAE](https://store.fcm.ea.com/en-ae/easports-fcmobile)
- [EA CFO Profile (Fortune)](https://fortune.com/2024/09/04/cfo-electronic-arts-14-different-jobs-at-the-company/)
- [Klarna: EA Store Page](https://klarna.com/us/store/Electronic-Arts/)
- [How EA FIFA Made $7B (Arthnova)](https://arthnova.com/how-ea-fifa-made-7-billion-before-rebrand/)
- [EA 10-K FY2025](https://last10k.com/sec-filings/ea/0000712515-25-000022.htm)
- [Xsolla + Adyen Partnership](https://www.businesswire.com/news/home/20250814871369/en/)
