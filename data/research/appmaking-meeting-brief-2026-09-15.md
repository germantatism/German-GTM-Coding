# Meeting Brief: Yuno <> Appmaking, Proposal Review and Full Demo

**Tuesday, September 15, 2026 · 09:00 to 09:45 COT (17:00 EEST, Cyprus and Minsk) · 45 min**
**Meet:** https://meet.google.com/nec-uorj-scr
**Event:** "AppMaking + Yuno" (organizer: German). Dzmitry Katsiushchyk, Sean Calabro and Joaquin Mann accepted. Tatsiana Gubarevich confirmed by email ("5 PM our time works perfectly") but shows as not responded on the invite. Jarrett Falasco not responded.

**Objective:** leave with the ramp-up pricing understood and accepted in principle, a list of which products beyond routing, connections and subscriptions they want to use, the remaining questions (bank introductions, Visa-side alerts, TC40/SAFE scope) closed or owned with a date, and a concrete next step: contract draft or kick-off timeline for their phase 1 providers.

Evidence labels: ✅ verified · ⚠️ inference or unconfirmed, never state in the call · 🔍 ask in discovery

### ⚠️ Pre-meeting actions
1. **Jarrett has not replied to your Slack note of tonight (18:13) and has not accepted the invite.** You told him the plan is "a full demo on the dashboard apart from what we showed them last time (routing, connections, subscriptions)" and "we want to know which products they'd like to use." If he is not confirmed by 08:30, the demo is yours: section 6 is the run order.
2. **Five minutes with Sean before 09:00.** He is on the call and he is your manager. Agree how the number is presented (final vs preliminary subject to contract), what he says if they push on price, and the honest answer on bank introductions.
3. **Verifi status.** You wrote yesterday "happy to walk you through our Visa-side coverage and roadmap on tomorrow's call." Only Ethoca (Mastercard) is publicly confirmed (April 2025 launch). An internal draft said RDR and Ethoca were "being relaunched." Get one sentence from Jarrett or Leo on where Verifi RDR/CDRN stands and say exactly that.
4. **TC40/SAFE providers.** Leo (Andres Leonardo Moreno) confirmed yesterday: Yuno reads the network files and sends a `payment.pre_chargeback` webhook per payment; dLocal delivers by SFTP; his real example came from Adyen. Neither is in their phase 1. Answer for the call: "live today with dLocal and Adyen-type providers; for Stripe, Ecompay, Unlimit, Airwallex, Shift4, Payabl and NMI we scope it together." Do not promise a consolidated report. Jira context: YSHUB-6715 and PRIOR-513 (Thiago).
5. **Connector coverage.** You have written twice ("we have full coverage with them all" on Sep 4; "full coverage of your phase 1 providers" on Sep 14) that Stripe, Ecompay, Unlimit, Airwallex, Shift4, Payabl and NMI are covered. Ecompay (ECOMMPAY), Unlimit (UNLIMINT), NMI, Airwallex and Stripe appear in Yuno's own RFP provider list; Shift4 and Payabl do not appear there. 🔍 Check the Dashboard connections catalog for Shift4 and Payabl before 09:00. If either is missing, say so before they ask.
6. **Run the calculator.** The ramp is checked by hand against the policy (all green) but the official score has not been run. Duplicate "Yuno — Pricing Palco" as "Yuno — Pricing Appmaking" (150,000 tx, AOV $18, Digital Business / Goods) so the number is documented before the Deal Desk on Wednesday.
7. **Tatsiana on the invite.** She confirmed by email; the event shows her as not responded. Re-send or ping so she has the link.

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
10. **The pricing you are presenting:** fixed fee all-in, stepped by successful transactions per month, no per-transaction fee until 150K, then $0.03 per successful transaction above 150K. Steps: $6,500 (0 to 25K), $8,000 (25,001 to 50K), $10,000 (50,001 to 100K), $13,000 (100,001 to 150K). On their curve the unit cost falls every month: $0.325, $0.267, $0.178, $0.154, $0.111, $0.108, $0.087. Months 1 to 7: $68,500 for 520K transactions. Year 1: $133,500 for 1.27M transactions ($0.105 average). Steady state: $156,000 a year. Slide: Deals/Appmaking/appmaking-pricing-ramp.png. ✅
11. **Why $13,000 and not less:** at $12,500 the implied pay-in line drops below the calculator's green floor for V3 (about $0.0188 per transaction) and needs approval. $13,000 keeps every step green with no approvals. Deal size at $13,000 a month clears the $10,000 new-logo minimum; take rate is 48 bps on $2.7M monthly TPV against 15 bps expected. ✅
12. **The internal comparison, for conversation only:** a standard structure (F3 $10,000 platform fee plus about $0.035 per transaction) would cost them about $164K in year 1 on their curve and about $183K a year at 150K; the ramp saves them about $31K in year 1 and about $27K a year after. In month 4 they are already at $0.15 per transaction. Never put this on a slide. ✅
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
3. The pricing is a stepped fixed fee that ends at $13,000 a month plus $0.03 above 150K; year 1 is $133,500. Everything green, no approvals.
4. They asked for the pricing three times in writing. It is the deliverable of this call.
5. You owe them five answers on the call: TC40/SAFE scope, Visa alerts, Japan/Brazil/Mexico acquirers, bank introductions, AI products.

**Three hooks, in priority order**
1. **A fee that grows slower than their volume.** They asked for pricing "to see profitability" on the ramp. The ladder answers exactly that: cost per successful transaction falls every month, declines cost nothing, no setup fee, no per-integration fee.
2. **Token freedom and dispute visibility, priced separately so they choose.** Their explicit asks on Sep 4 were network-token portability, TC40/SAFE, Verifi and Ethoca. All four are scoped as add-ons, not bundled, which matches the "diversify, stay independent" logic they stated.
3. **Products they have not seen yet.** Monitors (Rappi: incidents detected in milliseconds vs 5 to 10 minutes manually), reconciliation across Solidgate plus the second orchestrator plus Yuno, and Payments Concierge for a two-person payments function.

**THE objection they will raise (Dzmitry):** "$6,500 for 20,000 transactions is $0.33 each. That is expensive for month one."

**The answer:** the step is set by what you actually process, not by the calendar; month one is the only month above $0.30 and by month four you are at $0.15 and by month seven at $0.087. Over the whole ramp it averages $0.13, and year 1 lands at $0.105 all-in with every connector, KAM and TAM included. If they still push: the alternative is a standard platform fee plus a per-transaction fee, which costs more in year 1 on their own curve. Do not move $13,000; it is the floor that keeps the deal approval-free.

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

**How to read Dzmitry:** P&L first. He gave the ramp and the "profitability" framing. He decides whether $13,000 a month makes sense against the diversification benefit. Show him the unit cost curve, not the feature list.

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
| 5 | Do you introduce merchants to banks? | Sep 8 | ⬜ Deferred to the call | Honest answer agreed with Sean (section 7) |
| 6 | Pricing in writing on the ramp | Sep 8, Sep 10 | ✅ Slide ready | Present, explain, get reaction |
| 7 | AI products (Concierge, Nova) | Promised Sep 4 | ⬜ | Demo block (section 6) |
| 8 | Connector coverage in writing | Promised Sep 4 | ✅ Affirmed twice by email | Verify Shift4 and Payabl before you repeat it |

---

## 4. The pricing: how to present it

**One sentence:** "One monthly fee, all-in. It steps up as you ramp and stops at 150,000. Your cost per successful transaction falls at every step."

**The ladder (slide):**

| Step | Successful transactions / month | Expected (their curve) | Fixed fee / month | All-in per transaction at top of band |
|---|---|---|---|---|
| 1 | 0 to 25,000 | Month 1 | $6,500 | $0.26 |
| 2 | 25,001 to 50,000 | Months 2 to 3 | $8,000 | $0.16 |
| 3 | 50,001 to 100,000 | Months 4 to 5 | $10,000 | $0.10 |
| 4 | 100,001 to 150,000 | Months 6 to 7 | $13,000 | $0.087 |
| Fully ramped | Above 150,000 | Month 8 onward | $13,000 + $0.03 per successful transaction above 150,000 | Falls toward $0.03 |

**Their curve, month by month:**

| Month | Transactions | Step | Fee | All-in per transaction |
|---|---|---|---|---|
| 1 | 20,000 | 1 | $6,500 | $0.325 |
| 2 | 30,000 | 2 | $8,000 | $0.267 |
| 3 | 45,000 | 2 | $8,000 | $0.178 |
| 4 | 65,000 | 3 | $10,000 | $0.154 |
| 5 | 90,000 | 3 | $10,000 | $0.111 |
| 6 | 120,000 | 4 | $13,000 | $0.108 |
| 7 | 150,000 | 4 | $13,000 | $0.087 |
| 8 to 12 | 150,000 (held flat, they gave no number) | 4 | $13,000 | $0.087 |

**Rules to state:** the step follows successful transactions in the month, not the calendar; declines cost nothing; no setup fee; if they ramp slower they pay the higher step later, if faster, sooner.

**What the fee includes:** dedicated KAM and TAM, 1,000+ payment methods, 450+ providers, 50+ anti-fraud tools, orchestration and rules engine, smart routing and retries. Every connector maintained by Yuno; adding a provider later is a routing change, not a new fee.

**What it does not include (pending scoping, priced separately once they say which ones they want):** subscriptions engine standalone, token vault and network tokens, reconciliation, Verifi and Ethoca alerts.

**Do not say on the slide or in the room:** a minimum monthly billing line (the fixed fee is the minimum), a contract term (not discussed), PSP names as "included," approval or savings claims, the internal comparison to the standard structure, the Palco reference prices.

**If Dzmitry asks for volume-vs-calendar:** volume-based is what is proposed and it is in their favor if they ramp slower. Calendar-based is the alternative if they want fixed predictability; same total if they hit the plan.

**If they ask about the $0.03 overage:** it only starts above 150,000 successful transactions in a month, and it is the only per-transaction line in the whole structure.

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
| "Is $13,000 negotiable?" | The ladder is built so the economics work before 100K; $13,000 is what covers the stack at 150K. If they want a lower steady state, the trade is a per-transaction fee inside the steps, which costs them more on their curve. Sean decides live if anything moves. |
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

- Same-day email: pricing slide plus a one-page summary of the rules, the product checklist as they filled it, and owners and dates for anything still open (TC40 scope, Verifi, local acquirers, bank introductions).
- Run the calculator for Appmaking and file the score.
- Deal Desk framing for Sean (Wednesday 08:00): ARR $156K steady state ($133.5K year 1), close date, decision maker (Dzmitry with Butrym signing), blocker, and the ask.
- If they want the pending products, request the calculator run for each before quoting.
- Update memory: products selected, contracting entity, their reaction to $13,000, next-step date.

### Sources
Google Calendar (event "AppMaking + Yuno", Sep 15, 2026; "App Making x Yuno Dashboard Overview", Sep 4, 2026) · Gmail thread "Appmaking + Yuno: Call Recap and Next Steps" (Sep 4 to Sep 14, 2026, ten messages) · Gmail "You've been invited to Yuno" (sandbox, Sep 8) · Slack DM German and Jarrett (Sep 9, Sep 14), German and Leo (Sep 14), German and Thiago (Sep 11) · Deals/Appmaking/appmaking-pricing-proposal-2026-09-10.md (updated Sep 14) · Deals/Appmaking/appmaking-open-questions-2026-09-14.md · Deals/Appmaking/appmaking-followup-email-2026-09-04.md (call notes) · data/research/appmaking-meeting-brief-2026-09-04.md and appmaking-ltd-2026-09-03.md (company, attendees, competitive context) · docs.y.uno (network tokens, stored credentials) · Yuno RFP response to Hostinger (provider list, Aug 2026) · Finextra and Fintech Times on Yuno and Ethoca (April 2025).
