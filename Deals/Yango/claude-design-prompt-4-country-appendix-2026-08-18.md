# Prompt Claude Design: 4-Country Deep-Dive Appendix Slides for Yango (2026-08-18)

---

⚠️ **This replaces section 6.5 ("NEW: Country deep-dives") of the earlier prompt `claude-design-prompt-yango-deck-2026-08-16.md`.** That section built a lighter two-part slide per country (a methods table plus a short processor note). This version replaces those four slides with the full Suno-style deep-dive format below, same visual system as the rest of the Yango deck (which itself mirrors the Suno deck's design system — see `claude-design-prompt-20-country-appendix.md` for the reference layout this is built from). Everything else in the 2026-08-16 prompt (cover, "today" slide, opportunity slide, case studies, Yuno+Cobre section, other appendix sections) is unchanged.

You are adding 6 slides (1 divider + 4 country deep-dives + 1 Merchant of Record comparison) to the Yango deck, in the Appendix section, in this order: divider, Colombia, Peru, Bolivia, Venezuela, The Merchant of Record.

## DESIGN RULES (ABSOLUTE)

1. Use the SAME design system as the rest of the Yango deck: same fonts, same blue/purple palette, same yuno logo top-right, same page-number bottom-left, same card/box styling used elsewhere in the deck.
2. Layout for each of the 4 country slides, top to bottom:
   - Small country flag emoji top-left, above the title.
   - Title in the deck's blue title style (1-2 lines): "{Country}: {headline}"
   - Full-width dark blue/purple stat bar, 4 cells side by side, each with: a large white/bold number, a label below it, a small sub-caption below that.
   - Below the stat bar, 3 side-by-side lever cards separated by a horizontal line with circled numbers (1, 2, 3) centered on the line. Each card: small caps label, then a large bold figure, then a blue line with the $ or % impact, then a one-line italic tactic.
   - Two-column row: LEFT = "PAYMENT METHOD PRIORITY" table (columns: Priority chip, Method, Scale/penetration, Role for Yango). RIGHT = "TOP-PERFORMING PSPs / MoRs" table (columns: Rank, Provider, Type, Why it ranks here), ordered best to worst.
   - Full-width "SO WHAT" bar (light background, bold "SO WHAT" label, italic sentence).
   - Small grey footnote line at the very bottom: Source + "TO VALIDATE" clause.
3. US English. No em-dashes. No " - " as punctuation. Do not invent or alter any number below; use exactly what is given.
4. Every dollar figure below is a **modeled estimate**, not Yango's actual data. Wherever a cell shows a modeled or proxy number, keep the "(est.)" or "(industry proxy)" qualifier visible on the slide in small type, do not silently drop it to make the number look more authoritative.
5. **No processor gets a numeric approval/acceptance-rate percentage anywhere on these slides, not even a vendor's own self-reported one.** Rank providers instead by confirmed, sourced performance signals: transaction/merchant volume actually processed, confirmed support for the market's must-have local methods, and any confirmed direct relationship with Yango. The "Why it ranks here" column must cite one of those concrete, sourced reasons, never a percentage.
6. If any text overflows its box, shrink font size one step before truncating or dropping content.
7. **Slide 6 ("The Merchant of Record") is a comparative synthesis slide, not a country slide, and uses a different layout** — see its own section below instead of the 4-cell-stat-bar-plus-3-levers structure. Keep the same fonts, palette, logo and footnote treatment as the rest of the deck, but let the content (a wide comparison table plus two supporting boxes) drive the layout. If it doesn't fit on one slide at a legible size, split it into a 6 and 6b pair rather than shrinking text below the deck's normal minimum size.

## SHARED METHODOLOGY NOTE (put this once, on an appendix divider slide before the 4 country slides)

Divider slide title: "Appendix: Country Deep-Dives"
Body text: "Colombia, Peru, Bolivia and Venezuela are Yango's four LatAm driver-recharge markets. Modeled annual recharge-volume opportunity is built from each country's most recent public driver count (or the closest available proxy), an ARPU figure sourced from Yango's own disclosures where available or from comparable-platform driver economics where not, and Yango's own disclosed or estimated commission rate. Combined across Colombia, Peru and Bolivia this totals roughly $332M/year in recharge volume across ~162,000+ drivers, revised 2026-08-18; Venezuela's driver base could not be sized and is not included. No processor on these slides carries an approval or acceptance-rate percentage, including vendors' own self-reported figures; each market's PSPs and MoRs are ranked instead by confirmed transaction/merchant volume, confirmed support for that market's must-have local payment methods, and any confirmed direct relationship with Yango. All figures are Yuno's model outputs from public data, to be replaced with Yango's actual driver, recharge-volume and commission data in a joint data-validation sprint."

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

Top-performing PSPs / MoRs table (ranked best to worst):
| Rank | Provider | Type | Why it ranks here |
| 1 | Wompi (Bancolombia) | PSP/gateway | Only provider with confirmed Bre-B dispersal support, backed by Colombia's largest bank |
| 2 | PayU | PSP/gateway | Broadest confirmed multi-country LatAm processing volume |
| 3 | dLocal | PSP/gateway | Confirmed PSE + Nequi support, established LatAm-wide local-acquiring specialist |
| 4 | ePayco | PSP/gateway | Cash + PSE coverage, SME-focused, useful for smaller-city drivers |

SO WHAT: "Colombia already has the driver base and the payout side solved via Cobre; the recharge side is a coverage problem, adding Bre-B alongside PSE and the wallets, more than a which-processor-wins problem, since ranking here comes down to confirmed local-rail support, not a published performance number."

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
Lever 2 PROCESSOR SELECTION BY CONFIRMED SCALE: "Niubiz processed S/75,000M across 632M transactions in 2024" / "the clearest scale signal among Peru's PSPs" / "Rank by confirmed volume and local-method support, not by unverifiable performance claims"
Lever 3 DRIVER-BASE VISIBILITY: "No audited total Yango driver count exists in Peru" / "Only growth rates (+30-35% active drivers, Jan-Apr 2026) are public" / "This is itself a discovery-call question, not a gap to paper over with an invented number"

Payment method priority table:
| Priority | Method | Scale/penetration | Role for Yango |
| Must-have | Yape + Plin | 16.4M + 2.6M MAU, interoperable since 2023 | Matches the frequent, small-value driver top-up profile closely |
| Weak fit | PagoEfectivo | New wallet launched Jul 2025, no current user data | Voucher-based legacy, requires a physical cash step |
| Weak fit | Cards | Peru remains cash-heavy | Secondary only |

Top-performing PSPs / MoRs table (ranked best to worst):
| Rank | Provider | Type | Why it ranks here |
| 1 | Niubiz | PSP/acquirer | Largest multi-brand acquirer in Peru, S/75,000M processed across 632M transactions in 2024 |
| 2 | Izipay (BCP) | PSP/acquirer | Direct-processing edge for Visa via its BCP/VisaNet lineage |
| 3 | dLocal | PSP/gateway | Established LatAm-wide local-acquiring specialist, 2.99% card fee |
| 4 | Culqi (Credicorp) | PSP/gateway | Confirmed Yape + Plin + PagoEfectivo support, though weaker specifically for internationally-issued cards |

SO WHAT: "Peru's payment-method side is the most mature of the four markets, Yape and Plin already cover the driver top-up profile well; what's missing is Yango's own driver-count visibility, which matters more here than any processor comparison."

Footnote: "Source: Gestión, Credicorp, Ecommercenews.pe, Naran.blog, BCRP, Niubiz/Gestión, Revista Economía (2025-2026). Modeled TAM uses a fleet-financing proxy, not a confirmed driver count. TO VALIDATE: total Yango Peru driver count, actual average top-up amount, current Izipay/Culqi/Niubiz approval rates."

---

## SLIDE 3: 🇧🇴 Bolivia

Title: "Bolivia: Yango's biggest market outside Egypt and the UAE, and cards are already losing to QR"

Stat bar (4 cells):
1. "~27,000+" / "Yango drivers nationwide (revised)" / "Derived from Santa Cruz's own 4M trips/month + Cochabamba's confirmed 4,000; supersedes a stale 2023 figure"
2. "94%" / "of interbank transfers run through QR Simple" / "891M transactions, US$51.3B moved in 2025"
3. "~$107/mo" / "Avg. monthly driver revenue (ARPU, derived)" / "Cochabamba trips-per-driver x Yango's own fare range · avg ticket ~$0.61"
4. "~$5.2M/year" / "Est. annual recharge volume opportunity (revised, still a floor)" / "Modeled: 27K drivers x ARPU x ~15% commission x 12 (est., commission rate unconfirmed for Bolivia; La Paz/El Alto excluded)"

Lever 1 SCALE CONTEXT: "9.68% of Yango's global site traffic, #3 market after Egypt and UAE" / "Yango's own country manager: ~1M monthly active users, ~10% of Bolivia's population" / "Santa Cruz alone implies ~22,900 drivers by trip volume, already above the old nationwide figure"
Lever 2 RAIL SHIFT ALREADY HAPPENING: "Card-based dollar consumption fell ~40%" / "confirmed via ASOFIN/Red Enlace, Sept 2025" / "Cards are losing share to QR and stablecoins, not gaining it; build for that shift, don't fight it"
Lever 3 STABLECOIN BRIDGE ALREADY LIVE: "Peso x Yango Food went live Aug 14, 2026" / "USDT payments across 2,000+ restaurants" / "The precedent for a USDT bridge already exists inside Yango's own Bolivia stack"

Payment method priority table:
| Priority | Method | Scale/penetration | Role for Yango |
| Must-have | QR Simple | 94% of interbank electronic transfers, no fee, interoperable across all banks | Dominant small-ticket rail, directly matches the recharge use case |
| Must-have | USDT/stablecoin | Already in production at Yango Food via Peso | Dollar-liquidity hedge, precedent already exists inside Yango |
| Declining | Cash | 64% of payments in 2025, down from 85% in 2020 | Still dominant but falling fast |

Top-performing PSPs / MoRs table (ranked best to worst):
| Rank | Provider | Type | Why it ranks here |
| 1 | Peso | Fintech/USDT bridge | Only vendor with a confirmed relationship to Yango specifically, live inside Yango Food since Aug 2026 |
| 2 | Red Enlace | Interbank QR switch | Operates QR Simple, which already carries 94% of interbank electronic transfers |
| 3 | Tigo Money | Telco wallet | 3,500+ cash-in/cash-out points nationally, the widest physical footprint of the three |

SO WHAT: "Bolivia is quietly Yango's biggest LatAm market by traffic, and the region's most underserved by global payments research, no processor here discloses an approval rate, but the real story is that cards are already losing 40% of dollar-linked volume to QR and stablecoins, exactly where an orchestrator adds the most value."

Footnote: "Source: Similarweb, estrategiabolivia.com, Red Uno, Correo del Sur, Los Tiempos, criptonoticias.com, Banco Central de Bolivia, ASOFIN, Red Enlace (2025-2026). Driver count revised 2026-08-18 from a stale 2023 nationwide figure (14,000) to ~27,000+, derived by applying the Cochabamba trips-per-driver ratio to Santa Cruz's own ~4M trips/month, plus Cochabamba's confirmed 4,000; La Paz/El Alto excluded, so this is a floor. TO VALIDATE: current total driver count including La Paz/El Alto, actual recharge amount, Peso's transaction volume with Yango."

---

## SLIDE 4: 🇻🇪 Venezuela

Title: "Venezuela: no global PSP covers this market at all, and Yango is building it bank by bank"

Stat bar (4 cells):
1. "~3,100" / "Yango drivers (modeled)" / "Derived from Yango's own 11M+ km driven in 100 days; range ~2,100-4,700, softest estimate of the four countries"
2. "~7,000/min" / "Pago Móvil transactions nationally" / "20M+ affiliated customers, 86%+ banking penetration, 2026"
3. "~$915/mo" / "Avg. monthly driver revenue (Yango's own published ranges)" / "Blended, 60% moto / 40% car fleet mix · avg ticket ~$0.50-$5.80"
4. "~$9.4M/year" / "Est. annual recharge volume opportunity (modeled, wide range)" / "Modeled: ~3,100 drivers x ARPU x ~27.5% commission x 12 (est.); range ~$6.3M-$14.2M/year"

Lever 1 DAY-ONE FRAGMENTATION, LIVE RIGHT NOW: "Cash-only at launch, online methods added ~5 days later" / "Three separate bank \"payment buttons\" (Banco de Venezuela, BNC, Bancamiga)" / "This is the exact one-integration-per-bank pattern an orchestrator replaces, happening today, not hypothetically"
Lever 2 ZERO GLOBAL PSP COVERAGE: "Stripe confirmed not to support Venezuela at all" / "No approval-rate data exists for any provider covering the country" / "Whoever builds a real rail here first has no incumbent to displace"
Lever 3 DOLLARIZATION IS ALREADY THE DEFAULT: "~80% of oil exports settle in USDT" / "Bolívar is the most-traded fiat pair on Binance P2P globally" / "The market has already moved to dollar/stablecoin rails at the sovereign level, retail is following"

Payment method priority table:
| Priority | Method | Scale/penetration | Role for Yango |
| Must-have | Pago Móvil | ~7,000 tx/minute, 20M+ affiliated customers | Dominant, instant, no card needed, the standard for exactly this flow |
| Good, currency hedge | USDT/crypto | Venezuela ranks 18th globally (9th population-adjusted) on crypto adoption | Under 1% transfer cost, hedges hyperinflation |
| Weaker fit | Zelle | No quantified user base, genuinely unsourceable | More common for remittances than routine local payments, needs USD access |

Top-performing PSPs / MoRs table (ranked best to worst):
| Rank | Provider | Type | Why it ranks here |
| 1 | Mega Soft | Local processor | Largest confirmed local merchant network, 20,000+ affiliated businesses |
| 2 | Zinli | USD wallet | Only option that lets a driver hold and spend USD without a Venezuelan bank account |
| 3 | Reserve / UglyCash | Crypto/USD wallet | Most direct crypto-native rail, but current scale is unconfirmed since its July 2026 relaunch |

SO WHAT: "Venezuela is the weakest-evidence market of the four, no global PSP covers it and no processor discloses an approval rate, but even a conservative reading of Yango's own disclosed driving activity points to a real, if uncertain, recharge opportunity, on top of an online-payments rollout that is still three separate bank integrations bolted on five days after cash-only launch."

Footnote: "Source: elnacional.com, bancaynegocios.com, motummagazine.com, Últimas Noticias, Chainalysis, criptonoticias.com, elucabista.com (2025-2026). Driver count and TAM are modeled, not reported, derived from Yango's own 11M+ km driven in 100 days divided by an assumed trip distance and Bolivia's cross-market trip-frequency rate; this is the softest of the four country models, treat the range, not the point estimate, as the honest answer. TO VALIDATE: total driver count, blended average fare, whether the three bank integrations are still separate."

---

## SLIDE 5: The Merchant of Record

Title: "The Merchant of Record: why one vendor can't cover Colombia, Peru, Bolivia and Venezuela"

Framing text box, directly under the title, smaller body type: "A Merchant of Record (MoR) becomes the legal seller of a transaction, taking on tax collection and remittance, chargeback liability, and local compliance, unlike a plain PSP, which moves the payment and leaves that liability with the merchant. That distinction isn't academic for Yango: Bolivia unified its exchange rate in June 2026, ending a 15-year peg and devaluing the boliviano roughly 30-40%, and Venezuela is running 600%+ inflation and remains largely cut off from global card networks and correspondent banking, even after the January 2026 capture of Nicolás Maduro. An entity that owns FX conversion, settlement timing and local compliance is worth materially more here than a pure processor that pushes that risk back to Yango."

Stat bar (4 cells):
1. "2 of 4" / "Countries Unlimit confirms on its own site" / "Colombia + Peru only, per unlimit.com/coverage/latam"
2. "3 of 4" / "Countries Inswitch confirms on its own site" / "Colombia + Peru + Bolivia; its Venezuela page returns a 404"
3. "0 of 12+" / "MoR/PSP candidates researched with confirmed Venezuela coverage" / "dLocal, EBANX, Paddle, PayPal, Rebill, PayRetailers, Unlimit and Inswitch all exclude it"
4. "Neither" / "Unlimit nor Inswitch has a named, dedicated Merchant of Record product" / "Both are PSP/embedded-finance platforms; MoR is a side effect of their model, not a purpose-built service"

"WHO ACTUALLY PERFORMS BEST, RANKED" table (columns: Rank, Provider, True MoR?, Colombia, Peru, Bolivia, Venezuela, Why it ranks here):
| Rank | Provider | True MoR? | Colombia | Peru | Bolivia | Venezuela | Why it ranks here |
| 1 | dLocal | Yes, confirmed, "acts as Merchant of Record in each country" | Yes | Yes | Yes | No | Only true MoR here with a dedicated marketplace/payout product, dLocal for Platforms, built for splitting funds and paying sellers or partners, the closest structural match to driver payouts |
| 2 | Inswitch | Not a named MoR product; positions as embedded-finance/BaaS platform | Yes | Yes | Yes | No (404 on own site) | Best country coverage of the two HQ-shortlisted vendors, and the only one with a published ride-hailing case study, see verification flag below |
| 3 | EBANX | Yes, confirmed for at least some markets | Yes | Yes | Yes | No | Major established LatAm player with a dedicated Bolivia country page |
| 4 | Paddle | Yes, confirmed | Yes | Yes | Yes | No | True MoR with Bolivia coverage, but built for digital goods and subscriptions, not a proven fit for a driver-payout/gig use case |
| 5 | Unlimit | Not a named MoR product; PSP/aggregated-MID model | Yes | Yes | No | No | Weakest coverage of the group, 2 of 4 countries, and no gig-economy or ride-hailing client found anywhere in public sources |

Also considered, weaker fit, smaller text below the table: "PayPal (confirmed PSP, not an MoR; excludes Venezuela entirely; no gig-economy driver-payout product), Rebill (explicitly states it is not an MoR; Colombia and Peru only), PayRetailers (not branded as an MoR; Colombia and Peru only, no confirmed Bolivia or Venezuela coverage). FastSpring, 2Checkout/Verifone, Nomupay and Corpay all lack a confirmed, itemized coverage list for these four markets specifically."

Two-column box below the table:

LEFT box, "Unlimit vs. Inswitch, head to head":
- Founded: Unlimit 2009, London HQ, rebranded from Unlimint in 2023. Inswitch 2002, Uruguay-founded with a US legal entity, acquired by TransNetwork in May 2024.
- Funding: Unlimit has not publicly raised funding, per Tracxn. Inswitch's funding is not publicly disclosed either; it now operates as a TransNetwork subsidiary.
- Scale: Unlimit ~500-585 employees across 16 offices on 4 continents. Inswitch ~130-170 employees across 3 continents.
- Gig-economy/ride-hailing client: Unlimit, none found. Inswitch, one published case study, see verification flag.
- Independent reviews: no independently verified rating was confirmed for either vendor in this pass; treat any review-site number for either as unconfirmed until checked manually.

RIGHT box, "VERIFY BEFORE THE MEETING" (flagged/warning style):
"Inswitch publishes a case study titled 'Yango Scales with Inswitch' (inswitch.com/case-studies/yango), describing payments and payouts orchestration, hosted checkout, digital wallets and compliance for a multi-country mobility platform. It does not name a legal entity or list countries. Confirm directly with Yango's HQ team whether this is the same Yango before presenting this slide, it would mean Inswitch is a known or existing vendor, not a blind comparison, and that changes the framing of this whole conversation."

SO WHAT: "Across every credible Merchant of Record and PSP candidate researched, including both vendors Yango's HQ already likes, not one has confirmed coverage in Venezuela, and only Inswitch among the two shortlisted vendors reaches Bolivia. A single-MoR bet structurally cannot cover all four markets Yango operates in; the only way to get Colombia, Peru, Bolivia and Venezuela covered at once is to orchestrate across providers per market, not pick one."

Footnote: "Source: Unlimit, Inswitch, dLocal, EBANX, Paddle, PayPal, Rebill, PayRetailers official coverage pages and documentation (2026); Stripe and Paddle on MoR vs. PSP; Rio Times, Central Banking, Trading Economics, CSIS, USNI News on Bolivia's 2026 currency unification and Venezuela's 2026 macro and political situation. No approval or acceptance rate appears for any provider. TO VALIDATE: whether Inswitch's published Yango case study refers to this same prospect, and current commercial terms and country-specific licensing status for both shortlisted vendors."

---

## WHAT NOT TO DO

- Do not modify any other slide in the deck outside this new appendix section.
- Do not invent or round any number differently than given above.
- Do not put a numeric approval/acceptance rate on any provider anywhere in this appendix, including a vendor's own self-reported figure. Rank providers only by confirmed scale, confirmed local-method support, or a confirmed direct relationship with Yango.
- Do not model a dollar TAM for Venezuela. The slide explicitly says "Not modeled" for a reason, there is no defensible driver count to build one from.
- Do not drop the "(est.)," "(industry proxy)," "(derived)," or "(lower confidence)" qualifiers from any stat bar cell or lever card, they are load-bearing, not decorative.
- Do not carry over the lighter Colombia/Peru/Bolivia/Venezuela slides from section 6.5 of the 2026-08-16 prompt, these 6 slides replace them entirely.
- Keep all 4 country slides visually identical to each other in layout, differing only in content. Slide 5 (The Merchant of Record) is intentionally different, don't force it into the same 4-cell-stat-bar-plus-levers mold.
- Do not present the Inswitch "Yango Scales with Inswitch" case study as confirmed proof that Inswitch already serves this exact prospect. State it as a fact that needs verification, exactly as written on the slide, never stronger.
- Do not put a specific star rating or review-platform score on Unlimit or Inswitch anywhere on this slide. Research this pass turned up conflicting, unverifiable numbers for both; the slide correctly says no independently verified rating exists, keep it that way.
