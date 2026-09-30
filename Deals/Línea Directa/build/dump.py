# -*- coding: utf-8 -*-
import sys, json
from common import *
s = svc(); P = s.presentations().get(presentationId=PID).execute()
json.dump(P, open(f'{WORK}/deck_before.json', 'w'))
want = [int(x) for x in sys.argv[1:]] or range(1, len(P['slides']) + 1)
print('slides:', len(P['slides']))
for n, sl in enumerate(P['slides'], 1):
    if n not in want: continue
    print(f"\n##### SLIDE {n} id={sl['objectId']}")
    for el, tr in elements(sl):
        kind = 'shape' if 'shape' in el else ('image' if 'image' in el else ('table' if 'table' in el else ('line' if 'line' in el else 'other')))
        w = el.get('size', {}).get('width', {}).get('magnitude', 0) * tr.get('scaleX', 1) / 12700
        h = el.get('size', {}).get('height', {}).get('magnitude', 0) * tr.get('scaleY', 1) / 12700
        t = text_of(el).strip(); fs = '?'
        if 'shape' in el and 'text' in el['shape']:
            for te in el['shape']['text'].get('textElements', []):
                if 'textRun' in te: fs = te['textRun'].get('style', {}).get('fontSize', {}).get('magnitude', '?'); break
        if kind == 'image' or t or (kind == 'shape' and w > 30 and h > 8):
            print(f"  {kind:5} {el['objectId']} x={pos(el,tr)[0]} y={pos(el,tr)[1]} w={w:.0f} h={h:.0f} {fs}pt | {t.replace(chr(10),' ⏎ ').replace(chr(11),' ⇩ ')[:230]}")
