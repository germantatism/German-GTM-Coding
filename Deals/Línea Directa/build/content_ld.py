# -*- coding: utf-8 -*-
"""Línea Directa proposal: text per element ID on the Drive copy of 'Propuesta - Palco + Yuno' (now 22 slides).
Markup: **x** = bold run of the original element. Numbers come from model.py.
Datos del cliente: email de Luis Paternina (24-sep-2026) y llamada del 30-sep-2026. Pricing: German, 30-sep-2026."""
from model import *
G = 'g3fb7d86b358_4_'
T = {
# S1 cover
'g3c99cf7678e_0_1': 'IMPULSANDO PAGOS SIN FRICCIÓN PARA LÍNEA DIRECTA',
# S5 why partner
'g3caca0138e4_0_2155': 'Por qué creemos que Yuno es el socio ideal para Línea Directa',
'g3caca0138e4_0_2160': 'UN EQUIPO DEDICADO PARA LÍNEA DIRECTA',
'g3caca0138e4_0_2168': 'Cobertura global de proveedores + rieles locales de Colombia y Perú para lanzar y escalar rápido',
# S11 key advantages
'g3c99cf7678e_0_28715': 'Yuno es el socio de pagos para el recaudo digital de Línea Directa',
'g3c99cf7678e_0_28719': 'La cobertura de métodos de pago locales en Colombia y Perú y un checkout listo para su portal de pedidos posicionan a Yuno como el socio ideal para Línea Directa',
'g3c99cf7678e_0_28735': 'Una sola integración para Colombia y Perú',
'g3c99cf7678e_0_28722': 'Checkout alojado por Yuno para recibir tarjetas',
'g3c99cf7678e_0_28726': 'Sus contratos con cada proveedor siguen siendo suyos',
'g3c99cf7678e_0_28731': 'Una subcuenta por país, con reportes y analítica',
# S13 cuatro palancas
G+'74': 'Cuatro palancas sobre su propia data: completar más pagos en el portal es la más grande',
G+'188': f'Sobre **{TX:,} transacciones digitales al mes** ({TX_CO:,} en Colombia y {TX_PE:,} en Perú) y un ticket promedio cercano a **${t_co:.0f} y ${t_pe:.0f}**, Línea Directa recauda por canales digitales cerca de **${tpv/1e6:.0f}M al año.** Cerca del 30% de los pagos todavía se hace en puntos físicos y el portal aún no recibe tarjetas: ahí está el espacio más grande.',
G+'190': 'Palancas de recaudo',
G+'198': 'Pagos en Colombia',
G+'201': '+1% a +2%',
G+'202': 'Hoy el portal recibe PSE, Bancolombia y Nequi, y cerca del 30% de los pagos aún se hace en puntos físicos. Con tarjeta débito y crédito, Daviplata y más métodos en el mismo checkout, quien no logra pagar con uno tiene otro a un clic. Cada pago completado a tiempo es un pedido que alcanza la campaña.',
G+'205': f'**{M(L1[0])}**/año', G+'208': f'**{M(L1[1])}**/año',
G+'210': 'Pagos en Perú',
G+'213': '+1% a +2%',
G+'214': f'En Perú el recaudo digital hoy pasa por Yape: unas {TX_PE:,} transacciones al mes. La subcuenta de Perú suma Plin, PagoEfectivo y tarjeta débito y crédito sobre la misma integración, sin un desarrollo aparte. La lógica es la misma: más formas de pagar, más pagos completados a tiempo.',
G+'217': f'**{M(L2[0])}**/año', G+'220': f'**{M(L2[1])}**/año',
G+'222': 'Costo por transacción',
G+'225': '5 a 10 bps',
G+'226': 'Línea Directa sigue negociando directo con cada proveedor: Yuno no entra en el flujo del dinero. Con el costo de cada método y proveedor en un solo panel, puede priorizar en el checkout los de menor costo y cambiar de proveedor sin desarrollo. Se calibra con las tarifas que nos compartan.',
G+'229': f'**{M(L3[0])}**/año', G+'232': f'**{M(L3[1])}**/año',
G+'234': 'Integraciones',
G+'237': '6 → 1',
G+'238': 'Una sola integración reemplaza las cuatro que hoy mantienen (PSE, Bancolombia/Wompi y Nequi en Colombia; Yape en Perú) y evita construir las de tarjeta en los dos países. El checkout alojado por Yuno mantiene los datos de tarjeta fuera de sus sistemas.',
G+'241': f'**{M(L4[0])}**/año', G+'244': f'**{M(L4[1])}**/año',
G+'246': f'**Supuestos** Volumen base: {TX_CO:,} transacciones digitales al mes en Colombia y {TX_PE:,} en Perú, con el ticket promedio que compartió Línea Directa para cada país llevado a dólares a la tasa oficial: cerca de ${t_co:.0f} y ${t_pe:.0f}, unos ${tpv/1e6:.0f}M al año. Las palancas 1 y 2 miden recaudo digital que entra a tiempo; la 3 es ahorro en tarifas de procesamiento; la 4 es costo de ingeniería evitado. Los rangos de mejora son supuestos de modelación de Yuno, a validar con su data.',
# S14 impacto total
G+'449': 'PAGOS COLOMBIA', G+'452': 'PAGOS PERÚ', G+'455': 'COSTO', G+'458': 'INTEGRACIONES',
G+'462': '**Conservador** +1% de pagos digitales completados',
G+'464': M(L1[0]), G+'466': M(L2[0]), G+'468': M(L3[0]), G+'470': M(L4[0]), G+'472': M(cons),
G+'474': '**Optimista** +2% de pagos digitales completados',
G+'476': M(L1[1]), G+'478': M(L2[1]), G+'480': M(L3[1]), G+'482': M(L4[1]), G+'484': M(opt),
G+'488': M(avg[0]), G+'490': M(avg[1]), G+'492': M(avg[2]), G+'494': M(avg[3]), G+'496': M((cons + opt) / 2),
G+'498': M1(avg[0] + avg[1]), G+'499': 'RECAUDO DIGITAL A TIEMPO',
G+'500': f'Palancas 1 y 2. Pagos que hoy no se completan en el portal o se van a un punto físico. Es recaudo que entra antes y pedidos que alcanzan la campaña, no un ahorro. Rango de {M1(L1[0]+L2[0])} a {M1(L1[1]+L2[1])}.',
G+'502': M(avg[2]), G+'503': 'AHORRO EN PROCESAMIENTO',
G+'504': f'Palanca 3, por llevar cada pago al método y proveedor de menor costo. Ahorro directo sobre las tarifas que Línea Directa negocia. Rango de {M(L3[0])} a {M(L3[1])}.',
G+'506': M(avg[3]), G+'507': 'INGENIERÍA EVITADA',
G+'508': f'Palanca 4, por no construir las integraciones de tarjeta ni mantener las cuatro actuales. Rango de {M(L4[0])} a {M(L4[1])}.',
G+'514': f'**Supuestos** Base: {TX_CO:,} transacciones digitales al mes en Colombia y {TX_PE:,} en Perú, al ticket promedio que compartió Línea Directa para cada país, llevado a dólares a la tasa oficial (TRM de {TRM:,.2f} del 30-sep-2026; tipo de cambio SBS de {SBS:.2f} del 29-sep-2026): cerca de ${t_co:.0f} y ${t_pe:.0f} por transacción, ${tpv/1e6:.0f}M al año. L1 y L2: +1% conservador y +2% optimista de pagos digitales completados, a reemplazar con su tasa de pagos fallidos o abandonados en el portal. L3: 5 a 10 bps sobre ${tpv/1e6:.0f}M, a reemplazar con sus tarifas por método. L4: {NEW} integraciones nuevas (tarjeta en Colombia y en Perú) y {CUR} actuales; 8 a 12 semanas de ingeniería por integración, mantenimiento de 20% a 30% anual y $50K por persona al año. Todos los rangos son supuestos de modelación de Yuno, a validar con su data.',
# S17 pricing
G+'334': f'Una tarifa por transacción que empieza en 6 centavos y baja a 5 con el volumen, con todos los métodos de pago de Colombia y Perú, el checkout alojado por Yuno y las subcuentas por país incluidos, sobre un fee de plataforma fijo de ${PLATFORM:,} al mes.',
G+'626': f'0 a {CUT:,} trx',
G+'629': f'Más de {CUT:,} trx',
G+'646': 'Una integración para Colombia y Perú', G+'647': '**Incluido**',
G+'649': 'Checkout alojado por Yuno (PCI)',
G+'652': 'Cuenta matriz y subcuentas por país',
G+'655': 'Gestión de transacciones',
G+'658': 'Usuarios y roles',
'g3f8ec79a1c3_1_0': 'Ambiente de pruebas (sandbox)',
G+'668': f'**${PLATFORM:,} / mes**',
G+'670': 'LO QUE SIGNIFICA PARA LÍNEA DIRECTA',
G+'671': f'A {TX:,} transacciones exitosas / mes.',
G+'676': f'Tramo 1: {CUT:,} trx × ${P1:.2f}', G+'677': f'${CUT*P1:,.0f}', G+'678': f'${CUT*P1*12:,.0f}',
G+'680': f'Tramo 2: {TX-CUT:,} trx × ${P2:.2f}', G+'681': f'${(TX-CUT)*P2:,.0f}', G+'682': f'${(TX-CUT)*P2*12:,.0f}',
G+'684': f'**Subtotal transacciones ({TX//1000}k)**', G+'685': f'**${var:,.0f}**', G+'686': f'**${var*12:,.0f}**',
G+'688': 'Fee de plataforma', G+'689': f'${PLATFORM:,}', G+'690': f'${PLATFORM*12:,}',
G+'692': 'Métodos de pago de Colombia y Perú', G+'693': 'Incluido', G+'694': 'Incluido',
G+'696': '**Total mensual estimado**', G+'697': f'**${total:,.0f}**', G+'698': f'**${total*12:,.0f}**',
G+'699': f'≈ **${total/TX:.3f}** all-in por transacción exitosa. Baja a medida que crece el volumen.',
G+'700': f'Desglose a {TX:,} ({TX_CO:,} en Colombia y {TX_PE:,} en Perú): {CUT:,} × ${P1:.2f} = ${CUT*P1:,.0f} y {TX-CUT:,} × ${P2:.2f} = ${(TX-CUT)*P2:,.0f}. A 400,000 trx/mes: ${PLATFORM:,} + ${monthly(400_000)[0]:,.0f} = ${monthly(400_000)[1]:,.0f} / mes ≈ ${monthly(400_000)[1]/400_000:.3f} por trx.',
G+'703': 'Una cuenta matriz de Línea Directa con una subcuenta para Colombia y otra para Perú, cada una con sus propios métodos de pago. Línea Directa negocia sus tarifas directo con cada proveedor: Yuno no entra en el flujo del dinero.',
G+'705': '**OPCIONAL · PARA REVISAR DESPUÉS**',
G+'706': 'No incluido en esta propuesta.',
G+'708': 'Orquestación y smart routing',
G+'710': 'Monitores y alertas',
G+'712': 'Network tokens',
G+'713': 'Alcance y precio se revisan juntos en una siguiente fase, cuando Línea Directa lo necesite.',
}
# tranche 2 price: "$0.055/trx" -> "$0.05/trx" by deleting one character (keeps the big number + small suffix runs)
DELETE_CHARS = {G+'630': (5, 6)}
# third tranche row removed (label + price); its separator stays as the closing line of the two-row table
DELETE = [G+'632', G+'633']
# objectId -> (x, y, w, h) pt; None keeps the current value
MOVE = {
 # S13 card titles: wider boxes
 G+'198': (None, None, 110, None), G+'210': (None, None, 110, None), G+'222': (None, None, 112, None),
 # S14 supuestos: taller
 G+'513': (None, None, None, 68), G+'514': (None, None, None, 58),
 # S17 left panel: two rows re-spaced over the height that three rows used
 G+'626': (None, 158, 90, None), G+'627': (None, 153, None, None), G+'628': (None, 189, None, None),
 G+'629': (None, 210, 90, None), G+'630': (None, 205, None, None), G+'631': (None, 241, None, None),
 # S17 middle panel: wider labels, value boxes aligned with the other "Incluido"
 G+'646': (None, None, 140, None), G+'649': (None, None, 140, None), G+'652': (None, None, 140, None),
 G+'655': (None, None, 140, None), G+'658': (None, None, 140, None), 'g3f8ec79a1c3_1_0': (None, None, 140, None),
 G+'647': (391.3, None, 29, None), G+'668': (366, None, 53, None),
 # S17 right panel: wider labels
 G+'676': (None, None, 140, None), G+'680': (None, None, 140, None), G+'684': (None, None, 140, None),
 G+'688': (None, None, 140, None), G+'692': (None, None, 140, None), G+'696': (None, None, 140, None),
 # S17 optional strip
 G+'705': (None, None, 200, None), G+'708': (332, None, 100, None), G+'709': (436, None, None, None),
 G+'710': (449, None, 75, None), G+'711': (528, None, None, None), G+'712': (541, None, 100, None),
}
LOGO = 'https://images.weserv.nl/?url=https://webprdazwpa6f17f2501.blob.core.windows.net/blobwebprdazwpa6f17f2501/wp-content/uploads/2025/03/LogoBig.png&mod=12,0&w=1300&output=png&cx=228&cy=4&cw=844&ch=340'
# (old Palco image id, new id, slide index 0-based is resolved at build time, box)
LOGOS = [(G+'715', 'ld_cover_logo', (119, 19, 62, 25)), (G+'714', 'ld_close_logo', (621, 195, 62, 25))]
FORBID = ['Palco', 'PALCO', 'tenant', 'Tenant', 'TENANT', '235,000', '235k', '$37.09', '$104.6M', '58,750', '117,500', 'Openpay', 'Fiserv',
          '3DS (100k', '20k evaluaciones', '$7,000', '$12,044', '$19,044', '$23,404', 'GLOBALES PARA', 'conciliación y token vault',
          'Risk conditions', 'SEGURIDAD Y RIESGO', ' — ', ' - ']
