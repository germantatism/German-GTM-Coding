# Yuno facts, proof points and product nuances

Captured from Samuel's and Germán's decks, May-Sep 2026. Company stats move; before using a number, check y.uno or a deck newer than this file, and use **one consistent set** throughout the deck (past decks mixed 450+/460+ providers and 190+/194+/195 countries in the same file).

## Positioning line (German's canonical pitch; use verbatim or lightly adapted)

"Yuno is an AI native operating system for global financial infrastructure. We help companies orchestrate their payment stack across a fragmented ecosystem that includes payment methods, processors, antifraud tools, KYC/KYB providers, reconciliations, and stablecoins to lower payment processing costs, increase authorization rates, expand globally, and become more operationally efficient." Four outcomes: lower processing costs · higher authorization rates · global expansion · operational efficiency. Prefer this over the stat list when a narrative line is needed; the stats stay as supporting detail.

## Published performance figures (the only Yuno-wide numbers allowed)

7% authorization uplift and 30% recovered revenue, both published on y.uno (source line: "Yuno published figures · y.uno"). Verified client results are also fine: McDonald's +4.7% acceptance across 18 markets and $3.2M additional revenue. Never "+12% auth uplift" or "20-30% decline recovery": no public source, flagged as fabricated on six decks. Reconciliation across PSPs (settlement, payout and fee reconciliation) is roadmap, not GA: footnote it as such wherever it appears.

## Standard pricing (default when the deal has no negotiated pricing)

The first $50,000 processed is free; beyond that Yuno charges $0.05 per transaction. State it exactly this way and label it "standard pricing". Deal-specific pricing from German overrides it and is labeled deal-specific. Never invent tiers.

## Company one-liners

- Founded 2022 by co-founders of Rappi. Payment orchestration and infrastructure; does not custody funds ("orchestrated, not custodied"); no acquiring arm, so routing has nothing to optimize but the merchant's KPIs.
- Headline stats (pick the current set): 1,000+ payment methods · 450-460+ providers/integrations · 190+ countries · 180+ currencies · ~$80B/yr orchestrated.
- Integration velocity: ~150 new providers and 300+ new methods shipped in a trailing 12 months (≈ 3 providers a week); new connectors and their maintenance included for the life of the partnership.
- Recognition: named a World's Top Fintech Company and #1 Best Payment API (2025).
- Offices/teams: São Paulo, Mexico City, Bogotá, Buenos Aires, San Francisco, New York, Madrid, London, Paris, Dubai, Singapore, Mumbai, Manila. Follow-the-sun support.

## Customers to reference (choose by the prospect's vertical; confirm each is referenceable)

- Gaming / digital: NetEase Games, Garena, Moon Active.
- Mobility / delivery / platforms: Uber, Rappi, inDrive, GoFundMe.
- Travel: Qatar Airways, Wingo.
- Other: SpaceX (Starlink), McDonald's (Arcos Dorados), Livelo.
- Named results used in decks: inDrive expanded to 11 countries in 8 months with ~90% approval rates · Rappi cut new-provider implementation time to near zero · Livelo 50% transaction recovery and 5% approval uplift · Wingo +14% approval rates.
- GoFundMe is Yuno's first live Marketplace merchant (Feb 2026: Stripe + Adyen + Tabapay, splits, recipients, transfers), the platform-deal reference; ask German before sharing anything beyond the name.
- Nothing about Riot Games ever goes to a third party, in any deck.
- Never put a prospect or a customer under NDA on a logo wall. Never reveal another customer's commercial terms or volumes. Customer names are written as text; never fetch or redraw their logos.

## Why Yuno (five reasons) and vs other orchestrators

Truly global orchestrator · a dedicated team for <Merchant> (KAM, TAM, solutions engineer, fraud and optimization specialists) · payments-as-a-service for complex needs (we co-create, operate and optimize) · award-winning and recognized · infrastructure resilience (write this one for their vertical: concurrency spikes in gaming, peak booking windows in travel).

Versus alternatives: **local-rail breadth** deeper than building on one global processor · **no lock-in** through a processor-agnostic vault, unlike committing to a PSP's own rails · **payments-as-a-service**, beyond self-serve gateways.

## Product suite (four groups)

Payment orchestration and routing (orchestration, smart routing, monitors and auto-failover) · Checkout and SDKs (customizable checkout; SDK depths Full, Seamless, Lite, Headless, Secure Fields; web, iOS, Android; subscriptions) · Security and risk (3DS, network tokens, account updater, fraud routing, PCI Level 1 vault) · Insights and operations (analytics on fees/FX/approvals, reconciliation, payouts). Newer/adjacent: standalone vault / PCI proxy, KYC/KYB orchestration, tax and merchant-of-record partners, NOVA AI voice and WhatsApp outreach, Stripe Billing bridge and Stripe proxy, usage meters.

## Trust and reliability

- Certifications: PCI DSS Level 1 · SOC 2 Type 2 · ISO/IEC 27001 · ISO/IEC 27701 · GDPR · Registered Visa Service Provider. Trust center: security.y.uno. Status and incident archive: status.y.uno.
- Architecture talking points: active-active across availability zones; regional failover with RTO under 5 minutes and continuous replication; US primary/failover region pair by default; in-country residency live in India; failover for residency-constrained data stays in jurisdiction.
- Uptime/SLA numbers, TPS figures and latency commitments are **deal-specific and sensitive**. Past decks had conflicting uptime claims across email, order form and SLA. Do not print a number unless German confirms it for this deal; otherwise use the "what we publish / what we sign" framing with a flagged placeholder in speaker notes, not on the slide.

## Partnership and support model

Through go-live: forward-deployed engineers embedded through phase 1 (offered at no charge on strategic deals; confirm), dedicated solutions engineering, role-based onboarding. Ongoing: KAM, TAM, tier-3 engineering, executive sponsor and QBRs, 24/7 engineer-staffed tier-1 support, lifetime connector engineering. For multi-market localization deals Germán adds dedicated regional teams (APM partnerships, TAM, solutions engineers, strategic KAM) and a 60-day BD sprint to secure wallet and local acquirer commitments. These are commitments: include only what fits the deal size and what German confirms.

## Leadership slide (proposals)

Co-founder and CEO Juan Pablo Ortega (co-founder of Rappi) · co-founder Julián Núñez (Rappi founding team) · CRO Justo Benetti (ex-dLocal) · CPTO/CTO Edwin Poot · SVP Product Martin Mexia (ex-Revolut, Rappi) · VP Engineering Rik ter Beek (ex-Adyen) · GM APAC Chee Beh (ex-Uber, J.P. Morgan) · GM LATAM Walter Campos (ex-Mercado Pago, Cielo) · Chief Banking and FI Mauricio Schwartzmann (ex-Mastercard Mexico, RappiBank) · Head of GTM Bernabe Murata (ex-Worldpay). Titles change; verify before use.

## Pricing shapes (never invent numbers)

Shapes seen in approved deals: success-based per-transaction tranches (marginal, like tax brackets) · ramping monthly minimum in place of a fixed fee · platform fee plus lower per-transaction rate · flat monthly fee up to a volume cap · annual platform fee for low-count, high-ticket merchants · metered add-ons (network tokens, account updater, 3DS, fraud routing, reconciliation) · go-live incentive credits · paid POC with an exit. Match the shape to the volume profile: minimums for high-count/low-ticket, platform fee for low-count/high-ticket. Actual rates come from German, the deal folder (`Deals/<Merchant>/`) or an approved Slack/Gmail record for **this** merchant; with none, use the standard pricing above and say so. Show "what it means for <Merchant>" as all-in cost per transaction at three volumes.

## Product nuances to verify before they go on a slide (as of Sep 2026)

Check each against docs.y.uno (context7 MCP: resolve the docs.y.uno library, then query; or WebFetch the docs page); product status changes quickly.
- **Stripe Billing bridge (third-party processing mode):** Stripe stays the subscription system of record; Yuno collects the payment method through Yuno's checkout/SDK and runs the charges. Stripe Checkout, Stripe's Smart Retries and recovery emails, and Stripe-managed disputes do **not** carry over; Stripe must enable third-party processing on the account; the first payment must be reported within a short window after subscription creation. Do not write "Stripe Checkout unchanged". Stripe's Billing fee still applies to off-Stripe volume. Confirm live/production status with solutions engineering before labeling it "live".
- **Migrating existing Stripe tokens** depends on Stripe's Vault and Forward, which Stripe gates commercially. Long lead item; say so.
- **Yuno subscriptions engine:** plans with per-country pricing, retry strategies, webhooks per state. Documented recurring methods were card, PayPal enrollment and Pix Automático; other wallet mandates were claimed internally but not in docs. Usage-based billing (meters) was gated per organization and still maturing; prepaid credit packs are not the same as usage billed in arrears.
- **A/B testing:** backend/processing-path A/B shipped; in-SDK front-end A/B was roadmap.
- **Payouts:** orchestration (routing, coverage, tracking) is live; tax-compliance workflows (W-8/W-9, 1099) stay with the merchant's existing provider.
- **Link / processor-native wallets** generally live only inside that processor's checkout. If a large share of their transactions uses one, moving checkout has a conversion cost; address it, don't ignore it.
- **Dispute-alert vendors** are enrolled per merchant ID/descriptor; moving volume to new acquirers needs re-enrollment.
