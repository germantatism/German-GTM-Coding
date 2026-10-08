# -*- coding: utf-8 -*-
"""Pricing v7c (German, 8-oct-2026): tasas de los cuatro tramos 0.28 / 0.25 / 0.23 / 0.20 (antes 0.28 / 0.26 / 0.24 / 0.22).
Solo texto del slide de pricing, mismos IDs que fix7. Usage: python3 fix9_rates_28_25_23_20.py [dry]"""
import sys
from common import *
from model import *
G = 'g3fb7d86b358_4_'
s = svc(); P = s.presentations().get(presentationId=PID).execute()
sl = next(x for x in P['slides'] if x['objectId'] == G+'331')
idx = {el['objectId']: (el, tr) for el, tr in elements(sl)}
assert text_of(idx[G+'630'][0]).strip() == '0.26%', 'el slide no está en v7'
CT = f'{round(COMMIT_TX, -3):,.0f}'
r1, r2, r3, r4 = (r for _, r in TIERS)
reqs = []
def txt(oid, m): reqs.extend(fmt_requests(idx[oid][0], m)[0])
txt(G+'334', f'La tarifa empieza en {r1:.2%} por transacción aprobada y baja por tramos hasta {r4:.2%} a partir de {TIERS[2][0]:,} al mes; el motor de suscripciones cuesta {SUBS_S} por transacción enviada, con las primeras {SUBS_FREE:,} del mes sin costo. Fee de plataforma de ${PLATFORM:,} y facturación mínima mensual de ${MIN_BILL:,}.')
for oid, r in ((G+'627', r1), (G+'630', r2), ('un_t3_val', r3), ('un_t4_val', r4)): txt(oid, f'**{r:.2%}**')
txt(G+'635', f'Mínimo mensual de ${MIN_BILL:,}: ${PLATFORM:,} de plataforma más ${COMMIT:,} en transacciones (cerca de {CT} aprobadas al mes). Si el mes cierra por debajo, se factura la diferencia. Las declinadas no pagan. Sin fee de setup.')
for (lbl, m, a), (n, lo, hi, inside, r, amt) in zip(((G+'676', G+'677', G+'678'), (G+'680', G+'681', G+'682'), ('un_t3_r_lbl', 'un_t3_r_m', 'un_t3_r_a')), ROWS[:3]):
    txt(lbl, f'Tramo {n}: {inside:,} trx × ${TICKET} × {r:.2%}'); txt(m, f'${amt:,.0f}'); txt(a, f'${amt*12:,.0f}')
txt(G+'685', f'**${var:,.0f}**'); txt(G+'686', f'**${var*12:,.0f}**')
txt('un_min_r_lbl', f'Facturación mínima: ${MIN_BILL:,} (≈{CT} trx)')
txt(G+'697', f'**${total:,.0f}**'); txt(G+'698', f'**${total*12:,.0f}**')
txt(G+'699', f'≈ **${total/TX:.2f}** all-in por transacción aprobada.')
txt(G+'700', f'Mínimo mensual: ${MIN_BILL:,} (${PLATFORM:,} de plataforma + ${COMMIT:,} en transacciones, cerca de {CT} aprobadas al mes; con {TX:,} queda cubierto). El tramo 4 ({r4:.2%}) aplica por encima de {TIERS[2][0]:,}. Suscripciones: {SUBS_TX:,} envíos menos {SUBS_FREE:,} sin costo = {SUBS_BILL:,} × {SUBS_S} = ${subs:,.0f}.')
print(f'total ${total:,.0f}/mes ${total*12:,.0f}/año all-in {total/TX:.4f} min {COMMIT_TX:,.0f}')
if 'dry' in sys.argv: sys.exit(0)
run(s, PID, reqs, label='fix9: rates 0.28/0.25/0.23/0.20')
Q = s.presentations().get(presentationId=PID).execute(); thumbs(s, Q, [15], 'fix9'); print('ok')
