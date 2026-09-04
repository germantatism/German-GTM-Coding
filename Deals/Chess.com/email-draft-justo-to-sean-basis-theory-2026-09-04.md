# Draft: Justo → Sean Walkinshaw (Chess.com) | Yuno vs Basis Theory

**Fecha:** 2026-09-04
**Contexto:** Sean (Senior PM, Payments & Pricing) confirmó el 2-sep que el trabajo de infra arranca a finales de Q1 2027, empezando por vaulting de payment & network tokens con Basis Theory ("happy path"), touch base en diciembre. German ya respondió suave el 3-sep. Justo entra como senior voice para mandar el side-by-side y challenging MUY soft de la decisión de vault, sin reabrir el roadmap.
**Cómo enviarlo:** Reply-all sobre el thread "Let's Reconnect | Chess.com & Yuno" (Sean puso a justo@y.uno en cc en su última respuesta), adjuntando `Yuno vs Basis Theory.pdf`.

---

## Mensaje para Justo (pasar por Slack/WhatsApp)

Justo, te dejo listo el email para Sean de Chess.com. Va como reply-all sobre el thread "Let's Reconnect | Chess.com & Yuno" (estás en cc en la última respuesta de Sean, así que te llega directo). Adjunta el PDF "Yuno vs Basis Theory" que está en la carpeta del deal. El tono es deliberadamente suave: no reabrimos el roadmap ni el touch base de diciembre, solo ponemos los hechos del vault sobre la mesa antes de que provisionen tokens en Q1. Ajusta lo que quieras y sale.

---

## Email draft (English)

**To:** sean.walkinshaw@chess.com
**Cc:** german.tatis@y.uno, alejandro@y.uno
**Subject:** Re: Let's Reconnect | Chess.com & Yuno
**Attachment:** Yuno vs Basis Theory.pdf

Hi Sean,

Justo here, jumping in briefly. German and Alejandro keep me close to this conversation, and to be clear upfront, December stands and we are not trying to reopen your roadmap.

One thought before the Q1 work kicks off. Since the plan starts with the vault, that choice deserves the same scrutiny you are giving the 2027 shortlist, because it is the piece that is hardest to change once tokens are provisioned. So we did some of that homework for you: attached is a one page, side by side view of Yuno and Basis Theory on exactly the scope you described, vaulting plus network tokens. Each cell states only what a documented source supports. Two rows worth your time:

1. Your existing card base. Basis Theory documents that existing network tokens cannot be imported, every token is provisioned from scratch. Yuno imports scheme issued tokens and has migrated them from 24 providers, including Adyen and Checkout.com. That difference decides how much of your current vault survives the move.

2. What happens after the vault. Basis Theory's own framing is that it gives you the vault and lets you build the rules yourself, so each processor request and the routing are yours to write. Yuno's vault ships with 300+ maintained processor integrations, which turns the "enable another PSP" step of your plan into configuration instead of an engineering project.

Basis Theory is a good product, and if it still comes out ahead for Chess.com after this, that is a fine outcome. We would just hate for the comparison to happen after the tokens are provisioned rather than before. Happy to walk you through it in 20 minutes if useful, otherwise it simply waits for December.

Cheers,

Justo

---

## Notas de calibración

- El challenge vive en una sola frase ("hardest to change once tokens are provisioned") y en las dos filas citadas; todo lo demás es deferente al plan de Sean.
- Los dos claims salen literal del one-pager (filas Network tokens y Token portability), cero claims nuevos.
- Se ofrece salida sin fricción: "otherwise it simply waits for December" protege la relación y el touch base acordado.
- No se menciona el shortlist ni a los competidores PSP (Checkout, Stripe, Global Payments); esta jugada es solo sobre el vault.
