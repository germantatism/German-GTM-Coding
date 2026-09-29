# UNICEF Colombia | Follow-up post Dashboard Demo (29-sep-2026)

**Para:** Sebastian Garavito Rodriguez (sgaravito@unicef.org), Leidy Guio Castellanos (lguio@unicef.org), Idual Kerguelen (ikerguelen@unicef.org)
**CC:** Susana Awad (susana.awad@y.uno), Alejandro Albarracín (alejandro@y.uno)
**Asunto:** Re: UNICEF + Yuno (respuesta en el mismo hilo)
**Estado:** BORRADOR en Gmail, texto escrito por German. Sin enviar.

Contexto: "Dashboard Demo Unicef x Yuno" del 29-sep-2026, 3:00 a 3:45 p.m. COT. Por Yuno: German, Susana, Joaquin Mann. El transcript de Google Meet quedó vacío y la llamada aún no estaba en Gong al redactar.

⚠️ Pendiente antes de enviar: el saludo dice "Iván", pero el contacto del hilo y de la invitación es Idual Kerguelen. Confirmar si fue un lapsus o si asistió otra persona.

---

Hola Sebastián, Leidy e Iván,

Gracias por el espacio. Les dejo un resumen y las respuestas que teníamos pendientes:

**Resumen:** Vimos cómo integrar sus procesadores con Yuno y centralizar la visibilidad de las transacciones.

**Respuestas:**

- **Salesforce y middleware:** La integración con Yuno se haría vía API. Cómo incluir el middleware en el flujo del proyecto quedaría de su lado, según lo que decidan hacer con él.
- **ACH:** Corrijo un punto de la demo: no podemos hacer smart routing ni fallbacks para transacciones ACH. Sí se puede migrar la base de cuentas de ahorro/corriente ya prenotificadas, con datos en claro. Quedo pendiente de confirmar los tiempos de respuesta de esas transacciones.
- **Suscripciones:** Si no usan nuestro checkout, pueden crear suscripciones independientes, sin asociarlas a un plan, cada una con su propio monto y frecuencia. Así tendrían suscripciones con distintos valores. Si usan nuestro checkout, tendríamos que revisar la integración para permitir que el donante ingrese el monto; aún no tengo confirmado que el checkout lo soporte.

**Próximos pasos:** Les confirmo los tiempos de respuesta de ACH y preparamos la propuesta de integración y precios para revisarla la próxima semana. Sebastián, ¿nos cuentan cómo quieren manejar el middleware dentro del proyecto?

Quedo atento. ¡Gracias!
