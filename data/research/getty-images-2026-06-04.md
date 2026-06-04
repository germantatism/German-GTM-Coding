# SDR Research Brief — Getty Images
*Yuno Payment Orchestrator · Framework v8.0 · Researched 2026-06-04*
*All findings from public web data. PSP/gateway names NOT publicly confirmed — see §3. Where uncertain, disclaimers applied.*

---

## EXECUTIVE SUMMARY

Getty Images Holdings (NYSE: GETY) is the global stock-media leader, operating gettyimages.com plus higher-volume self-serve brand **iStock** (istockphoto.com, ~60M visits/mo) and Unsplash, across **30+ local billing entities in 50+ countries** with multi-currency, subscription-led revenue (**54%+ recurring**, $981M FY2025). The actual PSP/gateway and any orchestrator are **not publicly disclosed**, but Getty confirms it uses third-party processors + card-network **Account Updater** services and staffs a dedicated internal **"Director of Payments."** The standout Yuno opportunity is **subscription billing recovery / dunning** — auto-renewal and cancellation friction is so severe it drew an **ACCC regulatory settlement (~AUD $78K refunds)** and 313 BBB complaints — compounded by the pending **Getty + Shutterstock merger**, which forces consolidation of multiple billing/checkout stacks under stated $150–200M synergy targets.

---

## SECTION 1 — Traffic by Country

**gettyimages.com** — ~17.2M visits/mo, global rank #2,291 (SimilarWeb)

| Rank | Country | Traffic Share | Trend | Source |
|------|---------|--------------|-------|--------|
| 1 | United States | 56.08% | — | [S1] |
| 2 | Ukraine | 3.18% | — | [S1] |
| 3 | Russia | 3.13% | — | [S1] |
| 4 | Thailand | 2.54% | — | [S1] |
| 5 | Indonesia | 1.82% | — | [S1] |
| — | Others | 33.24% | — | [S1] |

> ⚠️ Ukraine/Russia/Thailand/Indonesia share likely reflects image-search/scraper traffic, not buyers. **[INFERENCE — not confirmed]**

**istockphoto.com (Getty subsidiary — the self-serve e-commerce volume center)** — ~60.9M visits/mo (Feb 2026)

| Rank | Country | Source |
|------|---------|--------|
| 1 | United States | [S2] |
| 2 | India | [S2] |
| 3 | Brazil | [S2] |
| 4 | Germany | [S2] |
| 5 | France | [S2] |

**Flags:** iStock carries the buyer volume and is far more globally distributed (India, Brazil, Germany, France in top 5) than gettyimages.com. LATAM (Brazil) + APAC (India) presence on the high-volume property = strong local-APM / acquirer-routing relevance. Getty operates many ccTLDs (.co.uk, .de, .fr, .ca, .com.mx, .com.br) with geo-redirect logic. No reliable per-ccTLD SimilarWeb breakdown was public.

---

## SECTION 2 — Legal Entities

Parent: **Getty Images Holdings, Inc.** (NYSE: GETY; SEC CIK 0001898496). Getty publishes per-country **Licensing Entities** — the entities that actually contract and bill customers (most operationally relevant). 30+ entities; selected:

| Country | In Top Traffic? | Local Entity? | Cross-Border Risk? | Source |
|---------|----------------|---------------|--------------------|--------|
| United States | ✅ (both) | ✅ Getty Images (US), Inc. | No | [S3] |
| United Kingdom | ✅ | ✅ Getty Images (UK) Limited | No | [S3][S4] |
| Germany | ✅ (iStock) | ✅ Getty Images Deutschland GmbH | No | [S3] |
| France | ✅ (iStock) | ✅ Getty Images France SAS | No | [S3] |
| Brazil | ✅ (iStock) | ✅ G&S Imagens do Brasil Ltda | No | [S3] |
| India | ✅ (iStock) | ✅ Getty Images Media India Pvt Ltd | No | [S3] |
| Mexico | ccTLD | ✅ Getty Images Mexico S de RL de CV | No | [S3] |
| Colombia | — | ✅ Getty Images Colombia SAS | No | [S3] |
| Japan | — | ✅ Getty Images Sales Japan GK | No | [S3] |
| UAE (+Gulf) | — | ✅ Getty Images Middle East FZ LLC | No | [S3] |
| Australia | — | ✅ Getty Images Sales Australia Pty Ltd | No | [S3] |
| All others | — | Getty Images International Unlimited Co. (Ireland) | varies | [S3] |

Also: Austria, Belgium, Denmark, Italy, Netherlands, Norway, Sweden, Switzerland, Spain, Portugal, NZ, Malaysia, Thailand, Hong Kong, Singapore, Turkey, Peru, Chile, Argentina, Israel.

**Takeaway:** Unusually deep multi-entity, multi-currency footprint — top traffic markets all have local entities. The complexity isn't a cross-border *gap*; it's a **per-entity/per-currency routing and reconciliation** problem, exactly where orchestration earns its keep.
> ⚠️ MANUAL: Verify current entity list on official T&Cs (geo-redirects).

---

## SECTION 3 — Payment Stack

**3A. PSPs & Acquirers**

| Country/Region | PSP / Acquirer | Evidence | Source |
|----------------|---------------|----------|--------|
| All | **Not publicly disclosed** | — | — |

Confirmed *facts* (not specific vendors):
- Getty uses **authorized third-party payment processor(s)** that store payment info. [Privacy Policy] [S5]
- Getty/its processor participates in **card-network / issuer Account Updater** services to reduce failed payments — directly relevant to recurring-billing recovery. [Privacy Policy] [S5]
- A **"Director of Payments"** role exists internally ("drive strategy for making it easy for customers to transact"). [Job Listing] [S6]
- iStock accepts **credit/debit/prepaid cards, PayPal, check/money order**, plus a **credits (pre-purchase)** system and **invoicing/net-terms** for B2B. Getty main site historically did not surface PayPal (cards + invoicing). [FAQ] [S7]

No public evidence found for Stripe, Adyen, Checkout.com, Worldpay, Braintree, or CyberSource.

**3B. Orchestrator:** **No public evidence found.** Checkout sits behind cart/sign-in, so source-level PSP fingerprinting was not possible.
> [INFERENCE — not confirmed]: 30+ entities + multi-currency + recurring subs + an internal Director of Payments make Getty a strong candidate for either a single enterprise acquirer or an orchestration layer. Unverified.
> ⚠️ MANUAL — DevTools at authenticated checkout: 4111 1111 1111 1111 | 02/30 | 123

---

## SECTION 4 — APMs (Live Verification)

**4A. Confirmed APMs**

| Market | APMs Confirmed | Verification Source | Source |
|--------|---------------|--------------------|--------|
| iStock (global) | Credit/debit/prepaid card, **PayPal**, check, money order; credits system; invoice/net-terms | iStock FAQ + third-party | [S7] |
| iStock | **Apple Pay / Google Pay NOT supported** (per data ~May 2025) | whoacceptsit | [S7] |
| Getty (US) | Card on file + invoice/net-terms accounts confirmed | Account FAQ | [S8] |

**4B. Unverified Markets**

| Market | Verified? | Reason | Popular Local APMs (context) |
|--------|-----------|--------|------------------------------|
| US / UK / DE / FR / BR checkout | ⚠️ Partial | Methods are JS-injected at authenticated checkout; WebFetch egress geo-routed to Colombia (COL$ prices), so displayed surface unreliable | DE: SEPA/Sofort; BR: Pix/boleto/installments; FR: Cartes Bancaires |

> "Not verified" ≠ "not available." **MANUAL: VPN checkout walk-through (US/UK/DE) before any APM claims in outreach.** Do not assert Getty lacks any method.

---

## SECTION 5 — Payment Complaints 🔴 (strongest signal — regulator-validated)

| Issue Type | Platform | Frequency | Date Range | Source |
|-----------|----------|-----------|------------|--------|
| Misleading iStock cancellation charge (50% of remaining annual) | **ACCC (regulator)** | ~AUD $78K refunded to 200+ customers | Nov 2023–Feb 2024 | [S9] |
| Billing issues | BBB (Seattle) | 74 complaints | last 3 yrs | [S10] |
| Product issues | BBB | 108 complaints | last 3 yrs | [S10] |
| Total complaints (not BBB-accredited) | BBB | 313 (38 in last 12 mo) | rolling | [S10] |
| "Monthly" plan → locked annual contract | BBB / Trustpilot | recurring theme | through 02/2026 | [S10] |
| No self-serve cancellation; cancel fees $70–96; auto-renew-off still charges | BBB / Trustpilot | recurring | through 2026 | [S10] |
| Refund denials on "nonrefundable" fees | Trustpilot | recurring | recent | [S11] |

> Reddit `site:` query returned no links (operator limitation, not confirmed absence).

**Analysis → Yuno:** The complaint cluster is overwhelmingly **involuntary/auto-renewal billing + cancellation friction + refund disputes**. Yuno's **subscription billing recovery, smart retries/dunning, and Account Updater orchestration** reduce failed-payment churn and the dispute volume that's already cost Getty a regulatory settlement and reputational damage.

---

## SECTION 6 — Expansion & Corporate Developments

| # | Date | Development | Category | Source |
|---|------|-------------|----------|--------|
| 1 | Jan 6/7 2025 | **Getty + Shutterstock "merger of equals"** (~$3.7B; Getty 54.7% / SSTK 45.3%); $150–200M synergy target by yr 3 | M&A | [S12][S13] |
| 2 | Jun 10 2025 | Shutterstock stockholders approve (~82%) | M&A | [S13] |
| 3 | Oct 2025 | UK CMA signals intent to refer to **Phase 2** review | Regulatory | [S14] |
| 4 | Feb 23 2026 | **DOJ unconditional antitrust clearance** | Regulatory | [S15] |
| 5 | Feb 19 2026 | CMA interim report flags UK editorial concern; final deadline **Jun 14 2026** | Regulatory | [S15] |
| 6 | — | Former Getty CFO Rik Powell → Shutterstock CFO; current Getty CFO **Jennifer Leyden** | Leadership | [S16] |

Merger **not yet closed**; expected to close 2026. Combined entity keeps name Getty Images Holdings (Mark Getty Chairman, Craig Peters CEO).

---

## SECTION 7 — Payment News

| # | Date | Headline | Relevance | Source |
|---|------|----------|-----------|--------|
| 1 | Jan 2025–2026 | Getty + Shutterstock merger consolidating Getty/iStock/Unsplash/Pond5/Envato billing | 🟡 Triggers payment-stack consolidation; synergy targets include systems rationalization [INFERENCE] | [S12] |
| 2 | Mar 16 2026 | FY2025 record revenue $981.3M; guides 2026 lower | Context | [S17] |
| 3 | — | No PSP partnership / fintech billing deal found | 🟡 No orchestrator publicly named | — |

---

## SECTION 8 — Checkout Audit

| Dimension | Finding | Notes |
|-----------|---------|-------|
| Checkout type | Subscriptions + credits (PAYG packs) + single-file | iStock 3-path model; credits never expire if you sign in yearly |
| Guest checkout | Mostly sign-in-gated; true guest limited to single-file | [INFERENCE — not confirmed] |
| Steps to purchase | Cart → sign-in → payment (methods JS-injected at final step) | Source-level PSP not visible pre-auth |
| 3DS | Not verified | — |
| Mobile experience | Not verified | — |
| APM display logic | Not verified (no geo-APM data found) | — |
| UX issues | Monthly price prominent, annual commitment obscured; annual↔monthly toggle reportedly disappears on scroll; no online cancel | Drives the complaint cluster in §5 |

> ⚠️ MANUAL: Walk checkout in US + DE + BR.

---

## SECTION 9 — PCI DSS

| PCI Level | Card data handling | Recommended Yuno integration | Source |
|-----------|-------------------|------------------------------|--------|
| No public cert/trust page found | Cardholder data handled by authorized third-party processors per contract (scope largely outsourced) | Yuno vaulting + tokenization keeps PCI scope minimal while unifying multi-entity processing | [S5] |

No standalone security/trust page enumerating PCI DSS / SOC 2 located. **No public PCI statement found.**

---

## SECTION 10 — Strategic Insights

**Insight #1: Subscription billing recovery is an open, regulator-flagged wound**
Evidence: §5 — ACCC settlement + 313 BBB complaints, auto-renewal/refund friction. Pain: involuntary churn, failed-payment loss, dispute/chargeback overhead, reputational + regulatory risk. Yuno: smart retries, dunning, Account Updater orchestration, 50% transaction recovery. Best case: **Livelo (+5% approval, 50% recovery)**. Angle: "Getty already participates in Account Updater and staffs a Director of Payments — the auto-renewal disputes that triggered the ACCC settlement are exactly the involuntary-churn surface Yuno's recovery logic closes."

**Insight #2: Merger = forced payment-stack consolidation**
Evidence: §6 — Getty + Shutterstock + iStock + Unsplash + Pond5 + Envato under $150–200M synergy targets. Pain: multiple billing/checkout systems across brands and 50+ geos to rationalize. Yuno: one orchestration layer, no-code PSP enablement, new markets live in weeks. Best case: **InDrive (10 LATAM markets <8 months)**. Angle: "As Getty and Shutterstock integrate, one orchestration layer lets you route every brand and currency without re-integrating each PSP."

**Insight #3: 54%+ recurring revenue concentrates risk on processing reliability**
Evidence: §1 financials — subscription is the majority of $981M. Pain: every point of approval/uplift compounds on the recurring base. Yuno: Smart Routing +7% approval uplift, real-time monitors. Best case: **Reserva (+4% approval <3 months)**. Angle: tie approval uplift directly to ARR.

**Insight #4: iStock's global self-serve base needs local APMs**
Evidence: §1 — iStock 60M visits, top-5 includes Brazil + India + Germany + France. Pain: card-only/PayPal checkout misses Pix, SEPA, local methods (unverified — do not assert absence). Yuno: 1,000+ APMs, local acquiring where cheaper. Best case: **InDrive**. Angle: market-coverage, never "you lack X."

---

## SECTION 11 — Pipeline

**11A. Direct Competitors**

| Company | Website | HQ | Size | Overlap | Source |
|---------|---------|----|----|---------|--------|
| Shutterstock | shutterstock.com | New York | Public (SSTK), merging w/ Getty | Global | [S18] |
| Adobe Stock | stock.adobe.com | San Jose | Adobe (ADBE) | Global | [S18] |
| Pond5 | pond5.com | New York | Owned by Shutterstock | Global | [S18] |
| Depositphotos | depositphotos.com | NY/Cyprus | Microstock | Global | [S18] |
| Alamy | alamy.com | Abingdon, UK | Owned by PA Media | Global | [S18] |
| Dreamstime | dreamstime.com | Brentwood, TN | ~326 employees | Global | [S18] |
| Freepik | freepik.com | Málaga, ES | ~1,500 (EQT-backed) | Global | [S18] |
| Canva | canva.com | Sydney, AU | Multi-$B valuation | Global | [S18] |

**11B. Industry Peers:** Vecteezy, Pexels, Envato (now Shutterstock), Stocksy, 123RF, Unsplash (Getty).

**11C. Adopting Orchestration:** None in this set publicly confirmed.

**11D. Scoring — Getty Images**

| Signal | Pts | Verified? |
|--------|-----|-----------|
| Operates in 3+ countries | +3 | ✅ 50+ |
| Multiple PSPs | +3 | ⚠️ Not verified (0) |
| Recent expansion (24 mo) | +2 | ✅ Merger |
| Public payment issues | +2 | ✅ ACCC/BBB |
| Funding/revenue >$10M | +2 | ✅ $981M |
| LATAM/APAC/MENA traffic | +2 | ✅ BR/IN |
| No orchestrator | +2 | ⚠️ Not confirmed either way (0) |
| Payment job postings | +1 | ✅ Director of Payments |
| Public RFP | +3 | ❌ |

**Score: 12 (verified) → 🔴 HIGH priority.** Two more points available on confirming multi-PSP / no-orchestrator.

**Top Pipeline (peers worth parallel outreach):**

| Rank | Company | Type | Key Markets | Priority | Top Signal |
|------|---------|------|-------------|----------|-----------|
| 1 | Getty Images | Direct | US/EU/LATAM/APAC | 🔴 High | Billing complaints + merger |
| 2 | Shutterstock | Peer (merging) | Global | 🔴 High | Same merger stack consolidation |
| 3 | Depositphotos | Peer | Global | 🟡 Med | Microstock subs |
| 4 | Freepik | Peer | EU/Global | 🟡 Med | PE-backed, scaling |
| 5 | Alamy | Peer | UK/Global | 🟢 Low | PA Media-owned |

Pipeline summary: Strongest vertical = **subscription-led stock-media** undergoing consolidation; Getty + Shutterstock are the same opportunity from two sides.

---

## SECTION 12 — Business Case

| Annual Revenue | Avg Transaction Value | Est. Annual Transactions | Primary Currency | Top 3 Markets |
|----------------|----------------------|--------------------------|------------------|---------------|
| **$981.3M FY2025** (Creative $556.9M / Editorial $369.6M) | Not disclosed (mix of subs + credit packs + single-file) | Not disclosed | USD (multi-currency, ~6% FX impact) | US, then iStock: India / Brazil / Germany |

> Subscription = 54.2% of revenue. Exact paying-subscriber/ARPU counts in full 10-K (not in retrieved excerpts). According to web data.

---

## SECTION 13 — Outreach (verified findings only — no unconfirmed APM claims)

```
--- LINKEDIN MESSAGE ---
Hi [Name] — congrats on the record 2025 and the Shutterstock integration ahead.

As Getty, iStock, Unsplash and the Shutterstock properties come together, you're consolidating several billing and checkout stacks across 50+ entities and currencies. That's the exact moment an orchestration layer pays for itself: one API to route every brand and market, add or swap PSPs with no code, and unify recovery logic.

Two things stood out from the outside: Getty already leans on Account Updater for recurring billing, and the iStock auto-renewal disputes (the ACCC matter) are precisely the involuntary-churn surface smart retries + dunning are built to shrink. We helped Livelo recover 50% of failed transactions and lift approvals 5%, and stood InDrive up across 10 markets in under 8 months.

Worth a 20-min look at where recovery + consolidation overlap for the combined company? I'm open Thursday 10am or Friday 2pm ET.

--- COLD EMAIL ---
Subject: Getty + Shutterstock: one billing stack, less involuntary churn

Hi [Name],

Record 2025 revenue on a 54%-subscription base means every point of approval and every recovered renewal compounds straight onto ARR — and the Shutterstock integration is about to put several billing and checkout systems under one roof.

From the outside, two signals line up: Getty already participates in card-network Account Updater for recurring billing, and the iStock auto-renewal disputes that drew the ACCC settlement are the kind of involuntary churn that smart retries and dunning are designed to reduce. Across 50+ entities and currencies, a single orchestration layer also lets you route each brand and market — and add or swap PSPs — without re-integrating anything.

Yuno is one API to 1,000+ payment methods and PSPs across 200+ countries. We recovered 50% of failed transactions and lifted approvals 5% for Livelo, and launched InDrive across 10 markets in under 8 months — with smart routing adding ~7% approval uplift.

Open to a 20-minute call to map this against the combined Getty + Shutterstock stack? Thursday 10am or Friday 2pm ET work on my side.

Best,
German
```

---

## APPENDIX — Source URLs
```
[S1]  https://www.similarweb.com/website/gettyimages.com/
[S2]  https://www.similarweb.com/website/istockphoto.com/
[S3]  https://www.gettyimages.com/licensing-entities  +  https://www.istockphoto.com/licensing-entities
[S4]  https://find-and-update.company-information.service.gov.uk/company/03728660
[S5]  https://www.gettyimages.com/company/privacy-policy
[S6]  https://jobs.lever.co/gettyimages
[S7]  https://www.istockphoto.com/faq/purchasing  +  https://www.whoacceptsit.com/companies/istock/8865/
[S8]  https://www.istockphoto.com/faq/your-account
[S9]  https://www.accc.gov.au/media-release/getty-images-to-refund-customers-for-allegedly-misleading-istock-subscription-cancellation-charge
[S10] https://www.bbb.org/us/wa/seattle/profile/stock-photos/getty-images-1296-37000916/complaints
[S11] https://www.trustpilot.com/review/www.gettyimages.com
[S12] https://investors.gettyimages.com/news-releases/news-release-details/getty-images-and-shutterstock-merge-creating-premier-visual
[S13] https://www.globenewswire.com/news-release/2025/01/07/3005175/0/en/Getty-Images-and-Shutterstock-to-Merge-Creating-a-Premier-Visual-Content-Company.html
[S14] https://investors.gettyimages.com/news-releases/news-release-details/uk-competition-and-markets-authority-refer-proposed-merger-getty
[S15] https://newsroom.gettyimages.com/en/getty-images/getty-images-shutterstock-doj
[S16] https://www.cfodive.com/news/shutterstock-promotes-former-gettyimages-cfo-earnings-acquisitions-envato/731401/
[S17] https://investors.gettyimages.com/news-releases/news-release-details/getty-images-reports-fourth-quarter-and-full-year-2025-results
[S18] https://www.mordorintelligence.com/industry-reports/stock-photography-market  +  https://photutorial.com/best-stock-photo-sites/
```
