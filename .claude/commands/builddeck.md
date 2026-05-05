# /builddeck — End-to-end deck build for a new merchant

You're building a complete merchant entry for **$ARGUMENTS** on `deck.yuno.tools`. End-to-end: research → Supabase row → CSV/manifest → logo → commit → push → deploy verification. Single command, no manual handoffs except the user dropping the logo PNG/SVG into the `Logos/` folder beforehand.

## Inputs

- **Required (positional):** the company name (everything before any `--flag`).
- **Optional flags:**
  - `--mode banking` — pitch mode targeting banks. Affects slide 3 framing only (different `CAPABILITY_DEFS_BANKING` set already wired into `SlideDiagnostic.jsx`).
  - `--mode partner` — partner-pitch framing.
  - `--industry "Industry & Subcategory"` — override auto-detected industry. Must be a value already used in `public/merchants.csv` or follow the same convention.

If no flag is passed, default mode is `merchant` (the standard Yuno-vs-merchant pitch).

## Hard constraints — read every time

These are not negotiable. They come from prior decisions and are documented in the user's auto-memory:

1. **Auto commit + push at the end.** Never stop at "wrote the files." Run `git add` → `git commit` → `git push origin master:main`. The remote branch is `main`, not `master`. The local working branch is `master` in this repo (yes, asymmetric — that's the actual setup). Source of truth: `feedback_auto_commit_push.md`.
2. **Never put false information.** When a fact (especially PSPs) isn't publicly verifiable, follow the disclaimer rule below. Source: `feedback_no_false_info_disclaimer.md`.
3. **Never use the phrase "no small feat"** anywhere in capability copy or pain titles. Source: `feedback_no_small_feat.md`.
4. **Em-dashes (`—`) are banned in body copy** per the deck's design principles. Use commas or restructure. Pain titles, capability descs, and the disclaimer text all count as body copy. Source: `DESIGN.md`.

## Pre-flight checks

Before doing anything else:

1. **Logo exists.** Look in `/Users/germantatis/Desktop/GTMCoding/yuno-sales-pitch-maker/Logos/` for any file matching the company name (case-insensitive substring). Accept `.svg`, `.png`, `.webp`, `.jpg`. If multiple, prefer SVG > PNG > WEBP > JPG. If nothing found, abort with a clear message: "Logo not found. Drop a PNG/SVG of the {Company} logo into `yuno-sales-pitch-maker/Logos/` and re-run."
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

Use `WebSearch` and `WebFetch` in parallel where possible. Cap at ~8 searches total. The research only powers the Supabase row fields, so don't go overboard — this isn't `/research`. Targets:

- **Headline financials**: latest annual revenue, growth rate, public/private, geographies of operation. Source: 10-K / 20-F if public, latest earnings release if recent. Verifiable numbers go into capability descs as anchors.
- **Geographic footprint**: which markets they serve, where their cloud/SaaS revenue is shifting toward, where they don't have local methods. This drives `missing_methods` and the local-payment-method capability copy.
- **Payment stack signals**: search for "{company} Stripe Adyen Worldpay Braintree Checkout.com payment processor", "{company} payment gateway", "{company} job listings payments engineer", "{company} press release fintech partnership". Look at official help pages, T&Cs, dev docs, job boards, SEC filings, press releases. Tag confirmed (live checkout, official docs, press release) vs. inferred (job posting alone, third-party article). If the company runs a help page describing how customers pay them, that's gold.
- **Business model**: subscription, transactional, marketplace? Shapes `capabilities_live` (subscriptions, tokenization, fraud, payouts, kyc, kyb, baas).
- **Pain points the merchant is publicly known to have**: complaints on Reddit/Trustpilot/community forums about declined cards, double charges, refunds, missing local methods, billing failures. These become real, verifiable pain titles.

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

## Capability cards — 4 fixed slots

`capability_titles` is always exactly these 4, in order:

1. `Smart Routing`
2. `Failover & Retries`
3. `Local Payment Methods`
4. `Unified Orchestration`

`capability_descs` is 4 paragraphs of 2-4 sentences each. Each desc must reference at least one **verifiable fact** about the merchant (revenue figure, country count, growth rate, specific product line) — no generic copy. Anchor to numbers from the research. Example for SAP capability 1: "Per-transaction routing across acquirers by card BIN, issuer, and market. With €21B in cloud subscription revenue (+26% YoY) across 180+ countries, lifting auth rates 3 to 10% on cloud renewals translates to hundreds of millions in recovered ARR annually."

## Capabilities live — what the merchant has today

Array of strings from this fixed set: `payouts`, `subscriptions`, `tokenization`, `fraud`, `kyc`, `kyb`, `baas`. Tag a capability as `live` only if you found public evidence the merchant operates it today (e.g. "subscriptions" if they sell SaaS subscriptions, "fraud" if they mention 3DS or Stripe Radar in docs). The rest render as muted "missing/upsell" chips on the slide.

## Logo processing

Inline node script using `sharp` (a dep of the project). Mirror the `toWhiteOnTransparent` logic from `scripts/build-merchants.mjs`. Don't run `npm run build:merchants` — it wipes `public/merchants/` and rebuilds from Isabella's desktop folder, which doesn't exist on this machine.

Inline script writes to `yuno-sales-pitch-maker/public/merchants/{slug}.png`. If the source PNG is already pre-processed (white-on-transparent, e.g. some brand kits ship that way), the corner-subtraction can wipe it — fall back to a raw resize+trim in that case.

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
  "capability_titles": ["Smart Routing", "Failover & Retries", "Local Payment Methods", "Unified Orchestration"],
  "capability_descs": ["...", "...", "...", "..."],
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
git add public/merchants.csv src/data/merchants.generated.js public/merchants/{slug}.png
git commit -m "feat: add {Company} merchant"
git push origin master:main
```

Use a HEREDOC for the commit body if you want to add detail. The body should mention: research highlights (revenue, geo), PSP source (confirmed vs. inferred), and any non-obvious decisions (e.g. "single-PSP topology preserved as Yuno talking point").

## Deploy verification

Poll `deck.yuno.tools` until the new bundle hash lands. Use `Bash` with `run_in_background: true` and an `until` loop:

```bash
until bundle=$(curl -s "https://deck.yuno.tools/m/{slug}" | grep -oE 'index-[A-Za-z0-9]+\.js' | head -1); \
  curl -s "https://deck.yuno.tools/assets/$bundle" | grep -q "{Company Name}"; do
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
- Don't push to `master` on the remote — that branch is stale ("Initial commit"). Only `main` deploys.
- Don't fabricate PSPs to "fill out" the topology to 4. Single-PSP merchants stay single-PSP.
- Don't put em-dashes in any copy you write to Supabase or to slides.
- Don't commit secrets. The service-role key never goes into a tracked file.
