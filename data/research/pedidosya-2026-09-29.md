# SDR Research Brief: PedidosYa (for Yuno Payment Orchestrator)
*Framework v8.0, 4 agents, accuracy-first. Research date: 2026-09-29*

> ⚠️ **OWNERSHIP CHANGE IN PROGRESS.** On 2026-07-16 Uber signed a business combination agreement to acquire Delivery Hero (PedidosYa's parent) at EUR 41.50 per share in cash. Closing is expected in the second half of 2027 and is NOT complete. PedidosYa gets split: Uber takes 13 markets (Argentina, Bolivia, Costa Rica, Dominican Republic, El Salvador, Guatemala, Honduras, Nicaragua, Panama, Paraguay, Peru, Uruguay, Venezuela) and SSW Partners takes PedidosYa Chile and Ecuador. Verified directly on the SEC exhibit: https://www.sec.gov/Archives/edgar/data/1543151/000155278126000382/e26302_ex99-1.htm
>
> ⚠️ **ORCHESTRATOR ALREADY PUBLISHED.** PedidosYa is a published Spreedly customer (vault plus routing to multiple providers). The only datable evidence is from October 2018 and the named sponsor (Mathias Fonseca) has left the company. Do not pitch "you have no orchestration". Source: https://www.spreedly.com/customers/pedidosya
>
> ⚠️ **RESEARCH LIMITS.** PedidosYa sites return HTTP 403 to automated requests and checkout sits behind login. Reddit and X were unreachable. No live checkout or source code inspection was possible. Everything on payment methods comes from official T&Cs, official promo terms, official help centers and dated press. "Not verified" never means "not available".

---

## EXECUTIVE SUMMARY

PedidosYa is Delivery Hero's Latin American delivery and quick-commerce platform (HQ Montevideo): 15 countries, 19M+ users, about 1 million average daily orders in Q4 2025, and an Americas segment GMV of EUR 4,079.6M in FY 2025 that accelerated to +29.4% in H1 2026. The payment stack is multi-provider and fragmented by market: Spreedly is published as the vault and routing layer (evidence dated 2018), Cybersource Decision Manager covers fraud (2021), Chile runs debit through Klap and Webpay, dLocal appears as the biller behind PedidosYa collection flows in Paraguay and El Salvador, and each market has added its own local method one at a time (Yape, QR in Bolivia, Deuna, Tigo Money, Yappy, MACH, Pago Móvil). The Yuno opportunity is to move from a vault-centric setup to active orchestration (routing, failover, monitoring, local methods, refunds, reconciliation) at the moment the business is being split between Uber and SSW Partners, which forces the stack to become portable across owners. Public complaint data (3,417 SERNAC complaints in Chile in 2024 with refunds as the top reason, plus repeated "charged but order not created" and double-charge reports) supplies the operational pain to anchor the conversation.

---

## SECTION 1: Traffic by Country

PedidosYa is app-first and runs one domain per country, so no single Similarweb page shows the country mix. The table below consolidates the 14 domains measured (Similarweb, data month August 2026).

**[ESTIMATE] Country totals are derived by this brief**: visits per domain multiplied by that domain's country share, then summed. They are web visits only and must not be read as order share.

| Rank | Country | Traffic Share (%) [ESTIMATE] | Est. Monthly Visits [ESTIMATE] | Trend (own domain, MoM) | Source URL |
|---|---|---|---|---|---|
| 1 | Argentina | 42.4% | 3.59M | pedidosya.com.ar -1.7% | https://www.similarweb.com/website/pedidosya.com/ ; https://www.similarweb.com/website/pedidosya.com.ar/ |
| 2 | Chile | 10.1% | 0.85M | pedidosya.cl -13.72% | https://www.similarweb.com/website/pedidosya.cl/ |
| 3 | Panama | 6.7% | 0.57M | +1,019% (anomalous spike, treat with caution) | https://www.similarweb.com/website/pedidosya.com.pa/ |
| 4 | Ecuador | 6.4% | 0.54M | +1.77% | https://www.similarweb.com/website/pedidosya.com.ec/ |
| 5 | Peru | 5.3% | 0.44M | +7.06% | https://www.similarweb.com/website/pedidosya.com.pe/ |
| 6 | Dominican Republic | 4.6% | 0.39M | +9.94% | https://www.similarweb.com/website/pedidosya.com.do/ |
| 7 | Uruguay | 3.8% | 0.32M | +30.58% | https://www.similarweb.com/website/pedidosya.com.uy/ |
| 8 | Guatemala | 3.0% | 0.25M | -12.6% | https://www.similarweb.com/website/pedidosya.com.gt/ |
| 9 | Paraguay | 2.5% | 0.21M | -31.03% | https://www.similarweb.com/website/pedidosya.com.py/ |
| 10 | Bolivia | 1.5% | 0.13M | -20.27% | https://www.similarweb.com/website/pedidosya.com.bo/ |
| 11 | Costa Rica | 0.7% | 0.06M | +85.05% | https://www.similarweb.com/website/pedidosya.cr/ |
| 12 | Venezuela | 0.7% | 0.06M | +351.4% (anomalous) | https://www.similarweb.com/website/pedidosya.com.ve/ |
| 13 | Honduras | 0.6% | 0.05M | -4.82% | https://www.similarweb.com/website/pedidosya.com.hn/ |
| N/A | Unattributed (US, Brazil, others) | 11.7% | 0.99M | N/A | same pages |

Total across the 14 domains measured: about 8.46M visits. The main domain pedidosya.com shows 3.2M (-9.69% MoM) with Argentina 59.58%, Chile 9.78%, Dominican Republic 7.69%, Peru 5.21%, Paraguay 3.63%.

**Caveats**
- Similarweb's free page labels the chart "Total Visits Last 3 Months"; it could not be settled whether the figure is monthly or a 3 month sum. Semrush shows 1.53M for pedidosya.com.ar in August 2026, close to Similarweb's 1.8M, which suggests monthly. [INFERENCE, not confirmed] https://www.semrush.com/website/pedidosya.com.ar/overview/
- El Salvador and Nicaragua run on pedidosyasv.com.sv and pedidosyani.com.ni. Traffic for both: Not found.
- Mobile is 79.57% of pedidosya.com.ar visits (Semrush). Web is a small fraction of total activity.

**App and volume metrics (not web traffic)**
| Metric | Value | Date | Source URL |
|---|---|---|---|
| Users | "más de 19 millones de usuarios en 15 países y más de 500 ciudades" | 2026-01-05 | https://www.prnewswire.com/mx/comunicados-de-prensa/pedidosya-foodie-radar-2025-el-mapa-del-sabor-en-latam-302652661.html |
| Average daily orders, Americas segment | 1 million (orders +24% YoY) | Q4 2025 | https://www.tradingview.com/news/eqs:81958b162094b:0-delivery-hero-reports-strong-q4-while-business-transforms-into-everyday-app/ |
| LatAm app active users | about 11M at end of June 2025 (weekly vs monthly basis not explicit); #2 by downloads behind iFood | Q2 2025 | https://sensortower.com/blog/2025-q2-unified-top-5-food%20delivery%20services-units-latin_am-63da96fbe1714cfff1c1e5a1 |
| Google Play | 4.7 stars, 2.24M reviews, 50M+ downloads | 2026-09-28 | https://play.google.com/store/apps/details?id=com.pedidosya&hl=es_419&gl=AR |
| Volume leaders | Argentina, Chile and Uruguay lead in volume (COO Juan Martín López) | 2026-01-02 | https://www.df.cl/america/mas-supermercados-digitales-e-impulso-a-la-vertical-fintech-la-formula |

**Flags**
- 🚩 Markets above 5% of web traffic: Argentina, Chile, Panama (spike), Ecuador, Peru.
- 🚩 100% LATAM footprint. No APAC or MENA exposure at the PedidosYa level.
- 🚩 Two of the top five web markets (Chile and Ecuador) are the two being carved out to SSW Partners.
- Top 10 countries without a local entity: none (see Section 2).

---

## SECTION 2: Legal Entities

Entity named in each country's Terms and Conditions (15 of 15 found).

| Country | In Top 10 Traffic? | Has Local Entity? | Cross-Border Risk? | Source URL |
|---|---|---|---|---|
| Argentina | Yes (#1) | Yes: Delivery Hero E-Commerce S.A. (CUIT 30-71198576-6). Fintech entity: Delivery Hero Financial Services S.A. (formerly Pagos Ya S.A.) | Low | https://www.pedidosya.com.ar/about/terminos-condiciones ; https://www.indicadores.ar/empresa/30715221159 |
| Chile | Yes (#2) | Yes: Delivery Hero E-Commerce Chile SpA (RUT 76.211.425-9) | Low | https://www.pedidosya.cl/about/terminos-condiciones |
| Panama | Yes (#3) | Yes: Delivery Hero Panamá (E-Commerce) S.A. | Low | https://www.pedidosya.com.pa/about/terminos-condiciones |
| Ecuador | Yes (#4) | Yes: Delivery Hero (DH E-Commerce) Ecuador S.A.S (RUC 1792512433001) | ⚠️ See note on "international card" wording | https://www.pedidosya.com.ec/about/terminos-condiciones |
| Peru | Yes (#5) | Yes: Delivery Hero Peru S.A.C. (RUC 20551348041) | Low | https://www.pedidosya.com.pe/about/terminos-condiciones |
| Dominican Republic | Yes (#6) | Yes: Delivery Hero República Dominicana, S.R.L. (RNC 131194281) | Low | https://www.pedidosya.com.do/about/terminos-condiciones |
| Uruguay | Yes (#7) | Yes: Delivery Hero Uruguay Marketplace S.A. and Delivery Hero Payments Uruguay S.A. | Low | https://www.pedidosya.com.uy/about/terminos-condiciones |
| Guatemala | Yes (#8) | Yes: T&C names Glovoapp Guatemala S.A.; Delivery Hero's shareholding list names Delivery Hero Guatemala S.A. | Low | https://www.pedidosya.com.gt/about/terminos-condiciones |
| Paraguay | Yes (#9) | Yes: Delivery Hero Pedidos Ya Paraguay S.A. (RUC 80090560-1) | Low | https://www.pedidosya.com.py/about/terminos-condiciones |
| Bolivia | Yes (#10) | Yes: PedidosYa Servicios S.A. (NIT 358245025) | Low | https://www.pedidosya.com.bo/about/terminos-condiciones |
| Costa Rica | No | Yes: Delivery Hero Costa Rica Limitada | ⚠️ See note | https://www.pedidosya.cr/about/terminos-condiciones |
| Venezuela | No | Branch only: Delivery Hero Panamá, S.A., Sucursal Venezuela (RIF J-50039513-2). No standalone Venezuelan company in Delivery Hero's shareholding list | ⚠️ Branch of a Panama entity, see note | https://www.pedidosya.com.ve/about/terminos-condiciones |
| Honduras | No | Yes: Delivery Hero Honduras S.A | ⚠️ See note | https://www.pedidosya.com.hn/about/terminos-condiciones |
| El Salvador | Not measured | Yes: Delivery Hero El Salvador, S.A. de C.V. | Low | https://www.pedidosyasv.com.sv/about/terminos-condiciones |
| Nicaragua | Not measured | Yes: Delivery Hero Nicaragua S.A. | Not verified | https://www.pedidosyani.com.ni/about/terminos-condiciones |

Full subsidiary list (all at 100%): Delivery Hero SE Annual Financial Statements 2025, Annex I. https://ir.deliveryhero.com/media/document/d7cd8a32-bb5e-48d0-a416-c38f9cad59e0/assets/DeliveryHeroSE_Annual_Financial.pdf?disposition=inline

**⚠️ Note on "international card" wording (verified verbatim in the T&C text).** The T&Cs of Ecuador, Venezuela, Costa Rica and Honduras say that to pay online the user "deberá cargar una tarjeta de crédito o débito internacional". Guatemala says "local y/o internacional". Argentina, Chile, Uruguay, Peru, Bolivia, Paraguay and Dominican Republic do not carry that wording. [INFERENCE, not confirmed] In those four markets online card payments may be acquired cross-border, which usually means lower approval and higher cost than local acquiring. These T&Cs are dated 28/11/2023 and may be outdated.

> ⚠️ MANUAL: Verify on official T&Cs and with a live card test in Ecuador and Costa Rica before using the cross-border angle.

**Exits and history**
- Brazil exit: iFood acquired PedidosJá in 2018. https://lexlatin.com/noticias/ifoodcom-adquiere-empresa-brasilena-de-delivery-pedidos-ja
- Colombia exit (2015 swap with Domicilios.com). Peru re-entry in 2021 after acquiring Glovo's LatAm operations in 2020. https://forbes.co/2021/06/25/emprendedores/la-emotiva-historia-de-domicilios-com-la-plataforma-de-delivery-que-deja-de-existir ; https://en.wikipedia.org/wiki/PedidosYa

---

## SECTION 3: Payment Stack

### 3A. PSPs, Acquirers and Payment Vendors

**PedidosYa-specific evidence**

| Country/Region | PSP / Acquirer / Vendor | Role | Evidence Type | Source URL |
|---|---|---|---|---|
| Regional | Spreedly | Card vault and tokenization, routing to multiple providers through one integration | [Case Study] undated; podcast dated 2018-10-16 | https://www.spreedly.com/customers/pedidosya |
| Regional | 10 or 11 providers "depending on the country" (none named) | Processing | [Case Study] vendor podcast, 2018-10-16 | https://www.spreedly.com/blog/payments-dialog-episode-2-payments-and-delivery-in-latin-america-with-mathias-fonseca |
| Regional | Cybersource Decision Manager (Visa) | Fraud prevention, in use "durante los últimos tres años" as of Oct 2021 | [Press Release] 2021-10-08 | https://www.montevideo.com.uy/Negocios-y-Tendencias/PedidosYa-y-Visa-firman-alianza-estrategica-regional-para-impulsar-el-Quick-Commerce-uc800543 |
| Regional | Cybersource payment gateway and Visa Direct | Stated intent in 2021 to process in all markets "a través de una sola conexión" and to run real-time payouts. Rollout not confirmed | [Press Release] 2021-10-08 | same URL |
| Chile | Klap | Debit cards ("tarjeta de débito vía Klap") | [Checkout] official T&C | https://www.pedidosya.cl/about/terminos-condiciones |
| Chile | Webpay | Debit cards ("tarjeta de débito vía Webpay") | [Checkout] official T&C | https://www.pedidosya.cl/about/terminos-condiciones |
| Paraguay | dLocal | "PEDIDOS YA" is listed as a biller under "Dlocal Service" on Bancard's Infonet payment portal. Flow type (consumer, rider or merchant collection) not stated | [Third-party biller listing] | https://www.infonet.com.py/servicios_disponibles/Dlocal%20Service |
| El Salvador | dLocal | Biller named "Pedidosya - Dlocal" in a bill payment catalogue. Flow type not stated | [Third-party biller listing] | https://www.bitrefill.com/sv/es/factura/pedidosya-dlocal-bill-el-salvador/ |
| Argentina, merchant side | Wibond S.A.S. | BCRA-registered payment service provider behind the virtual accounts of PeYa Wallet. PedidosYa's fintech entity states it "no ofrece cuentas virtuales ni servicios de pagos por sí misma" | [Checkout] official partner T&C | https://www.pedidosya.com.ar/about/api/policy?countryName=es-AR&policyType=advance-payouts-tyc-contract&version=latest |
| Argentina and Chile, riders | Pago46 | Cash remittance from riders (Socio46, Pago Fácil, ProvinciaNet in Argentina) | [Official help center] | https://riders.repartosya.com.ar/categorias/pagos.html ; https://riders.repartosya.cl/categorias/pagos.html |
| Uruguay | Delivery Hero Payments Uruguay S.A. | In-house entity, "prestador de servicios de pago y cobranzas" | [Checkout] official partner T&C | https://www.pedidosya.com.uy/about/api/policy?countryName=es-UY&policyType=advance-payouts-tyc-contract&version=latest |
| Regional, back office | Simetrik, SAP | Reconciliation with "adquirentes, gateways y bancos", chargebacks and refunds | [Job Listing] expired | https://empleos.pedidosya.com/job/reconciliation-sr-analyst-in-buenos-aires-argentina-jid-1456 |
| Panama, Chile | Acquirer unnamed | Partner T&Cs refer to "el adquirente de los medios de pago" without naming it | [Checkout] official T&C | https://www.pedidosya.com.pa/about/terminos-condiciones |

**Delivery Hero group evidence (not PedidosYa-specific)**

| Region | Vendor | What it shows | Evidence Type | Source URL |
|---|---|---|---|---|
| MENA | Checkout.com | Partnership "primarily focused in the Middle East and North Africa"; PedidosYa named only as a group brand; "400+ payment professionals" | [Case Study] 2023-07-25 | https://www.checkout.com/case-studies/how-localized-payments-is-driving-delivery-hero-s-global-expansion |
| Asia | Antom (Ant International) | Partner since 2019; PedidosYa not mentioned | [Case Study] | https://knowledge.antom.com/delivery-hero-antom-shaping-tomorrows-digital-platform-payments |
| Multi-region incl. LatAm | IXOPAY | Rider cash collection into a digital wallet | [Case Study] 2019-10-21 | https://www.ixopay.com/case-studies/delivery-hero-chooses-ixopay-to-streamline-the-cash-collection-process |
| Group | trimplement CoreWallet | Built the multi-country wallet platform | [Case Study] | https://trimplement.com/case-studies/delivery-hero |
| DE, AT, AU | Adyen | 2016 article; mentions plans for South America; PedidosYa not named | [Case Study] 2016-06-01 | https://www.adyen.com/knowledge-hub/delivery-hero-tucks-into-risk-management |

**Not found for PedidosYa:** Stripe, Adyen, Worldpay, Braintree, Kushki, Bamboo Payment, Fiserv, Payway, Mercado Pago as processor. No public information found.

### 3B. Orchestrator

- **Confirmed (published): Spreedly.** Vault plus "payment method distribution" to multiple providers. https://www.spreedly.com/customers/pedidosya
- Currency of the relationship is NOT confirmed. The case study is undated, the podcast is from 2018, and the sponsor moved to Delivery Hero in 2019 and later to Payrails.
- [INFERENCE, not confirmed] PedidosYa also runs an internally built gateway layer: job listings reference a "Payments Tribe", a "Payment Gateway team" and "Payment Services" microservices. https://freehire.me/companies/pedidosya
- Delivery Hero group has an in-house "Payment Orchestration domain, within Payments Tribe" (Berlin job listing, expired). https://careers.deliveryhero.com/job/product-manager-fintech-payments-in-berlin-germany-jid-8182
- Payrails was founded by the people who built Delivery Hero's in-house payment system across 50+ markets. The article does not say Delivery Hero is a Payrails customer. https://techcrunch.com/2022/03/17/payrails-emerges-from-stealth-with-6-4m-led-by-a16z-to-build-the-os-for-payments
- No public evidence found for Primer, Gr4vy, CellPoint Digital, APEXX or Yuno at PedidosYa or Delivery Hero.

> ⚠️ MANUAL, DevTools: test card 4111 1111 1111 1111 | 02/30 | 123. Priority checks: (1) is the tokenization call still going to Spreedly, (2) which processor domains appear in Argentina, Chile and Peru, (3) 3DS behavior.

---

## SECTION 4: APMs (Agent D findings)

Every general T&C says methods "dependen de cada Oferente" and lists online methods "a modo de ejemplo". The lists are illustrative, not exhaustive.

### 4A. Confirmed APMs

| Market | APMs Confirmed | Verification Source | Source URL |
|---|---|---|---|
| Argentina | Cash on delivery; POS on delivery; online credit and debit cards; coupons; "billetera virtual"; PedidosYa wallet balance. Card brands confirmed through official promos: American Express, Naranja X | Official T&C (06/12/2024), wallet T&C, promo terms | https://www.pedidosya.com.ar/about/terminos-condiciones ; https://terms.pedidosya.com/promociones-argentina/ ; https://terms.pedidosya.com/30-off-pagando-con-naranjax/ |
| Chile | Cash; credit card; debit via Klap; debit via Webpay; prepaid card; coupons; wallet PedidosYa Pagos / PedidosYa Pay; MACHBANK app button; MACH, SBPay Visa and Copec Pay cards | Official T&C (14/08/2024), official promo terms (Sept 2026), MACHBANK partner page | https://www.pedidosya.cl/about/terminos-condiciones ; https://www.machbank.cl/alianzas-y-conexiones/pedidosya ; https://terms.pedidosya.com/bases-usuarios-tarjeta-virtual-machbank-septiembre-2026/ |
| Uruguay | Cash (not after 19:00 since May 2026); credit and debit cards; coupons; POS on delivery; Santander, Amex Scotiabank, Cabal and Prex cards; Pluxee Alimentación card (third-party source) | Official T&C (Aug 2024), promo terms, Pluxee blog (2026-04-22) | https://www.pedidosya.com.uy/about/terminos-condiciones ; https://terms.pedidosya.com/20-off-pagando-con-tarjetas-cabal/ ; https://www.pluxee.uy/blog/pedidos-ya-uruguay-pluxee-alimentacion/ |
| Peru | Cash and POS on delivery; credit and debit cards; coupons; "billetera virtual"; Yape as an in-app payment method; Banco Falabella and CMR cards | Official T&C (19/03/2026), official promo terms (2026-06-11) | https://www.pedidosya.com.pe/about/terminos-condiciones ; https://terms.pedidosya.com/terminos-y-condiciones-del-sorteo-afilia-yape-en-pedidosya/ |
| Bolivia | Cash; credit and debit cards; coupons; QR payments (refunds for QR go exclusively to the wallet). QR scheme not specified | Official T&C, wallet T&C (24/09/2024), press (2024-12-06) | https://www.pedidosya.com.bo/about/terminos-condiciones ; https://www.aygun.com.bo/pedidosya-lanza-el-pago-con-qr-en-bolivia-y-marca-tendencia-en-la-region/ |
| Paraguay | Cash; credit, debit and prepaid cards; coupons; Banco Itaú Visa cards; Tigo Money (press 2022, dated) | Official T&C, promo terms, press | https://www.pedidosya.com.py/about/terminos-condiciones ; https://www.ultimahora.com/pedidosya-amplia-sus-medios-pago-n3040851 |
| Ecuador | Cash and POS on delivery; "international" credit or debit card; coupons; wallet; Deuna (launched 2026-08-12, redirect to the Deuna app) | Official T&C (28/11/2023), press citing PedidosYa (2026-09-15) | https://www.pedidosya.com.ec/about/terminos-condiciones ; https://www.ondata.com.ec/pedidosya-pagos-deuna-ecuador/ |
| Dominican Republic | Cash; credit and debit cards; coupons; PedidosYa Pay wallet; vouchers; any Visa card (promo) | Official T&C (08/01/2024), promo terms | https://www.pedidosya.com.do/about/terminos-condiciones |
| Venezuela | POS and cash on delivery; Pago Móvil to the rider; "international" card online; national Mastercard in bolívares and Bancamiga cards (promo); Zelle (press 2022, dated) | Official T&C, promo terms (Jun 2026) | https://www.pedidosya.com.ve/about/terminos-condiciones ; https://terms.pedidosya.com/terminos-y-condiciones-10-off-mastercard-junio-2026/ |
| Panama | POS and cash on delivery; credit and debit cards; coupons; Davivienda, Banco General Mastercard, MetroBank and Zinli prepaid cards (promo); Yappy via QR (press 2023) | Official T&C static copy, promo terms (2026), press | https://terms.pystatic.com/about/generales/tyc_generales_panama.html ; https://terms.pedidosya.com/terminos-y-condiciones-promociones-bancarias-agosto-2026/ ; https://dplnews.com/panama-pedidosya-integra-yappy-como-metodo-de-pago-en-la-entrega/ |
| Costa Rica | POS and cash on delivery; "international" credit or debit card; coupons; BN Gamecard Mastercard debit (promo) | Official T&C, promo terms (Sept 2026) | https://www.pedidosya.cr/about/terminos-condiciones |
| Guatemala | POS (datáfono) and cash on delivery; "local y/o internacional" cards; coupons | Official T&C | https://www.pedidosya.com.gt/about/terminos-condiciones |
| Honduras | POS and cash on delivery; "international" credit or debit card; coupons; BAC Amex cards (promo) | Official T&C, promo terms | https://www.pedidosya.com.hn/about/terminos-condiciones ; https://terms.pedidosya.com/promocion-bac-amex/ |
| El Salvador | Cash on delivery; credit and debit cards; coupons; co-branded Visa credit card with Banco Cuscatlán (2025) | Official T&C (22/01/2025), press | https://www.pedidosyasv.com.sv/about/terminos-condiciones ; https://diario.elmundo.sv/empresarial/banco-cuscatlan-visa-y-pedidosya-lanzaron-innovadora-tarjeta-de-credito-con-beneficios-para-el-delivery-y-el-ahorro |
| Nicaragua | BAC (Mastercard, Visa, American Express, Diners Club), Ficohsa and Banpro cards | Official promo terms only | https://terms.pedidosya.com/hasta-15off-con-bac-en-semana-santa/ |

**Merchant and rider side (official pages)**
| Flow | Finding | Source URL |
|---|---|---|
| Merchant settlement, Argentina | PedidosYa's fintech entity collects card and online payments on behalf of the merchant; weekly settlement; optional instant payout ("Liquidación Inmediata") with a fee; chargebacks deducted; optional virtual account with CVU through Wibond | https://www.pedidosya.com.ar/about/api/policy?countryName=es-AR&policyType=advance-payouts-tyc-contract&version=latest |
| PeYa POS, Argentina | "Aceptamos tarjetas de débito y crédito Visa y Mastercard"; POS sales settle into PeYa Wallet | https://www.pedidosya.com.ar/about/api/policy?countryName=es-AR&policyType=pos-guide&version=latest |
| PeYa Wallet, Argentina | Weekly payouts, yield on balance, transfers, free prepaid Visa card, QR payments enabled (Sept 2026 release) | https://apps.apple.com/ar/app/peya-wallet/id6783501507 |
| Rider payouts, Argentina and Chile | Weekly bank deposit on Thursdays; cash collected offsets earnings; cash debt remitted through Pago46 | https://riders.repartosya.com.ar/categorias/pagos.html |

### 4B. Unverified Markets and Methods

| Market | Verification Attempted? | Reason Not Verified | Popular Local APMs (market context only, NOT a PedidosYa gap) |
|---|---|---|---|
| All markets: live checkout screen | Yes | Login wall plus bot challenge (HTTP 403) | N/A |
| All markets: Apple Pay, Google Pay | Yes | No fetched page names them | N/A |
| All markets: installments, bank transfer at checkout, gift cards | Yes | No fetched page confirms them | N/A |
| Argentina: Mercado Pago, MODO, Cuenta DNI | Yes | Only search snippets and secondary blogs; partner center returned 403 | Mercado Pago, MODO, Cuenta DNI, interoperable QR |
| Argentina: newer T&C (23/03/2026) | Yes | 403 bot challenge; the version read is dated 06/12/2024 | same |
| Chile: meal vouchers | Yes | No fetched page names PedidosYa | Webpay and Redcompra, MACH, Mercado Pago, Khipu |
| Peru: Plin | Yes | No fetched page names it | Yape, Plin, PagoEfectivo |
| Costa Rica: SINPE Móvil | Partly | No fetched page names it | SINPE Móvil |
| Dominican Republic, Guatemala, Honduras: local wallets | Partly | No fetched page names local wallets | Cards and cash |
| Nicaragua: site T&Cs | Yes | 403 bot challenge; only promo terms verified | Cards and cash |

> "Not verified" ≠ "not available." MANUAL: VPN checkout walk-through before any APM claims.

---

## SECTION 5: Payment Complaints

| Issue Type | Platform | Frequency (distinct reports seen) | Date Range | Source URL |
|---|---|---|---|---|
| Official aggregate, Chile | SERNAC | 3,417 complaints against PedidosYa in 2024 (up from 1,766 in 2022). Top reason across delivery apps: difficulty obtaining refunds; list also includes unauthorized and duplicate charges and automatic tips. Favorable response rate 63% | 2022 to 2024 | https://www.sernac.cl/portal/604/w3-article-83827.html ; https://www.latercera.com/pulso-pm/noticia/aplicaciones-moviles-uber-eats-rappi-y-pedidosya-lideran-ranking-de-reclamos-al-sernac/EG7XCTPUGFGNRKG4UP5S6RUAAE/ |
| Charged but order not created, app error after paying | Trustpilot | 9 to 10 (AR, CL, PE, UY, VE) | Jul 2024 to Jul 2025 | https://es.trustpilot.com/review/pedidosya.com.ar?page=3 ; https://es.trustpilot.com/review/pedidosya.cl |
| Double charges | tuquejasuma (9, snippet only), reclamos.cl (1), Trustpilot (1) | about 11 | Jul 2024 to Feb 2025 where dated | https://www.reclamos.cl/pedidos-ya/reclamo/2024/jul/pedidos-ya-doble-cobro ; https://tuquejasuma.com/pedidos-ya/reclamos/cobro-doble-pedidos-ya-1284679 |
| Refund friction, delays, partial refunds | Trustpilot (about 13), defensadelconsumidor.com.ar (3), tuquejasuma (4), reclamos.cl (1) | about 21 (AR, CL, UY, PE, PA, GT) | Mar 2024 to Sep 2026 | https://es.trustpilot.com/review/pedidosya.com.ar ; https://www.defensadelconsumidor.com.ar/denuncias-empresa/399-pedidos-ya |
| Refund sent to wallet or coupon instead of the original card | Trustpilot (5), others | 7 recent | Jul 2024 to Aug 2026 | https://es.trustpilot.com/review/pedidosya.com.ar?page=2 |
| Card declines, online payment not working ("payment rejected but charged") | tuquejasuma (6, snippet only), others | about 9 | mostly undated | https://tuquejasuma.com/pedidos-ya/reclamos/me-sale-pago-rechazado-y-me-cobraron |
| Unauthorized charges, account takeover with saved cards | News (1), tuquejasuma (5), Trustpilot (1), App Store (1) | about 9 (AR) | Nov 2023 to Apr 2026 | https://www.rafaelanoticias.com/informacion-general/hackean-cuentas-en-aplicacion-de-delibery-de-que-se-trata-esta-modalidad-y-como-evitar-ser-una-victima.htm |
| PedidosYa Plus subscription billing (charge after cancelling) | tuquejasuma (4, snippet only), Trustpilot (1 to 2) | 5 to 6 | Dec 2024 to Apr 2026 | https://tuquejasuma.com/pedidos-ya/reclamos/cobro-indebido-de-pedidos-ya-plus-pese-a-yo-haber-dado-de-baja-mi-suscripcion |
| Pre-selected tip charged without consent | Regulators in Peru, Chile and Argentina | 4 regulatory or legal actions | Oct 2024 to Jul 2026 | https://www.infobae.com/peru/2026/07/22/pides-comida-por-delivery-probablemente-pagabas-mas-de-lo-debias-sancionan-a-pedidosya-por-incluir-propina-predeterminada-sin-consentimiento/ |

Trustpilot scores: pedidosya.com.ar 1.3 (168 reviews), pedidosya.cl 1.5 (34 reviews). Small samples that cover all complaint types, not only payments. Counts above are what was seen, not prevalence. tuquejasuma and reclamos.cl items are snippet only (pages return 403).

**Analysis: patterns linked to Yuno solutions**
1. **"Charged but no order" and "rejected but charged".** This is a state mismatch between the processor and the order system: the authorization succeeds at the bank while the app times out or errors. One Chilean customer was told there was nothing to refund "como no hay número de pedido" while the bank held an authorization code. Yuno link: unified transaction status across providers, real-time monitors, automatic reversal of orphan authorizations.
2. **Double charge after retrying with a second card.** The retry logic charges both attempts. Yuno link: orchestrated retries and failover with idempotency, so a fallback to a second provider does not create a second capture.
3. **Refund friction and refunds forced into the wallet.** Chile's T&C sends Webpay debit refunds to the wallet or to a bank transfer "dentro un plazo de 30 días hábiles"; Bolivia sends QR refunds exclusively to the wallet. Yuno link: refund orchestration per method and a single reconciliation view for refunds and chargebacks.
4. **Card testing and account takeover.** Small tickets make PedidosYa a target (stated by its own payments lead in 2018). Yuno link: fraud tools orchestrated per market and per provider on top of the existing Cybersource setup.

---

## SECTION 6: Expansion and Corporate Developments

| # | Date | Development | Category | Source URL |
|---|---|---|---|---|
| 1 | 2026-09-24 | Delivery Hero CEO Niklas Östberg stays (contract to 2029-04-30), reversing the May succession plan, citing the takeover offer | Leadership (parent) | https://www.ad-hoc-news.de/boerse/news/corporate-news/delivery-hero-stock-reports-a-ceo-leadership-reversal/70177707 |
| 2 | 2026-09-02 | Delivery Hero boards unanimously recommend accepting Uber's offer; acceptance period 2026-08-27 to 2026-11-05; competition reviews pending | M&A | https://www.techtimes.com/articles/326538/20260903/delivery-hero-boards-endorse-ubers-148b-bid-urging-shareholders-accept.htm |
| 3 | 2026-07-21 | Ecuador: Delivery Hero to provide technology and operational transition services to SSW for up to 24 months | Divestment | https://www.expreso.ec/economia-y-negocios/pedidosya-ecuador-tendra-nuevo-dueno-firma-wall-street-comprara-app-289950.html |
| 4 | 2026-07-16 | Uber signs agreement to acquire Delivery Hero: EUR 41.50 per share, equity value USD 14.8B, closing expected H2 2027. SSW Partners buys 14 markets (about USD 1.6B) including PedidosYa Chile and Ecuador | M&A | https://www.sec.gov/Archives/edgar/data/1543151/000155278126000382/e26302_ex99-1.htm |
| 5 | 2026-04 to 2026-09 | PeYa Wallet app for merchants in Argentina (weekly settlement, yield, transfers, prepaid Visa, QR payments) | Fintech | https://apps.apple.com/ar/app/peya-wallet/id6783501507 |
| 6 | 2026-04-22 | Fintech ecosystem presented to merchants: instant cash advances for merchants and riders, pre-approved credits, PeYa Wallet. Named executive: Ignacio Costa, VP Fintech | Fintech | https://www.mdzol.com/sociedad/pedidosya-reunio-mas-100-socios-mendoza-y-proyecta-el-crecimiento-del-quick-commerce-n1503763 |
| 7 | 2026-01-02 | 2026 plan: more PedidosYa Market stores (160 stores, 90+ cities, 14 countries) plus fintech push; more than USD 153M placed in credit | Quick commerce, fintech | https://www.df.cl/america/mas-supermercados-digitales-e-impulso-a-la-vertical-fintech-la-formula |
| 8 | 2025-12-09 | Delivery Hero announces a strategic review | Strategic review | https://ir.deliveryhero.com/media/document/a6007947-8b1b-416f-bb3e-6a7b798c4f75/assets/Delivery_Hero_Q1_2026_Trading_Update.pdf?disposition=inline |
| 9 | 2025-10-22 | Maximiliano Nocioni named General Director Peru | Leadership | https://www.peru-retail.com/pedidosya-anuncia-a-maximiliano-nocioni-como-su-nuevo-director-general-en-peru/ |
| 10 | 2025-09-05 | Enrique Valencia named General Manager Argentina | Leadership | https://mercado.com.ar/talento-y-liderazgo/pedidosya-designa-a-enrique-valencia-como-nuevo-gerente-general-para-su-operacion-en-argentina/ |
| 11 | 2025-07-08 | New app version; USD 87M technology investment in 2025 | Product | https://www.forbesargentina.com/negocios/pedidosya-lanza-nueva-version-su-app-inversion-us-87-millones-tecnologia-n75019 |
| 12 | 2025-06-02 | PedidosYa Plus launched in Uruguay; already live in Argentina, Chile and Peru | Subscription | https://www.elobservador.com.uy/cafe-y-negocios/el-delivery-entra-el-mundo-las-membresias-y-ahora-tambien-se-paga-mes-los-detalles-del-nuevo-modelo-suscripcion-pedidosya-n6002333 |
| 13 | 2025-03-19 | CEO Esteban Gutiérrez: 2024 was the first profitable year; fintech launch (loans, wallet, supplier payments, cards); strategy is depth in the 15 existing countries | Fintech, profitability | https://www.peru-retail.com/pedidosya-evoluciona-incursiona-en-fintech-y-expande-servicios-mas-alla-del-delivery/ |

**Payment-related job postings**
| Role | Location | What it reveals | Source URL |
|---|---|---|---|
| Software Engineer Backend, Fintech team (posted 2026-09-08) | Buenos Aires | Java, Kotlin, Go, AWS, microservices. No PSP named | https://freehire.me/jobs/software-engineer-backend-pedidosya-n235dn3t |
| Software Engineer Backend, Payment Services | Argentina | Payment microservices for the platform's payment gateway | https://freehire.me/companies/pedidosya |
| Payments Optimization Specialist, Fintech Operations (expired) | Montevideo or Buenos Aires | Monitors payments KPIs and acceptance; manages payment alarms with vendors; cards and APMs | https://empleos.pedidosya.com/job/payments-optimization-specialist-in-montevideo-uruguay-jid-977 |
| Reconciliation Sr Analyst (expired) | Buenos Aires | Daily reconciliation with acquirers, gateways and banks; Simetrik, SAP | https://empleos.pedidosya.com/job/reconciliation-sr-analyst-in-buenos-aires-argentina-jid-1456 |
| Rider Payments Optimization Specialist | Buenos Aires | Rider payout side | https://empleos.pedidosya.com/jobs |
| Fraud Analyst (expired) | Montevideo | Rules and model monitoring; SQL, BigQuery | https://empleos.pedidosya.com/job/fraud-analyst-in-montevideo-uruguay-jid-666 |

New country entries, PedidosYa-level acquisitions, public RFPs: No public information found.

**Key people (verify on LinkedIn before outreach)**
| Name | Title | Confidence | Source URL |
|---|---|---|---|
| Esteban Gutiérrez | CEO | High | https://empleos.pedidosya.com/equipo-de-liderazgo |
| Pablo Setuain | CFO | High | https://empleos.pedidosya.com/equipo-de-liderazgo |
| Juan Martín Sotuyo | CTO | High | https://empleos.pedidosya.com/equipo-de-liderazgo |
| Leandro Malandrini | Chief Product Officer | High | https://empleos.pedidosya.com/equipo-de-liderazgo |
| Juan Martín López | COO | High | https://www.df.cl/america/mas-supermercados-digitales-e-impulso-a-la-vertical-fintech-la-formula |
| Ignacio Costa | VP Fintech | Medium (press, 2026-04-22) | https://www.mdzol.com/sociedad/pedidosya-reunio-mas-100-socios-mendoza-y-proyecta-el-crecimiento-del-quick-commerce-n1503763 |
| Eduardo Conde | Business Development Director Fintech | Medium (press, 2024-12-05) | https://www.forbesargentina.com/negocios/pedidosya-financia-mas-12000-pymes-argentinas-programa-creditos-n63848 |
| Ignacio Ricci | Fintech Product Director | Low (search snippet only) | https://www.linkedin.com/in/ignacioricci/ |
| Melissa Calero | Senior Manager, LATAM Payments Business Development (ZoomInfo) vs Finance Sr. Manager (LinkedIn). Conflicting | Low (search snippet only) | https://www.linkedin.com/in/melissacalero/ |
| Mathias Fonseca | FORMER payments lead; left in 2019. Not a current contact | Dated | https://www.spreedly.com/customers/pedidosya |

Current Head, Director or VP of Payments at PedidosYa: No public information found.

---

## SECTION 7: Payment News

| # | Date | Headline | Relevance | Source URL |
|---|---|---|---|---|
| 1 | 2026-08-12 | 🟢 PedidosYa adds Deuna as a payment method in Ecuador, nationwide | New wallet APM via app redirect; stated aim is reducing cash | https://www.ondata.com.ec/pedidosya-pagos-deuna-ecuador/ |
| 2 | 2026-07-22 | Indecopi (Peru) fines Delivery Hero Perú S.A.C. S/ 20,790 for a pre-selected tip at checkout | Checkout design sanction; regulator labels it a dark pattern | https://larepublica.pe/sociedad/2026/07/22/indecopi-multa-a-pedidos-con-s20790-por-incluir-propina-en-su-servicio-de-delivery-sin-autorizacion-de-cliente-2194654 |
| 3 | 2026-07-23 | 🔴 PedidosYa states the automatic tip was removed in June 2026 | Checkout change after sanction | https://gestion.pe/economia/empresas/pedidos-ya-dice-que-ya-no-cobra-automaticamente-propinas-tras-sancion-de-indecopi-noticia/ |
| 4 | 2026-07-16 | Uber to acquire Delivery Hero; PedidosYa split between Uber and SSW Partners | Ownership change will drive payment stack decisions. The release says nothing about payments integration | https://www.sec.gov/Archives/edgar/data/1543151/000155278126000382/e26302_ex99-1.htm |
| 5 | 2026-07-10 | Argentina: court reopens class action against Delivery Hero E-Commerce S.A. over pre-set tip at payment | Ongoing litigation on checkout flow | https://justiciadeprimera.com/2026/07/10/ordenan-resolver-demanda-colectiva-contra-pedidos-ya-por-el-sistema-de-propinas/ |
| 6 | 2026-07-04 | 🟢 Chile: "Grupos Familiares", admin assigns balance to family members | Stored value feature | https://chocale.cl/2026/07/la-nueva-funcion-de-pedidosya-para-gestionar-compras-compartidas-con-familiares/ |
| 7 | 2026-05-01 | 🔴 Uruguay: PedidosYa stops accepting cash after 19:00 | Cash on delivery restricted for rider safety; pushes volume to digital methods | https://www.telenoche.com.uy/nacionales/pedidosya-no-aceptara-pago-efectivo-despues-las-1900-prevenir-hechos-inseguridad-n5399074 |
| 8 | 2026 (undated) | PedidosYa Créditos: over USD 30M granted in Q1 2026 (+50% YoY); repayment deducted from sales | Merchant lending scale | https://www.conopinion.com/novedades/financiamiento-otorgado-por-pedidosya-creci%C3%B3-un-50-en-latinoam%C3%A9rica |
| 9 | 2025-02-26 | 🟢 El Salvador: Banco Cuscatlán, Visa and PedidosYa launch a co-branded credit card | Issuer partnership | https://diario.elmundo.sv/empresarial/banco-cuscatlan-visa-y-pedidosya-lanzaron-innovadora-tarjeta-de-credito-con-beneficios-para-el-delivery-y-el-ahorro |
| 10 | 2024-12-06 | 🟢 Bolivia: PedidosYa launches QR payment, first market in the region on its platform | New local method | https://www.aygun.com.bo/pedidosya-lanza-el-pago-con-qr-en-bolivia-y-marca-tendencia-en-la-region/ |
| 11 | 2024-10-29 | SERNAC announces court action against Uber Eats, PedidosYa and Rappi for preset tips | Regulatory | https://www.sernac.cl/portal/604/w3-article-83146.html |
| 12 | 2024-04-05 | 🟢 Peru: Yape added as a payment method | New local method | https://latinanoticias.pe/lima/yape-pedidosya-lo-suma-como-medio-de-pago-y-forma-alianza-con-tottus-adp-noticia_20240405/ |
| 13 | 2023-04-24 | 🟢 Panama: Yappy added | New local method (older) | https://dplnews.com/panama-pedidosya-integra-yappy-como-metodo-de-pago-en-la-entrega/ |
| 14 | 2021-10-08 | Multi-year regional alliance with Visa (cards, Cybersource, Visa Direct) | Older, still the only named processor-level partnership | https://www.paymentmedia.com/news-5562-pedidosya-y-visa-firman-alianza-estratgica.html |

New PSP, acquirer or orchestrator announcements in the last 12 months: No public information found.

---

## SECTION 8: Checkout Audit

| Dimension | Finding | Quality | Notes |
|---|---|---|---|
| Checkout type | Native in-app checkout with a "Medios de Pago" screen; web also exists. Wallet APMs use app switch (MACHBANK, Deuna) or approval code (Yape) | Good | https://www.machbank.cl/alianzas-y-conexiones/pedidosya |
| Guest checkout | Registration required per Argentina T&C (2022 version). Current app: NOT VERIFIED | Unknown | https://terms.pystatic.com/about/generales/tyc_generales_argentina.html |
| Steps to purchase | Chile, per MACHBANK: build order, "Ir a pagar", "Medios de Pago", select method, confirm, app switch, PIN | Good | same MACHBANK URL |
| 3DS | NOT VERIFIED. T&Cs only say the bank validates the transaction. Venezuela T&C mentions optional biometric controls for saved payment methods | Unknown | https://www.pedidosya.com.ve/about/terminos-condiciones |
| Mobile experience | Google Play 4.7 (2.24M reviews), App Store 4.6. Listing promotes "tarjetas de crédito, débito, efectivo y billeteras digitales" | Good | https://play.google.com/store/apps/details?id=com.pedidosya&hl=es_419&gl=AR |
| APM display logic | Per country: Klap and Webpay in Chile, Yape in Peru, QR in Bolivia, Deuna in Ecuador, Pago Móvil in Venezuela | Market by market | See Section 4A |
| Saved cards | T&Cs allow a previously loaded payment method; card data "no son almacenados en PedidosYa" | Good | https://www.pedidosya.com.py/about/terminos-condiciones |
| Refund routing | Depends on method. Chile: credit card reversal via issuer; Webpay debit to wallet or bank transfer within 30 business days. Bolivia: QR refunds to wallet only. Elsewhere: coupon if the refund cannot be processed | Weak | https://www.pedidosya.cl/about/terminos-condiciones |
| Tipping | Pre-selected tip sanctioned in Peru, Argentina and challenged in Chile; removed in Peru in June 2026 | Weak (regulatory exposure) | See Section 7 |
| BNPL, installments, Apple Pay, Google Pay | NOT VERIFIED | Unknown | N/A |

> ⚠️ MANUAL: Walk checkout in top 2 to 3 markets (Argentina, Chile, Peru).

---

## SECTION 9: PCI DSS

| PCI DSS Level | Card data handling | Recommended Yuno integration | Source |
|---|---|---|---|
| Not published. Self-declared compliance only: PedidosYa "cumple con el PCI DSS (Payment Card Industry Data Security Standard)" (Costa Rica T&C, Panama privacy policy). No certificate, level or QSA disclosed | Card data collected by "proveedores financieros"; "sus datos no son almacenados en PedidosYa"; third-party vaulting through Spreedly | SDK or secure fields with Yuno as the token layer, keeping PedidosYa out of PCI scope as today. Any move requires a token migration plan from the current vault | https://www.pedidosya.cr/about/terminos-condiciones ; https://www.pedidosya.com.pa/about/privacy_policies ; https://www.spreedly.com/customers/pedidosya |

Delivery Hero group: no public PCI attestation found.

---

## SECTION 10: Strategic Insights

**Insight #1: The Uber and SSW split forces the payment stack to become portable**
Evidence: Section 6 (#3, #4). 13 markets go to Uber and Chile plus Ecuador go to SSW Partners, with Delivery Hero providing transition services for up to 24 months. | Pain Point: Chile and Ecuador will need a payment stack that can stand alone once the transition period ends (contracts, vault, routing, fraud, reconciliation), and the other 13 markets face a future platform decision under Uber. The release says nothing about payments integration, so this is an open question for the team. | Yuno Value Prop: one orchestration layer that abstracts processors and methods, so providers and ownership can change without re-integrating checkout. | Best Case: inDrive (10 LATAM markets live in under 8 months). | Outreach Angle: "With Chile and Ecuador moving to a different owner than the rest of the region, how are you planning to keep one payment stack running across both?" Note: Yuno's About page names Uber as a customer (https://y.uno/en/about); confirm scope internally before using it.

**Insight #2: Vault is not orchestration**
Evidence: Section 3B. Spreedly is published for vaulting and distribution; evidence is from 2018 and the sponsor left in 2019. Job listings show a team that monitors acceptance and "payment alarms with vendors" by hand. | Pain Point: a vault lets you switch providers, but routing rules, failover, monitoring and provider performance management still sit on internal teams. | Yuno Value Prop: smart routing (+7% approval uplift), automatic failover and real-time monitors on top of the providers already in place. | Best Case: Rappi (real-time detection in milliseconds versus 5 to 10 minutes manually; 80% less analyst resolution time). | Outreach Angle: ask how routing and failover decisions are made today between providers in Argentina and Chile, and how long it takes to detect a provider degradation.

**Insight #3: Local methods are being added one market at a time**
Evidence: Sections 4A and 7. Yappy (2023), Yape (2024), QR in Bolivia (Dec 2024), Deuna (Aug 2026), plus Tigo Money, MACH, Klap, Webpay and Pago Móvil. | Pain Point: each method is a separate integration with its own refund logic and reconciliation file; refund behavior already differs by method (Section 8). | Yuno Value Prop: single API to local methods across LATAM, new method enabled in weeks without a new build. | Best Case: inDrive. | Outreach Angle: reference only the methods confirmed above and ask which markets are next on the roadmap.

**Insight #4: Refund and orphan-charge complaints point to a reconciliation and status problem**
Evidence: Section 5. 3,417 SERNAC complaints in 2024 with refunds as the top reason; repeated "charged but order not created" and double charges after retry. | Pain Point: payment status and order status drift apart, which creates support cost, regulator exposure and refunds forced into wallet or coupons. | Yuno Value Prop: unified transaction status across providers, monitors, orchestrated retries with idempotency, single reconciliation view. Reconciliation already runs on Simetrik and SAP, so position as a cleaner data source, not a replacement. | Best Case: Livelo (+5% approval, 50% recovery). | Outreach Angle: "How much of your support volume in Chile comes from payments that were authorized but never became an order?"

**Insight #5: Cross-border card acquiring signals in four markets**
Evidence: Section 2 note. T&Cs in Ecuador, Venezuela, Costa Rica and Honduras require an "international" card for online payment. | Pain Point: [INFERENCE, not confirmed] cross-border acquiring in those markets, with lower approval and higher cost than local acquiring. | Yuno Value Prop: local acquirer connections per market with routing between local and cross-border. | Best Case: Reserva (+4% approval in under 3 months). | Outreach Angle: only after a manual test. Ask, do not assert.

**Insight #6: Collections and payouts are a second front**
Evidence: Section 3A and 4A. Rider cash remittance runs through Pago46 (Argentina, Chile) and dLocal-branded billers (Paraguay, El Salvador); merchant settlement runs weekly with paid instant payouts; PeYa Wallet depends on Wibond in Argentina. | Pain Point: a different collection and payout provider per market, plus cash risk (Uruguay cut cash after 19:00). | Yuno Value Prop: payouts and collection methods orchestrated across providers under one integration and one reconciliation. | Best Case: Rappi. | Outreach Angle: ask how cash collection from riders is reconciled across the 15 markets.

---

## SECTION 11: Pipeline

### 11A. Direct Competitors

| Company | Website | HQ | Est. Size | Overlap Markets | Source |
|---|---|---|---|---|---|
| Rappi | rappi.com | Bogotá, Colombia | Revenue USD 855.52M in 2023 (Sacra estimate); 5,200 employees | Argentina, Chile, Costa Rica, Peru, Uruguay (re-verify per country) | https://sacra.com/c/rappi/ ; https://en.wikipedia.org/wiki/Rappi |
| Uber Eats | ubereats.com | San Francisco, USA | Uber Delivery Q2 2026 Gross Bookings USD 27.463B | Argentina (relaunched 2026-03-02), Chile, Costa Rica, Dominican Republic, Ecuador, El Salvador, Guatemala, Panama. Future owner of PedidosYa in 13 markets | https://investor.uber.com/news-events/news/press-release-details/2026/Uber-Announces-Results-for-Second-Quarter-2026/default.aspx |
| DiDi Food | didi-food.com | Beijing, China | DiDi international FY 2025: 4.505B orders (all international, not food only) | Costa Rica, Peru, Dominican Republic | https://eu.36kr.com/en/p/3726781163682439 |
| Mercado Libre Restaurantes | mercadolibre.com.ar | Montevideo and Buenos Aires | Launched Q4 2025 in Rosario; no order figures | Argentina | https://www.lanacion.com.ar/economia/negocios/el-boom-del-delivery-revolucion-digital-con-traccion-a-sangre-nid25042026/ |
| Yummy | yummysuperapp.com | Caracas, Venezuela | 18M yearly transactions; valuation above USD 200M | Venezuela | https://news.northeastern.edu/2025/02/05/yummy-venezuela-delivery-app/ |
| iFood | ifood.com.br | Osasco, Brazil | 120M orders per month; 55M customers | None (Brazil only) | https://finance.yahoo.com/news/brazils-ifood-app-announces-3-100543479.html |
| 99Food (DiDi) | 99app.com | São Paulo, Brazil | Launched April 2025; 60+ cities | None (Brazil only) | https://eu.36kr.com/en/p/3726781163682439 |
| Keeta (Meituan) | keeta-global.com | Beijing, China | USD 1B pledged for Brazil | None (Brazil only) | https://technode.com/2025/05/14/chinas-meituan-to-launch-keeta-food-delivery-in-brazil-with-1-billion-investment/ |

### 11B. Industry Peers

| Company | Website | Vertical | Key Markets | Why Similar | Source |
|---|---|---|---|---|---|
| talabat | talabat.com | Food and quick commerce | Bahrain, Egypt, Iraq, Jordan, Kuwait, Oman, Qatar, UAE | Delivery Hero sister brand; FY 2025 revenue USD 3.9B | https://www.tradearabia.com/News/389296/Talabat-posts-28-Percent-GMV-growth-in-2025;-sets-$100m-for-expansion |
| Glovo | glovoapp.com | Food and quick commerce | Southern and Eastern Europe, Africa | Delivery Hero sister brand; split between Uber and SSW | https://www.sec.gov/Archives/edgar/data/1543151/000155278126000382/e26302_ex99-1.htm |
| foodpanda | foodpanda.com | Food and quick commerce | 9 APAC markets | Delivery Hero sister brand | same SEC URL |
| Baemin (Woowa Brothers) | baemin.com | Food delivery | South Korea | Delivery Hero sister brand; 2025 revenue KRW 5.28tn | https://www.koreaherald.com/article/10714666 |
| DoorDash (incl. Wolt, Deliveroo) | doordash.com | Food delivery | US, Europe | FY 2025 revenue USD 13.717B; Deliveroo closed 2025-10-02 | https://ir.doordash.com/news/news-details/2026/DoorDash-Releases-Fourth-Quarter-and-Full-Year-2025-Financial-Results/default.aspx |
| Just Eat Takeaway | justeattakeaway.com | Food delivery | Europe | Marketplace delivery peer (Prosus) | https://www.payrails.com/blog/payrails-series-a |
| Grab | grab.com | Super-app | Southeast Asia | Deliveries GMV USD 7.9B FY 2025 | https://www.grab.com/sg/press/others/grab-reports-fourth-quarter-and-2025-results-with-first-full-year-net-profit/ |
| inDrive | indrive.com | Mobility | LATAM and emerging markets | Multi-country emerging market payments | https://y.uno/en/success-stories/indrive |
| Careem | careem.com | Super-app | MENA, 10 countries | Multi-country emerging market payments | https://www.payrails.com/blog/careem-and-payrails-partner-to-optimize-payment-performance-across-mena |
| Swiggy | swiggy.com | Food and quick commerce | India | Delivery peer | https://juspay.io/customer-stories/swiggy |

### 11C. Adopting Orchestration

| Company | Orchestrator | Date | Vertical | Source |
|---|---|---|---|---|
| PedidosYa | Spreedly | Case study undated; podcast 2018-10-16 | Food delivery | https://www.spreedly.com/customers/pedidosya |
| Rappi | Yuno | Partnered 2023; case study 2024-11-21 | Super-app | https://y.uno/en/success-stories/rappi |
| inDrive | Yuno (case study 2024-09-10) and Payrails (undated) | 2024 | Mobility | https://y.uno/en/success-stories/indrive ; https://www.payrails.com/customers/indrive |
| Uber | Yuno (named on About page; scope and date not stated) | Undated | Mobility and delivery | https://y.uno/en/about |
| Just Eat Takeaway | Payrails | 2025-06-12 | Food delivery | https://www.payrails.com/blog/payrails-series-a |
| Careem | Payrails | 2024-06-19 | Super-app | https://www.payrails.com/blog/careem-and-payrails-partner-to-optimize-payment-performance-across-mena |
| Swiggy | Juspay | Undated | Food delivery | https://juspay.io/customer-stories/swiggy |

### 11D. Scoring: PedidosYa (verified only)

| Signal | Pts | Verified? |
|---|---|---|
| Operates in 3+ countries | +3 | ✅ 15 countries |
| Multiple PSPs | +3 | ✅ Klap and Webpay named in Chile T&C; dLocal billers; "10 or 11 providers" (2018) |
| Recent expansion (24 mo.) | +2 | ✅ No new countries, but new verticals (fintech, PeYa Wallet, Plus) and new payment methods (QR Bolivia, Deuna) |
| Public payment issues | +2 | ✅ SERNAC, Trustpilot, consumer portals |
| Funding >$10M | +2 | ✅ Subsidiary of listed Delivery Hero; Uber offer at USD 14.8B equity value |
| LATAM/APAC/MENA traffic | +2 | ✅ 100% LATAM |
| No orchestrator | 0 | ❌ Spreedly published |
| Payment job postings | +1 | ✅ |
| Public RFP | 0 | Not found |
| **Total** | **15** | 🔴 **High** |

🔴 High (12+) | 🟡 Medium (7 to 11) | 🟢 Low (<7)

**Top 10 Pipeline** (scores count only signals verified in this research pass; PSP stack of peers was not researched, so real scores may be higher)

| Rank | Company | Type | Key Markets | Score | Priority | Top Signal |
|---|---|---|---|---|---|---|
| 1 | PedidosYa | Target | 15 LATAM | 15 | 🔴 High | Ownership split plus multi-provider stack |
| 2 | DiDi Food | Direct competitor | Mexico, Costa Rica, Peru, Dominican Republic | 11 | 🟡 Medium | Multi-country LATAM, 99Food launch in Brazil, no orchestrator evidence |
| 3 | talabat | Sister brand | 8 MENA markets | 11 | 🟡 Medium | Going to Uber; USD 100M set for expansion |
| 4 | Glovo | Sister brand | Europe, Africa | 9 | 🟡 Medium | Split between Uber and SSW, same portability problem |
| 5 | foodpanda | Sister brand | 9 APAC markets | 9 | 🟡 Medium | Going to Uber; Taiwan sold to Grab |
| 6 | DoorDash (Wolt, Deliveroo) | Peer | US, Europe | 9 | 🟡 Medium | Post-merger stack consolidation |
| 7 | iFood | Direct competitor (Brazil) | Brazil | 6 | 🟢 Low | Single market; iFood Pago in-house |
| 8 | Yummy | Direct competitor | Venezuela | 6 | 🟢 Low | Verify multi-country footprint |
| 9 | Keeta | Direct competitor (Brazil) | Brazil, global | 6 | 🟢 Low | New LATAM entry with USD 1B commitment |
| 10 | Mercado Libre Restaurantes | Direct competitor | Argentina | N/A | N/A | Owns Mercado Pago; not a target |

Excluded because they already use Yuno or another orchestrator: Rappi, inDrive, Uber, Just Eat Takeaway, Careem, Swiggy.

Pipeline Summary: 18 companies found, 1 high-priority (PedidosYa itself), 5 medium. Strongest vertical: food and quick-commerce delivery platforms in LATAM and MENA that are part of the Delivery Hero transaction, since all of them face the same ownership split.

---

## SECTION 12: Business Case

| Annual Revenue | Avg Transaction Value | Est. Annual Transactions | Primary Currency | Top 3 Markets |
|---|---|---|---|---|
| Americas segment FY 2025: revenue EUR 977.4M (harmonized IFRS basis; EUR 1,057.6M as originally reported), GMV EUR 4,079.6M, adj. EBITDA EUR 100.0M. H1 2026: GMV EUR 2,559.8M (+29.4%), revenue EUR 618.9M (+31.3%), adj. EBITDA EUR 70.3M | [ESTIMATE] about EUR 12.4 per order in Q4 2025 (GMV EUR 1,141.2M divided by about 92M orders, from 1.0M average daily orders over 92 days). Published AOV: Not found | [ESTIMATE] about 365M orders per year at the Q4 2025 run rate of 1 million daily orders; orders grew +25% YoY in Q1 2026 | Multi-currency (ARS, CLP, UYU, PEN and others). Reported in EUR. No conversion made in this brief | Argentina, Chile, Uruguay (volume leaders per COO, 2026-01-02) |

Sources: https://ir.deliveryhero.com/media/document/a6007947-8b1b-416f-bb3e-6a7b798c4f75/assets/Delivery_Hero_Q1_2026_Trading_Update.pdf?disposition=inline ; https://ir.deliveryhero.com/media/document/8efa12b2-3fa3-4ebd-9333-ece6881bae50/assets/DE000A2E4K43-Q2-2026-EQ-E-00.pdf ; https://www.tradingview.com/news/eqs:81958b162094b:0-delivery-hero-reports-strong-q4-while-business-transforms-into-everyday-app/

**Caveats for the model**
- Delivery Hero does not publish a PedidosYa-only P&L. The Americas segment is used as the proxy. [INFERENCE, not confirmed]
- Argentina is accounted for under hyperinflation rules (IAS 29), which distorts EUR growth rates.
- Not all orders are paid online. Cash on delivery and POS on delivery exist in every market. The only published online share is about 30% in 2018, which is too old to model with. Ask for the current online share before sizing.
- Subscribers (PedidosYa Plus) were 40% of Americas GMV in Q2 2026, which adds a recurring billing flow. https://www.investing.com/news/transcripts/earnings-call-transcript-delivery-hero-tops-q2-2026-revenue-forecast-93CH-4879424

---

## SECTION 13: Outreach (verified findings only)

Written in Spanish because the payments team sits in Montevideo and Buenos Aires. No unconfirmed APM claims. Cold email carries no customer names.

```
--- LINKEDIN MESSAGE ---
Hola [Nombre], vi que PedidosYa sumó Deuna en Ecuador en agosto, después de Yape en Perú y el pago con QR en Bolivia. Cada método local nuevo es una integración más que mantener y conciliar.

En Yuno ayudamos a equipos como Rappi e inDrive a operar procesadores y métodos locales de toda la región desde una sola integración, con ruteo y monitoreo en tiempo real.

Con el acuerdo de Uber y SSW en curso, me gustaría mostrarte cómo otros equipos hicieron portable su stack de pagos. ¿Te sirve conversar 20 minutos el martes en la mañana?

--- COLD EMAIL ---
Subject: PedidosYa: 15 mercados y un método local distinto en cada uno

Hola [Nombre],

En los últimos dos años PedidosYa sumó Yape en Perú, pago con QR en Bolivia y Deuna en Ecuador. Cada método que entra es una integración más que mantener, conciliar y monitorear, en una operación que ya supera el millón de pedidos diarios.

A eso se suma el acuerdo con Uber y SSW: Chile y Ecuador van a operar bajo un dueño distinto al del resto de la región, y el stack de pagos va a tener que poder moverse con ellos.

En Yuno trabajamos esa capa: una sola integración hacia procesadores, métodos locales y antifraude, con ruteo y monitoreo en tiempo real, sin reemplazar lo que hoy funciona.

¿Tiene sentido una conversación de 30 minutos la próxima semana? Puedo el martes o el miércoles en la mañana.

Saludos,
German Tatis
Yuno
```

---

## SECTION 14: Internal Context (not public, do not cite externally)

Added after the public research was complete. Sources: Alejandro Albarracín's voice note, Gong, Google Calendar, Google Drive and Slack. Full call prep in `data/research/pedidosya-meeting-brief-2026-09-29.md`.

| Item | Detail | Source |
|---|---|---|
| This is a warm lead, not cold outreach | Belén Casaret (belen.casaret@pedidosya.com), described internally as Regional Collections Manager, reached Yuno through a contact of Alonso and wants to change the collections and payments provider. Call booked for 2026-09-29, 1:30pm COT | Voice note, Calendar |
| Main provider per Belén | dLocal. Consistent with the public biller listings in Section 3A, but share of volume and flow type are unconfirmed | Voice note |
| Head of Payments | Reportedly ex-dLocal. Name unknown | Voice note |
| Spreedly | Used mostly as a token vault. Elliot Watnik (Delivery Hero) told Yuno it has limitations and that the 2026 goal is faster time-to-market for new payment methods | Voice note, Gong |
| Cards | Internal deck states cards are processed via Worldpay and other PSPs through Spreedly. Not found in public sources | Drive, deck V3 |
| Prior engagement | Call on 2025-08-08; email thread with Elliot Watnik from 2025-11-13 to 2026-02-10; silent since December 2025. Lars Hofmann (Global Payments Director) met at MPE Berlin on 2026-03-17. Saad Saif asked for input for an APAC RFP | Gong, Slack |
| Parallel outreach | Yuno "Touchpoint" email to Leandro Malandrini (CPO) on 2026-09-21 | Gong |
| Uber | Active Yuno relationship. Keep Uber and PedidosYa information separate | Slack |

**Effect on Section 13:** the cold outreach copy is a fallback for other PedidosYa contacts. For Belén, use the meeting brief.

---

## APPENDIX: Source URLs

```
[S1] Traffic
https://www.similarweb.com/website/pedidosya.com/
https://www.similarweb.com/website/pedidosya.com.ar/
https://www.similarweb.com/website/pedidosya.cl/
https://www.similarweb.com/website/pedidosya.com.ec/
https://www.similarweb.com/website/pedidosya.com.pa/
https://www.similarweb.com/website/pedidosya.com.pe/
https://www.similarweb.com/website/pedidosya.com.uy/
https://www.semrush.com/website/pedidosya.com.ar/overview/
https://sensortower.com/blog/2025-q2-unified-top-5-food%20delivery%20services-units-latin_am-63da96fbe1714cfff1c1e5a1

[S2] Legal entities
https://www.pedidosya.com.ar/about/terminos-condiciones
https://www.pedidosya.cl/about/terminos-condiciones
https://www.pedidosya.com.uy/about/terminos-condiciones
https://www.pedidosya.com.pe/about/terminos-condiciones
https://www.pedidosya.com.ec/about/terminos-condiciones
https://www.pedidosya.com.ve/about/terminos-condiciones
https://ir.deliveryhero.com/media/document/d7cd8a32-bb5e-48d0-a416-c38f9cad59e0/assets/DeliveryHeroSE_Annual_Financial.pdf?disposition=inline

[S3] Payment stack
https://www.spreedly.com/customers/pedidosya
https://www.spreedly.com/blog/payments-dialog-episode-2-payments-and-delivery-in-latin-america-with-mathias-fonseca
https://www.montevideo.com.uy/Negocios-y-Tendencias/PedidosYa-y-Visa-firman-alianza-estrategica-regional-para-impulsar-el-Quick-Commerce-uc800543
https://www.infonet.com.py/servicios_disponibles/Dlocal%20Service
https://www.bitrefill.com/sv/es/factura/pedidosya-dlocal-bill-el-salvador/
https://www.checkout.com/case-studies/how-localized-payments-is-driving-delivery-hero-s-global-expansion
https://techcrunch.com/2022/03/17/payrails-emerges-from-stealth-with-6-4m-led-by-a16z-to-build-the-os-for-payments

[S4] APMs
https://terms.pedidosya.com/terminos-y-condiciones-del-sorteo-afilia-yape-en-pedidosya/
https://www.ondata.com.ec/pedidosya-pagos-deuna-ecuador/
https://www.aygun.com.bo/pedidosya-lanza-el-pago-con-qr-en-bolivia-y-marca-tendencia-en-la-region/
https://www.machbank.cl/alianzas-y-conexiones/pedidosya
https://riders.repartosya.com.ar/categorias/pagos.html

[S5] Complaints
https://www.sernac.cl/portal/604/w3-article-83827.html
https://es.trustpilot.com/review/pedidosya.com.ar
https://es.trustpilot.com/review/pedidosya.cl
https://www.defensadelconsumidor.com.ar/denuncias-empresa/399-pedidos-ya

[S6] Expansion and corporate
https://www.sec.gov/Archives/edgar/data/1543151/000155278126000382/e26302_ex99-1.htm
https://investor.uber.com/news-events/news/press-release-details/2026/Uber-Announces-Acquisition-Offer-for-Delivery-Hero/default.aspx
https://www.expreso.ec/economia-y-negocios/pedidosya-ecuador-tendra-nuevo-dueno-firma-wall-street-comprara-app-289950.html
https://www.df.cl/america/mas-supermercados-digitales-e-impulso-a-la-vertical-fintech-la-formula
https://empleos.pedidosya.com/equipo-de-liderazgo

[S7] Payment news
https://gestion.pe/economia/empresas/pedidos-ya-dice-que-ya-no-cobra-automaticamente-propinas-tras-sancion-de-indecopi-noticia/
https://www.telenoche.com.uy/nacionales/pedidosya-no-aceptara-pago-efectivo-despues-las-1900-prevenir-hechos-inseguridad-n5399074

[S8] Checkout
https://play.google.com/store/apps/details?id=com.pedidosya&hl=es_419&gl=AR
https://terms.pystatic.com/about/generales/tyc_generales_argentina.html

[S9] PCI DSS
https://www.pedidosya.cr/about/terminos-condiciones
https://www.pedidosya.com.pa/about/privacy_policies

[S11] Pipeline
https://y.uno/en/success-stories/rappi
https://y.uno/en/success-stories/indrive
https://y.uno/en/about
https://www.payrails.com/blog/payrails-series-a

[S12] Business case
https://ir.deliveryhero.com/media/document/a6007947-8b1b-416f-bb3e-6a7b798c4f75/assets/Delivery_Hero_Q1_2026_Trading_Update.pdf?disposition=inline
https://ir.deliveryhero.com/media/document/8efa12b2-3fa3-4ebd-9333-ece6881bae50/assets/DE000A2E4K43-Q2-2026-EQ-E-00.pdf
https://www.tradingview.com/news/eqs:81958b162094b:0-delivery-hero-reports-strong-q4-while-business-transforms-into-everyday-app/
```
