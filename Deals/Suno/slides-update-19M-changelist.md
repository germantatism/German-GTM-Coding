# Google Slides update: Business Case - Suno + Yuno → $19M

Target deck: https://docs.google.com/presentation/d/1Kk43MqH3Ve6eT640BCqShboedyoJp-dvaoQTx3M6A5s/edit

⚠️ **No blind deck-wide Find & Replace.** Several old values repeat identically across different countries but now map to DIFFERENT new values (Canada/Turkey/Thailand all show "$21K" today but are $36K/$37K/$30K respectively now). Go slide by slide using the slide titles below as anchors, not a single global Cmd+H pass.

Everything not listed here (design, colors, fonts, layout, narrative text, payment-method tables, footnotes, SO WHAT lines, base-case conversion %) stays exactly as-is.

---

## PART A — NOT UPDATED YET (flag, do not touch blindly)

The 12 "Business Case" region slides (North America / LATAM / EMEA / APAC × Cards, APMs, Development costs savings — roughly slides in the "Business Case" section before the Appendix) show numbers that don't match even the pre-$19M model validated on the call (e.g. Δ Acceptance rate shown as 1.50%/2.00% vs. the real 3%/3% in the current sheet). These look stale from an earlier draft. Updating them safely needs a direct look at the actual table (not a flattened text export) to avoid misaligning columns. Recommend a separate pass — flag if you want me to attempt it anyway with the caveat that some cells could be misassigned.

---

## PART B — Slide: Top-20 country table ("Stripe does the US and EU very well...")

Table has 20 rows (US through Argentina) with columns: Country · Suno monthly visits (unchanged) · Incremental MRR · Dominant play (unchanged) · Archetype (unchanged).

| # | Country | Old MRR | New MRR |
|---|---|---|---|
| 1 | United States | $180K | **$318K** |
| 2 | Brazil | $55K | **$85K** |
| 3 | Germany | $66K | **$87K** |
| 4 | Indonesia | $49K | **$66K** |
| 5 | India | $52K | **$77K** |
| 6 | United Kingdom | $41K | **$72K** |
| 7 | Japan | $53K | **$72K** |
| 8 | France | $38K | **$57K** |
| 9 | Italy | $28K | **$51K** |
| 10 | Republic of Korea | $23K | **$38K** |
| 11 | Spain | $37K | **$56K** |
| 12 | Canada | $21K | **$36K** |
| 13 | Turkey | $21K | **$37K** |
| 14 | Mexico | $25K | **$32K** |
| 15 | Thailand | $21K | **$30K** |
| 16 | Poland | $15K | **$28K** |
| 17 | Ukraine | $13K | **$22K** |
| 18 | Netherlands | $10K | **$19K** |
| 19 | Vietnam | $5K | **$9K** |
| 20 | Argentina | $11K | **$14K** |

**PORTFOLIO TOTAL box:**
- "$764M/mo" (this is a pre-existing typo in the deck — should read K, not M) → **"$1,206K/mo"**
- "$12M annualized · 61K subscriber impact" → **"$14.5M annualized (of the $19.2M full portfolio) · 96K subscriber impact"**
- "~1B local-payment audience" → unchanged (not a $ figure)
- "~23M Suno monthly visits" → unchanged (real traffic data)
- "~61K paid-subscriber impact" → **"~96K paid-subscriber impact"**

**CONCENTRATION box:**
- "TOP 3 ~39% US · Germany · Brazil" → **"TOP 3 ~41% US · Germany · Brazil"** (same 3 countries, ratio moved slightly)
- "TOP 10 ~78% of total value" → unchanged (coincidentally still ~78%)

**ARCHETYPE SPLIT box** (recomputed from real archetype tags in the table above):
- "Full-stack ~$479K/mo (~63%)" → **"Full-stack ~$686K/mo (~57%)"**
- "Mature ~$150K/mo (~20%)" → **"Mature ~$298K/mo (~25%)"**
- "APM-led ~$135K/mo (~18%)" → **"APM-led ~$222K/mo (~18%)"**

---

## PART C — Slide: "The Opportunity" (THE PROPOSED MODEL, first one)

- "~12M/year IN PRELIMINARY GROSS SUBSCRIPTION REVENUE" → **"~$19M/year"**
- "~$200M ARR" → unchanged (real external fact, not part of this model — leave as-is even though RESUMEN's input uses $300M; that's a separate discrepancy, not something this update should silently fix)
- "~$7.8M/year" (audience expansion, "largest share and ~80K incremental paid subscribers") → **"~$12M/year"**, and "~80K incremental paid subscribers" → **"~128K incremental paid subscribers"**
- "~$4.2M/year" (second and third levers combined) → **"~$7M/year"**

## PART D — Slide: "Stripe alone leaks revenue at four points..."

- "An estimated $12M per year sits across four payment-friction gaps" → **"An estimated $19M per year..."**
- "Local methods missing... ~$6M/yr at stake" → **"~$12M/yr at stake"**
- "Cross-border card declines... ~$2M/yr at stake" → **"~$3M/yr at stake"**
- "Renewal failures... ~$1M/yr at stake" → unchanged (rounds the same both before and after)
- "Three disconnected billing rails... ~$3M build can be avoided" → unchanged (rounds the same both before and after — this is engineering cost avoidance, not a dial that moved)
- Closing line "Estimated $12M/yr at stake" → **"Estimated $19M/yr at stake"**

---

## PART E — Appendix: 19 country slides (Mexico has no appendix slide, only appears in the Part B table)

Format per slide: stat-bar cell 3 (Incremental paid subscribers) · cell 4 (Total paid-subscriber impact, keep the "including auth + renewals · ~$X/mo total" phrasing) · Lever 1 Audience Expansion (subs / $/year) · Lever 2 Authorization Uplift (approvals/year / $/year) · Lever 3 Renewal Continuity (renewals/month / $/year). Everything else on each slide (title, tactic one-liners, payment method table, base-case model %, SO WHAT, footnote) stays as-is.

**United States** — 9,360→**16,553** | 14,400→**25,467** (~$180K/mo→**~$318K/mo**) | L1: 9,360→**16,553** subs / $1.40M→**$2.48M** | L2: 36,300→**64,711** / $0.45M→**$0.80M** | L3: 2,020→**300**/mo / $0.30M→**$0.53M**

**Brazil** — 2,860→**4,420** | 4,400→**6,800** (~$55K→**~$85K**) | L1: 2,860→**4,420** / $0.43M→**$0.66M** | L2: 11,090→**17,279** / $0.14M→**$0.21M** | L3: 620→**80**/mo / $0.09M→**$0.14M**

**Germany** — 3,432→**4,507** | 5,280→**6,933** (~$66K→**~$87K**) | L1: 3,432→**4,507** / $0.51M→**$0.68M** | L2: 13,300→**17,618** / $0.17M→**$0.22M** | L3: 740→**82**/mo / $0.11M→**$0.15M**

**Indonesia** — 2,548→**3,423** | 3,920→**5,267** (~$49K→**~$66K**) | L1: 2,548→**3,423** / $0.38M→**$0.51M** | L2: 9,880→**13,383** / $0.12M→**$0.17M** | L3: 550→**62**/mo / $0.08M→**$0.11M**

**India** — 2,704→**3,987** | 4,160→**6,133** (~$52K→**~$77K**) | L1: 2,704→**3,987** / $0.41M→**$0.60M** | L2: 10,480→**15,585** / $0.13M→**$0.19M** | L3: 580→**72**/mo / $0.09M→**$0.13M**

**United Kingdom** — 2,132→**3,727** | 3,280→**5,734** (~$41K→**~$72K**) | L1: 2,132→**3,727** / $0.32M→**$0.56M** | L2: 8,260→**14,568** / $0.10M→**$0.18M** | L3: 460→**68**/mo / $0.07M→**$0.12M**

**Japan** — 2,756→**3,760** | 4,240→**5,785** (~$53K→**~$72K**) | L1: 2,756→**3,760** / $0.41M→**$0.56M** | L2: 10,690→**14,704** / $0.13M→**$0.18M** | L3: 590→**68**/mo / $0.09M→**$0.12M**

**France** — 1,976→**2,947** | 3,040→**4,533** (~$38K→**~$57K**) | L1: 1,976→**2,947** / $0.30M→**$0.44M** | L2: 7,660→**11,519** / $0.10M→**$0.14M** | L3: 425→**53**/mo / $0.06M→**$0.10M**

**Italy** — 1,456→**2,629** | 2,240→**4,045** (~$28K→**~$51K**) | L1: 1,456→**2,629** / $0.22M→**$0.39M** | L2: 5,650→**10,283** / $0.07M→**$0.13M** | L3: 310→**48**/mo / $0.05M→**$0.08M**

**Republic of Korea** — 1,196→**1,993** | 1,840→**3,067** (~$23K→**~$38K**) | L1: 1,196→**1,993** / $0.18M→**$0.30M** | L2: 4,640→**7,792** / $0.06M→**$0.10M** | L3: 260→**36**/mo / $0.04M→**$0.06M**

**Spain** — 1,924→**2,903** | 2,960→**4,467** (~$37K→**~$56K**) | L1: 1,924→**2,903** / $0.29M→**$0.44M** | L2: 7,460→**11,350** / $0.09M→**$0.14M** | L3: 415→**53**/mo / $0.06M→**$0.09M**

**Canada** — 1,092→**1,863** | 1,680→**2,867** (~$21K→**~$36K**) | L1: 1,092→**1,863** / $0.16M→**$0.28M** | L2: 4,230→**7,284** / $0.05M→**$0.09M** | L3: 235→**34**/mo / $0.04M→**$0.06M**

**Turkey** — 1,092→**1,933** | 1,680→**2,974** (~$21K→**~$37K**) | L1: 1,092→**1,933** / $0.16M→**$0.29M** | L2: 4,230→**7,555** / $0.05M→**$0.09M** | L3: 235→**35**/mo / $0.04M→**$0.06M**

**Thailand** — 1,092→**1,560** | 1,680→**2,400** (~$21K→**~$30K**) | L1: 1,092→**1,560** / $0.16M→**$0.23M** | L2: 4,230→**6,098** / $0.05M→**$0.08M** | L3: 235→**28**/mo / $0.04M→**$0.05M**

**Poland** — 780→**1,469** | 1,200→**2,260** (~$15K→**~$28K**) | L1: 780→**1,469** / $0.12M→**$0.22M** | L2: 3,020→**5,743** / $0.04M→**$0.07M** | L3: 170→**27**/mo / $0.03M→**$0.05M**

**Ukraine** — 676→**1,160** | 1,040→**1,784** (~$13K→**~$22K**) | L1: 676→**1,160** / $0.10M→**$0.17M** | L2: 2,620→**4,540** / $0.03M→**$0.06M** | L3: 150→**21**/mo / $0.02M→**$0.04M**

**Netherlands** — 520→**1,005** | 800→**1,547** (~$10K→**~$19K**) | L1: 520→**1,005** / $0.08M→**$0.15M** | L2: 2,020→**3,930** / $0.03M→**$0.05M** | L3: 110→**18**/mo / $0.02M→**$0.03M**

**Vietnam** — 260→**464** | 400→**714** (~$5K→**~$9K**) | L1: 260→**464** / $0.04M→**$0.07M** | L2: 1,010→**1,813** / $0.01M→**$0.02M** | L3: 56→**8**/mo / $0.01M→**$0.01M**

**Argentina** — 572→**733** | 880→**1,127** (~$11K→**~$14K**) | L1: 572→**733** / $0.09M→**$0.11M** | L2: 2,220→**2,863** / $0.03M→**$0.04M** | L3: 120→**13**/mo / $0.02M→**$0.02M**

---

## Divider slide (Appendix section intro, if it has $ text)

If the appendix divider slide states a portfolio total in its body text, update "$12M" → "$19M" and note "20 markets total ~$14.5M/year of the full $19.2M portfolio (remainder sits in markets outside this top-20 view)."
