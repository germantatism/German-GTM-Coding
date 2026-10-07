/**
 * example_build_deck.js: a worked example of a build script that exercises every helper in yuno_deck.js
 * (cover with the yuno | merchant lockup, divider, twoColumn + bottomBar, statTiles, flow, table with totalRow,
 * columns, native bars, waterfall, phaseBar with chips, numbered, callout, bar, ask, close).
 * Copy it to <account>/build/build_deck.js, replace every value with ledger-backed facts for the real merchant,
 * then: node build_deck.js [output.pptx]
 * The numbers below are illustrative placeholders for the smoke test, not facts about 1Password.
 */
const Y = require("/Users/germantatis/Desktop/GTMCoding/.claude/skills/yuno-sales-deck/scripts/yuno_deck.js");
const REPO = "/Users/germantatis/Desktop/GTMCoding";
const OUT = process.argv[2] || `${REPO}/Deals/1Password/Yuno_x_1Password_BusinessCase_Sep2026.pptx`;
(async () => {
  const d = Y.createDeck({ merchant: "1Password" });
  Y.cover(d, { thesis: "The payments backbone for the next billion users", descriptor: "A business case for payments orchestration", date: "SEP 2026",
    sources: "Company filings, help center, job postings",
    yunoLogo: `${REPO}/Yuno Design System/yuno-design-system/assets/yuno-wordmark-white.png`,
    merchantLogo: `${REPO}/yuno-sales-pitch-maker/public/merchants/1password.png` });
  let s = Y.slide(d, { kicker: "WHY WE ARE HERE", title: "1Password scaled to $250M on one processor. Everything that leaks from here, Yuno can solve.", source: "Company blog, 2026-03 [F]; Yuno estimate [A]", notes: "Talk track: open with their own number.", tag: "Illustrative · pending 1Password data" });
  Y.twoColumn(s, { header: "What we see today", items: [{ bold: "Single processor for 100% of card volume", text: "Checkout inspection, 2026-09." }, { bold: "No local methods outside the US", text: "Help center lists cards and PayPal only." }, { bold: "Hiring a billing platform lead", text: "Posting dated 2026-08." }] },
    { header: "What Yuno solves, above Stripe", items: [{ bold: "Local methods", text: "Pix, UPI, iDEAL, SEPA.", chip: "~$1.2M/yr" }, { bold: "Local acquiring", text: "Domestic routes on the cross-border slice.", chip: "~$0.8M/yr" }, { bold: "Renewal recovery", text: "Retries across PSPs.", chip: "~$0.5M/yr" }] },
    { bottomBar: "One integration, live in weeks, with Stripe untouched: ~$2.5M a year at conservative inputs. The rest of this deck shows the math." });
  Y.divider(d, "THE REALITY", "Where money leaks today");
  s = Y.slide(d, { kicker: "WE'VE DONE OUR HOMEWORK", title: "1Password at a glance: a subscription business with 2-3 markets carrying most of the growth", source: "Company filings [F]; Yuno estimate [A]" });
  Y.statTiles(s, [{ value: "$250M", label: "ARR", note: "Company blog, 2026 [F]" }, { value: "~12M", label: "Monthly active users", note: "Yuno estimate [A]" }, { value: "75%", label: "Revenue outside the US", note: "Processor case study [F]" }, { value: "3", label: "Priority markets", note: "Brazil, India, Germany" }, { value: "~$2.5M/yr", label: "Preliminary gross value", note: "Base case [A]" }, { value: "1%", label: "of ARR", note: "Headline as share of revenue" }], { cols: 3, h: 1.6 });
  s = Y.slide(d, { kicker: "HOW MONEY MOVES", title: "Subscription economy: 3 nodes where Yuno operates", source: "Help center, terms of use [F]" });
  Y.flow(s, [{ title: "Pay-in", text: "Cards via Stripe, PayPal wallet", tag: "Yuno operates here" }, { title: "Subscription", text: "Stripe Billing, monthly and annual plans" }, { title: "Renewal", text: "Stripe smart retries, no cross-PSP fallback", tag: "Yuno operates here" }]);
  s = Y.slide(d, { kicker: "STRATEGIC CONTEXT · THE DECISION FRAME", title: "Stripe alone leaks revenue at three points, and a second PSP only fixes one", source: "Yuno analysis on public data" });
  Y.table(s, ["Gap", "Today", "Option A: second PSP", "Option B: Yuno"], [["Missing local methods ($1.2M/yr)", "○ Cards only", "◐ Some methods, second integration", "● 1,000+ methods, one API"], ["Cross-border declines ($0.8M/yr)", "○ US acquiring for all", "◐ One more acquirer", "● Local routes per market"], ["Failed renewals ($0.5M/yr)", "◐ Stripe retries", "○ Two retry engines, no fallback", "● Cross-PSP retries"], ["Total at stake", "", "", "~$2.5M/yr"]], { totalRow: true, colW: [3.6, 2.6, 3.0, 2.93] });
  s = Y.slide(d, { kicker: "THE RESOLUTION · OPERATING MODEL", title: "Three pillars sit above your existing rails", source: "docs.y.uno" });
  Y.columns(s, [{ header: "Local rails network", text: "Connect once.", bullets: ["1,000+ payment methods", "190+ countries", "Local acquirers per market"] }, { header: "Intelligent orchestration", bullets: ["Rules first, ML second", "Cross-PSP retries", "Rollback is a configuration change"] }, { header: "Unified data and treasury", bullets: ["One payment object", "Fees, FX and approvals in one view", "Reconciliation on the roadmap"] }]);
  s = Y.slide(d, { kicker: "THE RESOLUTION · AUTHORIZATION", title: "Two structural levers lift authorization: local routing and resilience", source: "Yuno performance dashboard, 24-month aggregate [Y]", tag: "Illustrative · pending 1Password data" });
  Y.bars(s, [{ name: "Approval rate", labels: ["Cross-border", "Local route"], values: [83, 93] }], { x: 0.6, w: 5.8, title: "First-attempt approval, %", pct: true });
  Y.bars(s, [{ name: "Approval rate", labels: ["1 provider", "2 providers", "3 providers"], values: [93, 94, 96] }], { x: 6.9, w: 5.8, title: "Approval with N providers, %", pct: true });
  Y.callout(s, "Honesty guardrail", "The lift applies only to the slice moved from cross-border to local routes. Net effect on total international volume is 2-3%, lower on baselines above 90%.", { y: 5.5, h: 0.9, kind: "guardrail" });
  s = Y.slide(d, { kicker: "METHODOLOGY BRIDGE", title: "How we sized the levers: start with existing demand, then remove leakage step by step", source: "Model in build/model.py [A]", tag: "Illustrative · pending 1Password data" });
  Y.waterfall(s, [{ label: "Local methods", value: 1.2, caption: "Add local ways to pay" }, { label: "Local acquiring", value: 0.8, caption: "Fix declined cards" }, { label: "Renewal recovery", value: 0.5, caption: "Save failed renewals" }], { fmt: v => "$" + v.toFixed(1) + "M", totalLabel: "Total /yr" });
  Y.callout(s, "Waterfall logic", "Local methods expand the paid base. Localized processing improves approval on the remaining card attempts. Retries recover failed renewals on the resulting base. The levers are not three independent user pools.", { y: 5.55, h: 0.9, kind: "important" });
  s = Y.slide(d, { kicker: "IMPLEMENTATION", title: "Production in weeks, not quarters", source: "Yuno implementation playbook" });
  Y.phaseBar(s, [{ label: "Phase 0", title: "Scope and connect", text: "Sandbox, SDK, first connectors." }, { label: "Phase 1", title: "Pilot on a contained slice", text: "One market, 5% cohort, validate vs Stripe." }, { label: "Phase 2", title: "Expand on evidence", text: "Ramp markets and methods as data confirms." }], { chips: ["Rollback = a configuration change", "Additive above your existing rails"] });
  s = Y.slide(d, { kicker: "WHERE WE'RE DIFFERENT", title: "Five things you can check", source: "y.uno, docs.y.uno" });
  Y.numbered(s, [{ bold: "No acquiring arm", text: "Routing optimizes your KPIs, not ours." }, { bold: "One payment object", text: "Normalized status, raw code preserved." }, { bold: "Published figures", text: "7% authorization uplift, 30% recovered revenue (Yuno published figures · y.uno)." }, { bold: "Standard pricing", text: "First $50,000 processed free, then $0.05 per transaction." }], { footer: "All four are checkable. Please check them." });
  Y.bar(s, "Keep Stripe as the global baseline. Yuno orchestrates the layer around it.", { y: 6.15, label: "Bottom line" });
  Y.ask(d, { title: "Three asks, and the first is your data", asks: [{ bold: "Your data, under NDA", text: "Decline file by ISO code, channel mix, auth rates by BIN and country." }, { bold: "A two-week joint data sprint", text: "Days 1-3 data exchange, 4-7 calibration, 8-11 roadmap, 12-14 pilot scope." }, { bold: "A contained pilot", text: "Brazil first, 5% cohort, validated against Stripe." }], footer: "Proposed dates: ____________", source: "Yuno proposal" });
  Y.close(d, { line: "Let's grow together", thesis: "The payments backbone for the next billion users", contact: "German Tatis · Account Executive · german.tatis@y.uno", yunoLogo: `${REPO}/Yuno Design System/yuno-design-system/assets/yuno-wordmark-white.png` });
  await Y.save(d, OUT);
  console.log("built", d.n, "slides ->", OUT);
})().catch(e => { console.error(e); process.exit(1); });
