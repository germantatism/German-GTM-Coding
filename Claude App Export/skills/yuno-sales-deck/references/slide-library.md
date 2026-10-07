# Slide library: patterns and copy templates

Contents: [Anatomy](#anatomy-of-every-content-slide) · [Writing titles](#writing-titles) · [Patterns](#patterns) · [Reusable copy](#reusable-copy-adapt-never-paste-blind)

Each pattern lists the helper in `scripts/yuno_deck.js` that draws it. Replace every `<...>`; if you can't fill one with a sourced fact, cut the element.

## Anatomy of every content slide

```
KICKER · ALL CAPS, SMALL, BLUE            (section · topic)
Action title: one full-sentence conclusion, max two lines
[ body: ONE chart, table, diagram or tile row ]
[ optional: SO WHAT / HONESTY GUARDRAIL / BOTTOM LINE bar ]
Source: ... · TO VALIDATE: ...                     Yuno × <Merchant> · Confidential   n
```

## Writing titles

- Types A, B, D: the title is the conclusion, with a number when there is one. Test: if the audience reads only the titles, do they get the argument?
  - Weak: "Market overview" → Strong: "82% of your users are international, but just ~45% of bookings"
  - Weak: "Our solution" → Strong: "Keep Stripe direct. Add Yuno alongside it. Zero infra risk, full upside."
  - Weak: "Risks" → Strong: "A concentrated, brittle payment stack, disclosed in your own filing"
- Type C: short declarative labels (2-6 words) plus a bold caption at the bottom that carries the point: "One Payment Object" / "One schema. Nothing discarded."
- Country pages: "<Country>: <the local-payment insight with a number>" ("Germany: PayPal + SEPA Direct Debit are 43% of online revenue; cards 14%").
- Write to them: "your users", "your filing", "your stack".

## Patterns

**Cover** · `cover()` · dark hero with the `yuno | <merchant logo>` lockup top-left (German's cover convention: no greeting, no large logo block), title "Yuno × <Merchant>", thesis line, descriptor, CONFIDENTIAL · PREPARED FOR · date.

**Why we are here** · `twoColumn()` · Left header WHAT WE SEE TODAY: three items "**<Observation with number>** / <one sentence of proof and where it comes from>". Right header WHAT YUNO SOLVES, ABOVE <INCUMBENT>: three-four items "**<Capability>** / <one sentence> / chip: ~<quantified outcome>". Bottom bar: "One integration, live in weeks, with <incumbent> untouched: ~$X a year at conservative inputs. The rest of this deck shows the math."

**At a glance / homework** · `statTiles()` · six tiles: big number, label, one-line context, tag [F]/[E].

**How money moves** · `flow()` · 3-4 nodes left to right, providers under each node, "YUNO OPERATES HERE" tag above the nodes we touch, one fact under the diagram (take rate, fee, payout rate).

**The reframe** · `quoteReframe()` · left: paraphrase of their statement + source; right: WHY THIS REFRAMES THE CONVERSATION with three lines (not a new idea · Yuno accelerates and globalizes it · the remaining upside is ...).

**Lever insight** · `chartSlide()` · one native chart (grouped bars for "share of users vs share of revenue by region"; wedge bars for fee deltas; line for cumulative savings) + right-hand callout with the single number + guardrail box.

**Decision frame** · `comparisonTable()` · rows: each gap with a sub-line and "$ at stake"; columns TODAY / OPTION A / OPTION B; cells are short phrases with a rating mark (○ ◐ ●). Closing bar: "Option A captures a fraction of the $X. Option B captures the full $X, because ...".

**Keep-the-incumbent architecture** · `twoBox()` · left box "<Incumbent> (direct) · existing integration preserved": what stays, fallback if Yuno is unavailable, no migration. Right box "Yuno orchestration layer · one new integration": local methods, cross-PSP retries, local acquiring, unified dashboard and reconciliation.

**Advantage table A-E** · `advantageTable()` · Domestic-first routing · Recurring beyond cards · Best local payment methods · Full-fidelity controls and data · Cost and resilience. Columns: Why this matters for <Merchant> | What PSP-only misses. Rewrite the middle column for their model.

**Authorization charts** · `dualBars()` · 83% → 93% and 93 / 94 / 96%, with source and the reconciliation footnote.

**Four-layer architecture** · `layers()` · Experience / Control (Yuno) / Connectivity (name their PSPs + "20 more") / Rail; side list 01 CIT, 02 MIT, 03 Resilience and ops.

**Three pillars** · `pillars()` · Local rails network · Intelligent orchestration · Unified data and treasury; three bullets each, vertical-flavored.

**Priority markets table** · `marketsTable()` · # | Country | demand est. | incremental value | dominant play | archetype, with sidebar totals and concentration. Archetypes: Full-stack (methods + local acquiring + retries) · APM-led · Mature (preferred methods + renewal recovery).

**Methodology bridge** · `waterfall()` · starting point → + lever 1 → + lever 2 → + lever 3 → total; caption each step in plain words ("Add local ways to pay", "Fix declined cards", "Save failed renewals").

**Scenario table (the value)** · `scenarioTable()` · Lever | Mechanism | CONSERVATIVE | BASE | UPSIDE, totals row, "what dominates" mini-bar, guardrail box.

**The return** · `returnTable()` · value, less Yuno investment, net benefit, ROI, payback × three cases; big callout "13.5x return, base case".

**Build vs buy** · `buildVsBuy()` · two columns with time to value, run-rate, one-time build, 3-year total, headcount, maintenance, opportunity cost; headline delta.

**What it rests on** · `floorRange()` · horizontal bar from floor to full range; four swing variables; "THE ASK: two data files turn this from illustrative into underwritable".

**Why move now** · `threeColumns()` · LOCALIZATION TAKES TIME (4-12 weeks per market via orchestration vs 6-18 months per direct integration) · DEMAND IS INFLECTING NOW (a dated fact) · THE WINDOW IS SHORT (the named competitor move). Bottom: CAPTURE TODAY / WIN TOMORROW.

**Country page** · `countryPage()` · see blueprint in `deck-types.md`. Footer always: "Source: <2-3 named sources with dates> · TO VALIDATE: <Merchant> <country> demand, checkout starts, paid conversion, method mix, decline codes".

**Required inputs** · `numberedCards()` · six cards: data point / Why / Use.

**Data sprint (next step)** · `timelineAsk()` · four blocks DAYS 1-3 Data exchange · DAYS 4-7 Model calibration · DAYS 8-11 Implementation roadmap · DAYS 12-14 Pilot scope and business case; right side WHAT WE AIM TO GET DONE (four checks); BOTTOM LINE bar.

**The Ask** · `ask()` · three numbered asks with generous spacing; the first is their data under NDA; footer "Proposed dates: ____".

**Honestly slide** · `threeColumns()` · WHAT'S LIVE | WHAT STAYS | THE MODEL.

**Partnership** · `twoColumnList()` · THROUGH GO-LIVE | ONGOING PARTNERSHIP; closing line on incentives (no professional-services revenue model).

**Section divider** · `divider()` · dark full-bleed (Unity Black), big label ("THE REALITY", "OUR COMMITMENT", "APPENDIX").

Note: only some pattern names above exist as functions in `scripts/yuno_deck.js` (see `design-system.md` for the actual API). For the others, compose the pattern from `table`, `columns`, `statTiles`, `callout`, `bar`, shapes and `tx`.

## Reusable copy (adapt, never paste blind)

Copy rules on every slide: no em-dashes and no " - " as punctuation (commas, periods, colons, or a new sentence); never the phrase "no small feat"; amounts in USD only; "~" on estimates; Yuno-wide stats are the published 7% uplift and 30% recovered revenue only.

- Guardrail: "The <X> is NOT Yuno-addressable. Our surface is <Y>, never the full <Z>."
- Guardrail: "Authorization uplift is capped at 2-3% on baselines above 90% and shown net of ~<n>% contribution margin. Incremental to what <Merchant> already captures."
- Waterfall logic: "Local methods expand the paid base. Localized processing improves approval on the remaining card attempts. Retries recover failed renewals on the resulting base. The levers are not three independent user pools."
- Important box (lever 1): "This is not a claim that every <method> user is incremental. It estimates how much existing <Merchant> demand could convert once preferred local methods are available."
- Important box (lever 2): "Lever 2 is not about finding new users. It recovers users who already tried to pay but were declined because the transaction was routed cross-border. Hard declines are excluded through the recoverable-share assumption."
- Reframe: "This isn't a new idea we're selling you. It's a strategy you've validated and prioritized. Yuno's job is to accelerate and globalize it."
- Architecture promise: "Additive above your existing rails. No rip-and-replace, with instant fallback. Rollback is a configuration change."
- Ask #1: "Your data, under NDA: decline file by ISO code, channel mix, auth rates by BIN and country. The next thing you see from us is your model, not ours."
- Bottom line (data sprint): "<Merchant> keeps <incumbent> as the global baseline. Yuno orchestrates the layer around it, adding methods, routing locally and recovering failures, with all economics validated against <Merchant>'s own data."
- Checkable claims footer: "All five are checkable. Please check them."
- Honesty footnote: "<Feature A>: shipped. <Feature B>: on roadmap."
- Build vs partner closers: "Focus on core business, not banking." · "The hidden maintenance tax: Day-2 compliance updates and API changes absorb a large share of engineering time." · "Speed is revenue: every month spent building the pipe is a month of margin not captured."
- Close: "Let's grow together."
