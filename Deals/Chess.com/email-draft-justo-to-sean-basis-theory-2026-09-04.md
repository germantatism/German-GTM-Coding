# Draft: Justo → Sean Walkinshaw (Chess.com) | Yuno vs Basis Theory

**Fecha:** 2026-09-04
**Contexto:** Sean (Senior PM, Payments & Pricing) confirmó el 2-sep que el trabajo de infra arranca a finales de Q1 2027, empezando por vaulting de payment & network tokens con Basis Theory, touch base en diciembre. German ya respondió suave el 3-sep. Justo (CRO, conoce a Sean de su época en dLocal) manda el side-by-side con un challenge muy soft.
**Cómo enviarlo:** Reply-all sobre el thread "Let's Reconnect | Chess.com & Yuno" (Sean puso a justo@y.uno en cc en su última respuesta), adjuntando `Yuno vs Basis Theory.pdf`.

---

## Email draft (English)

**To:** sean.walkinshaw@chess.com
**Cc:** german.tatis@y.uno, alejandro@y.uno
**Subject:** Re: Let's Reconnect | Chess.com & Yuno
**Attachment:** Yuno vs Basis Theory.pdf

Hi Sean, great to cross paths again, it's been a while since my dLocal days.

Quick one before the Q1 vaulting work starts, since the vault is the hardest piece to change once tokens are provisioned. Attached is a one page side by side of Yuno and Basis Theory, every cell backed by documented sources. Two rows matter: Basis Theory cannot import existing network tokens, everything gets re provisioned, while we have migrated them from 24 providers including Adyen and Checkout.com. And with their vault your team still builds each processor integration and the routing, while ours ships with 300+ maintained connectors, so adding a PSP later is configuration, not a build.

Not reopening your roadmap, December stands. If a 20 minute walkthrough helps before then, happy to jump on.

Cheers,

Justo

---

## Notas

- Intro de reencuentro (dLocal), sin presentación formal.
- Challenge en una frase ("hardest piece to change once tokens are provisioned") + dos hechos del one-pager, literales de las filas Network tokens y Token portability.
- Cierre protege el touch base de diciembre acordado con German.
