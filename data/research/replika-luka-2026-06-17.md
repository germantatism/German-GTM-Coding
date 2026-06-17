# SDR Research Brief — Replika (Luka, Inc.)

**Prepared for:** Yuno | **Date:** 2026-06-17 | **Analyst:** Payments Intelligence

---

## Executive Summary

Replika is the leading AI-companion chatbot app, operated by US-incorporated **Luka, Inc.** (San Francisco / Delaware), with **40M+ registered users across 150+ countries** and a freemium subscription model (Replika Pro) layered on top of heavy App Store / Google Play in-app-purchase (IAP) reliance. Web subscriptions are processed through **Stripe and PayPal** (confirmed via privacy policy and help-center signals), while the bulk of paid conversions route through **Apple and Google IAP at 15–30% commission** — a structure that caps margin and removes Replika's control over billing, refunds, and APM coverage. The company carries a measurable trust deficit on billing: an **F rating at the BBB (29 complaints)**, recurring Trustpilot/BBB complaints about double-charges, trial-to-annual auto-upgrades, and cancel-difficulty, plus a **€5M GDPR fine from Italy's Garante (2025)**. With a large international base (US, France, Germany, Russia, Taiwan on web; plus India/Brazil organic demand for AI companions) and an apparent single direct-web-PSP setup, Replika fits the Yuno cross-border + APM-gap + single-PSP-dependency thesis.

---

## S1 — Traffic by Country

Source: Similarweb (replika.com, May 2026 snapshot).

| Country | Share of web traffic | Notes |
|---|---|---|
| United States | 44.91% | Dominant market |
| France | 6.61% | |
| Germany | 4.85% | |
| Russia | 3.48% | |
| Taiwan | 3.45% | |
| **Total monthly visits** | **744.2K** | +15.16% MoM; global rank #67,335 |

- replika.com core audience also cited as US, **Mexico, India** in alternate Similarweb view. [Similarweb replika.com]
- replika.ai (separate property): ~109.8K visits, 41% bounce, US-led. [Similarweb replika.ai, Apr 2026]
- Note: Similarweb measures **web only**; the overwhelming majority of Replika usage and revenue is **mobile/IAP**, not captured here. [INFERENCE — not confirmed]

---

## S2 — Legal Entities

| Entity | Role | Jurisdiction / Address | Source |
|---|---|---|---|
| Luka, Inc. | Parent / operating company ("dba Replika") | Incorporated Delaware; HQ 490 Post St, Ste 526, San Francisco, CA 94102 (also cited 1266 Harrison St per BBB) | Replika legal notice; Padilla Senate letter; BBB |
| Replika | Flagship product (AI companion app) | Launched Nov 2017 | Wikipedia |
| Blush | Sibling app — AI dating sim ($99/yr premium) | Luka, Inc., San Francisco | Fast Company; PR Newswire |
| Tomo | Sibling app — AI wellness/coaching ($8/wk or $50/yr) | Luka, Inc. | Axios |

**Leadership:** Founder **Eugenia Kuyda stepped down as CEO in 2025** to launch new venture **Wabi** (raised ~$20M led by a16z); remains advisor. Former COO **Dmytro Klochko** now runs day-to-day. [LinkedIn; MindSite News; Crunchbase]

---

## S3 — Payment Stack

### 3A — PSPs / Acquirers / MoR

| Provider | Role | Confirmation | Source |
|---|---|---|---|
| **Stripe** | Direct web-subscription PSP | Named in third-party pricing/help guidance; Replika privacy policy confirms "third-party payment processors collect your payment information" | eesel AI; Replika privacy policy |
| **PayPal** | Alternate web payment method | Cited alongside Stripe as accepted methods | Search-corroborated; Replika privacy policy (generic "payment processors") |
| **Apple App Store (IAP)** | Mobile billing / MoR for iOS subs | "payments charged to iTunes… processed by the app marketplace partner" | Replika ToS / help center |
| **Google Play (IAP)** | Mobile billing / MoR for Android subs | Same as above | Replika ToS / help center |

> Replika's own help/ToS: "All payments and subscriptions are managed by Apple and Google, so Replika cannot process refunds or handle subscription changes on their end." This confirms heavy IAP dependence and loss of billing control. [Replika help center / ToS]

### 3B — Payment Orchestrator?

**No evidence of a payment orchestrator.** Web subscriptions appear to run on a **single direct PSP (Stripe)** plus PayPal, with mobile fully delegated to Apple/Google IAP. No public signal of Yuno, Spreedly, Primer, or comparable orchestration. [INFERENCE — not confirmed; based on absence of any orchestrator reference across privacy policy, ToS, and public sources]

---

## S4 — APMs Confirmed

| APM / Method | Status | Source |
|---|---|---|
| Credit/Debit card (via Stripe) | Confirmed (web) | eesel AI; privacy policy |
| PayPal | Confirmed (web) | Search-corroborated |
| Apple Pay / App Store balance (IAP) | Confirmed (iOS) | Replika ToS |
| Google Play balance / Google Pay (IAP) | Confirmed (Android) | Replika ToS |

**Unverified Markets / APM Gaps (not confirmed available — "not verified" ≠ "not available"):**
- **LATAM** (Mexico is a top-traffic market; Brazil strong organic demand): Pix, Boleto, OXXO, local cards/installments — **Not found** in any Replika checkout/help/ToS source.
- **APAC** (Taiwan top-5 web market; India significant): UPI (India), local wallets, carrier billing beyond IAP — **Not found**.
- **Europe** (France/Germany top markets): iDEAL, SEPA, Bancontact, Klarna — **Not found** as direct-web methods.

---

## S5 — Payment Complaints

| Complaint Theme | Detail | Source |
|---|---|---|
| Double / unexpected charges | Charged $39.50/mo after canceling a $19.95 trial; charges $40 USD–100 PLN reported | BBB; Trustpilot |
| Deceptive trial→annual upgrade | $1.25 "week" promo billed as $59.99/yr; trials auto-upgrade to Pro at higher rate without clear warning | BBB; Trustpilot |
| Cancellation difficulty | "No option in the menu to cancel"; users looped to initial page with no confirmation; support unresponsive | Trustpilot |
| Refund denial / no-refund policy | Refunds denied; "strict no-refund policy," auto-renewal on by default | BBB |
| Support deflection to app stores | Users "fobbed off to another company" (i.e., told to seek refund via Apple/Google) | Trustpilot; Replika help center |
| Overall trust signal | **BBB: F rating, not accredited, 29 complaints / 21 unanswered** | BBB |

---

## S6 — Expansion & Corporate Developments

| Development | Detail | Source |
|---|---|---|
| User scale | 2M (2018) → 10M (2023) → 30M (Aug 2024) → **40M+ (2025)**, 150+ countries | Wikipedia; aicompanionpick |
| Sibling apps | **Blush** (AI dating sim) and **Tomo** (AI wellness) launched under Luka | Fast Company; Axios |
| Founder transition | Kuyda → Wabi (2025, $20M a16z); Klochko now CEO | LinkedIn; MindSite News |
| Product/monetization | 2026 ElevenLabs voice add-on: vendor-claimed +20% 7-day retention, +53% long voice calls for paid users | aicompanionpick |
| Funding | ~$40M raised total (incl. $6.5M Series A.2 led by Khosla/Sherpa, 2017) | PR Newswire; search-corroborated |

---

## S7 — Payment / Regulatory News (last ~12 months)

| Date | Event | Relevance | Source |
|---|---|---|---|
| May 2025 | **Italian Garante fines Luka, Inc. €5M** for GDPR violations (no valid legal basis, no age verification, English-only/opaque privacy policy) | Heightened EU compliance/data-handling scrutiny; privacy policy is the same doc governing payment-data sharing | EDPB; Garante; PYMNTS |
| 2025 (ongoing) | Garante reserves separate proceeding on lawfulness of LLM-lifecycle data processing | Continued regulatory overhang | EDPB |
| Feb 2023 (context) | Italy previously banned Replika from processing Italian user data | Pattern of EU enforcement | Wikipedia |

No public M&A, IPO, or new-PSP payment-infrastructure announcements found.

---

## S8 — Checkout Audit

| Attribute | Web (replika.ai / .com — Replika Pro) | Mobile (iOS/Android IAP) |
|---|---|---|
| Subscription type | Monthly / Yearly / Lifetime; Pro + Ultra tiers | Monthly/quarterly/semi-annual/annual installments |
| Guest checkout | Account required (login at replika.ai → Settings → Subscriptions) | Tied to Apple ID / Google account |
| Steps | Login → Settings → Subscriptions → select plan → pay (card via Stripe / PayPal) | Native store sheet |
| 3DS / SCA | Not found (Stripe supports 3DS2; not independently verified on Replika flow) | Handled by Apple/Google |
| Mobile-optimized | Yes (app-native) | Yes |
| APM logic / geo-routing | **No evidence of geo-based APM display or local-method routing** [INFERENCE — not confirmed] | Limited to store-supported methods |

Sources: Replika help center ("Choosing a Subscription," "How do I change my Pro subscription"); eesel AI; pricing aggregators.

---

## S9 — PCI DSS

- Replika does **not** directly collect card data: "our third-party payment processors collect your payment information." [Replika privacy policy]
- Card processing rides on **Stripe, certified PCI Service Provider Level 1** (highest tier). [Stripe security docs]
- IAP card data handled entirely by **Apple/Google**.
- No independent PCI attestation published by Luka, Inc. itself — compliance is **inherited from processors**, which is standard for an app of this profile. [INFERENCE — not confirmed]

---

## S10 — Strategic Insights

**1. Single direct-web PSP + total IAP dependence = margin and control gap**
- **Evidence:** Web subs via Stripe/PayPal only; mobile fully delegated to Apple/Google (15–30% commission); "Replika cannot process refunds… on their end." [ToS; privacy policy]
- **Pain Point:** No control over mobile billing, no PSP redundancy on web, 15–30% IAP tax on the majority of revenue.
- **Yuno Value Prop:** Single API to orchestrate multiple PSPs/acquirers on the web flow, enable app-to-web purchase migration (steer users off IAP), and add failover + smart routing to lift auth rates.
- **Best Case:** **InDrive** — global consumer app that used Yuno to orchestrate multiple PSPs and local methods across emerging markets.
- **Outreach Angle:** "With 40M users in 150+ countries on essentially one web PSP and Apple/Google taking 15–30%, every point of auth-rate or IAP-bypass is pure margin — that's the wedge."

**2. Cross-border base, no local APMs**
- **Evidence:** Top markets include Mexico, France, Germany, Taiwan, India, Brazil; checkout shows only card + PayPal. [Similarweb; eesel AI]
- **Pain Point:** Card-only in markets where Pix, OXXO, UPI, iDEAL drive conversion — leaving paid-conversion money on the table internationally.
- **Yuno Value Prop:** Instant access to 1,000+ local payment methods through one integration; geo-aware checkout.
- **Best Case:** **Rappi** — scaled LATAM coverage by adding local APMs via a single orchestration layer.
- **Outreach Angle:** "Mexico and Brazil are top demand markets for AI companions, but a card-only web checkout caps conversion there. Pix/OXXO/UPI through one API is the unlock."

**3. Acute billing-trust problem (BBB F-rating, double-charges, cancel friction)**
- **Evidence:** BBB F (29 complaints/21 unanswered); Trustpilot double-charge, trial-upgrade, and cancel-loop reports. [BBB; Trustpilot]
- **Pain Point:** Billing disputes, involuntary churn, chargeback exposure, reputational damage.
- **Yuno Value Prop:** Unified subscription/billing visibility, retry & dunning logic, and consolidated reconciliation across PSPs to reduce failed payments and dispute volume.
- **Best Case:** **Livelo** — subscription/loyalty platform that used orchestration to stabilize recurring billing.
- **Outreach Angle:** "An F at the BBB on billing is recoverable — most of those complaints are retry/dunning and cancel-flow problems orchestration solves."

**4. EU regulatory overhang raises the cost of fragmented data/payment ops**
- **Evidence:** €5M Garante fine (2025) on opaque, English-only privacy policy — the same doc governing payment-data sharing. [EDPB; Garante]
- **Pain Point:** Fragmented payment-data flows across Stripe/PayPal/Apple/Google increase compliance surface in the EU (top markets France/Germany).
- **Yuno Value Prop:** Centralized, auditable payment-data layer and consistent processing logic across providers.
- **Best Case:** **Reserva** — consolidated payment operations to simplify compliance and reporting.
- **Outreach Angle:** "Post-Garante, a single orchestration layer gives you one auditable view of payment data across every processor in the EU."

**5. App-to-web migration upside (newer apps Blush/Tomo + voice add-ons)**
- **Evidence:** Multi-app portfolio (Replika, Blush $99/yr, Tomo) all on IAP-heavy models; 2026 voice add-on driving paid retention. [Fast Company; Axios; aicompanionpick]
- **Pain Point:** Each new app re-pays the IAP tax and rebuilds billing from scratch.
- **Yuno Value Prop:** One orchestration layer serving the whole Luka portfolio; standardized web checkout to capture margin Apple/Google take.
- **Best Case:** **InDrive** — multi-product consumer suite on one payment backbone.
- **Outreach Angle:** "You're launching Blush and Tomo on the same IAP model — build the web-billing rail once with Yuno and every app inherits it."

---

## S11 — Pipeline / Account Scoring

Scoring: 🔴 High 12+ / 🟡 Med 7–11 / 🟢 Low <7 (cross-border reach + single-PSP dependency + APM gap + complaint volume + scale).

| Company | Type | Signals | Score |
|---|---|---|---|
| **Replika (Luka, Inc.)** | Target | 40M users/150+ countries, single web PSP, full IAP reliance, BBB-F billing complaints, €5M fine, LATAM/APAC APM gaps | 🔴 **13 — High** |
| Character.AI | Direct competitor | 45M MAU, $50M rev 2025, 75M+ downloads, IAP-heavy, Google-acquired (deal terms ~$2.7B) | 🔴 12 |
| Chai AI | Direct competitor | ~$80M ARR, mobile-first companion app | 🟡 9 |
| Nomi AI | Direct competitor | Self-funded, subscription companion | 🟡 7 |
| Talkie AI | Direct competitor | High engagement (~62 min/day), global | 🟡 9 |
| Candy.ai | Direct competitor | ~$25M ARR, bootstrapped, web-subscription heavy | 🟡 10 |
| Paradot / Anima | Direct competitor | Smaller AI-companion apps | 🟢 6 |
| Blush (Luka) | Industry peer (same parent) | $99/yr, IAP model — same buyer | 🔴 (warm via Replika) |
| Tomo (Luka) | Industry peer (same parent) | Wellness subs $8/wk–$50/yr | 🟡 (warm via Replika) |

---

## S12 — Business Case

| Metric | Value | Basis / Source |
|---|---|---|
| Est. annual revenue | **~$24M (2024)**, ~$30M (2023); $14M ARR cited June 2024 | search-corroborated; aicompanionpick |
| Registered users | 40M+ (2025) | Wikipedia; aicompanionpick |
| Paid conversion | ~25% of base on annual subscription (per Wikipedia) | Wikipedia |
| Avg transaction value | **~$70/yr** (Pro annual $69.99) to $19.99/mo; Ultra $119.99/yr; Lifetime $299.99 | eesel AI; pricing aggregators |
| Est. annual paid transactions | **[INFERENCE — not confirmed]** If ~$24M revenue at a blended ~$70 effective annual ticket → **~340K paying subscriptions/yr** (order-of-magnitude only; mix unknown) | derived from above |
| Primary currency | USD (US #1 market) | Similarweb |
| Top 3 markets | United States, France, Germany (web); Mexico/India/Taiwan/Brazil notable | Similarweb; search |

> **Yuno opportunity sizing:** With the majority of revenue flowing through Apple/Google IAP at 15–30%, even a partial app-to-web migration plus international APM enablement represents a multi-million-dollar annual margin and incremental-conversion opportunity. [INFERENCE — directional]

---

## S13 — Outreach

### 13A — LinkedIn (≤300 words)

Hi [First Name] — I lead payments-orchestration conversations at Yuno, where we connect consumer apps to 1,000+ payment methods and multiple PSPs through one API across 200+ countries.

I've been following Replika's growth to 40M+ users across 150+ countries — genuinely one of the most globally distributed consumer-AI products out there. That scale is exactly where payments quietly become a growth lever.

Two things stood out from the outside: your web subscriptions run through a single direct processor, and the majority of paid conversions flow through Apple and Google IAP at 15–30%. For a base that's strong in Mexico, France, Germany, India, Taiwan and Brazil, a card-only web checkout also leaves local methods (Pix, OXXO, UPI, iDEAL) — and conversion — on the table.

Yuno gives you one integration to add PSP redundancy and smart routing on the web, enable app-to-web purchase flows to recover IAP margin, and switch on local payment methods market by market — without re-engineering each time you launch something new like Blush or Tomo.

Worth a 20-minute look at where the margin and conversion upside sits? Happy to share how comparable global consumer apps (InDrive, Rappi) approached it.

Best, [Your Name]

### 13B — Cold Email

**Subject:** 40M users, one web PSP — the margin hiding in Replika's checkout

Hi [First Name],

Replika reaching 40M+ users across 150+ countries is a serious distribution story — and at that scale, payments stop being plumbing and start being a growth lever.

From the outside, two patterns stand out. First, your web subscriptions appear to run through a single direct processor (Stripe/PayPal), with no redundancy or smart routing if a transaction fails. Second, the majority of paid conversions flow through Apple and Google IAP at 15–30% commission — margin you don't control, on the exact users who already chose to pay.

There's also a geographic gap: with strong demand in Mexico, France, Germany, India, Taiwan and Brazil, a card-only web checkout misses the local methods that actually convert in those markets (Pix, OXXO, UPI, iDEAL).

Yuno is a single API that lets you orchestrate multiple PSPs, add failover and smart routing to lift auth rates, build app-to-web purchase flows to recover IAP margin, and switch on 1,000+ local payment methods country by country — reusable across Replika, Blush and Tomo.

Global consumer apps like InDrive and Rappi used exactly this approach to grow internationally without rebuilding payments per market.

Would a short call next week make sense to look at where the conversion and margin upside is for Luka?

Best,
[Your Name] | Yuno

*Note: This email references only verified findings (single web PSP, IAP reliance, geographic footprint). It does not assert that any specific local method is currently unavailable — only that they are not confirmed present.*

---

## Appendix — Source URLs

- Similarweb replika.com — https://www.similarweb.com/website/replika.com/
- Similarweb replika.ai — https://www.similarweb.com/website/replika.ai/
- Replika Privacy Policy — https://replika.com/legal/privacy/en
- Replika Terms of Service — https://replika.com/legal/terms/en
- Replika Legal Notice (Impressum) — https://replika.com/impressum/en
- Replika Help — Subscriptions & Purchases — https://help.replika.com/hc/en-us/categories/4410747630093-Subscriptions-Purchases
- Replika Help — App Store/Play refunds — https://help.replika.com/hc/en-us/articles/360061935212-How-do-I-get-a-refund-in-the-Google-PlayStore-or-Apple-AppStore
- eesel AI — Replika pricing breakdown — https://www.eesel.ai/blog/replika-ai-pricing
- Wikipedia — Replika — https://en.wikipedia.org/wiki/Replika
- Y Combinator — Replika — https://www.ycombinator.com/companies/replika
- Padilla Senate letter to Luka, Inc. — https://www.padilla.senate.gov/wp-content/uploads/AI-Chatbot-Safety-Replika.pdf
- BBB — Replika.com complaints/profile — https://www.bbb.org/us/ca/san-francisco/profile/artificial-intelligence/replikacom-1116-930289/complaints
- Trustpilot — replika.com — https://www.trustpilot.com/review/replika.com
- EDPB — Italy fines Luka/Replika €5M — https://www.edpb.europa.eu/news/national-news/2025/ai-italian-supervisory-authority-fines-company-behind-chatbot-replika_en
- PYMNTS — Italy €5M fine — https://www.pymnts.com/cpi-posts/italy-fines-ai-chatbot-maker-replika-e5-million-over-privacy-violations/
- Fast Company — Blush launch — https://www.fastcompany.com/90906240/the-creators-of-replika-unveil-a-new-ai-dating-app-called-blush
- Axios — Tomo / wellness apps — https://www.axios.com/2024/01/30/ai-chatbots-human-loneliness-tomo-luka
- MindSite News — Kuyda interview (2026) — https://mindsitenews.org/2026/02/09/replikas-eugenia-kuyda-doesnt-believe-in-regulation/
- Crunchbase — Eugenia Kuyda / Wabi — https://www.crunchbase.com/person/eugenia-kuyda
- aicompanionpick — Replika user base / ARR — https://www.aicompanionpick.com/replika-user-base-2026
- TechCrunch — AI companion apps $120M in 2025 — https://techcrunch.com/2025/08/12/ai-companion-apps-on-track-to-pull-in-120m-in-2025/
- electroiq — Character.AI / AI companion stats — https://electroiq.com/stats/character-ai-statistics/
- Stripe security / PCI — https://docs.stripe.com/security
- PR Newswire — Replika Series A.2 funding — https://www.prnewswire.com/news-releases/replika-ai-confidant-raises-65-million-in-series-a2-funding-on-heels-of-the-personal-chatbot-opening-to-15-million-users-on-the-waitlist-300564092.html

**Integrity note:** PSP identification (Stripe/PayPal) is corroborated by Replika's privacy policy (third-party processors) plus multiple secondary sources, but the privacy policy does not name processors explicitly. APM availability beyond card/PayPal/IAP is marked "Not found" rather than "not offered." All inference-based estimates are labeled.
