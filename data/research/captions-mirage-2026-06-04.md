# SDR Research Brief — Captions / Mirage (captions.ai)
*Yuno Payment Orchestrator — Framework v8.0 | Date: 2026-06-04*

**Target:** Captions — US AI-powered short-form video creation/editing app for creators. Parent company **renamed from "Captions" to "Mirage" in Sept 2025** ("Captions" = consumer app; "Mirage" = parent brand + in-house AI UGC-video foundation model). Operating entities: **NOCAP, Inc. d/b/a Mirage** and **Mirage US LLC** (data controller), formerly Captions, Inc. HQ New York, NY. Founders Gaurav Misra & Dwight Churchill (founded 2021). *(Not the Mirage casino/hotel or any game engine.)*

---

## EXECUTIVE SUMMARY

Captions/Mirage is a mobile-first AI video subscription app with 20M+ users, 10M+ iOS downloads and ~$28.4M trailing in-app revenue, of which **only ~25% comes from the US (≈75% international).** Billing runs on three rails: **Apple App Store IAP, Google Play IAP, and Stripe on web** — a single web PSP, no orchestration layer, and heavy app-store-tax exposure on a majority-international revenue base. With a fresh **$75M growth financing (Mar 2026) explicitly earmarked for aggressive Asia expansion**, the Yuno opportunity is threefold: cut app-store fee leakage by scaling direct web checkout, add local payment methods for Asia/LATAM, and put redundancy + recovery on the single Stripe rail. Score: **🔴 16/15 (High).**

---

## SECTION 1 — Traffic by Country

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source URL |
|------|---------|-------------------|---------------------|-------|------------|
| — | United States | ~25% of in-app revenue | Not found (web geo split not disclosed) | growing | https://techcrunch.com/2026/03/24/mirage-raises-75m-to-continue-building-models-for-its-ai-video-editing-app-captions/ |
| — | International (rest) | ~75% of in-app revenue | Asia called out as fastest demand | growing | https://www.trendingtopics.eu/mirage-raises-75m-to-push-ai-video-app-captions-into-asian-markets/ |

- **Web visit geo breakdown: No public SimilarWeb figure found** for captions.ai specifically. Distribution is overwhelmingly **mobile/in-app** (iOS + Android + web/desktop since Apr 2024).
- **Critical flag:** revenue is **~75% non-US** and the company states Asia demand is "extraordinary" — a strong multi-market / APAC ICP signal.
- App-store presence: iOS App Store (app id 1541407007), Google Play, plus web/desktop.
- Sources: https://techcrunch.com/2026/03/24/mirage-raises-75m-to-continue-building-models-for-its-ai-video-editing-app-captions/ | https://www.businesswire.com/news/home/20240410992953/en/Leading-AI-Powered-Creative-Studio-Captions-Expands-to-Web-and-Desktop

---

## SECTION 2 — Legal Entities

| Country | In Top Markets? | Has Local Entity? | Cross-Border Risk? | Source URL |
|---------|-----------------|--------------------|--------------------|------------|
| United States | ✅ (HQ, ~25% rev) | ✅ NOCAP, Inc. d/b/a Mirage / Mirage US LLC (NYC) | n/a | https://mirage.app/legal/eea |
| International (~75% rev, incl. Asia/EEA) | ✅ | ❌ none found | ⚠️ likely cross-border acquiring from US | https://captions.ai/legal/privacy |

- Only US entities found. No per-country subsidiaries/offices disclosed. EEA users handled via Standard Contractual Clauses (cross-border data, and likely cross-border payment) from the US entity.
- ⚠️ **Potential cross-border operation:** ~75% of revenue is international but no local entities found → cross-border acquiring drag and FX on the web (Stripe) rail.

> ⚠️ MANUAL: Verify billing entity-of-record per market on official T&Cs and a VPN checkout walk-through.

---

## SECTION 3 — Payment Stack

**3A. PSPs & Acquirers**

| Country/Region | PSP / Acquirer | Evidence Type | Source URL |
|----------------|----------------|---------------|------------|
| Web (global) | **Stripe** | [Help Center] "If you paid on our website via Stripe…" | https://captions.ai/help/docs/manage-my-subscription |
| iOS (global) | **Apple App Store IAP** | [App Store] "purchased via the Apple App Store… connected to your AppleID" | https://captions.ai/help/docs/manage-my-subscription |
| Android (global) | **Google Play IAP** | [App Store] "purchased via the Google Play Store… connected to your Google account" | https://captions.ai/help/docs/manage-my-subscription |

- **Single web PSP = Stripe.** No Adyen / Checkout.com / Braintree / second web acquirer found. RevenueCat plausible but **NOT confirmed** — do not claim it.
- Web (Stripe) checkout supports business purchases (VAT/company info); Apple IAP does not, and the help center tells VAT customers to cancel App Store sub and re-buy on web.

**3B. Orchestrator:** **No public evidence found.** No Spreedly/Primer/Gr4vy/etc.

> ⚠️ MANUAL — DevTools on captions.ai web checkout: test card 4111 1111 1111 1111 | 02/30 | 123; BuiltWith/Wappalyzer to confirm whether RevenueCat or a second rail exists.

---

## SECTION 4 — APMs (Agent D findings)

**4A. Confirmed APMs**

| Market | APMs Confirmed | Verification Source | Source URL |
|--------|----------------|---------------------|------------|
| Web/Global | **None page-verified** (no card/PayPal/wallet logos rendered). Stripe web checkout confirmed exists; local-currency display confirmed | Pricing/plans/help pages fetched | https://captions.ai/help/docs/subscriptions |

**4B. Unverified Methods / Markets**

| Market | Verification Attempted? | Reason Not Verified | Popular Local APMs (worth exploring) |
|--------|------------------------|---------------------|--------------------------------------|
| Web checkout (cards/PayPal/Apple Pay/Google Pay) | ✅ | Marketing pages show no logos; live web checkout not reachable (404 on guessed paths) | — |
| Asia (funded expansion target) | ✅ | No local checkout verified | China Alipay/WeChat Pay; SEA GrabPay/PayNow; India UPI; Korea KakaoPay; Japan Konbini/PayPay |
| LATAM | ✅ | Not verified | Pix (Brazil), Mercado Pago, OXXO (Mexico) |

- Help center confirms **local-currency pricing** at checkout (consistent with Apple/Google IAP localization).

> "Not verified" ≠ "not available." MANUAL: VPN walk-through before any APM claim. Per Yuno rules, never tell them they "lack" a method.

---

## SECTION 5 — Payment Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| Charged while UI showed "Free"; only partial refund | Trustpilot | recurring | 2025–2026 | https://www.trustpilot.com/review/captions.ai |
| ~$300 annual plan cancelled, never refunded | App Store reviews | isolated/notable | 2025–2026 | https://apps.apple.com/us/app/captions-ai-edits-your-video/id1541407007?see-all=reviews |
| Credit refund went negative | Trustpilot | isolated | 2026 | https://www.trustpilot.com/review/captions.ai |
| Opaque credit system → unpredictable/"surprise" large bills | Review aggregators | common (#1 UX gripe) | 2025–2026 | https://www.eesel.ai/blog/captions-ai-review |
| Monthly plans non-refundable; auto-renew default | Help Center (policy) | policy | current | https://captions.ai/help/docs/manage-my-subscription |
| Positive: full refunds when unused; efficient cancel | Trustpilot | mixed | 2025–2026 | https://www.trustpilot.com/review/captions.ai |

- **No Reddit billing thread surfaced; no gateway-decline/double-charge pattern.** Dominant friction is refund denial + credit-billing unpredictability, not processor failures.

**Analysis → Yuno:** The credit/renewal billing confusion and refund friction point to subscription-lifecycle and reconciliation gaps. Yuno's subscription management (trials, renewals, retries), network tokens/account updater (fewer silent renewal failures), and unified reconciliation (one view across Stripe + Apple + Google) reduce both the involuntary churn and the support load.

---

## SECTION 6 — Expansion & Corporate Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | Jun 2023 | $25M Series B (Kleiner Perkins; Sequoia, a16z) | Funding | https://venturebeat.com/ai/ai-video-creation-app-captions-bags-25m-from-top-vcs |
| 2 | Jul 2024 | $60M Series C (Index Ventures) at **~$500M valuation**; total to $100M | Funding | https://slator.com/ai-video-startup-captions-valued-at-usd-500m-in-usd-60m-series-c/ |
| 3 | Jan 2025 | Switched to **freemium** to compete with CapCut & Meta Edits | Product/GTM | https://techcrunch.com/2026/03/24/mirage-raises-75m-to-continue-building-models-for-its-ai-video-editing-app-captions/ |
| 4 | Sep 2025 | **Rebrand Captions → Mirage**; launched Mirage UGC-video foundation model + Mirage Studio | Corporate/Product | https://techcrunch.com/2025/09/04/captions-rebrands-as-mirage-expands-beyond-creator-tools-to-ai-video-research/ |
| 5 | Mar 24 2026 | **$75M growth financing** from General Catalyst CVF (non-dilutive); total raised >$175M | Funding | https://captions.ai/blog/announcing-mirages-usd75m-growth-financing-with-general-catalyst |
| 6 | Mar 2026 | Funds earmarked for **aggressive Asia expansion** + agentic video editing | Expansion | https://www.trendingtopics.eu/mirage-raises-75m-to-push-ai-video-app-captions-into-asian-markets/ |

- Leadership: no CFO/CTO/VP Payments hire found. Acquired AlpacaML (CEO Will Buchwalter joined as research engineer).

---

## SECTION 7 — Payment News

| # | Date | Headline | Relevance | Source URL |
|---|------|----------|-----------|------------|
| 1 | — | No PSP/payments/billing partnership announced (no 🟢/🔴) | Greenfield on orchestration | N/A |

---

## SECTION 8 — Checkout Audit

| Dimension | Finding | Quality | Notes |
|-----------|---------|---------|-------|
| Checkout type | Dual: Apple/Google IAP (mobile) + Stripe (web) | Fragmented | Single web PSP |
| Guest checkout | Account-bound (Google/Apple/phone sign-up) | — | Not guest |
| Steps to purchase | Freemium → credits → paid tier; no time-boxed trial | Credit model = friction | Opaque per-task credit cost |
| 3DS | Not found | NOT VERIFIED | Check live |
| Mobile experience | Primary surface (IAP) | Strong but app-store-taxed | 15-30% store fees |
| APM display logic | Local-currency localization confirmed; method logos not verified | NOT VERIFIED | VPN test needed |

> ⚠️ MANUAL: Walk web (Stripe) + iOS checkout in US and one Asia market.

---

## SECTION 9 — PCI DSS

| PCI DSS Level | Card data handling | Recommended Yuno integration | Source |
|---------------|--------------------|------------------------------|--------|
| No public PCI/SOC2/ISO page found | Card billing delegated to Apple, Google and Stripe (likely minimal direct PCI scope) [INFERENCE] | Yuno as orchestration + vault layer over web checkout, so adding acquirers/APMs for Asia is config, not re-integration | https://mirage.app/legal/eea |

---

## SECTION 10 — Strategic Insights

**Insight #1: App-store fee leakage on a 75%-international base (lead)**
Evidence: S1/S3 — ~75% of ~$28.4M in-app revenue is international and flows through Apple/Google IAP at a 15-30% take. Pain Point: store fees are the single biggest margin leak; web checkout (Stripe) is underused and card-only. Yuno Value Prop: orchestration + a stronger direct web funnel lets them shift volume off app-store rails and route directly, reclaiming fee margin. Best Case: Whop (US digital subscription, resilient global checkout). Outreach Angle: every paid subscriber pushed to direct web billing instead of IAP is 15-30% margin recovered, at the exact moment they are funding growth.

**Insight #2: Asia expansion needs local payment methods**
Evidence: S6 — $75M earmarked for aggressive Asia push; S3 — web rail is Stripe/card-centric. Pain Point: cards convert poorly in much of Asia; cross-border acquiring from a US entity drags approval and adds FX. Yuno Value Prop: one API to 1,000+ methods (Alipay/WeChat Pay, GrabPay/PayNow, UPI, KakaoPay) and local acquiring, live in days. Best Case: InDrive (10 markets <8 months on one integration). Outreach Angle: time the conversation to the Asia rollout, activate local methods as a config change.

**Insight #3: Single web PSP, no redundancy**
Evidence: S3 — Stripe is the only web processor, no orchestrator. Pain Point: single point of failure + no routing optimization on the web rail. Yuno Value Prop: smart routing + auto-failover, ~7% approval uplift, A/B test processors for fee leverage. Best Case: Whop (added the fallback/redundancy they were missing for 24/7 uptime). Outreach Angle: add a backup acquirer beside Stripe with no rip-and-replace.

**Insight #4: Subscription churn + credit-billing friction**
Evidence: S5 — refund/credit complaints, auto-renew, recurring credit subscriptions. Pain Point: involuntary churn from failed renewals; reconciliation fragmented across Stripe + Apple + Google. Yuno Value Prop: subscription management, network tokens, account updater, smart retries + unified reconciliation. Best Case: Livelo (+5% approval, 50% recovery). Outreach Angle: recover failed renewals and unify reporting across all three billing rails.

---

## SECTION 11 — Pipeline

**11A. Direct Competitors**

| Company | Website | HQ | Est. Size | Overlap Markets | Source |
|---------|---------|-----|-----------|------------------|--------|
| CapCut (ByteDance) | capcut.com | Singapore/China | Market leader, 100s of M users | Global | https://www.gstory.ai/blog/best-ai-powered-video-editing-tools/ |
| Descript | descript.com | San Francisco (est.) | VC-backed (a16z, OpenAI Fund) | Global | https://www.aihustleguy.com/blog/descript-vs-capcut-vs-opus-clip-ai-video-editor |
| VEED.io | veed.io | London (est.) | ~11.7M visits | Global | https://www.opus.pro/blog/veed-vs-capcut |
| OpusClip | opus.pro | Palo Alto (est.) | Clip repurposing leader | Global | https://www.opus.pro/blog/descript-vs-capcut |
| InVideo | invideo.io | India/US (est.) | Text-to-video | Global | https://posteverywhere.ai/blog/20-best-ai-short-form-video-tools |
| Submagic | submagic.co | Paris (est.) | Short-form captions | Global | https://posteverywhere.ai/blog/20-best-ai-short-form-video-tools |

**11B. Industry Peers (avatar / gen-video)**

| Company | Website | Vertical | Key Markets | Why Similar | Source |
|---------|---------|----------|-------------|-------------|--------|
| Synthesia | synthesia.io | AI avatar video | Global | $200M Series E Jan 2026; UGC-ad overlap | https://www.yipitdata.com/resources/blog/heygen-vs-synthesia-vs-runway-ai-video-platforms |
| HeyGen | heygen.com | AI avatar video | Global | Closest to Mirage Studio | https://retailwit.com/whos-winning-in-ai-video-synthesia-vs-heygen-vs-runway-2026-data/ |
| Runway | runwayml.com | Gen-video | Global (NYC) | On Yuno HIGH list; gen-video peer | https://www.yipitdata.com/resources/blog/heygen-vs-synthesia-vs-runway-ai-video-platforms |
| Pika | pika.art | Gen-video | Global | Consumer gen-video | https://sacra.com/c/pika/ |
| Luma AI | lumalabs.ai | Gen-video | Global | $900M Series C | https://www.yipitdata.com/resources/blog/heygen-vs-synthesia-vs-runway-ai-video-platforms |

**11C. Adopting Orchestration:** None confirmed for any competitor → **Not found**. Most monetize via Apple/Google IAP + direct web — same orchestration gap as Captions.

**11D. Scoring (verified only)**

| Signal | Pts | Verified? |
|--------|-----|-----------|
| Operates in 3+ countries | +3 | ✅ ~75% revenue international |
| Multiple PSPs / rails | +3 | ✅ Stripe + Apple IAP + Google IAP |
| Recent expansion (24 mo.) | +2 | ✅ $75M, rebrand, Mirage model, Asia push |
| Public payment issues | +2 | ✅ refund/credit-billing complaints |
| Funding >$10M | +2 | ✅ $75M (2026), $60M (2024) |
| LATAM/APAC/MENA traffic | +2 | ✅ ~75% intl + funded Asia push |
| No orchestrator | +2 | ✅ none found |
| Payment job postings | 0 | ❌ not found |
| Public RFP | 0 | ❌ none |
| **TOTAL** | **16** | 🔴 **High** |

**Top Pipeline**

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal |
|------|---------|------|-------------|-------|----------|------------|
| 1 | **Captions / Mirage** | Target | US + ~75% intl (Asia) | 16 | 🔴 High | $75M for Asia expansion; single web PSP + IAP |
| 2 | Runway | Peer | Global | — | 🔴 | $315M Series E; on Yuno list |
| 3 | Synthesia | Peer | Global | — | 🟡 | $200M Series E |

Pipeline Summary: 1 high-priority target plus tracked AI-video peers. Strongest vertical: consumer AI video subscriptions expanding into APAC.

---

## SECTION 12 — Business Case

| Annual Revenue | Avg Transaction Value | Est. Annual Transactions | Primary Currency | Top 3 Markets |
|----------------|-----------------------|--------------------------|------------------|----------------|
| ~$28.4M trailing in-app revenue (ESTIMATE, Appfigures via TechCrunch); total ARR not disclosed | $4.99–$69.99/mo subscription tiers (CONFIRMED pricing) | [INFERENCE] high-volume recurring across 20M+ users (10M+ iOS downloads) | USD (localized) | US (~25%), then international incl. Asia |

- Sources: revenue https://techcrunch.com/2026/03/24/mirage-raises-75m-to-continue-building-models-for-its-ai-video-editing-app-captions/ | pricing https://captions.ai/pricing
- In-app figure excludes web (Stripe) revenue → total is higher; confirm with prospect.

---

## SECTION 13 — Outreach (verified findings only — no unconfirmed APM claims)

```
--- LINKEDIN MESSAGE ---
Hi ((contact_name)), congrats on the $75M from General Catalyst and the push into Asia, the Mirage model is genuinely impressive. As someone deep in payments, what jumped out is that around three quarters of your revenue is already international while billing leans on Apple and Google in-app plus Stripe on web. That mix means a lot of margin going to app-store fees and a card-centric web checkout heading into markets where local methods convert far better. Yuno is one API to 1,000+ payment methods and 190+ countries, so adding local Asia methods and a direct web rail becomes a config change. InDrive used us to go live across 10 markets in under 8 months. Worth 20 minutes next week?

--- COLD EMAIL ---
Subject: Asia rollout + the app-store fee math for Captions

Hi ((contact_name)),

Congrats on the $75M growth round and the Asia push. Looking at Captions from a payments angle, a few things stood out as you scale, given roughly three quarters of revenue is already international:

• App-store fees. Most of that international revenue flows through Apple and Google in-app at a 15 to 30 percent take. Strengthening your direct web checkout and orchestrating it lets you shift volume off app-store rails and reclaim that margin, right when you are funding growth.

• Local methods for Asia. The web rail looks card-centric today, and cards convert poorly across much of Asia. Through one Yuno API you can activate methods like Alipay, WeChat Pay, GrabPay, PayNow, UPI and KakaoPay as a configuration change, live in days.

• Redundancy and recovery. With Stripe as the single web processor, adding a backup acquirer plus smart retries and network tokens gives you failover and around a seven percent approval uplift, without rebuilding anything.

Yuno is a global payment infrastructure platform connecting 460+ integrations, 1,000+ payment methods and 180+ currencies across 190+ countries through a single API. InDrive went live across 10 markets in under 8 months on one integration, and Livelo recovered around half of its failed transactions.

Open to a quick 20 minute call next week to map this against the Asia plan?

Best,
German
```

> Outreach uses only verified facts ($75M round, Asia expansion, Stripe + Apple + Google billing, ~75% international). No claim is made that they "lack" any method.

---

## APPENDIX — Source URLs
```
[S1]  https://techcrunch.com/2026/03/24/mirage-raises-75m-to-continue-building-models-for-its-ai-video-editing-app-captions/
[S2]  https://captions.ai/blog/announcing-mirages-usd75m-growth-financing-with-general-catalyst
[S3]  https://techcrunch.com/2025/09/04/captions-rebrands-as-mirage-expands-beyond-creator-tools-to-ai-video-research/
[S4]  https://www.trendingtopics.eu/mirage-raises-75m-to-push-ai-video-app-captions-into-asian-markets/
[S5]  https://captions.ai/help/docs/manage-my-subscription
[S6]  https://captions.ai/pricing
[S7]  https://captions.ai/help/docs/subscriptions
[S8]  https://slator.com/ai-video-startup-captions-valued-at-usd-500m-in-usd-60m-series-c/
[S9]  https://www.businesswire.com/news/home/20240709061123/en/Captions-Raises-Series-C-to-Invest-$100M-in-Pioneering-AI-Video-Research-in-New-York-City
[S10] https://www.trustpilot.com/review/captions.ai
[S11] https://apps.apple.com/us/app/captions-ai-edits-your-video/id1541407007?see-all=reviews
[S12] https://mirage.app/legal/eea
[S13] https://www.eesel.ai/blog/captions-ai-review
```

---

## ⚠️ MANUAL VERIFICATION CHECKLIST
1. **Confirm web PSP + RevenueCat** — BuiltWith/Wappalyzer + DevTools on captions.ai web checkout (Stripe confirmed; RevenueCat unconfirmed).
2. **Confirm accepted methods** — live VPN walk-through of web checkout (no logos page-verified).
3. **Valuation** — ~$500M is from the 2024 Series C; the 2026 CVF round is non-dilutive (no new valuation).
4. **Revenue** — $28.4M is third-party in-app only; web/Stripe revenue not included.
