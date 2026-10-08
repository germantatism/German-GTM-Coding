# OnlyFans deck · what changed beyond layout (for Samuel) · 8 Oct 2026

Google Slides: https://docs.google.com/presentation/d/1JSaFLC6QEIoNDFq1RbmMglAyuf8bLx7HDk2qzeeEbbA/edit

Built on German's Eventbrite template (the 46-slide Google Slides deck). German asked for a deck that covers the whole story in his section order, so your 25 slides are the spine and the deck grew to 57 slides. Your wording, labels, quotes, the 4 / 1 / 4 tally and the six open items are carried over verbatim. Changes beyond layout:

## Structure
1. Sections renumbered to German's order: 01 Why we are here · 02 Industry context · 03 How OnlyFans runs payments today · 04 What the vault has to hold · 05 Why Yuno · 06 The Yuno token vault (your 01 Vault, 02 Proxy, 03 Decision layer) · 07 Versus a standalone vault (your 04) · 08 The path forward · Appendix. Your four dividers became the 06 and 07 dividers; their speaker notes were merged.
2. An agenda slide was added (German's decks always open with one).
3. Cross-references updated to the new numbers: "slide 21" (open items) → 50; "17, 18 and 19" → 45, 46, 47; "slide 25" (sources) → 57; "slide 23" (limits, in notes) → 54; "Sections 01 to 03" on your slide 2 → "Section 06". Footer page numbers follow the new positions. "Open item 3" references are unchanged.
4. Your slide 8 (seven buyer questions) is now "1 of 2"; a second slide adds eight more questions (rows 8 to 15) built from the standard vault RFP question set: export file contents, subprocessors and direct network connections, behaviour when the vault is unreachable, NTID capture through the proxy, SAQ impact of the proxy, bank accounts and APMs in the vault, bringing existing network tokens in, data location. Each row carries CONFIRMED with the docs.y.uno page or OPEN with an owner. Your seven rows are untouched, so the "five of the seven" count in your notes still holds.

## New slides (none change your claims)
- 01: Executive summary in the Eventbrite format.
- 02: Industry context (creator banking at a glance; why a multi-bank architecture; what a vault is expected to do in 2026; the independent vault market in three shapes).
- 03: OnlyFans in numbers (FY2025 accounts filed 20 Sep 2026), where demand sits, the stack as publicly evidenced (only OnlyFans' own Terms, Help Center and Privacy Policy; no third-party processor claims), the 2021 lesson, payments today in four numbers.
- 04: How OnlyFans vaults today (known, inferred, unknown), the six data classes the design implies, four external clocks (PCI 4.0.1, GENIUS Act, network tokenization 2030, agent credentials).
- 05 Why Yuno: German's standard Yuno story, four pillars, offices, trusted-by (SpaceX logo removed), team, dedicated team, plus a security and compliance table rebuilt from y.uno pages only.
- 06: two added vault slides, both CONFIRMED on docs.y.uno: "Keep current" (network tokens and account updater, with the stored-credentials NTID behaviour) and "Move" (card import, network token import, export, with the export-file gap marked OPEN).
- 06, closing the section: three "Product direction" slides from the banking orchestration draft (one creator account with every bank behind it; you set the rules and no single bank can cut a creator off; yield on idle balances through Jiko, Coinbase and Triple-A, and pluggable issuers). Each carries a DIRECTION pill and the line "Product direction, not a delivery commitment", and points to open items 2, 3 and 6, so nothing in them is presented as a delivered capability.
- 07: "One project instead of two", a three-option grid (standalone vault alone, standalone vault plus an orchestrator, Yuno) in the Eventbrite comparison style. Two Yuno cells are marked partly covered on purpose (bank allocation by rule, US banking and issuing providers) and point to open items 2 and 3.
- Appendix: credentials slide uses only the four stories published on y.uno (inDrive, Rappi, Livelo, McDonald's tokenized payments); Wingo is not on the success-stories page today, so it is out.

## Edits inside your slides (please confirm)
1. Open item 4 now reads "Token requestor model for each card network, scheme activation per network, and export of network transaction IDs, bank and entity data", owner "Trust & Vault product, Legal". Reason: the documented export file has no NTIDs while the y.uno vault page promises "transaction references"; and internal engineering says Amex network tokens are still in certification although the docs list Amex.
2. Open item 5 now reads "Contractual uptime, failover design, rate limits and the subprocessor list", owner "Engineering, Security". The count stays at six.
3. Speaker notes additions (slide text unchanged): slide 8 row 3 (the Invoke Forward Proxy reference says the security code cannot be injected; Phase 0 shows actual behaviour) and row 7 (y.uno/sla publishes 99.90% monthly availability and a 5-minute P1 response; the contract figure binds); slide 6 (scheme activation confirmed per network in writing; network token import is documented); slide 18 (Basis Theory routing guide "currently under construction" on 8 Oct 2026; Pagos listed as subprocessor for network tokens); slide 19 (VGS scopes Discover to US merchant IDs and Amex to direct merchants); slide 3 (the proxy sandbox is open; cryptogram API and account updater are switched on per organization).
4. Sources slide: Basis Theory announcement cited via the Merchant Risk Council republication (the PR Newswire URL returned 404 on 8 Oct); added y.uno/sla, trust page, status.y.uno, stored credentials, network token migration, 3DS Standalone and web SDK pages.

## Decisions only you can take
- Slide 8 row 7 stays OPEN as you wrote it. Under your own rule (company figures from y.uno count as CONFIRMED) the availability figure could be split out as CONFIRMED with failover design and rate limits OPEN. Your call.
- Amex network tokens: the docs say Visa, Mastercard and American Express; engineering says Amex is in certification (late 2026 or January 2027). The slide keeps your CONFIRMED; the notes and open item 4 cover activation. If OnlyFans tests Amex provisioning in Phase 0 it may fail.

## Your Basis Theory vs Yuno comparison, diffed against slide 18
German's three comparisons (8 Oct battlecard, 2 Sep battle card, Sept one-pager) were diffed row by row against your slides 17, 18 and 19 in `vs_standalone_vault.md`, section 1 (25 rows). None of your cells needed changing. The material differences: the one-pager's "TRID registered in your name" and "multi-cloud, regions" claims have no public source and were retired; the SLA figure is public at y.uno/sla (your row stays OPEN per the decision above); network token import is documented and went into notes; the "24 providers" migration figure is internal and was left out.
