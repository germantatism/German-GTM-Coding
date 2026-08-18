# Appendix: 4 Country Deep-Dive Slides for Yango (2026-08-18)

Colombia, Peru, Bolivia, Venezuela — driver "recarga" (top-up) collection business case. Mirrors the Suno 20-country deep-dive template, adapted to Yango's business model: a driver pre-funds a balance, Yango's commission is deducted per completed trip, and the "recharge" event is the transaction Yuno's orchestration would sit on top of (dispersal to drivers is a separate, already-solved problem via Cobre's Fast Pay in Colombia — see `claude-design-prompt-yango-deck-2026-08-16.md`).

⚠️ **Data quality varies sharply by country and every figure below carries its own confidence level.** Colombia has a strong, recent, company-adjacent driver count (Cobre press coverage). Peru and Bolivia have no single current total driver count — proxies are used and flagged. Venezuela has no driver count at all and is not sized in dollars; the absence of a payments ecosystem is itself the finding for that market. Nothing below should be repeated as a hard fact in front of Yango without the flags attached.

---

## METHODOLOGY (state this on the appendix divider/methodology slide)

- **Driver/user counts**: the most recent public or company-stated figure per country. Colombia (120,000+ drivers) comes from dated 2026 press coverage of the Cobre-Yango payout integration. Peru and Bolivia have no single audited total; Peru uses Yango's vehicle-financing affiliate (Yego) fleet size as a floor proxy, Bolivia uses a 2023 nationwide figure that likely understates 2026 scale. Venezuela has no public driver count at all, only a qualitative "hundreds of thousands of passengers in 100 days" and a driver-oversupply signal.
- **ARPU proxy** = average gross monthly revenue a driver generates on the platform. Used directly from Yango's own published ranges where available (Venezuela). Where not available, sourced from the closest comparable platform's driver-economics data (DiDi Colombia, DiDi Peru) or derived from a confirmed trips-per-driver ratio combined with Yango's own published fare range (Bolivia). Never invented.
- **Commission rate**: Yango's own self-reported range where confirmed (Colombia ≤14%; Venezuela 25-30%), a lower-confidence third-party figure where that's all that exists (Peru 10-15%, unofficial driver-blog source), or an unconfirmed regional assumption clearly flagged as such (Bolivia ~15%, no Bolivia-specific source found).
- **Annual Recharge Volume (modeled TAM)** = drivers × monthly ARPU × commission rate × 12. This approximates the total commission flow Yango collects from its driver base annually in that country, i.e. the volume that moves through the recharge/top-up rail and that Yuno's orchestration would optimize. Not modeled for Venezuela (no defensible driver count exists).
- **Approval-rate uplift**: no PSP in any of the four countries publicly discloses a current, country-specific approval-rate percentage. The one general, citable benchmark is PayRetailers' LatAm-wide finding that cross-border card processing sees approval rates "as low as 20% to 45%" versus 70-90% with local acquiring. This is cited qualitatively only — no per-provider ranking or invented percentage is presented for any of the four countries.
- All dollar figures are **Yuno business case model outputs, not Yango's actual data**, to be replaced in a joint data-validation sprint. Where a number could not be sourced at all, it is marked NOT FOUND rather than estimated.

---

## MASTER SUMMARY TABLE

| # | Country | Yango drivers (confidence) | Leading local payment method (users) | ARPU proxy (USD/mo) | Avg ticket (USD) | Modeled annual recharge TAM |
|---|---|---|---|---|---|---|
| 1 | 🇨🇴 Colombia | 120,000+ (dated, Cobre payout integration, May 2026) | PSE — 63.9% of digital payment transactions | ~$1,438 (industry proxy) | ~$8.00 | **~$290M/year** |
| 2 | 🇵🇪 Peru | 15,000 active vehicle units (Yego fleet-financing proxy, not total drivers) | Yape — 16.4M MAU (Q1 2026) | ~$1,665 (industry proxy) | ~$3.50 (low confidence) | **~$37M/year** (lower confidence) |
| 3 | 🇧🇴 Bolivia | ~27,000+ (revised 2026-08-18: Santa Cruz ~22,900 derived from its own 4M trips/month + Cochabamba's confirmed 4,000; supersedes the stale 14,000-nationwide 2023 figure) | QR Simple — 94% of interbank electronic transfers | ~$107 (derived, Bolivia-specific) | ~$0.61 | **~$5.2M/year** (revised from $2.7M; still a floor, excludes La Paz/El Alto) |
| 4 | 🇻🇪 Venezuela | ~3,100 (revised 2026-08-18: modeled from Yango's own disclosed 11M+ km in 100 days ÷ assumed trip distance ÷ Bolivia's cross-market trip-frequency rate; range ~2,100-4,700, softest estimate of the four) | Pago Móvil — ~7,000 tx/minute nationally, 20M+ affiliated customers | ~$915 (Yango's own published ranges) | ~$0.50-$5.80 | **~$9.4M/year** (revised from "Not modeled"; range ~$6.3M-$14.2M/year) |

Sum of modeled TAM (CO+PE+BO): **~$332M/year**, drivers **~162,000+**. These are the totals the rest of the Yango deck (executive summary, "The Opportunity," and the levers slide) should be reconciled to — see `claude-design-prompt-deck-reconciliation-2026-08-18.md`.

Sum of ALL FOUR including Venezuela's rough model: **~$341M/year**, drivers **~165,100+**. Keep Venezuela's contribution called out separately wherever this total is shown, its confidence level is materially lower than the other three countries and it should not be silently blended into a single headline number without that caveat visible.

---

## PER-COUNTRY DEEP-DIVE DATA

### 1. 🇨🇴 Colombia

**Yango scale:**
- 120,000+ drivers receiving instant payouts via Cobre's Fast Pay (La República, 2026-05-29; corroborated by DPL News, mobiletime.la, Gerencia y Negocios, same date)
- 1.5 million+ Colombians use the app weekly or monthly (Portafolio, 2026-03-11; same figure repeated by Infobae, 2025-12-19)
- ~38% share of Colombia's 23.6M mobility-app downloads in 2025 (Portafolio, 2026-03-11)
- Operates in Bogotá, Medellín, Cali, Barranquilla, Bucaramanga, Cúcuta (Portafolio, 2026-03-11)
- Commission ≤14% in most developed cities, self-reported, vs. 20-30% for competitors (Infobae, 2025-12-19)
- Competitive context: inDrive Colombia has 300,000+ active drivers (Forbes Colombia, 2026-04-27), roughly 2.5x Yango's confirmed driver count — useful scale framing, not a Yango figure.

**Payment methods:**
- PSE: 487M transactions in H1 2026 (+12% YoY), 35,000+ integrated companies (La República, 2026-08-04); 63.9% of Colombia's digital-payment transactions in Q2 2025 (CCCE, via areacucuta.com)
- Bre-B: 34,897,402 registered users at the 6-month mark (Banco de la República, 2026-04-06); 108M registered "keys" (not unique users) by 2026-06-30, up to ~5M transactions/day (Banco de la República indicators dashboard)
- Nequi: 28M users at its 10th anniversary (Infobae, 2026-05-22)
- Daviplata: 18.5M users (2024 figure, Yahoo Finance/La República); ~19-20.5M reported for 2025 (moderate confidence)

**ARPU / ticket:**
- No Yango-specific average driver earnings exist publicly (Yango's own "up to $2.3M COP/month" is a recruiting ceiling, not an average)
- Industry proxy used: DiDi Colombia net monthly income $1.8M-$4.2M COP (cuantomecuesta.com, 2026-05); gross-equivalent midpoint used for ARPU ≈ $1,438 USD/month at COP 3,128.65/USD (TRM, 2026-08-17)
- Avg ticket: Uber Colombia typical mid-range fare ~$25,000 COP ≈ $7.99 (cuantomecuesta.com, Apr 2026); head-to-head single-trip test (Pulzo, 2025-03-05) showed Uber $5.15 / DiDi $6.97 / Yango $0.99 (new-user promo, not representative)

**PSP / MoR landscape:** Wompi (Bancolombia, confirmed Bre-B dispersal support), PayU (strongest multi-country volume), ePayco (cash + PSE, SME-focused), dLocal (confirmed PSE + Nequi support), Kushki (self-reported "&gt;70% approval rate" — vendor marketing claim, general LatAm not Colombia-specific, low confidence). No independently-verified, Colombia-specific approval-rate percentage exists for any of them. The one usable market-level point: PPRO's Colombia page states local acquiring is "the single most important factor in improving authorisation rates" for Colombian-issued cards, without giving a number.

**Sources:** La República, Portafolio, Infobae, Forbes Colombia, Banco de la República, CCCE, PPRO, cuantomecuesta.com, Pulzo. **TO VALIDATE:** actual Yango driver count and top-up amounts, actual commission-rate application across cities, PSE/Bre-B/Nequi share specifically among Yango's own driver base.

---

### 2. 🇵🇪 Peru

**Yango scale:**
- No absolute driver or rider count published. Growth signals: ~15% user-base growth and 30-35% active-driver growth Jan-Apr 2026, &gt;25% full-year growth projected (Gestión, 2026-05-12)
- Mototaxi segment: 200,000+ weekly trips, &gt;50% Q1 2026 growth (Gestión, 2026-05-12)
- Yego (Yango's Peru vehicle-financing affiliate): ~15,000 active vehicle units (Gestión, 2025-12-02) — used here as the best available driver-base proxy, though it is a financing-program subset, not Yango's total active driver count
- Context: Lima's total taxi driver market across all platforms (formal + informal) is ~600,000 (Gestión, 2025-12-02)
- Yango added Yape as an in-app payment method during 2026 (Comunidaria.com, 2026-08-15) — a live signal Yango is actively investing in Peru's local-method coverage right now

**Payment methods:**
- Yape: 16.4M MAU as of Q1 2026 close, official Credicorp release (grupocredicorp.com, ~2026-05-15; corroborated by Infomercado, 2026-05-18)
- Plin: 2.6M MAU (IFS/Interbank, 2026-04-16), each user's operations grew 33% YoY
- Combined Yape+Plin QR transactions grew 82% Jan 2024-Apr 2026 within Niubiz's own processed volume (Perupayments.com, ~June 2026)
- PagoEfectivo: Paysafe launched its first LatAm digital wallet in Peru in July 2025 (Paysafe press release); no current user/volume figure found

**ARPU / ticket:**
- No Yango-specific figure. Industry proxy: DiDi Peru ~S/5,700/month gross (Naran.blog, Aug 2026) ≈ $1,665 USD/month at PEN 3.4230/USD (BCRP official close, 2026-08-05)
- Avg ticket: UberX Lima minimum fare S/12 ≈ $3.51 (third-party fare-estimator site, undated — **low confidence, no official Uber/Yango pricing source found**)

**PSP / MoR landscape:** Izipay (BCP-affiliated, qualitative edge on Visa approval via direct processing, no numeric rate published), Niubiz (largest multi-brand acquirer — S/75,000M processed across 632M transactions in 2024, Gestión 2025-04-21; qualitative "structural advantage in approval rate for Peruvian Visa cards," no number given), Culqi (Credicorp; flagged in comparison blogs as weaker specifically for internationally-issued cards, no number), dLocal (2.99% card fee, dLocal Go pricing PDF). The only actual numeric approval-rate figure found for Peru is **Kushki's self-reported "&gt;85% approval rate," but it is from H1 2023** (Revista Economía, 2023-08-16) — three years stale, do not present as current. A general market rule-of-thumb ("the standard in Peru is 80%") appears in a 2020/2023-dated blog (Apurata) — also dated, use only as a rough historical anchor.

**Sources:** Gestión, Credicorp/grupocredicorp.com, Infomercado, Ecommercenews.pe, Naran.blog, BCRP, Niubiz/Gestión, Revista Economía. **TO VALIDATE:** total Yango Peru driver count beyond the Yego proxy, actual average top-up amount, current (2025-2026) approval rates for Izipay/Culqi/Niubiz.

---

### 3. 🇧🇴 Bolivia

**Yango scale:**
- Bolivia is Yango's #3 global traffic source (9.68% of yango.com's total site traffic, behind only Egypt and UAE — Similarweb, re-confirmed 2026-08-18)
- Yango Bolivia's own country manager states "nearly 1 million monthly active users," ~10% of Bolivia's population, described as "4x larger than competitors" (estrategiabolivia.com, 2025-03-17) — this is a company claim covering riders + drivers combined, not a driver count
- $25M+ invested over ~3 years of operations (same interview)
- Driver counts (fragmented, dated): 14,000 active drivers nationwide as of 2023 (Delta Financiero/economy.com.bo, 2023-05-19 — the only nationwide figure found, likely stale); Cochabamba alone: 700,000+ trips/month, 100,000+ active users, 4,000 affiliated drivers (emprendimientosbolivia.com, 2026); Santa Cruz is Yango's largest market nationally at ~4M trips/month
- Bolivia is explicitly described by Yango as a market it is positioning as a Latin America hub, and was Yango's first LatAm market

**Payment methods:**
- QR Simple: 891M transactions moving US$51.293 billion in 2025, 94% of all interbank electronic fund-transfer orders (Red Uno, 2026-02-12; corroborated by Correo del Sur and Los Tiempos); value doubled 2024→2025 (US$22.5B → US$51.3B)
- 88.4% of QR transactions are under Bs 500, 49.7% under Bs 50 — QR Simple is overwhelmingly a small-ticket rail, directly relevant to driver top-ups
- Cash share fell from 85% (2020) to 64% (2025) (La Razón, May 2026)
- USDT: traded at a 35% premium to the official rate pre-unification (Bs 9.38 vs. Bs 6.86, criptonoticias.com, 2026-03-23); Banco Bisa launched USDT custody in Oct 2024, the first Bolivian bank to do so
- Peso + Yango Food: USDT payments went live inside Yango Food via Peso across 2,000+ restaurants on 2026-08-14 (Tether-confirmed, criptonoticias.com/cryptobriefing.com)
- Tigo Money: 3,500+ cash-in/cash-out points nationally, no public user count found

**Exchange-rate note (material to any USD figure in Bolivia):** Bolivia unified its exchange rate on 2026-06-26 (BCB Resolution 245), ending a 15-year fixed peg of Bs 6.96/USD and floating the rate, which opened at Bs 9.73 (a reported 43.10% devaluation). As of 2026-08-18 the official rate is Bs 11.56/USD and the parallel/USDT rate has converged to within roughly 1-6% of official — a dramatic change from the pre-unification gap, which exceeded 35% and at its peak reached Bs 17.8. **Use ~Bs 11.5/USD for all conversions below; the old 6.96 peg is obsolete and would overstate USD values.**

**ARPU / ticket:**
- No Yango-specific or Bolivia-specific driver-earnings figure exists. Derived instead from two real, sourced Bolivia data points: Cochabamba's 700,000+ trips/month ÷ 4,000 drivers = ~175 trips/driver/month; Yango's own published fare range (Bs 4-10 depending on city/tier) midpoint ≈ Bs 7 ≈ $0.61 at today's rate. 175 trips × $0.61 ≈ **$107/month ARPU proxy** — Bolivia-specific, though a derived estimate, not a directly reported figure.
- Avg ticket: Yango's own minimum fares — Economy from Bs 4, Comfort from Bs 7, Moto from Bs 3 (search-aggregated from Yango city pages); midpoint Bs 7 ≈ **$0.61** at today's rate.

**REVISED driver count (2026-08-18 cross-check, replaces the flat 14,000 nationwide figure):** the 14,000-nationwide figure (2023) is internally inconsistent with a second, more current, real data point already in this brief: Santa Cruz alone moves ~4,000,000 trips/month (Section: Yango scale, above), Yango's largest Bolivia market. Applying the same trips-per-driver ratio derived from Cochabamba (175 trips/driver/month) to Santa Cruz implies **~22,900 drivers in Santa Cruz alone** (4,000,000 ÷ 175), which already exceeds the entire 14,000-nationwide figure used previously. Adding Santa Cruz (~22,900, derived) to Cochabamba's confirmed 4,000 gives **~27,000 drivers as a floor**, excluding La Paz/El Alto entirely (no current trip-volume figure found for those cities, so this floor is conservative, not inflated). **Use ~27,000+ as the modeled Bolivia driver count going forward, not 14,000.** The ARPU proxy ($107/month) does not change, since it uses the same underlying per-driver trip rate that produced this revised count.
- **Revised modeled TAM: 27,000 drivers × $107/month ARPU × ~15% commission (still unconfirmed for Bolivia) × 12 = ~$5.2M/year**, roughly double the previous $2.7M figure, and still likely conservative since La Paz/El Alto are excluded.

**PSP / MoR landscape:** No provider in Bolivia has any publicly disclosed approval-rate percentage — this is a genuine, notable data gap (Bolivia is essentially absent from global PSP benchmarking reports like PPRO, EBANX, and Nilson). The real, sourced acceptance-relevant finding is qualitative but striking: Red Enlace's general manager confirmed via ASOFIN that dollar-related card restrictions caused **card-based dollar consumption to fall ~40%** (2025-09-19), while QR Simple now carries 92-94% of digital payments — i.e., cards are actively losing share to QR and stablecoin rails, not gaining it. Relevant providers: **Peso** (the only vendor with a confirmed relationship to Yango specifically — live inside Yango Food since 2026-08-14, no public volume/user data), **Red Enlace** (the interbank switch behind QR Simple, no merchant/cardholder fee), **Tigo Money** (telco wallet, 3,500+ points, no user count found).

**Sources:** Similarweb, estrategiabolivia.com, economy.com.bo, emprendimientosbolivia.com, Red Uno, Correo del Sur, Los Tiempos, criptonoticias.com, Banco Central de Bolivia, ASOFIN, Red Enlace. **TO VALIDATE:** a current (2026) total driver count nationwide — the 14,000 figure is 2023-vintage and almost certainly stale given Yango's stated 3-year, $25M investment since then; actual average recharge amount; Peso's transaction volume with Yango specifically.

---

### 4. 🇻🇪 Venezuela

**Yango scale:**
- Confirmed active, Caracas-only. Launched July/August 2025 via partnership with/absorption of BipBip, a pre-existing local ride-hailing app (elnacional.com, meridiano.net, caracasdigital.com, Aug 2025)
- At the 100-day mark (Nov 6, 2025): "hundreds of thousands" of passengers mobilized (Yango's own deliberately imprecise figure, bancaynegocios.com), 11M+ km covered in Caracas and satellite cities
- Driver-to-user ratio flagged by local press as unusually oversupplied relative to Yango's typical 15:1 ratio in other markets (bancaynegocios.com, 2025-11-06) — exact absolute driver count NOT FOUND
- Driver mix: 40% full-time / 60% part-time; 60% of the fleet is motorcycles
- Expansion beyond Caracas (Valencia, Maracaibo, Barquisimeto) is a stated goal, not yet launched
- Notable payments fact: Yango launched cash-to-driver only; online methods (Pago Móvil, direct debit, three separate bank "payment buttons" from Banco de Venezuela, BNC, and Bancamiga) were only added starting ~2025-08-05, each integrated separately — a live, current example of exactly the fragmented, one-vendor-per-bank pattern an orchestrator solves

**Payment methods:**
- Pago Móvil: ~6,000 interbank transactions/minute (Últimas Noticias, 2025-09-30), grown to ~7,000/minute in 2026 (La Prensa de Monagas, 2026-06-12); &gt;20M affiliated customers, &gt;86% banking penetration; Venezuela ranks 2nd globally in immediate-payment processing speed after Brazil
- USDT/crypto: Venezuela ranks 18th globally (9th population-adjusted) on Chainalysis's 2025 Global Crypto Adoption Index; ~80% of Venezuelan oil exports now settle in USDT (elucabista.com, 2025-11-14); the bolívar is the most actively-traded fiat currency on Binance P2P globally (criptonoticias.com, 2026-01-22)
- Zelle: widely and repeatedly described as the preferred method for receiving USD from abroad, but **no user-count or penetration percentage exists anywhere — genuinely unsourceable**, confirmed as a real gap by this research pass, not an oversight

**ARPU / ticket (the strongest Yango-specific data of all four countries, because Yango disclosed it directly):**
- Car drivers, full-time: $1,000-$1,400/month; motorcycle drivers, full-time: $650-$800/month; car drivers, part-time: $350-$400/month (bancaynegocios.com, 2025-11-06, Yango's own 100-day report)
- Blended ARPU proxy (weighted 60% moto / 40% car, full-time baseline): 0.6×$725 + 0.4×$1,200 ≈ **$915/month**
- Ticket: Yango's own minimum fare from $0.50; a sample comparative trip (9km, Caracas) showed motorcycle $2.10 and economy car from $5.80 (motummagazine.com, Aug 2025). No blended average fare exists across all rides.

**REVISED (2026-08-18): a modeled driver count and TAM for Venezuela, built from Yango's own disclosed operating metric rather than left unmodeled.** No direct driver count exists for Venezuela, and "hundreds of thousands of riders in 100 days" is a deliberately vague company phrase, not a usable base (applying the 5:1 driver-to-rider oversupply ratio to it would imply 40,000-100,000+ drivers, which is wildly inconsistent with the distance-based method below and is NOT used here; do not use it). Instead, this uses the one concrete operating metric Yango did disclose: **11,000,000+ km driven in Caracas and satellite cities in the first 100 days** (bancaynegocios.com, 2025-11-06), divided by an assumed average trip distance, since no Venezuela-specific average-trip-distance figure exists. The only real distance data point available is the 9km sample comparison trip; a shorter 4km urban-hop assumption is used as a lower bound given the motorcycle-heavy (60%) fleet and Caracas's density. Trip frequency per driver uses the same cross-market proxy applied in Bolivia (175 trips/driver/month, derived from Cochabamba), since no Venezuela-specific rate exists either.
  - At 9km/trip: 11,000,000 ÷ 9 = 1,222,222 trips/100 days → ~366,667 trips/month → ÷175 = **~2,100 drivers**
  - At 4km/trip: 11,000,000 ÷ 4 = 2,750,000 trips/100 days → ~825,000 trips/month → ÷175 = **~4,700 drivers**
  - Midpoint (6km, used as the working estimate): **~3,100 drivers**
- **Modeled TAM at the midpoint: 3,100 drivers × $915/month ARPU × ~27.5% commission (25-30% range, moderate confidence, driver-community sourcing) × 12 = ~$9.4M/year**, with a range of **~$6.3M/year (2,100 drivers) to ~$14.2M/year (4,700 drivers)** depending on the trip-distance assumption.
- **This is the softest of the four country models** — it rests on one company-disclosed distance figure, an assumed (not sourced) average trip length, and a trip-frequency rate borrowed from Bolivia. Treat it as directional, not equivalent in confidence to Colombia, Peru, or the revised Bolivia figure.

**PSP / MoR landscape:** No approval-rate data exists for any provider covering Venezuela — a real and notable gap, consistent with the country's isolation from standard global card-network infrastructure (the bulk of domestic volume runs on Pago Móvil, cash and P2P crypto rather than card acquiring, which is where approval-rate data is normally published). **Stripe is confirmed not to support Venezuela at all.** Relevant local/adjacent providers: **Mega Soft** (20,000+ affiliated merchants, but its only transaction-volume figure is from 2020 and stale; supports Pago Móvil, cards, Zelle, and crypto via a Cryptobuyer partnership; no ride-hailing use case documented), **Zinli** (Panama-origin USD wallet, no Venezuelan bank account required, $500/month receive limit for basic verification, no ride-hailing use case documented), **Reserve/UglyCash** (exited Venezuela in July 2023 over AML/OFAC risk, relaunched under the UglyCash brand on 2026-07-31 — current scale unknown, its ~500K users/26K merchants figure is from before the 2023 exit and is stale).

**Sources:** elnacional.com, bancaynegocios.com, motummagazine.com, Últimas Noticias, La Prensa de Monagas, Chainalysis, criptonoticias.com, elucabista.com, Fortune, Yahoo Finance ES. **TO VALIDATE:** total driver count, blended average fare, current UglyCash scale post-relaunch, whether Yango's three separate bank "payment button" integrations are still separate or have since been consolidated.

---

## MERCHANT OF RECORD LANDSCAPE (Unlimit, Inswitch, and alternatives)

Yango's HQ team has a positive initial read on two vendors, Unlimit and Inswitch, for driver-recharge collection, and wants one option that covers all four target countries. Neither actually has a named, dedicated "Merchant of Record" product; both are positioned by themselves as a PSP (Unlimit) or an embedded-finance/BaaS platform (Inswitch), with MoR-like behavior as a side effect of their model rather than a purpose-built service. Country coverage, confirmed directly on each vendor's own site:

**Unlimit** (rebranded from Unlimint, May 2023; founded 2009; London HQ; ~500-585 employees across 16 offices; Tracxn lists it as unfunded/no public funding round): confirmed coverage in **Colombia and Peru only** (unlimit.com/coverage/latam lists 10 LatAm countries total, none of them Bolivia or Venezuela). Peru coverage is backed by a direct Visa/Mastercard Principal Membership acquiring license secured 2025-09-30. No gig-economy, marketplace, or ride-hailing case study or client reference found anywhere in public sources. No independently verified approval rate, uptime, or processing-volume figure exists; Trustpilot data was conflicting and unverifiable in this pass (do not cite a specific score).

**Inswitch** (founded 2002, Uruguayan-origin fintech with a US legal entity; acquired by TransNetwork May 2024; ~130-170 employees across 3 continents; funding not publicly disclosed): confirmed coverage in **Colombia, Peru, and Bolivia** (dedicated country pages on inswitch.com for all three, with named local partners — e.g. Bancolombia/PSE/Transfiya in Colombia, BCP/Yape/Plin in Peru, Banco Nacional/BISA/BCP in Bolivia). **Venezuela: inswitch.com/network-countries/venezuela returns a 404, and Venezuela is absent from Inswitch's own 17-country LatAm coverage list.** ⚠️ **Critical, unresolved finding: Inswitch publishes a case study titled "Yango Scales with Inswitch" (inswitch.com/case-studies/yango), describing payments/payouts orchestration, hosted checkout, digital wallets and compliance for what it calls a multi-country mobility platform. It does not name a legal entity or list countries, so it cannot be confirmed with certainty that this is the same Yango being pitched, but circumstantial evidence (matching brand, matching business model, Yango's own Peru/Venezuela driver-recruitment pages existing) makes it plausible. This must be verified directly with Yango's HQ team before this finding is used in any meeting — if confirmed, Inswitch is a known or existing vendor, not a blind comparison, and that materially changes deal strategy.**

**dLocal** (NASDAQ-listed, well-established LatAm payments company): explicitly and confirmedly states it "acts as the Merchant of Record in each country it operates in." Official coverage includes Colombia, Peru, and Bolivia (dedicated Bolivia market page exists); **Venezuela is absent from dLocal's official country list.** Its "dLocal for Platforms" product explicitly supports multi-seller onboarding, fund splitting, and combined pay-in/payout flows, i.e., a genuine structural match for a driver-payout/marketplace use case, closer than either Unlimit's or Inswitch's public materials suggest for their own products.

**EBANX**: confirmed as an MoR for at least some markets; official 15-country LatAm operating list includes Colombia, Peru, and a dedicated Bolivia country page; **Venezuela is absent from EBANX's official list** (loose secondary-source mentions exist but contradict EBANX's own published country list, do not use them).

**Paddle**: confirmed true MoR (tax calculation, collection and remittance for all supported countries); its South America country table includes Colombia, Peru, and Bolivia; **Venezuela is absent.** Built for digital goods/subscriptions, not a proven fit for a driver-payout/gig use case.

**Also researched, weaker fit**: **PayPal** is confirmed to be a PSP, not a Merchant of Record, despite sometimes being informally described as one (Stripe's and Paddle's own MoR-vs-PSP explainers both name PayPal alongside Stripe as PSP examples, not MoR examples); PayPal explicitly does not support Venezuela at all (no bank-transfer capability). **Rebill** (Argentina-founded, not Peru as sometimes assumed, $3.6M seed 2022 led by Tiger Global/YC) explicitly states on its own site that it does NOT assume merchant-of-record responsibility; confirmed Colombia and Peru coverage only, no Bolivia or Venezuela. **PayRetailers**: not branded as an MoR; confirmed Colombia and Peru coverage on its own site, no confirmed Bolivia or Venezuela despite some low-quality secondary mentions. **FastSpring, 2Checkout/Verifone, Nomupay, Corpay, Boku**: none has a confirmed, itemized coverage list for these four specific markets; Nomupay in particular appears to have no Latin America presence at all.

**The headline finding**: of every MoR/PSP candidate researched, including both vendors Yango's HQ already favors, **not one has confirmed coverage in Venezuela.** Bolivia is reasonably well covered (Inswitch, dLocal, EBANX, Paddle all confirm it; only Unlimit misses it). This means a single-vendor MoR strategy structurally cannot serve all four of Yango's LatAm markets today, regardless of which vendor HQ ultimately prefers between Unlimit and Inswitch.

**Why the MoR-vs-PSP distinction specifically matters here**: a Merchant of Record takes on tax collection/remittance, chargeback liability, and local compliance as the legal seller of the transaction; a plain PSP just moves the payment and leaves that liability with the merchant (Stripe's and Paddle's own explainer pages, 2026). This is unusually consequential for these four countries right now: Bolivia ended its 15-year fixed exchange-rate peg on 2026-06-26, devaluing the boliviano roughly 30-40% in a floating-rate transition (Rio Times, Central Banking, 2026); Venezuela is running 600%+ inflation (Trading Economics, Feb 2026 reading) and remains substantially cut off from global card networks and correspondent banking, a situation still unresolved as of this research despite the US capture of Nicolás Maduro on 2026-01-03 and the subsequent transition period (CSIS, USNI News, Jan 2026). An entity that absorbs FX conversion, settlement timing and local compliance risk is worth materially more in this environment than a processor that pushes that risk back onto Yango.

**Sources:** unlimit.com (coverage, press releases, about, offices pages), inswitch.com (network-countries pages, case-studies/yango, platform page), Tracxn, PitchBook, LatamList, PR Newswire (TransNetwork/Inswitch acquisition, 2024-05-15), Finextra, dlocal.com, EBANX business.ebanx.com, developer.paddle.com, Stripe and Paddle MoR-vs-PSP explainer pages, Rebill.com, PayRetailers.com, Rio Times Online, Central Banking, Trading Economics, CSIS, USNI News (2025-2026). **TO VALIDATE:** whether the Inswitch "Yango" case study refers to this exact prospect; current commercial terms, pricing and country-specific acquiring-license status for both Unlimit and Inswitch; independent, verified customer-review data for both (this pass found only conflicting, unverifiable figures).

---

## Closing note for the appendix cover slide

"Colombia, Peru, Bolivia and Venezuela are Yango's four LatAm driver-recharge markets. Combined, the sourced and modeled opportunity across Colombia, Peru and Bolivia (the three markets with a usable driver-count anchor, Bolivia's revised 2026-08-18 to ~27,000+ drivers via a Santa Cruz trip-volume cross-check rather than the stale 2023 nationwide figure) is approximately $332M/year in recharge volume flowing through fragmented, market-by-market payment rails today, across roughly 162,000+ drivers. Venezuela could not be sized in dollars from public sources, and that absence is itself relevant: no processor publicly serving Venezuela discloses an approval rate, Stripe does not support the country at all, and Yango itself only added online payment methods a few days after its own 2025 launch, each bank integrated separately. All figures are Yuno's model outputs from public data, to be replaced with Yango's actual driver, recharge-volume and commission data in a joint data-validation sprint."