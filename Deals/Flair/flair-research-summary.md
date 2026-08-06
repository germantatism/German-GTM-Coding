# FLAIR AIRLINES — RESEARCH & CALL SUMMARY (YUNO)
*Prepared by German Tatis | Updated 2026-07-07 | Sources: discovery call transcript, email chain, prior research*

---

## 1. WHO IS IN THE CONVERSATION (WHO'S WHO)

### Flair Airlines
- **Juliana Ramirez** — Chief Digital Officer (stated on call). ~3.5 years at Flair. The person who re-engaged after a long silence; owns digital / e-commerce / ancillary. Champion, senior sponsor. Native Spanish speaker (Mexican; ex-Volaris, ex-OYO Mexico), so Spanish rapport works with her. Frames the mandate and the roadmap.
- **Lucas Oordt-Bosman** — Director, Payments & Digital Strategy. ~4 years at Flair; started in ancillary, moved into payments and now owns the payment stack. **The real decision owner and technical evaluator.** Vancouver-based, Dutch native, English only (do not open in Spanish). Currently the internal champion for buying: explicitly said he is "trying to push us towards the buy" in a build-vs-buy debate.
- **Abigail Wigle** — Payments & Revenue Integrity, works directly under/with Lucas. ~1.5–2 years at Flair. Note-taker and detail owner on payments and chargebacks. (abigail.wigle@flyflair.com)

### Yuno
- **German Tatis** — Business Development Manager. Primary relationship owner.
- **Justo Benetti** — CRO. Joining the next technical call; leads airline deals.
- **Jarrett Falasco** — Sales Engineer. Joining the next call for technical depth.

---

## 2. CURRENT STACK

- **Three processors live:** Elavon (live Nov 2024), Nuvei (live Mar 2025), Braintree / PayPal (live May 2025). Plus FlexPay (BNPL). That is 4 integrations to maintain.
- **In-house orchestration layer:** Flair built its own orchestration in-house, with a basic set of smart-routing business rules driven by their contract terms with each processor and their cash / revenue strategy. Juliana: "relative to other airlines, we have the capability in house to build this layer." It works today. Do NOT pitch "you lack an orchestrator."
- **Retry / failover:** Exists ONLY inside Nuvei (e.g. a CVV decline is resent without CVV). There is NO cross-processor failover. If a processor declines, that revenue is lost. This is the concrete gap.
- **Reconciliation:** Manual. They download PDFs from each processor dashboard (Elavon, Nuvei, Braintree) and stitch them together by hand.
- **Markets:** Canada, US, Mexico.
- **Volume:** ~4,000 transactions/day upper bound, across all channels ("maybe less"). Average ticket ~$200 USD. Roughly ~120K trx/month.
- **Methods today:** Credit / debit cards only, plus FlexPay BNPL. No wallets, no local Mexican methods, no cross-processor routing beyond their basic rules.

---

## 3. WHAT THEY ARE LOOKING FOR (their mandate)

Juliana's stated payment mandates, all under the goal of executing a roadmap they cannot build fast enough in-house:
- Keep distribution and processing costs lower and smarter.
- Control and improve approval / authorization rates.
- Smarter, more agile business rules.
- Improve revenue integrity and reduce chargebacks.
- Strong interest in AI use cases in payments.
- They asked to see the portal / a live demo (ideally with another airline) and clear pricing / commercial terms.

The strategic framing (from Lucas): it is a **build vs. buy** decision internally. They like the product; the open question is whether buying Yuno beats continuing to build on their own in-house layer. **Cost is the sticking point.**

---

## 4. WHAT WE CAN SELL THEM (angles, mapped to their needs)

- **Cross-processor failover** — their single clearest gap. Yuno sits behind Elavon, Nuvei and Braintree and cascades a declined transaction to the next best processor. Recovers revenue that is lost today.
- **Smart routing + cost optimization** — route each transaction to the best-performing / lowest-cost processor, with dynamic % volume splits. The "Yuno effect": using volume shifts as live leverage to renegotiate Elavon / Nuvei / Braintree fees. Directly answers "lower and smarter processing cost."
- **NOVA (AI decline recovery)** — AI agent that calls / WhatsApps the customer on a decline, explains the reason, and sends a payment link to complete via another method. Airline proof: Wingo +14% approval; Qatar Airways on smart routing.
- **Payments Concierge (AI agent)** — lives in their stack, answers real-time payment questions via WhatsApp / Slack, builds dashboards, and can be given agentic authority to shift processors in real time. Speaks to their AI interest.
- **Unified reconciliation engine** — replaces the manual PDF-download-and-stitch process with one automatic dashboard across all processors. Direct hit on revenue integrity + ops load.
- **Local payment methods + wallets** — one API for OXXO, SPEI, Mercado Pago, 7-Eleven in Mexico, plus Apple Pay, Google Pay, Interac. Lifts approval and conversion in MX / new markets. Direct connections to Prosa and Cielo. No charge for extra integrations.
- **Monitors** — auto-failover: if a processor's approval drops below a set threshold, Yuno shifts traffic and alerts the team (email / push). 24/7 coverage.
- **Roadmap accelerator (the core sale)** — position Yuno as the way to ship their big payments roadmap without in-house engineering time. This is the answer to build vs. buy: buy the roadmap, get faster time-to-market, keep their existing processors. Not a rip-and-replace; a technology layer on top.

**Key objection to handle next call: PRICING.** Lucas: "We really like the product, but the cost is proving to be a challenge on our side. It becomes a build vs. buy situation and I'm trying to push us towards the buy." He asked for a call on fees or several fee-structure options. Bring flexible pricing options + a business case that shows the recovered revenue (failover + NOVA + approval uplift) outweighing the fee.

Pricing sent so far (Jun 18): $6,000/mo fixed software fee + $0.08 per approved transaction, $12,000/mo combined minimum. On-call range quoted: $10–12K/mo minimum; makes sense above ~100K trx/mo.

---

## 5. CALL SUMMARY (Discovery, Jul 3 2026, ~42 min)

- **Reconnection after ~2 years** (prior contact was with Juan Pablo, whom Juliana knows personally). Warm, informal open (World Cup). German had been prospecting Juliana for ~1 year.
- **Objective (Juliana):** learn where Yuno is now, since they are actively working through internal payment milestones and evaluating.
- **Stack confirmed:** three processors + their own in-house orchestration with basic routing rules; retries only inside Nuvei; manual reconciliation.
- **Yuno positioning (German):** infrastructure platform that started as an orchestrator; sits behind existing processors, not a replacement. Highlighted reconciliation engine, NOVA AI recovery, and Payments Concierge.
- **Live demo of the dashboard:** connections (1,200+ methods, 450+ providers, 50+ anti-fraud), routing / cascade rules, cross-processor fallback, dynamic % split routing ("Yuno effect" for fee leverage), Monitors auto-failover, checkout builder + SDKs, data / decline-flow tabs, and unified reconciliation. NOVA and Payments Concierge described (not in the demo account).
- **Mexico APMs discussed:** OXXO, SPEI, 7-Eleven, Mercado Pago; direct connections to Prosa and Cielo.
- **Pricing explained:** minimum fee ~$10–12K/mo = fixed SaaS + variable per approved transaction; only approved transactions are billed. Makes sense above ~100K trx/mo.
- **Flair shared volume:** ~4,000 trx/day (upper bound, across channels), ATV ~$200 USD.
- **Commitments (German):** short deck + a quote modeled on 4,000 trx/day @ $200. Both delivered Jun 18 (deck link + $6K / $0.08 / $12K minimum).
- **Post-call thread:** Lucas replied the cost is the main sticking point (build vs. buy) and asked to review fee options on a call. Next meeting set for **Tuesday, July 7, 3:30 PM EDT**, with Justo (CRO) and Jarrett (SE) joining for the technical + commercial deep dive. Business case in preparation.

### Next steps
- Bring **flexible pricing options** and a **business case** proving recovered revenue > fee.
- Technical + commercial call **Jul 7, 3:30 PM EDT** (German + Justo + Jarrett | Lucas + Juliana + Abigail).
- Open question still to confirm: do Flair Vacations payments run through Flair's Elavon stack or through HBX / Onlinetravel?
