# -*- coding: utf-8 -*-
"""Pricing v4 (German, 14-oct-2026, tras presentar la propuesta): se elimina el compromiso mínimo de $7,500 en transacciones.
Queda solo el fee de plataforma de $7,500 fijo; las transacciones se facturan según consumo ($0.06 hasta 150,000, $0.05 después).
La franja inferior izquierda añade la facturación separada por entidad (Colombia y Perú). Solo toca el slide de pricing.
Usage: python3 fix4_no_commitment.py [dry]"""
import sys, json, os
from common import *
DRY = 'dry' in sys.argv
NEW = '/private/tmp/claude-501/-Users-germantatis-Desktop-GTMCoding/7939d2cd-c983-4781-a814-49958bb70e22/scratchpad/ld'
os.makedirs(NEW, exist_ok=True)
G = 'g3fb7d86b358_4_'
PLATFORM, P1, P2, CUT, TX = 7_500, 0.06, 0.05, 150_000, 325_000
def var(tx): return min(tx, CUT) * P1 + max(tx - CUT, 0) * P2
total = var(TX) + PLATFORM; v4 = var(400_000); t4 = v4 + PLATFORM
s = svc(); P = s.presentations().get(presentationId=PID).execute()
json.dump(P, open(f'{NEW}/deck_before_fix4.json', 'w'))
sl = next(x for x in P['slides'] if x['objectId'] == G + '331')
idx = {el['objectId']: (el, tr) for el, tr in elements(sl)}
reqs = []
def txt(oid, markup): reqs.extend(fmt_requests(idx[oid][0], markup)[0])        # styles from the element's own runs
def put(oid, x=None, y=None, w=None, h=None):
    el, tr = idx[oid]; x0, y0, w0, h0 = geom(el, tr)
    reqs.append(box_req(el, x0 if x is None else x, y0 if y is None else y, w0 if w is None else w, h0 if h is None else h))
def rm(*oids):
    for o in oids:
        if o in idx: reqs.append({'deleteObject': {'objectId': o}})
# header paragraph
txt(G + '334', f'Una tarifa por transacción que empieza en 6 centavos y baja a 5 con el volumen, facturada según el consumo real de cada mes. El fee de plataforma de ${PLATFORM:,} incluye orquestación y smart routing, los métodos de pago de Colombia y Perú y el checkout alojado. Sin compromiso mínimo de transacciones.')
# left card: the third row becomes the platform fee (same positions as the old commitment row)
txt(G + '623', '**FEE DE PLATAFORMA Y TARIFA POR TRANSACCIÓN**')
txt(G + '624', 'Fijo mensual más tarifa por transacción exitosa.')
txt('ld_commit_lbl', 'Fee de plataforma')
txt('ld_commit_val', f'**${PLATFORM:,}**/mes')
txt('ld_commit_sub', 'Fijo mensual. Sin compromiso mínimo de volumen.')
txt(G + '635', 'Las transacciones se facturan según el consumo real de cada mes. Sin fee de setup. Cada tramo se cobra a su tarifa dentro del mes. Las transacciones declinadas no se cobran.')
# right card: drop the commitment row (+ its separator) and close the gap
rm(G + '692', G + '693', G + '694', G + '695')
for o in ('696', '697', '698'): put(G + o, y=218.9)
put(G + '699', y=237.2)
put(G + '700', y=255.4)
txt(G + '700', f'Sin compromiso mínimo de transacciones: cada mes se factura el fee de plataforma de ${PLATFORM:,} más las transacciones exitosas que realmente se procesen. Desglose a {TX:,}: {CUT:,} × ${P1:.2f} = ${CUT*P1:,.0f} y {TX-CUT:,} × ${P2:.2f} = ${(TX-CUT)*P2:,.0f}. A 400,000 trx/mes: ${PLATFORM:,} + ${v4:,.0f} = ${t4:,.0f} / mes ≈ ${t4/400_000:.4f} por trx.')
# bottom-left note: separate invoicing per entity
txt(G + '703', 'Una cuenta matriz de Línea Directa con una subcuenta para Colombia y otra para Perú, cada una con sus propios métodos de pago. Facturación por separado a la entidad de Colombia y a la de Perú, cada una por su propio volumen. Línea Directa negocia sus tarifas directo con cada proveedor: Yuno no entra en el flujo del dinero.')
print('requests:', len(reqs), f'| total ${total:,.0f}/mes ${total*12:,.0f}/año all-in ${total/TX:.4f} | 400k: ${t4:,.0f}')
if DRY: sys.exit(0)
run(s, PID, reqs, label='pricing v4: no commitment')
Q = s.presentations().get(presentationId=PID).execute(); json.dump(Q, open(f'{NEW}/deck_final_v4.json', 'w'))
n = [x['objectId'] for x in Q['slides']].index(G + '331') + 1
import urllib.request
r = s.presentations().pages().getThumbnail(presentationId=PID, pageObjectId=G + '331', thumbnailProperties_thumbnailSize='LARGE').execute()
urllib.request.urlretrieve(r['contentUrl'], f'{NEW}/after_16.png'); print('slides:', len(Q['slides']), '| thumb slide', n)
