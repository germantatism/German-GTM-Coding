# -*- coding: utf-8 -*-
"""Pricing v7 (German, 8-oct-2026, tras presentar): cuatro tramos por transacciones aprobadas al mes,
0.28% (0 a 50,000), 0.26% (50,000 a 100,000), 0.24% (100,000 a 150,000) y 0.22% (más de 150,000).
Plataforma, suscripciones y mínimo no cambian. Solo toca el slide de pricing.
Panel izquierdo: 4 filas de tramo + suscripciones a paso 26 pt (antes 35) y la nota del mínimo más corta.
Panel derecho: fila nueva "Tramo 3" y todas las filas a paso 14.2 pt (antes 16.6).
Se niega a escribir si el slide no coincide con v6 (añadir "force" para pisar). Usage: python3 fix7_four_tiers.py [dry]"""
import sys, json
from common import *
from model import *
DRY = 'dry' in sys.argv
G = 'g3fb7d86b358_4_'
s = svc(); P = s.presentations().get(presentationId=PID).execute()
json.dump(P, open(f'{WORK}/deck_before_fix7.json', 'w'))
sl = next(x for x in P['slides'] if x['objectId'] == G+'331')
idx = {el['objectId']: (el, tr) for el, tr in elements(sl)}
V6 = {
 G+'334': 'La tarifa empieza en 0.28% por transacción aprobada y baja a 0.24% a partir de 100,000 al mes; el motor de suscripciones cuesta $0.015 por transacción enviada, con las primeras 50,000 del mes sin costo. Fee de plataforma de $7,000 y facturación mínima mensual de $10,000.',
 G+'626': '0 a 100,000 trx aprobadas', G+'627': '0.28%', G+'629': 'Más de 100,000 trx aprobadas', G+'630': '0.24%',
 G+'676': 'Tramo 1: 100,000 trx × $15 × 0.28%', G+'677': '$4,200', G+'678': '$50,400',
 G+'680': 'Tramo 2: 50,000 trx × $15 × 0.24%', G+'681': '$1,800', G+'682': '$21,600',
 G+'685': '$6,000', G+'686': '$72,000', 'un_min_r_lbl': 'Facturación mínima: $10,000 (≈71,000 trx)',
 G+'697': '$14,500', G+'698': '$174,000',
}
diff = [(k, v, text_of(idx[k][0]).strip()) for k, v in V6.items() if text_of(idx[k][0]).strip() != v]
print('manual edits since v6 on the boxes I touch:', diff or 'none')
if diff and 'force' not in sys.argv: sys.exit('STOP: the slide no longer matches v6; review the diff above (add "force" to overwrite)')
reqs = []
def txt(oid, markup): reqs.extend(fmt_requests(idx[oid][0], markup)[0])
def put(oid, x=None, y=None, w=None, h=None):
    el, tr = idx[oid]; x0, y0, w0, h0 = geom(el, tr)
    reqs.append(box_req(el, x0 if x is None else x, y0 if y is None else y, w0 if w is None else w, h0 if h is None else h))
def dup(src, new):
    reqs.append({'duplicateObject': {'objectId': src, 'objectIds': {src: new}}}); idx[new] = (dict(idx[src][0], objectId=new), idx[src][1])
CT = f'{round(COMMIT_TX, -3):,.0f}'          # 73,000
assert len(TIERS) == 4 and ROWS[3][3] == 0, 'el slide asume que el tramo 4 no se alcanza con el estimado'
r1, r2, r3, r4 = (r for _, r in TIERS)
# ---------- header ----------
txt(G+'334', f'La tarifa empieza en {r1:.2%} por transacción aprobada y baja por tramos hasta {r4:.2%} a partir de {TIERS[2][0]:,} al mes; el motor de suscripciones cuesta {SUBS_S} por transacción enviada, con las primeras {SUBS_FREE:,} del mes sin costo. Fee de plataforma de ${PLATFORM:,} y facturación mínima mensual de ${MIN_BILL:,}.')
# ---------- left panel: 4 tier rows + subscriptions, pitch 26 ----------
PITCH = 26.0; Y0 = 140.5                       # value box y of row 1 (label = +5, separator = +24.5)
dup(G+'626', 'un_t3_lbl'); dup(G+'627', 'un_t3_val'); dup(G+'631', 'un_t3_sep')
dup(G+'626', 'un_t4_lbl'); dup(G+'627', 'un_t4_val'); dup(G+'631', 'un_t4_sep')
left = [(G+'626', G+'627', G+'628'), (G+'629', G+'630', G+'631'), ('un_t3_lbl', 'un_t3_val', 'un_t3_sep'), ('un_t4_lbl', 'un_t4_val', 'un_t4_sep')]
labels = ['0 a 50,000 trx', '50,000 a 100,000 trx', '100,000 a 150,000 trx', 'Más de 150,000 trx']
for i, ((lbl_id, val_id, sep_id), (hi, r)) in enumerate(zip(left, TIERS)):
    y = Y0 + i * PITCH
    put(val_id, y=y); put(lbl_id, y=y + 5); put(sep_id, y=y + 24.5)
    txt(lbl_id, labels[i]); txt(val_id, f'**{r:.2%}**')
y = Y0 + 4 * PITCH                              # 244.5: subscriptions row
put('ld_commit_val', y=y); put('ld_commit_lbl', y=y + 5); put('ld_commit_sub', y=y + 19)
put(G+'634', y=276, h=42); put(G+'635', y=279, h=37)
txt(G+'635', f'Mínimo mensual de ${MIN_BILL:,}: ${PLATFORM:,} de plataforma más ${COMMIT:,} en transacciones (cerca de {CT} aprobadas al mes). Si el mes cierra por debajo, se factura la diferencia. Las declinadas no pagan. Sin fee de setup.')
# ---------- right panel: new "Tramo 3" row, pitch 14.2 ----------
dup(G+'680', 'un_t3_r_lbl'); dup(G+'681', 'un_t3_r_m'); dup(G+'682', 'un_t3_r_a'); dup(G+'683', 'un_t3_r_sep')
rows = [((G+'676', G+'677', G+'678'), G+'679'), ((G+'680', G+'681', G+'682'), G+'683'), (('un_t3_r_lbl', 'un_t3_r_m', 'un_t3_r_a'), 'un_t3_r_sep'),
        ((G+'684', G+'685', G+'686'), G+'687'), ((G+'688', G+'689', G+'690'), G+'691'), ((G+'692', G+'693', G+'694'), G+'695'),
        (('un_min_r_lbl', 'un_min_r_m', 'un_min_r_a'), 'un_min_r_sep')]
RP = 14.2; RY0 = 152.5
for i, (cells, sep) in enumerate(rows):
    y = RY0 + i * RP
    for c in cells: put(c, y=y)
    put(sep, y=y + 12.6)
for oid in (G+'696', G+'697', G+'698'): put(oid, y=254.0)
put(G+'699', y=269.5, h=14); put(G+'700', y=285.5, h=33)
for (cells, _), (n, lo, hi, inside, r, amt) in zip(rows[:3], ROWS[:3]):
    txt(cells[0], f'Tramo {n}: {inside:,} trx × ${TICKET} × {r:.2%}'); txt(cells[1], f'${amt:,.0f}'); txt(cells[2], f'${amt*12:,.0f}')
txt(G+'685', f'**${var:,.0f}**'); txt(G+'686', f'**${var*12:,.0f}**')
txt('un_min_r_lbl', f'Facturación mínima: ${MIN_BILL:,} (≈{CT} trx)')
txt(G+'697', f'**${total:,.0f}**'); txt(G+'698', f'**${total*12:,.0f}**')
txt(G+'699', f'≈ **${total/TX:.2f}** all-in por transacción aprobada.')
txt(G+'700', f'Mínimo mensual: ${MIN_BILL:,} (${PLATFORM:,} de plataforma + ${COMMIT:,} en transacciones, cerca de {CT} aprobadas al mes; con {TX:,} queda cubierto). El tramo 4 ({r4:.2%}) aplica por encima de {TIERS[2][0]:,}. Suscripciones: {SUBS_TX:,} envíos menos {SUBS_FREE:,} sin costo = {SUBS_BILL:,} × {SUBS_S} = ${subs:,.0f}.')
assert total >= MIN_BILL
print('requests:', len(reqs), f'| tramos {[f"{r:.2%}" for _, r in TIERS]} | variable ${var:,.0f} | total ${total:,.0f}/mes ${total*12:,.0f}/año | all-in ${total/TX:.2f} | mínimo -> {COMMIT_TX:,.1f} trx (slide: {CT})')
for r in reqs:
    if 'insertText' in r: print('  ', r['insertText']['objectId'], '->', r['insertText']['text'][:120])
if DRY: sys.exit(0)
run(s, PID, reqs, label='pricing v7: four tiers 0.28 / 0.26 / 0.24 / 0.22')
Q = s.presentations().get(presentationId=PID).execute(); json.dump(Q, open(f'{WORK}/deck_final_v7.json', 'w'))
n = [x['objectId'] for x in Q['slides']].index(G+'331') + 1
thumbs(s, Q, [n], 'fix7'); print('slides:', len(Q['slides']), '| thumb slide', n, '->', f'{WORK}/fix7_{n:02d}.png')
