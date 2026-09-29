# Experian (DataCrédito) | Follow-up post deep dive de suscripciones (29-sep-2026)

**Para:** Cristian Vargas (cristian.vargasm@experian.com), Carlos Falla (carlos.falla@experian.com)
**CC:** Magdalena Torrealba, Daniel Lozano, Joaquín Mann
**Asunto:** Re: Yuno + Experian (respuesta en el mismo hilo del 23-sep)
**Estado:** BORRADOR en Gmail, versión 2. Sin enviar.

Contexto: call "Experian + Yuno | Suscripciones" del 29-sep-2026, 2:00 p.m. COT. Versión 2 parte del texto de German, reorganizado con su estructura habitual (Resumen, bloque de contenido, Próximos pasos) y con la lista de procesadores que prometió en la llamada. La versión 1, más larga y redactada desde las notas, se descartó.

⚠️ Pendiente antes de enviar:
1. Confirmar con Daniel que Wompi, Redeban, Mercado Pago y Kushki soportan cobro recurrente de tarjetas en Colombia a través de Yuno. Las páginas públicas de Yuno confirman la conexión, no la recurrencia.
2. Si existe benchmark interno de aprobación por procesador en Colombia, usarlo para ordenar la lista. German prometió "los que mejor performance tienen" y no hay dato público que lo respalde.

Verificación completa de la lista en experian-colombia-card-processors-research-2026-09-29.md.

---

Hola Cristian y Carlos,

Gracias por el espacio para revisar el motor de suscripciones. Les dejo el resumen, la lista de procesadores que quedé de compartirles y los próximos pasos.

**Resumen:** Revisamos cómo se conectan y se rutean los procesadores, y el motor de suscripciones: planes, reintentos y gestión de cada suscripción desde el dashboard. De su lado nos llevamos tres frentes: alternativas a PayU para tarjetas, débito automático a cuentas bancarias (en particular Davivienda y Grupo Aval) y Bre-B como medio de pago recurrente.

**Alternativas a PayU para tarjetas:**

- **Wompi:** ya lo tienen contratado y permite tokenizar tarjetas para cobros recurrentes. Es la opción más rápida de activar.
- **Redeban:** red de pagos colombiana, con procesamiento local de tarjetas.
- **Mercado Pago:** procesamiento local de tarjetas con cobros recurrentes.
- **Kushki:** plataforma regional con procesamiento local en Colombia.

Los cuatro están conectados a Yuno. Para saber cuál rinde mejor con su base, lo más confiable es medirlo: se envía un porcentaje del tráfico al procesador nuevo, con PayU como respaldo, y se compara la aprobación antes de mover más volumen.

**Próximos pasos:**

1. **Débito automático a cuentas:** les compartimos las opciones que encontremos para Davivienda y Grupo Aval.
2. **Bre-B:** Daniel confirma el estado como medio de pago recurrente.
3. **Conciliación:** Cristian, quedamos atentos a las opciones de agenda para revisarla con Milena.

Quedo atento. ¡Gracias!

German

---

**Notas:**
- Sin em-dashes ni " - " como puntuación. Sin links ni adjuntos.
- "Breve" del texto original corregido a Bre-B.
- Fuera del correo a propósito: tarifas de los procesadores (tres de cinco no coincidían con lo publicado, y son de lista para comercios pequeños), tasas de aprobación (sin fuente), bancos conectados Nubank y BBVA (German no los incluyó en su texto), horarios propuestos para conciliación (German prefirió esperar las opciones de Cristian) y el comentario sobre la efectividad de PayU.
- Compromisos que deja el correo: (a) opciones de débito automático para Davivienda y Grupo Aval, (b) estado de Bre-B recurrente (Daniel).
