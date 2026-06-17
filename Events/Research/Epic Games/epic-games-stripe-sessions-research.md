# EPIC GAMES | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
═══════════════════════════════════════
DATABASE FIELDS: Epic Games
═══════════════════════════════════════

Logo: https://upload.wikimedia.org/wikipedia/commons/3/31/Epic_Games_logo.svg
Nombre merchant: Epic Games

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Multi PSP Fragmentation
Tittle_Pain Point_2: Cross Border Decline Rate
Tittle_Pain Point_3: V Bucks Checkout Friction
Tittle_Pain Point_4: APM Coverage Gaps
Tittle_Pain Point_5: Revenue Under Pressure

Desc_Pain Point_1: Xsolla handles card processing and wallet; PayPal runs as a secondary rail; CodaPay covers emerging markets; Apple and Google own mobile IAP. Four+ payment rails with no unified routing, no failover logic, no centralized approval rate visibility.
Desc_Pain Point_2: 650M+ registered Fortnite players across 200+ countries, but no local acquiring in most markets. Players in Brazil, India, Turkey, and Poland pay cross border on international cards with elevated decline rates.
Desc_Pain Point_3: "Transaction declined for your protection" is so common Epic created a dedicated help article. YouTube guides on fixing Epic payment errors have hundreds of thousands of views. Each failed V Bucks purchase is lost microtransaction revenue.
Desc_Pain Point_4: Despite 972M cross platform accounts, key markets lack local APMs. No BLIK in Poland (5.4% of players), no GCash in Philippines, no Mercado Pago in Argentina, no KakaoPay in South Korea. Gift card workarounds signal checkout gaps.
Desc_Pain Point_5: Epic cut 1,000+ jobs in March 2026 citing "spending more than we make." V Bucks prices rose 20%. Every failed payment or suboptimal route costs real dollars at a moment when margin recovery is existential.

SLIDE 1: PSP TOPOLOGY

PSP_1: Xsolla
PSP_2: PayPal
PSP_3: CodaPay (Coda Payments)
PSP_4: Apple App Store / Google Play

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: BLIK
Local_M_2: GCash
Local_M_3: KakaoPay
Local_M_4: Mercado Pago
Local_M_5: DANA
Local_M_6: SPEI
Local_M_7: Nequi
Local_M_8: Maya
Local_M_9: GrabPay
Local_M_10: PSE

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing Engine
Tittle_Yuno_Cap2: Transaction Recovery
Tittle_Yuno_Cap3: Local Payment Methods at Scale
Tittle_Yuno_Cap4: Unified Payment Dashboard

Desc_Yuno_Cap1: Route each V Bucks purchase, Battle Pass renewal, and Epic Games Store transaction to the highest performing processor for that card BIN, issuer, and geography. With $6B+ annual revenue and 650M+ Fortnite players, even a 3% auth rate uplift translates to $180M+ in recovered annual revenue across the ecosystem.
Desc_Yuno_Cap2: When Xsolla declines a card, Yuno cascades automatically to the next best acquirer in milliseconds. Epic's "transaction declined for your protection" error becomes a recovered sale instead of a lost player. Up to 50% recovery rate on soft declines, directly addressing the checkout friction that plagues V Bucks and Store purchases.
Desc_Yuno_Cap3: Activate 1,000+ payment methods through one API. BLIK for Poland's 5.4% player base, GCash and Maya for Southeast Asia, Mercado Pago for Argentina, KakaoPay for South Korea, DANA and GrabPay for Indonesia. No per market engineering sprints. Players pay how they want, conversion goes up, gift card dependency goes down.
Desc_Yuno_Cap4: Replace Epic's fragmented Xsolla + PayPal + CodaPay + Apple IAP + Google Play data silos with one real time console. Monitor approval rates, decline codes, and processing costs across every provider and every region. Millisecond anomaly detection via Yuno Monitors flags issues before they become outages.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Epic Games at a glance:**
- Founded 1991 by Tim Sweeney. HQ: Cary, North Carolina. Private company, majority owned by Sweeney (~50%) + Tencent (40%)
- Products: Fortnite (battle royale/social platform), Epic Games Store (PC game marketplace), Unreal Engine (game development), Fab (3D asset marketplace)
- Revenue: ~$6.01B in 2025, with Fortnite alone generating ~$4B/year. Epic Games Store: $1.16B in 2025 (+6% YoY)
- Users: 972M cross platform Epic accounts. EGS: 317M registered PC users, 78M peak MAU (Dec 2025), 31M avg DAU
- Fortnite: 650M+ registered players, 30M+ daily active players
- Employees: ~4,000 after March 2026 layoffs (down from ~5,000)
- V Bucks price increase effective March 19, 2026: 20% fewer V Bucks per dollar. Reason: "costs of running games has gone up a lot"
- Layoffs: 1,000+ cut in March 2026 (~20% of workforce). Tim Sweeney: "We are spending significantly more than we are making"
- IPO: No current plans. Private since founding

**Confirmed PSPs:**
- **Xsolla**: Primary payment processor. Named in official Epic Games billing support. Handles credit card processing, Xsolla Wallet, and checkout redirection. Dedicated help articles for "Xsolla payment errors" and "saved Xsolla credit cards" issues
- **PayPal**: Secondary payment option. Available alongside Xsolla in checkout flow. Users redirected to PayPal to complete purchase
- **CodaPay (Coda Payments)**: Regional payment processor for emerging markets. Handles local methods including PIX, Mercado Pago, PicPay in Brazil. Support article exists for "Payment Errors using CodaPay"
- **Apple App Store / Google Play**: Mobile IAP for iOS and Android Fortnite (reinstated after Epic v. Apple settlement)
- **No payment orchestrator detected.** Searched for Spreedly, Primer, Gr4vy, CellPoint, APEXX. No connections to Epic Games found

**Office Locations (22 worldwide):**

| Region | Locations |
|--------|-----------|
| North America | Cary NC (HQ), San Francisco, Bellevue, Boston, New York, San Diego, Larkspur, Riverton, Montreal (Canada) |
| Europe | London/Guildford/Manchester (UK), Berlin/Cologne (Germany), Paris (France), Stockholm (Sweden), Helsinki (Finland), Novi Sad (Serbia), Lucerne (Switzerland) |
| Asia | Seoul (South Korea), Yokohama (Japan), Shanghai (China), Islamabad (Pakistan) |
| Latin America | Porto Alegre (Brazil) |

**Legal Entities:**
- Epic Games, Inc. (US, Cary NC) for US operations
- Epic Games International S.a r.l. (Luxembourg) + Swiss branch (Root, Switzerland) for international operations
- Subsidiaries: Psyonix (Rocket League), Mediatonic (Fall Guys), Harmonix (Rock Band)

**Top Markets by Fortnite Player Distribution:**

| Rank | Country | Player Share | Est. Players | Key APM Gap |
|------|---------|-------------|-------------|-------------|
| 1 | United States | 21.1% | 108.2M | Served (cards, PayPal) |
| 2 | Russia | 7.5% | ~49M | YooMoney, SBP, Mir cards |
| 3 | Brazil | 5.5% | ~36M | Pix confirmed; Boleto unclear |
| 4 | Poland | 5.4% | ~35M | BLIK not confirmed |
| 5 | Mexico | 3.4% | ~22M | OXXO, SPEI gaps |
| 6 | Indonesia | High engagement (74.6% BR mode) | Large | DANA, OVO, GoPay gaps |
| 7 | India | High engagement (82.8% BR mode) | Large | UPI partially confirmed |
| 8 | South Korea | High engagement (63.2% BR mode) | Large | KakaoPay, Toss gaps |
| 9 | Germany | High engagement (53.6% BR mode) | Large | SEPA DD, Giropay gaps |
| 10 | Japan | Significant | Large | Konbini confirmed |

**Confirmed Payment Methods:**

| Category | Methods | Source |
|----------|---------|--------|
| Cards | Visa, Mastercard, Amex, Discover, prepaid cards | Epic Help Center |
| Digital Wallets | PayPal, Xsolla Wallet, Epic Account Balance (140+ countries) | Epic Help Center |
| LATAM | Pix (Brazil), CodaPay (Mercado Pago, PicPay) | Epic Help Center |
| Asia | Alipay, WeChat Pay (China region), Konbini (Japan) | Epic Help Center, support articles |
| Europe | Paysafecard | Epic Help Center |
| Prepaid | V Bucks gift cards (retail, select countries) | Fortnite.com |
| Other | Amazon Pay | Third party sources |

**Payment Complaints:**
- "Looks like something went wrong. For your protection, this transaction has been declined" is a well documented recurring error across Epic Games Store and Fortnite
- Epic has dedicated help articles for this specific error, indicating high volume
- YouTube troubleshooting videos have hundreds of thousands of views (e.g., "EPIC GAMES CREDIT CARD DECLINED FIXED 2024")
- Users report being blocked from purchases after multiple attempts
- CodaPay payment errors have their own dedicated support article
- Xsolla saved credit card errors have their own dedicated support article
- VPN usage triggers false positive fraud declines

**V Bucks Price Increase (March 2026):**
- 1,000 V Bucks bundle now gives 800 V Bucks for the same $8.99
- Fortnite Crew monthly grant dropped from 1,000 to 800 V Bucks
- Battle Pass cost reduced from 1,000 to 800 V Bucks but Bonus Rewards V Bucks removed
- 20% Epic Rewards credit offered as partial offset on direct purchases
- Player backlash: "furious" reception per multiple gaming outlets

**Key Meeting Angles:**

1. **Revenue pressure is real** | Epic is spending more than it makes, laid off 20% of staff, and raised V Bucks prices. Every failed transaction and suboptimal route directly impacts survival margins. Yuno's smart routing and recovery pay for themselves instantly.

2. **Multi PSP chaos with no orchestration** | Xsolla + PayPal + CodaPay + Apple IAP + Google Play. Five+ payment rails with zero unified visibility, no failover between them, no smart routing. Yuno consolidates everything into one dashboard with real time monitoring.

3. **Poland is a massive blind spot** | 5.4% of all Fortnite players are in Poland. BLIK dominates Polish digital payments. No evidence of BLIK support on Epic. That is 35M+ players without their preferred payment method.

4. **LATAM expansion opportunity** | Porto Alegre office proves commitment to Brazil. Pix is confirmed but CodaPay intermediation adds friction and cost. Local acquiring through Yuno could reduce cross border fees and lift approval rates across Brazil, Mexico, Colombia, Argentina.

5. **Competitor precedent** | Steam accepts 100+ payment methods globally. Roblox uses multi PSP architecture. Epic's limited APM coverage puts them at a competitive disadvantage in monetization efficiency.

6. **Microtransaction volume = massive smart routing impact** | $4B+ annual Fortnite revenue mostly from microtransactions ($0.99 to $29.99). High volume, low AOV transactions benefit disproportionately from smart routing and retry logic. Even 2% auth uplift = $80M+ recovered.

7. **Building vs. buying** | Epic is cutting costs aggressively. Building payment orchestration internally would require years and significant engineering investment. Yuno deploys in weeks with zero code.

**Leadership Contacts:**
- Tim Sweeney: CEO and Founder (majority owner)
- Joe Babcock / Randy S. Gelber: CFO (conflicting sources)
- Kim Libreri: CTO
- Brian Boyle: VP Controller (Finance)
- Mark Rein: VP and Co Founder
- No dedicated VP/Head of Payments identified publicly. Likely under Finance or Engineering leadership

**Sources:**
- [Epic Games Help: Payment Methods](https://www.epicgames.com/help/en-US/billing-support-c5719364845851/general-support-c5719348744091/what-forms-of-payment-can-i-use-to-make-a-purchase-a5720325816219)
- [Epic Games Help: Transaction Declined](https://www.epicgames.com/help/en-US/billing-and-payment-c-202300000001642/payment-issues-c-202300000001745/looks-like-something-went-wrong-for-your-protection-this-transaction-has-been-declined-please-try-another-card-or-other-payment-methods-error-a202300000012317)
- [Epic Games Help: Xsolla Wallet](https://www.epicgames.com/help/en-US/billing-and-payment-c-202300000001642/general-support-c-202300000001746/how-to-make-purchases-using-xsolla-wallet-balance-a202300000016198)
- [Epic Games Help: Pix Payment Method](https://www.epicgames.com/help/en-US/c-Category_BillingSupport/c-PaymentIssues/purchasing-with-the-pix-payment-method-a000085318)
- [Epic Games Help: CodaPay Errors](https://www.epicgames.com/help/c-202300000001642/c-202300000001745/payment-errors-using-codapay-a202300000010989)
- [Epic Games Help: Xsolla Card Errors](https://www.epicgames.com/help/en-US/fortnite-c5719335176219/billing-support-c5719343057307/purchasing-errors-when-using-saved-xsolla-credit-cards-a5720387978523)
- [Xsolla Partner: Epic Games](https://xsolla.com/portfolio/clients/epic-games)
- [Xsolla Partner: Fortnite](https://xsolla.com/stories/fortnite)
- [Epic Games Store: 2025 Year in Review](https://store.epicgames.com/en-US/news/epic-games-store-2025-year-in-review)
- [GamesMarket: EGS $1.1B in 2025](https://www.gamesmarket.global/epic-games-store-tops-1-1-billion-in-2025-third-party-game-spending-up-57/)
- [WCCFTech: EGS 317M Users](https://wccftech.com/epic-games-store-saw-record-setting-third-party-sales-growth-in-2025-reaches-317m-pc-users/)
- [Shacknews: EGS 78M MAU](https://www.shacknews.com/article/147709/epic-game-store-78-million-mau-2025)
- [DemandSage: Fortnite Statistics 2026](https://www.demandsage.com/fortnite-statistics/)
- [GamesHub: Epic Layoffs 2026](https://www.gameshub.com/news/article/epic-games-layoffs-2026-fortnite-job-cuts-2862852/)
- [PC Gamer: Tim Sweeney "Spending More"](https://www.pcgamer.com/gaming-industry/epic-games-lays-off-more-than-1-000-employees-were-spending-significantly-more-than-were-making-ceo-tim-sweeney-says/)
- [Fortnite.com: V Bucks Price Increase](https://www.fortnite.com/news/fortnite-v-bucks-price-increase)
- [GamesHub: V Bucks Price Increase 2026](https://www.gameshub.com/news/article/fortnite-v-bucks-price-increase-2026-epic-amazing-things-2861511/)
- [Epic Games Logo (SVG)](https://upload.wikimedia.org/wikipedia/commons/3/31/Epic_Games_logo.svg)
- [Clay: Epic Games Office Locations](https://www.clay.com/dossier/epic-games-headquarters-office-locations)
- [Craft.co: Epic Games](https://craft.co/epic-games)
- [Wikipedia: Epic Games](https://en.wikipedia.org/wiki/Epic_Games)
- [Epic Games About](https://www.epicgames.com/site/en-US/about)
- [Sacra: Epic Games Revenue](https://sacra.com/c/epic-games/)
- [OpenCritic: Epic $6B Revenue](https://opencritic.com/news/27770/epic-games-a-company-that-made-6-billion-last-year-is-raising-the-price-of-fortnite-v-bucks-to-help-pay-the-bills-)
- [CodaPay: 400+ Payment Methods](https://www.codapayments.com/codapay)
- [Epic Games Store: Wallet Expands](https://store.epicgames.com/en-US/news/epic-games-wallet-payment-option-expands)
- [Appuals: Transaction Declined Fix](https://appuals.com/epic-games-for-your-protection-this-transaction-has-been-declined/)
