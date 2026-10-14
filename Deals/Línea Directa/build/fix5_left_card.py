# -*- coding: utf-8 -*-
"""Pricing v4b (German, 14-oct-2026): la card izquierda vuelve a ser solo la tarifa por transacción (dos tramos);
la fila "Fee de plataforma $7,500/mes" se quita porque ya está en la card del medio. La nota sube debajo de los tramos
y conserva el mensaje "sin compromiso mínimo de volumen". Solo toca el slide de pricing. Usage: python3 fix5_left_card.py [dry]"""
import sys, json, os, urllib.request
from common import *
DRY = 'dry' in sys.argv
NEW = '/private/tmp/claude-501/-Users-germantatis-Desktop-GTMCoding/7939d2cd-c983-4781-a814-49958bb70e22/scratchpad/ld'
os.makedirs(NEW, exist_ok=True)
G = 'g3fb7d86b358_4_'
s = svc(); P = s.presentations().get(presentationId=PID).execute()
json.dump(P, open(f'{NEW}/deck_before_fix5.json', 'w'))
sl = next(x for x in P['slides'] if x['objectId'] == G + '331')
idx = {el['objectId']: (el, tr) for el, tr in elements(sl)}
reqs = []
def txt(oid, markup): reqs.extend(fmt_requests(idx[oid][0], markup)[0])
def put(oid, x=None, y=None, w=None, h=None):
    el, tr = idx[oid]; x0, y0, w0, h0 = geom(el, tr)
    reqs.append(box_req(el, x0 if x is None else x, y0 if y is None else y, w0 if w is None else w, h0 if h is None else h))
for o in ('ld_commit_lbl', 'ld_commit_val', 'ld_commit_sub'):
    if o in idx: reqs.append({'deleteObject': {'objectId': o}})
txt(G + '623', '**TARIFA POR TRANSACCIÓN EXITOSA**')
txt(G + '624', 'Por transacción exitosa, según el volumen del mes.')
put(G + '634', y=222, h=46); put(G + '635', y=226.5, h=38)
txt(G + '635', 'Las transacciones se facturan según el consumo real de cada mes, sin compromiso mínimo de volumen. Sin fee de setup. Cada tramo se cobra a su tarifa dentro del mes. Las transacciones declinadas no se cobran.')
print('requests:', len(reqs))
if DRY: sys.exit(0)
run(s, PID, reqs, label='pricing v4b: left card = tramos only')
Q = s.presentations().get(presentationId=PID).execute(); json.dump(Q, open(f'{NEW}/deck_final_v4b.json', 'w'))
r = s.presentations().pages().getThumbnail(presentationId=PID, pageObjectId=G + '331', thumbnailProperties_thumbnailSize='LARGE').execute()
urllib.request.urlretrieve(r['contentUrl'], f'{NEW}/after_16b.png'); print('slides:', len(Q['slides']), '| thumb saved')
