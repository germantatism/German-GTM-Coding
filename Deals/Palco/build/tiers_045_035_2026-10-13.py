"""Slide 17 (palco_pricing_poc_1013): tier 2 $0.04 -> $0.045 y tier 3 $0.03 -> $0.035, recalcula totales.
Inserta "5" por índice en los precios de tramo (3DS y risk conditions también usan $0.04, por eso no replaceAllText)."""
import os, warnings
warnings.filterwarnings("ignore")
from google.oauth2 import service_account
from googleapiclient.discovery import build
c = service_account.Credentials.from_service_account_file(os.path.expanduser("~/.config/gsuite/sa.json"),
    scopes=["https://www.googleapis.com/auth/presentations"])
s = build("slides", "v1", credentials=c)
PAGE = "palco_pricing_poc_1013"
ins = lambda oid, i: {"insertText": {"objectId": oid, "insertionIndex": i, "text": "5"}}
REPL = [("$2,350", "$2,644"), ("$3,525", "$4,113"),
        ("$8,813", "$9,694"), ("$105,750", "$116,325"), ("$13,813", "$14,694"), ("$165,750", "$176,325"),
        ("$18,173", "$19,054"), ("$218,070", "$228,645"), ("$0.059", "$0.063"), ("$0.077", "$0.081"),
        ("$10,763", "$11,969"), ("$15,763", "$16,969"), ("$0.053", "$0.057")]
reqs = [ins("SLIDES_API339898671_12", 5), ins("SLIDES_API339898671_15", 5),
        ins("SLIDES_API339898671_82", 86), ins("SLIDES_API339898671_82", 59)]
reqs += [{"replaceAllText": {"containsText": {"text": a, "matchCase": True}, "replaceText": b,
                             "pageObjectIds": [PAGE]}} for a, b in REPL]
r = s.presentations().batchUpdate(presentationId="1hWX6sNKKPpXhDSKGlZzrHWyKWMx5WlVxBeScEL_J7UY", body={"requests": reqs}).execute()
print([x.get("replaceAllText", {}).get("occurrencesChanged") for x in r["replies"][4:]])
t = s.presentations().pages().getThumbnail(presentationId="1hWX6sNKKPpXhDSKGlZzrHWyKWMx5WlVxBeScEL_J7UY",
    pageObjectId=PAGE, thumbnailProperties_thumbnailSize="LARGE").execute()
import urllib.request, sys
urllib.request.urlretrieve(t["contentUrl"], sys.argv[1])
