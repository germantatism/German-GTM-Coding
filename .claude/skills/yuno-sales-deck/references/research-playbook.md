# Research playbook

The deck is only as good as the evidence ledger behind it. Budget most of the effort here. Internal sources first: they tell you what Yuno already knows and has promised, and they keep you from presenting a "cold" deck to an account with history.

## 1. Internal sources (always check all of them)

| Source | Look for | Why it matters on the slide |
|---|---|---|
| Local repo (`Deals/<Merchant>/`, `Industry/<Vertical>/<Merchant>/`, `data/research/*<merchant>*`, `Business Cases/`) | Prior decks and PDFs, research briefs, meeting briefs, call notes, business cases, pricing already sent | The account's history and every number already shown to them |
| Memory (`~/.claude/projects/-Users-germantatis-Desktop-GTMCoding/memory/MEMORY.md`, then `project_<merchant>.md`) | Deal state, contacts, decisions, what German has said about the account | Tone, stage, who the champion is, what must never be said |
| deck.yuno.tools research cache (`yuno-sales-pitch-maker/public/merchants.csv`, `src/data/business-overviews.json`, Supabase `merchants` row) | PSPs, missing methods, pains, footprint for 700+ merchants | Verified starting point; rows built before June 2026 may hold padded content, re-verify before use |
| Gong (`mcp__claude_ai_Gong_MCP__ask_account`, `ask_deal`, `generate_brief`) | Call transcripts, what the buyer said, objections, commitments made | Their pain in their own words; nothing already promised gets contradicted |
| Calendar (`mcp__claude_ai_Google_Calendar__search_events`, today ± 2 weeks) | The meeting, attendees on both sides, who set it up | Deck type, audience, agenda slide owners |
| Slack (`mcp__claude_ai_Slack__slack_search_public_and_private` on the merchant name) | Existing opportunity and owner, pricing approvals, sandbox access, SE threads, incidents | Avoid contradicting prior proposals; acknowledge history; approved pricing |
| Gmail (`mcp__claude_ai_Gmail__search_threads`) | Threads with the merchant, DocuSign, Papermark views, questionnaires, drafts German left | Their words, their questions, what they opened |
| Drive (`mcp__claude_ai_Google_Drive__search_files`, `read_file_content`) | Past decks, business cases, call transcripts, SDR research docs, scoping docs, order forms | Their stack, volumes, AOV, pains quoted from calls |
| Glean (`mcp__plugin_yuno_glean__chat`, `company_search`) | Internal docs: pricing approvals, SE notes, product status, other teams' work on the account | Do not present a "cold" deck to an account Yuno already knows |
| Yuno docs (docs.y.uno via `mcp__plugin_yuno_context7__resolve-library-id` + `query-docs`, else WebFetch) | Product behavior and limits | Every product claim must survive this check |

If an opportunity already exists under another owner, tell German before building; the deck may need to acknowledge the earlier proposal and sandbox work.

## 2. Public sources, by what they prove

| Evidence you need | Best sources | Notes |
|---|---|---|
| Size, growth, geography, model | 10-K / S-1 / annual report / investor letters; for private companies: funding announcements, press quotes from executives, Sacra/PitchBook-type estimates | Filing numbers are [F]. Estimates are [E] and get a range. |
| Disclosed payment risks | 10-K Item 1A risk factors, Item 8 notes (processor and receivables concentration), human-capital section (engineering headcount) | This is the strongest material there is: "disclosed in your own filing". |
| Current payment stack | The processor's customer story or press release about them, checkout inspection, help center and billing FAQ, terms of use, status pages, engineering blog, BuiltWith-style signals | Record exactly which methods, currencies and wallets are live and where; the deck must not propose what they already have. |
| Pain signals | Job postings (payments, billing, retention, revenue accounting, regional GTM), outage reports, reviews and complaints (Trustpilot, BBB, Reddit, app stores), press investigations | A role being hired = a problem being staffed. Quote the posting date. |
| Demand by country | Traffic share by country (SimilarWeb-type), app-store rankings, their own regional disclosures | Triangulate; show ranges; label "Yuno-estimated". |
| Monetization benchmarks | Conversion and churn benchmarks for the model (subscription apps, SaaS), processor-published checkout studies, recurring-billing benchmarks | Keep units consistent with how you apply them. |
| Local payment facts per market | Central banks and scheme operators (NPCI, BCB, Banxico, Bank Indonesia, BKM, Betaalvereniging...), PPRO/Worldpay-type country reports | One proof stat per country page, dated. |
| Competitor moves | Competitors' pricing pages, launches with local methods or local pricing, their processor stories | Powers "why now". Must be real and dated. |
| Incumbent processor economics | The processor's public pricing page | Useful for "stack tax" comparisons; note that large merchants are on custom pricing. |
| Scheme rules | Visa/Mastercard monitoring programs when disputes are a theme | Frame as risk insurance, not accusation. |
| Attendee titles and remit | LinkedIn, the company's leadership page, press | Who signs; tailor examples to their remit. |

Use web search for anything time-sensitive; company facts from memory go stale fast. For a full company brief, run `/research <merchant>` (this repo's SDR research brief, written to `data/research/`). For the Excel model, `/business-case`.

## 3. The evidence ledger

Keep a scratch file (`ledger.md` or CSV) and fill it as you research:

```
| # | Claim (as it will appear) | Value | Source | Date | Tag | Used on slide |
|---|---|---|---|---|---|---|
| 1 | Share of revenue outside the US | 75% | Processor customer story | 2026-01 | F | 2, 3, 6 |
| 2 | Monthly active users, global | ~12M (10-14M) | Yuno estimate: 30M registered x ~40% | 2026-09 | A | 6, 17, appendix |
```

Tags: **[F]** disclosed by the merchant or in a primary document · **[E]** third-party estimate · **[Y]** Yuno platform data (say which dataset and period) · **[A]** our assumption (must appear in the appendix assumptions table).

Rules:
- A number without a ledger row does not go on a slide.
- One value per fact. If sources disagree, pick one, note the other in the ledger, and use the same value everywhere.
- [A] and [E] numbers are shown with "~" and, where it matters, a range.
- Paraphrase sources; never paste long passages. Short source line on the slide, full reference in the appendix or notes.
- Corroborate every material fact with a second independent source; primary sources beat blogs. Run a final pass over every value before it goes on a slide.
- If a fact cannot be verified, omit it. A disclaimer ("per public sources") is only for a real, sourced estimate worth keeping, never a license to include a guess. A shorter deck of true facts beats a fuller one with one guess.
- USD only. When a stat exists only in local currency, swap it for a currency-free metric from the same source (users, transaction counts, shares, growth) instead of converting at an assumed rate.
- Use the metric the client reported (ticket, TPV, volumes) over one derived from their other data; flag the discrepancy to German separately, never silently in the deck.
- PayPal is a wallet/APM, never a PSP: it does not count toward processor totals or the topology. Processor lists hold gateways, acquirers/PSPs and merchants of record only; BNPL, wallets, card networks, issuers and local methods go under payment methods.

## 4. What to extract from the research before writing

Answer these in a few lines each; they become the spine of the deck.
1. **What did they already choose?** (the reframe) A strategy, launch, hire, or statement that Yuno accelerates.
2. **How does money move?** Pay-in channels, the platform step, payouts; which providers at each node.
3. **Where does it leak?** Three or four gaps with a number each.
4. **Who else could fix it, and why only partly?** The real alternative in the account.
5. **What would they have to believe?** The two or three swing assumptions, and which of their data would settle them.
6. **What can we ask for this week?**
