# UNICEF LAC Cluster | Follow-up post llamada técnica (28-oct-2026)

**Para:** Sergio Rubio (srubio@unicef.org), Cluster Manager, UNICEF LAC Private Sector Fundraising Cluster (Panamá)
**Cc:** Juan Lapena Tortuero (jlapena@unicef.org), Lucca Zadra (lucca.zadra@y.uno), Carlos Medina (carlos.medina@y.uno, Implementation Engineer)
**Asunto:** Re: UNICEF – Recurring Payment Optimization Consultancy (reply al mensaje de Sergio del 26-oct, hilo 1a178b28b5cac823)
**Estado:** BORRADOR en Gmail (v2 corta, 28-oct-2026 tarde; German pidió "mucho más corto, solo docs.y.uno como link, sin tanta negrita"). v1 larga (4 links, subtítulos en negrita) SIGUE en Gmail como segundo borrador del hilo: trash_message fue bloqueado, German debe descartarla a mano. Sin enviar.

**Horarios (German + Carlos libres según calendario, hora Panamá):** vie 30-oct 14:00 a 16:00; mar 3-nov 8:30 a 12:00; vie 6-nov 8:00 a 10:00, 10:20 a 12:00, 14:00 a 16:00. ⚠️ 3-nov es feriado nacional en Panamá (Separación de Colombia; 2 al 5 de nov son feriados), por eso el correo deja el viernes 6 como salida.

**Compromisos que hace el correo:** revisar el análisis de rechazos de UNICEF antes de la sesión si lo comparten; validar en la sesión qué exporta cada pasarela (ExpressPago, Carnet, Dinelco) para la migración de tokens; sesión conjunta con Gustavo (Colombia) si les sirve. No promete un servicio de consultoría aparte.

---

Hola Sergio,

Gracias por el espacio de hoy. Les dejo un resumen corto, la documentación y opciones para la sesión técnica.

Lo que entendimos: procesamiento local en cinco mercados (ExpressPago, Carnet y Dinelco), el CRM conectado a cada pasarela y unos 60,000 donantes recurrentes con tokens que viven en cada pasarela. El cobro está en 75%, cerca del 20% de la base no se envía por falta de claridad en los errores y algunos reintentos han terminado en bloqueos de los bancos. Lo urgente es llegar mejor al próximo ciclo.

Lo que planteamos: Yuno como capa sobre las pasarelas que ya tienen, con ruteo y redundancia entre procesadores, una taxonomía estándar de errores (qué se reintenta, cuántas veces y cuándo parar), el motor de suscripciones corriendo los cobros en lugar del CRM y la migración de los tokens actuales a la bóveda de Yuno sin que el donante vuelva a ingresar su tarjeta.

Si nos comparten el análisis de rechazos que ya tienen, lo revisamos antes de la sesión y llegamos con recomendaciones concretas para el próximo ciclo.

La documentación técnica y de la API está en https://docs.y.uno

Para la sesión técnica, una hora con Carlos Medina, nuestro ingeniero de implementación (en copia), tenemos estas opciones en hora Panamá:
- Viernes 30 de octubre, 2:00 pm o 3:00 pm
- Martes 3 de noviembre, 10:00 am o 11:00 am

Si el martes les complica por los feriados, también podemos el viernes 6. Me dicen cuál les sirve y mando la invitación.

Saludos,
German
