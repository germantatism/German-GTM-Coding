# BUILD BRIEF · Eventbrite + Yuno Proposal Deck

This is the complete specification for a new deck: **"Proposal · Eventbrite + Yuno"**. Follow it exactly. Where this brief is silent, resolve by copying what the Flair deck does.

---

## 0. Mission and audience

- **What to build:** a 24-slide proposal deck, 1920×1080, in the exact visual system of the Flair Airlines proposal, ready to export as PDF and be forwarded by email.
- **Primary audience:** Noè, Giacomo and Filippo, the incoming commerce leadership of Eventbrite at Bending Spoons (Milan). They are sharp, fast, come from the subscription world, and are **new to marketplaces**. The deck must educate on marketplace payments without ever being condescending.
- **Secondary audience:** Paul Pasion, Eventbrite's outgoing Head of Payments (Director of Product Management, Commerce). He forwards this deck. He is a 25+ year payments veteran (Amazon, Marqeta, Uber, Recurly). One overclaimed capability and he will not forward it.
- **Context:** Eventbrite is right now deciding whether to bring in an orchestration layer, and is speaking with several orchestrators. This deck is Yuno's entry into that evaluation. It must work standalone, with nobody presenting it.
- **Language:** English. Everything.

## 1. Design source of truth

1. **Base template:** `templates/flair-business-case-v2/FlairBusinessCaseV2.dc.html`. Clone its structure, spacing, typography and slide chrome. The Eventbrite deck must look like a sibling of the Flair deck.
2. **Visual reference:** `uploads/flair/` and `uploads/flair2/` page renders, plus `decks/flair/slides/`.
3. **Tokens and components:** `tokens/*.css`, `styles.css`, and the components in `components/` (SlideFrame, CoverSlide, SlideHeadline, Kicker, StatCard, YunoCard, CaseTable, Pill, SourceFooter). Use them; do not invent new chrome.
4. **Archetype library:** `uploads/deck-library/` (234 pages, see `notes/deck-library-text.md`) is the canonical source for any slide pattern the Flair deck does not contain: logo grids, provider maps, team layouts, timeline slides. `uploads/deck-2026/` is the current master sales deck; reuse its Why Yuno content and phrasing where it fits.
5. **Assets:** Yuno marks and wordmarks in `assets/`. Cover lockup format: `yuno | eventbrite` top left, exactly like the Flair cover lockup. No "Hello team" greetings anywhere.

## 2. Hard rules (non-negotiable)

1. **Never mention Fever.** Not in text, not in logos, not in examples.
2. **No quantified business case and no pricing.** No dollar-value levers, no ROI tables, no fee cards. Numbers come later in a Milan workshop.
3. **Never mention "CFO Copilot".**
4. **EBANX must never appear as part of Eventbrite's current stack.** Eventbrite is not an EBANX customer. EBANX may appear only inside Yuno's own MoR partner network (slide 18).
5. **Never tell Eventbrite they "lack" anything.** Their current setup is described neutrally, in their own team's words. The conversation is performance, cost, reliability and speed to market.
6. **No em-dashes and no " - " as punctuation** anywhere. Use "·", commas, or periods. Never use the phrase "no small feat".
7. **Facts only.** Every capability claim in section 5 marked ✅ is backed by Yuno's public documentation and may be stated as fact. Every item marked ⚠️ is pending internal verification: include it exactly as written in this brief, changing nothing, so the reviewer can strip or confirm it before sending.
8. The industry quote on slide 10 is **anonymized**. Never attribute it to a person.

## 3. Narrative spine

The whole deck exists to prove one sentence, heard again and again across the industry:

> "There are great orchestrators for pay-ins, decent ones for payouts, and no one has tied the two together."

Yuno is the layer that ties them. Every slide either builds credibility for that claim or demonstrates it. Five acts: Executive Summary → Why Yuno? → Eventbrite & the marketplace gap → Modular by design → The path forward.

## 4. Slide-by-slide specification (24 slides)

### Act 1 · EXECUTIVE SUMMARY

**Slide 1 · Cover.** Flair-style dark cover. Lockup `yuno | eventbrite`. Title: "ONE LAYER FOR BOTH SIDES OF THE MARKETPLACE". Subtitle: "Prepared for the Eventbrite & Bending Spoons commerce team · August 2026".

**Slide 2 · Agenda.** Flair agenda style, five items: 01 Executive summary · 02 Why Yuno? · 03 Eventbrite & the marketplace gap · 04 Modular by design · 05 The path forward.

**Slide 3 · Executive Summary.** Exact Flair executive-summary layout: context left, "WHAT EVENTBRITE GETS WITH YUNO" right.
- Left, header "WHERE EVENTBRITE STANDS TODAY", four short blocks:
  1. *A new chapter.* Eventbrite operates since March 2026 as part of Bending Spoons, with a lean operating model and a new commerce leadership team.
  2. *The decision on the table, now.* Whether to bring in an orchestration layer, with an active evaluation of several orchestrators.
  3. *Direction already set.* The team has aligned on a multi-PSP strategy over consolidating into a single processor.
  4. *Open fronts the decision must resolve.* Intelligent routing across the existing rails (including the ChaseNet economics offered by J.P. Morgan), the exit from own LatAm entities, getting out of the funds flow with PSD3 on the horizon, and running all of it with a small team.
- Right, three benefit blocks (Flair right-column style):
  1. **PAY-IN AND PAYOUT ROUTING IN ONE LAYER.** Both sides of the marketplace orchestrated, with the ledger that links every pay-in to its payout.
  2. **MODULAR BY DESIGN.** Activate only what you need. Every provider you run today stays.
  3. **ONE DASHBOARD.** Normalized data and automatic reconciliation across every rail.

### Act 2 · WHY YUNO?

**Slide 4 · Divider.** Flair divider style. "Why Yuno?"

**Slide 5 · Yuno in numbers.** Flair stats slide, four tiles: 1,000+ payment methods · 190+ countries supported · 460+ integrations · 180+ currencies.

**Slide 6 · Trusted by leading companies worldwide.** Flair logo-grid slide. Fifteen logos: Uber, GoFundMe, Fiverr, Whop, SpaceX, Zuora, McDonald's, Qatar Airways, Rappi, Crypto.com, Samsung, inDrive, Copa Airlines, Ant Group, Hotmart. If a Fiverr asset is missing, render a clean wordmark. Do NOT include Fever, Moonactive or NetEase Games.

**Slide 7 · Built and operated by global payment operators.** Flair team slide layout. Founders: Juan Pablo Ortega, Co-founder & CEO, previously co-founder of Rappi · Julián Nuñez, Co-founder & COO, early employee at Rappi. Leadership: Justo Benetti, Chief Revenue Officer, previously enterprise integrations at dLocal, WorldPay and Global Collect · Mau Schwartzmann, Chief Banking & Financial Institutions Officer, ex CEO of RappiBank, leadership at Mastercard · Chee Beh, GM APAC, 20+ years across TSYS, NTT Data, JPMorgan and Uber · Walter Campos, GM LatAm, 20+ years including MercadoPago and Cielo. Footer line: regional payments teams on the ground in the Americas, Europe, the Middle East and Asia Pacific, operating as an extension of each merchant's payments team.

### Act 3 · EVENTBRITE & THE MARKETPLACE GAP

**Slide 8 · Divider.** "Eventbrite & the marketplace gap"

**Slide 9 · Eventbrite's payment stack today.** Flair "current setup" layout: topology diagram left, constraint cards right.
- **Diagram:** USERS → eventbrite (dark node) → six parallel provider chips: **Stripe, Braintree, J.P. Morgan Chase, Wells Fargo, Mercado Pago, Banco Galicia**. No other providers. Caption under the diagram: "Six rails, integrated point to point · no routing layer between them".
- **Right, header "IN THE TEAM'S OWN WORDS", four cards:**
  1. *No routing between rails.* No cross-processor failover, no BIN-based routing, no least-cost debit routing running today.
  2. *One portal per provider.* Reporting lives in each provider's own dashboard.
  3. *Creators coupled to one rail.* Onboarding is tied to the processor; cross-currency events can trigger double FX and re-onboarding.
  4. *Entities under review.* Own entities operate Brazil, Argentina, Mexico and Colombia; the team is evaluating an exit from the funds flow.

**Slide 10 · The gap nobody closes.** Full-width diagram slide.
- Left block: "PAY-IN ORCHESTRATION · a crowded, mature category. Routing, retries, tokenization, checkout. Attendee side only."
- Right block: "PAYOUT PROVIDERS · capable, but disconnected from the money coming in. No view of the pay-in side."
- Center, dashed-border box: "THE CONNECTING LAYER · KYC & KYB of creators · funds, ledger and reserves · FX across both sides · reconciliation end to end · fraud signals spanning pay-in and payout". Tagline inside: "this is where marketplaces live".
- Bottom full-width blue strip: "At Uber and Amazon, this middle layer is run by payments teams of hundreds. A company built to operate lean needs it as a service, not as an org."

### Act 4 · MODULAR BY DESIGN

**Slide 11 · Divider.** "Modular by design"

**Slide 12 · A modular operating system for payments.** The central diagram of the deck.
- Top: chip "EVENTBRITE · one API".
- Middle: large Yuno-blue board titled "YUNO OPERATING SYSTEM" holding seven white module sockets: Pay-in orchestration & routing · Payouts · KYC & KYB · Fraud · Reconciliation · Tokenization · MoR partner network. Sub-caption inside the board: "every module activates standalone · every module works with every provider below".
- Bottom: provider chip row: Stripe, Braintree, J.P. Morgan, Adyen, Mercado Pago, dLocal, Nium, Thunes, "+460 more".
- Footer line: "Adding or swapping a provider is configuration, not a build. Nothing obliges you to take the bundle."

**Slide 13 · Bundle lock-in vs modular freedom.** Two-column contrast diagram.
- Left, dark monolith titled "THE BUNDLE MODEL": stacked blocks "KYC locked to the platform account" / "Processing on the same rail only" / "Payout bound to country & currency". Under it: "Cross-currency events pay FX twice · leaving means re-onboarding every creator".
- Right, "THE MODULAR MODEL": top blue block "Creator onboarded once · portable KYC & KYB, owned by you" feeding three independent modules "Pay-in, best route per transaction" / "Funds & ledger, one source of truth" / "Payout, best provider per payout". Under it: "Each function routes to the best provider, independently · swap any piece without touching the creator".
- Bottom strip: "The platform products use the same underlying KYC and payout providers you can use standalone. Modularity returns that choice, and its economics, to you."

**Slide 14 · Pay-in routing, as deep as you want it.** Flow diagram left, two cards right.
- **Flow:** Transaction → "BIN lookup · issuer, network, type" → three branches: (a) "Chase-issued card → ChaseNet · on-us acquiring, discounted economics" ⚠️, (b) "US debit → least-cost debit rails · Star, Pulse, NYCE" ⚠️, (c) "Everything else → best route by cost and auth rate". Below branch (c): "on decline → cascading by outcome: chained steps for Succeeded, Pending, Declined and Error" ✅.
- **Documented capabilities to state as fact ✅:** condition-based routes (card type, amount, currency, origin) · Smart Routing AI that optimizes "conversion rate and costs" or "conversion rate and latency" · percentage splits across connections when the merchant wants to keep partial manual control · risk steps (fraud, 3DS) as gates inside the route · post-authorization steps for risk review or settlement.
- **Right cards:** "Smart retry economics: retry only when the expected recovery beats the scheme fees, rule based per decline code and market" · "Interchange+ visibility: transaction-level data surfaces downgrades and downgrade patterns".

**Slide 15 · Payout routing, the same discipline on the other side.** Flow diagram.
- Payout request → "KYC & KYB gate: beneficiary verified once" → "Provider selection per payout · providers quote live FX, the best rate wins" ⚠️ (wording pending) → three exit rails: (a) "Local bank transfer · directly into local bank accounts in the preferred currency" ✅, (b) "Card payout via Referenced Payouts · pays out to the tokenized card from the original pay-in, no PCI scope for the merchant" ✅, (c) "Wallets" ✅.
- Footer: real-time payout status and notifications across providers ✅.

**Slide 16 · Split marketplace payments, native.** Diagram plus cards.
- Flow: Payment → "Split among recipients · manual or automatic: percentage, fixed, or mixed" ✅ → "Each recipient onboarded with dynamic KYC & KYB workflows" ✅ → "Liability configured per recipient · processing fees and chargebacks: merchant, recipient, or shared" ✅ → "Standalone transfers from the organization balance, outside the payment cycle" ✅.
- Honest note at the bottom (keep it): "Yuno orchestrates the split; the provider processes it. Splits run on providers that support them, such as Stripe, Adyen and dLocal."

**Slide 17 · The marketplace loop, closed.** The signature diagram.
- Horizontal flow: ATTENDEE → PAY-IN (best route per transaction · Stripe, Braintree, J.P. Morgan, Adyen) → YUNO LEDGER (blue, center: "every pay-in linked to its payout, transaction level · KYC portable · reserves managed") → PAYOUT (providers compete per payout on FX · Nium, Thunes, TerraPay, local rails ⚠️) → CREATOR.
- Dark arc spanning pay-in and payout: "FRAUD SIGNALS ACROSS BOTH SIDES · the fake-event collusion pattern a pay-in-only tool cannot see".
- Badge: "Fiverr: ~$900K in FX saved on payouts in six months" ⚠️.

**Slide 18 · Exit LatAm entities without exiting LatAm.** Per-country transition diagram.
- Four country columns (BRAZIL, ARGENTINA, MEXICO, COLOMBIA), each with two rows: "TODAY · own entity, own compliance and funds flow" → "WITH YUNO · MoR partner in country, local pay-ins netted against payouts".
- Three cards: "85+ MoR providers, ranked per market ⚠️ · EBANX connected direct, dLocal and local specialists where they win" · "Fully modular scope · full MoR, or tax-of-record plus standalone components, staged" · "One reporting layer on top · operations see one normalized dashboard, never another portal".

**Slide 19 · One dashboard, every rail.** Funnel diagram.
- Left: stack of provider portal chips (Stripe portal, Braintree portal, J.P. Morgan portal, Mercado Pago portal, MoR partner portal) → center blue engine "NORMALIZATION + RECONCILIATION · transaction reports × settlement reports, cross-referenced automatically · raw data always accessible underneath" → right card "ONE DASHBOARD · payment ops, chargebacks and refunds in one place · drill into a provider portal only on a flagged discrepancy, with exact references".
- Bottom strip: "Starlink runs entities in nearly 100 markets. Before Yuno, one dashboard per acquirer. Today, everything through one." ⚠️

**Slide 20 · Out of the funds flow, in stages.** Three ascending stage blocks.
- STAGE 1 · FAST FIX: a local MoR partner takes the funds flow per market, entities wind down.
- STAGE 2 · UNBUNDLE: KYC, tax and payout run as separate modules, best provider on each, economics visible per component.
- STAGE 3 · END STATE: fully out of the funds flow, no PSP or MSB registration, PSD3-ready in Europe and the UK, Canada-compliant by design.
- Dark strip: "The agent exemption is narrowing in Europe and mostly gone in Canada. This structure is staged so the value lands before regulation forces the change."

### Act 5 · THE PATH FORWARD

**Slide 21 · Divider.** "The path forward"

**Slide 22 · Built for the Bending Spoons operating model.** Text left, three cards right.
- Left: "A lean company cannot run payments as an organization. **It can run payments as a service.**" Then: "Eventbrite's payments surface, six rails, a marketplace ledger, LatAm entities, creator payouts, is the kind of scope that consumes an entire engineering team. Yuno operates that surface as infrastructure: the roadmap, the maintenance, the provider relationships and the expertise, delivered through one API and one dashboard."
- Cards: 1. "The only marketplace in a subscription portfolio · the same Yuno layer runs both models; Zuora's payment rails run on Yuno on the subscription side" ⚠️. 2. "Every future acquisition lands as configuration, not as a payments integration project." 3. "An expert bench you do not have to hire · regional payments teams advising on providers, rates and methods per market."

**Slide 23 · Next steps.** Flair-style horizontal timeline, four milestones: THIS WEEK · MNDA signed as-is, custom materials delivered → NEXT WEEK · introduction to the incoming commerce leadership team → LATE AUGUST · working session in Milan, Yuno CRO on site → SEPTEMBER · technical deep-dive, data exchange and pilot design.
- Strip: "Everything on this page fits inside the current transition window. The foundation is set before the handover, so the incoming team starts with answers, not questions."

**Slide 24 · Closing.** Flair dark closing slide. "Let's grow together". Contacts: German Tatis · Business Development Manager · +57 317 645 7074 · german.tatis@y.uno, and Justo Benetti · Chief Revenue Officer. Lockup `yuno | eventbrite` bottom right.

## 5. Claim ledger

**State as fact ✅ (backed by Yuno public documentation):** condition-based routing · outcome-based cascading with chained steps · Smart Routing AI optimizing conversion+costs or conversion+latency · percentage splits across connections · risk and post-auth steps in routes · payouts via bank transfer, card and wallet · localized payouts to local bank accounts in preferred currency · Referenced Payouts to the tokenized card of the original pay-in · split marketplace payments with percentage/fixed/mixed autosplit · dynamic sub-merchant KYC & KYB onboarding · per-recipient liability for fees and chargebacks · standalone transfers from organization balance · real-time payout statuses.

**Include exactly as written, pending internal sign-off ⚠️:** ChaseNet connection and BIN routing in production · Star/Pulse/NYCE debit rails · live FX competition between payout providers · Nium, Thunes, TerraPay as named payout providers · EBANX direct connection and "85+ MoR providers" · Starlink ~100 dashboards to 1 · Fiverr ~$900K FX in six months · Zuora rails on Yuno.

## 6. Useful context data

- Eventbrite operates in **122 countries**. Top 10: United States, United Kingdom, Canada, Australia, Italy, Germany, Spain, Ireland, France, Mexico. Use these countries in routing and payout examples (note Italy, Germany, Spain and France are home turf for a Milan audience; Mexico is the only LatAm market in the top 10).
- Eventbrite is a merchant of record on its own platform, holds creator funds and pays out creators. Its checkout brand order: attendee pays Eventbrite, Eventbrite pays the creator.
- Do not use any Eventbrite financial figures in this deck.

## 7. Definition of done

- 24 slides, 1920×1080, visually indistinguishable in system from the Flair proposal (same cover treatment, dividers, kickers, headline bar, card styles, table chrome, closing).
- All nine diagrams built with the project's tokens and components, not screenshots.
- Zero violations of section 2. Zero em-dashes. English throughout.
- Every ⚠️ claim present verbatim so it can be confirmed or stripped in review.
