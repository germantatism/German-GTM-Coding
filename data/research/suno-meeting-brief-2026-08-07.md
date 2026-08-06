# Meeting Brief: Yuno <> Suno (Aug 7, 2026)

**Meeting:** "Suno & Yuno" · Friday, August 7, 2026 · 2:00 to 2:30 PM Colombia (3:00 PM ET) · Google Meet: https://meet.google.com/vze-qree-sfw · Organizer: Justo Benetti (CRO). All four attendees accepted.

**Objective (what winning looks like):** Convert an inbound discovery call into a scheduled technical deep-dive (45 to 60 min with Gurwinder) plus a data-driven assessment offer, within the next 2 weeks, while establishing German and Justo as Madden's most useful outside advisors in week one of the job.

**⚠️ Pre-meeting actions:**
1. ⚠️ Open both LinkedIn profiles manually to confirm current Suno titles (neither is public yet): https://www.linkedin.com/in/madden-t-2378aa38/ and https://www.linkedin.com/in/gurwindergulati
2. ⚠️ Align with Justo before the call: (a) which AI-company references are usable in the room (the June email to Suno name-dropped xAI, OpenAI and Lovable; be ready to back or soften), (b) breach posture: NEVER raise Suno's data breach first, and (c) who leads which section.
3. ⚠️ Do not re-send the existing business case (deck.y.uno/sunobc, also the pptx). Its numbers are stale: it cites $250M Series C / $2.45B / $200M ARR, all superseded. Refresh before any re-share.
4. ⚠️ Jasper van Rijckevorsel (the original contact, Music + Engineering) is not on this invite. Do not add anyone. After the call, send Jasper a short thank-you note referencing that the payments conversation is now live.

Evidence labels: ✅ verified · ⚠️ inference or unconfirmed (never state in the call) · 🔍 ask in discovery.

---

## 1. TL;DR BATTLE CARD

**Five facts to know cold:**
1. **This meeting is inbound.** Madden Titus WhatsApped Justo yesterday (Aug 6), named "payment orchestration" unprompted, wrote "I am only 3 days in and don't know what I don't know", and asked for the call. ✅
2. **The stack:** Stripe is Suno's sole direct processor (their own ToS: "SUNO DOES NOT PROCESS PAYMENT FOR ANY SERVICES"; help center: "our direct billing processor (Stripe)"), plus Apple IAP and Google Play as separate mobile rails. 17 billing currencies, subscriptions in 36 countries, one US legal entity, no orchestrator. Their own help center: "Options not yet available with our direct processor may be available on mobile." ✅
3. **The scale:** $300M ARR and 2M paid subscribers (Feb 2026, CEO statement), $5.4B valuation after a $400M+ Series D led by Bond Capital (Jun 2026), and reported IPO-readiness moves (first audit, Controller ex-Crunchyroll, Jul 2026). ✅
4. **2026 payment catalysts:** licensed models replace current ones under the Warner deal, adding paid download overages on top of subscriptions; the Spark program already pays cash grants to artists (payout rails incoming); international expansion is staffed (Gourab Ghose, Head of International Markets, ex-Snap India, Mumbai-based). ✅
5. **Payment pain is public:** BBB rating F (93 complaints, 89 unanswered), recurring "card declined but bank shows funds" reviews, and a documented cottage industry of workarounds for subscribers in Nigeria, India, Ghana, Pakistan, the Philippines. Sensitive context: a Nov 2025 breach (disclosed Jul 2026) exposed 55.3M emails and tens of thousands of Stripe payment records; class action filed Jul 24, 2026. ✅

**Three hooks, in priority order:**
1. **Madden's own thesis, played back.** At Netflix Madden co-presented "Shining a Light on the Transaction Lifecycle" (with Vantiv and Mastercard): false declines come from misaligned incentives and "inconsistent access to data and disconnected fraud strategies" across the payment chain. Yuno is the unified data-and-routing layer that fixes exactly that. Reference it as an operator, not as flattery. ✅
2. **The map as the gift.** Madden said "I don't know what I don't know." Hand over the outside-in map: one rail carrying 17 currencies, Brazil/Germany/Japan billed cross-border from a US entity, three disconnected billing rails (Stripe, Apple, Google), and the renewal math: at roughly 24M renewals a year, one point of approval is roughly $3M a year (derived, labeled). ✅
3. **Payouts plus new SKUs land in 2026.** Spark grants and Warner opt-in artist licensing mean money starts flowing out while paid download overages multiply pay-in transactions. Yuno orchestrates pay-in and payout through one API (GoFundMe is the live marketplace reference: splits, recipients, transfers across Stripe, Adyen, Tabapay; ask permission before sharing deal details). ✅

**THE objection they will raise: build-vs-buy** (Gurwinder led Uber One membership payments; Uber built orchestration in-house).
**The answer:** Uber-grade in-house orchestration took years and dedicated payments teams that Suno does not have and is not hiring (their board shows 8 open roles, all model/product engineering; ~200 employees total scaling to ~340). Yuno keeps Stripe, adds routing, retries, vault, reconciliation and connector maintenance as a product, live in weeks. The engineering Suno does have is needed for the 2026 licensed-model migration. And Yuno publicly supports Uber itself among its named brands, which Gurwinder can validate directly.

**The ask (next step to land):** a 45 to 60 min technical session next week with Gurwinder (API and sandbox walkthrough, architecture on top of Stripe) plus an approval-rate assessment by market using their data under NDA. Secondary ask: Madden shares how the evaluation will run so Yuno can map to it.

**Rapport opener:** Madden's own joke back: "You said our names rhyme and are one syllable off, so this meeting was clearly inevitable." Optionally the Suno-made song about Yuno from the June email (João's track) as a light moment. Congratulate day 4 on the job.

---

## 2. WHO IS IN THE ROOM

| Name | Role | Side | Status / history |
|---|---|---|---|
| Madden Titus | Payments leadership at Suno, exact title ⚠️ not public, started ~Aug 3, 2026 | Suno | Inbound requester (WhatsApp to Justo, Aug 6). German emailed Madden at Disney in Sept 2025 (Stripe Tour NY invite, no reply); do not reference that. |
| Gurwinder Singh Gulati | Payments/platform engineering at Suno, exact title ⚠️ not public | Suno | No prior contact. LinkedIn already shows Suno; identity as ex-Uber One payments tech lead ✅ confirmed via cross-referenced profiles. |
| Justo Benetti | CRO, Yuno | Yuno | Organizer. Knew Madden's number since at least Oct 2025 (unanswered WhatsApp ping while Madden was at Disney). Compressed "next week" to "tomorrow". |
| German Tatis | Sr. AE, Yuno | Yuno | Owner of the account history: Jasper LinkedIn thread (Feb to Apr), email waves (Feb to Jul), research. |

### Madden Titus (external, decision-side)
- **Career (✅ via RocketReach/ZoomInfo/Wiza, LinkedIn partially readable):** Accenture (2014 to 2016) → Netflix (2016 to 2020: Senior Financial Analyst → Manager, Payment Analytics and Fraud → Senior Manager, Global Payments Fraud Strategy and Analytics) → Disney Streaming (2021 to 2026: Lead PM Fraud → Senior Manager PM → Director, Payments and Fraud Product Management, Jul 2024 to 2026). Roughly 10 years in streaming-subscription payments and fraud, arriving via finance/analytics, not engineering.
- **Education:** Yale School of Management EMBA (2022 to 2024); Denison University, BA Economics and Philosophy.
- **Location:** New York metro. LinkedIn headline still says Disney (profile not yet updated). ⚠️ The Suno title is unknown: ask it naturally in the call.
- **Public thinking (✅):** Netflix-era conference deck "Shining a Light on the Transaction Lifecycle" (with Vantiv and Mastercard): false declines as "an intensely negative experience", root cause "inconsistent access to data and disconnected fraud strategies", tactics listed: card-on-file authentication updates, adaptive fraud rules, BIN analytics, 3DS, intelligent retries. This is Yuno's pitch in Madden's own vocabulary.
- **Disproven:** the "Global Head of Payments at Spotify" claim circulating in data brokers belongs to Lex Ledger, a different person. Never mention Spotify.
- **How to read Madden:** an empiricist ("passion for using empirical evidence") who lived subscription payments at the two most sophisticated streaming shops. Disney famously pulled Disney+/Hulu signups OFF the App Store in Oct 2024 to escape the 30% fee while Madden ran payments product there (Netflix did the same in 2018). Expect data, benchmarks and honest scoping to land, and inflated claims to get flagged instantly.

### Gurwinder Singh Gulati (external, technical evaluator)
- **Career (✅ via getprog.ai/weekday.works/ContactOut, LinkedIn partially readable):** Uber (Senior Software Engineer, Tech Lead of Uber One Membership Payments, "scalable payments infrastructure") → previously Netflix Ads Engineering/ML, LinkedIn (recruiter search, 2 search patents, Microsoft-assigned), Facebook, Hulu. ~12 years experience.
- **Education:** University of Washington CS (direct admit), HBS Online entrepreneurship cert.
- **Location:** New York. LinkedIn already shows Suno as current company; ⚠️ title not visible, start date unknown.
- **Signals:** personal site self-description "Tech lead and software engineer working across machine learning, growth, payments, search, ads, and developer tools." Active AI-coding-tools enthusiast (blog posts on CursorAI, Feb 2025). No public payments thought leadership: the lens will be practical engineering.
- **How to read Gurwinder:** the build-vs-buy voice, having built membership payments infra at Uber scale. Win Gurwinder with API quality, sandbox access, latency/uptime data and connector maintenance economics, not with sales narrative.

### Sponsor path and relationship timeline
- Feb 20 to Apr 29, 2026: German ↔ Jasper van Rijckevorsel on LinkedIn. Jasper confirmed active vendor evaluation ("optimizing our mobile payment flows and potentially moving payment vendors"), called German's 3-angle answer "a great answer", left timing open. Business case shared (deck.y.uno/sunobc).
- Feb to Mar 2026: email waves to 10 Suno contacts (founders included), 4-touch cadences. Zero replies.
- Jun 3 to Jul 28, 2026: "Congrats on the Series D" group thread to Martin Camacho, Jasper, Jeremy Sirota, Georg Kucsko, Jack; João and Justo added; final door-open note Jul 28. Zero replies.
- Oct 2025: Justo pinged Madden on WhatsApp (Disney era, unanswered). Sept 2025: German emailed Madden at Disney (Stripe Tour NY, unanswered).
- **Aug 6, 2026: Madden replied to Justo's 10-month-old ping from the new Suno seat and asked for this meeting.** Implication: they already hold the business case and months of Yuno context; treat this as a follow-up with a new, better-qualified audience, not a cold first meeting.

### Other known contacts in the account
| Person | Role | State |
|---|---|---|
| Jasper van Rijckevorsel | Music + Engineering | Warm-ish; emoji reaction Apr 29; origin of the thread. Send post-call note. |
| Jeremy Sirota | Chief Commercial Officer (ex Merlin CEO, joined 2026) | On the June email thread; owns licensing money flows. Future payout-angle door. |
| Mikey Shulman (CEO), Georg Kucsko (CTO), Martin Camacho (CPO), Keenan Freyberg (COO) | Co-founders (ex Kensho) | Martin and Georg were on email waves; no replies. |
| Gourab Ghose | Head of International Markets (ex Snap India; Mumbai) | Not contacted. Relevant to localization/expansion angle. |
| Paul Sinclair (CMO, ex Warner), Rosie Nguyen (Head of Creative Economy and Monetization), Jake McNeill (Controller, ex Crunchyroll) | Music/monetization/finance leadership | Not contacted. Rosie owns the payout side (Spark). |

---

## 3. THE COMPANY

**What they do:** AI music generation platform (suno.com, apps on iOS/Android). Text prompt to full song. Freemium: Free (50 daily credits, no commercial rights, downloads removed in 2026), Pro ($10/mo or $8/mo annual), Premier ($30/mo or $24/mo annual), plus top-up credit packs. 100M+ cumulative users, 2M paid. Founded 2022 in Cambridge MA by four ex-Kensho engineers; first public product Dec 2023.

| Key metric | Value | Date | Source |
|---|---|---|---|
| ARR | $300M | Feb 2026 | CEO announcement (TechCrunch/Billboard/MBW) |
| Paid subscribers | 2M | Feb 2026 | Same |
| Cumulative users | 100M+ | Feb 2026 | Same |
| Valuation | $5.4B post-money | Jun 2026 | Series D coverage (Variety/Bloomberg/MBW) |
| Total raised | $775M to $819M (sources conflict) | Jun 2026 | Tracxn/Sacra vs PitchBook |
| Employees | ~200, target ~340 by YE2026 | Jul 2026 | Music Business Worldwide |
| Web traffic | ~70.3M visits per trailing 3 months, global rank #539 | Jun 2026 | SimilarWeb |
| Category position | 68.9% of AI-music-generator traffic (AITools.xyz) to 90.9% of a 12-domain SimilarWeb cohort | Jun 2026 | AITools.xyz / SimilarWeb, both traffic-based |

**Corporate structure and billing entities:**
| Entity | Role | Notes |
|---|---|---|
| Suno Inc., 17 Dunster St, Cambridge MA | Sole contracting entity worldwide | ToS governed by Massachusetts law. ✅ |
| No foreign subsidiaries found | All markets billed cross-border from the US entity | VeraSafe (Ireland/UK) is only a GDPR representative service, not a Suno entity. ✅ |
| Billing rails | Stripe (web), Apple IAP (iOS), Google Play (Android) | Three disconnected rails; store subs must be managed in-store. ✅ |
| Offices | Cambridge, NYC, LA, SF (all US) | Job postings confirm. ✅ |

**Leadership and strategy themes:** IPO readiness (first audit, controller hire, strategic finance roles touching capital markets); licensed-model migration in 2026 under the Warner deal; music-industry integration (Songkick acquisition, CMO ex-Warner, CCO ex-Merlin); international expansion (Ghose); monetization deepening (download caps, top-ups, Spark creator economy under Rosie Nguyen).

---

## 4. FINANCIALS

**Growth trajectory (founding to today; private company, so milestones are funding/press anchored):**

| Period | Metric | Value | Type | Source |
|---|---|---|---|---|
| 2022 | Founded | Cambridge MA | | Forbes |
| Mar 2023 | Series A (earliest documented round; no seed found) | Amount undisclosed, Matrix-led | Funding | Clay dossier |
| 2023 | Revenue | Sub-$1M | ARR | valueaddvc (est.) |
| May 2024 | Series B | $125M, Lightspeed; ~$500M post | Funding | Suno blog + MBW |
| May 2024 | Revenue | ~$45M | ARR (est.) | Sacra |
| Jan 2025 | Revenue | $50M | ARR | Bloomberg via MBW |
| Sep 30, 2025 | Revenue | $140M | ARR (investor-pitch sourced) | Bloomberg via MBW |
| Nov 19, 2025 | Series C | $250M at $2.45B post; Menlo, NVentures/NVIDIA, Hallwood, Lightspeed, Matrix | Funding | PRNewswire |
| Nov 19, 2025 | Revenue | $200M | "Annual revenue" run-rate at a point in time, NOT FY recognized | WSJ via MBW/TechCrunch |
| FY2025 | Revenue | ~$150M | Recognized revenue, Forbes ESTIMATE | Forbes (Apr 2026) |
| Feb 27, 2026 | Revenue | **$300M** | ARR, company-stated | TechCrunch/Billboard/MBW |
| Jun 3, 2026 | Series D | $400M+ at $5.4B post; Bond Capital lead; IVP, Forerunner, USV, Alkeon, Quiet | Funding | MBW/Variety/Bloomberg |
| Jul 15, 2026 | Headcount | ~200 → ~340 target YE2026 | | MBW |

**Recent-months read (Nov 2025 to Aug 2026):** revenue up sharply ($200M → $300M ARR in ~3 months, +50%; Sacra frames Feb 2026 as +404% YoY). No public ARR update after February; the Series D and IPO coverage still cite $300M, so do not extrapolate past it. Cancellation rates reportedly declined into the Series D ("a higher share of users are falling in love with the product", CEO). No layoffs or restructuring; the opposite, +70% headcount plan. No guidance (private).

**Litigation and licensing exposure (material):**
- Warner: settled Nov 2025; all financial terms undisclosed (three sources confirm); Suno acquired Songkick in the deal; Suno is actively fighting disclosure of the Warner terms to UMG/Sony in discovery.
- UMG/Sony: ACTIVE in D. Mass. On May 21, 2026 the labels moved to expand from 560 works to 61,026 recordings after audio-fingerprint discovery. At the $150K statutory willful ceiling that is a THEORETICAL maximum above $9B (label it as theoretical ceiling, not a demand; the original 560-work baseline was ~$84M). Fact discovery runs to Sep 30, 2026; dispositive motions Apr 2027. Plus Koda (Denmark) and GEMA (Germany) suits.
- Licensed models introduce a new recurring royalty/rev-share COGS line in 2026 whose magnitude is undisclosed.

**Data breach (material, sensitive):** November 2025 breach via the Shai-Hulud npm supply-chain worm (employee dev credentials → internal repos and DBs) exposed 55,282,226 email addresses AND tens of thousands of Stripe payment records (names, addresses, purchase amounts, card type, expiry, last four). Added to Have I Been Pwned Jul 20, 2026; class action filed Jul 24, 2026 in D. Mass.; Suno reportedly had not notified users. Never raise it first; see Landmines.

**Other material items:** GPU compute costs exceed payroll "by several multiples" (Sacra analysis, not company-disclosed); NVIDIA's NVentures on the cap table; no disclosed burn/runway (do not state one); secondary shares list on Forge/NPM/UpMarket but no tender data; mobile IAP revenue estimates circulate from Appfigures but are mutually inconsistent (do not quote a number; direction only: mobile IAP is material but minority).

**Payment-cost-relevant economics:**
- Blended ARPU derived: $300M ÷ 2M ÷ 12 ≈ $12.50/mo, implying a Pro-heavy and/or annual-discounted mix.
- Annual plans are single high-ticket charges ($96/$288 web), raising decline and refund stakes per transaction.
- ~2% registered-to-paid conversion (derived); ~half of first-time users hit the free cap (Sacra); the 2026 free-tier download paywall is a deliberate conversion push, meaning MORE payment volume through the same single rail.
- iOS prices carry the store markup vs web: Pro $10 vs $8, Premier $30 vs $24 (verified Aug 6 on App Store vs suno.com/pricing). No public Suno commentary on IAP fee drag exists; treat as structural, unquantified, and as a discovery question. Madden lived Disney's Oct 2024 exit from App Store billing and knows this playbook cold.

**So what for the call:** a pre-IPO finance build-out plus flat-staffed engineering plus rising transaction volume through one processor makes approval rate, processing cost and payment-ops tooling exactly the margin levers a first audit will expose. The financial story argues for orchestration as margin infrastructure, bought not built.

---

## 5. COMPETITIVE LANDSCAPE

No analyst house publishes revenue-based market share for AI music; shares below are traffic-based (AITools.xyz category share, Jun 2026, SEMrush/Ahrefs-derived, monthly) or transparently derived. SimilarWeb figures are 3-month aggregates (Apr to Jun 2026). Bases are labeled per row; never mix bases in one claim.

| Competitor | Segment | Est. market share (basis + source) | Scale proxy | Differentiator | Payments posture |
|---|---|---|---|---|---|
| **Suno** | AI song generation, consumer | 68.9% of category traffic (AITools) / 90.9% of 12-domain SimilarWeb cohort (derived) | $300M ARR (Feb 2026); 81.8M monthly visits | The category leader by an order of magnitude | Stripe sole PSP + Apple/Google IAP; no orchestrator |
| Udio | AI song generation, consumer | 1.41% traffic (AITools) | ~$70M raised (a16z); ARR ~$3M circulates but has NO primary source, treat as unverified | Licensed with UMG and Warner (Oct/Nov 2025); relaunching 2026 as a licensed walled garden | Unknown (login-gated) |
| Mureka (Kunlun/Skywork) | AI song gen + fine-tuning API, CJK-native | No AITools entry; ~4.0% of Suno's traffic (derived, SimilarWeb) | $12M annualized revenue (Kunlun disclosure, Nov 2025); 2.8M visits/3mo | Suno's #1 SimilarWeb affinity competitor; MIDI export, stems, public API | Stripe + PayPal dual rail, live checkout A/B test, iOS IAP; no orchestrator |
| ElevenLabs (Eleven Music) | AI audio/voice, music vertical | No music-only estimate available | $500M ARR all products (May 2026, Stripe newsroom); $11B valuation | Licensed training (Believe), creator marketplace ($11M paid out) | Deepest Stripe stack in category incl. Connect payouts; single PSP, no orchestrator |
| Riffusion | AI music gen, free | No estimate available | $4M seed; 23K visits/3mo, collapsing | Open-source lineage | Unknown |
| MiniMax Music | AI music gen, API + app | No estimate available | Publicly listed parent (SEHK) | "Best vocals" in 2026 head-to-heads | Unknown |
| Musicful | AI music gen, consumer | No AITools entry; ~1.8% of Suno's traffic (derived) | 1.3M visits/3mo, growing | High Suno affinity | Unknown |
| Loudly | Royalty-free AI gen | 0.22% traffic (AITools) | 266K monthly visits, down 47.6% MoM | Legacy mobile install base | PayPal pay-in; payouts PayPal-only with 2.5% fee; iOS IAP primary; no orchestrator |
| AIVA | AI composition, classical | 0.19% traffic (AITools; only grower, but SimilarWeb disagrees on direction, hedge) | $2.48M raised | SACEM-recognized composer | Stripe only; no orchestrator |
| Soundraw | Royalty-free AI for video creators | 0.17% traffic (AITools) | 207K monthly visits | Creator keeps master rights | Stripe + PayPal; PayPal subs cancel inside PayPal; iOS IAP; no orchestrator |
| Mubert | B2B generative-music API | 0.15% traffic (AITools) | ~$4M revenue (Growjo, LOW confidence) | API-first infrastructure | Stripe + iOS IAP; no orchestrator |
| Beatoven.ai | Royalty-free mood music | No AITools entry; ~0.28% of Suno traffic (derived) | 96% of revenue from outside India (company) | Emotion-tagged scoring | Stripe only; no orchestrator |
| Boomy | AI gen + DSP distribution | 0.05% traffic (AITools) | Funding conflicts 4x across sources, do not state | Pays creator royalties (money-out exists) | Stripe + PayPal; no orchestrator |
| Splice (adjacent) | Sample subscription | No estimate available | >$100M revenue, ~600K paid subs (Apr 2025) | Pays sample creators when AI uses their sounds | Recurly billing → Stripe + PayPal (verbatim in ToS); Recurly is billing, not orchestration |
| Epidemic Sound (adjacent) | Stock music subscription | ~12 to 13% of royalty-free licensing (derived, both inputs soft) | FY2025 SEK 1,828M, MINUS 5% YoY, adj. EBITDA negative | The disrupted incumbent | PSP unknown; JCB/UnionPay/local options documented |
| Artlist (adjacent) | Creator asset subscription | No estimate available | $260M ARR, +50% YoY (Calcalist, Jan 2026); new CFO reads as IPO prep | Bundles music+SFX+footage+AI | PSP unknown |
| Google Lyria/Flow (Big Tech) | Foundation model | No estimate available | Killed MusicFX Jul 31, 2026; Lyria 3.5 shipped | Sells licensing indemnity + SynthID watermarking | Google billing; not a prospect |
| Stability Audio / Meta MusicGen (Big Tech) | Foundation models | No estimate available | Stability: 126K visits/3mo; Meta AudioCraft effectively abandoned (no commit since Mar 2025) | Open weights / research | Unknown / N/A |

**Where Suno sits:** it IS the category (roughly 69 to 91% of visits depending on basis, ~25x Mureka's revenue). The category's traffic is contracting across the board (June 2026 MoM: nearly every player down double digits, Suno itself down 13.85%), which shifts the growth burden from acquisition to monetization: approval rates and involuntary churn land directly on the revenue line. **For the call:** nobody in this category runs an orchestrator; the default is single-Stripe plus IAP (ElevenLabs runs everything on Stripe with reportedly one engineer). First-mover advantage on payments infrastructure is available, and Suno is the only one with the scale to need it.

---

## 6. PAYMENTS MONEY MAP

**Platform status:** No orchestrator, no MoR. Three rails: Stripe (web, sole direct processor per ToS and help center), Apple IAP, Google Play. Ex-subscriber invoices via Stripe billing portal. PayPal reachable ONLY by setting it as the app-store default payment method (i.e., PayPal volume pays the store tax). ✅

**Providers per region:** Stripe globally for web across all 17 currencies (USD, AUD, BRL, CAD, EUR, GBP, IDR, INR, JPY, KRW, MXN, NOK, PLN, SEK, THB, TRY, UAH). Subscriptions offered in 36 countries. RUB absent from the currency list while Russia is the #2 traffic country (5.41%): unclear monetization, 🔍 discovery. ✅

**Documented payment methods (help center, verbatim scope):**
| Market scope | Methods documented | Notes |
|---|---|---|
| Global web | Visa, Mastercard, Amex | Core rail |
| "Some regions" web | Apple Pay, Google Pay, Cash App Pay, Stablecoin | Region mapping not published |
| Korea web | Korean Card, KakaoPay, NaverPay | Already localized |
| India web | UPI | Already localized |
| Mobile | Apple IAP / Google Play (PayPal via store default) | Store-managed billing |

Every non-card method they document is Stripe-native; the coverage map is Stripe's catalog, not a Suno payments strategy. Never tell them what they "lack"; frame around market payment behavior (Section 7) and ask what is on the roadmap. Note their own help center already concedes the pattern: "Options not yet available with our direct processor may be available on mobile."

**Fraud/3DS posture:** nothing public; no trust center, no PCI/SOC statements (only "commercially reasonable security measures" in the privacy policy). ⚠️ Likely SAQ-A-style reduced scope via Stripe-hosted billing (inference, never assert). Post-breach, security posture is a live internal topic; Yuno's certifications (PCI DSS, SOC 2 Type 2, ISO 27001/27701) and vault/tokenization portability are the ready answer IF THEY raise security.

**Hiring signals:** no payments/billing role posted (8 open roles, all engineering; closest is Software Engineer, Growth, NYC, revenue-focused; Trust & Safety role mentions chargebacks). The payments team appears to be exactly the two people in this meeting. 🔍 Confirm team size and mandate.

**Complaints pattern (public):** BBB F, 93 complaints, 89 unanswered; recurring decline-despite-funds reviews on Trustpilot; refund friction; third-party guides teaching workarounds (PayPal via stores, virtual dollar cards) for Nigeria, India, Ghana, Pakistan, the Philippines. Classic single-rail false-decline signature plus a payment-ops tooling gap.

**Peer context:** zero orchestrators anywhere in the category (see Section 5 matrix). ElevenLabs = Stripe-only with one engineer per Stripe's own case study.

**Framing rules for this account:** keep Stripe, add a layer (German already told Jasper this in April, stay consistent); performance/cost/reliability/speed language; quantified claims with conditions; Yuno cases by name only where documented (InDrive, Rappi, Livelo, Reserva; GoFundMe with permission; Uber is publicly listed by Yuno).

---

## 7. TOP MARKETS (traffic + payment behavior)

| Market | Traffic share (SimilarWeb Jun 2026) | Local payment behavior (market-level, not claims about Suno) | For the call |
|---|---|---|---|
| United States | 19.2% | Cards dominant; wallets (Apple/Google Pay), Cash App Pay, BNPL growing | Core rail works; the lever here is retries, network tokens and account updater on renewals |
| Russia | 5.41% | Mir cards, SBP; international rails constrained | RUB not in Suno's currency list; monetization unclear; 🔍 ask, do not assert |
| Brazil | 4.97% | Pix ~40% of e-comm and rising, cards ~44% (with installments), boleto ~5% | #3 market billed in BRL cross-border from a US entity; local acquiring + local methods = the approval and cost lever |
| Germany | 4.72% | PayPal, SEPA/giropay heritage, strong debit culture | EU VAT already collected; local methods drive conversion |
| Japan | 3.93% | Konbini, PayPay, Rakuten Pay alongside cards | High-ARPU market; JPY billed cross-border |
| South Korea | in top 10 (currency + methods live) | Korean Card, KakaoPay, NaverPay standard | Already localized via Stripe: proof Suno responds to local-method demand |
| India | (currency + UPI live) | UPI dominant for low-ticket recurring | UPI already on; subscription mandates via UPI Autopay are their natural next step |
| Indonesia/Thailand/Turkey | currencies live (IDR/THB/TRY) | Wallet-heavy (DANA/OVO, TrueMoney), local cards | Billing currency exists; method depth is the question |

---

## 8. NEWS & SIGNALS (newest first)

| Date | Item | Why it matters |
|---|---|---|
| Aug 5, 2026 | Service outage, hundreds of user reports (DownDetector ~3PM ET) | Fresh; reliability is top-of-mind internally. Use with care, not as a gotcha |
| Aug 3-6, 2026 | Madden Titus and Gurwinder Gulati join Suno payments; Madden's inbound WhatsApp to Justo | The meeting's origin |
| Jul 28, 2026 | Class action filed over the data breach (D. Mass.) | Sensitive; never raise first |
| Jul 20, 2026 | Breach added to Have I Been Pwned: 55.3M emails + Stripe payment records | Same |
| Jul 15, 2026 | MBW: "Suno is building toward IPO readiness" (first audit, controller, strategic finance) | Payments become a CFO line item |
| Jun 25, 2026 | Spark incubator: cash grants to independent artists | Payout rails are live already |
| Jun 9, 2026 | AFM union sues UMG/Warner over AI settlement money distribution | Payout economics are contentious; Suno will need auditable rails |
| Jun 3, 2026 | Series D: $400M+ at $5.4B (Bond Capital) | War chest; "take bigger swings" |
| May 21, 2026 | UMG/Sony move to expand suit to 61,026 recordings | Legal overhang persists into 2027 |
| Apr 2026 | UMG/Sony settlement talks at an impasse (equity demands) | More settlements possible, more payout obligations |
| Feb 27, 2026 | $300M ARR, 2M paid subscribers, 100M+ users | The scale headline |
| Jan 21, 2026 | Yuno launches Agentic Commerce (works with Stripe, PayPal, Adyen, Checkout.com) | Yuno-side news; AI-native commerce angle for an AI company |
| Dec 22, 2025 | Details of 2026 Warner-deal changes: download caps, paid overages, non-downloadable free tier | New transaction types on the same rail |
| Nov 25, 2025 | Warner settlement + Songkick acquisition | Licensed-model era begins; ticketing adjacency |
| Nov 19, 2025 | Series C: $250M at $2.45B (Menlo, NVIDIA) | Prior round |
| Sep 2025 | Gourab Ghose joins as Head of International Markets (ex Snap India) | International expansion staffed |

---

## 9. SELLING YUNO HERE

**Core frame:** They came to us, three days into the new payments leader's tenure, asking about orchestration by name. Do not pitch the category. Run discovery, hand over the outside-in map as a gift, and behave like the advisors they want ("an honest assessment", Jasper's words in March; "I don't know what I don't know", Madden's words yesterday). The map IS the demo of what working with Yuno feels like.

**Hooks with proof points (real Yuno cases only):**
1. Renewal approval economics: Livelo +5% approval and 50% recovery of failed transactions; Reserva +4% in under 3 months. Tie to their ~24M renewals/year and ~$3M per approval point (labeled derived).
2. Market expansion speed: InDrive live in 10+ LATAM markets in under 8 months at 90% approval. Tie to Ghose's international mandate and BRL/IDR/THB/TRY currencies already billed.
3. Ops tooling: Rappi's real-time monitors, detection in milliseconds vs 5 to 10 minutes manual, 80% less analyst resolution. Tie to the 89 unanswered BBB complaints as the visible symptom of missing tooling (frame gently: "billing support load", never "your F rating").
4. Pay-in plus payout in one API: GoFundMe marketplace (splits, recipients, transfers across Stripe, Adyen, Tabapay). Ask permission internally before naming deal specifics. Tie to Spark grants and Warner opt-in licensing.
5. Keep-Stripe architecture: Yuno layers on top; nothing is ripped out. Consistent with what German already told Jasper in April.

**Landmines (what NOT to say):**
- Never raise the data breach, the BBB F rating as a label, the Aug 5 outage as a jab, or the lawsuits' merits. If THEY raise security: Yuno's PCI DSS, SOC 2 Type 2, ISO 27001/27701, vault and network tokenization, provider-agnostic token portability.
- Never mention the disproven Spotify role. Never mention the unanswered 2025 emails to Madden at Disney.
- Never claim Suno "lacks" Pix, OXXO or any method. Speak in market-behavior terms and roadmap questions.
- Do not quote the old business case numbers ($200M ARR, $2.45B) or re-send the stale deck; refresh first.
- Do not name-drop clients you cannot back in front of this audience. Gurwinder can validate Uber claims personally; Madden knows Disney/Netflix payment vendors. Uber and GoFundMe are publicly listed Yuno brands; align with Justo on xAI/OpenAI/Lovable before using them.
- Do not oversell IAP fee escape. Madden ran this exact play at Disney (Oct 2024 App Store exit). Position web-billing optimization and external-purchase flows honestly, jurisdiction by jurisdiction, and let Madden lead on store strategy.
- Do not let the call become a pitch. 30 minutes: listen first.

---

## 10. BE READY FOR (what THEY may ask)

| Likely question | Ready answer |
|---|---|
| "We could build this. Why buy?" (Gurwinder) | Uber-grade orchestration took years and dedicated teams. Suno has ~200 people, hiring is model/product engineering, and 2026 is consumed by the licensed-model migration. Yuno = maintained connectors, routing, vault, recon as product, live in weeks, on top of Stripe. Buy the commodity, build the differentiator. |
| "How exactly do you sit on top of Stripe?" | Yuno orchestrates: Stripe remains a processor (often the primary). Routing rules, cascading retries, fallbacks, network tokens/account updater, unified recon and analytics across Stripe + any added local acquirer. No rip-out; SDK or API-level integration. |
| "What does integration actually take?" | Single API/SDK; typical enterprise go-live in weeks; new providers enabled without new integrations. InDrive: 10+ markets in under 8 months. Offer the sandbox in the follow-up session. |
| "Pricing model?" | Align with Justo pre-call on what to share; standard posture: volume-based, structured so the approval uplift and cost savings fund it. Do not improvise numbers. |
| "PCI, security, data handling?" (post-breach sensitivity) | PCI DSS, SOC 2 Type 2, ISO 27001, ISO 27701. Tokenized vault, provider-agnostic tokens (portability = no lock-in), network tokenization. |
| "Which subscription/AI companies do you work with?" | Publicly named Yuno brands: Uber, McDonald's, NetEase, GoFundMe, inDrive, Rappi. For AI-specific references, follow the pre-call alignment with Justo. |
| "How do you prove approval uplift?" | Benchmarks come with conditions: Livelo +5% and 50% recovery, Reserva +4% <3 months, InDrive 90% approval across LATAM. Offer: assessment on THEIR data (by-market auth rates, decline codes) under NDA, before any commercial commitment. |
| "Can you help with app-store fees?" | Honest scope: web-billing conversion optimization, external purchase links where rules allow (US post-Epic, EU DMA), and better web checkout economics so more subscribers choose web. No magic IAP bypass. Madden knows this space; respect that. |
| "Do you do payouts?" | Yes: payout orchestration through the same API; GoFundMe marketplace live (splits, recipients, transfers). Relevant to Spark and artist licensing. |
| "Latency/uptime at our scale?" | Engineered for high-concurrency merchants; monitors + auto-failover keep checkout live through provider incidents. Bring specifics in the technical session. |
| "Who else in our space uses an orchestrator?" | Verified honestly: nobody in AI music. The category default is single-Stripe. That is the opportunity: payments as a competitive edge nobody else has, at the only company in the category with the scale to need it. |
| "What would the evaluation look like?" | Propose: technical session (API/sandbox) → data assessment under NDA → scoped pilot on one flow (e.g., renewals retries or one market's local acquiring) with success criteria you define together. |

---

# LIVE ZONE

## 11. AGENDA (30 min)

| Time | Block | Lead | Notes |
|---|---|---|---|
| 0:00-0:02 | Intros, congrats on the new roles, name-rhyme callback | Justo | Notes: ____ |
| 0:02-0:07 | Madden's context: mandate, week-one findings, current thinking on the stack | Madden (LISTEN) | Notes: ____ |
| 0:07-0:14 | Discovery questions (Section 12, pick by flow) | German | Notes: ____ |
| 0:14-0:21 | The outside-in map: 3 findings (single rail economics, cross-border markets, 2026 payout/SKU collision) + how Yuno layers on Stripe, one line | German | Notes: ____ |
| 0:21-0:26 | Operator exchange: reactions, Gurwinder's technical questions, build-vs-buy if it surfaces | Justo + German | Notes: ____ |
| 0:26-0:30 | Next steps: technical session + NDA data assessment; evaluation process and timeline; who else should be in the loop | Justo | Notes: ____ |

## 12. DISCOVERY QUESTIONS

1. What does your mandate cover: pay-in only, or also the payout side that Spark and the licensing deals are creating? Notes: ____
2. What did you inherit: is web billing all on Stripe today, and how are the Apple/Google rails managed alongside it? Notes: ____
3. Which numbers do you already have visibility into: auth rates by market, involuntary churn, decline codes? Which are you missing? Notes: ____
4. Roughly what share of paid subs come through the app stores vs web today? Notes: ____
5. Which markets matter most in the next 12 months (Brazil? Japan? India?), and does the international push change the billing setup? Notes: ____
6. The 2026 licensed-model launch adds paid download overages: whose roadmap is that checkout, yours or Growth's? Notes: ____
7. How do you two split payments product vs payments engineering, and is the team growing? Notes: ____
8. Where does your head go on build vs buy for routing/retries/failover, given the Uber One experience? Notes: ____
9. How will you run this evaluation: criteria, timeline, who signs off (finance? Jeremy? the founders?)? Notes: ____
10. What would make your first 90 days a win? Notes: ____

## 13. POST-MEETING CHECKLIST

- [ ] Same-day recap email to Madden and Gurwinder (cc Justo): what we heard, the 2 to 3 findings that resonated, proposed next step with dates.
- [ ] Send Jasper a short thank-you/loop-in note (the conversation his March reply started is now live).
- [ ] Log outcome + new facts (titles, team size, IAP split, evaluation process) in Deals/Suno/ and memory.
- [ ] Schedule the technical session with Gurwinder; prepare sandbox access.
- [ ] Refresh the business case with $300M ARR / $5.4B / 2M subs before any re-share.
- [ ] If payouts resonated: get internal permission to use GoFundMe specifics; brief Rosie Nguyen angle for later.

---

## APPENDIX: SOURCES

Company/financials: suno.com/terms · suno.com/pricing · suno.com/about · help.suno.com/en/articles/2421185 (methods/currencies) · help.suno.com/en/articles/2480705 (Stripe redirect) · techcrunch.com/2026/02/27 ($300M ARR) · musicbusinessworldwide.com (Series C/D, IPO readiness, WMG settlement, UMG/Sony expansion, Spark) · prnewswire.com (Series C, WMG deal) · variety.com / bloomberg.com (Series D) · forbes.com/companies/suno (FY2025 est.) · sacra.com/c/suno · pitchbook.com/profiles/company/512734-06
People: linkedin.com/in/madden-t-2378aa38 · linkedin.com/in/gurwindergulati · rocketreach.co/madden-titus-email_244265953 · zoominfo.com/p/Madden-Titus/10426663486 · wiza.co (Netflix/Disney roles) · slidetodoc.com/shining-a-light-on-the-transaction-lifecycle-ned (Netflix-era talk) · getprog.ai/profile/2336395 · weekday.works (Uber One TL) · contactout.com/gurwinder-singh-gulati-66038 · retailtechinnovationhub.com (Spotify role = Lex Ledger, disproven)
Complaints/breach: bbb.org profile suno-inc-0021-562641 · trustpilot.com/review/suno.com (regional mirrors) · technadu.com (breach) · digitalmusicnews.com/2026/07/28 (class action) · haveibeenpwned.com
Competitive: aitools.xyz (category traffic shares) · similarweb.com (suno.com and 12-domain cohort) · stripe.com/newsroom/news/elevenlabs-and-stripe · stripe.com/gb/customers/elevenlabs · splice.com/terms (Recurly/Stripe/PayPal verbatim) · calcalistech.com (Artlist ARR) · corporate.epidemicsound.com (FY2025) · chartlex.com · forbes.com (Udio deals)
Markets/context: worldpay GPR-style behavior via internal BC reference tables · musicinafrica.net · downdetector/statusgator (Aug 5 outage) · bestmediainfo.com + afaqs.com (Gourab Ghose) · macrumors.com/2024/10/21 (Disney App Store exit) · y.uno/en/newsroom/yuno-agentic-commerce · y.uno SOC 2/ISO certifications blog
Internal: Deals/Suno/jasper-linkedin-thread-2026-02-20_2026-04-29.md · Deals/Suno/madden-whatsapp-justo-2026-08-06.md · data/research/suno-2026-08-06.md · Business Cases/Business Case - Suno + Yuno.pptx (stale, refresh before use)
