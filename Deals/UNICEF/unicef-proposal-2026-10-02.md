# Propuesta - UNICEF Colombia + Yuno (Google Slides, 2026-10-02)

Deck: https://docs.google.com/presentation/d/111EW1tmbSYPYtxLYRa5Mf_yx0Cn-BxA4wT2FAZeGpe0/edit (raíz de My Drive)
Origen: copia Drive de "Propuesta - Línea Directa + Yuno" (126rE0knbVczAsHtRVCtRWopV4lOh3yrKx5038hhjdew) en su estado del 2-oct. 20 slides: los 21 de Línea Directa menos el de conexiones de Perú.
Vía: conector de Drive (copia + compartir con la service account gtm-claude-editor) y Slides API. Scripts en build/.
Estado: BORRADOR, sin enviar.

## Datos usados (instrucción de German, 2-oct-2026)
- Todo en dólares. 150,000 transacciones al mes, ticket promedio de $15: $2,250,000 de volumen aprobado al mes.
- Fee de plataforma: $10,000 al mes.
- Tarifa variable como porcentaje del volumen aprobado, "como en la propuesta de Yango".
- Motor de suscripciones: $0.02 por transacción enviada por el motor.

## Pricing (slide 15), build/model.py
| Concepto | Precio | Mensual | Anual |
|---|---|---|---|
| Tramo 1: $0 a $1.5M | 0.25% del volumen aprobado | $3,750 | $45,000 |
| Tramo 2: más de $1.5M | 0.20% | $1,500 | $18,000 |
| Subtotal volumen aprobado ($2.25M) | 0.233% efectivo, $0.035 por trx | $5,250 | $63,000 |
| Motor de suscripciones | $0.02 por trx enviada, 150,000 trx | $3,000 | $36,000 |
| Fee de plataforma | | $10,000 | $120,000 |
| **Total** | **$0.12 all-in por trx, 0.81% del volumen** | **$18,250** | **$219,000** |

- Incluido en el fee de plataforma: +1,000 métodos, +450 procesadores, orquestación y smart routing, una sola integración vía API, bóveda de tokens (PCI), gestión de transacciones, usuarios y roles, reportes y dashboard, equipo dedicado (KAM y TAM).
- Franja inferior "Opcional, para revisar después", sin precio: conciliación, monitores y alertas, network tokens, Nova.
- Sin compromiso mínimo ni facturación mínima (German no lo pidió; la propuesta final de Yango tampoco lo tiene).

**Supuestos míos, por confirmar con German:**
1. Porcentajes y corte de tramo: son los de la propuesta final de Yango (0.25% hasta $1.5M al mes, 0.20% por encima). German dijo "un % como en la propuesta de Yango", no dio las tasas. Los tramos altos de Yango (0.15% sobre $3M, 0.10% sobre $4.5M) no se muestran: UNICEF está en $2.25M.
2. Las 150,000 transacciones pasan todas por el motor de suscripciones, un envío por transacción. Si los reintentos cuentan como envíos, la línea de suscripciones sube: con 85% de aprobación, 150,000 aprobadas piden al menos 176,471 envíos, $3,529 al mes.
3. "Sin fee de setup" y "Contrato a 3 años" quedaron heredados de Línea Directa.
4. Los débitos a cuenta (ACH) entran en el mismo volumen. No hay dato del mix por método.

**Contra la Pricing Policy (copia leída el 21-sep, es DRAFT):**
- Fee de plataforma $10,000: es el list de V3 (100K a 1M trx al mes). Zona verde.
- Pay-ins: 0.25% y 0.20% sobre $15 equivalen a $0.0375 y $0.03 por trx, entre el list ($0.10) y el mínimo ($0.01). La zona la da el calculator; "nonprofit" no aparece en las bandas de margen.
- Suscripciones: la copia de la policy dice 0.7% del TPV (mínimo 0.3%) y "not sellable yet". $0.02 sobre $15 es 0.13%. German dio $0.02 por transacción enviada: confirmar con Finance cuál es el precio vigente.
- Pasar por Salesforce antes de cotizar. En Gong hay dos cuentas "UNICEF" duplicadas.
- Entidad colombiana contra entidad colombiana puede obligar a facturar en pesos.

**Referencia para la conversación:** UNICEF Colombia publica que una transacción con tarjeta le cuesta en promedio COP 700 y un débito a cuenta COP 1,400 (donaciones.unicef.org.co/captadores). El all-in de Yuno ($0.12 por transacción) va encima de ese costo.

## Cambios por slide vs Línea Directa
- S1 y S20: lockup yuno | unicef (logo de Wikimedia Commons en blanco). Título "IMPULSANDO PAGOS SIN FRICCIÓN PARA UNICEF COLOMBIA".
- S2: agenda "02. CONEXIONES EN COLOMBIA". S12: divisor "Conexiones en Colombia".
- S5: título, "UN EQUIPO DEDICADO PARA UNICEF COLOMBIA", "rieles locales de Colombia".
- S11: "Yuno es la capa de pagos para el recaudo recurrente de UNICEF Colombia". Ventajas clave: una sola integración sobre sus procesadores actuales; ruteo y respaldo automático entre procesadores de tarjeta; reintentos automáticos y configurables; todo el recaudo en un solo panel, con reportes.
- S13: conexiones de Colombia, sin cambios (Credibanco, Redeban, Wompi y Nuvei aparecen en la lista de procesadores).
- Slide de conexiones de Perú: eliminado.
- S15: pricing.
- Sin cambios: S3, S4, S6 a S10, S14, S16 a S19.

## Cuidado al presentar
- ACH: Yuno no hace smart routing ni fallbacks en débitos a cuenta (corregido por correo el 29-sep). La ventaja de ruteo dice "procesadores de tarjeta" a propósito.
- S10 (credenciales) trae "Wingo 14%" del template; German lo mantiene en sus propuestas.
- Pendientes de producto sin resolver: tiempos de respuesta de ACH, prenotificación de cuentas nuevas, monto abierto en el checkout.
- Pendientes de UNICEF: mix de volumen por método, cómo compran (RFP, LTA o directo), quién decide, y cómo manejar el middleware.

## Pricing v2 (2-oct, tarde): tramos por transacciones aprobadas
Instrucción de German: las tarifas y los tramos van sobre transacciones aprobadas, no sobre volumen aprobado. Aplicado con build/fix2_tx_tiers.py (solo el slide de pricing). Las tablas de arriba quedan como registro de la v1.

| Concepto | Precio | Mensual | Anual |
|---|---|---|---|
| Tramo 1: 0 a 100,000 trx aprobadas | 0.25% del valor de cada transacción aprobada | $3,750 | $45,000 |
| Tramo 2: más de 100,000 trx aprobadas | 0.20% | $1,500 | $18,000 |
| Subtotal transacciones (150k) | $0.035 por trx en promedio | $5,250 | $63,000 |
| Motor de suscripciones | $0.02 por trx enviada, 150,000 trx | $3,000 | $36,000 |
| Fee de plataforma | | $10,000 | $120,000 |
| **Total** | **$0.12 all-in por transacción aprobada** | **$18,250** | **$219,000** |

- Título del slide: "Fee de plataforma más un porcentaje por transacción aprobada". Panel izquierdo: "TARIFA POR TRANSACCIÓN APROBADA", tramos "0 a 100,000 trx aprobadas" y "Más de 100,000 trx aprobadas".
- Al ticket de $15, cada transacción aprobada paga $0.0375 en el tramo 1 y $0.03 en el tramo 2.
- Los totales no cambian frente a la v1: el corte de 100,000 transacciones equivale a $1.5M al ticket de $15.
- Ya no aparece "volumen aprobado" en el slide; el callout quedó en "≈ $0.12 all-in por transacción aprobada".

**Interpretación mía, por confirmar con German:**
1. La tarifa sigue siendo un porcentaje (como pidió antes) y lo que cambia es la base del tramo: número de transacciones aprobadas. Si quiso decir una tarifa fija en dólares por transacción aprobada, hay que cambiar las cifras grandes del panel izquierdo.
2. El corte de 100,000 transacciones sale de dividir el corte de Yango ($1.5M) por el ticket de $15.

## Pricing v3 (2-oct, tarde): 0.28% y 0.24%
Instrucción de German: la tarifa empieza en 0.28% y baja a 0.24%. Aplicado con build/fix3_rates.py (solo el slide de pricing). Tramos por transacciones aprobadas, sin cambio. Reemplazada por la v4 de abajo.

| Concepto | Precio | Mensual | Anual |
|---|---|---|---|
| Tramo 1: 0 a 100,000 trx aprobadas | 0.28% del valor de cada transacción aprobada | $4,200 | $50,400 |
| Tramo 2: más de 100,000 trx aprobadas | 0.24% | $1,800 | $21,600 |
| Subtotal transacciones (150k) | $0.04 por trx en promedio | $6,000 | $72,000 |
| Motor de suscripciones | $0.02 por trx enviada, 150,000 trx | $3,000 | $36,000 |
| Fee de plataforma | | $10,000 | $120,000 |
| **Total** | **$0.13 all-in por transacción aprobada** | **$19,000** | **$228,000** |

- Al ticket de $15, cada transacción aprobada paga $0.042 en el tramo 1 y $0.036 en el tramo 2 (list de pay-ins $0.10, mínimo $0.01: la zona la da el calculator).
- Las tasas ya no son las de Yango: las dio German. Sigue por confirmar el corte de 100,000 transacciones.

## Pricing v4 (2-oct, tarde): primeras 50,000 transacciones de suscripciones sin costo
Instrucción de German: en suscripciones se dan gratis las primeras 50,000 transacciones. Aplicado con build/fix4_subs_free.py (solo el slide de pricing). Reemplazada por la v5 de abajo.

| Concepto | Precio | Mensual | Anual |
|---|---|---|---|
| Tramo 1: 0 a 100,000 trx aprobadas | 0.28% del valor de cada transacción aprobada | $4,200 | $50,400 |
| Tramo 2: más de 100,000 trx aprobadas | 0.24% | $1,800 | $21,600 |
| Subtotal transacciones (150k) | $0.04 por trx en promedio | $6,000 | $72,000 |
| Motor de suscripciones | $0.02 por trx enviada; primeras 50,000 del mes sin costo; 100,000 facturables | $2,000 | $24,000 |
| Fee de plataforma | | $10,000 | $120,000 |
| **Total** | **$0.12 all-in por transacción aprobada** | **$18,000** | **$216,000** |

**Supuestos míos, por confirmar con German:**
1. Las 50,000 gratis son por mes y se renuevan cada mes (German dijo "las primeras 50k trx", sin decir el periodo). Si fueran 50,000 una sola vez, la línea vuelve a $3,000 al mes desde el segundo mes.
2. El corte de tramo en 100,000 transacciones aprobadas.
3. Las 150,000 transacciones pasan por el motor, un envío cada una. Si los reintentos cuentan, con 85% de aprobación serían unos 176,471 envíos: $2,529 al mes.

## Pricing v5 (4-oct): facturación mínima mensual de $14,000
Instrucción de German: facturación mínima mensual de $14,000, es decir $10,000 de plataforma más $4,000 en transacciones; calcular cuántas transacciones cubren los $4,000. Aplicado con build/fix5_min_billing.py (solo el slide de pricing). Reemplazada por la v6 de abajo.

- $4,000 ÷ ($15 × 0.28%) = $4,000 ÷ $0.042 = **95,238 transacciones aprobadas al mes** (en el slide: "cerca de 95,000"). Caen completas en el tramo 1.
- Si el compromiso también se cubriera con la tarifa de suscripciones ($0.02 por envío a partir de 50,000), bastarían 80,645 transacciones. El slide usa solo la tarifa por transacción aprobada, como en Línea Directa.
- Con 150,000 transacciones el mínimo queda cubierto (total estimado $18,000, sin cambio). Si el mes cierra por debajo, se factura la diferencia.
- Cambios en el slide: header; caja de notas del panel izquierdo (lleva el mínimo); fila nueva "Facturación mínima mensual $14,000 / mes" bajo el fee de plataforma en el panel del medio; fila nueva "Facturación mínima: $14,000 (≈95,000 trx) | Cubierta | Cubierta" antes del total en el panel derecho; nota del panel derecho reescrita.
- Contra la Pricing Policy: fee fija + MMG aditivo es la estructura preferida. Facturar plataforma y mínimo mensual (en vez de anual anticipado) va por zona amarilla. El equivalente en transacciones depende del ticket de $15: si el ticket real es otro, cambia el número de transacciones, no los $4,000.

## Pricing v6 (6-oct): plataforma $7,000, mínimo $10,000, suscripciones $0.015
Instrucción de German: bajar el fee de plataforma a $7,000, la facturación mínima mensual a $10,000 y cobrar el motor de suscripciones a $0.015 por transacción enviada. Aplicado con build/fix6_v6_lower_fees.py (solo texto del slide 15, mismos IDs que v5, nada se movió). **Esta es la versión vigente en el deck.** Los porcentajes (0.28% / 0.24%), el corte de 100,000 trx y las 50,000 gratis de suscripciones no cambian.

| Concepto | Precio | Mensual | Anual |
|---|---|---|---|
| Tramo 1: 0 a 100,000 trx aprobadas | 0.28% del valor de cada transacción aprobada | $4,200 | $50,400 |
| Tramo 2: más de 100,000 trx aprobadas | 0.24% | $1,800 | $21,600 |
| Subtotal transacciones (150k) | $0.04 por trx en promedio | $6,000 | $72,000 |
| Motor de suscripciones | $0.015 por trx enviada; primeras 50,000 del mes sin costo; 100,000 facturables | $1,500 | $18,000 |
| Fee de plataforma | | $7,000 | $84,000 |
| Facturación mínima mensual | $10,000 = $7,000 de plataforma + $3,000 en transacciones (≈71,000 trx aprobadas) | Cubierta | Cubierta |
| **Total** | **$0.10 all-in por transacción aprobada (0.64% del volumen)** | **$14,500** | **$174,000** |

- $3,000 ÷ ($15 × 0.28%) = $3,000 ÷ $0.042 = **71,429 transacciones aprobadas al mes** (en el slide: "cerca de 71,000"). Caen completas en el tramo 1. Si el compromiso también contara la tarifa de suscripciones, bastarían 65,789; el slide sigue usando solo la tarifa por transacción aprobada.
- Supuesto mío: el mínimo de $10,000 es el total facturado (plataforma + transacciones), igual que en la v5. Si German quería $10,000 solo en transacciones encima de los $7,000 de plataforma, el mínimo sería $17,000 y hay que rehacer el slide.
- Supuesto heredado: las 150,000 pasan por el motor, un envío cada una (con reintentos a 85% serían ~176,471 envíos: $1,897 al mes).
- Contra la Pricing Policy (ver memoria yuno-pricing-policy): el fee de plataforma de $7,000 queda por debajo del list de V3 ($10,000) y hay que validar la zona antes de enviar; la estructura fee fija + MMG aditivo sigue siendo la preferida.
- Cambios en el slide: header; "$0.015/trx" en el panel izquierdo; caja de notas del mínimo; filas "Fee de plataforma $7,000 / mes" y "Facturación mínima mensual $10,000 / mes" en el panel del medio; en el panel derecho suscripciones $1,500 / $18,000, plataforma $7,000 / $84,000, "Facturación mínima: $10,000 (≈71,000 trx)", total $14,500 / $174,000, "≈ $0.10 all-in" y la nota.
