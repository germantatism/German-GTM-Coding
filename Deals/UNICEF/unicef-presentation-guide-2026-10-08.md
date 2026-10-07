# UNICEF Colombia | Guía para presentar la propuesta (jue 8-oct-2026, 10:30 COT / 8:30 PT, 30 min)

**Reunión:** "Unicef + Yuno", Google Meet https://meet.google.com/hpq-jrwq-yka. Invitados: Idual Kerguelen (aceptó), Leidy Guio (aceptó), Sebastián Garavito (sin responder), Samuel (samuel@y.uno, sin responder). Organiza German.
**Deck:** "Propuesta - UNICEF Colombia + Yuno", 20 slides, pricing v6 vigente. https://docs.google.com/presentation/d/111EW1tmbSYPYtxLYRa5Mf_yx0Cn-BxA4wT2FAZeGpe0/edit
**Preparado:** 7-oct-2026 a partir del deck en vivo, el hilo "UNICEF + Yuno", Gong (llamada 21-sep), Slack (#deal-proposals-1bn-arr), la Pricing Policy y docs.y.uno.

---

## TL;DR battle card

1. **Qué vendemos:** una capa encima de Credibanco iPay, Redeban, Wompi y Nuvei que recupera donaciones recurrentes rechazadas (ruteo y respaldo entre procesadores de tarjeta, reintentos configurables, motor de suscripciones) y quita el trabajo manual. No vendemos métodos de pago nuevos: ellos lo dijeron.
2. **Precio en el slide 15:** 0.28% por transacción aprobada hasta 100,000 al mes y 0.24% por encima; motor de suscripciones $0.015 por envío con las primeras 50,000 del mes gratis; fee de plataforma $7,000; facturación mínima $10,000. Estimado con 150,000 aprobadas: $14,500 al mes, $174,000 al año, $0.10 all-in.
3. **El número que gana la reunión:** con sus datos (150,000 donantes, 92% dona cada mes, 85% de aprobación, ticket $15) se rechazan unas 20,700 donaciones al mes, $310,500 que hoy no se recuperan. Un punto de aprobación vale $20,700 al mes, más que toda la factura de Yuno. La plataforma se paga recuperando 967 de esas 20,700 donaciones (4.7%).
4. **Dos cosas que NO se pueden prometer:** ruteo o fallback en débitos a cuenta (ya corregido por correo el 29-sep) y motor de suscripciones para ACH, Nequi o Daviplata (docs: el motor soporta solo tarjeta, PayPal y Pix Automático). Esos cobros los dispara Salesforce vía la API de Yuno.
5. **Pendiente interno antes de las 10:30:** el pricing v6 NO está en Salesforce. La aprobación de UNICEF del 2-oct en #deal-proposals-1bn-arr es de otra oportunidad: UNICEF Brasil, de Lucca Zadra, en reales. Someter hoy o pedir OK por Slack a Sean y Juan Sebastián Bernate.
6. **Pendientes con el cliente que siguen abiertos:** tiempos de respuesta de ACH y prenotificación de cuentas nuevas. No hay respuesta de producto en Slack. Pedir hoy a Joaquin Mann o al product lead de subs; si no llega, decir en la call que va por escrito el viernes.
7. **Quién decide:** ninguno de los tres asistentes firma. Gustavo Ugalde (Chief of Fundraising, inferencia del research) es el probable decisor. Compra ONU: RFP o LTA, PCI SAQ D más AoC. Cerrar la call con el proceso de compra y el decisor sobre la mesa.

---

## 1. Revisión del deck, slide por slide

| # | Slide | Estado | Qué hacer |
|---|---|---|---|
| 1 | Portada con lockup yuno + UNICEF | OK | Nada |
| 2 | Agenda: Por qué Yuno / Conexiones en Colombia / Propuesta | OK | Nada |
| 3 a 10 | Bloque "¿Por qué Yuno?" (capacidades, pilares, suite, logos, equipo, credenciales) | Genérico, 8 slides | Ya vieron dos demos. Pasar en 2 minutos o saltar a los slides 11, 13 y 15. Slide 10 trae "14% Wingo" (template): no decir "12%" en voz alta; las cifras publicadas son 7% de uplift y 30% de revenue recuperado. Slide 5 nombra GoFundMe: es la referencia más relevante para fundraising, usarla solo como logo, sin detalles del deal. |
| 11 | "Yuno es la capa de pagos para el recaudo recurrente de UNICEF Colombia" | OK, es el slide central | Las 4 ventajas están bien redactadas. "Ruteo y respaldo automático entre procesadores de tarjeta" dice "de tarjeta" a propósito: no ampliar a ACH. |
| 12 | Divisor Conexiones en Colombia | OK | Nada |
| 13 | Conexiones Colombia: 19 métodos, 14 procesadores | OK con detalles menores | Credibanco, Redeban, Wompi y Nuvei están en la lista: señalarlos. Menor: "Addi" aparece dos veces; "Bank transfer via Druo" está en inglés. |
| 14 | Divisor Propuesta | OK | Nada |
| 15 | Pricing v6 | Correcto y consistente con model.py | Ver sección 3. El footer "Contrato a 3 años." es herencia de Línea Directa, sale 33 pt fuera de página y es una exigencia fuerte para una agencia ONU en primera propuesta: quitarlo. |
| 16 a 19 | Apéndice: tablas "Lo que Yuno desbloquea" y citas genéricas de marketplaces/SaaS | No aplica a una ONG | No mostrar. Slide 17 dice "300+ métodos" y el resto del deck "1,000+". |
| 20 | Cierre con contacto | OK | Nada |

**Lo que falta en el deck y conviene cubrir en voz (o sumar dos slides esta noche):**
- **Cómo quedaría la integración y el alcance.** El correo del 6-oct prometió "una propuesta inicial de cómo sería trabajar en conjunto" y el deck solo trae precio. Contenido: Salesforce dispara los cobros vía API de Yuno (el middleware de UNICEF Global queda intacto, como pidieron); Yuno rutea tarjetas entre Credibanco, Redeban, Wompi y Nuvei con respaldo y reintentos; débitos a cuenta y wallets pasan por Yuno para visibilidad y reporte, sin ruteo; tokens de tarjeta: migrar a la bóveda de Yuno (recomendado) o consumir los de iPay (pendiente técnico con SE).
- **Próximos pasos.** Validación técnica con SE e Idual (tokens, ACH, middleware); respuesta escrita a ACH y prenotificación; documentación PCI (AoC) y de proveedor para compras ONU; proceso de compra y decisor; fecha para una fase 1.

---

## 2. Cómo presentar (30 minutos)

**0 a 3 min · Apertura.** Saludar a Idual por su nombre (el correo del 29-sep decía "Iván"). Recap en una frase de lo que oímos: orquestación y reintentos manuales, débito a cuenta manual, comisiones por rechazos, y una donación no cobrada en el mes es una donación perdida. Objetivo de hoy: validar alcance y precio y acordar los próximos pasos. Preguntar si alguien más debería ver esto antes de avanzar.

**3 a 8 min · Slides 11 y 13.** Qué hace Yuno para UNICEF, sobre lo que ya tienen. Decir explícito lo que sí y lo que no: ruteo y respaldo para tarjeta; reintentos hasta 6 por suscripción con calendario propio o SMART; débitos a cuenta pasan por Yuno para visibilidad, no para ruteo. Señalar sus cuatro procesadores en el slide 13.

**8 a 18 min · Slide 15, pricing.** Recorrer los tres paneles en este orden:
1. Panel derecho primero ("Lo que significa para UNICEF Colombia"): el total mensual estimado y el all-in de $0.10 por transacción aprobada. Las declinadas no pagan.
2. Panel izquierdo: la tarifa por tramos y el motor de suscripciones. Aclarar en voz que la línea de suscripciones aplica a los cobros con tarjeta que dispare el motor; eso baja la línea, no la sube.
3. Panel medio: lo que incluye el fee de plataforma (orquestación, API única, bóveda PCI, equipo dedicado). Mínimo mensual: $7,000 de plataforma más $3,000 en transacciones; con 117,000 a 150,000 aprobadas al mes queda cubierto de sobra (el punto de corte son 71,000).
4. Cerrar con la franja inferior: UNICEF mantiene sus contratos y tarifas con cada procesador; Yuno no entra en el flujo del dinero.
Luego el business case en voz (sección 4): 20,700 rechazos al mes, $310,500; un punto de aprobación son $20,700 al mes; la plataforma se paga con 967 donaciones recuperadas.

**18 a 25 min · Preguntas.** Ver objeciones en la sección 5.

**25 a 30 min · Próximos pasos.** Proponer: sesión técnica con SE la semana del 13-oct; respuesta escrita a ACH el viernes; pedir el proceso de compra y quién aprueba; ofrecer una fase 1 acotada (recurrencia con tarjeta sobre Credibanco, Redeban y Nuvei) si el proceso de compra lo exige.

**Roles:** German presenta. Definir con Samuel si entra como apoyo comercial. Joaquin Mann no está invitado: considerar sumarlo para las preguntas técnicas de Idual y Leidy.

---

## 3. Chequeo del pricing contra la Pricing Policy (interno, no mostrar)

| Línea | Propuesta | Policy (copia 21-sep, DRAFT) | Lectura |
|---|---|---|---|
| Fee de plataforma | $7,000 al mes | V3 (100K a 1M trx): list $10,000, mínimo $4,000 | Por debajo del list. Con la regla del ejemplo del doc (verde cubre el 60% del tramo entre list y mínimo) quedaría verde; la zona real la da el calculator. |
| Pay-ins | 0.28% / 0.24% = $0.042 / $0.036 por trx a $15 | list $0.10, mínimo $0.01 | Dentro del rango. |
| Suscripciones | $0.015 por envío, 50,000 gratis al mes | 0.7% TPV, mínimo 0.3%, "not sellable yet" | $0.015 sobre $15 es 0.1% del TPV. Confirmar con Finance. Es una línea de $1,500 al mes. |
| Mínimo mensual | $10,000 = fee fijo + $3,000 | Fijo + MMG aditivo = estructura preferida | OK. Facturar plataforma y mínimo mes a mes (no anual anticipado) va por zona amarilla. |
| Moneda | USD | LC/LC permitido en Colombia | Una oficina ONU en Colombia puede exigir factura en pesos. No comprometer; decir que es posible. |
| Salesforce | No sometido | Fundamento 1: cotizar después de pasar por Salesforce | Someter hoy. La aprobación "UNICEF" del 2-oct es de Lucca Zadra: UNICEF Brasil, plataforma 22,530 BRL, tramos $0.24 a $0.15 por trx, mínimo 35,000 BRL, aprobada por Juan Sebastián Bernate. |

**Heads-up adicional:** UNICEF Brasil y UNICEF Colombia comparten mandato global (Nuvei) y el middleware de UNICEF Global. Colombia queda a $0.04 por transacción contra $0.24 en Brasil. Avisar a Lucca y a Sean para que las dos propuestas no se crucen si las oficinas comparan.

---

## 4. Business case en voz (aritmética con los números que ellos dieron)

| Dato | Valor | Fuente |
|---|---|---|
| Donantes recurrentes en Colombia | 150,000 | Llamada 21-sep |
| Donan cada mes | 92% = 138,000 cobros al mes | Llamada 21-sep |
| Tasa de aprobación | 85% = 117,300 aprobadas, 20,700 rechazadas | Harold Martinez, 21-sep |
| Ticket promedio | $15 | Input de German |
| No cobrado al mes | 20,700 × $15 = $310,500 | Cálculo |
| No cobrado al año | $3,726,000 | Cálculo |
| Un punto de aprobación | 1,380 cobros × $15 = $20,700 al mes | Cálculo |
| Breakeven de Yuno | $14,500 ÷ $15 = 967 donaciones recuperadas al mes (4.7% de los rechazos) | Cálculo |
| Recuperar 1 de cada 10 rechazos | 2,070 × $15 = $31,050 al mes, 2.1 veces la factura | Cálculo |

**Sensibilidad de la factura:** si las aprobadas reales son 117,300 y no 150,000, Yuno cuesta $4,200 + $623 en transacciones, $1,320 en suscripciones y $7,000 de plataforma: $13,143 al mes ($157,716 al año, $0.11 all-in). Sigue por encima del mínimo de $10,000.

**Su propio costo publicado:** en donaciones.unicef.org.co/captadores dicen que una transacción con tarjeta les cuesta COP 700 y un débito COP 1,400. Van a comparar el $0.10 contra eso. No convertir en el deck; en voz, el argumento es que Yuno se paga solo por aprobadas, que las comisiones por rechazo y prenotificación bajan cuando bajan los rechazos, y que el trabajo manual diario de Leidy desaparece.

**Su RFP de telemercadeo (RFP2026-10, cerró 28-sep):** pedían reactivar el cobro de 90,000 donantes recurrentes por teléfono, actualizando el medio de pago, con "Tasa de Cobrabilidad" como KPI. Usar su lenguaje: Yuno sube la tasa de cobrabilidad antes de que el call center tenga que llamar.

---

## 5. Objeciones probables y respuesta (Requirement → Benefit → Proof)

1. **"Es un costo adicional encima de los procesadores."** Sí, y solo sobre aprobadas. Se paga con 967 donaciones recuperadas al mes de 20,700 rechazadas. Además caen las comisiones bancarias por rechazo y prenotificación y el reproceso manual.
2. **"¿Por qué pagar el porcentaje por los débitos a cuenta si no los rutean?"** Pasan por Yuno para tener todo el recaudo en un panel, disparo y conciliación desde un solo lugar. Si presionan: la policy permite split por método de pago (tarifa distinta para ACH). No ofrecerlo de entrada; pre-aprobar con Sean antes de la call por si hace falta.
3. **"Nuvei ya viene por mandato global y trae orquestación."** Yuno va encima de Nuvei también; el mandato global no cubre Credibanco, Redeban, Wompi ni los tres bancos de débito. Integrar vía el middleware global hace replicable el modelo en otras oficinas (ellos hablaron de más de 1M de donantes en LatAm).
4. **"El mínimo mensual."** $10,000 = $7,000 de plataforma + $3,000 en transacciones, que son 71,000 aprobadas. Con 117,000 a 150,000 nunca pagan la diferencia.
5. **"Contrato a 3 años."** Quitar el footer antes de la call. Si sale: vigencia y términos se definen juntos; el estándar de mercado es plurianual y encaja con un LTA.
6. **"Facturación en pesos y términos de pago ONU."** Posible facturar en COP a la oficina en Colombia; se confirma con Finance. No prometer net distinto a 30 sin aprobación.
7. **"¿Hay que migrar las tarjetas a la bóveda?"** Recomendado, no obligatorio; la alternativa es consumir los tokens de iPay, que se valida en la sesión técnica.
8. **"¿Cómo funcionan los reintentos?"** Hasta 6 por suscripción; calendario propio o SMART (timing por machine learning); se activa por suscripción con retry_on_decline; los rechazos duros no se reintentan, las fallas de procesador sí.
9. **"¿Montos abiertos y distintos por donante?"** Sí: cada suscripción se crea por API con su propio monto y frecuencia, sin plan. En el checkout de Yuno el monto libre no es inmediato (ya dicho por correo).
10. **"Prenotificación y tiempos de respuesta de ACH."** Sigue sin respuesta de producto. La prenotificación que existe en Yuno es para UPI Autopay en India, no para débito en Colombia. No improvisar: "lo confirmo por escrito el viernes".
11. **"Compras ONU, PCI."** PCI DSS Level 1, AoC disponible. Preguntar el proceso (RFP, LTA, umbral de adjudicación directa) y los tiempos; ofrecer una fase 1 acotada si el monto exige licitación.

---

## 6. Agenda propuesta para la call

1. Apertura y objetivo (3 min)
2. Qué hace Yuno para UNICEF Colombia, sobre su stack: slides 11 y 13 (5 min)
3. Propuesta económica: slide 15 y business case en voz (10 min)
4. Preguntas (7 min)
5. Próximos pasos y fechas (5 min)

## 7. Preguntas para hacerles (al cierre)

- ¿Quién más debe revisar esta propuesta y quién la aprueba? ¿Gustavo Ugalde entra en la siguiente sesión?
- ¿Cómo compran un servicio así: RFP, LTA o adjudicación directa? ¿Hay umbral y tiempos?
- ¿Cuántas donaciones aprobadas reales tienen al mes y cuál es el mix tarjeta, débito a cuenta, Nequi y Daviplata?
- ¿Cuándo cierra el presupuesto 2027 y qué partida contempla esto (hablaron de IA)?
- ¿Quién opera el middleware de UNICEF Global y pueden empujar los cobros a Yuno vía API desde Salesforce?
- ¿Los tokens de Credibanco iPay son exportables? ¿Hay objeción a migrar la base a la bóveda de Yuno?
- ¿Nuvei ya está live y con qué métodos?
- La licitación de telemercadeo para reactivar 90,000 donantes, ¿ya se adjudicó?
