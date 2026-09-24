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

## Business case v2 (slides 13 y 14, 24-sep tarde, pedido de German)
Base: 100,000 tx/mes × $20 = $2.0M/mes, $24M/año. Cinco palancas (2 operativas + 3 de costo); script build/rebuild_bc_cruzverde.py (duplica la 4ª tarjeta y la 4ª columna, reubica todo a 5).
| Palanca | Métrica | Conservador | Optimista | Supuesto |
|---|---|---|---|---|
| L1 Aprobación de pagos | 91% → 92.5% / 94% | $0.40M | $0.79M | cerca de 110,000 intentos/mes; +1.5 pp / +3 pp (supuesto Yuno) |
| L2 Nuevos métodos (Apple Pay, Google Pay, Addi, Bre-B, Nequi, Daviplata) | +2% a +5% trx | $0.48M | $1.20M | billeteras 5% + BNPL 4% del ecommerce colombiano (dLocal/AMI); Bre-B 34.9M usuarios; captura de 2% a 5% del volumen (supuesto Yuno) |
| L3 Costo transaccional | 10 a 20 bps | $24K | $48K | sobre $24M de TPV (supuesto Yuno) |
| L4 Costo de integrar (6 métodos en casa) | 6 métodos | $55K | $90K | 8 a 12 semanas de ingeniería por integración (48 a 72 en total), 2 a 3 personas 4 a 8 meses, mantenimiento 20% a 30% anual, $50K por FTE; costo evitado año 1 |
| L5 Operación de pagos | 1 a 2 FTE | $50K | $100K | $50K por persona/año (supuesto Yuno) |
| Total | | $1.00M | $2.23M | promedio $1.62M; ventas incrementales (L1+L2) promedio $1.43M (rango $0.88M a $1.99M); integraciones + operación (L4+L5) promedio $148K (rango $105K a $190K) |
Relación valor/costo: 6x a 13.5x sobre $165K/año. La v1 (L2 = continuidad de PSE 4 a 8 h/mes, $76K/$153K; total $0.55M/$1.09M) queda reemplazada.

**Fuentes de mercado usadas en L2 y L4 (24-sep-2026):**
- Mix ecommerce Colombia: dLocal (fuente AMI): tarjeta de crédito 43%, transferencia 36%, débito 6%, eWallet 5%, BNPL 4%, efectivo 3%. PCMI 2024: crédito 45%, PSE 40%.
- Bre-B: 34,897,402 usuarios vinculados, 105M+ llaves, 782M transacciones acumuladas y hasta 5M operaciones diarias al 4-may-2026 (Banco de la República, indicadores; Infobae 6-may-2026).
- Nequi: más de 26M de usuarios (Infobae, ene-2026). Billeteras en Colombia: 54M usuarios en 13 billeteras (2023, El Tiempo).
- Addi: 2.7M usuarios activos, 33,000 comercios, 47% de usuarios sin tarjeta de crédito (Colombia Fintech 20-feb-2026; descubre.vc 30-ene-2026).
- Apple Pay y Google Pay operan en Colombia con Bancolombia, Davivienda, Banco de Bogotá, AV Villas, Occidente, BBVA, Nu, Nequi, etc. (La República; Apple; Google). Lyra reporta 96% de aprobación en Apple/Google Pay en Colombia (Colombia Fintech, 30-abr-2026), no usado en el deck.
- En Yuno: Apple Pay y Google Pay (docs.y.uno), Nequi y Daviplata (docs.y.uno), Addi (partner BNPL listado por Yuno; logo en el mapa del slide 11). ⚠️ Bre-B en Yuno NO verificado: lo ofrecen dLocal, EBANX, Nuvei, LocalPayment y PayRetailers; el deck dice "Bre-B vía proveedores conectados, a confirmar". Confirmar con Producto antes del viernes.

## Cambios por slide vs Palco
- S1 portada: título "IMPULSANDO PAGOS SIN FRICCIÓN PARA CRUZ VERDE"; lockup yuno | Cruz Verde (wordmark verde recortado del SVG de Wikimedia Commons vía images.weserv.nl).
- S5: título y "UN EQUIPO DEDICADO PARA CRUZ VERDE"; "rieles locales de Colombia".
- S6: "Un solo panel" (antes "Un cerebro"); pilar 4 "INSIGHTS Y DATOS / Todo en un solo lugar"; "Métodos de pago locales: PSE, Nequi, Daviplata y tarjetas" (reemplaza suscripciones); "Reintentos inteligentes" (reemplaza network tokens); "Reportes exportables" (reemplaza Payments Concierge).
- S7: "Tokenización en bóveda PCI" (reemplaza network tokens y account updater); "SDKs web y móviles" (reemplaza suscripciones); "Reportes exportables" (reemplaza Payouts).
- S11: ventajas clave en clave Cruz Verde (una integración para Mercado Pago y cada proveedor nuevo; contratos siguen siendo suyos; monitores con failover; reportes y conciliación).
- S13, S14: reconstruidos a cinco palancas (v2). S16: pricing.
- Sin cambios: S2, S3, S4, S8, S9, S10, S12, S15, S17 a S21.

## Verificaciones
- Mercado Pago, PSE, Nequi y Daviplata aparecen en la documentación pública de Yuno (y.uno/es/integrations/mercado-pago; docs.y.uno). El mapa del slide 11 (asset de Yuno) muestra Nequi, Daviplata, Bancolombia, Wompi y Efecty.
- QA visual de los 8 slides modificados: sin desbordes ni solapes tras la segunda pasada (tramos con "$0.06" grande + "/trx" pequeño; bullets de S11 acortados; pilar 4 de S6 en una línea).
