# US market sweep brief (Yuno, 27-Oct-2026)

## Who asks and why
German Tatis, Business Development Manager at Yuno (payment orchestration: one API to 1,000+ payment methods, PSPs, fraud tools, vault, network tokens, subscriptions engine, reconciliation; 190+ countries). He already has 2,533 companies across his lists. He wants the US companies that are MISSING from those lists and that "should use Yuno with their eyes closed to improve operational efficiency".

Yuno positioning: "AI native operating system for global financial infrastructure. We help companies orchestrate their payment stack across a fragmented ecosystem (payment methods, processors, antifraud tools, KYC/KYB, reconciliations, stablecoins) to lower processing costs, increase authorization rates, expand globally, and become more operationally efficient."

## Hard exclusion: the union file
File: /private/tmp/claude-501/-Users-germantatis-Desktop-GTMCoding/5ef0ebef-3807-40f8-a3b0-9455b33257d2/scratchpad/lists/union.tsv
Columns: norm (lowercase, no punctuation, no suffixes like inc/group/holdings) | kind (ACTIVE = in a working list; BANK = only in an old research bank) | raw_names | sources.
Before proposing ANY company run: grep -i "<distinctive word of the name>" union.tsv
- If found with kind ACTIVE: do NOT include it (already on a list).
- If found with kind BANK only: you may include it but set column "In old bank" = YES (German never promoted it to a working list; say why it deserves promotion).
- Not found: include it (this is the real target).
Also exclude known Yuno customers: Rappi, inDrive, McDonald's, Shein, Crunchyroll, GoFundMe/Classy, Allegiant Air, Suno, Skool, Whop, Open English, xAI/Grok, Qatar Airways, Copa Airlines, Kraken, Moon Active, Viva Aerobus, Crypto.com, Despegar, Automattic, Fever, Airalo, Wolt, Nubank, Mercado Libre, Hopper, Avianca. Also exclude payments providers themselves (PSPs, acquirers, money transmitters, wallets, BNPLs).

## Yuno ICP (score 1 to 5, column "Yuno Fit")
Base requirements: US or Canada headquarters or a US-run digital business; estimated 100K+ digital (card not present) transactions per month, or $100M+ online volume per year; the company owns its PSP contracts (not Shopify Payments captive, not app-store captive, not franchisee-held, not a MoR like Xsolla/Paddle/Digital River running everything).
Operational-efficiency signals (the more, the higher the score):
1. Multiple PSPs or acquirers run in parallel with in-house routing (names from job posts, 10-K, engineering blogs, Adyen/Stripe/Braintree/Checkout.com/Nuvei/Worldpay/Cybersource customer pages).
2. Multi-country acceptance (3+ countries) or active international expansion, especially LatAm, EMEA, APAC where local methods (Pix, OXXO, SPEI, iDEAL, UPI...) matter.
3. Subscriptions or recurring card-on-file billing at scale (renewals, dunning, retries, account updater, network tokens).
4. Payouts to sellers, drivers, creators, hosts, tutors (marketplaces) with reconciliation across pay-in and pay-out.
5. Multi-brand or multi-entity after M&A (several brands on different stacks that need one layer).
6. Manual reconciliation pain: finance teams matching settlements across providers, several currencies, several entities (look for "payments operations", "reconciliation analyst", "settlement" job posts).
7. Single-PSP concentration risk at large scale (Stripe-only or Braintree-only at $500M+ online) with documented declines or outages.
8. Active RFP, new Head of Payments, new CFO, IPO cost scrutiny, margin pressure, recent outage.
Score 5 = 4+ signals incl. multi-PSP or multi-market; 4 = 3 signals; 3 = 2 signals, clear volume; 2 = volume but single market/single PSP and little complexity; 1 = does not qualify (do not include 1s).

## Output
Write a TSV (tab separated, one row per company, header row) to the path your task gives you. Columns, in this order:
Company | Website | HQ (city, state) | Vertical | Sub-vertical | Est. annual revenue or GMV ($M, with year) | Est. online payment profile (volume, tx/month, avg ticket, markets served) | Known payment stack (providers, with source) | Orchestrator today? (none / in-house / Spreedly / Primer / Gr4vy / other) | Subscriptions? (yes/no + what) | Payouts? (yes/no + to whom) | Multi-market? (countries) | Ops-efficiency pain (1 to 2 sentences, concrete) | Why Yuno, eyes closed (1 to 2 sentences) | Yuno Fit (1 to 5) | In old bank (YES/NO) | Evidence URLs (2 to 4, space separated) | Confidence (High/Med/Low) | Payments leader (name, title, LinkedIn if found quickly, else blank)
Aim for 25 to 40 companies, quality over quantity. Every stack claim needs a URL. Mark estimates as "est.". No em-dashes. No invented numbers. If you cannot verify a stack, write "undisclosed" and lower Confidence.

## Research method and budget
- WebSearch budget for YOUR task: at most 30 calls (session budget is shared with 4 other agents; it is a hard cap). Use mode "standard". Batch thinking: one search should surface several candidates (e.g., "largest US subscription companies by revenue 2026", "Adyen customers United States 2026", "payments operations manager reconciliation multiple processors job").
- Prefer WebFetch (unlimited) on: company sites and investor pages, 10-K "Item 1" via sec.gov full-text search (https://efts.sec.gov/LATEST/search-index?q=%22payment%20processors%22&forms=10-K is NOT fetchable; use https://www.sec.gov/cgi-bin/browse-edgar or known 10-K URLs), PSP customer pages (https://www.adyen.com/customers, https://stripe.com/customers, https://www.braintreepayments.com/customers, https://www.checkout.com/customers, https://www.nuvei.com/customers, https://www.cybersource.com/en-us/customers.html, https://www.worldpay.com/en/insights/case-studies), job boards (company careers pages, https://www.builtin.com, greenhouse/lever pages), engineering blogs.
- Keep notes short. Do not write files anywhere except your output path.
