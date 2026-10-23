# BC Ferries (British Columbia Ferry Services Inc.) payments fact file

Research date: 23 Oct 2026. Scope: public facts only, for a short informational email and a general company deck. Every claim carries a URL, a quote or data point, and a date. Items that could not be verified from a primary or reputable source are marked UNVERIFIED. Nothing about Yuno's product is included here.

Budget log: 16/20 WebSearch calls used (all "standard" mode; four domain-restricted: procurement portals, bcferries.com, interac.ca, LinkedIn/ZoomInfo/TheOrg, BC news sites; one of the sixteen errored on a blocked domain and returned nothing). Primary sources fetched directly with curl or WebFetch: bcferries.com (home, /book-sailings/personal-travel, /payment-protection, /routes-fares/ferry-fares, /routes-fares/ferry-fares/experience-card, /travel-boarding/foot-passenger-check-in, /book-sailings/business-account-commercial-travel-services/ctc-card, /our-company/procurement, /our-company/leadership, /business-ops and /business-ops/competition/8803962892040, /travel-advisories/8800582315811, /login, /RouteSelectionPage, two JS bundles, the Fare Index PDF v26-05, the Fiscal 2026 Annual Report PDF, the FY2026 MD&A PDF, the Annual Report to the BC Ferries Commission PDF, the Strategic Plan June 2026 PDF, two news releases); CanadaBuys tender notice bcnrfp28-2026 and bcrfp25-2026; MERX public search listing; BC Ferries Commissioner site; interac.ca (two releases); Apple App Store listing; Times Colonist (four articles), Daily Hive, CHEK News, North Shore News, Foundation Magazine. Not reachable: BC Bid (Jaggaer portal behind a browser check and account), MERX abstract page (404/415 on all URL patterns tried), BIV (403), ZoomInfo (403).

Legend: [PRIMARY] company filing, company site, procurement portal, regulator or official doc. [PRESS] reputable trade or local press. [SNIPPET] only seen in a search-result snippet, page not fetched. [UNVERIFIED] could not confirm.

---

## 1. The open NRFP: "NRFP 28-2026 Electronic Payment Processing, Payment Gateway, Fraud Management, Wallet and Programs"

### 1.1 Notice facts (three public listings, all fetched 23 Oct 2026)

| Field | Value | Source |
|---|---|---|
| Exact title | "NRFP 28-2026 - Electronic Payment Processing, Payment Gateway, Fraud Management, Wallet and Programs" | [PRIMARY] CanadaBuys https://canadabuys.canada.ca/en/tender-opportunities/tender-notice/bcnrfp28-2026 ; identical title on BC Ferries https://www.bcferries.com/business-ops and on MERX |
| Solicitation number | "BCNRFP_28-2026" | [PRIMARY] CanadaBuys |
| Procurement type | "This Negotiated Request for Proposals (the "NRFP") is an invitation by British Columbia Ferry Services Inc. ("BC Ferries") to prospective Proponents to submit Proposals" | [PRIMARY] CanadaBuys description |
| Issuer | "British Columbia Ferry Services Inc" (CanadaBuys); "BC Ferry Services Inc", "British Columbia, CAN" (MERX) | [PRIMARY] |
| Publication date | CanadaBuys "Publication date 2026/10/06"; BC Ferries "Published: October 06, 2026"; MERX "Published 2026/10/07" | [PRIMARY] |
| Last amendment | "Last amendment date 2026/10/22" (CanadaBuys, page "Date modified: 2026-10-23") | [PRIMARY] |
| Status | "Open" (CanadaBuys, 23 Oct 2026); MERX listing "25 day(s) left" | [PRIMARY] |
| Closing date and time | CanadaBuys: "2026/11/17 17:00 EST"; BC Ferries: "Closing Date: November 17, 2026 / Closing Time: 2:00 PM Pacific Standard Time"; NRFP key dates: "Submission Deadline November 17, 2026, at 2:00 PM Pacific Time" | [PRIMARY] |
| MERX notice id | 444186922086 (listing row on https://www.merx.com/public/solicitations/open?keywords=NRFP%2028-2026 ); abstract page not retrievable without a MERX session | [PRIMARY] listing only |
| Where the documents are | "Organizations interested in reviewing the bid package must download the NRFP document, and choose the attachments listed under RFx Documents. Note that it is the Proponent's responsibility to check BC Bid for additional posted documents e.g., addendum and Q&A documents that may be issued up until the closing date and time." (CanadaBuys). BC Ferries page: "Organizations interested in reviewing the bid package are advised to visit the BC Bid Portal webpage here: BC BID and search for British Columbia Ferry Services Inc. under the organization field." | [PRIMARY] |
| Vendor registration | CanadaBuys: "Full details for this tender opportunity are available on a third-party site ... Note that on the third-party site you may need an account to view and/or bid on this tender." BC Bid itself redirected curl to a browser check page (https://bcbid.gov.bc.ca/page.aspx/en/bas/browser_check), so the RFx documents were not read. | [PRIMARY] for the account note; documents [UNVERIFIED] |
| Pre-qualification step | None mentioned in any of the three public notices. The NRFP schedule goes straight from submission to "Shortlisting of Proponents". | [PRIMARY] notice text; whether Appendix B adds one is [UNVERIFIED] |
| Contact named on the notices | CanadaBuys "Contracting authority: Jocelyn Lardizabal, Email: procurement@bcferries.com". BC Ferries page: "Primary contact: procurement@bcferries.com" (no person named). The BC Bid hyperlink on the BC Ferries page is an Outlook safelinks URL that embeds "Jocelyn.Lardizabal@bcferries.com" as the originating mailbox. | [PRIMARY] |
| "Phil Miller, Category Manager, Supply Chain" | Not named on CanadaBuys, MERX or bcferries.com. A ZoomInfo search snippet lists "Philip Miller ... Category Manager at BC Ferries" (Victoria address, start in 2025) with prior roles at PHSA (https://www.zoominfo.com/p/Phil-Miller/1536848529 , page returns 403). A LinkedIn profile for a Phil Miller shows "Category Lead II, Category Management - PHSA Procurement" (https://www.linkedin.com/in/philmiller2/ , not fetched). | [SNIPPET] for the ZoomInfo title; his role on this NRFP is [UNVERIFIED] (it would be inside the NRFP document on BC Bid) |
| Contact restriction | CanadaBuys boilerplate: "If you have questions about this tender opportunity, please contact the contracting officer, whose information is found in the Contact information tab." A sole-point-of-contact or no-lobbying clause is standard in BC Ferries NRFPs but was not visible on any public page. | [UNVERIFIED] |
| Incumbent named | Not named in the public notices. BC Ferries' own site states "Moneris is the company we use for payment processing" (see 2.2), so Moneris is the de facto processing incumbent. | [PRIMARY] for Moneris; notice wording [PRIMARY] |
| Contract duration | "Refer to the description above for full details." (no term stated publicly) | [PRIMARY] |
| Trade agreements | "Please refer to tender description or tender documents" | [PRIMARY] |
| Notice type / category | CanadaBuys "Notice type: Other"; search listing categorised the notice as "Services" | [PRIMARY] / [SNIPPET] |

### 1.2 Scope wording (verbatim, CanadaBuys description, 23 Oct 2026) [PRIMARY]

"BC Ferries is seeking Proposals from qualified Proponents for payment-related products, services, and capabilities to support BC Ferries' current and future payment ecosystem. The required services are intended to enable the secure, reliable, efficient, and cost-effective acceptance, processing, protection, management, and settlement of electronic payment transactions across BC Ferries' operational and customer-facing channels."

"BC Ferries seeks scalable, secure, compliant, and supportable solutions that meet current business requirements and provide the flexibility to support future business objectives, innovation, and technology modernization initiatives."

"The information contained in this NRFP is intended to assist Proponents in preparing their Proposals and is not intended to limit the scope of responses that may satisfy BC Ferries' requirements."

The Deliverables are "as further described in Appendix B of this NRFP". Appendix B sits on BC Bid and was not read.

What the public text does and does not say about channels:

| Item | In the public notice? |
|---|---|
| Electronic payment processing | Yes (title and description) |
| Payment gateway | Yes (title) |
| Fraud management | Yes (title) |
| Wallet(s) | Yes, "Wallet" in the title; "digital wallets" not spelled out |
| "Programs" | Yes, in the title; undefined publicly (could cover stored-value, gift or loyalty programs such as the Experience Card) [UNVERIFIED] |
| Settlement | Yes ("settlement of electronic payment transactions") |
| Channels | "operational and customer-facing channels" (unnamed) |
| POS / terminal acquiring, onboard, kiosks, vending, PIN pads | Not named publicly [UNVERIFIED]; note the separate POS RFP in 1.4 |
| Interac debit, tap-to-pay | Not named publicly [UNVERIFIED] |

### 1.3 Key dates (verbatim list from the notice) [PRIMARY]

"Issue Date of NRFP October 6, 2026 / Deadline for Questions October 28, 2026, at 2:00 PM Pacific Time / Deadline for Issuing Addenda November 4, 2026, at 2:00 PM Pacific Time / Submission Deadline November 17, 2026, at 2:00 PM Pacific Time / Rectification Period 5 Business Days / Shortlisting of Proponents Mid December 2026 / Anticipated Presentations Mid December 2026 – Early January 2027 / Anticipated Execution of Agreement By End of February 2027"

Reading (ours): questions close in five days (28 Oct 2026); anything sent after 4 Nov cannot change the documents; the award target is end of February 2027.

### 1.4 Related, already closed: "RFP 25-2026 Food and Retail Services Point of Sale Solution" [PRIMARY]

https://canadabuys.canada.ca/en/tender-opportunities/tender-notice/bcrfp25-2026 : solicitation BCRFP_25-2026, published 2026/05/29, closed 2026/07/06 17:00 EDT ("2pm Pacific Time"), last amended 2026/07/02, status "Expired", contracting authority "Kade Lentz", procurement@bcferries.com. BC Ferries "is seeking proposals for a modern Food and Retail Point of Sale Solution to support the future of onboard food and retail service delivery"; the solution should support "customer ordering, payment, kitchen coordination, retail operations, reporting, integrations"; "Any future expansion will be subject to BC Ferries' approvals, operational readiness, funding, and business needs." The notice does not mention PIN pads, Moneris or a payment processor. One business, IP Datapoint Solution, listed itself as interested in partnering. Award outcome: [UNVERIFIED].

### 1.5 Procurement page facts [PRIMARY]

https://www.bcferries.com/our-company/procurement (fetched 23 Oct 2026): "Supply Chain Management has a team of knowledgeable staff responsible for procurement, contract, inventory and logistics activities." ... "Email: procurement@bcferries.com" ... "Generally, phone quotations are sought for purchases of goods and services up to $25,000 and formal competitive bids are sought for purchases in excess of this value." Active competitions list at https://www.bcferries.com/business-ops (23 Oct 2026): NRFP 28-2026 (payments), RFQ 66-2026 (CNC plasma cutting tables), RFQ 70-2026 (anchor and chain), RFSQ 65-2026 (tail shaft support), RFSQ 24-2026 (water taxi services), 41-2025 (Baynes Sound Connector bull wheels). Supply Chain scale: a 2026 job posting for "Executive Director, Supply Chain" (Richmond) describes "over $500 million in annual spend" and about 65 staff (https://careers-bcferries.icims.com/jobs/4387/executive-director%2c-supply-chain/job , now HTTP 410) [SNIPPET].

---

## 2. Current payment acceptance (bcferries.com, fetched 23 Oct 2026)

### 2.1 Accepted methods by channel [PRIMARY]

Source unless noted: https://www.bcferries.com/book-sailings/personal-travel (section "Payment options").

| Channel | Verbatim | Reading |
|---|---|---|
| Terminal ticket booths (agents) | "Our ticket agents can accept these payment options: Debit / Visa / Mastercard / American Express / Google Pay and Apple Pay / Cash" and "Payment types accepted at the terminal ticket booths include Visa, MasterCard, American Express, Google Pay, Apple Pay, Cash, BC Ferries Experience™ Card and debit." | Full card, wallet, debit and cash acceptance at the booth; wallets are tap-to-pay on the PIN pad |
| Foot-passenger self-serve kiosks | personal-travel page: "Self-serve payment stations for foot passengers accept debit, credit card and Experience Cards." Foot-passenger page https://www.bcferries.com/travel-boarding/foot-passenger-check-in : "Self-serve kiosks accept debit, credit card, Google Pay, Apple Pay and Experience Cards." Same page lists accepted options as "Google Pay / Apple Pay / Cash and debit: Cash, Debit Interac / Credit cards: American Express ... / BC Ferries' card: Experience™ Card" | Kiosks at Swartz Bay, Tsawwassen, Horseshoe Bay, Departure Bay, Duke Point and Campbell River [SNIPPET for the terminal list]; northern terminals have no kiosks |
| Gift certificates | "Gift certificates can be used to purchase standard fares at the ticket booths. However, bookings and payment with a gift certificate must be made at the Terminal Administration office in advance of travel." Denominations "$10, $25, $50 and $100" (CTC page) | Offline redemption only |
| Online (bcferries.com and app) | "You can book online using the following payment options: Visa (including prepaid) / Mastercard (including prepaid) / Visa Debit and Debit Mastercard / American Express / BC Ferries Commercial Travel Card / BC Ferries Travel Card" and "The following payment options cannot be used for online bookings: Gift certificates / Experience Cards / Travel vouchers / TAP passes" | No Apple Pay, Google Pay, PayPal or Interac Debit listed for online; two house charge cards accepted online |
| Debit online | "At this time, debit cards that are not associated with Visa or Mastercard are not accepted for online bookings. You can use all debit cards regardless of the provider for payment of fares at terminals and for amenities on board." | Interac-only debit is terminal and onboard only |
| Card on file | "You can also save your Visa Debit and Debit Mastercard as payment options in your BC Ferries account, to load your BC Ferries Experience™ Card or Assured Loading Card and to purchase Gift Certificates. These cards are also available for bookings made over the phone through the Customer Service Centre." | Stored credentials exist in the BC Ferries account; phone channel (Customer Service Centre) takes cards |
| Booking fee only option | "When you book online, some routes offer the option of paying a booking fee only. If you just pay for the booking fee online, the remainder of your fare will be due at the ticket booth when you arrive at the terminal. For travel between Vancouver (Tsawwassen) and the Southern Gulf Islands and on our Northern routes, full pre-payment of fares is required at the time of booking." | Split payment across online and terminal on most routes |
| Refunds | "Refunds provided at terminals, on board ferries and over the phone will be credited back to the same form of payment used at the time of purchase." ... "Your fares and any booking fees will be automatically refunded to your original form of payment ... with the exception of a cash or cash equivalent transactions, which need to be processed by a ticket agent at the terminal." | Automated refunds to original tender |

Fare Index Version #26-05, "Effective June 16, 2026" (https://www.bcferries.com/web_image/h90/h4b/9089486028830.pdf , 41 pages) [PRIMARY]: "PAYMENT of FARES: - Cash, Debit Cards and BC Ferries ExperienceTM cards accepted at terminals - Visa, MasterCard, American Express accepted at terminals and for online bookings" and on several route pages "- Visa and MasterCard Debit Cards accepted for online bookings". "A 5% Fuel Surcharge will be applied at time of payment to the Net Fares listed above except on Stowage fare." "Customers looking to book ahead, but not prepay, can purchase a seprate [sic] reservation fee costing $20, and pay the At-Terminal tariff on departure".

### 2.2 Processor and gateway evidence

| Evidence | Verbatim | Source |
|---|---|---|
| Processor named by BC Ferries | "To provide you with additional payment protection while booking travel on bcferries.com and our mobile app, we recently introduced a feature called 3-D Secure – delivered by our payment partner Moneris." and "Moneris is the company we use for payment processing and 3-D Secure is a new credit card security measure we introduced on bcferries.com and the BC Ferries mobile app." | [PRIMARY] https://www.bcferries.com/payment-protection (fetched 23 Oct 2026) |
| 3DS version and date | "3-D Secure, version 2.0, was implemented on Saturday, October 28 on bcferries.com and the BC Ferries mobile app." (year not stated on the page; 28 October fell on a Saturday in 2023) ... "3-D Secure only impacts transactions made on bcferries.com or using the BC Ferries mobile app. This service does not impact purchases made with Experience Card either." ... "Canadian card providers vary in how often they require additional authentication on a transaction. BC Ferries does not have any control over how frequently this occurs" | [PRIMARY] same page |
| Script hosts on public pages | Home, /book-sailings/personal-travel, /login and /RouteSelectionPage reference only: www.bcferries.com, mtm.bcferries.com (tag-manager container `mtm.bcferries.com/js/container_hLWMAkCe.js`), www2.gov.bc.ca, play.google.com, apps.apple.com, toolbox.marketingtools.apple.com, youtube, linkedin, facebook, twitter, instagram, cansme.ca. The login page contains the string "recaptcha" twice. | [PRIMARY] curl 23 Oct 2026 |
| Vendor strings absent | The two storefront bundles `/_ui/responsive/js/common.min.js` (954 KB) and `/_ui/responsive/js/jsLibrary.min.js` (1.15 MB) and the four pages contain none of: moneris, paymentech, globalpay, elavon, adyen, js.stripe, braintree, cybersource, bambora, worldline, nuvei, payfirma, forter, kount, signifyd, siftscience, riskified, accertify, cardinalcommerce, songbird, threeds. The card-entry step sits inside an authenticated booking session and was not fetched, so the Moneris integration mode (hosted tokenization vs. server-side API) is [UNVERIFIED]. | [PRIMARY] for the absence on public pages |
| Storefront platform | Page assets under `/_ui/addons/bcfassistedservicesstorefront/`, `/_ui/addons/smarteditaddon/` and `smartedit` markers on home and booking pages: the booking site runs on SAP Commerce (Hybris) with the Assisted Service and SmartEdit addons. | [PRIMARY] observed markup; reading is ours |
| In-person stack (2019 interview) | "Moneris: PIN pad payment provider"; Acceo TenderRetail integrates Micros with Moneris; Oracle/Micros is the onboard POS; PR Bridge Systems supplies the cellular/LTE payment-gateway modems; TELUS (LTE, southern routes) and Infosat (satellite, northern routes) for connectivity; "it is not possible to accept debit card transactions when off-line"; payment mix after the debit rollout "20 per cent debit card, 50 per cent credit card and 30 per cent cash". Quoted: Erwin Martinez, then Chief Information Officer. | [PRESS] Foundation Magazine, "BC Ferries sets sail with advanced payments", 9 Aug 2019, https://foundationmag.ca/bc-ferries-sets-sail-with-advanced-payments/ |
| Debit and tap at booths | "B.C. Ferries passengers will be able to use debit cards at both vehicle and foot passenger ticket booths starting in March 2020." ... "Passengers will also be able to use Apple Pay and Google Pay on smartphones, B.C. Ferries spokesperson Tessa Humphries said. New PIN pads are being installed throughout B.C. Ferries operations this spring" ... "the tap option, which has a $100 limit." ... "B.C. Ferries starting offered a debit option on ferries in fall 2018." | [PRESS] Times Colonist, 2 Mar 2020, https://www.timescolonist.com/business/starting-this-month-youll-be-able-to-use-your-debit-card-at-bc-ferries-ticket-booths-4679500 |

Reading (ours, not a company statement): one acquirer, Moneris (RBC/BMO joint venture), serves e-commerce, app and terminal PIN pads; 3DS2 is issuer-triggered and Moneris-delivered; no third-party fraud tool, orchestration layer or alternative gateway is visible on the public site; wallets are accepted on PIN pads but not online; Interac-only debit is excluded online. The NRFP title ("Payment Gateway, Fraud Management, Wallet") maps onto those three gaps.

### 2.3 Stored value and house cards [PRIMARY]

| Product | Verbatim | Source |
|---|---|---|
| Experience Card | "The BC Ferries Experience™ Card is an electronic swipe card similar to a gift card that you can use to pay for ferry travel on a number of coastal routes." ... "cardholders must have their physical card in their possession and visible at time of payment." ... "You cannot use your Experience Card to make online bookings or for onboard purchases." ... "Effective April 15, 2026, the minimum amounts are: $50 minimum when loading at a ticket booth, online or at a self-serve foot passenger kiosk ... $130 minimum when loading at a ticket booth / $100 minimum when loading online or at a self-serve foot passenger kiosk" ... "Auto Load requires a valid credit card number." ... "The funds on your card never expire ... Funds loaded onto your Experience Card are non-refundable." ... "Share your balance when you add secondary cards" | https://www.bcferries.com/routes-fares/ferry-fares/experience-card (fetched 23 Oct 2026) |
| Experience Card discount | "savings between 13% and 40% on personal vehicles and passenger fares on select routes" | Annual Report Fiscal 2026, p. 20 |
| Commercial Travel Card (CTC) | "Each card on your CTC account acts as a charge card, which can be used to make bookings online or by phone, or for standby travel at terminals. Invoices must be paid in full when due as per contractual agreement." ... "Stay up-to-date with weekly invoices every Wednesday" ... "you can apply for a Travel Card (TC) account and have it linked to your CTC account" | https://www.bcferries.com/book-sailings/business-account-commercial-travel-services/ctc-card |
| Assured Loading Card | Loadable from a saved Visa Debit / Debit Mastercard in the account (personal-travel page) | personal-travel page |

### 2.4 Fees that ride on the payment flow (https://www.bcferries.com/routes-fares/ferry-fares , fetched 23 Oct 2026) [PRIMARY]

"Fares effective April 8, 2026". "As of October 15, 2025, all customers travelling by vehicle from Horseshoe Bay to Nanaimo (Departure Bay) will need to book and pay in advance, in one direction only." Southern Gulf Islands and North Coast: "Fares are paid in full at the time of booking, (no separate reservation fee applies)." "A non-refundable $5 change fee is applied each time you make a change to your booking's date, time or sailing." Cancellation fees: "$15" (SGI to Tsawwassen within 7 days), "$25" (Tsawwassen to SGI), "$60 cancellation fee will apply ($30 for Haida Gwaii routes)" within 30 days on North Coast. No-show fees: "$25", "$15", "For unredeemed Saver fare bookings, a $30 no-show fee will apply. For unredeemed Prepaid fare bookings, a $20 no-show fee will apply." Reservation-only fee "$20" (Fare Index). Temporary fuel surcharge "5%" from 16 June 2026 (Fare Index; MD&A p. 6: "Effective June 16, 2026, a temporary surcharge of 5% was implemented on all routes").

### 2.5 The app [PRIMARY]

Apple App Store, "BC Ferries" by BC Ferry Services Inc., https://apps.apple.com/us/app/bc-ferries/id6444454630 (fetched 23 Oct 2026): version 6.0.7 dated "May 21" (year not shown), 35.3 MB, 18 ratings averaging 2.2/5. Description: "Introducing a new travel resource for planning and booking personal ferry travel"; features "Express book", change/cancel bookings, foot-passenger bookings, accessibility requests; account creation, commercial, group and vacation bookings "require visiting bcferries.com". The description does not mention Apple Pay, saved cards or the Experience Card. The 3-D Secure page confirms the app takes card payments (see 2.2).

---

## 3. Scale, finances, digital posture, leadership

### 3.1 Fiscal 2026 (year ended 31 Mar 2026) by the numbers

| Metric | Value | Source |
|---|---|---|
| Passengers | "23.3M customers, up from 22.7 million in fiscal 2025" | [PRIMARY] Annual Report Fiscal 2026, p. 13, https://www.bcferries.com/web_image/h22/h9f/9110805250078.pdf (86 pages; landing page https://www.bcferries.com/bc-ferries-annual-report) |
| Vehicles | "10.0M vehicles, up from 9.7 million in fiscal 2025" | [PRIMARY] same |
| Traffic growth | "3.1% increase in vehicle traffic and 2.6% increase in passenger traffic, compared to the previous fiscal year" | [PRIMARY] Annual Report to the BC Ferries Commission, 29 Jul 2026, p. 4, https://www.bcferries.com/web_image/hd3/h68/9097126346782.pdf |
| Sailings / round trips | "197,809 sailings (196,465 in fiscal 2025)"; "91,275 round trips, 2,690 more than the annual number contractually required"; "about 542 each day" | [PRIMARY] Annual Report pp. 5, 13, 23 |
| Daily averages | "moving over 62,000 customers and 23,000 vehicles on average each day" | [PRIMARY] Strategic Plan, June 2026, p. 23, https://www.bcferries.com/web_image/h27/h0e/9093773754398.pdf |
| Network | "37 vessels operating on 25 routes out of 47 terminals spread over 1,600 kilometres of coastline" | [PRIMARY] MD&A FY2026 (dated 18 Jun 2026), p. 3, https://www.bcferries.com/web_image/hcb/h55/9091176857630.pdf |
| Employees | "our 5,000-plus employees" | [PRIMARY] Annual Report, Chair and CEO message, p. 2 |
| On-time performance | "86.1% ... up from 84.0%" | [PRIMARY] Annual Report p. 13 |
| Capacity utilisation | "67.9% vehicle capacity utilization system wide, up from 66.6%" | [PRIMARY] same |
| Total revenue | "Total revenue 1,259.8" ($ millions; 1,171.4 in FY2025; +8%) | [PRIMARY] MD&A p. 16 |
| Direct route revenue | "Direct Route Revenue 907.8 (862.3, +5%)": "Total vehicle tariff revenue 546.3", "Total passenger tariff revenue 256.0", "Total net retail revenue 74.2" | [PRIMARY] MD&A p. 16 |
| Tariff revenue (regulatory view) | "$802.3 million total passenger and tariff revenue"; regulatory table "Tariff Revenue 802,275" and "Ancillary Revenue 91,478" ($ thousands) | [PRIMARY] Annual Report to the Commission pp. 4, 41 |
| Indirect route revenue | "Indirect Route Revenue 349.0 (305.3, +14%)" incl. "Federal-Provincial subsidy 37.8"; ferry transportation fees from the Province "193,990" ($ thousands) | [PRIMARY] MD&A p. 16; Commission report p. 41 |
| Net earnings | "net earnings of $6.5 million was a $78.2 million improvement compared to our net loss of $71.7 million in the prior year" | [PRIMARY] MD&A p. 10 |
| Average tariffs | "Average vehicle tariff 54.79 (52.84)"; "Average passenger tariff 10.99 (10.74)" (dollars) | [PRIMARY] MD&A p. 17 |
| Food and retail | "$76.5M in food and retail revenue (after costs), up from $73.3 million" | [PRIMARY] Annual Report p. 13 (MD&A reports net retail revenue as 74.2; different measures) |
| Saver fares | "Approximately 1.4 million Saver fares were sold for sailings between Metro Vancouver and Vancouver Island last year, representing 32% of total vehicles travelling on those routes, up from 24% in fiscal 2025." ... "In July and August 2025, sailings on Routes 1, 2 and 30 averaged 92% full capacity" | [PRIMARY] Annual Report p. 20 |
| Customer Service Centre | "473,861 calls responded by Customer Service Centre"; "each call was answered within an average of 151 seconds"; "95% satisfaction with Customer Service Centre experience" | [PRIMARY] Annual Report p. 69 |
| Customer satisfaction | "86% customer satisfaction, up from 84%"; "4.8 customer complaints per 10,000 passengers, down from 5.9" | [PRIMARY] Annual Report p. 69 |
| Capex | "Capital Expenditures by Fiscal Year ($ millions) 2026 / 2025: ... Information technology 21.6 / 11.3 ... Total 436.9 / 276.9" | [PRIMARY] MD&A p. 24 |
| Online vs terminal share of fare revenue | Not published in the Annual Report, MD&A or Commission report. | [UNVERIFIED] |
| Payment-mix split (debit/credit/cash) | Only the 2019 interview figure (20/50/30) exists; no current figure published. | [PRESS] 2019; current [UNVERIFIED] |
| Tariff increases | "On April 1, 2025, BC Ferries implemented average tariff increases of 3.2%" and "On April 8, 2026, BC Ferries implemented average tariff increases of 3.2%" | [PRIMARY] MD&A p. 4 |

### 3.2 Digital and booking statements (verbatim)

| Statement | Source |
|---|---|
| "costs rose faster than revenues across much of the ferry system — a trend anticipated to continue" | [PRIMARY] Annual Report, Chair and CEO message |
| "On the technology side, we are modernizing our enterprise data and analytics capabilities and continuing the transition to cloud-based technologies across key systems." | [PRIMARY] Annual Report p. 32 |
| "$22 million in information technology and operations systems related improvements" (FY2026 capital) | [PRIMARY] Annual Report p. 25 |
| Strategic Plan June 2026, Goal 1: "modernizing older technology platforms that support the business"; "Modernize our enterprise data and business intelligence capabilities" | [PRIMARY] Strategic Plan pp. 14-15 |
| Strategic Plan June 2026, Goal 5 "Champion end-to-end customer experience", transformational priorities: "Simplify our booking processes, including for advance bookings"; "Explore new and expanded reservation strategies to improve travel certainty and expand affordable fare options"; "Identify solutions to reduce traffic congestion in terminal pre-ticketing areas" | [PRIMARY] Strategic Plan p. 23 |
| Booking alerts: "more than 429,000 total subscriptions, 138,000 unique subscribers and over 26% of subscribers successfully securing space on a previously sold-out sailing"; released in fiscal 2026 on Horseshoe Bay-Departure Bay, Horseshoe Bay-Langdale and Powell River-Comox, "with plans to expand to Tsawwassen-Swartz Bay and Tsawwassen-Duke Point in fiscal 2027" | [PRIMARY] Annual Report p. 73 |
| Waitlist: "a waitlist app pilot launched in early fiscal 2027 on Route 17 (Powell River-Comox) ... Between April 2026 and August 2026, over 5,000 people travelling with vehicles joined the waitlist, with 21% promoted to a confirmed booking." | [PRIMARY] Annual Report p. 73 |
| "More comprehensive end-to-end customer experience transformation will continue to be paced over the longer term, aligned with funding, asset renewal and workforce priorities." | [PRIMARY] Annual Report p. 70 |
| Horseshoe Bay booking-only: "on-time performance at Horseshoe Bay has risen from the mid-70% range to consistently above 90%" | [PRIMARY] Annual Report p. 71 |
| Booking-alert launch release, 10 Oct 2025, quoting Melanie Lucia, Vice President of Customer Experience: "This new tool is designed to help customers stay informed and act quickly if space becomes available." | [PRIMARY] https://www.bcferries.com/news-releases/bc-ferries-rolling-out-new-tool-to-improve-travel-planning-ahead-of-changes-at-horseshoe-bay |
| Current e-commerce platform history: "B.C. Ferries introduced a new mobile-friendly website Tuesday" ... "multi-year, multi-million dollar digital initiative" ... "The overall cost was about $29 million, with $11 million going to the development of the new website. That includes not only the website, but other systems such as a new e-commerce platform ... its reservation system, booking" (Tessa Humphries, spokesperson) | [PRESS] Times Colonist, 23 Sep 2020, https://www.timescolonist.com/local-news/bc-ferries-introduces-mobile-friendly-website-4684218 |
| Earlier reservation-model intent: "Under this model, reservations would be paid in full prior to boarding with no extra reservation fee." (Darin Guenette, manager of public affairs; article undated on the page, pre-2020) | [PRESS] CHEK, https://www.cheknews.ca/changes-coming-to-bc-ferries-reservation-system-497029/ |
| Cybersecurity: "Threat and risk assessments are conducted for new IT systems, and incident response processes are supported by external response specialists." | [PRIMARY] MD&A p. 45 |
| Revenue recognition: "We recognize revenue from vehicle fares, including reservation fees, passenger fares and fuel surcharges (rebates), when transportation is provided ... Prepayments for fares received in advance of providing transportation are included in the statement of financial position as contract liabilities" | [PRIMARY] MD&A p. 49 |
| PT7 filing: release dated 1 Oct 2026; PT7 covers "April 1, 2028 to March 31, 2032"; "Preliminary price cap determination expected by March 31, 2027"; "Final price caps by September 30, 2027" | [PRIMARY] https://www.bcferries.com/news-releases/bc-ferries-files-performance-term-seven-submission |

### 3.3 Leadership (https://www.bcferries.com/our-company/leadership , fetched 23 Oct 2026) [PRIMARY]

| Name | Title (verbatim) | Relevant detail |
|---|---|---|
| Nicolas Jimenez | "President & Chief Executive Officer" | "Since joining in 2023"; "almost 20 years at ICBC ... including five years as President and CEO"; boards: Interferry, Canadian Ferry Association |
| James Tan | "Vice President & Chief Information Officer" | "joined BC Ferries in July 2023"; ex-ICBC "Vice President, Claims Customer & Material Damage Services"; ex-Accenture and Ernst & Young |
| Dallyn Willis | "Vice President & Chief Financial Officer" | "oversees our financial, supply chain and commercial services groups. This includes teams responsible for treasury, forecasting and analysis, capital planning, accounting and reporting, internal audit, insurance and risk, payroll and benefits, procurement, materials management"; joined 2025, ex-Western Forest Products |
| Melanie Lucia | "Vice President, Customer Experience" | "responsible for the customer experience across our 47 terminals, catering operations on 22 vessels, our food and retail services and our call centre"; 35+ years at BC Ferries |
| Brian Anderson | "Vice President, Strategy & Planning" | ex-BC Transit VP Finance and COO |
| Lindsay Matthews | "Vice President, Public Affairs & Marketing" | ex-ICBC |
| Jason Boyd | "Vice President, Marine Operations" | ex-Canadian Navy |
| Stephen Jones | "Vice President, Engineering" | |
| Cameron Brine | "Vice President & Chief People Officer" | |
| Cathy McLay | Board Chair | ex-CFO TransLink |
| Director of Payments / Treasury / Revenue Systems | No public page or profile found. | [UNVERIFIED] |
| Jocelyn Lardizabal | "Contracting authority" on the NRFP (CanadaBuys) | title not published |
| Kade Lentz | "Contracting authority" on RFP 25-2026 (CanadaBuys) | title not published |
| Erwin Martinez | CIO in 2019 (Foundation Magazine) | no longer listed on the executive page |

Head office: Victoria, BC ("Sidney, BC V8L 3S8" is the Retail department mailing address on the procurement page). Procurement job postings are in Richmond and Victoria [SNIPPET].

---

## 4. Context: Canadian payment specifics, outages, regulation

### 4.1 Canadian specifics

| Fact | Verbatim | Source |
|---|---|---|
| Interac Debit online and in-app | "Interac Debit for In-App and In-Browser Payments with Apple Pay™ and Google Pay™ is now widely available" (Toronto, 15 Oct 2019); enabled with "acquirer Moneris" and "acquirer Everlink and payment service provider Adyen Canada Ltd."; "near real-time payments with no chargebacks" | [PRIMARY] Interac, https://www.interac.ca/en/content/business/interac-debit-for-in-app-and-in-browser-payments-expands-in-canada/ |
| Interac Debit via Stripe | "Stripe can now offer its customers Interac Debit for online and in-app purchases through participating digital wallets." ... "Previously, Stripe customers could only offer Interac Debit for in-person payments at physical stores." (10 Feb 2026); Interac products used "over 20 million times a day on average"; "nearly 300 financial institutions" | [PRIMARY] Interac, https://www.interac.ca/en/content/news/interac-debit-is-now-available-for-online-and-in-app-payments-with-stripes-customers/ |
| BC Ferries today | Online: "debit cards that are not associated with Visa or Mastercard are not accepted for online bookings"; wallets (Apple Pay, Google Pay) accepted at booths and kiosks only; Visa Debit and Debit Mastercard accepted online. Interac e-Transfer not mentioned anywhere on bcferries.com pages fetched. | [PRIMARY] bcferries.com (see 2.1) |
| Moneris | "a joint venture between Royal Bank and BMO Bank of Montreal"; "Moneris says it supports about 325,000 merchant locations across Canada." | [PRESS] Times Colonist, 24 Sep 2023 |

### 4.2 Payment and booking outages on record

| Date | What happened (verbatim where possible) | Source |
|---|---|---|
| 14 Jul 2026 | BC Ferries travel advisory "Point of Sale System Outage", posted Tuesday, July 14, 2026: point-of-sale disruptions "at many terminals, vessels, and the Customer Service Centre" due to "an issue with the server"; payment "limited to cash only until further notice"; customers "can still book and manage reservations through the BC Ferries website and mobile app". Duration and root cause: not published. | [PRIMARY] https://www.bcferries.com/travel-advisories/8800582315811 ; duration [UNVERIFIED] |
| 10 Apr 2024 | "A 'local power interruption' was to blame for the service issues related to debit and credit card payments" at Swartz Bay; "Cash was still accepted"; "The Swartz Bay terminal experienced a similar outage last month that forced crews to accept cash payments only." | [PRESS] CHEK, 10 Apr 2024, https://www.cheknews.ca/debit-credit-payment-restored-at-swartz-bay-following-power-interruption-bc-ferries-1198810/ |
| 26 Sep 2023 | "Check-in at B.C. Ferries terminals was delayed again Tuesday morning as the company experienced problems processing debit and credit card transactions at terminals." ... "the problem was due to 'an internal technical change' that affected communication between the corporation's point-of-sale systems and its payment processor." ... "Prepaid bookings, Experience cards, commercial-travel cards and assured-loading cards were not affected." BC Ferries on X: "Cash, Experience Card and Assured Loading Ticket customers are unaffected." Spirit of British Columbia "departed 39 minutes behind schedule". | [PRESS] Times Colonist, 26 Sep 2023, https://www.timescolonist.com/local-news/payment-problems-cause-delays-again-for-bc-ferries-7600455 ; Daily Hive, 26 Sep 2023, https://dailyhive.com/vancouver/payment-system-outage-bc-ferries |
| 23 Sep 2023 | "a fleetwide payment system disruption that forced employees to manually process all credit card and debit card payments" ... "The issue — a problem with third-party operator Moneris — was first reported by B.C. Ferries around 9:45 a.m. and resolved by 11:20 a.m., said B.C. Ferries spokesperson Karen Johnston." ... Queen of New Westminster's 10 a.m. sailing "departed for Tsawwassen 34 minutes late". Moneris: "the outage lasted about 90 minutes"; "There are no indications this appears to be cyber-attack related". | [PRESS] Times Colonist, 24 Sep 2023, https://www.timescolonist.com/local-news/bc-ferries-delays-expected-as-payment-processing-system-goes-down-7590305 |
| 20 Sep 2023 | Spirit of Vancouver Island, 7 p.m. Swartz Bay to Tsawwassen: "the vessel's point of sale machines malfunctioned"; "meals could only be purchased through cash and that B.C. Ferries would be offering free beverages" | [PRESS] North Shore News / Times Colonist, 20 Sep 2023, https://www.nsnews.com/bc-news/cash-only-for-meals-as-payment-machines-fail-on-bc-ferries-vessel-free-beverages-offered-7577682 |
| 8 Jul 2022 | Rogers national network outage affected BC Ferries debit and credit payments; BC Ferries asked passengers to carry cash | [SNIPPET] CTV / CHEK, https://beta.ctvnews.ca/local/vancouver-island/2022/7/8/1_5980024.amp.html |
| Jul-Aug 2022 | Online reservation system down several times over the July long weekend and crashed again on a busy August day (CTV) | [SNIPPET] https://bc.ctvnews.ca/bc-ferries-website-booking-systems-down-for-hours-due-to-technical-difficulties-1.5633780 |
| 2025-2026 online booking outages | None found in press for 2025 or 2026; the July 2026 event was POS-side with online unaffected. | [UNVERIFIED] absence |

### 4.3 Regulator and contract

| Fact | Verbatim | Source |
|---|---|---|
| Governance | "BC Ferries is an independent, regulated ferry service contractor that serves the public interest according to the Coastal Ferry Services Contract, the Coastal Ferry Act, and the oversight of the British Columbia Ferries Commissioner." ... "the Coastal Ferry Act converted BC Ferries from its status as a Crown corporation to a private company and created our parent company and sole voting shareholder, the B.C. Ferry Authority." | [PRIMARY] https://www.bcferries.com/our-company/leadership |
| What the price cap covers | The cap applies to vehicle fares, passenger fares and reservation fees: "the maximum allowable annual increase in average fares that BC Ferries is permitted to charge". "It does not apply to other customer fees, like fuel surcharges, food services, parking or retail." | [PRIMARY] BC Ferries Commissioner, https://www.bcferrycommission.ca/commissioner-decisions/price-cap-determinations/how-is-the-price-cap-determined/ |
| Current term | PT6, 1 Apr 2024 to 31 Mar 2028, price cap 3.2% per year; "Effective April 1, 2024, the CFSC was amended for PT6, formalizing ferry transportation fees for the four-year term" | [PRIMARY] Commission report p. 41; [PRESS] Marine Log / BIV for the 3.2% (consistent with MD&A tariff increases) |
| Fuel surcharges | "as authorized by the Commissioner, the Company collects fuel surcharges or provides fuel rebates" | [PRIMARY] Commission report p. 41 |
| Does the CFSC or the Commissioner regulate payment-processing fees or card surcharges? | Nothing found; the price cap counts reservation fees as fares, so any new reservation or booking fee is inside the cap, while payment-processing costs are an operating cost with no public ruling found. | [UNVERIFIED] |
| Essential service | "designated by the provincial government of British Columbia ... as an essential service for the purposes of the provincial Labour Relations Code" | [PRIMARY] MD&A p. 3 |
| Workforce | "Approximately 80% of BC Ferries' workforce are members of the BC Ferry & Marine Workers' Union" | [PRIMARY] MD&A p. 19 |

---

## Takeaways for the email (facts only)

- The NRFP covers "Electronic Payment Processing, Payment Gateway, Fraud Management, Wallet and Programs" for "acceptance, processing, protection, management, and settlement of electronic payment transactions across BC Ferries' operational and customer-facing channels"; questions close 28 Oct 2026 2:00 PM PT, submissions 17 Nov 2026 2:00 PM PT, award targeted by end of February 2027, with shortlisting and presentations in mid-December to early January.
- Documents live on BC Bid (account needed); the only published contacts are procurement@bcferries.com and contracting authority Jocelyn Lardizabal; Phil Miller is not on any public notice.
- BC Ferries names Moneris as "the company we use for payment processing" and the deliverer of 3-D Secure 2.0 on bcferries.com and the app; no other gateway, fraud or orchestration vendor is visible in the site's script hosts or JS bundles.
- Online acceptance today is Visa, Mastercard, Visa Debit, Debit Mastercard, Amex and two house charge cards; Apple Pay and Google Pay are accepted only at booths and kiosks, and Interac-only debit is not accepted online.
- Scale: 23.3M passengers, 10.0M vehicles, 197,809 sailings, $1,259.8M total revenue, $802.3M tariff revenue, 37 vessels, 25 routes, 47 terminals (FY2026, year ended 31 Mar 2026); IT capex doubled to $21.6M.
- Outages on record: Moneris network outage 23 Sep 2023 (fleetwide manual processing), POS-to-processor link failure 26 Sep 2023, Swartz Bay power interruption Apr 2024, and a POS server outage on 14 Jul 2026 that made many terminals, vessels and the Customer Service Centre cash-only while online booking kept working.

Budget log: 16/20 WebSearch calls used; roughly 25 WebFetch calls and about 45 curl fetches; no WebSearch calls remain reserved.
