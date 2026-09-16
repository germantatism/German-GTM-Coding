# Higgsfield x Yuno: slide-by-slide content (deck v1, conservative)

**Prepared:** 2026-09-16 | **Author voice:** German Tatis (AE, Yuno) | **Deck language:** English | **Base deck:** OpenAI_Yuno_MAY 2026 (49 slides) + 2 new slides (Industry context, What Higgsfield gets)
**Numbers:** every figure below is either (a) a company-stated or third-party figure with source and date, or (b) a Yuno-modeled estimate from the three-lever model in `model/higgsfield_three_lever_model.py`, labeled as such. Nothing is padded.

---

**Deck construido en Google Slides (2026-09-16):** https://docs.google.com/presentation/d/17V3SJ4ErlM_8RMq46XG0nRkdau9NYAYz4rX3ilDxI8g/edit ("Higgsfield_Yuno_SEP 2026", 49 slides). Copia del deck de OpenAI editada vía Slides API; scripts en `build/`. Cambios respecto a este documento durante la construcción: el competidor del slide 4 es genérico (Google/Veo vía Jio y Kling en USD vía Stripe; sin OpenAI/ChatGPT), el gráfico de "cost of delay" se rediseñó nativo, los logos de Higgsfield van como cuadro de texto (no hay asset), las banderas vienen de flagcdn.com, y los slides país usan las estadísticas verificadas con fuentes primarias el 16-sep-2026 (NPCI/RBI, BCB vía Worldpay, Bank of Korea, PayPay/METI, Bank Indonesia, Bizum, BKM, EHI, Groupement CB, Banxico, Betaalvereniging, MoMo/SBV, JazzCash/SBP) en lugar de las cifras heredadas del deck de OpenAI.

**Actualización (16-sep-2026, tarde):** el appendix ahora cubre los 20 mercados del top 20: se agregó **Estados Unidos** (slide 23, Stripe se queda como baseline; PayPal / Venmo / Cash App Pay, segundo procesador y recuperación de renovaciones modelados como upside de ~$4.0M/yr con +0.5pp, ARPU $300, fuera del hero de ~$25M) y **Rusia** (slide 42, mercado no direccionable: Visa/Mastercard suspendidos en marzo 2022, NSPK/Mir sancionado por el Tesoro de EE. UU. en febrero 2024; $0 modelado). El ranking de la palanca 1 (slide 43) muestra 20 filas y el gráfico de burbujas incluye a EE. UU. El deck tiene 51 slides.

## 0. Cómo usar este documento (para German)

1. Cada slide tiene: título, texto exacto que va en el slide, y notas de construcción. Copia el texto tal cual; los corchetes `[...]` son instrucciones, no texto de slide.
2. Todas las fuentes quedaron verificadas el 16-sep-2026 (slide 2, países nuevos, wave 2, Jio, ChatGPT Go, Kling). No quedan marcadores pendientes; solo las verificaciones del día de envío listadas en C.
3. Al final: (A) auditoría número por número contra el brief de Justo, (B) decisiones que tomé y (C) inputs que debes confirmar antes de enviar.
4. Regla del deck: nunca decir "Higgsfield no tiene X método". Solo decimos lo que está confirmado (help center 2026-08-01 y materiales de Stripe) y "verify at checkout" para lo demás.

---

## KEY NUMBERS (hero and anchors)

| Item | Value | Basis |
|---|---|---|
| Hero number | **~$25M/year** in preliminary gross subscription and credit revenue (defensible range $20M to $30M) | Three-lever model, base case, 18 addressable markets |
| Lever 1 (local ways to pay) | ~$21M/yr, ~83K incremental paid subscribers, ~$1.8M/mo | Model |
| Lever 2 (recovered cross-border declines) | ~$1.3M/yr, ~7K recovered subscribers, ~$0.11M/mo | Model |
| Lever 3 (saved renewals) | ~$2.8M/yr, ~27K renewals saved per year, ~$0.24M/mo | Model |
| Levers 2 + 3 combined | ~$4M/yr | Model |
| Global MAU anchor | ~12M (Yuno-estimated) | 30M+ users (Series B PR, Aug 17 2026) x ~40% monthly active; cross-checked vs ~32M monthly visits (SimilarWeb/Hypestat, Aug 2026) |
| MAU in top-20 traffic countries | ~8.3M; addressable (ex US, ex Russia) ~6.1M across 18 markets | SimilarWeb shares (German's table, 122 countries) x 12M |
| Weighted paid conversion, addressable markets | 1.7% today to 3.1% with local methods (+1.4pp blended) | Model |
| Consumer revenue pool | ~$210M annualized [ESTIMATE] | ~30% of $700M annualized revenue; 70% enterprise per The Information via MasterNodeAI (Jul 2 2026); FT via ContentGrip (Aug 2026): "most revenue now comes from businesses" |
| Hero as share of consumer pool | ~12% | $25.6M / $210M |
| Cost of inaction, 24 months | ~$19M cumulative, ~71K subscribers captured by a competitor that localizes first | Model, S-curve ratios reused from the OpenAI deck (11% / 44% / 72% / 86% of Lever 1 subs at months 6 / 12 / 18 / 24) |
| Sensitivity | 16M MAU: $34M. xAI-level uplift: $58M. All inputs at xAI/brief level + 16M MAU: $96M. Downside uplift: $15M. 9M MAU: $19M | `model/higgsfield_sensitivity.py` |

---

## SLIDE 1: Cover

**Title:** Scaling Higgsfield's payment capabilities in priority international markets
**Strapline:** 1,000+ PAYMENT OPTIONS / 180+ CURRENCIES / 194+ COUNTRIES
**Subtitle:** Why a Yuno layer above Stripe unlocks global growth fast
**Lockup:** `yuno | Higgsfield` at top-left (logo lockup rule). No greeting.

---

## SLIDE 2 (NEW, Suno-style "Industry context"): AI video at a glance

**Kicker:** INDUSTRY CONTEXT
**Title:** AI video at a glance: a category that scaled 10x in a year, and Higgsfield leads it

**Left column, three stat tiles (same layout as Suno slide 4):**

Tile 1: **$847M** TAM
Sub: AI video generator market, 2026. ~$3.35B by 2034 (18.8% CAGR), Fortune Business Insights (updated Aug 31 2026)
Right text: Analyst sizing lags the category: Higgsfield alone books ~$700M against an $847M 2026 estimate (The Business Research Company puts 2026 at $1.04B). The category is being re-sized in real time, and most of that revenue now comes from businesses buying production capacity, not from consumer subscriptions.

Tile 2: **$700M** annualized revenue, Aug 2026
Sub: From ~$10M in April 2025 to $700M in 16 months
Right text: Disclosed run-rates put Higgsfield first: Kling AI (Kuaishou) reported ~$500M ARR in March 2026 and RMB 850M+ revenue in Q2 2026; Runway reached $200M ARR in September 2026; MiniMax (Hailuo) reported $79.0M revenue for 2025. On traffic, higgsfield.ai ranks #1,228 globally vs kling.ai #4,223 and runwayml.com #7,435 (SimilarWeb, Aug 2026).

Tile 3: **30M+** users across 238 countries and territories
Sub: 390 of the Fortune 500 are customers (Aug 2026)
Right text: Usage is global by default and monetization is card-led by default. The Stripe case study puts 75% of Higgsfield's revenue outside the US, while the 95.6% authorization rate it quotes covers only the US, Europe and Australia.

**Right column, purple box:**
**#1**
THE CATEGORY, CONCENTRATED IN ONE COMPANY
30M+ users. $700M annualized revenue (Aug 2026), the highest disclosed in the category. Valued at $5.4B (Aug 2026), level with Runway ($5.3B, Feb 2026) and Luma ($4B+, Nov 2025). 75% of revenue outside the US. Where this category monetizes internationally is decided at Higgsfield's checkout.

**Bottom row, "WHAT DEFINES THE CATEGORY IN 2026" (three purple cards):**

Card 1: **The aggregation era**
Higgsfield sells one workflow over 30+ models: third-party (Kling 3.0, Seedance 2.0, Wan 2.7, Sora 2, Veo 3.1, Hailuo 2.3) plus its own Soul model (higgsfield.ai, Sep 16 2026). Switching cost for the user is low; the winner is whoever removes friction fastest.

Card 2: **The enterprise turn**
In January 2026 businesses were under a quarter of revenue; by August 2026 they were the majority (FT via ContentGrip). Consumer and prosumer is now the ~30% that has to be monetized efficiently, not the whole story.

Card 3: **Big tech retreated from the standalone app**
OpenAI discontinued the Sora app (announced Mar 24 2026; Sora 2 stays available through ChatGPT and partners such as Higgsfield until the API window closes). Google ships Veo 3.1 inside Gemini and Flow (275M videos in Flow's first five months), and Meta discloses no Vibes numbers. The consumer category belongs to the specialists.

**Closing bar:** When 75% of revenue sits outside the home market and the checkout is card-led, payments infrastructure becomes the growth lever. Every point of conversion, approval and renewal recovery lands directly on revenue. That is what this deck is about.

**Sources (footnote):** Fortune Business Insights, AI Video Generator Market (updated Aug 31 2026): https://www.fortunebusinessinsights.com/ai-video-generator-market-110060 · The Business Research Company via Research and Markets (Feb 2026): https://www.researchandmarkets.com/reports/6227059/ai-video-generator-market-report · PR Newswire, Higgsfield Series B (Aug 17 2026) · Stripe customer story: https://stripe.com/customers/higgsfield · Kuaishou Q1 2026 results (May 27 2026): https://www.prnewswire.com/apac/news-releases/kuaishou-technology-announces-first-quarter-2026-unaudited-financial-results-302782902.html · Kuaishou Q2 2026 results (Aug 19 2026) · PYMNTS, Runway $200M ARR (Sep 8 2026): https://www.pymnts.com/news/artificial-intelligence/2026/runway-ai-hits-200-million-revenue-and-expands-robotics-capabilities · Wikipedia/MiniMax (2025 revenue $79.0M) · SimilarWeb competitors page (Aug 2026): https://www.similarweb.com/website/higgsfield.ai/competitors/ · ContentGrip citing FT (Aug 18 2026) · TechCrunch, Sora app shutdown (Mar 24 2026): https://techcrunch.com/2026/03/24/openais-sora-was-the-creepiest-app-on-your-phone-now-its-shutting-down/ · Google blog, Veo 3.1 / Flow (Oct 15 2025): https://blog.google/technology/ai/veo-updates-flow/ · Higgsfield model pages: https://higgsfield.ai/ai-video, https://higgsfield.ai/soul · aifundingtracker (Runway, Luma rounds).

---

## SLIDE 3: Executive summary

**Kicker:** THE OPPORTUNITY
**Hero:** **~$25M/year** IN PRELIMINARY GROSS SUBSCRIPTION AND CREDIT REVENUE
**Lead text:** Higgsfield can unlock ~$25M/year in preliminary gross subscription and credit revenue by fixing three payment leakage points across 18 priority international markets.

**Body (left):** Higgsfield already has material demand in its priority international markets; the question is how much converts to paid, recurring revenue. With ~12M monthly active users (Yuno-estimated from 30M+ registered users, Series B release, Aug 2026) and 75% of revenue already outside the US (Stripe case study), today's card-led checkout misses local payment behavior, suppressing free-to-paid conversion, card approval and renewal retention.

**Three lever boxes:**

Box 1 (largest): **~$21M/year**
Pay online via dominant local rails: UPI, Pix Automático, QRIS, PayPal, iDEAL, Bizum, PayPay, SPEI and others
Comes from audience expansion via local payment methods. With ~85% of Higgsfield's traffic outside the US (SimilarWeb), concentrated in markets where consumers default to local rails over international cards (India, Indonesia, Turkey, Vietnam, Brazil, Mexico), adding the right method per market lifts paid conversion by making the subscription path familiar, trusted and accessible.
The largest share and ~83K incremental paid subscribers

Box 2 + 3: **~$4M/year**
The second and third levers add combined
Authorization uplift through local card processing recovers ~7K cross-border declines per year via local acquiring, MoR and domestic schemes (RuPay, TROY, Cartes Bancaires), most material in Brazil, India, Turkey and South Korea. Subscription continuity via retries and redundancy saves ~27K renewals annually from card expiries, auto-refill failures and renewal declines, particularly in the UK, Germany, India and South Korea.

**Bottom bar:** Higgsfield needs a payment-localization layer across its global payment stack: local methods where rails dominate, domestic routing where cross-border cards underperform, and recovery where payments fail. Yuno orchestrates that layer above Stripe. The proposed next step is a two-week joint data sprint to calibrate these estimates against Higgsfield's country-level checkout, authorization, renewal and ARPU data and produce an implementation roadmap.

---

## SLIDE 4: Speed to market and the cost of delay

**Kicker:** SPEED TO MARKET
**Title:** Outside the US and EU, paid AI-video subscribers are near zero. This is a greenfield race, and first mover takes it.

**Left text:** ~6M Higgsfield MAU across the 18 addressable priority markets, of ~12M globally (Yuno-estimated). No AI-video competitor has localized international checkout yet: Kling (Kuaishou, ~$500M ARR in March 2026) sells its global plans in USD through Stripe per its own payment policy. Distribution is moving faster than payments: Google bundles Google AI Pro, Veo video generation included, free for 18 months with Jio unlimited-5G plans in India (announced Oct 30 2025, still claimable Sep 2026), and OpenAI's ChatGPT Go launched in India at ₹399/month with UPI (Aug 2025) and more than doubled paid subscribers. Paid AI-video penetration outside US/EU is still near zero.

**Callout:** IN THESE 18 MARKETS, PAID AI-VIDEO SUBSCRIPTIONS ARE A BLANK SLATE. There are no incumbents to displace, only users to convert.

**Right: COMPOUNDING COST OF DELAY (four steps)**

| Month | If Higgsfield delays, a localized competitor captures: | Lost revenue (cumulative) |
|---|---|---|
| 6 | ~9K subs Higgsfield left open | ~$0.7M |
| 12 | ~36K subs | ~$3.9M |
| 18 | ~59K subs | ~$10.4M |
| 24 | ~71K subs | ~$19.0M |

**Footer tile:** 24 MONTHS COST OF INACTION: **~$19M+** to whoever localizes first

**Build note:** ratios reused from the OpenAI deck (competitor captures 11% / 44% / 72% / 86% of Lever 1 subscribers by months 6 / 12 / 18 / 24), applied to 83K Lever 1 subs at a blended $21.6/month. Source line: "Yuno model; SimilarWeb; Kuaishou Q1 2026 results (May 27 2026); Kling AI Payment Policy (Apr 21 2026); TechCrunch (Oct 30 2025; Aug 18 and Sep 22 2025); Jio offer page (Sep 2026)". URLs: https://kling.ai/docs/payment-policy · https://techcrunch.com/?p=3063978 · https://www.jio.com/google-gemini-offer/ · https://techcrunch.com/2025/08/18/openai-launches-a-sub-5-chatgpt-plan-in-india · https://techcrunch.com/2025/09/22/after-india-openai-launches-its-affordable-chatgpt-go-plan-in-indonesia/

---

## SLIDE 5: Strategic context, the decision frame

**Kicker:** STRATEGIC CONTEXT / THE DECISION FRAME
**Title:** Stripe alone leaks revenue at four points. A second PSP only fixes one.
**Sub:** To capture the full ~$25M annualized opportunity, Higgsfield needs more than another acquirer. It needs orchestration plus local depth.

**Table: FOUR PAYMENT-FRICTION GAPS**

| Where revenue leaks today | TODAY: Stripe only (cross-border, card-led) | OPTION A: + Adyen / Checkout.com as 2nd PSP (two integrations) | OPTION B: + Yuno orchestration (one integration, 30 PSPs, local ops) |
|---|---|---|---|
| **Local methods missing** (UPI, QRIS, PayPal, iDEAL, Bizum, SPEI...) ~$1.8M/mo at stake | Limited to Stripe's native LPM list. Help center (Aug 1 2026) lists cards, Apple Pay and bank payments; states "PayPal and cryptocurrency are not supported" | Better, but EM gaps remain | 30+ local PSPs per market, full LPM depth |
| **Cross-border card declines** (issuer risk, FX, 3DS) ~$0.1M/mo at stake | Cross-border routing only. Help center tells declined customers to "contact your bank and ask them to authorize online or international payments". Auth benchmark published only for US, Europe, Australia (95.6%) | Has local acquiring, but MoR capability and US-entity limitations for Higgsfield | Routes via Stripe + Adyen + 30 local acquirers, MoR where needed |
| **Renewal failures** (rebills, auto-refill) ~$0.25M/mo at stake | Single provider, no fallback. "Stripe retries automatically", ~14-day cure window, then cancellation | No cross-PSP retry between Stripe and Adyen | Cross-PSP retries, token refresh, issuer-aware |
| **No local expertise on the ground** (regulators, BIN logic, issuer escalations, FX, settlement) | No in-country ops in 18 markets. A Lifecycle & Retention PM role (Jul 2026) now owns "dunning, involuntary churn, grace flows" | Adyen is also global; Higgsfield still builds in-house | Yuno teams embedded per market: regs, declines, escalations. Enables 1 to 3 to actually work |

**Bottom line:** Option A captures a fraction of the $25M. Option B captures the full $25M, because Yuno includes redundancy plus the local rails and people a second PSP can't deliver alone.
**Source line:** Higgsfield help center (Aug 1 2026); Higgsfield Terms of Use 9.1 (Jul 26 2026); Stripe customer story; Ashby job posting (Jul 28 2026); Yuno research; Adyen Cross-Border Index; Recurly subscription benchmarks.

---

## SLIDE 6: Proposed architecture

**Kicker:** PROPOSED ARCHITECTURE
**Title:** Keep Stripe direct. Add Yuno alongside it. Zero infra risk, full upside.
**Sub:** Stripe stays live as your safety net. Yuno adds the orchestration layer around it: redundancy, local PSPs, retries and LPMs included.

**Left block, "Stripe (direct): existing integration preserved and key benefits locked"**
- Global card processing (US, EU, Australia) where Stripe already posts 95.6% authorization
- Link (40%+ of transactions), Klarna and Affirm, Adaptive Pricing stay as they are
- Stripe Connect payouts for Higgsfield Earn continue
- Fallback if Yuno is ever unavailable
- No migration needed: stays as-is

**Right block, "Yuno Orchestration Layer: new integration, single API unlocks everything below"**
- Local payment methods in all 18 priority markets
- Cross-PSP smart retries (Stripe → Adyen → local acquirer)
- Local acquiring + domestic scheme routing (RuPay, TROY, Cartes Bancaires, JCB local)
- Issuer-aware smart routing across 30+ PSPs and local acquirers
- Single dashboard for every attempt across every route

**Bottom row:** Local PSPs (logos: dLocal, EBANX, PayU, Razorpay, Xendit, iyzico, Mercado Pago, Adyen)

---

## SLIDE 7 (NEW, Bending-Spoons-style): What Higgsfield gets

**Kicker:** HIGGSFIELD PROPOSED MODEL
**Title:** From a single processor to one scalable Global Financial Infrastructure

**Diagram (left, same as Bending Spoons slide 7):**
Top: Higgsfield logo, with three product surfaces under it: Web Studio (subscriptions + credit packs + auto-refill), Team / Scale / Enterprise (per-seat, invoice or PO), Higgsfield Earn (creator payouts, 10,000+ creators, $1M+ distributed)
Arrow: "One integration owned by Higgsfield" → API
Yuno block modules (3x3): Smart Routing, Risk Conditions, Tokenization, Checkout Builder, Fraud & Risk (Nova), KYC / KYB, Payouts, Insights, Connectors
Bottom black bar: logos Stripe, Adyen, PayPal, dLocal, Mercado Pago, Razorpay, Nubank, Worldpay + "+1,000 Global Payment Partners & Methods"
Expected impact tiles: **+7%** avg. approval-rate uplift (published) | **30%** recovered revenue on failed payments (published)

**Right column cards (six, this is where Justo's points live):**

**Smart Routing Engine**
Route every subscription, credit pack and auto-refill across Stripe and local acquirers by BIN, issuer and market. Stripe keeps the traffic it already wins; local routes take the rest.

**Failover + Recovery**
Automatic cascade and retry logic across processors recovers renewals that a single retry schedule gives up on. Directly addresses the "dunning, involuntary churn, grace flows" scope of the Lifecycle & Retention PM role.

**1,000+ Local Methods**
Add UPI in India, Pix Automático in Brazil, QRIS in Indonesia, PayPal in Germany and the UK, iDEAL, Bizum, PayPay, SPEI and OXXO through one API, beyond card-only web checkout.

**KYC / KYB, orchestrated**
Onboard creators for Higgsfield Earn payouts (KYC is already mandatory per the Trust page) and verify Team, Scale and Enterprise workspaces (KYB) through the same integration, with provider choice per market instead of one vendor.

**Taxes and merchant-of-record coverage**
Sell locally without opening 18 entities: local tax handling, invoicing and settlement through Yuno's MoR and PSP-of-record partners per market, alongside Stripe's tax handling where it already works. [CONFIRMAR CON JUSTO: redacción exacta de la capacidad de impuestos que vamos a prometer]

**Distribution deals**
Yuno's BD team negotiates on Higgsfield's behalf: co-marketing with each wallet, priority placement and badge inclusion in APM apps, promotional rates per region, direct fee negotiations with each PSP (UPI apps, Mercado Pago, GCash, Kaspi). Integration alone doesn't get a merchant promoted; a relationship does.

**Build notes:** Reconciliation appears as a module label only; footnote "Reconciliation: confirm GA status before send" (flagged as roadmap in Sep 2026). Do not print the +12% / 20 to 30% tiles from the Bending Spoons slide; use +7% / 30% (published).

---

## SLIDE 8: Dedicated resources

**Kicker:** DEDICATED RESOURCES · YUNO COMMITMENT TO HIGGSFIELD
**Title:** Yuno commits dedicated teams across every region, not just software
**Regional presence line:** Local teams across the Americas, EMEA and APAC: São Paulo · Mexico City · San Francisco · New York · Bogotá · Buenos Aires · Madrid · London · Paris · Dubai · Singapore · Mumbai · Manila

Four columns, same copy as the OpenAI deck with "Higgsfield" substituted:
1. **MARKETING & PARTNERSHIPS** (APM partnerships: drive adoption + commercial promotions; embedded with 30+ local APMs): co-marketing with each APM (UPI, Pix, QRIS, iDEAL, PayPal...), priority placement and badge inclusion in APM apps, joint campaigns and promotional rates per region, direct fee and commercial negotiations with each PSP.
2. **TECHNICAL ACCOUNT MGMT** (TAM team: day-to-day platform health + decline analysis; same-timezone coverage): BIN-level decline analysis and routing optimization, issuer escalations on stuck and high-risk transactions, continuous tuning of retry logic and fallback paths, real-time dashboards and weekly business reviews.
3. **SALES ENGINEERING** (Solutions engineers: implementation + integration partner; on-call during launches): direct integration support (single API, all PSPs), per-market go-live runbook, custom checkout flow tuning per geography, sandbox, monitoring and reconciliation setup.
4. **KEY ACCOUNT MGMT** (Strategic KAM aligned to Higgsfield's roadmap): single point of contact across all regions, QBRs on funnel performance and market expansion, net new market entry sequencing (Kazakhstan and Central Asia included, given the Almaty hub), executive escalation owner.

**Source:** Yuno commercial commitment to Higgsfield; team structures dedicated upon contract signing.

---

## SLIDE 9: Top 20 markets by combined three-lever opportunity

**Kicker:** TOP MARKETS
**Title:** Stripe does the US, EU and Australia well. Yuno fills the gaps and reinforces those markets.
**Sub:** Ranked by Higgsfield web traffic share (SimilarWeb, 122 countries) [CONFIRMAR: periodo exacto de tu tabla de SimilarWeb para el footnote].

| # | Country | Traffic share | Higgsfield MAU (est.) | Incremental MRR | Dominant play | Archetype |
|---|---|---|---|---|---|---|
| 1 | United States | 15.13% | 1.82M | Baseline, $0 | Stripe direct, unchanged | Home market |
| 2 | India | 12.54% | 1.50M | $0.67M | UPI + UPI AutoPay + RuPay/local debit + retries | Full-stack |
| 3 | Russia | 3.82% | 0.46M | Not addressable | Visa and Mastercard suspended operations in March 2022; NSPK (Mir) under US sanctions since February 2024 | Excluded |
| 4 | United Kingdom | 3.76% | 0.45M | $0.14M | PayPal + Open Banking + Apple/Google Pay + retries | Mature |
| 5 | South Korea | 3.71% | 0.45M | $0.09M | Toss / Samsung Pay + local card acquiring + retries (Kakao Pay, Naver Pay, PayCo already live) | APM-led |
| 6 | Germany | 3.35% | 0.40M | $0.13M | PayPal + SEPA DD + Klarna recurring + retries | Mature |
| 7 | Brazil | 3.26% | 0.39M | $0.11M | Pix Automático + local BRL acquiring + installments (Pix already live) | Full-stack |
| 8 | Indonesia | 2.89% | 0.35M | $0.15M | QRIS + GoPay/OVO/DANA/ShopeePay + local cards | Full-stack |
| 9 | Spain | 2.31% | 0.28M | $0.09M | Bizum + PayPal + SCA-aware retries | Mature |
| 10 | Italy | 2.19% | 0.26M | $0.08M | PayPal + Satispay + Bancomat Pay / PostePay | Mature |
| 11 | France | 2.02% | 0.24M | $0.08M | Cartes Bancaires routing + PayPal / SEPA | Mature |
| 12 | Canada | 2.01% | 0.24M | $0.08M | Interac e-Transfer + PayPal + local CAD acquiring | Mature |
| 13 | Turkey | 1.96% | 0.24M | $0.11M | TROY + local installments + FX-aware local acquiring | Full-stack |
| 14 | Vietnam | 1.63% | 0.20M | $0.09M | MoMo / ZaloPay + VietQR / NAPAS + local cards | Full-stack |
| 15 | Netherlands | 1.62% | 0.19M | $0.06M | iDEAL + SEPA DD + PayPal | Mature |
| 16 | United Arab Emirates | 1.57% | 0.19M | $0.06M | Local AED acquiring + Apple Pay + Tabby / Tamara | APM-led |
| 17 | China | 1.55% | 0.19M | $0.02M | Alipay + WeChat Pay cross-border (WeChat Pay already live) | APM-led |
| 18 | Japan | 1.53% | 0.18M | $0.05M | PayPay + Konbini + JCB local routing | Mature |
| 19 | Mexico | 1.33% | 0.16M | $0.07M | SPEI + OXXO Pay + Mercado Pago + local MXN acquiring | Full-stack |
| 20 | Pakistan | 1.27% | 0.15M | $0.05M | JazzCash / Easypaisa + Raast + PayPak debit | Full-stack |
| | **PORTFOLIO TOTAL** | 68.5% of traffic | 8.3M (6.1M addressable) | **~$2.1M/mo · ~$25M annualized · ~90K users** | | |

**Right-side tiles:**
PORTFOLIO TOTAL: ~6.1M addressable MAU · ~12M global MAU (Yuno-estimated) · ~90K paid-subscriber impact (83K new + 7K recovered)
CONCENTRATION: TOP 3 ~45% (India · Indonesia · United Kingdom) · TOP 10 ~78% of total value
ARCHETYPE SPLIT: Full-stack ~$1.26M/mo (~59%) · Mature ~$0.71M/mo (~33%) · APM-led ~$0.17M/mo (~8%)

**Source line:** SimilarWeb (German's export, 122 countries); Yuno three-lever model; Russia constraint per The Moscow Times (Mar 6 2022) and Wikipedia/Mir; full detail in appendix.
**Build notes:** Row 1 (US) and row 3 (Russia) are shown in grey with no MRR; this reinforces the architecture message (Stripe keeps the US) and is honest about Russia. If you prefer 20 addressable markets, replace those two rows with ranks 21 and 22 from your SimilarWeb export and I will re-run the model.

---

## SLIDE 10: 20 additional emerging markets (wave 2)

**Kicker:** ADDITIONAL EMERGING MARKETS
**Title:** 20 additional emerging markets can extend Higgsfield's localization moat, ranked by long-term strategic attractiveness

**Selection logic (footnote):** emerging markets outside the top-20 traffic list, ranked by population x AI-demand headroom x payment-localization gap x execution feasibility (same weights as the OpenAI deck). Kazakhstan is included deliberately: it is Higgsfield's engineering hub (Almaty) and Kaspi.kz is a super-app rail.

| # | Country | Population (M) | Internet penetration | Payment-localization gap (dominant rails) | First-mover priority |
|---|---|---|---|---|---|
| 1 | Philippines | 117 | 83.8% | E-wallet 33%, card 30%, bank transfer 16% of e-com (PPRO 2024); GCash / Maya wallet-first, QR Ph | Very high |
| 2 | Saudi Arabia | 34.7 | 99.0% | Cards 42% (93% of them mada), e-wallet 22%, bank transfer 16% (PPRO 2023); mada, STC Pay, Apple Pay / mada Pay, Tabby / Tamara | Very high |
| 3 | Nigeria | 239 | 45.5% | Card 37%, bank transfer 29%, cash 16%, e-wallet 10% (PPRO 2023); bank transfers + wallets dominate, cards underperform | Very high |
| 4 | Thailand | 71.6 | 94.7% | Bank transfer 42%, e-wallet 25%, card 21% (PPRO 2024); PromptPay QR, TrueMoney | High |
| 5 | Colombia | 53.6 | 77.8% | Cards 36%, bank transfer 29%, e-wallet 26% (PPRO); PSE, Nequi, Daviplata, Bre-B (OA) | High |
| 6 | Argentina | 45.9 | 90.6% | Cards 46%, e-wallets 34%, bank transfer 14% (PPRO); Mercado Pago, MODO, installments, Naranja / Cabal domestic schemes | High |
| 7 | Egypt | 119 | 82.7% | Cash 31%, card 30%, e-wallet 15%, bank transfer 10% (PPRO 2024); Fawry, Meeza, InstaPay (OA) | High |
| 8 | Malaysia | 36.1 | 98.0% | Bank transfer 37%, cards 28%, e-wallet 24% (PPRO); FPX / DuitNow QR, Touch 'n Go, Boost, GrabPay | High |
| 9 | Bangladesh | 176 | 47.0% | bKash / Nagad mobile financial services (OA); e-com mix not published by PPRO | High |
| 10 | Poland | 38 | 89.8% | Bank transfer 67%, card 15%, e-wallet 15% (PPRO); BLIK (~30%), Przelewy24, PayU | High |
| 11 | South Africa | 64.9 | 79.6% | Card 43%, bank transfer 22%, e-wallet 20% (PPRO 2023); EFT, SnapScan, PayShap / Ozow (OA) | High |
| 12 | Kazakhstan | 20.9 | 93.4% | Kaspi.kz QR / Pay super-app (OA); Higgsfield's engineering hub (Almaty) | High |
| 13 | Peru | 34.7 | 82.0% | Cards 52%, bank transfer 17%, e-wallet 11%, cash 10% (PPRO 2023); Yape / PLIN, PagoEfectivo (OA) | Medium |
| 14 | Chile | 19.9 | 94.5% | Cards 53%, e-wallets 22%, bank transfer 21% (PPRO); local schemes 44% of card volume; Webpay, Mercado Pago, MACH (OA) | Medium |
| 15 | Kenya | 57.8 | 40.5% | Cash 35%, other 34%, card 28% (PPRO 2023); M-Pesa mobile money (OA) | Medium |
| 16 | Morocco | 38.5 | 92.2% | Cash 58%, e-wallet 20%, card 17% (PPRO 2024); CMI local cards; Moroccan card lockouts already reported (Trustpilot, Sep 2026) | Medium |
| 17 | Ukraine | 39.3 | 89.6% | Privat24 / LiqPay, Apple / Google Pay heavy (OA); PPRO mix not published | Medium |
| 18 | Sri Lanka | 23.3 | 59.7% | LankaQR, JustPay, CEFTS bank transfers (OA); PPRO mix not published | Medium |
| 19 | Nepal | 29.6 | 56.0% | Fonepay QR, eSewa / Khalti wallets (OA); PPRO mix not published | Medium |
| 20 | Ghana | 35.2 | 74.6% | MTN MoMo mobile money (OA); PPRO mix not published | Medium |
| | **WAVE 2 TOTAL** | **~1.3B** | **~79% simple avg (~70% weighted, ~0.9B internet users)** | Mobile money, wallets and instant rails dominate | |

**Right column ("WHY THIS MATTERS FOR HIGGSFIELD"):** Capture monetization in these markets early, before AI-video demand inflects and global competitors race in to localize. Tiles: "~1.3B population", "~79% avg internet penetration", "Mobile money / wallets / instant rails dominate", "Localize early, before demand inflects".
**Sources:** population (Oct 2025) and internet users (end-2025) from DataReportal Digital 2026 country reports (datareportal.com/reports/digital-2026-[country]); e-commerce payment mix from PPRO country pages (ppro.com/countries/[country], data vintage 2022 to 2024 as noted); (OA) = rail description carried over from the OpenAI deck (Yuno research).
**Build note:** ask German for SimilarWeb ranks 21 to 40 so the wave-2 order can also reflect actual Higgsfield traffic (today it reflects strategic attractiveness only).

---

## SLIDE 11: Methodology bridge (waterfall)

**Kicker:** METHODOLOGY BRIDGE
**Title:** How we sized the three levers: start with existing demand, then remove payment leakage step by step
**Sub:** Preliminary outside-in estimate; Higgsfield's internal funnel data should replace Yuno's external assumptions.

Waterfall steps (left to right):
0. STARTING POINT: Estimated Higgsfield monthly active users **~12M** globally, **~6.1M** across the 18 addressable markets. Demand baseline; Higgsfield internal data should replace this estimate.
1. ADD LOCAL WAYS TO PAY: **~83K new paid subscribers · ~$1.8M/month.** Local methods convert Higgsfield users who can't (or won't) pay with a global card today.
2. FIX DECLINED CARDS: **~7K recovered paid subscribers · ~$0.11M/month.** Local card processing recovers cross-border declines that issuers would otherwise reject.
3. SAVE FAILED RENEWALS: **~27K annual renewals saved · ~$0.24M/month.** Smart retries and provider redundancy save renewals and auto-refills lost to involuntary churn.
4. PRELIMINARY TOTAL: **~$2.1M/month · ~$25M annualized · ~90K new + retained users (base case).** PRELIMINARY GROSS SUBSCRIPTION AND CREDIT MRR IMPACT.

**Waterfall logic (bottom):** Local methods expand the paid base. Localized processing improves approval on remaining card attempts. Retries recover failed renewals on the resulting subscription base. Levers should not be interpreted as three independent user pools.

---

## SLIDE 12: Strategic logic, why move now

**Kicker:** STRATEGIC LOGIC · WHY MOVE NOW
**Title:** Beyond today's $25M: being first to localize wins the next decade in emerging markets
**Sub:** Payment localization is the bottleneck no AI-video platform has cracked. Whoever solves it first becomes the default monetization path as demand inflects.

Three columns:
- **LOCALIZATION TAKES TIME.** Payment orchestration: 4 to 12 weeks per market. Direct PSP integrations: 6 to 18 months each. Multiply by 20 to 40 markets, add local entity setup, regulatory work and operations on the ground, and the first mover holds a structural lead measured in years, not quarters. Higgsfield integrated Stripe in 3 days with one backend engineer (Stripe case study); Yuno is the same shape of decision, one integration, at the local-rails layer.
- **DEMAND IS INFLECTING NOW.** The next 20 emerging markets hold ~1.3B people and ~0.9B internet users (DataReportal Digital 2026), with penetration still rising in the largest ones (Nigeria 46%, Bangladesh 47%, Kenya 41%). Mobile money, wallets and instant rails are the default way these consumers pay online.
- **THE WINDOW IS SHORT.** Google gives Jio's unlimited-5G users 18 months of Google AI Pro with Veo at no cost (Oct 2025, all ages since Nov 10 2025, still live). OpenAI launched ChatGPT Go in India at ₹399/month with UPI (Aug 2025), then Indonesia at Rp 75,000 (Sep 2025), then made it free for a year in India (Nov 2025); Go is now sold in every ChatGPT country. The monetization race in emerging markets has started, with localized pricing, local rails and carrier distribution as the entry weapons. In AI video specifically, nobody has moved yet.

**Bottom bar:** CAPTURE TODAY / WIN TOMORROW: ~$25M annualized in the 18 priority markets, and market control across the next 20 emerging markets where AI-video demand is just starting. Tiles: "4 to 12 weeks vs 6 to 18 months per market" · "~1.3B population · ~0.9B internet users today" · "Payment infra is the moat models can't catch up to".

---

## SLIDE 13: Section divider

**Title:** The Decision Frame
**Sub:** Top markets by combined three-lever opportunity. Each market shows how the three levers stack to a single combined MRR.

---

## SLIDE 14: Bubble chart, demand vs local-payment intensity

**Kicker:** TOP MARKETS
**Title:** Localization matters most where Higgsfield already has demand and where local payment behavior is strong
**Axes:** X = Local-payment intensity (LPM / APM as % of digital payments): Low <30%, Medium 30 to 60%, High 60%+. Y = Higgsfield demand growth: Low <15%, Medium 15 to 30%, High 30%+. Bubble size = estimated Higgsfield MAU.

Placement (build note):
- High LPM intensity: India, Indonesia, Vietnam, Pakistan, Turkey, Brazil, Mexico, China
- Medium: South Korea, Japan, Netherlands, Spain, Italy, Germany, UAE
- Low: United Kingdom, Canada, France
- Largest bubble: India (1.5M). Then UK, South Korea, Germany, Brazil (0.39 to 0.45M).

**Right panel, PRIORITY COUNTRIES FOR LOCALIZATION COMBINE:** large or growing Higgsfield demand · high reliance on local payment methods · a clear localization path (APM enablement, local acquiring, or stronger retry / renewal recovery).
**Source:** team estimations based on various reports, incl. SimilarWeb, Statista, Semrush, Visual Capitalist.

---

## SLIDE 15: Section divider

**Title:** THE REALITY

---

## SLIDE 16: Second PSP vs Yuno

**Kicker:** REVENUE COMPARISON
**Title:** A second-PSP integration captures ~$6M/year. Yuno orchestration captures the full ~$25M.

Left (Stripe + Adyen direct): adds LPMs in ~8 to 10 markets where Adyen has coverage · no coverage depth in Pakistan, Vietnam, Turkey local rails · no cross-PSP retry (Lever 3 mostly lost) · authorization uplift limited to Adyen's own routing · ~25% of the addressable opportunity → **~$6M/YR** estimated incremental revenue.
Right (Stripe + Yuno orchestration): includes Adyen + Stripe + 30 local PSPs per market · cross-PSP retry unlocks full Lever 3 (~$2.8M/yr) · multi-acquirer routing maximizes Lever 2 (~$1.3M/yr) · 100% OF THE ADDRESSABLE OPPORTUNITY → **~$25M/YR**.
**Bottom:** Yuno ARR is ~4x the second-PSP-only ARR, because orchestration unlocks all three levers, not just partial LPM coverage.
**Build note:** the 25% share is the same modeled ratio used in the OpenAI deck; label "Yuno estimate".

---

## SLIDE 17: Six Higgsfield data points

**Kicker:** REQUIRED INPUTS
**Title:** Six Higgsfield data points convert this strategic case into a board-grade financial forecast

| # | Input | Why | Use |
|---|---|---|---|
| 1 | MAU, checkout starts and web vs invoice mix by country | Replaces the SimilarWeb-triangulated MAU with Higgsfield's actual demand baseline and separates consumer from Team/Enterprise | Sharpens Lever 1 per country |
| 2 | Today's free-to-paid conversion by country | Confirms the constrained-conversion baseline; quantifies the gap to close | Calibrates Lever 1 "today's conv" |
| 3 | Card authorization rate by country, issuer/BIN and decline reason (Stripe export) | Identifies recoverable cross-border declines vs hard declines and fraud; extends the 95.6% US/EU/AU benchmark to the other markets | Calibrates Lever 2 |
| 4 | Renewal and auto-refill failure rate, Stripe Smart Retries recovery, involuntary churn by country | Validates whether Higgsfield is at the ~38% default recovery baseline or already past it | Calibrates Lever 3 |
| 5 | Plan mix (Starter / Plus / Ultra, credit packs, auto-refill), Adaptive Pricing currencies, refunds, churn | Replaces the blended ARPU assumption ($240 EM / $300 DM) with actual per-country economics | Sharpens MRR across all levers |
| 6 | Risk, compliance, tax and MoR feasibility by market | Determines whether local entity, MoR or PSP-of-record is viable per market | Implementation path and sequencing |

---

## SLIDE 18: Section divider

**Title:** OUR COMMITMENT

---

## SLIDE 19: Two-week joint data sprint

**Kicker:** PROPOSED NEXT STEP
**Title:** A 2-week joint data sprint converts this strategic case into a Higgsfield-validated forecast

**WHAT WE RUN TOGETHER · 2 WEEKS**
- DAYS 1 to 3, Data exchange: Higgsfield shares country-level checkout starts, paid conversion, payment-method mix, decline codes and renewal failure data (Stripe exports). Yuno provides standardized templates.
- DAYS 4 to 7, Model calibration: replace Yuno's external estimates with Higgsfield's actual funnel data. Re-run all three lever sizings with country-specific parameters.
- DAYS 8 to 11, Implementation roadmap: sequence top markets by combined opportunity ÷ implementation effort. Identify 2 to 3 pilot countries and their priority methods.
- DAYS 12 to 14, Pilot scope and business case: joint paper with country-level forecast, MoR / processor / tax recommendations and a phased contract proposal.

**WHAT WE AIM TO GET DONE**
✓ Country-level monetization forecast across all three levers, calibrated against Higgsfield's actual funnel data
✓ Sequenced implementation roadmap with priority markets, payment methods and concrete provider recommendations (acquirers, MoRs, local PSPs)
✓ Pilot proposal for 2 to 3 countries (e.g., India + Brazil + Indonesia) with measurable conversion targets, expected MRR and contractual scope
✓ Risk-adjusted business case sized at Higgsfield's blended ARPU and country economics: board-grade input for payments-localization investment

**BOTTOM LINE:** Higgsfield keeps Stripe as the global baseline. Yuno orchestrates the localization layer around it, adding methods, routing locally and recovering failures, with all economics validated against Higgsfield's own data.

---

## SLIDE 20: 60-day BD sprint (the "distribution deals" slide)

**Kicker:** PROPOSED NEXT STEP
**Title:** Yuno deploys a full-time BD team for 60 days to secure wallet and distribution commitments across four regions, not just integration
**Intro:** Integration alone isn't enough. Many wallets only activate marketing, co-branding and full market support when the merchant has a direct relationship. Yuno's BD team builds those relationships on Higgsfield's behalf, securing commercial commitment, not just technical connectivity.

Four regional columns:
1. **LATIN AMERICA:** secure Pix Automático recurring commitment + Mercado Pago co-marketing for Higgsfield in Brazil, Mexico and Argentina; SPEI / OXXO activation.
2. **SOUTH ASIA:** UPI AutoPay mandate partnership with top banks and placement in Paytm / PhonePe; JazzCash / Easypaisa in Pakistan.
3. **EAST & SOUTHEAST ASIA:** Korea easy-pay completion (Toss, Samsung Pay) on top of Kakao / Naver / PayCo; Japan PayPay / Konbini activation; QRIS + GoPay / DANA in Indonesia; MoMo / ZaloPay in Vietnam.
4. **EUROPE / MENA:** PayPal enablement across UK, DE, ES, IT, NL, FR; iDEAL, Bizum, Satispay placement; UAE local acquirer contracts and Tabby / Tamara.

**What the 60-day sprint delivers:**
- WALLET COMMERCIAL COMMITMENTS: signed agreements with priority wallets per market, with marketing support, co-branding rights and preferred merchant status.
- GO-TO-MARKET READINESS: some wallets (GCash, Mercado Pago, Fawry) only promote a merchant if the integration is direct and the relationship is established; Yuno's BD team makes Higgsfield a named launch partner, not just another API merchant.
- LOCAL ACQUIRER CONTRACTS: pre-negotiated acquiring agreements in India, Brazil, Turkey, Mexico and the UAE for domestic card routing from day one.

**Closing:** This isn't a software demo followed by a handoff. Yuno puts a dedicated team in the field to make sure Higgsfield has full wallet support on day one.

---

## SLIDE 21: Section divider

**Title:** APPENDIX

---

## SLIDE 22: How to read the numbers in this deck

**Kicker:** APPENDIX · ASSUMPTIONS & METHODOLOGY

**WORKING ASSUMPTIONS**
- **Higgsfield MAU per country:** triangulated from SimilarWeb traffic share (122-country export) and a ~12M global MAU anchor (30M+ registered users per the Series B release, Aug 17 2026, at ~40% monthly active; cross-checked against ~32M monthly visits, SimilarWeb/Hypestat Aug 2026). Per-country range ±15% shown on each slide.
- **Free-to-paid conversion (today):** EM 0.5 to 1.5%; DM 2 to 3%. Anchored on OpenView SaaS Benchmarks and RevenueCat State of Subscription Apps. Note: the implied global paid base at 12M MAU and a ~$210M consumer pool is ~700K subscribers (~5.8%), so EM markets are assumed to convert well below the global average, which is what a card-only checkout would predict.
- **Free-to-paid conversion (with local methods):** EM full-stack +2.0pp (Pakistan +1.5pp); markets where Stripe already offers the main local method (Brazil Pix, Korea Kakao/Naver/PayCo, China WeChat Pay) +0.5 to +1.0pp; mature and APM-led markets +1.0pp. All below the xAI deck's lowest uplift (+2.5pp). Stripe's optimized-checkout study cites 7 to 12% average revenue lift; per-method examples include iDEAL +39%, BLIK +46%, PayPal DE +47%, Konbini +27%, SEPA DD +12%.
- **Blended ARPU:** EM markets $240/yr ($20/mo); DM markets $300/yr ($25/mo). Observed list prices (Sep 16 2026): Starter $19/mo, Plus $47/mo annual or $59 monthly, Ultra $99/mo annual or $129 monthly, plus credit packs and $20 to $300 auto-refill. Tier names changed at least twice in 2026; verify the live page before send.
- **Lever 2 decline gap:** cross-border decline rate 25% (EM), 15% (APM-led), 8% (DM); recoverable share 55% (EM), 40% (others); partial-year factor 0.685.
- **Lever 3 retry recovery:** monthly renewal failure 3.5% (EM) / 2.5% (DM); 40% of failed renewals rescued; average remaining value $120 (EM) / $150 (DM); 0.78 incrementality haircut. Recurly cites 5 to 7% monthly involuntary failure; Stripe Smart Retries recovers ~38% at default.

**SENSITIVITY (annualized hero)**
| Scenario | Total |
|---|---|
| Base case (12M MAU; EM +2.0pp, DM +1.0pp; ARPU $240/$300) | $25.6M |
| Downside uplift (EM +1.0pp, DM +0.5pp) | $15.3M |
| MAU 9M | $19.2M |
| MAU 16M (30M registered x ~53%) | $34.1M |
| Brief ARPU ($300 EM / $360 DM) | $31.5M |
| xAI-level uplift (EM +3.5pp, DM +3pp) | $58.3M |
| Everything at xAI/brief level + 16M MAU | $95.7M |

**CAVEATS & POSITIONING LANGUAGE**
- MAU is Yuno-triangulated: present as ranges and ask Higgsfield to validate against internal data.
- Levers are NOT additive: Lever 2 uses the post-Lever-1 paid base; Lever 3 uses the post-Lever-1+2 base.
- Recurring-native methods (UPI AutoPay, Pix Automático, SEPA DD) differ from acquisition-only methods (Konbini, OXXO, cash vouchers).
- Never state that Higgsfield lacks a method. Confirmed today (help center, Aug 1 2026): Visa, Mastercard, Amex, JCB, Apple Pay, bank payments where supported by Stripe; PayPal and cryptocurrency stated as not supported. Stripe materials add Link, Klarna, Affirm, Pix, Kakao Pay, Naver Pay, PayCo, WeChat Pay.
- Per-country sources are listed on each slide; commercial source estimates vary by year and methodology.

---

## SLIDES 23 to 40: Country slides (18 addressable markets, ordered by total opportunity)

**Template per slide (identical layout to OpenAI slides 21 to 40):** headline stat tiles (local audience · est. MAU · incremental paid subs · total impact), three lever boxes, PAYMENT METHOD PRIORITY table (Must-have / Must-have / Optional), BASE-CASE MODEL (today conv · with-LPM conv · uplift · ARPU), SO WHAT, source + TO VALIDATE line ("Higgsfield [country] MAU, checkout starts, current paid conversion, payment-method mix, decline codes").
**Stats marked (OA) are carried over from the OpenAI/xAI decks (Yuno research); re-verify date before send. Stats for the UK, Italy, Canada, UAE, China and Russia were verified on Sep 16 2026 and carry their source URL inline.**

### SLIDE 23: India: UPI is the largest audience-expansion lever in the portfolio
- Tiles: 504M+ UPI users, 84% of digital retail payments (OA) · ~1.5M est. MAU (1.3 to 1.7M) · ~30K incremental paid subs · ~31.5K total impact · ~$8.1M/yr total
- Lever 1: +~30K incremental paid subscribers · ~$7.2M/year. Lead with UPI for acquisition; UPI AutoPay for renewals.
- Lever 2: +~1.4K recovered card approvals · ~$0.23M/year. Localize card routing; support RuPay / local debit.
- Lever 3: +~550 renewals saved/month (~6.6K/yr) · ~$0.61M/year. Smart retries on AutoPay mandate failures.
- Method priority: Must-have UPI / UPI AutoPay (504M+ users; 84% of digital retail) · Must-have RuPay / local debit · Optional net banking, wallets (Paytm, PhonePe).
- Base case: today ~0.5% → with UPI ~2.5% (+2.0pp) · ARPU ~$240/yr.
- Higgsfield-specific line: India is Higgsfield's #2 market (12.54% of traffic). Neither Higgsfield's help center nor Stripe's published Higgsfield method list names an India-specific method; verify at checkout.
- SO WHAT: India's monetization path runs through UPI first; local card routing and AutoPay retries compound on top.
- Source: BCG / NPCI; SimilarWeb; Higgsfield help center.

### SLIDE 24: Indonesia: card share below 15% makes QRIS and wallets the only path to scale
- Tiles: QRIS mass-adopted, 39M merchants (OA) · ~0.35M MAU (0.29 to 0.40M) · ~6.9K incremental · ~7.3K total · ~$1.9M/yr
- L1 +~6.9K · ~$1.66M/yr (QRIS + GoPay/OVO/DANA/ShopeePay as primary acquisition) · L2 +~300 · ~$0.05M/yr (localize card routing; fallback for issuer declines) · L3 ~1.5K/yr · ~$0.14M/yr (provider redundancy across local PSPs)
- Method priority: QRIS (60M users; 39M merchants) · GoPay / OVO / DANA / ShopeePay · Optional VA / bank transfer (BI-FAST)
- Base case: 0.5% → 2.5% (+2.0pp) · ARPU $240
- SO WHAT: Indonesia is a mobile-wallet and local-rails market where card-only checkout under-monetizes existing demand (2.89% of Higgsfield traffic, #8).
- Source: Bank Indonesia; ASEAN Briefing; Adyen.

### SLIDE 25: United Kingdom: PayPal, Open Banking and wallets lift a strong card market
- Tiles: 351M Open Banking payments in 2025 (+57% YoY); 16.5M user connections (OBL, Jan 2026) · ~0.45M MAU (0.38 to 0.52M) · ~4.5K incremental · ~5.0K total · ~$1.7M/yr
- L1 +~4.5K · ~$1.35M/yr (PayPal + Open Banking pay-by-bank + Apple/Google Pay) · L2 +~500 · ~$0.10M/yr (local GBP acquiring, SCA-aware routing) · L3 ~2.2K/yr · ~$0.26M/yr (retries + provider fallback)
- Method priority: PayPal / e-wallets (e-wallets 35% of UK e-commerce transactions, cards 46%, PPRO) · Open Banking pay-by-bank (40.1M payments in June 2026; 1B+ cumulative; OBL via PYMNTS) · Optional Apple Pay / Google Pay (Apple Pay already live; 65% of UK adults registered for a mobile payment service, UK Finance 2025)
- Base case: 3.0% → 4.0% (+1.0pp) · ARPU $300
- Higgsfield-specific: help center states PayPal is not supported; the UK is Higgsfield's #4 market (3.76%).
- SO WHAT: The UK is a preferred-method and renewal-recovery market, not a card-access problem (debit cards are more than half of all UK payments, UK Finance).
- Source: Open Banking Limited (Jan 29 2026): https://www.openbanking.org.uk/insights/open-banking-in-2025-now-part-of-the-uks-everyday-financial-life/ · PYMNTS citing OBL (Jul 28 2026) · UK Finance (Aug 19 2026): https://www.ukfinance.org.uk/news-and-insight/press-release/digital-payments-continue-grow-mobile-wallets-become-more-popular · PPRO UK.

### SLIDE 26: Germany: PayPal, SEPA Direct Debit and invoice/BNPL make card-only checkout suboptimal
- Tiles: PayPal +47% conversion lift in DE digital media (Stripe, OA) · ~0.40M MAU (0.34 to 0.46M) · ~4.0K incremental · ~4.4K total · ~$1.5M/yr
- L1 +~4.0K · ~$1.21M/yr (PayPal + SEPA DD as primary recurring rails) · L2 +~400 · ~$0.09M/yr (EU domestic processing strong; limited uplift) · L3 ~2.0K/yr · ~$0.23M/yr (retry timing, SCA management, provider fallback)
- Method priority: PayPal (+47% lift, Stripe) · SEPA Direct Debit (+12% EU lift, Stripe) · Optional Klarna / invoice (Klarna already live), Apple / Google Pay
- Base case: 3.0% → 4.0% (+1.0pp) · ARPU $300
- Higgsfield-specific: Regional GTM Director Germany role posted Jul 2026; /de locale exists in code but is gated off.
- SO WHAT: Germany's opportunity is preferred local methods plus recovery logic, not card acceptance.
- Source: Trade.gov; Stripe; Bitkom.

### SLIDE 27: Turkey: domestic card scheme + FX-aware processing matter more than global cards
- Tiles: 67M TROY cards; 23M+ Papara users (OA) · ~0.24M MAU (0.20 to 0.27M) · ~4.7K incremental · ~5.1K total · ~$1.3M/yr
- L1 +~4.7K · ~$1.13M/yr (TROY + local installments; Papara / BKM tactically) · L2 +~400 · ~$0.07M/yr (local acquiring for TROY and local debit/credit) · L3 ~1.3K/yr · ~$0.12M/yr
- Method priority: TROY (67M cards, ~20% of card txns) · local installments · Optional Papara, Tosla, BKM / FAST
- Base case: 1.0% → 3.0% (+2.0pp) · ARPU $240
- SO WHAT: Turkey is a localization market where local card behavior, FX-friendly processing and retries combine.
- Source: Papara; BKM; Daily Sabah.

### SLIDE 28: Brazil: Pix is live; Pix Automático and local acquiring finish the job
- Tiles: 170M+ Pix consumers, ~40% of e-commerce (OA) · ~0.39M MAU (0.33 to 0.45M) · ~3.9K incremental · ~5.0K total · ~$1.3M/yr
- L1 +~3.9K · ~$0.94M/yr (Pix Automático as subscription-grade rail; installments) · L2 +~1.1K · ~$0.18M/yr (move card volume to local BRL acquiring / MoR; cross-border BR cards are the largest decline gap in the portfolio) · L3 ~1.8K/yr · ~$0.17M/yr (fallback PSP routing across local providers)
- Method priority: Pix / Pix Automático (Pix already live via Stripe) · local cards & installments · Optional Boleto
- Base case: 1.5% → 2.5% (+1.0pp, deliberately half the EM uplift because Pix already exists) · ARPU $240
- Higgsfield-specific: Trustpilot (Sep 2026) shows a Brazilian double-charge report; Brazil is #7 by traffic (3.26%).
- SO WHAT: Brazil is a full-stack market where Higgsfield already has reach through Pix; the upside is approval (local acquiring) and renewal recovery.
- Source: BCG / NPCI; Stripe customer story; Trustpilot.

### SLIDE 29: Spain: Bizum is the local APM to test alongside PayPal and retries
- Tiles: Bizum 28.8M users (Apr 2025); 1.24B operations 2025, +82% online YoY (OA) · ~0.28M MAU (0.24 to 0.32M) · ~2.8K incremental · ~3.1K total · ~$1.05M/yr
- L1 +~2.8K · ~$0.83M/yr (Bizum on mobile checkout + PayPal) · L2 +~300 · ~$0.06M/yr · L3 ~1.4K/yr · ~$0.16M/yr (retries, SCA handling, provider redundancy)
- Method priority: Bizum (28.8M users) · PayPal, cards · Optional SEPA Direct Debit
- Base case: 3.0% → 4.0% (+1.0pp) · ARPU $300
- Higgsfield-specific: the /es locale is live and its code targets 19 Spanish-speaking LatAm countries, so Spain also anchors the Spanish-language funnel.
- SO WHAT: Spain is a medium-effort European quick win, not a large local-processing gap.
- Source: Stripe; Bank of Spain.

### SLIDE 30: Vietnam: QR + bank transfer + wallets define digital payment expectations
- Tiles: MoMo 31M+ active; ~40% wallet share; QR payments +106% YoY (OA) · ~0.20M MAU (0.17 to 0.22M) · ~3.9K incremental · ~4.1K total · ~$1.05M/yr
- L1 +~3.9K · ~$0.94M/yr (MoMo / ZaloPay / ShopeePay + VietQR / NAPAS) · L2 +~200 · ~$0.03M/yr · L3 ~900/yr · ~$0.08M/yr (annual / prepaid where wallet recurring is constrained)
- Method priority: MoMo / ZaloPay / ShopeePay · VietQR / NAPAS · Optional bank transfer / local cards
- Base case: 0.5% → 2.5% (+2.0pp) · ARPU $240
- SO WHAT: Vietnam's opportunity is to align checkout with fast-growing QR / account-based payment behavior (1.63% of traffic, #14).
- Source: GAJRC; market reports.

### SLIDE 31: South Korea: easy-pay is live; completing the ecosystem and local acquiring is the play
- Tiles: Naver Pay 30.7M users, 24% share (2024) (OA) · ~0.45M MAU (0.38 to 0.51M) · ~2.2K incremental · ~3.0K total · ~$1.0M/yr
- L1 +~2.2K · ~$0.67M/yr (add Toss and Samsung Pay on top of Kakao Pay, Naver Pay, PayCo, which are already live via Stripe) · L2 +~800 · ~$0.16M/yr (local KRW card acquiring) · L3 ~1.7K/yr · ~$0.20M/yr (subscription retry + token management)
- Method priority: Naver Pay / Kakao Pay / PayCo (live) · Toss / Samsung Pay (add) · Optional local cards
- Base case: 2.5% → 3.0% (+0.5pp, the lowest uplift in the deck because the main wallets already exist) · ARPU $300
- Higgsfield-specific: Korea is a top-five market by users (VentureSquare, Aug 25 2026); Mirae Asset Capital is a strategic investor; APAC GTM org being built.
- SO WHAT: South Korea is not a wallet-coverage problem anymore; it is a local-acquiring and renewal-continuity problem at high ARPU.
- Source: Antom; KISDI; Stripe customer story; VentureSquare.

### SLIDE 32: Italy: PayPal, Satispay and domestic rails beyond cards
- Tiles: Satispay 6.5M users, 450K+ merchants (May 2026); e-wallets 35% of Italian e-commerce transactions (PPRO) · ~0.26M MAU (0.22 to 0.30M) · ~2.6K incremental · ~2.9K total · ~$1.0M/yr
- L1 +~2.6K · ~$0.79M/yr (PayPal + Satispay) · L2 +~300 · ~$0.06M/yr (local EUR acquiring) · L3 ~1.3K/yr · ~$0.15M/yr
- Method priority: PayPal / e-wallets (35% of e-com transactions vs cards 31%, PPRO) · Satispay (6.5M users; 450K+ merchants; EU-Startups Jun 2026) · Optional BANCOMAT Pay / PostePay / MyBank; BNPL EUR 9.9B in 2025, +45% (PoliMi)
- Base case: 3.0% → 4.0% (+1.0pp) · ARPU $300
- SO WHAT: Italy converts on trusted domestic methods (digital payments EUR 518B in 2025, +7%; ~14M Italians paid by smartphone, PoliMi); PayPal absence is the visible gap.
- Source: Osservatorio Innovative Payments, Politecnico di Milano (Mar 12 2026): https://www.osservatori.net/comunicato/innovative-payments/pagamenti-digitali-in-italia-mercato/ · EU-Startups (Jun 11 2026) · PPRO Italy.

### SLIDE 33: France: Cartes Bancaires routing + PayPal / SEPA make renewals the play in a strong card market
- Tiles: 73M+ CB cards; CB ≈ 60% of domestic card volume (OA) · ~0.24M MAU (0.21 to 0.28M) · ~2.4K incremental · ~2.7K total · ~$0.9M/yr
- L1 +~2.4K · ~$0.73M/yr (accept PayPal / SEPA) · L2 +~300 · ~$0.05M/yr (route via Cartes Bancaires local acquiring) · L3 ~1.2K/yr · ~$0.14M/yr (smart retries + SEPA DD for renewals)
- Method priority: Cartes Bancaires (73M+ cards) · PayPal / SEPA DD · Optional Apple Pay / Paylib
- Base case: 3.0% → 4.0% (+1.0pp) · ARPU $300
- Higgsfield-specific: Regional GTM Director France role posted Jul 2026.
- SO WHAT: France is a strong card market; the upside is CB routing, PayPal / SEPA and renewal recovery, not new rails.
- Source: Groupement CB; Banque de France.

### SLIDE 34: Canada: Interac and PayPal complete a card-heavy market
- Tiles: Interac e-Transfer 1.4B+ transactions worth $554B in 2024; 88% of Canadians have used it (Interac) · ~0.24M MAU (0.21 to 0.28M) · ~2.4K incremental · ~2.7K total · ~$0.9M/yr
- L1 +~2.4K · ~$0.72M/yr (Interac e-Transfer / Interac Debit online + PayPal) · L2 +~300 · ~$0.05M/yr (local CAD acquiring) · L3 ~1.2K/yr · ~$0.14M/yr
- Method priority: PayPal / e-wallets (27% of e-com transactions vs cards 52%, PPRO) · Interac e-Transfer / Interac Debit (online transfers +16% volume YoY; 6.5B Interac Debit transactions a year) · Optional Apple / Google Pay
- Base case: 3.0% → 4.0% (+1.0pp) · ARPU $300
- SO WHAT: Canada is a preferred-method market (credit 33%, debit 30%, EFT 14%, online transfer 7% of 2024 retail transactions, Payments Canada); local CAD processing, Interac and PayPal are the whole play.
- Source: Interac (Sep 16 2025): https://www.interac.ca/en/content/news/interac-broadens-access-to-interac-e-transfer-for-payment-service-providers-under-new-federal-framework/ · Payments Canada CPMT 2025 fact sheet · PPRO Canada.

### SLIDE 35: Mexico: cross-border card decline + cash-to-digital gap together suppress conversion
- Tiles: 21% bank transfer + 21% e-wallet share of e-commerce (OA) · ~0.16M MAU (0.14 to 0.18M) · ~3.2K incremental · ~3.5K total · ~$0.9M/yr
- L1 +~3.2K · ~$0.77M/yr (SPEI, OXXO Pay, Mercado Pago for non-card acquisition) · L2 +~300 · ~$0.05M/yr (local debit / MXN acquiring) · L3 ~900/yr · ~$0.08M/yr
- Method priority: local debit / domestic cards · SPEI (21% of e-commerce) · Optional OXXO Pay, Mercado Pago
- Base case: 1.0% → 3.0% (+2.0pp) · ARPU $240
- SO WHAT: Mexico combines local payment-method coverage with meaningful card-approval upside (1.33% of traffic, #19; anchors the Spanish-language LatAm funnel).
- Source: PPRO; PCMI; Adyen.

### SLIDE 36: Netherlands: iDEAL is table stakes for Dutch online conversion
- Tiles: iDEAL ~70% of online payments; cards ~14% (OA) · ~0.19M MAU (0.17 to 0.22M) · ~1.9K incremental · ~2.1K total · ~$0.7M/yr
- L1 +~1.9K · ~$0.58M/yr (iDEAL + PayPal) · L2 +~200 · ~$0.04M/yr · L3 ~1.0K/yr · ~$0.11M/yr (SEPA DD + retries)
- Method priority: iDEAL (~70%) · SEPA Direct Debit · Optional PayPal, cards
- Base case: 3.0% → 4.0% (+1.0pp) · ARPU $300
- SO WHAT: A card-only flow asks Dutch users to abandon their default online payment behavior.
- Source: Dutch Payments Association; Stripe.

### SLIDE 37: United Arab Emirates: local AED acquiring and wallets on a high-ARPU base
- Tiles: Cards 52%, e-wallets 24% of UAE e-commerce; m-commerce 60%+; cross-border 37% of e-commerce (PPRO) · ~0.19M MAU (0.16 to 0.22M) · ~1.9K incremental · ~2.1K total · ~$0.7M/yr
- L1 +~1.9K · ~$0.57M/yr (Apple Pay already live; add Tabby / Tamara and local wallets) · L2 +~300 · ~$0.05M/yr (local AED acquiring; issuer-friendly routing) · L3 ~700/yr · ~$0.08M/yr
- Method priority: local AED card acquiring incl. the Jaywan domestic scheme (inaugurated Jul 2026; added to Network International's e-com gateway, Gulf News) · Apple Pay (live) · Optional Tabby / Tamara (BNPL)
- Base case: 2.0% → 3.0% (+1.0pp) · ARPU $300
- SO WHAT: The UAE is a local-processing market at high purchasing power; cards work, but locally, and 37% of e-commerce is already cross-border, so issuers are used to foreign merchants but reward domestic routing.
- Source: PPRO UAE: https://www.ppro.com/countries/united-arab-emirates/ · Gulf News (Jul 20 2026): https://gulfnews.com/business/banking/uae-rolls-out-jaywan-the-first-national-payment-card-banks-launch-new-schemes-1.500614102 · Wikipedia, Jaywan.

### SLIDE 38: Japan: high card penetration does not remove the need for local methods
- Tiles: PayPay 70M+ registered users (Jul 2025); cashless ratio 42.8% (2024) (OA) · ~0.18M MAU (0.16 to 0.21M) · ~1.8K incremental · ~2.0K total · ~$0.66M/yr
- L1 +~1.8K · ~$0.55M/yr (add PayPay; Konbini for first purchase / rescue) · L2 +~100 · ~$0.03M/yr (JCB local routing; JCB already accepted) · L3 ~700/yr · ~$0.08M/yr (retry timing on renewals)
- Method priority: PayPay (70M+) · Konbini · Optional Rakuten Pay, carrier billing
- Base case: 2.0% → 3.0% (+1.0pp) · ARPU $300
- Higgsfield-specific: Japan is a top-five market by users (VentureSquare); NTT DOCOMO Ventures is a strategic investor; /ja locale is live.
- SO WHAT: Japan is a method-trust market: local payment familiarity lifts conversion even when cards are available.
- Source: PayPay; METI; VentureSquare.

### SLIDE 39: Pakistan: Raast, mobile wallets and local debit are the unlocks in a debit-heavy market
- Tiles: JazzCash 20.6M MAU; Easypaisa 55M+; 90% of cards are debit (OA) · ~0.15M MAU (0.13 to 0.18M) · ~2.3K incremental · ~2.4K total · ~$0.62M/yr
- L1 +~2.3K · ~$0.55M/yr (Raast + JazzCash / Easypaisa) · L2 +~100 · ~$0.02M/yr (prioritize debit acceptance) · L3 ~500/yr · ~$0.05M/yr (failed-card rescue methods)
- Method priority: JazzCash / Easypaisa · Raast (instant A2A) · Optional PayPak / local debit (61M+ cards)
- Base case: 0.5% → 2.0% (+1.5pp) · ARPU $240
- Higgsfield-specific: a Pakistani subscriber reported being locked out for card re-verification three days after buying a Max plan (Trustpilot, Sep 13 2026).
- SO WHAT: Pakistan's opportunity is to move beyond card-only monetization through wallets and instant rails.
- Source: Jazz; State Bank of Pakistan; Trustpilot.

### SLIDE 40: China: WeChat Pay is live; Alipay completes cross-border wallet coverage
- Tiles: Weixin + WeChat 1,414M MAU (Tencent, Sep 30 2025); e-wallets 65% of Chinese e-commerce transactions (PPRO) · ~0.19M MAU (0.16 to 0.21M) · ~900 incremental · ~1.0K total · ~$0.26M/yr
- L1 +~900 · ~$0.22M/yr (add Alipay alongside WeChat Pay, cross-border) · L2 +~100 · ~$0.01M/yr · L3 ~300/yr · ~$0.03M/yr
- Method priority: WeChat Pay (live via Stripe) · Alipay (add; Alipay and WeChat Pay are the two dominant wallets, PPRO) · Optional UnionPay SecurePay
- Base case: 0.5% → 1.0% (+0.5pp) · ARPU $240
- SO WHAT: China is a cross-border wallet market for a US merchant; the play is completeness, not entry. Smallest opportunity in the deck; keep as one slide or fold into the table.
- Source: Tencent Q3 2025 results (Nov 13 2025): https://www.prnewswire.com/apac/news-releases/tencent-announces-2025-third-quarter-results-302614403.html · PPRO China.

---

## SLIDE 41: Lever 1 country ranking

**Kicker:** LEVER 1 · COUNTRY RANKING
**Title:** Top Lever 1 markets are driven by incremental paid users unlocked through local payment methods
**Sub:** The largest markets combine high Higgsfield demand, low current monetization and strong conversion uplift when local methods are enabled.

| # | Country | Higgsfield MAU | Today conv. | With-LPM conv. | Incremental paid users | Lever 1 MRR |
|---|---|---|---|---|---|---|
| 1 | India | 1.50M | 0.5% | 2.5% (+2.0pp) | 30.1K | $0.60M |
| 2 | Indonesia | 0.35M | 0.5% | 2.5% (+2.0pp) | 6.9K | $0.14M |
| 3 | United Kingdom | 0.45M | 3.0% | 4.0% (+1.0pp) | 4.5K | $0.11M |
| 4 | Germany | 0.40M | 3.0% | 4.0% (+1.0pp) | 4.0K | $0.10M |
| 5 | Turkey | 0.24M | 1.0% | 3.0% (+2.0pp) | 4.7K | $0.09M |
| 6 | Brazil | 0.39M | 1.5% | 2.5% (+1.0pp) | 3.9K | $0.08M |
| 7 | Vietnam | 0.20M | 0.5% | 2.5% (+2.0pp) | 3.9K | $0.08M |
| 8 | Spain | 0.28M | 3.0% | 4.0% (+1.0pp) | 2.8K | $0.07M |
| 9 | Italy | 0.26M | 3.0% | 4.0% (+1.0pp) | 2.6K | $0.07M |
| 10 | Mexico | 0.16M | 1.0% | 3.0% (+2.0pp) | 3.2K | $0.06M |
| 11 | France | 0.24M | 3.0% | 4.0% (+1.0pp) | 2.4K | $0.06M |
| 12 | Canada | 0.24M | 3.0% | 4.0% (+1.0pp) | 2.4K | $0.06M |
| 13 | South Korea | 0.45M | 2.5% | 3.0% (+0.5pp) | 2.2K | $0.06M |
| 14 | Netherlands | 0.19M | 3.0% | 4.0% (+1.0pp) | 1.9K | $0.05M |
| 15 | United Arab Emirates | 0.19M | 2.0% | 3.0% (+1.0pp) | 1.9K | $0.05M |
| 16 | Japan | 0.18M | 2.0% | 3.0% (+1.0pp) | 1.8K | $0.05M |
| 17 | Pakistan | 0.15M | 0.5% | 2.0% (+1.5pp) | 2.3K | $0.05M |
| 18 | China | 0.19M | 0.5% | 1.0% (+0.5pp) | 0.9K | $0.02M |
| | **PORTFOLIO TOTAL** | 6.06M | ~1.7% | ~3.1% (+1.4pp) | **~83K** | **~$1.8M/mo** |

**Tiles:** LEVER 1 PORTFOLIO ~83K incremental paid subscribers · ~$1.8M/mo base case · CONCENTRATION: top 3 markets ~48% (India · Indonesia · UK), top 10 ~79%.

---

## SLIDE 42: Levers 2 and 3, targeted upside

**Kicker:** LEVERS 2 + 3 · TARGETED UPSIDE
**Title:** Levers 2 and 3 are targeted optimization layers
**Sub:** They matter most where users already have payment intent, but card authorization or renewal continuity fails.

Two columns:
- **Lever 2, recovered cross-border declines: ~7K subscribers/yr · ~$1.3M/yr.** Largest in India (1.4K), Brazil (1.1K), South Korea (800), UK (500). Full-stack EM markets carry a 25% cross-border decline assumption vs 8% in mature markets. Higgsfield's own help center already coaches declined customers to ask their bank to allow international charges.
- **Lever 3, saved renewals and auto-refills: ~27K renewals/yr · ~$2.8M/yr.** Largest in India (6.6K), UK (2.2K), Germany (2.0K), Brazil (1.8K), South Korea (1.7K). Stripe retries automatically today with a ~14-day cure window; cross-PSP retries and token refresh add recovery on top. Auto-refill packs ($20 to $300) are off-session stored-credential charges and sit inside this lever.

---

## SLIDE 43: Divider, LEVER 1

**Title:** LEVER 1 · Audience expansion through local payment methods · ~$1.8M/mo · ~$21M annualized · ~83K incremental paid subscribers

## SLIDE 44: Lever 1 methodology

**Title:** Lever 1 sizing: how local payment methods convert existing Higgsfield users into paid subscribers
**Formula:** MAU in priority markets x incremental conversion uplift (pp) x blended ARPU ($/yr) → 6.06M x ~1.4pp blended (2.0pp EM, 1.0pp mature, 0.5pp where the main local method is already live) x $240 to $300 → ~83K subscribers · ~$21.4M/yr.
**Inputs to validate:** MAU by country; checkout starts; today's conversion; method mix at checkout (Stripe export).

## SLIDE 45: Divider, LEVER 2

**Title:** LEVER 2 · Authorization uplift through localized card processing · ~$0.11M/mo · ~$1.3M annualized · ~7K recovered subscribers

## SLIDE 46: Lever 2 methodology

**Title:** Lever 2 sizing: how local processing turns failed card attempts into paid subscribers
**Formula:** current paid subs / (1 − decline rate) = implied attempts → declined = attempts − subs → recovered = declined x local-acquiring recovery rate → x ARPU x 0.685 partial-year factor. Decline rate 25% / 15% / 8% and recovery 55% / 40% by archetype. ~102K current paid subs in the 18 markets → ~7K recovered → ~$1.3M/yr.
**Inputs to validate:** authorization rate by country, BIN and decline reason; 3DS outcomes.

## SLIDE 47: Divider, LEVER 3

**Title:** LEVER 3 · Subscription continuity through retries and redundancy · ~$0.24M/mo · ~$2.8M annualized · ~27K renewals saved annually

## SLIDE 48: Lever 3 methodology

**Title:** Smart retries and provider redundancy recover failed renewals: recurring revenue that compounds annually
**Formula:** post-uplift subscriber base (102K + 83K + 7K = ~192K) x monthly renewal failure (3.5% EM / 2.5% DM) x 12 x 40% rescued x average remaining value ($120 EM / $150 DM) x 0.78 incrementality haircut → ~27K renewals saved · ~$2.8M/yr.
**Inputs to validate:** renewal and auto-refill failure rate, Stripe Smart Retries recovery, involuntary churn by country.

## SLIDE 49: Thank you

**Title:** THANK YOU
**Contact:** German Tatis · Account Executive · german.tatis@y.uno

---

## A. Auditoría número por número contra el brief de Justo

| Dato en el brief | Qué usé en el deck | Por qué |
|---|---|---|
| 22M+ users, 240+ countries | 30M+ users, 238 countries and territories | Cifra más reciente, declarada por la empresa (Series B PR, 17-ago-2026) |
| Diffuse mobile app como superficie de producto | Eliminado | Help center oficial: "Higgsfield has no mobile apps and no desktop app" (verificado 16-sep-2026) |
| ARR $700M (Jul/Ago 2026) | $700M annualized revenue (Aug 17 2026) | Verificado en el PR |
| ~70% enterprise / ~30% consumer → pool $210M | Mantenido, etiquetado [ESTIMATE] | MasterNodeAI citando The Information (2-jul-2026: "approximately 70%"); FT vía ContentGrip (ago-2026: mayoría B2B) |
| Traffic: US 18.6%, India 9.0%, KR 4.7%, UK 3.7%, DE 3.3% | Tu tabla de SimilarWeb (122 países): US 15.13%, India 12.54%, RU 3.82%, UK 3.76%, KR 3.71%, DE 3.35%, BR 3.26%... | Es tu fuente directa y cubre los 20; falta confirmar el periodo |
| MAU 12M | 12M (mantenido) | Coherente con 30M+ registrados x ~40% y ~32M visitas/mes |
| 4M MAU en mercados prioritarios (India 2.0M, BR 0.9M, MX 0.5M, ID/SEA 0.4M, otros 0.2M) | 6.06M en 18 mercados con reparto real por tráfico (India 1.50M, BR 0.39M, MX 0.16M, ID 0.35M...) | El brief sobreestimaba Brasil y México y omitía UK/DE/KR; el modelo usa tus shares reales |
| Uplift 2.0pp uniforme | 2.0pp EM; 1.5pp Pakistán; 1.0pp maduros/UAE; 0.5pp Brasil-Pix, Corea y China | Stripe ya ofrece Pix, Kakao/Naver/PayCo y WeChat Pay a Higgsfield: no se puede prometer el mismo salto ahí |
| ARPU $300 blended | $240 EM / $300 DM | Más conservador; los precios observados ($19 a $129/mes) lo soportan |
| Hero $35M (rango $30 a $40M) | ~$25M (rango $20 a $30M) | Resultado del modelo por país; Justo pidió más conservador que OpenAI; con los inputs del brief da $31.5M, con inputs xAI $58M (tabla de sensibilidad) |
| Lever 4 (credit reloads) | Narrativa en slide 42 (auto-refill dentro de Lever 3), sin número | Como recomendaba el brief |
| "Stripe acquired Metronome and Orum" | No se usa | No lo verifiqué; no hace falta para el argumento |
| Pricing: Basic $9 / Starter $15 a 19 / Plus $49 a 59 / Ultra $129 / Ultra 6K-9K / Team $65 | Solo lo observado el 16-sep-2026 (Starter $19, Plus $47/$59, Ultra $99/$129) con nota de verificación | Los trackers se contradicen y los nombres cambiaron 2 veces en 2026 |
| Korea/Japan "card-heavy, excluir de local rails" | Incluidos como Mature/APM-led con uplift bajo (0.5 a 1.0pp) | Están en tu top 20 y Corea/Japón son top-5 por usuarios (VentureSquare); excluirlos dejaba huecos en la tabla |
| Semrush: "users go to stripe.com after higgsfield.ai" como señal de PSP | Reemplazado por Terms of Use 9.1 + help center + case study de Stripe | Evidencia primaria, no inferencia |

## B. Decisiones que tomé (cámbialas si quieres)

1. **US y Rusia en la tabla top 20 sin MRR.** US = baseline (Stripe se queda), Rusia = no direccionable. Alternativa: reemplazarlos por los rangos 21 y 22 de tu export.
2. **18 slides país, no 20.** Consecuencia de lo anterior.
3. **Competidor en el slide de "cost of delay":** genérico ("a localized competitor") con Google/Veo y Kling como ejemplos, porque Kuaishou (Kwai/Snack Video) está bloqueado en India desde 2020 y no quiero un dato atacable.
4. **Nova fraud sin el "75%"** del deck de Bending Spoons; lo atamos al problema real (BBB F, 27 quejas, cargos no reconocidos).
5. **Competidor del slide 4 reformulado:** en lugar de "Kling toma tus usuarios", el argumento verificado es "nadie en AI video ha localizado el checkout (Kling global = USD vía Stripe) y la distribución ya se mueve (Google + Jio, ChatGPT Go + UPI)". Kwai y Snack Video están bloqueados en India desde 2020 (PIB), así que Kling en India no es un dato defendible.
6. **Reconciliation** aparece como módulo con nota "confirm GA status" (memoria: roadmap sep-2026).
7. **Impacto esperado:** +7% approval uplift y 30% recovered revenue (publicados), no +12% / 20 a 30%.

## C. Inputs que debes confirmar antes de enviar

1. Periodo de tu tabla de SimilarWeb (¿últimos 3 meses? ¿agosto 2026?) para el footnote, y si puedes, el export CSV con los rangos 21 a 40.
2. Con Justo: redacción exacta de "Taxes" (¿MoR/PSP-of-record por mercado? ¿cálculo de impuestos vía partner?) y qué significa "distribution deals" en su cabeza (yo lo mapeé al slide 20 de BD de 60 días + la tarjeta del slide 7).
3. Logos de referencia aprobados para un prospecto de AI/creator (deck OpenAI no los usa; el slide 7 los pide en la barra negra de partners, no de clientes).
4. Destinatario: Alex Mashrabov (CEO) o Shotan Jakupov (Data & Growth Lead, citado por Stripe). Cambia el tono del slide 19.
5. ¿Mantener slide 40 (China, $0.26M) o plegarlo a la tabla?
6. Verificar el día del envío: página de pricing en vivo y lista de modelos en higgsfield.ai (el bundle Gemini+Jio y ChatGPT Go ya quedaron verificados el 16-sep-2026).
