# SDR Research Brief — OneTravel (onetravel.com)
*Yuno Payment Orchestrator · Framework v8.0 · 2026-07-27*
*Brand of Fareportal Inc. Companion brief: fareportal-2026-07-23.md (CheapOair + group level, incl. 2026-07-27 stack addendum). This brief is OneTravel specific and supersedes the traffic picture in the older file.*

## EXECUTIVE SUMMARY
OneTravel is Fareportal's second consumer OTA brand (flights across 500+ airlines), legally operated by WK Travel Inc under Fareportal Inc in NYC, with ~8.6M annual visits that are US dominant (61% US, 11% Canada), settling the earlier Semrush claim of an India dominant audience, which does not survive cross-source checks. Its consumer payment stack is CONFIRMED via first-party checkout JavaScript: CyberSource (cards + Google Pay) and Braintree (PayPal + Venmo) running in parallel, CardinalCommerce 3DS, Accertify antifraud, Affirm BNPL for US residents only, all billed in US dollars on one US-style checkout for every market, with no consumer orchestrator. The sharpest verified pain is reconciliation: OneTravel's own FAQ institutionalizes "multiple charges per booking," "duplicate charges," and "charged more than quoted" with a dedicated billing phone line, and the same themes recur on Trustpilot and in 1,421 BBB complaints at group level. Yuno wedge: a consumer-side orchestration layer across CyberSource + Braintree with unified reconciliation and dispute control, cross-border cost relief for the ~39% non-US traffic paying in USD, and local methods for verified growth pockets (Philippines traffic +300%).

---

## SECTION 1 — Traffic by Country
Primary source: SimilarWeb (user-provided panel, Jul 2026). **8.615M annual visits** (~718K/mo).

| Rank | Country | Traffic Share | Est. Monthly Visits | Trend | Source |
|------|---------|--------------|--------------------:|-------|--------|
| 1 | United States | 61.39% | ~441K | ↓ 7.36% | [S1] |
| 2 | Canada | 10.63% | ~76K | ↓ 12.50% | [S1] |
| 3 | India | 1.76% | ~12.6K | ↓ 63.98% | [S1] |
| 4 | United Kingdom | 1.38% | ~9.9K | ↑ 10.69% | [S1] |
| 5 | Philippines | 1.30% | ~9.3K | ↑ 300.54% | [S1] |
| 6 | Australia | 1.11% | ~8.0K | ↓ 53.61% | [S1] |
| 7 | Ghana | 1.03% | ~7.4K | ↓ 68.70% | [S1] |

**Source conflict, resolved for sizing purposes:** Semrush (Jun 2026) shows India 45.79% of 1.48M visits; SimilarWeb (Jun 2026: US 69.7%, 635K visits) and Hypestat (US 65.55%) show US dominant. The ~678K "India block" in Semrush almost exactly equals the gap between the two panel totals. [INFERENCE — not confirmed] Plausible mechanism: Fareportal's own Gurgaon operations center (thousands of agents working US bookings on the platform) shows up as India traffic in Semrush's panel. For consumer demand sizing, use the US-heavy view; both panels agree US + Canada is the revenue geography. [S2][S3][S4]

Flags: >5% markets are US and Canada only. Emerging-market pockets (India, Philippines, Ghana) total ~4% but Philippines is growing +300%. Diaspora VFR profile [INFERENCE]: India, Philippines and Ghana traffic on a US OTA is consistent with US-route international ticket buyers.

---

## SECTION 2 — Legal Entities

| Country | In Top Traffic? | Has Local Entity? | Cross-Border Risk? | Source |
|---------|-----------------|-------------------|--------------------|--------|
| USA | Yes (#1) | Yes. **WK Travel Inc d/b/a OneTravel** (Las Vegas registration, NYC c/o Fareportal, 137 W 25th St), owned and operated by Fareportal Inc | Home market | [S5][S6][S7] |
| Canada | Yes (#2) | Partial. **RSH Travel Inc, Markham ON and Richmond BC**, is the registered seller of travel representing OneTravel.ca (TICO #50018542, BC #53325). Billing still in USD per FAQ | ⚠️ USD billing on US rails despite Canadian registration | [S6][S12] |
| India | Yes (#3) | Ops only. Fare Portal India Pvt Ltd, Gurgaon (CIN U72900DL2005PTC134394, revenue INR 100-500 crore FY2024). No consumer storefront entity | ⚠️ Potential cross-border operation for consumer billing | [S8] |
| UK | Yes (#4) | Not found | ⚠️ Potential cross-border operation, no local entity found | [S6] |
| Philippines / Australia / Ghana | Yes (#5-7) | Not found | ⚠️ Potential cross-border operation, no local entity found | [S6] |

US seller-of-travel registrations: CA CST #2090295-40, NV SOT #2007-0081, IA #883, WA #602785938, FL #ST38063. US DOT consent order EO-2014-1-1 is titled "WK Travel d/b/a OneTravel." [S6][S9]
> ⚠️ MANUAL: verify billing entity per storefront T&Cs before contract-stage claims.

---

## SECTION 3 — Payment Stack

**3A. PSPs & Acquirers (CONFIRMED via first-party checkout JS, Wayback captures; same Fareportal platform as CheapOair)**

| Country/Region | PSP / Acquirer | Evidence Type | Source |
|----------------|----------------|---------------|--------|
| All markets (one checkout) | **CyberSource (Visa)** — cards + Google Pay | [Source Code] first-party checkout JS | [S10] |
| All markets | **Braintree (PayPal)** — PayPal + Venmo (MerchantAccountId `fareportal`) | [Source Code] | [S10] |
| All markets | **CardinalCommerce (Visa)** — 3DS | [Source Code] | [S10] |
| All markets | **Accertify (Amex)** — antifraud; plus Fraud.net (2019 case study) and in-house Gurgaon review team | [Source Code] + [Press Release] | [S10][S11] |
| US | **Affirm** (direct integration, `cdn1.affirm.com/js/v2/affirm.js`; loans by Cross River Bank) | [Source Code] | [S13] |
| US | **Synchrony Bank** — co-branded OneTravel/CheapOair credit cards | [Press Release] | [S14] |
| Supplier side (group) | Amadeus Outpayce B2B Wallet (virtual cards, Jan 2026) | [Press Release] | [S15] |

Ruled out by code inspection: Stripe, Adyen, Worldpay, Chase, Vantiv/FIS, First Data, Elavon; Riskified, Signifyd, Forter, Sift, Kount. Acquirer behind CyberSource not exposed client-side. No 2025-2026 news of any consumer PSP change. [S10][S16]

**3B. Orchestrator:** **No consumer-side orchestrator found** (no Spreedly/Primer/Gr4vy/CellPoint/APEXX in code or news). Architecture is two parallel PSPs with no routing layer. Note: Fareportal orchestrates its supplier side (Outpayce) and markets "payment orchestration" in its B2B Enterprise Solutions product, so the org speaks the language. [S10][S15][S17]
> ⚠️ MANUAL — DevTools on live checkout (real browser bypasses Akamai 403): test card 4111 1111 1111 1111 | 02/30 | 123.

---

## SECTION 4 — APMs (Agent D verification)

**4A. Confirmed APMs**

| Market | APMs Confirmed | Verification Source | Source |
|--------|----------------|--------------------|--------|
| US | Cards (Visa incl. debit, MC, Amex, Discover, Diners), PayPal, Venmo, Apple Pay, Google Pay, Affirm (3/6/12 mo, 10-30% APR, US residents 18+ only) | First-party checkout JS + BNPL page + help center card list | [S10][S13][S18] |
| All markets | Same single checkout; "All payments must be in US Dollars" (FAQ) | Help center + FAQ snapshots | [S18][S19] |
| India | Same US-style card checkout, INR display currency only | First-party JS; onetravel.co.in parked | [S10] |

**4B. Unverified Markets**

| Market | Verification Attempted? | Reason Not Verified | Popular Local APMs (reference) |
|--------|------------------------|---------------------|-------------------------------|
| Canada (.ca) | Yes | No Wayback snapshot since 2020; live 403 | Interac Debit, Interac e-Transfer |
| UK | Yes | Checkout JS-rendered, no archived footer logos | Open Banking, Klarna/Clearpay |
| India | Yes | No affirmative UPI/RuPay/netbanking evidence anywhere | UPI, netbanking, RuPay |
| Philippines | Yes | No market-specific page exists | GCash, Maya |
| Ghana | Yes | Not in APM reference data; no market page | Mobile money (unreferenced) |

> "Not verified" ≠ "not available." MANUAL: VPN checkout walk-through before any APM claim in writing. Never tell the prospect they "lack" a method; anchor on the confirmed USD-only single-checkout architecture instead.

---

## SECTION 5 — Payment Complaints

| Issue Type | Platform | Frequency | Date Range | Source |
|-----------|----------|-----------|------------|--------|
| Multiple charges per booking (separate descriptors per airline/passenger/fee: "Airline/Taxes and Fees", "OT Car", "Agent fee") | OneTravel's OWN FAQ | Institutionalized (pre-written answer + dedicated Billing Dept line 646-738-4943) | Standing | [S19] |
| Duplicate charges for the same trip | Own FAQ + Trustpilot | Institutionalized + recurring reviews (card charged twice, 14-day refund promise) | 2023-2026 | [S19][S20] |
| Charged more than quoted (pending hold at full amount; quote excludes seats/insurance/add-ons) | Own FAQ + Quebec class action (group level) | Institutionalized; ~$20M punitive sought | 2017-ongoing | [S19][S21] |
| Refunds never received / delayed (3-7 days holds, 7-14 days airline refunds, 60-90 days per BBB) | Trustpilot, BBB | 1,421 BBB complaints in 3 yrs (Fareportal group), 809 last 12 mo | 2023-2026 | [S20][S22] |
| Card declined on ancillary (seat charge failed) | Trustpilot | Individual reports | 2025 | [S20] |
| Extra/unexpected fees at checkout ($50 cancel fee, service fees) | SiteJabber/SmartCustomer (3.7/5, 1,673 reviews) | Recurring | 2023-2026 | [S23] |

Rating spread: Trustpilot 4.2/5 (6,549 reviews, solicitation-driven) vs SiteJabber 3.7 vs PissedConsumer 1.6. Reddit: no OneTravel-specific payment threads found.

**Analysis:** the recurring pattern is not declines, it is charge fragmentation and reconciliation. Every booking posts as multiple charges across two PSPs (CyberSource + Braintree) plus ancillaries, which their own FAQ has to explain away. Yuno maps directly: one transaction view across processors, unified reconciliation, consistent charge logic, dispute tooling (Rappi: 80% less analyst resolution time).

---

## SECTION 6 — Expansion & Corporate Developments

| # | Date | Development | Category | Source |
|---|------|-------------|----------|--------|
| 1 | Aug 2025 | Amit Singh (ex-Despegar CFO) joins as CEO & President | Leadership | [S24] |
| 2 | Jan 2026 | Amadeus partnership + Outpayce B2B Wallet (supplier-side virtual cards) | Payments (B2B) 🟢 | [S15] |
| 3 | Mar 2026 | Amit Singh Travel Weekly interview: scaling hotels, cars, B2B | Expansion | [S25] |
| 4 | Apr 2026 | Fareportal Enterprise Solutions launch; markets "payment orchestration, multi-currency flows, mixed cash-and-loyalty, fraud mitigation, reconciliation" as a B2B product | Payments (B2B) 🟢 | [S17] |
| 5 | May 2026 | Sabre partnership expansion (agentic AI distribution) | Expansion | [S26] |
| 6 | Jun 2026 | **ClubMiles loyalty rebuild across CheapOair + OneTravel; points redeemable on airfare; quoted owner: Manish Sharma, SVP Finance and Fintech Products** ("We rebuilt the program to remove friction") | Fintech/Loyalty 🟢 | [S27] |
| 7 | Jun 2026 | Hiring: 39 open Fareportal vacancies in Gurgaon (Naukri); specific payment titles unverifiable (403) | Hiring | [S28] |
| 8 | Jan 2026 | OneTravel app promo push (first-app-booking offers; iOS 4.8/17K ratings, Android 4.7/500K+ installs, dev W K Travel / Fareportal) | Product | [S29] |

Payments org: CFO Gary Starr; **Manish Kumar Sharma, SVP Finance & Fintech Products, owns merchant processing, virtual cards, banking** (at Fareportal since 2013). Champion door: Tom Spagnola, SVP Supplier Relations.

---

## SECTION 7 — Payment News

| # | Date | Headline | Relevance | Source |
|---|------|----------|-----------|--------|
| 1 | Jan 2026 | Fareportal adopts Amadeus Outpayce B2B Wallet | Supplier side orchestrated; consumer side is not | [S15] |
| 2 | Apr 2026 | Enterprise Solutions sells "payment orchestration" to partners | They sell orchestration while their own consumer checkout has none | [S17] |
| 3 | Jun 2026 | ClubMiles rebuild under SVP Finance & Fintech | Loyalty + payments convergence; mixed cash-and-loyalty tenders raise reconciliation stakes | [S27] |
| 4 | 2025-2026 | No consumer PSP additions or removals found | Stack is static; CyberSource + Braintree unchanged | [S16] |

---

## SECTION 8 — Checkout Audit

| Dimension | Finding | Quality | Notes |
|-----------|---------|---------|-------|
| Checkout type | On-site embedded (Affirm selected "while checking out"; Braintree/CyberSource JS in page) | OK | [S10][S13] |
| Guest checkout | Not verified (booking flow not archived) | n/a | MANUAL check |
| Steps to purchase | Not verified | n/a | MANUAL check |
| 3DS | CardinalCommerce present in code | OK | Consistent with CyberSource Payer Auth [S10] |
| Mobile experience | Strong app ratings (iOS 4.8/17K, Android 4.7/6.9K reviews); app-exclusive fee discounts | Good | [S29] |
| APM display logic | One US-style checkout globally; currency selector is display-only; all payments in USD; full AVS (billing address + phone) mandatory | ⚠️ Weak | USD-only per FAQ [S18][S19] |
| Fees at payment | Service fees on air/hotel/car; "up to $50 off fees" promos; post-ticketing and exchange fees $125-350 | ⚠️ | Complaint driver [S19][S30] |

> ⚠️ MANUAL: walk US + Canada checkouts in a real browser (Akamai blocks bots).

---

## SECTION 9 — PCI DSS

| PCI DSS Level | Card data handling | Recommended Yuno integration | Source |
|---------------|--------------------|-----------------------------|--------|
| No public attestation found | Embedded card forms on own checkout; CyberSource + Braintree tokenization; full AVS required | [INFERENCE] Level 1 merchant by volume. Yuno vault + network tokens would cut PCI scope across both PSPs | [S18] |

---

## SECTION 10 — Strategic Insights

**Insight #1: Two PSPs in parallel, zero orchestration, while they SELL orchestration.**
Evidence: S3 (CyberSource + Braintree confirmed, no orchestrator) + S7 (Enterprise Solutions markets "payment orchestration"). Pain: no routing, no failover, no cross-processor view; every wallet transaction lives in Braintree while cards live in CyberSource. Yuno value: one API over both, smart routing (+7% approval), 50% recovery on soft declines. Best case: Kiwi.com runs orchestrated acquiring in the same vertical. Outreach angle: "You already sell payment orchestration to partners and orchestrate supplier settlement through Outpayce. Your own consumer checkout still runs CyberSource and Braintree side by side with no routing layer."

**Insight #2: Reconciliation pain so systemic it lives in their FAQ.**
Evidence: S5 (own FAQ pre-writes answers for multiple charges, duplicate charges, charged-more-than-quoted; dedicated billing phone line; Trustpilot and 1,421 BBB complaints echo it). Pain: charge fragmentation across two PSPs and ancillary fee lines burns support hours, chargebacks and trust. Yuno value: unified reconciliation and single transaction view across processors; Rappi cut analyst resolution 80%. Outreach angle: lead with their own FAQ language, it is unarguable.

**Insight #3: ~39% of traffic pays cross-border in USD on US rails.**
Evidence: S1 (Canada 10.6%, UK 1.4%, PH 1.3%, AU 1.1%, GH 1.0%, IN 1.8%) + S4 ("All payments must be in US Dollars") + S2 (no local acquiring entities). Pain: cross-border MDR, FX spread pushed to customers, structurally lower approval rates on foreign cards. Yuno value: local acquiring routes per market without new entities (MoR partners), weeks not quarters. Best case: inDrive, 10 markets live in under 8 months, 90% approval.

**Insight #4: Philippines +300% traffic on a checkout with no local methods verified.**
Evidence: S1 (PH +300.54%) + S4 (single USD checkout; GCash/Maya unverified). Pain: fastest-growing market where GCash + Maya cover ~45% of digital payments. Yuno value: no-code APM enablement in the fastest growing corridor. Angle: growth market framing, never "you lack GCash" (unverified), but "as Philippines demand accelerates, local tender coverage decides conversion."

**Insight #5: Loyalty-payments convergence under the exact buyer we want.**
Evidence: S6 (ClubMiles rebuild, June 2026, owned and quoted by Manish Sharma, SVP Finance & Fintech Products, whose remit is merchant processing). Pain: mixed cash-and-points tenders multiply reconciliation complexity across two PSPs. Yuno value: orchestration layer that treats loyalty + card + wallet as one transaction. Angle: his own words ("remove friction") applied to checkout.

---

## SECTION 11 — Pipeline

**11A. Direct Competitors**
| Company | Website | HQ | Est. Size | Overlap Markets | Source |
|---------|---------|-----|-----------|-----------------|--------|
| Priceline (Booking Holdings) | priceline.com | Norwalk, CT | Mega-cap parent | US, CA | [S31] |
| Kiwi.com | kiwi.com | Brno, CZ | 100M+ searches, 500+ airlines | Global | [S32] |
| ASAP Tickets / Trevolution (Dyninno) | asaptickets.com | Malta (group) | $1.21B gross bookings 2025, 4,600+ staff | US diaspora/VFR | [S33] |
| Hopper | hopper.com | Montreal | ~$5B val | US, CA | [S34] |
| Trip.com Group | group.trip.com | Shanghai | Largest OTA by GMV | Global | [S35] |
| BudgetAir (Travix) | budgetair.com | NL (Travix) | Storefronts in 12+ countries | US, CA, UK, IN, AU | [S36] |
| KAYAK (meta) | kayak.com | Stamford, CT | $1B-10B band | US | [S37] |
| StudentUniverse (Flight Centre) | studentuniverse.com | Boston | Flight Centre $10B band | US youth | [S37] |

**11B. Industry Peers**: Expedia, Booking.com (in-house payments platforms), eDreams ODIGEO (orchestration-adjacent), MakeMyTrip (India), Despegar (LATAM, CEO Singh's alma mater), Almosafer/Wego (MENA). [S37]

**11C. Adopting Orchestration**
| Company | Orchestrator | Date | Vertical | Source |
|---------|-------------|------|----------|--------|
| Kiwi.com | IXOPAY (+legacy ZOOZ, 12 acquirers) | Standing | OTA flights | [S32] |
| (Vertical signal) | CellPoint Digital: travel-only orchestrator, PayPal partnership Mar 2026, $8B volume | 2025-2026 | Travel | [S38] |

**11D. Scoring (verified only)**
| Signal | Pts | Verified? |
|--------|-----|-----------|
| Operates in 3+ countries | +3 | ✅ traffic + storefronts US/CA + 5 more |
| Multiple PSPs | +3 | ✅ CyberSource + Braintree (first-party JS) |
| Recent expansion (24 mo.) | +2 | ✅ Amadeus, Sabre, Enterprise Solutions, ClubMiles |
| Public payment issues | +2 | ✅ own FAQ + BBB 1,421 + QC class action |
| Funding >$10M (revenue proxy) | +2 | ✅ group revenue $460-487M (3rd-party est.) |
| LATAM/APAC/MENA traffic | +2 | ✅ IN + PH + GH ~4%, PH +300% |
| No orchestrator | +2 | ✅ code-confirmed |
| Payment job postings | +0 | ❌ Gurgaon hiring confirmed, titles not |
| Public RFP | +0 | ❌ none |
| **TOTAL** | **16** | **🔴 High** |

**Top 10 Pipeline:**
| Rank | Company | Type | Key Markets | Score | Priority | Top Signal |
|------|---------|------|-------------|-------|----------|------------|
| 1 | OneTravel/Fareportal | OTA | US, CA | 16 | 🔴 | 2 PSPs, no orchestrator, FAQ-level reconciliation pain |
| 2 | ASAP Tickets/Trevolution | OTA (VFR) | US diaspora | est. 🔴 | High | $1.2B bookings, 25 offices, multi-market | 
| 3 | BudgetAir/Travix | OTA | 12+ storefronts | est. 🟡 | Med | Multi-domain multi-currency |
| 4 | Hopper | OTA/fintech | US, CA | est. 🟡 | Med | Fintech ancillaries at scale |
| 5 | StudentUniverse | OTA niche | US | est. 🟡 | Med | Youth vertical, parent scale |
| 6-10 | Kiwi (reference), Priceline, Trip.com, MakeMyTrip, eDreams | OTA | Global | n/a | Ref | Orchestration proof points / in-house |

Pipeline summary: 13 companies mapped, 2 high-priority beyond target. Strongest vertical: budget/VFR flight OTAs in US + cross-border corridors.

---

## SECTION 12 — Business Case

| Annual Revenue | Avg Transaction Value | Est. Annual Transactions | Primary Currency | Top 3 Markets |
|----------------|----------------------|--------------------------|------------------|---------------|
| OneTravel implied ~$22M (modeled TPV × 10% take, estimate); Fareportal group $460-487M (Zippia/RocketReach/ZoomInfo est.) | ~$550 US benchmark (ARC: US domestic round-trip avg $570 Dec 2025, $543 H1 2025) | ~517K modeled (8.615M visits × 6%) | USD (all payments, per own FAQ) | US, Canada, India |

Modeled TPV $219.9M across 7 countries (78.6% of traffic). Full model: `Business Cases/BC sheets - OneTravel.xlsx` (total benefit $3.94M/yr: $0.65M acceptance uplift, $0.70M fee renegotiation, $0.63M APM growth, $1.97M engineering). Same platform serves CheapOair (~6x the traffic), so group-level upside scales accordingly.

---

## SECTION 13 — Outreach (verified findings only)

```
--- LINKEDIN MESSAGE ---
Hi Manish, your ClubMiles relaunch quote stuck with me: rebuilt to remove friction. The same logic applies one layer down. OneTravel and CheapOair run CyberSource for cards and Braintree for PayPal and Venmo side by side, with no routing or unified reconciliation between them, and your own FAQ has standing answers for multiple charges and duplicate charges per booking. You already orchestrate the supplier side with Outpayce and even sell payment orchestration through Enterprise Solutions. Yuno is that layer for your consumer checkout: one API across both processors, smart routing that lifts approvals ~7%, one reconciliation view that kills the duplicate-charge tickets, and local acquiring for the ~39% of traffic paying cross-border in USD. Kiwi.com runs orchestrated acquiring in your vertical; inDrive went live in 10 markets with us in under 8 months. Worth 20 minutes to map it against your current setup? Tuesday or Thursday work well.

--- COLD EMAIL ---
Subject: OneTravel's two processors and the FAQ that explains them

Hi Manish,

Your billing FAQ has pre-written answers for multiple charges per booking, duplicate charges, and charged more than quoted, plus a dedicated billing phone line. That is not a support problem. It is an architecture problem: cards clear through CyberSource while PayPal and Venmo clear through Braintree, every booking fragments into separate charge lines, and no layer reconciles across them.

You have already solved this on the supplier side with Outpayce, and Enterprise Solutions now sells payment orchestration to partners. The consumer checkout is the piece still running unrouted.

Yuno puts one API over CyberSource and Braintree: smart routing lifts approvals around 7 percent, failed transactions recover at up to 50 percent, and reconciliation collapses into one view across processors, currencies and loyalty tenders, which matters more now that ClubMiles points redeem against airfare. For the roughly 39 percent of OneTravel traffic paying in USD from Canada, the UK, the Philippines and beyond, local acquiring routes lift approval without new entities.

Rappi cut payment analyst resolution time 80 percent on Yuno. inDrive reached 90 percent approval across 10 new markets in under 8 months. Kiwi.com already runs orchestrated acquiring in your exact vertical.

Worth 20 minutes to compare against your current consumer setup? I have Tuesday and Thursday afternoon open.

Germán Tatis
Yuno | german.tatis@y.uno
```

---

## APPENDIX — Source URLs
```
[S1]  SimilarWeb geography panel, onetravel.com, annual view (user-provided, Jul 2026)
[S2]  https://www.semrush.com/website/onetravel.com/overview/
[S3]  https://www.similarweb.com/website/onetravel.com/
[S4]  https://hypestat.com/info/onetravel.com
[S5]  http://web.archive.org/web/20260411083819/https://www.onetravel.com/info/privacy-policy/
[S6]  http://web.archive.org/web/20260411085553/https://www.onetravel.com/info/generaltermsandconditions/
[S7]  https://www.bbb.org/us/nv/las-vegas/profile/travel-agency/wk-travel-inc-1086-79312
[S8]  https://www.tofler.in/fare-portal-india-private-limited/company/U72900DL2005PTC134394 · https://lei.bloomberg.com/leis/view/254900LNP7B8L1ZNY382
[S9]  https://www.transportation.gov/airconsumer/eo-2014-1-1
[S10] web.archive.org/web/20250211143156/https://www.onetravel.com/air/paymentoption.bundle.3eaa2fa386a3d4e29797.js (+ CheapOair bundle, see fareportal-2026-07-23.md addendum)
[S11] https://fraud.net/resources/case-study-fareportal-travel-agency/
[S12] http://web.archive.org/web/20230518114247/https://www.onetravel.com/faq/ (USD billing; Canada RSH registration in [S6])
[S13] http://web.archive.org/web/20251115174809/https://www.onetravel.com/flights/book-now-pay-later
[S14] https://www.synchrony.com/contenthub/newsroom/cheapoair-and-onetravel-launch-new-travel-rewards-credit-cards.html
[S15] https://amadeus.com/en/newsroom/press-releases/fareportal-partnership-amadeus-innovation-travel
[S16] 2025-2026 PSP news sweep: no results (Agents A+B, Jul 2026)
[S17] https://www.prweb.com/releases/fareportal-announces-launch-of-fareportal-enterprise-solutions-enabling-partners-to-own-and-scale-travel-offerings-302758710.html
[S18] web.archive.org/web/20121029162848/http://faq.onetravel.com/billing-payments.asp (card list re-confirmed via 2026 live-page snippet)
[S19] http://web.archive.org/web/20230518114247/https://www.onetravel.com/faq/
[S20] http://web.archive.org/web/20251208210645/https://www.trustpilot.com/review/www.onetravel.com
[S21] https://topclassactions.com/lawsuit-settlements/money/fees/cheapoair-facing-a-class-action-lawsuit-over-charging-customers-more-than-the-final-price/
[S22] https://www.bbb.org/us/ny/new-york/profile/travel-agency/fareportal-inc-0121-89212/complaints
[S23] https://www.smartcustomer.com/reviews/onetravel.com
[S24] Memory/prior research: Amit Singh CEO Aug 2025 (fareportal-2026-07-23.md)
[S25] https://www.travelweekly.com/On-The-Record/Amit-Singh-Fareportal
[S26] https://www.prweb.com/releases/fareportal-expands-long-term-partnership-with-sabre-to-accelerate-global-growth-and-ai-driven-distribution-302780866.html
[S27] https://www.fareportal.com/fareportal-announces-major-enhancement-to-clubmiles-loyalty-program-allowing-members-to-apply-points-directly-to-flights/
[S28] https://www.naukri.com/fareportal-jobs-in-gurgaon
[S29] https://apps.apple.com/us/app/onetravel-flight-hotel-deals/id680520990 · https://play.google.com/store/apps/details?id=com.wkt.onetravel.android
[S30] https://www.onetravel.com/flights/travel-deals
[S31] https://press.priceline.com/
[S32] https://www.kiwi.com/en/pages/content/about
[S33] https://trevolution.group/
[S34] https://media.hopper.com/
[S35] https://group.trip.com/
[S36] https://www.budgetair.com/
[S37] https://leadiq.com/c/fareportal/5a1d8939240000240062b527
[S38] https://www.cellpointdigital.com/news
```
