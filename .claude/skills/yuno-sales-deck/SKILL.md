---
name: yuno-sales-deck
description: Builds German's master Yuno sales deck (.pptx) for a named merchant, research-backed and consulting-grade. Merges German Tatis's outside-in three-lever business cases (xAI, Anthropic, Higgsfield, Flair) with Samuel Vieira's Roblox decks (10-K-driven business case, C-suite product session, first-meeting deck). TRIGGERS: "build a presentation / deck / slides for [merchant]", "business case deck", "BC deck", "pitch deck", "proposal deck", "first-meeting or intro deck", "C-suite / exec presentation", "QBR or workshop deck", "deck like Roblox / Higgsfield / Flair", "deck for my call with [merchant]", "arma el deck / la presentacion / el business case de [merchant]", or turning account research, a POV or a business case into slides for a Yuno prospect or customer. Works with only a company name: it researches (local repo, memory, Gong, Slack, Gmail, Drive, Calendar, Glean, web), asks at most three questions, sizes the value, writes the storyline, builds the .pptx and runs QA. Not for deck.yuno.tools web decks (/builddeck), the Excel model (/business-case), MBRs (/mbr-builder) or Google Slides QBRs (/slide-builder).
argument-hint: <merchant> [A|B|C|D|E] [--pricing "..."] [--lang en|es] [--out <dir>]
---

# Yuno Sales Deck

Build the deck German would build with a free week: German's research depth, quantified levers and market-by-market math, with Samuel's restraint, honesty guardrails and use of the merchant's own disclosures as the evidence. The audience is a payments, finance or product leader who will check the numbers. The deck wins when they say "you clearly did your homework" and agree to the next step.

Skill root: `/Users/germantatis/Desktop/GTMCoding/.claude/skills/yuno-sales-deck/` (call it `SKILL_DIR` below). Repo root: `/Users/germantatis/Desktop/GTMCoding/` (`REPO`).

## German's house rules (non-negotiable, enforced by `scripts/deck_qa.py` where a script can)

These come from German's standing feedback across every project. They override anything else in this skill or its references.

1. **RBP structure.** Every deck is organized top-down as Requirement (diagnose what they need), Benefit (what Yuno delivers against it), Proof (verified evidence). Type A maps as Acts 1-2 = Requirement, Act 3 = Benefit, Act 4 = Proof, Act 5 = why now and The Ask. Each slide must be checkable as an R, a B or a P.
2. **Facts only. Omit, don't fabricate.** Every number and claim is verified, ideally corroborated by a second independent source, primary sources first. If it cannot be verified, it is left out. A disclaimer ("per public sources") is only for a real, sourced estimate worth keeping, never a cover for a guess. A shorter deck of true facts beats a fuller one with a single guess. Never seed defaults or pad a list to hit a count.
3. **No dashes as punctuation.** No em-dashes and no " - " between words anywhere in slide copy or speaker notes. Use commas, periods, colons or a new sentence. Hyphens inside compound words are fine.
4. **Never the phrase "no small feat".**
5. **USD only.** No local-currency amounts anywhere, country pages included. When a verified stat exists only in local currency, use a currency-free metric from the same source (users, transaction counts, shares, growth) instead of converting at an assumed rate.
6. **Published Yuno stats only.** Yuno-wide performance figures are the published 7% authorization uplift and 30% recovered revenue (source line "Yuno published figures · y.uno"), or verified client results (McDonald's +4.7% acceptance across 18 markets, $3.2M). Never "+12% auth uplift" or "20-30% decline recovery". Cross-PSP reconciliation is roadmap, not GA: footnote it.
7. **Standard pricing when there is no deal pricing.** First $50,000 processed free, then $0.05 per transaction, labeled "standard pricing". Deal-specific pricing from German overrides it and is labeled as such. Never invent tiers.
8. **PayPal is a wallet/APM, never a PSP.** Processor lists and counts hold gateways, acquirers/PSPs and merchants of record only. BNPL, wallets, card networks, issuers and local methods are payment methods.
9. **Client-reported metrics win.** If the prospect stated a number (average ticket, TPV, transactions), the deck uses it everywhere. Flag any discrepancy with a derived figure to German separately, never fix it silently.
10. **One merchant per deck, nothing from other accounts.** Never reuse another merchant's file as the starting point. Nothing about Riot Games ever goes to a third party. GoFundMe (Yuno's first live Marketplace merchant) is a reference only with German's OK on the details.
11. **Cover lockup.** The cover carries the `yuno | <merchant logo>` lockup top-left on a dark hero. No "Hello team" greeting, no large logo block.
12. **Official positioning line** when a narrative sentence about Yuno is needed: "Yuno is an AI native operating system for global financial infrastructure. We help companies orchestrate their payment stack across a fragmented ecosystem that includes payment methods, processors, antifraud tools, KYC/KYB providers, reconciliations, and stablecoins to lower payment processing costs, increase authorization rates, expand globally, and become more operationally efficient."
13. **Commit and push when done.** Stage only the deck folder you produced, commit, push to `main`.

## What "good" looks like (the merged DNA)

From German's decks:
- **Action titles.** Every content slide title is a full-sentence conclusion ("Stripe alone leaks revenue at four points, and a second PSP only fixes one"), with a small ALL-CAPS kicker above it (WHY WE ARE HERE, STRATEGIC CONTEXT, PROPOSED NEXT STEP).
- **A quantified lever model** with a hero number, a methodology bridge (waterfall), a priority-markets table, per-country pages and an appendix that shows every assumption.
- **Evidence from the merchant's public footprint**: processor case studies, help center, terms of use, job postings (hiring is a pain signal), traffic by country, reviews.
- **"Keep the incumbent" architecture**: Yuno sits above or alongside Stripe/Adyen. Nothing is ripped out.
- **A decision frame**: today vs. add a second PSP vs. Yuno orchestration.
- **A low-commitment next step**: a two-week joint data sprint with named data requests, plus Yuno's team commitment.
- **SO WHAT boxes, BOTTOM LINE bars, and a Source line on every slide.**

From Samuel's decks:
- **Their own words as the proof.** Facts from the 10-K, S-1, investor letters and risk factors, tagged [F] (filing/fact) vs [E] (third-party estimate). "A concentrated, brittle payment stack, disclosed in your own filing."
- **The reframe.** "You've already chosen this strategy. Yuno's job is to accelerate it." Sell acceleration of something they already believe, not a new idea.
- **How money moves.** A flow-of-funds slide with "YUNO OPERATES HERE" on the nodes we touch.
- **Honesty guardrails.** Say what is NOT addressable, cap uplifts, net out contribution margin and Yuno's cost, show conservative / base / upside, and show the floor you can prove. "Payouts, honestly." "All five are checkable. Please check them."
- **The return, not just the value**: ROI multiple, payback, build-vs-buy TCO, the commercial model.
- **Engineering-grade restraint**: white content slides, dark ink, one idea per slide, large numbers, simple box diagrams, a bold caption at the bottom, and the deck ends on **The Ask**, never on "Thank you".

Avoid what went wrong in past decks (all real, including German's Anthropic and Higgsfield decks): other merchants' names left in from a template, headline numbers that differ between slides (four different totals in one deck), "$" on a user count, 18 vs 20 markets, a country's MAU above the global MAU, an internal Spanish note left on a slide, a paragraph about another prospect inside "Why move now", competitor text left in the Yuno column of an architecture slide, a product slide that contradicted docs.y.uno, a headline the merchant's own facts disprove, levers sized on a modeled base while ignoring the merchant's existing revenue book. The QA step exists because of these.

## Workflow

Work through these in order. Do the research before asking German anything.

### 0. Locate the account and its history

- Find where the account lives: `REPO/Deals/<Merchant>/`, `REPO/Industry/<Vertical>/<Merchant>/`, `REPO/data/research/*<merchant>*`, `REPO/Business Cases/`. Read what exists: prior decks and PDFs, research briefs, meeting briefs, call notes, proposals, pricing already sent.
- Read the memory index `~/.claude/projects/-Users-germantatis-Desktop-GTMCoding/memory/MEMORY.md` and any `project_<merchant>.md`: deal state, contacts, decisions, what must never be said.
- Check the deck.yuno.tools research cache (`REPO/yuno-sales-pitch-maker/public/merchants.csv`, `src/data/business-overviews.json`, the Supabase `merchants` row): PSPs, missing methods, pains and footprint for 700+ merchants. It is a starting point, not a source; re-verify anything you use.
- If a deck for this merchant already exists, say so and build on it (same numbers, same positioning) unless German asks for a new one. Never contradict a number already sent to the account without flagging it.
- Output location: the account folder found above; if none exists, create `REPO/Deals/<Merchant>/`. Working files go in `<out>/build/` (`ledger.md`, `model.py`, `build_deck.js`, `qa.txt`). `--out <dir>` overrides.

### 1. Pick the deck type

Read `references/deck-types.md` and choose one. If the request doesn't make it obvious, infer it from the calendar invite and deal stage; ask one short question only if still unclear.

| Type | Use when | Length |
|---|---|---|
| **A. Strategic business case** (the master deck) | Enterprise prospect, exec audience, you need to create urgency with numbers | 20-27 main + appendix |
| **B. First-meeting deck** | Intro or discovery call, little known about their stack | 12-15 |
| **C. C-suite product session** | Technical or product deep-dive with several Yuno presenters, often with a live demo | ~15 |
| **D. Commercial proposal** | They know Yuno, pricing is approved, mid-market or late stage | 15-20 |
| **E. Customer workshop / QBR** | Existing customer | 12-20 |

### 2. Research (internal first, then public)

Follow `references/research-playbook.md`. In short:
1. **Internal**: the account folder and memory (step 0), Gong call transcripts (`mcp__claude_ai_Gong_MCP__ask_account` / `ask_deal`), Slack, Gmail, Drive, Calendar (today ± 2 weeks), Glean for internal docs. Look for an existing opportunity or owner, who is in the meeting, their stack, volumes, pains in their own words, and anything already promised or priced.
2. **Public**: filings and investor materials, the processor's customer story about them, help center and checkout (methods, currencies, billing behavior), job postings, traffic by country, reviews and complaints, competitors' payment moves, local-payment facts per priority market. For a full brief, run `/research <merchant>`.
3. **Product claims**: check against docs.y.uno (context7 MCP: resolve the docs.y.uno library, then query; or WebFetch the docs page) before they go on a slide.
4. Record everything in an **evidence ledger** (`<out>/build/ledger.md`): claim, number, source, date, tag ([F] merchant-disclosed, [E] third-party estimate, [Y] Yuno data, [A] our assumption). Every number on a slide must trace to a ledger row. If it isn't in the ledger, it doesn't go in the deck. Corroborate material facts with a second source.

### 3. Ask only for what you couldn't find

One message, at most three questions, each with your best-guess default so German can reply "go". Typical gaps: meeting goal and audience, deal-specific pricing (never invent it; standard pricing is the default), anything confidential he knows from calls. If the session is non-interactive or he doesn't answer, proceed with the defaults, tag them [A] in the ledger and list them in the hand-off.

### 4. Size the value

Follow `references/value-model.md`. Choose the 3-4 levers that fit this merchant's model (subscription, marketplace, airline, gaming, platform), size each one conservatively, and keep these rules:
- Size approval and renewal levers on the **existing revenue book first**, then on incremental users.
- Levers are **sequential, not additive**. Say so on the slide.
- Keep cited evidence and the model in the same units (a "7-12% relative lift" cannot justify "+2pp absolute on a 0.5% base").
- Show **conservative / base / upside**, the **floor** you can prove on their data, the headline **as a % of their revenue**, and the value **net of Yuno's cost** (deal pricing, or standard pricing labeled as such).
- State what is **not addressable** (app-store fees, sanctioned markets, invoiced enterprise volume).
- Compute every figure in `<out>/build/model.py` (see `REPO/Industry/AI/Higgsfield/model/higgsfield_three_lever_model.py` for German's three-lever reference model). Slide numbers are copied from its output, never typed.
If German also wants the spreadsheet, hand the same assumptions to `/business-case`.

### 5. Write the storyline before any slide

Draft a ghost deck: slide number, kicker, action title, the one proof on the slide, source, and its RBP letter. Read the titles top to bottom; they should tell the whole story on their own. Use the blueprint for the chosen type in `references/deck-types.md` and pull slide patterns and copy from `references/slide-library.md`. Yuno boilerplate (positioning line, published stats, standard pricing, proof points, team, certifications, support model, product nuances to verify) lives in `references/yuno-facts.md`.

For a Type A deck with a lot at stake, show German the title-only storyline first (it fits on one phone screen) and build after he reacts. Otherwise build straight through.

Language: English by default. Spanish when the account is Spanish-speaking (Palco, Yango, Localiza style accounts) or German asks (`--lang es`); then pass `--lang es` to `deck_qa.py` too.

### 6. Build the .pptx

Read `references/design-system.md`, then write `<out>/build/build_deck.js` using `SKILL_DIR/scripts/yuno_deck.js` (a pptxgenjs helper with the Yuno slide patterns: cover with lockup, divider, action slide, stat tiles, two-column, table, flow, phase bar, numbered, columns, native bars, waterfall, callouts, bottom-line bar, ask, close). pptxgenjs is installed under `SKILL_DIR/scripts/node_modules`, so `require("<SKILL_DIR>/scripts/yuno_deck.js")` works from anywhere. Run `node build_deck.js`.

- Logos for the cover: Yuno wordmark `REPO/Yuno Design System/yuno-design-system/assets/yuno-wordmark-white.png`; merchant logo `REPO/yuno-sales-pitch-maker/public/merchants/<slug>.png` (white-on-transparent, 725 merchants). If the merchant PNG is missing, fetch it with the /builddeck logo step (`yuno-sales-pitch-maker/scripts/_logo-one.mjs`) or leave the text title alone. Everywhere else, provider and customer names are text; never fetch or redraw third-party logos.
- Deliver a **.pptx**: German's decks live in Drive/Google Slides and go out as files or PDFs. Name it `Yuno_x_<Merchant>_<Type>_<MonYYYY>.pptx` in the account folder. Presenter guidance goes in speaker notes, never on the slide.
- Themes: brand tokens by default (Yuno Blue, Unity Black, Titillium Web). `YUNO_DECK_THEME=navy` gives Samuel's original navy palette; `YUNO_DECK_FONT=Arial` forces a font that opens identically everywhere.

### 7. QA (not optional)

1. `python3 SKILL_DIR/scripts/deck_qa.py <deck.pptx> --merchant "<Name>" --allow "<their PSPs, named competitors>" [--lang es]`. It must exit 0. It checks leaked account names, placeholders, working notes, units, count consistency, off-slide shapes, source lines, density, and German's house rules (dashes, "no small feat", local currency, fabricated stats, PayPal as PSP, reconciliation without a roadmap footnote). It prints every money figure per slide: reconcile the hero number, lever subtotals and totals across slides by hand.
2. Work through `references/qa-checklist.md`.
3. Visual pass. This Mac has no LibreOffice, so: if `soffice` is on PATH, convert to PDF and look at every page; otherwise upload the .pptx to Drive, open it as Google Slides and run `python3 SKILL_DIR/scripts/slides_thumbs.py <presentationId> <out>/build/thumbs` to pull every slide as PNG, then look at each for overflow, overlap, clipped text and orphan words in titles. If neither is possible, say so explicitly in the hand-off.
4. Fix and re-run until clean. Save the final QA output as `<out>/build/qa.txt`.

### 8. Deliver

Present the file path, then in chat give German (briefly):
- the storyline in one line, and the hero number with its % of their revenue;
- **which 6-8 slides to present live** and which are leave-behind;
- **claims he should confirm** before sending (product status, pricing, anything tagged [A], defaults assumed in step 3);
- what you couldn't find, and whether the visual pass was done.
Then `git add` the account folder, commit, `git push origin main`.

## Principles to hold onto when the blueprint doesn't fit

- **Specific beats impressive.** "A decline on Nuvei doesn't fail over to Elavon" is worth more than any stat about Yuno. Name their processors, plans, prices, markets and people's roles.
- **Their pain, in their words, from their sources.** A risk factor they wrote, a job they posted, a complaint their customer left, a line from a Gong transcript.
- **Under-promise on purpose.** Allegiant was won by committing to ~3% when competitors claimed 5%+ and backing it with decline-code math. A number they can verify beats a bigger one they can't.
- **Never threaten the incumbent relationship.** Yuno is additive, with instant fallback and rollback as a configuration change.
- **Every deck ends in an ask they can say yes to this week**: their data under NDA, a two-week sprint, a contained pilot on 2-3 markets.
- **One merchant per deck.** Start from the helper and the ledger, not from another merchant's file.
- If something important is unknown, write it on the slide as "TO VALIDATE" or flag it for German. Do not fill gaps with invented specifics.

## Files

| File | Read it when |
|---|---|
| `references/deck-types.md` | Always, at steps 1 and 5: slide-by-slide blueprints for types A-E, RBP mapping, optional modules |
| `references/research-playbook.md` | Step 2: German's internal sources and tools, public sources by what they prove, the evidence ledger |
| `references/value-model.md` | Step 4: lever catalog, formulas, conservative defaults, guardrails (incl. pricing and published stats), scenario and ROI math |
| `references/slide-library.md` | Step 5: reusable slide patterns with copy templates and copy rules |
| `references/yuno-facts.md` | Step 5: positioning line, published stats, standard pricing, proof points, team, certifications, support model, product nuances to verify |
| `references/design-system.md` | Step 6: brand tokens, type, slide anatomy, layout rules, helper API, pptxgenjs gotchas |
| `references/qa-checklist.md` | Step 7: the full pre-send checklist |
| `scripts/yuno_deck.js` | Step 6: the pptxgenjs helper (brand and navy themes, lockup cover) |
| `scripts/deck_qa.py` | Step 7: automated QA, exit 1 on any ERROR |
| `scripts/slides_thumbs.py` | Step 7: slide thumbnails from Google Slides for the visual pass |

Origin: Samuel Vieira's `yuno-sales-deck` package (Slack DM, 2026-09-17), adapted to German's stack, paths and house rules.
