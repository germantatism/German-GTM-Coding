# Meeting Brief: Yuno <> Appmaking, Proposal Review and Full Demo

**Tuesday, September 15, 2026 · 09:00 to 09:45 COT (17:00 EEST, Cyprus and Minsk) · 45 min**
**Meet:** https://meet.google.com/nec-uorj-scr
**Event:** "AppMaking + Yuno" (organizer: German). Dzmitry Katsiushchyk, Sean Calabro and Joaquin Mann accepted. Tatsiana Gubarevich confirmed by email ("5 PM our time works perfectly") but shows as not responded on the invite. Jarrett Falasco not responded.

**Objective:** leave with the ramp-up pricing understood and accepted in principle, a list of which products beyond routing, connections and subscriptions they want to use, the remaining questions (bank introductions, Visa-side alerts, TC40/SAFE scope) closed or owned with a date, and a concrete next step: contract draft or kick-off timeline for their phase 1 providers.

Evidence labels: ✅ verified · ⚠️ inference or unconfirmed, never state in the call · 🔍 ask in discovery

### ⚠️ Pre-meeting actions
1. **Fix slide 13 and slide 11 of the deck** (section 4.3 and 4.7): the "Expected" months and the "What it means" box are still on the first assumed ramp, and two Key Advantages bullets are FlightHub copy. Ten minutes in Google Slides.
2. **Jarrett has not replied to your Slack note of tonight (18:13) and has not accepted the invite.** You told him the plan is "a full demo on the dashboard apart from what we showed them last time (routing, connections, subscriptions)" and "we want to know which products they'd like to use." If he is not confirmed by 08:30, the demo is yours: section 6 is the run order.
3. **Five minutes with Sean before 09:00.** He is on the call and he is your manager. Agree how the number is presented (final vs preliminary subject to contract), what he says if they push on price, and the honest answer on bank introductions.
4. **Verifi status.** You wrote yesterday "happy to walk you through our Visa-side coverage and roadmap on tomorrow's call." Only Ethoca (Mastercard) is publicly confirmed (April 2025 launch). An internal draft said RDR and Ethoca were "being relaunched." Get one sentence from Jarrett or Leo on where Verifi RDR/CDRN stands and say exactly that.
5. **TC40/SAFE providers.** Leo (Andres Leonardo Moreno) confirmed yesterday: Yuno reads the network files and sends a `payment.pre_chargeback` webhook per payment; dLocal delivers by SFTP; his real example came from Adyen. Neither is in their phase 1. Answer for the call: "live today with dLocal and Adyen-type providers; for Stripe, Ecompay, Unlimit, Airwallex, Shift4, Payabl and NMI we scope it together." Do not promise a consolidated report. Jira context: YSHUB-6715 and PRIOR-513 (Thiago).
6. **Connector coverage.** You have written twice ("we have full coverage with them all" on Sep 4; "full coverage of your phase 1 providers" on Sep 14) that Stripe, Ecompay, Unlimit, Airwallex, Shift4, Payabl and NMI are covered. Ecompay (ECOMMPAY), Unlimit (UNLIMINT), NMI, Airwallex and Stripe appear in Yuno's own RFP provider list; Shift4 and Payabl do not appear there. 🔍 Check the Dashboard connections catalog for Shift4 and Payabl before 09:00. If either is missing, say so before they ask.
7. **Run the calculator.** The ramp is checked by hand against the policy (all green) but the official score has not been run. Duplicate "Yuno — Pricing Palco" as "Yuno — Pricing Appmaking" (150,000 tx, AOV $18, Digital Business / Goods) so the number is documented before the Deal Desk on Wednesday.
8. **Tatsiana on the invite.** She confirmed by email; the event shows her as not responded. Re-send or ping so she has the link.

---

## 0. What you must know cold, no excuses

1. **They run a subscription business with 95% of revenue on web and 5% on app stores** (Tatsiana, Sep 4 call). Not a store-billing merchant. ✅
2. **They already have two orchestrators**: Solidgate and a second one they refused to name ("the performance of the second orchestrator isn't so good," Dzmitry). Yuno would be the third layer, to diversify volume, PSP-agnostic, out of the flow of funds. ⚠️ Funnel evidence points to Truegate as the second; never say it. ✅
3. **Solidgate exclusivity:** by contract they cannot use Adyen, JPMorgan or Checkout.com through other gateways. None of the three goes in the proposal. ✅
4. **Phase 1 providers through Yuno:** Stripe, Ecompay, Unlimit, Airwallex, Shift4, Payabl (signed, not yet live), NMI, plus one that was garbled on the transcript (⚠️ Nuvei?). ✅
5. **Markets:** EU large, US about 40%, Japan and LatAm relevant; Pix (Brazil) and UPI (India) just started on Solidgate. ✅
6. **Their ramp, in their words (Sep 8):** 20K, 30K, 45K, 65K, 90K, 120K, 150K transactions in months 1 to 7; GMV implies AOV of exactly $18. Fully ramped in month 7. ✅
7. **What they asked for and when:** pricing in writing on that ramp (Sep 8, chased Sep 10: "Will you be able to share the pricing this week?"); TC40 and SAFE sample (Sep 8); whether Yuno introduces merchants to banks (Sep 8); TRID under their own entity, prevention alerts provider, full PSP list (Sep 14). ✅
8. **What you sent yesterday at 15:19:** TC40/SAFE flow with a generic payload and a correction of the Sep 4 recap ("per-payment notification rather than a consolidated report... live with select providers today"); TRID default (Yuno-provisioned) vs passthrough (their own `token_requestor_id`); Ethoca as the alerts network; a PSP snapshot by market (US, Europe, Japan, LatAm). ✅
9. **What you explicitly deferred to this call:** TC40/SAFE scoped against their phase 1 list; Visa-side alerts coverage and roadmap; local acquirers in Japan, Brazil and Mexico; bank introductions ("happy to discuss our network and how we typically support our merchants in those conversations," Sep 10); AI products, Payments Concierge and Nova (promised in the Sep 4 recap). ✅
10. **The pricing you are presenting (deck, slide 13):** a platform fee plus a rate per successful transaction, both stepping by the month's successful transactions: $5,000 + $0.20 (0 to 25K, ceiling $10,000), $5,500 + $0.12 (25,001 to 50K, $11,500), $6,500 + $0.065 (50,001 to 100K, $13,000), $7,500 + $0.05 (100,001 to 150K, $15,000), then $7,500 + $0.05 per transaction above 150K. Declines free, no setup fee. On their curve the unit cost falls every month: $0.45, $0.30, $0.24, $0.165, $0.137, $0.1125, $0.10. Months 1 to 7: $80,575 for 520K transactions. Year 1: $155,575 for 1.27M ($0.12). Fully ramped: $15,000 a month, $180,000 a year. Full debrief in section 4. ✅
11. **Why it is green without approvals:** platform $5,000 is the F1 list price; $7,500 fully ramped is above the F3 green floor ($6,325, list $10,000); $0.05 per transaction is above the V3 suggested ladder and far above the green floor ($0.0188); deal size $15,000 a month clears the $10,000 new-logo minimum; take rate 56 bps on $2.7M monthly GMV against 15 bps expected. ✅
12. **The internal comparison, for conversation only:** a standard structure (F3 $10,000 plus about $0.035 per transaction) would cost them about $164,450 in year 1 on their curve and about $183,000 a year at 150K. The ramp does not discount the steady state ($180,000); it halves the platform fee early, so year 1 is about $9,000 cheaper and the unit cost is $0.165 by month 4. The Sep 10 fixed-fee draft ($133,500 year 1, $156,000 steady) is superseded; the deck is what you present. Never put this on a slide. ✅
13. **Not in the fixed fee, pending scoping:** subscriptions engine standalone, token vault and network tokens, reconciliation, Verifi and Ethoca alerts. Internal reference prices from the Palco calculator run (mid-margin, never quote): Subscriptions $0.0369 per unit, Network Tokens creation $0.2973 and update $0.0595, Reconciliation $0.0188. Appmaking is high-margin and would price slightly higher. ✅
14. **Sandbox:** delivered Sep 8 ("You've been invited to Yuno" to the AppMaking account); "our technical team checked out the sandbox and loved it" (Tatsiana, Sep 10). ✅
15. **NDA:** signed by both parties; Susana sent it with the Sep 4 recap. ✅
16. **What was shown on Sep 4:** routing, connections, subscriptions (your note to Jarrett). What has not been shown: monitors, vault and network tokens, 3DS, fraud connections, reconciliation, disputes and pre-chargeback alerts, reports, PCI proxy, Payments Concierge, Nova. ✅
17. **Who they are:** Tatsiana Gubarevich, Payment Manager (role created in 2025, law and cross-border background, the operator and champion). Dzmitry Katsiushchyk, Product Manager, former CEO of a prior company, owns monetization (the economic sponsor, thinks in P&L). Katsiaryna Butrym, Lead Legal Counsel and statutory director, declined Sep 4 and is not on this invite. ⚠️ Group brand appears to be Wowmaking (Minsk, ~77 staff, bootstrapped); four Cyprus entities (Appmaking, Gototop, Applabel, Appsella); never assert the group map, let them describe it. ✅
18. **Contracting entity is an open question:** Appmaking LTD publishes the apps, Appsella LTD is merchant of record for the Atrix web funnel. 🔍 Ask which entity signs. ✅
19. **Yesterday's email affirmed things you must be able to back:** "full coverage of your phase 1 providers" (verify Shift4 and Payabl), "our direct integration with Ethoca" (public), TRID passthrough for their PSPs (docs say `token_requestor_id` is "only required for certain providers"; confirm with Jarrett that passthrough works with their phase 1 PSPs). ✅
20. **Category context, never quoted to them:** astrology and esoteric merchants (MCC 8999, high risk) run 65 to 80% approval; RevenueCat 2026 puts Google Play billing-failure churn at 31% vs 14% on the App Store. Involuntary churn is structurally large in their model, which is why TC40, alerts and retries are on their list. ✅

---

## 1. TL;DR Battle Card

**Five facts to know cold**
1. Third orchestration layer, not first: they run Solidgate and an unnamed second one and want diversification with a neutral, PSP-agnostic layer out of the flow of funds.
2. Their ramp is fast: 150K transactions a month by month 7 at $18 AOV, about $2.7M monthly GMV.
3. The pricing is a platform fee plus a rate per successful transaction, both stepping from $10,000 to $15,000 a month; year 1 on their curve is $155,575, fully ramped $180,000 a year. Everything green, no approvals.
4. They asked for the pricing three times in writing. It is the deliverable of this call.
5. You owe them five answers on the call: TC40/SAFE scope, Visa alerts, Japan/Brazil/Mexico acquirers, bank introductions, AI products.

**Three hooks, in priority order**
1. **A fee that grows slower than their volume.** They asked for pricing "to see profitability" on the ramp. The ramp answers exactly that: the all-in cost per successful transaction falls every month on their curve ($0.45 to $0.10), declines cost nothing, no setup fee, no per-integration fee.
2. **Token freedom and dispute visibility, priced separately so they choose.** Their explicit asks on Sep 4 were network-token portability, TC40/SAFE, Verifi and Ethoca. All four are scoped as add-ons, not bundled, which matches the "diversify, stay independent" logic they stated.
3. **Products they have not seen yet.** Monitors (Rappi: incidents detected in milliseconds vs 5 to 10 minutes manually), reconciliation across Solidgate plus the second orchestrator plus Yuno, and Payments Concierge for a two-person payments function.

**THE objection they will raise (Dzmitry):** "$9,000 for 20,000 transactions is $0.45 each. That is expensive for month one."

**The answer:** the band is set by what you actually process, not by the calendar; month one is the only month above $0.30, by month four you are at $0.165 and by month seven at $0.10. Year 1 lands at $0.12 all-in with every connector, KAM and TAM included, and above 150K every extra transaction is five cents. If they still push: the standard structure costs more in year 1 on their own curve. Do not move the fully ramped $15,000 yourself; Sean decides live if anything moves.

**The second objection (Tatsiana):** "The recap said TC40 and SAFE come as normalized reports across all providers. Now it is a webhook with select providers."

**The answer:** you corrected it yourself in writing yesterday. Repeat it plainly: today it is a per-payment early warning through select providers, report views are on the roadmap, and you scope their phase 1 list together. Precision is what wins with a Payment Manager whose background is compliance.

**The ask:** agreement in principle on the ladder, the product checklist filled in (section 6), a decision on which entity contracts, and a date for the contract draft or the kick-off with their phase 1 provider credentials.

**Rapport opener:** "Your team loved the sandbox, so today is the part you asked for: the number, and everything we did not get to show last time." It is 5 PM for them; keep it brisk.

---

## 2. Who is in the room

| Name | Role | Side | Status |
|---|---|---|---|
| Tatsiana Gubarevich (Hubarevich) | Payment Manager (group), role created 2025; BSU International Law; Minsk. The operator and champion; writes every email | Appmaking | Confirmed by email, not on invite response |
| Dzmitry Katsiushchyk (Dmitrii Katiushchik) | Product Manager (group) since 2021, ex-CEO Webmart Group; owns monetization; the economic sponsor | Appmaking | Accepted |
| Katsiaryna Butrym | Lead Legal Counsel, statutory director of Appmaking LTD and Gototop LTD | Appmaking | Not invited (declined Sep 4) |
| German Tatis | BDM, organizer | Yuno | |
| Sean Calabro | Head of North America, German's manager, ex-Worldpay | Yuno | Accepted |
| Joaquin Mann | Yuno | Yuno | Accepted |
| Jarrett Falasco | Senior Sales Engineer; ran the Sep 4 demo | Yuno | Not responded |
| Susana Awad | SDR, sourced the account; on the email thread | Yuno | Not invited |

**How to read Tatsiana:** precise, follows up fast, reads what you send (she caught the "full list of PSPs" and TRID points). She will test the corrections you made yesterday. Answer narrowly.

**How to read Dzmitry:** P&L first. He gave the ramp and the "profitability" framing. He decides whether $15,000 a month makes sense against the diversification benefit. Show him the unit cost curve, not the feature list.

**Sean in the room:** first client call with your new manager on this deal. He expects the ARR, close date, decision maker and blocker cold, and an ask. Have the Deal Desk framing ready for him afterwards (section 10).

**Relationship timeline**

| Date | Event |
|---|---|
| Sep 3 | Susana books "App Making x Yuno Dashboard Overview" |
| Sep 4 | Call, 44 min: Tatsiana and Dzmitry; German, Jarrett, Susana. Recap email sent same day with NDA attached |
| Sep 8 | Tatsiana sends the ramp, asks for TC40/SAFE sample and bank introductions. Sandbox invite goes out |
| Sep 10 | Tatsiana: sandbox loved, "will you be able to share the pricing this week?" German: working on it; proposes a call instead |
| Sep 14, 07:22 UTC | Tatsiana: proposes tomorrow; adds TRID, alerts provider, PSP list |
| Sep 14, 13:49 UTC | German: answers coming through the day; call tomorrow 5 PM EEST. Tatsiana confirms |
| Sep 14, 20:19 UTC | German sends the four answers |
| Sep 15 | This call |

---

## 3. Where each of their questions stands

| # | Question | Asked | Status | On the call |
|---|---|---|---|---|
| 1 | TC40 and SAFE sample and delivery format | Sep 8 | ✅ Sent Sep 14: webhook flow, generic payload, recap corrected | Scope against phase 1; name which providers are live today (Leo: dLocal by SFTP; Adyen example). Do not promise reports |
| 2 | TRID under their own entity | Sep 14 | ✅ Sent Sep 14: default vs passthrough | Confirm passthrough works with their phase 1 PSPs (🔍 Jarrett) |
| 3 | Prevention alerts provider | Sep 14 | ✅ Sent Sep 14: Ethoca | Visa side: say exactly what is confirmed, nothing more |
| 4 | Full PSP list | Sep 14 | ✅ Sent Sep 14: snapshot by market | Local acquirers Japan, Brazil, Mexico (🔍 verify names in catalog first) |
| 5 | Do you introduce merchants to banks? | Sep 8 | ⬜ Deferred to the call | Honest answer agreed with Sean (section 5) |
| 6 | Pricing in writing on the ramp | Sep 8, Sep 10 | ✅ Slide ready | Present, explain, get reaction |
| 7 | AI products (Concierge, Nova) | Promised Sep 4 | ⬜ | Demo block (section 6) |
| 8 | Connector coverage in writing | Promised Sep 4 | ✅ Affirmed twice by email | Verify Shift4 and Payabl before you repeat it |

---

## 4. Proposal Debrief: how to sell it, how to show it, and the logic behind the number

**Source reviewed:** "Proposal - AppMaking + Yuno" (Google Slides, 18 slides, last edited Sep 14, 23:37 UTC; PDF copy in Deals/Appmaking). Link: https://docs.google.com/presentation/d/1oH2wwoz3EMYLKNMARaj23AVMf_C-hkPzdfLWnVZfNmc/edit

### 4.1 What the deck is, and what to show live

| Slide | Content | Live? | Time |
|---|---|---|---|
| 1 | Cover | Yes | 10 sec |
| 2 | Agenda: 01 Why Yuno? 02 Proposal | Yes, one line | 10 sec |
| 3, 4 | Divider; 180+ currencies, 460+ integrations, 190+ countries, 1,000+ methods | Skip, they saw the platform on Sep 4 | |
| 5 | Why we believe Yuno is the right partner for AppMaking (global orchestrator, dedicated team, payments-as-a-service, awards, resilience) | Yes, 30 sec: only "dedicated team" (KAM, TAM, Solutions, Fraud and Optimization) and "resilience" | 30 sec |
| 6 | A complete suite, four pillars, one brain (orchestration, checkout and SDKs, security and risk, AI and intelligence) | Yes, as the map: "On the 4th we showed pillar 1; today the number, then pillars 3 and 4" | 1 min |
| 7, 8, 9 | Suite detail, logos, team | Skip | |
| 10 | Cases: inDrive (11 countries in 8 months, 90% approval), Rappi (new provider implementation time to zero), Livelo (14% approval increase) | Optional, 30 sec, only if Dzmitry asks for proof | |
| 11 | Key advantages (⚠️ two bullets are FlightHub copy, see 4.7) | Yes if fixed, 20 sec | |
| 12 | Divider: Proposal | Yes | |
| 13 | The pricing | Yes. The ten minutes that matter | 10 min |
| 14 to 17 | Appendix: "What Yuno unlocks" (orchestration vs single PSP, industry statistics) and customer quotes | Do not present. Leave in the PDF | |
| 18 | Close | | |

Under three minutes of deck before the number. After the number, the dashboard (section 6), not the deck.

### 4.2 The model on slide 13, exactly as built

A platform fee plus a rate per successful transaction. Both step by the month's successful transactions. Declines cost nothing, no setup fee.

| Band (successful trx / month) | Platform fee | Rate per successful trx | Total at the top of the band |
|---|---|---|---|
| 0 to 25,000 | $5,000 | $0.20 | $10,000 |
| 25,001 to 50,000 | $5,500 | $0.12 | $11,500 |
| 50,001 to 100,000 | $6,500 | $0.065 | $13,000 |
| 100,001 to 150,000 | $7,500 | $0.05 | $15,000 |
| Above 150,000 | $7,500 | $0.05 | $15,000 plus $0.05 per extra successful trx |

Fully ramped: $15,000 a month ($7,500 platform plus $7,500 in transactions at 150,000), $180,000 a year. Pending scoping, priced separately: subscriptions engine, token vault and network tokens, reconciliation, Verifi and Ethoca alerts.

⚠️ This replaces the fixed-fee-only ladder ($6,500 to $13,000) from the Sep 10 draft. The deck is the source of truth. The two differ by $22,075 in year 1 and $24,000 a year fully ramped, in Yuno's favor.

### 4.3 The deck's numbers versus their curve: fix before 09:00

The "Expected" months and the "What it means for AppMaking" box on slide 13 still sit on the first assumed ramp (fully ramped in month 10, about 675K transactions in months 1 to 9). Tatsiana's curve of Sep 8 is faster. Recomputed with the exact model on slide 13:

| Month | Their trx | Band | Platform + trx | Total | All-in per trx |
|---|---|---|---|---|---|
| 1 | 20,000 | 1 | $5,000 + $4,000 | $9,000 | $0.45 |
| 2 | 30,000 | 2 | $5,500 + $3,600 | $9,100 | $0.30 |
| 3 | 45,000 | 2 | $5,500 + $5,400 | $10,900 | $0.24 |
| 4 | 65,000 | 3 | $6,500 + $4,225 | $10,725 | $0.165 |
| 5 | 90,000 | 3 | $6,500 + $5,850 | $12,350 | $0.137 |
| 6 | 120,000 | 4 | $7,500 + $6,000 | $13,500 | $0.1125 |
| 7 | 150,000 | 4 | $7,500 + $7,500 | $15,000 | $0.10 |
| 8 to 12 | 150,000 (held flat, they gave no number) | 4 | $7,500 + $7,500 | $15,000 | $0.10 |

Replacement values for slide 13:
- "Expected" column: Month 1 / Months 2 to 3 / Months 4 to 5 / Months 6 to 7 / Month 8 onward.
- "What it means for AppMaking", sub-line "On the ramp plan you shared on Sep 8": Months 1 to 7: $80,575, 520k, $0.155. Months 8 to 12: $75,000, 750k, $0.10. Year 1: $155,575, about 1.27M, $0.12.
- Fully ramped card unchanged: $15,000 a month, $180,000 a year.

If the deck cannot be edited before the call, say it on the slide: "the months here come from our first estimate; on the curve you sent you are fully ramped by month seven, so year 1 is $155,575 and by month seven you are at $0.10 per transaction." The totals move by $1,575; the message is that you rebuilt it on their numbers.

### 4.4 The logic behind the number, in your own words

1. **Two components because that is how Yuno prices and invoices every merchant.** The platform fee pays for the stack that exists whether they send one transaction or 150,000: KAM and TAM, every connector maintained, the rules engine, monitors, the dashboard. The per-transaction rate is usage, charged only on successes. Keeping both visible is honest, and it makes "declines cost nothing" concrete.
2. **Both step because a full platform fee at 20,000 transactions would be $0.50 each.** The list platform fee for a merchant of their fully ramped size (100K to 1M a month) is $10,000. Charging it in month one is what kills ramp deals. So the platform fee starts at $5,000, the list price for a 0 to 25K merchant, and ends at $7,500, still 25% under the $10,000 list at their size. The per-transaction rate starts high ($0.20) precisely because the fixed part is low, and it falls four times, to $0.05, as volume carries the stack.
3. **The ceilings are built so the all-in unit cost falls at every step:** $0.40 at the top of band 1, $0.23 at band 2, $0.13 at band 3, $0.10 at band 4. On their curve it falls every single month: $0.45, $0.30, $0.24, $0.165, $0.137, $0.1125, $0.10. That is the headline of the slide, "a fee that grows slower than your volume," and it is true on their numbers.
4. **$15,000 fully ramped is Yuno's standard price for their size, expressed as a ramp.** The standard structure (F3 $10,000 platform fee plus about $0.035 per transaction) is about $15,250 a month at 150K. The ramp does not discount the steady state; it discounts the early months (year 1 $155,575 versus about $164,450 standard on their curve) by halving the platform fee while they grow. The argument: "you pay for the stack when the stack is carrying your volume, not before."
5. **$0.05 above 150K is the number to remember.** The platform fee never rises again; every extra successful transaction costs five cents, all-in.
6. **Volume-triggered, not calendar-triggered.** Ramp slower and they stay in the lower band longer; ramp faster and they get the lower rate sooner. Fair both ways, and it removes the "what if we miss the plan" objection.
7. **Policy check, internal, never said aloud:** platform $5,000 is the F1 list price; $7,500 fully ramped is above the F3 green floor ($6,325); $0.05 per transaction is above the V3 suggested ladder ($0.031 to $0.043 in the Palco run) and far above the green floor ($0.0188); deal size $15,000 a month clears the $10,000 new-logo minimum; take rate 56 bps on $2.7M monthly GMV against 15 bps expected. All green, no approvals. Sean has room (the platform fee could go to $6,325 fully ramped and stay green). Do not offer it; know it.
8. **The quirk to know before Dzmitry finds it.** Because the band's rate applies to the whole month, the bill can drop when crossing into a higher band: 50,000 transactions cost $11,500 and 50,001 cost $9,750; on their curve month 4 (65,000) costs $10,725, less than month 3 (45,000) at $10,900. It is in their favor. If he notices: "correct, the bands are built so growing is never penalized; the totals in the table are the ceiling of each band." Sean should know revenue dips at each band entry.
9. **Why not one flat rate.** A rate that covers the stack at 20K transactions is $0.50; one that is fair at 150K is $0.10. No single number works across a 7x ramp. The ramp is the honest version of a flat rate.

### 4.5 Step by step: the sell

1. **Before sharing the screen (1 min).** "You asked for pricing on your ramp to see profitability. I built it on the exact curve you sent on the 8th: 20K in month one, 150K in month seven." Their words, their numbers, then the screen.
2. **Slide 6 (1 min).** "On the 4th we showed routing, connections and subscriptions. Today: the number first, then the parts you have not seen, and you tell us which ones you want."
3. **Slide 13, the headline (30 sec).** Read it as written: "A platform fee plus a rate per successful transaction. Both step as you ramp: $10,000 a month at the start, $15,000 fully ramped. Declines cost nothing." Then stop for two seconds.
4. **The ramp table (2 min), top to bottom, with their months.** "Band one is your month one. Band two is months two and three. Band three, months four and five. Band four, six and seven. From month eight you are above 150K." Then the line that matters: "the totals in the table are the ceiling of each band; on your curve you pay less than the ceiling in every month except month seven."
5. **The right-hand box (2 min).** Year 1: $155,575 for 1.27M transactions, $0.12 all-in. Fully ramped: $15,000 a month, $180,000 a year, $7,500 of it platform. Say "$0.10 per transaction at scale, and five cents for every transaction above 150K."
6. **What it includes (30 sec).** KAM and TAM, 1,000+ methods, 450+ providers, 50+ anti-fraud tools, rules engine, smart routing and retries. Then: "every connector is maintained by us; adding a provider later is a routing change, not a fee." That sentence answers their diversification logic directly.
7. **Pending scoping (1 min).** Name the four. Ask which they want priced first. Fill the checklist in section 6 as they answer.
8. **Silence.** Let Dzmitry react. Do not fill it.
9. **Objections (4.6).** Sean handles anything that moves a number.
10. **Close (1 min).** "I send you this slide and a one-page summary of the rules today, with the products you pick. Which entity signs, Appmaking LTD or the web merchant of record? And what is your timeline for phase 1 credentials?"

### 4.6 Objections on the number

| They say | You answer |
|---|---|
| "$0.20 per transaction on an $18 basket is over 1%." | Only in month one and only while under 25K. Year 1 blended is $0.12 and at scale $0.10, which is 0.55% of the basket, with every connector, KAM and TAM inside. The rate falls four times as you ramp. |
| "Why does the platform fee go up?" | Because the stack is carrying more of your volume. It goes from $5,000 to $7,500 and then never moves again. At your fully ramped size the list price is $10,000. |
| "Can the platform fee stay at $5,000?" | Then the per-transaction rate cannot fall to $0.05; the two move together. Sean decides whether anything moves. |
| "What if we ramp slower than the plan?" | You stay in the lower band longer and pay the lower total. The band follows what you process, not the calendar. |
| "Why not one per-transaction rate?" | A rate that covers the stack at 20K is $0.50; one that is fair at 150K is $0.10. The ramp is the honest version of a flat rate. |
| "How does this compare with Solidgate?" | Do not compare. Yuno does not process and sits out of the flow of funds; PSP fees stay with the PSPs. This is the price of the layer above them. |
| "Is there a minimum or a lock-in?" | The platform fee is the minimum. Term is not proposed yet; it goes in the written proposal once products are confirmed. |
| "What do subscriptions, vault and reconciliation cost?" | Priced separately once scoped; tell us which you want first and the numbers go in the written proposal. Never quote the Palco reference prices. |

### 4.7 Fixes in the deck before 09:00

- **Slide 13:** "Expected" months and the "What it means" box (values in 4.3). Sub-line: "On the ramp plan you shared on Sep 8."
- **Slide 11, Key Advantages:** two bullets are inherited from the FlightHub deck. "Your routing platform stays, Yuno extends it" → "Your current providers stay, Yuno adds an independent layer". "Network tokens across all seven providers" → "Network tokens across your phase 1 providers" (they do name seven, but the sentence was written for FlightHub). "Higher approvals, lower cost" and "Reporting and analytics" are fine.
- **Slides 15 and 16 (appendix)** carry industry statistics ("4 to 16% approval boost," "8 to 12% uplift with local APMs," "20 to 40 integrations monthly"). Keep them as appendix. If asked for Yuno figures, the published ones are 7% approval uplift and 30% recovered revenue.
- **Slide 5** is the standard pillar slide; fine as is.

---

## 5. Bank introductions: the answer to agree with Sean

Tatsiana's exact words (Sep 8): "we understand you're purely a technical orchestrator, but do you have any practice of introducing your merchants to banks?" Your reply (Sep 10): "happy to discuss our network and how we typically support our merchants in those conversations during our next call."

What can be said truthfully: Yuno has commercial relationships with the acquirers and PSPs on its catalog; when a merchant needs a new acquiring relationship for a market, Yuno can make the introduction to its contacts at those providers and the merchant contracts directly; Yuno does not act as a paid referrer, does not take part in the underwriting, and does not sit in the flow of funds. 🔍 Agree with Sean whether there is anything more formal to offer (named partner managers, a preferred-partner program) before you say it. Do not invent a program.

Context that makes this question important to them: they are MCC 8999 (high risk) with a web funnel; their sibling brand rotates four merchant-of-record entities across Cyprus, Hong Kong, the US and Dubai. Acquirer access is a real constraint for them, not a curiosity.

---

## 6. Demo plan: what has not been shown, and the product checklist to fill live

Your note to Jarrett: "a full demo on the dashboard apart from what we showed them last time which was routing, connections, and subscriptions. we want to know which products they'd like to use."

| Block | What to show | Why it matters to them | Interested? (fill live) |
|---|---|---|---|
| Monitors and alerts | A monitor on approval rate by provider with automatic traffic redirection; alerts to email | They diversify across orchestrators because "the performance of the second orchestrator isn't so good." Monitors are how they see that in minutes | ____ |
| Vault and network tokens | Vaulted card charged across two connections; enrollment with Yuno TRID or their own (passthrough); token lifecycle | Their Sep 4 ask: tokens "owned by you, usable inside Yuno and outside it." Pending scoping line | ____ |
| 3DS | Dynamic 3DS by rule, one authentication above the PSP layer | EU-heavy volume; they raised 3DS and Apple Pay decryption above the PSP layer on Sep 4 | ____ |
| Fraud connections | Antifraud tools plugged as connections; risk conditions in routing | High-risk MCC; a two-person payments function | ____ |
| Disputes and pre-chargeback alerts | The `payment.pre_chargeback` webhook (TC40/SAFE) and Ethoca alert flow; dispute response through one API where the provider supports it | Their explicit ask. State the provider scope honestly | ____ |
| Reconciliation | One ledger across Yuno, Solidgate and the second orchestrator (standalone reconciliation accepts external sources) | Four entities, several processors, tiny finance team. Pending scoping line | ____ |
| Reports | Approval by provider, country, BIN; export | Dzmitry's P&L view of the bake-off | ____ |
| Payments Concierge | Ask it a routing question, let it propose a change, confirm it | Promised Sep 4 | ____ |
| Nova | Whatever Jarrett is cleared to show | Promised Sep 4. If nothing is demo-ready, say it is in rollout and offer a follow-up | ____ |
| Subscriptions engine (recap only) | One screen if they ask about standalone pricing | Shown Sep 4; pending scoping line | ____ |

Owner: Jarrett if confirmed; otherwise German drives and Joaquin supports. Keep the demo to 15 minutes; the number is the point of the call.

---

## 7. Be ready for

| They ask | You answer |
|---|---|
| "Can you send the pricing in writing after the call?" | Yes, the slide plus a one-page summary of the rules, same day. |
| "What is the contract term?" | Not defined yet; propose it in the written proposal after they confirm products. Do not improvise a term on the call. |
| "Is $15,000 negotiable?" | $15,000 fully ramped is the standard price for their size; the ramp already halves the platform fee while they grow. If they want a lower steady state, the platform fee and the per-transaction rate move together. Sean decides live if anything moves. |
| "Which providers have TC40/SAFE today?" | The ones Leo confirmed. Not their phase 1 list. Scope together. |
| "Is Verifi live?" | Exactly what was confirmed internally, nothing more. |
| "Do you have Shift4 and Payabl?" | Only if verified in the catalog before the call. |
| "Can we keep our own TRID?" | Yes, passthrough: they register as token requestor and send `token_requestor_id` by API. Confirm it works with their phase 1 PSPs. |
| "Which entity should contract?" | Their call: Appmaking LTD or Appsella LTD (the web funnel merchant of record). Butrym signs for the Cyprus entities. |
| "Can you introduce us to acquirers in Japan or LatAm?" | Section 5 answer. Name the markets, take the ask, come back with names. |
| "How fast can phase 1 go live?" | Connections come up in days once credentials exist; the integration is one API and web SDK. Only quote a timeline Jarrett or Joaquin stands behind. |

**Landmines:** never "you don't have an orchestrator" or "your PSP shortlist is open"; never name Truegate; never include Adyen, JPMorgan or Checkout.com; never promise consolidated TC40/SAFE reports; never quote subscriptions, vault or reconciliation prices before the calculator is run; never assert the Wowmaking name or the four-entity group map; never quote their Play reviews or refund complaints; never mention the FTC case against Genesis; no em-dashes in the follow-up.

---

## 8. Agenda (45 minutes)

| Min | Block | Notes |
|---|---|---|
| 0 to 5 | Open: thank them for the sandbox feedback; confirm the three things for today (answers, pricing, demo); questions on yesterday's email (TC40/SAFE, TRID, Ethoca, PSPs) | Notes: ____ |
| 5 to 20 | Pricing: the slide, the rules, their curve month by month; reaction from Dzmitry; what is pending scoping and which ones they want | Notes: ____ |
| 20 to 25 | Bank introductions and local acquirers (Japan, Brazil, Mexico) | Notes: ____ |
| 25 to 40 | Demo of what was not shown (section 6), filling the product checklist as you go; Concierge and Nova | Notes: ____ |
| 40 to 45 | Close: contracting entity, next step (written proposal with products confirmed, then contract draft), kick-off timeline for phase 1 credentials | Notes: ____ |

---

## 9. Discovery questions

1. On the curve you sent, what drives the ramp: new traffic to the Atrix funnel, migration of existing volume from the other orchestrators, or both? Notes: ____
2. What share of the 150K would come through each phase 1 provider, and which ones are live today versus signed? Notes: ____
3. Which of the pending products (subscriptions standalone, vault and network tokens, reconciliation, Verifi and Ethoca) do you want priced first, and which are a later phase? Notes: ____
4. Which entity contracts with Yuno: Appmaking LTD or the web funnel merchant of record? Who signs? Notes: ____
5. For TC40/SAFE: is visibility on your phase 1 providers a launch requirement or a nice-to-have once live? Notes: ____
6. On bank introductions: which markets and which type of relationship do you need (local acquiring, cross-border, alternative methods)? Notes: ____
7. What does "fee only on successful transactions" mean for you when a retry succeeds after a decline: one billable transaction, correct? Notes: ____
8. What is your internal timeline for a decision and a go-live for phase 1? Who else needs to approve? Notes: ____
9. What would make you route more than the planned share to Yuno versus the other two layers? Notes: ____

---

## 10. Post-meeting checklist

- Same-day email: slide 13 (corrected) plus a one-page summary of the rules, the product checklist as they filled it, and owners and dates for anything still open (TC40 scope, Verifi, local acquirers, bank introductions).
- Run the calculator for Appmaking and file the score.
- Deal Desk framing for Sean (Wednesday 08:00): ARR $180K steady state ($155.6K year 1), close date, decision maker (Dzmitry with Butrym signing), blocker, and the ask.
- If they want the pending products, request the calculator run for each before quoting.
- Update memory: products selected, contracting entity, their reaction to $15,000, next-step date.

### Sources
Google Calendar (event "AppMaking + Yuno", Sep 15, 2026; "App Making x Yuno Dashboard Overview", Sep 4, 2026) · Gmail thread "Appmaking + Yuno: Call Recap and Next Steps" (Sep 4 to Sep 14, 2026, ten messages) · Gmail "You've been invited to Yuno" (sandbox, Sep 8) · Slack DM German and Jarrett (Sep 9, Sep 14), German and Leo (Sep 14), German and Thiago (Sep 11) · "Proposal - AppMaking + Yuno" (Google Slides, 18 slides, PDF in Deals/Appmaking, reviewed Sep 14) · Deals/Appmaking/appmaking-pricing-proposal-2026-09-10.md (Sep 10 draft, superseded by the deck model) · Deals/Appmaking/appmaking-open-questions-2026-09-14.md · Deals/Appmaking/appmaking-followup-email-2026-09-04.md (call notes) · data/research/appmaking-meeting-brief-2026-09-04.md and appmaking-ltd-2026-09-03.md (company, attendees, competitive context) · docs.y.uno (network tokens, stored credentials) · Yuno RFP response to Hostinger (provider list, Aug 2026) · Finextra and Fintech Times on Yuno and Ethoca (April 2025).
