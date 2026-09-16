# Propuesta comercial Palco + Yuno v1 (2026-09-16)

Google Slides: https://docs.google.com/presentation/d/1hWX6sNKKPpXhDSKGlZzrHWyKWMx5WlVxBeScEL_J7UY/edit (carpeta Drive "Palco")
Base: deck "Proposal - AppMaking + Yuno", 18 slides, todo en español. Slide 13 = propuesta. Para la reunión del lunes 21-sep 11:00 COT (Patricio, Fernando, Alfonso, Miguel tentativo).

## Fuente de los números
Hoja "Yuno — Pricing Matrix & Deal Calculator" (1Shux23cA23PBCcAlyhAiNrzXgzU6lbtQsLxUHgQ5NH8, pestaña Deal Calculator): 235,000 tx/mes, AOV $37.09, V3 / F3, ladder de 3 tramos (58,750 / 117,500 / 235,000). Precios Suggested: platform fee $10,000, 3DS $0.0403 (100,000 intentos/mes), Fraud Engine $0.0184 (20,000 evaluaciones/mes), Risk conditions $0.0139 (sin volumen). Tarifas de pagos dadas por German: $0.08 / $0.06 / $0.05 (la hoja sugería $0.0678 / $0.0514 / $0.0415).

## Estructura en el slide
| Tramo | Tx exitosas / mes | Plataforma | Por tx | All-in al tope |
|---|---|---|---|---|
| 1 | 0 a 58,750 | $10,000 | $0.08 | $14,700 |
| 2 | 58,751 a 117,500 | $10,000 | $0.06 | $18,225 |
| 3 | más de 117,500 (mostrado a 235,000) | $10,000 | $0.05 | $24,100 |

Ejemplo a 235,000: 58,750 × 0.08 = $4,700; 58,750 × 0.06 = $3,525; 117,500 × 0.05 = $5,875; total tramos $14,100 + plataforma $10,000 = $24,100/mes ($0.103 por tx). Pagos al año: $289,200.

Seguridad y riesgo (cotizado a precio Suggested): 3DS $0.0403 por autenticación ($4,030 a 100,000), motor antifraude $0.0184 por evaluación ($368 a 20,000), risk conditions $0.0139 por transacción evaluada (según uso). Total mensual estimado con 3DS y antifraude: $28,498 ($0.121 por tx).

Pendientes de revisión: conciliación, network tokens, token vault. Incluidos: KAM y TAM, +1,000 métodos, +450 proveedores, +50 conexiones antifraude, orquestación y reglas, smart routing y reintentos, monitores y alertas, reportes y dashboard, subcuentas por cliente. Pie: contrato a 3 años.

## Decisiones tomadas que German debe validar
1. Modelo ladder (cada tramo a su tarifa), como está activo en la hoja. Alternativa cliff (la tarifa del tramo aplica a todo el mes, como en Appmaking): a 235,000 sería 235,000 × 0.05 + 10,000 = $21,750/mes.
2. Se cobra solo sobre transacciones exitosas (convención del deck de Appmaking). Palco aprueba ~71%: si las 235,000 son intentos, las exitosas son ~167,000 y el total baja a ~$20,700/mes.
3. 3DS, fraud engine y risk conditions van cotizados a precio Suggested, no incluidos sin costo. "Les vamos a dar" se interpretó como "cotizar". Si es "incluir", cambia el slide.
4. Contrato a 3 años copiado del deck de Appmaking.
5. Ventajas clave (slide 11) adaptadas a Palco: una sola integración por país, cuentas y contratos de sus clientes siguen siendo suyos, monitores con redistribución automática, subcuentas por cliente con reportes.
6. Teléfono del cierre corregido a +1 786 238 4554 (el deck de Appmaking decía 787).
7. Los volúmenes de 235,000 tx y $37.09 son los de Patricio (2-sep) y siguen sin reconciliar (ticket vs orden).
