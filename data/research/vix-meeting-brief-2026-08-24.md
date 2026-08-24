# Meeting Brief: Yuno <> Stripe (ViX Prep) — Aug 24, 2026

**Google Doc:** https://docs.google.com/document/d/1yV3flvReakXjAmuGA_MVtFwauWRebK__8gc2iOSCDdA/edit

**Date/Time:** Monday, August 24, 2026, 1:00 PM – 1:30 PM (America/Bogota, GMT-5)
**Organizer:** Berni Castañeda (bcleon@stripe.com), Stripe
**Conference link:** Not found in the calendar event data. ⚠️ Check the original invite email or calendar entry directly before the call.
**Calendar event:** https://www.google.com/calendar/event?eid=YmluODUzcTdmZm45YXV1MTFhbDZqNW5rbW8gZ2VybWFuLnRhdGlzQHkudW5v

**Objective — what winning this meeting looks like:** Leave with a shared, non-competitive framing for how Yuno and Stripe jointly approach ViX (Yuno owns the cash/local/non-card long tail Stripe's own Orchestration product explicitly excludes; Stripe owns and keeps the card rail), and land one concrete next step — ideally a joint outreach or intro path into ViX, coordinated with the relationship Yuno already has with Lorena Velarde, ViX's Payments Director.

## ⚠️ Pre-meeting Action Flags

- Melissa Pottenger (Yuno) is still "tentative" on the invite — confirm she is joining before the call.
- Two of three Stripe attendees (Valentina "valen" and "A. Fernández S.") have not accepted the invite (status: needsAction) — do not assume they will show.
- No conference link is present in the calendar event — locate it from the original invite email (thread `1a02701c2b58ae04`) before 1:00 PM.
- LinkedIn profiles for all three Stripe attendees could not be resolved this session (web search budget was exhausted). Their identities are inferred only from email prefix and calendar display name — treat with caution and verify live in the call.
- This is Yuno and Stripe's **first documented meeting** together (calendar search found no prior events with any of the three Stripe attendees) — treat as a first-meeting relationship, even though the ViX relationship itself is a warm follow-up.

---

## 1. TL;DR Battle Card

**Five facts to know cold:**
1. ViX's checkout stack is identified from its own production code: **Recurly** (subscription billing) + **Conekta** (Mexican PSP) + a live **Mercado Pago** production key + **Bango** (carrier/app-store billing aggregator) + OXXO Pay cash codes + gift cards — with **no orchestrator anywhere in the stack**. ✅
2. Yuno and Stripe already have a real, public partnership: Stripe hosts an official Yuno app on its own marketplace (marketplace.stripe.com/apps/yuno), Yuno documents Stripe as a maintained connector, and both companies announced a global strategic partnership in July 2025. ✅ This is a co-sell conversation, not a competitive one.
3. ViX's CFO publicly named payments as an active lever on the Q1 2026 earnings call: *"expanding payment capabilities through the rollout of cash-based payment options in Mexico"* and a purpose-built checkout hub "to improve the purchase flow, enhance add-on conversions." ✅ Dated April 28, 2026.
4. Yuno already has a warm relationship with ViX's actual payments buyer: **Lorena Velarde, Payments Director at ViX** (⚠️ TheOrg/LinkedIn-sourced, not independently opened) — a Yuno exec (Alejandro) emailed her July 20, 2026 to schedule a dinner to advance "the project we discussed a few months ago." This is a live, in-motion relationship, not a cold account.
5. Stripe itself has no local acquiring in Colombia or Peru — its LatAm footprint is Brazil and Mexico only — and ViX operates in both. Stripe's Mexico OXXO support cannot do recurring billing and isn't available on Stripe Billing; SPEI in Mexico is one-time only, not recurring either. ✅

**Three hooks, in priority order:**
1. **The long tail outside Stripe Orchestration's own scope.** Stripe's new Orchestration product (private preview, May 2025) explicitly routes card PaymentIntents across processors — but by Stripe's own published feature scope, it excludes non-card payment methods, Radar on third-party-routed payments, disputes, and settlement. ViX's Mexico volume already leans on OXXO cash and app-store/carrier billing across 10+ named local partners (Telcel, izzi, Sky, Totalplay, Megacable, Mercado Libre, etc.) — squarely outside that scope.
2. **No orchestrator despite a fragmented, multi-rail stack.** Recurly (billing) + Conekta + Mercado Pago + Bango + 5 app stores + carrier billing across at least a dozen countries, with zero unified routing, retry, or reconciliation layer.
3. **Timing.** ViX just raised US prices (April 2026), just posted record subscriber additions off the World Cup, and management named subscription revenue growth and DTC profitability as its two primary operating priorities (Q2 2026 call) — exactly when involuntary churn and authorization leakage compound, and exactly when a CFO under 5.5x leverage cares about margin, not just growth.

**THE objection they will raise + the answer:**
Stripe will very likely raise **FOX Sports Mexico** — Stripe's own published case study of a Mexican Spanish-language sports streamer using Stripe Billing (Smart Retries + card updater) to get a 20% subscription revenue increase and 54% retention increase in 8 months. *Answer:* that is a pure churn/dunning story with zero mention of OXXO, local Mexican payment methods, or authorization-rate data — it proves Stripe recovers failed *card* payments well, and says nothing about the cash, carrier, and multi-provider complexity ViX already carries that Stripe's own docs place out of scope. Frame it as "that's exactly why this is a joint story, not a competing one."

**The ask (next step to land):** Agree on one concrete joint next step — e.g., a short joint one-pager on how Yuno + Stripe together cover ViX's full stack, or an aligned intro path leveraging Yuno's existing relationship with Lorena Velarde rather than two separate outreach threads.

**Rapport opener:** Congratulate on Stripe's own record year in payments volume (Authorization Boost materials cite $1.9T processed in 2025) and ask directly what Stripe's own relationship with ViX/TelevisaUnivision looks like today — no public evidence was found either way, so this is a genuine, useful discovery question rather than a rhetorical one.

## 2. Who Is in the Room

| Name | Email | Side | Status |
|---|---|---|---|
| German Tatis | german.tatis@y.uno | Internal | Accepted |
| Melissa Pottenger | melissa.pottenger@y.uno | Internal | ⚠️ Tentative |
| Berni Castañeda | bcleon@stripe.com | External (Stripe) | Organizer, Accepted |
| "Valen" (likely Valentina) | valen@stripe.com | External (Stripe) | ⚠️ Needs Action |
| "A. Fernández S." | afernandezs@stripe.com | External (Stripe) | ⚠️ Needs Action |

Stripe-side identities could not be resolved via LinkedIn this session (search budget exhausted). Berni Castañeda organized the call from a Bogota-timezone invite, ⚠️ [INFERENCE] likely LatAm partnerships/BD. The other two are unresolved — do not guess surnames in the room.

**Existing ViX relationship (context, not this meeting's attendees):**
- **Lorena Velarde** — ⚠️ Payments Director at ViX (TelevisaUnivision) since August 2023, Mexico-based (moderate-confidence source). A Yuno exec (Alejandro) emailed her July 20, 2026 proposing a dinner to advance "the project discussed a few months ago" — an active, in-motion relationship.
- **Y. Measson** (ymeasson@televisaunivision.com) — attended an in-person "Vix + Yuno" meeting October 1, 2025 in New York (Eataly), alongside Tomas Calle, German Tatis, and Samuel.

**Relationship timeline:** Oct 1, 2025 (in-person meeting, Measson) → Jul 20, 2026 (dinner outreach to Velarde) → Aug 24, 2026 (this Stripe prep call). Yuno already has a live, multi-touch relationship with ViX's actual payments decision-maker.

## 3. The Company — ViX / TelevisaUnivision

ViX is TelevisaUnivision's Spanish-language AVOD/SVOD/FAST streaming platform, launched January 2022, now the fastest-growing major SVOD in the Americas by subscriber growth rate (Ampere Analysis, June 2025).

| Metric | Value | Period/Source |
|---|---|---|
| Global subscribers | "Well above 10 million" | Jul 22, 2025 |
| Global MAU | ~50 million, +70% YoY | May 2024 upfront |
| DTC revenue (ViX) | ~$1.2B (derived) | FY2025 |
| DTC profitability | Profitable every quarter — first time | FY2025, 3rd year |
| Top markets | Mexico (dominant), US, Peru, Colombia, Argentina, Spain (Jan 2025) | SimilarWeb, 2026 |

**Corporate structure:** Univision Holdings → Broadcast Media Partners Holdings, Inc. → Univision Communications Inc. (bond issuer) → TelevisaUnivision, Inc. (parent). Contracting entity: Univision Communications, Inc. / TelevisaUnivision Digital, Inc., Doral, FL. Grupo Televisa holds a significant equity stake. Other shareholders: Searchlight, ForgeLight, Google, SoftBank Latin American Fund, The Raine Group.

**Leadership:** CEO Daniel Alegre. CFO Juan Pablo Newman (since Sep 1, 2024). ViX Payments Director: Lorena Velarde (⚠️ moderate confidence).

**Strategy themes:** repeated management language on "disciplined financial management," a $400M gross cost-reduction program fully realized in 2025, and subscription revenue growth + DTC profitability as "primary operating priorities" (Q2 2026 call). A margin-conscious buyer.

## 4. Financials

**10-year trajectory:** Pre-merger Univision Communications: 2016 $3,042M → 2018 $2,714M → 2019 $2,688M → 2020 $2,542M → 2021 $2,841M. **Merger: Feb 1, 2022** ($4.8B deal). Post-merger TelevisaUnivision: 2022 $4,626M → 2023 $4,928M → 2024 $5,056M → **2025 $4,827M (down 5%)**.

| Quarter | Revenue | Adj. OIBDA | Net income/(loss) | Leverage |
|---|---|---|---|---|
| Q3 2025 | $1,270.7M (−3%) | $466.7M (+9%) | $90.5M | 5.5x |
| Q4 2025 | $1,322.8M (−2%) | $396.4M (−12%) | $(234.7)M | 5.6x |
| Q1 2026 | $1,075.0M (+5%) | $323.3M (−6%) | $33.3M | 5.7x |
| Q2 2026 | $1,327.4M (+10%) | $387.9M (−3%) | $(10.5)M | 5.5x |

**FY2025 (Dec 31, 2025):** Revenue $4,827.2M (−5%). Advertising $2,916.9M. Subscription & licensing $1,820.2M. Operating income $604.7M (vs. $61.6M loss in 2024). Adjusted OIBDA $1,606.2M (+2%). Net loss $(36.3)M. Gross margin ≈54.7% (computed).

**Debt/leverage:** Total debt $9.3B at Dec 31, 2025. Leverage 5.5–5.7x through 2026. Interest expense $712.6M in FY2025 — **44% of Adjusted OIBDA**. Constant refinancing: $1.5B notes due 2032 (Jul 2025), $1.5B notes due 2033 (Apr 2026).

**Cost discipline (CFO, Feb 24, 2026):** *"These actions delivered approximately $400 million of gross cost reductions and contributed to an 8% year-over-year decline in consolidated operating expenses to $3.2 billion."*

**ViX payments signal (CFO, Apr 28, 2026):** *"We successfully operationalized our ViX add-on model across multiple digital channels while also expanding payment capabilities through the rollout of cash-based payment options in Mexico. Within ViX, we have created a dedicated World Cup hub to improve the purchase flow, enhance add-on conversions."*

**So what for the call:** A leveraged, margin-disciplined parent that just named payments/checkout-flow work as an active 2026 initiative, right when involuntary churn and authorization leakage have maximum financial leverage. Interest expense alone eats 44% of Adjusted OIBDA.

## 5. Competitive Landscape

| Competitor | Segment | Est. share (source + basis) | Scale proxy | Differentiator | Payments posture |
|---|---|---|---|---|---|
| Netflix (LatAm) | SVOD | No named-house estimate; ~53.8M LatAm subs (3Vision, derived) | ~53.8M (2026 est.) | Largest global library | In-house/self-orchestrated; no named PSP |
| Disney+ (LatAm) | SVOD | No estimate; ~16.9M LatAm subs (3Vision, derived) | ~16.9M (2026 est.) | Absorbed Star+ 2024 | **Worldpay** + Cardinal 3DS; no orchestrator; MX = cards + Mercado Pago only |
| Max (HBO Max LatAm) | SVOD | No estimate; ~9.6M LatAm subs (3Vision, derived), fastest-growing in region | ~9.6M (2026 est.) | WBD prestige content | **Spreedly orchestrator confirmed** (Adyen, Checkout.com, iyzico, PayPal); MX = cards only |
| Amazon Prime Video | SVOD | No estimate; ~17.5M LatAm subs (3Vision, derived) | ~17.5M (2026 est.) | Bundled w/ Amazon commerce | No orchestrator disclosed; deepest MX cash rail (OXXO, Kueski BNPL, MSI) |
| Claro Video | SVOD, telco | No estimate | 16 countries (América Móvil) | Telco bundling | Telmex/Telnor/Telcel carrier billing or card |
| Paramount+ (LatAm) | SVOD | No estimate | Priority growth market | Sports + Paramount IP | Not researched |
| Pluto TV (LatAm) | FAST/AVOD | No estimate | 17-country launch (2020); last global MAU 80M (Apr 2023) | Linear-first FAST | 100% free — no payments surface |
| Tubi (Fox) | AVOD/FAST | No LatAm estimate; 2.2% US TV viewing (Nielsen, FY2026, US only) | 110M global MAU (Aug 2026) | On-demand-first | Free; Fox runs separate paid DTC in MX (Jun 2025) |
| Peacock (NBCU) | SVOD/AVOD | No estimate | 48M global paid subs (Q2 2026) | No standalone Spanish tier | Not verified (geo-blocked) |
| Fubo/Hulu+Live TV | vMVPD | No estimate | 5.75M NA subs; Fubo Latino $19.99/mo | 70% Disney-controlled now | Cards + CashApp only; PSP not disclosed |
| Canela Media | FAST/AVOD, US Hispanic | No estimate (self-reported MAU inconsistent) | 85+ FAST channels; $32M funding | US Hispanic ad-tech play | 100% free — zero payments overlap |

**Where ViX sits:** the only major player combining (a) a real hybrid free+premium model, (b) native Mexican cash acceptance that Disney+ and Max lack, and (c) confirmed profitability. Max, its closest SVOD growth-rate rival, already runs Spreedly — ViX is the only major LatAm competitor to Max without an orchestration layer despite having more billing rails to coordinate.

**For the call:** use the Max/Spreedly precedent as air cover — orchestration in this exact vertical and region is already proven, not novel.

## 6. Payments Money Map

**ViX's stack (from production JavaScript, high confidence):**
- **Recurly** — subscription billing platform (not a PSP)
- **Conekta** — Mexican payment processor
- **Mercado Pago** — live production key present, but **not listed in ViX's own help-center article** — ⚠️ possible partial rollout, worth a discovery question
- **Bango** — carrier/app-store billing aggregator behind the reseller map (AT&T, izzi, Sky, Totalplay, Movistar in Mexico; Tigo in 6 Central American markets; Verizon/T-Mobile/Xfinity in US)
- OXXO Pay cash codes + ViX Gift Cards (Oxxo, 7-Eleven, Walmart Group, Soriana, Sam's Club) — Mexico only
- 5 app-store rails: Apple, Google Play, Samsung, Roku, Amazon Fire (+Vizio US)
- Mercado Libre resale bundling (Meli+) in Mexico, Argentina, Chile, Colombia
- **Roku bills ViX directly as merchant of record** outside the US — Roku's Q2 2026 shareholder letter (Aug 6, 2026) names ViX explicitly among "Roku-billed DTC subscription services," alongside TSN, Paramount+, Globoplay
- **No orchestrator identified anywhere.**

**Is Stripe already ViX's processor?** No public evidence found — zero Stripe fingerprints anywhere in ViX's checkout, help center, or shipped code. Genuine open discovery question, not an assumption.

**Stripe in Mexico/LatAm:** Stripe Payments Mexico is a licensed Payment Method Acquirer and Payment Facilitator, sponsored by GetNet México and BBVA México. Supports OXXO (MXN-only, no recurring, no refunds, no disputes, not on Billing/Invoicing/Radar), "Mexico bank transfers" (SPEI-based, no recurring), MSI installments. Does **not** support Carnet, CoDi, or Mercado Pago wallet in Mexico. LatAm footprint is **Brazil and Mexico only** — no Colombia, Peru, Argentina, Chile, all of which ViX operates in.

**Stripe's own orchestration product (key framing fact):** "Stripe Orchestration" (private preview since May 2025) routes card PaymentIntents across processors — but by Stripe's own scope, it excludes non-card payment methods, Radar, disputes, and settlement on third-party-routed payments. Clean line: Stripe Orchestration ≈ cards-across-PSPs; Yuno ≈ everything else.

**Yuno ↔ Stripe partnership (common ground, not news):** Official Yuno app on Stripe's marketplace (marketplace.stripe.com/apps/yuno). Yuno docs list Stripe as a maintained connector with an active 2025 migration notice. Public "global strategic partnership" announcement, July 2025. ⚠️ One flag: y.uno/partner/stripe currently 404s — check internally before referencing live.

**Framing rules:** Never position Yuno as a Stripe replacement. Never claim Stripe lacks Mexico local acquiring (false). Never lead with generic auth-uplift claims — Stripe sells Authorization Boost (+3.8%) into the same slot. Never say "you need an orchestrator" as a category pitch. Do lead with the parts of ViX's stack (OXXO, carrier billing, non-Mexico LatAm, app-store rails) outside Stripe's own scope.

## 7. News & Signals

| Date | Item |
|---|---|
| Jul 23, 2026 | Q2 2026 results: revenue +10% to $1,327.4M, Mexico +53% on World Cup; subscription & licensing +40%; record quarterly subscriber additions; all-time low churn |
| Jun 2026 | ViX raised prices across both ad-supported and ad-free premium tiers in the US |
| Apr 28, 2026 | CFO names "cash-based payment options in Mexico" as an active initiative + World Cup purchase-flow hub |
| Apr 28, 2026 | US ad-supported monthly plan $5.99 → $6.99 |
| Feb 24, 2026 | FY2025: DTC profitability every quarter, first time; $400M cost-reduction program realized |
| Jul 20, 2026 | (Yuno-side) Alejandro emails Lorena Velarde proposing dinner to advance existing project discussion |

## 8. Selling Yuno Here

**Core frame:** Yuno + Stripe together cover ViX's full stack — Stripe owns the card rail; Yuno owns the cash, carrier, app-store, and multi-country long tail.

**Hooks:** InDrive (10 LatAm markets <8 months, 90% approval), Rappi (zero implementation time, 80% less analyst resolution), Livelo (+5% approval, 50% recovery). Max/HBO Max already runs Spreedly in this exact region.

**Landmines:** Don't frame Yuno as a Stripe alternative. Don't claim Stripe lacks Mexico acquiring. Don't lead with generic auth-uplift numbers. Don't pitch "you need an orchestrator" as a category claim. Don't raise Stripe reliability/outages.

## 9. Be Ready For

| Question | Answer |
|---|---|
| "Isn't this what Stripe Orchestration already does?" | Card-only by Stripe's own scope — no non-card methods, no Radar/disputes/settlement on third-party volume. ViX's actual complexity sits outside that scope. |
| "What's Yuno's relationship with ViX today?" | Existing relationship with Lorena Velarde, in active discussion since mid-2026. Frame as bringing Stripe into a conversation already in motion. |
| "Is Yuno's Stripe integration a heavy lift?" | Maintained, production connector referenced in Yuno's own docs with an active 2025 migration notice. |
| "Do you compete with Stripe Billing/Smart Retries?" | No — Stripe Billing recovers card volume Stripe already processes. Yuno's value is the layer across everything Stripe doesn't itself acquire. |

## 10. Agenda (30 min)

| Time | Block |
|---|---|
| 1:00–1:05 | Intros — confirm who's in the room |
| 1:05–1:12 | Discovery: Stripe's current relationship (if any) with ViX/TelevisaUnivision |
| 1:12–1:20 | Align on joint framing (card rail vs. long-tail split) |
| 1:20–1:27 | Discuss ViX opportunity (payments-as-lever quote, OXXO/carrier fragmentation, timing) |
| 1:27–1:30 | Agree next step and owner |

## 11. Discovery Questions

1. Does Stripe have any existing commercial relationship with ViX or TelevisaUnivision today?
2. Has Stripe Orchestration been pitched into any LatAm streaming account yet — reaction to its card-only scope?
3. Who owns the ViX relationship on Stripe's side, if it exists?
4. What does Stripe's ideal co-sell motion look like here?
5. Is there a standard Stripe partner agreement or co-sell process not yet in place?

## 12. Post-Meeting Checklist

- Send recap email same day
- Log outcome and new facts about Stripe↔ViX relationship
- Schedule agreed next step
- Update Yuno memory/CRM

## Appendix — Sources

ViX Help Center (payment methods, pricing, cancellation articles) · ViX production JS bundles (vix.com/assets/web/_next/static/chunks) · TelevisaUnivision investor relations (corporate.televisaunivision.com/press, s29.q4cdn.com/983326523) · SEC EDGAR (Grupo Televisa 20-F, Univision Communications bond filings) · Stripe (stripe.com/mx/pricing, docs.stripe.com/payments/oxxo, docs.stripe.com/payments/orchestration, marketplace.stripe.com/apps/yuno, stripe.com/customers/fox-sports-mexico) · Yuno docs (docs.y.uno/docs/connections) · 3Vision Americas streaming forecast · Google Calendar and Gmail (Yuno internal) · TheOrg (Lorena Velarde, ⚠️ moderate confidence)
