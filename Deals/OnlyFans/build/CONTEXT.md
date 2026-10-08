# OnlyFans token vault deck · shared context for all agents (8 Oct 2026)

Owner: German Tatis (Senior AE, Yuno, german.tatis@y.uno). Requested by Samuel Vieira (BDM, samuel@y.uno) on 7 Oct 2026 by Slack DM.

## The deal in five lines
- OnlyFans (Fenix International Ltd, UK; Fenix Internet LLC, US) opened an RFP for a token vault. Yuno is late. Our contact forwards this deck to OnlyFans' Payments Manager; the deck must be good enough to get Yuno added to the RFP. Deadline: today, 8 Oct 2026.
- Readers: payments and engineering people who read it without us in the room and will test every claim.
- What OnlyFans told us about their design: (1) a creator opens one OnlyFans account; (2) behind it, accounts open across two to five banks plus several card-issuing and bank-transfer providers, so no single bank can cut a creator off; (3) funds can be converted to stablecoins to earn yield; (4) issuers are pluggable, add or swap; (5) initial scope is US balances only; (6) they are heading to full banking as a service, so vaulting any sensitive data matters, not only cards.
- What Yuno pitched: Yuno as the orchestration layer underneath, deciding which banks and providers each creator lands on. OnlyFans asked repeatedly who makes that decision; answer given: OnlyFans sets the rules.
- The focus of the deck is the STANDALONE TOKEN VAULT (the RFP), with the decision layer and the comparison vs VGS / Basis Theory as the differentiation. Samuel also asked for: a slide on how we differentiate from VGS / Basis Theory; and that we cover every gap we learned from a prior vault evaluation (see "internal context" below).

## Files already in this folder
- `samuel-handoff-prompt-2026-10-07.md`: Samuel's complete 25-slide content, speaker notes, label system, what can and cannot change, competitor sources. Content was fact-checked against docs.y.uno and competitor pages on 7 Oct 2026. Treat its claims and labels as the baseline. KEEP INTERNAL.
- `template_eventbrite_gslides_text.md`: the text of German's 46-slide Google Slides deck "Deck - Eventbrite (BSP) + Yuno", our layout template. Sections there: Agenda · 01 A global payment infrastructure for BSP's ecosystem · 02 How Eventbrite runs payments today · 03 The proposed model · 04 Why Yuno? · 05 The marketplace case · 06 Appendix.
- `template_dump.json` + `thumbs_template/`: Slides API dump and PNG thumbnails of the template copy.

## The working Google Slides file (final deliverable)
- Copy of the template, owned by German, shared as writer with the service account: presentation id `10A2GokDXPEPkeqqS29H7a460R6j5ux60nILIqUXmUKc` (title "Deck - OnlyFans + Yuno · Token Vault (Oct 2026)").
- Service account: `gtm-claude-editor@gtm-claude-tools-260922.iam.gserviceaccount.com`, key at `~/.config/gsuite/sa.json`, scope `https://www.googleapis.com/auth/presentations`. The OAuth tokens in the repo are dead (client deleted). Prior Slides API builds to learn from: `Industry/AI/Higgsfield/build/engine.py` (text replace preserving styles, element walker), `Deals/Thinkific/build/common.py` + `build_tk.py` (SA auth, box()/bar() primitives, fmt_requests with **bold** markup, thumbnails).
- OnlyFans logo, white on transparent, 1024x179: local `yuno-sales-pitch-maker/public/merchants/onlyfans.png`, public URL `https://deck.yuno.tools/merchants/onlyfans.png` (HTTP 200).

## Other source material in the repo
- `Vaulting/yuno_vault.md`, `Vaulting/basis_theory.md`, `Vaulting/vgs.md` (research dumps, 8 Oct 2026) and `Vaulting/Yuno Vault vs Basis Theory vs VGS.md` (German's internal battlecard, 8 Oct 2026, sourced).
- `Deals/Chess.com/yuno-vs-basis-theory.html` (+ `.pdf`) and `yuno-vs-basis-theory-onepager.html` (Sept 2026 battle card and the English side-by-side one-pager "yuno vs basis theory", internal). These are the "Basis Theory vs Yuno comparison" Samuel remembers; he asked for a row-by-row diff against his slide 18.
- `data/research/onlyfans-2026-05-11.md`: prior OnlyFans research brief (May 2026).
- Ria's questions from a prior standalone-vault evaluation (Google Doc id `1SMT3ZL7l6yEmKJmKqSwKM44y0Wi_HBPzaFlpxGKA9ew`, title "Subject: RE: Yuno standalone vault — your questions"; read with the Drive MCP read_file_content). Four rounds of buyer questions and Justo's draft answers, several bracketed or marked "confirm with product".
- Skill references for house style and Yuno facts: `.claude/skills/yuno-sales-deck/references/yuno-facts.md`, `design-system.md`, `slide-library.md`, `qa-checklist.md`.

## Internal context that must never reach the deck
- The prior vault evaluation was SpaceX (contact Ria, project "Spike"). Yuno sent material that overclaimed and left placeholders; the lesson shaped Samuel's label system. NEVER name SpaceX, Spike, Ria, Chess.com, Sean Walkinshaw or any other customer or prospect in slide text or speaker notes. Use "a prior evaluation" only in internal notes to German, never in the deck.
- Nothing about Riot Games ever goes to a third party.
- Competitor pricing (Basis Theory $995/month for 20,000 tokens then $0.05; VGS from $1,000/month) stays in speaker notes only.

## Label system (Samuel's, keep exactly; status readable from the word, not only the colour)
| Label | Meaning | Pill |
|---|---|---|
| CONFIRMED | Written in Yuno public documentation (docs.y.uno, read 7 Oct 2026); company figures from y.uno | green #1F8A5B on #E2F3EB |
| BETA | Qualifier next to CONFIRMED for anything that depends on the PCI Proxy (beta, enabled per organization) | grey #424449 on #EFF0F2 |
| PUBLIC DOCS | Read on a competitor's own public pages on 7 Oct 2026 | blue #3E4FE0 on #E8EAF5 |
| OPEN | Not confirmed in writing inside Yuno; always shown with an owner, never as a fact | amber #9A5B00 on #FBEFD9 |
| NOT IN DOCS | Appendix only: a gap in Yuno's public reference | grey |
Never upgrade a label. Never drop one. Anything not in public docs and not confirmed in writing is OPEN with an owner.

## German's house rules (non-negotiable)
1. Facts only; omit what cannot be verified. Every number traces to a source with a date. Primary sources first; corroborate material facts.
2. No em-dashes and no " - " as punctuation anywhere (slides, notes, files). Use commas, periods, colons.
3. Never the phrase "no small feat".
4. USD only. No local-currency amounts.
5. Yuno published performance stats only: 7% authorization uplift, 30% recovered revenue (y.uno). Never "+12%" or "20-30%". Named client results only if published by Yuno (inDrive 90% approval and 11 countries in 8 months; Rappi; Livelo 50% recovery and 5% uplift; Wingo 14%).
6. PayPal is a wallet / APM, never a PSP. Processor lists hold PSPs, acquirers, gateways and MoRs only.
7. Client-reported numbers win over derived ones.
8. One merchant per deck. Cover carries the `yuno | OnlyFans` lockup top-left on the dark hero; no "Hello team".
9. Official positioning line if needed: "Yuno is an AI native operating system for global financial infrastructure. We help companies orchestrate their payment stack across a fragmented ecosystem that includes payment methods, processors, antifraud tools, KYC/KYB providers, reconciliations, and stablecoins to lower payment processing costs, increase authorization rates, expand globally, and become more operationally efficient."
10. Tone toward VGS and Basis Theory: respectful and specific; both are Yuno partners. Say where they lead.
11. Action titles: every content slide headline is a full sentence stating the takeaway; small ALL-CAPS kicker above.
12. Deliverables in English. Speaker notes are written for the customer (anyone who opens the deck can read them).

## Target deck structure (German's sections, Eventbrite layout)
Cover · Agenda · 01 Why we are here · 02 Industry context · 03 How OnlyFans runs payments today · 04 How OnlyFans vaults today and what the RFP has to cover · 05 Why Yuno · 06 The Yuno token vault (vault, proxy, decision layer) · 07 Versus a standalone vault (VGS, Basis Theory) · 08 The path forward (phases, open items, next steps) · Appendix (limits, who we are, compliance, sources).

## Output location
Everything goes in `/Users/germantatis/Desktop/GTMCoding/Deals/OnlyFans/build/`. Web search budget is shared across the session (200 total): research agent ≤ 80, Yuno-facts agent ≤ 50, builder ≤ 10.
