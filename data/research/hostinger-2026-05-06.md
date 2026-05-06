# Hostinger — SDR Research Brief

**Prepared for:** Yuno (Payment Orchestrator)
**Date:** 2026-05-06
**Researcher:** German Tatis
**Disclaimer:** Findings include verified data and inferences. Inferences are tagged `[INFERENCE]`. Some data is "according to web data" / assumptions made — flagged where applicable.

---

## EXECUTIVE SUMMARY

Hostinger is a Lithuanian-headquartered global web hosting provider — **€275.4M (~$298M) revenue in 2025 (+51% YoY), 4.6M paying customers across 178 countries**, with India (19%), Brazil (15.4%), US (9.7%), Indonesia (4.1%), and Pakistan (3.9%) as the top traffic markets. Hostinger has a **dedicated Head of Payments (Gediminas Griška)** who has publicly described an **in-house orchestration layer called "hPayments"** and flagged **3DS coverage gaps in Latin America** as an operational pain — a textbook Yuno discovery hook. Their cross-border acquirer **Credorax → Finaro was acquired by Shift4 in 2023**, creating natural strategic rethink leverage; meanwhile, Hostinger has spent the last 12 months adding APMs one country at a time (Blik in Poland, Konbini in Japan, Nequi in Colombia, Akulaku in Indonesia, OPay in Nigeria, Fawry in Egypt) — exactly the fragmented stack a single orchestrator collapses. Top opportunity: replace/augment hPayments with Yuno smart routing to fix LATAM 3DS approval rates, accelerate market additions, and reduce direct-PSP integration burden.

---

## SECTION 1 — Traffic by Country

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source URL |
|---|---|---|---|---|---|
| 1 | India | 19.00% | ~9.6M | +2.39% MoM | [SimilarWeb](https://www.similarweb.com/website/hostinger.com/) |
| 2 | Brazil | 15.43% | ~7.8M | +1.41% MoM | [SimilarWeb](https://www.similarweb.com/website/hostinger.com/) |
| 3 | United States | 9.74% | ~4.9M | +3.85% MoM | [SimilarWeb](https://www.similarweb.com/website/hostinger.com/) |
| 4 | Indonesia | 4.07% | ~2.1M | +4.87% MoM | [SimilarWeb](https://www.similarweb.com/website/hostinger.com/) |
| 5 | Pakistan | 3.87% | ~2.0M | +7.14% MoM | [SimilarWeb](https://www.similarweb.com/website/hostinger.com/) |
| 6–10 | Not individually disclosed (lumped as "Others" 47.89%) | — | — | — | [SimilarWeb](https://www.similarweb.com/website/hostinger.com/) |

- **Total monthly visits:** 50.6M (March 2026)
- **Overall trend:** -1.47% MoM (slight decline)
- **Category rank:** #3 in Web Hosting & Domain Names; #690 globally
- **Regional sub-domain hostinger.in:** +10.73% MoM (strong India growth signal)

🚩 **Flagged markets (>5% traffic):** India, Brazil, USA — all heavy LATAM/APAC presence; APAC + LATAM = 38%+ of traffic, classic Yuno multi-market signal.

---

## SECTION 2 — Legal Entities

| Country | In Top 10 Traffic? | Has Local Entity? | Cross-Border Risk? | Source URL |
|---|---|---|---|---|
| Lithuania (HQ) | No | ✅ HOSTINGER operations, UAB (Reg. 306308157, LEI 894500QM0U6LWXLTOR14) | N/A — HQ | [LEI Lookup](https://www.lei-lookup.com/record/894500QM0U6LWXLTOR14/) |
| Cyprus | No | ✅ HOSTINGER INTERNATIONAL LIMITED (Larnaca) — serves "all other countries" per ToS | N/A | [Hostinger ToS](https://www.hostinger.com/legal/universal-terms-of-service-agreement) |
| United Kingdom | No | ✅ Hostinger UK Limited (London EC3N 3AX) | No | [Hostinger ToS](https://www.hostinger.com/legal/universal-terms-of-service-agreement) |
| United States | ✅ #3 | ✅ HOSTINGER US INC. | No | [Hostinger ToS](https://www.hostinger.com/legal/universal-terms-of-service-agreement) |
| Brazil | ✅ #2 | ✅ HOSTINGER BRASIL HOSPEDAGEM DE SITES LTDA (acquired Weblink 2014) | No | [Hostinger ToS](https://www.hostinger.com/legal/universal-terms-of-service-agreement) |
| Singapore | No | ✅ HOSTINGER PTE LTD (16 Raffles Quay) — serves Asia | No | [Hostinger ToS](https://www.hostinger.com/legal/universal-terms-of-service-agreement) |
| Indonesia | ✅ #4 | ✅ PT WEB MEDIA TECHNOLOGY INDONESIA (trades as Niagahoster) | No | [Hostinger ToS](https://www.hostinger.com/legal/universal-terms-of-service-agreement) |
| **India** | ✅ **#1** | ❌ **No local entity found** — served via Cyprus entity | ⚠️ **YES** | [Razorpay/Hostinger blog](https://razorpay.com/blog/hostinger-expands-to-india-with-razorpay/) |
| **Pakistan** | ✅ #5 | ❌ Not found | ⚠️ Likely | Not verified |
| **Mexico / Colombia / Argentina** | Likely top-15 | ❌ Not found | ⚠️ Likely | Not verified |

> ⚠️ **Cross-border opportunity:** India is the #1 traffic market (19%) but Hostinger appears to operate there **without a local legal entity** — meaning cross-border acquiring fees, FX losses, and lower local approval rates. Razorpay was specifically chosen because Hostinger had to enable India "without setting up a local entity." [INFERENCE based on public Razorpay blog quote]

> ⚠️ MANUAL: Verify cross-border presentment on Hostinger India and Pakistan checkouts via official T&Cs.

---

## SECTION 3 — Payment Stack

### 3A. PSPs & Acquirers

| Country/Region | PSP / Acquirer | Evidence Type | Source URL |
|---|---|---|---|
| **India** (main hosting checkout) | **Razorpay** (Embedded Payments) — UPI, cards, wallets, net banking, intl. payments | [Press Release] — April 29, 2025 partnership | [Razorpay blog](https://razorpay.com/blog/hostinger-partners-with-razorpay-to-simplify-payments-for-global-businesses/) |
| **Brazil** (Boleto) | **EBANX** — explicitly named as PSP for Boleto Bancário | [Help Center] | [Hostinger Boleto KB](https://www.hostinger.com/support/how-to-pay-with-boleto-bancario-at-hostinger/) |
| Cross-border / Global cards (since 2021) | **Credorax → Finaro → Shift4** (acquired 2023) — smart acquiring, 120+ currencies | [Press Release] | [BusinessWire](https://www.businesswire.com/news/home/20210413005514/en/) |
| Global Wallets | PayPal, Apple Pay, Google Pay, Alipay, UnionPay | [Checkout / Help Center] | [Hostinger /payments](https://www.hostinger.com/payments) |
| Crypto | CoinGate (Bitcoin + others) | [Help Center] | [Hostinger PM KB](https://www.hostinger.com/support/1583236-what-payment-methods-are-available-at-hostinger) |
| Hostinger Website Builder (end-user merchant payments — NOT Hostinger's own checkout) | **Stripe** | [Source / Documentation] | [Hostinger Stripe KB](https://www.hostinger.com/support/6538420-hostinger-website-builder-enabling-stripe-payments/) |

**APMs not yet linked to a public PSP:** PIX, Nubank, SPEI, OXXO, Blik (Poland), Konbini (Japan), Nequi (Colombia), Akulaku (Indonesia), Fawry (Egypt), OPay (Nigeria), JazzCash (Pakistan), Globe Cash (Philippines), OVO/QRIS/BCA/Mandiri/BRI/BNI (Indonesia), Klarna (Germany), Carte Bancaire (France), PaySera (Lithuania), RuPay (India), Amazon Pay (UK).

### 3B. Orchestrator

> **Confirmed: Hostinger has built an in-house orchestration layer called "hPayments."**
>
> Per ProcessOut interview with Gediminas Griška (Head of Payments, Hostinger): Hostinger built an internal payment infrastructure called **"hPayments"** to manage technical payment integration and maintenance. Griška also publicly flagged **3DS coverage gaps in Latin America** as an operational pain.
>
> Source: [ProcessOut interview – Gediminas Griška, Head of Payments](https://www.processout.com/blog/interview-gediminas-griska-head-of-payments-hostinger)

**No public evidence of Spreedly / Primer / Gr4vy / CellPoint / APEXX use.** The hPayments build-vs-buy is a critical Yuno talking point — they've already validated orchestration as a need; the question is whether their in-house effort delivers smart routing, fraud orchestration, and rapid PSP swap-in (Yuno's strengths) at the level a commercial orchestrator does.

> ⚠️ MANUAL — DevTools: test card 4111 1111 1111 1111 | 02/30 | 123 across .com.br, .in, .com.mx, .de checkouts to capture live PSP scripts, redirect domains, and 3DS issuer.

---

## SECTION 4 — APMs (Live Verification)

### 4A. Confirmed APMs

| Market | APMs Confirmed | Verification Source | Source URL |
|---|---|---|---|
| **Brazil** | Pix, Boleto Bancário (via EBANX), Nubank wallet, Visa, Mastercard, Amex, Elo, Hipercard, installments up to 12 months, PayPal, Apple Pay, Google Pay, crypto | Live pricing footer + Help Center | [/br/precos](https://www.hostinger.com/br/precos), [PM KB](https://www.hostinger.com/support/1583236-what-payment-methods-are-available-at-hostinger) |
| **India** | UPI, RuPay, Visa, Mastercard, Amex, Discover, Diners Club, PayPal, Google Pay, crypto | Live pricing footer + dedicated PM page | [/in/payment-methods](https://www.hostinger.com/in/payment-methods) |
| **United Kingdom** | Visa, Mastercard, Amex, Discover, JCB, Diners Club, PayPal, Amazon Pay, Apple Pay, Google Pay, crypto | Live pricing footer + Help Center | [/uk/pricing](https://www.hostinger.com/uk/pricing) |
| **France** | Carte Bancaire, Visa, Mastercard, Amex, Discover, JCB, Diners Club, PayPal, Apple Pay, Google Pay, crypto | Live pricing footer + Help Center | [/fr/tarifs](https://www.hostinger.com/fr/tarifs) |
| **Spain** | Visa, Mastercard, Amex, Discover, JCB, Diners Club, PayPal, Apple Pay, Google Pay, crypto | Live pricing footer + Help Center | [/es/precios](https://www.hostinger.com/es/precios) |
| **Germany** | Cards, PayPal, Google Pay, Apple Pay, **Klarna**, crypto | Help Center per-country | [PM KB](https://www.hostinger.com/support/1583236-what-payment-methods-are-available-at-hostinger) |
| **Poland** | Cards, PayPal, Google Pay, **Blik**, crypto | Help Center per-country | [PM KB](https://www.hostinger.com/support/1583236-what-payment-methods-are-available-at-hostinger) |
| **Mexico** | Visa, Mastercard, Amex, Carnet, installments 3-12mo, PayPal, Apple Pay, Google Pay, **SPEI, OXXO**, crypto | Help Center per-country | [PM KB](https://www.hostinger.com/support/1583236-what-payment-methods-are-available-at-hostinger) |
| **Colombia** | Cards, installments **up to 36 months**, **Nequi**, PayPal, Apple Pay, Google Pay, crypto | Help Center + 2025 product updates | [Product updates 2025](https://www.hostinger.com/blog/product-updates-2025) |
| **Argentina** | Cards, installments up to 12 months, crypto | Help Center | [PM KB](https://www.hostinger.com/support/1583236-what-payment-methods-are-available-at-hostinger) |
| **Indonesia** | Cards, **BCA, Mandiri, BRI, BNI** virtual accounts, **OVO, QRIS, Akulaku** BNPL, PayPal, crypto | Help Center + 2025 product updates | [PM KB](https://www.hostinger.com/support/1583236-what-payment-methods-are-available-at-hostinger) |
| **Nigeria** | Visa, Mastercard, **OPay** | Help Center per-country | [PM KB](https://www.hostinger.com/support/1583236-what-payment-methods-are-available-at-hostinger) |
| **Egypt / UAE** | Cards, PayPal, Apple Pay, Google Pay, **Fawry** | Help Center per-country | [PM KB](https://www.hostinger.com/support/1583236-what-payment-methods-are-available-at-hostinger) |
| **Pakistan** | Cards, **JazzCash**, crypto | Help Center per-country | [PM KB](https://www.hostinger.com/support/1583236-what-payment-methods-are-available-at-hostinger) |
| **Philippines** | Cards, PayPal, Google Pay, **Globe Cash**, crypto | Help Center per-country | [PM KB](https://www.hostinger.com/support/1583236-what-payment-methods-are-available-at-hostinger) |
| **Hong Kong** | Cards (UnionPay), PayPal, **AliPay**, crypto | Help Center per-country | [PM KB](https://www.hostinger.com/support/1583236-what-payment-methods-are-available-at-hostinger) |
| **Japan** | **Konbini** added Feb 2025 + cards | Product updates 2025 | [Product updates 2025](https://www.hostinger.com/blog/product-updates-2025) |
| **Lithuania** | Cards, **PaySera**, PayPal, crypto | Help Center | [PM KB](https://www.hostinger.com/support/1583236-what-payment-methods-are-available-at-hostinger) |

### 4B. Unverified Markets

| Market | Verification Attempted? | Reason Not Verified | Popular Local APMs (reference only) |
|---|---|---|---|
| Netherlands | Yes — Help Center | Listed only generic "cards, PayPal, Google Pay, Apple Pay, crypto" — **iDEAL not named** | iDEAL |
| Belgium | Yes — Help Center | Bancontact not named | Bancontact |
| China | Yes — Help Center | WeChat Pay not named (only Alipay confirmed for HK) | WeChat Pay, UnionPay |
| Top 6–10 traffic countries | Partial | SimilarWeb only shows top 5 publicly | — |

> "Not verified" ≠ "not available." MANUAL: VPN-based checkout walk-through across NL/BE/CN before any APM claims in outreach.

---

## SECTION 5 — Payment Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|---|---|---|---|---|
| **Auto-renewal charged 14 days early** (vs. 7-day industry norm) | Trustpilot CA | Multiple reviews | Recent | [Trustpilot CA](https://ca.trustpilot.com/review/hostinger.com) |
| **Domain renewal charged a month early** | Sikayetvar/Xolvie | Documented complaint | Recent | [Sikayetvar #1](https://www.sikayetvar.com/en/hostinger-us/hostinger-charged-me-for-domain-renewal-a-month-early-how-can-i-request-a-refund-q-12835) |
| **Auto-renew charged after disabling** (Turkey) | Sikayetvar/Xolvie | Documented complaint | 2024 | [Sikayetvar #2](https://www.sikayetvar.com/en/hostinger-us/hostinger-charged-my-account-without-notice-how-can-i-dispute-and-get-a-refund-q-12834) |
| **Refund denial after suspension** | Trustpilot | Recurring | Recent | [Trustpilot 1-star](https://www.trustpilot.com/review/hostinger.com?stars=1) |
| **Double charges** (dedicated KB article) | Hostinger Help Center | Frequent enough to warrant standing docs | Ongoing | [Charged Twice KB](https://www.hostinger.com/support/1583233-hostinger-solution-what-to-do-if-you-have-been-charged-twice/) |
| **FX surprise charges** | Help Center | Documented as expected behavior | Ongoing | [Different Amount KB](https://support.hostinger.com/en/articles/6321175-i-have-been-charged-a-different-amount-what-to-do) |
| **3DS verification failed** | Help Center | Documented standing issue | Ongoing | [3DS Error KB](https://support.hostinger.com/en/articles/5402772-3d-secure-verification-failed-error-while-making-a-payment) |
| **Do-Not-Honor declines** | Help Center | Documented standing issue | Ongoing | [DNH KB](https://www.hostinger.com/support/1583237-do-not-honor-authorization-error-while-making-a-payment-at-hostinger/) |
| **Fraud auto-refund recovery** (manual KYC: card photo or bank statement upload) | Help Center | Documented standing issue | Ongoing | [Fraud KB](https://www.hostinger.com/support/11027694-understanding-fraud-payments-and-how-to-resolve-them-at-hostinger/) |
| **Email velocity decline** (rate-limit blocks after multiple tries) | Help Center | Documented | Ongoing | [Payment errors KB](https://www.hostinger.com/support/4147167-what-to-do-if-there-is-an-error-during-payment-at-hostinger/) |

**Yuno-relevant analysis:**
- **FX presentment + 3DS failures + Do-Not-Honor declines** are the strongest signals. All three are direct Yuno solves: smart routing improves DNH approval, 3DS orchestration improves LatAm conversion (Griška's stated pain!), local-currency presentment fixes FX surprise.
- Hostinger maintains **standing KB articles** for double-charges, fraud auto-refund, and 3DS failures — meaning these are **frequent enough to be operationally institutionalized**, not edge cases.

---

## SECTION 6 — Expansion & Corporate Developments

| # | Date | Development | Category | Source URL |
|---|---|---|---|---|
| 1 | Apr 29, 2025 | Razorpay Embedded Payments partnership for India (UPI, cards, wallets, net banking) | PSP partnership 🟢 | [Razorpay blog](https://razorpay.com/blog/hostinger-partners-with-razorpay-to-simplify-payments-for-global-businesses/) |
| 2 | Feb 2025 | Added Blik (Poland) and Konbini (Japan) | APM expansion 🟢 | [Product updates 2025](https://www.hostinger.com/blog/product-updates-2025) |
| 3 | May 2025 | Added Nequi (Colombia) + Akulaku BNPL & installments (Indonesia) | APM expansion 🟢 | [Product updates 2025](https://www.hostinger.com/blog/product-updates-2025) |
| 4 | 2025 | Hostinger Nigeria launch with AI tools | Geographic expansion | [Dabafinance](https://dabafinance.com/en/news/hostinger-nigeria-launch-ai-web-hosting) |
| 5 | 2025 | Malaysia data center launch (Kuala Lumpur, NVMe/AMD/100Gbps) | Infrastructure | [HostScore](https://hostscore.net/news/hostinger-launches-new-malaysia-data-center/) |
| 6 | Nov 2025 | Canada launch (English + French billing) | Geographic expansion | [Product updates 2025](https://www.hostinger.com/blog/product-updates-2025) |
| 7 | Nov 2025 | Refinancing & dividend recapitalization | Corporate finance | [Tracxn](https://tracxn.com/d/companies/hostinger) |
| 8 | 2023 | Daugirdas Jankus appointed CEO | Leadership | [Hostinger blog](https://www.hostinger.com/blog/management-changes) |
| 9 | 2023 | Credorax/Finaro acquired by Shift4 ⚠️ key signal | M&A affecting Hostinger's acquirer | [BusinessWire](https://www.businesswire.com/news/home/20211201005805/en/) |
| 10 | 2025 | Hostinger Horizons (AI website builder) global launch | Product | [Hostinger blog](https://www.hostinger.com/blog/hostinger-horizons-global-launch) |

> ⚠️ **Strategic moment:** Their primary cross-border acquirer (Credorax → Finaro) was acquired by **Shift4** in 2023. This typically triggers contract reviews, fee renegotiations, or full migration evaluations within 18–36 months. We're inside that window. [INFERENCE — assumption based on typical post-M&A acquirer dynamics; according to web data]

---

## SECTION 7 — Payment News

| # | Date | Headline | Relevance | Source URL |
|---|---|---|---|---|
| 1 | Apr 2025 | "Hostinger partners with Razorpay to simplify payments for global businesses" | 🟢 Active PSP expansion — but India-only; gaps elsewhere = orchestration opportunity | [Razorpay](https://razorpay.com/blog/hostinger-partners-with-razorpay-to-simplify-payments-for-global-businesses/) |
| 2 | 2025 | "Hostinger reports 51% revenue growth in 2025, reaches €275.4M" | Volume + growth signal | [webhosting.today](https://webhosting.today/2026/02/18/hostinger-reports-51-revenue-growth-in-2025-reaches-e275-4-million/) |
| 3 | 2025 | "Hostinger added Blik, Konbini, Nequi, Akulaku" (multi-quarter rollouts) | One-by-one APM additions = orchestration use case | [Product updates](https://www.hostinger.com/blog/product-updates-2025) |
| 4 | 2024 | "Interview – Gediminas Griška, Head of Payments, Hostinger" (ProcessOut) | **Direct buyer persona** — discusses hPayments + 3DS LATAM gaps | [ProcessOut](https://www.processout.com/blog/interview-gediminas-griska-head-of-payments-hostinger) |
| 5 | 2021 | "Credorax enables Hostinger to accept cross-border payments" | Background — note Credorax now under Shift4 | [BusinessWire](https://www.businesswire.com/news/home/20210413005514/en/) |

---

## SECTION 8 — Checkout Audit

| Dimension | Finding | Quality | Notes |
|---|---|---|---|
| Checkout type | One-page checkout, inline (own domain) | ✅ Modern | "Review orders, make an account, submit payment on a single page" |
| Guest checkout | ❌ **No** — must create account or login mid-checkout | 🔴 Friction | Mandatory account creation = drop-off risk |
| Steps to purchase | 6 steps: plan → term → account → personal info → payment method → submit | 🟡 Acceptable | Account creation is the friction point |
| 3DS | Active but documented failures (KB article exists); **3DS gaps in LATAM publicly admitted by Head of Payments** | 🔴 **Pain point** | Yuno smart routing improves 3DS issuer fallback |
| Mobile experience | Responsive plan pages; live cart not directly verified | 🟡 Unverified | MANUAL: walk mobile checkout |
| APM display logic | ✅ **Adapts by country** — different stack per geo (Brazil/Mexico/India/Indonesia/Egypt/Nigeria/Poland/Lithuania/Japan/Colombia all different) | ✅ Mature | But fragmented — managed via in-house hPayments |
| BNPL | Klarna (DE + Website Builder users in 20 EU+US/UK/AU markets); Akulaku (Indonesia, May 2025); installments up to 36 months in Colombia, 12 months in Brazil/Mexico/Argentina | ✅ Strong LATAM focus | |
| Fraud auto-refund | Triggers manual KYC document upload (card photo + bank statement) — high friction recovery flow | 🔴 Friction | Yuno fraud orchestration could reduce false positives |
| FX presentment | Issuer-applied FX rather than local currency at checkout in some flows | 🔴 Pain | Documented in KB |

> ⚠️ MANUAL: Walk live checkout in Brazil, India, Mexico, Indonesia. Capture PSP scripts (Razorpay, EBANX, Stripe) + 3DS issuer behavior + redirect domains.

---

## SECTION 9 — PCI DSS

| PCI DSS Level | Card data handling | Recommended Yuno integration | Source |
|---|---|---|---|
| Hostinger references "PCI-DSS Level 1 compliance" via **vault separate from their system** (likely inherited via PSPs — Stripe/Razorpay are Level 1 Service Providers); ISO/IEC 27001:2022 certified; no public Hostinger AOC | **Tokenized at PSP level** ([INFERENCE] — assumptions made; according to web data on /payments page language) | **Yuno Vault + Network Tokens** + redirect-free hosted fields = lowest scope, fastest swap-in alongside hPayments | [Hostinger /payments](https://www.hostinger.com/payments), [Trust Center](https://trust.hostinger.com/) |

> Hostinger's Trust Center publishes ISO 27001 + GDPR but does not publicly list a PCI DSS AOC. According to web data, the Level 1 reference appears to be inherited via PSP relationships rather than a direct Hostinger merchant AOC. Disclaimer: assumptions made.

---

## SECTION 10 — Strategic Insights

### Insight #1: hPayments is solving a problem they could buy solved — and the Head of Payments is named, public, and accessible
**Evidence:** Section 3B — Gediminas Griška (Head of Payments) interview with ProcessOut explicitly describes building "hPayments" in-house to manage payment integration & maintenance.
**Pain Point:** Build-vs-buy on orchestration is now a sunk cost vs. ongoing engineering tax. Every new APM (Blik, Konbini, Nequi, Akulaku, OPay, Fawry) requires direct PSP work.
**Yuno Value Prop:** Single API → 1,000+ payment methods + 200+ countries. Yuno absorbs the integration & maintenance tax that hPayments currently shoulders.
**Best Case:** InDrive — 10 LATAM markets in <8 months, 90% approval, 4.5% recovery — proves Yuno can light up regions faster than any in-house build.
**Outreach Angle:** Reference hPayments + the ProcessOut interview directly. Position Yuno as a complement (or successor) to hPayments — not a rip-and-replace, but smart-routing-as-a-service that lifts approval rates without rebuilding what they have.

### Insight #2: Griška has publicly admitted 3DS coverage gaps in LATAM — this is the highest-leverage discovery hook
**Evidence:** ProcessOut interview — Griška directly flagged "3DS coverage gaps in Latin America" as an operational pain.
**Pain Point:** LATAM 3DS = lower issuer participation = higher false declines = lost revenue. Brazil is Hostinger's #2 market (15.4% traffic).
**Yuno Value Prop:** Smart Routing + 3DS orchestration = +7% approval uplift + 50% transaction recovery. Yuno's LATAM 3DS coverage is industry-leading via direct issuer relationships.
**Best Case:** Livelo (+5% approval, 50% recovery) — LATAM-native uplift exactly mirroring Hostinger's gap.
**Outreach Angle:** Lead with the 3DS LATAM gap — quote his own language back to him. "You publicly mentioned 3DS coverage in LATAM — Yuno fixes that without you having to rebuild hPayments."

### Insight #3: Credorax/Finaro → Shift4 acquisition is a renegotiation moment
**Evidence:** Hostinger's primary cross-border acquirer (Credorax) was rebranded Finaro and acquired by Shift4 in 2023. Acquisitions typically trigger 18–36-month contract review windows. [INFERENCE]
**Pain Point:** Single-acquirer dependency on a now-Shift4-owned entity creates concentration risk and limits negotiation leverage. Cross-border fees compound at $298M revenue scale.
**Yuno Value Prop:** Multi-acquirer routing via Yuno = leverage to renegotiate Shift4 fees, plus fallback paths for outages or regional approval lifts.
**Best Case:** Reserva (+4% approval <3 months, multi-acquirer routing).
**Outreach Angle:** "Now that Credorax is part of Shift4, what's your plan if you need a fallback acquirer for Brazil or LATAM cross-border?"

### Insight #4: APM rollouts are happening one country at a time — orchestration collapses the timeline
**Evidence:** Sections 4A + 6 — Blik (Feb 2025), Konbini (Feb 2025), Nequi (May 2025), Akulaku (May 2025), OPay, Fawry, JazzCash all added piecemeal.
**Pain Point:** Each APM = direct integration + maintenance + monitoring + reconciliation overhead. Engineering bandwidth is the bottleneck.
**Yuno Value Prop:** Single API → all APMs available immediately; new market live in weeks, no-code PSP enablement.
**Best Case:** InDrive — 10 LATAM markets in <8 months.
**Outreach Angle:** "What did Blik take you to launch — and what's the next 5 markets on the roadmap? Yuno would have all of them ready day 1."

### Insight #5: Cross-border India operation = approval rate ceiling
**Evidence:** Section 2 — India is the #1 traffic market (19%) but operated cross-border via the Cyprus entity. Razorpay was the workaround.
**Pain Point:** Cross-border acquiring fees + lower local approval rates + FX exposure on India's 9.6M monthly visitors.
**Yuno Value Prop:** Local acquiring relationships + smart routing = closer-to-domestic approval rates without local entity build-out.
**Best Case:** Rappi (zero implementation time, 80% less analyst resolution) — proves rapid lift on complex multi-rail APAC markets.
**Outreach Angle:** "Razorpay solved India for you — but you have the same cross-border problem in Pakistan, Mexico, Colombia, Argentina, and Indonesia. Yuno solves all five with one integration."

---

## SECTION 11 — Pipeline

### 11A. Direct Competitors

| Company | Website | HQ | Est. Size | Overlap Markets | Source |
|---|---|---|---|---|---|
| GoDaddy | godaddy.com | Tempe, AZ, USA | 6,500+ employees, NYSE: GDDY | Global | [GoDaddy Commerce Agreement](https://www.godaddy.com/legal/agreements/commerce-services-agreement) |
| Bluehost (Newfold) | bluehost.com | Burlington, MA, USA | Part of Newfold (3,500+) | US-centric | [TechAdvice](https://technologyadvice.com/blog/information-technology/bluehost-vs-godaddy/) |
| SiteGround | siteground.com | Sofia, Bulgaria / Madrid | ~650 [Unverified] | EU + global | [Hostinger compare](https://www.hostinger.com/compare/hostinger-vs-namecheap) |
| Namecheap | namecheap.com | Phoenix, AZ, USA | 1,625 / $222.8M revenue | Global | [RocketReach](https://rocketreach.co/namecheap-inc-profile_b5c177c6f42e08ec) |
| IONOS | ionos.com | Montabaur, Germany | ~4,000 [Unverified], FRA: IOS | Europe | [HostAdvice](https://hostadvice.com/tools/web-hosting-comparison/ionos-vs-namecheap/) |
| DreamHost | dreamhost.com | Brea, CA, USA | ~250–264, $15M-$41M | US | [Owler](https://www.owler.com/company/dreamhost) |
| HostGator (Newfold) | hostgator.com | Houston, TX, USA | Part of Newfold | US/global | [HostAdvice](https://hostadvice.com/tools/web-hosting-comparison/blue-host-vs-godaddy-vs-hostgator/) |
| Wix | wix.com | Tel Aviv, Israel | 5,340, NASDAQ: WIX | Global | [PitchBook](https://pitchbook.com/profiles/company/51726-07) |

### 11B. Industry Peers

| Company | Website | Vertical | Key Markets | Why Similar | Source |
|---|---|---|---|---|---|
| Shopify | shopify.com | Subscription SaaS + payments | Global | Subscription billing + own PayFac | [Wikipedia](https://en.wikipedia.org/wiki/Shopify) |
| Squarespace | squarespace.com | Web builder + commerce | Global, 4M+ subs | Subscription SaaS, Stripe-integrated | [Wikipedia](https://en.wikipedia.org/wiki/Squarespace) |
| Cloudflare | cloudflare.com | Subscription infrastructure | Global, NYSE: NET | Subscription billing at scale | [Tracxn] |
| **NordVPN (Nord Security)** | nordsecurity.com | Subscription SaaS | Global | **Lithuania-based, also uses Credorax/Finaro** | [Credorax announcement](https://www.businesswire.com/news/home/20210413005514/en/) |
| Semrush | semrush.com | SaaS subscription | Global, 1,400+ | **Also uses Credorax/Finaro** | [Credorax announcement](https://www.businesswire.com/news/home/20210413005514/en/) |
| DigitalOcean | digitalocean.com | Subscription infra | Global, ~1,400 | Cloud subscription billing [Unverified] | Public filings |
| Newfold Digital | newfold.com | Hosting holding co. | Global | Bluehost/HostGator/Network Solutions parent | [whtop.com](https://www.whtop.com/groups) |

### 11C. Adopting Orchestration

| Company | Orchestrator | Date | Vertical | Source |
|---|---|---|---|---|
| **Hostinger** | **In-house "hPayments"** | Built internally | Web hosting | [ProcessOut](https://www.processout.com/blog/interview-gediminas-griska-head-of-payments-hostinger) |
| GoDaddy | **De facto multi-PSP orchestration** (Adyen + Elavon + Nuvei + Stripe + PayPal + Square + own PayFac) | Ongoing | Web hosting | [GoDaddy Commerce Agreement](https://www.godaddy.com/legal/agreements/commerce-services-agreement) |
| Wix, Bluehost, HostGator, Namecheap, SiteGround, DreamHost, IONOS | Not publicly confirmed | — | Web hosting | [Unverified] |

### 11D. Scoring (Hostinger)

| Signal | Pts | Verified? |
|---|---|---|
| Operates in 3+ countries (178 countries) | +3 | ✅ |
| Multiple PSPs (Razorpay + EBANX + Finaro + PayPal + CoinGate + Stripe-for-builder) | +3 | ✅ |
| Recent expansion (24 mo.) — Nigeria, Malaysia, Canada, Pakistan | +2 | ✅ |
| Public payment issues (KB articles for double-charge, 3DS, DNH, fraud, FX) | +2 | ✅ |
| Funding / scale >$10M (€275M revenue, 4.6M customers) | +2 | ✅ |
| LATAM/APAC/MENA traffic (Brazil, India, Indonesia, Pakistan ≈ 42% traffic) | +2 | ✅ |
| No third-party orchestrator (in-house "hPayments" only) | +2 | ✅ |
| Payment job postings | 0 | Not verified |
| Public RFP | 0 | Not found |

**TOTAL SCORE: 16 → 🔴 HIGH PRIORITY**

### Top 10 Pipeline (Adjacent Targets for Yuno)

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal |
|---|---|---|---|---|---|---|
| 1 | **Hostinger** | Web hosting (target) | Global (178 countries) | 16 | 🔴 | Head of Payments + hPayments + 3DS LATAM gap |
| 2 | GoDaddy | Direct competitor | Global | 14 [Est.] | 🔴 | Multi-PSP de facto orchestration; potential replatform |
| 3 | NordVPN / Nord Security | Industry peer (Lithuania) | Global | 13 [Est.] | 🔴 | Same Credorax/Finaro acquirer, same geo |
| 4 | Semrush | Industry peer | Global | 12 [Est.] | 🔴 | Same Credorax/Finaro acquirer |
| 5 | Wix | Adjacent | Global | 11 [Est.] | 🟡 | Multi-rail subscription + commerce |
| 6 | Squarespace | Adjacent | Global | 11 [Est.] | 🟡 | Subscription billing at scale |
| 7 | Newfold (Bluehost/HostGator) | Direct competitor | US-centric | 9 [Est.] | 🟡 | Multi-brand consolidation, billing ops |
| 8 | IONOS | Direct competitor | Europe | 9 [Est.] | 🟡 | EU-strong, SEPA-heavy |
| 9 | Namecheap | Direct competitor | Global | 8 [Est.] | 🟡 | Crypto-friendly, multi-PSP |
| 10 | DigitalOcean | Industry peer | Global | 8 [Est.] | 🟡 | Subscription infra at scale |

> All scores beyond Hostinger are [Est.] / [INFERENCE] — assumptions made based on public profile.

**Pipeline Summary:** 10 companies surfaced; 4 high-priority (🔴), 6 medium (🟡). Strongest vertical: **subscription web infrastructure** in **global / multi-region** markets. Lithuanian cluster (Hostinger + NordVPN) sharing Credorax/Finaro acquirer = warmest cross-introduction territory.

---

## SECTION 12 — Business Case

| Annual Revenue | Avg Transaction Value | Est. Annual Transactions | Primary Currency | Top 3 Markets |
|---|---|---|---|---|
| **€275.4M (~$298M USD)** in 2025 (+51% YoY) — verified | **~$30–$120 per charge** [INFERENCE — assumptions made; depends on 12 vs 48-mo prepay mix] | **~4.6M+ renewals/year minimum** + new acquisitions, upsells, domain registrations [INFERENCE] | EUR / USD / BRL / INR / IDR (multi-currency, 120+ via Finaro) | India (19%) / Brazil (15.4%) / USA (9.7%) |

**Yuno Approval Lift Estimate (Illustrative):**
- $298M annual processed → +7% approval uplift = **+$20.9M recovered annually**
- 50% transaction recovery on declines — at typical 5–10% decline rates = **$7.5M–$15M recovered**
- Combined potential: **$25M–$35M revenue recovery / year** (excluding acquirer fee savings)

> Disclaimer per memory rules: ARPU and transaction-value figures are assumptions made — Hostinger does not publicly disclose ARPU. According to web data: revenue ÷ 4.6M paying customers = ~$65/year ARPU.

---

## SECTION 13 — Outreach

### 13A. LinkedIn Message — Target: Gediminas Griška, Head of Payments

```
--- LINKEDIN MESSAGE ---
Hi Gediminas,

Read your ProcessOut interview on hPayments and the LATAM 3DS coverage gap you flagged — it stuck with me. Yuno was built for exactly that problem: smart routing across acquirers + 3DS orchestration tuned for Brazil, Mexico, Colombia, Argentina.

We're seeing +7% approval uplift and ~50% transaction recovery for subscription-heavy merchants in LATAM. Livelo got +5% approval and recovered half their declines; InDrive lit up 10 LATAM markets in under 8 months at 90% approval.

I'm not pitching a rip-and-replace of hPayments — more a complement. You keep the integration layer you've built; Yuno handles smart routing, 3DS optimization, and rapid APM enablement on top. Especially relevant given Credorax now sits under Shift4 — having a multi-acquirer fallback in place quietly de-risks that relationship.

Would 20 minutes next week make sense? Tuesday 3pm CET or Wednesday 10am CET work on my side.

Best,
[Name]
Yuno
```

### 13B. Cold Email — Target: Gediminas Griška, Head of Payments

```
--- COLD EMAIL ---
Subject: 3DS LATAM gap → Hostinger's next +5% approval

Gediminas,

Your ProcessOut interview mentioned hPayments and LATAM 3DS coverage gaps. With Brazil at 15% of Hostinger's traffic and India at 19% — both running cross-border or via Razorpay — that 3DS gap likely costs you several percent of approval per month.

Yuno is a payment orchestrator that complements (not replaces) what hPayments already does well: we add smart routing across acquirers, 3DS issuer fallback tuned for Brazil/Mexico/Colombia/Argentina, and rapid APM enablement. New markets typically go live in weeks, no-code.

Three quick proof points:
• Livelo: +5% approval, 50% transaction recovery
• InDrive: 10 LATAM markets live in <8 months, 90% approval
• Reserva: +4% approval lift in <3 months

Two thoughts that might be timely:
1. Now that Credorax sits under Shift4 post-acquisition, having a multi-acquirer fallback gives you renegotiation leverage and operational resilience.
2. Each new APM you add (Blik, Konbini, Nequi, Akulaku) is integration tax — Yuno gives you all of them on day 1, plus the next 200.

Worth a 20-minute call? I'm open Tuesday 3pm CET or Wednesday 10am CET.

Best,
[Name]
Yuno
```

---

## APPENDIX — Source URLs

```
[S1]  https://www.similarweb.com/website/hostinger.com/
[S2]  https://www.hostinger.com/legal/universal-terms-of-service-agreement
[S3]  https://www.hostinger.com/blog/financial-results-2025
[S4]  https://www.hostinger.com/support/1583236-what-payment-methods-are-available-at-hostinger
[S5]  https://razorpay.com/blog/hostinger-partners-with-razorpay-to-simplify-payments-for-global-businesses/
[S6]  https://www.hostinger.com/payments
[S7]  https://www.hostinger.com/support/how-to-pay-with-boleto-bancario-at-hostinger/
[S8]  https://www.processout.com/blog/interview-gediminas-griska-head-of-payments-hostinger
[S9]  https://www.businesswire.com/news/home/20210413005514/en/ (Credorax/Hostinger)
[S10] https://www.hostinger.com/blog/product-updates-2025
[S11] https://trust.hostinger.com/
[S12] https://en.wikipedia.org/wiki/Hostinger
[S13] https://www.lei-lookup.com/record/894500QM0U6LWXLTOR14/
[S14] https://www.hostinger.com/support/4147167-what-to-do-if-there-is-an-error-during-payment-at-hostinger/
[S15] https://www.hostinger.com/support/11027694-understanding-fraud-payments-and-how-to-resolve-them-at-hostinger/
[S16] https://www.hostinger.com/support/1583233-hostinger-solution-what-to-do-if-you-have-been-charged-twice/
[S17] https://support.hostinger.com/en/articles/6321175-i-have-been-charged-a-different-amount-what-to-do
[S18] https://support.hostinger.com/en/articles/5402772-3d-secure-verification-failed-error-while-making-a-payment
[S19] https://www.hostinger.com/support/1583237-do-not-honor-authorization-error-while-making-a-payment-at-hostinger/
[S20] https://www.hostinger.com/in/payment-methods
[S21] https://webhosting.today/2026/02/18/hostinger-reports-51-revenue-growth-in-2025-reaches-e275-4-million/
[S22] https://www.godaddy.com/legal/agreements/commerce-services-agreement
[S23] https://theorg.com/org/hostinger/teams/leadership-team
[S24] https://ca.trustpilot.com/review/hostinger.com
[S25] https://www.businesswire.com/news/home/20211201005805/en/ (Credorax → Finaro rebrand)
[S26] https://hostscore.net/news/hostinger-launches-new-malaysia-data-center/
[S27] https://dabafinance.com/en/news/hostinger-nigeria-launch-ai-web-hosting
[S28] https://www.hostinger.com/blog/management-changes
```
