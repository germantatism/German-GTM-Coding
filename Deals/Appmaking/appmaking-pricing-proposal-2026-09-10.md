# Appmaking + Yuno: propuesta de pricing con ramp-up (2026-09-10)

**Estado:** borrador para revisión de German antes de la call de la semana del 14-sep (propuesta preliminar + AI products).
**Fuente de volúmenes:** call del 4-sep (Gong, 44 min) + instrucción de German del 10-sep. ⚠️ El thread de Gmail con los volúmenes que ellos mandaron NO se pudo leer en esta sesión (Gmail y Glean sin credenciales). Los números marcados 🔍 son supuestos que hay que reemplazar con los del correo.
**Modelo de referencia:** calculadora "Yuno — Pricing Matrix & Deal Calculator" (Drive, copia de Palco), plataforma F1–F5 y ladder de pay-ins V1–V5.

---

## 1. Lo que sabemos de sus volúmenes

| Dato | Valor | Fuente |
|---|---|---|
| Negocio | Suscripciones, 95% del revenue por web, 5% app stores | Call 4-sep ✅ |
| Arranque | ~10,000 tx/mes | Call 4-sep ✅ |
| Ramp que ellos plantearon | ~$1M/mes ≈ 50,000 tx/mes en 3 a 5 meses | Call 4-sep ✅ |
| AOV | ~$18 | Call 4-sep ✅ |
| Pidieron | Pricing por escrito con ramp hasta 100K tx/mes "para ver rentabilidad" | Call 4-sep ✅ |
| Target fully ramped | 150,000 tx/mes hacia el mes 9 | German 10-sep ✅ |
| TPV fully ramped | 150,000 × $18 ≈ $2.7M/mes | Calculado |
| Curva mes a mes | 🔍 la del correo de ellos. Abajo uso una curva supuesta | Supuesto |

Industria en la calculadora: **Digital Business / Goods** (alto margen, 70% GM, multiplicador 1.079). Bucket de volumen fully ramped: **V3 (100K a 1M)**, platform fee **F3 = $10,000 lista, green hasta $6,325, floor $4,000**.

## 2. El modelo: un fixed fee escalonado que crece más lento que el volumen

Lógica que pidió German: al principio no es rentable cobrar por transacción, así que se cobra un fee fijo all-in que sube por escalones a medida que ellos rampean, y que se detiene cuando están fully ramped. Como el fee sube menos que el volumen, el costo por transacción cae en cada escalón. Por encima del último escalón solo se cobra un overage por transacción exitosa.

**El escalón lo dispara el volumen mensual de transacciones exitosas, no el calendario.** Los meses son la expectativa según su ramp plan. Si rampean más lento pagan menos tiempo el escalón alto; si rampean más rápido, suben antes. Declinadas no cuentan. Sin setup fee.

### Ladder propuesto

| Escalón | Tx exitosas / mes | Mes esperado 🔍 | Fixed fee / mes | All-in por tx exitosa (tope de banda) |
|---|---|---|---|---|
| 1 | 0 a 25,000 | Meses 1 a 3 | **$6,500** | $0.26 |
| 2 | 25,001 a 50,000 | Meses 4 a 5 | **$8,000** | $0.16 |
| 3 | 50,001 a 100,000 | Meses 6 a 7 | **$10,000** | $0.10 |
| 4 | 100,001 a 150,000 | Meses 8 a 9 | **$13,000** | $0.087 |
| Fully ramped | Más de 150,000 | Mes 10 en adelante | **$13,000 + $0.03 por tx exitosa arriba de 150,000** | Cae hacia $0.03 |

Incrementos: +$1,500, +$2,000, +$3,000. Arranca en el rango $6,000 a $7,000 que pidió German y termina en $13,000 fully ramped.

### Curva mes a mes (🔍 reemplazar con la del correo)

| Mes | Tx exitosas | Escalón | Fee | All-in $/tx |
|---|---|---|---|---|
| 1 | 10,000 | 1 | $6,500 | $0.650 |
| 2 | 15,000 | 1 | $6,500 | $0.433 |
| 3 | 25,000 | 1 | $6,500 | $0.260 |
| 4 | 40,000 | 2 | $8,000 | $0.200 |
| 5 | 50,000 | 2 | $8,000 | $0.160 |
| 6 | 75,000 | 3 | $10,000 | $0.133 |
| 7 | 100,000 | 3 | $10,000 | $0.100 |
| 8 | 135,000 | 4 | $13,000 | $0.096 |
| 9 | 150,000 | 4 | $13,000 | $0.087 |
| 10 a 12 | 150,000 | Fully ramped | $13,000 | $0.087 |

Totales con esa curva:

| Periodo | Fee acumulado | Tx exitosas | All-in promedio |
|---|---|---|---|
| Meses 1 a 9 (ramp) | $81,500 | ~600,000 | ~$0.136 |
| Meses 10 a 12 | $39,000 | 450,000 | $0.087 |
| Año 1 | $120,500 | ~1,050,000 | ~$0.115 |
| Año 2 a 150K/mes | $156,000 | 1,800,000 | $0.087 |

⚠️ Con escalones por volumen, el $/tx puede subir un poco el mes en que cruzan de banda (ej. cruzar a 100,001 sube el fee a $13,000 y el unitario pasa de $0.10 a $0.13). Con la curva supuesta la serie baja todos los meses; si la curva real de ellos tiene un mes flojo justo después de cruzar, el unitario de ese mes sube. Si eso importa, la alternativa es disparar los escalones por calendario (meses 1 a 3, 4 a 5, 6 a 7, 8 a 9) y no por volumen: revenue más predecible para Yuno, y ellos pagan lo mismo aunque rampeen lento.

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
- Estructura estándar equivalente a 150K (F3 $10,000 + ~$0.035/tx blended) sería ~$15,250/mes ≈ $183K/año. El ramp les ahorra ~$62K en el año 1 y ~$27K/año en régimen. Ese es el argumento de "economics working for you well before 100K" que prometió el follow-up del 4-sep. Úsalo en la conversación, no en la slide.
- Si quieres el fully ramped en $12,500, el uso implícito baja a $0.0167/tx y la línea de pay-ins queda en zona amarilla por debajo del green-down-to. $13,000 es el número que mantiene todo verde sin aprobaciones.
- ⚠️ La calculadora no se pudo correr para Appmaking (el MCP de Drive solo edita celdas, no duplica archivos; escribir en la hoja de Palco la dañaría). Para el score oficial: duplicar "Yuno — Pricing Palco" como "Yuno — Pricing Appmaking", poner 150,000 tx, AOV $18, industria Digital Business / Goods, y en la sección 10 (Fixed fee ramp-up) modelar los escalones como % del fee full.

## 4. Qué incluye el fee y qué queda pendiente

**Incluido en el fixed fee (mismo bloque que FlightHub):** KAM y TAM dedicados, +1,000 métodos de pago, +450 proveedores, +50 herramientas antifraude, orchestration & rules engine, smart routing & retries. Cada conector lo mantiene Yuno; agregar un proveedor después es un cambio de ruteo, no un fee nuevo.

**Pendiente de scoping (precio aparte, como se dijo en la call):** Subscriptions engine standalone, token vault y network tokens, reconciliation, alertas Verifi y Ethoca.

Referencia interna, precios sugeridos por la calculadora en la corrida V3 de Palco (mid-margin; Appmaking high-margin saldría algo más alto): Subscriptions $0.0369/unidad, Network Tokens creación $0.2973 y update $0.0595, Reconciliation $0.0188/unidad. Verifi y Ethoca no están en la calculadora. No poner estos números en la slide hasta correrlos para Appmaking.

**No incluir en la slide:** minimum monthly billing (el fixed fee ya es el mínimo), término de contrato (no se habló), nombres de PSPs como "incluidos" (la cobertura de conectores se confirma por escrito aparte: Stripe, Ecompay, Unlimit, Airwallex, Shift4, Payabl, NMI y el octavo que quedó garbled), claims de aprobación o ahorro.

## 5. Pendientes antes de mandar

1. 🔍 Pegar la curva mes a mes del correo de Tatsiana y Dzmitry y reemplazar la columna "Mes esperado" y la tabla de la sección 2.
2. Decidir escalones por volumen (propuesta) o por calendario (alternativa).
3. Correr la calculadora para Appmaking y confirmar zona verde del escalón 4 y del overage.
4. Confirmar cobertura de conectores por escrito (compromiso del follow-up del 4-sep).
5. Slide: usar el prompt en `claude-design-prompt-pricing-ramp-2026-09-10.md`. Preview renderizado en `appmaking-pricing-ramp.png`.
