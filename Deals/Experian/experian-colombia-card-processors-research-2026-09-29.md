# Experian | Procesadores de tarjetas en Colombia: verificación de la lista (29-sep-2026)

**Para qué:** German prometió a Experian una lista de los procesadores con mejor performance en Colombia, como alternativas a PayU para tarjetas. Este archivo verifica la lista que German pasó contra fuentes públicas y contra lo que Yuno publica como integrado.

**Conclusión corta:** la lista original no se puede enviar tal cual. Tres de las cinco tarifas no coinciden con lo publicado, las tasas de aprobación no tienen fuente, y dos de los procesadores no son un fit para Experian. No existe dato público de tasa de aprobación por procesador en Colombia; el único dato real de "mejor performance" sería el benchmark interno de Yuno (pedirlo a Daniel o a datos).

## 1. Verificación por procesador

| Procesador | Dato de la lista | Verificación | Fuente |
|---|---|---|---|
| Wompi | 2.65% + $700 + IVA | ✅ Coincide. Tarifa plana del Plan Avanzado para todos los medios. Existe además Plan Gateway sin costo de Wompi, donde el comercio negocia directo con cada medio de pago | soporte.wompi.co |
| Wompi | "PSE con los 23 bancos" | ⚠️ Número sin verificar | |
| Wompi | Tokenización y recurrencia | ✅ Wompi tokeniza tarjetas y Nequi para cobros automáticos | wompi.com, docs.wompi.co |
| PayU | 3.29% + $300 y 3.49% + $300 recurrente | ⚠️ Sin fuente oficial. Blogs citan 3.29% + $300 y también 3.49% + $900. La página de tarifas de PayU Colombia ahora redirige a Rapyd | tiendanube.com |
| PayU | "Estándar de facto" | ⚠️ Opinión. Además es el procesador del que Experian quiere alternativas | |
| Mercado Pago | 3.49% + $500 crédito, 1.99% + $500 débito, PSE 1.79% | ❌ No coincide. Fuentes 2026 citan cerca de 3.99% + IVA crédito y 3.49% + IVA débito y PSE. Página oficial bloqueada para verificar | guiadebancos.com, mentoracolombia.com |
| Bold | 2.99% + $900 crédito, 1.79% débito, Nequi 1.50%, PSE 1.30% | ❌ No coincide. Fuentes 2026 citan 2.89% datáfono y PSE, 3.29% link de pago | ayuda.bold.co (título), mentoracolombia.com |
| ePayco | 2.99% + $900 + IVA | ❌ Desactualizado. Tarifa publicada: 2.64% + $690 + IVA (Davivienda) y 3.29% + $700 + IVA (otros bancos) | epayco.com/tarifas |
| EBANX | 2M+ transacciones al mes en Colombia con network tokens, +10 pp de aprobación, hasta 86% menos declines por fraude | ✅ Coincide con el comunicado del 11-dic-2025. Son datos internos de EBANX en contexto cross-border | business.ebanx.com |

## 2. Lo que no se pudo verificar

- **Tasas de aprobación promedio** (local 70 a 90%, cross-border 30 a 50%, recurrente doméstico 85 a 90%, etc.): sin fuente pública. No enviar al cliente.
- **Spread de 10 a 25 pp entre adquirentes para el mismo BIN:** sin fuente pública.
- **Mix de pagos en e-commerce** (PSE ~45%, wallets ~25%, tarjetas ~22%, efectivo ~8%): las fuentes se contradicen. PCMI cita PSE con 63.1% en el primer trimestre de 2025; la CCCE cita tarjetas con más de 60% de participación. No usar.
- **Penetración de tarjeta de crédito ~35% de adultos** y los datos de **3DS**: sin verificar.

## 3. Bre-B

- ✅ Lanzamiento completo en octubre de 2025.
- ✅ 108 millones de llaves (La República, vía Banco de la República) y 5 millones de transacciones diarias. Cifras más recientes hablan de más de 110 millones de llaves y casi 8 millones de transacciones diarias.
- **Cobro recurrente:** según prensa de mayo y julio de 2026, la función de pagos recurrentes todavía no está integrada en el ecosistema oficial de Bre-B. La ofrecen terceros sobre las llaves. No encontré anuncio oficial del Banco de la República con fecha.
- **DRUO:** fintech colombiana que desde el 5-may-2026 habilita débito automático sobre llaves Bre-B, y que hace débito directo desde cuentas bancarias vía API. Su comunicado no nombra bancos específicos. Toca las prioridades 1 y 3 de Experian. **No sé si Yuno lo tiene integrado ni si es el tercero que se está evaluando.** Validar con Daniel.
- **Yuno y PayRetailers:** alianza anunciada el 24-sep-2026; en Colombia cubre Bre-B y PSE.

## 4. PayU y la adquisición

Rapyd cerró la compra de PayU GPO (LatAm y África) el 14-mar-2025 por US$610 millones. Es la adquisición a la que se refería Cristian. No mencionar la caída de efectividad en correos.

## 5. Qué tiene Yuno integrado en Colombia (según páginas públicas de Yuno)

| Procesador | Evidencia |
|---|---|
| Wompi | Mostrado en el marketplace durante la demo; mencionado en docs de Yuno |
| PayU | Página de partner en y.uno; mostrado en la demo |
| Redeban | Página de partner en y.uno y página en docs.y.uno |
| Kushki | Página de partner en y.uno; alianza pública Yuno y Kushki |
| Mercado Pago | Mencionado en docs de Yuno (Headless SDK) |
| ePayco | Página de partner en y.uno |
| Nuvei, dLocal | Mencionados en páginas de Yuno |
| Credibanco | Sin confirmación pública. Se usó como ejemplo de ruteo en la demo de UNICEF |
| Bold, DRUO | Sin evidencia |

⚠️ Estas páginas confirman que la conexión existe, no que cada una soporte cobro recurrente (MIT) en Colombia a través de Yuno. Confirmar con Daniel.

## 6. Lista recomendada para Experian

Experian es una entidad local, con cobro recurrente de tarjetas y volumen grande. Criterios: procesamiento local, soporte de recurrencia, conectado a Yuno.

1. **Wompi:** ya lo tienen contratado para Bancolombia, Nequi y Daviplata. Activar tarjetas ahí es lo más rápido.
2. **Redeban:** red de pagos colombiana.
3. **Mercado Pago:** procesamiento local de tarjetas con cobros recurrentes.
4. **Kushki:** plataforma regional con procesamiento local.

**Fuera de la lista y por qué:**
- **PayU:** es el procesador actual.
- **Bold:** enfocado en datáfono y link de pago para comercios pequeños; sin evidencia de integración con Yuno.
- **dLocal y EBANX:** pensados para comercios internacionales sin entidad local. Experian tiene entidad en Colombia.
- **ePayco:** conectado a Yuno, pero orientado a pymes. Tiene tarifa preferencial para tarjetas Davivienda; podría sumarse si German lo ve útil.
- **Tarifas:** se dejaron fuera del correo. Las públicas son de lista para comercios pequeños y Experian negocia por volumen.

## Fuentes

- https://soporte.wompi.co/hc/es-419/articles/360020957133--Cu%C3%A1les-son-los-planes-y-tarifas-que-maneja-la-plataforma-Wompi
- https://docs.wompi.co/en/docs/colombia/fuentes-de-pago/
- https://epayco.com/tarifas/
- https://www.tiendanube.com/blog/como-cobrar-online-con-payu/
- https://mentoracolombia.com/pasarelas-de-pago-colombia-2026-comisiones-wompi-bold-mercadopago/
- https://www.guiadebancos.com/ar/blog/comisiones-mercado-pago-latam-2026
- https://business.ebanx.com/en/press-room/press-releases/ebanx-drives-the-next-phase-of-credit-cards-in-latam-with-network-tokenization-for-cross-border-transactions
- https://www.rapyd.net/company/news/press-releases/rapyd-completes-acquisition-of-payu-latin-america-and-africa/
- https://www.banrep.gov.co/es/noticias/la-republica-el-despliegue-de-bre-b-desde-su-lanzamiento-ya-tiene-108-millones-de-llaves-registradas
- https://www.infobae.com/colombia/2026/05/06/bre-b-disparo-sus-transacciones-en-colombia-y-ya-mueve-hasta-5-millones-de-operaciones-diarias/
- https://www.elheraldo.co/economia/2026/05/14/llaves-bre-b-ahora-serviran-para-pagos-recurrentes/
- https://www.vanguardia.com/colombia/2026/07/22/colombia-avanza-hacia-los-pagos-automaticos-bre-b-habilitara-debitos-recurrentes-sin-tarjetas/
- https://druo.com/es-co/sala-de-prensa/druo-habilita-debito-automatico-para-llaves-bre-b-en-colombia/
- https://docs.y.uno/docs/redeban
- https://www.y.uno/partner/kushki
- https://y.uno/partner/epayco
- https://y.uno/pt-br/partner/payu
- https://docs.y.uno/docs/headless-sdk-payment
