# SDR Research Brief — Tango (Tango Live, tango.me)
*Yuno Payment Orchestrator · Framework v8.0 · 2026-07-27*

---

## EXECUTIVE SUMMARY

Tango (TangoMe) is a live-streaming / creator-economy app (450M+ registered users, 170+ countries, virtual gifting via Coins in and Diamond payouts out) that is heavily concentrated in MENA (Egypt, Turkey), South Asia (India), the US diaspora, and CIS. The load-bearing finding: **Tango already operates a web coin store on tango.me that deliberately bypasses the Apple/Google 30% fee, incentivized with up to 40% bonus coins, and it accepts Visa/Mastercard/Amex, Fawry (Egypt), UPI + NetBanking (India), crypto stablecoins, and generic "regional payment methods."** Its underlying acquirer is undisclosed and there is **no evidence of any payment orchestrator**, while public complaints document real pain on both sides: "paid but coins never delivered" and card declines on the pay-in, and "approved but not settled" on creator payouts. **The Yuno opportunity is a dual-sided orchestration play**: smart routing, decline recovery, and local-APM acceptance across MENA/India/CIS on the web top-up, plus multi-rail redundancy and reconciliation across the 20+ payout providers Tango already juggles manually.

> Fit: 🔴 **High (16)**. Real consumer payments, emerging-market APM footprint, off-store web acquiring already live, no orchestrator, documented decline + settlement pain. Buyer sits in a payments-operations org (Tel Aviv) plus US/Cyprus finance.

---

## SECTION 1 — Traffic by Country (tango.me)

Total: mid-teens millions of monthly visits (~15.9M SimilarWeb 3-mo avg, +20% MoM; Semrush cross-check ~11.5M–16.5M). Traffic is ~66% direct, consistent with users going straight to the web store to top up.

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source URL |
|------|---------|-------------------|---------------------|-------|------------|
| 1 | United States | 18.83% | Largest slice of ~15.9M | Site +20% MoM | [SimilarWeb](https://www.similarweb.com/website/tango.me/) |
| 2 | India | 13.95% | — | Growing (#12 social in India) | [SimilarWeb](https://www.similarweb.com/website/tango.me/) |
| 3 | Egypt | 7.14% | — | — | [SimilarWeb](https://www.similarweb.com/website/tango.me/) |
| 4 | Turkey | 5.65% | — | — | [SimilarWeb](https://www.similarweb.com/website/tango.me/) |
| 5 | Russia | 5.47% | — | — | [SimilarWeb](https://www.similarweb.com/website/tango.me/) |
| — | Others (long tail) | ~49% | — | MENA/APAC/CIS tail | [SimilarWeb](https://www.similarweb.com/website/tango.me/) |

**Flags:**
- Markets >5% traffic: US, India, Egypt, Turkey, Russia.
- Heavy **MENA (Egypt, Turkey) + South Asia (India) + CIS (Russia)** concentration, the exact fragmented-local-APM footprint orchestration optimizes.
- Web top-up surface is tango.me itself (behind login on the Coin Balance page); no separate store subdomain found. Semrush cross-check: [Semrush](https://www.semrush.com/website/tango.me/overview/).

> ⚠️ MANUAL: pull a paid SimilarWeb seat for the full top-10 and to size India/Egypt/Turkey monthly visits precisely.

---

## SECTION 2 — Legal Entities

| Country | In Top Traffic? | Has Local Entity? | Cross-Border Risk? | Source URL |
|---------|-----------------|--------------------|--------------------|------------|
| United States | Yes (#1) | **TangoMe, Inc.** (Mountain View, CA; contracts all non-EU users; NY governing law) | Home base | [Terms of Use](https://www.tango.me/terms-of-use) |
| Cyprus (EU billing hub) | No (billing/ops) | **TangoMe Cyprus Limited** (reg C408288, Limassol; contracts EU users) / **TangoMe Technologies Limited** (relocation entity, 2022) | Low | [Cyprus Registry](https://cyprusregistry.com/companies/%CE%97%CE%95/408288), [Financial Mirror](https://www.financialmirror.com/2022/07/21/another-tech-firm-relocates/) |
| Israel (Tel Aviv) | No (ops) | Office described as **payments operations, analytics, customer success** | N/A | [TheOrg](https://theorg.com/org/tango-me/offices/tel-aviv) |
| India | Yes (#2) | Not found | ⚠️ Potential cross-border | — |
| Egypt | Yes (#3) | Not found | ⚠️ Potential cross-border | — |
| Turkey | Yes (#4) | Not found | ⚠️ Potential cross-border | — |

**Structure:** Dual contracting model, **TangoMe Inc. (US, non-EU users) + TangoMe Cyprus Ltd. (EU users)**; HQ relocated to Limassol in 2022 ([Invest Cyprus](https://www.investcyprus.org.cy/invest-cyprus-welcomes-tangome-inc-decision-to-relocate-offices-to-cyprus/)). Founded Sept 2009 in Mountain View by **Uri Raz** (original CEO) and **Eric Setton** (original CTO); Setton named CEO in Jan 2016 ([TechCrunch](https://techcrunch.com/2016/01/06/faltering-messaging-app-unicorn-tango-gets-a-new-ceo-to-turn-things-around/), [PRNewswire](https://www.prnewswire.com/news-releases/tango-names-eric-setton-chief-executive-officer-300200562.html)). ⚠️ **Current CEO ambiguous:** some current DB listings (Crunchbase/Invest Cyprus) still show Uri Raz, verify before use. Investors: Alibaba ($215M, 2014), DFJ, Qualcomm, Access Industries.

> ⚠️ MANUAL: confirm which entity is the billing/merchant-of-record for web coin sales in each region (US Inc. vs Cyprus Ltd.), it drives the acquiring/cross-border optimization argument.

---

## SECTION 3 — Payment Stack

**3A. PSPs & Acquirers** — Tango has two money-flow directions and three pay-in channels.

| Flow / Channel | Provider(s) | Evidence Type | Source URL |
|----------------|-------------|---------------|------------|
| Pay-in, in-app (iOS) | Apple App Store IAP (30% fee) | [Help Doc] | [Help](https://help.tango.me/en/articles/2985298-i-bought-coins-but-didn-t-receive-them-on-my-tango-balance-what-should-i-do) |
| Pay-in, in-app (Android) | Google Play IAP (30% fee) | [Help Doc] | [Help](https://help.tango.me/en/articles/2985298-i-bought-coins-but-didn-t-receive-them-on-my-tango-balance-what-should-i-do) |
| **Pay-in, WEB (the wedge)** | Direct card (Visa/MC/Amex) + Fawry + UPI/NetBanking + crypto + "regional methods"; **acquirer undisclosed** | [Help Doc] | [Help — Bonus](https://help.tango.me/en/articles/3872011-how-to-buy-coins-with-a-bonus), [Help — Crypto](https://help.tango.me/en/articles/8885625-buy-coins-with-crypto) |
| Payout (creator, outbound) | Airwallex, Tipalti/PayPal, Payoneer, Paxum, WebMoney, Mastercard Virtual Card, VISA, Crypto, PIX (BR), GCash (PH), STCPay (ME), SBP (RU), carrier billing (NG), country bank transfers | [Help Doc] | [Help — Payout platforms](https://help.tango.me/en/articles/2985211-tango-introduces-new-payout-platforms) |

Key facts:
- **Web top-up is deliberately incentivized over IAP with up to 40% bonus coins** (e.g. $49.99 web → 9,100 coins vs 6,500 in-app), a textbook Apple/Google fee-avoidance play steering volume to Tango's own acquiring ([Help — Bonus](https://help.tango.me/en/articles/3872011-how-to-buy-coins-with-a-bonus), corroborated [BitTopup](https://news.bittopup.com/news/buy-tango-coins-2026-get-40-more-with-web-recharge)).
- The **acquiring PSP behind the web card flow is not publicly disclosed.** Card + India (UPI/NetBanking) + Egypt (Fawry) + crypto on one checkout implies either a strong-MENA/India PSP or a multi-processor setup, a classic orchestration candidate, but the processor identity is unverified.
- A large **third-party UID top-up gray market** (SEAGM, BitTopup, TopUpLive, GamerMarkt, etc., some advertising 700+ methods / 123+ currencies) resells Tango coins, which itself signals **coverage gaps in Tango's own local acceptance**. These are not Tango's stack.

**3B. Orchestrator:** **No public evidence of any payment orchestrator** (no Spreedly, Primer, Gr4vy, CellPoint, APEXX). Greenfield. This is the opening.

> ⚠️ MANUAL — DevTools: log in and inspect the web Coin Balance checkout in an Egypt/India/Turkey session with test card 4111 1111 1111 1111 | 02/30 | 123 to identify the acquirer and see per-market method logic.

---

## SECTION 4 — APMs (verified)

**4A. Confirmed pay-in methods** (official Tango pages only):

| Market | Methods Confirmed (coin purchase) | Verification Source | Source URL |
|--------|-----------------------------------|---------------------|------------|
| Global web | Visa, Mastercard, Amex, bank cards | Help — Buy coins with a Bonus | [Help](https://help.tango.me/en/articles/3872011-how-to-buy-coins-with-a-bonus) |
| Egypt / MENA | **Fawry Pay** | Help — Bonus | [Help](https://help.tango.me/en/articles/3872011-how-to-buy-coins-with-a-bonus) |
| India | **UPI + NetBanking** | Help — Bonus | [Help](https://help.tango.me/en/articles/3872011-how-to-buy-coins-with-a-bonus) |
| Global | **Crypto stablecoins** (ETH/USDT/USDC ERC-20, >$15) | Help — Buy coins with Crypto | [Help](https://help.tango.me/en/articles/8885625-buy-coins-with-crypto) |
| Regional (generic) | "Your Regional Payment Method" (unspecified local APMs) | Help — missing coins | [Help](https://help.tango.me/en/articles/2985298-i-bought-coins-but-didn-t-receive-them-on-my-tango-balance-what-should-i-do) |
| iOS / Android | Apple App Store / Google Play billing | Help — missing coins | [Help](https://help.tango.me/en/articles/2985298-i-bought-coins-but-didn-t-receive-them-on-my-tango-balance-what-should-i-do) |

**Confirmed payout rails:** Payoneer, PayPal/Tipalti, Mastercard Virtual Card, VISA-to-card, Crypto, Paxum, WebMoney, GCash (PH), STCPay (ME), Wallet Egypt, PIX (BR), SBP + bank transfer (RU), Airwallex, carrier billing (NG), country bank transfers (Nigeria, Egypt, Colombia, Bangladesh, Indonesia, Pakistan, Morocco); **all settle in USD** ([Help — Payout platforms](https://help.tango.me/en/articles/2985211-tango-introduces-new-payout-platforms)).

**4B. Not verified (do NOT claim as gaps):**

| Item | Status |
|------|--------|
| Apple Pay / Google Pay as named web methods | NOT VERIFIED (official pages reference App Store / Google Play billing, not the wallets by name) |
| PayPal for BUYING coins | NOT VERIFIED (PayPal appears on payout side only) |
| Full per-market pay-in APM matrix | NOT VERIFIED (no consolidated methods page; distributed across help articles) |

> "Not verified" ≠ "not available." Tango accepts a broad method set. The angle is never "you lack X", it is that acceptance is fragmented across markets with no routing/recovery layer.

---

## SECTION 5 — Payment Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|-----------|----------|-----------|------------|------------|
| Paid but coins never delivered (payment captured, no credit) | Tango Help + Sikayetvar | Recurring (dedicated help article) | Current | [Help](https://help.tango.me/en/articles/2985298-i-bought-coins-but-didn-t-receive-them-on-my-tango-balance-what-should-i-do), [Sikayetvar](https://www.sikayetvar.com/en/tango-us/tango-live-payment-was-processed-but-tokens-were-not-received-how-can-i-resolve-this-issue-q-10868) |
| Card declined at checkout (Visa repeatedly rejected) | Sikayetvar | Multiple | Current | [Sikayetvar](https://www.sikayetvar.com/en/tango-us/tango-keeps-rejecting-my-visa-card-withdrawal-how-can-i-easily-fix-it-q-10871) |
| "Can't buy coins" / checkout won't process (money lost) | PissedConsumer | Multiple | Current | [PissedConsumer](https://tangome.pissedconsumer.com/review.html) |
| Unauthorized / accidental / double charges | Sikayetvar | Multiple | Current | [Sikayetvar](https://www.sikayetvar.com/en/tango-us/tango-live-charged-my-credit-card-for-a-subscription-i-didnt-authorize-how-can-i-easily-cancel-it-q-10874) |
| Refund friction (won't refund unless technical error) | Trustpilot / Help | Recurring | Current | [Trustpilot CA](https://ca.trustpilot.com/review/www.tango.me?page=2) |
| **Creator payout: approved but not settled** ($171/$136 via Airwallex never arrived) | Sikayetvar | Multiple, concrete | Current | [Sikayetvar](https://www.sikayetvar.com/en/tango-us/tango-diamonds-withdrawal-approved-but-money-not-deposited) |
| Payout "problem with your provider" errors; withdrawals rejected | Sikayetvar / PissedConsumer | Multiple | Current | [Sikayetvar](https://www.sikayetvar.com/en/tango-us/) |

Overall consumer sentiment PissedConsumer 2.1/5 ([PissedConsumer](https://tangome.pissedconsumer.com/review.html)).

**Analysis → Yuno:** Two clean pain surfaces. (1) **Pay-in capture reliability** (paid-but-no-coins, declines, checkout failures) maps to smart routing (+7% approval), retries, and decline recovery (50%). (2) **Payout settlement reliability** (approved-but-not-settled, provider errors) maps to multi-rail payout redundancy and reconciliation with a single transaction view. Both are orchestration outcomes.

---

## SECTION 6 — Expansion & Corporate Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | 2014 | Series D $280M (Alibaba $215M); peak valuation $2.3B | Funding | [TechCrunch](https://techcrunch.com/2016/01/06/faltering-messaging-app-unicorn-tango-gets-a-new-ceo-to-turn-things-around/) |
| 2 | 2022 | HQ relocation to Limassol, Cyprus (TangoMe Technologies Ltd.) | Corporate | [Financial Mirror](https://www.financialmirror.com/2022/07/21/another-tech-firm-relocates/) |
| 3 | Ongoing | Web coin store with up to 40% bonus (app-store fee bypass) | Payments | [Help — Bonus](https://help.tango.me/en/articles/3872011-how-to-buy-coins-with-a-bonus) |
| 4 | Ongoing | Crypto stablecoin coin purchases (USDC/USDT/ETH) | Payments | [Help — Crypto](https://help.tango.me/en/articles/8885625-buy-coins-with-crypto) |
| 5 | Dec 2024 | Temporarily removed from Google Play globally (with Bigo, LiveMe) over content moderation; reinstated ~May 2025 | Platform risk | [DeepClick](https://deepclick.com/resources/blog/tango-app-banned-advertiser-guide-2026/) |
| 6 | 2025 | Reported ~30% YoY increase in creator payouts | Growth/Payouts | [BMC Template](https://businessmodelcanvastemplate.com/blogs/brief-history/tangome-brief-history) |
| 7 | Ongoing | Expanded payout platform list (Airwallex, PIX, GCash, STCPay, SBP, carrier billing, etc.) | Payouts | [Help — Payout platforms](https://help.tango.me/en/articles/2985211-tango-introduces-new-payout-platforms) |

---

## SECTION 7 — Payment News

| # | Date | Headline | Relevance | Source URL |
|---|------|----------|-----------|------------|
| 1 | Ongoing | Web coin store bypasses Apple/Google fees, up to 40% bonus 🟢 | Owning web acquiring across markets | [Help — Bonus](https://help.tango.me/en/articles/3872011-how-to-buy-coins-with-a-bonus) |
| 2 | Ongoing | Crypto coin purchases live 🟢 | Method breadth, stablecoin appetite | [Help — Crypto](https://help.tango.me/en/articles/8885625-buy-coins-with-crypto) |
| 3 | Dec 2024 | Google Play delisting (reinstated May 2025) 🔴 | App-store risk → strategic value of off-store web rail | [DeepClick](https://deepclick.com/resources/blog/tango-app-banned-advertiser-guide-2026/) |
| 4 | Category | Bigo (bigo.tv) and TikTok (tiktok.com/coin) also run web top-up to escape IAP | Category-wide shift to web acquiring | [TechCrunch](https://techcrunch.com/2024/04/30/screenshots-suggest-tiktok-is-circumventing-apple-app-store-commissions/amp) |

---

## SECTION 8 — Checkout Audit

| Dimension | Finding | Quality | Notes |
|-----------|---------|---------|-------|
| Checkout type | Web store behind login (Coin Balance page) + in-app IAP | Functional | [Help](https://help.tango.me/en/articles/3872011-how-to-buy-coins-with-a-bonus) |
| Guest checkout | No, login required on web | ⚠️ | Account-tied; [BitTopup](https://news.bittopup.com/news/tango-coins-top-up-web-vs-in-app-value-2026) |
| Steps to purchase | Log in → Coin Balance → pick package → pay | OK | — |
| 3DS | Not documented publicly | Unknown | Verify in DevTools |
| Mobile experience | Mobile-first app; web store also mobile | Good | — |
| APM display logic | Regional methods surface by geo (Fawry EG, UPI/NetBanking IN); logic/coverage per market not transparent, no cross-provider routing | ⚠️ Gap | The orchestration white space |

> ⚠️ MANUAL: walk the web checkout via VPN in Egypt, India, and Turkey to see method display and decline behavior first-hand.

---

## SECTION 9 — PCI DSS

| PCI DSS Level | Card data handling | Recommended Yuno integration | Source |
|---------------|--------------------|------------------------------|--------|
| **No public Tango PCI / trust-center / security page found** (PCI badges online belong to reseller sites, not Tango) | Not disclosed; web card flow acquirer undisclosed | Yuno as a tokenized orchestration layer over the web checkout keeps card data out of scope while adding routing/recovery/local APMs; reduces the need to certify each new acquirer integration | [Buffget review](https://buffget.com/news/is-tango-live-safe-2026-security-review-and-breach-history) |

Historical (not payments): 2013 Syrian Electronic Army breach of a backup DB. No recent breach reported.

---

## SECTION 10 — Strategic Insights

**Insight #1: Off-store web acquiring is already live and incentivized, but fragmented and un-orchestrated.**
Evidence: web coin store with up to 40% bonus, accepting cards + Fawry + UPI/NetBanking + crypto + "regional methods", acquirer undisclosed, no orchestrator (S3/S4). Pain Point: managing local acceptance across MENA/India/Turkey/CIS with a single or few processors and no routing means lower auth rates and slow market-by-market expansion. Yuno Value Prop: one API for local acquiring + smart routing across all these markets, new markets live in weeks, +7% approval. Best Case: **inDrive** (10 emerging markets in <8 months at ~90% approval). Outreach Angle: "You already moved coin top-ups to the web to escape the 30% store fee. The next lever is routing that web volume across local acquirers per market for the auth-rate lift."

**Insight #2: Capture-reliability complaints are a direct decline-recovery story.**
Evidence: "paid but coins never delivered", repeated Visa declines, "can't buy coins" (S5). Pain Point: every failed top-up is lost gifting revenue and a churned viewer, at scale across 170+ countries. Yuno Value Prop: retries, failover, and decline recovery (50% of would-be-lost transactions). Best Case: **Livelo** (+5% approval, 50% recovery). Outreach Angle: "Your own help center has an article for 'I paid but got no coins.' That is exactly the decline/retry gap orchestration closes."

**Insight #3: Payout fragmentation and 'approved-but-not-settled' need multi-rail redundancy + reconciliation.**
Evidence: 20+ payout rails (Airwallex, Tipalti, Payoneer, PIX, GCash, STCPay, SBP, carrier billing) all settling in USD, with concrete "approved but not deposited" complaints (S4/S5). Pain Point: managing that many payout providers manually creates settlement failures, reconciliation overhead, and creator churn. Yuno Value Prop: orchestration + reconciliation across payout rails with a single transaction view and redundancy when a rail fails. Best Case: **Rappi** (zero implementation time for new providers, 80% less analyst resolution). Outreach Angle: "You run 20+ payout rails by hand and creators report approved-but-unpaid withdrawals. One orchestration layer gives you redundancy and one reconciliation view."

**Insight #4: App-store dependency risk makes the web rail strategic, not optional.**
Evidence: Dec 2024 Google Play global delisting, reinstated May 2025 (S6/S7). Pain Point: any store action cuts off IAP; the web channel is the hedge, and it needs to be robust and high-converting. Yuno Value Prop: a resilient, orchestrated web payment layer that is not hostage to a single store or acquirer. Best Case: fee-bypass web-checkout orchestration (same pattern Bigo/TikTok are racing on). Outreach Angle: "The Play delisting showed why the web rail matters. Orchestration is what makes it convert like the app without the 30% tax or the platform risk."

---

## SECTION 11 — Pipeline

**11A. Direct Competitors** (live-streaming / virtual-gifting apps)
| Company | Website | HQ / Owner | Est. Size | Overlap Markets | Source |
|---------|---------|-----------|-----------|-----------------|--------|
| Bigo Live | bigo.tv | Singapore (JOYY/YY) | Category leader by spend | MENA/SEA/global | [BitTopup](https://news.bittopup.com/news/bigo-live-web-top-up-vs-app-save-60-on-diamonds) |
| Likee | likee.video | JOYY/BIGO | Large | Global | [Apurple](https://www.apurple.co/insights/top-live-video-streaming-apps/) |
| MICO | micoworld.com | Newborn Town (CN) | Large | MENA/SEA | [LootBar](https://www.lootbar.com/blog/en/mico-vs-poppo-live-vs-chamet-which-is-the-best-host-platform.html) |
| Chamet | chamet.com | China | Large | South Asia/ME | [LootBar](https://www.lootbar.com/blog/en/chamet-vs-poppo-live-key-differences.html) |
| Poppo Live | (app) | China | Mid | Global gifting | [DXBApps](https://dxbapps.com/blog/poppo-live-app) |
| LiveMe | liveme.com | Cheetah Mobile (CN) | Mid | Global | [Marlvel](https://marlvel.ai/apps/com-cmcm-live) |
| StreamKar | streamkar.com | India | Mid | India | search-only |

**11B. Industry Peers** (broader live/creator monetization)
| Company | Website | Vertical | Key Markets | Why Similar | Source |
|---------|---------|----------|-------------|-------------|--------|
| TikTok Live | tiktok.com/coin | Live + gifting | Global | Official web recharge to bypass IAP | [TechCrunch](https://techcrunch.com/2024/04/30/screenshots-suggest-tiktok-is-circumventing-apple-app-store-commissions/amp) |
| Twitch | twitch.tv | Live streaming | West | Bits/subs monetization | — |
| Kick | kick.com | Live streaming | West | Creator payouts | — |
| YouTube Live | youtube.com | Live + Super Chat | Global | Gifting/superchat | — |

**11C. Adopting Orchestration / web top-up:** Bigo (bigo.tv web recharge), TikTok (tiktok.com/coin) have both launched official web top-up to escape 15–30% app-store fees. No named third-party orchestrator confirmed for any of them, an open field across the whole category.

**11D. Scoring (verified signals)**
| Signal | Pts | Verified? |
|--------|-----|-----------|
| Operates in 3+ countries | +3 | Yes (170+) |
| Multiple PSPs | +3 | Yes (multi web pay-in rails + 20+ payout providers) |
| Recent expansion (24 mo) | +2 | Yes (crypto coins, payout expansion, +30% payouts 2025) |
| Public payment issues | +2 | Yes (pay-in capture + payout settlement) |
| Funding >$10M | +2 | Yes (~$373M raised) |
| LATAM/APAC/MENA traffic | +2 | Yes (Egypt, Turkey, India + PIX/GCash/STCPay) |
| No orchestrator | +2 | Yes (none found) |
| Payment job postings | 0 | Not verified (Tel Aviv payments-ops team exists, no posting confirmed) |
| Public RFP | 0 | None found |
| **TOTAL** | **16** | **🔴 High** |

**Top Pipeline (this brief + adjacent targets):**
| Rank | Company | Type | Key Markets | Score | Priority | Top Signal |
|------|---------|------|-------------|-------|----------|------------|
| 1 | Tango (Tango Live) | Live-streaming / gifting | US, India, Egypt, Turkey, CIS | 16 | 🔴 High | Web top-up live, no orchestrator, dual-sided pain |
| 2 | Bigo Live | Live-streaming / gifting | MENA/SEA | TBD | 🔴 | Official web recharge, no orchestrator [verify] |
| 3 | MICO / Chamet | Live-streaming / gifting | MENA/South Asia | TBD | 🟡 | Same web-topup fee-bypass pattern [verify] |

Pipeline Summary: Tango scores 🔴 High (16). Strongest adjacent vertical to prospect next: **live-streaming / virtual-gifting apps moving coin top-ups to the web (Bigo, MICO, Chamet, LiveMe, StreamKar)** across MENA, South Asia, and SEA, every one with the same off-store acquiring + local-APM + no-orchestrator profile.

---

## SECTION 12 — Business Case

| Annual Revenue | Avg Transaction Value | Est. Annual Transactions | Primary Currency | Top 3 Markets |
|----------------|-----------------------|--------------------------|------------------|---------------|
| India alone ~$12M/month (~$144M/yr, Dec-2024 investor deck); global figures conflict, treat as unverified | Coin packs $0.99 to $199.99 | Not disclosed | USD (payouts settle in USD) | US, India, Egypt (traffic); India largest by revenue |

Anchors: **~$12M/month from India** (best-sourced, [The CapTable](https://the-captable.com/2025/04/tango-live-streaming-microtransactions/)), described as India's #1 social-grossing app; 450M+ registered users, 170+ countries; ~$373M raised, peak valuation $2.3B (2014), current est. ~$1.1B ([Tracxn](https://tracxn.com/d/companies/tango/__lgjNa-YBvFCHdgg0hSxaaW-OsvD75IOtzCB92Ul0bU0)). App-store revenue trackers (Sensor Tower) materially understate true spend because web-store top-ups are not counted.

---

## SECTION 13 — Outreach (verified findings only)

```
--- LINKEDIN MESSAGE ---
Hi [name], I lead payments partnerships at Yuno and spend most of my time with
high-volume consumer apps, so Tango's model caught my eye.

You have already made the smart move of pushing coin top-ups to the web to escape
the 30% app-store tax, with cards, Fawry, UPI, and crypto on one checkout across
a very MENA and India heavy base. The next lever is what sits behind that: routing
each top-up across local acquirers per market, retrying declines, and giving your
creators one reconciled view across the 20+ payout rails you run today.

That is exactly what Yuno is: a single API that orchestrates acquirers, local methods,
and recovery across 200+ countries, plus reconciliation across pay-in and payout. It
is what runs payments for inDrive (live in 10 markets in under 8 months at ~90%
approval), Rappi, and Kraken.

Worth 20 minutes this week to compare notes on the web rail? Open Wednesday or Thursday.

--- COLD EMAIL ---
Subject: Your web coin store, minus the declines

Hi [name],

Tango already did the hard part: you moved coin top-ups to tango.me to escape the
30% store fee and put cards, Fawry, UPI, NetBanking, and crypto on one checkout for a
MENA and India heavy audience. That is exactly the kind of web acquiring we help
consumer apps get more out of.

Two things stood out. First, your own help center has an article for "I paid but did
not receive my coins," and reviews show repeated card declines, every failed top-up is
lost gifting revenue. Second, creators report withdrawals that are approved but never
settle across the 20+ payout rails you manage by hand.

Yuno is a single API that orchestrates acquirers and local methods across 200+ countries
with smart routing (~+7% approval), decline recovery (about 50% of otherwise-lost
transactions), and one reconciliation view across pay-in and payout. inDrive used it to
go live across 10 markets in under 8 months at ~90% approval; Rappi added new providers
with zero implementation time.

Worth 20 minutes this week to walk your web rail together? I can do Wednesday or Thursday.

German
```

> Persona note: target **Head of Payments / Payments Operations (Tel Aviv team)**, **CTO**, or **VP Finance (US/Cyprus)**. Founders Eric Setton / Uri Raz for the strategic frame. Lead with the web-acquiring + decline-recovery angle; never claim they "lack" a method.

---

## APPENDIX — Source URLs
```
[S1] https://www.similarweb.com/website/tango.me/
[S2] https://www.semrush.com/website/tango.me/overview/
[S3] https://www.tango.me/terms-of-use
[S4] https://cyprusregistry.com/companies/%CE%97%CE%95/408288
[S5] https://www.financialmirror.com/2022/07/21/another-tech-firm-relocates/
[S6] https://www.investcyprus.org.cy/invest-cyprus-welcomes-tangome-inc-decision-to-relocate-offices-to-cyprus/
[S7] https://help.tango.me/en/articles/2985298-i-bought-coins-but-didn-t-receive-them-on-my-tango-balance-what-should-i-do
[S8] https://help.tango.me/en/articles/3872011-how-to-buy-coins-with-a-bonus
[S9] https://help.tango.me/en/articles/8885625-buy-coins-with-crypto
[S10] https://help.tango.me/en/articles/2985211-tango-introduces-new-payout-platforms
[S11] https://the-captable.com/2025/04/tango-live-streaming-microtransactions/
[S12] https://tangome.pissedconsumer.com/review.html
[S13] https://www.sikayetvar.com/en/tango-us/tango-diamonds-withdrawal-approved-but-money-not-deposited
[S14] https://deepclick.com/resources/blog/tango-app-banned-advertiser-guide-2026/
[S15] https://news.bittopup.com/news/buy-tango-coins-2026-get-40-more-with-web-recharge
[S16] https://techcrunch.com/2016/01/06/faltering-messaging-app-unicorn-tango-gets-a-new-ceo-to-turn-things-around/
[S17] https://www.crunchbase.com/organization/tango-me
[S18] https://tracxn.com/d/companies/tango/__lgjNa-YBvFCHdgg0hSxaaW-OsvD75IOtzCB92Ul0bU0
[S19] https://techcrunch.com/2024/04/30/screenshots-suggest-tiktok-is-circumventing-apple-app-store-commissions/amp
[S20] https://news.bittopup.com/news/bigo-live-web-top-up-vs-app-save-60-on-diamonds
```
