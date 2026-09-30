# -*- coding: utf-8 -*-
"""Second pass after the visual check: two-line intro and shorter first card on the levers slide, tranche-2 price aligned with tranche 1."""
import json
from common import *
from model import *
G = 'g3fb7d86b358_4_'
SRC = json.load(open(f'{WORK}/deck_before.json'))                     # pristine Palco copy: original run styles
sidx = {el['objectId']: el for sl in SRC['slides'] for el, tr in elements(sl)}
s = svc(); P = s.presentations().get(presentationId=PID).execute()
idx = {el['objectId']: (el, tr) for sl in P['slides'] for el, tr in elements(sl)}
def styles(oid): return [(c, st) for c, st in [(te['textRun']['content'], {k: v for k, v in te['textRun'].get('style', {}).items() if k in TEXT_FIELDS})
                         for te in sidx[oid]['shape']['text']['textElements'] if 'textRun' in te] if c.strip()]
FIX = {
 G+'188': f'Sobre **{TX:,} transacciones digitales al mes** y un ticket promedio cercano a **${t_co:.0f} y ${t_pe:.0f}**, Línea Directa recauda por canales digitales cerca de **${tpv/1e6:.0f}M al año.** Cerca del 30% de los pagos aún se hace en puntos físicos y el portal todavía no recibe tarjetas.',
 G+'202': 'Hoy el portal recibe PSE, Bancolombia y Nequi, y cerca del 30% de los pagos aún se hace en puntos físicos. Con tarjeta débito y crédito y más métodos en el mismo checkout, quien no logra pagar con uno tiene otro a un clic. Cada pago a tiempo es un pedido que alcanza la campaña.',
}
reqs = []
for oid, m in FIX.items(): reqs += fmt_requests(idx[oid][0], m, styles(oid))[0]
el, tr = idx[G+'630']; x, y, w, h = geom(el, tr); reqs.append(box_req(el, 161.2, y, w, h))
run(s, PID, reqs, label='fix1')
Q = s.presentations().get(presentationId=PID).execute(); json.dump(Q, open(f'{WORK}/deck_after_fix1.json', 'w'))
thumbs(s, Q, [13, 17], 'fix1')
