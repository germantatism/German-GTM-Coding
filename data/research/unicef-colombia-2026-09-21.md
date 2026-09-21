# SDR Research Brief: UNICEF Colombia
**Date:** 2026-09-21 | **Analyst:** Yuno Payments Intelligence | **Framework:** v8.0 (4 agents, accuracy-first)
**Context:** Inbound demo booked via Chili Piper. Call today, Mon 21-sep-2026, 4:00 to 4:30pm COT, Google Meet https://meet.google.com/zre-rmwt-ujn. Organizer Susana Awad; Alejandro Albarracín and German Tatis attending.

---

## TL;DR BATTLE CARD (for the 4pm call)

1. **Who they are:** the UNICEF country office in Colombia (UN agency, NIT 800.176.994-3, Bogotá). It raises money from individual monthly donors acquired face to face, by telemarketing and online. UNICEF received $16.56M from Colombia's private sector fundraising in 2024, rank 7 of 72 country offices and 4th in LatAm [S2].
2. **The live pain, in their own words:** an open tender (RFP2026-10, proposals due 28-sep-2026) asks a call center to "Reactivar el cobro de 90.000 donantes individuales recurrentes" over 3 years, recovering failed donations "mediante la actualización de datos de medio de pago". They measure "Tasa de Cobrabilidad" as a KPI [S6].
3. **Stack (from site code, not from a walked checkout):** custom Drupal 11 form, Firstoken card vault (Firstoken shows a UNICEF Colombia logo), Mercado Pago as the strongest PSP signal, Wompi and Nuvei/SafeCharge allowlisted, Sift for fraud, Evergiving (Waysact) for face-to-face and telemarketing sign-ups, Salesforce as CRM. No orchestrator found [S3].
4. **How they bill:** one automatic run on the first day of each month. Sign-ups from advisors are charged without CVV [S3][S5]. They publish their own cost per transaction: "Una transacción con tarjeta de crédito nos cuesta en promedio $700, mientras que un débito nos cuesta en promedio $1.400" (COP; "débito" is account debit) [S12]. Any per-transaction fee will be measured against that.
5. **The angle:** they do not need another PSP. They need the payment layer to recover failed recurring charges before a call center has to phone the donor: retries, network tokens for reissued cards, routing and failover across the processors they already have, and one view of collection rate by method and channel.
6. **Two questions that open everything:** What is your Tasa de Cobrabilidad on the first-of-month run, by payment method? Which processors are live behind Firstoken today, and who decides where each charge goes?
7. **Watch-outs:** UN procurement (formal RFP or LTA, vendors asked for PCI SAQ D plus AoC), nonprofit price sensitivity on a low average ticket (COP 40,000 to 80,000 monthly), and attendee roles are only partly verified, so open with a roles round.

**Attendees (snippet-level evidence only; LinkedIn and ZoomInfo blocked direct fetch):**

| Attendee | What was found | Confidence | Source |
|---|---|---|---|
| Idual Kerguelen Montaño (ikerguelen@) | LinkedIn headline "Database Officer UNICEF". Systems engineer (Universidad Popular del Cesar), project management studies (Universidad del Rosario), former software QA analyst at Choucair Testing | Strong match (initial, surname, masked i***@unicef.org on ZoomInfo) | https://co.linkedin.com/in/idual-kerguelen-monta%C3%B1o-87561433 |
| Sebastian Garavito Rodriguez (sgaravito@) | A ZoomInfo profile "Sebastian Garavito" lists UNICEF roles Fundraising Associate and Marketing Assistant (donor acquisition campaigns, Scrum Master on Salesforce projects), earlier Acción contra el Hambre (Fundraising Manager, implemented Salesforce for individual donors) and Aldeas Infantiles SOS Colombia (up to Coordinador de Recaudo) | Identity NOT confirmed: ZoomInfo shows UNICEF as a past employer and the snippet name varied | https://www.zoominfo.com/p/Sebastian-Garavito/9010517330 |
| Leidy Guio Castellanos (lguio@) | Not found. Two unrelated people with similar names exist; do not assume a role | None | N/A |

Likely reporting line [INFERENCE, not confirmed]: Gustavo Ugalde, "Gerente de Movilización de Recursos de UNICEF Colombia" per UNICEF's own press release of 31-Mar-2026 (LinkedIn headline "Chief of Fundraising, UNICEF Colombia") [S6]. The Representative named in that release is Tanya Chapuisat (not reconfirmed as of Sep 2026). Vacancies show an "Individual Giving Officer" and an "Individual Specialist" who supervises the Database Officer; no names are published [S6]. Read of the room [INFERENCE, not confirmed]: this is the individual giving operations side. Idual would be the technical evaluator (donor database, CRM data flows, recurring charge files). If the Sebastian match holds, his collections and loyalty background makes him the person closest to declined recurring charges. No payments or fintech background was found for any of the three.

---

## EXECUTIVE SUMMARY

UNICEF Colombia is the UNICEF country office in Bogotá, a UN agency office (not a local foundation) that has run a monthly donor program "Desde 2001" and sits among UNICEF's top private fundraising country offices: $16.56M in contributions received in 2024, rank 7 of 72 [S2][S6]. Its online donation form is a custom Drupal 11 build on Acquia whose security policy allowlists a card vault (Firstoken, which displays a UNICEF Colombia client logo and claims tokens usable "across over 200 processors"), Mercado Pago (the site carries a bespoke patch so mercadopago.js can run), Wompi, Nuvei/SafeCharge, Sift and Google Pay; face-to-face and telemarketing sign-ups run on Evergiving (Waysact), and Salesforce is the CRM. No orchestrator was found, and which processors are live and how volume is split was not observable [S3]. The strongest finding is a pair of open tenders closing 28-sep-2026: the telemarketing one asks the vendor to reactivate collection for 90,000 recurring donors over three years by phoning them to update payment details, and tracks "Tasa de Cobrabilidad" as a KPI, while the refund policy shows all monthly charges run once, on the first day of the month [S5][S6]. The Yuno opportunity is to sit above the processors they already use and recover failed recurring charges in the payment layer (retries, network tokens, routing and failover, unified collection reporting across cards, Nequi, Daviplata, PSE and account debit), at a moment when UNICEF globally projects "at least a 20 per cent decline in income from 2026" and every point of collection rate is money for programs [S7].

---

## SECTION 1: Traffic by Country

UNICEF Colombia fundraises on its own domain. Free Semrush and Similarweb views expose only the top 3 to 5 countries; ranks below that are paywalled.

**1A. unicef.org.co (Colombia fundraising site), Semrush, August 2026**

| Rank | Country | Traffic Share (%) | Est. Monthly Visits | Trend | Source URL |
|------|---------|-------------------|---------------------|-------|------------|
| 1 | Colombia | 88.83% | ~107.3K [ESTIMATE: share x 120.84K site total] | Site +68.44% vs July 2026 | https://www.semrush.com/website/unicef.org.co/overview/ |
| 2 | Mexico | 5.51% | ~6.7K [ESTIMATE] | Not shown per country | https://www.semrush.com/website/unicef.org.co/overview/ |
| 3 | United States | 3.81% | ~4.6K [ESTIMATE] | Not shown per country | https://www.semrush.com/website/unicef.org.co/overview/ |
| 4 to 10 | Not visible without login | N/A | N/A | N/A | N/A |

Site-level: 120.84K visits, global rank 272,472, Colombia rank 4,290, bounce rate 92.95%, top desktop sources Google paid search 26.36% and direct 24.23% [https://www.semrush.com/website/unicef.org.co/overview/].

**1B. unicef.org (global institutional site), August 2026**

| Rank | Country (Similarweb) | Share | Country (Semrush) | Share | Source URLs |
|------|----------------------|-------|-------------------|-------|-------------|
| 1 | United States | 8.91% | India | 19.43% | https://www.similarweb.com/website/unicef.org/ and https://www.semrush.com/website/unicef.org/overview/ |
| 2 | India | 6.13% | United States | 10.22% | same |
| 3 | Mexico | 5.89% | Brazil | 7.33% | same |
| 4 | Brazil | 5.00% | Mexico | 6.64% | same |
| 5 | France | 4.80% | Bangladesh | 6.40% | same |

Similarweb: 3.8M visits (down 1.56% MoM). Semrush: 4.35M visits (down 3.37% MoM). The two tools disagree on the top country. Top 10 not obtainable on free views.

**1C. National Committee domains (Similarweb, August 2026, top countries only)**

| Domain | Global rank | MoM | Top countries | Source URL |
|---|---|---|---|---|
| unicefusa.org | #116,091 | -21.57% | US 70.23%, UK 1.59%, PH 1.25% | https://www.similarweb.com/website/unicefusa.org/ |
| unicef.org.uk | #258,737 | -3.61% | UK 51.35%, US 6.04%, BR 3.66% | https://www.similarweb.com/website/unicef.org.uk/ |
| unicef.es | #289,600 | -18.06% | ES 27.11%, MX 14.57%, CO 6.54%, AR 5.29%, GT 5.22% | https://www.similarweb.com/website/unicef.es/ |
| unicef.de | #213,614 | +16.08% | DE 83.64%, AT 6.46%, CH 3.89% | https://www.similarweb.com/website/unicef.de/ |
| unicef.fr | #273,802 | -10.97% | FR 81.08%, BE 3.31%, US 2.43% | https://www.similarweb.com/website/unicef.fr/ |
| unicef.it | #261,866 | +11.73% | IT 87.22%, US 4.99%, UK 2.66% | https://www.similarweb.com/website/unicef.it/ |
| unicef.or.jp | #114,048 | -7.19% | JP 96.55%, US 1.31% | https://www.similarweb.com/website/unicef.or.jp/ |
| unicef.or.kr | #100,071 | +6.25% | KR 95.21%, US 3.14% | https://www.similarweb.com/website/unicef.or.kr/ |

Visit counts for the committee domains are omitted: the extraction labelled some as monthly and some as "last 3 months", so they are not safe to quote.

**Flags:**
- Markets above 5% on the Colombia site: Colombia, Mexico.
- The Colombia operation is a single-market, LATAM operation: 88.83% domestic traffic.
- Colombia is 6.54% of unicef.es traffic, so some Colombian visitors land on the Spanish committee's site [https://www.similarweb.com/website/unicef.es/].
- Other UNICEF Colombia hosts seen in site code and FAQ: donaciones.unicef.org.co (same form), legadosolidario.unicef.org.co (legacy giving), uniceferestu.com (donor portal), collect.unicef.org.co, donanteunicef.com, agenciasunicef.com, donaparalainfancia.com [https://donaciones.unicef.org.co/preguntas-frecuentes].
- The form may be embedded by tuboleta.com, caracoltv.com and donaparalainfancia.com (CSP frame-ancestors), which points to TV and ticketing partner channels [https://donaciones.unicef.org.co/donar].

---

## SECTION 2: Legal Entities

| Country | In Top 10 Traffic? | Has Local Entity? | Cross-Border Risk? | Source URL |
|---|---|---|---|---|
| Colombia | Yes (#1, 88.83%) | Yes. "UNICEF Oficina para Colombia", NIT 800.176.994-3, Calle 72 #10-71 piso 11, Bogotá. UN agency country office; acts as data controller for donor data | No | https://donaciones.unicef.org.co/aviso-privacidad |
| Mexico | Yes (#2, 5.51% of the Colombia site) | UNICEF Mexico is a separate country office with its own fundraising (2024 contributions received $18.2M) | Low. Visitors, not a Colombian operation | https://www.unicef.org/media/173291/file/UNICEF_FundingCompendium2024.pdf |
| United States | Yes (#3, 3.81% of the Colombia site) | UNICEF USA is an independent National Committee | Low | https://www.unicef.org/unicef-national-committees |

- UN status: the data policy preserves "las prerrogativas e inmunidades de las Naciones Unidas", cites Ley 1581 de 2012 and was approved by the UNICEF Representative for Colombia on 06-Jun-2018 [https://donaciones.unicef.org.co/politica-proteccion-datos-personales].
- The privacy notice says donor financial information may be shared with third parties "prestando servicios de procesamiento de pagos ... call center, servicios de tecnología", including outside Colombia. No processor is named in any legal text [https://donaciones.unicef.org.co/aviso-privacidad].
- No separate Colombian foundation or fundraising vehicle is referenced anywhere; only the country office NIT appears. A Basic Cooperation Agreement with the Colombian government: No public information found.
- Global structure: 32 National Committees, "each established as an independent local non-governmental organization", raise about one third of UNICEF income from more than 6 million individual donors [https://www.unicef.org/unicef-national-committees]. Country offices with structured private sector fundraising (Colombia among them) raise the rest of private income.
- Small cross-border note [INFERENCE, not confirmed]: the form hides Nequi and Daviplata when the donor's phone country is not Colombia, so donors abroad would give by card in COP through the Colombian setup.

> ⚠️ MANUAL: Verify on official T&Cs.

---

## SECTION 3: Payment Stack

Evidence comes from the donation pages' HTML, scripts and Content-Security-Policy (CSP) response header. A CSP allowlist shows which vendors are allowed to load; it does not prove they process live volume. The payment step (step 3 of the form) was not walked, so the processing PSP was not observed at checkout level.

**3A. PSPs, acquirers and payment vendors**

| Country/Region | PSP / Vendor | Evidence Type | Source URL |
|---|---|---|---|
| Colombia (web) | Firstoken (card tokenization and PCI vault). CSP allows its capture SDK (cdn.firstoken.co/captures/js/2.1/sdk.js), frames captures.firstoken.co, and CSP violation reports go to monitor.firstoken.co | [Source Code] | https://donaciones.unicef.org.co/donar |
| Colombia (web) | Firstoken homepage shows a client logo file named unicef_colombia.svg; claims PCI DSS Level 1 vault and tokens usable "across over 200 processors worldwide" | [Vendor Case Study] | https://firstoken.co/ |
| Colombia (web) | Mercado Pago. An inline script attaches the CSP nonce to scripts injected by mercadopago.js (the only loader handled besides gtm.js); CSP allows secure.mlstatic.com, http2.mlstatic.com and frames *.mercadolibre.com. Strongest PSP signal | [Source Code] | https://donaciones.unicef.org.co/donar |
| Colombia (web) | Wompi (Bancolombia): wompijs.wompi.com/libs/js/v1.js, checkout.wompi.co/widget.js, frames *.wompi.co. CSP only | [Source Code] | https://donaciones.unicef.org.co/donar |
| Colombia (web) | Nuvei / SafeCharge: cdn.safecharge.com in script and frame sources. CSP only; the theme is shared across UNICEF country sites, so this entry may belong to another country [INFERENCE, not confirmed] | [Source Code] | https://donaciones.unicef.org.co/donar |
| Colombia (web) | Sift (fraud): cdn.siftscience.com/s.js. CSP only | [Source Code] | https://donaciones.unicef.org.co/donar |
| Colombia (web) | Google Pay JS (pay.google.com/gp/p/js/pay.js) allowlisted; an HTML comment "google pay logo" has no rendered logo. Not verified as offered | [Source Code] | https://donaciones.unicef.org.co/donar |
| Colombia (back office) | Form may POST to uni-pfp-pci-co.azurewebsites.net/ComprobanteDonacion, a separate Azure ASP.NET app behind a login | [Source Code] | https://donaciones.unicef.org.co/donar |
| Colombia (face to face, telemarketing) | Evergiving, operated by Waysact: "la plataforma que utilizan los asesores autorizados de UNICEF Colombia para registrar donaciones" | [Checkout / FAQ] | https://donaciones.unicef.org.co/preguntas-frecuentes |
| Colombia (face to face, telemarketing) | Evergiving's public gateway list includes Mercado Pago, Stripe, CyberSource, Braintree, Openpay, Worldpay and others. Which one UNICEF Colombia uses there: Not found | [Vendor page] | https://www.evergiving.com/payment-gateways |
| Colombia (CRM) | Salesforce. The tender requires vendor integration "particularmente con Salesforce", plus "Aliados CPTP, Plataformas de Cobranza, Proveedor IVR" (none named) | [Procurement/Tender] | https://www.unicef.org/colombia/convocatorias-para-empresas |
| Germany (UNICEF Deutschland) | FundraisingBox donation platform; payment type enum PAYPAL_CHECKOUT, FB_STRIPE_CREDIT_CARD, UNICEF_DIRECT_DEBIT, which indicates Stripe card processing through FundraisingBox plus PayPal and direct debit | [Source Code] | https://www.unicef.de/spenden/jetzt-spenden |
| Australia (UNICEF Australia) | Stripe: page config keys stripeExpressOverride and stripeRequiredDetails, express checkout "enabled___production_mode"; FormAssembly form processor (unicefaustralia.tfaforms.net) | [Source Code] | https://www.unicef.org.au/donate/donate-once |
| Canada (UNICEF Canada) | Donate link redirects to secure.unicef.ca/page/31858/donate/1?ea.tracking.id=..., a URL pattern characteristic of Engaging Networks [INFERENCE from URL only; page returned 403] | [Redirect URL] | https://www.unicef.ca/donatenow |
| France (UNICEF France) | Standalone donation app at don.unicef.fr; config key "formerIRaiser": false; method labels include PayPal, Apple Pay, Google Pay, Bancontact, SEPA | [Source Code] | https://don.unicef.fr/ |
| South Korea | Page component named inicis-account-check (weak signal toward KG Inicis) | [Source Code] | https://www.unicef.or.kr/donate/ |
| UK | WordPress hub whose form sends donors to donate.unicef.org.uk (that host returned 403, PSP NOT VERIFIED); Salesforce Embedded Messaging on the hub (chat, not a payment signal) | [Source Code] | https://www.unicef.org.uk/donate/ |
| Italy, India | No PSP strings in the static HTML (forms render client-side or after a submit). PSP NOT VERIFIED | [Source Code] | https://donazioni.unicef.it/ and https://india.unicef.org/donate |
| USA, Spain, global help.unicef.org (which also hosts the Mexico, Brazil, Argentina and Peru donation pages) | NOT VERIFIED: Cloudflare 403 to non-browser requests | N/A | N/A |

Platform: Drupal 11 on Acquia, custom theme unicef_psfr, custom modules unicef_pci, unicef_form and unicef_datalayers, Drupal Webform wizard donaciones_hibrido_drtv. No off-the-shelf fundraising platform script (iRaiser, Fundraise Up, Classy, Blackbaud, Engaging Networks) was found on the Colombia pages. No PayU, PlacetoPay, ePayco, Stripe, Adyen, CyberSource, Kushki, dLocal or EBANX domains appear in the Colombia CSP or HTML [https://donaciones.unicef.org.co/donar].

Read of the architecture [INFERENCE, not confirmed]: a third-party vault (Firstoken) in front of more than one processor, which would make tokens portable across PSPs. Mercado Pago is the most likely active online card processor given the bespoke patch. Nequi and Daviplata recurring charges may run through Wompi or direct integrations. Each UNICEF market inspected runs a different stack, consistent with every office and committee choosing its own.

**3B. Orchestrator:** No public evidence found for UNICEF Colombia, UNICEF global or any National Committee (searched Spreedly, Primer, Gr4vy, CellPoint, APEXX). Note that Firstoken markets proxy and multi-processor token capabilities, so part of an orchestration function may already sit there; whether it does any routing for UNICEF is unknown.

Yuno fit check (Yuno public pages): Wompi, Nuvei and Nequi are listed Yuno partners, and Yuno docs list PSE, Daviplata and Mercado Pago among supported methods [https://www.y.uno/partner/wompi] [https://y.uno/partner/nuvei] [https://y.uno/partner/nequi] [https://docs.y.uno/docs/payment-features/enrollment/enroll-payment-methods]. Whether Yuno can consume Firstoken tokens or would need a vault migration is an open question for Solutions Engineering.

> ⚠️ MANUAL (DevTools): the form's first step captures personal data into UNICEF's CRM and call queue, so do not submit fake data. Ask the attendees which processors are live, or have them share a test environment. Test card for sandboxes only: 4111 1111 1111 1111 | 02/30 | 123

---

## SECTION 4: APMs

**4A. Confirmed APMs**

| Market | APMs Confirmed | Verification Source | Source URL |
|---|---|---|---|
| Colombia, monthly donation | "tarjeta de crédito, cuenta de Nequi o tu cuenta de ahorros o corriente" | On-page FAQ | https://donaciones.unicef.org.co/donar |
| Colombia, one-time donation | The three above plus "billeteras virtuales a través de PSE" | On-page FAQ | https://unicef.org.co/donar-mensual |
| Colombia, form footer logos | Visa, Mastercard, Amex, Bancolombia, PSE, Nequi, Daviplata | Page HTML | https://donaciones.unicef.org.co/donar |
| Colombia, form logic | medio_de_pago values nequi and daviplata, hidden when the phone country is not Colombia; hidden fields phone_nequi and phone_daviplata | Form JavaScript | https://donaciones.unicef.org.co/webform/javascript/donaciones_hibrido_drtv/custom.js |
| Colombia, home page copy | Also names debit card and Daviplata | Page copy | https://donaciones.unicef.org.co/ |
| Colombia, new donors via agencies (tender) | "tarjeta de crédito, cuenta corriente, cuenta de ahorros, billeteras virtuales o facturas de servicios públicos o privados", minimum COP 40,000 monthly | Tender ToR (RFP2026-10) | https://www.unicef.org/colombia/convocatorias-para-empresas |
| Colombia, offline | Bancolombia current account for deposits; "vueltas" donations at retail; payroll deduction and "redondeo en cajas" for corporate partners | Official pages | https://www.unicef.org/colombia/como-vincularse and https://donaciones.unicef.org.co/alianzas-corporativas |
| Colombia, other sign-up channels | WhatsApp +57 323 232 7944, phone 601 390 4705 and 01 8000 919866, donor portal uniceferestu.com. FAQ: no one linked to the campaign may request or receive cash. Form code also carries a bimonthly donation flag (isBimestral) | Official FAQ and form JavaScript | https://unicef.org.co/preguntas-frecuentes |
| UK | One-off: Visa, Mastercard, Amex, PayPal. Monthly: Direct Debit. FAQ adds cheque, bank transfer, CAF, phone and text giving | Hub logos and donations FAQ | https://www.unicef.org.uk/donate/ and https://www.unicef.org.uk/why-donate-to-unicef/donations-faq/ |
| Germany | Direct debit (Lastschrift), credit card, PayPal ("per Bankeinzug, Kreditkarte oder Paypal") | Page HTML and form schema | https://www.unicef.de/spenden/jetzt-spenden |
| Australia | Visa, Mastercard, PayPal, Apple Pay, Google Pay, Link wallet (logos) | Page HTML | https://www.unicef.org.au/donate/donate-once |
| Italy | "dona online con paypal e carta di credito" (meta description only) | Page meta | https://donazioni.unicef.it/ |
| France | Labels for PayPal, Apple Pay, Google Pay, Bancontact, Payconiq, Giropay, EPS, Swish, bank transfer, SEPA exist in the app's dictionary (labels, not proof each is enabled) | App config | https://don.unicef.fr/ |

**4B. Unverified Markets**

| Market | Verification Attempted? | Reason Not Verified | Popular Local APMs |
|---|---|---|---|
| Colombia, payment step (step 3) | Yes | Steps 2 and 3 load only after submitting personal data; not submitted | Cards, PSE, Nequi, Daviplata, Bancolombia button, account debit |
| USA (unicefusa.org) | Yes | Cloudflare 403 to non-browser requests | Cards, PayPal, Apple Pay, Google Pay, ACH, Venmo |
| Spain (unicef.es) | Yes | Cloudflare 403 | Cards, SEPA debit, Bizum, PayPal |
| Global, Mexico, Brazil, Argentina, Peru (all on help.unicef.org) | Yes | Cloudflare 403 on the shared host | Mexico: cards, SPEI, OXXO. Brazil: Pix, boleto, cards. Argentina: cards, Mercado Pago, account debit. Peru: cards, Yape, PagoEfectivo |
| UK form host (donate.unicef.org.uk) | Yes | Cloudflare 403; only the hub and FAQ were verified | Cards, Direct Debit, PayPal, Apple Pay, Google Pay |
| Canada (secure.unicef.ca) | Yes | 403; only the redirect URL was observed | Cards, PayPal, Interac, pre-authorized debit |
| India (india.unicef.org) | Yes | Only the amount step is visible (monthly ₹800 / 1000 / 1500); payment step needs a form submit | UPI, cards, netbanking, wallets |
| Japan | Yes | No PSP or method signal on the first page | Cards, konbini, bank transfer |
| France (unicef.fr homepage), Netherlands | Yes | 403 on the homepage (the don.unicef.fr app was readable, see 4A) | France: cards, SEPA, PayPal. Netherlands: iDEAL, SEPA |

> "Not verified" ≠ "not available." MANUAL: VPN checkout walk-through before any APM claims.

---

## SECTION 5: Payment Complaints

| Issue Type | Platform | Frequency | Date Range | Source URL |
|---|---|---|---|---|
| Unauthorized donation; one-time gift understood as monthly; debit after cancellation; debited more than once in a month | UNICEF Colombia's own refund policy (self-disclosed scenarios, not third-party complaints) | Listed as the reasons donors request refunds; no counts published | Current policy | https://donaciones.unicef.org.co/politica-de-reintegros |
| Refund friction: capped at 3 months of the monthly amount, written request by email, only to the original account or card, 2 to 5 weeks | UNICEF Colombia refund policy | Structural | Current policy | https://donaciones.unicef.org.co/politica-de-reintegros |
| Cancellation lag: charges run on day 1; a debit in the month of cancellation is not refundable | UNICEF Colombia refund policy | Structural | Current policy | https://donaciones.unicef.org.co/politica-de-reintegros |
| Cancellation not self-service: phone (601 3904705, 01 8000 919 866) or email only, although a donor hub exists for payment method updates | UNICEF Colombia donor hub | Structural | Current | https://donaciones.unicef.org.co/donantes-hub/contacto |
| Failed recurring charges recovered by outbound calls | UNICEF Colombia tender RFP2026-10 | Target: reactivate collection for 90,000 recurring donors over 3 years (a target, not a measured decline rate) | 2026 to 2029 | https://www.unicef.org/colombia/convocatorias-para-empresas |
| One-time gift turned monthly; no online cancel | Trustpilot, UNICEF UK (not Colombia) | About 2 of 25 reviews; TrustScore 1.8 | Mar 2024 to Nov 2024 | https://www.trustpilot.com/review/www.unicef.org.uk |
| Charge without consent | Trustpilot, UNICEF España (not Colombia) | 1 to 2 of 22 reviews; TrustScore 2.4; dominant theme is unsolicited calls | Oct 2021 to Jul 2026 | https://www.trustpilot.com/review/unicef.es |
| Card declines, double charges, checkout errors (third-party complaints) | Reddit, Trustpilot, SIC, X, Facebook, Google reviews | No public information found for UNICEF Colombia | N/A | N/A |

**Analysis:** there is no public complaint trail for UNICEF Colombia (the search tool indexes X and Facebook poorly, so absence is weak evidence). The pain is documented by UNICEF itself. A single first-of-month billing run plus phone-only cancellation produces the refund scenarios the policy lists, and failed charges are recovered by call center. Yuno maps to this as follows: recovery of failed recurring charges in the payment layer before a call is needed (Yuno publishes 30% recovered revenue), smart routing across the processors already allowlisted (Yuno publishes a 7% approval uplift), and real-time monitors so a processor or bank outage on the first of the month is caught in minutes instead of after the run.

---

## SECTION 6: Expansion & Corporate Developments

| # | Date | Development | Category | Source URL |
|---|------|-------------|----------|------------|
| 1 | Open, proposals due 28-sep-2026 | RFP2026-10 "Recaudación de Fondos" (telemarketing and digital channels), 3-year LTA: activate 28,500 new recurring donors (9,500 per year), reactivate collection for 90,000 recurring donors, welcome and loyalty campaigns for "alrededor de 180.000 donantes individuales" with 85% contactability and 62% effectiveness on contact | Public RFP, payments-adjacent | https://www.unicef.org/colombia/convocatorias-para-empresas |
| 2 | Open, proposals due 28-sep-2026 | RFP2026-11 "Face to Face", 36 months: "Activar 20.000 nuevos donantes individuales recurrentes", minimum COP 40,000 monthly, under a fundraising strategy for "2024 a 2027" | Public RFP, acquisition | https://www.unicef.org/colombia/convocatorias-para-empresas |
| 3 | 17-Apr-2026 | First UNICEF Colombia benefit gala (Country Club de Bogotá) for children affected by the winter emergency in Córdoba. UNICEF's release does not publish the amount; the Portafolio headline reports more than COP 560M (article not opened) | New channel | https://www.unicef.org/colombia/comunicados-prensa/unicef-celebrar%C3%A1-en-colombia-su-primera-gala-ben%C3%A9fica-para-apoyar-la-ni%C3%B1ez-y and https://www.portafolio.co/economia/gobierno/unicef-colombia-recaudo-mas-de-560-millones-de-pesos-en-su-primera-gala-para-la-educacion-de-ninos-en-cordoba-492914 |
| 4 | 2026 | Vacancy: Fund Raising Assistant (Donor Retention), GS5, Bogotá, Post 136577. KPIs "donor attrition, conversion rates, gross revenue"; tools "Salesforce, HubSpot, Marketing Cloud"; works with telemarketing agencies; channels "face-to-face, digital and TV" | Hiring | https://unjoblink.org/job/details/416493/ |
| 4b | 2026 | Vacancy: Fund Raising Associate (CRM Implementation), GS7, Post 136578 (listing expired; mirror now 404). A search snippet attributed to this ad says "over 130,000 active donors and an average monthly collection of USD 1.5 million", four years after implementing Salesforce. UNVERIFIED: original not readable | Hiring | https://jobs.unicef.org/en-us/job/561454 |
| 4c | 2023 | Vacancy: Salesforce CRM Implementation Associate, Post 124210: "Coordination of API integration of agencies to the new CRM", "Support in optimizing CRM collection processes" | Hiring (older than 24 months, context) | https://untalent.org/jobs/salesforce-crm-implementation-associate-gs7-ta-12-months-bogota-colombia |
| 4d | 06-Aug-2024 | Prior tender RFQ2024-26 "Agencias Recaudación Fondos F2F" on UNGM, deadline 25-Aug-2024 | Public RFP, acquisition | https://www.ungm.org/Public/Notice/242854 |
| 5 | Current | Legacy giving site legadosolidario.unicef.org.co and donor self-service hub (login with cédula, payment method update, amount increase, certificates) | Product | https://donaciones.unicef.org.co/donantes-hub/contacto |
| 6 | 8-aug-2025, updated 19-nov-2025 | UNICEF global restructuring: "at least a 20 per cent decline in income from 2026", "relocation of 70 per cent of staff to lower-cost locations", savings of "around $586 million in core resources" | Global restructuring | https://www.unicef.org/media/current-issues/information-note-ongoing-restructuring-initiatives |
| 7 | Feb 2026 | UNICEF private fundraising division (PFP) 2026 workplan: private sector target $1.96B; PFP budget $230M proposed vs $287M approved for 2025; investment funds cut by $20M, country office expenditure cut by $15M; 80 posts reduced; "Relocation of over 90% of staff from GVA to Rome"; model "decentralized, distributed, diversified" | Global restructuring | https://www.unicef.org/executiveboard/media/35901/file/2026-FRS-Item-13-PFP-Workplan-Budget-Carla-Haddad-Mardini-PPT-EN-2026-02-04.pdf |
| 8 | 2022 to 2023 | Accenture rolled out Salesforce for UNICEF country offices in Thailand, Malaysia, Indonesia and the Philippines (1 million supporters migrated), including "payment billing connected to local banks" and "donations processing" | Peer offices, CRM plus payments | https://www.accenture.com/us-en/case-studies/public-service/unicef-revamps-fundraising-future |

Both tender ToRs note a neighbouring block on the page showing 27-sep-2026; the process schedule in both says 28-sep. Verify before citing a date. Tender contact: col-corporateproposals@unicef.org.

Leadership: Representative Tanya Chapuisat and Gerente de Movilización de Recursos Gustavo Ugalde (UNICEF release, 31-Mar-2026); Mario Valderrama, Private Fundraising and Partnerships Officer, on the corporate alliances side [https://donaciones.unicef.org.co/alianzas-corporativas]. Head of individual giving, donor care, finance or ICT leads: No public information found. No tender for a payment gateway, donation platform or CRM was found on the UNICEF Colombia page or UNGM.

---

## SECTION 7: Payment News

| # | Date | Headline | Relevance | Source URL |
|---|------|----------|-----------|------------|
| 1 | Sep 2026 | 🟢 UNICEF Colombia tenders telemarketing and face-to-face fundraising for 3 years, including "recuperación de recaudo (cobranza)" | Collection recovery is budgeted and being bought now, as a call center service | https://www.unicef.org/colombia/convocatorias-para-empresas |
| 2 | 2025 to 2026 | 🔴 UNICEF projects "at least a 20 per cent decline in income from 2026" | Raises the weight of individual monthly giving and of collection rate [INFERENCE, not confirmed] | https://www.unicef.org/media/current-issues/information-note-ongoing-restructuring-initiatives |
| 3 | 2025 | UNICEF 2025 income $8,084M (2024: $8,263M); private sector $2.215B, up 19.7% vs 2024 and helped by the largest private donation in UNICEF history (up to $500M); country offices raised $379.3M (17%) and National Committees $1,836M (83%); "90% of private sector RR came from individual supporters"; "10 million+ individual supporters" | Individual monthly giving is the core of flexible funding | https://www.unicef.org/executiveboard/media/39341/file/2026-AS-Item-16-PFP-financial-report-Carla-Haddad-Mardini-PPT-EN-2026-06-17.pdf |
| 3b | Feb 2026 | 2026 private sector plan $1,957M, below the 2025 result, with the fundraising division's budget cut from $287M to $230M and country office expenditure cut by $15M | Country offices asked to raise with less central investment [INFERENCE, not confirmed for Colombia] | https://www.unicef.org/executiveboard/media/35901/file/2026-FRS-Item-13-PFP-Workplan-Budget-Carla-Haddad-Mardini-PPT-EN-2026-02-04.pdf |
| 4 | 2024 | Private sector income $1,847M, 22% of total, down 11% ($221M) vs 2023 | Private income volatile year to year (2022 $2,669M, 2023 $2,073M, 2024 $1,847M, 2025 $2,215M) | https://www.unicef.org/media/173291/file/UNICEF_FundingCompendium2024.pdf |
| 4b | 11-Apr-2024 | 🟢 Adyen and UNICEF global partnership through Adyen Giving (donations at merchants' checkout). It does not state that Adyen processes UNICEF's own donation forms | Adyen has a relationship at global level; not a processing signal for Colombia | https://www.adyen.com/press-and-media/adyen-and-unicef-launch-partnership |
| 4c | Undated | UNICEF USA (independent National Committee) uses Fundraise Up, which runs on Stripe | Confirms each entity picks its own stack | https://fundraiseup.com/case-studies/unicef-usa/ |
| 5 | May 2026 | 🟢 Bitget and UNICEF (via UNICEF Luxembourg) youth AI and financial literacy partnership | Programme partnership, not a donation payment rail | https://www.disruptionbanking.com/2026/05/21/bitget-and-unicef-partner-to-boost-ai-and-financial-literacy-among-youth-in-8-countries/ |
| 6 | 27-Jun-2022 | UNICEF Panama LTA "GESTIÓN DE RETENCION DE DONANTES INDIVIDUALES": outbound calls to donors "rejected by the payment processor due to a change in credit card number or expiration date"; vendor must provide a PCI DSS AoC | Same pattern regionally: involuntary churn handled by call center | https://www.ungm.org/Public/Notice/177105 |
| 7 | 27-Nov-2017 (context only) | Banco de Bogotá alliance: cardholders donate COP 30,000 monthly | Historic bank channel | https://www.unicef.org/colombia/comunicados-prensa/banco-de-bogota-y-unicef-firman-alianza |

No 2025 to 2026 partnership announcement with Nequi, Daviplata, Bancolombia or PSE was found (they appear only as accepted methods), no named round-up retail partner, and no PSP or payment vendor termination for any UNICEF entity.

---

## SECTION 8: Checkout Audit

Only step 1 was observed (server-rendered HTML and response headers). Steps 2 and 3 require submitting personal data and were not walked.

| Dimension | Finding | Quality | Notes |
|---|---|---|---|
| Checkout type | Embedded Drupal webform wizard on UNICEF's own domain (form id donaciones_hibrido_drtv), no iframe at step 1; card capture likely via Firstoken hosted fields [INFERENCE, not confirmed] | Good | Same widget on /donar, /donar-mensual, /futbol and campaign pages |
| Guest checkout | Yes. No account or login at step 1; CTA "Donar ahora". A separate donor hub uses cédula plus password | Good | https://donaciones.unicef.org.co/donar |
| Steps to purchase | 3: "Selecciona tu donación", "Ingresa tus datos personales", "Completa tu pago". Monthly preselected; monthly COP 50,000 / 80,000 (80,000 default), one-time COP 100,000 / 200,000 | Good | A click-to-call alternative ("Llámenme") sits on the same page |
| 3DS | Not observed | Unknown | FAQ: web form may ask CVV; advisors "nunca te solicitarán el código de seguridad (CVV)", so advisor sign-ups are charged without CVV |
| Mobile experience | Not tested (no browser rendering). Responsive theme and intl-tel-input present | Unknown | 92.95% bounce rate on the site per Semrush |
| APM display logic | Nequi and Daviplata hidden when the phone country is not Colombia; PSE wallets only for one-time gifts | Good | FAQ tells donors whose bank is not listed to use the credit card option with a debit card and enter "el código de seguridad (PIN) que sale al respaldo", which conflates CVV and PIN |

Tooling on the page: Optimizely, New Relic, Hotjar, Microsoft Clarity, reCAPTCHA, GTM, Meta, TikTok, LinkedIn, Bing and Pinterest pixels [https://donaciones.unicef.org.co/donar].

> ⚠️ MANUAL: Walk the Colombia checkout in a real browser (stop before paying); this is a single-market operation.

---

## SECTION 9: PCI DSS

| PCI DSS Level | Card data handling | Recommended Yuno integration | Source |
|---|---|---|---|
| Not published. Footer badge "Certificado PCI DSS" on every donation page; no certificate, QSA, level or date | Card capture set up for hosted fields or iframe via Firstoken (captures.firstoken.co allowlisted); custom Drupal module unicef_pci posts CSP violation reports to monitor.firstoken.co; separate Azure app uni-pfp-pci-co for receipts; Evergiving described as "PCI Compliance" for advisor sign-ups | Keep UNICEF out of PCI scope: Yuno SDK with hosted card fields on the web form, or API integration behind the existing vault if Firstoken stays. Decision depends on the Firstoken question in Section 3B | https://donaciones.unicef.org.co/donar and https://donaciones.unicef.org.co/preguntas-frecuentes |

Procurement signal: UNICEF Colombia asks fundraising vendors to complete SAQ D plus an Attestation of Compliance for service providers (RFP2026-10), and the 2022 Panama LTA required a PCI DSS AoC. Expect the same request of any payment vendor; have Yuno's AoC ready [https://www.unicef.org/colombia/convocatorias-para-empresas] [https://www.ungm.org/Public/Notice/177105].

---

## SECTION 10: Strategic Insights

**Insight #1: Collection recovery is being bought as a call center service**
Evidence: S6, RFP2026-10: "Reactivar el cobro de 90.000 donantes individuales recurrentes", recovery "mediante la actualización de datos de medio de pago", KPI "Tasa de Cobrabilidad" | Pain Point: every failed recurring charge becomes a phone call, with 85% contactability and 62% effectiveness targets, so a large share is never recovered | Yuno Value Prop: recover in the payment layer first (retries, network tokens that follow reissued cards, fallback to a second processor), leaving the call center only the cases that truly need a human | Best Case: Yuno publishes 30% recovered revenue on failed payments | Outreach Angle: "Your tender budgets three years of phone calls to fix declined donations. A good part of those can be fixed before anyone picks up the phone."

**Insight #2: One billing run a month**
Evidence: S5, refund policy: "los procesos de cobro se activan el primer día del mes y son automáticos" | Pain Point: a single attempt date concentrates insufficient-funds declines and makes any processor or bank incident on day 1 expensive; it also drives the cancellation-lag refunds the policy describes | Yuno Value Prop: retry logic after the first attempt, routing to a second processor on technical declines, and real-time monitors on the day of the run | Best Case: 7% approval uplift from smart routing (Yuno published) | Outreach Angle: "What happens today to a donation that fails on the first of the month: is there a second attempt before the call center hears about it?"

**Insight #3: Vault first, several processors allowlisted, no routing layer in evidence**
Evidence: S3, Firstoken vault plus Mercado Pago, Wompi and Nuvei in the site's security policy; no orchestrator found | Pain Point: [INFERENCE, not confirmed] several processors without a decision layer means routing, failover and reporting are manual or absent | Yuno Value Prop: one integration above the processors they already contract, no-code routing rules, no PSP replacement | Best Case: InDrive, 10 LATAM markets in under 8 months with 90% approval | Outreach Angle: "You already have more than one processor connected. Who decides, per transaction, which one gets the charge?"

**Insight #4: Three capture channels, three stacks, one CRM**
Evidence: S3, S6 and S12: web form (Drupal plus Firstoken), advisors on Evergiving (Waysact), donor hub for payment updates, an Azure app for receipts, Salesforce as the system of record, vendors required to integrate by web services, APIs or FTP. UNICEF also publishes that a card transaction costs it COP 700 on average and an account debit COP 1,400 | Pain Point: collection performance and cost by channel and method are hard to see in one place, yet the tender tracks exactly those splits (card vs savings and checking account, payment method changes) and the cheaper method is the one most exposed to expiry and reissue | Yuno Value Prop: one payment layer and one dataset across cards, Nequi, Daviplata, PSE and account debit, feeding Salesforce | Best Case: Rappi, real-time detection in milliseconds vs 5 to 10 minutes manually | Outreach Angle: "Can you see today, in one view, your collection rate by method and by acquisition channel?"

**Insight #5: Less central money, same targets, so retention math matters more than acquisition**
Evidence: S7: UNICEF projects "at least a 20 per cent decline in income from 2026"; the 2026 private sector plan ($1,957M) sits below the 2025 result ($2,215M) while the fundraising division's budget falls from $287M to $230M and country office expenditure is cut by $15M; Colombia is the #7 country office by private fundraising | Pain Point: the two tenders target 48,500 new donors, which is expensive acquisition, while failed charges erode the existing base | Yuno Value Prop: more money to programs from donors they already have | Best Case: Livelo, +5% approval | Outreach Angle: "Each point of collection rate on the existing base is funding that needs no new donor."

---

## SECTION 11: Pipeline

Verification for 11A = a live local donation page on 21-sep-2026; payment observations come from page source. "Gateway not visible" means not observed, not absent.

**11A. Direct Competitors (individual donors in Colombia)**

| Company | Website | HQ | Est. Size | Overlap Markets | Source |
|---|---|---|---|---|---|
| Save the Children Colombia (Fundación Save the Children Colombia, NIT 900.711.100-4) | https://savethechildren.org.co/como-ayudar/donacion/ | Colombia (city not verified) | Not found (79,712 people reached in 2024 per annual report snippet) | Colombia. Wompi confirmed as gateway (form config "wompiApiURL":"https://production.wompi.co/v1", card and Nequi endpoints, monthly commitment endpoint); Nequi, Daviplata, PSE referenced | https://savethechildren.org.co/como-ayudar/donacion/ |
| World Vision Colombia | https://worldvision.co/ | Colombia (city not verified) | Not found | Colombia. Sponsorship portal loads the Mercado Pago SDK (sdk.mercadopago.com/js/v2); HubSpot assets | https://mipatrocinio.worldvision.co/ |
| Médicos Sin Fronteras Colombia (MSF LAT office) | https://www.msf.org.co/ | Bogotá | Not found locally | Colombia. One-time and monthly forms; PSE and Nequi referenced; Salesforce referenced; runs face to face ("Diálogo Directo"). Gateway not visible | https://www.msf.org.co/donar-proyectos-colombia/ |
| Teletón Colombia | https://teleton.org.co/dona/ | Colombia (city not verified) | Not found | Colombia. PayU shown as ally logo; page canonical is mercadopago.teleton.org.co. Two providers visible | https://teleton.org.co/dona/ |
| Cruz Roja Colombiana | https://www.cruzrojacolombiana.org/dona-dinero/ | Colombia (city not verified) | Not found | Colombia. Donation form is an embedded Afrus widget (third-party fundraising platform) | https://www.cruzrojacolombiana.org/dona-dinero/ |
| Fundación Plan (Plan International Colombia) | https://plan.org.co/ | Colombia (city not verified) | Not found | Colombia. Face-to-face fundraisers collect credit card (no CVV) or savings and checking account. Gateway not visible | https://plan.org.co/captatadoras-de-donantes/ |
| Aldeas Infantiles SOS Colombia | https://www.aldeasinfantiles.org.co/donantes | Colombia (city not verified) | Not found | Colombia. Donation microsite sos.aldeasinfantiles.org.co. Gateway not visible | https://sos.aldeasinfantiles.org.co/ |
| Greenpeace Colombia | https://www.greenpeace.org/colombia/asociate/ | Colombia (city not verified) | "more than 3 million" supporters worldwide (snippet) | Colombia. Page describes monthly automatic card debit. Gateway not visible | https://www.greenpeace.org/colombia/asociate/ |
| WWF Colombia | https://donacion.wwf.org.co/ | Colombia (city not verified) | "more than 5 million" supporters globally (snippet) | Colombia. Live donation site. Gateway not visible | https://donacion.wwf.org.co/ |

ACNUR/UNHCR in Colombia: NOT verified as an individual donor fundraiser (acnur.org/colombia returned 403; funding notes list public sector, companies and UN funds only) [https://reliefweb.int/report/colombia/financiacion-y-donantes-de-acnur-colombia-2024-30-de-junio-2024].

**11B. Industry Peers**

| Company | Website | Vertical | Key Markets | Why Similar | Source |
|---|---|---|---|---|---|
| UNICEF country offices in LatAm: Brazil ($21.8M), Chile ($19.1M), Mexico ($18.2M), Uruguay ($14.1M), Argentina ($10.8M) (2024 contributions received) | https://help.unicef.org (shared donation host) | UN agency fundraising | Each its own market | Same model as Colombia (monthly donors, local methods, own stack). A Colombia win is a direct reference | https://www.unicef.org/media/173291/file/UNICEF_FundingCompendium2024.pdf |
| Médicos Sin Fronteras / MSF International | https://www.msf.org | Humanitarian NGO | 70+ countries | 2024 income over EUR 2B, 98% private, "more than 7 million individual donors and private foundations" | https://www.msf.org/international-activity-report-2024/2024-figures |
| UNHCR | https://www.unhcr.org | UN agency fundraising | Global, national partners | 2025 private sector $697M, $386M from individuals, 3.2M individual donors (search snippet; page returned 403) | https://www.unhcr.org/about-unhcr/planning-funding-and-results/contributions |
| World Vision International | https://www.wvi.org | Child sponsorship NGO | Global | 2024 total income $3.3B (search snippet); recurring sponsorship model | https://www.wvi.org/annual-report-2024 |
| Save the Children International | https://www.savethechildren.net | Child rights NGO | 115 countries | "annual revenue of over $2 billion" (search snippet) | https://www.savethechildren.net/about-us/accountability |
| WFP (ShareTheMeal) | https://www.wfp.org | UN agency fundraising | Global | Individual giving program; only dated figures found (2020: $50M from individuals) | https://executiveboard.wfp.org/document_download/WFP-0000124414 |
| Greenpeace International | https://www.greenpeace.org | Environmental NGO | Global | 3M+ supporters, monthly giving model, face-to-face acquisition | https://www.greenpeace.org/colombia/sobre-nosotros/ |
| WWF International | https://www.wwf.org.co/conocenos/quienes_somos_/ | Environmental NGO | Global | 5M+ supporters, monthly giving model | https://www.wwf.org.co/conocenos/quienes_somos_/ |

**11C. Adopting Orchestration**

| Company | Orchestrator | Date | Vertical | Source |
|---|---|---|---|---|
| Wikimedia Foundation | Gr4vy | Reported 11-Apr-2025 | Nonprofit (donations) | https://www.paymentsdive.com/news/gr4vy-payments-orchestration-startup-competition/745101/ |

This is the only nonprofit and orchestrator link found. No nonprofit was found publicly listed as a customer by Yuno, Primer, Spreedly, dLocal, EBANX or Checkout.com. Related but not orchestration: Adyen Giving lists 140+ nonprofits including UNICEF, WWF and UNHCR [https://www.adyen.com/giving/nonprofit]; Stripe's nonprofits page shows UNICEF, World Vision and Greenpeace logos without naming entities or countries [https://stripe.com/industries/nonprofits].

**11D. Scoring, UNICEF Colombia (verified only):**

| Signal | Pts | Verified? |
|---|---|---|
| Operates in 3+ countries | 0 | No. The Colombia office is a single-market operation (UNICEF globally is multi-country, but each office runs its own stack) |
| Multiple PSPs | 0 | Partly. Mercado Pago, Wompi and Nuvei are allowlisted, live use not confirmed. Worth +3 if confirmed on the call |
| Recent expansion (24 mo.) | +2 | Yes. First gala (Apr 2026), two tenders for 48,500 new donors |
| Public payment issues | +2 | Yes. Self-documented: refund policy scenarios and the 90,000-donor collection reactivation target |
| Funding >$10M | +2 | Yes. $16.56M contributions received in 2024 |
| LATAM/APAC/MENA traffic | +2 | Yes. 88.83% Colombia |
| No orchestrator | +2 | Yes. No public evidence of one |
| Payment job postings | 0 | Not within 24 months. 2026 vacancies are donor retention and CRM implementation; the 2023 CRM post mentioned "optimizing CRM collection processes" |
| Public RFP | +3 | Yes, with a caveat: two open RFPs, payments-adjacent (collection recovery, "Plataformas de Cobranza" integrations), not a payment gateway RFP |

**Total: 13, 🔴 High** (10, 🟡 Medium, if the RFP signal is not counted as payment-related; 16 if multiple live PSPs are confirmed on the call).

**Top 10 Pipeline** (scored on verified signals only, so local NGOs score low by construction; "no orchestrator" means no public evidence found):

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal |
|---|---|---|---|---|---|---|
| 1 | UNICEF LatAm country offices (Brazil, Chile, Mexico, Uruguay, Argentina) | Same network | 5 LatAm markets | 9 (3+ countries, funding, LATAM, no orchestrator) | 🟡 Medium, strategic | Same model as Colombia; $10.8M to $21.8M each; a Colombia win is the reference |
| 2 | Médicos Sin Fronteras (MSF LAT, Bogotá office) | Direct competitor and global peer | 70+ countries, Colombia | 9 | 🟡 Medium | EUR 2B+, 98% private, face to face plus PSE and Nequi in Colombia |
| 3 | World Vision (International and Colombia) | Direct competitor and global peer | Global, Colombia | 9 | 🟡 Medium | Recurring sponsorship; Mercado Pago SDK confirmed in Colombia |
| 4 | Save the Children (International and Colombia) | Direct competitor and global peer | 115 countries, Colombia | 9 | 🟡 Medium | Wompi confirmed as the single visible gateway in Colombia |
| 5 | Teletón Colombia | Direct competitor | Colombia | 7 (multiple PSPs, LATAM, no orchestrator) | 🟡 Medium | PayU and Mercado Pago both visible |
| 6 | UNHCR | Global peer | Global | 7 | 🟡 Medium | $386M from 3.2M individual donors (snippet) |
| 7 | WFP (ShareTheMeal) | Global peer | Global | 7 | 🟡 Medium | App-based individual giving; figures dated |
| 8 | Greenpeace (International and Colombia) | Direct competitor and global peer | Global, Colombia | 7 | 🟡 Medium | Monthly card debit model |
| 9 | WWF (International and Colombia) | Direct competitor and global peer | Global, Colombia | 7 | 🟡 Medium | Live Colombian donation site |
| 10 | Cruz Roja Colombiana | Direct competitor | Colombia | 4 | 🟢 Low | Afrus third-party donation widget |

Pipeline Summary: 17 organizations found (9 verified fundraisers in Colombia, 8 peer rows), 0 high-priority on verified signals alone. Strongest vertical: recurring-donor nonprofits in LatAm, where the most direct follow-on is the other UNICEF country offices in the region. Only one nonprofit was found using an orchestrator (Wikimedia Foundation with Gr4vy), so the category is largely untouched.

---

## SECTION 12: Business Case

| Annual Revenue | Avg Transaction Value | Est. Annual Transactions | Primary Currency | Top 3 Markets |
|---|---|---|---|---|
| $16.56M contributions received by UNICEF from Colombia private sector fundraising in 2024 (gross donations processed may be higher). UNVERIFIED snippet from a 2026 vacancy: "average monthly collection of USD 1.5 million", which would be about $18M a year | Suggested monthly gifts COP 50,000 and 80,000 (80,000 default); agency minimum COP 40,000; one-time COP 100,000 and 200,000. From the unverified snippet: about USD 11.5 per active donor per month [ESTIMATE: 1.5M / 130,000] | [ESTIMATE, from the unverified snippet] "over 130,000 active donors" x 12 monthly charges = about 1.56M successful charges a year, before failed attempts, retries and one-time gifts. Official donor count: No public information found; ask on the call | COP (UNICEF reports in USD) | Colombia (single market) |

Cost side, published by UNICEF Colombia: "Una transacción con tarjeta de crédito nos cuesta en promedio $700, mientras que un débito nos cuesta en promedio $1.400" (COP per transaction; "débito" is account debit) [https://donaciones.unicef.org.co/captadores].

Size of the recovery problem, from the tender: collection to be reactivated for 90,000 recurring donors over 3 years, against 48,500 new donors to be acquired across both tenders (28,500 plus 20,000). The tender publishes no decline or failure rate [INFERENCE, not confirmed: failed recurring payments are a volume problem comparable to or larger than new acquisition].

Sources: https://www.unicef.org/media/173291/file/UNICEF_FundingCompendium2024.pdf, https://donaciones.unicef.org.co/donar, https://donaciones.unicef.org.co/captadores, https://www.unicef.org/colombia/convocatorias-para-empresas, https://jobs.unicef.org/en-us/job/561454 (expired listing; snippet only)

---

## SECTION 13: Outreach (verified findings only)

The three attendees are already in a live conversation, so this outreach targets the likely executive sponsor who is not on the invite: Gustavo Ugalde Balcázar (Chief of Fundraising). Messages are in Spanish because the recipient is in Bogotá. No customer names in a first touch, per German's standing rule.

```
--- LINKEDIN MESSAGE ---
Hola Gustavo, felicitaciones por la primera gala de UNICEF Colombia.

Leí la convocatoria de Recaudación de Fondos: reactivar el cobro de 90.000 donantes recurrentes en tres años, actualizando medios de pago por teléfono. Una parte de esas donaciones fallidas se puede recuperar antes de la llamada, directamente en la capa de pagos: reintentos inteligentes, tokens de red que siguen a la tarjeta cuando el banco la reexpide y enrutamiento entre los procesadores que ya tienen.

En Yuno hacemos eso con una sola integración, sin cambiar de procesador. Esta semana conversamos con tu equipo de donantes individuales. ¿Te sirve que te comparta un resumen de 15 minutos el jueves en la mañana?

--- COLD EMAIL ---
Subject: Los 90.000 donantes de la convocatoria RFP2026-10

Hola Gustavo,

La convocatoria de Recaudación de Fondos que cierra el 28 de septiembre pide reactivar el cobro de 90.000 donantes recurrentes en tres años, actualizando por teléfono los datos del medio de pago, y mide la Tasa de Cobrabilidad como indicador.

Esa recuperación hoy depende de contactar al donante. Con UNICEF proyectando una caída de al menos 20% en ingresos desde 2026, cada punto de cobrabilidad sobre la base actual es financiación que no requiere adquirir un donante nuevo.

Yuno es una capa de orquestación de pagos: una sola integración por encima de los procesadores y métodos que ya usan (tarjetas, Nequi, Daviplata, PSE, débito a cuenta). Sobre esa base:

1. Reintentos y recuperación de cobros fallidos antes de que el caso llegue al call center. Nuestra cifra publicada es 30% de ingresos recuperados.
2. Enrutamiento inteligente entre procesadores, con 7% de mejora en aprobación.
3. Monitores en tiempo real para el cobro del primer día del mes, y una sola vista de cobrabilidad por método y canal, conectada a Salesforce.

Esta semana tuvimos una primera conversación con tu equipo. ¿Tienes 20 minutos el jueves o viernes para mostrarte cómo se vería en UNICEF Colombia?

Un saludo,
German Tatis
Yuno
```

---

## MEETING AGENDA & QUESTIONS (4:00 to 4:30pm COT)

**Agenda (30 min)**
1. 0 to 3 min: intros and roles round (roles are only partly verified; ask each person what they own).
2. 3 to 15 min: discovery. What made them book the demo, and how recurring collection works today.
3. 15 to 25 min: Yuno, focused on recurring donations: recovery of failed charges, routing across existing processors, monitors, one view by method and channel. Skip generic multi-country content; this is a single-market operation.
4. 25 to 30 min: next steps. Technical session with Idual's team, data request (decline rates by method), and how UNICEF buys (RFP or LTA vs direct).

**Questions (in Spanish, as they would be asked)**
1. ¿Qué los llevó a agendar la demo? ¿Hay un proyecto o una fecha detrás?
2. ¿Cuál es hoy la Tasa de Cobrabilidad del cobro del primer día del mes, y cómo se reparte entre tarjeta de crédito, cuenta de ahorros o corriente, Nequi y Daviplata?
3. De los cobros que fallan, ¿cuántos son por tarjeta vencida o reexpedida y cuántos por fondos insuficientes? ¿Hay reintentos automáticos antes de pasar el caso al call center?
4. ¿Qué procesadores están activos hoy detrás de Firstoken (Mercado Pago, Wompi, otros) y quién decide a cuál va cada cobro?
5. ¿El débito a cuentas de ahorros y corriente cómo se procesa hoy (archivos con los bancos, ACH, un agregador)?
6. Las altas de face to face y telemarketing entran por Evergiving: ¿con qué pasarela se cobran y cómo llegan a Salesforce?
7. ¿Usan network tokens o algún servicio de actualización automática de tarjetas?
8. ¿Cuántos donantes activos mensuales tienen hoy y cuál es la donación promedio? (Hay un dato sin verificar de más de 130.000 donantes activos y USD 1,5 millones de recaudo mensual; confirmarlo, no citarlo.)
8b. Ustedes publican que una transacción con tarjeta cuesta en promedio $700 y un débito a cuenta $1.400. ¿Cómo se reparte hoy la base entre los dos métodos, y cuál tiene mejor cobrabilidad?
9. ¿La convocatoria RFP2026-10 cambia algo en la parte tecnológica, o es solo el operador de telemarketing?
10. ¿Cómo compra UNICEF Colombia un servicio como este: convocatoria, LTA regional, aprobación de Ginebra o de la oficina regional? ¿Quién más debería estar en la conversación (Gustavo Ugalde, finanzas, ICT)?
11. ¿Las decisiones de stack de pagos son locales o hay lineamientos globales de PFP?

**Do not say:** that they lack any payment method, that a specific PSP is live (it is inferred from site code), or any Yuno reconciliation claim (roadmap).

---

## APPENDIX: Source URLs

```
[S1] https://www.semrush.com/website/unicef.org.co/overview/
     https://www.similarweb.com/website/unicef.org/
     https://www.semrush.com/website/unicef.org/overview/
     https://www.similarweb.com/website/unicef.es/ (and the other committee domains listed in Section 1C)
[S2] https://donaciones.unicef.org.co/aviso-privacidad
     https://donaciones.unicef.org.co/politica-proteccion-datos-personales
     https://www.unicef.org/unicef-national-committees
     https://www.unicef.org/media/173291/file/UNICEF_FundingCompendium2024.pdf
[S3] https://donaciones.unicef.org.co/donar (HTML, scripts and CSP response header)
     https://unicef.org.co/donar-mensual
     https://donaciones.unicef.org.co/webform/javascript/donaciones_hibrido_drtv/custom.js
     https://firstoken.co/
     https://donaciones.unicef.org.co/preguntas-frecuentes
     https://www.evergiving.com/payment-gateways
     https://www.unicef.de/spenden | https://don.unicef.fr/ | https://www.unicef.or.kr/donate/ | https://www.unicef.org.uk/donate/
     https://www.y.uno/partner/wompi | https://y.uno/partner/nuvei | https://y.uno/partner/nequi
     https://docs.y.uno/docs/payment-features/enrollment/enroll-payment-methods
[S4] https://donaciones.unicef.org.co/donar | https://donaciones.unicef.org.co/
     https://www.unicef.org/colombia/como-vincularse | https://donaciones.unicef.org.co/alianzas-corporativas
[S5] https://donaciones.unicef.org.co/politica-de-reintegros
     https://donaciones.unicef.org.co/donantes-hub/contacto
     https://donaciones.unicef.org.co/donantes-hub/actualizacion-medio-pago
     https://www.trustpilot.com/review/www.unicef.org.uk | https://www.trustpilot.com/review/unicef.es
[S6] https://www.unicef.org/colombia/convocatorias-para-empresas
     RFP2026-10 ToR: https://unicef-my.sharepoint.com/:b:/g/personal/aocasiones_unicef_org/IQAJoC7ccCJ6TbdE106aUm1MASxbwtR0nOCvmbJ3VwVK3xc?e=JHm9nv
     RFP2026-11 ToR: https://unicef-my.sharepoint.com/:b:/g/personal/aocasiones_unicef_org/IQBXM-ajUzMvRLhOPG7iNPu_AbOaVBJ0MyiE7SVTZpKux14?e=LdcaC4
     https://www.portafolio.co/economia/gobierno/unicef-colombia-recaudo-mas-de-560-millones-de-pesos-en-su-primera-gala-para-la-educacion-de-ninos-en-cordoba-492914
     https://www.linkedin.com/in/gustavougaldeb/
     https://www.unicef.org/colombia/comunicados-prensa/unicef-celebrar%C3%A1-en-colombia-su-primera-gala-ben%C3%A9fica-para-apoyar-la-ni%C3%B1ez-y
     https://unjoblink.org/job/details/416493/ | https://jobs.unicef.org/en-us/job/561454 (expired)
     https://untalent.org/jobs/salesforce-crm-implementation-associate-gs7-ta-12-months-bogota-colombia
     https://www.impactpool.org/jobs/861601 (Database Officer post, 2022)
     https://www.ungm.org/Public/Notice/242854
     https://www.accenture.com/us-en/case-studies/public-service/unicef-revamps-fundraising-future
     https://donaciones.unicef.org.co/alianzas-corporativas
[S7] https://www.unicef.org/media/current-issues/information-note-ongoing-restructuring-initiatives
     https://www.unicef.org/partnerships/funding
     https://www.unicef.org/executiveboard/media/39341/file/2026-AS-Item-16-PFP-financial-report-Carla-Haddad-Mardini-PPT-EN-2026-06-17.pdf
     https://www.unicef.org/executiveboard/media/35901/file/2026-FRS-Item-13-PFP-Workplan-Budget-Carla-Haddad-Mardini-PPT-EN-2026-02-04.pdf
     https://www.adyen.com/press-and-media/adyen-and-unicef-launch-partnership
     https://www.ungm.org/Public/Notice/177105
     https://www.disruptionbanking.com/2026/05/21/bitget-and-unicef-partner-to-boost-ai-and-financial-literacy-among-youth-in-8-countries/
     https://www.unicef.org/colombia/comunicados-prensa/banco-de-bogota-y-unicef-firman-alianza
[S8] https://donaciones.unicef.org.co/donar
[S9] https://donaciones.unicef.org.co/donar | https://donaciones.unicef.org.co/preguntas-frecuentes
[S11] https://savethechildren.org.co/como-ayudar/donacion/ | https://mipatrocinio.worldvision.co/
      https://www.msf.org.co/donar-proyectos-colombia/ | https://teleton.org.co/dona/
      https://www.cruzrojacolombiana.org/dona-dinero/ | https://plan.org.co/captatadoras-de-donantes/
      https://sos.aldeasinfantiles.org.co/ | https://www.greenpeace.org/colombia/asociate/ | https://donacion.wwf.org.co/
      https://www.msf.org/international-activity-report-2024/2024-figures
      https://www.unhcr.org/about-unhcr/planning-funding-and-results/contributions
      https://www.wvi.org/annual-report-2024 | https://www.savethechildren.net/about-us/accountability
      https://www.paymentsdive.com/news/gr4vy-payments-orchestration-startup-competition/745101/
      https://www.adyen.com/giving/nonprofit | https://stripe.com/industries/nonprofits
      https://fundraiseup.com/case-studies/unicef-usa/
[S12] https://www.unicef.org/media/173291/file/UNICEF_FundingCompendium2024.pdf
      https://donaciones.unicef.org.co/captadores (cost per transaction, verified in page text 21-sep-2026)
      https://jobs.unicef.org/en-us/job/561454 (expired; donor count and monthly collection are an unverified search snippet)
```
