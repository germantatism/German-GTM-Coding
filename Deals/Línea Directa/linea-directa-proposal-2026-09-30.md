# Propuesta - Línea Directa + Yuno (Google Slides, 2026-09-30)

Deck: https://docs.google.com/presentation/d/126rE0knbVczAsHtRVCtRWopV4lOh3yrKx5038hhjdew/edit (carpeta Drive "Línea Directa", 1DJqAtQ4fhAidFIzEFb-wGin5R_unhThB)
Origen: copia Drive de "Propuesta - Palco + Yuno" (1hWX6sNKKPpXhDSKGlZzrHWyKWMx5WlVxBeScEL_J7UY). 22 slides: los 21 de Palco más un slide nuevo de métodos de pago (S16).
Vía: conector de Drive (copia + compartir con la service account gtm-claude-editor) y Slides API. Scripts en build/.

## Datos del cliente usados
Fuentes: correo de Luis Paternina del 24-sep-2026 y notas de la llamada del 30-sep-2026 (el transcript de Meet salió ilegible; Fireflies no fue admitido).
- 300,000 transacciones digitales al mes en Colombia y 25,000 en Perú.
- Ticket promedio COP 180,000 y PEN 200.
- Mix: cerca de 70% digital y 30% físico (Efecty, Gana, Supergiros, corresponsales). Nequi cerca de 55% del total.
- Portal de pedidos: el cliente ve su saldo y paga antes de hacer un nuevo pedido. Integraciones hoy: PSE directo, Bancolombia/Wompi directo, Nequi vía plataforma. Sin tarjetas. Sin PCI.
- 150,000 clientes por campaña, 18 campañas al año (no se usó en el cálculo).
- Dos entidades legales (Colombia y Perú), mismo grupo.

## Pricing (S17), instrucción de German 30-sep
| Concepto | Precio | A 325,000 tx exitosas |
|---|---|---|
| Fee de plataforma | $15,000 / mes | $15,000 |
| Tramo 1: 0 a 150,000 | $0.06 / tx | $9,000 |
| Tramo 2: más de 150,000 | $0.05 / tx | $8,750 |
| **Total** | | **$32,750 / mes ($393,000 / año), $0.101 por tx, 18.6 bps** |

- A 400,000 tx: $15,000 + $21,500 = $36,500 ($0.091 por tx).
- Sin conciliación ni productos extra. Franja inferior: "Opcional, para revisar después" con orquestación y smart routing, monitores y alertas, network tokens, sin precio.
- Incluido: +1,000 métodos, +450 procesadores, una integración para Colombia y Perú, checkout alojado (PCI), cuenta matriz y subcuentas por país, gestión de transacciones, usuarios y roles, reportes y dashboard, sandbox, KAM y TAM.

**Supuestos míos, por confirmar con German:**
1. Corte de tramo en 150,000 (German dio las tarifas, no el corte).
2. Fee de plataforma $15,000: es el número dicho en la llamada; German solo cambió las tarifas por transacción.
3. "Sin fee de setup" y "Contrato a 3 años" quedaron heredados de Palco.
4. El volumen de Colombia y Perú suma para el tramo (una sola escala sobre 325,000).

**Contra la Pricing Policy:** platform $15,000 está por encima del list de V3 ($10,000). Pay-ins $0.06 y $0.05 contra list $0.10: la zona depende del calculator; moda cae en M4 (luxury & apparel), no en M2 como Palco, así que hay que validarlo en el calculator y pasar por Salesforce antes de enviar. Dos entidades legales: definir cómo se reparte el fee de plataforma. Entidad colombiana contra entidad colombiana puede obligar a facturar en pesos.

## Business case (S13 y S14), build/model.py
Base: 300,000 × COP 180,000 y 25,000 × PEN 200, llevados a dólares a tasa oficial (TRM 3,341.23 vigente el 30-sep-2026, datos.gov.co; SBS venta 3.45 del 29-sep-2026, BCRP). Ticket $53.87 y $57.97. Recaudo digital $17.6M al mes, $211.3M al año.

| Palanca | Métrica | Conservador | Optimista | Promedio |
|---|---|---|---|---|
| L1 Pagos en Colombia | +1% a +2% de pagos digitales completados | $1.94M | $3.88M | $2.91M |
| L2 Pagos en Perú | +1% a +2% | $174K | $348K | $261K |
| L3 Costo por transacción | 5 a 10 bps sobre $211M | $106K | $211K | $158K |
| L4 Integraciones | 6 a 1 (2 nuevas de tarjeta, 4 actuales) | $25K | $44K | $34K |
| Total | | $2.24M | $4.48M | $3.36M |

- L4: 8 a 12 semanas de ingeniería por integración, mantenimiento de 20% a 30% anual, $50K por persona al año (mismos supuestos del deck de Cruz Verde).
- Todos los rangos de mejora son supuestos de modelación de Yuno y el deck lo dice así. No hay dato del cliente sobre pagos fallidos, tarifas ni costo de ingeniería.
- **Ojo:** L1 y L2 son recaudo que entra a tiempo, no ahorro (el deck lo aclara). El ahorro duro (L3 + L4) es de $131K a $255K al año contra un costo de Yuno de $393K. El caso lo sostiene la palanca de pagos completados; conviene pedirle a Luis la tasa de pagos fallidos o abandonados en el portal.
- No se cuantificó la migración de físico a digital: sin su costo por recaudo en cada canal no hay cómo afirmar un ahorro (un porcentaje sobre COP 180,000 puede costar más que una tarifa fija de punto físico).
- Moneda: todo en dólares; los montos en pesos y soles no aparecen en el deck, solo las tasas de cambio usadas.

## Métodos de pago (S16, slide nuevo)
Fuente: docs.y.uno/reference/payment-type-list, consultado el 30-sep-2026.
- Colombia: Nequi, Daviplata, PSE, Botón Bancolombia (Wompi), Bre-B QR (dLocal), Transfiya (Movii), tarjetas (Credibanco, Redeban, Wompi, PayU, ePayco), Efecty, Addi, Bancolombia BNPL, SU+ Pay, Apple Pay, Google Pay.
- Perú: Yape (Niubiz, dLocal, Bamboo), Plin (Niubiz), tarjetas (Niubiz, Izipay, Redeban Perú, Monnet), PagoEfectivo, SafetyPay, Cuotéalo BCP.
- **Dale no aparece en el catálogo público.** El slide dice "disponibilidad en validación con nuestro equipo de producto". Confirmar con Producto antes de enviar. Gana y Supergiros tampoco aparecen (no se mencionan en el slide).
- "Blink" en las notas de la llamada se interpretó como Plin.

## Cambios por slide vs Palco
- S1 y S22: lockup yuno | Eledé Línea Directa (logo oficial de elede.com.co en blanco; lineadirecta.com.co redirige a ese sitio). Título "IMPULSANDO PAGOS SIN FRICCIÓN PARA LÍNEA DIRECTA".
- S5: título, "UN EQUIPO DEDICADO PARA LÍNEA DIRECTA", "rieles locales de Colombia y Perú".
- S11: ventajas clave (una integración para los dos países, checkout alojado para tarjetas, contratos con proveedores siguen siendo suyos, subcuenta por país).
- S13, S14: business case. S16: métodos de pago (nuevo). S17: pricing.
- Sin cambios: S2 a S4, S6 a S10, S12, S15, S18 a S21.

## Inconsistencias en los datos del cliente (para preguntar, no corregidas en el deck)
- 80,000 por Wompi/PSE más 180,000 por Nequi suman 260,000, no 300,000.
- Nequi "55% del total" no cuadra con 180,000 de 300,000 digitales si lo digital es el 70%.
- No está claro si el 70/30 es por número de pagos o por valor, ni si incluye Perú.

## Pricing v2 (30-sep, tarde): fee de plataforma + compromiso mínimo
Instrucción de German: platform fee de $7,500 más un compromiso de $7,500 en volumen transaccional, presentado como facturación mínima mensual de $15,000. Aplicado con build/fix2_commitment.py (solo toca el slide de pricing).

| Concepto | Precio | A 325,000 tx exitosas |
|---|---|---|
| Fee de plataforma | $7,500 / mes | $7,500 |
| Tramo 1: 0 a 150,000 | $0.06 / tx | $9,000 |
| Tramo 2: más de 150,000 | $0.05 / tx | $8,750 |
| Compromiso mínimo en transacciones | $7,500 / mes | cubierto |
| **Total** | | **$25,250 / mes ($303,000 / año), $0.078 por tx, 14.3 bps** |

- El compromiso de $7,500 equivale a 125,000 transacciones exitosas al mes a $0.06 (cae completo dentro del tramo 1). Si el mes cierra por debajo, se factura la diferencia.
- Facturación mínima mensual: $15,000. A 400,000 tx: $7,500 + $21,500 = $29,000 ($0.0725 por tx).
- Con su volumen actual (325,000) el compromiso se cubre 2.6 veces; solo aplica si caen por debajo de 125,000.
- Contra la Pricing Policy: es la estructura preferida (fee fija + MMG aditivo). Platform $7,500 queda por debajo del list de V3 ($10,000) y por encima del mínimo; facturar platform y MMG mensual en vez de anual anticipado va por zona amarilla. Validar en el calculator y Salesforce.

**Estado del deck tras ediciones de German a mano (30-sep, tarde): 20 slides.** Quitó la sección de Business Case (divisor, palancas e impacto total). Agenda: 01 ¿Por qué Yuno?, 02 Conexiones en Colombia y Perú, 03 Propuesta. El slide de métodos es el 13 y el de pricing el 15. La sección "Business case (S13 y S14)" de arriba queda como referencia; ya no está en el deck.
