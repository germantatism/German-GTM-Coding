# Experian (DataCrédito) | Follow-up post deep dive de suscripciones (29-sep-2026)

**Para:** Carlos Falla (carlos.falla@experian.com), Cristian Vargas (cristian.vargasm@experian.com)
**CC:** Magdalena Torrealba, Daniel Lozano, Joaquín Mann
**Asunto:** Re: Yuno + Experian (respuesta en el mismo hilo del 23-sep)
**Estado:** BORRADOR en Gmail. Sin enviar.

Contexto: call "Experian + Yuno | Suscripciones" del 29-sep-2026, 2:00 p.m. COT. Redactado desde las notas de German; la propuesta de texto de German no llegó en el mensaje, así que este borrador sale solo de las notas. Ver resumen en experian-call-summary-2026-09-29.md.

⚠️ Pendiente antes de enviar:
1. Confirmar que Nubank y BBVA son integraciones directas para débito automático a cuenta en Colombia (dato de las notas, sin contrastar).
2. Decidir si se deja por escrito "novedades en las próximas semanas" para el resto de bancos.
3. Confirmar las opciones de horario para conciliación (jueves 1 o viernes 2 de octubre, 10:00 a.m. o 2:30 p.m. COT, libres en el calendario de German al 29-sep).

---

Hola Carlos y Cristian,

Gracias por el espacio de hoy. Les dejo el resumen de lo que vimos y lo que quedó pendiente de cada lado.

**Resumen:** Recorrimos la plataforma en dos partes. Primero conexiones y ruteo: cómo se conecta un procesador nuevo, cómo se prenden y apagan métodos de pago en el checkout sin desarrollo, y cómo se reparte el tráfico por porcentaje con hasta dos fallbacks, de modo que si un procesador declina, el siguiente toma la transacción. Después el motor de suscripciones: planes por ciclo y por país con precio introductorio, estrategias de reintento (estándar, con machine learning o definida por ustedes), gestión de cada suscripción desde el dashboard (cancelar, pausar, cambiar de plan) y analítica por plan y por intento de cobro.

**Prioridades que nos llevamos:**

1. Débito automático a cuentas de ahorro y corriente, con foco en Davivienda y Grupo Aval.
2. Tarjetas: evaluar procesadores alternativos a PayU. La idea sería sumar un segundo procesador junto a PayU y mover el tráfico de forma gradual, sin tocar lo que hoy funciona.
3. Bre-B como medio de pago tokenizable para cobros recurrentes.

Cristian, si alguna quedó en otro orden, me corriges.

**Respuestas:**

- **Bancos para débito a cuenta:** hoy tenemos integración directa con Nubank y BBVA. Para Davivienda, Grupo Aval y el resto de bancos estamos evaluando un tercero que nos dé acceso, y esperamos tener novedades en las próximas semanas. Apenas esté definido les confirmo cobertura y tiempos de respuesta.
- **Bre-B:** Daniel confirma en qué está la tokenización y les contamos.

**Tiempos:** Con la implementación arrancando en abril de 2027, al inicio de su año fiscal, tiene sentido adelantar desde ya la vinculación de Yuno como proveedor y el caso de negocio. Cuéntenme qué documentación necesitan de nuestro lado para la vinculación y la vamos reuniendo.

**Próximos pasos:**

1. **Conciliación:** Cristian coordina con Milena. De nuestro lado tenemos disponibilidad el jueves 1 o el viernes 2 de octubre, a las 10:00 a.m. o 2:30 p.m. hora Colombia.
2. **Proveedores recomendados:** les comparto en los próximos días las opciones para tarjetas y para débito automático.
3. **Tarifarios:** los revisamos después de la sesión de conciliación, con el alcance ya claro, para que puedan armar el caso de negocio.

Quedo atento.

Saludos,
German

---

**Notas:**
- Sin em-dashes ni " - " como puntuación. Sin links ni adjuntos (German los agrega si quiere).
- Cifras y comentarios que NO van en el correo: split 55/25/20, suscriptores, 150M COP, y el comentario de Cristian sobre la caída de efectividad de PayU tras la adquisición (el hilo lleva a varias personas en copia).
- Compromisos que el correo deja sobre la mesa: (a) lista de proveedores recomendados para tarjetas y débito automático, (b) estado de tokenización de Bre-B (Daniel), (c) cobertura de bancos vía tercero, (d) tarifarios después de conciliación (consultar Pricing Policy), (e) documentación para vinculación de proveedores.
