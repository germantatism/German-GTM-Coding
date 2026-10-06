# -*- coding: utf-8 -*-
"""Pricing v6 (German, 6-oct-2026): fee de plataforma baja a $7,000, facturación mínima mensual baja a $10,000
($7,000 de plataforma + $3,000 en transacciones, cerca de 71,000 aprobadas al mes al ticket de $15) y el motor de
suscripciones baja a $0.015 por transacción enviada. Solo toca el slide de pricing; mismos IDs que fix5 (ninguna caja
nueva ni se mueve nada). Antes de escribir compara el texto actual con el que dejó fix5 para no pisar ediciones manuales.
Usage: python3 fix6_v6_lower_fees.py [dry]"""
import sys, json
from common import *
from model import *
DRY = 'dry' in sys.argv
G = 'g3fb7d86b358_4_'
s = svc(); P = s.presentations().get(presentationId=PID).execute()
json.dump(P, open(f'{WORK}/deck_before_fix6.json', 'w'))
sl = next(x for x in P['slides'] if x['objectId'] == G+'331')
idx = {el['objectId']: (el, tr) for el, tr in elements(sl)}
CT = f'{round(COMMIT_TX, -3):,.0f}'          # 71,000
# texto que dejó fix5 (v5) en cada caja que se toca; si German editó algo a mano, se avisa y no se escribe
V5 = {
 G+'334': 'La tarifa empieza en 0.28% por transacción aprobada y baja a 0.24% a partir de 100,000 al mes; el motor de suscripciones cuesta $0.02 por transacción enviada, con las primeras 50,000 del mes sin costo. Fee de plataforma de $10,000 y facturación mínima mensual de $14,000.',
 G+'635': 'Facturación mínima mensual de $14,000: $10,000 de plataforma más $4,000 en transacciones, cerca de 95,000 aprobadas al mes al ticket de $15. Si el mes cierra por debajo, se factura la diferencia. Las declinadas no pagan el porcentaje. Sin fee de setup.',
 'ld_commit_val': '$0.02/trx', G+'665': '$10,000 / mes', 'un_min_val': '$14,000 / mes',
 G+'688': 'Suscripciones: 100,000 trx × $0.02', G+'689': '$2,000', G+'690': '$24,000',
 G+'693': '$10,000', G+'694': '$120,000', 'un_min_r_lbl': 'Facturación mínima: $14,000 (≈95,000 trx)',
 G+'697': '$18,000', G+'698': '$216,000', G+'699': '≈ $0.12 all-in por transacción aprobada.',
 G+'700': 'Facturación mínima mensual: $14,000 ($10,000 de plataforma + $4,000 en transacciones, cerca de 95,000 transacciones aprobadas al mes al ticket de $15; con 150,000 queda cubierta). Suscripciones: 150,000 envíos menos las primeras 50,000 sin costo = 100,000 × $0.02 = $2,000.',
}
diff = [(k, v, text_of(idx[k][0]).strip()) for k, v in V5.items() if text_of(idx[k][0]).strip() != v]
print('manual edits since v5 on the boxes I touch:', diff or 'none')
if diff and 'force' not in sys.argv: sys.exit('STOP: the slide no longer matches v5; review the diff above (add "force" to overwrite)')
reqs = []
def txt(oid, markup): reqs.extend(fmt_requests(idx[oid][0], markup)[0])
# header
txt(G+'334', f'La tarifa empieza en {R1:.2%} por transacción aprobada y baja a {R2:.2%} a partir de {CUT_TX:,} al mes; el motor de suscripciones cuesta {SUBS_S} por transacción enviada, con las primeras {SUBS_FREE:,} del mes sin costo. Fee de plataforma de ${PLATFORM:,} y facturación mínima mensual de ${MIN_BILL:,}.')
# left panel: subscriptions price + minimum billing note
txt('ld_commit_val', f'**{SUBS_S}**/trx')
txt(G+'635', f'Facturación mínima mensual de ${MIN_BILL:,}: ${PLATFORM:,} de plataforma más ${COMMIT:,} en transacciones, cerca de {CT} aprobadas al mes al ticket de ${TICKET}. Si el mes cierra por debajo, se factura la diferencia. Las declinadas no pagan el porcentaje. Sin fee de setup.')
# middle panel: platform fee + minimum rows
txt(G+'665', f'${PLATFORM:,} / mes'); txt('un_min_val', f'${MIN_BILL:,} / mes')
# right panel: subscriptions, platform, minimum, total, all-in, note
txt(G+'688', f'Suscripciones: {SUBS_BILL:,} trx × {SUBS_S}'); txt(G+'689', f'${subs:,.0f}'); txt(G+'690', f'${subs*12:,.0f}')
txt(G+'693', f'${PLATFORM:,}'); txt(G+'694', f'${PLATFORM*12:,}')
txt('un_min_r_lbl', f'Facturación mínima: ${MIN_BILL:,} (≈{CT} trx)')
txt(G+'697', f'${total:,.0f}'); txt(G+'698', f'${total*12:,.0f}')
txt(G+'699', f'≈ **${total/TX:.2f}** all-in por transacción aprobada.')
txt(G+'700', f'Facturación mínima mensual: ${MIN_BILL:,} (${PLATFORM:,} de plataforma + ${COMMIT:,} en transacciones, cerca de {CT} transacciones aprobadas al mes al ticket de ${TICKET}; con {TX:,} queda cubierta). Suscripciones: {SUBS_TX:,} envíos menos las primeras {SUBS_FREE:,} sin costo = {SUBS_BILL:,} × {SUBS_S} = ${subs:,.0f}.')
assert total >= MIN_BILL and COMMIT_TX <= CUT_TX
print('requests:', len(reqs), f'| plataforma ${PLATFORM:,} | mínimo ${MIN_BILL:,} = ${PLATFORM:,} + ${COMMIT:,} -> {COMMIT_TX:,.1f} trx (slide: {CT}) | subs {SUBS_S} x {SUBS_BILL:,} = ${subs:,.0f} | total ${total:,.0f}/mes ${total*12:,.0f}/año | all-in ${total/TX:.2f}')
for r in reqs:
    if 'insertText' in r: print('  ', r['insertText']['objectId'], '->', r['insertText']['text'][:110])
if DRY: sys.exit(0)
run(s, PID, reqs, label='pricing v6: platform $7K, minimum $10K, subscriptions $0.015')
Q = s.presentations().get(presentationId=PID).execute(); json.dump(Q, open(f'{WORK}/deck_final_v6.json', 'w'))
n = [x['objectId'] for x in Q['slides']].index(G+'331') + 1
thumbs(s, Q, [n], 'fix6'); print('slides:', len(Q['slides']), '| thumb slide', n, '->', f'{WORK}/fix6_{n:02d}.png')
