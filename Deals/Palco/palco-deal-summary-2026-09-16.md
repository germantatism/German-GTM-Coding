# Palco + Yuno: resumen del deal antes de la propuesta (2026-09-16)

Recopilado de: thread de Gmail "Palco + Yuno - Próximos Pasos" (31-jul a 16-sep), Gong (1 call: deep dive 15-sep), Fireflies de Magdalena (demo 9-sep, solo auto-resumen), transcript local del 15-sep, briefs del 9 y 15-sep, research del 8-sep, DM de Slack con Carlos Medina, calendario y Drive. Sin números por pedido de German; la data vive en el correo de Patricio del 2-sep y en la hoja "Yuno — Pricing Palco" en Drive.

## 1. Quién es Palco y quién decide

- Palco (ex Palco4, pal.co): plataforma white-label de ticketing B2B, sede legal en Madrid, operación fuerte en México y LatAm. Vende a promotores, recintos y partners locales por país, que abren su propia tienda con tecnología de Palco.
- Comprada en oct/nov 2025 por Bocel Private Equity junto a Patricio Villalobos y Miguel Ramírez Lombana (mexicanos). Mandato de expansión LatAm. Es una empresa con dueño-operador en la sala y con presión de crecimiento.
- Construyeron in-house una capa propia con más de 50 integraciones de pasarelas en 18 mercados y la venden como feature. Alfonso Uribarri es el co-fundador que la construyó. Nunca decirles que "les falta orquestador".

Personas:
- Patricio Villalobos Cuevas, CEO y co-dueño, opera desde Madrid. Es quien decide build vs Yuno. Informal, rápido, escribió él mismo la agenda técnica de 6 puntos. El 16-sep escribió "looking fwd man a la propuesta".
- Miguel Ramírez Lombana (mike@pal.co), co-dueño. Estuvo un momento en la call del 9-sep. Tentativo para el 21-sep. Fernando lo considera relevante para lo comercial.
- Fernando Nava Feldman, firma como Technical Account Manager, Palco México (CDMX); Patricio lo presentó como VP of Engineering. Coordina agendas y es quien más quiere las integraciones de métodos de pago sin construirlas.
- Alfonso Uribarri, co-fundador, Manager of Development and Support (Madrid). Dueño de las 50+ integraciones. Fue quien más habló el 15-sep y quien corrigió el modelo de negocio. Cerró con "me ha gustado bastante".
- Álvaro García Torres (alvaro@pal.co), estuvo el 15-sep, rol no confirmado.
- Javier Sánchez, SSE. Fuera de oficina del 14-sep a fin de mes. Fuera del cc.
- Por Yuno: Magdalena Torrealba abrió la relación (call 30-jul, sin grabación) y pidió la data; German lleva el deal desde el 4-sep; Carlos Medina (Implementation Engineer) hizo la demo del 15-sep; Joaquin Mann (BDM NA, se unió la semana del 7-sep) acompaña; Saman Mortazavi fue mencionado como "manager en México" en julio pero no ha participado; Susana Awad estuvo en cc y nunca respondió invitaciones.

## 2. Cronología

| Fecha | Qué pasó |
|---|---|
| 30-jul | Primera call Magdalena + Patricio. Se habló de un piloto. Sin grabación ni transcript. |
| 31-jul | Magdalena pide volumen, ticket promedio, TPV, mix, países, aprobación por método, fraude/contracargos. Menciona a Saman como manager en México y "preparar una propuesta para el piloto que discutimos". |
| 18-ago | Patricio se disculpa, estaba de vacaciones. |
| 2-sep | Patricio manda la data completa de la plataforma (volumen, mix, países, aprobación por procesador, fraude) y sus 6 preguntas. Dice que "septiembre es cuando estaremos definiendo el camino a seguir en nuestro orquestamiento de pagos". Es el evento central del deal. |
| 4-sep | Magdalena agradece, reenvía a German, propone el mié 9. |
| 7-sep | Patricio confirma, manda invite, "bienvenido German al equipo". |
| 9-sep | Demo + payment orchestration review (Patricio, Fernando, Javier; Magdalena, German). Grabó Fireflies de Magdalena, no Gong. Solo existe el auto-resumen: se habló de Openpay y Mercado Pago, de procesar local en Bolivia y Venezuela, de merchant of record y tokens, se mostraron casos de éxito y el dashboard, y se acordó un deep dive de producto. |
| 10-sep | German propone 3 horarios para sesión técnica. Fernando: "dame la oportunidad de coordinar con el equipo". |
| 14-sep | German hace ping. Fernando pide el martes 10:00 COT. Invite enviado; Fernando suma a Alfonso y Álvaro. |
| 15-sep | Deep dive técnico (48 min, en Gong). Carlos demo del dashboard. German envía follow-up el mismo día con sandbox, docu y 4 opciones para la propuesta. Fernando elige lunes 21 11:00 COT. |
| 16-sep | Patricio: "looking fwd man a la propuesta". Invite "Palco + Yuno | Propuesta" aceptado por Patricio, Fernando y Alfonso; Miguel tentativo; Joaquin dentro. Magdalena y Carlos no están en esa invitación. German y Joaquin bloquearon tarde de trabajo interno "Propuesta PALCO" (13:15 a 15:00). |
| 21-sep | Reunión de propuesta comercial, 11:00 COT (10:00 CDMX, 18:00 Madrid), 45 min. |

## 3. Cómo opera Palco (lo que ellos mismos dijeron)

- Escrito por Patricio (2-sep): cada tenant es merchant of record y gestiona fraude y contracargos directo con su procesador. No tienen dato consolidado de fraude. Eso es una de las razones para centralizar la capa de pagos.
- Corregido por Alfonso (15-sep): las cuentas de procesamiento son de sus clientes, no de Palco. Buscan un partner por país (dueño de la cuenta, con contactos con promotores y recintos) que distribuye el producto. El cliente recauda y liquida mensualmente a Palco. Palco cobra fee por ticket o, con volumen, precio fijo por evento. Los tickets son del cliente; Palco es la capa de tecnología. Palco quiere cuentas propias en México y Europa "eventualmente".
- Sus clientes se autoconfiguran: ponen sus propias llaves de las pasarelas sin intervención de Palco. Por eso preguntaron si las credenciales se cargan por API (sí, existe la organization API).
- Están yendo hacia clientes nuevos: grandes recintos y clubes deportivos, donde Palco sí podría ir con comercio propio y marca blanca. A los partners locales actuales, que reciben el dinero directo, es difícil cambiarles el esquema.
- Integrarían en un 90% vía SDK.
- Ya diagnosticaron su problema: la aprobación de tarjeta en México cae fuerte según el procesador, y lo que esperan resolver con Yuno es "ruteo inteligente y reintentos". No hay que venderles el concepto, hay que probar ejecución y ponerle precio.

## 4. Lo que pidieron (la agenda real)

Las 6 preguntas escritas de Patricio (2-sep):
1. Split payments en México: qué procesadores soportan split de comisión al momento del cobro, con el tenant como MoR y Palco reteniendo su fee.
2. 3DS obligatorio en todos los flujos de tarjeta y cómo impacta la aprobación con el ruteo.
3. Tokenización y cargos recurrentes para abonos y suscripciones con procesadores mexicanos.
4. Modelo comercial multi-tenant: cómo se contrata y factura por tenant.
5. Integración vía API directa (no SDK embebido) y el alcance PCI resultante para Palco.
6. Procesamiento por BIN único de banco para preventas especiales.

Lo que sumaron el 15-sep:
- Acceso a integraciones de métodos de pago sin tener que construirlas (Fernando: "el principal objetivo", "cuello de botella sumamente costoso").
- Jugar con la pasarela según condiciones de la tarjeta y tasa de intercambio: más restrictiva donde hay riesgo, más margen donde no.
- Cargar credenciales de sus clientes por API.
- Split de pagos: fee de comisión a una cuenta, precio del ticket a otra.
- Fallback cuando una pasarela rechaza, incluyendo métodos con redirección.
- Panel de actividad en tiempo real por cuenta para on-sales (picos muy altos en ventanas cortas).
- Cómo cobra Yuno: por transacción, por volumen de dinero, mensual.
- Documentación de API y SDK, y sandbox.

## 5. Lo que Yuno ya mostró y prometió

Mostrado por Carlos el 15-sep: organización con subcuentas por merchant, cada una con su propio routing; perfiles y permisos; auditoría; catálogo de conexiones y credenciales por dashboard o por API (organization API, get de catálogo + post de conexión); costos por procesador para que el smart routing optimice por costo; rutas con condiciones (marca, BIN, país, monto, installments, CVV, metadata ilimitada), evaluación de arriba hacia abajo; rutas de rechazo y error hacia otro proveedor (el comprador nunca ve el rechazo intermedio); split de tráfico por porcentaje; smart routing por conversión + latencia o conversión + costo, automático o manual; monitores con alertas y redistribución automática de tráfico; antifraude y 3DS en el catálogo; checkout builder por cuenta con varios checkouts; operaciones con línea de tiempo por transacción y "ver ruta"; insights por proveedor, condición, issuer, primer intento vs reintento.

Prometido en la call y en el correo del 15-sep (enviado):
- Sandbox: Carlos envió invitación con Fernando como usuario principal, cc Alfonso y Álvaro. Hecho.
- Documentación SDK (Full Checkout Web) y API reference. Enviada en el correo.
- Propuesta comercial inicial para revisar el 21-sep. Tal como quedó escrito en el correo: "Inicialmente, veremos a Yuno como una solución directa para sus clientes actuales".
- Split marketplace: Carlos explicó que Yuno propaga la instrucción de split al PSP que lo soporta y el PSP dispersa. Queda por confirmar qué procesadores mexicanos lo soportan en la dirección de Palco (tenant cobra, Palco retiene al capturar).
- Métodos con redirección: fallback solo si falla la creación de la redirección; si el usuario es rechazado ya redirigido, debe reiniciar la compra.

## 6. Los dos modelos comerciales sobre la mesa

German los puso en la call del 15-sep:
- Marca blanca: Palco ofrece a sus clientes la plataforma completa de Yuno bajo su marca. Fee fijo más variable por volumen.
- Solo conexión: Palco se conecta a Yuno para acceder a todas las integraciones y al routing; lo demás depende de ellos. Solo variable por volumen procesado.

Lectura de Alfonso: marca blanca con comercio propio de Palco tiene sentido para clientes nuevos grandes (recintos, clubes) y para clientes con poca soltura técnica. Los partners locales actuales son difíciles de mover porque reciben el dinero directo. Entiende que agrupar todo bajo Palco da mejor tasa que cada cliente por separado. German confirmó que la relación es con Palco (cuenta grande) y subcuentas por cliente; Yuno no va a donde los clientes de Palco.

Lectura interna (Carlos, Slack 15-sep): "los vi bien, interesados". Sugiere que la fase 1 sea la más sencilla: que usen a Yuno para crear conexiones y routing, como un proveedor, con el checkout de sus merchants sobre nuestro SDK. Ningún rollo de integración. German: "lo veo igual".

## 7. Fricciones, objeciones y riesgos

- Costo trasladado al cliente final: Alfonso lo dijo dos veces. Sus clientes eligen pasarela por precio, no por seguridad. Cualquier costo adicional (Yuno, 3DS, scoring) es barrera de entrada. Esperan que el ahorro por ruteo compense. Es la objeción central de la propuesta.
- Alcance: el beneficio de aprobación se lo lleva el tenant (es MoR), no Palco. La propuesta tiene que mostrar cómo Palco gana con esto (nueva línea de ingreso o argumento de venta), no solo cuánto cuesta.
- Competidor real: su propio roadmap interno. Patricio dijo que septiembre define el camino de su orquestación.
- Alfonso es el constructor de las integraciones. "Reemplazar" lo pierde. El frame que funciona: ustedes construyeron la parte difícil, nosotros la mantenemos viva y le ponemos el cerebro encima.
- Sensibilidad de precio: en la call German dio un fee mínimo mensual de referencia y Alfonso ya se armó un rango en la cabeza. Ese número es distinto al modelado internamente. Hay que decidir cuál se presenta antes del 21.
- Datos que no cuadran: el ticket promedio que mandó Patricio parece ser por ticket, y cada orden lleva varios tickets; la tabla mensual por país omite España, Puerto Rico y Panamá. Cambia el take rate del pricing. Nadie lo ha preguntado aún.
- PCI: si van por API directa con PAN en su front, cargan scope completo. No se encontró attestation pública. Con SDK no lo necesitan.
- Métodos con redirección: no hay fallback post-rechazo; a Alfonso le importaba.
- Ventanas horarias: Patricio y Alfonso en Madrid, Fernando en CDMX. 11:00 COT = 18:00 Madrid.
- Gente fuera: Javier OOO hasta fin de mes. Magdalena y Carlos no están en la invitación del 21.

## 8. Cabos sueltos que la propuesta del 21-sep debe cerrar

1. Modelo: presentar solo conexión directa (lo que dice el correo) o ambos modelos (lo que se habló en la call). Decidir.
2. Estructura de precio que se sostenga frente a "el cliente final no paga más": fee fijo vs variable, cómo se reparte si Palco lo absorbe o lo empaqueta a sus tenants.
3. Reconciliar el volumen real (ticket vs orden) antes de cerrar números. Preguntarlo a Patricio o Fernando antes del lunes.
4. Alineación del número dicho en la call vs el modelo interno.
5. Piloto: alcance sugerido México sobre los rails de tarjeta con peor aprobación, baseline y fecha de revisión. Nadie lo ha propuesto formalmente aún.
6. Respuestas pendientes de Carlos: split al capturar por procesador mexicano con tenant MoR; recurrencia con procesadores mexicanos; cobertura de catálogo para sus procesadores (Openpay, Banorte, Santander, Mercado Pago, Redsys, Cybersource, Authorize.net, Fiserv) y ausencias probables (Line VE, Pixel Pay HN, Recurrente GT, Bancard PY, UepaPay DR, ECI ES).
7. Referencia de marketplace (GoFundMe) solo con permiso.
8. Quién presenta el 21: German + Joaquin están; definir si Magdalena y Carlos entran.

## Fuentes

- Gmail thread "Palco + Yuno - Próximos Pasos" (id 1a06e21d4b5dc7d3), 15 mensajes del 4-sep en adelante con la historia citada desde el 31-jul.
- Gong: call 891469394762814345 (deep dive 15-sep). Gong tiene dos cuentas CRM: "Palco" (001Ps00001qNjCWIA0, solo emails) y "Palco4" (001Ps00001VqkdvIAB, con la call).
- Fireflies de Magdalena: "Yuno / PALCO - Demo & Payment Orchestration Review" (9-sep), solo auto-resumen.
- Transcript local: Deals/Palco/palco-call-transcript-2026-09-15.md.
- Briefs: data/research/palco-meeting-brief-2026-09-09.md y palco-meeting-brief-2026-09-15.md (Google Docs equivalentes en Drive).
- Research: data/research/palco-ticketing-2026-09-08.md.
- Pricing: hoja "Yuno — Pricing Palco" en Drive (carpeta Palco).
- Slack: DM German + Carlos Medina, 14 y 15-sep.
- Calendario: "Palco + Yuno | Propuesta" lun 21-sep 11:00 a 11:45 COT; "Propuesta PALCO" (interno, mié 16-sep 13:15 a 15:00).
