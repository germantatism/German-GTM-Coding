# -*- coding: utf-8 -*-
"""Whole-deck QA: forbidden tokens, dashes as punctuation, element overflow past the page, contact sheet of all slides."""
import json, re
from common import *
from content_ld import FORBID
from PIL import Image
s = svc(); P = s.presentations().get(presentationId=PID).execute()
json.dump(P, open(f'{WORK}/deck_final.json', 'w'))
print('title:', P['title'], '| slides:', len(P['slides']))
ALLOW = {('SEGURIDAD Y RIESGO', 6), ('SEGURIDAD Y RIESGO', 7)}
for n, sl in enumerate(P['slides'], 1):
    for el, tr in elements(sl):
        t = text_of(el).strip()
        for f in FORBID + ['—', '–', 'Cruz Verde', 'Palco4']:
            if f in t and (f, n) not in ALLOW: print(f'  S{n} {el["objectId"]} [{f}] {t[:80]}')
        if 'size' in el and (t or 'image' in el):
            x, y, w, h = geom(el, tr)
            if x + w > 722 or y + h > 407 or x < -2 or y < -2: print(f'  S{n} {el["objectId"]} off-page x={x:.0f} y={y:.0f} w={w:.0f} h={h:.0f} | {t[:40]}')
    for el in sl.get('slideProperties', {}).get('notesPage', {}).get('pageElements', []):
        if text_of(el).strip(): print(f'  S{n} NOTES: {text_of(el).strip()[:100]}')
thumbs(s, P, range(1, len(P['slides']) + 1), 'final')
ims = [Image.open(f'{WORK}/final_{n:02d}.png').convert('RGB').resize((640, 360)) for n in range(1, len(P['slides']) + 1)]
for k in range(0, len(ims), 12):
    part = ims[k:k + 12]; sheet = Image.new('RGB', (640 * 3 + 40, 360 * 4 + 50), 'white')
    for i, im in enumerate(part): sheet.paste(im, (10 + (i % 3) * 650, 10 + (i // 3) * 370))
    sheet.save(f'{WORK}/sheet_{k // 12 + 1}.png')
print('contact sheets done')
