# Appmaking: respuesta a Tatsiana (21-sep-2026)

Borrador en Gmail, hilo "Appmaking + Yuno: Call Recap and Next Steps" (draft msg `1a0c62defbf08503`, v4; v1 a v3 borradas, respuesta al mensaje `1a0c47d10ec58f1a`). To: Tatsiana. Cc: Dzmitry, Jarrett, Sean (Piotr quedó fuera del cc en el último correo de Tatsiana; re-agregarlo es decisión de German).

Antes de enviar: adjuntar el PDF de la propuesta actualizada (slide 14 con ADD-ONS).

v2 (21-sep 17:45 COT): incorpora la respuesta de Jordan Belfort en Slack (llegó en alemán; traducida y cruzada con docs y casos internos). Foco: responder cada pregunta y anunciar la propuesta adjunta con el full package.

v3 (21-sep noche): German pidió reescribirlo en lenguaje simple (sin campos de API; el detalle técnico lo lleva Jarrett a la call) y alineado con la slide 13 final: PCI token vault $500/mes (ya no incluido), total estimado fully ramped $22,400/mes con add-ons ($0.149/trx), supuestos 20,000 tokens nuevos + ~17,000 updates al mes. La versión técnica v2 queda en el historial de git (commit 4403142).

## Texto

Hi Tatsiana,

Hope you had a great weekend too. Attached is the updated proposal, now with the full package priced, and below are the answers to your questions.

**Pricing**

The lines that were pending now have estimated pricing:

- **PCI token vault:** $500 per month.
- **Network tokens:** $0.05 per token created and $0.01 per token update. Using a token on a payment is not billed.
- **Reconciliation:** $1,500 a month including 50,000 reconciled transactions, then $0.032 for each additional one. It is optional, so you can add it later.

To give you the full picture, the proposal now shows what this looks like fully ramped at 150,000 transactions a month: $16,000 a month for payments, and an estimated $22,400 with all the add-ons, which is about $0.149 per transaction. The add-on figures assume roughly 20,000 new tokens and 17,000 token updates a month. We will adjust them once we know your real numbers and the phase 1 providers are set.

**One-click payments**

**1. Cards.** Yes. When a returning customer pays with a saved card, Yuno does not ask for the CVV and does not force 3DS. 3DS only runs if your own routing rules call for it or if the customer's bank demands it. Expect that more often in Europe, where strong authentication rules apply to payments the customer starts unless the bank accepts an exemption, and occasionally elsewhere when the bank or the acquirer sees a payment as risky. On CVV, it also depends on how each acquirer connection is set up, so we will test this on Unlimit and Ecommpay in sandbox with your team before go-live.

**2. Apple Pay and Google Pay.** Yes. After the first wallet payment you can charge the customer again without them opening the wallet, and it runs like a saved card. And yes, you need to store the token yourselves from that first payment, since it will not show up in the list of enrolled payment methods. Two limitations. The saved token is tied to the customer's device, so if they change phones or remove the card from the wallet it stops working and they pay through the wallet once more. And whether each provider accepts these later charges varies, so we will confirm it for Unlimit and Ecommpay in the same test.

**3. PayPal.** Yes. The customer approves a billing agreement on PayPal once, which is the only redirect, and from then on you charge the saved account directly with no redirect. Two things to keep in mind: the customer can cancel that agreement from their PayPal account at any time, and PayPal has to approve and enable this feature on your merchant account (they call it reference transactions), which you request from PayPal directly.

Jarrett can walk your technical team through the exact API fields for each of these flows. Shall we do that on Thursday at your 5:00 PM, together with the proposal?

Best regards,

German

## Fuente de cada afirmación

| Afirmación | Fuente | Estado |
|---|---|---|
| PCI token vault $500 / mes | Slide 13 final de German (21-sep) | ⚠️ La Pricing Policy dice vault $0 bundled para quien procesa pay-ins y prohíbe cobrarlo aparte; $500/mes es el precio del caso "vault-only". Decisión de German |
| Network tokens $0.05 + $0.01, el uso no se cobra | Slide 14 de German; modelo por evento: Alonso Benavides, #deal-proposals-1bn-arr 10-jul | Precio bajo el mínimo de la policy ($0.20 / $0.04): zona roja, falta firma CFO + CRO |
| Reconciliation $1,500 / 50,000 / $0.032 | Pricing Policy, pack "50K reconciled transactions" | Verificado |
| Sin CVV con vaulted_token; NTI adjunto automático | docs.y.uno stored-credentials; casos en Slack (card on file sin CVV) | Verificado |
| CVV pedido por algunos MIDs cuando el pago lleva datos 3DS | Caso vivo Ecommpay en #ext-overgear-yuno-ecommpay (8 a 10-sep), sin nombrar al merchant | Verificado; fix sin confirmar |
| 3DS como paso del route; `sdk_action_required`, `redirect_url` | docs.y.uno 3d-secure | Verificado |
| Exenciones SCA y campo de API | docs.y.uno sca-exemptions | Verificado |
| Flujo wallets: `vault_on_success`, registro CARD oculto, guardar el token | docs.y.uno stored-credentials, apple-pay-direct-integration, enroll-payment-methods | Verificado |
| PAN_ONLY vs CRYPTOGRAM_3DS | docs.y.uno google-pay-direct-integration | Verificado |
| Cargos posteriores sin criptograma, aceptación por proveedor | Casos internos (Cielo, emerchantpay) | Verificado como dependiente del proveedor; Unlimit y Ecommpay sin confirmar |
| PAYPAL_ENROLLMENT, redirect único, cobro sin redirect | docs.y.uno enroll-payment-methods; Reface en producción | Verificado; ZPY-590 (Zuora) sin confirmar si ya está resuelto |
| PayPal debe habilitar vaulting en la cuenta | Requisito de PayPal, no de Yuno | Confirmar con Jarrett |
| `stored_credentials` en `detail.wallet` para PayPal | Ticket de Varun Pathi 21-sep y repro de Starlink | Verificado |
| Casos de step up: issuer, riesgo del adquirente o scheme, exención rechazada, regulación local | Jordan Belfort (Slack, 21-sep) + docs sca-exemptions ("the card issuer has the final authority") | Verificado |
| Token del wallet atado al dispositivo, puede expirar o desactivarse | Jordan Belfort (Slack, 21-sep); comportamiento estándar de los DPAN | Verificado a nivel general |
| Dominio de Apple Pay registrado y verificado | Jordan Belfort + docs prerequisites-apple-pay | Verificado |
| PayPal = billing agreement; botón de enrollment dedicado en el SDK | Jordan Belfort + changelog Web SDK v1.11.9 (18-sep-2026): "PayPal enrollment button (vault and billing agreement)" | Verificado |
| El cliente puede revocar el agreement; PayPal puede limitar un cobro | Jordan Belfort; política de PayPal | No incluí "límites de variación del monto" por ser vago y sin fuente |

## Verificación de la sección One-click (21-sep, v4)

German pidió que quedara perfecta. Se le envió el texto a Jordan Belfort (Slack, 17:52 COT) para fact-check claim por claim; respondió "Still working on this one" y no entregó resultado (su mensaje quedó con reacción ❌). Verificación hecha con fuentes primarias:

| Claim | Fuente | Resultado |
|---|---|---|
| Saved card = one-click, sin CVV | docs.y.uno stored-credentials: CARD_ON_FILE "Allows customers one-click payment for a frictionless payment experience" | Confirmado |
| "Normally no 3DS" | El mismo doc dice que un CIT "typically requires cardholder authentication" | Sobreafirmado: se cambió a "Yuno does not force 3DS; it runs if your routing rules call for it or the bank demands it" |
| Wallet one-click sin abrir el wallet | docs.y.uno, tabla de wallet tokens: "One-click customer purchase: reason CARD_ON_FILE, usage USED" | Confirmado |
| Token del wallet atado al dispositivo | Apple Developer, merchant tokens: los DPAN se desactivan si el cliente cambia de dispositivo o quita la tarjeta | Confirmado; redacción ajustada a eso |
| PayPal debe aprobar y habilitar reference transactions | developer.paypal.com: "Approval from PayPal is required to enable reference transactions for your live account" | Confirmado |
| Botón de enrollment de PayPal con billing agreement | Changelog Web SDK v1.11.9 (18-sep-2026) | Confirmado |

Riesgos internos (NO van en el correo; para Jarrett e Ilya Ryabukhin antes de la call):
- **Ecommpay:** tarjeta guardada + paso 3DS de Yuno + sin CVV = rechazo 3201 "cvv required". Abierto desde el 8-sep, con impacto en producción; al 21-sep 03:27 COT sin hallazgos ni fecha de fix (#ext-overgear-yuno-ecommpay). Es justo el patrón de Appmaking en Europa.
- **Unlimit:** el one-click CIT sin CVV fallaba (YSHUB-6529) y se corrigió en prod el 18-ago-2026. Queda un ajuste en curso para CIT con network token + criptograma (YSHUB-6951, PR #173 en draft al 16-sep). La conexión debe estar en el tipo de integración "recurring" (/api/recurrings); el tipo e-commerce (/api/payments) siempre exige CVV. El 3DS hospedado por Unlimit no está soportado en el conector (PRIOR-1137); el 3DS de Yuno delante de Unlimit sí funciona. Rebills de wallets vía Unlimit fallaron a nivel plataforma hasta el 10-sep (YSHUB-6814, cerrado).
- **Apple Pay merchant tokens (MPAN):** sin evidencia de soporte en Yuno; no se menciona en el correo.
