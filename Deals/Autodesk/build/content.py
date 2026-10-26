# -*- coding: utf-8 -*-
"""Copy for the Autodesk orchestration and vault deck (26 Oct 2026).
Autodesk claims trace to data/research/autodesk-2026-10-19.md (FY26 10-K, Terms and Payments pages per country, Online Purchase
Terms); Yuno claims to Deals/OnlyFans/build/yuno_vault_facts.md (docs.y.uno) and y.uno pages re-read 26 Oct 2026.
Internal context (RFP intel, outreach) is in CONTEXT.md and never reaches a slide."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
LOGO_URL = open(os.path.join(HERE, 'LOGO_URL.txt')).read().strip() if os.path.exists(os.path.join(HERE, 'LOGO_URL.txt')) else ''

COVER = {
    'title': 'Global payments, one platform',
    'sub': 'The AI native operating system for global financial infrastructure',
    'prep': 'Prepared for Autodesk · October 2026 · Strictly confidential',
}

EXEC = {  # slide of_exec_understanding_v2, element id -> new text (styles kept)
    'of_es1_v2_003': "Yuno sits above Autodesk's processors and methods: one orchestration layer and one vault, together or on their own",
    'of_es1_v2_008': 'What Autodesk runs today',
    'of_es1_v2_009': 'Most of its revenue **billed directly**, through its own stores in the US, Europe, the UK, Brazil, Mexico, India, Japan and Australia, each with its own processors, local methods and renewals to collect.',
    'of_es1_v2_011': 'Where the complexity sits',
    'of_es1_v2_012': 'Every store adds a processor, a method and a contract. **Cards live with the processor that stored them**, a declined renewal retries inside one provider, and each new market or product line is a new integration.',
    'of_es1_v2_014': 'Where Yuno fits',
    'of_es1_v2_015': 'An **orchestration layer** that routes, retries and recovers every renewal across the processors and local methods behind each store, and a **PCI DSS Level 1 vault** that holds the cards above all of them. Two products on one platform; tokens stay portable and the exit is written into the contract.',
    'of_es1_v2_026': 'What we bring\nOrchestration runs on the processors and methods Autodesk uses today, and the vault holds the cards above them. One integration for every store, method and provider.',
}

SUBS = {  # new slide: the subscription engine (content as used in the HBO Max deck, Oct 2026, adapted to Autodesk)
    'kicker': 'SUBSCRIPTIONS  ›  THE ENGINE',
    'title': 'One subscription engine. Every payment method, every provider',
    'intro': "Plans, trials, add-ons, usage metering and Smart Retries, built on Yuno's orchestration, so the same subscription bills through any provider you route to.",
    'stats': [('300K+', 'active subscriptions billed by Yuno'), ('$15M/mo', 'recurring volume processed'),
              ('1.2M+', 'subscriptions created to date'), ('30+', 'merchants on recurring')],
    'flow_h': 'HOW IT WORKS  ·  ONE SUBSCRIPTION OBJECT, EVERY PROVIDER',
    'steps': [  # number, title, description, built on
        ('01', 'Define the plan', 'Phases (trial, intro, regular), a price per country and usage meters, set once from the back office or the API.', 'Back office · API'),
        ('02', 'Subscribe once', 'The customer checks out; the card, wallet or bank mandate is stored in the vault as one credential.', 'Checkout · Vault'),
        ('03', 'Bill every cycle', 'On each renewal date the engine creates the charge and routes it, through orchestration, to the best provider.', 'Smart routing'),
        ('04', 'Recover declines', 'Smart Retries pick when and through which provider to retry; account updater and network tokens keep the credential current.', 'Smart Retries · Updater'),
        ('05', 'Notify and measure', "Webhooks on every transition feed Autodesk's entitlement and finance systems; analytics per plan, country and provider.", 'Webhooks · Analytics'),
    ],
    'band': '**Built on the orchestration layer.** A renewal is routed like a first purchase: routing rules, provider fallback, vaulted credentials and the local rails behind each store, in one subscription object.',
    'box1_h': 'WHY THIS MATTERS FOR AUTODESK',
    'box1': 'Autodesk renews most of its $6.7B of subscription revenue directly, through stores with different processors and local methods. The engine sits above all of them, so a renewal can retry on a different provider instead of failing.',
    'box2_h': 'ALREADY LIVE ON THE SAME ENGINE',
    'box2': 'Subscription billing is in production across software, streaming, marketplace, mobility and creator platforms, on the same orchestration layer shown here. No pilot code path and no separate product.',
    'src': 'Yuno Subscriptions, production figures as of October 2026; flow as documented on y.uno/product/subscriptions and docs.y.uno, read 26 Oct 2026.',
}

DEPTH = {  # new slide: billing-platform depth (content as used in the HBO Max deck, Oct 2026, adapted to Autodesk)
    'kicker': 'SUBSCRIPTIONS  ›  BILLING DEPTH',
    'title': 'Full billing-platform depth, above the routing decision',
    'intro': 'Define plans once. Yuno bills every cycle, meters usage, recovers failed renewals and notifies your systems in real time.',
    'diff_h': 'THE DIFFERENCE',
    'diff': 'Billing platforms lock you to one processor. Yuno sits **above the routing decision**, so you switch providers, add local rails and keep every subscriber.',
    'cards': [
        ('Plans and local pricing', 'One plan definition with an explicit price per country, so there is no FX drift and no surprise on the statement.', 'Per-country prices, one plan'),
        ('Trials and intro offers', 'Free or paid trials in calendar days, multi-phase pricing in one subscription, pre-renewal events before every step-up.', 'Trial, intro price, full price'),
        ('Add-ons and promotions', 'Upsell extras and run promotions, billed together in one charge with a clean line-item breakdown.', 'Bundle and promo, one charge'),
        ('Upgrades and downgrades', 'Change a plan and Yuno applies it on the next billing date. Pause, cancel or reactivate without refund tickets.', 'Effective next renewal'),
        ('Smart Retries', 'Picks the best moment and provider to retry a failed renewal, by decline code, country and provider. Recovers revenue that is written off today.', 'Multi-provider recovery'),
        ('Usage-based billing', 'Meter anything: tokens, seats, cloud credits, add-on minutes. Send usage events and Yuno rates them into the renewal charge.', 'Per unit, package or tier'),
        ('Cards, wallets and local rails', 'Recurring on cards, Apple Pay, Google Pay, PayPal and the local rails behind your stores, such as SEPA mandates and Pix Automático.', 'The rails your stores already list'),
        ('Subscription analytics', 'Renewal approval, churn, trial conversion and recovered revenue, broken out per plan, per country and per provider.', 'Approval, churn, recovery'),
    ],
    'enabled': [('Back office', 'No-code setup and day-to-day operations'), ('API', 'Full programmatic control'), ('Webhooks', 'Real-time notifications on every event')],
}

TODAY = {  # slide vlt_problem, body redrawn
    'kicker': 'AUTODESK TODAY  ›  HOW THINGS STAND',
    'title': 'Autodesk now bills most of its revenue directly, through its own stores and local methods in every region',
    'left_h': 'THE BUSINESS',
    'tiles': [  # value, label, sub
        ('$7.2B', 'REVENUE, FY26', 'up 18%, with 64% earned outside the US'),
        ('63%', 'BILLED DIRECTLY', 'indirect revenue fell from 58% to 37% in one year'),
        ('$6.7B', 'SUBSCRIPTION REVENUE', 'of $7.2B, renewed and collected by Autodesk'),
        ('$2.6B', 'US REVENUE', 'EMEA $2.8B · APAC $1.2B · Other Americas $0.6B'),
    ],
    'bullets': [
        'Autodesk entities are seller of record in every region checked',
        'Monthly plans only direct; annual billing saves 33%',
        "Processing fees now sit in Autodesk's own operating costs",
    ],
    'left_src': 'Autodesk FY26 Form 10-K (revenue, indirect share, processing fees); Online Purchase Terms, Dec 2025 (seller of record); Terms and Payments pages (monthly plans direct only). Read 19 Oct 2026.',
    'right_h': 'THE STORES AND THEIR METHODS, AS PUBLISHED',
    'col1': 'MARKET', 'col2': 'METHODS LISTED ON THE TERMS AND PAYMENTS PAGE OF EACH STORE',
    'rows': [
        ('United States', 'Cards · Apple Pay · Google Pay · PayPal · Pay by Bank · ACH'),
        ('EU', 'Cards · SEPA · iDEAL · PayPal'),
        ('United Kingdom', 'Cards · BACS Direct Debit · PayPal · Apple Pay · Google Pay'),
        ('Germany', 'Cards · SEPA Direct Debit · PayPal · Apple Pay · Google Pay'),
        ('Brazil', 'Cards · Boleto · Pix · PayPal, priced in BRL'),
        ('Mexico', 'Cards · PayPal, priced in MXN'),
        ('India', 'Cards · net banking · UPI and wallets through CCAvenue'),
        ('Japan', 'Cards · konbini · Pay-easy · PayPal · Apple Pay · Google Pay'),
        ('Australia', 'Cards · Zip · PayPal · Apple Pay · Google Pay'),
    ],
    'right_note': "Card brands as listed per store (Germany's page lists cards without naming brands). The Plaid, Nacha, Direct Debit, Nexi and convenience-store marks stand for Pay by Bank, ACH, Bacs, CartaSi and konbini. Card acquirer and current card vault are not named on Autodesk's public pages; this deck assumes nothing about them.",
}

M5 = {  # slide m5_mock
    'm5_kk': 'WHY YUNO  ›  VAULT AND ORCHESTRATION, ONE PLATFORM',
    'm5_tt': "Yuno's vault does everything a standalone vault does, and the orchestration layer is already built around it",
    'm5_hl': 'What Autodesk needs',
    'm5_bd0': 'Cards, network tokens and the bank details behind SEPA, BACS and ACH, in one vault',
    'm5_ad1': 'Each processor and local method connection, built and run in-house',
    'm5_bd1': '460+ processor integrations already built and maintained, plus local methods per market',
    'm5_ad2': 'Routing, retries and failover across processors, built in-house',
    'm5_bd2': 'Routing, Smart Retries and failover on rules you set, on every renewal',
    'm5_bd3': '3DS, account updater, network tokens and subscriptions on the same tokens',
    'm5_band': 'Same independence, far less to build.   Autodesk keeps portable tokens and exit terms, and decides how much of the stack Yuno runs.',
}

ORCH = {  # new slide, drawn
    'kicker': 'ORCHESTRATION  ›  ONE INTEGRATION',
    'title': "One integration between Autodesk's stores and every processor and method, in every region you sell",
    'left_h': 'Autodesk', 'mid_h': 'Yuno', 'right_h': "Autodesk's methods today",
    'left': [
        ('Direct store checkout', 'checkout.autodesk.com, local currency per country'),
        ('Subscription renewals', 'monthly and annual plans, billed by Autodesk'),
        ('Regional sellers of record', 'Autodesk Inc, Ireland Operations, India, Japan, Australia'),
        ('New lines and entities', 'the same layer for every seller of record'),
    ],
    'mid_sub': 'One API, one dashboard, every provider',
    'mods': ['Checkout and SDKs', 'Smart routing and retries', 'Vault and network tokens', '3DS and risk conditions',
             'Subscriptions', 'Account updater', 'Reconciliation and insights', 'Payments Concierge (AI)'],
    'right': [
        ('Card acquirers', 'any region, any provider'),
        ('PayPal, Apple Pay, Google Pay', 'every store; wallets in US, UK, DE, JP, AU'),
        ('SEPA, iDEAL, BACS', 'EU, Germany, UK'),
        ('Pix, Boleto', 'Brazil'),
        ('UPI, net banking, konbini, Pay-easy', 'India, Japan'),
        ('Pay by Bank, ACH, Zip', 'US, Australia'),
    ],
    'band': "**Yuno never holds the money.** Funds settle from your providers straight to Autodesk's entities; Yuno connects, decides, secures and reconciles.",
    'src': "Autodesk's methods as listed on its Terms and Payments pages per country, read 19 Oct 2026. Yuno: 1,000+ payment methods, PSPs and fraud tools, as published on y.uno.",
}

RENEW = {  # new slide, drawn
    'kicker': 'ORCHESTRATION  ›  RENEWALS',
    'title': 'Every renewal takes its best route, and a decline takes a second one on the same token',
    'pay': ('RENEWAL', '$260.00 · card on file', 'Monthly plan · merchant initiated'),
    'engine': ('Routing engine', 'Rules you set, or AI', 'Issuer country, BIN, amount, transaction type, cost, provider health'),
    'providers': [('Processor A', 'DECLINED'), ('Processor B', 'APPROVED'), ('Processor C', 'STANDBY')],
    'steps': [('1', 'The first route declines, or the provider is down'),
              ('2', 'Smart Retries re-send on the schedule and route most likely to approve'),
              ('3', 'The customer keeps access and re-enters nothing')],
    'right_h': 'WHAT IT DELIVERS',
    'stats': [('Up to 7%', 'approval uplift'), ('30%', 'recovered revenue')],
    'checks': ['Network tokens and account updater keep the stored card current',
               'The network transaction ID travels with the token to any processor',
               'Hard declines stop; a retry cap protects scheme standing',
               'Monitors move traffic when a provider drops'],
    'src': 'Illustrative flow. Uplift and recovery are Yuno published figures (y.uno, read 26 Oct 2026); results vary by merchant. Smart Retries, stored credentials and Monitors as documented on docs.y.uno.',
}

CARDS = {  # slide vlt_cards
    'vlt_cards__9_244': 'Cards are stored once and work on every processor you connect',
    'vlt_cards_k038': 'Current processor exports',
    'vlt_cards_k047': 'customers untouched',
    'vlt_cards_k050': 'Import from your current processor as a PGP-encrypted file over SFTP, network tokens included. Export is documented.',
    'vlt_cards_k052': '**One vaulted token, every processor.** Add or swap a processor in any region and the stored cards keep working, with nothing collected again from customers.',
}

PORT = {  # slide h7c266de662ba1cf0_9_469
    'h7c266de662ba1cf0_9_507': "Registered under Autodesk's token requestor ID\nwhere the scheme allows it, so they survive a\nchange of processor or of vault. No\nre-tokenization on exit.",
    'h7c266de662ba1cf0_9_511': 'A written request from Autodesk',
}

BEYOND = {  # new slide, drawn
    'kicker': 'BEYOND ORCHESTRATION AND VAULT  ›  ON THE SAME PLATFORM',
    'title': 'Once the routing and the tokens are in one place, the rest switches on as configuration',
    'cards': [
        ('Agentic commerce', 'When AI agents buy on behalf of your customers, you set the spend limits and approvals. The platform enforces and records each one, on the same tokens and routing.', 'Agents buying seats, tokens and add-ons'),
        ('3DS and SCA', 'Yuno 3DS with Netcetera as the default provider, plus standalone authentication that returns ECI and CAVV for any acquirer, so EU and UK checkouts meet SCA on the same tokens.', 'EEA and UK stores'),
        ('Reconciliation', 'Settlement files from each provider matched to your transactions, and approval, cost and fees by provider and market in one view.', 'Finance and treasury'),
        ('Payments Concierge', 'An AI agent for the payments team. It watches approvals and providers, explains what changed in plain language and helps route, retry and recover.', 'Payments operations'),
    ],
    'also_pill': 'ALSO',
    'also': '**Stablecoins and banking connectivity** run on the same connection, when Autodesk needs them.',
    'src': 'Products as published on y.uno and docs.y.uno, read 26 Oct 2026.',
}

CLOSE = {  # new slide, drawn
    'kicker': 'NEXT STEPS',
    'title': 'Where we start',
    'steps': [
        ('01  ·  MAP', 'Your stack today', 'Processors, methods and entities per store, and where approvals, renewals or costs slip today.'),
        ('02  ·  TEST', 'A sandbox, open now', 'Hosted fields, vault, proxy and routing in a sandbox your team can try at its own pace.'),
        ('03  ·  PROVE', 'One flow, clear metrics', 'Start with routing on one store, or with the vault on your current processors. Nothing migrates until the numbers say so.'),
    ],
    'security': 'Available on request: PCI DSS Level 1 attestation, SOC 2 Type 2 report, ISO 27001 and ISO 27701 certificates, Visa Service Provider listing.',
    'band': "**Let's grow together**",
    'contact': 'German Tatis  ·  Senior Account Executive  ·  San Francisco\ngerman.tatis@y.uno  ·  +1 786 238 4554  ·  y.uno',
}

NOTES = {
    'exec': (
        "Labels: CONFIRMED = docs.y.uno or y.uno; BETA = depends on the PCI Proxy (beta, enabled per organization); PUBLIC = Autodesk's own pages or 10-K; OPEN = not confirmed in writing, owner named.\n"
        "What Autodesk is buying: the scope of the evaluation as we understand it from the market. Say 'from what we understand' and let them correct it.\n"
        "Direct billing, PUBLIC: FY26 10-K, indirect revenue 58% to 37% in a year under the new transaction model (partners quote, Autodesk transacts and bills); 'payment processing fees' listed in operating expenses. Stores: the Terms and Payments pages per country (US, EU, UK, DE, BR, MX, IN, JP, AU), read 19 Oct 2026 from snapshots.\n"
        "Two vendors line: a standalone vault vendor's public pages describe storage, proxy and tokens, and leave routing and provider connections to the merchant; an orchestrator that relies on each processor's vault leaves the cards there. Yuno's vault page: 'Yuno Vault runs standalone', 'Portable to any provider', '460+ Processor integrations'.\n"
        "Exit in the contract: the documented export process (written request, recipient's PCI DSS AOC, PGP file over SFTP) plus commercial terms in the MSA (OPEN, Legal). The y.uno vault page promises export at no charge to a defined timeline; the docs state no fee or timeline, so the MSA is where it gets written down."),
    'today': (
        "All PUBLIC. Revenue $7.206B FY26 (year ended 31 Jan 2026), +18%, 64% international; subscription revenue $6.74B; by region US $2,566M, EMEA $2,794M (+21%), APAC $1,234M (+11%), Other Americas $612M (+25%, fastest growing). Indirect revenue 58% to 37%, so about 63% is billed directly. 'Payment processing fees' sit in operating expenses. Source: FY26 Form 10-K.\n"
        "Seller of record: Autodesk, Inc. (US and Canada terms, Dec 2025), Autodesk Ireland Operations Unlimited Co. (EEA, Switzerland, UK), Autodesk India Online Store Pvt. Ltd., Autodesk Ltd. Japan, Autodesk Australia Pty Ltd. Brazil and Mexico stores price in BRL and MXN; their seller-of-record pages were not fetched.\n"
        "Methods: Terms and Payments pages per country, Wayback snapshots Mar to Oct 2026, plus the India help page for CCAvenue (annual and 3-year plans; monthly plans are credit card only there). Monthly billing 'only available directly from Autodesk'; annual 'Save 33% over the monthly price'.\n"
        "Not on the slide, on purpose: no card processor is named on any public page; older statement descriptors point to a past merchant-of-record provider and a possible processor in Australia, both inferences. Do not state them. If asked who processes today, say we do not know and the RFP will tell us.\n"
        "Logos (26 Oct, v2): every listed method as a mark, smaller. Card brands per store among Visa, Mastercard, Amex, Discover, JCB and Diners Club. Germany's page says 'cards' without brands: Visa, Mastercard and Amex are shown there as the usual set (assumption, say so if asked). Representative marks: Plaid for Pay by Bank (Autodesk's Pay by Bank runs on Plaid), Nacha for ACH, the UK Direct Debit mark for Bacs, Nexi for CartaSi (rebranded 2017), 7-Eleven, Lawson and FamilyMart for konbini, Pay-easy's own mark, a bank front for India net banking and Japan's invoice bank transfer, a barcode for Boleto, Paytm and CCAvenue for India wallets (help page). India's monthly plans take Visa and Mastercard credit only. The SEPA mark on the Germany row is SEPA-Lastschrift (direct debit); Brazil and Mexico price in BRL and MXN (grey notes removed 26 Oct evening so every row is marks only). Logos from Wikimedia Commons and the schemes' own sites.\n"
        "German decides whether this slide stays. If it goes, the deck is 11 slides."),
    'm5': (
        "Standalone vault column = what standalone vault vendors' public pages offer (storage, tokenization, proxy, portable tokens). Yuno column: PCI DSS Level 1, SOC 2 Type 2, ISO 27001, ISO 27701, Visa Service Provider and '460+ Processor integrations' (y.uno/product/vault, read 26 Oct 2026); routing, Monitors, Smart Retries (docs.y.uno automation page); account updater Visa and Mastercard (docs); network tokens Visa, Mastercard, Amex per docs, scheme activation confirmed in writing before any pilot (OPEN, Trust & Vault).\n"
        "Bank details: ACH and SEPA enrollments can be stored vault-only (enroll API, docs). BACS direct debit mandates are collected by a UK provider; whether the mandate reference is vaulted is a design choice (OPEN, Solutions).\n"
        "Subscriptions: y.uno/product/subscriptions (plans, trials, Smart Retries, retry through a different PSP, Stripe Billing compatibility), read 26 Oct 2026."),
    'orch': (
        "Left column is Autodesk's public footprint: hosted checkout on checkout.autodesk.com with local currency (BRL, MXN, INR, JPY, AUD, GBP, EUR); monthly and annual plans billed directly; sellers of record per region (see slide 3 notes). 'New lines and entities' is deliberately generic: Autodesk has closed acquisitions recently (MaintainX, Aug 2026; Payapps, 2024), but nothing public says how they bill, so do not claim it.\n"
        "Right column is what Autodesk already offers, per its own pages; it is not a claim that each method is live on Yuno today. Yuno publishes 1,000+ payment methods, PSPs and fraud tools and 190+ countries (y.uno). If asked about a specific method (Pay-easy, konbini, Zip, CCAvenue), check the integrations directory before answering.\n"
        "Yuno never holds the money: funds settle from each provider to the merchant's own accounts (docs, how Yuno works). Reconciliation: settlement files matched to transactions (docs automation page)."),
    'renew': (
        "Illustrative renewal: $260 is AutoCAD's US monthly list price (Autodesk product page snapshot, Oct 2026). Values and processors are fictional.\n"
        "Routing: conditions on amount, country, issuer country, card type, brand, BIN, currency, installments and transaction type (CIT, MIT, RECURRING); per-step outputs for declines, decline groups, timeouts and errors with a next step; percentage splits; Smart Routing optimizes conversion and cost or latency (docs.y.uno routing pages). CONFIRMED.\n"
        "Stored credentials: 'The network_transaction_id belongs to the card network, not to the provider that processed the first payment. Yuno stores it on the vaulted_token and sends it on every merchant-initiated payment, whichever provider your routing selects.' (docs.y.uno stored credentials). CONFIRMED.\n"
        "Smart Retries: timing from approval and decline data across issuers, methods and countries; hard declines stop; retry cap; a retry can go through a different PSP; A/B against your own schedule (y.uno/product/subscriptions, read 26 Oct 2026). Subscriptions Smart Retries 'up to six attempts' (docs automation page). Monitors: provider health events, traffic moved on drops (docs). Account updater: Visa and Mastercard, asynchronous, same vaulted token (docs). Network tokens: Visa, Mastercard, Amex per docs; activation per scheme in writing before a pilot.\n"
        "Figures: 'up to a 7% uplift in approval rates' and '30%' recovered revenue are on y.uno (read 26 Oct 2026). Never quote any other uplift number."),
    'subs': (
        "Figures: 300K+ active subscriptions and $15M a month of recurring volume come from the Subscriptions product team (Daniel Lozano, 1 Sep 2026); 1.2M+ subscriptions created and 30+ merchants on recurring are the figures already used in the HBO Max deck (Oct 2026). Internal production figures, not on y.uno: confirm with Daniel before quoting them in writing.\n"
        "Flow (26 Oct evening, German: no logos, illustrate the process): define the plan (phases, price per country, meters: y.uno/product/subscriptions) > subscribe once (credential in the vault: docs vault pages) > bill every cycle (renewal routed like a first purchase, routing rules and PSP fallback: y.uno subscriptions page) > recover declines (Smart Retries with hard-decline stop and retry cap, retry through a different PSP; account updater and network tokens on the same vaulted token: docs) > notify and measure (webhooks on every transition, subscription analytics: y.uno). Mandates for SEPA and ACH are stored in the vault per docs; Pix Automático per the subscriptions page.\n"
        "Autodesk: subscription revenue $6.74B of $7.21B in FY26 (Form 10-K); monthly plans sold only directly; annual plans renewed directly under the new transaction model. PUBLIC.\n"
        "Engine on the orchestration: each renewal is routed like a first purchase, with routing rules, PSP fallback, vaulted credentials and local rails (y.uno/product/subscriptions, read 26 Oct 2026)."),
    'depth': (
        "Source: y.uno/product/subscriptions (read 26 Oct 2026): phases (trial, intro, regular) with their own length and frequency, prices per country, Smart Retries with hard-decline stop and retry cap, retry through a different PSP, A/B tests against your own schedule, meters for usage-based billing (included credits, per-unit, package, tiered), cards, Apple Pay, Google Pay, PayPal and Pix Automático in one subscription object, webhooks on every transition, Stripe Billing compatibility. docs.y.uno: SEPA and ACH enrollments stored in the vault.\n"
        "Add-ons and promotions, upgrades and downgrades: wording as used in the HBO Max deck (Oct 2026); plan changes apply on the next billing date with no proration. Not offered: invoicing, tax, credit notes, end-customer dunning emails, revenue recognition. If Autodesk needs a full billing engine behind its enterprise invoices, say so; the engine covers the direct-store subscriptions.\n"
        "Usage-based billing example for Autodesk: Flex tokens (pay-as-you-go) are listed on Autodesk's own pages; metering them through Yuno is a possibility, not a claim about how Autodesk bills Flex today."),
    'cards': (
        "Store: SDKs for Web, iOS, Android, Flutter, React Native; Secure Fields; most SDK merchants qualify for SAQ A, the QSA confirms (docs.y.uno PCI compliance page). CONFIRMED.\n"
        "Keep: Card Account Updater, Visa and Mastercard, asynchronous; vaulted_token and fingerprint stay the same; registration up to 100 tokens per request; scheme registration up to 10 working days (docs). Amex and Discover updater: not in docs, concede if asked.\n"
        "Move: token migration process (PGP keys, SFTP, token_source MIGRATION_FILE, viability assessment first) and a separate network token migration process (docs data migration pages). CONFIRMED. Tokens provisioned under a processor's token requestor ID are re-provisioned rather than imported (OPEN, Trust & Vault, viability assessment).\n"
        "Export: written request, recipient's PCI DSS AOC, PGP file over SFTP; documented CSV has holder name, number, token, expiry; network tokens and NTIDs are not in the documented file (OPEN, Trust & Vault product and Legal, to be scoped in the MSA)."),
    'port': (
        "Portability: vaulted tokens work across all processors connected to the account, no re-tokenization (docs.y.uno tokens). Export process as documented (exporting tokens page). CONFIRMED. Fee, timeline and NTID export are not in docs: OPEN with Legal and Trust & Vault product, to be written into the MSA.\n"
        "Token requestor ID: the API reference says Yuno holds the TRID; the vault page says tokens are registered in your name. Say 'dedicated TRID for Autodesk where the scheme allows it' and confirm the model with Trust & Vault product before the RFP answer (OPEN). Never say 'in your name'.\n"
        "Processor logos are examples of Yuno connections, not a statement about Autodesk's current providers."),
    'beyond': (
        "Subscriptions: y.uno/product/subscriptions, read 26 Oct 2026: phases (trial, intro, regular) with their own length and frequency, prices per country, Smart Retries with hard-decline stop and retry cap, retry through a different PSP, A/B tests, meters for usage-based billing, cards, Apple Pay, Google Pay, PayPal and Pix Automático in one subscription object, Stripe Billing kept as the billing engine or a Stripe-compatible endpoint. Not offered: invoicing, tax, credit notes, end-customer dunning emails, revenue recognition; if Autodesk asks for a full billing engine, say so.\n"
        "3DS: own connection 'Yuno 3DS', Netcetera default; 3DS Standalone returns ECI and CAVV with no provider involved (docs). SCA applies to customer-initiated payments; merchant-initiated renewals are out of SCA scope once the mandate is set up with authentication.\n"
        "Reconciliation: 'Reconciliations against provider settlement files' on the docs automation page; Insights on y.uno. Scope per provider is confirmed during the evaluation.\n"
        "Payments Concierge, agentic commerce, stablecoins, banking connectivity: product names on y.uno (read 26 Oct 2026); banking connectivity per docs (accounts, balances, transfers)."),
    'close': (
        "Include: Yuno can be scored in the vault lot, the orchestration lot, or both; the products are separate and priced separately.\n"
        "Sandbox: 'The sandbox is open for testing' for the PCI Proxy (docs); SDK, vault and routing sandboxes are standard. The cryptogram API and account updater are switched on per organization.\n"
        "Security pack: PCI DSS Level 1, SOC 2 Type 2, ISO 27001, ISO 27701, Visa Service Provider (y.uno vault and trust pages); reports and the AOC come through Security, not links.\n"
        "German is based in San Francisco; Autodesk HQ is One Market. Offer the walkthrough in person."),
}
