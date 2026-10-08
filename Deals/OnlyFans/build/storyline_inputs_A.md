# Storyline inputs A · sections 01 to 04 (OnlyFans token vault deck)

Prepared 8 Oct 2026. Layout vocabulary follows the Eventbrite template: kicker in ALL CAPS, headline as a full-sentence conclusion, body elements (stat tiles, cards, bullet lists, "payments today in four numbers" row, traffic-by-country list), one Source line, speaker notes written for the customer. Every number cites a row in `ledger_onlyfans.md` (C, P, V, I, B, U). "Design facts" are what OnlyFans told us in conversation (see CONTEXT.md); they are shown as "as we understood it" and are for OnlyFans to correct, not as public facts. Items marked TO CONFIRM need German's or OnlyFans' confirmation before the deck ships.

Rules honoured: no em-dashes and no spaced hyphens as punctuation; USD only; no Yuno performance stats outside the published ones (none are used in these four sections); no customer or prospect names; competitor tone respectful; nothing from the unverified list (U rows) on a slide.

---

## Section 01 · Why we are here

### Divider
- Title: Why we are here
- Number: 01

### Slide 01.1
- Kicker: WHY WE ARE HERE · WHAT WE UNDERSTOOD
- Headline: One creator account on top; two to five banks, pluggable issuers and transfer providers underneath, so no single partner can cut a creator off.
- Body (design cards, left to right, "as we understood it"):
  * Card "Creator" · opens one OnlyFans account.
  * Card "Banks" · two to five per creator, opened behind the account.
  * Card "Card issuers" · pluggable: add or swap issuing providers.
  * Card "Bank transfer providers" · several, for redundancy.
  * Card "Stablecoin conversion" · balances can be converted to earn yield.
  * Card "Scope" · Phase 1 is US balances only; the destination is full banking as a service.
- Body (right column, "Why this matters for a vault"):
  * Every one of those boxes holds a secret: card numbers, account numbers, identity documents, issued-card data, wallet credentials, provider API keys.
  * A vault chosen for cards alone will be asked to hold all of them within a year of Phase 1.
- Source line: Design as described by OnlyFans to Yuno, October 2026 (TO CONFIRM by OnlyFans).
- Speaker notes: This is your design as we understood it from our conversation; please correct anything we have wrong before reading further. We drew it first because it changes what a token vault has to be: cards are the smallest class of secret in this picture. The rest of the deck is built on that reading.

### Slide 01.2
- Kicker: WHY WE ARE HERE · WHAT THIS DECK ANSWERS
- Headline: You have a token vault RFP open; this deck answers the vault question and the question you asked us most: who decides where each creator lands.
- Body (three cards):
  * Card "The vault" · What is stored, how it is tokenized, how it is forwarded, what leaves with you if you exit. Sections 06 and 07.
  * Card "The decision" · Which bank, issuer and rail each creator is placed on, and who sets that rule. Answer in one line: you do; the rule is yours and we execute it. Section 06.
  * Card "The path" · US balances first, banking as a service next, with open items named and owned. Section 08.
- Body (bullet list, "What we did not assume"):
  * We did not assume which processors or banks you use today; where it is not public we say so (Section 03).
  * We did not upgrade any claim: each one carries a label with its basis (slide 01.3).
- Source line: OnlyFans RFP context as shared with Yuno, October 2026.
- Speaker notes: We are late to your RFP, so this deck is written to be read without us in the room. It separates what is public about OnlyFans, what we inferred, and what only you can confirm. Where a standalone vault is ahead of us, Section 07 says so.

### Slide 01.3
- Kicker: HOW TO READ THIS DECK
- Headline: Every capability claim carries one of three labels, and every market fact carries a dated source, so your team can check both without us.
- Body (label cards, Samuel's system, keep exact):
  * CONFIRMED · Written in Yuno's public documentation, read at docs.y.uno on 7 October 2026; company figures from y.uno. A BETA tag marks anything that depends on the PCI Proxy, which is in beta and enabled per organization.
  * PUBLIC DOCS · Read on another vendor's public pages on 7 October 2026. Treat each line as a question to confirm with them.
  * OPEN · Not yet confirmed in writing inside Yuno. Shown with an owner, never as a fact. The open items are listed together in Section 08.
- Body (small card, "Market and company facts in Sections 02 to 04"):
  * Each slide ends with a Source line naming the document and its date: OnlyFans' own Terms, Help Center and Privacy Policy; Companies House filings; card-network and regulator publications; named press reports where no primary exists.
  * Third-party estimates (traffic, vendor headcounts) are marked as estimates.
- Source line: Yuno label system, October 2026.
- Speaker notes: We label every claim about what Yuno, or anyone else, can do. For facts about OnlyFans and the market we cite the document and the date, and we prefer your own pages and filings over press. A vault is the wrong place for surprises, so where we could not verify something we left it out or marked it open.

---

## Section 02 · Industry context

### Divider
- Title: Industry context
- Number: 02

### Slide 02.1
- Kicker: INDUSTRY CONTEXT · CREATOR BANKING AT A GLANCE
- Headline: Creator platforms are becoming the creator's bank, and OnlyFans brings a longer payout record to that shift than anyone launching it.
- Body (stat tiles):
  * $480B · creator economy addressable market projected for 2027, from about $250B in 2023 (I1)
  * 50M · global creators, growing 10% to 20% a year (I1)
  * $30B+ · paid by OnlyFans to creators since 2016 (C6)
  * $535M · Architect Capital's May 2026 investment, tied to new financial services for creators (C14)
- Body (cards, "Who launched what, 2025 to 2026"):
  * Card "Karat Banking · May 2025" · Creator business banking with Visa and Grasshopper Bank; more than $1.5B of credit and advances issued through its creator card (I2).
  * Card "Manifest × Mastercard · Jul 2026" · A business debit Mastercard for creators; Mastercard calls creators "some of today's most dynamic small businesses" (I3).
  * Card "OnlyFans × Architect · May 2026" · Architect's founder joined the Fenix board on 8 May 2026 with a stated plan to "add financial products for creators" (C15, C16).
- Source line: Goldman Sachs Research, Apr 2023; Tubefilter, 28 May 2025 and 14 Aug 2026; PYMNTS, 23 Jul 2026; Bloomberg, 8 May 2026; Companies House, read 8 Oct 2026.
- Speaker notes: The creator economy is roughly doubling between 2023 and 2027 on Goldman's numbers, and the money is moving from front-end tools to the financial stack underneath. Karat and Manifest show the pattern: a card, a bank partner and a platform that already knows the creator's income. OnlyFans has paid out more than $30 billion, which is the kind of record a bank partner can underwrite.

### Slide 02.2
- Kicker: INDUSTRY CONTEXT · WHY A MULTI-BANK ARCHITECTURE
- Headline: Platforms that depended on one bank, one network or one middleware learned the cost in 2020, 2021 and 2024; your design treats redundancy as the product.
- Body (timeline cards):
  * Card "Dec 2020 · one network decision" · Mastercard terminated and Visa suspended card acceptance at Pornhub within a day of a newspaper column; Discover followed (P22).
  * Card "Aug 2021 · one payout bank" · OnlyFans announced a content ban for 1 Oct 2021 after banks were "broadly rejecting money transfers and closing related accounts"; reversed six days later once assurances were secured (P19, P20).
  * Card "2024 · one middleware ledger" · Synapse's collapse left partner banks holding about $180M against $265M owed and more than 100,000 customers locked out; the Federal Reserve ordered Evolve to fix fintech partnership risk management on 14 Jun 2024 (I5, I6).
  * Card "2024 to 2025 · the regulators' answer" · FDIC consent orders on Lineage, Sutton and Piermont for third-party risk (I7); an Aug 2025 executive order directing regulators to drop "reputation risk" from bank exams (I8).
- Body (bullet list, "What this means for the vault"):
  * The vault must be bank-neutral and issuer-neutral: credentials for every bank and issuer in one place, under your keys, so swapping a partner is a configuration change.
  * The vault must hold the ledger-adjacent data a bank exit requires: account numbers, mandates, identity records, not only cards.
- Source line: Bloomberg, 10 Dec 2020; Fortune, 25 Aug 2021; Banking Dive, 12 Jun 2024; Federal Reserve, 14 Jun 2024; Covington and Mayer Brown summaries of the 7 Aug 2025 executive order.
- Speaker notes: Each of these failures had the same shape: one counterparty held a kill switch. Your two-to-five-bank design removes the single switch, but only if the credentials that let you move a creator between partners are held independently of any of them. That is the job we think the vault has in this architecture.

### Slide 02.3
- Kicker: INDUSTRY CONTEXT · WHAT A TOKEN VAULT IS EXPECTED TO DO IN 2026
- Headline: In 2026 a vault is judged on five things beyond storing a card: script controls, network tokens, lifecycle updates, agent credentials and the rules around stablecoin balances.
- Body (five cards):
  * Card "PCI DSS 4.0.1" · Future-dated requirements became mandatory on 31 Mar 2025; 6.4.3 requires payment-page scripts to be authorized, integrity-checked and monitored, and 11.6.1 requires detection of unauthorized page changes; SAQ A merchants must still confirm their site is not susceptible to script attacks (I9).
  * Card "Network tokens" · More than 16 billion Visa tokens (I12); more than 30% of Mastercard transactions tokenized, with a goal to tokenize all online transactions by 2030 and approval gains of three to six percentage points (I13); in Europe, three in five Mastercard e-commerce transactions are tokenized (I14, TO CONFIRM).
  * Card "Account updater" · Issuers push reissued numbers and expiries to Visa Account Updater; updates are shared with the Visa Token Vault, so a card on file keeps billing after reissue (I15).
  * Card "Agent credentials" · Visa Intelligent Commerce (30 Apr 2025) replaces card details with tokenized credentials for AI agents; Mastercard Agent Pay (29 Apr 2025) issues Agentic Tokens on MDES; Visa's Trusted Agent Protocol followed on 14 Oct 2025 (I16, I17, I20). Visa's own words in Apr 2026: agent platforms should "avoid being locked into a single token vault/vendor" (I18).
  * Card "Stablecoin balances" · The GENIUS Act (signed 18 Jul 2025) bars permitted issuers from paying holders "any form of interest or yield" for holding a stablecoin; it does not define "holder" and does not explicitly stop platforms or exchanges from paying rewards; the OCC proposed on 25 Feb 2026 to presume a violation when yield flows through an issuer's affiliate or "related third party", and no final rule had issued by 8 Oct 2026 (I21, I22, I23).
- Source line: PCI SSC blog, 26 Mar 2025; Visa newsroom, Jun 2024, Apr 2025, Oct 2025, Apr 2026, Jun 2026; Digital Transactions, 14 Nov 2024; Mastercard newsroom, Apr 2025 and Jun 2026; CRS IF13174, 6 Mar 2026; Paul Hastings, 12 Mar 2026.
- Speaker notes: Storing a PAN safely is table stakes; the questions that separate vaults in 2026 are whether the stored credential keeps working after reissue, whether it can be presented as a network or agent token, and whether the script controls keep you at SAQ A. The stablecoin point matters for your yield feature: today the prohibition sits on issuers, the status of platform-paid rewards is an open regulatory question, and the design should keep conversion and custody credentials portable while that settles.

### Slide 02.4
- Kicker: INDUSTRY CONTEXT · WHERE THE INDEPENDENT VAULT MARKET STANDS
- Headline: Independent vaults come in three shapes, pure vault, vault inside an orchestrator, and data privacy vault; the RFP should state which shape it is buying.
- Body (table: Vendor · HQ · Founded · Funding · Shape):
  * VGS · San Francisco · 2015 · about $104M raised, last priced round 2020 · pure payment vault (I24)
  * Basis Theory · California (HQ not stated by the company) · 2020 · about $50M, $33M Series B Oct 2025 · pure payment vault (I25)
  * Spreedly · Durham, North Carolina · 2008 · $75M growth round Nov 2019, about $81M total · vault inside an orchestrator (I26)
  * IXOPAY (TokenEx) · Tulsa and Vienna · merger announced 17 Apr 2024 · K1-backed · vault inside an orchestrator (I27)
  * Skyflow · Palo Alto · 2019 · about $105M, last round Mar 2024 · data privacy vault for PCI, PII and AI data (I28)
  * Evervault · Dublin · 2018 or 2019 · $46M, $25M Series B Mar 2026 · encryption-first payment vault (I29)
  * Bluefin · Atlanta · 2007 · about $31M · P2PE and vaultless tokenization (I30)
- Body (one line under the table): Yuno's vault is described in Section 06 and compared row by row with VGS and Basis Theory in Section 07.
- Source line: Vendor pages and press releases, read 7 and 8 Oct 2026; Spreedly blog, Nov 2019; BusinessWire, Mar 2024; Crowdfund Insider, Mar 2026; CB Insights profiles (estimates).
- Speaker notes: We list the market as it is, including vendors we partner with. The shape matters more than the logo: a pure vault keeps routing out of scope by design, an orchestrator's vault assumes its routing, and a data privacy vault is built for PII first. Your design needs card, bank, identity and issued-card objects under one key set plus a decision layer you control, which is the lens we apply in Section 07.

---

## Section 03 · How OnlyFans runs payments today

### Divider
- Title: How OnlyFans runs payments today
- Number: 03

### Slide 03.1
- Kicker: HOW ONLYFANS RUNS PAYMENTS TODAY · ONLYFANS IN NUMBERS
- Headline: OnlyFans moves more than $6 billion a year to 2.5 million creators with 47 employees, so any new payments layer has to scale without headcount.
- Body (stat tiles, FY ended 30 Nov 2025 unless stated):
  * $1.55B · net revenue, up 10% (C3)
  * $714M · pre-tax profit, up 5% (C4)
  * $6.3B · paid to creators in the year (C5)
  * $30B+ · paid to creators since 2016 (C6)
  * 2.5M · active creators (C7, TO CONFIRM wording against the filing)
  * 132M · active fan accounts (C7, TO CONFIRM wording)
  * 47 · employees (C9)
  * 5,076 · creators who have earned $1M or more since 2016 (C8)
- Body (small card, "Prior year for reference"): FY2024: fan payments $7.2B, revenue $1.41B, $5.8B paid to creators (C11).
- Source line: Fenix International Ltd group accounts to 30 Nov 2025, filed at Companies House 20 Sep 2026, as reported by Tubefilter (26 Aug 2026) and Eastern Eye (25 Aug 2026); FY2024 per RTÉ, 22 Aug 2025.
- Speaker notes: These are your own filed numbers, as reported in August. We show them to size the vault conversation: the payout side alone is more than $6 billion a year across millions of accounts, run by a team of 47. Anything added underneath has to be operated by configuration, not by people.

### Slide 03.2
- Kicker: HOW ONLYFANS RUNS PAYMENTS TODAY · WHERE DEMAND SITS
- Headline: The United States is about two thirds of revenue and more than 40% of traffic, which is why a US-first vault scope is the right Phase 1.
- Body (traffic-by-country list, "% of web traffic by country, Sept 2026"):
  * United States · 42.78%
  * United Kingdom · 5.41%
  * Germany · 5.32%
  * Canada · 5.27%
  * Spain · 2.96%
  * (extend to ten countries from Similarweb Pro, TO CONFIRM) (C28)
- Body (stat tiles, "Revenue by geography, FY2023, latest public split"):
  * 66% · United States, $863M of $1.3B (C12)
  * 18% · UK and Europe, $229M (C12)
  * 16% · rest of world, $214M (C12)
- Body (one line): All fan payments and creator earnings are transacted in USD (P2).
- Source line: Similarweb, onlyfans.com, September 2026 (estimate); Fenix International FY2023 accounts via Mostly Metrics; OnlyFans Terms of Service, last updated Aug 2024.
- Speaker notes: Your traffic is global but your revenue is American, and your pricing is in dollars everywhere. That makes US balances the right first scope for creator accounts, and it also means the vault must be ready for European and Canadian creators in Phase 2 without a second architecture. The geography split is the latest one published in your accounts; if you have a newer one we will use it.

### Slide 03.3
- Kicker: HOW ONLYFANS RUNS PAYMENTS TODAY · THE STACK AS PUBLICLY EVIDENCED
- Headline: Publicly, OnlyFans runs card pay-ins through an unnamed third-party processor and payouts on location-dependent rails, and holds the bank data itself; nothing public names a vault.
- Body (four cards):
  * Card "Pay-in" · "All Fan Payments will be received and processed by a third-party payment provider we approve" (P1). Cards only, charged in USD (P2); subscriptions renew automatically on the stored card (P4); a wallet can be set as the primary method for rebills (P5). Statement descriptors: "OnlyFans", "OF" or "OnlyFans.com" (P8).
  * Card "Payouts" · Method "will depend on where you live"; minimum $20 for most methods; manual or automatic daily, weekly or monthly where available (P11). Earnings pend 7 days, 21 days in a small number of high-reversal countries (P12); payouts "should be paid within 3-5 business days", up to 10 (P13).
  * Card "Data OnlyFans holds" · Bank account details for direct-transfer payouts (P15); creator ID and two photos (P17); tax IDs, VAT numbers and W-9 data (P18); retained up to 7 years where required (V4).
  * Card "Not public" · Processor and acquirer names; whether a vault vendor is in place; a PCI DSS attestation (V8, V9). Third-party claims about specific processors exist and are not used here.
- Body (bullet list, "Risk posture visible in the rules"): "OnlyFans cannot prevent a Fan from issuing a chargeback request"; the amount is removed from the creator's income and the fan's access may be limited (P10). The 20% platform fee is deducted from each fan payment (P3).
- Source line: OnlyFans Terms of Service (last updated Aug 2024), Help Center and Privacy Policy, read 8 Oct 2026.
- Speaker notes: We built this slide only from your own Terms, Help Center and Privacy Policy. The picture that emerges is a card checkout outsourced to a processor, a payout operation that varies by country, and bank account data that sits with OnlyFans. If any of this is out of date, tell us and we will correct it; we deliberately left out third-party claims about which processors you use.

### Slide 03.4
- Kicker: HOW ONLYFANS RUNS PAYMENTS TODAY · THE 2021 LESSON IN ONE SLIDE
- Headline: In 2021 it was the payout rail, not the checkout, that nearly stopped the business; the multi-bank design is the direct answer, and the vault is what makes it operable.
- Body (timeline):
  * Dec 2020 · Card networks cut off a major adult platform within a day (P22).
  * Apr 2021 · Mastercard AN 5196 sets registration, verification, consent, review and complaint rules for adult content merchants and their acquirers, effective 15 Oct 2021 (P21).
  * 19 Aug 2021 · OnlyFans announces a ban on sexually explicit content from 1 Oct 2021; the founder's explanation: "the short answer is banks" (P19, P20).
  * 25 Aug 2021 · Ban suspended after assurances from banks (P19).
  * Apr 2024 · The CEO says a bank rejected her as a customer because of OnlyFans: "Financial inclusion should be top of the agenda for everybody." (C21)
  * May 2026 · Architect Capital invests $535M with a mandate to build financial services for creators; its founder joins the board (C14, C15, C16).
- Body (card, "The requirement this creates"): Bank, issuer and transfer-provider credentials for every creator must be held independently of any single partner, so that losing one is a reallocation, not an outage.
- Source line: Bloomberg, 10 Dec 2020; AdultBizLaw, 27 Apr 2021; Fortune, 25 Aug 2021; Fortune, 4 Apr 2024; Bloomberg, 8 May 2026; Companies House, read 8 Oct 2026.
- Speaker notes: You lived this, so we keep it short. The 2021 episode was about payouts and bank accounts, and the 2026 plan answers it with several banks per creator. The vault is where that plan becomes operable: if the credentials and mandates for every partner sit in one neutral place under your keys, moving a creator is a rule change rather than a migration.

### Slide 03.5
- Kicker: HOW ONLYFANS RUNS PAYMENTS TODAY · PAYMENTS TODAY, IN FOUR NUMBERS
- Headline: Four published rules describe the payment operation a vault has to serve: one fee, one currency, one pending window and one payout clock.
- Body (four-number row):
  * 20% · platform fee deducted from each fan payment (P3)
  * 1 · currency: every fan payment and creator payout is in USD (P2)
  * 7 days · pending balance before earnings can be withdrawn; 21 days in a small number of countries (P12)
  * 3 to 5 · business days for a payout to arrive after request, up to 10 (P13)
- Alternate tile if the builder needs five: $20 · minimum payout for most methods (P11).
- Source line: OnlyFans Terms of Service and Help Center, read 8 Oct 2026.
- Speaker notes: These four numbers come from your Terms and Help Center. They set the operational envelope for anything underneath: a single currency simplifies Phase 1, and the pending and payout windows define how fast a creator's funds must be able to move between the banks in your design.

---

## Section 04 · How OnlyFans vaults today and what the RFP has to cover

### Divider
- Title: How OnlyFans vaults today and what the RFP has to cover
- Number: 04

### Slide 04.1
- Kicker: HOW ONLYFANS VAULTS TODAY · WHAT IS KNOWN, INFERRED AND UNKNOWN
- Headline: Today the cards live with the processors and the bank accounts live with OnlyFans; the RFP is the moment to put both under one set of keys.
- Body (three cards):
  * Card "Known (your own documents)" · "We do not receive your full payment card number, payment card expiration date, or the security code." (V1) Payments are processed by third-party providers (P1). Bank account details for direct-transfer payouts are stored by OnlyFans (V3). Identity documents, selfies and tax identifiers are collected (V6, V7). Financial and identity records are kept up to 7 years where required (V4).
  * Card "Inferred (from how the product behaves)" · Auto-renewing subscriptions and a "Your Cards" section mean a stored credential and merchant-initiated charges exist today; on the public evidence that credential is held by the processor, so it is tied to that processor (V5). Inference, for OnlyFans to confirm.
  * Card "Unknown (not public)" · Which processors and acquirers are live; whether a token vault or tokenization vendor is already in place; the PCI DSS validation path; whether network tokens are in use and under whose token requestor ID (V8, V9).
- Source line: OnlyFans Privacy Policy, Terms of Service and Help Center, read 8 Oct 2026.
- Speaker notes: We are careful here because this is your RFP and you know the answers. On the public record, card data never reaches OnlyFans and bank data does; the first is held by whoever processes your payments, the second by you. A vault RFP is the natural point to decide that both classes, and the new ones your design adds, sit in one place that you control.

### Slide 04.2
- Kicker: WHAT THE RFP HAS TO COVER · WHAT THE DESIGN IMPLIES THE VAULT MUST HOLD
- Headline: A vault for this design holds six kinds of secret, and payment cards are the smallest of them by count.
- Body (table: Data class · Where it comes from · Why the vault must hold it):
  * Fan payment cards (PAN, expiry, network token, network transaction ID) · Fan checkout and rebills (P4, P5) · Keeps subscriptions billing across processors and after card reissue (I15).
  * Creator bank accounts (account and routing numbers, mandates) · Direct-transfer payouts today (P15); two to five banks per creator in the design · The record that lets a creator be moved between banks without re-onboarding.
  * Identity documents and tax identifiers (ID, selfies, TIN or W-9, VAT) · Creator onboarding and tax reporting (P17, P18) · Required by every new bank and issuer; retained up to 7 years (V4).
  * Issued-card data (PAN, CVV, PIN, display) · New: cards issued to creators by pluggable issuers · Must survive an issuer swap; card display and PIN set without exposing data to OnlyFans systems.
  * Stablecoin and custody credentials (wallet addresses, provider tokens, conversion instructions) · New: conversion of balances to earn yield · Portable while the yield rules settle (I21, I22, I23).
  * Provider credentials (API keys, certificates for banks, issuers, transfer providers) · New: multi-provider architecture · Rotated and scoped in one place so adding or dropping a provider is configuration.
- Body (one line): Phase 1 is US balances only; the first three classes exist today, the last three arrive with the design.
- Source line: OnlyFans Terms, Help Center and Privacy Policy, read 8 Oct 2026; design as described by OnlyFans to Yuno, Oct 2026 (TO CONFIRM); Visa developer documentation; CRS IF13174, 6 Mar 2026.
- Speaker notes: This is the scope we think your RFP should write down explicitly, because a vault evaluated on cards alone will be re-evaluated within a year. Three of these classes already exist in your operation; the other three come with the banking design. In Sections 06 and 07 we label, class by class, what is documented today and what is open.

### Slide 04.3
- Kicker: WHAT THE RFP HAS TO COVER · THE QUESTIONS A CAREFUL VAULT BUYER ASKS
- Headline: Vault RFPs are decided on ten questions about exit, outage and scope; Sections 06 and 07 answer each one with a label.
- Body (numbered list, two columns):
  1. Which card networks are connected directly for network tokens, and which through a partner?
  2. In whose name is the token requestor ID registered, and what leaves with us on exit: PANs, network transaction IDs, bank and identity records?
  3. How is the network transaction ID captured on the first charge and replayed on rebills, across more than one processor?
  4. Does configuring the proxy or its routes move us from SAQ A toward SAQ A-EP under PCI DSS 4.0.1 (I9)?
  5. Can we take tokens back and route externally, or must every call pass through the vault's proxy?
  6. What happens when the vault is unavailable: dual-write at capture, direct processor fallback, and recurring continuity?
  7. Which objects are first-class beyond cards: bank accounts with mandates, identity documents, tax IDs, issued-card data, wallet credentials?
  8. Where does data sit at rest, in which regions, and who holds the keys?
  9. What is charged per store, forward, retrieve and per account-updater update, and is there a subprocessor list and a current PCI DSS attestation and SOC 2 report?
  10. Who decides which bank, issuer and rail a creator lands on, and can that rule change without a deployment?
- Source line: Standard vault evaluation criteria; PCI SSC guidance, 26 Mar 2025; Visa Intelligent Commerce Connect release, 8 Apr 2026 (I18).
- Speaker notes: These are the questions that decide vault RFPs in our experience, and we would rather you ask them of us first. Questions two, six and ten are the ones that separate vendors most: what leaves with you, what happens in an outage, and who holds the decision. We answer all ten in Sections 06 and 07 with a label on each answer, and we list the ones we cannot yet answer in writing as open items with an owner.

### Slide 04.4 (optional, use if Section 04 needs a closing beat)
- Kicker: WHAT THE RFP HAS TO COVER · FOUR EXTERNAL CLOCKS ALREADY RUNNING
- Headline: Four external clocks set the pace for Phase 1: PCI 4.0.1 is live, the GENIUS Act takes effect by January 2027, the networks are tokenizing everything by 2030, and agent credentials arrived in 2025.
- Body (stat tiles):
  * 31 Mar 2025 · PCI DSS 4.0.1 script controls became mandatory (I9)
  * 18 Jan 2027 · latest effective date of the GENIUS Act, or 120 days after final rules; OCC yield rule still proposed (I21, I23)
  * 2030 · Mastercard's goal to tokenize all online transactions (I13)
  * 2025 · Visa Intelligent Commerce, Mastercard Agent Pay and Visa's Trusted Agent Protocol launched (I16, I17, I20)
- Source line: PCI SSC, Mar 2025; Paul Hastings, Mar 2026; Digital Transactions, Nov 2024; Visa and Mastercard newsrooms, Apr and Oct 2025.
- Speaker notes: None of these clocks is set by a vendor. They are the reason to scope the vault for bank, identity and agent credentials now rather than after Phase 1, and they are the dates we use in Section 08 when we propose the phases.

---

## TO CONFIRM list for German (before build)
1. C7 wording: "active creators" and "active fan accounts" versus the filing's own terms; open the 20 Sep 2026 accounts at Companies House if possible.
2. C28: extend the traffic list to ten countries from Similarweb Pro; the public page shows five.
3. I14: open the Mastercard Europe June 2026 release to confirm "three in five"; otherwise drop that clause and keep I13.
4. C24 and U9: open Keily Blair's May 2026 LinkedIn post; if the "underserved by traditional financial institutions and products" line is there, it can replace the Bloomberg paraphrase on slide 02.1 with a dated quote.
5. Design facts on slides 01.1, 04.2: confirm with Samuel that the six design points are exactly what OnlyFans said.
6. P7 and P14 stay off the slides unless OnlyFans confirms accepted brands, 3DS and payout rails.
7. Slide 04.3 question 9 mentions a PCI DSS attestation and SOC 2 report; make sure Section 06 or the appendix actually states what Yuno can provide, with its label.
