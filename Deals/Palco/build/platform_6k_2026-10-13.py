"""Slide 17 (palco_pricing_poc_1013): platform fee $5,000 -> $6,000, recalcula totales."""
import os, sys, warnings, urllib.request
warnings.filterwarnings("ignore")
from google.oauth2 import service_account
from googleapiclient.discovery import build
c = service_account.Credentials.from_service_account_file(os.path.expanduser("~/.config/gsuite/sa.json"),
    scopes=["https://www.googleapis.com/auth/presentations"])
s = build("slides", "v1", credentials=c)
PRES, PAGE = "1hWX6sNKKPpXhDSKGlZzrHWyKWMx5WlVxBeScEL_J7UY", "palco_pricing_poc_1013"
REPL = [("$5,000", "$6,000"), ("$60,000", "$72,000"),
        ("$14,694", "$15,694"), ("$176,325", "$188,325"), ("$19,054", "$20,054"), ("$228,645", "$240,645"),
        ("$0.063", "$0.067"), ("$0.081", "$0.085"), ("$16,969", "$17,969"), ("$0.057", "$0.060")]
r = s.presentations().batchUpdate(presentationId=PRES, body={"requests": [
    {"replaceAllText": {"containsText": {"text": a, "matchCase": True}, "replaceText": b, "pageObjectIds": [PAGE]}}
    for a, b in REPL]}).execute()
print([x["replaceAllText"].get("occurrencesChanged") for x in r["replies"]])
t = s.presentations().pages().getThumbnail(presentationId=PRES, pageObjectId=PAGE,
    thumbnailProperties_thumbnailSize="LARGE").execute()
urllib.request.urlretrieve(t["contentUrl"], sys.argv[1])
