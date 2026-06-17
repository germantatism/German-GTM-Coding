# QLUB | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Qlub
=======================================

Logo: https://media.licdn.com/dms/image/v2/D4D0BAQFgQz2uP3qGCQ/company-logo_200_200/company-logo_200_200/0/1719835285053/qlub_pay_logo?e=2147483647&v=beta&t=qlub
Nombre merchant: Qlub

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Multi-Market Acquirer Mix
Tittle_Pain Point_2: Cross-Border Card Declines
Tittle_Pain Point_3: Missing Local Wallets
Tittle_Pain Point_4: FX Rate Volatility
Tittle_Pain Point_5: Tip Payout Complexity

Desc_Pain Point_1: Qlub operates across 10+ markets (UAE, KSA, Singapore, Korea, Brazil, Australia, Qatar, Kuwait, HK). Each market uses different acquirers and gateways. No unified routing layer optimizes transaction costs across all markets simultaneously.
Desc_Pain Point_2: Tourists paying restaurant bills with foreign-issued cards face high decline rates. Cross-border card-not-present transactions through Mastercard Gateway trigger fraud flags. In tourism-heavy markets like UAE and Singapore, this blocks significant revenue.
Desc_Pain Point_3: Qlub accepts Apple Pay, Google Pay, and cards, but lacks region-specific wallets. No Samsung Pay in Korea, no STC Pay in Saudi Arabia, no Pix QR in Brazil, no GrabPay in Singapore. Diners default to cash, eliminating the digital tipping uplift.
Desc_Pain Point_4: Processing billions in annual transactions across 10+ currencies creates FX exposure. Exchange rates fluctuate between diner payment and restaurant settlement. Multi-currency volatility compresses margins on every cross-border transaction.
Desc_Pain Point_5: Qlub increases tips by 300% through digital prompts. But routing tip payouts to waitstaff across 10+ countries with different tax rules, currencies, and banking systems creates settlement complexity for 5,000+ restaurant partners.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (partner, SoftPOS SDK, Tap-to-Pay)
PSP_2: Mastercard Gateway (card-not-present, GCC markets)
PSP_3: Apple Pay (via QR checkout)
PSP_4: Google Pay (via QR checkout)
PSP_5: Local acquirers (market-specific)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Samsung Pay (South Korea)
Local_M_2: STC Pay (Saudi Arabia)
Local_M_3: Pix (Brazil)
Local_M_4: GrabPay (Singapore)
Local_M_5: KakaoPay (South Korea)
Local_M_6: Mada (Saudi Arabia)
Local_M_7: PayPay (Japan)
Local_M_8: OXXO (Mexico)
Local_M_9: Naver Pay (South Korea)
Local_M_10: DANA (Indonesia)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each restaurant payment to the optimal acquirer by card BIN, currency, and market. For a platform processing billions annually across 10+ countries, smart routing maximizes approval rates on every dine-in transaction. 3% to 10% auth uplift on tourist cards.
Desc_Yuno_Cap2: Automatic cascade across Stripe, Mastercard Gateway, and local acquirers. When one processor declines a tourist card, Yuno reroutes in milliseconds. Up to 50% recovery on failed transactions. Diners pay seamlessly; restaurants never lose a sale at the table.
Desc_Yuno_Cap3: Activates the wallets diners actually use in each market: Samsung Pay and KakaoPay in Korea, STC Pay and Mada in Saudi, Pix in Brazil, GrabPay in Singapore, DANA in Indonesia. One API, 1,000+ methods, zero per-market builds for 5,000+ restaurants.
Desc_Yuno_Cap4: One dashboard unifying Stripe, Mastercard Gateway, and local acquirers across all 10+ markets. Real-time monitoring of dine-in payments, tips, and split bills. NOVA fraud engine with 75% fewer false positives. Centralized analytics for 5,000+ venues globally.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Qlub at a glance:**
- Founded: 2021 by Eyad Alkassar and Mahmoud Fouz (ex-founders of Lazada, Namshi, Snapp)
- Headquarters: Dubai, United Arab Emirates
- Co-CEOs: Eyad Alkassar and Mahmoud Fouz
- Employees: ~240 to 368 (across 6 continents)
- Funding: $72M+ total raised (some sources cite $99M)
  - Seed: $17M (2022, led by Cherry Ventures and Point Nine)
  - Series A: $25M (2023)
  - Series B: $30M (July 2025, led by Shorooq Partners and Cherry Ventures)
  - Investors: Mubadala Investment Company, e&, Legend Capital (China), Mastercard, Cherry Ventures, Point Nine, Shorooq Partners
- Transaction Volume: Billions of dollars processed annually
- Users: Millions of diners monthly
- Restaurants: 5,000+ venues globally across 10+ markets
- Markets: UAE, Saudi Arabia, Singapore, Hong Kong, Australia, Brazil, Qatar, Kuwait, South Korea

**Products:**
- Pay-at-Table: QR code scan, split bill, tip, pay in 10 seconds (no app required)
- Order-and-Pay: Digital ordering from table via QR code
- Digital Menus: Interactive menu display on diner smartphones
- Payment Links: Shareable via WhatsApp or email
- SoftPOS: Tap-to-Pay via Stripe SDK
- POS Integration: Connects to hundreds of POS systems globally
- Analytics Dashboard: Real-time payment and performance data

**Key Metrics:**
- 80% faster checkout speed
- 300% increase in tips via digital prompts
- Reduced restaurant labor costs
- 10-second payment completion time

**Confirmed PSPs / Payment Rails:**
- Stripe: Partner (SoftPOS SDK, Tap-to-Pay processing)
- Mastercard Gateway: Card-not-present transactions in GCC markets (UAE, KSA, Qatar, Kuwait, Bahrain)
- Apple Pay: Supported at QR checkout
- Google Pay: Supported at QR checkout
- Credit/Debit Cards: Primary payment method via QR scan
- Local acquirers: Market-specific processing
- No payment orchestrator detected

**Key Payment Challenges:**
- Multi-market acquirer fragmentation: Different processors in each of 10+ countries
- Tourist card declines: Foreign-issued cards trigger fraud flags in card-not-present flows
- Missing local wallets: No Samsung Pay (Korea), STC Pay (Saudi), Pix (Brazil), GrabPay (Singapore)
- FX exposure: Billions in multi-currency transactions create rate volatility
- Tip payout complexity: Digital tips in 10+ countries with different tax/banking rules
- Cash fallback: When digital payments fail, diners revert to cash, losing the 300% tip uplift

**Strategic Partnerships:**
- Mastercard: Partnership to transform digital payments in GCC hospitality sector
- Stripe: Official partner in Stripe Partner Ecosystem
- Mubadala: Abu Dhabi sovereign wealth fund investor
- e&: UAE telecom giant investor

**Competitive Landscape:**
- Sunday: 80M+ guests annually, 3,000+ restaurants, $21M Series B (Nov 2025)
- Mr Yum: QR ordering and payments for restaurants
- OrderPay: UK-focused pay-at-table
- Dine: Restaurant payment solutions
- MONEI Pay: QR code restaurant payments
- GoTab: Restaurant commerce platform

**Key Meeting Angles:**
1. **Billions processed, multi-acquirer chaos** | 10+ markets each with different acquirers. Smart routing unifies all processors into one optimization layer, reducing costs per transaction.
2. **Tourist card decline problem** | UAE and Singapore are tourism-heavy. Foreign cards face high decline rates in card-not-present QR flows. Failover routing recovers up to 50% of failed transactions.
3. **300% tip uplift at risk** | When digital payment fails, diners pay cash and the tip uplift disappears. Ensuring 100% payment success preserves the core value proposition for restaurants.
4. **Missing local wallets = cash fallback** | Korean diners want KakaoPay, Saudis want STC Pay, Brazilians want Pix. Without local wallets, diners default to cash at the table.
5. **$72M+ raised, global expansion** | New funding targets new geographies. Yuno's 1,000+ APMs enable instant launch in any new market without building local integrations.
6. **Mastercard + Stripe partner, ready for orchestration** | Already working with multiple processors. Orchestration is the natural next step to unify and optimize across all payment rails.

**Sources:**
- [Qlub Official Website](https://qlub.io/ae/en)
- [Qlub Stripe Partner Directory](https://stripe.partners/directory/qlub)
- [Qlub $30M Series B (Wamda)](https://www.wamda.com/2025/07/qlub-closes-30-million-round-backed-shorooq-e-mubadala)
- [Qlub $30M Series B (MENAbytes)](https://www.menabytes.com/qlub-series-b/)
- [Qlub $30M (Zawya)](https://www.zawya.com/en/press-release/companies-news/qlub-raises-30mln-to-take-its-hit-dining-payment-system-global-lms75rho)
- [Qlub $17M Seed (TechCrunch)](https://techcrunch.com/2022/01/31/sunday-competitor-qlub-emerges-with-17m-seed-round-from-cherry-and-point-nine/)
- [Qlub $17M Seed (Business Standard)](https://www.business-standard.com/content/press-releases-ani/qlub-raises-usd-17-million-in-seed-financing-to-drive-future-proof-restaurant-payments-122020100847_1.html)
- [Mastercard Partnership (Mastercard)](https://www.mastercard.com/news/eemea/en/newsroom/press-releases/en/2023/september/mastercard-partners-with-qlub-to-transform-digital-payments-in-the-gcc-hospitality-sector/)
- [Qlub Caterer Middle East](https://www.caterermiddleeast.com/suppliers/how-qlub-is-leading-the-way-for-contactless-payments-in-the-uae-saudi-arabia)
- [Qlub Pay (ExploreTech)](https://www.exploretech.io/en/product/qlub-qlub-pay)
- [Qlub Cherry Ventures](https://cherry.vc/founders/qlub)
- [Qlub Crunchbase](https://www.crunchbase.com/organization/qlub)
- [Qlub CB Insights](https://www.cbinsights.com/company/qlub)
- [Qlub Tracxn](https://tracxn.com/d/companies/qlub/__OiHPNaJtuKn9Kz7JeRg_ZGToYAsA9XmDwEq3uuPM6yE)
- [Sunday $21M Series B (BusinessWire)](https://www.businesswire.com/news/home/20251113471652/en/sunday-Raises-$21M-to-Grow-the-Payment-Platform-Used-by-80M-Diners)
