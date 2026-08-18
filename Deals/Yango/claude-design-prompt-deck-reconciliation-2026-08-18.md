# Prompt Claude Design: Reconcile the Yango deck's main-body numbers to the appendix base (2026-08-18)

---

⚠️ **This is an UPDATE to the LIVE, already-built deck** (Google Slides id `1XPdfoKEGoT-s7-XcIoewxbOWnMidO9JfcMTUgYvclak`), not a new build. Do not touch slide layout, design, or wording beyond the specific numbers listed below. Every change below is a number swap plus a one-line footnote update, nothing else.

## WHY THIS CHANGE IS HAPPENING

The deck currently has two unreconciled models running side by side:

1. **The main body** (the "How Yango Runs Payments Today," "The Opportunity," and "Yuno's orchestration layer unlocks" slides) uses a base of **~131,000 monthly active drivers** and **~$75M annual recharge volume across the four markets**, producing a headline opportunity of **+$6M/year**.
2. **The appendix** (the four country deep-dive slides) uses real, sourced, country-by-country modeling: Colombia alone is 120,000+ drivers and ~$290M/year in modeled recharge volume. Adding Peru (~$37M) and a revised Bolivia (~$5.2M, see below) gives **~$332M/year across ~162,000+ drivers for Colombia, Peru and Bolivia alone**, before Venezuela (unsized) is even counted.

These two numbers cannot both be right in the same deck: the main body's own "131k total across four markets" is already smaller than Colombia's driver count alone (120,000, stated on the very same slide two lines above it). A payments-literate audience like Yango's HQ team will catch this immediately. German has decided to **reconcile the main body up to the appendix's larger, better-sourced base**, since the appendix figures are individually cited and traceable, while the ~$75M/~131k figures are not.

## WHAT CHANGED IN THE APPENDIX FIRST (do this before touching the main body, the main-body numbers depend on it)

**Bolivia's modeled driver count and TAM were revised on 2026-08-18.** The old figure (14,000 drivers nationwide, a 2023 press figure) was internally inconsistent with a second real data point already in the brief: Santa Cruz alone moves ~4,000,000 trips/month, Yango's largest Bolivia market. Applying the same trips-per-driver ratio derived from Cochabamba (700,000 trips/month ÷ 4,000 drivers = 175 trips/driver/month) to Santa Cruz implies ~22,900 drivers in Santa Cruz alone, already above the old 14,000-nationwide total. Santa Cruz (~22,900, derived) plus Cochabamba's confirmed 4,000 gives a **~27,000-driver floor**, excluding La Paz/El Alto entirely (no current trip data found there, so this is conservative, not inflated). The ARPU proxy (~$107/month) is unchanged, since it uses the same per-driver trip rate.

**New Bolivia TAM: 27,000 drivers × $107/month × ~15% commission × 12 = ~$5.2M/year** (was ~$2.7M/year).

**Also fix the Venezuela appendix slide.** The live deck currently shows a fabricated, self-contradicting number: stat bar cell 1 reads "8,000 / Total driver count," while its own sub-caption still said "Only qualitative: 'hundreds of thousands' of riders in 100 days..." and cell 4 still said "Not modeled / No defensible driver count exists to size this in dollars." That "8,000" had no source and was never part of the original research or prompt for this slide. **As of 2026-08-18, Venezuela now has an actual modeled estimate to replace both the fabricated "8,000" and the old "Not modeled," built from Yango's own disclosed 11,000,000+ km driven in its first 100 days, divided by an assumed average trip distance (no Venezuela-specific figure exists, so a 4-9km range is used, midpoint 6km) and Bolivia's cross-market trip-frequency rate (175 trips/driver/month, since no Venezuela-specific rate exists either): ~3,100 drivers (range ~2,100-4,700). Modeled TAM: 3,100 × $915/month ARPU × ~27.5% commission × 12 = ~$9.4M/year (range ~$6.3M-$14.2M/year). This is explicitly the softest of the four country models, treat it as directional. Do NOT use the much larger alternative implied by applying the driver-to-rider oversupply ratio to "hundreds of thousands of riders" (would suggest 40,000-100,000+ drivers), that phrase is a vague company figure, not a usable base, and the two methods diverge by roughly 20-30x.**

**Revised combined base across Colombia + Peru + Bolivia**: **~162,000+ drivers, ~$332M/year modeled annual recharge volume.** This remains the base used for the main-body reconciliation below. Venezuela's new ~3,100-driver / ~$9.4M-year model is real but meaningfully less reliable than the other three; keep it visible on its own appendix slide, but do NOT fold it into the main-body headline numbers below without calling out its lower confidence every time it appears. If German wants Venezuela included in the whole-deck headline too, the all-four total is ~165,100+ drivers and ~$341M/year, always with that caveat attached.

## MAIN-BODY RECALCULATION METHODOLOGY

The original main-body numbers were built as straight percentage-of-base calculations: each lever's dollar impact = (percentage-point assumption) × (total annual recharge volume base). Confirmed by reverse-checking the original figures: 6pp × $75M = $4.5M (matches the stated Lever 1 figure exactly), 2pp × $75M = $1.5M (matches Lever 2 exactly). The percentage-point assumptions themselves (the "+6pp completed top-ups," "+2pp acceptance," "~200bps on shifted volume" ranges) are Yuno's own observed uplift benchmarks and do NOT change, only the base they're applied to changes, from $75M to $332M (a 4.43x scale factor).

⚠️ **Sanity-check before using**: this scaling takes the headline opportunity from "+$6M/year" to "+$29M/year," a nearly 5x increase to the core pitch number. That is mechanically correct given the corrected base, but it is a materially bigger claim to put in front of Yango. German should feel confident standing behind $29M/year specifically (not just "the math checks out") before this goes into any meeting. If in doubt, present the range ($15M-$35M) rather than anchoring hard on the $29M point estimate, or hold this slide back for one more validation pass.

## SLIDE-BY-SLIDE CHANGES

### "How Yango Runs Payments Today" (executive summary / overview slide)

| Element | Old | New |
|---|---|---|
| Total driver count line | "~131k monthly active drivers across CO, PE, BO, VE" | "~162,000+ monthly active drivers across Colombia, Peru and Bolivia (Venezuela's driver base could not be sized)" |
| Total recharge volume line | "~$75M annual recharge volume across the four markets" | "~$332M annual recharge volume across Colombia, Peru and Bolivia (Venezuela not sized)" |
| "120k+ drivers paid in real time via Cobre Fast Pay in Colombia" | unchanged | unchanged, still accurate and consistent with the new total |
| Bolivia bullet ("48x growth in QR simple transaction value 2021-2024, free and universal") | unchanged | unchanged (not part of this reconciliation; optional future update available if wanted, more current BCB data shows 2021-2025 growth of 14,508% in transaction volume) |

### "The Opportunity" slide

| Element | Old | New |
|---|---|---|
| Headline | "+$6M/year IN RECOVERED AND INCREMENTAL RECHARGE VOLUME, PLUS PROCESSING COST SAVINGS" | "+$29M/year IN RECOVERED AND INCREMENTAL RECHARGE VOLUME, PLUS PROCESSING COST SAVINGS" |
| Lever 1 (coverage expansion, "+6 pp completed top-ups") | "~$4.5M/year" | "~$19.9M/year" |
| Lever 2 (authorization uplift, "+2 pp acceptance") | "~$1.5M/year" | "~$6.6M/year" |
| Lever 3 (processing cost, "~200 bps on shifted volume") | "~$0.6M/year" | "~$2.7M/year" |
| Opening line ("cut ~$0.6M per year in processing cost by settling domestically, and avoid ~$0.52M in integration work") | "~$0.6M" | "~$2.7M" (keep "~$0.52M in integration work" unchanged, see note below) |
| Footnote | "The model rests on 120,000+ Yango drivers in Colombia, an estimated ~131,000 monthly active drivers across the four markets, and ~$75M in annual recharge volume, with Yuno's observed uplift benchmarks applied per lever." | "The model rests on 120,000+ Yango drivers in Colombia, an estimated ~162,000+ monthly active drivers across Colombia, Peru and Bolivia (Venezuela not sized), and ~$332M in annual recharge volume, with Yuno's observed uplift benchmarks applied per lever." |

**Do not scale "~$0.52M in integration work."** That figure represents engineering effort (8 integration builds across 7 teams), not a percentage of recharge volume, adding more countries to the routing layer doesn't multiply avoided engineering cost by the same factor as processed dollars. Leave it as-is pending a separate review with whoever originally estimated it.

### "Yuno's orchestration layer unlocks ~$6M/year across four identified levers" slide

| Element | Old | New |
|---|---|---|
| Slide title | "...unlocks ~$6M/year across four identified levers" | "...unlocks ~$29M/year across four identified levers" |
| CONSERVATIVE total | "$3.2M/yr" | "~$15M/yr" |
| OPTIMISTIC total | "$7.2M/yr" | "~$35M/yr" |
| "Cost Levers +$0.8M/yr" (optimistic processing-cost figure) | "+$0.8M/yr" | "~$3.6M/yr" |
| "+$0.5M" (integration-avoidance figure, matches the ~$0.52M above) | "+$0.5M" | unchanged, same note as above, do not scale |
| Percentage-point and bps labels ("+3-6 p.p.", "+1-3 p.p.", "~200 bps", "8", "12", "3", "4") | unchanged | unchanged, these are rates/counts, not dollar amounts, nothing here depends on the volume base |

### Appendix, Bolivia slide

Already specified in full in `claude-design-prompt-4-country-appendix-2026-08-18.md` (updated 2026-08-18): stat bar cell 1 becomes "~27,000+" with the caption explaining the Santa Cruz cross-check, cell 4 becomes "~$5.2M/year," Lever 1's sub-line updates to reference the Santa Cruz derivation, and the footnote explains the revision. Apply exactly as written there.

### Appendix, Venezuela slide

Full replacement text already specified in `claude-design-prompt-4-country-appendix-2026-08-18.md` (updated 2026-08-18): stat bar cell 1 becomes "~3,100" with a caption citing the km-based derivation and the softer-confidence flag, cell 4 becomes "~$9.4M/year" with its range noted, the SO WHAT line is reworded to reflect that a real (if uncertain) opportunity is now modeled, and the footnote drops the old "no dollar opportunity is modeled here" language. Apply exactly as written there.

## WHAT NOT TO DO

- Do not touch any slide's layout, design, wording, or structure beyond the specific number swaps listed above.
- Do not scale the ~$0.52M/~$0.5M integration-avoidance figure, it is not volume-driven.
- Do not silently drop the "Venezuela not sized" qualifier anywhere it appears in the updated text, it is load-bearing, not decorative.
- Do not present "$29M/year" as a firm, final number in any client-facing sentence without also keeping the "modeled from public data, to be validated with Yango's actual data" framing that already exists elsewhere in the deck.
- Do not blend Venezuela's ~3,100-driver / ~$9.4M-year model into the main-body headline numbers (the $332M/162,000-driver base used in the recalculation above) without explicitly flagging that Venezuela's figure is materially lower confidence than the other three. If in doubt, keep it out of the headline and confined to its own appendix slide.
- Do not use the driver-to-rider-ratio-derived alternative for Venezuela (40,000-100,000+ drivers) anywhere, it was explicitly rejected in favor of the distance-based method, see above.
