# deck_spec.json schema · OnlyFans token vault deck (gs_engine.py)

Field names are the ones agreed with the coordinator on 8 Oct 2026. `python3 gs_engine.py check deck_spec.json` validates and fit-checks a spec offline (no API calls); `python3 gs_engine.py build deck_spec.json --final` builds it.

## Top level
```json
{"presentation_id": "10A2GokDXPEPkeqqS29H7a460R6j5ux60nILIqUXmUKc", "merchant": "OnlyFans", "footer": "For: OnlyFans", "slides": [ ... ]}
```
`footer` is printed bottom-left on every content slide at 6.5 pt grey; the page number (position in the final deck) is printed bottom-right automatically. Cover, dividers and closing carry neither.

## Every slide
```json
{"id": "vault-cards", "type": "cards_row", "kicker": "THE YUNO TOKEN VAULT", "headline": "One vaulted token works on every processor you connect.",
 "source": "docs.y.uno, read 7 Oct 2026", "notes": "Speaker notes, plain text, written for the customer.", "tag": ["CONFIRMED", "BETA"], ...}
```
- `id` string, unique. `type` one of the types below.
- Content slides (every type except cover, agenda, divider, closing, template_keep) need `kicker` (rendered ALL CAPS 7 pt grey at the template's kicker position) and `headline`.
- `headline`: a full sentence. 20 pt when it fits in two lines (box 602 pt wide), else 18 pt in two lines, else 18 pt in three lines (the content zone then starts 17 pt lower). A headline that needs a fourth line raises `FitError` naming the slide id. Never below 18 pt.
- `source` optional one line, 6.5 pt grey at y 369.5. `notes` optional. `tag` optional list of pills shown on the kicker line, right-aligned next to the Yuno wordmark.
- Pill values: `CONFIRMED` (green on #E2F3EB), `BETA` (grey on #EFF0F2), `PUBLIC DOCS` (blue on #E8EAF5), `OPEN` (amber on #FBEFD9), `NOT IN DOCS` (grey). Any other string is rendered as a free-text chip (blue #1227AD on #E8EAF5), used for diagram boxes such as "Rules set by OnlyFans".
- Text items: a cell, card body, list item or bullet may be a string or `{"text": "...", "pill": "OPEN", "pill2": "BETA", "bold": true}`. `**bold**` markup is allowed inside any text. House rules are enforced by `validate()`: no em dash, no " - " as punctuation, never "no small feat".
- Geometry: page 720 x 405 pt, margins 36 pt, content zone x 36..684 (648 wide) from y 95 to 365 (y 112..365 under a three-line headline). Text sizes: body 7.5 to 10 pt, kicker 7 pt caps, source and footer 6.5 pt, nothing below 6.5 pt. When a slide type cannot fit its content at its minimum sizes the builder raises `FitError("slide <id>: ...")` instead of shrinking or overflowing.

## Types

### cover
```json
{"id": "cover", "type": "cover", "title": "The vault under creator banking", "subtitle": "A standalone token vault with the decision layer OnlyFans asked for",
 "presenter": "German Tatis, Yuno · 8 October 2026", "logo_url": "https://deck.yuno.tools/merchants/onlyfans.png", "notes": "..."}
```
Duplicates template slide 1: hero artwork, `yuno + OnlyFans` lockup top-left (logo replaced in place at the Eventbrite logo's height), title 30 pt white (26 pt if it needs three lines), subtitle 12 pt, presenter 8.5 pt.

### agenda
```json
{"id": "agenda", "type": "agenda", "items": [{"num": "01", "title": "Why we are here"}, {"num": "02", "title": "Industry context"}]}
```
Template slide 2 chrome; rows redrawn (Geist Mono numerals #7C89EF, 15 pt caps labels, hairlines). Pitch shrinks with the item count (15 pt down to 11 pt for 9 items).

### divider
```json
{"id": "d01", "type": "divider", "num": "01", "title": "Why we are here", "sub": "What you told us, what we heard, what this deck answers",
 "section_list": ["01 Why we are here", "02 Industry context", "03 How OnlyFans runs payments today"], "notes": "..."}
```
Template slide 3 (dark gradient, white 29 pt title above the hairline). `sub` sits under the title; `section_list` is printed small top-left, current section in white, the rest in #B9BFE8.

### exec_summary
```json
{"id": "exec", "type": "exec_summary", "kicker": "EXECUTIVE SUMMARY", "headline": "...", "left_header": "WHERE ONLYFANS STANDS",
 "left_items": [{"title": "One account, many banks", "body": "..."}, {"title": "...", "body": "..."}],
 "right_header": "WHAT YUNO BRINGS", "right_cards": [{"title": "A vault that is not tied to a processor", "body": "..."}], "bottom": "optional band text"}
```
Left column (x 36..373): header 8 pt blue caps, 4 to 5 titled paragraphs (9/8.5 pt, shrinking to 8.5/7.5 before raising). Right: blue #344FE0 panel (x 393..684) with a 8.5 pt caps header and 3 cards (8 pt bold caps title + 8 pt body, white). Geometry from template slide 10.

### stats
```json
{"id": "answer", "type": "stats", "kicker": "...", "headline": "...",
 "tiles": [{"label": "VAULT", "value": "1", "caption": "token per credential, usable on every processor"}, {"label": "PROXY", "value": "0", "caption": "..."}],
 "chips": ["PCI DSS Level 1", "SOC 2 Type 2", "ISO 27001"], "paragraph": "Optional 9.5 pt paragraph under the tiles.", "bar": "Optional bottom band text."}
```
3 or 4 tiles in a row (outlined, label 7 pt caps grey, value 24 pt bold blue, caption 7.5 pt), optional outlined chips row, paragraph, bottom band.

### scale
```json
{"id": "of-numbers", "type": "scale", "kicker": "...", "headline": "...", "left_header": "THE SCALE TODAY",
 "tiles": [{"value": "$6.6B", "label": "gross payments, FY2024"}, {"value": "2.5M", "label": "creators paid"}], "left_note": "...",
 "mid_header": "WHERE ONLYFANS IS HEADING", "mid_items": ["...", "...", "..."], "right_header": "THE OPERATION", "right_body": "...", "bar": "..."}
```
Three outlined cards 207 x 232 like template slide 4: two 22 pt numbers with labels and a note; three arrow bullets; a body paragraph; optional band.

### four_numbers
```json
{"id": "four-numbers", "type": "four_numbers", "kicker": "...", "headline": "...", "tiles": [{"value": "20%", "label": "platform fee on every transaction"}, {"value": "4", "label": "..."}, {"value": "...", "label": "..."}, {"value": "...", "label": "..."}],
 "right_header": "WHAT THE RULES MEAN FOR A VAULT", "right_items": [{"title": "...", "body": "..."}], "bar": "..."}
```
2 x 2 rounded tiles (outline #B0B7F2, 24 pt black numbers, 7.6 pt labels) left; 3 to 4 titled readings right; optional band. Geometry from template slide 13.

### traffic_list
```json
{"id": "traffic", "type": "traffic_list", "kicker": "...", "headline": "...", "rows": [{"country": "United States", "pct": "41.2%"}, {"country": "United Kingdom", "pct": "6.8%"}],
 "side": {"header": "WHAT IT MEANS", "items": [{"title": "...", "body": "..."}]}, "source": "Similarweb, Sep 2026"}
```
Up to 12 rows: country 9 pt, proportional blue bar, value 9 pt right-aligned, hairlines. With `side`, the list takes the left 55 percent and the side column the rest.

### cards_row
```json
{"id": "vault-cards", "type": "cards_row", "kicker": "...", "headline": "...",
 "cards": [{"eyebrow": "STORE", "num": "01", "title": "Processor-agnostic tokens", "body": "...", "foot": "docs.y.uno/vault", "pill": "CONFIRMED", "pill2": "BETA"}],
 "side": {"header": "...", "items": [{"title": "...", "body": "..."}]}, "limits": {"header": "LIMITS", "tiles": [{"value": "50", "label": "requests per second"}]}, "bar": "..."}
```
2 to 4 outlined cards (num Geist Mono 8 pt #7C89EF, eyebrow 7 pt caps, pills top-right, title 10 pt bold blue, body 8.5 pt, foot 7.5 pt bold deep blue with a blue tick). `side` shrinks the cards to 65 percent width. `limits` draws a four-tile strip (#F4F5FD, 15 pt values) under the cards. Card body that does not fit raises `FitError`.

### two_column
```json
{"id": "x", "type": "two_column", "kicker": "...", "headline": "...", "cols": [{"header": "TODAY", "items": [{"title": "...", "body": "..."}]}, {"header": "WITH YUNO", "items": [...]}], "bar": "..."}
```
Two numbered columns (header 9 pt bold blue caps, items 9 pt bold title + 8.5 pt body shrinking to 7.5).

### table · checklist_table · open_items_table
```json
{"id": "versus-table", "type": "table", "kicker": "...", "headline": "...", "tag": ["PUBLIC DOCS"],
 "columns": ["Need", "Yuno", "Basis Theory", "VGS", "Who leads"], "col_widths": [0.22, 0.22, 0.2, 0.2, 0.16],
 "rows": [["Vault any secret", {"text": "", "pill": "CONFIRMED"}, "Yes", "Yes", "Even"],
          ["Decision layer", {"text": "Trust & Vault product, Legal", "pill": "OPEN", "pill2": "BETA"}, "No", "No", {"text": "Yuno", "bold": true}]],
 "header_style": "dark", "font_size": 8, "bold_first_col": true, "zebra": true, "note": "one line under the table"}
```
Native Slides table (createTable). Header: #282A30 (`dark`) or #3E4FE0 (`blue`) with white 7.5 pt bold caps; body `font_size` (default 8, floor 6.5); first column bold on #E8EAF5; zebra #FFFFFF / #F6F7FB; 1 pt white borders. Pills are overlaid on the cell (one or two side by side); a cell with pills and text prints the text under them in 7 pt grey. Row heights are pinned from a text model (the API does not report rendered heights), so a table that would exceed the zone raises `FitError` with the height it needs.

### comparison_grid
```json
{"id": "versus-model", "type": "comparison_grid", "kicker": "...", "headline": "...", "quote": "Short italic line under the headline.",
 "legend": ["Gap stays open", "Partly closed", "Closed"], "row_header": "THE NEED", "row_header_sub": "What the design requires",
 "options": [{"header": "Standalone vault", "sub": "TODAY"}, {"header": "+ an orchestrator", "sub": "OPTION A"}, {"header": "Yuno vault + decision layer", "sub": "OPTION B · RECOMMENDED"}],
 "rows": [{"label": "Multi-bank routing", "sub": "two to five banks per creator", "cells": [{"state": "open", "text": "..."}, {"state": "partial", "text": "..."}, {"state": "closed", "text": "..."}]}],
 "footer": [{"label": "Gaps closed"}, {"value": "0 of 6"}, {"value": "2 of 6"}, {"value": "6 of 6"}], "closing_line": "...", "source": "..."}
```
Template slide 15 grid: label column 157.5 pt (#E8EAF5, 7.5 pt bold blue + 6.5 pt sub), three option columns (header fills #E8EAF5, #E8EAF5, #1227AD), glyph states ✕ grey / ◐ light blue / ✓ blue, cells 7.5 pt (7 pt before raising), up to 6 rows, footer row, right-aligned closing line.

### diagram
```json
{"id": "understood", "type": "diagram", "kicker": "...", "headline": "...",
 "boxes": [{"id": "lane1", "x": 0, "y": 0, "w": 120, "h": 14, "style": "label", "title": "CREATOR"},
           {"id": "acct", "x": 0, "y": 20, "w": 120, "h": 60, "title": "One OnlyFans account", "body": "...", "style": "blue"},
           {"id": "bank1", "x": 180, "y": 20, "w": 110, "h": 50, "title": "Bank A", "body": "...", "pill": "Rules set by OnlyFans", "style": "light"}],
 "connectors": [{"from": "acct", "to": "bank1", "label": "decision"}],
 "side": {"header": "...", "items": [{"title": "...", "body": "..."}]}, "source": "..."}
```
Box coordinates in pt relative to the content zone origin (0,0 = x 36, y 95; zone 640 x 270, or 420 x 270 when `side` is present; y 112 under a three-line headline). Styles: `light` #F4F5FD, `blue` #3E4FE0 white text, `dark` #282A30 white text, `outline` white with #1227AD line, `panel` #E8EAF5, `label` (no fill or outline, 7 pt bold blue caps lane header). Connectors are straight lines with a filled arrow between facing edge midpoints, optional 6.5 pt label on a white tab. Boxes leaving the zone raise `FitError`.

### code_before_after
```json
{"id": "proxy-how", "type": "code_before_after", "kicker": "...", "headline": "...", "tag": ["CONFIRMED", "BETA"],
 "left": {"title": "WHAT YOU SEND", "code": "POST /v1/proxy\n{\n  \"card\": \"{{ tok_123 }}\"\n}"},
 "middle": {"title": "Yuno proxy", "sub": "swaps tokens for values, forwards, never logs PAN"},
 "right": {"title": "WHAT THE PROVIDER RECEIVES", "code": "{\n  \"card\": \"4111 1111 1111 1111\"\n}", "caption": "Illustrative payload."},
 "side": {"header": "...", "items": [{"title": "...", "body": "..."}]}}
```
Two black code blocks (Geist Mono 7.5 pt, 7 pt when a line is too wide, line breaks preserved) with a middle label and arrow; optional side column (blocks shrink to 196 pt).

### phases
```json
{"id": "shape", "type": "phases", "kicker": "...", "headline": "...", "cards": [{"eyebrow": "PHASE 1", "title": "US card balances", "body": "...", "exit_label": "EXIT TEST", "exit": "..."}], "bar": "..."}
```
Three steps on a #F4F5FD band with arrows between them (template slide 19 rhythm): eyebrow Geist Mono 9 pt, title 10 pt bold deep blue, body 8.5 pt, exit criteria block anchored at the bottom.

### next_steps
```json
{"id": "next", "type": "next_steps", "kicker": "...", "headline": "...", "cards": [{"eyebrow": "THIS WEEK", "num": "01", "title": "Add Yuno to the RFP", "body": "..."}], "contact": "german.tatis@y.uno · +1 786 238 4554"}
```
Three cards plus a blue contact bar.

### sources
```json
{"id": "app-sources", "type": "sources", "kicker": "APPENDIX", "headline": "...", "cols": [{"header": "YUNO", "pill": "CONFIRMED", "items": ["docs.y.uno/docs/vault, read 7 Oct 2026", "..."]}, {"header": "COMPETITORS", "pill": "PUBLIC DOCS", "items": ["..."]}], "footnote": "..."}
```
Two numbered columns, 7.5 pt (7 pt before raising), footnote 6.5 pt.

### closing
```json
{"id": "closing", "type": "closing", "line": "Let's grow together", "name": "German Tatis", "title": "Business Development Manager", "phone": "+1 786 238 4554", "email": "german.tatis@y.uno"}
```
Template slide 46. The layout's `yuno |` lockup is covered and redrawn right-aligned as `yuno | OnlyFans` at matching height (the OnlyFans wordmark is 5.7 times wider than tall, so it cannot sit in the Eventbrite icon slot); if the wordmark image cannot be re-fetched the engine keeps the layout lockup and places the logo at 12 pt height.

### template_keep
```json
{"id": "trusted", "type": "template_keep", "template_index": 25, "replacements": [{"find": "Eventbrite", "replace": "OnlyFans"}],
 "delete_images_matching": ["g3f76accd9b2_0_4"], "notes": "..."}
```
Duplicates a template slide verbatim (index in `template_dump.json` order: 22 Yuno story stats, 23 four pillars, 24 offices, 25 trusted-by logos, 26 team, 27 dedicated team, 38 awards, 40 coverage, 41 credentials, 42 quotes, 45 compliance). `replacements` rewrite every text element containing `find`, preserving styles. `delete_images_matching` takes element objectIds; the placeholder `SPACEX_LOGO_OBJECT_ID` resolves to `g3f76accd9b2_0_4` (SpaceX mark on slide 25). The Eventbrite speaker notes of the source slide are always wiped. If the slide `id` names a known template (yuno-story, four-pillars, offices, trusted, team, dedicated) and `template_index` points elsewhere, the engine prints a warning and uses the slide the id names; `template_ref` can name it explicitly.

## Commands
```
python3 gs_engine.py check deck_spec.json              # offline validation + fit check, no API calls
python3 gs_engine.py build deck_spec.json              # append all slides after the 46 template slides
python3 gs_engine.py build deck_spec.json --only d01,exec
python3 gs_engine.py build deck_spec.json --final      # append all, then delete the 46 template slides in one call
python3 gs_engine.py cleanup                           # delete every slide this engine appended (build_state.json)
python3 qa_thumbs.py [--out thumbs_build] [--from 47]  # thumbnails, contact sheets, geometry and overflow report
```
