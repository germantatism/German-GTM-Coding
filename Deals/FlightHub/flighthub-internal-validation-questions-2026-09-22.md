# FlightHub · preguntas internas a validar tras el presencial del 22-sep-2026

Fuente: notas de Will Wong de la reunión en Montreal con Nick y Anna-Lena. Lectura de Will: todo es precio y el trade-off build interno vs orquestador. Call positiva.

## Chargebacks y disputas (Jarrett / producto)
1. ¿Qué tenemos hoy de chargeback y dispute management en el dashboard? ¿Solo visibilidad y alertas, o también gestión del caso: evidencia, representment, aceptar o disputar?
2. ¿Podemos orquestar chargebacks a través de sus 7 proveedores (Chase Paymentech, Stripe, Nuvei, Airwallex, Adyen, Braintree, ConnexPay)? ¿De cuáles ingerimos los chargebacks por webhook y los normalizamos en un solo lugar?
3. ¿Existe API de chargebacks (listar disputas, subir evidencia, responder)? ¿Para qué proveedores está soportada?
4. Ellos ya tienen proveedor de chargebacks. ¿Podemos alimentarlo (webhooks o export) o convivir con él sin duplicar alertas?
5. Chargeback alerts (Ethoca + Verifi): ¿cómo se enrolan los MIDs y descriptors de 7 proveedores, quién es titular del contrato con Ethoca y Verifi, qué match rate esperamos, qué pasa con las alertas unmatched, y la RDR de Verifi va vía PSP como en Appmaking?

## Retries (Jarrett / producto)
6. Instant retries: ¿reintento en el mismo proveedor o cascada al siguiente, sobre qué decline codes o grupos, y con qué tope de intentos?
7. Delayed retry por ruta: ¿se puede configurar un delay (segundos o minutos) antes de reintentar en una ruta? ¿Existe en routing o solo en subscriptions (smart retries programados)? Si no existe, ¿está en roadmap y cuándo?
8. ¿Cómo evitamos doble autorización o doble cobro cuando un intento hace timeout y se reintenta (idempotencia, void automático)?

## A/B testing de rutas (Jarrett)
9. Volume split por porcentaje: ¿se puede correr sobre un condition set específico, varios experimentos a la vez, y con asignación aleatoria por transacción o sticky por cliente?
10. ¿Qué reporting da el dashboard por variante (approval rate, latencia, costo) y se puede exportar para que Anna-Lena lo analice ella misma?

## Payment links (Jarrett / producto)
11. ¿Qué cubre hoy lo que mostramos como payment links (link único vs reutilizable, expiración, branding, métodos)? ¿Está incluido en la platform fee o se cobra como pay-in normal?

## Network tokens y vault (Jarrett / producto)
12. ¿Cuáles de sus 7 proveedores aceptan network tokens emitidos por Yuno y cuáles caen a PAN? El deck dice "across all seven providers".
13. ¿Qué evento exacto factura "token created" y "token updated"? Necesito el conteo esperado para estimar el add-on.
14. Migración de sus PANs cifrados al vault: ¿bulk import, formato, tiempos? ¿El vault sigue gratis con orquestación (la policy dice $0 bundled)?

## Reconciliación (Thiago de Souza / producto)
15. ¿Qué es una "transacción conciliada" a efectos de facturación: pay-in exitosa, o también refunds, chargebacks y payouts?
16. ¿Tenemos settlement reports configurados para sus 7 proveedores, incluido ConnexPay (acquiring e issuing)? ¿Fee y settlement recon está GA? En QA de decks figura como no GA.

## Uptime y single point of failure (infra / CTO)
17. Uptime real de los últimos 12 meses y SLA contractual (el apéndice dice 99.99%): ¿qué número podemos poner por escrito y con qué créditos?
18. ¿Qué pasa si Yuno se cae: multirregión, failover, RTO y RPO, status page, incidentes y post-mortems del último año?
19. ¿Podemos proponer un modo de contingencia donde su capa de routing actual llame directo a los PSPs si Yuno no responde? ¿Quién de Yuno (Edwin, Rik, infra) hace la sesión con Nick?

## Pricing (Sean / Finance)
20. Network tokens a $0.005 / $0.01 y recon 200K por $1,500 están bajo mínimo de la policy: ¿pedimos aprobación roja (CFO + CRO, 5 días hábiles) antes de enviar, o ajustamos?
21. Platform fee $9K + mínimo $25K: Sean dijo que normalmente es uno u otro. ¿Lo mantenemos o dejamos solo uno para responder al "todo es precio"?
22. Nova AI no les interesó: ¿lo quitamos de la slide en vez de dejarlo pending?
