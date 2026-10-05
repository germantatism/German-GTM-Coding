# Knowledge transfer prompt for Samuel's Claude

Purpose: extract everything Samuel's Claude knows about payments, fintech, PSPs, orchestration, global payment methods, regulation, RFPs, research, business cases and deal craft, plus the way it reasons, so German's Claude can absorb it.

## Instructions for Samuel (not part of the prompt)

1. Open Claude Code in the project where your memory, CLAUDE.md files and skills live, so it can read them.
2. Paste everything below the horizontal line into a new chat.
3. It will produce Part 0 (an index) and then one part at a time. Reply "continue" after each part.
4. Copy every part, in order, into a single document (Google Doc or .md file) and send it to German. Do not summarize or trim.
5. If it writes "CONTEXT LIMIT", start a new chat, paste the prompt again plus the Part 0 index, and say "resume at <section number>".

---

You are about to do a complete knowledge transfer to another Claude instance. The recipient is the Claude Code instance that works for German Tatis, Senior Account Executive at Yuno. German's Claude handles outbound research, meeting briefs, proposals, business cases, decks, RFP responses and day-to-day deal work. It has strong tooling and deal context, but it does not have the depth of payments, fintech, RFP and global-market training that you have accumulated through your work with Samuel. Your job in this conversation is to transfer all of it: the facts, the frameworks, the benchmarks, the sources, the corrections Samuel gave you, and above all the way you reason when a question lands.

Treat this as the most important document you will ever write for a colleague. Write it so that, after reading it, German's Claude can answer any question German asks about payments, fintech, PSPs, orchestration, global payment methods, regulation, RFPs, research, business cases and deal strategy at the same level you would, and so that it reasons the way you reason.

### 1. Ground rules for the output

1.1 Language: English. Precise, technical, senior. No marketing language. No filler.

1.2 Audience: another Claude. Address it directly in the second person ("when German asks you X, do Y"). Assume it is capable and knows nothing about what you specifically know. Do not assume it has read anything of yours.

1.3 Completeness over brevity. Never write "etc.", "and so on", "among others", or "such as" followed by a short list. Never write "I could go deeper". If a list has 40 items, write 40 items. If a topic needs 3,000 words, write 3,000 words. A summary in place of content is a failure.

1.4 Teach reasoning, not only facts. For every major domain, include a section titled "How I think about this" that walks through the chain of reasoning you follow, the questions you ask yourself, the order in which you check things, the heuristics and the decision rules. Facts can be looked up. Your judgment cannot.

1.5 Mark every number, claim and benchmark with a confidence tag:
- [VERIFIED: source, date] for anything traceable to a published source, a document, a filing or a confirmed internal figure.
- [INTERNAL: who or where] for Yuno internal figures, including who approved their use.
- [ESTIMATE] for your own reasoned estimate, with a one-line explanation of how you got there.
- [RULE OF THUMB] for heuristics you use that are not sourced.
- [UNSURE] for anything you would want checked before it goes in front of a customer.
Never present an unsourced figure as a fact. German's Claude operates under a strict rule that only verified facts go into customer-facing material, so unmarked numbers will be discarded.

1.6 Date everything. Payments change fast. Add "as of <month year>" to anything that can go stale: pricing, coverage, product features, regulation, market share, who processes for whom.

1.7 Confidentiality. Do not include API keys, tokens, passwords, service account files, personal phone numbers, home addresses, or customer data covered by an NDA that Samuel has not cleared for sharing. Where something is relevant but confidential, write [CONFIDENTIAL: ask Samuel] and describe it at a high level so German can ask Samuel directly. Do not silently omit it.

1.8 Read before you write. Before producing Part 0, read your entire memory directory, every CLAUDE.md you have access to, your skills and commands folders, your templates, and any reference documents you keep. When you draw on a memory or file, cite its path so German's Claude can ask for the original.

1.9 Delivery protocol. Deliver in parts. First produce Part 0 (the master index with an estimated part count). Then produce Part A and stop. Wait for the word "continue" before each subsequent part. Each part must be self-contained and complete, typically 2,500 to 5,000 words. Number every section (A.1, A.2, A.2.1) so sections can be referenced later. If you approach your context limit, write "CONTEXT LIMIT: resume at <section number>" and stop, so Samuel can restart in a new chat.

1.10 Format. Markdown. Use tables for anything comparative (payment methods by country, provider profiles, benchmarks, fee structures). Use numbered lists for procedures and decision trees. Do not use em-dashes anywhere. Do not use a hyphen surrounded by spaces as punctuation.

1.11 Honesty. If you do not know something, or your knowledge is thin in an area, say so explicitly in Part N. A clearly marked gap is far more valuable than a confident guess.

### 2. What to produce, part by part

#### Part 0: Master index
List every part and every major section you will produce, with an estimated word count per part and the total number of parts. In one table, list every memory file, CLAUDE.md, skill, command and template you read in preparation, with its path and a one-line description of what it contains.

#### Part A: Your own configuration and the rules Samuel gave you
A.1 Your identity and role as Samuel's Claude: what you do daily, in which tools, for which kinds of deliverables.

A.2 Every rule, correction and preference Samuel has given you, written as three lines each: the rule, why Samuel gave it (the mistake or situation behind it), and how you apply it now. Include tone rules, formatting rules, what never to say, what to always include, how Samuel wants decks, emails and briefs structured, what he rejected and why. This is the highest-value section of Part A. Be exhaustive.

A.3 Your skills and commands. For each one: its name, what it does, its inputs, its outputs, the steps it runs, the quality checks it applies, and what German's Claude would need in order to replicate it. Paste the full instruction text of each skill where it is not confidential.

A.4 Your templates: deck storylines (first-meeting deck, C-suite product session, 10-K-driven business case, the Roblox family of decks and anything newer), email templates, brief templates, RFP answer templates, proposal structures. Paste the actual templates, not descriptions of them.

A.5 Your workflows: how you prepare for a meeting, how you research an account from zero, how you build a business case, how you answer an RFP, how you write a proposal, how you run QA on a deliverable. Step by step, including which sources you check in which order and what you do when sources disagree.

A.6 Tools and data sources you use and how: Gong, Slack, Gmail, Drive, Glean, Metabase, Redash, web sources, SimilarWeb, BuiltWith, Wappalyzer, SEC EDGAR, app stores, LinkedIn, Crunchbase, and anything else. For each: what it is good for, its limitations, and the exact way you query it.

A.7 Samuel's working style and preferences that would help German's Claude collaborate with him well: communication style, what he values in a deliverable, what he dislikes. Keep it professional.

#### Part B: Payments fundamentals, the complete stack
Write this as the reference you wish you had on day one. Cover at minimum:

B.1 The four-party model and every participant: cardholder, merchant, acquirer, issuer, card network, processor, gateway, PSP, payment facilitator, ISO, merchant of record, orchestrator, token service provider, 3DS server and ACS, fraud vendor, vault provider, bank partners. For each: what it does, what it earns, what it is liable for, and how a merchant contracts with it.

B.2 Transaction lifecycle in detail: authorization, authentication, capture, clearing, settlement, funding, reconciliation, refunds, reversals, voids, chargebacks and representment. Include timing, the data fields that matter, and where failures happen.

B.3 Cost of acceptance: interchange (how it is set, by whom, by region, by card type, by channel), scheme fees and assessments, acquirer margin, gateway fees, FX and cross-border fees, DCC, blended versus interchange-plus versus interchange-plus-plus pricing, how to read a merchant statement, how to estimate a merchant's effective rate from the outside, and where savings usually hide.

B.4 Authorization and approval-rate optimization. Every lever you know: local acquiring, network tokens, account updater, retry logic and when it hurts, smart routing, cascading, 3DS exemptions and frictionless flows, data quality, MCC alignment, stored-credential framework and CIT versus MIT flags, issuer relationships, BIN-level routing, partial approvals, decline-code analysis, soft versus hard declines, do-not-honor handling, insufficient-funds strategies, dunning for subscriptions. For each lever: typical uplift range with source and confidence, when it works, when it does not, and how to measure it.

B.5 Authentication and security: 3DS1 versus 3DS2 versions, SCA under PSD2, exemptions (TRA, low value, trusted beneficiary, MIT, corporate), liability shift, frictionless rates, delegated authentication, passkeys and network-based authentication as they stand today, PCI DSS 4.0 scope and SAQ types, tokenization (network tokens versus PSP tokens versus vault tokens), token portability and vault migration, encryption and key management as they matter to a merchant.

B.6 Fraud and disputes: fraud types, chargeback reason codes by network, dispute lifecycle and deadlines, Visa and Mastercard monitoring programs with their current names and thresholds (with confidence tags), compelling-evidence rules, friendly fraud, pre-dispute tools (Ethoca, Verifi, RDR, CDRN), the fraud-tool landscape (Forter, Riskified, Signifyd, Sift, Stripe Radar, Adyen RevenueProtect, Kount, Ravelin, Seon, Cybersource Decision Manager, and any others), and how orchestration interacts with fraud tooling.

B.7 Recurring and subscriptions: stored credentials, CIT and MIT, network mandates, dunning, involuntary churn, account updaters, retry schedules, grace periods, subscription billing platforms (Stripe Billing, Recurly, Chargebee, Zuora, Braintree recurring, Paddle, and others), and how an orchestrator sits alongside or replaces them.

B.8 Payouts, marketplaces and platforms: pay-in versus pay-out, split payments, escrow, seller onboarding and KYB, payfac models, Stripe Connect and Adyen for Platforms and their alternatives, local payout rails by region, FX on payouts, tax reporting, and where Yuno plays.

B.9 Alternative payment methods: taxonomy (wallets, bank transfers and account-to-account, real-time payment rails, cash vouchers, BNPL, carrier billing, crypto on-ramps, prepaid, installments), how each settles, refund behavior, dispute behavior, typical cost, and integration patterns (redirect, embedded, QR, push versus pull).

B.10 Reconciliation and finance operations: what finance teams actually need, settlement files, fee reconciliation, multi-PSP reconciliation pain, how orchestration helps and where it does not.

B.11 Integration architecture: direct integrations versus gateway versus orchestrator, SDK versus API versus hosted checkout, mobile considerations, latency, idempotency, webhooks, retries, failover, multi-region, data residency, and how long real migrations take.

B.12 How I think about this: your reasoning chain when a merchant describes their stack, when a merchant quotes an approval rate, when a merchant says their costs are fine, and when a merchant says they built orchestration in-house.

#### Part C: Global payments by region and country
For every region and country you know, produce a table and a narrative. Cover at least: United States, Canada, Mexico, Brazil, Colombia, Peru, Chile, Argentina, Ecuador, Central America and the Caribbean, United Kingdom, Germany, France, Spain, Italy, Netherlands, Belgium, Poland, Portugal, the Nordics, Switzerland, Austria, Turkey, Israel, United Arab Emirates, Saudi Arabia, Egypt, Nigeria, Kenya, South Africa, India, Pakistan, Indonesia, Philippines, Vietnam, Thailand, Malaysia, Singapore, Japan, South Korea, China as it applies to foreign merchants, Hong Kong, Taiwan, Australia, New Zealand. For each country:

C.1 Dominant payment methods by share, with source and date.

C.2 Local real-time rails and bank-transfer schemes (Pix, Pix Automático, SPEI, PSE, Bre-B, Yape, Plin, UPI, PromptPay, PayNow, DuitNow, FPS, SEPA Instant, Faster Payments, FedNow, RTP, Interac, PayTo, and every other one you know): who runs them, whether they support recurring, refunds and disputes, and how a foreign merchant accesses them.

C.3 Cards: local schemes (Elo, Hipercard, RuPay, Mada, KNET, Benefit, Cartes Bancaires, Bancomat, Dankort, JCB, UnionPay, and others), installment culture and mechanics, debit versus credit behavior, domestic versus cross-border approval-rate differences and why, interchange levels or caps.

C.4 Local acquirers and PSPs that matter in that country, and which of them Yuno is connected to. Mark [UNSURE] where you are not certain.

C.5 Regulatory and tax specifics that affect a foreign merchant: local entity requirements, withholding taxes on cross-border, FX controls, data localization, licensing, e-invoicing, consumer-protection rules on refunds and disputes.

C.6 Approval-rate benchmarks for cross-border versus local acquiring, with sources.

C.7 What a merchant selling into that country usually complains about, and the standard Yuno play.

C.8 How I think about this: how you decide which markets matter for a given merchant, how you spot a coverage gap from the outside, and how you rank the opportunity.

#### Part D: The provider landscape
D.1 For every PSP, acquirer, gateway, local processor and merchant of record you know, at minimum: Stripe, Adyen, Checkout.com, PayPal and Braintree, Worldpay, Nuvei, dLocal, EBANX, PayU, Rapyd, Airwallex, Mollie, Cybersource, Chase and J.P. Morgan Payments, Fiserv, Global Payments, Elavon, Worldline, Nexi, Shift4, Paysafe, Trustly, GoCardless, Klarna, Affirm, Afterpay, Mercado Pago, PagSeguro, Stone, Cielo, Rede, Getnet, Kushki, Conekta, Openpay, Clip, Payoneer, Paddle, Digital River, FastSpring, 2Checkout and Verifone, Razorpay, PayU India, Cashfree, PhonePe PG, Xendit, Midtrans, 2C2P, Opn (formerly Omise), PayMongo, Tap, Telr, HyperPay, Moyasar, Paymob, Fawry, Flutterwave, Paystack, Peach Payments, Ozow, and any other you consider relevant. For each: what it is, where it is strong, where it is weak, pricing model and typical rates where known, geographic coverage, which verticals it wins, what merchants complain about, how it behaves in an RFP, and how you position Yuno next to it (as a layer on top, as a replacement, or as a complement).

D.2 Orchestration competitors: Spreedly, Primer, Gr4vy, Payrails, CellPoint Digital, IXOPAY, Zooz, BridgerPay, Corefy, ACI Worldwide, Juspay, Rebilly, Basis Theory, VGS, Evervault, Skyflow, Paydock, Akurateco, and the in-house build pattern. For each: product scope, pricing where known, who uses them, strengths, weaknesses, how they pitch against Yuno, and your counter.

D.3 Fraud, authentication, vault, reconciliation, billing and payout vendors that sit next to orchestration, and how they integrate.

D.4 A "who processes for whom" table: every merchant whose stack you know, with the providers, the evidence, the confidence and the date. This is extremely valuable for research work. Make it as long as you can.

D.5 How I think about this: how you tell from the outside which provider a merchant uses, how you infer their contract shape, how you decide whether Yuno is a layer or a replacement, and which competitor is probably in the room.

#### Part E: Yuno
E.1 Product, module by module: what each actually does today, what is roadmap, what is often oversold, and the precise words you use to describe each.

E.2 Positioning and messaging that works, by persona and by vertical. Proof points and customer references you are allowed to use, with who approved them and when. Published statistics you can cite and their sources. Statistics you must not use.

E.3 Pricing guardrails as you understand them. German's Claude already has the Pricing Policy, so focus on how deals were actually priced, what got approved, what got rejected, and why.

E.4 Objection handling: every objection you have met, the best answer, and what not to say. Include "we built it in-house", "our PSP already does routing", "we are single-PSP and happy", "no bandwidth to integrate", "too early for us", "what is your uptime", "you are a startup", "Stripe is adding this feature", "we need a local entity", "our volume is too small", "we already have a vault", and every other one you know.

E.5 Reference deals and stories you can tell (anonymized where needed): the merchant's problem, what Yuno did, the result, and the confidence level of each number.

E.6 Internal process knowledge: who to ask for what (pricing approval, legal, security questionnaires, solutions engineering, integration status, product roadmap), typical timelines, what slows deals down internally, and how to avoid it.

E.7 How I think about this: how you qualify fit, the signals that make an account a strong fit versus a weak fit, and how you choose the lead angle for an account.

#### Part F: RFP, RFI and security questionnaire playbook
F.1 Anatomy of a payments RFP: typical sections, who writes them, who scores them, how scoring usually works, the hidden evaluation criteria, and how incumbents shape them.

F.2 Go or no-go framework: the questions you ask, the red flags, the signals that an RFP is wired for a competitor, and how you decide to bid, bid partially, or decline.

F.3 Your end-to-end RFP process: intake, question parsing, ownership, answer drafting, evidence gathering, internal reviews, pricing, submission, follow-up presentations, and the timeline you plan against.

F.4 Question bank with model answers. Produce the fullest bank you can, grouped by theme: company and financials, product and functionality, integration and APIs, coverage by country and method, routing and retry logic, tokenization and vaulting, 3DS and authentication, fraud, reconciliation and reporting, payouts, subscriptions, uptime and SLAs, incident management, security (PCI DSS, SOC 2, ISO 27001, penetration testing, encryption, key management, access control), privacy and data residency (GDPR, LGPD, CCPA, India, and others), business continuity and disaster recovery, support and account management, implementation and migration, commercial terms, exit and portability. For each question: the model answer, what evidence to attach, who at Yuno owns the fact, and the traps in how the question is phrased.

F.5 Win themes and differentiation: how you turn an RFP from a feature checklist into a value story, how you handle mandatory requirements you do not fully meet, and how you use the presentation round.

F.6 Examples: every RFP you have worked on or seen (anonymized if required), what the merchant asked for, what was unusual, what won or lost, and the lessons.

F.7 How I think about this: your reasoning when a new RFP lands, in order.

#### Part G: Research methodology
G.1 How you build a complete picture of a merchant from zero: the ordered checklist of sources (website and checkout inspection, network requests and script domains, privacy policies and terms, app store listings, 10-K and annual reports and S-1 filings, earnings calls, investor decks, job postings, LinkedIn org charts, Glassdoor, G2 and Capterra, press, podcasts, conference talks, SimilarWeb, BuiltWith, Wappalyzer, Crunchbase, PitchBook, government filings, app analytics), with what each tells you and how reliable it is.

G.2 How to identify a merchant's payment stack from the outside, with the exact technical signals (script hosts, iframe domains, tokenization endpoints, 3DS providers, wallet buttons, payment method lists by country, cookie names, SDK names in app bundles) and the confidence you attach to each.

G.3 How to read a 10-K or annual report for payments: which sections, which line items, which phrases signal pain (payment processing fees, chargebacks, fraud losses, concentration risk on a provider, international expansion, app store fees, FX exposure), and how you turn them into a business case.

G.4 ICP scoring: the criteria, the weights, examples of high and low scores, and the exceptions.

G.5 Persona mapping: how you find the real decision-maker versus the champion, which titles matter by vertical and region, and how you adapt the message to each.

G.6 Intent and timing signals: what tells you a merchant is about to change providers, and where you find it.

G.7 Output standards: how a research brief should look, what must be in it, and the QA you run.

G.8 How I think about this.

#### Part H: Business case and value modeling
H.1 Your value framework: the levers, how they combine, and how you avoid double counting.

H.2 Every formula you use, written out, with the inputs and where each input comes from.

H.3 Benchmark library: approval-rate uplift by lever and region, cost savings by lever, chargeback and fraud benchmarks, retry recovery rates, network-token uplift, local-acquiring uplift, involuntary churn rates by vertical, false-decline rates, app store fee bypass economics, FX savings, operational cost of running multiple PSPs, time to integrate. Each with source, date and confidence. Separate published figures from Yuno internal figures from your own estimates.

H.4 Worked examples: at least three full business cases from inputs to output, in different verticals, showing every assumption.

H.5 Sanity checks: how you know a business case is too aggressive, the ranges that make a CFO stop reading, how you present uncertainty, and how you set conservative, base and upside cases.

H.6 How you present it: deck structure, the one slide that matters, and how to handle "where did this number come from".

H.7 How I think about this.

#### Part I: Vertical playbooks
For each vertical: how payments work in it, the specific pains, the KPIs the buyer cares about, the typical stack, the usual competitors in the deal, the Yuno angle, proof points, discovery questions, and mistakes to avoid. Cover at minimum: travel and airlines, online travel agencies, hospitality, gaming and in-app purchases, mobile apps and app store fee bypass, SaaS and subscriptions, streaming and media, marketplaces and platforms, mobility, delivery and quick commerce, ticketing and live events, retail and QSR, fashion and direct-to-consumer ecommerce, fintech and neobanks, crypto on-ramps, iGaming and sports betting, edtech, healthtech and telehealth, nonprofits and donations, telecom and utilities, B2B payments and invoicing, AI consumer apps, creator economy and payouts.

#### Part J: Sales motion and deal craft
J.1 The qualification method you use (MEDDIC or other), with the questions per element and what a good answer sounds like.

J.2 Discovery call structure: the questions that unlock the real pain, and the ones that waste time.

J.3 First-meeting deck, C-suite product session, 10-K-driven business case, proposal, and QBR: the storyline for each, slide by slide, with the reasoning behind the order.

J.4 Writing style for emails, LinkedIn, WhatsApp and executive summaries: rules, examples that worked, examples that failed.

J.5 Negotiation and pricing conversations: how you open, anchor, concede and close; what never to put in writing; how to handle procurement.

J.6 Deal stories: the deals you know in detail, what happened, and what you would do differently.

J.7 Multi-threading, champion building, executive alignment, and how to recover a stalled deal.

J.8 How I think about this.

#### Part K: Regulation, compliance and scheme rules reference
Cover PSD2, PSD3 and the Payment Services Regulation, SCA and its exemptions, UK and EU interchange caps, Durbin and US debit routing, surcharging rules by country, PCI DSS 4.0 including the requirements that became mandatory in 2025, SOC 2, ISO 27001, GDPR, LGPD, CCPA and other US state laws, India RBI tokenization and e-mandate rules and data localization, Brazil Central Bank rules on Pix and on payment institutions, Mexico CNBV and Banxico rules, Colombia Bre-B and SFC rules, Visa and Mastercard monitoring programs (names, thresholds, fees, as of today), Visa Compelling Evidence 3.0, Mastercard First Party Trust, stored-credential mandates, network-token mandates and incentives, account updater programs, Visa and Mastercard rules on installments, cross-border and currency rules, MCC rules and high-risk categories, and licensing requirements for orchestrators and for merchants in each region. For each: what it is, who it applies to, what it means for a merchant, what it means for Yuno, confidence and date.

#### Part L: Glossary
Every term and acronym you use, with a one or two sentence definition written the way you would explain it to a smart non-payments person. Aim for 300 or more entries.

#### Part M: Myths, common mistakes and corrections
Everything people commonly get wrong about payments and orchestration, everything you were corrected on, and the things that sound right but are not. Include the mistakes you have seen in decks, business cases and RFP answers, and the fix for each.

#### Part N: Gaps and open questions
Areas where your knowledge is thin, stale or uncertain, so German's Claude knows what to verify before relying on it. Also list the questions you would want to ask German's Claude in return, since it has deep context on German's deals, tooling and pricing that may be useful to you.

#### Part O: Ingestion guide for German's Claude
Tell German's Claude how to store what you sent: which parts should become persistent reference memory, which should become feedback-type rules, which should become project context, and which should be re-verified before use. Propose a file structure with a one-line description for each file. Finish with a list of 50 questions German is likely to ask and the section where each answer lives.

### 3. Quality bar
Before each part, ask yourself: if German's Claude had only this part and German asked a hard question in this domain, would it answer as well as I would? If not, add what is missing. Prefer tables and numbered steps to prose wherever the content is comparative or procedural. Prefer the specific to the general: a real reason code, a real threshold, a real script domain, a real line item from a real 10-K. If something is confidential, mark it rather than skipping it.

Start now with Part 0.
