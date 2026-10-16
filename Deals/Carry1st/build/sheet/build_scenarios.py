# Cordel scenario model, added to the proposal sheet (16 Oct 2026). Tabs: Summary, Inputs, Yuno fee by month,
# Provider alternatives, Approval sensitivity, What the platform fee covers (existing), Notes.
import warnings, os; warnings.filterwarnings('ignore')
from google.oauth2 import service_account
from googleapiclient.discovery import build
SID='1oIq55KHyjLA4R73_WtDLYLB5bG93rkh3WGcA6A3Mtmw'
creds=service_account.Credentials.from_service_account_file(os.path.expanduser('~/.config/gsuite/sa.json'),scopes=['https://www.googleapis.com/auth/spreadsheets'])
sh=build('sheets','v4',credentials=creds,cache_discovery=False).spreadsheets()
TABS=['Summary','Inputs','Yuno fee by month','Provider alternatives','Approval sensitivity','What the platform fee covers','Notes']
meta=sh.get(spreadsheetId=SID).execute(); cur={s['properties']['title']:s['properties']['sheetId'] for s in meta['sheets']}
req=[]
if 'Proposal' in cur: req.append({'updateSheetProperties':{'properties':{'sheetId':cur['Proposal'],'title':'What the platform fee covers'},'fields':'title'}})
for i,t in enumerate(TABS):
    if t not in cur and t!='What the platform fee covers': req.append({'addSheet':{'properties':{'title':t}}})
if req: sh.batchUpdate(spreadsheetId=SID,body={'requests':req}).execute()
meta=sh.get(spreadsheetId=SID).execute(); ids={s['properties']['title']:s['properties']['sheetId'] for s in meta['sheets']}
order=[{'updateSheetProperties':{'properties':{'sheetId':ids[t],'index':i},'fields':'index'}} for i,t in enumerate(TABS)]
sh.batchUpdate(spreadsheetId=SID,body={'requests':order}).execute()
for t in TABS:
    if t!='What the platform fee covers': sh.values().clear(spreadsheetId=SID,range=f"'{t}'!A1:Z300").execute()
SC=['Conservative','Base','Growth']; COL={'Conservative':'B','Base':'C','Growth':'D'}
I="'Inputs'!"
# ---------------- Inputs
IN=[['INPUT','Conservative','Base','Growth','Notes'],                                   #1
 ['Monthly sales at run rate (USD)',2500000,4500000,6000000,'Carry1st estimate $4 to 5M a month; edit freely'],  #2
 ['Monthly sales in the go-live month (USD)',500000,500000,500000,'First month live'],      #3
 ['Months to reach the run rate',12,10,8,'Linear ramp from go-live'],                   #4
 ['Go-live month','Dec 2026','','','Month 1 of year 1'],                                #5
 ['Average ticket (USD)',10,'','','Carry1st estimate'],                                 #6
 ['Median ticket (USD)',5,'','','Carry1st estimate'],                                   #7
 ['','','','',''],                                                                      #8
 ['SALES BY COUNTRY','Share','','','Assumed split, not agreed on the call; edit'],     #9
 ['Brazil',0.40,'','',''],['Mexico',0.25,'','',''],['Colombia',0.15,'','',''],['Argentina',0.15,'','',''],['Bolivia',0.05,'','',''],  #10-14
 ['Total','=SUM(B10:B14)','','','Must be 100%'],                                       #15
 ['','','','',''],                                                                      #16
 ['SALES BY PAYMENT METHOD','Share','','','Assumed split; edit'],                     #17
 ['Cards',0.45,'','',''],['Local methods (Pix, PSE, SPEI, OXXO, wallets)',0.55,'','',''],  #18-19
 ['','','','',''],                                                                      #20
 ['YUNO PRICING','Value','','','Proposal, Oct 2026'],                                  #21
 ['Platform fee a month (USD)',7500,'','','Covers the first $500K of monthly sales'],  #22
 ['Monthly sales covered by the platform fee (USD)',500000,'','','$7,500 on $500K = 150 bps'],  #23
 ['Band 1: $500K to $2M (bps)',40,'','','Bands applied marginally: each band only on the sales inside it'],  #24
 ['Band 2: $2M to $5M (bps)',30,'','',''],['Band 3: $5M to $10M (bps)',20,'','',''],['Band 4: above $10M (bps)',10,'','',''],  #25-27
 ['','','','',''],                                                                      #28
 ['APPROVAL','Value','','',''],                                                         #29
 ['Approval rate today, single provider',0.75,'','','Assumed; replace with Carry1st data'],  #30
 ['Carry1st margin on sales (take rate)',0.15,'','','Assumed; replace with Carry1st data']]   #31
# ---------------- Yuno fee by month (3 stacked blocks)
def band_usage(c):
    return (f"MAX(0,MIN({c},2000000)-{I}$B$23)*{I}$B$24/10000+MAX(0,MIN({c},5000000)-2000000)*{I}$B$25/10000"
            f"+MAX(0,MIN({c},10000000)-5000000)*{I}$B$26/10000+MAX(0,{c}-10000000)*{I}$B$27/10000")
Y=[]; ytot={}
for s in SC:
    c=COL[s]; start=len(Y)+1
    Y.append([f'{s.upper()} SCENARIO','Monthly sales','Covered by platform fee','Sales billed by band','Usage fee','Platform fee','Paid to Yuno','Effective bps'])
    for k in range(1,13):
        r=len(Y)+1
        sales=f"=IF({I}{c}$4<=1,{I}{c}$2,MIN({I}{c}$2,{I}{c}$3+({I}{c}$2-{I}{c}$3)*({k}-1)/({I}{c}$4-1)))"
        Y.append([f'Month {k}',sales,f'=MIN(B{r},{I}$B$23)',f'=B{r}-C{r}',f'={band_usage("B"+str(r))}',f'={I}$B$22',f'=E{r}+F{r}',f'=G{r}/B{r}*10000'])
    r=len(Y)+1; a=start+1; b=start+12
    Y.append(['Year 1 total',f'=SUM(B{a}:B{b})',f'=SUM(C{a}:C{b})',f'=SUM(D{a}:D{b})',f'=SUM(E{a}:E{b})',f'=SUM(F{a}:F{b})',f'=SUM(G{a}:G{b})',f'=G{r}/B{r}*10000'])
    ytot[s]=r; Y.append(['','','','','','','',''])
# ---------------- Provider alternatives
P=[['PROVIDER RATES (PENDING QUOTES)','EBANX','Provider B','Provider C','Notes'],   #1
 ['Card processing, % of card sales',0.035,0.032,0.030,'Pending quote; illustrative'],   #2
 ['Local methods, % of local-method sales',0.025,0.023,0.022,'Pending quote; illustrative'],  #3
 ['FX and settlement, % of sales',0.010,0.009,0.009,'Pending quote; illustrative'],   #4
 ['Taxes and MoR fee, % of sales',0.005,0.005,0.005,'Pending quote; illustrative'],    #5
 ['All-in rate, weighted by payment method',f"={I}$B$18*B2+{I}$B$19*B3+B4+B5",f"={I}$B$18*C2+{I}$B$19*C3+C4+C5",f"={I}$B$18*D2+{I}$B$19*D3+D4+D5",'Uses the method split in Inputs'],  #6
 ['','','','',''],                                                                      #7
 ['CONFIGURATIONS','Share EBANX','Share Provider B','Share Provider C','Blended provider rate','Uses Yuno'],  #8
 ['1. EBANX direct',1,0,0,'=B9*$B$6+C9*$C$6+D9*$D$6','No'],
 ['2. EBANX through Yuno',1,0,0,'=B10*$B$6+C10*$C$6+D10*$D$6','Yes'],
 ['3. EBANX + a second provider through Yuno',0.7,0.3,0,'=B11*$B$6+C11*$C$6+D11*$D$6','Yes'],
 ['4. Three providers through Yuno',0.5,0.3,0.2,'=B12*$B$6+C12*$C$6+D12*$D$6','Yes']]   #12
PA="'Provider alternatives'!"
# ---------------- Summary
YF="'Yuno fee by month'!"
S=[['YEAR 1 TOTAL COST BY CONFIGURATION','Year 1 sales','Provider costs','Paid to Yuno','Total cost','Effective bps','vs EBANX direct (USD)','vs EBANX direct (bps)']]
for s in SC:
    S.append([f'{s.upper()} SCENARIO','','','','','','',''])
    base_row=len(S)+1
    for j,cfg in enumerate(['1. EBANX direct','2. EBANX through Yuno','3. EBANX + a second provider through Yuno','4. Three providers through Yuno']):
        r=len(S)+1; pr=9+j
        yuno=f'=IF({PA}$F${pr}="Yes",{YF}$G${ytot[s]},0)'
        S.append([cfg,f'={YF}$B${ytot[s]}',f'=B{r}*{PA}$E${pr}',yuno,f'=C{r}+D{r}',f'=E{r}/B{r}*10000',f'=E{r}-$E${base_row}',f'=F{r}-$F${base_row}'])
    S.append(['','','','','','','',''])
S.append(['How to read it','Provider rates are placeholders until the quotes arrive; Yuno fees are the proposal. Approval gains are shown separately in Approval sensitivity and are not included here.','','','','','',''])
# ---------------- Approval sensitivity
A=[['EXTRA APPROVED SALES IN YEAR 1','Conservative','Base','Growth','Notes'],
 ['Year 1 sales today (USD)']+[f'={YF}$B${ytot[s]}' for s in SC]+[''],
 ['Sales attempted (USD)']+[f'={c}2/{I}$B$30' for c in 'BCD']+['Year 1 sales divided by today’s approval rate']]
for pts,note in ((1,''),(2,''),(3,''),(5,''),(8,'Garena: 8% approval improvement, shared on the call as a reference, not a promise for Carry1st')):
    r=len(A)+1
    A.append([f'Approval +{pts} pts: extra sales (USD)']+[f'={c}$3*{pts}/100' for c in 'BCD']+[note])
    A.append([f'Approval +{pts} pts: extra margin (USD)']+[f'={c}{r}*{I}$B$31' for c in 'BCD']+['Extra sales x Carry1st margin'])
A.append(['Paid to Yuno in year 1 (USD)']+[f'={YF}$G${ytot[s]}' for s in SC]+['From Yuno fee by month'])
A.append(['Approval gain that pays for Yuno (pts)']+[f'={c}{len(A)}/({c}$3*{I}$B$31)*100' for c in 'BCD']+['Points of approval at which the extra margin equals the Yuno fee'])
A.append(['How to read it','Approval gains are kept apart from cost: they depend on Carry1st’s decline mix and are confirmed once live traffic runs.','','',''])
# ---------------- Notes
N=[['TOPIC','STATUS','DETAIL'],
 ['Bands applied marginally','To confirm with Justo','Modeled marginally: each band only on the sales inside it. If bands applied to all volume, the totals change.'],
 ['Platform fee and what it covers','To confirm with Justo','$7,500 a month covering the first $500K of monthly sales; that equals 150 bps at $500K, falling as sales grow.'],
 ['Provider rates','Pending quotes','EBANX and second and third provider rates are placeholders; replace in Provider alternatives when quotes arrive.'],
 ['Sales by country and method','Assumed','Not agreed on the call; edit in Inputs.'],
 ['Go-live and ramp','Assumed','Go-live Dec 2026 and linear ramp; edit in Inputs.'],
 ['Garena approval reference','Reference only','8% approval improvement shared on the call; not a result promised for Carry1st.'],
 ['Blue cells','How to use','Blue numbers are inputs. Every other number is a formula.']]
data=[{'range':f"'{t}'!A1",'values':v} for t,v in (('Inputs',IN),('Yuno fee by month',Y),('Provider alternatives',P),('Summary',S),('Approval sensitivity',A),('Notes',N))]
sh.values().batchUpdate(spreadsheetId=SID,body={'valueInputOption':'USER_ENTERED','data':data}).execute()
# ---------------- formatting
NAVY={'red':16/255,'green':40/255,'blue':74/255}; WHITE={'red':1,'green':1,'blue':1}; LIGHT={'red':232/255,'green':234/255,'blue':245/255}; BLUEF={'red':0,'green':0,'blue':1}; YEL={'red':1,'green':0.95,'blue':0.8}
USD={'type':'CURRENCY','pattern':'"$"#,##0'}; PCT={'type':'PERCENT','pattern':'0.0%'}; BPS={'type':'NUMBER','pattern':'0" bps"'}; NUM={'type':'NUMBER','pattern':'#,##0'}
R=[]
def rg(t,r0,r1,c0,c1): return {'sheetId':ids[t],'startRowIndex':r0,'endRowIndex':r1,'startColumnIndex':c0,'endColumnIndex':c1}
def fmt(t,r0,r1,c0,c1,f,fields): R.append({'repeatCell':{'range':rg(t,r0,r1,c0,c1),'cell':{'userEnteredFormat':f},'fields':'userEnteredFormat('+fields+')'}})
def border(t,r0,r1,c0,c1): R.append({'updateBorders':{'range':rg(t,r0,r1,c0,c1),'top':{'style':'SOLID'},'bottom':{'style':'SOLID'},'left':{'style':'SOLID'},'right':{'style':'SOLID'},'innerHorizontal':{'style':'SOLID'},'innerVertical':{'style':'SOLID'}}})
HDR={'backgroundColor':NAVY,'textFormat':{'fontFamily':'Roboto','fontSize':10,'bold':True,'foregroundColor':WHITE},'verticalAlignment':'MIDDLE','wrapStrategy':'WRAP'}
SUB={'backgroundColor':LIGHT,'textFormat':{'fontFamily':'Roboto','fontSize':10,'bold':True}}
def base(t,n,c,widths):
    R.append({'updateSheetProperties':{'properties':{'sheetId':ids[t],'gridProperties':{'frozenRowCount':1,'frozenColumnCount':1,'hideGridlines':True}},'fields':'gridProperties(frozenRowCount,frozenColumnCount,hideGridlines)'}})
    fmt(t,0,n,0,c,{'textFormat':{'fontFamily':'Roboto','fontSize':10},'wrapStrategy':'WRAP','verticalAlignment':'MIDDLE'},'textFormat,wrapStrategy,verticalAlignment')
    fmt(t,0,n,0,1,{'textFormat':{'fontFamily':'Roboto','fontSize':10,'bold':True}},'textFormat')
    for j,w in enumerate(widths): R.append({'updateDimensionProperties':{'range':{'sheetId':ids[t],'dimension':'COLUMNS','startIndex':j,'endIndex':j+1},'properties':{'pixelSize':w},'fields':'pixelSize'}})
# Inputs
t='Inputs'; base(t,len(IN),5,[340,130,130,130,420])
for h,a,b in ((0,1,7),(8,9,15),(16,17,19),(20,21,27),(28,29,31)):
    fmt(t,h,h+1,0,5,HDR,'backgroundColor,textFormat,verticalAlignment,wrapStrategy'); border(t,h,b,0,5)
fmt(t,1,4,1,4,{'numberFormat':USD,'textFormat':{'fontFamily':'Roboto','fontSize':10,'foregroundColor':BLUEF}},'numberFormat,textFormat')
fmt(t,3,4,1,4,{'numberFormat':NUM,'textFormat':{'fontFamily':'Roboto','fontSize':10,'foregroundColor':BLUEF}},'numberFormat,textFormat')
fmt(t,4,7,1,2,{'textFormat':{'fontFamily':'Roboto','fontSize':10,'foregroundColor':BLUEF}},'textFormat'); fmt(t,5,7,1,2,{'numberFormat':USD},'numberFormat')
fmt(t,9,14,1,2,{'numberFormat':PCT,'textFormat':{'fontFamily':'Roboto','fontSize':10,'foregroundColor':BLUEF}},'numberFormat,textFormat'); fmt(t,14,15,0,5,SUB,'backgroundColor,textFormat'); fmt(t,14,15,1,2,{'numberFormat':PCT},'numberFormat')
fmt(t,17,19,1,2,{'numberFormat':PCT,'textFormat':{'fontFamily':'Roboto','fontSize':10,'foregroundColor':BLUEF}},'numberFormat,textFormat')
fmt(t,21,23,1,2,{'numberFormat':USD,'textFormat':{'fontFamily':'Roboto','fontSize':10,'foregroundColor':BLUEF}},'numberFormat,textFormat')
fmt(t,23,27,1,2,{'numberFormat':BPS,'textFormat':{'fontFamily':'Roboto','fontSize':10,'foregroundColor':BLUEF}},'numberFormat,textFormat')
fmt(t,29,31,1,2,{'numberFormat':PCT,'textFormat':{'fontFamily':'Roboto','fontSize':10,'foregroundColor':BLUEF}},'numberFormat,textFormat')
# Yuno fee by month
t='Yuno fee by month'; base(t,len(Y),8,[200,130,150,150,120,120,130,110])
R.append({'updateSheetProperties':{'properties':{'sheetId':ids[t],'gridProperties':{'frozenRowCount':0,'frozenColumnCount':1}},'fields':'gridProperties(frozenRowCount,frozenColumnCount)'}})
for s in SC:
    h=ytot[s]-14
    fmt(t,h,h+1,0,8,HDR,'backgroundColor,textFormat,verticalAlignment,wrapStrategy'); border(t,h,h+14,0,8)
    fmt(t,h+1,h+14,1,7,{'numberFormat':USD},'numberFormat'); fmt(t,h+1,h+14,7,8,{'numberFormat':BPS},'numberFormat')
    fmt(t,h+13,h+14,0,8,SUB,'backgroundColor,textFormat')
# Provider alternatives
t='Provider alternatives'; base(t,len(P),6,[330,130,130,130,170,120])
fmt(t,0,1,0,5,HDR,'backgroundColor,textFormat,verticalAlignment,wrapStrategy'); border(t,0,6,0,5)
fmt(t,1,5,1,4,{'numberFormat':{'type':'PERCENT','pattern':'0.00%'},'backgroundColor':YEL,'textFormat':{'fontFamily':'Roboto','fontSize':10,'foregroundColor':BLUEF}},'numberFormat,backgroundColor,textFormat')
fmt(t,5,6,0,5,SUB,'backgroundColor,textFormat'); fmt(t,5,6,1,4,{'numberFormat':{'type':'PERCENT','pattern':'0.00%'}},'numberFormat')
fmt(t,7,8,0,6,HDR,'backgroundColor,textFormat,verticalAlignment,wrapStrategy'); border(t,7,12,0,6)
fmt(t,8,12,1,4,{'numberFormat':{'type':'PERCENT','pattern':'0%'},'textFormat':{'fontFamily':'Roboto','fontSize':10,'foregroundColor':BLUEF}},'numberFormat,textFormat'); fmt(t,8,12,4,5,{'numberFormat':{'type':'PERCENT','pattern':'0.00%'}},'numberFormat')
# Summary
t='Summary'; base(t,len(S),8,[330,130,130,120,130,110,150,150])
fmt(t,0,1,0,8,HDR,'backgroundColor,textFormat,verticalAlignment,wrapStrategy'); border(t,0,len(S)-2,0,8)
r=1
for s in SC:
    fmt(t,r,r+1,0,8,SUB,'backgroundColor,textFormat'); fmt(t,r+1,r+5,1,5,{'numberFormat':USD},'numberFormat'); fmt(t,r+1,r+5,5,6,{'numberFormat':BPS},'numberFormat')
    fmt(t,r+1,r+5,6,7,{'numberFormat':{'type':'CURRENCY','pattern':'+"$"#,##0;-"$"#,##0;"$"0'}},'numberFormat'); fmt(t,r+1,r+5,7,8,{'numberFormat':{'type':'NUMBER','pattern':'+0" bps";-0" bps";0" bps"'}},'numberFormat')
    r+=6
R.append({'mergeCells':{'range':rg(t,len(S)-1,len(S),1,8),'mergeType':'MERGE_ALL'}}); fmt(t,len(S)-1,len(S),1,8,{'textFormat':{'fontFamily':'Roboto','fontSize':9,'italic':True}},'textFormat')
# Approval
t='Approval sensitivity'; base(t,len(A),5,[300,140,140,140,440])
fmt(t,0,1,0,5,HDR,'backgroundColor,textFormat,verticalAlignment,wrapStrategy'); border(t,0,len(A)-1,0,5)
fmt(t,1,len(A)-1,1,4,{'numberFormat':USD},'numberFormat'); fmt(t,len(A)-2,len(A)-1,1,4,{'numberFormat':{'type':'NUMBER','pattern':'0.0" pts"'}},'numberFormat'); fmt(t,len(A)-3,len(A)-1,0,5,SUB,'backgroundColor,textFormat')
for k in range(5): fmt(t,4+2*k,5+2*k,0,5,SUB,'backgroundColor,textFormat')
R.append({'mergeCells':{'range':rg(t,len(A)-1,len(A),1,5),'mergeType':'MERGE_ALL'}}); fmt(t,len(A)-1,len(A),1,5,{'textFormat':{'fontFamily':'Roboto','fontSize':9,'italic':True}},'textFormat')
# Notes
t='Notes'; base(t,len(N),3,[280,180,620]); fmt(t,0,1,0,3,HDR,'backgroundColor,textFormat,verticalAlignment,wrapStrategy'); border(t,0,len(N),0,3)
sh.batchUpdate(spreadsheetId=SID,body={'requests':R}).execute()
o=sh.values().batchGet(spreadsheetId=SID,ranges=["'Summary'!A1:H20","'Approval sensitivity'!A1:D14","'Yuno fee by month'!A1:H15"]).execute()
for vr in o['valueRanges']:
    for row in vr.get('values',[]): print(row)
    print('--')
