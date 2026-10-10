import sys,warnings,json,time; warnings.filterwarnings('ignore'); sys.path.insert(0,'.')
import split_decks as D
from split_decks import *
s=D.svc(); pid=D.BANK
P=s.presentations().get(presentationId=pid).execute()
json.dump(P,open('backup_bankdeck_pre_kycside_'+time.strftime('%H%M%S')+'.json','w'))
sid='bnk_kyc_side'
if sid in [x['objectId'] for x in P['slides']]:
    s.presentations().batchUpdate(presentationId=pid,body={'requests':[{'deleteObject':{'objectId':sid}}]}).execute()
    P=s.presentations().get(presentationId=pid).execute()
p=new_slide(s,pid,P,'bnk_money',sid,'BANKING CONNECTIVITY  ›  KYC AND KYB ORCHESTRATION','Verify a creator once, open an account at any bank')
def box(x,y,w,h,t,fill=WHITE,line=LINE,color=INK,size=7.5):
    p.card(x,y,w,h,fill=fill,line=line)
    p.text(x,y,w,h,t,size=size,color=color,weight=600,align='CENTER',valign='MIDDLE',ls=100)
# TODAY
p.card(36,84,304,208)
p.text(48,92,280,12,'TODAY  ·  EVERY BANK VERIFIES ON ITS OWN',size=7.5,color=GREY,weight=600)
box(48,114,58,34,'Creator')
p.line(108,131,126,131,GREY,1,arrow=True)
for i,b in enumerate(['Bank A','Bank B','Bank C']):
    x=132+i*66
    box(x,114,58,34,b+'\nown KYC',fill=WHITE,line=RED,color=INK)
today=[('Each bank runs its own KYC.','Different documents and rules per bank.'),
       ('Creators repeat themselves.','Same ID, selfie and tax forms, every time.'),
       ('Onboarding stalls.','Creators drop off, ops chases documents.'),
       ('A new bank is a new project.','Re-onboard every creator first.')]
# WITH YUNO
p.card(380,84,304,208,fill=PANEL,line=BLUE)
p.text(392,92,280,12,'WITH YUNO  ·  ONE LAYER, EVERY BANK',size=7.5,color=BLUE,weight=600)
box(392,114,50,34,'Creator')
p.line(444,131,456,131,BLUE,1,arrow=True)
box(460,114,82,34,'Yuno\nKYC and KYB',fill=BLUE,line=None,color=WHITE)
p.line(544,131,556,131,BLUE,1,arrow=True)
for i,b in enumerate(['A','B','C','+ New']):
    x=560+i*29
    box(x,114,26,34,b,fill=WHITE,line=BLUE if b=='+ New' else LINE,color=BLUE if b=='+ New' else INK,size=6.5 if b=='+ New' else 7.5)
yuno=[('Verify once, reuse everywhere.','Start from the checks you already run. Each bank gets its package.'),
      ('Best source per country.','Only the gaps a bank needs, from the strongest local source.'),
      ('One status for every creator.','Approved, pending or rejected, with a webhook on every change.'),
      ('A new bank is configuration.','Creators already verified move over without verifying again.')]
for x0,rows,col in [(48,today,RED),(392,yuno,GREEN)]:
    for i,(a,b) in enumerate(rows):
        yy=160+i*32
        p.line(x0,yy-4,x0+280,yy-4,LINE,0.75)
        p.shape(x0,yy+4,5,5,'ELLIPSE',col,None)
        p.text(x0+12,yy,268,28,f'**{a}**  {b}',size=8.5,color=BODY,bold_color=INK,ls=115)
p.line(345,188,375,188,BLUE,1.5,arrow=True)
# THE PACKAGE
p.card(36,302,648,68,fill=PANEL,line=None)
p.text(48,310,400,12,'THE PACKAGE COVERS EVERYTHING A BANK ASKS FOR',size=7.5,color=BLUE,weight=600)
pk=[('Individuals','identity, tax ID, ID document, selfie and liveness'),('Companies','registration, EIN, business documents, financials'),
    ('Beneficial owners','identity, ID and ownership % of each'),('Screening','PEP, sanctions, risk level, source of funds')]
for i,(a,b) in enumerate(pk):
    x=48+i*158
    p.text(x,326,148,14,a,size=9,color=INK,weight=600)
    p.text(x,340,148,26,b,size=8,color=BODY,ls=115)
run(s,pid,p.R,sid)
P=s.presentations().get(presentationId=pid).execute()
order=[x['objectId'] for x in P['slides'] if x['objectId']!=sid]
order.insert(order.index('bnk_kyc_detail')+1,sid)
finish(s,pid,order)
