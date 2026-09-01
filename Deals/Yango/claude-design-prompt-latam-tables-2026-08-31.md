# Prompt Claude Design: LatAm detail tables (Cards, APMs, Dev cost savings, 4-lever total) with Yango's real numbers (2026-08-31)

Target: the presentation uploaded alongside this prompt, "Yango + Yuno_Aug 26." Edit it in place, do not create a new deck or a new visual system.

**These four slides reuse the exact visual system already used elsewhere in Yuno's business case decks: dark header row, alternating light table rows, solid blue total row, a right-side "CONCLUSIONS" panel with arrow bullets, and a small footnote line at the bottom.** Match that system exactly, only the content and numbers below are new. This is a content build using an existing template, not a redesign.

**Insert all three table slides (Cards, APMs, Dev cost savings) as new appendix slides, positioned right after the four country deep-dive slides and right before "The Merchant of Record" section.** They are backup detail for the headline Opportunity numbers on slide 8, the same relationship these slides have to the main opportunity slide in Yuno's other business case decks.

**This prompt supersedes the slide 9 restructuring instructions in `claude-design-prompt-real-data-slide-2026-08-31.md`.** Use the 4-lever template below for slide 9 instead of the per-country table specified there. Everything else in that earlier prompt (the new data slide replacing slide 6, the slide 4 stat update, the slide 8 headline and footnote) still applies unchanged.

## The confirmed and modeled numbers behind every slide below

| Country | Cashless recharge GMV/year | Card approval today | Acceptance uplift applied | Confirmed Δ TPV/year (avg) | Illustrative new-rail Δ TPV/year (midpoint) |
|---|---|---|---|---|---|
| Colombia | $23.16M | 92.6% | +1.8 to 2.2pp | $0.50M | $2.32M |
| Peru | $21.55M | 93.1% | +1.8 to 2.2pp | $0.46M | $0.65M |
| Bolivia | $32.97M | 91.3% | +1.8 to 2.2pp | $0.72M | $3.30M |
| Venezuela | $9.98M | 85.8% | +4 to 7pp | $0.64M | $1.00M |
| **Total** | **$87.66M** | 91.5% blended | | **$2.33M** | **$7.26M** |

Source for every GMV, ticket, transaction, and approval-rate figure: Yango's own recharge data, shared by Javier Patiño's team, August 2026. The confirmed acceptance uplift column is built directly from that data. The illustrative new-rail column applies Yuno's standard "crucial missing local rail" benchmark (8 to 12% incremental transactions, 2 to 4% for Peru since Yape already covers most of the overlap with Plin) and has NOT been validated against Yango's actual conversion data. **Keep these two columns visually distinct everywhere they appear on every slide below, never sum them into one number.**

---

## 1. NEW SLIDE — "LatAm Cards, boost acceptance rates" (appendix)

Same table structure as Yuno's standard "LATAM Cards" slide: five columns, dark header, alternating rows, solid blue total row, CONCLUSIONS panel on the right.

**Title:** "Colombia, Peru, Bolivia, Venezuela Cards, boost acceptance rates and close the local rail gap"

**Table columns:** KEY MARKETS* | EST. ANNUAL CASHLESS RECHARGE GMV (USD M) | Δ ACCEPTANCE RATE (%)** | Δ TPV (USD M) | COST REDUCTIONS (USD M)

**Rows:**
| Colombia | $23.2 | 1.8 to 2.2% | $0.50 | Not modeled*** |
| Peru | $21.6 | 1.8 to 2.2% | $0.46 | Not modeled*** |
| Bolivia | $33.0 | 1.8 to 2.2% | $0.72 | Not modeled*** |
| Venezuela | $10.0 | 4 to 7% | $0.64 | Not modeled*** |

**Total row (blue):** $87.7 | (blank) | $2.33 | Not modeled

**CONCLUSIONS panel:**
"By partnering with Yuno, Yango will close the card acceptance gap across all four LatAm markets it operates in:
- Yango could recover approximately **$2.33M in annual recovered recharge volume** (range $1.98M to $2.67M), driven by smart routing and local acquiring fixing the card binding failure identified on the August 19, 2026 discovery call: only 68 to 70% of card verification attempts succeed today because Yango's acquirers have no local presence, versus 90 to 92% once a card is bound.
- Cost reduction from local processing has not been modeled yet. Yango's current MDR by processor (PayU, Unlimit, Inswitch) was not shared; this line will be completed once that data is available."

**Footnotes:** "*Based on Yango's own recharge data, shared by Javier Patiño's team, August 2026. **Range reflects Yuno's proposed uplift per market; average shown in the Δ TPV column. ***No current MDR data was shared for Colombia, Peru, Bolivia or Venezuela; do not estimate one."

---

## 2. NEW SLIDE — "LatAm, alternative payment methods (APMs)" (appendix, right after the Cards slide)

Same table structure as Yuno's standard "LATAM APMs" slide.

**Title:** "Colombia, Peru, Bolivia, Venezuela, the local rail each market is missing"

**Table columns:** KEY MARKETS* | PROPOSED APMS (based on current recharge flow) | Δ TPV (USD M)* | COST REDUCTIONS (USD M)

**Rows:**
| Colombia | PSE, Bre-B | $2.32 | Not modeled** |
| Peru | Plin | $0.65 | Not modeled** |
| Bolivia | QR Simple | $3.30 | QR Simple carries no merchant fee, vs cards today |
| Venezuela | Pago Móvil | $1.00 | Not modeled** |

**Total row (blue):** (blank) | $7.26 | Not modeled

**CONCLUSIONS panel:**
"By connecting each market's dominant local rail through Yuno:
- Yango could unlock approximately **$7.26M in additional annual recharge volume** (illustrative range $5.72M to $8.79M), using Yuno's standard benchmark for a crucial missing local rail. This is NOT validated against Yango's actual conversion data and should be presented as directional, not confirmed, until a joint sizing exercise runs.
- Bolivia is the clearest case: QR Simple carries 94% of the country's interbank transfers and moves no merchant fee at all, while Yango's card rail there, though its strongest of the four markets on approval (91.3%), is still not the rail most Bolivian drivers actually hold."

**Footnotes:** "*Illustrative, built from Yuno's standard modeling benchmark (8 to 12% incremental transactions for a crucial missing rail; 2 to 4% for Peru's Plin, since Yape already covers most of the overlap), not yet validated with Yango's data. **No current per-method cost data was shared beyond QR Simple's published no-fee structure; do not estimate the others."

---

## 3. NEW SLIDE — "LatAm, development cost savings" (appendix, right after the APMs slide)

Same table structure as Yuno's standard "LATAM Development costs savings" slide, same seven-department breakdown and the same standard $21,600 per team per month benchmark used across every Yuno business case.

**Title:** "Development cost savings, five local rails avoided market by market"

**Table columns:** TEAMS INVOLVED ON INTEGRATION MATTERS | COST PER TEAM/MONTH | TOTAL COST PER INTEGRATION (3 MONTH/INTEGRATION) | TOTAL COST PER TEAM (for all 5 integrations: PSE, Bre-B, Plin, QR Simple, Pago Móvil)

**Rows:**
| Product | $2,250.00 | $6,750.00 | $33,750 |
| Engineering | $10,500.00 | $31,500.00 | $157,500 |
| Fraud/Risk | $2,250.00 | $6,750.00 | $33,750 |
| Treasury | $1,350.00 | $4,050.00 | $20,250 |
| Compliance | $1,500.00 | $4,500.00 | $22,500 |
| Finance | $1,125.00 | $3,375.00 | $16,875 |
| Banking & Payments | $2,625.00 | $7,875.00 | $39,375 |

**Total row (blue):** $21,600.00 | $64,800.00 | $324,000

**CONCLUSIONS panel:**
"By centralizing all five missing local rails through Yuno's single API instead of integrating PSE, Bre-B, Plin, QR Simple and Pago Móvil one by one:
- Yango could save up to **$324,000 in development costs** associated with these five integrations.
- An estimated **13 months (about 1.1 years) of engineering time** could be returned to product work instead of being spent building and maintaining five separate local-rail connections, one country at a time."

No cards/MoR processor column on this slide, unlike Yuno's standard template. Yango already operates a processor in each of the four markets today; this is a consolidation, not a new-market entry, so there is no MoR/processor integration count to add here.

---

## 4. Slide 9, "Yuno's orchestration layer unlocks..." — use the 4-lever template, not the per-country table

Replace the per-country restructuring specified in the earlier prompt with this 4-lever layout instead, matching Yuno's standard "$X-$Y M per year" lever template exactly (OPERATIONAL LEVER / COMMERCIAL LEVERS grouping, numbered 1 through 4, LEVER / HOW IT WORKS rows, blue TOTAL IMPACT row at the bottom).

**New title:** "$2.33M confirmed, up to $9.6M per year in total identified opportunity across Colombia, Peru, Bolivia and Venezuela"

| | 1. Build/Run Avoidance (Capex+Opex) | 2. Acceptance Rate Uplift | 3. New-Methods Growth (APMs share capture) | 4. MDR Cost Optimization |
|---|---|---|---|---|
| **How it works** | One connector instead of five separate local-rail builds for PSE, Bre-B, Plin, QR Simple and Pago Móvil | Smart routing and local acquiring fix the card binding failure behind Yango's 68 to 70% verification success rate today | Turning on the local rail each market's drivers already hold and use most: PSE/Bre-B, Plin, QR Simple, Pago Móvil | Not modeled, current MDR by processor (PayU, Unlimit, Inswitch) was not shared |
| **Total impact** | $324K one-time, plus 13 months of engineering time returned | $1.98M to $2.67M/yr (avg $2.33M), CONFIRMED from Yango's own data | $5.72M to $8.79M/yr, ILLUSTRATIVE, not yet validated | Pending data |

Do not add a dollar-per-year figure to lever 1 (it is a one-time cost avoidance, not an annual recurring figure) or to lever 4 (no data exists to model it). Do not sum levers 2 and 3 into one blended annual total anywhere on this slide. The slide title's "$9.6M" is the sum of the confirmed average ($2.33M) plus the illustrative midpoint ($7.26M), shown once as a headline; even there, keep "confirmed" and "up to" language attached so the two parts are never read as equally certain.

**Footnote:** "Lever 2 is built directly from Yango's own recharge data, shared by Javier Patiño's team, August 2026. Lever 3 uses Yuno's standard modeling benchmark and has not been validated with Yango's data. Lever 1 uses Yuno's standard integration-cost benchmark ($21,600 per team per month, 3 months per integration). Lever 4 requires Yango's current processor fee data, not yet shared."

---

## What NOT to do

- Do not invent a cost-reduction dollar figure for any cell marked "Not modeled" or "pending data" above. No current MDR or processing-fee data exists for Yango beyond QR Simple's published no-fee structure in Bolivia.
- Do not blend the confirmed acceptance-uplift numbers ($1.98M to $2.67M/yr) with the illustrative new-rail numbers ($5.72M to $8.79M/yr) into a single total anywhere. They must stay visually and numerically separate on every slide, including the 4-lever slide.
- Do not present lever 1 (Build/Run Avoidance) as an annual recurring figure. It is a one-time $324,000 engineering-cost avoidance plus a one-time 13-month time savings, not a "$/yr" number.
- Do not use $332M, $29M, or any figure from the Aug 18, 2026 reconciliation prompt anywhere in this deck.
- Do not touch any slide's layout, design, fonts or colors beyond matching the existing "LATAM Cards / LATAM APMs / LATAM Development costs / 4-lever" templates already used in Yuno's other business case decks.
