# Propuesta - Cruz Verde + Yuno (Google Slides, 2026-09-24)

Deck: https://docs.google.com/presentation/d/1VTuUxAAyVVrbEkpce2z2zih3YbfaEEsQ6eUSMZwubxk/edit
Origen: copia Drive de "Propuesta - Palco + Yuno" (1hWX6sNKKPpXhDSKGlZzrHWyKWMx5WlVxBeScEL_J7UY), carpeta Drive "Cruz Verde" (1Q647xvALkM-qbxH7HFzyErT-QvBlSFZ0). 21 slides, misma estructura que Palco.
Vía: service account gtm-claude-editor (compartido como editor desde el conector de Drive, funcionó). Scripts en build/: content_cruzverde.py (texto por element ID), build_cruzverde.py (dry / apply), fix_cruzverde.py (segunda pasada).
Contexto: sesión con Gerencia y TI de Cruz Verde el viernes 25-sep-2026 11:00 (enfoque comercial y de valor de negocio, pedido por Michael Vargas). Alejandro Albarracín compartió el "Yuno — Pricing Calculator V2 - Cruz Verde" (1F5pFJxj0p9WNQQXlhHO0iyyrhWaHmV1kFmJssk7NyY4): Retail, 97,000 tx/mes, AOV $20, V2 × M2.

## Datos del cliente usados (call 21-may-2026, Gong 8940587603862854221)
- Más de 100,000 transacciones al mes: 80,000 por Mercado Pago + 20,000 en efectivo. Mercado Pago es el único proveedor.
- PSE = 58% de las ventas. Aprobación 91% (sin reintentos). Fraude por debajo de 0.05%.
- Ticket: COP 130,000 y a la baja, 40% de las tx bajo COP 30,000. En el deck se usa $20 (dato de German 24-sep y del calculator). ⚠️ Confirmar con Cruz Verde: COP 130,000 equivale a bastante más de $20.
- Dolores: dependencia de un solo proveedor, caídas de PSE, rechazos altos con fraude bajo, devoluciones de PSE.

## Pricing (slide 16), según instrucción de German 24-sep
| Concepto | Precio | A 100,000 tx exitosas |
|---|---|---|
| Fee de plataforma | $7,500 / mes | $7,500 |
| Tramo 1: 0 a 25,000 | $0.06 / tx | $1,500 |
| Tramo 2: 25,001 a 50,000 | $0.04 / tx | $1,000 |
| Tramo 3: más de 50,000 | $0.035 / tx | $1,750 |
| Subtotal pagos | | $11,750 / mes ($141,000 / año) |
| Conciliación (tarifa fija) | $2,000 / mes | $2,000 |
| **Total** | | **$13,750 / mes ($165,000 / año)** |
- ≈ $0.118 por tx en pagos, ≈ $0.138 con conciliación. A 150,000 tx: $7,500 + $6,000 = $13,500 en pagos (≈ $0.090 / tx).
- Cortes de tramo (25K / 50K) los fijé yo: German no los dio; el calculator usa 24,250 / 48,500 sobre 97,000. Ajustar si prefiere otros.
- Contra el calculator (todo verde): platform sugerido $7,000; pay-ins sugeridos $0.0553 / $0.0449 / $0.0378 (verde hasta $0.0235 / $0.0212 / $0.0194); conciliación sugerida $0.0234 / tx (≈ $2,340 a 100K; verde hasta $0.0141 ≈ $1,410). Deal size $13,750 > mínimo $10,000.
- Incluido en plataforma (lo de siempre): +1,000 métodos, +450 procesadores, +50 conexiones antifraude, orquestación y reglas, smart routing y reintentos, monitores y alertas, usuarios y roles, reportes y dashboard, KAM y TAM. **Token vault NO incluido** (German, 24-sep, tercera pasada: fix2_vault_cruzverde.py); sigue nombrado solo como capacidad de la suite en S6 y S7.
- Franja "Seguridad y riesgo" = opcional según consumo, fuera del total: 3DS $0.04, antifraude $0.018 (precios sugeridos del calculator), reglas de riesgo incluidas. ⚠️ German no las pidió: borrar la franja si no quiere abrir ese tema.
- "Contrato a 3 años" quedó igual que en Palco. ⚠️ Confirmar.
- Sin network tokens, sin IA (Payments Concierge), sin suscripciones en todo el deck (instrucción de German).

## Business case (slides 13 y 14)
Base: 100,000 tx/mes × $20 = $2.0M/mes, $24M/año.
| Palanca | Métrica | Conservador | Optimista | Supuesto |
|---|---|---|---|---|
| L1 Aprobación de pagos | 91% → 92.5% / 94% | $0.40M | $0.79M | ~110,000 intentos/mes; +1.5 pp / +3 pp (supuesto Yuno) |
| L2 Continuidad de PSE | 4 a 8 h/mes | $76K | $153K | PSE 58% de ventas ≈ $1,600/hora (730 h/mes) |
| L3 Costo de procesamiento | 10 a 20 bps | $24K | $48K | sobre $24M de TPV (supuesto Yuno) |
| L4 Operación de pagos | 1 a 2 FTE | $50K | $100K | $50K por persona/año (supuesto Yuno) |
| Total | | $0.55M | $1.09M | promedio $0.82M; ventas recuperadas (L1+L2) promedio $0.71M |
Los rangos son supuestos de modelación y así se declaran en ambos slides ("a validar con su data"). Relación valor/costo: 3.3x a 6.6x sobre $165K/año.

## Cambios por slide vs Palco
- S1 portada: título "IMPULSANDO PAGOS SIN FRICCIÓN PARA CRUZ VERDE"; lockup yuno | Cruz Verde (wordmark verde recortado del SVG de Wikimedia Commons vía images.weserv.nl).
- S5: título y "UN EQUIPO DEDICADO PARA CRUZ VERDE"; "rieles locales de Colombia".
- S6: "Un solo panel" (antes "Un cerebro"); pilar 4 "INSIGHTS Y DATOS / Todo en un solo lugar"; "Métodos de pago locales: PSE, Nequi, Daviplata y tarjetas" (reemplaza suscripciones); "Reintentos inteligentes" (reemplaza network tokens); "Reportes exportables" (reemplaza Payments Concierge).
- S7: "Tokenización en bóveda PCI" (reemplaza network tokens y account updater); "SDKs web y móviles" (reemplaza suscripciones); "Reportes exportables" (reemplaza Payouts).
- S11: ventajas clave en clave Cruz Verde (una integración para Mercado Pago y cada proveedor nuevo; contratos siguen siendo suyos; monitores con failover; reportes y conciliación).
- S13, S14, S16: reconstruidos con los datos de arriba.
- Sin cambios: S2, S3, S4, S8, S9, S10, S12, S15, S17 a S21.

## Verificaciones
- Mercado Pago, PSE, Nequi y Daviplata aparecen en la documentación pública de Yuno (y.uno/es/integrations/mercado-pago; docs.y.uno). El mapa del slide 11 (asset de Yuno) muestra Nequi, Daviplata, Bancolombia, Wompi y Efecty.
- QA visual de los 8 slides modificados: sin desbordes ni solapes tras la segunda pasada (tramos con "$0.06" grande + "/trx" pequeño; bullets de S11 acortados; pilar 4 de S6 en una línea).
