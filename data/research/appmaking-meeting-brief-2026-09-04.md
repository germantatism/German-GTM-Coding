# Meeting Brief: Yuno <> Appmaking (Sep 4, 2026)

**Meeting:** App Making x Yuno Dashboard Overview
**When:** Friday, Sep 4, 2026, 09:00 to 10:00 (GMT-5, Bogota). For the prospect this is 17:00 in Cyprus and Minsk, Friday evening: keep it tight and useful.
**Where:** Google Meet: https://meet.google.com/nnv-dymm-hbq
**Organizer:** Susana Awad (SDR, Yuno)
**Objective (what winning looks like):** leave with a scheduled technical deep dive (their engineer + Jarrett), an agreement to share 2 to 3 months of approval/decline data by geo under NDA, and clarity on which group entity would contract.

Evidence labels: ✅ verified · ⚠️ inference or unconfirmed (never state in the call) · 🔍 ask in discovery.

## ⚠️ PRE-MEETING ACTIONS

1. **Sync with Susana Awad before the call.** This meeting was booked by Susana on Sep 3 and there is zero history in German's mailbox, calendar, Gong, or Slack. German cannot see her outreach thread. Ask: how was it sourced, who replied (likely the Payment Manager), what was said or promised, what does "Dashboard Overview" mean to them.
2. **Attendance risk:** 2 of 3 prospect attendees have not accepted (t.gubarevich, d.katsiushchyk; only k.butrym accepted). Have Susana confirm attendance.
3. **With Jarrett (Senior Sales Engineer): verify the Yuno connector catalog for Solidgate, Truegate, and Maverick Bankcard before the call.** They will ask. Do not claim a connector exists without checking. Prep the dashboard storyline: routing rules, real-time monitors, subscriptions/retries, vault, reconciliation, in that order.
4. **Open the attendee people searches manually** (automated LinkedIn was blocked; identities below are from registry + RocketReach):
   - linkedin.com/search/results/people/?keywords=Tatsiana%20Hubarevich%20Wowmaking
   - linkedin.com/search/results/people/?keywords=Katerina%20Butrym%20Wowmaking
   - linkedin.com/search/results/people/?keywords=Katiushchik%20Wowmaking%20product
5. **Have the MSA, DPA and security pack ready to send same day.** The statutory director/legal counsel of the Cyprus entity is in the room on call one; that is unusual and it means contract terms are already on their mind.
6. Optional if the deal advances: paid Cyprus registry report (EUR 49 to 65) for shareholders/UBO of HE 437099.

---

# STUDY ZONE

## 1. TL;DR BATTLE CARD

### Five facts to know cold

1. ✅ **Appmaking LTD (Limassol, HE 437099) is one arm of a four-entity Cyprus group**: Appmaking (AstroSoul, Atrix), Gototop (Habio and habit apps), Applabel (Eliten, web billing for Habio), Appsella (Astroline, and merchant of record for the Atrix web funnel). Hard links: shared director (Katsiaryna Butrym), shared nominee officers, shared support domain (support-team.app), byte-identical support portals, shared CDN and funnel platform (mutator.magnus.ms). ⚠️ The group's internal brand appears to be **Wowmaking** (Minsk origin, founded ~2017, ~77 staff, ~$18.1M revenue per Tracxn estimate, bootstrapped, founder-owned per GLEIF): all three attendees appear in public records under Wowmaking titles. Do not assert the group map or the Wowmaking name in the call; let them describe it.
2. ✅ **They already run live web subscription billing outside the app stores.** The Atrix quiz funnel (quiz.atrix.guide) takes card, PayPal, Apple Pay and Google Pay, merchant of record Appsella LTD. Sibling brand Astroline runs the same platform with 77 geo rules, BRL and INR pricing, and four MoR entities (Cyprus, Hong Kong, Colorado, Dubai). Group legal docs name Solidgate, Stripe, Checkout.com, Maverick Bankcard as processors, plus PayPal (wallet).
3. ✅ **THE fact: they are mid-bake-off between two orchestration vendors right now.** Every Atrix plan is mapped to two gateways in parallel, **Solidgate** and **Truegate** (a Larnaca, Cyprus orchestration+gateway platform), with hand-written A/B rules splitting traffic by country and OS (JP 31%, DE/ES 25%, FR 12%, Nordics 100% to Truegate; PayPal on for 75% of US). Yuno arrives as vendor three, and as the only neutral one: both incumbents are gateways routing traffic to themselves.
4. ✅ **The room:** Tatsiana Hubarevich (Payment Manager, a role the group created only in 2025: the champion and likely meeting source), Dmitrii Katiushchik (Product Manager, former CEO of a prior company, owns monetization: the economic sponsor), Katsiaryna Butrym (Lead Legal Counsel and statutory director of the Cyprus entity: the signature and the gate). No engineer attending: they want the commercial and operational case first.
5. ✅ **Portfolio reality:** flagship AstroSoul has 6.5M installs but is 100% app-store IAP and has had no update in 20 months (harvest mode). Atrix is the web-monetized bet: tiny installs (17.5K Android), 2.1 stars on Android driven by web-billing complaints vs 4.0 on iOS. Category context: astrology/esoteric merchants average 65 to 80% approval rates (high-risk MCC 8999).

### Three hooks, in priority order

1. **Per-transaction smart routing vs hand-tuned geo splits.** Today someone maintains routing percentages by hand ("Truegate JP 31%"). Yuno's engine decides per transaction (BIN, issuer, method, geo, past outcomes) across Solidgate, Truegate, Stripe, Checkout.com and 1,000+ others, with automatic failover and retries: +7% approval uplift, up to 50% recovery of failed transactions, all visible in the dashboard they asked to see.
2. **The local-currency and local-method gap.** Atrix charges USD only across 52 countries; their own sibling brand already prices in BRL and INR. In a vertical running 65 to 80% approval, cross-border USD pricing leaves measurable money on the table. One Yuno integration adds local currencies, local acquiring options and APMs market by market, no new PSP projects.
3. **Multi-entity, multi-processor operations for a tiny team.** Four+ MoR entities, five+ processors, and a two-person finance function. Unified reconciliation, real-time monitors (Rappi: detection in milliseconds vs 5 to 10 minutes manually, 80% less analyst time), dispute workflows, and a PCI vault ABOVE the gateways so the subscriber card base is portable across entities and providers instead of locked to whichever gateway wins the current test.

### THE objection they will raise, and the answer

**"We already run Solidgate and Truegate, and both call themselves orchestrators. Why add a third layer?"**
Answer: both are gateways first; routing traffic to themselves is their business model, so their "orchestration" has a structural conflict of interest. Yuno does not process and does not compete with them: it is the neutral layer that makes them compete per transaction, adds the 1,000+ methods and processors they do not offer (local acquiring, APMs, local currency rails), and keeps the vault, and therefore the recurring-billing card base, in their hands rather than the gateway's. Commercially there is no rip-out: keep every existing contract, first $50K processed free, then $0.05 per transaction.

### The ask (next step to land)

Technical deep dive + sandbox next week with their engineer and Jarrett; 2 to 3 months of approval/decline data by geo and rail shared under NDA to quantify the uplift; confirmation of which entity would contract.

### Rapport opener

"You're one of the few app groups anywhere that has actually cracked web billing; most of the big US astrology apps are still 100% Apple and Google." True, public, flattering, and it invites them to talk about the funnel. (It is 5pm Friday for them: thank them for the slot, keep pace brisk.)

## 2. WHO IS IN THE ROOM

| Name | Role | Side | Status |
|---|---|---|---|
| Tatsiana Hubarevich ⚠️ | Payment Manager (group) | Prospect | Invited, not yet accepted |
| Katsiaryna Butrym ✅ | Lead Legal Counsel (group); statutory Director, Appmaking LTD | Prospect | Accepted |
| Dmitrii Katiushchik ⚠️ | Product Manager (group), owns monetization | Prospect | Invited, not yet accepted |
| German Tatis | Account Executive | Yuno | Accepted |
| Susana Awad | SDR (sourced the meeting) | Yuno | Organizer |
| Jarrett Falasco | Senior Sales Engineer | Yuno | Accepted |

### Tatsiana Hubarevich (t.gubarevich@appmaking.app) ⚠️ identity via transliteration match

- Payment Manager since 2025 (~1 year in seat). Prior: Specialist of Foreign Economic Activity at App Fork (2021 to 2024). Belarusian State University, International Law (2017 to 2021). Based in Minsk. Sits in a two-person finance function. Source: RocketReach.
- **How to read them:** the operator, not the buyer, and not an engineer; background is law and cross-border compliance, new to payments as a named function. Talk workload: PSP onboarding time, reconciliation, refund/chargeback handling, declines by market. Almost certainly sourced this meeting: treat as the champion and arm them internally.

### Katsiaryna Butrym (k.butrym@appmaking.app) ✅ highest confidence (Cyprus registry)

- Lead Legal Counsel since 2023; in-house counsel at the group since 2020; before that UIC BelVEB Insurance (2017 to 2020). Belarusian State University, Law. Based in Paphos, Cyprus. **Registered Director of Appmaking LTD and of Gototop LTD** (the other two Appmaking officers are nominees: Savvas Teklos, director of ~45 companies, and LSTS Services Limited, secretary to ~293). Sources: Cyprus registry HE 437099, RocketReach.
- **How to read them:** the contractual and compliance gate, and the person who legally signs for the Cyprus entity. Will care about DPA/GDPR, PCI scope, entity of contract, liability. Cannot approve the purchase; can stall it. Legal joining a first call is a buying-process signal: name the contracting-entity question openly and offer paper early.

### Dmitrii Katiushchik (d.katsiushchyk@appmaking.app) ⚠️ identity via transliteration match

- Product Manager at the group since 2021. Prior: CEO of Webmart Group LLC (2019 to 2021), sales lead before that, marketing degree (Belarusian State Economic University). Based in Belarus. Source: RocketReach.
- **How to read them:** the most senior commercial mind in the room; thinks in P&L, not architecture. Owns paywall, subscription conversion, renewals. Lead with recovered revenue and auth-rate uplift in dollars. The likeliest economic sponsor.

### Sponsor path and relationship timeline

- ✅ **This is a first meeting.** Definitive: no prior calendar event with any attendee, no email history (the only thread is the invite itself, sent Sep 3), no Gong account, no Slack mentions, no deck ever built for this account. Everything they know about Yuno came from Susana's outreach, which German has not seen (action #1).
- **Decision dynamics:** no CEO/CFO/CTO on the call, so this is evaluation, not decision. The trio (payments operator + monetization owner + legal director) is what a bootstrapped publisher assembles when it intends to change its payment stack rather than window-shop. The Payment Manager role being created only in 2025 says payments recently became painful enough to staff.
- **Other known group names** (⚠️ RocketReach/TheOrg/Tracxn, unconfirmed): Timur Latfulin (founder), Ivan Tsikota (CEO), Nikolay Zhdan (CTO), Maria Rabchun (CFO, Gdansk), Olga Vergey (CMO, Warsaw). None attending.

## 3. THE COMPANY

**What they do:** consumer subscription apps in spiritual wellness (astrology, palmistry, tarot), AI styling and habit tracking, monetized by weekly/monthly subscriptions through app-store IAP and, increasingly, web quiz funnels with card billing. Growth is paid UA (Meta, TikTok, Snap, Google, Unity, ironSource et al., Adjust as MMP), so payment acceptance rate directly moves blended CAC efficiency.

| Key metric | Value | Source |
|---|---|---|
| Group claim | 30+ products, 12M+ users, 180+ countries | appmaking.app ✅ (group-level claim) |
| AstroSoul installs | 6,513,372 (Google Play lifetime counter, Sep 3, 2026) | Play payload ✅ |
| AstroSoul rating | 4.4 stars, 54.3K reviews | Play ✅ |
| Atrix Android | 17,544 installs, 2.1 stars | Play ✅ |
| Atrix iOS | 4.0 stars, 216 ratings | App Store ✅ |
| AstroSoul pricing (listed) | $7.99/week (3-day trial), $24.99/month, $29.99/3 months; reviews cite $14.99/week and £27/week (per-market price testing ⚠️) | Play description ✅ |
| Appmaking LTD headcount | 2 to 10 (LinkedIn), 62 followers | LinkedIn ✅ |
| Group headcount | ~77 (Wowmaking, Tracxn estimate) ⚠️ | Tracxn |

### Corporate structure and billing entities

| Entity | Reg. | Incorporated | Role | Products |
|---|---|---|---|---|
| Appmaking LTD | HE 437099 | Aug 3, 2022 | Store publisher | AstroSoul, Atrix |
| Gototop LTD | HE 420118 | Apr 3, 2021 | Store publisher; web MoR for Astroline; former name link to "Wowmaking Apps Ltd" ⚠️ | Habio, BrainaryAI, CleverMe |
| Applabel LTD | HE 420746 | Apr 20, 2021 | **Web billing MoR for Habio** | Eliten |
| Appsella LTD | HE 427133 | Oct 26, 2021 | Store publisher of Astroline; **MoR of the Atrix web funnel** | Astroline, lifestyle apps |

- ✅ **Store publisher and web merchant of record are deliberately different entities** (Habio: published by Gototop, billed by Applabel; Atrix: published by Appmaking, web-billed by Appsella). The contracting-entity question is live, and the person who signs for two of these entities is on the call.
- ✅ GLEIF records Appmaking's parent exceptions as NATURAL_PERSONS: owned directly by individuals, no holding company, no PE. Bootstrapped; no funding found anywhere.
- ✅ Both Appmaking and Gototop are registered "High-Tech Company in the Cyprus Register of Companies with Foreign Interests." ⚠️ The four-entity split is consistent with IP Box optimization and store-account risk isolation.
- Astroline (sibling benchmark) swaps MoR by geo across four entities: Gototop (Cyprus), SGR Hong Kong Limited, Digital Solutions LLC (Colorado), an IFZA Dubai entity, and its policies name Stripe, Checkout.com, Maverick Bankcard and Paddle as MoR options.

## 4. FINANCIALS

**Growth trajectory (verifiable milestones only; no revenue is public at any point):**

| Date | Milestone | Source |
|---|---|---|
| Nov 12, 2019 | appmaking.app domain registered | whois ✅ |
| Jan 22, 2020 | AstroSoul released on Google Play | FoxData ✅ |
| Apr to Oct 2021 | Gototop, Applabel, Appsella incorporated in Limassol | Cyprus registry ✅ |
| Aug 3, 2022 | Appmaking LTD incorporated | Cyprus registry ✅ |
| Jun 6, 2024 | LEI issued (254900VKS5KAOPDYKB05) | GLEIF ✅ |
| Nov to Dec 2024 | Atrix launched (Android + iOS) | Store listings ✅ |
| Dec 26, 2024 | Last AstroSoul update (none since: 20 months stale) | Play ✅ |
| Jun 17, 2026 | Atrix updated to v2.17.0 (actively maintained) | Play ✅ |
| Sep 3, 2026 | AstroSoul 6.51M installs (~96/day new); Atrix 17.5K | Play payload, AppBrain ✅ |

**Recent trend read:** the flagship is in harvest mode (no updates, ~35K new installs/year on a 6.5M base) while investment moved to Atrix and the web funnel. This is a deliberate rail shift, not decline of the business per se; the web rail is where their money and their pain now live.

**Last full year:** no public financial statements exist (private Cyprus companies; accounts filed but not freely searchable). The only group-level revenue figure anywhere is Tracxn's ~$18.1M estimate for Wowmaking ⚠️ (estimate, basis undisclosed). Do not use any revenue number in the call.

**Benchmarks for internal sizing only (never quote to them):**
- Nebula/OBRIO, the category's scale player: $50M ARR, 30M users (company-stated, Dec 2023, tech.eu). Roughly 10x this group.
- Derived range for a 5M-install Android astrology app (Adapty and RevenueCat 2026 benchmarks, three methods): roughly $0.8M to $2.1M cumulative gross before store fees, or $130K to $340K/year steady-state; 95% of subscription revenue accrues to the top 10% of apps, so the true number could sit far from any midpoint. The group's real engine is the web funnels plus 30+ apps, not AstroSoul alone.
- RevenueCat 2026: Google Play billing-failure churn 31% vs App Store 14%; Lifestyle weekly plans first-renew at only 35%. Involuntary churn is structurally enormous in exactly their category and price model.

**Other material items:** Cyprus corporate tax rose 12.5% to 15% on Jan 1, 2026 (IP Box can bring effective rate near 2.5%): margin discipline context. Store fees of 15 to 30% apply to all IAP revenue (AstroSoul entirely). No debt, funding, or M&A found.

**So what for the call:** a bootstrapped, founder-owned, margin-conscious group running paid UA; every point of approval rate and every recovered renewal is direct profit, and the fee delta between IAP and their own web rail is the strategic play they are already executing. Size the deal on group web volume (🔍 get the number), not on install counts.

## 5. COMPETITIVE LANDSCAPE

No research house publishes company-level share in this category (IBISWorld: US psychic services "highly fragmented, no company above 5%"). Only one measured share figure exists (Sensor Tower FY2019). Every basis is labeled; install/tech-detection sources measure website installs, not revenue.

| Competitor | Segment | Est. market share (source + basis) | Scale proxy (dated) | Differentiator | Payments posture |
|---|---|---|---|---|---|
| Hint / Astrology & Palmistry Coach (Ruby Labs, UK) | Web-funnel palmistry (closest analog) | 35.3% of US top-10 astrology IAP revenue, FY2019 (Sensor Tower; basis: measured revenue share, dated) | 25M+ users claimed 2026; US App Store listing now 404s ✅ | Palm-scan + astrologer chat, web-first | Web card funnel ($1 trial then $30 to 40/mo); unnamed PCI processors, plural; was hiring to build an in-house "Payment Orchestration System MVP" ✅ |
| Nebula (OBRIO/Genesis, UA) | Chat marketplace + astrology, scale leader | ~1.5% derived ($50M ARR ÷ ~$3.3B category, 2023) ⚠️ derived; download-rank leader 2020-21 (Sensor Tower) | $50M ARR, 30M users (2023, company-stated); 70M+ claimed 2026 | Only true scale player; 900+ psychics; credits + subs | IAP + web card checkout (Visa/MC/Amex/Discover/Maestro/JCB/Verve) + PayPal; PSP undisclosed; ⚠️ multi-acquirer inferred |
| Astroline (Appsella/Gototop, CY) | **Their own sibling brand** | No estimate available | 10M+ Play installs, 87.8K reviews (Sep 2026) ✅ | Same funnel platform, more evolved | Solidgate + Truegate parallel IDs, PayPal, Apple/Google Pay; USD+BRL+INR; 77 geo rules; 4 MoR entities (CY, HK, US, Dubai); policies name Stripe, Checkout.com, Maverick Bankcard, Paddle ✅ |
| Astrotalk (India) | India marketplace, revenue leader | ~2 to 3% derived (₹1,176 cr ops revenue ÷ category estimates) ⚠️ derived | ₹1,214 cr total income FY25, +85% YoY ✅ | Astrologer marketplace + commerce, ~$1B valuation | Single PSP: Razorpay (domestic + international, 160+ currencies); no orchestrator ✅ |
| AstroSage (India) | India, Vedic tools | No estimate available | 79.4M Android installs (Sep 2026) ✅; revenue undisclosed | Oldest (2011), AI astrologer, bootstrapped | Web + Play IAP; Razorpay + Paytm logos; Shopify shop ✅ |
| Astroyogi (India) | India | No estimate available | ₹85 cr FY25 (YourStory); 20.3M installs | 25 years old, 11 languages | **The one orchestrator user in the field: Juspay** (live prod config) + Razorpay + PayPal ✅ |
| InstaAstro (India) | India challenger | No estimate available | ₹111 cr FY26, +113%; $12M Series A Aug 2026 ✅ | AI sentiment + spiritual commerce | PSP genuinely undisclosed; no Play IAP; (caught false positive: their "stripe" hits are a CSS class) ✅ |
| Anytime Astro (Innovana, India) | India/diaspora | No estimate available | 8.75M installs, 4.6 stars | US-diaspora web funnel | Policy names four PSPs: Stripe, CCAvenue, Razorpay, Paytm, plus Dodo Payments MoR; no orchestrator ✅ |
| Co-Star (US) | Western subscription app | No estimate available; #2 US grossing Q1 2026 (Statista/AppMagic; basis: IAP revenue rank) | 205K iOS ratings; $20.9M raised (Spark Capital) | Brand + friend-graph astrology | Subscriptions 100% IAP; web shop on Shopify Payments only ✅ |
| CHANI (US) | Western subscription app | No estimate available; #1 US grossing Q1 2026 (Statista/AppMagic; basis: IAP revenue rank) | ~$14M revenue (secondhand, unaudited); tiny Android base | Human-written, no-AI, highest ARPU | Pure IAP; Shopify merch only; greenfield web billing ✅ |
| The Pattern (US) | Western subscription app | No estimate available | 15K iOS ratings; 1M+ Play | Psychological readings | 100% IAP; no web checkout at all ✅ |
| Sanctuary (US) | Advisor marketplace + app | No estimate available (#28 US by revenue, 2019, Sensor Tower) | ~$6.5M raised; 44K iOS ratings | Gen-Z live readings, pay-per-minute | Three fragmented rails: IAP + WordPress/Stripe web checkout + Shopify; passes ~5% "fees" line to consumers ✅ |
| Ingenio: Keen + Kasamba + Purple Garden (Alpine Investors, US) | Advisor marketplaces (one owner, three storefronts) | No estimate available (IBISWorld <5% ceiling) | Kasamba $37.1M FY2022 (LivePerson 10-K, SEC ✅); Ingenio CV $462M | Consolidator of pay-per-minute brands | No PSP JS on any frontend; Sift fraud detected (webtechsurvey; basis: tech-install detection); ⚠️ direct high-risk merchant accounts inferred; payouts ACH/PayPal/Payoneer |
| California Psychics (US) | Advisor marketplace | No estimate available | $26.4M (Owler; basis: data-broker estimate, low confidence) | Est. 1995, screening-led brand | Cards + PayPal + Apple/Google Pay; billing descriptor "TELCASH" (discretion play) ⚠️ direct acquirer inferred |
| Life Palmistry (Bluewolf, HK) | AI palmistry, direct AstroSoul substitute | No estimate available | 21M lifetime downloads (AppBrain) | Pure palm scan | ⚠️ IAP-led inferred; no web checkout found |

**Where Appmaking sits:** mid-tier by scale (an order of magnitude below Nebula, Astrotalk, Hint; half its own sibling Astroline), but top-tier by playbook: it already runs the full web-funnel card stack that the entire US cohort lacks. Within its own group it lags Astroline on currencies (USD-only vs BRL/INR), geo rules (52 vs 77) and MoR coverage (2 entities vs 4). Category norm is DIY routing; the only third-party orchestrator user among 16 competitors is Astroyogi (Juspay).

**For the call:** the market leader in their exact playbook (Nebula) and their own sibling both out-execute Atrix on payment localization. Position Yuno as how Atrix catches up to Astroline (and both catch up to Nebula) without more hand-built routing: one integration, per-transaction routing, local currencies and methods, and vault portability across their entities.

## 6. PAYMENTS MONEY MAP

**Orchestrator status:** ✅ two gateway-owned "orchestrators" in a live A/B (Solidgate vs Truegate) on the Atrix web funnel, hand-tuned by geo/OS. No neutral third-party orchestrator anywhere in the group. 🔍 Ask who owns the routing table and how often it is re-tuned.

| Rail | Products | Providers and evidence | Entity |
|---|---|---|---|
| Google Play IAP | AstroSoul (all revenue), Atrix Android (partial) | Google Play billing ✅ (listings, T&Cs §8) | Appmaking LTD |
| Apple IAP | Atrix iOS | Apple billing ✅ (T&Cs §8) | Appmaking LTD |
| **Web funnel (LIVE)** | Atrix: quiz.atrix.guide | **Solidgate + Truegate in parallel** (54 and 68 plan IDs in live config ✅), PayPal (19 plans), Apple Pay, Google Pay; USD only, $4.99 to $53.99, 52 geo rules, 18 languages | **Appsella LTD** (MoR), with a geo-conditional Fort Lauderdale, FL variant |
| Web funnel (sibling benchmark) | Astroline: sub.astroline.today | Solidgate + Truegate + PayPal + Apple/Google Pay; USD + BRL + INR; 77 geo rules; policies name Stripe, Checkout.com, Maverick Bankcard, Paddle (MoR) ✅ | Gototop (CY), SGR (HK), Digital Solutions (US), IFZA (Dubai) |
| Web subscriptions (sibling) | Habio | PayPal, Solidgate, Checkout.com, Maverick Bankcard, Stripe named in policy ✅ | Applabel LTD |
| Fraud / 3DS | All | No public evidence found | 🔍 |
| PCI | All | No certification published; today card capture sits with gateways/stores ("we don't collect or store payment data") ✅ | 🔍 |
| Hiring signals | Group | Payment Manager role created 2025 ✅; junior IT/AdOps role open (Meta ad accounts, API integrations) ✅ | |

**Framing rules for this account:**
- The conversation is performance, cost, reliability and speed-to-market. Never tell them they lack anything.
- Solidgate and Truegate are incumbents to orchestrate, not rip out. "Keep both, make them compete per transaction."
- PayPal is a wallet/APM in our framing, never a PSP.
- The privacy-policy draft placeholder ("[confirm and list: e.g., Solidgate, Stripe, PayPal]") means their legal templates lag the live stack; do NOT conclude or say the web rail is new or undecided. It is live.
- Do not recite the funnel A/B percentages unprompted; demonstrating that depth uninvited can read as surveillance. Lead with "we can see you run a serious web funnel and test gateways side by side" and deploy the detail only if credibility is challenged.

*(A dedicated Top Markets demographics module is omitted: no verified per-country revenue or traffic data exists for this group. Verified market signals: funnel geo rules concentrate on US, DE, ES, FR, JP, Nordics, AU, CA, IT; USD-only pricing; 18 languages.)*

## 7. NEWS & SIGNALS (newest first)

| Date | Item | Relevance |
|---|---|---|
| Aug 6, 2026 | Astroline (sibling brand) announces mobile + web platform expansion (GlobeNewswire) | Group doubling down on web rail ⚠️ sibling link, do not assert |
| ~Aug 2026 | Appmaking LinkedIn job post: Junior IT Support/AdOps ("Russian-speaking team, remote/Limassol") | Ops scaling signal ✅ |
| Jun 17 to 18, 2026 | Atrix updated on both stores (v2.17.0) | Active product ✅ |
| Jun 16, 2026 | Fresh 1-star refund complaint on AstroSoul Play listing, developer replied | Billing friction ongoing ✅ |
| Jun 2, 2026 | FTC sues Genesis Tech (15 entities, ROSCA, ~$250M; names Nebula among brands) | **Internal only, never mention**: regulatory overhang on the whole quiz-funnel category; descriptor clarity, cancellation UX and chargeback ratios are existential in this MCC; multi-acquirer redundancy is the insurance story ✅ |
| Jan 1, 2026 | Cyprus corporate tax 12.5% → 15% | Margin-pressure context ✅ |
| Feb 2025 | Group privacy/billing policies updated naming processors (Solidgate, Stripe, Checkout.com, Maverick Bankcard, PayPal) | Stack evidence ✅ |
| Dec 26, 2024 | Last AstroSoul update | Flagship in harvest mode ✅ |
| Nov to Dec 2024 | Atrix launched (Android + iOS) | The web-rail bet ✅ |

No news in the last 7 days on the account itself; use the category rapport opener instead.

## 8. SELLING YUNO HERE

**Core frame:** you have already made the hard strategic move (web billing outside the stores) and you are already testing orchestration. Yuno is the neutral layer that makes that stack perform: per-transaction routing instead of hand-tuned geo splits, local currencies and methods your sibling brands already prove out, recovery of failed renewals, and one dashboard over every gateway, entity and rail. Yuno positioning: the unified operating system for global payments, orchestrating payment methods, processors, antifraud, KYC/KYB and reconciliation through one API.

**Hooks with proof points (real Yuno cases only):**
- Smart routing + failover: +7% approval uplift; InDrive: 10 LATAM markets live in under 8 months, 90% approval, 4.5% recovery.
- Failed-payment recovery: up to 50% of declined transactions recovered (Livelo: +5% approval, 50% recovery). For a weekly-subscription business where Google-rail billing-failure churn benchmarks at 31%, this is the single biggest revenue lever.
- Real-time monitors: Rappi detects payment incidents in milliseconds vs 5 to 10 minutes manually, 80% less analyst resolution time. Directly relevant to a 2-person finance team running 5 processors.
- Speed: new PSP or market enabled no-code, live in weeks; pricing $50K processed free, then $0.05 per transaction.

**Landmines (what NOT to say):**
- Never "you don't have an orchestrator" (they are testing two) or "your PSP shortlist is open" (dead thesis from their stale legal template).
- Never quote their Play reviews, the 2.1-star rating, or refund complaints back at them; translate to "renewal declines and billing UX cost retention; monitors and retry logic reduce refunds and disputes."
- Never mention the FTC/Genesis case, sanctions, or geopolitics. Contracting entities are Cypriot; any compliance/KYB questions route internally, not to the call.
- Never assert the Wowmaking name, the four-entity map, or the sibling brands (Astroline/Habio) as established fact; ask instead ("how is payments organized across the group's brands?"). If THEY name it, everything above is usable.
- Do not walk in with any revenue figure for them.
- Do not name-drop merchant logos beyond established Yuno cases; GoFundMe references require permission before details.

## 9. BE READY FOR (what THEY may ask)

| Likely question | Ready answer |
|---|---|
| Do you integrate with Solidgate? Truegate? Maverick Bankcard? | 🔍 VERIFY WITH JARRETT BEFORE THE CALL. If yes: instant. If no: Yuno builds connectors rapidly and they keep those contracts meanwhile; do not bluff this one. Stripe, Checkout.com and PayPal (wallet) are standard. |
| Pricing? | First $50K processed free, then $0.05 per transaction. No rip-out of existing contracts. |
| Integration effort? We have no engineer here today. | One API + web SDK; the funnel checkout embeds Yuno once and every PSP after that is no-code configuration. Weeks, not months. Offer the deep dive with Jarrett as the immediate next step. |
| PCI and data (from Butrym)? | Yuno vaults cards (PCI DSS Level 1); their scope stays minimal; GDPR DPA ready; flexible on which group entity contracts. Offer MSA + DPA + security pack same day. |
| We already route by geo ourselves. What does routing add? | Hand-tuned geo splits are static and per-segment; Yuno routes per transaction (BIN, issuer, method, outcome history), fails over automatically mid-transaction, and retries intelligently. The dashboard shows the uplift per route, which is exactly what a bake-off needs: measurement. |
| Subscriptions: can you handle recurring? | Yes: subscription billing with smart retry logic and network tokens sits natively on the orchestration layer, so renewals retry across processors rather than dying on one. (Same story that resonated with Hostinger.) |
| References? | InDrive, Rappi, Livelo, Reserva with the numbers above. Offer a reference call at deep-dive stage. |
| Why not just finish our Solidgate vs Truegate test and pick one? | Picking one gateway ends the competition that is currently earning you better pricing and approval. Yuno keeps both permanently competitive, adds local rails neither offers, and keeps your card vault independent so the next test costs nothing. |

---

# LIVE ZONE (German: take notes from here down)

## 10. AGENDA (60 min)

| Time | Block | Goal | Notes |
|---|---|---|---|
| 0:00 to 0:05 | Intros + agenda check | Confirm roles; confirm what they hoped to see today | ____ |
| 0:05 to 0:20 | Discovery: their stack story | Get them to describe the web funnel, entities, gateways, routing ownership, volumes | ____ |
| 0:20 to 0:40 | Dashboard walkthrough (Jarrett), tailored | Routing rules → real-time monitors → subscriptions/retries → vault → reconciliation | ____ |
| 0:40 to 0:48 | Commercial: pricing + how an engagement starts | $50K free, $0.05/txn; keep existing contracts; pilot on one funnel | ____ |
| 0:48 to 0:55 | Legal/entity lane (Butrym) | Contracting entity, DPA, PCI posture; offer paper same day | ____ |
| 0:55 to 1:00 | Next steps | Deep dive + sandbox next week; NDA + data share; owner and date | ____ |

## 11. DISCOVERY QUESTIONS

1. What made a payments conversation timely for you right now? (Let them state the pain before pitching.)
   Notes: ____
2. Which products run web checkout today, and roughly what share of revenue is web vs app store? Where do you want that split in 12 months?
   Notes: ____
3. Who decides how traffic is routed between your payment providers today, and how often does that get re-tuned?
   Notes: ____
4. What approval rates are you seeing by market and rail, and where are declines worst?
   Notes: ____
5. How do failed renewals get retried today, and who owns dunning/recovery?
   Notes: ____
6. How is payments organized across the group's brands and entities? Who would a payments platform actually contract with? (For Butrym.)
   Notes: ____
7. Where do subscriber cards live today, and does provider lock-in of the card base concern you?
   Notes: ____
8. What does reconciliation across entities and processors look like month-end, and who does it?
   Notes: ____
9. Which markets are next, and are local currencies or local payment methods on the roadmap? (USD-only today on web 🔍 confirm they say it.)
   Notes: ____
10. How do you handle chargebacks and disputes today, and is descriptor/refund workload growing?
    Notes: ____
11. What would the current gateway test have to show for you to call it a success?
    Notes: ____
12. If the deep dive goes well, what does your evaluation and sign-off process look like from here?
    Notes: ____

## 12. POST-MEETING CHECKLIST

- [ ] Recap email same day (thank you, what we heard, agreed next step, calendar invite for deep dive) with MSA/DPA/security pack if legal engaged
- [ ] Log outcome + new facts (entities confirmed?, volumes, routing owner, gateways confirmed) and update memory
- [ ] Schedule the technical deep dive with Jarrett + their engineer; send NDA for the data share
- [ ] Verify Solidgate/Truegate/Maverick connector status internally (if not done pre-call)
- [ ] Update Susana on outcome; agree who owns follow-up threads

## APPENDIX: KEY SOURCES

- Meeting + attendees: Google Calendar event (Sep 4, 2026); Cyprus registry HE 437099 (cyprusregistry.com/companies/ΗΕ/437099); RocketReach profiles (Hubarevich, Butrym, Katiushchik, Rabchun); TheOrg/Tracxn (Wowmaking)
- Company: appmaking.app; appmaking.app/terms-of-use; appmakingpub.b-cdn.net (privacy policy, general terms); LinkedIn company page; GLEIF LEI 254900VKS5KAOPDYKB05; i-cyprus.com/company/609040
- Group entities: cyprusregistry.com HE 420118 / 420746 / 427133; gototop.app; applabel.tech; habio.app; terms.habio.app/applabel/billing-terms; NorthData (Gototop former name)
- Live funnel evidence: quiz.atrix.guide/quiz-pp (Solidgate/Truegate/PayPal plan IDs, geo rules); quiz.atrix.guide/appsella/terms-of-use and /billing-terms; sub.astroline.today; truegate.tech; solidgate.com
- Stores: play.google.com (com.astrosouls, com.atrixapp, dev 8888427613446085618); apps.apple.com id6737768525
- Competitors: sensortower.com/blog/astrology-apps-2019-revenue-downloads; tech.eu/2023/12/05/obrio; SEC LivePerson 10-K (Kasamba); Outlook Business (Astrotalk FY25); razorpay.com/case-studies/astrotalk; Entrepreneur India (InstaAstro); Statista 1451664 (US grossing ranks); IBISWorld psychic services; hint.app/eula; nebulahoroscope.com FAQ; astroyogi.com (Juspay in prod config); GlobeNewswire Astroline Aug 6, 2026
- Category: thebusinessresearchcompany.com astrology app report; marknteladvisors.com (global + India); adapty.io State of In-App Subscriptions 2026; revenuecat.com State of Subscription Apps 2026; payatlas.com/industry/esoteric-4888; FTC press release Jun 2, 2026 (Genesis Tech)
- Internal: Gmail (invite only, Sep 3), Calendar (no prior meetings), Gong (no account), Slack (no mentions), repo (no prior deck); companion research brief: data/research/appmaking-ltd-2026-09-03.md
