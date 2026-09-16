# SDR Research Brief: Higgsfield AI
**Date:** 2026-09-16 | **Analyst:** Yuno Payments Intelligence | **Framework:** v8.0 (4 agents, accuracy-first)
**Supersedes:** higgsfield-ai-2026-03-27.md (kept for history; several March findings are corrected below)

---

## EXECUTIVE SUMMARY

Higgsfield AI (Higgsfield Inc., 535 Mission St, San Francisco; engineering and growth hub in Almaty, Kazakhstan) is an AI video and image generation platform that closed a $400M Series B at a $5.4B valuation on Aug 17, 2026, reporting $700M annualized revenue, 30M+ users across 238 countries and territories, and 390 of the Fortune 500 as customers [S6]. Every payment reference in its Terms of Use, privacy policy, help center, trust page, front-end code and job postings points to one processor: Stripe (Checkout, Billing, Link, Radar, Authorization Boost, Adaptive Pricing, Connect for creator payouts). No second PSP, no merchant of record and no orchestrator was found [S3][S4]. Stripe's own case study states 75% of revenue now comes from outside the US, while the 95.6% authorization rate it quotes covers only the US, Europe and Australia; SimilarWeb places India, South Korea and Brazil at positions 2 to 4 by traffic and Korean press reports Korea and Japan among the top five markets by users [S1][S5][S6]. The Yuno opportunity: sit one layer above Stripe (never replace it) to add local acquiring and local methods in India, Korea, Japan, Brazil and Spanish-speaking LatAm, provide failover at $700M scale, and take on the involuntary-churn recovery and Stripe reconciliation work that two open roles (PM Lifecycle & Retention, Head of Revenue Accounting) describe in their own words [S9].

**What changed since the March 27, 2026 brief**
- Revenue: $300M ARR (Feb 2026) to $700M annualized (Aug 2026). Valuation: $1.3B to $5.4B [S6].
- Traffic by country is now visible: India is #2 (9.15%), South Korea #3, Brazil #4, Germany #5 [S1].
- Mobile: Higgsfield's help center states it has no mobile or desktop apps. The App Store and Google Play listings cited in March were clones or have since been removed. Apple IAP and Google Play Billing should be dropped from the stack [S4].
- Two payment-adjacent roles opened (Jul 28 and Sep 1, 2026) that name Stripe reconciliation, chargebacks, dunning and payment recovery [S9].
- Help center (Aug 1, 2026) now states accepted methods explicitly: Visa, Mastercard, Amex, JCB, Apple Pay, bank payments; "PayPal and cryptocurrency are not supported" [S4].

---

## SECTION 1: Traffic by Country

Only the top five countries are exposed on the free SimilarWeb view (mirrored by Hypestat); ranks 6 to 10 are paywalled. Data month: August 2026.

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source URL |
|------|---------|-------------------|---------------------|-------|------------|
| 1 | United States | 18.24% | ~5.8M [ESTIMATE: share x 31.8M site total] | Site +2.62% MoM | https://www.similarweb.com/website/higgsfield.ai/ |
| 2 | India | 9.15% | ~2.9M [ESTIMATE] | Not shown per country | https://www.similarweb.com/website/higgsfield.ai/ |
| 3 | South Korea | 6.08% | ~1.9M [ESTIMATE] | Not shown per country | https://www.similarweb.com/website/higgsfield.ai/ |
| 4 | Brazil | 3.65% | ~1.2M [ESTIMATE] | Not shown per country | https://www.similarweb.com/website/higgsfield.ai/ |
| 5 | Germany | 3.63% | ~1.2M [ESTIMATE] | Not shown per country | https://www.similarweb.com/website/higgsfield.ai/ |
| 6 to 10 | Not visible without login | N/A | N/A | N/A | N/A |

**Site-level figures (third-party estimates, they disagree on volume):**
- SimilarWeb / Hypestat (updated ~Sep 14, 2026): 31,810,516 monthly visits; ~1.05M daily uniques; desktop 79.16% / mobile 20.84%; direct 74.19%, search 14.60%; global rank #1,228 [https://hypestat.com/info/higgsfield.ai], [https://www.similarweb.com/website/higgsfield.ai/]
- Semrush (updated Sep 12, 2026): June 2026 34.89M visits; July 2026 46.72M visits; organic search 3.86M (+13.03% MoM) [https://www.semrush.com/website/higgsfield.ai/overview/]
- Exploding Topics (July 2026): 46.7M visits, global rank 902 [https://analytics.explodingtopics.com/website/higgsfield.ai]

**Flags:**
- Markets above 5%: United States, India, South Korea.
- APAC: India and South Korea in top 3 by traffic; Korean press (Aug 25, 2026) states "Korea and Japan are among the top five markets based on Higgsfield's global user base" [https://www.venturesquare.net/1108245].
- LATAM: Brazil #4; the site ships a Spanish locale whose code targets 19 Spanish-speaking LatAm countries (AR, BO, CL, CO, CR, CU, DO, EC, GT, HN, MX, NI, PA, PE, PR, PY, SV, UY, VE) [S4, locales bundle].
- MENA: no MENA country visible in the top five.
- Top-5 countries without a local entity: India, South Korea, Brazil, Germany (see Section 2).
- No regional domains. Localized paths exist for /es, /ja, /ko (pricing pages return lang="es"/"ja"/"ko"); /de redirects to English [S4].

---

## SECTION 2: Legal Entities

| Country | In Top 10 Traffic? | Has Local Entity? | Cross-Border Risk? | Source URL |
|---------|:-:|:-:|:-:|------------|
| United States | Yes (#1) | Yes: Higgsfield Inc., 535 Mission St, 14th Floor, San Francisco, CA 94105 (contracting party in Terms of Use, updated Jul 26, 2026); Delaware registration per D&B snippet (page not fetchable) | Low | https://higgsfield.ai/terms-of-use-agreement ; https://www.dnb.com/business-directory/company-profiles.higgsfield_inc.62348e542f83f9e0dbbf609112bf86a1.html |
| India | Yes (#2) | No entity found | ⚠️ Potential cross-border operation, no local entity found | N/A |
| South Korea | Yes (#3) | No entity found (Mirae Asset Capital is a strategic investor, not an entity) | ⚠️ Potential cross-border operation, no local entity found | https://www.venturesquare.net/1108245 |
| Brazil | Yes (#4) | No entity found | ⚠️ Potential cross-border operation, no local entity found | N/A |
| Germany | Yes (#5) | No entity found. Regional GTM Director Germany role is remote; DataRep is only the GDPR representative | ⚠️ Potential cross-border operation, no local entity found | https://jobs.ashbyhq.com/higgsfieldai/7a2caafb-1b86-4cd6-8b51-93497a7a27ce ; https://higgsfield.ai/privacy-policy |
| Japan | Top 5 by users (press), traffic rank not visible | No entity found (NTT DOCOMO Ventures is a strategic investor) | ⚠️ Potential cross-border operation | https://www.venturesquare.net/1108245 |
| EU / UK | Germany in top 5 | No entity. EU/UK GDPR representative: Data Protection Representative Limited (DataRep), Rouen and London | ⚠️ Representative only, not a merchant entity | https://higgsfield.ai/privacy-policy |
| Kazakhstan | Not in visible top 5 | Office in Almaty (on-site roles); The Brand Media (Apr 7, 2026) reports 60+ of 67 staff in Almaty and a recent AIFC registration. No entity name published | N/A (engineering hub, not a sales market) | https://api.ashbyhq.com/posting-api/job-board/higgsfieldai ; https://thebrandmedia.org/en/higgsfield-ai-how-kazakhstans-first-unicorn-is-conquering-the-global-market/ |

Corporate facts: LinkedIn lists HQ San Francisco 94105, 51 to 200 employees, founded 2023, single location [https://www.linkedin.com/company/higgsfield]. CB Insights lists total raised $549.6M [https://www.cbinsights.com/company/higgsfield-agents]. No UK Companies House, Singapore or named Kazakhstan entity was found (OpenCorporates, Dealroom, D&B and Wikipedia pages returned 403/404).

> ⚠️ MANUAL: Verify on official T&Cs. Terms of Use section 9.1 names Higgsfield Inc. as the contracting party and Stripe, Inc. as "third-party service provider for payment services (e.g., card acceptance, merchant settlement, and related services)". The privacy policy references "Higgsfield Inc. and its affiliated entities" without naming them.

---

## SECTION 3: Payment Stack

### 3A. PSPs & Acquirers

| Country/Region | PSP / Acquirer | Evidence Type | Source URL |
|---------------|---------------|---------------|------------|
| Global (web) | Stripe, Inc. and affiliates: "third-party service provider for payment services (e.g., card acceptance, merchant settlement, and related services)" | [T&Cs] Terms of Use 9.1, updated Jul 26, 2026 | https://higgsfield.ai/terms-of-use-agreement |
| Global (web) | Stripe Checkout (hosted): "all payments go through Stripe Checkout only"; Stripe billing portal for subscription management; "Stripe retries automatically" on failed payments; Stripe validates VAT IDs and adds local tax at checkout | [Help Center] Aug 1, 2026 | https://higgsfield.ai/creator-hub/help-center/billing/how-does-billing-work ; https://higgsfield.ai/creator-hub/help-center/billing/what-should-i-do-if-my-payment-failed ; https://higgsfield.ai/creator-hub/help-center/billing/how-do-i-add-a-vat-or-tax-id-to-my-invoices |
| Global (web) | Stripe products in use: Payments, Elements, Link, Authorization Boost (Adaptive Acceptance, network tokens, card account updater), Billing, Radar, Checkout, Adaptive Pricing (local currency presentment across 150 countries), Connect. Selected Stripe March 2025; integrated in 3 days by one backend engineer | [Press Release] Stripe case study (undated, references Dec 2025 milestone) and Stripe newsroom Jan 20, 2026 | https://stripe.com/customers/higgsfield ; https://stripe.com/en-jp/newsroom/news/higgsfield-and-stripe |
| Global (web) | "Higgsfield processes subscription payments through Stripe"; "We do not store your full credit card information" | [T&Cs] Trust & Safety page | https://higgsfield.ai/trust |
| Creator payouts (Higgsfield Earn) | Stripe Connect: "onboard and verify creators, route payments from customers to those creators, and pay out earnings" (creators primarily in US, Europe, UK, South Korea, Japan, Canada). Trust page: "payouts are processed through our payment partner with full KYC" (partner unnamed); "10,000+ creators commissioned", "$1M+ distributed" | [Press Release] [T&Cs] | https://stripe.com/en-jp/newsroom/news/higgsfield-and-stripe ; https://higgsfield.ai/trust ; https://higgsfield.ai/earn |
| Enterprise | "Credit-based pricing on annual contracts with monthly payments"; "Centralized billing via invoice or PO" | [Help Center] Enterprise page | https://higgsfield.ai/enterprise |
| Front end (source code) | 162 JS bundles (5.8 MB) scanned on Sep 16, 2026: zero strings for js.stripe.com, checkout.stripe.com, Paddle, PayPal, Adyen, Braintree, Checkout.com, Klarna SDK, RevenueCat, Adapty or Superwall. Only Stripe references are an `invalid_stripe_payment_method` error filter and Clerk's own Stripe plumbing. Consistent with a redirect to hosted Stripe Checkout | [Source Code] | https://higgsfield.ai/pricing (bundles at assets.higgsfield.ai) |
| Mobile | No official apps: "Higgsfield has no mobile apps and no desktop app... Any downloadable app that presents itself as Higgsfield is a copy." No links to app stores anywhere on the site. Apple developer account "Higgsfield, Inc." exists but lists zero apps in US, KZ, GB, JP and KR storefronts | [Help Center] [Checkout] | https://higgsfield.ai/creator-hub/help-center/getting-started/official-higgsfield-platforms ; https://apps.apple.com/us/developer/higgsfield-inc/id1720531558 |
| Finance operations | Head of Revenue Accounting (posted Sep 1, 2026): "Own revenue-related Stripe processes, including payouts, fees, settlement timing, and reconciliation"; close covers "credit grants, consumption, breakage, unused balances, refunds, and chargebacks"; wants experience with "HubiFi, Zuora, NetSuite ARM, RevPro, Maxio" | [Job Listing] | https://jobs.ashbyhq.com/higgsfieldai/76e25734-c827-4f05-b5df-a269a67328d1 |

**Secondary PSPs:** none found. **Merchant of record:** the phrase does not appear on any Higgsfield page; Higgsfield Inc. contracts directly and collects sales tax itself, so it is its own MoR on Stripe [INFERENCE, not confirmed: no Paddle/FastSpring/Lemon Squeezy or Stripe Managed Payments reference anywhere].

### 3B. Orchestrator

**No public evidence found.** Searches for Spreedly, Primer, Gr4vy, CellPoint and APEXX returned nothing for Higgsfield, and no orchestration layer appears in the Terms of Use, privacy policy, cookie notice, help center, 162 front-end bundles, job listings or Stripe's materials. Every payment function (checkout, billing, retries, fraud, FX, tax, payouts) is attributed to Stripe [https://higgsfield.ai/terms-of-use-agreement ; https://higgsfield.ai/cookie-notice ; https://stripe.com/customers/higgsfield].

> ⚠️ MANUAL: DevTools on a live checkout: test card 4111 1111 1111 1111 | 02/30 | 123. Expect a redirect to checkout.stripe.com.

---

## SECTION 4: APMs (Agent D findings)

### 4A. Confirmed APMs

| Market | APMs Confirmed | Verification Source | Source URL |
|--------|---------------|---------------------|------------|
| Global | Credit and debit cards: Visa, Mastercard, Amex, JCB | Official help center, Aug 1, 2026 | https://higgsfield.ai/creator-hub/help-center/billing/how-does-billing-work |
| Global | Apple Pay ("available on supported devices") | Official help center | https://higgsfield.ai/creator-hub/help-center/billing/how-does-billing-work |
| Global | "Bank payments: where supported by Stripe in your region" (specific bank methods not named) | Official help center | https://higgsfield.ai/creator-hub/help-center/billing/how-does-billing-work |
| Global | 3D Secure in use ("Complete any bank verification prompt (3D Secure)") | Official help center | https://higgsfield.ai/creator-hub/help-center/billing/what-should-i-do-if-my-payment-failed |
| Global | Link by Stripe ("40%+ of transactions completed with Link") | Stripe case study | https://stripe.com/customers/higgsfield |
| Brazil | Pix | Stripe case study and newsroom | https://stripe.com/customers/higgsfield ; https://stripe.com/en-jp/newsroom/news/higgsfield-and-stripe |
| South Korea | Kakao Pay, Naver Pay, PayCo (Stripe's newsroom labels Naver Pay under Japan; the case study lists all three without country) | Stripe case study and newsroom | https://stripe.com/customers/higgsfield ; https://stripe.com/en-jp/newsroom/news/higgsfield-and-stripe |
| Chinese cardholders | WeChat Pay | Stripe case study and newsroom | https://stripe.com/customers/higgsfield |
| US / Europe | Klarna, Affirm (BNPL); "438% higher AOV with BNPL" | Stripe case study | https://stripe.com/customers/higgsfield |
| Global | Stablecoins (Stripe, Jan 2026). ⚠️ Discrepancy: help center (Aug 1, 2026) says "PayPal and cryptocurrency are not supported". Treat stablecoins as unconfirmed today | Stripe newsroom vs. help center | https://stripe.com/en-jp/newsroom/news/higgsfield-and-stripe ; https://higgsfield.ai/creator-hub/help-center/billing/how-does-billing-work |
| Global | PayPal: the merchant's own help center states "PayPal and cryptocurrency are not supported" (merchant statement, not an inference) | Official help center | https://higgsfield.ai/creator-hub/help-center/billing/how-does-billing-work |
| Global | Currency: pricing pages carry USD by default (billing-constants bundle); Stripe Adaptive Pricing presents local currencies at checkout | Source code + Stripe newsroom | https://higgsfield.ai/pricing ; https://stripe.com/en-jp/newsroom/news/higgsfield-and-stripe |

Google Pay: NOT VERIFIED (not mentioned on any Higgsfield or Stripe page fetched). This is not evidence it is unavailable.

### 4B. Unverified Markets

| Market | Verification Attempted? | Reason Not Verified | Popular Local APMs |
|--------|:-:|---------------------|-------------------|
| India (#2 traffic) | Yes | No India-specific method appears in the help center or in Stripe's published list; checkout is behind login | UPI, Paytm, PhonePe, RuPay, net banking |
| Germany (#5 traffic) | Yes | "Bank payments where supported by Stripe" is not itemized; /de locale redirects to English | SEPA Direct Debit, Klarna (Klarna is confirmed globally) |
| Japan (top 5 by users) | Yes | /ja pricing page renders no methods; Stripe newsroom attributes Naver Pay to Japan, which needs a live check | Konbini, PayPay, JCB (JCB is confirmed globally) |
| Spanish-speaking LatAm (es locale: MX, CO, AR, CL, PE and 14 others) | Yes | /es pricing page renders no methods | OXXO, SPEI, PSE, Mercado Pago, Rapipago |
| Indonesia, Turkey, Pakistan, Morocco, Africa | Partial | Complaint sources only (see Section 5); no help-center coverage | GoPay/OVO, Troy cards, JazzCash, CMI cards, M-Pesa |

> "Not verified" is not "not available." MANUAL: VPN checkout walk-through (IN, KR, JP, BR, MX, DE) before any APM claims in outreach.

---

## SECTION 5: Payment Complaints

Trustpilot: TrustScore 4.0/5 on 4,398 reviews; 62% 5-star, 19% 1-star (~835 one-star). Of ~54 one-star reviews read (all dated Sep 1 to 16, 2026), ~21 are billing, refund or renewal related [https://www.trustpilot.com/review/higgsfield.ai?stars=1]. BBB: rating F, 27 complaints closed in the last 12 months (Product Issues 18, Service 4, Billing 2, Sales/Advertising 2, Order 1); most "Product Issues" complaints read are refund or renewal disputes [https://www.bbb.org/us/ca/san-francisco/profile/artificial-intelligence/higgsfield-ai-1116-977987/complaints].

| Issue Type | Platform | Frequency | Date Range | Source URL |
|-----------|----------|-----------|-----------|------------|
| Post-purchase card re-verification locks account (Pakistan, Morocco cardholders) | Trustpilot | 2 | Sep 13, 2026 | https://www.trustpilot.com/review/higgsfield.ai?stars=1 |
| Double or inconsistent charges (Brazil, Argentina, Germany) | Trustpilot | 3 | Sep 5 to 13, 2026 | https://www.trustpilot.com/review/higgsfield.ai?stars=1&page=2 |
| Refund refused under 7-day / zero-credit / no-renewal-refund policy (NL, GB, US, TR, KR, AU) | Trustpilot + BBB | 9 + 2 | Jun 21 to Sep 8, 2026 | https://www.trustpilot.com/review/higgsfield.ai?stars=1&page=2 ; BBB link above |
| Renewal timing and trial-to-paid conversion disputes | Trustpilot + BBB | 2 + 1 | Aug 15 to Sep 14, 2026 | Same |
| Promo or discount code not applying at checkout | Trustpilot + BBB | 1 + 1 | Jun 27 to Sep 15, 2026 | Same |
| Charges continuing after account deletion / unrecognized charge | BBB + Sikayetvar | 1 + 1 | Mar 19 (year not shown) to Jun 17, 2026 | https://www.sikayetvar.com/en/higgsfield-ai-us/higgsfieldai-keeps-charging-customer-for-account-that-no-longer-exists |
| Cancellation and support response friction | BBB + Trustpilot | 1 + 1 | Jul 1 to Sep 3, 2026 | Same |
| Region-specific card declines in Africa (15 countries listed); vendor content selling a virtual card, treat as directional | EverTry blog | 1 article | May 9, 2026 (updated Aug 10, 2026) | https://evertry.co/blog/how-to-pay-for-higgsfield-ai-in-africa/ |
| Merchant's own failed-payment guidance: "Disable any VPN", "Contact your bank and ask them to authorize online or international payments", "Complete any 3D Secure verification", "Stripe retries automatically", cancellation after ~14 days | Help center | 1 official article | Current | https://higgsfield.ai/creator-hub/help-center/billing/what-should-i-do-if-my-payment-failed |
| Credit expiry and "hidden cost" perception (DE, GB, US) | Trustpilot | 3 | Sep 8 to 9, 2026 | https://www.trustpilot.com/review/higgsfield.ai?stars=1 |
| "Unlimited" tier throttling drives refund requests (US, NO, ZA, DK) | Trustpilot | 5 | Sep 1 to 8, 2026 | https://www.trustpilot.com/review/higgsfield.ai?stars=1&page=2 |

**Analysis.** The dominant pattern is policy-driven (refund rules, renewal timing, promo-to-list price jumps), not checkout failure. The payments-infrastructure signals sit in three places: (1) card-verification lockouts and declines concentrate in emerging markets (Pakistan, Morocco, Africa) while the merchant's own guidance tells customers to ask their bank to "authorize international payments", which is what cross-border acquiring looks like from the cardholder side; (2) three double-charge reports from Brazil, Argentina and Germany inside two weeks, at a company hiring a Head of Revenue Accounting to own "refunds and chargebacks"; (3) involuntary churn is handled by Stripe's automatic retries with a 14-day cure window. Yuno's real-time monitors (Rappi: millisecond detection vs. 5 to 10 minutes manually) address (2); local acquiring plus Smart Routing (+7% approval uplift) addresses (1); Yuno's retry and recovery logic addresses (3) (Livelo: 50% recovery).

---

## SECTION 6: Expansion & Corporate Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | Mar/Apr 2025 | Web platform launch; Stripe selected as billing and payments provider (March 2025) | Product / Payments | https://stripe.com/customers/higgsfield ; https://www.productgrowth.blog/p/higgsfield-growth-teardown |
| 2 | Aug 2025 | Cashflow positive at ~$50M ARR (third-party teardown) | Financial | https://www.productgrowth.blog/p/higgsfield-growth-teardown |
| 3 | Sep 9, 2025 | $50M Series A led by GFT Ventures (Menlo Ventures, BroadLight, NextEquity, AI Capital Partners, Alpha Square); 11M users in 5 months; "operations spanning U.S., Europe, and Asia" | Funding | https://www.prnewswire.com/news-releases/higgsfield-announces-50m-series-a-to-propel-click-to-video-ai-for-social-media-302550070.html |
| 4 | Oct 2025 | First sales force hired | GTM | https://www.productgrowth.blog/p/higgsfield-growth-teardown |
| 5 | Jan 15, 2026 | $80M Series A extension led by Accel; >$1.3B valuation; $200M ARR; 15M+ users; "enterprise and international expansion" named as funding priority | Funding / Expansion | https://www.prnewswire.com/news-releases/higgsfield-announces-130m-series-a-and-reports-200m-annual-run-rate-302661805.html |
| 6 | Jan 20, 2026 | Stripe newsroom: Higgsfield adopts Stripe Billing, Radar, Adaptive Pricing (150 countries) and Connect for a creator marketplace (US, EU, UK, KR, JP, CA) | Payments | https://stripe.com/en-jp/newsroom/news/higgsfield-and-stripe |
| 7 | Feb 2026 | $300M ARR (third-party) | Financial | https://www.productgrowth.blog/p/higgsfield-growth-teardown |
| 8 | Apr 22, 2026 | Growth Manager role, Almaty | Hiring | https://jobs.ashbyhq.com/higgsfieldai/82a5d241-3f4a-4835-bb6a-5ad71d79ebe7 |
| 9 | Jul 11, 2026 | Regional GTM Director France and Regional GTM Director Germany (remote) | European expansion | https://jobs.ashbyhq.com/higgsfieldai/34aca283-f7db-4e16-bb9c-b66c956e5af8 ; https://jobs.ashbyhq.com/higgsfieldai/7a2caafb-1b86-4cd6-8b51-93497a7a27ce |
| 10 | Jul 26, 2026 | Terms of Use updated (Stripe named as payment service provider; 7-day refund rule; add-on credits valid 90 days; 30-day notice for price increases) | Legal / Billing | https://higgsfield.ai/terms-of-use-agreement |
| 11 | Jul 28, 2026 | Product Manager, Lifecycle & Retention (Almaty): "rebills, dunning, involuntary churn, grace flows, save offers"; "which churn gets fixed with product and which gets fixed with payments infrastructure" | Payment-related hiring | https://jobs.ashbyhq.com/higgsfieldai/c457f78c-c25e-4692-bf23-32a8ae211ca2 |
| 12 | Aug 17, 2026 | $400M Series B at $5.4B valuation led by DST Global (Goldman Sachs Alternatives, Intel Capital, NTT DOCOMO Ventures, Mirae Asset Capital, Tribe, Smash, Fifth Wall, Valor, Liberty Global, plus existing Accel, Menlo, GFT). $700M annualized revenue; 30M+ users in 238 countries and territories; 390 of Fortune 500; use of funds includes "international go-to-market scaling" | Funding / Expansion | https://www.prnewswire.com/news-releases/higgsfield-raises-400-million-series-b-financing-at-5-4-billion-valuation-with-annualized-revenue-reaching-700-million-302852430.html ; https://techcrunch.com/2026/08/17/higgsfield-raises-400m-series-b-quadrupling-its-valuation-in-8-months-to-5-4b/ |
| 13 | Aug 18, 2026 | "Most of the company's revenue now comes from businesses" (was under one quarter in Jan 2026) | Revenue mix shift to B2B | https://www.contentgrip.com/higgsfield-ai-video-funding/ |
| 14 | Aug 25, 2026 | Korea and Japan among top five markets by users; company to expand a "dedicated Go-to-Market organization for the Asia-Pacific market" with Mirae Asset and NTT Docomo as enterprise partners | APAC expansion | https://www.venturesquare.net/1108245 |
| 15 | Sep 1, 2026 | Head of Revenue Accounting (SF): owns Stripe payouts, fees, settlement timing, reconciliation, refunds, chargebacks. Accounts Payable Manager (SF) | Payment-related hiring | https://jobs.ashbyhq.com/higgsfieldai/76e25734-c827-4f05-b5df-a269a67328d1 ; https://jobs.ashbyhq.com/higgsfieldai/b8a9f124-05a8-44d5-b630-8054b1a11266 |
| 16 | ~Sep 12, 2026 | Head of FP&A (remote); Chief Accountant (Almaty, Kazakhstan operations); Product ML Engineer, Personalization & Monetization (Almaty) | Finance / monetization hiring | https://builtin.com/company/higgsfield-ai/jobs |
| 17 | Sep 2026 | "Higgsfield For Good" (nonprofits, students; YGA partnership; STEM program in Central Asia) | Program | https://higgsfield.ai/higgsfield-for-good |

**M&A:** none found. **Leadership hires (CFO, CRO, Head of Payments):** no public announcement found. A ZoomInfo snippet names a Head of Finance and a VP Finance but the page was not readable [INFERENCE, not confirmed]. **Public RFPs:** none found.

---

## SECTION 7: Payment News

| # | Date | Headline | Relevance | Source URL |
|---|------|----------|-----------|------------|
| 1 | Jan 20, 2026 | 🟢 "Stripe powers Higgsfield's global expansion and marketplace launch": Billing, Radar, Adaptive Pricing, Connect; 95.6% auth rate across US, Europe, Australia; Link on 40%+ of transactions | Deepening single-PSP dependency; auth benchmark only for Tier 1 markets | https://stripe.com/en-jp/newsroom/news/higgsfield-and-stripe |
| 2 | Undated (Dec 2025 milestone) | Stripe case study: "$0 to $200 million run rate in processed payments per month in just 9 months"; "75% of revenue now coming from outside the US"; Shotan Jakupov (Data and Growth Lead): "Stripe is excellent for both our Tier 1 countries and global payments" | 75% non-US revenue on one US-anchored processor | https://stripe.com/customers/higgsfield |
| 3 | Jul 26, 2026 | Terms of Use rewrite names Stripe as sole payment service provider | Confirms no second PSP or MoR | https://higgsfield.ai/terms-of-use-agreement |
| 4 | Aug 1, 2026 | Help center "How does billing work" published: cards (Visa, MC, Amex, JCB), Apple Pay, bank payments; "PayPal and cryptocurrency are not supported"; tax added by Stripe at checkout | Official method list; conflicts with Stripe's stablecoin claim | https://higgsfield.ai/creator-hub/help-center/billing/how-does-billing-work |
| 5 | Aug 2026 | Plan tiers renamed twice in 2026 per third-party trackers (Basic/Pro/Ultimate/Creator, then Starter/Plus/Ultra/Business, then Basic/Pro/Max with per-seat Team and Scale) | Frequent pricing changes; verify live before quoting | https://www.usagepricing.com/blueprint/higgsfield |
| 6 | Aug 17, 2026 | $400M Series B; no payment vendor mentioned | Scale signal only | https://www.prnewswire.com/news-releases/higgsfield-raises-400-million-series-b-financing-at-5-4-billion-valuation-with-annualized-revenue-reaching-700-million-302852430.html |
| 7 | Sep 1, 2026 | Head of Revenue Accounting posting names Stripe reconciliation, refunds, chargebacks and subscription billing systems (Zuora, NetSuite ARM, Maxio) | Billing-ops build-out; potential evaluation window | https://jobs.ashbyhq.com/higgsfieldai/76e25734-c827-4f05-b5df-a269a67328d1 |

🔴 PSP removals: none found.

---

## SECTION 8: Checkout Audit

The live /pricing page is client-rendered; figures marked "observed" come from a text render on Sep 16, 2026 and match the Blotato tracker of Aug 19, 2026. Tier names may have changed (a Sep 13 Trustpilot reviewer bought a "Max" plan).

| Dimension | Finding | Quality | Notes |
|-----------|---------|---------|-------|
| Checkout type | Hosted Stripe Checkout: "choose a plan, and complete Stripe Checkout"; "all payments go through Stripe Checkout only" | Standard | Stripe case study also lists Elements, so some surfaces may be embedded [INFERENCE] [https://higgsfield.ai/creator-hub/help-center/billing/how-does-billing-work] |
| Guest checkout | NOT VERIFIED. All billing management sits under Manage Account, and pricing copy promotes "an additional discount on premium plans after signing up", so sign-up first is likely [INFERENCE] | N/A | Auth is Clerk (clerk.higgsfield.ai) |
| Steps to purchase | 3: Pricing page, choose plan, Stripe Checkout; "plan activates instantly" | Good | Monthly/Annual toggle ("Annual 30% OFF"); "There's no trial period" per help center, though Aug/Sep complaints describe a trial converting to paid [https://higgsfield.ai/creator-hub/help-center/plans/how-do-higgsfield-plans-work] |
| Plans observed | Free $0; Starter $19/mo billed annually (270 credits); Plus $47/mo annual, $59 monthly (1,200 credits); Ultra $99/mo annual, $129 monthly (3,000 credits); Enterprise via sales. Team and Scale per-seat tiers exist (prices not in help center) | N/A | Tier names NOT VERIFIED live [https://www.blotato.com/blog/higgsfield-pricing ; https://higgsfield.ai/creator-hub/help-center/business/team-and-business-higgsfield] |
| Credit packs / top-ups | Packs of 100 to 4,000 credits and adjustable 5,000 to 25,000; 90-day validity; require active subscription; Auto-Refill charges the saved payment method in $20/$40/$90/$150/$300 packs (off-session stored-credential charges) | N/A | https://higgsfield.ai/creator-hub/help-center/credits/how-credit-packs-work ; https://higgsfield.ai/creator-hub/help-center/credits/how-does-auto-refill-work |
| 3DS | In use: "Complete any bank verification prompt (3D Secure)"; failed 3DS listed as a decline cause | Standard | https://higgsfield.ai/creator-hub/help-center/billing/what-should-i-do-if-my-payment-failed |
| Mobile experience | Web only; no native apps; "new-mobile" flag and mobile web routes (/start) in code | N/A | https://higgsfield.ai/creator-hub/help-center/getting-started/official-higgsfield-platforms |
| APM display logic | Not visible pre-checkout (no payment logos on pricing page); Stripe Checkout shows methods by billing country; Adaptive Pricing localizes currency across 150 countries | Standard | https://stripe.com/en-jp/newsroom/news/higgsfield-and-stripe |
| Currency / tax | USD list prices; local tax added at checkout by billing location, "cannot be overridden" on individual plans; VAT ID only on Team/Scale/Enterprise via Stripe portal | Standard | https://higgsfield.ai/creator-hub/help-center/billing/how-do-i-add-a-vat-or-tax-id-to-my-invoices |
| Refund / cancellation | 7 days from initial purchase, zero credits used, "service fee of up to 6%"; renewals non-refundable; EU/UK 14-day withdrawal; self-serve cancel | ⚠️ Poor (drives complaints) | https://higgsfield.ai/creator-hub/help-center/refunds/how-do-i-request-a-refund |
| Localization | Locale code supports en, es, ja, ko (de gated off); /es, /ja, /ko pricing pages live; no hreflang tags | Partial | Source code (locales bundle) |

> ⚠️ MANUAL: Walk checkout in the top 3 markets (US, India, South Korea) and Brazil.

---

## SECTION 9: PCI DSS

| PCI DSS Level | Card data handling | Recommended Yuno integration | Source |
|--------------|-------------------|------------------------------|--------|
| No public PCI DSS attestation, SOC 2 report or ISO 27001 found. Enterprise page says "SOC 2-aligned controls" (aligned, not certified). Trust center (trust.higgsfield.ai) is JS-rendered and unreadable. SAQ A eligible [INFERENCE, not confirmed] given hosted Stripe Checkout | Stripe hosts checkout and stores card data: "Higgsfield staff have no access to your card details"; "We do not store your full credit card information" | Yuno Web SDK (Lite) or hosted checkout with Yuno vault and network tokens, keeping card data off Higgsfield systems and preserving SAQ A scope; Stripe stays connected as one of several routes | https://higgsfield.ai/enterprise ; https://higgsfield.ai/trust ; https://higgsfield.ai/creator-hub/help-center/billing/what-should-i-do-if-my-payment-failed ; https://higgsfield.ai/security-policy.pdf |

---

## SECTION 10: Strategic Insights

**Insight #1: One processor for $700M of annualized revenue across 238 countries**
Evidence: S3 (Terms 9.1 names Stripe alone; no orchestrator; hosted Stripe Checkout only) + S6 ($700M annualized revenue, 238 countries) + S7 (75% of revenue outside the US).
Pain Point: No failover, no routing choice, no price leverage; a Stripe incident, rule change or risk action halts 100% of web revenue. The 95.6% auth benchmark Stripe publishes covers only the US, Europe and Australia, leaving the other markets unmeasured in public.
Yuno Value Prop: Layer above Stripe, keep it as the primary route, add local acquirers and a backup processor per market through one API; Smart Routing (+7% approval uplift) and no-code PSP enablement.
Best Case: InDrive (10 LATAM markets live in under 8 months, 90% approval, 4.5% recovery).
Outreach Angle: "You scaled to $700M on one processor in 18 months. The question is not whether Stripe works, it is what happens to the 75% of revenue outside the US when a single route is the only route."

**Insight #2: Cross-border acquiring in India, Korea, Brazil and Japan without local entities**
Evidence: S1 (India 9.15%, South Korea 6.08%, Brazil 3.65%; Korea and Japan top five by users) + S2 (no entity found in any of them) + S5 (help center tells declined customers to ask their bank to "authorize online or international payments"; card re-verification lockouts from Pakistan and Morocco).
Pain Point: Issuers in those markets treat every Higgsfield charge as an international transaction: lower approvals, higher fees, FX on the cardholder side, and recurring rebills that banks block even when the first charge went through.
Yuno Value Prop: Local acquiring through Yuno's connections in India, Korea, Japan, Brazil and Mexico with no local entity required for many rails, plus local methods surfaced by market. New market live in weeks.
Best Case: Livelo (+5% approval, 50% recovery) and Reserva (+4% approval in under 3 months).
Outreach Angle: "Your own help center tells customers whose payment failed to ask their bank to allow international charges. Local processing in India, Korea and Brazil removes that step entirely."

**Insight #3: Involuntary churn is a named hiring priority, and it currently depends on Stripe's default retries**
Evidence: S6 #11 (PM Lifecycle & Retention: "dunning, involuntary churn, grace flows"; "which churn gets fixed with payments infrastructure") + S8 (Stripe retries automatically, ~14-day cure window; auto-refill charges stored credentials off-session).
Pain Point: A credit and subscription model with off-session charges (auto-refill, rebills) lives or dies on stored-credential approval rates; one processor's retry logic is the only lever today.
Yuno Value Prop: Retry orchestration across processors, network tokens and account updater across routes, real-time recovery of soft declines; the PM they are hiring gets the infrastructure the job description asks for.
Best Case: Livelo (50% of failed transactions recovered).
Outreach Angle: "Your Lifecycle PM posting says some churn gets fixed with payments infrastructure. That is the part we do: recovering rebills that a single retry schedule gives up on."

**Insight #4: Reconciliation, refunds and chargebacks are being staffed right now**
Evidence: S6 #15 (Head of Revenue Accounting, Sep 1, 2026: "Own revenue-related Stripe processes, including payouts, fees, settlement timing, and reconciliation"; close covers "refunds, and chargebacks") + S5 (three double-charge reports from BR, AR, DE in two weeks; BBB F rating, 27 complaints).
Pain Point: Duplicate charges and chargebacks at 30M-user scale are a finance and card-network exposure, and today they are detected after the fact through support tickets.
Yuno Value Prop: Real-time monitors (Rappi: millisecond anomaly detection vs. 5 to 10 minutes manually; 80% less analyst resolution time) and a single ledger of every attempt across processors. Reconciliation is roadmap, position monitors as the GA capability.
Best Case: Rappi (zero implementation time, 80% less analyst resolution).
Outreach Angle: "You are hiring someone to own Stripe settlement and chargebacks. We can give that person one view of every attempt across every route on day one."

**Insight #5: Creator payouts and an APAC go-to-market build make this a dual-sided conversation**
Evidence: S3 (Higgsfield Earn payouts via Stripe Connect; "$1M+ distributed", "10,000+ creators"; creators in US, EU, UK, KR, JP, CA) + S6 #14 (dedicated APAC GTM organization with Mirae Asset and NTT Docomo) + S6 #13 (majority of revenue now B2B, invoice/PO billing for enterprise).
Pain Point: Pay-ins, creator payouts and enterprise invoicing are three flows on one vendor; APAC enterprise expansion adds Korean and Japanese payment expectations on both sides.
Yuno Value Prop: One API for pay-in orchestration and marketplace flows (splits, recipients, transfers) across multiple processors, as already live for a US marketplace merchant (permission needed before naming it).
Outreach Angle: Secondary; raise once a first meeting is booked. "As Earn scales to Korea and Japan, payout rails and pay-in rails can be orchestrated together."

---

## SECTION 11: Pipeline

### 11A. Direct Competitors

| Company | Website | HQ | Est. Size | Overlap Markets | Source |
|---------|---------|----|-----------|----------------|--------|
| Runway | runway.com | New York, US | $315M Series E (Feb 2026) at $5.3B; ~$1.05B raised | Film/VFX, advertising, mid-market enterprise; Stripe named in ToS | https://en.wikipedia.org/wiki/Runway_(company) ; https://runway.com/terms-of-use |
| Luma AI | lumalabs.ai | Palo Alto, US | $900M Series C (Nov 2025) at $4B+, led by HUMAIN; $1.07B raised | Consumer/prosumer video; Middle East compute partnership; Stripe named in ToS | https://aifundingtracker.com/top-ai-video-generation-startups/ ; https://lumalabs.ai/legal/tos |
| Pika Labs | pika.art | Palo Alto, US | $80M Series B (Jun 2024) at ~$700M; $115M+ raised | Consumer social video | https://aifundingtracker.com/top-ai-video-generation-startups/ |
| Kling AI (Kuaishou) | klingai.com | Beijing, CN (HKEX 1024) | Kling ARR $240M (Dec 2025); 60M creators; 30,000+ enterprise partners | Global; Kuaishou apps strong in Brazil, India, Pakistan, Indonesia | https://www.prnewswire.com/news-releases/kling-ai-annualized-revenue-run-rate-hits-usd240-million-in-december-2025-302659847.html |
| Hailuo AI (MiniMax) | hailuoai.video | Shanghai, CN | HKEX IPO Jan 9, 2026; 2025 revenue $79.0M; 415 employees | China + international consumer apps | https://en.wikipedia.org/wiki/MiniMax_(company) |
| Midjourney | midjourney.com | San Francisco, US | Self-funded, profitable; V8.2 Jul 2026 | Global prosumer image and video | https://en.wikipedia.org/wiki/Midjourney |
| Krea | krea.ai | San Francisco, US | $83M raised; $47M Series B (Apr 2025) at $500M | Prosumer multi-model hub (closest product analog); Stripe named in ToS | https://techcrunch.com/2025/04/07/kreas-founders-snubbed-postgrad-grants-from-the-king-of-spain-to-build-their-ai-startup-now-its-valued-at-500m/ ; https://www.krea.ai/terms |
| Freepik (incl. Magnific) | freepik.com | Málaga, ES (EQT-owned); legal entity Freepik Company, S.L. | Acquired Magnific May 2024; Freepik Enterprise May 2025 | Global freemium creative; strong LatAm and EU | https://en.wikipedia.org/wiki/Freepik ; https://www.magnific.com/legal/terms-of-use |
| HeyGen | heygen.com | Los Angeles, US | $60M Series A (Jun 2024) at $500M; 332 employees | Mid-market avatar video | https://aifundingtracker.com/top-ai-video-generation-startups/ ; https://www.yipitdata.com/resources/heygen-vs-synthesia-vs-runway-ai-video-platforms |
| Synthesia | synthesia.io | London, UK | $200M Series E (Jan 2026) at $4B; 706 employees | Enterprise avatar video | https://aifundingtracker.com/top-ai-video-generation-startups/ |
| Mirage (ex-Captions) | captions.ai | New York, US | $75M growth round (Mar 24, 2026); $175M+ raised | Creator/social video | https://aifundingtracker.com/top-ai-video-generation-startups/ |
| Leonardo.Ai | leonardo.ai | Sydney, AU | Acquired by Canva Jul 29, 2024; 19M registered users | Global prosumer image/video (Canva billing) | https://techcrunch.com/2024/07/29/canva-acquires-leonardo-ai-to-boost-its-generative-ai-efforts |

### 11B. Industry Peers

| Company | Website | Vertical | Key Markets | Why Similar | Source |
|---------|---------|----------|-------------|-------------|--------|
| ElevenLabs | elevenlabs.io | AI voice | Global, 70+ languages; offices London, NY, Warsaw, SF; $500M Series D (Feb 2026) at $11B | Consumption + subscription AI at global scale; processor unnamed in ToS | https://en.wikipedia.org/wiki/ElevenLabs ; https://elevenlabs.io/terms-of-use |
| Suno | suno.com | AI music | Global consumer; $250M Series C (Nov 2025) at $2.45B; $200M revenue | Same consumer AI subscription model. ⚠️ Already an active Yuno deal (deep dive Sep 17, 2026); exclude from new outreach | https://techcrunch.com/2025/11/19/legally-embattled-ai-music-startup-suno-raises-at-2-45b-valuation-on-200m-revenue/ |
| Character.AI | character.ai | AI companion | Global consumer; $150M Series A (2023) at $1B; c.ai+ $9.99/mo | Consumer AI subscription, young global base | https://sacra.com/c/character-ai/ |
| Perplexity | perplexity.ai | AI search | Global; $21.21B valuation (early 2026) | Consumer AI subscription; ⚠️ already researched by Yuno (India UPI gap brief) | https://en.wikipedia.org/wiki/Perplexity_AI |
| Cursor (Anysphere) | cursor.com | AI coding | Global developer subscriptions; $2.3B Series D (Nov 2025) at $29.3B; Stripe named in ToS; Wikipedia states a SpaceX acquisition completed Aug 14, 2026 | Stripe-direct global subscription at scale | https://en.wikipedia.org/wiki/Cursor_(code_editor) ; https://cursor.com/terms-of-service |
| Lovable | lovable.dev | AI app builder | Stockholm; $400M Series C (Aug 2026) at $13.3B; ~8M users; Stripe named in ToS | Credit-based, Stripe-direct, global prosumer | https://en.wikipedia.org/wiki/Lovable_(company) ; https://lovable.dev/terms |
| Gamma | gamma.app | AI presentations | Global; ~$102M ARR (Sacra, Oct 2025); 600K+ paying subs | Prosumer AI subscription; ⚠️ Yuno deck already exists (slug gamma-ai) | https://sacra.com/c/gamma/ |

### 11C. Adopting Orchestration

| Company | Orchestrator | Date | Vertical | Source |
|---------|-------------|------|----------|--------|
| No direct competitor or peer found using a payment orchestrator (Primer, Spreedly, Gr4vy, CellPoint, APEXX). Stripe-direct is the verified pattern at Runway, Luma, Krea, Lovable and Cursor | N/A | N/A | N/A | ToS links in 11A/11B |
| MoR usage in adjacent AI apps (Paddle customers): quso.ai, Kaleido (remove.bg, unscreen), HubX, Monica AI | Paddle (MoR, not orchestration) | Various | AI SaaS / mobile-on-web | https://www.paddle.com/customers/ai-saas-business-uses-paddle-to-future-proof-growth ; https://www.paddle.com/customers/kaleido-software-launch ; https://www.paddle.com/customers/hubx-sells-mobile-apps-on-the-web-with-paddle |
| Suno | Privacy notice says providers "act as resellers of, and/or payment processors for" its services (reseller wording consistent with a MoR; provider unnamed) [INFERENCE, not confirmed] | N/A | AI music | https://suno.com/privacy |

### 11D. Scoring: Higgsfield AI (verified signals only)

| Signal | Pts | Verified? |
|--------|----:|:---------:|
| Operates in 3+ countries | +3 | ✅ 238 countries and territories; es/ja/ko locales; DataRep EU/UK rep; Almaty office [S6][S4][S2] |
| Multiple PSPs | 0 | ❌ Stripe only [S3] |
| Recent expansion (24 mo.) | +2 | ✅ Series B "international go-to-market scaling"; APAC GTM org; France/Germany GTM directors [S6] |
| Public payment issues | +2 | ✅ Trustpilot 19% 1-star, BBB F with 27 complaints, double charges, card lockouts [S5] |
| Funding >$10M | +2 | ✅ $400M Series B, Aug 17, 2026 [S6] |
| LATAM/APAC/MENA traffic | +2 | ✅ India 9.15%, South Korea 6.08%, Brazil 3.65% [S1] |
| No orchestrator | +2 | ✅ No evidence in T&Cs, code, help center or Stripe materials [S3] |
| Payment job postings | +1 | ✅ PM Lifecycle & Retention (dunning, payment recovery); Head of Revenue Accounting (Stripe reconciliation, chargebacks) [S9] |
| Public RFP | 0 | ❌ None found |
| **TOTAL** | **14** | 🔴 **High** |

**Top 10 Pipeline** (competitor/peer scores count only signals verified in this brief; unverified signals score 0, so these are floors, not estimates)

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal |
|------|---------|------|-------------|------:|:--------:|-----------|
| 1 | Higgsfield AI | Target | US, IN, KR, BR, DE, JP | 14 | 🔴 High | Stripe-only at $700M annualized revenue, 75% non-US, payment roles open |
| 2 | Kling AI (Kuaishou) | Competitor | CN, BR, IN, ID, PK | 7 (3+2+2) | 🟡 Medium | $240M ARR, emerging-market user base |
| 3 | ElevenLabs | Peer | Global, 70+ languages | 7 (3+2+2) | 🟡 Medium | $500M Series D Feb 2026, multi-office |
| 4 | Synthesia | Competitor | UK, US, enterprise global | 7 (3+2+2) | 🟡 Medium | $200M Series E Jan 2026 |
| 5 | Runway | Competitor | US, global enterprise | 6 (2+2+2) | 🟢 Low (floor) | Stripe-direct per ToS, $315M Series E |
| 6 | Luma AI | Competitor | US, Middle East | 6 (2+2+2) | 🟢 Low (floor) | Stripe-direct per ToS, HUMAIN partnership |
| 7 | Lovable | Peer | SE, global | 6 (2+2+2) | 🟢 Low (floor) | Stripe-direct per ToS, $400M Aug 2026 |
| 8 | Cursor | Peer | US, global | 6 (2+2+2) | 🟢 Low (floor) | Stripe-direct per ToS; ownership change to verify |
| 9 | Freepik | Competitor | ES, LatAm, EU | 5 (3+2) | 🟢 Low (floor) | EU seller entity, LatAm footprint |
| 10 | Hailuo (MiniMax) | Competitor | CN + international | 5 (3+2) | 🟢 Low (floor) | Jan 2026 IPO, international apps |

Excluded from new outreach: Suno (active deal), Gamma (deck exists), Perplexity (brief exists).

**Pipeline Summary:** 19 companies found (12 competitors, 7 peers), 1 high-priority (Higgsfield), 3 medium on verified floors. Strongest vertical: AI video and creative generation subscriptions, US-headquartered with APAC and LatAm consumer bases, all Stripe-direct where verifiable.

---

## SECTION 12: Business Case

| Annual Revenue | Avg Transaction Value | Est. Annual Transactions | Primary Currency | Top 3 Markets |
|---------------:|----------------------:|-------------------------:|------------------|---------------|
| $700M annualized (company-stated, Aug 17, 2026) [S6]; $300M ARR Feb 2026 and $200M Jan 2026 for trajectory | [ESTIMATE] $19 to $129 per monthly subscription charge (observed list prices), $47 to $99 per month on annual plans, $20 to $300 auto-refill packs; simple mean of monthly list prices $69 [S8] | [ESTIMATE, weak] 5M to 14M card-based transactions per year if the full $700M were consumer billing at $50 to $130 ATV; the true figure is lower because "most of the company's revenue now comes from businesses" on invoice/PO [S6 #13]. A ProductGrowth teardown cites 300K paying subscribers (Mar 2026), which at 12 rebills each implies ~3.6M subscription charges per year before top-ups [https://www.productgrowth.blog/p/higgsfield-growth-teardown] | USD list prices; Stripe Adaptive Pricing presents local currency in 150 countries [S4][S7] | United States (18.24%), India (9.15%), South Korea (6.08%) by traffic; Korea and Japan top five by users [S1][S6] |

---

## SECTION 13: Outreach (verified findings only)

Suggested targets: Alex Mashrabov (Co-Founder & CEO, quoted in Stripe materials) and Shotan Jakupov (Data and Growth Lead, quoted in the Stripe case study on Tier 1 vs. global payments). No CFO or Head of Payments has been publicly announced; the Head of Revenue Accounting role is open as of Sep 1, 2026.

```
--- LINKEDIN MESSAGE ---
Shotan, the Stripe case study quote stuck with me: excellent for Tier 1 countries and global payments. Then I looked at where Higgsfield's traffic actually comes from: India, Korea and Brazil are three of your top four markets, and 75% of revenue is now outside the US.

Two things I would want to check in your seat:

1. Approval rates outside the 95.6% you publish for the US, Europe and Australia. Your help center tells declined customers to ask their bank to allow international charges. Local processing in India, Korea and Brazil removes that step.

2. Rebill recovery. Your Lifecycle PM posting says some churn gets fixed with payments infrastructure. That is the layer we run above Stripe: routing, retries and local acquirers through one API, Stripe stays as your primary route.

Yuno does this for InDrive (10 LATAM markets live in under 8 months, 90% approval), Rappi and Livelo (+5% approval, half of failed payments recovered).

Open to a 25-minute call Tuesday Sep 22 or Thursday Sep 24 to compare approval data by market?

--- COLD EMAIL ---
Subject: Higgsfield's approval rate in India and Korea

Alex,

Higgsfield went from launch to $700M annualized revenue on a single processor, with 75% of revenue now coming from outside the US. India, South Korea and Brazil are three of your four largest markets by traffic, and none of them sits inside the 95.6% authorization figure Stripe publishes for the US, Europe and Australia.

Two signals suggest this is already costing you. Your help center tells customers with failed payments to ask their bank to authorize international charges, which is what cross-border acquiring looks like to an issuer in Mumbai or São Paulo. And the Lifecycle & Retention role you opened in July describes churn that gets fixed with payments infrastructure, not product.

Yuno is a payment orchestration platform: one API that connects your existing Stripe integration to local acquirers and 1,000+ payment methods across 200+ countries, with smart routing and retry logic that adds about 7% to approval rates. Stripe stays as your primary route; Yuno adds local processing and a backup where the math says so. New markets go live in weeks, no code per PSP.

If useful, I can walk you or Shotan through approval benchmarks for India, Korea and Brazil in 25 minutes. Would Tuesday Sep 22 or Thursday Sep 24 work?

Best regards,
German Tatis
Yuno
```

---

## APPENDIX: Source URLs

```
[S1] Traffic
https://www.similarweb.com/website/higgsfield.ai/
https://hypestat.com/info/higgsfield.ai
https://www.semrush.com/website/higgsfield.ai/overview/
https://analytics.explodingtopics.com/website/higgsfield.ai

[S2] Legal entities
https://higgsfield.ai/terms-of-use-agreement
https://higgsfield.ai/privacy-policy
https://www.dnb.com/business-directory/company-profiles.higgsfield_inc.62348e542f83f9e0dbbf609112bf86a1.html
https://www.linkedin.com/company/higgsfield
https://www.cbinsights.com/company/higgsfield-agents
https://thebrandmedia.org/en/higgsfield-ai-how-kazakhstans-first-unicorn-is-conquering-the-global-market/
https://api.ashbyhq.com/posting-api/job-board/higgsfieldai

[S3] Payment stack
https://higgsfield.ai/terms-of-use-agreement
https://higgsfield.ai/trust
https://higgsfield.ai/cookie-notice
https://higgsfield.ai/enterprise
https://stripe.com/customers/higgsfield
https://stripe.com/en-jp/newsroom/news/higgsfield-and-stripe
https://apps.apple.com/us/developer/higgsfield-inc/id1720531558

[S4] APMs / help center / checkout
https://higgsfield.ai/creator-hub/help-center/billing/how-does-billing-work
https://higgsfield.ai/creator-hub/help-center/billing/what-should-i-do-if-my-payment-failed
https://higgsfield.ai/creator-hub/help-center/billing/how-do-i-add-a-vat-or-tax-id-to-my-invoices
https://higgsfield.ai/creator-hub/help-center/billing/how-do-i-download-my-invoice-or-receipt
https://higgsfield.ai/creator-hub/help-center/refunds/how-do-i-request-a-refund
https://higgsfield.ai/creator-hub/help-center/refunds/how-do-i-cancel-my-subscription
https://higgsfield.ai/creator-hub/help-center/credits/how-credit-packs-work
https://higgsfield.ai/creator-hub/help-center/credits/how-does-auto-refill-work
https://higgsfield.ai/creator-hub/help-center/plans/how-do-higgsfield-plans-work
https://higgsfield.ai/creator-hub/help-center/business/team-and-business-higgsfield
https://higgsfield.ai/creator-hub/help-center/getting-started/official-higgsfield-platforms
https://higgsfield.ai/pricing
https://higgsfield.ai/es/pricing
https://higgsfield.ai/ja/pricing
https://higgsfield.ai/ko/pricing

[S5] Complaints
https://www.trustpilot.com/review/higgsfield.ai
https://www.trustpilot.com/review/higgsfield.ai?stars=1
https://www.trustpilot.com/review/higgsfield.ai?stars=1&page=2
https://www.bbb.org/us/ca/san-francisco/profile/artificial-intelligence/higgsfield-ai-1116-977987/complaints
https://www.sikayetvar.com/en/higgsfield-ai-us/higgsfieldai-keeps-charging-customer-for-account-that-no-longer-exists
https://evertry.co/blog/how-to-pay-for-higgsfield-ai-in-africa/

[S6] Expansion & financials
https://www.prnewswire.com/news-releases/higgsfield-raises-400-million-series-b-financing-at-5-4-billion-valuation-with-annualized-revenue-reaching-700-million-302852430.html
https://techcrunch.com/2026/08/17/higgsfield-raises-400m-series-b-quadrupling-its-valuation-in-8-months-to-5-4b/
https://www.prnewswire.com/news-releases/higgsfield-announces-130m-series-a-and-reports-200m-annual-run-rate-302661805.html
https://www.prnewswire.com/news-releases/higgsfield-announces-50m-series-a-to-propel-click-to-video-ai-for-social-media-302550070.html
https://www.contentgrip.com/higgsfield-ai-video-funding/
https://www.venturesquare.net/1108245
https://www.productgrowth.blog/p/higgsfield-growth-teardown
https://sacra.com/c/higgsfield/
https://higgsfield.ai/higgsfield-for-good
https://higgsfield.ai/earn

[S7] Payment news
https://stripe.com/en-jp/newsroom/news/higgsfield-and-stripe
https://stripe.com/customers/higgsfield
https://www.usagepricing.com/blueprint/higgsfield

[S8] Pricing
https://www.blotato.com/blog/higgsfield-pricing
https://aiforesight360.com/higgsfield-ai-pricing/

[S9] Job postings
https://jobs.ashbyhq.com/higgsfieldai/76e25734-c827-4f05-b5df-a269a67328d1
https://jobs.ashbyhq.com/higgsfieldai/c457f78c-c25e-4692-bf23-32a8ae211ca2
https://jobs.ashbyhq.com/higgsfieldai/b8a9f124-05a8-44d5-b630-8054b1a11266
https://jobs.ashbyhq.com/higgsfieldai/34aca283-f7db-4e16-bb9c-b66c956e5af8
https://jobs.ashbyhq.com/higgsfieldai/7a2caafb-1b86-4cd6-8b51-93497a7a27ce
https://builtin.com/company/higgsfield-ai/jobs

[S11] Competitors & peers
https://en.wikipedia.org/wiki/Runway_(company)
https://runway.com/terms-of-use
https://lumalabs.ai/legal/tos
https://www.krea.ai/terms
https://lovable.dev/terms
https://cursor.com/terms-of-service
https://elevenlabs.io/terms-of-use
https://aifundingtracker.com/top-ai-video-generation-startups/
https://www.yipitdata.com/resources/heygen-vs-synthesia-vs-runway-ai-video-platforms
https://www.prnewswire.com/news-releases/kling-ai-annualized-revenue-run-rate-hits-usd240-million-in-december-2025-302659847.html
https://en.wikipedia.org/wiki/MiniMax_(company)
https://en.wikipedia.org/wiki/Midjourney
https://en.wikipedia.org/wiki/Freepik
https://techcrunch.com/2024/07/29/canva-acquires-leonardo-ai-to-boost-its-generative-ai-efforts
https://sacra.com/c/character-ai/
https://sacra.com/c/gamma/
https://en.wikipedia.org/wiki/Lovable_(company)
https://en.wikipedia.org/wiki/Cursor_(code_editor)
https://en.wikipedia.org/wiki/ElevenLabs
https://techcrunch.com/2025/11/19/legally-embattled-ai-music-startup-suno-raises-at-2-45b-valuation-on-200m-revenue/
https://www.paddle.com/customers/ai-saas-business-uses-paddle-to-future-proof-growth

[S12] Security
https://higgsfield.ai/security-policy.pdf
https://trust.higgsfield.ai/
```
