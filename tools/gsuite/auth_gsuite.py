# -*- coding: utf-8 -*-
"""One-time OAuth for the Google Workspace suite (Sheets, Slides, Docs, plus files Claude creates in Drive).

Prereqs (done once by German in the browser, see the step-by-step in the chat / memory):
  1) GCP project with Google Sheets API, Google Slides API, Google Docs API and Google Drive API enabled
  2) OAuth consent screen: External, test user = german.tatis@y.uno, app PUBLISHED (avoids 7-day token expiry)
  3) OAuth client ID of type "Desktop app", JSON downloaded

Run:
  python3 tools/gsuite/auth_gsuite.py /path/to/client_secret_xxx.json
It opens the browser once, then writes:
  ~/.config/gsuite/token.json          (used by Claude's Sheets/Docs/Slides scripts)
  ~/.config/yuno-slides/token.json     (same token, so the existing Slides engine.py keeps working)
  ~/.config/gsuite/client_secret.json  (copy of the client, needed for future refreshes)

Scopes are deliberately "sensitive" only (no restricted Drive scopes), so an unverified app can still be
published and the refresh token does not expire every 7 days.
"""
import os, shutil, sys
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/presentations',
    'https://www.googleapis.com/auth/documents',
    'https://www.googleapis.com/auth/drive.file',
]
GSUITE_DIR = os.path.expanduser('~/.config/gsuite')
TOKEN = os.path.join(GSUITE_DIR, 'token.json')
SLIDES_TOKEN = os.path.expanduser('~/.config/yuno-slides/token.json')

if len(sys.argv) < 2:
    raise SystemExit(__doc__)
client_secret = sys.argv[1]
flow = InstalledAppFlow.from_client_secrets_file(client_secret, SCOPES)
creds = flow.run_local_server(port=0, prompt='consent', access_type='offline')

os.makedirs(GSUITE_DIR, exist_ok=True)
os.makedirs(os.path.dirname(SLIDES_TOKEN), exist_ok=True)
for path in (TOKEN, SLIDES_TOKEN):
    with open(path, 'w') as fh:
        fh.write(creds.to_json())
    os.chmod(path, 0o600)
dst = os.path.join(GSUITE_DIR, 'client_secret.json')
if os.path.abspath(client_secret) != os.path.abspath(dst):
    shutil.copyfile(client_secret, dst)
    os.chmod(dst, 0o600)
print('token written to', TOKEN, 'and', SLIDES_TOKEN)
print('refresh_token present:', bool(creds.refresh_token))
