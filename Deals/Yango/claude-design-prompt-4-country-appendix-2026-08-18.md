# Prompt Claude Design: 4-Country Deep-Dive Appendix Slides for Yango (2026-08-18)

---

⚠️ **This replaces section 6.5 ("NEW: Country deep-dives") of the earlier prompt `claude-design-prompt-yango-deck-2026-08-16.md`.** That section built a lighter two-part slide per country (a methods table plus a short processor note). This version replaces those four slides with the full Suno-style deep-dive format below, same visual system as the rest of the Yango deck (which itself mirrors the Suno deck's design system — see `claude-design-prompt-20-country-appendix.md` for the reference layout this is built from). Everything else in the 2026-08-16 prompt (cover, "today" slide, opportunity slide, case studies, Yuno+Cobre section, other appendix sections) is unchanged.

You are adding 5 slides (1 divider + 4 country deep-dives) to the Yango deck, in the Appendix section, in this order: divider, Colombia, Peru, Bolivia, Venezuela.

## DESIGN RULES (ABSOLUTE)

1. Use the SAME design system as the rest of the Yango deck: same fonts, same blue/purple palette, same yuno logo top-right, same page-number bottom-left, same card/box styling used elsewhere in the deck.
2. Layout for each of the 4 country slides, top to bottom:
   - Small country flag emoji top-left, above the title.
   - Title in the deck's blue title style (1-2 lines): "{Country}: {headline}"
   - Full-width dark blue/purple stat bar, 4 cells side by side, each with: a large white/bold number, a label below it, a small sub-caption below that.
   - Below the stat bar, 3 side-by-side lever cards separated by a horizontal line with circled numbers (1, 2, 3) centered on the line. Each card: small caps label, then a large bold figure, then a blue line with the $ or % impact, then a one-line italic tactic.
   - Two-column row: LEFT = "PAYMENT METHOD PRIORITY" table (columns: Priority chip, Method, Scale/penetration, Role for Yango). RIGHT = "PSP / MoR LANDSCAPE" table (columns: Provider, Type, Est. acceptance rate, Note).
   - Full-width "SO WHAT" bar (light background, bold "SO WHAT" label, italic sentence).
   - Small grey footnote line at the very bottom: Source + "TO VALIDATE" clause.
3. US English. No em-dashes. No " - " as punctuation. Do not invent or alter any number below; use exactly what is given.
4. Every dollar figure below is a **modeled estimate**, not Yango's actual data. Wherever a cell shows a modeled or proxy number, keep the "(est.)" or "(industry proxy)" qualifier visible on the slide in small type, do not silently drop it to make the number look more authoritative.
5. Do not invent a specific numeric approval/acceptance rate for any named provider in any country. Where the PSP / MoR Landscape table has no public rate, the cell must say "No public data" rather than a blank or an invented percentage. Where a general market-level benchmark exists (e.g. a LatAm cross-border-vs-local-acquiring range, or a dated country-level figure), it may appear in the Note column, explicitly labeled with its source and, if dated, flagged as dated.
6. If any text overflows its box, shrink font size one step before truncating or dropping content.

## SHARED METHODOLOGY NOTE (put this once, on an appendix divider slide before the 4 country slides)

Divider slide title: "Appendix: Country Deep-Dives"
Body text: "Colombia, Peru, Bolivia and Venezuela are Yango's four LatAm driver-recharge markets. Modeled annual recharge-volume opportunity is built from each country's most recent public driver count (or the closest available proxy), an ARPU figure sourced from Yango's own disclosures where available or from comparable-platform driver economics where not, and Yango's own disclosed or estimated commission rate. No approval-rate percentage is invented for any processor; where no public rate exists, the slide says so. All figures are Yuno's model outputs from public data, to be replaced with Yango's actual driver, recharge-volume and commission data in a joint data-validation sprint."

---

## SLIDE 1: 🇨🇴 Colombia

Title: "Colombia: PSE carries the volume today, Bre-B is the fastest-growing rail to build for"

Stat bar (4 cells):
1. "120,000+" / "Yango drivers" / "Cobre payout integration, May 2026"
2. "63.9%" / "PSE share of digital payments" / "35,000+ integrated companies, H1 2026"
3. "~$1,438/mo" / "Avg. monthly driver revenue (ARPU, industry proxy)" / "DiDi Colombia driver economics, 2026 · avg ticket ~$8.00"
4. "~$290M/year" / "Est. annual recharge volume opportunity" / "Modeled: 120K drivers x ARPU x 14% commission x 12 (est.)"

Lever 1 COVERAGE EXPANSION: "Bre-B: 34.9M registered users at its 6-month mark" / "108M registered keys by mid-2026" / "Add Bre-B alongside PSE and Nequi so drivers aren't limited to a single bank-redirect flow"
Lever 2 APPROVAL & COST RECOVERY: "Local acquiring is the single lever that moves approval" / "PPRO: local acquiring materially outperforms cross-border for Colombian-issued cards" / "No Colombia-specific approval percentage is publicly disclosed by any processor; route locally by default"
Lever 3 RAIL MOMENTUM: "Nequi: 28M users at its 10-year mark" / "Daviplata: ~19-20.5M users" / "Both wallets are already mainstream for exactly this kind of frequent, small-value flow"

Payment method priority table:
| Priority | Method | Scale/penetration | Role for Yango |
| Must-have | PSE | 63.9% of digital payment transactions, 487M in H1 2026 | Primary bank-redirect rail today |
| Must-have | Nequi / Daviplata | 28M / ~19-20.5M users | Mobile-native, real-time, already used by Uber and DiDi for the same flow |
| Growing | Bre-B | 34.9M registered users at 6 months | Fastest-growing rail; recurring/pull collection still maturing |
| Weak fit | Cards | Low card penetration among Colombia's population vs. LatAm peers | Secondary only |

PSP / MoR landscape table:
| Provider | Type | Est. acceptance rate | Note |
| Wompi (Bancolombia) | PSP/gateway | No public data | Confirmed Bre-B dispersal support |
| PayU | PSP/gateway | No public data | Strongest for multi-country volume |
| ePayco | PSP/gateway | No public data | Cash + PSE, SME-focused |
| dLocal | PSP/gateway | No public data | Confirmed PSE + Nequi support |
| Kushki | PSP/gateway | "&gt;70%" (vendor's own claim, general LatAm, not Colombia-specific) | Self-reported marketing figure, not independently verified |

SO WHAT: "Colombia already has the driver base and the payout side solved via Cobre; the recharge side is a coverage problem (adding Bre-B alongside PSE and the wallets) more than an approval-rate problem, since no processor here publishes a rate worth optimizing against yet."

Footnote: "Source: La República, Portafolio, Infobae, Banco de la República, PPRO, cuantomecuesta.com (2026). Modeled TAM, not Yango's actual data. TO VALIDATE: actual driver count, actual average recharge amount, commission rate by city."

---

## SLIDE 2: 🇵🇪 Peru

Title: "Peru: Yape already carries the market, the driver base itself is the open question"

Stat bar (4 cells):
1. "15,000" / "Active vehicle units (Yego fleet-financing proxy)" / "Not Yango's total driver count; the only concrete figure available, Dec 2025"
2. "16.4M" / "Yape monthly active users" / "Credicorp, Q1 2026"
3. "~$1,665/mo" / "Avg. monthly driver revenue (ARPU, industry proxy)" / "DiDi Peru driver economics, Aug 2026 · avg ticket ~$3.50 (low confidence)"
4. "~$37M/year" / "Est. annual recharge volume opportunity (lower confidence)" / "Modeled: 15K vehicles x ARPU x 12.5% commission x 12 (est., proxy driver count)"

Lever 1 COVERAGE EXPANSION: "Yape 16.4M MAU + Plin 2.6M MAU" / "Combined QR transactions +82% Jan 2024-Apr 2026" / "Interoperable since 2023; matches the frequent, small-value top-up profile closely"
Lever 2 APPROVAL & COST RECOVERY: "No current, provider-specific approval rate is public for Peru" / "Kushki self-reported &gt;85% is from H1 2023, three years stale" / "Treat any approval claim in this market as dated until re-verified"
Lever 3 DRIVER-BASE VISIBILITY: "No audited total Yango driver count exists in Peru" / "Only growth rates (+30-35% active drivers, Jan-Apr 2026) are public" / "This is itself a discovery-call question, not a gap to paper over with an invented number"

Payment method priority table:
| Priority | Method | Scale/penetration | Role for Yango |
| Must-have | Yape + Plin | 16.4M + 2.6M MAU, interoperable since 2023 | Matches the frequent, small-value driver top-up profile closely |
| Weak fit | PagoEfectivo | New wallet launched Jul 2025, no current user data | Voucher-based legacy, requires a physical cash step |
| Weak fit | Cards | Peru remains cash-heavy | Secondary only |

PSP / MoR landscape table:
| Provider | Type | Est. acceptance rate | Note |
| Izipay (BCP) | PSP/acquirer | No public data | Qualitative edge on Visa via direct processing, no number published |
| Niubiz | PSP/acquirer | No public data | Largest multi-brand acquirer, S/75,000M processed in 2024 |
| Culqi (Credicorp) | PSP/gateway | No public data | Flagged as weaker for internationally-issued cards, no number published |
| dLocal | PSP/gateway | No public data | 2.99% card processing fee |
| Kushki | PSP/gateway | "&gt;85%" (H1 2023, stale) | Do not present as current without re-verification |

SO WHAT: "Peru's payment-method side is the most mature of the four markets, Yape and Plin already cover the driver top-up profile well; what's missing is Yango's own driver-count visibility, which matters more here than any processor comparison."

Footnote: "Source: Gestión, Credicorp, Ecommercenews.pe, Naran.blog, BCRP, Niubiz/Gestión, Revista Economía (2025-2026). Modeled TAM uses a fleet-financing proxy, not a confirmed driver count. TO VALIDATE: total Yango Peru driver count, actual average top-up amount, current Izipay/Culqi/Niubiz approval rates."

---

## SLIDE 3: 🇧🇴 Bolivia

Title: "Bolivia: Yango's biggest market outside Egypt and the UAE, and cards are already losing to QR"

Stat bar (4 cells):
1. "14,000+" / "Yango drivers nationwide" / "2023 figure, likely understates 2026 scale"
2. "94%" / "of interbank transfers run through QR Simple" / "891M transactions, US$51.3B moved in 2025"
3. "~$107/mo" / "Avg. monthly driver revenue (ARPU, derived)" / "Cochabamba trips-per-driver x Yango's own fare range · avg ticket ~$0.61"
4. "~$2.7M/year" / "Est. annual recharge volume opportunity (likely understated)" / "Modeled: 14K drivers x ARPU x ~15% commission x 12 (est., commission rate unconfirmed for Bolivia)"

Lever 1 SCALE CONTEXT: "9.68% of Yango's global site traffic, #3 market after Egypt and UAE" / "Yango's own country manager: ~1M monthly active users, ~10% of Bolivia's population" / "Materially larger than the 14,000-driver figure alone suggests"
Lever 2 RAIL SHIFT ALREADY HAPPENING: "Card-based dollar consumption fell ~40%" / "confirmed via ASOFIN/Red Enlace, Sept 2025" / "Cards are losing share to QR and stablecoins, not gaining it; build for that shift, don't fight it"
Lever 3 STABLECOIN BRIDGE ALREADY LIVE: "Peso x Yango Food went live Aug 14, 2026" / "USDT payments across 2,000+ restaurants" / "The precedent for a USDT bridge already exists inside Yango's own Bolivia stack"

Payment method priority table:
| Priority | Method | Scale/penetration | Role for Yango |
| Must-have | QR Simple | 94% of interbank electronic transfers, no fee, interoperable across all banks | Dominant small-ticket rail, directly matches the recharge use case |
| Must-have | USDT/stablecoin | Already in production at Yango Food via Peso | Dollar-liquidity hedge, precedent already exists inside Yango |
| Declining | Cash | 64% of payments in 2025, down from 85% in 2020 | Still dominant but falling fast |

PSP / MoR landscape table:
| Provider | Type | Est. acceptance rate | Note |
| Peso | Fintech/USDT bridge | No public data | Only vendor with a confirmed relationship to Yango specifically |
| Red Enlace | Interbank QR switch | No public data | Operates QR Simple, no merchant/cardholder fee |
| Tigo Money | Telco wallet | No public data | 3,500+ cash-in/cash-out points, no user count found |

SO WHAT: "Bolivia is quietly Yango's biggest LatAm market by traffic, and the region's most underserved by global payments research, no processor here discloses an approval rate, but the real story is that cards are already losing 40% of dollar-linked volume to QR and stablecoins, exactly where an orchestrator adds the most value."

Footnote: "Source: Similarweb, estrategiabolivia.com, Red Uno, Correo del Sur, Los Tiempos, criptonoticias.com, Banco Central de Bolivia, ASOFIN, Red Enlace (2025-2026). Modeled TAM likely understates 2026 scale; the 14,000-driver figure is 2023-vintage. TO VALIDATE: current total driver count, actual recharge amount, Peso's transaction volume with Yango."

---

## SLIDE 4: 🇻🇪 Venezuela

Title: "Venezuela: no global PSP covers this market at all, and Yango is building it bank by bank"

Stat bar (4 cells):
1. "Not found" / "Total driver count" / "Only qualitative: \"hundreds of thousands\" of riders in 100 days, driver base oversupplied vs. Yango's other markets"
2. "~7,000/min" / "Pago Móvil transactions nationally" / "20M+ affiliated customers, 86%+ banking penetration, 2026"
3. "~$915/mo" / "Avg. monthly driver revenue (Yango's own published ranges)" / "Blended, 60% moto / 40% car fleet mix · avg ticket ~$0.50-$5.80"
4. "Not modeled" / "Est. annual recharge volume opportunity" / "No defensible driver count exists to size this in dollars"

Lever 1 DAY-ONE FRAGMENTATION, LIVE RIGHT NOW: "Cash-only at launch, online methods added ~5 days later" / "Three separate bank \"payment buttons\" (Banco de Venezuela, BNC, Bancamiga)" / "This is the exact one-integration-per-bank pattern an orchestrator replaces, happening today, not hypothetically"
Lever 2 ZERO GLOBAL PSP COVERAGE: "Stripe confirmed not to support Venezuela at all" / "No approval-rate data exists for any provider covering the country" / "Whoever builds a real rail here first has no incumbent to displace"
Lever 3 DOLLARIZATION IS ALREADY THE DEFAULT: "~80% of oil exports settle in USDT" / "Bolívar is the most-traded fiat pair on Binance P2P globally" / "The market has already moved to dollar/stablecoin rails at the sovereign level, retail is following"

Payment method priority table:
| Priority | Method | Scale/penetration | Role for Yango |
| Must-have | Pago Móvil | ~7,000 tx/minute, 20M+ affiliated customers | Dominant, instant, no card needed, the standard for exactly this flow |
| Good, currency hedge | USDT/crypto | Venezuela ranks 18th globally (9th population-adjusted) on crypto adoption | Under 1% transfer cost, hedges hyperinflation |
| Weaker fit | Zelle | No quantified user base, genuinely unsourceable | More common for remittances than routine local payments, needs USD access |

PSP / MoR landscape table:
| Provider | Type | Est. acceptance rate | Note |
| Mega Soft | Local processor | No public data | 20,000+ merchants; transaction-volume data is from 2020, stale; no ride-hailing use case documented |
| Zinli | USD wallet | No public data | No Venezuelan bank account required; $500/month receive limit; no ride-hailing use case documented |
| Reserve / UglyCash | Crypto/USD wallet | No public data | Exited Venezuela in 2023 over AML/OFAC risk, relaunched July 2026; current scale unknown |

SO WHAT: "Venezuela is the weakest-evidence market of the four, and that absence is itself the finding: no global PSP covers it, no processor discloses an approval rate, and Yango's own online-payments rollout is three separate bank integrations bolted on five days after cash-only launch."

Footnote: "Source: elnacional.com, bancaynegocios.com, motummagazine.com, Últimas Noticias, Chainalysis, criptonoticias.com, elucabista.com (2025-2026). No dollar opportunity is modeled here, the driver-count data does not support one. TO VALIDATE: total driver count, blended average fare, whether the three bank integrations are still separate."

---

## WHAT NOT TO DO

- Do not modify any other slide in the deck outside this new appendix section.
- Do not invent or round any number differently than given above.
- Do not invent a specific numeric approval/acceptance rate for any named provider. Every "No public data" cell must stay as-is; do not fill it in to make the table look more complete.
- Do not model a dollar TAM for Venezuela. The slide explicitly says "Not modeled" for a reason, there is no defensible driver count to build one from.
- Do not drop the "(est.)," "(industry proxy)," "(derived)," or "(lower confidence)" qualifiers from any stat bar cell or lever card, they are load-bearing, not decorative.
- Do not carry over the lighter Colombia/Peru/Bolivia/Venezuela slides from section 6.5 of the 2026-08-16 prompt, these 5 slides replace them entirely.
- Keep all 4 country slides visually identical to each other in layout, differing only in content.
