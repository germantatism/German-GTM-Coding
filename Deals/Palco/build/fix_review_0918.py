# -*- coding: utf-8 -*-
"""Aplica las correcciones de la revisión del 18-sep (Deals/Palco/palco-proposal-review-2026-09-18.md)
al deck "Propuesta - Palco + Yuno". Requiere token vivo del Slides API
(python3 Deals/Appmaking/build/auth_slides.py <client_secret.json>).

  python3 fix_review_0918.py dry   -> lista coincidencias, no toca el deck
  python3 fix_review_0918.py       -> aplica y baja thumbnails S13/S14/S16/S21 a build/

Cubre: B3 (valor vs costo), B4 (3DS selectivo), B5 (risk conditions $0.014), B6 (base de modelación),
B7 (exitosas → tratadas como aprobadas), M1, M2, M3, M4, M5, M6, M7 (lockup), M9.
No crea slides: B1 (preguntas) y B2 (piloto) se hacen a mano.
"""
import sys, os, urllib.request
sys.path.insert(0, '/Users/germantatis/Desktop/GTMCoding/Industry/AI/Higgsfield/build')
from engine import service, elements, text_of

DECK = '1hWX6sNKKPpXhDSKGlZzrHWyKWMx5WlVxBeScEL_J7UY'
S13 = 'g3fb7d86b358_4_73'     # Cuatro palancas
S14 = 'g3f6c0558646_0_35'     # Impacto total
S16 = 'g3fb7d86b358_4_331'    # Pricing
DRY = len(sys.argv) > 1 and sys.argv[1] == 'dry'
HERE = os.path.dirname(os.path.abspath(__file__))

def rep(old, new, pages=None):
    q = {'replaceAllText': {'containsText': {'text': old, 'matchCase': True}, 'replaceText': new}}
    if pages: q['replaceAllText']['pageObjectIds'] = pages
    return q

R = []
# ---- B6 / B7: base de modelación, no "Palco procesa"; 235,000 sin "exitosas" fuera del pricing
R += [
  rep('Palco procesa cerca de ', 'la base de modelación es de ', [S13]),
  rep('transacciones exitosas al mes', 'transacciones al mes', [S13]),
  rep('cerca de $104.6M al año, según lo compartido por Palco.',
      'según lo compartido por Palco y tratadas como aprobadas: base de modelación de $104.6M al año.', [S13]),
  rep('sobre cerca de $79M de TPV en tarjeta al año (75.7% de su volumen)',
      'sobre el TPV en tarjeta de la base de modelación, cerca de $79M al año (75.7% del volumen)', [S13]),
  rep('transacciones exitosas al mes ×', 'transacciones al mes ×', [S14]),
  rep('= $104.6M al año.', '= $104.6M al año (las 235,000 reportadas por Palco, tratadas como aprobadas).', [S14]),
  rep('L3: 7.5 a 12.5 bps sobre $79M de TPV en tarjeta (75.7% del volumen)',
      'L3: 7.5 a 12.5 bps sobre el TPV en tarjeta de la base, $79M (75.7% del volumen)', [S14]),
]
# ---- M1 / M2
R += [
  rep('Una sola integración reemplaza el mantenimiento de sus 50+ integraciones',
      'Una sola integración libera a su equipo del mantenimiento de sus 50+ integraciones', [S13]),
  rep('el time to market esperado es de 4 a 6 semanas sobre',
      'el time to market se mide en semanas, no meses, sobre', [S13]),
]
# ---- B3: valor vs costo en las tarjetas de S14 y en S16
R += [
  rep('Palco captura su fee de plataforma sobre ese volumen. Rango de $5.2M a $10.2M.',
      'Palco captura su fee sobre ese volumen. Rango de $5.2M a $10.2M: entre 18 y 36 veces el costo anual de Yuno.', [S14]),
  rep('por dejar de mantener sus 50+ integraciones. Rango de $230K a $360K.',
      'por dejar de mantener sus 50+ integraciones. Rango de $230K a $360K: cubre entre 82% y 128% del costo anual de Yuno ($281K).', [S14]),
  rep('con 3DS y antifraude. Baja a medida que crece el volumen.',
      'con 3DS y antifraude, 27 bps sobre un ticket de $37.09. Baja a medida que crece el volumen.', [S16]),
]
# ---- B4: 3DS selectivo, con la cifra a volumen completo
R += [
  rep('3DS (100k autenticaciones)', '3DS selectivo (100k)', [S16]),
  rep('Los volúmenes de 3DS y antifraude son estimados y se ajustan al consumo real.',
      '3DS modelado como selectivo (cerca del 40% de los intentos de tarjeta); en todos los flujos serían unas 250k autenticaciones, $10,000 al mes. Antifraude estimado. Ambos se ajustan al consumo real.', [S16]),
]
# ---- M3 / M4 / M9 / B2 (pie) en S16
R += [
  rep('Herramientas antifraude', 'Conexiones antifraude', [S16]),
  rep('Sin fee de setup. Cada tramo se cobra a su tarifa dentro del mes. Las transacciones declinadas no se cobran.',
      'Sin fee de setup. Un solo contrato y una sola factura a Palco; los tramos se calculan sobre el volumen agregado de todas sus subcuentas. Las declinadas no se cobran.', [S16]),
  rep('Pendiente de revisión: conciliación, network tokens y token vault.',
      'Pendiente de revisión: network tokens, token vault y conciliación (en roadmap).', [S16]),
  rep('Contrato a 3 años.',
      'Piloto en México con baseline propio y revisión a 90 días; plazo y condiciones del contrato se definen al cierre del piloto.', [S16]),
]
# ---- M5 / M6 en el resto del deck (cadenas únicas, sin page scope)
R += [
  rep('Acceso a 300+ métodos locales y globales con una sola integración',
      'Acceso a 1,000+ métodos locales y globales con una sola integración'),
  rep('Un solo libro contable para todos los PSPs.', 'Un solo libro contable para todos los PSPs (roadmap).'),
  rep('para unificar la gestión de pagos', 'para unificar la gestión de pagos (roadmap)'),
  rep('Conciliación reducida de semanas a horas', 'Visibilidad unificada en tiempo real entre proveedores'),
]

svc = service()
P = svc.presentations().get(presentationId=DECK).execute()
pageW = P['pageSize']['width']['magnitude']
slides = P['slides']
print('slides:', len(slides))

# ---- dry: verificar que cada cadena exista (y cuántas veces) antes de aplicar
alltext = {s['objectId']: '\n'.join(text_of(el) for el, _ in elements(s) if 'shape' in el) for s in slides}
for q in R:
    old = q['replaceAllText']['containsText']['text']
    pages = q['replaceAllText'].get('pageObjectIds') or list(alltext)
    n = sum(alltext[p].count(old) for p in pages if p in alltext)
    print(f"{n:2d}x  {old[:75]!r}" + ('' if n else '   <-- NO MATCH'))

# ---- B5: risk conditions $0.04 -> $0.014 insertando "1" dentro del run (conserva azul/negrita)
extra = []
s16 = [s for s in slides if s['objectId'] == S16][0]
for el, _ in elements(s16):
    if 'shape' not in el: continue
    t = text_of(el)
    k = t.find('Risk conditions $0.04')
    if k >= 0:
        idx = k + len('Risk conditions $0.0')
        print('risk conditions en', el['objectId'], 'idx', idx)
        extra.append({'insertText': {'objectId': el['objectId'], 'insertionIndex': idx, 'text': '1'}})

# ---- M7: lockup del cierre cortado a la derecha -> desplazar el grupo hasta 0.5in del borde
last = slides[-1]
els = [(el, tr) for el, tr in elements(last)]
imgs = []
for el, tr in els:
    w = el['size']['width']['magnitude'] * tr.get('scaleX', 1); h = el['size']['height']['magnitude'] * tr.get('scaleY', 1)
    x = tr.get('translateX', 0); y = tr.get('translateY', 0)
    if 'image' in el and x > pageW / 2: imgs.append((el, x, y, w, h))
if imgs:
    right = max(x + w for _, x, y, w, h in imgs)
    dx = (pageW - 457200) - right
    print(f'lockup: borde derecho {right/914400:.2f}in de {pageW/914400:.2f}in -> dx {dx/914400:.2f}in')
    if dx < 0:
        cy = sum(y + h / 2 for _, x, y, w, h in imgs) / len(imgs)
        for el, tr in els:
            x = tr.get('translateX', 0); y = tr.get('translateY', 0)
            h = el['size']['height']['magnitude'] * tr.get('scaleY', 1)
            if x > pageW / 2 and abs((y + h / 2) - cy) < 60 * 12700:
                print('  mover', el['objectId'])
                extra.append({'updatePageElementTransform': {'objectId': el['objectId'], 'applyMode': 'RELATIVE',
                              'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': dx, 'translateY': 0, 'unit': 'EMU'}}})
        logo = os.path.join(HERE, 'logo_url.txt')
        if os.path.exists(logo):
            url = open(logo).read().strip()
            for el, x, y, w, h in imgs:
                extra.append({'replaceImage': {'imageObjectId': el['objectId'], 'url': url, 'imageReplaceMethod': 'CENTER_INSIDE'}})
            print('  wordmark sin tagline desde logo_url.txt')

if DRY:
    print('DRY: nada aplicado'); sys.exit(0)

resp = svc.presentations().batchUpdate(presentationId=DECK, body={'requests': R + extra}).execute()
for q, r in zip(R, resp.get('replies', [])):
    if 'replaceAllText' in q:
        n = r.get('replaceAllText', {}).get('occurrencesChanged', 0)
        print(f"{n:2d}x  {q['replaceAllText']['containsText']['text'][:60]!r}" + ('' if n else '   <-- NO MATCH'))
Q = svc.presentations().get(presentationId=DECK).execute()
for pid, name in ((S13, 's13'), (S14, 's14'), (S16, 's16'), (Q['slides'][-1]['objectId'], 's21')):
    r = svc.presentations().pages().getThumbnail(presentationId=DECK, pageObjectId=pid, thumbnailProperties_thumbnailSize='LARGE').execute()
    urllib.request.urlretrieve(r['contentUrl'], os.path.join(HERE, f'review0918_{name}.png'))
print('thumbnails en build/review0918_*.png: revisar desbordes en S14 tarjetas, S16 caja blanca y nota del panel azul')
