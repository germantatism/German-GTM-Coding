# Hostinger: NDA firmado, working session y pregunta de India (2-oct-2026)

**Estado:** BORRADOR en Gmail, reply en el hilo "Hostinger + Yuno | Demo" (thread 1a0ae5f99f71a2d0), respondiendo al double email de German del 1-oct 13:18Z.
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

## Correo

Hi Paulius,

The NDA is signed, thank you for moving it through with your legal team.

That clears the way for the working session on the token migration with your own data. Would Tuesday 13 or Wednesday 14 October work, in your afternoon? Let me know who from your team should join and I'll send the invites. If you can also confirm that your network tokens sit under Hostinger's own token requestor ID, Dirk will bring the exact migration path to that session.

On India, one question so the answer I owe you next week fits your setup. You told us India runs cross-border today through Razorpay and BillDesk. Is the plan to keep it that way, or is local processing through an Indian entity on your roadmap? Cross-border is live on our side today, while local processing is a larger build for us, so knowing which one you need lets me come back with a realistic scope and timeline.

Best,
German

## Por qué está escrito así

- La pregunta de India es la que decide si el freno interno afecta a Hostinger. Si se quedan en cross-border, el scope pausado (local India processing) puede no ser el camino crítico del deal. Si quieren local, el plazo real es 2027 y hay que decírselo.
- "Cross-border is live on our side today" repite lo que German ya le escribió el 1-oct ("we're already live"). No nombra proveedores a propósito: BillDesk UPI se mostró conectado en la demo del 24-sep, Razorpay como conexión de Yuno sigue sin confirmar.
- "Local processing is a larger build for us" es la versión para el cliente de lo que dijo Antoine. No menciona fechas, ni el freno, ni Zuora.
- No promete nada nuevo sobre tokens ni mandatos UPI Autopay; solo mantiene la respuesta de la semana que viene.

## Antes de enviar

- **Validar con Antoine** si el caso de Hostinger (cross-border, Razorpay + BillDesk bajo una integración, tokens y mandatos guardados según la regulación local) entra en lo que "ya se puede hacer" o si depende del scope pausado. Antoine escribió en el hilo interno que Hostinger está interesado en "local india processing capabilities", así que él hoy lo cuenta como local.
- **Decidir si German quiere decirle ya** que local es "a larger build". Si prefiere no adelantarlo, se borra la última frase del párrafo de India y queda solo la pregunta.
- La respuesta sobre RBI, tokens y mandatos sigue debiéndose la semana del 5-oct y hoy no tiene dueño con fecha (TJ y Antoine).
