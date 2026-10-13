"""Slide 17 (palco_pricing_poc_1013): estructura del POC = contrato firmado, 2 meses a $10K/mes,
1 mes para decidir sin penalidad, si siguen 18 meses. Footer a 18 meses."""
import os, sys, warnings, urllib.request
warnings.filterwarnings("ignore")
from google.oauth2 import service_account
from googleapiclient.discovery import build
c = service_account.Credentials.from_service_account_file(os.path.expanduser("~/.config/gsuite/sa.json"),
    scopes=["https://www.googleapis.com/auth/presentations"])
s = build("slides", "v1", credentials=c)
PRES, PAGE = "1hWX6sNKKPpXhDSKGlZzrHWyKWMx5WlVxBeScEL_J7UY", "palco_pricing_poc_1013"
OLD = ("Proof of concept: 2 meses con un cliente de alto volumen de Palco, con un costo de $5,000 al mes y KPIs "
       "acordados al inicio y medidos al cierre. Si se cumplen, el contrato continúa a estos precios.")
NEW = ("Proof of concept: firman el contrato y prueban 2 meses con un cliente de alto volumen de Palco a $10,000 al mes, "
       "con KPIs medidos al inicio y al cierre. Tienen un mes más para decidir: si no siguen, salen sin penalidad; "
       "si siguen, aplica el contrato a 18 meses. Objetivo: en vivo antes de fin de año.")
REPL = [(OLD, NEW), ("Contrato a 3 años.", "Contrato a 18 meses tras el proof of concept.")]
r = s.presentations().batchUpdate(presentationId=PRES, body={"requests": [
    {"replaceAllText": {"containsText": {"text": a, "matchCase": True}, "replaceText": b, "pageObjectIds": [PAGE]}}
    for a, b in REPL]}).execute()
print([x["replaceAllText"].get("occurrencesChanged") for x in r["replies"]])
t = s.presentations().pages().getThumbnail(presentationId=PRES, pageObjectId=PAGE,
    thumbnailProperties_thumbnailSize="LARGE").execute()
urllib.request.urlretrieve(t["contentUrl"], sys.argv[1])
