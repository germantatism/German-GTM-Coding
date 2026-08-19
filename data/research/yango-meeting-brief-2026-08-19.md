# Meeting Brief: Yuno <> Yango (Aug 19, 2026)

Google Doc: https://docs.google.com/document/d/1rar1IrqDxZ6ZCKWnfbRd7pnT1BtCXuXHNVaOt_Zts74/edit

## Header

**Meeting:** "Yango + Yuno" · Wed Aug 19, 2026 · 11:00–11:45 AM (America/Bogota, GMT-5) · [meet.google.com/gai-cuqi-ffy](https://meet.google.com/gai-cuqi-ffy)

**Objective:** This is explicitly a data-gathering meeting, not a closing call. Winning this meeting means walking out with average ticket size, monthly recharge transaction volume, and acceptance/approval rate data (by country: Colombia, Peru, Bolivia, Venezuela) to replace the modeled figures currently in Yuno's business case and proposal.

**⚠️ Pre-meeting action flags:**
- **Deck version conflict, resolve before presenting.** The live Google Slides deck ("Yango + Yuno_Aug 26", id `1XPdfoKEGoT-s7-XcIoewxbOWnMidO9JfcMTUgYvclak`) still showed the OLD unreconciled headline numbers (~131k drivers, ~$75M volume, +$6M/year opportunity) as of the last content check today, even though the 2026-08-18 reconciliation work (git history) calls for updating to ~162,000+ drivers, ~$332M volume, +$29M/year, based on the appendix's better-sourced country data. Confirm which numbers are actually live before screen-sharing.
- **Three leftover "Eventbrite" template artifacts** per German's own presenter guide: Slide 6 eyebrow reads "HOW EVENTBRITE RUNS PAYMENTS TODAY"; Slide 19 has "Eventbrite's roadmap"/"commitment to Eventbrite"; Slide 29 (GoFundMe case) has an internal QA note pasted into a client-facing bullet.
- **Slide 6 country percentage chips** (CO 13–62%, PE 5–24%, BO 2–9%, VE 1–5%) have no legend explaining what they measure.
- Javier's `@yango-team.com` inbox bounces intermittently; backup invite went to `jpatino@yango.com` (still needsAction) — not blocking, yango-team.com acceptance is confirmed.

## 1. TL;DR Battle Card

**Five facts to know cold:**
1. Driver *payouts* (dispersal) are already solved via Cobre Fast Pay in Colombia (120,000+ drivers, real-time, ~$1M USD/week moving through the Dubai→Cobre corridor). Yuno does not touch this — it only orchestrates the *recharge/collection* side.
2. Confirmed current stack, from German's own May 12, 2026 in-person discovery: cards run through **PayU** (majority share) and **Unlimit** (minority, underperforming — "no les ha ido bien"); driver recharge pay-ins run through **PayRetailers**, called "basura" by Javier's team and actively being migrated away toward Cobre.
3. Yango HQ is evaluating **Unlimit** and **Inswitch**, but neither covers all 4 target countries (Unlimit: CO+PE only; Inswitch: CO+PE+BO, Venezuela page 404s). Inswitch also publishes a case study "Yango Scales with Inswitch" describing driver payouts, hosted checkout, wallets and cross-border payments — very likely this same Yango, not confirmed by name/date/quote. ⚠️ Ask directly.
4. HQ wants this evaluated in depth by end of August 2026; today's meeting exists specifically to gather the data Yuno needs to build the joint proposal HQ asked for.
5. "Konstantin" reportedly owns this decision for Colombia, Peru, Bolivia *and* Africa, per Javier's team (May 12 discovery notes). Identity/title unconfirmed.

**Three hooks, in priority order:**
1. **Multi-country consolidation:** 4 countries, 4 different winning local rails (PSE/Bre-B CO, Yape/Plin PE, QR Simple BO, Pago Móvil VE) — no vendor under evaluation covers all 4.
2. **Live vendor comparison:** neither Unlimit nor Inswitch publishes approval-rate data for these markets. Yuno's "Compare" rollout step is the first real head-to-head they'd ever see.
3. **Proven vertical fit:** inDrive (direct low-cost ride-hailing competitor) is already live on Yuno — 18 countries, ~90% approval on key routes, ~29% fraud reduction, 11 new countries in 8 months.

**THE objection + answer:** "Why not just pick Unlimit or Inswitch, HQ already likes them?" → Neither covers all 4 countries (confirmed on their own sites). If the Inswitch case study is confirmed as Yango, that's useful, not a blocker — Inswitch becomes a known integration Yuno orchestrates alongside, not a rival to fully replace.

**The ask:** average ticket size, monthly recharge volume (count + $), any acceptance/approval-rate data per country, confirmation of Konstantin's role, and whether Inswitch is a live vendor today.

**Rapport opener:** Javier's family is in Cali (confirmed well per his Aug 18 message).

## 2. Who Is in the Room

| Name | Role / Side | Status | Notes |
|---|---|---|---|
| Javier Patiño (jpatino@yango-team.com) | Yango Colombia — reported Head of Operations (unconfirmed tenure) ⚠️ | Accepted | Main contact since May 5, 2026. Coordinates NDA/legal. Bogotá, family in Cali. Wants pitch framed LatAm-wide so HQ product pays attention. |
| Alejandro Sanabria Cárdenas (pcardenas@yango-team.com) | Yango Colombia — "handled integrations previously"; possibly Regional Manager, Finance (medium confidence) ⚠️ | Accepted | Added Aug 18 to help gather transaction data. Likely data gatekeeper. |
| Luis Alejandro Montealegre Diaz (lmontealegre@yango-team.com) | Yango Colombia, Ops & Business Development Manager — ex-Rappi (Global Operations Incentives & Earnings Lead) | Accepted | Added Aug 18 as "ops manager." Civil Engineering, Universidad Javeriana. Deep marketplace/payout-economics background. |
| German Tatis | Yuno — organizer | Accepted | — |
| Justo Benetti | Yuno — CRO | Accepted | Led enterprise integrations at dLocal before Yuno. |
| Maria Jose Pineda Pedrazzini | Yuno — Sr. Key Account Manager | Accepted (optional) | — |

**Sponsor/intro path:** Javier Patiño since May 5, 2026 → in-person meeting May 12 with Mark Bitton (Yango Colombia Country Manager). Mark Bitton is NOT on today's invite — status unconfirmed. ⚠️ Ask.

**Other known contacts:**
- **Mark Bitton** — Country Manager, Yango Colombia; leads Yango Ventures Colombia (first investment: MejorCDT); fronted the Cobre Fast Pay announcement. Not on today's call.
- **"Konstantin"** — reportedly owns CO/PE/BO/Africa payments decision. Identity unconfirmed.
- **Andrei Krugliak** — CEO, Yango Fintech (Dubai); ex-CPO Yango; ex-Head of Product Yandex.Taxi. Likely the real HQ payments gatekeeper.
- **Daniil Shuleyko** — Group CEO. **Andrey Rozov** — Group CFO.

**Relationship timeline:** May 5 event invite → May 12 in-person discovery (Mark Bitton + Javier; FX/4x1000 workaround via Cobre Dubai corridor, $1M USD/week, PayU+Unlimit for cards, PayRetailers for recharge pay-ins, talks with Kushki and Inswitch) → NDA signed both sides by May 27 → Jun 24, HQ payments meeting flagged → Jul 10, HQ receptive but deprioritized behind driver top-up integration pain until "finales de agosto" → Jul 15, today's placeholder set → Aug 14, internal deck-review call → Aug 17–18, deck build/reconciliation, Javier adds Alejandro and Luis. **Implication:** warm 3.5-month relationship, real discovery already done — today closes the data gap before HQ's end-of-August review.

## 3. The Company

Dubai-headquartered ride-hailing, delivery and multi-service super-app (Ride, Moto, Delivery, Transport, Maps, Buy&Sell, Yango Pro, Yango Ventures), 30+ countries across MENA/Africa/Central Asia/LatAm. Historically part of Yandex (Yandex N.V. divested Russia businesses Feb 2024, rebranded Nebius Group Jul 2024, unrelated to ride-hailing now). Yango operates independently. Asset-light: no owned vehicles/employed drivers.

| Metric | Value | Source/date |
|---|---|---|
| Group footprint | 30+ countries; Yango Ride in 25 countries, 630M+ trips since launch ⚠️ | Internal Yuno proposal doc, not independently re-verified |
| Colombia MAU | 1.5M+ weekly/monthly | Portafolio 2026-03-11; Infobae 2025-12-19 |
| Colombia drivers | 120,000+ paid real-time via Cobre Fast Pay | La República et al., 2026-05-29 |
| Colombia commission | ≤14% self-reported vs 20–30% competitors | Infobae, 2025-12-19 |
| Colombia investment | USD 300M/4yr; target 600,000 daily trips by 2028 (50x) ⚠️ | Internal Yuno proposal doc, not independently re-verified |
| Bolivia | #3 global traffic source (9.68%); ~1M MAU claimed; $25M+/3yr invested; first LatAm market (2022) | Similarweb 2026-08-18; estrategiabolivia.com 2025-03-17 |
| Peru | ~15,000 active vehicle units (Yego proxy); 200,000+ weekly mototaxi trips | Gestión, 2026-05-12 |
| Venezuela | Caracas-only, launched Jul/Aug 2025; 11M+ km driven in first 100 days | bancaynegocios.com, 2025-11-06 |
| Africa expansion | $150M committed, 10 new markets 2026 | technext24.com, 2026-05-19 |

**Corporate structure:** current entity RideTechnology Global FZ-LLC (UAE Free Zone LLC). Historical: Ridetech International B.V. (ex-Yandex N.V. subsidiary). ⚠️ Unverified, do not cite: "MLU B.V." intermediate holding claim; €100M GDPR fine reference.

**Leadership:** Daniil Shuleyko (Group CEO) · Andrey Rozov (Group CFO) · Andrei Krugliak (CEO, Yango Fintech, Dubai — likely real payments decision-owner) · Mark Bitton (Country Manager, Colombia).

**Strategy themes:** aggressive capital-backed emerging-market expansion; building an internal financial layer (Yego, Yango Food stablecoin via Peso, Yango Ventures); asset-light + build-your-own-infra philosophy (own maps to cut Google dependency) — values control/reduced vendor dependency.

## 4. Financials

Privately held, no audited financials disclosed. No reliable revenue trajectory, recent-quarter trend, or last-full-year figure found.

**⚠️ Entity-confusion warning:** an unrelated, formerly Shenzhen-listed Chinese real-estate company is also named "Yango Group Co., Ltd." (SZ:000671, delisted). Data-aggregator results (Growjo's "$779.9M revenue, 1,000–5,000 employees"; Revelio Labs' "13,437 employees") almost certainly describe that unrelated company and are excluded here. PitchBook previously reported ~200 employees for the ride-hailing Yango — single, dated, low-confidence source.

No independent VC funding round found since separating from Yandex; capital commitments ($150M Africa, $20M Yango Ventures) read as parent/self-funded. No IPO signal found.

**So what for the call:** a company self-funding aggressive expansion (not answering to external VCs on unit economics) values speed-to-market and avoided integration cost over marginal fee savings. Lead with Yuno's 6–10-week time-to-market and no-lock-in optionality, not just bps savings.

## 5. Competitive Landscape

| Competitor | Segment vs. Yango | Est. market share | Differentiator | Payments posture |
|---|---|---|---|---|
| Uber / Careem | MENA ride-hailing (Egypt, UAE, Qatar, Saudi) | No sourced % split; Egypt ride-hailing market $1.84B (2024)→$3.61B (2030E), Grand View Research | Global scale, dual-brand MENA strategy | **Careem confirmed on Checkout.com** as PSP, incl. Mastercard-powered Careem Pay top-ups |
| Bolt | Africa/MENA (Morocco, Tunisia, Egypt + 8 African countries, 90+ cities) | No estimate available | EV push South Africa; ChatGPT booking (Jul 2026) | No confirmed PSP; reportedly in-house/proprietary |
| inDrive | Egypt, Morocco, Tunisia, Zambia — low-cost, direct competitor | No estimate available | Negotiated-fare model | **Yuno client** — 18 countries, ~90% approval key routes, ~29% fraud reduction, 11 countries/8mo |
| DiDi | Egypt (+4 cities Nov 2024) | No estimate available | China-scale tech, secondary-city push | Not confirmed |
| Yassir | Algeria, Morocco, Tunisia | No estimate (8M+ users, 100K+ drivers, $190M+ raised) | Super-app, YassirPay | Not confirmed |
| Heetch | Morocco, Algeria | No estimate available | France-origin, driver-friendly | Not confirmed |
| Grab | SE Asia super-app (peer, not direct) | N/A | 2025 revenue $3.37B, first profitable year | GrabPay — benchmark peer |
| Gojek/GoTo | Indonesia super-app (peer) | N/A | ~$1.1B net revenue 2025, 66M users | GoPay — benchmark peer |
| Rappi | LatAm super-app, driver/courier payout overlap | No estimate available | LatAm's largest delivery super-app | **Yuno client** — Nova AI recovery, +5pp/+8pp uplift, >$1M savings, 9 countries |
| Cabify | LatAm ride-hailing (Peru/Colombia) | No estimate available | Premium/corporate positioning | Not confirmed |

Yango's own group already validated the orchestrator model once: Flutterwave partnership in Zambia (Feb 2026) for card payments on rides + food delivery — a usable internal precedent. For the call: inDrive is the sharpest vertical reference; Careem the sharpest payments-stack benchmark.

## 6. Payments Money Map

**Confirmed current stack** (German's own May 12, 2026 discovery, primary source):
- Cards: **PayU** (majority) + **Unlimit** (minority, underperforming)
- Driver recharge pay-ins: **PayRetailers** ("basura," migrating away)
- Payouts: **Cobre** Fast Pay, real-time, 120,000+ CO drivers; Dubai→Cobre corridor ~$1M USD/week; Nequi via Cobre + tokenization
- In conversation with: **Kushki** and **Inswitch**
- "Konstantin" reportedly owns CO/PE/BO/Africa payments decision

**⚠️ Unresolved, ask directly:** Inswitch's "Yango Scales with Inswitch" case study (driver payouts, hosted checkout, wallets, cross-border payments for a mobility platform) is very likely this Yango, not confirmed by name/date/quote. If confirmed, Inswitch is an existing/former vendor, not just a candidate.

**Coverage gaps:** Unlimit = CO+PE only; Inswitch = CO+PE+BO (VE 404s). Of 12+ MoR/PSP candidates researched, none confirms Venezuela.

**Local rails not yet connected:**
- CO: Bre-B (34M+ users/6mo), Nequi, Daviplata
- PE: Yape + Plin (interoperable since 2023, 50%+ of cashless tx)
- BO: QR Simple (94% of interbank transfers); USDT via Peso live in Yango Food since 2026-08-14
- VE: Pago Móvil (~7,000 tx/min), USDT, Zelle; Yango runs 3 separate bank integrations (Banco de Venezuela, BNC, Bancamiga) today — live fragmentation example

**Framing rule:** Yuno complements Cobre, never replaces it. Recharge/collection side only.

## 7. Top Markets

| Country | Leading local rail | For the call |
|---|---|---|
| Colombia | PSE (63.9% of digital tx); Bre-B fastest-growing (34.9M users/6mo) | Cards are the weakest rail despite being one of only two methods Yango accepts today |
| Peru | Yape (16.4M MAU) + Plin (2.6M MAU), interoperable | Covering only one of the two leaves ~half the driver base uncovered |
| Bolivia | QR Simple, free/universal, 94% of interbank transfers | Cards never won here; USDT via Peso already live in Yango Food |
| Venezuela | Pago Móvil, ~7,000 tx/min | No global PSP confirms coverage; Yango's 3-bank setup is the fragmentation case in miniature |

## 8. News & Signals

- **2026-08-14** — Peso enables USDT payments inside Yango Food in Bolivia (2,000+ restaurants).
- **2026-08-14** — Naran (rent-to-own vehicle financing, founded by ex-Yango execs) raises $10M from Landel.
- **2026-08-04 (approx.)** — Bolt integrates ChatGPT booking in South Africa (competitive signal).
- **2026-05-29 (approx.)** — Cobre Fast Pay real-time payout integration for 120,000+ CO drivers covered in press.
- **2026-05-19** — Yango commits $150M to 10 new African markets in 2026.
- **2026-04-15** — Otaxi (Oman) acquired by ITHCA + Yango.
- **2026-02-25/26** — Flutterwave partners with Yango in Zambia — Yango's own orchestrator precedent.

## 9. Selling Yuno Here

**Core frame:** "Yuno sits on top of the recharge/collection side only. Cobre stays exactly as it is for dispersal. This isn't a vendor swap, it's the head-to-head comparison you've never had."

**Hooks with proof:** inDrive (same vertical, direct competitor, already Yuno) · Rappi (LatAm super-app, Nova AI recovery) · Yango's own Flutterwave-in-Zambia precedent.

**Landmines:**
- Don't state Yango "has no orchestrator" as fact — frame as discovery question.
- Don't disparage Unlimit/Inswitch beyond documented coverage gaps.
- Don't present $6M/$29M as firm — both modeled from public data; today's meeting replaces the model.
- Don't assume Mark Bitton is still involved — unconfirmed.

## 10. Be Ready For

| They may ask | Ready answer |
|---|---|
| "Why not just pick Unlimit or Inswitch?" | Neither covers all 4 countries — Unlimit CO+PE, Inswitch CO+PE+BO. Venezuela uncovered by everyone researched. |
| "Does this replace Cobre?" | No. Settles into the same Cobre account. |
| "How confident is the $6M/$29M number?" | Modeled from public data. Today's meeting is exactly how it gets replaced with real numbers. |
| "Is Inswitch already our vendor?" | Turn it back: ask if their published case study is live today. |
| "How long to production?" | 6–10 weeks per market, per the deck's own modeling. |
| PCI/security/compliance | PCI DSS v4.0, SOC 2 Type 2, ISO 27001, ISO 27701, GDPR. |

## 11. Agenda

| Time | Block | Notes |
|---|---|---|
| 0:00–0:05 | Warm open (Cali/family); confirm today's goal | ____ |
| 0:05–0:15 | Walk "Today" + "Opportunity" slides (confirm live numbers first) | ____ |
| 0:15–0:30 | Core data ask: ticket size, volume, acceptance rates by country | ____ |
| 0:30–0:38 | Confirm stack + Inswitch status; ask about Konstantin; confirm Bitton | ____ |
| 0:38–0:45 | Next steps: validate appendix figures, HQ timeline, "Connect" date | ____ |

## 12. Discovery Questions

1. Average driver recharge/top-up ticket size per country (CO/PE/BO/VE)? Notes: ____
2. Monthly transaction volume (count + $) for driver recharges, per country? Notes: ____
3. Current acceptance/approval rates by processor or method, even directional? Notes: ____
4. Is PayU still ahead of Unlimit on cards — approximate split? Notes: ____
5. Where does PayRetailers sit today — fully migrated to Cobre or still partial? Notes: ____
6. Is the Inswitch case study describing your team's setup? What's live vs. evaluated? Notes: ____
7. Who is Konstantin and what's his role? Notes: ____
8. Is Mark Bitton still involved? Notes: ____
9. Venezuela: still 3 separate bank integrations, or consolidated since launch? Notes: ____
10. What does HQ's "end of August" review actually decide? Notes: ____

## 13. Post-Meeting Checklist

- Send recap email same day (cc Alejandro, Luis; internal cc Justo, Maria).
- Log real ticket/volume/acceptance data into appendix "TO VALIDATE" fields.
- Fix the deck's 3 leftover Eventbrite artifacts and reconcile main-body numbers.
- Confirm Inswitch relationship status, update MoR/PSP appendix slide.
- Schedule agreed next step.
- Update Yango project memory.

## Appendix: Sources

La República, Portafolio, Infobae, DPL News, mobiletime.la, Gerencia y Negocios · Similarweb · estrategiabolivia.com · Gestión · bancaynegocios.com · technext24.com / ecofinagency.com · techcabal.com / thisdaylive.com · criptonoticias.com / cryptobriefing.com · launchbaseafrica.com · Grand View Research · Checkout.com / Mastercard press releases · inswitch.com/case-studies/yango · unlimit.com/coverage/latam · PitchBook, Tracxn · Wikipedia (Yango Group, Nebius Group) · German's May 12, 2026 discovery notes + WhatsApp thread with Javier Patiño · internal Yuno proposal doc for Mark Bitton · live deck "Yango + Yuno_Aug 26" + presenter guide · appendix-4-country-deepdives-2026-08-18.md · claude-design-prompt-deck-reconciliation-2026-08-18.md.
