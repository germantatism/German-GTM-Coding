"""Slide 17 (palco_pricing_poc_1013): el proof of concept cuesta $5,000 al mes."""
import os, sys, warnings, urllib.request
warnings.filterwarnings("ignore")
from google.oauth2 import service_account
from googleapiclient.discovery import build
c = service_account.Credentials.from_service_account_file(os.path.expanduser("~/.config/gsuite/sa.json"),
    scopes=["https://www.googleapis.com/auth/presentations"])
s = build("slides", "v1", credentials=c)
PRES, PAGE = "1hWX6sNKKPpXhDSKGlZzrHWyKWMx5WlVxBeScEL_J7UY", "palco_pricing_poc_1013"
r = s.presentations().batchUpdate(presentationId=PRES, body={"requests": [{"replaceAllText": {
    "containsText": {"text": "de Palco, fee reducido y KPIs", "matchCase": True},
    "replaceText": "de Palco, con un costo de $5,000 al mes y KPIs", "pageObjectIds": [PAGE]}}]}).execute()
print(r["replies"][0]["replaceAllText"].get("occurrencesChanged"))
t = s.presentations().pages().getThumbnail(presentationId=PRES, pageObjectId=PAGE,
    thumbnailProperties_thumbnailSize="LARGE").execute()
urllib.request.urlretrieve(t["contentUrl"], sys.argv[1])
