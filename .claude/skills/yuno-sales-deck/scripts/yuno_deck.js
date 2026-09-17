/**
 * yuno_deck.js — pptxgenjs helpers for Yuno sales decks.
 *
 * Usage:
 *   const Y = require("/Users/germantatis/Desktop/GTMCoding/.claude/skills/yuno-sales-deck/scripts/yuno_deck.js");
 *   const deck = Y.createDeck({ merchant: "Roblox" });
 *   Y.cover(deck, { thesis: "...", descriptor: "A business case for payments orchestration", date: "SEP 2026",
 *                   yunoLogo: "<REPO>/Yuno Design System/yuno-design-system/assets/yuno-wordmark-white.png",
 *                   merchantLogo: "<REPO>/yuno-sales-pitch-maker/public/merchants/roblox.png" });
 *   const s = Y.slide(deck, { kicker: "WHY WE ARE HERE", title: "...", source: "..." });
 *   Y.statTiles(s, [{ value: "$6.8B", label: "FY2025 bookings", note: "+55% YoY [F]" }, ...]);
 *   await Y.save(deck, "<REPO>/Deals/Roblox/Yuno_x_Roblox_BusinessCase_Sep2026.pptx");
 *
 * Themes: YUNO_DECK_THEME=brand (default, official Yuno palette) | navy (Samuel's original Roblox palette).
 * Font:   YUNO_DECK_FONT=Titillium Web (default, brand typeface) | Arial (opens identically everywhere).
 *
 * Canvas: LAYOUT_WIDE 13.33 x 7.5 in. Content zone: x 0.6..12.73, y 1.75..6.55.
 * Colors are hex WITHOUT '#'. Never share option objects between calls (pptxgenjs mutates them).
 */
const pptxgen = require("pptxgenjs");
const fs = require("fs");

// Token presets. "brand" maps the roles to Yuno's official palette (Brand Guidelines 20.01.2026:
// Yuno Blue 3E4FE0, Harmony Lilac E8EAF5, Unity Black 282A30, extended 1227AD / BDC3F6 / 616366).
// "navy" is Samuel's original Roblox-brief palette. Amber/green/red are functional colors for callout boxes only.
const THEMES = {
  brand: { navy: "282A30", blue: "3E4FE0", blueDark: "1227AD", lightBg: "E8EAF5", midBg: "BDC3F6",
           ink: "282A30", gray: "616366", line: "D1D5DB", white: "FFFFFF",
           green: "1A7A4A", amber: "B45309", red: "B91C1C", paleAmber: "FEF3C7", paleGreen: "E7F5EC" },
  navy:  { navy: "0A1F44", blue: "1A4ED4", blueDark: "0D2B6E", lightBg: "EBF0FD", midBg: "D6E0FA",
           ink: "1E1E1E", gray: "6B7280", line: "D1D5DB", white: "FFFFFF",
           green: "1A7A4A", amber: "B45309", red: "B91C1C", paleAmber: "FEF3C7", paleGreen: "E7F5EC" },
};
const C = THEMES[process.env.YUNO_DECK_THEME] || THEMES.brand;
// Titillium Web is Yuno's brand typeface (Google Font: native in Google Slides; PowerPoint substitutes when it is
// not installed). YUNO_DECK_FONT=Arial gives a file that opens identically everywhere.
const FONT = process.env.YUNO_DECK_FONT || "Titillium Web";
const W = 13.33, H = 7.5, MX = 0.6, CW = W - 2 * MX, CY = 1.75, CH = 4.8;

function createDeck({ merchant, footer, author = "Yuno" }) {
  const pres = new pptxgen();
  pres.layout = "LAYOUT_WIDE";
  pres.author = author;
  pres.title = `Yuno x ${merchant}`;
  return { pres, merchant, footer: footer || `Yuno × ${merchant} · Confidential`, n: 0, C, FONT };
}

function tx(slide, text, o) {
  slide.addText(text, Object.assign({ fontFace: FONT, color: C.ink, margin: 0, isTextBox: true, valign: "top" }, o));
}

/** Width/height ratio read from a PNG's IHDR chunk (no image library needed). */
function pngRatio(path, fallback) {
  try {
    const b = fs.readFileSync(path);
    if (b.toString("ascii", 1, 4) !== "PNG") return fallback;
    const w = b.readUInt32BE(16), hh = b.readUInt32BE(20);
    return hh ? w / hh : fallback;
  } catch (e) { return fallback; }
}

/** `yuno | <merchant>` co-brand lockup (German's cover convention: small, top-left, both logos at the same height).
 *  yunoLogo / merchantLogo are PNG paths; use the white-on-transparent versions on dark backgrounds.
 *  A missing file falls back to the text wordmark so a build never breaks on a logo. */
function lockup(deck, s, { yunoLogo, merchantLogo, x = 0.9, y = 0.55, h = 0.42, dark = true } = {}) {
  const fg = dark ? C.white : C.navy;
  let cx = x;
  if (yunoLogo && fs.existsSync(yunoLogo)) {
    const w = h * pngRatio(yunoLogo, 3.7);
    s.addImage({ path: yunoLogo, x: cx, y, w, h }); cx += w;
  } else {
    tx(s, "yuno", { x: cx, y: y - 0.1, w: 1.1, h: h + 0.2, fontSize: 22, bold: true, color: fg, valign: "middle" }); cx += 0.95;
  }
  if (merchantLogo && fs.existsSync(merchantLogo)) {
    cx += 0.22;
    s.addShape(deck.pres.ShapeType.line, { x: cx, y: y - 0.03, w: 0, h: h + 0.06, line: { color: fg, width: 1 } });
    cx += 0.22;
    const mw = Math.min(h * pngRatio(merchantLogo, 4), 3.2);
    s.addImage({ path: merchantLogo, x: cx, y, w: mw, h });
  }
}

/** Cover: dark hero (the brand cover), lockup top-left, title, thesis, descriptor, confidentiality line.
 *  `title` overrides the default "YUNO × <MERCHANT>". */
function cover(deck, { thesis, descriptor, date, sources, yunoLogo, merchantLogo, title }) {
  const s = deck.pres.addSlide(); deck.n++;
  s.background = { color: C.navy };
  s.addShape(deck.pres.ShapeType.rect, { x: 0, y: 0, w: 0.28, h: H, fill: { color: C.blue }, line: { color: C.blue } });
  lockup(deck, s, { yunoLogo, merchantLogo, x: 0.9, y: 0.55, h: 0.42, dark: true });
  tx(s, title || `YUNO × ${deck.merchant.toUpperCase()}`, { x: 0.9, y: 2.2, w: 11.5, h: 0.9, fontSize: 44, bold: true, color: C.white, charSpacing: 2 });
  if (thesis) tx(s, thesis, { x: 0.9, y: 3.25, w: 11, h: 0.9, fontSize: 24, color: C.white });
  if (descriptor) tx(s, descriptor, { x: 0.9, y: 4.25, w: 11, h: 0.5, fontSize: 16, color: C.midBg });
  tx(s, `CONFIDENTIAL · PREPARED FOR ${deck.merchant.toUpperCase()}${date ? " · " + date : ""}`, { x: 0.9, y: 6.3, w: 11, h: 0.3, fontSize: 10, color: C.midBg, charSpacing: 3 });
  if (sources) tx(s, `Sources: ${sources}`, { x: 0.9, y: 6.75, w: 11.5, h: 0.3, fontSize: 8, color: C.midBg });
  return s;
}

function divider(deck, label, sub) {
  const s = deck.pres.addSlide(); deck.n++;
  s.background = { color: C.navy };
  tx(s, label, { x: 0.9, y: 2.9, w: 11.5, h: 1, fontSize: 40, bold: true, color: C.white, charSpacing: 2 });
  if (sub) tx(s, sub, { x: 0.9, y: 4.0, w: 11.5, h: 0.6, fontSize: 18, color: C.midBg });
  return s;
}

/** Standard content slide frame. Returns the slide; draw the body inside the content zone. */
function slide(deck, { kicker, title, source, notes, tag }) {
  const s = deck.pres.addSlide(); deck.n++;
  s.background = { color: C.white };
  if (kicker) tx(s, kicker.toUpperCase(), { x: MX, y: 0.42, w: CW - 3, h: 0.28, fontSize: 10.5, bold: true, color: C.blue, charSpacing: 3 });
  if (tag) tx(s, `▲ ${tag}`, { x: W - MX - 3.6, y: 0.42, w: 3.6, h: 0.28, fontSize: 9, italic: true, color: C.amber, align: "right" });
  tx(s, title, { x: MX, y: 0.74, w: CW, h: 0.95, fontSize: 24, bold: true, color: C.navy, valign: "top", fit: "shrink" });
  s.addShape(deck.pres.ShapeType.line, { x: MX, y: 6.85, w: CW, h: 0, line: { color: C.line, width: 0.75 } });
  if (source) tx(s, `Source: ${source}`, { x: MX, y: 6.92, w: 8.6, h: 0.4, fontSize: 8, color: C.gray });
  tx(s, deck.footer, { x: W - MX - 4.2, y: 6.92, w: 3.6, h: 0.25, fontSize: 8, color: C.gray, align: "right" });
  tx(s, String(deck.n).padStart(2, "0"), { x: W - MX - 0.5, y: 6.92, w: 0.5, h: 0.25, fontSize: 8, bold: true, color: C.navy, align: "right" });
  if (notes) s.addNotes(notes);
  s._deck = deck;
  return s;
}

/** Row of 2-6 big-number tiles. tiles: [{value,label,note}] */
function statTiles(s, tiles, { y = CY, h = 1.9, cols } = {}) {
  const n = cols || tiles.length, gap = 0.22, w = (CW - gap * (n - 1)) / n;
  tiles.forEach((t, i) => {
    const x = MX + (i % n) * (w + gap), yy = y + Math.floor(i / n) * (h + gap);
    s.addShape(s._deck.pres.ShapeType.rect, { x, y: yy, w, h, fill: { color: C.lightBg }, line: { color: C.lightBg } });
    tx(s, t.value, { x: x + 0.2, y: yy + 0.18, w: w - 0.4, h: 0.75, fontSize: n > 4 ? 28 : 34, bold: true, color: C.blue, fit: "shrink" });
    tx(s, t.label, { x: x + 0.2, y: yy + 0.98, w: w - 0.4, h: 0.4, fontSize: 12, bold: true, color: C.navy });
    if (t.note) tx(s, t.note, { x: x + 0.2, y: yy + 1.36, w: w - 0.4, h: 0.45, fontSize: 10, color: C.gray });
  });
}

/** Two columns of items. col: {header, items:[{bold,text,chip}]} */
function twoColumn(s, left, right, { y = CY, h = 4.2, bottomBar } = {}) {
  const gap = 0.4, w = (CW - gap) / 2;
  [left, right].forEach((col, ci) => {
    const x = MX + ci * (w + gap);
    tx(s, col.header.toUpperCase(), { x, y, w, h: 0.3, fontSize: 11, bold: true, color: ci ? C.blue : C.navy, charSpacing: 2 });
    s.addShape(s._deck.pres.ShapeType.line, { x, y: y + 0.34, w, h: 0, line: { color: ci ? C.blue : C.navy, width: 1.5 } });
    const ih = (h - 0.5) / col.items.length;
    col.items.forEach((it, i) => {
      const yy = y + 0.5 + i * ih;
      const runs = [{ text: it.bold, options: { bold: true, color: C.navy, fontSize: 13, breakLine: true } }];
      if (it.text) runs.push({ text: it.text, options: { color: C.ink, fontSize: 11 } });
      tx(s, runs, { x, y: yy, w: it.chip ? w - 2.2 : w, h: ih - 0.1 });
      if (it.chip) {
        s.addShape(s._deck.pres.ShapeType.roundRect, { x: x + w - 2.05, y: yy + 0.05, w: 2.05, h: 0.42, rectRadius: 0.08, fill: { color: C.blue }, line: { color: C.blue } });
        tx(s, it.chip, { x: x + w - 2.05, y: yy + 0.05, w: 2.05, h: 0.42, fontSize: 10, bold: true, color: C.white, align: "center", valign: "middle" });
      }
    });
  });
  if (bottomBar) bar(s, bottomBar, { y: y + h + 0.1 });
}

/** Full-width emphasis bar (BOTTOM LINE / footer thesis). */
function bar(s, text, { y = 6.05, label } = {}) {
  s.addShape(s._deck.pres.ShapeType.rect, { x: MX, y, w: CW, h: 0.62, fill: { color: C.navy }, line: { color: C.navy } });
  const runs = label ? [{ text: label.toUpperCase() + "   ", options: { bold: true, color: C.midBg, fontSize: 10, charSpacing: 2 } }, { text, options: { color: C.white, fontSize: 12 } }]
    : [{ text, options: { color: C.white, fontSize: 12, bold: true } }];
  tx(s, runs, { x: MX + 0.25, y, w: CW - 0.5, h: 0.62, valign: "middle" });
}

/** Callout box. kind: "sowhat" | "guardrail" | "important" */
function callout(s, label, text, { x = MX, y = 5.35, w = CW, h = 0.95, kind = "sowhat" } = {}) {
  const fill = kind === "guardrail" ? C.paleAmber : kind === "important" ? C.paleGreen : C.lightBg;
  const lc = kind === "guardrail" ? C.amber : kind === "important" ? C.green : C.blue;
  s.addShape(s._deck.pres.ShapeType.rect, { x, y, w, h, fill: { color: fill }, line: { color: fill } });
  s.addShape(s._deck.pres.ShapeType.rect, { x, y, w: 0.07, h, fill: { color: lc }, line: { color: lc } });
  tx(s, [{ text: label.toUpperCase(), options: { bold: true, color: lc, fontSize: 10, charSpacing: 2, breakLine: true } }, { text, options: { color: C.ink, fontSize: 11 } }],
    { x: x + 0.25, y: y + 0.1, w: w - 0.4, h: h - 0.2 });
}

/** Styled table. header: string[]; rows: (string|{text,bold,color,fill,align})[][] */
function table(s, header, rows, { x = MX, y = CY, w = CW, colW, fontSize = 10.5, rowH = 0.42, zebra = true, totalRow = false } = {}) {
  const hdr = header.map((t) => ({ text: t.toUpperCase(), options: { bold: true, color: C.white, fill: { color: C.navy }, fontSize: fontSize - 1, fontFace: FONT, valign: "middle", charSpacing: 1 } }));
  const body = rows.map((r, ri) => r.map((c, ci) => {
    const o = typeof c === "string" ? { text: c } : c;
    const last = totalRow && ri === rows.length - 1;
    return { text: o.text, options: { fontFace: FONT, fontSize, valign: "middle", align: o.align || (ci === 0 ? "left" : "left"),
      bold: last || !!o.bold || ci === 0, color: o.color || (ci === 0 ? C.navy : C.ink),
      fill: { color: o.fill || (last ? C.midBg : zebra && ri % 2 ? C.lightBg : C.white) } } };
  }));
  s.addTable([hdr, ...body], { x, y, w, colW, rowH, border: { type: "solid", color: C.line, pt: 0.5 }, margin: [0.04, 0.1, 0.04, 0.1] });
}

/** Left-to-right flow of nodes. nodes: [{title,text,tag}] (tag e.g. "YUNO OPERATES HERE") */
function flow(s, nodes, { y = 2.3, h = 2.4 } = {}) {
  const gap = 0.6, w = (CW - gap * (nodes.length - 1)) / nodes.length;
  nodes.forEach((nd, i) => {
    const x = MX + i * (w + gap);
    if (nd.tag) tx(s, nd.tag.toUpperCase(), { x, y: y - 0.4, w, h: 0.3, fontSize: 9.5, bold: true, color: C.blue, charSpacing: 2, align: "center" });
    s.addShape(s._deck.pres.ShapeType.rect, { x, y, w, h, fill: { color: nd.tag ? C.lightBg : C.white }, line: { color: nd.tag ? C.blue : C.line, width: nd.tag ? 1.5 : 1 } });
    tx(s, nd.title, { x: x + 0.2, y: y + 0.2, w: w - 0.4, h: 0.5, fontSize: 15, bold: true, color: C.navy });
    tx(s, nd.text, { x: x + 0.2, y: y + 0.8, w: w - 0.4, h: h - 1.0, fontSize: 11, color: C.ink });
    if (i < nodes.length - 1) tx(s, "→", { x: x + w, y: y + h / 2 - 0.3, w: gap, h: 0.6, fontSize: 24, color: C.blue, align: "center", valign: "middle" });
  });
}

/** Horizontal phase bar. phases: [{label,title,text}] */
function phaseBar(s, phases, { y = 2.0, chips } = {}) {
  const gap = 0.12, w = (CW - gap * (phases.length - 1)) / phases.length;
  phases.forEach((p, i) => {
    const x = MX + i * (w + gap);
    s.addShape(s._deck.pres.ShapeType.chevron || s._deck.pres.ShapeType.rect, { x, y, w, h: 0.6, fill: { color: i === 0 ? C.navy : C.blue }, line: { color: C.white } });
    tx(s, p.label.toUpperCase(), { x: x + 0.3, y, w: w - 0.5, h: 0.6, fontSize: 10, bold: true, color: C.white, valign: "middle", charSpacing: 1 });
    tx(s, p.title, { x, y: y + 0.8, w: w - 0.1, h: 0.4, fontSize: 13, bold: true, color: C.navy });
    tx(s, p.text, { x, y: y + 1.25, w: w - 0.15, h: 1.7, fontSize: 10.5, color: C.ink });
  });
  if (chips) chips.forEach((c, i) => {
    const cw = (CW - 0.2 * (chips.length - 1)) / chips.length, x = MX + i * (cw + 0.2);
    s.addShape(s._deck.pres.ShapeType.roundRect, { x, y: 5.3, w: cw, h: 0.55, rectRadius: 0.1, fill: { color: C.lightBg }, line: { color: C.blue } });
    tx(s, c, { x, y: 5.3, w: cw, h: 0.55, fontSize: 11, bold: true, color: C.navy, align: "center", valign: "middle" });
  });
}

/** Numbered list with big numerals (Where we're different / The Ask). items: [{bold,text}] */
function numbered(s, items, { y = CY, h = 4.4, footer } = {}) {
  const ih = h / items.length;
  items.forEach((it, i) => {
    const yy = y + i * ih;
    tx(s, String(i + 1), { x: MX, y: yy, w: 0.8, h: ih - 0.1, fontSize: 36, bold: true, color: C.blue });
    tx(s, [{ text: it.bold, options: { bold: true, color: C.navy, fontSize: 15, breakLine: !!it.text } }].concat(it.text ? [{ text: it.text, options: { color: C.ink, fontSize: 12 } }] : []),
      { x: MX + 0.95, y: yy + 0.05, w: CW - 1.0, h: ih - 0.15 });
  });
  if (footer) tx(s, footer, { x: MX, y: y + h + 0.05, w: CW, h: 0.35, fontSize: 12, italic: true, color: C.gray });
}

/** Three (or N) columns of cards. cols: [{header,text,bullets}] */
function columns(s, cols, { y = CY, h = 3.6 } = {}) {
  const gap = 0.3, w = (CW - gap * (cols.length - 1)) / cols.length;
  cols.forEach((c, i) => {
    const x = MX + i * (w + gap);
    s.addShape(s._deck.pres.ShapeType.rect, { x, y, w, h, fill: { color: C.white }, line: { color: C.line } });
    s.addShape(s._deck.pres.ShapeType.rect, { x, y, w, h: 0.08, fill: { color: C.blue }, line: { color: C.blue } });
    tx(s, c.header.toUpperCase(), { x: x + 0.2, y: y + 0.25, w: w - 0.4, h: 0.55, fontSize: 11.5, bold: true, color: C.blue, charSpacing: 1.5 });
    const runs = [];
    if (c.text) runs.push({ text: c.text, options: { fontSize: 11.5, color: C.ink, breakLine: !!(c.bullets && c.bullets.length) } });
    (c.bullets || []).forEach((b, bi) => runs.push({ text: b, options: { bullet: true, fontSize: 11, color: C.ink, paraSpaceAfter: 5, breakLine: bi < c.bullets.length - 1 } }));
    tx(s, runs, { x: x + 0.2, y: y + 0.85, w: w - 0.4, h: h - 1.0 });
  });
}

/** Native bar chart. series: [{name, labels, values}] */
function bars(s, series, { x = MX, y = CY, w = 6, h = 3.6, title, stacked = false, pct = false, colors } = {}) {
  s.addChart(s._deck.pres.charts.BAR, series, {
    x, y, w, h, barDir: "col", barGrouping: stacked ? "stacked" : "clustered",
    chartColors: colors || (series.length === 1 ? [C.blue] : [C.blue, C.navy, C.midBg]),
    valAxisMinVal: 0, ...(pct ? { valAxisMaxVal: 100 } : {}),
    showTitle: !!title, title, titleFontSize: 11, titleColor: C.navy, titleFontFace: FONT,
    showValue: true, dataLabelPosition: stacked ? "ctr" : "outEnd", dataLabelFontSize: 10, dataLabelColor: stacked ? C.white : C.navy,
    dataLabelFormatCode: pct ? '0"%"' : "General",
    catAxisLabelColor: C.gray, valAxisLabelColor: C.gray, catAxisLabelFontSize: 10, valAxisLabelFontSize: 9, valAxisHidden: false,
    valGridLine: { color: "EEEEEE", size: 0.5 }, catGridLine: { style: "none" }, showLegend: series.length > 1, legendPos: "b", legendFontSize: 10,
  });
}

/** Waterfall drawn with shapes (fully editable, labeled). steps: [{label, value, caption}] ; last bar = total. fmt: v => "$14M" */
function waterfall(s, steps, { x = MX, y = CY, w = CW, h = 3.3, fmt = (v) => String(v), totalLabel = "Total" } = {}) {
  const total = steps.reduce((a, t) => a + t.value, 0), n = steps.length + 1, gap = 0.35;
  const bw = (w - gap * (n - 1)) / n, plotH = h - 1.0, scale = plotH / total, baseY = y + plotH + 0.35;
  let run = 0;
  steps.concat([{ label: totalLabel, value: total, isTotal: true }]).forEach((t, i) => {
    const bx = x + i * (bw + gap), bh = Math.max(t.value * scale, 0.04);
    const by = t.isTotal ? baseY - bh : baseY - (run + t.value) * scale;
    s.addShape(s._deck.pres.ShapeType.rect, { x: bx, y: by, w: bw, h: bh, fill: { color: t.isTotal ? C.navy : C.blue }, line: { color: t.isTotal ? C.navy : C.blue } });
    tx(s, (t.isTotal ? "" : "+") + fmt(t.value), { x: bx, y: by - 0.34, w: bw, h: 0.3, fontSize: 13, bold: true, color: C.navy, align: "center" });
    tx(s, [{ text: t.label, options: { bold: true, fontSize: 11, color: C.navy, breakLine: !!t.caption } }].concat(t.caption ? [{ text: t.caption, options: { fontSize: 9.5, color: C.gray } }] : []),
      { x: bx - 0.1, y: baseY + 0.08, w: bw + 0.2, h: 0.6, align: "center" });
    if (!t.isTotal) { run += t.value; s.addShape(s._deck.pres.ShapeType.line, { x: bx + bw, y: baseY - run * scale, w: gap, h: 0, line: { color: C.gray, width: 0.75, dashType: "dash" } }); }
  });
  s.addShape(s._deck.pres.ShapeType.line, { x, y: baseY, w, h: 0, line: { color: C.line, width: 1 } });
}

/** The Ask: numbered asks + proposed dates footer. */
function ask(deck, { kicker = "THE ASK", title, asks, footer = "Proposed dates: ____________", source }) {
  const s = slide(deck, { kicker, title, source });
  numbered(s, asks, { h: 4.2, footer });
  return s;
}

/** Closing slide. */
function close(deck, { line = "Let's grow together", thesis, contact, yunoLogo }) {
  const s = deck.pres.addSlide(); deck.n++;
  s.background = { color: C.navy };
  lockup(deck, s, { yunoLogo, x: 0.9, y: 0.6, h: 0.42, dark: true });
  tx(s, line, { x: 0.9, y: 2.8, w: 11.5, h: 1, fontSize: 40, bold: true, color: C.white });
  if (thesis) tx(s, thesis, { x: 0.9, y: 3.9, w: 11.5, h: 0.6, fontSize: 18, color: C.midBg });
  if (contact) tx(s, contact, { x: 0.9, y: 6.4, w: 11.5, h: 0.4, fontSize: 12, color: C.midBg });
  return s;
}

async function save(deck, path) { await deck.pres.writeFile({ fileName: path }); return path; }

module.exports = { C, THEMES, FONT, W, H, MX, CW, CY, CH, createDeck, tx, lockup, cover, divider, slide, statTiles, twoColumn, bar, callout, table, flow, phaseBar, numbered, columns, bars, waterfall, ask, close, save };
