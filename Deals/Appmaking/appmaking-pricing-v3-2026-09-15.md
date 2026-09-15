# Appmaking + Yuno: pricing v3 (2026-09-15, tras la call corta con Tatsiana)

> **NOTA 15-sep (noche):** German construyó la slide con otros números: platform fee $9,750 / $9,500 / $9,000 / $8,500 / $8,000 y rate $0.09 / $0.08 / $0.06 / $0.05 / $0.045; fully ramped $16,000/mes ($192K/año); año 1 $174,350. El deck es la fuente de verdad; este doc queda como referencia del razonamiento y del chequeo de política.

**Qué cambia frente al deck del 14-sep (v2):** el precio sube. La banda 1 ahora cierra en $12,000 all-in (antes $10,000) y fully ramped queda en $17,500/mes (antes $15,000). Subscriptions engine pasa de "Pending" a precio estándar de Yuno. Monitors se incluyen sin costo (German lo ofreció en la call). Reconciliation, token vault y network tokens, y Verifi/Ethoca siguen en "Pending". Se envía el martes 16-sep.

**Estructura (igual que v2):** platform fee + fee por transacción exitosa, ambos escalonados por banda de transacciones exitosas del mes. La tarifa de la banda aplica a todo el mes. Declinadas gratis, sin setup fee.

## Ladder v3

| Banda | Tx exitosas / mes | Platform fee | Por tx exitosa | All-in al tope de banda |
|---|---|---|---|---|
| 1 | 0 a 25,000 | $6,000 | $0.24 | $12,000 |
| 2 | 25,001 a 50,000 | $6,500 | $0.15 | $14,000 |
| 3 | 50,001 a 100,000 | $7,500 | $0.09 | $16,500 |
| 4 | 100,001 a 150,000 | $8,500 | $0.06 | $17,500 |
| Fully ramped | Más de 150,000 | $8,500 | $0.05 | $18,500 a 200K · $21,000 a 250K · $33,500 a 500K |

## Sobre la curva de Tatsiana (8-sep)

| Mes | Tx | Banda | Factura | Por tx |
|---|---|---|---|---|
| 1 | 20,000 | 1 | $10,800 | $0.540 |
| 2 | 30,000 | 2 | $11,000 | $0.367 |
| 3 | 45,000 | 2 | $13,250 | $0.294 |
| 4 | 65,000 | 3 | $13,350 | $0.205 |
| 5 | 90,000 | 3 | $15,600 | $0.173 |
| 6 | 120,000 | 4 | $15,700 | $0.131 |
| 7 | 150,000 | 4 | $17,500 | $0.117 |
| 8 a 12 | 150,000 | 4 | $17,500 | $0.117 |

- Meses 1 a 7: **$97,200** por 520,000 tx ($0.187).
- Meses 8 a 12: **$87,500** por 750,000 tx ($0.117).
- Año 1: **$184,700** por ~1.27M tx ($0.145). Frente a v2: +$29,125.
- Fully ramped: **$17,500/mes = $210,000/año**.
- La factura sube todos los meses y el unitario baja todos los meses sobre su curva (con estas tarifas no se repite el quirk de v2 donde el mes 4 costaba menos que el mes 3).
- Tatsiana pidió ver 20K y 50K explícitamente: a 20,000 son $10,800; a 50,000 son $14,000.

## Chequeo contra la política (calculadora, referencia V3 / F3)

- Platform fee fully ramped $8,500: bajo la lista F3 ($10,000) y sobre el piso verde ($6,325). Verde.
- $0.06 por tx a 150K y $0.05 arriba: muy por encima del ladder V3 sugerido ($0.03 a $0.04) y del green-down-to ($0.0188). Verde.
- Banda 1: $6,000 sobre la lista F1 ($5,000) y $0.24 sobre la lista V1 ($0.10). Verde.
- Deal size $17,500/mes contra mínimo new logo $10,000. Take rate a 150K: $17,500 sobre $2.7M = 65 bps. Verde.
- ⚠️ Correr la calculadora oficial (duplicar "Yuno — Pricing Palco") antes del Deal Desk.

## Otros productos

| Producto | En la slide | Detalle |
|---|---|---|
| Subscriptions engine (standalone) | **Precio estándar** | Primeros $50,000 procesados gratis, luego $0.05 por transacción que pase por el engine |
| Monitors & alerts | **Incluido** | German lo ofreció sin costo en la call |
| Reconciliation | Pending | German propuso discutirlo después, cuando sepan qué proveedores integran; con Solidgate y el orquestador #2 seguirán con trabajo manual |
| Token vault y network tokens | Pending | TRID propio en revisión legal de ellos |
| Verifi y Ethoca | Pending | No se tocó en la call corta; se mantiene como en v2 |

## Palancas que quedaron abiertas (no van en la slide)

- **Primer mes sin costo** (crédito) a cambio de más volumen: German propuso 250K, Tatsiana no puede decidir sin Dzmitry. Si aceptan, se aplica como crédito del mes 1 y se documenta con inicio y fin (política de créditos: hasta 3 meses sin aprobación).
- **Ramp extendido a 200K:** Tatsiana dijo que podrían dar pasos más grandes hasta 200K, nivel por nivel. La fila "fully ramped" ya muestra $18,500 a 200K y $21,000 a 250K para que vean que "the bigger we get, the pricing looks better".
- **"$20K minimum, $10K + $10K"** fue el ejemplo verbal de German en la call. La propuesta escrita queda por debajo en los primeros meses; no hay conflicto, pero conviene no repetir esa cifra.

## Lo que ella confirmó y afecta la propuesta

- Los MIDs son de ellos ("we are owners of MIDs, I think all of them"; tienen los acuerdos con los bancos). Solidgate tiene adquirencia y su propio PSP, y usan ambos.
- Restricción contractual con Solidgate: los PSPs que Solidgate les ayudó a abrir (Adyen fue el ejemplo) solo se pueden usar a través de Solidgate, aunque el MID sea de ellos. Quieren a Yuno totalmente separado de Solidgate y no piensan dejarlo.
- Ruteo post go-live: si funciona un PSP por dos orquestadores, repartirían tráfico en Unlimit y Ecompay (ya tienen tráfico ahí vía el orquestador #2), sobre todo Europa. Empiezan en 20K y escalan cuando reportes, fraude y todo esté en orden.
- Timeline: listos para arrancar en cuanto acuerden pricing; el TRID y nuevas conexiones con bancos toman tiempo.
