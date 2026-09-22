# FlightHub · correo post-presencial (2026-09-22)

Borrador en Gmail, reply al hilo "FlightHub + Yuno | Next Steps" (último mensaje de Anna-Lena 22-sep 13:45 UTC).
To: Anna-Lena, Nick. Cc: William, Justo, Jarrett.

Fuente de las respuestas: Jarrett por Slack, 22-sep (retries: sin delay configurable en failover, el retry completo lo controla el merchant vía create payment; disputes: "yes", alinear con Martin quién es owner de producto para capacidades vs roadmap).

v2 (pedido de German): ambas respuestas como un "sí" claro; no mencionar que el failover no tiene delay configurable.

Fuera del correo a propósito: la sesión de uptime / single point of failure que Will ofreció (pendiente de agendar con alguien de Yuno).

---

Subject: Re: FlightHub + Yuno | Next Steps

Hi Anna-Lena, Nick,

I caught up with William after your session. He came back with very positive feedback, thank you both for hosting him in Montreal.

Two of the questions you raised deserve a proper answer, so here is where we stand:

1. Retries with a delay. Yes. Yuno retries instantly on failover, and delayed or scheduled retries are available to you too: since you control the create-payment call, you decide when a retry fires and how long to wait before it does. The only trade-off to keep in mind is latency and the customer experience. William would like to understand the exact scenario you have in mind so we can recommend the cleanest setup.

2. Chargebacks and disputes. Yes. Chargeback and dispute management is available in Yuno, in the dashboard and via API. William will walk you through how it works and how it fits alongside your current chargeback provider.

William will follow up with the details on both.

On my side, the proposal is ready. Do you have 30 minutes tomorrow to go through it together? I can adapt to whatever time works best for you.

Best,
German
