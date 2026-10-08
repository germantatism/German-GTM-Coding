# Visual QA · OnlyFans token vault deck (Google Slides 10A2GokDXPEPkeqqS29H7a460R6j5ux60nILIqUXmUKc)

Reviewed 8 Oct 2026 from `thumbs_build/b_01.png` to `b_61.png` (every slide opened individually, 1600x900 LARGE thumbnails), against the Eventbrite template thumbnails.

## Read this first
- The live deck has 61 slides, the spec has 60. The buyer-questions checklist was split into three slides (positions 22, 23, 24 titled "1 of 3 / 2 of 3 / 3 of 3") instead of the spec's two. Positions 1 to 21 match the spec; from position 25 on, live position = spec index + 1. In-deck cross references ("slide 36", "slide 49, 50 and 51", "slide 54", "slide 61") already use the live numbering and are correct.
- Footer page numbers equal the slide position on every numbered slide (checked 4 to 61). Yuno wordmark present top right on every white and dark content slide. Cover lockup `yuno + OnlyFans` sits on one baseline. No leftover template text (Eventbrite, Bending Spoons, BSP, Paul, Milan, ticketing) on any slide. Fonts, colours and margins match the template throughout.
- Pills render correctly and readably everywhere they appear: CONFIRMED green, BETA grey, PUBLIC DOCS blue, OPEN amber, NOT IN DOCS grey, DIRECTION lavender.
- Result: 30 FIX, 31 OK. Five slides have overlapping or clipped text that a reader will notice immediately (25, 36, 37, 38, 48). Three engine-level bugs explain most of the rest and can be fixed once in `gs_engine.py` rather than slide by slide:
  1. Card kicker box is too narrow when a pill shares its row (two pills leave it almost zero width): long kickers wrap into the card title (10, 35, 38, 42) or render one letter per line (38). Fix: kicker width = card width minus pill widths minus 24 px, or put pills on their own row above the kicker.
  2. The source line box holds one line; a two-line source prints its second line over the footer "For: OnlyFans" (11, 12, 14, 15, 29). Fix: anchor the source box bottom at y = 845 px and allow two lines, or cap source text at 160 characters.
  3. Three-line headlines are allowed but the third line is a one-word widow on 6, 12, 14, 18, 20 and collides with content on 37 and 48. Fix: cap headline at 118 characters (two lines at this size) or shrink by one step when a third line would be a single word.

## Slide by slide (position · id · verdict · what is wrong · smallest fix)
01 · cover · OK
02 · agenda · OK
03 · d01 · OK
04 · understood · OK (diagram connectors touch all boxes, pill "Rules set by OnlyFans" readable)
05 · howtoread · FIX · Bottom 35% of the slide is empty below the "Why it matters" band; cards are 250 px tall with content filling them, so the gap is the band position. Fix: stretch the three cards from 250 px to about 400 px tall (band moves down to about y = 700), or move the band to y = 740.
06 · answer · FIX · Headline wraps to three lines and the third line is the single word "today."; the three stat cards are 380 px tall with about 60% empty. Fix: shorten headline to 105 characters: "A vault stores the credential. Your design also needs a layer that decides where it goes. Yuno does both."; reduce card height from 380 px to 230 px and move the "In one line" band up to follow.
07 · exec · OK
08 · d02 · OK
09 · industry-glance · FIX · The four stat cards are 340 px tall with about 50% empty, and the "Who launched what" paragraph underneath ends 10 px above the band (cramped, flagged as overflow by the engine). Fix: reduce card height from 340 px to 230 px; the paragraph then has 110 px of air.
10 · no-single-bank · FIX · Fourth card kicker "2024 TO 2025 · THE REGULATORS' ANSWER" wraps to two lines and "ANSWER" touches the card title. Fix: shorten kicker to "2024 TO 2025 · REGULATORS" (25 characters) or apply the engine kicker-width fix.
11 · vault-2026 · FIX · Source line wraps to two lines; the second line "Mar 2026." sits on top of the footer "For: OnlyFans". Fix: shorten to 155 characters: "PCI SSC, 26 Mar 2025; Visa and Mastercard newsrooms, 2024 to 2026; Digital Transactions, 14 Nov 2024; CRS IF13174, 6 Mar 2026; Paul Hastings, 12 Mar 2026."
12 · vault-market · FIX · Headline third line is the single word "buying."; source line wraps and "(estimates)." overprints the footer. Fix: headline to 86 characters: "Independent vaults come in three shapes. The RFP should state which one it is buying."; source to 160 characters by dropping "About and newsroom" and "profiles".
13 · d03 · OK
14 · of-numbers · FIX · Headline third line is the single word "headcount."; source wraps to two lines and the second line overprints the footer; third card "THE FOOTPRINT" is about 55% empty. Fix: headline to 115 characters: "OnlyFans moves $6 billion a year to 2.5 million creators with 47 staff. Any new layer must scale without headcount."; source to 160 characters by dropping "Companies House officers, read 8 Oct 2026".
15 · traffic · FIX · Source wraps to two lines and "OnlyFans Terms of Service, last updated Aug 2024." overprints the footer; bottom 45% of the slide is empty (bar chart ends at y = 440). Fix: source to 160 characters ("Share of web traffic: Similarweb, onlyfans.com, Sep 2026 (top five). Revenue split: Fenix FY2023 accounts via Mostly Metrics. OnlyFans Terms, Aug 2024."); raise bar row pitch from 49 px to 75 px so the chart ends near y = 600.
16 · stack · OK (headline is three full lines, acceptable)
17 · lesson-2021 · OK
18 · four-numbers · FIX · Headline third line is the single word "clock."; the "7 days" caption runs three lines to within 14 px of the card border. Fix: headline to 111 characters: "Four published rules define what a vault must serve: one fee, one currency, one pending window, one payout clock."; caption to 62 characters: "Pending balance before withdrawal; 21 days in a few countries".
19 · d04 · OK
20 · cof-today · FIX · Headline third line is the single word "keys.". Fix: 113 characters: "Cards live with the processors today and bank accounts with OnlyFans. The RFP can put both under one set of keys."
21 · five-data · OK
22 · questions-1 · OK (note: slides 23 and 24 carry a source line, this one does not; add the same line for consistency)
23 · questions-2 · FIX · Only four rows; the lower half of the slide is empty (table ends at y = 580, source at y = 829). Fix: rebalance the 15 questions 5/5/5 across slides 22, 23, 24 instead of 7/4/4.
24 · questions-3 · FIX · Same as 23: four rows, lower half empty. Same rebalance.
25 · clocks · FIX · MAJOR. Stat values "31 Mar 2025" and "18 Jan 2027" do not fit the card width at the stat size, wrap to two lines, and the second line ("2025", "2027") prints over the body text. Cards also about 60% empty. Fix: change the values to "Mar 2025" and "Jan 2027" (move the day into the caption), or set the stat font to 32 pt on this slide; reduce card height from 380 px to 230 px.
26 · d05 · OK
27 · yuno-story · OK (template slide, footer added correctly)
28 · four-pillars · OK (template slide)
29 · compliance · FIX · Source wraps to two lines; "team." overprints the footer. Fix: 157 characters: "Source: y.uno vault and trust pages, y.uno/sla (24 Oct 2025), status.y.uno, docs.y.uno API environments. Read 8 Oct 2026. Reports and attestations on request."
30 · offices · OK (template slide)
31 · trusted · OK (template slide)
32 · team · FIX · Inherited from the template: "Martin Mexia" wraps to two lines and "Mexia" prints over the role "SVP, PRODUCT". Fix: widen that name box by 40 px or set the name at one size smaller so it stays on one line.
33 · dedicated · FIX · A stray light-grey "33" sits at the bottom-left corner (x about 30, y about 870) in addition to the real page number at the right; it is a leftover text box from the template slide. Fix: delete that text box.
34 · d06 · OK
35 · vault-cards · FIX · Second card kicker "KEEP CURRENT" wraps ("KEEP / CURRENT") and the second line touches the title "Network tokens and account updater"; the three cards are 600 px tall with 40 to 60% empty. Fix: engine kicker-width fix (or kicker "KEEP", 4 characters); card height from 600 px to 420 px.
36 · vault-data · FIX · MAJOR. The dark card titles wrap one syllable per line because the title box is squeezed beside the pill: "card / s · / PCI", "bank / acco / unts · / ACH", "entit / ies · / KYC · / KYB", "your own / tables · / PII". The entities card's last sentence ("Taken by the banking API. Responses return the last four.") spills below the card and prints in pale text on the white background. Bottom 35% of the slide is empty. Fix: put the pill on its own line at the top of the card and give the title the full card width on the next line (titles "cards · PCI", "bank accounts · ACH", "entities · KYC · KYB", "your own tables · PII"); raise the dark card height from 352 px to 470 px so the entities content fits.
37 · keep-current · FIX · MAJOR. Headline wraps to three lines and the third line "processors." prints over the label "LANE 1 · NETWORK TOKENS · PROVISIONED ONCE PER CARD". The "Yuno vault" blue box text is cut at the box bottom ("docs), updated when the card is" and then nothing). The "Any processor you connect" and "Updated •••• 7740" light boxes have text running past their bottom edges. Fix: headline to 113 characters: "Card on file does not have to break: network tokens and the account updater keep the token valid across reissues."; raise every lane box from 125 px to 185 px tall (200 px are free below lane 2); cut the "Yuno vault" text to 110 characters.
38 · move · FIX · MAJOR. Third card has two pills, which leaves the kicker box a few pixels wide: "EXPORT · YOUR EXIT" renders one letter per line down the left edge of the card, over the body text. Second card kicker "IMPORT · NETWORK TOKENS" wraps to three lines and "TOKENS" prints over the title "A separate documented process". Cards 600 px tall, about 45% empty. Fix: engine kicker-width fix plus kickers "CARDS IN" (8), "TOKENS IN" (9), "EXPORT" (6); card height from 600 px to 420 px.
39 · proxy-how · FIX · The two black code boxes are 510 px tall and the code fills only the top 250 px, so half of each box is empty black. Fix: reduce both code boxes from 510 px to 320 px tall (keep the "Yuno proxy" arrow centred on the new height).
40 · proxy-controls · OK
41 · banking · OK (diagram connectors touch every box; best diagram in the deck)
42 · who-decides · FIX · All three kickers wrap into their titles: "PER CALL · BANKING" (second line touches the title), "BY RULE · CARD PAYMENTS" ("PAYMENTS" over "Rules you configure"), "BY RULE · BANKS AND ISSUERS" ("ISSUERS" over "The same rules for"). Cards 600 px tall, about 55% empty. Fix: engine kicker-width fix plus kickers "BANKING" (7), "CARDS" (5), "BANKS AND ISSUERS" (17); card height from 600 px to 420 px.
43 · direction-architecture · FIX · The connector label "creator data as tokens" is hidden behind the two blue boxes; only "ata ·" peeks out in the 22 px gap between "Yuno · orchestration" and "Yuno · vault". Fix: delete that label (and the orchestration-to-vault connector it labels), or move it below the vault box at y about 520.
44 · direction-rules · FIX · Right column header "NO SINGLE POINT OF FAILURE · BACKUP BANKS READY BEFORE YOU NEED THEM" wraps and "NEED THEM" prints over item "01 Backup accounts opened at sign-up". Fix: 52 characters: "NO SINGLE POINT OF FAILURE · BACKUP BANKS READY EARLY".
45 · direction-yield · FIX · Right column header "PLUGGABLE ISSUERS · ADD OR SWAP CARD ISSUERS LIKE ANY OTHER CONNECTION" wraps and "CONNECTION" prints over item "01 Issuers connect like PSPs and banks". Fix: 51 characters: "PLUGGABLE ISSUERS · ADD OR SWAP LIKE ANY CONNECTION".
46 · d07 · OK
47 · versus-thesis · OK
48 · versus-model · FIX · MAJOR. Four collisions on one slide: (a) headline wraps to three lines and the third line "Yuno." prints over the italic quote block; (b) the two-line italic quote ("VGS powers orchestration..." / "Basis Theory's vault operates...") runs into the dark table header; (c) column header "STANDALONE VAULT, PLUS AN ORCHESTRATOR ON TOP" wraps and "TOP" prints over "OPTION B"; (d) row labels "Provider connections, built and maintained" and "Vendors, contracts and incident ownership" wrap and their second line prints over the grey sub-caption. Fix: headline to 86 characters: "One project instead of two: what stays on your roadmap with each of the three options."; delete the italic quote block (both quotes already appear on slide 47); column header to "STANDALONE VAULT PLUS AN ORCHESTRATOR" (37); row labels to "Provider connections" (20), "Vendors and incidents" (21), "Bank accounts and payouts by API" (32).
49 · versus-table · OK
50 · versus-bt · OK
51 · versus-vgs · FIX · Headline wraps with the single word "you." on the second line. Fix: 58 characters: "VGS stores and reveals. Its guide leaves decisions to you."
52 · d08 · OK
53 · shape · OK
54 · owe · OK
55 · next · FIX · The three step cards are 245 px tall with about 50% empty and the slide is empty below the blue contact band (y = 558 to 840). Fix: reduce card height from 245 px to 170 px and keep the band directly under them; the remaining white space is acceptable on a closing-steps slide.
56 · closing · OK (a 1 px vertical tick at x about 62, y about 455 is inherited from the template closing slide; harmless)
57 · d-appx · OK
58 · app-limits · OK
59 · app-who · FIX · Three stat cards 380 px tall with about 60% empty above the certification chips. Fix: reduce card height from 380 px to 230 px and move the chip row up to y about 480.
60 · credentials · OK
61 · app-sources · FIX · Left list item 03 wraps to two lines and its second line "updater" prints over item 04 "docs.y.uno · Token migration process". Fix: item 03 to 62 characters: "docs.y.uno · Network tokens; cryptograms; Card account updater".

## Top 10 most visible problems (fix before the deck leaves the building)
1. Slide 36 (vault-data): card titles broken one syllable per line ("card / s · / PCI") and the entities card's last sentence spills below the card as pale text on white.
2. Slide 48 (versus-model): headline third line "Yuno." over the quote, the quote into the table header, "OPTION B" header wrap ("TOP"), and two row labels printing over their captions.
3. Slide 37 (keep-current): headline third line "processors." over the LANE 1 label; three flow boxes with text cut or running out of the bottom.
4. Slide 25 (clocks): "31 Mar 2025" and "18 Jan 2027" wrap and the year prints over the body text.
5. Slide 38 (move): kicker "EXPORT · YOUR EXIT" rendered one letter per line down the card; "IMPORT · NETWORK TOKENS" over the title.
6. Slide 42 (who-decides): all three kickers wrap into the card titles.
7. Slides 44 and 45 (direction two-column): right column header wraps onto item 01 on both.
8. Slides 11, 12, 14, 15, 29: two-line source text overprints the footer "For: OnlyFans" (one engine fix).
9. Slides 10 and 35: long kickers wrap into the card title ("THE REGULATORS' ANSWER", "KEEP CURRENT"), same kicker-width bug as 38 and 42.
10. Slide 43 (direction-architecture): hidden connector label peeking out as "ata ·" between the blue boxes; and slide 61 (sources) item 03 wrapping onto item 04.
Also worth two minutes: the stray "33" bottom-left on slide 33 and the inherited "Martin Mexia" wrap on slide 32.

## Slides that look good enough to present live as they are
01 cover · 04 understood (design diagram) · 07 executive summary · 16 stack · 17 the 2021 lesson table · 21 six data classes table · 22 buyer questions 1 of 3 · 40 proxy controls · 41 banking API diagram · 47 versus thesis · 49 nine things item by item · 50 Basis Theory row by row · 53 three phases · 54 six open items · 58 limits to plan for · 28 four pillars (template) · 56 closing.
After their one-line fixes, 29 (compliance) and 51 (VGS) join that list.
