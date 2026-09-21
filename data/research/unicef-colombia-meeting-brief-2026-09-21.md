# Meeting Brief: Yuno <> UNICEF Colombia

**Meeting:** Monday 21 September 2026, 4:00 to 4:30pm COT (GMT-5) · [Google Meet](https://meet.google.com/zre-rmwt-ujn) · phone (CO) +57 601 8957242, PIN 189183075
**Event:** "Fondo de las Naciones Unidas para la Infancia UNICEF Colombia & Yuno", booked through Chili Piper, created 8 September 2026 by Susana Awad
**Objective:** this is a 30 minute inbound first call. Winning it means leaving with two things: a number for their current collection rate on recurring donations, and a booked technical follow-up with their database owner. Not a closed deal, not a proposal.
**Evidence labels:** ✅ verified · ⚠️ inference or unconfirmed, never state as fact in the call · 🔍 ask in discovery

---

## ⚠️ PRE-MEETING ACTIONS

1. **German is marked optional on the invite.** Susana Awad organised it and Alejandro Albarracín is on it. Agree in the first minute who runs discovery and who runs the demo, so the 30 minutes are not spent handing off.
2. **One attendee's role is unknown.** Leidy Guio Castellanos returns nothing in public sources. Open with a roles round rather than guessing.
3. **One attendee identity is unconfirmed.** The Sebastian Garavito profile found is a probable match, not a proven one. Do not reference his background out loud until he describes it himself.
4. **LinkedIn blocked automated access.** Open these manually if there is time: [Idual Kerguelen Montaño](https://co.linkedin.com/in/idual-kerguelen-monta%C3%B1o-87561433) and search LinkedIn for "Sebastián Garavito Rodríguez UNICEF" and "Leidy Guio UNICEF".
5. **No prior contact exists.** Calendar history, Gmail and Slack are all empty except the invite itself. Treat this as a true first meeting and do not imply any prior relationship.
6. **Their public tender closes in 7 days (28 September).** If the goal is to influence anything in that process, timing is now, not next month.

---

## 1. TL;DR BATTLE CARD

### Five facts to know cold

1. **They came to Yuno.** Inbound booking via Chili Piper on 8 September. No prior emails, no prior calls, no Gong history. Something triggered this, and finding out what is the single most valuable thing in the first ten minutes. 🔍
2. **They are running a live tender to fix exactly the problem Yuno solves.** RFP2026-10 (proposals due 28 September 2026, 3 year agreement) asks a telemarketing vendor to "Reactivar el cobro de 90.000 donantes individuales recurrentes", recovering failed donations "mediante la actualización de datos de medio de pago". One of its KPIs is "Tasa de Cobrabilidad". ✅
3. **Their stack already has a vault and more than one processor wired in.** The donation site allowlists Firstoken (card vault, and Firstoken publishes a UNICEF Colombia client logo), Mercado Pago, Wompi and Nuvei, plus Sift for fraud. Face to face and telemarketing sign-ups run on Evergiving (Waysact). Salesforce is the CRM. No orchestrator found. ✅ for the allowlist, ⚠️ for which processors are actually live.
4. **All monthly donations are charged in one automatic run on the first day of the month.** Advisors in the street capture card details without CVV. ✅
5. **Scale and cost.** UNICEF received $16.56M from Colombia private sector fundraising in 2024, ranking 7th of 72 country offices and 4th in LatAm. They publish their own transaction cost: "Una transacción con tarjeta de crédito nos cuesta en promedio $700, mientras que un débito nos cuesta en promedio $1.400" (COP). ✅

### Three hooks, in priority order

1. **Recover failed recurring charges before a human has to phone the donor.** Their tender budgets three years of outbound calls to update payment details for 90,000 donors. Retries, network tokens that follow a reissued card, and failover to a second processor handle a portion of that in the payment layer. Yuno's published figure is 30% recovered revenue.
2. **Decide where each charge goes.** They already have more than one processor connected. Smart routing is a 7% approval uplift in Yuno's published numbers, and it costs them nothing to keep every processor they have.
3. **See collection rate in one place.** Their own tender tracks share of donors paying by card versus savings and checking account, and share who changed payment method. That is a routing and reporting question as much as a telemarketing one.

### THE objection they will raise

**"We already have a vault and processors, and we just tendered the recovery work. Why add another layer, and what does it cost us per transaction?"**

Answer: Yuno does not replace Firstoken, Mercado Pago, Wompi or the telemarketing agency. It sits above them and decides, per charge, where it goes and what happens when it fails. The call center still gets the donors who genuinely need a conversation, just fewer of them. On cost, they have published that a card transaction costs them COP 700 and an account debit COP 1,400, so the honest framing is recovered donations per peso of fee, not fee alone. 🔍 Ask what their all-in cost per successful collection is before quoting anything.

### The ask (next step to land)

A 45 minute technical session with whoever owns the donor database and the recurring charge files, plus a data pull: **collection rate on the first-of-month run, split by payment method, and the failure reasons behind it.** Without that number nothing can be sized.

### Rapport opener

Their first ever benefit gala (17 April 2026, Country Club de Bogotá) raised approximately USD 140,000 for children affected by the Córdoba floods, earmarked mainly for getting children back to school. It is recent, positive, and it is theirs. Their monthly donor programme has run since 2001, which is a long run worth acknowledging.

**If you want something from this week:** on 17 September 2026 UNICEF Colombia published "Invertir en la niñez es invertir en el desarrollo del país", asking Colombia to prioritise children in the National Development Plan debate. Four days old.

---

## 2. WHO IS IN THE ROOM

### Attendee table

| Name | Role | Side | Status |
|---|---|---|---|
| Sebastian Garavito Rodriguez (sgaravito@unicef.org) | ⚠️ probably fundraising / individual giving | UNICEF Colombia | Accepted |
| Leidy Guio Castellanos (lguio@unicef.org) | ⚠️ unknown, ask | UNICEF Colombia | Accepted |
| Idual Kerguelen Montaño (ikerguelen@unicef.org) | Database Officer | UNICEF Colombia | Accepted |
| Susana Awad (susana.awad@y.uno) | Organiser, booked the meeting | Yuno | Accepted |
| Alejandro Albarracín (alejandro@y.uno) | Added German to the invite today | Yuno | Accepted |
| German Tatis (german.tatis@y.uno) | Senior AE | Yuno | Accepted, marked optional |

### Profiles

**Idual Kerguelen Montaño, Database Officer** ✅ title, from his LinkedIn headline
A systems engineer (Universidad Popular del Cesar) with project management studies at Universidad del Rosario, previously a software QA analyst at Choucair Testing. Snippet level only; LinkedIn blocked direct access.

**The single most useful find in this research** is UNICEF's own published job description for the Database Officer post in Bogotá (NO-1, post 121164). It states the role **reports to the "Individual Specialist" inside the Private Fundraising and Partnerships team at the Colombia country office**, so this is a fundraising role, not general IT. Duties quoted: "Maintenance of the donor and supporter database"; manages "a team of assistants, working closely with Fundraisers, ICTD, and Third party vendors / agencies"; "Testing, modifying and implementing improvements to database"; "Data analysis, dashboard generation and monitoring plans". Requirement: "Minimum of three years managing CRM database in a fundraising environment. Salesforce is required". ⚠️ It is not confirmed that Idual was the person hired for that specific post.

*How to read him:* the technical evaluator and, on this call, the person who can actually answer the questions that matter. He owns the donor database, works directly with third-party agencies, and speaks Salesforce. He will care about integration effort, data flows into the CRM, what happens to existing tokens, and the format of the recurring charge file. Ask him directly what that file looks like today. No payments or banking background was found for him.

**Sebastian Garavito Rodriguez** ⚠️ identity match unconfirmed
A ZoomInfo profile for "Sebastian Garavito" lists UNICEF roles of Fundraising Associate and Marketing Assistant, covering donor acquisition campaigns and acting as Scrum Master on Salesforce projects, with earlier roles at Acción contra el Hambre (Fundraising Manager, implemented Salesforce for individual donors) and Aldeas Infantiles SOS Colombia, rising to Coordinador de Recaudo. Education: Magíster en Administración, Universidad Nacional. The same profile lists his current employer as elsewhere, which conflicts with a live @unicef.org address, and the rendered name varied between searches.
*How to read him:* if the match holds, he is the commercial counterpart and the person who feels declined recurring charges most directly, given a collections background. Let him describe his own role.

**Leidy Guio Castellanos** ⚠️ nothing found
No public source ties this name to UNICEF. Two similarly named people exist in unrelated organisations and should not be assumed to be her.
*How to read her:* unknown. ⚠️ One plausible reading, not confirmed: the Database Officer job description says the role "manages a team of assistants", so a low public footprint would fit a donor-database or donor-services analyst on Idual's team. Do not assume it. The roles round settles it.

### Sponsor and intro path

There is none. This is inbound: they found Yuno and booked through the website. ⚠️ No internal champion has been identified yet, which means the first call has to create one.

### Relationship timeline

| Date | Event |
|---|---|
| 8 September 2026 | Susana Awad creates the meeting after an inbound Chili Piper booking |
| 21 September 2026 | Alejandro Albarracín adds German to the invite; all three UNICEF attendees accept |
| 21 September 2026, 4:00pm | This call |

**Implication:** nothing has been sent, nothing has been promised, and no expectations have been set. Every framing decision in this call is the first one. That is an advantage: there is no bad prior pitch to undo.

### Other known contacts in the account

| Name | Role | Source |
|---|---|---|
| ⚠️ The "Individual Specialist" | Idual's direct manager per the published job description, sits between these attendees and the fundraising lead. Name not found. **Most likely economic influencer not on this call** | UNICEF job description, post 121164 |
| Gustavo Ugalde | Gerente de Movilización de Recursos, UNICEF Colombia (fundraising lead) | UNICEF press release, 31 March 2026 |
| Tanya Chapuisat | Representante de UNICEF en Colombia | Same release, not reconfirmed since |
| Mario Valderrama | Private Fundraising and Partnerships Officer, corporate alliances | UNICEF Colombia alliances page |

⚠️ None of them is on this call. Finding out whether Gustavo Ugalde owns this decision is a discovery objective.

---

## 3. THE COMPANY

UNICEF Colombia is the country office of the United Nations Children's Fund in Bogotá. It is a UN agency office, not a local foundation or NGO, and it raises money from Colombian individuals to fund its programmes. Donors are acquired three ways: face to face street and venue fundraising, telemarketing, and digital, with a direct response TV component visible in the donation form's own naming.

### Key metrics

| Metric | Value | Source |
|---|---|---|
| Legal entity | UNICEF Oficina para Colombia, NIT 800.176.994-3, Calle 72 #10-71 piso 11, Bogotá | Privacy notice |
| Contributions received 2024 | $16.56M, rank 7 of 72 country offices, 4th in LatAm | UNICEF Funding Compendium 2024 |
| Monthly donor programme running since | 2001 | RFP2026-10 terms of reference |
| Active donors | ⚠️ "over 130,000" and "average monthly collection of USD 1.5 million", from an expired vacancy snippet that could not be opened. Do not cite. 🔍 Ask instead | UNICEF vacancy post 136578 |
| Suggested monthly gift | COP 50,000 and 80,000 (80,000 preselected); tender minimum COP 40,000 | Donation page, tender |
| Published cost per transaction | Card COP 700, account debit COP 1,400 | UNICEF Colombia fundraisers page |
| Billing cycle | One automatic run, first day of each month | Refund policy |
| Website traffic | ~121K visits in August 2026, 88.8% from Colombia | Semrush |

### Corporate structure

| Entity | Relationship | Payments implication |
|---|---|---|
| UNICEF Oficina para Colombia | UN agency country office, data controller for donor data, privileges and immunities preserved in its policies | Contracts through UN procurement, not standard commercial terms |
| UNICEF Private Fundraising and Partnerships (PFP), Geneva moving to Rome | Global division that funds and steers country office fundraising | ⚠️ May hold veto or guidelines over stack choices. 🔍 Ask whether payment decisions are local |
| 32 National Committees (UNICEF USA, UK, Spain, Germany and others) | Independent local NGOs, not country offices | Each runs its own stack. UNICEF USA uses Fundraise Up on Stripe, Germany uses FundraisingBox, Australia shows Stripe. Colombia's choice is Colombia's |
| Other LatAm country offices (Brazil, Chile, Mexico, Uruguay, Argentina) | Peer offices with their own fundraising | The natural expansion path if Colombia works |

### Strategy themes

- **Income under pressure globally.** UNICEF published that it projects "at least a 20 per cent decline in income from 2026", with restructuring targeting around $586M in savings and relocation of 70% of staff to lower cost locations.
- **Less central investment, same ambition.** The 2026 fundraising division plan sets a $1,957M private sector target while cutting its own budget from $287M to $230M and country office expenditure by $15M.
- **Acquisition push regardless.** The two open tenders together target 48,500 new recurring donors over three years.

---

## 4. FINANCIALS

UNICEF is a UN agency, so there is no revenue, margin or equity story. The equivalent financial picture is contributions received, and the split between public sector (governments) and private sector (individuals, corporates, foundations), because private money is the flexible money.

### Income trajectory, ten years

Two official series exist and they differ slightly: the Funding Compendium reports "private sector income", the fundraising division's report to the Executive Board reports private sector revenue and runs a few million higher. Both are correct. Do not mix them in one chart without a footnote.

| Year | Total income (USD) | Private sector income (USD) | Source |
|---|---|---|---|
| 2016 | $4.9B | Not verified | Compendium 2016 |
| 2017 | $6,029M | Not verified, two conflicting published figures | Annual Report 2017 |
| 2018 | $6,060M | ⚠️ $1,461M, from a search snippet, not read directly | Compendium 2018 and 2019 |
| 2019 | $6,400M | $1,457M (23%) | Funding Compendium 2019 |
| 2020 | $7,219M | $1,606M (22%) | Funding Compendium 2020 |
| 2021 | $8,122M | $2,077M (26%) | Funding Compendium 2021 |
| 2022 | **$9,326M, the decade peak** | **$2,665M, the private peak** (29%) | Funding Compendium 2022 |
| 2023 | $8,920M | $2,068M (23%) | Funding Compendium 2023 |
| 2024 | $8,263M, down 7% | $1,847M (22%), down 11% | Funding Compendium 2024 |
| 2025 | $8,084M, down 2% | $2,209M (27%) | Funding Compendium 2025 |
| 2026 | Plan, see below | $1,957M target | PFP 2026 workplan |

Shape of the curve: total income rose to a $9.3B peak in 2022, then fell three years running to $8.1B. Private income peaked at $2.67B in 2022, bottomed at $1.85B in 2024, and recovered to $2.21B in 2025.

### The number that frames this entire call

At the Executive Board session on 1 to 4 September 2026, three weeks ago, Executive Director Catherine Russell stated that **UNICEF projects total income of $26 billion for 2026 to 2029, a 27% decline against the previous period**, described as the most dramatic financial contraction in decades, and representing a **$6.6 billion reduction** in funds reaching country programmes. ✅

### Recent trend

- **2025's private sector growth is not repeatable.** The 19.7% rise leans on a single donation of up to $500M. Underlying, the trend is flat to down.
- **2026 plans below what 2025 delivered:** a $1,957M target against a $2,215M result.
- **The fundraising engine is itself being cut:** division budget from $287M to $230M, investment funds down $20M, country office expenditure down $15M, 80 posts cut, over 90% of staff relocating from Geneva to Rome.
- **The humanitarian appeal shrank:** the 2026 Humanitarian Action for Children appeal is $7.66B, down sharply from $10.2B requested for 2025.
- **Individual donors are the flexible core:** "90% of private sector regular resources came from individual supporters", from over 10 million individual supporters worldwide.

### Colombia specifically

- $16.56M contributions received in 2024, 7th of 72 country offices, 4th in LatAm.
- ⚠️ No audited local income figure, donor count or average gift is published. The "130,000 donors, USD 1.5M monthly" figure is an unverified snippet from an expired job ad. 🔍 Ask.

### So what for the call

A 27% income contraction over four years, with the fundraising division's own budget cut at the same time, makes yield on the existing donor base the cheapest available source of funding. Every pledged donation that fails to collect is money already won and then lost. It also means a proposal requiring significant upfront investment is a harder sell than one framed around recovering money they have already been promised. Lead with recovery, not with transformation.

---

## 5. COMPETITIVE LANDSCAPE

UNICEF Colombia competes for the same Colombian household's monthly gift as every other international NGO running street fundraising in the country. "Market share" in this field is not published the way it is in commerce, so most rows carry a scale proxy instead of a percentage. **No percentage below is guessed.**

| Organisation | Segment | Share of individual giving in Colombia | Scale proxy (verified) | Differentiator | Payments posture |
|---|---|---|---|---|---|
| UNICEF Colombia | UN agency, child focus | No estimate available | USD 16.56M contributions received, 2024; 7th of 72 country offices | UN brand, monthly donor programme since 2001, face to face in 31 cities | Firstoken vault, Mercado Pago signal, Wompi and Nuvei allowlisted, Evergiving for face to face ✅ code level |
| Fundación Plan (Plan International Colombia) | INGO, child focus | No estimate available | **COP 50,533,868,000 total gross income, FY2024**, the largest verified local income in this set. Note most of it is international transfers, not local individual giving | Long established local foundation structure | Face to face capture of card without CVV or bank account; gateway not visible |
| Teletón Colombia | National telethon | No estimate available | COP 13,062,930,883 raised in one 28 hour event (2015 press figure) ⚠️ ten years old | Annual televised campaign, mass reach, event driven rather than monthly | PayU ally logo plus a Mercado Pago canonical domain, two providers visible ✅ |
| TECHO Colombia | INGO, housing | No estimate available | COP 6,359,718,939 total operating income, FY2024 | Youth volunteer model | Not checked |
| Save the Children Colombia | INGO, child focus | No estimate available | "más de 420,000 personas" reached in 2024 (income not extractable, image PDF) | Closest direct substitute for a child focused donor | **Wompi confirmed** in form config, with Nequi, Daviplata and PSE referenced ✅ |
| Aldeas Infantiles SOS Colombia | INGO, child focus | No estimate available | Audited financial statements published (FY2023); income line not extracted | **Sponsorship "padrinos" monthly model, the closest analogue to UNICEF's** | Donation microsite; gateway not visible |
| Cruz Roja Colombiana | National humanitarian | No estimate available | Financial statements published per seccional, so a single national individual giving figure may not exist | National institution, emergency recall | Afrus third-party donation widget ✅ |
| World Vision Colombia | INGO, child sponsorship | No estimate available | No Colombia entity filing found, only global consolidated statements | Sponsorship model, donor bonds to a named child | Mercado Pago SDK loaded on the sponsorship portal ✅ |
| Médicos Sin Fronteras (MSF LAT) | INGO, humanitarian medical | No estimate available | MSF globally: over EUR 2B income 2024, 98% private, 7M+ individual donors | Independence story, 98% private funding | PSE and Nequi referenced, Salesforce referenced; gateway not visible |
| Greenpeace Colombia (Greenpeace Andino) | INGO, environment | No estimate available | 3M+ supporters worldwide | Monthly only model, no one-time option visible | Monthly automatic card debit; gateway not visible |
| WWF Colombia | INGO, environment | No estimate available | 5M+ supporters globally | Conservation brand | Live donation site; gateway not visible |
| UNHCR / ACNUR | UN agency, refugees | No estimate available | Globally $697M private in 2025, $386M from 3.2M individual donors | Closest institutional peer, also a UN agency | ⚠️ Not verified as an individual donor fundraiser in Colombia |

**Caveat on method, and it matters:** **no defensible market share table exists for this field.** No credible published total for individual or private giving in Colombia was found. Two candidates were examined and both rejected: an AFE Colombia foundations figure measures corporate and family foundation spending, which is a different pool, and an APC Colombia figure measures inbound international philanthropy. With no market total, no share can be derived, so every share cell reads "no estimate available" and carries a verified scale proxy instead. Web technology install databases (6sense, Datanyze) measure website tech installs, not revenue or donors, and nothing above comes from them. **If anyone in the room quotes a market share percentage today, it is not sourced.**

### Where UNICEF Colombia sits

Only three organisations in this field publish a hard income figure, and UNICEF Colombia is among them. Fundación Plan reports a larger gross income, but most of it is international transfers rather than money raised from Colombian individuals, so it is not a like-for-like comparison. On payments, UNICEF Colombia's setup is visibly more built out than its peers: Save the Children runs on Wompi, World Vision on Mercado Pago, Teletón shows two providers, Cruz Roja uses an embedded third-party widget. **For the call:** UNICEF Colombia is ahead of its peers technically, not behind. The conversation is optimisation and yield, never catching up. The closest operational analogue is Aldeas Infantiles, whose sponsorship model has the same monthly collection problem.

---

## 6. PAYMENTS MONEY MAP

All of this comes from the donation site's own HTML, scripts and Content-Security-Policy header. A CSP allowlist shows which vendors are permitted to load. It does not prove they process live volume, and the payment step was never submitted.

### Status

**Orchestrator: none found.** No public evidence links UNICEF Colombia, UNICEF globally or any National Committee to Spreedly, Primer, Gr4vy, CellPoint or APEXX. ⚠️ Note that Firstoken markets multi-processor tokenization, so part of an orchestration function may already sit in the vault.

### Providers and tooling

| Layer | Vendor | Evidence |
|---|---|---|
| Card vault and tokenization | Firstoken (PCI Level 1 vault, claims tokens usable "across over 200 processors") | CSP allows its capture SDK and frame; CSP violation reports go to monitor.firstoken.co; Firstoken's own site shows a UNICEF Colombia client logo ✅ |
| Processor, strongest signal | Mercado Pago | The site carries a bespoke inline script patching appendChild and insertBefore so that scripts injected by mercadopago.js receive the CSP nonce. That is deliberate engineering, not boilerplate ✅ |
| Processor, allowlisted | Wompi (Bancolombia) | wompijs.wompi.com and checkout.wompi.co widget in CSP ⚠️ presence only |
| Processor, allowlisted | Nuvei / SafeCharge | cdn.safecharge.com in script and frame sources ⚠️ presence only, and the theme is shared across UNICEF country sites so it may belong elsewhere |
| Fraud | Sift | cdn.siftscience.com in CSP ⚠️ presence only |
| Wallet JS | Google Pay | pay.google.com JS allowlisted; an HTML comment for a Google Pay logo exists with no rendered logo ⚠️ not verified either way |
| Face to face and telemarketing capture | Evergiving, operated by Waysact | Named explicitly in the official FAQ as the platform authorised advisors use ✅ |
| Back office | Azure app uni-pfp-pci-co.azurewebsites.net | CSP form-action permits posting to its receipt endpoint ✅ |
| CRM | Salesforce | Tender requires vendor integration "particularmente con Salesforce" ✅ |
| Platform | Drupal 11 on Acquia, custom theme unicef_psfr, custom module unicef_pci | Response headers and page source ✅ |

### Methods by market

Single market. Colombia only.

| Method | One-time | Monthly | Evidence |
|---|---|---|---|
| Credit card | Yes | Yes | FAQ and form footer logos (Visa, Mastercard, Amex) ✅ |
| Debit card | Via the credit card option | Yes, "tarjeta débito sin clave" per the emergency donation page | FAQ instructs donors whose bank is not listed to use the card option with a debit card ✅ |
| Savings or checking account debit | Yes | Yes | FAQ ✅ |
| Nequi | Yes | Yes | FAQ and form logic (hidden when phone country is not Colombia) ✅ |
| Daviplata | Yes | ⚠️ present in form logic, monthly availability not confirmed | Form JavaScript ✅ for presence |
| PSE wallets | Yes | Not shown for monthly | FAQ and a form rule showing the PSE logo only when donation type is one-time ✅ |
| Utility bill charging | Named as acceptable for new donors | Named in tender | RFP2026-10 ✅ |

### Fraud, 3DS and PCI

- CVV is collected on the web form but never by street advisors, so a large share of the recurring base was tokenized without CVV. ✅
- 3DS behaviour: not observed. 🔍
- Footer badge reads "Certificado PCI DSS" with no level, QSA or date published. Their tender requires vendors to complete PCI SAQ D plus an Attestation of Compliance. Expect the same request of Yuno. ✅

### Hiring and procurement signals

- 2026 vacancy: Fund Raising Assistant (Donor Retention), KPIs "donor attrition, conversion rates, gross revenue", tools "Salesforce, HubSpot, Marketing Cloud". ✅
- 2023 vacancy: Salesforce CRM Implementation Associate, including "Coordination of API integration of agencies to the new CRM" and "Support in optimizing CRM collection processes". ✅
- No tender for a payment gateway, donation platform or CRM exists. The open tenders are for fundraising agencies. ✅

### Framing rules for this account

Never suggest they are missing a method or behind their peers. The entire conversation is yield, cost per collected donation, and speed. They have built something competent, and the pitch is a layer on top of it.

---

## 7. NEWS AND SIGNALS

| Date | Item | Why it matters |
|---|---|---|
| **17 Sep 2026** | **UNICEF Colombia: "Invertir en la niñez es invertir en el desarrollo del país", asking Colombia to prioritise children in the National Development Plan debate** | Four days old, local, and theirs. The freshest rapport opener available |
| 17 Sep 2026 | UNICEF appeals for USD 97.5M to protect 540,000 children in Gaza and the West Bank this winter, including digital cash assistance | Global context; also a reminder that UNICEF moves money out as well as in |
| 15 to 17 Sep 2026 | Appeals on Haiti malnutrition, Yemen hostilities, Ukraine schooling, Nepal floods | The organisation is in a heavy appeal cycle |
| **1 to 4 Sep 2026** | **Executive Board: Catherine Russell states UNICEF projects USD 26 billion for 2026 to 2029, a 27% decline, a USD 6.6 billion reduction reaching country programmes** | The dominant strategic story at UNICEF right now. Know it |
| 2 to 3 Sep 2026 | "Global funding cuts could force 6 million more children out of school in the coming year" | The consequence being communicated publicly |
| 2026 | Humanitarian Action for Children appeal set at USD 7.66B for 73 million children, down from USD 10.2B requested for 2025 | The scale of the contraction in practice |
| 31 Jan 2026 onward | Córdoba flood emergency: 53,400 families (167,700 people), 80% of the department flooded, 24 of 30 municipalities. Appeal now covers Córdoba and La Guajira, 202,000+ people affected | The cause behind the gala, and a live local emergency |
| Open now, closes 28 Sep 2026 | RFP2026-10 (telemarketing and digital fundraising) and RFP2026-11 (face to face), both 3 year agreements | The live commercial context for this call |
| 17 April 2026 | First ever UNICEF Colombia benefit gala, Country Club de Bogotá. Raised approximately USD 140,000 for the Córdoba response, mainly for return to school (Portafolio separately reported more than COP 560M) | Rapport opener, and evidence of new channel experimentation |
| 31 March 2026 | Gala announced, quoting Gustavo Ugalde as Gerente de Movilización de Recursos and Tanya Chapuisat as Representative | Names the fundraising decision maker |
| February 2026 | UNICEF fundraising division 2026 workplan: $1,957M target, budget cut from $287M to $230M, 80 posts cut, staff relocating Geneva to Rome | Cost pressure is real and current |
| 19 November 2025 (updated) | UNICEF restructuring note: "at least a 20 per cent decline in income from 2026", around $586M in savings targeted | The macro backdrop |
| 11 April 2024 | Adyen and UNICEF global partnership via Adyen Giving (donations at merchants' checkouts). It does not state Adyen processes UNICEF's own donation forms | ⚠️ Know it exists so it does not surprise you. It is not evidence about Colombia |

---

## 8. SELLING YUNO HERE

### Core frame

"You have built a serious payment setup, and you are about to spend three years paying people to phone donors whose charges failed. We can take a share of those failures out of the phone queue and back into the payment layer, without you changing a single processor."

### Hooks with proof points

| Hook | Yuno proof |
|---|---|
| Recover failed recurring charges | 30% recovered revenue (published). InDrive: 4.5% recovery across 10 LatAm markets |
| Route each charge to the best processor | 7% approval uplift (published). Livelo: +5% approval, 50% recovery |
| Speed to enable a new processor or method | InDrive went live across 10 LatAm markets in under 8 months, no-code enablement |
| Operational visibility | Rappi: real-time detection in milliseconds against 5 to 10 minutes manually, 80% less analyst resolution time |

### Landmines, do not say

- Do not say they lack any payment method. Nothing about their method coverage was verified beyond what is listed above.
- Do not assert that Mercado Pago, Wompi or Nuvei is live. It is an inference from site code.
- Do not claim reconciliation as a shipped capability. It is roadmap.
- Do not quote approval or recovery numbers other than 7% uplift and 30% recovered revenue.
- Do not name other Yuno clients as references without checking permission first, especially any nonprofit or platform deal.
- Do not sound like you have been reading their internal documents. Their tender is public, so say so plainly if it comes up.
- No em dashes in anything you send afterwards, and never the phrase "no small feat".

---

## 9. BE READY FOR

| They ask | Answer |
|---|---|
| "What does it cost?" | List pricing is the first $50,000 in transactions free, then $0.05 per transaction. ⚠️ Do not convert to pesos live against their published COP 700 and COP 1,400 without the day's rate. Better: ask for their all-in cost per successfully collected donation and size the recovery against it |
| "How does this work with Firstoken? Do we lose our tokens?" | 🔍 Genuinely open. Firstoken advertises tokens usable across many processors. Commit to bringing a Solutions Engineer rather than guessing. This is the single most likely technical blocker |
| "Do you support Nequi, Daviplata, PSE and account debit?" | Yuno's public partner pages list Wompi, Nuvei and Nequi, and its docs list PSE, Daviplata and Mercado Pago among supported methods. ⚠️ Recurring account debit specifically needs confirmation before promising it |
| "How long does integration take?" | Frame by comparable scope rather than a fixed number, and offer the technical session to scope it properly |
| "Are you PCI compliant? We will need SAQ D and an AoC" | Yes, expect this request; their own tender demands it of vendors. Bring Yuno's attestation to the follow-up |
| "Do you work with other nonprofits or UN agencies?" | Be honest. Yuno's public case studies are commercial (InDrive, Rappi, Livelo, Reserva). The recurring billing and recovery problem is identical; the vertical is not the point |
| "Why not just build the retry logic ourselves in Drupal?" | They could, per processor. The cost is doing it again for every processor, every method and every channel, and maintaining it with a small team while running two tenders |
| "We are a UN agency, how would we even contract this?" | 🔍 Ask them. UN procurement will drive timeline more than anything technical. Find out the threshold above which a formal tender is required |
| "Can you talk to our telemarketing agency?" | Yes, and it is a good sign if they ask. The agency is not the competitor here; fewer failed charges makes the agency's targets easier |

---

# LIVE ZONE

## 10. AGENDA (30 minutes)

| Time | Block | Owner | Notes |
|---|---|---|---|
| 0:00 to 0:04 | Intros and roles round. Get all three to say what they own. Settles the Leidy and Sebastian unknowns | Susana or German | Notes: ____ |
| 0:04 to 0:07 | Why they booked. What triggered the search | German | Notes: ____ |
| 0:07 to 0:17 | Discovery: the first-of-month run, collection rate, what happens on failure today | German | Notes: ____ |
| 0:17 to 0:25 | Yuno, narrow: recovery of failed recurring charges, routing across their processors, visibility. No generic multi-country content | Alejandro or German | Notes: ____ |
| 0:25 to 0:29 | Next step: technical session with Idual plus the data pull. Name a date | German | Notes: ____ |
| 0:29 to 0:30 | Buffer | | Notes: ____ |

## 11. DISCOVERY QUESTIONS

Ask in Spanish. Do not re-ask anything the research already answered.

1. ¿Qué los llevó a buscar una solución de pagos ahora? ¿Hay un proyecto o una fecha detrás?
   Notes: ____
2. ¿Cuál es hoy la tasa de cobrabilidad del cobro del primer día del mes?
   Notes: ____
3. ¿Cómo se reparte esa cobrabilidad entre tarjeta de crédito, cuenta de ahorros o corriente, Nequi y Daviplata?
   Notes: ____
4. De los cobros que fallan, ¿cuántos son por tarjeta vencida o reexpedida y cuántos por fondos insuficientes?
   Notes: ____
5. ¿Hay reintentos automáticos antes de que el caso pase al call center, o el primer intento fallido ya genera una llamada?
   Notes: ____
6. ¿Qué procesadores están activos hoy y quién decide a cuál va cada cobro?
   Notes: ____
7. ¿Usan network tokens o algún servicio de actualización automática de tarjetas?
   Notes: ____
8. El débito a cuentas de ahorros y corriente, ¿cómo se procesa hoy? ¿Archivos con cada banco, ACH, un agregador?
   Notes: ____
9. Las altas de face to face y telemarketing entran por Evergiving. ¿Cómo llega ese cobro al procesador y a Salesforce?
   Notes: ____
10. ¿Cuántos donantes activos mensuales tienen y cuál es la donación promedio?
    Notes: ____
11. Ustedes publican que una transacción con tarjeta les cuesta en promedio $700 y un débito a cuenta $1.400. ¿Ese costo incluye todo, o solo la comisión del procesador?
    Notes: ____
12. ¿Las decisiones de stack de pagos son locales, o hay lineamientos de la oficina regional o de Ginebra?
    Notes: ____
13. ¿Quién más debería estar en la próxima conversación? ¿Gustavo Ugalde, finanzas, tecnología?
    Notes: ____
14. ¿Cómo compra UNICEF Colombia un servicio como este? ¿Desde qué monto se necesita una convocatoria formal?
    Notes: ____

## 12. POST-MEETING CHECKLIST

- [ ] Recap email the same day, in Spanish, to the three attendees, with the agreed next step and a date
- [ ] Log the outcome and every new fact into the account record, especially the collection rate and the live processors
- [ ] Book the technical session with Idual and a Yuno Solutions Engineer; put the Firstoken token question in the invite so they arrive prepared
- [ ] Send the data request in writing: collection rate by method and failure reasons for the first-of-month run
- [ ] Update memory with confirmed roles for all three attendees and correct the unconfirmed items in this brief
- [ ] Decide whether the 28 September tender close changes the timeline, and whether Gustavo Ugalde needs a separate approach

---

## APPENDIX: SOURCES

Full research brief with every source URL: `data/research/unicef-colombia-2026-09-21.md`

Primary sources used here:
- Donation site, FAQ, refund policy and fundraisers page: https://donaciones.unicef.org.co/donar · /preguntas-frecuentes · /politica-de-reintegros · /captadores · https://unicef.org.co/donar
- Tenders: https://www.unicef.org/colombia/convocatorias-para-empresas
- Legal entity: https://donaciones.unicef.org.co/aviso-privacidad
- Vault vendor: https://firstoken.co/
- Face to face platform: https://www.evergiving.com/payment-gateways
- UNICEF finances: https://www.unicef.org/reports/funding-compendium-2025 · https://www.unicef.org/media/173291/file/UNICEF_FundingCompendium2024.pdf · https://www.unicef.org/executiveboard/media/39341/file/2026-AS-Item-16-PFP-financial-report-Carla-Haddad-Mardini-PPT-EN-2026-06-17.pdf · https://www.unicef.org/executiveboard/media/35901/file/2026-FRS-Item-13-PFP-Workplan-Budget-Carla-Haddad-Mardini-PPT-EN-2026-02-04.pdf
- Restructuring: https://www.unicef.org/media/current-issues/information-note-ongoing-restructuring-initiatives
- Gala and leadership: https://www.unicef.org/colombia/comunicados-prensa/unicef-celebrar%C3%A1-en-colombia-su-primera-gala-ben%C3%A9fica-para-apoyar-la-ni%C3%B1ez-y
- Attendee: https://co.linkedin.com/in/idual-kerguelen-monta%C3%B1o-87561433
- Traffic: https://www.semrush.com/website/unicef.org.co/overview/
