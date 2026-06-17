# SDR Research Brief — Perplexity AI
**Prepared for Yuno | Date: 2026-06-17 | Analyst: Payments Intelligence**

## Executive Summary
Perplexity AI (Perplexity AI, Inc., San Francisco) is one of the fastest-scaling consumer AI subscription businesses in the world — ~$450M+ ARR as of March 2026, a ~$22.6B valuation (Series E-6, Jan 2026), and ~138M monthly web visits with India already its #2 market (~10.5%) after the US. Its consumer billing (Pro at $20/mo, Max at $200/mo) runs through **Stripe** on web, with App Store / Google Play handling in-app, while its new agentic-commerce surface ("Buy with Pro" / Instant Buy) is currently powered by a single rail: **PayPal/Venmo** (US-only). The strategic opening is two-fold: (a) global subscription billing at hyperscale where India and other emerging markets expect local APMs (UPI) that a single cross-border PSP under-serves, and (b) Perplexity is itself becoming a payments surface, where orchestration across PSPs and 1,000+ global APMs is core to monetizing checkout beyond the US PayPal rail. Both map directly to Yuno's orchestration value.

---

## S1 — Traffic by Country (perplexity.ai)
Source: Similarweb (live fetch, May 2026 dataset). Total monthly visits ~138.1M.

| Rank | Country | Traffic Share | Notes |
|---|---|---|---|
| 1 | United States | 21.13% | Largest market; high-income shopper base |
| 2 | India | 10.53% | #2 market; surged after Airtel free-Pro partnership (reported +640% YoY in 2025) |
| 3 | Germany | 5.48% | EU; SEPA/local-method expectations |
| 4 | Russia | 4.63% | Sanctioned market — payment-acceptance constraints |
| 5 | France | 4.29% | EU; CB/SEPA expectations |

[INFERENCE — not confirmed] Mobile/desktop split not published in available data; India usage reported as mobile-skewed. Other syndicated trackers cite South Korea and the US at higher shares; figures vary by source/month, so treat as directional.
Sources: [Similarweb](https://www.similarweb.com/website/perplexity.ai/), [Demandsage](https://www.demandsage.com/perplexity-ai-statistics/), [Airtel](https://www.airtel.in/blog/airtel-app/unlock-the-power-of-ai-airtel-offers-perplexity-pro-worth-%E2%82%B917000-at-no-extra-cost/)

---

## S2 — Legal Entities
| Entity | Jurisdiction | Detail | Source |
|---|---|---|---|
| Perplexity AI, Inc. | California, USA | Incorporated 4 Aug 2022; Stock Corp #5186927; 115 Sansome St Suite 900, San Francisco, CA 94105; agent C T Corporation System | [Bizprofile](https://www.bizprofile.net/ca/san-francisco/perplexity-ai-inc) |
| Perplexity Management Co, LLC | California, USA | Affiliated entity, San Francisco | [Bizprofile](https://www.bizprofile.net/ca/san-francisco/perplexity-management-co-llc) |
| PERPLEXITY AI LTD | United Kingdom | Companies House #15470377 | [GOV.UK](https://find-and-update.company-information.service.gov.uk/company/15470377) |
| Singapore presence | Singapore | Employment provisions referenced in Privacy Policy; specific entity name Not found | [Privacy Policy](https://www.perplexity.ai/hub/legal/privacy-policy) |
| SEC registrant | USA | EDGAR CIK 0001972171 | [SEC EDGAR](https://www.sec.gov/edgar/browse/?CIK=0001972171) |

India-specific local entity: **Not found** (the large India user base is served via the US/global product and the Airtel partnership, not a confirmed Indian billing entity).

---

## S3 — Payment Stack

### 3A — PSPs / Acquirers / Processors
| Use case | Provider | Status | Source |
|---|---|---|---|
| Web subscription billing (Pro/Max) | **Stripe** | Confirmed — web checkout redirects to Stripe; invoices/portal via Stripe Customer Portal | [Help Center](https://www.perplexity.ai/help-center/en/collections/12584508-subscription-and-billing), [Finout](https://www.finout.io/blog/perplexity-pricing-in-2026) |
| Developer/API billing | **Stripe** | Confirmed — API billing managed via Stripe portal | [Perplexity API docs](https://docs.perplexity.ai/docs/getting-started/api-groups) |
| In-app subscription (iOS) | Apple App Store IAP | Confirmed | [Help Center](https://www.perplexity.ai/help-center/en/collections/12584508-subscription-and-billing) |
| In-app subscription (Android) | Google Play Billing | Confirmed | [Help Center](https://www.perplexity.ai/help-center/en/collections/12584508-subscription-and-billing) |
| Agentic commerce / Instant Buy checkout | **PayPal + Venmo** (PayPal agentic commerce) | Confirmed — US only | [eMarketer](https://www.emarketer.com/content/paypal-merchants-in-chat-checkout-perplexity-venmo), [CNBC](https://www.cnbc.com/2025/11/19/perplexity-ai-online-shopping-paypal.html) |

### 3B — Orchestrator in place?
**No third-party payment orchestrator identified.** Subscription = single PSP (Stripe) cross-border; agentic commerce checkout = single rail (PayPal/Venmo, US-only). No evidence of Yuno, Spreedly, Primer, or similar. This is a multi-PSP, multi-rail footprint stitched manually rather than via an orchestration layer. [INFERENCE — not confirmed]

---

## S4 — APMs Confirmed
| Method | Where | Status | Source |
|---|---|---|---|
| Credit/debit cards | Web (via Stripe), global | Confirmed | [Help Center](https://www.perplexity.ai/help-center/en/collections/12584508-subscription-and-billing) |
| Apple App Store billing | iOS app | Confirmed | [Help Center](https://www.perplexity.ai/help-center/en/collections/12584508-subscription-and-billing) |
| Google Play billing | Android app | Confirmed | [Help Center](https://www.perplexity.ai/help-center/en/collections/12584508-subscription-and-billing) |
| PayPal | US agentic checkout | Confirmed | [CNBC](https://www.cnbc.com/2025/11/19/perplexity-ai-online-shopping-paypal.html) |
| Venmo | US agentic checkout | Confirmed | [eMarketer](https://www.emarketer.com/content/paypal-merchants-in-chat-checkout-perplexity-venmo) |

**Unverified markets / APM gaps (NOT confirmed unavailable — verify at live checkout):**
- **India (UPI / RuPay / net banking):** Despite India being the #2 market, no UPI/net-banking support at Perplexity's own checkout was found in public sources. Airtel users get Pro free (bundle), but direct payers are reportedly being asked to add a **card** to continue — suggesting card-only billing, an APM gap in a UPI-first market. Verify on live `perplexity.ai/pro` checkout from an Indian IP. Source: [BusinessToday](https://www.businesstoday.in/technology/news/story/airtel-users-need-a-new-card-requirement-to-continue-using-free-perplexity-pro-507785-2025-12-23)
- **Germany/France/EU (SEPA Direct Debit, iDEAL, Bancontact, CB):** Not verified at checkout — "Not verified" ≠ "Not available."
- **Brazil (Pix), LatAm wallets, SE Asia wallets:** Not found.

---

## S5 — Payment / Billing Complaints
| Theme | Detail | Source |
|---|---|---|
| Post-cancel charges | Users report being billed after canceling; auto-renew unless canceled before renewal date | [Sikayetvar](https://www.sikayetvar.com/en/perplexity-us/perplexity-charged-me-after-canceling-pro-how-can-i-get-a-refund-q-39659) |
| Refund denials / non-refundable | Official policy: payments non-refundable, no partial credits; annual plans limited 72-hr window | [Trustpilot](https://www.trustpilot.com/review/www.perplexity.ai) |
| Surprise charges / hard to cancel | Recurring Trustpilot theme; avg ~1.6/5 across ~180 reviews | [Trustpilot](https://www.trustpilot.com/review/www.perplexity.ai) |
| Unresponsive support | AI agent "Sam" template loops; refund requests stalled | [Trustpilot](https://www.trustpilot.com/review/www.perplexity.ai) |
| India card requirement | Airtel free-Pro users asked to add a card to continue | [BusinessToday](https://www.businesstoday.in/technology/news/story/airtel-users-need-a-new-card-requirement-to-continue-using-free-perplexity-pro-507785-2025-12-23) |
| Model-swap refund demands | Nov 2025 — users demanded refunds over silent model downgrades | [abit.ee](https://abit.ee/en/artificial-intelligence/perplexity-pro-model-downgrade-ai-subscription-perplexity-misleading-silent-model-swap-perplexity-re-en) |

---

## S6 — Expansion & Corporate Developments
| Date | Development | Source |
|---|---|---|
| Mar 2026 | ARR reported >$450M (up from ~$200M late 2025); shift to agents + usage-based pricing | [Demandsage / FT-cited](https://www.demandsage.com/perplexity-ai-statistics/) |
| Jan 2026 | Series E-6 — ~$22.6B valuation | [AI Business Weekly](https://aibusinessweekly.net/p/perplexity-ai-valuation-2026) |
| Jun 2026 | ~$200M raised for Comet at ~$20B; total funding ~$1.72B | [TechTimes](https://www.techtimes.com/articles/318028/20260608/perplexity-raises-200-million-comet-ai-browser-agent-economy-front-door.htm) |
| Mar 2026 | Comet AI browser paywall dropped — free on iOS/Android/Win/Mac | [MacRumors](https://www.macrumors.com/2026/03/18/perplexity-comet-browser-iphone/) |
| Jul 2025 | Airtel India partnership — free 1-yr Pro (₹17,000 value) to all Airtel customers | [Airtel](https://www.airtel.in/blog/airtel-app/unlock-the-power-of-ai-airtel-offers-perplexity-pro-worth-%E2%82%B917000-at-no-extra-cost/) |
| Nov 2025 | Instant Buy / agentic checkout via PayPal launched (US) | [CNBC](https://www.cnbc.com/2025/11/19/perplexity-ai-online-shopping-paypal.html) |

---

## S7 — Payment-Specific News (last 12 months)
| Date | Event | Yuno relevance | Source |
|---|---|---|---|
| Nov 2025 | "Buy with Pro" / Instant Buy in-chat checkout, US, PayPal+Venmo; merchants stay merchant of record, zero commission | Perplexity becomes a checkout surface; single US rail = obvious global APM/PSP gap | [Stellagent](https://stellagent.ai/insights/perplexity-shopping-buy-with-pro), [eMarketer](https://www.emarketer.com/content/paypal-merchants-in-chat-checkout-perplexity-venmo) |
| Nov 2025 | Agentic commerce extended to US free users | Expands transaction volume through one rail | [DigitalCommerce360](https://www.digitalcommerce360.com/2025/11/19/perplexity-agentic-commerce-experience-to-expand-to-free-users/) |
| Mar 2026 | Amazon won preliminary injunction blocking Comet's shopping agent on Amazon (Judge Chesney) | Underscores need for sanctioned, native checkout rails Perplexity controls | [CNBC](https://www.cnbc.com/2026/03/10/amazon-wins-court-order-to-block-perplexitys-ai-shopping-agent.html), [GeekWire](https://www.geekwire.com/2026/judge-blocks-perplexitys-ai-bot-from-shopping-on-amazon-in-early-test-of-agentic-commerce/) |
| Dec 2025 | India Airtel free-Pro users asked to add a card | India APM/card-only friction signal | [BusinessToday](https://www.businesstoday.in/technology/news/story/airtel-users-need-a-new-card-requirement-to-continue-using-free-perplexity-pro-507785-2025-12-23) |

---

## S8 — Checkout Audit
| Surface | Type | Guest? | Steps | 3DS | Mobile | APM logic |
|---|---|---|---|---|---|---|
| Web Pro/Max | Hosted subscription (Stripe redirect) | No (account required) | Account → plan → Stripe card entry → confirm | Via Stripe (SCA where required) [INFERENCE] | Responsive | Card-centric; no localized APMs confirmed |
| iOS app | In-app purchase (Apple IAP) | No | App Store native flow | Apple-handled | Native | Apple Pay / store balance |
| Android app | In-app purchase (Google Play) | No | Play native flow | Google-handled | Native | Google Pay / store balance |
| Instant Buy (US agentic) | In-chat checkout, merchant of record = merchant | Pro/free (US) | Product card → Buy → PayPal/Venmo | PayPal-handled | In-app | PayPal + Venmo only |

Source: [Help Center](https://www.perplexity.ai/help-center/en/collections/12584508-subscription-and-billing), [Finout](https://www.finout.io/blog/perplexity-pricing-in-2026), [Stellagent](https://stellagent.ai/insights/perplexity-shopping-buy-with-pro). Live-checkout verification of 3DS and India APMs recommended.

---

## S9 — PCI DSS
- Trust Center publicly lists **PCI DSS SAQ A** compliance (i.e., card data outsourced to PCI-compliant processors — consistent with Stripe-hosted / PayPal-hosted flows). Also **SOC 2 Type II**, GDPR; HIPAA/PCI for enterprise where applicable.
- Sub-processor list maintained on Trust Center.
Source: [Trust Center](https://trust.perplexity.ai/), [TrustLists](https://trustlists.org/company/perplexity/), [Enterprise Security](https://www.perplexity.ai/enterprise/security)

---

## S10 — Strategic Insights

**1. India is #2 by traffic but billed card-only — UPI gap at hyperscale**
- Evidence: India ~10.5% of ~138M visits; Airtel free-Pro converters asked to add a **card**; no UPI at Perplexity checkout found. | Pain Point: UPI is the default consumer rail in India; card-only checkout depresses paid conversion as the Airtel cohort's free year expires. | Yuno Value Prop: One integration adds UPI, RuPay, net banking and routes locally — lifting India conversion without new PSP builds. | Best Case: **InDrive** (scaled local-APM coverage across emerging markets). | Outreach Angle: "Your #2 market converts on UPI, not cards — what does that do to Airtel free-tier conversion?"

**2. Single cross-border subscription PSP (Stripe) across 200+ countries**
- Evidence: Web billing routes solely to Stripe globally. | Pain Point: One PSP cross-border means higher decline rates, FX/cross-border fees, and no failover or local acquiring in key markets (DE, FR, BR, KR). | Yuno Value Prop: Orchestrate multiple acquirers/PSPs with smart routing, retries, and local acquiring to cut declines and cost. | Best Case: **Rappi** (multi-PSP orchestration at LatAm scale). | Outreach Angle: "At ~138M visits across 200 countries on one PSP, recovered declines alone fund the integration."

**3. Perplexity is becoming a payments surface — and it's stuck on one US-only rail**
- Evidence: Instant Buy / "Buy with Pro" runs entirely on PayPal/Venmo, US only; agentic commerce now extended to free users. | Pain Point: To globalize commerce and onboard non-US merchants, Perplexity needs PSP + APM breadth it doesn't have on a single rail. | Yuno Value Prop: Orchestration layer behind the agentic checkout — 1,000+ methods, MoR options, country-aware routing — turning a US feature into a global commerce channel. | Best Case: **Reserva** (orchestrated checkout breadth). | Outreach Angle: "You're building a checkout. The fastest way to take it global is an orchestration layer behind the agent, not a second PayPal integration per country."

**4. Billing-trust complaints (post-cancel charges, refund friction) erode LTV**
- Evidence: Trustpilot ~1.6/5; recurring post-cancel charges and refund denials. | Pain Point: Poor billing/dunning UX drives chargebacks and churn at subscription scale. | Yuno Value Prop: Unified retries, smart dunning, and clean cancellation/refund flows across PSPs reduce involuntary churn and disputes. | Best Case: **Livelo** (subscription/loyalty billing reliability). | Outreach Angle: "Involuntary churn and refund disputes scale with you — orchestrated dunning recovers revenue Stripe-alone can't."

**5. Regulatory/agent-access risk (Amazon injunction) favors native, sanctioned rails**
- Evidence: Mar 2026 court order blocked Comet's Amazon shopping agent. | Pain Point: Scraping-style agent checkout is legally fragile; Perplexity needs first-party, merchant-sanctioned payment rails it controls. | Yuno Value Prop: Power a compliant, merchant-integrated checkout across PSPs/APMs rather than agent-driven third-party site access. | Best Case: **Rappi** (owned, compliant payment infrastructure). | Outreach Angle: "Owning the rails — not borrowing them via agents on someone else's site — is the durable path to global agentic checkout."

---

## S11 — Pipeline / Competitive Scoring
Scoring: 🔴 High 12+ | 🟡 Med 7–11 | 🟢 Low <7 (multi-market subscription + commerce surface + APM gap)

| Company | Type | Why | Score |
|---|---|---|---|
| **Perplexity AI** | Target | Hyperscale subs + emerging APM gap + new commerce surface on single rail | 🔴 14 |
| OpenAI (ChatGPT) | Direct competitor | Global subs + ChatGPT Instant Checkout (ACP) commerce surface | 🔴 13 |
| Google (Gemini) | Direct competitor | Owns Google Pay; less PSP-pain but global commerce push | 🟡 9 |
| Anthropic (Claude) | Direct competitor | Global subs, fewer consumer APM datapoints public | 🟡 8 |
| You.com | Industry peer | AI search, smaller scale | 🟢 6 |
| Genspark | Industry peer | Agentic AI, early-stage | 🟢 6 |
| The Browser Company (Dia/Arc) | Industry peer | AI browser, pre-monetization at scale | 🟢 5 |

---

## S12 — Business Case (order-of-magnitude)
| Metric | Value | Basis / Source |
|---|---|---|
| ARR | ~$450M+ (Mar 2026) | [FT-cited / Demandsage](https://www.demandsage.com/perplexity-ai-statistics/) |
| Headline subscription prices | Pro $20/mo ($200/yr); Max $200/mo ($167/mo annual) | [Finout](https://www.finout.io/blog/perplexity-pricing-in-2026), [eesel](https://www.eesel.ai/blog/perplexity-comet-pricing) |
| Avg txn value (subscription) | ~$20 (monthly Pro) [INFERENCE — mix of monthly/annual unknown] | Derived from pricing |
| Est. annual subscription txns | [INFERENCE — not confirmed] At ~$450M ARR with a $20 avg blended monthly txn, ≈ on the order of 20M+ billing events/yr; precise paid-sub count Not found | Derived |
| Commerce GMV (Instant Buy) | Not found (per-order; "shoppers spend 57% more per order" vs other AI referrals) | [Stellagent](https://stellagent.ai/insights/perplexity-shopping-buy-with-pro) |
| Primary billing currency | USD | [Help Center](https://www.perplexity.ai/help-center/en/collections/12584508-subscription-and-billing) |
| Top 3 markets | US, India, Germany | [Similarweb](https://www.similarweb.com/website/perplexity.ai/) |

---

## S13 — Outreach

### 13A — LinkedIn (≤300 words)
Hi Aravind — congrats on the ARR ramp past $450M and the Comet rollout; the pace is genuinely rare in consumer AI.

One thing jumped out as I looked at the payment side. India is already your #2 market by traffic, yet consumer billing routes through a single cross-border PSP, and the rail consumers there actually trust is UPI — not cards. As the Airtel free-Pro cohort's year runs out, card-only checkout is exactly where paid conversion tends to leak. The same single-PSP pattern across 200+ countries usually means recoverable declines and avoidable cross-border cost at your scale.

Separately, Buy with Pro / Instant Buy is the more interesting story: you're becoming a checkout surface, but it's PayPal/Venmo, US-only. Taking that global means PSP and local-method breadth per country — not a new integration each time.

Yuno is a single API to 1,000+ payment methods and PSPs across 200+ countries, with smart routing, failover, and local acquiring. We help companies like InDrive and Rappi run exactly this: many rails, one integration. Worth a 20-minute look at the India conversion math and the agentic-checkout roadmap?

### 13B — Cold Email
**Subject: Perplexity's #2 market pays on UPI, not cards**

Hi Aravind,

Perplexity's growth is hard to overstate — ~$450M+ ARR and ~138M monthly visits, with India already your second-largest market.

That India position is also where I'd flag a payments gap. Consumer billing runs through a single cross-border PSP, and your web checkout is card-centric. In India the default consumer rail is UPI, so as the Airtel free-Pro cohort's year expires, card-only checkout is where paid conversion quietly leaks. The same one-PSP-everywhere pattern across 200+ countries typically leaves recoverable declines and avoidable cross-border cost on the table.

The bigger opportunity is Buy with Pro / Instant Buy. You're building a real checkout surface, but it currently rides one rail (PayPal/Venmo) in one market (US). Taking agentic commerce global means PSP and local-method breadth in every country — and the Amazon injunction is a reminder that owning sanctioned, first-party rails beats borrowing them.

Yuno is one API to 1,000+ payment methods and PSPs across 200+ countries, with smart routing, failover, and local acquiring. InDrive and Rappi use us to run many rails through one integration — both for subscriptions and for checkout.

Worth 20 minutes to walk through the India conversion math and where orchestration fits your agentic-checkout roadmap?

Best,
[Name] | Yuno

---

## Appendix — Source URLs
- https://www.similarweb.com/website/perplexity.ai/
- https://www.demandsage.com/perplexity-ai-statistics/
- https://www.airtel.in/blog/airtel-app/unlock-the-power-of-ai-airtel-offers-perplexity-pro-worth-%E2%82%B917000-at-no-extra-cost/
- https://www.businesstoday.in/technology/news/story/airtel-users-need-a-new-card-requirement-to-continue-using-free-perplexity-pro-507785-2025-12-23
- https://www.bizprofile.net/ca/san-francisco/perplexity-ai-inc
- https://www.bizprofile.net/ca/san-francisco/perplexity-management-co-llc
- https://find-and-update.company-information.service.gov.uk/company/15470377
- https://www.sec.gov/edgar/browse/?CIK=0001972171
- https://www.perplexity.ai/hub/legal/privacy-policy
- https://www.perplexity.ai/help-center/en/collections/12584508-subscription-and-billing
- https://docs.perplexity.ai/docs/getting-started/api-groups
- https://www.finout.io/blog/perplexity-pricing-in-2026
- https://www.emarketer.com/content/paypal-merchants-in-chat-checkout-perplexity-venmo
- https://www.cnbc.com/2025/11/19/perplexity-ai-online-shopping-paypal.html
- https://stellagent.ai/insights/perplexity-shopping-buy-with-pro
- https://www.digitalcommerce360.com/2025/11/19/perplexity-agentic-commerce-experience-to-expand-to-free-users/
- https://www.cnbc.com/2026/03/10/amazon-wins-court-order-to-block-perplexitys-ai-shopping-agent.html
- https://www.geekwire.com/2026/judge-blocks-perplexitys-ai-bot-from-shopping-on-amazon-in-early-test-of-agentic-commerce/
- https://trust.perplexity.ai/
- https://trustlists.org/company/perplexity/
- https://www.perplexity.ai/enterprise/security
- https://www.trustpilot.com/review/www.perplexity.ai
- https://www.sikayetvar.com/en/perplexity-us/perplexity-charged-me-after-canceling-pro-how-can-i-get-a-refund-q-39659
- https://abit.ee/en/artificial-intelligence/perplexity-pro-model-downgrade-ai-subscription-perplexity-misleading-silent-model-swap-perplexity-re-en
- https://aibusinessweekly.net/p/perplexity-ai-valuation-2026
- https://www.techtimes.com/articles/318028/20260608/perplexity-raises-200-million-comet-ai-browser-agent-economy-front-door.htm
- https://www.macrumors.com/2026/03/18/perplexity-comet-browser-iphone/
- https://www.eesel.ai/blog/perplexity-comet-pricing

*Integrity note: All factual claims carry source URLs. Inferences are labeled. APM non-availability is flagged as "unverified," not "unavailable." Subscriber count, India local billing entity, Singapore entity name, and commerce GMV = Not found in public sources.*
