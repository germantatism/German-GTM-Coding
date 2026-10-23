# -*- coding: utf-8 -*-
"""Copy for the Poshmark token vault deck (23 Oct 2026). Merchant claims trace to ../research/*.md (public pages and the
poshmark.com web bundle); Yuno claims to Deals/OnlyFans/build/yuno_vault_facts.md (docs.y.uno, read 8 and 22 Oct 2026).
Internal context (Gong call of 1 Apr 2026, Samuel's emails) is in CONTEXT.md and reaches speaker notes only."""

LOGO_URL = 'https://drive.google.com/uc?export=download&id=100NWHPLE6VHGXcqy0m0viY5CO-n7oAcf'   # poshmark_white_wordmark.png, 648x87, uploaded 23 Oct 2026, anyone-reader

COVER = {
    'title': 'The Poshmark Yuno Vault',
    'sub': 'One vault across Braintree and Adyen. Your tokens, your exit.',
    'prep': 'Prepared for Poshmark · October 2026 · Strictly confidential',
}

EXEC = {  # slide of_exec_understanding_v2, element id -> new text (styles kept)
    'of_es1_v2_003': 'Poshmark needs one vault that Braintree, Adyen and any future processor can use, under its own rules',
    'of_es1_v2_008': 'What Poshmark aims to deliver',
    'of_es1_v2_009': '**Every saved card, wallet token and network token in one place**, usable by any processor in the US and Canada, with the network tokens and account updater you run today kept intact.',
    'of_es1_v2_011': 'What makes this challenging',
    'of_es1_v2_012': 'Buyer cards sit in two processor vaults, Braintree and Adyen, split by country, channel and the date the card was saved. **Every processor change has meant moving stored cards again**, and every vault has to be secured and audited.',
    'of_es1_v2_014': 'The decision now',
    'of_es1_v2_015': 'Poshmark is choosing where buyer credentials will live through its next processor decisions. That choice decides **who holds every token** and how freely Poshmark can add, swap or leave processors.',
    'of_es1_v2_026': 'What we propose\nOne PCI DSS Level 1 Yuno Vault for cards, network tokens, wallet tokens and seller payout details, a proxy that sends each value only to the processor that needs it, and portable tokens with the exit in the contract. The sandbox is open now.',
}

PROBLEM = {
    'kicker': 'THE VAULT  ›  THE PROBLEM',
    'title': 'Buyer cards live in two processor vaults, split by country, channel and date saved',
    'before_h': 'Two processors, two vaults',
    'stacks': [
        ('Braintree', 'PayPal vault and gateway', ['Cards and wallets, US web', 'PayPal and Venmo', 'Promoted Posts account']),
        ('Adyen', 'Adyen vault and acquiring', ['Cards and wallets, Canada', 'New tokens since Mar 2022', 'Apple Pay merchant ID']),
    ],
    'before_x': ["A buyer's card can only be charged by the processor that stored it", 'A processor switch means a migration of every stored card', 'Two vaults to secure, audit and keep in sync'],
    'before_src': 'poshmark.com web bundle: Braintree and Adyen merchant IDs for the US and Canada; "adyen_switch_new_payment_tokens" enabled 9 Mar 2022; paylution.com (Hyperwallet) allowlisted. Read 23 Oct 2026.',
    'after_h': 'One vault',
    'swappable': ['Processors', 'Payout providers', 'Fraud and 3DS'],
    'vault_pills': ['Cards', 'Network tokens', 'Wallet tokens', 'Bank details'],
    'after_ok': ['Cards work on Braintree, Adyen or any processor you connect', 'One vault to secure and audit', 'Imported from both vaults, no buyer re-enters a card'],
}

M5 = {  # slide m5_mock
    'm5_hl': 'What Poshmark needs',
    'm5_bd0': 'Cards, network tokens, wallet tokens and seller bank details in one vault',
    'm5_ad2': 'Routing, retries, failover and payouts, built in-house',
    'm5_bd2': 'Routing, retries, failover and payouts on rules you set',
    'm5_bd3': '3DS, account updater, network tokens and payouts on the same tokens',
    'm5_band': 'Same independence, far less to build.   Poshmark keeps portable tokens and exit terms, and decides how much of the stack Yuno runs.',
}

CARDS = {  # slide vlt_cards
    'vlt_cards__9_244': 'Buyer cards are stored once and work on every processor you connect',
    'vlt_cards_k038': 'Each processor exports',
    'vlt_cards_k047': 'buyers untouched',
    'vlt_cards_k050': 'Import from Braintree and Adyen as PGP-encrypted files over SFTP, network tokens included. Export is documented.',
    'vlt_cards_k052': '**One vaulted token, every processor.** Add or swap a processor and the stored cards keep working, with nothing collected again from buyers.',
}

NT = {  # slide h7c266de662ba1cf0_9_207
    'h7c266de662ba1cf0_9_210': 'Network tokens and PAR sit next to the card, so one buyer stays one buyer\x0bacross every credential',
    'h7c266de662ba1cf0_9_235': 'One buyer across card, wallet and reissue: for offers, disputes\x0band fraud rules.',
    'h7c266de662ba1cf0_9_236': 'Token requestor ID registered under Poshmark where the scheme\nallows it. Yuno acts as TS-TRP.',
}

OFFER = {  # slide vlt_personal, body redrawn
    'kicker': 'THE VAULT  ›  OFFERS AND SHOWS',
    'title': 'A saved card is charged when the seller accepts, on any processor',
    'initials': 'ML', 'name': 'Maria Lopez', 'ref': 'buyer_4471',
    'col3': 'WHEN CHARGED',
    'rows': [  # field, stored as, when charged, pill kind
        ('Card PAN', '•••• 0193', 'Tokenized', 'blue'),
        ('Network token', '•••• 7740', 'Tokenized', 'blue'),
        ('Apple Pay token', '•••• 2215', 'Tokenized', 'blue'),
        ('Network transaction ID', '3812•••••••2210', 'Sent with the charge', 'lav'),
        ('PAR', '5001•••••••••', 'One buyer', 'lav'),
        ('Expiry', '09 / 29', 'Account updater', 'lav'),
    ],
    'foot': 'Captured when the buyer saves a card, bids in a show or makes an offer. Reused from the vault when the seller accepts.',
    'right': [
        ("Offer accepted on today's processor", 'The stored card, its network token and transaction ID travel with the charge, whichever account you route to.'),
        ('Offer accepted after a processor switch', "Same token, same reference, translated into the new provider's format. The buyer does nothing."),
        ('Charge after a card reissue', 'The account updater refreshes the PAN. Token, transaction ID and PAR stay the same.'),
    ],
    'quote': 'docs.y.uno: "The network_transaction_id belongs to the card network, not to the provider that processed the first payment." Read 23 Oct 2026.',
}

DESIGN = {  # slide h7c266de662ba1cf0_9_241 (table mockup): buyers table plus seller payout methods
    'h7c266de662ba1cf0_9_250': 'buyers',
    'h7c266de662ba1cf0_9_251': 'PII',
    'h7c266de662ba1cf0_9_261': 'payout_methods',
    'h7c266de662ba1cf0_9_265': 'payout_methods',
    'h7c266de662ba1cf0_9_306': 'tax_id',
    'h7c266de662ba1cf0_9_308': 'PII',
    'h7c266de662ba1cf0_9_309': 'Tokenized',
    'h7c266de662ba1cf0_9_310': '7 years',
}

PROXY = {  # slide h7c266de662ba1cf0_9_391
    'h7c266de662ba1cf0_9_398': 'Poshmark system',
    'h7c266de662ba1cf0_9_409': 'As Poshmark sends it',
}
PROXY_AMOUNT = '2800'

CONTROLS = {  # slide vlt_controls
    'vlt_controls_k003': 'Poshmark system',
    'vlt_controls_k036': 'Payout providers',
    'vlt_controls_k037': '3DS providers',
    'vlt_controls_k038': 'Bank validation and tax',
}

VERSUS = {  # slide vlt_versus
    'vlt_versus__9_244': 'Yuno matches standalone vaults on the core and leads on what a marketplace runs on',
    'vlt_versus_k019': 'Visa, Mastercard, Amex; TRID under Poshmark',
    # row 5 (issued card / PIN) becomes "Import existing network tokens"
    'vlt_versus_k029': 'Import existing network tokens',
    'vlt_versus_k030': 'Documented import process',
    'vlt_versus_k031': 'Not stated on public pages',
    'vlt_versus_k032': 'Re-provisioned, not imported',
    'vlt_versus_k033': 'Yuno leads',
    # row 9 stays payouts (marketplace)
    'vlt_versus_k057': 'Yuno leads on 5, level on 2, the standalone vaults lead on 2. VGS and Basis Theory: their public pages, read 7 and 22 October 2026.',
}
VERSUS_COLORS = {'vlt_versus_k033': '#3E4FE0'}  # row 5 verdict turns blue (Yuno leads)

PORT = {  # slide h7c266de662ba1cf0_9_469
    'h7c266de662ba1cf0_9_507': "Registered under Poshmark's token requestor ID\nwhere the scheme allows it, so they survive a\nchange of processor or of vault. No\nre-tokenization on exit.",
    'h7c266de662ba1cf0_9_511': 'A written request from Poshmark',
}

NOTES = {
    'exec': (
        "Labels: CONFIRMED = docs.y.uno or y.uno; BETA = depends on the PCI Proxy (beta, enabled per organization); PUBLIC = Poshmark's own pages or web bundle; OPEN = not confirmed in writing, owner named.\n"
        "Two processors: PUBLIC. The poshmark.com web bundle (read 23 Oct 2026) carries Braintree merchant IDs (poshmark_BT, Poshmark_CADUSD5931) and Adyen merchant IDs (APM_USDUSD5931, APM_CADCAD5931) for the US and Canada, an Apple Pay merchant ID under each, and the flag adyen_switch_new_payment_tokens enabled on 9 Mar 2022. The US web checkout config lists cards, Apple Pay, Google Pay, PayPal and Venmo on Braintree and Affirm direct; the Canada config lists cards and wallets on Adyen and PayPal on Braintree.\n"
        "What Adam told us (1 Apr 2026 demo, internal): cards are 'bolted at both locations', a 40-million-record vault migration from Braintree to Adyen had just been completed, Hyperwallet is payouts only, network tokens and an account updater are live, approval rate at an all-time high of 94.99% that week, a payments microservice launching in May, no engineering capacity until H2 2026, a slim team running payments that needs efficiencies and economics. Use as 'as you shared with us', never as a slide fact.\n"
        "Samuel's 6 Oct 2026 email already framed the standalone vault as one PCI DSS Level 1 vault across Braintree and Adyen with the sandbox open; this deck is the long form of that email.\n"
        "What we propose: vault, network tokens, proxy and export are CONFIRMED/BETA per the fact base; 'exit in the contract' means the documented export process plus commercial terms agreed in the MSA (OPEN, Legal)."),
    'problem': (
        "Factual, not critical. Braintree and Adyen both vault cards well and both run network tokens and account updaters; the point is that each one holds the cards it captured and a buyer's card can only be charged by the processor that stores it. Moving between them is a file migration (as Poshmark did from Braintree to Adyen), and the next processor decision would mean another one.\n"
        "Evidence lines: web bundle flags braintree_mid__us, braintree_mid__ca, adyen_mid__us, adyen_mid__ca, adyen_switch_new_payment_tokens__ca (enabled 2022-03-09), migration_payment_methods__ca, payment_methods__us and __ca; CSP allowlists *.braintreegateway.com, *.adyen.com, *.paypal.com, *.affirm.com, cdn.siftscience.com, *.paylution.com (Hyperwallet). See research/poshmark_live_site_2026-10-23.md.\n"
        "Promoted Posts: a second merchant ID per processor (Poshmark_USD7311, APM_USDUSD7311) bills seller advertising. Those cards are the same credentials and would live in the same vault.\n"
        "3DS: threeds2_enabled is false on both Adyen accounts in the web bundle; Yuno 3DS (Netcetera default, standalone mode returns ECI and CAVV for any acquirer) is available on the same tokens if Poshmark ever needs it (CONFIRMED).\n"
        "Do not quote the demo call or Samuel's emails in the room beyond 'as you shared with us'."),
    'm5': (
        "Standalone vault column = VGS and Basis Theory public pages (7 and 22 Oct 2026). Yuno column: PCI DSS Level 1, SOC 2 Type 2, ISO 27001, ISO 27701, Visa Service Provider (y.uno/product/vault); 460+ processor integrations (same page); routing, Monitors, Smart Retries (docs.y.uno automation page); account updater Visa and Mastercard (docs); network tokens Visa, Mastercard, Amex per docs, activation per scheme confirmed in writing before Phase 1 (OPEN, Trust & Vault).\n"
        "Wallet tokens: Apple Pay and Google Pay payments with vault_on_success store a hidden vaulted token (docs, enrollment page). Apple Pay merchant token storage is not in docs; do not promise it.\n"
        "Seller bank details: ACH enrollment with vault_only stores beneficiary name, routing number, account number and type without provider interaction (docs, enroll API). CONFIRMED. Payouts to a vaulted token or card are documented with the US in the country list; whether Hyperwallet is kept as the payout rail or replaced is Poshmark's call and not part of this proposal.\n"
        "Braintree and Adyen are both Yuno connections (Braintree appears in the unreferenced-refund provider list; Adyen throughout docs). CONFIRMED."),
    'cards': (
        "Store: SDKs for Web, iOS, Android, Flutter, React Native; Secure Fields; most SDK merchants qualify for SAQ A, your QSA confirms (docs.y.uno/docs/security-and-compliance/pci-compliance). CONFIRMED.\n"
        "Keep: Card Account Updater, Visa and Mastercard, asynchronous; vaulted_token and fingerprint stay the same; registration up to 100 tokens per request; scheme registration up to 10 working days (docs.y.uno/docs/additional-services/card-account-updater). CONFIRMED. Amex and Discover updater: not in docs.\n"
        "Move: token migration process (PGP keys, SFTP, token_source MIGRATION_FILE; viability assessment first) and a separate network token migration process (fields include network token number, FPAN, network token transaction ID, parent wallet type). docs.y.uno/docs/security-and-compliance/data-migration-processes. CONFIRMED.\n"
        "Source side: Braintree and Adyen both export vaulted cards to a PCI DSS compliant recipient on the merchant's request (Braintree 'vault migration' and Adyen 'migrating payment details' are documented on their sites; scope, format and timeline are OPEN until each processor confirms them to Poshmark). Tokens provisioned under a processor's token requestor ID are re-provisioned rather than imported (OPEN, Trust & Vault, Phase 0 viability assessment).\n"
        "Export from Yuno: written request, recipient's PCI DSS AOC, PGP file over SFTP; the documented CSV has holder name, number, token, expiry; network tokens and NTIDs are not in the documented file (OPEN, Trust & Vault product and Legal)."),
    'nt': (
        "Docs: Yuno procures network tokens from Visa, Mastercard and American Express; provisioned for every vaulted card once enabled; statuses Created, Active, Suspended, Canceled; tokens updated when a card is reissued (docs.y.uno/docs/security-and-compliance/network-tokens). Cryptogram API: Visa and Mastercard. CONFIRMED, enabled per organization. Scheme activation is confirmed per network in writing before Phase 1.\n"
        "Token requestor ID: the API reference says Yuno holds the TRID; the vault page says tokens are registered in your name. Say 'dedicated TRID for Poshmark where the scheme allows it' and confirm the model with Trust & Vault product (OPEN). Never say 'in your name'.\n"
        "PAR is returned on the network token object (docs, PCI retrieve endpoint). For a marketplace, PAR is the stable key to tie a buyer's card, Apple Pay token and reissued card to one person for Posh Protect disputes and Sift rules."),
    'personal': (
        "Stored credentials page, read 23 Oct 2026: 'The network_transaction_id belongs to the card network, not to the provider that processed the first payment. Yuno stores it on the vaulted_token and sends it on every merchant-initiated payment, whichever provider your routing selects.' Mastercard TLID stored and replayed. TRANSACTION_TYPE routing condition distinguishes CIT, MIT and RECURRING. CONFIRMED.\n"
        "Poshmark flows where a saved credential is charged later: Offers (the buyer's payment method is charged when the seller accepts, per Poshmark's offer pages), Offer to Likers, Bundles and Posh Shows auctions (a winning bid is charged to the saved method). Quote the support wording from research/poshmark_payments_2026-10-23.md if asked; whether Poshmark authorizes at offer time or charges on acceptance is Poshmark's implementation detail, not asserted on the slide.\n"
        "Imported NTIDs: the network token migration template carries the network token transaction ID; NTIDs for imported PAN-only cards are confirmed in the Phase 0 viability assessment (OPEN, Trust & Vault). The illustrative buyer and values are fictional."),
    'design': (
        "Vault product page: 'Define your own tables and fields. Vault what your business needs to protect' (y.uno/product/vault). The schema designer shown is illustrative; custom tables beyond cards, network tokens and bank details are OPEN with Trust & Vault product until shown live in Phase 0. Cards, network tokens, ACH and SEPA details are CONFIRMED in docs.\n"
        "payout_methods mirrors what Poshmark collects for redemptions today: direct deposit bank details (bank validation flag on), the Instant Transfer debit card, PayPal and Venmo handles, and the seller tax ID collected in-app for 1099-K reporting (web bundle flags redemptions_bank_validation__us, app_seller_tax_info__us). Which of these Poshmark moves into the vault is a design choice."),
    'proxy': (
        "PCI Proxy, BETA, enabled per organization; sandbox open (docs.y.uno/reference/pci-proxy/invoke-forward-proxy, changelog 11 Jul 2026). Resolves number, expiry, holder name, network token number and expiry, network_transaction_id, security code within its window. Provider tokens and cryptograms are not resolved. Request shown is illustrative; amount 2800 is a fictional $28.00 order.\n"
        "Braintree and Adyen both accept raw card data on their server APIs for PCI-compliant callers, which is what the proxy supplies; Poshmark's own scope does not change because the number never touches its systems (docs, proxy overview). Through the proxy Poshmark keeps its own Braintree and Adyen integrations and routing logic; through Yuno's connections it can also route the same token without building the request."),
    'controls': (
        "Allowlist of exact HTTPS hosts, no any-host mode, append-only audit log; destination authentication MTLS or DLOCAL_HMAC, secrets write-only in KMS; no storage or logging of bodies; redaction of echoed card numbers; 1 MB bodies, 20 vaulted tokens per request, 30 s timeout configurable to 120 s. All BETA per docs.y.uno/docs/security-and-compliance/pci-proxy. Inbound proxy and custom code: not in docs, concede if asked.\n"
        "Destinations for Poshmark: Braintree and Adyen APIs, Hyperwallet or any payout provider, a 3DS server, bank validation and tax services, Sift. Fraud data sent to Sift today (hashed card data, BIN) can keep flowing from the proxy response fields."),
    'versus': (
        "VGS and Basis Theory cells: their public pages read 7 Oct 2026 (Samuel's verification) and 22 Oct 2026. Basis Theory network tokens page: 'We don't support bringing existing Network Tokens into the vault at the moment, but we can help you re-provision them.' VGS pages describe issuing and managing network tokens; no import statement found, hence 'not stated'.\n"
        "Pricing, notes only: VGS 'Plans start at $1,000/month'; Basis Theory '$995 per month, includes 20,000 tokens'; Spreedly 'Independent Vault, starting at $750 per month'; Evervault $995/mo plus usage; TokenEx (IXOPAY) and Skyflow unpublished. All vendor pages, 22 Oct 2026.\n"
        "Payouts row: Yuno payouts to bank, card or wallet with the US in the documented country list and PAYPAL_PAYOUT and CARD among withdrawal types; split payments for marketplaces documented. Basis Theory has no payouts product; VGS routes through partners. Yuno leads.\n"
        "Yuno 3DS: own connection, Netcetera default, standalone mode returns ECI and CAVV for any acquirer (docs). CONFIRMED."),
    'port': (
        "Portability: vaulted tokens work across all processors connected to the account, no re-tokenization (docs.y.uno/docs/basic-concepts/tokens). Export: written request, recipient PCI DSS AOC, PGP file over SFTP, all exports logged (docs exporting-tokens page). CONFIRMED. Fee, timeline and NTID or network token export are not in docs: OPEN with Legal and Trust & Vault product, to be written into the MSA.\n"
        "Processor logos are examples of Yuno connections; Adyen and PayPal (Braintree) are already in Poshmark's stack, so a charge can keep running on the accounts Poshmark uses today while the cards live in one vault."),
}
