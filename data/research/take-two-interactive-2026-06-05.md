# Take-Two Interactive — SDR Research Brief
*Yuno Payment Orchestrator | Date: 2026-06-05 (refresh of 2026-06-04 brief) | Parent: Take-Two Interactive Software, Inc. (NASDAQ: TTWO)*
*Brands: Rockstar Games · 2K · Zynga · Private Division · Gearbox*

> **REFRESH NOTE (2026-06-05):** Focused delta pass over the prior brief. **No material new payment news, PSP partnership, executive hire, earnings event, or GTA VI storefront/pre-order announcement** surfaced in the last 24–48h — the Q4 FY2026 print and FY2027 guidance (filed 2026-05-21) remain the latest events, and GTA VI pre-orders/Trailer 3 are still pegged to "late June 2026" with no monetization detail confirmed. Two corrections were applied versus the 06-04 brief: (1) **the "Swirepay" signal was a FALSE POSITIVE** — `store2k.swirepay.com` is an unrelated Indian grocery store in Santa Clara, CA, not a Take-Two property; it has been removed. (2) `checkout.2k.com` now returns HTTP 404 and is not a live standalone host; Xsolla routing on the 2K Store is re-confirmed via the live `store.2k.com` footer → `help.xsolla.com`. One new datapoint: `store.2k.com` served prices in **COP (Colombian Peso)** on a geo-localized fetch, confirming an IP-localized international storefront. Next realistic catalyst: the late-June 2026 GTA VI marketing launch.

---

## EXECUTIVE SUMMARY

Take-Two Interactive is a ~$6.72B (FY2026 net bookings, +19% YoY) global games publisher where **recurrent consumer spending is 81% of GAAP revenue** and **mobile is ~52% of net sales**. The payment landscape is fragmented across at least three rails with no public orchestration layer: the **2K Store runs on Xsolla** (merchant of record, the single strongest verified finding, re-confirmed 2026-06-05), **Zynga is aggressively building per-game direct-to-consumer web stores** to bypass the 30% app-store fee using cards + PayPal + "several payment processors," and most console/mobile purchases still route through platform billers (Sony, Microsoft, Steam, Apple, Google). With **GTA VI confirmed for November 19, 2026** and FY2027 guidance of **$8.0 to 8.2B net bookings**, Take-Two is heading into the largest monetization event in its history. The strongest Yuno wedge is Zynga's live D2C push plus the looming GTA VI microtransaction stack, both of which need routing, retries, fraud, and local methods that a single orchestration layer provides. 🔴 **High-priority target (score 17).**

---

## SECTION 1 — Traffic by Country

Take-Two has no single storefront; traffic is split across brand sites. Country-level splits sit behind the SimilarWeb paywall, so only top-country signals and totals are captured.

| Rank | Property | Est. Monthly Visits | Top Countries | Trend | Source |
|---|---|---|---|---|---|
| 1 | rockstargames.com | ~10M | United States, then Russia (75% male, 18-24 core) | Down ~2.6% MoM | [SimilarWeb](https://www.similarweb.com/website/rockstargames.com/) |
| 2 | zynga.com | ~5.1M (Sept 2024 figure) | Not found in snippet | Stale figure | [SimilarWeb](https://www.similarweb.com/website/zynga.com/) |
| 3 | 2k.com | ~3.9M (Sept 2024 figure) | Not found in snippet | Stale figure | [SimilarWeb](https://www.similarweb.com/website/take2games.com/competitors/) |
| 4 | take2games.com | ~1M (corporate/IR, not a storefront) | Not found | Stale figure | [SimilarWeb](https://www.similarweb.com/website/take2games.com/competitors/) |

**Payment-processing storefronts (the ones that matter for PSP scope):**
- **2K Store** (store.2k.com) — live D2C storefront, geo-localized (served COP/Colombian Peso pricing on a 2026-06-05 fetch). [Live](https://store.2k.com/)
- **Rockstar Store / Rockstar Warehouse** (rockstarwarehouse.com → store.rockstargames.com) — D2C store. [Live](https://www.rockstarwarehouse.com/)
- **Rockstar Games Launcher / Social Club store** (socialclub.rockstargames.com) — sells/launches Rockstar PC titles. [Live](https://socialclub.rockstargames.com/rockstar-games-launcher)
- **Zynga per-game web stores** (store.zynga.com, store.wordswithfriends.com) — D2C webshops selling in-game items/currency off app-store rails. [Live](https://store.zynga.com/)

**Cross-border flag:** ~40.8% of FY2026 net revenue is earned outside the US ([SEC 4Q26 earnings](https://www.sec.gov/Archives/edgar/data/0000946581/000162828026037260/ttwo4q26earningsrelease.htm)), and mobile (global) is ~52% of net sales, so a large share of volume is international and cross-border. The 2K Store's IP-localized currency (COP observed) is direct evidence of geo-localized international checkout.

> ⚠️ MANUAL: Country-level traffic split requires SimilarWeb paid access. 2K / Zynga / Take2 visit figures above are 2024-vintage and should be refreshed.

---

## SECTION 2 — Legal Entities

Authoritative source is the FY2026 10-K Exhibit 21.1 (EDGAR returned 403 to the fetcher, so the list below is partial from the indexed snippet).

| Country | Entity (partial list) | Has Local Entity? | Source |
|---|---|---|---|
| USA | Multiple 2K-branded entities (Delaware, New York) | ✅ | [SEC Ex.21.1 FY2026](https://www.sec.gov/Archives/edgar/data/0000946581/000162828026037434/ex-21103312026.htm) |
| United Kingdom | NaturalMotion Limited | ✅ | SEC Ex.21.1 |
| Ireland | 2K Games Dublin; Nordeus (Ireland) | ✅ | SEC Ex.21.1 |
| Spain | 2K Games Madrid | ✅ | SEC Ex.21.1 |
| China | 2K Games Chengdu; 2K Games Shanghai | ✅ | SEC Ex.21.1 |
| Czech Republic | 2K Czech | ✅ | SEC Ex.21.1 |
| Germany | Nanotribe GmbH | ✅ | SEC Ex.21.1 |
| Serbia | Nordeus (Serbia) | ✅ | SEC Ex.21.1 |

**Confidence:** HIGH that these named subsidiaries exist (official SEC filing). The roster is partial.

> ⚠️ MANUAL: Open the EDGAR Exhibit 21.1 directly for the full jurisdiction roster, and verify any LATAM / APAC consumer-facing entities on official store T&Cs. (Note: 2K Store serves COP pricing but no Colombian consumer entity was found in the partial roster — potential cross-border operation, verify on T&Cs.)

---

## SECTION 3 — Payment Stack

### 3A. PSPs & Acquirers

| Property / Region | PSP / Acquirer | Evidence Type | Source |
|---|---|---|---|
| 2K Store | **Xsolla** (merchant of record) | [Support page + Live footer] store.2k.com footer routes "Support" and "Order Lookup & Refunds" to help.xsolla.com; 2K Support routes 2K Store order/payment questions to "the Xsolla Support Team" (re-confirmed 2026-06-05) | [2K Support](https://support.2k.com/hc/en-us/articles/360061754473-How-to-Contact-the-2K-Store) · [store.2k.com](https://store.2k.com/) |
| Rockstar Warehouse / Store | **Digital River (historical) → Xsolla (current)** | [Community / reviews] — MEDIUM confidence, not a Rockstar primary source | [Trustpilot](https://www.trustpilot.com/review/rockstarwarehouse.com) |
| Zynga web stores | Cards + PayPal + Apple Pay + Google Pay + "several payment processors"; in-house payments engineering org | [Help center + Job listing] | [Zynga Store billing FAQ](https://zyngasupport.helpshift.com/hc/en/119-zynga-store/section/1421-billing/) · [Payments role](https://www.zynga.com/job-listing/principal-software-engineer-payments/) |
| Console / mobile (all brands) | Platform billers: Sony, Microsoft, Steam, Apple, Google | [Support pages] refunds routed to these processors | [2K Support](https://support.2k.com/hc/en-us/articles/44052599101971-Missing-or-Not-Delivered-VC-Content-After-Purchase) |

> **CORRECTION (2026-06-05):** The prior brief listed a "Swirepay" signal on `store2k.swirepay.com`. This was a **false positive** — that domain is "Store 2K," an Indian grocery store in Santa Clara, CA (2213 El Camino Real), built on Swirepay's e-commerce platform, with no connection to 2K Games / Take-Two. It has been removed. Separately, `checkout.2k.com` now returns HTTP 404 and is not a live standalone host (checkout is served inline by Xsolla under store.2k.com [INFERENCE]).

### 3B. Orchestrator

**No public evidence found** of Spreedly, Primer, Gr4vy, CellPoint, APEXX, or Yuno (re-confirmed 2026-06-05). No named card-PSP (Stripe, Adyen, Checkout.com, Worldpay, Braintree) was found tying the storefronts together. [INFERENCE — not confirmed] Take-Two runs a fragmented multi-storefront landscape (Xsolla MoR for 2K and current Rockstar web, Zynga in-house D2C, plus platform billers), with no single orchestration layer connecting them. This fragmentation is the natural Yuno wedge.

> ⚠️ MANUAL — DevTools: test card 4111 1111 1111 1111 | 02/30 | 123 against store.2k.com and store.zynga.com checkout to fingerprint gateways.

---

## SECTION 4 — APMs (Live Verification)

### 4A. Confirmed APMs / PSP routing

| Market / Property | Confirmed | Verification Source | Source URL |
|---|---|---|---|
| 2K Store | Routed through **Xsolla** (MoR/PSP); geo-localized currency (COP observed) | store.2k.com footer → help.xsolla.com; 2K Support text (re-confirmed 2026-06-05) | [2K Support](https://support.2k.com/hc/en-us/articles/360061754473-How-to-Contact-the-2K-Store) · [store.2k.com](https://store.2k.com/) |
| Rockstar Store | **Guest checkout available**; no checkout fees | Rockstar Support | [Order receipts](https://support.rockstargames.com/articles/1v0gPkZJ8IiKarabrFPHZU/rockstar-store-order-receipts) |
| Zynga web store | Major credit cards + PayPal + Apple Pay + Google Pay + "several payment processors" | Stash.gg + Zynga help (re-confirmed 2026-06-05) | [Zynga billing FAQ](https://zyngasupport.helpshift.com/hc/en/119-zynga-store/section/1421-billing/) |

### 4B. Unverified Markets

| Property | Verification Attempted? | Reason Not Verified | Popular Methods (NOT a gap claim) |
|---|---|---|---|
| Rockstar / Social Club store | ✅ | Store homepage exposes no payment info pre-login; support pages timed out | PayPal (third-party Knoji, unconfirmed), cards |
| 2K Store card networks / wallets | ✅ | Method logos render only at the dynamic Xsolla Pay Station step, not in static HTML | Visa/MC/Amex, PayPal, Apple Pay, Google Pay |
| Zynga (Poker, CSR2, Store) | ✅ | store.zynga.com is JS-rendered; Helpshift billing FAQs returned 403 | Cards, PayPal, Apple/Google/Amazon/Facebook billing |

> ⚠️ "Not verified" ≠ "not available." A clothing brand at **rockstaroriginal.com** (Shopify, with Shop Pay / Afterpay / Zip) is **NOT Take-Two** and must not be attributed to Rockstar Games. Likewise **store2k.swirepay.com** (Indian grocery, Santa Clara CA) is NOT Take-Two. MANUAL: VPN checkout walk-through before any APM claims.

---

## SECTION 5 — Payment Complaints

| Issue Type | Platform | Frequency | Source |
|---|---|---|---|
| Charged for virtual currency (VC) never delivered | BBB (2K, NBA 2K PC glitch) | Recurring | [BBB 2K](https://www.bbb.org/us/ca/novato/profile/interactive-media/2k-games-inc-1116-146378/complaints) |
| Refund friction — 2K "cannot refund transactions not made through 2K", redirects to retailer/platform | BBB / 2K Support | Recurring | [2K Support](https://support.2k.com/hc/en-us/articles/44052599101971-Missing-or-Not-Delivered-VC-Content-After-Purchase) |
| Double-charge for VC ($149 NBA 2K24 PS5), remedy was a bank dispute | JustAnswer | Reported | [JustAnswer](https://www.justanswer.com/software/oaic6-made-double-transaction-accident-ps-nba-2k-24.html) |
| GTA Shark Card paid (bank pending) but currency not received | JustAnswer | Reported | [JustAnswer](https://www.justanswer.com/software/m0stl-just-purchased-whale-shark-card-gta-49-99-plus-tax.html) |
| Zynga coins/chips paid for but not delivered; refunds denied | PissedConsumer (~1.2K reviews) | High | [PissedConsumer](https://zynga.pissedconsumer.com/review.html) |

**Pattern:** Across all three labels Take-Two punts nearly every payment dispute to the platform/retailer (Apple, Sony, Microsoft, Steam) rather than owning the transaction. "Charged but currency not delivered" + double-charge complaints point to auth/settlement and delivery-reconciliation pain. Yuno's real-time monitors (Rappi: millisecond detection) and unified retry/reconciliation layer map directly to this, and matter far more once D2C volume grows.

---

## SECTION 6 — Expansion & Corporate Developments

| # | Date | Development | Category | Source |
|---|---|---|---|---|
| 1 | Nov 19, 2026 | **GTA VI confirmed launch** (PS5 / Xbox Series S\|X); reaffirmed at the May 21, 2026 earnings call | Product | [Rockstar Newswire](https://www.rockstargames.com/newswire/article/ak3ak31a49a221/grand-theft-auto-vi-is-now-set-to-launch-november-19-2026) |
| 2 | June 12, 2024 | **Gearbox (Borderlands) acquisition** closed, $460M from Embracer | M&A | [BusinessWire](https://www.businesswire.com/news/home/20240327928202/en/) |
| 3 | 2025-2026 | **Zynga pursuing D2C "very aggressively"** to bypass Apple's 30% fee; per-game web stores live | Commerce | [MobileGamer.biz](https://mobilegamer.biz/zynga-is-unhappy-with-apples-30-cut-and-is-going-after-d2c-very-aggressively/) |
| 4 | Sept 2025 | Borderlands 4 launched | Product | [BusinessWire FY26](https://www.businesswire.com/news/home/20260521450562/en/) |
| 5 | Ongoing | Zynga "Principal Software Engineer - Payments" role open | Payments hiring | [Zynga careers](https://www.zynga.com/job-listing/principal-software-engineer-payments/) |
| 6 | Late June 2026 (expected) | GTA VI pre-orders + marketing campaign + Trailer 3 expected; no monetization/storefront detail confirmed as of 2026-06-05 | Watch | [TechTimes](https://www.techtimes.com/articles/317156/20260525/gta-6-release-date-locked-pre-orders-trailer-3-expected-late-june.htm) · [GamingBible](https://www.gamingbible.com/news/gta-pre-order-window-confirmed-828857-20260526) |

No confirmed CTO/CFO/VP Payments hire surfaced via SEC or web search (re-checked 2026-06-05; leadership unchanged — Strauss Zelnick CEO, Lainie Goldstein CFO). [GAP — verify on LinkedIn.]

---

## SECTION 7 — Payment News

| # | Date | Headline | Relevance | Source |
|---|---|---|---|---|
| 1 | May 2026 | FY2027 guidance **$8.0-8.2B net bookings**, GTA VI named primary driver | 🟢 Massive incoming microtransaction stream | [Insider Gaming](https://insider-gaming.com/gta-6-release-date-earnings-call/) |
| 2 | 2025-2026 | Zynga goes after D2C aggressively, "how much value am I getting for these fees?" | 🟢 Live orchestration need (multi-PSP webshops) | [MobileGamer.biz](https://mobilegamer.biz/zynga-is-unhappy-with-apples-30-cut-and-is-going-after-d2c-very-aggressively/) |
| 3 | June 2026 | GTA VI pre-orders + Trailer 3 still expected late June; monetization/web-shop details not yet confirmed (re-checked 2026-06-05, still open) | 🟡 Watch for a direct storefront announcement | [TechTimes](https://www.techtimes.com/articles/317156/20260525/gta-6-release-date-locked-pre-orders-trailer-3-expected-late-june.htm) |

No public information found on a new named PSP/fintech partnership or PSP removal for Take-Two/Rockstar/Zynga in 2025-2026 (re-confirmed 2026-06-05).

---

## SECTION 8 — Checkout Audit

| Dimension | Finding | Quality | Notes |
|---|---|---|---|
| Checkout type | Multiple: Xsolla-hosted (2K), Rockstar web store, Zynga D2C webshops, platform stores | Confirmed | No unified flow |
| Guest checkout | Available on Rockstar Store | Confirmed | [Rockstar Support](https://support.rockstargames.com/articles/1v0gPkZJ8IiKarabrFPHZU/rockstar-store-order-receipts) |
| Steps to purchase | Not measured | — | MANUAL walk-through needed |
| 3DS | Not measured | — | Likely via Xsolla on 2K |
| Mobile experience | ~52% of net sales are mobile; Zynga steering players to webshops via in-game pop-ups | Confirmed | [MobileGamer.biz](https://mobilegamer.biz/zynga-is-unhappy-with-apples-30-cut-and-is-going-after-d2c-very-aggressively/) |
| APM display logic | Geo-localized currency confirmed (2K Store served COP); per-method logos not statically visible | Partial | Renders at Xsolla Pay Station step |

> ⚠️ MANUAL: Walk checkout on store.2k.com and store.zynga.com.

---

## SECTION 9 — PCI DSS

| PCI Level | Card data handling | Recommended Yuno integration | Source |
|---|---|---|---|
| Not published | No public Take-Two/Rockstar/2K/Zynga PCI page found | Hosted Fields / vault tokenization to keep SAQ-A scope while orchestrating across Xsolla, Zynga's in-house rails, and any new GTA VI storefront | No public document |

[INFERENCE — not confirmed] Using Xsolla as merchant of record for the 2K and Rockstar web stores pushes PCI scope onto Xsolla for those flows ([Xsolla MoR](https://xsolla.com/payment-service-provider)). Zynga's in-house D2C stack would carry its own scope.

---

## SECTION 10 — Strategic Insights

### Insight #1: Fragmented multi-storefront stack, no orchestration layer
**Evidence:** §3 — Xsolla (2K + current Rockstar web), Zynga in-house D2C with "several payment processors," plus platform billers, with no orchestrator found.
**Pain Point:** No smart routing, no failover, no consolidated reporting across rails; each storefront is a separate integration to maintain.
**Yuno Value Prop:** One API above every PSP and storefront, smart routing for +7% approval uplift, single reconciliation layer.
**Best Case:** InDrive (10 markets in <8 months, 90% approval).
**Outreach Angle:** "You run Xsolla on the 2K Store, an in-house stack on Zynga's webshops, and platform billing everywhere else. As D2C grows, a single routing and reconciliation layer above all of them is where approval uplift and clean reporting come from."

### Insight #2: Zynga's aggressive D2C push is the live wedge
**Evidence:** §6/§7 — Zynga building per-game web stores to dodge Apple's 30%, accepting cards + PayPal + several processors, with an open Payments engineering role.
**Pain Point:** Standing up multi-PSP webshops per game means routing, retries, fraud, and local methods built and maintained in-house, game by game.
**Yuno Value Prop:** No-code PSP enablement, new methods and markets live in weeks, fraud and retry built in.
**Best Case:** Reserva (+4% approval in <3 months).
**Outreach Angle:** "Every percentage point you save versus the 30% app-store cut only counts if the D2C checkout converts. We help studios stand up multi-PSP webshops with routing and local methods without building it per title."

### Insight #3: GTA VI (Nov 19, 2026) is a once-in-a-cycle monetization event
**Evidence:** §7 — FY2027 guidance $8.0-8.2B net bookings, GTA VI the primary driver; RCS is already 81% of revenue.
**Pain Point:** A launch this size concentrates auth volume and fraud surface into a narrow window; Shark-Card-style microtransactions return at scale, and any direct storefront would be greenfield.
**Yuno Value Prop:** Smart routing, 50% transaction recovery, and real-time monitors that flag issues in milliseconds at peak load.
**Best Case:** Rappi (millisecond detection vs 5-10 min manual; 80% less analyst resolution time).
**Outreach Angle:** "GTA VI is the biggest monetization moment in your history. The time to have routing, recovery, and real-time monitoring in place is before the launch window, not during it."

### Insight #4: Disputes punted to platforms = no transaction ownership today
**Evidence:** §5 — across 2K, GTA, and Zynga, refunds and "charged but not delivered" issues are routed to Sony/MS/Steam/Apple/Google.
**Pain Point:** As D2C grows, Take-Two inherits the disputes, refunds, and reconciliation it currently offloads, with limited tooling to manage them.
**Yuno Value Prop:** Unified dispute/refund and reconciliation layer with real-time monitoring.
**Outreach Angle:** "Today the platforms own your payment disputes. The moment D2C scales, you own them, and that is exactly where a unified reconciliation and monitoring layer pays for itself."

---

## SECTION 11 — Pipeline

### 11A. Direct Competitors

| Company | Website | HQ | Est. Size | Overlap | Source |
|---|---|---|---|---|---|
| Electronic Arts | ea.com | Redwood City, US | ~$7.5B FY25 net rev | Global, sports/live-service | [SEC](https://www.sec.gov/Archives/edgar/data/0000712515/000071251526000053/earningspressrelease2026_0.htm) |
| Ubisoft | ubisoft.com | Saint-Mandé, FR | Top-earning 2025 | Global | [SavvyGamer](https://www.thesavvygamer.com/gaming/the-top-20-gaming-companies-of-2025-by-revenue) |
| Activision Blizzard (Microsoft) | activisionblizzard.com | Redmond, US | Part of Microsoft Gaming | Global, King mobile | SavvyGamer |
| Epic Games | epicgames.com | Cary, US | Fortnite / Epic Store | Global, D2C leader | SavvyGamer |
| Roblox | roblox.com | San Mateo, US | UGC / Robux | Global | SavvyGamer |
| NetEase Games | neteasegames.com | Hangzhou, CN | Major mobile publisher | APAC + global | SavvyGamer |

### 11B. Industry Peers (mobile / social, closest to Zynga)

| Company | Website | Vertical | Markets | Why Similar | Source |
|---|---|---|---|---|---|
| Playtika | playtika.com | Social casino | Global | Heavy IAP monetization | [SavvyGamer](https://www.thesavvygamer.com/gaming/the-top-20-gaming-companies-of-2025-by-revenue) |
| Scopely (Savvy/PIF) | scopely.com | Mobile games | Global | Monopoly Go IAP scale | SavvyGamer |
| Epic Games | epicgames.com | Platform / D2C | Global | Anti-app-store-fee D2C | SavvyGamer |

### 11C. Adopting Orchestration
No direct competitor publicly confirmed using a named third-party payment orchestrator. **Epic Games** operates its own payments/storefront (D2C/anti-fee leader); **Zynga** is building in-house D2C. Gaming D2C remains underpenetrated for third-party orchestration, a strong inbound opportunity.

### 11D. Scoring (Take-Two Interactive)

| Signal | Pts | Verified? |
|---|---|---|
| Operates in 3+ countries | +3 | ✅ (US, UK, IE, ES, CN, CZ, DE, RS) |
| Multiple PSPs | +3 | ✅ (Xsolla, Zynga "several processors", Digital River historical, platform billers) |
| Recent expansion (24 mo.) | +2 | ✅ (Gearbox close, Zynga D2C, GTA VI) |
| Public payment issues | +2 | ✅ (VC not delivered, double charges, refund friction) |
| Funding >$10M | +2 | ✅ ($6.72B net bookings, NASDAQ) |
| LATAM/APAC/MENA traffic | +2 | ✅ (China entities; mobile ~52% global; 40.8% revenue ex-US; 2K Store COP pricing) |
| No orchestrator | +2 | ✅ (no public evidence) |
| Payment job postings | +1 | ✅ (Zynga Principal SWE - Payments) |
| Public RFP | +3 | ❌ Not found |

**Score: 17 → 🔴 HIGH PRIORITY** (unchanged; dropping the Swirepay false positive does not affect "Multiple PSPs," which still holds on Xsolla + Zynga's several processors + platform billers.)

### Top 10 Pipeline (this brief)

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal |
|---|---|---|---|---|---|---|
| 1 | **Take-Two Interactive** | Target | US, EU, CN, global mobile | 17 | 🔴 | Fragmented stack + GTA VI + Zynga D2C |

**Pipeline Summary:** Take-Two is a 🔴 high-priority target. Strongest entry points are **Zynga** (live D2C, payments hiring) and the **GTA VI launch window**. Adjacent gaming-D2C peers (Epic, Playtika, Scopely, EA) form a strong vertical for Yuno's gaming motion.

---

## SECTION 12 — Business Case

| Annual Net Bookings | Recurrent Spend | Mobile Mix | Geo Split | Primary Currency |
|---|---|---|---|---|
| ~$6.72B (FY2026, +19% YoY); $8.0-8.2B FY2027 guidance | RCS 81% of GAAP revenue | ~52% net sales mobile | ~40.8% revenue ex-US | USD + global (geo-localized, e.g. COP) |

Average transaction value not disclosed publicly [ESTIMATE not available]. Sources: [BusinessWire FY26](https://www.businesswire.com/news/home/20260521450562/en/) · [SEC 4Q26 earnings](https://www.sec.gov/Archives/edgar/data/0000946581/000162828026037260/ttwo4q26earningsrelease.htm) · [SEC FY2026 10-K](https://www.sec.gov/Archives/edgar/data/0000946581/000162828026037434/ttwo-20260331.htm)

---

## SECTION 13 — Outreach

### 13A. LinkedIn Message (to Zynga / Take-Two D2C or payments leadership)

```
--- LINKEDIN MESSAGE ---
Hi [First name],

I have been following Zynga's move to take more of its monetization direct, away from the 30% app-store cut. It is the right call, and the part that decides whether it pays off is the checkout itself: routing across your processors, retries when a charge soft-declines, fraud, and the local methods players actually use.

Yuno is a single API that sits in front of your PSPs and storefronts (1,000+ methods, 200+ countries) with smart routing, unified reconciliation, and real-time monitors. InDrive used it to launch 10 markets in under 8 months at 90% approval. Reserva lifted approval +4% in under three months.

With GTA VI and a record bookings year ahead across the group, worth a 20-minute exchange on what an orchestration layer looks like before the volume hits? Tuesday or Thursday afternoon ET works on my side.

— German
```

### 13B. Cold Email

```
--- COLD EMAIL ---
Subject: Zynga D2C + GTA VI — who's routing the checkout?

Hi [First name],

Zynga going direct-to-consumer to get out from under the 30% app-store fee is a smart move, and the savings only land if the webshop checkout actually converts: routing across your processors, retries on soft declines, fraud, and the local methods players expect.

From the outside, Take-Two's payment stack looks fragmented by design: Xsolla on the 2K Store, an in-house stack on Zynga's per-game webshops, and platform billing everywhere else. That is a lot of separate pipelines with no single routing or reconciliation layer above them.

Yuno is one API in front of your PSPs and storefronts with:
• Smart routing → +7% approval uplift on average
• 50% recovery on declined attempts
• Unified reconciliation across every rail
• Real-time monitors that flag issues in milliseconds (Rappi cut analyst resolution time 80%)

InDrive scaled across 10 markets in under 8 months at 90% approval. With GTA VI and an $8B+ bookings year ahead for the group, the time to have this in place is before the launch window.

Worth 20 minutes next week? I can hold Tuesday or Thursday afternoon ET.

— German
Yuno | Payment Orchestration
```

---

## APPENDIX — Source URLs

```
[S1]  https://www.similarweb.com/website/rockstargames.com/
[S2]  https://www.similarweb.com/website/zynga.com/
[S3]  https://www.similarweb.com/website/take2games.com/competitors/
[S4]  https://store.2k.com/
[S5]  https://store.zynga.com/
[S6]  https://www.sec.gov/Archives/edgar/data/0000946581/000162828026037434/ex-21103312026.htm
[S7]  https://support.2k.com/hc/en-us/articles/360061754473-How-to-Contact-the-2K-Store
[S8]  https://help.xsolla.com/ (2K Store footer support/refund routing)
[S9]  https://store.wordswithfriends.com/ (Zynga D2C webshop)
[S10] https://www.trustpilot.com/review/rockstarwarehouse.com
[S11] https://www.zynga.com/job-listing/principal-software-engineer-payments/
[S12] https://support.2k.com/hc/en-us/articles/44052599101971-Missing-or-Not-Delivered-VC-Content-After-Purchase
[S13] https://www.bbb.org/us/ca/novato/profile/interactive-media/2k-games-inc-1116-146378/complaints
[S14] https://zynga.pissedconsumer.com/review.html
[S15] https://www.rockstargames.com/newswire/article/ak3ak31a49a221/grand-theft-auto-vi-is-now-set-to-launch-november-19-2026
[S16] https://mobilegamer.biz/zynga-is-unhappy-with-apples-30-cut-and-is-going-after-d2c-very-aggressively/
[S17] https://www.businesswire.com/news/home/20260521450562/en/
[S18] https://www.sec.gov/Archives/edgar/data/0000946581/000162828026037260/ttwo4q26earningsrelease.htm
[S19] https://insider-gaming.com/gta-6-release-date-earnings-call/
[S20] https://support.rockstargames.com/articles/1v0gPkZJ8IiKarabrFPHZU/rockstar-store-order-receipts
[S21] https://www.thesavvygamer.com/gaming/the-top-20-gaming-companies-of-2025-by-revenue
[S22] https://www.techtimes.com/articles/317156/20260525/gta-6-release-date-locked-pre-orders-trailer-3-expected-late-june.htm
[S23] https://www.gamingbible.com/news/gta-pre-order-window-confirmed-828857-20260526
```
