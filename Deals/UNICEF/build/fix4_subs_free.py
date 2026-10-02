# -*- coding: utf-8 -*-
"""Pricing v4 (German, 2-oct-2026): el motor de suscripciones no cobra las primeras 50,000 transacciones (del mes).
Solo toca el slide de pricing. Compara contra el estado que dejó qa.py para no pisar ediciones manuales. Usage: python3 fix4_subs_free.py [dry]"""
import sys, json
from common import *
from model import *
DRY = 'dry' in sys.argv
G = 'g3fb7d86b358_4_'
s = svc(); P = s.presentations().get(presentationId=PID).execute()
json.dump(P, open(f'{WORK}/deck_before_fix4.json', 'w'))
PREV = json.load(open(f'{WORK}/deck_final.json'))
sl = next(x for x in P['slides'] if x['objectId'] == G+'331'); prev = next(x for x in PREV['slides'] if x['objectId'] == G+'331')
now_t = {el['objectId']: text_of(el).strip() for el, tr in elements(sl)}; old_t = {el['objectId']: text_of(el).strip() for el, tr in elements(prev)}
diff = [(k, old_t.get(k), now_t.get(k)) for k in set(now_t) | set(old_t) if old_t.get(k) != now_t.get(k)]
print('manual edits on the pricing slide since my last change:', diff or 'none')
idx = {el['objectId']: (el, tr) for el, tr in elements(sl)}
T = {
G+'334': f'La tarifa empieza en {R1:.2%} del valor de cada transacción aprobada y baja a {R2:.2%} a partir de {CUT_TX:,} transacciones al mes. El motor de suscripciones cuesta ${SUBS:.2f} por transacción enviada, con las primeras {SUBS_FREE:,} del mes sin costo. El fee de plataforma es de ${PLATFORM:,} al mes.',
'ld_commit_sub': f'Por transacción enviada por el motor. Las primeras {SUBS_FREE:,} del mes, sin costo.',
G+'688': f'Suscripciones: {SUBS_BILL:,} trx × ${SUBS:.2f}', G+'689': f'${subs:,.0f}', G+'690': f'${subs*12:,.0f}',
G+'697': f'**${total:,.0f}**', G+'698': f'**${total*12:,.0f}**',
G+'699': f'≈ **${total/TX:.2f}** all-in por transacción aprobada.',
G+'700': f'Estimado con {TX:,} transacciones aprobadas al mes y ticket promedio de ${TICKET}. Desglose: {TX1:,} trx × ${TICKET} × {R1:.2%} = ${t1:,.0f} y {TX2:,} trx × ${TICKET} × {R2:.2%} = ${t2:,.0f}. Suscripciones: {SUBS_TX:,} transacciones enviadas por el motor, menos las primeras {SUBS_FREE:,} sin costo: {SUBS_BILL:,} × ${SUBS:.2f} = ${subs:,.0f}.',
}
assert not [k for k in T if k not in idx]
reqs = []
for oid, markup in T.items(): reqs += fmt_requests(idx[oid][0], markup)[0]
stale = [(oid, f) for f in ('$3,000', '$36,000', '$19,000', '$228,000', '$0.13') for oid, t in now_t.items() if oid not in T and f in t]
print('requests:', len(reqs), '| old figures left outside the rewritten boxes:', stale or 'none', f'| total ${total:,.0f}/mes ${total*12:,.0f}/año all-in ${total/TX:.4f}')
if DRY: sys.exit(0)
run(s, PID, reqs, label='pricing v4: first 50,000 subscription trx free')
Q = s.presentations().get(presentationId=PID).execute(); json.dump(Q, open(f'{WORK}/deck_final_v4.json', 'w'))
n = [x['objectId'] for x in Q['slides']].index(G+'331') + 1
thumbs(s, Q, [n], 'fix4'); print('slides:', len(Q['slides']), '| thumb slide', n)
