# -*- coding: utf-8 -*-
"""Civitatis x Yuno proposal: fill the business case (slides 13 and 14) on German's copy of Alejandro's deck.
Five levers, Cruz Verde method (Deals/Cruz Verde/build/rebuild_bc_cruzverde.py), pure text replacement because
Alejandro's deck already has five cards and five columns. Object IDs survive a Drive copy, so the IDs below
(read from the original 1I176rhzowROapMxhyIJXcaLSfZhefKSkDbcAeIblLb8 on 2026-10-25) are the same on the copy.

  python3 fill_bc_civitatis.py <presentationId> dry      # validate IDs and current text, print requests
  python3 fill_bc_civitatis.py <presentationId> apply    # write, then save thumbnails of slides 13 and 14
"""
import sys, os, json, urllib.request, warnings
warnings.filterwarnings('ignore')
sys.path.insert(0, '/Users/germantatis/Desktop/GTMCoding/Industry/AI/Higgsfield/build')
from engine import elements, text_of, replace_requests, run
from google.oauth2 import service_account
from googleapiclient.discovery import build

HERE = os.path.dirname(os.path.abspath(__file__))
PID = sys.argv[1]
MODE = sys.argv[2] if len(sys.argv) > 2 else 'dry'
creds = service_account.Credentials.from_service_account_file(os.path.expanduser('~/.config/gsuite/sa.json'),
        scopes=['https://www.googleapis.com/auth/presentations'])
svc = build('slides', 'v1', credentials=creds, cache_discovery=False)
P = svc.presentations().get(presentationId=PID).execute()
json.dump(P, open(f'{HERE}/deck_before_bc.json', 'w'))
idx = {el['objectId']: el for s in P['slides'] for el, tr in elements(s)}
print('deck:', P['title'], '| slides:', len(P['slides']))

# ---------------- numbers (see ../civitatis-business-case-2026-10-25.md) ----------------
# Base 38,000 pay-ins/mes x USD 157.89 = USD 6.0M/mes = USD 72M/ano. 90% approval -> ~42,200 attempts/mes.
# L1 +1.5 pp / +3 pp = $1.20M / $2.40M. L2 +2% / +5% of volume = $1.44M / $3.60M. L3 10/20 bps = $72K / $144K.
# L4 7 direct integrations: build 8-12 wk x 2 eng at $60K/FTE, 20-30% maintenance + 1-2 new/yr avoided = $45K / $115K.
# L5 1-2 FTE at $60K = $60K / $120K. Totals $2.82M / $6.38M, average $4.60M. Investment $9,234/mes = $110,808/yr.

reqs = []; sim = {}
def txt(oid, new, expect=None):
    el = idx[oid]
    cur = text_of(el).strip()
    if expect is not None and not cur.startswith(expect):
        raise SystemExit(f'ID {oid}: expected text starting "{expect}", found "{cur[:60]}"')
    reqs.extend(replace_requests(el, new)); sim[oid] = new
def font(oid, pt):
    reqs.append({'updateTextStyle': {'objectId': oid, 'textRange': {'type': 'ALL'},
                 'style': {'fontSize': {'magnitude': pt, 'unit': 'PT'}}, 'fields': 'fontSize'}})

# ---------------- slide 13 (p14): five lever cards ----------------
txt('p14_i5618', 'Cinco palancas: aprobación y métodos locales son las dos más grandes', 'Cinco palancas')
txt('p14_i5620', 'Base Civitatis LATAM: 38,000 pay-ins al mes, ticket promedio USD 157.89, cerca de USD 6M al mes y USD 72M al año en MX, BR, AR, CO, CL y PE. Stack: dLocal, Ebanx, PayPal, MercadoPago, Amex, Adyen y Checkout.com. Aprobación de tarjeta cerca de 90%, chargebacks 0.35%.', 'Baseline')

CARDS = [
 # (title_id, metric_id, body_id, cons_id, opt_id, title, metric, body, cons, opt)
 ('p14_i5630', 'p14_i5633', 'p14_i5634', 'p14_i5637', 'p14_i5640',
  'Aprobación y ruteo', '+1.5 a +3 pp',
  'Con cerca de 42,000 intentos al mes y 90% de aprobación, unas 4,200 reservas se pierden cada mes. Rutear por BIN, país y método entre sus 7 PSPs y reintentar los rechazos técnicos en otra ruta recupera entre 1.5 y 3 puntos.',
  '$1.20M/año', '$2.40M/año'),
 ('p14_i5642', 'p14_i5645', 'p14_i5646', 'p14_i5649', 'p14_i5652',
  'Métodos LATAM', '+2% a +5% trx',
  'Civitatis quiere cubrir los métodos que suman el 90% del volumen en cada país. Pix ya es el 42% del ecommerce en Brasil, PSE cerca de un tercio en Colombia y las transferencias el 15% en Argentina. Cada método se activa por ruteo, sin desarrollo.',
  '$1.44M/año', '$3.60M/año'),
 ('p14_i5654', 'p14_i5657', 'p14_i5658', 'p14_i5661', 'p14_i5664',
  'Costo multi-PSP', '10 a 20 bps',
  'Con 7 PSPs en el stack, cada transacción va al proveedor más barato a igual aprobación: adquirencia local frente a cross-border, débito frente a crédito, cuotas. 10 a 20 bps sobre cerca de USD 72M al año. Se calibra con sus tarifas actuales.',
  '$72K/año', '$144K/año'),
 ('p14_i5666', 'p14_i5669', 'p14_i5670', 'p14_i5673', 'p14_i5676',
  'Costo de integrar', '7 → 1',
  'Mantener 7 integraciones directas cuesta cada año entre 20% y 30% de lo que costó construirlas (8 a 12 semanas y 2 ingenieros cada una), y sumar un método o PSP nuevo es otro proyecto. Con Yuno es configuración, no desarrollo.',
  '$45K/año', '$115K/año'),
 ('p14_i5681', 'p14_i5684', 'p14_i5685', 'p14_i5688', 'p14_i5691',
  'Operación multi-PSP', '1 a 2 FTE',
  'Conciliación, reportes y monitoreo unificados para los 7 proveedores desde un solo dashboard, sin trabajo manual por PSP. Libera entre 1 y 2 personas de finanzas y operaciones para tareas de más valor.',
  '$60K/año', '$120K/año'),
]
for tid, mid, bid, cid, oid, t, m, b, cv, ov in CARDS:
    txt(tid, t); txt(mid, m); txt(bid, b); txt(cid, cv, 'A cuantificar'); txt(oid, ov, 'A cuantificar')
    font(mid, 15)
txt('p14_i5678', 'Supuestos  Base: 38,000 pay-ins al mes × USD 157.89 (ticket implícito, TPV entre transacciones) = USD 6M al mes, USD 72M al año, según Civitatis. L1: aprobación de tarjeta 90%, cerca de 42,000 intentos al mes; +1.5 pp y +3 pp, supuesto de Yuno. L2: +2% a +5% de transacciones, supuesto de Yuno; cuotas de mercado según Global Payments Report 2026 y guías de PSPs. L3: 10 a 20 bps sobre USD 72M. L4: 7 integraciones, 8 a 12 semanas y 2 ingenieros cada una, 20% a 30% anual de mantenimiento, 1 a 2 integraciones nuevas evitadas al año, USD 60K por FTE. L5: 1 a 2 FTE a USD 60K al año. L1 y L2 miden valor de reservas incrementales; L3 a L5 son costos evitados. Rangos a validar con su data.', 'Supuestos')
font('p14_i5678', 7)

# ---------------- slide 14 (p15): totals table and tiles ----------------
txt('p15_i5696', 'Impacto total: entre $2.8M y $6.4M al año sobre su volumen LATAM', 'Impacto total')
txt('p15_i5715', 'Conservador  90% → 91.5% de aprobación, +2% de transacciones', 'Conservador')
txt('p15_i5727', 'Optimista  90% → 93% de aprobación, +5% de transacciones', 'Optimista')
COLS = {  # lever: (cons_id, opt_id, avg_id, cons, opt, avg)
 'L1': ('p15_i5717', 'p15_i5729', 'p15_i5741', '$1.20M', '$2.40M', '$1.80M'),
 'L2': ('p15_i5719', 'p15_i5731', 'p15_i5743', '$1.44M', '$3.60M', '$2.52M'),
 'L3': ('p15_i5721', 'p15_i5733', 'p15_i5745', '$72K', '$144K', '$108K'),
 'L4': ('p15_i5723', 'p15_i5735', 'p15_i5747', '$45K', '$115K', '$80K'),
 'L5': ('p15_i5768', 'p15_i5770', 'p15_i5772', '$60K', '$120K', '$90K'),
}
for L, (c, o, a, cv, ov, av) in COLS.items():
    txt(c, cv, '—'); txt(o, ov, '—'); txt(a, av, '—')
txt('p15_i5725', '$2.82M', 'A cuantificar'); txt('p15_i5737', '$6.38M', 'A cuantificar'); txt('p15_i5749', '$4.60M', 'A cuantificar')
# tiles
txt('p15_i5751', '$4.3M', '~$6M'); txt('p15_i5752', 'VENTAS INCREMENTALES', 'VOLUMEN')
txt('p15_i5753', 'Palancas 1 y 2. Rechazos recuperados y reservas nuevas por métodos locales, en valor de reservas. Promedio; rango de $2.6M a $6.0M al año.', '~38,000')
txt('p15_i5755', '$278K', '~$9.2K'); txt('p15_i5756', 'COSTOS EVITADOS', 'INVERSIÓN')
txt('p15_i5757', 'Palancas 3, 4 y 5. Ruteo por costo, integraciones que no construyen ni mantienen y menos trabajo manual. Promedio; rango de $177K a $379K al año.', 'Referencia')
txt('p15_i5759', '$111K', '7 PSPs'); txt('p15_i5760', 'INVERSIÓN ANUAL', 'STACK')
txt('p15_i5761', 'Plataforma $7,000 al mes más ladder de pay-ins: $9,234 al mes a 38,000 transacciones, $110,808 al año. 3DS y fraude no incluidos. Detalle en la propuesta.', 'dLocal')
txt('p15_i5763', 'Supuestos  Base: 38,000 pay-ins al mes × USD 157.89 = USD 6M al mes, USD 72M al año (Civitatis LATAM). L1: aprobación de tarjeta 90%, cerca de 42,000 intentos al mes; +1.5 pp y +3 pp, supuesto de Yuno. L2: +2% a +5% de transacciones por métodos locales, supuesto de Yuno. L3: 10 a 20 bps sobre USD 72M. L4: 7 integraciones directas, 8 a 12 semanas y 2 ingenieros cada una, 20% a 30% anual de mantenimiento, 1 a 2 integraciones nuevas evitadas al año, USD 60K por FTE. L5: 1 a 2 FTE a USD 60K al año. L1 y L2 en valor de reservas (TPV), no en comisión neta; L3 a L5 son costos evitados. Chargebacks 0.35% como contexto. Rangos a validar con la data de Civitatis.', 'Supuestos')
font('p15_i5763', 7)

# ---------------- speaker notes with sources (no internal names) ----------------
NOTES = {
 'p14': 'Fuentes y supuestos (oct-2026). Base y stack: datos compartidos por Civitatis (38,000 pay-ins/mes, TPV USD 6M/mes, aprobación de tarjeta ~90%, chargebacks 0.35%, 7 PSPs). Ticket: USD 157.89 implícito (TPV / transacciones); Civitatis Argentina declara públicamente un ticket promedio cercano a USD 150 por actividad (Infonegocios, 2026). Cuotas de mercado L2: Pix 42% del valor del ecommerce en Brasil 2025 y transferencias A2A 15% del ecommerce en Argentina 2025 (Worldpay Global Payments Report 2026); PSE 32% a 34% de las transacciones online en Colombia (Rebill, Antom). L1, L2 rangos y L4/L5 costos: supuestos de modelación de Yuno, a validar con la data de Civitatis.',
 'p15': 'Totales: conservador $2.82M (L1 $1.20M + L2 $1.44M + L3 $72K + L4 $45K + L5 $60K); optimista $6.38M (L1 $2.40M + L2 $3.60M + L3 $144K + L4 $115K + L5 $120K); promedio $4.60M. Ventas incrementales (L1+L2) $2.64M a $6.00M, promedio $4.32M, en valor de reservas. Costos evitados (L3+L4+L5) $177K a $379K, promedio $278K. Inversión: $7,000 plataforma + ladder $0.08 / $0.06 / $0.05 = $9,234/mes a 38,000 trx, $110,808/año; 3DS y fraude aparte.',
}
for sid, note in NOTES.items():
    s = next(x for x in P['slides'] if x['objectId'] == sid)
    nid = s['slideProperties']['notesPage']['notesProperties']['speakerNotesObjectId']
    cur = ''
    for el in s['slideProperties']['notesPage'].get('pageElements', []):
        if el['objectId'] == nid: cur = text_of(el)
    if cur.strip(): reqs.append({'deleteText': {'objectId': nid, 'textRange': {'type': 'ALL'}}})
    reqs.append({'insertText': {'objectId': nid, 'insertionIndex': 0, 'text': note}})

print('requests:', len(reqs), '| texts:', len(sim))
if MODE != 'apply':
    print('dry run, nothing written'); sys.exit(0)
run(svc, PID, reqs, label='civitatis bc')
Q = svc.presentations().get(presentationId=PID).execute(); json.dump(Q, open(f'{HERE}/deck_after_bc.json', 'w'))
for n in (13, 14):
    r = svc.presentations().pages().getThumbnail(presentationId=PID, pageObjectId=Q['slides'][n - 1]['objectId'],
        thumbnailProperties_thumbnailSize='LARGE').execute()
    urllib.request.urlretrieve(r['contentUrl'], f'{HERE}/thumbs/bc_{n:02d}.png')
print('thumbs saved')
