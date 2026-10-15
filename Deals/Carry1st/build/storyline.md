# Storyline · Carry1st Shop in Latin America by Black Friday (content agent, 15 Oct 2026, final after build)

One line per slide, generated from `deck_spec.json` so the QA agent can check alignment: index · position in the working copy (46 template slides + n) · id · type · action title (headline, verbatim) · the one number or claim · label. 42 slides. Pricing v3 throughout: $7,500 a month including the first $500K of monthly sales, then 30 bps to $3M, 25 bps to $6M, 20 bps above; $18,750 a month at $4.5M; footer "Rates locked, tranches reviewed annually as volume grows".

Appendix split rule (stated on the appendix divider): the three lever cards on each country slide carry one fifth of the base-case run-rate lever figures from `model/bc_numbers.md` (equal split, a placeholder until Carry1st's volume projections by country arrive): local methods $9K incremental GMV a month, approval and retries $36K incremental GMV a month, MDR leverage $4.5K saved a month (base case at 450K: $45.0K GMV, $180.0K GMV, $22.5K).

| # | Pos | id | type | Action title | The one number or claim | Label |
|---|---|---|---|---|---|---|
| 1 | 47 | cover | cover | Carry1st Shop in Latin America by Black Friday | One integration, two merchant-of-record providers, the economics at a $10 ticket |  |
| 2 | 48 | agenda | agenda | 01 to 08 plus Appendix | 01 to 08 plus Appendix (A) |  |
| 3 | 49 | d01 | divider | 01 Executive summary |  |  |
| 4 | 50 | exec | exec_summary | Through Yuno, EBANX and dLocal cost less than EBANX direct at run rate, add a second rail, and pay back in month two. | $44.2 vs $45.0 per $1,000 of sales at run rate (base); +$29.1K a month net, $349K a year, 2.6x; break-even about 65,000 tx a month; conservative cost-neutral at run rate | ESTIMATE |
| 5 | 51 | d02 | divider | 02 Where Carry1st stands and what Black Friday needs |  |  |
| 6 | 52 | heard | two_column | Three asks from Cordel and two from Fatih set the bar for this deck; each one has a section that answers it. | Five asks, close to verbatim, each mapped to a section | Carry1st, Oct 2026 |
| 7 | 53 | stands | scale | Five markets, a $10 average ticket and six weeks to Black Friday: the launch has to be fast, local and cheap per transaction. | $10 avg / $5 median; $4 to 5M a month by end 2027 (Cordel, estimate); 21 storefronts today | Carry1st estimate · PUBLIC DOCS |
| 8 | 54 | needs | four_numbers | In every launch market the method that wins is local and instant, and most of it sits outside international card rails. | Pix 42% (BR), PSE 63.9% (CO), wallets 46% (AR), debit 74% usage (MX) | PUBLIC DOCS |
| 9 | 55 | d03 | divider | 03 Two ways to launch |  |  |
| 10 | 56 | options | comparison_grid | EBANX direct can switch on all five markets with one integration; what it cannot give Carry1st is a second rail. | Rows closed: 0 of 6 direct · 1 of 6 with a second direct build · 6 of 6 through Yuno | PUBLIC DOCS · CONFIRMED |
| 11 | 57 | arrangement | diagram | Yuno sits between the Shop and both merchants of record: EBANX for what it covers, dLocal for what it does not, one integration. | One integration, two MoRs, local acquirers later without touching checkout | CONFIRMED · OPEN (EBANX Bolivia) |
| 12 | 58 | d04 | divider | 04 Why Yuno |  |  |
| 13 | 59 | why-rbp | table | Seven things the Shop needs in Latin America, what each one gets through Yuno, and how we prove it. | RBP table, 7 rows: requirement, benefit, proof, label | CONFIRMED · ESTIMATE |
| 14 | 60 | platform | template_keep | A complete suite · Four pillars · One brain (template 23, "460+ INTEGRATIONS" rewritten to "16 OFFICES") | 16 offices · 190+ countries · 1,000+ methods · 180+ currencies (template slide 23, 460+ rewritten) | CONFIRMED (y.uno/about) |
| 15 | 61 | proof | stats | The checkout already exists: a working prototype of the Shop on the Yuno SDK runs in four LatAm markets today. | 4 sandbox markets; up to 7% authorization uplift; 30% recovered revenue; inDrive 11 countries in under 8 months | CONFIRMED |
| 16 | 62 | trusted | template_keep | Yuno is trusted by leading companies worldwide (template 25, SpaceX image removed) | Template logo wall, SpaceX removed; NetEase, Garena among the logos | CONFIRMED (y.uno) |
| 17 | 63 | d05 | divider | 05 Business case |  |  |
| 18 | 64 | bc-tiers | bar_chart | The Yuno route costs $44.2 per $1,000 of sales at run rate against $45.0 direct, and covers its fee from about 65K transactions. | Option A $45.0 vs Option B $44.2 per $1,000 at 450K; net ($1.1K) / +$2.6K / +$9.9K / +$29.1K; break-even about 65K | ESTIMATE |
| 19 | 65 | bc-scenarios | table | Processing savings carry the case, then engineering avoided, then approval: the base case returns $29.1K a month net at run rate. | Net at 450K: +$4.6K / +$29.1K / +$60.5K a month; 41.7 bps all-in needs +4.2% approved sales at 10% margin, +2.1% at 20%; published uplift up to 7% | ESTIMATE · CONFIRMED |
| 20 | 66 | bc-ticket | table | A fixed fee doubles as a share of sales when the ticket halves; a share of sales does not: usage on a $5 purchase is one to two cents. | $5 median at 450K: 0.57% of sales, $0.028 per tx; marginal usage $0.015 / $0.0125 / $0.010 vs $0.05 or $0.10 fixed | ESTIMATE |
| 21 | 67 | d06 | divider | 06 Proposal |  |  |
| 22 | 68 | proposal | pricing_cards | One platform fee covering the first $500K of monthly sales, then a share of sales that falls as Carry1st grows. | $7,500 a month incl. first $500K of monthly sales; 0.30 / 0.25 / 0.20%; $7,500 / $12,000 / $18,750 a month at 50K / 200K / 450K; 0.42% of sales at run rate | quoted price only |
| 23 | 69 | onus | two_column | What Yuno puts in before signing, and what the platform fee already covers. | Prototype, localization, provider negotiation; no setup fee; routing change not a fee; vault, risk, monitors, dashboard, 20 seats; KAM and TAM | Yuno commitment |
| 24 | 70 | d07 | divider | 07 Launch plan to Black Friday and Phase 2 |  |  |
| 25 | 71 | launch | table | Six weeks to 27 November: provider contracts and KYC are the critical path; the Yuno work is measured in days. | Week by week, decision in week 1, Brazil live (soft) in week 5, Black Friday in week 6 | PUBLIC DOCS · ESTIMATE |
| 26 | 72 | phase2 | table | A merchant of record launches in weeks, local presence in months; through Yuno the move happens without a rebuild. | Launch time, tax and FX, approval and CX, cost, when it makes sense, Yuno's role | PUBLIC DOCS · OPEN (tax per MoR) |
| 27 | 73 | d08 | divider | 08 Next steps |  |  |
| 28 | 74 | next | next_steps | Three weeks, owners on both sides, and a decision by 23 October so provider onboarding can start in time for Black Friday. | Decision date Fri 23 Oct 2026; owners on both sides for three weeks |  |
| 29 | 75 | closing | closing | Senior Account Executive, Yuno |  |  |
| 30 | 76 | dA | divider | A Appendix: LatAm deep dive and sources | Split rule in the sub-line: equal fifths until volumes by country arrive |  |
| 31 | 77 | cty-br | country_deepdive | Brazil is the launch market: Pix and domestic cards carry more than 80% of online purchases and confirm in seconds. | Pix 42% · $2.5B games · 93% of adults used Pix · 46 providers live | PUBLIC DOCS · CONFIRMED |
| 32 | 78 | cty-br-connections | logo_grid | Brazil: EBANX and dLocal are two of 46 providers live through Yuno; Pix is carried by 27 of them. | 46 live providers, 27 carry Pix | CONFIRMED (directory, Oct 2026) |
| 33 | 79 | cty-ar | country_deepdive | Argentina is a wallet market where the 30% perception makes local-currency pricing the whole game; MODO arrives via dLocal. | Wallets 46% · domestic-only cards 22% · MODO 17M+ · 30% perception | PUBLIC DOCS |
| 34 | 80 | cty-ar-connections | logo_grid | Argentina: 23 providers live through Yuno; MODO and interoperable QR reach the Shop only through dLocal. | 23 live providers; MODO and QR on dLocal only | CONFIRMED |
| 35 | 81 | cty-mx | country_deepdive | Mexico is a debit market: three in four online buyers pay with debit cards foreign acquirers decline; the MoR must look domestic. | Debit 74% usage · 77M digital buyers · 76M+ players, $2.3B · 36 providers live | PUBLIC DOCS |
| 36 | 82 | cty-mx-connections | logo_grid | Mexico: 36 providers live through Yuno; SPEI and OXXO reach the Shop through either MoR, CoDi and 7-Eleven through dLocal. | 36 live providers | CONFIRMED |
| 37 | 83 | cty-co | country_deepdive | Colombia is an account-to-account market: PSE carries 64% of e-commerce transactions and Bre-B is the next rail; cards a third. | PSE 63.9% · Bre-B 36M+ users · Nequi 28M · 31 providers live | PUBLIC DOCS |
| 38 | 84 | cty-co-connections | logo_grid | Colombia: 31 providers live through Yuno; PSE is carried by 12 of them and Bre-B by dLocal today. | 31 live providers, PSE by 12 | CONFIRMED |
| 39 | 85 | cty-bo | country_deepdive | Bolivia is the clearest case for a second provider: EBANX direct means cash vouchers only; dLocal adds cards and QR on day one. | QR 36% · cash 64% · $500 foreign debit limit · 6 providers live | PUBLIC DOCS · OPEN |
| 40 | 86 | cty-bo-connections | logo_grid | Bolivia: dLocal is the route for cards, QR and cash through Yuno; EBANX in Bolivia stays an open item. | 6 live providers; EBANX Bolivia OPEN (owner Yuno integrations); QR on dLocal OPEN (owner German) | CONFIRMED · OPEN |
| 41 | 87 | risks | table | Every modeled number in this deck rests on nine assumptions, each with an owner and a replacement path. | 9 assumptions with value, basis, owner and status pill | ESTIMATE · OPEN · PUBLIC DOCS |
| 42 | 88 | sources | sources | Every page behind this deck, read on 15 October 2026 unless dated otherwise. | 14 source lines, two columns | CONFIRMED · PUBLIC DOCS |

## Notes for the QA agent
- Stat hygiene: "up to 7% authorization uplift", "30% recovered revenue", "1,000+ payment methods, PSPs and fraud solutions" (shown as "Methods, PSPs, fraud solutions · 1,000+" on the proposal and "1,000+ METHODS" on the template platform slide), "190+ countries", "180+ currencies", inDrive "around 90% approval, 11 new countries in under eight months", Rappi "implementation time for new providers down to zero". No McDonald's percentage, no provider count, no "+12%", no "20 to 30%" as a Yuno claim (the Nuvei "20 to 30 points" line on the Mexico slide is a vendor claim, attributed to Nuvei and labelled PUBLIC DOCS).
- Template keeps: slide 23 four pillars with "460+ INTEGRATIONS" rewritten to "16 OFFICES" (y.uno/about, CONFIRMED); slide 25 trusted-by with the SpaceX image removed. Slides 22 (unverified $30B+ / 150+), 27 (Eventbrite-specific, "30+ APMs"), 45 (6 pt text, em dash, 99.99% SLA) are not kept.
- Moon Active is not named anywhere; the proof slide says "one more mobile-games reference is to be confirmed" (OPEN, owner Justo). The "Moon Active test access" deliverable appears as "test access to a live gaming checkout".
- Partnership, GCC, Saudi, Pay1st, Riot Games: absent from slides and notes. Pocket concessions (included TPV to $1M, launch credit, $2M step, 3-year lock) and Finance caveats: absent.
- Labels used as pills: CONFIRMED, PUBLIC DOCS, OPEN, ESTIMATE (added to the engine palette on 15 Oct 2026).
