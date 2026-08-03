# Riot Games + Yuno: Meeting Brief
*Call: Friday, July 31, 2026, 11:00 to 11:30 AM Colombia time (COT), Google Meet (meet.google.com/hdf-nnsf-sie)*
*Prepared 2026-07-30. Sources: full Gmail thread, Yuno research brief v8.0 (2026-07-10), fresh web research 2026-07-30.*

---

## 1. Who Will Be in the Meeting

| Name | Company / Role | Status |
|------|----------------|--------|
| **Andreas Borngraeber** (aborngraber@riotgames.com) | Riot Games, title not public | Confirmed by email ("tomorrow, Friday 11am Colombian time") |
| **German Tatis** | Yuno, Business Development Manager | Organizer |
| **Samuel** (samuel@y.uno) | Yuno | Accepted |
| **Justo Benetti** (justo@y.uno) | Yuno, CRO | Optional invitee, has not responded |

**ACTION NEEDED: Andreas is NOT on the calendar invite.** The event only has German, Samuel and Justo. German told Andreas "Will send invite over," so aborngraber@riotgames.com still needs to be added to the event or the meeting link sent to him. Alejandro Albarracin (Head of GTM) is on the email thread but not on the invite either.

**Andreas Borngraeber, what we know:**
- Introduced by the CSO on 2026-07-29 as the person "who can follow up for a discussion." No public title anywhere on the web; his role is not listed on LinkedIn or Riot pages.
- Replied at 11:06 AM Central European Time using a German-language email client ("Am Do., 30. Juli 2026 um 04:23 Uhr schrieb"). Inference: he is a German speaker, very likely based in Europe, plausibly at Riot's Dublin EMEA hub (the entity that bills EEA, UK, Brazil and all markets outside US/KR/JP/SEA) or the Berlin office.
- Probable but UNCONFIRMED background match: Andreas Borngräber of Munich, former Geschäftsführer (managing director) of TG Payment GmbH, the payments subsidiary of Travian Games, and Prokurist of Travian Games until 2012. If correct, he has a payments-in-gaming career going back 15+ years and will be a sophisticated buyer. Verify on LinkedIn before referencing this in the call.
- Contextual signal: Riot currently has an open "Business Development Manager, Payments" role (18-month contract, Dublin city centre, onsite) whose remit is managing PSP relationships, negotiating commissions and deal structures, and financial modeling of payment opportunities. Andreas very likely sits in or near that payments partnerships org, alongside Goncalo Pereira (payment partnerships), whom German also touched in the sequence.
- Professional courtesy note: he moved Abhi to BCC in his reply, a clean operator move. Expect a structured, no-fluff conversation.

**Abhi "Gorn" Ramprasad, the CSO who made the intro (not expected on the call):**
- Chief Strategy Officer at Riot Games since 2021. Owns Corporate Strategy, Business Health & Analytics, Corporate Development, Platform & Strategic Partnerships, and the Office of the CEO.
- Ex-McKinsey, roughly 10 years there before Riot.
- He answered a 4-touch cold sequence and delegated downward. A top-down intro from the CSO means Andreas takes the meeting with a real mandate. Reference the intro once ("Abhi connected us") and do not overplay it.

**Relationship history in one paragraph:** German ran a 9-contact cold sequence at Riot (Jul 14 to Jul 29, 4 touches, last touch included the yunoforgaming deck). One rejection came from Tolga Tekin, R&D engineering: "Our internal teams handle payments for my org, and they handle it well." Abhi replied Jul 29 introducing Andreas. German sent a strong reply-all recap (orchestration over the in-house build, 94%+ auth in gaming with local acquiring, 460+ integrations, IAP fee bypass on Riot Points, gaming clients MoonActive, NetEase Games, Garena, Bonoxs, plus the deck deck.yuno.tools/m/riot-games), CC'ing Justo and Alejandro. Andreas proposed Friday 11 AM COT; German confirmed. Andreas already has the full pitch in writing, so the call should build on it, not repeat it.

---

## 2. What Riot Games Does (Deep Summary)

**Company:** Founded 2006, HQ in Los Angeles, 100% owned by Tencent since 2015. Valuation around $21B, estimated revenue roughly $3B for 2025 (Levvvel estimate; Riot is private and does not disclose). About 93% of revenue comes from virtual items: skins, bundles, battle passes and in-game currency (Riot Points, Valorant Points). CEO Dylan Jadeja (since 2023, previously CFO, led the 2015 Tencent equity sale). Marc Merrill is CPO and co-founder; Brandon Beck co-founder. Two rounds of cost discipline: 530 layoffs in Jan 2024 (11% of staff, Riot Forge closed) and the 2XKO team cut roughly 50% within three weeks of launch in late 2025. Regional financials that are public: Riot Games Korea 2025 revenue about $334M (+10.8%), and the Dublin EMEA entity reported profits of €587M (Irish Times, Oct 2025).

**Games portfolio and platforms:**

| Game | Genre | Platforms | Notes |
|------|-------|-----------|-------|
| League of Legends | MOBA | PC (own Riot Client) | Flagship, 130M+ monthly players, roughly $1.7 to 1.8B of revenue. LoL Classic mode just launched Jul 29, 2026 |
| Valorant | Tactical FPS | PC, console (since 2024) | Roughly $0.9 to 1.3B revenue, fastest-growing web traffic (+12% MoM) |
| Valorant Mobile | Tactical FPS | Mobile, China only so far | Launched Aug 19, 2025 with Tencent LIGHTSPEED; 50M+ MAU in China; global rollout expected 2026. THE catalyst |
| Teamfight Tactics | Auto-battler | PC + mobile (iOS/Android) | Mobile side monetizes through app-store IAP |
| Wild Rift (LoL mobile) | MOBA | Mobile | $500M+ lifetime revenue; SEA web store runs on Codashop |
| Legends of Runeterra | Card game | PC + mobile | Smaller title |
| 2XKO | Fighting | PC, console | Launched Oct 2025, team downsized after launch |
| Riftbound | Physical trading card game | Tabletop | Aggressive 2026 roadmap, international rollout |

Plus the Arcane/Netflix media arm and the largest esports operation in the world (Worlds, MSI, VCT; the LCK was absorbed into Riot Games Korea).

**Countries and structure:** Riot operates globally and bills through five regional entities (from its own Terms of Service): Riot Games Inc. (Americas except Brazil), Riot Games Korea, Riot Games LLC (Japan), Riot Games Services PTE (Singapore, for SEA), and Riot Games Ltd. Dublin (merchant of record for EEA, UK, Brazil and every other market). Top traffic: US #1 for both major titles; LoL skews Vietnam, Korea, Germany, France; Valorant skews India (#2), Philippines, Turkey, Indonesia. Very heavy emerging-market weight, exactly where local payment methods and auth rates matter most.

---

## 3. Payments Infrastructure

- **In-house payments and commerce platform**, no third-party orchestrator. Self-hosted checkout at pay.riotgames.com with a dedicated "Payments Checkouts, Publishing Platform" engineering team. They self-integrate PSPs and aggregators region by region.
- **Confirmed providers, stitched per region:** Paysafe (paysafecard, EU/US/UK, embedded in Valorant), BoaCompra by PagBank (LATAM cash rails and local cards), Codashop / Coda Payments (SEA partner web store, 40+ local methods), Boku direct carrier billing (Bahrain, Egypt, Jordan, Kuwait), plus a Mastercard global partnership (esports sponsorship expanded into payment technology integration).
- **Five billing entities** mean payment operations run market by market rather than through one layer. Dublin is MoR for a huge and diverse set (EEA, UK, Brazil, rest of world).
- **Antifraud: in-house rules, visibly aggressive.** Riot's own support pages document a 24-hour velocity block that counts declined attempts, standing FAQs for "charged for RP without receiving it," mobile partial-charge failures, chargeback-driven account bans, and a strict 90-day refund window. This pattern reads as false declines on high-intent buyers plus reconciliation gaps. No third-party fraud vendor is publicly identifiable.
- **3DS: not publicly verifiable** (checkout and support pages are JS-rendered). Treat as unknown and ask in discovery; Yuno brings 3DS, network tokens and account updater built in.
- **Active payments hiring on both sides of the org:** "Business Development Manager, Payments" (Dublin, 18-month contract: PSP relationship management, commission and deal negotiation, financial modeling) and "Manager, Software Engineering, Payments" (Los Angeles). They are investing in payments AND scrutinizing PSP economics right now.

---

## 4. Payment Methods (Direct/Web Rails, Top Games)

On mobile app versions (TFT, Wild Rift, LoR, Valorant Mobile) purchases run through Apple/Google IAP at 15 to 30% store fees. Outside the stores, on their own rails, this is the confirmed footprint:

| Game / Region | Methods confirmed (official Riot or partner sources) |
|---------------|------------------------------------------------------|
| League of Legends (in-client RP top-up, global) | Visa, Mastercard, Amex, Discover, Visa Electron, PayPal, paysafecard, prepaid/gift cards |
| LoL / Valorant Brazil | Pix (dedicated official support articles for RP and VP) |
| LoL Mexico | OXXO, SPEI, Telcel carrier top-up, 7-Eleven cash |
| LATAM (AR, CL, CO, PE, MX) via BoaCompra | Cash rails (Pago Facil, Rapipago, Bapro, LinkPagos, Cobro Express), local cards, card installments (3/6/9/12 months) |
| Wild Rift SEA via Codashop | GCash, PayMaya, GrabPay, GoPay, Wave Money; carrier billing (Singtel, M1, StarHub, Globe, Smart, MPT, Telenor); 7-Eleven retail |
| Korea | KakaoPay, Naver Pay, Toss (low confidence, confirm live) |
| MENA (BH, EG, JO, KW) | Boku direct carrier billing for League of Legends |
| Valorant (VP top-up) | Same in-house checkout; paysafecard partnership confirmed |

**Critical framing rule (from our own research): NEVER tell Riot they "lack" a payment method.** Their local bench is one of the deepest in gaming. The conversation is auth rates, provider performance, cost, reliability and speed-to-market for new titles and markets, never absence.

---

## 5. Relevant Payments News

1. **Riot is hiring a BD Manager, Payments in Dublin (18-month contract)** to renegotiate PSP commissions and deal structures and to model new payment opportunities. They are actively benchmarking their PSP economics at this exact moment. This is the single best-timed signal we have.
2. **Mastercard expanded its global partnership with Riot** beyond esports sponsorship into payment technology integration.
3. **Coda Payments partnership** covers SEA with 40+ local methods and third-party ecommerce distribution of in-game currency.
4. **Boku direct carrier billing** live for LoL in Bahrain, Egypt, Jordan and Kuwait, cardless payments for the MENA push.
5. **Paysafe/paysafecard partnership** embedded in Valorant (EU/US/UK reach, cash-adjacent prepaid).
6. **Dublin EMEA entity profits of €587M** (Oct 2025 reporting): the payments-relevant entity is large, profitable and under cost scrutiny.

---

## 6. Relevant Company News

1. **LoL Classic launched Jul 29, 2026** (Season 3 style mode, big re-engagement play). Two days old at meeting time, easy rapport opener with a payments-relevant tail: engagement spikes drive top-up spikes.
2. **Riot x Discord account linking** announced Jul 22, 2026.
3. **Give Back Bundle raised $6.5M** for the Riot Social Impact Fund (Jul 16, 2026).
4. **New parental controls in the US** (Jul 15, 2026), includes spend visibility.
5. **Riftbound 2026 roadmap:** four card sets, regional qualifiers across NA, EU and APAC (Lille, Atlanta, Sydney, Vancouver, Barcelona, Singapore, LA), French and Traditional Chinese language support coming.
6. **2XKO 2026 roadmap** continues (four more champions) despite the team cuts.
7. **Cost-discipline backdrop:** 530 layoffs Jan 2024, 2XKO cuts Oct 2025, "fewer, high-impact projects" mandate under CEO Dylan Jadeja.

---

## 7. Expansion Plans

- **Valorant Mobile global rollout is the anchor catalyst.** China-only since Aug 2025 with 50M+ MAU. Global launch expected 2026, no official date; industry speculation (unconfirmed) points to a possible reveal around Gamescom Cologne, Aug 27 to 29, 2026, where Tencent is showcasing 40 titles with "some making their global debut." Prioritized regions reported: Asia, North America, Europe. The monetizable base skews to India, Philippines, Turkey, Indonesia and Brazil, exactly the local-rails markets.
- **MENA:** dedicated LoL MENA servers launched (Arabic localization, culturally adapted content), Valorant MENA servers, Boku carrier billing already live in four markets. MENA gaming revenue forecast around 11% CAGR through 2027.
- **India:** Riot has signaled intent to expand (Valorant traffic is #2 there; talk of India servers for all titles). If they go deeper, UPI-first payment reality becomes central.
- **Riftbound international rollout:** new languages and worldwide competitive circuit, a physical-product commerce motion on top of digital.
- **Platform expansion:** Valorant on console, 2XKO multi-platform, LoL Classic re-engagement.

---

## 8. Sales Angle

**Core frame: an orchestration layer ON TOP of the in-house platform they are proud of. Never "replace," never "you lack."**

Four hooks, in priority order:

1. **PSP economics and leverage (lead with this given who Andreas likely is).** They are hiring someone in Dublin to renegotiate PSP commissions. Yuno makes every provider compete for every transaction: smart routing by performance and cost, volume shifting as negotiation leverage, failover recovering declines. Case: Rappi, 15% lower processing cost, $1M saved via routing.
2. **Valorant Mobile global launch readiness.** Standing up local acquiring and methods market by market in-house is quarters of engineering per market; through Yuno it becomes configuration, live in weeks. Direct web top-ups recover the 15 to 30% the app stores take on every IAP transaction. Case: InDrive, 10 markets live in under 8 months, 90% approval.
3. **False declines and top-up reliability.** Their own support docs show a 24h velocity block counting declined attempts, charged-but-no-points and mobile partial charges. That is recoverable revenue from high-intent buyers: smart routing (+7% approval typical), NOVA fraud scoring cutting false declines, automatic retries, unified reconciliation. Case: Livelo, +5% approval, 50% recovery.
4. **Cost discipline alignment.** Under Jadeja's "do more with less," orchestration frees the payments engineering team from per-region integration maintenance and turns processing cost into a managed lever.

**Gaming proof points:** MoonActive, NetEase Games, Garena, Bonoxs.

**Landmines:**
- Do not imply their platform or local coverage is deficient. Respect the build first; it earns the right to discuss what sits on top.
- Expect the Tolga Tekin objection ("internal teams handle it well"). Answer: agreed, and that is exactly who we serve; Yuno makes the internal platform perform better and cheaper, keeping their providers and their checkout.
- Andreas already received the full written pitch and deck. Repeating it cold will read as not listening; reference it and go deeper instead.
- Abhi is in BCC by Andreas's own choice; mention the intro once, then leave the CSO out of it.
- 3DS, orchestrator absence and fraud tooling are educated inferences from public sources; ask, do not assert.
- This is a 30-minute first call: discovery over demo.

---

## 9. Agenda for the Call (30 min)

| Time | Block |
|------|-------|
| 0 to 3 min | Intros. Thank the Abhi connection once. One line of rapport (LoL Classic launch two days ago). Confirm Andreas's role and remit |
| 3 to 13 min | Discovery: his scope, how payments is organized (LA engineering vs Dublin partnerships), PSP performance management, priority markets, Valorant Mobile payments readiness |
| 13 to 21 min | Yuno positioning tailored to what he said: orchestration over the in-house platform, routing and provider leverage, local acquiring for expansion markets, IAP bypass on direct rails. One or two gaming cases max |
| 21 to 26 min | Map to Riot's calendar: Valorant Mobile global launch, MENA/India push, PSP renegotiation cycle |
| 26 to 30 min | Next steps: propose a technical deep dive with solutions engineering plus a Riot-specific business case (approval uplift + processing cost + IAP recovery). Agree owner and date before leaving the call |

---

## 10. Open-Ended Questions

1. "What does your remit cover at Riot: PSP partnerships, payments product, or the full payments P&L? And how does the team split between Los Angeles and Dublin?"
2. "How are you thinking about payments readiness for Valorant Mobile's global launch? Will monetization run only through the app stores, or is a direct web top-up rail part of the plan from day one?"
3. "How do you measure PSP performance today, approval rates by market and provider, and what happens when one underperforms?"
4. "I saw you are bringing in a BD Manager for payments in Dublin focused on PSP deal renegotiation. How do you build leverage in those negotiations today with volume committed per region?"
5. "Which markets are hardest for you right now, whether on approval rates, cost, or local method coverage?"
6. "Your support docs show fairly strict velocity rules on top-ups. Who owns the balance between fraud prevention and false declines, and how do you measure the revenue you lose to blocked legitimate players?"
7. "What would need to be true for Riot to put an orchestration layer over the platform you have built, and who besides you would weigh in on that decision?"

---

*Prepared by German's AI assistant. Sources: Gmail thread "Payments at Riot Games"; Yuno research brief riot-games-2026-07-10.md; riotgames.com news; The Paypers (Mastercard, Coda); Paysafe resource center; Boku press release; builtin.com/themuse.com job listings; Irish Times; Sportskeeda/pley.gg (Valorant Mobile, speculation flagged); Inven Global (Riftbound roadmap).*
