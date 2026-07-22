# American Airlines | SDR Research Brief
*Yuno Payment Orchestrator · Framework v8.0 · Generated 2026-07-22*

**Company:** American Airlines Group Inc. (NASDAQ: AAL) · aa.com · Fort Worth, TX
**Analyst note:** aa.com, saleslink.aa.com, aavacations.com and aacargo.com all return HTTP 403 (Akamai Bot Manager) to automated fetches. Every aa.com claim below was retrieved live through a text proxy that returned HTTP 200 with full server-rendered page copy, so the evidence is first-party AA page text. Source-code-level PSP fingerprinting was not possible.

---

## EXECUTIVE SUMMARY

American Airlines is the world's largest airline by fleet, passengers carried and revenue: $54.6B in FY2025 (record), 224 million passengers boarded, service to over 350 destinations in more than 60 countries. Its FY2025 10-K discloses, in the plural, that it holds agreements with "companies that process customer credit card transactions," and that those processors can impose holdbacks of "up to and including 100% of relevant advanced ticket sales" against a $7.16B air traffic liability, yet **no processor, gateway, acquirer or orchestrator is named in any AA filing or public page**, and SEC full-text search returns zero hits for every major PSP name.

The commercially decisive finding is not an APM gap claim, it is AA's own published checkout policy: fares are recalculated in local currency for exactly **six markets** (Brazil, Canada, Colombia, Chile, Mexico, UK), so **every other market in the world is billed USD cross-border**; and **only one card can be used per booking on aa.com**. Both are verbatim from AA's own FAQ. Layer on five straight years of dated, still-live decline and stored-value redemption complaints, and the structural picture is a card-centric, POS-gated checkout without a routing layer.

Yuno's opportunity: an orchestration layer above AA's existing (unnamed, plural) acquirers to lift cross-border authorization outside the six local-currency markets, cascade the declines that today end in "call reservations," and add local rails per market without a per-provider integration project. Direct competitive pressure is already public: **Southwest Airlines, Virgin Atlantic, Avianca, GOL, Cebu Pacific and Riyadh Air all run a third-party payment orchestrator (CellPoint Digital)**. American does not, as far as public evidence shows.

---

## SECTION 1 — Traffic by Country

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source URL |
|---|---|---|---|---|---|
| 1 | United States | 91.26% | ~51.7M | Down 4.57% MoM | https://www.similarweb.com/website/aa.com/ |
| 2 | Brazil | 1.02% | ~0.58M | Up 64.23% | https://www.similarweb.com/website/aa.com/ |
| 3 | Canada | 0.98% | ~0.55M | Up 13.54% | https://www.similarweb.com/website/aa.com/ |
| 4 | Mexico | 0.82% | ~0.46M | Up 13.57% | https://www.similarweb.com/website/aa.com/ |
| 5 | United Kingdom | 0.78% | ~0.44M | Up 11.48% | https://www.similarweb.com/website/aa.com/ |
| 6 | Others (aggregate) | 5.14% | ~2.9M | N/A | https://www.similarweb.com/website/aa.com/ |

Total visits: **56.6M** (Similarweb, June 2026 data month), global rank #511, category rank #1 in Air Travel (United States).
Cross-check: Semrush reports **50.7M** visits June 2026 (down ~6% from 53.87M in May), country split United States 91.83%, Canada 1.2%, Mexico 1.06%. https://www.semrush.com/website/aa.com/overview

**Ranks 7 to 10: not obtainable.** Both Similarweb and Semrush publish only 5 countries plus "Others" on their free tiers. **No public information found.**

**Domain architecture:** AA runs **no country ccTLDs**. It serves a single domain with a locale parameter (`aa.com/i18n/...?locale=en_GB`, `?locale=pt_BR`, `?locale=es_MX`). Verified live. https://www.aa.com/i18n/customer-service/payment-options/payment-options.jsp

**Flags:**
- Only one market above 5% traffic (United States). Web traffic is heavily domestic, but revenue is not: **29.1% of passenger revenue is international** (Section 12).
- LATAM presence is material and understated by web traffic: **$6.44B Latin America passenger revenue FY2025**, Brazil is the #2 traffic country and the fastest-growing (+64% MoM).
- APAC presence is the fastest-growing region by revenue: **Pacific +13.7% YoY**.

---

## SECTION 2 — Legal Entities

Source for the full subsidiary list: Exhibit 21.1 "Subsidiaries of the Registrant" as of 31 Dec 2025, filed with the FY2025 10-K. https://www.sec.gov/Archives/edgar/data/4515/000000620126000014/ex211q42510k.htm

| Country | In Top 5 Traffic? | Has Local Entity? | Cross-Border Risk? | Source URL |
|---|---|---|---|---|
| United States | Yes (91.26%) | Yes (American Airlines, Inc., Delaware) | No | https://www.sec.gov/Archives/edgar/data/4515/000000620126000014/ex211q42510k.htm |
| Brazil | Yes (1.02%) | **No subsidiary in Ex. 21.1** | ⚠️ Yes | Same |
| Canada | Yes (0.98%) | **No subsidiary in Ex. 21.1** | ⚠️ Yes | Same |
| Mexico | Yes (0.82%) | Yes, but ground handling only (International Ground Services, S.A. de C.V.) | ⚠️ Yes (not a ticket-selling merchant entity) | Same |
| United Kingdom | Yes (0.78%) | **Branch only**: AMERICAN AIRLINES INC, overseas company FC011471, first UK establishment 1 Jan 1993, incorporated Delaware | ⚠️ Yes | https://find-and-update.company-information.service.gov.uk/company/FC011471 |
| Cayman Islands | No | Yes (AAdvantage Holdings 1 & 2 Ltd., AAdvantage Loyalty IP Ltd.) | Loyalty IP financing SPVs, not merchant entities | Ex. 21.1 |
| Luxembourg | No | Yes (Madrid IP Lux GP Sá.r.l, Madrid IP Lux HoldCo SCS, HoldCo 2 SCS) | IP structure, not merchant | Ex. 21.1 |
| India | No | Yes (American Airlines Services India LLP) | Shared services, not merchant | Ex. 21.1 |
| Bermuda | No | Yes (Avion Assurance Ltd.) | Captive insurer | Ex. 21.1 |

**The key read:** the consolidated subsidiary list contains only **six non-US jurisdictions** (Cayman Islands, Luxembourg, India, Mexico, Bermuda), and **not one of them is a ticket-selling merchant entity**. Every foreign subsidiary is loyalty IP, shared services, ground handling or insurance.

> ⚠️ **[INFERENCE, not confirmed]** International ticket sales are therefore billed from American Airlines, Inc. (Delaware) through registered branches rather than local selling entities. The UK branch registration (FC011471) supports this. AA does not state it in any document verified here.

**FX exposure, first-party (FY2025 10-K):** "Our largest exposure comes from the Euro, Canadian dollar, British pound sterling and various Latin American currencies (primarily the Brazilian real). **We do not currently have a foreign currency hedge program.**" A uniform 10% strengthening of the dollar would have cut FY2025 pre-tax income by approximately **$140 million**. https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/aal-20251231.htm

Countries named in AA's own privacy policy (implies local data processing / regulatory presence): United States, United Kingdom, EU member states, Uruguay, Brazil, China, Colombia, Ecuador, Peru, South Korea, France, Switzerland. https://www.aa.com/i18n/customer-service/support/privacy-policy.jsp

> ⚠️ MANUAL: Verify branch registrations in Brazil, Colombia, Chile and Peru on local registries. OpenCorporates returned no public information for AA branches in those countries in this pass.

---

## SECTION 3 — Payment Stack

### 3A. PSPs and Acquirers

| Country/Region | PSP / Acquirer | Evidence Type | Source URL |
|---|---|---|---|
| Global | **Not found. No processor, gateway or acquirer is named in any AA filing or public page.** | Exhaustive negative search | https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/aal-20251231.htm |
| Global | Multiple processors exist, contractually, but unnamed: "We have agreements with **companies that process customer credit card transactions**" (plural, repeated) | SEC filing (10-K, Item 1A + Note g "Credit Card Processing Agreements") | Same |
| Global | Card-network layer: **UATP**, AA is a founding member and an **issuing** airline, accepted at 340+ airline, rail and TMC merchants | Live page + vendor page | https://www.aa.com/i18n/customer-service/programs-products/uatp.jsp · https://uatp.com/partners/ |
| Global (co-brand issuing, **not** acquiring) | **Mastercard**, exclusive network for AAdvantage co-brand cards under a new 10-year contract signed July 2025 | SEC filing + press release | https://www.mastercard.com/us/en/news-and-trends/press/2025/july/american-airlines-mastercard-partnership-renewal.html |
| US (co-brand issuing, **not** acquiring) | **Citibank N.A.**, exclusive AAdvantage co-brand issuer from 2026 | Press release + 8-K | https://www.citigroup.com/global/news/press-release/2024/american-airlines-and-citi-extend-and-expand-co-branded-card-partnership-paving-the-way-for-more-customer-benefits |
| AA Vacations (separate stack) | **Upgrade, Inc.** (NMLS #1548935) powers the "Flex Pay" BNPL, APR 0 to 36%, minimum $300 | Live page | https://www.aavacations.com/flexpay |
| AA Cargo (separate stack) | **PayCargo** and **CargoSprint** as online payment platforms, plus direct credit accounts | Live page | https://www.aacargo.com/learn/payment.html |
| Booking host (not payments) | **Sabre SabreSonic PSS**, multi-year renewal announced 10 Dec 2024 | Press release | https://www.sabre.com/insights/releases/sabre-and-american-airlines-extend-it-partnership-multi-year-agreement-paves-way-for-joint-technology-modernization-and-innovation/ |

**Negative-search record (so the team does not repeat it):**
- SEC EDGAR full-text search across all AAL/AMR filings returns **0 hits** for each of: Cybersource, Adyen, Worldpay, First Data, Chase Paymentech.
- No public information found for: Stripe, Checkout.com, Braintree, Fiserv, Elavon, ACI Worldwide, Outpayce/Amadeus, Spreedly, Primer, Gr4vy, IXOPAY, CellPoint Digital, APEXX.
- Source-code inspection blocked: the only public urlscan.io capture of www.aa.com is itself a 403 page with zero third-party hosts. https://urlscan.io/result/019f6c0b-3ec0-72ca-b395-ef3ba490e2df/
- The `aa.com/ecommerce/checkout-app/payment` route renders an **Angular SPA shell** whose only third-party scripts are Dynatrace and Akamai mPulse. Payment SDKs load only inside an authenticated booking session. The JS bundle returns 403 to direct request.
- Keyword scan of every retrievable AA HTML page returned **zero hits** for adyen, cybersource, worldpay, braintree, stripe, cardinal, threeds, tokenex, spreedly, riskified, forter, kount, accertify, signifyd.

**Third-party analytics/tag stack observed on AA pages (not payments):** Adobe demdex, Tealium (`tags.tiqcdn.com/utag/aa/main/prod`), Quantum Metric (`quantum-aa.js`), Dynatrace, Akamai mPulse, OneTrust.

**High-value first-party quote, holdback exposure (FY2025 10-K):**
> "These agreements allow these credit card processing companies, under certain conditions (including, for certain agreements, our failure to maintain certain levels of liquidity), to hold an amount of our cash (referred to as a holdback) equal to some or all of the advance ticket sales that have been processed by that credit card processor, but for which we have not yet provided the air transportation. Additionally, those credit card processing companies may require cash or other collateral reserves to be established."

Risk-factor headline in the same filing: *"If our financial condition worsens, provisions in our credit card processing and other commercial agreements may adversely affect our liquidity."* Holdback can reach "up to and including 100% of relevant advanced ticket sales" against an **air traffic liability of $7,158M** at 31 Dec 2025. Receivables from ticket sales are "mostly settled within seven days after sale."

### 3B. Orchestrator

**No public evidence found** that American Airlines uses any payment orchestrator (CellPoint Digital, Spreedly, Primer, Gr4vy, IXOPAY, Yuno, APEXX). CellPoint publishes a client roster of roughly 250 airlines and American is not named in any CellPoint material located.

> **[INFERENCE, not confirmed]** AA appears to run multiple acquirer relationships directly, based on the plural language in the 10-K, with no orchestration layer disclosed. Do not assert on a call that AA "has no orchestrator." Say: "no public evidence of an orchestration layer."

> ⚠️ MANUAL, DevTools: run a live booking to the payment step in a US session and in a BR or MX session, capture the network calls. Test card 4111 1111 1111 1111 | 02/30 | 123. This is the only remaining path to identify the gateway.

---

## SECTION 4 — APMs

### 4A. Confirmed APMs

All rows verified from AA's own localized `payment-options.jsp` pages, fetched 2026-07-22. **The localized pages are genuinely different documents, not translations of one list.**

| Market | APMs Confirmed | Verification Source | Source URL |
|---|---|---|---|
| US (en_US) | Apple Pay, Google Pay, PayPal, **Venmo**, **Affirm**, **Citi Flex Pay**, UATP, gift cards (plastic + virtual), Travel Credit (Flight Credit / Travel Voucher / Trip Credit), Flight Discount, cash or check at counters | First-party AA page | https://www.aa.com/i18n/customer-service/payment-options/payment-options.jsp |
| UK (en_GB) | Apple Pay, PayPal, Affirm, UATP, gift cards, travel credit, flight discount, cash/check | First-party AA page | …payment-options.jsp?locale=en_GB |
| Spain (es_ES) | Apple Pay, PayPal, Affirm, UATP, tarjetas regalo, crédito aéreo, descuento, efectivo/cheque | First-party AA page | …?locale=es_ES |
| France (fr_FR) | Same set as es_ES | First-party AA page | …?locale=fr_FR |
| Germany (de_DE) | Same set as es_ES | First-party AA page | …?locale=de_DE |
| Japan (ja_JP) | Apple Pay, PayPal, Affirm, UATPカード, ギフトカード, トラベルクレジット, 運賃割引 | First-party AA page | …?locale=ja_JP |
| Brazil (pt_BR) | Apple Pay, **Google Pay**, PayPal, UATP, gift cards, crédito aéreo, desconto, dinheiro, **ETS phone-purchase rail**; **parcelamento up to 6x sem juros** on Brazil-issued Amex/Diners/Visa/Mastercard; co-brand shown is **Santander/AAdvantage**, not Citi | First-party AA page | https://www.aa.com/web/i18n/customer-service/payment-options/installments.html?locale=pt_BR |
| Mexico (es_MX) | Apple Pay, PayPal, UATP, efectivo/cheque, crédito aéreo; **MSI meses sin intereses**: 3 MSI Amex, 6 MSI Amex/Santander/Citibanamex/HSBC/Scotiabank, minimum MXN $500, CAT 0%, **direct channels only**; **Factura Electrónica (CFDI)** | First-party AA page | …installments.html?locale=es_MX |
| Onboard | "We accept all forms of contactless payment, including digital wallets linked to major credit and debit cards. You can also use your AAdvantage® miles on all flights." Single form of payment per inflight transaction | First-party AA page | https://www.aa.com/i18n/travel-info/experience/dining/main-cabin-food.jsp |
| AA Vacations | Amex, Discover, Mastercard, Visa only; billing address US/Canada/PR/USVI; miles or miles+cash; **Flex Pay by Upgrade, Inc.**; Travel Vouchers phone only | First-party page | https://www.aavacations.com/faq · https://www.aavacations.com/flexpay |
| AA Cargo | Credit account (US), **PayCargo**, **CargoSprint**, terminal card payment | First-party page | https://www.aacargo.com/learn/payment.html |
| Travel agency channel | Amex, Diners, Discover, JCB, Mastercard, UATP, Visa, **AA 2001 house card**, **AA Barter Cards** (BIN 10018). Verbatim: **"IATA EasyPay is not accepted by American Airlines"** | First-party page, updated Dec 2024 | https://saleslink.aa.com/en-US/resources/html/credit-card-acceptance.html |

Cards accepted globally, verbatim: **American Express, Diners Club, Discover, JCB\*, Mastercard, Visa, UATP Card, Union Pay (credit only)**. JCB is restricted to a named 27-market list.

**Verbatim geographic and functional constraints (all first-party):**
- PayPal: *"You can use PayPal for all travel except award tickets on aa.com or the American Airlines app if you reside in the U.S. or the United Kingdom. PayPal charges a cross border fee to residents of other countries."* And: *"If your payment is declined by PayPal, your reservation will be canceled."*
- Venmo: *"You can pay for your trip using Venmo when booking on aa.com"* (web only; app availability "planned for the future").
- Affirm: *"Affirm can be used to pay for flights and seats, but is not available for other extras like bags."*
- Citi Flex Pay: aa.com and the app, purchases of $75 or more, eligible Citi/AAdvantage cardmembers, no credit check.
- Gift cards and Flight Discounts: *"available in the U.S. (including Puerto Rico and U.S. Virgin Islands)"* only.

### 4B. Unverified Markets

| Market | Verification Attempted? | Reason Not Verified | Popular Local APMs |
|---|---|---|---|
| Brazil checkout (live) | Yes | Could not create a Brazilian booking session. The pt_BR help page is a marketing document, not the checkout renderer | Pix, boleto, Mercado Pago |
| Mexico checkout (live) | Yes | Could not create a Mexican booking session | SPEI, OXXO, Mercado Pago |
| Netherlands / DACH / Nordics checkout | Yes | Only the localized help pages loaded, not a live checkout | iDEAL, Bancontact, SEPA, Klarna, Vipps |
| China / Hong Kong checkout | Yes | No CN-locale checkout reachable | Alipay, WeChat Pay, UnionPay QR |
| India, Korea, Japan checkout | Yes | Help pages only | UPI, KakaoPay, Naver Pay, Konbini, PayPay |
| App checkout parity vs aa.com | Yes | AA confirms Citi Flex Pay and PayPal in the app and states Venmo is aa.com only. All other app-side methods unconfirmed | N/A |
| Sezzle, Zip, Klarna, Uplift (current status) | Yes | None appear on any AA page retrieved. The only Uplift trace is a stale `<title>` string on the AA Vacations FAQ, whose body names Upgrade, Inc. | N/A |
| eCheck, Western Union cash, "Fly Now Pay Later" | Yes | Present in a 2009 AA investor press release, absent from the current page. The popup fragments return 403 | N/A |
| 3DS / EMV-3DS / SCA posture | Yes | No AA page, release or forum thread verifies a step-up flow | N/A |

> **"Not verified" is not "not available."** The tables above record what each page lists, which is a verified fact about the page. They are **not** evidence that Google Pay is unavailable in the UK, that Affirm is unavailable in Brazil, or that Pix is unavailable at a Brazilian checkout. **MANUAL: VPN checkout walk-through before making any APM claim in a call or email.**

---

## SECTION 5 — Payment Complaints

Six `site:reddit.com` sweeps returned **133 distinct threads**, about 60 with verified dates, spanning **Dec 2015 to Apr 2026** with continuous coverage every year from 2021 to 2026. This is a persistent pattern, not an episode.

| Issue Type | Platform | Frequency | Date Range | Source URL |
|---|---|---|---|---|
| Card declined at checkout, "We're having trouble with your payment. Check your information or try another card or payment type." | Reddit r/americanairlines | 7+ dated threads plus 5 undated | Jan 2023 to Jan 2025 | https://www.reddit.com/r/americanairlines/comments/1g58w1v/aacom_doesnt_like_my_credit_cards_anymore_and_aa/ |
| **Live, unresolved decline defect on award bookings and seat upgrades**, agents instruct customers to call to pay | Reddit r/americanairlines | Active thread Oct 2025 into 2026 | Oct 2025 to 2026 | https://www.reddit.com/r/americanairlines/comments/1o293fu/anyone_else_successfully_resolve_aas_credit_card/ |
| "Something went wrong. We are unable to process your payment." | FlyerTalk | Dedicated thread | Multi-year | https://www.flyertalk.com/forum/american-airlines-aadvantage/2073952-something-went-wrong-we-unale-process-your-payment.html |
| Reservation auto-cancelled within 24 hours for "failed payment" | FlyerTalk | Dedicated thread | Multi-year | https://www.flyertalk.com/forum/american-airlines-aadvantage/1993359-aa-reservation-cancelled-due-failed-payment.html |
| Cannot pay for held award reservations online, workaround is to call | FlyerTalk | Multi-page thread, 3+ pages | Mid-2023 onward | https://www.flyertalk.com/forum/american-airlines-aadvantage/2148112-unable-pay-hold-award-reservations-online.html |
| Double charges and duplicate authorizations | Reddit (r/americanairlines, r/personalfinance) | 8+ threads | Nov 2021 to **Feb 2026** | https://www.reddit.com/r/americanairlines/comments/1qywsla/is_it_normal_for_american_airlines_to_double/ |
| Baggage double-charge at kiosk/gate | Reddit + FlyerTalk + Elliott.org | Multiple, plus a **$7.5M baggage-fee refund settlement** | 2024 to Mar 2026 | https://www.elliott.org/the-troubleshooter/help-american-airlines-charged-me-80-for-my-free-checked-bag/ · https://www.cbsnews.com/amp/news/american-airlines-baggage-fee-refund-lawsuit-settlement |
| Refund issued in AA's system but absent from the card for 2 weeks to 1 month+ | Reddit | 6+ dated threads | Sep 2023 to **Jan 2026** | https://www.reddit.com/r/americanairlines/comments/1qj4oy6/refund_pending_1_month/ |
| **Dispute/refund reconciliation collision**: AA refunded on top of a bank provisional credit, customer clawed back months later, 12+ calls and three faxed disputes | Elliott.org | Documented case | N/A | https://www.elliott.org/the-troubleshooter/billed-american-airlines-billed/ |
| Stored value fails at checkout: "cannot redeem online", "Trip Credit can't be used for this trip", "Trip credit not valid. Choose different form of payment." | Reddit | 8+ dated threads, **largest single cluster** | Sep 2022 to **Apr 2026** | https://www.reddit.com/r/americanairlines/comments/1i1mdkp/cant_book_with_trip_credit_online/ |
| Foreign card rejected / forced POS redirect with a price jump (e.g. $407 USD to $813; $303 USD to $521 CAD on the same itinerary) | Reddit + FlyerTalk | 5+ dated threads, incl. an explicit "I didn't have a problem when I booked with Delta" | Aug 2022 to May 2024 | https://www.reddit.com/r/americanairlines/comments/1b3cowq/paying_with_foreign_credit_card/ |
| PayPal / Venmo capture and settlement mismatch (charged, reservation gone; PayPal stuck in "authorization in progress" for 2 weeks) | Reddit | 3+ dated threads incl. **Feb 2026** | Jun 2024 to Feb 2026 | https://www.reddit.com/r/americanairlines/comments/1jly65y/paypal_payment_help/ |

**Not found:** AA-specific Trustpilot or ConsumerAffairs payment-failure statistics. Pages exist but no payment-specific breakdown is verifiable. No public disclosure of AA's auth rates, decline rates or chargeback ratios.

### Analysis: complaint pattern mapped to Yuno

| Pattern | Yuno lever |
|---|---|
| Declines that end in "call reservations," including on award bookings and upgrades | **Failover + Recovery**: automatic cascade to a second acquirer in milliseconds instead of a call-centre deflection. Livelo recovered +5% approvals within 3 months. |
| Foreign card rejected / POS mismatch, only six local-currency markets | **Smart Routing Engine**: route by BIN and issuer country to the best-performing path per market. InDrive reached 90% approval across 10 LATAM markets. |
| Double charges, duplicate authorizations, refund and dispute collisions | **Unified reconciliation and real-time monitors**: Rappi detects anomalies in milliseconds versus 5 to 10 minutes manually, with 80% less analyst time to resolution. |
| Stored value (Trip Credit, Flight Credit, gift cards) failing online, one card per booking | **Split tender and orchestration**: combine instruments in one transaction instead of pushing customers to the phone. |

---

## SECTION 6 — Expansion and Corporate Developments

| # | Date | Development | Category | Source URL |
|---|---|---|---|---|
| 1 | FY2025 | Launched **more than 60 new routes** in 2025, including transatlantic to Spain, Italy and Greece; announced **over 20 new routes** for 2026 | Network expansion | https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/aal-20251231.htm |
| 2 | 7 Aug 2025 | "Six For '26": PHL to Budapest and Prague, DFW to Athens and Zurich, MIA to Milan (year-round), DFW to Buenos Aires. Only carrier with nonstop US to Budapest | Network expansion | https://news.aa.com/news/news-details/2025/American-Airlines-announces-new-international-routes-for-next-summer-NET-RTS-08/default.aspx |
| 3 | 8 Mar 2026 | **JFK to Edinburgh launched**, first international A321XLR route, first single-aisle transatlantic service in seven years. Seventh new transatlantic route for summer 2026 | Network expansion | https://news.aa.com/news/news-details/2025/American-Airlines-unveils-first-international-route-for-the-Airbus-A321XLR-NET-RTS-10/default.aspx |
| 4 | 22 Jan 2026 | New domestic routes from ORD and LAX; ORD to have 500+ daily departures summer 2026 | Network expansion | https://news.aa.com/news/news-details/2026/American-enhances-network-with-new-routes-from-Chicago-and-Los-Angeles-NET-RTS-01/default.aspx |
| 5 | 2026 | New Porto, Portugal service | Network expansion | https://news.aa.com/news/news-details/2026/American-Airlines-flights-to-Porto-Portugal-NET-RTS-02/default.aspx |
| 6 | 2026 | **$1 billion investment** in Miami concourse expansion | Capex | https://news.aa.com/news/news-details/2026/American-carries-legacy-forward-with-1-billion-investment-in-MIA-OPS-OTH-02/default.aspx |
| 7 | 3 Nov 2025 | **Nathaniel "Nat" Pieper appointed Chief Commercial Officer**. Owns alliances, cargo, **co-branded credit card program, loyalty**, network planning, revenue management, **sales and distribution**. Ex-oneworld CEO | Leadership hire | https://news.aa.com/news/news-details/2025/American-names-Nathaniel-Pieper-Chief-Commercial-Officer-CORP-EXEC-10/ |
| 8 | 2025 | **Heather Garboden appointed Chief Customer Officer**, leading a newly created Customer Experience organization | Leadership hire | https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/aal-20251231.htm |
| 9 | 15 Jul 2026 | **John W. Dietrich elected to the AAL board** (Audit + Finance Committees), former EVP and CFO of FedEx | Governance | https://news.aa.com/news/news-details/2026/American-Airlines-elects-John-W-Dietrich-to-its-board-of-directors-CORP-EXEC-07/default.aspx |
| 10 | Current | **Payments org exists and is hiring.** "Analyst/Senior Analyst, **Payment Strategy**" (Phoenix, AZ): "cost reduction initiatives and payment reporting/policy/fraud issues," "liaison to the **Payment product delivery team**" | Payment job posting | https://jobs.aa.com/job/Phoenix-AnalystSenior-Analyst,-Payment-Strategy-AZ-85001/1124558300/ |
| 11 | Current | "Product Owner/Sr Product Owner": "member of the **Payments Automation Team within the Finance Division**" | Payment job posting | https://jobs.aa.com/job/Product-OwnerSr-Product-Owner,-Technology-Products/84173-en_US/ |
| 12 | Current | "Analyst/Sr Analyst, Revenue Accounting", **Passenger Interline Team**, supporting **Interline Settlement and Audit** | Payment job posting | https://jobs.aa.com/job/Phoenix-AnalystSr-Analyst,-Revenue-Accounting-AZ-85001/79673-en_US/ |
| 13 | Current | "Associate Analyst/Analyst, **Loyalty Fraud**" within Corporate Security | Payment job posting | https://jobs.aa.com/job/Associate-AnalystAnalyst,-Loyalty-Fraud/82942-en_US/ |
| 14 | Ongoing | **Treasurer role**: Meghan Montana (SVP & Treasurer from Dec 2020) has left AA for Norwegian Cruise Line Holdings. **No public successor found** | Leadership gap | https://www.flightglobal.com/strategy/montana-to-succeed-weir-as-american-airlines-treasurer/141495.article |

**Public RFP for payment services: No public information found.**

⚠️ **Do not target:** "Team Lead, AACU Payments Processing" and "Analyst, AACU Fraud" sit inside **American Airlines Credit Union**, a separate financial institution, not the airline's merchant payments org.

**Leadership roster (verified):** Robert Isom (CEO and President), Devon May (CFO since 1 Jan 2023, owns treasury, accounting, FP&A, tax, purchasing), Ganesh Jayaram (EVP & Chief Digital and Information Officer since Sep 2022, reports to Isom), Nat Pieper (CCO), Heather Garboden (CCO customer), Brian Znotins (SVP Network and Schedule Planning).
**No named VP/Head/Director of Payments at the airline: No public information found.**

---

## SECTION 7 — Payment News

| # | Date | Headline | Relevance | Source URL |
|---|---|---|---|---|
| 1 | **21 Jul 2026** | 🟢 **Venmo now live on aa.com; Apple Pay expanded "across additional purchase paths"** for "faster checkout with fewer steps." App availability for Venmo "planned for the future" | **Freshest possible hook, one day old.** AA is actively investing in checkout right now | https://news.aa.com/news/news-details/2026/From-booking-to-boarding-Giving-customers-more-control-throughout-their-journey-MKG-OTH-07/default.aspx |
| 2 | ~12 Jun 2026 | 🟢 Venmo spotted live ~6 weeks before the formal release. **JetBlue was first US airline to accept Venmo (Jan 2025)**, so AA is a follower here | Competitive timing | https://viewfromthewing.com/american-airlines-adds-venmo-fox-streaming-and-free-bag-rechecks-for-stranded-passengers-roundup/ |
| 3 | 24 to 27 Apr 2026 | 🔴 **Barclays AAdvantage portfolio converted to Citi.** Account-access blackout 24 to 26 Apr, access restored 27 Apr, **new card numbers issued** to every migrated cardmember, physical cards 6 to 8 weeks | Millions of stored card-on-file credentials changed PAN in one window. Classic account-updater and stored-credential failure scenario | https://onemileatatime.com/news/american-aadvantage-barclays-cards-transitioning-citi-discontinued/ · https://www.cnbc.com/select/citi-becomes-exclusive-issuer-aadvantage-credit-cards/ |
| 4 | 1 Jan 2026 | 🟢 **Citi exclusive AAdvantage issuer takes effect.** AA "successfully transitioned inflight and airport credit card acquisition channels to Citi." Co-brand and partner cash remuneration **$6.2B in 2025**, guided to ~10% annual growth and to approach **$10B/yr** | The single largest payments-adjacent P&L line at AA | https://americanairlines.gcs-web.com/news-releases/news-release-details/american-airlines-reports-fourth-quarter-and-full-year-2025 |
| 5 | 9 Apr / 18 May 2026 | 🟢 **Prepay-for-bags $5 discount** on aa.com and the app ($45/$55; Basic Economy $50/$60). Explicit push of ancillary payment volume into digital channels | More digital card transactions, more decline surface | https://news.aa.com/news/news-details/2026/Customers-save-time-and-money-when-prepaying-for-checked-bags-MKG-OTH-02/default.aspx |
| 6 | Mar 2026 | 🟢 **AAdvantage miles to retail gift cards** platform launched (aadvantagegiftcards.com), $10 to $500, Sephora/Nike/Best Buy. New outbound stored-value rail | New money-movement surface | https://awardfares.com/blog/american-airlines-march-2026-updates/ |
| 7 | 16 Mar 2026 | 🟢 App **disruption platform**: centralized rebooking plus **automated meal-voucher issuance**. Compensation money movement moving in-app | Payouts surface | https://news.aa.com/news/news-details/2026/From-booking-to-boarding-Giving-customers-more-control-throughout-their-journey-MKG-OTH-07/default.aspx |
| 8 | 2 Mar 2026 | 🟢 **Samsung Wallet** boarding-pass integration, first US airline. **Boarding passes only, not payment** | Do not mis-sell this as a wallet win | https://news.aa.com/news/news-details/2026/American-Airlines-expands-digital-wallet-integration-making-travel-day-easier-for-customers-MKG-OTH-03/default.aspx |
| 9 | 22 Jul 2025 | 🟢 **Mastercard renewal, 10-year, exclusive network** for AAdvantage co-brand. Cites "real-time fraud detection, analytics and secure payment solutions" | Issuing side. **Do not present as AA's acquiring stack** | https://www.mastercard.com/us/en/news-and-trends/press/2025/july/american-airlines-mastercard-partnership-renewal.html |
| 10 | 5 Dec 2024 | 🟢 Citi and AA extend for a decade; Citi becomes exclusive US issuer, acquires the Barclays portfolio including inflight and airport acquisition channels | Origin of items 3 and 4 | https://www.citigroup.com/global/news/press-release/2024/american-airlines-and-citi-extend-and-expand-co-branded-card-partnership-paving-the-way-for-more-customer-benefits |
| 11 | 27 Oct 2021, still live | 🟢 **Affirm** BNPL partnership, still listed on the live payment-options page | Existing BNPL relationship | https://investors.affirm.com/news-releases/news-release-details/affirm-and-american-airlines-partner |

**Regulatory watch item AA flagged itself (FY2025 10-K):** the Credit Card Competition Act, "designed to increase credit card transaction routing options for merchants which, if enacted, could result in a material reduction of the fees levied on credit card transactions," plus a proposed temporary 10% cap on card interest rates. AA says either "could fundamentally alter the profitability of our agreement with our co-branded credit card [partner]." **Routing is already on AA's regulatory radar in its own words.**

**Not found:** any PSP, orchestrator or acquirer RFP, contract or vendor news. AA does not appear on Google's named agentic-booking travel partner list (Booking.com, Expedia, Marriott, IHG, Choice, Wyndham), which is an absence from a list, not proof of non-participation.

---

## SECTION 8 — Checkout Audit

| Dimension | Finding | Quality | Notes |
|---|---|---|---|
| Checkout type | Angular SPA at `aa.com/ecommerce/checkout-app/payment`, named step "Review and pay", hosts the payment selector, "Add travel credit" and "Hold for 24 hours" | 🟡 | Payment SDKs load only inside an authenticated session |
| Guest checkout | **Yes.** No AAdvantage account required | 🟢 | Corroborated by a Mar 2024 user report booking without an account |
| Steps to purchase | 5: country/POS selection or login, flight search and select, seat map, Review and pay, confirmation | 🟡 | Login timing itself depends on card issuing country (below) |
| **Split tender** | **"Only one card can be used when you book on aa.com (but you can use multiple gift cards)."** Verbatim, AA FAQ. Up to 8 Trip Credits; 1 Flight Credit online, a second requires a phone call; difference payable **only** by credit card | 🔴 | Hardest, most quotable constraint in the file. https://www.aa.com/i18n/customer-service/faqs/reservations-tickets-faqs.jsp |
| **Currency and POS** | **"Which countries might recalculate fares in local currency? Brazil (BRL), Canada (CAD), Colombia (COP), Chile (CLP), Mexico (MXN), U.K. (GBP). Fares for countries not listed will be in USD."** Customer must self-select the country where their card was issued from the homepage dropdown | 🔴 | **Six local-currency markets worldwide.** Everything else is billed USD cross-border, structurally guaranteeing cross-border interchange, issuer FX and elevated cross-border declines |
| Login logic | AAdvantage member with a card issued in the country on their profile: log in from the home page. Card issued in a **different** country: log in **after** choosing flights | 🔴 | Card issuing country is a routing decision made by the customer, in the UI, before payment |
| 3DS | **No public information found.** UK is a supported POS with GBP recalculation and PayPal availability, which would place AA in UK-SCA scope | ⚪ | **[INFERENCE]** only. Do not assert a 3DS posture |
| Mobile experience | Booking, Citi Flex Pay, PayPal and Apple Pay supported in the app. **Venmo is web only.** Apple Pay expanded to additional purchase paths Jul 2026 | 🟡 | App/web parity is incomplete by AA's own statement |
| APM display logic | Localized `payment-options.jsp` pages differ per market (Venmo US only, Citi Flex Pay US only, Google Pay listed on US and BR, Affirm on US/UK/ES/FR/DE/JP, installments only on BR and MX) | 🟡 | These are help pages. **Not** proof of live checkout rendering |
| Stored value | Trip Credit **not redeemable** in 18 countries (Australia, China, Colombia, Croatia, Czech Republic, Guatemala, Hong Kong, Hungary, Iceland, Japan, Korea, Mexico, New Zealand, Norway, Paraguay, Peru, Poland, Singapore). **"Trip Credit currency must match point-of-sale currency."** Single-passenger reservations only online | 🔴 | Five straight years of "cannot redeem online" complaints are these rules surfacing as errors. https://www.aa.com/i18n/customer-service/payment-options/travel-credit.jsp |
| 24-hour hold | Free hold up to 24 hours if booking 7+ days out. **"If you're using travel credits or seat coupons, reapply them when you return to pay."** Auto-cancels if not completed | 🟡 | Simultaneously the workaround users adopt when payment fails **and** a documented source of failures |

> ⚠️ MANUAL: walk the checkout in the US, Brazil and Mexico with a VPN before any call.

---

## SECTION 9 — PCI DSS

| PCI DSS Level | Card data handling | Recommended Yuno integration | Source |
|---|---|---|---|
| **Highest level, stated by AA itself.** FY2025 10-K: AA is "required by the Payment Card Industry Security Standards Council… to comply with their **highest level of data security standards (PCI DSS)**," and notes compliance costs and that PCI DSS compliance does not guarantee against payment-system misuse | AA collects raw card data. Privacy policy: "Payment information, including credit or debit card number(s), associated billing address(es), and expiration date(s)," shared with "payment processors, payment card issuers and networks, and fraud detection and prevention services." **No vendor is named** | **Yuno SDK with network tokenization + vault**, so AA keeps its scope where it is today while gaining routing. Given the Apr 2026 Barclays-to-Citi PAN reissue, **network tokens and account updater are the highest-value first module** | https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/aal-20251231.htm · https://www.aa.com/i18n/customer-service/support/privacy-policy.jsp |

AA's dedicated public security page cites only NIST: "American has created an integrated cybersecurity framework using various National Institute of Standards and Technology (NIST) security standards." **PCI DSS, ISO 27001 and SOC 2 are not mentioned on that page**; the PCI commitment appears only in the 10-K. https://www.aa.com/pubcontent/en_US/customer-service/about-us/cybersecurity-policy-statement.jsp

---

## SECTION 10 — Strategic Insights

### Insight #1: Six local-currency markets, the rest of the world billed USD cross-border
**Evidence:** Section 8. AA's own FAQ, verbatim: fares recalculate in local currency only for Brazil, Canada, Colombia, Chile, Mexico and the UK; "Fares for countries not listed will be in USD." Section 2 confirms AA has no ticket-selling subsidiary outside the US and no FX hedge program ($140M pre-tax sensitivity to a 10% dollar move).
**Pain point:** every sale outside six markets is a cross-border transaction: higher interchange, issuer FX applied to the customer, and the elevated decline rates that cross-border BIN mismatches produce. Section 5 documents exactly this failure mode in dated user reports, including a customer who booked Delta instead.
**Yuno value prop:** local acquiring and per-market routing so the transaction presents domestically where AA has volume, with BIN and issuer-level routing decisions made by the platform rather than by the customer picking a country from a dropdown.
**Best case:** InDrive, 10 LATAM markets live in under 8 months, 90% approval rates, 4.5% recovery.
**Outreach angle:** "Your FAQ says fares recalculate in local currency for six markets and everything else is billed in USD. That is a cross-border interchange and decline problem in every market outside those six, and it is the one thing an orchestration layer fixes without touching your PSS."

### Insight #2: One card per booking, and stored value that ends in a phone call
**Evidence:** Section 8, verbatim: "Only one card can be used when you book on aa.com." One Flight Credit online, a second requires calling Reservations. Trip Credit not redeemable in 18 named countries and must match POS currency. Section 5: the largest single complaint cluster, Sep 2022 to Apr 2026, is stored value failing at checkout.
**Pain point:** every split-tender need becomes a call-centre contact, and every failed credit redemption is an abandoned digital booking on inventory AA has already sold once.
**Yuno value prop:** orchestrated split tender across cards, credits, gift cards and wallets in a single transaction. Note that Southwest bought exactly this: CellPoint's Offer and Order solution lets Southwest customers "combine multiple payment methods, from credit cards and travel credits to alternative payment methods and Rapid Rewards points, all within a single transaction."
**Best case:** Rappi, zero implementation time, 80% less analyst resolution time.
**Outreach angle:** "Southwest went live with combined tender (cards plus travel credits plus points in one transaction) in 2025. Your FAQ still says one card per booking and a second Flight Credit needs a phone call."

### Insight #3: Declines that terminate in "call us," on the highest-value flows
**Evidence:** Section 5. An active Oct 2025 thread running into 2026 documents award-booking and seat-upgrade payment failures where "essentially all representatives I have spoke with tell me to just call when I want to make a payment." FlyerTalk has a dedicated thread named after the error string, and a documented policy of auto-cancelling reservations within 24 hours on failed payment.
**Pain point:** a hard decline today has no second path. There is no cascade, so the transaction is lost or deflected to the most expensive channel AA operates.
**Yuno value prop:** Smart Routing plus automatic failover, up to 50% recovery on failed transactions, and real-time monitors that surface a degrading acquirer in milliseconds instead of via a FlyerTalk thread.
**Best case:** Livelo, +5% approvals and 50% recovery within 3 months.
**Outreach angle:** "Your own customers are being told to phone in to complete a payment on award bookings. That is a routing problem with a known fix, and it is happening on your highest-margin inventory."

### Insight #4: Six competitors and peers already run orchestration. American does not, publicly
**Evidence:** Section 11C. Southwest Airlines (Mar 2025, direct US competitor), Virgin Atlantic (Jan 2024, transatlantic, AA's own JV corridor), Avianca (5+ PSPs, 40+ acquirers, 40+ payment methods), GOL (Aug 2025, Brazil, AA's #2 traffic country), Cebu Pacific and Riyadh Air are all publicly on CellPoint Digital. Virgin Atlantic's Head of Distribution and Payments, on record: "Now that we have been able to use multiple acquirers at one time, we have been able to diversify our risk, reduce cost, and optimise our payments strategy."
**Pain point:** AA's payment architecture is now behind its direct competitive set on a capability its peers are publicly quantifying.
**Yuno value prop:** the same category, with LATAM depth AA needs given $6.44B of Latin America passenger revenue and Brazil as its #2 digital market.
**Best case:** Avianca is the closest structural analogue in the Americas.
**Outreach angle:** "Southwest, Virgin Atlantic, Avianca and GOL have all put an orchestration layer above their acquirers in the last 24 months. Worth 20 minutes on what they measured."

### Insight #5: The Citi conversion just reissued PANs across the co-brand base, and co-brand cash is heading to $10B/yr
**Evidence:** Section 7. Barclays to Citi conversion 24 to 27 Apr 2026 with **new card numbers issued** to every migrated cardmember. Co-brand and partner cash remuneration was $6.2B in 2025, guided toward ~$10B/yr. Section 6: Nat Pieper became CCO in Nov 2025 and owns the co-brand program, loyalty, sales and distribution.
**Pain point:** a mass PAN reissue breaks stored credentials on file for recurring and one-click purchases, exactly when AA is pushing ancillary volume into digital channels with the prepay-for-bags discount.
**Yuno value prop:** network tokenization and account updater so credentials survive reissue, plus a vault that is not tied to a single processor.
**Best case:** Rappi's real-time monitoring for detecting a credential-driven approval drop the week it starts, not the quarter after.
**Outreach angle:** targeted at the CCO and CDIO offices, framed around protecting the $6.2B co-brand economics through the conversion tail.

---

## SECTION 11 — Pipeline

### 11A. Direct Competitors

| Company | Website | HQ | Est. Size (FY2025) | Overlap Markets | Source |
|---|---|---|---|---|---|
| United Airlines Holdings | united.com | Chicago, IL | $59.1B revenue (record, +3.5%) | Global, largest US international network | https://ir.united.com/static-files/a37e057c-8ccf-41a8-ac93-4263f0527cc1 |
| Delta Air Lines | delta.com | Atlanta, GA | $58.3B revenue (record) | Global | https://ir.delta.com/news/news-details/2026/Delta-Air-Lines-Announces-December-Quarter-and-Full-Year-2025-Financial-Results/default.aspx |
| Southwest Airlines | southwest.com | Dallas, TX | $28.1B operating revenue | US domestic + near-international | https://www.southwestairlinesinvestorrelations.com/news-events/press-releases/detail/1914/ |
| Alaska Air Group (incl. Hawaiian) | alaskaair.com | Seattle, WA | $14.4B revenue | US West, Pacific, new Europe long-haul | https://news.alaskaair.com/releases/alaska-air-group-reports-fourth-quarter-and-full-year-2025-results/ |
| JetBlue Airways | jetblue.com | Long Island City, NY | $9.1B operating revenue | US East, Caribbean, transatlantic | https://ir.jetblue.com/news/news-details/2026/JetBlue-Announces-Fourth-Quarter-2025-Results/default.aspx |
| Air Canada | aircanada.com | Montreal, QC | C$22.4B record operating revenue | Canada, transborder, transatlantic | https://www.aircanada.com/media/air-canada-reports-fourth-quarter-and-full-year-2025-financial-results/ |
| IAG (British Airways, Iberia, Aer Lingus, Vueling, LEVEL) | iairgroup.com | London, UK | €33.2B revenue, 121.6M passengers | Europe to North America and LatAm. **AA's transatlantic JV partner** | https://www.iairgroup.com/press-releases/2026/iag-full-year-results-2025/ |
| LATAM Airlines Group | latamairlines.com | Santiago, Chile | FY2025 adj. EBITDA ~$4.1B, net income ~$1.5B | South America, LatAm to US and Europe | https://finance.yahoo.com/news/latam-airlines-group-q4-earnings-082658421.html |
| Copa Holdings | copaair.com | Panama City, Panama | Net profit $671.6M, op margin 22.6% | LatAm hub-and-spoke via PTY | https://ir.copaair.com/news-releases/news-release-details/copa-holdings-reports-fourth-quarter-and-full-year-2025 |

*LATAM and Copa full-year total revenue figures were not located in a primary source. Do not quote a FY revenue number for either.*

### 11B. Industry Peers (large travel merchants)

| Company | Website | Vertical | Key Markets | Why Similar | Source |
|---|---|---|---|---|---|
| Booking Holdings | bookingholdings.com | OTA | Global | $26.9B revenue (+13%), multi-currency, multi-market checkout at scale | https://www.phocuswire.com/booking-holdings-q4-full-year-2025-earnings |
| Expedia Group | expediagroup.com | OTA | Global | Gross bookings and revenue both +8% FY2025 | https://ir.expediagroup.com/news-and-events/news/news-details/2026/Expedia-Group-Reports-Fourth-Quarter-and-Full-Year-2025-Results/default.aspx |
| Carnival Corporation | carnivalcorp.com | Cruise | Global | $26.6B record revenue, deposits and staged payments model | https://www.prnewswire.com/news-releases/carnival-corporation--plc-achieves-record-full-year-adjusted-net-income-and-investment-grade-leverage-metrics-reinstates-dividend-302646558.html |
| Royal Caribbean Group | rclinvestor.com | Cruise | Global | $17.9B revenue, $4.3B net income | https://www.prnewswire.com/news-releases/royal-caribbean-group-reports-2025-results-issues-2026-guidance-302673898.html |
| Marriott International | marriott.com | Hotels | Global | ~$26.2B revenue, Bonvoy loyalty economics parallel AAdvantage | https://marriott.gcs-web.com/news-releases/news-release-details/marriott-international-reports-fourth-quarter-and-full-year-2025 |
| Hilton Worldwide | hilton.com | Hotels | Global | $3,725M adjusted EBITDA, asset-light, Honors loyalty | https://stories.hilton.com/releases/hilton-reports-2025-fourth-quarter-and-full-year-results |

### 11C. Travel Merchants Publicly Confirmed on a Payment Orchestrator

| Company | Orchestrator | Date | Vertical | Source |
|---|---|---|---|---|
| **Southwest Airlines** | CellPoint Digital | 18 Mar 2025 | US airline, **AA direct competitor** | https://cellpointdigital.com/articles/newsroom/cellpoint-digital-deepens-strategic-partnership-with-southwest-airlines |
| **Virgin Atlantic** | CellPoint Digital | Jan 2024 | UK airline, transatlantic | https://www.prnewswire.com/news-releases/virgin-atlantic-implement-payment-orchestration-with-cellpoint-digital-302036552.html |
| **Avianca** | CellPoint Digital | 31 Mar 2021 | LatAm airline, 5+ PSPs, 40+ acquirers, 40+ methods | https://www.prnewswire.com/news-releases/avianca-appoints-cellpoint-digital-for-ambitious-payment-orchestration-project-301259048.html |
| **GOL** | CellPoint Digital | Aug 2025 | Brazil airline | https://www.futuretravelexperience.com/2025/08/gol-expands-payment-choices-for-passengers-in-partnership-with-cellpoint-digital/ |
| **Cebu Pacific** | CellPoint Digital | N/A | APAC airline | https://cellpointdigital.com/articles/casestudies/payment-orchestration-as-a-growth-catalyst-the-cebu-pacific-case-study |
| **Riyadh Air** | CellPoint Digital | Feb 2025 | MENA airline | https://www.prnewswire.com/news-releases/cellpoint-digital-launches-new-industry-standard-payment-platform-purpose-built-for-airlines-travel-companies-and-their-customers-302378326.html |

Delta, United, Alaska, JetBlue, Air Canada, IAG, LATAM and Copa: **no public information found** confirming a third-party orchestrator.
Sector signal: World Aviation Festival 2026 carries an airline debate on build versus buy payment orchestration, so the category is a standing board-level airline topic. https://worldaviationfestival.com/category/blog/payments/

### 11D. Scoring

| Signal | Pts | Verified? |
|---|---|---|
| Operates in 3+ countries | +3 | ✅ Over 350 destinations in more than 60 countries (10-K) |
| Multiple PSPs | +3 | ✅ 10-K refers repeatedly to "companies that process customer credit card transactions" (plural). Names not disclosed |
| Recent expansion (24 mo.) | +2 | ✅ 60+ new routes in 2025, 20+ announced for 2026, first A321XLR transatlantic Mar 2026 |
| Public payment issues | +2 | ✅ 133 threads, Dec 2015 to Apr 2026, continuous 2021 to 2026 |
| Funding >$10M | +2 | ✅ Public company, $54.6B revenue, $9.2B liquidity |
| LATAM/APAC/MENA traffic | +2 | ✅ $6.44B LatAm and $1.42B Pacific passenger revenue; Brazil is #2 traffic country |
| No orchestrator | +2 | ✅ No public evidence of any orchestrator (stated as absence of evidence, not proven absence) |
| Payment job postings | +1 | ✅ Payment Strategy analyst + Payments Automation Team product owner |
| Public RFP | +3 | ❌ Not found |

**Total: 17 points → 🔴 HIGH PRIORITY**

### Top 10 Pipeline

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal |
|---|---|---|---|---|---|---|
| 1 | **American Airlines** | Target | US, LatAm, Atlantic, Pacific | 17 | 🔴 High | Six local-currency markets, one card per booking, no orchestrator evidence |
| 2 | United Airlines | Direct competitor | Global | Not scored | 🔴 Likely high | $59.1B, largest US international network, no orchestrator evidence |
| 3 | Delta Air Lines | Direct competitor | Global | Not scored | 🔴 Likely high | $58.3B, no orchestrator evidence |
| 4 | Air Canada | Direct competitor | Canada, transatlantic | Not scored | 🟡 Medium | C$22.4B, multi-currency by nature, no orchestrator evidence |
| 5 | Copa Holdings | Direct competitor | LatAm via PTY | Not scored | 🟡 Medium | LatAm hub carrier, Yuno's home region |
| 6 | JetBlue Airways | Direct competitor | US East, Caribbean, transatlantic | Not scored | 🟡 Medium | First US airline on Venmo, actively adding methods |
| 7 | Alaska Air Group | Direct competitor | US West, Pacific, new Europe | Not scored | 🟡 Medium | New long-haul Europe launches 2026, new cross-border surface |
| 8 | Carnival Corporation | Industry peer | Global | Not scored | 🟡 Medium | $26.6B, deposits and staged payments |
| 9 | Royal Caribbean Group | Industry peer | Global | Not scored | 🟡 Medium | $17.9B, multi-currency cruise checkout |
| 10 | Marriott International | Industry peer | Global | Not scored | 🟡 Medium | ~$26.2B, loyalty-linked payment economics |

**Pipeline summary:** 15 companies mapped (9 direct competitors, 6 industry peers). 1 fully scored at 🔴 High. 6 travel merchants confirmed already on an orchestrator, which is the single strongest competitive-pressure asset in this brief. Strongest vertical: **large network airlines in North America and LatAm**, where Yuno's regional depth and the AA-adjacent Avianca and GOL precedents both apply.

---

## SECTION 12 — Business Case

| Annual Revenue | Avg Transaction Value | Est. Annual Transactions | Primary Currency | Top 3 Markets |
|---|---|---|---|---|
| **$54,633M** total FY2025 (record, +0.8% YoY); passenger revenue $49,643M; cargo $839M; other $4,151M | **~$222 per passenger (derived estimate, not disclosed by AA)**: $49,643M ÷ 224M passengers. AA publishes yield (19.83¢/RPM), not average fare | **~224M passengers boarded in 2025.** Card-addressable transaction count is materially higher once ancillaries, bags, seats, Vacations packages and cargo are counted. AA does not disclose card volume | **USD.** Local currency recalculated in only 6 markets: BRL, CAD, COP, CLP, MXN, GBP | 1. United States (domestic $35,201M, 70.9% of passenger revenue) · 2. Atlantic ($6,583M, 13.3%, +2.1%) · 3. Latin America ($6,444M, 13.0%) · Pacific ($1,415M, 2.9%, +13.7%, fastest growing) |

Supporting figures, all from the FY2025 10-K and the 27 Jan 2026 earnings release:
- **International = 29.1% of passenger revenue**, roughly 26.4% of total operating revenue.
- **Air traffic liability $7,158M** at 31 Dec 2025, the base for card-processor holdback exposure.
- Total loyalty-derived revenue $7,547M (13.8% of total): $4,036M loyalty travel + $3,511M loyalty marketing services.
- Co-brand and partner cash remuneration **$6.2B in 2025**, guided to approach $10B/yr.
- FY2025 GAAP net income **$111M** ($0.17/diluted share), a **0.2% net margin**. Every basis point of authorization uplift matters disproportionately at this margin.
- Total debt $36.5B, net debt $30.7B, liquidity $9.2B. 2026 guidance: adjusted EPS $1.70 to $2.70, FCF over $2B, Q1 revenue growth +7.0% to +10.0%.

> ⚠️ **Misinformation circulating in open search, do not use:** "$55.2B revenue, +12%", "passenger revenue $50.5B with domestic +9% and Atlantic +22%", "debt reduced by $4.0B to $28.0B with $10.5B liquidity", "Derek Kerr is CFO", and a "new 2026 American to JetBlue codeshare". All are wrong or unverified. Use only the 10-K figures above.

---

## SECTION 13 — Outreach

*Built exclusively from verified findings. Contains no claim that AA lacks any payment method.*

```
--- LINKEDIN MESSAGE ---

Hi [First name],

Saw American put Venmo live on aa.com yesterday and widened Apple Pay across more purchase paths. Clear signal checkout is getting real investment right now.

Two things in your own published material stood out to me. Your FAQ lists six markets where fares recalculate in local currency (Brazil, Canada, Colombia, Chile, Mexico, UK) and says everything else is billed in USD. And it says only one card can be used per booking on aa.com. With $6.4B of Latin America passenger revenue and Brazil as your second-largest digital market, that first one is a cross-border interchange and authorization question at real scale.

Yuno sits above your existing acquirers as an orchestration layer, so you route per BIN and issuer country and cascade a decline to a second path instead of losing it. InDrive went live across 10 LATAM markets in under 8 months and holds 90% approval. Livelo picked up 5 points of approval in 3 months. Rappi cut anomaly detection from 5 to 10 minutes down to milliseconds.

Southwest, Virgin Atlantic, Avianca and GOL have all put this layer in over the last 24 months. Happy to walk you through what they measured.

Free Tuesday or Thursday at 10am CT for 20 minutes?

German

--- COLD EMAIL ---
Subject: six currencies, 60+ countries

Hi [First name],

American sells in more than 60 countries. Your own FAQ says fares recalculate in local currency for six of them, Brazil, Canada, Colombia, Chile, Mexico and the UK, and that everything else is billed in USD.

That makes almost every international sale a cross-border transaction: higher interchange, issuer FX passed to the customer, and the decline rates that come with a BIN and acquirer-country mismatch. Your 10-K puts $14.4B of passenger revenue outside the US and notes there is no FX hedge program. At a 0.2% net margin on $54.6B, a point of authorization is not a rounding error.

Yuno is an orchestration layer that sits above the acquirers you already have. Route per BIN, issuer and market, cascade a decline to a second path in milliseconds instead of losing the booking, and add a local rail per market without a new integration project.

InDrive: 10 LATAM markets live in under 8 months, 90% approval. Livelo: +5% approval and 50% recovery in 3 months. Rappi: anomaly detection in milliseconds instead of 5 to 10 minutes.

Southwest, Virgin Atlantic, Avianca and GOL all added this layer in the last 24 months. Worth 20 minutes to compare notes on what they measured?

German
```

**Persona routing:** no VP or Head of Payments is publicly identified at the airline. Route to **Nat Pieper (Chief Commercial Officer**, owns co-brand, loyalty, sales and distribution) or **Ganesh Jayaram (EVP and Chief Digital and Information Officer**, owns the full technology stack). Secondary: **Devon May (CFO)**, who owns treasury and would care about the holdback exposure against $7.16B of air traffic liability. Do not route to American Airlines Credit Union staff.

---

## APPENDIX — Source URLs

```
[S1]  https://www.similarweb.com/website/aa.com/
[S2]  https://www.semrush.com/website/aa.com/overview
[S3]  https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/aal-20251231.htm  (FY2025 10-K)
[S4]  https://www.sec.gov/Archives/edgar/data/4515/000000620126000014/ex211q42510k.htm  (Exhibit 21.1 subsidiaries)
[S5]  https://find-and-update.company-information.service.gov.uk/company/FC011471  (UK branch)
[S6]  https://www.aa.com/i18n/customer-service/payment-options/payment-options.jsp
[S7]  https://www.aa.com/i18n/customer-service/faqs/reservations-tickets-faqs.jsp  (one card per booking; 6 local currencies)
[S8]  https://www.aa.com/i18n/customer-service/payment-options/travel-credit.jsp  (18-country Trip Credit exclusion)
[S9]  https://www.aa.com/web/i18n/customer-service/payment-options/installments.html?locale=pt_BR
[S10] https://www.aa.com/web/i18n/customer-service/payment-options/installments.html?locale=es_MX
[S11] https://www.aa.com/i18n/customer-service/programs-products/uatp.jsp
[S12] https://saleslink.aa.com/en-US/resources/html/credit-card-acceptance.html
[S13] https://www.aavacations.com/flexpay  (Flex Pay by Upgrade, Inc.)
[S14] https://www.aacargo.com/learn/payment.html  (PayCargo, CargoSprint)
[S15] https://www.aa.com/i18n/travel-info/experience/dining/main-cabin-food.jsp  (onboard contactless)
[S16] https://www.aa.com/i18n/customer-service/support/privacy-policy.jsp
[S17] https://www.aa.com/pubcontent/en_US/customer-service/about-us/cybersecurity-policy-statement.jsp
[S18] https://news.aa.com/news/news-details/2026/From-booking-to-boarding-Giving-customers-more-control-throughout-their-journey-MKG-OTH-07/default.aspx  (Venmo + Apple Pay, 21 Jul 2026)
[S19] https://news.aa.com/news/news-details/2026/American-Airlines-reports-fourth-quarter-and-full-year-2025-financial-results-CORP-FI-01/default.aspx
[S20] https://www.citigroup.com/global/news/press-release/2024/american-airlines-and-citi-extend-and-expand-co-branded-card-partnership-paving-the-way-for-more-customer-benefits
[S21] https://www.mastercard.com/us/en/news-and-trends/press/2025/july/american-airlines-mastercard-partnership-renewal.html
[S22] https://onemileatatime.com/news/american-aadvantage-barclays-cards-transitioning-citi-discontinued/
[S23] https://news.aa.com/news/news-details/2025/American-names-Nathaniel-Pieper-Chief-Commercial-Officer-CORP-EXEC-10/
[S24] https://jobs.aa.com/job/Phoenix-AnalystSenior-Analyst,-Payment-Strategy-AZ-85001/1124558300/
[S25] https://cellpointdigital.com/articles/newsroom/cellpoint-digital-deepens-strategic-partnership-with-southwest-airlines
[S26] https://www.prnewswire.com/news-releases/virgin-atlantic-implement-payment-orchestration-with-cellpoint-digital-302036552.html
[S27] https://www.prnewswire.com/news-releases/avianca-appoints-cellpoint-digital-for-ambitious-payment-orchestration-project-301259048.html
[S28] https://www.futuretravelexperience.com/2025/08/gol-expands-payment-choices-for-passengers-in-partnership-with-cellpoint-digital/
[S29] https://www.reddit.com/r/americanairlines/comments/1o293fu/anyone_else_successfully_resolve_aas_credit_card/
[S30] https://www.elliott.org/the-troubleshooter/billed-american-airlines-billed/
[S31] https://urlscan.io/result/019f6c0b-3ec0-72ca-b395-ef3ba490e2df/
```
