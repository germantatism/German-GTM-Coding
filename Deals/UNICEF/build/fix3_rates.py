# -*- coding: utf-8 -*-
"""Pricing v3 (German, 2-oct-2026): la tarifa empieza en 0.28% y baja a 0.24% (antes 0.25% y 0.20%). Tramos por transacciones aprobadas, sin cambio.
Solo toca el slide de pricing. Compara contra el estado que dejó qa.py para no pisar ediciones manuales. Usage: python3 fix3_rates.py [dry]"""
import sys, json
from common import *
from model import *
DRY = 'dry' in sys.argv
G = 'g3fb7d86b358_4_'
s = svc(); P = s.presentations().get(presentationId=PID).execute()
json.dump(P, open(f'{WORK}/deck_before_fix3.json', 'w'))
PREV = json.load(open(f'{WORK}/deck_final.json'))
sl = next(x for x in P['slides'] if x['objectId'] == G+'331'); prev = next(x for x in PREV['slides'] if x['objectId'] == G+'331')
now_t = {el['objectId']: text_of(el).strip() for el, tr in elements(sl)}; old_t = {el['objectId']: text_of(el).strip() for el, tr in elements(prev)}
diff = [(k, old_t.get(k), now_t.get(k)) for k in set(now_t) | set(old_t) if old_t.get(k) != now_t.get(k)]
print('manual edits on the pricing slide since my last change:', diff or 'none')
idx = {el['objectId']: (el, tr) for el, tr in elements(sl)}
T = {
G+'334': f'Una tarifa variable que empieza en {R1:.2%} del valor de cada transacción aprobada y baja a {R2:.2%} a partir de {CUT_TX:,} transacciones al mes, más ${SUBS:.2f} por transacción enviada por el motor de suscripciones. El fee de plataforma de ${PLATFORM:,} incluye orquestación, smart routing y la bóveda de tokens.',
G+'627': f'**{R1:.2%}**', G+'630': f'**{R2:.2%}**',
G+'676': f'Tramo 1: {TX1:,} trx × ${TICKET} × {R1:.2%}', G+'677': f'${t1:,.0f}', G+'678': f'${t1*12:,.0f}',
G+'680': f'Tramo 2: {TX2:,} trx × ${TICKET} × {R2:.2%}', G+'681': f'${t2:,.0f}', G+'682': f'${t2*12:,.0f}',
G+'685': f'**${var:,.0f}**', G+'686': f'**${var*12:,.0f}**',
G+'697': f'**${total:,.0f}**', G+'698': f'**${total*12:,.0f}**',
G+'699': f'≈ **${total/TX:.2f}** all-in por transacción aprobada.',
G+'700': f'Estimado con {TX:,} transacciones aprobadas al mes y ticket promedio de ${TICKET}. Desglose: {TX1:,} trx × ${TICKET} × {R1:.2%} = ${t1:,.0f} y {TX2:,} trx × ${TICKET} × {R2:.2%} = ${t2:,.0f}. Suscripciones: {SUBS_TX:,} transacciones enviadas por el motor × ${SUBS:.2f} = ${subs:,.0f}.',
}
assert not [k for k in T if k not in idx]
reqs = []
for oid, markup in T.items(): reqs += fmt_requests(idx[oid][0], markup)[0]
for oid in (G+'627', G+'630'):
    reqs.append({'updateParagraphStyle': {'objectId': oid, 'textRange': {'type': 'ALL'}, 'style': {'alignment': 'END'}, 'fields': 'alignment'}})
stale = [(oid, f) for f in ('0.25%', '0.20%', '$3,750', '$1,500', '$5,250', '$63,000', '$18,250', '$219,000', '$0.12') for oid, t in now_t.items() if oid not in T and f in t]
print('requests:', len(reqs), '| old figures left outside the rewritten boxes:', stale or 'none', f'| total ${total:,.0f}/mes ${total*12:,.0f}/año all-in ${total/TX:.4f}')
if DRY: sys.exit(0)
run(s, PID, reqs, label='pricing v3: 0.28% / 0.24%')
Q = s.presentations().get(presentationId=PID).execute(); json.dump(Q, open(f'{WORK}/deck_final_v3.json', 'w'))
n = [x['objectId'] for x in Q['slides']].index(G+'331') + 1
thumbs(s, Q, [n], 'fix3'); print('slides:', len(Q['slides']), '| thumb slide', n)
