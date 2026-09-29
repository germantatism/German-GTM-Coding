#!/usr/bin/env python3
"""Cruz Verde: solicitud de información, versión sencilla en UNA sola hoja de Google Sheets.

Tres columnas: el campo que pedimos, la respuesta de Cruz Verde (amarillo) y comentarios.
Reemplaza todas las hojas del Sheet, así que se niega a correr si Cruz Verde ya escribió algo.

Requisito: el Sheet compartido como Editor con la service account (~/.config/gsuite/sa.json).
Uso: python3 build_data_request_simple.py
"""
import math
import os
import warnings

warnings.filterwarnings("ignore")

from google.oauth2 import service_account  # noqa: E402
from googleapiclient.discovery import build as gbuild  # noqa: E402

SPREADSHEET_ID = "1xipYBM6dNEVmCj_cxezIAqsfMb-gbPCimMJmXaGIMJQ"
SA_KEY = os.path.expanduser("~/.config/gsuite/sa.json")
GID, TAB = 2000, "Información"

BLUE, LILAC, BLACK, DGRAY = "3E4FE0", "E8EAF5", "282A30", "616366"
INPUT, WHITE, LINE = "FFF4CC", "FFFFFF", "D5D8E6"
WIDTHS = [470, 210, 360]

TITULO = "Cruz Verde + Yuno | Información para el business case"
INSTRUCCIONES = ("Completar las celdas en amarillo. Período: últimos 12 meses, de septiembre de 2025 a agosto de "
                 "2026. Cifras en pesos colombianos. Si un dato no existe, escribir \"No disponible\".")
CIERRE = ("Si les resulta más fácil, pueden enviarnos un export transaccional de Mercado Pago de los últimos 12 "
          "meses, con estado y motivo de rechazo por cada intento de pago, y nosotros calculamos estas cifras. "
          "No necesitamos datos personales ni números completos de tarjeta.")

# (campo, tipo). Tipos: num = cantidad o monto, libre = porcentaje o texto, sino = lista Sí / No
SECCIONES = [
    ("1. Volumen y ventas", [
        ("Intentos de pago al mes, promedio (#)", "num"),
        ("Pagos aprobados al mes, promedio (#)", "num"),
        ("Ventas aprobadas al mes, promedio (COP)", "num"),
        ("Ticket promedio (COP)", "num"),
        ("Pagos aprobados al mes que esperan en 2027 (#)", "num"),
    ]),
    ("2. Mix de medios de pago, sobre los pagos aprobados", [
        ("PSE (%)", "libre"),
        ("Tarjeta de crédito (%)", "libre"),
        ("Tarjeta de débito (%)", "libre"),
        ("Efectivo (%)", "libre"),
        ("Otros medios (%)", "libre"),
    ]),
    ("3. Aprobación", [
        ("Tasa de aprobación en tarjeta de crédito (%)", "libre"),
        ("Tasa de aprobación en tarjeta de débito (%)", "libre"),
        ("Tasa de aprobación en PSE, sobre pagos iniciados (%)", "libre"),
        ("¿Hacen reintentos automáticos cuando un pago es rechazado?", "sino"),
    ]),
    ("4. Rechazos en tarjetas, sobre el total de rechazos", [
        ("Rechazos definitivos (hard): tarjeta vencida, cancelada, reportada o inactiva (%)", "libre"),
        ("Rechazos temporales (soft): fondos insuficientes, error técnico, rechazo genérico (%)", "libre"),
        ("Rechazos por prevención de fraude (%)", "libre"),
        ("Rechazos por datos mal digitados (%)", "libre"),
        ("Los tres motivos de rechazo más frecuentes", "libre"),
        ("Los tres bancos emisores con más rechazos", "libre"),
    ]),
    ("5. Devoluciones y contracargos", [
        ("Devoluciones sobre los pagos aprobados (%)", "libre"),
        ("Devoluciones que corresponden a PSE (%)", "libre"),
        ("Días hasta que el cliente recibe el dinero de una devolución (#)", "num"),
        ("Contracargos sobre los pagos aprobados con tarjeta (%)", "libre"),
    ]),
    ("6. Disponibilidad", [
        ("Caídas o intermitencias de PSE o Mercado Pago en los últimos 12 meses (#)", "num"),
        ("Horas sin servicio en los últimos 12 meses (#)", "num"),
    ]),
    ("7. Costos actuales", [
        ("Comisión por pago con PSE (% o COP por transacción)", "libre"),
        ("Comisión por pago con tarjeta de crédito (%)", "libre"),
        ("Comisión por pago con tarjeta de débito (%)", "libre"),
        ("Comisión por pago en efectivo (% o COP por transacción)", "libre"),
        ("Costo total mensual de procesamiento de pagos (COP)", "num"),
    ]),
    ("8. Conciliación", [
        ("Pagos que no cruzan de forma automática al conciliar (%)", "libre"),
        ("Días que toma el cierre mensual de pagos (#)", "num"),
    ]),
    ("9. Nuevos medios de pago", [
        ("Medios de pago que quieren agregar, en orden de prioridad", "libre"),
        ("Ventas desde dispositivos iOS (%)", "libre"),
        ("Ventas desde dispositivos Android (%)", "libre"),
    ]),
]


def rgb(h):
    return {"red": int(h[0:2], 16) / 255, "green": int(h[2:4], 16) / 255, "blue": int(h[4:6], 16) / 255}


def cell(value=None, bg=WHITE, bold=False, italic=False, color=BLACK, size=10, h="LEFT", border=True,
         number=False, options=None):
    f = {"backgroundColor": rgb(bg), "horizontalAlignment": h, "verticalAlignment": "MIDDLE",
         "wrapStrategy": "WRAP",
         "textFormat": {"fontFamily": "Arial", "fontSize": size, "bold": bold, "italic": italic,
                        "foregroundColor": rgb(color)}}
    if border:
        b = {"style": "SOLID", "color": rgb(LINE)}
        f["borders"] = {"top": b, "bottom": b, "left": b, "right": b}
    if number:
        f["numberFormat"] = {"type": "NUMBER", "pattern": "#,##0"}
    d = {"userEnteredFormat": f}
    if value is not None:
        d["userEnteredValue"] = {"stringValue": value}
    if options:
        d["dataValidation"] = {"condition": {"type": "ONE_OF_LIST",
                                             "values": [{"userEnteredValue": o} for o in options]},
                               "showCustomUi": True, "strict": False}
    return d


def lines(text, px, size=10):
    return max(1, math.ceil(len(text) / max(1, int((px - 10) / (size * 0.62)))))


def main():
    rows, heights, merges = [], [], []

    def full(text, height, **kw):
        merges.append(len(rows))
        d = cell(text, border=False, **kw)
        rows.append([d] + [{"userEnteredFormat": d["userEnteredFormat"]}] * 2)
        heights.append(height)

    full(TITULO, 44, bg=BLUE, bold=True, color=WHITE, size=14)
    full(INSTRUCCIONES, 40, bg=LILAC, color=DGRAY)
    head = dict(bg=BLUE, bold=True, color=WHITE, h="CENTER")
    rows.append([cell("Campo", **head), cell("Respuesta de Cruz Verde", **head),
                 cell("Comentarios (opcional)", **head)])
    heights.append(30)
    n = 0
    for titulo, campos in SECCIONES:
        full(titulo, 28, bg=LILAC, bold=True, size=11)
        for campo, tipo in campos:
            n += 1
            rows.append([cell(campo),
                         cell(None, bg=INPUT, h="RIGHT" if tipo == "num" else "LEFT", number=(tipo == "num"),
                              options=["Sí", "No"] if tipo == "sino" else None),
                         cell(None, bg=INPUT)])
            heights.append(max(28, lines(campo, WIDTHS[0]) * 16 + 12))
    rows.append([cell(border=False)] * 3)
    heights.append(12)
    full(CIERRE, lines(CIERRE, sum(WIDTHS), 9) * 15 + 12, italic=True, color=DGRAY, size=9)

    creds = service_account.Credentials.from_service_account_file(
        SA_KEY, scopes=["https://www.googleapis.com/auth/spreadsheets"])
    api = gbuild("sheets", "v4", credentials=creds, cache_discovery=False).spreadsheets()
    meta = api.get(spreadsheetId=SPREADSHEET_ID, includeGridData=True, fields=(
        "sheets(properties(sheetId,title),data.rowData.values(formattedValue,"
        "userEnteredFormat.backgroundColor))")).execute()
    yellow = rgb(INPUT)
    for s in meta["sheets"]:
        for row in s["data"][0].get("rowData", []):
            for v in row.get("values", []):
                bg = v.get("userEnteredFormat", {}).get("backgroundColor", {})
                if v.get("formattedValue") and all(abs(bg.get(k, 0) - yellow[k]) < .01 for k in yellow):
                    raise SystemExit(f"La hoja \"{s['properties']['title']}\" ya tiene respuestas. No se reemplaza.")

    TMP = 999
    req = [{"addSheet": {"properties": {"sheetId": TMP, "title": "_tmp"}}}]
    req += [{"deleteSheet": {"sheetId": s["properties"]["sheetId"]}} for s in meta["sheets"]]
    req += [
        {"updateSpreadsheetProperties": {"properties": {"locale": "es_CO", "timeZone": "America/Bogota"},
                                         "fields": "locale,timeZone"}},
        {"addSheet": {"properties": {"sheetId": GID, "title": TAB, "index": 0, "tabColor": rgb(BLUE),
                                     "gridProperties": {"rowCount": len(rows) + 2, "columnCount": 3,
                                                        "frozenRowCount": 3, "hideGridlines": True}}}},
        {"deleteSheet": {"sheetId": TMP}},
        {"updateCells": {"rows": [{"values": r} for r in rows],
                         "fields": "userEnteredValue,userEnteredFormat,dataValidation",
                         "start": {"sheetId": GID, "rowIndex": 0, "columnIndex": 0}}},
    ]
    for r in merges:
        req.append({"mergeCells": {"mergeType": "MERGE_ALL", "range": {
            "sheetId": GID, "startRowIndex": r, "endRowIndex": r + 1, "startColumnIndex": 0,
            "endColumnIndex": 3}}})
    for dim, sizes in (("COLUMNS", WIDTHS), ("ROWS", heights)):
        for i, px in enumerate(sizes):
            req.append({"updateDimensionProperties": {
                "range": {"sheetId": GID, "dimension": dim, "startIndex": i, "endIndex": i + 1},
                "properties": {"pixelSize": int(px)}, "fields": "pixelSize"}})
    api.batchUpdate(spreadsheetId=SPREADSHEET_ID, body={"requests": req}).execute()
    print(f"OK {n} campos en {len(SECCIONES)} secciones, una hoja: "
          f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/edit")


if __name__ == "__main__":
    main()
