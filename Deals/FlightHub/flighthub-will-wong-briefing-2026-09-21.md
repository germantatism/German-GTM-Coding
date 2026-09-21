# FlightHub: full account briefing for Will Wong

**INTERNAL. Do not forward outside Yuno.** Prepared Sep 21, 2026 for the in-person meeting on Sep 22.

**Meeting:** "Yuno x Flighthub, In-Person". Tuesday Sep 22, 2026, 11:00 to 12:00 ET.
**Where:** 3333 Boulevard Côte-Vertu Ouest, Suite 600 (6th floor), Saint-Laurent, Montreal. Room SR-71 (the room resource lists a Meeting Owl and a TV, so remote participants are possible).
**Invite status:** Anna-Lena Schlenner (organizer, accepted), Nick Hart (no response), Will (accepted), German (accepted), Justo (optional, no response). Jarrett is not on the invite.

---

## 1. TL;DR battle card

1. **This is a build-plus-buy conversation, not a displacement.** FlightHub runs its own rule-based routing layer across seven providers. It is already live and a couple of years old. Anna-Lena owns it and wants to "improve it significantly". Our position since day one: Yuno extends what she built, she keeps control of routing strategy.
2. **The strongest hook is network tokens.** Nick on Jun 30: "we don't use tokens. we have the PAN and we have it encrypted right now." They are PCI DSS compliant. Tokens across all seven providers is something a single-company build cannot assemble alone.
3. **Anna-Lena's own stated want is ML routing.** Her rules are manual ("pick this provider second, or randomly go through them"). Verbatim on Sep 2: she would prefer to make it as automated as possible, where she can trust a model to make the decision and improve the success rate. She asked whether we already have models that know which BIN approves better on which processor. Jarrett's A/B test framing landed well.
4. **We have real numbers from her (Sep 3 email):** 500K to 800K transactions per month depending on seasonality, success rate 80% to 92% "depending on how you calculate it", average ticket of sale transactions about $800 CAD. All processors and currencies combined.
5. **A proposal exists and they have never seen it.** No price has ever been shared with FlightHub, only the model (platform fee plus a fee per successful transaction, declines free). German told her on Sep 8 the proposal would be reviewed together at the workshop, and she replied she is "looking forward to meeting William and discussing the proposal". She expects it tomorrow.
6. **Only two KPIs matter to the CFO.** Nick: "lower my cost and accept more." He volunteered no pain ("Adyen is going fine. No pain points."). The urgency comes from Anna-Lena, not from Nick.
7. **Nick is the economic buyer and has been silent since June 30.** The meeting was moved from Sep 18 to Sep 22 specifically so he could attend, but he has not answered the invite. Getting him in the room, even for 15 minutes, is the single most valuable outcome.

**What changed since the Jun 30 internal alignment call you were on.** Back then German described an internal engine "going live next year" and "about five providers". Both are now corrected: the routing layer is already live, the provider count is seven, and the contact who matters is Anna-Lena, who has been in her role only since January 2026 and inherited the acquiring rules rather than building them.

---

## 2. People

| Name | Role | Notes |
|---|---|---|
| **Anna-Lena Schlenner** | Product Manager, FlightHub.com & Justfly.com (email signature) | Day-to-day counterpart and emerging champion. In the role since Jan 2026. Quantitative background (M.A. in behavioral neuroscience, Concordia; Python and statistics). Wants evidence and measurement design, not narrative. Fast and reliable on email: she set the Sep 2 call herself, sent the volumes within 24 hours, booked the room for tomorrow. |
| **Nick Hart** | Chief Financial Officer (his signature; Hakan also calls him "our CFO"). LinkedIn and the Gong tag say Chief Corp Development Officer | Economic buyer. Took the Jun 30 call alone, asked how we make money, asked for a fee proposal and a walkthrough for Anna-Lena. Then ignored five follow-ups (Jul 6 to Aug 10). Matter-of-fact, numbers-driven, not a payments specialist ("I'd have to check" on approval rate). |
| Hakan Ersoy | Chief Operating Officer | Routed us to Nick in Feb 2026. Was tentative for Jun 30 and did not join. Background includes Symcor (Canadian payments utility), so likely the most payments-literate executive. Not on tomorrow's invite. |
| Billy Lim, Ezequiel Safirsztein | Accounting / unknown | Named only in Anna-Lena's out-of-office. No contact. |

Yuno side so far: German (owner), Justo (CRO, led Jun 30 with Nick), Jarrett Falasco (SE, ran the Sep 2 demo), Alejandro Albarracín (early outreach in Jan and Feb), Will (tomorrow).

---

## 3. Timeline

| Date | What happened |
|---|---|
| Late 2025 | German's outbound reaches Nick while FlightHub is starting talks with Adyen. A Loom was sent in Oct 2025; first conversation around Dec 2025. |
| Jan 29 to Feb 20, 2026 | Alejandro sends success-case emails, then offers an outside-in business case to Hakan (Feb 13). Hakan adds Nick: "Nick, our CFO, would be the best person." German follows up Feb 20 on the Adyen angle. No reply on record, and no record that the business case was ever walked through. Assume they have not seen it. |
| Jun 26 to 27 | German re-engages. Nick replies the same day: "Yes we are just onboarding Adyen in our mix. We can certainly chat." |
| **Jun 30** | **Discovery call, 25 min. Nick alone with German and Justo.** Full stack disclosed. Nick asks for a fee proposal and a platform walkthrough for Anna-Lena. Justo offers an in-person visit; Nick agrees. Same day: internal alignment with Will and Jarrett. |
| Jul 6, 10, 21, Aug 3, 10 | Five follow-ups to Nick. No reply. On Aug 3 German adds Anna-Lena to the thread. |
| Aug 24 | Anna-Lena replies after her time off and books the call herself. |
| **Sep 2** | **Demo call, 33 min. Anna-Lena alone with German and Jarrett.** Nick was optional and did not join. |
| Sep 2 | German sends recap and asks for monthly transaction count, approval rate, average ticket. |
| **Sep 3** | **Anna-Lena sends the numbers** and offers Sep 15, 17 or 18 for the in-person. |
| Sep 3 to 4 | German builds the proposal (deck plus Deal Calculator) and reviews pricing with Sean Calabro. |
| Sep 8 to 9 | Anna-Lena says Nick cannot make Friday the 18th. German asks to move it so Nick can attend. She confirms Tue Sep 22 at 11:00. |
| Sep 10 to 15 | She sends the calendar invite with a reserved room; Will confirms the address with her. |

---

## 4. What we know about their payments setup

**Business.** Montreal online travel agency, air-led, under Momentum Ventures. FlightHub is the Canada-facing brand, JustFly the US-facing one. Multiple legal entities across countries, used deliberately to process locally and lower rates. As a travel agent, airline settlement runs through BSP and ARC; we orchestrate the money movement around that, not the GDS. Recent launches: FlightHub Hotels (Jun 2026) and PAX, an AI deals assistant (Aug 2026).

**Provider stack, as stated by Nick and confirmed by Anna-Lena**

| Layer | Providers |
|---|---|
| Pay-in (acquiring) | Chase Paymentech, Stripe, Nuvei, Airwallex, Adyen (went live around Jun 30), Braintree (behind PayPal) |
| Both acquiring and issuing | ConnexPay (appears as "Connect Pay" in our transcripts). Anna-Lena called it "one of our biggest ones". |
| Issuing / payout | ConnexPay today; Wex being added on the issuing side; Adyen and Airwallex being added for payouts; Float in Canada |
| Seen at checkout | Cards, Apple Pay, PayPal, Affirm (German's inspection, Jun 2026) |

**How they route today.** Rules by currency and other conditions, then a fixed cascade: if one processor fails, it drops to the next. Anna-Lena: the rules system has existed "for a couple of years" and predates her. The selection of the second provider is manual or random.

**The issuing side is where she is building new things.** They take the customer's card, create a virtual card, and pass it to the airline. She is working on a "BIN rotation engine" that smart-selects the issuer, and possibly the BIN, based on inputs such as the airline and the office used. When Nick says "the more BINs we have the better", he means these virtual cards, not issuer BINs on the pay-in side. Justo misread this live on Jun 30 and Nick corrected him. Wex is being added partly to widen that BIN pool.

**Integration speed.** Most provider integrations take them about a month. Adyen was "way more complicated than any other integration" because Adyen is asynchronous and everything else they run is synchronous, which forced workarounds. When Jarrett said we could help her get there faster, her answer was: "yes, let's do that."

**Tokens and PCI.** No tokens at all. Raw PAN, encrypted, PCI DSS compliant.

**Fraud.** Their own internal model plus several data providers. Riskified is only "a backstop". Nick: "We're pretty good with the fraud, but always interested if people have new ideas."

**Reconciliation.** One person reconciles pay-ins and payouts at merchant level, while three providers are being added at once.

**Numbers.** 500K to 800K transactions per month; success rate 80% to 92% depending on the calculation; average sale ticket about $800 CAD. Nick had earlier said the ticket was "between five and 700" (USD).

---

## 5. What each call covered

**Jun 30 with Nick (Justo led).** Stack and entity structure; how traffic is distributed (no platform, a few rules, basic fallback); KPIs; virtual cards to airlines; reconciliation; what Yuno is (infrastructure across pay-ins and payouts, 50+ rule fields, metadata field); two examples that landed (Uber flagging VIPs through metadata; the Amazon Mexico case where US-issued cards routed as domestic dropped cost from about 4% to about 1.6 to 1.9%); payout orchestration with FX comparison by corridor; the no-tokens discovery and the network token pitch; our pricing model. Nick asked directly whether we issue single-use virtual cards. Justo answered that one merchant does that through our API today. Nick closed with: "maybe Anna-Lena can get a walkthrough of your platform and see if... it's easier for us to just integrate with you guys."

**Sep 2 with Anna-Lena (Jarrett led the demo).** Her opening question was whether we would "sit on top of everything... to replace the structure that we have right now". Jarrett's answer: extension first, no lift-and-replace, she stays in control. Shown or explained: API-only integration (they keep their front end), connections library, no-code routing, condition sets (BIN, issuing country, card brand, with or without CVV, stored credentials, metadata), volume splits for A/B tests, smart routing on conversion and latency using cross-portfolio data, decline groups and automatic failover, the new routing recommendation feature, vault and network tokens and account updater (mentioned, not demoed), 3DS through an external MPI (mentioned), Payments Concierge, and taking over maintenance when providers force API upgrades. Jarrett's proof point: a large Middle East airline that kept its own orchestration layer and paired it with Yuno. On speed he said a net-new connection is live in one to two days once credentials exist, three to five days with QA. She asked if we cover payouts as well as pay-ins (yes; Uber uses us for payouts in several emerging markets). She asked how we make money and for a ballpark; German declined to give a number without volumes.

Jarrett said openly that he did not get through a full demo: "this was just the tip of the iceberg" was the framing used to set up tomorrow.

---

## 6. What we have NOT discussed yet

- **Any price.** They know the model only.
- **The proposal and the business case.** Never shown.
- **Network tokens in depth.** Pitched to Nick, mentioned to Anna-Lena, never demoed. How their stored PANs would move into a vault has not come up at all.
- **Reconciliation.** Raised with Nick in one exchange. Never discussed with Anna-Lena.
- **The issuing side.** We have not explored whether or how Yuno plays in her BIN rotation engine or in virtual card issuing beyond Justo's one-line answer.
- **Whether they use 3DS today,** and where.
- **Fraud.** Not explored beyond Nick's description.
- **Volume and approval rate by provider, by currency and by entity.** We only have blended totals.
- **What the 500K to 800K count includes.** She gave ticket size specifically for "sale transactions", so the count may include other transaction types. Because ConnexPay does both sides, it could even include issuing. This moves both pricing and the business case.
- **Decision process, timeline, budget, signer, procurement and security review.** Nothing known.
- **Competition.** No other vendor has been mentioned. The alternative is continuing the internal build.
- **Engineering capacity and roadmap** for the internal platform (two payments roles were posted in Dec 2025, so the build is staffed).
- **APMs and new markets.** Not discussed with either contact.
- **Contract terms.** The deck proposes three years; never raised.

---

## 7. Open commitments

**Ours**
- The fee structure Nick asked for on Jun 30. This is the proposal. Still undelivered after 12 weeks.
- A deeper capability walkthrough in person (promised in the Sep 2 recap: "We didn't walk through our full capability stack today").
- **ConnexPay coverage.** Jarrett said he had seen it for pay-ins and would double-check payouts. No answer was ever sent. Have one before walking in.
- Justo's claim that one merchant issues single-use virtual cards through our API. Confirm the details with Justo before repeating it; Nick probed this point on purpose.

**Theirs**
- Nothing outstanding. Anna-Lena has delivered everything she promised. Nick never sent volumes, but hers cover it.

---

## 8. The proposal (built, not shared)

**Files.** Live deck: [Proposal - FlightHub + Yuno](https://docs.google.com/presentation/d/1O7nRB5nFt5DGSt_tnGsa0cY7HVQhui4CoCS_gJthczI/edit) (Google Slides, about 20 slides). Pricing model: [Yuno, Pricing FlightHub](https://docs.google.com/spreadsheets/d/1bWgHIGL3cRwUl51LBmoiSquhD18wb1443M8CtRV6SOc/edit) (Deal Calculator). The PDF in the repo is an older export and is not the current version.

**Structure.** Why Yuno (standard slides, with the key-advantages slide tailored: "Your routing platform stays, Yuno extends it" and "Network tokens across all seven providers"), then a two-slide business case, then one pricing slide, then a generic appendix.

**Business case.** Base case 700,000 monthly attempts (inside her 500K to 800K), $580 average ticket (consistent with her $800 CAD at roughly 0.72 to 0.73, and inside Nick's $500 to $700), which gives $4.87B of annual attempted volume. Baseline approval 86% (midpoint of her 80% to 92%), target 90%.

| Lever | Assumption | Conservative | Average | Optimistic |
|---|---|---|---|---|
| L1 Conversion uplift (network tokens plus best-acquirer routing) | +2.5 pts | $13.7M | $18.3M | $22.8M |
| L2 Smart routing and retries | +1.5 pts | $8.2M | $11.0M | $13.7M |
| L3 Processing cost reduction | 7.5 to 12.5 bps on TPV | $3.7M | $4.9M | $6.1M |
| L4 Run-ops reduction | 4 to 5 FTE at $100K | $0.40M | $0.45M | $0.50M |
| **Total annual** | | **$26.00M** | **$34.65M** | **$43.10M** |

The +4 points equal 28,000 recovered sales per month, about $195M of annual gross bookings, valued at a 15% net take benchmark. The deck states clearly that 86% is a working assumption and that the real baseline gets measured together before anything is committed. That sentence is the right posture with Anna-Lena. The arithmetic was rechecked today and is internally consistent.

**Pricing on the slide**

| Item | Value |
|---|---|
| Platform fee | $10,000 per month |
| Tier 1, 0 to 175,000 successful transactions | $0.06 |
| Tier 2, 175,001 to 350,000 | $0.05 |
| Tier 3, 350,001 and above | $0.04 |
| Minimum monthly billing | $25,000 (bites below 265,000 successful transactions) |
| Included | Orchestration, network tokens, rules engine, smart routing and retries, dedicated KAM and TAM |
| Pending review, not priced | Nova AI, reconciliation, monitors |
| Term | 3 years, rates locked, tiers reviewed annually |

At 602,000 successful transactions (700,000 attempts at 86%): $39,330 per month, $471,960 per year, $0.065 all-in. Low season at 430,000: $32,450 per month. Peak at 688,000: $42,770 per month. Against the average business case that is roughly 73 to 1.

**Internal context, not for the room.** The Deal Calculator's suggested ladder for this volume is $0.0333, $0.0292, $0.0260 (about $30K per month all-in), so the deck is quoted above it on purpose. Sean's feedback on Sep 3: the structure is fine, the $580 ticket supports a higher per-transaction fee, and we normally need either a platform fee or a monthly minimum rather than both, though both is good if we can get it. There is real room to move. Do not negotiate tomorrow; collect reactions and bring them back.

**Where they will push, and what to say**
- *"Where does +4 points come from?"* It is a working assumption inside her own stated range. Offer the A/B split Jarrett described: a share of traffic through Yuno, measured against her current rules, per provider and per market. She will respect a measurement design more than a benchmark.
- *"15% net take is not our number."* My assessment: 15% is likely high for an air-led OTA, and a CFO will spot it. Ask for their real take rate rather than defending ours. Sensitivity calculated today: at a 5% net take, the approval levers are worth about $9.7M, and the total is still about $15M per year against less than $0.5M of cost. The case survives.
- *"Why both a platform fee and a minimum?"* Note the reaction, do not concede in the room.
- *"We already built this."* Agree. She keeps the rules. We take the layer underneath (seven integrations to maintain, forced API upgrades such as Adyen's, token relationships per provider, reconciliation across all of them) and add two things a single-company build cannot produce: network tokens everywhere and cross-merchant routing data.

**Fix before anyone presents it**
1. Re-export the PDF from the live Slides. The repo PDF still has a slide titled for "CPD" (a CellPoint leftover), shows network tokens as pending instead of included, and carries a bank-oriented compliance slide that does not apply.
2. Both business case slides contain a stray "$ 0.71" text box. Check visually and delete.
3. Provider counts are inconsistent: the deck says 460+ integrations and +450 providers, Justo said "over 500" on Jun 30, Jarrett said "700 plus" on Sep 2. Pick the deck number and stick to it. Anna-Lena will notice.
4. Confirm what the 500K to 800K includes before treating 700,000 as pay-in attempts.
5. Consider one added slide on how the lift would be measured (A/B split, baseline per provider). It is the slide this audience wants most.

---

## 9. Risks and landmines

- **No stated pain at the CFO level and no compelling event.** Sean's first question about this deal was "why are they talking to us?" The honest answer: Anna-Lena wants ML routing and faster integrations, and Nick wants lower cost and higher acceptance, but nobody has said what happens if they do nothing.
- **Nick may not show.** Have a plan to get 15 minutes with him, or a firm follow-up date with him, before leaving the building.
- **Never imply the internal platform was a mistake** or that they "lack" orchestration. Never say "replace".
- **Do not call Riskified their fraud system.** Their own model is primary.
- **Do not confuse the two BIN conversations.** Pay-in issuer BIN routing is ours to pitch. Virtual card BINs to airlines is her issuing project.
- **Never raise FlightHub's regulatory history** (2019 to 2022 consumer-pricing matters, one of which involved Nick personally) or the 2020 restructuring. None of it is relevant.
- **Do not use peer pressure** ("Expedia and Trip.com already moved"). It reads as a tactic.
- **Transcripts are machine-generated.** Quotes here are lightly cleaned; treat wording as close, not exact.

---

## 10. Suggested run of show (60 minutes)

| Min | Block |
|---|---|
| 0 to 5 | Introductions. Will as the local face and long-term owner of the relationship in Canada. |
| 5 to 15 | Her turn first: where the routing layer stands today, what "improve significantly" means to her, where the BIN rotation engine is. |
| 15 to 35 | The capabilities Sep 2 did not reach: network tokens, vault and account updater; the A/B design for smart routing; reconciliation into one ledger; monitors; payouts. Decide today who drives the dashboard, since Jarrett is not on the invite. |
| 35 to 50 | The proposal: two business case slides, then pricing. Present the baseline as theirs to set. |
| 50 to 60 | Next steps: data for a measured baseline, a technical session with Jarrett, Nick's involvement, decision path and timing. |

---

## 11. Questions to get answered in the room

1. Does the 500K to 800K monthly count cover sale attempts only, or all transaction types? Pay-in only, or issuing as well?
2. How do you calculate success rate at the low end (80%) and the high end (92%)? Per attempt or per order after cascade?
3. What is the volume and approval split by provider? Which provider takes the majority today?
4. Is network tokenization on your roadmap? What has kept it off so far, priority or the providers?
5. Do you run 3DS today? On which flows and markets?
6. Where does the BIN rotation engine stand, and is the issuing side something you would want a partner in, or is that staying in-house?
7. What happens to reconciliation once Adyen, Airwallex and Wex are all live?
8. How much engineering time goes into maintaining the seven integrations today?
9. What would you need to see to run a split test through Yuno? Who approves it?
10. Who else weighs in on a decision like this besides you and Nick? Is there a budget cycle or date that matters?
11. What is your real net take rate, so we can replace our benchmark in the business case?

---

### Sources
Gmail threads "FlightHub + Yuno | Next Steps" (Jun 30 to Sep 15, 2026, all 28 messages read), "Catching up before my World Cup tour" (Jun 26 to 27), "mind if we sent the Business Case over?" (Feb 2026). Google Meet transcripts: FlightHub + Yuno Jun 30, FlightHub Alignment Jun 30, FlightHub + Yuno Sep 2 (all read in full). Gong account summary (2 calls, 81 emails). Google Calendar event for Sep 22. Slack: DM with Sean Calabro Sep 3, #travel-requests Sep 10 to 11. Live Google Slides "Proposal - FlightHub + Yuno" (last modified Sep 4) and the Deal Calculator "Yuno, Pricing FlightHub". Meeting brief of Sep 2, 2026 (`data/research/flighthub-meeting-brief-2026-09-02.md`) for company background.
