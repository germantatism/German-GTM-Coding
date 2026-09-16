# Propuesta comercial Palco + Yuno v1 (2026-09-16)

Google Slides: https://docs.google.com/presentation/d/1hWX6sNKKPpXhDSKGlZzrHWyKWMx5WlVxBeScEL_J7UY/edit (carpeta Drive "Palco")
Base: deck "Proposal - AppMaking + Yuno", 18 slides, todo en español. Slide 13 = propuesta. Para la reunión del lunes 21-sep 11:00 COT (Patricio, Fernando, Alfonso, Miguel tentativo).

## Fuente de los números
Hoja "Yuno — Pricing Matrix & Deal Calculator" (1Shux23cA23PBCcAlyhAiNrzXgzU6lbtQsLxUHgQ5NH8, pestaña Deal Calculator): 235,000 tx/mes, AOV $37.09, V3 / F3, ladder de 3 tramos (58,750 / 117,500 / 235,000). Precios Suggested: platform fee $10,000, 3DS $0.0403 (100,000 intentos/mes), Fraud Engine $0.0184 (20,000 evaluaciones/mes), Risk conditions $0.0139 (sin volumen). Tarifas de pagos dadas por German: $0.08 / $0.06 / $0.05 (la hoja sugería $0.0678 / $0.0514 / $0.0415).

## Estructura en el slide
| Tramo | Tx exitosas / mes | Plataforma | Por tx | All-in al tope |
|---|---|---|---|---|
| 1 | 0 a 58,750 | $10,000 | $0.08 | $14,700 |
| 2 | 58,751 a 117,500 | $10,000 | $0.06 | $18,225 |
| 3 | más de 117,500 (mostrado a 235,000) | $10,000 | $0.05 | $24,100 |

Ejemplo a 235,000: 58,750 × 0.08 = $4,700; 58,750 × 0.06 = $3,525; 117,500 × 0.05 = $5,875; total tramos $14,100 + plataforma $10,000 = $24,100/mes ($0.103 por tx). Pagos al año: $289,200.

Seguridad y riesgo (cotizado a precio Suggested): 3DS $0.0403 por autenticación ($4,030 a 100,000), motor antifraude $0.0184 por evaluación ($368 a 20,000), risk conditions $0.0139 por transacción evaluada (según uso). Total mensual estimado con 3DS y antifraude: $28,498 ($0.121 por tx).

Pendientes de revisión: conciliación, network tokens, token vault. Incluidos: KAM y TAM, +1,000 métodos, +450 proveedores, +50 conexiones antifraude, orquestación y reglas, smart routing y reintentos, monitores y alertas, reportes y dashboard, subcuentas por cliente. Pie: contrato a 3 años.

## Decisiones tomadas que German debe validar
1. Modelo ladder (cada tramo a su tarifa), como está activo en la hoja. Alternativa cliff (la tarifa del tramo aplica a todo el mes, como en Appmaking): a 235,000 sería 235,000 × 0.05 + 10,000 = $21,750/mes.
2. Se cobra solo sobre transacciones exitosas (convención del deck de Appmaking). Palco aprueba ~71%: si las 235,000 son intentos, las exitosas son ~167,000 y el total baja a ~$20,700/mes.
3. 3DS, fraud engine y risk conditions van cotizados a precio Suggested, no incluidos sin costo. "Les vamos a dar" se interpretó como "cotizar". Si es "incluir", cambia el slide.
4. Contrato a 3 años copiado del deck de Appmaking.
5. Ventajas clave (slide 11) adaptadas a Palco: una sola integración por país, cuentas y contratos de sus clientes siguen siendo suyos, monitores con redistribución automática, subcuentas por cliente con reportes.
6. Teléfono del cierre corregido a +1 786 238 4554 (el deck de Appmaking decía 787).
7. Los volúmenes de 235,000 tx y $37.09 son los de Patricio (2-sep) y siguen sin reconciliar (ticket vs orden).


## v2 del deck (16-sep, tarde): business case y pricing reajustados

German rehizo el deck: agenda 02 Business Case, slide 13 (cuatro palancas), slide 14 (Impacto total), slide 15 (pricing en layout Flair). Pricing v2: platform fee $7,000 + $0.06 / $0.055 / $0.045 por tramo (58,750 / 117,500 / +). A 235,000 tx exitosas: pagos $12,044 + plataforma $7,000 = $19,044/mes ($228,525/año); 3DS 100,000 × $0.04 = $4,000; antifraude 20,000 × $0.018 = $360; total $23,404/mes ($280,845/año); $0.081 y $0.100 por tx. Sigue GREEN contra el calculator.

**Regla de German (16-sep): el ticket promedio de Palco es $37.09, el que reportó Patricio. No usar el $163 derivado ($346M / 2.12M).** Business case reajustado con $37.09 en palancas 1 y 2 (L3 sigue sobre el TPV de tarjeta de $346M y L4 sobre FTE):

| Palanca | Conservador | Optimista | Promedio |
|---|---|---|---|
| L1 aprobación en tarjeta (+5 pp / +10 pp sobre 1,952,600 intentos) | $3.6M | $7.2M | $5.4M |
| L2 failover Fiserv + Pixel Pay (47.6% → 60% / 68% sobre 88,000) | $0.40M | $0.67M | $0.54M |
| L3 costo de procesamiento (7.5 a 12.5 bps sobre $346M) | $0.26M | $0.43M | $0.35M |
| L4 run-ops (3 a 4 FTE) | $0.23M | $0.36M | $0.30M |
| Total anual | $4.5M | $8.7M | $6.6M |

Tarjetas S14: GTV recuperado tenants $6.0M (rango $4.0M a $7.9M); ahorro MDR $0.35M; ahorro operativo Palco $0.30M. Cálculo: L1c 97,630 × 37.09 = $3,621,097; L1o 195,260 × 37.09 = $7,242,193; L2c 10,912 × 37.09 = $404,726; L2o 17,952 × 37.09 = $665,840.
ROI con estos números: costo Yuno $281K/año; L4 cubre 82% a 128%; cada 1% de fee de Palco sobre $6.0M = $60K/año. All-in $0.100 por tx = 27 bps sobre un ticket de $37.09.
Nota interna: $37.09 × 2.19M aprobadas = $81M, no los $346M de TPV en tarjeta que también reportaron; ambos son datos de Patricio. El deck usa el ticket para GTV recuperado y el TPV para bps.

Aplicado en el deck el 16-sep (tarde): números de S13 y S14; supuestos reescritos con $37.09; "Si el 3DS aplica a todos los flujos, como plantearon"; "Se calibra con el MDR que nos compartan"; "sus 50+ integraciones (16 procesadores concentran el volumen)"; "supuesto de modelación de Yuno" en vez de "benchmark"; cejillas S14 BUSINESS CASE y S15 PROPUESTA · PRICING; notas del orador de S11 (Kraken) borradas.
Pendiente de decisión de German: risk conditions $0.04 vs sugerido $0.0139; 3DS a 100,000 vs 257,000 intentos; "Contrato a 3 años"; línea de ROI en S14; "27 bps sobre $37.09" en S15; slides de contexto; lockup cortado en S20 y tagline del logo; "4 a 6 semanas"; apéndice sin fuentes.
