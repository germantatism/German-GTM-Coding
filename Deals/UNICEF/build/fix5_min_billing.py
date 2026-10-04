# -*- coding: utf-8 -*-
"""Pricing v5 (German, 4-oct-2026): facturación mínima mensual de $14,000 = $10,000 de plataforma + $4,000 en transacciones
(cerca de 95,000 transacciones aprobadas al mes al ticket de $15). Solo toca el slide de pricing.
Compara contra el estado que dejó qa.py para no pisar ediciones manuales. Usage: python3 fix5_min_billing.py [dry]"""
import sys, json
from common import *
from model import *
DRY = 'dry' in sys.argv
G = 'g3fb7d86b358_4_'
s = svc(); P = s.presentations().get(presentationId=PID).execute()
json.dump(P, open(f'{WORK}/deck_before_fix5.json', 'w'))
PREV = json.load(open(f'{WORK}/deck_final.json'))
sl = next(x for x in P['slides'] if x['objectId'] == G+'331'); prev = next(x for x in PREV['slides'] if x['objectId'] == G+'331')
now_t = {el['objectId']: text_of(el).strip() for el, tr in elements(sl)}; old_t = {el['objectId']: text_of(el).strip() for el, tr in elements(prev)}
diff = [(k, old_t.get(k), now_t.get(k)) for k in set(now_t) | set(old_t) if old_t.get(k) != now_t.get(k)]
print('manual edits on the pricing slide since my last change:', diff or 'none')
idx = {el['objectId']: (el, tr) for el, tr in elements(sl)}
reqs = []
def txt(oid, markup): reqs.extend(fmt_requests(idx[oid][0], markup)[0])
def put(oid, x=None, y=None, w=None, h=None):
    el, tr = idx[oid]; x0, y0, w0, h0 = geom(el, tr)
    reqs.append(box_req(el, x0 if x is None else x, y0 if y is None else y, w0 if w is None else w, h0 if h is None else h))
def dup(src, new):
    reqs.append({'duplicateObject': {'objectId': src, 'objectIds': {src: new}}}); idx[new] = (dict(idx[src][0], objectId=new), idx[src][1])
CT = f'{round(COMMIT_TX, -3):,.0f}'          # 95,000
# header
txt(G+'334', f'La tarifa empieza en {R1:.2%} por transacción aprobada y baja a {R2:.2%} a partir de {CUT_TX:,} al mes; el motor de suscripciones cuesta ${SUBS:.2f} por transacción enviada, con las primeras {SUBS_FREE:,} del mes sin costo. Fee de plataforma de ${PLATFORM:,} y facturación mínima mensual de ${MIN_BILL:,}.')
# left panel: note box carries the minimum billing
put(G+'634', y=261, h=52); put(G+'635', y=265, h=44)
txt(G+'635', f'Facturación mínima mensual de ${MIN_BILL:,}: ${PLATFORM:,} de plataforma más ${COMMIT:,} en transacciones, cerca de {CT} aprobadas al mes al ticket de ${TICKET}. Si el mes cierra por debajo, se factura la diferencia. Las declinadas no pagan el porcentaje. Sin fee de setup.')
# middle panel: new row under the platform fee
dup(G+'664', 'un_min_lbl'); dup(G+'665', 'un_min_val')
put('un_min_lbl', y=303.5); put('un_min_val', y=303.5)
txt('un_min_lbl', 'Facturación mínima mensual'); txt('un_min_val', f'**${MIN_BILL:,} / mes**')
# right panel: new row between platform fee and total; total, callout and note move down
dup(G+'692', 'un_min_r_lbl'); dup(G+'693', 'un_min_r_m'); dup(G+'694', 'un_min_r_a'); dup(G+'695', 'un_min_r_sep')
put('un_min_r_lbl', y=235.5); put('un_min_r_m', y=235.5); put('un_min_r_a', y=235.5); put('un_min_r_sep', y=248.2)
txt('un_min_r_lbl', f'Facturación mínima: ${MIN_BILL:,} (≈{CT} trx)'); txt('un_min_r_m', 'Cubierta'); txt('un_min_r_a', 'Cubierta')
for oid in (G+'696', G+'697', G+'698'): put(oid, y=252.1)
put(G+'699', y=270.4); put(G+'700', y=288.6, h=30)
txt(G+'700', f'Facturación mínima mensual: ${MIN_BILL:,} (${PLATFORM:,} de plataforma + ${COMMIT:,} en transacciones, cerca de {CT} transacciones aprobadas al mes al ticket de ${TICKET}; con {TX:,} queda cubierta). Suscripciones: {SUBS_TX:,} envíos menos las primeras {SUBS_FREE:,} sin costo = {SUBS_BILL:,} × ${SUBS:.2f} = ${subs:,.0f}.')
assert total >= MIN_BILL
print('requests:', len(reqs), f'| mínimo ${MIN_BILL:,} = ${PLATFORM:,} + ${COMMIT:,} -> {COMMIT_TX:,.1f} trx (slide: {CT}) | total ${total:,.0f}/mes')
if DRY: sys.exit(0)
run(s, PID, reqs, label='pricing v5: minimum monthly billing')
Q = s.presentations().get(presentationId=PID).execute(); json.dump(Q, open(f'{WORK}/deck_final_v5.json', 'w'))
n = [x['objectId'] for x in Q['slides']].index(G+'331') + 1
thumbs(s, Q, [n], 'fix5'); print('slides:', len(Q['slides']), '| thumb slide', n)
