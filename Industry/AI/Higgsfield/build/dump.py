"""usage: python3 dump.py 23 -> prints every text element of slide 23 with objectId, x,y (pt), font size and text"""
import sys, json
from engine import service, Slide, text_of, pos
COPY='17V3SJ4ErlM_8RMq46XG0nRkdau9NYAYz4rX3ilDxI8g'
n=int(sys.argv[1]); svc=service(); P=svc.presentations().get(presentationId=COPY).execute(); s=Slide(P['slides'][n-1])
print("slide",n,s.id)
for el,tr in s.els:
    t=text_of(el).strip()
    if not t: continue
    fs='?'
    for te in el['shape']['text'].get('textElements',[]):
        if 'textRun' in te: fs=te['textRun'].get('style',{}).get('fontSize',{}).get('magnitude','?'); break
    w=el['size']['width']['magnitude']*tr.get('scaleX',1)/12700
    print(f"{el['objectId']} | x={pos(el,tr)[0]} y={pos(el,tr)[1]} w={w:.0f} | {fs}pt | {t.replace(chr(10),' ⏎ ')[:140]}")
