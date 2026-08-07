# Meeting Brief: Yuno <> Suno (Aug 7, 2026) · v2 with Business Case

**Meeting:** "Suno & Yuno" · Friday, August 7, 2026 · 2:00 to 2:30 PM Colombia (3:00 PM ET) · https://meet.google.com/vze-qree-sfw · Organizer: Justo Benetti (CRO). All four attendees accepted.

**Objective:** Convert an inbound discovery call into a scheduled technical deep-dive with Gurwinder plus a data-sprint commitment, within 2 weeks, while establishing German and Justo as Madden's most useful outside advisors in week one of the job.

**⚠️ Pre-meeting actions:**
1. ⚠️ Fix the Slide 8 table before presenting: the dollar amounts are misaligned with countries (Brazil shows $66K and Germany $55K; correct is Germany $66K, Brazil $55K). Also "$764M/mo" must read "$764K/mo". Full corrected table in Section 14.
2. ⚠️ Decide whether to share the deck live or after. If shared live, the Slide 8 fix is mandatory. If not shared, this becomes a follow-up action.
3. ⚠️ Open both LinkedIn profiles manually to confirm current Suno titles (neither is public): linkedin.com/in/madden-t-2378aa38 and linkedin.com/in/gurwindergulati
4. ⚠️ Align with Justo pre-call: which AI references are usable (the June email named xAI, OpenAI, Lovable), breach posture (NEVER raise it first), who leads which section.
5. ⚠️ Jasper van Rijckevorsel is not on this invite. Do not add anyone. Send him a thank-you note after the call.

Evidence labels: ✅ verified · ⚠️ inference, never state in the call · 🔍 ask in discovery.

---

## 1. TL;DR BATTLE CARD

**Five facts to know cold:**
1. **This is inbound.** Madden WhatsApped Justo on Aug 6, named "payment orchestration" unprompted, wrote "I am only 3 days in and don't know what I don't know", and asked for the call. ✅
2. **The stack:** Stripe is the sole direct processor (their ToS: "SUNO DOES NOT PROCESS PAYMENT FOR ANY SERVICES"; help center: "our direct billing processor (Stripe)"), plus Apple IAP and Google Play as separate rails. 17 billing currencies, 36 countries, one US entity, no orchestrator. Their own help center: "Options not yet available with our direct processor may be available on mobile." ✅
3. **The scale:** $300M ARR, 2M paid subscribers (Feb 2026), $5.4B valuation after a $400M+ Series D (Jun 2026), reported IPO-readiness moves (first audit, Controller ex-Crunchyroll, Jul 2026). ✅
4. **2026 catalysts:** licensed models replace current ones under the Warner deal with paid download overages; Spark already pays cash grants to artists (payout rails incoming); international expansion staffed since Sept 2025 (Gourab Ghose, ex-Snap India, Mumbai). ✅
5. **The quantified case is ready:** a full per-country business case totalling **$12M/year** in identified value, built on their own public financials and validated market benchmarks. Section 14 has the whole model. ✅

**Three hooks, in priority order:**
1. **Madden's own thesis, played back.** At Netflix he co-presented "Shining a Light on the Transaction Lifecycle" (with Vantiv and Mastercard): false declines come from misaligned incentives and "inconsistent access to data and disconnected fraud strategies" across the chain. That is Yuno's thesis in his own words. Reference it as an operator, not as flattery. ✅
2. **The map as the gift.** He said "I don't know what I don't know." Hand over the outside-in map: one rail carrying 17 currencies, Brazil/Germany/Japan billed cross-border from a US entity, three disconnected billing rails, and the renewal math. ✅
3. **Payouts plus new SKUs land in 2026.** Spark grants and Warner opt-in artist licensing mean money flows out while download overages multiply pay-in transactions. Yuno orchestrates both through one API (GoFundMe is the live marketplace reference; ask permission before sharing deal details). ✅

**THE objection: build-vs-buy** (Gurwinder led Uber One membership payments; Uber built in-house).
**The answer:** Uber-grade orchestration took years and dedicated payments teams Suno does not have and is not hiring (8 open roles, all model/product engineering; ~200 employees scaling to ~340). Yuno keeps Stripe, adds routing, retries, vault, reconciliation and connector maintenance as a product, live in weeks. The engineering Suno has is needed for the 2026 licensed-model migration. And Yuno publicly supports Uber, which Gurwinder can validate directly.

**The ask:** a 45 to 60 min technical session next week with Gurwinder (API and sandbox walkthrough, architecture on top of Stripe) plus a two-week joint data sprint to replace Yuno's external estimates with Suno's actual funnel data. Secondary ask: how the evaluation will run.

**Rapport opener:** Madden's own joke back: "You said our names rhyme and are one syllable off, so this meeting was clearly inevitable." Congratulate day 5 on the job.

---

## 2. WHO IS IN THE ROOM

| Name | Role | Side | Status / history |
|---|---|---|---|
| Madden Titus | Payments leadership at Suno, exact title ⚠️ not public, started ~Aug 3, 2026 | Suno | Inbound requester (WhatsApp to Justo, Aug 6). German emailed Madden at Disney in Sept 2025 (Stripe Tour NY, no reply); do not reference. |
| Gurwinder Singh Gulati | Payments/platform engineering at Suno, exact title ⚠️ not public | Suno | No prior contact. LinkedIn shows Suno; identity as ex-Uber One payments tech lead ✅ confirmed via cross-referenced profiles. |
| Justo Benetti | CRO, Yuno | Yuno | Organizer. Knew Madden's number since Oct 2025 (unanswered ping while Madden was at Disney). Compressed "next week" to "tomorrow". |
| German Tatis | Sr. AE, Yuno | Yuno | Owns the account history: Jasper thread, email waves, research, business case. |

### Madden Titus (decision side)
- **Career ✅:** Accenture (2014-2016) → Netflix (2016-2020: Senior Financial Analyst → Manager Payment Analytics and Fraud → Senior Manager Global Payments Fraud Strategy and Analytics) → Disney Streaming (2021-2026: Lead PM Fraud → Senior Manager PM → Director, Payments and Fraud Product Management, Jul 2024 to 2026). ~10 years in streaming-subscription payments and fraud, arriving via finance/analytics.
- **Education:** Yale School of Management EMBA (2022-2024); Denison University, BA Economics and Philosophy.
- **Location:** New York metro. LinkedIn headline still says Disney. ⚠️ Suno title unknown, ask naturally.
- **Public thinking ✅:** Netflix-era deck "Shining a Light on the Transaction Lifecycle" with Vantiv and Mastercard: false declines as "an intensely negative experience", root cause "inconsistent access to data and disconnected fraud strategies", tactics listed: card-on-file authentication updates, adaptive fraud rules, BIN analytics, 3DS, intelligent retries.
- **Disproven:** the "Global Head of Payments at Spotify" claim in data brokers belongs to Lex Ledger. Never mention Spotify.
- **How to read Madden:** an empiricist ("passion for using empirical evidence") who lived subscription payments at the two most sophisticated streaming shops. Disney pulled Disney+/Hulu signups OFF the App Store in Oct 2024 to escape the 30% fee while Madden ran payments product there (Netflix did the same in 2018). Expect data, benchmarks and honest scoping to land, and inflated claims to get flagged instantly.

### Gurwinder Singh Gulati (technical evaluator)
- **Career ✅:** Uber (Senior SWE, Tech Lead of Uber One Membership Payments) → previously Netflix Ads Engineering/ML, LinkedIn (recruiter search, 2 patents assigned to Microsoft), Facebook, Hulu. ~12 years.
- **Education:** University of Washington CS (direct admit), HBS Online entrepreneurship cert.
- **Location:** New York. LinkedIn shows Suno as current; ⚠️ title not visible, start date unknown.
- **Signals:** personal site: "Tech lead and software engineer working across machine learning, growth, payments, search, ads, and developer tools." Active AI-coding-tools enthusiast (CursorAI blog posts, Feb 2025). No public payments thought leadership.
- **How to read Gurwinder:** the build-vs-buy voice, having built membership payments infra at Uber scale. Win him with API quality, sandbox access, latency/uptime data and connector maintenance economics, not sales narrative.

### Relationship timeline
- Feb 20 to Apr 29, 2026: German ↔ Jasper van Rijckevorsel on LinkedIn. Jasper confirmed an active vendor evaluation ("optimizing our mobile payment flows and potentially moving payment vendors"), called German's 3-angle answer "a great answer", left timing open. BC shared (deck.y.uno/sunobc).
- Feb to Mar 2026: email waves to 10 Suno contacts including founders, 4-touch cadences. Zero replies.
- Jun 3 to Jul 28, 2026: "Congrats on the Series D" group thread to Martin Camacho, Jasper, Jeremy Sirota, Georg Kucsko, Jack; João and Justo added; final door-open note Jul 28. Zero replies.
- Oct 2025: Justo pinged Madden on WhatsApp (Disney era, unanswered). Sept 2025: German emailed Madden at Disney (unanswered).
- **Aug 6, 2026: Madden replied to Justo's 10-month-old ping from the new Suno seat and asked for this meeting.** Implication: they already hold the business case and months of Yuno context. Treat as a follow-up with a better-qualified audience, not a cold first meeting.
- **Calendar check ✅: no prior meeting with any attendee of this call exists on the calendar.** This is the first live conversation.

### Other known contacts
| Person | Role | State |
|---|---|---|
| Jasper van Rijckevorsel | Music + Engineering | Origin of the thread; emoji reaction Apr 29. Send post-call note. |
| Jeremy Sirota | CCO (ex Merlin CEO, 2026) | On the June thread; owns licensing money flows. Payout-angle door. |
| Mikey Shulman (CEO), Georg Kucsko (CTO), Martin Camacho (CPO), Keenan Freyberg (COO) | Co-founders (ex Kensho) | Martin and Georg on email waves; no replies. |
| Gourab Ghose | Head of International Markets (ex Snap India; Mumbai) | Not contacted. Relevant to the expansion angle. |
| Paul Sinclair (CMO), Rosie Nguyen (Head of Creative Economy and Monetization), Jake McNeill (Controller) | Music/monetization/finance | Not contacted. Rosie owns the payout side (Spark). |

---

## 3. THE COMPANY

AI music generation platform. Text prompt to full song. Freemium: Free (50 daily credits, no commercial rights, downloads ending in 2026), Pro ($10/mo or $8/mo annual), Premier ($30/mo or $24/mo annual), plus top-up credit packs. Founded 2022 in Cambridge MA by four ex-Kensho engineers; first public product Dec 2023.

| Key metric | Value | Date | Source |
|---|---|---|---|
| ARR | $300M | Feb 2026 | CEO announcement (TechCrunch/Billboard/MBW) |
| Paid subscribers | 2M | Feb 2026 | Same |
| Cumulative users | 100M+ | Feb 2026 | Same |
| Valuation | $5.4B post-money | Jun 2026 | Series D coverage |
| Total raised | $775M to $819M (sources conflict) | Jun 2026 | Tracxn/Sacra vs PitchBook |
| Employees | ~200, target ~340 by YE2026 | Jul 2026 | MBW |
| Web traffic | ~23M visits/month, global rank #539 | Jun 2026 | SimilarWeb |
| Category position | 69% of AI-music-generator traffic (AITools) to 91% of a 12-domain SimilarWeb cohort | Jun 2026 | Both traffic-based |

**Corporate structure:**
| Entity | Role | Notes |
|---|---|---|
| Suno Inc., 17 Dunster St, Cambridge MA | Sole contracting entity worldwide | ToS governed by Massachusetts law ✅ |
| No foreign subsidiaries found | All markets billed cross-border from the US entity | VeraSafe (Ireland/UK) is a GDPR rep service, not a Suno entity ✅ |
| Billing rails | Stripe (web), Apple IAP (iOS), Google Play (Android) | Three disconnected rails ✅ |
| Offices | Cambridge, NYC, LA, SF (all US) | Job postings confirm ✅ |

**Strategy themes:** IPO readiness (first audit, controller hire, strategic finance roles touching capital markets); licensed-model migration in 2026 under the Warner deal; music-industry integration (Songkick acquisition, CMO ex-Warner, CCO ex-Merlin); international expansion; monetization deepening (download caps, top-ups, Spark creator economy).

---

## 4. FINANCIALS

| Period | Metric | Value | Type | Source |
|---|---|---|---|---|
| 2022 | Founded | Cambridge MA | | Forbes |
| Mar 2023 | Series A (earliest documented; no seed found) | Undisclosed, Matrix-led | Funding | Clay |
| 2023 | Revenue | Sub-$1M | ARR | valueaddvc (est.) |
| May 2024 | Series B | $125M, Lightspeed; ~$500M post | Funding | Suno blog + MBW |
| May 2024 | Revenue | ~$45M | ARR (est.) | Sacra |
| Jan 2025 | Revenue | $50M | ARR | Bloomberg via MBW |
| Sep 30, 2025 | Revenue | $140M | ARR (investor-pitch sourced) | Bloomberg via MBW |
| Nov 19, 2025 | Series C | $250M at $2.45B post | Funding | PRNewswire |
| Nov 19, 2025 | Revenue | $200M | Run-rate at a point in time, NOT FY recognized | WSJ via MBW |
| FY2025 | Revenue | ~$150M | Recognized revenue, Forbes ESTIMATE | Forbes (Apr 2026) |
| **Feb 27, 2026** | Revenue | **$300M** | ARR, company-stated | TechCrunch/Billboard/MBW |
| Jun 3, 2026 | Series D | $400M+ at $5.4B post; Bond Capital lead | Funding | MBW/Variety/Bloomberg |
| Jul 15, 2026 | Headcount | ~200 → ~340 target | | MBW |

**Recent months:** revenue up sharply ($200M → $300M ARR in ~3 months). No public ARR update after February; do not extrapolate. Cancellation rates reportedly declined into the Series D. No layoffs; +70% headcount plan. No guidance (private).

**Litigation and licensing (material):** Warner settled Nov 2025, terms undisclosed, Songkick acquired in the deal, Suno actively fighting disclosure of those terms to UMG/Sony. UMG/Sony ACTIVE in D. Mass.; on May 21, 2026 they moved to expand from 560 works to 61,026 recordings after audio-fingerprint discovery (at the $150K statutory willful ceiling that is a THEORETICAL maximum above $9B; original baseline ~$84M). Fact discovery to Sep 30, 2026; dispositive motions Apr 2027. Plus Koda (Denmark) and GEMA (Germany).

**Data breach (sensitive):** November 2025 breach via the Shai-Hulud npm supply-chain worm exposed 55,282,226 email addresses AND tens of thousands of Stripe payment records. Added to Have I Been Pwned Jul 20, 2026; class action filed Jul 24, 2026 in D. Mass. Never raise it first.

**Payment-cost economics:**
- Blended ARPU derived: $300M ÷ 2M ÷ 12 ≈ $12.50/mo ($150/year).
- Annual plans are single high-ticket charges ($96/$288 web), raising decline and refund stakes.
- ~2% registered-to-paid conversion; ~half of first-time users hit the free cap (Sacra). The 2026 free-tier download paywall pushes MORE volume through the same rail.
- iOS carries the store markup: Pro $10 vs $8, Premier $30 vs $24 (verified Aug 6). No public Suno commentary on IAP fee drag; treat as a discovery question. Madden lived Disney's Oct 2024 App Store exit.

**So what for the call:** a pre-IPO finance build-out plus flat-staffed engineering plus rising transaction volume through one processor makes approval rate, processing cost and payment-ops tooling exactly the margin levers a first audit will expose.

---

## 5. COMPETITIVE LANDSCAPE

No analyst house publishes revenue-based share for AI music. Shares below are traffic-based (AITools.xyz category share, Jun 2026, SEMrush/Ahrefs-derived) or transparently derived. SimilarWeb figures are 3-month aggregates (Apr-Jun 2026).

| Competitor | Segment | Est. share (basis + source) | Scale proxy | Differentiator | Payments posture |
|---|---|---|---|---|---|
| **Suno** | AI song generation | 69% category traffic (AITools) / 91% of 12-domain cohort (derived) | $300M ARR; 81.8M monthly visits | Category leader by an order of magnitude | Stripe sole PSP + Apple/Google IAP; no orchestrator |
| Udio | AI song generation | 1.41% traffic (AITools) | ~$70M raised (a16z); ARR ~$3M circulates with NO primary source | Licensed with UMG and Warner; relaunching as licensed walled garden | Unknown (login-gated) |
| Mureka (Kunlun/Skywork) | AI song gen + API, CJK-native | No AITools entry; ~4% of Suno traffic (derived) | $12M annualized (Kunlun disclosure, Nov 2025) | Suno's #1 SimilarWeb affinity competitor; MIDI export, stems, public API | Stripe + PayPal, live checkout A/B test, iOS IAP; no orchestrator |
| ElevenLabs (Eleven Music) | AI audio, music vertical | No music-only estimate available | $500M ARR all products (May 2026); $11B valuation | Licensed training (Believe), creator marketplace | Deepest Stripe stack incl. Connect payouts; single PSP, no orchestrator |
| Riffusion | AI music gen, free | No estimate available | $4M seed; 23K visits/3mo, collapsing | Open-source lineage | Unknown |
| MiniMax Music | AI music gen, API + app | No estimate available | Publicly listed parent (SEHK) | "Best vocals" in 2026 head-to-heads | Unknown |
| Musicful | AI music gen | No AITools entry; ~1.8% of Suno traffic (derived) | 1.3M visits/3mo, growing | High Suno affinity | Unknown |
| Loudly | Royalty-free AI gen | 0.22% traffic (AITools) | 266K monthly visits, down 47.6% MoM | Legacy mobile install base | PayPal pay-in; payouts PayPal-only with 2.5% fee; no orchestrator |
| AIVA | AI composition, classical | 0.19% traffic (AITools; SimilarWeb disagrees on direction, hedge) | $2.48M raised | SACEM-recognized composer | Stripe only; no orchestrator |
| Soundraw | Royalty-free AI for video | 0.17% traffic (AITools) | 207K monthly visits | Creator keeps master rights | Stripe + PayPal; iOS IAP; no orchestrator |
| Mubert | B2B generative-music API | 0.15% traffic (AITools) | ~$4M revenue (Growjo, LOW confidence) | API-first infrastructure | Stripe + iOS IAP; no orchestrator |
| Beatoven.ai | Royalty-free mood music | No AITools entry; ~0.28% of Suno traffic (derived) | 96% of revenue outside India | Emotion-tagged scoring | Stripe only; no orchestrator |
| Boomy | AI gen + DSP distribution | 0.05% traffic (AITools) | Funding conflicts 4x across sources | Pays creator royalties (money-out exists) | Stripe + PayPal; no orchestrator |
| Splice (adjacent) | Sample subscription | No estimate available | >$100M revenue, ~600K paid subs (Apr 2025) | Pays sample creators when AI uses their sounds | Recurly billing → Stripe + PayPal (verbatim in ToS); Recurly is billing, not orchestration |
| Epidemic Sound (adjacent) | Stock music subscription | ~12-13% of royalty-free licensing (derived, both inputs soft) | FY2025 SEK 1,828M, MINUS 5% YoY, EBITDA negative | The disrupted incumbent | PSP unknown |
| Artlist (adjacent) | Creator asset subscription | No estimate available | $260M ARR, +50% YoY (Jan 2026); new CFO reads as IPO prep | Bundles music+SFX+footage+AI | PSP unknown |
| Google Lyria/Flow | Foundation model | No estimate available | Killed MusicFX Jul 31, 2026 | Sells licensing indemnity + SynthID | Google billing; not a prospect |
| Stability Audio / Meta MusicGen | Foundation models | No estimate available | Stability 126K visits/3mo; Meta AudioCraft dormant since Mar 2025 | Open weights / research | Unknown / N/A |

**Where Suno sits:** it IS the category. Category traffic is contracting across every player (Jun 2026 MoM, Suno itself down 13.85%), shifting growth from acquisition to monetization, which puts approval rates and involuntary churn directly on the revenue line. **For the call:** nobody in this category runs an orchestrator; the default is single-Stripe plus IAP. First-mover advantage is available, and Suno is the only one with the scale to need it.

---

## 6. PAYMENTS MONEY MAP

**Platform status:** No orchestrator, no MoR. Three rails: Stripe (web, sole direct processor per ToS and help center), Apple IAP, Google Play. Ex-subscriber invoices via Stripe billing portal. PayPal reachable ONLY as the app-store default payment method, so that volume pays the store tax. ✅

**Coverage:** Stripe globally across 17 currencies (USD, AUD, BRL, CAD, EUR, GBP, IDR, INR, JPY, KRW, MXN, NOK, PLN, SEK, THB, TRY, UAH). Subscriptions in 36 countries. RUB absent while Russia is the #2 traffic country (5.41%): monetization unclear, 🔍 discovery.

**Documented methods:**
| Scope | Methods | Notes |
|---|---|---|
| Global web | Visa, Mastercard, Amex | Core rail |
| Brazil | Pix ✅ (confirmed live, not in their public help center) | Recurring version, Pix Automatico, is the gap |
| Korea | Korean Card, KakaoPay, NaverPay | Already localized |
| India | UPI | Already localized; UPI Autopay is the gap |
| "Some regions" | Apple Pay, Google Pay, Cash App Pay, stablecoin | Region mapping not published |
| Mobile | Apple IAP / Google Play (PayPal via store default) | Store-managed billing |

**The insight that lands:** Suno has the one-time versions of the local methods (Pix, UPI) but not the subscription-grade recurring rails (Pix Automatico, UPI Autopay). For a renewals business, that is the half that matters. Never say they "lack" a method; frame as depth and recurring capability.

**Fraud/3DS:** nothing public; no trust center, no PCI/SOC statements. ⚠️ Likely SAQ-A-style reduced scope via Stripe-hosted billing (inference, never assert). Post-breach, security is a live internal topic; Yuno's certifications (PCI DSS, SOC 2 Type 2, ISO 27001/27701) and provider-agnostic token vault are the ready answer IF THEY raise it.

**Hiring signals:** no payments/billing role posted (8 open roles, all engineering; closest is SWE Growth NYC; Trust & Safety mentions chargebacks). The payments team appears to be exactly the two people in this meeting. 🔍 Confirm.

**Complaints (public):** BBB rating F, 93 complaints, 89 unanswered; recurring decline-despite-funds reviews on Trustpilot; third-party guides teaching workarounds (virtual dollar cards, app-store routing) for Nigeria, India, Ghana, Pakistan, the Philippines. Classic single-rail false-decline signature plus a payment-ops tooling gap.

**Framing rules:** keep Stripe, add a layer (German told Jasper this in April, stay consistent); performance/cost/reliability/speed language; quantified claims with conditions; Yuno cases by name only where documented.

---

## 7. TOP MARKETS

| Market | Traffic (SimilarWeb Jun 2026) | Local payment behavior | For the call |
|---|---|---|---|
| United States | 19.2% | Cards dominant; wallets, Cash App Pay | Lever is retries, network tokens, account updater, plus PayPal/Venmo on web |
| Russia | 5.41% | Mir, SBP; international rails constrained | RUB not in the currency list; 🔍 ask, do not assert, do not propose |
| Brazil | 4.97% | Pix ~40% of e-comm, cards ~44% with installments | Pix live; Pix Automatico for renewals is the gap |
| Germany | 4.72% | PayPal, SEPA DD, strong debit culture | EU VAT already collected; recurring rails drive renewals |
| Japan | 3.93% | Konbini, PayPay, Rakuten Pay | High-ARPU market; method trust lifts conversion |
| South Korea | in top 10 | KakaoPay, NaverPay standard | Already localized: proof Suno responds to local demand |
| India | currency + UPI live | UPI dominant for low-ticket recurring | UPI Autopay mandates are the natural next step |
| Indonesia/Thailand/Turkey | IDR/THB/TRY live | Wallet-heavy, local schemes | Billing currency exists; method depth is the question |

---

## 8. NEWS & SIGNALS (newest first)

| Date | Item | Why it matters |
|---|---|---|
| Aug 6, 2026 | Madden's inbound WhatsApp to Justo | The meeting's origin |
| Aug 5, 2026 | Service outage, hundreds of user reports | Fresh; reliability top-of-mind. Never use as a jab |
| Aug 3, 2026 | Madden Titus starts at Suno (Gurwinder start date unknown) | Day 5 on the job today |
| Jul 28, 2026 | Class action filed over the data breach (D. Mass.) | Sensitive; never raise first |
| Jul 20, 2026 | Breach added to Have I Been Pwned: 55.3M emails + Stripe records | Same |
| Jul 15, 2026 | MBW: "Suno is building toward IPO readiness" | Payments become a CFO line item |
| Jun 25, 2026 | Spark incubator pays cash grants to artists | Payout rails already live |
| Jun 9, 2026 | AFM union sues UMG/Warner over AI settlement money | Payout economics contentious; auditable rails needed |
| Jun 3, 2026 | Series D: $400M+ at $5.4B (Bond Capital) | War chest |
| May 21, 2026 | UMG/Sony move to expand suit to 61,026 recordings | Legal overhang into 2027 |
| Feb 27, 2026 | $300M ARR, 2M paid subscribers, 100M+ users | The scale headline |
| Jan 21, 2026 | Yuno launches Agentic Commerce | Yuno-side news; AI-native angle |
| Dec 22, 2025 | 2026 Warner-deal changes detailed: download caps, paid overages | New transaction types on the same rail |
| Nov 25, 2025 | Warner settlement + Songkick acquisition | Licensed-model era begins |
| Sep 2025 | Gourab Ghose joins as Head of International Markets | Expansion staffed |

---

## 9. SELLING YUNO HERE

**Core frame:** They came to us, three days into the new payments leader's tenure, asking about orchestration by name. Do not pitch the category. Run discovery, hand over the outside-in map as a gift, and behave like the advisors they want. The map IS the demo of what working with Yuno feels like.

**Hooks with proof points (real Yuno cases only):**
1. Renewal approval economics: Livelo +5% approval and 50% recovery of failed transactions; Reserva +4% in under 3 months. Tie to ~24M renewals/year and the $12M model.
2. Market expansion speed: InDrive live in 11 countries in 8 months at 90% approval. Tie to Ghose's mandate and BRL/IDR/THB/TRY already billed.
3. Ops tooling: Rappi's real-time monitors, ms detection vs 5-10 minutes manual, 80% less analyst resolution. Tie gently to billing support load, never to "your F rating".
4. Pay-in plus payout in one API: GoFundMe marketplace (splits, recipients, transfers). Permission needed before naming deal specifics. Tie to Spark and Warner licensing.
5. Keep-Stripe architecture: Yuno layers on top, nothing ripped out.

**Landmines:**
- Never raise the data breach, the BBB rating, the Aug 5 outage, or the lawsuits' merits. If THEY raise security: PCI DSS, SOC 2 Type 2, ISO 27001/27701, vault and network tokenization, provider-agnostic token portability.
- Never mention the disproven Spotify role or the unanswered 2025 emails to Madden at Disney.
- Never claim Suno "lacks" Pix, UPI or any method. They have the one-time versions; the gap is recurring depth.
- Do not quote the old business case numbers ($200M ARR, $2.45B) or re-send the stale deck.
- Do not name-drop clients you cannot back. Gurwinder can validate Uber personally; Madden knows Disney/Netflix vendors.
- Do not oversell IAP fee escape. Madden ran this exact play at Disney. Let him lead on store strategy.
- Do not let the call become a pitch. 30 minutes: listen first.

---

## 10. BE READY FOR

| Likely question | Ready answer |
|---|---|
| "We could build this. Why buy?" (Gurwinder) | Uber-grade orchestration took years and dedicated teams. Suno has ~200 people, hiring is model/product engineering, and 2026 is consumed by the licensed-model migration. Yuno = maintained connectors, routing, vault, recon as product, live in weeks, on top of Stripe. |
| "How do you sit on top of Stripe?" | Stripe remains a processor, often primary. Routing rules, cascading retries, fallbacks, network tokens/account updater, unified recon across Stripe plus any local acquirer. No rip-out. |
| "What does integration take?" | Single API/SDK; typical enterprise go-live in weeks; new providers enabled without new integrations. InDrive: 11 countries in 8 months. Sandbox in the follow-up session. |
| "Pricing model?" | Align with Justo pre-call. Standard posture: volume-based, structured so the approval uplift and cost savings fund it. Do not improvise numbers. |
| "PCI, security, data handling?" (post-breach) | PCI DSS, SOC 2 Type 2, ISO 27001, ISO 27701. Tokenized vault, provider-agnostic tokens (portability = no lock-in), network tokenization. |
| "Which AI companies do you work with?" | Publicly named Yuno brands: Uber, McDonald's, NetEase, GoFundMe, inDrive, Rappi. For AI-specific references, follow the pre-call alignment with Justo. |
| "How do you prove approval uplift?" | Benchmarks with conditions: Livelo +5% and 50% recovery, Reserva +4% <3 months, InDrive 90% approval. Offer: assessment on THEIR data under NDA before any commercial commitment. |
| "Can you help with app-store fees?" | Honest scope: web-billing conversion optimization, external purchase links where rules allow (US post-Epic, EU DMA), better web checkout economics. No magic IAP bypass. |
| "Do you do payouts?" | Yes: payout orchestration through the same API; GoFundMe marketplace live. Relevant to Spark and artist licensing. |
| "Latency/uptime at our scale?" | Engineered for high-concurrency merchants; monitors and auto-failover keep checkout live through provider incidents. Specifics in the technical session. |
| "Who else in our space uses an orchestrator?" | Verified honestly: nobody in AI music. The category default is single-Stripe. That is the opportunity. |
| "What would the evaluation look like?" | Technical session (API/sandbox) → two-week joint data sprint under NDA → scoped pilot on one flow with success criteria they define. |
| **"What is this actually worth to us?"** | **Section 14. $12M/year identified, built country by country on their own public financials. Offer the model, not just the headline.** |

---

# LIVE ZONE

## 11. AGENDA (30 min)

| Time | Block | Lead | Notes |
|---|---|---|---|
| 0:00-0:02 | Intros, congrats on the new roles, name-rhyme callback | Justo | Notes: ____ |
| 0:02-0:07 | Madden's context: mandate, week-one findings, current thinking on the stack | Madden (LISTEN) | Notes: ____ |
| 0:07-0:14 | Discovery questions (Section 12, pick by flow) | German | Notes: ____ |
| 0:14-0:21 | The outside-in map: single rail economics, cross-border markets, 2026 payout/SKU collision, plus the $12M headline if it lands | German | Notes: ____ |
| 0:21-0:26 | Operator exchange: reactions, Gurwinder's technical questions, build-vs-buy if it surfaces | Justo + German | Notes: ____ |
| 0:26-0:30 | Next steps: technical session + data sprint; evaluation process and timeline; who else to include | Justo | Notes: ____ |

## 12. DISCOVERY QUESTIONS

1. What does your mandate cover: pay-in only, or also the payout side that Spark and the licensing deals are creating? Notes: ____
2. What did you inherit: is web billing all on Stripe today, and how are the Apple/Google rails managed alongside it? Notes: ____
3. Which numbers do you already have visibility into: auth rates by market, involuntary churn, decline codes? Which are you missing? Notes: ____
4. Roughly what share of paid subs come through the app stores vs web today? Notes: ____
5. Which markets matter most in the next 12 months, and does the international push change the billing setup? Notes: ____
6. The 2026 licensed-model launch adds paid download overages: whose roadmap is that checkout? Notes: ____
7. How do you two split payments product vs payments engineering, and is the team growing? Notes: ____
8. Where does your head go on build vs buy for routing/retries/failover, given the Uber One experience? Notes: ____
9. How will you run this evaluation: criteria, timeline, who signs off? Notes: ____
10. What would make your first 90 days a win? Notes: ____

## 13. POST-MEETING CHECKLIST

- [ ] Same-day recap email to Madden and Gurwinder (cc Justo): what we heard, the 2-3 findings that resonated, proposed next step with dates.
- [ ] Send Jasper a short thank-you/loop-in note.
- [ ] Log outcome and new facts (titles, team size, IAP split, evaluation process) in Deals/Suno/ and memory.
- [ ] Schedule the technical session with Gurwinder; prepare sandbox access.
- [ ] Fix the Slide 8 table before any deck share.
- [ ] If payouts resonated: get internal permission for GoFundMe specifics; brief the Rosie Nguyen angle for later.

---

# 14. BUSINESS CASE (the quantified ask)

## 14.1 Headline

**$12M per year in identified value**, built country by country from Suno's own public financials ($300M ARR, 2M paid subscribers, $150/year blended ARPU) and validated market benchmarks. Every figure traces to the underlying model; nothing is interpolated.

| Lever | Value/year | What it is |
|---|---|---|
| New APM growth (recurring rails) | **$6.07M** | Revenue from enabling subscription-grade local methods |
| Acceptance rate uplift (cards) | **$2.00M** | Recovered approvals via local acquiring and routing |
| Fee and MDR optimization | **$1.09M** | Lower processing cost through local rails |
| Engineering cost avoidance | **$2.83M** | Integrations Suno does not have to build and maintain |
| **Total** | **$11.99M ≈ $12M** | |

**How to say it in the room:** "We built the model on your public numbers, and it lands at roughly $12M a year. The point is not the number, it is that we can replace every assumption in it with your actual funnel data in two weeks."

## 14.2 Model assumptions (state these before the number, always)

- Traffic: SimilarWeb, ~23M visits/month, per-country shares Jun 2026 ✅
- Conversion: 6% visit-to-transaction, industry template standard
- ATV: $12.50, matching Suno's blended ARPU ✅ derived from $300M ARR / 2M subs
- Take rate: 60%, midpoint of the AI-industry benchmark range (40-80%)
- Acceptance uplift: 1-3% (AI industry benchmark, conservative end used)
- MDR: 1.5% local, 3.5% cross-border (AI industry benchmark)
- APM MDR cost: 1.2% across all markets
- **Only recurring-capable methods were counted.** One-time rails (OXXO, Konbini, boleto, SPEI, BLIK, PromptPay) were excluded because Suno is a subscription business. This is the single most defensible choice in the model and worth stating out loud.

## 14.3 Per-country breakdown (top 20, incremental MRR)

| # | Country | Visits/mo | Incremental MRR | Dominant play |
|---|---|---|---|---|
| 1 | United States | 4.9M | $180K | Network tokens + account updater + retries; PayPal and Venmo on web |
| 2 | Germany | 1.2M | $66K | PayPal + SEPA DD as recurring rails; SCA tuning |
| 3 | Brazil | 1.4M | $55K | Pix Automatico (recurring) + local acquiring + installments |
| 4 | Japan | 0.80M | $53K | PayPay + Rakuten Pay; renewal optimization |
| 5 | India | 0.9M | $52K | UPI Autopay mandates on live UPI + RuPay routing |
| 6 | Indonesia | 0.95M | $49K | GoPay + DANA + local cards |
| 7 | United Kingdom | 0.85M | $41K | Open Banking; retry and token optimization |
| 8 | France | 0.75M | $38K | Cartes Bancaires domestic routing + PayPal + SEPA DD |
| 9 | Spain | 0.6M | $37K | Bizum + SCA/retry tuning |
| 10 | Italy | 0.6M | $28K | PayPal + SEPA DD |
| 11 | Mexico | 0.40M | $25K | Local debit acquiring + Mercado Pago Suscripciones |
| 12 | Republic of Korea | 0.6M | $23K | Recurring tokens on live KakaoPay/NaverPay + Toss, Samsung Pay |
| 13 | Canada | 0.55M | $21K | Cards + PayPal; retry optimization |
| 14 | Turkey | 0.45M | $21K | TROY domestic scheme + installments + FX-aware acquiring |
| 15 | Thailand | 0.35M | $21K | TrueMoney + Rabbit LINE Pay |
| 16 | Poland | 0.33M | $15K | Card retries for renewals (BLIK is acquisition-only) |
| 17 | Ukraine | 0.28M | $13K | Local card routing + Apple/Google Pay tokens |
| 18 | Argentina | 0.20M | $11K | Mercado Pago Suscripciones + local cards |
| 19 | Netherlands | 0.22M | $10K | iDEAL first payment, SEPA DD renewals |
| 20 | Vietnam | 0.21M | $5K | Enable VND billing first, then MoMo |
| | **TOTAL** | | **$764K/mo** | **$9.2M/yr pay-in + $2.83M engineering = $12M** |

**Note on coverage:** 14 markets carry verified per-country data from the model; 6 (Italy, Turkey, Poland, Ukraine, Netherlands, Vietnam) are estimated using the same blended rate and proportionally reconciled to the confirmed total. Say this if asked; do not present all 20 as equally sourced.

## 14.4 The three-lever logic per market

Every market splits the same way, disclosed as a proportional allocation: **65% audience expansion** (recurring local methods), **21% authorization uplift** (local acquiring recovers cross-border declines), **14% renewal continuity** (retries and token management). Levers are NOT additive across independent user pools: each builds on the base the previous one creates.

## 14.5 What the deck contains (if you share it)

The full business case deck now carries: industry context (TAM, competitors, category dynamics), Suno's current stack and constraints, the 2026 money-flow shifts, the top-20 market table, 20 additional emerging markets, the decision frame (Stripe only vs second PSP vs orchestration), the keep-Stripe architecture, the UPI/Pix hop comparison, and a 20-country appendix with per-market deep dives.

**⚠️ Before sharing:** Slide 8's dollar column is misaligned with the country rows and the total reads "$764M/mo" instead of "$764K/mo". Fix both first. The appendix is correct and can be used to cross-check.

## 14.6 The offer that closes the loop

"These are our numbers built from the outside. The two-week data sprint replaces them with yours: country-level checkout starts, paid conversion, auth rates by BIN and decline reason, renewal failure and retry recovery, plan mix and per-country ARPU, plus MoR feasibility per market. What comes out is a forecast Suno's own finance team can defend, not a vendor estimate."

Six data points to request:
1. MAU and checkout starts by country
2. Free-to-paid conversion by country
3. Card authorization rate by country, issuer/BIN, decline reason
4. Renewal failure rate, retry recovery, involuntary churn by country
5. Plan mix, country pricing, refunds, churn, and the web-vs-IAP billing split
6. Risk, compliance and MoR feasibility by market

---

## APPENDIX: SOURCES

Company/financials: suno.com/terms · suno.com/pricing · suno.com/about · help.suno.com/en/articles/2421185 · help.suno.com/en/articles/2480705 · techcrunch.com/2026/02/27 · musicbusinessworldwide.com (Series C/D, IPO readiness, WMG settlement, UMG/Sony expansion, Spark) · prnewswire.com · variety.com / bloomberg.com · forbes.com/companies/suno · sacra.com/c/suno · pitchbook.com
People: linkedin.com/in/madden-t-2378aa38 · linkedin.com/in/gurwindergulati · rocketreach.co · zoominfo.com · wiza.co · slidetodoc.com (Netflix-era talk) · getprog.ai · weekday.works · contactout.com · retailtechinnovationhub.com (Spotify role = Lex Ledger, disproven)
Complaints/breach: bbb.org (suno-inc-0021-562641) · trustpilot.com/review/suno.com · technadu.com · digitalmusicnews.com/2026/07/28 · haveibeenpwned.com
Competitive: aitools.xyz · similarweb.com · stripe.com/newsroom/news/elevenlabs-and-stripe · splice.com/terms · calcalistech.com · corporate.epidemicsound.com · chartlex.com
Markets: musicinafrica.net · downdetector (Aug 5 outage) · bestmediainfo.com + afaqs.com (Gourab Ghose) · macrumors.com/2024/10/21 (Disney App Store exit) · y.uno newsroom
Business case: Google Sheet "BC sheets - Suno" (RESUMEN tab, verified Aug 6, 2026) · Google Slides "Business Case - Suno + Yuno"
Internal: Deals/Suno/jasper-linkedin-thread-2026-02-20_2026-04-29.md · Deals/Suno/madden-whatsapp-justo-2026-08-06.md · data/research/suno-2026-08-06.md · Deals/Suno/appendix-20-country-deepdives-2026-08-06.md
