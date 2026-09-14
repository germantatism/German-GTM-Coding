# Appmaking + Yuno: propuesta de pricing con ramp-up (2026-09-10, actualizada 2026-09-14)

> **⚠️ SUPERSEDIDO la noche del 14-sep por el deck "Proposal - AppMaking + Yuno" (Google Slides, 18 slides, PDF en esta carpeta).** German cambió el modelo a **platform fee + fee por transacción exitosa, ambos escalonados por banda de volumen mensual**: $5,000 + $0.20 (0 a 25K, tope $10,000), $5,500 + $0.12 (25,001 a 50K, $11,500), $6,500 + $0.065 (50,001 a 100K, $13,000), $7,500 + $0.05 (100,001 a 150K, $15,000), y $7,500 + $0.05 por tx arriba de 150K. Fully ramped $15,000/mes = $180,000/año. Sobre la curva real de Tatsiana: M1 $9,000, M2 $9,100, M3 $10,900, M4 $10,725, M5 $12,350, M6 $13,500, M7 $15,000; meses 1 a 7 $80,575 (520K tx, $0.155); meses 8 a 12 $75,000; **año 1 $155,575 (1.27M tx, $0.12)**. Todo verde sin aprobaciones (F1 $5,000 en lista; $7,500 sobre el piso verde F3 de $6,325; $0.05 sobre el ladder V3 sugerido; take rate 56 bps). Quirk: la tarifa de la banda aplica a todo el mes, así que la factura puede bajar al cruzar de banda (50,000 tx = $11,500; 50,001 = $9,750; M4 a 65K cuesta menos que M3 a 45K). La slide 13 del deck todavía muestra los meses y la caja "What it means" sobre la curva vieja: los valores corregidos y el paso a paso para venderla están en data/research/appmaking-meeting-brief-2026-09-15.md, sección 4 "Proposal Debrief". El modelo de fee fijo de abajo ($6,500 a $13,000, año 1 $133,500) queda como alternativa de respaldo, no se presenta.

**Estado:** lista para presentar en la call del **martes 15-sep, 9:00 COT / 17:00 EEST** (propuesta preliminar + AI products).
**Fuente de volúmenes:** curva mes a mes enviada por Tatsiana el 8-sep en el hilo "Appmaking + Yuno: Call Recap and Next Steps" (ya no hay supuestos en la curva; meses 8 a 12 se mantienen planos en 150K porque ellos no dieron más allá del mes 7).
**Modelo de referencia:** calculadora "Yuno — Pricing Matrix & Deal Calculator" (Drive, copia de Palco), plataforma F1–F5 y ladder de pay-ins V1–V5.

---

## 1. Lo que sabemos de sus volúmenes

| Dato | Valor | Fuente |
|---|---|---|
| Negocio | Suscripciones, 95% del revenue por web, 5% app stores | Call 4-sep ✅ |
| AOV | $18 (cada mes de su curva da exactamente GMV / tx = $18) | Email Tatsiana 8-sep ✅ |
| Mes 1 | 20,000 tx (~$360K GMV) | Email 8-sep ✅ |
| Mes 2 | 30,000 tx (~$540K GMV) | Email 8-sep ✅ |
| Mes 3 | 45,000 tx (~$810K GMV) | Email 8-sep ✅ |
| Mes 4 | 65,000 tx (~$1.17M GMV) | Email 8-sep ✅ |
| Mes 5 | 90,000 tx (~$1.62M GMV) | Email 8-sep ✅ |
| Mes 6 | 120,000 tx (~$2.16M GMV) | Email 8-sep ✅ |
| Mes 7 | 150,000 tx (~$2.7M GMV) | Email 8-sep ✅ |
| Meses 8 a 12 | 150,000 tx (plano) | Supuesto nuestro, ellos no lo dijeron |
| Pidieron | Pricing por escrito sobre esa curva, "para ver rentabilidad" | Email 8-sep + insistencia 10-sep ✅ |

Rampean bastante más rápido que lo que dijeron en la call del 4-sep (allí: 10K de arranque y 50K en 3 a 5 meses). Fully ramped llega en el **mes 7**, no en el 9.

Industria en la calculadora: **Digital Business / Goods** (alto margen, 70% GM, multiplicador 1.079). Bucket de volumen fully ramped: **V3 (100K a 1M)**, platform fee **F3 = $10,000 lista, green hasta $6,325, floor $4,000**.

## 2. El modelo: un fixed fee escalonado que crece más lento que el volumen

Lógica: al principio no es rentable cobrar por transacción, así que se cobra un fee fijo all-in que sube por escalones a medida que ellos rampean, y que se detiene cuando están fully ramped. Como el fee sube menos que el volumen, el costo por transacción cae en cada escalón. Por encima del último escalón solo se cobra un overage por transacción exitosa.

**El escalón lo dispara el volumen mensual de transacciones exitosas, no el calendario.** Los meses son la expectativa según su curva. Si rampean más lento pagan menos tiempo el escalón alto; si rampean más rápido, suben antes. Declinadas no cuentan. Sin setup fee.

### Ladder propuesto (fees sin cambio; solo se actualizó el mes esperado)

| Escalón | Tx exitosas / mes | Mes esperado (curva de ellos) | Fixed fee / mes | All-in por tx exitosa (tope de banda) |
|---|---|---|---|---|
| 1 | 0 a 25,000 | Mes 1 | **$6,500** | $0.26 |
| 2 | 25,001 a 50,000 | Meses 2 a 3 | **$8,000** | $0.16 |
| 3 | 50,001 a 100,000 | Meses 4 a 5 | **$10,000** | $0.10 |
| 4 | 100,001 a 150,000 | Meses 6 a 7 | **$13,000** | $0.087 |
| Fully ramped | Más de 150,000 | Mes 8 en adelante | **$13,000 + $0.03 por tx exitosa arriba de 150,000** | Cae hacia $0.03 |

Incrementos: +$1,500, +$2,000, +$3,000. Arranca en el rango $6,000 a $7,000 y termina en $13,000 fully ramped.

### Curva mes a mes (la de Tatsiana, 8-sep)

| Mes | Tx exitosas | Escalón | Fee | All-in $/tx |
|---|---|---|---|---|
| 1 | 20,000 | 1 | $6,500 | $0.325 |
| 2 | 30,000 | 2 | $8,000 | $0.267 |
| 3 | 45,000 | 2 | $8,000 | $0.178 |
| 4 | 65,000 | 3 | $10,000 | $0.154 |
| 5 | 90,000 | 3 | $10,000 | $0.111 |
| 6 | 120,000 | 4 | $13,000 | $0.108 |
| 7 | 150,000 | 4 | $13,000 | $0.087 |
| 8 a 12 | 150,000 (supuesto) | 4 | $13,000 | $0.087 |

Con su curva el unitario **baja todos los meses**, incluido el mes en que cruzan de banda (mes 2: $0.325 a $0.267; mes 4: $0.178 a $0.154; mes 6: $0.111 a $0.108). No hay ningún mes en que suba, así que el argumento "your cost per transaction falls at every step" se sostiene con sus propios números.

Totales con esa curva:

| Periodo | Fee acumulado | Tx exitosas | All-in promedio |
|---|---|---|---|
| Meses 1 a 7 (ramp) | $68,500 | 520,000 | $0.132 |
| Meses 8 a 12 | $65,000 | 750,000 | $0.087 |
| Año 1 | $133,500 | 1,270,000 | $0.105 |
| Año 2 a 150K/mes | $156,000 | 1,800,000 | $0.087 |

Escalones por volumen (propuesta) vs por calendario (alternativa): con su curva real los dos dan el mismo resultado si cumplen el plan. La diferencia solo aparece si rampean distinto: por volumen ellos pagan según lo que realmente procesan (más justo para ellos, es el argumento de venta); por calendario Yuno tiene revenue más predecible. Recomendación: **por volumen**, que es lo que ya está en la slide.

## 3. Chequeo contra la política de pricing (calculadora)

| Escalón | Fee | Platform fee de lista para esa banda | Uso implícito al tope de banda | Lectura |
|---|---|---|---|---|
| 1 (0 a 25K) | $6,500 | F1 $5,000 | $1,500 / 25K = $0.060/tx | Verde. Lista V1 es $0.10, floor $0.01 |
| 2 (25K a 50K) | $8,000 | F2 $7,000 | $1,000 / 50K = $0.020/tx | Arriba del floor, cerca del piso verde. Es el descuento de ramp |
| 3 (50K a 100K) | $10,000 | F2 $7,000 | $3,000 / 100K = $0.030/tx | Verde |
| 4 (100K a 150K) | $13,000 | F3 $10,000 | $3,000 / 150K = $0.020/tx | Verde justo: el green-down-to de pay-ins V3 en la corrida de Palco fue $0.0188 |
| Overage | $0.030/tx | | | Verde. El ladder V3 sugerido en Palco (mid-margin) fue $0.0427 / $0.0362 / $0.0314; Appmaking es high-margin, sugerido sale algo más alto |

- Deal size fully ramped $13,000/mes contra mínimo new logo de $10,000: cumple.
- Take rate fully ramped: $13,000 sobre $2.7M TPV = 48 bps contra 15 bps esperados para V3: sobra.
- Estructura estándar equivalente a 150K (F3 $10,000 + ~$0.035/tx blended) sería ~$15,250/mes ≈ $183K/año. Sobre su curva, el año 1 estándar daría ~$164K (12 × $10,000 + $0.035 × 1.27M) contra $133,500 con el ramp: **el ramp les ahorra ~$31K en el año 1 y ~$27K/año en régimen**. Como rampean rápido, el ahorro del año 1 es menor que con la curva lenta que asumimos antes (~$62K), pero el argumento de "economics working for you well before 100K" sigue vivo: en el mes 4 ya están en $0.15/tx y en el mes 7 en $0.087. Úsalo en la conversación, no en la slide.
- Si quieres el fully ramped en $12,500, el uso implícito baja a $0.0167/tx y la línea de pay-ins queda en zona amarilla por debajo del green-down-to. $13,000 es el número que mantiene todo verde sin aprobaciones.
- ⚠️ La calculadora no se ha corrido para Appmaking. Para el score oficial: duplicar "Yuno — Pricing Palco" como "Yuno — Pricing Appmaking", poner 150,000 tx, AOV $18, industria Digital Business / Goods, y en la sección 10 (Fixed fee ramp-up) modelar los escalones como % del fee full.

## 4. Qué incluye el fee y qué queda pendiente

**Incluido en el fixed fee (mismo bloque que FlightHub):** KAM y TAM dedicados, +1,000 métodos de pago, +450 proveedores, +50 herramientas antifraude, orchestration & rules engine, smart routing & retries. Cada conector lo mantiene Yuno; agregar un proveedor después es un cambio de ruteo, no un fee nuevo.

**Pendiente de scoping (precio aparte, como se dijo en la call):** Subscriptions engine standalone, token vault y network tokens, reconciliation, alertas Verifi y Ethoca.

Referencia interna, precios sugeridos por la calculadora en la corrida V3 de Palco (mid-margin; Appmaking high-margin saldría algo más alto): Subscriptions $0.0369/unidad, Network Tokens creación $0.2973 y update $0.0595, Reconciliation $0.0188/unidad. Verifi y Ethoca no están en la calculadora. No poner estos números en la slide hasta correrlos para Appmaking.

**No incluir en la slide:** minimum monthly billing (el fixed fee ya es el mínimo), término de contrato (no se habló), nombres de PSPs como "incluidos" (la cobertura de conectores se confirma por escrito aparte: Stripe, Ecompay, Unlimit, Airwallex, Shift4, Payabl, NMI y el octavo que quedó garbled), claims de aprobación o ahorro.

## 5. Pendientes antes de la call del 15-sep

1. ✅ Curva mes a mes pegada (8-sep) y slide actualizada (HTML + PNG re-renderizado el 14-sep).
2. ✅ Escalones por volumen (recomendado, ver sección 2).
3. ⬜ Correr la calculadora para Appmaking y dejar el score GREEN documentado (útil para Deal Desk del 16-sep).
4. ⬜ Confirmar cobertura de conectores por escrito. Ojo: el recap del 4-sep ya afirmó "we have full coverage with them all" para Stripe, Ecompay, Unlimit, Airwallex, Shift4, Payabl y NMI, y el correo del 14-sep lo repitió. Verificar en el catálogo de connections del Dashboard (Ecompay, Payabl y NMI en particular) antes de que lo pidan en contrato.
5. ⬜ Definir con Sean, antes de las 9:00, si el número se presenta como final o como "preliminar sujeto a contrato".
