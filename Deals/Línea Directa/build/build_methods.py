# -*- coding: utf-8 -*-
"""Payment-methods slide ('ld_methods', duplicate of the pricing slide made by step0_dup_methods.py).
Two cards (Colombia | Perú) with category -> methods rows, a note inside the Perú card and a full-width strip below.
Fuente de los métodos: docs.y.uno/reference/payment-type-list (consultado 30-sep-2026)."""
import sys, json
from common import *
DRY = 'dry' in sys.argv
s = svc(); P = s.presentations().get(presentationId=PID).execute()
sl = next(x for x in P['slides'] if x['objectId'] == 'ld_methods')
idx = {el['objectId']: (el, tr) for el, tr in elements(sl)}
L = lambda n: 'ldm_4_%d' % n
CO = [('Billeteras', 'Nequi · Daviplata'),
      ('Transferencia bancaria', 'PSE · Botón Bancolombia'),
      ('Pagos inmediatos', 'Bre-B (QR) · Transfiya'),
      ('Tarjeta débito y crédito', 'Credibanco · Redeban · Wompi · PayU · ePayco'),
      ('Efectivo', 'Efecty'),
      ('Compra ahora, paga después', 'Addi · Bancolombia BNPL · SU+ Pay'),
      ('Billeteras digitales de tarjeta', 'Apple Pay · Google Pay')]
PE = [('Billeteras', 'Yape · Plin'),
      ('Tarjeta débito y crédito', 'Niubiz · Izipay · Redeban Perú · Monnet'),
      ('Efectivo y banca por internet', 'PagoEfectivo · SafetyPay'),
      ('Cuotas sin tarjeta', 'Cuotéalo BCP')]
# (label id, value id, separator id) pools taken from the old "QUÉ CUBRE LA TARIFA" card
ROWS = [(L(640), L(641), L(639)), (L(643), L(644), L(642)), (L(646), L(647), L(645)), (L(649), L(650), L(648)),
        (L(652), L(653), L(651)), (L(655), L(656), L(654)), (L(658), L(659), L(657)),
        (L(661), L(662), L(660)), ('ldm_1_0', 'ldm_1_1', L(663)), (L(664), L(665), L(666)), (L(667), L(668), 'ldm_1_2')]
X_CO, X_PE, W, Y0, PITCH = 31.5, 366.5, 322.0, 137.3, 24.0
reqs = []; keep = set()
def put(oid, x, y, w, h): reqs.append(box_req(idx[oid][0], x, y, w, h)); keep.add(oid)
def txt(oid, markup, styles=None):
    r, _ = fmt_requests(idx[oid][0], markup, styles); reqs.extend(r); keep.add(oid)
val_style = [(c, st) for c, st in [(te['textRun']['content'], {k: v for k, v in te['textRun'].get('style', {}).items() if k in TEXT_FIELDS})
             for te in idx[L(641)][0]['shape']['text']['textElements'] if 'textRun' in te] if c.strip()]
# header
txt(L(332), 'Los métodos de pago de Colombia y Perú en una sola integración')
txt(L(333), 'PROPUESTA · MÉTODOS DE PAGO')
txt(L(334), 'Los métodos que Línea Directa usa hoy y la tarjeta débito y crédito, en un mismo checkout y organizados en una subcuenta por país. Cada método se conecta con el proveedor que Línea Directa elija.')
# Colombia card (reuses the white card) + Perú card (duplicates of background, header and sub-header)
put(L(636), X_CO, 102, W, 221.3); put(L(637), X_CO + 12, 112, 200, 12); put(L(638), X_CO + 12, 124, W - 24, 11)
txt(L(637), '**COLOMBIA**'); txt(L(638), 'Subcuenta Colombia. Hoy en su portal: PSE, Bancolombia (Wompi) y Nequi.')
for src, new in ((L(636), 'ldm_pe_bg'), (L(637), 'ldm_pe_hd'), (L(638), 'ldm_pe_sub')):
    reqs.append({'duplicateObject': {'objectId': src, 'objectIds': {src: new}}}); idx[new] = (dict(idx[src][0], objectId=new), idx[src][1])
put('ldm_pe_bg', X_PE, 102, W, 221.3); put('ldm_pe_hd', X_PE + 12, 112, 200, 12); put('ldm_pe_sub', X_PE + 12, 124, W - 24, 11)
reqs.append({'updatePageElementsZOrder': {'pageElementObjectIds': ['ldm_pe_bg'], 'operation': 'SEND_TO_BACK'}})
txt('ldm_pe_hd', '**PERÚ**'); txt('ldm_pe_sub', 'Subcuenta Perú. Hoy: Yape.')
def rows(data, pool, x0):
    for k, ((label, value), (lid, vid, sid)) in enumerate(zip(data, pool)):
        y = Y0 + PITCH * k
        put(sid, x0 + 12, y, W - 24, 0.6)
        put(lid, x0 + 12, y + 6.3, 125, 12); txt(lid, label)
        put(vid, x0 + 12 + 125, y + 6.3, W - 24 - 125, 12); txt(vid, '**' + value + '**', val_style)
        reqs.append({'updateParagraphStyle': {'objectId': vid, 'textRange': {'type': 'ALL'}, 'style': {'alignment': 'END'}, 'fields': 'alignment'}})
rows(CO, ROWS[:7], X_CO); rows(PE, ROWS[7:], X_PE)
# note inside the Perú card (old "pendiente de revisión" box with its accent bar)
put(L(701), X_PE + 12, 252, W - 24, 56); put(L(702), X_PE + 12, 252, 2.2, 56); put(L(703), X_PE + 24, 256, W - 48, 48)
txt(L(703), 'La subcuenta de Perú comparte la integración, el checkout y los reportes con Colombia. Cada país opera con sus propios métodos y proveedores, bajo la cuenta matriz de Línea Directa.')
# full-width strip below
put(L(704), 31.5, 332.3, 657, 52.5); put(L(705), 43.5, 339, 200, 12); put(L(706), 441, 340, 236, 10); put(L(707), 43.5, 352.6, 633, 0.6)
put(L(708), 43.5, 356.5, 633, 11); put(L(713), 43.5, 369.5, 633, 10)
txt(L(705), '**CÓMO SE ACTIVAN**'); txt(L(706), 'Fuente: catálogo público de Yuno (docs.y.uno), septiembre de 2026.')
txt(L(708), 'Cada método se activa desde el dashboard con el proveedor que Línea Directa elija y con la tarifa que negocie directo con él. Sumar o cambiar un método es configuración, no un desarrollo nuevo.')
txt(L(713), 'Dale: disponibilidad en validación con nuestro equipo de producto.')
# delete everything else on the slide
gone = [oid for oid in idx if oid not in keep]
reqs += [{'deleteObject': {'objectId': oid}} for oid in gone]
print('keep', len(keep), '| delete', len(gone), '| requests', len(reqs))
if DRY: sys.exit(0)
run(s, PID, reqs, label='methods slide')
Q = s.presentations().get(presentationId=PID).execute(); json.dump(Q, open(f'{WORK}/deck_after_methods.json', 'w'))
n = [x['objectId'] for x in Q['slides']].index('ld_methods') + 1
thumbs(s, Q, [n], 'methods'); print('thumb slide', n)
