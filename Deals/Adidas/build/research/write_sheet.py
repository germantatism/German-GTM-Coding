"""Write gaps.json to the internal Google Sheet (two tabs, house format). python3 write_sheet.py <gaps.json> <spreadsheetId>"""
import json, sys, os, collections
GAPS, SID = sys.argv[1], sys.argv[2]
ORDER = ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Mexico', 'Peru', 'Uruguay', 'Bolivia', 'Costa Rica', 'Dominican Republic', 'Ecuador', 'El Salvador', 'Guatemala',
         'Honduras', 'Nicaragua', 'Panama', 'Paraguay', 'Indonesia', 'Malaysia', 'Philippines', 'Singapore', 'Thailand', 'Vietnam', 'Myanmar', 'Israel']
G = json.load(open(GAPS))
H = ['Country', 'Region', 'Type', 'Category', 'Name', 'Why it matters', 'Market relevance', 'On Yuno today', 'Yuno entry', 'Action', 'Source']
rows = [H] + [[r['country'], r['region'], r['type'], r['category'], r['name'], r['why'], r['relevance'], r['on'], r['entry'], r['action'], r['source']] for r in G]
# summary tab
S = [['Country', 'Region', 'Rows', 'Covered', 'Covered via provider', 'Confirm with Integrations', 'Gap: High', 'Gap: Medium', 'High-relevance gaps (not on Yuno)', 'Items to confirm']]
for c in ORDER:
    rs = [r for r in G if r['country'] == c]
    if not rs: continue
    a = collections.Counter(r['action'].split(' (')[0] for r in rs)
    gaps = [r['name'] for r in rs if r['action'] == 'Gap: High']; conf = [r['name'] for r in rs if r['action'] == 'Confirm with Integrations']
    S.append([c, rs[0]['region'], len(rs), a['Covered'], a['Covered via provider'], a['Confirm with Integrations'], a['Gap: High'], a['Gap: Medium'], '; '.join(gaps), '; '.join(conf)])
TABS = [('Gaps by country', rows), ('Summary', S)]
from google.oauth2 import service_account
from googleapiclient.discovery import build
cr = service_account.Credentials.from_service_account_file(os.path.expanduser('~/.config/gsuite/sa.json'), scopes=['https://www.googleapis.com/auth/spreadsheets'])
api = build('sheets', 'v4', credentials=cr, cache_discovery=False).spreadsheets()
meta = api.get(spreadsheetId=SID, fields='sheets.properties').execute()
existing = {s['properties']['title']: s['properties']['sheetId'] for s in meta['sheets']}
reqs = []
for i, (t, v) in enumerate(TABS):
    if t not in existing: reqs.append({'addSheet': {'properties': {'title': t, 'index': i, 'gridProperties': {'rowCount': len(v) + 5, 'columnCount': len(v[0])}}}})
    else: reqs.append({'updateSheetProperties': {'properties': {'sheetId': existing[t], 'index': i, 'gridProperties': {'rowCount': len(v) + 5, 'columnCount': len(v[0])}}, 'fields': 'index,gridProperties(rowCount,columnCount)'}})
res = api.batchUpdate(spreadsheetId=SID, body={'requests': reqs}).execute()
for r in res.get('replies', []):
    if 'addSheet' in r: existing[r['addSheet']['properties']['title']] = r['addSheet']['properties']['sheetId']
for t0, sid0 in list(existing.items()):
    if t0 not in dict(TABS): api.batchUpdate(spreadsheetId=SID, body={'requests': [{'deleteSheet': {'sheetId': sid0}}]}).execute(); existing.pop(t0)
api.values().batchClear(spreadsheetId=SID, body={'ranges': [f"'{t}'" for t, _ in TABS]}).execute()
api.values().batchUpdate(spreadsheetId=SID, body={'valueInputOption': 'RAW', 'data': [{'range': f"'{t}'!A1", 'values': v} for t, v in TABS]}).execute()
NAVY = {'red': 0x10 / 255, 'green': 0x28 / 255, 'blue': 0x4A / 255}; WHITE = {'red': 1, 'green': 1, 'blue': 1}
thin = {'style': 'SOLID', 'width': 1, 'color': {'red': 0.8, 'green': 0.8, 'blue': 0.8}}
W = {'Gaps by country': [130, 100, 110, 150, 210, 460, 90, 160, 320, 170, 260], 'Summary': [130, 100, 60, 70, 90, 100, 70, 80, 420, 420]}
fmt = []
for t, v in TABS:
    sid = existing[t]; ncol = len(v[0]); nrow = len(v)
    rng = {'sheetId': sid, 'startRowIndex': 0, 'endRowIndex': nrow, 'startColumnIndex': 0, 'endColumnIndex': ncol}
    fmt += [{'repeatCell': {'range': rng, 'cell': {'userEnteredFormat': {'textFormat': {'fontFamily': 'Roboto', 'fontSize': 10}, 'verticalAlignment': 'TOP', 'wrapStrategy': 'WRAP'}}, 'fields': 'userEnteredFormat(textFormat,verticalAlignment,wrapStrategy)'}},
            {'repeatCell': {'range': {**rng, 'endRowIndex': 1}, 'cell': {'userEnteredFormat': {'backgroundColor': NAVY, 'textFormat': {'fontFamily': 'Roboto', 'fontSize': 10, 'bold': True, 'foregroundColor': WHITE}, 'verticalAlignment': 'MIDDLE', 'wrapStrategy': 'WRAP'}}, 'fields': 'userEnteredFormat(backgroundColor,textFormat,verticalAlignment,wrapStrategy)'}},
            {'updateBorders': {'range': rng, 'top': thin, 'bottom': thin, 'left': thin, 'right': thin, 'innerHorizontal': thin, 'innerVertical': thin}},
            {'updateSheetProperties': {'properties': {'sheetId': sid, 'gridProperties': {'frozenRowCount': 1, 'frozenColumnCount': 1, 'hideGridlines': True}}, 'fields': 'gridProperties(frozenRowCount,frozenColumnCount,hideGridlines)'}}]
    for ci, w in enumerate(W[t][:ncol]):
        fmt.append({'updateDimensionProperties': {'range': {'sheetId': sid, 'dimension': 'COLUMNS', 'startIndex': ci, 'endIndex': ci + 1}, 'properties': {'pixelSize': w}, 'fields': 'pixelSize'}})
    if t == 'Gaps by country':   # colour the Action column
        col = H.index('Action')
        for txt, color in [('Gap: High', {'red': 0.98, 'green': 0.85, 'blue': 0.85}), ('Gap: Medium', {'red': 1, 'green': 0.95, 'blue': 0.8}), ('Confirm', {'red': 0.88, 'green': 0.92, 'blue': 1}), ('Covered', {'red': 0.88, 'green': 0.96, 'blue': 0.88})]:
            fmt.append({'addConditionalFormatRule': {'rule': {'ranges': [{'sheetId': sid, 'startRowIndex': 1, 'endRowIndex': nrow, 'startColumnIndex': col, 'endColumnIndex': col + 1}],
                        'booleanRule': {'condition': {'type': 'TEXT_STARTS_WITH', 'values': [{'userEnteredValue': txt}]}, 'format': {'backgroundColor': color}}}, 'index': 0}})
api.batchUpdate(spreadsheetId=SID, body={'requests': fmt}).execute()
print('written + formatted:', SID, '| rows:', len(rows) - 1, '| summary rows:', len(S) - 1)
