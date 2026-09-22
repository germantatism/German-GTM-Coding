# FlightHub · correo post-presencial (2026-09-22)

Borrador en Gmail, reply al hilo "FlightHub + Yuno | Next Steps" (último mensaje de Anna-Lena 22-sep 13:45 UTC).
To: Anna-Lena, Nick. Cc: William, Justo, Jarrett.

Fuente de las respuestas: Jarrett por Slack, 22-sep (retries: sin delay configurable en failover, el retry completo lo controla el merchant vía create payment; disputes: "yes", alinear con Martin quién es owner de producto para capacidades vs roadmap).

Fuera del correo a propósito: la sesión de uptime / single point of failure que Will ofreció (pendiente de agendar con alguien de Yuno).

---

Subject: Re: FlightHub + Yuno | Next Steps

Hi Anna-Lena, Nick,

I caught up with William after your session. He came back with very positive feedback, thank you both for hosting him in Montreal.

Two of the questions you raised deserve a proper answer, so here is where we stand:

1. Retries with a delay. Yuno's failover retries run instantly today; there is no configurable wait time built into the failover logic. A scheduled retry is already in your hands, though: since you control the create-payment call, you can apply whatever retry timing you want on your side, with latency and user experience as the only trade-off. William would like to understand the exact scenario you have in mind so we can recommend the cleanest setup.

2. Chargebacks and disputes. The short answer is yes, dispute management is available in Yuno, including via API. William is aligning with our product team on what is live today versus on the roadmap, so we can show you exactly how it would fit alongside your current chargeback provider.

William will follow up with the details on both.

On my side, the proposal is ready. Do you have 30 minutes tomorrow to go through it together? I can adapt to whatever time works best for you.

Best,
German
