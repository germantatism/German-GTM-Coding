# QA del deck "Propuesta - Palco + Yuno" v2 (20 slides), 2026-09-16

Deck: https://docs.google.com/presentation/d/1hWX6sNKKPpXhDSKGlZzrHWyKWMx5WlVxBeScEL_J7UY/edit
Cambios de German sobre la v1: agenda 02 = Business Case; divisor 12 = Business Case; slide 13 nuevo (cuatro palancas); slide 14 reconstruido (Impacto total); slide 15 nuevo (pricing en layout Flair, $7,000 + $0.06/$0.055/$0.045); lockup Palco con tagline en portada y cierre.
Fuentes de verificación: correo de Patricio 2-sep (volúmenes, mix, aprobación por procesador), hoja "Yuno — Pricing Matrix & Deal Calculator" (Suggested), transcript 15-sep, research 8-sep, brief 9-sep (benchmark MX RankingsLatAm sep-2024: ~72% crédito, ~69% débito).

## A. Aritmética verificada (todo cuadra)

Business case (S13 y S14):
- 3,087,600 intentos; aprobados 2,187,480 = 70.8%; declinados 900,120 = 75,010/mes. OK.
- Cohorte L1 = MP v2 754,700 + Openpay 506,700 + Banorte 420,400 + Cybersource 109,800 + Santander 74,800 + Stripe 55,900 + Bancard 30,300 = 1,952,600. Aprobación ponderada 1,218,482 / 1,952,600 = 62.4%. OK.
- Ticket $163 = $346M TPV tarjeta / 2.12M aprobadas (2,187,480 menos 67,141 de MP Wallet). OK, derivación válida.
- L1: +5 pp = 97,630 tx × $163 = $15.9M; +10 pp = 195,260 × $163 = $31.8M. OK.
- L2: Fiserv 48,100 (43.7%) + Pixel Pay 39,900 (52.3%) = 88,000; mezcla 47.6%. A 60% = +10,912 × $43.10 = $0.47M; a 68% = +17,952 × $43.10 = $0.77M. OK.
- L3: $346M × 7.5 bps = $0.26M; × 12.5 bps = $0.43M. OK.
- Totales: conservador $16.9M, optimista $33.4M, promedio $25.1M; tarjetas $24.5M (rango $16.4M a $32.6M), $0.35M, $0.30M. OK.

Pricing (S15):
- Tramos: 58,750 × 0.06 = $3,525; 58,750 × 0.055 = $3,231; 117,500 × 0.045 = $5,288; total $12,044/mes, $144,525/año. Plataforma $7,000 / $84,000. Subtotal $19,044 / $228,525. 3DS 100,000 × $0.04 = $4,000 / $48,000. Antifraude 20,000 × $0.018 = $360 / $4,320. Total $23,404 / $280,845. OK.
- All-in $0.081 y $0.100 por tx; a 300,000: $21,969 ≈ $0.073. OK.
- Política (calculator): plataforma $7,000 > green-down-to $6,325; tramos $0.06/$0.055/$0.045 > $0.026/$0.0227/$0.0204; 3DS $0.04 > $0.0284; antifraude $0.018 > $0.0113; deal $23.4K/mes > mínimo $10K. Sigue GREEN.

## B. Bloqueantes (cambiar antes del lunes)

1. Notas del orador del slide 11 en inglés y mencionan a Kraken ("Yuno gives Kraken..."). Borrarlas. Si exportas a PDF con notas o compartes el archivo, sale.
2. Slide 13, bloque Supuestos: dice "Palancas 1 y 2 modeladas... con un ticket de $163", pero la palanca 2 se calculó con $43.10 (si fuera $163, L2 sería $1.78M, no $0.47M). Corregir: "Palanca 1 con un ticket de $163 por transacción de tarjeta... Palanca 2 con $43.10".
3. Slide 13, palanca 1: "Hoy el 3DS es obligatorio en todos los flujos de tarjeta" se afirma como hecho. Solo sabemos que Patricio lo puso como pregunta (2-sep). Cambiar a: "Si el 3DS aplica a todos los flujos de tarjeta, como plantearon, gestionar exenciones por riesgo, reintentar sobre otra ruta y tokenizar es la vía directa sobre esa brecha".
4. Slide 15, Risk conditions a $0.04 por trx evaluada. La hoja sugiere $0.0139 (piso $0.0070). $0.04 es casi 3x el sugerido y más caro que el 3DS; parece copiado del 3DS. Si es intencional, sostenerlo; si no, $0.014 (consistente con el redondeo de 3DS 0.0403 → 0.04 y antifraude 0.0184 → 0.018).
5. Slide 15, 3DS a 100,000 autenticaciones/mes: sus intentos de tarjeta son ~257,000/mes. Si el 3DS es obligatorio al 100%, el costo real es 257,000 × $0.04 = $10,280/mes, no $4,000. Dos salidas: (a) etiquetar 100,000 como escenario de 3DS selectivo ("3DS dinámico solo donde sube aprobación, ~40% de los intentos") o (b) presentar el 3DS a volumen completo. Recomiendo (a) porque conecta con la palanca 1 y con el 3DS dinámico que Carlos mostró.
6. Slide 14, cejilla dice "Propuesta"; debe decir "BUSINESS CASE". Slide 15, cejilla "BUSINESS CASE -    PROPUESTA" (guion y tabulador); debe ser "PROPUESTA · PRICING".
7. Slide 20, el lockup "yuno | PALCO" está cortado por el borde derecho. Moverlo a la izquierda. En portada y cierre el logo lleva la tagline "POWERING LIVE EVENTS BUSINESSES" en inglés e ilegible a ese tamaño; usar solo el wordmark (recorte en Deals/Palco/build/logo_url.txt).
8. Pie "Contrato a 3 años" en slide 15: viene de Appmaking; no se ha hablado de plazo con Palco. Quitar o confirmar.

## C. Lo que falta para que el deck cierre el argumento

9. El ROI de Palco no está escrito en ningún lado. El $25.1M es GTV de los tenants; el costo de Yuno ($280,845/año) lo paga Palco. Alfonso dijo dos veces que el costo se traslada al cliente final. Añadir en S14 (debajo de las tres tarjetas) una línea: "Costo anual de Yuno a su volumen: $281K. El ahorro operativo (palanca 4) cubre entre 82% y 128% de ese costo por sí solo. Cada punto porcentual de fee de Palco sobre el GTV recuperado suma $245K al año." (0.23/0.281 = 82%; 0.36/0.281 = 128%; $24.5M × 1% = $245K).
10. Añadir en S15, en la línea destacada de la tarjeta azul: "≈ 6 puntos básicos sobre una transacción promedio de $163" ($0.100 / $163 = 0.061%). Es la respuesta directa a "el cliente final no paga más".
11. Anclar los escenarios de L1 a referencias que ellos reconocen: conservador 67.4% ≈ lo que Mercado Pago ya les aprueba en tarjeta (67.9%); optimista 72.4% ≈ benchmark del mercado mexicano (~72% crédito, ~69% débito). Ponerlo en la fila de escenarios de S14 o en Supuestos.
12. Estructura RBP: el deck salta de "Por qué Yuno" al business case sin diagnóstico. Flair tenía "Our understanding of the context" (Executive Summary + current setup). Añadir después de la agenda: (a) "Lo que entendimos de Palco": white-label con 500+ recintos en 30 países; cada tenant es merchant of record y liquida a Palco; partners por país dueños de la cuenta; 50+ integraciones propias en 18 mercados; lo que pidieron: integraciones sin construirlas, credenciales por API, split de pagos, 3DS, ruteo por BIN, panel en on-sales. (b) "Su capa de pagos hoy": tabla de aprobación por procesador de su propia data (MX 56% a 60% vs MP Wallet 92.1%, Redsys 88.1%, UepaPay 98%), 900,120 declinadas al año, sin visibilidad consolidada de fraude. Con eso S13 deja de explicar y pasa a cuantificar. Agenda: 01 Contexto, 02 ¿Por qué Yuno?, 03 Business case, 04 Propuesta.
13. Agenda (S2) hoy solo tiene dos ítems y no menciona la propuesta. Mínimo: "03. PROPUESTA" y un divisor antes de S15 (duplicar S12).

## D. Ajustes de texto y números secundarios

14. S13 intro: "3.09 M de intentos de tarjeta" incluye 72,900 de MP Wallet. Decir "3.09 M de intentos en sus procesadores". "Concentradas en México y Argentina" es correcto (73% de las declinadas), pero la cohorte L1 incluye Cybersource, Stripe y Bancard; escribir "principalmente".
15. S13 palanca 1: el KPI muestra solo el conservador "62.4% → 67.4%". Mostrar "62.4% → 67.4% / 72.4%".
16. S13 palanca 2: el ticket $43.10 (Honduras) aplicado a Fiserv subestima si Fiserv es Uruguay (ticket UY = $2.1M / 7,900 = $266). Con ticket por mercado, L2 sería $2.2M conservador y $3.4M optimista; con el ticket mezclado de $163, $1.8M y $2.9M. Como Patricio no etiquetó el mercado de Fiserv, dejar $43.10 pero decir "ticket más bajo de su portafolio, como piso".
17. S13 palanca 3: "Requiere el MDR por procesador, que aún no tenemos" suena a carencia nuestra. Cambiar a "Se calibra con el MDR por procesador que nos compartan". "Benchmark de Yuno" (S13 y S14) para 7.5 a 12.5 bps y 3 a 4 FTE: no es un dato publicado; decir "supuesto de modelación de Yuno".
18. S13 palanca 4: "16 conexiones en 18 mercados" mezcla fuentes (16 = procesadores de su tabla; 18 mercados y 50+ pasarelas = su web). Escribir "las 50+ integraciones que hoy mantienen (16 procesadores concentran el volumen)". Añadir en Supuestos el costo cargado por FTE implícito ($77K a $90K).
19. S13 cierre: "time to market esperado de 4 a 6 semanas" no lo validó Carlos. Confirmarlo con él o cambiar a "semanas, no meses".
20. S13 título en dos líneas empuja el cuerpo. Alternativa de una línea: "La aprobación en tarjeta es la palanca más grande".
21. S15 tarjeta 2: "Herramientas antifraude +50" junto a "Motor antifraude $0.018" confunde. Cambiar a "Conexiones antifraude de terceros +50".
22. S15 base de volumen: 235,000 "transacciones exitosas" vs. su propia data (2.19M aprobadas al año = 182,000/mes de sus procesadores; 257,000 intentos/mes). 235,000 probablemente incluye efectivo, transferencia y pinpad. Añadir a la sub-línea "según la data compartida el 2 de septiembre, todos los métodos" y confirmar con Fernando qué incluye. Si el número correcto fuera 182,000: pagos $16,659/mes ($199,905/año), total con 3DS y antifraude $21,019/mes ($252,225/año), $0.092 y $0.116 por tx.
23. S6: "Menores costos de red, más aprobaciones" (Network tokens) toca la línea divisoria. Acortar a "Menos costo de red, más aprobación".
24. S17 y S18 (apéndice): estadísticas sin fuente en el slide (4% a 16%, 7% Amazon, $443B, 80%, 45%, 76%). Son del deck estándar; si Alfonso pregunta, no hay cita. Considerar quitar la columna "Datos de soporte" o dejar el apéndice fuera del envío.
25. Vs. lo dicho en la call del 15-sep ("alrededor de $15K como fee mínimo mensual"): la propuesta queda en $19,044 solo pagos y $23,404 con 3DS y antifraude. Dentro del rango que Alfonso asumió ($15K a $30K), pero prepararse para "dijiste 15".


## Estado tras el reajuste a $37.09 (16-sep, tarde)
Aplicados en el deck: 2 (supuestos con $37.09), 3 (3DS condicional), 6 (cejillas), 1 (notas Kraken borradas), 14, 17, 18 y todos los números de S13 y S14 recalculados con ticket $37.09 (ver palco-proposal-2026-09-16.md). El ítem 16 (ticket por mercado en L2) queda sin efecto: por instrucción de German, todo el GTV recuperado usa $37.09.
Pendientes de decisión: 4 (risk conditions $0.04), 5 (volumen 3DS), 7 (lockup S20 y tagline), 8 (contrato 3 años), 9 (ROI en S14, ahora: L4 cubre 82% a 128% del costo; cada 1% de fee sobre $6.0M = $60K), 10 (ahora 27 bps sobre $37.09), 11, 12, 13, 15, 19, 20, 21, 22, 23, 24, 25.
