# Revisión de la propuesta Palco + Yuno (2026-09-18)

Deck revisado: https://docs.google.com/presentation/d/1hWX6sNKKPpXhDSKGlZzrHWyKWMx5WlVxBeScEL_J7UY/edit (21 slides, export PDF del 18-sep en scratchpad, texto completo vía conector Drive).
Contrastado con: correo de Patricio del 2-sep (data + 6 preguntas), transcript del deep dive 15-sep, resumen del deal 16-sep, hoja "Yuno — Palco Pricing Calculator" (1Shux23cA23PBCcAlyhAiNrzXgzU6lbtQsLxUHgQ5NH8) y QA del 16-sep.
Por instrucción de German: el TPV LTM de ~$457M se ignora. La base del business case sigue siendo 235,000 transacciones al mes × $37.09.

⚠️ El token del Slides API sigue muerto (proyecto GCP 304613953104 borrado; el MCP gdrive usa el mismo proyecto). Nada de esto se aplicó al deck. Script listo en `build/fix_review_0918.py`; requiere correr antes `python3 Deals/Appmaking/build/auth_slides.py <client_secret.json>` con un OAuth client nuevo.

## 0. Veredicto

1. La aritmética del business case y del pricing cuadra al 100% con la base 235,000 × $37.09 y con las tasas de la tabla de Patricio. El pricing sigue GREEN en el calculator, salvo Risk conditions.
2. Lo que no cuadra es de alineación, no de números: el deck no responde las 6 preguntas escritas de Patricio, propone "contrato a 3 años" cuando desde el 30-jul se habla de piloto, y no contesta la objeción central de Alfonso (que el ahorro por ruteo compense el costo). Con los números del propio deck, el ruteo NO compensa: la palanca 3 vale $59K a $99K al año contra $281K de costo. Lo que compensa es la aprobación (18 a 36 veces el costo), y eso hay que decirlo en el slide de pricing.
3. Tres afirmaciones chocan con la data que ellos mandaron: "Palco procesa cerca de $104.6M al año" (Patricio dijo ~$28.3M al mes), "3DS a 100,000 autenticaciones" (Patricio dijo 3DS obligatorio en todos los flujos de tarjeta) y "235,000 transacciones exitosas ... según lo compartido por Palco" (Patricio nunca dijo "exitosas").
4. Risk conditions a $0.04 está por encima incluso del precio de lista de la política ($0.02); el sugerido es $0.0139.
5. Hay dos preguntas que cambian el tamaño del caso 3x y nadie ha hecho: si $37.09 es por boleto o por transacción, y si las 235,000 son aprobadas o intentos. Hacerlas antes del lunes.

## 1. Aritmética verificada (todo cuadra)

Base: 235,000 × $37.09 = $8,716,150/mes = $104,593,800/año.

| Palanca | Cómo se calculó | Conservador | Optimista | Deck |
|---|---|---|---|---|
| L1 aprobación | Cohorte MP v2 + Openpay + Banorte + Santander + Cybersource + Stripe + Bancard: 1,952,600 intentos/año, 62.4% aprobación, 55.7% de las aprobadas de su tabla → 130,900 aprobadas/mes, 209,800 intentos/mes; +5 pp = 10,490 tx/mes, +10 pp = 20,980 | $4.67M | $9.34M | $4.7M / $9.3M ✓ |
| L2 failover | Fiserv 43.7% + Pixel Pay 52.3% = 47.6%, 1.9% de las aprobadas → 4,500 aprobadas/mes, 9,454 intentos; a 60% y 68% | $0.52M | $0.86M | ✓ |
| L3 MDR | 7.5 a 12.5 bps sobre 75.7% × $104.6M = $79.2M | $59K | $99K | ✓ |
| L4 run-ops | 3 a 4 FTE | $230K | $360K | ✓ |
| Total | | $5.48M | $10.66M | $5.5M / $10.7M ✓ |

Promedios $7.0M / $0.69M / $79K / $295K / $8.1M ✓. GTV recuperado $7.7M (rango $5.2M a $10.2M) ✓.

Pricing S16: tramos 58,750 × 0.06 + 58,750 × 0.055 + 117,500 × 0.045 = $12,044 ✓; + $7,000 = $19,044 ($228,525/año) ✓; 3DS 100,000 × 0.04 = $4,000 ✓; antifraude 20,000 × 0.018 = $360 ✓; total $23,404 ($280,845/año) ✓; $0.081 y $0.100 por tx ✓; a 300,000: $21,969 ≈ $0.073 ✓.

Calculator (Deal Calculator, 235,000 tx, AOV $37.09, V3/F3): plataforma sugerido $10,000, green hasta $6,325 → $7,000 GREEN. Pay-ins sugerido $0.0678 / $0.0514 / $0.0415, green hasta $0.026 / $0.0227 / $0.0204 → $0.06 / $0.055 / $0.045 GREEN. 3DS sugerido $0.0403 (green hasta $0.0284) → $0.04 GREEN. Fraud Engine sugerido $0.0184 (green hasta $0.0113) → $0.018 GREEN. **Risk conditions: sugerido $0.0139, lista de política $0.0200, piso $0.0070 → $0.04 está 2x por encima de la lista.** Score a precios sugeridos 87.7 GREEN, take rate 31.3 bps; a los precios del deck queda GREEN.

## 2. Bloqueantes de alineación (ordenados por impacto)

### B1. El deck no responde lo que Patricio pidió por escrito
Las 6 preguntas del 2-sep son la agenda real y ninguna tiene respuesta explícita en el deck (German quitó los slides de contexto). Tampoco aparecen los pedidos del 15-sep: credenciales por API, split fee/ticket, panel en tiempo real para on-sales, fallback con redirección. Patricio abre el deck buscando sus preguntas.

Propuesta: un slide nuevo entre S11 y el divisor de Business Case, "Lo que nos pidieron y cómo lo cubrimos", dos columnas (pedido → respuesta), con estado honesto:

| Pedido (Patricio 2-sep / call 15-sep) | Respuesta | Estado |
|---|---|---|
| 1. Split de comisión en México al momento del cobro, tenant MoR y Palco retiene su fee | Split Marketplace en la petición de pago: Yuno propaga la instrucción y el procesador dispersa. Sellers y onboarding por API. | ⚠ Por confirmar qué procesadores mexicanos lo soportan en esa dirección (Carlos) |
| 2. 3DS obligatorio en todos los flujos y su impacto con el ruteo | 3DS como condición de ruteo (monto, BIN, riesgo, metadata), exenciones donde apliquen y reintento por otra ruta si la autenticación falla. | ✓ Impacto se mide en el piloto con su baseline |
| 3. Tokenización y recurrencia para abonos con procesadores mexicanos | Bóveda PCI de Yuno + gestión de suscripciones multi-procesador; network tokens cotizados aparte. | ⚠ Recurrencia con Openpay / Banorte / Santander por confirmar (Carlos) |
| 4. Modelo comercial multi-tenant: contratación y factura por tenant | Cuenta Palco + subcuentas por cliente (routing, credenciales y checkout propios). Un solo contrato y una sola factura a Palco; tramos sobre el volumen agregado. Palco decide si absorbe o traslada. | ✓ |
| 5. API directa vs SDK y alcance PCI | Ambas. SDK: la captura de tarjeta la soporta Yuno, sin PCI para Palco. API directa: PAN en su front → PCI DSS a cargo de Palco. Alfonso: 90% SDK. | ✓ |
| 6. Ruteo por BIN para preventas bancarias | Condición nativa de ruteo por BIN, país, monto, installments, CVV y metadata ilimitada. | ✓ Mostrado el 15-sep |
| Credenciales cargadas por API (sus clientes se autoconfiguran) | Organization API: GET catálogo + POST conexión. | ✓ |
| Panel en tiempo real para on-sales | Insights por cuenta: volumen, aprobación por proveedor, por condición, primer intento vs reintento. Monitores con redistribución automática. | ✓ |
| Fallback en métodos con redirección | Solo si falla la creación de la redirección; un rechazo post-redirección exige nueva compra. | ⚠ Limitación, decirla |

Las tres ⚠ son las pendientes de Carlos desde el 15-sep. Si Carlos las confirma antes del lunes, pasan a ✓.

### B2. "Contrato a 3 años" contra el piloto que ellos pidieron
Desde el 31-jul Magdalena escribió "preparar una propuesta para el piloto que discutimos". El business case dice "a validar en piloto" tres veces, y el deck no define ningún piloto. El pie "Contrato a 3 años" viene del deck de Appmaking y nunca se habló de plazo con Palco. Alfonso además dijo que a los partners actuales "es muy difícil cambiarles"; un compromiso de 3 años sin piloto es la excusa perfecta para no avanzar.

Propuesta: reemplazar el pie por un bloque "Piloto México":
- Alcance: 3 a 5 tenants mexicanos sobre Openpay, Banorte y Santander, vía subcuentas y SDK.
- Baseline: su propia tabla (58.0%, 59.6%, 56.1%).
- KPI: aprobación de la cohorte y GTV recuperado a $37.09; revisión a 90 días.
- Condición comercial (decisión de German): fee de plataforma reducido durante el piloto, por ejemplo 50% por 3 meses. Equivale a 1.5 meses de crédito, dentro del límite de 3 meses que el calculator permite sin sign-off.
- Plazo del contrato: se define al cierre del piloto, no antes.

### B3. La objeción de Alfonso sigue sin respuesta y los números del deck la contradicen
Alfonso dijo dos veces: el costo se traslada al cliente final, sus clientes eligen pasarela por precio, y "esperamos que el ahorro por ruteo compense". En el deck, la palanca 3 (ruteo de menor costo) vale $59K a $99K al año, 7.5 a 12.5 bps. Yuno cuesta $280,845 al año, 27 bps sobre un ticket de $37.09 (22 bps solo pagos). Si Alfonso hace esa resta en la reunión, pierde el deck.

Lo que sí compensa es la aprobación, y no está dicho en ningún slide en términos de costo:
- GTV recuperado (palancas 1 y 2): $5.2M conservador, $10.2M optimista, contra $281K de costo → 18x a 36x.
- Para un tenant de la cohorte, +5 pp sobre 62.4% son 8% más ventas aprobadas; +10 pp son 16%. Eso contra 27 bps de costo por transacción.
- Para Palco: la palanca 4 ($230K a $360K) cubre entre 82% y 128% del costo anual por sí sola.

Propuesta: en S16, debajo de "≈ $0.081 ... ≈ $0.100", añadir "27 bps sobre un ticket de $37.09"; y en S14, en las tarjetas, "18 a 36 veces el costo anual de Yuno" y "cubre entre 82% y 128% del costo anual de Yuno ($281K)". Textos exactos en el script.

### B4. 3DS a 100,000 autenticaciones contra "3DS obligatorio en todos los flujos"
Patricio escribió que el 3DS es obligatorio en todos los flujos de tarjeta. Solo la cohorte de la palanca 1 son 210,000 intentos al mes; los intentos de tarjeta totales rondan 250,000. A $0.04, el 3DS a volumen completo cuesta $8,400 a $10,000 al mes, no $4,000, y el total sube a $27,400 a $29,400 al mes.

Dos salidas: (a) etiquetar los 100,000 como 3DS selectivo o dinámico (cerca del 40% de los intentos, solo donde sube la aprobación), que conecta con la palanca 1 y con las exenciones por riesgo; o (b) presentar el 3DS a volumen completo. Recomiendo (a) y decir en el slide cuánto sería (b). El script aplica (a) con la cifra de (b) en la nota.

### B5. Risk conditions a $0.04
Está por encima de la lista de política ($0.02) y es casi 3x el sugerido ($0.0139). Además es más caro que el 3DS ($0.04) y que el motor antifraude ($0.018), y Alfonso preguntó específicamente por scoring y costo. Cambiar a $0.014 (consistente con el redondeo de 3DS 0.0403 → 0.04 y antifraude 0.0184 → 0.018). El script lo corrige.

### B6. "Palco procesa cerca de $104.6M al año" contradice su propia data
Patricio reportó ~$28.3M al mes, $211M al año solo en México y $346M en tarjeta. Que el deck afirme "Palco procesa cerca de $104.6M al año" (S13) y "$79M de TPV en tarjeta" (S13 y S14) le va a saltar a Patricio en la primera línea. El número no cambia (regla de German); cambia la frase: "la base de modelación es de $104.6M al año" en lugar de "Palco procesa". Mismo tratamiento para "$79M de TPV en tarjeta". El script lo aplica. Recomendación adicional: Supuestos de S14 dice "a validar en el piloto"; añadir "si $37.09 corresponde al boleto y no a la transacción, el GTV recuperado escala en la misma proporción" (opcional, decidir German).

### B7. "235,000 transacciones exitosas ... según lo compartido por Palco"
Patricio escribió "Volumen mensual promedio: ~235,000 transacciones", sin "exitosas". En el pricing, cobrar solo sobre exitosas con 235,000 como base es conservador para Palco (si incluye intentos, el costo baja). En el business case, atribuirle "exitosas" a Palco es inexacto. El script cambia S13 y S14 a "235,000 transacciones al mes (reportadas por Palco, tratadas como aprobadas)". S16 conserva "exitosas" porque es la base de facturación.

## 3. Ajustes menores (texto y consistencia)

| # | Slide | Hoy | Cambio | Por qué |
|---|---|---|---|---|
| M1 | S13 palanca 4 | "Una sola integración reemplaza el mantenimiento de sus 50+ integraciones" | "libera a su equipo del mantenimiento de sus 50+ integraciones" | Alfonso construyó esas integraciones; "reemplaza" es la palabra prohibida |
| M2 | S13 cierre | "time to market esperado es de 4 a 6 semanas" | "se mide en semanas, no meses" (o confirmar 4 a 6 con Carlos) | Nadie lo validó |
| M3 | S16 "Qué cubre" | "Herramientas antifraude +50" junto a "Motor antifraude $0.018" | "Conexiones antifraude +50" | Confunde incluido vs cobrado |
| M4 | S16 caja blanca | "Sin fee de setup. Cada tramo se cobra a su tarifa dentro del mes. Las transacciones declinadas no se cobran." | "Sin fee de setup. Un solo contrato y una sola factura a Palco; los tramos se calculan sobre el volumen agregado de todas sus subcuentas. Las declinadas no se cobran." | Responde la pregunta 4 y la de Alfonso ("si agrupamos todos, ¿mejor tasa?") |
| M5 | S18 apéndice | "Acceso a 300+ métodos" | "1,000+ métodos" | S4 y S6 dicen 1,000+ |
| M6 | S6, S7, S19 | Conciliación como producto vivo ("Un solo libro contable", "reducida de semanas a horas") | Marcar "(roadmap)" en S6 y S7; S19 → "Visibilidad unificada en tiempo real entre proveedores" | Regla vigente: conciliación no es GA; S16 ya la deja "pendiente" |
| M7 | S21 cierre | Lockup "yuno \| PALCO" cortado por el borde derecho, tagline ilegible | Mover el lockup a la izquierda; usar solo el wordmark (build/logo_url.txt) | Pendiente desde el QA del 16-sep |
| M8 | S13 palanca 1 KPI | "62.4% → 67.4%" | "62.4% → 67.4% / 72.4%" solo si cabe en el ancho de la tarjeta | Muestra solo el conservador |
| M9 | S16 pendientes | "Pendiente de revisión: conciliación, network tokens y token vault." | "network tokens, token vault y conciliación (en roadmap)" | Consistencia con M6 |
| M10 | S5 | "Con la confianza de Uber, Qatar Airways, Rappi y GoFundMe" | Dejar el nombre; NO describir el setup de marketplace de GoFundMe sin permiso | Regla del deal GoFundMe |

Lo que ya está bien y no tocar: S11 "Las cuentas y contratos de sus clientes siguen siendo suyos" (responde al modelo de Alfonso); S13 "Es la única palanca que cae directo en el P&L de Palco"; S14 "Palco captura su fee de plataforma sobre ese volumen"; L2 excluye Line VE con razón explícita; sin fee de setup; cobro solo sobre aprobadas.

## 4. Preguntas antes del lunes

A Fernando (correo corto o WhatsApp, jueves o viernes):
1. ¿$37.09 es el ticket promedio por boleto o por transacción? Su tabla mensual por país da $120 por transacción ($28.3M / 235,000), unos 3 boletos por compra. Si es por boleto, todo el GTV recuperado se multiplica por 3 y el costo de Yuno baja de 27 bps a unos 8 bps sobre la transacción. Es la pregunta que más cambia el caso.
2. ¿Las 235,000 transacciones mensuales son aprobadas o intentos, y cuántas son tarjeta? Define la base de facturación y el volumen de 3DS.
3. ¿El 3DS en todos los flujos es exigencia de sus adquirentes, de sus tenants o decisión de Palco? Si es decisión propia, el 3DS selectivo es la palanca más barata que tienen.

A Carlos (Slack, hoy):
4. Conectores en catálogo para Openpay, Banorte, Santander, Mercado Pago, Redsys, Cybersource, Authorize.net y Fiserv. Sin Openpay, Banorte y Santander la palanca 1 no existe; sin ruta alterna en UY y HN la palanca 2 tampoco. Ausencias probables: Line VE, Pixel Pay HN, Recurrente GT, Bancard PY, UepaPay DR, ECI ES.
5. Split al capturar con tenant MoR por procesador mexicano, y recurrencia con Openpay / Banorte / Santander.
6. Si 4 a 6 semanas de time to market es defendible con SDK y subcuentas.

## 5. Preparar la reunión

- "Dijiste 15K": en la call German dijo "alrededor de $15K como fee mínimo". La propuesta tiene fee fijo de $7,000 y el resto variable; en el primer tramo el mes completo son $10,525 y a su volumen actual $19,044 solo pagos ($23,404 con 3DS y antifraude). Está dentro del rango de $15K a $30K que Alfonso asumió. La respuesta: el mínimo bajó, lo demás crece con lo que procesen.
- "¿Cobran por transacción o por volumen de dinero?" (Alfonso): por transacción aprobada, no por monto. Si la orden real es de ~$120, el costo por orden queda en ~8 bps; conviene decirlo solo después de que respondan la pregunta 1.
- Dos modelos (white label vs solo conexión): el correo del 15-sep dice "solución directa para sus clientes actuales" y el deck presenta un solo precio. Decir en S16 que el precio es el mismo si la cuenta del procesador es del cliente o de Palco (recintos grandes y clubes, el caso que Alfonso quiere para clientes nuevos). Pendiente de que German lo confirme.
- Referencia GoFundMe para split: solo con permiso.

## 6. Cómo aplicar

1. Re-autenticar Slides: crear OAuth client (Desktop) en un proyecto GCP con Slides API habilitado y correr `python3 Deals/Appmaking/build/auth_slides.py <client_secret.json>`.
2. `python3 Deals/Palco/build/fix_review_0918.py dry` muestra qué encuentra sin tocar el deck.
3. `python3 Deals/Palco/build/fix_review_0918.py` aplica B3 a B7, M1 a M7 y M9, y baja thumbnails de S13, S14, S16 y S21 a build/ para verificar desbordes.
4. B1 (slide de preguntas) y B2 (bloque piloto) se construyen a mano o con Claude Design con los textos de arriba; el script no crea slides nuevos.
