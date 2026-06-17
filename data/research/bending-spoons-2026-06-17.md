# SDR Research Brief — Bending Spoons S.p.A.

**Prepared for:** Yuno GTM | **Date:** 2026-06-17 | **Analyst:** Payments Intelligence

---

## Executive Summary

Bending Spoons is a Milan-based "acquirer-operator" of 50+ consumer software brands (Evernote, WeTransfer, Vimeo, Meetup, Remini, Splice, Brightcove, Komoot, Eventbrite, AOL) that reached ~$1.31B FY2025 revenue (95% YoY growth), 500M+ MAU and ~9M paying subscribers, and filed for a Nasdaq IPO (ticker **BSP**) on 2026-06-08 at a ~$20B target valuation. ([techstartups](https://techstartups.com/2026/06/08/bending-spoons-files-for-u-s-ipo-after-revenue-doubles-to-601m-as-acquisition-strategy-pays-off/), [mostlymetrics](https://www.mostlymetrics.com/p/bending-spoons-ipo-s1-breakdown)) The single most important payments fact, straight from the F-1 analysis: **75% of Q1-2026 revenue flowed through electronic payments, and ~one-third of that ran through Apple App Store / Google Play at 15–30% take rates** — even though "Adyen, PayPal, and Stripe charge 5% or less," a gross-margin drag the company explicitly flags. ([mostlymetrics](https://www.mostlymetrics.com/p/bending-spoons-ipo-s1-breakdown)) Confirmed web-billing stacks are fragmented per brand (WeTransfer = Stripe; Evernote = direct card + PayPal via "Conceptive Apps LLC"; Vimeo = Stripe Connect), with no evidence of a unified cross-brand orchestration layer — a textbook post-acquisition consolidation + IAP-to-web migration thesis for Yuno.

---

## S1 — Traffic by Country (web properties; Similarweb, May 2026 unless noted)

| Property | Monthly Visits | Global Rank | Top 5 Countries (share) |
|---|---|---|---|
| WeTransfer | 67.2M | #6,278 | US 7.64% · India 7.11% · Italy 6.41% · UK 6.11% · Spain 6.02% ([Similarweb](https://www.similarweb.com/website/wetransfer.com/)) |
| Vimeo | 57.1M | #76,455 | US 38.21% · UK 5.88% · Japan 4.81% · Canada 3.76% · Brazil 3.26% ([Similarweb](https://www.similarweb.com/website/vimeo.com/)) |
| Evernote | 10.5M | #4,875 | US 25.79% · Japan 10.09% · Brazil 9.62% · India 6.54% · South Korea 3.97% ([Similarweb](https://www.similarweb.com/website/evernote.com/)) |
| Remini (app.remini.ai) | 1.2M | #40,632 | India 16.23% · Philippines 12.4% · US 9.35% · Russia 5.45% · Turkey 5.04% ([Similarweb](https://www.similarweb.com/website/remini.ai/)) |
| Meetup | ~12M (Oct figure 11.96M) | N/A | US-led, then UK, Germany ([Similarweb](https://www.similarweb.com/website/meetup.com/)) |

**Note:** Remini/Splice are overwhelmingly mobile-app driven; web traffic understates their true subscriber base. Country mix is genuinely global (heavy US + LatAm + India/SEA + Japan/Korea), reinforcing multi-currency / local-APM relevance.

---

## S2 — Legal Entities

| Entity | Role | Source |
|---|---|---|
| Bending Spoons S.p.A. | Parent, Milan, Italy | [Wikipedia](https://en.wikipedia.org/wiki/Bending_Spoons) |
| Evernote Corporation | Subsidiary (acquired Jan 2023) | [TechCrunch](https://techcrunch.com/2024/07/31/bending-spoons-acquires-file-transfer-service-wetransfer/) |
| WeTransfer (Dutch) | Subsidiary (acquired 2024) | [Fortune](https://fortune.com/europe/2024/08/01/wetransfer-acquired-bending-spoons-the-italian-software-powerhouse-behind-evernote-and-meetup-vimeo-remini-evernote/) |
| AI Creativity S.r.l. | Operates Remini (web) & Splice; "subject to management and coordination of Bending Spoons S.p.A." | [app.remini.ai footer](https://app.remini.ai/), [Splice ToS](https://spliceapp.com/app-terms-of-service/) |
| Conceptive Apps LLC | Billing/merchant-of-record entity appearing on **PayPal** charges for web subscriptions | [BS Support](https://bendingspoonssupport.zendesk.com/hc/en-gb/articles/32346488392721-I-received-a-PayPal-charge-from-Conceptive-Apps-LLC) |
| Bending Spoons US (Vimeo acquirer) | Acquired Vimeo $1.38B, Nov 2025 | [Investing.com](https://www.investing.com/news/sec-filings/vimeo-acquired-by-bending-spoons-us-in-138-billion-cash-deal-delisted-from-nasdaq-93CH-4376218) |

Founders: Luca Ferrari (CEO), Francesco Patarnello, Matteo Danieli, Luca Querella, Tomasz Greber. ([Wikipedia](https://en.wikipedia.org/wiki/Bending_Spoons)) Current CFO name: **Not found** (company is actively recruiting CFO/Office-of-the-CFO roles per its careers site). ([BS Jobs](https://jobs.bendingspoons.com/positions/6a22779735de636e51dd3568))

---

## S3 — Payment Stack

### 3A — PSPs / Acquirers / Billing Rails (confirmed per brand)

| Brand | Rail / PSP | Evidence |
|---|---|---|
| WeTransfer (integrated payments) | **Stripe** | "integrated payments on WeTransfer are powered by Stripe… rolling out to all users globally" ([TechCrunch](https://techcrunch.com/2024/04/30/wetransfer-cuts-out-the-middle-man-and-now-lets-users-sell-files-directly-on-the-platform/)) |
| Vimeo (OTT/creator payouts) | **Stripe (Standard Connect)** | Vimeo OTT uses Stripe Standard Connect for select markets ([Vimeo Help](https://help.vimeo.com/hc/en-us/articles/12425768308625-Standard-Connect-for-Select-Markets-on-Vimeo-OTT)) |
| Evernote (web/direct) | Credit card + **PayPal** (third-party PCI-DSS processor, unnamed) | [Evernote FAQ](https://help.evernote.com/hc/en-us/articles/28267325211795-Subscriptions-Payments-FAQ) |
| Web subscriptions (multi-app) | **PayPal** via "Conceptive Apps LLC" MoR | [BS Support](https://bendingspoonssupport.zendesk.com/hc/en-gb/articles/32346488392721-I-received-a-PayPal-charge-from-Conceptive-Apps-LLC) |
| All consumer apps (mobile) | **Apple App Store + Google Play IAP** (15–30% fees) | [mostlymetrics](https://www.mostlymetrics.com/p/bending-spoons-ipo-s1-breakdown) |
| F-1 cited alternative processors | **Adyen, PayPal, Stripe** ("5% or less") | [mostlymetrics](https://www.mostlymetrics.com/p/bending-spoons-ipo-s1-breakdown) |
| Mobile paywall tooling (Splice) | **Adapty** paywall (library reference) [INFERENCE — not confirmed as live production stack] | [Adapty library](https://adapty.io/paywall-library/splice-video-editor-maker/) |

Cloud infra: Google Cloud (named customer). ([Google Cloud](https://cloud.google.com/customers/bending-spoons))

### 3B — Orchestrator: **No dedicated third-party orchestrator confirmed.**
The "Spoon Engine" shared platform lists **"payments"** among 50+ in-house services it provides to acquired apps ([Sacra](https://sacra.com/c/bending-spoons/)) — i.e. an internally-built payments capability, not Primer/Gr4vy/Spreedly/Yuno. Each acquired brand still appears to run its own legacy rail (Stripe at WeTransfer/Vimeo, PayPal/Conceptive at Evernote). No public evidence of a unified multi-PSP routing/orchestration layer across the portfolio. [INFERENCE — not confirmed]

---

## S4 — APMs Confirmed

| APM | Confirmed where | Source |
|---|---|---|
| Credit/debit cards | Evernote web, Remini/Splice (via stores), WeTransfer (Stripe) | [Evernote FAQ](https://help.evernote.com/hc/en-us/articles/28267325211795-Subscriptions-Payments-FAQ) |
| PayPal | Evernote web; web subs via Conceptive Apps LLC | [Evernote FAQ](https://help.evernote.com/hc/en-us/articles/28267325211795-Subscriptions-Payments-FAQ), [BS Support](https://bendingspoonssupport.zendesk.com/hc/en-gb/articles/32346488392721-I-received-a-PayPal-charge-from-Conceptive-Apps-LLC) |
| Apple Pay / Google Pay (IAP) | All mobile apps | [Remini ToS](https://support.bendingspoons.com/tos?app=1470373330) |

**Unverified Markets / APMs:** Despite heavy traffic from Brazil (Pix), India (UPI), Philippines, Turkey, Japan and Korea, **no public confirmation** was found of local APMs (Pix, UPI, OXXO, boleto, Konbini, regional wallets) on any Bending Spoons web checkout. This is "Not verified," not "Not available" — but the absence on the Evernote/Remini web flows (card + PayPal only) is a strong signal of an APM gap in exactly the markets driving their traffic.

---

## S5 — Payment Complaints

| Theme | Evidence | Source |
|---|---|---|
| Unrecognized / unexpected charges | Dedicated BS help articles for "unrecognized charge from Bending Spoons" and Google-Play-labeled charges; multiple JustAnswer/Google Play Community threads | [BS Support](https://bendingspoonssupport.zendesk.com/hc/en-gb/articles/31044384664849-I-received-an-unrecognized-charge-from-Bending-Spoons), [Google Play Community](https://support.google.com/googleplay/thread/307753893/bending-spoons-scam-of-the-century?hl=en) |
| Refund friction / "can't refund" | BS states it cannot refund Apple/Google subs; routes users to Apple/Google — friction & deflection | [BS Support](https://bendingspoonssupport.zendesk.com/hc/en-gb/articles/32346488392721-I-received-a-PayPal-charge-from-Conceptive-Apps-LLC) |
| Hard-to-cancel / aggressive price hikes | Evernote pricing reportedly +257% ($70→$250/yr 2023→2026); Trustpilot "buys good services and turns them into bad ones" | [TrustPilot listing](https://www.trustpilot.com/review/bendingspoons.com) (page returned 403 on fetch; cited from search snippet) |
| "Scam" sentiment on Play Store | "Bending Spoons – Scam of the Century" community thread | [Google Play Community](https://support.google.com/googleplay/thread/307753893/bending-spoons-scam-of-the-century?hl=en) |

Note: Trustpilot page (`trustpilot.com/review/bendingspoons.com`) blocked direct fetch (403); claims above sourced from search-result snippets, not full-page verification.

---

## S6 — Expansion & Corporate Developments

| Date | Event | Value | Source |
|---|---|---|---|
| Jan 2023 | Evernote acquired | n/d | [Wikipedia](https://en.wikipedia.org/wiki/Bending_Spoons) |
| 2024 | Meetup, StreamYard/Hopin, Issuu | n/d | [Wikipedia](https://en.wikipedia.org/wiki/Bending_Spoons) |
| Jul 2024 | WeTransfer | n/d | [Fortune](https://fortune.com/europe/2024/08/01/wetransfer-acquired-bending-spoons-the-italian-software-powerhouse-behind-evernote-and-meetup-vimeo-remini-evernote/) |
| Nov 2024 | Brightcove | $233M | [Wikipedia](https://en.wikipedia.org/wiki/Bending_Spoons) |
| Mar 2025 | Komoot | ~€300M | [Wikipedia](https://en.wikipedia.org/wiki/Bending_Spoons) |
| Jul 2025 | MileIQ | $233M | [Wikipedia](https://en.wikipedia.org/wiki/Bending_Spoons) |
| Sep/Nov 2025 | Vimeo | $1.38B (delisted) | [Investing.com](https://www.investing.com/news/sec-filings/vimeo-acquired-by-bending-spoons-us-in-138-billion-cash-deal-delisted-from-nasdaq-93CH-4376218) |
| Oct 2025 | AOL | $1.5B | [TechCrunch](https://techcrunch.com/2026/01/25/what-is-bending-spoons-everything-to-know-about-aols-acquirer/) |
| Dec 2025 | Eventbrite | ~$500M | [Wikipedia](https://en.wikipedia.org/wiki/Bending_Spoons) |
| Apr 2026 | Tractive | n/d | [Wikipedia](https://en.wikipedia.org/wiki/Bending_Spoons) |
| Jun 8 2026 | Nasdaq IPO filing (BSP), ~$20B target | raise reportedly $1.5B+ | [Fortune](https://fortune.com/2026/06/08/bending-spoons-italian-aol-evernote-wetransfer-files-us-ipo/), [Bloomberg](https://www.bloomberg.com/news/articles/2026-06-08/vimeo-parent-bending-spoons-files-for-us-ipo-showing-sales-jump) |

---

## S7 — Payment News (last 12 months)

| Date | Item | Source |
|---|---|---|
| Jun 2026 | F-1 discloses app-store fees of 15–30% on ~⅓ of electronic-payment revenue; flags it vs. "Adyen/PayPal/Stripe ≤5%" | [mostlymetrics](https://www.mostlymetrics.com/p/bending-spoons-ipo-s1-breakdown) |
| Jun 2026 | Subscriptions = 84% of revenue; gross margin 68% in Q1-26, partly held back by "payments processor costs" | [mostlymetrics](https://www.mostlymetrics.com/p/bending-spoons-ipo-s1-breakdown) |
| 2024 | WeTransfer launches Stripe-powered creator payments/marketplace | [TechCrunch](https://techcrunch.com/2024/04/30/wetransfer-cuts-out-the-middle-man-and-now-lets-users-sell-files-directly-on-the-platform/) |

No public news found on a payment-orchestration RFP, PSP switch, or tokenization-vault project.

---

## S8 — Checkout Audit (observed, not full live-transaction tested)

| Brand | Type | Guest checkout | Steps | 3DS | Mobile | APM logic |
|---|---|---|---|---|---|---|
| Evernote (web) | Recurring subscription, direct | Account required | Card or PayPal on Billing page; supports currency change | Not verified | Responsive web | Card + PayPal only |
| Remini (web app.remini.ai) | Recurring (weekly $9.99 / monthly $24.99 / yearly $249.99) | Not found | Web paywall; checkout page not exposed to crawl | Not verified | Mobile-first | Not found |
| Splice / Remini (mobile) | IAP recurring | N/A (Apple/Google account) | StoreKit / Play Billing native | Handled by store | Native iOS/Android | Apple Pay / Google Pay |
| WeTransfer | Subscription + creator payments (Stripe) | Account required | Stripe-hosted | Stripe-managed | Responsive | Stripe APM set |
| Vimeo OTT | Creator/viewer payments (Stripe Connect) | Varies | Stripe Connect | Stripe-managed | Responsive | Stripe |

**Key finding:** Web checkouts are brand-siloed (different PSPs, different MoR entities, card+PayPal where present). No unified checkout experience or shared APM logic observed across the portfolio.

---

## S9 — PCI DSS

Evernote states it "contracts with third-party payment processors who are responsible for ensuring payment data is handled securely," using "credit card processing firms that are fully PCI-DSS compliant." ([Evernote security FAQ — search snippet](https://help.evernote.com/hc/en-us/articles/209005327-How-secure-is-my-credit-card-payment-information); page returned 403 on direct fetch.) No company-wide PCI level (e.g., Level 1 SAQ-D) disclosed publicly for the BS group. Mobile IAP keeps card data off BS systems entirely. Specific PCI certification level: **Not found.**

---

## S10 — Strategic Insights

**1. IAP fee leakage is quantified in their own F-1 — the strongest cold-open in months.**
- **Evidence:** ~⅓ of electronic-payment revenue runs through Apple/Google at 15–30%, vs. ≤5% for Adyen/PayPal/Stripe; they admit they accept it because "customers convert better when the App Store is the default." ([mostlymetrics](https://www.mostlymetrics.com/p/bending-spoons-ipo-s1-breakdown))
- **Pain:** Tens of millions in avoidable take-rate; gross margin held down "because of substantial payments processor costs."
- **Yuno value prop:** Orchestrate compliant web-billing / external-purchase flows (post-Epic, post-DMA) with smart routing + localized APMs to migrate convertible volume off IAP — capturing 10–25 pts of margin per migrated dollar.
- **Best case:** **Rappi** (multi-PSP routing + LatAm APMs at scale).
- **Angle:** "Your S-1 shows a third of card revenue paying 15-30% to the stores while Adyen/Stripe charge ≤5% — here's how peers route convertible volume to web without killing conversion."

**2. Fragmented post-acquisition PSP estate (Stripe + PayPal + Conceptive + in-house "Spoon" payments).**
- **Evidence:** WeTransfer/Vimeo on Stripe, Evernote on direct-card+PayPal via Conceptive Apps LLC, "payments" listed as an in-house Spoon Engine service. ([TechCrunch](https://techcrunch.com/2024/04/30/wetransfer-cuts-out-the-middle-man-and-now-lets-users-sell-files-directly-on-the-platform/), [BS Support](https://bendingspoonssupport.zendesk.com/hc/en-gb/articles/32346488392721-I-received-a-PayPal-charge-from-Conceptive-Apps-LLC), [Sacra](https://sacra.com/c/bending-spoons/))
- **Pain:** Every acquisition (now 50+, accelerating: AOL, Eventbrite, Tractive) re-creates integration + reconciliation work; no single routing/retry/failover layer.
- **Yuno value prop:** One integration that absorbs each acquired brand's existing PSP and adds new ones without re-coding — the consolidation layer for a roll-up.
- **Best case:** **Reserva** (multi-brand under one orchestration).
- **Angle:** "You buy a company every few weeks; each comes with its own billing stack. Yuno is the layer that makes PSP onboarding a config change, not an integration project."

**3. APM gap in their highest-traffic markets.**
- **Evidence:** Heavy traffic from Brazil, India, Philippines, Turkey, Japan, Korea ([Similarweb Evernote](https://www.similarweb.com/website/evernote.com/), [Remini](https://www.similarweb.com/website/remini.ai/)), yet confirmed web APMs are card + PayPal only.
- **Pain:** Lost conversion where Pix/UPI/Konbini/local wallets dominate; forced into high-fee IAP because web can't accept local methods.
- **Yuno value prop:** 1,000+ methods across 200+ countries via one API — add Pix, UPI, OXXO, Konbini, local wallets to web checkout to both lift conversion and pull volume off IAP.
- **Best case:** **InDrive** (emerging-market APM coverage at scale).
- **Angle:** "Your two biggest Remini markets are India and the Philippines — neither pays well with card-only web checkout. Here's the local-method coverage that lets you bypass the store tax."

**4. Resilience / decline-recovery for a 9M-subscriber, 84%-subscription book.**
- **Evidence:** 84% subscription revenue, ~9M subscribers, NRR 91-95%, 8-yr lifetimes ([mostlymetrics](https://www.mostlymetrics.com/p/bending-spoons-ipo-s1-breakdown)).
- **Pain:** Involuntary churn (failed renewals/declines) directly erodes NRR; no evidence of cross-PSP retry/cascading.
- **Yuno value prop:** Smart retries, network tokenization, and failover routing to recover declined renewals across all brands.
- **Best case:** **Livelo** (recurring/loyalty volume with recovery focus).
- **Angle:** "At 9M subs and 8-year lifetimes, a 1-pt decline-recovery gain is permanent ARR — and it's a margin lever you fully control, unlike the store fee."

**5. IPO timing = scrutiny on margin levers and platform-fee risk.**
- **Evidence:** F-1 explicitly names app-store fee dependence as a risk factor; analysts ask whether scale can negotiate fees down. ([investing.com search](https://www.investing.com/news/stock-market-news/bending-spoons-files-for-ipo-on-nasdaq-under-bsp-ticker-432SI-4730433))
- **Pain:** Public-market story needs a credible path to lower payment cost / higher gross margin.
- **Yuno value prop:** Orchestration is the documented lever to reduce the single largest controllable cost line and de-risk app-store dependence ahead of/after listing.
- **Best case:** **Rappi**.
- **Angle:** "Pre-IPO, the payment-cost line is the margin story investors will probe — orchestration is how you show a path to bend it."

---

## S11 — Pipeline / Account Scoring

| Type | Company | Score |
|---|---|---|
| **Direct peer (app roll-up / consumer subscription)** | Bending Spoons (subject) | 🔴 High (12+): global multi-brand subscription portfolio, quantified IAP fee pain in own filing, fragmented PSP estate, APM gaps in top markets, IPO-driven margin scrutiny, accelerating M&A |
| Industry peer | Photoroom / Picsart (AI photo, sub apps) | 🟡 Med |
| Industry peer | Duolingo / Babbel (consumer sub, multi-market) | 🟡 Med |
| Industry peer | Calm / Headspace (sub, IAP-heavy) | 🟡 Med |
| Industry peer | Eventbrite / Meetup (events, now BS-owned) | 🟢 Low (captive) |

Headline account score: **🔴 High (12+).**

---

## S12 — Business Case Inputs

| Metric | Value | Source |
|---|---|---|
| FY2025 revenue | ~$1.31B (95% YoY) | [techstartups](https://techstartups.com/2026/06/08/bending-spoons-files-for-u-s-ipo-after-revenue-doubles-to-601m-as-acquisition-strategy-pays-off/) |
| Q1 2026 revenue | $601M (+132% YoY); net income $27.5M | [techstartups](https://techstartups.com/2026/06/08/bending-spoons-files-for-u-s-ipo-after-revenue-doubles-to-601m-as-acquisition-strategy-pays-off/) |
| Subscription share | 84% of revenue | [mostlymetrics](https://www.mostlymetrics.com/p/bending-spoons-ipo-s1-breakdown) |
| Paying subscribers | ~9M | [mostlymetrics](https://www.mostlymetrics.com/p/bending-spoons-ipo-s1-breakdown) |
| MAU | 500M+ | [mostlymetrics](https://www.mostlymetrics.com/p/bending-spoons-ipo-s1-breakdown) |
| Electronic-payment share of revenue | 75%; ~⅓ via Apple/Google IAP (15-30% fee) | [mostlymetrics](https://www.mostlymetrics.com/p/bending-spoons-ipo-s1-breakdown) |
| Implied annual processed volume (subscription) | ~84% × ~$1.31B ≈ **~$1.1B** subscription revenue [INFERENCE — derived, not a stated GMV] | derived from above |
| Avg txn value | **N/A** (varies: Remini $9.99–$249.99; Evernote ~$129–$250/yr) — see [Remini ARPU range](https://apps.apple.com/us/app/remini-ai-photo-enhancer/id1470373330) |
| Est. annual txns | **Not found** (not disclosed; mix of weekly/monthly/annual) |
| Currency | Multi-currency (Evernote supports currency change) | [Evernote FAQ](https://help.evernote.com/hc/en-us/articles/28267325211795-Subscriptions-Payments-FAQ) |
| Top 3 markets (blended web) | United States, India, Japan/Brazil (varies by brand) | S1 tables above |

---

## S13 — Outreach

### 13A — LinkedIn (≤300 words)

Hi [First name],

Congratulations on the F-1 filing — building a 500M-MAU, 9M-subscriber portfolio across Evernote, WeTransfer, Vimeo and Remini through 50+ acquisitions is a genuinely rare feat.

One line in the filing jumped out from a payments lens: roughly a third of your electronic-payment revenue runs through Apple and Google at 15–30%, while the filing itself notes Adyen, PayPal and Stripe charge 5% or less. On a subscription book your size, that delta is one of the few margin levers you fully control.

There's a second angle that's almost unique to Bending Spoons: because you acquire a company every few weeks, each one arrives with its own billing stack (Stripe at WeTransfer and Vimeo, card + PayPal at Evernote, and so on). That's recurring integration and reconciliation work with every deal.

Yuno is a single API that orchestrates 1,000+ payment methods and PSPs across 200+ countries. For a roll-up like yours it does two things: it lets you add or absorb each acquired brand's PSP as a config change rather than an integration project, and it adds local methods (Pix in Brazil, UPI in India, Konbini in Japan — your biggest Remini and Evernote markets) plus compliant web-billing routing to move convertible volume off the app-store tax without hurting conversion.

Companies like Rappi, InDrive and Reserva use us for exactly this — multi-brand, multi-market routing with smart retries that lift authorization and recover failed renewals.

Worth a 20-minute conversation to map the fee delta against your top markets? Happy to share the peer benchmarks.

Best,
[Name] — Yuno

### 13B — Cold Email

**Subject:** The line in your S-1 about 15-30% app-store fees

Hi [First name],

Congratulations on the Nasdaq filing. Reading the S-1 from a payments seat, one disclosure stood out: about 75% of revenue runs through electronic payments, and roughly a third of that goes through the Apple App Store or Google Play at 15–30% — while the filing itself notes that Adyen, PayPal and Stripe charge 5% or less. With subscriptions at 84% of revenue and ~9M subscribers, that gap is one of the largest controllable cost levers in the business, and it's exactly the kind of margin story public markets will probe.

There's a second pattern specific to your model. Because you acquire a business roughly every few weeks, each arrives with its own billing stack — Stripe at WeTransfer and Vimeo, card plus PayPal at Evernote, and others. Every acquisition re-creates integration and reconciliation work, and there's no single routing or failover layer across the portfolio.

Yuno is one API that orchestrates 1,000+ payment methods and PSPs across 200+ countries. For Bending Spoons that means: absorb each acquired brand's existing PSP as configuration rather than a rebuild; add local methods in your highest-traffic markets (India and the Philippines for Remini, Japan and Brazil for Evernote) on web checkout; and use compliant routing plus smart retries to recover failed renewals and shift convertible volume off the store tax without hurting conversion.

Rappi, InDrive and Reserva run this exact playbook today.

Would a short call to map the fee delta against your top three markets be useful next week?

Best,
[Name] — Yuno

---

## Appendix — Source URLs

- https://techstartups.com/2026/06/08/bending-spoons-files-for-u-s-ipo-after-revenue-doubles-to-601m-as-acquisition-strategy-pays-off/
- https://www.mostlymetrics.com/p/bending-spoons-ipo-s1-breakdown
- https://en.wikipedia.org/wiki/Bending_Spoons
- https://sacra.com/c/bending-spoons/
- https://fortune.com/2026/06/08/bending-spoons-italian-aol-evernote-wetransfer-files-us-ipo/
- https://fortune.com/europe/2024/08/01/wetransfer-acquired-bending-spoons-the-italian-software-powerhouse-behind-evernote-and-meetup-vimeo-remini-evernote/
- https://www.bloomberg.com/news/articles/2026-06-08/vimeo-parent-bending-spoons-files-for-us-ipo-showing-sales-jump
- https://techcrunch.com/2024/07/31/bending-spoons-acquires-file-transfer-service-wetransfer/
- https://techcrunch.com/2024/04/30/wetransfer-cuts-out-the-middle-man-and-now-lets-users-sell-files-directly-on-the-platform/
- https://techcrunch.com/2026/01/25/what-is-bending-spoons-everything-to-know-about-aols-acquirer/
- https://www.investing.com/news/sec-filings/vimeo-acquired-by-bending-spoons-us-in-138-billion-cash-deal-delisted-from-nasdaq-93CH-4376218
- https://www.investing.com/news/stock-market-news/bending-spoons-files-for-ipo-on-nasdaq-under-bsp-ticker-432SI-4730433
- https://help.vimeo.com/hc/en-us/articles/12425768308625-Standard-Connect-for-Select-Markets-on-Vimeo-OTT
- https://help.evernote.com/hc/en-us/articles/28267325211795-Subscriptions-Payments-FAQ
- https://help.evernote.com/hc/en-us/articles/209005327-How-secure-is-my-credit-card-payment-information
- https://bendingspoonssupport.zendesk.com/hc/en-gb/articles/32346488392721-I-received-a-PayPal-charge-from-Conceptive-Apps-LLC
- https://bendingspoonssupport.zendesk.com/hc/en-gb/articles/31044384664849-I-received-an-unrecognized-charge-from-Bending-Spoons
- https://support.google.com/googleplay/thread/307753893/bending-spoons-scam-of-the-century?hl=en
- https://www.trustpilot.com/review/bendingspoons.com
- https://app.remini.ai/
- https://apps.apple.com/us/app/remini-ai-photo-enhancer/id1470373330
- https://support.bendingspoons.com/tos?app=1470373330
- https://spliceapp.com/app-terms-of-service/
- https://adapty.io/paywall-library/splice-video-editor-maker/
- https://cloud.google.com/customers/bending-spoons
- https://jobs.bendingspoons.com/positions/6a22779735de636e51dd3568
- https://www.similarweb.com/website/wetransfer.com/
- https://www.similarweb.com/website/vimeo.com/
- https://www.similarweb.com/website/evernote.com/
- https://www.similarweb.com/website/remini.ai/
- https://www.similarweb.com/website/meetup.com/

**Verification caveats:** Trustpilot and two Evernote help pages returned HTTP 403 on direct fetch; claims sourced from those URLs rely on search-result snippets and should be re-confirmed live before quoting in a customer-facing deck. Revenue figures vary across early reports ($601M was Q1-2026, not full-year; FY2025 = ~$1.31B). The "in-house payments" orchestration conclusion is an inference from the Spoon Engine service list, not a confirmed absence of a third-party orchestrator.
