# -*- coding: utf-8 -*-
"""Yuno-side slides built from yuno_vault_facts.md, gap_register.md and vs_standalone_vault.md (Agent B, 8 Oct 2026).
Every Yuno claim here is CONFIRMED on docs.y.uno or y.uno, or marked OPEN with an owner."""

K_VAULT = "THE YUNO TOKEN VAULT"
K_VS = "VERSUS A STANDALONE VAULT"

SLIDES = {}

# ---------------------------------------------------------------- questions 2 of 2 (rows 8 to 15 from the gap register)
SLIDES["questions-2"] = {
    "id": "questions-2", "type": "checklist_table",
    "kicker": "WHAT THE VAULT HAS TO HOLD · THE QUESTIONS",
    "headline": "The questions a careful vault buyer asks first, answered before you ask (2 of 2).",
    "source": "Yuno answers from docs.y.uno and y.uno, read 8 October 2026. Open rows map to the open items on slide {{slide:owe}}.",
    "columns": ["#", "The question", "Our answer", "Basis"],
    "col_widths": [0.04, 0.28, 0.52, 0.16],
    "header_style": "dark", "font_size": 7, "bold_first_col": False, "zebra": True,
    "rows": [
        ["8", {"text": "What is in the export file, and what is not?", "bold": True}, "Cardholder name, card number, expiry and the Yuno token, as documented. Network transaction IDs and network tokens are not in the documented file; we scope them with you in writing.", {"text": "Trust & Vault product, Legal", "pill": "CONFIRMED", "pill2": "OPEN"}],
        ["9", {"text": "Who are your subprocessors, and are your card-network connections direct?", "bold": True}, "A subprocessor list and the connection model for each network come in writing with the RFP response.", {"text": "Security, Product", "pill": "OPEN"}],
        ["10", {"text": "What happens at checkout and at renewal time if the vault is unreachable?", "bold": True}, "Failover between the processors you connect is a routing feature (Monitors). Capture and recurring behaviour during a vault outage comes with the failover design, not asserted here.", {"text": "Engineering", "pill": "CONFIRMED", "pill2": "OPEN"}],
        ["11", {"text": "Do you capture the network transaction ID when we charge through the proxy on our own processor?", "bold": True}, "For payments Yuno processes, the ID is stored on the token and replayed on every merchant-initiated charge, whichever provider. Through the proxy the stored ID is injected into your request; capturing a new one from your processor's response is open.", {"text": "Beta · Product", "pill": "CONFIRMED", "pill2": "OPEN"}],
        ["12", {"text": "Does using the proxy change our SAQ?", "bold": True}, "Capture stays in our hosted fields and the proxy resolves data inside Yuno's PCI environment, so per our documentation your scope does not change. Sending a raw CVV yourself outside the 3-hour window keeps that request in your scope. Your QSA confirms your SAQ.", {"text": "", "pill": "CONFIRMED", "pill2": "BETA"}],
        ["13", {"text": "Can we vault bank accounts and other payment methods, not only cards?", "bold": True}, "Yes. ACH and SEPA details with a mandate record through the enroll API, with no provider involved if you choose; PayPal and several wallets are enrollable. Other methods confirmed per method in writing.", {"text": "Product", "pill": "CONFIRMED", "pill2": "OPEN"}],
        ["14", {"text": "Can we bring our own network tokens, or move existing ones in?", "bold": True}, "Yes. A documented import process for network tokens (file over SFTP, including the network transaction ID) and a passthrough mode for tokens you hold. Tokens under another requestor's ID are re-provisioned, as with any vendor.", {"text": "", "pill": "CONFIRMED"}],
        ["15", {"text": "Where does the data live, and which region do we integrate with?", "bold": True}, "Separate production environments for the US (api.y.uno) and EMEA (api.eu.y.uno), on AWS with AES-256 at rest per our trust page. Key management and regional detail come in the security pack with the RFP response.", {"text": "Engineering, Security", "pill": "CONFIRMED", "pill2": "OPEN"}],
    ],
    "notes": "These are the questions a vault RFP always contains and a sandbox cannot answer on its own. Three of them are open today and we say so: subprocessors and direct connections, behaviour during a vault outage, and capturing a new network transaction ID through the proxy. Each has an owner on the open items slide and a written answer in our RFP response. The rest can be read in our public documentation today, and we would rather you read it before we talk than after. Two more documented capabilities worth knowing for a US card base: Yuno 3DS Standalone returns ECI and CAVV so you can authenticate once and authorize on any acquirer, and the web SDK exposes the BIN in real time through the card.onChange callback, so you can act on card type before the payment is sent.",
}

# ---------------------------------------------------------------- keep current (network tokens + account updater)
SLIDES["keep-current"] = {
    "id": "keep-current", "type": "diagram",
    "kicker": K_VAULT + " · KEEP CURRENT",
    "headline": "Card on file does not have to break: network tokens and the account updater keep the vaulted token valid across reissues and processors.",
    "tag": ["CONFIRMED"],
    "source": "Source: docs.y.uno, Network tokens; Card account updater; Stored credentials. Read 8 October 2026.",
    "boxes": [
        {"id": "l1", "x": 0, "y": 0, "w": 420, "h": 18, "title": "LANE 1 · NETWORK TOKENS · PROVISIONED ONCE PER CARD", "body": "", "style": "label"},
        {"id": "enr", "x": 0, "y": 22, "w": 110, "h": 56, "title": "Card enrolled once", "body": "Hosted fields, no charge", "style": "outline"},
        {"id": "vault1", "x": 136, "y": 22, "w": 150, "h": 56, "title": "Yuno vault", "body": "PAN stays here. Network token provisioned for enrolled cards (Visa, Mastercard, American Express per docs), updated when the card is renewed or reissued", "style": "blue"},
        {"id": "psp", "x": 312, "y": 22, "w": 108, "h": 56, "title": "Any processor you connect", "body": "Token plus cryptogram (Visa, Mastercard). The network transaction ID is stored on the token and sent on every merchant-initiated charge, whichever provider is used", "style": "light"},
        {"id": "l2", "x": 0, "y": 100, "w": 420, "h": 18, "title": "LANE 2 · ACCOUNT UPDATER · ASYNCHRONOUS, VISA AND MASTERCARD", "body": "", "style": "label"},
        {"id": "old", "x": 0, "y": 122, "w": 110, "h": 56, "title": "Stored •••• 0193", "body": "exp 09/26, past expiry or account closed, disabled or flagged", "style": "outline"},
        {"id": "vault2", "x": 136, "y": 122, "w": 150, "h": 56, "title": "Yuno asks the networks", "body": "Independently of the payment flow. Webhook enrollment.update carries the new expiry, last four and reason", "style": "blue"},
        {"id": "new", "x": 312, "y": 122, "w": 108, "h": 56, "title": "Updated •••• 7740", "body": "exp 09/29. The vaulted token and fingerprint stay the same, so nothing changes on your side", "style": "light"},
    ],
    "connectors": [{"from": "enr", "to": "vault1"}, {"from": "vault1", "to": "psp"}, {"from": "old", "to": "vault2"}, {"from": "vault2", "to": "new"}],
    "side": {"header": "WHAT YOU GET", "items": [
        {"title": "Fewer involuntary losses", "body": "Reissued and renewed cards keep renewing without the fan re-entering a card."},
        {"title": "One credential chain", "body": "The same stored credential and network transaction ID work on every processor you connect, so recurring survives a processor change."},
        {"title": "Per-card control", "body": "Opt a card out of the updater; duplicate enrollments of one PAN map to one network token through the fingerprint."},
    ]},
    "notes": "Two mechanisms keep a stored card valid. Network tokens are provisioned once for enrolled cards and updated by the network when the card is renewed or reissued; cryptograms are generated for Visa and Mastercard. The account updater works asynchronously for Visa and Mastercard: when a card is past expiry or the account has changed, Yuno asks the network and the vaulted token stays the same, so nothing changes in your systems. The network transaction ID belongs to the card network, not to the processor, and Yuno stores it on the token and sends it on every merchant-initiated charge whichever provider is used. Scheme activation is confirmed per network in writing before Phase 1; American Express is in our documentation and we will confirm its activation for your organization explicitly rather than assume it. Account updater for American Express and Discover is not in our documentation today.",
}

# ---------------------------------------------------------------- move (import in, export out)
SLIDES["move"] = {
    "id": "move", "type": "cards_row",
    "kicker": K_VAULT + " · MOVE",
    "headline": "Import your existing cards and network tokens in, and read the export process before you sign anything.",
    "source": "Source: docs.y.uno, Token migration process; Network token migration process; Exporting tokens from Yuno. Read 8 October 2026.",
    "cards": [
        {"pill": "CONFIRMED", "eyebrow": "IMPORT · CARDS", "title": "From your current gateway or vault", "body": "Your provider exports; Yuno and the provider exchange the file with PGP keys over SFTP; you map old tokens to vaulted tokens through the API. Mandatory fields: cardholder name, expiry, card number and the provider's card ID. It starts with a viability assessment."},
        {"pill": "CONFIRMED", "eyebrow": "IMPORT · NETWORK TOKENS", "title": "A separate documented process", "body": "The file includes the network token number, the card's last digits, the network transaction ID and the parent wallet type (Apple Pay, Google Pay), one file per parent type. Tokens under another requestor's ID are re-provisioned, as with any vendor."},
        {"pill": "CONFIRMED", "pill2": "OPEN", "eyebrow": "EXPORT · YOUR EXIT", "title": "Written request, encrypted file", "body": "Four written items, the recipient's current PCI DSS attestation, a PGP key from the recipient, a Yuno-hosted SFTP. The documented file holds cardholder name, card number, token and expiry. Network transaction IDs and network tokens are not in it today: open item 4."},
    ],
    "side": {"header": "WHAT YOU GET", "items": [
        {"title": "No re-collection", "body": "Fans do not re-enter cards when the vault changes."},
        {"title": "A public exit", "body": "The export process and the file contents are published, so you can check what you would take with you before signing."},
        {"title": "Every export logged", "body": "All exports are logged and monitored, per our documentation."},
    ]},
    "notes": "Migration in both directions is documented publicly. Cards come in through a PGP-encrypted file over SFTP and are mapped to vaulted tokens through the API; a second process imports network tokens with their network transaction IDs and wallet parent type. The export process is public too: a written request, the recipient's PCI DSS attestation, and an encrypted file to a Yuno-hosted SFTP. We would rather you notice now that the documented export file does not include network transaction IDs or network tokens; that is open item 4 and we will scope it with you in writing.",
}

# ---------------------------------------------------------------- compliance (native table replacing the template's compliance slide)
SLIDES["compliance"] = {
    "id": "compliance", "type": "table",
    "kicker": "WHY YUNO · SECURITY AND COMPLIANCE",
    "headline": "Yuno meets the security, privacy and resilience requirements that regulated institutions and vault buyers test for.",
    "source": "Source: y.uno vault and trust pages, y.uno/sla (last update 24 October 2025), status.y.uno, docs.y.uno API environments. Read 8 October 2026. Reports and attestations through our security team.",
    "columns": ["Risk dimension", "What a vault buyer asks", "How Yuno answers it", "Basis"],
    "col_widths": [0.16, 0.24, 0.46, 0.14],
    "header_style": "dark", "font_size": 7.2, "bold_first_col": True, "zebra": True,
    "rows": [
        ["Data security", "Protection of card data across processors", "Card numbers stay in a PCI DSS Level 1 vault; tokens replace them everywhere else. AES-256 at rest and TLS 1.3 in transit per our trust page. The CVV is never stored.", {"text": "PCI DSS v4.0", "pill": "CONFIRMED"}],
        ["Information security management", "Vendor maturity; passing your vendor audit", "ISO 27001 certified and SOC 2 Type 2, with external penetration tests and a HackerOne bug bounty per our trust page. Attestations and reports on request.", {"text": "", "pill": "CONFIRMED"}],
        ["Privacy and data location", "Personal data handling; where data is processed", "ISO 27701 and GDPR. Separate production environments for the US (api.y.uno) and EMEA (api.eu.y.uno); accounts are not synchronized between regions. Key management and regional detail in the security pack.", {"text": "Engineering, Security", "pill": "CONFIRMED", "pill2": "OPEN"}],
        ["Operational resilience", "Availability, incident response, failover", "Published SLA: 99.90% monthly availability, critical incidents answered within 5 minutes, service credits by availability band. Public status page with incident history. Provider-level failover through Monitors. Vault-outage design: open item 5.", {"text": "Engineering", "pill": "CONFIRMED", "pill2": "OPEN"}],
        ["Regulatory and licensing", "Who holds the funds; who is the regulated party", "Yuno is a technology provider and does not hold your funds; settlement runs between your processors, banks and you. Recognized as a Visa Service Provider.", {"text": "", "pill": "CONFIRMED"}],
        ["Vendor lock-in", "Portability of credentials and data", "Documented card export to any PCI DSS certified recipient, and a documented network token import. What the export file contains is public; network transaction ID export is open item 4.", {"text": "Trust & Vault product, Legal", "pill": "CONFIRMED", "pill2": "OPEN"}],
    ],
    "notes": "The compliance posture as published on our own pages, with the two places where we still owe you detail marked open. Certifications: PCI DSS Level 1 on version 4.0, SOC 2 Type 2, ISO 27001, ISO 27701 and Visa Service Provider registration. Our published SLA commits to 99.90% monthly availability with a 5-minute response on critical incidents; the figure that binds is the one in your contract. We hold no funds and are not the regulated party in your flows. Ask our security team for the attestation documents and their scope.",
}

# ---------------------------------------------------------------- credentials (published success stories only)
SLIDES["credentials"] = {
    "id": "credentials", "type": "cards_row",
    "kicker": "APPENDIX · SELECTED CREDENTIALS",
    "headline": "Published results from merchants that run cards, recovery and multi-provider resilience on Yuno.",
    "source": "Source: y.uno success stories and y.uno home page, read 8 October 2026. Figures as published; no others are quoted.",
    "cards": [
        {"eyebrow": "INDRIVE · MOBILITY", "title": "90% payment approval rate", "body": "Expanded into new countries within eight months on one integration."},
        {"eyebrow": "RAPPI · DELIVERY", "title": "New provider implementation time cut to zero", "body": "Payment issue response time reduced from minutes to seconds with Monitors."},
        {"eyebrow": "LIVELO · LOYALTY", "title": "50% of failed transactions recovered", "body": "5% increase in payment approval rates through Smart Routing."},
        {"eyebrow": "MCDONALD'S · ARCOS DORADOS", "title": "Tokenized payments across 21 LATAM markets", "body": "Payments unified on one layer across the region."},
    ],
    "bar": "**Yuno published figures.** Up to 7% uplift in approval rates and 30% recovered revenue, as stated on y.uno.",
    "notes": "Appendix. Four published stories, quoted as they appear on our site. inDrive reached a 90% approval rate and expanded into new countries within eight months. Rappi cut new provider implementation time to zero and handles payment anomalies with Monitors. Livelo recovered half of its failed transactions and lifted approvals by five points through Smart Routing. McDonald's, through Arcos Dorados, unified and tokenized payments across 21 markets. The Yuno-wide figures we quote are the published ones: up to 7% approval uplift and 30% recovered revenue.",
}

# ---------------------------------------------------------------- versus model grid (one project instead of two)
SLIDES["versus-model"] = {
    "id": "versus-model", "type": "comparison_grid",
    "kicker": K_VS + " · THE MODEL",
    "headline": "One project instead of two: what stays on your roadmap with a standalone vault, with an orchestrator on top, and with Yuno.",
    "quote": "\"VGS powers orchestration, but does not act as the orchestrator.\" verygoodsecurity.com · Basis Theory's vault \"operates independently of any payment processor or orchestration layer.\" 14 October 2025",
    "legend": ["Stays on your roadmap", "Partly covered", "Covered"],
    "options": [
        {"header": "OPTION A", "sub": "Standalone vault, the rest built in-house"},
        {"header": "OPTION B", "sub": "Standalone vault, plus an orchestrator on top"},
        {"header": "OPTION C · YUNO", "sub": "Vault and the layer above it, one platform"},
    ],
    "rows": [
        {"label": "PCI DSS Level 1 card vault", "sub": "Hosted capture, tokens, export", "cells": [
            {"state": "closed", "text": "Both vaults run a Level 1 vault with hosted capture."},
            {"state": "closed", "text": "Covered by the vault vendor."},
            {"state": "closed", "text": "SDK enrollment into a Level 1 vault, documented export."}]},
        {"label": "Rules for where each request goes", "sub": "Bank, issuer or processor per creator", "cells": [
            {"state": "open", "text": "Yours to write and maintain. VGS: \"does not make routing decisions for you.\""},
            {"state": "partial", "text": "The partner's rules for cards. Bank and issuer allocation depends on the partner."},
            {"state": "partial", "text": "Cards: rules, splits, fallbacks, Monitors today. Banks: per call today; by rule is open item 2."}]},
        {"label": "Provider connections, built and maintained", "sub": "PSPs, acquirers, banks, issuers", "cells": [
            {"state": "open", "text": "Every provider call is a proxy request your engineers write and maintain."},
            {"state": "partial", "text": "Processors via the partner; banks and issuers still via your own proxy requests."},
            {"state": "partial", "text": "460+ processor integrations maintained by Yuno. US banks and issuers: open item 3."}]},
        {"label": "Bank accounts and transfers by API", "sub": "Entities, onboarding, accounts, ACH, wire, RTP", "cells": [
            {"state": "open", "text": "No accounts or transfers API found at either vault; bank details stored and forwarded."},
            {"state": "open", "text": "Outside a payments orchestrator's scope."},
            {"state": "closed", "text": "Banking Connectivity API: entities, onboarding, accounts, transfers, per connection."}]},
        {"label": "Payouts and split payments", "sub": "Creator disbursement across rails", "cells": [
            {"state": "open", "text": "Via partners such as TabaPay or Astra, or not offered."},
            {"state": "partial", "text": "Depends on the partner's payout coverage."},
            {"state": "closed", "text": "Payouts API and split payments on the same platform."}]},
        {"label": "Vendors, contracts and incident ownership", "sub": "Who you call when a creator cannot be paid", "cells": [
            {"state": "open", "text": "One vendor for storage; your team for everything above it."},
            {"state": "partial", "text": "Two vendors, two contracts, two support desks, one incident."},
            {"state": "closed", "text": "One vendor, one contract, one support line, published SLA (P1 response within 5 minutes)."}]},
    ],
    "footer": [{"label": "Covered", "value": "1 of 6"}, {"label": "Covered or partly", "value": "4 of 6"}, {"label": "Covered or partly", "value": "6 of 6"}],
    "closing_line": "Option A keeps the vault narrow and the roadmap long. Option B closes part of it with a second vendor. Option C covers all six on one platform, with two cells marked partly covered on purpose and listed as open items with owners.",
    "source": "Vendor lines from public pages read 7 and 8 October 2026; Yuno lines from docs.y.uno and y.uno/sla. States are our reading; please confirm with each vendor.",
    "notes": "This is the same comparison from the point of view of your roadmap rather than feature by feature. With a standalone vault alone, the rules, the connections, the accounts and the payouts are yours to build. Adding an orchestrator on top closes part of that with a second vendor and a second contract. Yuno covers all six rows on one platform. Two of our cells are marked partly covered on purpose: rule-based allocation across banks and issuers, and the US banking and issuing providers behind the API. Both are open items with owners and come back in writing with the RFP response. Both vendors are good at what they say they do, and both are Yuno partners; the quotes are theirs, and we would ask you to confirm each one with them.",
}
