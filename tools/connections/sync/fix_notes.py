import os, sys
from google.oauth2 import service_account
from googleapiclient.discovery import build
PID='1Qu3JvldczchxT9TrXmUkU1bSso9ltTGvOt5peT3hHjQ'
creds = service_account.Credentials.from_service_account_file(os.path.expanduser('~/.config/gsuite/sa.json'), scopes=['https://www.googleapis.com/auth/presentations'])
svc = build('slides','v1',credentials=creds,cache_discovery=False)
p = svc.presentations().get(presentationId=PID).execute()
FIX = {
 'h2d2d16976c09ce2e_6_1304': [(' Same table as the OnlyFans vault deck; only the owner of the token requestor ID changed.', '')],
 'h2d2d16976c09ce2e_6_1198': [('The second PSP: told to German by Waymo, October 2026.', 'The second PSP: shared by Waymo with Yuno, October 2026.')],
}
reqs=[]
for s in p['slides']:
    if s['objectId'] not in FIX: continue
    notes = s['slideProperties']['notesPage']
    for e in notes.get('pageElements',[]):
        sh=e.get('shape')
        if not sh or not sh.get('text'): continue
        txt=''.join(te.get('textRun',{}).get('content','') for te in sh['text'].get('textElements',[]))
        new=txt
        for a,b in FIX[s['objectId']]:
            if a in new: new=new.replace(a,b)
        if new!=txt:
            reqs.append({'deleteText':{'objectId':e['objectId'],'textRange':{'type':'ALL'}}})
            reqs.append({'insertText':{'objectId':e['objectId'],'insertionIndex':0,'text':new.rstrip('\n')}})
            print('fixing', s['objectId'], '->', new[-140:])
if reqs:
    svc.presentations().batchUpdate(presentationId=PID, body={'requests':reqs}).execute()
    print('done', len(reqs)//2, 'notes updated')
else:
    print('nothing to fix')
