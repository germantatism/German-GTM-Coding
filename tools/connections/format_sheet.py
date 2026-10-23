"""format_sheet.py <spreadsheet_id> : load the three CSVs into tabs and apply German's house format via the service account."""
import os, sys, csv
from google.oauth2 import service_account
from googleapiclient.discovery import build
SP = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(SP, 'out')
SID = sys.argv[1]
creds = service_account.Credentials.from_service_account_file(os.path.expanduser('~/.config/gsuite/sa.json'), scopes=['https://www.googleapis.com/auth/spreadsheets'])
svc = build('sheets', 'v4', credentials=creds, cache_discovery=False)
meta = svc.spreadsheets().get(spreadsheetId=SID, fields='sheets.properties').execute()
sheets = {s['properties']['title']: s['properties']['sheetId'] for s in meta['sheets']}
first_title = list(sheets)[0]
TABS = [('Missing connections', 'missing.csv', [150, 300, 70, 120, 150, 170, 150, 430, 260, 160]),
        ('Full ranking', 'full_ranking.csv', [150, 300, 70, 120, 150, 170, 150, 430, 260, 160]),
        ('By market', 'by_market.csv', [150, 150, 90, 90, 90, 100, 100, 520])]
reqs = []
# rename the CSV-born first tab, add the other two
reqs.append({'updateSheetProperties': {'properties': {'sheetId': sheets[first_title], 'title': TABS[0][0]}, 'fields': 'title'}})
for title, _, _ in TABS[1:]:
    if title not in sheets: reqs.append({'addSheet': {'properties': {'title': title}}})
res = svc.spreadsheets().batchUpdate(spreadsheetId=SID, body={'requests': reqs}).execute()
meta = svc.spreadsheets().get(spreadsheetId=SID, fields='sheets.properties').execute()
sheets = {s['properties']['title']: s['properties']['sheetId'] for s in meta['sheets']}
# values
data = []
for title, fn, _ in TABS:
    rows = list(csv.reader(open(os.path.join(OUT, fn))))
    data.append({'range': f"'{title}'!A1", 'values': rows})
svc.spreadsheets().values().batchClear(spreadsheetId=SID, body={'ranges': [f"'{t}'!A1:Z5000" for t, _, _ in TABS]}).execute()
svc.spreadsheets().values().batchUpdate(spreadsheetId=SID, body={'valueInputOption': 'RAW', 'data': data}).execute()
# formatting
NAVY = {'red': 0x10/255, 'green': 0x28/255, 'blue': 0x4A/255}; WHITE = {'red': 1, 'green': 1, 'blue': 1}; BLACK = {'red': 0, 'green': 0, 'blue': 0}
border = {'style': 'SOLID', 'width': 1, 'color': BLACK}
fr = []
for title, fn, widths in TABS:
    sid = sheets[title]; rows = list(csv.reader(open(os.path.join(OUT, fn)))); nr, nc = len(rows), len(rows[0])
    fr.append({'updateSheetProperties': {'properties': {'sheetId': sid, 'gridProperties': {'frozenRowCount': 1, 'frozenColumnCount': 1, 'hideGridlines': True}}, 'fields': 'gridProperties.frozenRowCount,gridProperties.frozenColumnCount,gridProperties.hideGridlines'}})
    fr.append({'repeatCell': {'range': {'sheetId': sid, 'startRowIndex': 0, 'endRowIndex': nr, 'startColumnIndex': 0, 'endColumnIndex': nc},
               'cell': {'userEnteredFormat': {'textFormat': {'fontFamily': 'Roboto', 'fontSize': 10}, 'wrapStrategy': 'WRAP', 'verticalAlignment': 'MIDDLE'}}, 'fields': 'userEnteredFormat(textFormat,wrapStrategy,verticalAlignment)'}})
    fr.append({'repeatCell': {'range': {'sheetId': sid, 'startRowIndex': 0, 'endRowIndex': 1, 'startColumnIndex': 0, 'endColumnIndex': nc},
               'cell': {'userEnteredFormat': {'backgroundColor': NAVY, 'textFormat': {'fontFamily': 'Roboto', 'fontSize': 10, 'bold': True, 'foregroundColor': WHITE}, 'horizontalAlignment': 'LEFT', 'verticalAlignment': 'MIDDLE', 'wrapStrategy': 'WRAP'}}, 'fields': 'userEnteredFormat(backgroundColor,textFormat,horizontalAlignment,verticalAlignment,wrapStrategy)'}})
    fr.append({'repeatCell': {'range': {'sheetId': sid, 'startRowIndex': 1, 'endRowIndex': nr, 'startColumnIndex': 0, 'endColumnIndex': 1}, 'cell': {'userEnteredFormat': {'textFormat': {'fontFamily': 'Roboto', 'fontSize': 10, 'bold': True}}}, 'fields': 'userEnteredFormat.textFormat'}})
    fr.append({'updateBorders': {'range': {'sheetId': sid, 'startRowIndex': 0, 'endRowIndex': nr, 'startColumnIndex': 0, 'endColumnIndex': nc}, 'top': border, 'bottom': border, 'left': border, 'right': border, 'innerHorizontal': border, 'innerVertical': border}})
    fr.append({'updateDimensionProperties': {'range': {'sheetId': sid, 'dimension': 'ROWS', 'startIndex': 0, 'endIndex': 1}, 'properties': {'pixelSize': 34}, 'fields': 'pixelSize'}})
    for i, w in enumerate(widths[:nc]):
        fr.append({'updateDimensionProperties': {'range': {'sheetId': sid, 'dimension': 'COLUMNS', 'startIndex': i, 'endIndex': i + 1}, 'properties': {'pixelSize': w}, 'fields': 'pixelSize'}})
    # rating column (C) centered on the two ranking tabs; source column blue
    if fn != 'by_market.csv':
        fr.append({'repeatCell': {'range': {'sheetId': sid, 'startRowIndex': 1, 'endRowIndex': nr, 'startColumnIndex': 2, 'endColumnIndex': 3}, 'cell': {'userEnteredFormat': {'horizontalAlignment': 'CENTER', 'textFormat': {'fontFamily': 'Roboto', 'fontSize': 10, 'bold': True}}}, 'fields': 'userEnteredFormat(horizontalAlignment,textFormat)'}})
        fr.append({'repeatCell': {'range': {'sheetId': sid, 'startRowIndex': 1, 'endRowIndex': nr, 'startColumnIndex': 8, 'endColumnIndex': 9}, 'cell': {'userEnteredFormat': {'textFormat': {'fontFamily': 'Roboto', 'fontSize': 10, 'foregroundColor': {'red': 0, 'green': 0, 'blue': 1}}}}, 'fields': 'userEnteredFormat.textFormat'}})
        # colour scale on rating: 1 light grey -> 10 navy-ish blue text? keep simple: conditional fill for >= 8
        fr.append({'addConditionalFormatRule': {'rule': {'ranges': [{'sheetId': sid, 'startRowIndex': 1, 'endRowIndex': nr, 'startColumnIndex': 2, 'endColumnIndex': 3}],
                   'booleanRule': {'condition': {'type': 'NUMBER_GREATER_THAN_EQ', 'values': [{'userEnteredValue': '8'}]}, 'format': {'backgroundColor': {'red': 1, 'green': 0.92, 'blue': 0.6}}}}, 'index': 0}})
svc.spreadsheets().batchUpdate(spreadsheetId=SID, body={'requests': fr}).execute()
print('formatted', SID, {t: len(list(csv.reader(open(os.path.join(OUT, fn))))) - 1 for t, fn, _ in TABS})
