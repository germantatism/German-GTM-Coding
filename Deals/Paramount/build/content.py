# -*- coding: utf-8 -*-
"""Copy for the Skydance token vault deck (22 Oct 2026). Merchant claims trace to research/*.md; Yuno claims to
Deals/OnlyFans/build/yuno_vault_facts.md (docs.y.uno, re-read 8 and 22 Oct 2026)."""

COVER = {
    'title': 'The Skydance Yuno Vault',
    'sub': 'Two services, one vault. Your tokens, your exit.',
    'prep': 'Prepared for Skydance · October 2026 · Strictly confidential',
}

EXEC = {  # slide of_exec_understanding_v2, element id -> new text (styles kept)
    'of_es1_v2_003': 'Skydance needs one vault that both services and every processor can use, under its own rules',
    'of_es1_v2_008': 'What Skydance aims to deliver',
    'of_es1_v2_009': '**One service for Paramount+ and HBO Max without a missed renewal**: every stored card, network token and recurring reference in one place, usable by any processor in any of your markets.',
    'of_es1_v2_011': 'What makes this challenging',
    'of_es1_v2_012': 'Paramount+ bills through Recurly, which vaults its cards and ties gateway tokens to each processor. HBO Max vaults its cards in Spreedly. **Two vaults, two token programs**, and every processor change or consolidation means moving sensitive data again.',
    'of_es1_v2_014': 'The decision now',
    'of_es1_v2_015': 'Skydance is choosing where the combined service\'s credentials will live. That choice decides **who holds every token** and how freely Skydance can add, swap or leave billing platforms and processors.',
    'of_es1_v2_026': 'What we propose\nOne PCI DSS Level 1 Yuno Vault for cards, network tokens and recurring references from both services, a proxy that sends each value only to the processor that needs it, and portable tokens with the exit in the contract.',
}

PROBLEM = {
    'kicker': 'THE VAULT  ›  THE PROBLEM',
    'title': 'Paramount+ and HBO Max keep the same kind of credential in two vaults',
    'before_h': 'Two stacks, two vaults',
    'stacks': [
        ('Paramount+', 'Recurly billing and vault', ["Cards in Recurly's vault", 'Gateway-bound tokens', 'PayPal billing agreements']),
        ('HBO Max', 'Spreedly vault and gateways', ["Cards in Spreedly's vault", 'Spreedly network tokens', 'Adyen, Checkout.com, more']),
    ],
    'before_x': ["Each service's cards and network tokens live in a different vault", 'Two vaults, two token programs, two account updaters to audit', "Merging means moving one side's cards or asking again"],
    'before_src': 'paramountplus.com loads Recurly.js; auth.hbomax.com loads the Spreedly iframe. Recurly and Spreedly developer docs. All read 22 Oct 2026.',
    'after_h': 'One vault',
    'swappable': ['Billing platforms', 'Processors', 'Fraud and 3DS'],
    'vault_pills': ['Cards', 'Network tokens', 'NTIDs', 'Wallet tokens'],
    'after_ok': ['Cards work on any processor you connect', 'One vault to secure and audit', 'Imported from both vaults, no subscriber re-enters a card'],
}

M5 = {  # slide m5_mock
    'm5_hl': 'What Skydance needs',
    'm5_bd0': 'Cards, network tokens, wallet tokens and recurring references in one vault',
    'm5_ad2': 'Routing, retries, failover and renewal logic, built in-house',
    'm5_bd2': 'Routing, retries, failover and Smart Retries on rules you set',
    'm5_bd3': '3DS, account updater, network tokens and subscriptions on the same tokens',
    'm5_band': 'Same independence, far less to build.   Skydance keeps portable tokens and exit terms, and decides how much of the stack Yuno runs.',
}

CARDS = {  # slide vlt_cards
    'vlt_cards__9_244': 'Subscriber cards are stored once and work on every processor you connect',
    'vlt_cards_k038': 'Current vault exports',
    'vlt_cards_k047': 'subscribers untouched',
    'vlt_cards_k050': 'Import from each current vault as PGP-encrypted files over SFTP, network tokens included. Export is documented.',
    'vlt_cards_k052': '**One vaulted token, every processor.** Add or swap a processor and the stored cards keep working, with nothing collected again from subscribers.',
}

NT = {  # slide h7c266de662ba1cf0_9_207
    'h7c266de662ba1cf0_9_210': 'Network tokens and PAR sit next to the card, so one subscriber stays one subscriber across every credential',
    'h7c266de662ba1cf0_9_235': 'One subscriber across card, wallet and reissue: for renewals,\x0bchargebacks and fraud rules.',
    'h7c266de662ba1cf0_9_236': 'Token requestor ID registered under Skydance where the scheme\nallows it. Yuno acts as TS-TRP.',
}

RECUR = {
    'kicker': 'THE VAULT  ›  RECURRING',
    'title': 'The recurring reference travels with the token, so renewals run anywhere',
    'name': 'Maria Lopez', 'ref': 'sub_4471',
    'rows': [  # field, stored as, on a renewal, pill kind
        ('Card PAN', '•••• 0193', 'Tokenized', 'blue'),
        ('Network token', '•••• 7740', 'Tokenized', 'blue'),
        ('Network transaction ID', '3812•••••••2210', 'Sent on every MIT', 'lav'),
        ('Mastercard TLID', 'from the first payment', 'Sent on every MIT', 'lav'),
        ('PAR', '5001•••••••••', 'One subscriber', 'lav'),
        ('Expiry', '09 / 29', 'Account updater', 'lav'),
    ],
    'foot': 'Captured on the first payment. Reused from the vault on every renewal after.',
    'right': [
        ("Renewal on today's processor", 'usage USED, reason SUBSCRIPTION, and the stored network transaction ID go with it.'),
        ('Renewal after a processor switch', "Same token, same NTID, translated into the new provider's format. No new authentication."),
        ('Renewal after a card reissue', 'The account updater refreshes the PAN. Token, NTID and PAR stay the same.'),
    ],
    'quote': 'docs.y.uno: "The network_transaction_id belongs to the card network, not to the provider that processed the first payment." Read 22 Oct 2026.',
}

DESIGN = {  # slide h7c266de662ba1cf0_9_241 (table mockup)
    'h7c266de662ba1cf0_9_250': 'subscribers',
    'h7c266de662ba1cf0_9_251': 'PII',
    'h7c266de662ba1cf0_9_261': 'billing_methods',
    'h7c266de662ba1cf0_9_265': 'billing_methods',
    'h7c266de662ba1cf0_9_276': 'network_token',
    'h7c266de662ba1cf0_9_278': 'PCI',
    'h7c266de662ba1cf0_9_282': 'network_txn_id',
    'h7c266de662ba1cf0_9_284': '—',
    'h7c266de662ba1cf0_9_285': 'Clear',
    'h7c266de662ba1cf0_9_300': 'email',
    'h7c266de662ba1cf0_9_306': 'plan_id',
}

PROXY = {  # slide h7c266de662ba1cf0_9_391
    'h7c266de662ba1cf0_9_398': 'Skydance system',
    'h7c266de662ba1cf0_9_409': 'As Skydance sends it',
}

CONTROLS = {  # slide vlt_controls
    'vlt_controls_k003': 'Skydance system',
    'vlt_controls_k037': '3DS providers',
    'vlt_controls_k038': 'Any allowlisted PCI host',
}

VERSUS = {  # slide vlt_versus
    'vlt_versus__9_244': 'Yuno matches standalone vaults on the core and leads on what a subscription runs on',
    'vlt_versus_k019': 'Visa, Mastercard, Amex; TRID under Skydance',
    # row 5 (issued card / PIN) becomes "Import existing network tokens"
    'vlt_versus_k029': 'Import existing network tokens',
    'vlt_versus_k030': 'Documented import process',
    'vlt_versus_k031': 'Not stated on public pages',
    'vlt_versus_k032': 'Re-provisioned, not imported',
    'vlt_versus_k033': 'Yuno leads',
    # row 9 (payouts) becomes subscriptions
    'vlt_versus_k051': 'Subscriptions and renewal retries',
    'vlt_versus_k052': 'Subscriptions, Smart Retries up to six attempts',
    'vlt_versus_k053': 'Your billing platform',
    'vlt_versus_k054': 'Your billing platform',
    'vlt_versus_k055': 'Yuno leads',
    'vlt_versus_k057': 'Yuno leads on 5, level on 2, the standalone vaults lead on 2. VGS and Basis Theory: their public pages, read 7 and 22 October 2026.',
}
VERSUS_DELETE = []
VERSUS_COLORS = {'vlt_versus_k033': '#3E4FE0'}  # row 5 verdict turns blue (Yuno leads)

PORT = {  # slide h7c266de662ba1cf0_9_469
    'h7c266de662ba1cf0_9_507': "Registered under Skydance's token requestor ID\nwhere the scheme allows it, so they survive a\nchange of processor or of vault. No\nre-tokenization on exit.",
    'h7c266de662ba1cf0_9_511': 'A written request from Skydance',
}

NOTES = {
    'exec': (
        "Labels: CONFIRMED = docs.y.uno or y.uno; BETA = depends on the PCI Proxy (beta, enabled per organization); PUBLIC = the other company's own pages; OPEN = not confirmed in writing, owner named.\n"
        "Paramount+ on Recurly: PUBLIC. paramountplus.com loads https://js.recurly.com/v4/recurly.js, carries a Recurly public key and Recurly plan codes (read 22 Oct 2026); Recurly publishes the CBS Interactive / Paramount+ case study (recurly.com/resources/case-study/cbsi).\n"
        "Recurly vaults cards and ties gateway tokens to a gateway: PUBLIC. docs.recurly.com/docs/payment-gateways: \"Because Recurly stores customer credit card data, you can switch payment gateways at any time\" and \"not all payment data migrates easily, especially tokenized payment instruments\"; token-support page (15 Jul 2026): \"Gateway tokens are not transferable between gateways.\"\n"
        "HBO Max on Spreedly: PUBLIC. auth.hbomax.com production config SPREEDLY_IFRAME_SCRIPT_URL = core.spreedly.com/iframe/iframe-stable.min.js (read 22 Oct 2026); Spreedly lists HBO Max on its homepage logo wall and in its 24 Jun 2025 blog.\n"
        "Group: Skydance 8-K exhibit, 6 Oct 2026: the streaming products \"will unify into a single service over time\"; synergies of \"at least $6 billion\" \"primarily from technology, integration and procurement\"; \"200+ million streaming subscribers across platforms\". Paramount+ 81.6M subscribers at 30 Jun 2026 (10-Q); HBO Max \"nearly 132 million\" at 31 Dec 2025 (WBD letter, 26 Feb 2026), no 2026 count disclosed.\n"
        "What we propose: vault, network tokens, proxy and export are CONFIRMED/BETA per the fact base; \"exit written into the contract\" means the documented export process plus commercial terms agreed in the MSA (OPEN, Legal)."),
    'problem': (
        "Factual, not critical. HBO Max's Spreedly vault is portable by design: Spreedly documents a self-service export (store to about 64 gateways) or a PGP/SFTP export \"within 2 weeks\", one free export per destination (developer.spreedly.com/docs/exporting-payment-methods, read 22 Oct 2026). Spreedly also runs network tokens (TR-TSP, Visa and Mastercard) and lifecycle management for HBO Max's vault.\n"
        "Paramount+ side: Recurly stores cards in its own vault; Recurly support states card data leaves \"only in a tokenized format\" to a PCI-compliant system, handled by Recurly Professional Services (recurly.com/glossary/data-migration). Recurly network tokens are stored \"Recurly and Visa\" and are \"not bound to a single provider\".\n"
        "So the problem is not lock-in. It is two vaults, two token programs, two account updaters and two sets of recurring references for one future service. Yuno's role is the neutral place both can be imported into, with 460+ processor connections and renewals running on the same tokens.\n"
        "Adyen, Checkout.com and iyzico appear as vendor chunks in the HBO Max web bundle; the SDK hosts were not observed on 22 Oct 2026, so say \"Adyen, Checkout.com and others\" if asked. Antom chunk name present, vendor unconfirmed. Kount not seen in the HBO Max bundle; paramountplus.com carries a Recurly Kount flag.\n"
        "Do not quote the internal sales history with Paramount in the room; stick to the public evidence above."),
    'm5': (
        "Standalone vault column = VGS and Basis Theory public pages (7 and 22 Oct 2026). Yuno column: PCI DSS Level 1, SOC 2 Type 2, ISO 27001, ISO 27701, Visa Service Provider (y.uno/product/vault); 460+ processor integrations (same page); routing, Monitors, Smart Retries (docs.y.uno automation page); account updater Visa and Mastercard (docs); network tokens Visa, Mastercard, Amex per docs, activation per scheme confirmed in writing before Phase 1 (OPEN, Trust & Vault).\n"
        "Wallet tokens: Apple Pay and Google Pay payments with vault_on_success store a hidden vaulted token (docs, enrollment page). Apple Pay merchant token storage is not in docs; do not promise it."),
    'cards': (
        "Store: SDKs for Web, iOS, Android, Flutter, React Native; Secure Fields; most SDK merchants qualify for SAQ A, your QSA confirms (docs.y.uno/docs/security-and-compliance/pci-compliance). CONFIRMED.\n"
        "Keep: Card Account Updater, Visa and Mastercard, asynchronous; vaulted_token and fingerprint stay the same; registration up to 100 tokens per request; scheme registration up to 10 working days (docs.y.uno/docs/additional-services/card-account-updater). CONFIRMED. Amex and Discover updater: not in docs.\n"
        "Move: token migration process (PGP keys, SFTP, token_source MIGRATION_FILE; Yuno does not extract subscription data from the files) and a separate network token migration process (fields include network token number, FPAN, network token transaction ID, parent wallet type). docs.y.uno/docs/security-and-compliance/data-migration-processes. CONFIRMED.\n"
        "Source side: Spreedly export documented (self-service store or PGP/SFTP, one free export per destination). Recurly export of card data only to a PCI-compliant recipient through Recurly Professional Services; NTIDs migrated by the same team (recurly.com/glossary/data-migration). Yuno is PCI DSS Level 1, so it qualifies as the recipient; the Recurly export scope and timeline are OPEN until Recurly confirms them to Skydance.\n"
        "Export from Yuno: written request, recipient's PCI DSS AOC, PGP file over SFTP; the documented CSV has holder name, number, token, expiry; network tokens and NTIDs are not in the documented file (OPEN, Trust & Vault product and Legal)."),
    'nt': (
        "Docs: Yuno procures network tokens from Visa, Mastercard and American Express; provisioned for every vaulted card once enabled; statuses Created, Active, Suspended, Canceled; tokens updated when a card is reissued (docs.y.uno/docs/security-and-compliance/network-tokens). Cryptogram API: Visa and Mastercard. CONFIRMED, enabled per organization. Scheme activation is confirmed per network in writing before Phase 1.\n"
        "Token requestor ID: the API reference says Yuno holds the TRID; the vault page says tokens are registered in your name. Say \"dedicated TRID for Skydance where the scheme allows it\" and confirm the model with Trust & Vault product (OPEN). Never say \"in your name\".\n"
        "PAR is returned on the network token object (docs, PCI retrieve endpoint)."),
    'personal': (
        "Stored credentials page, read 22 Oct 2026: \"The network_transaction_id belongs to the card network, not to the provider that processed the first payment. Yuno stores it on the vaulted_token and sends it on every merchant-initiated payment, whichever provider your routing selects.\" Mastercard TLID: returned on the CIT response and required on MITs in addition to the trace ID; stored and replayed. TRANSACTION_TYPE routing condition distinguishes CIT, MIT and RECURRING. CONFIRMED.\n"
        "Subscriptions: Smart Retries up to six attempts, default, smart or custom schedule, stop on hard declines (docs.y.uno automation page). CONFIRMED.\n"
        "Imported NTIDs: the network token migration template carries the network token transaction ID; NTIDs for imported PAN-only cards are confirmed in the Phase 0 viability assessment (OPEN, Trust & Vault). The illustrative subscriber and values are fictional."),
    'design': (
        "Vault product page: \"Define your own tables and fields. Vault what your business needs to protect\" (y.uno/product/vault). The schema designer shown is illustrative; custom tables beyond cards, network tokens and bank details are OPEN with Trust & Vault product until shown live in Phase 0. Cards, network tokens, ACH and SEPA details are CONFIRMED in docs."),
    'proxy': (
        "PCI Proxy, BETA, enabled per organization; sandbox open (docs.y.uno/reference/pci-proxy/invoke-forward-proxy, changelog 11 Jul 2026). Resolves number, expiry, holder name, network token number and expiry, network_transaction_id, security code within its window. Provider tokens and cryptograms are not resolved. Request shown is illustrative; amount 1399 mirrors the Paramount+ Premium monthly price on paramountplus.com (read 22 Oct 2026).\n"
        "Recurly as a destination: Recurly is not in Yuno's connection catalog and Yuno is not a Recurly gateway. If Paramount+ keeps Recurly for a period, the vault runs beside it: cards captured once into Yuno and forwarded to Recurly's API through the proxy is possible only if Recurly's API accepts raw card data for Skydance's PCI level (OPEN, confirm with Recurly). Do not promise it on the slide."),
    'controls': (
        "Allowlist of exact HTTPS hosts, no any-host mode, append-only audit log; destination authentication MTLS or DLOCAL_HMAC, secrets write-only in KMS; no storage or logging of bodies; redaction of echoed card numbers; 1 MB bodies, 20 vaulted tokens per request, 30 s timeout configurable to 120 s. All BETA per docs.y.uno/docs/security-and-compliance/pci-proxy. Inbound proxy and custom code: not in docs, concede if asked."),
    'versus': (
        "VGS and Basis Theory cells: their public pages read 7 Oct 2026 (Samuel's verification) and 22 Oct 2026. Basis Theory network tokens page: \"We don't support bringing existing Network Tokens into the vault at the moment, but we can help you re-provision them.\" VGS pages describe issuing and managing network tokens; no import statement found, hence \"not stated\".\n"
        "Pricing, notes only: VGS \"Plans start at $1,000/month\"; Basis Theory \"$995 per month, includes 20,000 tokens\"; Spreedly \"Independent Vault, starting at $750 per month\"; Evervault $995/mo plus usage; TokenEx (IXOPAY) and Skyflow unpublished. All vendor pages, 22 Oct 2026.\n"
        "Spreedly is HBO Max's incumbent and does vaulting, network tokens, account updater and export well; it is not on this table and we do not position against it. The Yuno difference for the combined service is one vault for both stacks plus 460+ connections, routing, Smart Retries and 3DS on the same tokens.\n"
        "Yuno 3DS: own connection, Netcetera default, standalone mode returns ECI and CAVV for any acquirer (docs). CONFIRMED."),
    'port': (
        "Portability: vaulted tokens work across all processors connected to the account, no re-tokenization (docs.y.uno/docs/basic-concepts/tokens). Export: written request, recipient PCI DSS AOC, PGP file over SFTP, all exports logged (docs exporting-tokens page). CONFIRMED. Fee, timeline and NTID or network token export are not in docs: OPEN with Legal and Trust & Vault product, to be written into the MSA.\n"
        "Processor logos are examples of Yuno connections; Adyen and Checkout.com are already in HBO Max's stack, EBANX and dLocal are Recurly gateways, so a renewal can keep running on the processors each service uses today."),
}
