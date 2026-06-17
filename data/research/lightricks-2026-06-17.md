# SDR Research Brief — Lightricks Ltd.

**Prepared for Yuno B2B Sales | Date: 2026-06-17**
**Primary apps:** Facetune, Photoleap, Videoleap, LTX Studio | **HQ:** Jerusalem, Israel

---

## Executive Summary
Lightricks is a ~$300M-revenue Israeli creative-app company (Facetune, Photoleap, Videoleap) with **6.6M+ monthly paying users**, 50M+ monthly users, and 730M+ lifetime downloads, that explicitly sells subscriptions both via Apple/Google IAP and direct on its own websites ([Lightricks Wikipedia](https://en.wikipedia.org/wiki/Lightricks); [Calcalist](https://www.calcalistech.com/ctechnews/article/r1dgjt5gmg)). Its web checkout runs on a **multi-PSP stack of Stripe, Adyen and PayPal** (confirmed in its own published refund policy and terms of use), with Apple Pay/Google Pay routed through Adyen ([Refund Policy](https://static.lightricks.com/legal/refund-policy.html); [Terms of Use](https://static.lightricks.com/legal/terms-of-use.html)). The company is mid-restructuring — splitting Facetune (consumer apps) from its LTX AI-video unit and cutting 75 jobs — which sharpens the consumer business's focus on subscription margin and the well-known IAP fee-escape motion ([Calcalist](https://www.calcalistech.com/ctechnews/article/r1dgjt5gmg)). Facetune carries severe, public billing-complaint volume (1.4★ Trustpilot, 350+ complaints) around surprise charges, cancellation friction and refund denials — a direct subscription-lifecycle pain point Yuno orchestration addresses ([Trustpilot](https://www.trustpilot.com/review/facetuneapp.com); [PissedConsumer](https://facetune.pissedconsumer.com/review.html)).

---

## S1 — Traffic by Country

**lightricks.com** (corporate/portfolio site) — Total monthly visits: ~346.9K ([Similarweb](https://www.similarweb.com/website/lightricks.com/))

| Rank | Country | Share |
|------|---------|-------|
| 1 | United States | 27.39% |
| 2 | India | 10.76% |
| 3 | Israel | 5.51% |
| 4 | Brazil | 4.43% |
| 5 | Spain | 3.94% |
| — | Other | 47.98% |

**facetuneapp.com** (consumer web checkout) — Total monthly visits: ~499K ([Similarweb](https://www.similarweb.com/website/facetuneapp.com/))

| Rank | Country | Share |
|------|---------|-------|
| 1 | United States | 39.31% |
| 2 | India | 3.01% |
| 3 | United Kingdom | 2.76% |
| 4 | Germany | 2.69% |
| 5 | Australia | 2.57% |
| — | Other | ~49.66% |

*Note: Similarweb desktop-weighted web-traffic share. The vast majority of Lightricks' actual paying volume sits inside mobile App Store / Google Play IAP, not captured by web analytics. Brazil + India presence indicates meaningful LATAM/APAC demand where local APMs (Pix, UPI) materially lift conversion. [INFERENCE — not confirmed].*

---

## S2 — Legal Entities

| Entity | Jurisdiction | Address / ID | Source |
|--------|-------------|--------------|--------|
| Lightricks Ltd. | Israel (HQ) | Building 5.4, Prof. Racah, Givat Ram Campus, Jerusalem 91904; Co. No. 514879071. Also Yesha'yahu Leibowitz 30, Jerusalem | [Craft.co](https://craft.co/lightricks/locations) |
| Lightricks (Haifa office) | Israel | 1 Andrei Sakharov St, Matam Park, Haifa 3508409 | [Craft.co](https://craft.co/lightricks/locations) |
| Lightricks US, Inc. | USA | 530 5th Ave., New York, NY 10036; 311 W Monroe St., Chicago, IL 60606 (named co-defendant in BIPA settlement) | [Craft.co](https://craft.co/lightricks/locations); [ClassAction.org](https://www.classaction.org/news/nearly-4.5m-lightricks-settlement-resolves-lawsuit-over-alleged-biometric-privacy-violations) |
| Lightricks UK Ltd. | United Kingdom | 105 Bunhill Row, London EC1Y 8LZ; Companies House No. 11444887 | [Companies House](https://find-and-update.company-information.service.gov.uk/company/11444887/officers) |

---

## S3 — Payment Stack

### 3A — PSPs / Acquirers (web checkout)

| Provider | Role | Confirmation | Source |
|----------|------|--------------|--------|
| **Stripe** | PSP / card processing (web) | Named: "Stripe, Adyen and PayPal are PCI compliant service providers" | [Refund Policy](https://static.lightricks.com/legal/refund-policy.html) |
| **Adyen** | PSP / card + wallet processing (web); processes Apple Pay & Google Pay | Named in refund policy and ToU ("payment made and processed via the payment service Provider Ayden [sic]…Visa or Mastercard or Maestro…including through Apple Pay or Google Pay") | [Terms of Use](https://static.lightricks.com/legal/terms-of-use.html) |
| **PayPal** | Alternative payment method (web) | Named in refund policy and ToU | [Refund Policy](https://static.lightricks.com/legal/refund-policy.html) |
| **Apple App Store IAP** | Mobile billing (iOS) | App Store distribution; subscriptions sold via Apple | [Lightricks Help Center](https://lightricks.zendesk.com/hc/en-us/articles/6096750327570-How-Do-I-Cancel-A-Subscription-Or-Free-Trial) |
| **Google Play IAP** | Mobile billing (Android) | Play Store distribution | [Google Play – Facetune](https://play.google.com/store/apps/details?id=com.lightricks.facetune.free) |

Billing descriptor on card statements: **"Lightricks Ltd."** ([Lightricks Help Center](https://lightricks.zendesk.com/hc/en-us/articles/12524222810386-Learn-about-an-unfamiliar-charge)).

### 3B — Orchestrator: **NO (self-managed multi-PSP)**
Lightricks already runs **three PSPs in parallel (Stripe + Adyen + PayPal)** on its own web checkout, but there is **no public evidence of a payment orchestration layer** managing routing, failover, retries, or APM logic across them ([Refund Policy](https://static.lightricks.com/legal/refund-policy.html); [Terms of Use](https://static.lightricks.com/legal/terms-of-use.html)). This is the strongest Yuno signal: a company that has *already chosen* to run multiple PSPs but is stitching them together with in-house engineering. No public evidence of a third-party orchestrator was found. For mobile, RevenueCat is a plausible IAP-subscription layer given its category dominance, but **no public confirmation that Lightricks uses RevenueCat was found** [INFERENCE — not confirmed].

---

## S4 — APMs Confirmed

| Payment Method | Channel | Status | Source |
|----------------|---------|--------|--------|
| Visa / Mastercard / Maestro (credit/debit) | Web | ✅ Confirmed | [Terms of Use](https://static.lightricks.com/legal/terms-of-use.html) |
| Apple Pay | Web (via Adyen) + iOS IAP | ✅ Confirmed | [Terms of Use](https://static.lightricks.com/legal/terms-of-use.html) |
| Google Pay | Web (via Adyen) + Android IAP | ✅ Confirmed | [Terms of Use](https://static.lightricks.com/legal/terms-of-use.html) |
| PayPal | Web | ✅ Confirmed | [Refund Policy](https://static.lightricks.com/legal/refund-policy.html) |
| Apple App Store balance / Apple Account methods | iOS IAP | ✅ Confirmed | [Lightricks Help Center](https://lightricks.zendesk.com/hc/en-us/articles/6096750327570-How-Do-I-Cancel-A-Subscription-Or-Free-Trial) |
| Google Play balance / Play methods | Android IAP | ✅ Confirmed | [Google Play](https://play.google.com/store/apps/details?id=com.lightricks.facetune.free) |

### Unverified Markets / APM Gaps
The web stack is described only as "payment methods supported by Stripe, Adyen and PayPal" ([Refund Policy](https://static.lightricks.com/legal/refund-policy.html)). **No public confirmation found** that the following high-relevance local APMs are offered, despite meaningful traffic in those regions:
- **Brazil (4.4% of lightricks.com traffic):** Pix, Boleto — **Not found / not verified.**
- **India (10.8% lightricks.com / 3.0% facetune traffic):** UPI, RuPay, Paytm — **Not found / not verified.**
- **Mexico / LATAM:** OXXO, SPEI, Mercado Pago — **Not found / not verified.**
- **APAC:** GrabPay, GCash, KakaoPay, Alipay — **Not found / not verified.**
- **MENA:** Mada, Fawry, regional wallets — **Not found / not verified.**

*Per integrity rules: absence of public confirmation ≠ unavailable. These are verified-via-traffic gaps to probe, not asserted absences.*

---

## S5 — Payment Complaints

| Source | Volume / Rating | Core Issue | Link |
|--------|-----------------|------------|------|
| Trustpilot (facetuneapp.com) | **1.4★, 92%+ one-star** | Unauthorized charges, impossible cancellation, refund denials | [Trustpilot](https://www.trustpilot.com/review/facetuneapp.com) |
| PissedConsumer | **1.5★, 69+ reviews, 350+ complaints over 3 yrs** | Fraud/unauthorized payments, refund denials, poor support | [PissedConsumer](https://facetune.pissedconsumer.com/review.html) |
| Apple Community / Pine AI | Multiple threads | Free-trial→paid auto-conversion without notice; "dual/shadow subscription" from Facebook-ad sign-ups invisible in Apple subscriptions | [Pine AI](https://www.19pine.ai/cancel-subscription/newspaper-magazine-and-online-learning/how-to-cancel-facetune); [Apple Community](https://discussions.apple.com/thread/254785711) |
| Sikayetvar / arefund.com | Multiple | Charged after trial without notice; Apple refusing refunds | [Sikayetvar](https://www.sikayetvar.com/en/facetune-2-us/facetune-charged-me-after-trial-without-notice-requesting-refund) |

**Theme:** The pain is concentrated in **subscription lifecycle** — trial conversion, cancellation friction, surprise renewals, refund disputes, and a "shadow subscription" problem where ad-driven web sign-ups are invisible to the user. This is precisely the lifecycle/dunning/transparency surface a unified orchestration + subscription layer governs.

---

## S6 — Expansion & Corporate Developments

| Date | Development | Source |
|------|-------------|--------|
| Sep 2021 | $130M Series D ($100M primary + $30M secondary) at **$1.8B valuation**; total raised ~$335M. Investors: Insight Partners, Hanaco, Goldman Sachs, ClalTech, Greycroft, Migdal, Shavit | [TechRound](https://techround.co.uk/news/lightricks-valued-1-8-billion-funding-round/); [FinSMEs](https://www.finsmes.com/2021/09/130-million-series-d-round-lifts-valuation-of-lightricks-to-1-8-billion.html) |
| Jul 2025 | Hit **$250M ARR** (~46% YoY growth); 6.6M+ monthly paying users | [Shavit Capital](https://www.shavitcapital.com/the-250-million-arr-club-israels-most-lucrative-tech-startups/) |
| 2025–26 | App business ~$300M revenue, growing ~20%/yr; ~$150M invested into AI/LTX | [Startup Fortune](https://startupfortune.com/lightricks-splits-itself-in-two-as-ai-costs-force-a-reset/) |
| 2026 | **Company split:** Facetune (consumer, ~100 staff, led by Asaf Porat) separated from **LTX** AI-video unit (~250 staff, led by CEO Zeev Farbman); **75 jobs cut** (17% of staff), ~350 employees post-cut | [Calcalist](https://www.calcalistech.com/ctechnews/article/r1dgjt5gmg) |

---

## S7 — Payment / Product News (last 12 months)

| Date | Item | Relevance | Source |
|------|------|-----------|--------|
| Oct 2025 | LTX-2 next-gen AI video/audio model launched (partner: NVIDIA); LTX-2 API + commercial licensing (tens of $M annualized from Fortune 500/big tech) | New B2B/API monetization channel = new payments surface | [PR Newswire](https://www.prnewswire.com/news-releases/lightricks-releases-ltx-2-the-first-complete-open-source-ai-video-foundation-model-302593012.html) |
| Jan 2026 | LTX-2 open-sourced (open weights) | Strategic AI pivot | [GlobeNewswire](https://www.globenewswire.com/news-release/2026/01/06/3213304/0/en/Lightricks-Open-Sources-LTX-2-the-First-Production-Ready-Audio-and-Video-Generation-Model-With-Truly-Open-Weights.html) |
| 2026 | Facetune/LTX corporate split + layoffs (cost reset) | Consumer unit now standalone, margin-focused → IAP-fee pressure acute | [Calcalist](https://www.calcalistech.com/ctechnews/article/r1dgjt5gmg) |
| Nov 2024 (settled) | ~$4.5M BIPA biometric-privacy class-action settlement (IL) | Compliance/regulatory exposure | [ClassAction.org](https://www.classaction.org/news/nearly-4.5m-lightricks-settlement-resolves-lawsuit-over-alleged-biometric-privacy-violations) |

*No payment-orchestration-specific news (e.g. new PSP, orchestrator adoption) found in last 12 months.*

---

## S8 — Checkout Audit (web — facetuneapp.com)

| Attribute | Finding | Source |
|-----------|---------|--------|
| Checkout type | Direct web subscription via facetuneapp.com (My Account portal); subscriptions from $25/mo, monthly/quarterly/annual | [Facetune Pricing](https://www.facetuneapp.com/pricing); [Refund Policy](https://static.lightricks.com/legal/refund-policy.html) |
| Guest checkout | Requires account/login (My Account email) | [Lightricks Help](https://lightricks.zendesk.com/hc/en-us/articles/6096750327570-How-Do-I-Cancel-A-Subscription-Or-Free-Trial) |
| Steps | Not fully verifiable from public pages — **Not found** (checkout gated) | — |
| 3DS / SCA | **Not verified** (Adyen/Stripe both support 3DS2; not confirmed live for Lightricks) | — |
| Mobile | Primary paying channel is mobile IAP (Apple/Google); web is secondary | [Google Play](https://play.google.com/store/apps/details?id=com.lightricks.facetune.free) |
| APM logic / localization | Currency billed "in accordance with Customer's location"; payment methods limited to those supported by Stripe/Adyen/PayPal | [Terms of Use](https://static.lightricks.com/legal/terms-of-use.html) |
| Refund window | 14-day cooling-off full refund on web purchases; App Store purchases governed by Apple/Google | [Refund Policy](https://static.lightricks.com/legal/refund-policy.html) |

---

## S9 — PCI DSS
Lightricks' own refund policy states that **"Stripe, Adyen and PayPal are PCI compliant service providers,"** delegating card-data PCI scope to its PSPs ([Refund Policy](https://static.lightricks.com/legal/refund-policy.html)). No independent Lightricks PCI DSS attestation/AoC was found publicly — **No public information found** on Lightricks' own certification level.

---

## S10 — Strategic Insights

**1. Three PSPs, no orchestrator = in-house plumbing tax**
- **Evidence:** Web checkout explicitly runs Stripe + Adyen + PayPal in parallel, with no public orchestration layer ([Refund Policy](https://static.lightricks.com/legal/refund-policy.html)).
- **Pain Point:** Engineers (now scarcer post-layoffs, ~100 staff on Facetune) maintain three separate PSP integrations, routing logic, and reconciliation by hand.
- **Yuno Value Prop:** One API replaces three integrations — unify Stripe/Adyen/PayPal under smart routing, failover, and retries; free engineering for the AI pivot.
- **Best Case:** **Rappi** — consolidated a fragmented multi-PSP stack onto Yuno's single API.
- **Outreach Angle:** "You already run three PSPs on web — Yuno gives you the routing + failover layer on top, without three sets of code to maintain after the split."

**2. IAP fee burden + corporate split = web-billing margin imperative**
- **Evidence:** Lightricks explicitly offers web purchase to avoid Apple/Google commission; Facetune is now a standalone, margin-focused company ([Calcalist split](https://www.calcalistech.com/ctechnews/article/r1dgjt5gmg)).
- **Pain Point:** Every dollar pushed from 30% IAP to web is margin — but web conversion/approval rates make-or-break that math.
- **Yuno Value Prop:** Approval-rate uplift via intelligent retries + local APMs makes web billing convert better, accelerating the IAP-escape ROI.
- **Best Case:** **InDrive** — global consumer app that lifted approval rates and added local methods across emerging markets via Yuno.
- **Outreach Angle:** "Moving subscribers off Apple's 30% only pays off if web approval rates hold — that's exactly the lift Yuno delivers."

**3. LATAM/APAC/MENA traffic without confirmed local APMs**
- **Evidence:** Brazil 4.4% + India 10.8% of lightricks.com traffic; web methods limited to Stripe/Adyen/PayPal-supported, with Pix/UPI/OXXO unverified ([Similarweb](https://www.similarweb.com/website/lightricks.com/); [Refund Policy](https://static.lightricks.com/legal/refund-policy.html)).
- **Pain Point:** Card-only web checkout leaves emerging-market conversion on the table (Pix ~30%+ of Brazil online payments; UPI dominant in India).
- **Yuno Value Prop:** 1,000+ methods across 200+ countries — add Pix, UPI, OXXO, regional wallets through the same single integration.
- **Best Case:** **Rappi / Livelo** — LATAM consumer leaders using Yuno to unlock Pix/local-method coverage.
- **Outreach Angle:** "Brazil and India are top-5 web markets for you — are Pix and UPI live, or are you still card-only there?"

**4. Subscription-lifecycle complaints (trial, dunning, refunds, shadow subs)**
- **Evidence:** 1.4★ Trustpilot, 350+ billing complaints; "shadow subscription" + failed-cancellation patterns ([Trustpilot](https://www.trustpilot.com/review/facetuneapp.com); [Pine AI](https://www.19pine.ai/cancel-subscription/newspaper-magazine-and-online-learning/how-to-cancel-facetune)).
- **Pain Point:** Fragmented billing across PSPs + IAP creates reconciliation gaps, involuntary churn, and chargeback/refund risk that damages brand.
- **Yuno Value Prop:** Unified subscription + dunning + smart-retry layer reduces involuntary churn and gives one transparent view of every charge across channels.
- **Best Case:** **Reserva** — used Yuno to streamline checkout and reduce payment failures.
- **Outreach Angle:** "Your Facetune reviews are dominated by billing disputes — a unified retry + lifecycle layer cuts the involuntary churn and chargebacks driving those."

**5. New LTX-2 API/licensing = a fresh B2B payments surface**
- **Evidence:** LTX-2 API + commercial model licensing generating tens of $M annualized from Fortune 500 ([PR Newswire](https://www.prnewswire.com/news-releases/lightricks-releases-ltx-2-the-first-complete-open-source-ai-video-foundation-model-302593012.html)).
- **Pain Point:** B2B/usage-based API billing has different needs (invoicing, multi-currency, large-ticket cards/bank transfer) than consumer subscriptions.
- **Yuno Value Prop:** One orchestration layer spans both consumer subscriptions and B2B/API monetization — multi-currency acceptance, fallback, reconciliation in one place.
- **Best Case:** **InDrive** — scaling payments across diverse flows/geographies on one platform.
- **Outreach Angle:** "As LTX monetizes via API to enterprise clients, you'll want acceptance + multi-currency that your consumer stack already needs — one layer covers both."

---

## S11 — Pipeline / Competitive Mapping

| Company | Type | Signals | Score |
|---------|------|---------|-------|
| **Lightricks (Facetune)** | Target | Multi-PSP no orchestrator; IAP-fee escape; LATAM/APAC traffic; billing complaints; standalone consumer co | 🔴 **High (13)** |
| Picsart | Direct competitor (creative app, subs) | Global consumer subscriptions, IAP + web | 🔴 High (12) [INFERENCE — payment stack not verified] |
| Meitu | Direct competitor (beauty/photo, freemium) | Global consumer subs, APAC-heavy | 🟡 Med (9) |
| VSCO | Direct competitor (photo subs) | Subscription app, web + IAP | 🟡 Med (8) |
| Photoroom | Direct competitor (AI photo, subs) | Subscription SaaS + app | 🟡 Med (8) |
| Prequel | Direct competitor (creative app) | Subscription app | 🟢 Low (6) |
| Canva | Industry peer (design SaaS) | Large-scale web subs, global | 🟡 Med (10) [INFERENCE] |
| Adobe (Express/Lightroom) | Industry peer | Enterprise-scale own payments | 🟢 Low (5) [likely too large/in-house] |
| Runway / Reface / Bending Spoons | Industry peers (named Lightricks competitors per CB Insights) | AI-creative subscription apps | 🟡 Med (8) |

*Scores reflect Yuno-fit (multi-PSP/orchestrator gap + cross-border subscription volume), not company size. Competitor stacks flagged [INFERENCE] where not source-verified.*

---

## S12 — Business Case Inputs

| Input | Value | Basis / Source |
|-------|-------|----------------|
| App-business revenue | ~$300M/yr (growing ~20%) | [Startup Fortune](https://startupfortune.com/lightricks-splits-itself-in-two-as-ai-costs-force-a-reset/) |
| ARR milestone | $250M ARR (Jul 2025, +46% YoY) | [Shavit Capital](https://www.shavitcapital.com/the-250-million-arr-club-israels-most-lucrative-tech-startups/) |
| Monthly paying users | 6.6M+ | [Wikipedia](https://en.wikipedia.org/wiki/Lightricks) |
| Avg revenue per paying user | ~$45/yr (≈ $300M ÷ 6.6M) [INFERENCE — derived] | derived from above |
| Est. annual subscription txns | ~6.6M–13M+ (single + multi-period renewals across 6.6M payers) [INFERENCE — derived] | derived |
| Currency | Multi-currency, billed to customer location | [Terms of Use](https://static.lightricks.com/legal/terms-of-use.html) |
| Top 3 web markets | United States, India, Brazil (lightricks.com) / US, India, UK (facetune) | [Similarweb](https://www.similarweb.com/website/lightricks.com/) |

*Caveat: the majority of paying volume flows through Apple/Google IAP (outside Yuno's web-orchestration scope today); the addressable wedge is the growing direct-web channel + LTX-2 B2B API billing.*

---

## S13 — Outreach

### 13A — LinkedIn (≤300 words)
Hi [Name] — congrats on the LTX-2 launch and the Facetune/LTX restructuring; focusing the consumer business as its own company is a smart move.

A quick observation from the payments side: Facetune's web checkout already runs Stripe, Adyen and PayPal in parallel. Running three PSPs is the right instinct for resilience — but maintaining three integrations, routing logic and reconciliation in-house is a real engineering tax, especially as the team focuses headcount on the AI roadmap.

That's the gap Yuno fills. We're a single API that sits on top of your existing PSPs — Stripe, Adyen, PayPal and 1,000+ payment methods across 200+ countries — and adds the routing, automatic failover and smart retries layer you'd otherwise build yourself. The result is higher approval rates (which is what actually makes the move off Apple's 30% IAP pay off) without three sets of code to maintain.

Two things I'd love to compare notes on: (1) whether Pix and UPI are live on your web checkout — Brazil and India are both top-5 web markets for Lightricks, and card-only leaves real conversion on the table there; and (2) how you're thinking about billing for the new LTX-2 API as it scales with enterprise clients.

Worth a 20-minute call? Happy to walk through how peers like InDrive and Rappi consolidated multi-PSP stacks and lifted approval rates on Yuno.

Best, [Your name], Yuno

---

### 13B — Cold Email

**Subject:** Three PSPs on Facetune's checkout — one layer to run them

Hi [Name],

Congrats on the LTX-2 launch and on spinning Facetune into its own focused consumer company.

I noticed Facetune's web checkout already runs **Stripe, Adyen and PayPal** side by side. That's the right call for resilience — but it also means your team maintains three separate integrations, routing rules and reconciliation in-house, right as headcount is being prioritized for the AI roadmap.

Yuno is a single API that sits *on top of* your existing PSPs. You keep Stripe, Adyen and PayPal — we add the orchestration layer: smart routing, automatic failover, and retry logic that lifts approval rates. That uplift is exactly what makes shifting subscribers off Apple/Google's 30% IAP to web actually pay off, instead of trading a fee for a conversion drop.

Two quick questions:
1. Are **Pix (Brazil)** and **UPI (India)** live on your web checkout today? Both are top-5 web markets for Lightricks, and card-only typically leaves meaningful conversion on the table there — Yuno adds 1,000+ local methods across 200+ countries through the same integration.
2. As **LTX-2's API** scales with enterprise clients, how are you handling multi-currency B2B billing? One orchestration layer can cover both your consumer subscriptions and the new API revenue.

Companies like **InDrive** and **Rappi** used Yuno to consolidate multi-PSP stacks and raise approval rates across emerging markets. Open to a 20-minute call next week?

Best,
[Your name] | Yuno

*(All claims above are restricted to source-verified findings; no unconfirmed APM availability is asserted — Pix/UPI are posed as questions, not stated facts.)*

---

## Appendix — Source URLs
- Lightricks Wikipedia: https://en.wikipedia.org/wiki/Lightricks
- Refund & Cancellation Policy (PSPs named): https://static.lightricks.com/legal/refund-policy.html
- Terms of Use (Adyen / Apple Pay / Google Pay): https://static.lightricks.com/legal/terms-of-use.html
- Lightricks Help — unfamiliar charge / descriptor: https://lightricks.zendesk.com/hc/en-us/articles/12524222810386-Learn-about-an-unfamiliar-charge
- Lightricks Help — cancel subscription/trial: https://lightricks.zendesk.com/hc/en-us/articles/6096750327570-How-Do-I-Cancel-A-Subscription-Or-Free-Trial
- Lightricks Help — request a refund: https://lightricks.zendesk.com/hc/en-us/articles/5988128741906-How-do-I-request-a-refund
- Facetune FAQ: https://www.facetuneapp.com/faq
- Facetune Pricing: https://www.facetuneapp.com/pricing
- Similarweb lightricks.com: https://www.similarweb.com/website/lightricks.com/
- Similarweb facetuneapp.com: https://www.similarweb.com/website/facetuneapp.com/
- Companies House (Lightricks UK Ltd, 11444887): https://find-and-update.company-information.service.gov.uk/company/11444887/officers
- Craft.co locations: https://craft.co/lightricks/locations
- Series D / $1.8B valuation (TechRound): https://techround.co.uk/news/lightricks-valued-1-8-billion-funding-round/
- Series D (FinSMEs): https://www.finsmes.com/2021/09/130-million-series-d-round-lifts-valuation-of-lightricks-to-1-8-billion.html
- Company split + 75 layoffs (Calcalist): https://www.calcalistech.com/ctechnews/article/r1dgjt5gmg
- Split context (Startup Fortune): https://startupfortune.com/lightricks-splits-itself-in-two-as-ai-costs-force-a-reset/
- $250M ARR club (Shavit Capital): https://www.shavitcapital.com/the-250-million-arr-club-israels-most-lucrative-tech-startups/
- LTX-2 launch (PR Newswire): https://www.prnewswire.com/news-releases/lightricks-releases-ltx-2-the-first-complete-open-source-ai-video-foundation-model-302593012.html
- LTX-2 open-source (GlobeNewswire): https://www.globenewswire.com/news-release/2026/01/06/3213304/0/en/Lightricks-Open-Sources-LTX-2-the-First-Production-Ready-Audio-and-Video-Generation-Model-With-Truly-Open-Weights.html
- BIPA settlement (ClassAction.org): https://www.classaction.org/news/nearly-4.5m-lightricks-settlement-resolves-lawsuit-over-alleged-biometric-privacy-violations
- Trustpilot (facetuneapp.com): https://www.trustpilot.com/review/facetuneapp.com
- PissedConsumer (Facetune): https://facetune.pissedconsumer.com/review.html
- Pine AI (cancellation/shadow subs): https://www.19pine.ai/cancel-subscription/newspaper-magazine-and-online-learning/how-to-cancel-facetune
- Apple Community (Facetune scam thread): https://discussions.apple.com/thread/254785711
- Sikayetvar (trial→charge complaint): https://www.sikayetvar.com/en/facetune-2-us/facetune-charged-me-after-trial-without-notice-requesting-refund
- Google Play (Facetune): https://play.google.com/store/apps/details?id=com.lightricks.facetune.free
- CB Insights competitors: https://www.cbinsights.com/company/lightricks-ltd/alternatives-competitors
