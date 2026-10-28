# UNICEF LAC Cluster | Follow-up post llamada técnica (28-oct-2026)

**Para:** Sergio Rubio (srubio@unicef.org), Cluster Manager, UNICEF LAC Private Sector Fundraising Cluster (Panamá)
**Cc:** Juan Lapena Tortuero (jlapena@unicef.org), Lucca Zadra (lucca.zadra@y.uno), Carlos Medina (carlos.medina@y.uno, Implementation Engineer)
**Asunto:** Re: UNICEF – Recurring Payment Optimization Consultancy (reply al mensaje de Sergio del 26-oct, hilo 1a178b28b5cac823)
**Estado:** BORRADOR en Gmail, creado 28-oct-2026 tras "Yuno UNICEF LAC Cluster" (Teams, 11:00 Panamá, 30 min). Sin enviar.

**Horarios (German + Carlos libres según calendario, hora Panamá):** vie 30-oct 14:00 a 16:00; mar 3-nov 8:30 a 12:00; vie 6-nov 8:00 a 10:00, 10:20 a 12:00, 14:00 a 16:00. ⚠️ 3-nov es feriado nacional en Panamá (Separación de Colombia; 2 al 5 de nov son feriados), por eso el correo deja el viernes 6 como salida.

**Compromisos que hace el correo:** revisar el análisis de rechazos de UNICEF antes de la sesión si lo comparten; validar en la sesión qué exporta cada pasarela (ExpressPago, Carnet, Dinelco) para la migración de tokens; sesión conjunta con Gustavo (Colombia) si les sirve. No promete un servicio de consultoría aparte.

---

Hola Sergio,

Gracias por el espacio de hoy y por el detalle con el que nos contaron la operación. Les dejo un resumen de lo que entendimos, la documentación técnica y opciones de horario para la sesión con nuestro equipo técnico.

**Lo que entendimos**

Hoy operan con procesamiento local en cinco mercados: ExpressPago en Costa Rica, Panamá y Guatemala, Carnet en República Dominicana y Dinelco (vía CyberSoft) en Paraguay, con el CRM conectado a cada pasarela y comisiones locales de 1.5% a 2%. Cerca del 95% de los donantes son recurrentes, la mayoría mensual, y los tokens viven en cada pasarela: UNICEF no guarda tarjetas, recibe el token y el código de autenticación inicial para los cobros siguientes. Son unos 60,000 donantes activos que habría que migrar.

En cobro recurrente están en 75%, y alrededor del 20% de la base no se envía porque la clasificación de errores no es clara. Los códigos ISO agrupan causas distintas (el P14 que puede ser tarjeta bloqueada o fondos insuficientes) y algunos reintentos han terminado en bloqueos por parte de los bancos, así que hoy están probando con grupos pequeños de donantes con apoyo de Chile, Brasil y Colombia. Eso no escala, y lo urgente es llegar mejor al próximo ciclo de cobro.

**Lo que planteamos**

Yuno como capa de orquestación sobre las pasarelas que ya tienen: ruteo y redundancia cuando un procesador rechaza, manejo centralizado de rechazos con una taxonomía estándar de errores (qué se reintenta, cuántas veces y cuándo parar), y la posibilidad de conectar procesadores adicionales sin perder las cuentas locales.

Motor de suscripciones: Yuno dispara los cobros con la frecuencia y el monto de cada donante, el CRM deja de correr la recurrencia y consulta el estado por API.

Bóveda: los tokens de Yuno no están atados a una pasarela, así que la misma tarjeta se puede cobrar por cualquier procesador conectado. Los tokens actuales se migran a la bóveda de Yuno con un proceso cifrado coordinado con cada pasarela, sin que el donante vuelva a ingresar su tarjeta. Qué exporta cada pasarela lo validamos en la sesión técnica.

PCI: Yuno es PCI DSS nivel 1 y UNICEF sigue sin almacenar tarjetas.

Para el corto plazo: si nos comparten el análisis que ya tienen (códigos de respuesta por pasarela y volúmenes), lo revisamos antes de la sesión y llegamos con recomendaciones concretas de reintento para el próximo ciclo.

**Documentación**

Para que la socialicen con su equipo antes de la sesión:
- Documentación general y referencia de la API: https://docs.y.uno/ y https://docs.y.uno/reference/getting-started/api-reference-overview
- Suscripciones y reintentos inteligentes: https://docs.y.uno/docs/payment-features/subscriptions/retries
- Cobros recurrentes entre procesadores (el código de autenticación inicial del que hablamos): https://docs.y.uno/docs/payment-features/stored-credentials
- Migración de tokens a la bóveda de Yuno: https://docs.y.uno/docs/security-and-compliance/data-migration-processes/token-migration-process

**Sesión técnica**

Sería una hora con Carlos Medina, nuestro ingeniero de implementación (en copia), para cubrir demo, integración vía API, migración de tokens, ruteo, recurrencia y conectividad con sus procesadores. Opciones en hora Panamá (misma de Bogotá):
- Viernes 30 de octubre, 2:00 pm o 3:00 pm
- Martes 3 de noviembre, 10:00 am o 11:00 am

Si el martes les complica por los feriados de noviembre, el viernes 6 también lo tenemos abierto. Me dicen cuál les sirve y mando la invitación.

Lo de Colombia también lo tomamos: estamos en conversación con el equipo de UNICEF Colombia y, si les sirve, armamos una sesión conjunta con Gustavo.

Saludos,
German
