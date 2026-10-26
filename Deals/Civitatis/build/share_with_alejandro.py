# -*- coding: utf-8 -*-
"""Share German's Civitatis deck copy with Alejandro (writer) and send the Drive notification with a message.
  python3 share_with_alejandro.py <presentationId> [send]"""
import sys, os, warnings, json
warnings.filterwarnings('ignore')
from google.oauth2 import service_account
from googleapiclient.discovery import build
PID = sys.argv[1]; SEND = len(sys.argv) > 2 and sys.argv[2] == 'send'
c = service_account.Credentials.from_service_account_file(os.path.expanduser('~/.config/gsuite/sa.json'), scopes=['https://www.googleapis.com/auth/drive'])
d = build('drive', 'v3', credentials=c, cache_discovery=False)
MSG = ("Alejandro, te comparto la copia de la propuesta de Civitatis con el business case completo en los slides 13 y 14, "
       "sobre la data de tu calculador y con el método de cinco palancas de Cruz Verde. Supuestos en cada slide y fuentes en las notas del orador. "
       "Quedan dos puntos para cerrar con Civitatis: el ticket (USD 200 declarado vs USD 157.89 implícito) y qué métodos locales ya tienen vivos. "
       "German")
meta = d.files().get(fileId=PID, fields='id,name,owners(emailAddress),permissions(emailAddress,role)').execute()
print(json.dumps(meta, ensure_ascii=False))
if not SEND: print('dry: not shared'); sys.exit(0)
r = d.permissions().create(fileId=PID, body={'type': 'user', 'role': 'writer', 'emailAddress': 'alejandro@y.uno'},
                           sendNotificationEmail=True, emailMessage=MSG, fields='id,emailAddress,role').execute()
print('shared:', r)
