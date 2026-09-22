# -*- coding: utf-8 -*-
"""Push the openpyxl workbook to Google Sheets natively (Sheets API v4) using the gdrive MCP OAuth token."""
import json, os, sys, urllib.request, urllib.parse
from datetime import date, datetime
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter, column_index_from_string, range_boundaries

XLSX = "/Users/germantatis/Desktop/GTMCoding/Travel/SF Sep-Nov 2026/Presupuesto SF Sep28-Nov4 2026.xlsx"
TITLE = "Presupuesto San Francisco · 28-sep → 4-nov-2026 · German"
EXISTING = os.environ.get("SHEET_ID")  # set to update an existing spreadsheet instead of creating

# ---- auth ---------------------------------------------------------------
cfg = json.load(open(os.path.expanduser("~/.claude.json")))
env = cfg["mcpServers"]["gdrive"]["env"]
creds = json.load(open(os.path.expanduser("~/.config/mcp-gdrive/.gdrive-server-credentials.json")))
tok = urllib.parse.urlencode({"client_id": env["CLIENT_ID"], "client_secret": env["CLIENT_SECRET"],
                              "refresh_token": creds["refresh_token"], "grant_type": "refresh_token"}).encode()
access = json.load(urllib.request.urlopen(urllib.request.Request("https://oauth2.googleapis.com/token", data=tok)))["access_token"]

def api(method, url, body=None):
    req = urllib.request.Request(url, data=json.dumps(body).encode() if body is not None else None, method=method,
                                 headers={"Authorization": f"Bearer {access}", "Content-Type": "application/json"})
    try:
        return json.load(urllib.request.urlopen(req))
    except urllib.error.HTTPError as e:
        print(e.read().decode()[:3000]); raise

# ---- converters -----------------------------------------------------------
def color(rgb):
    if not rgb or not isinstance(rgb, str): return None
    h = rgb[-6:]
    try: return {"red": int(h[0:2], 16) / 255, "green": int(h[2:4], 16) / 255, "blue": int(h[4:6], 16) / 255}
    except ValueError: return None

def numfmt(fmt):
    if not fmt or fmt == "General": return None
    if "$" in fmt: return {"type": "CURRENCY", "pattern": fmt.replace('"', "")}
    if "%" in fmt: return {"type": "PERCENT", "pattern": fmt}
    if "yy" in fmt or "mmm" in fmt: return {"type": "DATE", "pattern": fmt}
    return {"type": "NUMBER", "pattern": fmt}

EPOCH = date(1899, 12, 30)
def cell_json(c):
    v = c.value
    out = {}
    if v is None: uev = None
    elif isinstance(v, str) and v.startswith("="): uev = {"formulaValue": v}
    elif isinstance(v, bool): uev = {"boolValue": v}
    elif isinstance(v, (datetime, date)):
        d = v.date() if isinstance(v, datetime) else v
        uev = {"numberValue": (d - EPOCH).days}
    elif isinstance(v, (int, float)): uev = {"numberValue": v}
    else: uev = {"stringValue": str(v)}
    if uev: out["userEnteredValue"] = uev
    f = {}
    tf = {}
    if c.font:
        if c.font.bold: tf["bold"] = True
        if c.font.italic: tf["italic"] = True
        if c.font.size and c.font.size != 11: tf["fontSize"] = int(c.font.size)
        col = color(c.font.color.rgb) if c.font.color is not None and isinstance(c.font.color.rgb, str) else None
        if col and col != {"red": 0, "green": 0, "blue": 0}: tf["foregroundColor"] = col
    if tf: f["textFormat"] = tf
    if c.fill and c.fill.fill_type == "solid":
        bg = color(c.fill.fgColor.rgb if isinstance(c.fill.fgColor.rgb, str) else None)
        if bg: f["backgroundColor"] = bg
    nf = numfmt(c.number_format)
    if nf: f["numberFormat"] = nf
    if c.alignment:
        if c.alignment.wrap_text: f["wrapStrategy"] = "WRAP"
        if c.alignment.vertical == "top": f["verticalAlignment"] = "TOP"
        if c.alignment.vertical == "center": f["verticalAlignment"] = "MIDDLE"
        if c.alignment.horizontal == "center": f["horizontalAlignment"] = "CENTER"
    if c.border and c.border.left and c.border.left.style:
        side = {"style": "SOLID", "color": color("D0D5DD")}
        f["borders"] = {"top": side, "bottom": side, "left": side, "right": side}
    if f: out["userEnteredFormat"] = f
    return out

def grid_range(sheet_id, sqref):
    min_col, min_row, max_col, max_row = range_boundaries(str(sqref))
    return {"sheetId": sheet_id, "startRowIndex": min_row - 1, "endRowIndex": max_row,
            "startColumnIndex": min_col - 1, "endColumnIndex": max_col}

wb = load_workbook(XLSX)
sheets = []
for idx, ws in enumerate(wb.worksheets):
    max_r, max_c = ws.max_row, ws.max_column
    rows = []
    for r in range(1, max_r + 1):
        vals = [cell_json(ws.cell(r, c)) for c in range(1, max_c + 1)]
        rows.append({"values": vals})
    colmeta = []
    for c in range(1, max_c + 1):
        w = ws.column_dimensions[get_column_letter(c)].width
        colmeta.append({"pixelSize": int(w * 7.2 + 8)} if w else {})
    frozen_r = frozen_c = 0
    if ws.freeze_panes:
        fc, fr = ws.freeze_panes[0], ws.freeze_panes[1:]
        letters = "".join(ch for ch in ws.freeze_panes if ch.isalpha()); digits = "".join(ch for ch in ws.freeze_panes if ch.isdigit())
        frozen_r = int(digits) - 1; frozen_c = column_index_from_string(letters) - 1
    sheet = {"properties": {"sheetId": idx, "title": ws.title, "index": idx,
                            "gridProperties": {"rowCount": max_r + 10, "columnCount": max_c + 2,
                                               "frozenRowCount": frozen_r, "frozenColumnCount": frozen_c}},
             "data": [{"startRow": 0, "startColumn": 0, "rowData": rows, "columnMetadata": colmeta}]}
    merges = [grid_range(idx, str(m)) for m in ws.merged_cells.ranges]
    if merges: sheet["merges"] = merges
    sheets.append(sheet)

body = {"properties": {"title": TITLE, "locale": "en_US", "timeZone": "America/Bogota"}, "sheets": sheets}
if EXISTING:
    ss = api("GET", f"https://sheets.googleapis.com/v4/spreadsheets/{EXISTING}?fields=spreadsheetId,spreadsheetUrl,sheets.properties")
    # wipe: delete extra sheets & rewrite via batchUpdate is more complex; for simplicity we only support create here
    print("Update mode not implemented; create a new one instead."); sys.exit(1)
ss = api("POST", "https://sheets.googleapis.com/v4/spreadsheets", body)
sid = ss["spreadsheetId"]; url = ss["spreadsheetUrl"]
print("created", sid, url)

# ---- post-create: data validation + conditional formatting ----------------
reqs = []
for idx, ws in enumerate(wb.worksheets):
    for dv in ws.data_validations.dataValidation:
        if dv.type != "list": continue
        opts = [o.strip() for o in dv.formula1.strip('"').split(",")]
        for sq in str(dv.sqref).split():
            reqs.append({"setDataValidation": {"range": grid_range(idx, sq),
                          "rule": {"condition": {"type": "ONE_OF_LIST", "values": [{"userEnteredValue": o} for o in opts]},
                                   "showCustomUi": True, "strict": True}}})
    for cf in ws.conditional_formatting:
        for rule in cf.rules:
            if rule.type != "cellIs": continue
            op = {"lessThan": "NUMBER_LESS", "greaterThanOrEqual": "NUMBER_GREATER_THAN_EQ", "greaterThan": "NUMBER_GREATER", "lessThanOrEqual": "NUMBER_LESS_THAN_EQ"}[rule.operator]
            bg = color(rule.dxf.fill.fgColor.rgb) if rule.dxf and rule.dxf.fill is not None else None
            if bg is None and rule.dxf and rule.dxf.fill is not None and rule.dxf.fill.bgColor is not None: bg = color(rule.dxf.fill.bgColor.rgb)
            ranges = [grid_range(idx, sq) for sq in str(cf.sqref).split()]
            reqs.append({"addConditionalFormatRule": {"rule": {"ranges": ranges,
                          "booleanRule": {"condition": {"type": op, "values": [{"userEnteredValue": str(rule.formula[0])}]},
                                          "format": {"backgroundColor": bg or color("EEEEEE")}}}, "index": 0}})
if reqs:
    api("POST", f"https://sheets.googleapis.com/v4/spreadsheets/{sid}:batchUpdate", {"requests": reqs})
    print("applied", len(reqs), "validation/format rules")
open("/Users/germantatis/Desktop/GTMCoding/Travel/SF Sep-Nov 2026/sheet_url.txt", "w").write(url + "\n" + sid + "\n")
print(url)
