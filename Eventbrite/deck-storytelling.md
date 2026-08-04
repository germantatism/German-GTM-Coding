# Storytelling · Deck Eventbrite + Yuno

**Estado:** propuesta de narrativa para aprobación de German. No se construye nada hasta que este documento esté aprobado.
**Fecha:** 2026-08-04 · **Fuente primaria:** transcript del call Eventbrite + Yuno (2026-08-04, 49 min, Paul Pasion) · **Referencia de formato:** Business Case Flair Airlines
**Deadline externo:** viernes 2026-08-14 ("we have from now until next Friday", Paul). Justo en Milán en ~3 semanas.

---

## 1. La situación, en cinco líneas

- Paul Pasion (Director of Commerce, Head of Payments) **sale de Eventbrite en dos semanas**. Su último encargo: dejarle a la nueva dirección una lista corta de orquestadores.
- Los decisores reales son **Noè, Giacomo y Filippo**, los tres líderes de commerce entrantes, en **Milán** (Bending Spoons).
- El deck es el **artefacto que Paul reenvía**: tiene que funcionar solo, sin nadie presentándolo.
- Los tres de Milán son "very smart, they move fast", vienen del mundo **suscripciones** y son **nuevos en marketplaces**. Paul pidió explícitamente que los eduquemos.
- Hay NDA en camino, y la promesa de Justo en el call fue "custom materials that speak to the points we reviewed".

## 2. La audiencia y qué necesita cada uno

| Audiencia | Qué necesita del deck |
|---|---|
| **Noè, Giacomo, Filippo (Milán)** | Entender qué es Yuno (no nos conocen), entender por qué un marketplace es distinto a una suscripción, y ver un plan que encaje con su modelo operativo de 40-50 personas |
| **Paul (filtro, 2 semanas)** | Ver reflejado 1:1 lo que dijo en el call, sin inflar nada. Si el deck exagera una sola capability, no lo reenvía |
| **Justo (Milán, en 3 semanas)** | Que el deck deje la mesa servida para el workshop: tesis clara, cero números que defender antes de tiempo |

## 3. La columna vertebral (la frase que carga todo el deck)

Paul, textual en el call:

> *"I found a lot of great orchestrators for pay-ins, a couple of pretty decent ones for payouts, but **no one's tied those two things together**."*

Ese es el gap, es la razón por la que todavía no ha elegido orquestador, y es exactamente lo que Yuno resuelve. **Todo el deck existe para demostrar esa frase.** Ningún slide que no alimente esa tesis entra.

La frase se usa **anonimizada** en el deck (como insight de industria, no como cita de Paul): él la reconocerá como suya, y para Milán funciona como diagnóstico experto.

## 4. El arco narrativo, en cinco actos

**Acto 1 · WHY YUNO? (credibilidad)**
Milán no nos conoce. Antes de cualquier tesis: quiénes somos, escala (1,000+ métodos, 190+ países, 460+ integraciones, 180+ monedas), quién confía en nosotros (Uber, GoFundMe, SpaceX, Zuora, McDonald's...), y quién opera esto (operadores de pagos: Rappi, dLocal, Worldpay, JPMorgan, MercadoPago). Sub-mensaje para Bending Spoons sin decirlo: somos el mismo ADN que ustedes, smart y rápido.

**Acto 2 · EVENTBRITE & THE MARKETPLACE GAP (el problema)**
Dos movimientos. Primero, el stack actual de Eventbrite tal como Paul lo describió (seis rieles sin routing, un portal por proveedor, creators acoplados a un rail, entidades LatAm bajo revisión). Segundo, la generalización: eso no es un problema de Eventbrite, es EL problema estructural de los marketplaces, y la industria de orquestación lo dejó abierto (pay-in resuelto, payout a medias, el medio vacío). Cierre del acto: en Uber y Amazon ese "medio" lo operan cientos de ingenieros; una compañía lean lo necesita como servicio.

**Acto 3 · MODULAR BY DESIGN (la solución, todo en diagramas)**
El corazón del deck. Primero los dos diagramas de posicionamiento: el sistema operativo modular (cada módulo standalone, cada módulo habla con cualquier provider) y bundle vs modular (el anti Stripe-Connect: el creator se onboardea una vez y es portable). Después, los cinco problemas de Paul resueltos 1:1, cada uno con su diagrama: routing/ChaseNet, salida de entidades LatAm, un solo dashboard, el loop marketplace cerrado, y la salida del funds flow por etapas.

**Acto 4 · PROOF (evidencia, no slides)**
Paul filtró con "specific examples". Cuatro credenciales con historia concreta: GoFundMe (el modelo two-sided espejo), Uber (extensión del equipo de pagos), Starlink (~100 dashboards a 1), Fiverr (~$900K FX en payouts en 6 meses). Sin Fever.

**Acto 5 · THE PATH FORWARD (el cierre para Milán)**
El puente al modelo Bending Spoons: payments como servicio y no como org, el único marketplace en un portafolio de suscripciones (misma capa cubre ambos: Zuora del lado subs), cada adquisición futura como configuración. Y el timeline: NDA esta semana, intro a Milán, workshop con Justo en Milán, deep-dive y piloto en septiembre.

## 5. Slide a slide (23 slides, esqueleto Flair)

Cada slide con: título (EN), el mensaje único (una frase que el lector debe llevarse), y el diagrama si aplica.

### Acto 1 · WHY YUNO?

| # | Slide | Mensaje único | Notas |
|---|---|---|---|
| 1 | **Cover** · "One layer for both sides of the marketplace" | El título ES la tesis | Lockup `yuno \| eventbrite`, estilo cover oscuro de casa |
| 2 | **Agenda** | 5 bloques | Formato Flair |
| 3 | Divider · Why Yuno? | | |
| 4 | **One integration, the whole payments ecosystem** | Escala real: 1,000+ métodos, 190+ países, 460+ integraciones, 180+ monedas | 4 stat tiles de casa |
| 5 | **Trusted by leading companies worldwide** | Jugamos en la liga de ustedes | Grilla de logos; priorizar Uber, GoFundMe, SpaceX, Zuora, McDonald's, Qatar. **Sin Fever** |
| 6 | **Built and operated by global payment operators** | No somos un vendor, somos operadores | Team: JP (Rappi), Julián, Justo (dLocal/Worldpay), Mau (RappiBank/Mastercard), Chee (JPMorgan/Uber), Walter (MercadoPago/Cielo) |

### Acto 2 · EVENTBRITE & THE MARKETPLACE GAP

| # | Slide | Mensaje único | Diagrama |
|---|---|---|---|
| 7 | Divider | | |
| 8 | **Eventbrite's payment stack today** | Seis rieles punto a punto, sin capa entre ellos | **D1 · Topología:** Users → Eventbrite → Stripe, Braintree, J.P. Morgan Chase, Wells Fargo, Mercado Pago, Banco Galicia; EBANX colgando de Braintree en línea punteada. Columna lateral "in the team's own words": sin routing entre rieles · un portal por proveedor · creators acoplados a un rail (doble FX) · entidades BR/AR/MX/CO bajo revisión. **Todo sale de las palabras de Paul**, redactado neutro, jamás "les falta" |
| 9 | **The gap nobody closes** | El medio del marketplace está vacío en toda la industria | **D2 · El hueco:** izquierda "pay-in orchestration, categoría madura" → centro punteado "the connecting layer: KYC/KYB · funds & ledger · FX · reconciliation · fraud en ambos lados" → derecha "payout providers, desconectados". Cierre en franja azul: en Uber y Amazon este medio lo operan equipos de cientos; una compañía lean lo necesita como servicio |

### Acto 3 · MODULAR BY DESIGN

| # | Slide | Mensaje único | Diagrama |
|---|---|---|---|
| 10 | Divider | | |
| 11 | **A modular operating system for payments** | Cada módulo standalone, cada módulo con cualquier provider, nada te obliga al bundle | **D3 · El central del deck:** arriba "EVENTBRITE · one API" → tablero azul "YUNO OS" con 7 módulos enchufables (Pay-in orchestration & routing · Payouts · KYC & KYB · Fraud · Reconciliation · Tokenization · MoR network) → abajo la fila de providers (Stripe, Braintree, J.P. Morgan, Adyen, Mercado Pago, EBANX, dLocal, Nium, Thunes, +460). Caption: "adding a provider is configuration, not a build" |
| 12 | **Bundle lock-in vs modular freedom** | El creator se onboardea una vez y es tuyo, no del rail | **D4 · Diferenciación:** izquierda el monolito oscuro (KYC atado a la cuenta, processing en el mismo rail, payout atado a país/moneda, doble FX, salir = re-onboardear a todos); derecha el modelo modular (creator onboarded once, KYC portable → pay-in, ledger y payout como módulos independientes, cada uno al mejor provider). Franja de cierre: los platform products usan por debajo los mismos providers de KYC y payout que puedes usar standalone; la modularidad te devuelve esa elección y su economía |
| 13 | **Routing that pays for itself from day one** | El caso ChaseNet que Paul planteó, resuelto como configuración | **D5 · Flujo de routing:** Transaction → BIN lookup → tres ramas: Chase-issued → ChaseNet (economía on-us) · US debit → least-cost rails (Star/Pulse/NYCE) · resto → mejor ruta por costo y auth; decline → cascada Stripe→Braintree→Adyen. Cards laterales: retry economics (retry solo cuando el recovery esperado supera los fees de scheme, por decline code) e interchange+ (downgrades visibles a nivel transacción) |
| 14 | **Exit LatAm entities without exiting LatAm** | Cerrar BR/AR/MX/CO sin perder el negocio local | **D6 · Por país, dos filas:** TODAY (entidad propia, compliance propio, funds flow propio) → WITH YUNO (MoR partner en el país, pay-ins neteados contra payouts localmente). Cards: 85+ MoR providers rankeados por mercado, EBANX directo y no vía gateway · alcance modular (MoR completo o tax-of-record + componentes, por etapas) · una capa de reporting encima, nunca otro portal |
| 15 | **One dashboard, every rail** | Payment ops nunca más entra a otro portal | **D7 · Embudo:** N portales (Stripe, Braintree, JPM, EBANX, Mercado Pago) → motor de normalización + reconciliación (transaction reports × settlement reports, cruzados automático, raw data debajo) → ONE DASHBOARD (drill-down solo en discrepancia señalada, con referencias exactas). Franja: Starlink, ~100 mercados, de ~100 dashboards a uno |
| 16 | **The marketplace loop, closed** | Cada pay-in ligado a su payout, a nivel transacción | **D8 · El loop:** Attendee → PAY-IN (mejor ruta) → YUNO LEDGER (el vínculo transaccional entre ambos lados, KYC/KYB portable, reservas) → PAYOUT (providers compiten por payout con FX en vivo: Nium, Thunes, TerraPay) → Creator. Arco superior oscuro: fraud signals en ambos lados, el patrón de colusión con eventos falsos que una herramienta solo-pay-in no puede ver. Badge: Fiverr ~$900K FX en 6 meses. **Sin CFO Copilot** |
| 17 | **Out of the funds flow, in stages** | El end-state regulatorio se alcanza por etapas, y el valor llega antes | **D9 · Escalera de 3 peldaños:** 1 Fast fix (MoR local toma el funds flow por mercado) → 2 Unbundle (KYC, tax y payout como módulos separados, economía visible por componente) → 3 End state (fuera del funds flow, sin registro PSP/MSB, PSD3-ready, Canadá compliant). Nota: la agent exemption se estrecha en Europa y casi desapareció en Canadá; la estructura está diseñada para que el valor aterrice antes de que la regulación fuerce el cambio |

### Acto 4 · PROOF

| # | Slide | Mensaje único | Contenido |
|---|---|---|---|
| 18 | Divider | | |
| 19 | **Marketplace problems we already run in production** | "Specific examples", literal | 4 cards: **GoFundMe** (two-sided a escala: pay-ins, KYC y payouts en una capa) · **Uber** (extensión del equipo de pagos: routing, conocimiento local, leverage de negociación) · **Starlink** (~100 mercados con entidades locales, ~100 dashboards a 1) · **Fiverr** (~$900K FX en payouts en 6 meses). Footnote: cifras como se compartieron en conversación, referencias disponibles. **Sin Fever, sin métricas inventadas** |

### Acto 5 · THE PATH FORWARD

| # | Slide | Mensaje único | Contenido |
|---|---|---|---|
| 20 | Divider | | |
| 21 | **Built for the Bending Spoons operating model** | Una compañía lean no corre payments como org; lo corre como servicio | Izquierda: la superficie de pagos de Eventbrite (6 rieles, ledger de marketplace, entidades LatAm, payouts a creators) consumía un equipo de ingeniería de 27; Yuno opera esa superficie como infraestructura. Derecha, 3 cards: el único marketplace en un portafolio de suscripciones, la misma capa corre ambos modelos (los rails de Zuora corren sobre Yuno) · cada adquisición futura aterriza como configuración, no como proyecto de integración · un banco de expertos regional que no tienes que contratar |
| 22 | **Next steps** | Todo cabe dentro de la ventana de transición | Timeline: THIS WEEK (MNDA firmado as-is + materiales custom) → NEXT WEEK (intro al equipo entrante de commerce) → LATE AUGUST (working session en Milán, CRO de Yuno en sitio) → SEPTEMBER (deep-dive técnico, intercambio de datos, diseño de piloto). Franja: la fundación queda puesta antes del handover; el equipo entrante arranca con respuestas, no con preguntas |
| 23 | **Closing** | Let's grow together | Contactos: German + Justo. Lockup de cierre |

## 6. Reglas duras de este deck (decididas por German)

1. **Cero menciones a Fever**, ni en texto ni en logos.
2. **Sin business case cuantificado ni pricing.** Los números llegan en Milán con datos de ellos.
3. **Sin CFO Copilot.**
4. Facts-only: nada que Justo no haya dicho en el call o que no sea público y verificable. Cifras de casos con footnote "as shared in conversation".
5. Nunca "you lack / les falta": el stack actual se describe en las palabras del propio equipo, neutro.
6. Sin em-dashes ni " - " como puntuación. Inglés en todo el deliverable.
7. La cita de Paul se usa anonimizada como insight de industria.

## 7. Claims a verificar con Justo/Jarrett ANTES de construir

Todo esto lo dijo Justo en el call y está en el storytelling; confirmar que puede ir por escrito y que es exacto:

- [ ] Conexión **ChaseNet** activa y routing por BIN en producción (con qué merchants se puede decir)
- [ ] Débito US: rieles **Star / Pulse / NYCE** directos o vía acquirer
- [ ] **EBANX directo** (no vía gateway) y el número "85+ MoR providers"
- [ ] Providers de payout nombrables: **Nium, Thunes, TerraPay** (Justo también mencionó "tidoka", verificar nombre real)
- [ ] **Starlink**: "~100 dashboards a 1" por escrito
- [ ] **Fiverr**: "~$900K FX en 6 meses" por escrito
- [ ] **GoFundMe** y **Zuora** ("we power all of the rails for Zora") nombrables por escrito
- [ ] Derechos de logos para el slide Trusted by
- [ ] La cascada "Stripe → Braintree → Adyen" como ejemplo escrito (son SUS providers, ¿ok nombrarlos así?)

## 8. Qué sigue

1. German aprueba o ajusta este storytelling.
2. Se valida el checklist de la sección 7 (idealmente en el SYNC con Justo y Jarrett).
3. Solo entonces se construye el deck, slide a slide, sobre este documento.
