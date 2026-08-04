# Eventbrite War Room: Platform Deep Dives + Intent Hypotheses

**Prepared 2026-08-04 for the Yuno <> Eventbrite call (16:30 COT, Paul Pasion).** Companion files: eventbrite-meeting-brief-2026-08-04.md (account brief) and eventbrite-pre-questions-2026-08-04.md (Q&A bank).

Paul's verbatim ask: "For reference, we are currently speaking with several other orchestrators. During our call, we would like to see specific examples of how your integrations with PayPal (Braintree), Stripe, Adyen, and JPM Chase support marketplace use cases."

All platform research below was produced 2026-08-04 from primary sources (official provider docs first); every claim carries an inline source URL. Items that could not be verified are marked NOT VERIFIED.

---

# What Eventbrite Wants: Ranked Hypotheses (Phase 2 Synthesis)

Built from the meeting brief (data/research/eventbrite-meeting-brief-2026-08-04.md), Paul Pasion's verbatim email, and the four platform deep dives below. Ranked by confidence.

## H1. Add J.P. Morgan as a US acquiring leg for cost, with the orchestrator carrying the integration (confidence: very high)

**Evidence:** Paul named "JPM Chase" although JPM is not on Eventbrite's sub-processor list. 71.6% of Eventbrite revenue is US. JPM is the number 1 US merchant acquirer (Nilson 2024: 40.98B transactions). JPM's Online Payments API exposes merchantPreferredRouting including PINless debit, which lets a high-volume US merchant route Durbin-regulated debit to cheaper networks. Their own 10-K names processing fees as the largest component of cost of net revenue. Post-acquisition, the team is small and no payments org is being hired, so a fourth direct integration in-house is exactly what they cannot staff.
**Implication for the call:** The JPM question is partly a capability trap. Answer it with total honesty (see Q31 in the pre-questions doc). The winning frame: the orchestrator is how a two-person payments team adds a bank acquirer without building and maintaining a fourth integration, and Yuno's routing can A/B the JPM leg against Stripe/Braintree on cost and auth rate.

## H2. Keep merchant-of-record, their own ledger, and Stripe Connect payouts; orchestrate only the pay-in leg (confidence: very high)

**Evidence:** Eventbrite is MoR under EPP, carries $278.2M payable to creators and $101.1M advance payouts in its OWN books, and runs creator payouts through Stripe Connect connected accounts in US/CA/UK/AU (organizers sign the Stripe Connected Account Agreement). Nothing in the 10-K suggests they want to give up MoR or float. The phrase "marketplace use cases" is the test of whether routing pay-ins across acquirers breaks Connect attribution, splits, and payout funding.
**Implication:** Lead with the funds-flow architecture: Yuno never touches funds, settlement paths unchanged, payouts and organizer KYC stay exactly where they are, pay-in routing happens in front. This is literally the GoFundMe architecture Yuno runs in production today.

## H3. De-risk vendor concentration without swapping it for orchestrator lock-in (confidence: high)

**Evidence:** They deliberately built their own multi-processor failover ("multiple integrations ... back up processing alternatives"), which reveals a no-single-point-of-failure philosophy. An evaluator with that philosophy will ask about the orchestrator as a new SPOF, token portability, and exit terms.
**Implication:** Yuno's documented token export process (PGP/SFTP to any PCI L1 recipient), PCI proxy, and network tokens are the proof points. Volunteer the exit story before they ask.

## H4. Turn on local payment methods and installments in the card-only markets with a small team (confidence: high)

**Evidence:** MX, AR, SG, HK are card-only; BR runs cards+Elo+Hipercard; OXXO/boleto/rapipago/pagofacil/installment flags exist in the checkout payload but are switched off. 41% of paid tickets are non-US vs 28% of revenue. Julia Hartz's last public roadmap named "the addition of more payment options" as the international lever, and that roadmap now belongs to a smaller team.
**Implication:** This is where Yuno structurally beats the other six orchestrators (LatAm depth, documented Mercado Pago connector, Pix/OXXO/installments via existing rails). Bring a 90-day LatAm activation story.

## H5. One reporting/reconciliation plane so a skeleton team can run 4 to 5 processors (confidence: medium-high)

**Evidence:** 636 employees post-layoffs, zero payments hiring on the Bending Spoons job board. Reconciling Stripe + Braintree + Adyen + Mercado Pago + Cybersource settlement files against a $278M payable is a real cost center.
**Implication:** Demo Yuno reconciliation (transactions vs provider settlement files vs acquirer balances) and transaction-level reporting keyed to their organizer IDs.

## H6. The email is also a bake-off filter run by a technical evaluator (confidence: high)

**Evidence:** "We are currently speaking with several other orchestrators" plus a request for "specific examples" on four named processors is designed to separate real connector depth from logo-ware. Competitor scan: Primer, Spreedly and Gr4vy publicly list all four processors; Payrails lists JPM as "Soon"; BR-DGE and ProcessOut do not enumerate them. NONE of the six publicly claims a native marketplace split/sub-merchant engine.
**Implication:** Yuno's Recipients/Split Payments Marketplace product, live in production with a named marketplace client, is the differentiator no competitor can publicly match. Precision and GA-vs-roadmap honesty win the second meeting.

## H7 (reserve). Bending Spoons group-level consolidation angle (confidence: medium)

**Evidence:** Parent runs 50+ consumer brands on fragmented per-brand billing stacks (Stripe at WeTransfer/Vimeo, PayPal/Conceptive at Evernote), 75% of group revenue through electronic payments, processor dependence flagged as an IPO risk factor.
**Implication:** Do not lead with it. If Paul says "decisions are made in Milan," convert to an introduction: Eventbrite is the natural first case of a portfolio-wide orchestration layer.

---

# DEEP DIVE 1: STRIPE CONNECT

## platform

Stripe Connect

## product_status

**Current product names and status as of 2026:**

- **Stripe Connect** remains the umbrella product for platforms and marketplaces (SaaS platforms, marketplaces, multi-party money movement). Source: https://docs.stripe.com/connect
- **The Standard/Express/Custom trichotomy is legacy.** The accounts page carries an explicit deprecation notice: "The information on this page applies only to platforms that already use legacy connected account types (Standard, Express, or Custom accounts)." Stripe's stated recommendation: "Stripe recommends that you use controller properties instead of account types." Sources: https://docs.stripe.com/connect/accounts, https://docs.stripe.com/connect/migrate-to-controller-properties
- **Controller properties** (controller.fees.payer, controller.losses.payments, controller.requirement_collection, controller.stripe_dashboard.type) are the current v1 account model. Legacy types map deterministically to property combinations (Standard = stripe/account/stripe/full; Express = application/application_express/stripe/express; Custom = application/application_custom/application/none). Source: https://docs.stripe.com/connect/migrate-to-controller-properties
- **Accounts v2 API** is now the recommended path for new platforms (docs use preview API version header 2026-07-29.preview, so parts are still in preview). It replaces controller.losses.payments with defaults.responsibilities.losses_collector and introduces merchant/customer/recipient configurations. Limits: OAuth, recipient service agreement signing, and Treasury still require v1. Source: https://docs.stripe.com/connect/accounts-v2
- **Connect embedded components** (onboarding, balances, payouts, instant-payouts-promotion) are generally available for adding dashboard functionality inside the platform's own app. Sources: https://docs.stripe.com/connect, https://docs.stripe.com/connect/supported-embedded-components/payouts
- **Global Payouts** is a standalone payouts product (send money to 60+ countries without processing pay-ins on Stripe), available to platforms in US and GB. UK legal terms still say "Preview Services Terms," so regional status varies; NOT VERIFIED as GA in every market. Sources: https://docs.stripe.com/global-payouts, https://stripe.com/payouts, https://stripe.com/gb/legal/global-payouts
- **Instant Payouts** for connected accounts: live in AE, AU, CA, DK, EU, GB, HK, MY, NO, NZ, SE, SG, US. Source: https://docs.stripe.com/connect/instant-payouts
- **Stripe Treasury**: still exists but requires v1 accounts; not fetched in depth for this brief (NOT VERIFIED beyond the Accounts v2 limitation note). Source: https://docs.stripe.com/connect/accounts-v2

## funds_flow_models

**Three charge types, each with a different merchant of record (Stripe calls it settlement merchant / business of record):**

1. **Direct charges**: charge is created on the connected account; "the payment appears in the connected account's balance, not in your platform's balance." The connected account is the merchant of record. Requires the connected account to hold the card_payments capability (full service agreement only). Typical for SaaS (Shopify-style), not marketplaces. Source: https://docs.stripe.com/connect/charges
2. **Destination charges**: charge is created on the platform; "the payment appears in your platform's balance. A portion of the funds immediately transfers to the connected account's balance." Platform is merchant of record unless on_behalf_of is set. Source: https://docs.stripe.com/connect/charges
3. **Separate charges and transfers**: charge on the platform account first, then one or more Transfer objects move funds to connected accounts, with independent timing and multi-party splits (DoorDash example in docs). Platform is merchant of record. Source: https://docs.stripe.com/connect/charges

**on_behalf_of**: setting it on a destination charge or separate charge makes the connected account the settlement merchant: "Charges settle in the connected account's country and settlement currency," the connected account's fee structure and statement descriptor apply. "If on_behalf_of is omitted, the platform is the business of record for the payment." Source: https://docs.stripe.com/connect/destination-charges?platform=web&ui=elements

**Cross-border rules:**
- Platforms in US, UK, EEA, Canada, Switzerland can transfer to connected accounts in those same regions. Supported flows are only: "Separate charges and transfers without on_behalf_of," "Top-ups and transfers," "Destination charges without on_behalf_of." on_behalf_of is NOT allowed cross-border in these flows. Source: https://docs.stripe.com/connect/cross-border-payouts
- Conversely, when platform and connected account are in different regions and you want the connected account as settlement merchant, docs require on_behalf_of "with certain exceptions," so the two constraints interact per corridor. Source: https://docs.stripe.com/connect/destination-charges?platform=web&ui=elements
- Cross-border payouts cannot go to accounts under a **recipient service agreement**; for those, Stripe points to Global Payouts. Recipient accounts "can't process payments or request the card_payments capability" and transfers to them "take an additional 24 hours to become available." Sources: https://docs.stripe.com/connect/cross-border-payouts, https://docs.stripe.com/connect/service-agreement-types

**Funding from outside Stripe (critical for orchestration):** platforms can add external funds to their Stripe balance via **top-ups**, explicitly including "Adding funds from non-Stripe income." GA in USA, UK, Japan; private preview in EU, Canada, Australia, New Zealand. Timing: US wire 1-5 days, ACH credit 1-3 days, ACH debit 5 days, UK FPS 2 hours to 1 day, SEPA 1-2 days. Restriction: the receiving connected account must be in the same market as the platform or on a recipient service agreement. Source: https://docs.stripe.com/connect/top-ups

## onboarding_kyc

**Three onboarding surfaces** (https://docs.stripe.com/connect/onboarding):

1. **Stripe-hosted onboarding**: Stripe builds and hosts the form, handles data validation and real-time verification, updates immediately for new compliance requirements, supports new countries without integration changes. "Use Stripe-hosted onboarding if you want Stripe to handle onboarding and reduce the amount of effort for your platform."
2. **Embedded onboarding**: platform embeds Stripe's Account onboarding component in its own app; "you get a customized onboarding flow and don't need to update your onboarding integration as compliance requirements change." Branded UX, Stripe still drives requirement collection.
3. **API onboarding**: platform builds the entire UI and owns the compliance treadmill: "You must plan on reviewing and updating onboarding requirements at least every 6 months," and Stripe says "We don't recommend this option unless you're committed to the operational complexity."

**Who carries regulatory responsibility** is set by controller.requirement_collection (v1): "stripe" means Stripe collects updated information when requirements change; "application" means the platform is responsible and gets full API access to KYC properties, including attesting to ToS acceptance. requirement_collection=application is incompatible with losses.payments=stripe, fees.payer=account, and any Stripe-hosted dashboard. Source: https://docs.stripe.com/connect/migrate-to-controller-properties

**Service agreements**: full agreement creates a direct Stripe relationship and allows card_payments; recipient agreement means "Stripe has no direct service relationship with the recipient" and the account can only receive transfers/payouts. The agreement type cannot be changed after acceptance. Source: https://docs.stripe.com/connect/service-agreement-types

**Timelines**: Stripe publishes no fixed KYC SLA on these pages; verification is real-time-ish in hosted flows but requirement-driven. NOT VERIFIED: any specific onboarding completion time statistics.

## ledger_balances

**Ledger model** (https://docs.stripe.com/connect/account-balances):
- "Both your platform account and a connected account are nothing more than regular Stripe accounts, each with their own separate account balance," each with pending and available states. Platforms also have a **connect_reserved** balance "used to offset negative balances on connected accounts."
- Balances of connected accounts are read by calling the Balance API with the Stripe-Account header.

**Holding funds**: platforms can hold funds either in the platform balance before transfer, or in the connected account balance with a manual payout schedule. **Hard country limits on how long funds can be held: United States 2 years, Thailand 10 days, all other countries 90 days.** Stripe adds: "We recommend that platforms hold funds only when there's a clear purpose and a commitment to transfer them or pay them out when an event occurs or a precondition is satisfied." Source: https://docs.stripe.com/connect/account-balances

**Negative balances and clawbacks**:
- "If at all possible, Stripe automatically offsets negative transactions against future payments." Negative transactions post to the account the charge was made on (direct charge negatives hit the connected account; platform-charge negatives hit the platform).
- Responsibility follows controller.losses.payments (v1) or defaults.responsibilities.losses_collector (v2): stripe or application.
- Platforms can set debit_negative_balances=true to let Stripe pull from the connected account's external bank account (supported: Australia, Canada, Europe/SEPA incl UK, New Zealand, US). "Stripe can't correct a negative Stripe account balance using a debit card."
- When the platform is loss-liable, Stripe holds a platform reserve for the account for an additional 3 business days after a covering bank withdrawal posts; and "When a connected account holds a negative balance amount for 180 days, Stripe transfers a portion of your balance to zero out that account's balance" (connect_collection_transfer).
- **No auto-retry**: failed transfers or payouts due to insufficient platform funds are never retried automatically after a top-up; the platform must re-issue them. Sources: https://docs.stripe.com/connect/account-balances, https://docs.stripe.com/connect/top-ups

**Reserves at platform level**: when losses_collector=application, "Stripe might hold reserves on your platform account to cover negative connected account balances"; when stripe, it does not. Source: https://docs.stripe.com/connect/risk-management

There is no formal escrow product; held balances are Stripe balances, and Stripe cautions against open-ended holding (see limits above).

## payouts

**Schedules**: default is "paid out on a daily rolling basis" per connected account; platforms can set automatic schedules, manual payouts, or retain funds at platform level. Control depends on dashboard type: with Express or no dashboard the platform controls payouts; with full dashboard the account holder manages external accounts. Failed payout = external account disabled until details are updated. Source: https://docs.stripe.com/connect/payouts-connected-accounts

**Instant Payouts** (https://docs.stripe.com/connect/instant-payouts):
- Countries: AE, AU, CA, DK, EU, GB, HK, MY, NO, NZ, SE, SG, US. Requires full ToS onboarding, local-currency payout, and an eligible external account (debit card in most markets; debit card only in CA, CZ, HU, NO, PL, RO, NZ, MY, AE; bank accounts only in HK).
- **Stripe fee: 1% of payout volume.** Per-payout limits: USD min $0.50, max $9,999 (per payout). Daily platform-wide volume cap resets at midnight US Central.
- Speed: "typically within 30 minutes," 24/7 including weekends.
- **Platforms can monetize on top** via application fees or account debits ("Platforms can realize additional revenue by assessing a fee for receiving Instant Payouts"). Sources: https://docs.stripe.com/connect/instant-payouts, https://stripe.com/connect/pricing

**Cross-border payouts**: platform in US/UK/EEA/CA/CH paying connected accounts in those regions; 0.25% fee, "waived (0%) for payouts sent between the UK and the EEA, or within the EEA." Not available to recipient-agreement accounts. Source: https://docs.stripe.com/connect/cross-border-payouts

**Currency rules / payout in collected currency**: **multi-currency settlement** lets connected accounts "hold and payout funds in up to 18 supported currencies... without having to convert funds." Available in EU, GB, CH, NO, LI, SG, HK, AU, US, and "Connected accounts must be in the same region as your platform." A multi-currency settlement fee applies when settling in a non-primary currency. So Stripe can replicate Eventbrite's pay-out-in-collected-currency model, and can also convert with FX fees if desired. Source: https://docs.stripe.com/connect/multicurrency-settlement

**Global Payouts (payouts-only mode)**: standalone product, no pay-in processing required; platform countries US and GB; "Send money to 60+ countries"; fund from external bank funds or Stripe payments balance, multi-currency funding to reduce FX; marketed example pricing "$1.50" per standard bank transfer and "$1.50 + 0.75%" for instant debit card payouts. Recipients sign nothing with Stripe (recipient model). Sources: https://stripe.com/payouts, https://docs.stripe.com/global-payouts, https://docs.stripe.com/connect/service-agreement-types

**Top-ups** fund payouts from non-Stripe income (GA US/UK/Japan, preview EU/CA/AU/NZ; ACH credit 1-3 days, wire 1-5 days, FPS same-day). Source: https://docs.stripe.com/connect/top-ups

## liability

**By charge type** (https://docs.stripe.com/connect/risk-management):
- **Direct charges**: connected account is "always the merchant of record"; "negative transactions for direct charges affect the connected account's balance." Refunds and chargebacks hit the seller first.
- **Destination charges and separate charges and transfers (indirect charges)**: "Indirect charges occur on the platform, so negative transactions for indirect charges affect the platform's balance." For destination charges specifically: "with or without on_behalf_of, Stripe debits dispute amounts and fees from your platform account." The platform then recovers from the seller by reversing the transfer (reverse_transfer on refunds, transfer reversals on disputes). Sources: https://docs.stripe.com/connect/risk-management, https://docs.stripe.com/connect/destination-charges?platform=web&ui=elements
- Refund default on destination charges: "by default the destination account keeps the funds that were transferred to it, leaving the platform account to cover the negative balance from the refund" unless reverse_transfer=true.
- Cross-border wrinkle: retransferring a previous reversal is subject to cross-border transfer restrictions, so Stripe advises waiting until a cross-border dispute is actually lost before clawing back. Source: https://docs.stripe.com/connect/destination-charges?platform=web&ui=elements

**By controller setting** (https://docs.stripe.com/connect/risk-management):
- losses_collector=stripe: "Stripe covers losses due to your connected accounts' negative balances," no platform reserves held, Stripe risk teams manage account risk.
- losses_collector=application: platform absorbs connected-account negative balances, Stripe may hold platform reserves, platform manages risk.
- Critical caveat: "Connected account balance liability applies only to connected account balances. It doesn't affect negative platform balances caused by transactions related to indirect charges. If you use indirect charges, assign negative balance responsibility to your platform, not to Stripe." Translation: for a marketplace like Eventbrite that is MoR, chargeback risk on the pay-in leg is always the platform's, regardless of settings.

## pricing

**Published Connect pricing** (https://stripe.com/connect/pricing):
- If Stripe bills connected accounts directly for processing ("Stripe handles pricing"): "No fees for your platform."
- If the platform handles pricing (marketplace model): **$2 per monthly active account** (active when payouts are sent) plus **0.25% + 25 cents per payout sent** (listed as 0.25% of payout volume for funds routing).
- **Instant Payouts: 1% of payout volume** (per-payout min/max by currency, e.g. USD $0.50 min, $9,999 max, per https://docs.stripe.com/connect/instant-payouts).
- **Cross-border payouts: starting at 0.25% of payout volume** (waived UK-EEA and intra-EEA per https://docs.stripe.com/connect/cross-border-payouts).
- **Account debits: 1.5% of debit volume.**
- Pay with Stripe Balance: 1% of transaction volume.
- US 1099 tax reporting: $2.99 per 1099 e-filed with IRS, $1.49 per state e-file, $2.99 per mailed 1099.
- Card processing baseline: "Starts at 2.9% + 30 cents per successful card charge" (large platforms negotiate custom/IC+ pricing; custom rates NOT VERIFIED, not published).
- Multi-currency settlement fee applies per currency/country, amounts not published on the docs page fetched. Source: https://docs.stripe.com/connect/multicurrency-settlement
- Global Payouts marketed examples: $1.50 standard bank payout, $1.50 + 0.75% instant to debit card. Source: https://stripe.com/payouts

## lock_in

**What is portable:**
- **PAN data**: Stripe has an explicit export policy: "we can only transfer your card data to another PCI DSS Level 1-compliant payment processor." Deliverable is an encrypted JSON file with card numbers, expiry, name, address, customer email, and metadata, transferred processor-to-processor via PGP (4096-bit key hosted on the receiving processor's domain). No published cost or SLA. Sources: https://docs.stripe.com/get-started/data-migrations/pan-export, https://support.stripe.com/questions/what-if-i-decide-to-leave-stripe-can-i-export-card-data
- Non-PCI data (payment history, subscriptions) is exportable via API/Dashboard but is NOT included in the PAN export file: "Stripe doesn't export your account's payment history, subscriptions, or other objects."

**What is NOT portable:**
- **Link credentials**: "We exclude any credentials saved through Link from our exports." Any share of checkout volume converted to Link is unroutable to other processors. Source: https://docs.stripe.com/get-started/data-migrations/pan-export
- **Connected accounts themselves**: there is no mechanism to export a connected account's verified KYC/KYB state to another provider. The verification status, ToS acceptance, and requirements history live in Stripe's Account objects. Moving payouts off Connect means re-onboarding and re-verifying every creator at the new provider. NOT VERIFIED: any Stripe program to transfer verification artifacts; none is documented.
- **The Connect ledger**: balances, pending payouts, reserves, negative-balance offsets, and the 118-country payout rail are proprietary; balances must be paid out or transferred, not migrated.
- **Service agreement**: "After a connected account accepts it, you can't modify the type of service agreement," so an installed base of full-agreement accounts cannot be converted to recipient-only accounts to slim down the relationship. Source: https://docs.stripe.com/connect/service-agreement-types

**Practical lock-in read**: pay-in tokens are exportable (minus Link); the payout/identity layer is the sticky part. A platform can go multi-processor on acquiring while keeping Connect for payouts, but it cannot cheaply replicate 78.9M-ticket-scale creator KYC elsewhere.

## limitations

- **Instant Payout caps**: $9,999 per payout (USD) and a platform-wide daily cap that resets at midnight CT; large organizers hit this fast. Debit-card-only in many markets. Source: https://docs.stripe.com/connect/instant-payouts
- **Fund-holding limits**: outside the US, funds can be held at most 90 days (US: 2 years, Thailand: 10 days). An events platform that sells tickets many months before the event and pays out about 5 days after it can exceed 90 days between collection and payout in non-US markets; this requires structuring (platform-balance holding, staged transfers) rather than naive connected-account holding. Source: https://docs.stripe.com/connect/account-balances
- **Cross-border constraints**: cross-region flows only within US/UK/EEA/CH/CA, only without on_behalf_of, and never to recipient-agreement accounts; 0.25% fee. Latin America and most of APAC are outside the Connect cross-border payout matrix (Global Payouts covers more countries but is a separate product with per-payout fees). Sources: https://docs.stripe.com/connect/cross-border-payouts, https://stripe.com/payouts
- **Multi-currency settlement requires same region** platform and connected account, 18 currencies max. Source: https://docs.stripe.com/connect/multicurrency-settlement
- **No auto-retry of failed transfers/payouts** after topping up; operational burden on the platform's treasury automation. Source: https://docs.stripe.com/connect/top-ups
- **Holds/freezes discourse**: persistent market criticism of Stripe fund holds and termination reserves. Most relevant precedent: donation platform Flipcause filed Chapter 11 in December 2025 owing $29M to nonprofits while Stripe froze $1.45M citing elevated risk and objected in court to releasing funds against up to $6M in potential chargebacks. This is the exact platform-holds-other-people's-money shape Eventbrite lives in ($278.2M payable to creators). Sources: https://terms.law/2025/03/03/when-stripe-holds-your-money-the-definitive-legal-guide-to-getting-your-funds-released/, https://www.lawpla.com/blog/when-stripe-freezes-your-business-funds-legal-solutions-and-protection-strategies/
- **Aggregator model criticism**: merchants share Stripe's master acquiring relationship rather than holding their own MID, so risk scoring is partly portfolio-driven. Source: https://www.servistree.com/blog/is-your-payment-processor-holding-your-funds
- **API onboarding burden** if a platform wants full white-label KYC: mandatory 6-month requirement reviews, explicitly discouraged by Stripe. Source: https://docs.stripe.com/connect/onboarding

## eventbrite_mapping

**What Eventbrite's setup tells us:**
- Eventbrite is merchant of record under EPP and holds/settles creator funds itself. In Stripe terms that is an **indirect charge model**: destination charges or separate charges and transfers, where "the platform is the business of record" and disputes debit the platform balance. This matches Eventbrite's own $10.5M chargeback reserve and $48.0M letter of credit: the liability sits with Eventbrite, exactly as Stripe's indirect-charge model assigns it. Sources: https://docs.stripe.com/connect/charges, https://docs.stripe.com/connect/risk-management
- Organizers must accept the **Stripe Connected Account Agreement**, which creates a direct legal relationship between organizer and Stripe and incorporates the Stripe Services Agreement. That is the **full service agreement** pattern, not recipient-only. Combined with the help-center wording that Eventbrite "uses Stripe to verify... payments" in US/CA/UK/AU, the likely configuration is requirement_collection=stripe with Stripe-driven onboarding (Express-like controller set: platform liable for losses, Stripe collects KYC, express or no dashboard). Exact controller values are NOT VERIFIED, this is inference from the agreement plus verification language. Sources: https://stripe.com/legal/connect-account, https://docs.stripe.com/connect/service-agreement-types
- **21 payout countries with same-region processing**: Stripe Connect requires platform and connected account in the same region for most flows (cross-border only within US/UK/EEA/CH/CA and only without on_behalf_of). Eventbrite's four Stripe countries (US/CA/UK/AU) span regions that mostly cannot be served cross-border from one platform account (AU is not in the cross-border matrix at all), implying per-region Stripe platform accounts or local entities. NOT VERIFIED how Eventbrite legally structures this. Source: https://docs.stripe.com/connect/cross-border-payouts
- **No-FX rule**: "Event Proceeds collected in a currency may only be paid out in the currency in which they are collected" is exactly Stripe's default same-currency settlement, and Stripe's multi-currency settlement (18 currencies, same region) would let Eventbrite keep that rule while expanding. Eventbrite's rule is a subset of what Connect supports; Stripe could also add FX conversion, which Eventbrite chooses not to offer. Source: https://docs.stripe.com/connect/multicurrency-settlement
- **US-only Instant Payout at 3% (min $2.99, max $40 fee)**: Stripe's underlying Instant Payouts cost is 1% with docs explicitly inviting platforms to charge more ("Platforms can realize additional revenue by assessing a fee"). Eventbrite is running a roughly 2-point margin on top of Stripe's rail, and its US-only scope matches launching only where its Stripe platform account has Instant Payouts plus debit-card eligibility. Note Stripe's $9,999 per-payout cap constrains large organizers. Sources: https://docs.stripe.com/connect/instant-payouts, https://stripe.com/connect/pricing
- **$101.1M advance payouts**: advances ahead of collected funds require platform-funded transfers (platform balance or top-ups); Stripe's top-ups use case list includes "Enabling faster payouts (for example, pay a vendor before incoming funds become available)." Source: https://docs.stripe.com/connect/top-ups
- **Holding-period exposure**: tickets sold months ahead plus payout about 5 business days post-event means collection-to-payout can exceed 90 days. Fine in the US (2-year limit), but in non-US markets the 90-day connected-account holding cap pushes Eventbrite to hold at platform level, one reason its non-Stripe markets (Adyen, Braintree, Mercado Pago) run a fully platform-side MoR model. Structuring inference NOT VERIFIED; the 90-day/2-year limits are verified. Source: https://docs.stripe.com/connect/account-balances

## orchestration_reality

**Brutally honest split of what Yuno can and cannot touch:**

**Cleanly orchestrable (pay-in leg):**
- If Eventbrite runs **separate charges and transfers** (platform-level PaymentIntents, transfers decoupled), the pay-in is just a platform charge. An orchestrator can route that authorization to Stripe, Braintree, Adyen, or JPM per BIN/geo/health, retry failed auths across processors, and vault cards processor-agnostically. The Connect machinery only needs money in Eventbrite's Stripe platform balance at transfer time.
- Token portability is workable: Stripe PAN export to any PCI DSS Level 1 processor is documented policy, and an orchestrator-level vault plus network tokens removes single-vault dependence going forward. Link-saved credentials are the exception: they never leave Stripe. Sources: https://docs.stripe.com/get-started/data-migrations/pan-export
- Retries, 3DS orchestration, and smart routing on the four named processors are standard orchestration surface; nothing in Connect prevents Eventbrite from acquiring anywhere for the charge itself when the platform is MoR.

**Awkward but possible:**
- **Feeding Stripe payouts from non-Stripe acquiring**: funds collected on Adyen/JPM must re-enter Stripe via **top-ups** to fund Connect transfers. Verified mechanics: top-ups are GA only in US/UK/Japan (EU/CA/AU/NZ in private preview), ACH credit 1-3 days, wire 1-5 days, UK FPS as fast as 2 hours, and "Adding funds from non-Stripe income" is an explicitly supported use case. The costs are working-capital drag (1-5 day float), treasury ops (no auto-retry of failed transfers after top-up), and preview-status risk in CA/AU. For Eventbrite's AU corridor this is a real gap today. Source: https://docs.stripe.com/connect/top-ups
- **Refunds and disputes split across rails**: a refund of an Adyen-collected payment cannot use Stripe's reverse_transfer to claw funds from the organizer's Connect balance; recovery becomes a manual transfer-reversal or account-debit flow plus cross-system reconciliation. Chargebacks on non-Stripe pay-ins are invisible to the Connect ledger, so Eventbrite's negative-balance offsets stop being automatic. Sources: https://docs.stripe.com/connect/destination-charges?platform=web&ui=elements, https://docs.stripe.com/connect/account-balances

**Not orchestrable (sticky Stripe estate):**
- **Destination charges are inseparable from Connect**: the charge and the transfer_data[destination] split are one object on Stripe. If Eventbrite's US/UK/CA/AU flow uses destination charges, any transaction routed away from Stripe loses the automatic split, the settlement-merchant option, and dispute clawback plumbing. Orchestrating those markets means first refactoring to separate charges and transfers or accepting top-up plumbing. Source: https://docs.stripe.com/connect/charges
- **The Connect ledger itself**: organizer balances, payout schedules, Instant Payouts (and Eventbrite's 2-point margin on them), reserves, debit_negative_balances, and the 90-day/2-year holding rules are proprietary Stripe constructs. No orchestrator can route "a payout" away from Connect without replacing the payout product.
- **KYC state**: organizer verification lives in Stripe Account objects under the Connected Account Agreement; it cannot be exported as verified status. Moving payouts elsewhere means re-KYC of the creator base. Sources: https://docs.stripe.com/connect/service-agreement-types, https://stripe.com/legal/connect-account

**Honest pitch framing for Yuno**: the winnable surface is pay-in routing, vaulting, retries, 3DS, and APM expansion in the markets where Eventbrite is already platform-MoR on Adyen/Braintree/Mercado Pago (all LatAm, EU, APAC card-only markets), plus processor-agnostic failover replacing their homegrown backup logic. The US/UK/CA/AU Stripe Connect estate should be positioned as keep-and-coexist: leave payouts, KYC, and Instant Payouts on Connect, orchestrate in front of it only where charge flows are already platform-level. Claiming an orchestrator can absorb Connect payouts or KYC would be false and will fail technical diligence in a bake-off where Eventbrite explicitly asked how integrations "support marketplace use cases."

## key_facts

- Stripe deprecated the Standard/Express/Custom account trichotomy in favor of controller properties, and its docs now tell new platforms to use the Accounts v2 API (preview version header 2026-07-29.preview). https://docs.stripe.com/connect/migrate-to-controller-properties and https://docs.stripe.com/connect/accounts-v2
- In destination charges and separate charges and transfers the platform is the business of record, and 'with or without on_behalf_of, Stripe debits dispute amounts and fees from your platform account.' https://docs.stripe.com/connect/destination-charges?platform=web&ui=elements
- Direct charges make the connected account the merchant of record; they require the card_payments capability, which recipient-agreement accounts can never hold. https://docs.stripe.com/connect/charges and https://docs.stripe.com/connect/service-agreement-types
- Cross-border Connect flows work only between US, UK, EEA, Canada, and Switzerland, only without on_behalf_of, at a 0.25% fee (waived UK-EEA and intra-EEA). Australia is not in the matrix. https://docs.stripe.com/connect/cross-border-payouts
- Connected account funds can be held at most 90 days in most countries, 2 years in the US, 10 days in Thailand; a hard constraint for an events platform selling tickets months ahead. https://docs.stripe.com/connect/account-balances
- Stripe's Instant Payouts fee is 1% with a $9,999 per-payout cap (USD) and docs explicitly invite platforms to charge extra; Eventbrite charges organizers 3%, roughly a 2-point margin on Stripe's rail. https://docs.stripe.com/connect/instant-payouts and https://stripe.com/connect/pricing
- Connect platform pricing when the platform handles pricing: $2 per monthly active account plus 0.25% + 25 cents per payout sent; account debits cost 1.5%. https://stripe.com/connect/pricing
- Top-ups let a platform fund its Stripe balance from non-Stripe income (explicitly listed use case), but are GA only in US, UK, and Japan, with EU, Canada, Australia, New Zealand in private preview; US ACH credit takes 1-3 days, wires 1-5 days. https://docs.stripe.com/connect/top-ups
- Failed Stripe transfers and payouts are never auto-retried after adding funds; the platform must re-issue every failed movement. https://docs.stripe.com/connect/top-ups
- Multi-currency settlement lets connected accounts hold and pay out in up to 18 currencies without conversion, but platform and connected account must be in the same region. https://docs.stripe.com/connect/multicurrency-settlement
- Stripe will export full PANs, but only processor-to-processor to a PCI DSS Level 1 recipient via 4096-bit PGP, and 'We exclude any credentials saved through Link from our exports.' https://docs.stripe.com/get-started/data-migrations/pan-export
- A connected account's service agreement type can never be changed after acceptance, and verified KYC state has no documented export path, so moving payouts off Connect means re-KYC of the entire creator base. https://docs.stripe.com/connect/service-agreement-types
- Stripe advises against API-built onboarding unless the platform commits to reviewing requirement changes at least every 6 months: 'We don't recommend this option unless you're committed to the operational complexity.' https://docs.stripe.com/connect/onboarding
- When the platform is the losses collector, Stripe may hold reserves on the platform account; when a connected account stays negative 180 days, Stripe zeroes it out from the platform balance (connect_collection_transfer). https://docs.stripe.com/connect/account-balances and https://docs.stripe.com/connect/risk-management
- Global Payouts is Stripe's standalone payouts-without-processing product: US and GB platforms, 60+ recipient countries, marketed example pricing $1.50 per bank payout and $1.50 + 0.75% for instant debit payouts. https://stripe.com/payouts
- Recipient-agreement accounts cannot process payments, and transfers to them take an extra 24 hours to become available. https://docs.stripe.com/connect/service-agreement-types
- The Stripe Connected Account Agreement that Eventbrite organizers accept creates a direct legal relationship between the organizer and Stripe, incorporating the full Stripe Services Agreement. https://stripe.com/legal/connect-account
- Precedent for platform-fund risk: Flipcause filed Chapter 11 in December 2025 owing $29M to nonprofits while Stripe froze $1.45M of its funds citing elevated risk and fought the release in bankruptcy court. https://www.lawpla.com/blog/when-stripe-freezes-your-business-funds-legal-solutions-and-protection-strategies/
- Stripe markets Connect payouts as reaching 118 countries, versus Eventbrite's current 21 payout countries. https://stripe.com/payouts

## sources

- https://docs.stripe.com/connect
- https://docs.stripe.com/connect/charges
- https://docs.stripe.com/connect/accounts
- https://docs.stripe.com/connect/migrate-to-controller-properties
- https://docs.stripe.com/connect/accounts-v2
- https://docs.stripe.com/connect/onboarding
- https://docs.stripe.com/connect/account-balances
- https://docs.stripe.com/connect/payouts-connected-accounts
- https://docs.stripe.com/connect/instant-payouts
- https://docs.stripe.com/connect/cross-border-payouts
- https://docs.stripe.com/connect/multicurrency-settlement
- https://docs.stripe.com/connect/service-agreement-types
- https://docs.stripe.com/connect/top-ups
- https://docs.stripe.com/connect/risk-management
- https://docs.stripe.com/connect/destination-charges?platform=web&ui=elements
- https://docs.stripe.com/global-payouts
- https://stripe.com/payouts
- https://stripe.com/connect/pricing
- https://docs.stripe.com/get-started/data-migrations/pan-export
- https://support.stripe.com/questions/what-if-i-decide-to-leave-stripe-can-i-export-card-data
- https://stripe.com/legal/connect-account
- https://stripe.com/gb/legal/global-payouts
- https://docs.stripe.com/connect/supported-embedded-components/payouts
- https://terms.law/2025/03/03/when-stripe-holds-your-money-the-definitive-legal-guide-to-getting-your-funds-released/
- https://www.lawpla.com/blog/when-stripe-freezes-your-business-funds-legal-solutions-and-protection-strategies/
- https://www.servistree.com/blog/is-your-payment-processor-holding-your-funds
---

# DEEP DIVE 2: ADYEN FOR PLATFORMS

## platform

Adyen for Platforms (Adyen N.V.)

## product_status

## Product names and current state (as of 2026)

- **Current product: "Adyen for Platforms"**, running on what Adyen calls the **balance platform**. Two packaged models sit on top of the same infrastructure: **"Adyen for Platforms"** for platforms whose "brand may be invisible to your users' customers" (supports online + in-person payments and payment facilitators) and **"Adyen for Marketplaces"** where "your brand is known to both your users and their customers" (online payments only) (https://docs.adyen.com/platforms/, https://docs.adyen.com/marketplaces/, https://docs.adyen.com/adyen-for-platforms-model).
- **Legacy product: "classic Adyen for Platforms"** (the MarketPay generation; legacy report names still literally say "Marketpay", e.g. the "Marketpay Balance Report"). The classic docs carry the banner: "This page is for classic Adyen for Platforms integrations. If you are just starting your implementation, refer to our new integration guide instead" (https://docs.adyen.com/classic-platforms, https://docs.adyen.com/classic-platforms/reports-and-fees/marketpay-balance-report). A hard sunset date for classic integrations is NOT VERIFIED in public docs.
- **Customer Area consolidation**: the separate Balance Platform Customer Area was retired; users transitioned to Adyen's unified Customer Area starting Q3 2025, and the old Balance Platform Customer Area is no longer accessible after February 28, 2026 (https://docs.adyen.com/about-our-customer-area).
- **Newest layer: "Intelligent Money Movement"**, announced April 9, 2026, unifying payments, liquidity management, and payouts on one platform, with Etsy, Expedia Group, and Vinted as named users (https://www.adyen.com/press-and-media/adyen-launches-intelligent-money-movement, https://www.prnewswire.com/news-releases/adyen-launches-intelligent-money-movement-to-unify-enterprise-payments-liquidity-management-and-payouts-302738084.html).
- **Onboarding stack**: Legal Entity Management API + Hosted Onboarding are the current KYC front doors (https://docs.adyen.com/platforms/onboard-users/).

## funds_flow_models

## Funds-flow architectures on the balance platform

**1. Standard enterprise merchant account (no Platforms product).** Adyen acquires, settles to the merchant's own bank account, merchant is the contracting merchant and handles its own downstream payouts. This is the plain-acquiring model any orchestrator can route to. Eventbrite could use Adyen this way today (role of Adyen B.V. in Eventbrite's stack is undisclosed; this is the most orchestration-friendly configuration).

**2. Adyen for Platforms / Marketplaces (balance platform).** The platform onboards users as **legal entities / account holders**, each with one or more **balance accounts** (virtual ledger accounts). Payments are authorized on behalf of users and split between balance accounts (https://docs.adyen.com/platforms/, https://docs.adyen.com/platforms/account-structure-resources).
- **Splits at authorization**: a `splits` array in POST `/payments` or `/sessions` with types **BalanceAccount** (sale amount to a user's balance account), **Commission** (to the platform's liable balance account), **PaymentFee**, **Remainder** (leftover after currency conversion), **TopUp** (https://docs.adyen.com/platforms/online-payments/split-transactions/split-payments-at-authorization).
- **Splits at capture**: "split instructions provided at capture override any split instructions provided with the initial payment request"; Adyen recommends splitting at authorization because some payment methods do not support delayed capture (same source). Post-settlement reallocation is possible via internal transfers between balance accounts (Transfers API).
- **Automatic split configuration profiles**: rule-based splitting per store, managed via Customer Area or Management API (`/merchants/{merchantId}/splitConfigurations`) (https://docs.adyen.com/platforms/automatic-split-configuration).
- **Default**: with no split instructions, "the whole transaction amount and fees are booked to your liable balance account" (https://docs.adyen.com/platforms/automatic-split-configuration).

**3. Multi pay-in (third-party acquired volume into the ledger).** "It consolidates all funds processed for your users within Adyen's infrastructure, making it possible for you to combine payments processed by Adyen with third-party acquired volume." A dedicated multi pay-in account receives the third-party PSP's payouts; the platform then allocates funds to balance accounts using `/payments` with split instructions, and can refund third-party payments via `/payments/{pspReference}/refunds`. Restrictions: "Multi pay-in does not support separate authorization and capture" and "you must allocate the funds you receive in your multi pay-in account to the balance accounts in your balance platform within 24 hours" (https://docs.adyen.com/platforms/multi-pay-in/).

**Merchant of record**: Adyen's public docs do NOT explicitly designate who is merchant of record in the Platforms model (checked https://docs.adyen.com/adyen-for-platforms-model and https://www.adyen.com/platform-payments; neither uses the term). What the marketing page does claim: Adyen holds "EU, UK, and US financial licenses," platforms operate "under your brand name," and platforms can "Self-manage your risk for full control, or let Adyen take on the liability" (https://www.adyen.com/platform-payments). NOT VERIFIED: an official Adyen statement that the platform or the sub-merchant is MoR.

## onboarding_kyc

## Sub-merchant onboarding and KYC/KYB

- **Two integration modes**: (1) **Hosted Onboarding**, where "Adyen manages the onboarding flow and user interface," minimal build, supporting organizations, individuals, sole proprietorships, and trusts across 40+ countries; (2) **API-only** via the **Legal Entity Management API** plus Configuration API, where the platform builds its own UI and owns the journey (https://docs.adyen.com/platforms/onboard-users/).
- **Verification**: "Your users' legal entity type and operating country determine the required verification information"; verification starts automatically on submission. Instant bank account verification is available in ~20 markets (US, CA, UK, and most of Western/Northern Europe); ID document scanning can autofill personal details (https://docs.adyen.com/platforms/onboard-users/).
- **Capabilities model**: each account holder gets capabilities that must be verified before use, with statuses pending / valid / invalid / rejected; if verification fails, Adyen sets `allowed: false` on the capability until errors are resolved. Key capabilities: **receivePayments**, **receiveFromPlatformPayments** (receive funds from split payments), **receiveFromBalanceAccount**, **sendToBalanceAccount**, **receiveFromTransferInstrument** (top-ups from verified bank accounts), **sendToTransferInstrument** (payouts to verified bank accounts) (https://docs.adyen.com/platforms/verification-overview/capabilities).
- **Deadlines**: when user data changes, users must "provide the necessary information within a specific deadline" and can keep using capabilities during remediation; exact deadline lengths are not published on that page (https://docs.adyen.com/platforms/verification-overview/capabilities). In the classic-generation docs, suspended account holders who are unsuspended get 42 days to provide information before re-suspension, and classic offered staggered (tiered, volume-based) vs upfront verification (https://docs.adyen.com/classic-platforms/verification-process, https://docs.adyen.com/platforms/quickstart-guide/onboarding-and-kyc).
- **Regulatory responsibility**: Adyen positions itself as the licensed party ("EU, UK, and US financial licenses... We handle compliance globally", https://www.adyen.com/platform-payments); the docs pages reviewed do not contain an explicit allocation-of-regulatory-responsibility statement, so treat precise legal allocation as contract-level, NOT published.
- **Timelines**: no published SLA for verification turnaround. Market commentary reports four-to-eight-week onboarding for higher-risk accounts at Adyen generally (secondary source: https://www.embed.co/blog/adyen-alternatives-for-mid-market-saas-platforms-the-complete-2025-guide).

## ledger_balances

## Ledger, balances, reserves, negative balances

- **Structure**: legal entity -> account holder -> balance account(s). Balance accounts are the ledger; the platform holds its own funds in **liable balance accounts**: "balance accounts that belong to your platform and hold your platform's funds. Funds can be deducted from this account if your users' balance accounts incur negative balances due to refunds and chargebacks" (https://docs.adyen.com/platforms/manage-liable-accounts, https://docs.adyen.com/platforms/account-structure-resources).
- **Holding funds**: split payments can "hold funds until payout" on user balance accounts (https://docs.adyen.com/marketplaces/).
- **Negative balances**: Adyen allows a balance account to stay negative for up to 30 days; a warning webhook fires at 20+ days negative; if not covered before the scheduled date, "Adyen compensates this by debiting your reserved compensation account on the first day of the following month," i.e. the platform's liable account eats it (https://help.adyen.com/knowledge/adyen-for-platforms/funds-transfers/why-do-i-have-a-negative-balance-on-my-platform, https://docs.adyen.com/api-explorer/negative-balance-compensation-warning-webhooks/1/post/balancePlatform.negativeBalanceCompensationWarning.scheduled).
- **Sweeps**: "A sweep automatically pushes out or pulls in funds from a balance account based on a pre-defined schedule, amount, and source or destination," configured in Customer Area or Configuration API (`POST /balanceAccounts/{id}/sweeps`), cron-style schedules supported (https://docs.adyen.com/api-explorer/balanceplatform/2/post/balanceAccounts/(balanceAccountId)/sweeps, https://docs.adyen.com/marketplaces/payout-to-users/scheduled-payouts).
- **Top-ups / external funding**: balance accounts can be funded by push bank transfer from an onboarded, verified external bank account (transferInstrument) once the account holder has the `receiveFromTransferInstrument` capability; scheduled and on-demand top-ups exist (https://docs.adyen.com/platforms/top-up-balance-account, https://docs.adyen.com/issuing/add-manage-funds/external-bank-transfer).
- **Reserves**: Adyen documents a reserve concept at account level (https://docs.adyen.com/account/balances/reserve); a formal rolling-reserve product per sub-merchant on the balance platform is NOT VERIFIED in public docs beyond the liable-account and reserved-compensation mechanics above.

## payouts

## Payouts

- **Three payout modes** on the balance platform: **Managed payouts** ("an optimized, hands-off experience with automatic scheduling, clear end-to-end payout ETAs, and built-in execution tracking"), **Custom payouts** (full control via sweeps and Transfers API), and **Cashout** ("instant access to pending funds before they are settled") (https://docs.adyen.com/platforms/quickstart-guide/payouts).
- **Managed payouts**: schedules on weekdays, weekly, or monthly; payout types Standard (2-day arrival) or Accelerated (1-day); one schedule per currency per balance account; "You can only configure local payouts (within the same country and currency)"; cross-border or multi-currency requires custom payouts (https://docs.adyen.com/platforms/managed-payouts).
- **Custom scheduled payouts**: push sweeps from the user's balance account to their transfer instrument; sales day cycles are 24-hour batches, default midnight to midnight local, closing time configurable up to 07:00 (https://docs.adyen.com/marketplaces/custom-payouts/scheduled-payouts, https://docs.adyen.com/platforms/quickstart-guide/payouts).
- **On-demand payouts**: Transfers API pays out from balance accounts to third-party bank accounts; multiple priorities can be passed in preference order (https://docs.adyen.com/payouts/payout-service/pay-out-to-bank-accounts).
- **Priorities**: Regular; Fast ("processes faster than Regular and incurs higher fees"); Wire ("the fastest option, with the highest fees"); **Instant: "Transfers funds instantly within the United States, Australia, the United Kingdom, and the Single Euro Payments Area (SEPA)"**; Cross-border ("recommended for high-value transfers to recipients in other regions or countries", with possible intermediary bank fees and delays) (https://docs.adyen.com/payouts/payout-service/pay-out-to-bank-accounts).
- **Currency / FX rule**: "Adyen only supports paying out to third parties in local currencies," with two exceptions: EUR within SEPA regions outside the eurozone, and USD to Canada (https://docs.adyen.com/payouts/payout-service/pay-out-to-bank-accounts). On the acquiring side Adyen lets merchants "choose when and in which currency you want to settle" with multi-currency bank accounts (https://www.adyen.com/pricing).
- **Payouts-only mode**: the Payout Service exists for paying out to bank accounts independent of the balance platform (https://docs.adyen.com/payouts/payout-service/pay-out-to-bank-accounts). Instant card payouts (push-to-card) are documented separately (https://docs.adyen.com/online-payments/online-payouts/instant-payouts).
- **Onboarding country coverage** for platform users: 40+ countries via hosted onboarding (https://docs.adyen.com/platforms/onboard-users/); the platform payments page claims 33+ countries in 23 languages, with financial products (accounts, issuing, capital) limited to EU/EEA, UK, and US (https://www.adyen.com/platform-payments, https://docs.adyen.com/issuing). Stripe Connect's cross-border payout country list is broader in raw country count; a precise Adyen payout-country list is NOT published as a single public page, so a hard side-by-side count is NOT VERIFIED.

## liability

## Liability: chargebacks, refunds, fraud

- **Chargebacks, default**: "Adyen withdraws the disputed funds from your platform's liable balance account" (https://docs.adyen.com/platforms/online-payments/split-transactions/split-chargebacks).
- **Chargebacks, configurable** via `platformChargebackLogic`: (1) book the full disputed amount to the platform's liable balance account, (2) book it to one user balance account (`targetAccount`), or (3) "book different amounts to different balance accounts, according to the split ratio defined in the splits array" of the original payment; chargeback fees can be routed via `costAllocationAccount` (https://docs.adyen.com/platforms/online-payments/split-transactions/split-chargebacks).
- **Refunds**: split instructions in the refund request decide who funds the refund; "if a partial refund is initiated without split information, the funds will be debited from the platform's liable account, and not from the accounts specified in the original payment" (https://docs.adyen.com/marketplaces/split-transactions/split-refunds).
- **Invalid split targets**: the API validates only format; if a balance account does not exist or its account holder is closed, "the full transaction and its fees are booked to your platform's liable balance account" (https://docs.adyen.com/platforms/online-payments/split-transactions/split-payments-at-authorization).
- **Negative balances**: user accounts negative for >30 days are compensated from the platform's liable/reserved compensation account, so the platform ultimately eats uncovered user losses (https://help.adyen.com/knowledge/adyen-for-platforms/funds-transfers/why-do-i-have-a-negative-balance-on-my-platform).
- **Risk model choice**: platforms "can decide to take full liability for chargebacks or share the liability with the account holder," and can self-manage risk or "let Adyen take on the liability" (https://www.adyen.com/platform-payments; help.adyen.com Adyen for Platforms knowledge base). Exact commercial terms of the Adyen-takes-liability option are not public.

## pricing

## Published pricing

- Adyen's public pricing is **per-transaction: $0.13 fixed processing fee + a payment-method fee**; cards are Interchange++ (example shown: Visa/Mastercard $0.13 + Interchange+ + 0.60%); "We do not have monthly fees, set-up fees, integration fees or closure fees" but "we do have a minimum invoice depending on industry or business model," and "the fees outlined above are indicative" (https://www.adyen.com/pricing).
- **No public price list exists for Adyen for Platforms itself**: balance platform fees, payout/transfer fees per priority (instant vs regular), onboarding/KYC fees, and multi pay-in fees are all contract-negotiated and NOT published. The docs confirm only that "a payout with a higher priority incurs higher fees" without numbers (https://docs.adyen.com/payouts/payout-service/pay-out-to-bank-accounts).
- Secondary sources report minimum invoices in practice around $120 to EUR 1,000 per month depending on terms (secondary, treat as market color: https://fitsmallbusiness.com/adyen-payments-review/, https://www.embed.co/blog/adyen-alternatives-for-mid-market-saas-platforms-the-complete-2025-guide).

## lock_in

## Lock-in and portability

- **Card tokens: portable out.** Adyen supports token/payment-data export to another PSP: the receiving provider must supply a valid PCI Attestation of Compliance and a PGP key, delivery over SFTP; "Adyen does not charge for migrating payment data," and migration "usually takes 10 days or more" (https://help.adyen.com/en_US/knowledge/ecommerce-integrations/tokenization/how-to-prepare-for-token-migration-export, https://docs.adyen.com/development-resources/migrating-payment-data). Adyen-issued tokens themselves only work at Adyen; the export gives raw card data for re-tokenization.
- **KYC data: not portable.** Legal entities, verification results, and capabilities live in Adyen's Legal Entity Management; there is no documented export of completed verifications to another provider. Moving off means re-running KYC/KYB on every account holder at the new provider. NOT VERIFIED: any Adyen mechanism to export verification artifacts.
- **Balance accounts: not portable.** Balances must be paid out or transferred; ledger history stays in Adyen reports. There is no documented "migrate account holders off the balance platform" tooling.
- **Split logic: embedded in the payment call.** Because splits ride inside `/payments` requests and split configuration profiles live in Adyen's Management API, funds-flow logic is written against Adyen-proprietary objects (https://docs.adyen.com/platforms/online-payments/split-transactions/split-payments-at-authorization, https://docs.adyen.com/platforms/automatic-split-configuration).
- **Even Adyen's own multi-PSP story deepens ledger lock-in**: multi pay-in lets third-party acquired funds enter the Adyen ledger, but allocation, refunds, and payout rails then all run through Adyen APIs (https://docs.adyen.com/platforms/multi-pay-in/).

## limitations

## Known limitations and criticisms

- **Local-currency payout constraint**: third-party payouts only in local currency (exceptions: EUR in non-eurozone SEPA, USD to Canada); managed payouts are local-only, one currency per schedule (https://docs.adyen.com/payouts/payout-service/pay-out-to-bank-accounts, https://docs.adyen.com/platforms/managed-payouts).
- **Financial products geography**: business accounts, issuing, and capital are limited to EEA/EU, UK, and US (https://docs.adyen.com/issuing, https://www.adyen.com/platform-payments). Creator onboarding coverage (40+ countries via hosted onboarding) is heavily weighted to Europe, North America, AU/NZ/SG/HK-type markets; LatAm sub-merchant onboarding coverage is NOT VERIFIED and should be pressure-tested in any bake-off (https://docs.adyen.com/platforms/onboard-users/).
- **Multi pay-in constraints**: no separate auth/capture, and a 24-hour deadline to allocate funds out of the multi pay-in account (https://docs.adyen.com/platforms/multi-pay-in/).
- **Classic-to-new migration burden**: classic MarketPay-generation platforms must rebuild onto the balance platform APIs (new LEM, Transfers, Configuration APIs); classic docs are maintenance-mode (https://docs.adyen.com/classic-platforms).
- **Enterprise gatekeeping**: sales-led onboarding, minimum invoice ("we do have a minimum invoice depending on industry or business model", https://www.adyen.com/pricing); reviewers cite monthly minimums, pricing opacity, and slow onboarding for higher-risk accounts as top complaints (secondary: https://www.embed.co/blog/adyen-alternatives-for-mid-market-saas-platforms-the-complete-2025-guide, https://fitsmallbusiness.com/adyen-payments-review/).
- **Split fragility**: format-only validation of splits means bad balance-account references silently dump full amounts plus fees into the platform's liable account (https://docs.adyen.com/platforms/online-payments/split-transactions/split-payments-at-authorization).
- **Negative-balance exposure**: the platform's liable account backstops all user negatives after 30 days (https://help.adyen.com/knowledge/adyen-for-platforms/funds-transfers/why-do-i-have-a-negative-balance-on-my-platform).

## eventbrite_mapping

## Mapping Adyen for Platforms to Eventbrite EPP

Eventbrite ground truth: Eventbrite is merchant of record under EPP, holds creator funds ($278.2M payable to creators), pays out ~5 business days post-event in 21 countries, US-only Instant Payout at 3% (min $2.99, max $40), "Event Proceeds collected in a currency may only be paid out in the currency in which they are collected. We do not provide currency conversion services," $10.5M chargeback/refund reserve, $101.1M advance payouts, Adyen B.V. already on its sub-processor list with role undisclosed.

**Fit points**
- **No-FX payout rule maps 1:1**: Adyen also "only supports paying out to third parties in local currencies" (https://docs.adyen.com/payouts/payout-service/pay-out-to-bank-accounts). Eventbrite would not need to change its no-conversion policy on Adyen rails.
- **Instant payout upgrade path**: Adyen Instant priority covers US, UK, AU, and SEPA (https://docs.adyen.com/payouts/payout-service/pay-out-to-bank-accounts), wider than Eventbrite's US-only Instant Payout; Adyen Cashout offers "instant access to pending funds before they are settled" (https://docs.adyen.com/platforms/quickstart-guide/payouts), a structural analog to Eventbrite's $101.1M advance-payout program.
- **Reserve/backstop mechanics map**: Eventbrite's $10.5M reserve and offset rights correspond to Adyen's liable balance account plus negative-balance compensation (20-day warning webhook, 30-day tolerance, then debit of the platform's reserved compensation account) and `platformChargebackLogic` options (https://docs.adyen.com/platforms/online-payments/split-transactions/split-chargebacks, https://help.adyen.com/knowledge/adyen-for-platforms/funds-transfers/why-do-i-have-a-negative-balance-on-my-platform).

**Clash points**
- **MoR posture**: under EPP Eventbrite itself is MoR and already operates its own ledger (accounts payable to creators on its balance sheet). Adopting Adyen for Platforms as the ledger means re-onboarding every paid creator through Adyen LEM KYC (capabilities: receiveFromPlatformPayments, sendToTransferInstrument) and rewriting payout logic onto sweeps/Transfers API. That is a re-platforming, not a vendor swap.
- **21 payout countries vs Adyen coverage**: Adyen hosted onboarding covers 40+ countries but skews Europe/NA/APAC (https://docs.adyen.com/platforms/onboard-users/). Eventbrite's MX and AR legs run on Mercado Pago cards today; Adyen balance-platform creator onboarding and local payouts in MX/AR are NOT VERIFIED and must be asked directly in the bake-off.
- **Payouts staying on Stripe Connect**: Eventbrite's help center ties AU/CA/UK/US processing and organizer agreements to Stripe Connect connected accounts. Adyen as a second acquiring leg is trivially compatible only if Adyen settles to Eventbrite's own bank account (standard merchant account, scenario A below) and Eventbrite's ledger keeps feeding Stripe payouts.

**Scenario A: Adyen as a second acquiring leg, payouts remain on Stripe Connect.** Eventbrite (MoR) processes selected geographies/methods on a standard Adyen merchant account; Adyen settles in the collected currency to Eventbrite's own multi-currency bank accounts ("choose when and in which currency you want to settle", https://www.adyen.com/pricing); Eventbrite's internal ledger books the funds and funds Stripe Connect payouts as today. No Adyen Platforms product needed, no creator re-KYC, fully orchestratable. This is plausibly what Adyen B.V. already is in Eventbrite's stack (role undisclosed; NOT VERIFIED).

**Scenario B: Adyen for Platforms as the payout ledger.** Creators become account holders with balance accounts; Adyen-acquired volume splits at authorization; Stripe/Braintree/Mercado Pago volume enters via **multi pay-in** (third-party PSP payouts land in a multi pay-in account, allocated to creator balance accounts within 24 hours via `/payments` with splits; refunds of third-party payments via Adyen's refund endpoint) (https://docs.adyen.com/platforms/multi-pay-in/). Payouts move to managed payouts (local-only, 1-2 day) or sweeps/Transfers API with Instant in US/UK/AU/SEPA. Cost: full creator re-KYC in Adyen LEM, ledger migration off Eventbrite's internal system, multi pay-in's no-separate-auth-capture limitation (Eventbrite does delayed event-cancellation flows), and deep Adyen lock-in of the exact layer Eventbrite currently owns.

## orchestration_reality

## Orchestration reality check (honest)

**Cleanly orchestrable by a layer like Yuno**
- **Pay-in routing to Adyen as plain acquirer** (scenario A): Adyen exposes a standard `/payments` API on a merchant account where Eventbrite is the merchant; an orchestrator can route by geography/BIN/method across Stripe, Braintree, Adyen, and a JPM Chase leg, run failover and retries, and manage 3DS. Eventbrite already hand-built exactly this failover internally, so the orchestrator pitch is replacing home-grown routing code, not adding a new concept.
- **Tokenization**: orchestrator-vaulted cards plus network tokens can be forwarded to Adyen; Adyen also imports payment data from other PSPs free of charge (https://docs.adyen.com/development-resources/migrating-payment-data), and exports out under PCI AoC/PGP process (https://help.adyen.com/en_US/knowledge/ecommerce-integrations/tokenization/how-to-prepare-for-token-migration-export). Card credentials are the most portable asset in this stack.
- **Retries, cascading, smart routing** between acquiring legs: fully realistic as long as settlement lands in Eventbrite's own bank accounts and Eventbrite's own ledger drives payouts.

**Sticky / not realistically orchestrable**
- **The balance platform ledger**: balance accounts, sweeps, liable accounts, and negative-balance compensation are proprietary Adyen constructs with no cross-provider abstraction. No orchestrator can route "the ledger."
- **Splits defined at payment creation**: if Eventbrite adopted Adyen splits, every payment routed to Adyen needs Adyen-specific split payloads, and a payment routed to any other PSP books nothing into the Adyen ledger. Split-at-auth couples routing decisions to the ledger, which is precisely what breaks multi-PSP freedom, unless funds enter via multi pay-in instead.
- **KYC in Adyen LEM**: verified legal entities and capabilities are not exportable; multi-provider payout strategies mean duplicate KYC per provider. Orchestrators do not solve this today.
- **Payout rails**: Transfers API payouts, managed payouts, and Cashout only move money already inside Adyen balance accounts.

**The important nuance for the bake-off**: Adyen DOES accept externally-acquired funds into the ledger. Multi pay-in explicitly "makes it possible for you to combine payments processed by Adyen with third-party acquired volume" (https://docs.adyen.com/platforms/multi-pay-in/), and balance accounts also take push bank-transfer top-ups from verified transfer instruments (https://docs.adyen.com/platforms/top-up-balance-account, https://docs.adyen.com/issuing/add-manage-funds/external-bank-transfer). So Adyen's answer to "we want multiple acquirers" is "keep them, but make my ledger the single payout brain." That is Adyen competing directly with the orchestration layer at the funds-flow level: it neutralizes the multi-acquirer objection while making the stickiest layer (ledger + KYC + payouts) 100% Adyen. For Eventbrite, whose real asset is that it ALREADY owns its ledger and MoR status, the honest orchestrator counter is: keep MoR and the internal ledger, orchestrate the pay-in legs (including Adyen and JPM Chase as plain acquirers), and never hand the ledger to any single PSP, because that is the layer with zero portability.

## key_facts

- Adyen's current platform product is 'Adyen for Platforms' on the balance platform; the MarketPay-era 'classic' docs tell new builders to use the new integration guide (https://docs.adyen.com/classic-platforms)
- Adyen distinguishes marketplaces (your brand known to buyers, online only) from platforms (your brand may be invisible, adds in-person payments) (https://docs.adyen.com/adyen-for-platforms-model)
- Splits ride in the /payments request with types BalanceAccount, Commission, PaymentFee, Remainder, TopUp; splits at capture override splits at authorization (https://docs.adyen.com/platforms/online-payments/split-transactions/split-payments-at-authorization)
- With no split instructions, the whole amount and fees book to the platform's liable balance account; split validation is format-only, so bad account references silently dump funds there too (https://docs.adyen.com/platforms/online-payments/split-transactions/split-payments-at-authorization)
- Chargebacks default to the platform's liable balance account, configurable via platformChargebackLogic to hit one user account or follow the original split ratio (https://docs.adyen.com/platforms/online-payments/split-transactions/split-chargebacks)
- Negative user balances are tolerated 30 days, warned at 20 days by webhook, then compensated from the platform's reserved compensation account on the first of the next month (https://help.adyen.com/knowledge/adyen-for-platforms/funds-transfers/why-do-i-have-a-negative-balance-on-my-platform)
- Payout priorities are Regular, Fast, Wire, Cross-border, and Instant; Instant covers the United States, Australia, the United Kingdom, and SEPA (https://docs.adyen.com/payouts/payout-service/pay-out-to-bank-accounts)
- Adyen only pays out to third parties in local currencies, except EUR in non-eurozone SEPA and USD to Canada, which mirrors Eventbrite's own no-currency-conversion payout rule (https://docs.adyen.com/payouts/payout-service/pay-out-to-bank-accounts)
- Managed payouts (hands-off scheduling, 1-2 day arrival) are local-only, one currency per schedule; cross-border requires custom payouts (https://docs.adyen.com/platforms/managed-payouts)
- Multi pay-in lets platforms combine Adyen-processed and third-party acquired volume in one Adyen ledger, but funds must be allocated within 24 hours and separate auth/capture is not supported (https://docs.adyen.com/platforms/multi-pay-in/)
- Balance accounts accept external push bank-transfer top-ups from verified transfer instruments via the receiveFromTransferInstrument capability (https://docs.adyen.com/platforms/top-up-balance-account)
- Onboarding is Hosted (Adyen-run UI, 40+ countries) or API-only via the Legal Entity Management API; capabilities like receivePayments and sendToTransferInstrument gate usage until verified (https://docs.adyen.com/platforms/onboard-users/, https://docs.adyen.com/platforms/verification-overview/capabilities)
- Published pricing is $0.13 per transaction plus method fee (Visa/Mastercard: Interchange++ + 0.60%), no monthly fees but a minimum invoice by industry; Platforms-specific fees are not public (https://www.adyen.com/pricing)
- Adyen exports tokens/payment data to another PCI AoC-holding PSP free of charge over PGP/SFTP, typically 10+ days; KYC data and balance accounts have no documented export path (https://help.adyen.com/en_US/knowledge/ecommerce-integrations/tokenization/how-to-prepare-for-token-migration-export)
- The separate Balance Platform Customer Area was retired on February 28, 2026 in favor of Adyen's unified Customer Area (https://docs.adyen.com/about-our-customer-area)
- Adyen launched Intelligent Money Movement on April 9, 2026, unifying payments, liquidity, and payouts, citing Etsy, Expedia Group, and Vinted (https://www.adyen.com/press-and-media/adyen-launches-intelligent-money-movement)
- Adyen holds EU, UK, and US financial licenses and offers platforms the choice to self-manage risk or 'let Adyen take on the liability' (https://www.adyen.com/platform-payments)
- Adyen's public docs never explicitly state who is merchant of record in the Platforms model; that allocation is contract-level (https://docs.adyen.com/adyen-for-platforms-model)
- Financial products on the balance platform (business accounts, issuing, capital) are limited to EEA, UK, and US, so LatAm coverage for Eventbrite's MX/AR creator legs must be challenged in the bake-off (https://docs.adyen.com/issuing)

## sources

- https://docs.adyen.com/platforms/
- https://docs.adyen.com/marketplaces/
- https://docs.adyen.com/adyen-for-platforms-model
- https://docs.adyen.com/classic-platforms
- https://docs.adyen.com/classic-platforms/reports-and-fees/marketpay-balance-report
- https://docs.adyen.com/platforms/online-payments/split-transactions/split-payments-at-authorization
- https://docs.adyen.com/platforms/automatic-split-configuration
- https://docs.adyen.com/platforms/online-payments/split-transactions/split-chargebacks
- https://docs.adyen.com/marketplaces/split-transactions/split-refunds
- https://docs.adyen.com/platforms/onboard-users/
- https://docs.adyen.com/platforms/verification-overview/capabilities
- https://docs.adyen.com/platforms/quickstart-guide/onboarding-and-kyc
- https://docs.adyen.com/classic-platforms/verification-process
- https://docs.adyen.com/platforms/manage-liable-accounts
- https://docs.adyen.com/platforms/account-structure-resources
- https://help.adyen.com/knowledge/adyen-for-platforms/funds-transfers/why-do-i-have-a-negative-balance-on-my-platform
- https://docs.adyen.com/api-explorer/negative-balance-compensation-warning-webhooks/1/post/balancePlatform.negativeBalanceCompensationWarning.scheduled
- https://docs.adyen.com/api-explorer/balanceplatform/2/post/balanceAccounts/(balanceAccountId)/sweeps
- https://docs.adyen.com/platforms/quickstart-guide/payouts
- https://docs.adyen.com/platforms/managed-payouts
- https://docs.adyen.com/marketplaces/custom-payouts/scheduled-payouts
- https://docs.adyen.com/payouts/payout-service/pay-out-to-bank-accounts
- https://docs.adyen.com/online-payments/online-payouts/instant-payouts
- https://docs.adyen.com/platforms/multi-pay-in/
- https://docs.adyen.com/platforms/top-up-balance-account
- https://docs.adyen.com/issuing/add-manage-funds/external-bank-transfer
- https://docs.adyen.com/issuing
- https://www.adyen.com/pricing
- https://www.adyen.com/platform-payments
- https://docs.adyen.com/development-resources/migrating-payment-data
- https://help.adyen.com/en_US/knowledge/ecommerce-integrations/tokenization/how-to-prepare-for-token-migration-export
- https://docs.adyen.com/about-our-customer-area
- https://www.adyen.com/press-and-media/adyen-launches-intelligent-money-movement
- https://www.prnewswire.com/news-releases/adyen-launches-intelligent-money-movement-to-unify-enterprise-payments-liquidity-management-and-payouts-302738084.html
- https://docs.adyen.com/account/balances/reserve
- https://fitsmallbusiness.com/adyen-payments-review/
- https://www.embed.co/blog/adyen-alternatives-for-mid-market-saas-platforms-the-complete-2025-guide
---

# DEEP DIVE 3: PAYPAL / BRAINTREE PLATFORM OFFERINGS

## platform

PayPal / Braintree (PayPal Complete Payments Platform, Braintree gateway, PayPal Payouts, Hyperwallet / Enterprise Payouts)

## product_status

**Current product family as of 2026 (verified against live PayPal docs):**

- **PayPal Complete Payments Platform (multiparty)** is the current marketplace/platform product. The multiparty docs hub (https://developer.paypal.com/docs/multiparty/) presents it as "platform and marketplace payment solutions" with two packaged checkouts: "PayPal Checkout" (PayPal, Pay Later, Venmo) and "Expanded Checkout" (adds white-label card fields). It is **approval-gated**: "only available to approved partners"; unapproved API callers get 401 Unauthorized, sandbox is open but going live requires PayPal partner approval (https://developer.paypal.com/docs/multiparty/). This is the lineage successor to "PayPal for Marketplaces" and "PayPal Commerce Platform"; the multiparty URL still answers to the old "PayPal Commerce Platform" search term (https://developer.paypal.com/docs/multiparty/?mark=PayPal+Commerce+Platform).
- **Braintree Marketplace (the sub-merchant split product) is CLOSED to new platforms.** The overview doc still exists but says new merchants "looking for a marketplace solution" must contact Sales, and the product was strictly US-only (master merchant and all sub-merchants US-domiciled) (https://developer.paypal.com/braintree/docs/guides/braintree-marketplace/overview). PayPal shut the service down for existing platforms with a December 15, 2023 migration deadline communicated only via dashboard alerts (https://news.ycombinator.com/item?id=37756664), and the "Marketplace Service Provider Agreement and all references thereto" were removed from Braintree legal terms on November 7, 2024 (https://www.paypal.com/us/legalhub/braintree/past-policy-updates). Treat it as dead.
- **Braintree the gateway/acquirer remains fully live** for standard (single-merchant) acquiring, which is exactly how Eventbrite uses it today. Braintree supports merchants in roughly 45 countries and 130+ presentment currencies (https://developer.paypal.com/braintree/docs/reference/general/currencies, https://www.chargebee.com/docs/payments/2.0/payment-gateways-and-configuration/braintree).
- **PayPal Payouts** (successor of Mass Pay) is live, split into "Standard Payouts" (email/phone/PayPal ID recipients, 20+ currencies, 96 countries) and "Advanced Payouts," which the docs route to Hyperwallet as the enterprise tier (https://developer.paypal.com/docs/payouts/).
- **Hyperwallet has been RENAMED "Enterprise Payouts."** PayPal's own page states "Enterprise Payouts is the new name for Hyperwallet" (https://www.paypal.com/us/business/make-payments/enterprise-payouts); the hyperwallet.com site still runs under the old brand (https://www.hyperwallet.com/). Fully open for new enterprise integrations, custom-priced.
- **Legacy "PayPal for Marketplaces"** (Managed Path / Connected Path naming) survives only in third-party docs (https://support.x-cart.com/en/articles/4660405-paypal-for-marketplaces-overview); the paths were folded into the multiparty/PPCP docs. NOT VERIFIED: any formal deprecation notice with a date; PayPal simply replaced the docs.

## funds_flow_models

**Four distinct architectures, with different merchants of record:**

1. **PPCP multiparty (connected model).** Every seller onboards to their OWN PayPal business account via the Partner Referrals API. An order carries up to 10 `purchase_units`, each with a `payee` (seller `merchant_id` or email); "each purchase unit will result in a separate transaction settled to each of the merchants," and the platform takes its cut via `payment_instruction/platform_fees` inside each purchase unit. Disbursement can be `INSTANT` or delayed (DELAYED holds funds before release to the seller) (https://developer.paypal.com/docs/multiparty/checkout/multiseller-payments/). **The seller is the merchant of record**: funds settle into the seller's PayPal account and "Sellers will handle their disputes through the PayPal Account Resolution Center" (https://developer.paypal.com/docs/multiparty/). This is the structural opposite of Eventbrite's EPP model where Eventbrite is MoR.
2. **Standard Braintree acquiring in the platform's own name.** The platform (Eventbrite) is the direct merchant; Braintree is gateway plus acquiring; 100% of gross settles to the platform's bank account; the platform runs its own creator ledger and payouts. Merchant of record: the platform. This is Eventbrite's current model and it is the model Ticketmaster uses at larger scale ("PayPal Braintree will become Ticketmaster's primary global payment processor," https://business.ticketmaster.com/press-release/paypal-named-the-preferred-payments-partner-of-ticketmaster/). PayPal has no objection to a marketplace being MoR on standard acquiring; the constraint is the platform carries all regulatory/KYC/payout burden itself.
3. **Braintree Marketplace (closed).** Master merchant plus US-only sub-merchants, service fee split, optional escrow ("hold funds in escrow until you decide to disburse them") (https://developer.paypal.com/braintree/docs/guides/braintree-marketplace/overview). Dead end for new work.
4. **Pay-in on any rail + Hyperwallet/Enterprise Payouts for the payout leg.** Platform stays MoR on collections (any acquirer), then funds Hyperwallet and disburses to payees over 11+ transfer methods in 200+ markets (https://www.paypal.com/us/business/make-payments/enterprise-payouts). This decouples acquiring from disbursement and is the architecture Ticketmaster adopted for resale-seller payouts (https://help.ticketmaster.co.uk/hc/en-us/articles/19959004677905).

**PayPal-the-wallet acceptance** is a separate rail from all of the above: it can be reached natively via the Orders API, via Braintree's gateway, or through the platform's existing PSPs; the money always flows through the merchant's PayPal business account relationship.

## onboarding_kyc

**PPCP multiparty:** Onboarding runs through the **Partner Referrals API**, which pre-fills the PayPal signup with data the platform already collected. Three modes: onboard **before payment** (recommended, supports standard and expanded checkout), **after payment** (seller can take payments immediately then complete signup; standard checkout only, business accounts only, excludes vaulting/auth-holds/casual sellers), and **build into software** (self-hosted flow, limits multi-seller purchases and dispute APIs) (https://developer.paypal.com/docs/multiparty/seller-onboarding/). **PayPal carries the compliance burden**: "PayPal screens your sellers and conducts local and global risk and compliance checks" (https://developer.paypal.com/docs/multiparty/). A seller is live when they created the PayPal account, granted the platform permissions, and confirmed email; platforms poll `payments_receivable` and `primary_email_confirmed` status flags (https://developer.paypal.com/docs/multiparty/checkout/save-payment-methods/onboarding/platform/). Timelines are not published.

**Critical implication:** every Eventbrite creator would need their own PayPal business account. That is real onboarding friction for a self-service long tail of casual event organizers versus Eventbrite's current email-plus-bank-details flow.

**Hyperwallet / Enterprise Payouts:** payee onboarding via hosted Pay Portal, embedded widgets, CSV upload, or REST API; PayPal/Hyperwallet performs "KYC/KYB verification and account validation" plus "integrated anti-money laundering and sanctions screening" and offers 1099 tax reporting for US payees (https://www.paypal.com/us/business/make-payments/enterprise-payouts). Hyperwallet operates as a regulated money mover in the US, Canada, UK, EEA, Australia, Singapore and other jurisdictions (https://www.hyperwallet.com/). Ticketmaster's help pages confirm the live operating pattern: "our payment provider (Hyperwallet, a PayPal service) regularly screens information and payments" and may request seller documentation (https://help.ticketmaster.co.uk/hc/en-us/articles/19959004677905).

## ledger_balances

- **PPCP multiparty:** funds sit in each seller's own PayPal balance after capture; the API response exposes `seller_receivable_breakdown` (gross, PayPal fee, net) per merchant. The platform never holds the seller's money; it only receives its `platform_fees`. Timing control is limited to `disbursement_mode` INSTANT vs delayed (https://developer.paypal.com/docs/multiparty/checkout/multiseller-payments/). There is no platform-programmable reserve engine comparable to Eventbrite's internal reserves/offset rights; PayPal applies its own risk holds on PayPal accounts under the PayPal user agreement (a frequent large-merchant complaint, see limitations).
- **Standard Braintree acquiring:** no ledger product at all. Braintree settles net card volume to the merchant's bank account; holding creator funds, advance payouts (Eventbrite's $101.1M advances), chargeback reserves ($10.5M) and offsets all live in the merchant's OWN books. Braintree Marketplace was the only Braintree escrow construct and it is closed (https://developer.paypal.com/braintree/docs/guides/braintree-marketplace/overview).
- **Hyperwallet / Enterprise Payouts:** the platform pre-funds a program account (28 direct funding currencies) and payees hold virtual account balances until they withdraw to their chosen method; Hyperwallet runs payment tracking, screening and compliance holds on those balances (https://www.paypal.com/us/business/make-payments/enterprise-payouts, https://help.ticketmaster.co.uk/hc/en-us/articles/19959004677905). NOT VERIFIED: public documentation of negative-balance/clawback mechanics in Hyperwallet; pricing and program mechanics are behind sales.
- **Negative balance handling in multiparty:** partial-capture behavior exists (HTTP 207, `PARTIALLY_COMPLETED` orders) but seller debit/clawback flows are governed by PayPal account terms, not platform APIs (https://developer.paypal.com/docs/multiparty/checkout/multiseller-payments/).

## payouts

- **PayPal Payouts (Standard):** batch sends to thousands of recipients by email, phone, or PayPal ID, via API, web upload, or file transfer; 20+ currencies, 96 countries; recipients are paid into PayPal (and Venmo in the US) (https://developer.paypal.com/docs/payouts/). Fee: 2% of transaction amount capped per currency; US API payouts cap around $0.25 per payment (https://www.paypal.com/us/business/paypal-business-fees). Limitation for Eventbrite: recipient must claim funds into a PayPal account; not a bank-transfer rail.
- **Hyperwallet / Enterprise Payouts:** 200+ markets, 50+ send currencies, 28 direct funding currencies, 11+ transfer methods: bank account, debit card (push-to-card), prepaid and virtual prepaid cards, PayPal, Venmo, check, eGift cards, PYUSD stablecoin wallets, regional wallets, cash pickup; "near real-time access for wallet and card payouts; same-day for select bank markets"; built-in currency conversion/FX with claimed cost reduction; 1099 reporting (https://www.paypal.com/us/business/make-payments/enterprise-payouts, https://www.hyperwallet.com/).
- **Instant payouts:** Hyperwallet's push-to-debit and wallet payouts are the credible replacement or extension of Eventbrite's US-only 3% Instant Payout; PayPal markets Southwest refunding "several hundred million dollars in under a couple of weeks" via the platform (https://www.paypal.com/us/business/make-payments/enterprise-payouts).
- **Payout in collected currency:** Hyperwallet supports holding/funding in 28 currencies and paying in 50+, so Eventbrite's "no currency conversion" rule can be preserved (fund in collected currency, pay out same currency) or relaxed (offer FX as a feature). NOT VERIFIED: per-corridor FX spreads; pricing is custom.
- **PPCP multiparty payouts:** not applicable as a separate leg; sellers are paid by settlement into their own PayPal accounts at capture (https://developer.paypal.com/docs/multiparty/checkout/multiseller-payments/).
- **Peer signal:** Ticketmaster pays resale sellers through Hyperwallet, typically up to 17 days after sale, with payee choice of method in the seller account (https://help.ticketmaster.co.uk/hc/en-us/articles/19959004677905).

## liability

- **PPCP multiparty:** dispute liability follows the money to the seller. Each purchase unit settles to the seller's PayPal account and "Sellers will handle their disputes through the PayPal Account Resolution Center" (https://developer.paypal.com/docs/multiparty/). The multiparty docs carry a full disputes/chargebacks suite (lifecycle, Disputes API) that the platform can operate on sellers' behalf (https://developer.paypal.com/docs/multiparty/disputes-chargebacks/). Without add-ons, "merchants are responsible for making transaction risk decisions and are liable for any associated chargebacks" on card payments; the paid **Chargeback Protection** tool shifts fraud-chargeback losses to PayPal up to a loss cap when delivery is proven (https://developer.paypal.com/docs/multiparty/checkout/advanced/customize/chargeback-protection/). For Eventbrite this liability model is inverted versus EPP, where Eventbrite absorbs chargebacks centrally, holds a $10.5M reserve, and offsets creators.
- **Standard Braintree acquiring:** classic model; the merchant (Eventbrite) bears 100% of chargeback liability and fees. PayPal's published chargeback fee is $20.00 and dispute fees are $15.00 standard / $30.00 high-volume (https://www.paypal.com/us/business/paypal-business-fees). NOT VERIFIED: Braintree enterprise dispute fees for a merchant of Eventbrite's size (negotiated).
- **PayPal wallet transactions** carry PayPal Seller Protection / Buyer Protection program rules under the PayPal user agreement rather than card-network chargeback rules, which typically lowers card-style chargeback exposure on wallet volume but adds PayPal claim/dispute volume. NOT VERIFIED beyond program existence on the fees/legal pages.

## pricing

**Published list prices (US, from https://www.paypal.com/us/business/paypal-business-fees):**
- Advanced credit/debit (white-label card fields, the PPCP card rate): **2.89% + $0.39** domestic; **+1.50%** on international cards.
- PayPal-branded checkout (wallet): **3.49% + $0.49** domestic.
- Chargeback fee **$20.00**; dispute fee **$15.00** standard, **$30.00** high-volume.
- Currency conversion spread: **3.00% to 4.00%**.
- **PayPal Payouts:** 2% of payout amount with per-currency caps (US API payouts cap around $0.25 per payment).

**Not published:** PPCP multiparty partner economics (platform fee revenue shares, partner rates) are negotiated after partner approval (https://developer.paypal.com/docs/multiparty/). **Hyperwallet / Enterprise Payouts is explicitly "custom pricing"** based on volume and ticket size (https://www.paypal.com/us/business/make-payments/enterprise-payouts). Braintree gateway/interchange-plus enterprise rates: negotiated, not public. At Eventbrite's >$3.0B volume everything material is a negotiated contract; the list prices above only matter as ceilings.

## lock_in

**Braintree is one of the LEAST locked-in enterprise gateways on card data:**
- Official policy: "Your data belongs to you. That's why we support credit card data portability... we'll import your sensitive customer data into your new Braintree gateway, as well as export it if you ever need to leave" and "We do not charge any fees for data migrations" (https://developer.paypal.com/braintree/articles/get-started/data-migration/overview).
- Export mechanics: receiving processor must supply a **PCI compliance attestation**; Braintree encrypts to the receiver's public key and delivers a **GPG-encrypted CSV** over SFTP/SCP/FTPS containing customers plus card records **including network transaction identifiers** (critical for migrating merchant-initiated/stored-credential transactions without re-consent) (https://developer.paypal.com/braintree/articles/get-started/data-migration/exports).
- Hard limits: **maximum two exports** (bulk plus catch-up); **Apple Pay and Google Pay tokens are NOT transferable** ("secure tokens associated with Apple Pay and Google Pay network transactions are not transferrable between providers"); **subscriptions and transaction history cannot be migrated** (https://developer.paypal.com/braintree/articles/get-started/data-migration/overview).

**PayPal wallet tokens (billing agreements / vaulted PayPal):**
- Vaulted PayPal in Braintree is a billing agreement keyed to the merchant's **PayPal Business Account**, not to the gateway: Braintree's import docs require that "The PayPal Business Account used to create your billing agreements must match the PayPal Business Account linked to your Braintree gateway" (https://developer.paypal.com/braintree/articles/get-started/data-migration/imports). Practical consequence: if Eventbrite keeps the same PayPal business account, its agreements are importable into Braintree and remain anchored at PayPal even if card acquiring moves. NOT VERIFIED: an official PayPal statement covering the reverse direction (using Braintree-created billing agreement IDs through the native PayPal REST APIs); flag as a diligence question for PayPal.
- Moving CARD volume off Braintree does not touch PayPal wallet acceptance at all; the wallet runs on the PayPal account relationship, reachable natively or through most major PSPs and orchestrators.

**PPCP multiparty lock-in:** seller PayPal accounts and platform-level vault tokens (Payment Method Tokens API, platform-level vaulting where "a payer saves their payment method... and can then use their saved payment method with any merchant on the marketplace," https://developer.paypal.com/docs/multiparty/checkout/save-payment-methods/onboarding/platform/) live inside PayPal; there is no published export path for multiparty vault tokens. NOT VERIFIED: any portability commitment for PPCP vault tokens equivalent to Braintree's.

**Hyperwallet lock-in:** payee KYC records and stored transfer methods sit in Hyperwallet's program; no published export/portability policy. NOT VERIFIED.

## limitations

- **Braintree Marketplace shutdown is the cautionary tale:** existing platforms got a dashboard-only notice and a December 15, 2023 deadline; users called out "no public announcement, email notification, or press release" and a broader "enshitification since Paypal purchased them" (https://news.ycombinator.com/item?id=37756664); the legal agreement was scrubbed November 7, 2024 (https://www.paypal.com/us/legalhub/braintree/past-policy-updates). PayPal has exited the marketplace split-payments business once already.
- **PPCP multiparty is approval-gated and PayPal-account-centric:** partners must be approved (401 until then) and every seller must open a PayPal business account and confirm email before receiving funds (https://developer.paypal.com/docs/multiparty/, https://developer.paypal.com/docs/multiparty/seller-onboarding/). Heavy friction for a casual-organizer long tail; the old X-Cart description of the Connected Path noted it "binds your vendors to use PayPal Business accounts" (https://support.x-cart.com/en/articles/4660405-paypal-for-marketplaces-overview).
- **10 purchase units per order** caps basket-level multi-seller checkout (https://developer.paypal.com/docs/multiparty/checkout/multiseller-payments/).
- **No platform-controlled ledger:** in multiparty, funds go to seller PayPal balances; platform reserve/offset logic like Eventbrite's advance-payout and negative-balance offsets has no first-class API. Delayed disbursement is the only hold primitive (https://developer.paypal.com/docs/multiparty/checkout/multiseller-payments/).
- **PayPal risk holds and account reserves** on merchant/seller PayPal balances are governed by PayPal's user agreement and applied unilaterally; a long-standing merchant complaint (context: https://news.ycombinator.com/item?id=37756664).
- **FX spread of 3 to 4%** on cross-currency PayPal flows is expensive at scale (https://www.paypal.com/us/business/paypal-business-fees).
- **Apple Pay / Google Pay tokens and subscription state are non-portable** from Braintree, so recurring/wallet volume needs re-tokenization on exit (https://developer.paypal.com/braintree/articles/get-started/data-migration/overview).
- **Hyperwallet pricing opacity:** custom-only pricing, no public rate card (https://www.paypal.com/us/business/make-payments/enterprise-payouts).
- **Braintree merchant-domicile footprint (~45 countries, 130+ currencies)** is solid but smaller than Adyen/Stripe for some emerging markets; MX and AR acquiring is why Eventbrite runs Mercado Pago there (https://www.chargebee.com/docs/payments/2.0/payment-gateways-and-configuration/braintree).

## eventbrite_mapping

**How each PayPal asset maps to Eventbrite's EPP reality (Eventbrite = MoR, 21 payout countries, no FX, reserves and offsets, US-only 3% instant payout):**

- **Standard Braintree acquiring (current state) fits EPP perfectly and changes nothing structurally.** Eventbrite already runs Braintree for card acquiring in US, UK, IE, DE, NL, ES, CA, AU (live checkout flags) alongside Stripe in US/CA/UK/AU. Eventbrite keeps MoR status, its own $278.2M creator-payable ledger, reserves, offsets and no-FX payout rule. Braintree is a routable gateway here, nothing more.
- **PPCP multiparty CLASHES with EPP head-on:** it makes each creator the merchant of record with their own PayPal business account, moves funds out of Eventbrite's control at capture, relocates disputes to the creator's Resolution Center, and offers no reserve/offset engine (https://developer.paypal.com/docs/multiparty/, https://developer.paypal.com/docs/multiparty/checkout/multiseller-payments/). Adopting it would mean dismantling EPP economics (float on $278.2M payables, advance-payout product, central chargeback management). It is the wrong architecture for Eventbrite unless they deliberately want to de-risk MoR status, which nothing in the 10-K suggests.
- **Braintree Marketplace is not an option:** closed to new platforms, US-only when it existed (https://developer.paypal.com/braintree/docs/guides/braintree-marketplace/overview, https://www.paypal.com/us/legalhub/braintree/past-policy-updates).
- **Hyperwallet / Enterprise Payouts is the genuinely interesting piece:** it could replace or extend Eventbrite's payout leg beyond 21 countries to 200+ markets, honor the no-FX rule (fund and pay in collected currency across 28 funding / 50+ payout currencies), and generalize the US-only 3% Instant Payout into global near-real-time push-to-card/wallet payouts, with Hyperwallet absorbing payee KYC and 1099 reporting (https://www.paypal.com/us/business/make-payments/enterprise-payouts). Direct peer proof: Ticketmaster, whose card volume also runs on Braintree, pays resale sellers via Hyperwallet (https://business.ticketmaster.com/press-release/paypal-named-the-preferred-payments-partner-of-ticketmaster/, https://help.ticketmaster.co.uk/hc/en-us/articles/19959004677905). Expect PayPal to lead with exactly this Ticketmaster story in the bake-off.
- **PayPal wallet + Pay in 3/4 acceptance is routing-independent:** it lives on Eventbrite's PayPal business account. Moving card volume from Braintree to Adyen, Stripe, JPM or Yuno-routed acquirers does not degrade PayPal/Venmo/Pay Later acceptance or (per the billing-agreement-follows-the-PayPal-account model) the vaulted PayPal agreements, provided the same PayPal business account stays live (https://developer.paypal.com/braintree/articles/get-started/data-migration/imports). One caveat to confirm with PayPal: exercising Braintree-created billing agreement IDs through non-Braintree integrations is NOT VERIFIED in public docs.
- **Card vault portability is a non-issue:** Braintree exports card PANs with network transaction IDs, free, to any PCI L1 recipient, so Eventbrite's Braintree-vaulted cards can be mirrored into an orchestrator vault; only Apple Pay / Google Pay device tokens would need re-provisioning (https://developer.paypal.com/braintree/articles/get-started/data-migration/exports, https://developer.paypal.com/braintree/articles/get-started/data-migration/overview).
- **Pricing leverage:** published ceilings (2.89% + $0.39 advanced cards, 3.49% + $0.49 PayPal button, https://www.paypal.com/us/business/paypal-business-fees) are irrelevant at $3B; but the 3 to 4% PayPal FX spread is a real argument for keeping the no-FX payout design or negotiating Hyperwallet FX hard.

## orchestration_reality

**What an orchestrator like Yuno can genuinely do here:**

- **Card routing through Braintree: clean.** Braintree is a standard gateway/acquirer with full server-side APIs; an orchestrator can tokenize once in its own vault, route card authorizations between Braintree, Stripe, Adyen, Cybersource and a new JPM Chase connection, run failover and retries, and replace the failover logic Eventbrite hand-built ("multiple integrations... back up processing alternatives" per their 10-K). Braintree's free PAN export with network transaction IDs makes the initial vault migration into an orchestrator vault straightforward (https://developer.paypal.com/braintree/articles/get-started/data-migration/exports). This is the strongest, most honest part of the pitch.
- **PayPal-the-wallet: orchestrable but shallow.** PayPal can be reached natively (Orders API) or via the Braintree gateway; an orchestrator can present the button, manage the session, and record the result in one ledger. But there is only ONE PayPal; you cannot route PayPal volume between competing processors for auth-rate gains, and the funds always land in Eventbrite's PayPal business account. Value-add is limited to unified reporting, reconciliation, retry hygiene and vault continuity, not routing arbitrage. Venmo and Pay in 3/4 similarly only exist on PayPal rails.
- **Vaulted PayPal agreements: mostly sticky to PayPal, not to Braintree.** Agreements key to the PayPal business account (https://developer.paypal.com/braintree/articles/get-started/data-migration/imports); an orchestrator can likely keep charging them so long as the integration (Braintree or native) stays connected to the same account, but the Braintree-ID-to-native-API path is NOT VERIFIED and must be tested; do not promise it.
- **NOT orchestrable / sticky:** (1) Eventbrite's proprietary creator ledger, reserves, advance payouts and offset rights are Eventbrite's own books; no orchestrator or PSP replaces that without a ledger product. (2) Hyperwallet payouts are a closed program: payee KYC records, virtual balances and transfer methods live inside PayPal's regulated entity with no published portability, so if Eventbrite adopts Hyperwallet, that leg is PayPal-sticky (https://www.paypal.com/us/business/make-payments/enterprise-payouts). (3) Apple Pay / Google Pay tokens vaulted at Braintree cannot be exported and would re-provision through the orchestrator (https://developer.paypal.com/braintree/articles/get-started/data-migration/overview). (4) PPCP multiparty, if ever adopted, would put checkout, vault and seller accounts inside an approval-gated PayPal partner program that no third-party orchestrator can sit inside.
- **Honest bake-off framing for the call:** PayPal's best card in this deal is Hyperwallet plus the Ticketmaster reference, which addresses payouts, a domain orchestrators typically do not own. Yuno's counter is that pay-in routing, failover, unified tokenization and multi-acquirer redundancy (including adding JPM Chase) are exactly what PayPal cannot neutrally provide, since PayPal will always route to itself; and that Eventbrite keeps MoR, ledger and payout control regardless.

## key_facts

- Braintree Marketplace, the sub-merchant split product, is closed: new platforms are told to 'contact our Sales team' and it was always US-only for master and sub-merchants (https://developer.paypal.com/braintree/docs/guides/braintree-marketplace/overview)
- PayPal shut Braintree Marketplace for existing platforms with a December 15, 2023 deadline announced only via dashboard alerts, no public notice (https://news.ycombinator.com/item?id=37756664)
- The Braintree 'Marketplace Service Provider Agreement and all references thereto' were removed from Braintree legal terms on November 7, 2024 (https://www.paypal.com/us/legalhub/braintree/past-policy-updates)
- PayPal Complete Payments Platform multiparty is 'only available to approved partners'; unapproved API callers get 401 Unauthorized (https://developer.paypal.com/docs/multiparty/)
- In PPCP multiparty each purchase unit settles to the seller's own PayPal account and 'Sellers will handle their disputes through the PayPal Account Resolution Center', i.e. the seller, not the platform, is merchant of record (https://developer.paypal.com/docs/multiparty/)
- PPCP multiparty orders max out at 10 purchase units (sellers) per order, with platform fees set per purchase unit via payment_instruction/platform_fees (https://developer.paypal.com/docs/multiparty/checkout/multiseller-payments/)
- In PPCP multiparty 'PayPal screens your sellers and conducts local and global risk and compliance checks', but every seller must open a PayPal business account and confirm email before payments are receivable (https://developer.paypal.com/docs/multiparty/, https://developer.paypal.com/docs/multiparty/seller-onboarding/)
- Hyperwallet has been renamed: 'Enterprise Payouts is the new name for Hyperwallet' (https://www.paypal.com/us/business/make-payments/enterprise-payouts)
- Enterprise Payouts/Hyperwallet covers 200+ markets, 50+ send currencies, 28 direct funding currencies and 11+ methods including bank, push-to-debit, PayPal, Venmo, check, prepaid, eGift, cash pickup and PYUSD, with near real-time wallet and card payouts (https://www.paypal.com/us/business/make-payments/enterprise-payouts)
- Hyperwallet handles payee KYC/KYB, AML and sanctions screening plus US 1099 tax reporting, taking that burden off the platform (https://www.paypal.com/us/business/make-payments/enterprise-payouts)
- PayPal Payouts (Standard) sends to recipients by email, phone or PayPal ID in 20+ currencies across 96 countries; list fee is 2% capped per currency, about $0.25 per US API payout (https://developer.paypal.com/docs/payouts/, https://www.paypal.com/us/business/paypal-business-fees)
- Braintree card data portability is official and free: 'we'll... export it if you ever need to leave' and 'We do not charge any fees for data migrations' (https://developer.paypal.com/braintree/articles/get-started/data-migration/overview)
- Braintree vault exports require a PCI attestation from the receiving processor and are limited to a maximum of two exports, delivered as GPG-encrypted CSV including network transaction identifiers (https://developer.paypal.com/braintree/articles/get-started/data-migration/exports)
- Apple Pay and Google Pay tokens are excluded from Braintree exports ('not transferrable between providers') and subscription/transaction history cannot be migrated (https://developer.paypal.com/braintree/articles/get-started/data-migration/overview)
- PayPal billing agreements are keyed to the merchant's PayPal Business Account, not the gateway: Braintree imports require the same PayPal Business Account that created the agreements (https://developer.paypal.com/braintree/articles/get-started/data-migration/imports)
- PayPal Braintree is Ticketmaster's primary global payment processor under the April 3, 2023 Live Nation deal naming PayPal 'Preferred Payments Partner of Ticketmaster' across 21 countries (https://business.ticketmaster.com/press-release/paypal-named-the-preferred-payments-partner-of-ticketmaster/)
- Ticketmaster pays resale sellers through 'our payment provider (Hyperwallet, a PayPal service)', typically up to 17 days after sale, direct peer proof for the Eventbrite payout use case (https://help.ticketmaster.co.uk/hc/en-us/articles/19959004677905)
- Published US list rates: advanced card fields 2.89% + $0.39 (plus 1.50% international), PayPal-branded checkout 3.49% + $0.49, chargeback fee $20, dispute fees $15/$30, FX spread 3 to 4% (https://www.paypal.com/us/business/paypal-business-fees)
- Braintree supports merchants in about 45 countries with 130+ presentment currencies, which is why Eventbrite needs Mercado Pago for Mexico/Argentina acquiring (https://www.chargebee.com/docs/payments/2.0/payment-gateways-and-configuration/braintree, https://developer.paypal.com/braintree/docs/reference/general/currencies)
- Hyperwallet/Enterprise Payouts pricing is custom-only, no public rate card (https://www.paypal.com/us/business/make-payments/enterprise-payouts)

## sources

- https://developer.paypal.com/docs/multiparty/
- https://developer.paypal.com/docs/multiparty/checkout/multiseller-payments/
- https://developer.paypal.com/docs/multiparty/seller-onboarding/
- https://developer.paypal.com/docs/multiparty/checkout/save-payment-methods/onboarding/platform/
- https://developer.paypal.com/docs/multiparty/disputes-chargebacks/
- https://developer.paypal.com/docs/multiparty/checkout/advanced/customize/chargeback-protection/
- https://developer.paypal.com/braintree/docs/guides/braintree-marketplace/overview
- https://www.paypal.com/us/legalhub/braintree/past-policy-updates
- https://news.ycombinator.com/item?id=37756664
- https://developer.paypal.com/braintree/articles/get-started/data-migration/overview
- https://developer.paypal.com/braintree/articles/get-started/data-migration/exports
- https://developer.paypal.com/braintree/articles/get-started/data-migration/imports
- https://developer.paypal.com/docs/payouts/
- https://www.paypal.com/us/business/make-payments/enterprise-payouts
- https://www.hyperwallet.com/
- https://www.paypal.com/us/business/paypal-business-fees
- https://business.ticketmaster.com/press-release/paypal-named-the-preferred-payments-partner-of-ticketmaster/
- https://help.ticketmaster.co.uk/hc/en-us/articles/19959004677905
- https://www.paypal.com/us/cshelp/article/what-is-hyperwalletpayouts-help1129
- https://support.x-cart.com/en/articles/4660405-paypal-for-marketplaces-overview
- https://www.chargebee.com/docs/payments/2.0/payment-gateways-and-configuration/braintree
- https://developer.paypal.com/braintree/docs/reference/general/currencies
---

# DEEP DIVE 4: J.P. MORGAN PAYMENTS

## platform

J.P. Morgan Payments (heritage Chase Paymentech / Chase Merchant Services)

## product_status

## What "JPM Chase" actually is in 2026

There is no product called "JPM for Platforms". The relevant umbrella is **J.P. Morgan Payments**, with these named components:

- **Merchant acquiring / Commerce Solutions**: J.P. Morgan is "#1 Merchant acquirer in the U.S." and "#1 European ecommerce acquirer for 10 years running", and states the firm processes "over $10T in payments every day" (firmwide, not acquiring-only) (https://www.jpmorgan.com/payments/solutions/commerce). The #1 US acquirer claim is corroborated by Nilson: largest acquirer of card payments from US merchants in 2024 with 40.98B transactions, ahead of Fiserv and Worldpay (https://www.globenewswire.com/news-release/2025/04/10/3059175/0/en/top-acquirers-of-card-payments-at-us-merchants.html) and by JPM's own press release (https://media.chase.com/news/jpmorgan-named-number-one-merchant-acquirer-in-the-us).
- **Online Payments API** (developer.payments.jpmorgan.com): the modern single integration covering "the entire payments lifecycle for multiple methods of payment, including card payments, alternative methods of payment, and wallet payments", offered as Direct API, Checkout (pre-built), drop-in UIs and payment links (https://developer.payments.jpmorgan.com/docs/commerce/online-payments, https://www.jpmorgan.com/payments/solutions/commerce). Industry commentary describes the underlying cloud acquiring platform as "Helix" (https://www.fintechwrapup.com/p/deep-dive-jpmorgans-payments-strategy); "Helix" is not a customer-facing product name on jpmorgan.com. NOT VERIFIED as official branding.
- **Legacy gateway: Orbital (Chase Paymentech)**, on the Salem and Tampa host platforms. Third-party docs now flag it as sunset for new business: Chargebee states "Orbital is now deprecated... new onboarding is no longer available" (https://www.chargebee.com/docs/payments/2.0/payment-gateways-and-configuration/orbital) and PaymentsOS lists "Chase Paymentech (deprecated)" (https://developers.paymentsos.com/docs/connect/partner-providers/chase-paymentech.html). JPM itself still documents Orbital (https://secure.paymentech.com/mcp/protected/documents/product_sheets/orbital_gateway.pdf). Flag: any orchestrator claiming a "Chase" connector must be asked whether it is legacy Orbital or the new Online Payments API.
- **Embedded Payments (Embedded Finance solutions)**: "a powerful solution designed to give platforms the ability to power payouts" via "a single API", including client onboarding with "built-in verification from J.P. Morgan", accounts, and payouts (https://developer.payments.jpmorgan.com/docs/embedded-finance-solutions/embedded-payments).
- **Payment facilitation solutions**: JPM as sponsor/acquirer for payfacs, "The path to pay-in, pay-out and banking is one path — not three or four" (https://www.jpmorgan.com/payments/solutions/payment-facilitation, https://www.jpmorgan.com/insights/payments/embedded-finance-baas/payfac-101).
- **Chase Payment Solutions**: the SMB-facing brand (https://www.chase.com/business/payments); not the vehicle for an Eventbrite-scale deal.
- **WePay (acquired Dec 2017)**: effectively absorbed. JPM's own May 13, 2024 article: "we have integrated WePay's capabilities into the broader J.P. Morgan Payments suite" and "we recently evaluated all ISV relationships and ended certain agreements" (https://www.jpmorgan.com/insights/payments/merchant-services/wepay-integration). The Information reported WePay "abruptly dumps business customers" in early 2024 (https://www.theinformation.com/articles/jpmorgans-wepay-abruptly-dumps-business-customers). The wepay.com site currently fails with an expired TLS certificate (checked 2026-08-04). WePay is not a live standalone option for Eventbrite.

## funds_flow_models

## Funds-flow models JPM sells to a marketplace like Eventbrite

1. **Direct merchant acquiring (merchant = MoR)**. Eventbrite contracts as the merchant; JPM acquires and settles gross card proceeds to Eventbrite's bank account; Eventbrite remains merchant of record and runs its own creator ledger and payouts. This is the classic Chase Paymentech model and the natural fit for EPP, where Eventbrite already is MoR. Sold under Commerce Solutions / Online Payments (https://www.jpmorgan.com/payments/solutions/commerce, https://developer.payments.jpmorgan.com/docs/commerce/online-payments).
2. **Payment facilitation sponsorship (platform = payfac, sub-merchants = MoR-ish)**. JPM is "an acquiring bank, a direct processor, and also connected to one of the largest card issuers in the U.S." and sponsors payfacs; onboarding, pay-in, pay-out and operations are the four pillars they describe (https://www.jpmorgan.com/payments/solutions/payment-facilitation, https://www.jpmorgan.com/insights/payments/embedded-finance-baas/pathtopayfac). Under this model each event creator could become a sub-merchant; this would be a structural change from EPP's MoR model.
3. **Embedded Payments (platform holds/moves money via JPM accounts)**. Platforms "onboard clients faster with built-in verification from J.P. Morgan", "create and manage accounts for clients and counterparties" including "fully routable virtual accounts for each counterparty", and "trigger payouts across currencies and payment methods at scale" via one API (https://developer.payments.jpmorgan.com/docs/embedded-finance-solutions/embedded-payments). Closest JPM analog to Stripe Connect's account+payout layer, but a treasury/banking product, not a Connect clone.
4. **Marketplace embedded finance (multi-party payables)**. JPM's Oct 16, 2025 blog "Powering Marketplaces with Embedded Finance Solutions" describes a hosted solution (product named **Concourse**) to manage third-party suppliers and bank details, tokenization, and payout management including "state-specific regulatory navigation" (https://developer.payments.jpmorgan.com/blog/product/powering-marketplaces-embedded-finance-solutions).
5. **Payouts-only rails**: Push to Card and RTP/FedNow via the Global Payments API, usable without JPM acquiring (https://developer.payments.jpmorgan.com/docs/treasury/global-payments/capabilities/global-payments/push-to-card).

For Eventbrite specifically, model 1 (direct acquiring, Eventbrite stays MoR) is the only one that fits the current EPP architecture without re-papering creators.

## onboarding_kyc

## Onboarding and KYC

- **Merchant onboarding (Eventbrite as the client)**: enterprise contract with underwriting. JPM's Digital Onboarding docs: "In order to process payments and receive settlement payouts, your client must be fully onboarded", requiring "basic business and personal information", an EIN-type identifier, and "answers to due diligence questions served by the API", with KYC via a Customer Identification Program (CIP) (https://developer.payments.jpmorgan.com/docs/commerce/optimization-protection/capabilities/digital-onboarding). Onboarding can be staggered: "you can stagger the process by taking the most basic information first."
- **Progressive underwriting** (WePay heritage): "allows J.P. Morgan Payments to re-underwrite relationship risk with each incremental transaction in real-time and at scale" (https://www.jpmorgan.com/insights/payments/merchant-services/wepay-integration).
- **Sub-merchant/creator KYC**: under direct acquiring, JPM does NOT KYC Eventbrite's creators; Eventbrite keeps that (today it is delegated to Stripe Connect in US/CA/UK/AU per Eventbrite's help center). Under payfac sponsorship or Embedded Payments, JPM's verification applies to onboarded clients/counterparties (https://developer.payments.jpmorgan.com/docs/embedded-finance-solutions/embedded-payments).
- **Regulatory responsibility**: in the payfac model, "the acquirer remains responsible for the acts of both the PayFac and the sponsored merchants" (https://www.jpmorgan.com/insights/payments/embedded-finance-baas/payfac-101 as summarized in JPM/industry material).
- **Timelines**: no public SLA. Enterprise acquiring deals of this size are multi-month sales-plus-underwriting cycles. Industry-standard knowledge, NOT VERIFIED from JPM sources.

## ledger_balances

## Where funds live

- **Direct acquiring**: JPM settles card proceeds to the merchant's designated bank account. JPM's pitch is that acquiring plus settlement banking is one stack: "The path to pay-in, pay-out and banking is one path — not three or four" (https://www.jpmorgan.com/payments/solutions/payment-facilitation). Settling into a JPM DDA collapses acquirer-to-bank hops; Eventbrite would then fund its $278.2M creator payable and its payout runs from that account (Eventbrite side from its 10-K, ground truth provided).
- **Embedded Payments**: platforms get "limited accounts" and "fully routable virtual accounts for each counterparty" and can "move money into and out of accounts you manage and on behalf of your clients" (https://developer.payments.jpmorgan.com/docs/embedded-finance-solutions/embedded-payments). This is the JPM-side ledger option if Eventbrite ever wanted bank-held creator balances instead of an internal payable.
- **Reserves / negative balances**: JPM enterprise merchant agreements include reserve and offset rights for future-delivery businesses. Industry-standard knowledge; specific JPM reserve terms are contract-level and NOT VERIFIED from public sources. Relevant because Eventbrite already carries a $10.5M chargeback/refund reserve and a $48.0M letter of credit, and an acquirer underwriting a ticketing MoR will price and collateralize that same event-delivery risk.
- **Escrow/for-benefit-of structures**: not publicly documented for Commerce Solutions; Concourse (marketplace payables) manages supplier bank details and payout flows, not buyer-funds escrow (https://developer.payments.jpmorgan.com/blog/product/powering-marketplaces-embedded-finance-solutions).

## payouts

## Payouts capabilities

- **Push to Card**: disbursements to any "Visa or Mastercard-branded debit or reloadable prepaid card"; "funds become available in near-real time, typically within about 30 seconds, with a network service level agreement (SLA) of 30 minutes"; up to $125,000 per transaction ($50,000 for money-transfer use cases); US and Canada (Canada Visa-only with fast-funds caveats); explicit use cases include "marketplace payouts" and gig economy (https://developer.payments.jpmorgan.com/docs/treasury/global-payments/capabilities/global-payments/push-to-card). JPM also announced a Visa Direct collaboration for faster domestic payments (https://www.pymnts.com/real-time-payments/2024/jpmorgan-offers-faster-domestic-payments-via-visa-direct/).
- **RTP and FedNow**: Chase participates in both US instant rails, and "with one API integration, clients can access both the FedNow Service and TCH RTP rails" (https://www.jpmorgan.com/payments/solutions/fednow, https://www.jpmorgan.com/insights/payments/real-time-payments/instant-payments-understanding-rtp-and-fednow-service).
- **Embedded Payments payouts**: "trigger payouts across currencies and payment methods at scale" for "clients on their platform, payouts for themselves or to any external counterparty" (https://developer.payments.jpmorgan.com/docs/embedded-finance-solutions/embedded-payments).
- **Acquiring settlement schedule**: enterprise-negotiated; no public schedule. NOT VERIFIED / custom.
- Relevance to Eventbrite: US-only Instant Payouts at 3% is Eventbrite's current premium product; JPM's RTP/FedNow/Push to Card rails are the bank-grade way to run instant creator payouts in the US, independent of who acquires the card transaction. This is a genuine JPM strength versus a pure acquirer.

## liability

## Liability and risk

- **Direct acquiring (Eventbrite = MoR)**: the merchant carries chargeback and refund liability; the acquirer carries credit exposure if the merchant fails to cover them, which is why acquirers demand reserves/collateral from future-delivery merchants. Industry-standard knowledge; JPM's specific terms are contract-level, NOT VERIFIED publicly. JPM publishes dispute/chargeback mitigation tooling under "Insights, Optimization & Protection" ("mitigate the impact of disputes") (https://www.jpmorgan.com/payments/solutions/commerce, https://www.jpmorgan.com/payments/solutions/commerce/optimization-protection).
- **Payfac model**: "the acquirer remains responsible for the acts of both the PayFac and the sponsored merchants under the PayFac program framework" (JPM PayFac material, https://www.jpmorgan.com/insights/payments/embedded-finance-baas/payfac-101); the payfac in turn indemnifies the acquirer and manages sub-merchant risk day to day.
- **Embedded Payments**: JPM performs "comprehensive identity verification and due diligence processes" on onboarded clients, shifting some compliance burden to the bank (https://developer.payments.jpmorgan.com/docs/embedded-finance-solutions/embedded-payments).
- **Eventbrite reality**: as EPP MoR it already owns chargeback/refund liability regardless of acquirer (10-K: $10.5M reserve, $48.0M LOC). Adding JPM changes who processes and settles, not who is liable to the ticket buyer.

## pricing

## Pricing

- **Published (SMB only, Chase Payment Solutions)**: 2.6% + 10c card-present; 3.5% + 10c keyed; 2.9% + 25c e-commerce; no monthly fee on basic plans; "businesses that process a large volume of transactions may be eligible for custom pricing" (https://www.chase.com/business/payments, https://www.chase.com/business/payments/merchant-fees).
- **Enterprise (Eventbrite-relevant)**: NOT PUBLISHED. Interchange-plus pricing negotiated per merchant is the industry norm at this scale; JPM publishes an interchange education guide, "A Merchant's Guide to Card Acceptance Fees" (https://www.jpmorgan.com/content/dam/jpm/merchant-services/documents/jpmorgan-interchange-guide.pdf) and a payment optimization page on balancing cost and auth rates (https://www.jpmorgan.com/payments/payment-optimization), but no rate card.
- **Push to Card / RTP / FedNow pricing**: NOT PUBLISHED; treasury-negotiated.

## lock_in

## Portability and lock-in

- **Card tokens**: JPM offers tokenization and network tokens within its stack; there is no public JPM commitment to bulk token export equivalent to Stripe's data-portability policy. NOT VERIFIED either way; treat as negotiable. Orchestrator-side vaulting is the standard mitigation: Spreedly explicitly markets vaulting and transacting against Orbital (Chase Paymentech) precisely so credentials are not captive to the gateway (https://www.spreedly.com/gateways/orbital-chase-paymentech).
- **No connected-account construct in direct acquiring**: if Eventbrite adds JPM purely as a US acquirer, there is nothing analogous to Stripe Connect connected accounts to migrate; creator KYC and payout relationships stay wherever they are today (Stripe Connect in US/CA/UK/AU). That makes a JPM acquiring leg LOW lock-in relative to replacing Connect.
- **KYC data**: merchant-level KYC sits with JPM per its CIP process (https://developer.payments.jpmorgan.com/docs/commerce/optimization-protection/capabilities/digital-onboarding); sub-merchant KYC portability from Stripe Connect to any new provider is governed by Stripe, not JPM.
- **Settlement banking**: the deeper the treasury integration (JPM DDA, RTP/FedNow, Push to Card, Embedded Payments accounts), the stickier the relationship; that is JPM's explicit "one path" strategy (https://www.jpmorgan.com/payments/solutions/payment-facilitation).

## limitations

## Limitations and criticisms

- **WePay track record with platforms**: JPM "abruptly dumps business customers" (early 2024) when it wound down WePay ISV relationships (https://www.theinformation.com/articles/jpmorgans-wepay-abruptly-dumps-business-customers); JPM's own note confirms it "ended certain agreements" (https://www.jpmorgan.com/insights/payments/merchant-services/wepay-integration). A platform buyer can fairly ask about JPM's commitment volatility in platform/marketplace segments.
- **Legacy vs modern rail confusion**: many third-party "Chase" connectors are the legacy Orbital gateway, now closed to new onboarding at several partners (https://www.chargebee.com/docs/payments/2.0/payment-gateways-and-configuration/orbital, https://developers.paymentsos.com/docs/connect/partner-providers/chase-paymentech.html). The modern Online Payments API is a different integration.
- **US/Europe-centric acquiring**: JPM's headline claims are US and European (https://www.jpmorgan.com/payments/solutions/commerce); it is not the answer for Eventbrite's LatAm card-only markets (Mexico/Argentina run on Mercado Pago today).
- **Enterprise-only, no published enterprise pricing, bank-grade sales cycle**: contract, underwriting, and collateral negotiation; no self-serve. Industry-standard knowledge.
- **No Stripe-Connect-equivalent marketplace product in the acquiring stack**: marketplace money movement is served by separate treasury products (Embedded Payments, Concourse), meaning multi-product integration rather than one Connect-style API (https://developer.payments.jpmorgan.com/docs/embedded-finance-solutions/embedded-payments, https://developer.payments.jpmorgan.com/blog/product/powering-marketplaces-embedded-finance-solutions).
- **Push to Card geographic limits**: US + Canada only, with Canadian caveats (https://developer.payments.jpmorgan.com/docs/treasury/global-payments/capabilities/global-payments/push-to-card).

## eventbrite_mapping

## Mapping JPM to Eventbrite EPP

- **Why Paul named JPM**: Eventbrite is ~72% US revenue and is MoR under EPP. JPM is the #1 US merchant acquirer (https://media.chase.com/news/jpmorgan-named-number-one-merchant-acquirer-in-the-us). The rational play is adding JPM as a **US direct-acquiring leg** for cost and auth-rate leverage against Stripe/Braintree, not replacing the marketplace layer.
- **Economics of the US leg**: enterprise IC+ pricing (custom, not published), interchange optimization (https://www.jpmorgan.com/content/dam/jpm/merchant-services/documents/jpmorgan-interchange-guide.pdf), and documented **debit routing control**: the Online Payments API exposes `merchantPreferredRouting` including PINless debit so the merchant directs debit transactions to lower-cost networks (https://developer.payments.jpmorgan.com/docs/commerce/online-payments/capabilities/online-payments/payment-methods/cards/routing). Durbin-regulated debit routing is material for a high-volume US ticket seller. Settlement into a JPM account tightens the cash cycle that funds the $278.2M creator payable.
- **No-FX rule**: unaffected. A US leg settles USD collected in USD, consistent with Eventbrite's "paid out in the currency in which they are collected" policy.
- **Payouts**: JPM does not touch Stripe Connect. Creator payouts in US/CA/UK/AU ride Stripe connected accounts today; a JPM acquiring leg decouples pay-in from payout, so Eventbrite must fund Stripe-side (or bank-rail) payouts from JPM settlements. That is ledger and treasury work Eventbrite would own. Longer term, JPM RTP/FedNow/Push to Card could power US instant payouts (Eventbrite currently charges 3%, min $2.99, max $40, US-only) at bank economics (https://developer.payments.jpmorgan.com/docs/treasury/global-payments/capabilities/global-payments/push-to-card, https://www.jpmorgan.com/payments/solutions/fednow).
- **Reserves/risk**: JPM will underwrite Eventbrite as a future-delivery MoR; expect reserve/collateral discussion mirroring the $48.0M LOC and $10.5M reserve Eventbrite already carries. Contract-level, NOT VERIFIED publicly.
- **What JPM requires**: full enterprise onboarding/KYC of Eventbrite as the merchant client (https://developer.payments.jpmorgan.com/docs/commerce/optimization-protection/capabilities/digital-onboarding), an integration to the Online Payments API (direct or via an orchestrator), and a settlement bank account.
- **Post-acquisition reality**: Bending Spoons runs a small generalist team with no payments org being hired; a direct JPM integration plus in-house failover maintenance is exactly the workload they lack staff for, which is why the orchestrator is expected to bring the JPM connector and the routing logic.

## orchestration_reality

## Orchestration reality check (honest version)

**How orchestrators actually integrate JPM**: gateway-to-acquirer card processing, not the full JPM stack. Verified examples: Spreedly vaults and transacts against Orbital (Chase Paymentech) (https://www.spreedly.com/gateways/orbital-chase-paymentech, https://docs.spreedly.com/payment-gateways/orbital/); Gr4vy offers a Chase Orbital card connection (https://docs.gr4vy.com/connections/payments/chaseorbital-card); Primer is an official JPM partner whose integration lets "clients connect directly to J.P. Morgan to facilitate Merchant Services card-not-present transactions" (https://partners.jpmorgan.com/Primer.html); IXOPAY is an official partner processing "online credit card transactions, including recurring payments" via JPM (https://partners.jpmorgan.com/ixopay.html); ACI is listed in JPM's partner network as an orchestration platform (https://partners.jpmorgan.com/e-commerce/). Caveat: several third-party Chase connectors are the deprecated Orbital gateway, closed to new onboarding (https://www.chargebee.com/docs/payments/2.0/payment-gateways-and-configuration/orbital); the credible 2026 answer is a connector to the modern Online Payments API.

**Yuno's own JPM connector: NOT VERIFIED from public sources.** Yuno does not appear on the JPM partner network pages checked (https://partners.jpmorgan.com/e-commerce/), and JPM/Chase was not visible on y.uno/integrations at check time (https://y.uno/integrations). German must confirm with Solutions BEFORE the call whether Yuno has a production J.P. Morgan Online Payments API (or Orbital) connector, in which mode (card-not-present US), and with which reference merchants. Do not claim it cold; Paul explicitly asked for "specific examples".

**What an orchestrator CAN credibly do with JPM**:
- Route US card auths to JPM as an acquiring leg alongside Stripe/Braintree/Adyen, with retries and failover replacing Eventbrite's home-built failover.
- Vault cards orchestrator-side and use network tokens so credentials are portable across JPM/Stripe/Adyen (the Spreedly-style value proposition, https://www.spreedly.com/gateways/orbital-chase-paymentech).
- Pass through JPM-specific fields such as `merchantPreferredRouting` for PINless debit; but the debit-routing savings are JPM capabilities, the orchestrator only exposes them (https://developer.payments.jpmorgan.com/docs/commerce/online-payments/capabilities/online-payments/payment-methods/cards/routing).
- A/B auth-rate and cost testing across processors on the US leg.

**What is NOT orchestrable**:
- Eventbrite's proprietary creator ledger, advance payouts, reserves, and offset rights: those live in Eventbrite's own systems.
- Stripe Connect connected accounts and organizer KYC: they belong to Stripe's ecosystem; no orchestrator moves them.
- JPM merchant underwriting, reserve terms, settlement banking, and treasury products (Embedded Payments, Concourse, Push to Card, RTP/FedNow): direct bank relationships Eventbrite must contract itself.
- Payout execution to creators: an orchestrator can trigger payout APIs at best; the money movement and compliance sit with the bank or Stripe.

**Honest pitch line**: Yuno can be the routing, tokenization, retry, and reconciliation layer that lets a two-person payments team run a four-processor stack (Stripe, Braintree, Adyen, JPM) and add a JPM US acquiring leg without engineering a fourth direct integration; Yuno cannot and should not claim to replace Stripe Connect payouts, Eventbrite's ledger, or the JPM banking relationship.

## key_facts

- J.P. Morgan was the largest acquirer of card payments from US merchants in 2024 with 40.98B transactions, ahead of Fiserv (40.72B) and Worldpay (34.15B) per Nilson (https://www.globenewswire.com/news-release/2025/04/10/3059175/0/en/top-acquirers-of-card-payments-at-us-merchants.html)
- JPM claims #1 US merchant acquirer and #1 European e-commerce acquirer for 10 years running, processing over $10T in payments daily firmwide (https://www.jpmorgan.com/payments/solutions/commerce)
- There is no product called 'JPM for Platforms'; the 2026 stack is the Online Payments API (Direct API, Checkout, drop-in UIs, payment links) under Commerce Solutions (https://developer.payments.jpmorgan.com/docs/commerce/online-payments)
- The legacy Chase Paymentech Orbital gateway is deprecated for new onboarding at multiple partners; Chargebee: 'Orbital is now deprecated... new onboarding is no longer available' (https://www.chargebee.com/docs/payments/2.0/payment-gateways-and-configuration/orbital)
- JPM's Online Payments API exposes merchantPreferredRouting including PINless debit, letting merchants direct US debit to lower-cost networks (https://developer.payments.jpmorgan.com/docs/commerce/online-payments/capabilities/online-payments/payment-methods/cards/routing)
- JPM Push to Card delivers funds to Visa or Mastercard debit/prepaid in about 30 seconds with a 30-minute network SLA, up to $125,000 per transaction, US and Canada, with marketplace payouts as a named use case (https://developer.payments.jpmorgan.com/docs/treasury/global-payments/capabilities/global-payments/push-to-card)
- Chase participates in both RTP and FedNow, and one API integration reaches both US instant rails (https://www.jpmorgan.com/payments/solutions/fednow)
- JPM Embedded Payments gives platforms a single API for client onboarding with JPM-run verification, virtual accounts per counterparty, and payouts at scale (https://developer.payments.jpmorgan.com/docs/embedded-finance-solutions/embedded-payments)
- JPM's marketplace embedded-finance blog (Oct 16, 2025) names Concourse as its hosted solution for managing third-party supplier bank details and payouts (https://developer.payments.jpmorgan.com/blog/product/powering-marketplaces-embedded-finance-solutions)
- WePay (acquired Dec 2017) was absorbed into J.P. Morgan Payments; JPM 'ended certain agreements' with ISVs, and The Information reported WePay abruptly dumped business customers in early 2024 (https://www.jpmorgan.com/insights/payments/merchant-services/wepay-integration, https://www.theinformation.com/articles/jpmorgans-wepay-abruptly-dumps-business-customers)
- WePay's progressive underwriting survives inside JPM: re-underwriting relationship risk with each incremental transaction in real time (https://www.jpmorgan.com/insights/payments/merchant-services/wepay-integration)
- JPM digital onboarding requires full merchant KYC (CIP) before processing and settlement: 'your client must be fully onboarded' (https://developer.payments.jpmorgan.com/docs/commerce/optimization-protection/capabilities/digital-onboarding)
- Published pricing exists only for SMB Chase Payment Solutions (2.6% + 10c in person, 2.9% + 25c e-commerce, 3.5% + 10c keyed); enterprise acquiring is custom IC+ with no public rate card (https://www.chase.com/business/payments/merchant-fees)
- Primer and IXOPAY are officially listed J.P. Morgan Payments partners for card processing via JPM; ACI is listed as an orchestration partner (https://partners.jpmorgan.com/Primer.html, https://partners.jpmorgan.com/ixopay.html, https://partners.jpmorgan.com/e-commerce/)
- Spreedly and Gr4vy publicly offer Chase Orbital connectors, the historical way orchestrators reached Chase acquiring (https://www.spreedly.com/gateways/orbital-chase-paymentech, https://docs.gr4vy.com/connections/payments/chaseorbital-card)
- Yuno is NOT visible in JPM's public partner catalog and JPM/Chase was not visible on y.uno/integrations at check time; Yuno's JPM connector status must be confirmed internally before the call (https://partners.jpmorgan.com/e-commerce/, https://y.uno/integrations)
- JPM's payfac framework keeps the acquirer responsible for the acts of both the payfac and sponsored merchants (https://www.jpmorgan.com/insights/payments/embedded-finance-baas/payfac-101)
- JPM sells acquiring plus settlement banking as one stack: 'The path to pay-in, pay-out and banking is one path, not three or four' (https://www.jpmorgan.com/payments/solutions/payment-facilitation)

## sources

- https://www.jpmorgan.com/payments/solutions/commerce
- https://developer.payments.jpmorgan.com/docs/commerce/online-payments
- https://developer.payments.jpmorgan.com/docs/commerce/online-payments/capabilities/online-payments/payment-methods/cards/routing
- https://developer.payments.jpmorgan.com/docs/commerce/optimization-protection/capabilities/digital-onboarding
- https://developer.payments.jpmorgan.com/docs/embedded-finance-solutions/embedded-payments
- https://developer.payments.jpmorgan.com/blog/product/powering-marketplaces-embedded-finance-solutions
- https://developer.payments.jpmorgan.com/docs/treasury/global-payments/capabilities/global-payments/push-to-card
- https://www.jpmorgan.com/payments/solutions/payment-facilitation
- https://www.jpmorgan.com/insights/payments/embedded-finance-baas/payfac-101
- https://www.jpmorgan.com/insights/payments/embedded-finance-baas/pathtopayfac
- https://www.jpmorgan.com/insights/payments/merchant-services/wepay-integration
- https://www.theinformation.com/articles/jpmorgans-wepay-abruptly-dumps-business-customers
- https://www.jpmorgan.com/payments/solutions/fednow
- https://www.jpmorgan.com/insights/payments/real-time-payments/instant-payments-understanding-rtp-and-fednow-service
- https://www.pymnts.com/real-time-payments/2024/jpmorgan-offers-faster-domestic-payments-via-visa-direct/
- https://www.jpmorgan.com/content/dam/jpm/merchant-services/documents/jpmorgan-interchange-guide.pdf
- https://www.jpmorgan.com/payments/payment-optimization
- https://www.chase.com/business/payments
- https://www.chase.com/business/payments/merchant-fees
- https://media.chase.com/news/jpmorgan-named-number-one-merchant-acquirer-in-the-us
- https://www.globenewswire.com/news-release/2025/04/10/3059175/0/en/top-acquirers-of-card-payments-at-us-merchants.html
- https://partners.jpmorgan.com/
- https://partners.jpmorgan.com/e-commerce/
- https://partners.jpmorgan.com/Primer.html
- https://partners.jpmorgan.com/ixopay.html
- https://www.spreedly.com/gateways/orbital-chase-paymentech
- https://docs.spreedly.com/payment-gateways/orbital/
- https://docs.gr4vy.com/connections/payments/chaseorbital-card
- https://developers.paymentsos.com/docs/connect/partner-providers/chase-paymentech.html
- https://www.chargebee.com/docs/payments/2.0/payment-gateways-and-configuration/orbital
- https://www.fintechwrapup.com/p/deep-dive-jpmorgans-payments-strategy
- https://y.uno/integrations
- https://www.jpmorgan.com/payments/solutions/commerce/optimization-protection
- https://secure.paymentech.com/mcp/protected/documents/product_sheets/orbital_gateway.pdf
---

# COMPETITOR SCAN: THE OTHER ORCHESTRATORS IN THE BAKE-OFF

## Bake-off competitor scan (as of 2026-08-04)

**BR-DGE (Edinburgh):** Positions as vendor-agnostic orchestration with "routing-as-a-service"; claims 40+ partners and ~400 ongoing connections to PSPs, acquirers, gateways and value-added services (https://br-dge.to/connections/), but its public connections page does NOT name Stripe, Braintree, Adyen or J.P. Morgan individually; third-party coverage says its site claims 100+ PSPs including Worldpay, Adyen, Stripe and NMI (https://businessofpayments.com/tag/br-dge/). Braintree and J.P. Morgan/Chase support: NOT VERIFIED. No public marketplace/split-payment/sub-merchant product found: NOT VERIFIED. Ticketing proof point is real: 2025 press release, 3-year deal to power Resident Advisor's ticketing platform with multi-acquiring, dynamic routing, wallet optimization, then LPMs as RA expands into LatAm/APAC, explicitly including "payments to local stakeholders, including venues, DJs, and security providers" (https://br-dge.to/press/br-dge-to-power-payments-for-resident-advisors-enhanced-ticketing-platform/, https://ffnews.com/newsarticle/paytech/br-dge-to-power-payments-for-resident-advisors-enhanced-ticketing-platform/).

**ProcessOut (Checkout.com):** Now Checkout.com's orchestration product ("Payment Services") after the acquisition (https://www.processout.com/blog/a-new-chapter-for-processout-as-part-of-checkoutcom); public claims center on AI Smart Routing across providers, failover/retry, Telescope monitoring, and a PCI vault (https://www.processout.com/). No public marketplace/split-payment/sub-merchant or payout product claims found: NOT VERIFIED. Specific connector list for Stripe, Braintree, Adyen, JPM Chase is not publicly enumerated: NOT VERIFIED. Fever deployment: no public case study naming Fever with ProcessOut/Checkout.com was found; Fever publicly describes only an IN-HOUSE routing system that "automatically selects the best payment processor" (https://business.feverup.com/ticketing-revenue-optimization/). ProcessOut-Fever deal: NOT VERIFIED publicly.

**Primer:** Claims 100+ payment methods and 45+ processor integrations via its "Primer Connect" unified-API framework; Stripe, Braintree and Adyen are publicly listed connections (https://primer.io/docs/payments/connect-a-processor, https://sacra.com/c/primer/). J.P. Morgan Payments is a formal Primer partner integration, launched 2025 with GetYourGuide as first adopter (https://partners.jpmorgan.com/Primer.html). So Primer publicly covers all four requested processors. No dedicated marketplace/split-payment/sub-merchant/payout product publicly claimed (it is checkout + orchestration + workflows): NOT VERIFIED for marketplace features.

**Spreedly:** Open orchestration with a vault and hundreds of gateway connections; its supported-gateways docs list Stripe (incl. Payment Intents), Braintree, Adyen, and "Orbital (Chase Paymentech)", covering all four (https://developer.spreedly.com/docs/supported-gateways, https://www.spreedly.com/gateways/stripe, https://www.spreedly.com/gateways/adyen). Marketplace support is thin: docs show payouts only as pass-through gateway transactions (e.g. Adyen General Credit with payout=true) rather than a native split-payment/sub-merchant product (https://docs.spreedly.com/payment-gateways/adyen/). Native marketplace/split features: NOT VERIFIED.

**Gr4vy:** Cloud-native orchestration claiming 400+ PSP/method/fraud connections through one integration; public connections directory lists Adyen, Braintree, Chase, Cybersource, PayPal and Stripe, covering all four requested processors (https://gr4vy.com/connections/, https://docs.gr4vy.com/connections/payments/overview). Publicly touts being ChaseNet Certified for on-us routing with J.P. Morgan Chase merchants (https://gr4vy.com/posts/product-updates-q2-2026-new-payment-orchestration-features-connectors-and-enhancements-from-gr4vy/). No native marketplace/split-payment/sub-merchant or payout product publicly claimed: NOT VERIFIED.

**Payrails (Berlin):** Enterprise "payment OS" with ~72 public integrations; Stripe, Braintree, PayPal and Adyen all listed live, while J.P. Morgan is listed as "Soon" (i.e., not yet live) on its integrations page (https://www.payrails.com/integrations). It is the only one of the six with an explicit standalone Payouts product ("global payout infrastructure", plus Thunes for cross-border payouts) and it surfaces marketplace flows via MangoPay ("purpose-built for marketplaces", multi-party fund flows/escrow) rather than a native split-payments engine (https://www.payrails.com/integrations). Native split-payment/sub-merchant product: NOT VERIFIED.

**Cross-cutting notes for the call:** Only Primer, Spreedly and Gr4vy publicly cover all four processors Paul named today; Payrails covers three with JPM pending; BR-DGE and ProcessOut do not publicly enumerate them. None of the six publicly claims a native marketplace split/sub-merchant engine; all rely on the underlying processors' platform products (Stripe Connect, Adyen for Platforms, Braintree Marketplace) or partners (MangoPay). The two ticketing references: BR-DGE x Resident Advisor is press-verified; ProcessOut x Fever is NOT VERIFIED in any public source.