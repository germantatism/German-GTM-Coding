# Meeting Brief: Yuno <> American Red Cross
*Sep 2, 2026*

## Header

**Meeting:** Red Cross Org x Yuno
**Date/time:** Wednesday, September 2, 2026, 10:30-11:00 AM Colombia Time (COT) / 11:30 AM-12:00 PM Eastern (EDT)
**Link:** meet.google.com/zbo-vdac-oce
**Organizer:** Susana Awad (Yuno SDR)
**Objective:** This is a cold, SDR-booked, 30-minute first call with a single external attendee whose seniority is unconfirmed. Winning this meeting means confirming who Carlos actually is and what he owns, landing one or two hooks that map to what Red Cross has already said publicly about itself, and leaving with a named next step, ideally an introduction to whoever owns the payments decision (most likely CIO Ronnie Strickland's org or Finance/Financial Shared Services under CFO Carmel Darcy), not a close.

### ⚠️ Pre-meeting actions
- No prior Yuno-Red Cross contact exists anywhere (calendar, Gmail). Confirm with Susana what prompted Carlos to accept, since no email trail was found.
- Carlos Carneiro's LinkedIn could not be found despite exhaustive search. Try manually before the call: linkedin.com/search/results/people/?keywords=Carlos%20Carneiro&company=American%20Red%20Cross
- His title ("Consultant, Merchant Services") rests on a single blocked ZoomInfo record. Confirm his actual role and scope in the first two minutes rather than assuming seniority.
- German's calendar status on this event shows as optional/needsAction on some views despite being listed as accepted. Confirm attendance.
- No agenda was set on the invite. Align with Susana beforehand on the specific ask for this call.

---

## 1. TL;DR Battle Card

**Five facts to know cold:**
1. American Red Cross is one single legal entity, EIN 53-0196605, no operating subsidiaries (Form 990 Schedule R confirms zero related organizations). Every chapter, Biomedical Services, Training Services, the Store, and International Services sit inside one corporation.
2. Revenue is majority B2B, not donations: 63% of FY2025's $3.92B came from Biomedical Services selling blood products to ~2,500 hospitals ($2.3B); only 34% was contributions.
3. Live inspection found at least three disconnected gateway combinations across three donation/checkout surfaces (Braintree plus a legacy Cybersource vault on the main donation form, Cybersource alone on Training/Store, and Stripe plus Braintree plus Plaid plus TokenEx on the Classy-powered campaign-giving property), including a hand-written code branch on the main form that manually decides which token to submit, hard evidence of homegrown orchestration they built and now maintain themselves.
4. Red Cross declared its second-ever national blood supply crisis on July 27, 2026, and three weeks later launched a $300M, five-year "LifeBlood Fund" that explicitly names "advanced technology" as part of the fix.
5. Three financial-services CEOs sit on the 12-person Board of Governors: Michael Miebach (Mastercard), Gunjan Kedia (U.S. Bancorp), and Juan C. Andrade (USAA). U.S. Bank already issues Red Cross's own prepaid Mastercard for disaster payouts.

**Three hooks, in priority order:**
1. **Invoice Central (B2B billing on the $2.3B blood-product line).** Their homegrown Oracle APEX portal added "Quick Pay" card acceptance in December 2025, but there is no stored-credential vault (hospitals re-key full card details on every single invoice) and Red Cross's own public FAQ still says "we do NOT accept Credit Card payments online." This is an unfinished modernization on their largest revenue line, live right now.
2. **Consumer donation checkout consolidation.** Three separate donation surfaces run three different gateway combinations (Braintree+Cybersource on the main form, Cybersource alone on Training/Store, Stripe+Braintree+Plaid+TokenEx on the Classy-powered campaign-giving property), and on the main form some recurring donors with saved cards get silently forced to re-enter payment details, a self-inflicted churn leak on Monthly Giving, evidenced in their own code, not assumed.
3. **Cross-border disbursement speed and cost.** 100% of international grant payments run by wire transfer, 49 of 49 lines across three straight years, while Red Cross's own strategy explicitly calls for expanding cash and voucher assistance, and IFRC's own internal review called its systems "a key blocker to rapid and scalable CVA delivery."

**THE objection they will likely raise + the answer:** Given Carlos's likely individual-contributor level, expect either "I don't have budget authority for this" or "we're a nonprofit, this isn't the kind of spend we make." Answer: this is a discovery call, not a purchase conversation. Frame it as understanding their environment and asking who else should be in the room, not asking for a decision today.

**The ask:** Leave with a named next step: either a second call with a specific technical or finance stakeholder (CIO org or Financial Shared Services), or a concrete list of what Red Cross would need to see to take this further. Do not push for a demo or pricing discussion in a 30-minute first call with an unconfirmed decision-maker.

**Rapport opener:** September 2 is day two of National Preparedness Month, and the meeting lands three weeks after the $300M LifeBlood Fund announcement (Aug 17) and five weeks after the national blood supply crisis declaration (Jul 27). Open with genuine interest in the LifeBlood Fund's "advanced technology" language rather than a generic icebreaker.

---

## 2. Who Is in the Room

| Name | Role | Side | Status |
|---|---|---|---|
| Carlos Carneiro | Consultant, Merchant Services (⚠️ unconfirmed, single source) | External | Accepted |
| German Tatis | Account Executive | Internal (Yuno) | Accepted |
| Susana Awad | SDR, organizer | Internal (Yuno) | Accepted |

**Carlos Carneiro profile (confidence: low-medium on role, high on existence):**
- Email carlos.carneiro@redcross.org, based Washington DC per ZoomInfo (single source, page itself blocked, confidence low-medium)
- Title reads "Consultant, Merchant Services," American National Red Cross. "Consultant" is commonly used at large nonprofits as an individual-contributor band title, not a leadership title. Read him as a technical evaluator or coach, not a budget holder, until proven otherwise.
- LinkedIn profile not found despite nine query variants. About a dozen unrelated people named Carlos Carneiro exist (Itau, SEDRA Chile, Portuguese Football Federation, Vertex, others); none connects to Red Cross.
- No press mentions, no career history, no education data found anywhere.
- Surname is Portuguese/Brazilian in origin; no evidence connects him to Brazil or Cruz Vermelha. Do not assume.
- Zero prior correspondence in Gmail, zero prior calendar history with him or anyone at redcross.org. This is a genuinely cold first meeting.

**Sponsor/intro path:** Susana Awad (Yuno SDR) booked this cold; the only artifact is her Aug 26 calendar invite. No email sequence or reply thread exists in Gmail, so the original outreach channel is unknown, confirm with Susana before the call.

**Relationship timeline:** None. No prior Yuno-Red Cross meeting or email exists on any channel checked (Calendar, Gmail; Gong is not configured in this environment). Treat as a pure first meeting.

**Other known contacts in the account (buying committee map):**
- **Carmel Darcy, Chief Financial Officer** since 1999, licensed CPA (VA), Executive Champion of the ARC Latino Resource Group. linkedin.com/in/carmel-darcy-a8b50718a/
- **Brian J. Rhoa, Chief Investment Officer** (current title, confirmed live). Joined as CFO in 2008, when Red Cross had 4,000 bank accounts and 500 general ledgers; led the "One Red Cross" consolidation into one. The single best proof point that this organization has already bought into, and executed, exactly the kind of financial-plumbing consolidation Yuno sells.
- **Ronnie Strickland, Chief Information Officer.** The only technology executive on the current leadership page; there is no CTO or Chief Digital Officer at Red Cross.
- **Anne McKeough, Chief Development Officer** (confirmed live, owns fundraising strategy).
- **James "Chris" Hrouda, President, Biomedical Services.** Owns the $2.3B blood-product line and Invoice Central; highest-paid Red Cross executive in FY2025 ($928,973), ahead of the CEO's base salary, consistent with where the revenue actually sits.
- **Jack McMaster, President, Training Services** (owns the paid CPR/first-aid certification business).
- **Kathy Miu, VP of Innovation** (public spokesperson for the Clara AI / AWS grant initiative).
- **Cliff Holtz, President & CEO** since July 1, 2024, prior COO; ex-Pelco/Schneider Electric, Nortel, Deloitte, Qwest, Gateway.
- **Board of Governors payments literacy:** Michael Miebach (CEO, Mastercard), Gunjan Kedia (President & CEO, U.S. Bancorp), Juan C. Andrade (President & CEO, USAA) all sit on the 12-person board. Assume anything said in the room could eventually be tested against people who run networks and banks for a living.

---

## 3. The Company

American Red Cross is a congressionally chartered 501(c)(3), legally a "federal instrumentality," not a federal agency and not regularly federally funded (36 U.S.C. §300101 et seq., chartered 1900). Five operating lines: Biomedical Services (blood collection and sale to hospitals), Training Services (paid CPR/first aid/lifeguard certification), Domestic Disaster Services, International Services, and Service to the Armed Forces.

**Key metrics (FY2025, ended June 30 2025):**

| Metric | Value | Source |
|---|---|---|
| Total revenue | $3,916,983,933 (990) / $3,964.2M (audited operating) | Form 990, EIN 53-0196605 |
| Net income | $631,126,389 | Form 990 |
| Total assets | $5,052,941,623 | Form 990 |
| Employees / volunteers | 17,907 / 325,000 | Form 990 / Annual Report |
| Program expense ratio | 91% | Charity Navigator (4-star), Red Cross self-published |

**Corporate structure and subsidiaries:** No operating subsidiaries. Form 990 Schedule R shows zero disregarded entities, zero related tax-exempt organizations, and zero related partnerships, only 71 planned-giving trust vehicles (pooled income funds and charitable remainder/perpetual trusts). The filer name is literally "American National Red Cross & Its Constituent Chapters and Branches," meaning every chapter, blood region, and business unit sits inside one corporation under one EIN. This is unusual for an organization this size and is a genuine structural argument for a single orchestration layer, there is no subsidiary or separate billing entity to reconcile.

| Unit | FY2025 revenue | How it collects money |
|---|---|---|
| Biomedical Services (redcrossblood.org) | $2,305.2M | B2B invoicing to ~2,500 hospitals via Invoice Central (Oracle APEX); donors are unpaid volunteers |
| Training Services (redcrosslearningcenter.org) | $175.4M | Paid B2C/B2B certification checkout on Salesforce Commerce Cloud |
| Domestic Disaster Services | $0 (pure cost center, $591.7M expense) | N/A, disburses via prepaid Mastercard |
| International Services | $0 (pure cost center, $48.8M expense) | N/A, disburses 100% by wire |
| Contributions/Fundraising | $1,312.8-1,355.6M | Online card (USD only), phone, mail, text-to-give, chapter cash/check |
| Red Cross Store | Not separately disclosed | redcrossstore.org redirects to redcross.org/store, platform unconfirmed |

**Leadership and strategy themes:** Cliff Holtz (CEO since Jul 2024) and Carmel Darcy (CFO since 1999) lead an organization with no CTO or Chief Digital Officer, technology sits under CIO Ronnie Strickland and VP of Innovation Kathy Miu. Current stated priorities: disaster response at scale, "a safe and reliable blood supply," growth of Training Services, and international response across 30 countries. The clearest live strategic commitment is the LifeBlood Fund (Aug 17, 2026), $300M over five years for "expanded donor engagement, advanced technology and modernized facilities."

---

## 4. Financials

**10-year revenue trajectory** (Form 990 basis, FYE June 30, ProPublica/EIN 53-0196605):

| FY | Total revenue | YoY | Net income | Driver |
|---|---|---|---|---|
| 2016 | $2,618.2M | — | -$61.4M | |
| 2017 | $2,676.0M | +2.2% | -$132.6M | |
| 2018 | $3,608.0M | +34.8% | +$465.0M | Hurricanes Harvey/Irma/Maria + CA wildfires (Aug-Oct 2017); $691M combined hurricane relief raised |
| 2019 | $2,813.5M | -22.0% | -$123.7M | Reversal of 2018 disaster giving spike |
| 2020 | $2,839.4M | +0.9% | +$155.8M | Not a COVID donation surge, giving actually fell slightly |
| 2021 | $3,090.2M | +8.8% | +$294.2M | |
| 2022 | $3,182.2M | +3.0% | +$134.0M | |
| 2023 | $3,217.1M | +1.1% | +$246.0M | |
| 2024 | $3,804.4M | +18.3% | +$273.9M | Government-contract spike, not donations: government grants $539.6M vs $61.2M in FY2025; Hawaii paid ARC $350M for Maui wildfire sheltering through Jun 2024 |
| 2025 | $3,917.0M | +3.0% | +$631.1M | Private giving grew 58%, driven partly by Jan 2025 LA wildfires |

9-year CAGR is 4.6%, but two of the ten years are disaster-driven spikes; underlying growth is slower.

**Revenue composition, FY2025 (audited):** Biomedical Services 58.2% ($2,305.2M) + program materials 4.4% = 62.6% products and services. Corporate/foundation/individual giving 27.2%, legacies and bequests 3.2%, federal contracts 1.8%, donated services 1.6%. **The core finding: roughly 63% of Red Cross is a B2B blood-products business, not a donation business.** Private (non-government) contributions grew 58% year over year even as total contributions looked flat, masked by a government-grant collapse.

**Recent-months trend:** No quarterly reporting exists; FY2025 audited statements (issued Oct 21, 2025) are the latest hard numbers, FY2026 statements are not expected until roughly October 2026. Revenue +3.1%, expenses -6.7% (disaster-driven decline, not efficiency), net operating result nearly doubled. Headcount essentially flat (17,967 to 17,907). No restructuring or layoffs found for American Red Cross specifically. **Operational stress signal:** on July 27, 2026, Red Cross declared its second-ever national blood supply crisis, donations at a four-year summer low, directly threatening the 58% of revenue tied to Biomedical Services.

**Important disambiguation:** widely reported November 2025 headlines about "Red Cross cutting 2,900 jobs, 17% budget cut" refer to the Geneva-based ICRC (International Committee of the Red Cross), a completely separate legal entity with a different funding base (government-dependent). American Red Cross has announced no layoffs. Do not conflate these in the room.

**Last full year headline (FY2025):** Revenue $3,917.0M, net income $631.1M (15.9% operating margin, the strongest in the ten-year series), program expense ratio 91%, Charity Navigator Four-Star rating.

**Other material items:** Debt of $297.1M (down from $365.1M), fixed rate 0-3.83%, maturing through 2044, no public credit rating from Moody's/S&P/Fitch on the entity itself (historical bonds were insured by Ambac or backed by letters of credit from U.S. Bank and JPMorgan Chase, not rated on Red Cross's own credit; no new bond issuance since 2008). $200M undrawn committed credit lines, $52M unused letters of credit. Investment portfolio $3.08B, 67% cash equivalents. Pension essentially fully funded ($165K surplus). CEO Cliff Holtz total FY2025 compensation $989,075; CFO Carmel Darcy $570,214.

**So what for the call:** the B2B blood-product line that generates 58% of Red Cross's revenue is under acute, publicly declared stress, and the organization just committed $300M with executive and board-level sponsorship explicitly naming "advanced technology" as part of the response. That makes payments and billing modernization on the Invoice Central side a live, funded conversation right now, more so than the consumer donation side.

---

## 5. Competitive Landscape

Two distinct arenas. Blood/biomedical services (Red Cross's largest revenue line) and large-scale US charitable fundraising (its donation line). Share bases differ by arena and are labeled accordingly.

**Arena A: Blood and biomedical services** (denominator: 11.58M red blood cell units collected nationally in 2023, AABB National Blood Collection and Utilization Survey; revenue-panel shares below are derived by me across these named organizations only, not the full sector)

| Competitor | Est. market share (basis) | Scale (dated) | Differentiator | Payments posture |
|---|---|---|---|---|
| **American Red Cross** (incumbent) | ~40% self-reported, units basis; 45.5% derived, 7-org revenue panel | Biomedical revenue $2.1B FY2025, 4.7M units | Only national collector, single-source disaster surge capacity | Cybersource + Braintree, no orchestrator |
| Vitalant | No official share published; 16.0% derived, revenue-panel basis | $739.6M revenue FY2024 | Largest independent nonprofit collector | Not found (B2B hospital billing) |
| New York Blood Center Enterprises | No estimate available; 13.6% derived | $629.0M revenue FY2025 | Multi-region roll-up + research arm | Not found |
| Versiti | No estimate available; 9.8% derived | ~$454M FY2023 (summed operating entities) | Blood center + diagnostics + research | Not found |
| OneBlood | No estimate available; 9.8% derived | $450.7M revenue FY2024 | Dominant Southeast regional | Not found |
| CSL Plasma (CSL Behring) | Part of the big-four ~80% of US plasma centers by facility count | 300+ US centers; CSL Behring segment $11.16B FY2025 | For-profit paid-donor plasma model | Pays donors, prepaid/reloadable cards |
| Grifols (Biomat USA) | ~30% of US/Europe plasma centers by facility count | 300+ US centers | Largest plasma-center footprint | Pays donors |
| Bloodworks Northwest | No estimate available; 3.3% derived | $154.2M revenue FY2023 | Pacific NW regional | Not found |
| Cascade Regional Blood Services | Exited the market | Closed Feb 2024 after 80 years | Consolidation datapoint: sub-scale center could not survive | n/a |

**Where Red Cross sits:** the single largest collector by roughly 2.8x over the next competitor, but only about 40% of a market where the other 60% is a fragmented federation that collectively out-collects it. The dynamic has shifted from shortage to periods of oversupply and price competition; Red Cross has won hospital contracts by underbidding community centers in at least one documented case (Indiana), and Cascade Regional's 2024 closure is the same pressure ending in exit.

**Arena B: Large US charitable fundraising** (denominator: $592.5B total US giving in 2024, Giving USA 2025; shares below are derived by me, org contributions divided by that total; note that Feeding America, Direct Relief, Americares and World Vision book large gifts-in-kind that are not competing for the same cash donor dollar as Red Cross)

| Competitor | Est. market share (basis) | Scale (dated) | Differentiator | Payments posture |
|---|---|---|---|---|
| **American Red Cross** (incumbent) | 0.22% derived, cash contributions basis | Contributions $1,312.8M, total revenue $3,917M FY2025 | Majority earned-revenue (63%), not donation-dependent | Cybersource + Braintree, no orchestrator, confirmed via live code |
| The Salvation Army USA | Not derivable, files no public Form 990 (church-exempt) | ~$4.78B total revenue 2024 (secondary source, verify before quoting) | Largest US charity by revenue, thrift retail + kettle giving | Classy (GoFundMe Pro), DNS-confirmed |
| ALSAC / St. Jude | 0.41% derived | ALSAC revenue $2.687B FY2023 | Purest cash-fundraising machine in US philanthropy, Red Cross's closest true cash-donor competitor | **Identical stack to Red Cross**: Cybersource + Braintree + hand-rolled Apple Pay |
| Feeding America | 0.80% derived, but overstates cash competition roughly 10x (mostly donated food) | Total revenue $4.917B FY2023 | 200-food-bank federation, largest GIK operation | EveryAction/NGP VAN (Bonterra) + VGS tokenization. Adyen listed only as a $250K+ corporate donor, not a processor, correcting an earlier assumption |
| Direct Relief | 0.38% derived, mostly donated medicine | Total revenue $2.267B FY2023 | Pure GIK medical logistics | Classy (GoFundMe Pro), DNS-confirmed |
| World Vision US | 0.25% derived | Total revenue $1.510B FY2023 | Deepest recurring child-sponsorship billing book in the sector | Likely Classy, unconfirmed (403-blocked) |
| Doctors Without Borders USA | 0.13% derived | Total revenue $767.4M FY2023 | Refuses most government funding, benchmark for donor loyalty | Classy (GoFundMe Pro) + Braintree, DNS-confirmed |
| American Heart Association | 0.11% derived | Total revenue $925.8M FY2023 | Also Red Cross's direct competitor in the paid CPR/first-aid training market | Not found |
| Habitat for Humanity International | 0.05% derived | Total revenue $329.2M FY2023 | Volunteer-build model + ReStore retail | Blackbaud Luminate/Convio, DNS-confirmed |
| Team Rubicon | 0.007% derived | Total revenue $40.4M FY2023 | Small but a direct brand rival in disaster-fundraising narratives | Classy (GoFundMe Pro) |

**Where Red Cross sits:** market share is close to a meaningless frame here, the largest single US charity holds well under 1% of national giving. The real competition is for donor attention during disaster news cycles. Red Cross's structural peculiarity is that it is not primarily a donation business at all (63% earned revenue), unlike ALSAC/St. Jude (~90% contributed) which raises roughly 1.8x Red Cross's cash contributions with none of its earned-revenue base.

**For the call:** St. Jude/ALSAC, Red Cross's closest true fundraising competitor, runs the identical Cybersource plus Braintree plus hand-rolled Apple Pay stack, this is a category-wide pattern, not a Red Cross-specific oversight. Meanwhile Salvation Army, Direct Relief, MSF-USA, and Team Rubicon have all outsourced the problem to Classy, whose parent is GoFundMe. Yuno has an existing relationship in this exact vertical via GoFundMe (get permission before naming specifics externally per standing account rules).

---

## 6. Payments Money Map

**No orchestration layer exists anywhere in the Red Cross stack.** At least five disconnected payment surfaces confirmed via live technical inspection:

1. **Consumer donations** (redcross.org/donate): Braintree primary (Hosted Fields for cards, PayPal, Venmo, Google Pay via Braintree gateway, Apple Pay under Red Cross's own merchant ID `merchant.redcross.org.arcapplepay.prod`), plus a legacy Cybersource card vault. The application code contains a hand-written branch choosing between a Braintree nonce or a Cybersource token, confirmed hard evidence of homegrown orchestration logic they built and maintain themselves. A 16-character Cybersource token check silently disables the saved-card option and forces re-entry for some recurring donors, a real, evidenced churn leak on Monthly Giving. reCAPTCHA Enterprise and Cardinal Commerce (3DS) references are present in the code.
2. **Training/Store checkout** (redcross.org/take-a-class, /store): Salesforce Commerce Cloud (Demandware) with a Cybersource LINK cartridge; PayPal is routed through Cybersource rather than directly.
3. **B2B blood-product billing** (rcinv.redcross.org, "Invoice Central"): a self-hosted Oracle APEX portal serving the $2.3B Biomedical revenue line to ~2,500 hospitals. ACH plus card "if contractually allowed." "Quick Pay," a one-time no-login payment option, launched December 2025 but stores no credentials, customers re-key full card details on every invoice. Red Cross's own public FAQ still contradicts this, stating "we do NOT accept Credit Card payments online at this time." Also supports MOTO (phone) payment and EDI/cXML invoice delivery over customer SFTP.
4. **Domestic disaster payouts**: a prepaid Mastercard, the "Client Assistance Card," issued by U.S. Bank National Association under license from Mastercard. $236.0M disbursed this way in FY2025 to roughly 117,000 households.
5. **International disbursements**: 100% wire transfer, 49 of 49 grant line items in FY2025 and consistent across three years, zero ACH, EFT, check, or cash. Red Cross's own FY2025 Annual Report states it is "expanding cash and voucher assistance," and IFRC's own internal review of the Ukraine response called IFRC systems "a key blocker to rapid and scalable CVA delivery."
6. **Peer-to-peer/campaign giving** (give.redcross.org, redirects to raise.redcross.org): a third distinct surface, running on Classy (GoFundMe Pro) with its own stack, Stripe for cards, Braintree for PayPal/Venmo, Plaid for ACH, and TokenEx for vaulting. Confirmed via live page payload (83 classy.org references, Stripe error-handling code, Braintree PayPal logo assets, Plaid client name "GoFundMe Pro"). This is a third gateway combination alongside the Braintree-plus-Cybersource main donation form and the Cybersource-only Training/Store checkout.
7. **Crypto**: BitPay, hosted off-site, fee-free to Red Cross.
8. **Zelle**: disaster relief only, manual peer-to-peer via the donor's own bank app, not integrated into Red Cross's own stack.

**Fraud/3DS posture:** reCAPTCHA Enterprise on the donation checkout; Cardinal Commerce (3DS) referenced 98 times in the donation app bundle. Red Cross's own FAQ publicly lists false-decline causes including AVS mismatches, "you are currently outside of the US and/or using an international credit card," and its own fraud filters, a self-documented false-decline problem.

**Hiring signals:** confirmed live against Red Cross's Workday ATS (345 open roles as of Aug 31, 2026), zero roles matching payment, treasury, merchant services, PCI, or e-commerce keywords. One open Salesforce Solution Architect role (RC89499, posted Aug 15, 2026, $165-180K) is scoped entirely to Biomedical Services Salesforce work, not payments. A possibly-still-open Director of Marketing Technology Architecture role oversees fundraising-systems architecture (Adobe Experience Cloud plus Salesforce Marketing Cloud) but its live status could not be confirmed on the current board.

**Peer context:** St. Jude/ALSAC, Red Cross's closest fundraising peer, runs an identical Cybersource-plus-Braintree stack. Salvation Army, Direct Relief, MSF-USA, and Team Rubicon have all standardized on Classy (GoFundMe's platform).

**Framing rules for this account:** never suggest Red Cross lacks a payment method, nothing here indicates an APM gap. The story is consolidation, resilience, and speed, not deficiency. Lean into their own language ("advanced technology," LifeBlood Fund) rather than implying they're behind. Given the mission-driven, congressionally chartered context, keep tone peer-level and consultative, not aggressive growth-sales.

**Consumer donation methods-by-market:** effectively single-market. Red Cross explicitly states online donations process in USD only and lists international cards as a decline reason, there is no localized or multi-currency donation experience to reference.

---

## 8. News & Signals

**Last 7 days (rapport openers):**
- **Aug 27, 2026** — Nepal Red Cross responds to a devastating flash flood in Rasuwa District.
- **Aug 24, 2026** — Red Cross and Hello Kitty launch a blood-donor campaign (Sep 1-20); the release states the blood supply "continues to recover from critically low levels" but "remains vulnerable" into September.
- **Aug 24, 2026** — Red Cross assisting evacuees from the Hawk Wildfire near Reno, NV.
- **Aug 24, 2026** — National Preparedness Month coverage; September 2 (meeting day) is day two of the month.

**The dominant 2026 story, the blood crisis:**
- **Aug 17, 2026** — LifeBlood Fund launched: $300M over 5 years, co-chaired by Teresa and Byron Pollitt ($15M lead gift), explicitly citing "advanced technology" alongside donor engagement and modernized facilities.
- **Jul 27, 2026** — Second-ever national blood supply crisis declared in Red Cross's history (prior was Jan 2022); under one day's supply of type O positive.
- **Jul 13, 2026** — Emergency blood shortage declared after supply fell 25%.
- **Jan 20, 2026** — Severe shortage declared after supply fell 35% in one month.

Structural driver Red Cross publishes itself: donor base down 40% over 20 years, demand projected to rise 12% by 2030.

**Technology and digital signals:**
- **Jan 29, 2026** — Red Cross wins an AWS Nonprofit Imagine Grant (up to $200K plus credits) to prototype "Clara AI," a multi-agent gen-AI platform on Amazon Bedrock AgentCore spanning disaster relief, blood services, military family support, and training.
- **Dec 2025** — Invoice Central "Quick Pay" launches, the B2B card-acceptance modernization described above.
- FY2025 Annual Report notes Red Cross named a Fast Company "Best Workplace for Innovators," a GenAI exam-question pilot in Training Services, nationwide launch of the "Red Cross Delivers" blood-logistics app, and a new Humanitarian Services innovation incubator in Nashville covering fundraising.

**Partnerships:** Toyota ($1M, Aug 4, 2026), Farmers Insurance (Disaster Responder Program, Apr 2026), American Airlines (40-year partnership, Apr 2026), Uber (Disaster Responder Program, Mar 2026), Maja Kristin ($3M gift, Jan 2026).

**Important correction:** November 21, 2025 headlines about Red Cross cutting 2,900 jobs and a 17% budget reduction refer to the Geneva-based ICRC, not American Red Cross. Do not conflate.

---

## 9. Selling Yuno Here

**Core frame:** American Red Cross has already built, by hand, exactly the kind of orchestration logic Yuno sells (the Braintree/Cybersource token-selection code), is mid-flight on a B2B payments modernization with real executive sponsorship (Invoice Central, LifeBlood Fund), and has a board with unusually high payments literacy. This is a consolidation and resilience story, not a market-expansion story, and it is not the usual Yuno pitch, there is no cross-border APM gap to point to since the organization is 93.7% single-market. Lead with what their own code and their own public statements already say.

**Hooks with proof points:**
- Invoice Central modernization: a live, unfinished B2B payments build on the $2.3B blood-revenue line, direct opening to talk about vault-based card storage and unified reconciliation.
- Recurring-donor recovery: framed around Yuno's transaction recovery capability for failed or expired cards on Monthly Giving, distinct from the vault-forced-reentry issue but complementary. Proof points: Livelo (+5% approval, 50% recovery), Reserva (+4% approval in under 3 months).
- Real-time monitoring for disaster-driven traffic surges: Rappi (zero implementation time, 80% less analyst resolution time, millisecond-level detection versus 5-10 minutes manually) maps well to Red Cross's disaster-response donation spikes.
- GoFundMe reference: Yuno's first live Marketplace-solution merchant, a donation-platform analogue. Only the name is safe to use without clearance, architecture and volume details are internal per standing account rules, get explicit permission before naming specifics to this prospect.

**Landmines, what NOT to say:**
- Never suggest Red Cross lacks a payment method or APM, nothing in this research supports that and it would read as unresearched.
- Do not pitch cross-border APM expansion as a primary hook, Red Cross is 93.7% single-market and that framing will land as generic.
- Do not conflate ICRC's November 2025 layoffs/budget cuts with American Red Cross, different legal entity entirely.
- Do not treat Carlos as the economic buyer or push for a close, use the 30 minutes to map the real committee.
- Do not name GoFundMe specifics without clearing it first.
- No em-dashes, no " - " as punctuation, no "no small feat" in any written follow-up.

---

## 10. Be Ready For

| They may ask | Ready answer |
|---|---|
| What's your pricing model? | Standard Yuno positioning; defer exact figures to a follow-up with the actual budget holder once identified |
| How does this integrate with what we already have (Braintree, Cybersource, Salesforce Commerce, Oracle Invoice Central)? | Yuno sits above existing gateways via a single API; Braintree and Cybersource don't need to be ripped out on day one, Yuno can orchestrate across both immediately |
| We're a nonprofit and congressionally chartered, is this really something you sell to? | GoFundMe is Yuno's first live Marketplace/donation-platform merchant (name only, get clearance before sharing specifics); frame Yuno as proven for donation-driven platforms |
| What's your PCI/security posture? | Standard Yuno PCI DSS compliance answer; confirm current certification level with the team before the call if not already known |
| Do you have references? | GoFundMe (with permission), Reserva, Livelo |
| We already built custom logic to route between Braintree and Cybersource ourselves, why do we need you? | Frame as validation: they've already proven the orchestration need internally; Yuno replaces bespoke, hard-to-maintain code with a managed layer plus real-time monitoring and recovery capability they haven't built themselves |
| Who actually makes this decision here? | This is a discovery goal for the call itself, ask directly rather than assuming |

---

## 11. Agenda (30 minutes)

| Time | Block | Notes |
|---|---|---|
| 0:00-0:03 | Intros, rapport (LifeBlood Fund / blood crisis opener) | Notes: ____ |
| 0:03-0:08 | Confirm Carlos's actual role and scope (Merchant Services, which surfaces he owns) | Notes: ____ |
| 0:08-0:18 | Discovery questions (below) | Notes: ____ |
| 0:18-0:25 | Position Yuno with 1-2 hooks tailored to what's confirmed | Notes: ____ |
| 0:25-0:28 | Next steps, who else should be in the room | Notes: ____ |
| 0:28-0:30 | Wrap, confirm follow-up | Notes: ____ |

---

## 12. Discovery Questions

1. Can you walk me through your role and what "Merchant Services" covers here, given how many different collection surfaces Red Cross runs? Notes: ____
2. We noticed the donation checkout runs through Braintree with Cybersource also involved for saved cards, is that still accurate, and is anyone actively working on consolidating those? Notes: ____
3. How is the Invoice Central Quick Pay rollout going since December, and is there a plan to expand card acceptance further across your hospital and institutional customers? Notes: ____
4. Who owns the decision on payment processing here, is that inside your team, under Ronnie Strickland's IT organization, or under Finance with Carmel Darcy's team? Notes: ____
5. With the LifeBlood Fund naming "advanced technology" as part of the strategy, is payments infrastructure part of that roadmap, or is the technology focus elsewhere? Notes: ____
6. On the international side, cross-border disbursements appear to run entirely on wire transfer today, has speed or cost of those transfers come up as a pain point? Notes: ____
7. Is there a specific budget or initiative already underway that this conversation should plug into, or is this more exploratory right now? Notes: ____

---

## 13. Post-Meeting Checklist

- Send recap email same day
- Log outcome and any new facts (confirm Carlos's actual title/scope, confirm current PSP stack, identify real decision-maker) in memory
- Schedule the agreed next step
- Update project memory with what was learned

---

## Appendix — Sources

```
https://projects.propublica.org/nonprofits/organizations/530196605
https://www.redcross.org/about-us/who-we-are/governance.html
https://www.redcross.org/about-us/who-we-are/leadership.html
https://www.redcross.org/about-us/who-we-are/leadership/board-of-governors.html
https://www.redcross.org/content/dam/redcross/about-us/publications/2025-publications/2025-American-Red-Cross-Form-990.pdf
https://www.redcross.org/content/dam/redcross/about-us/publications/2025-publications/2025-Consolidated-Financial-Statement.pdf
https://www.redcross.org/content/dam/redcross/about-us/publications/2025-publications/510901-02-FY25-Annual-Report-EN-Final.pdf
https://www.redcross.org/about-us/news-and-events/press-release/2026/red-cross-launches-multi-year-fundraising-campaign-to-strengthen.html
https://www.redcross.org/about-us/news-and-events/press-release/2026/red-cross-declares-national-blood-supply-crisis-urges-immediate-.html
https://www.redcross.org/about-us/news-and-events/press-release/2026/red-cross-receives-aws-grant-to-prototype-aid-platform.html
https://www.redcross.org/about-us/news-and-events/press-release/2026/red-cross-and-hello-kitty-team-up-to-help-save-lives.html
https://www.redcross.org/invoice-central.html
https://www.redcross.org/faq.html
https://www.redcross.org/donate/donation.html
https://www.redcross.org/store
https://www.charitynavigator.org/ein/530196605
https://www.aabb.org/news-resources/news/article/2025/03/17/results-of-2023-nbcus-suggest-continued-stabilization-of-the-blood-supply
https://givingusa.org/giving-usa-2025-u-s-charitable-giving-grew-to-592-50-billion-in-2024-lifted-by-stock-market-gains/
https://www.feedingamerica.org/partners/food-and-fund-partners/guiding-partners
https://www.france24.com/en/europe/20251121-red-cross-to-shed-2-900-jobs-as-it-cuts-back-2026-budget
https://www.axios.com/2026/07/28/us-blood-supply-health-red-cross-donate
https://salesforce.org/stories/american-red-cross/
https://americanredcross.wd1.myworkdayjobs.com/American_Red_Cross_Careers
https://reliefweb.int/report/ukraine/ukraine-conflict-american-red-cross-leads-largest-cash-assistance-program-red-cross-history
```
