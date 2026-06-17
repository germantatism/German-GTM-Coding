# /prioritizeaccounts — Account Prioritization by Buying Signals

SPEED TARGET: Complete in under 3 minutes. Follow the optimized flow below strictly.

## STEP 1 — Build the account pool (30 seconds max)

### A. Excel target accounts
Read the file `Target Accounts - NORAM Team.xlsx` from the project root directory.
From the sheet called "New Accounts", extract every row where the SDR column equals "German" (case insensitive).
Include all rows regardless of the value in the Contacted column.
For each row, capture: Company name, Industry/Vertical, Contacted status (True/False).

If the file is not found, stop and tell the user to place it in the project root.

### B. Previously suggested new accounts
Read the file `newaccounts_suggested.txt` from the project root directory.
If it exists, add those company names to the pool as well (treat them all as Contacted = False).
If it does not exist, skip this step.

### C. Pre-filter to top 30 candidates
From the full pool, select ~30 companies most likely to have recent news. Prioritize:
1. Well-known brands and public companies (more likely to have press coverage)
2. Companies in high-signal industries: AI, Gaming, iGaming, Sports Betting, SaaS, Airlines, Car Rental, Parking, Web Cloud Hosting, Cybersecurity & VPNs, Retail & E-Commerce
3. Mix of Contacted = False (preferred) and True
4. Ensure at least 2-3 companies per industry vertical for diversity
Skip tiny/obscure companies unlikely to have recent news coverage.

## STEP 2 — Search for buying signals (2 minutes max)

CRITICAL SPEED RULES:
- Do NOT use Agent tool or subagents. Search directly with WebSearch in the main thread.
- Use ONE search query per company: "[Company] funding acquisition payments executive news 2026"
- Run searches in PARALLEL batches of 10. Three rounds of 10 = 30 companies in ~90 seconds.
- Do NOT run 6 queries per company. One broad query is enough.

Signals to look for (in order of strength):

STRONG signals (high weight):
- Executive hire/departure: Head of Payments, VP Payments, CFO, CTO, CPO, CEO, COO
- Funding round announced (any stage)
- Acquisition, merger, or IPO announced
- PSP switch, payment provider change, or checkout redesign
- Payment outage, fraud incident, or decline rate issue

MODERATE signals:
- New country or market entry
- New product line, subscription tier, or app launch
- New fintech or payment partnership
- Job postings for payment, treasury, fraud, or fintech roles

MILD signals:
- LinkedIn headcount growth
- Major customer win or partnership
- Regulatory fine or compliance issue related to payments

## STEP 3 — Score each company

Score each company 1 to 10 based on signal strength and recency:

10: multiple strong signals, or a key payments decision maker just joined or left
7 to 9: one strong signal or two moderate signals
4 to 6: one mild or indirect signal
1 to 3: no signal found

Recency weighting:
- Signals from the last 30 days count at full weight
- Signals from 31 to 60 days ago count at 75% weight
- Signals from 61 to 90 days ago count at 50% weight

Never fabricate a signal. If nothing is found, give a low score and be honest.

## STEP 4 — Output the top 6

Return the 6 highest scoring companies. If scores are tied, prioritize companies where Contacted = False.

Rotate industries across the 6 results when scores are close (do not output 6 companies from the same vertical).

For each company, output exactly this format (plain text, no markdown, no dashes, no tables):

```
[Rank]. [Company name]
Industry: [vertical] | Status: [Contacted or Not contacted]
Urgency score: [X]/10
Signal: [One sentence. What happened and when.]
Why now: [One sentence. Why this signal opens a payments conversation.]
Source: [URL or publication name]
```

Separate each company with a blank line.

## RULES

- Only include real signals you can verify with a source
- Never fabricate a signal. If nothing is found for a company, give it a low score
- If fewer than 6 companies have signals, fill the remaining slots with the highest ICP fit companies and note "No recent signal found"
- Rotate industries across the 6 results when scores are close
- No markdown formatting, no tables, no dashes in the output
- Do not modify the Excel or any other file
- Do not confuse this with /prioritize (which is DB powered). This command reads directly from the Excel.
