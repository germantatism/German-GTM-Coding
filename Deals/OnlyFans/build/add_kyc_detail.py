import sys,warnings,json,time; warnings.filterwarnings('ignore'); sys.path.insert(0,'.')
import split_decks as D
from split_decks import *
s=D.svc(); pid=D.BANK
P=s.presentations().get(presentationId=pid).execute()
json.dump(P,open('backup_bankdeck_pre_kycdetail_'+time.strftime('%H%M%S')+'.json','w'))
sid='bnk_kyc_detail'
if sid not in [x['objectId'] for x in P['slides']]:
    p=new_slide(s,pid,P,'bnk_money',sid,'BANKING CONNECTIVITY  ›  WHAT KYC AND KYB COVER','KYC for creators and KYB for their companies, everything a bank asks for')
    cols=[(36,'KYC','Individual creators',[('Identity','name, date of birth, email, address, residence'),('Tax IDs','SSN, ITIN, TIN, VAT and more'),
            ('ID document','passport, driver\'s license, national or state ID'),('Selfie and liveness','biometric check on a live capture'),
            ('Address and income','proof of address, bank statement, employment')]),
          (366,'KYB','Creators operating as companies',[('Company','legal name, country of incorporation, entity type'),('Tax IDs','EIN, VAT and more'),
            ('Beneficial owners','identity, ID, tax ID and ownership % of each'),('Business documents','incorporation, license, EIN letter, good standing'),
            ('Financials','balance sheet, P&L, cash flow, audit')])]
    for x,tag,ttl,rows in cols:
        p.card(x,84,318,178)
        p.pill(x+12,95,38,tag,size=8,h=16)
        p.text(x+58,95,240,16,ttl,size=11.5,color=INK,weight=600)
        for i,(a,b) in enumerate(rows):
            yy=124+i*26
            p.line(x+12,yy-5,x+306,yy-5,LINE,0.75)
            p.text(x+12,yy,104,14,a,size=9,color=INK,weight=600)
            p.text(x+118,yy,190,14,b,size=8.5,color=BODY)
    p.card(36,272,648,44,fill=PANEL,line=None)
    p.text(48,280,160,12,'SENT WITH EVERY ONBOARDING',size=7.5,color=BLUE,weight=600)
    chips=[('PEP status',70),('Sanctions screening',104),('Risk level',66),('Source of funds and income',140),('Terms accepted, with time and IP',170)]
    x=48
    for t,w in chips:
        p.pill(x,295,w,t,fill=WHITE,color=INK,size=7.5,h=15,line=LINE); x+=w+8
    pts=[('Live status','pending, under review, succeeded. A webhook on every change.'),
         ('Previously onboarded','creators already verified at a bank move over without verifying again.'),
         ('Masked by default','tax IDs and document numbers come back showing the last four only.')]
    for i,(a,b) in enumerate(pts):
        x=36+i*220
        p.card(x,326,208,44)
        p.text(x+10,332,190,34,f'**{a}**  {b}',size=8.5,color=BODY,bold_color=INK,ls=115)
    run(s,pid,p.R,sid)
P=s.presentations().get(presentationId=pid).execute()
order=[x['objectId'] for x in P['slides'] if x['objectId']!=sid]
order.insert(order.index('bnk_kyc')+1,sid)
finish(s,pid,order)
