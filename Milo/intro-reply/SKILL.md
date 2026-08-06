---
name: intro-reply
description: >-
  Procesa las intros que Magdalena (SDR de Yuno) hace por email presentando a
  German con un lead externo (German en CC, lead de otra empresa en TO).
  Investiga al lead, clasifica su buyer persona, redacta la respuesta corta de
  German, pide el OK a Magdalena por email y SOLO tras su OK envía la respuesta
  en el hilo original. Usar cuando corra la tarea programada de intros, o cuando
  German pida "revisa intros", "procesa intros" o "procesa aprobaciones".
---

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
5. **Clasificar el buyer persona** del lead usando `references/buyer-personas.md`
   (13 personas). Elegir el más cercano por cargo y scope. El persona define el ángulo
   de valor del mensaje.
6. **Redactar la respuesta de German** siguiendo las reglas de redacción de abajo y el
   ejemplo de `references/ejemplo-real.md`.
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

- `references/buyer-personas.md`: los 13 buyer personas de Yuno con pains, KPIs y ángulo
  de valor. Usar SIEMPRE para elegir el ángulo del mensaje.
- `references/ejemplo-real.md`: una intro real de Magdalena (Lowe's) y un ejemplo de
  respuesta con el tono correcto. Es referencia de tono y estructura, no plantilla literal.
