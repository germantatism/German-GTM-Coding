---
description: Build a Business Case Excel for any prospect company
argument-hint: <company name>
model: opus
---

# Business Case Builder — Yuno Payment Orchestrator

Generates a full Business Case Excel file (same structure as the Canva BC template) for **$ARGUMENTS**.

---

## Step 0 — Parse & Validate

Extract `company_name` from $ARGUMENTS. If empty, ask the user for the company name.

---

## Step 1 — Collect SimilarWeb Data from User

Ask the user for the following inputs (do NOT proceed without them):

1. **Annual Total Visits** (from SimilarWeb)
2. **Countries and Traffic Share (%)** — can be a screenshot, table, or text list
3. **Which regions to include** — or say "all" for auto-detection from traffic data

Tell the user:
> I need the SimilarWeb traffic data to build the BC. Please share:
> 1. Annual total visits
> 2. Countries + traffic share % (screenshot or list)
>
> I'll handle the rest — research, calculations, and Excel generation.

Wait for the user's response before proceeding.

---

## Step 2 — Research (parallel agents)

Once you have the SimilarWeb data, run a `/research` on the company to gather:
- Annual Revenue (estimate from public sources, Crunchbase, reports)
- Industry classification
- Legal entities / local offices per country
- PSP/payment stack (Stripe, PayPal, Adyen, etc.)
- Current APMs at checkout per market
- Average Transaction Value (ATV) per market
- Any payment-related complaints or issues

Launch 3 agents in parallel:

### Agent 1 — Company Profile & Financials
- What the company does, industry, business model
- Annual revenue (actual or estimated)
- Funding, employee count
- Legal entities by country (Companies House, OpenCorporates, SEC, LinkedIn, T&Cs)

### Agent 2 — Payment Stack & Checkout
- PSPs/acquirers used
- Payment methods available at checkout per market
- Checkout UX (guest checkout, mobile, BNPL)
- Payment complaints (Reddit, Trustpilot)

### Agent 3 — Market & Product Context
- ATV estimates per market/region
- Business model (subscription, one-time, marketplace)
- Competitor payment approaches
- Recent news or expansion

**CRITICAL**: Only use data about the target company. Do NOT mix in competitor data.

---

## Step 3 — Determine Regions & Countries

From the SimilarWeb traffic data, group countries into max 4 regions with max 5 countries each:

| Region | Typical Countries |
|--------|-------------------|
| **NA** | United States, Canada, Mexico (if >1.5% traffic) |
| **EMEA** | UK, Spain, Germany, France, Netherlands, Italy, Poland, etc. |
| **LATAM** | Brazil, Mexico, Colombia, Argentina, Peru, Chile, etc. |
| **APAC** | Australia, India, Japan, Singapore, Indonesia, Philippines, etc. |

Rules:
- Only include countries with >1% traffic share
- Max 5 countries per region
- A country goes to the region where it geographically belongs (Mexico → LATAM if LATAM exists, otherwise NA)
- If a region has only 1 country with <2% traffic, skip that region

---

## Step 4 — Set Industry Benchmarks

Read **all** BC sheets in the `Business Cases/` folder (Canva, SendOwl, Pulsz, HelloFresh, Gett, Cloudflare, Figma, Peloton, Bumble, UPS, Hostelworld, EA, Microsoft, and any others present) to understand how existing BCs are structured and what values they use. Use the "Aceptance Rate Delta per Indust" sheet from any of them to get benchmarks for the company's industry:

| Metric | Use |
|--------|-----|
| Δ acceptance rate (Lower/Higher) | Per-country acceptance rate improvement |
| Local MDR | MDR for countries with local entity |
| Cross-Border MDR | MDR for countries without local entity |
| Take Rate (Lower/Higher) | Revenue-to-TPV ratio |
| VtC (%) | View to Checkout conversion |
| CtS (%) | Checkout to Success conversion |

If industry not found in the table, use the closest match and note it.

---

## Step 5 — Define Per-Country Inputs

For each country, determine these SDR inputs:

### 5A. From Research:
| Input | How to Determine |
|-------|-----------------|
| **ATV** | Research average transaction value for the company's product/service in each market. Adjust by purchasing power. |
| **Local Entity?** | From Agent 1 research. Yes/No per country. |
| **Current APMs** | From Agent 2 checkout research. Count of APMs currently available. |
| **APMs to Integrate** | From the APMs reference sheet — which crucial local APMs are missing? |

### 5B. Derived from Current APMs:
| Input | Logic |
|-------|-------|
| **SoW Cards (%)** | If 0 APMs → 100%. If 1-2 APMs → 88-95%. If 3+ APMs → 75-85%. Adjust by market APM adoption. |
| **SoW APMs (%)** | = 1 - SoW Cards |
| **(%) Incremental Transactions** | Crucial APMs (Pix, UPI, Bizum, iDEAL): 8-12%. Less relevant: 2-4%. |
| **(%) TPV from Cards to APMs** | Crucial APMs: 4-5%. Less relevant: 1-2.5%. |
| **Δ Acceptance Rate** | Local entity: use lower range. No entity: use higher range. |

### 5C. MDR Logic:
| Scenario | Current MDR | Reduction | New MDR |
|----------|-------------|-----------|---------|
| Has local entity | Local MDR from benchmarks | -0.2% | Local MDR - 0.2% |
| No local entity | Cross-Border MDR from benchmarks | -1.0% | Cross-Border MDR - 1.0% |

### 5D. Engineering/Dev Inputs:
| Input | Standard Value |
|-------|---------------|
| Time to integrate +1 APM | 3 months |
| Time to integrate +1 PSP | 4 months |
| Cost per integration/month | $21,600 |
| Yuno integration time | 2 months |
| MoR/Processors to integrate (no entity) | 2 |
| MoR/Processors to integrate (has entity) | 1 |
| Need MoR? | Yes if no local entity |

### 5E. APM Selection — Use Reference Data

Before recommending APMs per country, **always read the "APMs" tab** from the BC sheets in `Business Cases/` (any of them — the APMs tab is the same reference data). This tab lists the most popular/relevant APMs per country. Use it as the primary source to decide which APMs to recommend integrating in each market. Only recommend APMs that appear as relevant for that country in the reference tab.

### 5F. APMs MDR Cost: 0.012 (1.2%) — standard across all markets

---

## Step 6 — Calculate Everything

For each country, calculate the full Pay-ins sheet:

```
Visits = Annual_Total_Visits × SoW_traffic
Successful_Transactions = Visits × Conversion (0.06)
TPV = Transactions × ATV
TPV_Cards = TPV × SoW_Cards
TPV_APMs = TPV × SoW_APMs

-- Cards Section --
Incremental_TPV = TPV_Cards × Δ_Acceptance_Rate
Incremental_Revenue = Incremental_TPV × Take_Rate
Annual_Cards_TPV = TPV_Cards + Incremental_TPV
MDR_Reduction_Savings = Annual_Cards_TPV × |MDR_Reduction|
Cards_Benefit = Incremental_Revenue + MDR_Reduction_Savings

-- APMs Section --
APMs_Incremental_TPV = TPV × Pct_Incremental_Transactions
APMs_Incremental_Revenue = APMs_Incremental_TPV × Take_Rate
APMs_Shifted_TPV = TPV × Pct_Cards_to_APMs
APM_MDR_Savings = APMs_Shifted_TPV × (Cards_MDR - APMs_MDR_Cost)
APMs_Benefit = APMs_Incremental_Revenue + APM_MDR_Savings
```

For each region, calculate the Devs/Eng sheet:
```
Total_APMs_to_Integrate = sum across countries
APM_Cost = Total_APMs × Time_per_APM × Cost_per_Month
Total_MoRs = sum across countries
PSP_Cost = Total_MoRs × Time_per_PSP × Cost_per_Month
Total_Eng_Savings = APM_Cost + PSP_Cost
Total_Months = (APMs × 3) + (MoRs × 4) per country, summed
Time_Saved = Total_Months - Yuno_Integration_Months
```

RESUMEN totals:
```
TPV_Acceptance_Rate_Uplift = sum of all Incremental_Revenue across regions
Fee_Renegotiation = sum of all MDR_Reduction_Savings across regions
New_APM_Growth = sum of all (APMs_Incremental_Revenue + APM_MDR_Savings) across regions
Engineering_Savings = sum of all Total_Eng_Savings (in millions)
Total_Benefit = sum of all above
```

---

## Step 7 — Generate Excel

Use Python with `openpyxl` to create the Excel file with these sheets:

1. **RESUMEN** — Company info, key inputs, total benefits, problems identified
2. **BC Pay-ins NA** — (if applicable)
3. **BC Pay-ins EMEA** — (if applicable)
4. **BC Pay-ins LatAm** — (if applicable)
5. **BC Pay-ins APAC** — (if applicable)
6. **BC Devs.Eng NA** — (if applicable)
7. **BC Devs.Eng EMEA** — (if applicable)
8. **BC Devs.Eng LatAm** — (if applicable)
9. **BC Devs.Eng APAC** — (if applicable)
10. **Current Payment Methods** — For each country, list the payment methods the company currently offers (from Agent 2 checkout research). This sheet is mandatory and must always be included.

Save to: `BC sheets - {company_name}.xlsx` in the project root.

### RESUMEN Problems (adapt to company):
| Problem | Description |
|---------|-------------|
| PROBLEM 1 | Dependencies on [primary PSP] |
| PROBLEM 2 | No fallbacks or smart routing |
| PROBLEM 3 | High transactional costs (cross-border) |
| PROBLEM 4 | Need of APMs to increase sales in key markets |
| PROBLEM 5 | Reconciliation complexity across multiple gateways |

---

## Step 8 — Present Slide Content (Slides 4–7)

After completing the research (Step 2), present the content for slides 4–7 as text in the chat. The user will copy this into the PowerPoint template.

**Before writing**, read the existing BC PowerPoints in `Business Cases/` (Canva, Patreon, Runway, SendOwl, Suno, The Economist, and any others) to match the tone and level of detail.

### Writing rules

1. **No dashes.** Never use em dashes, en dashes, or hyphens as punctuation. Rewrite the sentence instead.
2. **Short and concise.** Every sentence must earn its place. Cut filler words. Be direct.
3. **Use ALL the research.** Incorporate specific data points: revenue, TPV, member counts, settlement amounts, PSP names, complaint sources, funding rounds, acquisitions, expansion plans. The more specific, the better.
4. **Adapt to the company.** Do NOT always cover the same 4 topics. Identify what matters most for THIS company based on the research and lead with that. Examples:
   - If the biggest issue is billing disputes and regulatory risk, lead with that.
   - If the company has no APMs at all, make that the headline.
   - If cross-border is irrelevant (e.g., US only), skip it entirely and focus on what IS relevant.
   - If the company is expanding into new verticals, highlight the payment complexity that creates.
5. **Every claim must be sourced from research.** Name PSPs, name countries, name complaint platforms, cite settlement amounts, reference funding rounds.

---

#### SLIDE 4 — Executive Summary

3 content areas. **Keep everything brief.** This is a summary, not a deep dive.

**COMPANY INTRO** (top paragraph under company name):
1 sentence max. What the company does + 2–3 key scale metrics. Nothing else.

**SUBTITLE + BODY** (second block):
Subtitle in UPPERCASE. Body = 1–2 sentences max describing the payment setup. Who processes, what's missing.

**KEY CHALLENGES** (5 bullet points):
1 sentence each. Specific, data-backed. Mention names and numbers but do not over-explain.

---

#### SLIDE 5 — Current Setup Constraints

Title: `"{company}'s current setup"` — Subtitle: `"THE CURRENT SETUP HAS MANY CONSTRAINTS"`

**4 boxes**, each with a bold title + 2–3 sentence description. Choose the 4 most relevant constraints for THIS company. Do not force-fit the same 4 topics every time. Possibilities include:

- Missing APMs (name which ones per country)
- Single processor dependency (name the PSP)
- Billing/dispute/chargeback risk (cite complaints, settlements)
- No orchestration/routing/failover
- Cross-border cost drag (name countries without entity)
- Reconciliation overhead across multiple PSPs
- Vertical expansion without payment infrastructure
- Regulatory/compliance exposure
- Subscription/recurring billing fragility

Pick the 4 that matter most based on research.

---

#### SLIDE 6 — Payment Stack Overview

Title: adapt to company situation (lowercase).

3 sections with bold titles + descriptions. The sections should reflect what the research actually found. Not always the same 3 topics. Possible sections:

- Current card processing setup (PSPs, card brands, fallback or not)
- APM opportunity (specific APMs per market from the APMs reference tab)
- Orchestration gap
- Billing infrastructure weakness
- Vertical-specific payment needs
- Recurring/subscription payment fragility

---

#### SLIDE 7 — Current Landscape

Title: `"{company}'s current landscape"` (lowercase)

Country traffic data from SimilarWeb (all >0.5%). Group by region. Include key company metrics (locations, members, revenue, TPV, employees, etc.).

---

**After presenting slides 4–7, proceed to Steps 3–7 (calculations + Excel generation).**

---

## Step 9 — Generate Excel

After presenting the slide content, generate the Excel file using Python with `openpyxl`.

Save to: `Business Cases/BC sheets - {company_name}.xlsx`

Include sheets: RESUMEN + BC Pay-ins per region + BC Devs.Eng per region (same as current Step 7).

---

## IMPORTANT RULES

1. **Only use data about the target company** — never mix in competitor or other company data
2. **Be conservative** with estimates — use lower ranges when uncertain
3. **Label all estimates** — if revenue, ATV, or other data is estimated, note it
4. **APM accuracy** — only list APMs as "missing" if confirmed through research. When in doubt, list fewer.
5. **All amounts in millions USD** in the Excel (consistent with Canva template)
6. **Conversion rate = 0.06** — standard across all markets (same as template)
7. **Wait for SimilarWeb data** — do NOT proceed without the user providing traffic data
8. **Slide content must match the exact format** of existing BCs in `Business Cases/` — same section headers, same conclusion templates, same table structures. **Review all available BC sheets** (not just Canva) to calibrate values, structure, and tone.
9. **Proposed APMs per country** — must be specific, researched, and relevant to that market (e.g., Pix for Brazil, Bizum for Spain, iDEAL for Netherlands). Never generic.
10. **Slide content is text output** — present slides 4–7 as concise, data-rich text in the chat. No dashes. Adapt topics to what matters most for each company. Never repeat the same structure mechanically.
