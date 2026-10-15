# Build report · Carry1st LatAm Shop deck (content and build agent, 15 Oct 2026)

Working copy: `https://docs.google.com/presentation/d/1-IdPVaPu5FE4P36ByuiQ2vupRFocujdFcmmQeuPI9kk/edit` · 42 built slides appended after the 46 template slides (positions 47 to 88). Not finalized (`--final` not run), nothing committed. `build_state.json` tracks the 42 built ids; `python3 gs_engine.py cleanup` still works.

Files: `make_spec.py` (generates `deck_spec.json`; pulls the ~150 provider and method logo chips from `research/connections_latam_from_adidas.json` so no URL is hand-typed) · `deck_spec.json` (42 slides, `check` passes with 0 problems) · `storyline.md` (regenerated from the final spec) · `thumbs/build/b_47.png … b_88.png`, `contact_1..3.png`, `qa_report.json`.

## Slide list (position in the working copy · id · type · title)

| Pos | id | type | Title |
|---|---|---|---|
| 47 | cover | cover | Carry1st Shop in Latin America by Black Friday |
| 48 | agenda | agenda | 01 to 08 plus Appendix (A) |
| 49 | d01 | divider | 01 Executive summary |
| 50 | exec | exec_summary | Through Yuno, EBANX and dLocal cost less than EBANX direct at run rate, add a second rail, and pay back in month two. |
| 51 | d02 | divider | 02 Where Carry1st stands and what Black Friday needs |
| 52 | heard | two_column | Three asks from Cordel and two from Fatih set the bar for this deck; each one has a section that answers it. |
| 53 | stands | scale | Five markets, a $10 average ticket and six weeks to Black Friday: the launch has to be fast, local and cheap per transaction. |
| 54 | needs | four_numbers | In every launch market the method that wins is local and instant, and most of it sits outside international card rails. |
| 55 | d03 | divider | 03 Two ways to launch |
| 56 | options | comparison_grid | EBANX direct can switch on all five markets with one integration; what it cannot give Carry1st is a second rail. |
| 57 | arrangement | diagram | Yuno sits between the Shop and both merchants of record: EBANX for what it covers, dLocal for what it does not, one integration. |
| 58 | d04 | divider | 04 Why Yuno |
| 59 | why-rbp | table | Seven things the Shop needs in Latin America, what each one gets through Yuno, and how we prove it. |
| 60 | platform | template_keep (23) | A complete suite · Four pillars · One brain ("460+ INTEGRATIONS" rewritten to "16 OFFICES") |
| 61 | proof | stats | The checkout already exists: a working prototype of the Shop on the Yuno SDK runs in four LatAm markets today. |
| 62 | trusted | template_keep (25) | Yuno is trusted by leading companies worldwide (SpaceX image deleted) |
| 63 | d05 | divider | 05 Business case |
| 64 | bc-tiers | bar_chart | The Yuno route costs $44.2 per $1,000 of sales at run rate against $45.0 direct, and covers its fee from about 65K transactions. |
| 65 | bc-scenarios | table | Processing savings carry the case, then engineering avoided, then approval: the base case returns $29.1K a month net at run rate. |
| 66 | bc-ticket | table | A fixed fee doubles as a share of sales when the ticket halves; a share of sales does not: usage on a $5 purchase is one to two cents. |
| 67 | d06 | divider | 06 Proposal |
| 68 | proposal | pricing_cards | One platform fee covering the first $500K of monthly sales, then a share of sales that falls as Carry1st grows. |
| 69 | onus | two_column | What Yuno puts in before signing, and what the platform fee already covers. (kicker INCLUDED, AT NO EXTRA COST) |
| 70 | d07 | divider | 07 Launch plan to Black Friday and Phase 2 |
| 71 | launch | table | Six weeks to 27 November: provider contracts and KYC are the critical path; the Yuno work is measured in days. |
| 72 | phase2 | table | A merchant of record launches in weeks, local presence in months; through Yuno the move happens without a rebuild. |
| 73 | d08 | divider | 08 Next steps |
| 74 | next | next_steps | Three weeks, owners on both sides, and a decision by 23 October so provider onboarding can start in time for Black Friday. |
| 75 | closing | closing | Let's grow together · German Tatis, Senior Account Executive, Yuno |
| 76 | dA | divider | Appendix: LatAm deep dive and sources (split rule in the sub-line) |
| 77 | cty-br | country_deepdive | Brazil is the launch market: Pix and domestic cards carry more than 80% of online purchases and confirm in seconds. |
| 78 | cty-br-connections | logo_grid | Brazil: EBANX and dLocal are two of 46 providers live through Yuno; Pix is carried by 27 of them. |
| 79 | cty-ar | country_deepdive | Argentina is a wallet market where the 30% perception makes local-currency pricing the whole game; MODO arrives via dLocal. |
| 80 | cty-ar-connections | logo_grid | Argentina: 23 providers live through Yuno; MODO and interoperable QR reach the Shop only through dLocal. |
| 81 | cty-mx | country_deepdive | Mexico is a debit market: three in four online buyers pay with debit cards foreign acquirers decline; the MoR must look domestic. |
| 82 | cty-mx-connections | logo_grid | Mexico: 36 providers live through Yuno; SPEI and OXXO reach the Shop through either MoR, CoDi and 7-Eleven through dLocal. |
| 83 | cty-co | country_deepdive | Colombia is an account-to-account market: PSE carries 64% of e-commerce transactions and Bre-B is the next rail; cards a third. |
| 84 | cty-co-connections | logo_grid | Colombia: 31 providers live through Yuno; PSE is carried by 12 of them and Bre-B by dLocal today. |
| 85 | cty-bo | country_deepdive | Bolivia is the clearest case for a second provider: EBANX direct means cash vouchers only; dLocal adds cards and QR on day one. |
| 86 | cty-bo-connections | logo_grid | Bolivia: dLocal is the route for cards, QR and cash through Yuno; EBANX in Bolivia stays an open item. |
| 87 | risks | table | Every modeled number in this deck rests on nine assumptions, each with an owner and a replacement path. |
| 88 | sources | sources | Every page behind this deck, read on 15 October 2026 unless dated otherwise. |

Slide count: 42 against the 30 to 34 target. The two slides the coordinator added on 15 Oct ("What we heard", "On us"), the eight section dividers plus the appendix divider (9) and the mandatory appendix (12) account for the difference. If the coordinator wants fewer, the candidates are the four dividers d02, d04, d06, d08 (kickers already carry the section name) and the trusted-by template keep.

## Build sequence
1. All 42 slides built in one pass with the five pricing-dependent slides (exec, bc-tiers, bc-scenarios, bc-ticket, proposal) as visible in-position placeholders, per the coordinator's instruction to wait for pricing v3.
2. On the coordinator's go, the five were written from the regenerated `model/bc_numbers.md`, `model/model_numbers.json` and `model/proposal_slide_content.md` (v3) and replaced in place with `--only … --replace`, so positions hold.
3. Two thumbnail passes with `qa_thumbs.py --from 47`; fixes below; final pass is 38 clean, 4 with findings that are template text or bounding-box overlaps (see "Not resolved").

## Engine changes (gs_engine.py, documented in SPEC_SCHEMA.md where user-facing)
- `PILLS`: added `ESTIMATE` (purple #5B3FA0 on #EEE9F8), the fourth house label; without it `validate()` rejected the tag.
- `r_exec_summary`: the right-card loop reassigned `bh`, so the bottom band was placed with the last card's body height and its text spilled over the source line (visible on the first thumbnail of slide 50). Loop variable renamed; band now sits at `363 - bar_h`.
- `SB.table`: header font is now `max(font_size - 0.5, 6.5)` so a 6.5 pt body table (country method tables) no longer prints a 6 pt header below the floor; `min_font` updated the same way.

## Changes after seeing thumbnails
- exec (50): band overflow (engine bug above); headline cut to two lines; third left item shortened (its three-line body ran into the next title); right cards trimmed to fit.
- bc-tiers (64): headline cut to two lines (the third line sat on the legend); legend name for Option B shortened; the 50K net benefit of ($1.1K) is drawn as a zero-height bar with the label "($1.1K)" above the baseline, because a true negative bar of 1 pt hung into the axis labels.
- proposal (68): headline cut to two lines (it collided with the sub-line); sub-line to one line; "Payment methods, PSPs and fraud solutions" and "Checkout and SDKs (web, iOS, Android)" wrapped inside 12 pt rows and were shortened to "Methods, PSPs, fraud solutions · 1,000+" and "Checkout, web and mobile SDKs"; left note and right paragraph shortened to fit the cards.
- Country slides (77, 79, 81, 83, 85): lever "money" lines wrapped to two lines, shortened to one ("$9K incremental GMV a month, one fifth" etc.); five stat labels over ~33 characters shortened; Bolivia box body shortened to one line; headlines cut to two lines so the bottom row has room (the three-line variant left 78 pt for a table that needs 85).
- onus (69), launch (71), phase2 (72): three-line bodies or headlines collided with the next element; shortened to two lines.
- options (56): headline cut to two lines and all cells to 60 characters or fewer so six rows plus footer and closing line fit; closing line cut to one line.
- arrangement (57): headline cut to two lines; MoR boxes 66 pt and the note box 36 pt so the diagram stays inside the zone.
- risks (87): column widths changed to [0.20, 0.24, 0.30, 0.13, 0.13] and every cell cut to one line; the "Carry1st estimate" free-text chip replaced by the ESTIMATE pill (the chip was wider than the column).
- sources (88): footnote cut to one line; column 2 items shortened.
- stands (53): three middle items instead of four so the card fits above the band.

## Not resolved (coordinator to decide)
- trusted (62): deleting the SpaceX image leaves a visible empty slot at the start of the second logo row. The other 19 logos (xAI, Qatar Airways, Samsung, Zuora, crypto.com, Kraken, Open English, fever, Whop, GoFundMe, Ant Group among them) are German's template set, not re-verified against y.uno for this audience; drop the slide if any of them should not be shown to Carry1st.
- qa_thumbs findings that remain: 6 pt kicker text on the two template keeps (template text, not engine text); three 0-width vertical hairlines on the four-pillars template reported as OUT (template artefacts); label bounding boxes on the bar chart ("$45.0K" x "$49.0K" etc., 13 x 6 pt) and on the proposal's tranche rows ("TRANCHE 1" x "0.30%", 3 x 9 pt) overlap as boxes but not as glyphs on the thumbnails.
- bc-ticket (66): the table ends about 60 pt above the source line; the slide reads a little empty but every number the coordinator asked for is on it.
- next (74): the three cards take their natural height; about 60 pt of white space under the contact bar.
- The Yuno integrations directory and the EBANX docs disagree on two points that the deck carries as OPEN rather than resolving: EBANX cards in Bolivia (directory yes, EBANX docs cash only) and EBANX PSE in Colombia (the adidas-pull methods table lists EBANX under PSE; the research note said "not in the directory local list"; the deck says "dLocal, EBANX, PayU, Kushki, Wompi" per the methods table and asks to confirm on Carry1st's account).

## Open items mentioned in the speaker notes or on slides (owner)
- Volumes by country, EBANX's proposed rates, Carry1st's take rate on GMV, Shop margins (Cordel).
- Tax treatment per country under each MoR, in writing from EBANX and dLocal; IOF (Brazil), 30% perception (Argentina), IVA (Mexico 16%, Colombia 19%) (German).
- EBANX card coverage in Bolivia; QR enabled on the Yuno dLocal Bolivia connection (Yuno integrations, German).
- EBANX PSE Avanza and Bre-B enabled on Carry1st's account in Colombia (German with EBANX).
- EBANX and dLocal rates through Yuno for the MDR lever (Justo).
- Third mobile-games reference, not named on any slide (Justo).
- Implementation lead (Mauricio or Alfredo) and prototype access for Fatih's team after the call (JP, German).
- Fatih's full name and title are not in any public source; the deck uses "Fatih" as on the call (German).

## Hygiene checks run on the final spec
No em dashes, no " - ", no exclamation marks, no "no small feat", no minimum / list price / discount / starting at / from or up to next to a price, no 450+ / 460+ (except the find-string of the template rewrite), no +12%, no McDonald's percentage or dollar figure, no Moon Active, Riot, Saudi, GCC, Pay1st, partnership or pocket concessions. USD only. PayPal appears only in wallet chips, never as a PSP.

## Reframe pass (15 Oct 2026, evening): EBANX plus any rail, Luni-format business case, 39 slides
- Framing: EBANX plus any local rail, acquirer, APM or additional MoR through Yuno; never "EBANX and dLocal". Connection slides now show "Merchant of record at launch" (EBANX) and "Local rails and acquirers live through Yuno (N)"; headlines lead with the provider count.
- Removed: `launch`, `d08`, `next` (live slides deleted). `d07` is now "Phase 2: merchant of record or local presence"; agenda and every divider list 01 to 07 plus Appendix (edited in place: agenda and divider types cannot be re-created after `--final`).
- `heard` rewritten as Yuno's read of what the launch has to get right (no names, no "you asked").
- Business case: `bc-tiers` and `bc-scenarios` replaced by `bc-levers` (`lever_grid`) and `bc-impact` (`impact_table`), Luni format; annual per-lever values at 450K from `model/model_numbers.json` (x12, contribution view): totals $280K / $574K / $950K vs Yuno $225K a year. `bc-ticket` kept.
- "For: Carry1st" footer removed everywhere (spec footer is empty; leftover shapes deleted live, 0 remain).
- Live update ran through `apply_reframe_live.py` (one-off): `--replace` matched old slides by id prefix, which breaks once slides are removed from the spec; `gs_engine.py` now matches by position on a finalized deck.
- Live cover subtitle still reads "One integration for five markets, EBANX and dLocal behind it, priced on what Carry1st sells" (left as instructed; to decide).
NOTE 16-oct: phase2 + d07 removed live and from deck_spec.json; make_spec.py still generates them, remove there before regenerating.
