# -*- coding: utf-8 -*-
"""Cross-check market research JSON (apac.json, europe.json, latam.json) against Yuno coverage → ranking.json + review list."""
import json,re,sys,collections
SC='/private/tmp/claude-501/-Users-germantatis-Desktop-GTMCoding/e20b86c2-3386-425f-bf11-372e66253c70/scratchpad'
cov=json.load(open(f'{SC}/yuno_coverage_full.json'))
def nk(s): return re.sub(r'[^a-z0-9]','',(s or '').lower())
# market name → Yuno name(s) (either provider or method label). Lowercase normalised keys.
ALIAS={
 'unlimint':['Unlimit'],'omise':['Opn'],'opnpayments':['Opn'],'transbank':['Webpay','Transbank'],'webpayplus':['Webpay'],
 'decidir':['Prisma'],'payway':['Payway','Prisma'],'firstdata':['Fiserv'],'ingenico':['Worldline'],'sixpaymentservices':['Worldline'],
 'paypalbraintree':['Braintree'],'checkout':['Checkout.com'],'checkoutcom':['Checkout.com'],'jpmorgan':['J.P. Morgan (Orbital)'],'chase':['J.P. Morgan (Orbital)'],
 'authorizenet':['Authorize.Net'],'globalpayments':['Global Payments'],'evopayments':['EVO Payments'],'evo':['EVO Payments'],
 'visamastercard':['Visa','Mastercard'],'visamastercardamex':['Visa','Mastercard'],'cards':['Visa','Mastercard','Cards'],'internationalcards':['Visa','Mastercard','Cards'],
 'creditdebitcards':['Visa','Mastercard','Cards'],'visa':['Visa'],'mastercard':['Mastercard'],'amex':['Cards'],'americanexpress':['Cards'],
 'applepay':['Apple Pay'],'googlepay':['Google Pay'],'paypal':['PayPal'],'sepadirectdebit':['SEPA Direct Debit'],'sepa':['SEPA Direct Debit'],'sepalastschrift':['SEPA Direct Debit'],
 'ideal':['iDEAL'],'blik':['BLIK'],'swish':['Swish'],'vipps':['Vipps'],'vippsmobilepay':['Vipps','MobilePay'],'mobilepay':['MobilePay'],'twint':['TWINT'],
 'mbway':['MB WAY'],'multibanco':['Multibanco'],'satispay':['Satispay'],'eps':['EPS'],'bacs':['Bacs direct debit'],'bacsdirectdebit':['Bacs direct debit'],
 'autogiro':['Autogiro'],'betalingsservice':['Betalingsservice'],'klarna':['Klarna'],'trustly':['Trustly'],'openbanking':['Open banking'],'paybybank':['Open banking'],
 'bancontact':['Bancontact'],'przelewy24':['Przelewy24'],'p24':['Przelewy24'],'revolutpay':['Revolut Pay'],'revolut':['Revolut','Revolut Pay'],
 'gcash':['GCash'],'maya':['Maya'],'paymaya':['Maya'],'grabpay':['GrabPay'],'shopeepay':['ShopeePay'],'dana':['DANA'],'ovo':['OVO'],'gopay':['GoPay'],'qris':['QRIS'],
 'touchngo':['Touch \'n Go'],'touchngoewallet':['Touch \'n Go'],'tng':['Touch \'n Go'],'boost':['Boost'],'fpx':['FPX'],'paynow':['PayNow'],'promptpay':['Thai QR (PromptPay)'],
 'thaiqr':['Thai QR (PromptPay)'],'truemoney':['TrueMoney'],'truemoneywallet':['TrueMoney'],'alipay':['Alipay'],'alipayhk':['Alipay'],'wechatpay':['WeChat Pay'],'momo':['MoMo'],
 'afterpay':['Afterpay'],'zip':['Zip'],'zippay':['Zip'],'atome':['Atome'],'unionpay':['UnionPay'],'jcb':['Cards'],
 'pix':['PIX'],'pixautomatico':['PIX Automático'],'boleto':['Boleto'],'boletobancario':['Boleto'],'nupay':['NuPay'],'picpay':['PicPay'],'mercadopago':['Mercado Pago','Mercado Pago Wallet'],
 'mercadopagowallet':['Mercado Pago Wallet'],'nequi':['Nequi'],'daviplata':['Daviplata'],'pse':['PSE'],'breb':['Bre-B'],'efecty':['Efecty'],'bancolombia':['Bancolombia','Botón Bancolombia'],
 'oxxo':['OXXO'],'oxxopay':['OXXO Pay'],'spei':['SPEI'],'codi':['CoDi'],'kueski':['Kueski'],'kueskipay':['Kueski'],'aplazo':['Aplazo'],'yape':['Yape'],'plin':['Plin'],
 'pagoefectivo':['PagoEfectivo'],'niubiz':['Niubiz'],'izipay':['Izipay'],'webpay':['Webpay'],'khipu':['Khipu'],'fintoc':['Fintoc'],'mach':['MACH','Mach Pay'],'machpay':['Mach Pay'],
 'servipag':['Servipag'],'rapipago':['Rapipago'],'pagofacil':['Pago Fácil'],'rapipagopagofacil':['Rapipago','Pago Fácil'],'transferencias30':['Transferencias 3.0'],'modo':['MODO'],
 'yappy':['Yappy'],'clave':['Clave'],'azul':['Azul'],'cardnet':['Cardnet'],'datafast':['Datafast'],'medianet':['Medianet'],'deuna':['Deuna'],'pagalo':['Pagalo'],'bancard':['Bancard'],
 'baccredomatic':['BAC Credomatic'],'bac':['BAC Credomatic'],'evertec':['Evertec','PlacetoPay'],'placetopay':['PlacetoPay'],'powertranz':['Powertranz'],'fac':['FAC (First Atlantic Commerce)'],
 'firstatlanticcommerce':['FAC (First Atlantic Commerce)'],'kushki':['Kushki'],'payu':['PayU'],'wompi':['Wompi'],'epayco':['ePayco'],'credibanco':['Credibanco'],'redeban':['Redeban'],
 'conekta':['Conekta'],'openpay':['Openpay'],'prosa':['Prosa'],'banorte':['Banorte'],'bbva':['BBVA'],'fiserv':['Fiserv'],'cielo':['Cielo'],'rede':['Rede'],'getnet':['Getnet'],'stone':['Stone'],
 'pagarme':['Pagar.me'],'pagbank':['PagBank'],'pagseguro':['PagSeguro'],'vindi':['Vindi'],'zoop':['Zoop'],'ebanx':['EBANX'],'dlocal':['dLocal'],'adyen':['Adyen'],'stripe':['Stripe'],
 'prisma':['Prisma'],'mobbex':['Mobbex'],'nave':['Nave'],'bamboo':['Bamboo'],'astropay':['AstroPay'],'safetypay':['SafetyPay'],'pagsmile':['Pagsmile'],'payretailers':['PayRetailers'],
 'xendit':['Xendit'],'midtrans':['Midtrans'],'doku':['Doku'],'2c2p':['2C2P'],'asiapay':['AsiaPay'],'ecpay':['ECPay'],'boku':['Boku'],'antom':['Antom'],'airwallex':['Airwallex'],
 'nuvei':['Nuvei'],'rapyd':['Rapyd'],'worldpay':['Worldpay'],'worldline':['Worldline'],'cybersource':['Cybersource'],'nttdata':['NTT DATA'],'paymob':['Paymob'],'simpaisa':['Simpaisa'],
 'windcave':['Windcave'],'fatzebra':['Fat Zebra'],'paysquad':['Paysquad'],'gocardless':['GoCardless'],'mollie':['Mollie'],'redsys':['Redsys'],'iyzico':['iyzico'],'param':['Param'],
 'qnbfinansbank':['QNB Finansbank'],'nets':['Nets'],'payplug':['PayPlug'],'novalnet':['Novalnet'],'payabl':['payabl.'],'volt':['Volt'],'paysafe':['Paysafe'],'ppro':['PPRO'],
 'sibs':['SIBS'],'pixandpixautomatico':['PIX','PIX Automático'],'pixpixautomatico':['PIX','PIX Automático'],'pixautomatic':['PIX Automático'],'pixrecorrente':['PIX Automático'],'bancontactpayapp':['Bancontact'],'payconiqbybancontact':['Bancontact'],'comerciaglobalpayments':['Global Payments'],'comercia':['Global Payments'],'mayabusiness':['Maya'],'paymayabusiness':['Maya'],'unionpayinternational':['UnionPay'],'cupi':['UnionPay'],'nupaynubank':['NuPay'],'mercadopagocheckout':['Mercado Pago'],'webpayplustransbank':['Webpay'],'kushkipagos':['Kushki'],'pseach':['PSE'],'psebanktransfer':['PSE'],'bbvaprovincial':['BBVA'],'bbvamexico':['BBVA'],'redcompra':['Webpay'],'debitcardsredcompra':['Webpay'],'transbankwebpay':['Webpay'],'webpayoneclick':['Webpay'],'oneclick':['Webpay'],'nequipanama':['Nequi'],'mercadopagoargentina':['Mercado Pago'],'paywaydecidir':['Payway','Prisma'],'prismapayway':['Prisma','Payway'],'fiservfirstdata':['Fiserv'],'firstdatafiserv':['Fiserv'],'cybersourcevisa':['Cybersource'],'applepaygooglepay':['Apple Pay','Google Pay'],'googlepayapplepay':['Apple Pay','Google Pay'],'pixpixautomatico':['PIX','PIX Automático'],'cardsvisamastercard':['Visa','Mastercard'],'visamastercardelo':['Visa','Mastercard'],'elohipercard':[],'braintreepaypal':['Braintree'],'dlocalebanx':['dLocal','EBANX'],'opayo':['Opayo'],'elavon':[],'nexi':[],'wero':[],'bizum':[],'payconiq':[],'kaspi':[],'kaspipay':[],'cartesbancaires':[],'dankort':[],'troy':[],
 'elo':[],'hipercard':[],'carrierbilling':[],'directcarrierbilling':[],'dcb':[],
}
STATUS_RANK={'Live':0,'Homologating':1,'Integrated (code)':2}
GLOBAL_PROV={}
for _c,_e in cov.items():
    for _p,_v in _e['providers'].items(): GLOBAL_PROV.setdefault(nk(_p),_p)
GLOBAL_METH={}
for _c,_e in cov.items():
    for _m in list(_e['methods'])+list(_e['carried']): GLOBAL_METH.setdefault(nk(_m),_m)
GENERIC={'bankwallets','fintechwallets','installments','account2account','a2a','banktransfer','localbanktransfer','bankacquirers','debitcards','debitcardsonline','domesticdebitcards','cards','internationalcards','creditdebitcards'}
SCHEME={'elo','hipercard','cartesbancaires','cb','dankort','bancomat','bancomatpay','postepay','troy','eftpos','cabal','naranja','naranjax','cabaluruguay','oca','jcb','amex','americanexpress','diners','dinersclub','girocard','vpay','maestro','redcompra','unionpay','rupay'}
NEVER={'abapayway','payway'}
NEVER_BY_COUNTRY={('Czech Republic','gopay'),('Czech Republic','gopaycz')}
SUFFIX={'mexico','provincial','cr','sv','png','uruguay','bolivia','macau','panama','venezuela','hk','taiwan','hongkong','singapore','malaysia','australia','nz','newzealand','chile','peru','colombia','argentina','brazil','brasil','ecuador','guatemala','honduras','nicaragua','paraguay','costarica','elsalvador','dominicana','rd','pakistan','bangladesh','srilanka','nepal','cambodia','laos','mongolia','myanmar','indonesia','vietnam','philippines','thailand','global','international','ltd','sa','sas','inc'}
def variants(name):
    out=[nk(name)]
    w=name.replace('(',' ').replace(')',' ').split()
    if len(w)>1 and nk(w[-1]) in SUFFIX: out.append(nk(' '.join(w[:-1])))
    if len(w)>1 and nk(w[0]) in SUFFIX: out.append(nk(' '.join(w[1:])))
    low=name.lower()
    if 'carrier' in low or 'telco bill' in low or 'dcb' in low or 'isp billing' in low: out.append('carrierbilling')
    if low.startswith('debit card') or low=='domestic debit cards' or 'visa' in low or 'mastercard' in low or 'credit card' in low or low.startswith('cards') or 'international cards' in low: out.append('cards')
    if 'app store' in low or 'in-app' in low: out.append('appstorebilling')
    return out
def split_top(name):
    parts=[];depth=0;cur=''
    for ch in name:
        if ch=='(': depth+=1
        if ch==')': depth-=1
        cur+=ch
    # split on ' / ' only when outside parentheses
    res=[];depth=0;cur=''
    i=0
    while i<len(name):
        if name[i]=='(': depth+=1
        if name[i]==')': depth-=1
        if depth==0 and name[i:i+3]==' / ': res.append(cur); cur=''; i+=3; continue
        cur+=name[i]; i+=1
    res.append(cur); return [r.strip() for r in res if r.strip()]
def have_one(country,name,aliases):
    e=cov.get(country)
    if not e: return None
    keys=variants(name)+[nk(a) for a in aliases or []]
    if any((country,k) in NEVER_BY_COUNTRY for k in keys): return None
    if any(k in ('cardinstallments','installments','taksit','installmentcards') for k in keys):
        live=[p for p,v in e['providers'].items() if v['status']=='Live']
        return (3,'Partial','installments depend on the acquirer connection; local acquirers live through Yuno: '+', '.join(live[:4]),'note') if live else None
    if 'carrierbilling' in keys:
        if 'Boku' in e['providers']: return (3,'Partial','Boku live in country; carrier billing not catalogued as a method','note')
        return None
    if 'appstorebilling' in keys: return (4,'N/A','platform billing, not a Yuno connection','note')
    if 'paypal' in keys and 'PayPal' not in e['methods'] and 'PayPal' not in e['carried']: return (4,'N/A','PayPal does not serve this market (paypal.com country list)','note')
    if 'applepay' in keys and 'Apple Pay' not in e['methods'] and 'Apple Pay' not in e['carried']: return (4,'N/A','Apple Pay not offered in this market (Apple)','note')
    if any(k in SCHEME for k in keys):
        live=[p for p,v in e['providers'].items() if v['status']=='Live']
        if live: return (3,'Partial','local card scheme; rides on the card acquirers live through Yuno, not listed as a separate method','note')
    cands=set()
    for k in keys:
        cands.update(ALIAS.get(k,[]))
        # also try raw name against yuno names
        for p in e['providers']:
            if nk(p)==k: cands.add(p)
        for m in list(e['methods'])+list(e['carried']):
            if nk(m)==k: cands.add(m)
    hits=[]
    for cnd in cands:
        if cnd in e['providers']: hits.append((STATUS_RANK[e['providers'][cnd]['status']], e['providers'][cnd]['status'], cnd, 'provider'))
        if cnd in e['methods']: hits.append((STATUS_RANK.get(e['methods'][cnd]['status'],0), e['methods'][cnd]['status'], cnd, 'direct method'))
        if cnd in e['carried']: hits.append((0,'Live',cnd,'via '+', '.join(e['carried'][cnd][:4])+(' …' if len(e['carried'][cnd])>4 else '')))
    if hits: hits.sort(); return hits[0]
    if any(k in GENERIC for k in keys): return (4,'Generic','category, not a specific connection','note')
    for k in variants(name):
        if k in NEVER: continue
        if k in GLOBAL_PROV: return (3,'Elsewhere',GLOBAL_PROV[k],'connection exists in other countries, not listed here')
        if k in GLOBAL_METH: return (3,'Elsewhere',GLOBAL_METH[k],'available in other countries, not listed here')
    return None
def have(country,name,aliases):
    parts=split_top(name)
    res=[have_one(country,p,aliases if len(parts)==1 else None) for p in parts]
    got=[r for r in res if r]
    if not got: return None
    got.sort()
    if len(parts)>1:
        matched=[p for p,r in zip(parts,res) if r]
        return (got[0][0],got[0][1],'; '.join(f"{p}: {r[2]}" for p,r in zip(parts,res) if r),got[0][3]+('' if len(matched)==len(parts) else f"; unmatched: {', '.join(p for p,r in zip(parts,res) if not r)}"))
    return got[0]
rows=[]; review=collections.Counter()
for fn in ('apac.json','europe.json','latam.json'):
    try: data=json.load(open(f'{SC}/{fn}'))
    except FileNotFoundError: print('missing',fn); continue
    for country,blocks in data.items():
        c='Turkey' if country in ('Türkiye','Turkiye') else country
        for typ,key in (('Method','methods'),('Processor','processors')):
            for it in blocks.get(key,[]):
                h=have(c,it['name'],it.get('aliases'))
                status = 'MISSING' if h is None else h[1]
                rows.append({'country':c,'type':typ,'name':it['name'],'rating':int(it.get('rating',0)),'recurring':it.get('recurring'),'why':it.get('why',''),'source':it.get('source',''),
                             'yuno_status':status,'yuno_match':'' if h is None else f"{h[2]} ({h[3]})"})
                if h is None or h[1]=='Elsewhere': review[(it['name'],typ,'' if h is None else 'ELSEWHERE→'+h[2])]+=1
OVERRIDES=[
 ('Kazakhstan','Visa/Mastercard (KZT','Partial','cards only through cross-border PSPs live in Kazakhstan (Ecommpay, Nuvei, Pagsmile, Pockyt); no KZT local acquirer listed'),
 ('Turkey','Visa/Mastercard credit cards','Live','local TRY acquiring: Param live; iyzico and QNB Finansbank integrated in code; Adyen, Worldline, Nuvei also live'),
 ('Pakistan','JazzCash','Partial','Simpaisa (Pakistani wallet and carrier-billing aggregator) live through Yuno; JazzCash not catalogued as a method, confirm activation'),
 ('Pakistan','Easypaisa','Partial','Simpaisa (Pakistani wallet and carrier-billing aggregator) live through Yuno; Easypaisa not catalogued as a method, confirm activation'),
]
for r in rows:
    for c,sub,st,note in OVERRIDES:
        if r['country']==c and r['name'].startswith(sub): r['yuno_status']=st; r['yuno_match']=note
json.dump(rows,open(f'{SC}/ranking.json','w'),ensure_ascii=False,indent=1)
print(len(rows),'items;', sum(1 for r in rows if r['yuno_status']=='MISSING'),'unmatched')
print('\nUNMATCHED (name, type) × countries:')
for (n,t,x),k in sorted(review.items(), key=lambda x:(-x[1],x[0])): print(f'  {k:2d}  {t:9} {n}  {x}')
