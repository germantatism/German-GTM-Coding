# /builddeck — End-to-end deck build for a new merchant

You're building a complete merchant entry for **$ARGUMENTS** on `deck.yuno.tools`. End-to-end: research → Supabase row → CSV/manifest → logo → business-overview → commit → push → deploy verification. Single command, fully automated (the logo is auto-fetched via logo.dev; no manual handoff needed).

## A "complete" deck — the current standard (build to this every time)

A deck is only complete when ALL of these are produced, in this order. This is the standard every recent deck (Stripe Tour Berlin batch, DistroKid, Midjourney, Kick) was built to. Do not stop early or skip any item:

1. **Business Overview entry** in `src/data/business-overviews.json` so the **"What we know about your business"** slide renders (revenue if verifiable, description, catalyst, 3 commerce-footprint anchors, top countries, business lines, APMs). This slide is NOT optional anymore; a deck without it reads as incomplete.
2. **5 pain titles** anchored to real research, each weaving a taxonomy keyword in organically (NO literal "(BUCKET)" tag in the text).
3. **PSPs** per the decision tree (confirmed, single, or seeded + disclaimer).
4. **10 missing methods**, real markets the merchant operates in.
5. **The 4 standard capability levers** (current names + copy, see the Capability section).
6. **capabilities_live** subset.
7. **Logo** at `public/merchants/{slug}.png` (auto-fetched + normalized).
8. **CSV row + manifest entry** (generated.js) for the slug.
9. **Supabase row upserted**, **build passes**, **commit + push to `main`**, **deploy verified**.

The helper scripts `scripts/_finish-merchant.sh` + `scripts/_add-merchant.mjs` + `scripts/_logo-one.mjs` automate steps 1, 7, 8 and the Supabase upsert (see "Build mechanism").

## Inputs

- **Required (positional):** the company name (everything before any `--flag`).
- **Optional flags:**
  - `--mode banking` — pitch mode targeting banks. Affects slide 3 framing only (different `CAPABILITY_DEFS_BANKING` set already wired into `SlideDiagnostic.jsx`).
  - `--mode partner` — partner-pitch framing.
  - `--industry "Industry & Subcategory"` — override auto-detected industry. Must be a value already used in `public/merchants.csv` or follow the same convention.

If no flag is passed, default mode is `merchant` (the standard Yuno-vs-merchant pitch).

## Hard constraints — read every time

These are not negotiable. They come from prior decisions and are documented in the user's auto-memory:

1. **Auto commit + push at the end.** Never stop at "wrote the files." Run `git add` → `git commit` → `git push origin main`. The local working branch is `main` and the deploy branch is `main` (Railway auto-deploys from it). Source of truth: `feedback_auto_commit_push.md`.
2. **Never put false information.** When a fact (especially PSPs) isn't publicly verifiable, follow the disclaimer rule below. Source: `feedback_no_false_info_disclaimer.md`.
3. **Never use the phrase "no small feat"** anywhere in capability copy or pain titles. Source: `feedback_no_small_feat.md`.
4. **Em-dashes (`—`) are banned in body copy** per the deck's design principles. Use commas or restructure. Pain titles, capability descs, and the disclaimer text all count as body copy. Source: `DESIGN.md`.

## Pre-flight checks

Before doing anything else:

1. **Logo.** First check `/Users/germantatis/Desktop/GTMCoding/yuno-sales-pitch-maker/Logos/` for a file matching the company name (case-insensitive substring; prefer SVG > PNG > WEBP > JPG) and use it if present. If nothing is there, do NOT abort: auto-fetch via logo.dev using the merchant domain (this is the standard flow, handled by `scripts/_finish-merchant.sh {slug} {domain}` which calls logo.dev then `_logo-one.mjs` to normalize to white-on-transparent). Only ask the user for a logo if logo.dev returns nothing usable.
2. **Slug determination.** Slugify the company name: lowercase, non-alphanumeric → `-`, trim. E.g. `SAP` → `sap`, `Trip.com Group` → `trip-com-group`. Don't shorten — the slug must match what the app's `resolveMerchant()` looks up.
3. **Existing-merchant check.** Query Supabase for the slug:
   ```bash
   curl -s "https://mlwiosgalwsroisdkytl.supabase.co/rest/v1/merchants?slug=eq.{slug}" \
     -H "apikey: <service_role_key>" -H "Authorization: Bearer <service_role_key>"
   ```
   If a row comes back, **show the user a diff** of what's about to change vs. what's there, and ask before upserting. Don't silently overwrite someone's manual edits.

## Service-role key retrieval

The Supabase service-role key is needed for INSERT/PATCH on the `merchants` table (RLS only allows anon SELECT). It's not stored in any `.env` file in this repo. Recover it by grepping prior Claude chat history:

```bash
grep -rh "sb_secret_" /Users/germantatis/.claude/projects/-Users-germantatis-Desktop-GTMCoding/ 2>/dev/null \
  | grep -oE "sb_secret_[a-zA-Z0-9_-]+" | sort -u | head -1
```

Project URL: `https://mlwiosgalwsroisdkytl.supabase.co`. Anon publishable key (read-only, safe to use): `sb_publishable_2DtpydQUpys--Waoc_Vy-g__fjTrzr2`.

If the service-role key isn't recoverable from history, ask the user to paste it and continue.

## Research — what to find

Use `WebSearch` and `WebFetch` in parallel where possible. Cap at ~12 searches total. The research powers both the Supabase row fields AND the Business Overview slide (slide 2), so cover both. Targets:

- **Headline financials**: latest annual revenue (always in USD), growth rate, public/private, fiscal year. Source: 10-K / 20-F if public, latest earnings release if recent. If the company is private and revenue is reported by a third party (Forbes, Inc, PitchBook, S&P), use that number and mark `estimated: true` with the source. If no number is verifiable, **omit revenue entirely** — never fabricate.
- **Geographic footprint**: which markets they serve, where their cloud/SaaS revenue is shifting toward, where they don't have local methods. This drives `missing_methods` and the local-payment-method capability copy.
- **SimilarWeb top countries**: WebFetch `https://www.similarweb.com/website/{primary-domain}/` and pull the country-share table. Filter to share ≥ 1%, cap at top 10. If the SimilarWeb page is unreachable or returns no data, omit the countries section entirely.
- **Recent strategic catalyst**: most recent acquisition, IPO, take-private, market exit, major product launch, regulatory event, or leadership change in the last 12-24 months. One headline + one detail sentence with the deal size / date / counterparty. If nothing material, omit the catalyst block.
- **Commerce footprint (3 anchors, payment-relevant)**: pick 3 stats that describe where and how this merchant transacts, NOT biographical trivia. Bias toward payment-relevant dimensions Yuno can optimize: digital vs in-store sales mix, # of stores / POS surface, # of countries shipped to, monthly visitors (SimilarWeb), active customers / loyalty members, average order value, # of currencies transacted. Avoid: founding year, headcount (unless extraordinary), HQ location. The slide section is called "Commerce Footprint" — every anchor must answer "how big is the surface Yuno would optimize?"
- **Business lines / product portfolio**: the distinct revenue lines the company operates (e.g. for Nordstrom: Full-Line, Rack, Nordstrom.com, Nordstrom Local). Only include lines you can confirm with a primary source. 3-6 chips ideal.
- **APMs (Alternative Payment Methods) at checkout**: WebFetch their checkout / payment-options help page and list the non-card methods accepted (wallets like Apple Pay / Google Pay / PayPal, BNPL like Affirm / Afterpay / Klarna / Sezzle / Zip, bank methods like Pix / SEPA / iDEAL / OXXO). Confirm via official pages or partner pages (e.g. afterpay.com/store-directory). If you can't verify the checkout, omit the APMs section.
- **Payment stack signals**: search for "{company} Stripe Adyen Worldpay Braintree Checkout.com payment processor", "{company} payment gateway", "{company} job listings payments engineer", "{company} press release fintech partnership". Look at official help pages, T&Cs, dev docs, job boards, SEC filings, press releases. Tag confirmed (live checkout, official docs, press release) vs. inferred (job posting alone, third-party article). If the company runs a help page describing how customers pay them, that's gold.
- **Business model**: subscription, transactional, marketplace? Shapes `capabilities_live` (subscriptions, tokenization, fraud, payouts, kyc, kyb, baas).
- **Pain points the merchant is publicly known to have**: complaints on Reddit/Trustpilot/community forums about declined cards, double charges, refunds, missing local methods, billing failures. These become real, verifiable pain titles.

**Accuracy rule.** Every field in the Business Overview slide is independently optional. The slide reflows automatically — never pad an empty section with guesses. If revenue is not verifiable, omit. If APMs aren't documented, omit. If SimilarWeb fails, omit countries. **Mentir es peor que omitir.**

## Industry — pick from the canonical list

Use values already in `public/merchants.csv` whenever possible. Canonical buckets we use:

```
AdTech & Mobile · AI & Data · AI & Dev Tools · AI & Productivity ·
Big Tech · Big Tech & Electronics · Big Tech & Social ·
Crypto / Financial Services · Data & Credit · Dev Tools ·
Digital Goods & {Audio/Community/Design/Genealogy/Media/Music/Reading/Streaming} ·
E-commerce & {D2C/Luxury/Marketplace/Retail/Sports} · E-commerce Platform ·
EdTech & {Creator/Enterprise/K-12/Languages/Presentations/Subscriptions} ·
Enterprise Software & ERP · Fintech · Fintech & {BNPL/Banking/Credit/Cross-border/Crypto/FX/Investing/Remittances} ·
Gaming · Gaming & {Entertainment/Payments} · Health & Wellness · Health Tech ·
HR Tech / FinTech · Marketplace & {Local/Mobility/Real Estate/Resale/Retail/Services/Ticketing/Travel} ·
Media & {Entertainment/Streaming} · Mobile Payments / Marketplace · Mobility & EV ·
Nonprofit Tech / Donations · Payments & {Commerce/Fintech} ·
SaaS · SaaS & {Accounting/Analytics/Automation/Business/CRM/Communications/Design/Dev Tools/Enterprise/HR/Hospitality/Hosting/Infrastructure/Legal/Marketing/Payments/Productivity/Sales/Scheduling/Security/Support/Website Builder} ·
SaaS / FinTech · SaaS / Software ·
Social & Professional · Social / Dating ·
Travel & {Airlines/Corporate/Hospitality/Marketplace/Mobility/OTA}
```

If the merchant fits an existing bucket, use it verbatim. If it's a genuinely new vertical (very rare), invent one in the same `Category & Subcategory` form. Print your pick and reasoning.

## Pain titles — anchor to research, classify to taxonomy

Always 5 pain titles. Each one must be derived from something real you found about THIS merchant. Generic boilerplate ("Declines hurt revenue") is not allowed.

Each title should still **classify into one of the 7 taxonomy buckets** in `SlideDiagnostic.jsx` so the slide picks the right icon + fallback description. Buckets and their trigger keywords:

- **RESILIENCE** — `outage|downtime|availability|uptime|single.?point|resilience|failover`
- **CROSS-BORDER** — `cross.?border|fx|foreign|international|currency|non.?usd`
- **ROUTING** — `routing|orchestration|multi.?psp|single.?psp|acquirer|provider|processor|fragment|stack`
- **RECOVERY** — `churn|recurring|retry|subscription|lifetime|ltv|recovery`
- **AUTH RATE** — `decline|auth.?loss|auth.?rate|approval|success.?rate`
- **COVERAGE** — `apm|method|coverage|wallet|pix|upi|oxxo|local|localiz|card.?only|blik`
- **SECURITY** — `3ds|fraud|risk|chargeback|dispute|compliance|security|tokeniz`
- **OPERATIONS** — `reconcil|settle|finance|ledger|close|ops|operational`

Bake the keyword into the title organically. Example: "License-to-Cloud Subscription Transition at €21B Scale" hits RECOVERY via `subscription`. "Card Payments Enabled in Only 18 of 180 Countries" hits COVERAGE via `card`.

**Never append the bucket name in parentheses.** The Diagnostic slide renders the title text verbatim, so a literal `(CROSS-BORDER)` tag would show on the slide. The keyword must live inside the sentence ("...strains cross-border settlement"), never as a trailing label. Aim for variety across the 5 (don't stack three RECOVERY pains).

## PSPs — the rule

Walk this decision tree on the research output:

1. **2 or more PSPs confirmed publicly** (live checkout, official docs, press release, job listing with the PSP name) → use those PSPs only. No disclaimer. Set `psps_disclaimer = null`.
2. **Exactly 1 PSP confirmed** → use only that one. **Do NOT fill the second slot.** A single-PSP topology is itself a Yuno talking point — single-acquirer dependency. The slide will render only one chip, which is the intended signal. No disclaimer.
3. **Zero PSPs confirmed** → seed 2 region-appropriate enterprise providers and add the disclaimer. Region picks:
   - **EU / global enterprise** → Adyen + Stripe
   - **US-only or US-heavy** → Stripe + Braintree
   - **LATAM-heavy** → dLocal + Stripe
   - **APAC-heavy** → Airwallex + Adyen
   - **EMEA traditional (UK retail, banks)** → Worldline + Stripe
   - **Default if region unclear** → Stripe + Adyen
   - Disclaimer text (verbatim): `No public information on providers so assumptions were made`

PSP entries are objects: `{"name": "Adyen", "role": "EU · global acquirer"}`. Look up the canonical role for each PSP in `yuno-sales-pitch-maker/scripts/sql/psp-roles.json`. Default if not in the file: `"Regional · gateway"`.

## Missing methods — 10 entries, real markets

Pick 10 local payment methods the merchant likely doesn't accept yet but matters in markets they care about. Reference standard set: Pix (Brazil), Boleto (Brazil), OXXO (Mexico), UPI (India), iDEAL (Netherlands), SEPA Direct Debit (Germany), BLIK (Poland), Bizum (Spain), Konbini (Japan), PayNow (Singapore), PromptPay (Thailand), GoPay (Indonesia), DANA (Indonesia), WeChat Pay (China), Alipay (China). Filter to markets where the merchant actually does business (from research) — don't put Pix on a US-only merchant.

Format: `[{"market": "Brazil", "method": "Pix"}, ...]`.

## Capability cards — 4 fixed slots (CURRENT standard)

`capability_titles` is always exactly these 4, in order (these are the current names; the old "Smart Routing / Failover & Retries / Local Payment Methods / Unified Orchestration" set is retired):

1. `Smart Routing Engine`
2. `Failover + Recovery`
3. `1,000+ Local Methods`
4. `NOVA Fraud Intelligence`

`capability_descs` is 4 short paragraphs, each adapting Yuno's standard lever to a **verifiable fact** about THIS merchant (revenue, country count, user count, business model) plus the canonical Yuno proof point for that lever. No generic copy. The proof points (use verbatim phrasing):

1. **Smart Routing Engine** — per-transaction routing across PSPs by BIN, issuer and market; proof: "InDrive achieved 90% approval rates across 10 LATAM markets."
2. **Failover + Recovery** — automatic cascade + dunning on failed renewals; "up to 50% recovery on failed transactions"; proof: "Livelo recovered +5% approvals within 3 months."
3. **1,000+ Local Methods** — name 4-6 REAL local APMs for the merchant's actual markets (Pix Brazil, UPI India, OXXO Mexico, iDEAL Netherlands, BLIK Poland, GCash Philippines, etc.); one API, beyond card-only.
4. **NOVA Fraud Intelligence** — AI scoring on 5,000+ data points; "reduces false declines up to 75%"; proof: "McDonald's uses NOVA across LATAM markets."

These render on **SlideYunoSolve** (The Solve), whose card body clamps at `WebkitLineClamp: 5`. Keep each desc to ~2 sentences (roughly <=200 chars) so nothing ellipsizes. If a desc runs long, cut adjectives then a sentence, never invent.

## Business Overview entry — slide 2 data

**Always produce this entry** (it powers the "What we know about your business" slide, which is part of a complete deck). Append a new entry to `yuno-sales-pitch-maker/src/data/business-overviews.json` keyed by slug. Within the entry, every FIELD is independently optional — only include a field when the source is verifiable; omit (don't fabricate) the rest. Full shape:

```json
{
  "<slug>": {
    "revenue": {
      "amount": "15.02",        // string, decimal-pointed
      "unit": "B",              // "M" or "B"
      "currency": "USD",        // always USD
      "year": "FY24",           // fiscal year label
      "growth": "+2.2% YoY",    // optional
      "estimated": false,       // true when source is not a public filing
      "source": "10-K filed Mar 2025"
    },
    "description": "2-3 sentences anchored to verifiable numbers. Tight.",
    "catalyst": {
      "headline": "Take-private closed May 2025 in a $6.25B deal",
      "detail": "One sentence with counterparty, % stake, date."
    },
    "footprint": [
      { "value": "~34%", "label": "digital sales mix vs in-store" },
      { "value": "350+", "label": "stores in 32 US states" },
      { "value": "30", "label": "countries shipped to via ESW" }
    ],
    "countries": [
      { "name": "United States", "code": "us", "share": 0.94 }
    ],
    "countriesSource": "SimilarWeb",
    "apms": ["Apple Pay", "Google Pay", "PayPal", "Affirm"],
    "businessLines": ["Full-Line", "Rack", "Nordstrom.com"]
  }
}
```

Rules:
- Country `code` is ISO 3166 alpha-2 lowercase. Flags must exist at `public/flags/{code}.svg` — if a country code isn't in that folder, **download it from `https://raw.githubusercontent.com/HatScripts/circle-flags/gh-pages/flags/{code}.svg`** before adding the country to the entry.
- `share` is a decimal/fraction (0.94, not 94 or "94%"). **Gotcha:** SimilarWeb and most research report shares as percentages (e.g. 16.9). Divide by 100 before writing (16.9 → 0.169). Only include countries ≥ 0.01. Cap at top 10.
- `apms` is the non-card methods only. Cards (Visa/MC/Amex) are implicit; don't list them.
- `businessLines` **3-4 SHORT entries** (no long parentheticals/pricing). Long lines overflow and get cut off at the bottom of the slide (this bit DistroKid). Consolidate, e.g. "Annual subscription tiers (Basic / Pro / Mega)" as one line, not three.
- Any field you can't verify: **omit the key entirely**. The slide reflows.

After writing the JSON entry, no other file needs to change — `src/lib/supabase.js` already lifts the entry via `getBusinessOverview()` into `data.OVERVIEW`, and `SlideViewer.jsx` already filters the slide via `requiresDataField: 'OVERVIEW'` (so merchants without an entry skip it cleanly).

## Capabilities live — what the merchant has today

Array of strings from this fixed set: `payouts`, `subscriptions`, `tokenization`, `fraud`, `kyc`, `kyb`, `baas`. Tag a capability as `live` only if you found public evidence the merchant operates it today (e.g. "subscriptions" if they sell SaaS subscriptions, "fraud" if they mention 3DS or Stripe Radar in docs). The rest render as muted "missing/upsell" chips on the slide.

## Build mechanism — the helper scripts (recommended, fastest path)

The recent standard automates logo + local files + Supabase in one shot. Prefer this over hand-running each step.

1. Write two temp files:
   - `/tmp/{slug}.json` = `{ "slug", "name", "industry", "overview": {…the business-overviews entry…} }` (input for `_add-merchant.mjs`). **Divide country `share` by 100 here.**
   - `/tmp/{slug}-row.json` = the full Supabase row (slug, name, vertical:"merchant", auto_generated:true, industry, pain_titles, psps, psps_disclaimer, missing_methods, capability_titles, capability_descs, capabilities_live).
2. Ensure the service key is at `/tmp/.sbkey` (read it from `yuno-sales-pitch-maker/.env.local` → `SUPABASE_SERVICE_ROLE_KEY`, else recover from chat history per "Service-role key retrieval").
3. Run `bash scripts/_finish-merchant.sh {slug} {domain}` from the app root. It: fetches the logo from logo.dev for `{domain}`, normalizes it to white-on-transparent via `_logo-one.mjs` → `public/merchants/{slug}.png`, runs `_add-merchant.mjs` (prepends to `merchants.generated.js` MERCHANTS + MERCHANT_LIST, appends the CSV row, writes the `business-overviews.json` entry), then upserts the Supabase row. Expect `Supabase HTTP 201` (insert) or `200` (update).
4. Download any missing country flag SVGs (see Business Overview rules), `npm run build`, then commit + push.

If a merchant already exists (the existing-merchant check returned a row), `_add-merchant.mjs` skips the generated.js/CSV inserts automatically and only refreshes the overview; the Supabase upsert still updates the row.

## Logo processing (manual fallback)

If you are not using `_finish-merchant.sh` (e.g. the user dropped a logo in `Logos/`), process it with an inline node script using `sharp`. Mirror the `toWhiteOnTransparent` logic from `scripts/_logo-one.mjs` / `scripts/build-merchants.mjs`. Don't run `npm run build:merchants` — it wipes `public/merchants/` and rebuilds from a path that doesn't exist on this machine.

Write to `yuno-sales-pitch-maker/public/merchants/{slug}.png`. If the source PNG is already pre-processed (white-on-transparent), corner-subtraction can wipe it — fall back to a raw resize+trim.

## CSV update

Insert a new row in `yuno-sales-pitch-maker/public/merchants.csv` alphabetically:

```
{Company Name},1,{Industry},,,
```

Tier column is hardcoded to `1` because tiers are no longer relevant (per user 2026-05-04). The trailing empty columns are placeholders for future fields (PPT Link, etc.) — keep them.

## Manifest update

Edit `yuno-sales-pitch-maker/src/data/merchants.generated.js` directly (don't run `build:merchants`). Add the new merchant entry to BOTH:

1. The `MERCHANTS` object (alphabetical-ish slot, near similar merchants is fine).
2. The `MERCHANT_LIST` array.

Entry shape:

```json
{
  "name": "{Company Name}",
  "slug": "{slug}",
  "tier": "1",
  "industry": "{Industry}",
  "logo": "/merchants/{slug}.png",
  "logoMono": null,
  "matchedSlug": "{slug}"
}
```

## Supabase upsert

`POST` to the merchants table with `Prefer: resolution=merge-duplicates`. The full row shape:

```json
{
  "slug": "...",
  "name": "...",
  "pain_titles": ["...", "...", "...", "...", "..."],
  "psps": [{"name": "...", "role": "..."}],
  "psps_disclaimer": null | "No public information on providers so assumptions were made",
  "missing_methods": [{"market": "...", "method": "..."}, ...],
  "capability_titles": ["Smart Routing Engine", "Failover + Recovery", "1,000+ Local Methods", "NOVA Fraud Intelligence"],
  "capability_descs": ["...", "...", "...", "..."],
  "vertical": "merchant",
  "auto_generated": true,
  "industry": "...",
  "capabilities_live": ["subscriptions", "tokenization", "fraud"]
}
```

cURL pattern:

```bash
curl -s -X POST "https://mlwiosgalwsroisdkytl.supabase.co/rest/v1/merchants" \
  -H "apikey: $KEY" -H "Authorization: Bearer $KEY" \
  -H "Content-Type: application/json" \
  -H "Prefer: resolution=merge-duplicates,return=representation" \
  --data @/tmp/{slug}-row.json
```

Expect HTTP 201 (insert) or HTTP 200 (update via PATCH). Anything else = abort and surface the error.

## Build verify

Before committing, run `npm run build` in `yuno-sales-pitch-maker/` to make sure nothing broke. If `node_modules` doesn't exist, run `npm install` first. Build failure = abort, don't push broken code to main.

## Commit + push

```bash
cd /Users/germantatis/Desktop/GTMCoding/yuno-sales-pitch-maker
git add public/merchants.csv src/data/merchants.generated.js src/data/business-overviews.json public/merchants/{slug}.png public/flags/
git commit -m "feat: add {Company} merchant"
git push origin main
```

Note: stage `public/flags/` only if you downloaded a new flag SVG for this merchant (most existing top countries are already covered). The `git add public/flags/` line is a no-op when nothing changed there.

Use a HEREDOC for the commit body if you want to add detail. The body should mention: research highlights (revenue, geo), PSP source (confirmed vs. inferred), and any non-obvious decisions (e.g. "single-PSP topology preserved as Yuno talking point").

## Deploy verification

Poll `deck.yuno.tools` until the new bundle hash lands. Use `Bash` with `run_in_background: true` and an `until` loop:

```bash
until bundle=$(curl -s "https://deck.yuno.tools/m/{slug}" | grep -oE 'index-[A-Za-z0-9_-]+\.js' | head -1); \
  [ -n "$bundle" ] && curl -s "https://deck.yuno.tools/assets/$bundle" | grep -q "{Company Name}"; do
  echo "$(date +%H:%M:%S) bundle=$bundle waiting"
  sleep 30
done
echo "$(date +%H:%M:%S) DEPLOYED — {Company} live at deck.yuno.tools/m/{slug}"
```

Railway typical deploy: 4 to 8 minutes from push.

If the user reports the deploy isn't landing after ~10 minutes, push an empty commit to nudge the webhook:
```bash
git commit --allow-empty -m "chore: trigger Railway redeploy" && git push origin master:main
```

## Final report to the user

End your turn with a short summary:
- Slug, industry, mode
- Confirmed vs. inferred PSP count, disclaimer yes/no
- Pain title themes (e.g. "subscription churn, cross-border, single-PSP")
- Commit SHA + deploy URL `deck.yuno.tools/m/{slug}`

Format the URL as a clickable markdown link.

## Things NOT to do

- Don't run `npm run build:merchants` — it wipes `public/merchants/` and rebuilds from a hard-coded path that doesn't exist on this machine.
- Don't skip the Business Overview entry — a deck without the "What we know" slide is incomplete.
- Don't ship the retired capability titles ("Smart Routing / Failover & Retries / Local Payment Methods / Unified Orchestration"); use the current 4 (Smart Routing Engine / Failover + Recovery / 1,000+ Local Methods / NOVA Fraud Intelligence).
- Don't append "(BUCKET)" tags to pain titles — they render literally on the slide.
- Don't leave country `share` as a percentage; store it as a fraction (divide by 100).
- Don't let `businessLines` run long — keep 3-4 short entries or the slide overflows.
- Don't fabricate PSPs to "fill out" the topology to 4. Single-PSP merchants stay single-PSP.
- Don't put em-dashes in any copy you write to Supabase or to slides.
- Don't commit secrets. The service-role key never goes into a tracked file.
