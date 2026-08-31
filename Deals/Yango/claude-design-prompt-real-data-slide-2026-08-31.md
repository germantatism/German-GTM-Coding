# Prompt Claude Design: real recharge data slide + reconcile Opportunity/Levers to Javier's actual numbers (2026-08-31)

Target: the presentation uploaded alongside this prompt, "Yango + Yuno_Aug 26." Edit it in place, do not create a new deck or a new visual system.

**Match the uploaded deck's existing visual system exactly everywhere below: same fonts, same colors, same chip and callout style, same stat-block and card layout, same eyebrow/title/footer structure already used on its other slides.** Every new or edited slide must look like it was always part of this deck. This is a content and data update, not a redesign.

## Why this change is happening

Javier's team shared real, country-level recharge data (Cashless GMV, average recharge ticket, monthly transactions, card and APM approval rate for Colombia, Peru, Bolivia and Venezuela). This is the actual data the discovery call on Aug 19, 2026 was run to collect. It replaces every modeled recharge-volume figure in this deck, including the Aug 18, 2026 reconciliation that scaled the deck's headline numbers up to ~$332M/year and +$29M/year.

**That Aug 18 reconciliation is now superseded and must NOT be applied.** It scaled the deck to a modeled $332M/year base built from driver-count proxies. The real data shows annual cashless recharge GMV across the four markets is **$87.7M/year**, close to the deck's original, pre-reconciliation $75M figure and nowhere near the $332M modeled figure. Do not use $332M, $29M, or any number from the `claude-design-prompt-deck-reconciliation-2026-08-18.md` prompt anywhere in this deck. If that prompt was already applied to the live deck, undo it using the numbers below.

## The real data (source: Javier's team, shared August 2026, monthly, converted to annual by ×12 in this deck)

| Country | Cashless GMV/year | Avg recharge ticket | Transactions/year | Card approval today | APM approval today |
|---|---|---|---|---|---|
| Colombia | $23,155,176 | $3.50 | 6,615,768 | 92.6% | Nequi 80.5% |
| Peru | $21,553,152 | $3.20 | 6,735,360 | 93.1% | Yape 85.7% |
| Bolivia | $32,968,452 | $1.50 | 21,978,972 | 91.3% | none live |
| Venezuela | $9,983,520 | $2.80 | 3,565,548 | 85.8% | none live |
| **Total** | **$87,660,300** | $2.25 blended | 38,895,636 | 91.5% blended | |

Card acceptance uplift modeled from this data (formula: incremental GMV = current GMV × uplift points ÷ current approval rate):

| Country | Uplift applied | Conservative/year | Optimistic/year | Average/year |
|---|---|---|---|---|
| Colombia | +1.8 to 2.2pp | $450,101 | $550,123 | $500,112 |
| Peru | +1.8 to 2.2pp | $416,710 | $509,312 | $463,011 |
| Bolivia | +1.8 to 2.2pp | $649,980 | $794,421 | $722,201 |
| Venezuela | +4 to 7pp | $465,432 | $814,506 | $639,969 |
| **TOTAL** | | **$1.98M** | **$2.67M** | **$2.33M** |

This is the only dollar figure on this deck backed by Yango's own real data. Everything else Yuno models (new local rail coverage, processing cost, integration savings) must stay visually and numerically separated from this figure, clearly labeled as illustrative or pending validation, never summed into one blended headline number with it.

---

## 1. NEW SLIDE — insert in place of slide 6, "Yango's current landscape"

Slide 6 currently has two problems: a leftover template artifact reading "HOW EVENTBRITE RUNS PAYMENTS TODAY," and four unlabeled percentage chips (13-62%, 2-9%, 1-5%, 5-24%) with no legend explaining what they measure. Replace this slide entirely with the real data table below. This fixes both problems and delivers exactly what the new content needs to say.

**Eyebrow:** YANGO TODAY
**Title:** "The data behind this business case, straight from Yango's own numbers"

**Body:** four country columns (Colombia, Peru, Bolivia, Venezuela), each a stat block in the same visual style as the appendix country deep-dive slides (pages 32-35), with these rows:
- Cashless GMV, annualized (the four values from the table above)
- Average recharge ticket
- Transactions per year
- Card approval today, plus APM approval where one is live (Nequi in Colombia, Yape in Peru; Bolivia and Venezuela show no APM live today)

**Closing line under the table:** "Card approval already clears 90% in three of the four markets. None of them yet connect to the local rail that dominates their country: PSE and Bre-B in Colombia, Plin in Peru, QR Simple in Bolivia, Pago Móvil in Venezuela."

**Footer:** "Source: Yango's own recharge data, shared by Javier Patiño's team, August 2026. Replaces all previously modeled recharge-volume figures in this deck."

---

## 2. Slide 4, "The Scale Today" — update one stat only

| Element | Old | New |
|---|---|---|
| "~$75M annual recharge volume across the four markets" | modeled | "**~$87.7M** annual cashless recharge volume across the four markets, per Yango's own August 2026 data" |

Leave the driver-count stats ("120k+ drivers paid via Cobre Fast Pay," "~131k monthly active drivers") unchanged. No new driver-count data was shared; that gap is still open and separate from this update.

---

## 3. Slide 8, "The Opportunity" — replace the headline and the lever breakdown

Current slide shows "+$6M/year" built from three levers (coverage expansion +6pp ~$4.5M, acceptance uplift +2pp ~$1.5M, processing cost ~200bps ~$0.6M). Only one of those was ever grounded in Yango-specific data, and even that one used the wrong base. Replace with:

**New headline:** "+$2.33M/year in recovered recharge volume from closing the card acceptance gap alone" (range $1.98M to $2.67M)

**Body, keep the lever-description format but with one lever, not three:**
"Card approval already clears 90% in three of the four markets, but the binding step, verifying a driver's card before it can fund a balance, fails 30 to 40% of the time because Yango's acquirers have no local presence and the issuing bank flags the charge as cross border. Smart routing and local acquiring close that gap directly."
"+1.8 to 2.2pp acceptance in Colombia, Peru and Bolivia; +4 to 7pp in Venezuela, where the current rate is lowest"
"~$2.33M/year average"

**Add a clearly separated secondary block below, visually distinct (different background or a bordered callout, not blended into the headline number):**
"Additional upside, not yet validated: connecting each market's dominant local rail, PSE and Bre-B in Colombia, Plin in Peru, QR Simple in Bolivia, Pago Móvil in Venezuela, none of which are live today. Using Yuno's standard benchmark for a crucial missing local rail (8 to 12% incremental transactions), this could add another $5.7M to $8.8M/year, but this has not been validated against Yango's actual conversion data and should not be presented as confirmed."

**Keep unchanged:** the "~$0.52M in integration work avoided" figure. It is engineering-effort based, not volume based, and does not depend on the GMV correction above.

**Footnote, replace:** "The acceptance figure above is built directly from Yango's own recharge data, shared August 2026: real GMV, real transaction counts, and real approval rates per country. The $5.7M-$8.8M additional-rail figure is a Yuno benchmark estimate, not yet validated with Yango's data."

---

## 4. Slide 9, "Yuno's orchestration layer unlocks ~$6M/year across four identified levers" — replace title and totals

**New title:** "Yuno's orchestration layer unlocks $2.33M/year in confirmed value, with more upside pending validation"

**Restructure the lever table to lead with the confirmed lever, per country, matching this data:**

| | Colombia | Peru | Bolivia | Venezuela |
|---|---|---|---|---|
| Lever | Card acceptance uplift | Card acceptance uplift | Card acceptance uplift | Card acceptance uplift |
| How it works | Smart routing and local acquiring close the residual card gap; already Yango's second-strongest market on approval | Local acquiring and retries lift the card rail past its already-strong 93.1% base | Card rail is Yango's strongest of the four; the real opportunity is the missing QR Simple rail below | Weakest card infrastructure of the four; largest proportional gain from smart routing |
| Conservative | $450K/yr | $417K/yr | $650K/yr | $465K/yr |
| Optimistic | $550K/yr | $509K/yr | $794K/yr | $815K/yr |

**CONSERVATIVE total: $1.98M/yr** (was $3.2M/yr)
**OPTIMISTIC total: $2.67M/yr** (was $7.2M/yr)

**Keep "New Local Rails per Market" as a fifth, visually separated column or a footer callout, not folded into the conservative/optimistic totals above:** "Illustrative only, pending validation: $5.7M to $8.8M/year from connecting PSE/Bre-B (CO), Plin (PE), QR Simple (BO) and Pago Móvil (VE)."

**Drop "Processing Cost Reduction" and "Fixed Costs Reduction" from this slide's dollar totals.** No current MDR or current engineering-cost data exists for Yango specifically to ground either figure after the base correction. If German wants to keep them for narrative reasons, they must show no dollar figure and carry a visible "not yet sized" label, they cannot appear in the CONSERVATIVE/OPTIMISTIC sums.

**Footnote, replace:** "The acceptance figures above are built from Yango's own recharge data, shared by Javier Patiño's team, August 2026, covering real GMV, transaction counts and approval rates per country. All other figures on this slide are Yuno modeling benchmarks pending validation with Yango's data."

---

## What NOT to do

- Do not use $332M, $29M, ~$15M-$35M, or any figure from the Aug 18, 2026 reconciliation prompt anywhere in this deck. That reconciliation is superseded by real data and must be treated as if it was never applied.
- Do not blend the $5.7M-$8.8M illustrative new-local-rail figure into the same conservative/optimistic total as the $1.98M-$2.67M confirmed acceptance figure. They must stay visually and numerically separate everywhere they appear.
- Do not invent or update driver-count figures (120k+, ~131k, the per-country appendix counts). No new driver data was shared. Only the recharge-volume, ticket, transaction and approval-rate figures change in this update.
- Do not touch any slide's layout, design, or wording beyond what is specified above.
- Do not leave "HOW EVENTBRITE RUNS PAYMENTS TODAY" anywhere in the deck. If it appears on any slide besides the old slide 6, remove it there too.
- Do not present the $2.33M average as a single point estimate in client-facing language without the $1.98M-$2.67M range attached, consistent with how the rest of the deck presents modeled figures.
