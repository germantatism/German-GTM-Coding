# Eventbrite Pre-Questions Bank: Yuno <> Eventbrite Call — FINAL (v3)

**2026-08-04, 16:30 COT. Attendee: Paul Pasion (Eventbrite). Yuno: German, Justo, Jarrett.**
**v2 status:** reviewed by the internal Yuno knowledge agent (avg quality 7.9/10). 8 answers corrected (Q2, Q8, Q9, Q28, Q37, Q51, Q57, Q59), conditional-promise rule applied (Q39, Q41, Q48, Q51: no dated commitments without a confirmed owner), 4 questions added from the gap check (Q61 to Q64). All OPEN items and ⚠️ statuses REMAIN OPEN: the review validated wording, not internal facts; Section 0 still needs Justo + Jarrett.
**v3 additions:** Yuno for Platforms capability brief (internal agent, public-docs based) added as Appendix B, plus 6 product-model questions (Q65 to Q70) derived from it.
Paste-ready for the "pre questions" tab of the meeting brief doc. Companion research: `eventbrite-platform-deepdives-2026-08-04.md`.

**Their verbatim ask:** "For reference, we are currently speaking with several other orchestrators. During our call, we would like to see specific examples of how your integrations with PayPal (Braintree), Stripe, Adyen, and JPM Chase support marketplace use cases."

**How to read this doc:** every question has a spoken answer (what you say out loud, English, senior AE register), technical backup, a status, and a source. Statuses: ✅ verified (public docs or hard internal evidence), ⚠️ partial (capability verified but details need internal confirmation), OPEN (do not answer in the call until resolved; the resolution owner is named). Facts marked **INTERNAL** must never be quoted to Eventbrite verbatim (volumes, client architecture details) without permission.

---

## SECTION 0. OPEN ITEMS: RESOLVE WITH JUSTO + JARRETT BEFORE 16:30

1. **JPM connector status as of today.** Internal evidence: the JPMORGAN provider was configured as a mock (yunotestpaymentgw, not live) as of 2026-05-11, and a separate JPM cards integration was reported in build in March 2026. Get the current status and the exact sentence Jarrett is comfortable saying. This decides how Q31 is answered. CRITICAL.
2. **Exact GA scope of the marketplace (Recipients) product per provider.** Internal picture: Stripe in production, Adyen in production and being extended, PayPal/Braintree marketplace in build. Confirm what can be shown live in a demo and what is roadmap, with dates.
3. **Permission to name GoFundMe** as the live marketplace reference, and at what level of detail (client name only vs architecture vs reference call).
4. **Uptime, SLA, p99 added latency, status page.** No public numbers exist. Needed for Q41 to 45.
5. **Pricing shape at 79M paid tickets / $3B GTV.** Per-transaction model, what counts as billable, retry billing. Q46.
6. **Auth-rate uplift data segmented by baseline** (merchants who came from in-house multi-PSP routing vs single PSP). Q52.
7. **Payout rails beyond the documented 17 countries** (public payout API enum is US + LATAM heavy; Eventbrite pays out in 21 countries incl. UK, EU, AU, SG, HK). Q21, Q24.
8. **Network token coverage by scheme and market + account updater story.** Q33, Q56.
9. **Braintree connector documented scope** (public partner page was removed; nothing on docs.y.uno). Q4.
10. **Data residency specifics** (EU, UK, Brazil, Mexico). Q39.
11. **SOC 1 / insurance / escrow posture** for vendor-risk questions. Q40.
12. **Sandbox with marketplace features enabled** ready to share same-week if Paul asks for hands-on. Q51.

---

## THE TOP 15 MUST-REHEARSE QUESTIONS

Q1, Q2, Q5, Q6, Q9, Q11, Q16, Q21, Q22, Q25, Q26, Q31, Q41, Q50, Q54. They are marked inline below.

---

# CATEGORY A. CONNECTOR DEPTH PER PROCESSOR

### Q1. [MUST REHEARSE] "For each of Stripe, Braintree, and Adyen: are your connectors built on the platform/marketplace flavor of the API, meaning Stripe Connect, PayPal's multiparty products, Adyen for Platforms, or only on the vanilla acquiring APIs?"
**Why they ask:** They run as MoR on Stripe Connect today; a card-only connector is disqualifying. This is the heart of their written ask.
**A (spoken):** "Three different depths, and I want to be precise rather than tell you we support everything. On Stripe, we operate the Connect model in production through our marketplace product: recipient onboarding to connected accounts, split payments with platform fees, transfers and transfer reversals. On Adyen, we also run platform flows in production, including hosted onboarding and split payments, and we are actively extending that connector's marketplace surface. On the PayPal side, Braintree acquiring and PayPal wallet are standard scope; the multiparty marketplace layer is in active development right now. JPM I'll answer separately because you named it deliberately, and it deserves a straight answer."
**Backup:**
- Yuno's documented marketplace feature: Split Payments Marketplace + full Recipients API (create/onboard/block recipients, transfers, reverse transfers). https://docs.y.uno/docs/payment-features/split-payments-marketplace
- **INTERNAL:** GoFundMe live in production since 2026-02-19 on exactly these Stripe Connect flows (connected accounts created via Yuno, application fees, transfer reversals, delayed capture) and Adyen platform flows (hosted onboarding, splits on ACH). PayPal marketplace being built for GoFundMe now.
- Docs caveat to respect: "Yuno acts solely as the orchestrator of the payment, not the processor. Ensure your provider supports split payments."
**Status:** ⚠️ partial (capabilities verified internally; exact per-provider GA wording needs Jarrett, open item 2)
**Source:** docs.y.uno split-payments-marketplace; internal Slack (#product-tech, #go-live, Feb-Aug 2026)

### Q2. [MUST REHEARSE] "On Stripe specifically: can a payment created through Yuno target one of our existing connected accounts, with destination, application fee, and statement descriptor fields passed through? Or do we re-paper every organizer?"
**Why they ask:** Organizers sign the Stripe Connected Account Agreement; re-onboarding the creator base is commercially unacceptable.
**A (spoken, FINAL):** "Nobody gets re-papered. Your organizers exist as recipients in Yuno, each linked to your provider connections, including existing Stripe connected accounts, and the split carries purchase, commission, and fee components through Stripe's transfer mechanics. Agreements, KYC status, and payout schedules stay exactly where they are. On the exact field-level pass-through, destination, application fee, statement descriptor, I'll give you the field map in the technical session rather than improvise API fields on a call; the model is that we sit in front of the charge, not inside your Connect relationship."
**Backup:**
- Recipients link to one or more provider connections; split types PURCHASE, COMMISSION, PAYMENTFEE, VAT, MARKETPLACE, with liability fields for processing fee and chargebacks. https://docs.y.uno/docs/payment-features/split-payments-marketplace
- **INTERNAL:** GFM flows use application_fee_amount and transfer_data on Stripe through Yuno; onboarding transfers between recipients exist (POST /v1/recipients/{id}/onboardings/{id}/transfer).
- ⚠️ Confirm with Jarrett whether on_behalf_of and statement descriptor pass-through are exposed field-level today. Do not improvise field names in the call.
**Status:** ⚠️ partial (model verified; exact field matrix needs Jarrett)
**Source:** docs.y.uno recipients-for-marketplace; internal Slack

### Q3. "On Adyen: do you integrate the Checkout API and Adyen for Platforms with balance accounts and splits, or only standard ecommerce payments? Named live customer?"
**Why they ask:** Adyen's role in their stack is undisclosed strategic optionality; vendors routinely demo plain ecommerce and call it marketplace support.
**A (spoken):** "Both layers. Standard Adyen acquiring is fully supported for routing, and on the platforms side we run Adyen hosted onboarding for sub-merchants and split payments in production today, including on bank-debit rails, not just cards. I'd rather be precise than oversell: parts of the Adyen platform surface are still being extended, and I can walk you through exactly which capabilities are live versus in progress in the technical session. We do have a live marketplace merchant running this in production."
**Backup:**
- Adyen listed live in Yuno's public catalog: 52 countries, network tokenization, 3DS, recurring. https://y.uno/integrations
- **INTERNAL:** GFM on Adyen via Yuno: hosted onboarding links (with cross-border payout flags), ACH via Plaid with split_marketplace objects, live since late 2025. Jarrett: Adyen marketplace functionality "being built out more."
**Status:** ⚠️ partial (live evidence internal; GA wording needs Jarrett)
**Source:** y.uno/integrations; internal Slack

### Q4. "On Braintree: do you support the vault, marketplace constructs, and PayPal wallet through the same connector? Which Braintree features are not exposed?"
**Why they ask:** Braintree carries their PayPal volume in 8 markets; losing wallet or vault features in the abstraction is a hidden cost.
**A (spoken):** "Braintree acquiring routes through Yuno like any other processor connection, and PayPal as a wallet is supported both natively and through processor rails. Two honest notes. First, Braintree's own marketplace product was closed to new platforms by PayPal years ago, so nobody's 'Braintree marketplace' connector means much today; the current PayPal answer is their multiparty product, and our support for that layer is in active development. Second, on vault: Braintree officially exports card data free of charge, including network transaction IDs, to any PCI Level 1 recipient, so your Braintree-vaulted cards can be mirrored into our vault without cardholder re-consent."
**Backup:**
- Braintree Marketplace closed: new platforms told to contact Sales, was US-only; agreement scrubbed from Braintree legal terms 2024-11-07. https://developer.paypal.com/braintree/docs/guides/braintree-marketplace/overview
- Braintree data portability: free export, GPG CSV incl. network transaction identifiers, max two exports; Apple Pay / Google Pay tokens NOT transferable. https://developer.paypal.com/braintree/articles/get-started/data-migration/overview
- ⚠️ Yuno's Braintree connector has no public docs page (partner page removed); get the internal feature matrix from Jarrett. **INTERNAL:** PayPal marketplace layer in build.
**Status:** OPEN on Yuno-side Braintree scope (open item 9); ✅ on the Braintree-side facts
**Source:** developer.paypal.com; internal Slack

### Q5. [MUST REHEARSE] "Walk me end to end through a ticket order in your marketplace model: who is merchant of record, where does the split happen, where does our platform fee get carved out, and what does the processor see?"
**Why they ask:** This is the exact sentence from their email. Generic routing slides here are disqualifying.
**A (spoken):** "The buyer pays at your checkout. Yuno routes the authorization to whichever of your processor connections your routing rules pick, by market, BIN, cost, or health. The payment request carries the split: the organizer's share, your commission, and the processing fee, each typed separately. The processor that wins the route executes that split on its own rails, Stripe transfers on Connect, Adyen splits on their platform layer. Funds settle from the processor directly to you, exactly as today. You remain merchant of record everywhere; Yuno is never in the funds flow, we are the orchestration and data layer. Your ledger stays the source of truth for creator balances; we feed it clean, per-processor, per-organizer data."
**Backup:**
- Split flow and validations (splits must sum to payment amount, currency match, recipients onboarded). https://docs.y.uno/docs/payment-features/split-payments-marketplace
- Verbatim docs line to quote if pressed: "Yuno acts solely as the orchestrator of the payment, not the processor."
**Status:** ✅ verified (documented model)
**Source:** docs.y.uno split-payments-marketplace

### Q6. [MUST REHEARSE] "Sub-merchant onboarding: if I onboard an organizer once with Yuno, is that organizer usable across Stripe, Adyen, and a future JPM connection, or do I run KYC per processor?"
**Why they ask:** This is where marketplace-orchestration claims usually collapse, and their WIN condition is an honest answer.
**A (spoken):** "Honest answer: the organizer exists once in Yuno as a recipient, one canonical record with one onboarding workflow and status tracking. But KYC itself is executed by each provider, because Stripe and Adyen each carry the regulatory obligation for accounts on their rails; no orchestrator can legally make one KYC pass cover both. What we remove is the integration and operational burden: one API to onboard, monitor statuses, block, and even transfer onboardings between recipients in a controlled, reversible way. In practice you onboard where you need the organizer to be paid, which today is Stripe, and add providers only where it earns something."
**Backup:**
- Recipients architecture: Organization, Account, Connections, Recipients; each recipient links to one or more provider connections; onboarding statuses CREATED to SUCCEEDED/DECLINED/BLOCKED; Transfer Onboarding endpoints documented. https://docs.y.uno/docs/payment-features/split-payments-marketplace and https://docs.y.uno/reference/recipients-for-marketplace/create-recipient-1
**Status:** ✅ verified (documented; the honest boundary is the right answer)
**Source:** docs.y.uno

### Q7. "Feature parity: what percentage of each processor's surface do you cover: network tokens, L2/L3, incremental auth, multicapture, account updater? What do we lose with you in the middle?"
**Why they ask:** Orchestrators are lowest-common-denominator by construction; they want the gaps named unprompted.
**A (spoken):** "We won't claim full parity; no orchestrator honestly can. What I can tell you is documented: we run our own network token layer with Visa, Mastercard and Amex, card account updater, delayed and partial capture, and provider-specific pass-through where merchants need a processor feature we haven't abstracted. The right way to answer this properly is a per-processor feature matrix against the specific features you use today, which I'd like to make deliverable one of the working session. Tell us which Stripe and Braintree features you lean on and we will map them line by line."
**Backup:**
- Network tokens: Yuno-procured from Visa/MC/Amex, bring-your-own supported, cryptogram API, Card Account Updater. https://docs.y.uno/docs/security-and-compliance/network-tokens and https://y.uno/en/product/token-vault
- **INTERNAL:** delayed capture (separate authorize + capture) live for GFM on Stripe.
- ⚠️ L2/L3, incremental auth, multicapture per connector: not publicly documented; do not claim.
**Status:** ⚠️ partial
**Source:** docs.y.uno; y.uno

### Q8. "Do you support Mercado Pago as we use it in Mexico and Argentina, and can you switch on the local rails we have flagged off: OXXO, boleto, Rapipago, Pago Facil, installments, Pix?"
**Why they ask:** Card-only checkout in MX/AR/SG/HK is their biggest conversion gap; this is the growth story.
**A (spoken):** "Yes, Mercado Pago is a documented connector for us, wallet and checkout flows included, and LatAm is where Yuno is strongest, it is where we were born. OXXO, boleto, Rapipago, Pago Facil, Pix, and installment programs like meses sin intereses are standard methods in our catalog through local processors. And from what's visible in your own checkout, much of this is activation, not construction; the plumbing for these methods is closer than you may think. The one piece I want to flag honestly is settlement timing: cash vouchers settle days later, which interacts with your five-day post-event payout clock, and we should design that together in the working session."
**Safety rule:** never say "we probed your checkout payload" in any form; "from what's visible in your checkout" at most.
**Backup:**
- Mercado Pago in Yuno docs since 2020: Checkout Pro, wallet enrollment, antifraud. https://docs.y.uno/changelog/android
- Dormant Eventbrite flags verified 2026-08-03: should_accept_oxxo, rapipago, pagofacil, boleto_bancario, maxInstallments (meeting brief).
- Catalog claim: 1,000+ providers, 190+ countries. https://y.uno/integrations
**Status:** ✅ verified (connector + dormant flags); ⚠️ exact method-by-market list for the follow-up
**Source:** docs.y.uno changelog; meeting brief probes

### Q9. [MUST REHEARSE] "If a transaction fails over between processors, what happens to the split configuration, the connected account attribution, and the payout mapping? Failover on a marketplace is not just re-authing a card."
**Why they ask:** They built failover in-house precisely because naive retry breaks funds attribution. This question separates real marketplace orchestration from card-retry demos.
**A (spoken):** "You're right, and this is exactly why marketplace failover has to be recipient-aware. In our model the retry can only cascade to a connection where that organizer is onboarded as a recipient; the split is then re-expressed in the winning processor's own split mechanics. Where the organizer exists on only one processor, routing pins to it, no blind cascading. So failover and splits compose, but by design, not magic: you decide which organizers are multi-homed and which are pinned. We run this recipient-aware model in production with a live marketplace merchant today, and I'd love to walk the concrete failure cases with your team in the deep dive, because the edge cases are where we've done the real work."
**Backup:**
- Split validation requires all recipients onboarded on the connection. https://docs.y.uno/docs/payment-features/split-payments-marketplace
- Routing: outcome paths per connection for Declined/Error with chained next steps. https://docs.y.uno/docs/using-yuno/dashboard-overview/routing
- **INTERNAL:** GFM runs Stripe + Adyen with recipients on both; known bug history (split data lost on 3DS, fixed via payment-event-orc#787) shows the edge cases are real and worked.
**Status:** ⚠️ partial (verify exact retry-split behavior with Jarrett before promising specifics)
**Source:** docs.y.uno; internal Slack

### Q10. "Who maintains connectors when a processor ships a breaking change? What is your update SLA and can we pin versions?"
**Why they ask:** With in-house failover they control change management; an orchestrator can break checkout on its own release schedule.
**A (spoken):** "Connector maintenance is the product; it is what you stop paying for in engineering time. Our platform publishes changelogs, and provider API changes are absorbed by us behind a stable Yuno API, that is the contract. On formal update SLAs and version pinning per merchant, I want to give you the precise policy in writing rather than approximate it live, so let me take that as a follow-up with our platform team."
**Backup:**
- Public SDK changelogs exist (https://docs.y.uno/changelog/android). Formal connector-update SLA: not public.
**Status:** OPEN (formal SLA and pinning policy: Justo/product)
**Source:** docs.y.uno changelog

---

# CATEGORY B. MARKETPLACE CORE

### Q11. [MUST REHEARSE] "Does Yuno sit in the funds flow at all, or does money still settle directly from Stripe, Braintree and Adyen into our accounts exactly as today?"
**Why they ask:** A vendor in the money flow changes regulatory posture, float, and counterparty risk for a $278M creator payable.
**A (spoken):** "We are never in the funds flow. Full stop. Yuno is a technical orchestration layer: funds settle from your processors directly into your accounts, on the same rails and timelines as today. We are not a money transmitter in your flow, we hold no balances, and if Yuno disappeared tomorrow your money would be exactly where it is now. That is also why your merchant-of-record status, your float, and your treasury model do not change by adopting us."
**Backup:**
- Docs: "Yuno acts solely as the orchestrator of the payment, not the processor." https://docs.y.uno/docs/payment-features/split-payments-marketplace
- Consistent with the official positioning (orchestration across methods, processors, antifraud, reconciliation).
**Status:** ✅ verified
**Source:** docs.y.uno

### Q12. "Is there a first-class sub-merchant object that payments, refunds, chargebacks and payouts all attribute to, or do we encode creators in metadata?"
**Why they ask:** If creators are metadata strings, all downstream reconciliation and payout logic stays theirs to build.
**A (spoken):** "First-class. The recipient is a real object in our API: it has its own lifecycle, onboarding state per provider connection, and it is what splits, transfers, and reverse transfers reference. It is not a metadata convention. That is the difference between a marketplace product and a routing product with a tag field, and frankly it is the reason we get invited to conversations like this one."
**Backup:**
- Full Recipients API suite: create/get/update/delete/list, onboarding lifecycle, block/unblock, transfers. https://docs.y.uno/reference/recipients-for-marketplace/create-recipient-1
**Status:** ✅ verified
**Source:** docs.y.uno

### Q13. "How do you represent splits between platform fee and creator proceeds at authorization, and does that survive partial refunds?"
**Why they ask:** Split accounting with partial refunds is where marketplace abstractions break; ticketing refunds are frequent and partial.
**A (spoken):** "Splits are typed at payment creation: purchase amount to the organizer, commission to you, payment fee, tax if needed, each with explicit liability assignment for processing fees and chargebacks. Refunds, including partials, are split-aware: the refund carries its own split instruction so you control whose share funds it. I'll be honest that partial refunds across multi-component orders are the hardest surface in any marketplace stack; it is an area where we have hardened the product in production with a live merchant, and I would rather show you the actual behavior in sandbox than hand-wave it."
**Backup:**
- Split types + liability fields documented. https://docs.y.uno/docs/payment-features/split-payments-marketplace
- **INTERNAL:** GFM refund flows declare recipient_id for refund sourcing (Adyen), partial-refund split miscount bug found and fixed Jul 2026. Do not quote; it informs the "hardened in production" phrasing.
**Status:** ⚠️ partial (behavior verified internally; demo-ready state needs Jarrett)
**Source:** docs.y.uno; internal Slack

### Q14. "Partial refunds and organizer-funded refunds: who claws back the organizer's share, what if their balance is insufficient, and what happens to your platform fee on refund?"
**Why they ask:** They hold a $10.5M reserve and offset rights; they need to know if the model supports clawback.
**A (spoken):** "The split on the refund decides who funds it, so organizer-funded refunds express naturally. Insufficient organizer balance is a processor-ledger question: on Stripe that is transfer reversals against the connected account, on Adyen it is their negative-balance mechanics, and your offset rights against future sales remain your ledger's logic, which we feed with per-organizer, per-processor data rather than replace. Commission treatment on refund is configurable per refund instruction. Where I'd focus the working session is your advance-payout scenario: refunds after money has left are a design conversation, not a checkbox, and I'd rather engineer it with you than claim it is free."
**Backup:**
- Stripe: reverse_transfer on refunds; negative balance offsets; 180-day zero-out. https://docs.stripe.com/connect/account-balances
- Adyen: refund splits decide funding; platform liable account backstops negatives after 30 days. https://docs.adyen.com/marketplaces/split-transactions/split-refunds
**Status:** ⚠️ partial
**Source:** docs.y.uno; docs.stripe.com; docs.adyen.com

### Q15. "Which of your live customers run our exact model: marketplace MoR holding funds with delayed payout to sellers, at what volume?"
**Why they ask:** Most orchestrator references are linear ecommerce, not fund-holding marketplaces.
**A (spoken):** "We have a live marketplace merchant in production on exactly this shape: platform as merchant of record, sub-merchant onboarding, split payments including tips and fees, transfers and refund reversals, running across two of the same processors you named. It went live in February this year and has scaled every month since. Subject to their approval I'm happy to name them and set up a reference conversation, and I'd rather do that than say a name in a first call without their permission; you'd want the same discretion from us."
**Backup:**
- **INTERNAL:** GoFundMe, live 2026-02-19, first Marketplace-solution merchant, ramp 25K (Feb) to 468K (Apr) monthly transactions, expected 3.5M to 10M at full ramp. GoFundMe is publicly named as a Yuno client on y.uno homepage, so the name itself is public; architecture details need permission (open item 3).
- Also **INTERNAL**: split payments live with Pagar.me in Brazil; Zoop connector extension in build (Ze Delivery).
**Status:** ⚠️ partial (permission pending)
**Source:** y.uno homepage; internal Slack

---

# CATEGORY C. FUNDS FLOW, LEDGER, RECONCILIATION

### Q16. [MUST REHEARSE] "If Yuno is in the middle, what do we reconcile against: your ledger or the raw processor settlement files? Do you deliver a normalized settlement report?"
**Why they ask:** They reconcile per-processor settlement files against ticket-level records to support a $278M creator payable. A third source of truth that replaces nothing makes their close worse.
**A (spoken):** "The processors' settlement files remain the financial source of truth, and your ledger remains the creator-balance source of truth; we do not insert a third authority. What Yuno adds is a reconciliation product that does the matching for you: our transaction records against each provider's settlement files against acquirer balances, with per-transaction statuses, conflict flagging, and settlement reports through a Reports API. So instead of your team normalizing five file formats, you consume one reconciled, transaction-level view per processor and per organizer, and exceptions surface instead of hiding."
**Backup:**
- Reconciliation docs: matches Yuno transactions vs provider settlement files vs acquirer balances; statuses Reconciled / Non reconcilable / Not reconciled / Conflict; transaction + settlement reports. https://docs.y.uno/docs/using-yuno/dashboard-overview/reconciliations
- Reports API. https://docs.y.uno/reference/reports/create-a-report
**Status:** ✅ verified (product documented); ⚠️ file formats/cadence detail for follow-up
**Source:** docs.y.uno reconciliations

### Q17. "When one organizer's sales run across two processors, how do I get a unified per-organizer view of gross, fees, refunds, chargebacks for payout calculation?"
**Why they ask:** Their payout engine needs one number per organizer per event; routing fragments it unless the layer aggregates correctly.
**A (spoken):** "That is precisely what the recipient object gives you. Because every split payment, refund, and transfer references the recipient, our reporting can cut across processors by organizer, at transaction level, exportable to feed your payout engine. The processor becomes an attribute of the transaction rather than a silo. That is the practical difference between orchestrating a marketplace and orchestrating cards."
**Backup:**
- Recipient-scoped transfers/listing endpoints documented. https://docs.y.uno/reference/recipients-for-marketplace/create-recipient-1
- ⚠️ Confirm export formats and whether per-recipient rollups are dashboard-native today or via Reports API.
**Status:** ⚠️ partial
**Source:** docs.y.uno

### Q18. "How do timing differences between authorization through you and settlement at the processor surface? If the processor later rejects, reverses, or settles a different amount, how fast do we see it?"
**Why they ask:** Break-timing between orchestration layer and settlement is where ledger discrepancies hide.
**A (spoken):** "Status changes propagate by webhook through the payment lifecycle, and the reconciliation layer is the backstop: when a settlement file disagrees with the transaction record, it lands as a conflict instead of silently passing. You get both the real-time stream and the batch truth, and the deltas between them are surfaced as work items, not surprises. On exact conflict-surfacing SLAs I'll bring the specifics in the follow-up."
**Backup:**
- Reconciliation conflict status documented. https://docs.y.uno/docs/using-yuno/dashboard-overview/reconciliations
**Status:** ⚠️ partial (SLA detail OPEN)
**Source:** docs.y.uno

### Q19. "Can every transaction carry our event ID, creator ID, and payout batch so we can roll the creator payable forward daily from your data?"
**Why they ask:** The $101M advance-payout balance and payable roll-forward are audit-critical; payment-level-only data does not help.
**A (spoken):** "Yes on the two identities that matter: the recipient is first-class, and payments carry merchant metadata end to end, so event and batch identifiers flow through to reports and webhooks. I want to confirm cardinality and retention limits on metadata before you design an audit process on it, so let me take that specific point to the technical session."
**Backup:**
- ⚠️ Metadata limits not verified in public docs; do not promise specifics.
**Status:** ⚠️ partial
**Source:** docs.y.uno

### Q20. "We pay out only in the collection currency, no FX. Does anything in your routing or settlement layer ever introduce a currency conversion we did not ask for?"
**Why they ask:** Silent FX from routing would break their published creator terms.
**A (spoken):** "No. Routing respects settlement currency as a constraint: currency is a first-class routing condition, so you can pin any market to connections that settle in the collected currency. We do not convert funds, we never touch funds. Your no-FX policy is a routing rule, not a hope."
**Backup:**
- Routing conditions include currency, amount, origin, issuer country. https://docs.y.uno/docs/using-yuno/dashboard-overview/routing
- Split validation requires currency match. https://docs.y.uno/docs/payment-features/split-payments-marketplace
**Status:** ✅ verified
**Source:** docs.y.uno

---

# CATEGORY D. PAYOUTS

### Q21. [MUST REHEARSE] "Do you orchestrate the payout leg at all: disbursements to creator bank accounts across our 21 payout countries? Live in production or roadmap?"
**Why they ask:** Payouts are the most overclaimed area in this market; a vague answer is disqualifying by their own criteria.
**A (spoken):** "Straight scope answer. Yes, Yuno has a payouts product live in production: bank transfers, push to card, and wallet payouts, and we run recipient transfers for a live marketplace merchant today. Where I will be precise: our deepest documented payout coverage today is the Americas, the United States plus Latin America. For your current 21-country payout footprint, our recommendation is not to touch what works: creator payouts stay on Stripe Connect and your rails, and we orchestrate the pay-in leg. Where payouts become interesting with us is expansion, Latin America in particular, and I'd rather earn the payout conversation market by market than claim 21 countries on day one."
**Backup:**
- Payouts product documented: bank/card/wallet/referenced payouts; API country enum: AR, BO, BR, CL, CO, CR, EC, SV, GT, HN, MX, NI, PA, PY, PE, US, UY (17). Methods incl. PIX_PAYOUT, PAYPAL_PAYOUT. https://docs.y.uno/docs/payouts and https://docs.y.uno/reference/payouts/create-payout
- Marketing claims 190+ countries; the API reference is the technical truth. Do not quote 190+ for payouts.
- **INTERNAL:** GFM beneficiary transfers live (with active issue being fixed on Stripe MCC updates, 2026-08-03; do not volunteer).
**Status:** ✅ verified (scope as stated); OPEN on any coverage beyond the 17 (open item 7)
**Source:** docs.y.uno payouts

### Q22. [MUST REHEARSE] "If we keep payouts exactly as they are on Stripe and our own rails, does your orchestration interfere with them in any way?"
**Why they ask:** Do-no-harm: they will not destabilize a payout machine moving billions to creators.
**A (spoken):** "No interference by design, with one nuance I want to put on the table because your team will find it anyway. If a charge is processed on Stripe, your Connect balance funds transfers exactly as today. If routing sends a US charge to a different acquirer, those funds settle to your bank, not your Stripe balance, so payouts funded from the Stripe balance need a treasury bridge; Stripe supports top-ups from external funds for exactly this. That is a design decision per market: many merchants pin Stripe-payout markets to Stripe acquiring initially and route markets where payouts do not depend on the acquirer. We will not pretend that coupling does not exist; we design around it with you."
**Backup:**
- Stripe top-ups: "Adding funds from non-Stripe income" explicitly supported; GA US/UK/Japan, preview EU/CA/AU/NZ; ACH credit 1-3 days, wires 1-5 days. https://docs.stripe.com/connect/top-ups
- Also relevant: instant payout eligibility depends on Stripe balance (Q23).
**Status:** ✅ verified (this is the sophisticated, honest answer)
**Source:** docs.stripe.com/connect/top-ups

### Q23. "If we route a creator's pay-ins away from Stripe, what happens to their Instant Payout eligibility, which depends on their Stripe balance?"
**Why they ask:** Tests whether the vendor understands coupled pay-in and payout balances.
**A (spoken):** "Exactly the coupling I just described, and the honest pattern is: creators who use Instant Payout stay pinned to Stripe acquiring, or you fund the balance via top-ups and accept the float. Routing rules make that a per-segment decision, you can pin by recipient. Longer term, if instant payouts matter internationally, there are bank rails and push-to-card options worth evaluating, but I would not sell you a Stripe-decoupled instant payout today as if it were free."
**Backup:**
- Stripe Instant Payouts: 1% fee, $9,999/payout cap USD, platform can surcharge (Eventbrite charges 3%). https://docs.stripe.com/connect/instant-payouts
**Status:** ✅ verified
**Source:** docs.stripe.com

### Q24. "Could you help us extend instant payouts beyond the US, and who carries funds and FX risk in that model?"
**Why they ask:** Instant Payout at 3% is a revenue line and a creator-retention lever.
**A (spoken):** "It is a genuine expansion path, and the answer depends on the market: in Latin America we have live payout rails today, Pix payouts in Brazil for example, and funds always move processor-to-recipient, never through Yuno, so FX and settlement risk stay with the licensed provider. For Europe and APAC I want to scope provider by provider rather than claim a map. What I can commit to: we bring the payout providers to one API, and you keep the pricing power you have today over the payout experience." (Do not spell out their 3%-over-1% margin arithmetic; it is public math, let them do it.)
**Backup:**
- PIX_PAYOUT, STP_PAYOUT (MX), NEQUI/TRANSFIYA (CO) documented. https://docs.y.uno/reference/payouts/create-payout
- Stripe's 1% instant fee vs Eventbrite's 3% pricing: https://docs.stripe.com/connect/instant-payouts
**Status:** ⚠️ partial
**Source:** docs.y.uno; docs.stripe.com

---

# CATEGORY E. MIGRATION AND COEXISTENCE

### Q25. [MUST REHEARSE] "We built our own failover and it works. Can Yuno run in shadow or passthrough mode on a small slice per country while our routing stays primary, and how do we roll back instantly?"
**Why they ask:** No big-bang cutover of a $3B checkout. The answer reveals whether we have done enterprise migrations.
**A (spoken):** "Yes, and that is exactly how we would start. Routing in Yuno supports percentage-based traffic splits per connection, so phase one is a small slice in one market, with your existing integrations untouched and rollback being a routing rule change, effectively instant, no deploy. You compare authorization rate, latency, and settlement behavior side by side before Yuno makes a single routing decision that matters. We would also agree the rollback criteria upfront in writing. You are not buying a leap of faith; you are buying a controlled experiment that earns each next percent of traffic."
**Backup:**
- Manual percentage splits per connection documented ("define the exact percentage of transactions to route through each connection"), usable for A/B. https://docs.y.uno/docs/using-yuno/dashboard-overview/routing
- Named enterprise migration reference: OPEN (ask Justo which logo fits).
**Status:** ✅ verified (mechanism); OPEN (reference)
**Source:** docs.y.uno routing

### Q26. [MUST REHEARSE] "Our cards are vaulted with Stripe and Braintree. Do stored credentials keep working without re-authorization? Do you force vaulting with Yuno? What survives a migration?"
**Why they ask:** Forced re-vaulting kills returning-buyer conversion; vault lock-in is the dependency they are trying to remove.
**A (spoken):** "Both Stripe and Braintree have official card-data export processes to PCI Level 1 recipients, and Yuno is PCI DSS Level 1 with documented inbound token migration, so vaulted cards mirror into our vault without cardholder re-consent. Braintree's export explicitly includes network transaction IDs, which is what keeps stored-credential compliance intact. Going forward, network tokens make credentials processor-agnostic at the scheme level. Two honest caveats: Stripe excludes Link-saved credentials from any export, and Apple Pay and Google Pay device tokens are never portable from anyone, they re-provision. And the same door exists on the way out: our token export process is documented, PGP-encrypted, to any PCI Level 1 destination. We win by performance, not by hostage-taking."
**Backup:**
- Stripe PAN export policy (PCI L1 recipient, PGP; Link excluded). https://docs.stripe.com/get-started/data-migrations/pan-export
- Braintree free export incl. network transaction identifiers; Apple Pay/Google Pay tokens excluded. https://developer.paypal.com/braintree/articles/get-started/data-migration/exports
- Yuno inbound migration + outbound export documented. https://docs.y.uno/docs/security-and-compliance/data-migration-processes/exporting-tokens-from-yuno
- Yuno network tokens (Visa/MC/Amex) + Card Account Updater. https://docs.y.uno/docs/security-and-compliance/network-tokens
**Status:** ✅ verified
**Source:** docs.stripe.com; developer.paypal.com; docs.y.uno

### Q27. "How much of our existing Stripe Connect creator onboarding flow has to be rebuilt versus left in place in phase one?"
**Why they ask:** The onboarding flow is legally and operationally entangled with Stripe; rebuilding it is a large hidden cost.
**A (spoken):** "In phase one: none of it. Pay-in orchestration does not require touching organizer onboarding; your Connect flow, the agreement acceptance, the verification, all stays. Recipients in Yuno become relevant only when you want split payments or multi-processor flows for a given organizer, and even then we link to existing connected accounts rather than recreate them. Onboarding migration is never a prerequisite; it is an option per organizer segment."
**Backup:**
- Recipients link to existing provider connections. https://docs.y.uno/docs/payment-features/split-payments-marketplace
**Status:** ✅ verified (model); ⚠️ confirm "link to pre-existing connected account" mechanics with Jarrett
**Source:** docs.y.uno

### Q28. "What did your fastest and slowest enterprise implementations actually take, and what made the slow one slow?"
**Why they ask:** Small post-acquisition team; a 12-month, 10-engineer integration is not viable.
**A (spoken, FINAL):** "I'll give you real numbers with our delivery team as a follow-up rather than a brochure answer. Directionally, from public cases: inDrive stood up 10 new countries in under 8 months on our layer. Slow implementations in this industry always have the same cause, underestimating funds-flow design, which is exactly why we start there with you, not with the SDK."
**Backup:**
- inDrive: 10 countries <8 months, ~90% approval quote. https://y.uno/en/success-stories/indrive
- **INTERNAL:** GFM timeline: integration work visible from ~Aug 2025 (shared Stripe channel), live 2026-02-19.
**Status:** ⚠️ partial (real timeline table OPEN with delivery)
**Source:** y.uno success stories; internal Slack

### Q29. "During a phased migration, how do we reconcile a split world: two ID schemes, two webhook streams, one creator ledger?"
**Why they ask:** The transition period is where the accounting close breaks; vendors only describe the end state.
**A (spoken):** "By keeping the processors' settlement files as the constant. They do not change during migration, so your close keeps one anchor while traffic moves. On the Yuno side every transaction carries your merchant order reference, so your ledger keys stay primary, and our reconciliation ingests the same settlement files for both migrated and legacy traffic views. I will bring the specific dual-run tooling and a typical transition calendar to the working session rather than improvise it here."
**Backup:**
- merchant reference retrieval endpoint exists (retrieve-payout-by-merchant-reference pattern; payments carry merchant order id). https://docs.y.uno/reference
**Status:** ⚠️ partial
**Source:** docs.y.uno

### Q30. "What are our exit terms? If we terminate in year two, what do we get back and how long does extraction take?"
**Why they ask:** They refuse to replace processor lock-in with orchestrator lock-in; they ask early because vendors hate it.
**A (spoken):** "You get your vault back: documented export of card data, PGP-encrypted, to any PCI DSS Level 1 destination you name, that is in our public docs, not a promise I am making up in a sales call. Transaction history exports via our reporting APIs. Network tokens are scheme-level assets. And because we never touch funds, there is no balance to unwind, exit is a routing change, not a treasury event. On contractual specifics, timelines and costs, that is Justo's territory and we will put it in writing in the proposal, not after signature."
**Backup:**
- Token export process documented: written authorization + receiving entity PCI AOC + PGP CSV over SFTP. https://docs.y.uno/docs/security-and-compliance/data-migration-processes/exporting-tokens-from-yuno
**Status:** ✅ verified (process); OPEN (contract terms, fees, timelines: Justo)
**Source:** docs.y.uno

---

# CATEGORY F. THE JPM QUESTION

### Q31. [MUST REHEARSE, THE TRAP QUESTION] "JPM Chase is not in our stack today, and we named it deliberately. Do you have a live, in-production connector to J.P. Morgan Payments, and can you name a mutual merchant processing on it right now?"
**Why they ask:** Public sources do not confirm a Yuno JPM connector. This is a designed honesty test; the answer calibrates the credibility of everything else said in the call.
**A (spoken, PENDING JARRETT'S CONFIRMATION OF CURRENT STATUS):** "I will give you the straight answer rather than the salesy one, because I suspect that is the point of the question. [IF STILL IN BUILD: 'J.P. Morgan is in our provider network and our cards integration with JPM's modern Online Payments API is in active development; I will not claim a referenceable production merchant on it today, because there is not one yet. What I can commit to is a written timeline with certification milestones, and JPM as a named deliverable in our contract.'] And one thing worth checking with every vendor in your process: many 'Chase connectors' in this market are the legacy Orbital gateway, which is deprecated and closed to new onboarding at several partners. The question that matters is who integrates the modern Online Payments API. Adding JPM through an orchestrator is precisely the right architecture, one certification, and the connector work is ours, not your team's; I just will not pretend we are further along than we are."
**Backup:**
- **INTERNAL, drives the wording:** JPMORGAN provider was a mock (yunotestpaymentgw) as of 2026-05-11; JPM cards integration reported in build 2026-03-16; current status unknown. Chase logo appears in TOP PROVIDERS on y.uno homepage. RESOLVE BEFORE CALL (open item 1).
- Orbital deprecation: Chargebee "Orbital is now deprecated... new onboarding is no longer available". https://www.chargebee.com/docs/payments/2.0/payment-gateways-and-configuration/orbital
- Competitor reality: Primer is an official JPM partner (GetYourGuide first adopter); Gr4vy lists Chase and touts ChaseNet certification; Spreedly lists Orbital. https://partners.jpmorgan.com/Primer.html, https://gr4vy.com/connections/
**Status:** OPEN (current build status: Jarrett/product). The honest frame above is safe regardless.
**Source:** internal Slack; chargebee.com; partners.jpmorgan.com

### Q32. "If we sign with JPM for US acquiring, what does onboarding Chase behind Yuno look like, and what is the realistic time to first live dollar, including JPM underwriting a future-delivery marketplace MoR?"
**Why they ask:** Vendors quote connector timelines and omit acquirer underwriting, which for future-delivery ticketing is the long pole.
**A (spoken):** "Two clocks running in parallel, and the slower one is not ours. Clock one is JPM underwriting you: an enterprise merchant agreement for a future-delivery business that holds funds for third parties, which means due diligence, reserve and collateral conversations, the same shape as the letter of credit you already maintain. That is typically months and it is between you and the bank; we can support but not compress it. Clock two is the technical leg through Yuno: connector, certification, routing config, and that is our work, not a project for your team. The orchestrator's promise is that clock two never becomes your bottleneck, and that when JPM is live it is a routing rule, A/B tested against Stripe and Braintree on cost and auth rate from day one."
**Backup:**
- JPM digital onboarding: full merchant KYC (CIP) required before processing; staggered onboarding possible. https://developer.payments.jpmorgan.com/docs/commerce/optimization-protection/capabilities/digital-onboarding
- Eventbrite already carries $48M LOC + $10.5M reserve (10-K), the exact collateral shape an acquirer will price.
**Status:** ✅ verified (structure); ⚠️ Yuno-side certification timeline needs product input
**Source:** developer.payments.jpmorgan.com; Eventbrite 10-K

### Q33. "When we route US volume to a new acquirer, how do you handle the pieces that do not move: network tokens, account updater enrollment, chargeback tooling?"
**Why they ask:** Adding an acquirer is never just routing; ancillary services are where auth rate quietly degrades in month one.
**A (spoken):** "This is exactly why the token layer has to live above the acquirer. Yuno procures network tokens directly from Visa, Mastercard and Amex, so the token, its cryptogram, and its lifecycle updates travel with the transaction to whichever acquirer wins the route; account updater runs at our vault level, not per processor. Disputes remain per-acquirer legally, but they consolidate operationally in one queue on our side. The month-one auth dip you are describing usually comes from re-vaulting at the new acquirer; the orchestrator-level vault is specifically how that is avoided."
**Backup:**
- Network tokens Yuno-procured (Visa/MC/Amex), cryptogram generation API, Card Account Updater. https://docs.y.uno/docs/security-and-compliance/network-tokens, https://y.uno/en/product/token-vault
- Chargeback management + disputes API documented. https://docs.y.uno/docs/payouts-and-disputes/chargeback-management
**Status:** ✅ verified; ⚠️ updater coverage by market (open item 8)
**Source:** docs.y.uno

### Q34. "Does your JPM connector support marketplace-specific pieces, sub-merchant data, split settlement, managed payouts, or is it straight acquiring with marketplace logic staying in our layer?"
**Why they ask:** JPM acquiring without marketplace features just adds a fourth processor to reconcile.
**A (spoken):** "For the architecture we are recommending, straight acquiring is actually the right shape: you stay merchant of record, JPM settles gross to your bank, and marketplace logic, splits and recipient attribution, lives at the Yuno layer consistently across all processors, so the JPM leg does not need JPM-proprietary marketplace constructs. JPM's own marketplace products are treasury-side, virtual accounts and payout rails, a different conversation and a direct banking relationship if you ever want it. I would not couple your split logic to any single acquirer's ledger; that is the lock-in we are helping you avoid on Stripe."
**Backup:**
- JPM has no Connect-clone in acquiring; marketplace money movement is Embedded Payments/Concourse (treasury products). https://developer.payments.jpmorgan.com/docs/embedded-finance-solutions/embedded-payments
- Yuno split model is processor-agnostic at the API, executed on provider rails where supported.
**Status:** ✅ verified (architecture); OPEN (Yuno JPM connector feature detail, item 1)
**Source:** developer.payments.jpmorgan.com; docs.y.uno

---

# CATEGORY G. RISK, COMPLIANCE, SECURITY

### Q35. "What is your PCI DSS level and attestation date, do you have SOC 2 Type II, and what happens to our PCI scope if you vault our cards?"
**Why they ask:** Table stakes screening; hesitation ends the evaluation.
**A (spoken):** "Yuno is PCI DSS Level 1 as a service provider, and we hold SOC 2 Type 2, ISO 27001, ISO 27701, and GDPR compliance; we are also a recognized Visa Service Provider. On your side: capturing cards through our SDK narrows a merchant toward SAQ A scope, which for a team your size is real audit relief. Current attestation documents and the AOC go to your security team under NDA this week if you want them."
**Backup:**
- PCI DSS Level 1 stated in docs; SDK merchants can qualify for SAQ A. https://docs.y.uno/docs/security-and-compliance/pci-compliance
- Footer badges: ISO 27001, ISO 27701, GDPR, PCI DSS, SOC 2 Type 2, Visa Service Provider. https://y.uno/en
- ⚠️ Exact AOC/ROC dates and QSA name: get from SecOps before promising dates.
**Status:** ✅ verified (certifications exist); ⚠️ dates/QSA (open item 11)
**Source:** docs.y.uno; y.uno

### Q36. "Chargebacks are ours as MoR and we hold a $48M letter of credit. Does anything in your model change our liability or descriptors, and do you consolidate disputes across processors?"
**Why they ask:** Certainty that liability and reserves do not move, plus real ops relief across three-plus dispute dashboards.
**A (spoken):** "Liability does not move: you are merchant of record before and after, descriptors are configured per processor exactly as today, and your reserve and letter-of-credit arrangements are between you and your acquirers, we do not sit in that chain. What changes is operations: disputes across your processors consolidate into one management surface and one API on our side, with the evidence flowing to each processor's rails underneath. Your team stops living in three dashboards; your risk posture stays exactly yours."
**Backup:**
- Chargeback management + disputes API documented. https://docs.y.uno/docs/payouts-and-disputes/chargeback-management, https://docs.y.uno/reference/payments/disputes
- ⚠️ Confirm which of their specific processors have full dispute-API coverage vs dashboard-only.
**Status:** ⚠️ partial
**Source:** docs.y.uno

### Q37. "We enable 3DS2 in only five European markets, by choice. Who decides when 3DS fires in your platform? Can we keep exemption logic per market, and our current 3DS setup?"
**Why they ask:** Blanket 3DS would crater conversion on high-demand on-sales; some orchestrators impose their own decisioning.
**A (spoken, FINAL):** "You decide, not us. 3DS routes through the same rules engine as payments: per market, per BIN, per amount, and it supports three models including external MPI, so you keep your own 3DS provider where you have one, and our 3DS where you want it. However you run 3DS today, and I'd rather have you describe your current posture than assume it, that expresses directly as routing rules. Nothing fires globally because a vendor default said so."
**Note:** never assert their 3DS configuration as fact; let them describe it.
**Backup:**
- Three 3DS models documented: Checkout SDK auto, External MPI ("use your own 3DS"), Direct; 3DS via dynamic routing; 3DS Standalone feature. https://docs.y.uno/docs/security-and-compliance/3d-secure, https://docs.y.uno/docs/payment-features/3ds-standalone
- ⚠️ SCA exemption engine (TRA, low-value) per acquirer: not explicitly documented; do not claim, offer technical session.
**Status:** ⚠️ partial (exemptions detail OPEN)
**Source:** docs.y.uno

### Q38. "Ticketing gets card-testing storms at on-sales. What does your fraud layer do natively versus orchestrating third parties, and can we keep our current fraud stack?"
**Why they ask:** They need to know if the fraud story is product or a partner directory, and whether incumbent tooling survives.
**A (spoken):** "Both layers exist and we are explicit about which is which. Native: blocklists, allowlists, velocity rules, and risk profiles that sit at the start of a route, which is your card-testing storm defense, rate and velocity controls per BIN, device, and identity before a single auth burns money. Orchestrated: third-party fraud engines connect as steps in the same routes, so your current fraud stack stays and gets orchestrated rather than replaced. Fraud screening can also be skipped per allowlist for your known-good flows, which matters at on-sale volume."
**Backup:**
- Risk conditions: blocklists, allowlists (skip fraud screening / skip 3DS), velocity rules; third-party fraud providers as non-payment connections in routes. https://docs.y.uno/docs/using-yuno/dashboard-overview/risk-conditions
**Status:** ✅ verified
**Source:** docs.y.uno

### Q39. "Where is our transaction data processed and stored, and how do you handle GDPR, UK, Brazil, Mexico data residency?"
**Why they ask:** Cross-border data through a new intermediary creates compliance work their shrunken team cannot absorb.
**A (spoken, FINAL):** "GDPR compliance and ISO 27701 privacy certification are in place, and I want to give your privacy team the precise data-residency architecture in writing rather than approximate regions in a call; I'll confirm the exact delivery timeline with our compliance team right after this call." (Say "this week" only once a delivery owner is confirmed.)
**Backup:**
- Data residency specifics: NOT publicly documented. Do not improvise. (Open item 10.)
**Status:** OPEN (residency architecture: SecOps)
**Source:** y.uno badges only

### Q40. "You were founded in 2022. Funding runway, customer concentration, insurance, and what protects us if Yuno is acquired or wound down?"
**Why they ask:** Board-level counterparty risk for a $3B GPV business; they just lived through an acquisition.
**A (spoken):** "Fair question, we ask it of vendors too. Yuno is backed by [DO NOT IMPROVISE: let Justo carry funding, investors, and continuity terms]. Two structural points I can make confidently: first, we are never in your funds flow, so vendor failure cannot strand a dollar of your money; second, your exit is documented, vault export to any PCI Level 1 destination, so continuity risk is a re-routing project, not a hostage negotiation. Contractual continuity provisions are a conversation we are happy to have in the proposal."
**Backup:**
- The two structural mitigations are verified (no funds flow; token export). https://docs.y.uno/docs/security-and-compliance/data-migration-processes/exporting-tokens-from-yuno
- Funding/insurance/escrow specifics: OPEN (Justo).
**Status:** OPEN (financial posture talking points: Justo)
**Source:** docs.y.uno

---

# CATEGORY H. RELIABILITY AND PERFORMANCE

### Q41. [MUST REHEARSE] "You become a single point of failure in front of my multi-processor redundancy. Measured availability, SLA with credits, and what happens to checkout when Yuno itself is down?"
**Why they ask:** The ironic failure mode of orchestration; the bypass answer separates serious vendors from the rest. They built failover precisely so no single vendor can take down checkout.
**A (spoken):** "The most legitimate question in this space, and I will not answer it with adjectives. Directionally: our platform is built for processor failure as a routine event, automatic failover, retries, and traffic redistribution when a provider degrades, and one public case: a merchant whose provider-disruption response went from five to ten minutes of manual work to milliseconds of automatic rerouting. For Yuno's own availability, measured uptime, the SLA with credits, and the degraded-mode design, I want you to have the real engineering answer with real numbers, and I would rather bring our platform team to the technical session than quote marketing at you. I'll confirm right after this call exactly when the SLA documentation reaches you." (Promise a date only once the doc's existence and owner are confirmed.)
**Backup:**
- Rappi public case: disruption response 5-10 min to milliseconds. https://y.uno/en/success-stories/rappi
- Routing: "Automatically redistributes traffic if a provider's performance drops." https://y.uno/en/product/smart-routing
- Uptime numbers, SLA, status page, degraded/bypass mode: NOT public. DO NOT invent. (Open item 4.)
**Status:** OPEN (SLA numbers and degraded-mode story: Justo/platform)
**Source:** y.uno; docs.y.uno

### Q42. "On-sales go from zero to thousands of transactions per minute. What burst throughput have you sustained, what is p99 added latency during spikes, and do platform rate limits throttle us?"
**Why they ask:** Ticketing traffic is spike-shaped; an orchestrator sized for steady-state ecommerce fails exactly when failure is most public.
**A (spoken):** "We process serious burst volume for consumer platforms today, and I want to answer this with production numbers, sustained TPS, p99 added latency, and per-merchant limits, from our platform team rather than approximate them. What I can tell you now: high-volume consumer marketplaces run on us in production, and capacity planning for spike events, including pre-warming for known on-sales, is part of enterprise onboarding. Let me make the load profile a named deliverable of the technical session."
**Backup:**
- **INTERNAL:** GFM scaled 25K to 468K monthly transactions Feb-Apr 2026; latency workstreams exist (tokenization latency war room, POST /v1/payments optimization). Do NOT quote numbers or war rooms externally; they inform caution: do not promise latency figures.
**Status:** OPEN (production TPS/latency numbers: platform team)
**Source:** internal Slack (context only)

### Q43. "Show me your status page history and your worst incident in the last 18 months: duration, impact, root cause, what changed."
**Why they ask:** Postmortem culture tells the truth that SLA pages do not; evasion is disqualifying.
**A (spoken):** "That is the right way to evaluate any vendor in your critical path. I will bring the incident history and how we communicated it, and you should ask our references the same question, ideally the finance team, not just engineering. I would rather show you a real postmortem than claim we have never had a bad day; nobody in payments gets to claim that honestly."
**Backup:**
- Public status page: not found in research. OPEN. Do not claim one exists until verified.
**Status:** OPEN (status page + incident narrative: platform)
**Source:** none public

### Q44. "Webhook delivery at spike volume: guarantees, ordering, retry policy, replay? Ticket issuance is coupled to payment confirmation."
**Why they ask:** Delayed or out-of-order events oversell or strand inventory exactly during the events that matter.
**A (spoken):** "Webhooks drive the payment lifecycle in our platform, and idempotency keys are first-class in our APIs. On delivery guarantees, ordering semantics, and replay tooling at spike volume, that is a precision answer I want our engineers to give yours in the technical session, alongside the pull-based reconciliation backstop: you should never depend on webhook timeliness alone for inventory release, and our transaction query APIs give you the authoritative pull path."
**Backup:**
- X-Idempotency-Key documented (transfers API). https://docs.y.uno/reference/transfers/create-standalone-transfer
- Webhook-based lifecycle documented across payments/3DS. https://docs.y.uno/docs/security-and-compliance/3d-secure
**Status:** ⚠️ partial (delivery SLOs OPEN)
**Source:** docs.y.uno

### Q45. "What p50/p99 latency do you add from Sao Paulo, Sydney, London, and how many regions do you serve from?"
**Why they ask:** Added latency directly costs conversion on their global checkout.
**A (spoken):** "Taking it as a committed follow-up with real measured numbers per region rather than a guess. What I will say: Latin America is where our infrastructure is deepest, Sao Paulo will not be our weak point."
**Backup:** No public region/latency documentation. OPEN.
**Status:** OPEN (platform team)
**Source:** none public

---

# CATEGORY I. COMMERCIAL

### Q46. "Pricing at our volume, 79M paid tickets, $3B gross: per-transaction or basis points, what is billable, do retries bill twice, do refunds and webhooks bill?"
**Why they ask:** Per-attempt vs per-success pricing swings the cost by millions at their volume; hidden ancillary billing is the classic trap.
**A (spoken):** "Per-transaction pricing on volume, decoupled from processor economics, our incentive is to lower your cost per approved transaction, not to sit on a percentage of it. I will not improvise your rate in this call: the honest version is a modeled proposal against your real mix, volume by market, method, and processor, which is exactly the working-session deliverable we are proposing. What I can commit to now: transparent tiers, and no surprise per-feature line items buried in an order form."
**Backup:**
- Pricing shape (per-transaction, volume-based) is the standing Yuno enterprise answer from the meeting brief. Rate specifics: OPEN (Justo).
**Status:** OPEN (rate card: Justo)
**Source:** meeting brief section 8

### Q47. "Do you take revenue from processors you route to? Will you contractually commit that routing is never influenced by your own economics?"
**Why they ask:** Rev-share with processors makes smart routing a conflict of interest.
**A (spoken):** "Routing rules are yours: you configure the conditions, the priorities, and the cost model the Smart Routing optimizes against, conversion plus cost, and you can audit why any transaction went where it went. On the commercial question, whether any processor-side economics exist anywhere in our business, I want Justo to answer that precisely rather than me approximating it, and if a routing-neutrality clause is what gets you comfortable, that is a contract conversation we will have directly."
**Backup:**
- Smart Routing optimization modes: conversion+latency or conversion+costs; conditions and priorities merchant-configured. https://docs.y.uno/docs/using-yuno/dashboard-overview/routing
- Processor rev-share existence: OPEN (Justo).
**Status:** OPEN (commercial disclosure: Justo)
**Source:** docs.y.uno

### Q48. "Beyond your fee: what did year one actually cost a customer our size, including our engineering months?"
**Why they ask:** The fee is never the cost; they need the fully loaded number against the do-nothing baseline.
**A (spoken):** "Fair, and the honest comparison for you is not Yuno versus free, it is Yuno versus the fully loaded cost of your in-house failover layer: every processor version change, every new method, every new market is engineering headcount you no longer have. I'll scope with our delivery team what comparable year-one numbers we can share, integration engineering included, and bring them to the working session." (Confirm feasibility with Justo before naming it a deliverable.)
**Backup:** OPEN (comparable TCO case: Justo/delivery).
**Status:** OPEN
**Source:** none

### Q49. "Contract terms: minimums, term length, what if our owner consolidates vendors and we exit in year one? And have you modeled how volume fragmentation affects our negotiated processor tiers?"
**Why they ask:** Bending Spoons integrates aggressively; and naive least-cost routing can breach volume commitments, raising the blended rate.
**A (spoken):** "On terms, Justo will walk you through structure, and your post-acquisition reality is exactly the kind of thing we would rather reflect in the contract than discover in year one. On the second question, that is one of the sharpest points anyone has raised in a first call: routing constraints in our engine are exactly how you respect volume tiers, you can floor a processor's share to protect a negotiated rate, and cost-aware routing should optimize your blended rate including tier effects, not just the marginal transaction. That is modeling we would do with your real contracts in the business case."
**Backup:**
- Percentage-based routing splits make tier-floors expressible. https://docs.y.uno/docs/using-yuno/dashboard-overview/routing
**Status:** ⚠️ partial (contract structure: Justo)
**Source:** docs.y.uno

---

# CATEGORY J. PROOF

### Q50. [MUST REHEARSE] "Name your largest live marketplace using split payments across multiple processors in production, and set up a reference call with their payments or finance lead."
**Why they ask:** A reference who runs marketplace splits at scale is the strongest signal in the bake-off; logos are not proof.
**A (spoken):** "We have a global marketplace live in production on our marketplace product, split payments, sub-merchant onboarding, transfers, running across two of the processors on your list, live since February and scaling monthly. I will request their permission today to name them formally and to set up the reference call, and I would push for their payments operations lead, since you will want reconciliation truth, not a marketing reference. [IF PERMISSION IS GRANTED BEFORE THE CALL: 'It is GoFundMe.']"
**Backup:**
- GoFundMe is publicly listed as a Yuno client on y.uno homepage; case study page does not exist yet.
- **INTERNAL:** first Marketplace merchant, live 2026-02-19, Stripe + Adyen + Tabapay. Name only after permission (open item 3).
**Status:** ⚠️ partial (permission)
**Source:** y.uno; internal Slack

### Q51. "Rather than slides: can you show me live, today, a split payment on Stripe Connect through your API, and the same order failing over to a second processor?"
**Why they ask:** They asked in writing for specific examples; inability to demo the named use case reads as not ready.
**A (spoken, FINAL):** "Yes to showing you the real thing, with one honesty rule we hold ourselves to: everything we show gets labeled GA, beta, or roadmap as we go, and you should hold every vendor to that. And if we don't get through the full flow in this half hour, my commitment is hands-on sandbox access for your engineers, real API keys, your team driving; I'll confirm the exact timeline right after this call." (Upgrade back to "this week" the moment open item 12 is confirmed.)
**Backup:**
- Demo depth constraint is real: Jarrett flagged he may be limited on a very deep dive. Pre-align with him exactly which screens/flows are shown and how each is labeled. (Open items 2 and 12.)
**Status:** ⚠️ partial (demo scope: Jarrett)
**Source:** internal

### Q52. "What auth-rate uplift have you measured for merchants who moved from in-house multi-processor routing, as opposed to single-processor merchants?"
**Why they ask:** Uplift stats are always quoted against single-PSP baselines; they already run failover, so the honest incremental number is smaller, and they want to see if we admit it.
**A (spoken):** "You are right to split those cohorts, and most uplift marketing hides it. For a merchant that already does failover, the incremental gains come from different levers: cost-aware and BIN-level routing rather than availability failover, smart retries on soft declines, network tokens, and local acquiring in markets where you are cross-border today. Public reference points: inDrive operates around ninety percent approval on our routing, and Rappi cut provider-disruption response from minutes to milliseconds. For your cohort question specifically, I will pull segmented data rather than quote you a blended number that flatters us."
**Backup:**
- inDrive ~90% approval (their Head of FinTech quote). https://y.uno/en/success-stories/indrive
- Rappi failover ms. https://y.uno/en/success-stories/rappi
- Segmented cohort data: OPEN (open item 6).
**Status:** ⚠️ partial
**Source:** y.uno success stories

### Q53. "Of everything shown today: what is GA, what is beta, what is roadmap? Split payments marketplace specifically: GA since when, how many merchants live?"
**Why they ask:** Marketplace features are the newest part of every orchestrator; they are scoring GA-versus-slideware.
**A (spoken):** "The split payments marketplace product is documented, in production, and carrying live volume today with a marketplace merchant at scale; it is our newest major product line and I will not pretend it is ten years old, it is battle-tested where it is live and expanding by provider. The provider-by-provider GA map, Stripe live, Adyen live and extending, PayPal multiparty in development, is exactly the level of honesty you will get from us on every feature, and I will put that map in writing in the follow-up."
**Backup:**
- Docs live. https://docs.y.uno/docs/payment-features/split-payments-marketplace
- **INTERNAL:** live merchant count on marketplace product: small (GFM first, Feb 2026; Pagar.me split in BR). Do not volunteer counts; if pressed: "the product is new and I will get you exact counts."
**Status:** ⚠️ partial
**Source:** docs.y.uno; internal Slack

---

# CATEGORY K. COMPETITION

### Q54. [MUST REHEARSE] "We are also evaluating BR-DGE, ProcessOut, Primer, Spreedly, Gr4vy and Payrails. Where do you objectively lose to them? Do not tell me you win everywhere."
**Why they ask:** Candor test that also maps what to probe with other vendors; refusing to name a weakness is a disqualifier.
**A (spoken):** "Fair, so here is a real answer. Where others are ahead: Primer is an official J.P. Morgan partner with a live JPM integration today, and Spreedly and Gr4vy have carried Chase connections longer than we have, though check whether those are the legacy Orbital gateway, which is deprecated, versus JPM's modern API. Payrails has a mature payouts partnership story in Europe. Where we win, and this is verifiable, not positioning: none of those six has a native marketplace product, a first-class sub-merchant object with split payments, onboarding, and transfers, live in production; they route cards and lean on each processor's own platform products. We built that layer and a global marketplace runs on it today. And in Latin America, where your growth story lives, our depth is not comparable to any of them. So if your evaluation is card routing only, we are one of several; if it is marketplace use cases, which is what you wrote in your email, the field narrows fast."
**Backup:**
- Competitor scan: Primer official JPM partner (GetYourGuide); Gr4vy ChaseNet certified + lists Chase; Spreedly lists Orbital; Payrails JPM "Soon", payouts via Thunes/MangoPay; BR-DGE and ProcessOut do not publicly enumerate the four; NONE claims a native split/sub-merchant engine. Full scan in eventbrite-platform-deepdives-2026-08-04.md.
- BR-DGE's ticketing reference (Resident Advisor, 3-year deal, includes payouts to venues/DJs) is real; expect them to lead with it.
**Status:** ✅ verified (public claims compared)
**Source:** competitor scan (deep-dives file)

### Q55. "What share of your customer base is marketplaces or platforms with a payout leg, versus straight merchants?"
**Why they ask:** A 95%-linear-ecommerce vendor will deprioritize marketplace features regardless of promises.
**A (spoken):** "Marketplaces and platforms are the strategic core of our roadmap, our marketplace product line shipped and went live with a flagship merchant this year, and payouts and recipient infrastructure are dedicated product areas, not side features. On exact portfolio percentages I will get you a real number rather than a guess. What I would point you to is trajectory: the newest, most invested surface of our platform is exactly the marketplace layer you are evaluating."
**Backup:**
- OPEN: portfolio mix number (Justo). Roadmap ownership evidence is internal (dedicated squad on GFM split/recipients tickets).
**Status:** OPEN
**Source:** internal

### Q56. "Your network token coverage by scheme and market, and your account updater story, versus what Stripe gives us for free?"
**Why they ask:** If orchestrator lifecycle tooling is worse than incumbent Stripe features, moving vaulted traffic is value-negative.
**A (spoken):** "We procure network tokens directly from Visa, Mastercard and American Express, support bring-your-own network tokens with issuer cryptograms, and run card account updater at the vault level. The structural difference versus Stripe's, which is genuinely good: Stripe's tokens optimize Stripe's rail; ours travel with the routing decision across every acquirer, including a future JPM leg. Scheme-by-market coverage tables and measured uplift data, I will include in the technical follow-up."
**Backup:**
- Network tokens + BYO + cryptogram API + Card Account Updater documented; marketing claims up to 4.6% approval improvement (use "up to", it is a marketing figure). https://docs.y.uno/docs/security-and-compliance/network-tokens, https://y.uno/en/product/token-vault
**Status:** ⚠️ partial (coverage tables OPEN)
**Source:** docs.y.uno

---

# CATEGORY L. PRODUCT AND ROADMAP

### Q57. "If we activated local methods and installments in Latin America through you, what ships in the first 90 days, and how do delayed-settlement methods like OXXO reconcile against a payout due 5 days post-event?"
**Why they ask:** APM expansion is the growth story, but cash-voucher settlement timing collides with their payout clock; they want evidence we thought past checkout.
**A (spoken):** "First 90 days, realistically: Mexico installments and OXXO through your existing Mercado Pago rail plus our recommended local acquirers, Brazil Pix, which now moves more transactions than cards in Brazil, and Argentina installments, all as routing configuration; from what's visible in your checkout this is activation, not construction. On your second point, which most vendors will not have thought about: delayed-settlement methods change the cash timing, not the payout obligation, so the design is settlement-aware payout eligibility, an OXXO ticket enters the organizer's payable when the voucher confirms, not when it is issued, and your five-day clock runs from event date as today with funds already settled. We model that per method in the business case, with your real settlement lags."
**Backup:**
- Pix 8.6x card volume (Central Bank of Brazil, meeting brief section 5).
- Dormant flags list (meeting brief).
- Mercado Pago connector documented. https://docs.y.uno/changelog/android
**Status:** ✅ verified (framing + facts); ⚠️ named acquirer recommendations per market for follow-up
**Source:** meeting brief; docs.y.uno

### Q58. "Will you contractually commit delivery dates for marketplace features we depend on that are not GA today?"
**Why they ask:** Roadmap promises are free in a bake-off; contractual commitment separates plans from sales talk.
**A (spoken):** "For named features you depend on, yes, that is a conversation we will have seriously in the proposal, with dates and remedies, Justo owns the commercial mechanics. What I will not do is verbally commit engineering dates in a first call, because you would rightly discount them. The PayPal multiparty layer and the JPM connector are the two obvious candidates for contractual milestones in your case."
**Backup:** Contract mechanics: Justo.
**Status:** OPEN (what product will commit to: Justo + product)
**Source:** internal

### Q59. "Our owner runs 50+ consumer apps on their own stacks. Does anything support or block one Yuno contract across multiple legal entities and product lines?"
**Why they ask:** Group-level leverage changes the commercial calculus; entity surprises kill deals at legal review.
**A (spoken, FINAL):** "Our architecture is built for exactly that: organizations with multiple accounts, entities, and connections under one integration, with per-entity segregation. Several of our merchants run multiple brands and countries under one relationship. If the portfolio conversation becomes relevant on your side, the contract can extend rather than restart; Eventbrite would be the natural first case."
**Note:** let THEM raise the parent-company angle; do not presume a conversation with Milan.
**Backup:**
- Organization > Account > Connections architecture documented. https://docs.y.uno/reference/organizations/connections-routing-overview
- Reserva public case: multiple brands under one orchestration layer (meeting brief hook 2).
**Status:** ✅ verified (architecture); ⚠️ contract structuring (Justo)
**Source:** docs.y.uno; meeting brief

### Q60. "What is on your committed 12-month roadmap for marketplace and platform use cases specifically?"
**Why they ask:** Scoring dedicated ownership and momentum on the layer they care about.
**A (spoken):** "Direction I can share today: extending provider coverage of the marketplace product, the PayPal multiparty layer is in active development, deepening Adyen platform capabilities, and payout expansion by market. The dated roadmap under NDA is a working-session deliverable, and where you have hard dependencies we will discuss committed milestones. What I want you to take from today: this is the part of our platform with the most investment right now, not a feature we maintain."
**Backup:**
- **INTERNAL:** PayPal marketplace in build for GFM; Adyen "being built out more" (Jarrett); Zoop split connector extension in flight. Consistent with the spoken direction; do not cite merchants.
**Status:** ⚠️ partial (dated roadmap: product)
**Source:** internal Slack

---

# ADDED AFTER INTERNAL REVIEW (GAP CHECK)

### Q61. "Who is our named technical contact post-sale, and what does enterprise support look like: ticket SLAs, shared Slack channel, TAM?"
**Why they ask:** A skeleton team needs to know the vendor carries the operational load, not them.
**A (spoken):** "A dedicated technical account manager plus a shared-channel model with our engineers is the standard enterprise shape, and support tiers with response SLAs go in the proposal in writing, not as verbal assurances. The people you meet in the technical session are the people who run our largest accounts."
**Status:** ⚠️ partial (confirm the exact support model and SLAs with Justo before quoting specifics)

### Q62. "What happens to in-flight payments during a Yuno deploy or a region failover?"
**Why they ask:** Deploy-time behavior reveals engineering maturity; fund-holding marketplaces cannot tolerate lost or duplicated payment events.
**A (spoken):** "Same standard I'm holding on availability: no adjectives. That question goes to our platform team in the technical session with the real engineering answer, deploy semantics, idempotency behavior, and what fails open versus closed. What I can say now is that idempotency keys are first-class in our APIs, and our transaction query APIs give you the authoritative pull path independent of event delivery."
**Status:** OPEN (platform team)

### Q63. "Can our data team get read-only access to routing decisions for audit?"
**Why they ask:** Consistent with the routing-neutrality concern (Q47); they want to verify, not trust.
**A (spoken):** "Routing decisions are auditable per transaction: you can see which connection took it and why, against the rules you configured. The exact export surface for your data team, API versus reports, is a technical-session item, and given the neutrality question you raised, I'd encourage you to make auditability a scoring criterion for every vendor in your process."
**Status:** ⚠️ partial (export surface detail: technical session)

### Q64. "Which of your answers today will you put in writing?"
**Why they ask:** The natural close for an honesty-test buyer.
**A (spoken):** "All of them. The follow-up includes the per-provider GA map, the feature matrix against the features you use, and the SLA documentation, in writing. Hold us to it, and hold the other six vendors to the same standard."
**Status:** ✅ (the commitment mechanism itself; the documents behind it are the Section 0 items)

---

# YUNO FOR PLATFORMS: PRODUCT QUESTIONS (ADDED v3, from the capability brief)

### Q65. "Is 'Yuno for Platforms' an off-the-shelf product or positioning? What exactly are we buying?"
**Why they ask:** Bake-off evaluators test whether the marketplace story is a packaged product or slideware.
**A (spoken):** "It is a real capability set, documented and live, not a label: the recipient object, typed split payments, recipient-linked payouts, and the orchestration layer underneath, all through one integration. What you buy is that model configured to your funds flow: your entities as accounts, your processors as connections, your organizers as recipients. The packaging and commercial shape come in the proposal; the capabilities you can verify in our public docs today."
**Status:** ✅ (components documented: Recipients, Split Payments Marketplace, Payouts, routing)

### Q66. "We process through different legal entities per region. How does your account structure map to that?"
**Why they ask:** They run 16 subsidiaries with dedicated processing entities (Dublin, Mexico "Payment Processing", AU, SG, HK, CA); entity mapping kills deals at legal review.
**A (spoken):** "One organization, multiple accounts, one integration. Each account maps to a country, entity, or brand, with its own provider connections, routing rules, and reporting, so your Dublin entity, your Mexican payment-processing entity, and the US parent each keep their own configuration while your engineers integrate once. Reporting rolls up or segregates per entity, which your finance team will care about at close."
**Status:** ✅ (Organization > Accounts > Connections documented)

### Q67. "Can one payment split across multiple recipients? Our orders can contain tickets from multiple events."
**Why they ask:** Basket-level multi-seller checkout is a known breaking point (PayPal multiparty caps at 10 purchase units, for example).
**A (spoken):** "Yes. The split breakdown distributes typed components, purchase, commission, fees, tax, across one or more recipients in the same payment, and the same structure carries into refunds, so a partial refund can target the right recipient's share. Multi-event orders express naturally; the constraint to design around is each underlying provider's own split mechanics, which is exactly what we map in the technical session."
**Status:** ✅ (multi-recipient splits documented; provider mechanics honesty kept)

### Q68. "We are effectively headless. What integration surfaces exist?"
**Why they ask:** A platform with its own checkout does not want an SDK-only vendor.
**A (spoken):** "Server-to-server API first, which is how marketplace merchants at our largest scale integrate with us, plus web and mobile SDKs and hosted checkout where you want them. Headless is a first-class path, not a workaround. One nuance: capturing cards through our SDK narrows your PCI scope toward SAQ A, while direct API keeps your current PCI posture with our vault or PCI proxy behind it; both are supported, you choose per surface."
**Status:** ✅ (API/SDK/hosted surfaces + PCI proxy documented)

### Q69. "Does the sub-merchant dimension actually survive retries, refunds, and reporting?"
**Why they ask:** This is the practical test of "first-class object" claims.
**A (spoken):** "Yes, and that is the design point. Because payments reference the recipient object rather than a metadata tag, the sub-merchant dimension persists through routing decisions, retries, refunds, and into reporting and reconciliation. Your per-organizer view does not fragment when the processor changes: the processor is an attribute, the organizer is the key."
**Status:** ✅

### Q70. "You claim 300+ providers and 1,000+ methods. What of that is actually relevant to us?"
**Why they ask:** Catalog numbers are the classic orchestrator vanity metric; a sharp evaluator discounts them.
**A (spoken):** "Honestly, a fraction, and that is the right way to read any vendor's catalog number. What matters for you: your five current providers, the JPM leg you want to add, and the local methods in your card-only markets, Pix, OXXO, installments, plus the payout rails where expansion earns something. The catalog's value is optionality: the next method or processor is configuration, not a build. We will scope the relevant subset in the business case rather than wave the catalog at you."
**Status:** ✅ (catalog claims are public marketing; the framing keeps them honest)

---

# APPENDIX. VERIFIED FACTS CHEAT SHEET

## Yuno (public, safe to state)
- PCI DSS Level 1; SOC 2 Type 2; ISO 27001; ISO 27701; GDPR; Visa Service Provider (y.uno, docs.y.uno)
- Split Payments Marketplace + Recipients API: first-class sub-merchants, typed splits (PURCHASE/COMMISSION/PAYMENTFEE/VAT), liability assignment, onboarding lifecycle, transfers + reverse transfers (docs.y.uno)
- "Yuno acts solely as the orchestrator of the payment, not the processor" (docs.y.uno, verbatim)
- Payouts live: bank/card/wallet rails, 17 documented countries (US + LATAM), Pix/STP/Nequi/PayPal payout methods (docs.y.uno)
- Network tokens procured from Visa/MC/Amex + BYO tokens + Card Account Updater + cryptogram API (docs.y.uno)
- Token export documented: PGP CSV over SFTP to any PCI L1 recipient with AOC (docs.y.uno)
- Routing: condition-based (card type, amount, currency, origin, issuer country), cascading outcome paths, percentage splits for A/B, Smart Routing AI (conversion+latency or conversion+costs) (docs.y.uno)
- Reconciliation product: Yuno records vs provider settlement files vs acquirer balances, conflict statuses, Reports API (docs.y.uno)
- 3DS: three models incl. External MPI (keep your own 3DS), routed via rules (docs.y.uno)
- Fraud: native blocklists/allowlists/velocity + third-party engines orchestrated in routes (docs.y.uno)
- Public references: inDrive (~90% approval, 10 countries <8 months), Rappi (disruption response 5-10 min to milliseconds, 300+ methods), GoFundMe named as client on homepage
- Adyen connector public: 52 countries, network tokenization, 3DS, recurring (y.uno/integrations); Mercado Pago documented since 2020

## The four platforms (for credibility moments)
- **Stripe:** Standard/Express/Custom deprecated for controller properties; destination charges and separate charges make the PLATFORM the business of record and disputes debit the platform; cross-border Connect only US/UK/EEA/CH/CA (AU not in matrix); funds holdable 90 days max outside US (2yr US); Instant Payouts cost 1% (Eventbrite charges 3%, margin ~2pts); top-ups from non-Stripe income GA only US/UK/JP; PAN export excludes Link credentials; connected-account KYC not exportable
- **Adyen:** Adyen for Platforms on Balance Platform (MarketPay is legacy); splits at auth/capture; chargebacks default to platform's liable account; negative balances eaten by platform after 30 days; payouts local-currency-only (mirrors Eventbrite's no-FX rule); multi pay-in accepts third-party acquired volume but requires allocation within 24h and no separate auth/capture; Instant payouts US/UK/AU/SEPA
- **PayPal/Braintree:** Braintree Marketplace CLOSED (Dec 2023 shutdown, dashboard-only notice); current product is PPCP multiparty (approval-gated; SELLER is MoR, clashes with EPP); Hyperwallet renamed Enterprise Payouts (200+ markets, 11+ methods); Ticketmaster runs Braintree acquiring + Hyperwallet payouts; Braintree vault export free incl. network transaction IDs; Apple/Google Pay tokens never portable
- **JPM:** No "JPM for Platforms" product exists; modern rail is Online Payments API under Commerce Solutions (legacy Orbital deprecated); #1 US acquirer (Nilson 2024); PINless debit routing via merchantPreferredRouting; Push to Card ~30s, $125K cap, US/CA; RTP+FedNow via one API; WePay absorbed, ISV agreements ended (platform-commitment volatility is a fair diligence point); marketplace money movement = Embedded Payments/Concourse (treasury products, separate from acquiring)

## Landmines (from the meeting brief, still binding)
- Never say Eventbrite "lacks" anything; respect their failover build, distinguish failover from routing
- Never quote a dollar figure for their processing cost (not disclosed)
- Never assert Adyen's or Cybersource's role in their stack (undisclosed); ask
- PayPal is a wallet/APM, never a processor; Braintree is the acquiring relationship
- Stripe, Braintree, Adyen, Cybersource, Mercado Pago all STAY; never pitch replacement
- Do not mention: layoffs, CFIUS, Delaware lawsuit, privacy letters, NYSE:EB, earnings calls, Julia Hartz as CEO
- **INTERNAL facts (GFM volumes, war rooms, build statuses, mock connectors) are for calibration only; never quoted externally**

## Additions from the internal review (binding)
- **No unconfirmed "this week" promises.** Every dated commitment needs a confirmed owner before the call; otherwise say "I'll confirm the timeline right after this call." Applies to Q39, Q41, Q48, Q51 and anything improvised live.
- **Never say "we probed/inspected your checkout payload."** Maximum: "from what's visible in your checkout." (Q8, Q57)
- **Never assert their configuration as fact** (3DS posture, processor roles); let them describe it. (Q37, consistent with the Adyen/Cybersource landmine)
- **The anonymized reference is only anonymous while vague.** February go-live + two named processors + the homepage logo is a solvable puzzle; freeze all further detail (tips/fees/rails) until GoFundMe permission lands. (Q15, Q28, Q50)
- **Q31 bracket discipline:** if JPM status is unresolved at call time, use only the neutral second half (Orbital vs modern API + orchestrator-as-right-architecture) and commit to a written status within 24h. Never improvise beyond the bracket.

---

# APPENDIX B. YUNO FOR PLATFORMS — CAPABILITY BRIEF (internal agent, public-docs based)

*Scope note: this brief is built from Yuno's public documentation (docs.y.uno, y.uno). It describes the platform/marketplace model and its documented capabilities. Provider-by-provider GA status, timelines, and anything commercial (pricing, SLA terms) are not covered here; those come from the product and commercial teams.*

## 1. The model in one paragraph

Yuno for Platforms is Yuno's orchestration model for marketplaces, ticketing platforms, delivery apps, and any business that processes payments on behalf of third parties (sellers, creators, organizers, drivers: "recipients"). The platform keeps its role as merchant of record and keeps its own ledger; Yuno provides a single integration layer that orchestrates the **pay-in leg** across multiple processors, represents sub-merchants as first-class objects, carries split instructions with each payment, and (where enabled) orchestrates payouts. Yuno is **never in the funds flow**: money settles processor to merchant directly; Yuno moves instructions and data, not funds.

## 2. Core building blocks

*Organizations, accounts, connections:* one organization can hold multiple accounts (per country, entity, or brand), each with its own provider connections, routing rules, and reporting. One integration covers all of them; this is how multi-country / multi-brand platforms run under a single relationship.

*Recipients (sub-merchant object):* recipients are first-class API objects, not metadata. A recipient represents the seller/creator/organizer, carries identification and account data, and is linked to the platform's provider connections (e.g. an existing Stripe connected account). Payments reference recipients, so the sub-merchant dimension survives routing, retries, refunds, and reporting.

*Split payments:* a payment can carry a split breakdown with **typed components** (PURCHASE, COMMISSION, PAYMENTFEE, VAT, MARKETPLACE) distributed across one or more recipients. The split travels with the transaction into the provider's platform mechanics (e.g. Stripe Connect transfers and application fees, Adyen for Platforms splits), so commission/fee logic is expressed once at the Yuno layer instead of per-processor.

*Provider platform flavors:* for marketplace use cases the connectors target the platform/marketplace flavor of each provider's API where available (Stripe Connect, Adyen for Platforms, PayPal multiparty, local equivalents such as Pagar.me recipients), not just vanilla acquiring. Exact per-provider scope is a matrix the team shares in technical sessions.

## 3. Pay-in orchestration (applies fully to the platforms model)

- *One API / SDKs:* single integration (server-to-server API, web/mobile SDKs, hosted checkout) covering 300+ providers and 1,000+ payment methods globally: cards, wallets, bank transfers (Pix, PSE, SPEI), cash, BNPL, installments.
- *Smart routing:* rules engine on any transaction attribute (country, currency, amount, BIN, method, recipient) with cascading/retry across providers. Currency and market pinning are routing conditions (relevant for no-FX policies).
- *Vaulting and network tokens:* PCI DSS Level 1 vault, cards stored once and routable to any connected processor; network tokenization so credentials travel with the routing decision instead of being locked to one PSP. Documented vault export (encrypted, to a PCI L1 destination) on exit.
- *3DS and fraud:* flexible 3DS orchestration (including external MPI support) driven by the same rules engine; native anti-fraud capabilities plus orchestration of third-party fraud providers.
- *Lifecycle:* authorizations, captures (full/partial), refunds (full/partial, split-aware), voids, webhooks for every status transition, idempotency, merchant-side order references carried end to end.

## 4. Recipient lifecycle and KYC

Recipient creation and onboarding runs through Yuno's API; where the underlying provider requires its own KYC/verification (e.g. Stripe Connect hosted onboarding, Adyen hosted onboarding), Yuno orchestrates into those flows. Important honesty point: **KYC is a per-provider regulatory obligation**; an orchestrator cannot collapse one KYC into universal coverage across processors. What Yuno removes is the integration cost of each flow, not the regulatory step itself.

## 5. Payouts

Yuno has a payouts API (recipient-linked) with documented coverage concentrated in the Americas (US + LATAM, 17 countries in the public docs). A platform can also keep its existing payout rails (e.g. Stripe Connect payouts) while Yuno orchestrates only pay-ins; the recipient object still gives a unified per-sub-merchant view across processors. Coverage beyond the documented countries is a roadmap conversation with the team.

## 6. Reporting and reconciliation

Per-transaction data with recipient and split detail, unified across processors; reconciliation tooling that ingests processor settlement files (the settlement file stays the anchor, important for platforms with their own ledger); dashboards per account/entity; metadata pass-through (event IDs, batch IDs, internal keys) for joining Yuno data to the platform's ledger.

## 7. Migration and exit posture

- Shadow/passthrough mode and percentage-based traffic splits with instant rollback; platforms migrate gradually, keeping existing processors live.
- Stored credentials keep working: vault migration paths for existing card-on-file portfolios; network tokens are scheme-level assets.
- Exit: documented vault export, transaction history via reporting APIs, and, because Yuno never holds funds, no balance to unwind. Exit is a routing change, not a treasury event.

## 8. Compliance envelope

PCI DSS Level 1, SOC 2 Type II, ISO 27001, ISO 27701, GDPR alignment; Visa-listed service provider. Specific dates, AOC, and residency architecture are shared under NDA via the compliance package.

*Sources: docs.y.uno (Payments, Recipients/Split Payments, Payouts, Routing, Tokenization, Reconciliation sections) and y.uno public pages.*

