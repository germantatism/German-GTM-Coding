# Guía de la semana: 14 al 18 de septiembre de 2026

Preparada el lunes 14-sep a partir del calendario, Gmail, Gong y los archivos de cada deal. Horas en Colombia (GMT-5).

## 0. Mapa de la semana

| Día | Hora | Reunión | Quién | Prep |
|---|---|---|---|---|
| Lun 14 | 15:30 a 17:30 | Meetings Prep (tu bloque) | | Esta guía |
| Mar 15 | 9:00 a 9:45 | AppMaking + Yuno | Tatsiana, Dzmitry (Appmaking); Sean, Joaquin, Jarrett sin confirmar | Sección 1 |
| Mar 15 | 10:00 a 10:45 | Palco + Yuno, Deep Dive | Fernando, Alfonso, Alvaro (Palco); Carlos Medina, Joaquin, Magdalena | Sección 2 |
| Mar 15 | 10:45 a 11:00 | Sync before Hostinger | Piotr Sierpinski, Dirk | Sección 3 |
| Mar 15 | 11:00 (12:00 ET) | Deadline Deal Desk: deals a Tania vía Sean | | Sección 6 |
| Mié 16 | 8:00 a 9:15 | Weekly Deal Desk | Justo, GMs, Tania, Bernabé, todos los BDMs | Sección 6 |
| Jue 17 | 6:00 a 6:45 | Hostinger + Yuno, Demo | Paulius; Justo, Antoine, Dirk, Piotr, Tautvydas | Sección 3 |
| Jue 17 | 13:00 a 14:00 | Suno + Yuno, Technical Deep Dive | Gurwinder, Madden, Ben Rawstron (opcional); Justo, Sean, Jarrett sin confirmar | Sección 5 |
| Jue 17 | 13:30 a 14:00 | Forecast Call NA | Felipe, Tania, Sean, William, Melissa | ⚠️ Se cruza con Suno. Avisar a Felipe y Sean |
| Mar 22 | 10:00 a 11:00 | FlightHub In-Person, Montreal | Anna-Lena, Nick; William | Sección 4, la prep es esta semana |

Dos cosas que encontré revisando Gmail y que van primero que todo:

1. **El follow-up de Hostinger del 3-sep nunca salió.** No está en enviados ni en borradores. Paulius no tiene ni el recap ni los datos del NDA (entidad y firmante) que pidió en la call. Dejé el borrador listo en Gmail para que lo revises y lo mandes hoy.
2. **El correo post-demo a FlightHub tampoco salió.** El último correo a Anna-Lena es del 3-ago. Ella igual agendó el presencial del 22-sep. El deck de propuesta está construido sobre volúmenes estimados por nosotros. Dejé el borrador en Gmail pidiendo los tres datos que ella se comprometió a dar.

---

## 1. Appmaking (martes 9:00)

### Dónde está el deal
- Demo 4-sep hecha. Recap enviado el mismo día. Sandbox entregado y "our technical team loved it" (10-sep).
- Tatsiana mandó la curva de ramp el 8-sep y pidió el pricing por escrito; insistió el 10-sep. Tú respondiste que preferías revisarlo juntos en una call.
- Hoy 15:19 enviaste las respuestas a TC40/SAFE, TRID, alertas y lista de PSPs. Tatsiana confirmó la call de mañana.
- Lo que ellos esperan mañana: **el pricing**. Es la entrega de la call. Todo lo demás es secundario.

### Lo que prometiste para esta call (y tienes que poder responder)
| Compromiso | Dónde lo prometiste | Qué necesitas antes de las 9:00 |
|---|---|---|
| Pricing por escrito con ramp | Recap 4-sep, correos 10-sep | Slide lista y actualizada con su curva real (Deals/Appmaking/appmaking-pricing-ramp.png) |
| AI products: Payments Concierge y Nova | Recap 4-sep | Quién hace la demo. Jarrett no ha aceptado. Si no hay SE, la haces tú desde el dashboard (routing recommendation + Concierge, lo mismo que Jarrett mostró a FlightHub) |
| Intro a bancos | Correo 10-sep | Respuesta honesta acordada con Sean: qué hace Yuno realmente (relaciones con adquirentes, presentaciones cuando aplica) sin inventar un programa que no existe |
| Cobertura Visa-side de alertas y roadmap | Correo 14-sep | Status real de Verifi (RDR/CDRN). Solo Ethoca está confirmado público. No afirmar Verifi live sin confirmarlo con Jarrett o Leo |
| TC40/SAFE scopeado contra su fase 1 | Correo 14-sep | Qué proveedores lo tienen hoy (Leo: dLocal por SFTP; su ejemplo era Adyen). Ninguno está en su fase 1. Respuesta: "hoy dLocal; para Stripe, Ecompay, Unlimit, Airwallex, Shift4, Payabl y NMI lo scopeamos juntos" |
| Adquirentes locales Japón, Brasil, México | Correo 14-sep | Lista corta verificada en el catálogo del Dashboard (Japón es el más flojo: GMO, SB Payment, Univapay, Komoju sin confirmar) |

### Pricing con su curva real (ya actualizado en archivo y slide)
Curva de Tatsiana (8-sep): 20K, 30K, 45K, 65K, 90K, 120K, 150K tx en los meses 1 a 7, AOV $18. Rampean más rápido que lo dicho en la call (fully ramped en el mes 7, no en el 9).

| Escalón | Tx exitosas / mes | Mes esperado | Fee fijo / mes | All-in tope de banda |
|---|---|---|---|---|
| 1 | 0 a 25,000 | Mes 1 | $6,500 | $0.26 |
| 2 | 25,001 a 50,000 | Meses 2 a 3 | $8,000 | $0.16 |
| 3 | 50,001 a 100,000 | Meses 4 a 5 | $10,000 | $0.10 |
| 4 | 100,001 a 150,000 | Meses 6 a 7 | $13,000 | $0.087 |
| Fully ramped | Más de 150,000 | Mes 8 en adelante | $13,000 + $0.03 por tx arriba de 150,000 | Cae hacia $0.03 |

Con su curva el unitario baja todos los meses ($0.325, $0.267, $0.178, $0.154, $0.111, $0.108, $0.087). Meses 1 a 7: $68,500 por 520K tx. Año 1: $133,500 por 1.27M tx ($0.105 promedio). Régimen: $156K/año. Todo verde contra la calculadora sin aprobaciones. Detalle en Deals/Appmaking/appmaking-pricing-proposal-2026-09-10.md.

Argumento para la conversación (no para la slide): una estructura estándar (F3 $10K + ~$0.035/tx) les costaría ~$164K el año 1 y ~$183K/año en régimen; el ramp les ahorra ~$31K el año 1 y ~$27K/año después. Y en el mes 4 ya están en $0.15/tx.

### Agenda propuesta (45 min)
1. 5 min. Cierre de las respuestas de ayer: preguntas sobre TC40/SAFE, TRID, Ethoca, PSPs.
2. 15 min. Pricing: la slide. Lógica en una frase: un fee fijo all-in que sube por escalones según lo que procesan y que se detiene en 150K; el unitario cae cada mes; declinadas no cuentan; sin setup fee.
3. 5 min. Qué queda por scoping y en qué orden lo quieren: subscriptions standalone, vault y network tokens, reconciliation, Verifi y Ethoca.
4. 5 min. Intro a bancos.
5. 10 min. AI products: Payments Concierge y Nova.
6. 5 min. Next steps: ¿mandamos contrato o hacen falta más rondas? Timeline de credenciales de sus PSPs fase 1. Fecha de kick-off.

### Checklist antes de las 9:00
- [ ] 5 min con Sean antes de la call: cómo se presenta el número (final o "preliminar sujeto a contrato") y qué autoridad tiene él en vivo.
- [ ] Confirmar quién demo AI products (Jarrett o Joaquin).
- [ ] Verifi: status en una línea, confirmado.
- [ ] TC40/SAFE: proveedores que lo tienen hoy, confirmado con Leo.
- [ ] Conectores fase 1: verificar Ecompay, Payabl y NMI en el catálogo. Ya afirmaste "full coverage" dos veces por escrito.
- [ ] Correr la calculadora para Appmaking (duplicar "Yuno — Pricing Palco") para tener el score documentado antes del Deal Desk del miércoles.
- [ ] Verificar que Tatsiana esté en la invitación del calendario (aparece como needsAction; ella confirmó por correo).

### Qué no decir
No "ustedes no tienen orquestador" (tienen dos: Solidgate y otro que no nombraron). No nombrar Truegate. No incluir Adyen, JPMorgan ni Checkout.com (exclusividad Solidgate). No prometer reportes consolidados de TC40/SAFE. No dar precios de subs, vault ni recon sin correr la calculadora. No "no small feat".

---

## 2. Palco (martes 10:00)

### Dónde está el deal
- Demo y payment orchestration review el 9-sep (grabada por Fireflies de Magdalena, no en Gong). Patricio, Fernando y Javier del lado de ellos.
- Follow-up tuyo el 10-sep con tres opciones; Fernando confirmó hoy el martes 10:00. Invitación enviada.
- Patricio dijo el 2-sep: "septiembre es cuando estaremos definiendo el camino a seguir en nuestro orquestamiento de pagos". El competidor real es su roadmap interno.

### Quién está en la sala mañana
| Persona | Lado | Rol | Nota |
|---|---|---|---|
| Fernando Nava Feldman | Palco | Firma como **Technical Account Manager, Palco México (CDMX)** | Patricio lo presentó como VP of Engineering. Es quien coordina y quien te confirmó |
| Alfonso Uribarri Carrasco | Palco | Co-fundador de Palco4 (2017), Manager of Development and Support, Madrid (RocketReach, sin segunda fuente) | Aceptó. Es quien construyó y mantiene las 50+ integraciones. El más sensible a cualquier frase que suene a "reemplazar" |
| Alvaro (alvaro@pal.co) | Palco | Desconocido | Sin responder. Preguntar su rol al abrir |
| Patricio Villalobos | Palco | CEO y co-dueño | **No está en la invitación.** Mantenerlo en el loop con el recap |
| Javier Sánchez | Palco | SSE | Fuera de la oficina del 14-sep al fin de mes |
| Carlos Medina | Yuno | Solutions | Lleva la parte técnica |
| Joaquin Mann, Magdalena Torrealba | Yuno | | Magdalena es la dueña de la relación |

### Qué vamos a hacer (agenda, 45 min)
Los cuatro puntos que tú mismo pusiste en el correo del 10-sep, más el discovery de negocio que quieres sacar:
1. Arquitectura de integración: API directa vs SDK, y alcance PCI de cada opción (Carlos).
2. Split payments con el promotor como merchant of record, y tokenización para abonos y cobros recurrentes.
3. Ruteo y reintentos en México, con reglas por BIN para las preventas bancarias.
4. Cobertura de procesamiento local en Bolivia y Venezuela (Line VE aprueba 8.7%).
5. Discovery de negocio: márgenes, cómo ganan dinero, quién es el cliente, cómo escalan (tú).

Sugerencia de orden: abrir con 10 min de discovery de negocio (punto 5) antes de la parte técnica. Con Alfonso y Fernando en la sala, la conversación se va a lo técnico rápido y después no vuelve.

### La información que tienes que sacar

**A. Márgenes y cómo ganan dinero**
- ¿Cuánto cobran por ticket vendido y cómo está estructurado (fijo, %, mixto)? ¿Varía por país o por tenant? (El registro mercantil implica €0.10 a €0.19 por ticket sobre 8M tickets; es inferencia, confirmar.)
- ¿Ganan algo hoy con los pagos? ¿Hay markup sobre el processing fee del tenant o el tenant le paga directo al procesador y Palco no ve un peso de eso?
- ¿Quién paga el processing fee y a quién: el tenant al procesador (MoR) o Palco factura y repasa?
- ¿Qué porcentaje del revenue viene de fee por ticket vs SaaS vs otros (pinpad, access control, CRM)?
- ¿Cuánto les cuesta mantener las 50+ integraciones? Personas, horas al mes, incidentes en on-sales.

Por qué importa: si hoy no monetizan pagos, la propuesta se vende como línea de ingreso nueva (30 bps sobre $457M ≈ $1.37M/año contra ~$220K/año de Yuno), no como costo. Si ya tienen markup, el pitch es que Yuno lo hace defendible y escalable.

**B. Quién es el cliente subyacente**
- ¿Los tenants son promotores, venues, o ambos? ¿Cuántos tenants activos? ¿Concentración: cuánto del GTV está en los 10 más grandes?
- ¿Quién elige y negocia el procesador por tenant: Palco o el tenant?
- ¿Quién firmaría con Yuno: Palco como cuenta multi-tenant o cada tenant? ¿Cómo lo imaginan comercialmente?
- ¿Cómo onboardean un tenant nuevo hoy (KYC, alta con el procesador, tiempo hasta el primer cobro)?
- Para el split: ¿el tenant cobra y Palco retiene su fee al capturar, o Palco cobra y liquida al tenant? Esto define si el modelo de marketplace de Yuno aplica directo o invertido. Carlos no debe improvisar la respuesta; si no está confirmado por procesador mexicano, se lleva de tarea.

**C. Escala**
- Nuevos mercados 2026 y 2027 (el plan post-adquisición decía "más LatAm a mediados de 2026"). ¿Cuáles y qué les falta en cada uno (procesador local, entidad, método)?
- Picos: Bad Bunny RD fueron tres sellouts en 8 horas. ¿TPS pico? ¿Qué pasa con el procesador en pico? ¿Hay fallback hoy?
- Reconciliar el volumen: $37.09 es ticket promedio y la orden lleva ~4 tickets (~$148); la tabla de procesadores da ~257K tx/mes, no 235K. Preguntarlo directo, cambia el take rate del pricing de 21 bps a ~5 bps.
- Piloto: ¿México, los tres rails de tarjeta (Openpay 58.0%, Banorte 59.6%, Santander 56.1%)? ¿Baseline y fecha de revisión?
- Decisión: ¿quién decide build vs Yuno (Patricio, Bocel)? ¿Cuándo? ¿Qué tendría que ver Fernando para recomendar Yuno?

**D. Técnico (para que Carlos lo lleve)**
- Cómo está construida la capa de pagos: ¿una abstracción única con configuración por tenant (se ve `PaymentsAjax.getCompanyPaymentMethod` en el HTML de sus tiendas) o cada integración aparte?
- 3DS al 100% de las tarjetas: ¿decisión de quién (adquirente, tenant, Palco)? Es probablemente la palanca más grande de aprobación en México.
- Tokenización hoy: ¿guardan PAN? ¿AOC PCI vigente? ¿SAQ-D? (No se encontró certificación pública.)
- Abonos y recurrencia: ¿con qué procesadores mexicanos hacen recurrente hoy?
- Reconciliación: ¿cómo concilian 50+ procesadores por N tenants?
- Fraude y contracargos: Patricio dijo que no tienen dato consolidado. ¿Herramienta de fraude? ¿Quién responde disputas?

### Qué llevar y qué no
- Llevar la aritmética de sus propios datos: Mercado Pago wallet 92.1% vs tarjeta 67.9% por el mismo proveedor; tres rails MX combinados 58.5% contra ~72% del mercado mexicano; +2 puntos en MX son ~20K transacciones y ~$743K de GTV al año.
- El pricing ($10K + ladder ≈ $18.3K/mes) no se presenta en esta sesión técnica salvo que lo pidan; se confirma después de reconciliar volumen.
- GoFundMe como referencia de marketplace solo en genérico, salvo permiso.
- Nunca decir que les falta orquestador: "ustedes construyeron la parte difícil; nosotros la mantenemos viva y le ponemos el cerebro encima".

### Cierre que buscas
Alcance de piloto en México con baseline y fecha de revisión, un dueño técnico nombrado del lado de Palco, y Patricio de vuelta en la siguiente reunión con la propuesta comercial.

---

## 3. Hostinger (sync martes 10:45, demo jueves 6:00)

### Primero: el correo que no salió
El recap del 3-sep con los datos del NDA (entidad YUNO TECNOLOGIAS S.A.P.I. DE C.V., firmante Diego Felipe Alonso Cruz) nunca se envió. Paulius pidió esos datos en la call para que su legal arrancara. Borrador listo en Gmail (asunto "Hostinger + Yuno: Call Recap and Next Steps", cc Justo). Mandarlo hoy.

### Sync del martes con Piotr y Dirk (15 min): qué cerrar
1. Quién conduce la demo (Dirk) y en qué ambiente: sandbox con conexiones parecidas a las de ellos (Stripe, Adyen, Checkout.com) para que el fallback se vea real.
2. Los compromisos del 3-sep: Justo debía mandar material de vault standalone, status de India (token portability UPI vía el GM local) e info de Revolut Pay y la notificación de Mastercard de tarjeta fondeada; Dirk debía confirmar que el retry timing opera dentro de su ventana de dunning. Nada de eso aparece enviado. Definir qué se muestra el jueves y qué se manda después.
3. El ask al final de la demo: Paulius quiere decidir vault standalone este año. ¿Proponemos una propuesta comercial de vault standalone + India, o un PoC acotado? Piotr decide con Justo.
4. Quién cubre India (¿Tautvydas? ¿el GM de India en vivo?).
5. NDA: si Paulius no lo ha mandado el martes, Piotr o Justo lo empujan por su lado.

### Demo del jueves: cómo darle más impacto (vaulting, tokens, routing)
Paulius es técnico, ya lo sobrevendieron antes y pregunta por los modos de falla. Cada bloque debe mostrar el flujo real, no slides.

**Vault standalone (el centro del deal)**
- Un token del vault cobrando por dos PSPs distintos en vivo (Stripe y Adyen, por ejemplo). Esa es la imagen de "business continuity" que él quiere ver.
- Migración de tokens hacia Yuno desde su vault actual: proceso, tiempos, qué porcentaje llega con network transaction ID (era la respuesta débil 2.4 del RFP).
- Portabilidad de salida: cómo exporta sus tokens si un día se va. Él va a preguntar. Responder sin rodeos.
- Proxy PCI y permisos: quién puede ver PAN y quién no (Antoine lo mencionó en la call).
- Infraestructura: regiones (2 US, 1 EU, 1 APAC, KSA, India), NOC 24/7. Justo ya lo dijo; ahora mostrarlo.

**Network tokens y account updater**
- Provisioning Visa y Mastercard con TRID propio o de Yuno. Account updater solo Visa y Mastercard: **no afirmar Amex**.
- Card-on-file sobre 60 a 70% del revenue: el argumento es renovaciones que sobreviven reemisión de tarjeta.
- Matriz de aceptación de network tokens y de network transaction ID scopeada a sus PSPs reales (Stripe, Adyen, Checkout.com, Razorpay, BillDesk). Convierte las respuestas "on request" del RFP en la parte más hecha a la medida.

**Routing y retries**
- Reglas por país, BIN, emisor; fallback automático cuando un PSP falla.
- El modelo de timing de retries: mover el intento dentro de su ventana de dunning (jueves a viernes sí; "una semana después" no sirve, lo dijo textual). Dirk tiene que confirmar esto antes, no en vivo.
- Batches de renovación que disparan reglas de fraude en los PSPs: mostrar cómo se reparte la carga.
- Retries en producción topados en 5: decirlo si preguntan, no esconderlo.

**Subscriptions engine (breve)**
- Están migrando billing in-house, así que el pitch no es "reemplacen Chargebee". Es "nosotros ejecutamos el cobro y optimizamos el momento dentro de su calendario". Mostrar planes y meters solo si sobra tiempo.

**India**
- Una integración sobre Razorpay + BillDesk con un solo journey. UPI Autopay.
- Status del mandato de portabilidad de tokens UPI: Justo dijo en la call que Razorpay lo tendría este año. Verificar con el GM local antes de repetirlo por escrito.

**Agentic**
- Antoine: update de MPP y x402. Paulius prioriza stablecoins sobre rieles de tarjeta.

### Qué no decir
No mencionar la evaluación anterior fallida de Yuno salvo que él la saque. No nombrar ProcessOut ni Credorax/Finaro/Shift4 preventivamente. No decir que hay SDKs de backend (fue corregido antes de enviar el RFP). No prometer Amex en account updater.

---

## 4. FlightHub (presencial martes 22, la prep es esta semana)

### Estado
- Demo 2-sep hecha (Jarrett, tú, Anna-Lena sola). Ella pidió el cost estimate y se comprometió a conseguir el volumen. Tú quedaste en mandarle un correo con los tres datos: número de transacciones al mes, approval rate actual y ticket promedio. **Ese correo no salió.** Borrador listo en Gmail (reply al hilo "FlightHub + Yuno | Next Steps", cc Nick, William, Justo, Jarrett).
- Anna-Lena agendó "Yuno x Flighthub - In-Person" el 22-sep 10:00 a 11:00 COT en 3333 Boulevard Côte-Vertu Ouest, Suite 600, Saint-Laurent (sala SR-71 con Meeting Owl y TV). Nick está invitado. William aceptó. Justo opcional. En su invitación tú figuras como opcional.
- Decisión pendiente: ¿viajas a Montreal o va William con Jarrett y tú entras remoto? Definirlo esta semana con Sean y William.

### Slides
- Ya existe el deck "Proposal - FlightHub + Yuno" en Drive (~20 slides: Why Yuno, Business Case de 2 slides, Pricing con platform fee $10K + ladder $0.0333 / $0.0292 / $0.0260).
- ⚠️ Todo el business case y el pricing están sobre **volúmenes estimados por nosotros** (700K tx/mes, $580 ticket). Sin los datos reales de Anna-Lena, el deck del 22 es una hipótesis. Por eso el correo es la prioridad de la semana.
- Cuando lleguen los datos: recalcular pricing (Deal Calculator "Yuno — Pricing FlightHub") y los cuatro levers del BC.
- Revisar que el fix "CPD" a "FlightHub" en el slide de "Why we believe Yuno is the right partner" quedó aplicado.

### Demo
- Presencial con Anna-Lena: lo que le importa es ML routing por BIN y procesador (preguntó si ya tenemos modelos que predigan qué BIN aprueba mejor en qué procesador), routing recommendation, condition sets, network tokens (no tienen, procesan PAN cifrado) y vault.
- Ejemplos vivos que ya funcionaron con Nick: metadata de Uber para VIPs; tarjetas US de expats en Amazon México ruteadas como domésticas.
- Frame permanente: Yuno se pone encima del motor de reglas que ella heredó y está evolucionando, no lo reemplaza.

### Información a extraer el 22
- Volumen de transacciones por mes (en cantidad, no en dólares) y ticket promedio real.
- Approval rate baseline total y por procesador (Chase Paymentech, Stripe, Nuvei, Airwallex, Adyen, Braintree, ConnectPay).
- Mix de volumen por procesador y por entidad/país.
- MDR blended y cómo miden costo (los dos KPIs de Nick: "lower my cost and accept more").
- Qué recupera hoy su fallback en cascada y cuánto se pierde en la última caída.
- Roadmap del build interno: el motor de rotación de BIN/emisor para pagar a aerolíneas (lado issuing).
- Proceso de decisión: quién decide (Nick), presupuesto, timing, qué tendría que ver Anna-Lena para recomendar.
- Payouts: ConnectPay, Wex entrando, Adyen y Airwallex. ¿Es un segundo deal?

---

## 5. Suno (jueves 13:00)

No estaba en tus notas pero está en el calendario. Lo mínimo:
- Technical deep dive pedido por Gurwinder el 3-sep. Madden estuvo fuera la semana del 7. Ben Rawstron entra como opcional (nuevo, verificar quién es).
- ⚠️ **Sin notetaker ni Gong.** Madden pidió explícitamente no grabar el 7-ago y el Notetaker grabó igual. No repetirlo. Avisar a Justo y Sean antes.
- ⚠️ Se cruza con el Forecast Call NA (13:30). Avisar a Felipe y a Sean; Sean está en las dos.
- NDA pendiente por WhatsApp con Madden.
- Pedidos abiertos de Madden: case studies de migración desde Stripe y reference calls (Justo lo ofreció). Llevarlos.
- Agenda sugerida: arquitectura de una capa encima de Stripe (sin rip and replace), retry scheduler vs el de Stripe ("Stripe has a really bad retry scheduler", dicho por Madden), Japón/PayPay recurrente, Pix Automático y UPI Autopay, network tokens, web checkout vs IAP con RevenueCat.
- Confirmar quién hace la demo técnica (Jarrett no ha aceptado).

---

## 6. Internas: Deal Desk (miércoles 8:00) y Forecast (jueves)

Reglas del Deal Desk (invitación de Justo): deals a Tania vía Sean antes del **martes 12:00 ET**; califican los que están en Proposal Issued o más adelante con cierre este trimestre, o sin movimiento de etapa en 14 días; se llega con un ask, no con un status; sin slides; Tania ordena por ARR.

Candidatos y el ask de cada uno:

| Deal | Etapa real | Ask concreto |
|---|---|---|
| Appmaking | Propuesta se presenta el martes 9:00 | Si el número queda aceptado en principio: contrato y kick-off. Si no: nada para el desk todavía |
| Palco | Deep dive técnico martes 10:00; pricing modelado verde | Permiso para usar la referencia GoFundMe con Palco; un dueño de solutions (Carlos) con fecha para la respuesta de split con MoR invertido por procesador mexicano |
| Hostinger | Demo jueves; decisión de vault este año | Que Justo entregue el material de vault e India antes del jueves; definir si se propone vault standalone + India como deal propio y a qué precio |
| FlightHub | Presencial 22-sep; propuesta construida sobre estimados | Aprobación de viaje a Montreal (o confirmar William + Jarrett); executive touch de Justo con Nick el 22 |
| Suno | Deep dive jueves; NDA pendiente | Un cliente de referencia para migración desde Stripe (Justo lo ofreció el 7-ago) |

Forecast Call NA del jueves: Excel de pipeline actualizado con el formato de Sean (target vs forecast, gap, plan) y close dates de estos cinco. Como se cruza con Suno, mandarlo por escrito antes.

---

## 7. Orden sugerido para el bloque de hoy (15:30 a 17:30)
1. Revisar y enviar el borrador de Hostinger (5 min).
2. Revisar y enviar el borrador de FlightHub (5 min).
3. Appmaking: mensajes a Sean (número y presentación), Jarrett o Joaquin (demo AI), Leo (proveedores TC40/SAFE) y Jarrett (Verifi) para tener respuestas mañana a las 8:30 (15 min).
4. Appmaking: repasar la slide y la propuesta actualizada (15 min).
5. Palco: mandar a Carlos Medina la lista técnica de la sección 2D y los cuatro puntos de agenda para que llegue preparado (10 min).
6. Deal Desk: decidir con Sean qué se sube mañana antes de las 11:00 (10 min).
7. Suno: avisar a Justo y Sean lo del notetaker y el cruce con el forecast (5 min).
