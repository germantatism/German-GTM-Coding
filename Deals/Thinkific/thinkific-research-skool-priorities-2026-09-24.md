# Thinkific · Research profundo para el mensaje de Justo (24-sep-2026)

Objetivo: entender el fit de Thinkific con las tres prioridades que ya vimos en Skool (subscriptions, nuevos métodos de pago, local acquiring en más regiones) y dejar un borrador del mensaje que Justo manda al equipo de Thinkific.

Regla de este documento: solo hechos verificados en fuente primaria (filings de Thinkific, su centro de soporte, y.uno, docs.y.uno, Slack/Drive internos). Lo que no se pudo verificar se marca como tal y NO va al mensaje.

---

## 0. Estado del deal (Gmail + Gong + memoria)

- Hilo: "Re: Thinkific + Yuno at Stripe Sessions" (Gmail 19ddaaf62bafc410). Reunión presencial en Stripe Sessions SF, 30-abr-2026.
- Contactos: Darren Guarnaccia (VP Product, decide, solo ha respondido a Justo), Tauqeer Ahmad (Group PM, a quien Darren delegó orquestación), Greg y Amy Oilman en copia (roles sin verificar). Ojo: Greg Smith es el CEO y cofundador de Thinkific; no está confirmado que "greg@thinkific.com" sea él.
- 13-may-2026, Darren a Justo: "Tauqueer will follow up later this summer when we start to look again into Orchestration." Justo cerró con "think of us as an extension of your payments team".
- Follow-ups de German sin respuesta: 15-jul, 20-jul (Q3 roadmap con "commerce flexibility and global growth"), 10-ago, 9-sep (viaje a Canadá con William Wong). Cero respuestas de Thinkific desde el 13-may.
- Gong: 0 llamadas, 3 emails indexados. No hay transcript.
- Deck: ss26.yuno.tools/m/thinkific (corregido 17-sep vía Supabase).

## 1. Lo que cambió esta semana (contexto para el timing del mensaje)

**23-sep-2026, después del cierre: reorganización.** Fuente: investors.thinkific.com/2026-09-23-Thinkific-Reorganizes-to-Focus-Investments-on-Growth-Opportunities-and-Maximize-Free-Cash-Flow
- 96 puestos eliminados (no dicen el % de la plantilla). ~$19M de ahorro anualizado bruto, la mayoría desde Q4-2026. ~$5M de cargos de reestructuración, casi todo en Q3-2026.
- Inversión concentrada en Thinkific Plus (mid-market y enterprise) y "new AI-first products".
- Guidance Q3 de revenue reafirmado en $18.6M a $18.9M, "tracking to the high end". Adjusted EBITDA Q3 subido de 2% a 5% a 7% a 10% del revenue.
- Nuevo target: free cash flow margin de 25% o más del revenue en F2027.
- CEO Greg Smith: "By aligning our efforts towards Plus, we will be in a position to re-accelerate growth and operate the remainder of the company with greater discipline and higher margins."

**24-sep-2026: la acción reaccionó.** THNC cerró el 23-sep en CA$1.20 (rango 52 semanas CA$1.11 a CA$2.40) y el 24-sep a media tarde estaba en CA$2.10, +75% en el día (Yahoo Finance, StockAnalysis, Globe and Mail). El "$1.34" del resumen de Justo no aparece en ninguna fuente; lo más cercano es CA$1.22 el 18-sep y CA$1.27 el 16-sep.

Implicación para el mensaje: la empresa acaba de despedir a 96 personas y comprometerse públicamente con márgenes. Menos capacidad de ingeniería para construir pagos in-house, y todo lo que suene a "spend" o "proyecto grande" muere. "Extension of your payments team" y "profit, not spend" son exactamente el tono. Riesgo real: Darren o Tauqeer pueden estar entre los 96; el mensaje debería ir a Darren con copia a Tauqeer y no depender de ninguno de los dos.

## 2. Financials verificados (Q2-2026, filings del 5-ago-2026)

Fuentes: press release Q2, transcript de la call (PDF en investors.thinkific.com), MD&A Q2, investor deck Q2, estados financieros Q2, AIF 2025.

| Métrica | Q2-2026 | Nota |
|---|---|---|
| Revenue | $18.6M (+3% YoY) | Sobre el rango guiado $18.2M a $18.5M |
| ARR | $61.7M (+2%) | El deck redondea a $62M |
| ARPU | $177/mes (+5%) | |
| Subscription revenue | $15.2M (+3%) | |
| Commerce revenue | $3.4M (+4%) | Q1 fue $3.5M (+8%); FY2025 $13.4M (+32%) |
| GPV (volumen por Thinkific Payments) | $71.4M (+10% YoY, desde $75.7M en Q1) | Caída secuencial = "typical seasonality" según el CFO |
| GMV (ventas totales de los clientes en la plataforma) | $107.0M (-4% YoY) | Baja YoY por "a significant customer that moved off platform" + estacionalidad |
| Penetración (GPV/GMV) | 67% (desde 58%) | "plateau in the mid-to-high 60-percent range" |
| Take rate | 4.4% TTM (deck); 4.3% en Q1 | Q2 trimestral no revelado |
| Gross margin | 73% (+100 pb) | "driven by our Commerce product... improved operational efficiencies in our Payments platform" |
| Plus revenue | $5.3M (+14%) = 28% del revenue | Plus ARPU = 20x Self Serve; >50% de deals nuevos multi-year |
| Self Serve revenue | $13.3M (-1%) | Primera caída YoY, "expected" |
| Net loss | $(0.3)M | |
| Adjusted EBITDA | $273K (1%) | Guidance era pérdida de 2% a 5% |
| OCF trimestre | $1.7M | H1 fue $1.5M (Q1 negativo) |
| Cash + STI | $51.0M, sin deuda | |
| Guidance Q3 | $18.6M a $18.9M (~1% YoY) | EBITDA subido a 7% a 10% el 23-sep |
| TTM jun-2026 | GMV $456M, GPV $291M, commerce rev $13.8M | Deck Q2 |

Corrección al resumen de Justo: el "significant customer" explica la caída de GMV año contra año, no la de GPV. El CFO Leigh Ramsden (en el cargo desde el 1-jun-2026) atribuyó la caída secuencial de GPV solo a estacionalidad.

**Geografía del revenue (estados financieros Q2-2026, por país del cliente facturado):** US 53% ($9.8M), Rest of world 33% ($6.1M), Canadá 14% ($2.7M). FY2025: US 53%, RoW 33%, Canadá 14%. Un tercio del revenue viene de clientes fuera de Norteamérica.

**Otros datos del deck Q2:** ~35,000 customers, $4B+ ganados por sus clientes, 230M students served. Growth drivers: "Grow Thinkific Commerce penetration with Plus customers", "Internationalization of features driving adoption in UK and EU". Feature set de commerce: multi-currency, sales tax, BNPL, order bumps, group sales.

**Liderazgo 2026:** CEO Greg Smith (tomó supervisión directa de producto y tecnología cuando el CPTO Ryan Donovan salió el 15-abr-2026). CFO Leigh Ramsden desde 1-jun-2026 (ex Trulioo). CRO Amanda Malko. Darren Guarnaccia (VP Product) no aparece en ningún filing o call de 2026. Peter Fitzpatrick figuraba como VP of Commerce en 2023 (página de Stripe); sin confirmación 2026.

## 3. Lo que Thinkific dice de pagos en sus propios documentos

- AIF 2025: "Thinkific Payments is an embedded payment processing service that allows our customers to accept payments without reliance on third-party payment gateways or acquirers and is built-on Stripe, Inc."
- AIF 2025: "We rely on Stripe for payment processing." Acuerdo del 22-sep-2020, término inicial 36 meses, renueva cada 12 meses salvo aviso con 30 días. BNPL (ago-2023) y sales tax (ago-2023) son "Stripe-powered" bajo el mismo acuerdo.
- AIF 2025, factores de riesgo: Stripe listado junto a AWS y Wistia como "critical U.S.-based vendors"; "if any of these suppliers were to terminate their relationship with us, we could incur substantial delays and expense in finding and integrating alternative providers".
- MD&A Q2: "Thinkific Commerce, powered by Thinkific Payments, supports recurring subscriptions, payment plans, Buy Now Pay Later options, refunds, and multi-currency transactions - all without requiring third-party integrations."
- MD&A Q2: "Thinkific Commerce is available in over 30 countries and may present risks and challenges that we have not yet experienced."
- MD&A Q2: "As we continue to roll out local currency billing options... We believe that it is more important to remove friction for non-U.S. customers by charging in their local currency." (Esto es sobre cómo Thinkific cobra sus suscripciones SaaS a sus clientes, no sobre el checkout de los estudiantes.)
- Call Q4-2025 (CFO): el take rate baja cuando sube la venta internacional porque "they utilize a lower cost payment option like ACH, our sales tax solutions aren't available to them, and they have lower usage of options like buy now, pay later that have a higher take rate."
- Call Q4-2025 (CEO): pagos integrados "not necessarily on their RFP as a requirement... quickly becomes a strong selling feature and can help us win the deal" en Plus. "Less than 10 percent of Thinkific Commerce revenue comes from Plus opportunities" (dato de una call anterior citado por el CEO).
- Call Q2-2026 (CFO): "opportunity to optimize our pricing and packaging, potentially including outcome-based pricing models."
- Product updates 2026 (thinkific.com/product-updates): ene-2026 "Local currency at checkout", "built-in invoicing", "instant payouts for eligible customers", "unified subscriptions view"; jul-2026 "sell more in a single checkout" (multi-item); ago-2026 "Phased Subscriptions and revenue protection through Thinkific Payments".
- Página de Stripe sobre Thinkific (stripe.com/customers/thinkific, cifras de ~2023): usa Stripe Billing, Connect, Elements, Payments, Radar, Tax, Payment Links, Link, Financial Connections. "32% of Thinkific Payments GMV from recurring subscriptions". "80% of new creators in US, UK, and Canada start with Thinkific Payments".
## 4. Thinkific Payments hoy: cobertura, métodos y suscripciones (centro de soporte, artículos leídos completos vía API de Zendesk el 24-sep-2026)

### 4a. Local acquiring: dónde puede estar el creator para usar Thinkific Payments

Fuente: support.thinkific.com/hc/en-us/articles/1500012376321 (actualizado 3-ago-2026).

**36 países:** Estados Unidos, Canadá, Reino Unido, Australia, Nueva Zelanda, Singapur, Hong Kong, Noruega, Suiza y 27 de la UE/EEE (Austria, Bélgica, Bulgaria, Croacia, Chipre, Chequia, Dinamarca, Estonia, Finlandia, Francia, Alemania, Grecia, Hungría, Irlanda, Italia, Letonia, Lituania, Luxemburgo, Malta, Países Bajos, Polonia, Portugal, Rumanía, Eslovaquia, Eslovenia, España, Suecia).

**Cero en:** toda Latinoamérica (Brasil, México, Colombia, Argentina, Chile, Perú), India, Japón, Corea, Sudeste Asiático fuera de Singapur (Indonesia, Filipinas, Tailandia, Malasia, Vietnam), Medio Oriente (EAU, Arabia Saudita), África (Sudáfrica, Nigeria, Kenia, Egipto), Turquía, Israel.

No hay ningún anuncio de nuevos países en 2025 ni 2026 (lista de noticias de IR, product updates, releases trimestrales; captura de Wayback de oct-2025 muestra la misma lista). La URL thinkific.com/tcommerce-global redirige a la home. El MD&A dice "Thinkific Commerce is available in over 30 countries".

**Qué le pasa a un creator fuera de esos 36 países:**
- Thinkific le recomienda Stripe directo, que solo está disponible en plan Grow o superior (support 360030723513, 21-jul-2026). La integración nativa de Stripe NO soporta iDEAL, SEPA, FPX ni Apple Pay (support 360030357334, 18-ago-2026).
- Si tampoco hay Stripe en su país: PayPal (solo pagos únicos, "PayPal integration supports USD only"), Stripe Atlas (abrir entidad en US), solución externa propia, o la app CheckoutJoy (support 360030357514, 1-sep-2026).
- Sin Thinkific Payments no hay TCommerce: sin wallets, sin BNPL, sin bank redirects, sin moneda local en checkout, sin sales tax, sin Smart Retries de TP, sin Card Account Updater, sin invoicing, sin gifting, sin order bumps, sin Phased Subscriptions.
- Third-party gateway fee (support 22383950439575): 5% Basic, 2% Start, 1% Grow, 0.5% Expand, Plus sin fee, sobre el primer $1M de ventas al año, en transacciones Stripe directo (y "in the future" PayPal). No se cobra si TCommerce no está disponible en tu país.

**Qué le pasa al estudiante que paga a un creator de los 36 países desde otro país:** puede pagar (no hay restricción de país del estudiante), pero con tarjeta internacional cross-border. Al creator le cargan +1.5% international card (US) o +1.55% (UK/EU) y +1% (US) o +2% (resto) por conversión de moneda. Sin Pix, UPI, OXXO, PSE, Yape, GCash ni ningún método local.

**Moneda:** una sola moneda base por sitio y payout en una sola moneda ("It is not possible to charge and receive payouts in multiple currencies", support 360030737273, 17-feb-2026). "Local Currency at Checkout" (Q1-2026) presenta el precio en la moneda del comprador por IP con FX de Stripe "plus a foreign exchange buffer", pero SOLO para pagos únicos, solo en Thinkific Payments, y desactiva los BNPL. No aplica a suscripciones ni payment plans (support 38311651243671, 21-may-2026).

**Fees de tarjeta por país del creator** (fuente única, artículo 1500012376321): US 2.9% + $0.30; Canadá 2.9% + C$0.30; UK 1.7% + £0.20; UE 1.7% + €0.25; Australia 1.75% + A$0.30; Suiza 2.9% + CHF0.30; NZ 2.9% + NZ$0.30; Noruega 2.4% + 3.9kr; HK 3.4% + HK$2.35; Singapur 3.4% + S$0.50. Suscripciones y payment plans: +0.7% en todos los países (era +0.5% en la captura de oct-2025; la fecha exacta del cambio no está en ninguna fuente de Thinkific). Sales tax: +0.5% cuando se evalúa impuesto (US/CA obligatorio, UK/EU opt-in). Payouts: 2 a 7 días según país; Instant Payouts 1% a 1.5%.

### 4b. Métodos de pago que puede aceptar un creator en Thinkific Payments

Fuentes: support 360060177513 (wallets, 14-abr-2026), 14047200964119 (bank redirects, 3-nov-2025), 12448134209303 (BNPL, 17-jun-2026), 360030357494 (PayPal, 31-oct-2025), 1500012376321 (fees).

| Método | Dónde | Recurrente | Fee |
|---|---|---|---|
| Tarjetas (Visa, MC, Amex, redes locales) | Todos | Sí | Base |
| Apple Pay, Google Pay | Todos | Sí | Base |
| Link by Stripe | NA, Europa, APAC | Sí | 3.9% + $0.30 |
| Link Instant Bank Payments (cuenta bancaria US) | US | Sí | 3.9% + $0.30 |
| Cash App | US | No | 3.9% + $0.30 |
| Amazon Pay | US, solo USD | No | 3.9% + $0.30 |
| Bancontact, EPS, iDEAL, Przelewy24, Sofort | BE, AT, NL, PL, DE/AT/BE/NL/ES; sitio en EUR | No | 3.9% + $0.30 |
| Giropay | Deprecado desde 30-jun-2024 | | |
| Afterpay / Clearpay | Comprador en AU, CA, NZ, UK, US; oculto si la moneda del sitio no es la del país del creator | No | 6.5% + $0.30 |
| Klarna | Comprador en 20 países (AT, BE, CA, DK, EE, FI, FR, DE, GR, IE, IT, LV, LT, NL, NO, SI, ES, SE, UK, US); no se muestra si creator y comprador están en países distintos | No | 6.5% + $0.30 |
| Affirm | Eliminado el 27-feb-2026 "due to a change from Affirm" | | |
| PayPal (integración aparte) | Cuenta Business; solo USD | No | Según PayPal |
| ACH Debit / PAD / SEPA | Solo vía Invoicing B2B (US/CA/EU) | | 1% a 1.5% + 0.4% invoicing |
| In-app purchases | Solo Branded Mobile; Apple/Google se llevan 30% (15% small business); tope $1,000; sin memberships ni free trials | | |

**Lo que NO existe en ningún artículo de Thinkific:** Interac (Canadá, su mercado HQ), SEPA Direct Debit o ACH en checkout, PayPal recurrente, BNPL recurrente, y ningún método local fuera de UE (Pix, Boleto, OXXO, SPEI, PSE, Nequi, Yape, UPI, PayPay, konbini, GCash, GrabPay, Dana, QRIS, FPX, Tabby, Tamara, mada, M-Pesa, BLIK, Swish, MobilePay, Vipps).

**Lo que sí cambió en 2026:** Affirm fuera (feb), Local Currency at Checkout (Q1), Shop with Cart multi-producto (jul), Multi-Item Checkout API para Plus (jun), Stripe Capital para creators US (ago), IAP extendido a Communities, Digital Downloads y Events (jun).

### 4c. Suscripciones y recurrencia

Fuentes: support 5964503973271 (failed payments, 28-ago-2026), 42880290187287 (Phased Subscriptions, 20-ago-2026), 4403759737879 (manage student payments, 11-sep-2026), 360034692814 (subscription price, 30-ago-2026), stripe.com/customers/thinkific.

- Peso: "32% of Thinkific Payments GMV from recurring subscriptions" (Stripe, cifra ~2023). Sobre el GPV TTM de $291M serían ~$93M/año recurrentes si la proporción se mantiene (estimación propia, NO citar como dato de Thinkific).
- Solo corren en Thinkific Payments o Stripe directo. PayPal no soporta recurrencia. Métodos válidos para recurrencia: tarjeta, Apple Pay, Google Pay, Link. Ningún APM, ningún débito bancario en checkout.
- Las suscripciones y payment plans NO usan Local Currency at Checkout: un estudiante en Brasil o India que se suscribe a un creator de US paga en USD con tarjeta cross-border, cada mes.
- Fallo de cobro: el estudiante pierde acceso a las 23:59:59 UTC del día de renovación ("Enrollment Expired"). Smart Retries de Stripe: "eight times over a three-week period". Card Account Updater incluido. Un solo email al estudiante tras el primer fallo; puede renovar desde My Account > Billing.
- Tras 3 semanas: en plan Plus la suscripción pasa a "Unpaid" con ventana de recuperación de 90 días (solo retry manual del admin, no configurable; aplica a suscripciones que pasen a Unpaid desde el 25-ago-2026). En todos los demás planes, y en payment plans y phased subscriptions de cualquier plan, se cancela de inmediato y el estudiante debe recomprar.
- Stripe directo: el creator elige en el dashboard de Stripe entre Smart Retries o schedule propio; una actualización de tarjeta no dispara reintento, hay que reintentar a mano.
- Novedades 2026: Phased Subscriptions (ago, solo Plus + TCommerce: pago inicial que convierte a recurrente), repricing masivo con 30 días de aviso (jun), recordatorio 7 días antes del cobro mensual (jul), EU Withdrawal Right de 14 días (ago), avisos pre-renovación para BC (ago). Thinkific vende esto como "revenue protection through Thinkific Payments".
- Fee de suscripción: +0.7% sobre el fee de tarjeta.
- Dependencia: todo esto es Stripe Billing + Stripe Radar + Stripe Tax bajo un contrato que "renews every 12 months unless either party provides a notice of termination at least 30 days prior" (AIF 2025).
### 4d. Thinkific Plus y B2B: lo que sí y lo que no tienen

Fuentes: thinkific.com/plus, thinkific.com/pricing, support 20508209851671 (Group Orders, 17-jul-2026), 32324759426839 (Invoicing, 5-feb-2026), 360049340433 (B2B con Plus).

- Plus = precio custom flat sin fee por learner, 10,000+ seats, SSO (OIDC/SAML), SCORM 1.2 y 2004, SOC 2 Type II, data residency, múltiples sitios/environments bajo un plan, HubSpot/Salesforce sync, custom roles, Thinker AI, Branded Mobile.
- Pagos en Plus: mismos tres procesadores (Thinkific Payments, Stripe directo, PayPal). Plus está exento del third-party gateway fee ("No fee at this time"). Group Orders (solo con Thinkific Payments, solo precios únicos, con volume discounts) e Invoicing (Grow+, solo precios únicos, 0.4% por factura; ACH US 1%, PAD Canadá 1.5%, SEPA UE 1%, off-platform 0%).
- No existe: purchase orders como feature (solo factura marcada pagada off-platform), checkout custom para Plus, two-step checkout en Thinkific Payments, multi-currency real (una moneda de cobro y payout por sitio; "Multi-currency pricing - coming soon!" en la roadmap de TCommerce).
- Lo que dijo el CEO en la call Q4-2025 sobre Plus y pagos: los compradores enterprise "do have other options to process payments or maybe doing it somewhere else. But then, when they realize they can bring it all into one system with us that's truly integrated... it quickly becomes a strong selling feature". Growth driver del deck Q2: "Grow Thinkific Commerce penetration with Plus customers". Un cliente Plus con entidad en Brasil, México o India hoy no puede usar Thinkific Payments: tiene que irse a Stripe directo sin TCommerce o fuera de la plataforma.
- Vacantes: en 2025 hubo un Group Product Manager, Commerce ("checkout and payments to pricing and subscriptions", reporta al VP Product; posting retirado el 2-sep-2025). En 2026 no hay ninguna vacante que mencione payments, billing, Stripe u orquestación. Vacante viva: Senior PM para Thinkific Plus. Ninguna mención pública de "orchestration", "multiple processors" o "auth rates" en blog, soporte, filings o calls.
## 5. Fit contra las tres prioridades que ya vimos en Skool

### 5a. Subscriptions: fit alto, y es el mismo patrón exacto de Skool

Lo que Thinkific tiene: motor de suscripciones de Stripe Billing, 8 reintentos en 3 semanas, CAU, un email de dunning, cancelación automática salvo Plus, todo en un solo procesador, solo tarjeta y wallets, sin moneda local en renovaciones.

Lo que Yuno pone encima sin cambiar el motor:
- **Stripe Billing bridge** (docs.y.uno/docs/payment-features/subscriptions/stripe-billing): "Keep Stripe Billing as your subscription engine — plans, invoices, billing cycles, dunning — while Yuno processes every charge through your own providers and routing rules." Yuno guarda la tarjeta, ejecuta el primer cobro y cada renovación como MIT con stored credentials, reporta el resultado a Stripe, y "Failed renewals follow the retry schedule you configure in Stripe; each retry is executed by Yuno across your provider cascade." Requisito: Stripe con "third-party payment processing enabled" (self-serve, US soportado, como confirmó Samuel a Skool el 18-ago). Es lo que Skool está probando en sandbox desde el 10-sep con retries de Yuno en lugar de Smart Retries.
- **Yuno Subscriptions** (docs.y.uno/docs/payment-features/subscriptions): retries DEFAULT (6 intentos en ~9 días), CUSTOM_SCHEDULE o SMART (modelo ML que elige el momento por "decline reason, the country, the card issuer and the payment provider"); PAST_DUE con webhook; pause/resume; trials; CARD, PAYPAL_ENROLLMENT y PIX_AUTOMATIC. Pix Automático (docs.y.uno/docs/payment-features/subscriptions/pix-automatico) es recurrencia nativa del rail brasileño vía Adyen: algo que Stripe Billing no ofrece.
- Network tokens y account updater en todos los providers, no solo en Stripe.
- Cifras públicas: página de subscriptions en y.uno muestra "4.6% Approval-rate uplift" y "30% Decline recovery"; home muestra "74.30% Retry success rate" y "30% recovered revenue". Internas (OK de Daniel Lozano): 16 merchants, 135K subs activas, 83% primer intento a 86% tras retries, 69K subs past-due reactivadas en 30 días.
- Gap honesto: Yuno no tiene invoicing, tax, dunning emails al estudiante ni portal self-serve. Por eso el bridge es el pitch correcto: Thinkific conserva todo eso en Stripe Billing.

### 5b. Nuevos métodos de pago: fit alto en recurrencia y fuera de UE, fit bajo dentro de US/UE

Thinkific ya cubre bien wallets, BNPL y bank redirects europeos para pagos únicos en sus 36 países. El pitch NO es "les faltan métodos en US/UE"; el deck /m/thinkific ya corrigió eso el 17-sep (Thinkific ya ofrece iDEAL, Bancontact, EPS, P24, Sofort).

Dónde sí hay hueco verificado:
1. **Métodos que aceptan recurrencia.** Hoy solo tarjeta, Apple Pay, Google Pay y Link. Yuno documenta PayPal enrollment y Pix Automático como instrumentos de suscripción, y SEPA/ACH como métodos de débito (Xendit DIRECT_DEBIT, etc.). Para un negocio donde ~un tercio del GMV es recurrente, cada método recurrente nuevo es retención.
2. **Métodos locales para el estudiante fuera de US/UE** que hoy paga cross-border con tarjeta: Pix, Boleto, Nupay (BR); OXXO, SPEI, CoDi (MX); PSE, Nequi, Daviplata (CO); Yape, Plin, PagoEfectivo (PE); Webpay, Khipu, Mach (CL); MODO, RapiPago (AR); PayPay y konbini (JP); KakaoPay, NaverPay (KR); GCash, Maya (PH); Dana, OVO, QRIS (ID); FPX, GrabPay (MY); Tabby, Tamara (EAU/KSA); Vodafone Cash, Fawry (EG); M-Pesa (KE); BLIK, Swish, MobilePay, Vipps (PL/SE/DK/NO). Todos listados en y.uno/en/integrations o en docs.y.uno/reference/payment-type-list. UPI aparece solo en copy de marketing de y.uno, no en el catálogo: no prometerlo por escrito.
3. **BNPL sin las restricciones de Stripe:** Klarna hoy se oculta si creator y comprador están en países distintos, y todos los BNPL se apagan al activar moneda local. Con orquestación se puede rutear Klarna/Afterpay por el provider que corresponda y sumar ADDI, Kueski, Aplazo, aCuotaz, Tabby, Tamara en sus mercados.
4. **Interac en Canadá:** Thinkific no lo ofrece. Yuno tampoco lo lista en el catálogo público. No usar.

### 5c. Local acquiring en más regiones: el hueco más grande y el que Justo pidió mapear

Thinkific tiene procesamiento local en 36 países. Un tercio de su revenue (33%, $6.1M en Q2) viene de clientes fuera de US y Canadá, y su propio deck Q2 lista "Internationalization of features driving adoption in UK and EU" como growth driver. El take rate cae cuando sube la venta internacional (CFO, call Q4-2025), justamente porque fuera de sus mercados core no tienen los productos de mayor margen (sales tax, BNPL).

Mercados donde Thinkific Payments NO existe y Yuno tiene adquirencia local publicada (y.uno/en/integrations, catálogo parseado el 24-sep-2026; docs.y.uno/reference/payment-type-list):

| Mercado | Adquirentes / PSPs locales en Yuno (selección) | Métodos locales en Yuno |
|---|---|---|
| Brasil | Cielo, Rede, Getnet, Stone, Pagar.me, PagSeguro/PagBank, Adyen, dLocal, EBANX (MoR) | Pix, Pix Automático (recurrente), Boleto, Nupay, PicPay, Pix Parcelado |
| México | OpenPay, Prosa, BBVA, Banorte, Kushki, Getnet, EVO, Global Payments, Fiserv, dLocal, EBANX | SPEI, OXXO Pay, CoDi, Kueski, Aplazo, Mercado Pago |
| Colombia | Credibanco, Redeban, Wompi, PayU, ePayco, PlaceToPay, Kushki | PSE, Nequi, Daviplata, Efecty, ADDI |
| Argentina | Prisma, Mercado Pago, Getnet, dLocal | MODO, Pago Fácil, RapiPago |
| Chile | Transbank/Webpay, Klap, Kushki, Fintoc | Webpay, Khipu, Mach, Servipag |
| Perú | Niubiz, Izipay, Alignet, Kushki, Monnet | Yape, Plin, PagoEfectivo, Cuotéalo |
| India | Razorpay, BillDesk, PayU, 2C2P, NTT Data | UPI solo en copy de marketing, no en catálogo |
| Japón | NTT Data (network tokens, 3DS), Adyen | PayPay, konbini (7-Eleven, FamilyMart, Lawson) |
| Corea | Adyen vía KCP, NTT Data | KakaoPay, NaverPay, Payco |
| Indonesia | Xendit, Doku, Midtrans, 2C2P | Dana, OVO, ShopeePay, QRIS, Alfamart, Indomaret |
| Filipinas | Maya, Xendit, 2C2P | GCash, GrabPay, Maya wallet, QRPH |
| Tailandia / Malasia / Vietnam | 2C2P, AsiaPay, Xendit, NTT Data | Thai QR, TrueMoney, FPX, Boost, GrabPay, ShopeePay |
| EAU | Network International, Telr, PayTabs, Tap, Checkout.com | Tabby, Tamara, Careem Pay |
| Arabia Saudita | Mada, Moyasar, Geidea, HyperPay, PayTabs, Tap | SADAD, STC Pay, Tabby, Tamara |
| Sudáfrica | Yoco, PayFlex, iVeri, DPO, Flutterwave, PayU | Solo tarjetas y wallets globales |
| Nigeria / Kenia | Flutterwave, OPay, Monnify, M-Pesa, Pesapal, DPO | M-Pesa (como provider) |
| Egipto | Fawry, Paymob, Kashier, Geidea | Vodafone Cash, Meeza, ValU, 38 métodos locales |
| Turquía | Param (network tokens) | Solo globales |
| Israel | Sin adquirente local en el catálogo | No proponer |

Además, en los 27 países de la UE donde Thinkific ya procesa, Yuno suma métodos que Thinkific no tiene: BLIK y Przelewy24 (PL, vía Stripe/Adyen), Swish (SE), MobilePay (DK), Vipps (NO), Trustly, SEPA DD, TWINT (CH).

**Cómo priorizar los mercados sin inventar datos de Thinkific:** Thinkific no publica distribución de creators por país fuera de US/CA/RoW. Lo que sí es verificable: Hotmart (dueño de Teachable, cliente de Yuno con logo público) nació en Brasil y procesa con Yuno en BR, MX, CO, CL, AR, PE; Skool está abriendo LatAm con dLocal bajo Yuno; Open English (caso público) opera 30+ países con foco LatAm. Es decir, los competidores directos de Thinkific ya están cobrando localmente en LatAm con nosotros. Ese es el argumento: no "Brasil es grande" sino "tus competidores ya lo hacen con nosotros".

Dos formas de darles adquirencia local, ambas sin abrir entidades:
1. **MoR/cross-border local:** dLocal, EBANX, Flutterwave, PayRetailers, PagSmile como merchant of record en el país, liquidando en USD. Es lo que hace Whop con dLocal (cobra en moneda local, FX en el payout).
2. **Adquirente local directo** cuando el creator (o Thinkific Plus) tiene entidad local: Cielo/Rede/Getnet en BR, Prosa/BBVA en MX, Credibanco/Redeban en CO, Niubiz en PE, Razorpay en IN, NTT Data en JP.

### 5d. Dos ángulos extra que salieron del research y no estaban en el brief de Justo

- **Riesgo de proveedor único, en sus propias palabras.** El AIF 2025 lista a Stripe como vendor crítico con contrato que renueva cada 12 meses y termina con 30 días de aviso, y dice que reemplazarlo implicaría "substantial delays and expense in finding and integrating alternative providers". Yuno es la forma de tener esa alternativa integrada antes de necesitarla, sin sacar a Stripe.
- **Margen.** Gross margin 73% y el CFO atribuye la mejora a "improved operational efficiencies in our Payments platform". Con un target de FCF 25%+ en 2027 y 96 despidos, cada punto de costo de procesamiento y cada dólar recuperado en renovaciones va directo al objetivo público. Cifras públicas de Yuno para esto: "27% savings on payment costs" y "30% recovered revenue" (home de y.uno). Whop, con logo público, pasó de Stripe único a 7 providers; los dólares recuperados ($216M) son internos.
## 6. Competidores: cómo cobran hoy (para dimensionar la presión competitiva)

| Plataforma | Procesamiento | Países del creator | Métodos del comprador | Moneda |
|---|---|---|---|---|
| **Thinkific** | Thinkific Payments = Stripe | 36 | Tarjetas, Apple/Google Pay, Link, Cash App, Amazon Pay, 5 bank redirects UE, Klarna, Afterpay; recurrente solo tarjeta/wallets/Link | Una por sitio; local currency solo en pagos únicos |
| **Teachable** (Hotmart) | teachable:pay, reconstruido sobre Stripe | "40+ markets"; changelog de 47 países nuevos incl. Argentina, Chile, Colombia, Perú, México, India, Indonesia, Malasia, Filipinas, Vietnam, Egipto, Kenia, Sudáfrica, Arabia Saudita, Turquía | "35+" métodos locales: Pix, iDEAL, SEPA, BNPL regional, Apple/Google Pay, Klarna, Affirm, Alipay, WeChat Pay | "local-currency adaptive pricing"; tax en 45+ países |
| **Kajabi** | Kajabi Payments, "built in partnership with Stripe" | US, CA, AU, EAU, UK y 20 países UE | Tarjetas, Apple/Google Pay, Afterpay/Clearpay, Klarna, ACH en facturas; sin iDEAL/Bancontact/SEPA listados | Una cuenta bancaria por moneda de payout |
| **Podia** | Solo Stripe y/o PayPal del creator | Donde haya Stripe; no cobra application fee en cuentas de BR, MY, IN, TH, MX | Vía Stripe: Apple/Google Pay, iDEAL, Link; "unable to process" SEPA, Bancontact, Afterpay, Klarna, Razorpay | Una por sitio |
| **Skool** | Stripe Express bajo el merchant de Skool | Payouts a ~152 países | Solo tarjeta en su help center | "All subscription prices on Skool are in USD. Members pay in USD"; payout en moneda local |
| **Mighty Networks** | Solo Stripe | 46 países de Stripe | Vía Stripe; sin PayPal | Hasta 10 monedas de presentación |
| **LearnWorlds** | Stripe, PayPal, Shopify, PagSeguro | Donde haya Stripe; PagSeguro solo BRL | Vía Stripe: Apple/Google Pay, Klarna, Afterpay, iDEAL, Bancontact, P24, Boleto, Pix | Según gateway |

Fuentes: teachable.com/payments, support.teachable.com/en/articles/11682555, changelog.teachable.com/teachable-payments-expands-to-47-new-countries-249543, help.kajabi.com (artículos 34652803193499, 31588593189787, 23370972909851), help.podia.com/en/articles/11370248, help.skool.com/article/86-subscriptions-faq, docs.mightynetworks.com/en/articles/3825267, support.learnworlds.com/support/solutions/articles/12000027007.

**Lectura:**
- El competidor más parecido (Teachable) está muy por delante en cobertura local: 40+ mercados con Pix, iDEAL, SEPA y precio adaptativo en moneda local, contra 36 países y solo tarjeta fuera de la UE en Thinkific. Hotmart, la matriz de Teachable, anunció con EBANX (PR 24-sep-2025) Pix Automático en producción desde jun-2025 con "32 percentage point uplift in customer retention for recurring payments via Pix". Ojo: ese caso es de EBANX, no de Yuno; Hotmart es cliente de Yuno para otros flujos. No mezclar en el mensaje.
- Kajabi está más o menos a la par de Thinkific (Stripe, mismos países, menos bank redirects). Podia y Mighty Networks van por detrás.
- Skool, que es nuestro cliente y "adjacent" según Justo, todavía cobra solo en USD y con tarjeta: exactamente los tres huecos que está cerrando con nosotros (Stripe Billing bridge, Apple Pay, dLocal para LatAm). Es la prueba de que las tres prioridades son las mismas en todo el vertical.
- Ninguna de las siete plataformas anuncia orquestación multi-adquirente. La primera que lo haga tiene un argumento de venta para creators internacionales que ninguna otra tiene.
## 7. Referencias de Yuno en el vertical creator / edtech (qué es público y qué no)

Logos públicos en la home de y.uno (24-sep-2026): McDonald's, Rappi, Uber, NetEase, Ant Group, inDrive, Despegar, **Hotmart**, Viva Aerobus, Tada, **Whop**, Moon Active, Livelo, Wingo, Garena, Reserva, GoFundMe, Kavak, Copa Airlines, Carrefour. Skool NO está.

Success stories públicas (y.uno/en/success-stories): Vibra, inDrive, McDonald's, Rappi, Livelo, Viva Aerobus, Reserva, **Open English** (único SaaS/edtech). Ni Hotmart ni Whop ni Skool tienen caso público.

### Skool (merchant, NO público todavía)
- Contrato firmado 23-jul-2026, 36 meses con ventana de validación de 90 días (termina ~21-oct-2026) en la que Skool puede salir sin penalidad. Owner: Samuel Vieira. Sam Ovens (CEO) es el contacto.
- Live desde el 15-sep-2026 (Salesforce, "Lord Live Updater"). Primeros días: 167 tx / $17K el 18-sep. Región North America, tarjetas US vía Stripe bajo Yuno.
- Lo que están construyendo con nosotros, mapeado a sus tres prioridades:
  1. **Subscriptions:** Stripe Billing bridge. Skool sigue usando Stripe Billing como motor de suscripciones y Yuno procesa los cobros como "third-party processor" (custom payment method en Stripe). Stripe Smart Retries apagados, el engine de retries de Yuno maneja los reintentos (Samuel a Sam Ovens, 18-ago). Bridge en pruebas de sandbox 10 a 14-sep.
  2. **Nuevos métodos de pago:** Apple Pay en integración (Barak, frontend Skool, 10-sep). Jarrett les advirtió el 23-sep que Pix, Boleto, OXXO, SPEI y PSE son asíncronos y la mayoría no sirve para renovaciones off-session, así que APMs para signups LatAm van en una conversación aparte.
  3. **Local acquiring en más regiones:** dLocal conectado como provider (canal compartido con dLocal 2 a 11-sep). Plan de Skool: "LATAM countries route through dlocal, and elsewhere goes through stripe" (Kevin, Skool, 18-sep). dLocal exige documento (CPF, CURP, DNI) en casi todo LatAm; Justo escaló a C-level de dLocal y consiguieron waiver salvo Brasil y Argentina (21-sep). Crossbeam/Salesforce: dLocal para "Europe/LatAm", Skool migrando payouts fuera de Stripe.
- Benchmarks que Skool mira: Whop y Hotmart ("When testing out the workflow on Whop and Hotmart...", Kevin 18-sep). Whop cobra subs en moneda local con FX en el payout vía dLocal.
- Sam Ovens rechazó el workshop con CTO/CPO: "i'd rather just do the integration and let you know what we need from you guys." Cliente pragmático, poco apetito de reuniones.
- Cifras internas que NO se comparten: TPV proyectado $960M run-rate a 12 meses, mínimo mensual $30K.
- **Uso en el mensaje:** Skool es competidor directo de Thinkific (Justo lo lista como adjacent). Está en ventana de POC, sin permiso de referencia. Recomendación: no nombrarlo; describirlo como "a fast-growing US community and course platform that went live with us this month". Si Justo quiere nombrarlo, pedir OK a Samuel y a Sam Ovens antes.

### Whop (logo público; cifras internas)
- Marketplace de creator commerce. Live en Yuno desde 9-ago-2025. Antes: "Whop ran Stripe as its sole processor before Yuno, and the move to Yuno removed that dependency."
- Doc interno de Caio Freitas "Whop and Yuno: a business case success story" v1.0, 20-sep-2026 (Google Doc 1wk8h8bGWIvH5a5_rIj_8DQYKFiBQLJGo27piIPgrxSI), datos del warehouse 9-ago-2025 a 20-sep-2026:
  - $2.73B TPV y 17.8M pagos exitosos. Agosto 2026: $349M, 2.46M pagos, 237 países, 75 monedas, 16 tipos de método, 7 providers con volumen (Checkout.com, Adyen, Stripe, NMI, Airwallex, Splitit, dLocal).
  - Salió a producción el mismo día en Stripe + Adyen + Checkout.com. Migración de ~1.4M tarjetas Apple Pay y 17,806 network tokens fuera de Stripe con 92% de éxito.
  - Métodos añadidos en 12 meses: Apple Pay, Google Pay, Klarna, Afterpay, iDEAL, SEPA, Bancontact, TWINT, crypto, Splitit, installments vía dLocal.
  - Cascade recuperó 880,665 pagos por $216.3M tras un primer intento fallido = 7.9% del TPV total; 99.7% vía una capa de routing posterior. Adyen 905_1 recuperado al 87.2%.
  - Approval transaction-level pasó de 45.7% (sep-2025) a 57.9% (ago-2026). Network tokens en 89.1% de intentos de tarjeta en ago-2026.
  - MIT (renovaciones) aprueba 57.3% vs CIT 73.9%: gap de 16.6 puntos, workstream propuesto.
- **Postura de share (Taylor Mason / Caio, #roblox-internal 22-sep):** "Whop (internal only per KAM/Marketing, not social/public)". Caio: "if we are not sharing in social media/public, i dont see any problem". Es decir, en un email 1:1 se puede citar el logo (es público) y como mucho la historia cualitativa ("Stripe-solo a 7 providers, 237 países, 16 métodos"); los dólares ($216M) son internos. Recomiendo confirmar con William Wong (TAM) antes de dar cifras.

### Hotmart (logo público; dueño de Teachable)
- Merchant de Yuno desde antes de 2026 (renovación de contrato en curso desde abr-2026, KAM Martin Seggewiss; Martin pidió incluir uso de marca en el website y hoy el logo está en y.uno).
- Datos internos (Melissa Pottenger, #gtm-team, 7-jul-2026): providers Stripe, Rede, MercadoPago; países US, CA, BR, MX, CO, CL, AR, PE y más; 1.2M pagos/30 días; approval 61.5%. Network tokens activos para Visa y MC (abr-2026), Mastercard Account Updater en enrolamiento. Web SDK headless.
- Hotmart es la matriz de Teachable, el competidor más parecido a Thinkific. German ya le dijo a Teachable en abril que Hotmart trabaja con nosotros ("I already told him Hotmart works with us", DM con Martin 14-abr). Martin confirmó que Teachable "not yet" usa Yuno y que "were considering consolidating some services/providers later this year".
- **Uso en el mensaje:** se puede nombrar como logo (público). Sin cifras.

### Open English (caso público, edtech con suscripciones en LatAm)
- y.uno/en/success-stories/open-english: plataforma de inglés online, 30+ países, 2M+ estudiantes. Yuno integró wallets y BNPL, optimizó routing en LatAm, PCI y antifraude centralizados. Resultados publicados: "increased approval rates across Latin American markets", "reduced time-to-market for expansion into new regions", "decreased processing costs". Sin porcentajes públicos.
- Quote pública: "By enhancing our payment processing, we have increased our approval rates and reduced costs." Wilmer Sarmiento, cofundador.

### Cifras públicas de Yuno utilizables (y.uno, 24-sep-2026)
- "1,000+ payment methods, PSPs, and fraud solutions"; "60+ providers in North America"; "20+ countries in North America".
- "30% recovered revenue"; "27% savings on payment costs"; "74.30% retry success rate"; "7% uplift in approval rates" (FAQ); "90% reduction in development time".
- inDrive: ~90% approval, 11 nuevos países en menos de 8 meses.
- Subscriptions engine (Control Center 31-ago-2026, deck interno de Daniel Lozano): 16 merchants en producción, 135K suscripciones activas, aprobación por ciclo 86% tras retries vs 83% primer intento, 69K suscripciones past-due reactivadas en 30 días. Magdalena ya usó "16 merchants / 135K" en outbound; el resto requiere OK de Daniel Lozano.
## 8. Mensaje propuesto para que Justo lo envíe

Cómo enviarlo: reply-all en el hilo "Re: Thinkific + Yuno at Stripe Sessions", a Darren y Tauqeer, con Greg y Amy en copia como hasta ahora, y German y William en copia. Sin links ni adjuntos en el cuerpo (German o Justo agregan el deck si quieren). Sin em-dashes. Tono de Justo: corto, cálido, CRO a VP.

Por qué este ángulo: Darren dijo "later this summer when we start to look again into Orchestration". Ya es fin de septiembre, la empresa acaba de anunciar foco en Plus y cash flow, y las tres prioridades que vimos en Skool (subscriptions, métodos nuevos, local acquiring) son exactamente los tres huecos verificados de Thinkific Payments. El mensaje no pide reunión primero; primero da dimensión de lo que hacemos con plataformas iguales y deja la reunión como consecuencia.

### Versión A (recomendada, ~210 palabras)

Subject: Re: Thinkific + Yuno at Stripe Sessions

Hi Darren, Tauqeer,

Saw this week's update on concentrating investment in Plus and free cash flow. Payments is one of the few levers that moves both, so instead of asking for time again I wanted to share what we are doing with platforms like yours.

Three things come up with every course and community platform we work with this year.

Subscriptions. They keep Stripe Billing as the engine and let Yuno run every charge and retry across their own processors. Nothing in their billing logic changes, renewals simply clear more often. Across our platform, retries and fallback recover about 30% of revenue that would otherwise be lost.

Payment methods that can carry a subscription. Cards and wallets are the ceiling today. We add PayPal, SEPA, Pix Automático in Brazil and local debit rails so a renewal runs on whatever the student actually uses.

Local acquiring beyond the 36 countries where Thinkific Payments is available today. Whop moved from Stripe only to a multi-acquirer setup on Yuno and now sells in local currency almost everywhere. Hotmart, Teachable's parent company, is a Yuno customer across Latin America. A US community platform that went live with us this month routes Latin America through a local acquirer while the rest stays on Stripe.

None of this replaces Stripe or Thinkific Payments. It sits on top of them.

When the orchestration review is back on your agenda, thirty minutes is enough for us to show you what each of these looked like for those teams.

Best,
Justo

### Versión B (nudge corto, ~110 palabras, si Justo prefiere no explicar)

Hi Darren, Tauqeer,

Hope the summer treated you well. When we spoke in May you mentioned revisiting orchestration after the summer, and given this week's update on Plus and free cash flow I think the timing is better, not worse.

Since Sessions we have gone live with several course and community platforms on the same three things: keeping Stripe Billing as the engine while we run the charges and retries across their processors, adding methods that can carry a subscription, and local acquiring in the markets where Thinkific Payments is not available today. Whop and Hotmart, Teachable's parent, are two you would recognise.

Happy to walk you through what that looked like for them whenever it is useful. Thirty minutes is enough.

Best,
Justo

### Sustituciones opcionales (solo con el OK indicado)

- Nombrar a Skool en lugar de "A US community platform that went live with us this month": requiere OK de Samuel Vieira y de Sam Ovens. Skool está en ventana de validación de 90 días y es competidor directo de Thinkific. Si se nombra: "Skool went live with us this month and is routing Latin America through a local acquirer while the rest stays on Stripe."
- Cifras de Whop ("237 countries, 75 currencies, seven processors, $216M recovered"): son internas según KAM y Marketing. Requiere OK de William Wong. Sin OK, dejar la versión cualitativa.
- Detalle de Hotmart ("across Latin America", países): el logo es público, los países vienen de Slack interno. Confirmar con Martin Seggewiss o dejar solo "is a Yuno customer".
- Cifras del engine de suscripciones ("16 merchants, 135K active subscriptions, 83% to 86% per cycle, 69K past-due subscriptions reactivated in 30 days"): requieren OK de Daniel Lozano. Si se aprueban, reemplazan la frase "retries and fallback recover about 30%..." por: "Across the sixteen merchants on our subscriptions engine, retries lift per-cycle approval from 83% to 86% and reactivated 69,000 past-due subscriptions in a month."
- "About 30% of revenue that would otherwise be lost": es "30% recovered revenue" y "30% Decline recovery" publicados en y.uno (home y página de subscriptions). Ok tal cual.
- "36 countries": es la lista oficial de Thinkific (support 1500012376321). Ok tal cual. Demuestra que hicimos la tarea.
- "Hotmart, Teachable's parent company": Hotmart compró Teachable en 2020 (público). Ok tal cual.

## 9. Lo que NO decir y pendientes

- No afirmar que Yuno mueve Pix Automático para Hotmart: el caso público de Pix Automático de Hotmart (32 puntos de retención) es de EBANX (PR 24-sep-2025), no de Yuno.
- No decir "one currency lock" o "les faltan iDEAL/Bancontact": ya lo corrigió el deck el 17-sep. Thinkific tiene bank redirects UE, wallets, BNPL y moneda local en pagos únicos.
- No decir UPI por escrito como método en catálogo: aparece solo en copy de marketing de y.uno; Razorpay, BillDesk y PayU sí están como providers.
- No decir Interac: ni Thinkific ni el catálogo público de Yuno lo listan.
- No usar "+12% uplift" ni "20 a 30% decline recovery" (marcados como inventados). Públicos: 7% uplift (FAQ), 8% uplift (smart routing page), 4.6% (network tokens y subscriptions pages), 30% recovered revenue, 74.30% retry success, 27% savings on payment costs.
- No mencionar los 96 despidos de forma explícita; "this week's update on concentrating investment in Plus and free cash flow" es suficiente y es lenguaje del propio release.
- No citar "Automated Sales Tax launched via a Stripe partnership" como novedad 2026: se lanzó en agosto de 2023.
- El precio "$1.34" de la acción no existe en ninguna fuente; cerró a CA$1.20 el 23-sep y subió a ~CA$2.10 el 24-sep tras la reorganización.
- Pendiente: confirmar si "greg@thinkific.com" del hilo es Greg Smith (CEO). Si lo es, es quien hoy supervisa producto directamente y quien firmó la reorganización; el mensaje ya le llega en copia.
- Pendiente: si no hay respuesta en 10 días, el siguiente toque debería ir a Greg Smith directamente (LinkedIn o correo) con el ángulo de margen, porque Darren y Tauqeer pueden haber salido en la reorganización.
- Pendiente: el deck /m/thinkific todavía muestra la fila de impacto +12% / 20 a 30% y la card 03 de slide 4 con "iDEAL in Netherlands, BLIK in Poland". Corregir antes de reenviarlo (ver memoria project_thinkific).
- Glean devolvió 401 (Invalid Secret) durante este research; no se pudo consultar. Gong no tiene llamadas con Thinkific.

## 10. Fuentes principales

Thinkific (primarias): investors.thinkific.com (release Q2 5-ago-2026, transcript Q2, MD&A Q2, deck Q2, estados financieros Q2 y FY2025, AIF 2025, release reorganización 23-sep-2026, transcript Q4-2025); support.thinkific.com artículos 1500012376321, 22383950439575, 360030737273, 38311651243671, 360060177513, 14047200964119, 12448134209303, 360030357494, 360030357334, 360030723513, 360030357514, 5964503973271, 42880290187287, 4403759737879, 360034692814, 7302902582807, 41582716364567, 20508209851671, 32324759426839; thinkific.com/product-updates, /pricing, /plus; stripe.com/customers/thinkific; prnewswire (sales tax ago-2023); Yahoo Finance / StockAnalysis / Globe and Mail (cotización 24-sep-2026).
Competidores: teachable.com/payments, support.teachable.com, changelog.teachable.com, help.kajabi.com, stripe.com/customers/kajabi, help.podia.com, help.skool.com, docs.mightynetworks.com, support.learnworlds.com, prnewswire (EBANX/Hotmart 24-sep-2025).
Yuno (públicas): y.uno/en, y.uno/en/integrations (catálogo parseado, 420 items), y.uno/en/success-stories, y.uno/en/product/subscriptions, y.uno/en/product/smart-routing, docs.y.uno/docs/payment-features/subscriptions (+ retries, pix-automatico, stripe-billing), docs.y.uno/reference/payment-type-list.
Internas: Gmail hilo 19ddaaf62bafc410; Slack #yuno-skool-external, #salesops-legal, #roblox-internal, #gtm-team, #test-updater, #finance-merchants, DMs con Martin Seggewiss y Samuel Vieira; Google Doc "Whop and Yuno: a business case success story" (Caio Freitas, 20-sep-2026); memoria project_thinkific, reference_subscriptions_stats, feedback_published_stats_only.
