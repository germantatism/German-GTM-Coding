# Experian (DataCrédito) | Follow-up post demo motor de suscripciones (23-sep-2026)

**Para:** Carlos Falla (carlos.falla@experian.com, PM), Cristian Vargas (cristian.vargasm@experian.com, dueño de Midatacrédito)
**CC:** Magdalena Torrealba, Daniel Lozano (PM Subscriptions), Joaquín Mann
**Asunto:** Yuno + Experian | Resumen y próximos pasos: suscripciones y conciliación

Contexto: call del 23-sep-2026 2:00 p.m. COT (34 min, Gong id 4409727408628545713). Primera conversación desde abril. Daniel mostró el motor de suscripciones; German presentó el producto de conciliación como standalone. Carlos se fue antes y dejó a Cristian coordinando.

Lo que dijo Experian:
- Tres "autopistas": tarjeta débito/crédito con PayU; Bancolombia, Nequi y Daviplata con Wompi; resto del sistema financiero vía PSE + enrolamiento + débito automático por archivo cargado a Bancolombia (respuesta D+1 después de las 9 p.m.).
- Split de recaudo aprox. 55 / 25 / 20; el 55 es cuentas (débito). Es el modelo más grande en ingresos y donde quieren optimizar.
- ~100 a 150K suscriptores efectivos, base de ~300K aptos para cobro.
- Dolor: cuenta capturada antes del PSE no coincide con la que usa el usuario; datos inválidos para la recurrencia; usuarios en limbo mientras llega la respuesta del banco.
- No quieren tocar PayU ni Wompi por ahora (estables); la oportunidad es suscripciones de cuentas de ahorro.
- Datos que tienen de cada cuenta: cédula, número de cuenta, entidad, nombre, autorización.
- Cristian preguntó por Bre-B (tokenizar cuentas) y por qué bancos tenemos conectados para débito a cuenta.
- Carlos pidió: diagrama del flujo de integración (es "visual"), tarifarios actualizados para business case por transacción.
- Timeline: proyecto del siguiente año fiscal, arrancar ene/feb/mar y terminar abr/may; ~150M COP en desarrolladores de su lado (no citar en el correo).
- Piloto propuesto por Carlos: ~20.000 cuentas comparando modelo actual vs Yuno (eficiencia, costo, recaudo), luego escalar.
- "Esto sí no lo hemos visto en el mercado y sí generaría valor para nuestra operación" (Carlos).

Instrucciones de German: martes 29-sep 2:00 p.m. suscripciones; miércoles 30-sep conciliación (pasar horarios); migración de cuentas = "validando internamente, creemos que sí"; alineados en que el producto de suscripciones les sirve. Español.

Calendario verificado (hora Bogotá): martes 29 2:00 a 3:00 p.m. libre para German y Daniel. Miércoles 30 libres para ambos: 10:00 a.m., 2:30 p.m., 4:00 p.m. German opera desde San Francisco a partir del 28-sep (PT = COT menos 2 h): 2:00 p.m. COT = 12:00 p.m. PT.

---

Hola Carlos y Cristian,

Gracias por retomar la conversación hoy. Nos quedó claro cómo está montado el recaudo: tarjetas con PayU, Bancolombia, Nequi y Daviplata con Wompi, y el resto del sistema financiero vía PSE, enrolamiento y débito automático por archivo con respuesta de Bancolombia en D+1. Ese tercer flujo es el más grande en ingresos y es donde más se pierde: cuentas capturadas antes del PSE que no coinciden con la que el usuario termina usando, y suscriptores en limbo mientras llega la respuesta del banco.

Lo que vimos con Daniel y por qué creemos que encaja:

1. El motor de suscripciones corre encima de la orquestación: cada cobro recurrente es una transacción que hereda los métodos de pago y procesadores que ya tienen, y los que quieran sumar.
2. Reintentos con un modelo de machine learning entrenado con nuestra data, que decide el mejor momento para recobrar una cuota declinada.
3. Webhooks por cada cambio de estado de la transacción y de la suscripción (activa, pendiente, en mora, cancelada). Así es como su core se entera del resultado de cada cobro y de cada reintento.
4. Dashboard con todas las suscripciones agrupadas por plan y por estado, que es la base para la analítica por plan y la proyección de cierre de mes que mencionaba Cristian.
5. Planes mensuales, trimestrales o anuales, con los siete días gratis configurados en la plataforma. Si un reintento exitoso mantiene o reinicia la fecha de cobro es una decisión de negocio que queda de su lado.

Sobre la migración:

- Tokens de tarjeta en PayU y Wompi: se pueden migrar a Yuno y seguir cobrando como MIT con el network transaction ID. Entendemos que por ahora prefieren no tocar esos dos flujos, así que el foco es cuentas.
- Cuentas de ahorro (cédula, número de cuenta, entidad y nombre): lo estamos validando internamente y creemos que sí podemos hacer la migración. Lo cerramos el martes.
- Bre-B: ya lo tenemos integrado. El cobro recurrente sobre Bre-B depende de que el sistema habilite la tokenización de cuentas; cuando eso pase, el motor podrá crear suscripciones sobre ese método.

Nos gusta la idea del piloto con unas 20.000 cuentas para comparar eficiencia, costo y recaudo contra el modelo actual, y de ahí escalar. Y como te decía, Carlos, la integración no la cargan solos: nuestro equipo acompaña el desarrollo de punta a punta para que sea lo más rápida y liviana posible dentro de la ventana de enero a mayo.

Próximos pasos:

1. Martes 29 de septiembre, 2:00 p.m. hora Colombia: sesión de suscripciones con Daniel y Cristian. Flujo de integración paso a paso con el diagrama que pedía Carlos (alta de suscripción y primer cobro, cobros recurrentes, reintentos, webhooks y cancelaciones), proceso de migración de cuentas, y bancos conectados para débito a cuenta con sus tiempos de respuesta. Ya les envío la invitación.
2. Miércoles 30 de septiembre: sesión de conciliación con la persona de operaciones que mencionó Cristian. Opciones en hora Colombia: 10:00 a.m., 2:30 p.m. o 4:00 p.m. Me dicen cuál le sirve y envío la invitación.
3. Tarifarios: los revisamos al cierre de la sesión del martes y te los dejo por escrito ese mismo día, para que puedan armar el business case por transacción.

Quedo atento.

Saludos,
German

---

**Notas:**
- Sin em-dashes ni " - " como puntuación. Español, tuteo, tono senior.
- Compromisos que el correo deja sobre la mesa: (a) diagrama del flujo de integración para el martes (Daniel / German), (b) respuesta sobre bancos conectados para débito a cuenta y tiempos de respuesta, (c) tarifarios por escrito el martes después de la sesión (consultar Pricing Policy antes), (d) invitación del martes 2:00 p.m. COT por enviar.
- Cifras que NO van en el correo: split 55/25/20, 100 a 150K suscriptores, 300K base, 150M COP de desarrollo.
- Borrador creado en Gmail como correo nuevo (no existe hilo de correo con Carlos; el hilo "Experian + Yuno" de febrero es la intro de Clariana a Julián Buitrago con siete personas de Experian en copia).
