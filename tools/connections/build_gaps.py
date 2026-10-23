"""Merge adidas research + agent research + manual rows -> ratings table with Yuno status. Outputs CSVs + xlsx in scratchpad/out."""
import json, re, glob, os, csv, collections, unicodedata
SP = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(SP, 'out'); os.makedirs(OUT, exist_ok=True)
ROOT = '/Users/germantatis/Desktop/GTMCoding'
def nk(s):
    s = unicodedata.normalize('NFKD', s or ''); s = ''.join(ch for ch in s if not unicodedata.combining(ch))
    return re.sub(r'[^a-z0-9]', '', s.lower())
def canon(name): return nk(re.split(r' \(| / | or ', name)[0])
REGION = {}
cfg = json.load(open(f'{ROOT}/Deals/Waymo/build/config.json'))
ORDER = []
for r in cfg['regions']:
    for c in r['countries']: REGION[c] = r['name']; ORDER.append(c)
# ---------------- coverage from the rebuilt rows.json
import sys as _sys; _sys.path.insert(0, f'{ROOT}/tools/connections'); import lib as _lib
_lib.APPLY_HOMOLOGATING_EXTRA = False   # real status, not the deck's homologation framing
_lib.CODE_AS_LIVE = False
_lib.SIGNED_AS_HOMOLOGATING = False   # real status: signed partners stay 'Signed' in the ratings sheet   # real status: 'Integrated (code)' stays distinct from Live in the ratings sheet
rows = _lib.Data(ORDER).rows(signed=True)
COV = collections.defaultdict(lambda: collections.defaultdict(set))
for c, typ, name, meths, st, key in rows:
    if typ == 'Provider':
        if st == 'Live': COV[c]['live'].add(name); COV[c]['methods'] |= set(meths)
        elif st == 'Live (cross-border)': COV[c]['xb'].add(name)
        elif st == 'Homologating': COV[c]['hom'].add(name)
        elif st == 'Integrated (code)': COV[c]['code'].add(name); COV[c]['code_methods'] |= set(meths)
        elif st in ('Activation on request', 'On request'): COV[c]['request'].add(name)
    else:
        if st == 'Live': COV[c]['direct'].add(name)
        elif st == 'Signed': COV[c]['signed'].add(name)
        elif st in ('On request',): COV[c]['request'].add(name)
LIVE_ANYWHERE = set().union(*[v['live'] for v in COV.values()])
ALIAS = {  # research name -> names as Yuno lists them
 'promptpay': ['thaiqrpromptpay'], 'thaiqr': ['thaiqrpromptpay'], 'knet': ['knet', 'kfast'], 'napsqpay': ['napsqpay', 'qpay'], 'qpay': ['qpay'],
 'touchngoewallet': ['touchngo'], 'tngewallet': ['touchngo'], 'touchngo': ['touchngo'], 'grabpay': ['grabpay'], 'mercadopago': ['mercadopago'],
 'transbank': ['transbank', 'webpay'], 'webpayplus': ['webpay'], 'sinpemovil': ['sinpemovil'], 'sinpemvil': ['sinpemovil'], 'yappy': ['yappy'],
 'clave': ['clave'], 'tarjetaclave': ['clave'], 'nhnkcp': ['nhnkcp'], 'kcp': ['nhnkcp'], 'omise': ['opn'], 'opnpayments': ['opn'], 'opn': ['opn'],
 'jpmorgan': ['jpmorganorbital'], 'chasepaymentech': ['jpmorganorbital'], 'jpmorganchase': ['jpmorganorbital'], 'allinpay': ['allinpay'],
 'cal': ['calisraelcreditcards'], 'icccal': ['calisraelcreditcards'], 'visacal': ['calisraelcreditcards'], 'calisraelcreditcards': ['calisraelcreditcards'],
 'bit': ['bit'], 'bitbankhapoalim': ['bit'], 'max': ['max'], 'maxleumicard': ['max'], 'finaro': ['finaroshift4'], 'shift4': ['finaroshift4'], 'credorax': ['finaroshift4'],
 'bamboopayment': ['bamboo'], 'bamboo': ['bamboo'], 'plin': ['plin'], 'yape': ['yape'], 'paynow': ['paynow'], 'dana': ['dana'], 'gopay': ['gopay'],
 'duitnowqr': ['duitnowqr'], 'duitnow': ['duitnowqr'], 'zalopay': ['zalopay'], 'vnpay': ['vnpayqr'], 'vnpayqr': ['vnpayqr'], 'napas': ['napasdomesticcardsandvietqr'],
 'vietqr': ['napasdomesticcardsandvietqr'], 'viettelmoney': ['viettelmoneyviettelpay'], 'viettelpay': ['viettelmoneyviettelpay'], 'viettelpayviettelmoney': ['viettelmoneyviettelpay'],
 'momo': ['momo'], 'gcash': ['gcash'], 'maya': ['maya'], 'paymaya': ['maya'], 'mayabusiness': ['maya'], 'payu': ['payu'], 'ebanx': ['ebanx'], 'dlocal': ['dlocal'], 'localpayment': ['localpayment'], 'pixautomatico': ['pixautomatico'], 'qrbcb': ['qrbcb'], 'qrsimple': ['qrbcb'], 'duitnowtransfer': ['duitnowqr'], 'napas247': ['napasdomesticcardsandvietqr'], 'onlinebanking': ['onlinebanking'], 'qrph': ['qrph'], 'fpx': ['fpx'], 'qris': ['qris'], 'ovo': ['ovo'], 'shopeepay': ['shopeepay'],
 'truemoney': ['truemoney'], 'truemoneywallet': ['truemoney'], 'kakaopay': ['kakaopay'], 'naverpay': ['naverpay'], 'tosspay': ['tosspay'], 'payco': ['payco'], 'samsungpay': ['samsungpay'],
 'paypay': ['paypay'], 'konbini': ['konbini'], 'applepay': ['applepay'], 'googlepay': ['googlepay'], 'paypal': ['paypal'], 'klarna': ['klarna'], 'sepadirectdebit': ['sepadirectdebit'], 'sepa': ['sepadirectdebit'],
 'sofort': ['klarna'], 'klarnasofort': ['klarna'], 'paybybank': ['volt', 'trustly', 'openbanking'], 'openbanking': ['volt', 'trustly', 'openbanking'], 'volt': ['volt'], 'trustly': ['trustly'],
 'bacs': ['bacsdirectdebit'], 'bacsdirectdebit': ['bacsdirectdebit'], 'paddirectdebit': ['paddirectdebit'], 'pad': ['paddirectdebit'], 'becs': ['becsdirectdebit'], 'becsdirectdebit': ['becsdirectdebit'],
 'upi': ['upi'], 'upiautopay': ['upiautopay'], 'billdesk': ['billdesk'], 'razorpay': ['razorpay'], 'payu': ['payu'], 'ccavenue': ['ccavenue'], 'mada': ['mada'], 'stcpay': ['stcpay'], 'sadad': ['sadad'],
 'careempay': ['careempay'], 'omannet': ['omannet'], 'benefit': ['benefit'], 'benefitpay': ['benefit'], 'fawry': ['fawry'], 'vodafonecash': ['vodafonecash'], 'meeza': ['meeza'], 'paymob': ['paymob'],
 'efawateercom': ['efawateercom'], 'meps': ['middleeastpaymentsmeps'], 'middleeastpaymentservices': ['middleeastpaymentsmeps'], 'networkinternational': ['networkinternational'],
 'amazonpaymentservices': ['amazonpaymentsservices'], 'amazonpaymentsservices': ['amazonpaymentsservices'], 'payfort': ['amazonpaymentsservices'], 'tap': ['tappayments'], 'tappayments': ['tappayments'],
 'checkoutcom': ['checkoutcom'], 'checkout': ['checkoutcom'], 'nbk': ['nbknationalbankofkuwait'], 'nationalbankofkuwait': ['nbknationalbankofkuwait'], 'qnb': ['qatarnationalbank'], 'qatarnationalbank': ['qatarnationalbank'],
 'fab': ['nationalbankofabudhabinbad'], 'firstabudhabibank': ['nationalbankofabudhabinbad'], 'mashreq': ['mashreqbank'], 'mashreqbank': ['mashreqbank'], 'bbvaprovincial': ['bbva'], 'provincial': ['bbva'],
 'ecpay': ['ecpay'], 'lsecpay': ['ecpay'], 'useepay': ['useepay'], 'unlimit': ['unlimit'], 'windcave': ['windcave'], 'fatzebra': ['fatzebra'], 'gocardless': ['gocardless'], 'moneris': ['moneris'],
 'globalpayments': ['globalpayments'], 'elavon': ['elavon'], 'worldline': ['worldline'], 'anzworldline': ['worldline'], 'worldlinenz': ['worldline'], 'paymark': ['worldline'], 'redsys': ['redsys'],
 'getnet': ['getnet'], 'santandergetnet': ['getnet'], 'bbva': ['bbva'], 'comerciaglobalpayments': ['globalpayments'], 'caixabank': ['globalpayments'], 'opayo': ['opayo'], 'sagepay': ['opayo'], 'elavonuk': ['elavon'],
 'cardnet': ['cardnet'], 'azul': ['azul'], 'midtrans': ['midtrans'], 'doku': ['doku'], 'xendit': ['xendit'], 'asiapay': ['asiapay'], '2c2p': ['2c2p'], 'nium': ['nium'], 'ppro': ['ppro'], 'paysafe': ['paysafe'],
 'bancard': ['bancard'], 'niubiz': ['niubiz'], 'izipay': ['izipay'], 'culqi': ['culqi'], 'openpay': ['openpay'], 'conekta': ['conekta'], 'prosa': ['prosa'], 'payway': ['payway'], 'prisma': ['prisma'], 'modo': ['modo'],
 'nequi': ['nequi'], 'daviplata': ['daviplata'], 'pse': ['pse'], 'breb': ['breb'], 'pix': ['pix'], 'spei': ['spei'], 'codi': ['codi'], 'dimo': ['dimo'], 'oxxo': ['oxxo', 'oxxopay'], 'mach': ['mach'], 'khipu': ['khipu'],
 'fintoc': ['fintoc'], 'deuna': ['deuna'], 'pagoefectivo': ['pagoefectivo'], 'baccredomatic': ['baccredomatic'], 'bac': ['baccredomatic'], 'credibanco': ['credibanco'], 'redeban': ['redeban'], 'wompi': ['wompi'],
 'mercadopagowallet': ['mercadopagowallet'], 'itau': ['itau'], 'refacil': ['refacil'], 'kredivo': ['kredivo'], 'linepay': ['linepay'], 'rabbitlinepay': ['rabbitlinepay'], 'alipayhk': ['alipayhk'], 'fps': ['fpsqr'],
 'octopus': ['octopus'], 'payme': ['payme'], 'wechatpayhk': ['wechatpayhk'], 'interac': ['interac'], 'bizum': ['bizum'], 'rakutenpay': ['rakutenpay'], 'jcb': ['jcb'], 'gmopaymentgateway': ['gmopaymentgateway'], 'gmo': ['gmopaymentgateway'],
 'sbpaymentservice': ['sbpaymentservice'], 'sbpayment': ['sbpaymentservice'], 'sonypaymentservices': ['sonypaymentservices'], 'sonypayment': ['sonypaymentservices'], 'payssion': ['payssion'],
 'kginicis': ['kginicis'], 'tosspayments': ['tosspayments'], 'nicepayments': ['nicepayments'], 'jkopay': ['jkopay'], 'taiwanpay': ['taiwanpay'], 'newebpay': ['newebpay'], 'tappay': ['tappay'],
 'adyen': ['adyen'], 'stripe': ['stripe'], 'worldpay': ['worldpay'], 'cybersource': ['cybersource'], 'braintree': ['braintree'], 'fiserv': ['fiserv'], 'nuvei': ['nuvei'], 'rapyd': ['rapyd'], 'airwallex': ['airwallex'],
 'visa': ['visa'], 'mastercard': ['mastercard'], 'cards': ['cards'], 'cliq': ['cliq'], 'instapay': ['instapay'], 'aani': ['aani'], 'jaywan': ['jaywan'], 'magnati': ['magnati'], 'urpay': ['urpay'], 'payit': ['payit'],
 'pagomovil': ['pagomovil'], 'pagomvil': ['pagomovil'], 'zelle': ['zelle'], 'mercantil': ['mercantil'], 'banesco': ['banesco'], 'credicard': ['credicard'], 'biopago': ['biopago'],
 'rupay': ['rupay'], 'netbanking': ['netbanking'], 'paytm': ['paytm'], 'phonepe': ['phonepe'], 'cashfree': ['cashfree'], 'eftpos': ['eftpos'], 'payto': ['payto'], 'payid': ['payid'], 'account2account': ['account2account'],
 'wero': ['wero'], 'girocard': ['girocard'], 'nexi': ['nexi'], 'concardis': ['concardis'], 'payone': ['payone'], 'unzer': ['unzer'], 'barclaycard': ['barclaycard'], 'amex': ['americanexpress'], 'americanexpress': ['americanexpress'],
 'dbspaylah': ['dbspaylah'], 'paylah': ['dbspaylah'], 'nets': ['nets'], 'enets': ['nets'], 'dbs': ['dbs'], 'uob': ['uob'], 'ocbc': ['ocbc'], 'hitpay': ['hitpay'], 'kbank': ['kasikornbank'], 'kasikornbank': ['kasikornbank'],
 'scb': ['siamcommercialbank'], 'siamcommercialbank': ['siamcommercialbank'], 'bangkokbank': ['bangkokbank'], 'krungsri': ['krungsri'], 'kplus': ['kplus'], 'bca': ['bca'], 'mandiri': ['bankmandiri'], 'bankmandiri': ['bankmandiri'],
 'bni': ['bni'], 'linkaja': ['linkaja'], 'bifast': ['bifast'], 'faspay': ['faspay'], 'maybank': ['maybank'], 'cimb': ['cimb'], 'ipay88': ['ipay88'], 'razermerchantservices': ['razermerchantservices'], 'eghl': ['eghl'],
 'publicbank': ['publicbank'], 'boost': ['boost'], 'mae': ['mae'], 'bdo': ['bdo'], 'paymongo': ['paymongo'], 'payoo': ['payoo'], 'onepay': ['onepay'], 'alepay': ['alepay'], 'nganluong': ['nganluong'],
 'techcombank': ['techcombank'], 'vietcombank': ['vietcombank'], 'virtualaccount': ['virtualaccount'], 'virtualaccounts': ['virtualaccount'], 'nequipanama': ['nequi'], 'bancolombiabutton': ['botonbancolombia'], 'botonbancolombia': ['botonbancolombia'], 'tosspayments': ['tosspayments'], 'networkinternationaljordan': ['networkinternational'], 'anzworldlinepaymentsolutions': ['worldline'], 'westpac': ['payway'], 'westpacpayway': ['payway'], 'chasepaymentsolutions': ['jpmorganorbital'], 'globalpaymentscanada': ['globalpayments'], 'elavoncanada': ['elavon'], 'interacdebit': ['interac'], 'interacetransfer': ['interac'], 'ipay88': ['nttdata'], 'grabpaywallet': ['grabpay'], 'paymebyhsbc': ['payme'], 'stclocalentity': ['stripe'], 'stripelocalentity': ['stripe'], 'opnpayments': ['opn'], 'globalpaymentsasiapacific': ['globalpayments'], 'hsbcglobalpaymentsasiapacific': ['globalpayments'], 'sonypaymentservicesrenamedsplinksoct2025': ['sonypaymentservices'], 'nhnkcpdomesticpg': ['nhnkcp'], 'redsystpvvirtual': ['redsys'], 'getnetsantander': ['getnet'], 'thawanipay': ['thawani'], 'benefitdebitscheme': ['benefit'], 'mepsmiddleeastpaymentservices': ['middleeastpaymentsmeps'], 'orangecash': ['orangecash'], 'crediMax': ['credimax'], 'credimax': ['credimax'], 'nationalbankofkuwaitnbk': ['nbknationalbankofkuwait'], 'dibsy': ['dibsy'], 'skipcash': ['skipcash'], 'telr': ['telr'], 'geidea': ['geidea'], 'hyperpay': ['hyperpay'], 'paytabs': ['paytabs'], 'myfatoorah': ['myfatoorah'], 'fawry': ['fawry'], 'paymob': ['paymob'], 'meeza': ['meeza'], 'vodafonecash': ['vodafonecash'], 'upiautopayrecurringmandates': ['upiautopay'], 'momo': ['momo'], 'napasdomesticcardsdomesticbanklinking': ['napasdomesticcardsandvietqr'], 'vnpaygatewayandvnpayqr': ['vnpayqr'], 'vietqrnapas247': ['napasdomesticcardsandvietqr'], 'duitnowqrandtransfer': ['duitnowqr'], 'fpxonlinebanking': ['fpx'], 'promptpaythaiqr': ['thaiqrpromptpay'], 'truemoneywallet': ['truemoney'], 'midtransgotofinancial': ['midtrans'], 'mayabusinessacquiringandcheckout': ['maya'], 'worldlinenzpaymark': ['worldline'], 'account2accountwindcave': ['windcave'], 'comerciaglobalpaymentscaixabank': ['globalpayments'], 'adyenlocalacquiringjapan': ['adyen'], 'adyenlocalacquiringhongkong': ['adyen'], 'ecpay': ['ecpay'], 'nttdatacafis': ['nttdata'], 'sbpaymentservicesoftbank': ['sbpaymentservice'], 'pagomovilp2c': ['pagomovil'], 'cardsinbolivares': ['cards'], 'careempay': ['careempay'],
}
def status_for(country, name, typ):
    parts = [x.strip() for x in re.split(r' / |, | or ', re.sub(r'\s*\([^)]*\)', '', name)) if x.strip()]
    best = None
    for part in parts + [name]:
        st, hit = _status_for(country, part, typ)
        if st == 'Live': return st, hit
        if st != 'Missing' and best is None: best = (st, hit)
    return best or ('Missing', '')
GENERIC = ['merchantservices', 'paymentservices', 'paymentsolutions', 'paymentgateway', 'payments', 'payment', 'acquiring', 'acquirer', 'gateway', 'services', 'service', 'solutions', 'online', 'localentity', 'bank']
def canon2(k):
    for g in GENERIC: k = k.replace(g, '')
    return k
def _status_for(country, name, typ):
    cov = COV[country]; k = nk(name); low = name.lower()
    if re.match(r'^(visa|mastercard|cards|debit and credit cards|credit and debit cards|international cards|visa and mastercard|visa / mastercard|cards in bol)', low) and not any(w in low for w in ('domestic', 'korean', 'rupay', 'jcb', 'elo', 'interac', 'eftpos', 'mydebit', 'carnet', 'hipercard', 'amex', 'american', 'visanet', 'neonet')):
        return ('Live', 'Cards') if 'Cards' in cov['methods'] else ('Missing', '')
    cands = ALIAS.get(k, [k])
    def hit(pool):
        for p in pool:
            pk = nk(p)
            for cand in cands:
                if cand == pk or canon2(cand) == canon2(pk): return p
        return None
    h = hit(cov['live']) or hit(cov['direct']) or hit(cov['methods'])
    if h: return 'Live', h
    h = hit(cov['xb'])
    if h: return 'Live (cross-border)', h
    h = hit(cov['signed'])
    if h: return 'Signed, not integrated', h
    h = hit(cov['code']) or hit(cov['code_methods'])
    if h: return 'In code, not yet listed', h
    h = hit(cov['hom'])
    if h: return 'Homologating', h
    h = hit(cov['request'])
    if h: return 'On request', h
    if typ == 'Acquirer/PSP':
        h = hit(LIVE_ANYWHERE)
        if h: return f'Live elsewhere, not listed for {country}', h
    return 'Missing', ''

# ---------------- adidas research rows (14 Oct 2026, deep) -> items
ADIDAS = json.load(open(os.path.join(SP, 'adidas_rows_filtered.json')))
CAT_MAP = {'Cross-border PSP': 'Global acquirer (local acquiring)', 'Local acquirer': 'Local acquirer', 'Domestic PSP/gateway': 'Domestic PSP/gateway', 'Acquirer / PSP': 'Domestic PSP/gateway',
           'Wallet': 'Wallet', 'Instant / bank transfer': 'Instant/A2A', 'Cards': 'Cards', 'Local card scheme': 'Local card scheme', 'Other': 'Other'}
def adidas_rating(r):
    base = 8 if r['relevance'] == 'High' else 5
    if r.get('score'): base = max(3, min(9, round(r['score'] / 10)))
    cat = r['category']
    if cat == 'Cards': base = 10
    if cat == 'Cross-border PSP': base = min(base, 6)
    if cat == 'Local card scheme': base = min(base, 6)
    if cat == 'Other': base = min(base, 5)
    return base
ITEMS = {}   # (country, nk(name)) -> item
def put(country, name, typ, cat, rating, why, source, origin, prio):
    if name in DROP and prio < 3: return
    k = (country, nk(name))
    cur = ITEMS.get(k)
    if cur and cur['prio'] >= prio:   # keep the higher-priority source, but fill gaps
        if not cur['source'] and source: cur['source'] = source
        return
    ITEMS[k] = dict(country=country, name=name, type=typ, category=cat, rating=int(rating), why=(why or '')[:300], source=source or '', origin=origin, prio=prio)
DROP = {'BCA / Mandiri acquiring', 'Maybank / CIMB acquiring', 'KBank / SCB / Bangkok Bank / Krungsri acquiring', 'Bank mobile apps (K PLUS, SCB Easy, Krungthai NEXT, Krungsri App)', 'DBS / UOB / OCBC merchant acquiring', 'Orange Money / Zain Cash (JoMoPay wallets)', 'K PLUS (KBank mobile banking)', 'Prepaid wallets (Paytm Wallet, Mobikwik, Ola Money, Amazon Pay)', 'Account2Account (bank transfer)', 'NETS / eNETS', 'Razer Merchant Services', 'Bank acquirers (CTBC, Cathay United, E.Sun, Taishin)', 'NewebPay / TapPay (gateways)', 'Global acquirers for Hong Kong (Adyen, Stripe, Checkout.com, Worldpay, Cybersource, Global Payments)', 'PayMe (HSBC)', 'Pago Móvil (interbank mobile transfer)', 'Local acquiring in bolívares (Mercantil, Banesco, Credicard switch)', 'Zelle (USD)', 'Stablecoins (USDT via Binance Pay)', 'Toss Payments (PG)', 'Barclaycard (acquirer)', 'Pay by Bank (open banking)', 'CommBank / NAB / Westpac acquiring', 'J.P. Morgan (Chase) acquiring', 'Wallets (Paytm, PhonePe, Amazon Pay)', 'CaixaBank / Comercia Global Payments', 'Magnati (FAB acquiring)', 'Aani (instant payments)', 'Jaywan (domestic card scheme)', 'CliQ (instant payments)', 'Thai QR (PromptPay)', 'Interac (Debit online, e-Transfer)', 'Klarna (incl. Sofort)', 'RuPay (domestic scheme, credit on UPI)', 'Opn (Omise)', 'Windcave', 'Fat Zebra'}
for r in ADIDAS:
    if 'Not applicable' in r['action'] or 'cash on delivery' in r['name'].lower(): continue
    put(r['country'], r['name'], r['type'], CAT_MAP.get(r['category'], r['category']), adidas_rating(r), r['why'], r['source'], 'adidas research 14 Oct 2026', 1)

# ---------------- manual rows (today's searches + known facts), prio 2
S = dict(
 citcon='https://www.citcon.com/blog-posts/japan-digital-payments-2026-what-merchants-need-to-know', payroute='https://pay-route.co.jp/article/2026/03/16/uber-eats-d-payment-usage-and-best-payment-methods-explained/',
 ubereats_paypay='https://www.uber.com/ja-JP/newsroom/uber-eats-paypay', antom_jp='https://knowledge.antom.com/paypay', kapron='https://www.kapronasia.com/asia-payments-research-category/taiwan-has-nearly-10-million-mobile-payment-users.html',
 antom_hk='https://www.antom.com/markets/hong-kong', ftn_hk='https://fintechnews.hk/top-e-wallets-hong-kong-2025/', kpay='https://go.kpay-group.com/blog/payment-methods',
 hyperswitch_de='https://hyperswitch.io/blog/popular-payment-methods-in-germany', unzer_de='https://www.unzer.com/en/knowledge/articles/preferred-payment-methods-germany-2026/', zunapro='https://www.zunapro.com/germany/de/blog/digitale-zahlungsloesungen-deutschland',
 paynopain='https://paynopain.com/en/blog/payment-methods-spain-2025-consumer-trends-and-habits/', cbm_es='https://cross-border-magazine.com/e-commerce-payment-landscape-in-spain-2025/', stripe_es='https://stripe.com/ie/resources/more/payment-methods-in-spain',
 ncfa='https://ncfacanada.org/how-canadians-pay-online-in-2026-interac-digital-wallets-and-open-banking/', interac_pr='https://www.interac.ca/en/format/press-release/page/2/', paramount='https://www.paramountcommerce.com/resources/blog/the-rise-of-pay-by-bank-in-canadian-ecommerce-2026-guide',
 tazapay_au='https://tazapay.com/blog/local-payment-methods-in-australia', volt_au='https://www.volt.io/content-hub/understanding-the-australian-payments-landscape/', stripe_oce='https://stripe.com/at/resources/more/payments-in-oceania',
 shuttle_nz='https://www.shuttleglobal.com/blog/the-most-popular-payment-methods-in-new-zealand', retailtimes='https://retailtimes.co.uk/how-britain-pays-online-in-2026-cards-wallets-and-open-banking-in-one-table/',
 obie='https://www.openbanking.org.uk/insights/pay-by-bank-a-big-step-forward-for-everyday-payment/', techcrunch_in='https://techcrunch.com/2025/01/09/india-rupay-upi-payment-push-is-cutting-out-visa-and-mastercard/',
 egstreets='https://egyptianstreets.com/?p=85499', mef_eg='https://mobileecosystemforum.com/egypts-digital-payment-revolution/', mordor_eg='https://www.mordorintelligence.ar/industry-reports/egypt-mobile-payment-market',
 meatech_jo='https://meatechwatch.com/2025/10/15/jordan-efawateercom-payment-transactions-reach-16-3-billion-in-2025/', orange_jo='https://orange.jo/en/help-center/orange-money', zain_jo='https://apps.apple.com/us/app/-/id1472544421',
 wise_ve='https://wise.com/gb/hub/payment-methods/venezuela', cripto_pm='https://criptonoticias.com/comunidad/adopcion/pagomovil-63-operaciones-venezuela-compite-usdt', cripto_usdt='https://criptonoticias.com/comunidad/adopcion/binance-viable-alternativa-zelle-venezuela',
 ntn24='https://www.ntn24.com/noticias-economia/pago-mixto-el-fenomeno-unico-en-venezuela-que-ralentiza-el-proceso-de-pago-407874', amazon_ps='https://paymentservices.amazon.com/docs/payment-methods/payment-methods-support',
 tap='https://learnwithhasan.com/payment-gateways/tap-payments/', careem='https://www.paisabazaar.ae/bank-accounts/articles/careem-pay/', careem26='https://www.solcard.cc/ru/blog/pay-careem-with-crypto',
 waymo_help='https://support.google.com/waymo/answer/14160746', gkomunika='https://gkomunika.com/id/pages/panduan-lengkap-transaksi-di-thailand-cara-menggunakan-qris-rabbit-line-pay-dan-uang-tunai',
 tazapay_sea='https://tazapay.com/blog/local-payment-methods-ewallets-in-southeast-asia', hitpay='https://docs.hitpayapp.com/changelog/promptpay-online-and-qris-cross-border',
 yuno_code='Yuno integration code scan and repo inventory (internal, Oct 2026)', yuno_dir='y.uno/integrations (export 14 Oct 2026)', apple='https://support.apple.com/en-us/102775',
)
MANUAL = [
 # Japan
 ('Japan','PayPay','Payment method','Wallet',9,'About 65% of QR payment volume in Japan; Uber Eats has accepted PayPay since May 2020. Live via Adyen, Antom, NTT DATA.',S['citcon']),
 ('Japan','JCB (domestic card scheme)','Payment method','Local card scheme',7,'Japan-issued scheme; cards are 59% of online value. Not listed as a scheme on y.uno/integrations; confirm JCB on the Japan acquirers (GMO, SB Payment, Sony in code).',S['antom_jp']),
 ('Japan','GMO Payment Gateway','Acquirer/PSP','Domestic PSP/gateway',8,'Largest domestic payment gateway; integration repo exists (gmo-pg-int, Jul 2026) but not live or listed.',S['yuno_code']),
 ('Japan','SB Payment Service','Acquirer/PSP','Domestic PSP/gateway',6,'SoftBank group PSP; repo softbank-int (Sep 2026), not live or listed.',S['yuno_code']),
 ('Japan','Sony Payment Services','Acquirer/PSP','Domestic PSP/gateway',6,'Sony group PSP; repo sony-int (Jul 2026), not live or listed.',S['yuno_code']),
 ('Japan','Rakuten Pay','Payment method','Wallet',6,'Accepted by Uber Eats alongside PayPay (2026 guide); not carried by any live provider in Japan.',S['payroute']),
 ('Japan','d払い (docomo)','Payment method','Wallet',4,'Carrier wallet; Uber Eats did not offer it as of March 2026; not in Yuno.',S['payroute']),
 ('Japan','au PAY','Payment method','Wallet',4,'Carrier wallet; not usable directly on Uber Eats (2026 guide); not in Yuno.',S['payroute']),
 ('Japan','Merpay','Payment method','Wallet',4,'Mercari wallet; no public share figure; not in Yuno.',S['citcon']),
 ('Japan','Apple Pay','Payment method','Wallet',8,'Available in Japan (Apple); live via Adyen, Fiserv, Rapyd, Worldpay.',S['apple']),
 ('Japan','Google Pay','Payment method','Wallet',7,'Live via Adyen, Fiserv, Rapyd.',S['yuno_dir']),
 # Singapore
 ('Singapore','PayNow','Payment method','Instant/A2A',8,'National instant rail on every bank app; in code only (AllinPay repo), no live provider carries it.',S['yuno_code']),
 ('Singapore','GrabPay','Payment method','Wallet',8,'Grab is the ride-hailing leader; GrabPay live via Adyen.',S['yuno_dir']),
 ('Singapore','Apple Pay','Payment method','Wallet',8,'Live via Adyen, Airwallex, Fiserv, Rapyd, Worldpay.',S['apple']),
 # Australia
 ('Australia','eftpos (domestic debit)','Payment method','Local card scheme',5,'Domestic debit scheme; online eftpos routes through local acquirers (Windcave, Fat Zebra are in code). Not listed as a scheme.',S['tazapay_au']),
 ('Australia','PayTo (NPP account-to-account)','Payment method','Instant/A2A',5,'A2A is about 4% of online transactions and growing with PayTo (Volt); not in Yuno.',S['volt_au']),
 ('Australia','CommBank / NAB / Westpac acquiring','Acquirer/PSP','Local acquirer',5,'Big-4 bank acquiring; Worldline (ANZ Worldline JV) is live, the other three are not connected. No public share figure.',S['stripe_oce']),
 ('Australia','Windcave','Acquirer/PSP','Domestic PSP/gateway',6,'Major AU/NZ gateway; repo windcave-int (Oct 2026), not live or listed.',S['yuno_code']),
 ('Australia','Fat Zebra','Acquirer/PSP','Domestic PSP/gateway',5,'Australian gateway (cards, BECS); repo fatzebra-int (Jul 2026), not live or listed.',S['yuno_code']),
 ('Australia','Apple Pay','Payment method','Wallet',8,'Live via Adyen, Airwallex, Fiserv, Rapyd, Worldpay.',S['apple']),
 ('Australia','PayPal','Payment method','Wallet',7,'Live via Braintree, Ecommpay, Pockyt, Stripe.',S['yuno_dir']),
 # Thailand
 ('Thailand','Rabbit LINE Pay','Payment method','Wallet',7,'Top-3 Thai wallet with TrueMoney and ShopeePay; not carried by any live provider.',S['gkomunika']),
 ('Thailand','Thai QR (PromptPay)','Payment method','Instant/A2A',9,'National real-time rail, the most used payment method in Thailand; live via dLocal, Xendit.',S['hitpay']),
 ('Thailand','TrueMoney','Payment method','Wallet',8,'Leading Thai wallet; live via dLocal, Xendit.',S['tazapay_sea']),
 ('Thailand','Apple Pay','Payment method','Wallet',1,'Not offered in Thailand by Apple (country list, 22 Oct 2026); not a gap.',S['apple']),
 ('Thailand','Opn (Omise)','Acquirer/PSP','Domestic PSP/gateway',6,'Thai gateway (Omise name again since 2025); repo opn-int (Jul 2026), not live or listed.',S['yuno_code']),
 # Indonesia
 ('Indonesia','GoPay','Payment method','Wallet',9,'Gojek wallet, ride-hailing native; signed with partners, not integrated (also appears via Boku).',S['yuno_dir']),
 ('Indonesia','QRIS','Payment method','Instant/A2A',10,'National QR standard accepted by every local wallet and bank; live via dLocal, Ecommpay, Xendit.',S['hitpay']),
 ('Indonesia','OVO','Payment method','Wallet',8,'Grab-aligned wallet; live via Adyen, dLocal, Xendit.',S['tazapay_sea']),
 ('Indonesia','Apple Pay','Payment method','Wallet',1,'Not offered in Indonesia by Apple (country list, 22 Oct 2026); not a gap.',S['apple']),
 # South Korea
 ('South Korea','NHN KCP (domestic PG)','Acquirer/PSP','Domestic PSP/gateway',9,'A Korean PG is the route to domestic-only Korean cards and bank transfer; repo kcp-int (Oct 2026), not live or listed.',S['yuno_code']),
 ('South Korea','KG Inicis','Acquirer/PSP','Domestic PSP/gateway',6,'One of the main Korean PGs; not in Yuno. No public share figure.',''),
 ('South Korea','Toss Payments (PG)','Acquirer/PSP','Domestic PSP/gateway',6,'Toss group PG; not in Yuno. No public share figure.',''),
 ('South Korea','Kakao Pay','Payment method','Wallet',9,'Leading Korean wallet; live via Adyen, Antom (and KCP in code).',S['yuno_dir']),
 ('South Korea','Naver Pay','Payment method','Wallet',8,'Second wallet; live via Adyen, Antom (Payssion in code).',S['yuno_dir']),
 ('South Korea','Samsung Pay','Payment method','Wallet',6,'In code only (Payssion), no live provider lists it for Korea.',S['yuno_code']),
 ('South Korea','Toss Pay','Payment method','Wallet',6,'Live via Antom.',S['yuno_dir']),
 # Taiwan
 ('Taiwan','LINE Pay','Payment method','Wallet',8,'Top Taiwanese wallet (25% of mobile-payment users in the FSC survey cited by Focus Taiwan); not in Yuno.',S['kapron']),
 ('Taiwan','JKOPAY','Payment method','Wallet',7,'Home-grown wallet, third by users (10.9%); not in Yuno.',S['kapron']),
 ('Taiwan','Taiwan Pay','Payment method','Wallet',4,'Bank-consortium wallet; no public share figure; not in Yuno.',S['kapron']),
 ('Taiwan','NewebPay / TapPay (gateways)','Acquirer/PSP','Domestic PSP/gateway',5,'Second-tier Taiwanese gateways behind ECPay (live); not in Yuno. No public share figure.',''),
 ('Taiwan','Bank acquirers (CTBC, Cathay United, E.Sun, Taishin)','Acquirer/PSP','Local acquirer',5,'Largest card acquirers in Taiwan; reachable today only through ECPay and the global acquirers; no direct connection.',''),
 ('Taiwan','Apple Pay','Payment method','Wallet',8,'Second wallet by users (17.9%); live via Fiserv, Rapyd, Worldpay.',S['kapron']),
 # Hong Kong
 ('Hong Kong','Global acquirers for Hong Kong (Adyen, Stripe, Checkout.com, Worldpay, Cybersource, Global Payments)','Acquirer/PSP','Global acquirer (local acquiring)',9,'Only Unlimit is listed for Hong Kong on y.uno/integrations; the global acquirers are live in neighbouring markets but not listed here. Listing gap to confirm.',S['yuno_dir']),
 ('Hong Kong','AlipayHK','Payment method','Wallet',8,'Wallets are 41% of HK e-commerce (Antom 2025); AlipayHK accepted at 150,000+ outlets; not in Yuno for HK.',S['antom_hk']),
 ('Hong Kong','PayMe (HSBC)','Payment method','Wallet',7,'HSBC wallet, one of the top HK e-wallets (Fintech News, Jan 2026); not in Yuno.',S['ftn_hk']),
 ('Hong Kong','FPS (Faster Payment System)','Payment method','Instant/A2A',6,'19% of HK e-commerce via FPS bank transfer (Antom 2025); no chargeback protection; not in Yuno.',S['antom_hk']),
 ('Hong Kong','WeChat Pay HK','Payment method','Wallet',6,'Top HK e-wallet (Fintech News); not listed for Hong Kong.',S['ftn_hk']),
 ('Hong Kong','Octopus','Payment method','Wallet',6,'Octopus wallet and card, universal for transport; not in Yuno.',S['ftn_hk']),
 ('Hong Kong','Google Pay','Payment method','Wallet',6,'Not listed for Hong Kong on y.uno/integrations (listing to confirm).',S['yuno_dir']),
 ('Hong Kong','Apple Pay','Payment method','Wallet',8,'22% of users choose Apple Pay (survey cited by Antom); live via Unlimit.',S['antom_hk']),
 # Malaysia / Philippines / Vietnam extras
 ('Malaysia','DuitNow QR','Payment method','Instant/A2A',8,'National QR standard; signed with partners, not integrated.',S['yuno_dir']),
 ('Malaysia',"Touch 'n Go eWallet",'Payment method','Wallet',8,'Largest Malaysian wallet; live via Boku, dLocal, Xendit.',S['tazapay_sea']),
 ('Malaysia','FPX','Payment method','Instant/A2A',8,'Online banking rail; live via dLocal, Xendit.',S['yuno_dir']),
 ('Philippines','GCash','Payment method','Wallet',10,'Dominant Philippine wallet; live via six providers.',S['tazapay_sea']),
 ('Philippines','Maya','Payment method','Wallet',8,'Second wallet; live as provider and method.',S['yuno_dir']),
 ('Vietnam','ZaloPay','Payment method','Wallet',8,'Grab Vietnam wallet partner with MoMo; signed, not integrated.',S['yuno_dir']),
 ('Vietnam','MoMo','Payment method','Wallet',9,'Largest Vietnamese wallet; live via Adyen, Antom, Ecommpay.',S['tazapay_sea']),
 # India
 ('India','UPI','Payment method','Instant/A2A',10,'About 71% of transactions nationwide (Bernstein via TechCrunch); live via Adyen, dLocal, EBANX, PayU, plus Razorpay and BillDesk live.',S['techcrunch_in']),
 ('India','UPI Autopay','Payment method','Instant/A2A',8,'Recurring mandate for card-on-file style billing; live via Adyen, EBANX.',S['yuno_dir']),
 ('India','RuPay (domestic scheme, credit on UPI)','Payment method','Local card scheme',6,'Only network allowed for credit cards on UPI; 28% of credit-card transactions (TechCrunch). Not listed as a scheme; processed by the live Indian acquirers.',S['techcrunch_in']),
 ('India','Net banking','Payment method','Instant/A2A',4,'Classic Indian checkout option; not listed as a method in Yuno.',''),
 ('India','Wallets (Paytm, PhonePe, Amazon Pay)','Payment method','Wallet',5,'Wallet balances outside UPI; not listed; UPI intent covers the apps themselves.',''),
 ('India','CCAvenue','Acquirer/PSP','Domestic PSP/gateway',5,'Indian gateway in code only (integrations-x), not live.',S['yuno_code']),
 # New Zealand
 ('New Zealand','Windcave','Acquirer/PSP','Domestic PSP/gateway',7,'Main NZ gateway; repo windcave-int (Oct 2026), not live or listed.',S['yuno_code']),
 ('New Zealand','Account2Account (bank transfer)','Payment method','Instant/A2A',4,'NZ online bank transfer option; no public share figure; not in Yuno.',S['shuttle_nz']),
 ('New Zealand','POLi','Payment method','Instant/A2A',1,'Closed 30 September 2023 (Tazapay); not a gap.',S['tazapay_au']),
 ('New Zealand','Apple Pay','Payment method','Wallet',8,'Live via Adyen, Fiserv, Worldpay.',S['apple']),
 ('New Zealand','PayPal','Payment method','Wallet',6,'Live via Braintree, Ecommpay, Pockyt, Stripe (added after the PayPal listing fix).',S['yuno_dir']),
 # UK
 ('United Kingdom','Pay by Bank (open banking)','Payment method','Instant/A2A',5,'About 6% of UK online spend; launched on Amazon and eBay; live via Volt, Trustly.',S['retailtimes']),
 ('United Kingdom','Barclaycard (acquirer)','Acquirer/PSP','Local acquirer',5,'Large UK acquirer; not in Yuno. No public share figure.',''),
 ('United Kingdom','Apple Pay','Payment method','Wallet',9,'Wallets are 40% of UK online spend (2025); live via Adyen, Airwallex, Fiserv, Rapyd, Worldpay.',S['retailtimes']),
 ('United Kingdom','Google Pay','Payment method','Wallet',8,'Live via Adyen, Airwallex, Fiserv, Rapyd.',S['retailtimes']),
 ('United Kingdom','PayPal','Payment method','Wallet',7,'Default wallet for a meaningful slice of UK e-commerce; live via Braintree, Ecommpay, Pockyt, Stripe.',S['retailtimes']),
 ('United Kingdom','Worldpay','Acquirer/PSP','Local acquirer',8,'Largest UK acquirer; live.',S['yuno_dir']),
 # Germany
 ('Germany','PayPal','Payment method','Wallet',9,'About 28% of German e-commerce transactions (HDE via Hyperswitch); carried by Braintree, Ecommpay, Pockyt, Stripe. The y.uno PayPal page omitted Germany; corrected in the rebuilt deck.',S['hyperswitch_de']),
 ('Germany','SEPA Direct Debit','Payment method','Instant/A2A',7,'About 17% of e-commerce; live via Adyen, Checkout.com, Stripe, Worldline.',S['hyperswitch_de']),
 ('Germany','Klarna (incl. Sofort)','Payment method','Wallet',5,'Sofort is now Klarna Pay Now; carried by Adyen, Nuvei, Stripe. The y.uno Klarna page omitted Germany; corrected.',S['zunapro']),
 ('Germany','Wero (EPI)','Payment method','Instant/A2A',5,'Bank-backed wallet replacing giropay; e-commerce rollout 2025-2026; not in Yuno.',S['zunapro']),
 ('Germany','girocard / giropay','Payment method','Local card scheme',1,'giropay was discontinued in 2024 and girocard has no e-commerce rail; not a gap.',S['hyperswitch_de']),
 ('Germany','Nexi / Concardis','Acquirer/PSP','Local acquirer',5,'Large German acquirer; not in Yuno. No public share figure.',''),
 ('Germany','Payone','Acquirer/PSP','Local acquirer',5,'Worldline and Sparkassen JV, large German acquirer; not in Yuno directly (Worldline is live). No public share figure.',''),
 ('Germany','Apple Pay','Payment method','Wallet',8,'Live via Adyen, Airwallex, Fiserv, Rapyd, Worldpay.',S['apple']),
 # Spain
 ('Spain','Bizum','Payment method','Instant/A2A',8,'26 to 27 million users; 58,000+ e-commerce stores accept it (2024); not in Yuno (Redsys in code lists cards, Apple Pay, Google Pay only).',S['paynopain']),
 ('Spain','Redsys','Acquirer/PSP','Domestic PSP/gateway',8,'The Spanish banks\' acquiring gateway; repo integrations-x/providers/redsys, not live or listed.',S['yuno_code']),
 ('Spain','CaixaBank / Comercia Global Payments','Acquirer/PSP','Local acquirer',5,'Largest Spanish acquirer (Global Payments JV); Global Payments is live, the Spanish entity is not confirmed.',''),
 ('Spain','Apple Pay','Payment method','Wallet',8,'Wallets are 26 to 29% of Spanish online payments; live via Adyen, Airwallex, Fiserv, Rapyd, Worldpay.',S['stripe_es']),
 ('Spain','BBVA','Acquirer/PSP','Local acquirer',7,'Spanish bank acquirer; live.',S['yuno_dir']),
 ('Spain','Getnet (Santander)','Acquirer/PSP','Local acquirer',7,'Santander acquirer; live.',S['yuno_dir']),
 # Canada
 ('Canada','Interac (Debit online, e-Transfer)','Payment method','Instant/A2A',7,'7 billion Interac Debit and 1.6 billion e-Transfer transactions in FY2025; 58% of Canadians rate e-Transfer secure vs 41% PayPal. Catalog code exists, no provider carries it.',S['ncfa']),
 ('Canada','Moneris','Acquirer/PSP','Local acquirer',7,'Largest Canadian acquirer (RBC and BMO); repo moneris-int (Oct 2026), not live or listed.',S['yuno_code']),
 ('Canada','J.P. Morgan (Chase) acquiring','Acquirer/PSP','Local acquirer',5,'Repo orbital-int (Oct 2026), not live or listed.',S['yuno_code']),
 ('Canada','Desjardins (Quebec)','Acquirer/PSP','Local acquirer',3,'Quebec cooperative acquirer; not in Yuno. No public share figure.',''),
 ('Canada','Apple Pay','Payment method','Wallet',8,'Adoption growing (Stripe); live via Adyen, Airwallex, Fiserv, Worldpay.',S['ncfa']),
 ('Canada','Global Payments','Acquirer/PSP','Local acquirer',7,'Live.',S['yuno_dir']),
 ('Canada','Elavon','Acquirer/PSP','Local acquirer',6,'Live.',S['yuno_dir']),
 # Venezuela
 ('Venezuela','Pago Móvil (interbank mobile transfer)','Payment method','Instant/A2A',9,'The everyday bolívar rail: about 63% of operations (CriptoNoticias); accepted by local ride-hailing apps; not in Yuno.',S['cripto_pm']),
 ('Venezuela','Local acquiring in bolívares (Mercantil, Banesco, Credicard switch)','Acquirer/PSP','Local acquirer',8,'BBVA Provincial is live; Mercantil and Banesco, the other large acquiring banks, are not connected.',S['wise_ve']),
 ('Venezuela','Zelle (USD)','Payment method','Other',3,'Very popular for USD payments but a P2P rail, not a merchant checkout integration; US banks restricting Venezuelan use.',S['wise_ve']),
 ('Venezuela','Stablecoins (USDT via Binance Pay)','Payment method','Other',4,'Merchants adding USDT acceptance; Triple-A (crypto PSP) is live for Yuno in the Gulf, not listed for Venezuela.',S['cripto_usdt']),
 ('Venezuela','PayPal','Payment method','Wallet',4,'Carried by Ecommpay, Pockyt (after the PayPal listing fix).',S['yuno_dir']),
 # Saudi Arabia
 ('Saudi Arabia','mada','Payment method','Local card scheme',10,'National debit scheme; live (mada and the Saudi banks).',S['amazon_ps']),
 ('Saudi Arabia','STC Pay','Payment method','Wallet',8,'Largest Saudi wallet; live.',S['amazon_ps']),
 ('Saudi Arabia','Apple Pay','Payment method','Wallet',9,'Careem accepts cards, Apple Pay and Careem Pay (2026); live via Fiserv.',S['careem26']),
 ('Saudi Arabia','urpay','Payment method','Wallet',4,'Al Rajhi wallet; no public share figure; not in Yuno.',''),
 ('Saudi Arabia','Samsung Pay','Payment method','Wallet',4,'Available in Saudi Arabia; not listed for Saudi Arabia on y.uno/integrations.',S['tap']),
 # UAE
 ('United Arab Emirates','Apple Pay','Payment method','Wallet',9,'Careem: cards, Apple Pay, Careem Pay; live via Adyen, Fiserv.',S['careem26']),
 ('United Arab Emirates','Careem Pay','Payment method','Wallet',7,'Ride-hailing native wallet; live (direct).',S['careem']),
 ('United Arab Emirates','Aani (instant payments)','Payment method','Instant/A2A',5,'CBUAE instant payment platform (Al Etihad Payments); early merchant adoption; not in Yuno.',''),
 ('United Arab Emirates','Jaywan (domestic card scheme)','Payment method','Local card scheme',5,'New UAE domestic scheme rolling out on debit cards; not listed as a scheme.',''),
 ('United Arab Emirates','Magnati (FAB acquiring)','Acquirer/PSP','Local acquirer',6,'FAB\'s acquiring arm; not in Yuno. No public share figure.',''),
 ('United Arab Emirates','Network International','Acquirer/PSP','Local acquirer',8,'Largest regional acquirer; live.',S['yuno_dir']),
 # Qatar / Kuwait / Oman / Bahrain
 ('Qatar','NAPS / QPay','Payment method','Local card scheme',9,'Qatar national debit scheme; live (direct).',S['tap']),
 ('Qatar','Ooredoo Money','Payment method','Wallet',4,'Telecom wallet; no public share figure; not in Yuno.',''),
 ('Qatar','Samsung Pay','Payment method','Wallet',3,'Not listed for Qatar.',S['tap']),
 ('Kuwait','KNET','Payment method','Local card scheme',10,'Kuwait national debit switch; live (KNET, KFast).',S['tap']),
 ('Kuwait','Apple Pay','Payment method','Wallet',8,'Live via Adyen.',S['apple']),
 ('Oman','OmanNet','Payment method','Local card scheme',9,'Oman national debit switch; live (direct).',S['tap']),
 ('Oman','Samsung Pay','Payment method','Wallet',3,'Not listed for Oman.',S['tap']),
 ('Bahrain','Benefit / BenefitPay','Payment method','Local card scheme',9,'Bahrain national switch and wallet; Benefit live as provider.',S['amazon_ps']),
 ('Bahrain','Google Pay','Payment method','Wallet',5,'Not listed for Bahrain on y.uno/integrations.',S['yuno_dir']),
 # Jordan
 ('Jordan','CliQ (instant payments)','Payment method','Instant/A2A',7,'JoPACC instant rail: value up 73% YoY to JD14.5 billion through Sep 2025; not in Yuno.',S['meatech_jo']),
 ('Jordan','Orange Money','Payment method','Wallet',5,'Telecom wallet with merchant and QR payments; not in Yuno.',S['orange_jo']),
 ('Jordan','Zain Cash','Payment method','Wallet',5,'CBJ-regulated wallet with online shopping and QR; not in Yuno.',S['zain_jo']),
 ('Jordan','Google Pay','Payment method','Wallet',5,'Not listed for Jordan on y.uno/integrations.',S['yuno_dir']),
 ('Jordan','Careem Pay','Payment method','Wallet',4,'Careem Pay operates in Jordan (consumer guide); listed only for the UAE in Yuno.',S['careem']),
 # Egypt
 ('Egypt','InstaPay','Payment method','Instant/A2A',8,'CBE-licensed instant payment app, fee-free transfers, fastest-growing rail; not in Yuno.',S['egstreets']),
 ('Egypt','Fawry','Acquirer/PSP','Domestic PSP/gateway',9,'Most popular digital payment service, 35 million+ users, Uber partner since 2021; live.',S['egstreets']),
 ('Egypt','Vodafone Cash','Payment method','Wallet',9,'About 78% of mobile-wallet transaction volume; live (direct).',S['mef_eg']),
 ('Egypt','Meeza','Payment method','Local card scheme',7,'43.5 million national cards (Jun 2025); live (direct).',S['mordor_eg']),
 ('Egypt','Google Pay','Payment method','Wallet',5,'Not listed for Egypt on y.uno/integrations.',S['yuno_dir']),
 ('Egypt','Apple Pay','Payment method','Wallet',7,'Live via Fiserv.',S['apple']),
 # LatAm extras not in the adidas gap rows
 ('Brazil','Elo (local card scheme)','Payment method','Local card scheme',6,'Main Brazilian domestic scheme; not listed as a scheme; processed by the live local acquirers (Cielo, Rede, Getnet, Stone, PagSeguro).',S['yuno_dir']),
 ('Brazil','PIX','Payment method','Instant/A2A',10,'Live via 27 providers.',S['yuno_dir']),
 ('Dominican Republic','Cardnet','Acquirer/PSP','Local acquirer',7,'Second Dominican acquirer; homologating.',S['yuno_dir']),
 ('Paraguay','QR Bancard (interoperable QR)','Payment method','Instant/A2A',7,'Bancard is live for cards; its QR (180 million transactions in 2025) is not listed as a method.','https://www.bancard.com.py'),
 ('Panama','Yappy','Payment method','Wallet',8,'Banco General wallet, the everyday Panamanian payment app; live (direct).',S['yuno_dir']),
 ('Peru','Plin','Payment method','Wallet',8,'Interbank, BBVA and Scotiabank wallet interoperable with Yape; live via Niubiz.',S['yuno_dir']),
 ('Peru','Yape','Payment method','Wallet',9,'BCP wallet, the largest in Peru; live via Bamboo, dLocal, Monnet, Niubiz.',S['yuno_dir']),
 ('Bolivia','QR BCB (interoperable QR)','Payment method','Instant/A2A',6,'Bolivian interoperable QR; not listed (PagosNet homologating).',''),
 ('Mexico','Clip','Acquirer/PSP','Domestic PSP/gateway',6,'Aggregator with 2 million+ merchants; not in Yuno.','https://www.mordorintelligence.com'),
]
for c, n, t, cat, r, why, src in MANUAL: put(c, n, t, cat, r, why, src, 'manual (searches 22 Oct 2026)', 2)
# American Express, one row per market where it matters
for c in ['United Kingdom','Germany','Spain','Canada','Australia','New Zealand','Japan','Singapore','Hong Kong','United Arab Emirates','Saudi Arabia','Israel','Mexico','Brazil','Argentina']:
    put(c, 'American Express', 'Payment method', 'Cards', 6, 'Waymo accepts Amex in the US; Amex is not listed as a scheme on y.uno/integrations. Acceptance runs through the global acquirers\' Amex agreements; confirm per market.', S['waymo_help'], 'manual', 2)
# ---------------- agent research (prio 3, rating overrides only when sourced)
for f in sorted(glob.glob(os.path.join(SP, 'research_*.json'))):
    try: data = json.load(open(f))
    except Exception as e: print('bad json', f, e); continue
    for r in data:
        if r.get('country') not in REGION: continue
        src = r.get('source') or ''
        if r['name'] in DROP: continue
        if any(w in (r.get('why') or '').lower() for w in ("not on apple's supported", 'not in google', 'not in the samsung pay availability', 'not offered in yuno')) and r.get('rating', 5) <= 2: continue
        put(r['country'], r['name'], r.get('type', 'Payment method'), r.get('category', 'Other'), r.get('rating', 5), r.get('why', ''), src, 'agent research 22 Oct 2026', 3 if src.startswith('http') else 0)
OVERRIDES = json.load(open(os.path.join(SP, 'overrides.json'))) if os.path.exists(os.path.join(SP, 'overrides.json')) else {}
for k, v in OVERRIDES.items():
    c, n = k.split('|'); kk = (c, nk(n))
    if kk in ITEMS: ITEMS[kk]['rating'] = v
# ---------------- status + outputs
out = []
for (c, _), it in ITEMS.items():
    st, hit = status_for(c, it['name'], it['type'])
    it['status'] = st; it['matched'] = hit; it['region'] = REGION[c]; out.append(it)
ded = {}
for it in out:
    key = (it['country'], it['type'], it['matched'] or 'canon:' + canon(it['name']))
    cur = ded.get(key)
    if cur is None or (it['prio'], it['rating']) > (cur['prio'], cur['rating']):
        if cur is not None and not it['source'] and cur['source']: it['source'] = cur['source']
        ded[key] = it
out = list(ded.values())
out = [it for it in out if 'not a gap' not in it['why'].lower() and not (it['rating'] <= 1)]
OVR = {('Venezuela', 'zelle'): 5, ('Germany', 'klarnasofortpaynow'): 4}
for it in out:
    if (it['country'], nk(it['name'])) in OVR: it['rating'] = OVR[(it['country'], nk(it['name']))]
RORDER = {'Asia Pacific': 0, 'Europe and North America': 1, 'Latin America': 2, 'Middle East': 3}
out.sort(key=lambda x: (RORDER[x['region']], ORDER.index(x['country']), -x['rating'], x['name'].lower()))
COLS = ['Country', 'Connection', 'Rating (1-10)', 'Type', 'Category', 'Status in Yuno', 'Matched Yuno entry', 'Why it matters for a ride-hailing app', 'Source', 'Research origin']
def row(it): return [it['country'], it['name'], it['rating'], it['type'], it['category'], it['status'], it['matched'], it['why'], it['source'], it['origin']]
missing = [it for it in out if it['status'] != 'Live']
with open(os.path.join(OUT, 'full_ranking.csv'), 'w', newline='') as f: w = csv.writer(f); w.writerow(COLS); [w.writerow(row(it)) for it in out]
with open(os.path.join(OUT, 'missing.csv'), 'w', newline='') as f: w = csv.writer(f); w.writerow(COLS); [w.writerow(row(it)) for it in missing]
summ = []
for c in ORDER:
    items = [it for it in out if it['country'] == c]; miss = [it for it in missing if it['country'] == c]
    top = '; '.join(f"{it['name']} ({it['rating']}, {it['status']})" for it in sorted(miss, key=lambda x: -x['rating'])[:6])
    summ.append([c, REGION[c], len(COV[c]['live']), len(items), len(miss), sum(1 for it in miss if it['rating'] >= 8), sum(1 for it in miss if 5 <= it['rating'] < 8), top])
with open(os.path.join(OUT, 'by_market.csv'), 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['Country', 'Region', 'Providers live in Yuno', 'Connections ranked', 'Not live in Yuno', 'Must-haves missing (8-10)', 'Important missing (5-7)', 'Top gaps (rating, status)']); [w.writerow(s) for s in summ]
json.dump(out, open(os.path.join(OUT, 'items.json'), 'w'), ensure_ascii=False, indent=0)
print('items', len(out), 'missing', len(missing)); print(collections.Counter(it['status'] for it in out))
for s in summ: print(f"{s[0]:<22} live={s[2]:<3} ranked={s[3]:<3} notlive={s[4]:<3} must={s[5]} imp={s[6]} | {s[7][:150]}")
