# SDR Research Brief — Fareportal (CheapOair, OneTravel)
*Yuno Payment Orchestrator · Framework v8.0 · 2026-07-27 · supersedes fareportal-2026-07-23.md (retains all confirmed findings + 4-agent refresh)*
*Deliverable live: custom deck with subaccount PSP topology at deck.yuno.tools/m/fareportal*

## EXECUTIVE SUMMARY
Fareportal is a New York travel technology company (Fareportal Holdings Inc., DE; founder Sam Jain; CEO & President Amit Singh, ex-CFO of Despegar) running the OTAs CheapOair and OneTravel plus Travelong, FareBuzz, Duke's Court Travel (UK) and ConTravel (MX), selling 500+ airlines to travelers in 195 countries. The consumer payment stack is CONFIRMED via first-party checkout JavaScript: CyberSource (cards + Google Pay) and Braintree (PayPal + Venmo) running in parallel on one shared platform for both brands, CardinalCommerce 3DS, Accertify anti-fraud, Affirm BNPL natively integrated, and NO consumer-side orchestrator, while the supplier side is already orchestrated (Amadeus Outpayce B2B Wallet) and Fareportal even sells "payment orchestration" B2B. The Yuno wedge: a consumer-side orchestration layer across the two confirmed processors (routing, failover, recovery) that fixes the litigated/complained-about decline-then-recharge and duplicate-charge patterns, plus reconciliation for the new ClubMiles points-toward-airfare split tender owned by Manish Kumar Sharma, SVP Finance & Fintech Products, the payments buyer.

**Traffic conflict RESOLVED this pass:** OneTravel is US-dominant (~70% US, June 2026 SimilarWeb), NOT India-dominant. The earlier Semrush "India 45.8%" reading is a transient anomaly Semrush itself flags as a +1,636.7% momentum spike. Do not lead with India.

---

## SECTION 1 — Traffic by Country

**cheapoair.com** ~6.5–6.7M visits/mo, +30.96% MoM (~5.1M Feb → 6.7M Mar 2026). [S1]
**onetravel.com** ~635–644K visits/mo (SimilarWeb Jun 2026: −6.02% MoM; Hypestat Jan→Mar: +62% off a low base). [S2][S3]

| Brand | Rank | Country | Share | Source |
|-------|------|---------|-------|--------|
| CheapOair | 1 | United States | 80.93% | [S1] |
| CheapOair | 2 | Canada | 2.38% | [S1] |
| CheapOair | 3 | India | 1.25% | [S1] |
| CheapOair | 4 | Saudi Arabia | 0.93% | [S1] |
| CheapOair | 5 | Argentina | 0.76% | [S1] |
| OneTravel | 1 | United States | 69.7% (SW Jun 2026) / 65.55% (Hypestat) | [S2][S3] |
| OneTravel | 2 | Canada | 7.09% / 6.21% | [S2][S3] |
| OneTravel | 3 | Puerto Rico | 1.39% / 2.67% | [S2][S3] |
| OneTravel | 4 | Philippines / Mexico | 1.21% / 1.89% | [S2][S3] |
| OneTravel | 5 | Thailand / India | 0.84% / 1.10% | [S2][S3] |

- Ranks 6–10: Not found (paywalled on all free sources).
- **OneTravel geo verdict:** US-dominant. Semrush's India 45.8% is flagged by Semrush's own "Trending Travel Websites in India" page as a +1,636.7% momentum anomaly; SimilarWeb's June 2026 panel has India outside OneTravel's top 5. [INFERENCE — transient India spike, not a stable audience shift.] [S2][S4]
- Emerging-market long tail (India, Saudi, Argentina, PR, PH, TH, MX) is real but small per market.

---

## SECTION 2 — Legal Entities

| Country | In Top Traffic? | Local Entity? | Cross-Border Risk? | Source |
|---------|-----------------|---------------|--------------------|--------|
| USA | Yes (both) | Fareportal Holdings Inc. (DE) → Fareportal Inc. (NY); WK Travel, Inc. (NV) d/b/a OneTravel; Travelong, Inc. (NJ); Onetravel Group, Inc. (NY, 2021) | Home market | [S5][S6][S7] |
| India | Yes (small) | Fare Portal India Pvt Ltd (CIN U72900DL2005PTC134394, Delhi; ops Gurugram + Pune; ₹481 Cr FY25 revenue; ~2,157 staff) | Service/dev center; consumer billing entity for India buyers not confirmed | [S8][S9] |
| Canada | Yes | Offices Toronto + Montreal; BBB lists "CheapOair.ca" (Markham, ON). Canadian legal entity name / TICO: Not found | ⚠️ cheapoair.ca FAQ warns Canadian cardholders "currency conversion rates are in effect" → non-CAD (likely USD) settlement signal | [S10][S11][S24] |
| UK | Regional domain | UK Companies House: "fareportal" = zero results. Presence via acquired brand Duke's Court Travel. (CHEAPOAIR LTD #15847020, dissolved 2025-01-28, mass-registration address — [INFERENCE] unrelated opportunistic filing) | ⚠️ Potential cross-border operation — no local entity found | [S12][S13] |
| Mexico | OneTravel top-5 (Hypestat) | Brand ConTravel ("Mexico-based consolidator") | Entity name not found | [S13] |
| UAE / Ukraine | Offices per third-party profiles | No entity names found | ⚠️ Not verified | [S10] |

HQ note: current HQ 135 West 50th Street, Suite 500, NYC (vs 137 W 25th St in the 2021 JetBlue complaint). [S10]
> ⚠️ MANUAL: live T&Cs for onetravel.com / cheapoair.ca are Akamai-403'd; merchant-of-record per storefront rests on WK Travel d/b/a OneTravel (US DOT order EO-2014-1-1) and [INFERENCE] Fareportal Inc for CheapOair.

---

## SECTION 3 — Payment Stack

**3A. PSPs & processors (CONFIRMED via first-party checkout JS on Wayback; both brands = one platform, byte-identical asset hashes)**

| Layer | Vendor | Role | Confidence | Evidence |
|---|---|---|---|---|
| Card gateway / PSP | **CyberSource (Visa)** | Cards + Google Pay (`Gateway:"cybersource"`, GatewayMerchantId 007100) | High | [A1] |
| PSP for wallets | **Braintree (PayPal)** | PayPal + Venmo (prod TokenizationKey, MerchantAccountId `CheapOair_instant`/`fareportal`) | High, both brands | [A1][A2] |
| 3-D Secure | **CardinalCommerce (Visa)** | Payer auth | High | [A3] |
| Anti-fraud | **Accertify (Amex)** + Fraud.net (2019 case study) + in-house Gurgaon review team | Device intel / scoring / manual review | High | [A3][A4][A5] |
| Edge | **Akamai** bot management (the 403 blocker) | CDN/bot | High | live headers |
| Co-brand issuer (adjacent) | **Synchrony** (CheapOair + OneTravel travel rewards cards, doc ref "ONETRAVEL/CHEAPOAIR [WF7840401EE]") | PLCC | High | [S14] |
| Acquiring bank behind CyberSource | **No public information found** | — | — | dedicated search, nothing named |

Ruled out (explicit, code-level): Stripe, Adyen, Worldpay, Chase Paymentech, FIS/Vantiv, First Data, Elavon; Riskified, Signifyd, Forter, Sift, Kount, ThreatMetrix, Iovation.

**3B. Orchestrator:** consumer side — **none found** (no Spreedly/Primer/Gr4vy/CellPoint/APEXX in code). Supplier side — **Amadeus Outpayce B2B Wallet** (Jan 2026) [S15]; Fareportal also SELLS "payment orchestration" via Enterprise Solutions (Apr 2026) [S16]. Never pitch "you lack orchestration"; pitch the consumer-side acquiring layer.
> ⚠️ MANUAL — DevTools on live checkout (real browser beats Akamai): test card 4111 1111 1111 1111 | 02/30 | 123.

---

## SECTION 4 — APMs (Agent D live verification, 2026-07-27)

**4A. Confirmed APMs**

| Market | APMs Confirmed | Verification Source | Source URL |
|--------|----------------|---------------------|------------|
| US both brands | **Affirm (native)** — Affirm JS v2 embed + Public API Key live in page; OneTravel snapshot is FRESH (2025-11-15); loans via Cross River Bank | First-party BNPL landing pages (Wayback) | [A6][A7] |
| US CheapOair | **Paze** (2024 consumer-facing: one of only 7 stores per finder.com; 2026 code-level find stands; 2026 consumer lists don't show it — status "code-confirmed, consumer NOT re-verified") | finder.com + checkout JS | [A8][A1] |
| US both brands | Cards V/MC/Amex/Discover/Diners + Synchrony PLCC; PayPal + Venmo (code-level); Apple Pay; Google Pay | Checkout JS + Synchrony newsroom | [A1][S14] |
| Canada (cheapoair.ca) | Visa, Mastercard, Amex, Discover + US/CA debit cards; "cheque of any type not accepted"; split-tender (2 cards) only via phone | Official Payment & Billing FAQ (Wayback 2022-12-18, latest available) | [A9] |

**Negative verifications (safe to state):**
- **Sezzle and Zip are NOT native**: their own store pages instruct shoppers to generate app virtual cards for CheapOair. Card-rail overlays, no Fareportal integration. [A10]
- **Accrue Savings**: accruesavings.com now 301s to byaccrue.com (B2B loyalty-wallet pivot), no CheapOair mention. The checkout-JS reference may be legacy. 2026 consumer status NOT VERIFIED. [A11]

**4B. Unverified markets (do NOT treat as gaps)**

| Market | Attempted? | Reason Not Verified | Popular Local APMs (opportunity, unclaimed) |
|--------|-----------|---------------------|---------------------------------------------|
| Canada 2026 state | Yes | 2026-06-06 snapshot exists but archive.org data plane reset connections; live 403 | Interac |
| UK (cheapoair.co.uk) | Yes | Same (2026-04-10 snapshot exists, unretrievable); live 403 | Open banking |
| Mexico | Yes | Latest snapshot 2013; es./mx. subdomains zero snapshots | OXXO, SPEI |
| India | Yes | cheapoair.co.in latest 2013; onetravel.co.in / in.cheapoair.com zero snapshots (consistent with parked/dead) | UPI, RuPay, netbanking |
| Help centers | Yes | onetravel.com/faq/payments.asp + help.cheapoair.com: zero snapshots, live 403 | — |

> "Not verified" ≠ "not available." MANUAL: VPN + real-browser checkout walk-through before any APM claim. Retry targets for next session: the two 2026 homepage snapshots (cheapoair.ca 2026-06-06, cheapoair.co.uk 2026-04-10).

---

## SECTION 5 — Payment Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|-----------|----------|-----------|------------|------------|
| Debited → "payment declined" notice → debited AGAIN without authorization; 25 emails w/ bank statements, wrongdoing denied | Trustpilot (UK) | Recurring pattern, both brands | pre-2026 | [S17] |
| Charged more than displayed "Final Total Price" (class action) | Quebec Superior Court | Filed 2020; **no settlement/authorization/hearing update found 2025–2026** (not in CLG list nor MTL Blog Jun 2026 roundup; Registry needs interactive search) | 2020– | [S18][S19] |
| Refund delays (60–90 days), post-ticketing fees, duplicate charges → chargebacks | BBB (Fareportal Inc) | 1,421 complaints/3 yrs | rolling | [S20] |
| $2,000 refund never received; luggage charged twice, refund denied within the hour; 24h fee-free cancellation never processed | App Store reviews (4.8★/264K overall) | Individual but consistent theme | Jun 2024–Dec 2025 | [S21] |
| Overcharging, double charges, refund friction | OneTravel PissedConsumer 1.6★; JustUseApp safety 30/100 (NLP on 253K reviews) | High | rolling | [S22][S23] |
| Managed-review contrast: Trustpilot 4★ (~35.3K reviews COA, ~7.4K OT), company actively responding | Trustpilot | — | Jul 2026 | [S17] |

Analysis: the decline-then-recharge pattern is [INFERENCE] consistent with auth-retry/duplicate-capture behavior with no orchestration-layer idempotency; duplicate charges + 60–90-day refunds + chargebacks map to Yuno's unified transaction view, reconciliation and dispute tooling across CyberSource + Braintree + Affirm. Currency/FX complaints: none surfaced this pass.

---

## SECTION 6 — Expansion & Corporate Developments

| # | Date | Development | Category | Source |
|---|------|-------------|----------|--------|
| 1 | Apr 2025 | Frontier Airlines NDC API integration | Distribution | [S25] |
| 2 | Aug 28 2025 | **Amit Singh appointed President** (ex-CFO Despegar, NYSE-listed LatAm travel tech; Wall Street background); now "CEO & President" per leadership page ([INFERENCE] CEO title added later, no standalone PR found) | Leadership | [S26][S27] |
| 3 | Jan 2026 | Amadeus partnership; adopts **Outpayce B2B Wallet** (virtual-card supplier settlement) | Payments | [S15] |
| 4 | Apr 2026 | Launches **Fareportal Enterprise Solutions**, markets "payment orchestration" B2B | Payments | [S16] |
| 5 | May 2026 | Sabre partnership expansion; "agentic AI orchestrating end-to-end shopping" + NDC | Distribution | [S28] |
| 6 | **Jun 3 2026** | **ClubMiles rebuilt: points redeem directly toward airfare** (majority of flights), Double-Dip Rewards, 2x points on app bookings. Quote from **Manish Sharma, SVP Finance and Fintech Products**: "We rebuilt the program to remove friction..." [INFERENCE] points-toward-airfare implies split-tender (points + card) logic under the payments owner's org | Payments/Loyalty | [S29] |

**Leadership (all confirmed on fareportal.com/leadership, fetched live 2026-07-27):** Sam S. Jain, Founder & Executive Chairman · Amit Singh, CEO & President · **Gary Starr, CFO** · **Manish Kumar Sharma, SVP Finance & Fintech Products** (the payments/fintech owner; prior sourced scope: merchant processing, virtual cards, banking; at Fareportal since ~2013) · Yuvraj Datta, Chief Supply & Revenue Officer. [S27]

**Jobs:** fareportal.com/careers and /job-openings both 404; no careers link in current site nav ([INFERENCE] hiring routed to LinkedIn/Naukri). Naukri shows 29 vacancies (39 in Gurugram) per indexed titles, role names bot-walled. No payments-title postings verifiable this pass. [S30]

---

## SECTION 7 — Payment News (rolling 12 months)

| # | Date | Headline | Relevance | Source |
|---|------|----------|-----------|--------|
| 1 | Jan 2026 | Outpayce B2B Wallet adoption | 🟢 Supplier side orchestrated; consumer side is the open question | [S15] |
| 2 | Apr 2026 | Enterprise Solutions sells "payment orchestration" | 🟢 They speak orchestration natively | [S16] |
| 3 | Jun 2026 | ClubMiles points-toward-airfare, fronted by the SVP Finance & Fintech Products | 🟢 Fresh, payments-owned catalyst; split-tender + reconciliation hook | [S29] |
| 4 | Jun–Jul 2026 | No new PSP/BNPL/wallet partnerships, removals, exec changes or M&A found; no July 2026 PRs on the press page as of Jul 27 | — | [S31] |

---

## SECTION 8 — Checkout Audit

| Dimension | Finding | Quality | Notes |
|-----------|---------|---------|-------|
| Checkout type | Web + phone + mobile app (iOS/Android), one shared platform both brands | — | [S32][A1] |
| Guest checkout | Not verified (Akamai 403) | — | — |
| Steps to purchase | Search → select → passenger details + payment → confirmation (app-listing description); processing fee added for all ticket types at checkout | ⚠️ | [S32][S33] |
| 3DS | CardinalCommerce present in code; consumer friction not verified | — | [A3] |
| Mobile experience | iOS 4.8★ (264K); Play ~4.75★ (~83K); company steering volume to app with 2x ClubMiles points | 🟢 channel, ⚠️ refund themes | [S21][S29] |
| APM display logic | Same US-style checkout all markets, currency display localization only (code-level) | ⚠️ | [A1] |

> ⚠️ MANUAL: walk CheapOair US + OneTravel US checkouts in a real browser; capture PSP/3DS network calls.

---

## SECTION 9 — PCI DSS

| PCI DSS Level | Card data handling | Recommended Yuno integration | Source |
|---------------|--------------------|-----------------------------|--------|
| Not publicly disclosed | Cards processed as merchant via CyberSource; [INFERENCE] IATA-accredited agencies charging cards as merchant must maintain PCI DSS; at this volume almost certainly Level 1 | Yuno vault + network tokenization to cut PCI scope across both brands and all processors | [S34] |

---

## SECTION 10 — Strategic Insights

**Insight #1: Supplier side orchestrated, consumer side confirmed fragmented.**
Evidence: S3 (CyberSource + Braintree in parallel, no orchestrator in code), S15/S16. Pain: no routing/failover between two live processors on high-decline airfare. Yuno: consumer-side orchestration across the exact confirmed rails, +7% approval uplift. Best case: Kiwi.com (orchestrated OTA peer). Angle: "You orchestrate supplier settlement with Outpayce and sell orchestration through Enterprise Solutions; the consumer checkout still runs CyberSource and Braintree side by side with nothing routing between them."

**Insight #2: ClubMiles split tender is a warm, payments-owned doorway (NEW).**
Evidence: S29 — Manish Sharma publicly fronting points-toward-airfare redemption. Pain: split tender (points + card) across two processors plus a loyalty ledger multiplies reconciliation and partial-refund complexity, exactly the complaint categories already hurting them (S5). Yuno: one transaction view + reconciliation across processors and tenders. Angle: congratulate the ClubMiles relaunch, then ask how points+card settles and reconciles across CyberSource and Braintree today.

**Insight #3: The decline-then-recharge / duplicate-charge pattern is a recovery + idempotency story.**
Evidence: S5 (Trustpilot double-debit, BBB 1,421, App Store refund themes; Quebec class action dormant but alive). Yuno: cascade retries with idempotent capture, 50% recovery on failed transactions, dispute tooling. Best case: Livelo (+5% approvals, 50% recovery).

**Insight #4: Cross-border settlement leakage signals in Canada.**
Evidence: A9 — official FAQ warns Canadian cardholders that currency conversion applies. [INFERENCE] non-CAD settlement on a 7%-of-OneTravel / 2.4%-of-CheapOair market = FX spread + foreign-issuer decline drag. Yuno: local acquiring via the same API. Do NOT claim missing local methods; frame as settlement currency question.

**Insight #5: India demoted to exploratory.**
Evidence: S1/S2 — OneTravel is US-dominant; India ~1% on both brands. The Gurgaon center (2,157 staff) means build-vs-buy bias, not consumer demand. Keep UPI in the local-methods menu; do not lead with it.

---

## SECTION 11 — Pipeline

**11A/11B. OTA competitors & peers** (carried from 2026-07-23 brief, unchanged): Expedia (in-house payments platform), Booking Holdings (in-house), Trip.com, eDreams ODIGEO, **Kiwi.com (confirmed IXOPAY + 12 acquirers)**, Hopper, Despegar, MakeMyTrip, Almosafer/Wego. [S35]

**11C. Adopting Orchestration (travel, fresh this pass)**
| Company | Orchestrator | Date | Vertical | Source |
|---------|-------------|------|----------|--------|
| Southwest Airlines | CellPoint Digital (Offer & Order; cards + APMs + Rapid Rewards points in ONE transaction — the exact ClubMiles-style split-tender problem) | Mar 2025 | Airline | [S36] |
| Riyadh Air | CellPoint Digital (early adopter, new travel platform) | Feb 2025 | Airline | [S37] |
| Kiwi.com | IXOPAY | prior | OTA | [S35] |
| Fareportal itself | Outpayce (supplier side only) | Jan 2026 | OTA | [S15] |

**11D. Scoring (verified only)**
| Signal | Pts | Verified? |
|--------|-----|-----------|
| Operates in 3+ countries | +3 | ✅ US, CA, UK, IN, MX, UAE |
| Multiple PSPs | +3 | ✅ CyberSource + Braintree (first-party JS) — upgraded from 0 in prior brief |
| Recent expansion (24 mo.) | +2 | ✅ Outpayce, Enterprise Solutions, Sabre, ClubMiles |
| Public payment issues | +2 | ✅ Class action + BBB + Trustpilot pattern |
| Revenue scale (funding proxy) | +2 | ✅ ~$460–488M est. |
| LATAM/APAC/MENA traffic | +2 | ✅ IN/SA/AR/PH/TH/MX tail |
| No (consumer) orchestrator | +2 | ✅ code-confirmed none |
| Payment job postings | +0 | Not verifiable (bot-walled) |
| Public RFP | +0 | None found |
| **Total** | **16** | **🔴 High** |

Pipeline summary: OTA vertical, best comparables Kiwi.com (orchestrated OTA) and Southwest (points split-tender via orchestrator). Strongest wedge: consumer-side routing/recovery + ClubMiles reconciliation, US-first.

---

## SECTION 12 — Business Case

| Annual Revenue | Avg Transaction Value | Est. Annual Transactions | Primary Currency | Top 3 Markets |
|----------------|----------------------|--------------------------|------------------|---------------|
| ~$460M (RocketReach) to $487.5M (Zippia) — aggregator ESTIMATES, private co. India entity alone: ₹481 Cr (~$57M) FY25 (MCA filing, service center) | ARC industry benchmark: **$570 avg US domestic round-trip ticket, Dec 2025 (+2% YoY)**; economy ATP $514 | Not disclosed. [INFERENCE] At ~$3.5B-era gross bookings (2014, dated) and $570 ATP, order-of-magnitude millions of tickets/yr | USD (also CAD, GBP, AED, INR displays) | US, Canada, then long tail (IN/SA/AR/PR/PH) |

Context: US travel-agency air sales hit a record $100.4B in 2025 (ARC). Company self-reports 2,000+ employees, 7 brands, 195 countries, 40M+ lifetime travelers (homepage, live 2026-07-27; third-party profiles say ~3,152 staff). [S38][S39][S8]

---

## SECTION 13 — Outreach (verified findings only; target: Manish Kumar Sharma, SVP Finance & Fintech Products; Tom Spagnola = door-opener, not buyer)

```
--- LINKEDIN MESSAGE ---
Hi Manish, congrats on the ClubMiles relaunch. Points redeeming directly toward airfare is a real product change, not a marketing refresh, and it lands squarely in your world: every points plus card booking now settles across two processors and a loyalty ledger.

That is the part I would love to compare notes on. Your consumer checkout runs CyberSource and Braintree side by side, with nothing routing between them, while your supplier side is already orchestrated through Outpayce. Yuno is the layer OTAs put on the consumer side: per-transaction routing across processors for higher approval on airfare, idempotent retries so a declined attempt never becomes a duplicate charge, and one reconciliation view across processors, Affirm and points redemptions. Kiwi.com runs orchestrated acquiring in your vertical; Southwest just solved the same points-plus-card transaction problem with an orchestration layer; inDrive hit 90% approval across 10 markets on Yuno.

Worth 20 minutes to map how points plus card settles today and where approval and recovery upside sits? Tuesday or Thursday afternoon works on my side.

--- COLD EMAIL ---
Subject: ClubMiles points + card: how does it settle across CyberSource and Braintree?

Hi Manish,

The ClubMiles relaunch caught my attention: points applying directly to airfare on most flights means every redemption booking is now a split-tender transaction touching your card gateway, your PayPal rail and a loyalty ledger at once.

From the outside, your consumer stack runs CyberSource and Braintree in parallel with no routing layer between them, while the supplier side is already orchestrated through Outpayce. On airfare-sized tickets, that gap usually shows up in three places: declines that never retry on the second processor, retries that turn into duplicate charges and disputes, and reconciliation that gets slower with every new tender type.

Yuno sits on top of the processors you already have. One API routes each transaction by BIN, issuer and market (about +7% approval across our base), cascades failed payments with idempotent capture (up to 50% recovery), and gives finance one reconciliation view across processors, Affirm and points redemptions. Kiwi.com runs orchestrated consumer acquiring in your vertical, and Southwest adopted an orchestration layer specifically to combine cards, alternative payments and loyalty points in one transaction.

Worth 20 minutes to walk through the points plus card flow and where the approval and recovery upside sits for CheapOair and OneTravel? I have Tuesday or Thursday afternoon open.

[Signature]
```

---

## APPENDIX — Source URLs
```
[S1]  https://hypestat.com/info/cheapoair.com
[S2]  https://www.similarweb.com/website/onetravel.com/ (data month Jun 2026)
[S3]  https://hypestat.com/info/onetravel.com
[S4]  https://www.semrush.com/trending-websites/in/travel-and-tourism
[S5]  https://s3.amazonaws.com/media.wandr.me/PaxExAero/Fareportal+Complaint+-+filed+version.pdf (E.D.N.Y. 1:21-cv-00061, Parties section)
[S6]  https://www.transportation.gov/airconsumer/eo-2014-1-1 (WK Travel d/b/a OneTravel)
[S7]  https://www.bizprofile.net/ny/new-york/onetravel-group-inc
[S8]  https://tracxn.com/d/legal-entities/india/fare-portal-india-private-limited/__jACAv2facfvJj1pJw9XWGCRsUtr9wPfukpCaYYygVpY
[S9]  https://www.indiafilings.com/search/fare-portal-india-private-limited-cin-U72900DL2005PTC134394
[S10] https://www.highperformr.ai/company/fareportal
[S11] https://www.bbb.org/ca/on/markham/profile/travel-agency/cheapoairca-0107-1227946
[S12] https://find-and-update.company-information.service.gov.uk/search?q=fareportal · /search?q=cheapoair
[S13] https://www.fareportal.com/about/
[S14] https://www.synchrony.com/contenthub/newsroom/experience-exciting-travel-adventures-with-synchrony-financial.html · https://apply.syf.com/cs/groups/public/documents/et_tcdoc/e050345.pdf
[S15] https://amadeus.com/en/newsroom/press-releases/fareportal-partnership-amadeus-innovation-travel
[S16] https://www.prweb.com/releases/fareportal-announces-launch-of-fareportal-enterprise-solutions-enabling-partners-to-own-and-scale-travel-offerings-302758710.html
[S17] https://www.trustpilot.com/review/www.cheapoair.com · https://uk.trustpilot.com/review/www.cheapoair.com?page=278 · https://www.trustpilot.com/review/www.onetravel.com
[S18] https://clg.org/Class-Action/List-of-Class-Actions · https://www.mtlblog.com/class-action-lawsuit-settlement-quebec-2026
[S19] https://ca.topclassactions.com/lawsuit-settlements/money/fees/class-action-lawsuit-filed-against-cheapoair-over-ticket-prices
[S20] https://www.bbb.org/us/ny/new-york/profile/travel-agency/fareportal-inc-0121-89212/complaints
[S21] https://apps.apple.com/us/app/cheapoair-cheap-flight-deals/id436858222?see-all=reviews
[S22] https://onetravel.pissedconsumer.com/review.html
[S23] https://justuseapp.com/en/app/436858222/cheapoair-cheap-flight-deals/reviews
[S24] (see A9 — cheapoair.ca payments FAQ)
[S25] https://news.flyfrontier.com/fareportal-and-frontier-airlines-launch-ndc-api-to-offer-travelers-more-personalized-options/
[S26] https://www.prnewswire.com/news-releases/fareportal-inc-appoints-amit-singh-as-president-302541147.html
[S27] https://www.fareportal.com/leadership/
[S28] https://www.prweb.com/releases/fareportal-expands-long-term-partnership-with-sabre-to-accelerate-global-growth-and-ai-driven-distribution-302780866.html
[S29] https://www.fareportal.com/fareportal-announces-major-enhancement-to-clubmiles-loyalty-program-allowing-members-to-apply-points-directly-to-flights/
[S30] https://www.naukri.com/fareportal-jobs · https://www.naukri.com/fareportal-jobs-in-gurgaon
[S31] https://www.fareportal.com/press-releases/
[S32] https://www.appbrain.com/app/cheapoair-cheap-flight-deals/com.fp.cheapoair · https://appmaus.com/app/cheapoair-cheap-flight-deals
[S33] https://upgradedreviews.com/cheapoair-reviews/
[S34] https://www.iata.org/en/services/finance/pci-dss/
[S35] https://silviglobaltechnology.com/blog/best-otas-in-2026/ · https://mize.tech/blog/online-travel-agencies-market-share-across-the-world/
[S36] https://www.pymnts.com/travel-payments/2025/cellpoint-and-southwest-expand-payment-orchestration-partnership/
[S37] https://www.prnewswire.com/news-releases/cellpoint-digital-launches-new-industry-standard-payment-platform-purpose-built-for-airlines-travel-companies-and-their-customers-302378370.html
[S38] https://www2.arccorp.com/about-us/newsroom/2026-news-releases/december-2025-air-ticket-sales/
[S39] https://www.fareportal.com/ (homepage stats, live 2026-07-27)

[A1]  web.archive.org/web/20260626225207/https://www.cheapoair.com/air/paymentoption.bundle.8e517cea72796b9c65a1.js
[A2]  web.archive.org/web/20250211143156/https://www.onetravel.com/air/paymentoption.bundle.3eaa2fa386a3d4e29797.js
[A3]  web.archive.org/web/20250624211940/https://www.cheapoair.com/air/iln/desktop/en-us/2.2.821/_air_payment
[A4]  fraud.net/resources/case-study-fareportal-travel-agency/
[A5]  web.archive.org/web/20260411083819/https://www.onetravel.com/info/privacy-policy/
[A6]  web.archive.org/web/20230202201910/https://www.cheapoair.com/flights/book-now-pay-later-flights
[A7]  web.archive.org/web/20251115174809/https://www.onetravel.com/flights/book-now-pay-later
[A8]  https://www.finder.com/banking/paze-digital-wallet
[A9]  web.archive.org/web/20221218122529/https://www.cheapoair.ca/faq/payments.asp
[A10] https://sezzle.com/shop/cheapoair/ · https://zip.co/us/store/cheapoair
[A11] https://byaccrue.com (accruesavings.com 301s here) · prnewswire.com Jun 2023 partnership release
```
