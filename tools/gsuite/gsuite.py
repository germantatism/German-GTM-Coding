#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tiny CLI over the Google Sheets / Slides / Docs APIs using ~/.config/gsuite/token.json
(created by tools/gsuite/auth_gsuite.py). Values in/out are JSON.

  gsuite.py sheets meta   <spreadsheetId>
  gsuite.py sheets read   <spreadsheetId> "<Sheet!A1:F50>"
  gsuite.py sheets append <spreadsheetId> "<Sheet!A1>" '[["col1","col2"]]'
  gsuite.py sheets update <spreadsheetId> "<Sheet!A23:F23>" '[["col1","col2"]]'
  gsuite.py slides get    <presentationId>            (slide ids + text per element)
  gsuite.py slides batch  <presentationId> '[{...requests...}]'
  gsuite.py docs   get    <documentId>
  gsuite.py docs   batch  <documentId> '[{...requests...}]'
"""
import json, os, sys
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

TOKEN = os.path.expanduser('~/.config/gsuite/token.json')

def creds():
    c = Credentials.from_authorized_user_file(TOKEN)
    if c.expired and c.refresh_token:
        c.refresh(Request())
        with open(TOKEN, 'w') as fh:
            fh.write(c.to_json())
    return c

def svc(name, version):
    return build(name, version, credentials=creds(), cache_discovery=False)

def out(obj):
    print(json.dumps(obj, ensure_ascii=False, indent=1))

def sheets(args):
    api = svc('sheets', 'v4').spreadsheets()
    cmd, sid = args[0], args[1]
    if cmd == 'meta':
        meta = api.get(spreadsheetId=sid, fields='properties.title,sheets.properties').execute()
        out({'title': meta['properties']['title'],
             'sheets': [{'title': s['properties']['title'], 'gid': s['properties']['sheetId'],
                         'rows': s['properties'].get('gridProperties', {}).get('rowCount'),
                         'cols': s['properties'].get('gridProperties', {}).get('columnCount')}
                        for s in meta['sheets']]})
    elif cmd == 'read':
        out(api.values().get(spreadsheetId=sid, range=args[2]).execute().get('values', []))
    elif cmd == 'append':
        out(api.values().append(spreadsheetId=sid, range=args[2], valueInputOption='USER_ENTERED',
                                insertDataOption='INSERT_ROWS', body={'values': json.loads(args[3])}).execute())
    elif cmd == 'update':
        out(api.values().update(spreadsheetId=sid, range=args[2], valueInputOption='USER_ENTERED',
                                body={'values': json.loads(args[3])}).execute())
    else:
        raise SystemExit(__doc__)

def _texts(elements):
    res = []
    for el in elements or []:
        if 'shape' in el and 'text' in el['shape']:
            txt = ''.join(te.get('textRun', {}).get('content', '') for te in el['shape']['text'].get('textElements', []))
            res.append({'objectId': el['objectId'], 'text': txt.strip()})
        if 'elementGroup' in el:
            res.extend(_texts(el['elementGroup'].get('children')))
        if 'table' in el:
            for r in el['table'].get('tableRows', []):
                for c in r.get('tableCells', []):
                    txt = ''.join(te.get('textRun', {}).get('content', '') for te in c.get('text', {}).get('textElements', []))
                    res.append({'objectId': el['objectId'], 'cell': True, 'text': txt.strip()})
    return res

def slides(args):
    api = svc('slides', 'v1').presentations()
    cmd, pid = args[0], args[1]
    if cmd == 'get':
        p = api.get(presentationId=pid).execute()
        out({'title': p.get('title'), 'slides': [{'index': i + 1, 'objectId': s['objectId'], 'elements': _texts(s.get('pageElements'))}
                                                  for i, s in enumerate(p.get('slides', []))]})
    elif cmd == 'batch':
        out(api.batchUpdate(presentationId=pid, body={'requests': json.loads(args[2])}).execute())
    else:
        raise SystemExit(__doc__)

def docs(args):
    api = svc('docs', 'v1').documents()
    cmd, did = args[0], args[1]
    if cmd == 'get':
        d = api.get(documentId=did).execute()
        text = []
        for el in d.get('body', {}).get('content', []):
            for pe in el.get('paragraph', {}).get('elements', []):
                text.append(pe.get('textRun', {}).get('content', ''))
        out({'title': d.get('title'), 'text': ''.join(text)})
    elif cmd == 'batch':
        out(api.batchUpdate(documentId=did, body={'requests': json.loads(args[2])}).execute())
    else:
        raise SystemExit(__doc__)

if __name__ == '__main__':
    if len(sys.argv) < 4:
        raise SystemExit(__doc__)
    {'sheets': sheets, 'slides': slides, 'docs': docs}.get(sys.argv[1], lambda a: (_ for _ in ()).throw(SystemExit(__doc__)))(sys.argv[2:])
