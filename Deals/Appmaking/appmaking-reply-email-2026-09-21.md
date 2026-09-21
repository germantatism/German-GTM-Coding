# Appmaking: respuesta a Tatsiana (21-sep-2026)

Borrador en Gmail, hilo "Appmaking + Yuno: Call Recap and Next Steps" (draft msg `1a0c5bf6bcda6d3d`, respuesta al mensaje `1a0c47d10ec58f1a`). To: Tatsiana. Cc: Dzmitry, Jarrett, Sean (Piotr quedó fuera del cc en el último correo de Tatsiana; re-agregarlo es decisión de German).

Antes de enviar: adjuntar el PDF de la propuesta actualizada (slide 14 con ADD-ONS).

## Texto

Hi Tatsiana,

Hope you had a great weekend too. Your team is clearly deep in the docs already, so I will go straight to the answers. I am also attaching the updated proposal, with the two pending lines now priced.

**1. Reconciliation and network tokens (estimated pricing)**

- **Token vault:** included, no separate fee.
- **Network tokens:** $0.05 per token created and $0.01 per token update (reissues, expiry changes). Using a token on a payment is not billed, that sits inside the per transaction fee.
- **Reconciliation:** $1,500 a month including 50,000 reconciled transactions, then $0.032 for each additional one. It is an optional module that covers the volume routed through Yuno, so you can switch it on later without touching the rest of the proposal.

These are estimates, and we firm them up once the phase 1 providers are set.

**2. One-click payments**

**Cards (`CARD_ON_FILE` + `USED`).** Yes. With a `vaulted_token` Yuno does not ask for the CVV, and we attach the original network transaction ID for you, so the charge reaches the acquirer flagged as a customer initiated card on file payment. Two things can still bring CVV or 3DS back:

- **CVV** is the acquirer's call. Providers generally accept card on file payments without it, but some MID configurations still request it, in particular when the payment carries 3DS authentication data. Since your live traffic runs on Unlimit and Ecommpay, we will validate both with your team in sandbox before go-live.
- **3DS** in Yuno is a step you place in your card route with your own conditions, so you decide whether returning customers go through it. When your route does call for a challenge, the payment comes back with `sdk_action_required: true` and a `redirect_url`. Beyond your own rules the issuer has the last word: in the EEA and UK a customer initiated payment stays in scope of SCA, so without an exemption the issuer can soft decline and ask for authentication. You can request exemptions through `three_d_secure.strong_customer_authentication_exemptions` (low value, transaction risk analysis and trusted beneficiary, among others), and the issuer decides whether to accept them.

**Apple Pay and Google Pay.** Yes, you read the docs right. Send the first wallet payment with `vault_on_success: true` and the `stored_credentials` under `detail.wallet` with usage `FIRST`. Yuno decrypts it into a card network token and stores it as a `CARD` record whose `parent_payment_method_type` is the wallet. Later charges use that `vaulted_token` with `detail.card.stored_credentials` and usage `USED`, with no wallet sheet and the network transaction ID attached automatically.

- And yes, store the `vaulted_token` on your side, together with the brand and last four you want to display. It is returned only in that first payment response, and wallet vaulted instruments are intentionally left out of Retrieve Enrolled Payment Methods.
- Limitations: the wallet's built in authentication covers the first payment only. Later charges travel as card on file on the network token, without a new cryptogram, so the SCA points above apply to them as well. Acceptance of that flow is provider specific, and we will confirm it on Unlimit and Ecommpay in the same sandbox pass. On Google Pay, `CRYPTOGRAM_3DS` credentials arrive as a device token, while `PAN_ONLY` credentials are the card stored in the Google account, which Yuno runs through 3DS when you have it enabled.

**PayPal.** Yes. PayPal is enrolled as its own method, `PAYPAL_ENROLLMENT`: the customer approves the agreement once on PayPal, which is the only redirect, and you receive a `vaulted_token`. From then on you charge it server side with no redirect back to PayPal. Three things to know: PayPal needs to have vaulting enabled on your PayPal merchant account, the enrollment runs through our SDK and not through the Direct card workflow, and for PayPal the `stored_credentials` go under `detail.wallet`, not `detail.card`.

**3. Call**

No worries about the invite. With this you should have everything on pricing, so shall we go through it on Thursday at your 5:00 PM? I will bring Jarrett so your technical team can go deep on the one-click flows, and we can open the shared Slack channel we talked about to keep questions like these moving quickly.

Best regards,

German

## Fuente de cada afirmación

| Afirmación | Fuente | Estado |
|---|---|---|
| Vault incluido | Pricing Policy (Laura Galan, 21-sep): $0 bundled en core | Verificado |
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
