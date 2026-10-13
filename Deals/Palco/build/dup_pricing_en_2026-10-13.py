"""Copia el slide 17 (palco_pricing_poc_1013) y lo traduce al inglés para Sean."""
import os, sys, warnings, urllib.request
warnings.filterwarnings("ignore")
from google.oauth2 import service_account
from googleapiclient.discovery import build
c = service_account.Credentials.from_service_account_file(os.path.expanduser("~/.config/gsuite/sa.json"),
    scopes=["https://www.googleapis.com/auth/presentations"])
s = build("slides", "v1", credentials=c)
PRES, SRC, NEW = "1hWX6sNKKPpXhDSKGlZzrHWyKWMx5WlVxBeScEL_J7UY", "palco_pricing_poc_1013", "palco_pricing_poc_en_1013"
T = {
 "Fee de plataforma más tarifa por transacción exitosa": "Platform fee plus a fee per successful transaction",
 "PROPUESTA · PRICING": "PROPOSAL · PRICING",
 "Una tarifa por transacción que empieza en 5 centavos y baja con el volumen, con orquestación, smart routing, monitores y subcuentas incluidos, sobre un fee de plataforma fijo de $6,000 al mes.":
   "A per-transaction fee that starts at 5 cents and drops with volume, with orchestration, smart routing, monitors and sub-accounts included, on top of a fixed platform fee of $6,000 per month.",
 "TARIFA POR TRANSACCIÓN EXITOSA": "FEE PER SUCCESSFUL TRANSACTION",
 "Por transacción exitosa, según el volumen del mes.": "Per successful transaction, based on monthly volume.",
 "0 a 58,750 trx": "0 to 58,750 trx", "58,751 a 117,500 trx": "58,751 to 117,500 trx", "Más de 117,500 trx": "Over 117,500 trx",
 "Sin fee de setup. Cada tramo se cobra a su tarifa dentro del mes. Las transacciones declinadas no se cobran.":
   "No setup fee. Each tier is billed at its own rate within the month. Declined transactions are not charged.",
 "QUÉ CUBRE LA TARIFA": "WHAT THE FEE COVERS",
 "El fee de plataforma se factura por separado.": "The platform fee is billed separately.",
 "Métodos de pago": "Payment methods", "Procesadores": "Processors", "Conexiones antifraude": "Fraud provider connections",
 "Orquestación y motor de reglas": "Orchestration and rules engine", "Smart routing y reintentos": "Smart routing and retries",
 "Monitores y alertas": "Monitors and alerts", "Subcuentas por cliente": "Sub-accounts per client",
 "Reportes y dashboard": "Reporting and dashboard", "Equipo dedicado (KAM y TAM)": "Dedicated team (KAM and TAM)",
 "Incluido": "Included", "Fee de plataforma": "Platform fee",
 "LO QUE SIGNIFICA PARA PALCO": "WHAT IT MEANS FOR PALCO",
 "A 235,000 transacciones exitosas / mes.": "At 235,000 successful transactions / month.",
 "CONCEPTO": "ITEM", "MENSUAL": "MONTHLY", "ANUAL": "ANNUAL",
 "Transacciones exitosas (235k)": "Successful transactions (235k)", "Subtotal pagos": "Payments subtotal",
 "3DS (100k autenticaciones)": "3DS (100k authentications)", "Motor antifraude (20k evaluaciones)": "Fraud engine (20k evaluations)",
 "Total estimado": "Estimated total", "incluye 3DS y antifraude": "incl. 3DS and fraud engine",
 "all-in por transacción exitosa en pagos; ≈": "all-in per successful transaction for payments; ≈",
 "con 3DS y antifraude. Baja a medida que crece el volumen.": "with 3DS and fraud engine. Drops as volume grows.",
 "Desglose a 235,000: 58,750 ×": "Breakdown at 235,000: 58,750 ×", "y 117,500 ×": "and 117,500 ×",
 ". A 300,000 trx/mes:": ". At 300,000 trx/month:", "/ mes ≈": "/ month ≈", "/ mes": "/ month",
 "por trx. Los volúmenes de 3DS y antifraude son estimados y se ajustan al consumo real.":
   "per trx. 3DS and fraud engine volumes are estimates and adjust to actual usage.",
 "SEGURIDAD Y RIESGO": "SECURITY AND RISK",
 "Uso puro, sin mínimos, se factura según consumo.": "Pure usage, no minimums, billed on consumption.",
 "/ autenticación": "/ authentication", "Motor antifraude": "Fraud engine", "/ evaluación": "/ evaluation",
 "/ trx evaluada": "/ trx evaluated",
 "Risk conditions no está incluido en el total estimado: se factura según las transacciones que efectivamente se evalúen.":
   "Risk conditions is not included in the estimated total: billed on the transactions actually evaluated.",
 "Proof of concept: firman el contrato y prueban 2 meses con un cliente de alto volumen de Palco a $10,000 al mes, con KPIs medidos al inicio y al cierre. Tienen un mes más para decidir: si no siguen, salen sin penalidad; si siguen, aplica el contrato a 18 meses. Objetivo: empezar el POC antes de fin de año.":
   "Proof of concept: Palco signs the contract and tests for 2 months with one high-volume Palco client at $10,000 per month, with KPIs measured at the start and at the end. They get one more month to decide: if they don't continue, they exit with no penalty; if they do, the 18-month contract applies. Goal: start the POC before year end.",
 "Contrato a 18 meses tras el proof of concept.": "18-month contract after the proof of concept.",
}
reqs = [{"duplicateObject": {"objectId": SRC, "objectIds": {SRC: NEW}}}]
reqs += [{"replaceAllText": {"containsText": {"text": a, "matchCase": True}, "replaceText": T[a], "pageObjectIds": [NEW]}}
         for a in sorted(T, key=len, reverse=True)]
r = s.presentations().batchUpdate(presentationId=PRES, body={"requests": reqs}).execute()
miss = [a for a, x in zip(sorted(T, key=len, reverse=True), r["replies"][1:]) if not x["replaceAllText"].get("occurrencesChanged")]
print("sin match:", miss)
t = s.presentations().pages().getThumbnail(presentationId=PRES, pageObjectId=NEW, thumbnailProperties_thumbnailSize="LARGE").execute()
urllib.request.urlretrieve(t["contentUrl"], sys.argv[1])
