"""Duplica el slide de pricing (g3fb7d86b358_4_331) y aplica la propuesta rebajada del 13-oct-2026:
platform $5,000 + $0.05 / $0.04 / $0.03 (tramos 58,750 / 117,500 / +) a 235,000 tx/mes.
Uso: python3 dup_pricing_poc_2026-10-13.py dry   -> muestra el texto del slide y qué reemplazos aplican
     python3 dup_pricing_poc_2026-10-13.py apply -> duplica y reemplaza solo en la copia
Requiere el deck compartido como Editor con gtm-claude-editor@gtm-claude-tools-260922.iam.gserviceaccount.com
"""
import os, sys, warnings
warnings.filterwarnings("ignore")
from google.oauth2 import service_account
from googleapiclient.discovery import build

PRES = "1hWX6sNKKPpXhDSKGlZzrHWyKWMx5WlVxBeScEL_J7UY"
SRC = "g3fb7d86b358_4_331"
NEW = "palco_pricing_poc_1013"

# Orden importa: valores viejos que coinciden con valores nuevos se cambian primero.
REPL = [
    ("$0.045", "$0.03"), ("$0.055", "$0.04"), ("$0.06", "$0.05"),
    ("$3,525", "$2,938"), ("$5,288", "$3,525"), ("$3,231", "$2,350"),
    ("$42,300", "$35,250"), ("$63,450", "$42,300"), ("$38,775", "$28,200"),
    ("$12,044", "$8,813"), ("$144,525", "$105,750"),
    ("$7,000", "$5,000"), ("$84,000", "$60,000"),
    ("$19,044", "$13,813"), ("$228,525", "$165,750"),
    ("$23,404", "$18,173"), ("$280,845", "$218,070"),
    ("$10,525", "$7,938"), ("6 centavos", "5 centavos"),
    ("$14,969", "$10,763"), ("$21,969", "$15,763"), ("$0.073", "$0.053"), ("$0.081", "$0.059"), ("$0.100", "$0.077"), ("27 bps", "21 bps"),
]

def svc():
    c = service_account.Credentials.from_service_account_file(
        os.path.expanduser("~/.config/gsuite/sa.json"),
        scopes=["https://www.googleapis.com/auth/presentations"])
    return build("slides", "v1", credentials=c)

def slide_text(slide):
    out = []
    def grab(text):
        for t in text.get("textElements", []):
            out.append(t.get("textRun", {}).get("content", ""))
    for e in slide.get("pageElements", []):
        grab(e.get("shape", {}).get("text", {}))
        for row in e.get("table", {}).get("tableRows", []):
            for cell in row["tableCells"]:
                grab(cell.get("text", {}))
    return "".join(out)

def main(mode):
    s = svc()
    p = s.presentations().get(presentationId=PRES).execute()
    src = next(sl for sl in p["slides"] if sl["objectId"] == SRC)
    txt = slide_text(src)
    print(txt)
    print("---- reemplazos con match ----")
    for a, b in REPL:
        if a in txt:
            print(f"{a} -> {b} ({txt.count(a)}x)")
    if mode != "apply":
        return
    reqs = [{"duplicateObject": {"objectId": SRC, "objectIds": {SRC: NEW}}}]
    reqs += [{"replaceAllText": {"containsText": {"text": a, "matchCase": True},
                                 "replaceText": b, "pageObjectIds": [NEW]}} for a, b in REPL]
    s.presentations().batchUpdate(presentationId=PRES, body={"requests": reqs}).execute()
    print(f"OK: copia creada {NEW} justo después del slide original")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "dry")
