---
description: Build a 10-slide Monthly Business Review deck for any Yuno merchant
argument-hint: <merchant> <month YYYY>
model: opus
---

# MBR Builder

Builds a full 10-slide Monthly Business Review deck for any Yuno merchant.

## Usage

```
/mbr-builder [MERCHANT] [MONTH YYYY]

Examples:
  /mbr-builder "Smiles Argentina" "February 2026"
  /mbr-builder ZigFun "March 2026"
  /mbr-builder Rappi "January 2026"
```

## What it builds

| Slide | Content |
|-------|---------|
| 1 | Cover |
| 2 | Monthly Overview — KPIs + MoM comparison + 3 mini charts |
| 3 | Weekly Volume — weekly table + combo bar/line chart |
| 4 | Provider Breakdown — table + donut + AR bar chart |
| 5 | Card Performance — table + horizontal bar charts |
| 6 | Top Decline Reasons — Pareto chart |
| 7 | Declines by Provider — stacked horizontal bar |
| 8 | Refunds — KPI tiles + provider table |
| 9 | Improvement Suggestions & Opportunities — 2x3 card grid |
| 10 | Next Steps — 5 action items (reference template layout) |

## Data source

- **Metabase**: `ABSTRACT.CALCULATED_TRANSACTIONS` (Snowflake PROD, db=2)
- Auth: `x-api-key` header with API key from `~/.openclaw/secrets/metabase.env`
- Org filter: `ORGANIZATION_CODE = '<org_code>'`
- Key fields: `PAYMENT_CODE`, `TRANSACTION_STATUS`, `AMOUNT_USD`, `PROVIDER_ID`, `CARD_TYPE`, `CARD_BRAND`, `RESPONSE_MESSAGE`, `TRANSACTION_CATEGORY`, `IS_TPV`

## Key lessons learned (do not change these patterns)

### Table styling — CRITICAL

Always use **separate requests** for background and text:

```python
# CORRECT — separate requests
reqs.append({"updateTableCellProperties": {
    "objectId": oid,
    "tableRange": {...},
    "tableCellProperties": {
        "tableCellBackgroundFill": {"solidFill": {...}}
    },
    "fields": "tableCellBackgroundFill"   # background ONLY
}})
reqs.append({"updateTextStyle": {...}})
reqs.append({"updateParagraphStyle": {...}})

# WRONG — contentAlignment in same request silently kills background change
reqs.append({"updateTableCellProperties": {
    "tableCellProperties": {
        "tableCellBackgroundFill": {...},
        "contentAlignment": "MIDDLE"       # this breaks it
    },
    "fields": "tableCellBackgroundFill,contentAlignment"
}})
```

### Table color scheme

```python
HDR_BG  = "#E8EAF5"  # Yuno lilac header
HDR_FG  = "#282A30"  # dark text, bold
COL0_BG = "#000000"  # black first column
COL0_FG = "#FFFFFF"  # white text
DATA_BG = "#FFFFFF"  # white data cells
DATA_FG = "#282A30"  # dark text
```

### Fill table cells in REVERSE order

Always process cells last-to-first (reverse row and col loops) to avoid index shift bugs when using `insertText`.

### Next Steps slide layout

Based on template from `1uX0IrZEZ7paXR1Jd9E1iHm3h3ickEysxXS18FkBYMUA` slide 2:
- Card: `ROUND_RECTANGLE`, no fill, `#BDC3F5` border (1pt)
- Left accent bar: 4pt wide, `#3E4FE0` blue
- Number circle: `ELLIPSE` at x=898pt, 36x36pt, blue fill with white number
- The slide template already has the blue left line built in — do NOT add another one
- `START_Y = 106pt`, `CARD_H = 75pt`, `GAP = 9pt` (fits 5 cards in 540pt height)

### Google Slides API notes

- Always pass `supportsAllDrives=True` on all Drive API calls
- Slide template ID: `1PQS7NWcqkfC9_tQqV1mi5wuRm6GLebnhscQp8iXprQ0`
- Yuno Drive folder: `1KF9BrNkMOqFztPcmrKKs4TYUB-qSLoWx`
- Chart workflow: matplotlib PNG → upload to Drive (public reader) → `createImage` in Slides
- Label intercept fix: always `ylim/xlim = max * 1.25-1.30` so labels never clip

## Files

- `build_mbr.py` — main build script (Smiles Feb 2026 as reference)
- `utils.py` — reusable helper functions (table styling, shapes, charts)

## Step-by-step

### Step 1 — Parse Intent
Extract from $ARGUMENTS:
- `merchant_name`
- `month` and `year`
- Resolve `org_code` from merchant name (check local files or Salesforce)

### Step 2 — Query Metabase
Pull transaction data for the merchant + month from `ABSTRACT.CALCULATED_TRANSACTIONS`.
Also pull prior month for MoM comparison.

### Step 3 — Build Data Dict
Structure all data into the standard schema expected by `build_mbr.py`.

### Step 4 — Generate Charts
Use matplotlib with Yuno palette to create:
- MoM comparison bar charts (slide 2)
- Weekly volume combo chart (slide 3)
- Provider donut + AR bar chart (slide 4)
- Card performance horizontal bars (slide 5)
- Decline reasons Pareto chart (slide 6)
- Declines by provider stacked bar (slide 7)

Upload PNGs to Drive folder `1KF9BrNkMOqFztPcmrKKs4TYUB-qSLoWx`.

### Step 5 — Build Slides
Copy template, populate all 10 slides with data + charts.
Return the Google Slides URL.

## Output

```
[Merchant] [Month YYYY] MBR deck ready!
Link: https://docs.google.com/presentation/d/{id}/edit
Charts generated: 6
Slides: 10
Built in Xs
```
