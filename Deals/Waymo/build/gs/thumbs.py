import os,sys,warnings,urllib.request; warnings.filterwarnings('ignore')
from google.oauth2 import service_account
from googleapiclient.discovery import build
from PIL import Image
pid,out=sys.argv[1],sys.argv[2]; only=[int(x) for x in sys.argv[3].split(',')] if len(sys.argv)>3 else None
os.makedirs(out,exist_ok=True)
creds=service_account.Credentials.from_service_account_file(os.path.expanduser('~/.config/gsuite/sa.json'),scopes=['https://www.googleapis.com/auth/presentations'])
svc=build('slides','v1',credentials=creds,cache_discovery=False)
P=svc.presentations().get(presentationId=pid).execute()
for i,sl in enumerate(P['slides'],1):
    if only and i not in only: continue
    r=svc.presentations().pages().getThumbnail(presentationId=pid,pageObjectId=sl['objectId'],thumbnailProperties_thumbnailSize='LARGE').execute()
    urllib.request.urlretrieve(r['contentUrl'],f'{out}/s_{i:02d}.png')
print('ok',len(P['slides']))
