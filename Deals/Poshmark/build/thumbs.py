import sys, os, urllib.request, time
import gs_lib as g
pid = '1IzB5Cu6PGBEKGJzVGqc4mWpTNyNjLGmBHYyCTV-a7r8'
out = sys.argv[1] if len(sys.argv) > 1 else 'thumbs_v1'
os.makedirs(out, exist_ok=True)
s = g.svc(); P = s.presentations().get(presentationId=pid).execute()
for i, sl in enumerate(P['slides'], 1):
    for a in range(4):
        try:
            t = s.presentations().pages().getThumbnail(presentationId=pid, pageObjectId=sl['objectId'], thumbnailProperties_thumbnailSize='LARGE').execute(); break
        except Exception as e:
            if a < 3: time.sleep(10); continue
            raise
    urllib.request.urlretrieve(t['contentUrl'], f'{out}/s{i:02d}.png')
print('thumbs in', out, len(P['slides']))
