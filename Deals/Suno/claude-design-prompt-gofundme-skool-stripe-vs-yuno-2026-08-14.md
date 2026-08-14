# Prompt Claude Design: GoFundMe + Skool case studies, new "Stripe vs Yuno" section (2026-08-14)

Target deck: the Suno success-cases deck (Client Case Studies + Appendix), current structure as edited in Google Slides (file id `1hOUPZ7HAvDzT-2Y2Xw2-Tdr3J-gCWIHi`).

Three things to do, in this order:
1. Add a GoFundMe case study slide after Mercado Libre.
2. Add a Skool case study slide after GoFundMe.
3. Add a new section, "The Case for a Second Rail," with 3 slides, positioned after the case studies + testimonials slide and before the Appendix divider. Move the existing "The acceptance gap is measurable" (LATAM/APAC) slide into this new section too, right after slide 3.1 below.

Match the existing visual design system (cards, stat boxes, color, typography) already used in the Whop/Rappi/Mercado Libre case study slides and in the appendix tables. Do not change layout conventions, only the content specified below.

---

## 1. GoFundMe case study slide

Use the same Before Yuno / After Yuno / Impact / Pain Points card layout as Whop.

**Company description:** GoFundMe, the world's largest social fundraising and community-giving platform, is a live Yuno merchant.

**Before Yuno:** [NOT CONFIRMED — leave this card empty or hidden. We do not have a verified fact about GoFundMe's payments stack before Yuno; do not infer or invent one.]

**After Yuno:** [PENDING APPROVAL — do not publish any of the following until Samuel Vieira or Justo Benetti confirms it is cleared for external use. If not cleared by the time this deck ships, delete this card and keep only the one-line company description above plus the GoFundMe logo.]
- Yuno's first live merchant on the Marketplace / Recipients solution, since February 19, 2026
- Multi-processor: Stripe (primary, connected accounts, splits via application_fee and transfer_data, ACH), Adyen (hosted onboarding, ACH via Plaid, cross-border payout handling), Tabapay (card collection + beneficiary KYC); PayPal marketplace in build
- Automated splits across donation, tip and processing fee, with beneficiary transfers live in production
- Direct headless API integration, pilot merchant for Yuno's new Universal SDK

**Impact:** [PENDING APPROVAL, same gate as above] Transaction volume grew from 25K in February 2026 to 468K in April 2026, projected to reach 3.5M-10M transactions/month at full ramp.

**Pain points before Yuno:** [NOT CONFIRMED — leave empty, same reason as "Before Yuno."]

---

## 2. Skool case study slide

Use a lighter one-card layout (logo + 2 short paragraphs), not the dense 4-card Whop layout — there is not enough confirmed data yet to fill Impact or Pain Points honestly.

**Company description:** Skool, a community and course platform for creators (Austin, TX).

**Before Yuno (confirmed):** Skool ran its community subscription billing entirely on Stripe, a single PSP, with no failover or local payment rails.

**How we could help (explicitly labeled as a projection, not a confirmed result — Skool is signed and currently onboarding, so there is no live "after" data yet):** Based on the pattern from comparable Stripe-only subscription businesses, most directly Whop (see that case study on this same deck), we would expect to add a second and third card PSP for redundancy, local APMs and BNPL relevant to Skool's international creator and student base, and smart routing with retries and 3DS orchestration. In Whop's case this delivered +5 to 10 percentage points of acceptance uplift by corridor; we would expect a similar direction for Skool, to be confirmed against their real funnel data once onboarding completes.

**Do not add:** any specific dollar figure, percentage, or "Impact" card for Skool. None of that exists yet.

**PENDING APPROVAL:** confirm with Justo Benetti that it is authorized to name Skool externally to Suno while Skool is still in onboarding, not yet live.

---

## 3. New section: "The Case for a Second Rail"

Section divider slide, same style as the existing "Client Case Studies" / "Appendix" dividers.

### 3.1 — "THE DECISION"

Reuse this content as-is (source: internal MoonActive engagement deck, this specific slide has no MoonActive-identifying data in it):

Title: "The decision: one provider for everything, or the best provider per market"

Option 1, one provider for everything:
- All traffic stays with a single provider, in every market
- (+) One integration and one relationship to manage
- (−) Leaves measured revenue uncollected in every market a second provider would win
- (−) No live comparison: underperformance has no reference and goes unnoticed
- (−) All volume depends on a single provider's performance and uptime

Option 2, the best provider per market:
- Each market runs on the provider that measurably wins it, and switches if the data changes
- (+) Maximizes revenue: every market on its best provider
- (+) Keeps both providers competing on live, comparable data, so performance keeps improving
- (+) Markets switch by an agreed rule, in both directions, as results change
- (−) Needs routing and shared measurement

Do not include the "~$3M a year" figure that appeared in the source slide, that is MoonActive's measured number and does not apply to Suno.

### 3.2 — "THE FRAMEWORK: Four Levers, One Orchestration Layer"

This replaces the source deck's four-lever framework entirely with Suno's own business case levers (source: Suno BC model, $19.2M portfolio, as presented to Suno Aug 7, 2026). Do not use any of the four lever definitions or numbers from the MoonActive source deck for this slide.

Headline: "Suno can unlock an estimated ~$19M a year in subscription revenue across four levers"
Subhead: "Estimated from Suno's public data and Yuno's business case model; to be validated together with Suno's real funnel data."

Box 1 — Local payment methods: "Add the local payment methods your funnel is missing in top markets, like Pix and UPI." — ~$12M/yr estimated, ~128K incremental paid subscribers
Box 2 — Authorization uplift: "Recover cross-border card declines through local acquiring and multi-PSP routing." — ~$3M/yr estimated
Box 3 — Renewal continuity: "Fix the retry logic currently losing renewals." — ~$1M/yr estimated
Box 4 — Engineering avoidance: "Skip building and maintaining three disconnected billing rails in-house." — ~$3M build avoided, estimated

Footer: "Value estimates based on Suno's public ARR and subscriber data plus Yuno's business case model presented Aug 7, 2026. Figures are estimates, to be validated jointly with Suno's real funnel data."

### 3.3 — "What we typically see in a head-to-head test" (new slide, does not exist in the source deck)

This slide extracts the PATTERN from a real Yuno multi-market comparative engagement, fully anonymized. Do not name the client, do not use any exact dollar figure tied to anyone's revenue, do not use precise per-market percentage-point deltas presented as exact results. Round and generalize everything below, it is drawn from a real engagement but must read as an aggregate pattern, not an attributable result.

Headline: "When we've run Yuno head-to-head against a single global PSP, the pattern repeats"

Bullets:
- In live multi-market comparisons, Yuno has come out ahead on end-to-end conversion in roughly a third of markets tested outright, concentrated in markets with strong local acquiring
- Bank approval, the infrastructure half of the funnel, has favored Yuno in close to half of tested markets, including large markets where checkout-page conversion is still catching up
- Where Yuno trailed at the start, the gap has closed by more than 80% within about a month once specific fixes shipped: 3DS/SCA tuning, stored-credential and network-token handling, and checkout redesign
- First-time payers converting on Yuno's rails return as one-click buyers on saved cards, so the advantage compounds automatically as the token vault matures, independent of any other fix
- Local payment methods, once enabled, have captured a large share of completed volume in the markets that offered them, often 30%+ of volume in the strongest cases

Footer/source line: "Patterns observed across live Yuno orchestration engagements. Individual results vary by market and merchant."

---

## WHAT NOT TO DO

- Do not attach, reference, or pull any content directly from the MoonActive/Coin Master engagement deck into this design tool. Only the abstracted text in section 3.3 above, already stripped of client identity and exact figures, should be used.
- Do not publish the GoFundMe "After Yuno" or "Impact" cards, or the Skool case study at all, until the approvals noted above (Samuel Vieira/Justo for GoFundMe specifics, Justo for naming Skool externally) are confirmed. If unconfirmed at build time, ship the safe fallback version noted in each section.
- Do not invent a "Before Yuno" or "Pain points" narrative for GoFundMe. Leave blank rather than infer.
- Do not add a specific "Impact" figure to the Skool slide. It is explicitly a projection, not a result.
- Do not touch any other slide in the deck outside what is listed here (case studies for Whop/Rappi/Mercado Libre, the appendix compliance table, the closing slide, etc. stay as they are).
- Do not invent per-country or per-market percentage figures for a Yuno vs Stripe comparison beyond what is in section 3.3, and keep that section's language rounded and aggregate, not precise-looking.
