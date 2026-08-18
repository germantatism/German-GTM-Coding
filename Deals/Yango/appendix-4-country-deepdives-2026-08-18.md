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
| 3 | 🇧🇴 Bolivia | 14,000+ nationwide (2023, likely understates 2026 scale) | QR Simple — 94% of interbank electronic transfers | ~$107 (derived, Bolivia-specific) | ~$0.61 | **~$2.7M/year** (low confidence, likely understated) |
| 4 | 🇻🇪 Venezuela | Not found (qualitative: "hundreds of thousands" of riders in 100 days, oversupplied driver base) | Pago Móvil — ~7,000 tx/minute nationally, 20M+ affiliated customers | ~$915 (Yango's own published ranges) | ~$0.50-$5.80 | Not modeled — insufficient driver-count data |

Sum of modeled TAM (CO+PE+BO): **~$330M/year**. Venezuela intentionally excluded from the sum, not zeroed — see its slide.

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

**PSP / MoR landscape:** No approval-rate data exists for any provider covering Venezuela — a real and notable gap, consistent with the country's isolation from standard global card-network infrastructure (the bulk of domestic volume runs on Pago Móvil, cash and P2P crypto rather than card acquiring, which is where approval-rate data is normally published). **Stripe is confirmed not to support Venezuela at all.** Relevant local/adjacent providers: **Mega Soft** (20,000+ affiliated merchants, but its only transaction-volume figure is from 2020 and stale; supports Pago Móvil, cards, Zelle, and crypto via a Cryptobuyer partnership; no ride-hailing use case documented), **Zinli** (Panama-origin USD wallet, no Venezuelan bank account required, $500/month receive limit for basic verification, no ride-hailing use case documented), **Reserve/UglyCash** (exited Venezuela in July 2023 over AML/OFAC risk, relaunched under the UglyCash brand on 2026-07-31 — current scale unknown, its ~500K users/26K merchants figure is from before the 2023 exit and is stale).

**Sources:** elnacional.com, bancaynegocios.com, motummagazine.com, Últimas Noticias, La Prensa de Monagas, Chainalysis, criptonoticias.com, elucabista.com, Fortune, Yahoo Finance ES. **TO VALIDATE:** total driver count, blended average fare, current UglyCash scale post-relaunch, whether Yango's three separate bank "payment button" integrations are still separate or have since been consolidated.

---

## Closing note for the appendix cover slide

"Colombia, Peru, Bolivia and Venezuela are Yango's four LatAm driver-recharge markets. Combined, the sourced and modeled opportunity across Colombia and Peru alone (the two markets with a usable driver-count anchor) is approximately $327M/year in recharge volume flowing through fragmented, market-by-market payment rails today; Bolivia adds a smaller but real ~$2.7M/year on the only driver count publicly available, almost certainly an undercount of Yango's actual 2026 scale there. Venezuela could not be sized in dollars from public sources, and that absence is itself relevant: no processor publicly serving Venezuela discloses an approval rate, Stripe does not support the country at all, and Yango itself only added online payment methods a few days after its own 2025 launch, each bank integrated separately. All figures are Yuno's model outputs from public data, to be replaced with Yango's actual driver, recharge-volume and commission data in a joint data-validation sprint."