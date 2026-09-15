# Appmaking: preguntas pendientes antes de la propuesta (15-sep-2026)

**Contexto:** segunda call 15-sep-2026 (47 min, grabada). Yuno: German, Jarrett Falasco (SE), Joaquin Mann (BDM NA nuevo, observando), Sean Calabro (GM NA, en la invitación). Appmaking: Tatsiana Hubarevich (Payment Manager; firma Gubarevich por email) y Dzmitry Katsiushchyk. La propuesta NO se mostró: German quedó en una call corta (hoy o mañana) para cerrar inputs y presentarla después.
**Objetivo comercial:** el mayor volumen posible. Procesan ~500K tx/mes; su ramp llega a 150K en el mes 7, es decir ~30% del total.
**Qué consolida este doc:** las tres preguntas de Sean, la pregunta de Justo (MIDs y money flow), la sección 9 del brief del 15-sep y la sección 2 del Q&A del 14-sep, depuradas con lo que la call ya respondió.
**Orden:** lo que ya sabemos → Top 10 para la call corta → Sean 1, 2 y 3 → capabilities que usarían → volumen → qué sale de aquí para la propuesta → pre-call interno.

---

## 0. Lo que ya sabemos (no volver a preguntar)

| Tema | Lo que dijeron | Fuente |
|---|---|---|
| Ramp mes a mes | 20K, 30K, 45K, 65K, 90K, 120K, 150K tx en meses 1 a 7; AOV exacto $18; fully ramped en el mes 7 | Email Tatsiana 8-sep |
| Volumen total | ~500,000 transacciones en agosto 2026 across all providers | Call 15-sep, 15:41 |
| Qué mueve el ramp | Performance. Testean qué transacciones funcionan mejor en Yuno y a medida que lo encuentran mandan más. "We do have big volumes at the moment". Falta la métrica y el baseline | 14:30 |
| Solidgate | Sin mínimo escrito, pero se abarata con volumen, por eso concentran ahí. Justo: Solidgate está en el money flow con casi todo el flujo | 16:11, WhatsApp |
| Segundo orquestador (sin nombre) | Equipo y gateway pequeños, sin recursos; fixes lentos → caídas de aprobación y problemas de billing. Si migran algo, sería desde ellos | 17:48 |
| Un PSP por dos orquestadores | Quieren usar el mismo banco (ej. Unlimit) por el orquestador actual y por Yuno. Jarrett: posible con las mismas credenciales; el dolor es reconciliación y alertas duplicadas; opción MID separado vía partnership con Unlimit | 21:20 |
| Coverage gaps | Interés en LatAm; miran Korea y África; "many regions not processing to full capacity". Pix, Pix Automático, UPI y UPI Autopay ya integrados vía Solidgate | 20:21, 23:50 |
| 3DS | Usan el 3DS nativo de cada orquestador | 28:27 |
| Tokens | No vaultean tokens hoy; ambos proveedores son PCI. Quieren TRID propio por seguridad, ownership y flexibilidad; legal revisando. Jarrett: Yuno es TSR certificado, TRID propio en ~1 semana, tokens portables por batch file. Matiz: TRID propio = modo passthrough; ahí los network tokens son de ellos | 5:34 a 13:25 |
| Alertas | Jarrett: Ethoca y Visa RDR soportados, proyecto de mejora de pre-chargeback en curso. ⚠️ El 14-sep Verifi no estaba confirmado internamente; verificar antes de ponerlo por escrito | 3:06 |
| TC40 / SAFE | Jarrett: reportes customizables si el dato viene en el archivo. ⚠️ Internamente hoy solo dLocal vía SFTP (Leo); ninguno de sus PSPs fase 1 confirmado. Alinear con Jarrett antes de escribir | 4:17 |
| Sandbox | Probado y les gustó; "intuitively understandable" | 1:52, 25:21 |
| Entidad y mercados | Chipre. Venden global, más fuerte en USA y Europa, mucho interés en LatAm con pocas conexiones | WhatsApp con Justo |
| Demo cubierta | Routing, condiciones, decline groups, retries, failover, traffic split (commitments y A/B), smart routing, monitors con redistribución automática, checkout builder, tenant structure; subscriptions en la call 1 | 25:32 a 46:14 |
| Intro a bancos | Pregunta de Tatsiana del 8-sep. NO se tocó el 15-sep. Sigue abierta (sección 2a) | Email 8-sep |
| Próximos pasos | Call corta para cerrar datos de la propuesta ("do you need more information from me?"); canal de Slack compartido (Jarrett) | 46:14 |

---

## TOP 10 para la call corta

1. When do you want the first live transaction, and what has to be true on your side first (legal on TRID, dev capacity, signature)?
2. Rank your phase 1 markets: US, EU (which countries), LatAm (which), Japan, Korea, Africa.
3. Are the MIDs in your name or Solidgate's? Which providers do you contract directly today?
4. Of the ~500K monthly transactions, how are they split between Solidgate, the second orchestrator and direct integrations?
5. What performance result would make you move more volume to Yuno, measured against which baseline and over what window?
6. Once live, who decides routing and on what rules? Would you let smart routing run on a share of traffic?
7. Where does subscription logic live today (plans, trials, renewals, retries)? Would you run a segment on Yuno's engine?
8. How do you reconcile across Solidgate, the second orchestrator and the app stores today? Who does it and with what tools?
9. Which integration path: full SDK, lite SDK or server to server? Who builds it and when?
10. What would it take to move the second orchestrator's full volume to Yuno, and when?

---

## 1. Timelines y mercados prioritarios (Sean, punto 1)

**Para qué:** fijar el alcance de la fase 1 y el calendario. Su curva ya está; falta saber cuándo arranca el mes 1 y en qué mercados.

**Timelines**
- What is your target date for the first live transaction? Is there an internal quarter or a business event driving it?
- What is on the critical path on your side: legal review for your own TRID, engineering capacity, procurement or contract signature?
- Month 1 in your curve: is that the first month live, or the first month after integration is complete?
- How long do you expect integration and testing to take? Who is the technical owner on your side?
- Do you have any commitment with Solidgate or another provider that gates when you can start moving volume?
- Is there seasonality (for example Q4 user acquisition peaks) that affects when you want to be live?
- Who takes the final decision and who else needs to approve? When does legal (Butrym) come in?

**Mercados**
- Rank your priority markets for phase 1. Which ones go first and why?
- For each priority market, which payment methods must be live on day one: cards, Apple Pay, Google Pay, PayPal, Pix, UPI, local cards?
- Is the 150K curve Atrix only, or across brands (AstroSoul, Astroline, others)? Which funnels go first?
- For LatAm, which countries specifically, and do you plan local entities and local acquiring, or cross border from Cyprus?
- Korea and Africa: is that a 2027 plan or something you want in phase 1?
- Which entity will contract and process (Appmaking LTD, Appsella LTD, others)? Who signs?

---

## 2. Estrategia de ruteo y de partners de pago (Sean, punto 2 + Justo)

**Para qué:** saber si Yuno va a ser el cerebro de ruteo o solo rieles adicionales, y quién está en el money flow. Justo: "el tema es si los MIDs son de ellos o de Solidgate"; si son de ellos, hay que onboardearlos con procesadores y la propuesta cambia.

**2a. Money flow, MIDs y adquirencia (Justo)**
- Are the merchant IDs with your acquirers in your name or in Solidgate's name? Provider by provider: Stripe, Unlimit, Ecompay, Airwallex, Shift4, Payabl, NMI, Nuvei, Maverick, Checkout.com.
- Which providers do you contract directly, with your own contract and settlement, versus through Solidgate as aggregator or merchant of record?
- Where does settlement land per provider: which entity, which currency, which bank?
- Which providers are contracted but not live (Payabl), and why? Which would you onboard new for phase 1?
- What is the exact scope and expiry of the Solidgate exclusivity? Adyen, JPMorgan and Checkout.com were mentioned. Anything else? When does the Solidgate contract renew?
- If the MIDs are Solidgate's: which ones could you open in your own name, and how fast?
- Bank introductions (their Sep 8 question, still unanswered): which markets do you need new acquiring in, with which entity, what volume would you put on a new acquirer, and what happened with previous acquirers?
  - Respuesta honesta acordada en el brief (sección 5): Yuno tiene relaciones comerciales con los adquirentes y PSPs del catálogo, puede presentar al merchant con sus contactos y el merchant contrata directo; Yuno no es referidor pagado, no participa en underwriting ni está en el flujo de fondos. No prometer un programa formal sin acordarlo con Sean.

**2b. Ruteo después del go-live**
- Who owns routing decisions today and how often do rules change?
- What drives routing today in Solidgate and in the second orchestrator: geo, OS, BIN, cost, approval rate, provider commitments?
- Can you share two or three months of approvals and declines by geo and PSP under the NDA? Without a baseline there is no way to measure the uplift you will scale on.
- Would you run Yuno smart routing (conversion, latency, cost) on a share of traffic from day one, or start with manual rules?
- What share of each market do you plan to send to Yuno at the start, and what metric and window would scale it up?
- Which providers would sit behind Yuno, and which stay only on Solidgate?
- One PSP through two orchestrators: which providers and markets? Do you want a separate MID via our Unlimit partnership? Who reconciles the two streams?
- What retry and decline logic exists today? Do you retry across providers? Do you carry network transaction IDs for MITs?
- Would you move 3DS to Yuno's decoupled 3DS so retries can cross providers without re-authentication? Any SCA exemption strategy in the EU?
- Monitors: what approval rate thresholds would you set, and where do alerts go (email, OpsGenie, Slack)?
- Partner strategy going forward: are you looking to add local acquirers in LatAm, Korea or Africa through Yuno connections, or do you already have candidates?
- Second orchestrator: how much volume is on it, what is the timeline to phase it out, and what needs to be true for Yuno to take that volume?

---

## 3. Subscriptions y reconciliación: in-house o con Yuno (Sean, punto 3)

**Para qué:** saber si hay un módulo standalone que vender (subscriptions engine, reconciliation) o si todo queda in-house y Yuno es solo pay-in.

**Subscriptions**
- Where does the subscription logic live today: your own billing system, Solidgate's subscription product, the second orchestrator, something else?
- Which features are handled where: plans, trials, phased pricing, per-country pricing, renewals, retries, proration, cancellations?
- What share of the ~500K monthly transactions are renewals (merchant initiated) versus first payments?
- How does approval on renewals compare with first payments? Do you use account updater or network tokens on renewals today?
- Where are cards vaulted today, how many cards on file, and under whose TRID are the current network tokens?
- How do you handle failed renewals: retry schedule, dunning emails, downgrade? Who owns that logic, and how much revenue do you lose to failed renewals per month?
- Would you consider running a segment on Yuno's subscription engine (a new brand, a new market, the web funnel)? What would be must-have for that?
- Is Nova or a retry optimization layer interesting for renewal recovery? Would you want a session on it?

**Reconciliación**
- How do you reconcile today across Solidgate, the second orchestrator and the app stores? Spreadsheets, in-house tool, third party?
- Who does it and how much time does it take per month? What breaks most often? (They mentioned billing problems with the second orchestrator.)
- Which reports do you need and how often: transactional, settlement, fees, chargebacks, TC40 and SAFE, bank and fraud rates per PSP?
- Which data points must be in those reports? Who consumes them, finance or payment ops?
- Would you use Yuno reconciliation as a standalone module, and for which sources (Yuno only, or also Solidgate and the second orchestrator)?
- Chargebacks and alerts: who provides Verifi and Ethoca alerts today, through which descriptor, how many alerts a month, and what do you pay? Would you route alerts through Yuno for Yuno processed traffic only, or for everything?
- Who responds to disputes today and with what tool? How many per month? Any MID near a Visa or Mastercard monitoring threshold?

---

## 4. Capabilities de Yuno que estarían dispuestos a usar

| Capability | Lo que sabemos | Pregunta directa | Si dicen sí, va a la propuesta como |
|---|---|---|---|
| Routing rules (conditions, BIN, metadata) | Demostrado, lo entendieron | Will you manage routing yourselves in the dashboard, or want us to configure phase 1 with you? | Incluido |
| Smart routing | Demostrado; hoy hacen splits geo/OS a mano | Would you enable smart routing on a share of traffic from day one? Which share? | Incluido |
| Monitors + redistribución automática | "It looks cool"; resuelve el dolor del orquestador #2 | Which thresholds and alert channels do you want? | Incluido |
| Failover, retries, decline groups | Demostrado | What retry logic do you have today that we should replicate or improve? | Incluido |
| 3DS desacoplado | Hoy usan el 3DS de cada orquestador | Would you move 3DS to Yuno for cross provider retries? | Incluido |
| Network tokens con TRID propio (passthrough) | Interés fuerte; legal revisando; ~1 semana según Jarrett | Do you want your own TRID from day one, for all cards or renewals first? | Pendiente scoping (vault y tokens) |
| Vault agnóstico y proxy (tokens usables fuera de Yuno) | Pidieron portabilidad; no vaultean hoy | Which providers outside Yuno would consume the tokens? | Pendiente scoping |
| Subscriptions engine standalone | Demo en la call 1; hoy in-house o en Solidgate, por confirmar | Would you run a segment on our engine? | Pendiente scoping |
| Reconciliation | Reportes normalizados explicados | Would you use reconciliation standalone, for which sources? | Pendiente scoping |
| Reports (approval by provider, country, BIN; export) | Parte del dashboard | Which views does Dzmitry need for the bake-off? | Incluido |
| TC40 / SAFE, bank y fraud rates por PSP | Customizable según Jarrett; internamente solo dLocal hoy | Is TC40/SAFE on your phase 1 providers a launch requirement or a nice to have? | Scoping por proveedor |
| Verifi RDR y Ethoca | Ethoca confirmado; Verifi por verificar | Route alerts through Yuno for Yuno traffic only, or for all? | Pendiente scoping, precio aparte, no inventar |
| Fraud engine y risk conditions | No se habló | Who does antifraud today (in-house, provider)? Interested in risk conditions on routes? | Pendiente scoping |
| Checkout: full SDK, lite SDK o server to server | Tienen su propio quiz funnel UI | Which path? Who builds it? | Define integración |
| Tenant structure (accounts por región o marca) | Explicado | How do you want data split: by brand, by region, by entity? | Incluido |
| Métodos de pago y APMs nuevos | Pix y UPI ya; gaps en LatAm, Korea, África | Which APMs per priority market for phase 1? | Incluido, confirmar conectores |
| Nova y Payments Concierge (AI) | Prometidos desde el 4-sep; no se cubrieron | Do you want a 20 minute session on Nova and Concierge? | Sesión aparte |
| Marketplaces, installments | No aplica a su modelo | No preguntar | No va |

---

## 5. Volumen: cómo llegar al máximo posible

**Para qué:** 150K en el mes 7 es ~30% de lo que procesan hoy. La restricción real es Solidgate: entre más le mandan, más barato les sale, así que mover volumen a Yuno puede costarles un tramo de precio allá.

- Map the ~500K: by provider, by region, by brand, and first payments versus renewals.
- Solidgate price breaks: at what volumes does your per transaction cost drop, and how much volume do you need to keep there to hold your current tier?
- Second orchestrator: how much volume is there, and is all of it movable?
- If performance is good by month 7, what does month 12 look like? Would you commit to a target share (for example half of your volume) contingent on agreed performance results?
- Let us define "performance" together: approval rate by market and BIN, latency, cost per transaction, chargeback rate. What is the baseline from your current reports and what measurement window works for you?
- Would a price that drops per transaction as your volume grows change how fast you move volume to us?
- New markets (LatAm, Korea, Africa) are greenfield: would you route those through Yuno from day one?
- Anything contractual or technical that caps the share of volume you could send to Yuno in year 1?

---

## 6. Qué sale de aquí para la propuesta

**Modelo vigente (deck "Proposal - AppMaking + Yuno", slide 13):** platform fee + fee por transacción exitosa, ambos escalonados por banda mensual: $5,000 + $0.20 (0 a 25K) / $5,500 + $0.12 (25,001 a 50K) / $6,500 + $0.065 (50,001 a 100K) / $7,500 + $0.05 (100,001 a 150K) / $7,500 + $0.05 por tx arriba de 150K. Fully ramped $15,000/mes, $180,000/año. Sobre su curva: meses 1 a 7 $80,575, año 1 $155,575. El fixed fee del 10-sep queda como respaldo, no se presenta.

- **Arreglos pendientes en el deck antes de mostrarlo** (brief 15-sep, secciones 4.3 y 4.7): columna "Expected" → Month 1 / Months 2 to 3 / Months 4 to 5 / Months 6 to 7 / Month 8 onward; caja "What it means" → Months 1 to 7 $80,575 (520K, $0.155), Months 8 to 12 $75,000 (750K, $0.10), Year 1 $155,575 (~1.27M, $0.12). Slide 11: quitar los dos bullets heredados de FlightHub.
- **La banda arriba de 150K ahora importa:** con 500K totales, mostrar qué pasa si suben el share: 250K tx = $20,000/mes ($0.08); 500K tx = $32,500/mes ($0.065). Es el argumento para la pregunta de share objetivo de la sección 5.
- **Criterios de escalado por escrito:** convertir la respuesta a la pregunta 5 del Top 10 (métrica, baseline, ventana) en una cláusula de la propuesta. Ellos dijeron que el volumen sigue a la performance; que quede definido cómo se mide.
- **Onboarding con procesadores:** si los MIDs son de Solidgate, la propuesta incluye el plan de apertura de MIDs propios con cada PSP de fase 1 y sus tiempos. Si son de ellos, es solo conexión y credenciales.
- **Módulos standalone:** solo se cotizan los que digan que sí en la sección 4, y solo después de correr la calculadora para cada uno. El resto queda "Pending".
- **Entidad contratante y término:** Appmaking LTD o Appsella LTD (Butrym firma); preguntar qué término firmarían (12, 24 o 36 meses). Facturación en USD.
- **Fecha:** Tatsiana pidió el pricing el 8-sep, el 10-sep y hoy quedó para la call corta. Comprometer jueves 17 o viernes 18 y cumplir.

---

## 7. Pre-call interno (antes de hablar con ellos)

- **Hablar con Piotr** (Justo: "los conoce bien"): qué sabe de su setup con Solidgate, quién tiene los MIDs, y qué relación tienen con Unlimit y los demás PSPs.
- **Jarrett:** timeline formal del TRID propio (dijo "a week or so"); status real de Verifi antes de repetir lo que afirmó en la call; viabilidad del MID separado vía partnership con Unlimit; Shift4 y Payabl en el catálogo antes de repetir "full coverage".
- **Leo:** qué proveedores tienen TC40/SAFE hoy además de dLocal, para scopear contra su fase 1.
- **Sean:** frase acordada para la intro a bancos; Deal Desk del miércoles 08:00 (ARR $180K en régimen, $155.6K año 1, decisor Dzmitry con Butrym firmando).
- **Conectores por escrito** (compromiso del 4-sep, todavía pendiente): Stripe, Ecompay, Unlimit, Airwallex, Shift4, Payabl, NMI y el octavo que quedó garbled en la primera call (Nuvei, por confirmar).
- **Canal de Slack compartido:** Jarrett lo propuso en la call; crearlo hoy y mandar la invitación.
- **Mandar el Top 10 por Slack o email antes de la call corta** para que Tatsiana llegue con los números (split del volumen, MIDs, share por PSP).
