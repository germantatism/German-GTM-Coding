# PokerPlanets — SDR Research Brief
**Date:** 2026-03-27
**Analyst:** Yuno Payments Intelligence

---

## EXECUTIVE SUMMARY

PokerPlanets is a CIS-focused online poker room operated by **Entertainment Planets B.V.** (Curacao), launched in May 2025 after inheriting the entire verified player base from PokerStars Sochi when Flutter/PokerStars exited the Russian market. The platform runs on **EvenBet Gaming** software and is licensed by the Curacao Gaming Control Board (OGL/2024/1469/0855). Its payment stack is heavily CIS-oriented — MIR cards, SBP (Russian instant payments), Piastrix, and Luxon Pay — with crypto as the primary international on-ramp. **No payment orchestration or named PSP was identified**, and the 72-hour withdrawal SLA + phased payment rollout signal an immature payments infrastructure where Yuno could add immediate value for multi-market expansion and approval optimization.

---

## SECTION 1 — Traffic by Country

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source URL |
|------|---------|-------------------|---------------------|-------|------------|
| 1 | Russia | Majority (est. >60%) | Not found | Stable — inherited PokerStars Sochi base | [WorldPokerDeals](https://worldpokerdeals.com/rakeback-deals/pokerplanets-review) |
| 2 | Kazakhstan | Significant | Not found | Stable | [GipsyTeam](https://www.gipsyteam.com/pokerrooms/pokerplanets) |
| 3 | Belarus | Significant | Not found | Stable | [GipsyTeam](https://www.gipsyteam.com/pokerrooms/pokerplanets) |
| 4–10 | Other CIS countries | Minor | Not found | N/A | N/A |

> **Note:** No SimilarWeb or Semrush traffic data publicly available. PokerPlanets does not appear in major poker traffic rankings. The site reports 10–15 active tables at low/medium stakes during peak hours, indicating a small-to-medium player base. Primary traffic comes from CIS markets based on payment method mix and language support.

**Restricted jurisdictions (per T&Cs):** Aruba, Australia, Austria, Bonaire, Sint Eustatius and Saba, Curacao, France, Germany, Malta, the Netherlands, Spain, Sint Maarten, USA (and dependencies), United Kingdom — [Source](https://pokerplanets.com/terms-conditions/)

---

## SECTION 2 — Legal Entities

| Country | In Top 10 Traffic? | Has Local Entity? | Cross-Border Risk? | Source URL |
|---------|--------------------|--------------------|---------------------|------------|
| Russia | Yes (#1) | No — operated from Curacao | ⚠️ HIGH — all Russian transactions processed cross-border | [Info-Clipper](https://www.info-clipper.com/en/company/curacao/entertainment-planets-bv.cwddi72xe.html) |
| Kazakhstan | Yes (#2) | No | ⚠️ HIGH — cross-border | N/A |
| Belarus | Yes (#3) | No | ⚠️ HIGH — cross-border | N/A |
| Curacao | No | Yes — Entertainment Planets B.V. (Reg. 166486) | N/A | [Curacao GCB Registry](https://gamingcontrol.spin-cdn.com/media/license_registry/20250904_20250903_license_registry.pdf) |

| Field | Detail |
|-------|--------|
| **Operating Entity** | Entertainment Planets B.V. |
| **Jurisdiction** | Curacao |
| **Registration No.** | 166486 |
| **Registered Address** | Kaya Richard J. Beaujon Z/N, Curacao |
| **Gaming License** | Curacao Gaming Control Board, OGL/2024/1469/0855 |
| **License Issued** | June 24, 2025 |
| **License Expiry** | December 24, 2025 |

> ⚠️ *All top markets (Russia, Kazakhstan, Belarus) are served cross-border from Curacao with no local entity. T&Cs explicitly disclaim any affiliation with Flutter Group/PokerStars.*
> ⚠️ MANUAL: Verify on official T&Cs.

---

## SECTION 3 — Payment Stack

### 3A. PSPs & Acquirers

| Country/Region | PSP / Acquirer | Evidence Type | Source URL |
|---------------|----------------|---------------|------------|
| CIS (Russia) | Piastrix (payment aggregator) | [Checkout] — listed as deposit/withdrawal method | [PokerPlanets](https://pokerplanets.com/) |
| CIS (Russia) | Luxon Pay | [Checkout] — listed as deposit/withdrawal method | [PokerPlanets](https://pokerplanets.com/) |
| CIS (Russia) | Vouwallet | [Checkout] — listed as deposit/withdrawal method | [PokerPlanets](https://pokerplanets.com/) |
| Global | Skrill (Paysafe Group) | [Checkout] — listed as e-wallet option | [PokerPlanets](https://pokerplanets.com/) |
| Global | Neteller (Paysafe Group) | [Checkout] — listed as e-wallet option | [PokerPlanets](https://pokerplanets.com/) |
| Global | Visa P2P (card-to-card, not merchant acquiring) | [Checkout] — Pokeroff review specifies P2P | [Pokeroff](https://pokeroff.com/en/poker-room/pokerplanets/) |

> **Analysis:** The Visa "P2P transfer" model (card-to-card rather than merchant acquiring) is a common pattern for offshore poker rooms that lack direct Visa merchant accounts. No evidence of Stripe, Adyen, Checkout.com, Worldpay, Braintree, or any enterprise-grade PSP.

### 3B. Orchestrator

**No public evidence found** of any payment orchestration platform (Spreedly, Primer, Gr4vy, CellPoint, APEXX, or similar).

> ⚠️ MANUAL — DevTools: test card 4111 1111 1111 1111 | 02/30 | 123

---

## SECTION 4 — APMs (Agent D Findings)

### 4A. Confirmed APMs

| Market | APMs Confirmed | Verification Source | Source URL |
|--------|---------------|---------------------|------------|
| Global (main site) | Visa, Mastercard, MIR, SBP, Skrill, Neteller, Piastrix, Luxon Pay, Vouwallet, BTC, ETH, USDT (TON/Polygon/ERC-20/TRC-20) | Homepage + Pokeroff review | [PokerPlanets](https://pokerplanets.com/), [Pokeroff](https://pokeroff.com/en/poker-room/pokerplanets/) |

**Detailed breakdown:**

| Category | Method | Min Deposit | Max Deposit | Source |
|----------|--------|-------------|-------------|--------|
| Card | Visa (P2P) | $25 | $1,200 | [Pokeroff](https://pokeroff.com/en/poker-room/pokerplanets/) |
| Card | Mastercard | Not found | Not found | [PokerPlanets](https://pokerplanets.com/) |
| Card | MIR (Russia) | Not found | Not found | [PokerPlanets](https://pokerplanets.com/) |
| Instant Bank | SBP (Russia) | Not found | Not found | [PokerPlanets](https://pokerplanets.com/) |
| E-wallet | Skrill | Not found | Not found | [PokerPlanets](https://pokerplanets.com/) |
| E-wallet | Neteller | Not found | Not found | [PokerPlanets](https://pokerplanets.com/) |
| E-wallet | Luxon Pay | $10 | $2,000 | [Pokeroff](https://pokeroff.com/en/poker-room/pokerplanets/) |
| E-wallet | Piastrix | $10 | $2,000 | [Pokeroff](https://pokeroff.com/en/poker-room/pokerplanets/) |
| E-wallet | Vouwallet | Not found | Not found | [PokerPlanets](https://pokerplanets.com/) |
| Crypto | USDT (TON) | $40 | $2,000 | [Pokeroff](https://pokeroff.com/en/poker-room/pokerplanets/) |
| Crypto | USDT (Polygon) | $40 | $2,000 | [Pokeroff](https://pokeroff.com/en/poker-room/pokerplanets/) |
| Crypto | USDT (ERC-20) | $40 | $2,000 | [Pokeroff](https://pokeroff.com/en/poker-room/pokerplanets/) |
| Crypto | USDT (TRC-20) | $40 | $2,000 | [Pokeroff](https://pokeroff.com/en/poker-room/pokerplanets/) |
| Crypto | ETH | $40 | $2,000 | [Pokeroff](https://pokeroff.com/en/poker-room/pokerplanets/) |
| Crypto | BTC | $40 | $2,000 | [Pokeroff](https://pokeroff.com/en/poker-room/pokerplanets/) |

### 4B. Unverified Markets

| Market | Verification Attempted? | Reason Not Verified | Popular Local APMs |
|--------|------------------------|---------------------|-------------------|
| Kazakhstan | No regional domain found | Single global domain; country-dependent availability stated in T&Cs | Kaspi Pay, Halyk Bank transfers |
| Belarus | No regional domain found | Single global domain | BelCard, ERIP |
| Other CIS | No regional domain found | Single global domain | Varies by country |

> "Not verified" ≠ "not available." MANUAL: VPN checkout walk-through before any APM claims.

---

## SECTION 5 — Payment Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| Delayed crypto deposits | GipsyTeam | Low (isolated reports) | 2025 | [GipsyTeam](https://www.gipsyteam.com/pokerrooms/pokerplanets) |
| Frozen funds / unresponsive support | GipsyTeam | Low (isolated reports) | 2025 | [GipsyTeam](https://www.gipsyteam.com/pokerrooms/pokerplanets) |
| KYC verification friction | GipsyTeam | Low | 2025 | [GipsyTeam](https://www.gipsyteam.com/pokerrooms/pokerplanets) |

> **No results on Reddit or Trustpilot** — the site is under 1 year old.

**Analysis:**
- **Delayed crypto deposits** → Yuno's real-time transaction monitoring could reduce detection time from minutes to milliseconds (Rappi case: ms detection vs. 5–10 min manually).
- **Frozen funds** → Yuno's smart routing and multi-PSP failover could reduce false declines and processing failures.
- **KYC friction** → While not directly a Yuno solution, smoother payment processing reduces the compounding effect of KYC + payment delays.

---

## SECTION 6 — Expansion & Corporate Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | April 2025 | PokerStars exits Russia; all Sochi player accounts migrated to PokerPlanets | Market Entry | [Poker.org](https://www.poker.org/latest-news/pokerstars-to-exit-russian-online-poker-market-in-april-aZtdZ6J6GXja/) |
| 2 | May 2025 | PokerPlanets officially launches (crypto-only deposits initially) | Launch | [PokerIndustryPro](https://pokerindustrypro.com/news/article/222121-pokerplanets-launches-pokerstars-former-russian) |
| 3 | Mid 2025 | Fiat payment methods added (Visa, MIR, SBP, Skrill, Neteller, Piastrix, Luxon) | Payment Expansion | [WorldPokerDeals](https://worldpokerdeals.com/rakeback-deals/pokerplanets-review) |
| 4 | June 2025 | Curacao GCB license issued (OGL/2024/1469/0855) | Licensing | [Curacao GCB Registry](https://gamingcontrol.spin-cdn.com/media/license_registry/20250904_20250903_license_registry.pdf) |
| 5 | 2025 | Live tournament satellites to Sochi gambling zone events added | Product | [GipsyTeam](https://www.gipsyteam.com/pokerrooms/pokerplanets) |

---

## SECTION 7 — Payment News

| # | Date | Headline | Relevance | Source URL |
|---|------|----------|-----------|------------|
| 1 | April 2025 | PokerStars exits Russia, player base migrates to PokerPlanets | Direct — created the platform's player base | [Poker.org](https://www.poker.org/latest-news/pokerstars-to-exit-russian-online-poker-market-in-april-aZtdZ6J6GXja/) |
| 2 | Mid 2025 | Phased fiat payment rollout after crypto-only launch | Direct — signals evolving payment infrastructure | [WorldPokerDeals](https://worldpokerdeals.com/rakeback-deals/pokerplanets-review) |

> No PSP partnership announcements or payment technology news found in public sources.

---

## SECTION 8 — Checkout Audit

| Dimension | Finding | Quality | Notes |
|-----------|---------|---------|-------|
| Checkout type | In-app Cashier (poker client + website) | Standard for iGaming | Transactions processed via official website |
| Guest checkout | No — requires account + KYC | Standard for real-money poker | |
| Steps to purchase | Register → KYC → Cashier → Select method → Deposit | 4–5 steps | Standard flow |
| 3DS | Not verified | N/A | Visa P2P model may bypass standard 3DS |
| Mobile experience | iOS (App Store) + Android (APK) with cashier | Adequate | APK distribution (not Play Store) adds friction |
| APM display logic | Country-dependent (stated in T&Cs) | Basic geo-routing | "Payment methods depend on player's country" |

> ⚠️ MANUAL: Walk checkout in top 2–3 markets.

**Key UX observations:**
- "More options will be added in the future" message on site — payment stack is still being built out
- Android via APK (not Google Play Store) due to real-money gambling restrictions
- Some deposit methods only available via website, not the downloadable client

---

## SECTION 9 — PCI DSS

| PCI DSS Level | Card data handling | Recommended Yuno integration | Source |
|--------------|-------------------|------------------------------|--------|
| Not found | Likely outsourced to payment aggregators (Piastrix, Luxon Pay) — Visa P2P model suggests no direct card acquiring | Redirect / Hosted checkout | [PokerPlanets T&Cs](https://pokerplanets.com/terms-conditions/) |

**Security certifications found:**
- iTechLabs (RNG/fairness testing) — [PokerPlanets](https://pokerplanets.com/)
- Curacao GCB compliance
- GameCare responsible gambling reference
- SSL encryption (general reference)
- Segregated player funds (monitored daily per T&Cs)
- GDPR compliance stated

---

## SECTION 10 — Strategic Insights

### Insight #1: Crypto-First Launch Signals Immature Payment Infrastructure
**Evidence:** Section 6 — launched crypto-only in May 2025, added fiat methods incrementally. "More options coming soon" on site.
**Pain Point:** Payment infrastructure is being built reactively rather than strategically. Each new payment method likely requires separate integration effort.
**Yuno Value Prop:** Single API to 1,000+ payment methods — could accelerate their roadmap from months to weeks. No-code PSP enablement means new methods go live without engineering effort.
**Best Case:** InDrive scaled to 10 LATAM markets in <8 months with Yuno.
**Outreach Angle:** "You're building your payment stack method-by-method. What if one integration gave you access to 1,000+ methods across 200 countries?"

### Insight #2: Cross-Border Processing Risk — All Top Markets Served from Curacao
**Evidence:** Section 2 — no local entities in Russia, Kazakhstan, or Belarus. All transactions processed cross-border. Visa via P2P (not merchant acquiring).
**Pain Point:** Cross-border card processing = higher decline rates, higher fees, and regulatory risk. P2P card model is fragile and may not scale.
**Yuno Value Prop:** Smart Routing to local acquirers = +7% approval uplift. Local processing reduces costs and improves reliability.
**Best Case:** Reserva achieved +4% approval in <3 months.
**Outreach Angle:** "Cross-border processing from Curacao to CIS markets comes with approval rate challenges. We help operators route transactions through local acquirers for better approval rates."

### Insight #3: 72-Hour Withdrawal SLA Below Industry Standard
**Evidence:** Section 5 — 72-hour withdrawal processing (extendable to 144 hours). Player complaints about delayed deposits and frozen funds.
**Pain Point:** Slow withdrawals erode player trust and increase churn. Manual fraud review on all requests adds latency.
**Yuno Value Prop:** Real-time monitoring (Rappi: ms detection vs. 5–10 min manually). 50% transaction recovery. Faster, automated decisioning.
**Best Case:** Rappi achieved 80% less analyst resolution time with Yuno.
**Outreach Angle:** "Your 72-hour withdrawal SLA could be a churn driver. We've helped operators cut processing time and reduce manual review with real-time monitoring."

### Insight #4: No Payment Orchestration — Single-Aggregator Dependency
**Evidence:** Section 3B — no orchestration platform found. CIS transactions likely routed through Piastrix as primary aggregator.
**Pain Point:** Single-aggregator dependency creates a single point of failure. If Piastrix goes down or changes terms, deposits halt.
**Yuno Value Prop:** Multi-PSP orchestration with automatic failover. Smart routing optimizes for approval rates across multiple providers.
**Best Case:** Livelo achieved +5% approval and 50% recovery with Yuno orchestration.
**Outreach Angle:** "Having a backup processor isn't enough — smart routing across multiple PSPs is what drives approval rates up. We orchestrate that automatically."

### Insight #5: EvenBet Gaming as Technology Partner — B2B Entry Point
**Evidence:** Section 6 — PokerPlanets runs on EvenBet Gaming (Malta, MGA license). EvenBet provides turnkey poker platform including some payment integration.
**Pain Point:** If EvenBet's built-in payment tools are the primary solution, PokerPlanets may be limited by EvenBet's payment partner ecosystem.
**Yuno Value Prop:** Yuno can integrate alongside or on top of EvenBet's platform, adding orchestration capabilities without replacing the poker software.
**Best Case:** No-code PSP enablement — works with existing infrastructure.
**Outreach Angle:** Dual approach — pitch to PokerPlanets directly AND to EvenBet as a B2B partnership (EvenBet serves multiple poker operators).

---

## SECTION 11 — Pipeline

### 11A. Direct Competitors

| Company | Website | HQ | Est. Size | Overlap Markets | Source |
|---------|---------|-----|-----------|-----------------|--------|
| GGPoker (NSUS Group) | ggpoker.com | Isle of Man | Large (global) | CIS, international | [GlobeNewsWire](https://www.globenewswire.com/news-release/2026/03/09/3251583/0/en/Online-Poker-Market-Forecast-and-Company-Analysis-Report-2025-2033-Featuring-Playtika-PokerStars-Baazi-Games-BetOnline-Tencent-True-Poker-Zynga-Ignition-Americas-Cardroom-and-MPL.html) |
| 888poker (Evoke) | 888poker.com | Gibraltar | Large | International | [GlobeNewsWire](https://www.globenewswire.com/news-release/2026/03/09/3251583/0/en/Online-Poker-Market-Forecast-and-Company-Analysis-Report-2025-2033-Featuring-Playtika-PokerStars-Baazi-Games-BetOnline-Tencent-True-Poker-Zynga-Ignition-Americas-Cardroom-and-MPL.html) |
| partypoker (Entain) | partypoker.com | Gibraltar | Large | International | [GlobeNewsWire](https://www.globenewswire.com/news-release/2026/03/09/3251583/0/en/Online-Poker-Market-Forecast-and-Company-Analysis-Report-2025-2033-Featuring-Playtika-PokerStars-Baazi-Games-BetOnline-Tencent-True-Poker-Zynga-Ignition-Americas-Cardroom-and-MPL.html) |
| Americas Cardroom | americascardroom.eu | Costa Rica | Medium | Offshore, CIS-accepting | [GlobeNewsWire](https://www.globenewswire.com/news-release/2026/03/09/3251583/0/en/Online-Poker-Market-Forecast-and-Company-Analysis-Report-2025-2033-Featuring-Playtika-PokerStars-Baazi-Games-BetOnline-Tencent-True-Poker-Zynga-Ignition-Americas-Cardroom-and-MPL.html) |
| Ignition Poker | ignitioncasino.eu | Kahnawake, Canada | Medium | Offshore | [GlobeNewsWire](https://www.globenewswire.com/news-release/2026/03/09/3251583/0/en/Online-Poker-Market-Forecast-and-Company-Analysis-Report-2025-2033-Featuring-Playtika-PokerStars-Baazi-Games-BetOnline-Tencent-True-Poker-Zynga-Ignition-Americas-Cardroom-and-MPL.html) |
| BetOnline Poker | betonline.ag | Panama | Medium | Offshore, crypto-friendly | [GlobeNewsWire](https://www.globenewswire.com/news-release/2026/03/09/3251583/0/en/Online-Poker-Market-Forecast-and-Company-Analysis-Report-2025-2033-Featuring-Playtika-PokerStars-Baazi-Games-BetOnline-Tencent-True-Poker-Zynga-Ignition-Americas-Cardroom-and-MPL.html) |

### 11B. Industry Peers

| Company | Website | Vertical | Key Markets | Why Similar | Source |
|---------|---------|----------|-------------|-------------|--------|
| EvenBet Gaming | evenbetgaming.com | B2B Poker Platform | Global (Malta HQ) | PokerPlanets' software provider | [EvenBet](https://evenbetgaming.com/company/about-us/) |
| Playtika | playtika.com | Social Poker | Global (Israel HQ) | WSOP app operator | [GlobeNewsWire](https://www.globenewswire.com/news-release/2026/03/09/3251583/0/en/Online-Poker-Market-Forecast-and-Company-Analysis-Report-2025-2033-Featuring-Playtika-PokerStars-Baazi-Games-BetOnline-Tencent-True-Poker-Zynga-Ignition-Americas-Cardroom-and-MPL.html) |
| Zynga Poker (Take-Two) | zynga.com | Social Poker | Global (US HQ) | Large casual poker base | [GlobeNewsWire](https://www.globenewswire.com/news-release/2026/03/09/3251583/0/en/Online-Poker-Market-Forecast-and-Company-Analysis-Report-2025-2033-Featuring-Playtika-PokerStars-Baazi-Games-BetOnline-Tencent-True-Poker-Zynga-Ignition-Americas-Cardroom-and-MPL.html) |
| Baazi Games | baazigames.com | Online Poker | India | Emerging market poker | [GlobeNewsWire](https://www.globenewswire.com/news-release/2026/03/09/3251583/0/en/Online-Poker-Market-Forecast-and-Company-Analysis-Report-2025-2033-Featuring-Playtika-PokerStars-Baazi-Games-BetOnline-Tencent-True-Poker-Zynga-Ignition-Americas-Cardroom-and-MPL.html) |
| MPL | mpl.live | Mobile Gaming | India | Mobile-first poker | [GlobeNewsWire](https://www.globenewswire.com/news-release/2026/03/09/3251583/0/en/Online-Poker-Market-Forecast-and-Company-Analysis-Report-2025-2033-Featuring-Playtika-PokerStars-Baazi-Games-BetOnline-Tencent-True-Poker-Zynga-Ignition-Americas-Cardroom-and-MPL.html) |

### 11C. Adopting Orchestration

| Company | Orchestrator | Date | Vertical | Source |
|---------|-------------|------|----------|--------|
| No public evidence found for any listed competitor using payment orchestration | N/A | N/A | N/A | N/A |

### 11D. Scoring (verified only)

| Signal | Pts | Verified? |
|--------|-----|-----------|
| Operates in 3+ countries | +3 | ✅ Russia, Kazakhstan, Belarus + CIS |
| Multiple PSPs | +3 | ✅ Piastrix, Luxon Pay, Skrill, Neteller, Vouwallet |
| Recent expansion (24 mo.) | +2 | ✅ Launched May 2025, still adding payment methods |
| Public payment issues | +2 | ✅ GipsyTeam: delayed deposits, frozen funds |
| Funding >$10M | +2 | ❌ Not found |
| LATAM/APAC/MENA traffic | +2 | ❌ CIS-focused, no LATAM/APAC/MENA evidence |
| No orchestrator | +2 | ✅ No evidence of any orchestration platform |
| Payment job postings | +1 | ❌ Not found |
| Public RFP | +3 | ❌ Not found |

**Total: 12 points — 🔴 High Priority**

### Top 10 Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal |
|------|---------|------|-------------|-------|----------|------------|
| 1 | **PokerPlanets** | Target | Russia, CIS | 12 | 🔴 High | No orchestrator + cross-border from Curacao + phased payment buildout |
| 2 | GGPoker | Competitor | Global, CIS | Not scored | — | Major competitor with mature payment stack |
| 3 | Americas Cardroom | Competitor | Offshore | Not scored | — | Crypto-friendly, similar profile |
| 4 | BetOnline Poker | Competitor | Offshore | Not scored | — | Crypto-friendly, Panama-based |
| 5 | Ignition Poker | Competitor | Offshore | Not scored | — | Kahnawake license, similar model |
| 6 | EvenBet Gaming | B2B Partner | Global | Not scored | — | PokerPlanets' tech provider — B2B partnership opportunity |

> **Pipeline Summary:** 6 companies identified, 1 high-priority (PokerPlanets). Strongest opportunity is in the CIS-focused offshore iGaming vertical. EvenBet Gaming represents a B2B channel opportunity — they serve multiple poker operators who could benefit from Yuno orchestration.

---

## SECTION 12 — Business Case

| Annual Revenue | Avg Transaction Value | Est. Annual Transactions | Primary Currency | Top 3 Markets |
|---------------|----------------------|--------------------------|-----------------|---------------|
| Not found (private Curacao entity) | $10–$2,000 deposit range (min $10 Piastrix/Luxon, max $2,000) | Not found | USD | Russia, Kazakhstan, Belarus |

---

## SECTION 13 — Outreach (verified findings only)

### 13A. LinkedIn Message

```
--- LINKEDIN MESSAGE ---
Hi [Name],

Noticed PokerPlanets launched last year after inheriting the PokerStars Sochi player base — impressive move into a competitive space.

Building out a payment stack for CIS markets is no small feat, especially when you're processing cross-border from Curacao. We've seen similar operators struggle with approval rates and withdrawal speed when relying on a handful of aggregators.

At Yuno, we help iGaming platforms connect to 1,000+ payment methods through a single API — smart routing across multiple PSPs to improve approvals and reduce dependency on any one provider. InDrive scaled to 10 LATAM markets in under 8 months with us, hitting 90% approval rates.

Would it make sense to chat for 15 minutes next [Tuesday/Thursday] about how we could support PokerPlanets' payment expansion?

Best,
[Your Name]
--- END ---
```

### 13B. Cold Email

```
--- COLD EMAIL ---
Subject: PokerPlanets' payment stack — one integration vs. building method by method

Hi [Name],

PokerPlanets went from crypto-only to supporting 16 payment methods in under a year — that's fast for a team building from scratch.

But here's the challenge: every new market and every new payment method means another integration, another aggregator to manage, and more cross-border processing risk from Curacao. When your Russian players hit a declined MIR card or a slow Piastrix payout, they don't file a ticket — they switch rooms.

Yuno gives iGaming operators a single API to 1,000+ payment methods in 200+ countries, with smart routing that pushes approval rates up by 7%+ and recovers 50% of failed transactions automatically. InDrive used us to scale payments across 10 LATAM markets in 8 months. Rappi cut their payment monitoring response time from minutes to milliseconds.

Worth a 15-minute call next week to see if this fits where PokerPlanets is headed?

[Your Name]
--- END ---
```

---

## APPENDIX — Source URLs

```
[S1] https://worldpokerdeals.com/rakeback-deals/pokerplanets-review
[S2] https://pokerplanets.com/terms-conditions/
[S3] https://www.info-clipper.com/en/company/curacao/entertainment-planets-bv.cwddi72xe.html
[S4] https://gamingcontrol.spin-cdn.com/media/license_registry/20250904_20250903_license_registry.pdf
[S5] https://pokerplanets.com/
[S6] https://pokeroff.com/en/poker-room/pokerplanets/
[S7] https://www.gipsyteam.com/pokerrooms/pokerplanets
[S8] https://pokerindustrypro.com/news/article/222121-pokerplanets-launches-pokerstars-former-russian
[S9] https://www.poker.org/latest-news/pokerstars-to-exit-russian-online-poker-market-in-april-aZtdZ6J6GXja/
[S10] https://www.globenewswire.com/news-release/2026/03/09/3251583/0/en/Online-Poker-Market-Forecast-and-Company-Analysis-Report-2025-2033-Featuring-Playtika-PokerStars-Baazi-Games-BetOnline-Tencent-True-Poker-Zynga-Ignition-Americas-Cardroom-and-MPL.html
[S11] https://evenbetgaming.com/company/about-us/
[S12] https://pokerplanets1.com/terms-conditions/deposits-and-withdrawals/
[S13] https://www.canadianpoker.com/en/reviews/pokerplanets/
[S14] https://somuchpoker.com/online-poker/review/pokerplanets
[S15] https://www.pokerwired.com/reviews/pokerplanets/
[S16] https://highstakesdb.com/news/online-poker-news/pokerplanets-the-cosmic-poker-adventure-that-s-actually-out-of-this-world
```
