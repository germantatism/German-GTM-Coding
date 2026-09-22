# Yango + Yuno · Propuesta comercial para Colombia, Perú, Bolivia y Venezuela (2026-09-22)

**Por qué existe:** Javier Patiño escribió que en el business case (deck "Business Case Yango + Yuno", Slides `1txk0atU1_2jUcEva6WYIQjvNlUp4yO_BPuWHzATOnQw`, 36 slides, enviado el 4-sep vía deck.y.uno/yangobclatam) no encontró cómo serían los costos de Yuno. Este documento define la propuesta que entra como sección nueva **06 · Proposal** del mismo deck (divider + 2 slides), con la misma lógica de las propuestas de FlightHub (22-sep) y Appmaking (21-sep).

**Estado:** propuesta construida, NO enviada. Antes de mandarla: (1) pasarla por Salesforce (fundamental #1 de la Pricing Policy: cotizar después de la aprobación), (2) resolver las zonas amarilla y roja listadas abajo con Juan Sebastián Bernate / Laura Galan, (3) subir el PDF nuevo a Papermark para que el mismo link muestre la sección.

---

## 1. Lo que dijeron ellos, y lo que eso obliga

| Dato | Fuente | Efecto en la propuesta |
|---|---|---|
| Ticket promedio $1.50 a $3.50 (blended $2.25) | Data de Yango, ago-2026 (slide 31) | Cualquier fijo por transacción pesa mucho; $0.05/tx sería 2.2% del ticket |
| "Preferimos tarifa variable para acuerdos globales, porque con el ticket bajo los costos fijos nos pegan" | Alejandro Sanabria, call 19-ago (Gong) | La transacción se cobra como **% del volumen aprobado**, no como $ por tx |
| Unlimit 2.4% flat; Inswitch 2.4% + COP 150; PayU en Perú | Call 19-ago | Yuno se compara contra 240 bps: la tarifa de Yuno debe verse como una fracción de eso |
| Quieren todo consolidado en una plataforma (y minimizar movimientos por el 4x1000) | Call 19-ago | Un solo contrato y un solo stream de volumen para los cuatro países |
| "Propuesta conjunta hacia Colombia y Perú" primero; Bolivia y Venezuela después | Javier, WhatsApp 18-ago | La slide 2 muestra el costo país por país en esa secuencia |
| Binding de tarjeta falla 30 a 32% por adquirencia cross-border; 90 a 92% una vez vinculada | Call 19-ago | La verificación (pre-auth) no se cobra: es el corazón del pitch |
| Volumen 3.24M tx/mes, $7.3M/mes en recargas aprobadas | Data de Yango (slide 31), anual / 12 | Segmento V4 (1M a 5M tx/mes), industria mobility = M1 (margen fino). Yango califica como **strategic merchant** (≥ 1.2M tx/mes) |

Volúmenes mensuales (data de Yango / 12, exactamente lo que usa el deck):

| País | Recargas aprobadas / mes | Transacciones / mes | Ticket |
|---|---|---|---|
| Colombia | $1,929,598 | 551,314 | $3.50 |
| Perú | $1,796,096 | 561,280 | $3.20 |
| Bolivia | $2,747,371 | 1,831,581 | $1.50 |
| Venezuela | $831,960 | 297,129 | $2.80 |
| **Total** | **$7,305,025** | **3,241,304** | $2.25 |

Nota de alcance: el deck dice que la tarjeta es donde Yango es el merchant y que los APMs los cobran ~80 flotas. El business case (slides 30 a 32) usa igual los $87.7M completos como base del rail de tarjeta, así que la propuesta ilustra sobre ese mismo volumen. Si solo pasa por Yuno la porción de tarjeta, la factura baja en proporción y las tarifas no cambian.

---

## 2. La propuesta (lo que va en la slide)

**Platform fee:** $10,000 / mes ($120,000 / año). Cubre: KAM y TAM dedicados, +1,000 métodos, +450 proveedores, +50 herramientas antifraude, orquestación y motor de reglas, smart routing y retries, monitores y auto-failover, PCI token vault, reporting y dashboard.

**Transaction fee:** porcentaje del volumen de recargas aprobadas del mes, sumando Colombia, Perú, Bolivia y Venezuela en un solo stream (tranches: cada banda aplica solo al volumen dentro de ella).

| Tranche | Volumen aprobado / mes | Tarifa | Equivalente por tx al ticket blended $2.25 |
|---|---|---|---|
| 1 | $0 a $2.5M | 0.60% | $0.0135 |
| 2 | $2.5M a $5M | 0.50% | $0.0113 |
| 3 | Más de $5M | 0.45% | $0.0101 |

Sin setup fee. Sin fijo por transacción. Declines y verificaciones de tarjeta (binding) no se cobran.

**Add-ons (uso, encima de lo anterior):** network tokens $0.05 por token creado y $0.01 por update; reconciliation, pending review; Nova (recuperación de top-ups fallidos, slide 13), pending review.

**Término:** 3 años, tarifas fijas, tranches revisadas anualmente con el volumen. Todo en USD.

### Qué significa para Yango (los cuatro mercados vivos)

| Línea | Mensual | Anual |
|---|---|---|
| Tranche 1 · $2.5M al 0.60% | $15,000 | $180,000 |
| Tranche 2 · $2.5M al 0.50% | $12,500 | $150,000 |
| Tranche 3 · $2,305,025 al 0.45% | $10,373 | $124,471 |
| Platform fee | $10,000 | $120,000 |
| **Total** | **$47,873** | **$574,471** |

- All-in: $0.0148 por recarga aprobada (se muestra $0.015), 0.66% del volumen. Tarifa transaccional efectiva 0.52%.
- Contra el caso del rail de tarjeta del deck ($3.21M/año: $2.33M aceptación + $0.88M MDR): el caso es **5.6 veces** el costo. El lever de MDR solo ($0.88M estimado) ya supera el costo anual.
- Contra lo que pagan hoy: 66 bps all-in frente a 240 bps de Unlimit / Inswitch.

### País por país, en la secuencia que propuso Javier (acumulado, tranches compartidas)

| Paso | Volumen acumulado / mes | Tx acumuladas | Fee transaccional | Total / mes | Lo que agrega el país | All-in por recarga |
|---|---|---|---|---|---|---|
| 1 · Colombia | $1,929,598 | 551,314 | $11,578 (todo al 0.60%) | **$21,578** | $21,578 (incluye el platform fee) | $0.039 |
| 2 · + Perú | $3,725,694 | 1,112,594 | $21,128 | **$31,128** | +$9,551 (parte al 0.60%, el resto al 0.50%) | $0.028 |
| 3 · + Bolivia | $6,473,065 | 2,944,175 | $34,129 | **$44,129** | +$13,000 (parte al 0.50%, el resto al 0.45%) | $0.015 |
| 4 · + Venezuela | $7,305,025 | 3,241,304 | $37,873 | **$47,873** | +$3,744 (todo al 0.45%) | $0.015 |

El orden es de Yango; como el volumen se suma en un solo stream, el total a volumen completo no cambia con la secuencia. Suma de "lo que agrega": 21,578 + 9,551 + 13,000 + 3,744 = 47,873. Verificado con `build/yango_pricing_model.py`.

Asignación a tarifa efectiva (0.518%) si se quiere hablar de "cuánto paga cada país" con los cuatro vivos: Colombia $10,004, Perú $9,312, Bolivia $14,244, Venezuela $4,313 al mes (suma $37,873, sin platform fee). No va en la slide para no mostrar dos cifras distintas por país.

---

## 3. Pricing Policy: zonas y aprobaciones (INTERNO, no va al cliente)

Fuente: Doc `Yuno_Pricing_Policy_Merchants_Banking_DRAFT_WIP` (Laura Galan) leído el 21-sep y Cheatsheet `17Fv6SB8M-e-2zqCLzYWUSpsWe8wkt-60Aw9gs_ZxYZs` leída hoy. Segmento de Yango: **V4 × M1**.

| Ítem | Propuesta | List / mínimo | Zona | Qué hacer |
|---|---|---|---|---|
| Platform fee | $10,000 | V4 list $16,000 · min $4,000 | Probablemente 🟡 (el piso verde de V3 fue $6,325 = 63% del list; para V4 sería ~$10,100) | Si se quiere verde sin discusión, $12,000 (+$2,000/mes). Yango pidió variable: mantener $10,000 y pasar por RevOps |
| Pay-ins como % de TPV | Permitido ("fixed $ or % of TPV") | | ✅ | Un solo stream (sin split por país). Un split por país dejaría a Bolivia en $0.0068/tx (0.45% × $1.50), por debajo del mínimo |
| Pay-ins, nivel | 0.60 / 0.50 / 0.45% = $0.0135 / $0.0113 / $0.0101 por tx | Doc: list $0.10, **min $0.01**. Cheatsheet: list $0.10, **min $0.08** (ejemplo $0.0825) | 🟡 según el Doc (todas las bandas ≥ $0.01) · 🔴 según la Cheatsheet | ⚠️ Los dos documentos se contradicen. Con un ticket de $2.25 ningún precio viable llega a $0.08. Yango es strategic merchant (3.24M tx/mes ≥ 1.2M): la zona roja es "decisión deliberada" con CFO + CRO (5 días hábiles). Confirmar con Laura / Juan Sebastián cuál mínimo aplica ANTES de enviar |
| Verificación de tarjeta no cobrada | "Declines and card verification attempts cost nothing" | Doc: "Card verification: PENDING si cuenta como tx" | ⚠️ pendiente en policy | Es el corazón del pitch (binding). Confirmar con Finance que la pre-auth de $0 no factura; si contara, serían ~$0.0135 por intento en la banda 1 |
| Network tokens | $0.05 / $0.01 | list $0.35 / $0.07 · min $0.20 / $0.04 | 🔴 (igual que FlightHub y Appmaking) | Misma decisión que en las dos propuestas anteriores; sin firma aún en ninguna |
| Reconciliation | Pending review | packs: 1M $14,000 · 3M $30,000 / mes; min $1,500 + $0.0085/tx | n/a | A 3.24M tx/mes conciliar costaría ~$30,000/mes (pack 3M): duplicaría la factura. Por eso queda pending, atado al "joint data sprint" del deck |
| Nova | Pending review | PENDING (cost-plus) | n/a | No cotizable aún |
| Término 3 años | Igual que FlightHub y Appmaking | plazos largos = 🟡 | 🟡 | Palanca de negociación |
| Billing | USD; platform fee anual upfront (estándar), uso mensual in arrears | mensual = 🟡 | | Si Yango quiere facturación local, Colombia está en la excepción LC/LC (MX, CO, BR, QA, SA) |
| Deal size | $574K/año | "no puede ser menor a 10k" | ✅ | |

**Mínimo de policy que nunca se muestra al cliente.** En la slide solo van las tarifas cotizadas.

---

## 4. Alternativas que quedan en el bolsillo (no se presentan)

| Alternativa | Estructura | Total / mes a volumen completo | Comentario |
|---|---|---|---|
| A · Por transacción (estilo FlightHub) | $10,000 + $0.015 (0 a 1M) / $0.012 (1M a 2M) / $0.011 (2M a 3M) / $0.010 (>3M) | $50,413 ($604,956/año, $0.0156/tx, 0.69%) | Contradice lo que pidió Alejandro; pega más a Bolivia ($1.50 de ticket) |
| B · % más bajo | 0.55 / 0.45 / 0.40% | $44,220 ($530,640/año) | La banda 3 queda en $0.009/tx, bajo el mínimo del Doc: 🔴 seguro |
| C · Platform fee $12,000 | igual, con fijo verde | $49,873 ($598,471/año) | +$24,000/año; usar si RevOps frena el $10,000 |
| D · Mínimo mensual en vez de platform fee | $0 fijo + MMG $20,000 | depende | Sean: "platform fee O mínimo, no ambos". Yango pidió variable; el MMG es la forma de darles "sin fijo" sin regalar la plataforma |
| E · Ramp con credits | m1 a m3 platform fee $0 vía credits | | Cubre la fase Connect / Compare (deck slide 8) sin tocar el precio; policy lo permite (credits solo contra fijos) |

---

## 5. Cómo se lee en la sala

1. "Ustedes pidieron variable: es variable." 0.60% que baja a 0.45% sobre recargas aprobadas, nada por transacción, nada por declines ni por verificaciones. Frente a los 240 bps del rail, Yuno es una fracción.
2. "Un contrato, cuatro países." El volumen se suma: cada mercado que entra cae en una banda más barata. Colombia y Perú primero, como propuso Javier: $31K al mes; los cuatro, $48K.
3. "El caso se paga solo." $3.21M al año identificados en el rail de tarjeta contra $574K de costo: 5.6 veces. El ahorro de MDR estimado ya cubre la factura.
4. Objeción "el platform fee es fijo": lo que cubre (KAM/TAM, 450 conectores, routing, monitores, vault, dashboard) y la alternativa D (MMG) si insisten.
5. Objeción "¿por qué no Inswitch/Unlimit directo?": porque ninguno arregla el binding cross-border ni cubre los cuatro países; Yuno rutea entre ellos y el adquirente local.

---

## 6. Respuesta a Javier (WhatsApp, enviar DESPUÉS de la aprobación en Salesforce)

> Javi, tienes toda la razón, el business case no traía los costos de Yuno. Ya le agregué una sección de propuesta al mismo deck, para Colombia, Perú, Bolivia y Venezuela: una tarifa variable sobre las recargas aprobadas que arranca en 0.60% y baja a 0.45% con volumen, sin fijo por transacción como nos pidió Alejo, más un platform fee de $10,000 al mes que cubre toda la plataforma y el equipo dedicado. Con los volúmenes que nos compartieron queda en unos $48K al mes con los cuatro países vivos, y arrancando por Colombia y Perú en unos $31K. Está en el mismo link. Si te sirve, lo recorremos con tu equipo o con HQ en una llamada esta semana.

Si prefiere correo, el mismo texto como reply al hilo "Yango + Yuno: resumen de la llamada y próximos pasos" (a Javier, Alejo y Luis; cc Justo, Majo, jpatino@yango.com).

---

## 7. Archivos

- `build/yango_pricing_model.py`: toda la aritmética de este documento.
- `build/yango_proposal_slides.py`: construye la sección (agenda, divider, 2 slides) vía Slides API con la service account. Modo scratch (deck propio de la SA, para QA) y modo `--pid` sobre el deck real una vez compartido con `gtm-claude-editor@gtm-claude-tools-260922.iam.gserviceaccount.com` como Editor.
- `claude-design-prompt-proposal-section-2026-09-22.md`: el mismo contenido como prompt de Claude Design, por si se prefiere esa vía.
