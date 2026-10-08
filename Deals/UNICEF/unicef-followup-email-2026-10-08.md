# UNICEF Colombia | Follow-up post presentación de propuesta (8-oct-2026)

**Para:** Sebastian Garavito (sgaravito@unicef.org), Leidy Guio (lguio@unicef.org), Idual Kerguelen (ikerguelen@unicef.org)
**Asunto:** Re: UNICEF + Yuno (respuesta en el hilo, al mensaje de Sebastián del 6-oct)
**Estado:** BORRADOR en Gmail, creado 8-oct-2026 tras la reunión "Unicef + Yuno" (10:30 COT). Sin enviar.

**v3 (8-oct): cuatro tramos 0.28/0.26/0.24/0.22 en el correo y en el deck. v2:** German pidió incluir el link https://docs.y.uno/ y decir que el sandbox se prepara hoy y las invitaciones llegan en el día. Borrador recreado como reply (nunca update_draft). **German debe agregar antes de enviar:** la propuesta actualizada adjunta (tramo 0 a 50,000 + precio de conciliación) y crear las cuentas sandbox para los tres. Confirmar si lo de ACH (tiempos y prenotificación) ya se resolvió en la llamada; si sí, borrar esa frase.

**Lo que salió de la llamada (resumen automático pegado por German, con correcciones de nombres):** pricing percentual para proteger el ticket bajo, 0.28% / 0.24%; motor de suscripciones opcional (si no se usa, la línea sale); rechazadas no pagan; montos del donante los capturan ellos en sus formularios (el monto libre en checkout no les aplica); acuerdos con adquirentes intactos; pidieron un primer tramo más bajo (0 a 50,000) y Yuno está abierto; conciliación hoy la hace finanzas (área de Lorena) a mano cruzando dashboards de cada procesador; UNICEF evalúa internamente tarifas y volúmenes antes de sumar otros equipos; Idual prefiere una prueba de concepto acotada antes de escalar. ⚠️ El resumen dice "primeras 100,000 gratis" en suscripciones; el deck dice 50,000: confirmar qué se dijo.

---

Hola Sebastián, Leidy e Idual,

Gracias por el espacio de hoy. Me quedo con que la conversación ya está en terreno concreto: cómo encaja Yuno con lo que tienen y cuánto cuesta. Les dejo por escrito lo que acordamos y lo que queda de mi lado.

**Sobre la propuesta que revisamos:**

1. La tarifa es un porcentaje del valor de cada transacción aprobada, pensada justamente para proteger el ticket bajo. Las transacciones rechazadas no pagan.
2. El motor de suscripciones es opcional. Si prefieren seguir disparando los cobros desde Salesforce y usar solo la orquestación y el ruteo, no hay ninguna limitación funcional y esa línea sale de la propuesta.
3. Sus acuerdos y tarifas con Credibanco, Redeban, Wompi y Nuvei no cambian: Yuno se conecta por encima de ellos y no entra en el flujo del dinero.
4. La facturación mínima es de $10,000 al mes y ya incluye el fee de plataforma.

**Lo que ajusto con base en lo que pidieron:**

1. Los tramos ahora empiezan más abajo y son cuatro: 0.28% de 0 a 50,000 transacciones aprobadas al mes, 0.26% de 50,000 a 100,000, 0.24% de 100,000 a 150,000 y 0.22% por encima de 150,000. Cada tramo se cobra a su tarifa dentro del mes, así que el precio acompaña el volumen desde el inicio.
2. El precio del motor de conciliación: un solo reporte configurable con la información de todos los procesadores, para reemplazar el cruce manual que hoy hace el equipo de finanzas.

Adjunto la propuesta actualizada con esos dos cambios. Para calibrar bien el tramo inicial me ayuda saber cuántas transacciones aprobadas cierran al mes y cómo se reparten entre tarjeta, débito a cuenta y billeteras.

**Accesos y documentación:** las cuentas de sandbox las estamos preparando hoy mismo, y en el transcurso del día les llega a cada uno la invitación desde la plataforma. La documentación de la API está en https://docs.y.uno/ para que Idual y el equipo técnico la revisen con calma.

Idual, me gustó la idea de empezar con una prueba de concepto acotada sobre un solo flujo antes de extenderla a los demás canales. Propongo que definamos juntos el alcance y el cronograma de esa prueba en una sesión técnica con nuestro Solutions Engineer: la integración es vía API, así que los tiempos dependen sobre todo de cómo decidan conectar Salesforce y el middleware. Sigo además pendiente de confirmarles por escrito los tiempos de respuesta de los débitos a cuenta y la prenotificación de cuentas nuevas.

Entiendo que primero lo revisan internamente con las tarifas y los volúmenes antes de sumar a otros equipos. Cualquier dato que les ayude en ese análisis, me lo piden.

¿Les sirve la semana del 13 de octubre para la sesión técnica? Puedo el martes 13 o el jueves 15 a las 10:30 a.m. hora Bogotá, el mismo horario de hoy.

Gracias de nuevo por el tiempo y por lo directo de la conversación. Quedo atento.

Saludos,
German
