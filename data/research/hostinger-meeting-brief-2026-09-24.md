# Meeting Brief: Yuno <> Hostinger, Demo (Sep 24, 2026)

**Thursday, September 24, 2026 · 06:00 to 06:45 COT · 14:00 Vilnius · 13:00 Amsterdam and Warsaw · 11:00 UTC · 45 min**
**Meet:** https://meet.google.com/uri-otwr-mua · Event "Hostinger + Yuno | Demo" (organizer: German). Moved from Sep 17 at Paulius's request ("unplanned conflict", Sep 17, 07:58 UTC).
**Hostinger:** Paulius Lapėnas, Head of Payments, Hostinger Global (accepted Sep 17, 10:55 UTC).
**Yuno:** German (lead, discovery, close) · Dirk van der Meulen, Senior Solutions Engineer (demo, accepted) · Antoine Cathelin, Head of Product (accepted Sep 18; he had declined the Sep 17 slot) · Piotr Sierpinski, Sales Manager Europe (relationship, accepted Sep 23) · Tautvydas "TJ" Paukštė, VP Transaction Rails (short hello, no response yet) · Justo Benetti, CRO (India and commercial, no response yet).

**Objective:** Paulius sees four things work live, hears every limit before he asks for it, and leaves with three commitments: an engineering working session with his hPayments team, a written proposal for vault standalone plus India within a week, and a chosen route to close the NDA. Winning is not "he liked the demo". Winning is a date and a name for each of those three.

**What this document is:** the single brief for tomorrow. It merges the technical deep dive brief prepared for Sep 17, the Sep 15 internal sync decisions, what changed since (NDA, attendees, India, product facts), the demo plan, and the live agenda and questions at the end. Deeper material: [Sep 3 meeting brief](https://docs.google.com/document/d/1CqI5ig5Z-K4iE0uPrLol6-aab49BRiIPh89Tu8YYYCU/edit) · [Sep 15 internal sync brief](https://docs.google.com/document/d/1dawyrxuyxnN3lGYGnIYzfEeGHq6GqMKUyZPpDKAejPI/edit) · [Sep 17 technical deep dive brief](https://docs.google.com/document/d/1_jBl7CvKactL-qzqpdpNJ-TeSC9OOxO3zASd3cZ0w5s/edit) · [Sep 3 call in Gong](https://app.gong.io/call?id=8546116675641297982) · [Sep 3 transcript](https://docs.google.com/document/d/1tsdPQISrvM2ITKkuhkAiwyKVaYwxhpXZcYKOXtXpMJM/edit) · RFP answers: Deals/Hostinger/Yuno-RFP-Response-Hostinger-Aug2026.md.

Evidence labels: ✅ verified · ⚠️ inference, unverified, roadmap or internal only (never state in the call) · ❓ open, needs an owner · 🔍 ask in discovery

### ⚠️ Pre-meeting actions (tonight and before 06:00)

1. **Justo and TJ have not responded to the Sep 24 invite.** Justo owns India status and the commercial frame; TJ is the local presence that Piotr wanted in the room. Ping both tonight. If Justo does not join, German takes the India block with Dirk and the commercial close alone (structure only, no numbers).
2. **No evidence that the Sep 17 prep items got done.** As of Sep 23, 20:00 UTC, nothing in Gmail, Slack or Drive shows the sandbox build, the three acceptance matrices, Dirk's retry-timing answer, Justo's India status or the vault material. Confirm with Dirk tonight what is actually ready. Anything not ready is stated in the room as "you will have it by {date}", never improvised.
3. **NDA is stuck on our side of the table now.** Paulius sent Hostinger's NDA via DocuSign to Diego (Sep 18). Ivvy rejected it (one-way, EUR 10k fixed penalty per event, IP ownership clause). Your Sep 21 email to Paulius (cc Ivvy) laid out the options and attached Yuno's mutual NDA. He has not replied. Two things to fix at the open: (a) the numbered list in that email came out garbled (the redlines option got folded into item 1, so he may have read two options instead of three); say the three options out loud: Yuno's mutual NDA, our redlines on his template, or his mutual template; (b) ask him to have Legal void the open envelope so nothing dangles.
4. **⚠️ Entity mismatch to check with Ivvy before he asks.** The mutual NDA you attached is titled "EN - Mutual NDA - Yuno Payments Limited", while the signatory data you sent Paulius names YUNO TECNOLOGIAS S.A.P.I. DE C.V. His Legal will notice. Get Ivvy's one-line answer on which entity signs which paper, tonight.
5. **Reply to Ivvy in #salesops-legal with the chosen route.** Still open since Sep 21.
6. **Correct three written RFP answers proactively** (details in section 9): retries cap is 6 in production, not 5; the subscription engine now supports card, PayPal and Pix Automático, not "cards only"; SMART retry timing applies from the second retry onward.
7. **India facts changed since the Sep 17 brief.** NPCI's interoperability framework is being rolled out and Razorpay claims mandate execution across gateways without re-registration. Use the wording in section 8.4, not the Sep 17 wording.
8. **Open Paulius's LinkedIn manually:** https://lt.linkedin.com/in/paulius-lapenas-25964976 (blocked for automated reading; background below comes from a single aggregator).
9. **TJ's title changed.** Slack now lists him as VP Transaction Rails (it said Engineering Management Consultant on Sep 15). Introduce him by that title. ⚠️ His Slack timezone is São Paulo while Piotr describes him as Vilnius-based; let Piotr confirm the "local in Vilnius" line before anyone uses it.

---

## 1. TL;DR Battle Card

**Five facts to know cold**

1. **What he is buying: the vault as a standalone service, for business continuity.** His words on Sep 3: 60 to 70% of revenue is subscription payments; he wants to own the tokens and keep charging if the orchestration layer goes down. "Finalize this year, plan for next year." Everything else (routing, retries, India) is what the vault plugs into.
2. **What decides tomorrow: precision, not breadth.** He wrote RFP question 3.6 ("token enrollment is far from 100%") to catch overclaiming. He has been oversold before, including by Yuno in a prior evaluation that we never raise. Every claim gets a live proof or a stated limit, limit first.
3. **He already runs an orchestrator.** Card subscriptions go through a third-party layer with PSP fallbacks and retry rules. Piotr confirmed it is ProcessOut (Checkout.com) as of March 2026. Never say "you lack orchestration". Never name ProcessOut, Credorax, Finaro or Shift4 unless he does.
4. **His constraint on retries is explicit.** Yuno may move an attempt inside his dunning window ("Thursday to Friday is okay"), never delay his cycle ("delay for one week, no use"). Chargebee today: up to 5 retries in 21 days, charging at the customer's original purchase hour, batches tripping PSP fraud rules.
5. **India is the wedge and it just moved.** He runs Razorpay and BillDesk direct, cross-border, roughly 70% UPI and 30% cards, two journeys, and wants one integration plus clarity on mandate portability. Since Sep 17: NPCI presented MyUPI at Global Fintech Fest (Sep 10), Razorpay markets mandate execution across gateways with no re-registration, and Yuno shipped a UPI Autopay fix on its EBANX India connection to production (Sep 21). Section 8.4 has the exact wording to use.

**Three hooks, in priority order**

1. **One token, any provider, even if a layer disappears.** A vaulted card charged through two of his PSPs from the same token, with the network transaction ID travelling with it. This is the business-continuity proof he asked for.
2. **Enrollment below 100% never blocks a charge.** Per provider at payment time: network token plus cryptogram where accepted, vaulted credential where not. Say it plainly and hand over the matrices scoped to Stripe, Adyen, Checkout.com, Razorpay and BillDesk. It converts the weakest column of our written RFP into the most tailored one.
3. **Retries that respect his window.** Real-time fallback across PSPs on every request his billing engine sends, and the retry timing model (DEFAULT, SMART, CUSTOM_SCHEDULE) described honestly: it moves attempts inside a window, capped at 6 in production, and it lives in our subscription engine, which fits the in-house scheduler he is building.

**THE objection he will raise:** "This is the third time Yuno tells me something is 'available on request' or 'confirm with your account team'. I am comparing orchestrators on paper. Where are the specifics?"

**The answer:** do not apologize; close it in the room. The matrices for network transaction ID, network token and wallet MIT acceptance, scoped to his five providers, are the specifics. If any cell is unknown, say unknown and commit to a date. Show the report columns (network_transaction_id, network_token, merchant_order_id) live so the data-warehouse question stops being theoretical.

**The ask:** (1) a working session with his hPayments engineers and Dirk within two weeks, (2) a written proposal for vault standalone plus India within a week (Justo owns pricing; structure only in the room), (3) which NDA route he prefers, today.

**Rapport opener:** Hostinger turned Kodee into "Hostinger Agent" on Sep 2, after Kodee resolved 91% of roughly 1.5 million support conversations a month on its own. One line, then move on. For the India block, GFF (Sep 8 to 11, Mumbai) is the natural bridge: "you probably followed what NPCI showed at GFF."

---

## 2. Who Is in the Room

| Name | Role | Side | Invite status | Notes |
|---|---|---|---|---|
| Paulius Lapėnas | Head of Payments, Hostinger Global | Hostinger | ✅ Accepted Sep 17 | Only Hostinger attendee on the invite. RFP owner. Controls roadmap and calendar |
| German Tatis | Business Development Manager, organizer | Yuno | Accepted | Owner of record in Salesforce since Sep 9 |
| Dirk van der Meulen | Senior Solutions Engineer (Amsterdam) | Yuno | ✅ Accepted Sep 17 | Runs the four proof points and India detail |
| Antoine Cathelin | Head of Product (Amsterdam) | Yuno | ✅ Accepted Sep 18 | Was on the Sep 3 call. Declined Sep 17, accepted Sep 24. Owns agentic/MPP and the Amex network token status |
| Piotr Sierpinski | Sales Manager Europe (Warsaw) | Yuno | ✅ Accepted Sep 23 | Knew Paulius and Mindaugas from Braintree/PayPal days; opens the India bridge |
| Tautvydas "TJ" Paukštė | VP Transaction Rails | Yuno | ⚠️ No response to Sep 24 (accepted the Sep 17 slot) | Short hello only |
| Justo Benetti | CRO | Yuno | ⚠️ No response | India status via India GM; commercial frame |

**Paulius Lapėnas.** ✅ Head of Payments, Hostinger Global (his signature, consistent April to September 2026). Aggregator profile (RocketReach, single source, ⚠️ unverified against LinkedIn): Head of Payments, Hostinger International, Vilnius; previously Western Union and Lindorff (Nordic collections, now Lowell); MA in E-business Management, Mykolas Romeris University, 2014 to 2017. LinkedIn profile exists (lt.linkedin.com/in/paulius-lapenas-25964976, roughly 1K followers) but could not be read by automation.

**How to read him.** A practitioner with a collections background: his RFP asks how to recover, not only avoid, failed renewals. He answers logistics fast and short ("Sure, who should be signing…", "Thanks, sent to our Legal.") and says nothing on substance until he has a view. He moved the call with two hours' notice and picked "same time next week" without discussion. He will reward narrow, specific answers and notice hedging instantly. He does not want issuer-specific logic ("I really don't want them to be building some logical flow just for a single issuer"). He wants one approach that covers all subscriptions.

**The Yuno room, roles agreed Sep 15 and updated Sep 23**

| Who | Does | Does not |
|---|---|---|
| German | Opens, runs discovery, keeps time, closes with the ask, sends every written follow-up (Piotr cc'd) | Improvise pricing |
| Dirk | Proof points A to D in the sandbox; the three matrices; the retry-timing answer; India connections detail | Claim anything not built |
| Antoine | States product truth when asked (Amex network tokens, subscription engine methods, MPP). One sentence on agentic only if Paulius raises it | Turn the demo into a roadmap session |
| Piotr | One line of history at the open if useful; opens the India block with the Berlin (March) and April thread; listens for what Paulius does not say | Run a parallel thread with Paulius |
| TJ | Hello at the open: VP Transaction Rails; local context if Piotr confirms it | Stay past 10 minutes |
| Justo (if he joins) | India status and the commercial frame at the close | |

**Relationship timeline (calendar and Gmail, ✅)**

| Date | What happened |
|---|---|
| Before 2026 | Prior Yuno evaluation that did not convert (previous Europe GM and a BD; questionnaire never answered). Never raise it |
| Late Mar 2026 | MPE Berlin: Hostinger tells Piotr they are happy with ProcessOut, not shopping, but want help with connections in India |
| Apr 2026 | Piotr sends them the "Payment Methods, India, Recurring / MIT Support" list (section 6.3) |
| Apr 29, 2026 | In person at Stripe Sessions SF, Booth 214: Juan Pablo Ortega, Justo, German, Paulius. India opened the door again |
| Jul 7, 2026 | Paulius: Q3 closed, "readiness for Q4", revisit August or early September. Questionnaire sent Jul 8 |
| Aug 6, 2026 | RFP answers returned ("Questions to orchestrators", 17 sections) |
| Sep 3, 2026 | 45 min debrief: German, Justo, Antoine, Dirk with Paulius alone. Recap with NDA entity sent the same day |
| Sep 9, 2026 | NDA reminder. Salesforce opportunity transferred to German |
| Sep 15, 2026 | Internal sync: German, Piotr, Dirk |
| Sep 17, 2026 | Paulius moves the demo ("unplanned conflict"). Rescheduled to Sep 24 within three hours; he accepted the same morning |
| Sep 18, 2026 | NDA: he asks for signatory data, German sends it, "Thanks, sent to our Legal." Hostinger's NDA reaches Diego via DocuSign |
| Sep 21, 2026 | Ivvy: cannot sign as sent. German emails Paulius the three routes and attaches Yuno's mutual NDA (cc Ivvy). Piotr reacts 👍. No reply from Paulius |
| Sep 24, 2026 | This demo |

**Prior meetings with the people on this call, per the calendar:** Apr 29 (Stripe Sessions booth, Paulius, Justo, Juan Pablo) and Sep 3 (debrief, Paulius, Justo, Antoine, Dirk). Nothing else. This is the third live conversation and the first demo.

**Implication:** follow-up framing. He has the RFP answers, the Sep 3 recap, and our NDA template. Do not re-explain Yuno. Open on what he wants to see and on the two discovery questions we have never asked (section 7.2).

**Other Hostinger names to know (never ask about them directly):** Mindaugas (Piotr's other contact from Braintree days, role today ⚠️ unverified); Gediminas Griška (named Head of Payments in an older ProcessOut interview, ⚠️ may still sit near this decision); Marija (head of expansion) and Robertas (head of billing) per a Jul 2025 SDR account map ⚠️; an open "Head of Payments" job posting exists ⚠️. CEO Giedrius Zakaitis since Jun 16, 2026, AI-first mandate. CFO Domantas Beržanskis.

---

## 3. What Paulius Wants, Ranked

Ranked by weight in the RFP plus what he chose to spend the Sep 3 call on. Gong's synthesis of the Sep 3 call and the 13 emails since Sep 2: he wants to see a full demonstration of the standalone vault, the subscription engine including plan creation and retry logic, and an update on Indian payment operations.

| # | Topic | Evidence | What "good" looks like tomorrow |
|---|---|---|---|
| 1 | **Vault standalone for business continuity**: own the tokens, charge through any PSP, migrate in without losing data, export if they leave | Sep 3: his stated interest and the only thing he asked to go deeper on. RFP 2.3, 2.4, 3.4, 9.1 to 9.3 | One vaulted card charged through two of his providers. Import with network transaction IDs. PCI proxy placeholder. Export path in one sentence. Permissions on PAN visibility |
| 2 | **Renewal authorization**: network tokens, network transaction IDs, account updater | Roughly half the RFP (sections 2, 3, 10, 11). Renewals price at roughly 3.5 to 4x the intro price, so a declined renewal is the most expensive event in his model | Enrollment with his TRID or ours. Token type per provider at payment time (3.6). Matrices scoped to his five providers. Limits stated first |
| 3 | **Retries inside his dunning schedule**, and renewal batches that stop tripping PSP fraud rules | Sep 3: the Chargebee pain and the verbatim constraint. RFP 11.1, 11.2 | Clear statement of what happens to a charge his billing engine sends us; the three retry strategies shown in plan creation; the cap said out loud |
| 4 | **India as one integration** over Razorpay and BillDesk, one journey, UPI recurring, portability status | Sep 3, plus Berlin and April with Piotr, plus Stripe Sessions with German | Which connections run UPI Autopay today, where Razorpay and BillDesk stand, portability status as verified, owner and date for the rest |
| 5 | **Routing, fallback, Monitors, operational safety** | RFP 5, 6, 7. He runs this today | One rule, one fallback, one Monitor, the audit log. Say plainly what is not there (webhook delivery logs in the payment screen) |
| 6 | **Data and BI**: order-level approval rate, warehouse export | RFP 4.3, 4.4; 4.4 was our weakest written answer | Report columns shown live; a real answer on export |
| 7 | Secondary RFP items: PayPal billing agreements (12), Apple Pay MPAN (13.4), pinless debit (8), co-badged cards (18) | RFP only | Answer if asked, limit first |
| 8 | Agentic payments (MPP, x402) | Sep 3, early, "keep us posted" | Antoine, one sentence, separate session |

**What he said, in his words (Sep 3, ✅ transcript)**

- Modular first: can the blocks (PCI proxy, vault, orchestration) be used separately? Justo and Antoine: yes, all standalone.
- "We still continue to look into the business redundancy problem and how we can be the owners of all the tokens we have, so we could continue our subscription business in case the orchestrator goes down."
- "It would be good to finalize this year and then have a plan at least for next year."
- Retries: "If I send you a request today, Thursday, my next request will come on Saturday. If your intelligence tells that don't charge on Thursday but attempt on Friday, that's okay with me because it will not impact my dunning. But if your intelligence will say delay for one week, then for us it's no use."
- India: Razorpay and BillDesk direct, cross-border, roughly 70% UPI, 30% cards, two journeys. "As far as I know the central bank does not allow it, but I'm not fully sure" (on moving tokens between providers).
- Agentic: stablecoin protocols (x402, Cloudflare wallet, MPP) over card rails for service businesses; already talking to Stripe on specs; open question on invoicing micro-payments.
- Org: "the overall organization is shifting priorities for the way we position ourselves in the market."

---

## 4. The Company, in Brief

Hostinger (Lithuania) sells hosting, VPS, domains and AI website and app builders on long prepaid terms that renew at roughly 3.5 to 4x the introductory per-period price, which is why a declined renewal is a large revenue event and why the RFP is half about renewal authorization. Bootstrapped, no VC; ConHostinger GmbH holds roughly 31% (2021). CEO Giedrius Zakaitis since Jun 16, 2026 (from CPTO, AI-first mandate); chairman Arnas Stuopelis; CFO Domantas Beržanskis. Contracting entities per the Terms of Service: Hostinger International Limited (Cyprus, primary), Hostinger PTE LTD (Singapore), Hostinger Global S.à r.l (Luxembourg), Hostinger UK Limited, PT WEB MEDIA TECHNOLOGY INDONESIA, plus two Lithuanian operating entities. Payments sit inside product: an "hPayments" technical team plus a strategy team (PSP relationships, fraud, disputes) ⚠️ per an older public interview.

**Financials (Hostinger's own results post, Feb 23, 2026 ✅)**

| FY | Revenue | Growth | Customers |
|---|---|---|---|
| 2022 | €69.6M | +64% | 1.5M |
| 2023 | €110.2M | +57% | 2.4M |
| 2024 | €182.4M | +65% | 3.5M |
| 2025 | €275.4M | +51% | 4.6M |

58% revenue CAGR 2022 to 2025; first EBITDA-positive year 2023 (€2.4M); FY2023 cash billings €139.1M against €110.2M recognized revenue (prepaid model); roughly €14M opex saved through AI automation; €11.8M employee stock-option payout Mar 18, 2026; ⚠️ FY2025 net profit roughly €38.4M per a registry aggregator, unverified. No IPO plans found. **So what:** a company compounding at 50%+ on a long-prepaid, high-renewal-multiple model has a renewal-authorization problem that grows every quarter, and the budget to fix it. Never frame it as "you are losing money"; he knows his numbers better than we do.

**Competitive landscape (context only, never a talking point).** W3Techs measures share of surveyed websites detected on each platform, not revenue. Hostinger is #2 by that measure at 5.1%, behind Shopify (5.3%), ahead of Wix (4.2%), IONOS (2.6%), GoDaddy (2.5%), Squarespace (2.5%), Newfold (2.4%), OVHcloud (2.4%), team.blue (2.2%), Hetzner (2.2%), SiteGround (2.0%), DigitalOcean (1.5%). Scale proxies and payments posture per competitor are in the Sep 3 brief. None of the peers has a disclosed orchestration or PSP-independence story; GoDaddy and Squarespace (via Stripe) went the other way, toward a single processor. Hostinger is growing faster than every large peer with a disclosed rate, at roughly a quarter of GoDaddy's or IONOS's revenue per customer.

---

## 5. News & Signals (newest first)

| Date | Item | Use |
|---|---|---|
| Sep 23, 2026 | Hostinger status page: emergency maintenance on server IN-840 (India), investigating 09:27 UTC, resolved 09:49 UTC | Do not raise. Context only: India traffic is on their radar today |
| Sep 21, 2026 | ⚠️ Internal: ebanx-int v2.10.6 released to production fixing UPI Autopay mandate creation on EBANX India connections (subscription_name sanitization). Same day: PayU India partner agreement signed for another merchant covering cards, RuPay and e-mandates (card SI plus UPI Autopay) | Evidence that UPI Autopay recurring runs on Yuno's EBANX India connection today. Dirk confirms which connections before we name them |
| Sep 10, 2026 | NPCI launched MyUPI at Global Fintech Fest (announced by the RBI Governor): one view of a user's UPI transactions and active AutoPay mandates across apps and banks | India bridge line |
| Sep 8 to 11, 2026 | Global Fintech Fest 2026, Mumbai (PCI, NPCI, FCC). Reports since Aug 31 expected NPCI to formalize AutoPay mandate portability there | See section 8.4 for what is verified |
| Sep 2, 2026 | Hostinger Agent: Kodee, which resolved 91% of roughly 1.5M support conversations a month on its own, became a broader business tool | Rapport opener |
| Sep 1, 2026 | Hostinger launched Managed Hermes Agent (developer-grade AI agent for anyone) | Context |
| Aug 31, 2026 | Reports (Medianama, Inc42, others): NPCI to let users port UPI AutoPay mandates across apps and merchants move mandate bases between gateways; based on NPCI's Oct 2025 framework (Merchant Identifier Code, purpose code AZ); user-side portability once per rolling 90 days with UPI PIN; Razorpay staged rollout from Jul 2026 | India block wording |
| Aug 18, 2026 | Hostinger AI Builder launched | Context |
| Jul 28, 2026 | Hostinger: 3,000+ new servers and new data centers | Context |
| Jun 16, 2026 | CEO transition to Giedrius Zakaitis | "Organization shifting priorities" (his words Sep 3) |
| Oct 6, 2025 | Razorpay blog: UPI Autopay interoperability on Razorpay's APB Switch, routing mandate executions across gateways and acquirers on NPCI's MIC framework, "no re-registration required" | Razorpay's claim, label it as such |

---

## 6. Payments Money Map

### 6.1 Their stack as we know it

| Layer | What we know | Source |
|---|---|---|
| PSPs | Stripe, Adyen, Checkout.com, local providers in APAC and LatAm | Paulius ✅ |
| India | Razorpay and BillDesk, direct, cross-border, roughly 70% UPI / 30% cards, two journeys | Paulius ✅ |
| Orchestration | Third-party layer for card subscriptions with PSP fallbacks and retry rules (Paulius). ProcessOut, Checkout.com, as of March 2026 (Piotr) | ✅ |
| Billing | Chargebee, migrating in-house gradually; up to 5 retries in 21 days; charges at the customer's original purchase hour | Paulius ✅ |
| Wallets and APMs | PayPal (billing agreements), Apple Pay, Google Pay, Revolut Pay (recent, small); PayTM, LatAm and India APMs direct with no fallback | Paulius ✅ |
| Acquiring history | Credorax (2021), later Finaro, now inside Shift4 | Public ✅, current status ⚠️ |
| Fraud and identity | Ravelin, iDenfy (privacy policy) | Public ✅ |
| Descriptors | Six card descriptors, including EBN* (⚠️ EBANX in LatAm) and DM.HOSTINGERCOMBR (second Brazil rail, unidentified); dLocal for Japan | Public ⚠️ |
| Checkout observed Sep 2 | Netherlands: cards, PayPal, Google Pay, Apple Pay, CoinGate, Alipay; no iDEAL. Colombia: PayPal, Google Pay, Apple Pay, Nequi | Antoine and German ✅ |
| Stated pains (public) | "Lack of 3DS coverage in Latin America makes fighting chargebacks challenging"; some methods cannot be tokenized, hurting recurring revenue | Interview ✅ |

### 6.2 Framing rules for this account

- The vault is the product. Orchestration is why it is safer to buy the vault from Yuno than from a vault-only vendor: connectors already running volume, regions in the US (two), EU, APAC, KSA and India, 24/7 NOC (Justo, Sep 3).
- Independence from any PSP is our argument. Make it once, plainly, only if he brings up his own history with a partner that got acquired.
- Local payment methods (iDEAL in NL, the thin Colombia mix) are a later thread. Not tomorrow.

### 6.3 The India list Piotr already sent them (April 2026)

Paulius may hold tomorrow's answers against it. Cards recurring and MIT on Visa, Mastercard, RuPay, Amex, Diners, JCB, Discover via Airwallex, Adyen, Stripe, Checkout.com, Splitit, Worldpay, Unlimint, Nuvei, NMI. Apple Pay MIT via Adyen, Stripe, Checkout.com, Airwallex, Braintree. Google Pay MIT via Stripe, Airwallex, Adyen. UPI Autopay "via supported UPI-enabled providers", none named. Afterpay and Cash App Pay via Stripe (not India).

What this means tomorrow: Razorpay and BillDesk are not on that list and must be addressed by name; UPI Autopay providers must be named this time (section 8.4); card brands accepted for recurring are not the same as Amex network tokens or Amex account updater, say it in those words if he connects the two; drop Afterpay and Cash App Pay from anything India.

---

## 7. How to Run the Meeting

### 7.1 Format

Not a from-scratch tour. Four proof points in the dashboard or API, then India in six minutes, then the close. No slides between proof points. Dirk drives the screen; German drives the conversation and the clock. When Paulius interrupts with a question, answer it narrowly and return to the proof point. If a limit exists, say it before he asks. If something is unknown, say unknown and give a date.

### 7.2 Discovery in the first five minutes

We have never asked why they are looking. Two questions before any demo:

1. "What triggered the business-continuity review this year, and what does 'decide this year, plan next year' need to contain to get approved?"
2. "If the orchestration layer went down for 48 hours today, what exactly stops, and what would you need from a vault to keep charging?"

The second answer becomes the success criterion for proof point A. Write it down and repeat it back when A is shown.

### 7.3 The proof points

| Proof point | Show | Say | State the limit before he asks |
|---|---|---|---|
| A. One token, two PSPs | A vaulted card charged on Stripe and Adyen test connections; export path; user permissions on PAN visibility | "If a layer goes down, you charge from the vault through any of these" | Bulk backfill outside a migration is handled with the Yuno team, not a self-serve endpoint (RFP 2.3). Export at exit: state the process in one sentence only if Dirk has confirmed it; otherwise "it goes in writing in the proposal" |
| B. Migration keeps the data | Token import with network transaction IDs; PCI proxy request with the network transaction ID placeholder; report with network_transaction_id, network_token and merchant_order_id columns | "Card data and network transaction IDs import together (PGP, SFTP). Order-level approval rate comes straight from the report" | Vault health (share of tokens with a network transaction ID) is run by our team, not self-serve; offer to run it during the evaluation (2.4). Migration timeline depends on the source gateway's response time |
| C. Renewal authorization | Enrollment with his TRID or ours; token type per provider at payment time; hand over the three matrices | "Enrollment below 100% never blocks a charge" | Account updater is Visa and Mastercard only; scheme registration up to 10 working days. Amex network tokens: Antoine states the current status (section 9) |
| D. Retries and routing, plus the engine he asked about | One routing rule by country or BIN, one fallback on provider error, one Monitor with a threshold, the audit log; then plan creation in the subscription engine showing the three retry strategies | "Real-time fallback on every request your billing engine sends. Retry timing moves the attempt inside your window, never past it" (see section 9 for the exact scope of that claim) | Production cap is 6 attempts (our written answer said 5; correct it). Sandbox shows 5 today. SMART timing applies from the second retry; the first retry uses the fixed 5h delay. Webhook delivery logs are not in the payment screen (7.1) |

If he asks about replacing Chargebee: "You keep the schedule, we execute the charge, route the retry through a different PSP and pick the moment inside your window." Do not pitch replacing Chargebee.

### 7.4 India in six minutes

Piotr opens: in Berlin they mentioned UPI challenges, he sent the April list, tomorrow is where we land it. Then Dirk or Justo: which connections run UPI Autopay recurring today, where Razorpay and BillDesk stand, one integration and one journey, portability status as verified (wording in 8.4), owner and date for what is not confirmed. Ask the two India questions (section 12, 8 and 9).

### 7.5 The close

German: "Three things I would like to leave with. A working session between Dirk and your hPayments engineers in the next two weeks; a written proposal for the vault standalone and India within a week; and your preferred route on the NDA so Legal can close it this week." Then ask who from his side joins the engineering session and who else is part of the decision. Confirm the date of the follow-up email (same day).

### 7.6 If things go sideways

- **Justo absent:** German takes India with Dirk; commercial frame is "platform fee plus fee on successful transactions; numbers follow with volume in the proposal".
- **Paulius brings engineers:** good; let Dirk go deeper on proof points B and D, cut section 4 talk to zero.
- **He raises ProcessOut or Checkout.com himself:** one sentence on independence (a layer bought by a PSP stops being independent), then back to the proof point. Never first.
- **He raises the prior Yuno experience:** acknowledge once, point at what is different (answers on paper, specifics in hand, one owner), move on.
- **He asks for pricing:** structure only. "Justo owns the numbers and they depend on volume; you will have them in writing within a week."
- **He asks about agentic/MPP:** Antoine, one sentence: he is designing the MPP integration and wants Paulius's merchant feedback; separate session.
- **Sandbox fails on something:** say what it was supposed to show, show the API or docs equivalent, and put it in the follow-up. Do not narrate around a broken screen.

---

## 8. Internal Alignment: What We Agreed, What Changed, What Is Open

### 8.1 Decisions from the Sep 15 sync (German, Piotr, Dirk) ✅

- Ownership: German is owner of record (Salesforce, Sep 9). Piotr supports with the relationship. One written voice: German sends, Piotr cc'd. Credit split is a Sean and Justo conversation, not for the demo.
- Format: no interactive from-scratch demo; few strong points with live proof; Dirk demos and looks at India; Piotr silent unless history helps; TJ 10 minutes for local presence.
- Position: vault standalone is the product; orchestration is what makes it safe.
- The ask: engineering session on the call, proposal in parallel within a week. Justo to own vault standalone pricing (not in the deal calculator).

### 8.2 What changed since Sep 15 and Sep 17

| Change | Detail | Effect tomorrow |
|---|---|---|
| Demo moved | Paulius asked Sep 17 07:58 UTC; rebooked same day; he accepted 10:55 UTC | One more week passed with no Hostinger reply on substance |
| Antoine joins | Accepted Sep 18 after declining the Sep 17 slot | Product truth is in the room; agentic can be answered by its owner |
| Piotr confirmed | Accepted Sep 23 | India bridge and history available |
| TJ | Title now VP Transaction Rails; no response to the new date | Introduce by title; confirm attendance tonight |
| NDA | Hostinger's paper rejected by Ivvy (Sep 21); three routes emailed with Yuno's mutual NDA attached; no reply | Ask the route at the open; fix the numbering and the entity question |
| Subscription engine methods | docs.y.uno (read Sep 23): CARD, PAYPAL_ENROLLMENT and PIX_AUTOMATIC, all via previously enrolled instruments | Correct RFP 11.1 ("only Cards") proactively |
| Retry facts | docs.y.uno: DEFAULT (5h, 12h, 24h, 36h, 48h, 96h), SMART (ML from the second retry), CUSTOM_SCHEDULE (up to 7 attempts, 1 second to 7 days per delay); production cap 6, sandbox 5 | Correct RFP 11.2 ("up to 5") proactively |
| India | NPCI interoperability framework rolling out; Razorpay claims cross-gateway execution with no re-registration; Yuno UPI Autopay fix live on EBANX India (Sep 21); PayU India agreement signed (Sep 21) | Use section 8.4 wording |
| Report fields verified | docs.y.uno reports fields: network_transaction_id (Payment, Transaction, Reconciliation reports), network_token, network_token_type, merchant_order_id, subscription_id, billing_cycles_current / next_at / total | Show them live in proof point B; data-warehouse connectors still ❓ |

### 8.3 Open items and owners (status as of Sep 23, 20:00 UTC)

| Item | Owner | Status |
|---|---|---|
| Sandbox with Stripe, Adyen and Checkout.com test connections; vaulted card with network transaction ID charged on two of them; one rule, one fallback, one Monitor; PCI proxy request; report with the three columns; a subscription plan with the three retry strategies | Dirk | ❓ no evidence visible |
| The three matrices (2.1 network transaction ID, 3.5 network token, 13.3 wallet MIT) scoped to Stripe, Adyen, Checkout.com, Razorpay, BillDesk, as documents he can keep | Dirk with Solutions | ❓ no evidence visible |
| Retry-timing answer for merchant-scheduled charges (does SMART or CUSTOM timing apply to MITs his scheduler sends, or only to engine cycles) | Dirk | ❓ committed Sep 3, no answer visible |
| Token export at termination: the process in one sentence | Dirk | ❓ (docs do not cover it; legal has precedent for a termination migration clause ⚠️ internal) |
| Data warehouse connectors (4.4) and routing audit trail (6.3) | Dirk | ❓ (report fields verified; connectors not found in docs) |
| Which Yuno connections run UPI Autopay recurring today; Razorpay and BillDesk status for cards and UPI; PayU India integration status | Dirk with Product | ❓ EBANX India ✅ per Sep 21 release; rest open |
| NPCI portability live date and BillDesk readiness through the India GM | Justo | ❓ committed Sep 3, nothing sent |
| Vault standalone material "full breadth and depth" | Justo | ❓ the demo can replace it if the proposal follows within a week |
| Vault standalone pricing for the proposal | Justo | ❓ not in the deal calculator |
| Revolut Pay and Mastercard funded-card notification info | Justo | Low priority (Paulius: Revolut is small) |
| Piotr's notes from Berlin (March 2026) | Piotr | ❓ promised Sep 15, not received |
| Amex network tokens: current status | Antoine | ⚠️ RFP 3.1 and docs.y.uno list Amex; Antoine said Sep 2 it is months away. He is on the call; he answers it |
| NDA route and entity question | German, Ivvy | ❓ open since Sep 21 |
| Justo's and TJ's RSVP | German | ❓ |

### 8.4 India: exactly what to say

**Verified, can say:** NPCI has a framework for interoperable UPI AutoPay mandates (Merchant Identifier Code) and aggregators are rolling it out; NPCI presented MyUPI at Global Fintech Fest on Sep 10 (one view of transactions and mandates across apps); Razorpay states publicly that its switch can route mandate executions across gateways and acquirers with no customer re-registration. UPI Autopay recurring runs in production on Yuno's India connections today (EBANX ✅ per the Sep 21 release; Dirk confirms the full list before we name more).

**Not verified, do not say:** that merchant-side mandate portability is live across the whole ecosystem; that BillDesk supports it; that "the central bank mandate exists and players comply by year-end" (Sep 3 wording, retire it); any date.

**The line:** "The NPCI framework for moving mandates between providers exists and is being rolled out; Razorpay says it can execute mandates registered elsewhere without re-registration. What I will confirm through our India team this week is BillDesk's status and what it means for moving your existing base under one integration. On our side, UPI Autopay recurring is live on our India connections today; Dirk will walk you through which ones, and where Razorpay and BillDesk stand as connections."

**Cards in India:** RBI card-on-file tokens are issued by the networks and issuers, not by the acquirer, so a network token is not tied to Razorpay or BillDesk ⚠️ confirm with Product for the MIT flow on both before stating as fact.

---

## 9. Facts to Have Straight

| Topic | Say | Do not say | Status |
|---|---|---|---|
| Retry strategies (subscription engine) | Three per plan: DEFAULT fixed schedule (5h, 12h, 24h, 36h, 48h, 96h), SMART (ML timing on decline reason, country, issuer, provider, applied from the second retry onward), CUSTOM_SCHEDULE (per-attempt delay from 1 second to 7 days, up to 7 attempts). stop_on_hard_decline stops the current cycle only. Cap 6 in production | "Unlimited", "5 in production", "A/B testing" (not in docs) | docs.y.uno ✅ (Sep 23) |
| Retry timing for charges his own billing engine sends | Until Dirk confirms: real-time fallback across PSPs on every request; time-shifted retries are a feature of our subscription engine that fits his in-house scheduler when billing moves | "We pick the moment" for standalone charges | ❓ Dirk |
| Subscription engine, payment methods | Card, PayPal (enrollment) and Pix Automático, all through previously vaulted instruments | "UPI Autopay inside the engine" (not in docs), "cards only" (outdated) | docs.y.uno ✅ |
| Subscription engine, results | Externally: the published 7% uplift and 30% recovered revenue only | Internal deck numbers (16 merchants, 135K subscriptions, 86% per cycle) | ⚠️ internal only |
| Account updater | Visa and Mastercard; asynchronous; vaulted token and fingerprint stay stable; enrollment.update webhook; registration up to 10 working days | Amex | docs.y.uno ✅ |
| Network tokens | Visa and Mastercard live; TRID theirs or ours; per-provider selection at payment time; vaulted credential used where a provider does not accept the token | Amex live, unless Antoine says so in the room. RFP 3.1 and docs list Amex; Antoine (Sep 2): months away | ⚠️ Antoine answers |
| Network transaction IDs | Stored per credential; merchant-supplied value accepted in the payment request; imported with card data in migration; injected by the PCI proxy placeholder; present in Payment, Transaction and Reconciliation reports | A self-serve bulk backfill endpoint | docs.y.uno ✅ |
| Token migration | Merchant requests migration from the current processor; Yuno and the provider import card data into the vault (PGP, SFTP); merchant maps provider tokens to vaulted_tokens via API. Network token migration imports token number, expiry, holder, last four, network transaction ID, provider reference | A fixed timeline (the source gateway's response time drives it) | docs.y.uno ✅ |
| Token export at exit | Only what Dirk confirms; otherwise "in writing in the proposal" | Anything improvised | ❓ |
| PCI proxy | Forward proxy through Yuno's PCI environment; placeholders for PAN, expiry, holder, network transaction ID; response redaction header; 1 MB body, 20 tokens per request, timeout up to 120 s; proxied calls audited, not listed as payments | Proxied calls appear as payments | RFP ✅ |
| Fallbacks and Monitors | Condition-based chains on decline, timeout or error; Monitors redirect traffic below an approval threshold and auto-recover; alerts by email and Opsgenie | | docs.y.uno ✅ |
| Webhooks | At-least-once, seven attempts out to 96 hours, HMAC and OAuth2, unified event model | Delivery logs in the payment screen | RFP ✅ (7.1 is a no) |
| Reporting | Report fields verified (section 8.2); Reporting API per RFP 4.4 | Named warehouse connectors (none found in docs) | ⚠️ partial |
| Pinless debit | Acquirer capability; Yuno segments debit traffic and routes it to connections where it is enabled | A Yuno-side debit switch | RFP ✅ |
| Backend SDKs | REST API only, by design; Postman collection | Kotlin, Java or Node server SDKs | RFP ✅ |
| PayPal billing agreements | IDs are scoped to the PayPal merchant account, so they stay valid if Hostinger keeps the same account; Yuno has migrated agreement portfolios; zero-value verification available | | RFP ✅ |
| SLA and what "Yuno goes down" means | The vault answers the continuity question: the tokens are theirs. Yuno's SLA covers availability of the Yuno platform, APIs and routing; third-party providers are excluded; credits are set in the order form | Numbers from other deals | ⚠️ legal precedent, internal |
| Interchange and scheme fee effect of network tokens and 3DS | Nothing numeric | Antoine's Sep 2 figures (5.5 bps Mastercard, 7.5 bps Visa), unverified | ⚠️ |
| Infrastructure | Regions: two in the US, one EU, one APAC, KSA, India; 24/7 NOC | | Justo, Sep 3 ✅ |
| India, portability | Section 8.4 wording | "The mandate exists and players comply by year-end" | ⚠️ |

---

## 10. Selling Yuno Here

**Core frame.** Vault standalone is the product. Orchestration is why it is safer with us than with a vault-only vendor: the connectors are plugged in and running volume, the regions exist, the NOC is 24/7. Show orchestration as what the vault plugs into, never as a second pitch.

**Hooks with proof**
- Business continuity: one token charged through two PSPs, live (proof A).
- Migration without loss: network transaction IDs travel with the card data; PCI proxy injects them; reports expose them (proof B).
- Honest tokenization: enrollment below 100% never blocks a charge; matrices in hand (proof C).
- Retries inside his window: the three strategies shown in plan creation, cap stated (proof D).
- Published subscription results only: 7% uplift, 30% recovered revenue.
- India: live UPI Autopay on our India connections, portability framed as verified (8.4).

**Competitive frame, once.** The RFP is addressed to orchestrators, plural. Their optimization partner was bought by Checkout.com (2020), their acquirer by Shift4 (2022). Independence from any PSP is the argument. We do not name any of them first.

**Landmines**
- Never say Hostinger "lacks" orchestration.
- Never raise the prior Yuno evaluation.
- Never claim Amex on account updater, backend SDKs, unlimited retries, webhook delivery logs in the payments screen, "cards only" for subscriptions, or a self-serve backfill.
- Never repeat the Sep 3 India mandate wording.
- Never name ProcessOut, Credorax, Finaro or Shift4 first.
- Never improvise a price or an SLA number.
- One email thread to Paulius: German writes, Piotr cc'd.
- No dashes as punctuation in anything sent to him; no "no small feat".

---

## 11. Be Ready For

| They ask | You answer |
|---|---|
| "Why will this go differently than last time?" | Do not relitigate. What changed: answers on paper (Aug 6), specifics in hand (matrices, live proof), one owner (German), product in the room (Antoine, Dirk). Then show proof A |
| "Which of our PSPs accept a network transaction ID and a network token?" | The matrices, scoped to his five. Unknown cells are unknown, with a date |
| "If Yuno goes down, what happens to my renewals?" | The tokens are his, in a vault that charges through any connected PSP; that is the design. SLA covers the Yuno platform; third parties are excluded; credits are in the order form. Then repeat his own 48-hour answer from discovery and show that proof A covers it |
| "Can I export my tokens if I leave?" | Only what Dirk confirmed; otherwise: "the process goes in writing in the proposal, and our order form can carry a termination migration clause" |
| "How long does migration take?" | Card data plus network transaction IDs import together over PGP and SFTP; the source gateway's response time drives the calendar; account updater scheme registration is a separate track up to 10 working days. Sequence both against his "decide this year, plan next year" |
| "Do you have Razorpay and BillDesk?" | Truthfully, per what Dirk confirms. If not as connections today: which India connections run UPI Autopay and cards now, and what it takes to add his two |
| "Can your retry logic delay my dunning cycle?" | No, and we would not want it to. It moves the attempt inside the window. Real-time fallback runs on every request regardless |
| "Amex network tokens?" | Antoine states the current status. If not live: Visa and Mastercard live, Amex on the roadmap with the scheme, and Amex volume is processed on the vaulted credential meanwhile |
| "Do you have a subscription dashboard?" | Not a dedicated one. Insights segmentation over recurring traffic, subscription and billing-cycle fields in reports for his BI, lifecycle webhooks. Given his 4.3 question, his BI path is better for him |
| "Data warehouse export?" | Reporting API plus the report fields shown live; no native connector to name today; he ingests the files |
| "Backend SDKs?" | REST API only, by design; Postman collection |
| "Pinless debit in the US?" | Acquirer capability; Yuno routes debit BINs to connections where it is enabled; validated against his US acquirers |
| "What does it cost?" | Platform fee plus a fee on successful transactions; numbers with volume, in writing within a week; Justo owns it |
| "Agentic, MPP, x402?" | Antoine: designing the MPP integration, wants his merchant feedback, separate session |
| "NDA?" | Three routes, his choice; our mutual template is already in his inbox; void the open envelope |

---

## 12. Run of Show (45 minutes) with notes

| Min | Block | Owner | Notes |
|---|---|---|---|
| 0 to 5 | Open. TJ and Piotr one line each. NDA route (three options said out loud, void the envelope). The two discovery questions (7.2). Write down his 48-hour answer | German | Notes: ____ |
| 5 to 17 | Proof points A and B: one token through two PSPs; migration with network transaction IDs; PCI proxy; export line; permissions; report columns | Dirk | Notes: ____ |
| 17 to 26 | Proof point C: network tokens, TRID, token type per provider, account updater. Hand over the matrices. Limits first. Antoine on Amex if asked | Dirk, German, Antoine | Notes: ____ |
| 26 to 33 | Proof point D: routing rule, fallback, Monitor, audit log; plan creation with the three retry strategies; the dunning-window answer; cap 6 | Dirk | Notes: ____ |
| 33 to 39 | India: Piotr bridges from Berlin and April; connections running UPI Autopay; Razorpay and BillDesk status; one integration; portability line (8.4) | Piotr, Dirk, Justo or German | Notes: ____ |
| 39 to 45 | Close: engineering session date, proposal in a week, NDA route, who else decides, who joins from hPayments | German | Notes: ____ |

---

## 13. Questions for Paulius (with notes)

1. What triggered the business-continuity review this year, and what does "decide this year, plan next year" need to contain to get approved? **Notes: ____**
2. If the orchestration layer went down for 48 hours today, what exactly stops, and what would you need from a vault to keep charging? **Notes: ____**
3. Where do the tokens live today, how many are there, and what share carries a network transaction ID? **Notes: ____**
4. Network token enrollment today: coverage, and is the TRID yours or the provider's? **Notes: ____**
5. How much Amex card-on-file volume do you carry? **Notes: ____**
6. Which providers must be in the acceptance matrices beyond Stripe, Adyen, Checkout.com, Razorpay and BillDesk? **Notes: ____**
7. When billing moves in-house, will your scheduler send us each charge with a deadline, so retry timing can work inside the window? And how far along is the move from Chargebee? **Notes: ____**
8. In Berlin you mentioned challenges with UPI. Which ones, and do they still stand? **Notes: ____**
9. India: what would "one integration" have to cover on day one (UPI Autopay, cards, mandates already live, both providers)? **Notes: ____**
10. Who else is part of this decision, and who from hPayments joins the engineering session? **Notes: ____**
11. Which NDA route do you prefer, and can your Legal void the open envelope? **Notes: ____**
12. What did you think of the RFP answers: which sections did you push back on? (Only if time allows; he has not commented since Aug 6.) **Notes: ____**

---

## 14. Post-Meeting Checklist

- Same-day recap to Paulius (Piotr cc'd): what was shown, every limit stated, the three commitments with dates, the matrices attached or dated, the NDA route.
- Deliver every promised item within 48 hours; this account is judged on precision.
- Message Justo with the proposal scope (vault standalone plus India), the volume inputs gathered, and the date promised.
- Confirm with Dirk the engineering session date and who from hPayments attends.
- Tell Ivvy the NDA route and the entity answer; get the envelope voided.
- Log in Salesforce: next step, close date consistent with "decision this year".
- Update memory: his 48-hour answer, token count and network transaction ID share if given, Amex share, Chargebee migration status, India day-one scope, who else decides, NDA route, TJ's role.

---

### Sources
Google Calendar (events "Hostinger + Yuno | Demo" Sep 24, "Hostinger + Yuno" Sep 3 with recording and transcript attachments, "Hostinger + Yuno | Stripe Sessions Booth 214" Apr 29, 2026; attendee statuses read Sep 23, 20:11 UTC) · Gmail thread "Hostinger + Yuno | Demo" (Sep 17 to 21, 2026, including Paulius's Sep 17 and Sep 18 replies and German's Sep 21 NDA email with the attachment "EN - Mutual NDA - Yuno Payments Limited.docx.pdf"); calendar acceptances Sep 17 to 23; no drafts pending to Paulius · Gong ask_account on CRM account Hostinger (001Hu00003OAHynIAH), Sep 1 to 23, 2026: 1 call, 13 emails · Slack: #salesops-legal thread "NDA - Hostinger" (Sep 3 to 21), #release-requests (ebanx-int v2.10.6, Sep 21), #partnerships-only-visibility-integrations (PayU India agreement, Sep 21), Slack user directory (TJ, Dirk, read Sep 23), DM with Piotr (Sep 3), #sdr-bdm-global (Jul 2025 account map) · Google Drive: "Technical Deep Dive Brief: Hostinger (Sep 17, 2026)", "Internal Sync Brief: Hostinger demo prep (Sep 15, 2026)", Sep 3 meeting brief · Deals/Hostinger/hostinger-call-transcript-2026-09-03.md · Deals/Hostinger/Yuno-RFP-Response-Hostinger-Aug2026.md · docs.y.uno (read Sep 23): subscriptions, subscriptions retries, network tokens, network token migration process, token migration via API, data migration processes, reports fields · Hostinger blog and newsroom (Sep 1, Sep 2, Aug 18, Jul 28, Jun 16, Feb 23, 2026), Hostinger status page (Sep 10 to 23, 2026) · Medianama, Inc42, India TV, Trak.in, Lapaas Voice (Aug 31, 2026) on NPCI UPI AutoPay portability · ClearingPost on NPCI MyUPI (Sep 10, 2026) · Razorpay blog "UPI Autopay interoperability" (Oct 6, 2025) and Razorpay guides on international subscriptions and gateway migration (2026) · Vajiram, 10times, The Hawk on Global Fintech Fest 2026 dates (Sep 8 to 11, Mumbai) · RocketReach (Paulius Lapėnas) · W3Techs and public filings as cited in the Sep 3 brief.

---

## 15. Opening script (German, first 2 minutes, spoken)

"Paulius, thanks for making the time this week. Quick round of the room: Dirk, Senior Solutions Engineer, drives the screen today. Antoine, Head of Product, who you met on the third. Piotr, who runs Europe for us and knows you from his Braintree days. TJ, our VP of Transaction Rails. [Justo, our CRO, if present.]

Where we are, in one minute. We met in San Francisco in April. In July you sent the questionnaire, we returned the answers on August 6, and on September 3 you told us what actually matters. Three things. First, the vault as a standalone service: 60 to 70 percent of your revenue is subscription, and you want to own the tokens and keep charging if any layer above them goes down. Second, retries: we can move an attempt inside your dunning window, we can never delay your cycle. Third, India: one integration over Razorpay and BillDesk, one journey, and clarity on where mandate portability stands. On agentic you asked us to keep you posted, and Antoine will.

Before we show anything, three corrections to our written answers, because you care about precision more than polish. Our production cap on retries is six attempts, not five. The subscription engine supports card, PayPal and Pix Automático, not cards only. And smart retry timing applies from the second retry; the first retry follows the fixed schedule.

Today, 45 minutes, no slides. Four things live: one vaulted card charged through two of your providers; a migration that keeps the network transaction IDs, with the PCI proxy and the report fields; network tokens with your TRID or ours, plus the acceptance matrices for your five providers; and routing, fallback, monitors and the retry strategies inside plan creation. Then six minutes on India, then next steps. Where something has a limit, we say it before you ask. One housekeeping item for the end: the NDA route, so Legal can close it this week.

Two questions first, so the demo answers your situation and not ours. What triggered the business-continuity review this year, and what does 'decide this year, plan next year' need to contain to get approved? And if the orchestration layer went down for 48 hours today, what exactly stops?"

**30-second version (if he wants to go straight in):** "Quick frame and then Dirk takes over. On September 3 you gave us three priorities: the vault as a standalone service for business continuity, retries that stay inside your dunning window, and India as one integration over Razorpay and BillDesk. Three corrections to our written answers first: retries cap at six in production, not five; the subscription engine takes card, PayPal and Pix Automático; smart timing starts at the second retry. Four live proofs, then India, then next steps, limits stated before you ask. One question before we start: if the orchestration layer went down for 48 hours today, what exactly stops?"
