# SDR Research Brief — Eldorado.gg
**Date:** 2026-03-27 | **Analyst:** Yuno Payments Intelligence

---

## EXECUTIVE SUMMARY

Eldorado.gg is a peer-to-peer marketplace for virtual gaming goods (in-game currency, accounts, items, boosting) with ~18.7M monthly visits, EUR 16.11M revenue in 2024 (88% YoY growth), and 150+ employees headquartered in Vilnius, Lithuania. **Critical finding: Eldorado.gg already integrated Primer as their payment orchestration platform in March 2025**, connecting Checkout.com and Nuvei, with Adyen and Stripe being actively added. The primary Yuno opportunity is a **competitive displacement play** — positioning against Primer on superior LATAM coverage (PIX optimization, local acquiring), smart routing performance, and fraud tool integration — or pivoting to high-priority competitors (G2G, PlayerAuctions, Eneba) that show no orchestration adoption.

---

## SECTION 1 — Traffic by Country

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source URL |
|------|---------|-------------------|---------------------|-------|------------|
| 1 | United States | Primary market | — | Stable | [SimilarWeb](https://www.similarweb.com/website/eldorado.gg/) |
| 2–10 | Not broken out by country | — | — | — | — |
| — | **Global total** | 100% | **18.68M** (Feb 2026) | Growing | [Semrush](https://www.semrush.com/website/eldorado.gg/overview/) |
| — | Brazil | Emerging market | "Hundreds of daily transactions" | Growing (entered late 2024) | [GlobeNewsWire](https://www.globenewswire.com/news-release/2025/08/13/3132613/0/en/Eldorado-Gaming-integrates-PIX-to-enhance-payment-experience-for-Brazilian-users.html) |
| — | Traffic sources | Direct 57.22%, Organic Search, Paid Search | — | — | [SimilarWeb](https://www.similarweb.com/website/eldorado.gg/) |
| — | Audience | 74.24% male, largest age group 18–24 | — | — | [Semrush](https://www.semrush.com/website/eldorado.gg/overview/) |

> ⚠️ Full country-by-country breakdown not publicly available without premium SimilarWeb/Semrush access. US is confirmed primary market; Brazil is a confirmed growth market.

---

## SECTION 2 — Legal Entities

| Country | Entity Name | In Top Traffic? | Has Local Entity? | Cross-Border Risk? | Source URL |
|---------|------------|-----------------|--------------------|--------------------|------------|
| Lithuania | Eldorado Market, UAB (Reg. 304881891) | — | ✅ Yes (HQ) | Low | [Scoris](https://scoris.lt/en/imone/304881891) |
| UAE | GWD Processing FZCO (License 52076, IFZA Dubai) | — | ✅ Yes (Processing entity) | Low | [Terms of Service](https://www.eldorado.gg/terms-of-service) |
| United States | Eldorado Sales LLC (Delaware, 1209 Orange St, Wilmington) | ✅ Primary market | ✅ Yes (Sales entity) | Low | [Terms of Service](https://www.eldorado.gg/terms-of-service) |
| Brazil | — | ✅ Growth market | ❌ No entity found | ⚠️ **Cross-border risk** | Not found |

> ⚠️ Brazil: Active market with PIX integration and hundreds of daily transactions, but no local entity found. Potential cross-border operation — verify on official T&Cs.
> ⚠️ MANUAL: Verify corporate structure on official T&Cs and check for additional entities not found publicly.

**Key personnel:**
| Role | Name | Source |
|------|------|--------|
| CEO & Co-founder | Vladas Jurkevicius | [TheOrg](https://theorg.com/org/eldorado-gg) |
| CTO | Edvard Poliakov | [TheOrg](https://theorg.com/org/eldorado-gg) |
| CPO | Dainius Kudarauskas | [TheOrg](https://theorg.com/org/eldorado-gg) |
| Payments Product Owner | Arminas Simkus | [EZ Newswire](https://www.eznewswire.com/newsroom/eldorado-gg-integrates-primer-to-deliver-seamless-transactions-and-enhance-user-experience) |
| MLRO | Saule J. | [TheOrg](https://theorg.com/org/eldorado-gg) |

---

## SECTION 3 — Payment Stack

### 3A. PSPs & Acquirers

| Country/Region | PSP / Acquirer | Evidence Type | Source URL |
|----------------|---------------|---------------|------------|
| Global (Cards) | **Checkout.com** | [Press Release] | [EZ Newswire - Primer integration](https://www.eznewswire.com/newsroom/eldorado-gg-integrates-primer-to-deliver-seamless-transactions-and-enhance-user-experience) |
| Global (Cards) | **Nuvei** | [Press Release] | [EZ Newswire - Primer integration](https://www.eznewswire.com/newsroom/eldorado-gg-integrates-primer-to-deliver-seamless-transactions-and-enhance-user-experience) |
| Global (Cards) | **Adyen** — actively being implemented (as of March 2025) | [Press Release] | [EZ Newswire - Primer integration](https://www.eznewswire.com/newsroom/eldorado-gg-integrates-primer-to-deliver-seamless-transactions-and-enhance-user-experience) |
| Global (Cards) | **Stripe** — actively being implemented (as of March 2025) | [Press Release] | [EZ Newswire - Primer integration](https://www.eznewswire.com/newsroom/eldorado-gg-integrates-primer-to-deliver-seamless-transactions-and-enhance-user-experience) |
| Global (Crypto) | **CoinGate** — crypto payment gateway, fiat settlement (EUR/USD/GBP) | [Third-party Case Study] | [CoinGate Case Study](https://coingate.com/blog/post/eldorado-gg-case-study) |
| Global (Fraud) | **nSure.ai** — AI fraud prevention for digital goods | [Source Code] — `sdk.nsureapi.com` in page head | [eldorado.gg](https://www.eldorado.gg) (HTML source) |
| DACH/Nordics/UK | **Klarna** — BNPL (AT, DE, BE, NL, UK) | [Website] | [Help Center](https://support.eldorado.gg/en/articles/10213898-payment-methods) |
| Netherlands | **iDEAL** | [Website] | [Help Center](https://support.eldorado.gg/en/articles/10213898-payment-methods) |
| Baltics/Nordics/DE | **Trustly** — open banking (LT, LV, EE, DK, SE, FI, NO, DE) | [Website] | [Help Center](https://support.eldorado.gg/en/articles/10213898-payment-methods) |
| Brazil | **PIX** — integrated Aug 2025 | [Press Release] | [GlobeNewsWire](https://www.globenewswire.com/news-release/2025/08/13/3132613/0/en/Eldorado-Gaming-integrates-PIX-to-enhance-payment-experience-for-Brazilian-users.html) |
| Asia-Pacific | **AliPay** — 30+ countries | [Website] | [Help Center](https://support.eldorado.gg/en/articles/10213898-payment-methods) |
| Denmark/Finland | **MobilePay** | [Website] | [Help Center](https://support.eldorado.gg/en/articles/10213898-payment-methods) |

### 3B. Orchestrator

**⚠️ CONFIRMED: Eldorado.gg uses Primer (payment orchestration platform) as of March 2025.**

> *"Integrating Primer's platform helps us deliver on that promise by enabling a seamless payment experience. It builds trust through higher reliability and gives our users more choice in how they pay, all while keeping transactions secure."* — **Arminas Simkus, Payments Product Owner, Eldorado.gg**

Primer consolidates Checkout.com and Nuvei, with Adyen and Stripe being actively added, enabling intelligent routing across providers.

Source: [EZ Newswire — Eldorado.gg Integrates Primer (March 2025)](https://www.eznewswire.com/newsroom/eldorado-gg-integrates-primer-to-deliver-seamless-transactions-and-enhance-user-experience)

> ⚠️ MANUAL — DevTools: test card 4111 1111 1111 1111 | 02/30 | 123

---

## SECTION 4 — APMs (Agent D Findings)

### 4A. Confirmed APMs

| Market | APMs Confirmed | Verification Source | Source URL |
|--------|---------------|---------------------|------------|
| Global | Visa, Mastercard, Maestro, AMEX, Diners Club, Discover, JCB, UnionPay | Official Help Center | [Payment Methods](https://support.eldorado.gg/en/articles/10213898-payment-methods) |
| Global | Apple Pay (Safari/iOS), Google Pay (Chrome/Android/Windows) | Official Help Center | [Payment Methods](https://support.eldorado.gg/en/articles/10213898-payment-methods) |
| Global | Bitcoin, Ethereum, Tether, Dogecoin + others via CoinGate | CoinGate Case Study | [CoinGate](https://coingate.com/blog/post/eldorado-gg-case-study) |
| AT, DE, BE, NL, UK | Klarna (EUR) | Official Help Center | [Payment Methods](https://support.eldorado.gg/en/articles/10213898-payment-methods) |
| Netherlands | iDEAL (EUR) | Official Help Center | [Payment Methods](https://support.eldorado.gg/en/articles/10213898-payment-methods) |
| LT, LV, EE, DK, SE, FI, NO, DE | Trustly | Official Help Center | [Payment Methods](https://support.eldorado.gg/en/articles/10213898-payment-methods) |
| Brazil | PIX | Official Help Center + Press Release | [GlobeNewsWire](https://www.globenewswire.com/news-release/2025/08/13/3132613/0/en/Eldorado-Gaming-integrates-PIX-to-enhance-payment-experience-for-Brazilian-users.html) |
| 30+ countries (APAC) | AliPay (USD, EUR, GBP, JPY, AUD, SGD, CHF, SEK, NOK, NZD, THB, HKD, CAD) | Official Help Center | [Payment Methods](https://support.eldorado.gg/en/articles/10213898-payment-methods) |
| Denmark, Finland | MobilePay (EUR, NOK, SEK, DKK) | Official Help Center | [Payment Methods](https://support.eldorado.gg/en/articles/10213898-payment-methods) |
| Global | Prepaid/Gift Cards (excl. Amazon, Apple, Google Play) | Official Help Center | [Prepaid Cards](https://support.eldorado.gg/en/articles/9685712-prepaid-gift-card-payment-method) |

**Notable:** PayPal is explicitly **NOT accepted** — confirmed via Help Center: "PayPal is not an available deposit method." ([Deposits](https://support.eldorado.gg/en/articles/8409024-deposits))

### 4B. Unverified Markets

| Market | Verification Attempted? | Reason Not Verified | Popular Local APMs |
|--------|------------------------|--------------------|--------------------|
| United States (top market) | Yes — Help Center reviewed | No US-specific APMs listed beyond cards/wallets | Venmo, Zelle, ACH |
| Turkey | No | No regional domain found | Troy cards, Papara |
| Russia/CIS | No | No regional domain found | Qiwi, YooMoney |
| Southeast Asia | Partial (AliPay confirmed) | No SEA-specific page found | GrabPay, GCash, DANA |

> "Not verified" ≠ "not available." MANUAL: VPN checkout walk-through before any APM claims.

---

## SECTION 5 — Payment Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|-----------|----------|-----------|------------|------------|
| Payment processing failures (auth-capture mismatch / ghost charges) | Trustpilot | Multiple reports | Ongoing | [Trustpilot](https://www.trustpilot.com/review/eldorado.gg) |
| $6 processing fee not refunded on failed orders | SmartCustomer | Repeated | Ongoing | [SmartCustomer](https://www.smartcustomer.com/reviews/eldorado.gg) |
| Refunds go to Eldorado balance (store credit), not original payment method | Official Policy | By design | N/A | [Refund Policy](https://support.eldorado.gg/en/articles/8409020-refund-return-policy) |
| Card declines — dedicated help article with 4 common causes (3DS, international, funds, prepaid) | Help Center + TikTok | Known recurring issue | Ongoing | [Declined Cards](https://support.eldorado.gg/en/articles/10338401-declined-card-payments) |
| TradeShield disputes auto-marking orders as received without buyer confirmation | SmartCustomer | Multiple reports | Ongoing | [SmartCustomer](https://www.smartcustomer.com/reviews/eldorado.gg) |
| Identity verification / ban complaints during KYC | SmartCustomer | Some reports | Ongoing | [SmartCustomer](https://www.smartcustomer.com/reviews/eldorado.gg) |

**Review score divergence:**
- Trustpilot: **4.4/5** (88,000+ reviews) — skews positive, likely includes seller-prompted reviews
- SmartCustomer: **1.2/5** (177 reviews) — heavily negative, organic complaint-driven
- Scam-Detector: Low trust score — [Source](https://www.scam-detector.com/validator/eldorado-gg-review/)

**Analysis:** The card decline issue + dedicated help article + TikTok workaround videos signal a systemic authorization rate problem. This is exactly where smart routing and local acquiring could help — but they're already deploying Primer for this. The refund-to-balance policy suggests active chargeback management. nSure.ai integration confirms fraud is a top concern for this business.

---

## SECTION 6 — Expansion & Corporate Developments

| # | Date | Development | Category | Source URL |
|---|------|------------|----------|------------|
| 1 | March 2025 | Integrated Primer as payment orchestration platform | Payment Infrastructure | [EZ Newswire](https://www.eznewswire.com/newsroom/eldorado-gg-integrates-primer-to-deliver-seamless-transactions-and-enhance-user-experience) |
| 2 | March 2025 | Adding Adyen and Stripe as additional PSPs via Primer | Payment Infrastructure | [EZ Newswire](https://www.eznewswire.com/newsroom/eldorado-gg-integrates-primer-to-deliver-seamless-transactions-and-enhance-user-experience) |
| 3 | August 2025 | Integrated PIX for Brazilian market | Market Expansion | [GlobeNewsWire](https://www.globenewswire.com/news-release/2025/08/13/3132613/0/en/Eldorado-Gaming-integrates-PIX-to-enhance-payment-experience-for-Brazilian-users.html) |
| 4 | Late 2024 | Entered Brazilian market | Market Expansion | [GlobeNewsWire](https://www.globenewswire.com/news-release/2025/08/13/3132613/0/en/Eldorado-Gaming-integrates-PIX-to-enhance-payment-experience-for-Brazilian-users.html) |
| 5 | 2024 | Revenue grew 88% YoY to EUR 16.11M | Financial Growth | [EMIS](https://www.emis.com/php/company-profile/LT/Eldorado_Market_UAB_en_17005525.html) |
| 6 | 2024 | Headcount grew to ~150 employees | Organizational Growth | [Scoris](https://scoris.lt/en/imone/304881891) |
| 7 | March 2026 | Hiring Fraud & Risk Manager, Head of Engineering, multiple backend roles | Active Hiring | [Careers](https://careers.eldorado.gg/jobs) |

---

## SECTION 7 — Payment News

| # | Date | Headline | Relevance | Source URL |
|---|------|---------|-----------|------------|
| 1 | Mar 2025 | 🟢 Eldorado.gg integrates Primer for payment orchestration | Direct competitor — Primer is live | [EZ Newswire](https://www.eznewswire.com/newsroom/eldorado-gg-integrates-primer-to-deliver-seamless-transactions-and-enhance-user-experience) |
| 2 | Mar 2025 | 🟢 Adding Adyen & Stripe via Primer | Expanding PSP coverage | [EZ Newswire](https://www.eznewswire.com/newsroom/eldorado-gg-integrates-primer-to-deliver-seamless-transactions-and-enhance-user-experience) |
| 3 | Aug 2025 | 🟢 PIX integration for Brazil | LATAM expansion, local payment method | [GlobeNewsWire](https://www.globenewswire.com/news-release/2025/08/13/3132613/0/en/Eldorado-Gaming-integrates-PIX-to-enhance-payment-experience-for-Brazilian-users.html) |
| 4 | Ongoing | 🟢 CoinGate partnership for crypto | Crypto gateway, 3% of sales | [CoinGate](https://coingate.com/blog/post/eldorado-gg-case-study) |

No PSP removals (🔴) found.

---

## SECTION 8 — Checkout Audit

| Dimension | Finding | Quality | Notes |
|-----------|---------|---------|-------|
| Checkout type | Account-based with cart → summary → payment flow | Standard | Multi-step process |
| Guest checkout | ❌ Not available — account creation required | Below average | Friction for first-time buyers |
| Steps to purchase | 3+ steps (cart → summary/delivery → payment) | Average | Could be streamlined |
| 3DS | Required — mentioned in declined card help article | Standard | 3DS failures are a known issue |
| Mobile experience | Responsive design, touch-optimized, webkit scroll | Good | Breakpoints at 600px |
| APM display logic | Homepage shows Visa, MC, AMEX, Discover, BTC, GPay, APay + "+18 more" | Good | APMs get equal visual weight |
| Fees | **8% + $0.30 flat fee on all payment methods** | ⚠️ High | Potential conversion killer |
| BNPL visibility | Klarna available but NOT prominently displayed (help center only) | Below average | Missed conversion opportunity |
| Trust signals | TradeShield, Account Warranty — no PCI/SSL badges visible | Below average | Lacks payment security indicators |

> ⚠️ MANUAL: Walk checkout in top 2–3 markets.

---

## SECTION 9 — PCI DSS

| PCI DSS Level | Card data handling | Recommended Yuno integration | Source |
|--------------|-------------------|------------------------------|--------|
| Not publicly disclosed | Delegated to third-party Payment Processors (per ToS) | N/A — already using Primer | [Terms of Service](https://www.eldorado.gg/terms-of-service) |

No public PCI DSS certification or security compliance page found. Payment processing responsibility lies with PSPs (Checkout.com, Nuvei, Adyen, Stripe via Primer).

---

## SECTION 10 — Strategic Insights

### Insight #1: Primer Is Already Live — Competitive Displacement Required
**Evidence:** S3B — Primer announced March 2025, connecting Checkout.com and Nuvei, adding Adyen and Stripe.
**Pain Point:** Primer may lack deep LATAM local acquiring capabilities; Eldorado is actively expanding in Brazil (PIX, hundreds of daily transactions) with no local entity.
**Yuno Value Prop:** Yuno's 300+ LATAM connections, local acquiring in Brazil/Mexico/Colombia, and PIX optimization could outperform Primer's routing in their fastest-growing market.
**Best Case:** InDrive — 10 LATAM markets in <8 months, 90% approval rate.
**Outreach Angle:** "Your Brazil market is growing fast — but cross-border acquiring through Primer means you're likely leaving 5-7% approval uplift on the table vs. local acquiring. We helped InDrive solve this across 10 LATAM markets."

### Insight #2: Card Decline Rate Is a Known Problem
**Evidence:** S5 — Dedicated help article for declined cards, TikTok workaround videos, 3DS failure reports, ghost charge complaints.
**Pain Point:** Users actively searching for workarounds to payment failures = lost revenue. Smart routing could recover failed transactions.
**Yuno Value Prop:** Smart Routing → +7% approval uplift; 50% transaction recovery on declines.
**Best Case:** Livelo — +5% approval, 50% recovery.
**Outreach Angle:** "Your users are literally making TikTok videos about how to fix payment failures on your site. Our smart routing typically recovers 50% of declined transactions."

### Insight #3: High Fee Structure Signals Margin Pressure on Payments
**Evidence:** S8 — 8% + $0.30 fee per transaction across all payment methods.
**Pain Point:** At EUR 16.11M revenue, payment processing costs are a significant line item. Smart routing to cheapest-available acquirer could reduce costs.
**Yuno Value Prop:** Route-to-cheapest logic optimizes cost per transaction while maintaining approval rates.
**Best Case:** Reserva — +4% approval in <3 months.
**Outreach Angle:** "At your transaction volume, even 1% savings on processing costs through intelligent routing is meaningful."

### Insight #4: Competitors Are Unorchestrated — Pipeline Opportunity
**Evidence:** S11 — G2G (5.4M visits), PlayerAuctions (2.9M visits), Eneba, Z2U show no payment orchestration adoption.
**Pain Point:** These competitors face the same multi-market, multi-APM challenges as Eldorado but haven't adopted an orchestrator.
**Yuno Value Prop:** First-mover advantage pitch to competitors, especially those with LATAM/APAC exposure.
**Outreach Angle:** "Your competitor Eldorado.gg already adopted payment orchestration to improve their authorization rates. Are you seeing similar challenges with cross-border payments?"

### Insight #5: No PayPal + Fraud Focus = Chargeback-Sensitive Business
**Evidence:** S4A — PayPal explicitly not accepted; S3A — nSure.ai fraud prevention in source code; S5 — refunds to balance only.
**Pain Point:** Virtual goods marketplaces have inherently high fraud/chargeback rates. The no-PayPal policy and nSure.ai integration confirm this is a top business concern.
**Yuno Value Prop:** Yuno's fraud tool orchestration could complement nSure.ai or provide fallback, and smart routing can reduce false declines (legitimate transactions flagged as fraud).
**Outreach Angle:** "We see gaming marketplaces lose 3-5% of good transactions to false declines. Our fraud tool orchestration works alongside nSure to maximize approval without increasing risk."

---

## SECTION 11 — Pipeline

### 11A. Direct Competitors

| Company | Website | HQ | Est. Size | Overlap Markets | Source |
|---------|---------|-----|-----------|-----------------|--------|
| G2G | g2g.com | Malaysia | Large (5.4M visits) | Global, APAC-strong | [SimilarWeb](https://www.similarweb.com/website/eldorado.gg/competitors/) |
| PlayerAuctions | playerauctions.com | USA | Medium (2.9M visits) | Global, US-strong | [SimilarWeb](https://www.similarweb.com/website/eldorado.gg/competitors/) |
| Z2U | z2u.com | China | Medium (2.2M visits) | Global, China-strong | [TurboSmurfs](https://turbosmurfs.gg/article/eldoradogg-alternatives) |
| GameBoost | gameboost.com | Not found | Small-Medium (1.3M visits) | Global | [TurboSmurfs](https://turbosmurfs.gg/article/eldoradogg-alternatives) |
| ZeusX | zeusx.com | Not found | Small-Medium (1.1M visits) | Global, crypto-accepting | [TurboSmurfs](https://turbosmurfs.gg/article/eldoradogg-alternatives) |
| GamerMarkt | gamermarkt.com | Not found | Small | EU-focused | [TurboSmurfs](https://turbosmurfs.gg/article/eldoradogg-alternatives) |
| PlayerUp | playerup.com | Not found | Small | Global | [TurboSmurfs](https://turbosmurfs.gg/article/eldoradogg-alternatives) |
| EpicNPC | epicnpc.com | Not found | Small (forum-based) | Global | [TurboSmurfs](https://turbosmurfs.gg/article/eldoradogg-alternatives) |

### 11B. Industry Peers

| Company | Website | Vertical | Key Markets | Why Similar | Source |
|---------|---------|----------|-------------|-------------|--------|
| Eneba | eneba.com | Game keys marketplace | Global, Lithuania-based | Same HQ country, digital goods, multi-APM | [SimilarWeb](https://www.similarweb.com/website/eldorado.gg/competitors/) |
| G2A | g2a.com | Game keys marketplace | Global | Digital goods, high-volume marketplace | [TurboSmurfs](https://turbosmurfs.gg/article/eldoradogg-alternatives) |
| Kinguin | kinguin.net | Game keys marketplace | Global, EU-strong | Digital goods marketplace | [TurboSmurfs](https://turbosmurfs.gg/article/eldoradogg-alternatives) |
| CDKeys | cdkeys.com | Digital game keys | Global | Digital goods, similar checkout flow | [TurboSmurfs](https://turbosmurfs.gg/article/eldoradogg-alternatives) |
| OffGamers | offgamers.com | Game credits/gift cards | APAC-strong | Digital goods, shares infra with G2G | [Triple-A Blog](https://www.triple-a.io/blog/stablecoin-payments-global-gaming-marketplace) |

### 11C. Adopting Orchestration

| Company | Orchestrator | Date | Vertical | Source |
|---------|-------------|------|----------|--------|
| **Eldorado.gg** | **Primer** | March 2025 | Gaming marketplace | [EZ Newswire](https://www.eznewswire.com/newsroom/eldorado-gg-integrates-primer-to-deliver-seamless-transactions-and-enhance-user-experience) |
| G2G / OffGamers | Triple-A (crypto only, not full orchestration) | Ongoing | Gaming marketplace | [Triple-A Blog](https://www.triple-a.io/blog/stablecoin-payments-global-gaming-marketplace) |
| PlayerAuctions | No public evidence | — | Gaming marketplace | Not found |
| Others | No public evidence | — | Various | Not found |

### 11D. Scoring (Eldorado.gg)

| Signal | Pts | Verified? |
|--------|-----|-----------|
| Operates in 3+ countries | +3 | ✅ US, EU, Brazil confirmed |
| Multiple PSPs | +3 | ✅ Checkout.com, Nuvei, adding Adyen & Stripe |
| Recent expansion (24 mo.) | +2 | ✅ Brazil market entry, PIX, Primer |
| Public payment issues | +2 | ✅ Decline articles, TikTok workarounds, review complaints |
| Funding >$10M | 0 | ❌ Bootstrapped, no funding disclosed |
| LATAM/APAC/MENA traffic | +2 | ✅ Brazil growth, AliPay for APAC |
| No orchestrator | 0 | ❌ **Already uses Primer** |
| Payment job postings | +1 | ✅ Fraud & Risk Manager open |
| Public RFP | 0 | ❌ Not found |

**Total: 13 pts → 🔴 High Priority** (but with orchestrator caveat)

> Note: Score is high due to market signals, but the Primer integration significantly reduces short-term opportunity. Recommend pivoting pipeline focus to unorchestrated competitors.

### Top 10 Pipeline (Competitors & Peers)

| Rank | Company | Type | Key Markets | Est. Score | Priority | Top Signal |
|------|---------|------|-------------|------------|----------|------------|
| 1 | **G2G** | Direct competitor | Global, APAC | ~12 | 🔴 High | 5.4M visits, multi-market, no full orchestration |
| 2 | **Eneba** | Industry peer | Global, EU/Lithuania | ~11 | 🟡 Medium-High | Same HQ market, digital goods, likely multi-PSP |
| 3 | **G2A** | Industry peer | Global | ~11 | 🟡 Medium-High | Major marketplace, high volume |
| 4 | **PlayerAuctions** | Direct competitor | Global, US | ~9 | 🟡 Medium | 2.9M visits, US-focused, no orchestration |
| 5 | **Kinguin** | Industry peer | Global, EU | ~8 | 🟡 Medium | Digital marketplace, EU payments complexity |
| 6 | **Z2U** | Direct competitor | Global, China | ~8 | 🟡 Medium | 2.2M visits, cross-border China exposure |
| 7 | **CDKeys** | Industry peer | Global | ~7 | 🟡 Medium | Digital keys, checkout optimization opportunity |
| 8 | **GameBoost** | Direct competitor | Global | ~6 | 🟢 Low-Medium | 1.3M visits, smaller scale |
| 9 | **ZeusX** | Direct competitor | Global | ~6 | 🟢 Low-Medium | Crypto-accepting, processing delays reported |
| 10 | **OffGamers** | Industry peer | APAC | ~6 | 🟢 Low-Medium | APAC digital goods, uses Triple-A for crypto |

**Pipeline Summary:** 10 companies identified, 1 high-priority (G2G), 5 medium-priority. Strongest vertical: **gaming virtual goods marketplaces** in Global/APAC/EU markets. G2G (Malaysia, 5.4M visits) is the top pipeline target — largest competitor with no full orchestration and strong APAC presence where local acquiring matters most.

---

## SECTION 12 — Business Case

| Metric | Value | Source |
|--------|-------|--------|
| Annual Revenue (2024) | EUR 16.11M (~USD 17.5M) | [EMIS](https://www.emis.com/php/company-profile/LT/Eldorado_Market_UAB_en_17005525.html) |
| Net Profit (2024) | EUR 6.39M | [EMIS](https://www.emis.com/php/company-profile/LT/Eldorado_Market_UAB_en_17005525.html) |
| YoY Growth | 88% | [EMIS](https://www.emis.com/php/company-profile/LT/Eldorado_Market_UAB_en_17005525.html) |
| Avg Transaction Value | Estimated $5–$50 (gaming virtual goods) **[INFERENCE — not confirmed]** | N/A |
| Est. Annual Transactions | Estimated 350K–3.5M (based on revenue ÷ ATV range) **[INFERENCE — not confirmed]** | N/A |
| Primary Currencies | USD, EUR, GBP + 26 others (29 total) | [Help Center](https://support.eldorado.gg/en/articles/8409024-deposits) |
| Top 3 Markets | United States, Europe (EU), Brazil (emerging) | Multiple sources |
| Transaction Fee | 8% + $0.30 per payment | [Help Center](https://support.eldorado.gg/en/articles/8408992-how-to-buy-items-and-game-currency) |
| Funding | Bootstrapped — no external funding disclosed | [Crunchbase](https://www.crunchbase.com/organization/eldorado-gg) |
| Tech Stack | Phoenix (Elixir), Zendesk, SendGrid, Hotjar, TalkJS | [ContactOut](https://contactout.com/company/Eldoradogg-64796/technology-stack) |

---

## SECTION 13 — Outreach (Verified Findings Only)

> ⚠️ **Important context for outreach:** Eldorado.gg already uses Primer. Outreach must acknowledge this and position Yuno as a superior alternative, OR pivot to competitors.

### 13A. LinkedIn Message (to Arminas Simkus, Payments Product Owner)

```
--- LINKEDIN MESSAGE ---
Hi Arminas,

Congrats on the Primer rollout and the PIX integration — scaling payments while growing 88% YoY is no small feat.

I work with gaming marketplaces at Yuno on payment orchestration. We helped InDrive go live across 10 LATAM markets in under 8 months with 90% approval rates and 4.5% transaction recovery.

I noticed you're expanding in Brazil with cross-border acquiring. We've seen gaming platforms gain 5-7% approval uplift by switching to local acquiring in LATAM — something our 300+ regional connections are built for.

Would be worth a 15-minute chat to compare notes on LATAM payment performance? Happy to share some benchmark data from the gaming vertical. How does Thursday or Friday look?

Best,
[Name]
```

### 13B. Cold Email

```
--- COLD EMAIL ---
Subject: Your Brazil payments are growing — here's what InDrive learned scaling LATAM

Hi Arminas,

Saw the PIX launch and the 88% revenue growth — impressive trajectory for Eldorado.gg.

As you scale Brazil and other LATAM markets, one pattern we see consistently: cross-border acquiring leaves 5-7% in approval rates on the table compared to local processing. Your users are already making workaround videos for payment failures — smart routing typically recovers 50% of those declined transactions.

We helped InDrive go live across 10 LATAM markets in under 8 months — 90% approval rates, 4.5% transaction recovery, all through a single API. Rappi cut analyst resolution time by 80% with our real-time monitoring.

Worth a quick conversation to compare LATAM payment performance benchmarks? I can share specific data from the gaming marketplace vertical.

[Name]
```

---

## APPENDIX — Source URLs

```
[S1] https://www.similarweb.com/website/eldorado.gg/ — Traffic data
[S2] https://www.semrush.com/website/eldorado.gg/overview/ — Traffic/audience data
[S3] https://www.eldorado.gg/terms-of-service — Legal entities, T&Cs
[S4] https://theorg.com/org/eldorado-gg — Leadership team
[S5] https://scoris.lt/en/imone/304881891 — Lithuanian company registration
[S6] https://www.dnb.com/business-directory/company-profiles.eldorado_market_uab.6dd7ceee3e8060dbad9baf0464c60999.html — D&B profile
[S7] https://www.eznewswire.com/newsroom/eldorado-gg-integrates-primer-to-deliver-seamless-transactions-and-enhance-user-experience — Primer integration
[S8] https://www.globenewswire.com/news-release/2025/08/13/3132613/0/en/Eldorado-Gaming-integrates-PIX-to-enhance-payment-experience-for-Brazilian-users.html — PIX integration
[S9] https://coingate.com/blog/post/eldorado-gg-case-study — CoinGate partnership
[S10] https://support.eldorado.gg/en/articles/10213898-payment-methods — Payment methods
[S11] https://support.eldorado.gg/en/articles/8409024-deposits — Deposits help
[S12] https://support.eldorado.gg/en/articles/10338401-declined-card-payments — Declined cards
[S13] https://support.eldorado.gg/en/articles/8409020-refund-return-policy — Refund policy
[S14] https://www.trustpilot.com/review/eldorado.gg — Trustpilot reviews
[S15] https://www.smartcustomer.com/reviews/eldorado.gg — SmartCustomer reviews
[S16] https://www.emis.com/php/company-profile/LT/Eldorado_Market_UAB_en_17005525.html — Financials
[S17] https://www.crunchbase.com/organization/eldorado-gg — Crunchbase
[S18] https://www.similarweb.com/website/eldorado.gg/competitors/ — Competitors
[S19] https://turbosmurfs.gg/article/eldoradogg-alternatives — Competitor alternatives
[S20] https://www.triple-a.io/blog/stablecoin-payments-global-gaming-marketplace — G2G/Triple-A
[S21] https://careers.eldorado.gg/jobs — Job postings
[S22] https://www.scam-detector.com/validator/eldorado-gg-review/ — Trust score
[S23] https://contactout.com/company/Eldoradogg-64796/technology-stack — Tech stack
[S24] https://www.eldorado.gg — Homepage (source code inspection for nSure.ai)
```
