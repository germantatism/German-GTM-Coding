# Storytelling v2 · Deck Eventbrite + Yuno

**Estado:** v2 con los ajustes de German (2026-08-04). Pendiente de aprobación final antes de construir.
**Cambios vs v1:** entra Executive Summary como primer slide de contenido · EBANX fuera del stack actual (no son cliente de EBANX, cero mentiras) · el routing de pay-ins Y payouts pasa al centro con respaldo de la documentación pública de Yuno · desaparece la sección Proof (la lista de clientes la absorbe: entra Fiverr, salen los que no hacen fit).
**Fuentes:** transcript call 2026-08-04 (Paul Pasion) · docs.y.uno (Routing, Payouts, Split Marketplace Payments) · deck Flair como referencia de formato.
**Deadline externo:** viernes 2026-08-14. Justo en Milán en ~3 semanas.
**Dato de German (2026-08-04):** Top 10 operating countries de Eventbrite (de **122**): 1 US · 2 UK · 3 Canadá · 4 Australia · 5 Italia · 6 Alemania · 7 España · 8 Irlanda · 9 Francia · 10 México. Implicación para el deck: el peso está en US + Europa (IT/DE/ES/FR, territorio de Milán y de PSD3) y México es el único LatAm en el top 10; usar estos países en los ejemplos de routing y en el slide de entidades.

---

## 1. Contexto en cinco líneas

- Paul Pasion (Director of Commerce, Head of Payments) sale en dos semanas; deja una lista corta de orquestadores a la dirección entrante.
- Deciden **Noè, Giacomo y Filippo** (commerce, Bending Spoons, Milán): muy inteligentes, rápidos, ADN suscripciones, **nuevos en marketplaces**.
- El deck es el artefacto que Paul reenvía: **funciona standalone**.
- Eventbrite está **en este momento decidiendo si meter un orquestador o no**, hablando con varios. Ese es el punto de partida del deck y por eso el Executive Summary abre.
- La columna vertebral sigue siendo la frase de Paul (anonimizada): *"great orchestrators for pay-ins, decent ones for payouts, no one's tied the two together."*

## 2. Arco narrativo (5 actos)

1. **EXECUTIVE SUMMARY** · dónde está Eventbrite hoy y qué decisión tienen sobre la mesa. Un solo slide, denso, estilo Flair.
2. **WHY YUNO?** · credibilidad para una audiencia que no nos conoce: escala, clientes, operadores.
3. **EVENTBRITE & THE MARKETPLACE GAP** · su stack real (sin EBANX) y el hueco estructural de la industria.
4. **MODULAR BY DESIGN** · el corazón: cómo operamos modular y cómo ruteamos **pay-ins y payouts**, con capabilities documentadas públicamente en docs.y.uno.
5. **THE PATH FORWARD** · el encaje con el modelo Bending Spoons y el timeline.

---

## 3. Slide a slide (24 slides)

### Bloque 01 · EXECUTIVE SUMMARY

| # | Slide | Contenido |
|---|---|---|
| 1 | **Cover** · "One layer for both sides of the marketplace" | Lockup `yuno \| eventbrite`, estilo casa |
| 2 | **Agenda** | 01 Executive summary · 02 Why Yuno? · 03 Eventbrite & the marketplace gap · 04 Modular by design · 05 The path forward |
| 3 | **Executive Summary** (el slide nuevo, primero de contenido, formato Flair: contexto izquierda, valor derecha) | **Izquierda, "Where Eventbrite stands today":** (a) Nueva etapa: Eventbrite opera desde marzo 2026 como parte de Bending Spoons, con un modelo operativo lean. (b) **La decisión sobre la mesa, hoy: si incorporar una capa de orquestación o no**, con una evaluación activa de varios orquestadores. (c) Dirección ya tomada por el equipo: multi-PSP sobre consolidar en un solo procesador. (d) Frentes abiertos que la decisión debe resolver: routing inteligente entre los rieles existentes (incl. la economía ChaseNet ofrecida por J.P. Morgan), la salida de entidades propias en LatAm, la salida del funds flow con PSD3 en el horizonte, y la operación con un equipo reducido. **Derecha, "What Eventbrite gets with Yuno" (3 bullets):** 1) Pay-in AND payout routing en una sola capa, con el ledger que los une. 2) Modular: activa solo lo que necesitas, conserva cada provider que ya tienes. 3) Un dashboard: data normalizada y reconciliación automática en todos los rieles |

### Bloque 02 · WHY YUNO?

| # | Slide | Contenido |
|---|---|---|
| 4 | Divider | |
| 5 | **One integration, the whole payments ecosystem** | 1,000+ métodos · 190+ países · 460+ integraciones · 180+ monedas |
| 6 | **Trusted by leading companies worldwide** | La lista de clientes ES la prueba (sección Proof eliminada). **Entran: Fiverr y Whop** (marketplaces, máximo fit). **Salen: Moonactive y NetEase Games** (gaming, poco fit con su modelo). Lista propuesta (15): Uber, GoFundMe, **Fiverr**, **Whop**, SpaceX, Zuora, McDonald's, Qatar Airways, Rappi, Crypto.com, Samsung, inDrive, Copa Airlines, Ant Group, Hotmart. ⚠️ No hay asset de logo Fiverr en el repo: conseguirlo o wordmark |
| 7 | **Built and operated by global payment operators** | Team de casa: JP (Rappi), Julián (Rappi), Justo (dLocal/Worldpay/Global Collect), Mau (RappiBank/Mastercard), Chee (JPMorgan/Uber), Walter (MercadoPago/Cielo). Sub-mensaje para Milán: mismo ADN |

### Bloque 03 · EVENTBRITE & THE MARKETPLACE GAP

| # | Slide | Mensaje único | Diagrama |
|---|---|---|---|
| 8 | Divider | | |
| 9 | **Eventbrite's payment stack today** | Seis rieles punto a punto, sin capa entre ellos | **D1 · Topología:** Users → Eventbrite → **Stripe, Braintree, J.P. Morgan Chase, Wells Fargo, Mercado Pago, Banco Galicia**. **SIN EBANX** (no son cliente; cero mentiras). Columna "in the team's own words": sin failover ni BIN routing entre rieles · un portal de reporting por proveedor · creators acoplados a un rail (doble FX en eventos cross-currency) · entidades propias BR/AR/MX/CO bajo revisión |
| 10 | **The gap nobody closes** | El medio del marketplace está vacío en toda la industria | **D2 · El hueco:** pay-in orchestration (madura) ← [centro punteado vacío: KYC/KYB · funds & ledger · FX · recon · fraud en ambos lados] → payout providers (desconectados). Franja: en Uber y Amazon este medio lo operan cientos de ingenieros; una compañía lean lo necesita como servicio |

### Bloque 04 · MODULAR BY DESIGN (el corazón)

| # | Slide | Mensaje único | Diagrama y respaldo |
|---|---|---|---|
| 11 | Divider | | |
| 12 | **A modular operating system for payments** | Cada módulo standalone, cada módulo con cualquier provider | **D3 · El central:** EVENTBRITE one API → tablero YUNO OS con 7 módulos (Pay-in routing · Payouts · KYC & KYB · Fraud · Reconciliation · Tokenization · MoR network) → fila de providers (Stripe, Braintree, J.P. Morgan, Adyen, Mercado Pago, dLocal, Nium, Thunes, +460). "Adding a provider is configuration, not a build" |
| 13 | **Bundle lock-in vs modular freedom** | El creator se onboardea una vez y es tuyo, no del rail | **D4 · Diferenciación:** monolito (KYC atado, payout atado a país/moneda, doble FX, salir = re-onboardear) vs modular (creator onboarded once, KYC portable; pay-in, ledger y payout independientes, cada uno al mejor provider) |
| 14 | **Pay-in routing, as deep as you want it** | Rutas por condiciones, cascadas por outcome, AI que optimiza conversión y costo | **D5 · Flujo pay-in (todo documentado en docs.y.uno ✅):** Transaction → **condition-based routes** (card type, amount, currency, origin, BIN) → ramas: Chase-issued → **ChaseNet** (economía on-us) ⚠️verificar · US debit → least-cost rails ⚠️verificar · resto → **Smart Routing AI** que "optimiza conversion rate + costs o conversion rate + latency" ✅doc. Decline → **cascading por outcome** (Succeeded/Pending/Declined/Error, pasos encadenados) ✅doc. Extras documentados: **splits porcentuales entre conexiones** (el 50% modelos / 50% reglas propias que pidió Paul) ✅doc · risk steps (fraud/3DS) como gates ✅doc · post-auth steps (p.ej. Cybersource para risk review o settlement) ✅doc. Cards laterales: retry economics por decline code, interchange+ downgrades visibles |
| 15 | **Payout routing, the same discipline on the other side** (NUEVO, el slide que pidió German) | El payout también se rutea: provider, riel, moneda y FX, por payout | **D6 · Flujo payout (documentado ✅):** Payout request → gate KYC/KYB del beneficiario → **selección de provider por payout** con cotización FX en vivo entre providers (la subasta que describió Justo: cada provider responde su rate, gana el mejor) ⚠️verificar wording → tres rieles de salida documentados: **bank transfer local** ("directly into your partners' local bank accounts in their preferred currency" ✅doc) · **card payout vía Referenced Payouts** ("card payouts using previously tokenized card data from earlier transactions" ✅doc, el tie pay-in→payout literal, sin PCI scope para el merchant) · **wallets** ✅doc. Estados y notificaciones en tiempo real ✅doc |
| 16 | **Split marketplace payments, native** (NUEVO) | Los fondos del marketplace se dividen, con KYC y liability configurados por recipient | **D7 · Splits (documentado ✅):** payment → split entre recipients **manual o automático (PERCENTAGE / FIXED / MIXED)** ✅doc → cada recipient con **onboarding dinámico KYC/KYB** (forms, docs, validación, estados CREATED→PENDING→SUCCEEDED) ✅doc → **liability configurable por recipient**: processing fee MERCHANT/RECIPIENT/SHARED y chargeback liability ✅doc → **standalone transfers** desde el balance de la organización fuera del ciclo de pago (SPLIT_TRANSFER / reverse) ✅doc. Nota honesta en el slide: Yuno orquesta, el provider procesa; los splits corren sobre providers que los soportan (Stripe, Adyen, dLocal) ✅doc |
| 17 | **The marketplace loop, closed** | Cada pay-in ligado a su payout, a nivel transacción | **D8 · El loop:** Attendee → PAY-IN (mejor ruta) → **YUNO LEDGER** (vínculo transaccional, KYC portable, reservas) → PAYOUT (ruteado, FX competido) → Creator. Arco de fraude cruzando ambos lados: el patrón de colusión con eventos falsos que una herramienta solo-pay-in no ve. Referenced Payouts como el hilo técnico documentado que une las puntas ✅doc. Badge: Fiverr ~$900K FX en 6 meses ⚠️verificar por escrito |
| 18 | **Exit LatAm entities without exiting LatAm** | Cerrar BR/AR/MX/CO sin perder el negocio local | **D9 · Por país:** TODAY (entidad propia, funds flow propio) → WITH YUNO (MoR partner en el país, pay-ins neteados vs payouts). Cards: 85+ MoR providers rankeados por mercado ⚠️verificar · alcance modular (MoR completo o tax-of-record + componentes) · una capa de reporting encima. EBANX aparece aquí **solo como parte de la red de Yuno** (conexión directa) ⚠️verificar, jamás como algo que Eventbrite ya usa |
| 19 | **One dashboard, every rail** | Payment ops nunca más entra a otro portal | **D10 · Embudo:** N portales → normalización + recon (transaction × settlement reports) → un dashboard con drill-down dirigido. Franja: Starlink ~100 mercados, de ~100 dashboards a 1 ⚠️verificar por escrito |
| 20 | **Out of the funds flow, in stages** | El end-state regulatorio llega por etapas, y el valor antes | **D11 · Escalera:** 1 Fast fix (MoR local) → 2 Unbundle (KYC, tax, payout como módulos) → 3 End state (fuera del funds flow, sin registro PSP/MSB, PSD3-ready). Nota: la agent exemption se estrecha en Europa y casi desapareció en Canadá |

### Bloque 05 · THE PATH FORWARD

| # | Slide | Mensaje único | Contenido |
|---|---|---|---|
| 21 | Divider | | |
| 22 | **Built for the Bending Spoons operating model** | Payments como servicio, no como org | La superficie de pagos de Eventbrite (6 rieles, ledger de marketplace, entidades LatAm, payouts) consumía un equipo de ingeniería de 27. Cards: el único marketplace en un portafolio de suscripciones, la misma capa corre ambos modelos (los rails de Zuora corren sobre Yuno ⚠️verificar por escrito) · cada adquisición futura aterriza como configuración · un banco de expertos regional sin contratarlo |
| 23 | **Next steps** | Todo cabe en la ventana de transición | THIS WEEK: MNDA + materiales custom → NEXT WEEK: intro al equipo entrante → LATE AUGUST: working session en Milán, CRO en sitio → SEPTEMBER: deep-dive, datos y diseño de piloto |
| 24 | **Closing** | Let's grow together | German + Justo, lockup de cierre |

---

## 4. Reglas duras (decididas por German)

1. **Cero Fever** (texto y logos). 2. **Sin business case cuantificado ni pricing.** 3. **Sin CFO Copilot.** 4. **EBANX jamás como parte del stack actual de Eventbrite**; solo como conexión de la red Yuno. 5. Facts-only: capabilities con respaldo en docs.y.uno van como afirmación; lo dicho por Justo en el call se marca ⚠️ y se verifica antes de escribirlo. 6. Nunca "you lack". 7. Sin em-dashes ni " - ". 8. Inglés. 9. La cita de Paul, anonimizada.

## 5. Capabilities con respaldo público (docs.y.uno) → seguras por escrito ✅

- Routing por condiciones (card type, amount, currency, origin) con **cascading por outcome** y pasos encadenados
- **Smart Routing AI**: optimiza "conversion rate + costs" o "conversion rate + latency"; splits porcentuales entre conexiones cuando el merchant quiere mantener control parcial
- Risk steps (fraud/3DS) como gates dentro de la ruta; post-auth steps (p.ej. Cybersource)
- **Payouts API**: bank transfer, card, wallet; localización a cuentas bancarias locales en la moneda preferida; estados y notificaciones
- **Referenced Payouts**: payout a la tarjeta tokenizada del pay-in original (el tie documentado, sin PCI scope para el merchant)
- **Split Marketplace Payments**: splits manual/auto (percentage/fixed/mixed), onboarding dinámico de sub-merchants con KYC/KYB, liability por recipient (fees y chargebacks), standalone transfers; con la nota honesta de que corre sobre providers que soportan splits

## 6. Checklist a verificar con Justo/Jarrett ANTES de construir ⚠️

- [ ] **ChaseNet** activo y routing por BIN en producción (y con quién se puede decir)
- [ ] Débito US: **Star / Pulse / NYCE**, directo o vía acquirer
- [ ] La **subasta de FX entre payout providers** tal como la contó Justo (wording exacto para el slide 15)
- [ ] Providers de payout nombrables: **Nium, Thunes, TerraPay** (y el "tidoka" del transcript: ¿es Tazapay u otro? confirmar nombre real)
- [ ] **EBANX conexión directa** de Yuno y el número "85+ MoR providers"
- [ ] **Starlink** ~100 dashboards → 1, por escrito
- [ ] **Fiverr** ~$900K FX / 6 meses, por escrito, y logo
- [ ] **Zuora** "rails corren sobre Yuno", por escrito
- [ ] **Whop** nombrable en logos (ya está en el asset folder)
- [ ] Cascada de ejemplo "Stripe → Braintree → Adyen" con SUS providers, ¿ok por escrito?

## 7. Qué sigue

1. German aprueba esta v2 (o ajusta).
2. Checklist sección 6 validado en el SYNC con Justo y Jarrett.
3. Se construye el deck sobre este documento, slide a slide.
