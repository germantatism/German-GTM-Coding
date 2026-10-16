# One-off: "EBANX direct vs through Yuno" proposed-model slide (Suno layout), inserted after the comparison grid.
import warnings; warnings.filterwarnings('ignore')
import gs_engine as E, os, re, sys
from google.oauth2 import service_account
from googleapiclient.discovery import build
LOGO='1N2MEukNJk0ixglVluHB8keewCBVxb3gp'
creds=service_account.Credentials.from_service_account_file(os.path.expanduser('~/.config/gsuite/sa.json'),scopes=['https://www.googleapis.com/auth/drive'])
try: build('drive','v3',credentials=creds,cache_discovery=False).permissions().create(fileId=LOGO,body={'type':'anyone','role':'reader'}).execute()
except Exception as e: print('perm', str(e)[:80])
url=f'https://drive.google.com/uc?export=download&id={LOGO}'
deck=E.Deck('1-IdPVaPu5FE4P36ByuiQ2vupRFocujdFcmmQeuPI9kk')
s={'id':'model2','kicker':'TWO WAYS TO LAUNCH · THE PROPOSED MODEL','headline':'Go direct with EBANX, or put Yuno around it: same launch date, far more room to grow.'}
sid,sb=E._content_base(deck,s,'mdl2x')
G='#C9CEEA'
lw=72; lh=lw*121/480; sb.image(url,360-lw/2,93,lw,lh)
y0=93+lh+5
sb.rect(359.8,y0,0.6,6,fill=G); sb.rect(186,y0+6,348,0.6,fill=G)
sb.rect(186,y0+6,0.6,8,fill=G); sb.rect(533.4,y0+6,0.6,8,fill=G)
py=y0+14; ph=24
sb.rect(36,py,300,ph,fill=E.PANEL3); sb.text(36,py,300,ph,'EBANX direct',size=12,bold=True,color=E.INK,align='CENTER',valign='MIDDLE',ls=100)
sb.rect(384,py,300,ph,fill=E.BLUE); sb.text(384,py,300,ph,'Through Yuno',size=12,bold=True,color=E.WHITE,align='CENTER',valign='MIDDLE',ls=100)
cy=py+ph
sb.rect(185.7,cy,0.6,14,fill=G); sb.text(36,cy+15,300,11,'One integration, one provider, one price',size=8.5,bold=True,color=E.BLUE,align='CENTER',ls=100); sb.rect(185.7,cy+28,0.6,22,fill=G)
sb.rect(533.7,cy,0.6,8,fill=G); sb.text(384,cy+9,300,11,'One integration, every rail below it',size=8.5,bold=True,color=E.BLUE,align='CENTER',ls=100)
chips=['EBANX','Other MoRs','Local acquirers','Local methods']; cw=69; gap=(300-4*cw)/3; chy=cy+36
sb.rect(533.7,cy+21,0.6,6,fill=G); sb.rect(384+cw/2,cy+27,300-cw,0.6,fill=G)
for k,c in enumerate(chips):
    x=384+k*(cw+gap); sb.rect(x+cw/2-0.3,cy+27,0.6,chy-(cy+27),fill=G)
    sb.round_rect(x,chy,cw,18,fill=E.WHITE,outline=G,outline_w=0.75)
    sb.text(x,chy,cw,18,c,size=8,bold=True,color=(E.DEEP if c=='EBANX' else E.INK),align='CENTER',valign='MIDDLE',ls=100)
by=chy+28; bh=330-by
L=['One merchant of record for all five markets, once EBANX enables each','One approval rate: a decline on EBANX is a lost sale','One price, with no alternative route to negotiate against','Bolivia cash only; no MODO or interoperable QR in Argentina','Every later provider or local acquirer is a new build']
R=['Smart routing by BIN, brand, country and amount lifts approval','A decline on EBANX retries on another provider; Monitors fail over','Volume moves by rule, so every rate has a real alternative','Pix, PSE, Bre-B, SPEI, OXXO, MODO and QR, market by market','Local acquiring later without touching checkout; one dashboard']
for x,items in ((36,L),(384,R)):
    sb.rect(x,by,300,bh,fill=E.WHITE,outline='#E3E6F3',outline_w=0.75)
    pitch=(bh-16)/len(items); yy=by+9
    for it in items:
        sb.text(x+14,yy,8,11,'•',size=8.5,color=E.BLUE,ls=100); sb.text(x+26,yy,262,11,it,size=8.5,color=E.INK,ls=100); yy+=pitch
sb.rect(36,338,648,0.6,fill=E.BLUE)
sb.text(36,343,648,24,[('EBANX stays at the center. Yuno adds what going direct cannot: ',10,False,E.INK),('routing, retries, leverage and every rail Carry1st adds next.',10,True,E.BLUE)],align='CENTER',ls=110)
sb.flush('model slide')
deck.set_notes(sid,'Both options launch on EBANX and on the same Black Friday date. Going direct gives one provider, one approval rate and one price. Through Yuno, EBANX stays at the center and the Shop gains smart routing to lift approval, retries on another provider when EBANX declines, a real alternative to negotiate every rate against, and the local methods each market needs, without rebuilding checkout as Carry1st grows.')
pos=int(sys.argv[1]) if len(sys.argv)>1 else 10
deck.svc.presentations().batchUpdate(presentationId=deck.pid, body={'requests':[{'updateSlidesPosition':{'slideObjectIds':[sid],'insertionIndex':pos}}]}).execute()
P=deck.fetch(); reqs=[]
for i,sl in enumerate(P['slides'],1):
    for el,tr in E.elements(sl):
        t=E.text_of(el).strip()
        if re.fullmatch(r'\d{1,2}',t) and E.geom(el,tr)[1]>=370 and t!=str(i):
            reqs+=[{'deleteText':{'objectId':el['objectId'],'textRange':{'type':'ALL'}}},{'insertText':{'objectId':el['objectId'],'insertionIndex':0,'text':str(i)}}]
# new slide has no page number yet
sb2=E.SB(deck,sid,'mdl2pg'); sb2.text(640,383,44,9,str(pos+1),size=6.5,color=E.GREY,align='END',ls=100); sb2.flush('pg')
if reqs: deck.svc.presentations().batchUpdate(presentationId=deck.pid, body={'requests':reqs}).execute()
print('inserted at', pos+1, 'renumbered', len(reqs)//2)
