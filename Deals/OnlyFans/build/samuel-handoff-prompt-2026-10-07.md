\# Handoff: finish the OnlyFans deck in Germán's template  
  
This brief comes from Samuel Vieira (Business Development Manager, Yuno). It is written for the Claude Code session that Germán Tatis runs, which has Germán's deck template. It contains everything needed to finish the job without access to the conversation that produced the deck.  
  
\#\# What I need from you  
  
Take the 25-slide deck described below and rebuild it in Germán's template so it looks like one of his decks (the reference is his "Deck - Eventbrite (BSP) + Yuno", Google Slides id \`1qe5p-D3Cgx63UuHj8nf3JaY\_4wxOqytJKgo9IDzGI\_E\`). The content is finished and fact-checked. The job is layout and visual polish: map each slide onto the right template layout, fix density and hierarchy where the template calls for it, and deliver a deck Samuel can send. Samuel wants the result as a Google Slides link.  
  
The deck has to be ready to send on 8 October 2026.  
  
\#\# Why this deck exists  
  
OnlyFans opened an RFP for a token vault. Yuno is late to it. Our contact there will forward this deck to OnlyFans' Payments Manager, and the deck has to be good enough that he adds Yuno to the RFP. The readers are payments and engineering people who will read it without us in the room and will test what it says.  
  
What OnlyFans told us about their design:  
  
1\. A creator opens one account in OnlyFans.  
2\. Behind it, accounts are opened across two to five banks, plus several card issuing and bank transfer providers, so no single bank can cut a creator off.  
3\. Funds can be converted to stablecoins to earn yield.  
4\. Issuers are pluggable: they can add or swap card issuing providers.  
5\. The initial scope is US balances only.  
6\. They are heading to full banking as a service, so vaulting any sensitive data matters, not only cards.  
  
What Yuno pitched: Yuno as the orchestration layer underneath, deciding which banks and providers each creator lands on. OnlyFans asked several times who makes that decision. The answer given was that OnlyFans sets the rules. Slides 12 to 14 answer that question precisely.  
  
\#\# The rule that shaped the content, and that you need to protect  
  
In an earlier vault evaluation with another customer, Yuno sent material that claimed capabilities that were not built and left placeholders in the text. That is internal context: never mention it, or that customer, in the deck. The lesson is the reason this deck works the way it does:  
  
\- Every capability claim carries a label that says what it is based on.  
\- Where a standalone vault is ahead of Yuno, the deck says so.  
\- Anything not confirmed in writing is listed as an open item with an owner, never stated as a fact.  
\- There are no placeholders.  
  
A vault buyer who finds one overclaim stops trusting the rest. So the honesty of the deck is the pitch. Please do not make it more "salesy" while polishing it.  
  
\#\#\# The labels  
  
| Label | Meaning | Where it appears |  
|---|---|---|  
| CONFIRMED | Written in Yuno's public documentation (docs.y.uno, read 7 October 2026). Company figures come from y.uno. | Green pill |  
| BETA | Qualifier next to CONFIRMED for anything that depends on the PCI Proxy, which is in beta and enabled per organization. | Grey pill |  
| PUBLIC DOCS | Read on a competitor's own public pages on 7 October 2026. | Blue pill |  
| OPEN | Not confirmed in writing inside Yuno. Always shown with an owner. | Amber pill |  
| NOT IN DOCS | Appendix only: a gap in Yuno's public reference. | Grey pill |  
  
Keep every label attached to the claim it is attached to now. Never upgrade one (for example OPEN to CONFIRMED) and never drop one because a layout has no slot for it. If the template has its own pill or tag style, use it, but keep these five meanings and keep them visually distinct. Status must be readable from the word, not only from the colour.  
  
\#\# What you can change, and what you cannot  
  
You can change freely: layout, grid, spacing, type sizes, colours within the template's palette, card and table styling, icons and artwork from the template, the order of elements inside a slide, how a table is drawn, and whether a dense slide is split in two.  
  
Please leave these as they are, and tell Samuel if you think one of them needs to change instead of changing it:  
  
\- \*\*Claims and their wording.\*\* Every sentence about what Yuno, VGS or Basis Theory does was checked against a source. Shortening connective text is fine; changing what a claim says is not.  
\- \*\*Quotes.\*\* Text inside quotation marks is verbatim from the vendor's page. Do not edit, trim mid-sentence or re-capitalise it.  
\- \*\*Who leads.\*\* The "Who leads" column on slides 17, 18 and 19, and the tally on slide 4.  
\- \*\*Numbers.\*\* 460+, 190+, 4 certifications, 20 tokens, 1 MB, 30 s / 120 s, TLS 1.2, 3 hours, 11 July 2026, 14 October 2025, 7 October 2026.  
\- \*\*Speaker notes.\*\* They are written for the customer to read, because anyone who opens the deck can see them. Carry them over as they are. Competitor pricing appears only in the notes of slides 18 and 19, on purpose; keep it off the slides.  
\- \*\*Tone toward VGS and Basis Theory.\*\* Both are Yuno partners. The deck is respectful and specific about where they lead. Do not sharpen it.  
  
\#\#\# Things that must stay in sync  
  
If you add, remove, split or reorder slides, these break silently. Check each one at the end.  
  
\- \*\*Tally on slide 4: 4 of 9 Yuno leads, 1 of 9 level, 4 of 9 VGS and Basis Theory lead.\*\* It is the count of the "Who leads" column on slide 17 (row 1 level, rows 2 to 5 vaults lead, rows 6 to 9 Yuno leads). Slides 18 and 19 each also come to 4 / 1 / 4.  
\- \*\*Six open items\*\* on slide 21. Slide 3 and slide 22 say "six". Every OPEN label or "open" cell elsewhere maps to one of the six.  
\- \*\*Cross-references by slide number:\*\* slide 3 points to slide 21; slide 4 points to 17, 18 and 19; slide 6 points to 25; slide 14 and slide 20 point to "open item 3"; slide 16 points to 21; the notes of slide 10 point to 23. Update the numbers if the order changes.  
\- \*\*Footer page numbers\*\* equal the slide's position.  
\- \*\*Section numbering:\*\* 01 Vault, 02 Proxy, 03 Decision layer, 04 Versus a standalone vault. Slide 2 refers to "Sections 01 to 03" and "Section 03".  
\- \*\*Slide 8 notes:\*\* "Five of the seven are documented today; three of those depend on the proxy." That matches rows 1, 2, 3, 4 and 6, with BETA on 2, 3 and 4.  
  
\#\# Design: where it stands and what is left for you  
  
The deck was built as a 1920×1080 HTML deck (one HTML file per slide, inline styles). It was restyled toward Germán's Eventbrite deck, but with one hard limit: only the \*\*cover\*\* of that deck could be seen. The file is 44 MB and could not be exported, so its inner slides were never visible. Everything inside is an approximation built from the cover and from other Yuno decks set in Geist. That gap is the main thing to close.  
  
What is in place now:  
  
\- \*\*Typeface:\*\* Geist for everything (300 to 700), Geist Mono for code and field names. Matched letter by letter against the Eventbrite cover title.  
\- \*\*Cover, four section dividers, closing slide:\*\* black, with the blue orb artwork taken from the Eventbrite cover. The dividers and the closing slide use the same artwork shifted right so text sits on black.  
\- \*\*Cover lockup:\*\* white Yuno wordmark, a grey "+", then "OnlyFans" typed in Geist SemiBold. The official OnlyFans logo was not available. If the template or Germán has it, use it.  
\- \*\*Content slides:\*\* white, with a blue uppercase kicker, a bold near-black headline that states the takeaway as a sentence, body in grey, big numbers in bold blue, the blue Yuno wordmark top right, and a footer row (\`For: OnlyFans NN\` · \`WWW.Y.UNO\` · \`Confidential · y.uno\`).  
\- \*\*Palette in use:\*\* blue \`\#3E4FE0\`, lavender \`\#8F99F0\` / \`\#B7BEF2\` / \`\#D5D9F5\`, tints \`\#E8EAF5\` and \`\#F4F5FD\`, ink \`\#121212\` / \`\#282A30\` / \`\#424449\`, greys \`\#757882\` / \`\#92959B\` / \`\#CDCFD3\` / \`\#E2E3E6\`, cover grey \`\#A3AAC3\`. Pills: green \`\#1F8A5B\` on \`\#E2F3EB\`, amber \`\#9A5B00\` on \`\#FBEFD9\`, blue on \`\#E8EAF5\`, grey \`\#424449\` on \`\#EFF0F2\`.  
  
What I would like you to do with the template:  
  
1\. Replace each approximated layout with the real template layout that fits it. Where the template's own colours, type scale or footer differ from the list above, the template wins.  
2\. The Eventbrite deck has patterns that fit this content well. Its "proposed model" slide compares options in a grid with a three-state legend (gap stays open, partly closed, closed); slides 17, 18 and 19 are the same kind of content, as long as the "Who leads" column and the cell text survive. Its stat slides (label, big number, caption) fit slides 4 and 24. Its chapter dividers (title plus number) fit slides 5, 9, 12 and 15.  
3\. Slides 17, 18 and 19 are the densest: nine-row tables at 24 px on a 1920 px canvas. If the template needs larger type, split a table across two slides before cutting cell text, and then update the cross-references.  
4\. The Eventbrite deck opens with an agenda slide. This deck has none; the four dividers carry the structure. Add one only if Germán's decks always have it, and renumber if you do.  
5\. Slide 2 (the architecture diagram), slide 10 (request before and after the proxy) and slide 13 (entity → onboarding → Yuno → three accounts → transfers) are diagrams. Redraw them in the template's diagram style if it has one. Keep the code on slide 10 exactly as written: the header name, the path and the \`{{vaulted\_token.\<TOKEN\>.field}}\` syntax are documented, and the caption says the rest is illustrative.  
  
Germán once sent a Basis Theory versus Yuno comparison document. Samuel remembers it, but it could not be found in Slack, Drive or email. If Germán has it, compare it with slide 18. Where it disagrees with slide 18, list the differences for Samuel instead of overwriting cells: slide 18 was verified against Basis Theory's pages on 7 October 2026.  
  
\#\# Open points that only Samuel or Yuno product can settle  
  
Do not resolve these by guessing. The deck already handles each one honestly; they are listed so you do not "fix" them.  
  
1\. \*\*Token requestor ID.\*\* The vault page on y.uno says requestor IDs are registered in the merchant's name; Yuno's API reference says Yuno holds the Token Requestor ID. The deck states what the API reference says and marks the rest OPEN.  
2\. \*\*CVV through the proxy.\*\* The proxy overview and forward-proxy guide say the security code can be referenced for 3 hours after enrollment by default; the "Invoke forward proxy" API reference says the security code "cannot be injected". The deck follows the guide and says "per the proxy guide".  
3\. \*\*Tables for personal and KYC data.\*\* Shown on y.uno's vault product page, but there is no public API reference. Marked OPEN.  
4\. \*\*Rule-based allocation of creators across banks and issuers.\*\* This is what was pitched. It is not in the public API reference. Today the bank is chosen per call (\`yuno\_connection\_id\` on each onboarding request). Marked OPEN.  
5\. \*\*Which US banking and issuing providers are connected, and whether one entity can hold onboardings on several connections.\*\* Not stated in the docs. Marked OPEN. This is the core of OnlyFans' design, so do not soften the open label.  
6\. \*\*Uptime, failover design, rate limits, stablecoin conversion providers.\*\* OPEN, no figures anywhere in the deck.  
7\. \*\*Commitments made in Samuel's name:\*\* written answers to the six open items with the RFP response, and the Phase 0 exit on slide 20 ("Every Confirmed capability your Phase 1 relies on is shown working to your engineers, or we change the label"). Keep the wording.  
  
\#\# Sources behind the competitor lines  
  
These are the pages the fact-check used, in case anything needs re-checking. All were read on 7 October 2026.  
  
VGS  
\- \`verygoodsecurity.com/payment-orchestration\`: "VGS does not make routing decisions for you." and "VGS powers orchestration, but does not act as the orchestrator."  
\- \`docs.verygoodsecurity.com/integrating-a-second-payment-provider\`: "Your application keeps ownership of provider selection, routing, and failover logic."  
\- \`verygoodsecurity.com/network-tokens\`: "VGS is the ONLY non-PSP, neutral vault connected to all 4 major networks for network tokens."  
\- \`verygoodsecurity.com/vault\`: PII, bank account numbers and IBANs stored as aliases; PCI DSS Level 1.  
\- \`docs.verygoodsecurity.com/vault/guides/card-issuing\`: names Marqeta, I2C and Galileo as examples; card display through VGS Show.  
\- \`verygoodsecurity.com/use-cases/card-issuers\`: money movement partners "including TabaPay and Astra".  
\- \`verygoodsecurity.com/pricing\`: "Plans start at $1,000/month" (speaker notes only).  
\- VGS docs on inbound and outbound routes and on VGS Compute (Larky) for custom code.  
  
Basis Theory  
\- Press release, PR Newswire, 14 October 2025: its vault "operates independently of any payment processor or orchestration layer."  
\- \`developers.basistheory.com/docs/api/tokens/token-types\`: card, bank, us\_bank\_account\_number, us\_bank\_routing\_number, social\_security\_number, employer\_id\_number, token, network\_token.  
\- \`developers.basistheory.com/docs/features/network-tokens\`: creates the Token Requestor ID with each network on the merchant's behalf; existing network tokens are not imported, they are re-provisioned.  
\- \`developers.basistheory.com/docs/card-issuing/\`: issue-cards, display-cards and set-card-pin guides; the PIN guide covers Lithic and Marqeta.  
\- Proxy transforms and Reactors concept pages.  
\- \`basistheory.com/use-cases/creator-economy\`: markets routing and retries across processors; quotes a creator platform whose processor shut it off without warning. No rules product, pre-built connectors, accounts or transfers API, or payouts product was found.  
\- \`basistheory.com/resources/pricing-details\`: $995 a month for 20,000 stored tokens, then $0.05 per additional token (speaker notes only).  
  
Yuno (docs.y.uno)  
\- PCI Proxy: overview, forward proxy, destination allowlist, destination authentication, and the \`POST /v1/pci-proxy/forward\` reference.  
\- Network tokens; Generate network token cryptogram (cryptogram-only mode); Card account updater.  
\- Token migration process; Exporting tokens from Yuno.  
\- Banking Connectivity reference: entities, onboarding, accounts, transfers.  
\- Routing; Monitors; Audit logs; Roles; Security; API environments; Payouts; Split payments marketplace; API changelog July to September 2026.  
\- y.uno vault product page for 460+ processor integrations, 190+ countries and the certifications.  
  
\#\# Files in this package  
  
\- \`PROMPT.md\`: this brief, with the full slide content below.  
\- \`onlyfans-deck-current.pdf\`: all 25 slides as they render today. Use it to see the intended hierarchy on each slide.  
\- \`html/project/deck.json\` and \`html/project/slides/\*.html\`: the source of each slide (one \`\<section\>\` per file, 1920×1080, inline styles, speaker notes in the final \`\<aside\>\`). Image \`src\` values of the form \`/\_blob/\<id\>\` point at the two artwork files in \`art/\`.  
\- \`art/orbs-cover.jpg\`, \`art/orbs-section.jpg\`: the orb artwork as used on the black slides.  
  
If you only received this file, the slide content below is complete on its own: it has every word on every slide and every speaker note.  
  
\#\# What to send back to Samuel  
  
1\. The finished deck in Germán's template, as a Google Slides link.  
2\. A short list of anything you changed beyond layout: split or added slides, shortened text, renumbered references.  
3\. Anything you could not place, and any claim you think is wrong, flagged instead of edited.  
  
Before you hand it back, check that there are still 25 slides' worth of content (or more if you split), that every label is still on its claim, that the 4 / 1 / 4 tally and the six open items still add up, that every slide-number reference points at the right slide, that no text overflows or is clipped, and that nothing from this brief (the internal context, the open points, the pricing) leaked onto a slide.  
  
\---  
  
\# Slide content (source of truth for the text)  
  
How to read this section: each slide lists its kicker, headline and body in reading order. \`\[CONFIRMED\]\`, \`\[BETA\]\`, \`\[PUBLIC DOCS\]\`, \`\[OPEN\]\` and \`\[NOT IN DOCS\]\` are the evidence pills. \`BOX:\` is a card or diagram box, with its parts separated by \`·\`. Small outlined tags appear either as a bold label followed by its line of text (\*\*Who decides:\*\* …) or as \`Chip "…"\`. Tables are given as tables. On the cover, "+" and "OnlyFans" sit beside the Yuno wordmark, and " / " in the title marks the line break.  
  
\#\#\# Slide 01 · \`cover\` · black slide with orb artwork  
  
\- +  
\- OnlyFans  
\*\*Title:\*\* The vault under / creator banking  
\- Your credentials, your connections, your rules.  
\- Samuel Vieira · Business Development · October 2026 · Strictly confidential  
  
\*\*Speaker notes:\*\* You have an RFP open for a token vault, and you told us where the product is going: one creator account on top, several banks, issuers and transfer providers underneath. This deck answers the vault question and the question you asked us most, which is who decides where each creator lands. Every claim in it is labeled with its basis, so your payments team can check it without us in the room.  
  
\#\#\# Slide 02 · \`understood\` · white content slide  
  
\- Overview · what we understood  
\*\*Headline:\*\* One creator account on top. Several banks, issuers and transfer providers underneath, so no single partner can cut a creator off.  
\- Your design as we understood it. Indigo marks where Yuno would sit. Sections 01 to 03 show what exists today and what is open.  
\- BOX: Creator · opens one OnlyFans account  
\- BOX: Yuno · decision layer · Which bank, issuer and rail each creator lands on · Chip "Rules set by OnlyFans"  
\- BOX: Yuno · vault · Cards, account numbers and credentials, tokenized once · Sections 01 and 02  
\- BOX: Banks · Two to five per creator  
\- BOX: Card issuers · Pluggable: add or swap  
\- BOX: Bank transfer providers · Several, for redundancy  
\- BOX: Stablecoin conversion · So balances can earn yield  
\- What you asked  
\- \*\*Who decides:\*\* You do. Your policy picks the provider and Yuno executes it. Section 03.  
\- \*\*US first:\*\* Phase 1 covers US balances only, as you scoped it.  
\- \*\*Banking next:\*\* Every sensitive record needs a home in the vault, not only cards.  
  
\*\*Speaker notes:\*\* This is your design as we understood it from our conversation. Correct anything we have wrong before we go further. The two indigo bands are where Yuno would sit: the vault at the base, and the layer that decides which bank, issuer and rail each creator lands on. You asked several times who makes that decision. The short answer is that OnlyFans does, and Section 03 shows exactly how.  
  
\#\#\# Slide 03 · \`howtoread\` · white content slide  
  
\- How to read this deck  
\*\*Headline:\*\* Every capability claim carries one of three labels, so your team can check it without us in the room.  
\- BOX: \[CONFIRMED\] · \*\*Written in Yuno's public documentation\*\* · Read at docs.y.uno on 7 October 2026; company figures come from y.uno. Most of it can be tested in the sandbox. A Beta tag marks anything in beta.  
\- BOX: \[PUBLIC DOCS\] · \*\*Read on another vendor's public pages\*\* · VGS and Basis Theory, read on 7 October 2026. Treat every one of these lines as a question to confirm with them.  
\- BOX: \[OPEN\] · \*\*Not yet confirmed in writing inside Yuno\*\* · Shown with an owner, never as a fact. The six open items are listed together on slide 21. In the appendix, Not in docs marks a gap in our public reference.  
\- Why it matters  
\- A vault sits under everything you build on it. We would rather show you an open item today than have your engineers find it in the sandbox.  
  
\*\*Speaker notes:\*\* We label every claim. Confirmed means it is in our public documentation, and most of it can be tried in the sandbox. Public docs means we read it on a competitor's own pages and you should confirm it with them. Open means we have not confirmed it in writing internally, so we will not present it as a fact. A vault is the wrong place for surprises.  
  
\#\#\# Slide 04 · \`answer\` · white content slide  
  
\- The answer up front  
\*\*Headline:\*\* A vault stores the credential. Your design also needs a layer that decides where it goes. Yuno does both; here is how far each goes today.  
\- Nine things your design needs: item by item on slide 17, vendor by vendor on slides 18 and 19. Competitor lines from public pages, read 7 October 2026.  
\- Where Yuno leads  
\- 4 of 9  
\- Routing rules for card payments, processor integrations already built, a banking API across providers, and payouts.  
\- Level  
\- 1 of 9  
\- A card vault at PCI DSS Level 1 with hosted capture. All three of us have one.  
\- Where VGS and Basis Theory lead  
\- 4 of 9  
\- Network token depth, token types for personal data, issued-card display (PIN setting at Basis Theory), and a more established proxy with custom code.  
\- In one line  
\- If the RFP is for storage alone, a standalone vault is a fair choice. If the vault has to serve a multi-bank, multi-issuer product, the harder half is the layer above it.  
  
\*\*Speaker notes:\*\* Here is the conclusion before the detail. We compared Yuno with VGS and Basis Theory on nine things your design needs. On four of them a standalone vault leads today, and we say so. On one we are level. On four Yuno leads, and those four are the ones your architecture adds on top of a vault: routing rules for card payments, processor integrations that are already built, a banking API across providers, and payouts. Where any of these is only partly there today, the deck says so.  
  
\#\#\# Slide 05 · \`s1-vault\` · black slide with orb artwork  
  
\- 01  
\*\*Headline:\*\* Vault  
\- Cards today. Next, every credential that creator banking adds.  
\- 01 Vault  
\- 02 Proxy  
\- 03 Decision layer  
\- 04 Versus a standalone vault  
  
\*\*Speaker notes:\*\* Section one is the RFP itself: the vault. Three slides. What it does for cards, what it holds beyond cards, and the questions a careful vault buyer asks first.  
  
\#\#\# Slide 06 · \`vault-cards\` · white content slide  
  
\- 01 · Vault · cards  
\*\*Headline:\*\* One vaulted token works on every processor you connect, so no processor owns your cards.  
\- Source: docs.y.uno, read 7 October 2026. Page list on slide 25.  
\- BOX: \[CONFIRMED\] · Store · \*\*Collect a card without charging it\*\* · SDK enrollment on Web, iOS and Android creates a vaulted token without a charge. Card numbers never reach your pages, which is why most SDK merchants qualify for SAQ A. Zero-amount verification is optional where the provider supports it.  
\- BOX: \[CONFIRMED\] · Keep current · \*\*Network tokens and account updater\*\* · Once activated, network tokens are provisioned for enrolled cards with Visa, Mastercard and American Express. The account updater refreshes reissued Visa and Mastercard cards while the vaulted token stays the same.  
\- BOX: \[CONFIRMED\] · Move · \*\*Import in, export out\*\* · Cards arrive from your current gateway or vault as PGP-encrypted files over SFTP. Card export is documented too: on written request, to a recipient with a valid PCI DSS attestation.  
\- What you get  
\- \*\*No re-tokenization:\*\* Add or swap a processor and the stored cards keep working.  
\- \*\*Fewer declines:\*\* Reissued and renewed cards update without the cardholder.  
\- \*\*A public exit:\*\* You can read the export process before you sign anything.  
  
\*\*Speaker notes:\*\* The same logic you apply to banks applies to card processors: no single one should be able to cut you off. A card is collected once in our hosted fields and stored as a vaulted token that works on every processor connected to your account. Network tokens and the account updater keep it current. And the way out is documented publicly: an encrypted export to a recipient with a valid PCI DSS attestation. Your QSA confirms your own SAQ level; we describe how capture works.  
  
\#\#\# Slide 07 · \`vault-data\` · white content slide  
  
\- 01 · Vault · beyond cards  
\*\*Headline:\*\* Creator banking adds account numbers, tax IDs and identity documents. Here is where each one lives in Yuno today.  
\- BOX: cards · PCI · number · •••• 3456 · expiration · ••/27 · holder\_name · string · network\_token · DPAN · network\_transaction\_id · The CVV is never stored. · \[CONFIRMED\]  
\- BOX: bank accounts · ACH · type · ACH\_ENROLLMENT · routing\_number · string · beneficiary\_name · string · account\_type · enum · vault\_only · true · In the enroll API reference. Access rules to confirm. · \[CONFIRMED\]  
\- BOX: entities · KYC · KYB · national\_entity · INDIVIDUAL · tax\_id · •••• 6789 · document\_number · •••• 4421 · documentation · KYC files · onboarding · SUCCEEDED · Taken by the banking API. Responses return the last four. · \[CONFIRMED\]  
\- BOX: your own tables · PII · customer\_records · table · identity\_documents · table · protection · per column · retention · per record · access · per role · On our product page. API reference not yet public. · \[OPEN\]  
\- Why it matters  
\- \*\*Today:\*\* Cards are vaulted. Bank details can be stored through the enroll API. Entity data goes through the banking API and comes back masked.  
\- \*\*Next:\*\* Tables you define for any other record. We show you where they stand in a working session, not on a slide.  
  
\*\*Speaker notes:\*\* You told us the product is heading to full banking as a service, so the vault has to hold more than cards. Here is where each kind of data lives today. Cards are vaulted. Bank account details can be stored through the enroll API with no provider involved; we still owe you the exact access rules for that. Entity data for onboarding goes through the banking API, and the tax ID and document number come back masked to the last four; how that data is stored is part of open item one. The fourth class is tables you define yourself for any other personal record. That is on our product page and our roadmap, but the API reference is not public yet, so we mark it open and will walk you through its real state with the Trust & Vault product team.  
  
\#\#\# Slide 08 · \`vault-checklist\` · white content slide  
  
\- 01 · Vault · what an evaluation turns on  
\*\*Headline:\*\* The questions a careful vault buyer asks first, answered before you ask.  
  
| \# | The question | Our answer | Basis |  
|---|---|---|---|  
| 1 | Can we store a card without charging it? | Yes. SDK enrollment creates a vaulted token without a charge. Zero-amount verification is optional where the provider supports it. | \[CONFIRMED\] |  
| 2 | Can we send a stored card to an endpoint we choose? | Yes. The forward proxy sends it to any HTTPS host on your allowlist, including providers Yuno does not connect to. | \[CONFIRMED\] \[BETA\] |  
| 3 | What happens to the CVV? | It is never stored. Per the proxy guide it is held briefly after entry, 3 hours by default, for a first charge. | \[CONFIRMED\] \[BETA\] |  
| 4 | Can we charge with network tokens on our own processor and stay out of PCI scope? | Yes. Cryptogram-only mode (Visa, Mastercard; enabled per organization) needs no PCI certification: it returns no card data and the proxy fills in the token. Recurring charges add the network transaction ID. | \[CONFIRMED\] \[BETA\] |  
| 5 | Whose name are network tokens registered in? | Our API reference says Yuno holds the token requestor ID. Whether requestor IDs can be registered in your name is open, per network. Written answer with the RFP response. | \[OPEN\] |  
| 6 | How do we leave? | A documented card export: a written request, the recipient's PCI DSS attestation, and a PGP-encrypted file over SFTP. | \[CONFIRMED\] |  
| 7 | What uptime do you commit to, and how does it fail over? | You get a contractual figure and the failover design with the RFP response, not a number on a slide. | \[OPEN\] |  
  
  
\*\*Speaker notes:\*\* These are the questions that decide a vault evaluation, and the ones that get tested in a sandbox. Five of the seven are documented today; three of those depend on the proxy, which is in beta and switched on per organization. Two are open and we say so: the token requestor model per network, and the contractual uptime and failover design. On both you get a written answer with the RFP response.  
  
\#\#\# Slide 09 · \`s2-proxy\` · black slide with orb artwork  
  
\- 02  
\*\*Headline:\*\* Proxy  
\- Your connections. Detokenized on the fly.  
\- 01 Vault  
\- 02 Proxy  
\- 03 Decision layer  
\- 04 Versus a standalone vault  
  
\*\*Speaker notes:\*\* Section two is the proxy: how a stored card reaches a provider you chose, including providers Yuno does not connect to. This is in beta and we say so on each slide.  
  
\#\#\# Slide 10 · \`proxy-how\` · white content slide  
  
\- 02 · Proxy · how it works  
\*\*Headline:\*\* You write the request your provider expects and mark the tokens. The proxy swaps in the real values and forwards it.  
\- \[CONFIRMED\]  
\- \[BETA\]  
\- Source: docs.y.uno, PCI Proxy. In the API changelog since 11 July 2026. Read 7 October 2026.  
\- BOX: As OnlyFans sends it · POST /v1/pci-proxy/forward · yuno-proxy-destination-url: · https://api.provider.example/v1/payouts · { · "amount": 2500, · "number": "{{vaulted\_token.9f2a….number}}", · "name": "{{vaulted\_token.9f2a….holder\_name}}" · }  
\- BOX: Yuno proxy  
\- Tokens resolved inside PCI DSS Level 1  
\- BOX: As the destination receives it · POST https://api.provider.example/v1/payouts · { · "amount": 2500, · "number": "4821 •••• •••• 0193", · "name": "ANA SOUZA" · } · Destination and body are illustrative; header and expression syntax are as documented. The full card number is masked here for the slide.  
\- What you get  
\- \*\*Your format:\*\* Your request body, your provider. No waiting for Yuno to build a connector.  
\- \*\*Any destination:\*\* A processor Yuno does not orchestrate, a fraud or issuer service, or your own acquiring connection.  
\- \*\*In beta:\*\* Enabled per organization in production. The sandbox is open for testing today.  
  
\*\*Speaker notes:\*\* The proxy sends stored card data to any provider API you choose. Your backend builds the exact request a provider expects and puts token expressions where the card data goes. Yuno resolves them inside its PCI environment and forwards the call. The destination does not have to be a provider Yuno integrates. For issuers specifically, note the limits on slide 23: capturing or displaying a card your issuer creates is not something the proxy does today. To be clear on status: this has been in our API changelog since July, it is in beta, and production access is switched on per organization. Your team can test it in the sandbox now.  
  
\#\#\# Slide 11 · \`proxy-controls\` · white content slide  
  
\- 02 · Proxy · controls  
\*\*Headline:\*\* The controls you would otherwise build around card data come with the proxy.  
\- Source: docs.y.uno, PCI Proxy overview, destination allowlist and destination authentication. Read 7 October 2026.  
\- BOX: \[CONFIRMED\] · \[BETA\] · Allowlist · \*\*Only hosts you register\*\* · Exact hostname, HTTPS on port 443, no IP addresses or wildcards. You register a host by API and it is usable within minutes. Scope it to one account or the whole organization. Every change lands in an append-only audit log.  
\- BOX: \[CONFIRMED\] · \[BETA\] · Authentication · \*\*Mutual TLS per destination\*\* · Yuno presents your client certificate in the handshake. The private key is write-only and encrypted with a dedicated KMS key. One request-signing scheme is built in today, for dLocal.  
\- BOX: \[CONFIRMED\] · \[BETA\] · Hygiene · \*\*Nothing kept, every call recorded\*\* · Request and response bodies are not stored or logged. Every call produces an audit record. A card number echoed back by a destination is redacted to its last four digits.  
\- Limits to plan for  
\- 20  
\- tokens per request  
\- 1 MB  
\- request and response body  
\- 30 s  
\- timeout, up to 120 s by header  
\- TLS 1.2  
\- or higher, on every destination  
  
\*\*Speaker notes:\*\* A proxy that can send card data anywhere is only safe with controls around it. Destinations are an allowlist you manage by API. Mutual TLS is configured per destination. Bodies are never stored, every call leaves an audit record, and card numbers that come back in a response are redacted. The limits at the bottom are the documented ones, so your engineers can plan around them now.  
  
\#\#\# Slide 12 · \`s3-decision\` · black slide with orb artwork  
  
\- 03  
\*\*Headline:\*\* Decision layer  
\- Who decides where a creator lands. You do.  
\- 01 Vault  
\- 02 Proxy  
\- 03 Decision layer  
\- 04 Versus a standalone vault  
  
\*\*Speaker notes:\*\* Section three is the question you asked most: who decides which bank and which provider each creator lands on. Two slides: the banking objects that exist in our API today, then exactly where the decision sits.  
  
\#\#\# Slide 13 · \`banking\` · white content slide  
  
\- 03 · Decision layer · the banking API  
\*\*Headline:\*\* Entity, onboarding, account and transfer are separate objects, and every onboarding names the provider connection it runs on.  
\- \[CONFIRMED\]  
\- Source: docs.y.uno, Banking Connectivity reference, read 7 October 2026. One entity on several connections: open.  
\- BOX: Creator · One entity: individual or business  
\- BOX: Onboarding · KYC or KYB, on a named provider connection  
\- BOX: Yuno · Banking Connectivity API  
\- BOX: Account · connection A · account and routing number  
\- BOX: Account · connection B · account and routing number  
\- BOX: Account · connection C · account and routing number  
\- BOX: Transfers · ACH: standard, same day · Wire and RTP · Book transfers  
\- BOX: "yuno\_connection\_id": "your Bank A connection" · A required field on every onboarding request. Your system sets it.  
\- What you get  
\- \*\*One API:\*\* Entities, onboarding, accounts and transfers across banking providers in the US, UK, Australia and EU.  
\- \*\*US rails:\*\* ACH standard, ACH same day, wire and RTP, with status by webhook.  
\- \*\*Open:\*\* Which US providers are connected today, and one entity on several connections: named in writing.  
  
\*\*Speaker notes:\*\* This is the part of your design we described to you, and it is in our public API reference. A creator is an entity. Onboarding runs KYC or KYB on a provider connection that the request names. An approved onboarding lets you open an account, which comes back with an account and routing number. Transfers run on ACH, same-day ACH, wire and RTP. What the reference does not state, and we therefore mark open, is which US banking providers are connected today and whether one entity can hold onboardings on several connections at once. We will name both in writing, and the second is the first thing to prove in a sandbox.  
  
\#\#\# Slide 14 · \`who-decides\` · white content slide  
  
\- 03 · Decision layer · who decides  
\*\*Headline:\*\* You asked who decides where each creator lands. You do: per call for banking today, and by rule for card payments.  
\- Source: docs.y.uno, Banking Connectivity; Routing; Monitors; Audit logs; Roles. Read 7 October 2026.  
\- BOX: \[CONFIRMED\] · Per call · banking · \*\*Your policy names the provider\*\* · Every onboarding request carries the provider connection it should run on. Your own allocation logic picks the bank. Yuno executes on it and reports status back by webhook.  
\- BOX: \[CONFIRMED\] · By rule · card payments · \*\*Rules you configure\*\* · Conditions on country, amount, BIN, brand and your own metadata. Percentage splits. Fallback steps on decline, error rate or timeout. Monitors that move traffic away and bring it back.  
\- BOX: \[OPEN\] · By rule · banks and issuers · \*\*The same rules for accounts\*\* · Allocating creators across banks and issuers by rules you set is what we described to you. It is not in the public API reference yet. Owner: Yuno product, in writing with the RFP response.  
\- What you get  
\- \*\*Yours:\*\* The policy belongs to OnlyFans. The API takes the connection you name on each onboarding.  
\- \*\*Changeable:\*\* A new bank for a creator is a new onboarding on that connection (one entity on several is open item 3). Card traffic moves by changing a rule.  
\- \*\*Visible:\*\* Audit logs for dashboard and API activity, custom roles and SAML sign-on.  
  
\*\*Speaker notes:\*\* You asked this more than once, so here is the precise answer. Today, for banking, the decision is literally yours on every call: the onboarding request names the provider connection, so your allocation policy picks the bank and Yuno executes. For card payments, rule-based routing is a mature product: conditions, splits, fallbacks and monitors, set by you. What we told you about rule-based allocation across banks and issuers is where the product is going; it is not in the public reference yet, so we mark it open and owe you a written answer.  
  
\#\#\# Slide 15 · \`s4-versus\` · black slide with orb artwork  
  
\- 04  
\*\*Headline:\*\* Versus a standalone vault  
\- Where VGS and Basis Theory lead, and where they stop.  
\- 01 Vault  
\- 02 Proxy  
\- 03 Decision layer  
\- 04 Versus a standalone vault  
  
\*\*Speaker notes:\*\* Section four compares Yuno with the two standalone vaults you are most likely evaluating. Both are good products. We show where they lead as well as where they stop.  
  
\#\#\# Slide 16 · \`versus-thesis\` · white content slide  
  
\- 04 · Versus a standalone vault · the difference  
\*\*Headline:\*\* A standalone vault is built to store and forward. The rules that decide where each request goes are yours to write and maintain.  
\- BOX: VGS · \[PUBLIC DOCS\] · "VGS does not make routing decisions for you." · "VGS powers orchestration, but does not act as the orchestrator." · verygoodsecurity.com, payment orchestration page  
\- BOX: Basis Theory · \[PUBLIC DOCS\] · Its vault "operates independently of any payment processor or orchestration layer." · Its creator-economy page markets routing and retries across processors. We found no rules product. Ask who writes and maintains the rules. · Basis Theory press release, 14 October 2025; basistheory.com  
\- BOX: What stays on your roadmap · The rules for which bank, issuer or processor each request goes to · Retries, fallbacks and failover between providers · Every provider integration, and its upkeep when an API changes · Moving money: accounts, transfers and payouts  
\- So what  
\- You already asked the hard question: who decides. With a standalone vault, the rules and every connection are yours to build and maintain. With Yuno, card routing is a rule you configure today and bank allocation is a value you set per call; rules for banks are an open item on slide 21.  
  
\*\*Speaker notes:\*\* This is the one difference that matters for your design, in the vendors' own words. VGS says plainly that it does not make routing decisions for you. Basis Theory describes its vault as independent of any processor or orchestration layer. That independence is a real strength if storage is the whole job. In a product with two to five banks, several issuers and several transfer providers per creator, it means the rules, the failover logic and the upkeep of every integration sit with you. Ask each vendor exactly how much of that they run for you.  
  
\#\#\# Slide 17 · \`versus-table\` · white content slide  
  
\- 04 · Versus a standalone vault · item by item  
\*\*Headline:\*\* Nine things your design needs, and who leads on each.  
\- \[PUBLIC DOCS\]  
\- Yuno: docs.y.uno and y.uno. VGS and Basis Theory: public pages. Read 7 October 2026. "Found" means in the pages read.  
  
| \# | Your design needs | Yuno | VGS | Basis Theory | Who leads |  
|---|---|---|---|---|---|  
| 1 | PCI DSS Level 1 card vault | Yes, hosted capture fields | Yes, Collect and Show | Yes, Elements | Level |  
| 2 | Network tokens | Three networks. Requestor model open | Four networks | Requestor ID created for you | Vaults lead |  
| 3 | A proxy to any destination | Outbound, in beta. No inbound route or custom code | Inbound and outbound routes, plus custom code | Proxy, plus serverless Reactors | Vaults lead |  
| 4 | Bank accounts, tax IDs, documents | Bank accounts: yes. Tables for other records: open | PII, bank accounts and IBANs as aliases | Token types for bank, SSN and EIN data | Vaults lead |  
| 5 | Show an issued card, set its PIN | Not in our public documentation | Card display with VGS Show | Card display; PIN set with Lithic and Marqeta | Vaults lead |  
| 6 | Rules for where each request goes | Card payments: rules, splits, fallbacks. Banks: per call | Says it "does not make routing decisions for you" | Routing and retries marketed; no rules product found | Yuno leads |  
| 7 | Provider connections built for you | 460+ processor integrations. US banks: open | Your own logic, or an orchestrator partner | Proxy requests you write per provider | Yuno leads |  
| 8 | Bank accounts and transfers by API | Entities, accounts, ACH, wire and RTP | No API found. Forwards bank details to your processor | No API found. Forwards bank details to your processor | Yuno leads |  
| 9 | Payouts and split payments | Payouts API, split payments | Via partners like TabaPay, Astra | No payouts product found | Yuno leads |  
  
  
\*\*Speaker notes:\*\* The comparison row by row. Rows two to five are where VGS and Basis Theory lead today, and we would rather you hear it from us: deeper network token programs, a more established proxy with custom code, token types built for personal data, and tooling to show an issued card, plus PIN setting at Basis Theory. The next two slides take each vendor on its own. Rows six to nine are what your architecture adds on top of a vault, and that is where Yuno leads. The competitor columns come from their public pages on 7 October; where a cell says something was not found, we mean on those pages, so please confirm with them.  
  
\#\#\# Slide 18 · \`versus-bt\` · white content slide  
  
\- 04 · Versus a standalone vault · Basis Theory  
\*\*Headline:\*\* Basis Theory goes deeper on the vault. Yuno goes further above it.  
\- \[PUBLIC DOCS\]  
\- Basis Theory: basistheory.com and developers.basistheory.com. Yuno: docs.y.uno and y.uno. Read 7 October 2026.  
  
| What you need | Yuno | Basis Theory | Who leads |  
|---|---|---|---|  
| Card capture and storage | SDK enrollment into a PCI DSS Level 1 vault | Elements into a PCI DSS Level 1 vault | Level |  
| Data beyond cards | Bank details through the enroll API. Tables for personal records: open | Token types for bank accounts, SSN, EIN and generic data | Basis Theory |  
| Proxy and custom code | Outbound proxy, in beta. No inbound route and no custom code | Proxy with request and response transforms, plus serverless Reactors | Basis Theory |  
| Card issuing | Stored card data can go to issuer APIs. Card display and PIN: not in our docs | Guides to issue and display cards. PIN setting documented for Lithic and Marqeta | Basis Theory |  
| Token requestor ID | Yuno holds it, per our API reference. In your name: open | Creates one for you with each network. Existing network tokens are re-provisioned, not imported | Basis Theory |  
| Routing rules and failover | A rules product for card payments: conditions, splits, fallbacks and monitors | Routing and retries marketed. No rules product found | Yuno |  
| Provider integrations | 460+ processor integrations. US banks: open | Proxy requests you write for each provider. No pre-built connectors found | Yuno |  
| Bank accounts and transfers | Banking Connectivity API: entities, accounts, ACH, wire and RTP | No accounts or transfers API found. Stores bank details and forwards them to your processor | Yuno |  
| Payouts | Payouts API and split payments | No payouts product found. Forwards to payout processors you choose | Yuno |  
  
  
\*\*Speaker notes:\*\* Basis Theory on its own. It is a strong vault, and it knows your sector: its creator-economy page quotes a creator platform whose processor shut it off without warning. It leads us on four rows today: token types for personal data, a proxy with transforms and serverless code, card issuing guides, and a clear statement that it creates the token requestor ID for you. We lead on the four rows above the vault: a rules product for routing and failover, processor integrations that are already built, a banking API, and payouts. Two questions worth asking them: who writes and maintains the routing rules they market, and what the cost is at your scale. Their public list price is 995 dollars a month for 20,000 stored tokens, then 5 cents per additional token each month; ask for the enterprise schedule at your volume.  
  
\#\#\# Slide 19 · \`versus-vgs\` · white content slide  
  
\- 04 · Versus a standalone vault · VGS  
\*\*Headline:\*\* VGS stores and reveals. Its own guide leaves the decisions to you.  
\- \[PUBLIC DOCS\]  
\- VGS: verygoodsecurity.com and docs.verygoodsecurity.com. Yuno: docs.y.uno and y.uno. Read 7 October 2026.  
  
| What you need | Yuno | VGS | Who leads |  
|---|---|---|---|  
| Card capture and storage | SDK enrollment into a PCI DSS Level 1 vault | VGS Collect and Show, PCI DSS Level 1 vault | Level |  
| Data beyond cards | Bank details through the enroll API. Tables for personal records: open | PII, bank account numbers and IBANs stored as aliases | VGS |  
| Proxy and custom code | Outbound proxy, in beta. No inbound route and no custom code | Inbound and outbound routes, plus custom code that runs in the proxy | VGS |  
| Card issuing | Stored card data can go to issuer APIs. Card display and PIN: not in our docs | Card issuing guide (examples: Marqeta, I2C, Galileo), with card display through VGS Show | VGS |  
| Network tokens | Visa, Mastercard and American Express once activated. Cryptograms: Visa and Mastercard | Says it is the only neutral vault connected to all four major networks | VGS |  
| Routing rules and failover | A rules product for card payments: conditions, splits, fallbacks and monitors | "Your application keeps ownership of provider selection, routing, and failover logic." | Yuno |  
| Provider integrations | 460+ processor integrations. US banks: open | Your own logic, or an orchestrator partner | Yuno |  
| Bank accounts and transfers | Banking Connectivity API: entities, accounts, ACH, wire and RTP | No accounts or transfers API found. Tokenizes bank details and forwards them to your processor | Yuno |  
| Payouts | Payouts API and split payments | Via partners, including TabaPay and Astra | Yuno |  
  
  
\*\*Speaker notes:\*\* VGS on its own. It is one of the longest-established independent vaults, and it leads us on four rows today: aliases for personal and bank data, inbound and outbound proxy routes with custom code, a card issuing guide with card display, and network token reach, where it says it is the only neutral vault connected to all four major networks. VGS is also explicit about where its scope ends. Its orchestration page says it does not make routing decisions for you, and its guide to integrating a second payment provider says your application keeps ownership of provider selection, routing and failover logic. For a product with several banks, issuers and transfer providers per creator, that logic is most of the work. That is the part Yuno covers for card payments today, and the part we are extending to banks. VGS's public pricing starts at 1,000 dollars a month; ask both of us for the cost at your scale.  
  
\#\#\# Slide 20 · \`shape\` · white content slide  
  
\- Proposed shape  
\*\*Headline:\*\* Three phases that mirror your scope, each with a test you can run to close it.  
\- BOX: Phase 0 · sandbox proof · \*\*Prove it on your own requests\*\* · Your engineers vault test cards and bank details, forward the cards through the proxy to two destinations you pick, and walk the banking API with our product team. · The exit · Every Confirmed capability your Phase 1 relies on is shown working to your engineers, or we change the label.  
\- BOX: Phase 1 · US balances · \*\*Cards, accounts and your first banks\*\* · The vault in production for US creators. Banking connections live. Allocation by your policy, per call, with API activity in the audit log. · The exit · One creator holds accounts on two banking connections, opened from one entity record. Depends on open item 3.  
\- BOX: Phase 2 · issuers and beyond · \*\*Issuers, and more records\*\* · Stored card data sent to issuer APIs through the proxy. Tables for identity and customer records as they land. Stablecoin conversion providers scoped with you. · The exit · Adding or swapping a provider is a configuration change on your side, not a project.  
\- At any phase  
\- You can leave with your cards: a documented export, on written request, to a recipient with a valid PCI DSS attestation. Export of bank and entity data is one of the open items.  
  
\*\*Speaker notes:\*\* We are proposing phases, not dates, until we have seen your RFP timeline. Phase 0 is a sandbox proof on your own requests, and its exit is simple: every capability this deck marks Confirmed that your Phase 1 relies on has to run for your engineers, or we change the label. Phase 1 is your stated scope, US balances. Phase 2 brings in issuers through the proxy and the wider data vault as it lands.  
  
\#\#\# Slide 21 · \`owe\` · white content slide  
  
\- What we owe you  
\*\*Headline:\*\* Six open items, each with an owner and a written answer in our RFP response.  
  
| \# | Open item | Why it matters to you | Owner at Yuno |  
|---|---|---|---|  
| 1 | Tables you define for identity and customer records, and how bank and entity data is stored and accessed: availability and API reference | Banking as a service puts far more than cards in the vault. | Trust & Vault product |  
| 2 | Rule-based allocation of creators across banks and issuers | It turns "who decides" from code you maintain into a rule you set. | Product |  
| 3 | US banking and issuing providers connected today, their policy for your category, and one entity on several connections | No single bank should be able to cut a creator off. That depends on which banks are behind the API. | Partnerships |  
| 4 | Token requestor model for each card network, and export of bank and entity data | Together they decide what you can take with you if you ever change vault. | Trust & Vault product |  
| 5 | Contractual uptime, failover design and rate limits | A vault in the payment path must never be the weak point. | Engineering |  
| 6 | Stablecoin conversion providers | Yield on balances is part of your design, and outside the vault itself. | Partnerships |  
  
  
\*\*Speaker notes:\*\* These are the six things we have not confirmed in writing, collected in one place. Each has an owning team at Yuno, and each gets a written answer with our RFP response. If any of them is a deciding factor for you, tell us now and we will answer it first.  
  
\#\#\# Slide 22 · \`next\` · black slide with orb artwork  
  
\- Next steps  
\*\*Headline:\*\* Include us, then test us.  
\- BOX: Step 01 · OnlyFans · \*\*Share the RFP requirements\*\* · And the timeline, so we answer in your format and to your deadline.  
\- BOX: Step 02 · Together · \*\*One working session\*\* · Your payments and engineering leads with our Trust & Vault product team: vault, proxy and banking API in the sandbox.  
\- BOX: Step 03 · Yuno · \*\*Written answers\*\* · The six open items and the full RFP response, with nothing left as a placeholder.  
\- Samuel Vieira · Business Development · samuel@y.uno  
  
\*\*Speaker notes:\*\* The ask is simple: include Yuno in the RFP, and then test what we have shown you. Send us the requirements and the timeline. Give us one working session with your payments and engineering leads and our Trust & Vault product team, in the sandbox. We will come back with written answers to every open item and a complete response.  
  
\#\#\# Slide 23 · \`app-limits\` · white content slide  
  
\- Appendix · limits to plan for  
\*\*Headline:\*\* What the vault and proxy do not do today, so you can plan around it.  
\- From docs.y.uno, read 7 October 2026. The proxy is in beta and enabled per organization.  
  
| Item | Today | Basis |  
|---|---|---|  
| Inbound proxy | Not in the public API reference. The forward proxy is outbound only. | \[NOT IN DOCS\] |  
| Cards issued by your issuer | A card number returned by a destination is redacted, not vaulted. Showing an issued card to its holder and setting a PIN are not documented. | \[NOT IN DOCS\] |  
| Custom code on stored tokens | Not offered today. | \[NOT IN DOCS\] |  
| BIN lookup as its own API | No standalone endpoint. BIN, brand, issuer, type and country come back with each stored card. | \[CONFIRMED\] |  
| Signing and cryptograms | One built-in request-signing scheme, for dLocal; mutual TLS for other destinations. Network token cryptograms for Visa and Mastercard. | \[CONFIRMED\] |  
| What the proxy resolves | Card fields only: number, expiration, holder name, network token, network transaction ID and, per the proxy guide, the security code inside its window. Bank data is not resolved by the proxy. | \[CONFIRMED\] |  
| Token search | Stored payment methods are listed per customer. There is no vault-wide search in the reference. | \[CONFIRMED\] |  
| Idempotent forwards | Not in the public API reference. Until it is, a retry after a timeout needs a status check at the destination. | \[NOT IN DOCS\] |  
  
  
\*\*Speaker notes:\*\* Appendix. These are the limits as they stand today, so nobody on your side discovers them later. The two that matter most for an issuing use case are the first two: there is no inbound proxy in the public reference, and a card number that comes back from your issuer is redacted rather than vaulted. If your Phase 1 needs to show an issued card to a creator or set a PIN, that is a gap for us today and a strength of a standalone vault.  
  
\#\#\# Slide 24 · \`app-who\` · white content slide  
  
\- Appendix · who we are  
\*\*Headline:\*\* The vault runs in a PCI DSS Level 1 environment.  
\- Source: y.uno vault product page and docs.y.uno API environments, read 7 October 2026.  
\- Integrations  
\- 460+  
\- Processor integrations: PSPs, gateways and acquirers the vault can detokenize to.  
\- Countries covered  
\- 190+  
\- With separate API environments for the US (api.y.uno) and EMEA (api.eu.y.uno).  
\- Certifications  
\- 4  
\- Plus registration as a Visa Service Provider, as listed on y.uno. Attestation scope on request.  
\- As listed  
\- Chip "PCI DSS Level 1"  
\- Chip "SOC 2 Type 2"  
\- Chip "ISO 27001"  
\- Chip "ISO 27701"  
\- Chip "Visa Service Provider"  
  
\*\*Speaker notes:\*\* Appendix. Yuno in three numbers, all from our public site. More than 460 processor integrations the vault can detokenize to. Coverage in more than 190 countries, with separate API environments for the US and EMEA. Four certifications plus Visa Service Provider registration, as listed on our site; ask us for the attestation documents and their scope and we will route the request to our security team.  
  
\#\#\# Slide 25 · \`app-sources\` · white content slide  
  
\- Appendix · sources  
\*\*Headline:\*\* Every page behind this deck, all read on 7 October 2026.  
\- Yuno  
\- \[CONFIRMED\]  
\- docs.y.uno · Tokens; PCI compliance; Enroll payment methods  
\- docs.y.uno · PCI Proxy: overview, forward proxy, destination allowlist, destination authentication  
\- docs.y.uno · Network tokens; Generate network token cryptogram; Card account updater  
\- docs.y.uno · Token migration process; Exporting tokens from Yuno  
\- docs.y.uno · Banking Connectivity reference: entities, onboarding, accounts, transfers  
\- docs.y.uno · Routing; Monitors; Audit logs; Roles; Security; API environments  
\- docs.y.uno · Payouts; Split payments marketplace  
\- docs.y.uno · API changelog, July to September 2026  
\- y.uno · Vault product page  
\- VGS and Basis Theory  
\- \[PUBLIC DOCS\]  
\- verygoodsecurity.com · Payment orchestration; Vault; Network tokens; Card issuers; Pricing  
\- docs.verygoodsecurity.com · Integrating a second payment provider; Card issuing; VGS Compute (Larky)  
\- basistheory.com · Platform; Creator economy; Pricing details  
\- developers.basistheory.com · Token types; Network tokens; Issue cards; Set card PIN  
\- Basis Theory press release · 14 October 2025, PR Newswire  
\- Competitor lines are our reading of public pages on the date shown. Products change. Please confirm each one with the vendor before you rely on it.  
  
\*\*Speaker notes:\*\* Appendix. The pages behind every claim, so your team can open them. Yuno claims come from our public documentation and product page. Competitor lines come from their own public pages on the same date; please confirm them with each vendor.  