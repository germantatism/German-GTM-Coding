# Design system

The look is Samuel's Roblox brief: **clean, engineering-grade, made by people who respect the reader.** Dark ink on white content slides, Yuno Blue accents, one idea per slide, large numbers, simple box-and-line diagrams, generous whitespace. No stock photos, gradients, clip art, 3D, drop shadows or decorative icons. German's information density is welcome in tables and country pages, but each slide still makes one point.

Tokens map the roles to Yuno's official brand palette (Brand Guidelines 20.01.2026, see `REPO/Design System/yuno-commercial-design-system.md`). Samuel's original navy palette is still available as a preset (`YUNO_DECK_THEME=navy`).

## Tokens

| Token | brand (default) | navy (Samuel's original) | Use |
|---|---|---|---|
| navy | 282A30 Unity Black | 0A1F44 | Titles, table headers, dividers, cover and closing backgrounds, total bars |
| blue | 3E4FE0 Yuno Blue | 1A4ED4 | Kickers, big numbers, accent rules, chips, primary chart color |
| blueDark | 1227AD | 0D2B6E | Secondary emphasis |
| lightBg | E8EAF5 Harmony Lilac | EBF0FD | Tiles, zebra rows, SO WHAT boxes |
| midBg | BDC3F6 | D6E0FA | Total rows, secondary chart color, text on dark backgrounds |
| ink | 282A30 | 1E1E1E | Body text |
| gray | 616366 | 6B7280 | Notes, sources, footers |
| line | D1D5DB | D1D5DB | Hairlines, table borders |
| amber / paleAmber | B45309 / FEF3C7 | same | HONESTY GUARDRAIL boxes, "illustrative" tags (functional color, callouts only) |
| green / paleGreen | 1A7A4A / E7F5EC | same | IMPORTANT boxes, positive marks (functional color, callouts only) |
| red | B91C1C | same | Use sparingly (risk, blocked) |

Font: Titillium Web, Yuno's brand typeface (a Google Font: Google Slides renders it natively; PowerPoint substitutes when it is not installed). Set `YUNO_DECK_FONT=Arial` when the file must open identically everywhere. Charts use the blue scale only.

Logos: the cover carries the `yuno | <merchant logo>` lockup top-left (German's convention), built from local PNGs: `REPO/Yuno Design System/yuno-design-system/assets/yuno-wordmark-white.png` and `REPO/yuno-sales-pitch-maker/public/merchants/<slug>.png` (white-on-transparent). The closing slide repeats the Yuno wordmark. Everywhere else, provider and customer names are text; never fetch or redraw third-party logos. Never combine the Yuno symbol and wordmark.

## Canvas and anatomy

`LAYOUT_WIDE` 13.33 × 7.5 in. Margins 0.6 in. The frame drawn by `slide()`:

| Zone | Position | Style |
|---|---|---|
| Kicker | y 0.42 | 10.5 pt bold, blue, ALL CAPS, letter-spaced ("SECTION · TOPIC") |
| "▲ Illustrative · pending <Merchant> data" tag | top right | 9 pt italic amber; on every modeled slide |
| Action title | y 0.74, up to two lines | 24 pt bold navy |
| Content zone | y 1.75 → 6.55 | one chart / table / diagram / tile row |
| Emphasis element | bottom of content zone | `callout()` (SO WHAT, HONESTY GUARDRAIL, IMPORTANT) or `bar()` (BOTTOM LINE) |
| Footer | y 6.92 | Source line left (8 pt gray), "Yuno × <Merchant> · Confidential" and slide number right |

Type scale: hero numbers 34-44 pt · tile numbers 28-34 · body 11-13 · table 10-11 · notes/sources 8-10. Nothing below 8 pt. If text doesn't fit, cut words or split the slide; don't shrink.

## Layout rules

- One idea per slide; the title states it. If a slide needs two charts, they must make one comparison.
- Vary layouts across the deck: tiles, two-column, table, chart, flow, pillars, numbered list. Three identical layouts in a row reads as a template.
- Charts are native and honest: bars start at zero, percentages share the same axis, one color per series, value labels on, gridlines faint, no legend for a single series. Label modeled numbers with "~".
- Tables: dark header, zebra rows, first column bold, total row tinted. Max ~8 rows on a main slide (20-row market tables belong in the appendix or need 9-10 pt and full height).
- Ratings in comparison tables use ○ ◐ ● text marks, not images.
- Diagrams: rectangles, hairlines and arrows only. Highlight "where Yuno operates" with the blue outline and light fill.
- The cover, section dividers and the closing slide are dark full-bleed (Unity Black); everything else is white.
- Copy: no em-dashes or " - " as punctuation; never "no small feat"; USD only; the merchant's own words where possible.
- Speaker notes hold talk track, caveats to say aloud and items German must confirm. Working notes never go on the slide.

## Helper API (`scripts/yuno_deck.js`)

```js
const Y = require("/Users/germantatis/Desktop/GTMCoding/.claude/skills/yuno-sales-deck/scripts/yuno_deck.js");
const d = Y.createDeck({ merchant: "Roblox" });                       // footer text auto-set
Y.cover(d, { thesis, descriptor, date: "SEP 2026", sources,
             yunoLogo: "<REPO>/Yuno Design System/yuno-design-system/assets/yuno-wordmark-white.png",
             merchantLogo: "<REPO>/yuno-sales-pitch-maker/public/merchants/roblox.png" });   // missing files fall back to text
Y.divider(d, "THE REALITY", "optional sub-line");
const s = Y.slide(d, { kicker, title, source, notes, tag });          // standard frame; returns slide
Y.statTiles(s, [{ value, label, note }], { cols, y, h });             // 2-6 big-number tiles (rows wrap by cols)
Y.twoColumn(s, { header, items:[{ bold, text, chip }] }, {...}, { bottomBar });
Y.table(s, header[], rows[][], { colW, rowH, fontSize, totalRow });   // cells: string or { text, bold, color, fill, align }
Y.flow(s, [{ title, text, tag }]);                                    // tag e.g. "Yuno operates here"
Y.columns(s, [{ header, text, bullets }]);                            // pillars, why-now, live/stays/model
Y.bars(s, [{ name, labels, values }], { x, w, title, pct, stacked }); // native chart, zero-based
Y.waterfall(s, [{ label, value, caption }], { fmt: v => "$"+v+"M" }); // shape-based, editable
Y.phaseBar(s, [{ label, title, text }], { chips: [] });
Y.numbered(s, [{ bold, text }], { footer });
Y.callout(s, "Honesty guardrail", text, { kind: "guardrail" | "sowhat" | "important", x, y, w, h });
Y.bar(s, text, { y, label: "Bottom line" });
Y.ask(d, { title, asks:[{ bold, text }], footer, source });
Y.close(d, { line: "Let's grow together", thesis, contact, yunoLogo });
await Y.save(d, "<REPO>/Deals/Roblox/Yuno_x_Roblox_BusinessCase_Sep2026.pptx");
```

Constants exported: `C` (active colors), `THEMES`, `FONT`, `MX`, `CW`, `CY`, `CH`, `W`, `H`, plus `tx(slide, text, opts)` for free text and `lockup(deck, slide, opts)` for the co-brand lockup. For patterns the helper lacks (country page, markets table with sidebar, floor-to-range bar, build-vs-buy), compose them from `table`, `statTiles`, `callout`, shapes and `tx` inside the content zone, keeping the same tokens. Coordinates beyond the slide are written, not clamped, so check the render.

Country page composition (appendix): `statTiles` with `{ cols: 4, y: 1.7, h: 1.25 }` → three lever boxes via `columns` at y≈3.05, h≈1.35 → `table` for PAYMENT METHOD PRIORITY on the left (w≈7.6) and a small BASE-CASE MODEL table on the right (w≈4.3) at y≈4.55 → `callout` SO WHAT at y≈6.0, h≈0.6. Use 9.5-10 pt in tables here.

## pptxgenjs gotchas

- Colors are hex without `#`. Never share option objects between calls; pptxgenjs mutates them.
- Every text box needs explicit `x, y, w, h` in inches; `fit: "shrink"` is used on titles only, everything else is cut or split, not shrunk.
- Chart values are numeric arrays; labels and values must have the same length.
- `addImage` needs a real file: the helper guards logo paths with `fs.existsSync`, other images must be checked before use.
- `save()` is async: `await` it (wrap the build in `(async () => { ... })()`).
- Titillium Web glyph widths are close to Arial's; if a title wraps to three lines, cut words.

## After building

1. `python3 <SKILL_DIR>/scripts/deck_qa.py deck.pptx --merchant "<Name>" --allow "<their PSPs, named competitors>"` must exit 0; reconcile the money inventory it prints by hand.
2. Visual pass: if `soffice` is on PATH, `soffice --headless --convert-to pdf deck.pptx` and look at every page. Otherwise upload the .pptx to Drive, open as Google Slides, and run `python3 <SKILL_DIR>/scripts/slides_thumbs.py <presentationId> build/thumbs` to pull every slide as PNG. Look for overflow, overlap, clipped text, orphaned words in titles, empty space.
3. Walk `references/qa-checklist.md`.
