# -*- coding: utf-8 -*-
"""Build 'Propuesta - UNICEF Colombia + Yuno' on the Drive copy of 'Propuesta - Línea Directa + Yuno' (Slides API, service account).
Usage: python3 build_unicef.py dry -> simulate, report missing ids and forbidden tokens | python3 build_unicef.py -> apply + thumbnails
Markup: **x** = bold run of the original element. Numbers come from model.py."""
import sys, json
from common import *
from model import *
DRY = 'dry' in sys.argv
G = 'g3fb7d86b358_4_'
NAME, NAME_UP = 'UNICEF Colombia', 'UNICEF COLOMBIA'
T = {
# S1 cover
'g3c99cf7678e_0_1': f'IMPULSANDO PAGOS SIN FRICCIÓN PARA {NAME_UP}',
# S2 agenda
'g3caca0138e4_0_5': 'CONEXIONES EN COLOMBIA',
# S5 why partner
'g3caca0138e4_0_2155': f'Por qué creemos que Yuno es el socio ideal para {NAME}',
'g3caca0138e4_0_2160': f'UN EQUIPO DEDICADO PARA {NAME_UP}',
'g3caca0138e4_0_2168': 'Cobertura global de proveedores + rieles locales de Colombia para lanzar y escalar rápido',
# S11 key advantages
'g3c99cf7678e_0_28715': f'Yuno es la capa de pagos para el recaudo recurrente de {NAME}',
'g3c99cf7678e_0_28719': f'Una sola integración sobre sus procesadores actuales y un motor de suscripciones con reintentos automáticos posicionan a Yuno como el socio ideal para {NAME}',
'g3c99cf7678e_0_28735': 'Una sola integración sobre sus procesadores actuales',
'g3c99cf7678e_0_28722': 'Ruteo y respaldo automático entre procesadores de tarjeta',
'g3c99cf7678e_0_28726': 'Reintentos automáticos configurados por su equipo',
'g3c99cf7678e_0_28731': 'Todo el recaudo en un solo panel, con reportes',
# S12 divider
'SLIDES_API561741952_132': 'Conexiones en Colombia',
# S16 pricing: header
G+'332': 'Fee de plataforma más un porcentaje del volumen aprobado',
G+'334': f'Una tarifa variable que empieza en {R1:.2%} del volumen aprobado y baja a {R2:.2%} con el volumen, más ${SUBS:.2f} por transacción enviada por el motor de suscripciones. El fee de plataforma de ${PLATFORM:,} incluye orquestación y smart routing, la bóveda de tokens y una sola integración vía API.',
# S16 left panel
G+'623': '**TARIFA SOBRE VOLUMEN APROBADO**',
G+'624': 'Porcentaje del volumen aprobado en el mes, por tramos.',
G+'626': f'$0 a {K(CUT)} al mes', G+'627': f'**{R1:.2%}**',
G+'629': f'Más de {K(CUT)} al mes', G+'630': f'**{R2:.2%}**',
'ld_commit_lbl': 'Motor de suscripciones', 'ld_commit_val': f'**${SUBS:.2f}**/trx',
'ld_commit_sub': 'Por transacción enviada por el motor de suscripciones.',
G+'635': 'El porcentaje se cobra sobre el volumen aprobado: las transacciones declinadas no lo pagan. Cada tramo se cobra a su tarifa dentro del mes. Sin fee de setup.',
# S16 middle panel
G+'646': 'Orquestación y smart routing',
G+'649': 'Una sola integración vía API',
G+'652': 'Bóveda de tokens (PCI)',
G+'655': 'Gestión de transacciones',
G+'665': f'**${PLATFORM:,} / mes**',
# S16 right panel
G+'670': f'**LO QUE SIGNIFICA PARA {NAME_UP}**',
G+'671': f'A {TX:,} transacciones al mes y ticket promedio de ${TICKET}.',
G+'676': f'Tramo 1: ${min(VOL, CUT):,.0f} × {R1:.2%}', G+'677': f'${t1:,.0f}', G+'678': f'${t1*12:,.0f}',
G+'680': f'Tramo 2: ${VOL-CUT:,.0f} × {R2:.2%}', G+'681': f'${t2:,.0f}', G+'682': f'${t2*12:,.0f}',
G+'684': f'**Subtotal volumen aprobado ({K(VOL)})**', G+'685': f'**${var:,.0f}**', G+'686': f'**${var*12:,.0f}**',
G+'688': f'Suscripciones: {SUBS_TX:,} trx × ${SUBS:.2f}', G+'689': f'${subs:,.0f}', G+'690': f'${subs*12:,.0f}',
G+'692': 'Fee de plataforma', G+'693': f'${PLATFORM:,}', G+'694': f'${PLATFORM*12:,}',
G+'696': '**Total mensual estimado**', G+'697': f'**${total:,.0f}**', G+'698': f'**${total*12:,.0f}**',
G+'699': f'≈ **${total/TX:.2f}** all-in por transacción, {total/VOL:.2%} del volumen aprobado.',
G+'700': f'Estimado con {TX:,} transacciones al mes y ticket promedio de ${TICKET}: ${VOL:,.0f} de volumen aprobado. Desglose: ${min(VOL, CUT):,.0f} × {R1:.2%} = ${t1:,.0f} y ${VOL-CUT:,.0f} × {R2:.2%} = ${t2:,.0f}. Suscripciones: {SUBS_TX:,} transacciones enviadas por el motor × ${SUBS:.2f} = ${subs:,.0f}.',
# S16 bottom
G+'703': f'{NAME} mantiene sus contratos y tarifas con cada procesador (Credibanco, Redeban, Wompi y Nuvei): Yuno se conecta por encima de ellos y no entra en el flujo del dinero.',
G+'705': '**OPCIONAL · PARA REVISAR DESPUÉS**',
G+'706': 'No incluido en esta propuesta.',
G+'708': 'Conciliación  ·  Monitores y alertas  ·  Network tokens  ·  Nova',
G+'713': f'Alcance y precio se revisan juntos en una siguiente fase, cuando {NAME} lo necesite.',
}
DELETE = [G+'709', G+'710']                       # separator dot + second price of the LD reconciliation strip
DELETE_SLIDES = ['h32a7d7002d26eaec_0_47']        # Perú connections
END = [G+'627', G+'630', G+'665']                 # right-aligned values
# objectId -> (x, y, w, h) pt; None keeps the current value
MOVE = {
 G+'627': (133, None, 80, None), G+'630': (133, None, 80, None),     # same box as the subscriptions value: right edges line up
 G+'626': (None, None, 100, None), G+'629': (None, None, 100, None),
 G+'665': (364, None, 55.3, None),
 G+'708': (None, None, 345, None),
}
LOGO = 'https://images.weserv.nl/?url=https://upload.wikimedia.org/wikipedia/commons/e/ed/Logo_of_UNICEF.svg&mod=12,0&w=1300&output=png'
# (old image id, new id, box): UNICEF wordmark is 1300 x 313 (4.15:1)
LOGOS = [('ld_cover_logo', 'un_cover_logo', (119, 23, 70.6, 17)), ('ld_close_logo', 'un_close_logo', (621, 197.5, 70.6, 17))]
FORBID = ['Línea Directa', 'LÍNEA DIRECTA', 'Linea Directa', 'Eledé', 'Perú', 'PERÚ', 'portal de pedidos', 'subcuenta', '$7,500', '325,000', '125,000',
          '225,000', '$0.06', '$0.05', '$15,000', 'compromiso', 'Compromiso', 'Palco', ' — ', ' – ', ' - ']

if __name__ == '__main__':
    s = svc(); P = s.presentations().get(presentationId=PID).execute()
    json.dump(P, open(f'{WORK}/deck_before_build.json', 'w'))
    idx = {}; slide_of = {}
    for n, sl in enumerate(P['slides'], 1):
        for el, tr in elements(sl): idx[el['objectId']] = (el, tr); slide_of[el['objectId']] = n
    sids = [x['objectId'] for x in P['slides']]
    need = list(T) + DELETE + list(MOVE) + END + [l[0] for l in LOGOS]
    print('MISSING ids:', [k for k in need if k not in idx], '| missing slides:', [x for x in DELETE_SLIDES if x not in sids])
    reqs = []; sim = {}
    for oid, markup in T.items():
        r, text = fmt_requests(idx[oid][0], markup); reqs += r; sim[oid] = text
    for oid in END:
        reqs.append({'updateParagraphStyle': {'objectId': oid, 'textRange': {'type': 'ALL'}, 'style': {'alignment': 'END'}, 'fields': 'alignment'}})
    for oid in DELETE: reqs.append({'deleteObject': {'objectId': oid}}); sim[oid] = ''
    for oid, (x, y, w, h) in MOVE.items():
        el, tr = idx[oid]; x0, y0, w0, h0 = geom(el, tr)
        reqs.append(box_req(el, x0 if x is None else x, y0 if y is None else y, w0 if w is None else w, h0 if h is None else h))
    for old, new, (x, y, w, h) in LOGOS:
        page = P['slides'][slide_of[old] - 1]['objectId']
        reqs.append({'deleteObject': {'objectId': old}})
        reqs.append({'createImage': {'objectId': new, 'url': LOGO, 'elementProperties': {'pageObjectId': page,
            'size': {'width': {'magnitude': w * 12700, 'unit': 'EMU'}, 'height': {'magnitude': h * 12700, 'unit': 'EMU'}},
            'transform': {'scaleX': 1, 'scaleY': 1, 'shearX': 0, 'shearY': 0, 'translateX': x * 12700, 'translateY': y * 12700, 'unit': 'EMU'}}}})
    for sid in DELETE_SLIDES: reqs.append({'deleteObject': {'objectId': sid}})
    bad = []
    for n, sl in enumerate(P['slides'], 1):
        if sl['objectId'] in DELETE_SLIDES: continue
        for el, tr in elements(sl):
            t = text_of(el).strip()
            if not t: continue
            chk = sim.get(el['objectId'], t)
            for f in FORBID:
                if f in chk: bad.append((n, el['objectId'], f, chk[:70]))
    print('FORBIDDEN tokens in final text:'); [print('  S%d %s [%s] %s' % b) for b in bad]
    print('requests:', len(reqs), '| text elements replaced:', len(sim))
    if DRY: print('dry run, nothing changed'); sys.exit(0)
    run(s, PID, reqs, label='unicef build')
    Q = s.presentations().get(presentationId=PID).execute(); json.dump(Q, open(f'{WORK}/deck_after_build.json', 'w'))
    qids = [x['objectId'] for x in Q['slides']]
    changed = sorted({qids.index(P['slides'][slide_of[o] - 1]['objectId']) + 1 for o in list(T) + list(MOVE)} | {1, len(Q['slides'])})
    thumbs(s, Q, changed, 'after'); print('slides:', len(Q['slides']), '| thumbs:', changed)
