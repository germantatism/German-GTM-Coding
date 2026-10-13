"""Slide inglés (palco_pricing_poc_en_1013): ensancha cajas que se partían tras traducir.
Etiquetas crecen a la derecha; valores ("Included", "$6,000 / month") crecen a la izquierda manteniendo el borde derecho."""
import os, sys, warnings, urllib.request
warnings.filterwarnings("ignore")
from google.oauth2 import service_account
from googleapiclient.discovery import build
c = service_account.Credentials.from_service_account_file(os.path.expanduser("~/.config/gsuite/sa.json"),
    scopes=["https://www.googleapis.com/auth/presentations"])
s = build("slides", "v1", credentials=c)
PRES, PAGE = "1hWX6sNKKPpXhDSKGlZzrHWyKWMx5WlVxBeScEL_J7UY", "palco_pricing_poc_en_1013"
PT = 12700
LABELS = {"0 to 58,750 trx": 105, "58,751 to 117,500 trx": 105, "Payment methods": 135, "Fraud provider connections": 135,
          "Sub-accounts per client": 135, "Reporting and dashboard": 135, "Dedicated team (KAM and TAM)": 135}
VALUES = {"Included": 36, "$6,000 / month": 58}
pg = s.presentations().pages().get(presentationId=PRES, pageObjectId=PAGE).execute()
reqs = []
for e in pg["pageElements"]:
    tes = e.get("shape", {}).get("text", {}).get("textElements", [])
    full = "".join(t.get("textRun", {}).get("content", "") for t in tes).strip()
    tr, w = dict(e["transform"]), e["size"]["width"]["magnitude"]
    cur = w * tr.get("scaleX", 1)
    if full in LABELS:
        tr["scaleX"] = LABELS[full] * PT / w
    elif full in VALUES:
        new = VALUES[full] * PT
        tr["translateX"] = tr.get("translateX", 0) + cur - new
        tr["scaleX"] = new / w
    else:
        continue
    tr["unit"] = "EMU"
    reqs.append({"updatePageElementTransform": {"objectId": e["objectId"], "applyMode": "ABSOLUTE", "transform": tr}})
s.presentations().batchUpdate(presentationId=PRES, body={"requests": reqs}).execute()
print(len(reqs), "cajas ajustadas")
t = s.presentations().pages().getThumbnail(presentationId=PRES, pageObjectId=PAGE, thumbnailProperties_thumbnailSize="LARGE").execute()
urllib.request.urlretrieve(t["contentUrl"], sys.argv[1])

# Alinea a la derecha los valores para que cierren en el mismo borde que "+1,000"
pg = s.presentations().pages().get(presentationId=PRES, pageObjectId=PAGE).execute()
al = [{"updateParagraphStyle": {"objectId": e["objectId"], "style": {"alignment": "END"}, "fields": "alignment",
       "textRange": {"type": "ALL"}}} for e in pg["pageElements"]
      if "".join(t.get("textRun", {}).get("content", "") for t in e.get("shape", {}).get("text", {}).get("textElements", [])).strip() in VALUES]
s.presentations().batchUpdate(presentationId=PRES, body={"requests": al}).execute()
t = s.presentations().pages().getThumbnail(presentationId=PRES, pageObjectId=PAGE, thumbnailProperties_thumbnailSize="LARGE").execute()
urllib.request.urlretrieve(t["contentUrl"], sys.argv[1])
