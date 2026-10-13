# SDR Research Brief: JPay (Securus / Aventiv)
*Framework v8.0 · 4 agents · Research date: 13-Oct-2026*

> **Entity note:** No separate company called "JPay Solutions" was found (searches covered the US, Kenya, Jamaica, India, the Philippines and the UK). The target is **JPay LLC (jpay.com)**, a US corrections payments company and subsidiary of Securus Technologies under **Aventiv Technologies** [S1][S2]. Unrelated names that are easy to confuse with it: **Juspay** (Bengaluru), **JetPay**, and a Taiwan Shopify app called "JPAY" built by HiTRUSTpay [S30].

---

## EXECUTIVE SUMMARY

JPay is a NY DFS‑licensed money transmitter based in Miramar, FL. It moves money from families into inmate trust accounts, runs parole and probation payments, and issues release cards. It serves roughly 1.5M to 1.9M incarcerated people across about 33 to 35 state DOCs [S1][S3].

- **Traffic:** effectively 100% US (96.65%) [S4].
- **Payment rails:** cards (web, app, IVR), MoneyGram cash at retail, and money orders sent to a lockbox [S5][S6].
- **Card processor:** not publicly identifiable. Card entry sits behind login, and the public pages load no third‑party payment scripts [S5][S7].
- **Context for an approach:** creditors took control of the parent in July 2026 [S8][S9], a new CEO was named on 3‑Aug‑2026 with "payments" listed among his priorities [S10], and JPay lost New Jersey (2025), Florida (2024) and North Carolina (2023) to rivals on fees [S11][S12][S13].

That points to a payment cost and approval‑rate story on small‑ticket, high‑frequency US card deposits. **This is not a cross‑border or APM fit, and the ICP score is Low.**

---

## SECTION 1: Traffic by Country

Source: Similarweb, September 2026 [S4]

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source URL |
|---|---|---|---|---|---|
| 1 | United States | 96.65% | ~1.0M total site (chart label, approx.) | -4.88% MoM | [S4] |
| 2 | United Kingdom | 0.64% | N/A | N/A | [S4] |
| 3 | Mexico | 0.33% | N/A | N/A | [S4] |
| 4 | Brazil | 0.27% | N/A | N/A | [S4] |
| 5 | Canada | 0.22% | N/A | N/A | [S4] |
| | Others | 1.88% | N/A | N/A | [S4] |

**Other Similarweb data:**
- Global rank #38,524; US rank #7,795; #107 in Finance > Other (US).
- Direct traffic is 59.25% of visits, which fits a repeat, logged‑in user base.

**Flags:**
- No market other than the US is above 5%.
- LATAM, APAC and MENA traffic is negligible.
- securustech.net was not analyzed.

---

## SECTION 2: Legal Entities

| Country | In Top 10 Traffic? | Has Local Entity? | Cross-Border Risk? | Source URL |
|---|---|---|---|---|
| United States | Yes (#1) | Yes. JPay LLC is a Delaware LLC with HQ in Miramar, FL, wholly owned by Securus Technologies. It holds a NY DFS money transmitter license and a GA DBF license (NMLS #926932). | No | [S7][S14] |
| UK / Mexico / Brazil / Canada | Yes | No entity found | Not applicable. These shares are almost certainly visitors, not a served market. | [S4] |

**Corporate tree:**
- Aventiv Technologies is the parent of Securus Technologies, Securus Monitoring, JPay and **AllPaid** (government payments outside corrections) [S15][S16].
- Footer: "© 2002‑2026 JPay LLC, An Aventiv Company."

> ⚠️ MANUAL: Verify the full money‑transmitter license list on NMLS Consumer Access.

---

## SECTION 3: Payment Stack

**3A. PSPs, Acquirers and Issuers**

| Country/Region | Provider | Role | Evidence Type | Source URL |
|---|---|---|---|---|
| US | **Not found** | Card acquirer / gateway | [Source Code] Homepage, SendMoney and Login pages plus the JS bundles show only ASP.NET WebForms, jQuery 3.5.1, GTM, New Relic and OneTrust. No stripe.js, Braintree, CyberSource, Authorize.net, Worldpay, Paya, Nuvei or Fiserv. | [S5][S7] |
| US | **MoneyGram** | Cash deposits at agent locations (Walmart, CVS, 7‑Eleven) with a receive code | [Checkout] [Regulatory Filing: state DOC pages] | [S5][S6][S17] |
| US | JPay lockbox (Miramar, FL) | Money orders, "processed electronically" | [Checkout] | [S5][S17] |
| US | **Metropolitan Commercial Bank**, with Praxell Inc. dba Juice Financial as program manager | Issuer of the JPay release prepaid Mastercard. Georgia DOC (about Dec‑2023) says it is "soon transitioning to a new bank"; the CFPB database shows the Metropolitan agreements as Withdrawn. | [Regulatory Filing] | [S18][S19] |
| US | MetaBank, N.A. | Issuer of the paySupreme prepaid Mastercard sold through JPay. **Search snippet only, page not opened.** | Unverified | N/A |

**3B. Orchestrator:** No public evidence found for JPay, Securus, ViaPath or Access Corrections.
- [INFERENCE, not confirmed] Card capture is probably server‑side in a legacy in‑house stack with a direct gateway integration.

> ⚠️ MANUAL, DevTools: create a sender account, start a deposit, and inspect network calls for the gateway host. Test card 4111 1111 1111 1111 | 02/30 | 123 (do not submit a live deposit).

---

## SECTION 4: APMs (Agent D findings)

**4A. Confirmed payment methods**

| Market | Methods Confirmed | Verification Source | Source URL |
|---|---|---|---|
| US (jpay.com) | Credit/debit card (web, app, phone/IVR at 800‑574‑5729); MoneyGram cash; money order to lockbox; recurring transfers; saved cards | jpay.com Money Transfer page, App Store listing | [S5][S20] |
| US (Virginia DOC) | Card online, phone, app; MoneyGram cash (Walmart, CVS); money order (3 business days) | Official DOC page | [S6] |
| US (Oregon DOC) | Card online or phone; MoneyGram at Walmart, 7‑Eleven, CVS with receive code 7813 | Official DOC page | [S17] |
| US (Missouri DOC) | Exclusive JPay vendor; phone via live agent; MoneyGram receive code 2439 | Official DOC page | [S21] |
| US (Pennsylvania DOC) | Card capped at $300 per card every 72h; MoneyGram walk‑in up to $5,000; money orders **not** accepted at PA institutions | Search snippet (page not fetched) | [S22] |

**4B. Unverified items**

| Item | Verification Attempted? | Reason Not Verified | Notes |
|---|---|---|---|
| Card brands (Visa/MC/Discover/Amex) | Yes | No official JPay page names them; a third‑party guide says "Visa and MasterCard only" | Treat as unverified |
| Apple Pay / Google Pay / PayPal / Venmo / ACH | Yes | Not mentioned on any public page; checkout is behind login | "Not verified" ≠ "not available" |
| International senders / non‑USD | Yes | No official statement either way | All evidence is US/USD |

> MANUAL: Walk a logged‑in checkout before making any wallet or bank‑payment claim.

---

## SECTION 5: Payment Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|---|---|---|---|---|
| Forced release‑card fees, EFTA/Reg E violations; $6M order ($4M redress + $2M penalty) | CFPB consent order | About 1.2M cards issued 2011‑2021; about 176K consumers affected 2014‑2017 | Order 19‑Oct‑2021, 5‑year term | [S23][S24] |
| Refunds withheld for failed downloads; defective tablets; $500K in credits | NY Attorney General | Settlement | Dec‑2022 | [S25] |
| Refunds denied ("system will not allow a refund"); one ticket at a time; replies take weeks | Prison Journalism Project | Reported pattern | Oct‑2023 | [S26] |
| Payment declined; advice not to resend until cleared, which implies duplicate‑charge risk | GetHuman (third‑party guide) | Unquantified | Undated | [S27] |
| Double charge followed by account block | PissedConsumer | Single anecdote | 2020 | [S28] |
| High fees relative to deposit size (about 19% on $20, about 12% on $50) | Prison Policy Initiative | Structural | 2021 | [S29] |
| Low app satisfaction: iOS about 2.3★ (about 13K ratings); Google Play about 4.0★ (about 104K reviews) | App store aggregators | N/A | Dec‑2025 listing | [S31][S32] |

**What the complaints tell us:**
- The documented pain is mostly refund friction, fees and regulatory exposure.
- Card declines and double charges show up only as anecdotes and could not be quantified.
- **Yuno link:** real‑time monitoring and retry logic on small‑ticket deposits, plus cleaner refund and reconciliation flows.
- This is a soft angle, not a proven one.

---

## SECTION 6: Expansion & Corporate Developments

| # | Date | Development | Category | Source URL |
|---|---|---|---|---|
| 1 | Apr‑2024 | Aventiv defaults after a failed refinancing (about $1.6B of debt) | Distress | [S33] |
| 2 | 16‑Apr‑2025 | Debt‑for‑equity agreement with Platinum Equity and 100% of lenders; $360M new financing | Recapitalization | [S8][S34] |
| 3 | 30‑Apr‑2025 | 🔴 NJ DOC moves trust deposits from JPay to ViaPath. NJ says fees fell 37% on average. | Contract loss | [S11] |
| 4 | Aug‑2025 | PA DOC emergency procurement extends the JPay EFT contract "to prevent a lapse" | Contract bridge (possible re‑bid) | [S35] |
| 5 | 11‑Jun‑2026 | California PUC approves the ownership transfer | Regulatory | [S36] |
| 6 | 2‑Jul‑2026 | Recapitalization and ownership transition completed; lenders reportedly hold about 97% of equity (secondary source) | Ownership change | [S9][S37] |
| 7 | ~21‑Jul‑2026 | S&P cuts Aventiv to D (distressed exchange) | Credit | [S38] |
| 8 | 3‑Aug‑2026 | **Brian Evans named CEO**, Kevin Elder named President, Jorge Dominicis Chair. Priorities include tech investment in "payments". | Leadership | [S10] |
| 9 | ~Oct‑2026 | CFPB consent order reaches the end of its 5‑year term [INFERENCE, not confirmed] | Regulatory | [S24] |

**Earlier losses (outside the 24‑month window):**
- Florida DOC moved to CorrectPay (1‑May‑2024) [S12].
- North Carolina moved to ViaPath (Oct‑2023) [S13].

**Not found:** payments job postings, a CFO or CTO hire, M&A.

**Payments leadership:** Peter Ohser (ex‑MoneyGram CRO) became President of payment services in 2019 [S39]. **Whether he is still there is unverified.**

---

## SECTION 7: Payment News

| # | Date | Headline | Relevance | Source URL |
|---|---|---|---|---|
| 1 | Jul‑2026 | Aventiv completes recapitalization; Securus, Securus Monitoring and JPay brands continue | New owners mean a likely vendor and cost review [INFERENCE] | [S9] |
| 2 | Aug‑2026 | New CEO Brian Evans; "payments" among priorities | Entry point at the executive level | [S10] |
| 3 | 2025 | NJ swaps JPay for ViaPath and advertises lower deposit fees | Fee competition in state re‑bids | [S11] |
| 4 | 2024‑2026 | FCC IPCS rules (Martha Wright‑Reed Act) cap card payment‑processing charges on communications; implementation delayed and under revision | Squeezes margin on the Securus comms side. JPay money‑transfer fees are set by state contracts, not the FCC. | [S40][S41] |
| 5 | 2025‑2026 | 🟢 New PSP partnerships / 🔴 removals | **None found** | N/A |

---

## SECTION 8: Checkout Audit

| Dimension | Finding | Quality | Notes |
|---|---|---|---|
| Checkout type | Account‑based; register first, then find the incarcerated person [S42] | ⚠️ | Legacy ASP.NET WebForms front end [S7] |
| Guest checkout | Not indicated; registration required [S42] | ⚠️ | "Depositor verification" applies (KYC‑style) [S5] |
| Steps to purchase | Not verified (behind login) | N/A | MANUAL |
| 3DS | No 3DS scripts on public pages; checkout not inspected | N/A | MANUAL |
| Mobile experience | Native apps exist with saved cards and recurring transfers [S20]; iOS about 2.3★ [S31] | ⚠️ | |
| Method display logic | Varies by agency contract. Example: PA rejects money orders and caps cards at $300/72h [S22]. | N/A | Each state is effectively its own configuration |

**Fees by state:**

| State | Online | Phone/IVR | Walk‑in (MoneyGram) | Source |
|---|---|---|---|---|
| Virginia | $2.95 to $9.95 | $3.95 to $10.95 | $6.95 | [S6] |
| Washington ("JPay & Securus") | $3.25 to $10.95 | Not captured | $6.95 | [S43] |
| Georgia | $3.50 to $6.50 | $3.50 to $6.50 | $4.95 | [S44] |

> ⚠️ MANUAL: Walk the checkout in 2 or 3 states (e.g. VA, PA, GA).

---

## SECTION 9: PCI DSS

| PCI DSS Level | Card data handling | Recommended Yuno integration | Source |
|---|---|---|---|
| No public certification or attestation found | Card fields served from jpay.com's own pages; no hosted fields from a third party seen [INFERENCE, not confirmed] | **Direct API with Yuno vault** (keeps their UX, lowers their PCI scope) or **SDK Lite** if they rebuild the front end | [S7] |

---

## SECTION 10: Strategic Insights

**Insight #1: New owners, new CEO, payments on the agenda**
- **Evidence:**
  - Section 6, rows 6 and 8: lenders hold about 97% of equity, the S&P rating is D, and Evans was named CEO on 3‑Aug‑2026 with "payments" among his priorities.
- **Pain point:**
  - After a distressed exchange the mandate is margin and cash discipline.
  - Payment cost and lost deposits are direct P&L levers.
- **Yuno value prop:**
  - Smart routing and cost‑based routing across acquirers.
  - +7% approval uplift on card deposits.
  - One integration for the JPay, Securus Debit and AllPaid flows [INFERENCE that these run on separate stacks].
- **Best case:** Rappi (zero implementation time, 80% less analyst resolution time).
- **Outreach angle:** "New ownership usually brings a hard look at cost to collect. On high‑frequency, small‑ticket deposits, routing and approval rate move margin more than anything else."

**Insight #2: State re‑bids are being won on fees**
- **Evidence:**
  - Section 6, rows 3 and 4: NJ moved to ViaPath with a 37% fee cut, and PA is on an emergency bridge.
  - FL and NC were lost earlier.
- **Pain point:**
  - Every RFP compares deposit fees.
  - The processing cost under each deposit sets how low JPay can bid.
- **Yuno value prop:**
  - Lower blended processing cost through routing.
  - Faster rollout of new rails a DOC may ask for in an RFP (e.g. wallets), live in weeks.
- **Best case:** Livelo (+5% approval, 50% recovery).
- **Outreach angle:** "When a state re‑bid comes down to fees, the cost of processing each deposit sets your floor."

**Insight #3: Each failed deposit is a lost fee plus a frustrated family**
- **Evidence:**
  - Section 5: decline and duplicate‑charge advice, refund friction, iOS 2.3★.
  - Section 8: deposit fees run $2.95 to $10.95.
- **Pain point:**
  - A declined $20 deposit loses about a $3 fee.
  - Retries risk double charges and drive support tickets.
- **Yuno value prop:**
  - Retry and failover to a second acquirer.
  - Real‑time monitors (Rappi: millisecond detection vs. 5 to 10 minutes manually).
- **Best case:** Reserva (+4% approval in under 3 months).
- **Outreach angle:** Keep it about approval rate and monitoring. **Do not cite complaints in outreach.**

**Insight #4 (watch item): Release cards and disbursements**
- **Evidence:**
  - Section 3A: the issuing bank is in transition.
  - Section 6, row 9: the CFPB order is reaching the end of its term.
- **Pain point:** Payout (gate money) design is under regulatory scrutiny.
- **Yuno value prop:** Payouts orchestration as a later conversation. **Not a lead angle.**

---

## SECTION 11: Pipeline

**11A. Direct Competitors (corrections payments)**

| Company | Website | HQ | Est. Size | Overlap Markets | Source |
|---|---|---|---|---|---|
| ViaPath Technologies (ex‑GTL; TouchPay, Telmate) | viapath.com | Not verified | Sole provider in ~6 states, present in ~13 (2021); won NJ 2025 and NC 2023 | US state DOCs | [S11][S13][S29] |
| Access Corrections (Keefe / TKC Holdings) | accesscorrections.com | Not verified | Sole provider in ~10 states, present in ~16 (2021) | US state DOCs | [S29] |
| CorrectPay | Not verified | Not verified | Won Florida DOC (May‑2024) | US | [S12] |
| JailATM | Not verified | Not verified | SD, WV (2021) | US | [S29] |
| Western Union | westernunion.com | Denver, CO | Global | Alternative in ~5 states | [S29] |

Not verified this pass: Smart Communications, Pigeonly, NCIC, Union Supply, CorrLinks, Edovo.

**11B. Industry Peers**

| Company | Website | Vertical | Key Markets | Why Similar | Source |
|---|---|---|---|---|---|
| AllPaid (Aventiv sister) | Not verified | Government payments | US | Same parent; possible joint acquiring | [S15] |
| MoneyGram | moneygram.com | Remittance / cash network | Global | JPay's cash partner | [S6] |

Other peers named in the brief (PayNearMe, Paymentus, Invoice Cloud, Tyler payments, nCourt) were **not researched** in this pass.

**11C. Adopting Orchestration:** No public evidence found for any company in this vertical.

**11D. Scoring (JPay, verified only)**

| Signal | Pts | Verified? |
|---|---|---|
| Operates in 3+ countries | +3 | ❌ US only |
| Multiple PSPs | +3 | ❌ Not verified (MoneyGram is a cash network, not a PSP) |
| Recent expansion (24 mo.) | +2 | ❌ Contract losses, not expansion |
| Public payment issues | +2 | ✅ CFPB, NY AG, refund friction |
| Funding >$10M | +2 | ✅ $360M new lender financing (2025) |
| LATAM/APAC/MENA traffic | +2 | ❌ <1% |
| No orchestrator | +2 | ✅ No public evidence |
| Payment job postings | +1 | ❌ Not found |
| Public RFP | +3 | ❌ PA emergency extension only (watch for re‑bid) |
| **Total** | **6** | 🟢 **Low** |

**Top Pipeline:** The vertical is US‑only and regulated, so it is a weak fit across the board. No competitor could be fully scored with verified data.
- **ViaPath:** multi‑brand (TouchPay, Telmate, ConnectNetwork), so a consolidation angle. Score not verified.
- **Access Corrections:** score not verified.

**Pipeline summary:** 5 direct competitors and 2 peers found; 0 high priority. The strongest vertical for Yuno is not this one.

---

## SECTION 12: Business Case

| Annual Revenue | Avg Transaction Value | Est. Annual Transactions | Primary Currency | Top 3 Markets |
|---|---|---|---|---|
| Aventiv: Q2‑2023 revenue $156M [S45], which implies about $600M+/yr for the group [INFERENCE, not confirmed]. JPay alone: not found. | Not published. Likely $20 to $100 based on fee bands [INFERENCE, not confirmed]. | Not found | USD | US (96.65%). No other real market. |

---

## SECTION 13: Outreach

Target: payments leadership at Aventiv/JPay. Confirm Peter Ohser's status first, or go to Kevin Elder (President).

```
--- LINKEDIN MESSAGE ---
Hi Kevin, congrats on the new role and on closing the recapitalization in July.

A new ownership group usually takes a hard look at cost to collect. JPay's
deposits are small, frequent and priced state by state, so approval rate and
processing cost carry more weight than usual. A declined $20 deposit is a lost
fee and a family calling support.

At Yuno we sit on top of existing acquirers with one API: smart routing, retries
and real-time monitoring, typically adding around 7% to approval rates. Rappi and
Livelo run on it today.

Open to a 20 minute call next Tuesday or Wednesday to compare notes on how
you're thinking about payments under the new structure?

--- COLD EMAIL ---
Subject: Cost to collect on JPay deposits

Hi Kevin,

Congratulations on the new role, and on getting the recapitalization over the
line in July. Brian's note that payments sits among the priorities caught my eye.

JPay is a payments business where every transaction is small and frequent, and
the price to the family is set contract by contract. That makes two numbers
matter more than usual: how many deposits get approved the first time, and what
each one costs to process. As state re-bids keep coming down to fees, the second
one sets the floor on what you can offer.

Yuno is a payment orchestration layer. We sit on top of the acquirers you
already use, route each deposit to the best path, retry soft declines and watch
performance in real time. Merchants typically see around a 7% lift in approvals,
and Rappi cut analyst resolution time by 80% with our monitors.

Would a short call next Tuesday or Wednesday be useful? Happy to walk through
what this looks like for a high-volume deposit flow.

Best,
German
```

**Notes:**
- Recipient and dates are placeholders. Confirm the right owner of payments (Ohser / Elder / Evans) before sending.
- No unverified payment methods are referenced.
- No complaints or regulatory history appear in the outreach.

---

## APPENDIX: Source URLs

```
[S1]  https://en.wikipedia.org/wiki/JPay
[S2]  https://www.platinumequity.com/our-company/aventiv/
[S3]  https://builtin.com/company/jpay
[S4]  https://www.similarweb.com/website/jpay.com/
[S5]  https://www.jpay.com/PMoneyTransfer.aspx
[S6]  https://vadoc.virginia.gov/family-and-friends/sending-money/
[S7]  https://www.jpay.com/ ; https://www.jpay.com/TermsOfService.aspx
[S8]  https://www.sfnet.com/home/chapters/canada/news-detail/2025/04/17/aventiv-technologies-reaches-agreement-with-key-financial-stakeholders-to-recapitalize-the-company-and-position-it-for-future-growth
[S9]  https://www.financialcontent.com/article/bizwire-2026-7-2-aventiv-technologies-completes-recapitalization-and-ownership-transition
[S10] https://correctionalnews.com/?p=57300
[S11] https://nj.gov/corrections/pages/viapath.html
[S12] https://pubapps.fdc.myflorida.com/citizen/friendsandfamily.html
[S13] https://dac.nc.gov/media/12738/open
[S14] https://files.consumerfinance.gov/f/documents/cfpb_jpay-llc_consent-order_2021-10.pdf
[S15] https://www.corrections1.com/products/communications/press-releases/securus-technologies-realigns-business-units-diversifies-product-offerings-under-new-corporate-parent-aventiv-technologies-4cyTB8h0FapoFP4L
[S16] https://www.prisonlegalnews.org/news/2020/jan/9/securus-technologies-rebrands-aventiv/
[S17] https://oregon.gov/doc/sending-money/pages/jpay.aspx
[S18] https://gdc.georgia.gov/document/document/georgia-release-card-change/download
[S19] https://www.consumerfinance.gov/data-research/prepaid-accounts/search-agreements/detail/188075/
[S20] https://apps.apple.com/us/app/jpay/id584959322
[S21] https://docservices.mo.gov/DAI/Money_Transfer.php
[S22] https://www.cor.pa.gov/family-and-friends/Pages/How%20to%20Send%20an%20Inmate%20Money.aspx
[S23] https://www.consumerfinance.gov/enforcement/actions/jpay-llc/
[S24] https://www.prisonpolicy.org/blog/2021/10/28/cfpb-jpay/
[S25] https://ag.ny.gov/press-release/2022/attorney-general-james-delivers-500000-credits-incarcerated-individuals-who-were
[S26] https://prisonjournalismproject.org/2023/10/22/jpay-refuses-refunds-videogram-software-glitches/
[S27] https://gethuman.com/customer-service/JPay/how/What-Do-I-Do-If-My-Payment-Was-Declined-on-JPay/efy
[S28] https://www.pissedconsumer.com/people/2939885.html
[S29] https://www.prisonpolicy.org/blog/2021/11/09/moneytransfers/
[S30] https://apps.shopify.com/jpay
[S31] https://mwm.ai/apps/jpay/584959322
[S32] https://apppricinglab.com/app/google_play/com.brisk.jpay
[S33] https://pestakeholder.org/news/platinum-equity-owned-prison-telecom-company-aventiv-defaults-faces-uncertain-future/
[S34] https://news.bloomberglaw.com/bankruptcy-law/platinum-backed-aventiv-agrees-to-hand-control-to-creditors
[S35] https://www.emarketplace.state.pa.us/EP_Details.aspx?id=40145
[S36] https://news.bloomberglaw.com/bankruptcy-law/prison-phone-company-aventiv-clears-hurdle-for-lenders-takeover
[S37] https://briefglance.com/articles/aventivs-new-guard-can-tech-and-finance-remake-a-controversial-giant
[S38] https://news.bloomberglaw.com/bankruptcy-law/aventiv-technologies-cut-to-d-by-s-p-after-debt-equity-exchange
[S39] https://www.executivebiz.com/articles/peter-ohser-joins-securus-technologies-to-lead-payment-services-business-robert-pickens-comments
[S40] https://finesandfeesjusticecenter.org/research-tools/guide-to-new-low-rates-and-consumer-protections-for-incarcerated-peoples-communications-services/
[S41] https://www.nclc.org/resources/comments-urging-fcc-to-retain-regulations-protecting-incarcerated-people-and-their-families-access-to-affordable-communications/
[S42] https://www.jpay.com/Help.aspx
[S43] https://www.doc.wa.gov/node/179
[S44] https://gdc.georgia.gov/friends-and-family/send-money-offender/how-do-i-send-money-offender/send-money-online-jpay
[S45] https://www.bloomberg.com/news/articles/2023-08-18/tom-gores-s-prison-phone-firm-aventiv-reports-improved-earnings
```
