"""Internal gap analysis sheet (single tab, house format) from research/gaps.json.
python3 write_gaps.py <gaps.json> <spreadsheetId>"""
import json, sys, os
GAPS, SID = sys.argv[1], sys.argv[2]
ORDER = ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Mexico', 'Peru', 'Uruguay', 'Bolivia', 'Costa Rica', 'Dominican Republic', 'Ecuador', 'El Salvador', 'Guatemala',
         'Honduras', 'Nicaragua', 'Panama', 'Paraguay', 'Indonesia', 'Malaysia', 'Philippines', 'Singapore', 'Thailand', 'Vietnam', 'Myanmar', 'Israel']
REGION = {**{c: 'LATAM' for c in ORDER[:17]}, **{c: 'Southeast Asia' for c in ORDER[17:24]}, 'Israel': 'Middle East'}
G = json.load(open(GAPS))
G.sort(key=lambda r: (ORDER.index(r['country']) if r['country'] in ORDER else 99, r.get('kind', ''), {'High': 0, 'Medium': 1}.get(r.get('priority'), 2), r['name']))
rows = [['Country', 'Region', 'Type', 'Name', 'Why it matters', 'On Yuno today', 'Yuno entry', 'Priority', 'Source']]
for r in G:
    rows.append([r['country'], REGION.get(r['country'], ''), r.get('kind', ''), r['name'], r.get('why_it_matters', ''), r.get('on_yuno', ''), r.get('yuno_entry', ''), r.get('priority', ''), r.get('source_url', '')])
print(len(rows) - 1, 'rows')
from google.oauth2 import service_account
from googleapiclient.discovery import build
cr = service_account.Credentials.from_service_account_file(os.path.expanduser('~/.config/gsuite/sa.json'), scopes=['https://www.googleapis.com/auth/spreadsheets'])
api = build('sheets', 'v4', credentials=cr, cache_discovery=False).spreadsheets()
meta = api.get(spreadsheetId=SID, fields='sheets.properties').execute()
sid = meta['sheets'][0]['properties']['sheetId']; title = 'Gaps by country'
api.batchUpdate(spreadsheetId=SID, body={'requests': [{'updateSheetProperties': {'properties': {'sheetId': sid, 'title': title, 'gridProperties': {'rowCount': len(rows) + 5, 'columnCount': len(rows[0])}}, 'fields': 'title,gridProperties(rowCount,columnCount)'}}]}).execute()
api.values().clear(spreadsheetId=SID, range=f"'{title}'").execute()
api.values().update(spreadsheetId=SID, range=f"'{title}'!A1", valueInputOption='RAW', body={'values': rows}).execute()
NAVY = {'red': 0x10 / 255, 'green': 0x28 / 255, 'blue': 0x4A / 255}; WHITE = {'red': 1, 'green': 1, 'blue': 1}
thin = {'style': 'SOLID', 'width': 1, 'color': {'red': 0.8, 'green': 0.8, 'blue': 0.8}}
rng = {'sheetId': sid, 'startRowIndex': 0, 'endRowIndex': len(rows), 'startColumnIndex': 0, 'endColumnIndex': len(rows[0])}
fmt = [
    {'repeatCell': {'range': rng, 'cell': {'userEnteredFormat': {'textFormat': {'fontFamily': 'Roboto', 'fontSize': 10}, 'verticalAlignment': 'TOP', 'wrapStrategy': 'WRAP'}}, 'fields': 'userEnteredFormat(textFormat,verticalAlignment,wrapStrategy)'}},
    {'repeatCell': {'range': {**rng, 'endRowIndex': 1}, 'cell': {'userEnteredFormat': {'backgroundColor': NAVY, 'textFormat': {'fontFamily': 'Roboto', 'fontSize': 10, 'bold': True, 'foregroundColor': WHITE}, 'verticalAlignment': 'MIDDLE', 'wrapStrategy': 'WRAP'}}, 'fields': 'userEnteredFormat(backgroundColor,textFormat,verticalAlignment,wrapStrategy)'}},
    {'updateBorders': {'range': rng, 'top': thin, 'bottom': thin, 'left': thin, 'right': thin, 'innerHorizontal': thin, 'innerVertical': thin}},
    {'updateSheetProperties': {'properties': {'sheetId': sid, 'gridProperties': {'frozenRowCount': 1, 'frozenColumnCount': 1, 'hideGridlines': True}}, 'fields': 'gridProperties(frozenRowCount,frozenColumnCount,hideGridlines)'}},
]
for ci, w in enumerate([140, 110, 120, 190, 420, 110, 190, 90, 260]):
    fmt.append({'updateDimensionProperties': {'range': {'sheetId': sid, 'dimension': 'COLUMNS', 'startIndex': ci, 'endIndex': ci + 1}, 'properties': {'pixelSize': w}, 'fields': 'pixelSize'}})
api.batchUpdate(spreadsheetId=SID, body={'requests': fmt}).execute()
print('written + formatted:', SID)
