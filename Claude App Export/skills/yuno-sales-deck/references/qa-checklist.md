# Pre-send QA checklist

Every item below is here because it went wrong in a real deck. Run `scripts/deck_qa.py` first; it catches the mechanical ones (including German's house rules) and prints the money inventory you need for section 2. The rest needs reading.

## 1. Identity and leftovers
- [ ] Only this merchant's name, products, plan names and people appear. No other prospect's name anywhere (past decks shipped with OpenAI, Discord, Scopely, Turo and a Mastercard Agent Pay paragraph inside a different merchant's deck).
- [ ] Provider names in diagrams are *their* providers; no competitor or incumbent text left in the Yuno column of an architecture or comparison slide (Higgsfield deck shipped with "Adyen's own routing" in the Yuno column).
- [ ] No placeholders, brackets, "TBD", template text, or internal working notes in any language on slides. Notes for German live in speaker notes.
- [ ] Each Source line belongs to its slide (no copy-pasted source from the previous slide).
- [ ] No em-dashes and no " - " as punctuation anywhere in slide copy or notes. The phrase "no small feat" appears nowhere.

## 2. Numbers reconcile
- [ ] The hero number is identical on every slide it appears (exec summary, why-we're-here bar, decision frame, waterfall, value table, close). The Anthropic deck shipped with four different totals ($1.25B, $2.5B, $105M/mo, $238M/mo).
- [ ] Lever subtotals sum to the total; monthly × 12 = annual; country rows sum to the portfolio total; concentration percentages match the table.
- [ ] Counts are consistent: number of markets, levers, data points (Higgsfield deck said 18 markets in some places and 20 in others).
- [ ] Units are right: "$" only on money ("$6.1M MAU" shipped once); MAU/WAU/users have no "$"; every figure has a unit and period (/mo, /yr); "~" on estimates.
- [ ] Every amount is in USD. No ₩ € £ ¥ ₹ R$ C$ or local-currency codes; where a stat only exists in local currency, a currency-free metric replaced it.
- [ ] No sub-population exceeds its parent (India MAU above the global MAU shipped once; WAU vs MAU not mixed).
- [ ] Cited evidence and model use the same kind of uplift (relative % vs percentage points).
- [ ] Headline shown as a % of the merchant's revenue; transactions ≈ revenue / average ticket.
- [ ] Client-reported metrics (ticket, TPV, volumes) are used exactly as reported; any derived figure that disagrees is flagged to German, not printed.
- [ ] Every [A] assumption on a slide is in the appendix assumptions table; sensitivity line present.

## 3. Truth and claims
- [ ] Every fact traces to a ledger row with a source; anything unverifiable was omitted, not disclaimed. Disclaimers appear only under real, sourced estimates.
- [ ] Nothing the merchant's own disclosures contradict (e.g. claiming no paid users abroad when most revenue is international).
- [ ] The deck doesn't propose what they already have live (methods, wallets, local pricing). It says "live via <PSP>" and moves to what's missing.
- [ ] Product claims checked against docs.y.uno; "live" only when confirmed; shipped vs roadmap stated honestly. Reconciliation across PSPs is footnoted as roadmap.
- [ ] Yuno-wide performance figures are the published ones (7% authorization uplift, 30% recovered revenue) or verified client results; no "+12%" or "20-30%" tiles.
- [ ] PayPal is listed as a wallet/APM, never counted as a PSP; processor lists hold gateways, acquirers/PSPs and merchants of record only.
- [ ] Pricing is deal-approved, or Yuno's standard pricing labeled as such ($50,000 processed free, then $0.05 per transaction); no invented tiers.
- [ ] Uptime, latency, TPS and SLA figures appear only if German confirmed them for this deal.
- [ ] Customer names are referenceable; no other customer's terms or volumes disclosed; nothing about Riot Games; GoFundMe details only with German's OK.
- [ ] What is not addressable is stated (guardrail box). Gross vs net is labeled.
- [ ] The real competitor in the account is the one in the comparison.
- [ ] Prior history with the account (earlier proposal, sandbox, contacts, numbers already sent) is acknowledged or deliberately left out with German's agreement.
- [ ] Team and resource commitments fit the deal size.

## 4. Story
- [ ] Every slide is checkable as Requirement, Benefit or Proof; the deck moves R → B → P → Ask.
- [ ] Reading only the titles tells the argument (types A, B, D). Titles are sentences with numbers; no "Overview", "Solution", "Agenda" as content titles.
- [ ] Every content slide has one idea, one proof, a source.
- [ ] Yuno boilerplate is at most a quarter of the main deck; the rest is about them.
- [ ] The deck ends on The Ask or a dated next step, then the close line. Not "Thank you".
- [ ] Main body is presentable in the meeting length; the rest is appendix.

## 5. Craft
- [ ] `deck_qa.py` exits 0; every slide looked at (LibreOffice render, Google Slides thumbnails via `scripts/slides_thumbs.py`, or opened by hand): no overflow, overlap, clipped text, off-slide shapes, orphan words in titles.
- [ ] Cover shows the `yuno | <merchant>` lockup top-left on the dark hero; no greeting, no large logo block.
- [ ] Charts start at zero, labeled, one color per series; tables ≤ ~8 rows on main slides.
- [ ] Layouts vary; no three identical layouts in a row.
- [ ] Footer, slide numbers and "Illustrative · pending data" tags present where needed.
- [ ] File named `Yuno_x_<Merchant>_<Type>_<MonYYYY>.pptx`, saved in the account folder with `build/` next to it.

## 6. Hand-off note to German
- [ ] Storyline in one line + hero number and its % of revenue.
- [ ] The 6-8 slides to present live.
- [ ] Claims to confirm before sending, defaults assumed, and open gaps.
- [ ] Whether the visual pass was done, and how.
- [ ] Committed and pushed to `main`.
