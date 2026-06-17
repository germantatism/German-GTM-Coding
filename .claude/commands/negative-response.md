# /negative-response — Reply to Prospect Objection or Rejection

## Argument
$ARGUMENTS = email subject line to search in Gmail

## STEP 1 — Find the email thread

Search Gmail for the thread matching the subject provided in $ARGUMENTS.
Use the Gmail MCP tool `gmail_search_messages` with the subject as query.

- If exactly one thread matches, proceed to STEP 2.
- If multiple threads match or the result is ambiguous, ask the user for the prospect's name to narrow it down, then search again combining subject + name.
- If no thread is found, try a partial subject search. If still nothing, inform the user and stop.

## STEP 2 — Read the full thread

Use `gmail_read_thread` to read the complete conversation. Extract:

1. **Prospect name and title** (from signature or email headers)
2. **Company name**
3. **Industry / vertical**
4. **The objection or rejection** — what exactly did they say? Classify it:
   - "Not interested" / generic brush-off
   - "We already have a provider" / incumbent loyalty
   - "Not the right time" / timing objection
   - "Too expensive" / budget concern
   - "We handle this internally" / build vs buy
   - "Need to check with [someone]" / authority deflection
   - Other (describe it)
5. **Conversation history** — what was pitched, how many touches, what value props were used
6. **Language** — detect whether the prospect writes in English, Portuguese, or Spanish

## STEP 3 — Select the response levers

Based on the thread context, pick the ONE or TWO most relevant Yuno value levers. Do NOT pitch everything. Choose from:

- **Approval rate uplift**: smart routing, retry logic, cascading across PSPs (strongest when prospect uses a single PSP or mentions failed transactions)
- **PSP consolidation**: single integration to 300+ PSPs, reduce vendor management overhead (strongest when prospect manages multiple providers manually)
- **APM coverage**: 300+ local payment methods across LatAm, missing conversion from local buyers (strongest for companies expanding in LatAm or with checkout gaps)
- **Engineering cost reduction**: one API instead of maintaining multiple PSP integrations (strongest for "we handle this internally" objections)
- **Subscription recovery**: smart dunning, retry on soft declines, involuntary churn reduction (strongest for SaaS / subscription businesses)
- **Cross-border / MoR**: merchant of record for tax, FX, compliance (strongest for companies selling into LatAm from outside)
- **Negotiation leverage / MDR optimization**: volume aggregation across PSPs to negotiate better rates (strongest for budget objections)

## STEP 4 — Generate two response variants

Detect the prospect's language from the thread:
- If they wrote in English → respond in English
- If they wrote in Portuguese or are clearly Brazilian → respond in Portuguese
- If they wrote in Spanish → respond in Spanish
- If unclear, default to English

### VARIANT 1 — Detailed

Structure:
1. **Acknowledge** their response in one sentence. No apology, no defensiveness. Just a clean acknowledgment that shows you read what they said.
2. **Reframe** (2-3 sentences): Pivot to the specific business problem Yuno solves for companies like theirs. Use a concrete data point or metric if possible (e.g., "companies routing through a single PSP in LatAm typically leave 8-12% of approvals on the table").
3. **Proof point** (1-2 sentences): Reference a relevant enterprise client. Pick the most contextually relevant:
   - inDrive — ride-hailing, multi-country LatAm expansion
   - Rappi — super-app, high-volume payments across LatAm
   - Livelo — loyalty/rewards, subscription model
   - Wingo — airline, cross-border payments
   - JEEP / Stellantis — automotive, enterprise scale
   - OpenAI, Uber, SpaceX, GoFundMe — if more relevant to the vertical
4. **Close** with a low-friction ask. Options:
   - A specific question that invites a reply without commitment ("Out of curiosity, are you seeing consistent approval rates above 90% in Brazil?")
   - A future touchpoint ("I will circle back in Q3 when budgets reset. In the meantime, happy to share our benchmark report for [industry].")
   - A soft leave-the-door-open ("If anything changes on your end, I am one message away.")

Length: 6-10 sentences total. No more.

### VARIANT 2 — Short and direct

- 3-4 sentences maximum
- Same strategic intent as Variant 1 but compressed
- Conversational, confident, zero fluff
- Still includes one proof point or data point

### VARIANT 3 — Challenge / Pattern interrupt

- 4-6 sentences maximum
- Takes a bolder angle: challenges an assumption the prospect made, shares a surprising data point, or reframes the objection as a symptom of a bigger problem
- Slightly provocative but never disrespectful
- Goal: make the prospect think "huh, I hadn't considered that"
- Still grounded in a real Yuno value lever and a proof point

## STEP 5 — Recommendation

After all three variants, add:

**Recommendation:** [Which variant to send] — [One sentence explaining why based on the prospect's tone, seniority, and objection type]

## OUTPUT RULES (apply to all three variants)

- NEVER use dashes (hyphens as punctuation, em-dashes, en-dashes). Use commas, colons, semicolons, or line breaks instead.
- NEVER use bold, italic, or any markdown formatting in the email text. Plain text only.
- NEVER use these phrases: "I hope this finds you well", "I wanted to reach out", "I understand your concerns", "I appreciate your time", "Just following up", "Circling back", "Touching base"
- NEVER be apologetic or defensive about the rejection
- NEVER pitch more than two value levers
- NEVER use excessive flattery or softening language
- Sound like a sharp, senior sales professional who has heard every objection and is genuinely unfazed
- Keep the tone professional but human. Write like a real person, not a template.
- Sign off as "German" (no last name, no title block)
- The reply should feel like it took 2 minutes to write, even though it is strategically precise

## OUTPUT FORMAT

```
CONTEXT
Prospect: [Name], [Title]
Company: [Company]
Industry: [Industry]
Objection type: [Classification from Step 2]
Language: [English / Portuguese / Spanish]
Selected levers: [1-2 levers from Step 3]
```

Then:

```
VARIANT 1 — DETAILED

[Email text, plain text, no formatting]
```

```
VARIANT 2 — SHORT

[Email text, plain text, no formatting]
```

```
VARIANT 3 — CHALLENGE

[Email text, plain text, no formatting]
```

```
RECOMMENDATION: [Variant] — [Why]
```
