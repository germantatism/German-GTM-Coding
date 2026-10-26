# Civitatis + Yuno: business case (25-oct-2026)

Pedido de German (25-oct-2026): business case "como siempre" (método Cruz Verde, cinco palancas) sobre la data que Alejandro Albarracín compartió por correo, en una COPIA de su deck, y compartirla con Alejandro cuando esté lista.

## Fuentes de Alejandro (compartidas con la service account el 25-oct)
- Deck original: "Civitatis × Yuno — Propuesta", Google Slides `1I176rhzowROapMxhyIJXcaLSfZhefKSkDbcAeIblLb8` (21 slides, español, estructura Palco/Cruz Verde; firma Lucca Zadra + Alejandro). Slides 13 y 14 venían con "A cuantificar" en todas las palancas.
- Calculador: "Civitatis – Pricing Calculator LATAM (2026-10)", Google Sheet `1IssNFagNj-ajV53g4XNIvPKRozQN0ui_s70EHEO4LYI`. Tab "Civitatis – Inputs & notas" = la data del cliente.

## Data de Civitatis (tab Inputs, solo LATAM)
| Dato | Valor |
|---|---|
| TPV mensual | ~USD 6,000,000 |
| Transacciones mensuales | 38,000 |
| Ticket promedio | USD 200 declarado / USD 157.89 implícito (6M / 38K). Alejandro usa 157.89 para cuadrar el TPV. ⚠️ Confirmar con Civitatis |
| Industria | Travel (tours/actividades, marketplace), margen 15%, banda M2 |
| Países | México, Brasil, Argentina, Colombia, Chile, Perú |
| Proveedores actuales | dLocal, Ebanx, PayPal, MercadoPago, American Express, Adyen, Checkout.com |
| Nuevos métodos | cubrir los métodos que representan el 90% del volumen en esos países |
| Chargeback rate | 0.35% |
| Expansión | ninguna por ahora |
| Aprobación de tarjeta | ~90% |
| 3DS / fraude | sin dato, no cotizados |

Calculador: V2 (25K a 100K) × M2, platform fee sugerido $7,000, ladder 3 tramos $0.0787 / $0.0603 / $0.0481 (9,500 / 9,500 / 19,000) = $2,234/mes, blended $0.0588. Todo GREEN. Deck slide 16: $0.08 / $0.06 / $0.05 redondeados, all-in $9,234/mes = $110,808/año, "contrato a 3 años", 3DS y fraude a cotizar. ⚠️ El slide 13 original decía "inversión de referencia ~USD 12,000/mes" (inconsistente con los $9,234 de los slides 14 y 16); en la copia quedó $9,234.

## Business case (slides 13 y 14 de la copia)
Base: 38,000 pay-ins/mes × $157.89 = $6.0M/mes = $72M/año. Aprobación 90% → cerca de 42,200 intentos/mes.
| Palanca | Métrica | Conservador | Optimista | Promedio | Supuesto |
|---|---|---|---|---|---|
| L1 Aprobación y ruteo | +1.5 a +3 pp | $1.20M | $2.40M | $1.80M | 42,222 intentos × pp × $157.89 × 12; supuesto Yuno (igual que Cruz Verde) |
| L2 Métodos LATAM | +2% a +5% trx | $1.44M | $3.60M | $2.52M | % sobre $72M; Pix 42% del ecommerce BR 2025 y A2A 15% AR 2025 (GPR 2026); PSE 32% a 34% CO (Rebill, Antom) |
| L3 Costo multi-PSP | 10 a 20 bps | $72K | $144K | $108K | sobre $72M |
| L4 Costo de integrar | 7 integraciones | $45K | $115K | $80K | build 8 a 12 semanas × 2 ingenieros a $60K/FTE ($18.5K a $27.7K por integración); mantenimiento 20% a 30% × 7 ($25.8K a $58.2K) + 1 a 2 integraciones nuevas evitadas ($18.5K a $55.4K) = $44K a $114K |
| L5 Operación multi-PSP | 1 a 2 FTE | $60K | $120K | $90K | $60K por FTE (Madrid), supuesto Yuno |
| Total | | $2.82M | $6.38M | $4.60M | ventas incrementales L1+L2 $2.64M a $6.00M (prom. $4.32M); costos evitados L3 a L5 $177K a $379K (prom. $278K) |
Inversión: $110,808/año. Relación valor/inversión 25x a 58x, pero L1 y L2 están en valor de reservas (GMV), no en la comisión neta de Civitatis; se declara en los supuestos de ambos slides.

Diferencias con Cruz Verde: FTE a $60K (equipo en Madrid) en vez de $50K (Colombia); L4 = mantener 7 integraciones existentes + nuevas evitadas, en vez de construir 6 métodos en casa; L1 con +1.5/+3 pp iguales.

## Hechos públicos verificados (25-oct-2026)
- Europa Press / Bolsamanía, 19-ene-2026: Civitatis prevé crecer más de 30% en Latinoamérica en 2026; mercados clave México, Brasil, Argentina y Colombia; 1.2M de viajeros mensuales; 23,000+ agencias en LatAm de 40,000 en el mundo; 18 años; 5M+ reseñas, 9.1/10; CEO Andrés Spitzer; app nueva en 2026.
- Infonegocios, 11-jun-2026 (Nicolás Posse, country manager Argentina y Cono Sur): ticket promedio US$150 por actividad; 1M+ clientes argentinos en 2025; 3,000 agencias; 95% de los clientes en Argentina son extranjeros (negocio receptivo); más del 55% de las ventas globales vienen de Latinoamérica; 160 países; crecimiento 30% proyectado en Argentina 2026.
- Checkout.com, caso de éxito 27-nov-2025: Checkout.com procesa para Civitatis desde abril de 2025 con Intelligent Acceptance, Network Tokens, Real-Time Account Updater, Authentication y Fraud Detection Pro; métodos Visa, Mastercard, Amex, Discover, Cartes Bancaires, Google Pay y Apple Pay; "miles de reservas diarias en España, México, Brasil, Argentina, Colombia, Italia y Francia"; 90,000+ experiencias en 4,000+ destinos; cita de Arturo Moreno, Chief Data Officer. Sin cifras de aprobación.
- civitatis.com: no se encontró página oficial de métodos de pago; un blog de terceros menciona tarjeta, PayPal y bonos regalo. Pix, OXXO y Mercado Pago NO confirmados públicamente → pregunta de descubrimiento para la palanca 2.

## Puntos abiertos para Alejandro / Civitatis
1. Ticket: $200 declarado vs $157.89 implícito (el dato público de Argentina, US$150, apoya el implícito).
2. Qué métodos locales ya están vivos con dLocal, Ebanx y Mercado Pago (Pix, OXXO, SPEI, PSE, Yape, Webpay, cuotas) para afinar L2.
3. Checkout.com ya les da Intelligent Acceptance y network tokens en tarjeta: no criticar; el argumento de L1 es el ruteo ENTRE PSPs (adquirencia local vs cross-border), no reemplazar a Checkout.com.
4. "Contrato a 3 años" y la franja 3DS/fraude son de Alejandro, sin confirmar.
5. Los slides de Alejandro (fuera de 13 y 14) usan guiones largos en varios títulos; no se tocaron.

## Build
`build/fill_bc_civitatis.py <presentationId> dry|apply` (texto por element ID, método Cruz Verde; los IDs sobreviven la copia de Drive). `build/share_with_alejandro.py <presentationId>` comparte la copia con alejandro@y.uno como editor con mensaje. Thumbs en `build/thumbs/`.
Limitación encontrada: la service account tiene cuota de Drive 0 (Google), así que NO puede copiar ni crear archivos; la copia la hace German desde la UI y la comparte con `gtm-claude-editor@gtm-claude-tools-260922.iam.gserviceaccount.com`.
