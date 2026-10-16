# v2: two tabs only (Proposal, Business case). 16 Oct 2026.
import warnings, os, json; warnings.filterwarnings('ignore')
from google.oauth2 import service_account
from googleapiclient.discovery import build
SID='1oIq55KHyjLA4R73_WtDLYLB5bG93rkh3WGcA6A3Mtmw'
creds=service_account.Credentials.from_service_account_file(os.path.expanduser('~/.config/gsuite/sa.json'),scopes=['https://www.googleapis.com/auth/spreadsheets'])
sh=build('sheets','v4',credentials=creds,cache_discovery=False).spreadsheets()
M=json.load(open(os.path.join(os.path.dirname(__file__),'..','model','model_numbers.json')))
meta=sh.get(spreadsheetId=SID).execute(); sheets=meta['sheets']
keep=sheets[0]['properties']['sheetId']
req=[{'deleteSheet':{'sheetId':s['properties']['sheetId']}} for s in sheets[1:]]
req+=[{'updateSheetProperties':{'properties':{'sheetId':keep,'title':'Proposal'},'fields':'title'}}]
sh.batchUpdate(spreadsheetId=SID,body={'requests':req}).execute()
meta=sh.get(spreadsheetId=SID).execute(); ids={s['properties']['title']:s['properties']['sheetId'] for s in meta['sheets']}
for t in ids: sh.values().clear(spreadsheetId=SID,range=f"'{t}'!A1:Z200").execute()
# ---------------- Proposal tab
P=[]
P.append(['THE PRICE','Rate','How it works','','',''])                                   # r1
P.append(['Platform fee, a month',7500,'Covers the first $500K of monthly sales and everything listed below','','',''])  # r2
P.append(['$500K to $2M of monthly sales',40,'Each band is charged only on the sales inside it','','',''])           # r3
P.append(['$2M to $5M',30,'','','',''])                                                  # r4
P.append(['$5M to $10M',20,'','','',''])                                                 # r5
P.append(['Above $10M',10,'Only approved sales are billed; declines cost nothing','','',''])  # r6
P.append(['','','','','',''])                                                               # r7
P.append(['WHAT CARRY1ST PAYS','Usage','Platform fee','Total a month','Total a year','Share of sales'])  # r8
vols=[500000,1000000,2000000,4500000,10000000]
for i,v in enumerate(vols):
    r=9+i
    use=f"=MAX(0,MIN({v},2000000)-500000)*$B$3/10000+MAX(0,MIN({v},5000000)-2000000)*$B$4/10000+MAX(0,MIN({v},10000000)-5000000)*$B$5/10000+MAX(0,{v}-10000000)*$B$6/10000"
    P.append([f'{"$"}{v/1e6:g}M of monthly sales'+(' (run rate)' if v==4500000 else ''),use,'=$B$2',f'=B{r}+C{r}',f'=D{r}*12',f'=D{r}/{v}*10000'])  # r9..13
P.append(['','','','','',''])                                                               # r14
P.append(['WHAT THE $7,500 COVERS','What Carry1st gets','How we value it','Value a month','',''])  # r15
items=[
 ['First $500K of monthly sales','No usage fee on the first $500K of approved sales, every month','What it would pay at the first band (40 bps)','=500000*$B$3/10000'],
 ['Dedicated Key Account Manager','Payments strategy, provider negotiation including EBANX, quarterly reviews','Senior payments consultant, 20 hours at $200',4000],
 ['Dedicated Technical Account Manager','Integration support, routing setup, incident escalation','Payments solutions engineer, 20 hours at $175',3500],
 ['Orchestration and rules engine','Rules by country, card, amount and method across every provider','Half a senior engineer ($130K a year), in house',5417],
 ['Smart routing and retries','Each payment to the best route; soft declines retried on another provider','A quarter of a senior engineer, in house',2708],
 ['Monitors and auto-failover','Detects approval drops and outages, shifts traffic, returns it on recovery','Monitoring tools plus on-call',1500],
 ['Provider integrations kept current','EBANX and every provider added later maintained by Yuno','2 providers at 0.15 of an engineer each',3250],
 ['Checkout and SDKs','Localized web and mobile checkout with local methods per market','Build spread over two years, plus upkeep',1500],
 ['Dashboard and insights','Approval, cost and provider performance in one view','Reporting tools and analyst time',1000],
 ['PCI token vault','Cards stored once and usable with any provider','Standalone vault service',1000]]
for it in items: P.append(it+['',''])                                                       # r16..25
P.append(['Total value covered','','','=SUM(D16:D25)','',''])                               # r26
P.append(['Platform fee Carry1st pays','','','=B2','',''])                                  # r27
P.append(['Value for every $1 of platform fee','','','=D26/D27','',''])                     # r28
P.append(['Value Carry1st gets on top of the fee, a year','','','=(D26-D27)*12','',''])    # r29
# ---------------- Business case tab
S=M['model']; T=M['ttm']
def ann(sc,k): return round(S[sc]['450000'][k]*12)
B=[['VALUE A YEAR AT $4.5M OF MONTHLY SALES','Conservative','Base','Optimistic','What it is'],
   ['Approval uplift',ann('Conservative','l2c'),ann('Base','l2c'),ann('Optimistic','l2c'),'Routing and retries recover sales a single provider declines'],
   ['Local methods',ann('Conservative','l3c'),ann('Base','l3c'),ann('Optimistic','l3c'),'Methods one provider does not carry: MODO, QR, Bre-B, Nequi, Bolivia cards'],
   ['Processing cost',ann('Conservative','l1'),ann('Base','l1'),ann('Optimistic','l1'),'Volume moves to the cheaper route; every rate has a real alternative'],
   ['Integrations avoided',ann('Conservative','l4'),ann('Base','l4'),ann('Optimistic','l4'),'Market-by-market EBANX work, later builds and upkeep Carry1st does not carry'],
   ['Total value a year','=SUM(B2:B5)','=SUM(C2:C5)','=SUM(D2:D5)',''],
   ['What Yuno costs a year',"='Proposal'!E12","='Proposal'!E12","='Proposal'!E12",'$21,000 a month at $4.5M of monthly sales'],
   ['Net value a year','=B6-B7','=C6-C7','=D6-D7','What Carry1st keeps after paying Yuno'],
   ['Value for every $1 paid to Yuno','=B6/B7','=C6/C7','=D6/D7',''],
   ['','','','',''],
   ['PLUS IN 2027 ONLY','Conservative','Base','Optimistic',''],
   ['Time to market',round(T['Conservative']['l5']),round(T['Base']['l5']),round(T['Optimistic']['l5']),'Run rate reached in Nov, Sep or Aug 2027 instead of Dec 2027'],
   ['Total value in 2027','=B6+B12','=C6+C12','=D6+D12',''],
   ['','','','',''],
   ['Assumptions','','','','$10 average and $5 median ticket and $4.5M a month are Carry1st estimates. 75% baseline approval, a 4.5% all-in EBANX rate and a 15% take rate are Yuno estimates, replaced by Carry1st data and EBANX’s quote.']]
sh.values().batchUpdate(spreadsheetId=SID,body={'valueInputOption':'USER_ENTERED','data':[{'range':"'Proposal'!A1",'values':P},{'range':"'Business case'!A1",'values':B}]}).execute()
# ---------------- format
NAVY={'red':16/255,'green':40/255,'blue':74/255}; WHITE={'red':1,'green':1,'blue':1}; LIGHT={'red':232/255,'green':234/255,'blue':245/255}
USD={'type':'CURRENCY','pattern':'"$"#,##0'}; X={'type':'NUMBER','pattern':'0.0"x"'}; BPS={'type':'NUMBER','pattern':'0" bps"'}; BPSR={'type':'NUMBER','pattern':'0" bps"'}
R=[]
def rg(t,r0,r1,c0,c1): return {'sheetId':ids[t],'startRowIndex':r0,'endRowIndex':r1,'startColumnIndex':c0,'endColumnIndex':c1}
def fmt(t,r0,r1,c0,c1,f,fields): R.append({'repeatCell':{'range':rg(t,r0,r1,c0,c1),'cell':{'userEnteredFormat':f},'fields':'userEnteredFormat('+fields+')'}})
def border(t,r0,r1,c0,c1): R.append({'updateBorders':{'range':rg(t,r0,r1,c0,c1),'top':{'style':'SOLID'},'bottom':{'style':'SOLID'},'left':{'style':'SOLID'},'right':{'style':'SOLID'},'innerHorizontal':{'style':'SOLID'},'innerVertical':{'style':'SOLID'}}})
HDR={'backgroundColor':NAVY,'textFormat':{'fontFamily':'Roboto','fontSize':10,'bold':True,'foregroundColor':WHITE},'verticalAlignment':'MIDDLE','wrapStrategy':'WRAP'}
for t,n,cols in (('Proposal',len(P),6),('Business case',len(B),5)):
    R.append({'updateSheetProperties':{'properties':{'sheetId':ids[t],'gridProperties':{'frozenRowCount':0,'frozenColumnCount':1,'hideGridlines':True}},'fields':'gridProperties(frozenRowCount,frozenColumnCount,hideGridlines)'}})
    fmt(t,0,n,0,cols,{'textFormat':{'fontFamily':'Roboto','fontSize':10},'wrapStrategy':'WRAP','verticalAlignment':'MIDDLE'},'textFormat,wrapStrategy,verticalAlignment')
    fmt(t,0,n,0,1,{'textFormat':{'fontFamily':'Roboto','fontSize':10,'bold':True}},'textFormat')
# Proposal blocks: (header row index, first, last, ncols)
for h,a,b,c in ((0,1,6,3),(7,8,13,6),(14,15,29,4)):
    fmt('Proposal',h,h+1,0,c,HDR,'backgroundColor,textFormat,verticalAlignment,wrapStrategy'); border('Proposal',h,b,0,c)
fmt('Proposal',1,2,1,2,{'numberFormat':USD},'numberFormat')
fmt('Proposal',2,6,1,2,{'numberFormat':BPS,'horizontalAlignment':'LEFT'},'numberFormat,horizontalAlignment')
fmt('Proposal',8,13,1,5,{'numberFormat':USD},'numberFormat'); fmt('Proposal',8,13,5,6,{'numberFormat':BPS},'numberFormat')
fmt('Proposal',11,12,0,6,{'backgroundColor':LIGHT},'backgroundColor')
fmt('Proposal',15,29,3,4,{'numberFormat':USD},'numberFormat'); fmt('Proposal',27,28,3,4,{'numberFormat':X},'numberFormat')
fmt('Proposal',25,29,0,4,{'backgroundColor':LIGHT,'textFormat':{'fontFamily':'Roboto','fontSize':10,'bold':True}},'backgroundColor,textFormat')
for t,h,b,c in (('Business case',0,9,5),('Business case',10,13,5)):
    fmt(t,h,h+1,0,c,HDR,'backgroundColor,textFormat,verticalAlignment,wrapStrategy'); border(t,h,b,0,c)
fmt('Business case',1,13,1,4,{'numberFormat':USD},'numberFormat'); fmt('Business case',8,9,1,4,{'numberFormat':X},'numberFormat')
for r in (5,7,12): fmt('Business case',r,r+1,0,5,{'backgroundColor':LIGHT,'textFormat':{'fontFamily':'Roboto','fontSize':10,'bold':True}},'backgroundColor,textFormat')
R.append({'mergeCells':{'range':rg('Business case',14,15,1,5),'mergeType':'MERGE_ALL'}})
fmt('Business case',14,15,1,5,{'textFormat':{'fontFamily':'Roboto','fontSize':9,'italic':True}},'textFormat')
for t,ws in (('Proposal',[300,300,320,130,130,120]),('Business case',[300,130,130,130,440])):
    for j,w in enumerate(ws): R.append({'updateDimensionProperties':{'range':{'sheetId':ids[t],'dimension':'COLUMNS','startIndex':j,'endIndex':j+1},'properties':{'pixelSize':w},'fields':'pixelSize'}})
sh.batchUpdate(spreadsheetId=SID,body={'requests':R}).execute()
o=sh.values().batchGet(spreadsheetId=SID,ranges=["'Proposal'!A1:F29","'Business case'!A1:E15"]).execute()
for vr in o['valueRanges']:
    for r in vr.get('values',[]): print(r)
    print('--')

# NOTE 16 Oct 2026: German asked for a single Proposal tab, no business-case data. The Business case tab was deleted; the block above that writes it is obsolete.
