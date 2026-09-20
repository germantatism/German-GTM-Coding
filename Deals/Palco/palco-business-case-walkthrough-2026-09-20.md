# Palco: walkthrough profundo del business case (guía de estudio, 2026-09-20)

Para la reunión de propuesta del lunes 21-sep. Todos los números están verificados contra la tabla de Patricio del 2-sep y la base que fijó German: 235,000 transacciones al mes × $37.09. Nada usa el TPV de $457M.

## 1. La historia completa en 60 segundos

Palco nos mandó su aprobación por procesador. Siete procesadores de tarjeta aprueban entre 56% y 68% y concentran el 56% de sus transacciones. El mismo checkout aprueba 88% en España y 92% en el wallet de Mercado Pago, así que el problema es la ruta, no el producto ni el país. Sobre 235,000 transacciones al mes y un ticket de $37.09 medimos cuatro palancas. Dos recuperan ventas que hoy se rechazan (aprobación y failover). Una baja el costo de procesar (ruteo de menor costo). Una libera al equipo de Palco de mantener 50+ integraciones. Total: $5.5M conservador, $10.7M optimista, $8.1M punto medio. Las tres primeras benefician a los clientes de Palco porque son merchant of record; la cuarta es la única que cae en el P&L de Palco. Yuno cuesta $281K al año. Las ventas recuperadas son entre 18 y 36 veces ese costo. Todo se valida en un piloto en México con su propio baseline.

## 2. La base: de dónde sale cada número

- 235,000 transacciones al mes y $37.09 de ticket promedio: los dos los escribió Patricio el 2-sep.
- 235,000 × $37.09 = $8,716,150 al mes = $104,593,800 al año. Esto es la "base de modelación". Nunca decir "Palco procesa $104.6M": Patricio escribió $28.3M al mes.
- De la tabla por procesador solo se usan dos cosas: la tasa de aprobación de cada procesador y su peso relativo. Nunca sus volúmenes absolutos.
- La tabla suma 3,087,600 intentos al año, 2,187,480 aprobados (70.85%) y 900,120 rechazos.
- Tarjeta es 75.7% del volumen según su mix, así que la tarjeta de la base es $79.2M al año.

## 3. Palanca 1: aprobación en tarjeta ($4.7M a $9.3M al año)

**Qué es.** Subir la tasa de aprobación de los procesadores de tarjeta que hoy rinden mal pero funcionan.

**La cohorte.** Mercado Pago v2 (67.9%), Openpay (58.0%), Banorte (59.6%), Santander (56.1%), Cybersource (63.7%), Stripe (57.4%) y Bancard (58.1%). Suman 1,952,600 intentos al año con 1,218,482 aprobados: 62.4% ponderado. Esos aprobados son el 55.7% de todos los aprobados de la tabla.

**El cálculo, paso a paso.**
1. 55.7% de 235,000 = 130,900 transacciones aprobadas al mes pertenecen a esta cohorte.
2. Si esas son el 62.4% de los intentos, los intentos son 130,900 ÷ 0.624 = 209,800 al mes. Los rechazos son 78,900 al mes.
3. Conservador, +5 puntos: 209,800 × 5% = 10,490 transacciones más al mes, 125,860 al año, × $37.09 = $4.67M.
4. Optimista, +10 puntos: 20,980 al mes, 251,720 al año, × $37.09 = $9.34M.

**Por qué +5 y +10.** Son anclas que ellos reconocen, no promesas. 62.4% + 5 = 67.4%, que es lo que Mercado Pago ya les aprueba en tarjeta hoy (67.9%). 62.4% + 10 = 72.4%, que es el promedio del mercado mexicano en crédito (~72% crédito, ~69% débito, RankingsLatAm sep-2024). Dicho de otra forma: el conservador recupera el 13% de los rechazos de la cohorte y el optimista el 27%. La cifra publicada de Yuno es 30% de ingresos recuperados y 7% de uplift en autorización; los dos escenarios quedan alrededor de eso, no por encima.

**Cómo se logra, mecánicamente.**
- Reintento por otra ruta: un rechazo blando (do not honor, emisor no disponible, error del procesador) se reenvía a otro adquirente en milisegundos. El comprador nunca ve el primer rechazo.
- Ruteo por BIN y emisor: cada tarjeta va al adquirente que mejor aprueba ese banco emisor. Una tarjeta Banorte suele aprobar mejor en adquirencia Banorte.
- 3DS selectivo: si hoy el 3DS corre en el 100% de los flujos, cada abandono del challenge y cada autenticación fallida cuenta como rechazo. Aplicarlo por regla (monto, BIN, riesgo) y con exenciones quita fricción donde no aporta.
- Tokenización y network tokens: credenciales que el emisor reconoce y que sobreviven al cambio de plástico. Importa sobre todo para abonos.
- Monitores: en un on-sale, si un procesador se degrada, el tráfico se redistribuye solo.

**Qué tiene que ser cierto.**
- El tenant necesita al menos dos rutas conectadas. Con un solo procesador no hay reintento ni ruteo; solo quedan 3DS selectivo, tokens y monitores. Es el punto más débil de la palanca y el criterio para elegir tenants del piloto. Alfonso ya lo imagina así ("si tira por Santander mejor tasa que por BBVA").
- Openpay, Banorte, Santander y Mercado Pago deben estar en el catálogo de Yuno. Pendiente de Carlos.
- No todos los rechazos son recuperables: fondos insuficientes y rechazos duros no lo son. Por eso el caso asume recuperar entre 13% y 27%, no 100%.

**Sensibilidades que debes tener en la cabeza.**
| Si dicen | La palanca 1 queda en |
|---|---|
| "Saca a Mercado Pago, ya aprueba 68%" | $2.9M a $5.7M (cohorte de 6, 58.9%, 128,700 intentos al mes) |
| "Solo México: Openpay, Banorte, Santander" | $2.4M a $4.8M (58.5%, 107,600 intentos al mes) |
| "Las 235,000 incluyen efectivo y taquilla" | Escala con la porción tarjeta; a 75.7%, $3.5M a $7.1M |
| "El $37.09 es por boleto, la compra es de ~$120" | Se multiplica por ~3 |

**Dos números para memorizar.** Cada punto de aprobación en la cohorte vale 2,098 transacciones al mes y $934K al año. Con 0.3 puntos de mejora las ventas recuperadas ya igualan el costo anual de Yuno.

## 4. Palanca 2: failover en rutas rotas ($0.52M a $0.86M al año)

**Qué es.** Rescatar dos rutas que aprueban menos de la mitad: Fiserv 43.7% y Pixel Pay (Honduras) 52.3%. No es optimización, es una ruta que falla de forma estructural.

**El cálculo.**
1. Fiserv 48,100 + Pixel Pay 39,900 = 88,000 intentos al año, 41,888 aprobados, 47.6%.
2. Esos aprobados son el 1.9% del total. Sobre la base: 4,500 aprobadas al mes y 9,454 intentos al mes.
3. A 60%: 9,454 × 60% = 5,672, menos 4,500 = 1,172 más al mes → $0.52M al año.
4. A 68%: 6,429 menos 4,500 = 1,929 más al mes → $0.86M al año.

**Por qué 60% y 68%.** 60% es el nivel de su propia cohorte principal (62.4%); 68% es su mejor riel de tarjeta en LatAm (Mercado Pago 67.9%). Llevar una ruta rota al nivel de sus rutas normales.

**Cómo se logra.** Monitores con umbral por ruta. Cuando la aprobación cae por debajo del umbral, el tráfico se mueve a una ruta alterna y una fracción pequeña sigue probando la original hasta que se recupere.

**Por qué Line (Venezuela) queda fuera.** Aprueba 8.7%. Eso no lo arregla ningún ruteo; es un problema de mercado. Incluirlo inflaría el caso. Decirlo en voz alta da credibilidad.

**Sin doble conteo.** Fiserv y Pixel Pay no están en la cohorte de la palanca 1.

**Qué tiene que ser cierto.** Debe existir una ruta alterna en esos mercados, en el catálogo de Yuno y con cuenta del tenant. Pendiente de Carlos. Ojo: Patricio no etiquetó el país de Fiserv; Uruguay es inferencia nuestra, no afirmarlo.

**Número útil.** Cada punto en estas rutas vale $42K al año. Es una palanca chica; se presenta por rigor, no por tamaño.

## 5. Palanca 3: costo de procesamiento ($59K a $99K al año)

**Qué es.** A igual probabilidad de aprobación, mandar cada transacción al adquirente más barato.

**El cálculo.** 7.5 a 12.5 puntos básicos sobre $79.2M de tarjeta de la base. Un punto básico = $7,918 al año.

**De dónde sale el rango.** Es un supuesto de modelación de Yuno, no un benchmark publicado. Se reemplaza con su MDR real por procesador cuando lo compartan. Decirlo así.

**Cómo se logra.** El dashboard permite cargar el costo de cada procesador (por transacción exitosa, fallida, fijo o porcentual) y el smart routing optimiza por conversión más costo. Suma el poder de negociación: con dos adquirentes conectados, el tenant puede mover volumen al que cobre menos. Es el ejemplo que German dio el 15-sep (15 centavos vs 11).

**Quién se lo queda.** El tenant, que es quien paga el MDR. Los contratos siguen siendo de cada tenant; no depende de renegociar.

**La verdad incómoda.** Es la palanca más chica y NO paga a Yuno por sí sola: 7.5 a 12.5 bps contra 27 bps de costo. Alfonso espera lo contrario. Hay que decirlo primero: lo que paga es la aprobación.

**Solo si ellos lo traen:** si Patricio dice "nuestra tarjeta son $346M", la palanca escala a $260K a $433K. No usarlo en el deck.

## 6. Palanca 4: run-ops de integraciones ($230K a $360K al año)

**Qué es.** Lo que Palco deja de gastar en mantener su propia capa de pagos.

**El cálculo.** 3 a 4 FTE de ingeniería a un costo cargado de $77K a $90K. Supuesto de modelación de Yuno. Palco tiene 42 a 47 empleados, así que serían 7% a 9% de la plantilla.

**Qué trabajo es.** Mantener 50+ conectores vivos (cambios de versión de API, certificados, mandatos como los nuevos datos de 3DS de Mastercard de 2026), integrar pasarelas nuevas por cada país, onboarding manual de cada tenant, atender incidentes en on-sales. Fernando lo llamó "cuello de botella sumamente costoso".

**Cómo decirlo.** "Libera", nunca "reemplaza". No es recorte: el equipo de Alfonso pasa de mantener conectores a construir producto de ticketing. Y las integraciones siguen siendo suyas.

**Por qué es la más importante para Patricio.** Es la única que cae directo en el P&L de Palco, y sola cubre entre 82% y 128% del costo anual de Yuno.

**Cómo volverla de ellos.** Preguntar a Alfonso: "¿cuántas personas de tu equipo tocan integraciones de pago en un trimestre normal?" Si dice 2, la palanca baja a ~$170K; si dice 5, sube a ~$420K. En ambos casos el número pasa a ser suyo.

**Lo que no está cuantificado.** El costo de oportunidad: entrar a un país nuevo sin construir sus pasarelas. Es el mandato de expansión de los dueños nuevos.

## 7. Escenarios, quién captura y valor contra costo

| | L1 | L2 | L3 | L4 | Total |
|---|---|---|---|---|---|
| Conservador | $4.67M | $0.52M | $59K | $230K | $5.5M |
| Optimista | $9.34M | $0.86M | $99K | $360K | $10.7M |
| Punto medio | $7.0M | $0.69M | $79K | $295K | $8.1M |

- El punto medio es un promedio simple, no un pronóstico.
- Es un caso anual en régimen, no del año uno. El piloto arranca con 3 a 5 tenants.
- **Ventas recuperadas (L1 + L2): $7.7M punto medio, $5.2M a $10.2M.** Llegan a los tenants. Palco gana su fee sobre ese volumen: cada punto de fee son $77K al año.
- **Ahorro de MDR (L3): $79K.** También de los tenants.
- **Ahorro operativo (L4): $295K.** De Palco.
- **Costo de Yuno: $280,845 al año** ($23,404 al mes con 3DS selectivo y antifraude). $0.10 por transacción, 27 bps sobre $37.09.
- Para el tenant: paga 27 bps y vende entre 8% y 16% más en la cohorte.

## 8. Lo que el caso NO incluye (upside sin cuantificar)

- Métodos de pago y países nuevos sin construirlos, que es el interés número uno de Fernando.
- Fraude y contracargos: no hay dato consolidado porque cada tenant es MoR.
- Preventas bancarias por BIN con meses sin intereses.
- Abonos y recurrencia.
- La diferencia boleto vs compra (~3x).
- El ingreso que Palco puede generar empaquetando pagos a sus clientes.

## 9. Banco de preguntas difíciles

| Pregunta | Respuesta |
|---|---|
| "¿De dónde sacan 5 y 10 puntos?" | "De ustedes: 67% es lo que Mercado Pago ya les aprueba en tarjeta; 72% es el mercado mexicano en crédito. No es una promesa de Yuno, es llegar a lo que ya existe." |
| "¿Todos los rechazos se recuperan?" | "No. Fondos insuficientes y rechazos duros no. El caso asume recuperar entre 13% y 27% de los rechazos de la cohorte." |
| "Nuestros clientes tienen una sola pasarela" | "Entonces para ese cliente aplican 3DS selectivo, tokens y monitores, no reintento. Por eso el piloto se arma con tenants que tengan o abran dos rutas. La segunda cuenta sigue siendo del cliente." |
| "¿Por qué está Mercado Pago si ya aprueba 68%?" | "Porque es su mayor volumen y su wallet aprueba 92% con el mismo proveedor. Sin Mercado Pago la palanca queda en $2.9M a $5.7M." |
| "¿Eso es dinero para Palco?" | "No directo. Es venta de sus clientes. Palco gana su fee sobre ese volumen y, sobre todo, tiene un producto que vender. Lo directo de Palco es la palanca 4." |
| "¿El ahorro de ruteo paga a Yuno?" | "No. Son 7 a 12 bps contra 27. Lo paga la aprobación." |
| "¿De dónde salen los 3 a 4 FTE?" | "Es un supuesto nuestro. Alfonso, ¿cuántas personas tocan integraciones de pago en un trimestre?" |
| "¿Por qué no está Venezuela?" | "Porque 8.7% no es un problema de ruteo y meterlo inflaría el caso." |
| "¿Y si el piloto no mueve la aguja?" | "Tienen la data con su propio baseline a 90 días y deciden. No hay contrato a tres años de por medio." |
| "Nuestro volumen es mucho mayor que $104M" | "Correcto, por eso lo llamamos base de modelación: son sus 235,000 transacciones por su ticket de $37.09. Si el ticket es por boleto y la compra es mayor, todo el caso escala en esa proporción." |
| "¿El 3DS selectivo es legal en México?" | No afirmar. "Depende de quién lo exige: el adquirente, el tenant o Palco. ¿Quién lo exige hoy?" |
