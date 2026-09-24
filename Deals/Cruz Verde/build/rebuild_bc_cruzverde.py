# -*- coding: utf-8 -*-
"""Business case v2 (German, 24-sep): five levers. L2 = new payment methods (more volume), new L4 = cost of building the
integrations in-house, old L4 (payments operation) becomes L5. Rebuilds S13 (5 cards) and S14 (5 lever columns)."""
import sys, os, json, urllib.request
sys.path.insert(0, '/Users/germantatis/Desktop/GTMCoding/Industry/AI/Higgsfield/build')
from engine import elements, text_of, replace_requests, run
from google.oauth2 import service_account
from googleapiclient.discovery import build
PID = '1VTuUxAAyVVrbEkpce2z2zih3YbfaEEsQ6eUSMZwubxk'
OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
DRY = 'dry' in sys.argv
creds = service_account.Credentials.from_service_account_file(os.path.expanduser('~/.config/gsuite/sa.json'), scopes=['https://www.googleapis.com/auth/presentations'])
svc = build('slides', 'v1', credentials=creds, cache_discovery=False)
P = svc.presentations().get(presentationId=PID).execute()
json.dump(P, open(f'{OUT}/deck_before_bc2.json', 'w'))
idx = {el['objectId']: el for s in P['slides'] for el, tr in elements(s)}
E = lambda n: f'g3fb7d86b358_4_{n}'
reqs = []; sim = {}
def box(oid, x, y, w, h):
    size = idx[oid]['size']
    return {'updatePageElementTransform': {'objectId': oid, 'transform': {'scaleX': w * 12700 / size['width']['magnitude'], 'scaleY': h * 12700 / size['height']['magnitude'],
            'shearX': 0, 'shearY': 0, 'translateX': x * 12700, 'translateY': y * 12700, 'unit': 'EMU'}, 'applyMode': 'ABSOLUTE'}}
def dup(src, new):
    reqs.append({'duplicateObject': {'objectId': src, 'objectIds': {src: new}}})
    el2 = dict(idx[src]); el2['objectId'] = new; idx[new] = el2
def txt(oid, new):
    reqs.extend(replace_requests(idx[oid], new)); sim[oid] = new
def font(oid, pt):
    reqs.append({'updateTextStyle': {'objectId': oid, 'textRange': {'type': 'ALL'}, 'style': {'fontSize': {'magnitude': pt, 'unit': 'PT'}}, 'fields': 'fontSize'}})

# ---------------- S13: five cards ----------------
ROLES = ['bg', 'title', 'dot', 'num', 'metric', 'body', 'cbg', 'cline', 'ctxt', 'obg', 'oline', 'otxt']
BASES = [197, 209, 221, 233]
cards = [{r: E(b + i) for i, r in enumerate(ROLES)} for b in BASES]
c5 = {r: f'cv_c5_{r}' for r in ROLES}
for r in ROLES: dup(cards[3][r], c5[r])
cards.append(c5)
CW, GAP = 113.5, 6.1
XS = [round(97 + i * (CW + GAP), 1) for i in range(5)]
for c, X in zip(cards, XS):
    reqs += [box(c['bg'], X, 137, CW, 169.6), box(c['title'], X + 8, 144, 86, 11.2), box(c['dot'], X + 96, 144, 10.1, 10.1),
             box(c['num'], X + 94, 143, 14.6, 12.4), box(c['metric'], X + 8, 159, CW - 12, 19.1), box(c['body'], X + 8, 179, CW - 13, 74),
             box(c['cbg'], X, 256, CW - 0.6, 25.2), box(c['cline'], X, 256, CW - 0.6, 0.6), box(c['ctxt'], X - 2, 263, CW + 4, 14.7),
             box(c['obg'], X, 282, CW - 0.6, 25.2), box(c['oline'], X, 282, CW - 0.6, 0.6), box(c['otxt'], X - 2, 288, CW + 4, 14.7)]
    font(c['title'], 8); font(c['metric'], 15)
reqs += [box(E(195), 27, 259, 58.5, 26.1), box(E(196), 27, 283, 58.5, 26.1),
         box(E(189), 97, 115, 2 * CW + GAP, 13.5), box(E(190), 97, 117, 2 * CW + GAP, 10.1),
         box(E(191), XS[2], 115, 3 * CW + 2 * GAP, 13.5), box(E(192), XS[2], 117, 3 * CW + 2 * GAP, 10.1)]
LEVERS = [
 ('Aprobación de pagos', '91% → 92.5%',
  'Cruz Verde aprueba el 91% de sus intentos con fraude por debajo de 0.05%: la mayoría de los rechazos son técnicos o del emisor. Reintentar en una segunda ruta, reglas de riesgo afinadas y reintentos automáticos recuperan parte de esos 9 de cada 100.',
  '$0.40M/año', '$0.79M/año'),
 ('Nuevos métodos', '+2% a +5% trx',
  'Hoy no ofrece los métodos que suman cerca del 9% del ecommerce colombiano (billeteras 5%, BNPL 4%) ni Bre-B, con 34.9M de usuarios. Nequi (26M+), Daviplata, Addi (2.7M activos, 47% sin tarjeta de crédito), Apple Pay y Google Pay abren esa demanda.',
  '$0.48M/año', '$1.20M/año'),
 ('Costo transaccional', '10 a 20 bps',
  'Rutear cada transacción al proveedor más barato a igual aprobación, sobre cerca de $24M de TPV al año. Con un solo proveedor no hay con quién comparar; con dos o más, Yuno elige por costo. Se calibra con sus tarifas actuales.',
  '$24K/año', '$48K/año'),
 ('Costo de integrar', '6 métodos',
  'Construir Apple Pay, Google Pay, Addi, Bre-B, Nequi y Daviplata en casa: 8 a 12 semanas de ingeniería por integración (build, certificación y QA), 2 a 3 personas durante 4 a 8 meses y 20% a 30% al año de mantenimiento. Con Yuno se activan sin desarrollo.',
  '$55K/año', '$90K/año'),
 ('Operación de pagos', '1 a 2 FTE',
  'Conciliación automática entre proveedores y nuevos métodos o proveedores activados desde el dashboard, sin desarrollo. Libera al equipo de ecommerce y TI del trabajo manual de conciliar y de cada integración nueva.',
  '$50K/año', '$100K/año'),
]
for c, (t, m, b, cv, ov), n in zip(cards, LEVERS, '12345'):
    txt(c['title'], t); txt(c['metric'], m); txt(c['body'], b); txt(c['ctxt'], cv); txt(c['otxt'], ov); txt(c['num'], n)
txt(E(74), 'Cinco palancas sobre su propia data: aprobación y nuevos métodos de pago son las más grandes')
txt(E(188), 'Sobre 100,000 transacciones al mes y un ticket promedio de $20, Cruz Verde procesa cerca de $24M al año con un solo proveedor, sin billeteras, BNPL ni Bre-B, y con 91% de aprobación: ahí están las dos brechas más grandes.')
txt(E(246), 'Supuestos  Volumen base: 100,000 transacciones al mes y ticket promedio de $20, cerca de $24M al año, según Cruz Verde; aprobación 91% sin reintentos y fraude menor a 0.05%, según su equipo. Mix del ecommerce colombiano según dLocal/AMI; usuarios de Bre-B según el Banco de la República (mayo 2026). Las palancas 1 y 2 miden ventas incrementales; la 3, 4 y 5 son costos evitados. Rangos: supuestos de modelación de Yuno, a validar con su data.')

# ---------------- S14: five lever columns ----------------
CROLES = ['hbg', 'L', 'lbl', 'cbg', 'cv', 'obg', 'ov', 'pbg', 'pv']
CB = [(447, 448, 449, 463, 464, 475, 476, 487, 488), (450, 451, 452, 465, 466, 477, 478, 489, 490),
      (453, 454, 455, 467, 468, 479, 480, 491, 492), (456, 457, 458, 469, 470, 481, 482, 493, 494)]
cols = [{r: E(n) for r, n in zip(CROLES, b)} for b in CB]
k5 = {r: f'cv_k5_{r}' for r in CROLES}
for r in CROLES: dup(cols[3][r], k5[r])
cols.append(k5)
W = 83; CX = [165 + i * W for i in range(5)]
for c, X in zip(cols, CX):
    reqs += [box(c['hbg'], X, 77, W, 27.8), box(c['L'], X, 83, W - 7.3, 10.1), box(c['lbl'], X, 91, W - 7.3, 9.8),
             box(c['cbg'], X, 105, W, 38.4), box(c['cv'], X + 3, 113, W - 11.2, 23.8),
             box(c['obg'], X, 143, W, 38.4), box(c['ov'], X + 3, 151, W - 11.2, 23.8),
             box(c['pbg'], X, 181, W, 31.6), box(c['pv'], X + 3, 190, W - 11.2, 16.9)]
reqs += [box(E(445), 31, 77, 134, 27.8), box(E(446), 42, 85, 118, 14.2), box(E(461), 31, 105, 134, 38.4), box(E(462), 42, 113, 118, 23.8),
         box(E(473), 31, 143, 134, 38.4), box(E(474), 42, 151, 118, 23.8), box(E(485), 31, 181, 134, 31.6), box(E(486), 42, 190, 118, 16.9),
         box(E(459), 580, 77, 109, 27.8), box(E(460), 586, 85, 91, 14.2), box(E(471), 580, 105, 109, 38.4), box(E(472), 586, 113, 91, 23.8),
         box(E(483), 580, 143, 109, 38.4), box(E(484), 586, 151, 91, 23.8), box(E(495), 580, 181, 109, 31.6), box(E(496), 586, 190, 91, 16.9),
         box(E(508), 486, 251, 197.9, 27.6)]
HDR = [('L1', 'APROBACIÓN'), ('L2', 'NUEVOS MÉTODOS'), ('L3', 'COSTO'), ('L4', 'INTEGRACIONES'), ('L5', 'OPERACIÓN')]
VALS = [('$0.40M', '$0.79M', '$0.59M'), ('$0.48M', '$1.20M', '$0.84M'), ('$24K', '$48K', '$36K'), ('$55K', '$90K', '$73K'), ('$50K', '$100K', '$75K')]
for c, (L, lbl), (cv, ov, pv) in zip(cols, HDR, VALS):
    txt(c['L'], L); txt(c['lbl'], lbl); txt(c['cv'], cv); txt(c['ov'], ov); txt(c['pv'], pv)
txt(E(462), 'Conservador  91% → 92.5% de aprobación, +2% de transacciones')
txt(E(474), 'Optimista  91% → 94% de aprobación, +5% de transacciones')
txt(E(472), '$1.00M'); txt(E(484), '$2.23M'); txt(E(496), '$1.62M')
txt(E(498), '$1.43M'); txt(E(499), 'VENTAS INCREMENTALES')
txt(E(500), 'Palancas 1 y 2. Rechazos recuperados y compras nuevas por los métodos que hoy no ofrece. Entran directo a Cruz Verde. Rango de $0.88M a $1.99M.')
txt(E(506), '$148K'); txt(E(507), 'INTEGRACIONES Y OPERACIÓN')
txt(E(508), 'Palancas 4 y 5. Seis integraciones que no construyen ni mantienen, y menos trabajo manual de conciliación. Rango de $105K a $190K.')
txt(E(514), 'Supuestos  Base: 100,000 transacciones al mes × $20 = $24M al año. L1: aprobación 91% sin reintentos (cerca de 110,000 intentos al mes); +1.5 pp y +3 pp, supuesto de Yuno. L2: billeteras 5% y BNPL 4% del ecommerce colombiano (dLocal/AMI); Bre-B 34.9M de usuarios (Banco de la República, mayo 2026); Nequi 26M+, Addi 2.7M activos; captura de +2% a +5% de transacciones, supuesto de Yuno. L3: 10 a 20 bps sobre $24M de TPV. L4: 6 integraciones a 8 a 12 semanas de ingeniería cada una más 20% a 30% anual de mantenimiento, a $50K por FTE; costo evitado del año 1; Bre-B vía proveedores conectados, a confirmar. L5: 1 a 2 FTE a $50K al año. Rangos a validar con su data.')
print('requests:', len(reqs), '| texts:', len(sim))
if DRY: print('dry run'); sys.exit(0)
run(svc, PID, reqs, label='bc v2')
Q = svc.presentations().get(presentationId=PID).execute(); json.dump(Q, open(f'{OUT}/deck_after_bc2.json', 'w'))
for n in (13, 14):
    r = svc.presentations().pages().getThumbnail(presentationId=PID, pageObjectId=Q['slides'][n - 1]['objectId'], thumbnailProperties_thumbnailSize='LARGE').execute()
    urllib.request.urlretrieve(r['contentUrl'], f'{OUT}/bc2_{n:02d}.png')
print('thumbs done')
