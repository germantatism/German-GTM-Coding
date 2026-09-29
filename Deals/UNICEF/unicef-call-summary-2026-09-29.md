# UNICEF Colombia | Resumen de la Dashboard Demo (29-sep-2026)

**Reunión:** "Dashboard Demo Unicef x Yuno", martes 29-sep-2026, 3:00 a 3:45 p.m. COT, Google Meet.
**Invitados UNICEF:** Idual Kerguelen, Leidy Guio, Sebastian Garavito.
**Por Yuno:** German Tatis, Susana Awad, Joaquin Mann.
**Fuente:** resumen automático de la llamada, pegado por German el 29-sep. El texto de abajo está tal cual llegó.
**Follow-up:** borrador en Gmail, copia en `unicef-followup-email-2026-09-29.md`.

## Notas sobre el resumen automático

Errores de transcripción (el texto original no se tocó):

- "Revan" es Redeban.
- "Nube" es Nuvei.
- "Lady" es Leidy Guio.
- "~150,000 donations/month": en la llamada del 21-sep el dato fue unos 150.000 donantes recurrentes, 92% dona cada mes.

Puntos que cambiaron después de la llamada o que hay que cuidar:

- **ACH orchestration:** el resumen dice que el ruteo entre bancos quedó confirmado como posible. El follow-up de German lo corrige: Yuno no puede hacer smart routing ni fallbacks para transacciones ACH.
- **Wingo, 12% de aumento en aprobación:** cifra dicha en la demo. La regla interna es usar solo estadísticas publicadas (7% de uplift, 30% de revenue recuperado). No repetir el 12% por escrito sin fuente.
- **Prenotificación ACH:** sigue abierta. El follow-up habla de migrar cuentas ya prenotificadas, no de si Yuno soporta la prenotificación de cuentas nuevas.

---

# UNICEF Context and Current Stack

- ~150,000 donations/month in Colombia, avg. ticket of 50,000 COP
- Current processors: CrediBanco (via iPay), Revan, Wompi, Nube (entering by global UNICEF mandate)
- Payment methods: Nequi, Daviplata, PSE, ACH (direct bank agreements with Bancolombia, Davivienda, Banco de Bogotá)
- ACH processed via batch flat files today; Lady manually downloads, routes, and re-imports responses daily
- CRM: Salesforce, used as the billing engine and central data hub
  - Connects via a UNICEF Global-provided middleware, not direct Salesforce APIs
- Key mandates: cost optimization, higher approval rates, orchestration, and future subscriptions

# Dashboard and Orchestration Demo

- Marketplace: all processors/payment methods under one roof, new integrations via a few clicks (no months-long dev cycles)
- Routing rules: configurable by card type, country, cost, metadata (e.g. Rappi Prime users skip anti-fraud)
- Monitors: auto-alerts + traffic redistribution if approval rate drops below a set threshold
  - Example: CrediBanco falls below 85% over 10 transactions in 30 min, traffic reroutes automatically
  - Useful for off-hours donations (Sunday nights) with no team online
- Smart Routing engine: balances conversion rate and processing cost in real time
  - Wingo case study: 12% approval rate increase in a couple of months
- Insights dashboard: processor-vs-processor comparison, per-transaction detail, anti-fraud tool usage
- Payments Concierge: AI assistant via WhatsApp/Slack/Telegram for natural-language payment queries
- Nova agent: contacts declined donors via call or chat, offers a payment link with alternative methods to recover the transaction

# Subscriptions and Key Open Questions

- Subscription engine sits on top of the routing layer; supports custom retry schedules and A/B testing
  - Standard retries: ~7 min, 5 hrs, 47 hrs, 5 days, 12 days; fully customizable
- Variable donation amounts: UNICEF donors have non-fixed amounts with upgrades/downgrades mid-cycle
  - German to check with the subscriptions product lead on supporting free-form amounts
- Salesforce integration: no native connection today, but buildable
  - UNICEF's preferred model: push data to Yuno via API (not Salesforce-native); Yuno's single API would cover this
  - Existing middleware can stay untouched
- ACH orchestration: routing between banks (e.g. Davivienda → Bancolombia on decline) confirmed as possible
- ACH pre-notification (zero-value auth before full charge): German to confirm with the team if supported
- ACH response times: German to confirm (vs. real-time for card transactions)
- Existing Nube integration not yet live; can go live within one day once credentials are entered

# Next Steps

- **Validate ACH pre-notification support and response times** (German)
- **Check free-form subscription amount support with product lead** (German)
- **Prepare integration and pricing proposal for next week**
