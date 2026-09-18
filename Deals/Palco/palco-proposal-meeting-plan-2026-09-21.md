# Plan de presentación: Palco + Yuno | Propuesta (lun 21-sep-2026, 11:00 a 11:45 COT)

Asisten: Patricio (CEO, decide), Alfonso (co-fundador, construyó las 50+ integraciones, objeción de costo), Fernando (TAM, quiere integraciones sin construirlas), Miguel (co-dueño, tentativo, comercial). Por Yuno: German y Joaquin.
Deck: https://docs.google.com/presentation/d/1hWX6sNKKPpXhDSKGlZzrHWyKWMx5WlVxBeScEL_J7UY/edit (con los cambios de palco-proposal-review-2026-09-18.md aplicados).

## Objetivo

Salir con el piloto aprobado: tenants nombrados, fecha de kickoff y quién firma. No salir con "lo revisamos internamente". Patricio dijo que septiembre define el camino; el lunes es 21.

## Antes del lunes

1. Aplicar los cambios del deck (script + slide de preguntas + bloque piloto). No presentar risk conditions a $0.04 ni "Contrato a 3 años".
2. Pregunta a Fernando (jueves): ¿$37.09 es por boleto o por transacción? Su tabla mensual da $120 por transacción. Si es por boleto, el caso se triplica y el costo por orden cae a ~8 bps. Preguntar antes, no descubrirlo en la reunión.
3. Carlos, con fecha: catálogo Openpay / Banorte / Santander / Mercado Pago / Fiserv; split al capturar con tenant MoR por procesador mexicano; recurrencia con procesadores mexicanos. Lo que no confirme queda en ⚠ con fecha en el slide de preguntas.
4. Brief a Joaquin (15 min): él lleva México (preventas bancarias por BIN con Banamex, Santander y Banorte; picos de on-sale) y toma nota de compromisos, nombres y fechas. German lleva números y cierre.
5. Decidir la moneda de negociación: fee de plataforma reducido durante el piloto (hasta 3 meses de crédito sin aprobación). Se da a cambio de tenants nombrados y fecha, nunca solo.
6. Tener el calculator abierto por si aprietan precio. Hay margen (plataforma green hasta $6,325; tramos hasta $0.026 / $0.0227 / $0.0204), pero el lunes no se regala: se cambia por compromiso.
7. No mandar el deck antes. Se manda el PDF el mismo lunes con el resumen y el piloto por escrito.

## Los 45 minutos

**0 a 3 · Apertura.** Sin rodeos. "Patricio, gracias por la data del 2 de septiembre: casi nadie manda aprobación por procesador sin que se lo pidan. Hicimos la aritmética sobre esos números y hoy quiero contestar tres cosas: cuánto vale arreglarlo, cuánto cuesta con nosotros y cómo lo probamos en 90 días sin que cambien nada de lo que ya construyeron. La plataforma ya la vieron con Carlos; si quieren, volvemos ahí al final." Con eso saltas los diez slides de "por qué Yuno" y Patricio lo agradece.

**3 a 8 · Lo que nos pidieron.** Slide nuevo. Una frase por fila, sin leer. "Seis preguntas de Patricio, cuatro de Alfonso y Fernando. Seis respondidas, tres con confirmación el [fecha]." Decir las tres pendientes tú, antes de que las descubran: qué procesadores mexicanos hacen split en su dirección, recurrencia con procesadores mexicanos, y que el fallback en métodos con redirección solo aplica si falla crear la redirección. Credibilidad: dices lo que no sabes con fecha.

**8 a 18 · Business case, por encima.** Solo S13 y S14. No leer supuestos; ofrecerlos a Fernando después.

Abrir con su propio dato, no con el nuestro: "Un dato de su tabla: Mercado Pago les aprueba 92% en wallet y 68% en tarjeta, mismo proveedor. Redsys en España está en 88% con el mismo checkout. Openpay, Banorte y Santander en México, entre 56% y 60%. No es el país ni el producto: es la ruta."

Las cuatro palancas en una frase cada una. Luego el titular: "Sobre sus 235,000 transacciones al mes y su ticket de $37.09, mover esa cohorte cinco puntos son $4.7M al año; diez puntos, $9.3M. Con failover y ruteo de costo, el rango total es $5.5M a $10.7M. Punto medio, $8M."

Anclar los escenarios: "El conservador, 67.4%, es lo que Mercado Pago ya les da hoy en tarjeta. El optimista, 72%, es el mercado mexicano en crédito. No inventamos un número; pedimos llegar a lo que ya existe."

La línea honesta, que es la que vende a Patricio: "Ese dinero llega a sus clientes porque son merchant of record. Lo que cae directo en Palco es dejar de mantener 50 integraciones: $230K a $360K al año. Y lo tercero, donde yo lo pondría: cada punto de fee de Palco sobre $7.7M recuperados son $77K al año. Esto deja de ser un costo y pasa a ser un producto que ustedes venden."

Trial close: "¿Este es el tamaño de problema que tenían en la cabeza?" Si Patricio dice "más" o "menos", ya está negociando el caso, no la decisión.

**18 a 30 · Propuesta.** Estructura primero, número después, traducción inmediata.

"Dos componentes: $7,000 fijos al mes y una tarifa por transacción aprobada que empieza en 6 centavos y baja a 4.5 con volumen. Solo aprobadas, sin setup, subcuentas por cliente incluidas, un solo contrato y una sola factura a Palco; los tramos se calculan sobre el volumen agregado de todos sus clientes. A su volumen: $19,000 al mes en pagos, $23,400 si sumamos 3DS selectivo y antifraude."

Silencio. Que hable Alfonso. Después: "Eso son 10 centavos por transacción, 27 puntos básicos sobre un ticket de $37. Contra 8% a 16% más ventas aprobadas para el tenant. Por cada dólar que Palco nos paga, sus clientes recuperan entre 18 y 36."

Segundo trial close, dirigido a Alfonso: "¿Con esta estructura, cómo lo empaquetarían a sus clientes?" Lo conviertes en co-diseñador del producto en vez de auditor del costo.

Piloto: "Por eso no traigo un contrato a tres años. Traigo un piloto: 3 a 5 tenants en México sobre Openpay, Banorte y Santander, subcuentas y SDK, baseline su tabla de agosto, revisión a 90 días. Fernando ya tiene el sandbox; Carlos hace el onboarding la semana del 28."

**30 a 40 · Discusión.** Objeciones abajo. Joaquin entra en México y preventas.

**40 a 45 · Cierre.** Dos preguntas, en este orden: "¿Qué tenants pondrían en el piloto?" (nombrar tenants es el compromiso). "¿Quién firma el piloto de su lado, tú o Miguel?" Cerrar con fechas: lista de tenants el miércoles, kickoff con Carlos la semana del 28, revisión a 90 días en calendario.

## Objeciones

| Van a decir | Respuesta |
|---|---|
| "Dijiste 15K" (Alfonso) | "El fijo bajó a $7,000. Lo demás crece solo si procesan más. En el primer tramo el mes completo son $10,500." |
| "El costo se traslada al cliente final y ellos eligen por precio" | "Tienes razón en que el ruteo de costo solo no paga esto: 7 a 12 puntos básicos contra 27. Lo que lo paga es la aprobación. Un tenant que hoy aprueba 62 y pasa a 67 vende 8% más. Nadie cambia de pasarela por 27 bps si vende 8% más." |
| "Ya tenemos 50 integraciones" | "Y las siguen teniendo; cuentas y contratos siguen siendo suyos. No reemplazamos lo que construyeron: ponemos la capa de decisión encima y mantenemos los conectores vivos para que Fernando no construya el siguiente país." Nunca "les falta orquestador". |
| "¿Por qué no lo construimos nosotros?" | "Pueden. La pregunta es si quieren que el equipo de Alfonso mantenga 50 conectores y un motor de ruteo, o construya producto de ticketing. Y el tiempo: esto está en producción hoy; el piloto arranca en semanas." |
| "¿Garantizan el uplift?" | "No, y desconfiaría de quien lo haga. Por eso el piloto tiene baseline con sus números y revisión a 90 días. Si no movemos la aguja, tienen la data para decidir." |
| "¿Y el split / la recurrencia en México?" | "Yuno propaga el split al procesador que lo soporta; cuáles mexicanos lo hacen en su dirección lo confirma Carlos el [fecha]. Prefiero eso a prometerles algo hoy." |
| "El 3DS nos mata la aprobación" | "Por eso lo modelamos selectivo: 3DS como condición de ruteo, exenciones por riesgo y reintento por otra ruta. Y la pregunta de vuelta: ¿el 3DS al 100% se lo exige el adquirente, el tenant, o es decisión de Palco?" |
| "Bájame el precio" (Patricio) | No bajar en la mesa. "Lo que puedo hacer es reducir el fee de plataforma durante el piloto si salimos hoy con los tenants y la fecha." Dar a cambio de compromiso. |
| "¿Tienen un caso de marketplace / split?" | Solo genérico: "Tenemos un marketplace en producción con split, sellers y transfers sobre tres procesadores." Sin nombre salvo permiso. |

## Reglas de la sala

- Nunca $457M ni el ticket de $163; todo sobre 235,000 y $37.09.
- No leer supuestos ni la tabla de procesadores; ofrecerlos a Fernando por correo.
- Los tres ⚠ se dicen con fecha; no se prometen.
- No hablar de "orquestador" como carencia; hablar de "capa de decisión encima de lo que construyeron".
- Si Miguel entra, una frase para él: "Esto convierte pagos en una línea de ingreso de Palco, no en un costo."
- Cerrar preguntando, no resumiendo.

## Después (mismo lunes)

Correo a Patricio, Alfonso, Fernando (cc Miguel si estuvo, Joaquin, Carlos): PDF del deck, el piloto en cinco líneas (alcance, baseline, KPI, fechas, condición comercial), las tres confirmaciones pendientes con fecha, y la pregunta del ticket si no se resolvió. Pedir la lista de tenants para el miércoles.
