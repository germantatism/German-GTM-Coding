# Prompt Claude Design: New Yango deck, mirroring the Suno success-cases deck (2026-08-16)

⚠️ **Start from a DUPLICATE of the Suno deck, never edit it in place.** Source design system: the Suno deck (Google Slides file id `1hOUPZ7HAvDzT-2Y2Xw2-Tdr3J-gCWIHi`). Duplicate that file first, then build the Yango content in the copy. The Suno deck is live and in active use with a different prospect — it must not be touched.

Match the existing visual design system exactly (cover treatment, case-study card layout, stat boxes, section dividers, color, typography, appendix tables). Only the content below changes.

Audience: Javier Patiño (Yango Colombia) plus Yango HQ product/payments team, evaluating options by end of August 2026 for driver "recarga" (top-up) collection across Colombia, Peru, Bolivia and Venezuela. HQ already has a positive initial read on two vendors, Unlimit and Inswitch, but wants one option that covers all four countries. Dispersal (paying drivers) is already solved via Cobre's Fast Pay in Colombia.

---

## 1. Cover

Title: "Payment Infrastructure for Yango's Driver Economy in LatAm"
Subtitle: "One rail across Colombia, Peru, Bolivia and Venezuela"
Same date/CONFIDENTIAL treatment as the Suno cover.

---

## 2. "How Yango Handles Payments Today" (new slide, no direct equivalent in the Suno deck, build fresh in the same visual style as the deck's other architecture/explainer slides)

Diagram, left to right: Driver → [Recharge: fragmented, evaluating Unlimit/Inswitch, partially through Cobre in Colombia] → Available balance → Commission consumed per ride → Yango disperses earnings via Cobre Fast Pay (real-time) → Driver

Three callout boxes underneath (same style as the case-study "Pain Points" boxes):

**Dispersal is solved, collection isn't yet**
Cobre's Fast Pay already pays 120,000+ Yango drivers in Colombia in real time, down from delays that used to run up to 48 hours. The recharge side, how drivers fund that balance, is still being solved market by market.

**One-vendor evaluation, four-country need**
Unlimit and Inswitch have shown good results in initial testing, but neither has a public track record covering all four LatAm markets Yango operates in: Colombia, Peru, Bolivia, Venezuela.

**New instant-payment rails are moving faster than the roadmap**
Bre-B launched in Colombia in October 2025 and reached 34 million registered users within six months. Cobre already supports it for dispersal. Recurring, pull-style collection on Bre-B is still maturing, not yet confirmed at full production scale.

Footer: "Based on Yango's own account of its current setup and public reporting on the Cobre-Yango dispersal integration, August 2026."

---

## 3. The Opportunity (new slide, positioned right after the "today" slide)

Headline: "Yuno as a complement to Cobre, not a replacement"

Body: Yuno optimizes the collection side, how a recharge is accepted (card, PSE, Bre-B, wallets), routed by BIN, cost and approval rate to the best-performing method and provider. The money settles into the same Cobre account Yango already uses for driver dispersal, so fleets keep available balance without duplicating the 4x1000 tax or splitting funds across accounts.

Flow diagram: Driver recharges → Yuno processes the entry and routes to the best-performing method/provider → settles to Cobre's account → Cobre disperses to drivers (unchanged, already works)

Sub-note, smaller text: "Neither Unlimit nor Inswitch has public evidence of a ride-hailing driver-recharge use case specifically, or of confirmed coverage across all four target countries. Yuno's track record in this exact business model (drivers, fleets, multi-country LatAm) is the differentiator, not just another routing layer."

---

## 4. Case studies section

Use the SAME card layout as the Suno deck's case studies (Before Yuno / After Yuno / Impact / Pain Points). Include only these two, in this order, both are the real slides already built for other decks, reuse their content directly, do not alter the numbers:

**inDrive** — pull the existing inDrive case study content (the version that was in the Suno deck's source material before it was cut: single-PSP setup without resilience before, multi-PSP orchestration across 18 countries after, ~90% approval on key routes, ~29% fraud reduction, 11 new countries in 8 months). This is the most directly relevant case in the whole portfolio: same vertical (ride-hailing), same emerging-market profile, a close competitor to Yango.

**Rappi** — reuse as-is from the current Suno deck (in-house country-by-country orchestration before, centralized orchestration with Nova AI decline recovery after, +5pp authorization uplift, +8pp recovery uplift via Nova, >$1M annual savings, 9 countries live in months). Directly relevant: Rappi is a LatAm super-app with the same driver/courier-side payment shape as Yango.

Do NOT include Whop, Skool, or the Confidential Merchant slide from the Suno deck, none of them share Yango's business model (subscription billing vs. driver recharge/payout).

Optional third slide, only if there's room: GoFundMe, reused as-is, on the strength of its multi-processor marketplace-payout architecture (splits, beneficiary payouts, connected accounts) being structurally close to what Yango needs (collect from many, payout to many, on one ledger). If cut for space, no loss, inDrive and Rappi alone carry the argument.

---

## 5. Section: "Yuno + Cobre" (replaces the Suno deck's "Yuno vs. Stripe" section, same slide count and structure, different framing since Yango's incumbent is a set of point solutions plus Cobre, not a single global PSP like Stripe)

### 5.1 Divider slide
Title: "Yuno + Cobre"

### 5.2 "THE DECISION" (reuse the Suno version's structure, reword away from Stripe)
Title: "One vendor for every country, or the best rail per market"

Option 1, one vendor for everything:
- All recharge collection stays with a single vendor, in every market
- (+) One integration and one relationship to manage
- (−) Leaves approval and cost differences uncollected in every country a second rail would win
- (−) No live comparison: underperformance in any one country has no reference point
- (−) All recharge volume depends on one vendor's coverage and uptime across four very different markets

Option 2, the best rail per market:
- Each country and method routes to whichever rail measurably performs best, and switches if that changes
- (+) Maximizes approval and minimizes cost per country
- (+) Keeps vendors competing on live, comparable data
- (+) Extends automatically as Yango enters new markets, no new vendor negotiation each time
- (−) Needs routing and shared measurement

### 5.3 "When we run Yuno head-to-head" (reuse the Suno deck's abstracted pattern slide content, it is already anonymized and not Stripe-specific in its bullet text, only retitle it)
Title: "When we run Yuno head-to-head against a single-vendor setup, the pattern repeats"
Reuse the four bullets exactly as they appear in the Suno deck (Yuno wins outright in about a third of markets / bank approval favors Yuno in close to half / gaps close by over 80% within about a month / the advantage compounds on its own). No changes needed, the language is already generic.

### 5.4 Acceptance gap chart
Reuse the Suno deck's "The acceptance gap is measurable" LATAM/APAC chart as-is, it is aggregate portfolio data, not client-specific, and LATAM is directly relevant to all four target countries. Include only once (the Suno deck currently has this slide duplicated back to back, do not carry that duplication into the Yango deck).

---

## 6. Appendix

### 6.1 Divider + "Why we believe Yuno is the right partner for Yango"
Reuse the Suno deck's version, change "for Suno" to "for Yango" in the headline, keep the trusted-by line as-is (Uber, Qatar Airways, SpaceX, GoFundMe, Whop), keep "100% SaaS, pure API: Yuno never touches funds."

### 6.2 Pain point quotes
Reuse only these two from the Suno deck's set of seven, both map directly to what Yango needs (reliable, monitored payout infrastructure and consolidated visibility across markets):
- "Whenever a provider goes down, our teams have to be called in the middle of the night to manually resolve the issue and reroute the payments" — Chief Operations Officer, equipment manufacturer
- "We know there's revenue on the table, but without visibility into routing, costs, and failures, we're making decisions blind" — Head of Payments, digital marketplace

### 6.3 "What Yuno unlocks 1/2" and "2/2"
Reuse both tables exactly as they appear in the Suno deck, this content is generic to Yuno's orchestration model, not Suno-specific.

### 6.4 Compliance table
Reuse exactly as-is from the Suno deck (PCI DSS v4.0, SOC 2 Type 2, ISO 27001, ISO 27701, GDPR). No changes.

### 6.5 NEW: Country deep-dives (Colombia, Peru, Bolivia, Venezuela)

Replace whatever country appendix exists in the Suno deck with four new slides, one per country, in this order: Colombia, Peru, Bolivia, Venezuela. Same visual format as the Suno deck's per-country appendix slides (a payment-method table plus a short processor-landscape note). For each country, state plainly wherever noted that no public approval-rate or head-to-head performance data was found for any processor, do not imply a "best performer" ranking exists when it does not.

**Colombia**
Methods table (method / fit for frequent small-value driver top-ups):
- PSE: good, real-time, requires a redirect to the driver's own bank app each time
- Bre-B: promising, ~20 second settlement, 34M+ registered users within 6 months of its October 2025 launch, but recurring/pull collection at production scale is still maturing
- Nequi / Daviplata: very good, mobile-native, real-time, already used by Uber and DiDi in Colombia for a comparable flow
- Cards: weak, low card penetration among Colombia's population relative to LatAm peers
- Efecty / Baloto (cash): weak for this use case specifically, requires an in-person errand, poor fit when the driver needs to stay on the road

Processor note: "Most commonly used or vendor-recommended for these methods, not a verified performance ranking, no public approval-rate data exists for any of them." List: Wompi (Bancolombia, confirmed Bre-B support for dispersal), PayU (strongest for multi-country volume), ePayco (cash + PSE, SME-focused), dLocal (confirmed PSE and Nequi support).

**Peru**
Methods table:
- Yape + Plin: very good, interoperable since 2023, together over 50% of Peru's cashless transactions, matches the frequent small-value profile closely
- PagoEfectivo: weak for this use case, voucher-based, requires a physical cash step
- Cards: weak, Peru remains cash-heavy (47% of 2023 payment value was cash)

Processor note, same caveat as Colombia: Izipay (BCP-affiliated, strong Yape integration), Niubiz (ex-VisaNet, confirmed cards + Yape + Plin support), Culqi (Credicorp, confirmed Yape + Plin + PagoEfectivo support), dLocal (Yape confirmed, Plin not confirmed).

**Bolivia**
Methods table:
- QR Simple (central bank system): very good, interoperable across all banks, no fee, grew 48x in transaction value 2021-2024
- USDT/stablecoin: already in production use, Yango Food already uses this in Bolivia via Peso, driven by a dollar-liquidity shortage
- Cash: still dominant (64% of payments in 2025) but declining fast

Processor note: Peso (already integrated with Yango Food, the only vendor with a confirmed relationship to Yango specifically), Red Enlace (the interbank switch behind QR Simple), Tigo Money (telco wallet, focused on the unbanked, likely overlaps with many drivers' profile).

**Venezuela**
Methods table:
- Pago Móvil: very good, ~6,000 transactions per minute nationally, instant, no card needed, the dominant method for exactly this kind of flow
- USDT/crypto: good as a currency hedge, under 1% transfer cost, speed comparable to Zelle
- Zelle: good but depends on the driver having USD access, more common for remittances than routine local payments

Processor note: weaker evidence base than the other three countries. Mega Soft (20,000+ Venezuelan businesses, flexible by bank) and Zinli (USD wallet, no Venezuelan bank account required) are the only vendors found with confirmed local presence, neither has a documented ride-hailing use case. State this gap plainly on the slide rather than filling it, it is itself a relevant data point for the conversation with Javier: no public case of a driver-recharge fintech operating in Venezuela was found, unlike Bolivia (Peso) or Colombia (Cobre).

### 6.6 Closing
Reuse the Suno deck's closing slide exactly (German's contact info, "Let's grow together").

---

## WHAT NOT TO DO

- Do not edit the Suno deck. Duplicate it first, build the Yango deck in the copy.
- Do not include Whop, Skool, or the Confidential Merchant case studies, none of them match Yango's business model.
- Do not carry over any Suno-specific number, name, or reference (e.g. "Suno," the $19M figure, Suno's country list).
- Do not invent an approval-rate or performance ranking for any processor in any of the four countries. Where no data exists, say so on the slide rather than implying one processor is measurably better than another.
- Do not duplicate the acceptance-gap chart the way the current Suno deck does (it currently appears twice back to back), include it once.
- Do not add specific claims about Unlimit's or Inswitch's weaknesses beyond what is stated above (no confirmed driver-recharge use case, no confirmed four-country coverage), there is no evidence of anything more negative than that and nothing more should be implied.
