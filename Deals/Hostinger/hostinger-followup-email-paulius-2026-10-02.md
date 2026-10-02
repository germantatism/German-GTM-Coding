# Hostinger: NDA firmado, working session y pregunta de India (2-oct-2026)

**Estado:** BORRADOR en Gmail (v2), reply en el hilo "Hostinger + Yuno | Demo" (thread 1a0ae5f99f71a2d0), respondiendo al double email de German del 1-oct 13:18Z.
**To:** paulius.lapenas@hostinger.com
**Cc:** ivvy@y.uno, antoine.cathelin@y.uno, dirk.meulen@y.uno, justo@y.uno, piotr@y.uno, tautvydas@y.uno

## Contexto

- **NDA firmado.** Ivvy lo confirmó en #salesops-legal (hilo "NDA - Hostinger"): "NDA signed". Era la condición para la working session con datos de Hostinger.
- **Paulius no ha respondido** a las fechas propuestas el 1-oct (martes 13 o miércoles 14-oct, en su tarde), ni a quién entra de su equipo, ni a la pregunta de Dirk sobre el TRID (25-sep). Su último correo es del 1-oct 08:15Z ("Legal accepted suggestions").
- **Promesa escrita vigente (1-oct):** "Next week I will send you an answer on what is possible under RBI rules for the card tokens and UPI Autopay mandates you hold at Razorpay and BillDesk." Vence la semana del 5-oct.
- **India, grupo de Slack de Hostinger (2-oct, Antoine):**
  - Resultado del kick-off del 1-oct: local India processing "will take us quite some time to have this in prod", "not before the end of the year".
  - Después: "we got asked to stop the scoping for now on india local processing". El freno viene de Elizabeth Sargeant ("hold on any work relating to Zuora India for now, until further notice"). Antoine le respondió que hay dos prospectos interesados ("Singapore airline", por RFP, y Hostinger); Elizabeth: "if its not just Zuora thats fine", hay una conversación abierta sobre el tiempo y los recursos que se gastan en Zuora.
  - Antoine actualizó la respuesta de ese RFP ("SA") a "we are scoping local india and would know more in 27", y anotó en ese hilo que a Hostinger le interesan las capacidades de local India processing "(and SG)".
  - Cross-border: "we can already do it" (Antoine, 29-sep).
  - German respondió "Still a GO!" y que apuntan a Razorpay y BillDesk.
- **Hostinger procesa India cross-border.** Paulius, call del 3-sep: "Yeah, we do cross border."

## Correo (v2, con los cambios que pidió German)

Hi Paulius,

The NDA is signed, thank you for moving it through with your legal team.

With that in place, the next step is the working session on how the token migration would run with your own data. It is the main pending item, and the one I'd like to get on the calendar. Would Tuesday 13 or Wednesday 14 October work, in your afternoon? Let me know who from your team should join and I'll send the invites. Dirk will walk you through it.

On India, cross-border processing is live today, and we are targeting early 2027 to go live with local processing.

Best,
German

## Qué cambió frente a la v1

- German pidió quitar la pregunta del token requestor ID (network tokens no es lo relevante ahora); Dirk queda solo como quien conduce la sesión.
- El foco pasa a ser agendar la working session de token migration, que es lo pendiente y lo más relevante.
- India deja de ser una pregunta (cross-border vs local) y pasa a ser una afirmación: cross-border live hoy, local processing a comienzos de 2027.
- La v1 se borró de Gmail; solo queda este borrador en el hilo.

## Antes de enviar

- **"Early 2027" para local processing no está confirmado internamente.** Lo que hay en Slack al 2-oct: Antoine dijo "not before the end of the year" y "Once we have an ETA I'll share it"; el scoping está pausado; en el otro RFP escribió "would know more in 27". El correo dice "we are targeting", no "we will go live", por eso. Confirmar la fecha con Antoine antes de que salga por escrito.
- El correo ya no menciona la respuesta sobre RBI, tokens y mandatos UPI Autopay que German prometió el 1-oct para la semana del 5-oct. Sigue debiéndose, o se cubre en la working session.
- Razorpay como conexión de Yuno sigue sin confirmar (BillDesk UPI se mostró en la demo del 24-sep). El correo no nombra proveedores.
