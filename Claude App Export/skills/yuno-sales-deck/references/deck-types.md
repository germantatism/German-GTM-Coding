# Deck types: slide-by-slide blueprints

Contents: [A. Strategic business case](#a-strategic-business-case-the-master-deck) · [B. First-meeting deck](#b-first-meeting-deck) · [C. C-suite product session](#c-c-suite-product-session) · [D. Commercial proposal](#d-commercial-proposal) · [E. Customer workshop / QBR](#e-customer-workshop--qbr) · [Optional modules](#optional-modules)

Format of each line: **KICKER** · action-title pattern · what goes on the slide · origin (G = Germán, S = Samuel).
Blueprints are a starting order, not a cage. Drop slides that have no real evidence behind them; a shorter deck with proof on every slide beats a complete one with filler.

German structures every deck top-down as **Requirement, Benefit, Proof (RBP)**: diagnose what they need, organize what Yuno delivers against it, then substantiate it with verified evidence. In Type A, Acts 1-2 are the Requirement, Act 3 the Benefit, Act 4 the Proof, and Act 5 is why now and The Ask. Every slide should be checkable as an R, a B or a P; the Proof step is verified facts only, never assumed or padded.

---

## A. Strategic business case (the master deck)

The merged flagship. Story arc: *we know you → here is where money leaks → here is the decision → here is the math, sized honestly → here is the return → here is how little we ask to prove it.*

**Act 1 · We know you**
1. **Cover** · "Yuno × <Merchant>" + a one-line thesis in their language ("The payments backbone for the next billion users") + "A business case for payments orchestration" + CONFIDENTIAL · PREPARED FOR <MERCHANT> · <MON YYYY>. Source list small at bottom. (S)
2. **WHY WE ARE HERE** · "<Merchant> scaled to $X on <one processor / N processors>. Everything that leaks from here, Yuno can solve." · Left: WHAT WE SEE TODAY = three observations, each a bold claim plus one sentence of public proof. Right: WHAT YUNO SOLVES, ABOVE <INCUMBENT> = three or four blocks each with a quantified chip. Footer bar: one sentence with the hero number and "the rest of this deck shows the math". (G)
3. **WE'VE DONE OUR HOMEWORK** · "<Merchant> at a glance: <the one-line characterization>" · six stat tiles from filings or strongest public sources (revenue/bookings, growth, users, geography split, cash flow, a model-specific stat). Tag [F]/[E]. For private companies, merge with industry context: category size, their rank, what defines the category this year. (S + G)
4. **HOW MONEY MOVES** · "<Their economy>: N nodes where Yuno operates" · flow of funds (pay-in → spend/platform → payout) with YUNO OPERATES HERE tags and their current providers named at each node. (S)
5. **THE REFRAME** · "You've already chosen this strategy, at the <board / product / hiring> level" · paraphrase of their own statement (filing, CEO letter, launch, job posting) + three lines: this isn't a new idea; Yuno's job is to accelerate and globalize it; the remaining upside is X. Include a PROOF IT WORKS chart if they or a third party have quantified results so far. (S)

**Act 2 · Where it leaks and what the decision is**
6. **EXECUTIVE SUMMARY · THE OPPORTUNITY** · "<Merchant> can unlock ~$X/year by fixing N leakage points across <scope>" · hero number, three tiles (addressable base, largest lever, other levers), closing paragraph that ends with the proposed next step. State the number as "preliminary, outside-in" and as a % of their revenue. (G)
7. **LEVER slides (one per lever, 2-4)** · each title states the insight with a number ("82% of your users are international but just ~45% of bookings") · one chart or wedge diagram + an HONESTY GUARDRAIL box saying what is not addressable. (S)
8. **DISCLOSED RISK · CONCENTRATION** · "A concentrated, brittle payment stack, disclosed in your own filing" · share of volume on one processor, receivables concentration, outage history if public. If no filing: build it from checkout inspection and their processor's case study. (S)
9. **DISCLOSED RISK · MARGIN LEAKAGE** · fraud/disputes (and scheme monitoring thresholds if complaints are visible), cross-border declines, FX. Only what you can source. (S)
10. **STRATEGIC CONTEXT · THE DECISION FRAME** · "<Incumbent> alone leaks revenue at N points, and a second PSP only fixes one" · table: rows = friction gaps with $/mo at stake; columns = TODAY | OPTION A + second PSP | OPTION B + Yuno. Use the competitor actually in the account (e.g. an orchestrator already doing disputes for them), not a generic Adyen. (G)
11. **PROPOSED ARCHITECTURE** · "Keep <incumbent> direct. Add Yuno alongside it. Zero infra risk, full upside." · two boxes: existing integration preserved (what stays, fallback) vs new integration (what one API unlocks). (G)

**Act 3 · What Yuno is (keep tight: 3-5 slides)**
12. **THE RESOLUTION · WHAT YUNO IS** · "A single orchestration layer beats connecting to PSPs one by one" · advantage table A-E: Advantage | Why this matters for <Merchant> | What PSP-only misses. (S)
13. **THE RESOLUTION · AUTHORIZATION** · "Two structural levers lift authorization: local routing + resilience" · two bar charts (cross-border vs local route; 1/2/3 providers) + the footnote that reconciles the slice-level uplift with the net figure used in the valuation. (S)
14. **THE RESOLUTION · ARCHITECTURE** · four layers (experience / control / connectivity / rail) "sitting above your existing rails", with 01 first purchase (CIT), 02 renewal (MIT), 03 resilience and ops. Name their providers in the connectivity layer. (S)
15. **THE RESOLUTION · BREADTH or PRODUCT MODULE** · product suite mapped to their flows (pay-in $ and payout $), or a product deep-dive module (see Optional modules). (S/G)
16. **TRUST & COMPLIANCE** · certifications as badges + three benefit cards written for their specific obligation (minors' data, PCI scope, data residency). (S)

**Act 4 · The math**
17. **PRIORITY MARKETS** · "<Incumbent> does <home markets> well. Yuno fills the gaps and reinforces those markets" · table of top markets: demand est. | incremental value | dominant play | archetype (Full-stack / APM-led / Mature) + sidebar with portfolio total, concentration (top 3, top 10), archetype split. Only for multi-market cases. (G)
18. **METHODOLOGY BRIDGE** · "How we sized the levers: start with existing demand, then remove leakage step by step" · waterfall 0→N with the WATERFALL LOGIC caveat that levers are sequential. (G)
19. **ECONOMICS · THE VALUE** · "N levers, sized honestly, and gated on your data" · table: lever | mechanism | CONSERVATIVE | BASE | UPSIDE + what dominates + honesty guardrail. (S)
20. **ECONOMICS · THE RETURN** · "Every $1 to Yuno returns roughly $a-$b, and pays back in <time>" · value − Yuno investment = net benefit, ROI, payback per scenario. With approved deal pricing, or with Yuno's standard pricing labeled as such (first $50,000 processed free, then $0.05 per transaction; see `value-model.md`, guardrail 11). Skip only if German says pricing must stay out. (S)
21. **ECONOMICS · BUILD VS. BUY** · 3-year TCO, time to value, headcount, maintenance, opportunity cost; anchor headcount on their disclosed engineering numbers. (S)
22. **ECONOMICS · WHAT IT RESTS ON** · floor vs full range bar, the swing variables, and the data that turns "illustrative" into "underwritable". (S)

**Act 5 · Why now, why us, what next**
23. **STRATEGIC LOGIC · WHY MOVE NOW** · cost of delay with a *named* competitor move (someone already localizing, launching, or hiring for it) + three columns: localization takes time / demand is inflecting / the window is short. Do not claim "near zero paid users" or similar if their own revenue mix disproves it. (G)
24. **WHY US** · five reasons + "Why Yuno vs other orchestrators" (local-rail breadth, no lock-in, payments-as-a-service) + stats (Yuno-wide figures are the published 7% authorization uplift and 30% recovered revenue only) + vertical-relevant customers, names as text. (S)
25. **PARTNERSHIP · WHAT YOU GET** · through go-live (forward-deployed engineers, solutions engineering, onboarding) | ongoing (KAM, TAM, tier-3, exec sponsor + QBRs, 24/7 support) and, for multi-market deals, the dedicated regional teams / 60-day wallet BD sprint. Commit only to what German confirms for this deal size. (S + G)
26. **ECONOMICS · COMMERCIAL MODEL** (optional, approved pricing only) · success-based, tranches, ramping minimum, what's included, metered add-ons. (S)
27. **IMPLEMENTATION** · "Production in weeks, not quarters" · Phase 0 scope and connect → Phase 1 pilot on a contained slice → Phase 2 expand; chips: "Rollback = a configuration change", "Additive above your existing rails". (S)
28. **REQUIRED INPUTS** · "N <Merchant> data points convert this strategic case into a board-grade forecast" · each with Why and Use. (G)
29. **THE ASK / PROPOSED NEXT STEP** · two-week joint data sprint (Days 1-3 data exchange, 4-7 model calibration, 8-11 roadmap, 12-14 pilot scope) + what we aim to get done + BOTTOM LINE bar. First ask is always *their data under NDA*: "the next thing you see from us is your model, not ours." Close with "Let's grow together" + thesis line. (G + S)

**Appendix** (leave-behind): "How to read the numbers in this deck" (working assumptions table, caveats and positioning language, sensitivity) · one country page per priority market · lever ranking tables · lever methodology pages (formula, worked example, IMPORTANT honesty box).

**Presenting it live:** tell German to present ~8: slides 2, 4 or 5, 6, 10, 11, 19, 22, 29. Everything else is leave-behind.

---

## B. First-meeting deck

Goal: earn the second meeting and the data. 12-15 slides. Assume they know little about orchestration and you know little about their stack; be explicit about what you inferred.

1. Cover · "Yuno × <Merchant>" · month, year.
2. **EXECUTIVE SUMMARY** · two columns: CONTEXT (3-4 bullets on their situation, each sourced) | WHAT <MERCHANT> CAN GET FROM PARTNERING WITH YUNO (measurable uplift · operational efficiency · strategic acceleration), each with a number and its basis.
3. **OUR UNDERSTANDING OF YOUR SETUP** · "The current setup has N constraints" · diagram Users → their PSPs with callouts naming the exact failure mode ("a decline on X doesn't fail over to Y"; methods missing in named markets; manual reconciliation). Mark inferred items "to confirm".
4. **WHAT YUNO IS** · advantage table A-E.
5. **AUTHORIZATION** · the two charts (local routing, multi-provider).
6. **ARCHITECTURE** · one control layer + local connectors, above their rails, CIT / MIT / resilience.
7. **OPERATING MODEL** · three pillars (local rails network · intelligent orchestration · unified data and treasury) with bullets flavored for their vertical.
8. **VALUE** · "Orchestration unlocks ~$X in estimated annual value via N levers" · lever | assumption | how it works | $/yr, revenue levers and cost levers, assumptions footnote, "illustrative, pending your data".
9. **BUILD VS PARTNER** · pros/cons + three closers (focus on core, the maintenance tax, speed is revenue).
10. **WHY YUNO** · five reasons, vertical-specific resilience line.
11. **PROOF** · stats + named customer results + logo wall relevant to their vertical.
12. **THE ASK** · three numbered asks (data under NDA · technical deep-dive · sandbox or pilot scoping) + proposed dates.

## C. C-suite product session

Goal: credibility with engineering-led leadership in a 60-minute session with several Yuno presenters. Short declarative titles (2-6 words) are right here, each paired with a bold caption line at the bottom. One idea per slide.

1. TITLE (wordmark, subtitle "Payments orchestration, shown live.", date; nothing else).
2. THE HOUR · agenda rows with owner and minutes · "Interrupt us anywhere."
3. YUNO IN NINETY SECONDS · founding line + four big stats + vertical-relevant customer strip.
4. WHERE WE'RE DIFFERENT · five numbered one-liners · "All five are checkable. Please check them."
5. ONE PAYMENT OBJECT · PAYMENT → TRANSACTIONs → *their* providers; normalized status + raw code preserved · "One schema. Nothing discarded."
6. ROUTING: RULES + ML, FULLY AUDITABLE · "Your rules always win."
7. THE FRONT END · SDK depths, PCI L1 vault → their SAQ-A posture; address their known data concern.
8. INTEGRATION VELOCITY · three huge numbers + honesty footnote (what's shipped vs roadmap).
9. UPTIME AND SCALE: WHAT WE PUBLISH, WHAT WE SIGN · published (status page) vs signed (contractual SLA); placeholders flagged for internal confirmation; joint load test on *their* peak events.
10. FALLBACKS: WHAT HAPPENS WHEN THINGS BREAK · three layers + "And if Yuno itself is down?"
11. DATA RESIDENCY · map + minimization / deletion / transparency.
12. LIVE DEMO: YOUR STACK · their providers, numbered demo beats; calm holding frame.
13. <TOPIC>, HONESTLY · WHAT'S LIVE | WHAT STAYS | THE MODEL (for the area where Yuno is partial, e.g. payouts).
14. THE PATH TO <DATE> · scoping → sandbox and certification → 5% cohort → validate vs incumbent → ramp on evidence; chips for rollback and forward-deployed engineers.
15. THE ASK · three numbered asks, data first · proposed dates.

## D. Commercial proposal

Goal: get to signature. They know Yuno. Modest, credible numbers and pricing they can compute themselves.

1. Cover.
2. Agenda (01 Our understanding of the context · 02 Why Yuno · 03 Business case · 04 Pricing · 05 Next steps); reuse as section dividers.
3. EXECUTIVE SUMMARY · one-line who they are · their stack headline ("3 processors with no orchestration") · KEY CHALLENGES (from calls, in their words) · WHAT YOU GET (three blocks).
4. CURRENT SETUP · diagram with the constraints named.
5-9. WHY YUNO · stats · five reasons · suite · advantage table · credentials with named customer metrics · leadership team (for buyers who care who is behind it).
10. BUSINESS CASE · "Small performance lifts compound into meaningful impact" · four levers (operational + cost), How it works, Conservative, Optimistic. Mid-market ranges: +0.5-1.0% conversion, +0.75-1.0% routing/retries, 7.5-12.5 bps cost, 3-4 FTE.
11. TOTAL IMPACT · scenario × levers table + average, set against their current monthly processing cost.
12-13. PRICING · Option A vs Option B, each with WHAT IT COVERS and WHAT IT MEANS FOR <MERCHANT> (all-in $/transaction at three volumes), term, ramp note. Approved numbers only; if the deal has no negotiated pricing yet, use Yuno's standard pricing (first $50,000 processed free, then $0.05 per transaction) and label it standard. Never invent tiers.
14. IMPLEMENTATION and TEAM · timeline in weeks, who they get.
15. NEXT STEPS · dated checklist to signature · close with German's name and title (Account Executive, Yuno).

## E. Customer workshop / QBR

Agenda with times and owners · team introductions · what we've built since last time (company and engineering update) · *their* performance (approval, volume, incidents, open items, stated plainly) · their roadmap and feedback · two or three expansion topics tied to their asks (vaulting, payouts, reconciliation, new methods, 3DS) · commitments and owners with dates. Incidents get their own honest slide: what happened, root cause, what changed.

---

## Optional modules

Add when relevant; each is 1-3 slides and follows the same anatomy.

- **Country pages** (appendix): insight title · four stat tiles (local-payment proof stat, est. demand with range, incremental users, total impact) · three lever boxes · PAYMENT METHOD PRIORITY table (Must-have / Optional | method | scale | role) · BASE-CASE MODEL · SO WHAT · "Source … · TO VALIDATE: …". See `slide-library.md`.
- **Additional emerging markets (wave 2)**: population, internet penetration, localization gap, first-mover priority.
- **Subscriptions / billing**: engine layers · "<Billing system> stays. Payments route through Yuno." with UNCHANGED / WHAT CHANGES / NOT REQUIRED · their plans mocked up in the dashboard. Verify every claim against docs.y.uno (see `yuno-facts.md`, product nuances).
- **Payouts**: what's live / what stays / the model.
- **Vault / PCI proxy**: orchestrator, vault, or both; token portability; migration path.
- **Disputes and scheme monitoring**: when public complaints or a dispute vendor are visible; redundancy as insurance.
- **Cost of delay chart**: 24-month lines for "moves now / does nothing / competitor moves first". Use only with a named competitor signal.
- **Dedicated resources and 60-day wallet BD sprint**: for multi-market localization deals.
- **Team / leadership** and **credentials with customer quotes**.
