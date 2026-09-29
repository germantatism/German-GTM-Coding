# Cruz Verde · solicitud de información para el business case (2026-09-29)

Cruz Verde pidió que Yuno les solicite todos los datos necesarios para construir el business case lo más a la medida posible (ejemplo de German: hasta el porcentaje de rechazos que son hard y los que son soft). Es el "documento de información requerida" prometido en el follow-up del 25-sep.

## Entregable que se envía: Google Sheet

"Cruz Verde + Yuno | Información para el business case": https://docs.google.com/spreadsheets/d/1xipYBM6dNEVmCj_cxezIAqsfMb-gbPCimMJmXaGIMJQ/edit (carpeta Drive "Cruz Verde", dueño German). Pedido de German el 29-sep: formato de formulario, el campo a la izquierda y al lado el espacio para que Cruz Verde ponga sus números.

- 13 hojas: Inicio, 1. Export y las hojas 2 a 12. 878 celdas amarillas para llenar y 104 listas desplegables. Configuración regional es_CO (1.000 y 90,0%).
- Mismo contenido que el Excel (90 solicitudes), sin columnas calculadas, totales ni filas de ejemplo. No tiene hoja Resumen: el índice está en Inicio.
- Tablas: campo en la columna A, respuestas de la B en adelante. Preguntas: campo, respuesta, prioridad y lo que nos han compartido por confirmar.
- Se genera con `build/build_data_request_gsheet.py`, que toma el contenido de `build/build_data_request.py` y lo escribe con la Sheets API y la service account. El Sheet lo creó el conector de Drive y el mismo conector lo compartió con la service account como Editor.
- ⚠️ `--rebuild` borra y recrea las hojas: no usarlo cuando Cruz Verde ya haya escrito datos.
- German comparte el Sheet con Cruz Verde desde la interfaz. La service account aparece en la lista de personas con acceso; se puede quitar antes de compartir.

## Excel (respaldo)

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

Borrador r5433334866971531362: reply en el hilo "Cruz Verde + Yuno" (threadId 1a0da6fca5a65b53, reply a 1a0da7e93f16f71d). To: Michael Vargas, Sandra P. Vargas, Andrés Guzmán, Edisson Olarte, Francy Silva, Santiago Castaño. Cc: Guillermo Gutiérrez, Alejandro Albarracín, Susana Awad, Carlos Medina. German agrega el link del Google Sheet. Reemplaza al primer borrador, que hablaba de un adjunto.

Asunto: Re: Cruz Verde + Yuno

Hola Sandri, Mike, Andrew, Santi y equipo,

Como quedamos, les comparto el documento con la información que necesitamos para construir el business case sobre las cifras reales de Cruz Verde.

Lo armamos con el mayor nivel de detalle posible para que el caso quede a la medida de su operación. Está en formato de formulario: a la izquierda el campo que necesitamos y al lado el espacio para su respuesta. Cubre volumen y ventas, mix de medios de pago, aprobación en tarjetas, motivos de rechazo con la separación entre rechazos definitivos y temporales, PSE y efectivo, incidentes, devoluciones y contracargos, costos actuales, conciliación, checkout y nuevos medios de pago.

Hay una alternativa más rápida para ustedes: compartirnos un export transaccional de Mercado Pago de los últimos doce meses con los campos que detallamos en la hoja de export. Con eso nosotros calculamos buena parte de las tablas y ustedes completan solo el resto. Cada tabla tiene una prioridad, así que si algún dato no está disponible avanzamos con lo imprescindible y acordamos un supuesto para lo demás.

No necesitamos datos personales de clientes ni números completos de tarjeta. Entendemos que la información la comparten una vez quede firmado el NDA, que ya está en trámite.

Mike, si te parece usamos la conversación que teníamos pendiente esta semana para recorrer el documento juntos y resolver dudas.

Quedo atento. Gracias!

Saludos,
German

## Pendientes

- El follow-up del 25-sep prometió enviar este documento junto con la propuesta v2 (tiers, cifras en pesos, BC sin L4 y L5). El correo solo cubre el documento; la v2 sigue pendiente.
- No hay reunión de Cruz Verde en el calendario esta semana: ni la técnica con TI ni la conversación con Michael están agendadas.
