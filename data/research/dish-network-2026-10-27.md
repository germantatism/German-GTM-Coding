# DISH Network (EchoStar): SDR Research Brief
*Yuno Payment Orchestrator. Framework v8.0, 4 research agents plus one people agent, accuracy first. Researched 27-Oct-2026 for the "Dish <> Yuno" call on Wed 28-Oct-2026, 8:30 to 9:00 AM PT.*

Reading guide: every factual line carries its source URL. [Source Code] = merchant JavaScript or server-rendered HTML fetched live on 27-Oct-2026. [Help Page] and [T&Cs] = official merchant pages. [Job Listing] = search snippets of EchoStar postings (originals now 404). [Review Site] is weak evidence. [INFERENCE, not confirmed] = my reading, not a fact. "Not verified" never means "not available".

---

## EXECUTIVE SUMMARY

DISH Network is the pay-TV and wireless arm of EchoStar Corporation (NASDAQ: ECHO since 24-Jun-2026, formerly SATS; https://www.satellitetoday.com/finance/2026/06/22/echostar-swaps-sats-ticker-for-echo-to-emphasize-business-shift/), Englewood, Colorado: DISH TV (4.68M satellite subscribers), Sling TV (1.71M), Boost Mobile (7.38M wireless subscribers, a hybrid MNO riding AT&T's network since 15-Nov-2025) and, one level up, Hughes/HughesNet satellite broadband in the US, six Latin American countries and India. FY2025 revenue was $15.0B. 2026 has been a restructuring year: the $20.25B AT&T spectrum sale closed 28-Jul-2026, DISH DBS ran a prepackaged Chapter 11 from 30-Jun to 1-Oct-2026 and shed about $4.35B of debt, Hughes Satellite Systems has been in a free-fall Chapter 11 since 2-Aug-2026 (international subsidiaries excluded), CEO Hamid Akhavan left on 6-Jul-2026 and Charlie Ergen now runs the group directly.

Key payment-stack finding: every brand runs its own stack and nothing is shared. Sling TV bills through Recurly with Kount fraud screening and PayPal, Apple Pay, Google Pay and Amazon Pay as "Express Pay". DISH TV takes payments through a CSG-hosted portal with Apple Pay, Google Pay, PayPal, bank account, Bitcoin via BitPay and cash at MoneyGram, Western Union and CheckFreePay. Boost Mobile runs an Amdocs Kenan/Optima billing stack with cards, Apple Pay, Google Pay and Affirm device financing, and states on its own help page that it does not accept prepaid cards on the web. HughesNet in Latin America has wired a different local collection stack in each of six countries (PayU and Facture in Colombia, Webpay in Chile, OXXO and SPEI in Mexico, boleto in Brazil, Yape in Peru, Servipagos in Ecuador). No orchestrator was found anywhere.

Yuno opportunity: one payments layer that sits on top of the billing systems they already run. Three levers: recurring-decline recovery on roughly $1B a month of consumer subscription billing (estimate from Q2-2026 segment revenue), consolidation of the six HughesNet LatAm stacks into one integration with local acquiring, and a day-one payments stack for whatever international or wireless-innovation product Chris Ergen's team launches next. Caveats for tomorrow: Chris is an international BD and innovation scout, not the payments owner; the group has just come out of two bankruptcies and is cutting cost; and which legal entity carries Boost Mobile after the restructuring is not clear from public filings.

---

## INTERNAL CONTEXT (Yuno only, not for external use)

**TL;DR battle card**
- Who: Chris Ergen, "International Business Development & Wireless Innovation at DISH Wireless", Littleton, CO. Joined DISH in 2014 as a business analyst scouting international markets (Cuba), moved to Dish Wireless in 2018 and "took over the Wireless Innovation team". Board director, Cuba Study Group. Not a payments operator. https://www.linkedin.com/in/chris-ergen/ ; https://cubastudygroup.org/about-us/members/
- Why now: Juan Pablo and Chris were both on the Bullhound Summit 2026 attendee list (Marbella, 23 to 26 Sep 2026); the invite was created from Juan Pablo's calendar on 27-Oct-2026. This is a CEO-to-innovation-lead conversation, so qualify before pitching.
- Four brands, four stacks, zero orchestration (Section 3). ~$1B a month of recurring consumer billing (Section 12). Six LatAm countries on six local collection stacks (Section 4).
- Lead with: one layer on top of Recurly, CSG and Kenan, not a rip-and-replace; LatAm fluency (Rappi, inDrive, Livelo); new market live in weeks.
- Do not: claim any payment method is missing; raise the Ergen family link (only an aggregator states it); quote cost numbers before Finance pricing policy.

**The meeting.** "Dish <> Yuno", Wed 28-Oct-2026, 8:30 to 9:00 AM PT (9:30 MT, 10:30 Bogotá), Google Meet meet.google.com/ewr-mouw-uqr. Organizer Juan Pablo Ortega (juan@y.uno), created by angelica@y.uno on 27-Oct-2026 17:10 UTC. Guests: Chris Ergen (accepted), German Tatis (accepted), Kara Pfeffer (kara.merchant@dish.com, optional, no response), Max Orcutt (jennings.orcutt@dish.com, no response), tyler.boscolo@dish.com (no response). German's attendance is marked optional on the invite.

**The other DISH attendees.** No public profile was found for Kara Pfeffer (the alias kara.merchant@ suggests a name change), Max (Jennings) Orcutt or Tyler Boscolo on LinkedIn, press, RocketReach or TheOrg. Do not state a title for any of them. Open with "which part of the international and wireless-innovation work do you each own?"

**Prior Yuno activity.** Salesforce has a "Dish Network" account (id 001Ps00000wq60oIAA) with no Gong calls or emails. Gmail holds only the invite. In Slack, Susana Awad asked the Bullhound bot to prep a "DISH TV" meeting on 23-Sep-2026; the bot's note rated DISH "Tier 1, moderate ICP fit, not in the top 15 chase order" and warned that Chris may not own payments (#bullhoundsummit-2026). No recap of that Marbella conversation was posted; ask Susana or Juan Pablo what was said before the call.

**Do not confuse.** Salesforce also holds "Dish México" (last activity Jul-2024; 100% MVS since 2022, not owned by DISH Network: https://en.wikipedia.org/wiki/Dish_M%C3%A9xico), "Dish TV India", "d2h (Dish TV)" and "Watcho (Dish TV)" (the Indian DishTV group, unrelated). None of them is this prospect.

**Yuno references that fit.** Subscription and recurring billing at scale (Yuno subscriptions engine, internal stats: 16 merchants, 135K subscriptions, approval 83% to 86%, 69K reactivated), LatAm local methods and cash networks, stablecoins and payouts, published stats on y.uno (up to 7% approval uplift, 30% recovered revenue, 27% savings on payment costs, 1,000+ payment methods, 190 countries). Peers that orchestrate, from prior internal research: HBO Max and Peacock on Spreedly; Sky appears on Spreedly's customer index (Section 11C). Use published cases only in front of the merchant: inDrive, Rappi, Livelo, Reserva.

---

## SECTION 1: Traffic by Country

Similarweb estimates for Sep-2026 (the headline figure sits under the "last 3 months" widget, so treat the period as approximate). DISH Network has no consumer domains outside the US; the international footprint is EchoStar's Hughes.

| Rank | Domain / Country | Traffic share | Est. monthly visits | Trend (MoM) | Source |
|---|---|---|---|---|---|
| 1 | sling.com: US 95.79%, Puerto Rico 0.61%, Canada 0.43%, India 0.24%, UK 0.20% | US-centric | 11.1M | +34.8% | https://www.similarweb.com/website/sling.com/ |
| 2 | boostmobile.com: US 94.92%, Mexico 0.62%, Colombia 0.42%, Brazil 0.18%, India 0.18% | US-centric | 8.4M | -13.0% | https://www.similarweb.com/website/boostmobile.com/ |
| 3 | dish.com: US 96.41%, Mexico 0.26%, Brazil 0.23%, India 0.20%, UK 0.17% | US-centric | 2.3M | +11.1% | https://www.similarweb.com/website/dish.com/ |
| 4 | hughesnet.com: US 83.79%, Mexico 2.13%, Brazil 2.01%, India 1.33%, Puerto Rico 1.11% | US + spill-over | 228.7K | -13.7% | https://www.similarweb.com/website/hughesnet.com/ |
| 5 | hughesnet.com.br: Brazil 99.58% | Brazil | 31.0K | -22.3% | https://www.similarweb.com/website/hughesnet.com.br/ |
| 6 | hughesnet.com.mx: Mexico 83.19%, US 16.81% | Mexico | 16.1K | -28.1% | https://www.similarweb.com/website/hughesnet.com.mx/ |
| 7 | hughesnet.com.co: Colombia 85.15%, US 12.92%, Peru 1.93% | Colombia | 13.3K | +7.4% | https://www.similarweb.com/website/hughesnet.com.co/ |

Flags: no non-US market exceeds 5% on any DISH brand. LATAM presence is real but sits in the Hughes regional domains (Brazil, Mexico, Colombia, plus Peru, Chile and Ecuador sites not measured). The three HughesNet LatAm domains are all shrinking month on month, consistent with Hughes' stated shift from consumer to enterprise (Section 6). Puerto Rico appears on both sling.com and hughesnet.com. No traffic data for hughesnet.com.pe, hughesnet.cl, hughesnet.com.ec or hughes.in: not found.

---

## SECTION 2: Legal Entities

| Country | In top traffic? | Local entity | Cross-border risk | Source |
|---|---|---|---|---|
| United States | Yes (all brands) | DISH Network Corporation (NV), DISH DBS Corporation (CO), DISH Network L.L.C. (CO), DISH Wireless Holding L.L.C., DISH Wireless L.L.C., Hughes Satellite Systems Corporation (CO), Hughes Communications, Inc. (DE); Sling TV L.L.C., Sling Media L.L.C., DISH Technologies L.L.C., Hughes Network Systems, L.L.C. named as wholly owned in the 10-K | No | https://www.sec.gov/Archives/edgar/data/1415404/000110465926021817/tmb-20251231xex21.htm ; https://www.sec.gov/Archives/edgar/data/1415404/000110465926021817/tmb-20251231x10k.htm ; https://www.sling.com/legal |
| Brazil | Yes (hughesnet.com.br) | Hughes Telecomunicações do Brasil ("HTB"), named in the 10-K (São Paulo tax claim); no razão social or CNPJ printed on the site | No | 10-K above ; https://www.hughesnet.com.br/ |
| Mexico | Yes (hughesnet.com.mx) | Hughes de México, Bosques de Chiapas 21, Tlalnepantla, Edo. de México (suffix not shown) | No | https://www.hughesnet.com.mx/aviso-de-privacidad |
| Colombia | Yes (hughesnet.com.co) | Hughes de Colombia S.A.S., NIT 900.971.687-1 | No | https://www.hughesnet.com.co/ |
| Peru | Site only | Hughes de Perú (name as printed on the BCP payment instructions) | Not assessed | https://www.hughesnet.com.pe/pagos |
| Chile | Site only | Entity name not printed; Servipag/Webpay collection codes 69210 and 69270 | Not assessed | https://hughesnet.cl/pagos |
| Ecuador | Site only | Hughes del Ecuador HDE CIA LTDA (printed on the Edoc payment portal) | No | https://www.hughesnet.com.ec/pagos |
| India | Low (1.33% of hughesnet.com) | Hughes Communications India Private Limited ("HCIPL"), wholly owned; enterprise and government only | No | 10-K above ; https://www.hughes.in/ |
| Ireland / Europe | No consumer traffic | EchoStar Mobile Limited, registered in Ireland, S-band licence covering the EU, UK and Scandinavia (IoT, B2B) | N/A | https://www.echostarmobile.com/privacy-policy/ ; https://www.echostarmobile.com/about/regulatory/ |
| Puerto Rico | 0.61% sling.com, 1.11% hughesnet.com | No separate entity found (US territory, served from US entities) | Low | Similarweb pages above |

Cross-reference: every market with meaningful traffic has a local operating entity, so there is no obvious cross-border acquiring gap. The real entity question is internal, not geographic: DISH DBS and its subsidiaries (including DISH Wireless L.L.C.) filed Chapter 11 on 30-Jun-2026 and DISH DBS emerged on 1-Oct-2026, while the DISH Wireless assets were split off into a Section 363 sale with EchoStar as stalking horse (Section 6). Which entity carries the Boost Mobile retail business today is not stated in public sources [INFERENCE, not confirmed]: ask on the call which entity would contract.

> ⚠️ MANUAL: verify contracting entities on the brand T&Cs and the post-emergence 8-K before any proposal.

---

## SECTION 3: Payment Stack

**3A. PSPs, billing platforms and acquirers**

| Brand / Country | Vendor | Role | Evidence | Source |
|---|---|---|---|---|
| Sling TV, US | Recurly | Subscription billing and card tokenization (recurly.configure, #recurly-payment-form, Visa/MC/Amex/Discover brands) | [Source Code] | https://www.sling.com/etc.clientlibs/sling-television/clientlibs/clientlib-site.min.js |
| Sling TV, US | Kount | Fraud screening inside Recurly's fraud config (kountMerchantId, kountSessionId) | [Source Code] | same bundle |
| Sling TV, US | PayPal, Apple Pay, Google Pay (googleMerchantId), Amazon Pay, BitPay | Wallet and crypto handlers in the checkout bundle; "Express Pay" on the help page | [Source Code] [Help Page] | same bundle ; https://www.sling.com/help/en/account-questions/billing-payments/billing-faq |
| Sling TV, US | Apple, Google, Amazon app stores | Third-party partner billing for app-store sign-ups | [Help Page] | https://www.sling.com/help/en/account-questions/gift-cards/gift-cards-explained |
| Sling TV, US | Recurly (corroboration) | Recurly investor Accel-KKR lists Sling TV among Recurly customers; Recurly's own customer page no longer shows it | [Case Study] | https://www.accel-kkr.com/portfolio-company/recurly/ |
| DISH TV, US | CSG Systems | Guest "Pay now, no sign-in" portal hosted at paymentportal.csgweb.com/dish/ | [Help Page] [Checkout] | https://support.dish.com/getting-started/billing-and-payments |
| DISH TV, US | Google Pay (pay.google.com/gp/p/js/pay.js), Apple Pay (ApplePaySession label "DISH NETWORK"), PayPal ("payPalProcessing"), BitPay | Wallet and crypto handlers on my.dish.com | [Source Code] | https://www.mydish.com ; https://my.dish.com/static/js/vendor-1fe33b30.7f154674.js |
| DISH TV, US | MoneyGram Express Payments, Western Union Payments, CheckFreePay | Cash bill-pay networks ("processing fees may apply") | [Help Page] | https://support.dish.com/getting-started/billing-and-payments |
| DISH TV, US | Coinbase (2014) then BitPay (Oct-2018, added Bitcoin Cash) | Crypto acceptance history | [Press coverage] | https://pymnts.com/?p=532925 ; https://www.financemagnates.com/cryptocurrency/news/pay-tv-provider-dish-now-accepts-bitcoin-cash-as-a-payment-option/ |
| Boost Mobile, US | Amdocs Kenan / Optima | Wireless billing stack ("Senior Engineer Optima/Kenan Development", Bengaluru, Mar-2025, 4+ years Amdocs Kenan) | [Job Listing] | https://jobs.spacetalent.org/companies/dish-network/jobs/47551314-senior-engineer-optima-kenan-development |
| Boost Mobile, US | Optima, GoTransverse, Zuora, Recurly, Aria (listed as relevant billing systems) | "Staff Charging Platform Engineer", Aurora CO | [Job Listing, snippet only] | https://www.echostar.com/gfj/staff-charging-platform-engineer-aurora-co-68bab1ce4b22d2045fb6dd75 (now 404) |
| Boost Mobile, US | Affirm | Device financing, 0% to 36% APR, 24-month term, new customers on boostmobile.com; "your payments will be handled by Affirm" | [Help Page] [Checkout] | https://www.boostmobile.com/phone-financing-affirm ; https://help.boostmobile.com/docs/financing-affirm |
| Boost Mobile, US | In-house BNPL account type | "If you finance a device directly through Boost, your account will become a Buy Now, Pay Later account", requires AutoPay and a soft credit check (updated 30-Jun-2026) | [Help Page] | https://help.boostmobile.com/docs/account-types |
| Boost Mobile, US | Apple Pay, Google Pay | Accepted at checkout on boostmobile.com and for AutoPay in app and online (help page updated 18-Aug-2026) | [Help Page] | https://help.boostmobile.com/docs/boost-mobile-plan-billing-and-payments |
| Boost Mobile, US | Alviere + Community Federal Savings Bank | OmniMoney no-fee checking, debit card and remittances to Mexico (launched 27-Oct-2022) | [Press Release] | https://www.prnewswire.com/news-releases/boost-mobile-expands-into-financial-services-arena-with-launch-of-omnimoney--no-fee-digital-checking-account-301661282.html |
| Boost Mobile, US | T-Mobile billing (historical) | 2022: Boost still ran on T-Mobile's billing system while DISH migrated to its own | [Press coverage] | https://www.lightreading.com/5g/wide-launch-of-dishs-boost-infinite-service-slips-to-q1-2023-/d/d-id/781531 |
| HughesNet, US | None named | Cards (MC, Visa, Amex, Discover) with automatic recurring billing; ACH via debit-card activation; $5/month paper-invoice fee; hughesnet.com HTML shows only Ketch consent and GTM | [T&Cs] [Source Code] | https://legal.hughesnet.com/SubAgree8.23.22 |
| HughesNet, Colombia | PayU (labelled "pago vía web"), Facture (plataformav3.facture.co, PSE module) | Online card/PSE collection and e-invoice bill pay | [Help Page] [Source Code] | https://www.hughesnet.com.co/pagos |
| HughesNet, Chile | Webpay Plus (Transbank product), Servipag | Online card and cash collection | [Help Page] | https://hughesnet.cl/pagos |
| HughesNet, Mexico | Own portal mi.hughesnet.com.mx (Angular), SPEI, BBVA, OXXO and nine other cash networks, Mercado Pago, Rappi, Cashi, UnDosTres, Yomp, Intercambio Express (from the US) | Collection rails | [Help Page] | https://www.hughesnet.com.mx/pagos |
| HughesNet, Brazil | Boleto (BB, Bradesco, Itaú, Caixa, Santander, Sicredi, Bancoob), débito automático, PEC Caixa; selfcare on Salesforce Lightning | Collection rails | [Help Page] [Source Code] | https://www.hughesnet.com.br/perguntas-frequentes/ |
| HughesNet, Peru | Yape (BCP), PagoEfectivo, BCP channels (agent code 20859) | Collection rails | [Help Page] | https://www.hughesnet.com.pe/pagos |
| HughesNet, Ecuador | Edoc portal (ech.edocnube.com), Servipagos, Pago Ágil, Mi Vecino (Banco Pichincha) | Collection rails | [Help Page] | https://www.hughesnet.com.ec/pagos |

Card acquirers for Sling, DISH TV and Boost: not found. Recurly abstracts the gateway for Sling, the CSG portal abstracts it for DISH TV, and the Boost checkout is a JavaScript shell with no gateway host visible. Searches for Stripe, Adyen, Braintree, Worldpay, Checkout.com, Fiserv, ACI and PayNearMe returned nothing linked to any DISH brand. The 17 "Stripe" strings on help.boostmobile.com are ReadMe platform configuration, not a Boost vendor.

**3B. Orchestrator.** No public evidence found. Searches for Spreedly, Primer, Gr4vy, CellPoint and APEXX returned nothing for DISH, Sling, Boost or Hughes, and none of the fetched bundles reference an orchestration SDK.

> ⚠️ MANUAL, DevTools on sling.com/get-started and boostmobile.com checkout with test card 4111 1111 1111 1111 | 02/30 | 123 to surface the gateway behind Recurly and the Boost card form.

---

## SECTION 4: APMs (Agent D findings)

**4A. Confirmed APMs** (official pages fetched 27-Oct-2026)

| Market | APMs confirmed | Verification source | Source URL |
|---|---|---|---|
| DISH TV, US | Apple Pay, Google Pay, PayPal, credit or debit card, bank account (ACH), Bitcoin (BitPay), AutoPay, eBill, cash at MoneyGram / Western Union / CheckFreePay, check by mail, text "PAY BILL" to 46764, phone 866-595-4587, pay from the Hopper or Wally receiver, guest pay without sign-in. Fees: late $15 ($10 in VA, ME, AZ), returned check or EFT $20, payment extension $15 | Help page, fees page, page source | https://support.dish.com/getting-started/billing-and-payments ; https://support.dish.com/billing/fees ; https://www.mydish.com |
| Sling TV, US | Debit and credit cards; "Express Pay at checkout to use tools like PayPal, Apple Pay, Google Pay and Amazon Pay"; Sling gift cards; app-store billing through Amazon, Google or Apple | Help page (raw HTML) | https://www.sling.com/help/en/account-questions/billing-payments/billing-faq ; https://www.sling.com/help/en/account-questions/gift-cards/gift-cards-explained |
| Boost Mobile, US | Visa, Mastercard, American Express, Discover; Apple Pay and Google Pay at checkout and for AutoPay; AutoPay ($5/month discount, required on some plans); Affirm device financing; "Buy Now, Pay Later Available" badge on Unlimited+ and Premium plans; pay in store, online, in app or via Customer Care; free guest payment by automated phone; $4 fee for agent-assisted payments. Merchant's own statement: "We do not currently accept prepaid debit or credit cards on boostmobile.com" | Help page, homepage, Affirm page | https://help.boostmobile.com/docs/boost-mobile-plan-billing-and-payments ; https://www.boostmobile.com/phone-financing-affirm |
| HughesNet, US | MasterCard, Visa, American Express, Discover with automatic recurring billing; ACH via debit-card authorization; paper invoice with $5.00/month fee; checks (returned check up to $25) | Residential Subscriber Agreement (8.23.22) | https://legal.hughesnet.com/SubAgree8.23.22 |
| HughesNet, Brazil | Boleto bancário (internet banking, ATM, branch, lotérica), cartão de crédito Visa and Mastercard, débito automático (Banco do Brasil, Bancoob, Banrisul, Caixa, Santander, Sicredi), PEC Caixa, recarga de dados; boleto priced above card and débito | FAQ page | https://www.hughesnet.com.br/perguntas-frequentes/ |
| HughesNet, Mexico | Card (crédito/débito, Visa and Mastercard) via mi.hughesnet.com.mx; domiciliación to card with a $100 MXN/month discount (Jan-2026 to Dec-2027); SPEI; BBVA branch; cash at OXXO, 7-Eleven, MTC, Farmacia Benavides, Farmacia del Ahorro, Farmapronto, Walmart, Sam's, Bodega Aurrera, Financiera para el Bienestar; apps Mercado Pago, Rappi, Cashi, UnDosTres, Yomp; from the US via Intercambio Express | Pagos page | https://www.hughesnet.com.mx/pagos |
| HughesNet, Colombia | PSE (any bank account), cards MasterCard, Visa, American Express, Diners in Mi Cuenta, Efecty cash (convenio 112856), Su Red / Pagatodo (Gana, Su Chance, Acertemos), PayU web payment, Facture "Paga tu Factura" portal | Pagos page, portal source | https://www.hughesnet.com.co/pagos |
| HughesNet, Peru | Yape (BCP), PagoEfectivo coupon, cards Visa, MasterCard, American Express, Diners in Mi Cuenta, BCP channels (agentes code 20859); due within 20 days | Pagos page | https://www.hughesnet.com.pe/pagos |
| HughesNet, Chile | Pago Automático with debit or credit card, Webpay Plus, Servipag online and in person (codes 69210, YoPAG 69270) | Pagos page | https://hughesnet.cl/pagos |
| HughesNet, Ecuador | Recurring credit card (Titanium, American Express, Mastercard, Visa, Diners), Servipagos, Pago Ágil (cash or debit), Mi Vecino Pichincha stores; due within 15 days | Pagos page, Edoc portal | https://www.hughesnet.com.ec/pagos |

**4B. Unverified markets and steps**

| Market / step | Verification attempted? | Reason not verified | Popular local APMs (for reference only) |
|---|---|---|---|
| Hughes India (hughes.in, hughesnet.in) | Yes | Enterprise and government site only; consumer pages 404; hughesnet.in empty | UPI, net banking, cards |
| Sling TV live payment step | Yes | Account-first flow behind an email gate at /get-started; home.sling.com returns 403 | Venmo, Cash App Pay (not seen) |
| Boost Mobile card-entry step | Yes | /shop/check-compatibility errored; checkout is a JavaScript shell; boostmobile.com/reboost is 404 | PayPal, Venmo, cash at retail, PayNearMe (none seen on current official pages) |
| DISH TV order flow | Yes | "Add to Cart" hands off to webapps.dish.com, not captured | N/A |
| HughesNet US self-care portal | Yes | my.hughesnet.com is an Angular SPA | N/A |
| HughesNet Brazil, Pix | Yes | Only "pix" strings in source are city names | Pix |
| HughesNet Colombia, Nequi / Daviplata / Baloto | Yes | Listed only by third-party site Selectra, not on the official page | Nequi, Daviplata, Baloto |
| Puerto Rico (Sling, HughesNet) | No | No PR-specific page located | ATH Móvil |

> "Not verified" ≠ "not available". ⚠️ MANUAL: walk sling.com/get-started and boostmobile.com checkout with a US card before any APM claim in front of the merchant.

---

## SECTION 5: Payment Complaints

| Issue type | Platform | Frequency | Date range | Source |
|---|---|---|---|---|
| Sling TV: duplicate charge ("charged me double for one month") | Trustpilot (TrustScore 1.1, 2,732 reviews) | Recurrent | 1-Oct-2026 | https://www.trustpilot.com/review/sling.com |
| Sling TV: unselected premium add-ons billed ($149 overnight), refund refused | Trustpilot | Recurrent | 18-Oct-2026 | same |
| Sling TV: "asked for a refund and I got charged again" | Trustpilot | Recurrent | 12-Oct-2026 | same |
| Sling TV: "charged my card without my permission ... refund never happen" | Trustpilot | Recurrent | 6-Oct-2026 | https://www.trustpilot.com/review/sling.com?page=2 |
| Sling TV: chargeback intent ("disputing the charge based on the false advertising") | Trustpilot | Occasional | 3-Oct-2026 | same |
| Sling TV: refund denied after cancellation | Trustpilot | 8 of ~20 reviews on page 2 | 19-Sep to 6-Oct-2026 | same |
| DISH TV: cancellation fees over $300 / $400 plus $25 return box | Trustpilot (TrustScore 1.2, 1,506 reviews, 81% one star) | Dominant theme | 28-Aug and 24-Sep-2026 | https://www.trustpilot.com/review/dish.com |
| DISH TV: billing dispute sent to collections (Valor Intelligence) for $100 | Trustpilot | Occasional | 29-Sep-2026 | same |
| DISH TV: bill above the agreed price, 24-month credits with no price lock | Trustpilot | Recurrent | 17-Oct-2026 | same |
| Boost Mobile: AutoPay charged without consent, no refund, users recommend one-time virtual cards so renewal "will get declined" | Slickdeals thread | Occasional | 21-Feb to 3-Mar-2025 | https://slickdeals.net/f/18132763-boost-mobile-buy-6-months-get-6-months-free-unlimited-plan-300 |
| Boost Mobile: "trouble getting the credit approved each month ... billing issues have been resolved" | Trustpilot (TrustScore 3.9, 32,486 reviews, mostly positive) | Rare | 26-Oct-2026 | https://www.trustpilot.com/review/boostmobile.com |

Policy context: Boost's T&Cs (updated 25-Aug-2026) reserve "the right to retry your payment method" when AutoPay fails, give postpaid customers a 10-day grace period to update the method, and state that payments are not refunded on cancellation. https://help.boostmobile.com/docs/general-terms-conditions ; https://help.boostmobile.com/docs/boost-mobile-plan-billing-and-payments

Reddit and BBB: no public information found (reddit not fetchable, BBB returned no pages).

Analysis: the Sling pattern is entitlement and refund policy more than card authorization, but "charged twice" and "charged again after asking for a refund" are payment-layer symptoms that idempotent retries, a single ledger per customer and real-time monitors would remove. The Boost pattern (customers deliberately using cards that will decline on renewal) is the dark side of blunt AutoPay retry logic. Neither pattern is a public "my card was declined" problem, so do not pitch decline rates from reviews; pitch them from the ARPU and churn maths in Section 12. [INFERENCE, not confirmed]: the uniform "no refunds" stance across Sling and Boost reflects cost pressure after the 2026 restructuring.

---

## SECTION 6: Expansion and Corporate Developments (last 24 months)

| # | Date | Development | Category | Source |
|---|---|---|---|---|
| 1 | 30-Sep-2024 | DISH / DirecTV merger abandoned after bondholder opposition; DirecTV 100% TPG since 2-Jul-2025 | M&A (failed) | https://en.wikipedia.org/wiki/DirecTV |
| 2 | 25/26-Aug-2025 | AT&T agrees to buy 3.45 GHz and 600 MHz spectrum for $22.65B; Boost to become a hybrid MNO on AT&T's RAN with its own cloud 5G core, T-Mobile MVNO continues | Divestiture | https://www.sec.gov/Archives/edgar/data/1001082/000141540425000035/tmb-20250825xex99.htm ; https://insidetowers.com/?p=64273 |
| 3 | 8-Sep-2025 | SpaceX agrees to buy AWS-4 and H-block for ~$17B (half cash, half SpaceX stock; SpaceX funds ~$2B of EchoStar interest through Nov-2027); Boost subscribers to get Starlink Direct to Cell | Divestiture | https://www.sec.gov/Archives/edgar/data/1001082/000141540425000041/tmb-20250907xex99d1.htm |
| 4 | 6-Nov-2025 | SpaceX adds the unpaired AWS-3 portfolio for ~$2.6B in stock | Divestiture | https://www.prnewswire.com/news-releases/echostar-agrees-to-sell-full-unpaired-aws-3-spectrum-license-portfolio-to-spacex-302606455.html |
| 5 | 15-Nov-2025 | Zero customer traffic left on Boost's own 5G network; hybrid MNO model live; own RAN being decommissioned | Operations | https://www.sec.gov/Archives/edgar/data/1415404/000110465926089370/sats-20260630x10q.htm |
| 6 | 2-Mar-2026 | FY2025 results: revenue $15.0B, net loss $14.5B incl. ~$17.6B impairments; 7.00M pay-TV, 7.51M wireless, 739K broadband subs | Financials | https://finviz.com/news/326589/echostar-announces-financial-results-for-the-three-and-twelve-months-ended-december-31-2025 |
| 7 | 14-Apr-2026 | Hughes wins Air India in-flight connectivity | Expansion (B2B) | https://www.hughes.com/resources/press-releases |
| 8 | 12-May-2026 | FCC approves both spectrum sales; $2.4B escrow for tower litigation; SpaceX close expected around Nov-2027 | Regulatory | https://capacityglobal.com/news/fcc-approves-40bn-echostar-spectrum-sale/ ; https://www.telecompetitor.com/fcc-approves-att-and-starlink-purchases-of-echostar-spectrum/ |
| 9 | 26-Jun-2026 | Chief Legal Officer Dean Manson resigns; Jeffrey Blum acting CLO | Leadership | https://www.lightreading.com/satellite/hamid-akhavan-exiting-echostar-amid-change-in-strategic-direction- |
| 10 | 30-Jun-2026 | DISH DBS Corporation and subsidiaries (including DISH Wireless L.L.C. entities) file a prepackaged Chapter 11 in S.D. Texas; >88% of noteholders signed the RSA; trigger was the $2B 7.75% notes due 1-Jul; DISH TV and Sling service unaffected; EchoStar, Boost Mobile, Gen Mobile and Hughes reported outside the filing; $9.729B non-cash deconsolidation gain | Restructuring | https://www.lightreading.com/finance/dish-turns-to-chapter-11 ; https://www.advanced-television.com/2026/07/01/echostar-confirms-dish-dbs-bankruptcy/ ; 10-Q above |
| 11 | 6-Jul-2026 | CEO Hamid Akhavan resigns effective immediately ("change in strategic direction"); Charlie Ergen (chairman, president, CEO) takes direct charge; EchoStar Capital folded into corporate development under EVP Tom Cullen | Leadership | Light Reading, 7-Jul-2026 (URL in row 9) |
| 12 | Jul-2026 | EchoStar is stalking-horse bidder for substantially all DISH Wireless assets (Section 363); FTI marketing to third parties | M&A | 10-Q above ; https://chapter11cases.com/blogs/news/dish-dbs-corporation-a-prepackaged-plan-and-a-363-sale-under-one-roof |
| 13 | 28-Jul-2026 | AT&T sale closes: $20.25B proceeds plus $2.4B into an FCC "Wireless Creditor Trust"; $3.686B 11.75% notes redeemed; DISH DBS repays the $2B notes | Divestiture | https://www.sec.gov/Archives/edgar/data/1415404/000141540426000035/sats-20260728x8k.htm ; https://broadbandbreakfast.com/echostar-at-t-close-23-billion-spectrum-sale/ |
| 14 | 2-Aug-2026 | Hughes Satellite Systems Corp and US subsidiaries (incl. Hughes Network Systems LLC) file Chapter 11 without a pre-negotiated plan after missing a $1.5B maturity; international subsidiaries excluded; refocus on enterprise, government and defense; consumer HughesNet to wind down over time; CRO Robert Del Genio; 330 Maryland layoffs from 22-Sep | Restructuring | https://www.sec.gov/Archives/edgar/data/1415404/000141540426000038/sats-20260728xex99.htm ; https://www.advanced-television.com/2026/08/03/hughes-network-files-for-bankruptcy/ |
| 15 | 3-Aug-2026 | Q2-2026 results: revenue $3.58B; DISH TV 4.68M (-161K), Sling 1.71M (-80K), wireless 7.38M (-118K), broadband 622K (-59K); wireless OIBDA positive $50.8M | Financials | https://www.taiwannews.com.tw/en/news/6413699 ; https://www.advanced-television.com/2026/08/03/echostar-q2-revenue-falls/ |
| 16 | 7-Aug-2026 | Hughes management plan filed: international enterprise revenue $239M (2025) to $364M (2030) across Brazil, Europe, LATAM, India, ROW | Strategy | https://www.sec.gov/Archives/edgar/data/1415404/000141540426000042/sats-20260807xex99d1.htm |
| 17 | 24/25-Aug-2026 | US Trustee seeks an examiner over allegations that Ergen stripped ~$1.5B from Hughes (satellite lease, dividends, tax payment, SpaceX participation); lenders seek control 17-Sep | Litigation | https://www.advanced-television.com/2026/08/25/hughes-satellite-bankruptcy-wants-court-examiner/ |
| 18 | 16-Sep-2026 | Hughes supplies a Jupiter gateway to NIGCOMSAT (Nigeria) | Expansion (B2B) | https://www.hughes.com/resources/press-releases |
| 19 | 1-Oct-2026 | DISH DBS plan effective: ~$4.35B debt reduction, reconsolidated into EchoStar; plan bifurcated from DISH Wireless | Restructuring | https://www.sec.gov/Archives/edgar/data/1415404/000141540426000048/sats-20261001x8k.htm ; https://www.advanced-television.com/2026/10/05/echostars-dish-dbs-exits-bankruptcy/ |
| 20 | ~Sep/Oct-2026 | Job: Program Manager I, Billing and Credit PMO, EchoStar Englewood ($63K to $90K), liaison between Wireless Billing/Credit and IT | Hiring | https://www.builtincolorado.com/job/program-manager-i-billing-and-credit-pmo/10469019 |

Not found: any 2026 DirecTV revival, any sale of DISH TV or Sling, any sale of the Hughes international units, any CFO, CDO or VP Payments change, any public payments RFP, any Boost Mobile international launch. Headcount: ~12,100 employees at 31-Dec-2025, of which ~600 international (10-K).

---

## SECTION 7: Payment News (last 12 to 18 months)

| # | Date | Headline | Relevance | Source |
|---|---|---|---|---|
| 1 | help page updated 20-May-2026 | 🟢 Boost Mobile x Affirm: 0% to 36% APR device financing over 24 months, new customers online only | Boost has a live BNPL partner at checkout | https://www.boostmobile.com/phone-financing-affirm ; https://help.boostmobile.com/docs/financing-affirm |
| 2 | 30-Jun-2026 | 🟢 Boost in-house "Buy Now, Pay Later account" type for devices financed directly, with AutoPay and a soft credit check | Boost carries its own device receivables | https://help.boostmobile.com/docs/account-types |
| 3 | 18-Aug-2026 | 🟢 Boost confirms Apple Pay and Google Pay at checkout and for AutoPay; prepaid cards not accepted on the web; $4 assisted-payment fee | Wallet coverage and web friction | https://help.boostmobile.com/docs/boost-mobile-plan-billing-and-payments |
| 4 | undated page | 🟢 Boost x Chime: $25/month BYOD plan when the bill is paid with a Chime Visa card | Fintech co-marketing on payment method | https://www.boostmobile.com/plans/byod |
| 5 | 22-Jan-2026 | Sling TV raises prices (Blue locals fee $5 to $9; Orange & Blue $60.99 to $64.99; existing customers from 20-Feb-2026) | Price increase into a shrinking base | https://cordcuttersnews.com/sling-tv-is-raising-its-price-this-month/ |
| 6 | 5-Aug-2026 | Liberty Latin America signs a 10-year Amdocs deal (peer, not DISH) | Regional telco billing consolidation trend | https://www.lla.com/our-brands |

🔴 Removals: none found. No PayPal, Venmo, Klarna, PayNearMe, Fiserv, Amazon Pay or Roku Pay announcements with any DISH brand in the window. Older context: Coinbase 2014 and BitPay 2018 (Section 3), Green Dot retail cash (https://www.nexttv.com/news/echostar-teams-green-dot-302389).

---

## SECTION 8: Checkout Audit (desk audit, 27-Oct-2026)

| Dimension | Finding | Quality | Notes |
|---|---|---|---|
| Checkout type | Sling: own domain, Recurly-embedded card form, wallets as "Express Pay". Boost: own-domain multi-step shop (/shop/devices, /check-compatibility, /checkout/cart, /activation). DISH: marketing site hands off to webapps.dish.com, 2-year commitment with ETF and eAutoPay, "requires credit qualification", phone ordering pushed. HughesNet: address-gated plan finder with CAPTCHA, order by phone or dealer | Mixed | Four brands, four flows, no shared component. https://www.sling.com ; https://www.boostmobile.com ; https://www.dish.com/packages ; https://www.hughesnet.com/get-started |
| Guest checkout | Sling: account-first ("Enter your email ... we'll help you create one"). Boost: email tied to purchase for activation. DISH and HughesNet: no guest flow, credit check | Weak | Sling: https://www.sling.com/get-started?classification=us&plan=one-month&plan_offer=monthly-web |
| Steps to purchase | Boost BYOP: 4 steps (IMEI, number, plan, SIM/eSIM). Sling: plan grid then email then payment. DISH and HughesNet: lead capture then phone or external app | Average | Payment steps NOT VERIFIED on all four |
| 3DS | Not observed on any captured page | Not verified | US-centric flows; no 3DS prompt seen |
| Mobile experience | Boost mobile nav present; Sling and DISH responsive marketing pages | Average | Not walked on a device |
| APM display logic | Sling lists wallets on the help page, not on the plan grid. Boost shows the Affirm logo and "Buy Now, Pay Later Available" badges on the homepage. DISH shows a Spanish pop-up "¿Tienes tarjeta de crédito?" with "otras opciones de pago disponibles por teléfono". HughesNet LatAm: one template per country with the local rails listed on /pagos | Average | DISH pushes non-card customers to the phone channel |
| Trial / card capture | Sling: "Your credit card will be charged monthly ... until you cancel"; no free-trial wording seen | N/A | Price shown before email capture |

> ⚠️ MANUAL: walk sling.com and boostmobile.com with a US card and a VPN in Puerto Rico; DevTools for the gateway behind Recurly.

---

## SECTION 9: PCI DSS

| PCI DSS level | Card data handling | Recommended Yuno integration | Source |
|---|---|---|---|
| Not published. The FY2025 10-K and the Q1-2025 DISH 10-Q contain zero occurrences of "PCI", "Payment Card Industry", "credit card" or "cardholder". No public attestation or trust page for DISH, EchoStar, Sling or Boost was found | Sling tokenizes through Recurly (hosted fields in the bundle). DISH TV guest payments run through a CSG-hosted portal. Boost card form not captured. Cybersecurity program "informed in part by the NIST Cybersecurity Framework", CISO with 25+ years, monthly briefings, past cyber-attacks acknowledged | Yuno vault as the single token store across brands (network tokens plus PSP tokens), SDK or hosted fields to keep each brand in SAQ-A scope, with Recurly, CSG and Kenan kept as the billing systems of record [INFERENCE on scope, not confirmed] | https://www.sec.gov/Archives/edgar/data/1415404/000110465926021817/tmb-20251231x10k.htm |

---

## SECTION 10: Strategic Insights

**Insight 1: Four brands, four payment stacks, no shared layer.**
Evidence: Section 3 (Recurly + Kount for Sling; CSG portal for DISH TV; Amdocs Kenan/Optima plus Affirm for Boost; cards and ACH for HughesNet US). | Pain point: duplicated vendor contracts, four separate wallet integrations (Apple Pay and Google Pay are integrated at least three times), no cross-brand routing, no single vault, and a group that just cut $4.35B of debt and is hunting cost. | Yuno value prop: one integration that sits above Recurly, CSG and Kenan, consolidates acquirer contracts, routes every charge to the cheapest approving path and gives Finance one reconciliation view; published 27% savings on payment costs. | Best case: Rappi (zero implementation time, 80% less analyst resolution time). | Outreach angle: "You run at least four payment stacks for one customer base; Yuno makes them one without touching the billing systems."

**Insight 2: Roughly $1B a month of recurring consumer billing with rising churn.**
Evidence: Section 12 (pay-TV ARPU $112.39 on 6.39M subscribers, Boost ARPU $38.60 on 7.38M, Q2-2026); DISH TV monthly churn 1.42%, Boost 2.88%; Sling lost 80K subscribers in Q2-2026 while raising prices. | Pain point: every failed renewal on a $112 ticket is lost margin on a base that is already shrinking; retries today are blunt (Boost T&Cs: "right to retry your payment method"), and Sling customers report being charged twice. | Yuno value prop: smart retries, account updater and network tokens, routing by issuer and BIN, idempotent retries; published up to 7% approval uplift and 30% recovered revenue; the Yuno subscriptions engine lifted approval from 83% to 86% across 16 merchants (internal). | Best case: Livelo (+5% approval, 50% recovery). | Outreach angle: "On $112 a month per household, every recovered decline is a saved subscriber, not a saved transaction."

**Insight 3: Six HughesNet countries, six collection stacks, carved out of the bankruptcy.**
Evidence: Section 4 (PayU and Facture in Colombia, Webpay and Servipag in Chile, OXXO/SPEI/Mercado Pago in Mexico, boleto in Brazil, Yape and PagoEfectivo in Peru, Servipagos and Edoc in Ecuador); Section 6 rows 14 and 16 (international subsidiaries excluded from the Hughes Chapter 11; international enterprise revenue planned to grow from $239M to $364M by 2030). | Pain point: each country team maintains its own portal, acquirer and cash network; consumer HughesNet is winding down in the US, so the LatAm units need to run lean. | Yuno value prop: one integration for all local rails and local acquiring, new market or new rail live in weeks, Pix and other methods switched on without code. | Best case: inDrive (10 LatAm markets in under 8 months, 90% approval, 4.5% recovery). | Outreach angle: "Your Colombian, Chilean, Mexican, Brazilian, Peruvian and Ecuadorian teams each built their own collection stack; Yuno runs all six through one API."

**Insight 4: Chris Ergen's remit is new markets and new products, and DISH has a history of paying first.**
Evidence: Internal Context (international BD since 2014, Wireless Innovation since 2018); Section 3 (DISH took Bitcoin through Coinbase in 2014 and BitPay from 2018); Section 6 (Starlink Direct to Cell for Boost subscribers, EchoStar Mobile in Europe, Hughes B2B wins in India and Nigeria). | Pain point: any new consumer product or market needs local payment acceptance on day one, and today each DISH brand would build it again from scratch. | Yuno value prop: 1,000+ payment methods in 190 countries behind one API, no-code PSP enablement, stablecoin rails for a crypto-friendly house. | Best case: inDrive. | Outreach angle: "Whatever your team launches next, payments should not be the thing that delays it."

**Insight 5: Boost's prepaid base is under-served on the web.**
Evidence: Section 4 (merchant statement: no prepaid debit or credit cards on boostmobile.com; cash only in store; $4 fee for assisted payments); Section 5 (AutoPay complaints, customers using single-use cards to force declines); Section 3 (OmniMoney remittances to Mexico, Chime co-marketing). | Pain point: 7.38M mostly prepaid subscribers, many unbanked or thin-file, pushed to stores or paid phone support to pay; blunt retries create disputes. | Yuno value prop: cash and wallet networks on the web, fraud orchestration that lets prepaid cards through safely [INFERENCE, not confirmed that fraud is the reason for the block], retry rules per plan type. | Best case: Rappi. | Outreach angle: "Boost's own help page tells prepaid customers their prepaid card will not work online; that is a routing and risk problem Yuno solves."

---

## SECTION 11: Pipeline

**11A. Direct competitors**

| Company | Website | HQ | Est. size | Overlap markets | Source |
|---|---|---|---|---|---|
| DirecTV | directv.com | El Segundo, CA (satellite ops Englewood, CO) | 100% TPG; no recent sub count | US | https://en.wikipedia.org/wiki/DirecTV |
| YouTube TV | tv.youtube.com | San Bruno, CA | >10M subs (Nov-2025) | US | https://en.wikipedia.org/wiki/YouTube_TV |
| Fubo (incl. Hulu + Live TV) | fubo.tv | New York | 5.75M NA subs, $1.48B Q3-2026 revenue; Disney 70% since 29-Oct-2025 | US, Canada, Spain | https://en.wikipedia.org/wiki/Fubo |
| Philo | philo.com | San Francisco | ~1.3M subs, ~$450M 2024 revenue | US | https://en.wikipedia.org/wiki/Philo_(company) |
| Charter Spectrum | corporate.charter.com | Stamford, CT | $54.77B 2025; Cox merger closed 20-Aug-2026 | US | https://en.wikipedia.org/wiki/Charter_Communications |
| Comcast Xfinity | xfinity.com | Philadelphia | $123.7B 2025; NBCU + Sky spin planned by summer 2027 | US | https://en.wikipedia.org/wiki/Comcast |
| Starlink | starlink.com | Redmond, WA | ~13.6M subs (30-Sep-2026), $11.4B 2025 revenue | ~160 countries | https://en.wikipedia.org/wiki/Starlink |
| Viasat | viasat.com | Carlsbad, CA | $4.64B FY2026; ~130K US fixed broadband subs | US, global | https://en.wikipedia.org/wiki/Viasat,_Inc. |

**11B. Industry peers**

| Company | Website | Vertical | Key markets | Why similar | Source |
|---|---|---|---|---|---|
| Sky Group | skygroup.sky | Pay-TV + broadband | UK, IE, IT (Sky DE sold to RTL 1-Jun-2026) | Multi-country subscription operator | https://en.wikipedia.org/wiki/Sky_Group |
| DAZN | dazn.com | Sports streaming | 200+ territories; Foxtel (AU) since 2-Apr-2025 | Global recurring billing | https://en.wikipedia.org/wiki/DAZN |
| Canal+ | canalplusgroup.com | Pay-TV + streaming | 50 countries; MultiChoice control 22-Sep-2025 | Multi-market pay-TV | https://en.wikipedia.org/wiki/Canal%2B_S.A. |
| Liberty Latin America | lla.com | Telco + pay-TV | PR, Costa Rica, Panama, Bahamas, 15 Caribbean markets | LatAm telco billing; 10-year Amdocs deal 5-Aug-2026 | https://www.lla.com/our-brands |
| Millicom / Tigo | millicom.com | Telco + pay-TV | 10 countries; buying Telefónica units in CO, UY, EC, CL | Prepaid wireless + pay-TV in LatAm | https://en.wikipedia.org/wiki/Millicom |
| Grupo Televisa (izzi + Sky México) | televisa.com | Pay-TV | Mexico; izzi and Sky México merged Aug-2025 | Satellite + cable pay-TV | https://en.wikipedia.org/wiki/Grupo_Televisa |
| América Movil / Claro | americamovil.com | Telco + pay-TV | ~25 countries | Largest LatAm prepaid base | https://en.wikipedia.org/wiki/Am%C3%A9rica_M%C3%B3vil |
| Vrio (DirecTV Latin America, Sky Brasil, DGO) | vrio.com | Satellite pay-TV + streaming | AR, CL, CO, EC, PE, UY, BR | $450M investment plan to 2031 | https://en.wikipedia.org/wiki/DirecTV_Latin_America |
| Telefónica | telefonica.com | Telco | Spain, Brazil, Germany, UK; exiting six LatAm markets | Divesting peer | https://en.wikipedia.org/wiki/Telef%C3%B3nica |

**11C. Adopting orchestration**

| Company | Orchestrator | Date | Vertical | Source |
|---|---|---|---|---|
| Sky | Spreedly (customer page appears in search; direct fetch redirects to the index, partially verified) | n/a | Pay-TV | https://spreedly.com/customers/sky |
| HBO Max (WBD) | Spreedly (prior internal Yuno research, not re-verified here) | 2026 | Streaming | internal |
| Peacock (NBCU) | Spreedly (prior internal Yuno research, not re-verified here) | 2026 | Streaming | internal |

Primer and Gr4vy customer pages returned 404; no other public orchestration evidence for the companies above.

**11D. Scoring (DISH Network / EchoStar, verified signals only)**

| Signal | Pts | Verified? |
|---|---|---|
| Operates in 3+ countries | +3 | Yes (US, BR, MX, CO, PE, CL, EC, IN via Hughes; Ireland via EchoStar Mobile) |
| Multiple PSPs | +3 | Yes (Recurly, CSG portal, PayU, Webpay, BitPay, Affirm, per-country rails) |
| Recent expansion (24 mo.) | 0 | No: 2026 was divestiture and restructuring; B2B wins only (Air India, NIGCOMSAT) |
| Public payment issues | +2 | Yes (Sling double charges, Boost AutoPay disputes) |
| Funding >$10M | +2 | Yes (public company, $15.0B revenue, $20.25B spectrum proceeds) |
| LATAM/APAC/MENA traffic | +2 | Yes (Hughes regional domains, India) |
| No orchestrator | +2 | Yes (no public evidence) |
| Payment job postings | +1 | Yes (Billing and Credit PMO; Kenan engineer) |
| Public RFP | 0 | None found |
| **Total** | **15** | 🔴 High |

Fit caveat: the score measures the group; the buyer map does not. Chris Ergen does not own billing, two entities are in or just out of Chapter 11, and Hughes consumer is winding down. Treat as 🔴 for the group and 🟡 for the specific meeting until a payments owner is named.

**Top 10 pipeline** (peer scores use only the signals Agent C verified, so they are floor values)

| Rank | Company | Type | Key markets | Score | Priority | Top signal |
|---|---|---|---|---|---|---|
| 1 | DISH Network / EchoStar | Target | US + 7 Hughes countries | 15 | 🔴 | Four stacks, no orchestration, $1B/month recurring |
| 2 | Millicom / Tigo | Peer | 10 LatAm countries | 11 | 🟡 | Buying four Telefónica units, prepaid base |
| 3 | Liberty Latin America | Peer | PR + Caribbean + CA | 11 | 🟡 | Amdocs billing replatform Aug-2026 |
| 4 | DAZN | Peer | 200+ territories | 11 | 🟡 | Foxtel integration, global recurring |
| 5 | Canal+ | Peer | 50 countries | 11 | 🟡 | MultiChoice consolidation |
| 6 | Starlink | Competitor | ~160 countries | 11 | 🟡 | Fastest-growing consumer sat base |
| 7 | Vrio | Peer | 7 LatAm countries | 9 | 🟡 | $450M plan, satellite + OTT |
| 8 | Fubo | Competitor | US, CA, ES | 9 | 🟡 | Disney merger, Hulu Live folded in |
| 9 | América Movil / Claro | Peer | ~25 countries | 9 | 🟡 | Largest prepaid base in LatAm |
| 10 | Grupo Televisa (izzi + Sky México) | Peer | Mexico | 8 | 🟡 | Aug-2025 merger, single market |

Pipeline summary: 17 companies found, 1 high priority (the target), 9 medium. Strongest vertical: multi-country pay-TV and prepaid telco in Latin America (Millicom, LLA, Vrio, Claro, Televisa). Sky is already orchestrated (Spreedly) and would be a displacement play.

---

## SECTION 12: Business Case

| Annual revenue | Avg transaction value | Est. annual transactions | Primary currency | Top 3 markets |
|---|---|---|---|---|
| $15,005.0M FY2025 (Pay-TV $9,700.5M; Wireless $3,795.7M; Broadband & Satellite $1,456.1M). Q2-2026 run-rate $3,576.2M/quarter | Pay-TV ARPU $112.39/month (Q2-2026); Boost ARPU $38.60/month; HughesNet ARPU not disclosed | ~173M recurring consumer payments/year [estimate: (6.39M pay-TV + 7.38M wireless + 0.62M broadband subscribers) × 12], before one-time device, PPV and cash payments | USD | United States; then Brazil and Mexico (Hughes) |

Sources: https://finviz.com/news/326589/echostar-announces-financial-results-for-the-three-and-twelve-months-ended-december-31-2025 ; https://www.sec.gov/Archives/edgar/data/1415404/000110465926021817/tmb-20251231x10k.htm ; https://www.taiwannews.com.tw/en/news/6413699 ; https://www.sec.gov/Archives/edgar/data/1415404/000110465926089370/sats-20260630x10q.htm

Working numbers for the call (all estimates from the figures above): consumer recurring billing ≈ $718M/month pay-TV (6.39M × $112.39) + $285M/month wireless (7.38M × $38.60) ≈ $1.0B/month. FY2025 pay-TV subs 7.00M (5.02M DISH TV, 1.98M Sling); DISH TV churn 1.31% (FY2025) and 1.42% (Q2-2026); DISH TV subscriber acquisition cost $1,529 (Q2-2026). Every 1 point of recovered involuntary churn on the pay-TV base is ~64K households × $112 × remaining lifetime; size it with Finance before quoting.

---

## SECTION 13: Outreach (verified findings only; written as the post-call follow-up for Wed 28-Oct, adapt to what is actually said)

```
--- LINKEDIN MESSAGE (connection note, Chris Ergen) ---
Hi Chris, good to meet you on the call with Juan Pablo today after Marbella. I did the homework on how DISH, Sling, Boost and the HughesNet markets collect money and I think there is a clean story for one payments layer across all of them, without touching the billing systems you already run. Happy to keep the thread going here or by email. German

--- COLD EMAIL (follow-up, to Chris, cc Juan Pablo) ---
Subject: One payments layer across Sling, DISH, Boost and Hughes

Hi Chris,

Thank you for the time today, and good to meet you properly after Marbella.

What stood out from our homework: Sling bills through Recurly with Kount in front, DISH TV collects through a CSG portal with Apple Pay, Google Pay, PayPal, bank account and Bitcoin, Boost runs its own stack with Affirm for devices, and each HughesNet country in Latin America has built its own collection setup, from PSE and Efecty in Colombia to OXXO and SPEI in Mexico and Webpay in Chile. Four brands, at least four payment stacks, no shared layer.

That is the gap Yuno closes. One integration that sits on top of the billing systems you already run, routes every recurring charge to the best acquirer, retries intelligently when a renewal fails, and switches on local methods in a new country in weeks. Livelo lifted approval 5 points and recovered half of its failed charges this way; inDrive went live in ten Latin American markets in under eight months.

If payments sits with someone else on your side, a name is all I need. Otherwise, would 30 minutes next week with whoever runs billing for Boost or Sling make sense?

Best,
German
```

---

## CALL PLAN (28-Oct-2026, 30 minutes, Juan Pablo leads)

**Agenda**
1. Marbella recap and Chris's current remit (5 min).
2. Yuno in two minutes: one layer above Recurly, CSG and Kenan; LatAm roots; who we work with (5 min).
3. Their map: who owns billing and payments per brand; what is on the roadmap for Boost post-AT&T, Hughes LatAm, and the innovation team (10 min).
4. Where a pilot could sit: Sling renewals, Boost web payments, or one HughesNet country (5 min).
5. Next step: a working session with the payments or billing owner (5 min).

**Discovery questions (ask in this order)**
1. Which part of the international and wireless-innovation work do you, Kara, Max and Tyler each own, and what is the next launch on your list?
2. Who owns billing and payment acceptance for Boost, Sling and DISH TV today, and do they talk to each other?
3. After the AT&T close and the DISH DBS emergence on 1-Oct, which legal entity carries Boost Mobile, and which would contract for a payments platform?
4. Is Recurly still the Sling billing system, and what sits behind it as the card gateway?
5. On Boost, why are prepaid cards blocked on the web, and how much volume goes through stores and the $4 assisted channel?
6. What happens to the HughesNet consumer businesses in Brazil, Mexico, Colombia, Peru, Chile and Ecuador now that the US consumer business is winding down? Who runs collections there?
7. DISH has taken Bitcoin since 2014: is there appetite for stablecoin settlement or crypto on Boost and Sling?
8. What would a 90-day pilot need to prove for Charlie's team to care: approval rate, recovered churn, or cost per transaction?

---

## APPENDIX: Source URLs

```
[S1 Traffic] https://www.similarweb.com/website/sling.com/ | https://www.similarweb.com/website/boostmobile.com/ | https://www.similarweb.com/website/dish.com/ | https://www.similarweb.com/website/hughesnet.com/ | https://www.similarweb.com/website/hughesnet.com.br/ | https://www.similarweb.com/website/hughesnet.com.mx/ | https://www.similarweb.com/website/hughesnet.com.co/
[S2 Entities] https://www.sec.gov/Archives/edgar/data/1415404/000110465926021817/tmb-20251231xex21.htm | https://www.sec.gov/Archives/edgar/data/1415404/000110465926021817/tmb-20251231x10k.htm | https://www.sling.com/legal | https://www.hughesnet.com.mx/aviso-de-privacidad | https://www.hughesnet.com.co/ | https://www.hughes.in/ | https://www.echostarmobile.com/privacy-policy/ | https://www.echostarmobile.com/about/regulatory/ | https://legal.hughesnet.com/subscriber-agreement | https://www.sec.gov/Archives/edgar/data/1001082/000155837025007591/dish-20250331x10q.htm
[S3 Stack] https://www.sling.com/etc.clientlibs/sling-television/clientlibs/clientlib-site.min.js | https://www.sling.com/help/en/account-questions/billing-payments/billing-faq | https://www.accel-kkr.com/portfolio-company/recurly/ | https://www.mydish.com | https://my.dish.com/static/js/vendor-1fe33b30.7f154674.js | https://support.dish.com/getting-started/billing-and-payments | https://pymnts.com/?p=532925 | https://www.financemagnates.com/cryptocurrency/news/pay-tv-provider-dish-now-accepts-bitcoin-cash-as-a-payment-option/ | https://jobs.spacetalent.org/companies/dish-network/jobs/47551314-senior-engineer-optima-kenan-development | https://www.echostar.com/gfj/staff-charging-platform-engineer-aurora-co-68bab1ce4b22d2045fb6dd75 | https://www.boostmobile.com/phone-financing-affirm | https://help.boostmobile.com/docs/financing-affirm | https://help.boostmobile.com/docs/account-types | https://help.boostmobile.com/docs/boost-mobile-plan-billing-and-payments | https://www.prnewswire.com/news-releases/boost-mobile-expands-into-financial-services-arena-with-launch-of-omnimoney--no-fee-digital-checking-account-301661282.html | https://www.lightreading.com/5g/wide-launch-of-dishs-boost-infinite-service-slips-to-q1-2023-/d/d-id/781531
[S4 APMs] https://support.dish.com/billing/fees | https://www.sling.com/help/en/account-questions/gift-cards/gift-cards-explained | https://legal.hughesnet.com/SubAgree8.23.22 | https://www.hughesnet.com.br/perguntas-frequentes/ | https://www.hughesnet.com.mx/pagos | https://www.hughesnet.com.co/pagos | https://www.hughesnet.com.pe/pagos | https://hughesnet.cl/pagos | https://www.hughesnet.com.ec/pagos
[S5 Complaints] https://www.trustpilot.com/review/sling.com | https://www.trustpilot.com/review/sling.com?page=2 | https://www.trustpilot.com/review/dish.com | https://www.trustpilot.com/review/boostmobile.com | https://slickdeals.net/f/18132763-boost-mobile-buy-6-months-get-6-months-free-unlimited-plan-300 | https://help.boostmobile.com/docs/general-terms-conditions | https://help.boostmobile.com/docs/30-day-money-back-guarantee-terms
[S6 Corporate] https://en.wikipedia.org/wiki/DirecTV | https://www.sec.gov/Archives/edgar/data/1001082/000141540425000035/tmb-20250825xex99.htm | https://insidetowers.com/?p=64273 | https://www.sec.gov/Archives/edgar/data/1001082/000141540425000041/tmb-20250907xex99d1.htm | https://www.prnewswire.com/news-releases/echostar-agrees-to-sell-full-unpaired-aws-3-spectrum-license-portfolio-to-spacex-302606455.html | https://www.sec.gov/Archives/edgar/data/1415404/000110465926089370/sats-20260630x10q.htm | https://finviz.com/news/326589/echostar-announces-financial-results-for-the-three-and-twelve-months-ended-december-31-2025 | https://www.hughes.com/resources/press-releases | https://capacityglobal.com/news/fcc-approves-40bn-echostar-spectrum-sale/ | https://www.telecompetitor.com/fcc-approves-att-and-starlink-purchases-of-echostar-spectrum/ | https://www.lightreading.com/satellite/hamid-akhavan-exiting-echostar-amid-change-in-strategic-direction- | https://www.lightreading.com/finance/dish-turns-to-chapter-11 | https://www.advanced-television.com/2026/07/01/echostar-confirms-dish-dbs-bankruptcy/ | https://chapter11cases.com/blogs/news/dish-dbs-corporation-a-prepackaged-plan-and-a-363-sale-under-one-roof | https://www.sec.gov/Archives/edgar/data/1415404/000141540426000035/sats-20260728x8k.htm | https://broadbandbreakfast.com/echostar-at-t-close-23-billion-spectrum-sale/ | https://www.sec.gov/Archives/edgar/data/1415404/000141540426000038/sats-20260728xex99.htm | https://www.advanced-television.com/2026/08/03/hughes-network-files-for-bankruptcy/ | https://www.taiwannews.com.tw/en/news/6413699 | https://www.advanced-television.com/2026/08/03/echostar-q2-revenue-falls/ | https://www.sec.gov/Archives/edgar/data/1415404/000141540426000042/sats-20260807xex99d1.htm | https://www.advanced-television.com/2026/08/25/hughes-satellite-bankruptcy-wants-court-examiner/ | https://www.sec.gov/Archives/edgar/data/1415404/000141540426000048/sats-20261001x8k.htm | https://www.advanced-television.com/2026/10/05/echostars-dish-dbs-exits-bankruptcy/ | https://www.builtincolorado.com/job/program-manager-i-billing-and-credit-pmo/10469019 | https://cordcuttersnews.com/dish-sling-tv-had-a-really-bad-2nd-quarter-of-2026/
[S7 News] https://www.boostmobile.com/plans/byod | https://cordcuttersnews.com/sling-tv-is-raising-its-price-this-month/ | https://www.lla.com/our-brands | https://www.nexttv.com/news/echostar-teams-green-dot-302389 | https://benzinga.com/z/25741790
[S8 Checkout] https://www.sling.com | https://www.sling.com/get-started?classification=us&plan=one-month&plan_offer=monthly-web | https://www.boostmobile.com | https://www.boostmobile.com/shop/activation_v2/start/ | https://www.dish.com | https://www.dish.com/packages | https://www.hughesnet.com | https://www.hughesnet.com/get-started | https://www.hughesnet.com/home-satellite-internet-plans
[S11 Pipeline] https://en.wikipedia.org/wiki/YouTube_TV | https://en.wikipedia.org/wiki/Fubo | https://en.wikipedia.org/wiki/Philo_(company) | https://en.wikipedia.org/wiki/Charter_Communications | https://en.wikipedia.org/wiki/Comcast | https://en.wikipedia.org/wiki/Starlink | https://en.wikipedia.org/wiki/Viasat,_Inc. | https://en.wikipedia.org/wiki/Sky_Group | https://en.wikipedia.org/wiki/DAZN | https://en.wikipedia.org/wiki/Canal%2B_S.A. | https://en.wikipedia.org/wiki/Millicom | https://en.wikipedia.org/wiki/Grupo_Televisa | https://en.wikipedia.org/wiki/Am%C3%A9rica_M%C3%B3vil | https://en.wikipedia.org/wiki/Telef%C3%B3nica | https://en.wikipedia.org/wiki/Dish_M%C3%A9xico | https://en.wikipedia.org/wiki/DirecTV_Latin_America | https://spreedly.com/customers/sky | https://spreedly.com/customers
[People] https://www.linkedin.com/in/chris-ergen/ | https://cubastudygroup.org/about-us/members/ | https://people.equilar.com/bio/person/chris-ergen-cuba-study-group/28087800 | https://en.wikipedia.org/wiki/Charlie_Ergen
[Internal] Calendar event "Dish <> Yuno" id 4k1e0kgu8cbs6b3t0322e68err | Gmail thread 1a17e57b049116d2 | Slack #bullhoundsummit-2026 thread 1790183495.434369 | Bullhound Summit 2026 sheet 1YREo8sceRM114H90R9W7xcgOBJ8SGUJGZBOIVNx5BKA, tab "Attendee List Enriched" row 5 | Salesforce account "Dish Network" 001Ps00000wq60oIAA
```
