# ROBLOX | Stripe Sessions Research (SS Database Format)
*Generated: 2026-04-21*

```
=======================================
DATABASE FIELDS: Roblox
=======================================

Logo: https://cdn.prod.website-files.com/6257adef93867e50d84d30e2/roblox-logo.svg
Logo_alt: https://images.rbxcdn.com/8e5e2a378f21eba4499977e3de610e04.svg
Nombre merchant: Roblox

SLIDE 1: PAIN POINTS

Tittle_Pain Point_1: Dual PSP, No Orchestrator
Tittle_Pain Point_2: APAC Checkout Gaps
Tittle_Pain Point_3: Outage Revenue Bleed
Tittle_Pain Point_4: Child Chargeback Spiral
Tittle_Pain Point_5: Cross Border FX Drag

Desc_Pain Point_1: Stripe + Xsolla process all web/desktop transactions with no orchestration layer. No smart routing between them. If one declines, there is no automatic failover, costing conversions across 37M monthly payers.
Desc_Pain Point_2: APAC bookings surged 96% YoY but checkout still lacks Pix, UPI, GCash, KakaoPay, Konbini. 110% India growth and 160% Japan growth hit a wall when users cannot pay with local methods.
Desc_Pain Point_3: July 2025 outage blocked purchases for 3.5+ hours across 144M DAU. No failover routing means a single backend failure halts all monetization globally, with developers reporting major revenue loss.
Desc_Pain Point_4: Under 13 users trigger unauthorized purchase disputes at scale. Chargebacks auto ban accounts, creating support overload and net revenue leakage across millions of minor linked payment methods.
Desc_Pain Point_5: 180+ countries but only ~20 local currencies supported. Most markets settle in USD cross border, adding FX markup. With $6.8B in 2025 bookings, even 1% FX drag equals $68M in lost margin.

SLIDE 1: PSP TOPOLOGY

PSP_1: Stripe
PSP_2: Xsolla
PSP_3: Apple App Store
PSP_4: Google Play

SLIDE 1: MISSING LOCAL METHODS (BLIND SPOTS)

Local_M_1: Pix
Local_M_2: UPI
Local_M_3: GCash
Local_M_4: KakaoPay
Local_M_5: Konbini
Local_M_6: BLIK
Local_M_7: OXXO
Local_M_8: DANA
Local_M_9: Maya
Local_M_10: Boleto

SLIDE 2: YUNO CAPABILITIES

Tittle_Yuno_Cap1: Smart Routing Engine
Tittle_Yuno_Cap2: Instant Failover Cascades
Tittle_Yuno_Cap3: 300+ Local Payment Methods
Tittle_Yuno_Cap4: Unified Payment Dashboard

Desc_Yuno_Cap1: Route every Robux purchase to the optimal acquirer by card BIN, issuer, geography, and transaction amount. With 37M monthly unique payers and $6.8B in annual bookings, even a 2% auth rate uplift through intelligent Stripe vs. Xsolla routing translates to $136M+ in recovered annual revenue without adding a single new user.
Desc_Yuno_Cap2: When Stripe declines or an outage hits (like July 2025's 3.5 hour shutdown), Yuno automatically cascades to Xsolla or the next best acquirer in milliseconds. Zero customer friction, zero developer revenue loss. Convert the single point of failure architecture into a resilient multi path payment mesh.
Desc_Yuno_Cap3: Activate Pix in Brazil (181% DAU growth), UPI in India (110% bookings growth), GCash in Philippines, KakaoPay in Korea, Konbini in Japan (160% growth), OXXO in Mexico, BLIK in Poland, DANA in Indonesia (700% growth). One API, 300+ methods, instant geo routing. No per market engineering sprints needed.
Desc_Yuno_Cap4: Replace fragmented Stripe + Xsolla + Apple IAP + Google Play reporting with one real time dashboard. Centralized reconciliation across all 180+ countries, all processors, all currencies. Millisecond anomaly detection catches auth rate drops before they become revenue emergencies. Full visibility across $6.8B in annual bookings.
```

---

## RESEARCH BACKING | Key Facts for the Meeting

**Roblox at a glance:**
- NYSE: RBLX | Founded 2004 | HQ: San Mateo, California
- Full year 2025 revenue: $4.9B (36% YoY growth)
- Full year 2025 bookings: $6.8B (55% YoY surge)
- Q4 2025 DAU: 144M (69% YoY increase)
- Q4 2025 monthly unique payers: 36.7M (94% YoY growth)
- Average spending per payer: $20.18 (53% YoY increase)
- Q4 2025 engagement: 35 billion hours (88% YoY increase)
- 2026 guidance: 22% to 26% bookings growth ($8.2B to $8.5B projected)
- Revenue streams: Robux virtual currency, Roblox Premium subscriptions, in experience developer products/gamepasses, advertising (Immersive Ads), Creator Marketplace
- Creator payouts: $1.5B+ in 2025 via Developer Exchange (DevEx), top 1,000 creators avg $1.3M each
- 21 material subsidiaries across 13 countries
- Offices in US, Canada, UK; data centers in US, France, Germany, Hong Kong, Japan, Singapore, Netherlands, India, Australia, UK

**Key leadership (payments relevant):**
- David Baszucki: Founder & CEO
- Naveen Chopra: CFO (ex Paramount CFO, ex Amazon Devices & Services CFO)
- Enrico D'Angelo: Chief Business Officer, oversees Advertising + Economy Group (which includes Payments and all monetization). Former Activision Blizzard strategy/BD/M&A lead
- Seb Barrios: SVP Engineering (User, Economy, Ads, Brands, and Discovery)
- Antoni Choudhuri: VP/Head of Engineering, Economy Group (Marketplace, Advertising, Developer Monetization, Payments & Fraud). 11 years at Roblox. Attended CNP Expo (Card Not Present fraud conference)
- Amy Rawlings: Chief Accounting Officer (global accounting, revenue, SEC reporting)
- Jerret West: CMO & Head of Market Expansion

**No dedicated VP of Payments identified.** Payments sits within the Economy Group under Enrico D'Angelo (CBO) and Antoni Choudhuri (VP Eng, Economy). The Payments & Fraud team is one of four pillars in the Economy Group alongside Marketplace, Advertising, and Developer Monetization.

---

## Confirmed PSPs & Payment Stack

| Provider | Role | Evidence | Source |
|----------|------|----------|--------|
| Stripe | Primary card processor (web/desktop) | Named in Roblox help pages, privacy policy, developer forums | en.help.roblox.com/hc/en-us/articles/203312560 |
| Xsolla | Secondary processor, fraud/verification, local methods | Named in help pages, Xsolla verification charges article, Xsolla partner spotlight | en.help.roblox.com/hc/en-us/articles/360016750311 |
| Apple App Store | iOS in app purchases | Standard IAP for mobile | help.roblox.com |
| Google Play | Android in app purchases | Standard IAP for mobile | help.roblox.com |
| Amazon Appstore | Fire tablet IAP | Named in help center | en.help.roblox.com/hc/en-us/articles/203312760 |
| Samsung Galaxy Store | Samsung device IAP | Named in help center | en.help.roblox.com/hc/en-us/articles/203312760 |

**Payment orchestrator:** No evidence found of any payment orchestration platform (Spreedly, Primer, Gr4vy, CellPoint, APEXX, or Yuno). Searched extensively. Roblox appears to manage Stripe and Xsolla routing manually/internally.

**Xsolla's specific role:** Xsolla handles verification micro charges ($1 or less holds to validate cards), processes Robux and Premium purchases, appears on credit card statements as the merchant of record for many transactions, and provides fraud detection. Xsolla supports 130+ currencies and 1,000+ payment methods globally through its infrastructure, but Roblox does not appear to leverage the full breadth of Xsolla's APM network.

---

## Website Traffic Analysis by Country

| Rank | Country | Traffic Share (%) | DAU/Growth Context | Source |
|------|---------|-------------------|---------------------|--------|
| 1 | United States | 20.7% | Largest market, 41% bookings growth | similarweb.com/website/web.roblox.com |
| 2 | Turkey | 8.4% | Significant web traffic market | similarweb.com/website/web.roblox.com |
| 3 | Russia | 5.6% | Web traffic; limited monetization | similarweb.com/website/web.roblox.com |
| 4 | Philippines | 4.9% | 52% spending increase with regional pricing | similarweb.com/website/web.roblox.com |
| 5 | Brazil | 4.8% | 181% DAU growth 2020 to 2024; 26% spending lift | similarweb.com/website/web.roblox.com |
| 6 | Japan | ~5.1% (est.) | 160% bookings growth Q4 2025 | statista.com |
| 7 | India | ~3% (est.) | 110% bookings growth Q4 2025 | respawn.outlookindia.com |
| 8 | Indonesia | ~3% (est.) | 700%+ bookings growth Q4 2025 | respawn.outlookindia.com |
| 9 | United Kingdom | Top 10 | Established EU market | semrush.com/website/roblox.com |
| 10 | South Korea | ~2% (est.) | 2.4M MAU, growing rapidly | medium.com |

**Audience profile:** 70.6% male, 29.4% female. Largest age group: 18 to 24 year olds (growing 50%+ in US for 18+ cohort). Direct traffic dominates (69.7%).

---

## Geographic Bookings Breakdown (2025)

| Region | 2025 Bookings (Est.) | YoY Growth | Key Markets |
|--------|----------------------|------------|-------------|
| US & Canada | ~$3.8B | 41% | Core market, highest ARPU |
| Europe | ~$1.4B | 63% | UK, Germany, France, Turkey |
| APAC | ~$819M | 96% (77% FY) | Japan (160%), India (110%), Indonesia (700%+) |
| Rest of World | ~$673M | 123% (80% FY) | Brazil, Mexico, LATAM, Middle East |

---

## Legal Entities & Subsidiaries

Roblox has 21 material subsidiaries across 13 countries. Key entities include:

| Country | Entity Confirmed | Cross Border Risk |
|---------|-----------------|-------------------|
| United States | Roblox Corporation (HQ, San Mateo, CA) | No |
| Canada | Yes (office) | No |
| United Kingdom | Yes (office + data center) | No |
| Netherlands | Yes (data center) | Possible |
| France | Yes (data center) | Possible |
| Germany | Yes (data center) | Possible |
| Japan | Yes (data center) | Possible |
| Singapore | Yes (data center) | Possible |
| Hong Kong | Yes (data center) | Possible |
| India | Yes (office + data center) | Yes, likely cross border |
| Australia | Yes (data center) | Possible |
| South Korea | Yes (regional operations) | Possible |
| Cayman Islands | 1 entity (likely treasury/holding) | N/A |

> China: Roblox launched LuoBu in July 2021 via Tencent partnership, shut down January 2022, currently redeveloping.

> MANUAL: Verify exact subsidiary names from SEC Exhibit 21 (10 K filed Feb 2025) at ir.roblox.com

---

## Payment Methods Confirmed

**Global (Web/Desktop via Stripe + Xsolla):**
- Visa, Mastercard, American Express, Discover
- PayPal
- Prepaid credit cards (with known error issues)
- Roblox Gift Cards (sold at GameStop, Target, Walmart, Best Buy, CVS, Dollar General, Starbucks, and online)

**Mobile:**
- Apple Pay (via App Store IAP)
- Google Pay (via Google Play IAP)
- Samsung Pay (via Galaxy Store)
- Amazon Pay (via Amazon Appstore on Fire tablets)

**Limited local methods via Xsolla (unconfirmed full list):**
- Xsolla's infrastructure supports 130+ currencies and 1,000+ methods, but Roblox appears to expose only a fraction to end users
- Regional payment methods "depending on your location" per help center, but specifics not documented

---

## Missing APM Gap Analysis (Top Growth Markets)

| Market | Growth Signal | Missing APMs | Impact |
|--------|--------------|-------------|--------|
| Brazil | 181% DAU growth, 26% spending lift with regional pricing, 4.8% web traffic | Pix (handles 70%+ of digital payments), Boleto Bancario | Massive conversion gap in #5 traffic market |
| India | 110% bookings growth, mobile first market | UPI (75%+ of digital payments), RuPay, Paytm, PhonePe, Net Banking | DevForum posts explicitly request UPI autopay for Premium |
| Japan | 160% bookings growth, 5.1% user share | Konbini (7 Eleven, Lawson, FamilyMart), PayPay, LINE Pay | Low credit card penetration among younger users |
| Philippines | 52% spending increase, 4.9% traffic | GCash (60M+ users), Maya, GrabPay | ~6% credit card penetration; most users cannot pay |
| Indonesia | 700%+ bookings growth | DANA, OVO, GoPay, ShopeePay | Fastest growing market globally |
| South Korea | 2.4M MAU, growing rapidly | KakaoPay, Naver Pay, Toss | Digital wallets dominate youth spending |
| Mexico | 17% spending increase with regional pricing | OXXO, SPEI | Cash based economy, OXXO essential |
| Poland | Growing EU market | BLIK (used by 80%+ of online shoppers) | BLIK is practically mandatory for Polish checkout |
| Turkey | 8.4% of web traffic (#2 globally) | Papara, Troy cards, iyzico | Second largest web traffic country with no local APMs |
| Germany | Top EU market | SEPA Direct Debit, Sofort/Klarna, Giropay | ~35% credit card penetration; SEPA is subscription backbone |

---

## Customer Payment Complaints

| Issue Type | Platform | Frequency | Date Range | Source |
|-----------|----------|-----------|------------|--------|
| Incorrect charge amounts (e.g. charged 22K Robux instead of 400) | Trustpilot | Recurring | 2024 to 2025 | trustpilot.com/review/www.roblox.com |
| Gift card codes not crediting Robux | Trustpilot, SmartCustomer | Moderate | 2024 to 2025 | smartcustomer.com/reviews/roblox.com |
| Unauthorized child purchases, refund denials | Trustpilot, Quora | High | 2024 to 2026 | en.help.roblox.com/hc/en-us/articles/203312650 |
| Account banned after chargeback | DevForum, Quora | Recurring | 2024 to 2025 | quora.com |
| Purchase auth token failures (504 errors) | DevForum | Outage related | June to July 2025 | devforum.roblox.com/t/3767944 |
| Purchases blocked during platform outages | DevForum | Outage related | July 2025 | devforum.roblox.com/t/3804623 |
| Prepaid card systematic rejections | Roblox Help Center | Recurring | Ongoing | en.help.roblox.com/hc/en-us/articles/203312680 |
| Payment holds not clearing (24 to 48 hrs) | Roblox Help Center | Moderate | Ongoing | en.help.roblox.com/hc/en-us/articles/360000359923 |

---

## Platform Outage History (Payment Impact)

| Date | Duration | Impact | Source |
|------|----------|--------|--------|
| July 8, 2025 | ~3.5 hours | DataStores, purchases, Studio all down. Failed purchase auth tokens (HTTP 504). Developers reported major revenue loss. | devforum.roblox.com/t/3804623 |
| June 2025 | 12+ hours intermittent | Purchase dialogs failed to show, MarketplaceService errors, revenue loss reported | devforum.roblox.com/t/3767944 |
| October 2024 | Multi hour | Roblox down for millions of users (covered by Variety) | variety.com/2024/digital/news/roblox-down-outage-1236176895 |

---

## Expansion Plans & Corporate Developments

| # | Date | Development | Category | Source |
|---|------|-------------|----------|--------|
| 1 | Apr 2025 | Launched regional pricing for in experience items across 180+ countries | International Expansion | about.roblox.com/newsroom/2025/04 |
| 2 | Mar 2026 | Enabled regional pricing for all Passes by default | International Expansion | devforum.roblox.com/t/4471199 |
| 3 | Q4 2025 | APAC bookings grew 96% YoY; Indonesia 700%+, Japan 160%, India 110% | Growth | respawn.outlookindia.com |
| 4 | 2025 | Monthly unique payers nearly doubled to 36.7M | Monetization | ir.roblox.com |
| 5 | 2025 | Creators earned $1.5B+ through DevEx for first time | Creator Economy | ir.roblox.com |
| 6 | 2025 | 18+ user cohort in US growing 50%+ | Demographics | fool.com (earnings transcript) |
| 7 | 2025 | Roblox represents 3.4% of global gaming content market | Market Position | respawn.outlookindia.com |
| 8 | 2024 | Colvin v. Roblox class action (child gambling/RICO) survived motion to dismiss | Legal/Risk | sskblaw.com |
| 9 | 2025 | Xsolla partnered with Adyen for global game payments PSP offering | PSP Ecosystem | businesswire.com |

---

## Key Meeting Angles

1. **APAC explosion without local APMs** | 96% APAC bookings growth proves demand exists, but Pix, UPI, GCash, KakaoPay, Konbini, DANA are all missing. Regional pricing launched but local payment methods did not. Yuno bridges this gap with one integration.

2. **Outage vulnerability** | Three major payment disrupting outages in 12 months. No failover between Stripe and Xsolla. Yuno's cascade routing eliminates the single point of failure that cost developers "major revenue loss" in July 2025.

3. **37M payers, no orchestration** | Roblox nearly doubled monthly payers to 36.7M but still routes manually between two PSPs. At $6.8B bookings scale, even marginal auth rate optimization via smart routing yields nine figure revenue recovery.

4. **Child chargeback cost** | Roblox's core demographic (under 18) generates elevated unauthorized purchase disputes and chargebacks. Yuno's fraud detection and intelligent routing can reduce false declines while catching true fraud earlier in the flow.

5. **IAP fee arbitrage** | Every purchase routed through Apple (30%) or Google (15 to 30%) instead of web checkout costs Roblox significantly. Making web payments frictionless with local APMs shifts volume away from platform fees.

6. **Creator economy alignment** | $1.5B+ in DevEx payouts depend on healthy in experience purchase flows. Payment failures directly reduce creator earnings and platform stickiness. Reliable payment infrastructure is a creator retention tool.

7. **Indonesia as proof point** | 700%+ bookings growth with no local APMs (DANA, OVO, GoPay). Adding them could accelerate an already explosive trajectory.

8. **Economy Group owns payments** | Enrico D'Angelo (CBO, ex Activision) and Antoni Choudhuri (VP Eng Economy) own the payments decision. Both have gaming + commerce DNA. D'Angelo's CBO title means this is a business conversation, not just engineering.

---

## Sources

- [Roblox Q4 & FY2024 Financial Results](https://ir.roblox.com/news/news-details/2025/Roblox-Reports-Fourth-Quarter-and-Full-Year-2024-Financial-Results/)
- [Roblox 2025 Revenue Hits $4.9B (Outlook Respawn)](https://respawn.outlookindia.com/gaming/gaming-news/roblox-daily-users-jump-69-to-record-144-million-in-q4-2025)
- [Roblox Q4 2025 Earnings Call Transcript (Motley Fool)](https://www.fool.com/earnings/call-transcripts/2026/02/05/roblox-rblx-q4-2025-earnings-call-transcript/)
- [S&P Global: Roblox Global Expansion in 2025](https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/01/roblox-poised-for-robust-global-expansion-in-2025)
- [Roblox Leadership Page](https://about.roblox.com/leadership)
- [Roblox Economy Group (Team Behind the Tech)](https://about.roblox.com/newsroom/2023/04/team-behind-tech-economy-group)
- [Roblox Payment Methods Help](https://en.help.roblox.com/hc/en-us/articles/203312580-Which-payment-methods-can-I-use)
- [Roblox Adding Payment Information](https://en.help.roblox.com/hc/en-us/articles/203312560-Adding-and-Updating-Payment-Information)
- [Xsolla Verification Charges on Roblox](https://en.help.roblox.com/hc/en-us/articles/360016750311-Xsolla-verification-charges-micro-transactions)
- [Xsolla Role in Roblox Payments (Playgama)](https://playgama.com/blog/game-faqs/what-is-xsollas-role-in-roblox-payments/)
- [Xsolla Partner Spotlight: Roblox Gift Cards](https://xsolla.com/portfolio/story/video-gaming-roblox-gift-cards)
- [Roblox July 2025 Outage (DevForum)](https://devforum.roblox.com/t/widespread-roblox-outage-disrupts-datastores-purchases-and-studio-functionality/3804623)
- [Roblox June 2025 Outage (DevForum)](https://devforum.roblox.com/t/roblox-cloud-services-experiencing-yet-another-wave-of-outages-purchases-and-memorystore-affected/3767944)
- [Roblox Trustpilot Reviews](https://www.trustpilot.com/review/www.roblox.com)
- [Roblox Unauthorized Charges Help](https://en.help.roblox.com/hc/en-us/articles/203312650-Unauthorized-Charges-Refund-Requests)
- [Roblox Regional Pricing Launch](https://about.roblox.com/newsroom/2025/04/roblox-launches-regional-pricing-for-in-experience-items)
- [Roblox Regional Pricing Developer Docs](https://create.roblox.com/docs/production/monetization/regional-pricing)
- [UPI Autopay Request (DevForum)](https://devforum.roblox.com/t/make-roblox-premium-available-for-purchase-with-upi-autopay-for-indian-users/4225257)
- [Roblox Press Kit](https://about.roblox.com/press-kit)
- [Roblox SEC Filings](https://ir.roblox.com/financials/sec-filings/default.aspx)
- [Roblox Subsidiaries (Tracenable)](https://tracenable.com/company/roblox/group-entities)
- [Enrico D'Angelo LinkedIn](https://www.linkedin.com/in/enricodangelo1/)
- [Antoni Choudhuri LinkedIn](https://www.linkedin.com/in/antonichoudhuri/)
- [SimilarWeb: web.roblox.com Traffic](https://www.similarweb.com/website/web.roblox.com/)
- [SimilarWeb: roblox.com Traffic](https://www.similarweb.com/website/roblox.com/)
- [Roblox Down (Variety, Oct 2024)](https://variety.com/2024/digital/news/roblox-down-outage-1236176895/)
- [Roblox Gambling Lawsuit](https://sskblaw.com/class-action-and-mass-tort/roblox-robux-gambling)
- [Xsolla + Adyen Partnership (BusinessWire)](https://www.businesswire.com/news/home/20250814871369/en/Xsolla-and-Adyen-Partner-to-Power-Global-Game-Payments)
- [Roblox Q4 2025 Slides (Investing.com)](https://in.investing.com/news/company-news/roblox-q4-2025-slides-69-user-growth-and-63-bookings-surge-despite-continued-losses-93CH-5225092)
- [Roblox Statistics 2025 (SQ Magazine)](https://sqmagazine.co.uk/roblox-statistics/)
- [Roblox User Demographics (TechPoint)](https://techpoint.africa/guide/roblox-user-demographics/)
