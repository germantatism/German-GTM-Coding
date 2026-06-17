# NHN GLOBAL | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: NHN Global
=======================================

Logo: https://nhnglobal.com/m/img/logo.svg
Nombre merchant: NHN Global

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Cross-Border Settlement
Tittle_Pain Point_2: B2B Net Terms Complexity
Tittle_Pain Point_3: Multi-Platform Reconcile
Tittle_Pain Point_4: Card Decline at Checkout
Tittle_Pain Point_5: FX Leakage Korea-US

Desc_Pain Point_1: Bridging Korean parent (NHN Corp, $1.75B revenue) and US marketplace (FashionGo). KRW/USD settlement creates FX exposure on every vendor payout and charge.
Desc_Pain Point_2: FashionGo launched Dynamic Net Terms (net 30/45/60) in 2024. Mixing card payments with deferred billing across thousands of wholesale buyers adds load.
Desc_Pain Point_3: FashionGo, LA Showroom, N41, and Comico each have separate payment flows. Parent adds PAYCO, NHN KCP ($38B volume), and Hangame gaming payments.
Desc_Pain Point_4: FashionGo buyers report declined cards from billing errors, bank holds, and cross-border flags. Each decline blocks a wholesale order and delays restocking.
Desc_Pain Point_5: NHN KCP processes $38B/yr in Korea; FashionGo does $31.5M in the US. Settling between ecosystems in different currencies with different PSPs leaks margin.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe (FashionGo FG Pay)
PSP_2: NHN KCP (Korea, $38B volume)
PSP_3: PAYCO (Korea mobile wallet)
PSP_4: Deutsche Bank (Henkel Korea gateway)

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: KakaoPay
Local_M_2: Naver Pay
Local_M_3: Toss
Local_M_4: ACH (US bank transfer)
Local_M_5: OXXO (Mexico)
Local_M_6: Pix (Brazil)
Local_M_7: Konbini (Japan)
Local_M_8: PayPay (Japan)
Local_M_9: GrabPay (Southeast Asia)
Local_M_10: BLIK (Poland)

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing
Tittle_Yuno_Cap2: Failover & Retries
Tittle_Yuno_Cap3: Local Payment Methods
Tittle_Yuno_Cap4: Unified Orchestration

Desc_Yuno_Cap1: Route each FashionGo wholesale transaction to the optimal acquirer by card BIN, buyer country, and order size. With thousands of retail buyers placing cross-border orders, smart routing can uplift authorization 3-10%. InDrive achieved 90% approval through Yuno's routing engine.
Desc_Yuno_Cap2: Automatic cascade recovers declined wholesale orders instantly. When Stripe declines a buyer's card, Yuno reroutes to the next acquirer in milliseconds, preventing lost orders and delayed inventory. Up to 50% recovery on failed transactions across the B2B marketplace.
Desc_Yuno_Cap3: Adds KakaoPay, Naver Pay, and Toss for Korean vendors; ACH for US wholesale buyers; Konbini and PayPay for Japanese expansion. One API, 1,000+ methods. Enables NHN Global to match NHN KCP's local method coverage internationally.
Desc_Yuno_Cap4: One dashboard consolidating Stripe (FashionGo), NHN KCP (Korea), PAYCO, and gaming payments. Cross-border KRW/USD reconciliation, net terms tracking, and NOVA AI recovering 75% of failed payments. Unifies the NHN ecosystem under a single payment intelligence layer.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**NHN Global at a glance:**
- Founded: 2018, HQ: 510 South Broadway, Los Angeles, CA
- CEO: Paul Lee; CFO: Jason Kim; CTO: Choi Kirin
- Subsidiary of NHN Corporation (KRX: 181710), South Korea
- NHN Global revenue: ~$31.5M (2026 estimate)
- NHN Corporation revenue: $1.75B (trailing 12 months, Sep 2025)
- NHN Corporation market cap: $756M
- NHN KCP transaction volume: $38B annually (2025)
- PAYCO users: 12M+ in South Korea (~10% mobile payment market)

**Platforms operated by NHN Global:**
- FashionGo: leading B2B wholesale fashion marketplace, connects brands/manufacturers with retail buyers
- LA Showroom: online wholesale marketplace, 600+ vendors (acquired 2018)
- N41: apparel ERP system for fashion brands, 120+ clients, 99%+ retention rate
- Comico: webtoon platform (Japan, Korea, Taiwan, Thailand)
- Hangame: online/mobile gaming (via parent)

**Parent company NHN Corporation businesses:**
- Cloud services
- Fintech: cross-border e-commerce, payment processing (NHN KCP, PAYCO)
- Entertainment: games, webtoons, music
- Advertising
- PAYCO: digital wallet, member of Cross-Border Mobile Payment Alliance (LINE Pay, Naver Pay, iPASS)
- NHN KCP: dominant Korean payment gateway, $38B annual volume, PG/VAN/Smart Services
- NHN KCP + Avalanche: building payments-focused Layer 1 blockchain for tokenized deposits and cross-border payments

**Confirmed PSPs:**
- Stripe: powers FG Pay on FashionGo (confirmed via help center, PCI Level 1)
- NHN KCP: Korean payment gateway (parent company subsidiary)
- PAYCO: Korean mobile wallet payment service
- Deutsche Bank: appointed as payment gateway for Henkel Korea alongside NHN KCP (January 2026)
- No payment orchestrator detected

**FashionGo payment methods:**
- Credit cards: Visa, Mastercard, Discover, American Express (via Stripe/FG Pay)
- Dynamic Net Terms: net 30, 45, or 60 days (launched March 2024)
- All credit card data tokenized through Stripe

**Payment complaint evidence:**
- Declined cards from incorrect billing address, expiration date, or cross-border flags
- Chargeback disputes trigger temporary account blocks
- Banking account errors: users report difficulty updating bank account information
- Refunds take 5-7 business days to original payment method

**KREAM context (NHN ecosystem partner):**
- KREAM: Korea's #1 sneaker/streetwear resale marketplace, 70%+ market share
- 5.3M monthly active users (2025)
- Uses NHN KCP PAY (easy bank transfer) with improved authorization rates
- Note: KREAM is owned by Naver Corp, not NHN Global directly, but operates within the Korean payment ecosystem

**Key meeting angles:**
1. **$1.75B parent, $38B payment volume** | NHN Corp is a payments powerhouse in Korea (NHN KCP). NHN Global needs equivalent payment sophistication for its US/international operations
2. **FashionGo B2B marketplace on single PSP** | All wholesale transactions flow through Stripe. Dynamic Net Terms add complexity that requires orchestration-level tooling
3. **Cross-border KRW/USD settlement** | Bridging Korean parent and US subsidiary creates FX exposure on every transaction. Smart routing to local acquirers reduces cross-border fees
4. **Gaming + commerce + webtoons** | Multiple revenue streams across NHN ecosystem (games, e-commerce, digital content) each need different payment optimization
5. **PAYCO Cross-Border Alliance precedent** | NHN already participates in cross-border mobile payment alliances. Yuno extends this capability to 1,000+ methods globally
6. **NHN KCP blockchain ambitions** | Building Avalanche L1 for cross-border payments shows NHN invests heavily in payment innovation. Yuno complements with immediate routing optimization
7. **Stripe relationship preserved** | Yuno sits on top of Stripe (FG Pay), adding routing intelligence and failover without replacing the existing integration

**Sources:**
- [NHN Global Official Website](https://nhnglobal.com/index)
- [NHN Corporation](https://nhn.com/en-US)
- [NHN Corporation Wikipedia](https://en.wikipedia.org/wiki/NHN_Corporation)
- [NHN Global LinkedIn](https://www.linkedin.com/company/nhnglobal)
- [NHN Global Crunchbase](https://www.crunchbase.com/organization/nhn-global)
- [FashionGo Official Website](https://www.fashiongo.net/)
- [FashionGo: What Payment System](https://www.fashiongo.net/help-center/topics?categoryGroupId=2&categoryId=16)
- [FashionGo: Dynamic Net Terms Launch](https://www.businesswire.com/news/home/20240318562353/en/FASHIONGO-Unveils-The-First-Dynamic-Net-Terms-for-Wholesale)
- [FashionGo Trustpilot Reviews](https://www.trustpilot.com/review/fashiongo.net)
- [NHN KCP](https://kcp.co.kr/eng/)
- [NHN KCP + Avalanche Blockchain](https://www.theblock.co/post/397153/south-korea-nhn-kcp-avalanche)
- [Deutsche Bank + NHN KCP Partnership](https://www.db.com/news/detail/20260120-deutsche-bank-and-nhn-kcp-appointed-as-henkel-korea-s-payment-gateway-service-providers)
- [PAYCO Service](https://www.nhn.com/en/os/detail.nhn?no=2)
- [PAYCO Cross-Border Alliance](https://en.komoju.com/blog/payment-method/payco/)
- [KREAM Official](https://global.kream.co.kr/)
- [KREAM CBInsights](https://www.cbinsights.com/company/kream)
- [RetailBoss: KREAM Profile](https://retailboss.co/kream-koreas-leading-authenticated-sneaker-resale-marketplace/)
- [NHN Corp Revenue](https://companiesmarketcap.com/nhn-corp/revenue/)
- [Growjo: NHN Global Revenue](https://growjo.com/company/NHN_Global)
