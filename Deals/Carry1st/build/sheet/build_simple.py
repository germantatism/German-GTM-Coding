# Simple 3-tab version (16 Oct 2026): Proposal, Calculator, Notes.
import warnings, os; warnings.filterwarnings('ignore')
from google.oauth2 import service_account
from googleapiclient.discovery import build
SID='1oIq55KHyjLA4R73_WtDLYLB5bG93rkh3WGcA6A3Mtmw'
creds=service_account.Credentials.from_service_account_file(os.path.expanduser('~/.config/gsuite/sa.json'),scopes=['https://www.googleapis.com/auth/spreadsheets'])
sh=build('sheets','v4',credentials=creds,cache_discovery=False).spreadsheets()
meta=sh.get(spreadsheetId=SID).execute(); cur={s['properties']['title']:s['properties']['sheetId'] for s in meta['sheets']}
prop=cur['What the platform fee covers'] if 'What the platform fee covers' in cur else cur['Proposal']
req=[{'deleteSheet':{'sheetId':i}} for t,i in cur.items() if i!=prop]
req+=[{'updateSheetProperties':{'properties':{'sheetId':prop,'title':'Proposal','index':0},'fields':'title,index'}},{'addSheet':{'properties':{'title':'Calculator'}}},{'addSheet':{'properties':{'title':'Notes'}}}]
sh.batchUpdate(spreadsheetId=SID,body={'requests':req}).execute()
ids={s['properties']['title']:s['properties']['sheetId'] for s in sh.get(spreadsheetId=SID).execute()['sheets']}
P="'Proposal'!"
def usage(c): return (f"MAX(0,MIN({c},2000000)-500000)*{P}$B$3/10000+MAX(0,MIN({c},5000000)-2000000)*{P}$B$4/10000"
                      f"+MAX(0,MIN({c},10000000)-5000000)*{P}$B$5/10000+MAX(0,{c}-10000000)*{P}$B$6/10000")
C=[['PLUG IN YOUR NUMBERS','Scenario 1','Scenario 2','Scenario 3','Notes'],          #1
 ['Monthly sales (USD)',2500000,4500000,6000000,'Edit in blue'],                     #2
 ['Average ticket (USD)',10,10,10,'Carry1st estimate'],                               #3
 ['EBANX all-in rate',0.045,0.045,0.045,'Replace with EBANX’s quote'],          #4
 ['Second provider all-in rate',0.040,0.040,0.040,'Replace with the quote'],         #5
 ['Share of sales routed to the second provider',0.3,0.3,0.3,'0% if EBANX only'],   #6
 ['Approval rate today',0.75,0.75,0.75,'Replace with Carry1st data'],                #7
 ['Approval gain through Yuno (points)',2,3,5,'Garena saw 8% (reference, not a promise)'],  #8
 ['Carry1st margin on sales',0.15,0.15,0.15,'Replace with Carry1st data'],           #9
 ['','','','',''],                                                                    #10
 ['YUNO FEE, A MONTH','','','',''],                                                   #11
 ['Platform fee']+[f'={P}$B$2']*3+['Covers the first $500K of monthly sales'],        #12
 ['Usage fee']+[f'={usage(c+"2")}' for c in 'BCD']+['40 / 30 / 20 / 10 bps above $500K'],  #13
 ['Total paid to Yuno']+[f'={c}12+{c}13' for c in 'BCD']+[''],                       #14
 ['Share of sales']+[f'={c}14/{c}2*10000' for c in 'BCD']+[''],                      #15
 ['Per transaction']+[f'={c}14/({c}2/{c}3)' for c in 'BCD']+[''],                    #16
 ['','','','',''],                                                                    #17
 ['TOTAL COST, A MONTH','','','',''],                                                 #18
 ['EBANX direct: provider cost']+[f'={c}2*{c}4' for c in 'BCD']+['All sales on EBANX'],  #19
 ['Through Yuno: provider cost']+[f'={c}2*((1-{c}6)*{c}4+{c}6*{c}5)' for c in 'BCD']+['EBANX plus the second provider'],  #20
 ['Through Yuno: Yuno fee']+[f'={c}14' for c in 'BCD']+[''],                          #21
 ['Through Yuno: total cost']+[f'={c}20+{c}21' for c in 'BCD']+[''],                  #22
 ['Cost difference vs EBANX direct']+[f'={c}22-{c}19' for c in 'BCD']+['Positive = through Yuno costs more on rates alone'],  #23
 ['','','','',''],                                                                    #24
 ['MORE SALES APPROVED, A MONTH','','','',''],                                        #25
 ['Extra approved sales']+[f'={c}2/{c}7*{c}8/100' for c in 'BCD']+['Sales recovered by routing and retries'],  #26
 ['Extra margin for Carry1st']+[f'={c}26*{c}9' for c in 'BCD']+[''],                 #27
 ['','','','',''],                                                                    #28
 ['RESULT','','','',''],                                                              #29
 ['Net for Carry1st, a month']+[f'={c}27-{c}23' for c in 'BCD']+['Extra margin minus the cost difference'],  #30
 ['Net for Carry1st, a year']+[f'={c}30*12' for c in 'BCD']+[''],                    #31
 ['Approval gain that pays for Yuno (points)']+[f'=MAX(0,{c}23)/({c}2/{c}7*{c}9)*100' for c in 'BCD']+['Below this, the cost difference is larger than the extra margin']]  #32
N=[['NOTE','DETAIL'],
 ['How to use','Change the blue cells in Calculator. Everything else updates.'],
 ['Bands','Applied marginally: each band is charged only on the sales inside it. To confirm with Justo.'],
 ['Platform fee','$7,500 a month covering the first $500K of monthly sales, equal to 150 bps at $500K. To confirm with Justo.'],
 ['Provider rates','EBANX and second-provider rates are placeholders until the quotes arrive.'],
 ['Approval','Garena’s 8% approval improvement was shared on the call as a reference, not a result promised for Carry1st.'],
 ['Billing','Platform fee billed annually; usage billed monthly on approved sales only. Declines are not billed.']]
sh.values().batchUpdate(spreadsheetId=SID,body={'valueInputOption':'USER_ENTERED','data':[{'range':"'Calculator'!A1",'values':C},{'range':"'Notes'!A1",'values':N}]}).execute()
NAVY={'red':16/255,'green':40/255,'blue':74/255}; WHITE={'red':1,'green':1,'blue':1}; LIGHT={'red':232/255,'green':234/255,'blue':245/255}; BLUEF={'red':0,'green':0,'blue':1}
USD={'type':'CURRENCY','pattern':'"$"#,##0'}; PCT={'type':'PERCENT','pattern':'0.0%'}; BPS={'type':'NUMBER','pattern':'0" bps"'}
R=[]
def rg(t,r0,r1,c0,c1): return {'sheetId':ids[t],'startRowIndex':r0,'endRowIndex':r1,'startColumnIndex':c0,'endColumnIndex':c1}
def fmt(t,r0,r1,c0,c1,f,fields): R.append({'repeatCell':{'range':rg(t,r0,r1,c0,c1),'cell':{'userEnteredFormat':f},'fields':'userEnteredFormat('+fields+')'}})
def border(t,r0,r1,c0,c1): R.append({'updateBorders':{'range':rg(t,r0,r1,c0,c1),'top':{'style':'SOLID'},'bottom':{'style':'SOLID'},'left':{'style':'SOLID'},'right':{'style':'SOLID'},'innerHorizontal':{'style':'SOLID'},'innerVertical':{'style':'SOLID'}}})
HDR={'backgroundColor':NAVY,'textFormat':{'fontFamily':'Roboto','fontSize':10,'bold':True,'foregroundColor':WHITE},'verticalAlignment':'MIDDLE','wrapStrategy':'WRAP'}
for t,n,c,ws in (('Calculator',len(C),5,[330,140,140,140,380]),('Notes',len(N),2,[200,700])):
    R.append({'updateSheetProperties':{'properties':{'sheetId':ids[t],'gridProperties':{'frozenRowCount':1,'frozenColumnCount':1,'hideGridlines':True}},'fields':'gridProperties(frozenRowCount,frozenColumnCount,hideGridlines)'}})
    fmt(t,0,n,0,c,{'textFormat':{'fontFamily':'Roboto','fontSize':10},'wrapStrategy':'WRAP','verticalAlignment':'MIDDLE'},'textFormat,wrapStrategy,verticalAlignment')
    fmt(t,0,n,0,1,{'textFormat':{'fontFamily':'Roboto','fontSize':10,'bold':True}},'textFormat')
    for j,w in enumerate(ws): R.append({'updateDimensionProperties':{'range':{'sheetId':ids[t],'dimension':'COLUMNS','startIndex':j,'endIndex':j+1},'properties':{'pixelSize':w},'fields':'pixelSize'}})
t='Calculator'
for h,b in ((0,9),(10,16),(17,23),(24,27),(28,32)):
    fmt(t,h,h+1,0,5,HDR,'backgroundColor,textFormat,verticalAlignment,wrapStrategy'); border(t,h,b,0,5)
blue=lambda f:{**f,'textFormat':{'fontFamily':'Roboto','fontSize':10,'foregroundColor':BLUEF}}
fmt(t,1,3,1,4,blue({'numberFormat':USD}),'numberFormat,textFormat'); fmt(t,3,7,1,4,blue({'numberFormat':PCT}),'numberFormat,textFormat')
fmt(t,7,8,1,4,blue({'numberFormat':{'type':'NUMBER','pattern':'0.0" pts"'}}),'numberFormat,textFormat'); fmt(t,8,9,1,4,blue({'numberFormat':PCT}),'numberFormat,textFormat')
fmt(t,11,14,1,4,{'numberFormat':USD},'numberFormat'); fmt(t,14,15,1,4,{'numberFormat':BPS},'numberFormat'); fmt(t,15,16,1,4,{'numberFormat':{'type':'CURRENCY','pattern':'"$"0.000'}},'numberFormat')
fmt(t,18,23,1,4,{'numberFormat':USD},'numberFormat'); fmt(t,22,23,1,4,{'numberFormat':{'type':'CURRENCY','pattern':'+"$"#,##0;-"$"#,##0;"$"0'}},'numberFormat')
fmt(t,25,27,1,4,{'numberFormat':USD},'numberFormat'); fmt(t,29,31,1,4,{'numberFormat':{'type':'CURRENCY','pattern':'+"$"#,##0;-"$"#,##0;"$"0'}},'numberFormat'); fmt(t,31,32,1,4,{'numberFormat':{'type':'NUMBER','pattern':'0.0" pts"'}},'numberFormat')
for r in (13,21,29,30): fmt(t,r,r+1,0,5,{'backgroundColor':LIGHT,'textFormat':{'fontFamily':'Roboto','fontSize':10,'bold':True}},'backgroundColor,textFormat')
fmt('Notes',0,1,0,2,HDR,'backgroundColor,textFormat,verticalAlignment,wrapStrategy'); border('Notes',0,len(N),0,2)
sh.batchUpdate(spreadsheetId=SID,body={'requests':R}).execute()
print([s['properties']['title'] for s in sh.get(spreadsheetId=SID).execute()['sheets']])
for r in sh.values().get(spreadsheetId=SID,range="'Calculator'!A11:D32").execute()['values']: print(r)
