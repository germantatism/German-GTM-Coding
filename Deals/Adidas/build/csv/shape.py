"""Shape adidas_payment_connections_live.csv (Payments Concierge, #partnerships--sales, 14 Oct 2026) into a per-country view.
The matrix country = country of the payment (cross-border included), so local methods are kept only in their home country
and global methods listed under a provider (iDEAL, SEPA, Cash App...) are dropped outside their market."""
import csv, json, sys, collections
SRC = sys.argv[1]; OUT = sys.argv[2]
NATIVE = {  # method -> (label, home countries)
 'PAGO_FACIL':('Pago Fácil',['Argentina']),'RAPI_PAGO':('Rapipago',['Argentina']),'MODO':('MODO',['Argentina']),
 'TRANSFERENCIA_30':('Transferencias 3.0',['Argentina']),'BANK_TRANSFER_AR':('Bank transfer',['Argentina']),
 'PIX':('PIX',['Brazil']),'SMART_PIX':('Smart PIX',['Brazil']),'PIX_AUTOMATIC':('PIX Automático',['Brazil']),'PIX_AUTOMATIC_ENROLLMENT':('PIX Automático',['Brazil']),
 'PIX_PARCELADO':('PIX Parcelado',['Brazil']),'GOOGLE_PAY_PIX':('Google Pay PIX',['Brazil']),'BOLETO':('Boleto',['Brazil']),
 'NU_PAY':('NuPay',['Brazil']),'NU_PAY_ENROLLMENT':('NuPay',['Brazil']),'PICPAY':('PicPay',['Brazil']),'ALELO':('Alelo',['Brazil']),
 'KHIPU':('Khipu',['Chile']),'WEBPAY':('Webpay',['Chile']),'MACH_PAY':('MACH',['Chile']),'BCI_MACH_QR':('MACH QR',['Chile']),'SERVIPAG':('Servipag',['Chile']),
 'PSE':('PSE',['Colombia']),'NEQUI':('Nequi',['Colombia','Panama']),'NEQUI_QR':('Nequi QR',['Colombia']),'NEQUI_ENROLLMENT':('Nequi',['Colombia']),
 'DAVIPLATA':('Daviplata',['Colombia']),'EFECTY':('Efecty',['Colombia']),'BREB':('Bre-B',['Colombia']),'BREB_LLAVES':('Bre-B',['Colombia']),
 'BANCOLOMBIA_QR':('Bancolombia QR',['Colombia']),'BANCOLOMBIA_TRANSFER':('Bancolombia transfer',['Colombia']),'BOTON_BANCOLOMBIA':('Botón Bancolombia',['Colombia']),
 'BANCOLOMBIA_BNPL':('Bancolombia BNPL',['Colombia']),'ADDI':('ADDI',['Colombia']),
 'SPEI':('SPEI',['Mexico']),'CODI':('CoDi',['Mexico']),'OXXO':('OXXO',['Mexico']),'OXXO_PAY':('OXXO Pay',['Mexico']),'PAYNET':('Paynet',['Mexico']),
 'PAYCASH':('PayCash',['Mexico']),'APLAZO':('Aplazo',['Mexico']),'DIRECT_DEBIT_ENROLLMENT':('Direct debit',['Mexico']),
 '7ELEVEN':('7-Eleven',['Mexico','Malaysia','Philippines']),
 'PAGO_EFECTIVO':('PagoEfectivo',['Peru','Ecuador']),'YAPE':('Yape',['Peru']),'YAPE_ENROLLABLE':('Yape',['Peru']),'YAPE_ONESHOT':('Yape',['Peru']),
 'CUOTEALO_BCP':('Cuotéalo BCP',['Peru']),'ACUOTAZ':('aCuotaz',['Peru']),'POWERPAY':('Powerpay',['Peru']),
 'MONNET_QR':('Monnet QR',['Peru','Guatemala']),'MONNET_WALLET':('Monnet wallet',['Peru','Guatemala']),
 'DE_UNA':('Deuna',['Ecuador']),'PAGOSNET':('PagosNet',['Bolivia']),'PAGO_AL_PASO':('Pago al Paso',['Bolivia']),
 'BANCO_NACIONAL_CASH':('Banco Nacional cash',['Costa Rica']),'BANCO_NACIONAL_TRANSFER':('Banco Nacional transfer',['Costa Rica']),
 'PUNTO_XPRESS':('PuntoXpress',['Costa Rica','El Salvador']),'BANCO_POPULAR':('Banco Popular',['Dominican Republic']),'BANRESERVAS':('Banreservas',['Dominican Republic']),
 'YAPPY':('Yappy',['Panama']),'PUNTO_PAGO':('Punto Pago',['Panama']),'PLUXEE_PA':('Pluxee',['Panama']),
 'QRIS':('QRIS',['Indonesia']),'ALFAMART':('Alfamart',['Indonesia']),'INDOMARET':('Indomaret',['Indonesia']),'OVO_WALLET':('OVO',['Indonesia']),
 'DANA':('DANA',['Indonesia']),'VIRTUAL_ACCOUNT_IDN':('Virtual Account',['Indonesia']),
 'FPX':('FPX',['Malaysia']),'BOOST':('Boost',['Malaysia']),'TOUCH_AND_GO':("Touch 'n Go",['Malaysia']),'TOUCH_AND_GO_ENROLLMENT':("Touch 'n Go",['Malaysia']),
 'GCASH':('GCash',['Philippines']),'MAYA_WALLET':('Maya',['Philippines']),'GRABPAY':('GrabPay',['Philippines']),'DIRECT_DEBIT':('Direct debit',['Philippines']),
 'SHOPEEPAY':('ShopeePay',['Indonesia','Malaysia','Philippines','Thailand']),'PAYNOW':('PayNow',['Singapore']),
 'THAI_QR':('Thai QR (PromptPay)',['Thailand']),'TRUEMONEY':('TrueMoney',['Thailand']),'BIG_C':('Big C',['Thailand']),
 'MERCADO_PAGO_WALLET':('Mercado Pago Wallet',['Argentina','Brazil','Chile','Colombia','Mexico']),
 'MERCADO_PAGO_CHECKOUT_PRO':('Checkout Pro',['Argentina','Brazil','Chile','Colombia','Mexico','Peru','Uruguay']),
}
DR_BANKS = {'ASOCIACION_BONAO','ASOCIACION_CIBAO','ASOCIACION_LA_NACIONAL','BANCO_ADOPEM','BANCO_ATLANTICO','BANCO_BANESCO','BANCO_JMMB','BANCO_LAFISE','BANCO_SANTA_CRUZ','BANCO_VIMENCA'}
WALLET_PROV = {'APPLE_PAY':'Apple Pay','GOOGLE_PAY':'Google Pay','PAYPAL':'PayPal'}
NAME = {'DLOCAL':'dLocal','MERCADO_PAGO':'Mercado Pago','PAYU':'PayU','CHECKOUT':'Checkout.com','CYBERSOURCE_GTW':'Cybersource','EBANX':'EBANX',
 'NMI':'NMI','BAC_CREDOMATIC':'BAC Credomatic','QNB_MPGS':'QNB (MPGS)','REDEBAN_DIRECT':'Redeban','REDEBAN':'Redeban','PAGSEGURO':'PagSeguro','PAGBANK':'PagBank',
 'PAGARME':'Pagar.me','PICPAY':'PicPay','TAP_PAYMENTS':'Tap Payments','E_MERCHANT_PAY':'emerchantpay','NTT_DATA':'NTT Data','PROSA_ISO':'Prosa','PROSA':'Prosa',
 'KLAP_2':'Klap','TRANSBANK_2':'Transbank','PLACE_TO_PAY':'PlacetoPay','PAY_RETAILERS':'PayRetailers','BCI_MACH':'BCI MACH','DE_UNA':'Deuna','STP':'STP',
 'FAC':'FAC','EVO':'EVO','BBVA':'BBVA','VR':'VR','AMEX':'American Express','DINERS':'Diners Club','CIBC':'CIBC','RAPPIBANK':'RappiBank','RAPPIPAY':'RappiPay',
 'PAYAMIGO':'PayAmigo','MCTPAY':'MCTPay','T1PAGOS':'T1Pagos','ALL_IN_PAY':'AllInPay','DOLARAPP':'DolarApp','PUNTOXPRESS':'PuntoXpress','PAGO_EFECTIVO':'PagoEfectivo',
 'COBRO_DIGITAL':'Cobro Digital','BANCO_DO_BRASIL':'Banco do Brasil','STARKBANK':'Stark Bank','UNLIMINT':'Unlimint','ECOMMPAY':'Ecommpay','XACBANK':'XacBank','ZOOP':'Zoop','ASTROPAY':'AstroPay','SAFETYPAY':'SafetyPay','ADDI':'ADDI','ITAU':'Itaú','OPENPAY':'Openpay','PAGALEVE':'Pagaleve','KUSHKI':'Kushki','WOMPI':'Wompi','PAYMENTEZ':'Paymentez','INSWITCH':'Inswitch','FINTOC':'Fintoc','XENDIT':'Xendit','SPINPAY':'Spinpay','OKTO':'Okto','PAGSMILE':'Pagsmile','REFACIL':'Refacil','MONNET':'Monnet','NIUBIZ':'Niubiz','IZIPAY':'Izipay','CUOTEALO':'Cuotéalo','ACUOTAZ':'aCuotaz','POWERPAY':'Powerpay','BOKU':'Boku','MAYA':'Maya','APLAZO':'Aplazo','BELVO':'Belvo','PAYVALIDA':'Payvalida','TRANSFEERA':'Transfeera','PINBANK':'Pinbank','BAMBOO':'Bamboo','DAVIPLATA':'Daviplata','NEQUI':'Nequi','YAPPY':'Yappy','MODO':'MODO','PLUXEE':'Pluxee'}
def nm(p): return NAME.get(p, p.replace('_',' ').title())
LATAM = {'Argentina','Brazil','Chile','Colombia','Mexico','Peru','Uruguay','Bolivia','Costa Rica','Dominican Republic','Ecuador','El Salvador','Guatemala','Honduras','Nicaragua','Panama','Paraguay'}
rows = list(csv.DictReader(open(SRC)))
out = collections.OrderedDict()
for r in rows:
    c, p = r['Country'], r['Provider']
    d = out.setdefault(c, {'cards':set(), 'local':collections.defaultdict(set), 'wallets':set(), 'providers':set()})
    d['providers'].add(p)
    ms = r['Payment Methods (via Yuno)'].split('; ')
    if p in WALLET_PROV: d['wallets'].add(WALLET_PROV[p]); continue
    for m in ms:
        if m == 'CARD': d['cards'].add(nm(p))
        elif m in ('PAYPAL','PAYPAL_ENROLLMENT','PAYPAL_BRAINTREE'): d['wallets'].add('PayPal')
        elif m in NATIVE and c in NATIVE[m][1]: d['local'][nm(p)].add(NATIVE[m][0])
        elif m in DR_BANKS or m == 'PAGA_TODO':
            if c == 'Dominican Republic': d['local'][nm(p)].add('Local bank transfers and cash (11 banks)' if m in DR_BANKS else 'Pagatodo')
        elif m == 'SAFETYPAY' and c not in ('Israel',): d['local'][nm(p)].add('SafetyPay')
        elif m in ('BANK_TRANSFER','CASH') and p in ('BAMBOO','DLOCAL','UNLIMINT','MONNET','PAYMENTEZ','EBANX','FINTOC') and c in LATAM:
            d['local'][nm(p)].add('Bank transfer' if m == 'BANK_TRANSFER' else 'Cash')
        elif m == 'MULTIPAGO' and c == 'Bolivia': d['local'][nm(p)].add('Multipago')
        elif m == 'PAYVALIDA' and c in ('Colombia', 'Peru'): d['local'][nm(p)].add('Payvalida')
        elif m == 'DOLARAPP' and c in ('Argentina', 'Brazil', 'Colombia', 'Mexico'): d['local'][nm(p)].add('DolarApp')
        elif m in ('ASTROPAY','ASTROPAY_ENROLLABLE') and c in ('Argentina','Brazil','Colombia','Mexico','Peru','Uruguay'): d['local'][nm(p)].add('AstroPay')
res = {}
for c, d in out.items():
    res[c] = {'n_providers': len(d['providers']), 'cards': sorted(d['cards'], key=str.lower),
              'local': {k: sorted(v) for k, v in sorted(d['local'].items(), key=lambda kv: kv[0].lower())}, 'wallets': sorted(d['wallets'])}
json.dump(res, open(OUT, 'w'), indent=1, ensure_ascii=False)
for c, d in res.items(): print(f"{c:20s} providers={d['n_providers']:3d} card={len(d['cards']):3d} local_prov={len(d['local']):2d} wallets={d['wallets']}")
