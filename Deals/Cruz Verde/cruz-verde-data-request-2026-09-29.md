# Cruz Verde · solicitud de información para el business case (2026-09-29)

Cruz Verde pidió que Yuno les solicite todos los datos necesarios para construir el business case lo más a la medida posible (ejemplo de German: hasta el porcentaje de rechazos que son hard y los que son soft). Es el "documento de información requerida" prometido en el follow-up del 25-sep.

## Entregable que se envía: Google Sheet sencillo, una sola hoja

"Cruz Verde + Yuno | Información para el business case": https://docs.google.com/spreadsheets/d/1xipYBM6dNEVmCj_cxezIAqsfMb-gbPCimMJmXaGIMJQ/edit (carpeta Drive "Cruz Verde", dueño German).

German pidió primero un Google Sheet en formato de formulario y luego, al ver la versión de 13 hojas, "mucho más sencillo y en un solo tab". La versión vigente es la sencilla:

- Una hoja ("Información"), tres columnas: Campo, Respuesta de Cruz Verde (amarillo), Comentarios (opcional).
- 36 campos en 9 secciones: volumen y ventas (5), mix de medios (5), aprobación (4), rechazos con hard, soft, fraude y datos mal digitados (6), devoluciones y contracargos (4), disponibilidad (2), costos actuales (5), conciliación (2), nuevos medios de pago (3).
- Una línea al final ofrece la alternativa del export transaccional de Mercado Pago.
- Se genera con `build/build_data_request_simple.py`. Reemplaza todas las hojas del Sheet y se niega a correr si alguna celda amarilla ya tiene respuesta.
- Quedó por fuera frente a la versión detallada: series mensuales, cortes por canal, banco emisor, rango de ticket y tipo de entrega, códigos `status_detail` por motivo, embudos de PSE y checkout, registro de incidentes, proceso de conciliación y prioridades A, B, C. Si Cruz Verde quiere profundizar, esa versión sigue disponible (Excel y `build/build_data_request_gsheet.py`).
- ⚠️ `build/build_data_request_gsheet.py --rebuild` apunta al mismo Sheet y lo devolvería a la versión de 13 hojas. No correrlo sobre este archivo.
- German comparte el Sheet con Cruz Verde desde la interfaz. La service account aparece en la lista de personas con acceso; se puede quitar antes de compartir.

## Excel (respaldo, versión detallada)

`Solicitud de información - Cruz Verde + Yuno.xlsx` (esta carpeta). Se regenera con `build/build_data_request.py`; todo el contenido vive en el script y la hoja Resumen se arma sola a partir de las tablas y preguntas.

- 14 hojas, 90 solicitudes: 41 prioridad A (imprescindible), 37 B (deseable), 12 C (si está disponible).
- Dos caminos para Cruz Verde. Opción A: export transaccional de Mercado Pago (24 campos, una fila por intento de pago); con eso Yuno calcula 17 solicitudes completas y 15 parciales. Opción B: llenar las tablas resumen.
- Período pedido: septiembre de 2025 a agosto de 2026 (mínimo 6 meses). Cifras en COP.
- Cada solicitud trae prioridad, área sugerida (Ecommerce, Finanzas, TI), para qué se usa en el caso y, cuando existe, el dato que Cruz Verde ya nos dio (llamada 21-may o reunión 25-sep) para que lo confirmen o corrijan.

| Hoja | Contenido | Solicitudes |
|---|---|---|
| Instrucciones | Objetivo, cómo llenar, prioridades, confidencialidad, definiciones (hard y soft decline, intento vs orden) | |
| Resumen | Lista completa con estado y comentarios | |
| 1. Export | 24 campos con el nombre de referencia en la API de Mercado Pago | 1 |
| 2. Volumen | Mensual 12 meses, por canal, por rango de ticket, por tipo de entrega, proyección 2027 | 10 |
| 3. Mix de medios | Por medio de pago, por marca y tipo de tarjeta, origen y modalidad, efectivo, links | 5 |
| 4. Aprobación | Por banco emisor (top 15), por intento vs por orden, reintentos, 3DS | 8 |
| 5. Rechazos | 17 motivos con código status_detail y clasificación hard, soft, riesgo o datos; separación hard vs soft | 7 |
| 6. PSE y efectivo | Embudo de PSE, PSE por banco, embudo de efectivo | 5 |
| 7. Incidentes | Registro de caídas, tiempo sin servicio, alternativa actual | 6 |
| 8. Devoluciones | Por medio de pago, motivos, proceso PSE, contracargos y fraude | 12 |
| 9. Costos | Tarifas por medio, otros costos, contrato Mercado Pago, liquidaciones | 8 |
| 10. Conciliación | Proceso, fuentes, ERP, partidas abiertas, formatos | 13 |
| 11. Checkout | Embudo, plataforma, tipo de integración, dispositivos | 8 |
| 12. Nuevos medios | Nequi, Daviplata, Bre-B, Apple Pay, Google Pay, Addi, Sistecrédito, gift cards; estado con PayU, Redeban, Movii y Kushki | 7 |

## Decisiones y cuidados

- Respeta el pedido de Sandra: no se reabren las palancas L4 y L5. La única pregunta de horas (10.13, conciliación) es prioridad C y dice explícitamente que no entra a la sección de ahorros.
- Códigos de rechazo: son los que documenta Mercado Pago en `status_detail` (verificados en la documentación de Mercado Pago Colombia el 29-sep). Mercado Pago no tiene código propio para tarjeta vencida, robada o cuenta cerrada, así que esas filas piden el código del banco si lo tienen.
- La clasificación hard, soft, riesgo y datos es la propuesta de trabajo de Yuno y Cruz Verde la puede cambiar en cada fila. La tabla 5.2 contrasta su separación con la calculada desde la 5.1.
- Dato a aclarar con ellos: aprobación de PSE "casi 100%". La hoja 6 pregunta si se mide sobre pagos iniciados o finalizados.
- Dato a aclarar con ellos: las 20.000 transacciones en efectivo. La pregunta 3.4 pide la modalidad (contra entrega, recaudo en puntos u otra).
- Bre-B aparece como medio de interés de Cruz Verde. La disponibilidad de Bre-B en Yuno sigue sin verificar: no afirmarla.
- Fórmulas: 223, verificadas sin errores con un motor de cálculo en Python y con datos de prueba. No se recalcularon en Excel, así que en una vista previa (Quick Look, vista protegida) las celdas calculadas pueden verse en 0 hasta habilitar la edición.

## Correo (borrador Gmail)

Borrador vigente **r8537645621480480793** (cuarta versión, 29-sep tarde): reply en el hilo "Cruz Verde + Yuno" (threadId 1a0da6fca5a65b53, reply a 1a0da7e93f16f71d). To: Michael Vargas, Sandra P. Vargas, Andrés Guzmán, Edisson Olarte, Francy Silva, Santiago Castaño. Cc: Guillermo Gutiérrez, Alejandro Albarracín, Susana Awad, Carlos Medina.

German decidió ADJUNTAR el documento en vez de compartir el link. Cambios frente a la tercera versión: "les comparto" pasó a "les adjunto" y se agregó una línea sobre la reunión técnica con TI (nadie reservó los horarios ofrecidos el 25-sep).

Archivo para adjuntar: `Información para el business case - Cruz Verde + Yuno.xlsx` (esta carpeta). Es un export del Google Sheet en vivo hecho el 29-sep, así que trae las ediciones que German hizo a mano en el Sheet. Si el Sheet cambia, volver a exportar antes de enviar.

⚠️ El borrador anterior r5317102337443385744 ("les comparto") sigue en el hilo: el clasificador bloqueó el borrado. German lo descarta a mano.

⚠️ En el Sheet hay tres campos de costos con "desglozado" (debe ser "desglosado") y con " - " como separador. Son ediciones de German; no se tocaron.

Asunto: Re: Cruz Verde + Yuno

Hola Sandri, Mike, Andrew, Santi y equipo,

Como quedamos, les adjunto el documento con la información que necesitamos para construir el business case sobre las cifras reales de Cruz Verde.

Es una sola hoja: a la izquierda el campo que necesitamos y al lado el espacio para su respuesta. Cubre volumen y ventas, mix de medios de pago, aprobación, motivos de rechazo, devoluciones, disponibilidad, costos actuales, conciliación y nuevos medios de pago.

Si algún dato no está disponible, avanzamos con lo que tengan y acordamos un supuesto para el resto. Si les resulta más fácil, también pueden enviarnos un export transaccional de Mercado Pago de los últimos doce meses y nosotros calculamos las cifras.

No necesitamos datos personales de clientes ni números completos de tarjeta. Entendemos que la información la comparten una vez quede firmado el NDA, que ya está en trámite.

Mike, si te parece usamos la conversación que teníamos pendiente esta semana para recorrer el documento juntos y resolver dudas.

Sobre la reunión técnica con TI, cuéntenme qué día les funciona y envío la invitación.

Quedo atento. Gracias!

Saludos,
German

## Pendientes

- El follow-up del 25-sep prometió enviar este documento junto con la propuesta v2 (tiers, cifras en pesos, BC sin L4 y L5). El correo solo cubre el documento; la v2 sigue pendiente.
- No hay reunión de Cruz Verde en el calendario esta semana: ni la técnica con TI ni la conversación con Michael están agendadas.
