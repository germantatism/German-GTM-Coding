# -*- coding: utf-8 -*-
"""Sections 01 to 04: slides built from ledger_onlyfans.md and storyline_inputs_A.md (Agent A, 8 Oct 2026)
and from OnlyFans' own stated design. Every number cites a ledger row (C, P, V, I, B); nothing from the
"Unverified" section is on a slide. No em-dashes, no spaced hyphens, USD only."""

K03 = "HOW ONLYFANS RUNS PAYMENTS TODAY"
K02 = "INDUSTRY CONTEXT"
K04 = "WHAT THE VAULT HAS TO HOLD"

SLIDES = {}

# ---------------------------------------------------------------- 01 executive summary
SLIDES["exec"] = {
    "id": "exec", "type": "exec_summary",
    "kicker": "WHY WE ARE HERE · EXECUTIVE SUMMARY",
    "headline": "Executive summary",
    "left_header": "WHERE ONLYFANS STANDS TODAY",
    "left_items": [
        {"title": "A payout business at scale, run lean", "body": "FY2025 accounts filed 20 September 2026: $1.55B net revenue, $6.3B paid to creators in the year, more than $30B since 2016, 47 employees. Anything added underneath must run by configuration, not headcount."},
        {"title": "An RFP for a token vault, with a bigger design behind it", "body": "One creator account on top. Two to five banks, pluggable card issuers and bank-transfer providers underneath, so no single partner can cut a creator off. US balances first, banking as a service next, stablecoin yield on balances."},
        {"title": "The question you asked most", "body": "Who decides which bank, issuer and rail each creator lands on. The answer in this deck: OnlyFans does. The mechanism is shown in writing, with what exists today and what is open."},
        {"title": "A vault alone stores the credential", "body": "Your design also needs the rules, the provider connections, the accounts and the money movement above it. With a standalone vault, all of that stays on your roadmap."},
    ],
    "right_header": "WHAT ONLYFANS GETS WITH YUNO",
    "right_cards": [
        {"title": "A PCI DSS LEVEL 1 VAULT WITH A PUBLIC EXIT", "body": "One vaulted token that works on every processor you connect, network tokens and account updater to keep it current, documented import and export."},
        {"title": "A PROXY TO ANY DESTINATION YOU CHOOSE", "body": "Stored card data forwarded to providers Yuno does not orchestrate, including issuers and your own acquiring connections, behind an allowlist, mutual TLS and audit logs."},
        {"title": "THE DECISION LAYER, WITH YOUR RULES", "body": "Per call for banking today, by rule for card payments. Entities, onboarding, accounts and transfers across providers through one API, with payouts and split payments on the same platform."},
    ],
    "source": "Fenix International Ltd accounts to 30 Nov 2025 (Companies House, filed 20 Sep 2026) as reported by Tubefilter, 26 Aug 2026; design as described by OnlyFans to Yuno, Oct 2026.",
    "notes": "The summary before the detail. Your filed numbers say the payout side alone is more than six billion dollars a year, operated by a team of 47. You opened an RFP for a token vault, but the design you described needs more than storage: a layer that decides where each creator lands and the connections to execute on it. This deck answers both, and it says plainly where a standalone vault leads today and what we still owe you in writing.",
}

# ---------------------------------------------------------------- 02.1 creator banking at a glance
SLIDES["industry-glance"] = {
    "id": "industry-glance", "type": "stats",
    "kicker": K02 + " · CREATOR BANKING AT A GLANCE",
    "headline": "Creator platforms are becoming the creator's bank. OnlyFans brings a longer payout record to that shift than anyone launching it.",
    "tiles": [
        {"label": "CREATOR ECONOMY, 2027", "value": "$480B", "caption": "Addressable market projected for 2027, from about $250B in 2023 (Goldman Sachs Research)."},
        {"label": "GLOBAL CREATORS", "value": "50M", "caption": "Growing 10% to 20% a year (Goldman Sachs Research)."},
        {"label": "PAID TO CREATORS SINCE 2016", "value": "$30B+", "caption": "OnlyFans, per the FY2025 accounts as reported in August 2026."},
        {"label": "ARCHITECT CAPITAL, MAY 2026", "value": "$535M", "caption": "About 16% of Fenix at a $3.15B valuation, to develop new financial services and products for creators."},
    ],
    "paragraph": "**Who launched what, 2025 to 2026.** Karat Banking (May 2025): creator business banking with Visa and Grasshopper Bank, more than $1.5B of credit and advances issued through its creator card. Manifest with Mastercard (July 2026): a business debit Mastercard for creators; Mastercard calls creators \"some of today's most dynamic small businesses\". OnlyFans with Architect (May 2026): Architect's founder joined the Fenix board on 8 May 2026 with a stated plan to \"add financial products for creators\" and to help creators \"address challenges with things like payment processors and banks\".",
    "bar": "The money is moving from front-end creator tools to the financial stack underneath. A platform that already knows the creator's income is the natural bank partner, and the credentials that make that work need one neutral home.",
    "source": "Goldman Sachs Research, Apr 2023; Tubefilter, 28 May 2025 and 14 Aug 2026; PYMNTS, 23 Jul 2026; Bloomberg, 8 May 2026; Companies House officer appointments, read 8 Oct 2026.",
    "notes": "The creator economy is roughly doubling between 2023 and 2027 on Goldman's numbers, and the money is moving from front-end tools to the financial stack underneath. Karat and Manifest show the pattern: a card, a bank partner and a platform that already knows the creator's income. OnlyFans has paid out more than 30 billion dollars, which is the kind of record a bank partner can underwrite, and Architect's investment is explicitly about building financial services on it.",
}

# ---------------------------------------------------------------- 02.2 why multi-bank
SLIDES["no-single-bank"] = {
    "id": "no-single-bank", "type": "cards_row",
    "kicker": K02 + " · WHY A MULTI-BANK ARCHITECTURE",
    "headline": "Platforms that depended on one bank, one network or one middleware learned the cost in 2020, 2021 and 2024. Your design makes redundancy the product.",
    "cards": [
        {"eyebrow": "DEC 2020 · ONE NETWORK DECISION", "title": "Card acceptance switched off in a day", "body": "Mastercard terminated and Visa suspended card acceptance at a major adult platform within a day of a newspaper column; Discover followed."},
        {"eyebrow": "AUG 2021 · ONE PAYOUT BANK", "title": "A content ban announced, then reversed", "body": "OnlyFans announced a ban for 1 October 2021 after banks were \"broadly rejecting money transfers and closing related accounts\". Reversed six days later once assurances were secured."},
        {"eyebrow": "2024 · ONE MIDDLEWARE LEDGER", "title": "Customers locked out of their own money", "body": "Synapse's collapse left partner banks holding about $180M against $265M owed and more than 100,000 customers locked out. The Federal Reserve ordered Evolve to fix fintech partnership risk management on 14 June 2024."},
        {"eyebrow": "2024 TO 2025 · THE REGULATORS' ANSWER", "title": "Third-party risk became the exam question", "body": "FDIC consent orders on Lineage, Sutton and Piermont for third-party risk; an August 2025 executive order directing regulators to drop \"reputation risk\" from bank exams."},
    ],
    "bar": "**What this means for the vault.** Credentials for every bank, issuer and transfer provider must sit in one place, independent of any of them, so that swapping a partner is a configuration change and losing one is a reallocation, not an outage.",
    "source": "Bloomberg, 10 Dec 2020; Fortune, 25 Aug 2021; Banking Dive, 12 Jun 2024; Federal Reserve, 14 Jun 2024; FDIC orders Jan to Feb 2024; executive order of 7 Aug 2025.",
    "notes": "Each of these failures had the same shape: one counterparty held a kill switch. Your two-to-five-bank design removes the single switch, but only if the credentials that let you move a creator between partners are held independently of any of them. That is the job we think the vault has in this architecture, and it is why the vault and the decision layer belong together.",
}

# ---------------------------------------------------------------- 02.3 what a vault is expected to do in 2026
SLIDES["vault-2026"] = {
    "id": "vault-2026", "type": "cards_row",
    "kicker": K02 + " · WHAT A TOKEN VAULT IS EXPECTED TO DO IN 2026",
    "headline": "In 2026 a vault is judged on five things beyond storing a card: script controls, network tokens, lifecycle updates, agent credentials, stablecoin rules.",
    "cards": [
        {"eyebrow": "PCI DSS 4.0.1", "title": "Script controls are live", "body": "Future-dated requirements became mandatory on 31 March 2025. Requirement 6.4.3 covers payment-page script authorization, integrity and monitoring; 11.6.1 covers detection of unauthorized page changes. SAQ A merchants must still confirm the site is not susceptible to script attacks."},
        {"eyebrow": "NETWORK TOKENS", "title": "The default credential", "body": "More than 16 billion Visa tokens issued. More than 30% of Mastercard transactions are tokenized, with a stated goal of all online transactions by 2030 and approval gains of three to six percentage points."},
        {"eyebrow": "ACCOUNT UPDATER", "title": "Cards that keep billing after reissue", "body": "Issuers push reissued numbers and expiries to Visa Account Updater, and updates are shared with the Visa Token Vault, so a card on file keeps billing after reissue."},
        {"eyebrow": "AGENT CREDENTIALS", "title": "A new token type since 2025", "body": "Visa Intelligent Commerce (30 April 2025) and Mastercard Agent Pay (29 April 2025) issue tokenized credentials for AI agents. Visa, April 2026: agent platforms should \"avoid being locked into a single token vault/vendor\"."},
    ],
    "bar": "**Stablecoin balances.** The GENIUS Act (signed 18 July 2025) bars permitted issuers from paying holders \"any form of interest or yield\" for holding a stablecoin. It does not define \"holder\" or explicitly stop platforms from paying rewards; the OCC proposed on 25 February 2026 to presume a violation when yield flows through an issuer's affiliate or \"related third party\", and no final rule had issued by 8 October 2026. Conversion and custody credentials should stay portable while that settles.",
    "source": "PCI SSC blog, 26 Mar 2025; Visa newsroom, Jun 2024, Apr 2025, Apr 2026; Mastercard newsroom, Apr 2025; Digital Transactions, 14 Nov 2024; CRS IF13174, 6 Mar 2026; Paul Hastings, 12 Mar 2026.",
    "notes": "Storing a card number safely is table stakes. The questions that separate vaults in 2026 are whether the stored credential keeps working after reissue, whether it can be presented as a network or agent token, and whether the script controls keep you at SAQ A. The stablecoin point matters for your yield feature: today the prohibition sits on issuers, the status of platform-paid rewards is an open regulatory question, and the design should keep conversion and custody credentials portable while that settles.",
}

# ---------------------------------------------------------------- 02.4 the independent vault market
SLIDES["vault-market"] = {
    "id": "vault-market", "type": "table",
    "kicker": K02 + " · WHERE THE INDEPENDENT VAULT MARKET STANDS",
    "headline": "Independent vaults come in three shapes: pure vault, vault inside an orchestrator, data privacy vault. The RFP should state which one it is buying.",
    "columns": ["Vendor", "HQ", "Founded", "Funding (public)", "Shape"],
    "col_widths": [0.18, 0.20, 0.10, 0.28, 0.24],
    "header_style": "dark", "font_size": 7.5, "bold_first_col": True, "zebra": True,
    "rows": [
        ["VGS", "San Francisco", "2015", "About $104M raised, last priced round 2020", "Pure payment vault"],
        ["Basis Theory", "California (HQ not stated by the company)", "2020", "About $50M; $33M Series B, Oct 2025", "Pure payment vault"],
        ["Spreedly", "Durham, North Carolina", "2008", "$75M growth round, Nov 2019; about $81M total", "Vault inside an orchestrator"],
        ["IXOPAY (TokenEx)", "Tulsa and Vienna", "Merger announced 17 Apr 2024", "K1-backed", "Vault inside an orchestrator"],
        ["Skyflow", "Palo Alto", "2019", "About $105M, last round Mar 2024", "Data privacy vault for PCI, PII and AI data"],
        ["Evervault", "Dublin", "2018", "$46M; $25M Series B, Mar 2026", "Encryption-first payment vault"],
        ["Yuno", "16 offices, 5 continents", "2021", "About $80M; $45M Series B, Aug 2026", "Vault inside an operating system for payments and banking connectivity"],
    ],
    "note": "Yuno's vault is described in Section 06 and compared row by row with VGS and Basis Theory in Section 07. Funding figures are third-party estimates where the vendor does not publish them.",
    "source": "Vendor pages and press releases, read 7 and 8 Oct 2026; Spreedly blog, Nov 2019; BusinessWire, Mar 2024; Crowdfund Insider, Mar 2026; y.uno About and newsroom; CB Insights profiles (estimates).",
    "notes": "We list the market as it is, including vendors we partner with. The shape matters more than the logo: a pure vault keeps routing out of scope by design, an orchestrator's vault assumes its routing, and a data privacy vault is built for personal data first. Your design needs card, bank, identity and issued-card objects under one key set plus a decision layer you control, which is the lens we apply in Section 07.",
}

# ---------------------------------------------------------------- 03.1 OnlyFans in numbers
SLIDES["of-numbers"] = {
    "id": "of-numbers", "type": "scale",
    "kicker": K03 + " · ONLYFANS IN NUMBERS",
    "headline": "OnlyFans moves more than $6 billion a year to 2.5 million creators with 47 employees. Any new payments layer has to scale without headcount.",
    "left_header": "THE SCALE TODAY · FY ENDED 30 NOV 2025",
    "tiles": [{"value": "$1.55B", "label": "Net revenue, up 10%"}, {"value": "$6.3B", "label": "Paid to creators in the year"}],
    "left_note": "**$714M** pre-tax profit, up 5%. **$30B+** paid to creators since 2016. **5,076** creators have earned $1M or more since 2016. FY2024 for reference: $7.2B of fan payments, $1.41B revenue, $5.8B paid to creators.",
    "mid_header": "WHERE THE COMPANY IS HEADING",
    "mid_items": [
        "Architect Capital bought about 16% for $535M at a $3.15B valuation (May 2026) to develop new financial services and products for creators.",
        "Architect's founder joined the Fenix International board on 8 May 2026, alongside the CEO and the owner; the CFO has been a director since December 2021.",
        "The stated direction: add financial products for creators and address their challenges with payment processors and banks.",
    ],
    "right_header": "THE FOOTPRINT",
    "right_body": "**2.5M** active creators and **132M** active fan accounts in FY2025, as reported from the filing. **47** employees. Revenue by geography, latest public split (FY2023): **66%** United States, **18%** UK and Europe, **16%** rest of world. Every fan payment and creator payout is in USD.",
    "bar": "A payout operation above $6 billion a year across millions of accounts, run by a team of 47: whatever sits underneath has to be operated by configuration, not by people.",
    "source": "Fenix International Ltd group accounts to 30 Nov 2025 (Companies House, filed 20 Sep 2026) as reported by Tubefilter, 26 Aug 2026 and Eastern Eye, 25 Aug 2026; FY2024 per RTÉ, 22 Aug 2025; FY2023 geography via Mostly Metrics; Bloomberg, 8 May 2026; Companies House officers, read 8 Oct 2026.",
    "notes": "These are your own filed numbers, as reported in August. We show them to size the vault conversation: the payout side alone is more than six billion dollars a year across millions of accounts, run by a team of 47. Anything added underneath has to be operated by configuration, not by people. The geography split is the latest one published in your accounts; if you have a newer one we will use it.",
}

# ---------------------------------------------------------------- 03.2 where demand sits
SLIDES["traffic"] = {
    "id": "traffic", "type": "traffic_list",
    "kicker": K03 + " · WHERE DEMAND SITS",
    "headline": "The United States is about two thirds of revenue and more than 40% of traffic, which is why a US-first vault scope is the right Phase 1.",
    "rows": [
        {"country": "United States", "pct": "42.78%"}, {"country": "United Kingdom", "pct": "5.41%"},
        {"country": "Germany", "pct": "5.32%"}, {"country": "Canada", "pct": "5.27%"}, {"country": "Spain", "pct": "2.96%"},
    ],
    "side": {"header": "REVENUE BY GEOGRAPHY · FY2023, LATEST PUBLIC SPLIT", "items": [
        {"title": "66% United States", "body": "$863M of $1.3B."},
        {"title": "18% UK and Europe", "body": "$229M."},
        {"title": "16% Rest of world", "body": "$214M."},
        {"title": "One currency", "body": "All fan payments and creator earnings are transacted in USD, per the Terms of Service."},
    ]},
    "source": "Share of web traffic by country: Similarweb, onlyfans.com, September 2026 (estimate, top five as published). Revenue split: Fenix International FY2023 accounts via Mostly Metrics. OnlyFans Terms of Service, last updated Aug 2024.",
    "notes": "Your traffic is global but your revenue is American, and your pricing is in dollars everywhere. That makes US balances the right first scope for creator accounts, and it also means the vault must be ready for European and Canadian creators in Phase 2 without a second architecture. The geography split is the latest one published in your accounts; if you have a newer one we will use it.",
}

# ---------------------------------------------------------------- 03.3 the stack as publicly evidenced
SLIDES["stack"] = {
    "id": "stack", "type": "cards_row",
    "kicker": K03 + " · THE STACK AS PUBLICLY EVIDENCED",
    "headline": "Publicly, OnlyFans runs card pay-ins through a third-party processor, pays out on location-dependent rails and holds the bank data itself. No vault is named.",
    "cards": [
        {"eyebrow": "PAY-IN", "title": "Cards, in USD, through an approved provider", "body": "\"All Fan Payments will be received and processed by a third-party payment provider we approve.\" Charged in USD; subscriptions renew automatically on the stored card; a wallet can be set as the primary method for rebills. Descriptors: \"OnlyFans\", \"OF\", \"OnlyFans.com\"."},
        {"eyebrow": "PAYOUTS", "title": "Rails that depend on where the creator lives", "body": "Method \"will depend on where you live\"; $20 minimum for most methods; manual or automatic daily, weekly or monthly where available. Earnings pend 7 days, 21 in a small number of high-reversal countries; payouts within 3 to 5 business days, up to 10."},
        {"eyebrow": "DATA ONLYFANS HOLDS", "title": "Bank accounts, identity and tax records", "body": "Bank account details for direct-transfer payouts; creator ID and two photos; tax IDs, VAT numbers and W-9 data; retained up to 7 years where required."},
        {"eyebrow": "NOT PUBLIC", "title": "Processors, vault, attestation", "body": "Processor and acquirer names, whether a vault vendor is in place, and a PCI DSS attestation are not public. Third-party claims about specific processors exist and are not used here."},
    ],
    "bar": "**Risk posture visible in the rules.** \"OnlyFans cannot prevent a Fan from issuing a chargeback request\"; the amount is removed from the creator's income and the fan's access may be limited. The 20% platform fee is deducted from each fan payment.",
    "source": "OnlyFans Terms of Service (last updated Aug 2024), Help Center and Privacy Policy, read 8 Oct 2026.",
    "notes": "We built this slide only from your own Terms, Help Center and Privacy Policy. The picture that emerges is a card checkout outsourced to a processor, a payout operation that varies by country, and bank account data that sits with OnlyFans. If any of this is out of date, tell us and we will correct it; we deliberately left out third-party claims about which processors you use.",
}

# ---------------------------------------------------------------- 03.4 the 2021 lesson
SLIDES["lesson-2021"] = {
    "id": "lesson-2021", "type": "table",
    "kicker": K03 + " · THE 2021 LESSON IN ONE SLIDE",
    "headline": "In 2021 the payout rail, not the checkout, nearly stopped the business. The multi-bank design is the answer, and the vault is what makes it operable.",
    "columns": ["When", "What happened", "What it shows"],
    "col_widths": [0.14, 0.52, 0.34],
    "header_style": "dark", "font_size": 7.5, "bold_first_col": True, "zebra": True,
    "rows": [
        ["Dec 2020", "Card networks cut off a major adult platform within a day of a newspaper column.", "One network decision can end acceptance overnight."],
        ["Apr 2021", "Mastercard AN 5196 sets registration, verification, consent, review and complaint rules for adult-content merchants and their acquirers, effective 15 Oct 2021.", "Compliance load lands on the platform and every acquirer it uses."],
        ["19 Aug 2021", "OnlyFans announces a ban on sexually explicit content from 1 Oct 2021. The founder's explanation: \"the short answer is banks\".", "The constraint was the payout bank, not the checkout."],
        ["25 Aug 2021", "Ban suspended after assurances from banks.", "Reversed in six days, with no change to the architecture."],
        ["Apr 2024", "The CEO says a bank rejected her as a customer because of OnlyFans: \"Financial inclusion should be top of the agenda for everybody.\"", "The exposure persists at the level of the company and its people."],
        ["May 2026", "Architect Capital invests $535M with a mandate to build financial services for creators; its founder joins the board.", "The answer is now a product: several banks per creator."],
    ],
    "note": "**The requirement this creates.** Bank, issuer and transfer-provider credentials for every creator must be held independently of any single partner, so that losing one is a reallocation, not an outage.",
    "source": "Bloomberg, 10 Dec 2020; AdultBizLaw, 27 Apr 2021; Fortune, 25 Aug 2021; Fortune, 4 Apr 2024; Bloomberg, 8 May 2026; Companies House, read 8 Oct 2026.",
    "notes": "You lived this, so we keep it short. The 2021 episode was about payouts and bank accounts, and the 2026 plan answers it with several banks per creator. The vault is where that plan becomes operable: if the credentials and mandates for every partner sit in one neutral place under your keys, moving a creator is a rule change rather than a migration.",
}

# ---------------------------------------------------------------- 03.5 payments today in four numbers
SLIDES["four-numbers"] = {
    "id": "four-numbers", "type": "four_numbers",
    "kicker": K03 + " · PAYMENTS TODAY, IN FOUR NUMBERS",
    "headline": "Four published rules describe the payment operation a vault has to serve: one fee, one currency, one pending window and one payout clock.",
    "tiles": [
        {"value": "20%", "label": "Platform fee deducted from each fan payment"},
        {"value": "1", "label": "Currency: every fan payment and creator payout is in USD"},
        {"value": "7 days", "label": "Pending balance before earnings can be withdrawn; 21 in a small number of countries"},
        {"value": "3 to 5", "label": "Business days for a payout to arrive after request, up to 10"},
    ],
    "right_header": "WHAT THE ENVELOPE MEANS FOR THE VAULT",
    "right_items": [
        {"title": "One currency simplifies Phase 1", "body": "US balances in USD, with no FX leg inside the vault scope."},
        {"title": "Two clocks the banks must meet", "body": "A 7-day pending window and a 3-to-5-day payout clock define how fast funds must move between the banks in your design."},
        {"title": "A $20 minimum payout for most methods", "body": "Small, frequent transfers across many accounts, which favours rails like same-day ACH and RTP."},
    ],
    "bar": "These four numbers come from your Terms and Help Center. They set the operational envelope for anything underneath.",
    "source": "OnlyFans Terms of Service and Help Center, read 8 Oct 2026.",
    "notes": "These four numbers come from your Terms and Help Center. They set the operational envelope for anything underneath: a single currency simplifies Phase 1, and the pending and payout windows define how fast a creator's funds must be able to move between the banks in your design.",
}

# ---------------------------------------------------------------- 04.1 how OnlyFans vaults today
SLIDES["cof-today"] = {
    "id": "cof-today", "type": "cards_row",
    "kicker": "HOW ONLYFANS VAULTS TODAY · KNOWN, INFERRED, UNKNOWN",
    "headline": "Today the cards live with the processors and the bank accounts live with OnlyFans. The RFP is the moment to put both under one set of keys.",
    "cards": [
        {"eyebrow": "KNOWN · YOUR OWN DOCUMENTS", "title": "Card data never reaches OnlyFans; bank data does", "body": "\"We do not receive your full payment card number, payment card expiration date, or the security code.\" Payments are processed by third-party providers. Bank account details for direct-transfer payouts are stored by OnlyFans. Identity documents, selfies and tax identifiers are collected and kept up to 7 years where required."},
        {"eyebrow": "INFERRED · FROM HOW THE PRODUCT BEHAVES", "title": "A stored credential exists, held by the processor", "body": "Auto-renewing subscriptions and a \"Your Cards\" section mean a stored credential and merchant-initiated charges exist today. On the public evidence that credential is held by the processor, so it is tied to that processor. An inference, for OnlyFans to confirm."},
        {"eyebrow": "UNKNOWN · NOT PUBLIC", "title": "Processors, vault vendor, PCI path, token requestor", "body": "Which processors and acquirers are live; whether a token vault or tokenization vendor is already in place; the PCI DSS validation path; whether network tokens are in use and under whose token requestor ID."},
    ],
    "bar": "On the public record the first class of data is held by whoever processes your payments and the second by you. A vault RFP is the natural point to decide that both, and the new classes your design adds, sit in one place that you control.",
    "source": "OnlyFans Privacy Policy, Terms of Service and Help Center, read 8 Oct 2026.",
    "notes": "We are careful here because this is your RFP and you know the answers. On the public record, card data never reaches OnlyFans and bank data does; the first is held by whoever processes your payments, the second by you. A vault RFP is the natural point to decide that both classes, and the new ones your design adds, sit in one place that you control.",
}

# ---------------------------------------------------------------- 04.2 six kinds of secret
SLIDES["five-data"] = {
    "id": "five-data", "type": "table",
    "kicker": K04 + " · WHAT THE DESIGN IMPLIES THE VAULT MUST HOLD",
    "headline": "A vault for this design holds six kinds of secret, and payment cards are the smallest of them by count.",
    "columns": ["Data class", "Where it comes from", "Why the vault must hold it", "Today"],
    "col_widths": [0.24, 0.30, 0.34, 0.12],
    "header_style": "dark", "font_size": 7.5, "bold_first_col": True, "zebra": True,
    "rows": [
        ["Fan payment cards (PAN, expiry, network token, network transaction ID)", "Fan checkout and rebills", "Keeps subscriptions billing across processors and after card reissue.", "Exists"],
        ["Creator bank accounts (account and routing numbers, mandates)", "Direct-transfer payouts today; two to five banks per creator in the design", "The record that lets a creator be moved between banks without re-onboarding.", "Exists"],
        ["Identity documents and tax identifiers (ID, selfies, TIN or W-9, VAT)", "Creator onboarding and tax reporting", "Required by every new bank and issuer; retained up to 7 years.", "Exists"],
        ["Issued-card data (PAN, CVV, PIN, display)", "New: cards issued to creators by pluggable issuers", "Must survive an issuer swap; card display and PIN set without exposing data to OnlyFans systems.", "With the design"],
        ["Stablecoin and custody credentials (wallet addresses, provider tokens)", "New: conversion of balances to earn yield", "Portable while the yield rules settle.", "With the design"],
        ["Provider credentials (API keys, certificates for banks, issuers, transfer providers)", "New: multi-provider architecture", "Rotated and scoped in one place so adding or dropping a provider is configuration.", "With the design"],
    ],
    "note": "Phase 1 is US balances only; the first three classes exist today, the last three arrive with the design. Where each class lives in Yuno today, with its label, is on slide {{slide:vault-data}}.",
    "source": "OnlyFans Terms, Help Center and Privacy Policy, read 8 Oct 2026; design as described by OnlyFans to Yuno, Oct 2026; Visa developer documentation; CRS IF13174, 6 Mar 2026.",
    "notes": "This is the scope we think your RFP should write down explicitly, because a vault evaluated on cards alone will be re-evaluated within a year. Three of these classes already exist in your operation; the other three come with the banking design. In Sections 06 and 07 we label, class by class, what is documented today and what is open.",
}

# ---------------------------------------------------------------- 04.4 four external clocks
SLIDES["clocks"] = {
    "id": "clocks", "type": "stats",
    "kicker": K04 + " · FOUR EXTERNAL CLOCKS ALREADY RUNNING",
    "headline": "Four external clocks set the pace for Phase 1, and none of them is set by a vendor.",
    "tiles": [
        {"label": "PCI DSS 4.0.1", "value": "31 Mar 2025", "caption": "Script controls (6.4.3, 11.6.1) became mandatory."},
        {"label": "GENIUS ACT", "value": "18 Jan 2027", "caption": "Latest effective date, or 120 days after final rules; the OCC yield rule is still proposed."},
        {"label": "MASTERCARD", "value": "2030", "caption": "Stated goal to tokenize all online transactions."},
        {"label": "AGENT CREDENTIALS", "value": "2025", "caption": "Visa Intelligent Commerce, Mastercard Agent Pay and Visa's Trusted Agent Protocol launched."},
    ],
    "bar": "None of these clocks is set by a vendor. They are the reason to scope the vault for bank, identity and agent credentials now rather than after Phase 1, and the dates behind the phases in Section 08.",
    "source": "PCI SSC, Mar 2025; Paul Hastings, Mar 2026; Digital Transactions, Nov 2024; Visa and Mastercard newsrooms, Apr and Oct 2025.",
    "notes": "None of these clocks is set by a vendor. They are the reason to scope the vault for bank, identity and agent credentials now rather than after Phase 1, and they are the dates we use in Section 08 when we propose the phases.",
}
