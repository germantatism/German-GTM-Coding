# -*- coding: utf-8 -*-
"""Pricing v2 (German, 2-oct-2026): los tramos se definen por número de transacciones aprobadas, no por volumen aprobado.
El porcentaje se aplica al valor de cada transacción aprobada. Los totales no cambian. Solo toca el slide de pricing.
Compara contra el estado que dejó qa.py para no pisar ediciones manuales. Usage: python3 fix2_tx_tiers.py [dry]"""
import sys, json
from common import *
from model import *
DRY = 'dry' in sys.argv
G = 'g3fb7d86b358_4_'
s = svc(); P = s.presentations().get(presentationId=PID).execute()
json.dump(P, open(f'{WORK}/deck_before_fix2.json', 'w'))
PREV = json.load(open(f'{WORK}/deck_final.json'))
sl = next(x for x in P['slides'] if x['objectId'] == G+'331'); prev = next(x for x in PREV['slides'] if x['objectId'] == G+'331')
now_t = {el['objectId']: text_of(el).strip() for el, tr in elements(sl)}; old_t = {el['objectId']: text_of(el).strip() for el, tr in elements(prev)}
diff = [(k, old_t.get(k), now_t.get(k)) for k in set(now_t) | set(old_t) if old_t.get(k) != now_t.get(k)]
print('manual edits on the pricing slide since my last change:', diff or 'none')
idx = {el['objectId']: (el, tr) for el, tr in elements(sl)}
T = {
G+'332': 'Fee de plataforma más un porcentaje por transacción aprobada',
G+'334': f'Una tarifa variable que empieza en {R1:.2%} del valor de cada transacción aprobada y baja a {R2:.2%} a partir de {CUT_TX:,} transacciones al mes, más ${SUBS:.2f} por transacción enviada por el motor de suscripciones. El fee de plataforma de ${PLATFORM:,} incluye orquestación, smart routing y la bóveda de tokens.',
G+'623': '**TARIFA POR TRANSACCIÓN APROBADA**',
G+'624': 'Porcentaje del valor de cada transacción aprobada, por tramos.',
G+'626': f'0 a {CUT_TX:,} trx aprobadas',
G+'629': f'Más de {CUT_TX:,} trx aprobadas',
G+'635': 'El porcentaje se cobra sobre el valor de cada transacción aprobada: las declinadas no lo pagan. Cada tramo se cobra a su tarifa dentro del mes. Sin fee de setup.',
G+'671': f'A {TX:,} transacciones aprobadas al mes y ticket promedio de ${TICKET}.',
G+'676': f'Tramo 1: {TX1:,} trx × ${TICKET} × {R1:.2%}',
G+'680': f'Tramo 2: {TX2:,} trx × ${TICKET} × {R2:.2%}',
G+'684': f'**Subtotal transacciones ({TX//1000}k)**',
G+'699': f'≈ **${total/TX:.2f}** all-in por transacción aprobada.',
G+'700': f'Estimado con {TX:,} transacciones aprobadas al mes y ticket promedio de ${TICKET}. Desglose: {TX1:,} trx × ${TICKET} × {R1:.2%} = ${t1:,.0f} y {TX2:,} trx × ${TICKET} × {R2:.2%} = ${t2:,.0f}. Suscripciones: {SUBS_TX:,} transacciones enviadas por el motor × ${SUBS:.2f} = ${subs:,.0f}.',
}
assert not [k for k in T if k not in idx]
reqs = []
for oid, markup in T.items(): reqs += fmt_requests(idx[oid][0], markup)[0]
el, tr = idx[G+'334']; x0, y0, w0, h0 = geom(el, tr); reqs.append(box_req(el, x0, y0, 656, h0))   # header on two lines
left = [f for f in ('volumen aprobado', '$1.5M', '$1,500,000', '$750,000') for oid, t in now_t.items() if oid not in T and f in t]
print('requests:', len(reqs), '| volume wording left outside the rewritten boxes:', left or 'none')
if DRY: sys.exit(0)
run(s, PID, reqs, label='pricing v2: tiers by approved transactions')
Q = s.presentations().get(presentationId=PID).execute(); json.dump(Q, open(f'{WORK}/deck_final_v2.json', 'w'))
n = [x['objectId'] for x in Q['slides']].index(G+'331') + 1
thumbs(s, Q, [n], 'fix2'); print('slides:', len(Q['slides']), '| thumb slide', n)
