# -*- coding: utf-8 -*-
"""Pricing v7b (German, 8-oct-2026): Monitores y alertas incluido en el fee de plataforma (reemplaza la fila
"Una sola integración vía API"); franja inferior solo con conciliación: $0.012 por transacción conciliada
= $1,800 al mes a 150,000 trx (no suma al total). Solo texto, mismos IDs. Usage: python3 fix8_monitors_recon.py [dry]"""
import sys
from common import *
from model import TX
RECON = 1800 / TX                      # $0.012
assert abs(RECON - 0.012) < 1e-9
G = 'g3fb7d86b358_4_'
s = svc(); P = s.presentations().get(presentationId=PID).execute()
sl = next(x for x in P['slides'] if x['objectId'] == G+'331')
idx = {el['objectId']: (el, tr) for el, tr in elements(sl)}
OLD = {G+'649': 'Una sola integración vía API', G+'705': 'OPCIONAL · PARA REVISAR DESPUÉS', G+'706': 'No incluido en esta propuesta.',
       G+'708': 'Conciliación  ·  Monitores y alertas  ·  Network tokens  ·  Nova',
       G+'713': 'Alcance y precio se revisan juntos en una siguiente fase, cuando UNICEF Colombia lo necesite.'}
diff = [(k, v, text_of(idx[k][0]).strip()) for k, v in OLD.items() if text_of(idx[k][0]).strip() != v]
print('manual edits:', diff or 'none')
if diff and 'force' not in sys.argv: sys.exit('STOP')
reqs = []
def txt(oid, m): reqs.extend(fmt_requests(idx[oid][0], m)[0])
txt(G+'649', 'Monitores y alertas')
txt(G+'705', 'OPCIONAL · CONCILIACIÓN')
txt(G+'706', 'No incluido en el total.')
txt(G+'708', f'**${RECON:.3f}** por transacción conciliada  ·  ${RECON*TX:,.0f} al mes a {TX:,} transacciones')
txt(G+'713', 'Un solo reporte configurable con todos los procesadores. Se activa cuando lo necesiten.')
for r in reqs:
    if 'insertText' in r: print(' ', r['insertText']['objectId'], '->', r['insertText']['text'])
if 'dry' in sys.argv: sys.exit(0)
run(s, PID, reqs, label='fix8: monitors in platform, reconciliation only in bottom box')
Q = s.presentations().get(presentationId=PID).execute()
thumbs(s, Q, [15], 'fix8'); print('ok')
