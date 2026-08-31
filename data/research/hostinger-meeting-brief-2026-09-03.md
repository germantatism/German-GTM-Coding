# Meeting Brief: Yuno <> Hostinger

**Thursday, September 3, 2026 · 06:00 to 06:45 · 45 min**
**Meet:** https://meet.google.com/udy-vvio-vbm
**Event:** "Hostinger + Yuno" (organizer: German)

**Objective:** this is the RFP debrief and the Q4 gate. Winning means Paulius says the answers hold up, names what is still open, and agrees a concrete Q4 next step (technical deep dive, pilot scope or commercial conversation) rather than another "let's revisit."

### ⚠️ Pre-meeting actions
- **Justo has not responded to the invite** (status: needsAction). He has been on this account since Stripe Sessions. Confirm him.
- **⚠️ Verify the meeting time.** The calendar entry stores a **-05:00 offset** but labels the timezone **America/New_York**, which is UTC-4 in September. As stored, the call is 06:00 to 06:45 Bogota time, which is 14:00 in Vilnius. If it was actually set in Eastern time it would be an hour earlier for German. Confirm with Paulius in writing before Wednesday so nobody misses it.
- **Bring the three matrices the RFP deferred** (see section 3): PSP support for network transaction ID acceptance, PSP support for network token acceptance, and PSP support for wallet-token MITs, each scoped to Hostinger's actual provider mix. Five separate RFP answers say "available on request." Arriving with them is the single highest-leverage move available.
- **Get a real answer on data-warehouse connectors** (RFP 4.4) and on **routing version control / audit trail** (RFP 6.3). Both currently say "confirm with your Yuno account team," which is the weakest phrasing in the document, and Hostinger has a BI team.
- **No reply from Paulius since the answers were sent on August 6.** Twenty-five days of silence on the substance. Assume he has read them and is comparing against other orchestrators.
- **⚠️ There may be a second Head of Payments.** An external interview names a **Gediminas Griška** as Hostinger's Head of Payments (joined 2018, customer success → retention → payments), and Hostinger currently has an open "Head of Payments" job requisition posted. Paulius's own email signature is unambiguous ("Head of Payments | Hostinger Global"), so do not raise this as a question, but do not be surprised if payments decisions run through more than one person.

---

## 1. TL;DR Battle Card

**Five facts to know cold**

1. **This is a competitive RFP, and the file name says so.** Hostinger's questionnaire is titled *"Questions to orchestrators"*, plural. Yuno is one of several being evaluated in writing on the same 17 question groups. The comparison is happening on paper, side by side, which raises the cost of every "available on request" answer.
2. **This is also a re-engagement after a prior Yuno evaluation that did not convert.** German's own May 6 email: *"your experience with Yuno will be very different this time."* And on June 5: the questionnaire is *"the one you originally shared with Yuno previously."* Paulius has judged Yuno before. Never raise it defensively, but understand that credibility, not capability, is what is actually being tested.
3. **Paulius set the timing himself and it is Q4.** July 7, verbatim: *"We finalised our plans and capacity for Q3 and we don't have plans for new integrations, but as readiness for Q4 maybe we could revisit this somewhere in August or early September?"* This meeting exists because he scheduled the Q4 readiness conversation. That framing is the agenda.
4. **India is the market that opened the door.** German referenced Yuno's India coverage in two separate follow-ups as the thing discussed in San Francisco. It is the concrete geographic wedge into an otherwise global conversation.
5. **The RFP is roughly half about renewal authorization rates.** Four of the seventeen sections (network transaction ID, network tokenization, account updater, recurring engine) are all one question in different clothes: how do we stop losing subscription renewals. That is the deal.
6. **Hostinger has already tried this, twice, and both partners got absorbed by parties with a conflicting interest.** ✅ ProcessOut, an orchestration and payment-optimization layer, was Hostinger's own optimization partner per a public interview with their payments lead; ProcessOut was acquired by **Checkout.com** in February 2020 and is now a Checkout.com product. Separately, **Credorax**, a Hostinger acquirer announced in April 2021, rebranded to **Finaro** in December 2021 and was then acquired by **Shift4** for $575M in March 2022. An independent orchestration layer that gets bought by a PSP stops being independent. This is almost certainly why this RFP exists, and it is the strongest reason Yuno's independence is worth stating plainly, once, without naming either company as a competitor in the room.

**Three hooks, in priority order**

1. **Renewal authorization on a migrated vault.** Their questions on backfilling network transaction IDs and measuring what share of the token database carries one are migration-planning questions. Nobody asks those unless they intend to move. Yuno's answer here is genuinely strong: network transaction IDs import with card data during token migration, merchant-supplied values are accepted directly in the payment request, and the PCI proxy injects the stored ID natively with a documented placeholder.
2. **Enrollment below 100% never blocks a charge.** Their question 3.6 (*"Token enrollment is far from 100%, what logic do you use to decide which type of token to use?"*) is a trap laid for vendors who overclaim. Yuno's answer is the right one: per provider at payment time, network token plus cryptogram where accepted, vaulted card credential where not, so every vaulted card always has a processable credential. Say this plainly; it is a credibility win.
3. **Order-level approval rate.** Their question 4.3 shows a sophisticated team: retries drag down transaction-level auth rate and obscure true conversion. Yuno exposes `merchant_order_id` in the API and in reports, so order-level success is computable directly. Small feature, large signal that we understood the question.
4. **The size of a single declined renewal.** Hostinger's pricing runs long prepaid terms (a common intro-priced plan charges roughly $140 to $150 upfront, then renews around 3.5 to 4x that per-period price). A declined renewal on that model is not a small transaction, it is real revenue walking. ⚠️ Industry benchmarks (Recurly, 2026) put involuntary churn around 1.25% of recurring revenue and roughly 4% of renewal invoices failing outright; Visa and Mastercard both publish measured authorization lifts from tokenization in the mid-single digits of percentage points. Use these only as external validation, never as a claim about Hostinger's own numbers, which are 🔍 to ask for.

**THE objection they will raise:** *"Several of your answers say the detail is available on request. We are comparing written responses across orchestrators and we need the specifics."*

**The answer:** do not apologize for it, close it in the room. Five answers defer (PSP support for network transaction IDs, token database health, network token acceptance, wallet-token MITs, plus data-warehouse connectors and routing version control deferring to the account team). Every one of those is deliverable scoped to Hostinger's actual provider list, which is exactly why they were scoped rather than published as a generic list. Arrive with the matrices, hand them over, and the weakest column in the comparison becomes the most tailored one.

**The ask:** a named Q4 next step with a date. Best case, a technical deep dive with their engineers plus a migration-scoping conversation on the vault and the PayPal billing agreement book. Minimum, agreement on what still has to be proven and by when.

**Rapport opener:** he was out the last week of August and September 1, and picked this week himself back in July. A light *"welcome back, you picked the date so I hope the timing still works"* acknowledges he has been driving the calendar without making it about the delay.

---

## 2. Who Is in the Room

| Name | Role | Side | Status |
|---|---|---|---|
| Paulius Lapenas | Head of Payments, Hostinger Global | Hostinger | ✅ Accepted |
| German Tatis | BDM, organizer | Yuno | Accepted |
| Justo Benetti | CRO | Yuno | ⚠️ No response |

**Paulius Lapenas** (Lapėnas). ✅ **Head of Payments, Hostinger Global**, confirmed from his own email signature (used consistently April through July 2026) and independently from an aggregator profile as **Head of Payments, Hostinger International**, Vilnius. ⚠️ His LinkedIn profile could not be opened directly (blocked); background below comes from a single aggregator source (RocketReach), unverified against a second. Prior roles: **Western Union** and **Lindorff** (Nordic debt-collection and credit management, now part of Lowell), a card-payments-plus-recovery background rather than a pure engineering one. Education: MA in E-business Management, Mykolas Romeris University, 2014 to 2017. He is the RFP owner, the person who wrote or curated the questionnaire, and the one who controls both the roadmap slot and the calendar. He travels frequently and takes long breaks: out of office April 29 to May 4 (business trip), May 6 to 11, June 5 to 18, and again the last week of August through September 1.

**How to read him:** the questionnaire is the tell. He asks about the failure modes vendors hide (enrollment coverage below 100%, retries inflating decline rates, whether the token vault actually carries network transaction IDs), and he cites a specific Cybersource knowledge-base article on Apple Pay merchant-initiated transaction format. His collections background reads through the RFP too: several questions are really asking "how do we recover, not just avoid, a failed renewal." This is a practitioner who has run these systems and been oversold before. He will reward precision and specific limits, and he will notice hedging immediately. Answer narrowly and admit gaps; do not fill silence with capability language.

**Payments org structure at Hostinger (external interview, undated but corroborating):** payments sits inside the product organization, split into a technical team running integrations and infrastructure (internally called "hPayments") and a strategy team owning PSP relationships, negotiation and optimization, including five people dedicated to fraud, chargebacks and disputes. This is a real, staffed function, not a side responsibility.

**Relationship timeline**

| Date | What happened |
|---|---|
| Before 2026 | ⚠️ A prior Yuno engagement exists. Paulius had *"originally shared"* this questionnaire with Yuno previously, and German's May 6 note promises a different experience *"this time."* The outcome of that earlier evaluation is not documented in the thread |
| **Apr 29, 2026** | **Met in person at Stripe Sessions, San Francisco, Booth 214.** Calendar shows **Juan Pablo Ortega** (Yuno co-founder), German, Justo and Paulius all accepted. Deck shared: `ss26.yuno.tools/m/hostinger`. India discussed |
| May 6, May 20, Jun 5, Jun 25 | Four German follow-ups. Paulius out of office through most of it |
| **Jul 7, 2026** | Paulius replies: Q3 capacity is closed, no new integrations, proposes revisiting in August or early September as **Q4 readiness** |
| Jul 8, 2026 | Paulius sends the questionnaire, flags he is out the last week of August, asks for the first week of September. Meeting booked same day |
| Aug 3 to 5, 2026 | Yuno internal work on the responses (Samuel Vieira Tamayo drafting, internal review comments) |
| **Aug 6, 2026** | German returns the completed responses in two formats: the original file with every question answered, plus a document version with added context |
| Aug 6 to Sep 3 | **No reply.** Twenty-five days |
| Sep 3, 2026 | This call |

**Implication:** they have had the answers for nearly four weeks and have said nothing. That is not necessarily bad in a written RFP process, but it means the meeting opens cold on content he has already formed a view about. Ask what he thought before presenting anything.

**Other contacts:** none identified at Hostinger beyond Paulius. Yuno side: Juan Pablo Ortega (co-founder, met them at Stripe Sessions, a real escalation card if needed), Justo Benetti (CRO), Samuel Vieira Tamayo (solutions, wrote the RFP responses), Briana (cc'd on the original outreach).

---

## 3. RFP Summary: What Hostinger Asked and Where the Answers Land

Hostinger's questionnaire ("Questions to orchestrators", July 2026) runs **17 sections**. Yuno returned completed answers on August 6, 2026.

### 3.1 What the questions reveal about Hostinger

| Signal | Evidence in the RFP | Why it matters |
|---|---|---|
| **They intend to migrate an existing vault** | 2.3 asks for a backfill API for missing network transaction IDs; 2.4 asks how to check what share of the token database carries at least one | Nobody asks these unless they are planning to move card-on-file data. This is the commercial centre of the deal |
| **Renewal authorization is the core problem** | Sections 2, 3, 10 and 11 (network tx ID, network tokenization, account updater, recurring engine) are four of seventeen | Roughly half the document is one question: how do we lose fewer renewals |
| **They have been oversold before** | 3.6: *"Token enrollment is far from 100%, what logic do you use to decide which type of token to use?"* | A trap for vendors who claim universal coverage. Answer it honestly and score points |
| **They have a real analytics function** | 4.3 distinguishes transaction-level from order-level approval rate; 4.4 asks for data-warehouse export | They will validate claims against their own data, not our dashboard |
| **Meaningful US debit volume** | Section 8, three questions on pinless debit routing | Least-cost debit routing is a US-specific cost lever. Yuno's internal review noted this is US-PSP-only territory |
| **A PayPal billing agreement book exists** | 12.1 on reference transactions and billing agreement IDs | Migrating recurring PayPal without re-consenting customers is a genuine risk item for them |
| **They track scheme mandates closely** | 13.4 cites a specific Cybersource article on Apple Pay MPAN replacing device-token MITs | Current, technical, and not a question a generalist asks |
| **EU footprint with local rails** | 18.1 on co-badged card selection, Cartes Bancaires in France | Regulatory compliance (EU IFR 2015/751) is in scope |
| **They have been burned operationally** | 6.2 validation against user error; 6.3 routing version control; 7.1 whether webhook delivery is visible in the payment timeline | These are questions from someone who has lost a webhook or shipped a bad routing rule |

### 3.2 Where Yuno's answers are strongest (lead with these)

- **PCI proxy with native network transaction ID injection (9.3).** The `{{vaulted_token.<TOKEN>.network_transaction_id}}` placeholder exists precisely because processors require it for merchant-initiated transactions. Specific, documented, and directly on their pain.
- **Token-type selection logic (3.6).** Per provider at payment time: network token plus cryptogram where accepted, vaulted credential where not. Enrollment below 100% never blocks authorization.
- **Fallbacks and Monitors (5.1).** Automatic detection of approval-rate drops below a configurable threshold, traffic redirection, auto-recovery when the primary returns, and routing to the best-performing provider when all are degraded. Alerting to email and Opsgenie.
- **Routing condition breadth (5.2, 6.1).** Ten named condition types plus a free-form metadata field, configurable through both a visual dashboard and a full REST API.
- **Order-level aggregation (4.3).** `merchant_order_id` in the API and in reports, so retries of the same order roll up and true conversion separates from attempt-level noise.
- **Account updater mechanics (10.2).** Vaulted token and fingerprint stay stable across updates, so no integration change is required, with an `enrollment.update` webhook carrying the new details and a `card_data_history` array.
- **Co-badged cards (18.1).** Automatic per EU IFR Article 8, with named SDK minimum versions and the customer's network choice persisted to recurring payments.
- **Webhook reliability (7.1).** At-least-once delivery with seven attempts on a documented escalating schedule out to 96 hours, HMAC and OAuth2.

### 3.3 ⚠️ Where the answers are soft, and what to do about each

| RFP item | The soft spot | How to handle on the call |
|---|---|---|
| **2.1** PSP support for network tx ID | *"can be provided on request."* A list of 75 integration names is given, but not which of them accept a network transaction ID | Bring the matrix scoped to their provider mix |
| **2.3** Backfill | *"Bulk backfills outside a migration are handled with the Yuno team rather than a self-service endpoint"* | Frame as a one-time migration event with a named owner and timeline, not a recurring need |
| **2.4** Token database health | Analysis *"on request"* rather than a self-serve view | Offer a standing cadence tied to account reviews, and run it once during evaluation to prove it |
| **3.5** Network token acceptance by PSP | Capability matrix *"shared scoped to the merchant's provider mix"* | Same matrix, same delivery |
| **4.2** Subscription dashboard | They asked for one. The answer is that there is no subscription-only dashboard | Redirect to what is arguably better: billing-cycle fields (`billing_cycles_current`, `_next_at`, `_total`) plus `subscription_id` in reports, feeding their own BI |
| **4.4** Data warehouse export | ⚠️ **Weakest answer in the document.** No named connectors; *"should be confirmed with your Yuno account team"* | Get a real answer before Wednesday. They have a BI team and this will be compared |
| **6.3** Routing version control | *"For full audit trail and version history details, confirm with your Yuno account team"* | Also resolve before the call. Audit logs exist; get the specifics |
| **7.1** Webhook delivery logs | Direct no: per-payment webhook delivery logs are not surfaced in the payments screen | Answer honestly, then pivot to the seven-attempt retry schedule, which is strong |
| **8.1 to 8.3** Pinless debit | Acquirer capability, not a Yuno-side debit switch | This answer is correct and honest. Competitors may overclaim. Pre-empt by naming the US acquirers where it works |
| **10.1** Account updater schemes | **Visa and Mastercard only. No Amex** | A real gap if they carry meaningful Amex card-on-file volume. 🔍 Find out their Amex share |
| **10.3** Manual update trigger | No on-demand refresh, and scheme registration can take **up to 10 working days** for new customers | Timeline detail that matters for a Q4 go-live. Put it on the plan explicitly |
| **11.1** Recurring engine | **Subscriptions support cards only** | Clarify the boundary: PayPal recurring runs through billing agreements (section 12), it is just not inside the subscription object |
| **11.2** Retries | Capped at **5 in production** | If their dunning strategy uses more attempts, this is a constraint worth surfacing early rather than at contract |
| **13.3** Wallet-token MITs by PSP | *"validated per provider rather than published as a static list"* | The fourth deferred matrix. Same fix |
| **13.4** Apple Pay MPAN | *"MPAN rollout status is processor-dependent"* | He cited a specific article. Come with the current state for the processors he cares about, or commit to a date |
| **17.1** Backend SDKs | *"deliberately no required server-side SDKs"* | Framed as a feature, and defensible. Note that an internal draft claimed Kotlin/Java and Node SDKs existed and was corrected before sending. **Do not resurrect that claim** |

### 3.4 The pattern to name before he does

Six answers defer to the Yuno team or the account team rather than giving the specific (2.1, 2.4, 3.5, 4.4, 6.3, 13.3). Individually each is reasonable, since the honest answer genuinely depends on Hostinger's provider mix. Read together in a written comparison against other orchestrators, they read as one thing: **less specific on paper.** A competitor who publishes a static matrix scores higher in a spreadsheet even if the matrix is less accurate. Closing that gap in the room, with tailored documents in hand, converts the weakest column into the most tailored one, and it is the single highest-value thing German can do on Wednesday.

---

## 4. The Company

Hostinger is a Lithuania-headquartered web hosting, VPS, domains and website/app-builder company, bootstrapped with no VC funding. **Giedrius Zakaitis became CEO on June 16, 2026**, promoted from Chief Product & Technology Officer after 14 years at the company, with an explicit "AI-first" mandate. Prior CEO **Daugirdas Jankus** (Oct 2023 to Jun 2026) moved to strategic projects. **Arnas Stuopelis remains Chairman.** CFO is **Domantas Beržanskis**. ⚠️ The CPO seat appears vacant since Zakaitis moved up.

**Corporate structure:** contracting entities per the current Terms of Service include **Hostinger International Limited** (Larnaca, Cyprus, the primary EU and rest-of-world entity), **Hostinger PTE LTD** (Singapore), **Hostinger Global S.à r.l** (Luxembourg), **Hostinger UK Limited**, and **PT WEB MEDIA TECHNOLOGY INDONESIA**, plus two Lithuanian operating entities in Vilnius. Brand history: **Zyro** merged into the core product; **Niagahoster** (Indonesia) rebranded to Hostinger in June 2025; **000webhost** shut down in October 2024.

**Business model, and why it matters for this RFP:** headline plans are sold on long prepaid terms, commonly billed upfront for the full term and then **renewing at roughly 3.5 to 4x the introductory per-period price**. That gap is exactly why a declined renewal authorization is a large, not a marginal, revenue event, and it is the business logic underneath the RFP's heavy focus on network tokens, network transaction IDs and account updater.

**Recent product signal:** **AI Builder** launched August 18, 2026; Hostinger's own numbers show projects outside traditional website categories grew from under 4% to nearly 1 in 5 of all projects in twelve months, a fivefold shift toward customers who need to take payments themselves through what they build, which is a second, less obvious surface where payments infrastructure matters (Hostinger Horizons, their no-code app builder, already had 800,000-plus users at the end of 2025).

---

## 5. Financials

| FY | Revenue | Growth | Customers |
|---|---|---|---|
| 2022 | €69.6M | +64% | 1.5M |
| 2023 | €110.2M | +57% | 2.4M |
| 2024 | €182.4M | +65% | 3.5M |
| **2025** | **€275.4M** | **+51%** | **4.6M (+35%)** |

Source: Hostinger's own financial-results blog post, published Feb 23, 2026. That is a 58% revenue CAGR from 2022 to 2025 and four consecutive years of 50%+ growth. Hostinger states roughly €14M of opex saved through AI automation and ranked #2 on the FT/Statista Long-term Growth Champions Europe 2026 list.

**Deferred revenue is large by design.** FY2023 cash billings were €139.1M against €110.2M of recognized revenue, a direct consequence of the multi-year upfront billing model. Hostinger's first EBITDA-profitable year was 2023 (€2.4M). ⚠️ A Lithuanian company-registry figure (unverified against a primary filing) puts FY2025 net profit at roughly €38.4M, a 14% margin, on revenue close to the stated €275.4M.

**Ownership signals worth knowing, not raising:** Hostinger remains bootstrapped with no VC rounds; **ConHostinger GmbH (Equivia Partners)** took a roughly 31% minority stake in April 2021. An **€11.8M employee stock-option payout** landed March 18, 2026, and ⚠️ a November 2025 dividend recapitalization has been reported by a secondary source. Together these read as pre-liquidity-event grooming rather than distress. No IPO plans found. Headcount is roughly 900 as of 2023, with third-party estimates in the 1,150 to 1,340 range for 2026.

**So what for the call:** a company growing 50%+ a year on a long-prepaid, high-renewal-multiple model, with a real payments organization and a documented history of losing independent payment partners to acquisition, is a buyer whose Q4 timeline is credible and whose stated pain (renewal authorization, tokenization gaps, 3DS coverage in LatAm) maps directly onto what the RFP asked.

---

## 6. Payments Stack: External Evidence

Hostinger names no PSP publicly; its own privacy policy declines to identify "3rd party (payment processor) services" by name. What is verifiable:

- **Card statement descriptors** (from Hostinger's own support article on identifying charges): `HOSTINGER.COM`, `HOSTINGER*SERVICES`, `HOSTINGER.COM/LT`, `HOSTINGER INTERNATIONAL`, `DM.HOSTINGERCOMBR`, `EBN*HOSTINGER`. Six distinct descriptors point to multiple acquiring rails already in place. ⚠️ `EBN*` is EBANX's standard processor prefix, a strong but inferred signal of EBANX in Latin America; the `DM.` Brazil descriptor points to a second, unidentified Brazil rail.
- **dLocal:** a live, Japan-specific Hostinger payments page (`hostinger.jp/payments-dlocal`) suggests dLocal processes Hostinger's own Japanese transactions. ⚠️ Do not confuse this with **dLocal Go**, which is a separate, merchant-facing partnership Hostinger offers to *its own customers'* online stores, not Hostinger's own payment stack.
- **Prior acquirer, historical:** Credorax (2021, see section 1), now inside Shift4 via Finaro. ⚠️ Current status of that relationship not found.
- **Fraud and identity:** **Ravelin** is named in the privacy policy as a fraud-prevention provider; **iDenfy** for identity/biometric verification. No Riskified, Signifyd, Forter or Sift found.
- **Vaulting:** described as "PCI-DSS Level 1" with cards stored outside Hostinger's own systems.
- **Payment methods by market** (from Hostinger's own support pages): Brazil, Pix, Boleto, Nubank, up to 12-month installments; Mexico, OXXO, SPEI, 3 to 12 months; Colombia, up to 36-month installments; Argentina, 12 months; India, UPI; Indonesia, QRIS, OVO, DANA and major bank virtual accounts; Nigeria, OPay; Egypt, Fawry; Pakistan, JazzCash; Poland, Blik; Germany, Klarna; France, Carte Bancaire; Lithuania, Paysera; UK, Amazon Pay; Hong Kong, UnionPay, Alipay; plus PayPal, Apple Pay, Google Pay and crypto broadly. Twenty-plus local payment methods across 150-plus countries.
- **Stated pain, in Hostinger's own words** (from the public interview with their payments lead): *"Lack of 3DS coverage in Latin America makes fighting chargebacks challenging."* And on tokenization gaps: some methods *"are not possible to tokenize, such as cash payments... it can affect recurring revenue."*
- **ARPU is unusually low for the category:** roughly €60 per customer per year (2025 revenue divided by customers), against GoDaddy at roughly $242 and IONOS at roughly €199. High-volume, low-ticket, globally distributed, heavily recurring: a small shift in decline rate moves real revenue at this scale.

---

## 7. Competitive Landscape

Hostinger competes across mass-market hosting, website builders and adjacent no-code/ecommerce tools. Share basis varies by source and is labeled; W3Techs measures the share of surveyed websites detected running each platform, not revenue.

| Competitor | Segment | Est. share (source + basis) | Scale proxy (dated) | Payments posture |
|---|---|---|---|---|
| Shopify | Ecommerce (adjacent) | 5.3% (W3Techs, sites detected) | $11.56B FY25 revenue, $378.4B GMV | Shopify Payments / Shop Pay, own acquiring |
| **Hostinger** | Mass-market hosting | **5.1%, #2** (W3Techs, sites) | €275.4M FY25 revenue, 4.6M customers | Multi-PSP, no named orchestrator |
| Wix | SMB website builder | 4.2% (W3Techs, sites) | $1.99B FY25 revenue (+13%) | Routes Adyen, Stripe and PayPal by region |
| IONOS | EU hosting (United Internet) | 2.6% (W3Techs, sites) | €1,316.9M FY25 revenue, 6.63M customers | Not found |
| GoDaddy | Domains + SMB | 2.5% (W3Techs, sites) | $4,951M FY25 revenue, 20.42M customers (-0.4%) | Own acquiring, GoDaddy Payments |
| Squarespace | Website builder | 2.5% (W3Techs, sites) | $1.01B FY23 revenue; taken private by Permira, $7.2B, 2024 | Squarespace Payments, a Stripe white label |
| Newfold Digital (Bluehost, HostGator) | Hosting roll-up | 2.4% (W3Techs, sites) | ⚠️ ~$1.4B, -1.2% (2024); Moody's rates it Caa1 | Not found |
| OVHcloud | EU cloud/IaaS | 2.4% (W3Techs, sites) | €1,084.6M FY25 revenue (+9.3%) | Not found |
| team.blue | EU hosting roll-up | 2.2% (W3Techs, sites) | €866M ARR FY25, 3.3M customers | Not found |
| Hetzner | EU low-cost hosting | 2.2% (W3Techs, sites) | No estimate available | Not found |
| SiteGround | Premium shared hosting | 2.0% (W3Techs, sites) | ⚠️ ~$94.7M 2025 (estimate) | Not found |
| DigitalOcean (+ Cloudways) | Cloud IaaS | 1.5% (W3Techs, sites) | $901M FY25 revenue (+15%) | Not found |
| Namecheap | Registrar + hosting | No estimate available | 22M+ domains; CVC took a stake at ~$1.5B, Sep 2025 | Not found |
| Automattic / WordPress.com | Managed WordPress | No estimate available | ⚠️ ~$710M 2024 (estimate) | WooPayments, ⚠️ unconfirmed |
| WP Engine | Managed WordPress | No estimate available | $132M ARR (2019, last disclosed) | Not found |

**Where Hostinger sits:** it is the #2 most-detected hosting platform by installed-site share, growing revenue faster than every large peer above with a disclosed growth rate, at roughly a quarter of GoDaddy's or IONOS's per-customer revenue. None of the named peers has a disclosed orchestration or PSP-independence story; several (GoDaddy, Squarespace via Stripe) have gone the opposite direction, toward a single deeply integrated processor. **For the call:** this is context, not a talking point. Hostinger's scale and growth rate make the renewal-authorization problem larger every quarter, which is useful for urgency, but never frame it as "you are behind your peers."

---

## 8. News & Signals

| Date | Item |
|---|---|
| 2026-08-31 | Product update: new Ecommerce headless WordPress plugin with payments, Reach API, AI Builder rollback support |
| 2026-08-18 | **AI Builder launched.** Non-website project types grew from under 4% to nearly 20% of projects in 12 months |
| 2026-07-09 | Stripe Express Checkout added to Quick Link stores (a feature Hostinger offers its own customers, not Hostinger's own payment stack) |
| 2026-06-16 | CEO transition: Giedrius Zakaitis succeeds Daugirdas Jankus |
| 2026-03-18 | €11.8M employee stock-option payout |
| 2026-02-23 | FY2025 financial results published |

No news found in the last 7 days beyond the August 31 product update.

---

## 9. Be Ready For

| They ask | You answer |
|---|---|
| "Why should we believe this evaluation goes differently than last time?" | Do not relitigate history. The answer is what has actually changed: the platform surface they are asking about (network tokens, account updater, subscriptions, PCI proxy, Monitors) is documented feature by feature, and the specifics they asked for are in hand today rather than promised. Then hand over the matrices. |
| "Which of our PSPs actually accept a network transaction ID and a network token?" | The matrices, scoped to their list. If a provider is missing from the matrix, say so rather than generalizing. |
| "What happens to our PayPal billing agreements if we move?" | Billing agreement IDs are scoped to the PayPal merchant account (payee), so they stay valid as long as Hostinger retains the same PayPal merchant account. Yuno has migrated existing billing agreement portfolios for large recurring merchants, and zero-value verification validates vaulted agreements without charging. Flow design happens with the solution team. |
| "How long does a vault migration actually take?" | Card data and network transaction IDs import together as part of the token migration process. Account updater scheme registration is a separate track and takes up to 10 working days for new customers. Sequence both explicitly against a Q4 date. |
| "Do you have a subscription dashboard?" | Not a dedicated one, and here is what exists instead: Insights segmentation over recurring traffic, subscription and billing-cycle fields in transaction reports for their own BI, and real-time lifecycle webhooks. Given their question 4.3, their BI path is likely better for them than a canned dashboard anyway. |
| "Can we do least-cost debit routing in the US?" | Yuno segments debit traffic by card type, BIN and issuer country and steers it to connections where the acquirer has pinless enabled. The debit-network connection itself sits with the acquirer. Yuno will validate this against their US acquirer shortlist. |
| "What does this cost?" | Platform fee plus a fee per successful transaction. Actual numbers need volume. Do not improvise a number; Justo owns pricing. |

**Landmines**
- Never tell Hostinger they "lack" orchestration or that their current stack is behind. Paulius built it.
- Do not overclaim on the deferred matrices. If a provider's support is unknown, say unknown. He designed question 3.6 specifically to catch overclaiming.
- Do not claim server-side SDKs in Kotlin, Java or Node. The shipped answer says there are deliberately none.
- Do not present pinless debit as a Yuno capability. It is an acquirer capability that Yuno routes into.
- Do not bring up the prior Yuno evaluation unless he does.
- Do not name other orchestrators in the RFP or speculate about who else is bidding.
- Do not name ProcessOut or Credorax/Finaro by name as a talking point. If Paulius raises his own history with an orchestration or acquiring partner that was later acquired, that is the moment to make the independence point, once, plainly, and move on.

---

## 10. Agenda (45 minutes)

| Min | Block | Notes |
|---|---|---|
| 0 to 5 | Warm open. Ask directly what he thought of the responses and which sections raised questions. Listen first, do not present | Notes: ____ |
| 5 to 20 | Work his list. Whatever he flags, answer narrowly. Hand over the network tx ID, network token and wallet MIT matrices scoped to his providers | Notes: ____ |
| 20 to 30 | The migration conversation: existing vault, network transaction ID coverage, PayPal billing agreement book, account updater registration lead time | Notes: ____ |
| 30 to 38 | Q4 readiness. What has to be proven, by whom, by when. India as the concrete first scope if it is still live | Notes: ____ |
| 38 to 45 | Next step with a date and an owner. Confirm who else on his side joins a technical session | Notes: ____ |

---

## 11. Discovery Questions

1. You have had the responses for a few weeks. Which sections did you push back on, and where did we come up short against what you needed? **Notes: ____**
2. Your questions on backfilling network transaction IDs and token database health read like migration planning. Is moving the vault actually on the table for Q4, or is this about pressure-testing the incumbent? **Notes: ____**
3. What share of your card-on-file base currently carries a network transaction ID, and do you know your network token enrollment coverage today? **Notes: ____**
4. On account updater, we cover Visa and Mastercard. How much Amex card-on-file volume do you carry? **Notes: ____**
5. Your retry strategy today: how many attempts, and over what window? We cap at five in production and I would rather know now if that is a constraint. **Notes: ____**
6. How large is the PayPal billing agreement book, and is retaining the same PayPal merchant account an option? **Notes: ____**
7. Pinless debit came up in three questions. How much US debit volume are we talking about, and which acquirers are you on there? **Notes: ____**
8. When we met in San Francisco, India was the market you raised. Is that still the sharpest problem, or has the priority moved? **Notes: ____**
9. You mentioned publicly that 3DS coverage gaps in Latin America make chargebacks hard to fight. Is that still the sharpest regional pain, or has something else overtaken it? **Notes: ____**
10. What does Q4 readiness actually mean on your side: a decision, an integration slot, or a pilot? And who else needs to be convinced? **Notes: ____**

---

## 12. Post-Meeting Checklist

- Same-day recap listing every open item he raised, with an owner and a date against each.
- Deliver any matrix or answer promised in the room within 48 hours; this account is being judged on precision.
- If migration is real, get the solution team scoping the vault and PayPal billing agreement portfolio immediately.
- Update memory: RFP outcome, whether Q4 is a decision or a slot, Amex share, US debit volume, retry strategy, India status, clarity on whether Griška or Lapenas or both own the decision.

---

### Sources
Google Calendar (event "Hostinger + Yuno", Sep 3, 2026; prior events Apr 29, 2026 Stripe Sessions Booth 214, and internal RFP work blocks Jul 29 and Aug 5, 2026) · Gmail thread "Hostinger + Yuno at Stripe Sessions" (Apr 29 to Aug 6, 2026), including Paulius Lapenas replies of Jul 7 and Jul 8, 2026 and his out-of-office signatures (Apr 29, May 6, Jun 5, 2026) · Hostinger questionnaire "Questions to orchestrators - Hostinger July 2026" (Google Sheet, 17 question groups) · Yuno response document "Payment Infrastructure: Answers to Questions to Orchestrators, Hostinger, August 2026" · Google Docs comment notifications on the questionnaire, Aug 3, 2026 (internal Yuno review by Samuel Vieira Tamayo) · Yuno public documentation at docs.y.uno as cited throughout the RFP responses · RocketReach (Paulius Lapenas profile summary) · public interview with Hostinger's payments lead (ProcessOut blog) · Hostinger financial-results blog posts (Feb 23, 2026 and May 30, 2024) · Hostinger Terms of Service and privacy policy (updated Jul 15 and Jul 10, 2026) · Hostinger support articles on payment-method availability and charge identification · BusinessWire (Credorax, Apr 13, 2021) and TechCrunch (ProcessOut acquisition, Feb 25, 2020) · Hostinger blog (CEO transition, AI Builder launch, product updates) · W3Techs market-share survey (accessed Aug 31, 2026) and public filings/press for GoDaddy, IONOS, Squarespace, Wix, Shopify, Newfold Digital, OVHcloud, team.blue, DigitalOcean, Namecheap.
