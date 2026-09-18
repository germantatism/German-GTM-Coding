# -*- coding: utf-8 -*-
"""Re-create ~/.config/yuno-slides/token.json for the Slides API (the previous GCP project was deleted on/before 2026-09-18).
1) console.cloud.google.com -> new or existing project -> enable "Google Slides API"
2) APIs & Services -> Credentials -> Create OAuth client ID -> Desktop app -> download JSON
3) python3 Deals/Appmaking/build/auth_slides.py /path/to/client_secret_xxx.json   (opens the browser once)
"""
import sys, os
from google_auth_oauthlib.flow import InstalledAppFlow
SCOPES=['https://www.googleapis.com/auth/presentations']
TOKEN=os.path.expanduser('~/.config/yuno-slides/token.json')
if len(sys.argv)<2: raise SystemExit(__doc__)
flow=InstalledAppFlow.from_client_secrets_file(sys.argv[1],SCOPES)
creds=flow.run_local_server(port=0)
os.makedirs(os.path.dirname(TOKEN),exist_ok=True); open(TOKEN,'w').write(creds.to_json())
print('token written to',TOKEN)
