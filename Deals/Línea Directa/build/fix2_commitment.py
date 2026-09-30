# -*- coding: utf-8 -*-
"""Pricing v2 (German, 30-sep-2026): platform fee $7,500 + compromiso mínimo de $7,500 en transacciones (= 125,000 trx a $0.06),
facturación mínima mensual de $15,000. Rewrites the pricing slide only. Usage: python3 fix2_commitment.py [dry]"""
import sys, json
from common import *
from model import *
DRY = 'dry' in sys.argv
G = 'g3fb7d86b358_4_'
SRC = json.load(open(f'{WORK}/deck_before.json'))                     # pristine Palco copy: original run styles
sidx = {el['objectId']: el for sl in SRC['slides'] for el, tr in elements(sl)}
s = svc(); P = s.presentations().get(presentationId=PID).execute()
idx = {el['objectId']: (el, tr) for sl in P['slides'] for el, tr in elements(sl)}
def styles(oid): return [(c, st) for c, st in [(te['textRun']['content'], {k: v for k, v in te['textRun'].get('style', {}).items() if k in TEXT_FIELDS})
                         for te in sidx[oid]['shape']['text']['textElements'] if 'textRun' in te] if c.strip()]
reqs = []
def txt(oid, markup, style_from=None):
    reqs.extend(fmt_requests(idx[oid][0], markup, styles(style_from or oid))[0])
def put(oid, x=None, y=None, w=None, h=None):
    el, tr = idx[oid]; x0, y0, w0, h0 = geom(el, tr)
    reqs.append(box_req(el, x0 if x is None else x, y0 if y is None else y, w0 if w is None else w, h0 if h is None else h))
def dup(src, new):
    reqs.append({'duplicateObject': {'objectId': src, 'objectIds': {src: new}}}); idx[new] = (dict(idx[src][0], objectId=new), idx[src][1])
var, total = monthly(TX); v4, t4 = monthly(400_000)
# header
txt(G+'334', f'Una tarifa por transacción que empieza en 6 centavos y baja a 5 con el volumen, con los métodos de pago de Colombia y Perú, el checkout alojado y las subcuentas por país incluidos. Fee de plataforma de ${PLATFORM:,} más un compromiso de ${COMMIT:,} en transacciones: facturación mínima mensual de ${MIN_BILL:,}.')
# left panel: back to three rows (tramo 1, tramo 2, compromiso mínimo) + taller note
put(G+'626', y=150); put(G+'627', y=145); put(G+'628', y=171.9)
put(G+'629', y=185); put(G+'630', y=180); put(G+'631', y=206.8)
dup(G+'629', 'ld_commit_lbl'); dup(G+'630', 'ld_commit_val'); dup(G+'624', 'ld_commit_sub')
put('ld_commit_lbl', 43.9, 220, 100, 12); reqs.extend(fmt_requests(idx['ld_commit_lbl'][0], 'Compromiso mínimo mensual', styles(G+'629'))[0])
put('ld_commit_val', 133, 214.5, 80, 22); reqs.extend(fmt_requests(idx['ld_commit_val'][0], f'**${COMMIT:,}**/mes', styles(G+'630'))[0])
reqs.append({'updateParagraphStyle': {'objectId': 'ld_commit_val', 'textRange': {'type': 'ALL'}, 'style': {'alignment': 'END'}, 'fields': 'alignment'}})
put('ld_commit_sub', 43.9, 238, 166, 11)
reqs.extend(fmt_requests(idx['ld_commit_sub'][0], f'Equivale a {COMMIT_TX:,.0f} transacciones exitosas al mes a ${P1:.2f}.', styles(G+'624'))[0])
put(G+'634', y=264, h=49); put(G+'635', y=268.5, h=40)
txt(G+'635', 'Si el mes cierra por debajo del compromiso, se factura la diferencia. Sin fee de setup. Cada tramo se cobra a su tarifa dentro del mes. Las transacciones declinadas no se cobran.')
# middle panel: last three rows = equipo dedicado, fee de plataforma, compromiso mínimo
txt('g3f8ec79a1c3_1_0', 'Equipo dedicado (KAM y TAM)')
txt(G+'664', 'Fee de plataforma'); put(G+'664', w=140)
txt(G+'665', f'**${PLATFORM:,} / mes**', G+'668'); put(G+'665', x=374.3, w=45)
txt(G+'667', 'Compromiso mínimo en transacciones'); put(G+'667', w=125)
txt(G+'668', f'**${COMMIT:,} / mes**'); put(G+'668', x=374.3, w=45)
# right panel
txt(G+'689', f'${PLATFORM:,}'); txt(G+'690', f'${PLATFORM*12:,}')
txt(G+'692', f'Compromiso mínimo: ${COMMIT:,} ({COMMIT_TX:,.0f} trx)'); txt(G+'693', 'Cubierto'); txt(G+'694', 'Cubierto')
txt(G+'697', f'**${total:,.0f}**'); txt(G+'698', f'**${total*12:,.0f}**')
txt(G+'699', f'≈ **${total/TX:.3f}** all-in por transacción exitosa. Baja a medida que crece el volumen.')
put(G+'700', y=272, h=44)
txt(G+'700', f'Facturación mínima mensual: ${MIN_BILL:,} (${PLATFORM:,} de plataforma + ${COMMIT:,} de compromiso en transacciones, que equivale a {COMMIT_TX:,.0f} trx a ${P1:.2f}). Desglose a {TX:,}: {CUT:,} × ${P1:.2f} = ${CUT*P1:,.0f} y {TX-CUT:,} × ${P2:.2f} = ${(TX-CUT)*P2:,.0f}. A 400,000 trx/mes: ${PLATFORM:,} + ${v4:,.0f} = ${t4:,.0f} / mes ≈ ${t4/400_000:.4f} por trx.')
print('requests:', len(reqs), f'| total ${total:,.0f}/mes ${total*12:,.0f}/año all-in ${total/TX:.4f} | commit tx {COMMIT_TX:,.0f}')
if DRY: sys.exit(0)
run(s, PID, reqs, label='pricing v2: commitment')
Q = s.presentations().get(presentationId=PID).execute(); json.dump(Q, open(f'{WORK}/deck_after_fix2.json', 'w'))
n = [x['objectId'] for x in Q['slides']].index(G+'331') + 1
thumbs(s, Q, [n], 'fix2'); print('thumb slide', n)
