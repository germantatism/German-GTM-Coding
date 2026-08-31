# Meeting Brief: Yuno <> FlightHub

**Wednesday, September 2, 2026 · 09:30 to 10:00 COT** (10:30 to 11:00 ET, Montreal) · 30 min
**Meet:** https://meet.google.com/xnb-ebnf-cfk
**Event:** "FlightHub + Yuno" (organizer: German)

**Objective:** this is the platform walkthrough Nick asked for, with the person who built FlightHub's internal routing engine. Winning means Anna-Lena leaves seeing Yuno as the layer that makes her build better rather than the thing that replaces it, and we walk out with her volumes so the fee structure Nick asked for on June 30 can finally go out.

### ⚠️ Pre-meeting actions
- **Jarrett Falasco has not responded to the invite.** Nick scoped this call as *"maybe Anna-Lena can get a walkthrough of your platform."* A walkthrough without the sales engineer is a problem. Confirm him or reschedule the demo portion.
- **Nick Hart is on the invite as OPTIONAL and has not responded.** He is the CFO and the economic buyer. Decide deliberately whether to chase him for this one or treat this as the technical track and keep him on the recap.
- **William Wong (Toronto, Yuno's Canada lead) is not on the invite.** He was the person assigned to the Montreal in-person visit that never happened. Consider adding him so the in-person can be re-proposed with a face already in the room.
- **Two Yuno commitments from June 30 are still open:** the detailed fee structure (blocked because Nick never sent volumes) and the in-person Montreal session. Both should be closed or re-set on this call.

---

## 1. TL;DR Battle Card

**Five facts to know cold**

1. **Anna-Lena is the person Nick described as having built the internal routing platform, but her exact function is not fully pinned down.** Her own email signature says **Product Manager, FlightHub.com & Justfly.com**. ⚠️ A LinkedIn snippet (page would not fully load) lists a different title, "Marketing Manager, Compare and Ads," at what appears to be the same person (Montreal, Concordia M.A. in behavioral neuroscience, prior research associate at UC San Diego). Treat the email signature as current and correct since it is first-party and recent, but do not be surprised if her day-to-day is more data/growth-flavored than a typical payments PM. Either way, she is the one who owns FlightHub's internal routing platform per Nick, and that is what matters for the call.
2. **They store raw PANs, encrypted, and use no network tokens at all.** Nick, verbatim: *"we don't use tokens. we have the PAN and we have it encrypted right now. We haven't started using tokens."* They are PCI DSS compliant. This is the single most concrete approval-rate and PCI-scope lever on the table, and it is something her internal build cannot deliver on its own because it requires tokenization relationships at each provider.
3. **The stack is already large and growing, and confirmed in full.** Pay-in: Chase Paymentech, Stripe, **Nuvei**, Airwallex, Adyen (live as of June 30), Braintree (underlying PayPal). Payout: ConnectPay (primary, including virtual cards), plus Wex, Adyen and Airwallex being added, and Float in Canada. That is seven providers already live plus Wex incoming. Full detail in section 3 below.
4. **Their two KPIs are the only two that matter.** Nick: *"lower my cost and accept more, that's the KPIs that we always work."* No other pain was volunteered. He explicitly said Adyen had *"no pain points."* This is a low-drama, numbers-driven account.
5. **Nick already floated buy over build himself.** His own words closing the June call: *"maybe Anna-Lena can get a walkthrough of your platform and see if [it's] something that maybe it's easier for us to just integrate with you guys."* The build-vs-buy door was opened by the CFO, not by us. Do not re-open it as if it were our idea.

**Three hooks, in priority order**

1. **Network tokens across every provider.** They run raw PANs today. Network tokens lift approval rates, cut PCI scope, and survive card reissuance. Yuno provides them across all connected providers rather than one at a time, which is exactly the piece a single-company internal router cannot assemble alone.
2. **The reconciliation load that is about to get much worse, and FlightHub's own Terms of Service already admit the symptom.** One person reconciles pay-ins and payouts at merchant level today, while Adyen, Airwallex and Wex are simultaneously being added. FlightHub's own checkout terms (§15, "Payment and Credit Card Charges") state: *"multiple charges may appear on your credit card. Payment may be charged by more than one party."* That is a split-tender, multi-MID model by design, the exact pattern that makes reconciliation hard and drives cardholder confusion and disputes. Reconciliation into one ledger is the operational relief, not a feature slide, and it is already visible in their own public terms.
3. **Payouts and virtual card BINs.** Their BIN strategy is on the airline payout side: they take the customer card, mint a virtual card, and pass it to the airline, where more BIN ranges means better airline acceptance. Nick probed directly on whether Yuno issues single-use virtual cards; Justo confirmed one merchant does exactly that through Yuno's API today. Payout orchestration plus FX and rate comparison per corridor is the second half of the story most orchestrator pitches skip.

**THE objection they will raise:** *"We are building this ourselves and it goes live this quarter."*

**The answer:** agree with the build, then reframe where the work actually is. The rules engine is the visible part and Anna-Lena has clearly done it well. The recurring cost is everything underneath: maintaining each provider integration as its API changes, normalizing reconciliation and settlement files across five-plus providers, keeping PCI scope contained on stored PANs, and adding the next provider after Wex. Yuno takes that layer so she keeps owning routing strategy and rules, which is the part that is genuinely FlightHub-specific. Then add the two things no internal build produces: network tokens across all providers, and cross-merchant benchmark data from other OTAs and airlines. Never suggest her platform was the wrong call.

**The ask:** her processing volumes and average approval rate, so the fee structure Nick requested on June 30 can go out this week, plus a working session in Montreal with William Wong.

**Rapport opener:** she is new to this conversation and set the meeting herself after Nick went quiet, so lead with genuine curiosity about her build. *"Nick told us you designed the routing platform. I would rather hear how you approached it before we show you anything."* That is also the fastest route to the volumes.

---

## 2. Who Is in the Room

| Name | Role | Side | Status |
|---|---|---|---|
| Anna-Lena Schlenner | Product Manager, FlightHub.com & Justfly.com | FlightHub | ✅ Accepted |
| Nick Hart | Chief Financial Officer, FlightHub.com & Justfly.com | FlightHub | ⚠️ Optional, no response |
| Justo Benetti | CRO | Yuno | Accepted |
| Jarrett Falasco | Senior Sales Engineer | Yuno | ⚠️ No response |
| German Tatis | BDM, organizer | Yuno | Accepted |

**Anna-Lena Schlenner** (Montreal). Signs her emails **Product Manager, FlightHub.com & Justfly.com**. She personally developed the specification for FlightHub's internal traffic-distribution platform during Q2 2026, per Nick, with implementation set for the following quarter. She was out of office August 10 to 21, replied on August 24, proposed the week herself, then asked to move the time earlier the same day, which reads as someone with a full calendar who still wanted this booked. **First contact with Yuno: this call.** No prior meeting with her exists on the calendar.

⚠️ Her LinkedIn profile returned only search-engine snippets (the page itself would not load), and those snippets show a different title, "Marketing Manager, Compare and Ads," at what appears to be the same person by name, location and education. Background corroborated across LinkedIn, ResearchGate and GitHub: **M.A. in Psychology / Behavioral Neuroscience, Concordia University** (2021 thesis on midbrain dopamine and reward prediction), prior **Research Associate, Department of Neurosciences, UC San Diego**, fluent in Python (scikit-learn, pandas), MATLAB, and statistical modeling. Native German speaker.

**How to read her:** whichever title is current, she is a trained quantitative researcher, not a sales-facing executive, and she owns (or co-owns) the rules that decide where FlightHub's traffic goes. Expect skepticism of vendor claims without a measurement design and a preference for concrete numbers over narrative. Lead with specifics: rule types, BIN-level logic, token handling, reconciliation output, API surface, and where possible frame improvements as a testable lift (e.g. "here is the baseline, here is what changes, here is how we would measure it") rather than a capability list. Avoid the executive value narrative; Nick already heard it on June 30.

**Nick Hart** (Montreal). Signs his emails **Chief Financial Officer, FlightHub.com & Justfly.com** (June 27, 2026 signature). ⚠️ LinkedIn and Crunchbase list him as **Chief Corp Development Officer**, a title he was promoted into in October 2019, and **the June 30 call recording itself tags him the same way** ("FlightHub, Nick Hart, Chief Corp Development Officer"), one addition day after his CFO-signed email. Two consistent sources point to Corp Development, one recent email says CFO; use CFO in address but do not be surprised if the room or his own team refers to a broader corporate-development remit. He led the June 30 call alone (Hakan Ersoy was invited, tentative, did not join), is matter-of-fact, does not volunteer pain, and answered "I'd have to check" on approval rates because payments detail is not his day job. He is the one who asked how Yuno makes money and who asked for a fee proposal. He has not replied to any email since June 30, across five follow-ups, and is optional on this invite.

🔴 **Sensitivity, never raise:** Nick Hart was one of two FlightHub directors personally fined **CAD $400,000** in a February 2021 Competition Bureau consent agreement over drip pricing (total company + director penalty **$5.8M**, the largest such penalty at the time), carrying a 10-year prohibition on misleading pricing claims. This is public record, not a rumor, but it has no bearing on a payments-orchestration conversation and should never come up.

**Hakan Ersoy**, Chief Operating Officer, Montreal. Was tentative on the June 30 invite and did not attend. Prior: VP Technical Delivery at FlightHub; before that, **Symcor** (Canadian bank-owned payments and transaction-processing utility), a BNP Paribas joint-venture factoring business, and Fortis Commercial Finance. This is the most payments-literate executive in the account, more so than Nick, and worth pulling into a follow-up technical session even though he is not on Wednesday's invite.

**Other names in the account:** Billy Lim (accounting), Ezequiel Safirsztein. ⚠️ CEO is unclear: FlightHub's own corporate site and a June 2026 Forbes piece on the Hotels launch quote **Henri Chelhot** as CEO, while an older Forbes Business Council profile still shows **Christopher Cave** as CEO of FlightHub Group; no transition date was found. Confirm who holds the title if it comes up. Also on record: Dimitri Giouzelis (VP Finance). Yuno side: William Wong (Toronto, Canada lead, joined around June 2026), Alejandro.

**Relationship timeline**

| Date | What happened |
|---|---|
| ~Dec 2025 | First conversation between German and Nick, around FlightHub starting talks with Adyen |
| Oct 31, 2025 | Loom video "Yuno \| FlightHub" viewed |
| Feb 16, 2026 | Business Case "FlightHub + Yuno" sent, Alejandro introduces Nick as the right contact |
| Jun 26 to 27, 2026 | German reconnects; Nick replies same day: *"Yes we are just onboarding Adyen in our mix"* |
| **Jun 30, 2026** | **Discovery call, 25 min, Nick solo** (Hakan tentative, did not join). Full stack disclosed. Nick asks for a fee proposal and a walkthrough for Anna-Lena |
| Jul 6, 10, 21 and Aug 3, 10 | Five follow-ups from German. No reply from Nick to any of them |
| Aug 24, 2026 | **Anna-Lena replies**, proposes the week, negotiates the time, confirms |
| Sep 2, 2026 | This call |

**Implication:** they already have the executive pitch and a business case. What they have never received is the fee structure, because Nick never sent volumes. The path forward runs through Anna-Lena now, not Nick.

---

## 3. Call Recap: June 30, 2026 Discovery Call — Full Stack and What to Carry Into the Anna-Lena Call

**The call.** 23 minutes, Google Meet. Yuno: German, Justo (CRO). FlightHub: **Nick Hart, alone** (Hakan Ersoy was invited, tentative, did not join). Opened by referencing a prior December 2025 conversation. ⚠️ The call recording itself tags Nick as "Chief Corp Development Officer," matching LinkedIn and Crunchbase rather than his CFO email signature from three days earlier, see the title note in section 2.

### FlightHub's complete payment stack, as stated on this call (definitive)

| Layer | Providers | Detail |
|---|---|---|
| Pay-in | Chase Paymentech, Stripe, **Nuvei** (transcribed "Nuve," stated twice by Nick and confirmed again in German's closing recap), Airwallex, Adyen, Braintree (underlying PayPal) | Adyen: *"going fine, no pain points... the team is launching it as we speak."* Braintree: German flagged it from inspecting the live checkout, Nick confirmed, *"we have PayPal and all that [nonsense]."* |
| Pay-in and payout | ConnectPay | *"We also have ConnectPay on the pay-in and payout side."* |
| Payout | ConnectPay (primary today), adding **Wex**, Adyen and Airwallex; **Float** in Canada | Wex is being added specifically to the payout and virtual-card side, not just "in the pipeline" generically |
| Virtual cards | Already live via ConnectPay | Customer card in, FlightHub-issued virtual card out to the airline, for settlement |
| Tokens | **None. Raw PAN, encrypted.** PCI DSS compliant, confirmed directly | The single largest approval-rate and PCI-scope lever on the table |
| Fraud | Own internal model plus multiple data providers, primary; **Riskified explicitly "a backstop"** | *"We're pretty good with the fraud, but always interested if people have new ideas."* |

That is **seven providers already live** (Chase Paymentech, Stripe, Nuvei, Airwallex, Adyen, Braintree, ConnectPay) plus Wex incoming, split across pay-in and payout, with Float as a Canada-specific payout add.

### How they route today, and why the timing with Anna-Lena matters

No orchestration platform exists yet. Nick: *"because the majority is going to one of them we don't have... a platform to distribute the traffic... we have a few rules in place."* The only resilience today is a basic cascade: *"if it fails on one processor, it drops to the next one."* **Anna-Lena wrote the specification this quarter (Q2 2026), with implementation targeted for the following quarter.** September 2 lands squarely inside that implementation window, so ask directly where the build actually stands rather than assuming it is live.

**The BIN nuance, confirmed twice:** BINs, in Nick's usage, means the virtual cards FlightHub issues to pay airlines, not issuer BINs on the pay-in side: *"I'm talking about the cards that we're passing to the airline having multiple bins."* Justo initially read this as pay-in issuer routing and Nick redirected him mid-call. More BIN ranges means better airline-side acceptance, which is part of why Wex is being added.

**Local-processing strategy:** multiple legal entities across countries, deliberately processing locally to reduce rates; the virtual-card provider is also chosen per case to optimize cost.

**Reconciliation:** one person, merchant-level, across both pay-in and payout, today, about to get harder as Adyen, Airwallex and Wex all land at once.

**Three numbers from this call, one still missing, one now more precise:**
- Monthly transaction volume: **still never delivered.** Nick started to answer, said he would send a number, never did.
- Current approval rate: **unknown even to him.** *"I'd have to check... relatively high... I don't know off the top of my head."*
- Average ticket: **roughly USD 500 to 700**, a range, not a single point figure as earlier notes suggested; the clean recording confirms *"I would say between five and 700."*

**Settlement context:** as a travel agent rather than an operator, airline settlement runs through BSP and ARC, with GDS connectivity for reservations. Yuno orchestrates the money movement around that, not the GDS itself.

### Rules-engine proof points Justo used live, reusable in the Anna-Lena demo

- **Uber's metadata field:** Uber tags VIP customers through a free-form metadata field so those transactions are never auto-declined for insufficient funds, one example among 50-plus rule dimensions (issuing country, BIN, currency, and more).
- **Amazon Mexico case study:** a wave of US expats living in Mexico were buying on Amazon with US-issued cards; routed as international, those cards cost up to 4%; routed as domestic through a Mexican entity, roughly 1.6 to 1.9%, less on debit. A BIN and issuing-country rule fixed it. This is the same "process locally to cut interchange" logic FlightHub already runs with its own multi-entity setup, just manual today where Yuno automates it, which makes it a natural bridge into the pitch.

### What Nick actually asked for, twice, closing the call

1. **A platform walkthrough for Anna-Lena:** *"maybe Anna-Lena can get a kind of a walkthrough of your platform and see if it's easier for us to just integrate with you guys."* This is the September 2 meeting.
2. **A fee-structure proposal**, explicitly blocked because volumes were never sent: *"if you could send me a more detailed... what fees it kind of would look like for us, so I can see what makes sense."*

### What to carry into the Anna-Lena call, and what not to redo

- **Reference, do not re-explain:** the full seven-provider stack, the no-tokens/raw-PAN finding, Riskified-as-backstop, ConnectPay spanning both pay-in and payout, and the fee model (platform fee plus per-successful-transaction) are all already on record with Nick. Anna-Lena was not on this call, so a brief, confident recap is fine, but do not run this as fresh discovery.
- **Do not re-ask what Nick already answered**, even with a different person in the room: the two KPIs (cost and acceptance), the local-processing/multi-entity structure, and the airline-payout BIN logic.
- **Get the two numbers Nick never delivered:** monthly volume and current or target approval rate. This is the single most important open item for September 2, since it directly unblocks the fee proposal Nick asked for.
- **Confirm implementation status directly:** spec written in Q2, implementation targeted for Q3, which is now. Ask where the build actually stands rather than assuming June 30's plan held.
- **Reuse the Amazon Mexico and Uber examples** if the conversation needs a concrete illustration of rule depth; both already landed well with Nick and cost nothing to repeat.
- **Public corroboration of what Nick disclosed:** Affirm launched in Canada on FlightHub/JustFly in May 2024 (purchases of CAD $200 or more, Canada only); Accrue (Pay by Bank) launched on justfly.com in August 2024, explicitly to cut card-processing fees; the Riskified case study quotes a 30% approval-rate increase, an 80% drop in manual reviews, and a 75% cut in chargeback-review time, consistent with Nick's "backstop" framing. ⚠️ Braintree, Adyen and Nuvei specifically carry no public corroboration (expected, this kind of relationship is rarely publicized); they are confirmed by direct call disclosure, which is reliable but not citable externally. Payment methods accepted publicly conflict across sources; verify live at checkout before the call.
- **Two distinct payments roles were posted, not one, strengthening the build signal:** alongside "Product Manager, Payments," FlightHub separately posted a "Payment Manager / Gestionnaire des paiements" role scoped to the in-house payment tool, *"managing payment gateways and processors, optimizing transaction approval rates,"* plus two Fraud Analyst listings and a data-entry role for chargebacks and refunds. This reads as a small but real internal payments organization being staffed around Anna-Lena's platform, not a side project.

---

## 4. The Company

FlightHub is a Montreal-based online travel agency, air-ticketing-led with ancillaries and service fees, founded 2012. Company boilerplate (Aug 13, 2026): *"a leading North American online travel agency... has facilitated more than 30 million connections"* and serves *"millions of Canadians each year."* Public positioning repeats **"over $3 billion a year in sales"** and **"3 million customers per year"** (first stated 2019, repeated in a December 2025 job posting), which should be read as gross bookings, not net revenue; net revenue is not disclosed. ⚠️ Employee count estimates cluster around **100 to 200** (aggregator sources, dated Feb 2026).

**Corporate structure.** Parent is **Momentum Ventures** (Montreal), over **FlightHub** (Canada-facing), **JustFly** (US-facing), and separately **Flygreen** (private jet charter) and **Cruise-hub**. Sister company Momentum Solutions built FlightHub's Mila AI assistant. The CCAA debtor caption names the full legal group: **Flighthub Group Inc., Flighthub Service Inc., SSFP Corp., Justfly Inc., Justfly Corp., and 11644670 Canada Inc.** Justfly Inc. is CBCA-registered out of Summerside, PEI; Justfly Corp. is a Delaware entity (the reason a parallel Chapter 15 recognition exists in the US); **11644670 Canada Inc.** is the Québec-facing contracting entity named in FlightHub's own Canadian terms ("Québec permit holder #703501"). Separate Terms of Service exist for the Canadian and US sites. ⚠️ The exact card billing descriptor could not be confirmed, but the Canadian ToS (§15, "Payment and Credit Card Charges") states directly: *"multiple charges may appear on your credit card. Payment may be charged by more than one party... the total amount charged will not exceed the total price of your Booking."* That is a split-tender, multi-MID model, confirmed in FlightHub's own consumer-facing legal text.

**Recent expansion, both dated within the last three months:** **FlightHub Hotels** launched June 25, 2026 (2.6M+ properties, moving the business from air-only toward full-trip), and **PAX**, an AI travel-deals assistant, launched August 13, 2026. Both point to active product investment and a broadening surface area that will eventually touch payments (hotel merchant-of-record flows are a different beast than air ticketing).

---

## 5. Financials

**Scale (as publicly stated by the company):** "$3B+ a year in sales," "3M customers a year." No audited or independently disclosed revenue figures exist; this is a private company and third-party revenue estimates found online range so widely (from roughly $35M to over $4B depending on source and methodology) that none should be quoted as fact.

**The one hard financial event on record is the 2020 restructuring.** FlightHub was reportedly the first Canadian tech company granted CCAA protection after the onset of COVID-19: revenue fell more than 90%, Q1 2020 cumulative loss was approximately $8M, roughly 108 employees were laid off (about half the Canadian workforce), and over $19M was owed to creditors including Google and Bell. A plan of arrangement was accepted by 100% of creditors (by number and value) and implemented April 30, 2021; the CCAA proceeding was terminated by court order shortly after, with parallel recognition under Chapter 15 in the US.

**Three regulatory actions cluster in 2019-2022** (see the sensitivity flag on Nick Hart above): a **California Attorney General suit (Sep 2019)** over deceptive fees; a **Competition Bureau consent agreement (Feb 2021, $5.8M combined)** over drip pricing, concealed seat-selection fees, mid-purchase price increases and company-authored fake reviews, binding for 10 years to 2031; and a **US DOT consent order (Feb 2022, $300,000)**, described at the time as the highest civil penalty ever assessed against a ticket agent, over fare, cancellation and baggage-fee disclosures. The Competition Bureau investigation traces back to a Feb 2019 search warrant at FlightHub's Montreal HQ.

**So what for the call:** none of this is current-state distress, it is history from five to six years ago, and the company has clearly rebuilt (two product launches in the last three months). But it explains a culture that is likely cost-conscious and disclosure-cautious, and it is the backdrop against which "reduce processing fees" has been a standing KPI, per Nick, since well before this deal started.

---

## 6. Competitive Landscape

FlightHub competes as an air-focused North American OTA. Minimum-10 table below; several "competitors" are brands inside the same two large groups (Booking Holdings, Expedia Group, Trip.com Group), noted where applicable. Share bases vary and are labeled; where nothing sourced exists, no percentage is invented.

| Competitor | Segment | Est. share (source + basis) | Scale proxy (dated) | Differentiator | Payments posture |
|---|---|---|---|---|---|
| Booking Holdings (Priceline, Kayak) | Global OTA group, hotel-led | ⚠️ ~25% (derived from GM Insights 2026 gross-bookings figure vs. Booking's Q2 2026 GB; basis not stated by publisher) | Gross bookings $51.0B, revenue $7.35B, Q2 2026 | Highest-margin hotel mix | Adyen partner since 2019; merchant/MoR ~67-73% of Booking.com GB (2024-2026) |
| Expedia Group (Travelocity, Orbitz, CheapTickets) | Global OTA group | ⚠️ ~16% (same derivation basis as above) | Gross bookings $33.93B (+12%), revenue $4.32B (+14%), Q2 2026 | B2B (Expedia Partner Solutions) growing faster than consumer | Launch partner for Adyen "Intelligent Money Movement" orchestration, announced Apr 2026; ~61% merchant/MoR |
| Trip.com Group (Skyscanner) | Global OTA group, APAC-led | ⚠️ ~26% (same derivation basis) | Revenue ~US$8.9B FY2025; Q1 2026 net revenue $2.4B (+17%) | Fastest international expansion from a China core | Moved to Checkout.com localized acquiring, Mar 2026, expanding from UK/Japan/Saudi to NA/EU/ANZ |
| eDreams ODIGEO | Air-focused OTA, subscription model | No estimate available | 7.9M Prime members (+9%), adj. EBITDA €172.3M (+29%), FY26 | Monetizes via subscription (Prime) rather than ticket margin, closest business-model analogue outside pure air-agency peers | Adopted Visa's Trusted Agent Protocol for agentic bookings, Jul 2026; PayPal partnership |
| Despegar | LatAm full-service OTA | No estimate available | Revenue $774.1M FY2024 (+10%), adj. EBITDA $175.2M | Acquired by Prosus ($1.7B, closed May 2025); owns in-region payments via its Koin subsidiary | Deepest in-house payments stack in this peer set: installments, BNPL, fraud, built rather than bought |
| Fareportal (CheapOair, OneTravel) | Air-focused hybrid OTA, direct comparable | No estimate available (third-party revenue estimates for this company conflict too widely to quote) | Not reliably found | Call-center plus online hybrid model, deep air-ticketing focus | Not found |
| Hopper | Air-focused app, Montreal-based (closest local peer) | No estimate available | Bookings $7.5B, revenue $850M (+21.4%), 2024; ~40% of bookings tied to its fintech products | Monetizes the risk product (Price Freeze, Cancel for Any Reason) more than the fare itself | Runs on PayPal Braintree processing plus PayPal Hyperwallet for refunds; Capital One announced a deal in Apr 2026 to bring Hopper's tech and ~150 staff in-house |
| Kiwi.com | Air-focused OTA, virtual interlining | No estimate available | ⚠️ Latest public figures are FY2023: adj. EBITDA €34M, bookings +24% | Self-connect itineraries not sold via GDS | Not found |
| Skyscanner | Metasearch, referral only | No estimate available (68%+ of global metasearch traffic share cited by Similarweb, May 2026, a traffic basis, not revenue) | ⚠️ £540M+ revenue 2025 (aggregator estimate) | Distribution chokepoint feeding all of the above, not a direct payments rival since it takes no payment itself | No consumer payment leg |
| Google Flights | Metasearch, referral only | No estimate available | Not disclosed | Same distribution role as Skyscanner, larger reach | No payment leg |

**Where FlightHub sits:** every large peer above has made a named, dated payments move in the last 18 months (Expedia to Adyen orchestration, Trip.com to Checkout.com, eDreams to Visa's agentic protocol, Despegar building its own Koin stack). FlightHub has announced nothing publicly, while quietly building the in-house tool this meeting is about. **For the call:** this is useful context for Justo and German, not a talking point. Do not tell FlightHub they are behind peers; let the "what would it take to move faster than a peer group that is already moving" framing come from a question, not a statement.

---

## 7. News & Signals

| Date | Item |
|---|---|
| 2026-08-13 | Launched **PAX**, an AI assistant scanning for price drops, flash sales and mistake fares. Usable as a rapport opener, within the last 30 days. |
| 2026-06-25 | Launched **FlightHub Hotels** (2.6M+ properties), first major move beyond air-only. |
| 2026-01-13 | **Frontier Airlines** direct API connection live on FlightHub, extending a JustFly rollout from December 2025. |
| 2025-12-18 | FlightHub posted a **"Product Manager, Payments"** role (Montreal, bilingual EN/FR) scoped explicitly to their **in-house payment tool**: "managing payment gateways and processors, optimizing transaction approval rates." The listing is no longer live as of Aug 31, 2026, meaning it was filled or pulled. This is the strongest public corroboration that the internal build discussed on June 30 is real and resourced, and that approval-rate optimization is a named, budgeted priority rather than a side project. |

No news found in the last 7 days beyond the above.

---

## 8. Be Ready For

| They ask | You answer |
|---|---|
| "How is this different from what I already built?" | Your rules engine is the part that is genuinely FlightHub-specific and you keep owning it. What we take off you is the layer under it: maintaining each of your seven provider integrations as their APIs change, normalizing reconciliation and settlement across all of them, PCI scope, and adding whatever comes after Wex. Plus two things a single-company build cannot produce: network tokens across every provider, and benchmark data from other OTAs and airlines. |
| "What rules can you actually express?" | Over 50 fields including issuing country, BIN, currency, amount, card type, plus a free-form metadata field you populate yourself. Two examples already used with Nick: Uber flags VIP users through metadata so those transactions get special handling downstream; and a merchant routing US-issued cards used by expats in Mexico as domestic through a Mexican entity cut interchange from ~4% to ~1.6-1.9%. Routing is dynamic and can optimize on cost, approval rate, or a blend, not static failover. |
| "Do you issue single-use virtual cards for airline payouts?" | Yes, through the API. One merchant runs exactly that today. Since your BIN breadth is the lever on airline acceptance, this is where to spend demo time, alongside payout corridor and FX rate comparison. |
| "How do you make money?" | Platform fee plus a fee per **successful** transaction, so the incentive is aligned with approval rate. Justo covered this with Nick on June 30. Any actual numbers need volumes first, which is precisely the ask. |
| "We are PCI compliant already, why does tokenization matter?" | Approval rate and resilience, not just compliance. Network tokens survive card reissuance and lift authorization rates, and moving PANs out of your systems shrinks the audit surface. It also removes the migration friction when you add or swap providers. |
| "How long does integration take?" | One integration to Yuno, then providers are enabled without new merchant-side builds. Net-new provider integrations are delivered by Yuno's team, typically within a week. Jarrett should give the concrete sequencing. |
| "Can we keep Adyen, Chase, Stripe and the rest?" | Yes. Yuno is the layer above them, never a replacement. You keep every commercial relationship and every rate you have negotiated, and gain the ability to move traffic between them. |

**Landmines**
- Never imply the internal platform was a mistake or that they "lack" orchestration. Anna-Lena built it and Nick funded it. The frame is augmentation and speed.
- Do not re-pitch the executive story from June 30. She was not on that call, but Nick was, and he asked for a **walkthrough**, not a value deck.
- Do not claim Riskified is their fraud system. Nick corrected that: their own internal model is primary, Riskified is a backstop.
- Do not push pricing numbers without volumes. Get the volumes, then Justo prices it.
- Never raise the 2019 California AG suit, the 2021 Competition Bureau matter, the 2022 DOT consent order, or the 2020 CCAA restructuring. None are relevant to this conversation and one implicates Nick Hart personally.
- Do not tell FlightHub that peers like Expedia or Trip.com have already moved to orchestration or a new PSP. It reads as pressure tactics, not insight.

---

## 9. Agenda (30 minutes)

| Min | Block | Notes |
|---|---|---|
| 0 to 4 | Intro to Anna-Lena. Ask her to walk through her platform first: what she built, what stage it is at, what she optimized for | Notes: ____ |
| 4 to 12 | Yuno walkthrough scoped to her build: rules engine and the 50+ fields, BIN-level logic, dynamic vs static routing, dashboard | Notes: ____ |
| 12 to 20 | The two things her build cannot do alone: network tokens across all providers, and reconciliation into one ledger. Then payouts and virtual card BINs | Notes: ____ |
| 20 to 26 | Volumes and approval rate, so the fee structure Nick asked for can go out. Frame it as finishing what Nick started | Notes: ____ |
| 26 to 30 | Next step: Montreal working session with William Wong, and confirm who else should be in it | Notes: ____ |

---

## 10. Discovery Questions

1. Nick told us you designed the routing platform this spring. What's your role in payments day-to-day, and what did you decide to optimize for first, cost or approval rate? **Notes: ____**
2. What has been the hardest part to get right? Justo and Jarrett can compare notes honestly on where we landed differently. **Notes: ____**
3. On the pay-in side, are you routing on issuer BIN, or is the BIN work mostly on the virtual cards you pass to the airlines? **Notes: ____**
4. Nick mentioned you store PANs encrypted rather than tokenized. Is network tokenization on your roadmap, and is it blocked by the providers or by priority? **Notes: ____**
5. Who handles reconciliation across pay-ins and payouts today, and what happens to that workload once Adyen, Airwallex and Wex are all live? **Notes: ____**
6. Nick mentioned the spec was written this past quarter with implementation targeted for this one. Where does the build actually stand today? **Notes: ____**
7. What is your monthly transaction volume and current approval rate? Nick asked us for a fee structure and we have been holding on this number to give him something real. **Notes: ____**
8. What would have to be true for FlightHub to route through a third-party layer rather than finish the internal build? **Notes: ____**

---

## 11. Post-Meeting Checklist

- Same-day recap to Anna-Lena, copying Nick, closing the loop on the fee structure he requested on June 30.
- If volumes land, brief Justo immediately and get the fee structure out within the week.
- Book the Montreal working session with William Wong.
- Update memory: Nick is CFO (not Chief Corporate Development Officer), Adyen is live (not roadmap), full stack, Anna-Lena as the new primary contact.

---

### Sources
Google Calendar (event "FlightHub + Yuno", Sep 2, 2026, and prior events Jun 30, 2026) · Gmail thread "FlightHub + Yuno | Next Steps" (Jun 30 to Aug 24, 2026), thread "Catching up before my World Cup tour" (Jun 26 to 27, 2026), thread "mind if we sent the Business Case over?" (Feb 2026) · Google Meet transcript "FlightHub + Yuno", Jun 30, 2026 · Google Meet transcript "FlightHub Alignment" (internal), Jun 30, 2026 · Papermark notification, Business Case viewed Feb 16, 2026 · LinkedIn (Anna-Lena Schlenner, Nick Hart, Hakan Ersoy profiles, snippet access), Crunchbase (Nick Hart), ResearchGate and Concordia Spectrum repository (Anna-Lena Schlenner thesis), GitHub (Bionerdess) · mventures.ca/about-us · FlightHub Canadian Terms of Service (Wayback snapshot, Feb 14, 2026), §15 "Payment and Credit Card Charges" · FlightHub/JustFly press releases and job postings (PRNewswire 2019-10-23, Business Wire 2026-08-13, 2026-08-11, 2026-06-25 and 2026-04-15, news.flyfrontier.com 2026-01-13, Greenhouse careers page, Dec 2025 Payment Manager and Product Manager Payments postings) · ISED CCAA records (Flighthub Group Inc. et al.), MNP Monitor's First Report, Competition Bureau consent agreement (canada.ca, 2021-02-24), US DOT consent order (transportation.gov, 2022-02-09), CBC coverage of the 2019 California AG suit · Riskified case study, Affirm/Business Wire (2024-05-23), Accrue/Business Wire (2024-08-29) · Forbes (Jun 2026 Hotels coverage; Forbes Business Council profile) · public competitor filings and press for Booking Holdings, Expedia Group, Trip.com Group, eDreams ODIGEO, Despegar, Hopper, Kiwi.com, Skyscanner (2025-2026).
