import json, sys, os
from google.oauth2 import service_account
from googleapiclient.discovery import build
PID = sys.argv[1]
creds = service_account.Credentials.from_service_account_file(os.path.expanduser('~/.config/gsuite/sa.json'), scopes=['https://www.googleapis.com/auth/presentations.readonly'])
svc = build('slides', 'v1', credentials=creds, cache_discovery=False)
p = svc.presentations().get(presentationId=PID).execute()
def txt(el):
    out=[]
    sh=el.get('shape')
    if sh and sh.get('text'):
        s=''.join(te.get('textRun',{}).get('content','') for te in sh['text'].get('textElements',[]))
        if s.strip(): out.append(s.strip())
    tb=el.get('table')
    if tb:
        for r in tb.get('tableRows',[]):
            cells=[]
            for c in r.get('tableCells',[]):
                s=''.join(te.get('textRun',{}).get('content','') for te in c.get('text',{}).get('textElements',[]))
                cells.append(s.strip().replace('\n',' / '))
            out.append(' | '.join(cells))
    if el.get('elementGroup'):
        for ch in el['elementGroup'].get('children',[]): out+=txt(ch)
    return out
lines=[]
for i,s in enumerate(p['slides'],1):
    lines.append(f'\n##### SLIDE {i}  id={s["objectId"]}')
    n_img=sum(1 for e in s.get('pageElements',[]) if e.get('image'))
    lines.append(f'[images: {n_img}]')
    for e in s.get('pageElements',[]):
        for t in txt(e): lines.append('  '+t)
    notes=s.get('slideProperties',{}).get('notesPage',{})
    for e in notes.get('pageElements',[]):
        sh=e.get('shape')
        if sh and sh.get('text'):
            s_=''.join(te.get('textRun',{}).get('content','') for te in sh['text'].get('textElements',[]))
            if s_.strip(): lines.append('  NOTES: '+s_.strip().replace('\n',' // '))
open(sys.argv[2],'w').write('\n'.join(lines))
print(len(p['slides']),'slides dumped')
