import sys,warnings,json,time; warnings.filterwarnings('ignore'); sys.path.insert(0,'.')
import split_decks as D
from split_decks import *
s=D.svc(); pid=D.BANK
P=s.presentations().get(presentationId=pid).execute()
json.dump(P,open('backup_bankdeck_pre_kyc_'+time.strftime('%H%M%S')+'.json','w'))
ids=[x['objectId'] for x in P['slides']]
sid='bnk_kyc'
if sid not in ids:
    p=new_slide(s,pid,P,'bnk_money',sid,'BANKING CONNECTIVITY  ›  KYC AND KYB','Yuno verifies a creator once and onboards them at every bank')
    # creator
    p.card(36,120,124,96)
    p.text(48,130,104,16,'Creator',size=11,color=INK,weight=600)
    p.text(48,150,104,60,'Submits once: ID, selfies, tax ID and business documents',size=8.5,color=BODY,ls=120)
    p.line(160,168,180,168,'#C9CDD6',1,arrow=True)
    # yuno layer
    p.card(182,86,176,186,fill=BLUE,line=None)
    p.text(194,96,160,16,'Yuno KYC and KYB',size=12,color=WHITE,weight=600)
    for i,t in enumerate(('One submission per creator','Sent to every provider and bank in the format each one needs','One status model across all of them','Documents kept in the vault')):
        yy=124+i*35
        p.shape(194,yy+3,6,6,'ELLIPSE','#B7BEF2',None)
        p.text(206,yy,144,32,t,size=8.5,color='#E8EAF5',ls=118)
    # destinations
    dest=[('KYC provider','identity, selfies, sanctions'),('Bank A','onboarding on its connection'),('Bank B','onboarding on its connection')]
    for i,(a,b) in enumerate(dest):
        yy=86+i*66
        p.line(358,179,376,yy+27,'#C9CDD6',1,arrow=True)
        p.card(378,yy,150,54)
        p.text(390,yy+9,130,16,a,size=10.5,color=INK,weight=600)
        p.text(390,yy+28,134,14,b,size=8.5,color=GREY)
    # status
    p.card(544,86,140,186,fill=PANEL,line=None)
    p.text(556,96,120,12,'ONE STATUS MODEL',size=7.5,color=BLUE,weight=600)
    for i,(t,c,bg) in enumerate((('APPROVED',GREEN,'#E2F3EB'),('PENDING','#9A5B00','#FBEFD9'),('REJECTED',RED,'#FBE4E1'))):
        p.pill(556,118+i*24,90,t,fill=bg,color=c,size=7.5,h=16)
    p.text(556,196,120,66,"Each with the provider's own reason, so your team knows exactly what is missing.",size=8.5,color=BODY,ls=120)
    # three points
    pts=[('Individuals and businesses','KYC for individual creators, KYB for creators who operate through a company.'),
         ('Portable','The verification belongs to OnlyFans, not to one bank. Adding or swapping a bank does not mean verifying again.'),
         ('Enforced at payout','Block, unblock or re-verify a creator, and it applies when money moves, not only in a report.')]
    for i,(a,b) in enumerate(pts):
        x=36+i*220
        p.card(x,288,208,82)
        p.text(x+12,298,184,16,a,size=10.5,color=INK,weight=600)
        p.text(x+12,318,186,48,b,size=8.5,color=BODY,ls=120)
    run(s,pid,p.R,sid)
R=[rep('of_exec_understanding_v2','One API to your banks, issuers and rails, an aggregation layer that shows each creator one balance and one history, and rules OnlyFans controls. The banks hold the money.',
       'One API to your banks, issuers and rails, KYC and KYB done once for every bank, an aggregation layer that shows each creator one balance and one history, and rules OnlyFans controls. The banks hold the money.')]
run(s,pid,R,'exec')
P=s.presentations().get(presentationId=pid).execute()
order=[x['objectId'] for x in P['slides'] if x['objectId']!=sid]
order.insert(order.index('bnk_opening'),sid)
finish(s,pid,order)
