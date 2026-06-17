# SDR Research Brief — Getty Images
### Yuno Payment Orchestrator | Intelligence Report
**Date:** March 9, 2026 | **Ticker:** NYSE: GETY | **Website:** gettyimages.com

---

## EXECUTIVE SUMMARY

Getty Images is a global visual content marketplace (~$939M revenue, NYSE: GETY) with 27 offices across 22 countries, serving customers in 200+ markets. Their payment stack relies on **Checkout.com as the sole confirmed PSP** with no orchestration layer. Per Daine Weston (SVP E-commerce), Getty has **PIX in Brazil and iDEAL in Netherlands** (not publicly documented), plus retry processes, auto account updater, and intelligent acceptance — indicating a more mature payment operation than publicly visible. However, the **single-PSP dependency**, **cross-border acquiring through Ireland for all APAC/ME markets**, and the **pending merger with Shutterstock** (combined ~$1.87B revenue, 5+ brands to consolidate) create significant orchestration opportunities — particularly around multi-PSP resilience, local acquiring in APAC, and post-merger payment infrastructure unification.

**IMPORTANT CORRECTION (Mar 10, 2026):** A previous outreach email incorrectly stated Getty had no PIX in Brazil and no iDEAL in Netherlands. Daine Weston corrected this — they DO have both. They also confirmed having retry processes, auto account updater, and intelligent acceptance. Any outreach must reflect these corrections.

---

## SECTION 1 — Website Traffic Analysis by Country

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source URL |
|------|---------|-------------------|---------------------|-------|------------|
| 1 | United States | ~61–65% | ~11.2M | Stable | [SimilarWeb](https://www.similarweb.com/website/gettyimages.com/), [6Sense](https://6sense.com/tech/content-marketplace/getty-images-market-share) |
| 2 | Germany | ~4.2–7.7% | ~770K–1.4M | Stable | [WebTechSurvey](https://webtechsurvey.com/technology/getty-images), [6Sense](https://6sense.com/tech/content-marketplace/getty-images-market-share) |
| 3 | United Kingdom | ~2.9–7.7% | ~530K–1.4M | Stable | [WebTechSurvey](https://webtechsurvey.com/technology/getty-images), [6Sense](https://6sense.com/tech/content-marketplace/getty-images-market-share) |
| 4 | Israel | ~4.5% | ~820K | Not found | [WebTechSurvey](https://webtechsurvey.com/technology/getty-images) |
| 5 | France | ~2.3% | ~420K | Not found | [WebTechSurvey](https://webtechsurvey.com/technology/getty-images) |
| 6 | Canada | ~2.2% | ~400K | Not found | [WebTechSurvey](https://webtechsurvey.com/technology/getty-images) |
| 7 | Brazil | Not found | Not found | Not found | N/A |
| 8 | India | Not found | Not found | Not found | [SimilarWeb](https://www.similarweb.com/website/gettyimages.in/) |
| 9 | Japan | Not found | Not found | Not found | N/A |
| 10 | Australia | Not found | Not found | Not found | N/A |

**Total estimated monthly visits:** ~18.3M (SimilarWeb, late 2024/early 2025)

**Competitive context (Dec 2024):** Shutterstock 68.3M | iStockphoto (Getty-owned) 47.5M | Dreamstime 19.2M | Alamy 18.6M | **gettyimages.com ~18.3M**

**Regional domains confirmed:** gettyimages.co.uk, gettyimages.de, gettyimages.fr, gettyimages.com.br, gettyimages.com.mx, gettyimages.ie, gettyimages.in, gettyimages.pt, gettyimages.co.jp, gettyimages.com.au

**Analysis:** Heavy US concentration (~61–65%). Getty has offices in Brazil, India, Japan, and Australia but exact traffic shares for these markets were not found. The LATAM presence (offices in Buenos Aires, Lima, Santiago, São Paulo, Mexico City) suggests meaningful traffic that likely processes cross-border through the Irish entity.

---

## SECTION 2 — Legal Entities & Local Presence

### Corporate Structure
- **Parent:** Getty Images Holdings, Inc. (Delaware, USA)
- **HQ:** 605 5th Ave S., Suite 400, Seattle, WA 98104

### Confirmed Entities

| Country | In Top 10 Traffic? | Has Local Entity? | Cross-Border Risk? | Source URL |
|---------|-------------------|-------------------|---------------------|------------|
| United States (Delaware/Washington) | Yes (#1) | Yes ✅ | No | [OpenCorporates](https://opencorporates.com/companies/us_wa/601815818) |
| United Kingdom | Yes (#3) | Yes ✅ (Co. #03728660) | No | [Companies House](https://find-and-update.company-information.service.gov.uk/company/03728660) |
| Ireland | N/A | Yes ✅ (Co. #573347) — Payment processing hub | N/A | [SoloCheck](https://www.solocheck.ie/Irish-Company/Getty-Images-International-573347) |
| Germany | Yes (#2) | Office confirmed (Munich) | Low | [Built In](https://builtin.com/company/getty-images/offices) |
| France | Yes (#5) | Office confirmed (Paris) | Low | [Built In](https://builtin.com/company/getty-images/offices) |
| Canada | Yes (#6) | Yes ✅ (iStockphoto ULC, Alberta) | No | SEC filings |
| Israel | Yes (#4) | Office confirmed (Tel Aviv) | Not found | [Built In](https://builtin.com/company/getty-images/offices) |
| Brazil | Likely | Office confirmed (São Paulo) | ⚠️ Possible | [Built In](https://builtin.com/company/getty-images/offices) |
| India | Likely | Office confirmed (Mumbai) | ⚠️ Possible | [Built In](https://builtin.com/company/getty-images/offices) |
| Japan | Likely | Office confirmed (Tokyo) | ⚠️ Possible | [Built In](https://builtin.com/company/getty-images/offices) |
| Australia | Likely | Office confirmed (Sydney) | ⚠️ Possible | [Built In](https://builtin.com/company/getty-images/offices) |

### All 27 Confirmed Office Locations

**Americas (9+):** Seattle (HQ), Chicago, Los Angeles, McLean VA, New York, Calgary, Buenos Aires, Lima, Santiago, São Paulo, Mexico City

**EMEA (10):** London, Dublin, Amsterdam, Madrid, Milan, Munich, Oslo, Paris, Stockholm, Tel Aviv

**APAC (5):** Kuala Lumpur, Mumbai, Singapore, Sydney, Tokyo

**Key finding — Irish entity as payment hub:** For customers in New Zealand, Japan, Malaysia, India, UAE, Hong Kong, Singapore, or Thailand paying by credit card, payments are processed via a **European Acquirer** through **Getty Images International Unlimited Company** (Ireland). This confirms cross-border acquiring for APAC/ME markets.

> ⚠️ *Cross-border payment processing confirmed for APAC/ME markets. Card payments routed through Ireland-based entity via European Acquirer model.*

> ⚠️ *LATAM offices (Buenos Aires, Lima, Santiago, São Paulo, Mexico City) exist but payment processing structure for these markets is unclear — likely also routed through Ireland.*

> ⚠️ **MANUAL**: Verify on official website T&Cs per country domain.

**SEC Exhibit 21:** Full subsidiary list filed with 10-K references entities across Netherlands, France, Germany, Switzerland, Australia, New Zealand, India, Hong Kong, Japan, South Korea, Singapore, and China. Source: [SEC EDGAR](https://www.sec.gov/Archives/edgar/data/1898496/000162828024011316/exhibit21.htm)

---

## SECTION 3 — Payment Stack Mapping

### 3A. PSPs & Acquirers

| Country/Region | PSP / Acquirer | Evidence Type | Source URL |
|----------------|---------------|---------------|------------|
| Global (primary) | **Checkout.com** | [Terms of Service] — named as "authorised third-party payment processor" | [Getty Images UK Terms](https://www.gettyimages.co.uk/company/terms), [Getty Images MX Terms](https://www.gettyimages.com.mx/company/terms) |
| APAC/ME (NZ, JP, MY, IN, AE, HK, SG, TH) | **European Acquirer via Ireland** | [Terms of Service] — payments processed via Getty Images International Unlimited Company | [Getty Images UK Terms](https://www.gettyimages.co.uk/company/terms) |
| Contributor payouts | PayPal, Payoneer | [Royalties Guide] | [Getty Contributors](https://contributors.gettyimages.com/help/article/5191) |

**Evidence summary:**

| PSP/Provider | Evidence Type | Confidence |
|-------------|---------------|------------|
| **Checkout.com** | [Terms of Service] — named as "authorised third-party payment processor" | **HIGH** |
| European Acquirer (via Ireland) | [Terms of Service] — APAC/ME card payments routed through Irish entity | **HIGH** |
| PayPal (contributor payouts only) | [Royalties Guide] | HIGH |
| Payoneer (contributor payouts only) | [Royalties Guide] | HIGH |

### 3B. Payment Orchestrator

**No public evidence found of a payment orchestration platform in use.** Searches for Getty Images + Spreedly, Primer, Gr4vy, CellPoint, BR-DGE, Pagos, APEXX, Nuvei, and Airwallex returned no results.

Getty Images appears to use **Checkout.com directly** as a single PSP without an orchestration layer. This represents a **single-PSP dependency** — a core ICP signal for Yuno.

> ⚠️ **MANUAL — DevTools**: test card 4111 1111 1111 1111 | 02/30 | 123

---

## SECTION 4 — Alternative & Local Payment Methods

**Current offering:** Credit/debit cards as primary method. Per Daine Weston (SVP E-commerce), PIX is available in Brazil and iDEAL in Netherlands — though neither is publicly documented on the website or help center. No PayPal, Apple Pay, or Google Pay confirmed for customer purchases.

**Daine Weston also noted (Mar 10, 2026):** "We approach alternative payment methods strategically and approval or more accurately authorization rates aren't our KPI for them, that's table stakes. We aim to establish a clear line of sight to incremental value and in some cases it's just customers switching from one method to another with no change in behavior, no increased consumption and authorization rates that don't have any material change."

| Market | APMs Confirmed | APMs Not Found / Missing | Gap Opportunity |
|--------|---------------|--------------------------|-----------------|
| **Brazil** | PIX (confirmed by Daine Weston, not PIX Automático) | Boleto, Elo cards | 🟡 MEDIUM — PIX exists but Boleto/Elo gaps remain |
| **Mexico** | None publicly confirmed | OXXO, SPEI | 🔴 HIGH — Office in Mexico City, local domain exists |
| **Colombia** | None | PSE, Nequi, Efecty, Daviplata | 🟡 MEDIUM — No office confirmed |
| **Chile** | None | Webpay, MACH | 🟡 MEDIUM — Office in Santiago |
| **Peru** | None | PagoEfectivo, Yape | 🟡 MEDIUM — Office in Lima |
| **Argentina** | None | Rapipago, Pago Fácil, Mercado Pago | 🟡 MEDIUM — Office in Buenos Aires |
| **India** | None | UPI, Paytm, Netbanking, RuPay | 🔴 HIGH — Office in Mumbai, local domain exists |
| **SE Asia** | None | GrabPay, GoPay, GCash, OVO, TrueMoney | 🟡 MEDIUM — Offices in KL, Singapore |
| **Germany** | None publicly confirmed | Sofort/Klarna, SEPA Direct Debit | 🟡 MEDIUM — Office in Munich, local domain exists |
| **Netherlands** | iDEAL (confirmed by Daine Weston) | Bancontact | 🟢 LOW — iDEAL covered |
| **Poland** | None | BLIK | 🟢 LOW |
| **Belgium** | None | Bancontact | 🟢 LOW |
| **UK** | None | Open Banking / Pay by Bank, PayPal | 🟡 MEDIUM — Major market, office in London |
| **Sweden** | None | Swish | 🟢 LOW — Office in Stockholm |
| **Italy** | None | MyBank, Satispay | 🟢 LOW — Office in Milan |
| **Japan** | None | Konbini, PayPay, LINE Pay | 🟡 MEDIUM — Office in Tokyo, local domain exists |

> ⚠️ *PIX and iDEAL confirmed by SVP E-commerce (Mar 10, 2026) but not publicly documented — suggests APM rollout is happening but may be early/limited.*

> ⚠️ *In India, UPI accounts for 80%+ of digital transactions but is not available on Getty Images — despite having a Mumbai office and local domain.*

> ⚠️ *In Mexico, OXXO is used by millions for online payments but is not offered — despite having a Mexico City office.*

> ⚠️ *Daine's "incremental value" framework is key: she doesn't care about adding APMs for the sake of coverage — she wants proof that a new method drives NEW revenue, not just cannibalization from cards.*

> ⚠️ **MANUAL**: Use VPN to verify checkout APMs per country — confirm PIX flow in Brazil and iDEAL flow in Netherlands.

---

## SECTION 5 — Customer Payment Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|-----------|----------|-----------|------------|------------|
| Unauthorized subscription charges after free trial | Trustpilot | High (recurring theme) | 2024–2025 | [Trustpilot](https://www.trustpilot.com/review/www.gettyimages.com) |
| Refund denial / excessive cancellation fees | Trustpilot | High | 2024–2025 | [Trustpilot Page 4](https://www.trustpilot.com/review/www.gettyimages.com?page=4) |
| Deceptive pricing (annual billed as monthly) | BBB | 200+ complaints | Ongoing | [BBB](https://www.bbb.org/us/wa/seattle/profile/stock-photos/getty-images-1296-37000916/complaints) |
| Misleading cancellation charges (50% of remaining annual) | ACCC (Australia) | 200+ customers refunded (~AUD $78K) | Closed Nov 2024 | [ACCC](https://www.accc.gov.au/media-release/getty-images-to-refund-customers-for-allegedly-misleading-istock-subscription-cancellation-charge) |
| No email notifications before charges | Trustpilot, BBB | Moderate | 2024–2025 | [BBB](https://www.bbb.org/us/wa/seattle/profile/stock-photos/getty-images-1296-37000916/customer-reviews) |
| Website malfunction during cancellation | Trustpilot | Low–Moderate | 2025 | [Trustpilot](https://www.trustpilot.com/review/www.gettyimages.com) |

**Selected complaints:**
- *"They started a subscription I didn't even know about"* — Susanna Alm, July 2025 (Trustpilot)
- *"Charged $70 after free trial ended... customer service refused refund"* — Justin, June 2025 (Trustpilot)
- *"Lost EUR 230 without service use... refuse any refund... administrative fees of up to 500 euros to cancel"* — Charlotte, January 2025 (Trustpilot)
- *"Paid $325+ for image, received incomplete product"* — Sharla Knox, November 2025 (Trustpilot)

**Additional detail (Agent B, Mar 9 2026):**
- Multiple users report "$70/mo" displayed at checkout but it is actually an annual commitment (12 x $70 = $840)
- Users report early termination fees of $350–$425 to exit contracts
- One user double-charged $499 for a single image; took a month+ and credit card dispute to resolve
- ACCC (Australia): Getty refunded ~AUD $78,000 to 200+ customers (Nov 2023 – Feb 2024). Issue: cancellation charge was 50% of remaining annual subscription. Getty agreed to amend pricing disclosures and add trial-end notifications.
- BBB: 200+ complaints on file

**Yuno relevance:** The complaint pattern is primarily billing/subscription practices (not payment processing failures), BUT it reveals a rigid payment infrastructure with no self-service cancellation flow. With subscriptions at 58.4% of revenue, improved dunning, pre-expiry notifications, and smarter retry logic could reduce involuntary churn. Daine confirmed they have retry and account updater, so the angle is multi-PSP retry cascading (recovers transactions that fail on primary PSP by routing to a second acquirer).

---

## SECTION 6 — Expansion Plans & Corporate Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | Jan 7, 2025 | Getty Images and Shutterstock announce merger (enterprise value ~$3.7B) | M&A | [Getty Newsroom](https://investors.gettyimages.com/news-releases/news-release-details/getty-images-and-shutterstock-merge-creating-premier-visual) |
| 2 | Jun 10, 2025 | Shutterstock stockholder approval (~82% in favor) | M&A | [Getty Investors](https://investors.gettyimages.com/) |
| 3 | Nov 3, 2025 | UK CMA refers merger to Phase 2 investigation | Regulatory | [CMA Case Page](https://www.gov.uk/cma-cases/getty-images-slash-shutterstock-merger-inquiry) |
| 4 | Feb 23, 2026 | US DOJ grants unconditional antitrust clearance | Regulatory | [Getty Newsroom](https://newsroom.gettyimages.com/en/getty-images/getty-images-shutterstock-doj) |
| 4b | Feb 19, 2026 | UK CMA Phase 2 provisional findings — competition concerns re: editorial content supply in UK. Responses due Mar 12, 2026 | Regulatory | [CMA Case Page](https://www.gov.uk/cma-cases/getty-images-slash-shutterstock-merger-inquiry) |
| 5 | Apr 2026 (expected) | UK CMA Phase 2 final decision | Regulatory | [CMA Case Page](https://www.gov.uk/cma-cases/getty-images-slash-shutterstock-merger-inquiry) |
| 6 | Oct 6, 2026 (target) | Merger close date | M&A | [Getty Investors](https://investors.gettyimages.com/) |
| 7 | Jul 22, 2024 | Shutterstock completes Envato acquisition ($245M) | M&A | [Shutterstock IR](https://investor.shutterstock.com/news-releases/news-release-details/shutterstock-completes-acquisition-envato) |
| 8 | Nov 1, 2024 | Rik Powell (former Getty exec) promoted to Shutterstock CFO | Leadership | [CFO Dive](https://www.cfodive.com/news/shutterstock-promotes-former-gettyimages-cfo-earnings-acquisitions-envato/731401/) |
| 9 | Oct 2025 | Getty & iStock launch apps in Webflow Marketplace | Partnership | [Getty Newsroom](https://newsroom.gettyimages.com/en/getty-images/getty-images-and-istock-announce-new-app-integration-in-webflows-marketplace) |
| 10 | Jan 2026 | Getty Images and Perplexity multi-year image licensing partnership | Partnership | [Getty Newsroom](https://newsroom.gettyimages.com/en/getty-images/getty-images-and-perplexity-strike-multi-year-image-partnership) |

**Key Leadership (confirmed):**
- CEO: Craig Peters
- CFO: Jenn Leyden
- SVP & General Counsel: Kjelti Kellough
- VP Sales, Americas: Josh Rucci
- Shutterstock CFO (former Getty exec): Rik Powell (promoted Nov 2024)
Source: [Getty Leadership](https://www.gettyimages.com/about-us/leadership), [CFO Dive](https://www.cfodive.com/news/shutterstock-promotes-former-gettyimages-cfo-earnings-acquisitions-envato/731401/)

**Payment-related job listings:** No public job listings found mentioning payment systems, PSP evaluation, or payment engineering. Getty has 363+ open roles but none payment-specific.

**No public payment-related RFP found.**

---

## SECTION 7 — Payment-Related News

| # | Date | Headline / Summary | Relevance | Source URL |
|---|------|--------------------|-----------|------------|
| 1 | Jan 2025 | Getty-Shutterstock merger announced ($3.7B combined) | 🟢 Payment infrastructure consolidation opportunity | [TechCrunch](https://techcrunch.com/2025/01/07/getty-images-and-shutterstock-will-merge-to-form-37-billion-stock-photo-giant/) |
| 2 | Feb 2026 | DOJ clears merger unconditionally | 🟢 Removes US regulatory obstacle for integration planning | [Getty Newsroom](https://newsroom.gettyimages.com/en/getty-images/getty-images-shutterstock-doj) |
| 3 | Nov 2025 | CMA Phase 2 — concerns re: editorial content competition in UK | 🟡 Could delay integration timeline | [PYMNTS](https://www.pymnts.com/cpi-posts/getty-images-warns-uk-operations-could-shrink-if-cma-blocks-shutterstock-merger/) |
| 4 | Q2 2025 | Subscription revenue grew 3.7% YoY, now 53.5% of total | 🟡 Recurring billing optimization increasingly important | [Getty Q2 Results](https://newsroom.gettyimages.com/en/getty-images/getty-images-reports-second-quarter-2025-results) |
| 5 | Q3 2025 | Subscription revenue at 58.4% of total (up from 52.4% YoY) | 🟡 Accelerating shift to recurring payments | [Getty Q3 Results](https://investors.gettyimages.com/news-releases/news-release-details/getty-images-reports-third-quarter-2025-results) |

**No PSP partnerships, payment provider changes, or payment infrastructure news found for Getty Images in the last 12 months on Finextra, The Paypers, or PYMNTS.com.**

---

## SECTION 8 — Checkout Experience Audit

| Dimension | Finding | Quality (Good/Fair/Poor) | Notes |
|-----------|---------|--------------------------|-------|
| Checkout type | Third-party processor (Checkout.com) | Fair | Privacy policy references "authorized third-party payment processors" |
| Guest checkout | Account creation likely required | Poor | FAQ references account-based features for purchases |
| Steps to purchase | Not found | N/A | |
| 3DS implementation | Not found | N/A | Checkout.com supports 3DS natively |
| Mobile experience | Web-only (no buyer-side app) | Poor | Only a contributor app exists on iOS/Android |
| APM display logic | No APMs displayed — cards only | Poor | Zero geo-adaptation detected |
| BNPL options | None offered | Poor | No Klarna, Afterpay, or Affirm |
| Pricing transparency | Deceptive monthly/annual toggle | Poor | BBB: "$70/mo" shown but annual commitment in fine print |
| Cancellation flow | No self-service; must contact support | Poor | ACCC enforcement action in Australia |

> ⚠️ **MANUAL**: Walk through checkout in US, UK, and Brazil markets with VPN.

---

## SECTION 9 — PCI DSS Compliance

| Dimension | Finding | Source |
|-----------|---------|--------|
| PCI DSS Level | Compliant (level not specified) | [Nudge Security](https://security-profiles.nudgesecurity.com/app/gettyimages-com) |
| Card data handling | SAQ A — Payment data stored by Checkout.com, not by Getty Images directly | [Getty Terms](https://www.gettyimages.co.uk/company/terms) |
| Additional certifications | SOC 2, ISO 27001, GDPR, HIPAA, FedRAMP, CSA Star Level 1 | [Nudge Security](https://security-profiles.nudgesecurity.com/app/gettyimages-com) |
| Recommended Yuno integration | SDK (given SAQ A profile — no direct card handling) | — |

---

## SECTION 10 — Strategic Insights & Outreach Angles

**CRITICAL CONTEXT:** Daine Weston (SVP E-commerce) responded to initial outreach on Mar 10, 2026. She corrected factual errors (Getty HAS PIX and iDEAL), confirmed they have retry, auto account updater, and intelligent acceptance, and stated their KPI is "incremental value" not authorization rates. She CC'd Eric Christensen (Director of Payments). All insights below are reframed to account for this.

### Insight #1: Single-PSP Dependency — No Baseline for Incremental Value Measurement
**Evidence**: Section 3 — Checkout.com is the sole confirmed PSP. Daine's own framework is "incremental value."
**Pain Point**: With a single processor, Getty cannot A/B test routing strategies or measure what Checkout.com leaves on the table. They have no second acquirer to compare against, which means they cannot truly measure "incremental value" — the exact metric Daine says matters most.
**Yuno Value Prop**: Orchestration layer enables parallel processing paths to isolate and measure incremental lift per acquirer, per market, per card type. Data-driven routing decisions, not faith in a single provider.
**Best Success Case**: **Rappi** — real-time anomaly detection across multiple providers, 80% reduction in analyst resolution time. Resonates because it solves the visibility/measurement problem Daine cares about.
**Outreach Angle**: "You cannot measure what Checkout.com leaves on the table without a second route to test against. An orchestration layer is not about replacing your PSP — it is about giving you the data to prove what is actually incremental."

### Insight #2: Cross-Border Acquiring Through Ireland for APAC/ME — The Silent Revenue Leak
**Evidence**: Section 2 & 3 — APAC/ME card payments (India, Japan, Singapore, Thailand, UAE, HK, NZ, Malaysia) all route through Getty Images International Unlimited Company (Ireland) via European Acquirer. Daine did NOT dispute this in her response.
**Pain Point**: Cross-border acquiring typically has 3–8% lower approval rates than local acquiring. For India (where UPI dominates) and Japan (where local card networks like JCB prefer local acquirers), routing through Ireland is almost certainly suppressing approval rates. This is not about "table stakes" authorization — this is structural revenue leakage from acquiring geography.
**Yuno Value Prop**: Local acquiring in 200+ countries. Smart Routing to prefer local acquirers where available, with cross-border as fallback. The incremental value here is measurable: compare cross-border vs. local acquiring approval rates per market.
**Best Success Case**: **Reserva** — +4% approval rate in <3 months by switching to local acquiring. **InDrive** — 90% approval rates across 10 LATAM markets through local acquiring + smart routing.
**Outreach Angle**: "Your APAC/ME transactions route through Ireland via a European acquirer. That cross-border hop suppresses approval rates by 3–8% vs. local acquiring. This is not a coverage issue — it is a structural inefficiency that an orchestration layer with local acquirers would make visible and fixable."

### Insight #3: Post-Merger Payment Infrastructure Unification (5+ Brands)
**Evidence**: Section 6 — Getty + Shutterstock merger ($3.7B combined, DOJ cleared, target close Oct 2026). Combined entity: Getty Images, iStock, Unsplash, Shutterstock, Envato, Pond5. Daine did NOT dispute this angle.
**Pain Point**: 5+ brands almost certainly run different payment stacks, different PSP contracts, different reconciliation systems. Post-merger, the combined entity needs a single control plane to: (1) consolidate PSP contracts and negotiate better rates with combined volume, (2) unify reporting across brands, (3) apply consistent routing/retry logic, (4) measure — per Daine's framework — what is truly incremental across the combined portfolio.
**Yuno Value Prop**: Single API to orchestrate all PSPs across all brands. Unified dashboard for monitoring, reconciliation, and routing. Volume aggregation for MDR negotiation leverage.
**Best Success Case**: **Rappi** — zero implementation time for new providers, real-time monitoring across all processors. Resonates because the combined entity will need exactly this operational clarity across 5+ brands.
**Outreach Angle**: "Post-merger, you will have 5+ brands likely on different payment stacks. The question is not whether to consolidate — it is whether you do it proactively with an orchestration layer or reactively brand by brand. Rappi chose proactive and cut analyst resolution time by 80%."

### Insight #4: APM Strategy Gaps Beyond PIX and iDEAL
**Evidence**: Section 4 — Daine confirmed PIX (not PIX Automático) and iDEAL. But no evidence of UPI in India, OXXO/SPEI in Mexico, Konbini/PayPay in Japan, GrabPay in SE Asia, or Open Banking in UK. Getty has offices in all these markets.
**Pain Point**: Daine's "incremental value" concern is valid — some APMs do just cannibalize card volume. But in India (where UPI is 80%+ of digital payments) and Mexico (where OXXO reaches unbanked customers), these are not substitution methods — they reach entirely new customer segments who CANNOT pay with cards.
**Yuno Value Prop**: Yuno's analytics layer can isolate which APMs drive truly incremental customers vs. card cannibalization. Unified Checkout Builder deploys new methods per market without engineering overhead, and importantly, provides the data to prove Daine's "incremental value" thesis per method.
**Best Success Case**: **InDrive** — 10 LATAM markets in <8 months, activated local APMs and achieved 90% approval. Key: they measured incremental revenue per method, not just authorization rates.
**Outreach Angle**: "UPI in India and OXXO in Mexico are not substitution methods — they reach customers who cannot pay with cards. The question you are already asking (is this incremental?) is exactly what an orchestration layer can answer with data, not assumptions."

### Insight #5: Subscription Revenue at 58.4% — Dunning and Recovery Beyond Auto Account Updater
**Evidence**: Section 7 — Subscription revenue grew from 52.4% to 58.4% of total in 12 months. Daine confirmed they have retry, auto account updater, and intelligent acceptance.
**Pain Point**: Daine's team has the basics covered. But with subscriptions now >58% of revenue, the question is whether their retry logic is optimized across different decline codes, issuer behaviors, and time windows — or if it is a one-size-fits-all approach through Checkout.com. With a single PSP, retry strategies are limited to that PSP's capabilities and issuer relationships.
**Yuno Value Prop**: Multi-PSP retry cascading — if a recurring charge fails on Checkout.com, try a second acquirer with different issuer relationships. Network tokens across multiple PSPs for better card-on-file approval. Yuno's intelligent retry optimizes timing and routing per decline code.
**Best Success Case**: **Livelo** — +5% approval rate, 50% transaction recovery. Relevant because Livelo is also subscription-heavy and already had basic retry before Yuno.
**Outreach Angle**: "You have retry and account updater in place — that is solid. The next level is multi-PSP retry cascading: when Checkout.com declines a recurring charge, a second acquirer with different issuer relationships often recovers it. Livelo found 50% of their failed transactions were recoverable this way."

---

## SECTION 11 — Similar Companies & Prospecting Pipeline

### 11A. Direct Competitors

| Company | Website | HQ | Est. Size | Overlap Markets | Source URL |
|---------|---------|-----|-----------|-----------------|------------|
| Shutterstock | shutterstock.com | New York, NY | $935M rev, ~1,700 emp | Global | [Shutterstock IR](https://investor.shutterstock.com/news-releases/news-release-details/shutterstock-reports-full-year-2024-and-fourth-quarter-financial) |
| Adobe Stock | stock.adobe.com | San Jose, CA | Part of Adobe $23.8B | Global | Public knowledge |
| Alamy | alamy.com | Abingdon, UK | Est. $30–50M, ~86 emp | UK, Global | [ZoomInfo](https://www.zoominfo.com/c/alamy-ltd/1049207) |
| 123RF | 123rf.com | Chicago / Malaysia | Est. $15M, 200–500 emp | APAC, Global | [Craft.co](https://craft.co/123rf) |
| Dreamstime | dreamstime.com | Brentwood, TN | Private (small), ~326 emp | Global | Public knowledge |
| Depositphotos / Vista | depositphotos.com | New York, NY | Est. $72M, ~351 emp | Global | [Craft.co](https://craft.co/depositphotos-inc) |
| Pond5 | pond5.com | New York, NY | Est. $35–61M, ~335 emp | Global | [ZoomInfo](https://www.zoominfo.com/c/pond5/353834135) |

### 11B. Industry Peers

| Company | Website | Vertical | Key Markets | Why Similar (Payment Context) | Source URL |
|---------|---------|----------|-------------|-------------------------------|------------|
| Canva | canva.com | Design platform | Global (190+ countries) | Visual content, freemium + subscription, multi-currency | [Canva stats](https://famewall.io/statistics/canva-stats/) |
| Envato | envato.com | Digital assets | Global | Creative marketplace, subscription, now owned by Shutterstock | [Growjo](https://growjo.com/company/Envato) |
| Storyblocks | storyblocks.com | Stock media | US, Global | Subscription stock media | [Growjo](https://growjo.com/company/Storyblocks) |
| Coursera | coursera.com | EdTech | Global | Digital content licensing, B2C+B2B, global payments | Public knowledge |
| Figma | figma.com | Design SaaS | Global | Subscription, enterprise + self-serve, multi-currency | Public knowledge |
| Spotify | spotify.com | Music streaming | Global (180+ markets) | Subscription, local APMs, multi-currency | Public knowledge |
| Netflix | netflix.com | Video streaming | Global (190+ markets) | Subscription, local payment methods, multi-currency | Public knowledge |
| WordPress.com | wordpress.com | CMS platform | Global | Digital platform, global payments, multi-currency | Public knowledge |

### 11C. Companies Recently Adopting Payment Orchestration

| Company | Orchestrator / PSP Optimization | Date | Vertical | Source URL |
|---------|-------------------------------|------|----------|------------|
| Canva | Stripe Payments Intelligence Suite (Authorization Boost, Adaptive Acceptance) | Ongoing | Design platform | [Stripe - Canva](https://stripe.com/customers/canva) |

No other direct competitor or industry peer was found to have publicly adopted a payment orchestration platform (Spreedly, Primer, APEXX, Yuno, etc.).

### 11D. Prospect Scoring — Getty Images

| Signal | Points | Verified? |
|--------|--------|-----------|
| Operates in 3+ countries | +3 | ✅ (27 offices, 22 countries) |
| Uses multiple PSPs | 0 | ⚠️ Only Checkout.com confirmed |
| Recent expansion / new market (last 24 mo.) | +2 | ✅ (Shutterstock merger, Envato acquisition) |
| Publicly reported payment issues | +2 | ✅ (BBB 200+ complaints, ACCC enforcement, Trustpilot) |
| Recent funding round (>$10M) | 0 | ⚠️ Public company, no recent equity raise |
| High web traffic in LATAM / APAC / MENA | +2 | ✅ (Offices in 5 LATAM cities + India, Japan, Singapore, Australia) |
| No known orchestrator in place | +2 | ✅ (No orchestrator found) |
| Active payment-related job postings | 0 | ⚠️ None found |
| Public RFP for payment services | 0 | ⚠️ None found |
| **TOTAL** | **11** | |

**Priority: 🟡 Medium (11 points)**

*Note: Score would increase to 🔴 High Priority (14+) once post-merger integration planning begins and payment infrastructure consolidation becomes active.*

### Top 10 Prospect Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal |
|------|---------|------|-------------|-------|----------|------------|
| 1 | Getty Images + Shutterstock (combined) | Target | Global (200+ countries) | 11 → 14+ post-merger | 🟡→🔴 | Merger payment consolidation across 5+ brands |
| 2 | Canva | Industry Peer | Global (190+ countries) | Not scored | 🟡 Est. | Uses Stripe; massive global APM needs |
| 3 | Adobe Stock | Direct Competitor | Global | Not scored | 🟡 Est. | Part of Adobe; likely mature payment stack |
| 4 | Alamy | Direct Competitor | UK, Global | Not scored | 🟢 Est. | Smaller scale; UK-focused |
| 5 | Depositphotos / Vista | Direct Competitor | Global | Not scored | 🟡 Est. | Parent company Vista has global commerce needs |
| 6 | Envato | Industry Peer | Global | Not scored | 🟡 Est. | Now under Shutterstock; part of merger consolidation |
| 7 | 123RF / Inmagine | Direct Competitor | APAC, Global | Not scored | 🟡 Est. | APAC presence strong; local APM needs |
| 8 | Storyblocks | Industry Peer | US, Global | Not scored | 🟢 Est. | Smaller scale; US-focused |
| 9 | Coursera | Industry Peer | Global | Not scored | 🟡 Est. | Global digital content, B2C payments |
| 10 | Figma | Industry Peer | Global | Not scored | 🟡 Est. | SaaS subscription, global self-serve |

**Pipeline Summary**: Based on research on Getty Images, we identified 15 similar companies across stock media and digital content licensing. The combined Getty-Shutterstock entity (post-merger) is the highest-priority prospect, with the merger creating an urgent payment consolidation need across 5+ brands and ~$1.87B combined revenue. Strongest outreach vertical: **stock media / digital content licensing** in **Global markets with LATAM, APAC, and European APM gaps**.

---

## SECTION 12 — Business Case Assistant

| Metric | Value | Source / Methodology |
|--------|-------|---------------------|
| Annual Revenue (USD) | $939.3M (FY 2024); FY2025 guidance updated to $942M–$951M (+0.3%–1.2% YoY) | [Getty FY2024 Results](https://investors.gettyimages.com/news-releases/news-release-details/getty-images-reports-fourth-quarter-and-full-year-2024-results), [Getty Q3 2025](https://investors.gettyimages.com/news-releases/news-release-details/getty-images-reports-third-quarter-2025-results) |
| Shutterstock Revenue | $935.3M (FY 2024); tracking ~$1.02B for FY2025 | [Shutterstock IR](https://investor.shutterstock.com/) |
| Combined Revenue (post-merger) | ~$1.87B (2024); ~$1.97B (2025E) | Getty $939M + Shutterstock $935M (2024); Getty ~$946M + SSTK ~$1.02B (2025E) |
| Subscription Revenue Share | 58.4% (Q3 2025) | [Getty Q3 2025](https://investors.gettyimages.com/news-releases/news-release-details/getty-images-reports-third-quarter-2025-results) |
| Average Transaction Value (USD) | $200–$500 (individual); $5,000–$50,000+ (enterprise) | [ESTIMATE — not confirmed]: based on published pricing tiers |
| Pricing Range | $49 (AI packs) — $7,250 (BBC Motion Gallery) | [Photutorial](https://photutorial.com/getty-images-pricing/) |
| Est. Annual Transactions | [ESTIMATE — not confirmed]: ~2–5M (based on $939M rev ÷ $200–$500 avg) | Calculated |
| Adjusted EBITDA | $300.3M (32.0% margin, FY2024); FY2025 guidance $291M–$293M (32.8% Q3 margin) | [Getty FY2024 Results](https://investors.gettyimages.com/news-releases/news-release-details/getty-images-reports-fourth-quarter-and-full-year-2024-results) |
| Net Income | $39.5M (FY 2024); Q3 2025 $21.6M (9.0% margin); YTD 9mo 2025 net loss $115.3M (driven by FX loss $78.4M + higher interest) | Same |
| Long-term Debt | $1.336B (Q3 2025) | [Getty Q3 2025 10-Q](https://www.stocktitan.net/sec-filings/GETY/10-q-getty-images-holdings-inc-quarterly-earnings-report-8fdff2ff64bd.html) |
| Cash & Equivalents | $109.5M (Q3 2025) | Same |
| Merger-related Costs | $9.9M (Q3 2025); $38.3M (9mo YTD 2025) | Same |
| Primary Currency | USD | SEC filings |
| Top Markets by Revenue | Americas (~63%), EMEA (~30%), APAC (remainder) | [ESTIMATE -- not confirmed]: based on employee distribution |
| Stock Photography Market Size | $5.09B (2025), forecast $7.27B by 2030 | [Mordor Intelligence](https://www.mordorintelligence.com/industry-reports/stock-photography-market) |
| Getty Market Share | ~18% global | [Arizton](https://www.arizton.com/blog/stock-content-market) |
| Shutterstock Market Share | ~23% global | [Arizton](https://www.arizton.com/blog/stock-content-market) |
| Combined Post-Merger Market Share | ~41% global (dominant position) | [ESTIMATE -- not confirmed]: sum of individual shares |
| Shutterstock AI License Revenue | $104M in 2024 (monetizing archives for AI training) | [Expert Market Research](https://www.expertmarketresearch.com/blogs/top-stock-images-companies) |

---

## SECTION 13 — Outreach Messages

**CONTEXT:** Daine Weston (SVP E-commerce) and Eric Christensen (Director of Payments) are now both in the thread. Previous outreach had factual errors (PIX, iDEAL) that were corrected. All messages below avoid those sensitive topics and focus on undisputed angles.

**13A. Follow-Up Reply to Daine + Eric** — See /negative-response output for 3 variants.

**13B. LinkedIn Message to Eric Christensen (Director of Payments)**

```
--- LINKEDIN MESSAGE (Eric Christensen) ---

Hi Eric, Daine looped you into a thread with me last week. I got some of the APM details wrong in my initial outreach and that is on me.

What I did not get wrong: your APAC and Middle East card payments route through your Irish entity via a European acquirer. That cross-border acquiring structure typically suppresses approval rates by 3 to 8 points versus local acquiring, and it is measurable.

With the Shutterstock merger on track (congrats on the DOJ clearance), you will soon be running payments across Getty, iStock, Shutterstock, Envato, and Pond5, likely on different stacks. Rappi runs 11 processors through Yuno and their biggest win was not coverage, it was operational visibility: real-time anomaly detection across all providers and 80% faster analyst resolution.

Would be interested in your perspective on how the payment infrastructure consolidation is shaping up. Happy to share how other companies at your scale have approached it.

German
```

**13C. Cold Email to New Contacts at Getty**

```
--- COLD EMAIL (New contacts) ---

Subject: Getty's APAC card payments route through Ireland, that is a measurable gap

Hi [Name],

I have been mapping Getty's payment infrastructure and one structural detail stands out: APAC and Middle East card transactions process through Getty Images International Unlimited Company in Ireland via a European acquirer. That cross-border hop typically costs 3 to 8 points in approval rates versus local acquiring.

With subscriptions now 58.4% of revenue and the Shutterstock merger bringing 5+ brands under one roof, the payment stack becomes a consolidation priority. The combined entity will process nearly $2B through what are likely multiple disconnected PSP setups.

At Yuno, we give companies like Rappi, InDrive, and McDonald's a single API to orchestrate all PSPs, route intelligently across acquirers, and measure exactly where incremental value sits. InDrive went live in 10 LATAM markets in under 8 months. Rappi cut analyst resolution time by 80% with unified monitoring across 11 processors.

Would a 20 minute conversation about post-merger payment orchestration make sense?

German
```

---

## APPENDIX — All Source URLs

```
[Section 1 — Traffic]
- https://www.similarweb.com/website/gettyimages.com/
- https://www.tipranks.com/stocks/gety/website-traffic
- https://www.similarweb.com/website/gettyimages.com/competitors/
- https://webtechsurvey.com/technology/getty-images
- https://6sense.com/tech/content-marketplace/getty-images-market-share
- https://www.similarweb.com/website/gettyimages.in/

[Section 2 — Legal Entities]
- https://opencorporates.com/companies/us_wa/601815818
- https://find-and-update.company-information.service.gov.uk/company/03728660
- https://www.solocheck.ie/Irish-Company/Getty-Images-International-573347
- https://www.solocheck.ie/Irish-Company/Getty-Images-Ireland-Holdings-Limited-646889
- https://www.sec.gov/Archives/edgar/data/1898496/000162828024011316/exhibit21.htm
- https://builtin.com/company/getty-images/offices

[Section 3 — Payment Stack]
- https://www.gettyimages.co.uk/company/terms
- https://www.gettyimages.com.mx/company/terms
- https://contributors.gettyimages.com/help/article/5191
- https://gettyimages.knoji.com/questions/getty-images-paypal/
- https://www.gettyimages.com/faq/purchasing
- https://security-profiles.nudgesecurity.com/app/gettyimages-com

[Section 4 — APMs]
- https://www.whoacceptsit.com/companies/istock/8865/
- https://gettyimages.knoji.com/questions/getty-images-paypal/

[Section 5 — Complaints]
- https://www.trustpilot.com/review/www.gettyimages.com
- https://www.trustpilot.com/review/www.gettyimages.com?page=4
- https://www.bbb.org/us/wa/seattle/profile/stock-photos/getty-images-1296-37000916/complaints
- https://www.bbb.org/us/wa/seattle/profile/stock-photos/getty-images-1296-37000916/customer-reviews
- https://www.accc.gov.au/media-release/getty-images-to-refund-customers-for-allegedly-misleading-istock-subscription-cancellation-charge

[Section 6 — Expansion]
- https://investors.gettyimages.com/news-releases/news-release-details/getty-images-and-shutterstock-merge-creating-premier-visual
- https://newsroom.gettyimages.com/en/getty-images/getty-images-shutterstock-doj
- https://www.gov.uk/cma-cases/getty-images-slash-shutterstock-merger-inquiry
- https://investors.gettyimages.com/
- https://investor.shutterstock.com/news-releases/news-release-details/shutterstock-completes-acquisition-envato
- https://www.cfodive.com/news/shutterstock-promotes-former-gettyimages-cfo-earnings-acquisitions-envato/731401/
- https://newsroom.gettyimages.com/en/getty-images/getty-images-and-istock-announce-new-app-integration-in-webflows-marketplace
- https://newsroom.gettyimages.com/en/getty-images/getty-images-and-perplexity-strike-multi-year-image-partnership

[Section 7 — News]
- https://techcrunch.com/2025/01/07/getty-images-and-shutterstock-will-merge-to-form-37-billion-stock-photo-giant/
- https://www.pymnts.com/cpi-posts/getty-images-warns-uk-operations-could-shrink-if-cma-blocks-shutterstock-merger/
- https://newsroom.gettyimages.com/en/getty-images/getty-images-reports-second-quarter-2025-results

[Section 8 — Checkout]
- https://www.gettyimages.com/company/privacy-policy
- https://www.gettyimages.com/faq/purchasing
- https://www.gettyimages.com/faq/your-account

[Section 9 — PCI DSS]
- https://security-profiles.nudgesecurity.com/app/gettyimages-com

[Section 10 — no URLs required]

[Section 11 — Competitors]
- https://investor.shutterstock.com/news-releases/news-release-details/shutterstock-reports-full-year-2024-and-fourth-quarter-financial
- https://www.zoominfo.com/c/alamy-ltd/1049207
- https://craft.co/123rf
- https://craft.co/depositphotos-inc
- https://www.zoominfo.com/c/pond5/353834135
- https://famewall.io/statistics/canva-stats/
- https://growjo.com/company/Envato
- https://growjo.com/company/Storyblocks
- https://stripe.com/customers/canva

[Section 12 — Financials]
- https://investors.gettyimages.com/news-releases/news-release-details/getty-images-reports-fourth-quarter-and-full-year-2024-results
- https://investors.gettyimages.com/news-releases/news-release-details/getty-images-reports-third-quarter-2025-results
- https://photutorial.com/getty-images-pricing/
```
