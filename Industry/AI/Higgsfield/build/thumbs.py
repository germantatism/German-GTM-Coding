"""usage: python3 thumbs.py 1-16  -> downloads LARGE thumbnails to ../thumbs/S##.png for that slide range"""
import sys, urllib.request, os
from engine import service
COPY='17V3SJ4ErlM_8RMq46XG0nRkdau9NYAYz4rX3ilDxI8g'
a,b=[int(x) for x in sys.argv[1].split('-')]; svc=service(); P=svc.presentations().get(presentationId=COPY).execute()
out=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','thumbs'); os.makedirs(out,exist_ok=True)
for n in range(a,b+1):
    th=svc.presentations().pages().getThumbnail(presentationId=COPY,pageObjectId=P['slides'][n-1]['objectId'],thumbnailProperties_thumbnailSize='LARGE').execute()
    urllib.request.urlretrieve(th['contentUrl'],f"{out}/S{n:02d}.png"); print(f"S{n:02d} -> {out}/S{n:02d}.png")
