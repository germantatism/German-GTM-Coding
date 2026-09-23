# FlightHub · pricing v3 (post call 23-sep-2026, propuesta de estructura para confirmar)

## Lo que pidió Anna-Lena en la call (22 min, Sean y Joaquin presentes, Nick no asistió)
- Tiers por bucket, no tranches: "if we reach the highest tier, that cost applies to all volume" (10:27).
- Fee fija lo más baja posible: "a fixed monthly bill of 10,000 is a huge impact... our preference is a lower or non existent monthly flat fee" (15:16). El mínimo de $20K le pareció "a pretty steep price per month".
- Industria de márgenes extremadamente bajos; lo lleva a Nick y "run some numbers".
- Alternativa: build in-house. "The integrations are not the pain point anymore... the one thing that was interesting is the smart routing for acquiring" (17:02). No han dimensionado el costo del build; tener la comparación les ayuda.
- Equipo real: integración 1.5 personas, mantenimiento ella, reconciliación el equipo de accounting (NetSuite, "fairly manual").
- Network tokens opcionales: pueden seguir pasando PAN. Alertas de chargeback: si no las usan, no se cobran. Corto plazo 7 procesadores; entidad australiana nueva.

## Decisiones de German (notas post call)
Platform fee se mantiene en $10K · quitar el minimum monthly billing · tiers por bucket con precio ~10% menor a sus volúmenes · recon plana $7,500/mes · 3 años "happy to discuss" · build vs buy como sección para comentarios.

## Estructura propuesta (rate por bucket aplicado a TODO el volumen del mes)
| Successful trx / month | Rate |
|---|---|
| 0 to 200,000 | $0.08 |
| 200,001 to 400,000 | $0.06 |
| 400,001 to 600,000 | $0.04 |
| 600,001 to 799,999 | $0.035 |
| 800,000 and above | $0.03 |

Platform fee $10,000/mes flat. Sin mínimo mensual. Reconciliation $7,500/mes plana. Network tokens $0.05 creado / $0.01 update, opcionales. Alertas $15 por matched alert, opcionales (sin uso, sin cobro). 3 años, abierto a discutir.

## Antes vs ahora (platform + transacciones, sin add-ons)
| Volumen | Antes (tranches + mín $20K) | Ahora | Delta | Por trx |
|---|---|---|---|---|
| 500,000 | $33,000 | $30,000 | -9.1% | $0.060 |
| 600,000 | $36,000 | $34,000 | -5.6% | $0.057 |
| 700,000 | $38,000 | $34,500 | -9.2% | $0.049 |
| 800,000 | $40,000 | $34,000 | -15.0% | $0.043 |
| Año a 700K | $456,000 | $414,000 | -9.2% | |
| Año estacional (4×500K, 6×700K, 2×800K) | $440,000 | $395,000 | -10.2% | |

Quirk de los tiers por bucket (ella lo pidió así): al cruzar un límite la factura baja. 600,000 paga $34,000 y 600,001 paga $31,000; 799,999 paga $38,000 y 800,000 paga $34,000.

## Policy (interno)
- Recon plana $7,500: piso de la policy = $1,500 + $0.0085/trx → $5,750 a 500K, $7,450 a 700K, $8,300 a 800K. A 700K está justo en el piso (amarillo); a 800K queda debajo (rojo). Fórmula anterior daba $17,500 a 700K.
- Network tokens $0.05/$0.01 siguen bajo mínimo ($0.20/$0.04): rojo, CFO + CRO.
- Tiers de pay-in: todos sobre el piso de $0.01. Platform fee $10K = list V3. Sin MMG.
