# Cruz Verde Colombia: recomendación de pricing (24-sep-2026)

## Perfil (Gong 21-may-2026 + dato de German 24-sep)
- 100,000 tx exitosas/mes, ticket promedio USD 20 (German). En la call de mayo dijeron COP 130,000 y a la baja, 40% de las tx por debajo de COP 30,000; 80K por Mercado Pago + 20K en efectivo.
- TPV ≈ USD 2.0M/mes, USD 24M/año.
- Stack: Mercado Pago único (incluye links de pago para puntos de venta). PSE = 58% de las ventas.
- Dolores: dependencia de un solo proveedor, caídas de PSE, rechazos altos con fraude bajo, devoluciones PSE.
- Pidieron: métodos nuevos, smart routing, modelo de pricing, demo técnica; NDA en curso. Objeción declarada: un costo por transacción en USD puede subirles el gasto porque el ticket cae.
- Contacto: Andrés Guzmán Forero (Ecommerce Manager). Yuno: Susana Awad, Alejandro Bernal, Saman Mortazavi, Carlos Medina.

## Segmento (Pricing Policy)
- Size V3 (100K a 1M tx/mes), justo en el borde con V2. Dimensionar por la oportunidad: los 20K en efectivo y los links de POS son upside.
- Margen M2 (retail). Misma celda que Palco (V3 × M2), cuyo calculator dio: platform sugerido $10,000 (green hasta $6,325); pay-ins sugerido $0.0678 / $0.0514 / $0.0415 por tramos 25% / 25% / 50% (green hasta $0.026 / $0.0227 / $0.0204).

## Recomendación de apertura (todo GREEN, auto-aprobación)
| Concepto | Precio | A 100,000 tx |
|---|---|---|
| Platform fee | $7,000 / mes | $7,000 |
| Pay-ins, tramo 1 (0 a 25,000) | $0.06 por tx exitosa | $1,500 |
| Pay-ins, tramo 2 (25,001 a 50,000) | $0.05 | $1,250 |
| Pay-ins, tramo 3 (más de 50,000) | $0.04 | $2,000 |
| **Total** | | **$11,750 / mes ≈ $141,000 / año** |

- Blended pay-ins $0.0475 por tx; all-in $0.1175 por tx = 59 bps del TPV.
- Contra el calculator: pay-ins a 100K sugeridos $5,055 vs $4,750 propuestos (dentro de green); platform $7,000 vs $10,000 sugerido (green hasta $6,325).
- Alternativa más simple: $7,000 + $0.05 flat = $12,000/mes. Los tramos cuentan mejor la historia ("pagas menos en tu volumen alto") y absorben el crecimiento.

## Piso de negociación (sigue green y no baja de $10K/mes de deal size)
- $6,500 + $0.045 / $0.04 / $0.035 → $10,375/mes. O $6,500 + $0.04 flat → $10,500/mes.
- No bajar de ahí: el deal size mínimo de la policy es $10K y el ladder de Palco/Appmaking nunca se acercó al piso verde.

## Cómo responder a "el costo en USD por tx nos sube el gasto"
1. Tramos: el precio por tx cae con el volumen; a 150K el blended baja a $0.045 y a 200K a $0.0438.
2. Facturar en COP a tasa oficial del Banco de la República (pricing USD / billing LC, permitido). Si insisten, LC/LC es excepción permitida para Colombia (revisión yellow).
3. Alternativa de precio: 0.25% del TPV en lugar de $ por tx (≈ $5,000/mes hoy, equivalente). Protege al cliente si el ticket sigue cayendo; para Yuno rinde menos con ticket bajo (a ticket $10 = $0.025/tx, sigue sobre el piso de $0.01). Usar solo si la objeción bloquea.
4. Ramp: crédito sobre la platform fee (nunca sobre pay-ins): 50% los primeros 3 meses = 1.5 meses de crédito, dentro del límite de 3 meses sin sign-off.

## Fuera de la cotización de apertura
- Risk conditions bundled en la platform fee ($0): fraude bajo, no lo van a valorar.
- 3DS: no aplica a PSE; si lo quieren para tarjeta, cobrar por intento ($0.04 sugerido en V3).
- Reconciliation: hoy un solo proveedor; cuando tengan 2+ conexiones PSE la van a necesitar (list $2,500/mes + $0.03; pack 50K $1,500 + $0.032).
- Subscriptions y Nova: no aplican.

## Reglas
- Salesforce antes de cotizar (fundamental 1). Minimum price nunca customer-facing.
- Confirmar el ticket real ($20 vs COP 130,000 de mayo) antes de fijar el business case.
