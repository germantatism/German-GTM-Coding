"""Reemplaza la línea de conciliación/token vault por el proof of concept en la copia del slide de pricing."""
import os, warnings
warnings.filterwarnings("ignore")
from google.oauth2 import service_account
from googleapiclient.discovery import build
c = service_account.Credentials.from_service_account_file(os.path.expanduser("~/.config/gsuite/sa.json"),
    scopes=["https://www.googleapis.com/auth/presentations"])
s = build("slides", "v1", credentials=c)
OLD = "Pendiente de revisión: conciliación y token vault. Alcance y precio se revisan juntos en la siguiente fase."
NEW = ("Proof of concept: 2 meses con un cliente de alto volumen de Palco, fee reducido y KPIs acordados "
       "al inicio y medidos al cierre. Si se cumplen, el contrato continúa a estos precios.")
r = s.presentations().batchUpdate(presentationId="1hWX6sNKKPpXhDSKGlZzrHWyKWMx5WlVxBeScEL_J7UY", body={"requests": [
    {"replaceAllText": {"containsText": {"text": OLD, "matchCase": True}, "replaceText": NEW,
                        "pageObjectIds": ["palco_pricing_poc_1013"]}}]}).execute()
print(r["replies"][0]["replaceAllText"].get("occurrencesChanged", 0))
