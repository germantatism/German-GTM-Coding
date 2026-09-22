# FlightHub · QA del deck final antes de enviar (2026-09-22)

Deck: Google Slides 1O7nRB5nFt5DGSt_tnGsa0cY7HVQhui4CoCS_gJthczI, 24 slides, revisado en texto y en PDF exportado (todas las slides vistas en imagen).

## Aritmética verificada (todo cuadra)
- Slide 16, a 700,000 tx exitosas: 200K x $0.06 = $12,000; 200K x $0.04 = $8,000; 200K x $0.03 = $6,000; 100K x $0.02 = $2,000; subtotal $28,000; + $10,000 = $38,000/mes; x12 = $456,000; $38,000 / 700,000 = $0.054.
- Low 500K: $23,000 + $10,000 = $33,000/mes, $396,000/año, $0.066. Peak 800K: $30,000 + $10,000 = $40,000/mes, $480,000/año, $0.050.
- Mínimo $20,000 deja de aplicar en 166,667 tx ($10,000 + 166,667 x $0.06): "166,700" correcto.
- Slide 14: 13.7 + 8.2 + 3.7 + 0.40 = 26.00; 18.3 + 11.0 + 4.9 + 0.45 = 34.65; 22.8 + 13.7 + 6.1 + 0.50 = 43.10. L1 + L2 = 84.6% del promedio. Slide 19: 34.65 / 12 = 2.89.
- Slide 13: 700K x $580 x 12 = $4.87B; +4 pts = 28,000 ventas/mes = $195M/año; L1 = 17,500 x 580 x 12 x 15% = $18.3M; L2 = $11.0M; L3 = 7.5 a 12.5 bps sobre $4.87B = $3.7M a $6.1M; L4 = 4 a 5 x $100K.

## Bloqueantes (arreglar antes de enviar)
1. Slide 16, caja inferior izquierda: "NETWORK AND SECURITY TOKENS & RECONCILIATION" y "Network and security tokens: $0.05 ..." deben decir "NETWORK TOKENS & RECONCILIATION" y "Network tokens: ...". "Security tokens" no es producto y contradice "PCI token vault · Included".
2. Slide 13: el encabezado de la palanca 2 se ve "Smart Routing &" (se pierde "Retries"). Acortar a "Routing & retries" o dar espacio.
3. Slide 19 vs 13: build in-house "$0.8M to $1.0M / yr" contra L4 "4 to 5 FTE at $100K" = $0.40M a $0.50M. Arreglo mínimo en la línea Assumptions de la 19: "in-house cost: 4 to 5 payments engineers at $100K fully loaded ($0.4M to $0.5M, the run-ops lever) plus infrastructure, PCI and certification upkeep and tooling (est.)".

## Recomendados (5 minutos)
4. Slide 16: "$15 p|er matched alert": el azul bold se pasa a la "p" de "per".
5. Slide 13, Assumptions: "$580 average ticket,TPV, $4.87B annual" -> "$580 average ticket, $4.87B annual TPV".
6. Slide 18: "4–5 FTE" -> "4 to 5 FTE" (el resto del deck usa "to"); "approval measurement , approved" tiene un espacio antes de la coma.
7. Slides 16 y 19 dicen "450+" proveedores/integraciones; slides 4 y 6 dicen "460+". Unificar.
8. Slide 19: "12 to 18 month build before any value" sin fuente; poner "(est.)" como en la celda de costo.

## Para tener claro al responder (no cambiar)
- El BC usa 700,000 como INTENTOS (86% = 602,000 aprobadas); la slide 16 usa 700,000 como EXITOSAS. A 602,000 la factura sería $36,040/mes ($432,480/año, $0.060). Si Anna-Lena pregunta: la ilustración está en el tope de su rango; la tabla de tiers permite calcular cualquier volumen.
- "Network tokens across all seven providers" (slides 11, 13, 18): confirmar con Jarrett qué proveedores aceptan tokens emitidos por Yuno antes de que lo pregunten.
- GoFundMe aparece como referencia (slide 5 texto, slide 8 logo): la memoria dice pedir permiso para usarlos como referencia.
- Apéndice 21 y 22 compara contra "single PSP/MoR", que no es FlightHub, con stats sin fuente. Opcional quitarlo.
- Policy: network tokens $0.05/$0.01 y reconciliation 200K por $1,500 están bajo mínimo (zona roja, CFO + CRO); alerts $15 y platform fee $10K están en list. Sirve para enviar, no para bookear sin firma.
- El text box "$ 0.71" de las slides 13 y 14 no se ve en el export; no afecta.

## Aplicado en el deck vivo (22-sep, vía Slides API con service account)
- Bloqueante 1: slide 16 ahora dice "NETWORK TOKENS & RECONCILIATION" y "Network tokens: $0.05 per token created, $0.01 per token update".
- Bloqueante 2: slide 13, palanca 2 = "Routing & retries", cabe en una línea (verificado en PDF re-exportado).
- Bloqueante 3: slide 19, Assumptions = "in-house cost: 4 to 5 payments engineers at $100K fully loaded ($0.4M to $0.5M, the run-ops lever) plus infrastructure, PCI and tooling". La caja de texto se estrechó al margen (antes se salía del slide, borde derecho en 1.048 del ancho); ahora envuelve en dos líneas dentro del margen.
- Observado al verificar: German cambió el Tier 5 a $0.018/trx (era $0.015); no afecta los totales de 700K ni 800K. La palanca 1 de la slide 13 dice "Conversion uplift" pero solo se ve "Conversion" (el resto queda oculto, no se nota).
- Script: Deals/FlightHub/build/apply_blocker_fixes_2026-09-22.py. Los recomendados 4 a 8 siguen pendientes.
