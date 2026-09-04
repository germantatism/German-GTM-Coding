# Follow-up Email — Appmaking (Tatsiana Gubarevich + Dzmitry Katsiushchyk)

**To:** t.gubarevich@appmaking.app, d.katsiushchyk@appmaking.app
**Cc:** susana.awad@y.uno, jarrett.falasco@y.uno
**Subject:** Appmaking + Yuno: Call Recap and Next Steps
**Status:** draft en Gmail (2026-09-04). ⚠️ Adjuntar el NDA firmado antes de enviar (Susana lo tiene, firmado por ambas partes).

---

Hi Tatsiana and Dzmitry,

Thank you for the time today. It was a great conversation and left us with a clear picture of what you are looking for in your next orchestration layer.

In summary:

- Diversification with full independence: as a subscription business with ~95% of revenue on web, you want volumes spread across more than one orchestration layer, on a platform that is PSP agnostic and out of the flow of funds. That is exactly how Yuno is built: you bring your own PSP relationships, set up connections and routing yourself in the dashboard, and we never charge per integration.
- Token freedom: network tokens are provisioned and lifecycle-managed by Yuno but owned by you, usable inside Yuno and outside it, with an agnostic vault and a proxy layer on top. Same logic for 3DS and Apple Pay: one authentication or decryption above the PSP layer, so MITs and retries can move across providers carrying the network transaction ID.
- Risk and dispute visibility: TC40 and SAFE data, bank and fraud rates are delivered today as normalized reports across all your providers, with dashboard views on the roadmap. Chargeback disputes can be responded to through one API where the provider supports it, and RDR and Ethoca capabilities are being relaunched in the platform.
- Connector coverage: for the first phase you mentioned Stripe, Ecompay, Unlimit, Airwallex, Shift4, Payabl and NMI, among others. We will confirm coverage for your full list in writing as part of the proposal.
- Subscriptions: our standalone engine covers plans, trials, phased and per-country pricing, metered billing and multi-currency, and every renewal follows the routing logic you define.

Next steps:

- Sandbox: we are provisioning access for you both; credentials to follow shortly.
- Documentation: https://docs.y.uno covers everything Jarrett walked through, from routing and monitors to reconciliation and network tokens.
- NDA: the fully executed copy is attached, as Susana mentioned on the call.
- Pricing in writing: share the ramp-up you have in mind (you mentioned starting around 10K transactions per month and scaling toward $1M monthly, roughly 50K transactions, over 3 to 5 months at an AOV near $18) and we will build the preliminary proposal around it: platform fee plus a fee only on successful transactions, standalone pricing for subscriptions, vault and reconciliation, Verifi and Ethoca alerting included, and a ramp structure that keeps the economics working for you well before the 100K transaction mark.
- Follow-up call: week of September 14 to review the preliminary proposal together and walk through what we did not get to cover, including our AI products, Payments Concierge and Nova. Would Tuesday the 15th or Wednesday the 16th at 5:00 PM EEST work? Same slot as today.

Best regards,

German Tatis
Yuno

---

**Notas de la call (2026-09-04, 44 min, Gong):**

- Asistieron solo Tatsiana Gubarevich (Payment Manager) y Dzmitry Katsiushchyk. Katsiaryna Butrym declinó.
- Negocio: suscripciones, **95% del revenue por web**, 5% App Store/Google Play.
- Ya trabajan con **dos orquestadores**: Solidgate + un segundo que no quisieron revelar (Dzmitry: "the performance of the second orchestrator isn't so good"). Buscan un **tercero** para diversificar volúmenes. ⚠️ La evidencia del funnel (quiz.atrix.guide) apunta a que el segundo es Truegate; no confirmado en call, no mencionar.
- **Exclusividad Solidgate:** por contrato no pueden usar Adyen, JPMorgan ni Checkout.com a través de otros gateways. No incluirlos en la propuesta fase 1.
- PSPs para fase 1 vía Yuno: Stripe, Ecompay, Unlimit, Airwallex, Shift4, Payabl (firmado, aún sin operar), NMI, +1 más que quedó garbled en el transcript (¿Nuvei?) 🔍 confirmar.
- Mercados: EU grande, US ~40%, Japón y LatAm relevantes; acaban de arrancar Pix (Brasil) y UPI (India) vía Solidgate.
- Volúmenes: arranque ~10K txn/mes, ramp a ~$1M/mes ≈ 50K txn/mes en 3 a 5 meses. AOV ~$18. Pidieron pricing por escrito con ramp hasta 100K txn/mes para ver rentabilidad.
- Asks explícitos: portabilidad de network tokens (dentro y fuera de Yuno, "the treat is ours"), data TC40/TC15(SAFE), bank rates y fraud rates por PSP, pricing de alertas Verifi y Ethoca, sandbox, documentación, interés en productos AI.
- Susana envía el NDA (ya firmado por ambas partes) junto con este follow-up.
- Pricing comunicado en call: fixed platform fee + variable solo sobre transacciones exitosas; pricing aparte para subscriptions standalone, token vault y reconciliation engine. German mencionó que el sweet spot es >100K txn/mes.
