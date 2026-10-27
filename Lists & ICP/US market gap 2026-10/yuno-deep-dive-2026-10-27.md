# Yuno deep dive (inside view), 27 Oct 2026

Prepared for German Tatis (AE, NorthAm). Purpose: a sourced reference to decide which US companies should use Yuno "with their eyes closed" to gain operational efficiency.

Source coverage note: Glean (company_search, chat, people search) returned "fetch failed" on every attempt this session, so nothing below comes from Glean. Internal facts come from the local repo, German's memory notes, the Finance pricing policy summary, the Payments Concierge internal deck and German's Google Sheets. Public facts come from y.uno, docs.y.uno and press. Anything not confirmed is tagged [UNVERIFIED]; reasoning is tagged [INFERENCE].

---

## 1. Yuno in one page

**Positioning (canonical, use verbatim):** "Yuno is an AI native operating system for global financial infrastructure. We help companies orchestrate their payment stack across a fragmented ecosystem that includes payment methods, processors, antifraud tools, KYC/KYB providers, reconciliations, and stablecoins to lower payment processing costs, increase authorization rates, expand globally, and become more operationally efficient." Four outcomes: lower processing costs, higher authorization rates, global expansion, operational efficiency.

**Public taglines (Oct 2026):** homepage "The AI-native intelligence system of global payments"; docs "Yuno is the AI operating system for payments: one API and one SDK connect you to payment providers, banks, fraud tools, and local payment methods, with AI agents on top"; about page "Making global payments effortless" and "Agent-first by design".

**What it is, structurally:** an orchestration layer on top of the merchant's own PSP, acquirer, fraud and local-method contracts. Yuno does not custody funds and has no acquiring arm, so routing has no margin conflict ("orchestrated, not custodied"). Docs frame the fit explicitly: Yuno is for accepting payments across multiple countries, currencies or methods through one integration, routing across providers with retries and failover, building checkout, enrollment or subscription flows on a vaulted method, or running marketplace splits. Docs also say it is not the right fit for "a single fixed payment processor integration with no need for routing or multiple payment methods".

**Founding and founders:** Juan Pablo Ortega (co-founder, CEO) and Julián Núñez (co-founder, COO), both from Rappi. Founding year is inconsistent across Yuno's own pages: the about-page timeline and the "vs" pages say 2021; the about-page "What we do" block and the Series B release say 2022 (Colombia); TechCrunch reported the product launched October 2022.

**HQ and footprint:** no official HQ statement on the about page; New York is listed first. 16 offices on 5 continents: New York, Miami, Mexico City, Bogotá, Buenos Aires, São Paulo, Shanghai, Singapore, London, Paris, Porto, Madrid, Warsaw, Doha (regional HQ), Dubai, San Francisco. Processing environments are split into US and EMEA regions (docs). Saudi Central Bank certification obtained April 2026.

**Funding:** $10M seed (March 2022; about page credits Kaszek and Monashees as leads, TechCrunch credits a16z and LatAm VCs), $25M Series A (March 2024, led by DST Global Partners, with a16z, Tiger Global, Kaszek, Monashees; TechCrunch put the valuation at $150M), $45M Series B (12 Aug 2026, San Francisco dateline, led by Global PayTech Ventures with a16z, Tiger Global, Monashees, Kaszek, Endeavor Catalyst, QuantumLight Capital, Rasmal Ventures, Further Ventures, GrowthX Capital). Cumulative about $80M (Forbes Colombia, Caplight). Post-B valuation not disclosed. Series B use of funds: path to profitability, R&D, global infrastructure, in-person payments, scaling the United States, Middle East expansion.

**Scale claims (Yuno's own):** 1,000+ payment methods, 460+ integrations, 190+ countries, 180+ currencies; 150 new integrations in the year to Aug 2026; target of $100B annual transaction volume within 12 months of Aug 2026; "more than $5B in failed-transaction volume recovered" in the prior year; "authorization rates up about 5%"; "more than $500M saved in customer processing costs". North America panel on the homepage: "COUNTRIES 20+, PROVIDERS 60+". Headcount is not disclosed (third-party listings of 1,400 are unreliable) [UNVERIFIED].

**Certifications:** PCI DSS Level 1, SOC 2 Type 2, ISO/IEC 27001, ISO/IEC 27701, GDPR, registered Visa Service Provider. Trust center security.y.uno, status page status.y.uno.

**Leadership (titles move; verify before external use):** JP Ortega CEO; Julián Núñez COO; Justo Benetti CRO (ex-dLocal); Edwin Poot CTO (appointed 2 Jun 2026); Martin Mexia SVP Product (ex-Revolut, Rappi); Rik ter Beek VP Engineering (ex-Adyen); Chee Beh GM APAC; Walter Campos GM LATAM; Mauricio Schwartzmann Chief Banking and FI; Bernabé Murata Head of GTM (ex-Worldpay); Sean Calabro Head of North America (ex-Worldpay, German's manager since Sep 2026); Melissa Pottenger VP Enterprise Growth NA.

**Recognition used in decks:** "World's Top Fintech Company" and "#1 Best Payment API (2025)" (from internal fact file, source not re-verified) [UNVERIFIED].

Sources
- Memory: reference_yuno_positioning.md (27 Aug 2026)
- https://www.y.uno/en (homepage, fetched 27 Oct 2026)
- https://www.y.uno/en/about
- https://www.y.uno/en/newsroom/yuno-series-b (12 Aug 2026)
- https://techcrunch.com/?p=2673996 (5 Mar 2024, Christine Hall)
- https://forbes.co/2026/08/13/emprendedores/yuno-levanta-us45-millones-en-una-ronda-serie-b-para-acelerar-su-expansion-global/
- https://docs.y.uno/docs/how-yuno-works/what-is-yuno and https://docs.y.uno/AGENTS
- https://docs.y.uno/docs/using-yuno (US and EMEA regions)
- https://y.uno/en/newsroom/edwin-poot
- Local: .claude/skills/yuno-sales-deck/references/yuno-facts.md; Vaulting/Yuno Vault vs Basis Theory vs VGS.md

---

## 2. "ACP" at Yuno

**What ACP means in Yuno's current context:** the Agentic Commerce Protocol published by OpenAI (with Stripe) in September 2025 for buying inside ChatGPT. Yuno's blog (12 May 2026) defines ACP as "a set of technical standards that allows AI agents to browse merchant catalogs", covering how an agent authenticates, queries inventory, initiates payment and receives confirmation, and notes the standard is still being formalized with parallel specifications from OpenAI and Google. No internal document in the repo or memory uses "ACP" for anything else; Glean could not be checked, so an internal alternative meaning cannot be ruled out [UNVERIFIED].

**What Yuno offers (public product page "Agentic Commerce", y.uno/en/product/agentic-commerce):**
- Headline: "Your one-stop platform for agentic commerce." Sub: "One integration to be agentic-ready. Built for the next era of AI-driven commerce."
- ACP-ready infrastructure: real-time catalog sync, certified endpoints, and payments, so a merchant's products "appear and can be bought directly inside ChatGPT".
- Product feed control: inventory, pricing and visibility across AI surfaces from one dashboard; Yuno handles catalog syncing, ACP compliance and product updates "without changing your stack".
- Channel insights: which AI platforms send traffic; GMV, orders, approval rate and funnel per channel.
- AI surfaces named: ChatGPT, Claude, Gemini, Perplexity, Copilot. Organizations named: OpenAI (creator of ACP), Visa (service provider status).
- Status: the page carries no "live", "beta" or "waitlist" label. The earlier landing page y.uno/agentic-page (which a search snippet described as refreshing product data every 15 minutes) now returns 404. Treat GA status, named live merchants and volumes as unconfirmed [UNVERIFIED].
- Pitch numbers used: "20% of eCommerce tasks in 2025 completed through agentic AI", "58% of consumers rely on GenAI to discover products", "2 to 6x higher conversion with agentic flows", "1 in 6 Black Friday purchases completed with AI assistance". These are Yuno marketing claims, not independently sourced.

**Adjacent AI-native products (documented, live):**
- Documentation MCP server (read-only, no credentials): https://docs.y.uno/mcp; also llms.txt, AGENTS.md and openapi.json for coding agents.
- Action MCP servers: local `npx @yuno-payments/yuno-mcp@latest` and hosted `https://mcp.prod.y.uno/mcp` (API-key auth); tools cover customers, payment methods, checkout sessions, payments, payment links, subscriptions, recipients, installment plans. Remote server enforces rate limits, IP binding and session expiry.
- Agent Toolkit (TypeScript) with adapters for Vercel AI SDK, Google Genkit, LangChain, OpenAI Chat and OpenAI Agents SDK; docs describe it as "one integration to access 300+ payment providers globally".
- Yuno connector for Claude (announced 28 Sep 2026, "available now") and a Yuno app in ChatGPT; Grok connector "coming soon". The press release describes the Claude connector as read-only analytics; the docs FAQ says the connectors can also run payment operations (create, capture, cancel, refund, manage subscriptions and links) with a confirmation step on production. Two sources disagree; confirm scope before promising it.
- Maia (AI technical account manager in chat widget, Slack, Google Chat, WhatsApp, email), Payments Concierge (AI payments analyst) and NOVA (AI decline recovery on WhatsApp and voice) are covered in section 3.

**Internal signals (memory):**
- German has pitched "Google Universal Commerce Protocol / agentic checkout" to Gap (22 Jul 2026, no reply) and later switched to a POS angle; guidance is to never reuse that text with the same contact.
- In the Hostinger call (Sep 2026) the merchant preferred stablecoin protocols (x402, Cloudflare wallet, MPP) over card rails for agent payments, and a Yuno person (Antoine) asked for merchant feedback "for the design of Yuno's MPP integration". So an MPP integration was in design in Sep 2026 [internal, status unknown].
- In the Autodesk deck (26 Oct 2026) "agentic commerce" sits on the "what's new / beyond the RFP" slide next to stablecoins and banking, and German swapped that card out for "Multiple entities" in the final cut. Agentic is a secondary "what's new" talking point in NorthAm decks today, not the lead pitch [INFERENCE].
- A LinkedIn post by a Yuno executive mentions a Mastercard partnership on agentic payments in LatAm and the Caribbean; no press release found [UNVERIFIED].

**How it is pitched:** "be agentic-ready with one integration on top of the payment stack you already have", with the catalog, checkout and payment handled by Yuno so the merchant is purchasable inside assistants, and conversion claims of 2 to 6x. For US prospects, the safer line is the one Yuno's own battlecard uses: "agent payments still need a provider to authorize them; Yuno covers that part as well."

Sources
- https://y.uno/en/product/agentic-commerce
- https://y.uno/post/can-ai-agents-buy-things-autonomously-inside-the-agentic-commerce-protocol (12 May 2026)
- https://docs.y.uno/docs/ai-capabilities (hub), /setup-mcp, /docs/ai-capabilities/remote-yuno-mcp-server, /docs/ai-capabilities/agent-toolkit, /docs/ai-capabilities/use-yuno-with-claude-and-chatgpt, /docs/ai-capabilities/build-with-ai
- https://y.uno/en/newsroom/yuno-and-claude (28 Sep 2026)
- Memory: project_gap_inc.md, project_hostinger.md (call 24 Sep 2026), project_autodesk.md; Vaulting/Yuno Vault vs Basis Theory vs VGS.md ("We are built for AI agents" row)
- Web search 27 Oct 2026 ("Yuno agentic commerce protocol"), LinkedIn mention unconfirmed

---

## 3. Orchestration

**Routing engine (docs, Routing API GA):**
- Dynamic routing on conditions: amount, BIN, card brand, country, currency, installments, transaction type, metadata, time period and volume or count limits; ordered condition sets, first match wins.
- Steps: provider steps (payment, fraud, 3DS, authentication), action steps (CAPTURE, HOLD_FOR_REVIEW, CANCEL, REVERT), delayed capture from 1 minute to 7 days, `retry: true` re-attempts the same provider once on DECLINED or INTERNAL_ERROR, `next` and `next_split` send fallbacks to one or several providers by percentage, `start_split` A/B tests providers from the first attempt.
- Smart Routing step: Yuno picks the provider per payment among 2 to 4 connections by COSTS (needs costs loaded per connection) or LATENCY, with decline types that stop further attempts; card routings only, one smart step per route. Dashboard describes the objectives as "conversion rate and latency" or "conversion rate and costs".
- Routing recommendations (Beta): routes ranked from the merchant's own reported history, objectives APPROVAL_RATE, LATENCY, BALANCED; "there is no cost objective yet".
- Monitors: approval-rate threshold per route; alerts by email or Opsgenie; automatic redirection to fallback providers while a small share keeps probing the original; automatic return when the rate recovers. Pricing policy lists Monitors at $0.02 per alert (list) and German usually bundles them in the platform fee.
- Transaction retries: failed captures and refunds retried up to seven times in 96 hours.
- Published routes stay editable; audit logs cover routing, connections and monitor events.

**Network tokens, account updater, 3DS, one-click:**
- Network tokens provisioned automatically for every vaulted card; Visa and Mastercard live, Amex "still in certification" per engineering on 5 Oct 2026 (docs list Amex); cryptogram API lets a Yuno network token be authorized on an external PSP; passkey authentication on network tokens (pilot). List price $0.35 per token creation, $0.07 per update (min $0.20 / $0.04).
- Card Account Updater: Visa, Mastercard, ELO; token and fingerprint stay the same, webhook on update; bulk registration up to 100 vaulted tokens per request; enabled per organization. Internal uplift target 1.2 to 2.8 approval points; list $0.40 per update.
- 3DS: Yuno 3DS (providers Netcetera, Checkout.com, Cybersource), external 3DS, 3DS standalone returning ECI and CAVV for any acquirer, native mobile challenge SDKs, SCA exemptions. List $0.06 per authentication attempt.
- One-click: vaulted tokens across Full, Lite, Seamless and Headless SDKs; Click to Pay; Apple Pay and Google Pay express checkout with in-sheet shipping; PayPal enrollment and vaulting element; the vaulted token carries the fraud data of every configured fraud provider.

**Vault:** PCI DSS Level 1; one vaulted token works on every processor connected to the account (no re-tokenization); token import (PGP over SFTP) and export to any receiver with a PCI AOC; forward PCI Proxy to allowlisted hosts (beta, enabled per org); product page adds a standalone vault with custom schema, identity documents and role-based access (docs do not yet describe identity data, so confirm with Product before writing it). Vault is $0 inside the core platform; vault-only is $500 per month plus $0.00015 per stored card per month.

**No-code connections:** Dashboard "Connections" Explore tab lists providers (payment methods, processors, anti-fraud); three-step connect (credentials, optional costs, accounts); costs feed both Smart Routing and fee reconciliation; a Connections API and provider catalog endpoint expose the same thing programmatically. Marketing line: "Add APMs, PSPs, cards, or risk tools without writing a single line of code" and "go live in weeks, not months". New connectors and their maintenance are included for the life of the contract (internal fact file).

**Coverage numbers (use one consistent set):** 1,000+ payment methods, 460+ integrations, 190+ countries, 180+ currencies (y.uno). Older or divergent figures still appear: "200+ countries" on blog posts, "300+ payment providers" in the Agent Toolkit docs, "450+" in old decks (banned internally). North America panel: 20+ countries, 60+ providers.

**Checkout and SDKs:** Full, Lite, Seamless, Headless and Secure Fields on Web, iOS, Android, Flutter, React Native; WooCommerce and VTEX plugins; payment links; Checkout Builder (no-code form behavior); 70+ languages (per comparison pages); most SDK merchants qualify for SAQ A.

**Payments Concierge (AI payments analyst):**
- Docs (Oct 2026): an AI agent "like a payments analyst on your team" in Slack, WhatsApp, Telegram or Microsoft Teams, 24/7; answers "why did my approval rate drop in the UK this week", explains root cause to issuer level, recommends an action, builds reports; proactive scheduled briefings (daily volume and approval, per-provider breakdown, top decline reasons, anomaly flags); admin tabs Access, Scheduled tasks, Concierge knowledge; in Slack it appears as "@Tom (Payments Concierge)" through a Slack Connect channel created by the TAM.
- Internal deck (Assets/Yuno_Payments_Concierge.pdf, 14 pages): exports to CSV, XLSX, PDF, PPTX, Word; alert types (approval drop, rejection spike, unusual volume); "<2s response time", "+2h weekly savings"; 4-week pilot; v1.1 roadmap (latency analysis, routing recommendations, anomaly alerts, cost optimization, "Feb"), v1.2 API access, v2.0 white label. The deck lists WhatsApp alerts as "coming soon" while the docs now list WhatsApp as live, so the deck is older than the docs.
- Internal writing rule: describe the Concierge in 2 to 3 sentences in emails. The 26.49 pp PayPal-vs-card stat that came out of the Concierge is Reface, anonymized, a spread between methods, not a retries proof, and Comms must approve external use.

**Maia (AI TAM) and NOVA (AI recovery):** Maia answers integration and payment questions in the support chat, Slack, Google Chat, WhatsApp and email and analyzes three months of patterns. NOVA recovers declined payments and abandoned carts by WhatsApp and outbound AI voice calls; public claims 75% recovery rate, 70+ languages, 190+ countries, quote from Rappi's Global Head of PayIns; pricing policy shows NOVA at "cost plus, pending" with reference costs of about $0.01 per WhatsApp message.

**Published proof points (and which to use):**
- Homepage: "up to a 7% uplift in approval rates", "30% recovered revenue", "27% savings on payment costs", "90% reduction in development time".
- Smart Routing product page and the 2026 orchestration post: "8% auth-rate uplift" (average) and "30% decline recovery" or "about 8% of transactions recovered via fallback". The 7% and 8% figures coexist on y.uno; internal rule is 7% and 30%, one set per deck.
- Series B release: $5B+ failed volume recovered in a year, approval rates up about 5%, $500M+ processing costs saved.
- Customer results: inDrive about 90% approval and 10 to 11 new countries live in under eight months (y.uno says 11, the orchestration post says 10); Rappi "implementation time for new providers down to zero", provider-disruption detection "from 5 to 10 minutes to milliseconds", 80% less analyst time; Livelo 50% of failed transactions recovered and +5 points approval; Reserva +4 points in under three months; Vibra 80% new-user approval; Wingo +14% approval after Smart Routing (newsroom); McDonald's (Arcos Dorados) unified 21 LatAm markets, "higher approval rates", no percentage; Viva Aerobus 75% of contacted customers recovered with average ticket over $300 (NOVA); Risk Conditions 29% fraud reduction.
- Banned internally (no source): "+12% auth uplift", "20 to 30% decline recovery", "McDonald's +4.7% / 18 markets / $3.2M", "450+ providers", "typical migration about a week", "$100B TPV / 150 merchants" house slide unless German confirms. Uptime and SLA numbers are deal-specific and never printed.

Sources
- https://docs.y.uno/reference/organizations/routing/create-routing, /routing-resource-shape, /get-routing-recommendations
- https://docs.y.uno/docs/using-yuno/dashboard-overview/routing, /monitors, /automation, /connections
- https://docs.y.uno/docs/security-and-compliance/network-tokens, /pci-compliance, /pci-proxy/overview; https://docs.y.uno/docs/additional-services/card-account-updater; https://docs.y.uno/docs/payment-features/3ds-standalone; https://docs.y.uno/docs/basic-concepts/tokens
- https://docs.y.uno/docs/ai-capabilities/payment-concierge, /maia-ai-technical-account-manager, /nova
- https://y.uno/en/product/smart-routing, /integrations, /vault, /nova
- https://y.uno/post/best-payment-orchestration-platforms-in-2026 (22 Apr 2026)
- https://y.uno/en/success-stories and https://y.uno/en/newsroom/wingo-improves-payment-efficiency-with-yuno-as-strategic-partner
- Local: Assets/Yuno_Payments_Concierge.pdf; Assets/research-skill-v8.md; Vaulting/Yuno Vault vs Basis Theory vs VGS.md (8 Oct 2026)
- Memory: feedback_published_stats_only.md, reference_yuno_pricing_policy.md, reference_subscriptions_stats.md, feedback_concierge_short.md

---

## 4. Reconciliation

**What the product does (docs, Oct 2026):** compares every transaction processed through Yuno with the settlement files of each payment provider, checks balances with acquirers and verifies records. Each transaction gets a reconciliation status: RECONCILED, NOT_RECONCILED (still inside payment terms or pending), CONFLICT (found but amounts differ), NON_RECONCILABLE; sub-status AUTOMATICALLY, MANUAL or PENDING. The dashboard shows the reconciliation rate by provider, account and currency. Three reports: Reconciliation Overview, Settlements and Fees (per transaction: settlement batch id visible on the bank statement, settlement and estimated settlement dates, acquirer, gross and net, provider fees, settlement fees, taxes, local retention, FX rate, card data, country) and Settlement Payouts (gross, fees and net of each transfer a provider reports having paid, API only, "no dashboard tab yet", available only to organizations on "Yuno's new reconciliation engine"). All three are available through the Reports API for bookkeeping systems. Docs recommend daily reconciliation. Provider costs entered on each connection drive fee reconciliation. An in-person reconciliation page covers POS settlements for omnichannel merchants.

**How the product page sells it (y.uno/en/product/reconciliations):** headline "Know what every provider owes you." Any PSP, acquirer or bank via API, SFTP or file; across currencies and entities; online and in-store; pre-built editable rules; exceptions sorted by cause with items still inside the settlement window excluded; "AI agents explain each exception every morning" so a person assigns an owner; flags fees above contract terms; one standard report with settlements traceable to payouts; "~99% reconciled on a typical day" and "~10 min to connect a provider"; "Already on Yuno? Connected from day one. Not on Yuno? It works the same" (so it can be sold standalone to a merchant that does not route through Yuno).

**Status caveat:** three internal sources disagree in time. Sep 2026 deck QA (feedback_published_stats_only) required footnoting "settlement, payout and fee reconciliation" as roadmap; the Finance pricing policy (Jul to Sep 2026 draft) lists Reconciliation as Live with packs; docs in Oct 2026 describe a "new reconciliation engine" with the Settlement Payouts report on API only. Read: the engine is live and being migrated organization by organization; confirm with Solutions Engineering which providers and reports are GA for a given prospect before committing to a close-the-books use case [INFERENCE].

**Pricing (Finance policy, internal only):** list $2,500 per month plus $0.03 per reconciled transaction; minimum $1,500 plus $0.0085. Packs: 50K transactions $1,500 plus $0.032 extra; 250K $5,000 plus $0.022; 1M $14,000 plus $0.016; 3M $30,000 plus $0.0085. Deal examples: UNICEF Colombia proposal at $0.012 per reconciled transaction, optional and outside the core total (Oct 2026); Appmaking asked for a reconciliation and network-token ballpark (Sep 2026).

**Which merchants use it:** no public case study or named merchant for reconciliation on y.uno or in the newsroom. Internal pipeline mentions only (not live): UNICEF Colombia (proposal), Appmaking (ballpark), PedidosYa (B2B collections, "a reconciliation engine that matches payments with partners without manual receipts"), Experian DataCrédito (subscriptions call). Live reconciliation customers: none verifiable from the sources reachable in this session [UNVERIFIED].

**How it is positioned for Finance, Treasury and PayOps (from the 13 buyer personas and the product page):**
- Controller / Head of Finance Ops: faster month-end close, match rate, fewer manual adjustments, audit trail per market, one source of truth for payments data.
- Treasurer: settlement visibility per provider and currency, predictable settlement timing, what each provider still owes, FX at settlement.
- Head of Payment Operations: exceptions sorted by cause with an owner, fee audit against contract, one place for refunds and chargebacks across PSPs.
- CFO: cost of payments, fees above contract flagged, vendor consolidation.

Sources
- https://docs.y.uno/docs/using-yuno/dashboard-overview/reconciliations (full page read via docs MCP)
- https://docs.y.uno/reference/reports/reports-fields (Settlements & Fees, Settlement Payouts)
- https://docs.y.uno/docs/glossary#reconciliation; https://docs.y.uno/docs/using-yuno/dashboard-overview/connections (costs for fees)
- https://y.uno/en/product/reconciliations
- Memory: reference_yuno_pricing_policy.md (Finance, Laura Galan, Doc 11_giTduW5K...), feedback_published_stats_only.md, project_unicef_colombia.md, project_appmaking.md, project_pedidosya.md, reference_buyer_personas.md

---

## 5. Subscriptions and recurring

**Engine (docs):**
- Plans with base amount, per-country prices, phases (trial, intro price, regular price), trials; subscriptions created from a plan or inline; `execution: YUNO` (Yuno bills) or `MERCHANT` (record only); one-call "start with payment" that creates charge and subscription atomically (no charge, no subscription); pause, resume, cancel, change plan (KEEP or RESTART), PAST_DUE state (opt-in per account) with a webhook on every transition; soft descriptor per rebill; usage meters (included credits, per-unit, package, tiered; overages on next cycle); promotions and discount engine (Q3 2026).
- Smart Retries: `retry_on_decline` is the only switch; up to six attempts (production cap, an RFP once said five); schedules DEFAULT (5h, 12h, 24h, 36h, 48h, 96h), SMART (ML by decline reason, country, issuer, provider) and CUSTOM_SCHEDULE (1 second to 7 days per attempt); stop on hard declines; `cancel_on_exhausted_retries`; A/B split of retry strategies per plan from the dashboard; manual Retry endpoint for mid-cycle card updates; retries can be routed through a different PSP than the first attempt (product page). Pix Automático subscriptions follow the rail's own ladder (3 retries within 7 days).
- Methods on one subscription object: cards, Apple Pay, Google Pay, PayPal (billing agreement enrollment), Pix Automático; UPI Autopay mandates documented separately.
- Stripe Billing bridge: Stripe stays the billing engine, Yuno collects the method and runs the charges in Stripe's third-party processing mode; events mirrored (invoice.payment_failed to SUBSCRIPTION.PAST_DUE); Stripe Checkout, Stripe Smart Retries, recovery emails and Stripe-managed disputes do not carry over; Stripe must enable third-party processing; first payment reported within 23 hours; Stripe's Billing fee still applies to off-Stripe volume. Also a Stripe-compatible endpoint ("Stripe Proxy") to point existing integrations at Yuno.
- Dunning: no end-customer dunning emails; recovery is retries plus NOVA WhatsApp or voice outreach, plus "enroll cards with payment links" to replace a declining card.
- Account updater and network tokens keep vaulted cards current before the renewal fails (docs: "reduced declines: network tokens automatically update when cards are renewed or reissued").

**Public page:** "Subscriptions on any PSP. Recover what fails." No published recovery, uplift, merchant or subscription numbers on y.uno (checked 27 Oct 2026).

**The internal figure (16 merchants / 135K subs / 83 to 86% / 69K reactivated): verified as internal, not public.** Source is the "Yuno Subscriptions, Internal Launch" deck (offsite 7 to 11 Sep 2026) and Daniel Lozano's Google Slides, with Control Center data as of 31 Aug 2026: 16 merchants in production, 135K active subscriptions, 86% approval per cycle after retries vs 83% first attempt, 69K past-due subscriptions reactivated within 30 days. The deck is marked "internal, do not forward"; Daniel Lozano (PM) must OK any external use. Magdalena used "16 merchants / 135K" in outbound on 15 Sep 2026. Related internal numbers that must stay internal: $1.3B per quarter of recurring volume across 65 merchants with 97% outside the engine, $7.2M per month of declined renewals in the engine portfolio (Jul 2026), 47.5% first-attempt approval on recurring attempts. Glean could not be used to re-verify any of this today.

**Gaps (Jarrett, 31 Aug 2026, partly outdated):** no bundles, add-ons or multi-line items, no proration, no entitlements, no invoicing, tax or credit notes, no end-customer dunning emails, no rev-rec or ERP sync. His guidance: do not pitch Yuno as a full billing engine to anyone who needs those; pitch it as the recurring payments and recovery layer on any PSP (the Stripe Billing bridge covers the billing-engine gap).

**Commercials:** Finance policy lists Subscriptions at 0.7% of TPV list, 0.3% minimum, billed on top of pay-ins, first $50,000 of monthly subscription TPV included in pay-ins, and still marks it "under development, not sellable yet" (Jul to Sep 2026 draft) even though German sells it (Suno, Peacock, Anthropic, Luni); confirm with Finance before quoting. German's outreach line "first $50K processed free, then $0.05 per transaction" versus Stripe Billing's $0.07 is a lightweight default, not policy.

**Vault-first motion:** several NorthAm pursuits lead with the PCI vault plus network tokens and add PSPs later: Chess.com (vault and network tokens first, then another PSP, late Q1 2027), Hostinger (vault-as-a-service, India first), Autodesk (vault plus orchestration RFP, 12-slide deck 26 Oct 2026), Waymo (token vault RFP), OnlyFans and Poshmark (vault decks), Appmaking (TRID, network tokens, reconciliation). The battlecard line: a standalone vault solves card storage and PCI scope; Yuno solves that plus the reason the buyer wanted a vault, which is freedom to add, switch and combine providers, so "two projects become one". Recurring merchants get the retries, account updater, network tokens and PSP fallback on the same token.

Sources
- https://docs.y.uno/docs/payment-features/subscriptions/retries, /plans, /start-with-payment, /stripe-billing, /pix-automatico; https://docs.y.uno/reference/subscriptions/retry-subscription, /the-subscription-object, /update-subscription; https://docs.y.uno/reference/plans/retrieve-plan; https://docs.y.uno/changelog/whats-new (Q2 and Q3 2026)
- https://y.uno/en/product/subscriptions
- Memory: reference_subscriptions_stats.md (18 Sep 2026), project_yuno_vs_stripe_subscriptions.md, reference_yuno_pricing_policy.md, reference_yuno_pricing.md, project_chess_com.md, project_hostinger.md, project_autodesk.md
- Local: Vaulting/Yuno Vault vs Basis Theory vs VGS.md; .claude/skills/yuno-sales-deck/references/yuno-facts.md

---

## 6. Customers

Legend: PUBLIC = logo or name on y.uno, newsroom or press; STORY = y.uno success story with result; INTERNAL = known inside Yuno only (ask the owner before naming externally). Region = where the business is based.

| Customer | Vertical | Region | Evidence | Numbers |
|---|---|---|---|---|
| McDonald's (Arcos Dorados) | QSR / retail | LatAm (21 markets) | PUBLIC, STORY, Series B release | Unified 21 markets, "higher approval rates", no % |
| Rappi | Delivery / super app | LatAm (Colombia) | PUBLIC, STORY, Series B, NOVA quote | New-provider implementation time to zero; detection ms vs 5 to 10 min; 80% less analyst time |
| inDrive | Mobility | Global (LatAm focus) | PUBLIC, STORY, Series B | ~90% approval; 10 to 11 countries in under 8 months |
| Uber | Mobility | US (SF), global | PUBLIC logo; INTERNAL active relationship | None public |
| NetEase Games | Gaming | APAC (China) | PUBLIC, Series B | None |
| Garena | Gaming | APAC (Singapore) | PUBLIC logo | None |
| Moon Active | Gaming | Israel | PUBLIC logo; INTERNAL sheet | None |
| Ant Group | Fintech | APAC | PUBLIC logo | None |
| Tada | Mobility [INFERENCE on vertical] | APAC | PUBLIC logo | None |
| GoFundMe | Fundraising platform | US (San Diego) | PUBLIC logo, Series B, Claude and Coinbase releases; INTERNAL first Marketplace merchant (live 19 Feb 2026, Stripe + Adyen + Tabapay) | Volumes internal only |
| Whop | Digital products marketplace | US (New York) | PUBLIC logo; INTERNAL sheet | None |
| Despegar (Decolar) | OTA | LatAm (Argentina) | PUBLIC logo; INTERNAL sheet | None |
| Hotmart | Digital products | Brazil | PUBLIC logo | None |
| Viva Aerobus | Airline | Mexico | PUBLIC, STORY; INTERNAL sheet | NOVA: 75% of contacted customers recovered, ticket over $300 |
| Copa Airlines | Airline | Panama | PUBLIC logo; INTERNAL sheet | None |
| Wingo | Airline | Colombia | PUBLIC newsroom | +14% approval with Smart Routing |
| Avianca | Airline | Colombia | PUBLIC (TechCrunch 2024) | None |
| Livelo | Loyalty | Brazil | PUBLIC, STORY | 50% of failed transactions recovered; +5 points approval |
| Reserva | Fashion retail | Brazil | PUBLIC, STORY | +4 points in under 3 months |
| Vibra | Fuel retail | Brazil | STORY | 80% new-user approval |
| Kavak | Used-car marketplace | Mexico | PUBLIC logo | None |
| Carrefour | Retail | Region not stated on y.uno | PUBLIC logo | None |
| Open English | Edtech | US (Miami) | STORY; INTERNAL sheet | No numbers |
| Global game publisher (anonymous) | Gaming | n/a | STORY | No numbers |
| SpaceX / Starlink | Satellite internet | US | INTERNAL (German's customer line; logo-wall rule) | None |
| Samsung | Electronics | Korea / US | INTERNAL (German's 26 Oct customer line) | None [UNVERIFIED beyond that line] |
| Qatar Airways | Airline | Qatar | INTERNAL (fact file, sheet) | None |
| Allegiant Air | Airline | US (Las Vegas) | INTERNAL, signed Oct 2026, first NA airline logo; Samuel Vieira and Adam Mawdesley | None |
| Kraken | Crypto exchange | US (SF) | INTERNAL sheet "Yuno customers (removed)" | None |
| Crypto.com | Crypto | Singapore | INTERNAL sheet; also a 2026 stablecoin partner | None |
| Automattic | Web / SaaS | US (SF) | INTERNAL sheet | None |
| Fever | Live entertainment | US (NY) / Spain | INTERNAL sheet; "CFO Copilot in beta with Fever" note | None |
| Skool | Community platform | US (LA) | INTERNAL sheet; flagged as existing customer in Core ICP | None |
| xAI (Grok) | AI | US (Palo Alto) | INTERNAL sheet (removed from AI prospects 12 Oct 2026 as existing customer) | None |
| Yango | Mobility | CIS / LatAm | INTERNAL (Sr KAM owns it; expansion proposal) [INFERENCE: existing account] | None |
| OpenAI, Lovable | AI | US / Sweden | INTERNAL (named as references in German's Feb 2026 LinkedIn opener) [UNVERIFIED] | None |

Not customers, despite appearing in the question: Crunchyroll (Stripe Sessions prospect research only), Shein (top-rated prospect in TCL, no customer evidence), Suno (prospect; Madden paused 21 Sep 2026). Riot Games: closed core, no RFP in 2 to 3 years; nothing about Riot ever goes to a third party. PedidosYa, Localiza, Super.com, Patreon, NYT, HBO Max, Peacock, Thinkific, GoDaddy and the rest of the Core ICP tab are pipeline, not customers.

**US / North America read:** publicly namable US customers today are GoFundMe and Whop (plus Uber by logo, and Open English via its story). Internally known US customers: SpaceX/Starlink, Allegiant, Kraken, Automattic, Skool, xAI, Fever, and Samsung by German's line. Partners that are also brand names in the US (never pitched as merchants): PayPal, Coinbase, Revolut, dLocal, EBANX, Shopify, Affirm, Nium, Bitso.

Sources
- https://www.y.uno/en (logo wall), https://www.y.uno/en/about (names), https://y.uno/en/success-stories (and each story page), https://www.y.uno/en/newsroom/yuno-series-b, https://y.uno/en/newsroom/yuno-and-claude, https://y.uno/en/newsroom/yuno-and-coinbase, https://y.uno/en/newsroom/wingo-improves-payment-efficiency-with-yuno-as-strategic-partner, https://techcrunch.com/?p=2673996
- Google Sheet 1_OhZny-TZBdIIOqHfdV5MzLGH9Bi9KmuUxD1TwfYk8A, tab "Yuno customers (removed)" (read 27 Oct 2026)
- Memory: project_gofundme_marketplace.md, project_allegiant_signed.md, feedback_keep_spacex_logo.md, project_suno_jasper.md, project_riot_games.md, project_yango.md, reference_core_icp_vs_master_sheets.md, Grokbot/prompts/00-SHARED-CORE.md (section 0.4), project_tcl_agent.md

---

## 7. How Yuno runs and sells

**Org structure (from memory and the Grokbot people map; titles as recorded, not re-verified via Glean):**
- Regions: LATAM (GM Walter Campos), APAC (GM Chee Beh), EMEA (Piotr Sierpinski, Sales Manager Europe), North America (Sean Calabro, Head of North America; Melissa Pottenger, VP Enterprise Growth NA). CRO Justo Benetti leads strategic deals (Carry1st, CellPoint, OnlyFans, Autodesk reviews). Head of GTM Bernabé Murata. Banking and FI is a separate line (Mauricio Schwartzmann).
- NorthAm selling roles: AEs and BDMs (German Tatis AE; Samuel Vieira AE in SF owning Waymo, Collinson, Adobe, Discord, Poshmark, OnlyFans vault; Joaquin Mann BDM NA, joined Sep 2026; Alejandro Albarracín on Paramount and Cruz Verde; Alejandro Bernal on Upwork; Rasheed on DoorDash); Sales Strategy Associates running SDR campaigns and hand-offs (Magdalena Torrealba, also owns Pipeline Sync and the web deck tool; Samuel Carreño); SDR Susana "Susi" Awad (inbound LatAm, intros, event meetings).
- Sales Engineering and implementation: Jarrett Falasco (SE, product on subscriptions and marketplace, ex-CellPoint), Carlos Medina (implementation engineer, Bogotá, runs dashboard demos), Dirk and TJ (SEs on Hostinger), Drew Snyder (demos), William Wong and Juan Ferrari (implementation), forward-deployed engineers offered on strategic deals.
- Post-sale: KAM (Maria Jose Pineda Sr KAM on Yango), TAM (Tomas Calle Espinal on GoFundMe), tier-3 engineering, executive sponsor and QBRs, 24/7 tier-1 support, lifetime connector engineering; AI layer Maia (TAM) and Payments Concierge delivered through Slack Connect.
- Support functions: RevOps and Salesforce (Felipe Triboni), Finance pricing (Laura Galan, #finance-merchants), Legal and NDAs (Ivvy Soberay, #salesops-legal), Product (Daniel Lozano PM Subscriptions; Caio Freitas on product demos; Antoine on MPP design), Yuno Agents platform team ("ia-crew": Simón Martínez, Gustavo Mendes, Rafael Tejon, Ben Lee).
- Operating cadence under Sean (from 1 Sep 2026): one pipeline file per rep, Thursday noon NorthAm forecast (target vs forecast, deals, gap, plan), multi-year pipeline building ("mark it, work it, buy it", position two years ahead), comp as a flat rate per dollar generated with cliffs.
- Salesforce process: BDMs create the opportunity from a Lead ("Convert to Deal") or a Contact; "Set Pricing" routes to Finance approval; prices outside policy are not booked.

**Commercial model (Finance policy, internal; all USD):**
- Platform fee per month by size segment: V1 (<25K monthly pay-in tx) $5,000; V2 (25K to 100K) $7,000; V3 (100K to 1M) $10,000; V4 (1M to 5M) $16,000; V5 (>5M) $25,000; minimum $4,000; never waived (waiver goes to Yellow). Includes connection management, routes and rules, transaction management, reporting, checkout builder, 20 seats, webhooks, PCI vault.
- Pay-ins per successful transaction: $0.10 list, $0.01 floor, fixed or % of net TPV, tranches by default (tiers only when the deal demands); never bundled or free; declines cost nothing.
- Add-ons metered: network tokens, account updater, Yuno 3DS, monitors, risk conditions, fraud engine, chargeback alerts ($15 per matched alert), reconciliation, pay-outs ($0.07), subscriptions (0.7% TPV, status caveat), NOVA (cost plus).
- Levers: tranches, tiers, price splitting by business unit, country, time phase or method; credits against platform fee or MMG for the integration ramp; MMG (monthly minimum guarantee) with true-up; annual upfront billing of platform fee and MMG (monthly via Yellow); net 30.
- Approval zones: Green auto-approved in Salesforce, Yellow (RevOps, Sales Ops or GM, 2 business days), Red below minimum (Global Controller/CFO plus CRO, 5 business days). "Overall deal size cannot be under 10k." Strategic merchant: TPV at or above $38.0M per month or 1.2M pay-in transactions per month, or two of market recognition, referenceability, beachhead value, halo effect.
- Industry margin segmentation for pay-in prices: M1 thin (<15%: airlines, delivery, mobility, remittance), M2 mid (retail, travel, ticketing, marketplaces, e-learning), M3 healthy (gaming, gambling, streaming, edtech, hosting), M4 rich (>60%: software, AI, digital goods, luxury, social, crypto).
- Outreach default (not policy): "the first $50,000 processed is free, then $0.05 per transaction", labeled "standard pricing" in decks when no negotiated pricing exists. Shapes seen in approved deals: success-based tranches, ramping monthly minimum, platform fee plus lower per-transaction, flat fee up to a cap, annual platform fee for low-count high-ticket merchants, metered add-ons, go-live credits, paid POC with an exit.

**ICP as written internally:**
- /newaccounts command: based in North America (US or Canada); 100K+ digital transactions per month (or strong signals: high revenue, large user base, digital-first); operating in AI, SaaS, gaming, iGaming, sports betting, airlines, digital products and subscriptions, parking, car rental, web and cloud hosting, cybersecurity and VPN, retail and e-commerce; global or multi-market presence preferred; already processing payments digitally; mid-market to enterprise. Anti-ICP: very low digital volume, pure brick-and-mortar, already on the team's exclusion list.
- Grokbot shared core (Oct 2026): "a digital merchant with 120K+ online transactions a month (100K+ acceptable, 25K+ only if the platform fee still makes sense), selling in several countries or about to, with more than one processor or a risky single-processor dependency, and with local payment method gaps." Strongest triggers: new Head of Payments or Payments PM, several payments roles posted, PSP migration or outage, expansion, funding round or IPO filing, checkout redesign, public complaints about declines or billing, an RFP for vault, orchestration or processing. Anti-ICP adds invoiced B2B with no online checkout, pre-revenue, China HQ, accounts owned by another rep, existing customers; PSPs, wallets, acquirers, banks and aggregators are partners, never merchants.
- Research rubric v8 (urgency, verified signals only): 3+ countries +3, multiple PSPs +3, public RFP +3, recent expansion +2, public payment issues +2, funding over $10M +2, LatAm/APAC/MENA traffic +2, no orchestrator +2, payments job postings +1; High 12+, Medium 7 to 11, Low under 7. Deal size is a separate axis (V1 to V5).
- Core ICP workbook (NorthAm ICP sheet 1_FLbJCR8..., tab Core ICP, 226 companies as of 26 Oct 2026, with a WHY column per row and a 0 to 100 priority sort). "Yuno Fit" rubric used on 26 Oct: 5 = multi-market plus multi-PSP, competitor orchestrator in place, or active RFP; 4 = strong with one caveat (single PSP, giant procurement, non-US, stack unverified); 3 = real volume and own contracts but single market or narrow angle; 2 = app-store, Shopify or franchise captive, DTC minority, declining; 1 = payments provider itself, in-house builder, invoiced B2B, lost or declined, being absorbed.

**Sales motions in use:** RFP entry (direct emails: context, "we do both, we would love to be considered", one ask); vault-first (Chess.com, Hostinger, Autodesk, Waymo, OnlyFans, Poshmark); orchestration-first (Autodesk final deck, Carry1st, Yango); subscriptions engine and Stripe Billing bridge (Suno, Peacock, Anthropic, Luni, Experian); marketplace and payouts (GoFundMe as reference, Eventbrite, Thinkific); reconciliation as a Finance entry point (UNICEF, PedidosYa); white label and partner (CellPoint APM proposal, Carry1st/Pay1st, Getnet MoR); POS orchestration and Tap to Pay (Gap; product launched 29 Sep 2026); agentic commerce and stablecoins as "what's new" items; event-driven outreach (Money20/20 Vegas, SF after-hours).

**Internal tooling:** Yuno Agents platform (ai.agents.y.uno: owner plus admins, Personal vs Service agents, Public/Private, toolkits, skills, channels, scheduled tasks, evals); Lucky (BD deal strategist between discovery and demo: MEDDIC doc plus account plan from transcripts and research, DeepSeek via OpenRouter); Eve (SF events agent fed by a Google Sheet); Milo (hourly intro routine); Payments Concierge (also used internally in #roberto-ai for merchant stats); Grokbot bots (SCOUT, PREP, DEEP, DECK, COACH); deck.yuno.tools and the pitch-maker; Target Company List and Deal Status GTM sheets with the Pipeline Sync Apps Script; Gong, Salesforce, Glean, the Yuno docs MCP, the Finance pricing calculator.

Sources
- Local: Grokbot/prompts/00-SHARED-CORE.md (sections 0.3 to 0.7, 0.11, 0.12); .claude/commands/newaccounts.md; Assets/research-skill-v8.md; .claude/skills/yuno-sales-deck/references/yuno-facts.md
- Memory: project_sean_calabro_manager.md, reference_yuno_pricing_policy.md, reference_yuno_pricing.md, reference_salesforce_opp_process.md, reference_core_icp_vs_master_sheets.md, reference_yuno_agents_platform.md, project_lucky_agent.md, project_eve_events_agent.md, project_milo_intro_routine.md, project_grokbot_bots.md, feedback_rfp_entry_emails_direct.md, project_poshmark.md, project_allegiant_signed.md, project_cruz_verde.md, project_palco_ticketing.md, project_hostinger.md, project_gofundme_marketplace.md

---

## 8. Competitive landscape as Yuno frames it

Yuno publishes "Yuno vs" pages for Primer, Payrails, Gr4vy, Spreedly, Ixopay, Solidgate, BlueSnap, CellPoint Digital, APEXX Global, Juspay and Tuna. The common frame: 190+ countries and 1,000+ methods versus regional players; AI routing, AI recovery and AI fraud versus rules; SOC 2 plus ISO 27001/27701 versus missing certifications; disputes, chargeback alerts, reconciliation, subscriptions and payouts as "enterprise tools"; single fast integration; and provider neutrality (no acquiring, so routing serves the merchant). One line each:

- **Spreedly:** the oldest orchestrator (2007, orchestration since 2013), mature API-first vault with "universal tokenization" and Data Explorer, strong in North America, Europe and LatAm; Yuno says Spreedly's AI is limited to support tooling, it lacks ISO 27001/27701, reporting and pre-chargeback alerts are weaker, onboarding is complex. In NorthAm practice Spreedly is the incumbent at HBO Max, Peacock, NYT, SeatGeek, Lemonade, Priceline; the Yuno answer is the same vault portability plus routing, retries, monitors and subscriptions on the token.
- **Primer:** Europe-focused, "a relatively smaller player"; Yuno claims Primer has no dispute or chargeback platform, basic orchestration and limited AI, fewer direct APM and scheme connections, and (per Yuno) lacks SOC 2 Type II.
- **Gr4vy:** no-code cloud orchestrator; Yuno credits its simplicity, then claims no native AI engine, manual rules, limited reporting, missing ISO 27701 and "an average of 90 days to implement". Noted in travel: Gr4vy closed an exclusivity with Datalex (Aug 2025).
- **Adyen and Stripe native routing (single-processor platforms):** Yuno's orchestration post argues that providers who run their own rails have a conflict of interest in routing, while Yuno does not sell acquiring. Against Stripe Billing specifically: Stripe's subscription engine is wired only to Stripe, the merchant builds any other processor integration itself, and Stripe charges $0.07 per transaction versus Yuno's $0.05 line; Yuno's engine routes renewals across PSPs. Internal honesty rule: Stripe Billing's catalog, proration, dunning automations and customer portal are real strengths; do not concede or hide them without checking.
- **CellPoint Digital:** travel and airline specialist (Offer-Order-Settle-Deliver, 100+ currencies, 168+ methods, 220+ PSPs per its site); Yuno concedes it "remains a powerful specialist" for travel and hospitality with zero-downtime deployments and failover, and positions itself for broad use cases. CellPoint is simultaneously a Yuno white-label prospect (APM connections at $15K per month, Sep to Oct 2026), so tone stays partner-grade.
- **Basis Theory and VGS (standalone vaults):** both "stop at the vault" in their own words (VGS: "does not make routing decisions for you"; Basis Theory routing guide "under construction"); Yuno gives the same PCI L1 vault with the payment stack already built on the token, token import and export, cryptogram API, and prices by approved transaction instead of stored cards. VGS is also a Yuno partner with a shared integration, and VGS is in the Autodesk RFP under NDA (never name the source).
- **Recurly and Chargebee (subscription billing engines):** no public "Yuno vs" page. Internal framing: they are billing systems that vault cards and depend on gateway tokens and professional-services migrations (Recurly: card export only in tokenized form to a PCI-compliant system, account updater at extra cost, network tokens surfaced only via Adyen); Yuno positions the recurring layer on an orchestrated, portable token with multi-PSP retries, and keeps Recurly or Stripe Billing as system of record when the merchant wants (bridge). Where the buyer needs invoicing, tax, proration, entitlements or dunning emails, Yuno should not claim parity.
- **Juspay, APEXX, Payrails, Ixopay, Solidgate, BlueSnap, Tuna:** listed on Yuno's pages; Juspay won Sabre (Nov 2025) in travel; Amadeus/Outpayce is "the best-funded native threat" in airline deals. No specific framing retrieved beyond the generic frame.

Sources
- https://y.uno/spreedly-alternatives, https://y.uno/primer-alternatives, https://y.uno/gr4vy-alternatives, https://y.uno/cellpointdigital-alternatives
- https://y.uno/post/best-payment-orchestration-platforms-in-2026 (22 Apr 2026)
- Local: Vaulting/Yuno Vault vs Basis Theory vs VGS.md (8 Oct 2026); Deals/Paramount/research/hbomax_spreedly_and_vault_market_2026-10-22.md
- Memory: project_yuno_vs_stripe_subscriptions.md, project_cellpoint_whitelabel.md, project_autodesk.md, project_chess_com.md, project_hbo_max.md, project_peacock.md, project_fareportal.md (airline competition notes)

---

## 9. Operational-efficiency thesis and ICP checklist

**Where the efficiency comes from (each line maps to a documented capability):**
1. One integration replaces N processor integrations; adding or switching a PSP, acquirer, APM or fraud tool becomes a dashboard connection, not an engineering project (connections, routing, Rappi "implementation time to zero", "90% reduction in development time").
2. Incident response moves from humans to monitors: approval-rate drops trigger alerts and automatic failover with automatic return, so PayOps stops watching dashboards and provider status pages (Rappi: milliseconds versus 5 to 10 minutes; 80% less analyst time).
3. Recovery is automated on the same token: same-provider retry, fallback to a second provider, smart retries on renewals (83 to 86% internal), account updater and network tokens before the decline happens, NOVA outreach after it.
4. Cost control is mechanical: smart routing by cost once connection costs are loaded; fee reconciliation flags charges above contract; provider neutrality means no routing conflict.
5. Finance closes faster: settlement matching per provider, account and currency, exceptions sorted by cause with an owner, settlement traceable to payout, Reports API into the ERP ("~99% reconciled on a typical day", "month-end closes faster").
6. Reporting and analysis stop being tickets: Payments Concierge answers in chat and sends scheduled briefings; Claude and ChatGPT connectors query the same data; Maia handles integration questions.
7. PCI scope and vault lock-in shrink: SAQ A through the SDK, one PCI L1 vault, portable tokens with export rights, no re-tokenization when adding a processor.
8. Vendor consolidation: one contract and one support model (KAM, TAM, tier-3) across PSPs, fraud tools, 3DS, payouts and marketplace splits.

**Who gains the most (profile):** a US company with more than one processor or acquirer (or a risky single one), several markets or currencies, a meaningful recurring or card-on-file share, a finance team reconciling multiple settlement files by hand, and a payments team that is small relative to transaction count. Companies with one processor, one market, no recurring revenue and no local-method needs do not get enough from the layer to justify a platform fee, and docs say so themselves.

**ICP checklist (score 0 to 100; apply only verified signals; gates first):**

Gates (fail any, stop):
- G1. HQ or payments decision center in the US or Canada.
- G2. Online or in-app checkout the company controls (not fully captive to app stores, Shopify Payments or a franchisor), with its own PSP or acquirer contracts or the intent to sign them.
- G3. Not a PSP, wallet, acquirer, bank or aggregator (partner, not merchant); not an existing Yuno customer or another rep's account.

Weighted criteria:
| # | Criterion | Weight | How to score |
|---|---|---|---|
| 1 | Digital transaction volume | 15 | 15 at 1M+ per month, 12 at 120K to 1M, 8 at 100K to 120K, 4 at 25K to 100K, 0 below 25K |
| 2 | Processor plurality or concentration risk | 15 | 15 with 2+ PSPs or acquirers live, 12 with an active migration or RFP, 8 with a single cross-border PSP in a market where local acquiring is cheaper, 0 with one domestic PSP and no plan |
| 3 | Multi-market footprint | 12 | 12 at 5+ countries or 3+ currencies, 8 at 2 to 4, 4 if expansion announced within 24 months, 0 single-market |
| 4 | Recurring and card-on-file share | 10 | 10 if subscriptions or stored-card renewals are the main revenue, 6 if material, 2 if occasional, 0 if none |
| 5 | Reconciliation and finance complexity | 10 | 10 with 3+ settlement sources or multiple legal entities and a visible finance-ops team, 6 with 2 sources, 2 if a single provider report, 0 if invoiced B2B |
| 6 | Orchestration status | 8 | 8 with no orchestrator and an in-house router or none, 6 with a legacy orchestrator up for renewal (Spreedly, CellPoint, APEXX), 3 with a modern competitor recently signed, 0 if a competitor signed within 12 months |
| 7 | Local payment method gaps in top markets | 8 | 8 if top-5 markets lack verified local methods (Pix, UPI, SPEI, iDEAL, wallets), 4 if partial, 0 if covered (never claim a gap without live checkout proof) |
| 8 | Trigger events in the last 12 months | 7 | 7 for an RFP, new Head of Payments or PSP migration, 5 for funding, IPO filing or expansion, 3 for a checkout redesign or public decline complaints, 0 none |
| 9 | Vertical and margin fit | 5 | 5 for M3/M4 ICP verticals (AI, software, gaming, streaming, digital goods, hosting, iGaming), 3 for M2 (retail, travel, ticketing, marketplaces, edtech), 1 for M1 (airlines, delivery, mobility), 0 outside the vertical list |
| 10 | Engineering and PCI drain | 5 | 5 if payments roles are posted or the company maintains its own PSP integrations or vault, 3 if PCI scope is visibly in-house, 0 if payments are fully outsourced |
| 11 | Operational pain evidence | 3 | 3 for documented outages, duplicate charges or refund friction, 0 none |
| 12 | Referenceability and halo | 2 | 2 if a recognizable logo with logo rights likely, 0 if NDA-only |

Thresholds: 75+ "eyes closed" (multi-PSP, multi-market, recurring and finance complexity all present); 55 to 74 strong fit, lead with the dominant pain (vault-first, recovery, reconciliation or expansion); 35 to 54 narrow fit, one product entry (subscriptions engine, reconciliation standalone, vault) and a platform-fee sanity check against V1/V2 pricing; below 35 do not pursue. Deal size (V1 to V5) and urgency are separate axes; a 75+ score with V1 volume still needs the "overall deal size cannot be under 10k" check.

Sources
- Sections 3 to 5 above (docs and product pages); https://docs.y.uno/AGENTS ("When to use Yuno")
- Grokbot/prompts/00-SHARED-CORE.md section 0.5; .claude/commands/newaccounts.md; Assets/research-skill-v8.md (rubric); memory reference_core_icp_vs_master_sheets.md (Yuno Fit 1 to 5), reference_yuno_pricing_policy.md (V1 to V5, M1 to M4, $10k floor), reference_buyer_personas.md

---

## Summary (under 400 words)

Yuno is a Rappi-spinout payment orchestrator (founded 2021 or 2022 depending on the Yuno page) that sits on top of a merchant's own PSP, acquirer, fraud and local-method contracts; it does not custody funds or sell acquiring. About $80M raised (last: $45M Series B, 12 Aug 2026), 16 offices on 5 continents, US and EMEA processing regions. Published numbers: 1,000+ methods, 460+ integrations, 190+ countries, 180+ currencies, "up to 7%" approval uplift, 30% recovered revenue, 27% cost savings, 90% less development time.

ACP means OpenAI's Agentic Commerce Protocol. Yuno sells an "Agentic Commerce" product (catalog sync, certified endpoints, payments, feed control, channel insights) that makes merchants purchasable inside ChatGPT and other assistants; the page has no live or beta label and no named merchants. The documented, live AI layer is the MCP servers, Agent Toolkit, Claude and ChatGPT connectors, Payments Concierge, Maia and NOVA. Internally an MPP stablecoin agent-payments integration was in design in Sep 2026, and agentic is a "what's new" slide, not the lead.

Orchestration is mature and API-driven: conditional routing, percentage splits, smart routing by cost or latency, retry plus fallback, monitors with automatic failover and recovery, routing recommendations in beta, Visa and Mastercard network tokens, account updater, Yuno 3DS and standalone 3DS, a portable PCI L1 vault, and no-code connections whose costs feed routing and fee reconciliation.

Reconciliation matches transactions to settlement files per provider, account and currency, with Settlements and Fees and (new engine, API only) Settlement Payouts reports; the product page claims about 99% reconciled daily. No public reconciliation customer exists.

Subscriptions run on any PSP with plans, trials, meters, Pix Automático, PayPal, wallets, smart retries up to six attempts with A/B tests, and a Stripe Billing bridge. The 16 merchants / 135K / 83 to 86% / 69K figure is an internal 31 Aug 2026 launch-deck number that needs Daniel Lozano's OK. Gaps: no bundles, proration, invoicing, tax or dunning emails.

Public US customers: GoFundMe and Whop (plus Uber and Open English). Internal US names: SpaceX, Allegiant, Kraken, Automattic, Skool, xAI, Fever. Crunchyroll, Shein and Suno are not customers.

Commercially: platform fee $5K to $25K list by volume segment plus per-transaction pay-ins ($0.10 list, $0.01 floor) and metered add-ons; "$50K free then $0.05" is outreach shorthand. The ICP is a US digital merchant with 100K+ monthly transactions, multiple processors, several markets, recurring revenue and manual reconciliation; section 9 is the gated, weighted checklist.

## Facts I could not verify
- Anything from Glean (ICP docs, NorthAm org chart, reconciliation customer list, internal ACP usage): Glean was unreachable all session.
- Whether "ACP" has any internal meaning other than the Agentic Commerce Protocol.
- GA status, live merchants and volumes of the Agentic Commerce product; the Mastercard agentic partnership (LinkedIn mention only); status of the MPP integration.
- The 16 / 135K / 83 to 86% / 69K subscription figures (internal deck only, not re-checked at source).
- Which merchants are live on the new reconciliation engine; whether Fever's "CFO Copilot" beta exists today.
- Samsung, OpenAI and Lovable as customers (only German's own outreach lines); Tada's vertical; Carrefour's region.
- Yuno headcount; post-Series B valuation; the "World's Top Fintech" and "#1 Best Payment API" awards.
- Exact current titles for Sean Calabro, Melissa Pottenger, Bernabé Murata, Martin Mexia, Rik ter Beek and the GMs.
- Amex network tokens status beyond the 5 Oct 2026 "in certification" note; identity-data vault features on the product page versus docs.
- The Claude connector scope (press says read-only analytics, docs say it can also run payment operations).
