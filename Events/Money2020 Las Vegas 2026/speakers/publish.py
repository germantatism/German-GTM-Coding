"""Write speakers + side events tabs and apply house format via service account."""
import os, sys, csv
from google.oauth2 import service_account
from googleapiclient.discovery import build
SID = sys.argv[1]
s = build("sheets", "v4", credentials=service_account.Credentials.from_service_account_file(
    os.path.expanduser("~/.config/gsuite/sa.json"), scopes=["https://www.googleapis.com/auth/spreadsheets"]))
tabs = [("Speakers ICP", "speakers_icp.csv", [80, 170, 230, 190, 90, 320, 150, 300, 300]),
        ("Side events", "side_events.csv", [300, 200, 160, 200, 300, 330])]
meta = s.spreadsheets().get(spreadsheetId=SID).execute()
first = meta["sheets"][0]["properties"]["sheetId"]
reqs = [{"updateSheetProperties": {"properties": {"sheetId": first, "title": tabs[0][0]}, "fields": "title"}},
        {"addSheet": {"properties": {"title": tabs[1][0]}}}]
r = s.spreadsheets().batchUpdate(spreadsheetId=SID, body={"requests": reqs}).execute()
gids = [first, r["replies"][1]["addSheet"]["properties"]["sheetId"]]
navy = {"red": 16/255, "green": 40/255, "blue": 74/255}
thin = {"style": "SOLID", "width": 1, "color": {}}
reqs = []
for (title, fn, widths), gid in zip(tabs, gids):
    rows = list(csv.reader(open(fn)))
    s.spreadsheets().values().update(spreadsheetId=SID, range=f"'{title}'!A1",
        valueInputOption="RAW", body={"values": rows}).execute()
    n, m = len(rows), len(rows[0])
    reqs += [
     {"updateSheetProperties": {"properties": {"sheetId": gid, "gridProperties": {"frozenRowCount": 1, "frozenColumnCount": 1 if title=="Side events" else 2, "hideGridlines": True}},
       "fields": "gridProperties.frozenRowCount,gridProperties.frozenColumnCount,gridProperties.hideGridlines"}},
     {"repeatCell": {"range": {"sheetId": gid, "startRowIndex": 1, "endRowIndex": n, "endColumnIndex": m},
       "cell": {"userEnteredFormat": {"textFormat": {"fontFamily": "Roboto", "fontSize": 10}, "wrapStrategy": "WRAP", "verticalAlignment": "MIDDLE"}},
       "fields": "userEnteredFormat(textFormat,wrapStrategy,verticalAlignment)"}},
     {"repeatCell": {"range": {"sheetId": gid, "startRowIndex": 0, "endRowIndex": 1, "endColumnIndex": m},
       "cell": {"userEnteredFormat": {"backgroundColor": navy, "textFormat": {"fontFamily": "Roboto", "fontSize": 10, "bold": True, "foregroundColor": {"red": 1, "green": 1, "blue": 1}},
                "horizontalAlignment": "LEFT", "verticalAlignment": "MIDDLE", "wrapStrategy": "WRAP"}},
       "fields": "userEnteredFormat(backgroundColor,textFormat,horizontalAlignment,verticalAlignment,wrapStrategy)"}},
     {"updateBorders": {"range": {"sheetId": gid, "startRowIndex": 0, "endRowIndex": n, "endColumnIndex": m},
       "top": thin, "bottom": thin, "left": thin, "right": thin, "innerHorizontal": thin, "innerVertical": thin}},
     {"updateDimensionProperties": {"range": {"sheetId": gid, "dimension": "ROWS", "startIndex": 0, "endIndex": 1}, "properties": {"pixelSize": 30}, "fields": "pixelSize"}},
     {"deleteDimension": {"range": {"sheetId": gid, "dimension": "ROWS", "startIndex": n, "endIndex": 1000}}},
    ]
    url_col = rows[0].index("Fuente") if "Fuente" in rows[0] else rows[0].index("URL")
    reqs.append({"repeatCell": {"range": {"sheetId": gid, "startRowIndex": 1, "endRowIndex": n, "startColumnIndex": url_col, "endColumnIndex": url_col+1},
        "cell": {"userEnteredFormat": {"textFormat": {"fontFamily": "Roboto", "fontSize": 10, "foregroundColor": {"red": 0, "green": 0, "blue": 1}}}}, "fields": "userEnteredFormat.textFormat"}})
    reqs.append({"repeatCell": {"range": {"sheetId": gid, "startRowIndex": 1, "endRowIndex": n, "startColumnIndex": 1 if title!="Side events" else 0, "endColumnIndex": 2 if title!="Side events" else 1},
        "cell": {"userEnteredFormat": {"textFormat": {"fontFamily": "Roboto", "fontSize": 10, "bold": True}}}, "fields": "userEnteredFormat.textFormat.bold"}})
    for i, w in enumerate(widths):
        reqs.append({"updateDimensionProperties": {"range": {"sheetId": gid, "dimension": "COLUMNS", "startIndex": i, "endIndex": i+1}, "properties": {"pixelSize": w}, "fields": "pixelSize"}})
s.spreadsheets().batchUpdate(spreadsheetId=SID, body={"requests": reqs}).execute()
print("ok")
