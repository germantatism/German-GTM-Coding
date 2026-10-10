import sys,warnings,json,time; warnings.filterwarnings('ignore'); sys.path.insert(0,'.')
import split_decks as D
from split_decks import *
s=D.svc(); pid=D.BANK
P=s.presentations().get(presentationId=pid).execute()
json.dump(P,open('backup_bankdeck_pre_kycdetail_'+time.strftime('%H%M%S')+'.json','w'))
sid='bnk_kyc_detail'
if sid in [x['objectId'] for x in P['slides']]:
    s.presentations().batchUpdate(presentationId=pid,body={'requests':[{'deleteObject':{'objectId':sid}}]}).execute()
    P=s.presentations().get(presentationId=pid).execute()
p=new_slide(s,pid,P,'bnk_money',sid,'BANKING CONNECTIVITY  ›  KYC AND KYB ORCHESTRATION','One KYC and KYB layer, best source per country, ready for any bank')
# the message: what we solve
steps=[('Best source per country','Each check goes to the strongest identity, document and registry source in that market.'),
       ('Onboarding that succeeds','The right source for every document and country, so fewer creators get stuck or declined.'),
       ('Separate from the banks','Packages built once and kept current. Add a bank tomorrow and every creator is ready.')]
p.card(36,84,648,62,fill=PANEL,line=None)
for i,(a,b) in enumerate(steps):
    x=48+i*214
    p.circle_num(x,93,str(i+1),d=18)
    p.text(x+26,93,170,14,a,size=9.5,color=INK,weight=600)
    p.text(x+26,109,178,32,b,size=8,color=BODY,ls=115)
    if i<2: p.line(x+200,102,x+210,102,BLUE,1,arrow=True)
# the package every bank receives
p.text(36,154,400,12,'THE PACKAGE EVERY BANK RECEIVES',size=7.5,color=BLUE,weight=600)
cols=[(36,'KYC','Individual creators',[('Identity','name, date of birth, email, address, residence'),('Tax IDs','SSN, ITIN, TIN, VAT and more'),
        ('ID document','passport, driver\'s license, national or state ID'),('Selfie and liveness','biometric check on a live capture'),
        ('Address and income','proof of address, bank statement, employment')]),
      (366,'KYB','Creators operating as companies',[('Company','legal name, country of incorporation, entity type'),('Tax IDs','EIN, VAT and more'),
        ('Beneficial owners','identity, ID, tax ID and ownership % of each'),('Business documents','incorporation, license, EIN letter, good standing'),
        ('Financials','balance sheet, P&L, cash flow, audit')])]
for x,tag,ttl,rows in cols:
    p.card(x,170,318,132)
    p.pill(x+12,179,38,tag,size=8,h=16)
    p.text(x+58,179,240,16,ttl,size=11,color=INK,weight=600)
    for i,(a,b) in enumerate(rows):
        yy=205+i*19
        p.line(x+12,yy-3,x+306,yy-3,LINE,0.75)
        p.text(x+12,yy,104,14,a,size=8.5,color=INK,weight=600)
        p.text(x+118,yy,190,14,b,size=8,color=BODY)
p.card(36,310,648,30,fill=PANEL,line=None)
p.text(48,318,92,14,'WITH EVERY ONBOARDING',size=7,color=BLUE,weight=600)
chips=[('PEP status',62),('Sanctions screening',96),('Risk level',58),('Source of funds and income',128),('Terms accepted, with time and IP',156)]
x=150
for t,w in chips:
    p.pill(x,317,w,t,fill=WHITE,color=INK,size=7,h=15,line=LINE); x+=w+6
p.text(36,348,648,20,'**Live status** with a webhook on every change.   **Previously onboarded** creators move over without verifying again.   **Masked** tax IDs and document numbers.',
       size=8,color=BODY,bold_color=INK)
run(s,pid,p.R,sid)
P=s.presentations().get(presentationId=pid).execute()
order=[x['objectId'] for x in P['slides'] if x['objectId']!=sid]
order.insert(order.index('bnk_kyc')+1,sid)
finish(s,pid,order)
