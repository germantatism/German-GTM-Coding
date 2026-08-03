# Meeting Brief: Yuno <> Eventbrite

**Tuesday, August 4, 2026 · 16:30 to 17:00 COT (30 minutes) · https://meet.google.com/zoj-mucn-hyd**
Organizer: German Tatis · Prepared 2026-08-03

> **Read this first, three things reframe the whole call.**
> **1. THIS IS A FORMAL ORCHESTRATOR EVALUATION, NOT COLD DISCOVERY.** Paul's email to German (quoted 2026-08-03) asks for *"specific examples of how your integrations with Braintree, Stripe, Adyen and J.P. Morgan Payments support marketplace use cases"* and states *"we are speaking with several other orchestrators."* They have already concluded that their self-built failover is not enough and are comparing vendors. The competition is no longer the status quo; it is other orchestrators.
> **2. The attendee is a payments infrastructure veteran, not a generalist.** Paul Pasion's career arc is Amazon, Marqeta (card issuing), Uber (marketplace payments and payouts at scale), and most recently Director of Payments Product and Engineering at Recurly (subscription billing). His own public bio reads "Payments and tech nerd." Someone who writes that email is not a curious browser; he is the person holding the technical checklist, almost certainly running the evaluation.
> **3. Eventbrite is no longer NYSE: EB.** Bending Spoons S.p.A. (Milan) closed its acquisition on **2026-03-10** at $4.50 per share, roughly $505M, and the stock was delisted. Julia Hartz, CFO Anand Gandhi, CPO Ted Dworkin, CLO Lisa Gorman and the entire board are gone. Bending Spoons IPO'd on Nasdaq (BSP) on 2026-07-01. Calling Eventbrite public, citing earnings calls, or naming Hartz as CEO would be an immediate credibility loss.

**Objective, what winning looks like:** advance to the technical round of the bake-off with evidence, not slides. Concretely: leave with a scheduled working session where Yuno demonstrates the four named connectors against their marketplace flows, plus the evaluation's timeline, criteria and decision makers.

## The email, decoded

Paul's message carries four signals beyond its literal ask:

1. **The four connectors he named are the evaluation scope: Braintree, Stripe, Adyen, J.P. Morgan Payments.** Three of them (Braintree, Stripe, Adyen) are already among Eventbrite's five listed payment sub-processors, so he is testing whether Yuno layers on top of the existing estate without an engineering project.
2. **What he did NOT name matters: Cybersource and Mercado Pago.** Both are on their sub-processor list and absent from his question. ⚠️ Inference: that silence hints at where the strategic core of the evaluation sits, and possibly which rails are not part of the future stack. Do not assert it; note it.
3. **J.P. Morgan Payments is NOT in their current stack. This is the big signal.** A merchant with 71.6% of revenue in the US putting JPM on the list is evaluating adding a direct bank acquirer, almost certainly for cost (direct acquiring economics on large US volume, possibly consolidating with a treasury bank). The read for Yuno: **the orchestrator they pick is probably the vehicle for bringing JPM in without building another in-house integration.** Whoever makes that migration look easy has structural advantage in this deal.
4. **"Marketplace use cases" is the hard question, deliberately.** Eventbrite is a merchant of record with a two-sided flow: collect from the attendee, hold funds ($278M payable to creators), run reserves and chargebacks, pay out to creators (3% Instant Payout in the US). In processor language that means the platform products: Stripe Connect (which they already use for payouts in US/UK/CA/AU), Adyen for Platforms, Braintree marketplace tooling, and JPM's equivalent. He is probing whether an orchestrator's connectors reach **platform depth** (fund splits, sub-merchant KYC onboarding, payout ledgers) or only cover auth/capture/refund. Many orchestrators have the logo but only in simple pay-in mode. He is filtering who advances on evidence.

Also: *"we are speaking with several other orchestrators"* is partly classic negotiating posture to pressure price and urgency. Behind it there is a real evaluation, which is good news: intent and budget exist. Probable rivals given the peer context in this brief: **BR-DGE** (used by Resident Advisor), **ProcessOut** (Checkout.com-owned, used by Fever), and the usual **Spreedly, Primer, Gr4vy, Payrails**.

**Yuno's escape from the feature-matrix trap:** BR-DGE, Primer and Spreedly cannot say what Yuno can, that one layer covers **pay-in AND pay-out plus antifraud, KYC and reconciliation**. For a merchant of record holding $278M payable to creators, that is exactly the frame that breaks a connector-by-connector comparison.

## ⚠️ Pre-meeting actions

| Action | Why |
|---|---|
| **Open https://www.linkedin.com/in/phpasion/ logged in and read his current title and start date.** | His career history is verified from third-party databases, but **his Eventbrite title is not in any public source**, and every database still shows him at Recurly. That lag is consistent with a recent move, but it is inference. Two minutes logged in confirms what he actually owns. |
| **Confirm Jarrett Falasco is attending.** | Still needsAction on the invite. |
| **Get gong@y.uno to accept, or the call is not recorded.** | Still needsAction. |
| **Build the four-connector capability matrix at the 11:30 SYNC** (meet.google.com/bex-zuij-hyf, with Jarrett and Justo, both still needsAction). | Paul asked for specific examples on **Braintree, Stripe, Adyen and J.P. Morgan Payments**. Before the call you need, per connector: operations supported, tokenization, payouts, and above all whether Yuno supports the **platform modes** (Stripe Connect, Adyen for Platforms, Braintree marketplace, the JPM equivalent) or standard acquiring only. ⚠️ This is internal Yuno knowledge that could not be verified from this session; it must come from Justo and Jarrett. Standing rule: what is not verified is not asserted on the call; the answer is "I will confirm that with the technical detail in the working session." |
| **Prepare 1 or 2 real marketplace examples (Rappi, InDrive)** with the detail of which processors they route and whether payout is in the flow. | "Specific examples" is literally what he asked for. He is filtering who advances on evidence, not slides. |
| **Authorize the Gmail connector** (claude.ai → Settings → Connectors → Gmail). | This brief only learned about Paul's email because German pasted it. The full thread (tone, history, whatever else was said) remains unread by this workflow, and next runs should read it directly. |

**Calendar history, checked explicitly:** searched the calendar by Paul's email, his surname, the eventbrite.com domain and "Bending Spoons". **No prior meeting with any attendee of this call exists.** The only related events are your own prep blocks today (14:30 solo, 16:00 with Jarrett and Justo, which has a recording saved) and tomorrow's SYNC. Gong is not configured in this environment, so there is no call history either. **First video call, but not a cold start: the email exchange already established intent.**

---

# 1. TL;DR Battle Card

### Five facts to know cold

1. **You are talking to a payments builder.** Paul Pasion: Amazon, Marqeta, Uber, and Director of Payments Product and Engineering at Recurly. Issuing, marketplace payments, and recurring billing, end to end. ✅ career verified · ⚠️ Eventbrite title unverified.
2. **Eventbrite is the merchant of record and carries payments in its own P&L.** Under Eventbrite Payment Processing the 10-K states it "is the merchant of record," acts as principal and books revenue gross. FY2025: net revenue $291.8M, cost of net revenue $94.5M (32%), 78.9M paid tickets, gross ticket sales over $3.0B. ✅
3. **Their own 10-K names processing fees as the biggest cost line.** Verbatim: *"Processing fees are the largest component of cost of net revenue."* And: *"Our payment processing costs for credit and debit card payments are generally lower outside of the United States due to a number of factors, including lower card network fees and lower cost alternative payment networks."* ✅
4. **Five payment vendors, self-built failover, no third-party control plane.** Eventbrite's own sub-processor page lists under Payment Services: **Cybersource (Visa), Adyen B.V., Braintree (a division of PayPal), MercadoLibre, and Stripe**. The 10-K: *"We have multiple integrations in place at one time allowing for back up processing alternatives on our payments system if a single provider is unable or unwilling to process any given transaction, payment method or currency."* ✅
5. **On the final earnings call, the company named your pitch as its own plan.** Julia Hartz, 2025-11-06: *"increasing localization and monetization in our existing regions through **the addition of more payment options** and expanded creator tools."* Same call: *"Eventbrite is used in 180 countries every year."* ✅

### Three hooks, in priority order

| # | Hook | Why it lands on this person |
|---|---|---|
| **1** | **The international monetization gap, in their own numbers.** 41% of paid tickets are non-US but only 28.4% of revenue is. Their 10-K says processing costs run lower internationally on local rails. Brazil, Mexico, Argentina, Singapore and Hong Kong currently transact on cards. | He has run payments at Uber and Marqeta. He will immediately understand that a ticket-to-revenue mix gap is partly acceptance and partly method economics, and he can act on it. |
| **2** | **Routing economics, not redundancy.** They have five vendors and hand-rolled failover. The open question is what decides which processor takes a transaction: availability, or cost and auth rate. | This is a peer conversation, not a pitch. Ask him how it works today and let him tell you where it hurts. |
| **3** | **Decline recovery and payout mechanics.** Chargeback and refund provision fell from $27.5M (FY2024) to $16.1M (FY2025). 3DS2 runs only in the European perimeter. They hold $278.2M payable to creators, run reserves, and state they do not provide currency conversion. | Recurly is a dunning-and-retries business. This is his native vocabulary, and the payout side is where Uber-scale experience shows up. |

**The single sharpest fact you hold:** they have already migrated processors twice. Square was their *"primary online payment processing partner"* on a five-year deal signed 2017 and terminated in **January 2020**, two years in. Stripe came in from 2023. And their own FY2019 10-K wrote the consequence down: *"**Our costs for payment processing may increase with a new partner** due to higher direct costs of development and implementation and fee structure."* You are not arguing that switching processors is expensive. They filed it.

**Fourth hook, for a Milan audience:** the parent's IPO prospectus states that in Q1 2026, 75% of group revenue came through electronic payments, 67% of that via "providers such as Adyen, PayPal, and Stripe" and 33% via app stores at 15% to 30% against "5% or less" for processors, with a dedicated risk factor headed "A significant portion of our products depend on third-party payment processors." One integration absorbing each acquired brand's rail is a portfolio thesis.

### THE challenge he will put, and the answer

The old objection ("we already have failover, why add a layer?") **is dead: they killed it themselves by opening a formal evaluation.** The real test is now:

> **"Do your Braintree, Stripe, Adyen and JPM connectors reach platform depth for marketplace use cases, or just auth, capture and refund?"**

**Answer discipline:** only what the 11:30 matrix confirmed gets asserted. For everything else, verbatim: "I will confirm that with the technical detail in the working session, and I would rather show you than tell you." Then pivot to the frame competitors cannot match: "The part I can tell you today is that we treat your model as what it is, a merchant of record with a two-sided flow. Orchestration for you is not just routing the pay-in; it is the payout side, the fraud layer, KYC onboarding for organizers and reconciliation across processors, in one layer. That is the conversation where a connector checklist stops being the whole picture."

He may also probe the fund-flow question directly: **if a payment is collected on one processor but the creator payout runs on another rail, how does the ledger reconcile while preserving the MoR model?** If the matrix has not confirmed the answer, take it to the working session; do not improvise.

**Second challenge, the comparison itself: "We are speaking with several other orchestrators."** Do not flinch and do not disparage anyone. "That is the right way to run this. What I would ask is that the comparison include the payout and reconciliation side, because that is where marketplace orchestration actually gets hard, and where the differences between us and the pay-in-only players show up." It is also partly negotiating posture; the correct response to posture is process questions, not concessions.

**Third: "Payments decisions sit with Bending Spoons now."** Convert it: "That makes it a bigger conversation, not a smaller one. Their own prospectus quantifies this at the portfolio level. Point me at whoever owns routing in Milan and let us bring them in."

### The ask

Advance to the technical round: a working session where Yuno demonstrates the four named connectors against their actual flows, with the routing owner present. Walk out with the evaluation's **timeline, decision criteria, and who else is at the table**, all normal questions in a bake-off. Also confirm whether **JPM is something they are already negotiating or something they want the orchestrator to enable**.

### Rapport opener

His background. "Marqeta, Uber, Recurly is about as complete a payments arc as it gets, issuing through marketplace through recurring. What pulled you to ticketing?" Specific, verifiable, flattering. **Then the question that earns the whole call:** "When you say marketplace use cases, what weighs most for you: fund splits, organizer onboarding, payouts, or the funds-holding side?" His answer tells you exactly what to demo and reveals the real pain. **Do not open on the acquisition or the layoffs.**

---

# 2. Who Is in the Room

| Name | Role | Side | Invite status |
|---|---|---|---|
| German Tatis | Account Executive | Yuno | Organizer, accepted |
| Justo | Yuno | Yuno | Accepted |
| Jarrett Falasco | Yuno | Yuno | ⚠️ No response |
| gong@y.uno | Call recorder | Yuno | ⚠️ No response, recording at risk |
| **Paul Pasion** | Payments (⚠️ Eventbrite title unconfirmed) | Eventbrite | Accepted |

### Profile: Paul Pasion ✅ identity · ✅ career · ⚠️ current title

**LinkedIn: https://www.linkedin.com/in/phpasion/** (private to logged-out viewers, so the profile itself could not be read; everything below comes from corroborating sources, each labeled).

| Field | Detail | Source and confidence |
|---|---|---|
| Most recent documented role | **Director, Payments Product and Engineering, Recurly** | RocketReach · MEDIUM-HIGH on content, MEDIUM on currency |
| Earlier roles | **Director, Program Operations** and **Director of Metrics, Analytics, Performance and Strategy** at **Marqeta** | ZoomInfo, Adapt.io · MEDIUM |
| Other companies in his history | **Uber**, **Amazon** | RocketReach · MEDIUM (exact sequence not stated, do not assert an order) |
| Self-description | **"Payments and tech nerd"** | His own X/Twitter bio, @phpasion · HIGH |
| Location | **Bay Area** (Piedmont / Oakland, California) | X bio, RocketReach · HIGH |
| Education | **Oberlin College, BA Economics and East Asian Studies, 1987 to 1993** | RocketReach · MEDIUM |
| Listed skills | E-commerce, Payments, Credit Cards, Payment Industry, Payment Card Processing | RocketReach · MEDIUM |
| Public footprint | **Essentially none.** Zero posts on X in 17 years, two empty GitHub accounts, an expired personal domain, no talks, no patents, no podcasts, no published writing. | Verified across all channels · HIGH |

**How to read this person.** Roughly 30 years into a career spent entirely inside payments infrastructure. Amazon and Uber give him scale, Marqeta gives him issuing and card economics, Recurly gives him recurring billing, dunning and retries. He will know what an orchestrator is, will have opinions about the category, and may have run a build-versus-buy on exactly this at a prior company. Treat this as a peer technical conversation. The fastest way to lose him is to spend five minutes defining orchestration or reciting a generic deck. The fastest way to earn the second meeting is to ask a sharp question about how routing decisions are made today and then actually engage with the answer.

⚠️ **What is NOT verified, and matters:** his Eventbrite title, department, and start date. No public source ties a Paul Pasion to Eventbrite at all, and every database still lists him at Recurly. Database lag is typically 6 to 18 months, which is consistent with a recent move, and the fact that a payments person of this seniority now has an eventbrite.com address is itself a strong signal, but **the hypothesis that he was hired specifically to own payments is an inference, not a fact.** Test it with discovery question 1; never assert it.

**Note on his email address:** do not read seniority into `paul@eventbrite.com`. First-name-only is Eventbrite's standard format across roughly 40% of addresses. What it does confirm is that he is a current employee who kept his address through the April 2026 reduction.

**Do not confuse him with:** an attorney at a Department of Energy, a document controller at Samsung E&A, a maintenance supervisor in Hawaii, Bryan Paul Pasion of Long Beach, or Paul Pasion-Gonzalez the psychologist. All verified as different people.

### Relationship timeline

**This is a first meeting.** Verified, not assumed:

- **Calendar:** no prior event with paul@eventbrite.com, with anyone at eventbrite.com, or referencing Bending Spoons, exists anywhere in the calendar.
- **Gong:** not configured in this environment, so no call history.
- **Repo and memory:** no prior Eventbrite research file. The relevant parent-account file is `data/research/bending-spoons-2026-06-17.md`.
- **2026-07-29** German creates the "Eventbrite + Yuno" event. **By 2026-08-03** Paul has accepted and stayed on.
- ⚠️ **Gmail was unavailable to this session**, so if a thread exists it is not reflected here. Read it yourself before the call.

**Implication:** nothing has been pitched yet, which means the first ten minutes are yours to spend on discovery rather than on correcting a prior impression. Given who he is, spend them there.

### Other contacts in the account

| Name | Role | Relevance |
|---|---|---|
| Andrea Parodi | General Manager, Eventbrite (Bending Spoons) | Runs the business since March 2026. Stated priorities include ticketing and checkout. The economic buyer. |
| Francesco Patarnello | President and Secretary, Eventbrite; Bending Spoons co-founder | Officer of record post-close. |
| Mattie Maharaj | Treasurer, Eventbrite (Bending Spoons) | Treasury title over a business holding $278.2M payable to creators. |
| Davide Scarpazza | Co-CFO, Bending Spoons | On the 2026-07-28 term-loan release: capital deployed "primarily through acquisitions." Finance door in Milan. |
| Luca Ferrari | Co-founder and CEO, Bending Spoons | Named secondary ticketing among his Eventbrite ambitions at deal announcement. ⚠️ Of his four stated ideas, only searchability made the actual post-close roadmap. |

---

# 3. The Company

Eventbrite is a self-service ticketing and event-discovery marketplace. Creators publish events, Eventbrite sells the tickets and earns a service fee per paid ticket plus a payment processing fee, with a growing advertising line. Free events are free to publish. Legal entity: **Eventbrite, Inc.**, a Delaware corporation, HQ in San Francisco, now wholly owned through Bending Spoons US Inc. by **Bending Spoons S.p.A.** (Nasdaq: BSP).

### Corporate structure and payment entities ✅

Sixteen subsidiaries on the FY2025 Exhibit 21.1. What matters here is which entity processes.

| Region | Entity used for Eventbrite Payment Processing | Location |
|---|---|---|
| Europe | Eventbrite Operations (IE) Limited | Citywest Business Campus, Dublin 24 |
| Australia | Eventbrite AU Pty Limited | Southbank, VIC |
| Canada | Eventbrite Canada Inc. | Vancouver, BC |
| Singapore | Eventbrite Singapore Pte. Ltd. | Marina Bay Financial Centre |
| Hong Kong | Eventbrite Hong Kong Limited | Hopewell Centre, Wan Chai |
| Mexico | **Eventbrite Mexico Payment Processing S. de R.L. de C.V.** | Polanco, CDMX |
| Argentina (general contracting) | Eventbrite Argentina S.A. | Mendoza |
| Brazil (general contracting) | Eventbrite Brasil Gestao Online De Eventos Ltda. | São Paulo |
| Everywhere else | Eventbrite, Inc. | Delaware / San Francisco |

**Framing rule:** Mexico has a subsidiary literally named "Payment Processing." The entity work in LatAm and APAC is already done, which makes local acceptance a configuration conversation rather than a market-entry one. Eventbrite UK Limited, Eventbrite ES SL and Eventbrite DE GmbH exist but are **not** contracting or payments entities; Europe runs through Dublin. Do not name them in outreach.

### Ownership and strategy

**Bending Spoons S.p.A.** is a leveraged roll-up of consumer software: Eventbrite, Vimeo, AOL, Evernote, **Meetup**, WeTransfer, Brightcove, komoot, Remini, Splice, StreamYard. Their stated playbook, verbatim from a 2026-07-28 filing: *"The transformation is typically deep and entails reorganizing teams, overhauling technology, redesigning user interfaces, accelerating product development, and enhancing marketing and monetization."*

**For later, not for this call:** Bending Spoons also owns Meetup. One owner now holds both event platforms, with no integration announced.

---

# 4. Financials

### 4.1 Ten-year growth trajectory ✅ (all figures from SEC filings)

$ thousands except tickets (thousands). Public company through 2026-03-10, Bending Spoons subsidiary after.

| FY | Net revenue | Gross ticket sales | Paid tickets | Net income/(loss) | Adj. EBITDA | Employees |
|---|---|---|---|---|---|---|
| 2016 | 133,499 | not disclosed | 44,572 | (40,392) | (17,591) | not disclosed |
| 2017 | 201,597 | not disclosed | 71,046 | (38,547) | 4,206 | not disclosed |
| 2018 | 291,611 | not disclosed | 97,295 | (64,078) | 28,765 | 1,094 |
| **2019** | **326,801 ← peak** | **~4,600,000 ← peak** | **109,428 ← peak** | (68,760) | (5,641) | 1,140 |
| 2020 | 106,006 | not disclosed | 47,092 | **(224,718)** | (134,075) | 611 |
| 2021 | 187,134 | 2,437,000 | 67,427 | (139,080) | 1,005 | 707 |
| 2022 | 260,927 | 3,274,358 | 87,056 | (55,384) | 22,323 | 881 |
| 2023 | 326,134 | 3,560,304 | 93,443 | (26,479) | 28,655 | 866 |
| 2024 | 325,068 | 3,283,561 | 83,834 | (15,571) | 35,111 | 748 |
| 2025 | 291,843 | "over $3.0B" | 78,862 | (10,515) | 25,336 | 636 |

*GTV was never an audited annual metric. FY2016, FY2017, FY2018 and FY2020 have no GTV figure in any filing and have not been interpolated.*

**Shape of the curve, in one line:** grew fast into the 2018 IPO, was nearly destroyed by COVID, clawed revenue back to almost exactly the 2019 peak by 2023 but on far less volume, then declined for two straight years into the sale.

| Segment | Period | Revenue CAGR |
|---|---|---|
| Hypergrowth through IPO | FY2016 to FY2019 | **+34.8%** |
| COVID collapse | FY2019 to FY2020 | **−67.6%** in one year |
| Recovery | FY2020 to FY2023 | **+45.4%** |
| Decline into the sale | FY2023 to FY2025 | **−5.4%** |
| Full ten years | FY2016 to FY2025 | **+9.1%** |

**The structural fact that matters most for a payments conversation.** The recovery was priced, not earned on volume:

| | FY2019 | FY2024 | Change |
|---|---|---|---|
| Gross ticket sales | ~$4,600M | $3,283.6M | **−28.6%** |
| Paid tickets | 109.4M | 83.8M | **−23.4%** |
| Net revenue | $326.8M | $325.1M | **−0.5%** |
| Take rate | 7.10% | 9.90% | **+280 bps** |
| Revenue per paid ticket | $2.99 | $3.88 | **+29.8%** |

Eventbrite restored its revenue line while the marketplace shrank by roughly a quarter, closing the gap almost entirely with pricing. That lever is now spent (see 4.4), which is why FY2025 revenue fell 10% on tickets down only 6%.

### 4.2 Recent-months trend ✅

| Metric | Q1 2025 | Q2 2025 | Q3 2025 | Q4 2025 |
|---|---|---|---|---|
| Reported | 2025-05-08 | 2025-08-07 | **2025-11-06** | **never reported** |
| Net revenue | $73.8M | $72.8M | $71.7M | — |
| Revenue YoY | (14)% | (14)% | **(8)%** | — |
| Paid tickets | 19.6M | 19.7M | 19.1M | — |
| Adj. EBITDA | $4.6M | $6.4M | **$8.4M** | — |
| Net income/(loss) | $(6.6)M | $(2.1)M | **+$6.4M** | — |
| Take rate | 9.53% | 9.64% | 9.59% | — |

**The trend was improving into the sale:** the revenue decline moderated from −14% to −8%, and Q3 posted the only positive net income of the year. Q3 2025 was the final earnings release and the final call; every 8-K after it is merger-related. Guidance given on that call (Q4 revenue $71.5M to $74.5M, FY2025 $290M to $293M) simply lapsed when the deal closed.

**Post-acquisition, the only operating figure disclosed:** Eventbrite contributed **revenue of $18.7M and a loss before tax of $31.5M** for the stub period 2026-03-10 to 2026-03-31 (Bending Spoons 424B4). **Bending Spoons has not reported Q2 2026 as of 2026-08-03**, and no earnings date is announced. Its only post-IPO filing is a 2026-07-28 6-K announcing a €500M term loan within €1.49B of facilities maturing March 2031. Note for the account: BSP is a foreign private issuer filing annually on Form 20-F, so ongoing financial visibility into Eventbrite will be materially lower than under quarterly 10-Q reporting.

**Restructuring history:**

| Date | Action | Cost |
|---|---|---|
| April 2020 | COVID reduction, ~45% of employees (1,140 to 611) | ≥$100M annual cost out |
| February 2023 | Restructuring, consolidate into regional hubs | $16.5M ($12.1M severance) |
| 2024-08-07 | Reduction in force, ~11% / ~100 employees | $5.3M |
| FY2025 | No new program, headcount still fell 748 to 636 | — |
| ~April 2026 | Post-acquisition layoffs under Bending Spoons | ⚠️ Not disclosed; press-reported only |

### 4.3 Last full year: FY2025 ✅ (10-K filed 2026-03-12)

| Line | FY2025 | FY2024 |
|---|---|---|
| **Net revenue** | **$291,843K (−10%)** | $325,068K |
| Cost of net revenue | $94,544K | $98,505K |
| Gross profit / margin | $197,299K / **67.6%** | $226,563K / 69.7% |
| Operating loss | $(26,094)K | $(30,793)K |
| **Net loss** | **$(10,515)K** | $(15,571)K |
| **Adjusted EBITDA** | **$25,336K** | $35,111K |
| Operating cash flow | $17,725K | $35,573K |
| Free cash flow (computed) | ~$13,766K | ~$27,298K |
| Paid tickets | 78,862K (−6%) | 83,834K |
| Employees | 636 (319 US / 317 non-US) | 748 |

**Revenue bridge:** −$20.8M ticketing on lower volume, −$16.8M organizer fees from the September 2024 removal, +$4.4M advertising.

**Geography, the number to bring:** United States $209.1M (71.6%), United Kingdom $30.6M (10.5%), all other international $52.1M (17.9%). **41% of paid tickets are non-US but only 28.4% of revenue is.** International tickets monetize materially lower.

### 4.4 Other material items ✅

**Take rate by year** (computed, revenue ÷ GTV): FY2019 **7.10%** · FY2021 7.68% · FY2022 7.97% · FY2023 9.16% · FY2024 **9.90%** · 9M 2025 **9.58%**. Quarterly, the true peak was **Q1 2024 at 10.10%**, falling steadily to 9.53% to 9.64% through 2025. Two levers drove the expansion: **January 2023 ticketing fee increases** (which stuck) and the **June 2023 organizer fee** (which did not). FY2025's ~9.6% is still far above FY2022's 7.97%, so only the organizer-fee layer reversed.

**Revenue per paid ticket** (disclosed every year through FY2024): $3.00 (2016) · $2.84 (2017) · $3.00 (2018) · $2.99 (2019) · $2.25 (2020) · $2.78 (2021) · $3.00 (2022) · $3.49 (2023) · $3.88 (2024) · **$3.70 (2025, computed; FY2025 is the first year they stopped disclosing it)**.

**International mix of paid tickets, rising steadily:** 36.0% (2017) · 34.1% (2018) · 36.1% (2019) · 35% (2021) · 39% (2022) · 40% (2023) · 40% (2024) · **41% (2025)**. Their own filings say processing costs run structurally lower outside the US, so this mix shift has been working in their favour on cost while working against them on revenue per ticket.

**The pricing experiment that had to be unwound.** Organizer fees introduced June 2023, reversed September 2024. The 10-K attributes a **$16.8M revenue decline in 2025** to the removal, and warns they "may be unable to win back the business of departed creators." A clean case of a take-rate lever that worked on paper and cost them supply.

**Payments on the balance sheet (2025-12-31):** accounts payable to creators **$278.2M** · cash held on behalf of creators $253.6M · funds receivable from processors $27.1M (settling in roughly five business days) · restricted cash $107.6M, which includes a **$48.0M letter of credit established in 2024 specifically to mitigate refunds and chargebacks** · accumulated deficit $841.5M.

**Chargeback and refund provision, the full series:** FY2020 **$61.0M** · FY2021 $6.5M · FY2022 $8.1M · FY2023 $12.4M · FY2024 **$27.5M** · FY2025 **$16.1M**. The FY2025 improvement is attributed to "fraud remediation initiatives." They actively manage this number and can talk about it in detail. The structural exposure is the **advance payout program**, flagged as a **critical audit matter** in the FY2025 10-K: if an event is cancelled or fraudulent after a creator has been paid early, unrecoverable losses "could equal the value of the transaction or transactions settled to the creator prior to the event."

**Debt, all cleared at close:** the $60M August 2025 term loan was paid off and the credit agreement terminated on the closing date; the merger triggered a Fundamental Change on the remaining $87.75M of 2026 convertible notes, and Eventbrite deposited cash with the trustee to repurchase all of them.

**Merger economics:** $4.50 cash per share, roughly **$505M** total consideration, an **81% premium** to the $2.49 unaffected close on 2025-11-28 but only **9% over the 52-week high** of $4.12. Against a $1.76B valuation at the 2018 IPO ($23.00 per share). Management's long-range plan, disclosed in the proxy: revenue $308M (2026E) rising to $452M (2030E) while Adjusted EBITDA nearly triples from $31M to $90M.

**Payment processing cost, the honest boundary:** the filings say processing fees are the largest component of cost of net revenue ($94.5M in FY2025), but **the dollar amount is never disclosed in any year**. Do not quote one. ⚠️

### 4.5 So what, for this call

The whole financial story points at one lever. Pricing is exhausted, having been pushed to 9.90% and then partly reversed at a $16.8M cost. Volume is 28% below the 2019 peak. Headcount is down from 1,140 to 636 before the 2026 cuts. What is left is a plan that needs EBITDA to roughly triple by 2030 on modest revenue growth, and the largest variable cost in that plan is, in their own words, processing fees. **Cost per transaction and authorization rate are among the few levers still fully in their control.** That is the frame, and with a payments engineer in the room you can say it plainly.

---

# 5. Payments Money Map

### Architecture ✅

**Two models.** Under **Eventbrite Payment Processing (EPP)** the 10-K states Eventbrite "is the merchant of record," is the principal and records revenue gross. Under **Facilitated Payment Processing (FPP)** the creator receives proceeds directly through a third-party service "such as PayPal," booked net. FPP is restricted to cases where "you select a currency and payout country that isn't supported by Eventbrite Payment Processing," and it costs the organizer reserved seating, in-app card payments, fee absorption and order modification. EPP is the business.

| Vendor | Role | Evidence |
|---|---|---|
| **Stripe** | Verification, processing and payouts in AU, CA, UK, US via Stripe Connect | ✅ Help centre: "uses Stripe to verify and process payments in Australia, Canada, the United Kingdom, and the United States"; Merchant Agreement requires the Stripe Connected Account Agreement |
| **Braintree** (a division of PayPal) | Card acquiring and gateway | ✅ Named sub-processor; live flag `enableNonceBraintreePayments` true in US, UK, IE, DE, NL, ES, CA, AU |
| **MercadoLibre / Mercado Pago** | LatAm acquiring | ✅ Named sub-processor; live flag true in MX and AR only |
| **Adyen B.V.** | Named payment sub-processor | ✅ Listed, ⚠️ specific role not disclosed |
| **Cybersource** (Visa) | Named payment sub-processor | ✅ Listed, ⚠️ specific role not disclosed |
| Authorize.Net, Moneris | Legacy platform integrations, currently off | ✅ `accept_authnet` and `accept_moneris` flags present and false |
| LexisNexis Risk Solutions | Risk and analytics | ✅ Named sub-processor |
| reCAPTCHA v3 | Bot defence at checkout | ✅ `disableRecaptcha3: false` |
| Concentrix, Teleperformance | Outsourced payment operations | ✅ 10-K: BPOs in the Philippines and El Salvador support "creator payouts, chargeback management, and fraud identification" |

**Counting rule:** five payment vendors. **PayPal is a wallet and the FPP fallback rail, never a processor.** Braintree is the acquiring relationship. Getting this wrong in front of Paul specifically would be expensive.

**Boundary on sourcing:** the vendor list above comes from Eventbrite's own sub-processor page and live checkout inspection. Their 10-Ks refer only generically to "third-party payment processors." Cite it as "your sub-processor page lists," not "your filings say."

### Processor history, and why it matters ✅ (this is filing-verified)

Their processor estate has already turned over twice, and both moves are documented in their own SEC correspondence and filings. Paul will know this history; you should too.

| Period | Processor | Evidence |
|---|---|---|
| Named 2018 | **Braintree**, third-party processor for EPP where Eventbrite is merchant of record | Eventbrite's own response to an SEC comment letter (DRSLTR, 2018-07-23), verbatim: *"payment processing fee costs represent the Company's portion of payment processing fees paid to third-party payment processors, **such as Braintree**, for transactions processed using EPP and **for which the Company is the merchant of record**."* This is the only time a processor is named in any Eventbrite SEC document. |
| Sept 2017 to **Jan 2020** | **Square**, announced as *"our primary online payment processing partner for EPP in the United States, Canada, Australia, the United Kingdom"* and exclusive partner for all point-of-sale, on a five-year initial term | Contract **terminated January 2020**, roughly two years into five. The FY2019 10-K says why it mattered: *"**Our costs for payment processing may increase with a new partner** due to higher direct costs of development and implementation and fee structure."* |
| From 2023 | **Stripe**, onboarding and creator payouts in certain geographies, later Stripe point-of-sale | FY2022 10-K: *"In 2023, we plan to begin onboarding and facilitating payouts for creators through Stripe, Inc. in certain geographies as part of our EPP offering."* Q4 2024 call describes *"rolling out stripe point-of-sale at scale."* |

**Two things this gives you.** First, they have lived through the cost and engineering pain of a processor migration, and wrote in a filing that switching partners can raise their costs. That is precisely the pain an orchestration layer removes, and you can reference it without them having said it to you. Second, **EPP concentration was disclosed as *"over 90% of revenue on our platform is associated with payments processed through EPP"* in every 10-K from FY2018 through FY2022, then quietly dropped from FY2023 onward and never restated.** Do not speculate about why. It is worth a discovery question.

**Payment processing cost, the only quantified trail that exists:** absolute cost is never disclosed, but year-over-year deltas were, from FY2017 through FY2022: **+$17.0M (2017), +$20.7M (2018), +$10.3M (2019), −$55.1M (2020), +$15.6M (2021), +$20.7M (2022)**. From FY2023 onward the direction is disclosed but not the amount. These are deltas with no anchoring base, so they cannot be chained into a level. ⚠️ Do not present them as a cost series.

**Interchange entered their risk factors in the FY2023 10-K** (zero mentions FY2018 through FY2022) and has stayed: *"For certain payment methods, we pay interchange and other related acceptance fees, along with additional transaction processing fees. Payment card networks and our third-party payment services providers could increase the fees or interchange they charge us... **which would increase our operating costs and reduce our margins**."* And: *"**If we are unable to negotiate favorable economic terms with these partners**, our business, financial condition and results of operations could be harmed."* They put scheme and processor pricing power in writing as a named risk two years before the sale.

**Orchestration status:** no third-party orchestrator appears in the sub-processor list or the checkout bundle. What exists is self-built failover, described in the 10-K as *"multiple integrations in place at one time allowing for back up processing alternatives."* ✅

### Methods by market ✅ (21 payout countries)

| Payout country | Currency | Attendee payment methods |
|---|---|---|
| United States | USD | Card, PayPal, PayPal Pay in 4, Klarna, Afterpay |
| United Kingdom | GBP | Card, PayPal, PayPal Pay in 3, Klarna, Afterpay |
| Canada | CAD + USD | Card, PayPal, Klarna, Afterpay, Affirm |
| Australia | AUD | Card, PayPal, PayPal Pay in 4, Afterpay |
| New Zealand | NZD | Card, Afterpay |
| Austria, Germany | EUR | Card, SOFORT, PayPal, Klarna |
| Belgium, Netherlands | EUR | Card, Bancontact, iDEAL, PayPal, Klarna |
| Finland, France, Greece, Ireland, Italy, Portugal, Spain | EUR | Card, PayPal, Klarna |
| Brazil | BRL | Card, Hipercard, Elo |
| **Mexico** | MXN | **Card only** |
| **Argentina** | ARS | **Card only** |
| **Singapore** | SGD | **Card only** |
| **Hong Kong SAR** | HKD | **Card only** |

**The detail he will appreciate:** the live checkout payload already carries dormant flags for `should_accept_oxxo`, `should_accept_rapipago`, `should_accept_pagofacil`, `should_accept_boleto_bancario` and `maxInstallments`, all inactive across the twelve locales sampled on 2026-08-03. The plumbing exists and is switched off. Frame it as an observation about prioritization, never as an accusation.

⚠️ Apple Pay and Google Pay appear in Eventbrite documentation only for in-person Tap to Pay in AU, CA, UK and US, and no keys for either were found in the online checkout payload. High confidence, not absolute. Ask, do not assert.

### 3D Secure and fraud ✅ (live probe, 2026-08-03)

| 3DS2 enabled | 3DS2 not enabled |
|---|---|
| GB, DE, NL, ES, IE | US, CA, AU, MX, AR, SG, HK |

Maps cleanly to the PSD2 and UK SCA perimeter and nowhere else, which is a normal posture. The commercial read is that outside Europe there is no exemption engine or risk-based authentication to trade auth against fraud. Chargeback liability contractually sits with the organizer (Merchant Agreement §5.4), and Eventbrite reimburses its processors for card network fines.

### Payout mechanics ✅

Payouts land roughly five business days after the event, with a reserve against net sales and a US-only Instant Payout at 3% (min $2.99, max $40). Merchant Agreement §9.2 gives reserve and offset rights, §10.1 allows capping and withholding advance payouts. And: *"Event Proceeds collected in a currency may only be paid out to you in the currency in which they are collected. We do not provide currency conversion services."* On the Q4 2024 call they described *"rolling out stripe point-of-sale at scale"* and, on Timed Entry, *"the ability to consolidate the payout for the creator... one account level payout."* Payouts are an active product surface, not an afterthought.

### Fee card ✅

| Market | Service fee | Payment processing fee |
|---|---|---|
| United States | 3.7% + $1.79 per ticket | 2.9% per order |
| Canada | 3.5% + C$1.29 | 2.9% per order |
| New Zealand | 4.2% + NZ$0.55 | 2.4% per order |
| Australia | 5.35% + A$1.19 | Bundled |
| United Kingdom | 6.95% + £0.59 | Bundled |
| Ireland | 5.9% + €0.79 | Bundled |

Eventbrite's fee page splits countries into current "Standard" packages (US, UK, Canada, Australia, Ireland, New Zealand) and **"Legacy Package Countries"** including Spain, Netherlands, Germany, Mexico, Brazil, Argentina, Hong Kong and Singapore. That word is theirs. Orchestration is how a smaller team keeps monetizing a long tail it no longer staffs.

**Structural detail worth noticing:** the UK, Australia and Ireland are sold as a **single blended ticketing fee with no separately disclosed processing line**, while the US, Canada and New Zealand unbundle service fee and processing fee. Where processing is bundled, the merchant absorbs the variance; where it is unbundled, the buyer sees it. Both models are affected differently by a cost change, which is a good question to ask rather than assume.

**The buyer-facing processing fee has moved, and moved up ✅** (Eventbrite's own help pages and archived captures):

| Period | US processing fee charged | Source |
|---|---|---|
| Through 2018-09-03 | **3.0%** of ticket cost | Help article, 2017 capture |
| From 2018-09-04, 1pm EDT | **2.5%** of total transaction | Fee-change article, verbatim: "a reduction in the Eventbrite Service flat fee (from $0.99 to $0.79) and the EPP fee (from 3% to 2.5%)" |
| By 2023-01-20 to today | **2.9%** per order | Pricing page and help article 755615 |

The same 2018 change **removed the US$19.95 per-ticket fee cap**, and no cap has been disclosed since. So over eight years the processing fee they charge buyers fell then rose 40bps, while the service fee rose materially (Professional was 2.5% + $1.99 in 2018 against 3.7% + $1.79 today). ⚠️ You cannot infer their acquiring cost from any of this; the buyer-facing fee is a price, not a cost. Use it only to show you have read the history.

**Organizer-selectable processors have narrowed.** Until roughly 2021 organizers could choose **Eventbrite Payment Processing, PayPal, or Authorize.Net** (US and Canada, and only on a paid package). Authorize.Net was present in a March 2021 capture and gone by September 2022. Today the help centre offers only EPP, with PayPal framed purely as the fallback "if you don't see your currency." The consolidation onto EPP is complete, which is consistent with the dormant `accept_authnet` flag still sitting in the checkout payload.

### Hiring signal ✅

`eventbrite.com/careers/jobs` now redirects to `jobs.bendingspoons.com` (verified 2026-08-03). Across the full Bending Spoons job board: payment 1, fraud 0, billing 0, treasury 0, fintech 0. No payments organization is being staffed up. **Do not say this out loud.** Use it to calibrate: if Paul owns payments, he likely owns it thinly.

### Peer context ✅

| Company | Processors | Orchestration |
|---|---|---|
| Ticketmaster (Live Nation) | Braintree (primary), Adyen, Nuvei, Paybilt | **Built their own, "TMPay"**, with a live provider enum. FY2025: $37.1B fee-bearing GTV, 346M tickets. Payouts migrated to Hyperwallet Aug 2025. |
| Resident Advisor | Braintree plus multi-acquiring | **Bought: BR-DGE**, three-year deal Feb 2025 for multi-acquiring, dynamic routing and method connectivity |
| Fever (owns DICE since Jun 2025) | Checkout.com, Nuvei, PayU, Mercado Pago (AR), PayPal | **Bought: ProcessOut** in production, plus Forter and Queue-it. Note ProcessOut is owned by Checkout.com, one of Fever's own acquirers. |
| DICE | Stripe only (Stripe Connect) | None found. India card-only, no UPI. |
| Luma, Posh, Partiful, Humanitix | Stripe Connect | None. The organizer, not the platform, is the merchant. |
| StubHub | Afterpay, Klarna, Zip, Affirm in the US | None found (Yuno research, 2026-07-09) |

**Use this as the build-versus-buy evidence base**, since that is his likely objection. Ticketmaster built. Resident Advisor and Fever bought. Both are live, defensible choices by serious teams, and the peer set splits roughly down the middle.

---

# 6. Top Markets

⚠️ **Honest limitation.** Only a few canonical market statistics were verified; the rest were dropped rather than estimated. The Worldpay Global Payments Report 2026 is download-gated and would close the gaps for UK, Canada, Australia, Netherlands, Germany, Mexico, New Zealand and Singapore. Do not quote numbers for those markets.

| Market | Verified statistic | For the call |
|---|---|---|
| **Brazil** | Pix has roughly 200M monthly active users, about 80% of the population (Central Bank of Brazil, Q1 2026), moving roughly R$3.4 trillion a month. Pix processed **8.6 times** more transaction value than credit and debit cards combined (2024). | Eventbrite has a Brazilian entity and sells in BRL on cards plus Elo and Hipercard. Ask what share of Brazilian checkouts complete today. |
| **Spain** | Bizum reached 27.6M active users (2024) and joined EuropPA on 2025-03-31, interoperable with Bancomat Pay (Italy) and MB Way (Portugal). | A Legacy Package country with a method now interoperable across three of their EUR markets. |
| **India** | UPI runs roughly 84% of digital payments (2025). ⚠️ Secondary aggregation, directional only. | Not a payout country for Eventbrite, but it is where the engineering team sits. Context only, not an opportunity claim. |

**More useful than any statistic:** Mexico, Argentina, Singapore and Hong Kong transact on cards, Brazil on cards plus two domestic schemes, and installments are inactive across every locale sampled. In Mexico, Brazil and Argentina, installments are ordinary consumer expectation.

---

# 7. News & Signals

### Fresh, last 21 days

| Date | Item |
|---|---|
| 2026-08-03 | Bending Spoons Q2 2026 results not yet published and no date announced. First post-IPO print is pending. |
| 2026-07-28 | BSP 6-K: €500M term loan within €1.49B of facilities maturing March 2031. Co-CFO Davide Scarpazza: capital deployed "primarily through acquisitions." |
| **2026-07-24** | Product: refund for order-level transfers. **Rapport option.** |
| 2026-07-23 | Product: bot-view filtering in traffic and conversion reporting. |
| 2026-07-17 | Product: cross-event sales tracking by day, week and month. |
| 2026-07-15 | Product: add-on revenue broken out on the dashboard. |
| **2026-07-13** | Product: real-time sold-out status and real-time waiting room. **Rapport option.** |

### Earlier, newest first

| Date | Item |
|---|---|
| 2026-07-01 | Bending Spoons IPOs on Nasdaq (BSP) at $29.00, raising roughly $1.68B, closing day one at $40.50. |
| 2026-06-08 | BSP files its F-1. Q1 2026 revenue $601.3M (up 132%). Prospectus quantifies group payment mix and names processor dependence as a risk factor. |
| 2026-05-03 | Julia Hartz confirms in her first post-sale interview that she stepped away as CEO. |
| **2026-04-13** | Layoffs announced by GM Andrea Parodi, weighted toward India, headcount never disclosed. Stated forward priorities: reliability, creator tools, event reach and discovery, ticketing experience, and **checkout**. ⚠️ Do not raise. |
| 2026-03-23 | NYSE removes EB from listing and registration. |
| 2026-03-12 | Final FY2025 10-K filed. Hartz and Gandhi step down immediately after. |
| **2026-03-10** | Merger consummated. Entire board resigns. Patarnello, Maharaj and Mulligan appointed. |
| 2026-02-27 | Stockholders approve the merger, 212.4M for against 1.17M. |
| 2026-01-12 | ⚠️ *Juniper International LLC et al. v. Eventbrite, Inc.*, Delaware Chancery, over Class B voting power. **Do not raise.** |
| 2025-12-01 / 12-02 | Merger agreement signed and announced. Inbound and relationship-originated at Sun Valley; no activist, no pre-announced strategic review. The market check produced one competing bid, at a lower price. |
| 2025-11-06 | Final earnings call. Q3 2025 revenue $71.7M, first positive net income of the year, Ads up 38% YoY. Hartz names "the addition of more payment options" as the 2026 international lever. |
| 2025-05-16 / 2025-05-02 | CTO Vivek Sagi and GC Julia Taylor resign weeks apart, before the sale process. **The CTO seat was never refilled.** |

⚠️ **Live matters, do not mention any of them:** the April 2026 CFIUS inquiry into the acquisition; the Juniper Delaware lawsuit; and the hundreds of substantially similar letters Eventbrite received in December 2025 alleging violations of the California Invasion of Privacy Act.

---

# 8. Selling Yuno Here

### Core frame

Yuno is the unified operating system for global financial infrastructure, orchestrating across payment methods, processors, antifraud, KYC and KYB, reconciliation and stablecoins through one integration.

**For this room specifically:** you are not there to teach him what orchestration is. You are there to find out how routing decisions get made at Eventbrite today, and to establish that the maintenance burden of five integrations is a cost he does not have to carry. Keep returning to **cost per transaction, authorization rate, and time to launch a method**. Never gaps, never what is missing.

### Hooks with proof points

| Hook | Evidence you cite | Yuno proof point |
|---|---|---|
| **Processing cost is the last big controllable line** | Their 10-K: processing fees are the largest component of cost of net revenue; non-US processing runs lower on local rails. Take rate already pushed to 9.90% and partly reversed. Plan needs EBITDA to triple by 2030. | **Rappi**: multi-PSP routing at scale in LatAm on cost and authorization, not availability. |
| **International monetization gap** | 41% of paid tickets non-US against 28.4% of revenue. Payment entities already exist in Mexico, Singapore, Hong Kong, Canada, Australia and Ireland, plus Brazil and Argentina. | **InDrive**: emerging-market local method coverage at scale through one integration. |
| **Maintenance, not capability** | Five vendors, self-built failover, no CTO since May 2025, headcount 1,140 to 636 before the 2026 cuts, zero payments roles open on the parent job board. | **Reserva**: multiple brands under one orchestration layer. |
| **Decline recovery and retries** | Chargeback and refund provision $27.5M to $16.1M year over year, so they measure this. 3DS2 only in the European perimeter. | **Livelo**: recurring and high-volume flows with smart retries and network tokenization. His Recurly background makes this the easiest technical conversation of the call. |
| **Portfolio consolidation (Milan)** | BSP prospectus: 75% of Q1 2026 revenue via electronic payments, 67% of that through Adyen, PayPal and Stripe, 33% through app stores at 15% to 30% against "5% or less" for processors. | **Rappi** and **Reserva**: absorb each brand's rail as configuration. |

### Landmines, what NOT to say

- **Do not explain orchestration from first principles.** He has spent 30 years in payments. Condescension is the fastest way to lose this specific person.
- **Do not call them NYSE: EB, do not cite earnings calls as current, do not name Julia Hartz as CEO.**
- **Do not raise the April 2026 layoffs, the India cuts, or headcount.** If he raises it, acknowledge briefly and move on.
- **Do not mention CFIUS, the Juniper lawsuit, or the CIPA letters.**
- **Never say they "lack" an orchestrator or that anything is missing, broken or behind.** They made a deliberate multi-provider architecture choice. Respect it, then separate failover from routing.
- **Do not quote a dollar figure for their processing cost.** Never disclosed in any year. Cost of net revenue ($94.5M) is public; the processing share is not.
- **Do not call PayPal a processor.** Braintree is the acquiring relationship.
- **Do not say their filings name their processors.** They never do. The vendor list comes from their sub-processor page.
- **Do not assert Adyen's or Cybersource's specific role.** Listed but undisclosed. Ask, it is a good question.
- **Do not assert his title or that he was hired to fix payments.** Both are inferences.
- **Do not pitch replacement.** Say early that Stripe, Braintree, Adyen, Cybersource and Mercado Pago all stay.
- **Do not assert any connector capability the 11:30 matrix did not confirm.** In a bake-off run by a payments engineer, one overclaimed capability discovered later kills the deal. "I will confirm in the working session" is a strength, not a weakness.
- **Do not disparage the other orchestrators** he is talking to, and do not guess out loud who they are. Reframe the comparison onto payout, reconciliation and the full-stack scope instead.
- **Do not read the Cybersource and Mercado Pago omission back to him as a conclusion.** It is an inference about evaluation scope. If relevant, ask about geographic scope instead: "does the evaluation cover the LatAm rails too, or is this phase US and Europe?"

---

# 9. Be Ready For

| What he may ask | Ready answer |
|---|---|
| **"Do your connectors support Connect / Adyen for Platforms / Braintree marketplace / JPM's equivalent, or just standard acquiring?"** (the central question of the evaluation) | Only what the 11:30 matrix confirmed. Everything else: "I will confirm with the technical detail in the working session." Then widen to payout, reconciliation, fraud and KYC in one layer. |
| "If you route my pay-in to one processor and my payout runs elsewhere, how does the ledger reconcile without breaking my MoR model?" | If confirmed in the matrix, answer concretely. If not, working session. Never improvise fund-flow answers to a person who has built payout ledgers. |
| "Why not build it?" (less likely now that they opened a formal evaluation, but possible from him) | Concede he could, reframe on maintenance and opportunity cost, use the peer split: Ticketmaster built, Resident Advisor and Fever bought. |
| "How do you price?" | Per-transaction on volume, decoupled from processor economics so the incentive is to lower your cost per transaction. Shape now, number after seeing volume by market and method. Do not invent a rate. |
| "What does integration actually cost my team?" | One integration to Yuno, then each processor and method is configuration. Be honest that the first integration is real work; the return is on the second and every one after. Offer an API and SDK walkthrough. |
| "Do we replace Stripe or Braintree?" | No. Everything stays. Say it before he asks. |
| "How does routing actually decide?" (he will go deep) | Bring Justo or Jarrett in for the technical answer on rules, cascading, retry logic and observability. Do not improvise depth you do not have. |
| "PCI and security?" | PCI DSS Level 1, tokenized card data, reduces rather than expands your scope. ⚠️ Confirm the exact current wording with Justo or Jarrett before the call. |
| "Who holds the money? Does this change our MoR model?" | No. Yuno is an orchestration layer, not a merchant of record and not a processor. Funds settle through your existing acquirers into your existing entities. You remain MoR under EPP. |
| "References in ticketing?" | Lead with Rappi, InDrive, Reserva, Livelo. If pressed on ticketing specifically, be straight and point to what peers do rather than claiming a logo we do not have. |
| "What about payouts, not just pay-ins?" | Strong ground: $278.2M payable to creators, reserves, 3% US-only Instant Payout, no currency conversion, and an existing account-level payout consolidation effort. One layer covers both. |
| "Bending Spoons decides this." | Convert into an introduction request. |
| "What data do you need to show me a number?" | Volume and approval rate by market, method and processor, plus decline reason codes. Offer to work from one market if that is all he can share. |

---

# LIVE ZONE

# 10. Agenda (30 minutes)

Restructured for a bake-off: less open discovery, more demonstration, and process questions at the close.

| Time | Block | Notes |
|---|---|---|
| 0:00 to 0:03 | Intros. Rapport on his Marqeta/Uber/Recurly arc. Then the clarifier from his own email: "when you say marketplace use cases, what weighs most: splits, onboarding, payouts, funds holding?" His answer steers the whole call. | Notes: ____________________ |
| 0:03 to 0:08 | **Targeted discovery.** Questions 2 through 5 below: how routing decides today, where decisions sit post-acquisition, and the JPM question. | Notes: ____________________ |
| 0:08 to 0:20 | **The evidence block, the longest on purpose.** The four connectors from the 11:30 matrix (only confirmed facts), plus the Rappi and InDrive marketplace examples with processors routed and payout flows. This answers "specific examples" head on. Hand technical depth to Justo or Jarrett. | Notes: ____________________ |
| 0:20 to 0:26 | The frame that breaks the feature matrix: pay-in plus pay-out plus fraud, KYC and reconciliation in one layer for a MoR holding $278M payable to creators. | Notes: ____________________ |
| 0:26 to 0:30 | **Process close:** timeline, decision criteria, who else is at the table, whether JPM is negotiated or to-be-enabled, and the working session with the routing owner. | Notes: ____________________ |

# 11. Discovery Questions

Nothing here re-asks what filings or the help centre already answer. Calibrated for a payments engineer running a vendor evaluation.

1. **"When you say marketplace use cases, what weighs most for you: fund splits, organizer onboarding, payouts, or the funds-holding side?"** (His own email, turned back. The answer steers the demo and reveals the pain.)
   *Notes: ____________________________________________*
2. **"J.P. Morgan Payments is not on your sub-processor list today. Is that a relationship you are already negotiating, or something you would want the orchestration layer to enable?"** (The biggest signal in his email. The answer changes the pitch: enablement is Yuno's home turf.)
   *Notes: ____________________________________________*
3. **Your sub-processor page lists five payment vendors and the 10-K describes multiple integrations with back-up alternatives. In practice, what decides which one takes a given transaction today?** (Still the pivotal question, and now it also reveals how far their internal evaluation has gone.)
   *Notes: ____________________________________________*
4. **Since the transition in March, where do processor and routing decisions actually get made? Here, or Milan? And for this evaluation specifically, who besides you is at the table, what are the criteria, and what timeline are you working to?** (Normal bake-off questions; ask them without apology.)
   *Notes: ____________________________________________*
4b. **Coming from Recurly and Marqeta into ticketing, what looked different about this payments problem from the outside, and what has surprised you since?** (Rapport-grade discovery, use if the room allows.)
   *Notes: ____________________________________________*
5. **41% of paid tickets are outside the US but 28% of revenue. When you look at that gap, how much of it is pricing versus acceptance and completion?**
   *Notes: ____________________________________________*
6. **In Brazil, Mexico, Argentina, Singapore and Hong Kong the checkout runs on cards, and I noticed the platform already has flags for local rails and installments that are switched off. What has kept them off, engineering priority or something else?**
   *Notes: ____________________________________________*
7. **The chargeback and refund provision came down from $27.5M to $16.1M last year. Outside Europe where 3DS is in play, what are you using to trade authorization against fraud?**
   *Notes: ____________________________________________*
8. **The last public plan named "more payment options" as the international monetization lever for 2026. Did that survive into the current roadmap, and who owns it?**
   *Notes: ____________________________________________*
8b. **You have already migrated processors more than once, Square out in 2020 and Stripe in from 2023. What did those migrations actually cost the team, and what would make the next one cheaper?** (Their own FY2019 10-K warned that switching partners could raise costs. This question invites him to describe the pain in his own words, which is far stronger than you asserting it.)
   *Notes: ____________________________________________*
9. **On the creator side you hold a large payable balance, run reserves, and offer instant payouts in the US only. Is the payout experience on the same roadmap as checkout, or owned separately?**
   *Notes: ____________________________________________*
10. **If you wanted to turn on a new method in a market tomorrow, what does that path look like today and how long is it really?**
    *Notes: ____________________________________________*
11. **If we built a cost and authorization model on two or three of your non-US markets, what would have to be in it to be worth your time?**
    *Notes: ____________________________________________*

# 12. Post-Meeting Checklist

- Send the recap the same day. Confirm what you heard, restate the next step with a date, attach nothing he did not ask for.
- Log **Paul's confirmed title and remit**, how routing is decided today, and who owns processor strategy.
- Book the working session before end of day, with the routing owner invited.
- Create a `project_eventbrite.md` memory entry (Bending Spoons ownership, Paul Pasion's payments background, five-vendor stack, MoR model, LatAm and APAC card-only) and add the pointer line to `MEMORY.md`.
- Update this file with the outcome, then commit and push.
- Cross-link to the Bending Spoons account: Eventbrite is the strongest single proof point in a portfolio pitch covering Vimeo, WeTransfer, AOL and Meetup.

---

## Appendix: Sources

**Attendee**
- Paul Pasion LinkedIn (private to logged-out viewers): https://www.linkedin.com/in/phpasion/
- X/Twitter @phpasion (self-description and location): https://x.com/phpasion
- RocketReach (Recurly role, career list, Oberlin education): https://rocketreach.co/paul-pasion-email_5238654
- ZoomInfo (Marqeta role): https://www.zoominfo.com/p/Paul-Pasion/3770788514
- Adapt.io (Marqeta role): https://www.adapt.io/contact/paul-pasion/266274476

**Financials and filings**
- FY2025 10-K, filed 2026-03-12: https://www.sec.gov/Archives/edgar/data/1475115/000147511526000005/eb-20251231.htm
- SEC XBRL company facts, CIK 0001475115: https://data.sec.gov/api/xbrl/companyfacts/CIK0001475115.json
- FY2020 10-K (five-year table, FY2016 to FY2020): https://www.sec.gov/Archives/edgar/data/1475115/000147511521000020/eb-20201231.htm
- FY2022 10-K: https://www.sec.gov/Archives/edgar/data/1475115/000147511523000040/eb-20221231.htm
- Q4/FY2024 earnings release: https://www.sec.gov/Archives/edgar/data/1475115/000147511525000025/earningspressrelease-fy2024.htm
- Q3 2025 earnings release (final): https://www.sec.gov/Archives/edgar/data/1475115/000147511525000114/ebq32025earningspressrelea.htm
- Q4 2019 shareholder letter (FY2019 GTV): https://www.sec.gov/Archives/edgar/data/1475115/000147511520000012/q4shareholderlettera03.htm
- Merger completion 8-K, 2026-03-10: https://www.sec.gov/Archives/edgar/data/1475115/000114036126008636/ef20067526_8k.htm
- DEFM14A merger proxy, 2026-01-28: https://www.sec.gov/Archives/edgar/data/1475115/000114036126002685/ny20061430x2_defm14a.htm
- Bending Spoons 424B4 IPO prospectus, 2026-07-01: https://www.sec.gov/Archives/edgar/data/2004711/000110465926079884/tm2613674-14_424b4.htm
- Bending Spoons 6-K (term loan), 2026-07-28: https://www.sec.gov/Archives/edgar/data/2004711/000110465926087587/tm2621445d1_ex99-1.htm

**Payments**
- Eventbrite Sub-Processors: https://www.eventbrite.com/help/en-us/articles/891292/eventbrite-subprocessors/
- Merchant Agreement: https://www.eventbrite.com/help/en-us/articles/346993/eventbrite-merchant-agreement/
- Payment processing options and method matrix: https://www.eventbrite.com/help/en-us/articles/705340/comparing-payment-processing-options/
- Stripe verification: https://www.eventbrite.com/help/en-us/articles/856831/verify-your-financial-information-through-stripe/
- Ticketing fees by country: https://www.eventbrite.com/help/en-us/articles/755615/how-much-does-it-cost-for-organizers-to-use-eventbrite/
- Event payouts: https://www.eventbrite.com/help/en-us/articles/640593/get-started-with-event-payouts/
- Live checkout and 3DS flags probed directly across 12 locales, 2026-08-03.

**Peers and news**
- Parodi post-acquisition post, 2026-04-13: https://www.eventbrite.com/blog/whats-next-at-eventbrite/
- Eventbrite product updates: https://www.eventbrite.com/product-updates/
- BR-DGE and Resident Advisor: https://br-dge.to/press/br-dge-to-power-payments-for-resident-advisors-enhanced-ticketing-platform/
- Ticketmaster and Braintree: https://business.ticketmaster.com/press-release/paypal-named-the-preferred-payments-partner-of-ticketmaster/
- Fever acquires DICE: https://newsroom.feverup.com/en-US/250537-fever-and-dice-join-forces-to-build-a-live-entertainment-tech-powerhouse/
- DICE terms (Stripe): https://support.dice.fm/article/286-standard-ticket-terms
- Pix (Central Bank of Brazil, via): https://en.wikipedia.org/wiki/Pix_(payment_system)
- Bizum: https://en.wikipedia.org/wiki/Bizum
- Internal: data/research/bending-spoons-2026-06-17.md and data/research/stubhub-2026-07-09.md

*Method note: Gmail and Glean were not authorized in this session and Gong is not configured, so no email or call history is reflected. Calendar history was checked directly and returned a verified negative. Paul Pasion's LinkedIn is private to logged-out viewers; his career history comes from third-party databases that lag LinkedIn by 6 to 18 months, and his Eventbrite title is unverified.*
