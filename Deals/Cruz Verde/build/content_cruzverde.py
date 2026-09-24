# -*- coding: utf-8 -*-
"""Cruz Verde proposal: text per element ID on the copy of 'Propuesta - Palco + Yuno' (21 slides).
Base de modelación (datos reportados por Cruz Verde, call 21-may-2026 + calculator de Alejandro 24-sep):
100,000 tx/mes, ticket $20, TPV $2.0M/mes ($24M/año), aprobación 91% sin reintentos, fraude <0.05%, PSE 58% de ventas,
Mercado Pago único proveedor. Pricing (German 24-sep): platform $7,500 + tramos $0.06 / $0.04 / $0.035 + conciliación $2,000 flat."""
Q='¿POR QUÉ YUNO?'
BR='\x0b'
T = {
# S1 cover
'g3c99cf7678e_0_1': 'IMPULSANDO PAGOS SIN FRICCIÓN PARA CRUZ VERDE',
# S5 why partner
'g3caca0138e4_0_2155': 'Por qué creemos que Yuno es el socio ideal para Cruz Verde',
'g3caca0138e4_0_2160': 'UN EQUIPO DEDICADO PARA CRUZ VERDE',
'g3caca0138e4_0_2168': 'Cobertura global de proveedores + rieles locales de Colombia para lanzar y escalar rápido',
# S6 four pillars (sin IA, suscripciones ni network tokens)
'g3f8b4c413fe_1_2569': 'Una suite completa · Cuatro pilares · Un solo panel',
'g3f8b4c413fe_1_2571': 'Diseñada para escalar con su volumen, con visibilidad completa de cada proveedor y cada ruta',
'g3f8b4c413fe_1_2582': 'Todo en un solo lugar', 'g3f8b4c413fe_1_2583': 'INSIGHTS Y OPERACIONES',
'g3f8b4c413fe_1_2608': 'Métodos de pago locales', 'g3f8b4c413fe_1_2609': 'PSE, Nequi, Daviplata y tarjetas.',
'g3f8b4c413fe_1_2623': 'Reintentos inteligentes', 'g3f8b4c413fe_1_2624': 'Recupera rechazos recuperables en otra ruta.',
'g3f8b4c413fe_1_2632': 'Reportes exportables', 'g3f8b4c413fe_1_2633': 'Transacciones de todos los\nproveedores en un solo archivo.',
# S7 suite (sin suscripciones ni network tokens)
'g3caca0138e4_0_2204': 'Tokenización en bóveda PCI',
'g3caca0138e4_0_2205': 'para guardar tarjetas seguras y usarlas con cualquier proveedor',
'g3caca0138e4_0_2208': 'SDKs web y móviles',
'g3caca0138e4_0_2209': 'para integrar una sola vez en web, iOS y Android',
# S11 key advantages
'g3c99cf7678e_0_28715': 'Yuno es el socio de pagos para escalar a Cruz Verde',
'g3c99cf7678e_0_28719': 'La cobertura de métodos de pago locales y las capacidades líderes en ruteo y orquestación posicionan a Yuno como el socio ideal para Cruz Verde',
'g3c99cf7678e_0_28735': 'Una sola integración para Mercado Pago y cada proveedor que sumen',
'g3c99cf7678e_0_28722': 'Sus contratos con cada proveedor siguen siendo suyos',
'g3c99cf7678e_0_28726': 'Monitores con redistribución automática de tráfico cuando PSE o un proveedor falla',
'g3c99cf7678e_0_28731': 'Reportes y conciliación de todos los proveedores',
# S13 cuatro palancas
'g3fb7d86b358_4_74': 'Cuatro palancas sobre su propia data: aprobación y continuidad de PSE son las más grandes',
'g3fb7d86b358_4_188': 'Sobre 100,000 transacciones al mes y un ticket promedio de $20, Cruz Verde procesa cerca de $24M al año con un solo proveedor. PSE es el 58% de sus ventas y la aprobación es de 91%: ahí están las dos brechas más grandes.',
'g3fb7d86b358_4_198': 'Aprobación de pagos',
'g3fb7d86b358_4_201': '91% → 92.5%',
'g3fb7d86b358_4_202': 'Cruz Verde aprueba el 91% de sus intentos con fraude por debajo de 0.05%: la mayoría de los rechazos son técnicos o del emisor, no fraude. Reintentar en una segunda ruta, reglas de riesgo afinadas y reintentos automáticos recuperan parte de esos 9 de cada 100 intentos.',
'g3fb7d86b358_4_205': '$0.40M/año', 'g3fb7d86b358_4_208': '$0.79M/año',
'g3fb7d86b358_4_210': 'Continuidad de PSE',
'g3fb7d86b358_4_213': '4 a 8 h/mes',
'g3fb7d86b358_4_214': 'PSE es el 58% de sus ventas, cerca de $1,600 por hora, y hoy depende de una sola conexión que falla. Monitores con redistribución automática mueven el tráfico a un segundo proveedor de PSE en lugar de perderlo mientras dura la caída.',
'g3fb7d86b358_4_217': '$76K/año', 'g3fb7d86b358_4_220': '$153K/año',
'g3fb7d86b358_4_222': 'Costo de procesamiento',
'g3fb7d86b358_4_225': '10 a 20 bps',
'g3fb7d86b358_4_226': 'Rutear cada transacción al proveedor más barato a igual aprobación, sobre cerca de $24M de TPV al año. Con un solo proveedor no hay con quién comparar; con dos o más, Yuno elige por costo. Se calibra con las tarifas de Mercado Pago que nos compartan.',
'g3fb7d86b358_4_229': '$24K/año', 'g3fb7d86b358_4_232': '$48K/año',
'g3fb7d86b358_4_234': 'Operación de pagos',
'g3fb7d86b358_4_237': '1 a 2 FTE',
'g3fb7d86b358_4_238': 'Conciliación automática entre proveedores y nuevos métodos o proveedores activados desde el dashboard, sin desarrollo. Libera al equipo de ecommerce y TI del trabajo manual de conciliar y de cada integración nueva.',
'g3fb7d86b358_4_241': '$50K/año', 'g3fb7d86b358_4_244': '$100K/año',
'g3fb7d86b358_4_246': 'Supuestos  Volumen base: 100,000 transacciones al mes y ticket promedio de $20, cerca de $24M al año, según lo compartido por Cruz Verde. Aprobación de 91% sin reintentos, fraude menor a 0.05% y PSE como 58% de las ventas, según su equipo. Las palancas 1 y 2 miden ventas recuperadas; la 3 es ahorro en tarifas de procesamiento; la 4 es ahorro operativo. Los rangos de mejora son supuestos de modelación de Yuno, a validar con su data.',
# S14 impacto total
'g3fb7d86b358_4_449': 'APROBACIÓN', 'g3fb7d86b358_4_452': 'CONTINUIDAD PSE',
'g3fb7d86b358_4_455': 'COSTO', 'g3fb7d86b358_4_458': 'OPERACIÓN',
'g3fb7d86b358_4_462': 'Conservador  91% → 92.5% de aprobación',
'g3fb7d86b358_4_464': '$0.40M', 'g3fb7d86b358_4_466': '$76K', 'g3fb7d86b358_4_468': '$24K',
'g3fb7d86b358_4_470': '$50K', 'g3fb7d86b358_4_472': '$0.55M',
'g3fb7d86b358_4_474': 'Optimista  91% → 94% de aprobación',
'g3fb7d86b358_4_476': '$0.79M', 'g3fb7d86b358_4_478': '$153K', 'g3fb7d86b358_4_480': '$48K',
'g3fb7d86b358_4_482': '$100K', 'g3fb7d86b358_4_484': '$1.09M',
'g3fb7d86b358_4_488': '$0.59M', 'g3fb7d86b358_4_490': '$114K', 'g3fb7d86b358_4_492': '$36K',
'g3fb7d86b358_4_494': '$75K', 'g3fb7d86b358_4_496': '$0.82M',
'g3fb7d86b358_4_498': '$0.71M', 'g3fb7d86b358_4_499': 'VENTAS RECUPERADAS · CRUZ VERDE',
'g3fb7d86b358_4_500': 'Palancas 1 y 2. Ventas que hoy se pierden por rechazos y por caídas de PSE, y que entran directo a Cruz Verde. Rango de $0.47M a $0.94M.',
'g3fb7d86b358_4_502': '$36K', 'g3fb7d86b358_4_503': 'AHORRO EN PROCESAMIENTO',
'g3fb7d86b358_4_504': 'Palanca 3, por ruteo de menor costo a igual aprobación. Ahorro directo sobre las tarifas que hoy paga a un solo proveedor. Rango de $24K a $48K.',
'g3fb7d86b358_4_506': '$75K', 'g3fb7d86b358_4_507': 'AHORRO OPERATIVO · CRUZ VERDE',
'g3fb7d86b358_4_508': 'Palanca 4, por dejar de conciliar a mano y de integrar cada método nuevo. Rango de $50K a $100K.',
'g3fb7d86b358_4_514': 'Supuestos  Base: 100,000 transacciones al mes × $20 = $2.0M al mes, $24M al año. L1: aprobación de 91% sin reintentos según Cruz Verde, cerca de 110,000 intentos al mes; +1.5 pp conservador y +3 pp optimista, supuesto de modelación de Yuno. L2: PSE es el 58% de las ventas, cerca de $1,600 por hora; 4 a 8 horas al mes de indisponibilidad o degradación, a reemplazar con su registro de incidentes. L3: 10 a 20 bps sobre $24M de TPV, supuesto de modelación de Yuno, a reemplazar con sus tarifas actuales. L4: 1 a 2 FTE de ecommerce y TI dedicados a conciliación e integraciones, a $50K por persona al año, supuesto de modelación de Yuno. Rangos a validar con su data.',
# S16 pricing
'g3fb7d86b358_4_334': 'Una tarifa por transacción que empieza en 6 centavos y baja con el volumen, con orquestación, smart routing, monitores y reportes incluidos, sobre un fee de plataforma fijo de $7,500 al mes más conciliación a tarifa fija de $2,000.',
'g3fb7d86b358_4_626': '0 a 25,000 trx', 'g3fb7d86b358_4_627': '$0.06/trx',
'g3fb7d86b358_4_629': '25,001 a 50,000 trx', 'g3fb7d86b358_4_630': '$0.04/trx',
'g3fb7d86b358_4_632': 'Más de 50,000 trx', 'g3fb7d86b358_4_633': '$0.035/trx',
'g3fb7d86b358_4_658': 'Usuarios y roles',
'g3f8ec79a1c3_1_0': 'Conciliación', 'g3f8ec79a1c3_1_1': '$2,000 / mes',
'g3fb7d86b358_4_668': '$7,500 / mes',
'g3fb7d86b358_4_670': 'LO QUE SIGNIFICA PARA CRUZ VERDE',
'g3fb7d86b358_4_671': 'A 100,000 transacciones exitosas / mes.',
'g3fb7d86b358_4_676': 'Transacciones exitosas (100k)', 'g3fb7d86b358_4_677': '$4,250', 'g3fb7d86b358_4_678': '$51,000',
'g3fb7d86b358_4_681': '$7,500', 'g3fb7d86b358_4_682': '$90,000',
'g3fb7d86b358_4_685': '$11,750', 'g3fb7d86b358_4_686': '$141,000',
'g3fb7d86b358_4_688': 'Conciliación (tarifa fija)', 'g3fb7d86b358_4_689': '$2,000', 'g3fb7d86b358_4_690': '$24,000',
'g3fb7d86b358_4_692': 'Monitores, reintentos y reportes', 'g3fb7d86b358_4_693': 'Incluido', 'g3fb7d86b358_4_694': 'Incluido',
'g3fb7d86b358_4_696': 'Total mensual estimado', 'g3fb7d86b358_4_697': '$13,750', 'g3fb7d86b358_4_698': '$165,000',
'g3fb7d86b358_4_699': '≈ $0.118 all-in por transacción exitosa en pagos; ≈ $0.138 con conciliación. Baja a medida que crece el volumen.',
'g3fb7d86b358_4_700': 'Desglose a 100,000: 25,000 × $0.06 = $1,500, 25,000 × $0.04 = $1,000 y 50,000 × $0.035 = $1,750. A 150,000 trx/mes: $7,500 + $6,000 = $13,500 / mes ≈ $0.090 por trx en pagos.',
'g3fb7d86b358_4_703': 'Sin costos de implementación. Mercado Pago sigue como su proveedor, conectado a través de Yuno. Sumar otro proveedor de PSE, métodos locales o un adquirente es un cambio de ruteo, no un desarrollo.',
'g3fb7d86b358_4_706': 'Opcional, según consumo y sin mínimos.',
'g3fb7d86b358_4_708': '3DS $0.04 / autenticación',
'g3fb7d86b358_4_710': 'Motor antifraude $0.018 / evaluación',
'g3fb7d86b358_4_712': 'Reglas de riesgo Incluidas',
'g3fb7d86b358_4_713': 'Ninguno está incluido en el total estimado: se activan solo si los necesitan y se facturan según uso.',
}
DELETE = []
# objectId -> (x, y, w, h) pt
MOVE = {'g3f8ec79a1c3_1_1': (374, 268, 45, 12)}
# copy the whole-text style of another element (value cell of Conciliación takes the style of the platform fee value)
RESTYLE_FROM = {'g3f8ec79a1c3_1_1': 'g3fb7d86b358_4_668'}
COVER_LOGO_OLD = 'g3fb7d86b358_4_715'   # Palco wordmark img @(119,22) 95x19
LOGO = 'https://images.weserv.nl/?url=upload.wikimedia.org/wikipedia/commons/7/7e/Logotipo_Cruz_Verde.svg&output=png&w=1000&cx=108&cy=637&cw=675&ch=157'
COVER_LOGO_BOX = (119, 21.5, 82, 19)    # 675x157 crop -> aspect 4.3
FORBID = ['Palco','PALCO','tenant','Tenant','TENANT','Subcuenta','subcuenta','Network','network token','suscripci','Suscripci',
          'INTELIGENCIA','Concierge','Copiloto','235,000','235k','$37.09','$104.6M','58,750','117,500','Openpay','Fiserv',
          '3DS (100k','20k evaluaciones','$7,000','$10,000','GLOBALES PARA','$12,044','$19,044','$23,404']
