# SDR Research Brief — Ford / Ford Credit
*Yuno Payment Orchestrator · Framework v8.0 · Researched 2026-07-21*
*All findings from public web data. Every claim carries a source URL. Where uncertain, disclaimers applied.*

---

## EXECUTIVE SUMMARY

Ford Motor Credit Company LLC (**Ford Credit**), the captive finance arm of Ford Motor Company ($185B FY2024 revenue), is a multi-brand lender (Ford Credit, Lincoln Automotive Financial Services, Ford Pro FinSimple) with **$143.6B in net receivables** and its own SEC 10-K. Ford runs a confirmed **5-year premier-PSP agreement with Stripe** (signed Jan 2022, North America + Europe, renewal window ~2026–2027) spanning Ford Credit digital payments, dealer payouts via Stripe Connect, vehicle ordering, EV charging and Ford Pro commercial billing — with **no orchestration layer** and a notably **card-hostile collections flow** (loan payments run on ACH/bank debit; cards are steered to third-party billers MoneyGram/Western Union). The standout Yuno opportunity is orchestrating on top of that single-PSP stack across a multi-entity European footprint (FCE Bank plc UK, Ford Bank GmbH DE), expanding tender options to reduce delinquency friction, and fixing documented portal/decline failures — right as CEO Cathy O'Callaghan drives a public "fintech" transformation and Ford layers in Bread Financial embedded lending.

---

## SECTION 1 — Traffic by Country

**ford.com** — ~19.7M visits/mo (3-mo avg), global rank #1,828, +0.47% MoM. [S1]

| Rank | Country | Traffic Share (%) | Trend | Source URL |
|------|---------|-------------------|-------|------------|
| 1 | United States | 78.12% | ↑ | [S1] |
| 2 | India | 2.59% | ↑16.8% | [S1] |
| 3 | Mexico | 2.48% | ↑17.8% | [S1] |
| 4 | Canada | 2.30% | ↑ | [S1] |
| 5 | United Kingdom | 1.98% | ↑16.2% | [S1] |

**credit.ford.com** — ~809.5K visits/mo, US ~100%, bounce 31%, 3.74 pages/visit, 3m28s avg (strong bill-pay servicing engagement). [S2]

**Key payment subdomains:** `pay.ford.com` (Guest Pay, no login), `accountmanager.ford.com` (logged-in payments/autopay), `credit.ford.com` (apply/pay hub). Regional: ford.co.uk, ford.de, ford.com.br, ford.com.mx, ford.com.au, ford.ca (per-domain visits Not found this pass).

**Flags:** US-dominant, but LATAM (Mexico) + APAC (India, plus China per Ford Credit's own disclosure) + European lending footprint = multi-entity, multi-currency relevance on the financing side.

---

## SECTION 2 — Legal Entities

Source: Ford Motor Credit Company LLC 10-K (SEC EDGAR CIK 38009, filed 06-Feb-2025). [S3]

| Country | In Top Traffic? | Local Ford Credit Entity? | Cross-Border Risk? | Source URL |
|---------|-----------------|---------------------------|--------------------|------------|
| United States | ✅ | ✅ Ford Motor Credit Company LLC (+ Lincoln Auto Financial, Ford Pro FinSimple) | No | [S3] |
| Canada | ✅ | ✅ Ford Credit Canada | No | [S3] |
| United Kingdom | ✅ | ✅ FCE Bank plc (PRA-authorised, FCA+PRA regulated) | No | [S3] |
| Germany | — | ✅ Ford Bank GmbH | No | [S3] |
| Brazil / other EU | — | Served via FCE / regional entities (names Not found this pass) | varies | [S3] |

**Structure:** Ford Motor Company (CIK 37996) parent; Ford Motor Credit files its own 10-K. US & Canada = **83% of net receivables** (US = 89% of that). Securitization vehicles (e.g., Ford Credit Auto Receivables Two LLC) in EDGAR. [S3]
> ⚠️ MANUAL: Verify per-country financing entity on regional T&Cs.

---

## SECTION 3 — Payment Stack

### 3A. PSPs & Acquirers / Billers

| Country/Region | PSP / Biller | Evidence Type | Source URL |
|----------------|--------------|---------------|------------|
| **NA + Europe (premier PSP)** | **Stripe** — 5-yr agreement (Jan 2022): Ford Credit digital payments, dealer payouts via **Stripe Connect**, vehicle ordering/reservations, EV charging, **Ford Pro FinSimple** commercial billing | [Press Release] | [S4][S5] |
| Ford Credit **Guest Pay** (pay.ford.com) | Bank-connect flow routes through **Stripe** (must accept Stripe Terms/Privacy) | [Checkout] | [S6] |
| Ford Credit loan payments (card/wire) | **MoneyGram** and **Western Union** (third-party billers; cards NOT accepted directly) | [Checkout] | [S7] |
| Embedded lending (Mar 2026) | **Bread Financial** — co-brand Ford Rewards Visa + installment-loan program (0% for qualified), for parts/service/accessories/subscriptions | [Press Release] | [S8] |
| UK retail shop (shop.ford.co.uk) | PayPal, Apple Pay, Google Pay, Klarna, cards (PSP not named on page) | [Checkout] | [S9] |

### 3B. Orchestrator

**No public evidence found** (Spreedly, Primer, Gr4vy, CellPoint, APEXX, IXOPAY). Ford relies on Stripe's native capabilities across surfaces. The card/ACH processor behind accountmanager.ford.com is **not publicly disclosed** (likely Stripe under the 2022 deal — [INFERENCE — not confirmed]).

> **The pattern:** one premier PSP (Stripe) across NA+Europe, a card-hostile collections rail (ACH-only + MoneyGram/WU), a new embedded-lending layer (Bread), plus region-siloed retail (UK: Klarna/wallets) — no unifying orchestration or routing.
> ⚠️ MANUAL — DevTools at authenticated checkout: 4111 1111 1111 1111 | 02/30 | 123

---

## SECTION 4 — APMs (Live Verification)

### 4A. Confirmed APMs

| Market | APMs Confirmed | Verification Source | Source URL |
|--------|---------------|--------------------|------------|
| Ford Credit US (loan/lease) | Bank account / ACH (Account Manager, mobile app, Guest Pay checking-only); mail check; payroll deduction; card/wire only via MoneyGram or Western Union | Official ways-to-pay + FAQ (search-snippet; page timed out) | [S7] |
| Ford Credit Guest Pay | Checking accounts only (no savings, no cards) | Guest Pay FAQ | [S6] |
| UK retail shop (shop.ford.co.uk) | Mastercard, Visa, PayPal, Apple Pay, Google Pay, Klarna (Pay Later in 3) | Live fetch (full content) | [S9] |
| FordPass Charging (BlueOval) | Associated credit card, Plug-and-Charge auto-bill | Ford support | [S10] |

### 4B. Unverified Markets

| Market | Verification Attempted? | Reason Not Verified | Popular Local APMs (context) |
|--------|-------------------------|---------------------|------------------------------|
| shop.ford.com (US official) | ✅ | Timed out | — |
| ford.de / ford.com.br / ford.com.mx / ford.com.au | ✅ | Not fetched (budget) | DE: SEPA/giropay; BR: Pix/boleto; MX: OXXO/SPEI |
| FordPass app wallet / BlueCruise subscription pay | ✅ | Not fetched | — |

> "Not verified" ≠ "not available." **MANUAL: VPN checkout walk-through before any APM claim.** The card-hostile loan-payment flow (ACH-only, cards via MoneyGram/WU) IS confirmed via official pages [S6][S7] and is fair to reference; do not extend it to other surfaces.

---

## SECTION 5 — Payment Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|------------|----------|-----------|------------|------------|
| Portal login blocked ("400 Bad Request – Header/Cookie Too Large") after MFA | Mach-E forum | Cluster | early 2024 | [S11] |
| Online payment declines with no explanation; workaround = have your bank push the payment | Mach-E forum | Recurring | early 2024 | [S12] |
| Autopay breaks after bank switch (in-app update link broken; rep can't take payment) | PissedConsumer (1.7★, 286 reviews) | Recurring | rolling | [S13] |
| Auth/MFA loop ("never receive a code"); IVR can't process "I want to pay my bill" | PissedConsumer | Recurring | rolling | [S13] |
| Payment-arrangement failure → 30-day delinquency + ~100-pt credit drop despite perfect history | PissedConsumer | Recurring | rolling | [S13] |
| BlueOval charging Plug-and-Charge billing-sync failures (fix = cancel/reactivate subscription) | F150 Lightning forum | Recurring | 2022–2025 | [S14] |

**Analysis → Yuno:** The cluster is **collections-side friction** (declines with no diagnostics, broken autopay updates, MFA/portal failures, posting delays that trigger delinquency) plus **subscription/charging billing sync**. Every one of those is a missed or late payment for a lender. This maps to Yuno **smart retries + real-time decline monitors + network tokenization + Account Updater + wider tender options** (Rappi: ms detection vs 5–10 min manual; Livelo: 50% recovery). For a captive lender, easier and more reliable payment = lower delinquency, not just better UX.

---

## SECTION 6 — Expansion & Corporate Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | Jan 17 2022 | **Stripe** 5-yr premier-PSP agreement (NA + Europe) | PSP | [S4] |
| 2 | Dec 2023 → Mar 2024 | **Cathy O'Callaghan** becomes President & CEO Ford Credit (succeeds Marion Harris) | Leadership | [S15] |
| 3 | 2025 | O'Callaghan priorities: **technology, affordability, profitable growth**; "fintech" transformation | Strategy | [S15] |
| 4 | Feb 2025 | **Sherry House** appointed Ford CFO (ex-Lucid CFO, ex-Waymo/Alphabet finance) | Leadership | [S16] |
| 5 | Oct 2024 | BlueCruise repricing: $495/yr, $49.99/mo, or $2,495 one-time | Subscription | [S17] |
| 6 | Mar 10 2026 | **Bread Financial** co-brand Visa + installment-loan program (embedded 0% financing) | Fintech / BNPL | [S8] |

---

## SECTION 7 — Payment News

| # | Date | Headline | Relevance | Source URL |
|---|------|----------|-----------|------------|
| 1 | Mar 2026 | 🟢 Ford + Bread Financial co-brand card + installment loans | New embedded pay-over-time across service/accessories/subs | [S8] |
| 2 | Jan 2022 | 🟢 Ford + Stripe 5-yr deal (renewal window ~2026–2027) | Incumbent PSP behind Ford Credit/dealer/charging/Ford Pro | [S4] |
| 3 | — | 🔴 PSP removals | None found | — |

---

## SECTION 8 — Checkout Audit

| Dimension | Finding | Quality | Notes |
|-----------|---------|---------|-------|
| Checkout type | Multi-surface: Ford Credit collections (ACH), UK retail (wallets/Klarna), charging, subscriptions, Bread lending | 🟡 | Siloed, no unifying processor |
| Guest checkout | Guest Pay: pay w/o login via acct # + last-4 SSN; checking-only, no cards | 🟡 | Narrow tender [S6] |
| Steps to purchase | Guest Pay same-day if before 9pm ET | 🟢 | [S6] |
| 3DS | Not verified | — | — |
| Mobile experience | Ford Credit Mobile App primary; autopay update link reported broken | 🔴 | Complaint driver [S13] |
| APM display logic | UK retail geo APM stack (Klarna/wallets); US loan flow ACH-centric | 🟡 | [S9][S7] |
| BNPL | Klarna on UK shop; Bread installments (Mar 2026) on US service/parts | 🟢 | [S9][S8] |

> ⚠️ MANUAL: Walk Ford Credit make-a-payment (US) + UK shop + a subscription renewal.

---

## SECTION 9 — PCI DSS

| PCI DSS Level | Card data handling | Recommended Yuno integration | Source |
|---------------|-------------------|------------------------------|--------|
| No public PCI page found | Guest Pay retains only last-4 of card for troubleshooting → tokenized/PSP-hosted handling; card rails delegated to Stripe (PCI L1) | Yuno vault + tokenization to widen tender options (cards/wallets/A2A) on the loan bill without adding PCI scope | [S6] |

No standalone Ford/Ford Credit PCI attestation page located. **Not found.**

---

## SECTION 10 — Strategic Insights

**Insight #1: Single premier PSP (Stripe) across NA + Europe, renewal window ~2026–2027**
Evidence: §3A — Stripe 5-yr deal, no orchestrator. Pain: no cross-provider routing/failover, limited local acquiring across FCE Bank (UK) and Ford Bank (DE), fragmented reconciliation, weaker leverage at renewal. Yuno: orchestrate on top of Stripe, add local acquirers where they price/approve better, one reconciled view, +7% approval / 50% recovery. Best Case: Livelo. Angle: "You are heading into a Stripe renewal window with one processor across North America and Europe. An orchestration layer above it gives you failover, local acquiring in your UK and German entities, and negotiating leverage, without ripping anything out."

**Insight #2: Card-hostile collections flow raises delinquency friction**
Evidence: §4 — loan payments are ACH/checking-only; cards steered to MoneyGram/Western Union. §5 — declines, broken autopay, posting delays driving delinquencies. Pain: every payment obstacle is a missed/late payment on a $143.6B book. Yuno: enable more tender types (cards, wallets, A2A) + smart retries + real-time decline monitoring + network tokens/Account Updater, without PCI burden. Best Case: Livelo (50% recovery), Rappi (80% less resolution time). Angle: "Making it easier and more reliable to pay is a delinquency lever, not just a UX one. Widening tender options and adding retry/monitoring to the collections rail keeps more accounts current."

**Insight #3: A fragmenting, multi-surface payments estate under a 'fintech' mandate**
Evidence: §3A/§6 — Stripe + Bread Financial + MoneyGram/WU + UK Klarna/wallets + in-app charging + connected-services subs, no unifying layer, under CEO O'Callaghan's fintech transformation. Pain: each surface is its own integration and data silo. Yuno: single API across every surface and market, new methods/markets in weeks. Best Case: InDrive (10 markets <8 months). Angle: "As Ford Credit remakes itself into a fintech and layers in Bread, one orchestration layer unifies collections, retail, charging and subscriptions across markets instead of stitching each provider by hand."

**Insight #4: Recurring-billing surfaces (BlueCruise, Connectivity, charging) need dunning/retry**
Evidence: §6/§5 — subscriptions ($495/yr, $49.99/mo) + in-app charging with documented billing-sync failures. Pain: involuntary churn and billing confusion on recurring revenue. Yuno: dunning, retries, network tokens, real-time monitors. Angle: coverage + recovery framing, never "you lack X."

---

## SECTION 11 — Pipeline

### 11A. Direct Competitors (captive / auto finance)

| Company | Website | HQ | Est. Size | Overlap | Source |
|---------|---------|----|-----------|---------|--------|
| GM Financial | gmfinancial.com | Fort Worth, TX | GM captive | NA/Global | [S18] |
| Toyota Financial Services | toyotafinancial.com | Frisco, TX | $150B+ managed assets | Global | [S19] |
| American Honda Finance | hondafinancialservices.com | Torrance, CA | Captive | NA | [S20] |
| Ally Financial | ally.com | Detroit, MI | Largest US auto finance (one ranking) | US | [S21] |
| Chrysler Capital / Santander (Stellantis) | santanderconsumerusa.com | — | Major | US | — |
| BMW Financial Services | bmwusa.com/financial-services | — | Captive | Global | — |
| Mercedes-Benz Financial | mbfs.com | — | Captive | Global | — |

### 11B. Industry Peers (PSPs / billers)

| Company | Vertical | Why Similar | Source |
|---------|----------|-------------|--------|
| Stripe | PSP (Ford incumbent) | Powers Ford collections/dealer/charging/Ford Pro | [S4] |
| ACI Payments (ACI Speedpay) | Bill-pay processor | **GM Financial's** loan-payment biller | [S18] |
| Paymentus | Auto & consumer-finance pay platform | Markets captive/indirect lender integrations (OFLL, Megasys) | [S22] |
| Bread Financial | Embedded lending / co-brand | Ford's new BNPL/card partner | [S8] |

### 11C. Adopting Orchestration

No captive auto-finance arm in this set is publicly confirmed on an independent orchestrator. Field runs on single PSPs/billers (Ford→Stripe, GM Financial→ACI). **Greenfield for orchestration in captive auto-finance.** [S4][S18]

### 11D. Scoring (verified only)

| Signal | Pts | Verified? |
|--------|-----|-----------|
| Operates in 3+ countries | +3 | ✅ US, CA, UK (FCE), DE (Ford Bank), China |
| Multiple PSPs | +3 | ✅ Stripe + Bread + MoneyGram/WU + UK stack |
| Recent expansion (24 mo.) | +2 | ✅ Bread Financial, fintech transformation |
| Public payment issues | +2 | ✅ Declines, portal errors, PissedConsumer 1.7★ |
| Funding/revenue >$10M | +2 | ✅ $185B / FMCC $143.6B receivables |
| LATAM/APAC/MENA traffic | +2 | ✅ Mexico, India, China |
| No orchestrator | +2 | ✅ No public evidence |
| Payment job postings | +1 | ❌ Not found |
| Public RFP | +3 | ❌ Not found |

**Score: 16 → 🔴 HIGH PRIORITY**

### Top Pipeline

| Rank | Company | Type | Key Markets | Priority | Top Signal |
|------|---------|------|-------------|----------|-----------|
| 1 | Ford Credit | Direct | US/CA/UK/DE | 🔴 High | Stripe single-PSP + card-hostile collections + fintech mandate |
| 2 | GM Financial | Competitor | NA | 🔴 High | On ACI biller, captive, multi-brand |
| 3 | Ally Financial | Peer | US | 🟡 Med | Largest US auto finance |
| 4 | Toyota Financial | Competitor | Global | 🟡 Med | $150B+ assets, global captive |
| 5 | Stellantis Financial | Competitor | US/EU | 🟡 Med | Multi-brand, Santander-backed |

Pipeline Summary: Strongest vertical = **captive auto-finance lenders** modernizing collections/embedded-payments — an orchestration greenfield. Ford Credit is the sharpest: Stripe renewal window, card-hostile collections, documented failures, and a public fintech mandate.

---

## SECTION 12 — Business Case

| Annual Revenue | Avg Transaction Value | Est. Annual Transactions | Primary Currency | Top 3 Markets |
|----------------|----------------------|--------------------------|------------------|---------------|
| Ford Motor Co: $185B FY2024. Ford Credit: $143.6B net receivables, $1.65B EBT | Auto loan/lease ~$500–750/mo [ESTIMATE, industry]; BlueCruise $495/yr; charging micro | Not disclosed (millions of recurring monthly payments across the receivables book) | USD (multi-currency in Europe) | US, Canada, UK |

> ⚠️ The orchestration TAM is the **payment-processing / collections rail** (huge recurring ACH + card volume across millions of accounts), plus subscriptions, charging and retail — not the receivables balance itself. Ford Credit does not disclose processing volume; do not fabricate a figure.

---

## SECTION 13 — Outreach (verified findings only)

```
--- LINKEDIN MESSAGE ---
Hi [Name],

Been mapping how captive lenders run payments, and Ford Credit stood out. Stripe has carried your digital payments, dealer payouts and Ford Pro billing across North America and Europe since 2022, and Bread just came in on the embedded-financing side. A lot of surfaces, and no single layer routing or reconciling across them.

Two things stood out from the outside. Your loan payments run on ACH and bank debit, with cards pushed out to third-party billers, and owners report payment declines with no diagnostics and broken autopay updates. For a lender, each of those is a missed or late payment, not just a UX issue.

Yuno sits on top of your existing PSPs: smart routing and failover, wider tender options on the bill, and real-time decline monitoring with retries and network tokens. Livelo recovered 50% of otherwise-failed transactions this way, and Rappi cut payment-issue resolution time 80%.

With the Stripe renewal window and Cathy's fintech push, worth 20 minutes to compare notes? Open Tuesday or Thursday.

--- COLD EMAIL ---
Subject: Ford Credit collections — a delinquency lever hiding in payments

Hi [Name],

Ford Credit has run on Stripe across North America and Europe since 2022, with Bread now layered in for embedded financing. Real coverage, and also several payment surfaces with nothing routing, failing over or reconciling across them.

The part that stood out: your loan payments run on ACH and bank debit, cards are routed to MoneyGram and Western Union, and owners publicly report declines with no explanation and autopay that breaks after a bank switch. On a $143.6B book, every one of those is a late or missed payment, so this is a delinquency lever, not just a UX one.

Yuno is one API above your existing processors:
- Smart routing + automatic failover, with local acquiring in your UK and German entities
- Wider tender options on the bill (cards, wallets, A2A) with no added PCI scope
- Real-time decline monitoring, retries, network tokens and Account Updater to keep accounts current

Livelo lifted approval 5% and recovered 50% of failed transactions. Rappi cut resolution time 80%. With your Stripe renewal window and the fintech transformation underway, this is the moment to add the layer.

Worth 20 minutes? I can hold Tuesday or Thursday.

Best,
German
Yuno | Payment Orchestration
```

---

## APPENDIX — Source URLs

```
[S1]  https://www.similarweb.com/website/ford.com/
[S2]  https://www.similarweb.com/website/credit.ford.com/
[S3]  https://www.sec.gov/Archives/edgar/data/38009/000003800925000007/fmcc-20241231.htm
[S4]  https://stripe.com/newsroom/news/stripe-ford-agreement
[S5]  https://www.cnbc.com/2022/01/17/ford-signs-five-year-payments-deal-with-stripe-for-e-commerce-drive.html
[S6]  https://www.ford.com/finance/customer-support/payments/what-is-guest-pay/
[S7]  https://www.ford.com/finance/ways-to-pay/
[S8]  https://newsroom.breadfinancial.com/ford-financing-program
[S9]  https://shop.ford.co.uk/pages/payment-options
[S10] https://www.ford.com/support/how-tos/fordpass/blueoval-charge-network/what-is-the-ford-blueoval-charge-network/
[S11] https://www.macheforum.com/site/threads/ford-credit-users-are-you-able-to-access-your-portal.33767/
[S12] https://www.macheforum.com/site/threads/anyone-else-having-problems-with-ford-credit-and-the-balloon-payment-at-the-end-of-ford-options.33970/
[S13] https://ford-credit.pissedconsumer.com/review.html
[S14] https://www.f150lightningforum.com/forum/threads/plug-and-charge-charge-faults.25005/
[S15] https://www.autofinancenews.net/allposts/technology/ford-credit-ceo-identifies-tech-affordability-as-2025-priorities/
[S16] https://www.tipranks.com/news/company-announcements/ford-appoints-new-cfo-amid-leadership-changes
[S17] https://www.fromtheroad.ford.com/us/en/articles/2024/ford-lowers-bluecruise-annual--monthly-plan-pricing
[S18] https://www.gmfinancial.com/en-us/resources/payment-options.html
[S19] https://pressroom.toyota.com/toyota-financial-services-expands-headquarters/
[S20] https://pitchbook.com/profiles/company/152799-13
[S21] https://www.fi-magazine.com/news/ally-financial-largest-us-auto-finance-company-report-finds
[S22] https://www.paymentus.com/consumer-finance/
```
