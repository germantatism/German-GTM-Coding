/**
 * build_deck.js: Yuno Subscriptions x The New York Times, 12-slide cut of Magdalena Torrealba's
 * 19-slide "The New York Times - Subscriptions Deck" (Google Slides 1eFQx1WE..., 18 Sep 2026).
 * Storyline: their stack today (R) -> the engine (B) -> how we help and what is live (B/P) -> next step.
 * Run: node build_deck.js [out.pptx]
 */
const fs = require("fs");
const Y = require("/Users/germantatis/Desktop/GTMCoding/.claude/skills/yuno-sales-deck/scripts/yuno_deck.js");
const REPO = "/Users/germantatis/Desktop/GTMCoding";
const OUT = process.argv[2] || `${REPO}/Deals/NYT/Yuno_x_NYT_Subscriptions_Sep2026.pptx`;
const LOGO_Y = `${REPO}/Yuno Design System/yuno-design-system/assets/yuno-wordmark-white.png`;
const LOGO_M = fs.existsSync(`${REPO}/Deals/NYT/build/nyt-wordmark-white.png`) ? `${REPO}/Deals/NYT/build/nyt-wordmark-white.png` : `${REPO}/Deals/NYT/build/nyt-logo-white.png`;
const { C, MX, CW, tx } = Y;

// ---------- small drawing helpers (rectangles, hairlines, arrows only) ----------
function rect(s, d, { x, y, w, h, fill = C.white, line = C.line, lw = 1, radius }) {
  const o = { x, y, w, h, fill: { color: fill }, line: { color: line, width: lw } };
  if (radius) { o.rectRadius = radius; s.addShape(d.pres.ShapeType.roundRect, o); } else s.addShape(d.pres.ShapeType.rect, o);
}
function layer(s, d, { x, y, w, h, head, body, note, accent = false, headColor }) {
  rect(s, d, { x, y, w, h, fill: accent ? C.lightBg : C.white, line: accent ? C.blue : C.line, lw: accent ? 1.5 : 1 });
  tx(s, head, { x: x + 0.2, y: y + 0.1, w: w - 0.4, h: 0.28, fontSize: 10, bold: true, color: headColor || C.blue, charSpacing: 2 });
  tx(s, body, { x: x + 0.2, y: y + 0.4, w: w - 0.4, h: 0.4, fontSize: 12.5, bold: true, color: C.navy });
  if (note) tx(s, note, { x: x + 0.2, y: y + h - 0.36, w: w - 0.4, h: 0.3, fontSize: 9.5, italic: true, color: C.gray });
}
function vlink(s, d, { x, y, h = 0.3, text }) {
  s.addShape(d.pres.ShapeType.line, { x, y, w: 0, h, line: { color: C.blue, width: 1.25, endArrowType: "triangle" } });
  if (text) tx(s, text.toUpperCase(), { x: x + 0.15, y: y + h / 2 - 0.13, w: 4, h: 0.26, fontSize: 9, bold: true, color: C.gray, charSpacing: 1.5, valign: "middle" });
}
function hlink(s, d, { x, y, w = 0.45, text }) {
  s.addShape(d.pres.ShapeType.line, { x, y, w, h: 0, line: { color: C.blue, width: 1.25, endArrowType: "triangle" } });
  if (text) tx(s, text.toUpperCase(), { x: x - 0.4, y: y - 0.32, w: w + 0.8, h: 0.26, fontSize: 8.5, bold: true, color: C.gray, charSpacing: 1, align: "center" });
}
function takeaways(s, { x, y, w, items, gapY = 0.6, fontSize = 12 }) {
  items.forEach((t, i) => {
    tx(s, "↗", { x, y: y + i * gapY, w: 0.35, h: 0.4, fontSize: 16, bold: true, color: C.blue });
    tx(s, t, { x: x + 0.38, y: y + i * gapY + 0.04, w: w - 0.4, h: gapY - 0.05, fontSize, bold: true, color: C.navy });
  });
}
function node(s, d, { x, y, w, h, head, body, sub, accent = false, fill }) {
  rect(s, d, { x, y, w, h, fill: fill || (accent ? C.lightBg : C.white), line: accent ? C.blue : C.line, lw: accent ? 1.5 : 1 });
  tx(s, head, { x: x + 0.15, y: y + 0.1, w: w - 0.3, h: 0.28, fontSize: 9.5, bold: true, color: C.blue, charSpacing: 1.5 });
  tx(s, body, { x: x + 0.15, y: y + 0.38, w: w - 0.3, h: 0.4, fontSize: 12, bold: true, color: C.navy });
  if (sub) tx(s, sub, { x: x + 0.15, y: y + 0.76, w: w - 0.3, h: h - 0.82, fontSize: 9.5, color: C.ink });
}
function chip(s, d, { x, y, w = 1.6, h = 0.36, text, dark = false }) {
  rect(s, d, { x, y, w, h, fill: dark ? C.navy : C.white, line: dark ? C.navy : C.blue, lw: 1, radius: 0.08 });
  tx(s, text, { x, y, w, h, fontSize: 10, bold: true, color: dark ? C.white : C.navy, align: "center", valign: "middle" });
}

(async () => {
  const d = Y.createDeck({ merchant: "The New York Times" });

  // 01 COVER
  Y.cover(d, {
    title: "YUNO SUBSCRIPTIONS",
    thesis: "The New York Times: your stack today, our engine, and a second path for every renewal",
    descriptor: "Where NYT billing sits today · the Yuno Subscriptions engine · what is live and a first cycle together",
    date: "SEP 2026",
    sources: "The New York Times Company Q2 2026 results and FY2025 Form 10-K · help.nytimes.com · docs.y.uno · Yuno Control Center",
    yunoLogo: LOGO_Y, merchantLogo: LOGO_M,
  });

  // 02 THE NUMBERS (R)
  let s = Y.slide(d, {
    kicker: "WHERE NYT BILLING SITS TODAY",
    title: "The renewal happens 12.8 million times, every four weeks",
    source: "The New York Times Company Q2 2026 results, 5 Aug 2026 [F] · FY2025 Form 10-K, risk factors and MD&A [F] · help.nytimes.com, Understanding Your Bill [F] · nytimes.com subscription pricing, Sep 2026 [F]",
    notes: "Open with their own numbers. 12.8 million digital-only subscribers, billed in advance every four weeks, so about 13 renewals a year each. A quarter of the base is outside the US. The 10-K itself names the end of promotional pricing and card replacement as churn factors, and card reissuance as a payment risk. Acquisition is one payment; everything after it is a renewal.",
  });
  Y.statTiles(s, [
    { value: "12.80M", label: "Digital-only subscribers", note: "30 June 2026, Q2 2026 results [F]" },
    { value: "~13 cycles", label: "Renewals a year, per subscriber", note: "Billed in advance every four weeks [F]" },
    { value: "26%", label: "Of digital-only subscriptions outside the US", note: "234 countries and territories, FY2025 10-K [F]" },
    { value: "$4 → $25", label: "The promotional step up", note: "All Access, every four weeks: intro price, then regular price [F]" },
  ], { y: 1.8, h: 1.85 });
  rect(s, d, { x: MX, y: 3.9, w: CW, h: 1.6, fill: C.lightBg, line: C.lightBg });
  rect(s, d, { x: MX, y: 3.9, w: 0.07, h: 1.6, fill: C.blue, line: C.blue });
  tx(s, [
    { text: "WHAT YOUR 10-K SAYS ABOUT THE RENEWAL", options: { bold: true, color: C.blue, fontSize: 10, charSpacing: 2, breakLine: true } },
    { text: "Churn factors: ", options: { bold: true, color: C.navy, fontSize: 11.5 } },
    { text: "“the end of a subscriber’s promotional pricing (which is an important aspect of our strategy)” and “the expiration or replacement of subscribers’ credit cards”.", options: { color: C.ink, fontSize: 11.5, breakLine: true } },
    { text: "Payment risk: ", options: { bold: true, color: C.navy, fontSize: 11.5 } },
    { text: "“material changes in the payment ecosystem such as large reissuances of payment cards by credit card issuers”.", options: { color: C.ink, fontSize: 11.5 } },
  ], { x: MX + 0.3, y: 4.0, w: CW - 0.6, h: 1.4, valign: "top", paraSpaceAfter: 4 });
  Y.bar(s, "Acquisition is one payment. Everything after it is a renewal.", { y: 5.75, label: "Bottom line" });

  // 03 YOUR STACK TODAY (R)
  s = Y.slide(d, {
    kicker: "WHERE NYT BILLING SITS TODAY · YOUR STACK",
    title: "Your stack today: two systems, and one path for every renewal",
    source: "NYTimes Terms of Sale, effective 9 Mar 2026 [F] · Yuno business case for The New York Times, Feb 2026 [Y]",
    notes: "Walk the layers top down. The subscription engine decides what to charge and when; Spreedly vaults and routes; Stripe is the one gateway connected. The Athletic, India and the app stores sit beside it. The point is structural: the engine and the orchestrator are two systems, and the retry has one place to go. Say it once, do not argue vendors.",
  });
  const LX = MX, LW = 7.3;
  layer(s, d, { x: LX, y: 1.85, w: LW, h: 1.0, head: "YOUR SUBSCRIPTION ENGINE", body: "plans · promotional phases · billing dates · retry rules · past due · entitlement", note: "wherever it runs, it is a separate system from the orchestrator" });
  vlink(s, d, { x: LX + 0.6, y: 2.85, h: 0.32, text: "hands over a charge" });
  layer(s, d, { x: LX, y: 3.17, w: LW, h: 0.95, head: "ORCHESTRATION · SPREEDLY", body: "vaults the credential · routes the charge to a gateway · reports the result", note: "the orchestrator is in place" });
  vlink(s, d, { x: LX + 0.6, y: 4.12, h: 0.32, text: "one gateway connected" });
  layer(s, d, { x: LX, y: 4.44, w: LW, h: 0.9, head: "PROCESSING", body: "Stripe", note: "the retry has one place to go" });
  const RX = 8.35, RW = 12.73 - 8.35;
  takeaways(s, { x: RX, y: 1.85, w: RW, items: ["The orchestrator is in place.", "The engine is a separate system.", "The retry has one place to go."], gapY: 0.55 });
  tx(s, "ALSO IN THE STACK", { x: RX, y: 3.6, w: RW, h: 0.26, fontSize: 9.5, bold: true, color: C.gray, charSpacing: 2 });
  [["THE ATHLETIC", "Stripe and Braintree, billed and canceled separately"], ["INDIA", "BillDesk as third party processor"], ["APP STORES", "Apple and Google collect the fees"]].forEach(([h, t], i) => {
    const yy = 3.9 + i * 0.5;
    rect(s, d, { x: RX, y: yy, w: RW, h: 0.44, fill: C.white, line: C.line });
    tx(s, [{ text: h + "  ", options: { bold: true, color: C.blue, fontSize: 9.5, charSpacing: 1 } }, { text: t, options: { color: C.ink, fontSize: 10 } }], { x: RX + 0.15, y: yy, w: RW - 0.3, h: 0.44, valign: "middle" });
  });
  Y.bar(s, "Two systems, one path. Nothing here can route a declined renewal somewhere else.", { y: 5.75, label: "Bottom line" });

  // 04 WHAT THE SPLIT COSTS (R)
  s = Y.slide(d, {
    kicker: "WHERE NYT BILLING SITS TODAY · THE COST",
    title: "What that split costs at renewal: three failures a second path would catch",
    source: "FY2025 Form 10-K, risk factors [F] · Q2 2026 results [F] · nytimes.com pricing, Sep 2026 [F] · Yuno checkout review, Feb 2026 [Y]",
    notes: "Three concrete failure modes. One: a decline is retried on the same path with the same odds. Two: the step up from $4 to $25 is a fresh issuer decision, tested on one path. Three: reissued cards (their 10-K names large reissuances as a payment risk) and local rails such as SEPA and UPI are simply not in the renewal path. Close: a better engine beside the same orchestrator does not fix this; one layer does.",
  });
  Y.columns(s, [
    { header: "01 · Retried where it declined", text: "Same routing, same acquirer, same odds.", bullets: ["The engine can only ask again", "The orchestrator can only send it back to the same place"] },
    { header: "02 · Step ups tested on one path", text: "Cycle 12 at $4, cycle 13 at $25.", bullets: ["A new decision for the issuer", "One path to clear it"] },
    { header: "03 · Reissued cards and local rails", text: "Your 10-K names large reissuances of payment cards among payment risks.", bullets: ["Reissued cards: no second path", "SEPA, UPI: not in the renewal path"] },
  ], { y: 1.85, h: 2.6 });
  // mini flow: declined -> ask again -> declined
  const fw = 3.4, fg = 0.55, fy = 4.7, fh = 0.75;
  [["STRIPE", "Declined"], ["THE ENGINE", "Asks again, same path"], ["STRIPE", "Declined again"]].forEach(([h, b], i) => {
    const x = MX + i * (fw + fg);
    rect(s, d, { x, y: fy, w: fw, h: fh, fill: i === 1 ? C.white : C.lightBg, line: i === 1 ? C.line : C.blue, lw: i === 1 ? 1 : 1.5 });
    tx(s, [{ text: h + "   ", options: { bold: true, color: C.blue, fontSize: 9.5, charSpacing: 1.5 } }, { text: b, options: { bold: true, color: C.navy, fontSize: 12 } }], { x: x + 0.2, y: fy, w: fw - 0.4, h: fh, valign: "middle" });
    if (i < 2) hlink(s, d, { x: x + fw + 0.05, y: fy + fh / 2, w: fg - 0.1 });
  });
  tx(s, "$4 → $25 at cycle 13 · reissued cards · SEPA · UPI: none of these get a second path", { x: MX + 2 * (fw + fg) + fw + 0.1, y: fy, w: CW - 3 * fw - 2 * fg - 0.1, h: fh, fontSize: 9.5, italic: true, color: C.gray, valign: "middle" });
  Y.bar(s, "A better engine beside the same orchestrator does not fix this. One layer does.", { y: 5.75, label: "Bottom line" });

  // 05 THE ENGINE · THE LAYERS (B)
  s = Y.slide(d, {
    kicker: "THE ENGINE · THE LAYERS",
    title: "A subscription engine inside the payments layer, not a silo beside it",
    source: "docs.y.uno, Subscriptions [Y] · Yuno Subscriptions internal launch deck, Sep 2026 [Y]",
    notes: "Same picture as slide 3, with the engine moved inside the payments layer. Your platform stays the system of record. One Yuno integration. The engine creates every cycle charge as a Yuno payment, so every renewal inherits routing, fallback, the vault and retries on another provider. One plan definition, every provider. You stay in front of your subscriber.",
  });
  layer(s, d, { x: LX, y: 1.85, w: LW, h: 0.9, head: "THE NEW YORK TIMES SUBSCRIPTION PLATFORM", body: "your system of record: plans · entitlement · account · customer comms" });
  vlink(s, d, { x: LX + 0.6, y: 2.75, h: 0.32, text: "one Yuno integration" });
  layer(s, d, { x: LX, y: 3.07, w: LW, h: 0.95, head: "YUNO SUBSCRIPTIONS ENGINE", body: "plan → subscription → charge per cycle · smart retries · plan changes · webhooks", accent: true });
  vlink(s, d, { x: LX + 0.6, y: 4.02, h: 0.32, text: "configures · every cycle charge is a Yuno payment" });
  layer(s, d, { x: LX, y: 4.34, w: LW, h: 0.95, head: "MULTI PROVIDER ROUTING", body: "routing · fallback · vaulted tokens · retries on another provider", accent: true });
  ["Stripe", "Second acquirer", "Local rails"].forEach((t, i) => chip(s, d, { x: LX + i * 2.5, y: 5.42, w: 2.3, h: 0.36, text: t }));
  takeaways(s, { x: RX, y: 1.85, w: RW, items: ["The engine sits inside the payments layer.", "So every renewal inherits routing, fallback and the vault.", "One plan definition, every provider.", "You stay in front of your subscriber."], gapY: 0.78 });
  Y.bar(s, "An engine beside an orchestrator retries where it declined. Here the retry is a routed charge.", { y: 5.95, label: "Bottom line" });

  // 06 IN THE DASHBOARD (B)
  s = Y.slide(d, {
    kicker: "THE ENGINE · IN THE DASHBOARD",
    title: "NYT’s plans, configured in the Yuno dashboard by your billing team",
    source: "nytimes.com and NYT help center pricing, Sep 2026 [F] · Yuno dashboard, Subscriptions module [Y]",
    tag: "Illustrative mockup · test mode",
    notes: "This is a mockup, say so. Every NYT plan becomes a Yuno plan: All Access at $25 every four weeks with country pricing, the family plan, Games, The Athletic on its own cadence. Billing teams run plans and subscriptions from the dashboard; the API mirrors it. One view per plan: subscribers, cycle, countries, analytics one tab away.",
  });
  const DX = MX, DY = 1.8, DW = 8.4, DH = 3.95, SBW = 1.75;
  rect(s, d, { x: DX, y: DY, w: DW, h: DH, fill: C.white, line: C.line });
  rect(s, d, { x: DX, y: DY, w: SBW, h: DH, fill: C.lightBg, line: C.lightBg });
  tx(s, "yuno", { x: DX + 0.2, y: DY + 0.12, w: 1.2, h: 0.3, fontSize: 13, bold: true, color: C.navy });
  const sb = ["Home", "Insights", "Operations", "Reconciliation", "Costs", "Marketplace"];
  sb.forEach((t, i) => tx(s, t, { x: DX + 0.2, y: DY + 0.55 + i * 0.27, w: SBW - 0.3, h: 0.25, fontSize: 9, color: C.ink }));
  tx(s, "SOLUTIONS", { x: DX + 0.2, y: DY + 2.25, w: SBW - 0.3, h: 0.22, fontSize: 7.5, bold: true, color: C.gray, charSpacing: 1.5 });
  tx(s, "Subscriptions", { x: DX + 0.2, y: DY + 2.48, w: SBW - 0.3, h: 0.25, fontSize: 9, bold: true, color: C.navy });
  ["Analytics", "Plans", "Subscriptions", "Meters", "Payment links"].forEach((t, i) => {
    const on = t === "Plans";
    if (on) rect(s, d, { x: DX + 0.3, y: DY + 2.75 + i * 0.23, w: SBW - 0.45, h: 0.22, fill: C.white, line: C.white, radius: 0.04 });
    tx(s, t, { x: DX + 0.38, y: DY + 2.75 + i * 0.23, w: SBW - 0.5, h: 0.22, fontSize: 8.5, bold: on, color: on ? C.blue : C.ink, valign: "middle" });
  });
  tx(s, "Plans", { x: DX + SBW + 0.25, y: DY + 0.15, w: 2, h: 0.32, fontSize: 13, bold: true, color: C.navy });
  tx(s, "Test mode · On", { x: DX + SBW + 1.2, y: DY + 0.18, w: 2, h: 0.28, fontSize: 8.5, color: C.gray, valign: "middle" });
  chip(s, d, { x: DX + DW - 1.35, y: DY + 0.15, w: 1.15, h: 0.3, text: "Create plan", dark: true });
  const plans = [
    ["All Access", "$25 / 4 weeks", "Country pricing", "Every 4 weeks", "All"],
    ["All Access Family", "$30 / 4 weeks", "Up to 4 people", "Every 4 weeks", "All"],
    ["Games", "$6 / 4 weeks", "Single price", "Every 4 weeks", "All"],
    ["The Athletic", "$71.99 / year", "Single price", "Yearly", "All"],
  ];
  const cw = (DW - SBW - 0.25 * 3) / 2, ch = 1.45;
  plans.forEach((p, i) => {
    const x = DX + SBW + 0.25 + (i % 2) * (cw + 0.25), y = DY + 0.6 + Math.floor(i / 2) * (ch + 0.2);
    rect(s, d, { x, y, w: cw, h: ch, fill: C.white, line: C.line, radius: 0.06 });
    tx(s, p[0], { x: x + 0.15, y: y + 0.1, w: cw - 1.1, h: 0.28, fontSize: 11, bold: true, color: C.navy });
    tx(s, "● Active", { x: x + cw - 0.95, y: y + 0.12, w: 0.85, h: 0.24, fontSize: 8, bold: true, color: C.green, align: "right" });
    tx(s, p[1], { x: x + 0.15, y: y + 0.4, w: cw - 0.3, h: 0.34, fontSize: 14, bold: true, color: C.blue });
    tx(s, p[2], { x: x + 0.15, y: y + 0.74, w: cw - 0.3, h: 0.22, fontSize: 8.5, color: C.gray });
    tx(s, [{ text: "Subscribers  ", options: { color: C.gray, fontSize: 8 } }, { text: "0", options: { color: C.navy, fontSize: 8, bold: true } },
           { text: "     Billing  ", options: { color: C.gray, fontSize: 8 } }, { text: p[3], options: { color: C.navy, fontSize: 8, bold: true } },
           { text: "     Countries  ", options: { color: C.gray, fontSize: 8 } }, { text: p[4], options: { color: C.navy, fontSize: 8, bold: true } }],
      { x: x + 0.15, y: y + ch - 0.4, w: cw - 0.3, h: 0.3, valign: "middle" });
  });
  const TX = 9.3, TW = 12.73 - 9.3;
  [["01", "Every plan as a Yuno plan", "All Access, family plans and gift terms, priced per country."], ["02", "Run by billing teams", "Plans and subscriptions from the dashboard, the API mirrors it."], ["03", "One view per plan", "Subscribers, cycle and countries, analytics one tab away."]].forEach(([n, h, t], i) => {
    const y = 1.85 + i * 1.25;
    tx(s, n, { x: TX, y, w: 0.6, h: 0.5, fontSize: 24, bold: true, color: C.blue });
    tx(s, [{ text: h, options: { bold: true, color: C.navy, fontSize: 12.5, breakLine: true } }, { text: t, options: { color: C.ink, fontSize: 10.5 } }], { x: TX + 0.65, y: y + 0.04, w: TW - 0.65, h: 1.1 });
  });
  tx(s, "Illustrative mockup in test mode. Plan names and prices from The New York Times’s public pricing, September 2026; web prices vary by market and promotion.", { x: MX, y: 5.9, w: CW, h: 0.4, fontSize: 8.5, italic: true, color: C.gray });

  // 07 THE CYCLE AND THE RETRY (B)
  s = Y.slide(d, {
    kicker: "THE ENGINE · THE CYCLE AND THE RETRY",
    title: "Every cycle: charge, and if it declines, go get it back on another provider",
    source: "docs.y.uno, Subscriptions: plans, retries, webhooks [Y]",
    notes: "Read left to right, then down. A plan holds phases, prices and the retry strategy. A subscription is one subscriber on one plan. Every billing date the engine creates a cycle charge, which is a Yuno payment routed across providers. If it declines, the retry is routed too: another provider if the rules say so, a strategy per plan (default, custom schedule, Smart ML) with A/B in the dashboard, and it stops on hard declines. Recovered means the charge still becomes a renewal. Exhausted means PAST_DUE or CANCELED, with a webhook on every transition.",
  });
  const nw = (CW - 3 * 0.45) / 4, ny = 1.95, nh = 1.35;
  [["PLAN", "Phases · prices · retries", "one definition, every provider"], ["SUBSCRIPTION", "One subscriber, one plan", "subscribes once"], ["CYCLE CHARGE", "A Yuno payment", "routed across providers, every billing date", true], ["RENEWED", "Revenue collected", "approved: the cycle is renewed"]].forEach(([h, b, sub, acc], i) => {
    const x = MX + i * (nw + 0.45);
    node(s, d, { x, y: ny, w: nw, h: nh, head: h, body: b, sub, accent: !!acc });
    if (i < 3) hlink(s, d, { x: x + nw + 0.03, y: ny + nh / 2, w: 0.39 });
  });
  const cx = MX + 2 * (nw + 0.45) + nw / 2;
  s.addShape(d.pres.ShapeType.line, { x: cx, y: ny + nh, w: 0, h: 0.5, line: { color: C.red, width: 1.25, endArrowType: "triangle" } });
  tx(s, "DECLINED", { x: cx + 0.12, y: ny + nh + 0.1, w: 1.5, h: 0.26, fontSize: 9, bold: true, color: C.red, charSpacing: 1.5, valign: "middle" });
  const ry = ny + nh + 0.5, rh = 1.45, rw = 7.9;
  rect(s, d, { x: MX, y: ry, w: rw, h: rh, fill: C.lightBg, line: C.blue, lw: 1.5 });
  tx(s, "RETRIES · STRATEGY PER PLAN · ROUTED", { x: MX + 0.2, y: ry + 0.1, w: rw - 0.4, h: 0.28, fontSize: 9.5, bold: true, color: C.blue, charSpacing: 1.5 });
  tx(s, [{ text: "Retry 1 → provider A     Retry 2 → provider B", options: { bold: true, color: C.navy, fontSize: 12, breakLine: true } },
         { text: "Strategy per plan: DEFAULT · CUSTOM_SCHEDULE · SMART (ML), A/B tested in the dashboard", options: { color: C.ink, fontSize: 10.5, breakLine: true } },
         { text: "Stops on hard declines: stolen card, invalid account, retry cap", options: { color: C.ink, fontSize: 10.5 } }], { x: MX + 0.2, y: ry + 0.42, w: rw - 0.4, h: rh - 0.5, paraSpaceAfter: 3 });
  const ox = MX + rw + 0.45, ow = CW - rw - 0.45;
  hlink(s, d, { x: MX + rw + 0.03, y: ry + 0.36, w: 0.39 });
  hlink(s, d, { x: MX + rw + 0.03, y: ry + rh - 0.36, w: 0.39 });
  node(s, d, { x: ox, y: ry, w: ow, h: 0.68, head: "RECOVERED · ACTIVE", body: "The charge still becomes a renewal", fill: C.paleGreen });
  node(s, d, { x: ox, y: ry + rh - 0.68, w: ow, h: 0.68, head: "RETRIES EXHAUSTED", body: "PAST_DUE or CANCELED, webhook sent", fill: C.paleAmber });
  Y.bar(s, "The retry is a routed charge too. It can go through a different provider than the one that declined, and when it clears, the cycle is simply renewed.", { y: 5.95, label: "The structural difference" });

  // 08 PROMOTIONAL STEP UPS (B)
  s = Y.slide(d, {
    kicker: "THE ENGINE · PROMOTIONAL STEP UPS",
    title: "The step up from promotional to full price, without losing the renewal",
    source: "FY2025 Form 10-K, MD&A and risk factors [F] · Q2 2026 results [F] · nytimes.com pricing, Sep 2026 [F]",
    tag: "Illustrative · one subscription, one plan",
    notes: "Their stated ARPU driver, handled as a phase on the plan rather than a migration. Cycle 12 is the last $4 charge, cycle 13 the first at $25. If it declines, the retry is routed by the plan's strategy. Recovered means the cycle is renewed, no new mandate. And it is visible per cohort in the dashboard. The moment a price steps up is the moment a stored credential gets retested.",
  });
  tx(s, "Your stated ARPU driver, handled as a phase on the plan rather than a migration.", { x: MX, y: 1.78, w: CW, h: 0.35, fontSize: 13, color: C.ink });
  Y.flow(s, [
    { title: "Cycle 12 · $4.00", text: "Last promotional charge.\nSet as the first phase of the plan." },
    { title: "Cycle 13 · $25.00", text: "First charge at the regular price.\nSame subscription, new price, no new mandate." },
    { title: "If it declines: retry", text: "Routed by the plan’s strategy, another provider if the rules say so.", tag: "Yuno operates here" },
    { title: "Recovered · active", text: "The cycle is simply renewed.\nApproval and recovery visible per cohort, per cycle." },
  ], { y: 2.6, h: 1.85 });
  Y.callout(s, "In your own words", "FY2025 10-K: ARPU growth was “driven primarily by subscribers transitioning from promotional to higher prices”, and “the end of a subscriber’s promotional pricing” is named among the factors that drive churn.", { y: 4.7, h: 0.95, kind: "important" });
  Y.bar(s, "The moment a price steps up is the moment a stored credential gets retested.", { y: 5.85, label: "Bottom line" });

  // 09 SUBSCRIPTIONS ON TOP OF ORCHESTRATION (B, how we help)
  s = Y.slide(d, {
    kicker: "SUBSCRIPTIONS ON TOP OF ORCHESTRATION · HOW WE HELP",
    title: "The engine comes with its orchestration underneath, moved one cohort at a time",
    source: "docs.y.uno [Y] · Yuno Subscriptions internal launch deck, Sep 2026 [Y]",
    notes: "How we help, in one picture. Your platform stays the system of record. The engine creates the cycle charge and schedules the retry. Same layer: every cycle charge is a Yuno payment, routed by your rules and retried on another provider. Underneath, Stripe stays, a second acquirer and local rails are added. The move is cohort by cohort, from Spreedly to Yuno, never everything on day one. The retry can only go to a different provider if the engine and the routing are the same thing.",
  });
  Y.columns(s, [
    { header: "System of record · your platform", text: "Plans, entitlement, the account page and everything your subscriber sees stay with you." },
    { header: "Built by Yuno · the engine", text: "Creates the cycle charge, knows the phase and the price, schedules the retry." },
    { header: "Same layer · Yuno routing", text: "Every cycle charge is a Yuno payment: routed by your rules, retried on another provider." },
    { header: "Where it runs · providers", text: "Stripe stays. A second acquirer and local rails are added as the cohorts move." },
  ], { y: 1.85, h: 2.35 });
  tx(s, "FROM SPREEDLY TO YUNO, ONE COHORT AT A TIME", { x: MX, y: 4.32, w: CW, h: 0.26, fontSize: 9.5, bold: true, color: C.gray, charSpacing: 2 });
  Y.phaseBar(s, [{ label: "Cohort 1", title: "", text: "" }, { label: "Cohort 2", title: "", text: "" }, { label: "Cohort 3", title: "", text: "" }, { label: "Whole base", title: "", text: "" }],
    { y: 4.6, chips: ["UNCHANGED: your platform as system of record", "CHANGES: renewals route on Yuno", "NOT REQUIRED: moving everything on day one"] });
  Y.bar(s, "The retry can only go to a different provider if the engine and the routing are the same thing.", { y: 5.98, label: "Bottom line" });

  // 10 WHAT IS LIVE (P)
  s = Y.slide(d, {
    kicker: "WHAT IS LIVE",
    title: "Live in production today, with the roadmap in the open",
    source: "Yuno Control Center, 31 Aug 2026 [Y] · Yuno Subscriptions internal launch deck, Sep 2026 [Y] · docs.y.uno [Y]",
    notes: "Proof, then honesty. 16 merchants run on the engine, 135K active subscriptions. Per cycle, 83% of renewals approve on the first attempt and 86% after retries; 69K past-due subscriptions were reactivated in 30 days. Then the list of what is live and what is next. Built for billing teams, not only developers.",
  });
  Y.statTiles(s, [
    { value: "16", label: "Merchants live on the engine", note: "Yuno Control Center, 31 Aug 2026 [Y]" },
    { value: "135K", label: "Active subscriptions", note: "Yuno Control Center, 31 Aug 2026 [Y]" },
    { value: "83% → 86%", label: "Renewal approval per cycle", note: "First attempt, then after retries [Y]" },
    { value: "69K", label: "Past-due subscriptions reactivated", note: "In 30 days, across the engine [Y]" },
  ], { y: 1.8, h: 1.8 });
  const LIVE = ["Plans with phases and a price per country", "Trials of any length", "Retries per plan: default, custom schedule, Smart ML, A/B", "Pause, resume, cancel, change plan", "PAST_DUE and a webhook on every transition", "Cards, Apple Pay, Google Pay, PayPal, Pix Automático", "Analytics: MRR and ARR, retry results by strategy", "Stripe Billing bridge and Stripe Proxy"];
  const ROAD = [["Promotions: codes, automatic promos, first N cycles", "NEXT"], ["Subscriptions created inside the payment flow", "NEXT"], ["Change the payment method on a subscription", "LATER"], ["Testing and simulation with a test clock", "LATER"]];
  const lx = MX, lw = 6.9, rx = MX + lw + 0.45, rw2 = CW - lw - 0.45, ly = 3.85;
  tx(s, "LIVE IN PRODUCTION", { x: lx, y: ly, w: lw, h: 0.26, fontSize: 10.5, bold: true, color: C.navy, charSpacing: 2 });
  s.addShape(d.pres.ShapeType.line, { x: lx, y: ly + 0.3, w: lw, h: 0, line: { color: C.navy, width: 1.5 } });
  LIVE.forEach((t, i) => tx(s, [{ text: "✓  ", options: { bold: true, color: C.green, fontSize: 10.5 } }, { text: t, options: { color: C.ink, fontSize: 10.5 } }], { x: lx, y: ly + 0.4 + i * 0.235, w: lw, h: 0.235, valign: "middle" }));
  tx(s, "ON THE ROADMAP", { x: rx, y: ly, w: rw2, h: 0.26, fontSize: 10.5, bold: true, color: C.blue, charSpacing: 2 });
  s.addShape(d.pres.ShapeType.line, { x: rx, y: ly + 0.3, w: rw2, h: 0, line: { color: C.blue, width: 1.5 } });
  ROAD.forEach(([t, w], i) => {
    const yy = ly + 0.42 + i * 0.46;
    chip(s, d, { x: rx, y: yy + 0.02, w: 0.7, h: 0.3, text: w, dark: w === "NEXT" });
    tx(s, t, { x: rx + 0.85, y: yy, w: rw2 - 0.85, h: 0.36, fontSize: 10.5, color: C.ink, valign: "middle" });
  });
  Y.bar(s, "Built for billing teams, not only developers: everything in the dashboard, and the API mirrors all of it.", { y: 6.05, label: "Bottom line" });

  // 11 PROPOSED NEXT STEP
  s = Y.slide(d, {
    kicker: "PROPOSED NEXT STEP",
    title: "A first cycle together: one cohort, one renewal path, measured",
    source: "Yuno proposal, Sep 2026",
    notes: "The ask is small and measurable. Scope one cohort and one plan family together. Run one billing cycle, four weeks, with a second provider as fallback and your platform unchanged. Measure renewal approval per cycle in the dashboard, first attempt vs after retries. We need decline codes by country and issuer, current retry recovery, plan mix and country pricing. You get a per-cycle baseline, a retry A/B on your own traffic and a build or buy call on your data. First step: a 30 minute walkthrough with your subscription platform team.",
  });
  Y.phaseBar(s, [
    { label: "1 · Scope", title: "One cohort, one plan family", text: "Picked together: a plan family and a market where renewals are visible." },
    { label: "2 · Run", title: "One billing cycle", text: "Four weeks of renewals on Yuno, second provider as fallback, your platform unchanged." },
    { label: "3 · Measure", title: "Renewal approval per cycle", text: "First attempt vs after retries, per cohort, in the dashboard." },
  ], { y: 1.9 });
  Y.twoColumn(s, { header: "We need", items: [{ bold: "Decline codes by country and issuer" }, { bold: "Current retry recovery" }, { bold: "Plan mix and country pricing" }] },
    { header: "You get", items: [{ bold: "A per cycle baseline" }, { bold: "A retry A/B on your traffic" }, { bold: "A build or buy call on your data" }] }, { y: 4.2, h: 1.55 });
  Y.bar(s, "First step: a 30 minute walkthrough with your subscription platform team, then we scope the cohort together.", { y: 5.95, label: "Bottom line" });

  // 12 CLOSE
  Y.close(d, { line: "Let’s grow together", thesis: "Every renewal, with a second path.",
    contact: "German Tatis · Business Development Manager · german.tatis@y.uno      Magdalena Torrealba · Sales Strategy Associate · magdalena.torrealba@y.uno · +1 786 219 7612",
    yunoLogo: LOGO_Y });

  await Y.save(d, OUT);
  console.log("built", d.n, "slides ->", OUT);
})().catch(e => { console.error(e); process.exit(1); });
