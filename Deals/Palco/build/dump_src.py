import sys, json, urllib.request
sys.path.insert(0,'/Users/germantatis/Desktop/GTMCoding/Industry/AI/Higgsfield/build')
from engine import service, Slide, text_of, pos
SRC='1oH2wwoz3EMYLKNMARaj23AVMf_C-hkPzdfLWnVZfNmc'
svc=service()
P=svc.presentations().get(presentationId=SRC).execute()
json.dump(P,open('src_deck.json','w'))
print("slides:",len(P['slides']), "size:",P['pageSize'])
for n,sl in enumerate(P['slides'],1):
    s=Slide(sl)
    print(f"\n##### SLIDE {n} id={s.id} layout={sl.get('slideProperties',{}).get('layoutObjectId')}")
    for el,tr in s.els:
        kind='shape' if 'shape' in el else ('image' if 'image' in el else ('table' if 'table' in el else ('line' if 'line' in el else 'other')))
        w=el.get('size',{}).get('width',{}).get('magnitude',0)*tr.get('scaleX',1)/12700
        h=el.get('size',{}).get('height',{}).get('magnitude',0)*tr.get('scaleY',1)/12700
        t=text_of(el).strip()
        fs='?'
        if 'shape' in el and 'text' in el['shape']:
            for te in el['shape']['text'].get('textElements',[]):
                if 'textRun' in te: fs=te['textRun'].get('style',{}).get('fontSize',{}).get('magnitude','?'); break
        if kind=='table':
            tb=el['table']; print(f"  TABLE {el['objectId']} x={pos(el,tr)[0]} y={pos(el,tr)[1]} rows={tb['rows']} cols={tb['columns']}")
            for r in tb['tableRows']:
                cells=[]
                for c in r['tableCells']:
                    cells.append(''.join(te.get('textRun',{}).get('content','') for te in c.get('text',{}).get('textElements',[])).strip().replace('\n',' ⏎ '))
                print("     | "+" | ".join(cells))
            continue
        if kind=='image' or t:
            print(f"  {kind:5} {el['objectId']} x={pos(el,tr)[0]} y={pos(el,tr)[1]} w={w:.0f} h={h:.0f} {fs}pt | {t.replace(chr(10),' ⏎ ').replace(chr(11),' ⇩ ')[:150]}")
# thumbnails
for n,sl in enumerate(P['slides'],1):
    r=svc.presentations().pages().getThumbnail(presentationId=SRC,pageObjectId=sl['objectId'],thumbnailProperties_thumbnailSize='LARGE').execute()
    urllib.request.urlretrieve(r['contentUrl'],f"src_{n:02d}.png")
print("thumbs done")
