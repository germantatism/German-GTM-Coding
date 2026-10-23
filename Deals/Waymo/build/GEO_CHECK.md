# Waymo connections deck · geography check (23 Oct 2026)

German: every connection shown under a country must exist, be real and be operating there (through Yuno or through any other route). Three verification passes on 23 Oct 2026 checked every provider and method listed in two or more countries against the operator's own coverage pages (WebFetch), plus a manual scan of the single-country names. Rule applied: remove the pair when the operator's own site names its markets and the country is not among them, or when nothing confirms the country; keep when the operator confirms it or states global coverage.

## Removed from the deck (96 country pairs, `lib.GEO_EXCLUDE`)

- **Argentina**: emerchantpay (no Argentina payment method pages on emerchantpay.com (unsure, removed)); Transfero (transfero.com names Brazil, Mexico, US, EU, China only)
- **Bahrain**: Tabby (2025 and 2026 profiles list KSA, UAE, Kuwait only (unsure, removed)); Triple-A (no licence or coverage mention; UAE is the only GCC market with regulatory status (unsure, removed)); Pockyt (not a Pockyt checkout consumer region); Ecommpay (not named in Ecommpay payment method coverage (unsure, removed))
- **Brazil**: Safeway (code repo only, no company identified (removed))
- **Canada**: Kushki (kushkipagos.com: operates in MX, CO, CL, PE, EC only); Simpaisa (Canadian flag without a product; acquiring is 5 frontier markets (unsure, removed)); Novalnet (no Canada office or pricing market (unsure, removed))
- **Chile**: Transfero (transfero.com names Brazil, Mexico, US, EU, China only); Wibond (wibond.co mentions Argentina only (unsure, removed)); Payzen (Lyra: Chile only in a contact dropdown (unsure, removed)); Pockyt (not a Pockyt checkout consumer region); Worldpay (LatAm domestic acquiring names AR, BR, MX, CO only (unsure, removed))
- **Colombia**: Transfero (transfero.com names Brazil, Mexico, US, EU, China only); More Payments (morepaymentevolution.com does not name Colombia (unsure, removed)); Belvo (belvo.com payments: Mexico and Brazil only)
- **Costa Rica**: PuntoXpress (puntoxpress.com selector: El Salvador and Nicaragua only)
- **Ecuador**: More Payments (morepaymentevolution.com does not name Ecuador (unsure, removed))
- **Egypt**: Tabby (Tabby paused Egypt operations in 2023, no relaunch); Triple-A (no Egypt mention on own pages (unsure, removed)); Pockyt (not a Pockyt checkout consumer region); Ecommpay (not named in Ecommpay payment method coverage (unsure, removed)); Fiserv (not in Fiserv's country selector (unsure, removed))
- **El Salvador**: Ibex (bitcoin Lightning processor, no country list (unsure, removed))
- **Germany**: Getnet (not in Getnet's current presence list (unsure, removed)); PayPlug (France-focused, Germany never named (unsure, removed))
- **Guatemala**: Ibex (bitcoin Lightning processor, no country list (unsure, removed))
- **India**: Neteller (Neteller no longer accepts registrations from India); Getnet (not in Getnet's presence list (Chennai is a tech hub)); 2C2P (2C2P markets: ID, MY, PH, SG, TH, VN only); Ecommpay (not named in Ecommpay payment method coverage (unsure, removed))
- **Japan**: Click to Pay (Mastercard's 65-country Click to Pay list excludes Japan (unsure, removed)); Fiserv (not in Fiserv's country selector (unsure, removed))
- **Jordan**: Paymob (Jordan dropped from Paymob's 2025 market list (unsure, removed)); Pagsmile (Pagsmile docs: Jordan is a payout destination only); Pockyt (not a Pockyt checkout consumer region); Ecommpay (not named in Ecommpay payment method coverage (unsure, removed)); Checkout.com (only in global card lists, no local method, licence or office (unsure, removed))
- **Kuwait**: HyperPay (hyperpay.com lists 9 countries, Kuwait not among them); NBK EG Wallet (NBK Egypt product; NBK Kuwait uses NBK Mobile Banking); Triple-A (no Kuwait mention on own pages (unsure, removed)); Pockyt (not a Pockyt checkout consumer region); Ecommpay (not named in Ecommpay payment method coverage (unsure, removed))
- **Malaysia**: DANA (Indonesian wallet; cross-border use not confirmed (unsure, removed))
- **Mexico**: PlacetoPay (no PlacetoPay gateway in Mexico on Evertec or docs (unsure, removed)); Payments Way (paymentsway.co: Colombia only); Wibond (no Mexico mention, no wibond.mx (unsure, removed)); Druo (only a locale page, no Mexico coverage claim (unsure, removed)); Tpaga (no Mexico mention; tpaga.mx does not resolve (unsure, removed)); Payzen (Lyra: Mexico only in a contact dropdown (unsure, removed)); Datransfer (no such company found (removed)); Nium (Mexico licence not held yet (unsure, removed))
- **New Zealand**: Pockyt (not a Pockyt checkout consumer region)
- **Oman**: Pockyt (not a Pockyt checkout consumer region); Ecommpay (not named in Ecommpay payment method coverage (unsure, removed))
- **Peru**: Payments Way (paymentsway.co: Colombia only); RappiBank (Peru absent from rappipay.com selector; rappipay.pe empty); Druo (only a locale page, no Peru coverage claim (unsure, removed))
- **Philippines**: Panda blue (Asia deposit list excludes the Philippines); Directa 24 (Asia deposit list excludes the Philippines)
- **Qatar**: QNB Al-Ahli E-Wallet (QNB Al Ahli is the Egyptian subsidiary; wallet is an Egypt product); Tamara (tamara.co country selector: KSA, UAE, Kuwait, Bahrain only); Triple-A (no Qatar mention on own pages (unsure, removed)); Pockyt (not a Pockyt checkout consumer region); Ecommpay (not named in Ecommpay payment method coverage (unsure, removed)); Novalnet (only a generic Middle East region (unsure, removed))
- **Saudi Arabia**: Triple-A (no Saudi mention on own pages (unsure, removed)); Pockyt (not a Pockyt checkout consumer region); Ecommpay (not named in Ecommpay payment method coverage (unsure, removed)); Novalnet (only a generic Middle East region (unsure, removed))
- **Singapore**: DANA (Indonesian wallet; cross-border use not confirmed (unsure, removed))
- **South Korea**: Google Pay (not in Google's pay online or in apps country list); Stripe (South Korea is not a Stripe supported country); NTT DATA (NTT DATA Payment Services covers IN, JP, MY, PH, TH only); 2C2P (2C2P markets: ID, MY, PH, SG, TH, VN only)
- **Spain**: Commerce Gate (Bank of Spain licence only; markets are Latin American (unsure, removed)); PagSeguro (PagSeguro International covers Latin America only); PayPlug (no Spanish site (unsure, removed))
- **Taiwan**: NTT DATA (NTT DATA Payment Services covers IN, JP, MY, PH, TH only); Fiserv (not in Fiserv's country selector (unsure, removed)); Worldpay (APAC acquiring list excludes Taiwan (unsure, removed))
- **Thailand**: DANA (Indonesian wallet; cross-border use not confirmed (unsure, removed)); Nium (not named on Nium licence pages (unsure, removed))
- **United Arab Emirates**: DPO Africa (dpogroup.com country pages are African only); Bank Dhofar (Omani bank, no UAE presence found (unsure, removed)); Getnet (not in Getnet's presence list (Dubai is a tech hub)); Novalnet (only a generic Middle East region (unsure, removed))
- **United Kingdom**: Getnet (not in Getnet's presence list); Simpaisa (Simpaisa coverage page has no UK)
- **Uruguay**: PlacetoPay (Evertec processes for banks in Uruguay, no PlacetoPay gateway reference (unsure, removed)); Payzen (Lyra: Uruguay only in a contact dropdown (unsure, removed))
- **Venezuela**: Pockyt (not a Pockyt checkout consumer region); Ecommpay (not named in Ecommpay payment method coverage (unsure, removed))
- **Vietnam**: More Payments (not acquiring; at most a remittance corridor (unsure, removed))

## Kept with a note

- Carry1st / Pay1st in the Gulf and Jordan: carry1st.com names only six African markets, but Yuno's partnership covers Pay1st merchant-of-record in the GCC (German's own account); kept.
- Network International in Kuwait, Oman and Bahrain: network.ae blocks automated reads; UAE, Jordan and Saudi confirmed; the other three kept as a regional acquirer.
- AstroPay in Bolivia, Costa Rica, India, Indonesia, Japan, Mexico and Venezuela: AstroPay's business site lists a shorter region list; the wallet is sold cross-border; kept.
- Stripe and Braintree in Israel: shown in the cross-border tier (Israeli cards processed for a foreign merchant), not as local acquirers; kept. Stripe removed from South Korea, where it was shown as live.
- PayU in Latin America: PayU GPO LatAm now belongs to Rapyd (2025); processing continues, brand may read Rapyd.
- Facilitapay now trades as Attrus (Brazil, Mexico, Colombia active). STC Pay now operates as stc bank.
- WeChat Pay, UnionPay, Discover, UATP, Western Union, Neteller (except India), Cybersource: global coverage statements on the operators' sites; no per-country list published.
- ShopeePay in Thailand, the Philippines, Singapore and Taiwan: own sites render as JavaScript only; Shopee operates the wallet in all four; kept.
- payabl. in Spain and Paysera in the UK: EU-passported EMIs that do not name countries; kept. Boku in Singapore: carrier billing coverage not itemised; kept.
- PlacetoPay: Evertec processes for banks in Uruguay and has no gateway reference for Mexico; both removed as unconfirmed.

## Still open

- DANA outside Indonesia and Click to Pay in Japan were removed as unconfirmed; if Yuno's directory owners confirm them, add them back by deleting the pairs from `GEO_EXCLUDE`.
- Payamigo (Brazil, code tier): a Miami cross-border PSP for emerging markets; Brazil not individually confirmed; kept because the repo exists.
