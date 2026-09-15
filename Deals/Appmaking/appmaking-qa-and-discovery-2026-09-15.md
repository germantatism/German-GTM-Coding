# Appmaking: dominio de las preguntas de Tatsiana y discovery para la call del 15-sep

Decisión de German (14-sep noche): NO mostrar la propuesta mañana. La call es para dominar sus preguntas, hacer discovery y llevarlos a la decisión. La propuesta se manda después con los inputs cerrados.

## 1. Las preguntas de Tatsiana, lo que respondimos y lo que hay detrás

### Q1. "Sample de reporte TC40 y SAFE, en el formato en que lo entregarían" (8-sep)
**Lo que respondimos (14-sep):** no entregamos archivos. Cuando el banco del tarjetahabiente reporta fraude a Visa (TC40) o a Mastercard (SAFE), el proveedor nos pasa la alerta y nosotros avisamos por pago con el webhook `payment.pre_chargeback`. Es un aviso temprano: el pago sigue aprobado, no se ha movido plata, pueden reembolsar o bloquear al cliente antes de que sea contracargo. Payload ilustrativo con valores genéricos. Corrección explícita al recap del 4-sep: hoy es notificación por pago, no reporte consolidado; vistas en dashboard y reportes en roadmap; cobertura depende de que cada proveedor nos pase la data de red; vive con "select providers". Se scopea contra su fase 1 en la call.
**La verdad interna:** Leo (Andres Leonardo Moreno) es el dueño. dLocal deja archivos en SFTP, el equipo de Thiago los baja, Leo los convierte en webhook. El ejemplo real de Leo venía de Adyen (NOTIFICATION_OF_FRAUD). Ninguno de los dos está en su fase 1, y Adyen además lo tienen bloqueado por la exclusividad con Solidgate. Jira: YSHUB-6715 y PRIOR-513.
**Qué es y por qué lo pide:** TC40 y SAFE son los registros de fraude confirmado que los emisores reportan a Visa y Mastercard. Las redes los usan para sus programas de monitoreo (Visa VFMP y VDMP, Mastercard ECM), que umbralan por ratio de fraude y de contracargos por MID (cifras públicas de referencia, verificar antes de citarlas: Visa 0.9% de fraude y $75K, o 0.9% y 100 contracargos; Mastercard 1.5% y 100 contracargos). Un merchant MCC 8999 con funnel web vive de no cruzar esos umbrales. Ella quiere ver el fraude por PSP antes de que se vuelva contracargo, y en el 4-sep pidió además "bank rates y fraud rates por PSP", que es un agregado que hoy no existe en Yuno.
**Lo que tienes que dominar en vivo:** (a) hoy es un aviso por pago vía dLocal (y Adyen por confirmar), no un reporte; (b) para Stripe, Ecompay, Unlimit, Airwallex, Shift4, Payabl y NMI hay que ver proveedor por proveedor si pasan la data; (c) lo que de verdad protege sus ratios son las alertas pre-disputa (Q4) más reembolso automático, no el reporte.

### Q2. "¿Tienen práctica de presentar merchants a bancos?" (8-sep)
**Lo que respondimos (10-sep):** diferido a la call: "happy to discuss our network and how we typically support our merchants in those conversations."
**La verdad interna:** Yuno tiene relaciones comerciales con adquirentes y PSPs del catálogo; puede presentar al merchant con sus contactos; el merchant contrata directo; Yuno no es referidor pagado, no participa en underwriting ni está en el flujo de fondos. No hay un programa formal que puedas prometer. Acordar la frase con Sean.
**Por qué lo pide:** son alto riesgo (astrología, suscripción web, MCC 8999); la capacidad de adquirencia es su cuello de botella real. Su marca hermana rota cuatro entidades MoR (Chipre, Hong Kong, EE.UU., Dubái) justamente por eso. Payabl está firmado y no live. Buscan que el orquestador les abra puertas de adquirencia en mercados nuevos (Japón, LatAm).
**Lo que tienes que dominar:** la pregunta no es de cortesía. Conviértela en discovery: qué mercados, qué entidad contrataría, qué volumen le pondrían a un adquirente nuevo, qué les pasó con adquirentes anteriores. Y la respuesta comercial honesta: los adquirentes dicen que sí cuando el ratio de contracargos está controlado; ruteo más alertas es lo que hace que la intro funcione.

### Q3. "Confirmar si el TRID queda abierto bajo nuestra propia entidad merchant" (14-sep)
**Lo que respondimos (14-sep):** dos modos. Default: Yuno provisiona los network tokens con Visa, Mastercard y Amex en nombre de ellos, cero integración extra, provisioning y ciclo de vida con el token requestor de Yuno, "los tokens son suyos, usables dentro y fuera de Yuno". Passthrough: ellos se registran como token requestor ante las redes y mandan su `token_requestor_id` por API; Yuno es passthrough. "Si el requisito es TRID bajo su entidad, los configuramos en passthrough desde el día uno."
**El matiz que no puedes fallar:** un network token está ligado al token requestor que lo provisionó. Con el TRID de Yuno, el token de red es de Yuno como requestor; lo que es portable es la tarjeta subyacente en el vault (exportación de PAN, PCI proxy). Con su propio TRID, los network tokens son de ellos y viajan con ellos a cualquier proveedor que los acepte. Si lo que Tatsiana quiere es "que los tokens sobrevivan si nos vamos de Yuno" o "usarlos directo en Solidgate", la respuesta correcta es passthrough con TRID propio, no "los tokens son suyos" a secas.
**Pendiente interno:** la documentación dice que `token_requestor_id` es "only required for certain providers"; confirmar con Jarrett que passthrough funciona con sus PSPs fase 1, y que esos PSPs aceptan network token más criptograma de un requestor externo (algunos solo aceptan sus propios tokens). Esa es la misma matriz que Hostinger pidió.
**Por qué lo pide:** independencia. Hoy sus tokens probablemente viven bajo el TRID de Solidgate y del segundo orquestador. Migrar tokens entre orquestadores es doloroso; ella quiere que la tercera capa no repita el candado. En la call del 4-sep lo dijo: portabilidad de tokens, "the treat is ours".

### Q4. "¿Quién es su proveedor de prevention alerts?" (14-sep)
**Lo que respondimos (14-sep):** integración directa con Ethoca (red de alertas de Mastercard); cuando el emisor marca la transacción, la alerta llega por Yuno en tiempo real y pueden reembolsar antes de que sea contracargo. "Cobertura del lado Visa y roadmap en la call de mañana."
**La verdad interna:** Ethoca es público (lanzamiento abril 2025, Finextra y Fintech Times). Verifi (Visa: CDRN, RDR, Order Insight) NO está confirmado; un borrador interno decía "RDR y Ethoca being relaunched". Mañana solo puedes decir lo que Jarrett o Leo confirmen.
**Qué es y por qué lo pide:** Ethoca (propiedad de Mastercard) y Verifi (propiedad de Visa) son las dos redes de alertas pre-disputa; las alertas las generan emisores participantes, y en la práctica cubren tarjetas de varias marcas según el emisor; RDR (Verifi) resuelve la disputa automáticamente con reglas de reembolso. Para un merchant de suscripción alto riesgo, las alertas son el seguro contra los programas de monitoreo. Casi seguro ya las tienen vía Solidgate o directo; la pregunta es si Yuno las trae integradas para el volumen que pase por Yuno y a qué precio (en la call del 4-sep pidieron el pricing de Verifi y Ethoca). En la industria se cobran por alerta; en Yuno el precio no está en la calculadora: "priced separately", no inventar.

### Q5. "Lista completa de PSPs con los que trabajan" (14-sep)
**Lo que respondimos (14-sep):** catálogo vivo, 1,000+ integraciones en 190+ países; snapshot por mercado: US (Stripe, Braintree, Worldpay, Nuvei, Shift4, NMI, Airwallex, ACI Worldwide, Tabapay, dLocal cross-border), Europa (Stripe, Worldpay, Nuvei, Unlimit, Ecompay, Payabl, Airwallex, ACI, Braintree, Shift4), Japón (Stripe, Worldpay, 2c2p y adquirentes locales "a detallar en la call"), LatAm (dLocal, EBANX, Mercado Pago, PayU, Kushki, Stripe y adquirentes locales de Brasil y México). "Full coverage of your phase 1 providers."
**Pendientes internos:** Shift4 y Payabl no aparecen en la lista de 75 proveedores que Yuno puso en el RFP de Hostinger (Ecommpay, Unlimint, NMI, Airwallex y Stripe sí). Verificar en el catálogo antes de repetir "full coverage". Japón: GMO, SB Payment, Univapay, Komoju son candidatos, ninguno verificado. Excluidos siempre: Adyen, JPMorgan, Checkout.com (exclusividad Solidgate) y Solidgate.
**Por qué lo pide:** dos lecturas posibles y conviene aclararla en vivo: (a) cobertura de su fase 1 y de su expansión, o (b) con qué PSPs Yuno ya mueve volumen real (conectores probados, no solo listados). Si es (b), la respuesta honesta es distinta a un catálogo.

### Q6. Pricing por escrito sobre su ramp (8-sep, insistió el 10-sep)
**Estado:** curva recibida (20K a 150K en 7 meses, AOV $18). Dijiste "esta semana" el 10-sep y luego propusiste revisarlo en call. No se ha enviado nada. Mañana no lo vas a mostrar.
**Cómo manejarlo sin quemar confianza:** decir que la propuesta está construida y que antes de compartirla quieres cerrar tres inputs que mueven el número: qué productos entran (subs standalone, vault y tokens, reconciliación, alertas), qué PSPs y qué volumen por PSP, y qué entidad contrata. Comprometer fecha concreta (jueves 17 o viernes 18) y cumplirla. Es la tercera vez que lo piden; una cuarta sin fecha es un problema.

### Lo que pidieron en la call del 4-sep y no volvió a escribirse
Portabilidad de network tokens (Q3), TC40/SAFE (Q1), bank rates y fraud rates por PSP (no existe como agregado), pricing de alertas Verifi y Ethoca (Q4, no cotizar), sandbox (entregado, "loved it"), documentación (docs.y.uno), productos AI (Concierge y Nova, prometidos para esta call). Y la corrección que ya hiciste por escrito: el recap decía "normalized reports across all your providers" y no era cierto.

## 2. Discovery: qué preguntar y qué cuestionar para llevarlos a la decisión

### A. El volumen y de dónde sale
1. La curva de 20K a 150K: ¿es tráfico nuevo del funnel, volumen que hoy va por Solidgate y el segundo orquestador, o ambos? ¿Qué porcentaje del volumen web total del grupo sería el 150K?
2. ¿Qué marcas y qué entidades mandan ese volumen (Atrix, otras apps del grupo)? ¿Una cuenta o varias?
3. Reparto por mercado (EU, US 40%, Japón, LatAm) y por PSP fase 1. ¿Cuáles de los siete están live hoy y con qué volumen? ¿Por qué Payabl está firmado y no live?
4. Aprobación por PSP y por mercado hoy. ¿Nos pueden compartir 2 o 3 meses de aprobaciones y rechazos por geo y PSP bajo el NDA? Sin eso no hay baseline para medir uplift.

### B. El segundo orquestador y la lógica de "diversificar"
5. "The performance of the second orchestrator isn't so good": ¿en qué exactamente, aprobación, caídas, soporte, costo, reporting? ¿Qué tendría que pasar para mover todo ese volumen fuera de él?
6. ¿Por qué una tercera capa y no reemplazar la segunda? ¿Qué reparto máximo por capa tienen en mente? (Aquí cuestionas: tres capas son tres integraciones y tres vaults; la independencia está en dónde vive la tarjeta y en poder mover volumen sin proyecto, no en el número de capas.)
7. Contrato con Solidgate: plazo, renovación, mínimos, alcance real de la exclusividad (¿solo Adyen, JPM y Checkout, o más?). Si están amarrados, Yuno es la capa de crecimiento; si renuevan pronto, Yuno es la palanca de negociación.
8. ¿Están evaluando otras terceras capas? ¿Qué criterios pesan más: independencia, cobertura, precio, soporte?

### C. Dónde vive la tarjeta y quién factura la suscripción
9. ¿Dónde están vaulteadas las tarjetas hoy: Solidgate, el segundo orquestador, ambos? ¿Cuántas tarjetas on-file? ¿Tienen network tokens activos y bajo qué TRID?
10. ¿Ya tienen TRID propio o lo abrirían para esto? ¿Han migrado tokens alguna vez y cómo les fue?
11. ¿Quién dispara la renovación: el motor de suscripciones de Solidgate, uno propio, otro billing? Si el billing se queda en Solidgate, ¿qué papel tendría Yuno en las renovaciones? (Esto decide si "subscriptions standalone" entra o no en la propuesta.)
12. Reintentos y dunning: cuántos intentos, en qué ventana, quién decide el momento. ¿Cuánto revenue pierden por renovaciones fallidas al mes?
13. 3DS y wallets: ¿quién corre 3DS hoy, qué tasa de challenge en EU, cómo manejan Apple Pay y Google Pay en el funnel web? (En la call del 4-sep pidieron una autenticación por encima de la capa PSP.)

### D. Riesgo, disputas y adquirencia (Q1, Q2, Q4 convertidas en discovery)
14. Ratio de contracargos y de fraude por MID hoy. ¿Algún MID cerca de umbral de programa de Visa o Mastercard? ¿Han estado en un programa antes?
15. ¿Tienen alertas hoy (Ethoca, Verifi, vía Solidgate o directo)? ¿Cuántas alertas al mes, qué pagan, qué porcentaje reembolsan automáticamente?
16. ¿Quién responde disputas hoy y con qué herramienta? ¿Cuántas por mes?
17. Herramientas de fraude: ¿propias, de Solidgate, terceros? ¿Cuánto les preocupan los falsos rechazos frente al fraude?
18. Bancos: ¿en qué mercados necesitan adquirencia nueva, con qué entidad, qué volumen le pondrían? ¿Qué les pasó con adquirentes anteriores? (Cuestionar: un adquirente nuevo sin ratios controlados dura poco; el orden es ruteo y alertas primero, intro después.)

### E. Operación y entidades
19. ¿Cómo concilian hoy dos orquestadores por varias entidades y quién lo hace? ¿Cuántas horas al mes?
20. ¿Qué entidad contrata (Appmaking LTD, el MoR del funnel web u otra) y quién firma? ¿Necesitan una cuenta por entidad?
21. Moneda y métodos por mercado: ¿cobran en moneda local en Japón, Brasil, India? ¿Qué métodos locales tienen hoy y cuáles quieren?

### F. Decisión, criterios y tiempo
22. ¿Quién toma la decisión final y quién más tiene que aprobar? ¿Qué papel tiene legal (Butrym) y cuándo entra?
23. ¿Cuál es el criterio de éxito de la fase 1: puntos de aprobación, caídas evitadas, costo, tiempo de integración? ¿Cómo lo van a medir y contra qué baseline?
24. ¿Qué haría que subieran el reparto hacia Yuno por encima del plan?
25. Timeline: ¿cuándo quieren estar live con fase 1, quién integra, cuántos desarrolladores, y cuándo necesitan el pricing para decidir?

### Lo que conviene cuestionar, con cuidado y sin decir "les falta"
- **"Diversificar" sin baseline no se puede medir.** Pedir la data de rechazos por PSP y geo es el paso que convierte una conversación de proveedores en una de resultados.
- **Tres capas y tokens en la capa equivocada no es independencia.** Si las tarjetas siguen bajo el TRID de Solidgate, cambiar de capa sigue costando lo mismo. La independencia que dicen querer se llama vault propio y TRID propio.
- **Un segundo orquestador que "no rinde" no se arregla con un tercero.** O se mide y se sustituye, o se reduce. Yuno quiere ser el destino de ese volumen, no un tercio de un experimento.
- **Payabl firmado y no live es la prueba de lo que cuesta integrar por cuenta propia.** Preguntar cuánto llevan y por qué. Con un orquestador, un PSP nuevo es configuración, no proyecto.
- **TC40 como reporte es visibilidad tardía; alertas más reembolso automático es protección.** Lo que baja el ratio es actuar antes del contracargo.
- **Intro a bancos sin ratios controlados es una puerta que se cierra sola.** El orden correcto es ruteo y alertas, luego adquirencia nueva.
- **El pricing sin productos definidos es un número sin contexto.** Por eso mañana cierras los inputs y mandas la propuesta con fecha.

### Cómo cerrar la call
- Resumir lo que quedó claro de sus cinco preguntas y lo que se verifica por escrito (TC40 por proveedor, TRID passthrough con sus PSPs, Verifi, Shift4 y Payabl, adquirentes de Japón).
- Pedir la data de aprobaciones por PSP y geo bajo NDA.
- Confirmar productos que entran, entidad que contrata y timeline de fase 1.
- Fecha concreta para la propuesta escrita y para la siguiente call con el número.
