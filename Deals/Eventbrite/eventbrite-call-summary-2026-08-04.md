# Eventbrite + Yuno: resumen detallado del call

**Call:** 2026-08-04, 49 min (contenido real desde 12:40, Paul llegó tarde)
**Eventbrite:** Paul Pasion, Director of Product Management, Commerce (Head of Payments)
**Yuno:** German (SDR), Justo (CRO), Jarrett (Senior SE), Tomas (SE), Joaquin (SE)

---

## TL;DR

El call cambió el deal por completo. Paul Pasion sale de Eventbrite en ~2 semanas (se va a Hawaii, sin planes después) y su última tarea es armar la shortlist de orchestrators para el nuevo liderazgo. Los decision makers reales son ahora tres líderes de commerce de Bending Spoons en Milán: **Noe, Giacomo y Filippo**. Paul prometió intro (email como mínimo, meeting idealmente) apenas firmemos su MNDA, y Justo estará en Milán en ~3 semanas para un posible workshop. La ventana operativa que Paul dio: **"from now until next Friday"** (viernes 2026-08-14). El diferenciador que nos hace avanzar, en palabras de Paul: encontró buenos orchestrators de pay-in, decentes de payout, y **"no one's tied those two things together"**. Eso es exactamente nuestro pitch de marketplace (GoFundMe/Fever).

---

## 1. El cambio de escenario

- **Paul se va en 2 semanas.** "I'm Paul, director of commerce at Eventbrite for another two weeks." Su misión de salida: "put together a list of folks for the incoming leadership team to talk to". Ya no vendemos a Paul; vendemos a través de Paul.
- **Los compradores son Bending Spoons Milán.** Noe, Giacomo y Filippo, "the three leaders for commerce that are taking over", todos basados en o cerca de Milán. Vienen del mundo suscripciones, "relatively new to the marketplace space". Paul pidió explícitamente que los eduquemos: "give them a little bit of education".
- **Eventbrite pesa dentro del grupo.** Representa ~1/3 del revenue total de Bending Spoons y es su único marketplace (el resto del portafolio, ~50 compañías, es suscripción). Paul: "they move fast... I see some of the similar DNA with you guys."
- **El mandato de recursos es brutal.** Eventbrite tenía 700-800 empleados; Bending Spoons cree que el negocio se corre con 40-50 personas. El equipo de ingeniería de Paul era de 27. Modernizar payments in-house es inviable; por eso existe el proceso de outsourcing de orquestación.
- **Puerta al portafolio.** Justo lo dijo en el pre-call: entrar a Eventbrite es la puerta a Vimeo y al resto de las ~50 propiedades de Bending Spoons.

## 2. Qué busca Eventbrite (sus pains, en detalle)

**a. Orquestación básica que hoy no existe.** Stack fragmentado: Stripe, PayPal/Braintree, JPMorgan Chase, Wells Fargo, Mercado Pago y Banco Galicia (Argentina). Sin routing por rieles de débito, sin cascada de failover ("if something fails at Stripe, send it over to Braintree... we're not doing any of that"), sin routing por BIN.

**b. Multi-PSP ya decidido.** Stripe y PayPal presionan para consolidar todo con ellos; Paul lo rechazó: "Been in the payments business for 20+ years. I don't trust any payment gateway... their profit is most important to them, not my customers." Internamente ya hay alineación multi-PSP. La pregunta abierta es solo cómo resolver la orquestación.

**c. Use case ChaseNet.** JPM les ofreció descuentos vía ChaseNet para tarjetas emitidas por Chase. Necesitan reconocer el BIN upfront y rutear a Chase en vez de PayPal. No tienen recursos para construirlo; esperan que el orchestrator lo haga.

**d. Salida de entidades LatAm + MoR.** Tienen entidades propias en Brasil, Argentina, México y algo en Colombia que quieren cerrar, pero como marketplace necesitan presencia in-country para pagar a los creators locales. Están hablando con EBANX (accesible vía Braintree), pero el reporting es un desastre y su líder de payment ops se negó a "ir a otro portal más".

**e. Data normalization + portal único.** Pregunta directa: "do you do data normalization? Do we have a single portal where payments operations folks go and do the chargeback management even though it's going through this very weird EBANX flow?"

**f. Detalle a nivel transacción para economía interchange+.** Son interchange plus en US. Quieren identificar downgrades y patrones de downgrades, y aplicar lógica de retry con criterio económico: a veces vale pagar las multas de Visa por reintentar, a veces no.

**g. Fraude de colusión, específico de su marketplace.** El onboarding de creators es tan fácil que fraudsters crean eventos falsos y pasan tarjetas robadas por su propio "merchant" falso. Stripe Radar no ve el lado merchant. Hoy lo detectan post-transacción con herramientas internas y reversan o refundan para evitar chargebacks. Su pregunta clave: ¿Yuno amarra la data de pay-in con la de payout (pay-ins por un MID de PayPal pagados a 12,000 creators distintos) para rastrear de la tarjeta individual al payout?

**h. EL gap de la industria (la razón por la que tomó el call).** "I found a lot of great orchestrators for pay-ins. I found a couple of pretty decent ones for payouts, but no one's tied those two things together." Ex-Uber y ex-Amazon: sabe que ahí viven los equipos de payments de cientos de ingenieros, y Eventbrite no puede pagarlos.

**i. Lock-in de Stripe Connect.** Creators atrapados: las connected accounts están acopladas a país y moneda, generan doble FX (creator canadiense con evento en US cobrando USD) y cambiar implica re-onboardear al creator. "That's just not OK. We're doing all that kind of scrambling in house right now... tape and glue to keep it going."

**j. Salir del funds flow.** Con PSD3 en camino en Europa, la agent exception desapareciendo en EU/UK y casi eliminada en Canadá, no quieren registrarse como PSP ni MSB: "we're looking for those partners that can essentially take over that role for us."

## 3. Qué respondió Yuno (y qué prometimos)

- **Pitch de Justo:** OS unificado de infraestructura financiera (pay-ins, payouts, KYC/KYB, issuing, BaaS), 500+ integraciones directas, equipos de expertos por región, reconciliación incluida en cada integración, "extensión de tu equipo de payments" (Uber, Starlink/SpaceX para negociar mejores tasas).
- **ChaseNet:** Justo afirmó que tenemos la conexión y ruteamos por BIN, más rieles de débito US (Star, Pulse, NYCE). ⚠️ Ver riesgos abajo.
- **MoR:** 85+ proveedores MoR por región (EBANX, dLocal), advisory de quién es mejor por mercado, caso OpenAI (mismo modelo US-céntrico expandiéndose global).
- **Fever como credencial de vertical:** procesamos para Fever, su gran competidor europeo. A Paul le pareció "reassuring... because live events is weird". Fever también valida el modelo de plug-in de credenciales de terceros (venues/equipos con sus propias cuentas de Banorte/Banamex).
- **Demo de Jarrett (reconciliación):** conexiones directas por proveedor en pago, payout y reconciliación; consumo de transaction + settlement reports; cross-reference capturado vs liquidado; discrepancias señaladas con target ("estas 17 transacciones llevan 2 meses sin liquidar con EBANX"). Solo vas al portal del proveedor con un caso puntual.
- **Marketplace desagregado:** KYC/KYB standalone y portable, pay-in por el acquirer que quieras, payout por TerraPay, Nium, Thunes u otros, con subasta de FX rate por API que auto-selecciona la tasa más competitiva.
- **CFO Copilot (honestidad incluida):** en beta con Fever (nació porque descubrieron doble FX entre sus dos equipos), release estimado ~2 meses. Justo fue claro: el dashboard unificado pay-in + payout con vista de tesorería aún no está; la orquestación de las partes sí.
- **Fiverr:** atascados en Adyen, les ahorramos ~$900K en 6 meses solo en FX fees de payouts.
- **Zuora:** "we power all the rails for Zuora". Paul conoce a Tien (fue de sus primeros clientes en Real Networks). Útil para el lado suscripciones de Bending Spoons.
- **Red de contactos:** Billy Chen (contrató a Paul en Uber), Peter Hazlehurst (Justo lo vio hace un par de meses), Marqeta. Justo ofreció conectar a Paul con Juan Pablo (CEO, Bay Area) para un café.

## 4. Dónde ganamos este deal

1. **Somos el único que cierra el gap pay-in + payout.** Paul lo dijo textual: nadie más lo ha resuelto. Nuestra arquitectura GoFundMe (Stripe+Adyen+Tabapay, splits, recipients, transfers) es exactamente eso, y Fever prueba que entendemos live events.
2. **Modularidad vs lock-in.** Su trauma es Stripe Connect. Nuestro pitch de KYC portable + payout provider libre + FX auction ataca el dolor exacto que describió con el creator canadiense.
3. **El pitch para Milán es de headcount, no de features.** Bending Spoons quiere correr Eventbrite con 40-50 personas. El mensaje: los marketplaces de la escala de Uber/Amazon resuelven esto con cientos de ingenieros; Yuno lo entrega como servicio. Eso es lenguaje de operating model, que es como piensa Bending Spoons.
4. **Puerta al portafolio.** Un grupo de ~50 compañías de suscripción + Zuora como referencia = orquestación transversal al portafolio como visión de segunda fase.

## 5. Gaps y riesgos a manejar (internos, no compartir)

- **⚠️ ChaseNet/JPM:** Justo afirmó en el call "we have that connection". Nuestra evidencia interna (pre-questions bank) decía que el connector JPMORGAN era mock al 2026-05-11, con integración de cards en build desde marzo. ANTES de poner nada de JPM/ChaseNet por escrito en los materiales para Milán, confirmar el estado real con Jarrett/producto. Si los materiales repiten un claim que la due diligence técnica desmiente, perdemos la credibilidad que Paul nos está prestando.
- **CFO Copilot:** está en beta y Justo dio "~2 meses" de release. En los materiales escritos, tratarlo como roadmap con fecha condicional, no como feature actual (regla de conditional promises del Q&A bank).
- **Pregunta de colusión sin respuesta completa:** Paul preguntó si amarramos data de pay-in con payouts para detectar colusión (tarjetas robadas → evento falso → payout al fraudster). La respuesta se desvió a arquitectura de payouts. Los materiales custom deben responderla explícitamente: qué señales cruzadas pay-in/payout tenemos hoy (ledger transaccional que liga cada pay-in a su recipient/payout) y qué haría el stack de fraud (Forter/Sardine/Signifyd vía Yuno) con visibilidad de ambos lados.
- **Downgrades interchange+ y retry economics:** tampoco se respondió en detalle. Incluir en materiales: reporting de downgrades a nivel transacción y reglas de retry por decline code con lógica de costo (fee de scheme vs probabilidad de recovery).
- **Nombres de Milán sin verificar:** "Noe, Giacomo, Filippo" es como suenan en el transcript. Verificar nombres completos y títulos en LinkedIn antes de cualquier email.

## 6. Next steps acordados (con dueño y deadline)

| Acción | Dueño | Cuándo |
|---|---|---|
| Paul envía su MNDA estándar | Paul | Ya (inmediato post-call) |
| Firmar el MNDA "as is", sin ida y vuelta legal | Yuno (Justo) | Apenas llegue |
| Materiales custom para que Paul comparta internamente (use cases marketplace, Fever/GoFundMe, respuestas a colusión + interchange + funds-flow exit) | Yuno | Antes del viernes 2026-08-14 |
| Pedirle data a Paul (él ofreció: "if you want some data from me, let me know, I can prepare that") | German/Justo | Esta semana, mientras sigue en la silla |
| Intro a Noe, Giacomo y Filippo (email mínimo, meeting ideal) | Paul, tras MNDA | Antes de su salida |
| Workshop en Milán aprovechando el viaje de Justo | Justo | ~3 semanas (fin de agosto) |
| Café Juan Pablo + Paul en Bay Area (relación de largo plazo; Paul queda libre y es un operador de payments serio) | Justo conecta | Post salida de Paul |
| WhatsApp directo Justo ↔ Paul activado | Hecho en el call | n/a |
