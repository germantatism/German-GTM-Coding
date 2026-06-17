# /newaccounts — Find 5 New ICP-Fit Companies for Yuno

## STEP 1 — Load exclusion lists

### A. Excel master list
Read the file `Target Accounts - NORAM Team.xlsx` from the project root directory.
Extract ALL company names from the "New Accounts" sheet (every row, every rep, not just Germán's).
These are excluded. Never suggest any company that appears here.

If the file is not found, warn the user and proceed with only the suggested history file as exclusion.

### B. Previously suggested companies
Read the file `newaccounts_suggested.txt` from the project root directory.
If it exists, add every company listed there to the exclusion list.
If it does not exist, skip this step (it will be created at the end).

## STEP 2 — Search for new companies

Use web search to find real North American companies that fit Yuno's ICP.

Search across these verticals (rotate, do not pick 5 from the same one):
- AI
- SaaS
- Gaming
- iGaming
- Sports Betting
- Airlines
- Digital Products & Subscriptions
- Parking
- Car Rental
- Web Cloud Hosting
- Cybersecurity & VPNs
- Retail & E-Commerce

Run multiple web searches targeting different verticals. Example queries:
- "fastest growing AI companies US 2025 2026 series B C funding"
- "top SaaS companies North America high transaction volume"
- "digital parking companies US payments"
- "online gaming companies North America revenue growth"
- "sports betting operators US market share"
- "car rental companies US digital payments"
- "airline companies North America digital bookings"
- "web cloud hosting companies US payments subscriptions"
- "VPN cybersecurity companies US subscription revenue growth"
- "top retail e-commerce companies US high transaction volume global"
- "fastest growing DTC brands US e-commerce payments 2026"

### ICP criteria (ALL must apply):
1. Based in North America (US or Canada)
2. 100K+ digital transactions per month (or strong signals: high revenue, large user base, digital-first model)
3. Operating in one of the verticals listed above
4. Global or multi-market presence preferred
5. Already processing payments digitally
6. Mid-market to enterprise size

### Anti-ICP (auto-exclude):
- Very low digital transaction volume
- Pure brick-and-mortar with no digital payments
- Already in the Excel exclusion list
- Already in newaccounts_suggested.txt

## STEP 3 — Output format

Return exactly 5 companies. Plain text, no markdown tables, no dashes.

For each company:

```
Company: [Name]
Website: [URL]
Industry: [Vertical]
HQ: [City, Country]
Why ICP: [One sentence explaining why they fit: volume signal, PSP complexity, global presence, or APM gap]
```

Separate each company with a blank line.

Rules:
- Only real, verifiable companies (must exist, must have a real website)
- No companies from the exclusion lists
- Rotate across verticals: at least 3 different industries in each batch of 5
- Prioritize companies likely to have PSP complexity, cross-border volume, or APM gaps
- Plain text only, no formatting

## STEP 4 — Save to history

After outputting the 5 companies, append them to `newaccounts_suggested.txt` in the project root.

Format in the file (one company per line, with date):
```
[YYYY-MM-DD] Company Name | Vertical
```

This ensures no company is ever suggested twice across sessions.
