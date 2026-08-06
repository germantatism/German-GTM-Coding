
# Intro Reply: respuesta de German a las intros de Magdalena

## Contexto

Magdalena Torrealba (SDR de Yuno, `magdalena.torrealba@y.uno`) incluye a German
(`german.tatis@y.uno`, Account Executive de Yuno) en su cadence. En cierto punto
le escribe al lead un email presentando a German: el lead va en TO, German va en CC,
y el cuerpo dice algo como "introduce you to German" / "presentarte a German".

Este skill convierte esa intro en una respuesta de German: corta, tailored al rol
del lead, aprobada por Magdalena antes de enviarse. **Nunca se envía nada al lead
sin el OK explícito de Magdalena.**

## Configuración

- `MAGDALENA` = magdalena.torrealba@y.uno
- `GERMAN` = german.tatis@y.uno (la cuenta de Gmail conectada; todo se envía desde aquí)
- Dominio interno: `y.uno`. Un "lead externo" es cualquier destinatario cuyo dominio NO sea y.uno.
- Labels de estado en Gmail (crearlos si no existen con la herramienta de labels):
  - `Milo-Intros/pendiente-ok` = borrador enviado a Magdalena, esperando su OK
  - `Milo-Intros/enviada` = respuesta final ya enviada al lead
  - `Milo-Intros/descartada` = hilo evaluado y descartado (no era intro, o German decidió no responder)

## Cada ejecución corre DOS flujos, en este orden

### Flujo A: detectar intros nuevas y pedir OK

1. **Buscar candidatos** en Gmail:
   `from:magdalena.torrealba@y.uno cc:german.tatis@y.uno newer_than:4d`
2. **Filtrar**. Procesar un hilo solo si cumple TODO:
   - Al menos un destinatario en TO tiene dominio distinto de y.uno (ese es el lead).
   - El hilo NO tiene ningún label `Milo-Intros/*` (si lo tiene, ya fue procesado: saltar).
   - El último mensaje del hilo es el de Magdalena presentando a German. Señales de intro:
     "introduce you to German", "introducing German", "presentarte a German",
     "conectarte con German" o equivalente. Si German va en CC pero no es una intro,
     aplicar label `Milo-Intros/descartada` y seguir.
   - Si el lead ya respondió después de la intro, NO automatizar: avisar a German en el
     reporte para que responda él directamente, y aplicar `Milo-Intros/descartada`.
3. **Leer el hilo completo** (no solo el último mensaje). Extraer: nombre del lead,
   empresa, cargo si aparece (firma, contexto), qué le mandó ya Magdalena (business case,
   números, CTA propuesto). Esto evita repetir lo que el lead ya recibió.
4. **Investigar al lead** con búsqueda web:
   - Buscar `"{nombre completo}" {empresa} LinkedIn` y fuentes públicas (sitio de la
     empresa, prensa, podcasts). LinkedIn suele estar tras login: usar lo que sea visible
     públicamente. Si no se encuentra nada, usar el cargo de la firma del email o del
     contexto del hilo.
   - Objetivo: cargo real + 1 dato de contexto útil (scope del rol, mercado, iniciativa).
   - **Nunca inventar datos.** Si no se puede verificar algo, se omite.
5. **Clasificar el buyer persona** del lead usando el ANEXO 1 de este documento
   (13 personas). Elegir el más cercano por cargo y scope. El persona define el ángulo
   de valor del mensaje.
6. **Redactar la respuesta de German** siguiendo las reglas de redacción de abajo y el
   ejemplo del ANEXO 2 de este documento.
7. **Pedir el OK a Magdalena**: enviar un email NUEVO (hilo aparte, nunca en el hilo del
   lead) desde la cuenta de German:
   - TO: magdalena.torrealba@y.uno
   - Subject: `[MILO] OK intro: {Nombre del lead} ({Empresa})`
   - Body:

     ```
     Hola Magda, este es el borrador de la respuesta de German para tu intro
     con {Nombre} ({Empresa}, {cargo detectado}) en el hilo "{subject original}".

     ---BORRADOR---
     {texto completo del borrador}
     ---FIN BORRADOR---

     Dos opciones:
     1. Responde "OK" y lo envío tal cual en el hilo original.
     2. Responde con la versión final completa corregida y enviaré exactamente ese texto.

     Ref: {threadId del hilo original}
     ```
8. **Marcar estado**: aplicar `Milo-Intros/pendiente-ok` al hilo original del lead.
   Nunca enviar dos solicitudes de OK por el mismo hilo.

### Flujo B: procesar aprobaciones de Magdalena y enviar

1. **Buscar respuestas** de Magdalena en los hilos de aprobación:
   `from:magdalena.torrealba@y.uno subject:"[MILO] OK intro" newer_than:7d`
2. Para cada hilo de aprobación cuyo hilo original siga en `Milo-Intros/pendiente-ok`,
   leer el ÚLTIMO mensaje de Magdalena e interpretarlo:
   - **OK simple** ("OK", "ok", "dale", "listo", "approved", "enviar", "👍" o similar,
     sin texto de email nuevo): recuperar el borrador exacto de entre los delimitadores
     `---BORRADOR---` / `---FIN BORRADOR---` del primer mensaje del hilo de aprobación
     y ese es el texto a enviar, sin cambios.
   - **Versión corregida** (su respuesta contiene un email completo o un texto sustancial
     distinto al borrador): el texto a enviar es el de Magdalena, **VERBATIM**. No
     corregir, no completar, no mejorar. Tomar solo su texto nuevo (excluir la cita del
     mensaje anterior y su firma).
   - **Ambiguo** (comentarios tipo "cámbiale el CTA", preguntas, instrucciones parciales):
     NO enviar. Responderle en el mismo hilo pidiendo el OK explícito o la versión final
     completa. Si la instrucción es clara y puntual, se puede responder con un nuevo
     borrador ajustado entre los mismos delimitadores y esperar su OK.
3. **Enviar la respuesta al lead**: localizar el hilo original con el `Ref:` del hilo de
   aprobación y responder DENTRO de ese hilo, desde la cuenta de German:
   - TO: el lead. CC: Magdalena. Mantener el subject del hilo (Re: ...).
   - Body: el texto aprobado, tal cual.
4. **Cerrar el ciclo**:
   - Quitar `Milo-Intros/pendiente-ok` y aplicar `Milo-Intros/enviada` al hilo original.
   - Responder en el hilo de aprobación: "Enviado ✅".
5. **Fallback si el conector de Gmail no permite enviar correos** (solo crear borradores):
   crear el borrador final como respuesta en el hilo correspondiente, dejarlo listo, y
   reportar a German que el borrador está esperando un clic en Enviar. Decirlo
   explícitamente en el reporte; nunca afirmar que algo "se envió" si solo quedó en borrador.

## Reglas de redacción (voz de German)

- **Idioma**: el mismo del hilo original (las intros de Magdalena suelen ser en inglés).
- **Largo**: 60 a 110 palabras. Corto gana. Es una respuesta de intro, no un pitch.
- **Estructura**:
  1. Una línea agradeciendo a Magda ("Thanks Magda." o equivalente).
  2. Saludo directo al lead + 1 línea de credibilidad: German estuvo detrás del análisis
     que Magdalena ya compartió (eso dice la propia intro de Magda).
  3. 1 o 2 frases de valor tailored al buyer persona del lead: qué le importa a ese rol
     y qué aporta German en esa conversación. Concreto, no genérico.
  4. CTA que refuerce el que Magda ya propuso (el call de los tres). Si Magda propuso
     día, confirmarlo y ofrecer horas. Tono de facilitar, no de presionar.
  5. Cierre simple: "Best," + "German".
- **Tono**: senior, sobrio, seguro. German es el AE que lleva las conversaciones grandes;
  no suena a vendedor persiguiendo, suena a la persona que el lead va a querer en la sala.
- **Prohibido**:
  - Em-dashes y " - " como puntuación. Usar comas o puntos.
  - La frase "no small feat".
  - Inventar números, datos o afirmaciones sobre la empresa del lead. Solo lo verificado
    en el hilo o en la investigación. Ante la duda, omitir.
  - Repetir el pitch o los bullets que Magdalena ya mandó (el lead ya los tiene).
  - Name-dropping de clientes salvo que un caso sea directamente relevante al persona
    y a la industria del lead (máximo uno).

## Reglas de seguridad (no negociables)

1. NUNCA enviar nada al lead sin OK explícito de Magdalena en el hilo `[MILO]`.
2. NUNCA pedir OK dos veces por el mismo hilo (verificar labels antes de actuar).
3. La versión corregida de Magdalena se envía VERBATIM, sin ningún cambio.
4. Todo envío al lead va DENTRO del hilo original de la intro, nunca en un hilo nuevo.
5. Ante cualquier ambigüedad, error o caso raro: no actuar sobre el lead; reportar a
   German y, si aplica, preguntar a Magdalena.
6. Al final de cada ejecución, reportar en una línea por hilo: qué se detectó, qué se
   envió a aprobación, qué se envió al lead, qué quedó pendiente.

## Recursos

- ANEXO 1: los 13 buyer personas de Yuno con pains, KPIs y ángulo
  de valor. Usar SIEMPRE para elegir el ángulo del mensaje.
- ANEXO 2: una intro real de Magdalena (Lowe's) y un ejemplo de
  respuesta con el tono correcto. Es referencia de tono y estructura, no plantilla literal.

# ANEXO 1

# Buyer personas de Yuno (13)

Cómo usarlos: clasifica al lead en el persona más cercano según su cargo y scope.
El persona define qué le duele, qué mide y qué ángulo de Yuno le habla. El mensaje de
intro toma UNA idea de ese ángulo (la más relevante al contexto del hilo), no la lista
completa. Nunca inventar datos de la empresa del lead.

## CFO
Prioridad: rentabilidad y eficiencia. Pains: costos de pago altos, revenue perdido por
declines/chargebacks, conciliación manual, carga de compliance, demasiados vendors.
KPIs: Cost of Payments, Operating Margin, Cash Flow, Fraud/Chargeback Rates, ROI.
Ángulo Yuno: reducir fees vía smart routing, recuperar revenue vía approval uplift,
conciliación unificada, control de fraude/compliance, consolidación de vendors.
Proof stat: 5-20% approval uplift + ahorro por consolidación de vendors.

## VP / Head of Payments
Prioridad: performance y confiabilidad. Pains: múltiples proveedores, approval rates
bajos, rollout lento de métodos, ops manuales, riesgo de escalabilidad. KPIs:
Authorization Rate, Success Rate por región, costos de transacción, # métodos
soportados, uptime, fraude/chargebacks, conciliación de settlements. Ángulo Yuno:
smart routing + dynamic retries para approvals, habilitar métodos sin integración,
retries/conciliación/settlement automatizados, dashboards en tiempo real (approval por
región, salud de proveedores), alta disponibilidad.

## CCO (Chief Commercial Officer)
Prioridad: revenue y crecimiento global. Pains: ventas perdidas por declines, expansión
de mercados difícil, presión competitiva en checkout, visibilidad fragmentada, fricción
de checkout que golpea loyalty, falta de métodos locales que limita conversión. KPIs:
Revenue Growth, Conversion Rate, Market Expansion, CLV, Profit Margin. Ángulo Yuno:
approval uplift vía routing, 1,000+ métodos en 190+ países para expandir más rápido,
checkout unificado más fluido, visibilidad centralizada, capa de orquestación (sin
necesidad de reemplazar proveedores actuales).

## Engineering Leads (CTO / VP Eng)
Prioridad: sistemas escalables, seguros y eficientes. Pains: sobrecarga de
integraciones, mantenimiento/tech debt, carga PCI, escalar in-house consume tiempo de
ingeniería. KPIs: Development Velocity, Uptime/Reliability, Security/Compliance,
Resource Allocation, Scalability. Ángulo Yuno: un API reemplaza integraciones
fragmentadas, Yuno asume mantenimiento/compliance/PCI/tokenización, escalabilidad
cloud-native, entrega de features más rápida. Libera a los ingenieros para el core.

## CPO (Chief Product Officer)
Prioridad: UX fluida e innovación rápida. Pains: integraciones de pago lentas, fricción
en checkout, drenaje de ingeniería, experiencias globales inconsistentes, seguridad
compleja. KPIs: Feature Delivery Speed, Checkout Conversion, User Satisfaction,
Retention/Churn, cobertura global de features. Ángulo Yuno: lanzamientos de payment
features más rápidos, one-click/saved cards, suscripciones fáciles (tokenización +
retries automáticos), UX global consistente vía una capa de orquestación, seguridad y
compliance delegados.

## Marketing / Growth Leaders
Prioridad: adquisición, conversión, retención. Pains: carritos abandonados, opciones de
pago limitadas, fricción que desperdicia ad spend, fallas en pagos recurrentes que
cortan LTV, sin data de pagos para campañas. KPIs: Conversion Rate, Cart Abandonment,
CAC vs Conversion, LTV, crecimiento geográfico, NPS. Ángulo Yuno: más métodos + checkout
más rápido para bajar abandono, experiencias one-click/saved/localizadas, retries y
routing inteligentes para reducir renovaciones fallidas (LTV), insights de pago en
tiempo real para optimizar adquisición/ROI/CAC.

## CEO / Founder
Prioridad: crecimiento, márgenes, riesgo estratégico, escala, fundraising/valuación.
Pains: pagos filtrando revenue y margen en silencio, no poder expandirse a mercados
nuevos con velocidad, pagos como cuello de botella estratégico, riesgo de concentración
de infraestructura/vendors, sin visibilidad limpia de pagos para board e inversionistas.
KPIs: Revenue Growth, Gross Margin, velocidad de expansión, Customer Growth/Retention,
eficiencia operativa/valuación. Ángulo Yuno: convertir pagos en palanca de crecimiento
(approval uplift = más revenue sin más CAC), entrar a mercados en semanas vía un API,
proteger margen con routing + consolidación, un partner de infraestructura que escala
con la empresa, visibilidad nivel board, des-riesgar la dependencia de un solo rail o
vendor. Proof: 5-20% approval uplift, InDrive 10 mercados LATAM en <8 meses.

## Product Manager
Prioridad: shippear features de pago/checkout y ser dueño de métricas de funnel (más
táctico que el CPO). Pains: features de pago tardan y dependen de ingeniería, fricción
de checkout golpea activación/conversión, difícil hacer A/B testing de métodos o
routing, data inconsistente para decidir, lanzamientos lentos de métodos bloquean el
roadmap. KPIs: Feature Delivery Velocity, Checkout Conversion, funnel/activación,
time-to-launch de métodos nuevos, throughput de experimentos. Ángulo Yuno: capacidades
pre-built + SDKs para shippear sin ingeniería pesada, habilitar métodos/PSPs no-code
(config, no proyecto), one-click y saved cards, A/B testing fácil entre métodos y
routing, analítica de pagos unificada. Libera el roadmap del plumbing de pagos.

## Treasurer
Prioridad: caja, liquidez, settlement, FX y riesgo financiero. Pains: settlement
fragmentado entre múltiples PSPs, timing de settlement lento o impredecible, costos de
FX y cross-border erosionando fondos, conciliación manual, poca visibilidad de caja
entre mercados/monedas, riesgo de contraparte/concentración. KPIs: Cash Flow/Liquidity,
Settlement Time, costos de FX y procesamiento, DSO, precisión de conciliación, Working
Capital. Ángulo Yuno: conciliación y visibilidad de settlement unificadas en un
dashboard, settlement más rápido y predecible, multi-currency + local acquiring para
bajar costo FX/cross-border, una vista en tiempo real del movimiento de dinero para
forecasting, menor dependencia de un solo procesador/banco.

## Head of Payment Operations
Prioridad: el practitioner que corre pagos día a día (a menudo el verdadero champion).
Pains: conciliación y matching de settlements manual, apagar incendios de pagos
fallidos y disputas, chargebacks entre múltiples proveedores, sin un solo lugar para
monitorear approval rates/salud de proveedores, rollout de métodos o PSPs dependiente
de ingeniería, data inconsistente entre PSPs. KPIs: Authorization/Success Rate,
Chargeback & Dispute Rate, tiempo de conciliación, recovery de pagos fallidos, uptime
de proveedores, time-to-add de método/PSP. Ángulo Yuno: un dashboard sobre todos los
procesadores y métodos (approvals, refunds, chargebacks, salud de proveedores) con
monitoreo en tiempo real y alertas proactivas, retries/conciliación/settlement
automatizados, smart routing + failover para subir approvals y recuperar soft declines,
habilitación no-code de métodos/PSPs. Convierte el firefighting en supervisión.

## Head of Fraud / Risk & Compliance
Prioridad: proteger revenue de fraude y chargebacks manteniendo compliance. Pains:
pérdidas por chargebacks y fraude, false declines matando revenue bueno, transacciones
cross-border mal marcadas, muchas herramientas de fraude desconectadas, fricción de 3DS
golpeando conversión, carga de SCA/PCI entre mercados. KPIs: Fraud & Chargeback Rate,
False-decline Rate, Dispute Win Rate, Approval Rate neto de fraude, compliance 3DS/SCA,
costo de fraud ops. Ángulo Yuno: screening de riesgo en tiempo real sobre 50+
herramientas de fraude desde una capa, 3DS agnóstico/optimizado que minimiza fricción,
network tokens + account updater para reducir exposición y fallas silenciosas,
resolución temprana de disputas antes del chargeback, local acquiring para resolver
flags de fraude cross-border. Reduce pérdidas Y sube approvals a la vez.

## COO
Prioridad: eficiencia operativa y escalar la organización sin sumar complejidad. Pains:
demasiados vendors/contratos de pago, operaciones que no escalan con el crecimiento,
sistemas y reporting fragmentados, tiempo de ingeniería y ops drenado por mantenimiento
de pagos, expansión de mercados frenada por el setup de pagos. KPIs: Operating
Margin/Efficiency, Cost per Transaction, Vendor Count, time-to-market de geos nuevas,
automatización de procesos, uptime. Ángulo Yuno: consolidar todos los proveedores en
una plataforma y un contrato, automatizar retries/conciliación/settlement, lanzar
mercados en semanas vía un API, visibilidad operativa unificada, infraestructura
cloud-native escalable para que ops e ingeniería se enfoquen en el core.

## Controller / Head of Finance Ops
Prioridad: el cierre contable, conciliación y precisión de reporting (más granular que
CFO/Treasurer). Pains: conciliación multi-PSP manual que atrasa el cierre de mes,
descuadres entre reportes de procesadores y settlements bancarios, tracking de
refunds/chargebacks entre mercados, spreadsheets propensos a error, sin fuente única de
verdad de data de pagos, complejidad de auditoría. KPIs: Time-to-close, precisión de
conciliación/match rate, volumen de ajustes manuales, tracking de refunds/chargebacks,
audit readiness. Ángulo Yuno: conciliación unificada consolidando todos los
procesadores y métodos en un dashboard con approvals/refunds/chargebacks en tiempo
real, matching automatizado para acelerar el cierre, audit trails centralizados por
mercado, una fuente de verdad para finanzas.

# ANEXO 2

# Ejemplo real: intro de Magdalena (Lowe's, agosto 2026)

## El email de intro que dispara el skill

Hilo: "Re: The Lowe's Business Case, in Numbers"
De: magdalena.torrealba@y.uno | TO: lead de Lowe's | CC: german.tatis@y.uno

> Hi Lali,
>
> I wanted to follow up on the business case I shared, to see if you had the
> chance to look through it, and to use it as the excuse to introduce you to German.
>
> Every time I dug into something on Lowe's and hit a wall, there was one person
> I kept turning to, so it only feels fair to introduce you two. German runs our
> biggest merchant conversations across North America, and he has quietly shaped
> most of the analysis I have shared with you. He tends to see the patterns I miss,
> which is exactly why I want him to join our future conversation.
>
> I genuinely think a conversation between the three of us would be extremely
> useful. Are you available for a quick call next Wednesday?
>
> Best,
> Magda

Notas del patrón:
- Antes de la intro, Magdalena ya envió un business case con bullets (approval uplift,
  métodos locales, local acquiring, tiempo de ingeniería). El lead YA tiene el pitch:
  la respuesta de German no lo repite.
- La intro ya posiciona a German: lleva las conversaciones grandes de NA y estuvo
  detrás del análisis. La respuesta debe estar a la altura de ese framing.
- Magdalena ya propuso un CTA (call el miércoles). La respuesta de German lo refuerza
  y lo facilita, no propone otra cosa.

## Ejemplo de respuesta de German (referencia de tono, NO plantilla literal)

Persona asumido en este ejemplo: VP / Head of Payments.

> Thanks Magda.
>
> Lali, great to meet you. I was behind most of the analysis Magda shared, so I know
> exactly where those numbers are conservative. In conversations with merchants at
> Lowe's scale, the gap usually sits in authorization rates and cost per transaction
> across processors, and that is where I can add the most in a first call: pressure
> testing the case against how your stack actually runs today.
>
> Wednesday works on my end. Happy to adjust to whatever time suits you best.
>
> Best,
> German

Por qué funciona:
- 80 palabras. Corto, denso, senior.
- Línea 1: gracias a Magda, una sola línea.
- Credibilidad heredada de la intro ("I was behind most of the analysis"), no inventada.
- Una sola idea de valor, tomada del persona (authorization rate y costo por
  transacción para un Head of Payments), conectada al contexto real del hilo (el
  business case con estimados conservadores).
- CTA que confirma el miércoles que Magda propuso y cede el control del horario.
- Sin em-dashes, sin " - " como puntuación, sin datos inventados de Lowe's, sin
  repetir los bullets del business case, sin name-dropping.
