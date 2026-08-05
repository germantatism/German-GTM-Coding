# Email follow-up a Paul Pasion (Eventbrite) — 2026-08-05

**Adjuntar:** yuno-marketplace-capabilities-deck_7.html (el link file:// no funciona para él; va como archivo adjunto, se abre en cualquier browser).

**Subject:** Yuno <> Eventbrite: materials for the handoff

---

Hi Paul,

It was a pleasure connecting yesterday, and thank you for being so open about where Eventbrite is heading.

Quick recap, mostly so nothing gets lost in the handoff. The hard decision is already made: multi-PSP, with orchestration bought rather than built. What's still open is everything around it: six rails running side by side with no routing or failover between them, a payment ops lead who has every right to refuse another portal, creators locked into accounts that quietly charge FX twice, and a funds flow you want out of before PSD3 makes that call for you. And the line that stuck with us after the call: plenty of great orchestrators for pay-ins, a couple of decent ones for payouts, and nobody tying the two together. That gap is exactly where we live, and it's the story we'll bring to Milan.

Three things for you and the incoming team, sized for a quick read:

1. **Marketplace capabilities deck (attached).** Our recipients model across Stripe Connect, Adyen for Platforms, PayPal and Braintree; splits with liability assigned per leg; standalone transfers for the merchant-of-record model; and what is live versus in build. We kept the status column honest on purpose.

2. **Eventbrite deck:** https://deck.yuno.tools/m/eventbrite?s=gt. A short version of the story tailored to your stack, easy to forward.

3. **Docs:** https://docs.y.uno. The split marketplace payments section shows the actual API: recipients, onboarding, splits, transfers.

If it helps the handoff, we can prep a one-page summary for the three commerce leads in whatever format works for them, and Justo's offer stands for a working session in Milan in three weeks. If it's easy to pull the data you mentioned, that would let us make the Milan conversation concrete rather than conceptual.

Looking forward to the MNDA so we can get the introduction moving.

Best,
German

---

**Notas:**
- "the three commerce leads" evita escribir mal Noe/Giacomo/Filippo; si German verifica los nombres en LinkedIn antes de enviar, puede nombrarlos.
- GoFundMe/OLX/Whop/Leroy Merlin van nombrados en el HTML adjunto: confirmar con Justo el permiso de naming ANTES de enviar (MNDA aún no firmado).
- Sin em-dashes, sin claims de JPM/ChaseNet en el email.
