# Yango + Yuno · Revisión de la propuesta antes de compartirla (2026-09-24)

**Objeto:** deck "Business Case Yango + Yuno", Slides `1txk0atU1_2jUcEva6WYIQjvNlUp4yO_BPuWHzATOnQw`, 39 slides, última edición 22-sep-2026 23:26. Sección **06 · Proposal** = slides 35 (divider), 36 (pricing), 37 (país por país).

**Veredicto:** la aritmética de la propuesta cuadra completa, pero hay dos puntos de fondo que hay que resolver antes de compartir (reconciliation y mínimo mensual), un residuo oculto que borrar y una verificación visual que no pude hacer (sin acceso de la service account y el export PDF del conector falla por tamaño).

⚠️ El modelo vivo en el deck NO es el que quedó documentado el 22-sep (`yango-pricing-proposal-2026-09-22.md`, % del volumen 0.60/0.50/0.45%). El deck tiene tranches por transacción. Este documento revisa lo que está vivo.

---

## 1. Lo que dice hoy el deck (slides 36 y 37)

**Slide 36 · "Proposal · Platform fee plus a fee per approved recharge"**

| Tranche | Tx / mes | Tarifa |
|---|---|---|
| 1 | 0 a 500K | $0.023 |
| 2 | 500K a 1M | $0.020 |
| 3 | 1M a 1.5M | $0.017 |
| 4 | 1.5M a 2M | $0.014 |
| 5 | 2M a 3M | $0.011 |
| 6 | > 3M | $0.008 |

Platform fee $10,000 / mes ($120,000 / año). **"Monthly minimum billing: $25,000."** Add-ons: network tokens $0.05 / $0.01; **reconciliation $2,000 / mes por los primeros 500K tx conciliadas, luego $0.0003 / tx**. Nova ya no aparece. Término 3 años, tarifas fijas, tranches revisadas anualmente, USD.

"What it means for Yango" a 3.24M tx / $7.3M por mes: tx fee $49,930 + $10,000 = **$59,930 / mes, $719,165 / año, $0.018 por recarga**. Colombia + Perú primero: $33,414 / mes sobre 1.11M recargas. Caso del rail de tarjeta $3.21M = 4.5x el costo; el lever de MDR $0.88M lo supera.

**Slide 37 · "Country by country: what each market carries at full volume"**: asigna el tx fee y el platform fee por participación en transacciones: Colombia $10,194 (17.0%), Perú $10,377 (17.3%), Bolivia $33,865 (56.5%), Venezuela $5,494 (9.2%). Banda: $59,930 / mes · $719,165 / año · $0.018.

## 2. Verificación aritmética (todo cuadra)

Recalculado con `build/yango_pricing_model.py` (sección LIVE):

| Cifra en el deck | Recalculado | OK |
|---|---|---|
| Tranche 6 · 0.24M at $0.008 = $1,930 / $23,165 | 241,304 × 0.008 = $1,930.43 / $23,165 | ✅ |
| Total $59,930 / $719,165 | $59,930.43 / $719,165.18 | ✅ |
| $0.018 por recarga | $0.01849 | ✅ (redondeo hacia abajo; $0.0185 sería más exacto) |
| CO + PE $33,414 sobre 1.11M | $33,414.10 sobre 1,112,594 | ✅ |
| 4.5x el costo | 3,210,000 / 719,165 = 4.46 | ✅ |
| $0.88M supera el costo anual | 880,000 > 719,165 | ✅ |
| Colombia $10,194 = $8,493 + $1,701 (17.0%) | $10,193.58 | ✅ |
| Perú $10,377 = $8,646 + $1,731 (17.3%) | $10,377.85 | ✅ (se dejó en $10,377 para que la suma cierre en $59,930) |
| Bolivia $33,865 = $28,214 + $5,651 (56.5%) | $33,865.21 | ✅ |
| Venezuela $5,494 = $4,577 + $917 (9.2%) | $5,493.80 | ✅ |
| Agenda 06 PROPOSAL, divider "06 Proposal", eyebrow, footer | presentes | ✅ |

## 3. Hallazgos, por severidad

### 🔴 A. Reconciliation a $0.0003 por transacción (slide 36, add-ons)
- Policy (Doc Laura Galan): list $2,500 / mes + $0.03 / tx; **mínimo $1,500 / mes + $0.0085 / tx**; pack 3M tx = $30,000 / mes.
- Lo que dice el deck a volumen pleno: $2,000 + 2.74M × $0.0003 = **$2,822 / mes**. Diez veces por debajo del mínimo. Con $0.003 seguiría en rojo.
- El 22-sep quedó "Pending review" justamente porque conciliar 3.24M tx / mes bajo policy (~$30K) duplicaría la factura.
- Qué hacer: volver a "Pending review" (sin número) o cotizar dentro de policy (tranches por tx conciliada nunca bajo $0.0085, o pack). Si es una decisión deliberada, va a CFO + CRO.

### 🔴 B. "Monthly minimum billing: $25,000" (slide 36, tarjeta platform fee)
1. **Ambiguo:** no dice si los $25,000 incluyen el platform fee. Policy: fixed fee + MMG aditivo es lo preferido; MMG embebido en la fee fija = excepción legacy vía 🟡.
2. **Contradice lo pedido:** Alejandro (Gong 19-ago) "heavily prefer variable-only rates for global agreements" por el ticket bajo; Sean: "platform fee o mínimo, no ambos".
3. **Choca con la slide 37:** con solo Colombia viva la factura calculada es $22,526 (tx fee $12,526 + $10,000) y se facturaría $25,000. La slide 37 muestra "Colombia · MONTHLY COST AT FULL VOLUME $10,194" bajo la etiqueta "STEP 1 · GOES LIVE FIRST". Javier puede leer $10K y recibir una primera factura de $25K.
- Qué hacer, una de dos:
  - (i) Quitar el mínimo. Queda $10,000 + tranches, coherente con "variable" y con Sean. Nada más cambia.
  - (ii) Mantenerlo y escribirlo claro: "Minimum monthly invoice: $25,000, platform fee included", y agregar la rampa en la slide 37 (ver C).

### 🟡 C. Slide 37 mezcla secuencia y asignación
- Etiquetas "STEP 1 · GOES LIVE FIRST … STEP 4" con cifras "at full volume". El intro sí lo explica ("split by each market's share of transactions"), pero el lector rápido se queda con "Colombia cuesta $10,194".
- Qué hacer: en el intro, cambiar "Sequence shown as Yango proposed it: Colombia and Peru first, then Bolivia and Venezuela." por "Sequence as Yango proposed it: Colombia first ($22,526 a month on its own), then Peru ($33,414 for both), then Bolivia and Venezuela." (si el mínimo se mantiene: "…$22,526 a month on its own, billed at the $25,000 minimum…"). Rampa completa: CO $22,526 → +PE $33,414 → +BO $57,386 → +VE $59,930.
- Preparar la objeción de Bolivia: carga 56.5% del costo ($33,865 = 1.23% de su volumen) con 37.6% del volumen, por el ticket de $1.50. Respuesta: sigue siendo la mitad de los 240 bps de Unlimit / Inswitch, y el pool de tranches es lo que baja la tarifa de todos.

### 🟡 D. Residuo oculto "$ 75.56" en slides 34, 36 y 37
- Caja de texto con "$ 75.56" que no existía en el PDF del 4-sep y hoy aparece en la slide 34 y en las dos slides nuevas (se duplicó con la base). Las cajas hermanas "$ 0.71" / "$ 0.40" son texto blanco de 8 pt detrás de las tablas (invisibles, verificado en el PDF del 4-sep), así que probablemente esta también, pero en las slides 36 y 37 no hay tabla que la tape.
- Qué hacer: en Slides, Ctrl+F "75.56" y borrar las tres, o correr `build/apply_review_fixes_2026-09-24.py --apply --delete-stray`.

### 🟡 E. Verificación visual pendiente (no pude hacerla)
- Seis tranches en la tarjeta izquierda de la slide 36 (el diseño del 22-sep tenía tres): confirmar que las filas no se solapan con la caja de nota de abajo ([[feedback_no_slide_overlap]]).
- Para hacerla desde aquí: compartir el deck con `gtm-claude-editor@gtm-claude-tools-260922.iam.gserviceaccount.com` como Editor y correr el script con `--thumbs`.

### 🟡 F. Modelo por transacción frente a lo que pidió Alejandro
- Gong 19-ago: prefieren tarifa variable pura porque el ticket bajo hace pesar los fijos por transacción. El deck ahora cotiza $ por recarga. En Bolivia (ticket $1.50) $0.023 es 1.53% del ticket en la banda 1; $0.008 es 0.53%.
- Es defendible (tarifa efectiva pooled $0.0154 / tx = 0.68% del volumen sin platform fee; 0.82% all-in) y sigue muy por debajo de 240 bps, pero conviene tener a mano el modelo % del 22-sep (0.60 / 0.50 / 0.45%, $47,873 / mes) como alternativa si insisten en "variable".

### 🟡 G. Fecha de la fuente
- Slide 31: "Source: Yango's own recharge data, July 2026". Slides 30 y 36: "Yango's own August 2026 data". Unificar; si el mes de datos es julio y se compartió en agosto: "recharge data for July 2026, shared August 2026".

### Pre-existentes (ya los vio Javier en la versión del 4-sep; no bloquean)
- Slide 7 "Expected Impact +6 pp completed top-ups / +2 pp acceptance rate": el +6 pp no sale del BC (el BC usa +2 pp CO/PE/BO y +5.5 pp VE).
- Em-dashes en slides 3, 6, 10 y en las de inDrive; cierre "German Tatis - Business Development Manager" ([[feedback_no_dashes]]).

## 4. Pricing Policy · zonas del modelo vivo (INTERNO, nunca al cliente)

Segmento Yango: V4 (1M a 5M tx / mes) × M1 (mobility, margen fino). Strategic merchant (3.24M tx / mes ≥ 1.2M).

| Ítem | Deck | List / mínimo | Zona |
|---|---|---|---|
| Pay-ins tranche 6 | $0.008 | Doc min $0.01 (Cheatsheet min $0.08) | 🔴 bajo el mínimo del Doc; todo 🔴 según Cheatsheet |
| Pay-ins tranches 1 a 5 | $0.023 a $0.011 | list $0.10 / min $0.01 | 🟡 según Doc, 🔴 según Cheatsheet |
| Platform fee | $10,000 | V4 list $16,000 / min $4,000 | 🟡 |
| Mínimo mensual $25,000 | embebido o aditivo, no definido | aditivo preferido; embebido = excepción | 🟡 (y "el MMG nunca autoriza bajar del piso de $0.01") |
| Network tokens | $0.05 / $0.01 | min $0.20 / $0.04 | 🔴 |
| Reconciliation | $2,000 + $0.0003 / tx | min $1,500 + $0.0085 / tx | 🔴 (ver A) |
| Término 3 años | | plazos largos | 🟡 |
| Deal size | $719K / año | ≥ 10K | ✅ |

Fundamental #1: cotizar después de Salesforce. Rojo = CFO/Global Controller + CRO, SLA 5 días hábiles.

## 5. Después de corregir
1. Re-exportar el PDF y subirlo a Papermark en el mismo slug (deck.y.uno/yangobclatam) para que el link que Javier abrió el 16-sep muestre la sección.
2. Responder a Javier (WhatsApp; ajustar si el mínimo se mantiene):

> Javi, tienes toda la razón, el business case no traía los costos de Yuno. Ya le agregué una sección de propuesta al mismo deck, para Colombia, Perú, Bolivia y Venezuela: una tarifa por recarga aprobada que arranca en $0.023 y baja hasta $0.008 a medida que se suma el volumen de los cuatro países, sin cobrar declines ni verificaciones de tarjeta, más un platform fee de $10,000 al mes que cubre toda la plataforma y el equipo dedicado. Con los volúmenes que nos compartieron queda en unos $60K al mes con los cuatro países vivos, y arrancando por Colombia y Perú en unos $33K. Está en el mismo link. Si te sirve, lo recorremos con tu equipo o con HQ en una llamada esta semana.

## 6. Archivos
- `build/yango_pricing_model.py`: sección LIVE con el modelo por transacción (tranches, rampa con mínimo, asignación por país, add-on de reconciliation contra policy).
- `build/apply_review_fixes_2026-09-24.py`: service account, dry-run por defecto; borra "$ 75.56", aclara el mínimo, agrega la rampa en la slide 37, unifica la fuente y exporta thumbnails para la QA visual.
- `yango-pricing-proposal-2026-09-22.md`: el modelo % anterior, ahora alternativa.
