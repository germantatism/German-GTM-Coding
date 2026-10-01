# -*- coding: utf-8 -*-
"""Pricing v3 (German, 1-oct-2026): orquestación y smart routing pasan a estar incluidos en el fee de plataforma;
la franja inferior cotiza conciliación ($1,000 fijos por 200,000 trx conciliadas, $0.03 por trx conciliada adicional).
Solo toca el slide de pricing. Usage: python3 fix3_orchestration_recon.py [dry]"""
import sys, json
from common import *
from model import *
DRY = 'dry' in sys.argv
G = 'g3fb7d86b358_4_'
RECON_FIXED, RECON_PACK, RECON_TX = 1_000, 200_000, 0.03
SRC = json.load(open(f'{WORK}/deck_before.json'))                     # pristine Palco copy: original run styles
sidx = {el['objectId']: el for sl in SRC['slides'] for el, tr in elements(sl)}
s = svc(); P = s.presentations().get(presentationId=PID).execute()
json.dump(P, open(f'{WORK}/deck_before_fix3.json', 'w'))
PREV = json.load(open(f'{WORK}/deck_final_v2.json'))                  # state after my last edit: detect manual edits by German
sl = next(x for x in P['slides'] if x['objectId'] == G+'331'); prev = next(x for x in PREV['slides'] if x['objectId'] == G+'331')
now_t = {el['objectId']: text_of(el).strip() for el, tr in elements(sl)}; old_t = {el['objectId']: text_of(el).strip() for el, tr in elements(prev)}
diff = [(k, old_t.get(k), now_t.get(k)) for k in set(now_t) | set(old_t) if old_t.get(k) != now_t.get(k)]
print('manual edits on the pricing slide since my last change:', diff or 'none')
idx = {el['objectId']: (el, tr) for el, tr in elements(sl)}
def styles(oid): return [(c, st) for c, st in [(te['textRun']['content'], {k: v for k, v in te['textRun'].get('style', {}).items() if k in TEXT_FIELDS})
                         for te in sidx[oid]['shape']['text']['textElements'] if 'textRun' in te] if c.strip()]
reqs = []
def txt(oid, markup): reqs.extend(fmt_requests(idx[oid][0], markup, styles(oid))[0])
def put(oid, x=None, y=None, w=None, h=None):
    el, tr = idx[oid]; x0, y0, w0, h0 = geom(el, tr)
    reqs.append(box_req(el, x0 if x is None else x, y0 if y is None else y, w0 if w is None else w, h0 if h is None else h))
txt(G+'334', f'Una tarifa por transacción que empieza en 6 centavos y baja a 5 con el volumen. El fee de plataforma de ${PLATFORM:,} incluye orquestación y smart routing, los métodos de pago de Colombia y Perú y el checkout alojado; con el compromiso de ${COMMIT:,} en transacciones, la facturación mínima mensual es de ${MIN_BILL:,}.')
# included list: orchestration + smart routing first
txt(G+'646', 'Orquestación y smart routing')
txt(G+'649', 'Una integración para Colombia y Perú')
txt(G+'652', 'Checkout alojado por Yuno (PCI)')
txt(G+'655', 'Cuenta matriz y subcuentas por país')
# bottom strip: reconciliation priced, monitors + network tokens left for later
txt(G+'705', '**OPCIONAL · CONCILIACIÓN**')
txt(G+'706', 'Según consumo, fuera del total estimado.')
txt(G+'708', f'Conciliación **${RECON_FIXED:,}** / mes fijos por {RECON_PACK:,} trx conciliadas'); put(G+'708', x=332, w=165)
put(G+'709', x=499)
txt(G+'710', f'**${RECON_TX:.2f}** / trx conciliada adicional'); put(G+'710', x=511, w=130)
reqs += [{'deleteObject': {'objectId': G+'711'}}, {'deleteObject': {'objectId': G+'712'}}]
txt(G+'713', 'Monitores y network tokens también son opcionales: alcance y precio se revisan en una siguiente fase.')
print('requests:', len(reqs))
if DRY: sys.exit(0)
run(s, PID, reqs, label='pricing v3: orchestration included + reconciliation')
Q = s.presentations().get(presentationId=PID).execute(); json.dump(Q, open(f'{WORK}/deck_final_v3.json', 'w'))
n = [x['objectId'] for x in Q['slides']].index(G+'331') + 1
thumbs(s, Q, [n], 'fix3'); print('slides:', len(Q['slides']), '| thumb slide', n)
