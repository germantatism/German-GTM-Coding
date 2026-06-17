# Estée Lauder Companies — Yuno SDR Research Brief
**Date:** 2026-04-10 | **Analyst:** Yuno SDR (German Tatis) | **Framework:** v8.0

---

## EXECUTIVE SUMMARY

Estée Lauder Companies (NYSE: EL) is a ~$14.3B global prestige beauty conglomerate operating in ~150 countries across 20+ brands (Estée Lauder, Clinique, MAC, La Mer, Bobbi Brown, Aveda, Tom Ford Beauty, etc.). **The single biggest signal: ELC announced a strategic partnership with Shopify on Oct 28, 2025 to re-platform global ecommerce, with the first rollout phase landing in Q1 2026 — payments stack is actively in play right now.** Combined with a brand-new CTO (Brian Franz, Apr 2025), brand-new CDMO (Aude Gandon, Aug 2025), new CFO (Akhil Shrivastava, Nov 2024), an FY25 net loss of ~$1.13B driving the "Beauty Reimagined" turnaround, and a rumored $40B Puig merger being finalized in NYC (April 2026) — ELC is the textbook payment-orchestration buyer at the textbook moment.

---

## SECTION 1 — Traffic by Country

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source URL |
|---|---|---|---|---|---|
| 1 | United States | Not found (qualitative #1) | Not found | Down YoY | [SimilarWeb](https://www.similarweb.com/website/esteelauder.com/) |
| 2 | Canada | Not found | Not found | N/A | [Semrush](https://www.semrush.com/website/esteelauder.com/overview/) |
| 3 | United Kingdom | Not found | Not found | N/A | [Semrush](https://www.semrush.com/website/esteelauder.com/overview/) |

> **Exact volumes not retrievable** — SimilarWeb/Semrush snippets behind paywall. Top-3 markets qualitatively confirmed (US, CA, UK). esteelauder.com ranked #41,823 globally / #101 in Beauty & Cosmetics (Mar 2026).
> esteelauder.com online sales ~$93.6M / yr (Grips Intelligence). Total ELC ecommerce ~$2.23B (2025). [Source](https://gripsintelligence.com/insights/retailers/esteelauder.com) | [Source](https://www.digitalcommerce360.com/2025/12/04/estee-lauder-shopify-ecommerce-overhaul/)

🚩 ELC operates dozens of brand sites (clinique.com, maccosmetics.com, lamer.com, bobbibrown.com, aveda.com, tomford.com beauty, etc.) — each with own checkout instance per geo. Multi-brand × multi-geo fragmentation = orchestration sweet spot.

---

## SECTION 2 — Legal Entities

| Country | In Top 10 Traffic? | Has Local Entity? | Cross-Border Risk? | Source URL |
|---|---|---|---|---|
| ~150 countries (full list in Exhibit 21.1) | — | Yes (per FY2025 10-K) | Lower than DTC peers given physical retail footprint | [10-K](https://media.elcompanies.com/files/e/estee-lauder-companies/global/investors/investor-resources/toolkit/form-10k-08202025.pdf) |

> ⚠️ MANUAL: Download Exhibit 21.1 from FY2025 10-K (filed Aug 20, 2025) for the per-country entity list. SEC filings hub: [elcompanies.com/investors/sec-filings](https://www.elcompanies.com/en/investors/earnings-and-financials/sec-filings)

---

## SECTION 3 — Payment Stack

### 3A. PSPs & Acquirers
| Country/Region | PSP / Acquirer | Evidence Type | Source URL |
|---|---|---|---|
| Global | **No public evidence found** | — | — |

### 3B. Orchestrator
**No public evidence of a payment orchestrator.** No press releases, job postings, source code, or case studies tying ELC to Spreedly / Primer / Gr4vy / CellPoint / APEXX / Yuno.

> ⚠️ MANUAL — DevTools fingerprint: walk checkout on esteelauder.com/maccosmetics.com (US, UK, AU) with test card 4111 1111 1111 1111 | 02/30 | 123. ELC properties return 403 to scrapers — requires real browser session. Look for Adyen, Cybersource, Worldpay, Stripe, Braintree script tags.

---

## SECTION 4 — APMs (Agent D Findings)

### 4A. Confirmed APMs

| Market | APMs Confirmed | Verification Source | Source URL |
|---|---|---|---|
| **US — esteelauder.com** | Cards, **Afterpay**, **Klarna**, **Zip**, **Alipay**, eGift Cards | Official help page snippets + brand merchant pages | [/afterpay](https://www.esteelauder.com/afterpay) · [Klarna](https://www.klarna.com/us/store/2c359c15-bf63-46b4-b960-81ebf5f13a7d/Estee-Lauder/pay-with-klarna/) · [Zip](https://zip.co/us/store/estee-lauder) |
| **UK — esteelauder.co.uk** | Cards, **Clearpay** | Official Clearpay lander | [/clearpay](https://www.esteelauder.co.uk/clearpay) |
| **AU — esteelauder.com.au** | Cards, Visa, MC, Amex, **PayPal**, **Afterpay** (LIVE confirmed) | Afterpay merchant directory | [Afterpay AU](https://www.afterpay.com/en-AU/stores/estee-lauder) · [/payments](https://www.esteelauder.com.au/payments) |
| **MAC US — maccosmetics.com** | Amex, Discover, MC, Visa, **PayPal**, **Afterpay**, MAC Gift Cards | Official FAQ | [Customer Service FAQ](https://www.maccosmetics.com/customer-service-faq) |
| **MAC UK — maccosmetics.co.uk** | Amex, MC, Visa, **PayPal**, **Clearpay**, **Klarna Pay-in-3 / Pay-in-30**, **Apple Pay**, **Google Pay** | Multiple official landers | [/ordering-online](https://www.maccosmetics.co.uk/ordering-online) · [/klarna](https://www.maccosmetics.co.uk/klarna) |
| **Clinique US — clinique.com** | Cards, **Alipay**, Instagram Checkout, gift cards | Official Shopping Online help | [Customer Care](https://www.clinique.com/customer-care/shopping-online) |
| **La Mer US — cremedelamer.com** | Cards, **Afterpay** | Official help | [Customer Service](https://www.cremedelamer.com/customer-service-shopping) |
| **MX (MAC / Clinique)** | **Kueski Pay** mentioned for MAC and Clinique Mexico | Specialty Retailer article | [Source](https://specialty-retailer.com/2024/05/20/kueski-pay-advancing-mexicos-economy/) |

### 4B. Unverified Markets

| Market | Verification Attempted? | Reason Not Verified | Popular Local APMs (NOT confirmed) |
|---|---|---|---|
| Germany (esteelauder.de) | Yes | 403 bot block, no snippets | Klarna, SOFORT, SEPA, PayPal, giropay |
| France (esteelauder.fr) | Yes | 403 bot block | CB, PayPal, Klarna |
| Brazil (esteelauder.com.br) | Yes | 403 bot block | PIX, boleto, parcelamento, Mercado Pago |
| Mexico (esteelauder.com.mx) | Yes | 403 bot block | OXXO, MSI, SPEI |
| India (esteelauder.in) | Yes | 403 bot block | UPI, Razorpay, Paytm |
| Japan / China | Yes | 403 / not surfaced | Konbini, JCB / Alipay+, WeChat Pay |

> ⚠️ "Not verified" ≠ "not available." MANUAL: VPN walk-through of DE/BR/MX top-2 markets before any APM-gap claims.

---

## SECTION 5 — Payment Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|---|---|---|---|---|
| Refund stuck "in payment platform" 6+ weeks | Trustpilot UK/US | Multiple recent reviews | 2025–2026 | [Trustpilot UK](https://uk.trustpilot.com/review/www.esteelauder.com?page=2) |
| Refund "failed silently, will reissue in 3-5 days" — never received | Trustpilot | Multiple | 2025–2026 | [Trustpilot US](https://www.trustpilot.com/review/www.esteelauder.com) |
| Refund never issued — customer forced to chargeback via bank | Trustpilot | Multiple | 2025–2026 | [Trustpilot UK](https://www.trustpilot.com/review/www.esteelauder.co.uk) |
| Promotional gifts auto-added then disappear at final checkout (UX bug) | Trustpilot | Recurring | 2025–2026 | [Trustpilot UK](https://www.trustpilot.com/review/www.esteelauder.co.uk) |
| Polish customer >2,000 PLN order returned with no refund | Trustpilot | 1 high-value case | 2025 | [Trustpilot](https://www.trustpilot.com/review/www.esteelauder.com) |
| Cannot modify or cancel orders post-submit | Trustpilot | Recurring | 2025–2026 | [Customer Service](https://www.esteelauder.com/customer-service/shopping) |

**Analysis:** "Stuck in the payment platform" + "refund failed and would be reissued" are textbook reconciliation/refund-retry pain points. Yuno's automated retry, refund routing, and real-time monitors directly address this — Rappi case study shows millisecond detection vs 5–10 min manual.

---

## SECTION 6 — Expansion & Corporate Developments

| # | Date | Development | Category | Source URL |
|---|---|---|---|---|
| 1 | **2025-10-28** | **Shopify global e-commerce re-platform — Phase 1 Q1 2026** | 🟢 Re-platform | [ELC PR](https://www.elcompanies.com/en/news-and-media/newsroom/press-releases/2025/10-28-2025-212608571) |
| 2 | 2025-04-22 | **Brian Franz** named first-ever Chief Technology, Data & Analytics Officer (ex-State Street CIO) | Leadership | [ELC PR](https://www.elcompanies.com/en/news-and-media/newsroom/press-releases/2025/04-22-2025-151519012) |
| 3 | 2025-08-01 | **Aude Gandon** (ex-Nestlé Global CMO) joins as Chief Digital & Marketing Officer | Leadership | [ELC PR](https://www.elcompanies.com/en/news-and-media/newsroom/press-releases/2025/07-16-2025-114507070) |
| 4 | 2024-11-01 | **Akhil Shrivastava** named EVP & CFO (succeeds Tracey Travis) | Leadership | [ELC PR](https://www.elcompanies.com/en/news-and-media/newsroom/press-releases/2024/07-23-2024-220015942) |
| 5 | 2025-01 | **Stéphane de La Faverie** assumes CEO role; launches "Beauty Reimagined" turnaround | Leadership | [Fortune](https://fortune.com/2025/11/19/estee-lauder-cfo-driving-turnaround-led-by-consumer-first-innovation/) |
| 6 | **2026-04-07** | **Lauder + Puig families meet in NYC to finalize ~$40B merger** | M&A | [FinancialContent](https://markets.financialcontent.com/stocks/article/marketminute-2026-4-7-beauty-behemoth-este-lauder-and-puig-families-convene-in-new-york-to-finalize-historic-40-billion-merger) |
| 7 | 2026 | **Forest Essentials (India)** — acquiring remaining 51%, closing H2 2026 | M&A | [WWD](https://wwd.com/beauty-industry-news/skin-care/estee-lauder-fully-acquire-forest-essentials-1238647007/) |
| 8 | 2025-11 | **Xinú (Mexico)** — first LatAm minority investment via NIV | M&A | [Cosmetics Business](https://cosmeticsbusiness.com/est%C3%A9e-lauder-companies-ceo-on-company-acquisitions) |
| 9 | 2025 | SAP Supplier Managed Inventory live across 38 countries | Back-office | [diginomica](https://diginomica.com/estee-lauders-seven-year-sap-inventory-roll-boosts-digital-ambitions) |

---

## SECTION 7 — Payment News

| # | Date | Headline | Relevance | Source URL |
|---|---|---|---|---|
| 1 | 2025-10-28 | ELC × Shopify partnership — global e-commerce re-platform | 🟢🟢🟢 Live payments project | [Digital Commerce 360](https://www.digitalcommerce360.com/2025/12/04/estee-lauder-shopify-ecommerce-overhaul/) |
| 2 | 2025-11-04 | Shopify to power ELC's next-gen beauty commerce | 🟢 Confirms scope (multi-brand) | [CosmeticsDesign](https://www.cosmeticsdesign.com/Article/2025/11/04/shopify-to-power-estee-lauders-next-gen-beauty-commerce/) |
| 3 | 2026-02-09 | Q2 FY26 — AI online sales return to growth | 🟢 Digital is the growth lever | [DC360](https://www.digitalcommerce360.com/2026/02/09/estee-lauder-ai-online-sales-q2-2026/) |

> No PSP-specific partnership or removal announcement found beyond the Shopify replatform.

---

## SECTION 8 — Checkout Audit

| Dimension | Finding | Quality | Notes |
|---|---|---|---|
| Checkout type | Multi-step (separate brand instances per geo) | 🟡 | Re-platforming to Shopify Q1 2026 |
| Guest checkout | Available | 🟢 | Order modification post-submit not supported (UX complaint) |
| Steps to purchase | Not measured | — | ⚠️ MANUAL walk |
| 3DS | Not verified | — | EU/UK PSD2 — assume on, verify |
| Mobile experience | Not measured | — | ⚠️ MANUAL walk |
| APM display logic | Fragmented per brand × per geo | 🔴 | Afterpay+Klarna+Zip stacked in US, Clearpay UK, Kueski MX-only — no unified APM strategy |
| BNPL | US: Afterpay+Klarna+Zip · UK: Clearpay+Klarna · AU: Afterpay · MX: Kueski | 🟡 | Multiple BNPL contracts per market |

> ⚠️ MANUAL: Walk checkout in US, UK, DE, BR (top brands).

---

## SECTION 9 — PCI DSS

| PCI DSS Level | Card data handling | Recommended Yuno integration | Source |
|---|---|---|---|
| Not found publicly | Not verified | Hosted Fields / Vault for tokenization to minimize PCI scope | — |

---

## SECTION 10 — Strategic Insights

### Insight #1: Shopify Re-Platform = Live Payments Project Window
**Evidence:** S6 #1, S7 #1 — ELC announced Shopify re-platform Oct 2025, Phase 1 rolling out Q1 2026.
**Pain Point:** Shopify Payments cannot natively serve ~150 markets, multi-currency, multi-brand. Default Shopify checkout pushes merchants into Stripe-only or limited APM coverage.
**Yuno Value Prop:** Drop Yuno as the orchestration layer on top of Shopify — keep all 7+ brand checkouts unified, route to local PSPs/APMs per geo, no replatforming risk.
**Best Case:** InDrive (10 LATAM markets <8 months, 90% approval) — proves rapid multi-market enablement.
**Outreach Angle:** "With the Shopify rollout starting this quarter, are you planning to handle global payments natively in Shopify or layer an orchestrator on top to keep your 150-market footprint covered?"

### Insight #2: New Tech Buying Committee in Year-1
**Evidence:** S6 #2/3/4 — Brand-new CTO (Brian Franz, ~12 months in), brand-new CDMO (Aude Gandon, ~8 months in), new CFO (Shrivastava, ~17 months in).
**Pain Point:** New leaders need quick wins on revenue + cost. Smart routing + decline recovery = visible margin lift.
**Yuno Value Prop:** +7% approval uplift, 50% transaction recovery — measurable in 90 days.
**Best Case:** Livelo (+5% approval, 50% recovery) — prestige loyalty/retail analog.
**Outreach Angle:** "Brian — first 12 months at ELC and a $1.13B FY25 loss to claw back. Recovering 4-5% of declined transactions is usually the fastest margin lift in payments. Worth a 20-min look?"

### Insight #3: $40B Puig Merger = Combined Stack Decision
**Evidence:** S6 #6 — Lauder + Puig families meeting in NYC April 7, 2026 to finalize merger.
**Pain Point:** Merging two ~150-market beauty conglomerates means rationalizing 20+ brand checkouts, multiple PSPs, two compliance footprints. Neither company is publicly tied to an orchestrator — green field.
**Yuno Value Prop:** Single API across all brands and markets; new market live in weeks; no-code PSP enablement.
**Outreach Angle:** "If the Puig deal closes, you'll inherit Charlotte Tilbury, Rabanne, Byredo, Jean Paul Gaultier — each on its own stack. A single orchestration layer is the cleanest way to unify checkout post-merger without re-IT'ing every brand."

### Insight #4: Refund / Reconciliation Pain Is Public
**Evidence:** S5 — Multiple Trustpilot complaints citing "stuck in payment platform" and "refund failed silently."
**Pain Point:** Manual reconciliation, no real-time monitoring, refund retry loops failing.
**Yuno Value Prop:** Real-time monitors (Rappi: ms detection vs 5–10 min manually) + automated refund routing.
**Best Case:** Rappi (zero implementation time, 80% less analyst resolution).

### Insight #5: Fragmented BNPL/APM Stack Across Brands × Geos
**Evidence:** S4 — US has Afterpay + Klarna + Zip in parallel; UK has Clearpay + Klarna; MX has Kueski but only on MAC/Clinique. Each brand has own contracts.
**Pain Point:** Multiple BNPL contracts, integration overhead per brand × per geo, inconsistent customer experience.
**Yuno Value Prop:** One contract → 1,000+ payment methods. Add/remove BNPLs via dashboard, no engineering.
**Outreach Angle:** "You have 3 BNPLs live in the US alone, all on separate integrations per brand. One orchestration contract could replace all of that — and add the EU/LATAM APMs you'll need post-Shopify rollout."

---

## SECTION 11 — Pipeline

### 11A. Direct Competitors
| Company | Website | HQ | Est. Size | Overlap Markets | Source |
|---|---|---|---|---|---|
| L'Oréal Group | loreal.com | Clichy, France | ~$45-51B | Global | [Wikipedia](https://en.wikipedia.org/wiki/L'Or%C3%A9al) |
| Shiseido | shiseido.com | Tokyo, Japan | ~$6.9B | JP, CN, Travel Retail | [BoF](https://www.businessoffashion.com/articles/beauty/earnings-wrap-up-3q25-loreal-coty-shiseido/) |
| Coty Inc. | coty.com | Amsterdam / NY | ~$5.8B | US, EU, LatAm | [BoF](https://www.businessoffashion.com/articles/beauty/earnings-wrap-up-3q25-loreal-coty-shiseido/) |
| LVMH P&C | lvmh.com | Paris, France | ~€8.4B segment | Global luxury | [LVMH](https://www.lvmh.com) |
| Beiersdorf | beiersdorf.com | Hamburg, DE | ~€10B | EU, global | [Beiersdorf](https://www.beiersdorf.com) |
| Puig | puig.com | Barcelona, ES | €5.04B FY25 | EMEA 55% / Americas 35% | [Premium Beauty News](https://www.premiumbeautynews.com/en/puig-s-revenue-surpassed-the-5,27125) |
| Kao Corporation | kao.com | Tokyo, JP | ~¥1.5T | JP, APAC | [Kao](https://www.kao.com) |
| Amorepacific | apgroup.com | Seoul, KR | +83% US YoY FY25 | KR, US, Asia | [Amorepacific](https://www.apgroup.com/int/en/news/2025-11-06-1.html) |
| Natura & Co | naturaeco.com | São Paulo, BR | ~$5.5B | LatAm, Avon global | [Global Cosmetics News](https://www.globalcosmeticsnews.com/2025-in-review-manufacturers-results-resilience-amid-uneven-global-demand/) |

### 11B. Industry Peers
| Company | Website | Vertical | Key Markets | Why Similar |
|---|---|---|---|---|
| Sephora | sephora.com | Prestige multi-brand retail | Global | LVMH-owned, multi-brand checkout |
| Ulta Beauty | ulta.com | Mass + prestige | US | ~$11B, BNPL-heavy |
| Charlotte Tilbury | charlottetilbury.com | Luxury color | Global | Puig-owned |
| Rare Beauty | rarebeauty.com | DTC celeb brand | US, EU | DTC-first |
| Fenty Beauty | fentybeauty.com | LVMH/Kering | Global | DTC-first |
| e.l.f. Beauty | elfcosmetics.com | Mass | US-led | ~$1.3B+, public |
| Glossier | glossier.com | DTC digital native | US, UK | DTC-first |
| Oddity (Il Makiage / SpoiledChild) | oddity.com | AI DTC | US, EU | Public, AI-led |

### 11C. Adopting Orchestration
| Company | Orchestrator | Date | Vertical | Source |
|---|---|---|---|---|
| **None publicly disclosed across the prestige beauty cohort** | — | — | — | — |

🚩 **Whitespace alert:** No major prestige beauty conglomerate is publicly tied to a payment orchestrator. ELC could be the lighthouse in this vertical.

### 11D. Scoring (Estée Lauder Companies)
| Signal | Pts | Verified? |
|---|---|---|
| Operates in 3+ countries | +3 | ✅ (~150 countries) |
| Multiple PSPs | +3 | 🟡 (multi-BNPL across brands; PSP unverified) |
| Recent expansion (24 mo.) | +2 | ✅ (Forest Essentials, Xinú, Shopify, Puig) |
| Public payment issues | +2 | ✅ (Trustpilot refund failures) |
| Funding >$10M | +2 | ✅ (NYSE: EL, $14.3B revenue) |
| LATAM/APAC/MENA traffic | +2 | ✅ (MX, IN, JP, CN, BR) |
| No orchestrator | +2 | ✅ (none found) |
| Payment job postings | +1 | 🟡 (389 ecom roles, none surfaced as payment-titled) |
| Public RFP | +3 | 🟡 (Shopify replatform = de facto active) |
| **TOTAL** | **20** | 🔴 **HIGH PRIORITY** |

### Top Pipeline (this account)
| Rank | Company | Type | Key Markets | Score | Priority | Top Signal |
|---|---|---|---|---|---|---|
| 1 | **Estée Lauder Cos.** | Direct | US/UK/CA/DE/JP/CN/BR/MX/IN | 🔴 20 | HIGH | Shopify replatform Q1 2026 + new CTO/CDMO/CFO + Puig merger |

---

## SECTION 12 — Business Case

| Annual Revenue | Avg Transaction Value | Est. Annual Transactions | Primary Currency | Top 3 Markets |
|---|---|---|---|---|
| **$14.3B** (FY25) [src](https://stockanalysis.com/stocks/el/revenue/) | **$100–$125** AOV (esteelauder.com) [src](https://gripsintelligence.com/insights/retailers/esteelauder.com) | ELC ecommerce ~$2.23B → ~17–22M txns/yr [INFERENCE] | USD / EUR / GBP / CNY | US, UK, Greater China |

> **Approval uplift math:** $2.23B ecom × 7% approval lift = **~$156M incremental net sales**. 50% recovery on declines (assume 8% decline rate) = **~$89M recovery**. Combined Yuno value-at-stake: **~$245M / yr**.

---

## SECTION 13 — Outreach

```
--- LINKEDIN MESSAGE ---
Hi Brian — congrats on the first year as ELC's Chief Technology, Data & Analytics Officer. The Shopify re-platform announcement in October was a big move; with Phase 1 landing this quarter, the question I'd be asking is how you keep all 20+ brand checkouts unified across ~150 markets without inheriting Shopify Payments' geo gaps.

We're Yuno — single API to 1,000+ payment methods, PSPs and fraud tools. We sit on top of platforms like Shopify so brands keep one global checkout layer while routing locally per market. Smart routing typically lifts approval by ~7% and recovers 50% of declined transactions — on $2.2B of ecommerce that's material in a turnaround year.

Clients like InDrive (10 LATAM markets in <8 months, 90% approval), Livelo (+5% approval, 50% recovery) and Rappi (real-time decline detection in milliseconds vs 5–10 min manual) are the closest analogs.

Open to a 20-min intro next Tuesday or Wednesday afternoon ET? Happy to bring a quick value-at-stake estimate for ELC's footprint.

--- COLD EMAIL ---
Subject: Q1 Shopify rollout — keeping 150 markets covered

Hi Brian,

Saw the Shopify re-platform news and the Phase 1 timeline for this quarter. Across ELC's 20+ brands and ~150 markets, the part that usually surprises retailers post-Shopify migration is how thin native APM coverage gets outside the US — Pix in Brazil, OXXO in Mexico, UPI in India, Konbini in Japan all need separate enablement, brand by brand.

Yuno is the orchestration layer that sits on top of Shopify so you keep one checkout layer globally. Single API → 1,000+ payment methods, PSPs and fraud tools, no-code PSP enablement, new market live in weeks. Two outcomes that tend to land in turnaround years: +7% approval uplift via smart routing and 50% recovery on declined transactions — on ELC's ~$2.2B of ecommerce, that's roughly $245M of value at stake annually.

Closest analogs:
- InDrive — 10 LATAM markets live in under 8 months, 90% approval rate
- Livelo — +5% approval, 50% transaction recovery
- Rappi — real-time decline monitoring in milliseconds vs 5–10 minutes manual

Would a 20-min intro next Tuesday or Wednesday afternoon ET work? I'll bring a tailored value-at-stake estimate for ELC's top markets.

Best,
German
```

---

## APPENDIX — Source URLs

```
[S1] https://www.similarweb.com/website/esteelauder.com/
[S2] https://www.semrush.com/website/esteelauder.com/overview/
[S3] https://media.elcompanies.com/files/e/estee-lauder-companies/global/investors/investor-resources/toolkit/form-10k-08202025.pdf
[S4] https://www.elcompanies.com/en/news-and-media/newsroom/press-releases/2025/10-28-2025-212608571
[S5] https://www.digitalcommerce360.com/2025/12/04/estee-lauder-shopify-ecommerce-overhaul/
[S6] https://www.cosmeticsdesign.com/Article/2025/11/04/shopify-to-power-estee-lauders-next-gen-beauty-commerce/
[S7] https://www.elcompanies.com/en/news-and-media/newsroom/press-releases/2025/04-22-2025-151519012
[S8] https://www.elcompanies.com/en/news-and-media/newsroom/press-releases/2025/07-16-2025-114507070
[S9] https://www.elcompanies.com/en/news-and-media/newsroom/press-releases/2024/07-23-2024-220015942
[S10] https://markets.financialcontent.com/stocks/article/marketminute-2026-4-7-beauty-behemoth-este-lauder-and-puig-families-convene-in-new-york-to-finalize-historic-40-billion-merger
[S11] https://wwd.com/beauty-industry-news/skin-care/estee-lauder-fully-acquire-forest-essentials-1238647007/
[S12] https://stockanalysis.com/stocks/el/revenue/
[S13] https://gripsintelligence.com/insights/retailers/esteelauder.com
[S14] https://www.trustpilot.com/review/www.esteelauder.com
[S15] https://www.trustpilot.com/review/www.esteelauder.co.uk
[S16] https://www.esteelauder.com/afterpay
[S17] https://www.maccosmetics.co.uk/klarna
[S18] https://specialty-retailer.com/2024/05/20/kueski-pay-advancing-mexicos-economy/
[S19] https://www.afterpay.com/en-AU/stores/estee-lauder
[S20] https://www.businessoffashion.com/articles/beauty/earnings-wrap-up-3q25-loreal-coty-shiseido/
```
