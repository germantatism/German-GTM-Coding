# Buyer personas de Yuno (13)

Cómo usarlos: clasifica al lead en el persona más cercano según su cargo y scope.
El persona define qué le duele, qué mide y qué ángulo de Yuno le habla. El mensaje de
intro toma UNA idea de ese ángulo (la más relevante al contexto del hilo), no la lista
completa. Nunca inventar datos de la empresa del lead.

## CFO
Prioridad: rentabilidad y eficiencia. Pains: costos de pago altos, revenue perdido por
declines/chargebacks, conciliación manual, carga de compliance, demasiados vendors.
KPIs: Cost of Payments, Operating Margin, Cash Flow, Fraud/Chargeback Rates, ROI.
Ángulo Yuno: reducir fees vía smart routing, recuperar revenue vía approval uplift,
conciliación unificada, control de fraude/compliance, consolidación de vendors.
Proof stat: 5-20% approval uplift + ahorro por consolidación de vendors.

## VP / Head of Payments
Prioridad: performance y confiabilidad. Pains: múltiples proveedores, approval rates
bajos, rollout lento de métodos, ops manuales, riesgo de escalabilidad. KPIs:
Authorization Rate, Success Rate por región, costos de transacción, # métodos
soportados, uptime, fraude/chargebacks, conciliación de settlements. Ángulo Yuno:
smart routing + dynamic retries para approvals, habilitar métodos sin integración,
retries/conciliación/settlement automatizados, dashboards en tiempo real (approval por
región, salud de proveedores), alta disponibilidad.

## CCO (Chief Commercial Officer)
Prioridad: revenue y crecimiento global. Pains: ventas perdidas por declines, expansión
de mercados difícil, presión competitiva en checkout, visibilidad fragmentada, fricción
de checkout que golpea loyalty, falta de métodos locales que limita conversión. KPIs:
Revenue Growth, Conversion Rate, Market Expansion, CLV, Profit Margin. Ángulo Yuno:
approval uplift vía routing, 1,000+ métodos en 190+ países para expandir más rápido,
checkout unificado más fluido, visibilidad centralizada, capa de orquestación (sin
necesidad de reemplazar proveedores actuales).

## Engineering Leads (CTO / VP Eng)
Prioridad: sistemas escalables, seguros y eficientes. Pains: sobrecarga de
integraciones, mantenimiento/tech debt, carga PCI, escalar in-house consume tiempo de
ingeniería. KPIs: Development Velocity, Uptime/Reliability, Security/Compliance,
Resource Allocation, Scalability. Ángulo Yuno: un API reemplaza integraciones
fragmentadas, Yuno asume mantenimiento/compliance/PCI/tokenización, escalabilidad
cloud-native, entrega de features más rápida. Libera a los ingenieros para el core.

## CPO (Chief Product Officer)
Prioridad: UX fluida e innovación rápida. Pains: integraciones de pago lentas, fricción
en checkout, drenaje de ingeniería, experiencias globales inconsistentes, seguridad
compleja. KPIs: Feature Delivery Speed, Checkout Conversion, User Satisfaction,
Retention/Churn, cobertura global de features. Ángulo Yuno: lanzamientos de payment
features más rápidos, one-click/saved cards, suscripciones fáciles (tokenización +
retries automáticos), UX global consistente vía una capa de orquestación, seguridad y
compliance delegados.

## Marketing / Growth Leaders
Prioridad: adquisición, conversión, retención. Pains: carritos abandonados, opciones de
pago limitadas, fricción que desperdicia ad spend, fallas en pagos recurrentes que
cortan LTV, sin data de pagos para campañas. KPIs: Conversion Rate, Cart Abandonment,
CAC vs Conversion, LTV, crecimiento geográfico, NPS. Ángulo Yuno: más métodos + checkout
más rápido para bajar abandono, experiencias one-click/saved/localizadas, retries y
routing inteligentes para reducir renovaciones fallidas (LTV), insights de pago en
tiempo real para optimizar adquisición/ROI/CAC.

## CEO / Founder
Prioridad: crecimiento, márgenes, riesgo estratégico, escala, fundraising/valuación.
Pains: pagos filtrando revenue y margen en silencio, no poder expandirse a mercados
nuevos con velocidad, pagos como cuello de botella estratégico, riesgo de concentración
de infraestructura/vendors, sin visibilidad limpia de pagos para board e inversionistas.
KPIs: Revenue Growth, Gross Margin, velocidad de expansión, Customer Growth/Retention,
eficiencia operativa/valuación. Ángulo Yuno: convertir pagos en palanca de crecimiento
(approval uplift = más revenue sin más CAC), entrar a mercados en semanas vía un API,
proteger margen con routing + consolidación, un partner de infraestructura que escala
con la empresa, visibilidad nivel board, des-riesgar la dependencia de un solo rail o
vendor. Proof: 5-20% approval uplift, InDrive 10 mercados LATAM en <8 meses.

## Product Manager
Prioridad: shippear features de pago/checkout y ser dueño de métricas de funnel (más
táctico que el CPO). Pains: features de pago tardan y dependen de ingeniería, fricción
de checkout golpea activación/conversión, difícil hacer A/B testing de métodos o
routing, data inconsistente para decidir, lanzamientos lentos de métodos bloquean el
roadmap. KPIs: Feature Delivery Velocity, Checkout Conversion, funnel/activación,
time-to-launch de métodos nuevos, throughput de experimentos. Ángulo Yuno: capacidades
pre-built + SDKs para shippear sin ingeniería pesada, habilitar métodos/PSPs no-code
(config, no proyecto), one-click y saved cards, A/B testing fácil entre métodos y
routing, analítica de pagos unificada. Libera el roadmap del plumbing de pagos.

## Treasurer
Prioridad: caja, liquidez, settlement, FX y riesgo financiero. Pains: settlement
fragmentado entre múltiples PSPs, timing de settlement lento o impredecible, costos de
FX y cross-border erosionando fondos, conciliación manual, poca visibilidad de caja
entre mercados/monedas, riesgo de contraparte/concentración. KPIs: Cash Flow/Liquidity,
Settlement Time, costos de FX y procesamiento, DSO, precisión de conciliación, Working
Capital. Ángulo Yuno: conciliación y visibilidad de settlement unificadas en un
dashboard, settlement más rápido y predecible, multi-currency + local acquiring para
bajar costo FX/cross-border, una vista en tiempo real del movimiento de dinero para
forecasting, menor dependencia de un solo procesador/banco.

## Head of Payment Operations
Prioridad: el practitioner que corre pagos día a día (a menudo el verdadero champion).
Pains: conciliación y matching de settlements manual, apagar incendios de pagos
fallidos y disputas, chargebacks entre múltiples proveedores, sin un solo lugar para
monitorear approval rates/salud de proveedores, rollout de métodos o PSPs dependiente
de ingeniería, data inconsistente entre PSPs. KPIs: Authorization/Success Rate,
Chargeback & Dispute Rate, tiempo de conciliación, recovery de pagos fallidos, uptime
de proveedores, time-to-add de método/PSP. Ángulo Yuno: un dashboard sobre todos los
procesadores y métodos (approvals, refunds, chargebacks, salud de proveedores) con
monitoreo en tiempo real y alertas proactivas, retries/conciliación/settlement
automatizados, smart routing + failover para subir approvals y recuperar soft declines,
habilitación no-code de métodos/PSPs. Convierte el firefighting en supervisión.

## Head of Fraud / Risk & Compliance
Prioridad: proteger revenue de fraude y chargebacks manteniendo compliance. Pains:
pérdidas por chargebacks y fraude, false declines matando revenue bueno, transacciones
cross-border mal marcadas, muchas herramientas de fraude desconectadas, fricción de 3DS
golpeando conversión, carga de SCA/PCI entre mercados. KPIs: Fraud & Chargeback Rate,
False-decline Rate, Dispute Win Rate, Approval Rate neto de fraude, compliance 3DS/SCA,
costo de fraud ops. Ángulo Yuno: screening de riesgo en tiempo real sobre 50+
herramientas de fraude desde una capa, 3DS agnóstico/optimizado que minimiza fricción,
network tokens + account updater para reducir exposición y fallas silenciosas,
resolución temprana de disputas antes del chargeback, local acquiring para resolver
flags de fraude cross-border. Reduce pérdidas Y sube approvals a la vez.

## COO
Prioridad: eficiencia operativa y escalar la organización sin sumar complejidad. Pains:
demasiados vendors/contratos de pago, operaciones que no escalan con el crecimiento,
sistemas y reporting fragmentados, tiempo de ingeniería y ops drenado por mantenimiento
de pagos, expansión de mercados frenada por el setup de pagos. KPIs: Operating
Margin/Efficiency, Cost per Transaction, Vendor Count, time-to-market de geos nuevas,
automatización de procesos, uptime. Ángulo Yuno: consolidar todos los proveedores en
una plataforma y un contrato, automatizar retries/conciliación/settlement, lanzar
mercados en semanas vía un API, visibilidad operativa unificada, infraestructura
cloud-native escalable para que ops e ingeniería se enfoquen en el core.

## Controller / Head of Finance Ops
Prioridad: el cierre contable, conciliación y precisión de reporting (más granular que
CFO/Treasurer). Pains: conciliación multi-PSP manual que atrasa el cierre de mes,
descuadres entre reportes de procesadores y settlements bancarios, tracking de
refunds/chargebacks entre mercados, spreadsheets propensos a error, sin fuente única de
verdad de data de pagos, complejidad de auditoría. KPIs: Time-to-close, precisión de
conciliación/match rate, volumen de ajustes manuales, tracking de refunds/chargebacks,
audit readiness. Ángulo Yuno: conciliación unificada consolidando todos los
procesadores y métodos en un dashboard con approvals/refunds/chargebacks en tiempo
real, matching automatizado para acelerar el cierre, audit trails centralizados por
mercado, una fuente de verdad para finanzas.
