---
description: Build a Yuno-branded presentation deck in Google Slides
argument-hint: <merchant> <period> [qbr|brief]
model: opus
---

# Slide Builder

Builds a polished, Yuno-branded deck from any data source and returns a Google Slides link.

| Format | Audience | Slides | Charts | Flag |
|--------|----------|--------|--------|------|
| `qbr` | External — the merchant | 12 slides | Matplotlib | `--mode merchant` |
| `brief` | Internal — Yuno leadership | 9 slides | Tables & KPI cards only | `--mode exec --no-charts` |

---

## How to Trigger

```
/slide-builder [merchant] [period] [format?]

Examples:
  /slide-builder ZigFun "February 2026"
  /slide-builder ZigFun "February 2026" qbr
  /slide-builder "Smiles Argentina" "Q1 2026" brief
  /slide-builder Rappi "March 2026" qbr
```

- Format omitted → default to `qbr`
- `brief` → runs exec mode with `--no-charts`

---

## Step 1 — Parse Intent

Extract from $ARGUMENTS:
- `merchant_name` — e.g. "ZigFun", "Smiles Argentina"
- `period` — e.g. "February 2026", "Q1 2026"
- `format` — "qbr" (default) | "brief"
- `account_manager` — pull from Salesforce or local files

Map to builder flags:
- `qbr` → `--mode merchant`
- `brief` → `--mode exec --no-charts`

---

## Step 2 — Gather Data

Run all applicable tracks **in parallel**.

### 2a. Local Files (always — check first)

Search for merchant-related files:
```
~/Downloads/*{merchant}*
~/Documents/*{merchant}*
/tmp/*{merchant}*
```
Look for:
- **Account Plan** (.xlsx) → ARR, contacts, opportunities, risks, share of wallet
- **Performance CSVs** → transaction volumes, AR%, providers, decline reasons
- **Previous decks** (.pptx) → historical context, prior commitments
- **Project trackers** → implementation status, open actions, blockers

Extract and structure all relevant numbers.

### 2b. Salesforce (if accessible)

Query for the merchant account:
- ARR / MRR
- Contract start + renewal dates
- Health score (Green / Yellow / Red)
- Account Manager name
- Open tickets or escalations
- Recent activity notes

### 2c. Metabase / Snowflake (QBR format — core transaction data)

Pull for merchant + period:

```
OVERVIEW
- Total transactions, Approved transactions
- Approval Rate % = approved / total * 100
- TPV (Total Payment Volume) in USD
- Same metrics for prior period (MoM comparison)

WEEKLY_VOLUME
- Per ISO week: label, total tx, approved tx, AR%, TPV

PROVIDERS
- Per provider: name, total tx, approved tx, AR%, share%, TPV

CARD_PERFORMANCE
- Per card type + brand: type (Credit/Debit), brand, total tx, approved tx, AR%

DECLINE_REASONS
- Per reason: label, count, % of total declines, cumulative %
- Classification: "Recoverable" | "Fix Bug" | "Not recoverable"
- Take top 10 by count

DECLINES_BY_PROVIDER
- Per provider: top 3 decline reasons with counts

REFUNDS
- Total refunds, succeeded, refund rate %, refunded amount USD
- Per provider: refund count, succeeded, amount USD
```

### 2d. Gong (brief / exec format only)

Summarize last 2 calls with this merchant:
- Key themes discussed
- Open issues or commitments made
- Sentiment (positive / neutral / at-risk)

---

## Step 3 — Build DATA Dict

Assemble all gathered data into the standard schema:

```python
DATA = {
    "merchant": {
        "name": str,               # "Smiles Argentina"
        "period": str,             # "Q1 2026"
        "account_manager": str,    # "Tania"
        "mode": str,               # "merchant" | "exec"
        # exec/brief extras:
        "arr_usd": float,
        "contract_start": str,
        "contract_renewal": str,
        "health_score": str,       # "Green" | "Yellow" | "Red"
        "gong_summary": str,       # optional
    },
    "overview": {
        "total_tx": int,
        "approved_tx": int,
        "approval_rate": float,    # e.g. 82.46
        "tpv_usd": float,
        "prev_total_tx": int,
        "prev_approved_tx": int,
        "prev_approval_rate": float,
        "prev_tpv_usd": float,
        "tpv_delta_pct": float,    # positive = growth
        "ar_delta_pp": float,      # positive = improvement
    },
    "weekly_volume": [
        {"week": str, "total": int, "approved": int, "ar_pct": float, "tpv": float}
    ],
    "providers": [
        {"name": str, "total": int, "approved": int, "ar_pct": float,
         "share_pct": float, "tpv": float}
    ],
    "card_performance": [
        {"type": str, "brand": str, "total": int, "approved": int, "ar_pct": float}
    ],
    "decline_reasons": [
        {"reason": str, "count": int, "pct": float, "cumul_pct": float,
         "classification": str}
    ],
    "declines_by_provider": [
        {"provider": str, "reasons": [{"reason": str, "count": int}]}
    ],
    "refunds": {
        "total": int, "succeeded": int, "rate_pct": float, "amount_usd": float,
        "by_provider": [
            {"provider": str, "count": int, "succeeded": int, "amount_usd": float}
        ]
    },
    "recommendations": [
        {
            "tag": str,    # "fix" | "critical" | "optimize" | "grow" | "expand"
            "title": str,
            "body": str
        }
    ],
    "next_steps": [
        {
            "action": str,
            "owner": str,    # "Yuno" | "Merchant" | "Joint"
            "target": str,
            "priority": str  # "Critical" | "High" | "Medium"
        }
    ],
}
```

If any field is unavailable, use `0`, `""`, or a clear placeholder.
**Never omit a field** — the builder will raise a KeyError.

---

## Step 4 — Synthesize Insights

Before building, derive 3 insight categories to populate the Executive Summary slide:

**Key Wins**
- Best-performing provider(s) by AR%
- TPV growth vs prior period
- Any metric that beat benchmark or target
- Recently launched features or APMs

**Critical Issues**
- Providers / card types with AR% significantly below average
- Any decline reason > 10% of total declines
- "Fix Bug" classifications with high volume
- Integration blockers or escalations

**Opportunities**
- APMs with above-avg AR but low volume (promote)
- Upsell: Monitors, Anti-fraud, 3DS, new payment methods
- Wallet adoption (Apple Pay / Google Pay) where AR% is higher
- Volume migration from underperforming providers

---

## Step 5 — Run Builder

```bash
# QBR format (with charts)
python3 ~/Downloads/qbr_builder.py \
  --data "$(cat /tmp/merchant_data.json)" \
  --mode merchant

# Executive Brief (no charts)
python3 ~/Downloads/qbr_builder.py \
  --data "$(cat /tmp/merchant_data.json)" \
  --mode exec \
  --no-charts
```

Or from Python:
```python
from qbr_builder import build_qbr_deck

# QBR with charts
url = build_qbr_deck(DATA, mode="merchant")

# Executive brief, no charts
url = build_qbr_deck(DATA, mode="exec", no_charts=True)

print(f"Deck ready: {url}")
```

---

## Slide Structure

### QBR Format — `merchant` mode (12 slides)

| # | Slide | Key content |
|---|-------|------------|
| 1 | **Cover** | Merchant name, period, AM name |
| 2 | **Agenda** | 9-item section list |
| 3 | **Executive Summary** | 3-col: Wins / Issues / Opportunities + 3 KPIs |
| 4 | **Monthly Overview** | 4 KPI cards + MoM comparison bar chart |
| 5 | **Weekly Volume** | Grouped bar + AR% line chart + table |
| 6 | **Provider Breakdown** | Horizontal AR% bar chart + provider table |
| 7 | **Card Performance** | Dual chart (Tx by type + AR% by type) + table |
| 8 | **Top Decline Reasons** | Pareto chart (vertical bars + cumul% line) + table |
| 9 | **Declines by Provider** | Provider-level decline breakdown table |
| 10 | **Refunds** | 3 KPI cards + provider refund table |
| 11 | **Improvement Opportunities** | Tagged recommendation cards (2x3 grid) |
| 12 | **Next Steps** | Action table with owner + priority + timeline |

### Executive Brief — `exec` mode, no charts (9 slides)

| # | Slide | Key content |
|---|-------|------------|
| 1 | **Cover** | "Executive Review" subtitle |
| 2 | **Agenda** | Exec-audience topic list |
| 3 | **Executive Summary** | Wins / Issues / Opportunities + 3 KPIs |
| 4 | **Commercial Overview** | ARR, health score, contract status, Gong themes |
| 5 | **Performance Summary** | 4 KPI cards + provider + card metrics tables |
| 6 | **Provider Health** | AR% + share table, top decline per provider |
| 7 | **Revenue Opportunities** | Opportunities framed as growth levers |
| 8 | **Strategic Next Steps** | Joint roadmap action table |
| 9 | **Closing** | Yuno closing slide |

---

## Design Rules

| Rule | Detail |
|------|--------|
| Template | Copy of `1PQS7NWcqkfC9_tQqV1mi5wuRm6GLebnhscQp8iXprQ0` |
| Heading color | YUNO_BLUE `#3B4BF9` — never black |
| Charts | Matplotlib with Yuno palette; uploaded to Drive `1KF9BrNkMOqFztPcmrKKs4TYUB-qSLoWx` |
| Tables | min 10.5pt body, 11pt header, proportional column widths (min 406 400 EMU) |
| KPI cards | HARMONY_LILAC bg, YUNO_BLUE number, delta with trend arrow |
| Rec. tags | `fix` (black), `optimize` (blue), `grow` (periwinkle), `critical` (dark navy) |
| Brief mode | All chart inserts skipped; slide space used by expanded tables / KPI cards |

---

## Output

```
[Merchant] [Period] [Format] deck ready!
Link: https://docs.google.com/presentation/d/{id}/edit
Charts generated: 5     (or: "No charts — brief mode")
Slides: 12              (or: 9 for brief)
Built in Xs
```

If any data source is unavailable, generate the slide with placeholder text and note the gap.

---

## Troubleshooting

| Error | Fix |
|-------|-----|
| `column width must be at least 406400 EMU` | `smart_col_widths()` auto-clamps — verify table width vs column count |
| `createImage` 400 error | Drive file not shared publicly — `_save_upload()` sets `anyoneWithLink` |
| `KeyError: 'agenda'` | Template slide `p53` not found; check `TMPL_AGENDA` constant |
| Chart colors wrong | Check `CLASSIFICATION_COLORS` in `chart_helpers.py` |
| Slides in wrong order | Build must use `reversed(slide_defs)` due to `duplicateObject` behavior |
| `--no-charts` has no effect | Ensure `no_charts=True` is passed through to `_generate_charts()` |
