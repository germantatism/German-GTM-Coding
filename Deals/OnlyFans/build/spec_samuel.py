# -*- coding: utf-8 -*-
"""Samuel Vieira's 25 slides (handoff 7 Oct 2026) mapped to the deck_spec schema.
Wording, labels, quotes, numbers, the 4 / 1 / 4 tally and the six open items are carried over verbatim.
Cross-references use {{slide:<id>}} tokens that make_spec.py resolves to the final slide numbers.
Kickers are rewritten to the deck's section names; headlines and bodies are Samuel's."""

K_VAULT = "THE YUNO TOKEN VAULT"
K_VS = "VERSUS A STANDALONE VAULT"
K_PATH = "THE PATH FORWARD"
SRC_DATE = "Read 7 October 2026."

SLIDES = {}

# ---------------------------------------------------------------- cover (S1)
SLIDES["cover"] = {
    "id": "cover", "type": "cover",
    "title": "The vault under creator banking",
    "subtitle": "Your credentials, your connections, your rules.",
    "presenter": "German Tatis · Business Development · October 2026 · Strictly confidential",
    "logo_url": "https://deck.yuno.tools/merchants/onlyfans.png",
    "notes": "You have an RFP open for a token vault, and you told us where the product is going: one creator account on top, several banks, issuers and transfer providers underneath. This deck answers the vault question and the question you asked us most, which is who decides where each creator lands. Every claim in it is labeled with its basis, so your payments team can check it without us in the room.",
}

# ---------------------------------------------------------------- S2 understood
SLIDES["understood"] = {
    "id": "understood", "type": "diagram",
    "kicker": "WHY WE ARE HERE · WHAT WE UNDERSTOOD",
    "headline": "One creator account on top. Several banks, issuers and transfer providers underneath, so no single partner can cut a creator off.",
    "source": "Your design as we understood it. Blue marks where Yuno would sit. Section 06 shows what exists today and what is open.",
    "boxes": [
        {"id": "creator", "x": 0, "y": 0, "w": 420, "h": 40, "title": "Creator", "body": "opens one OnlyFans account", "style": "outline"},
        {"id": "decision", "x": 0, "y": 58, "w": 420, "h": 48, "title": "Yuno · decision layer", "body": "Which bank, issuer and rail each creator lands on", "pill": "Rules set by OnlyFans", "style": "blue"},
        {"id": "vault", "x": 0, "y": 124, "w": 420, "h": 44, "title": "Yuno · vault", "body": "Cards, account numbers and credentials, tokenized once · Section 06", "style": "blue"},
        {"id": "banks", "x": 0, "y": 192, "w": 98, "h": 60, "title": "Banks", "body": "Two to five per creator", "style": "light"},
        {"id": "issuers", "x": 107, "y": 192, "w": 98, "h": 60, "title": "Card issuers", "body": "Pluggable: add or swap", "style": "light"},
        {"id": "transfer", "x": 214, "y": 192, "w": 98, "h": 60, "title": "Bank transfer providers", "body": "Several, for redundancy", "style": "light"},
        {"id": "stable", "x": 321, "y": 192, "w": 99, "h": 60, "title": "Stablecoin conversion", "body": "So balances can earn yield", "style": "light"},
    ],
    "connectors": [
        {"from": "creator", "to": "decision"}, {"from": "decision", "to": "vault"},
        {"from": "vault", "to": "banks"}, {"from": "vault", "to": "issuers"}, {"from": "vault", "to": "transfer"}, {"from": "vault", "to": "stable"},
    ],
    "side": {"header": "WHAT YOU ASKED", "items": [
        {"title": "Who decides", "body": "You do. Your policy picks the provider and Yuno executes it. Section 06."},
        {"title": "US first", "body": "Phase 1 covers US balances only, as you scoped it."},
        {"title": "Banking next", "body": "Every sensitive record needs a home in the vault, not only cards."},
    ]},
    "notes": "This is your design as we understood it from our conversation. Correct anything we have wrong before we go further. The two blue bands are where Yuno would sit: the vault at the base, and the layer that decides which bank, issuer and rail each creator lands on. You asked several times who makes that decision. The short answer is that OnlyFans does, and Section 06 shows exactly how.",
}

# ---------------------------------------------------------------- S3 how to read
SLIDES["howtoread"] = {
    "id": "howtoread", "type": "cards_row",
    "kicker": "WHY WE ARE HERE · HOW TO READ THIS DECK",
    "headline": "Every capability claim carries one of three labels, so your team can check it without us in the room.",
    "cards": [
        {"pill": "CONFIRMED", "title": "Written in Yuno's public documentation", "body": "Read at docs.y.uno on 7 October 2026; company figures come from y.uno. Most of it can be tested in the sandbox. A Beta tag marks anything in beta."},
        {"pill": "PUBLIC DOCS", "title": "Read on another vendor's public pages", "body": "VGS and Basis Theory, read on 7 October 2026. Treat every one of these lines as a question to confirm with them."},
        {"pill": "OPEN", "title": "Not yet confirmed in writing inside Yuno", "body": "Shown with an owner, never as a fact. The six open items are listed together on slide {{slide:owe}}. Direction marks product direction, not a delivery commitment. In the appendix, Not in docs marks a gap in our public reference."},
    ],
    "bar": "**Why it matters.** A vault sits under everything you build on it. We would rather show you an open item today than have your engineers find it in the sandbox.",
    "notes": "We label every claim. Confirmed means it is in our public documentation, and most of it can be tried in the sandbox: the proxy sandbox is open today, while the cryptogram API and the account updater are switched on for your organization. Public docs means we read it on a competitor's own pages and you should confirm it with them. Open means we have not confirmed it in writing internally, so we will not present it as a fact. A vault is the wrong place for surprises.",
}

# ---------------------------------------------------------------- S4 answer up front
SLIDES["answer"] = {
    "id": "answer", "type": "stats",
    "kicker": "WHY WE ARE HERE · THE ANSWER UP FRONT",
    "headline": "A vault stores the credential. Your design also needs a layer that decides where it goes. Yuno does both.",
    "source": "Nine things your design needs: item by item on slide {{slide:versus-table}}, vendor by vendor on slides {{slide:versus-bt}} and {{slide:versus-vgs}}. Competitor lines from public pages, read 7 October 2026.",
    "tiles": [
        {"label": "WHERE YUNO LEADS", "value": "4 of 9", "caption": "Routing rules for card payments, processor integrations already built, a banking API across providers, and payouts."},
        {"label": "LEVEL", "value": "1 of 9", "caption": "A card vault at PCI DSS Level 1 with hosted capture. All three of us have one."},
        {"label": "WHERE VGS AND BASIS THEORY LEAD", "value": "4 of 9", "caption": "Network token depth, token types for personal data, issued-card display (PIN setting at Basis Theory), and a more established proxy with custom code."},
    ],
    "bar": "**In one line.** If the RFP is for storage alone, a standalone vault is a fair choice. If the vault has to serve a multi-bank, multi-issuer product, the harder half is the layer above it.",
    "notes": "Here is the conclusion before the detail. We compared Yuno with VGS and Basis Theory on nine things your design needs. On four of them a standalone vault leads today, and we say so. On one we are level. On four Yuno leads, and those four are the ones your architecture adds on top of a vault: routing rules for card payments, processor integrations that are already built, a banking API across providers, and payouts. Where any of these is only partly there today, the deck says so.",
}

# ---------------------------------------------------------------- S6 vault cards
SLIDES["vault-cards"] = {
    "id": "vault-cards", "type": "cards_row",
    "kicker": K_VAULT + " · CARDS",
    "headline": "One vaulted token works on every processor you connect, so no processor owns your cards.",
    "source": "Source: docs.y.uno, read 7 October 2026. Page list on slide {{slide:app-sources}}.",
    "cards": [
        {"pill": "CONFIRMED", "eyebrow": "STORE", "title": "Collect a card without charging it", "body": "SDK enrollment on Web, iOS and Android creates a vaulted token without a charge. Card numbers never reach your pages, which is why most SDK merchants qualify for SAQ A. Zero-amount verification is optional where the provider supports it."},
        {"pill": "CONFIRMED", "eyebrow": "KEEP", "title": "Network tokens and account updater", "body": "Once activated, network tokens are provisioned for enrolled cards with Visa, Mastercard and American Express. The account updater refreshes reissued Visa and Mastercard cards while the vaulted token stays the same."},
        {"pill": "CONFIRMED", "eyebrow": "MOVE", "title": "Import in, export out", "body": "Cards arrive from your current gateway or vault as PGP-encrypted files over SFTP. Card export is documented too: on written request, to a recipient with a valid PCI DSS attestation."},
    ],
    "side": {"header": "WHAT YOU GET", "items": [
        {"title": "No re-tokenization", "body": "Add or swap a processor and the stored cards keep working."},
        {"title": "Fewer declines", "body": "Reissued and renewed cards update without the cardholder."},
        {"title": "A public exit", "body": "You can read the export process before you sign anything."},
    ]},
    "notes": "The same logic you apply to banks applies to card processors: no single one should be able to cut you off. A card is collected once in our hosted fields and stored as a vaulted token that works on every processor connected to your account. Network tokens and the account updater keep it current. And the way out is documented publicly: an encrypted export to a recipient with a valid PCI DSS attestation. Your QSA confirms your own SAQ level; we describe how capture works. Scheme activation for network tokens is confirmed per network in writing before Phase 1. Network token import is also a documented process, with the network transaction ID and the wallet parent type in the file.",
}

# ---------------------------------------------------------------- S7 vault data
SLIDES["vault-data"] = {
    "id": "vault-data", "type": "diagram",
    "kicker": K_VAULT + " · BEYOND CARDS",
    "headline": "Creator banking adds account numbers, tax IDs and identity documents. Here is where each one lives in Yuno today.",
    "boxes": [
        {"id": "cards", "x": 0, "y": 0, "w": 100, "h": 180, "title": "cards · PCI", "body": "number · •••• 3456\nexpiration · ••/27\nholder_name · string\nnetwork_token · DPAN\nnetwork_transaction_id\nThe CVV is never stored.", "pill": "CONFIRMED", "style": "dark"},
        {"id": "bank", "x": 107, "y": 0, "w": 100, "h": 180, "title": "bank accounts", "body": "ACH_ENROLLMENT\nrouting_number · string\nbeneficiary_name · string\naccount_type · enum\nvault_only · true\nIn the enroll API reference. Access rules to confirm.", "pill": "CONFIRMED", "style": "dark"},
        {"id": "entities", "x": 214, "y": 0, "w": 100, "h": 180, "title": "entities · KYC", "body": "national_entity · INDIVIDUAL\ntax_id · •••• 6789\ndocument_number · •••• 4421\ndocumentation · KYC files\nonboarding · SUCCEEDED\nBanking API. Responses return the last four.", "pill": "CONFIRMED", "style": "dark"},
        {"id": "tables", "x": 321, "y": 0, "w": 99, "h": 180, "title": "your tables · PII", "body": "customer_records · table\nidentity_documents · table\nprotection · per column\nretention · per record\naccess · per role\nOn our product page. API reference not yet public.", "pill": "OPEN", "style": "outline"},
    ],
    "connectors": [],
    "side": {"header": "WHY IT MATTERS", "items": [
        {"title": "Today", "body": "Cards are vaulted. Bank details can be stored through the enroll API. Entity data goes through the banking API and comes back masked."},
        {"title": "Next", "body": "Tables you define for any other record. We show you where they stand in a working session, not on a slide."},
    ]},
    "notes": "You told us the product is heading to full banking as a service, so the vault has to hold more than cards. Here is where each kind of data lives today. Cards are vaulted. Bank account details can be stored through the enroll API with no provider involved; we still owe you the exact access rules for that. Entity data for onboarding goes through the banking API, and the tax ID and document number come back masked to the last four; how that data is stored is part of open item one. The fourth class is tables you define yourself for any other personal record. That is on our product page and our roadmap, but the API reference is not public yet, so we mark it open and will walk you through its real state with the Trust & Vault product team.",
}

# ---------------------------------------------------------------- S8 checklist (seven rows verbatim)
SLIDES["questions-1"] = {
    "id": "questions-1", "type": "checklist_table",
    "kicker": "WHAT THE VAULT HAS TO HOLD · THE QUESTIONS",
    "headline": "The questions a careful vault buyer asks first, answered before you ask (1 of 3).",
    "columns": ["#", "The question", "Our answer", "Basis"],
    "col_widths": [0.04, 0.30, 0.52, 0.14],
    "header_style": "dark", "font_size": 7.5, "bold_first_col": False, "zebra": True,
    "rows": [
        ["1", {"text": "Can we store a card without charging it?", "bold": True}, "Yes. SDK enrollment creates a vaulted token without a charge. Zero-amount verification is optional where the provider supports it.", {"text": "", "pill": "CONFIRMED"}],
        ["2", {"text": "Can we send a stored card to an endpoint we choose?", "bold": True}, "Yes. The forward proxy sends it to any HTTPS host on your allowlist, including providers Yuno does not connect to.", {"text": "", "pill": "CONFIRMED", "pill2": "BETA"}],
        ["3", {"text": "What happens to the CVV?", "bold": True}, "It is never stored. Per the proxy guide it is held briefly after entry, 3 hours by default, for a first charge.", {"text": "", "pill": "CONFIRMED", "pill2": "BETA"}],
        ["4", {"text": "Can we charge with network tokens on our own processor and stay out of PCI scope?", "bold": True}, "Yes. Cryptogram-only mode (Visa, Mastercard; enabled per organization) needs no PCI certification: it returns no card data and the proxy fills in the token. Recurring charges add the network transaction ID.", {"text": "", "pill": "CONFIRMED", "pill2": "BETA"}],
        ["5", {"text": "Whose name are network tokens registered in?", "bold": True}, "Our API reference says Yuno holds the token requestor ID. Whether requestor IDs can be registered in your name is open, per network. Written answer with the RFP response.", {"text": "", "pill": "OPEN"}],
        ["6", {"text": "How do we leave?", "bold": True}, "A documented card export: a written request, the recipient's PCI DSS attestation, and a PGP-encrypted file over SFTP.", {"text": "", "pill": "CONFIRMED"}],
        ["7", {"text": "What uptime do you commit to, and how does it fail over?", "bold": True}, "Our published SLA (y.uno/sla) commits to 99.90% monthly availability and a 5-minute response on critical incidents. The contractual figure for OnlyFans, the failover design and rate limits come with the RFP response.", {"text": "Engineering", "pill": "CONFIRMED", "pill2": "OPEN"}],
    ],
    "notes": "These are the questions that decide a vault evaluation, and the ones that get tested in a sandbox. Six of the seven are documented today; three of those depend on the proxy, which is in beta and switched on per organization. Two are open and we say so: the token requestor model per network, and the contractual uptime and failover design. On both you get a written answer with the RFP response. Row 3: the proxy overview and guide document the 3-hour window; the Invoke Forward Proxy API reference page states that the security code cannot be injected, and Phase 0 shows the actual behavior. Row 7: the published SLA annex is at y.uno/sla; the figure that binds is the one in your contract. Eight more questions continue on the next two slides.",
}

# ---------------------------------------------------------------- S10 proxy how
SLIDES["proxy-how"] = {
    "id": "proxy-how", "type": "code_before_after",
    "kicker": K_VAULT + " · PROXY · HOW IT WORKS",
    "headline": "You write the request your provider expects and mark the tokens. The proxy swaps in the real values and forwards it.",
    "tag": ["CONFIRMED", "BETA"],
    "source": "Source: docs.y.uno, PCI Proxy. In the API changelog since 11 July 2026. Read 7 October 2026.",
    "left": {"title": "AS ONLYFANS SENDS IT", "code": "POST /v1/pci-proxy/forward\nyuno-proxy-destination-url:\n  https://api.provider.example/v1/payouts\n{\n  \"amount\": 2500,\n  \"number\": \"{{vaulted_token.9f2a….number}}\",\n  \"name\": \"{{vaulted_token.9f2a….holder_name}}\"\n}"},
    "middle": {"title": "Yuno proxy", "sub": "Tokens resolved inside PCI DSS Level 1"},
    "right": {"title": "AS THE DESTINATION RECEIVES IT", "code": "POST https://api.provider.example/v1/payouts\n{\n  \"amount\": 2500,\n  \"number\": \"4821 •••• •••• 0193\",\n  \"name\": \"ANA SOUZA\"\n}", "caption": "Destination and body illustrative; header and expression syntax as documented. Card number masked for the slide."},
    "side": {"header": "WHAT YOU GET", "items": [
        {"title": "Your format", "body": "Your request body, your provider. No waiting for Yuno to build a connector."},
        {"title": "Any destination", "body": "A processor Yuno does not orchestrate, a fraud or issuer service, or your own acquiring connection."},
        {"title": "In beta", "body": "Enabled per organization in production. The sandbox is open for testing today."},
    ]},
    "notes": "The proxy sends stored card data to any provider API you choose. Your backend builds the exact request a provider expects and puts token expressions where the card data goes. Yuno resolves them inside its PCI environment and forwards the call. The destination does not have to be a provider Yuno integrates. For issuers specifically, note the limits on slide {{slide:app-limits}}: capturing or displaying a card your issuer creates is not something the proxy does today. To be clear on status: this has been in our API changelog since July, it is in beta, and production access is switched on per organization. Your team can test it in the sandbox now.",
}

# ---------------------------------------------------------------- S11 proxy controls
SLIDES["proxy-controls"] = {
    "id": "proxy-controls", "type": "cards_row",
    "kicker": K_VAULT + " · PROXY · CONTROLS",
    "headline": "The controls you would otherwise build around card data come with the proxy.",
    "source": "Source: docs.y.uno, PCI Proxy overview, destination allowlist and destination authentication. Read 7 October 2026.",
    "cards": [
        {"pill": "CONFIRMED", "pill2": "BETA", "eyebrow": "ALLOWLIST", "title": "Only hosts you register", "body": "Exact hostname, HTTPS on port 443, no IP addresses or wildcards. You register a host by API and it is usable within minutes. Scope it to one account or the whole organization. Every change lands in an append-only audit log."},
        {"pill": "CONFIRMED", "pill2": "BETA", "eyebrow": "AUTHENTICATION", "title": "Mutual TLS per destination", "body": "Yuno presents your client certificate in the handshake. The private key is write-only and encrypted with a dedicated KMS key. One request-signing scheme is built in today, for dLocal."},
        {"pill": "CONFIRMED", "pill2": "BETA", "eyebrow": "HYGIENE", "title": "Nothing kept, every call recorded", "body": "Request and response bodies are not stored or logged. Every call produces an audit record. A card number echoed back by a destination is redacted to its last four digits."},
    ],
    "limits": {"header": "LIMITS TO PLAN FOR", "tiles": [
        {"value": "20", "label": "tokens per request"}, {"value": "1 MB", "label": "request and response body"},
        {"value": "30 s", "label": "timeout, up to 120 s by header"}, {"value": "TLS 1.2", "label": "or higher, on every destination"},
    ]},
    "notes": "A proxy that can send card data anywhere is only safe with controls around it. Destinations are an allowlist you manage by API. Mutual TLS is configured per destination. Bodies are never stored, every call leaves an audit record, and card numbers that come back in a response are redacted. The limits at the bottom are the documented ones, so your engineers can plan around them now.",
}

# ---------------------------------------------------------------- S13 banking
SLIDES["banking"] = {
    "id": "banking", "type": "diagram",
    "kicker": K_VAULT + " · DECISION LAYER · THE BANKING API",
    "headline": "Entity, onboarding, account and transfer are separate objects, and every onboarding names the provider connection it runs on.",
    "tag": ["CONFIRMED"],
    "source": "Source: docs.y.uno, Banking Connectivity reference, read 7 October 2026. One entity on several connections: open.",
    "boxes": [
        {"id": "creator", "x": 0, "y": 20, "w": 90, "h": 50, "title": "Creator", "body": "One entity: individual or business", "style": "outline"},
        {"id": "onb", "x": 0, "y": 110, "w": 90, "h": 56, "title": "Onboarding", "body": "KYC or KYB, on a named provider connection", "style": "light"},
        {"id": "yuno", "x": 118, "y": 60, "w": 100, "h": 70, "title": "Yuno", "body": "Banking Connectivity API", "style": "blue"},
        {"id": "accA", "x": 240, "y": 0, "w": 104, "h": 50, "title": "Account · connection A", "body": "Account and routing number", "style": "light"},
        {"id": "accB", "x": 240, "y": 60, "w": 104, "h": 50, "title": "Account · connection B", "body": "Account and routing number", "style": "light"},
        {"id": "accC", "x": 240, "y": 120, "w": 104, "h": 50, "title": "Account · connection C", "body": "Account and routing number", "style": "light"},
        {"id": "transfers", "x": 354, "y": 40, "w": 66, "h": 90, "title": "Transfers", "body": "ACH: standard, same day\nWire and RTP\nBook transfers", "style": "dark"},
        {"id": "code", "x": 0, "y": 200, "w": 420, "h": 50, "title": "\"yuno_connection_id\": \"your Bank A connection\"", "body": "A required field on every onboarding request. Your system sets it.", "style": "dark"},
    ],
    "connectors": [
        {"from": "creator", "to": "onb"}, {"from": "onb", "to": "yuno"},
        {"from": "yuno", "to": "accA"}, {"from": "yuno", "to": "accB"}, {"from": "yuno", "to": "accC"},
        {"from": "accA", "to": "transfers"}, {"from": "accB", "to": "transfers"}, {"from": "accC", "to": "transfers"},
    ],
    "side": {"header": "WHAT YOU GET", "items": [
        {"title": "One API", "body": "Entities, onboarding, accounts and transfers across banking providers in the US, UK, Australia and EU."},
        {"title": "US rails", "body": "ACH standard, ACH same day, wire and RTP, with status by webhook."},
        {"title": "Open", "body": "Which US providers are connected today, and one entity on several connections: named in writing."},
    ]},
    "notes": "This is the part of your design we described to you, and it is in our public API reference. A creator is an entity. Onboarding runs KYC or KYB on a provider connection that the request names. An approved onboarding lets you open an account, which comes back with an account and routing number. Transfers run on ACH, same-day ACH, wire and RTP. What the reference does not state, and we therefore mark open, is which US banking providers are connected today and whether one entity can hold onboardings on several connections at once. We will name both in writing, and the second is the first thing to prove in a sandbox.",
}

# ---------------------------------------------------------------- S14 who decides
SLIDES["who-decides"] = {
    "id": "who-decides", "type": "cards_row",
    "kicker": K_VAULT + " · DECISION LAYER · WHO DECIDES",
    "headline": "You asked who decides where each creator lands. You do: per call for banking today, and by rule for card payments.",
    "source": "Source: docs.y.uno, Banking Connectivity; Routing; Monitors; Audit logs; Roles. Read 7 October 2026.",
    "cards": [
        {"pill": "CONFIRMED", "eyebrow": "PER CALL", "title": "Banking: your policy names the provider", "body": "Every onboarding request carries the provider connection it should run on. Your own allocation logic picks the bank. Yuno executes on it and reports status back by webhook."},
        {"pill": "CONFIRMED", "eyebrow": "BY RULE", "title": "Cards: rules you configure", "body": "Conditions on country, amount, BIN, brand and your own metadata. Percentage splits. Fallback steps on decline, error rate or timeout. Monitors that move traffic away and bring it back."},
        {"pill": "OPEN", "eyebrow": "BY RULE", "title": "Banks and issuers: the same rules for accounts", "body": "Allocating creators across banks and issuers by rules you set is what we described to you. It is not in the public API reference yet. Owner: Yuno product, in writing with the RFP response."},
    ],
    "side": {"header": "WHAT YOU GET", "items": [
        {"title": "Yours", "body": "The policy belongs to OnlyFans. The API takes the connection you name on each onboarding."},
        {"title": "Changeable", "body": "A new bank for a creator is a new onboarding on that connection (one entity on several is open item 3). Card traffic moves by changing a rule."},
        {"title": "Visible", "body": "Audit logs for dashboard and API activity, custom roles and SAML sign-on."},
    ]},
    "notes": "You asked this more than once, so here is the precise answer. Today, for banking, the decision is literally yours on every call: the onboarding request names the provider connection, so your allocation policy picks the bank and Yuno executes. For card payments, rule-based routing is a mature product: conditions, splits, fallbacks and monitors, set by you. What we told you about rule-based allocation across banks and issuers is where the product is going; it is not in the public reference yet, so we mark it open and owe you a written answer.",
}

# ---------------------------------------------------------------- S16 versus thesis
SLIDES["versus-thesis"] = {
    "id": "versus-thesis", "type": "cards_row",
    "kicker": K_VS + " · THE DIFFERENCE",
    "headline": "A standalone vault is built to store and forward. The rules that decide where each request goes are yours to write and maintain.",
    "cards": [
        {"pill": "PUBLIC DOCS", "eyebrow": "VGS", "title": "\"VGS does not make routing decisions for you.\"", "body": "\"VGS powers orchestration, but does not act as the orchestrator.\"", "foot": "verygoodsecurity.com, payment orchestration page"},
        {"pill": "PUBLIC DOCS", "eyebrow": "BASIS THEORY", "title": "Its vault \"operates independently of any payment processor or orchestration layer.\"", "body": "Its creator-economy page markets routing and retries across processors. We found no rules product. Ask who writes and maintains the rules.", "foot": "Basis Theory press release, 14 October 2025; basistheory.com"},
        {"eyebrow": "WHAT STAYS ON YOUR ROADMAP", "title": "With a standalone vault", "body": "The rules for which bank, issuer or processor each request goes to\nRetries, fallbacks and failover between providers\nEvery provider integration, and its upkeep when an API changes\nMoving money: accounts, transfers and payouts"},
    ],
    "bar": "**So what.** You already asked the hard question: who decides. With a standalone vault, the rules and every connection are yours to build and maintain. With Yuno, card routing is a rule you configure today and bank allocation is a value you set per call; rules for banks are an open item on slide {{slide:owe}}.",
    "notes": "This is the one difference that matters for your design, in the vendors' own words. VGS says plainly that it does not make routing decisions for you. Basis Theory describes its vault as independent of any processor or orchestration layer. That independence is a real strength if storage is the whole job. In a product with two to five banks, several issuers and several transfer providers per creator, it means the rules, the failover logic and the upkeep of every integration sit with you. Ask each vendor exactly how much of that they run for you.",
}

# ---------------------------------------------------------------- S17 versus table
SLIDES["versus-table"] = {
    "id": "versus-table", "type": "table",
    "kicker": K_VS + " · ITEM BY ITEM",
    "headline": "Nine things your design needs, and who leads on each.",
    "tag": ["PUBLIC DOCS"],
    "source": "Yuno: docs.y.uno and y.uno. VGS and Basis Theory: public pages. Read 7 October 2026. \"Found\" means in the pages read.",
    "columns": ["#", "Your design needs", "Yuno", "VGS", "Basis Theory", "Who leads"],
    "col_widths": [0.035, 0.20, 0.235, 0.21, 0.21, 0.11],
    "header_style": "dark", "font_size": 7, "bold_first_col": False, "zebra": True,
    "rows": [
        ["1", {"text": "PCI DSS Level 1 card vault", "bold": True}, "Yes, hosted capture fields", "Yes, Collect and Show", "Yes, Elements", {"text": "Level", "bold": True}],
        ["2", {"text": "Network tokens", "bold": True}, "Three networks. Requestor model open", "Four networks", "Requestor ID created for you", {"text": "Vaults lead", "bold": True}],
        ["3", {"text": "A proxy to any destination", "bold": True}, "Outbound, in beta. No inbound route or custom code", "Inbound and outbound routes, plus custom code", "Proxy, plus serverless Reactors", {"text": "Vaults lead", "bold": True}],
        ["4", {"text": "Bank accounts, tax IDs, documents", "bold": True}, "Bank accounts: yes. Tables for other records: open", "PII, bank accounts and IBANs as aliases", "Token types for bank, SSN and EIN data", {"text": "Vaults lead", "bold": True}],
        ["5", {"text": "Show an issued card, set its PIN", "bold": True}, "Not in our public documentation", "Card display with VGS Show", "Card display; PIN set with Lithic and Marqeta", {"text": "Vaults lead", "bold": True}],
        ["6", {"text": "Rules for where each request goes", "bold": True}, "Card payments: rules, splits, fallbacks. Banks: per call", "Says it \"does not make routing decisions for you\"", "Routing and retries marketed; no rules product found", {"text": "Yuno leads", "bold": True}],
        ["7", {"text": "Provider connections built for you", "bold": True}, "460+ processor integrations. US banks: open", "Your own logic, or an orchestrator partner", "Proxy requests you write per provider", {"text": "Yuno leads", "bold": True}],
        ["8", {"text": "Bank accounts and transfers by API", "bold": True}, "Entities, accounts, ACH, wire and RTP", "No API found. Forwards bank details to your processor", "No API found. Forwards bank details to your processor", {"text": "Yuno leads", "bold": True}],
        ["9", {"text": "Payouts and split payments", "bold": True}, "Payouts API, split payments", "Via partners like TabaPay, Astra", "No payouts product found", {"text": "Yuno leads", "bold": True}],
    ],
    "notes": "The comparison row by row. Rows two to five are where VGS and Basis Theory lead today, and we would rather you hear it from us: deeper network token programs, a more established proxy with custom code, token types built for personal data, and tooling to show an issued card, plus PIN setting at Basis Theory. The next two slides take each vendor on its own. Rows six to nine are what your architecture adds on top of a vault, and that is where Yuno leads. The competitor columns come from their public pages on 7 October; where a cell says something was not found, we mean on those pages, so please confirm with them.",
}

# ---------------------------------------------------------------- S18 versus BT
SLIDES["versus-bt"] = {
    "id": "versus-bt", "type": "table",
    "kicker": K_VS + " · BASIS THEORY",
    "headline": "Basis Theory goes deeper on the vault. Yuno goes further above it.",
    "tag": ["PUBLIC DOCS"],
    "source": "Basis Theory: basistheory.com and developers.basistheory.com. Yuno: docs.y.uno and y.uno. Read 7 October 2026.",
    "columns": ["What you need", "Yuno", "Basis Theory", "Who leads"],
    "col_widths": [0.20, 0.34, 0.34, 0.12],
    "header_style": "dark", "font_size": 7, "bold_first_col": True, "zebra": True,
    "rows": [
        ["Card capture and storage", "SDK enrollment into a PCI DSS Level 1 vault", "Elements into a PCI DSS Level 1 vault", {"text": "Level", "bold": True}],
        ["Data beyond cards", "Bank details through the enroll API. Tables for personal records: open", "Token types for bank accounts, SSN, EIN and generic data", {"text": "Basis Theory", "bold": True}],
        ["Proxy and custom code", "Outbound proxy, in beta. No inbound route and no custom code", "Proxy with request and response transforms, plus serverless Reactors", {"text": "Basis Theory", "bold": True}],
        ["Card issuing", "Stored card data can go to issuer APIs. Card display and PIN: not in our docs", "Guides to issue and display cards. PIN setting documented for Lithic and Marqeta", {"text": "Basis Theory", "bold": True}],
        ["Token requestor ID", "Yuno holds it, per our API reference. In your name: open", "Creates one for you with each network. Existing network tokens are re-provisioned, not imported", {"text": "Basis Theory", "bold": True}],
        ["Routing rules and failover", "A rules product for card payments: conditions, splits, fallbacks and monitors", "Routing and retries marketed. No rules product found", {"text": "Yuno", "bold": True}],
        ["Provider integrations", "460+ processor integrations. US banks: open", "Proxy requests you write for each provider. No pre-built connectors found", {"text": "Yuno", "bold": True}],
        ["Bank accounts and transfers", "Banking Connectivity API: entities, accounts, ACH, wire and RTP", "No accounts or transfers API found. Stores bank details and forwards them to your processor", {"text": "Yuno", "bold": True}],
        ["Payouts", "Payouts API and split payments", "No payouts product found. Forwards to payout processors you choose", {"text": "Yuno", "bold": True}],
    ],
    "notes": "Basis Theory on its own. It is a strong vault, and it knows your sector: its creator-economy page quotes a creator platform whose processor shut it off without warning. It leads us on four rows today: token types for personal data, a proxy with transforms and serverless code, card issuing guides, and a clear statement that it creates the token requestor ID for you. We lead on the four rows above the vault: a rules product for routing and failover, processor integrations that are already built, a banking API, and payouts. Two questions worth asking them: who writes and maintains the routing rules they market, and what the cost is at your scale. On 8 October 2026 their Payments Routing guide still read \"This guide is currently under construction.\" Their network tokens page names Pagos as the subprocessor behind network tokens and the account updater; ask both of us for the equivalent list. Their public list price is 995 dollars a month for 20,000 stored tokens, then 5 cents per additional token each month; ask for the enterprise schedule at your volume.",
}

# ---------------------------------------------------------------- S19 versus VGS
SLIDES["versus-vgs"] = {
    "id": "versus-vgs", "type": "table",
    "kicker": K_VS + " · VGS",
    "headline": "VGS stores and reveals. Its own guide leaves the decisions to you.",
    "tag": ["PUBLIC DOCS"],
    "source": "VGS: verygoodsecurity.com and docs.verygoodsecurity.com. Yuno: docs.y.uno and y.uno. Read 7 October 2026.",
    "columns": ["What you need", "Yuno", "VGS", "Who leads"],
    "col_widths": [0.20, 0.34, 0.34, 0.12],
    "header_style": "dark", "font_size": 7, "bold_first_col": True, "zebra": True,
    "rows": [
        ["Card capture and storage", "SDK enrollment into a PCI DSS Level 1 vault", "VGS Collect and Show, PCI DSS Level 1 vault", {"text": "Level", "bold": True}],
        ["Data beyond cards", "Bank details through the enroll API. Tables for personal records: open", "PII, bank account numbers and IBANs stored as aliases", {"text": "VGS", "bold": True}],
        ["Proxy and custom code", "Outbound proxy, in beta. No inbound route and no custom code", "Inbound and outbound routes, plus custom code that runs in the proxy", {"text": "VGS", "bold": True}],
        ["Card issuing", "Stored card data can go to issuer APIs. Card display and PIN: not in our docs", "Card issuing guide (examples: Marqeta, I2C, Galileo), with card display through VGS Show", {"text": "VGS", "bold": True}],
        ["Network tokens", "Visa, Mastercard and American Express once activated. Cryptograms: Visa and Mastercard", "Says it is the only neutral vault connected to all four major networks", {"text": "VGS", "bold": True}],
        ["Routing rules and failover", "A rules product for card payments: conditions, splits, fallbacks and monitors", "\"Your application keeps ownership of provider selection, routing, and failover logic.\"", {"text": "Yuno", "bold": True}],
        ["Provider integrations", "460+ processor integrations. US banks: open", "Your own logic, or an orchestrator partner", {"text": "Yuno", "bold": True}],
        ["Bank accounts and transfers", "Banking Connectivity API: entities, accounts, ACH, wire and RTP", "No accounts or transfers API found. Tokenizes bank details and forwards them to your processor", {"text": "Yuno", "bold": True}],
        ["Payouts", "Payouts API and split payments", "Via partners, including TabaPay and Astra", {"text": "Yuno", "bold": True}],
    ],
    "notes": "VGS on its own. It is one of the longest-established independent vaults, and it leads us on four rows today: aliases for personal and bank data, inbound and outbound proxy routes with custom code, a card issuing guide with card display, and network token reach, where it says it is the only neutral vault connected to all four major networks. VGS is also explicit about where its scope ends. Its orchestration page says it does not make routing decisions for you, and its guide to integrating a second payment provider says your application keeps ownership of provider selection, routing and failover logic. For a product with several banks, issuers and transfer providers per creator, that logic is most of the work. That is the part Yuno covers for card payments today, and the part we are extending to banks. On network tokens, VGS's own documentation scopes Discover to US merchant IDs and American Express to direct merchants, so ask for the exact coverage for your entity. VGS's public pricing starts at 1,000 dollars a month; ask both of us for the cost at your scale.",
}

# ---------------------------------------------------------------- S20 shape
SLIDES["shape"] = {
    "id": "shape", "type": "phases",
    "kicker": K_PATH + " · PROPOSED SHAPE",
    "headline": "Three phases that mirror your scope, each with a test you can run to close it.",
    "cards": [
        {"eyebrow": "PHASE 0 · SANDBOX PROOF", "title": "Prove it on your own requests", "body": "Your engineers vault test cards and bank details, forward the cards through the proxy to two destinations you pick, and walk the banking API with our product team.", "exit_label": "THE EXIT", "exit": "Every Confirmed capability your Phase 1 relies on is shown working to your engineers, or we change the label."},
        {"eyebrow": "PHASE 1 · US BALANCES", "title": "Cards, accounts and your first banks", "body": "The vault in production for US creators. Banking connections live. Allocation by your policy, per call, with API activity in the audit log.", "exit_label": "THE EXIT", "exit": "One creator holds accounts on two banking connections, opened from one entity record. Depends on open item 3."},
        {"eyebrow": "PHASE 2 · ISSUERS AND BEYOND", "title": "Issuers, and more records", "body": "Stored card data sent to issuer APIs through the proxy. Tables for identity and customer records as they land. Stablecoin conversion providers scoped with you.", "exit_label": "THE EXIT", "exit": "Adding or swapping a provider is a configuration change on your side, not a project."},
    ],
    "bar": "**At any phase.** You can leave with your cards: a documented export, on written request, to a recipient with a valid PCI DSS attestation. Export of bank and entity data is one of the open items.",
    "notes": "We are proposing phases, not dates, until we have seen your RFP timeline. Phase 0 is a sandbox proof on your own requests, and its exit is simple: every capability this deck marks Confirmed that your Phase 1 relies on has to run for your engineers, or we change the label. Phase 1 is your stated scope, US balances. Phase 2 brings in issuers through the proxy and the wider data vault as it lands.",
}

# ---------------------------------------------------------------- S21 owe
SLIDES["owe"] = {
    "id": "owe", "type": "open_items_table",
    "kicker": "APPENDIX · WHAT WE OWE YOU",
    "headline": "Six open items, each with an owner and a written answer in our RFP response.",
    "columns": ["#", "Open item", "Why it matters to you", "Owner at Yuno"],
    "col_widths": [0.04, 0.46, 0.34, 0.16],
    "header_style": "dark", "font_size": 7.5, "bold_first_col": False, "zebra": True,
    "rows": [
        ["1", "Tables you define for identity and customer records, and how bank and entity data is stored and accessed: availability and API reference", "Banking as a service puts far more than cards in the vault.", {"text": "Trust & Vault product", "bold": True}],
        ["2", "Rule-based allocation of creators across banks and issuers", "It turns \"who decides\" from code you maintain into a rule you set.", {"text": "Product", "bold": True}],
        ["3", "US banking and issuing providers connected today, their policy for your category, and one entity on several connections", "No single bank should be able to cut a creator off. That depends on which banks are behind the API.", {"text": "Partnerships", "bold": True}],
        ["4", "Token requestor model and scheme activation per network; network transaction IDs captured through the proxy and included in the export, with bank and entity data", "Together they decide what you can take with you if you ever change vault.", {"text": "Trust & Vault product, Legal", "bold": True}],
        ["5", "Contractual uptime, failover design, rate limits, and the security pack: subprocessors, connection model per card network, key management and regions", "A vault in the payment path must never be the weak point.", {"text": "Engineering, Security", "bold": True}],
        ["6", "Yield and stablecoin partners (Jiko, Coinbase, Triple-A): confirmation of the connections and their terms", "Yield on balances is part of your design, and outside the vault itself.", {"text": "Partnerships", "bold": True}],
    ],
    "notes": "These are the six things we have not confirmed in writing, collected in one place. Each has an owning team at Yuno, and each gets a written answer with our RFP response. If any of them is a deciding factor for you, tell us now and we will answer it first.",
}

# ---------------------------------------------------------------- S22 next
SLIDES["next"] = {
    "id": "next", "type": "next_steps",
    "kicker": K_PATH + " · NEXT STEPS",
    "headline": "Include us, then test us.",
    "cards": [
        {"eyebrow": "STEP 01 · ONLYFANS", "num": "01", "title": "Share the RFP requirements", "body": "And the timeline, so we answer in your format and to your deadline."},
        {"eyebrow": "STEP 02 · TOGETHER", "num": "02", "title": "One working session", "body": "Your payments and engineering leads with our Trust & Vault product team: vault, proxy and banking API in the sandbox."},
        {"eyebrow": "STEP 03 · YUNO", "num": "03", "title": "Written answers", "body": "The six open items and the full RFP response, with nothing left as a placeholder."},
    ],
    "contact": "Samuel Vieira · Business Development · samuel@y.uno",
    "notes": "The ask is simple: include Yuno in the RFP, and then test what we have shown you. Send us the requirements and the timeline. Give us one working session with your payments and engineering leads and our Trust & Vault product team, in the sandbox. We will come back with written answers to every open item and a complete response.",
}

# ---------------------------------------------------------------- S23 limits
SLIDES["app-limits"] = {
    "id": "app-limits", "type": "table",
    "kicker": "APPENDIX · LIMITS TO PLAN FOR",
    "headline": "What the vault and proxy do not do today, so you can plan around it.",
    "source": "From docs.y.uno, read 7 October 2026. The proxy is in beta and enabled per organization.",
    "columns": ["Item", "Today", "Basis"],
    "col_widths": [0.20, 0.64, 0.16],
    "header_style": "dark", "font_size": 7.5, "bold_first_col": True, "zebra": True,
    "rows": [
        ["Inbound proxy", "Not in the public API reference. The forward proxy is outbound only.", {"text": "", "pill": "NOT IN DOCS"}],
        ["Cards issued by your issuer", "A card number returned by a destination is redacted, not vaulted. Showing an issued card to its holder and setting a PIN are not documented.", {"text": "", "pill": "NOT IN DOCS"}],
        ["Custom code on stored tokens", "Not offered today.", {"text": "", "pill": "NOT IN DOCS"}],
        ["BIN lookup as its own API", "No standalone endpoint. BIN, brand, issuer, type and country come back with each stored card.", {"text": "", "pill": "CONFIRMED"}],
        ["Signing and cryptograms", "One built-in request-signing scheme, for dLocal; mutual TLS for other destinations. Network token cryptograms for Visa and Mastercard.", {"text": "", "pill": "CONFIRMED"}],
        ["What the proxy resolves", "Card fields only: number, expiration, holder name, network token, network transaction ID and, per the proxy guide, the security code inside its window. Bank data is not resolved by the proxy.", {"text": "", "pill": "CONFIRMED"}],
        ["Token search", "Stored payment methods are listed per customer. There is no vault-wide search in the reference.", {"text": "", "pill": "CONFIRMED"}],
        ["Idempotent forwards", "Not in the public API reference. Until it is, a retry after a timeout needs a status check at the destination.", {"text": "", "pill": "NOT IN DOCS"}],
        ["Agent credentials", "Visa Intelligent Commerce and Mastercard Agent Pay credentials are not in our documentation today.", {"text": "", "pill": "NOT IN DOCS"}],
    ],
    "notes": "Appendix. These are the limits as they stand today, so nobody on your side discovers them later. The two that matter most for an issuing use case are the first two: there is no inbound proxy in the public reference, and a card number that comes back from your issuer is redacted rather than vaulted. If your Phase 1 needs to show an issued card to a creator or set a PIN, that is a gap for us today and a strength of a standalone vault.",
}

# ---------------------------------------------------------------- S24 who we are
SLIDES["app-who"] = {
    "id": "app-who", "type": "stats",
    "kicker": "APPENDIX · WHO WE ARE",
    "headline": "The vault runs in a PCI DSS Level 1 environment.",
    "source": "Source: y.uno vault product page and docs.y.uno API environments, read 7 October 2026.",
    "tiles": [
        {"label": "INTEGRATIONS", "value": "460+", "caption": "Processor integrations: PSPs, gateways and acquirers the vault can detokenize to."},
        {"label": "COUNTRIES COVERED", "value": "190+", "caption": "With separate API environments for the US (api.y.uno) and EMEA (api.eu.y.uno)."},
        {"label": "CERTIFICATIONS", "value": "4", "caption": "Plus registration as a Visa Service Provider, as listed on y.uno. Attestation scope on request."},
    ],
    "chips": ["PCI DSS Level 1", "SOC 2 Type 2", "ISO 27001", "ISO 27701", "Visa Service Provider"],
    "notes": "Appendix. Yuno in three numbers, all from our public site. More than 460 processor integrations the vault can detokenize to. Coverage in more than 190 countries, with separate API environments for the US and EMEA. Four certifications plus Visa Service Provider registration, as listed on our site; ask us for the attestation documents and their scope and we will route the request to our security team.",
}

# ---------------------------------------------------------------- S25 sources (extended by make_spec with the OnlyFans ledger sources)
SLIDES["app-sources"] = {
    "id": "app-sources", "type": "sources",
    "kicker": "APPENDIX · SOURCES",
    "headline": "Every page behind this deck, all read on 7 October 2026 unless dated otherwise.",
    "cols": [
        {"header": "YUNO", "pill": "CONFIRMED", "items": [
            "docs.y.uno · Tokens; PCI compliance; Enroll payment methods",
            "docs.y.uno · PCI Proxy: overview, forward proxy, destination allowlist, destination authentication",
            "docs.y.uno · Network tokens; Generate network token cryptogram; Card account updater",
            "docs.y.uno · Token migration process; Exporting tokens from Yuno",
            "docs.y.uno · Banking Connectivity reference: entities, onboarding, accounts, transfers",
            "docs.y.uno · Routing; Monitors; Audit logs; Roles; Security; API environments",
            "docs.y.uno · Payouts; Split payments marketplace",
            "docs.y.uno · API changelog, July to September 2026",
            "docs.y.uno · Stored credentials; Network token migration process; 3DS Standalone; Web SDK references",
            "y.uno · Vault product page; Trust and security page; SLA page (y.uno/sla, last update 24 October 2025); Success stories; About",
            "status.y.uno · Public status page and incident history",
        ]},
        {"header": "VGS AND BASIS THEORY", "pill": "PUBLIC DOCS", "items": [
            "verygoodsecurity.com · Payment orchestration; Vault; Network tokens; Card issuers; Pricing",
            "docs.verygoodsecurity.com · Integrating a second payment provider; Card issuing; VGS Compute (Larky)",
            "basistheory.com · Platform; Creator economy; Pricing details",
            "developers.basistheory.com · Token types; Network tokens; Issue cards; Set card PIN",
            "Basis Theory Series B announcement · 14 October 2025, as republished by the Merchant Risk Council",
            "developers.basistheory.com · Payments routing guide, read 8 October 2026",
        ]},
    ],
    "footnote": "Competitor lines are our reading of public pages on the date shown. Products change. Please confirm each one with the vendor before you rely on it.",
    "notes": "Appendix. The pages behind every claim, so your team can open them. Yuno claims come from our public documentation and product page. Competitor lines come from their own public pages on the same date; please confirm them with each vendor.",
}

# Samuel's dividers (S5, S9, S12, S15) are replaced by the deck's section dividers; their speaker notes are folded into the 06 and 07 dividers:
DIVIDER_NOTES = {
    "d06": "Section six is the RFP itself: the vault, the proxy and the decision layer. What the vault does for cards, what it holds beyond cards, how a stored card reaches a provider you chose, including providers Yuno does not connect to, and the question you asked most: who decides which bank and which provider each creator lands on. The proxy is in beta and we say so on each slide.",
    "d07": "Section seven compares Yuno with the two standalone vaults you are most likely evaluating. Both are good products. We show where they lead as well as where they stop.",
}
