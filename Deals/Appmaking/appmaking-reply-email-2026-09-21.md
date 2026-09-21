# Appmaking: respuesta a Tatsiana (21-sep-2026)

Borrador en Gmail, hilo "Appmaking + Yuno: Call Recap and Next Steps" (draft msg `1a0c61f1e7db4171`, v2; la v1 `1a0c5bf6bcda6d3d` fue borrada, respuesta al mensaje `1a0c47d10ec58f1a`). To: Tatsiana. Cc: Dzmitry, Jarrett, Sean (Piotr quedó fuera del cc en el último correo de Tatsiana; re-agregarlo es decisión de German).

Antes de enviar: adjuntar el PDF de la propuesta actualizada (slide 14 con ADD-ONS).

v2 (21-sep 17:45 COT): incorpora la respuesta de Jordan Belfort en Slack (llegó en alemán; traducida y cruzada con docs y casos internos). Foco: responder cada pregunta y anunciar la propuesta adjunta con el full package.

## Texto

Hi Tatsiana,

Hope you had a great weekend too. Answers to everything below, and attached is the updated proposal with the full package: the two lines that were pending are now priced, so the platform fee, the transaction tiers, token vault, network tokens, reconciliation, the subscriptions engine and the pre chargeback alerts are all in one place.

**Reconciliation and network tokens (estimated pricing)**

- **Token vault:** included, no separate fee.
- **Network tokens:** $0.05 per token created and $0.01 per token update (reissues, expiry changes). Using a token on a payment is not billed, that sits inside the per transaction fee.
- **Reconciliation:** $1,500 a month including 50,000 reconciled transactions, then $0.032 for each additional one. It is an optional module that covers the volume routed through Yuno, so you can switch it on later without touching the rest of the proposal.

These are estimates, and we firm them up once the phase 1 providers are set.

**1. Cards: CIT one-click with `CARD_ON_FILE` + `USED`**

Yes, in the normal case it skips both. You charge the `vaulted_token`, so no raw card data travels and the CVV is not involved, and Yuno attaches the original `network_transaction_id` automatically, so the payment reaches the acquirer as a customer initiated card on file charge linked to the first authenticated one.

Cases where CVV or 3DS can still be triggered:

- **Your own route.** 3DS in Yuno is a step you place in your card route with your own conditions, so it only runs for returning customers if your rules say so.
- **The issuer.** It can require authentication regardless of the stored credential flag, or decline an SCA exemption. You request exemptions through `three_d_secure.strong_customer_authentication_exemptions` (low value, transaction risk analysis and trusted beneficiary, among others), and the issuer always has the last word.
- **Local regulation.** In the EEA and UK a customer initiated payment stays in scope of SCA unless an exemption is accepted.
- **Risk.** The acquirer or the scheme can flag a transaction as high risk and force a step up.
- **CVV at the acquirer.** A few MID configurations still ask for it on card on file charges, in particular when the payment carries 3DS data. Your live traffic runs on Unlimit and Ecommpay, so we will validate both with your team in sandbox before go-live.

When a challenge does run, the payment comes back with `sdk_action_required: true` and a `redirect_url`, so the customer completes it and the sale is not lost. No orchestration layer can guarantee zero step ups, but the framework to skip CVV and 3DS is there and most of it is in your hands.

**2. Apple Pay and Google Pay**

Yes, it is supported, and you read the docs right.

- **First payment:** send it with `vault_on_success: true` and the `stored_credentials` under `detail.wallet` with usage `FIRST`. Yuno decrypts the wallet token into a card network token and stores it as a `CARD` record whose `parent_payment_method_type` is the wallet.
- **Later charges:** send the `vaulted_token` with `detail.card.stored_credentials` (`CARD_ON_FILE`, `USED`). No wallet sheet, no biometric prompt, no Apple or Google interaction. It runs on the network token rail like a card.
- **Storing the token:** yes, persist the `vaulted_token` from that first payment response, together with the brand and last four you want to display. Wallet vaulted instruments are intentionally excluded from Retrieve Enrolled Payment Methods, so an empty list for a wallet only customer is expected even though the token is valid and chargeable.

Limitations:

- The token behind the wallet is tied to the customer's device. If it expires or is deactivated, the one-click charge fails and the customer has to pay through the wallet again.
- The wallet's built in authentication covers the first payment only, so later customer initiated charges follow the same SCA logic as cards above. Acceptance of charges without a new cryptogram is provider specific, and we will confirm it on Unlimit and Ecommpay in the same sandbox pass.
- On Google Pay, `CRYPTOGRAM_3DS` credentials arrive as a device token, while `PAN_ONLY` credentials are the card stored in the Google account, which Yuno runs through 3DS when you have it enabled.
- Apple Pay on the web needs your domain registered and verified with Apple, as for any Apple Pay payment.

**3. PayPal**

Yes, after a one time enrollment. The mechanism is PayPal's billing agreement:

1. The customer goes through `PAYPAL_ENROLLMENT` and approves the agreement on PayPal. That is the only redirect, and our SDK has a dedicated PayPal enrollment button for it.
2. Yuno returns a `vaulted_token`.
3. Later charges use that token server side, with no redirect and no PayPal login window.

Restrictions:

- The agreement has its own lifecycle on PayPal's side: the customer can revoke it from their PayPal account, and PayPal's risk engine can limit a charge.
- PayPal needs to have vaulting (reference transactions) enabled on your PayPal merchant account.
- The enrollment runs through our SDK and not through the Direct card workflow, and for PayPal the `stored_credentials` go under `detail.wallet`, not `detail.card`.

Once you have gone through it, shall we do the call on Thursday at your 5:00 PM? I will bring Jarrett for the technical side.

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
| Casos de step up: issuer, riesgo del adquirente o scheme, exención rechazada, regulación local | Jordan Belfort (Slack, 21-sep) + docs sca-exemptions ("the card issuer has the final authority") | Verificado |
| Token del wallet atado al dispositivo, puede expirar o desactivarse | Jordan Belfort (Slack, 21-sep); comportamiento estándar de los DPAN | Verificado a nivel general |
| Dominio de Apple Pay registrado y verificado | Jordan Belfort + docs prerequisites-apple-pay | Verificado |
| PayPal = billing agreement; botón de enrollment dedicado en el SDK | Jordan Belfort + changelog Web SDK v1.11.9 (18-sep-2026): "PayPal enrollment button (vault and billing agreement)" | Verificado |
| El cliente puede revocar el agreement; PayPal puede limitar un cobro | Jordan Belfort; política de PayPal | No incluí "límites de variación del monto" por ser vago y sin fuente |
