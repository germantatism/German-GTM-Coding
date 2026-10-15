# LatAm markets for a gaming top-up shop: Brazil, Argentina, Mexico, Colombia, Bolivia (research agent, 15 Oct 2026)

Labels: CONFIRMED (docs.y.uno or y.uno) · PUBLIC DOCS (third-party public page, dated) · ESTIMATE (modeled or derived, assumption stated) · OPEN (with owner) · NOT FOUND. USD only; where a source reports local currency the figure is replaced by a currency-free metric. Provider-per-method data comes from the Yuno integrations directory pull of 14 Oct 2026 (Deals/Adidas/build/csv/by_country.json), cited as "Yuno integrations directory, Oct 2026". Vendor approval-rate claims are directional, never independent studies; say so on the slide.

## Cross-country facts used on every slide
* Newzoo 2025 (via secondary reports, Apr 2026): Latin America games revenue about $8.3B (+6.4%), 372.3M players (+4.5%); global $188.8B (+3.4%); mobile about $103B globally (+2.9%). PUBLIC DOCS.
* Approval gap, local vs cross-border (all vendor claims, PUBLIC DOCS): Worldline LatAm brochure: offshore solutions 20 to 45% approval for international cards vs 60 to 80% for local cards via its cross-border product · Rapyd: 20 to 45% with offshore methods vs 80% or more with local acquiring · Nuvei (Mexico): local acquiring "20% to 30% higher" authorization than cross-border routing · EBANX (Colombia, 11 Sep 2017): "near to 80%" via local acquirers vs "the average 30% in Latin America" for international acquirers (AMI data) · Antom (Brazil): cross-border card authorization "below 60%" vs "90%+" for local channels such as Pix · EBANX homepage: "+10.2 pp uplift" for its merchants (2021 to 2022 data). Rule-of-thumb for the deck: cross-border cards 30 to 60%, local acquiring or local MoR 80 to 90%, labelled "vendor-reported ranges, 2017 to 2026".
* Launch time, MoR vs local entity (PUBLIC DOCS): dLocal dMoRe (26 Aug 2026): market entry "from up to a year down to up to 8 weeks" · PayPro Global: MoR launch "in weeks or even days" vs 9 to 18 months to open a branch · incorporation and bank-account timelines per country below (consultancy estimates). Yuno's role: the move from MoR to local acquirer is a new connection and a routing rule, checkout unchanged (CONFIRMED, docs connections and routing).

---

## Brazil  ![BR](https://flagcdn.com/w80/br.png)

### Gaming and digital goods
* Largest games market in Latin America; about 103M to 115M players (103M per local press citing ISTOÉ Dinheiro 2025; 115M per Newzoo via Allcorrect). Revenue estimates for 2025 range from $2.5B (Allcorrect projection) to $2.6B (Newzoo via Mundo do Marketing, 2025). Brazil ranked 10th globally by revenue and 5th by players (Newzoo, 2022). PUBLIC DOCS, estimates conflict; show "about $2.5B, 100M+ players".
* Mobile share: about 60.8% of games revenue (IMARC, 2025 estimate). PUBLIC DOCS.
* Card-less or unbanked gamers: 142M people (93% of adults) made at least one Pix payment in Apr 2026 (Banco Central via press, May 2026); about 70% of Brazilian Visa and Mastercard cards are domestic-only and cannot pay cross-border (IQPC document, undated). PUBLIC DOCS. Top-up behaviour by method: NOT FOUND.

### E-commerce payment mix 2025 to 2026
* Pix took 42% of online purchases in 2025, credit cards 41%; EBANX projects Pix at 45% by end 2026 and 50% in 2028 (Reuters, 10 Feb 2026, EBANX forecast on PCMI data). PUBLIC DOCS.
* Global Payments Report 2026: Pix 42% of e-commerce transaction value in 2025, credit cards 40%, cards still lead "because of installments" (via Gironews/LetsMoney, 2026). PUBLIC DOCS.
* Installments: 47% of total online sales volume (EBANX Beyond Borders 2026 via press). Boleto share: NOT FOUND for 2025.
* Pix scale: 80 billion transactions in 2025 (+25%), 374 operations per capita; 12M merchants receiving Pix (Banco Central presentations via press, 2026). PUBLIC DOCS.
* Card brand mix in e-commerce: Mastercard 48%, Visa 37%, Elo 9% (Finsiders, Brazilian cards study, 2025). PUBLIC DOCS.

### Approval rates
* Cross-border card authorization "below 60%" vs "90%+" for local channels; e-commerce fraud rate cited at 3.9% (Antom market page, 2026). Local acquiring rule of thumb: 80 to 90% (vendor ranges above). PUBLIC DOCS, vendor claims.

### Tax and withholding reality: cross-border MoR vs local entity
* IOF on international card purchases: 3.5% since 17 Jul 2025 (credit, debit and prepaid), legal basis Decree 6.306/2007 art. 15-B as amended by Decree 12.499/2025; the 2022 step-down schedule (2.38% from Jan 2026, zero in 2028) is discontinued after Congress suspended the May 2025 increase (Legislative Decree 176/2025) and the STF reinstated it (ADC 96). PUBLIC DOCS (ARQ Finance, 29 Sep 2026; Tecnoblog; BR-MM). Relevance: a Brazilian consumer paying a foreign merchant with a card bears IOF; a local-currency charge through a MoR's Brazilian entity is domestic. OPEN, owner German: confirm with EBANX and dLocal that their Brazil charges are domestic for IOF purposes.
* Imported digital services today: IRRF, CIDE, PIS/COFINS-Importação, ISS and IOF stack (worked example in an IBDT 2025 presentation shows 15% IRRF and 5% ISS). PUBLIC DOCS; CIDE and PIS/COFINS rates not re-verified in this pass.
* Tax reform: CBS (federal) and IBS (state and municipal) in test mode for 2026 at 0.9% and 0.1%; Decree 12.955/2026 and CGIBS Resolution 6/2026 bring non-resident digital providers and platforms into scope, registration with no revenue threshold and obligations from 1 Aug 2026; CBS replaces PIS/COFINS in 2027; IBS phases in from 2029 to 2033; reference rates commonly cited around 26.5% combined. PUBLIC DOCS (VATCalc, Fonoa, DHL, 2026).
* CPF: required for every EBANX and dLocal Brazil payment (11 digits). PUBLIC DOCS.
* Launch time: MoR weeks; local entity 6 to 12 weeks for a foreign-owned company (registration often quoted at 60 to 90 days, Redesim states faster), bank account only after CNPJ and often the slowest step, foreign shareholders registered within 30 days, Central Bank FDI registration. PUBLIC DOCS (Healy, Commenda, Wise, TMF, 2025 to 2026). Acquirer onboarding time: NOT FOUND.

### Method priority for a gaming top-up shop
| Priority | Method | Why | Carried through Yuno by (Yuno integrations directory, Oct 2026) |
|---|---|---|---|
| Must-have | Pix | 42% of online purchases, instant confirmation fits instant delivery | EBANX, dLocal, Adyen, Cielo, Getnet, Mercado Pago, PagSeguro, Pagar.me, PagBank, Nuvei, Stripe (Pix Automático), PayRetailers, Pagsmile and 20+ more |
| Must-have | Credit and debit cards incl. Elo and Hipercard | 40 to 41% of value; installments 47% of volume | EBANX, dLocal (Elo, Hipercard), Adyen, Cielo, Rede, Stone, Getnet, PagSeguro, Worldpay, Stripe and others |
| Optional | Boleto | Legacy cash voucher, delayed confirmation (up to 8 days at dLocal) | EBANX, dLocal, Mercado Pago, Pagar.me, PagBank, Banco do Brasil, Bradesco |
| Optional | NuPay, PicPay, Mercado Pago Wallet | Wallet reach | dLocal (NuPay), EBANX (PicPay), Mercado Pago, PicPay, Spinpay |
| Optional | Google Pay, Apple Pay, PayPal | Wallets (PayPal is a wallet, not a PSP) | Listed for Brazil in the directory |

SO WHAT: launch Brazil with Pix and local cards through the MoR; keep Boleto off at launch (slow confirmation hurts instant top-ups). TO VALIDATE: Boleto share 2025; acquirer onboarding time.

---

## Argentina  ![AR](https://flagcdn.com/w80/ar.png)

### Gaming and digital goods
* Newzoo (2024, via iProUP): about $780M games revenue, mobile about $319M, about 26.5M players, second largest player base in South America. A Statista figure of $1.78B for 2025 circulates in press but could not be reconciled with Newzoo; show the Newzoo 2024 figure. PUBLIC DOCS, sources conflict.
* Players equal about 40% of the population (sector investor report via Forbes Argentina, 2023). PUBLIC DOCS.
* Card-less gamers: no direct metric. Proxy: digital wallets are 46% of e-commerce volume and domestic-only credit cards 22% (PCMI, 2024 data). PUBLIC DOCS.

### E-commerce payment mix 2025 to 2026
* PCMI (2024 data, published 2025): digital wallets 46%, domestic-only credit cards 22%, internationally enabled credit cards 12%, debit cards 11%, cash 3%, bank transfers 2%; Mercado Pago is the most used wallet. PUBLIC DOCS.
* Global Payments Report 2026 (via Forbes Argentina, May 2026): digital wallets above 55% of e-commerce transactions. PUBLIC DOCS.
* MODO: more than 17M users and about 800K merchants (2024, Play Digital via Descubre); 35+ member banks. QR payments exceeded 100M transactions per month in May 2026; banks via MODO initiate 52.8% of QR payments, fintechs led by Mercado Pago accept 52.4% (Descubre, 14 Jul 2026). PUBLIC DOCS.
* Rapipago and Pago Fácil: cash share is 3% to 4% of e-commerce (PCMI 2024; PPRO). PUBLIC DOCS.

### Approval rates
* No Argentina-specific published figure. Use the regional vendor ranges (20 to 45% offshore vs 80%+ local). Structural point: domestic-only credit cards (22% of volume) cannot be charged cross-border at all (PCMI definition). PUBLIC DOCS.

### Tax and withholding reality: cross-border MoR vs local entity
* Impuesto PAIS: no longer charged since 23 Dec 2024 (its five-year term expired). PUBLIC DOCS (Fortuna, 29 Jul 2026, data as of 22 Sep 2026; Reba).
* Percepción Ganancias / Bienes Personales: a single 30% advance payment on card purchases in foreign currency, RG 5617/2024 (ARCA), still in force in Sep 2026; refundable only through an ARCA claim after year end. PUBLIC DOCS (Fortuna, 2026). Relevance: a USD-priced cross-border charge costs the gamer 30% more; a charge in local currency through a local MoR is a domestic card transaction. OPEN, owner German: confirm with EBANX and dLocal that their Argentina card charges are not subject to the 30% perception.
* IVA on digital services supplied from abroad (Ley 27.430 Título II, RG 4240/2018): the card issuer or local payment intermediary withholds the IVA when the buyer is a consumer; general IVA rate applies. PUBLIC DOCS (Boletín Oficial 14 May 2018; ARCA consultation Oct 2025 via Blog del Contador). Verify the rate applied by each MoR (OPEN, owner German).
* Documents: DNI, CUIT or CUIL required by EBANX and dLocal; CUIT mandatory for DEBIN. PUBLIC DOCS.
* Launch time: MoR weeks. Local entity: SAS incorporation 7 to 15 business days, CUIT in 24 to 48 hours (commercial guide, Jan 2025); IGJ RG 8/2024 requires at least one member with real domicile in Argentina and a CDI plus local representative for foreign members; bank-account timing NOT FOUND. PUBLIC DOCS.

### Method priority for a gaming top-up shop
| Priority | Method | Why | Carried through Yuno by (Yuno integrations directory, Oct 2026) |
|---|---|---|---|
| Must-have | Mercado Pago Wallet | Wallets 46 to 55% of e-commerce | Mercado Pago (Wallet, Checkout Pro), EBANX (Checkout Pro), dLocal |
| Must-have | Credit and debit cards incl. Naranja, Cabal | 45% of volume across the three card lines | EBANX, dLocal, Prisma, Fiserv, Mercado Pago, Getnet, Nuvei, PayU, Worldline, Worldpay and others |
| Must-have (Phase 1b) | MODO and interoperable QR | 17M+ users, 100M+ QR payments a month; not available via EBANX | dLocal (MODO), MODO direct |
| Optional | Rapipago, Pago Fácil | Cash 3 to 4%, slow confirmation | dLocal, Bamboo (Pago Fácil) |
| Optional | Bank transfer, DEBIN | Small share | dLocal, Unlimint, Bamboo (Transferencias 3.0) |

SO WHAT: Argentina is a wallet market where the 30% perception makes local-currency MoR pricing the whole game; MODO only arrives through dLocal. TO VALIDATE: perception treatment per MoR; 2025 games revenue.

---

## Mexico  ![MX](https://flagcdn.com/w80/mx.png)

### Gaming and digital goods
* "Game On: el auge del gaming en México" (Endeavor México and Santander, 2025): more than 76M active players, more than $2.3B annual revenue, largest market in Latin America and tenth globally; 67 gaming companies based in Mexico (via Forbes México, El Universal, IFT 1H2025). PUBLIC DOCS. Note the conflict with Brazil also claiming the regional lead; show both as "top two LatAm markets".
* Statista: market growth 12.9% in 2023, slowing toward about 7% a year by 2027; mobile the largest segment. PUBLIC DOCS, values paywalled.
* Card-less gamers: ENIF 2024 (via FacePhi 2026): about 80% of adults 18 to 70 hold at least one formal financial product, 63% a savings account, 15.7% a credit card, 37.3% formal credit. PUBLIC DOCS, secondary.

### E-commerce payment mix 2025 to 2026
* AMVO Estudio de Venta Online 2026 (Mar 2026): 77.2M digital buyers in 2025, retail e-commerce +19.2% in 2025, Mexico enters the global top 10. PUBLIC DOCS (method shares in the PDF are not machine-readable; OPEN, owner content agent, if needed).
* AMVO Estudio de Venta Online 2024 (usage, multi-answer): debit card 74%, credit card 54%, transfers or deposits 20%, cash 17%, wallets 8%. AMVO Ecosistema Financiero Digital 2025: eight of ten online buyers use cards or SPEI transfers. PUBLIC DOCS.
* PCMI (Jan 2025, by value): internationally enabled credit cards 29%, digital wallets 10%, cash 6%. Debit share of e-commerce value: 38% in 2024 (Unlimit) vs about 23% in 2025 (Antom), conflicting methodologies. PUBLIC DOCS.
* OXXO: cash at convenience chains represented 26% of transactions in a 2024 AMVO reading (via press); OXXO-specific share NOT FOUND.

### Approval rates
* Nuvei: direct local acquiring yields authorization "20% to 30% higher than cross-border routing"; Unlimit: many Mexican debit cards are not enabled for e-commerce or cross-border and are declined as out-of-territory when routed through an international acquirer; Antom: Mexican debit cards frequently fail 3DS on foreign merchant sites; Carnet debit sees higher declines through international gateways (Nuvei). PUBLIC DOCS, vendor claims.

### Tax and withholding reality: cross-border MoR vs local entity
* IVA 16% on digital services supplied by non-residents to Mexican consumers since 1 Jun 2020; non-residents register with SAT and charge the 16%; a legal representative in Mexico is cited as required by some guides; a 2026 guide reports that from 1 Apr 2026 platforms must give SAT real-time access to transaction data (not confirmed in an official publication). PUBLIC DOCS (Kintsugi 2026; Siemprealdía; Veritas). Platform withholding rules (IVA and ISR) apply to intermediary platforms, not to a direct seller.
* Documents: CURP or RFC optional at EBANX, required at dLocal. PUBLIC DOCS.
* Launch time: MoR weeks. Local entity: 4 to 12 weeks end to end (BizLatinHub 4 to 6 weeks; Commenda about 10 weeks; notarial deed 3 to 10 business days, Public Registry 5 to 15 business days, RFC and e.firma 1 to 7 business days, bank KYC 2 to 8 weeks); RNIE registration within 40 business days. PUBLIC DOCS (2025 to 2026 consultancy guides).

### Method priority for a gaming top-up shop
| Priority | Method | Why | Carried through Yuno by (Yuno integrations directory, Oct 2026) |
|---|---|---|---|
| Must-have | Debit and credit cards incl. Carnet | Debit is the most used online method (74% usage) | EBANX, dLocal (Carnet), Adyen, Banorte, BBVA, Conekta, Kushki, Openpay, Prosa, Stripe, Nuvei, PayU, Worldpay and others |
| Must-have | SPEI | Eight of ten buyers use cards or SPEI; instant | EBANX, dLocal, Kushki, Nuvei, PagSeguro, STP, Unlimint, Bamboo |
| Must-have | OXXO Pay (digital) and OXXO cash | Cash still 17% of usage; OXXO Pay confirms faster than paper vouchers | EBANX (OXXO Pay), dLocal (OXXO, 7-Eleven, Paynet), Bamboo, PagSeguro, Paymentez, Unlimint |
| Optional | Mercado Pago Wallet, CoDi | Wallets about 8 to 10% | Mercado Pago, EBANX (Checkout Pro), dLocal (CoDi), Unlimint |
| Optional | Google Pay, Apple Pay, PayPal | Wallets | Listed for Mexico |

SO WHAT: Mexico is a debit market where cross-border routing loses the issuer; the MoR must present as domestic and support Carnet and SPEI. TO VALIDATE: AMVO 2026 method shares; OXXO share.

---

## Colombia  ![CO](https://flagcdn.com/w80/co.png)

### Gaming and digital goods
* Statista (via Valora Analitik, 2025): games revenue expected above $500M in 2025, about 28M users, more than 80% of players on mobile. PUBLIC DOCS, single-source projection.
* Card-less gamers: Nequi reached 28M active users in May 2026; Bre-B has more than 36M users with at least one key (Oct 2026). Credit-card penetration: NOT FOUND for 2025. PUBLIC DOCS.

### E-commerce payment mix 2025 to 2026
* CCCE, Q2 2025 (Valora Analitik, 24 Aug 2025): PSE account debit 63.9% of transactions, credit cards 33.3%, cash incl. cash on delivery 2.7%; 140.6M approved transactions (+10.6%). Trend 2022 to 2025: PSE 35.4% to 63.9%, cards 59.4% to 33.3%, cash 5.2% to 2.7% (MinTIC observatory on CCCE data). PUBLIC DOCS.
* PCMI (2024 data, by value): internationally enabled credit cards 43%, bank transfers 34%, debit cards 6%, digital wallets 5%, BNPL 4%, cash 3%. PUBLIC DOCS.
* Bre-B (launched Oct 2025): at its first anniversary, 6 Oct 2026, more than 1.7 billion transactions in twelve months, 62% of operations are small-value payments, more than 36M users with a key, more than 116M keys registered, 245 connected entities (Banco de la República press release, 6 Oct 2026). Daily volume above 5M operations by May 2026 (Infobae). PUBLIC DOCS.
* Nequi: 28M active users (May 2026); Nequi becomes a licensed finance company on 1 Sep 2026. Daviplata: last public figure 15.7M clients (2022). PUBLIC DOCS.

### Approval rates
* EBANX (11 Sep 2017): cross-border merchants "can expect a credit card approval rate near to 80%" via local acquirers vs "the average 30% in Latin America" with international acquirers (AMI). PUBLIC DOCS, dated. Use with the regional ranges.

### Tax and withholding reality: cross-border MoR vs local entity
* IVA 19% on digital services supplied from abroad to Colombian users; the non-resident either registers and files bimonthly or is subject to 100% withholding of the IVA by card issuers and other agents (Estatuto Tributario; Accounter summary). Hosting and cloud excluded. PUBLIC DOCS.
* Presencia Económica Significativa (art. 20-3 ET, Decreto 2039/2023): non-residents with deliberate and systematic interaction with Colombian users (presumed at 300,000 or more users, or pricing in local currency) and gross income above 31,300 UVT face a 10% withholding on gross income, or may elect to file and pay 3% of gross income from digital goods and services sold to Colombian users; DIAN Concept 525 of 8 Jul 2024 covers tax-treaty cases. PUBLIC DOCS (El Universal; Accounter; DIAN). 2025 emergency-decree measures (Decreto 1390/2025) targeted goods imports via platforms, not digital services; status OPEN.
* Documents: CC, NIT or CE required by EBANX and dLocal; local processing at EBANX requires IVA data in the request. PUBLIC DOCS.
* Launch time: MoR weeks. Local entity: SAS can be constituted online through the Bogotá Chamber of Commerce (up to 10 shareholders, electronic signatures); RUT provisional online, NIT at DIAN, bank account after tax registration; foreign shareholders need an apostilled power of attorney; day counts NOT FOUND. PUBLIC DOCS.

### Method priority for a gaming top-up shop
| Priority | Method | Why | Carried through Yuno by (Yuno integrations directory, Oct 2026) |
|---|---|---|---|
| Must-have | PSE | 63.9% of e-commerce transactions | dLocal, PayU, Kushki, Wompi, Nuvei, Mercado Pago, Bamboo, Paymentez, PagSeguro, Unlimint (EBANX carries PSE Avanza per its docs; not in the directory local list) |
| Must-have | Nequi (push and QR) | 28M users, instant | dLocal, Nequi direct, Wompi, Nuvei, Bamboo, Paymentez |
| Must-have | Credit and debit cards | 33% of transactions, 43% of value | EBANX, dLocal, Credibanco, Redeban, Wompi, PayU, Kushki, Nuvei, Mercado Pago, Worldpay and others |
| Must-have (fast follow) | Bre-B | 36M users, 1.7B transactions in year one | dLocal, Refacil (EBANX lists Bre-B in its docs) |
| Optional | Daviplata, Efecty | Wallet reach; cash 2.7% | Daviplata direct, Wompi, Nuvei, Paymentez (Daviplata); dLocal, PagSeguro, Paymentez, Unlimint (Efecty) |

SO WHAT: Colombia is an account-to-account market (PSE now, Bre-B next); cards are a third of transactions. PES tax rules make the local MoR the clean path for a foreign seller. TO VALIDATE: whether EBANX's PSE Avanza and Bre-B are enabled on Carry1st's account; credit-card penetration 2025.

---

## Bolivia  ![BO](https://flagcdn.com/w80/bo.png)

### Gaming and digital goods
* Statista Video Games outlook (2024 edition, values in EUR, omitted): mobile games about 58% of games revenue (derived from the two published segment values, ESTIMATE), 7.55% CAGR 2024 to 2027, user penetration 11.5% in 2024 rising to 13.1% in 2027, about 1.7M users by 2027; analyst note that high inflation challenges affordability and favours budget-friendly games. PUBLIC DOCS, dated 2024.
* Market still early: "Bolivia is an early-stage digital commerce market", "Cross-border transactions account for the majority of total e-commerce volume" (EBANX Bolivia overview, 2026). PUBLIC DOCS.

### Payment mix 2025 to 2026
* Banco Central de Bolivia (via Los Tiempos, 14 Jun 2026): cash fell from 85% of payments in 2020 to 64% in 2025 while QR rose from 15% to 36%; 28 QR payments per second; 3.7M QR users (Asoban); a record 891M QR transactions in 2025. PUBLIC DOCS.
* 99.6% of retail payment operations were in local currency in the first half of 2026 (BCB via La Razón). PUBLIC DOCS.
* Cards for international and online payments: after almost three years of restrictions due to dollar scarcity, banks restored international card payments on 9 Apr 2026; credit cards subject to each client's credit line, debit cards with a monthly limit of $500, all at the BCB daily reference rate (Asoban via Los Tiempos, 9 Apr 2026). Previously ASFI Resolution 216/2025 allowed up to $100 of foreign transactions without commission, with a variable commission above (via eju.tv). PUBLIC DOCS.
* Exchange-rate unification: Ministerial Resolution 245/2026 (Ministry of Economy, 26 Jun 2026) established a flexible exchange-rate regime and delegated the transition to the BCB (board resolution 88/2026); the first flexible official rate took effect on Mon 29 Jun 2026, replacing the fixed rate held for 15 years; the official rate is now a daily weighted average of bank dollar purchases published each evening for the next day. The first flexible rate was about 40% weaker than the old fixed selling rate (derived from the two published rates, ESTIMATE). PUBLIC DOCS (Correo del Sur 26 Jun 2026; ABI; Diario Financiero; La Razón 29 Jun 2026; Infobae 27 Jun 2026).
* Unbanked share 2025: NOT FOUND (ASFI 2019 cited 93% population coverage of financial services; Asoban Oct 2025 reports deposit accounts up by more than 1.5M). 

### Approval rates
* No Bolivia-specific figure. EBANX itself lists no card method for Bolivia; dLocal processes Visa and Mastercard credit and debit locally. Use regional ranges and state that a cross-border USD card charge in Bolivia also meets the $500 monthly debit limit. PUBLIC DOCS.

### Tax and withholding reality: cross-border MoR vs local entity
* IVA 13% nominal (14.94% effective on invoices); IT 3% on gross income; IUE-BE: remittances abroad for services or profits bear an effective 12.5% withholding (25% on a presumed 50% net income). PUBLIC DOCS (AGN 2026 tax card). A bill to apply 13% IVA to digital services from abroad (PL 164) was debated; current status NOT FOUND. OPEN, owner German.
* Documents: PagosNet refunds need a carnet de identidad and Bolivian bank data (EBANX). PUBLIC DOCS.
* Launch time: MoR weeks (dLocal cards, QR, cash live; EBANX cash only). Local entity: SEPREC registration, NIT at SIN, bank account; legal representative required for foreign companies; day counts for companies NOT FOUND (SEPREC quotes under 24 hours for sole proprietorships only). PUBLIC DOCS.

### Method priority for a gaming top-up shop
| Priority | Method | Why | Carried through Yuno by (Yuno integrations directory, Oct 2026) |
|---|---|---|---|
| Must-have | QR (interoperable, BCB) | 36% of payments and rising, instant | dLocal (QR Payments per its docs; directory lists dLocal Multipago and Pago al Paso); OPEN, owner German: confirm QR is enabled on Yuno's dLocal Bolivia connection |
| Must-have | Visa and Mastercard credit and debit (local) | Only local acquiring avoids the $500 debit limit and FX | dLocal; also AstroPay, Cybersource, Ecommpay, Inswitch, Nuvei listed; EBANX listed in the directory but not in EBANX docs (OPEN) |
| Optional | Cash vouchers: Pago al Paso, Multipago, PagosNet | Cash still 64% of payments but slow confirmation | dLocal (Pago al Paso, Multipago), EBANX (PagosNet) |
| Optional | Google Pay, PayPal | Wallets | Listed for Bolivia |

SO WHAT: Bolivia is the clearest case for the second MoR: EBANX direct means cash vouchers only; dLocal through Yuno adds cards and QR on day one. TO VALIDATE: QR on the dLocal connection; Bolivia pay-in coverage item in CONTEXT.md.
