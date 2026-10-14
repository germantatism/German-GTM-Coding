// Yuno x adidas: connections and payment methods for LATAM, SEA and Israel.
// Data: Yuno API reference "Payment Type" list (docs.y.uno/reference/payment-type-list)
// and Yuno Integrations Directory (y.uno/integrations), pulled 14 Oct 2026.
const REPO = "/Users/germantatis/Desktop/GTMCoding";
const Y = require(`${REPO}/.claude/skills/yuno-sales-deck/scripts/yuno_deck.js`);
const { C, MX, CW, tx } = Y;

const SRC = "Yuno API reference, Payment Type list (docs.y.uno) and Yuno Integrations Directory (y.uno/integrations), Oct 2026";
const ACT = "Method availability per country is confirmed with each provider during setup.";

(async () => {
  const d = Y.createDeck({ merchant: "adidas", footer: "Yuno × adidas · Confidential" });

  // 1. Cover
  Y.cover(d, {
    title: "YUNO × ADIDAS",
    thesis: "Connections and payment methods in LATAM, Southeast Asia and Israel",
    descriptor: "Mercado Pago · dLocal · PayU · 2C2P · PayPlus",
    date: "OCT 2026",
    yunoLogo: `${REPO}/Yuno Design System/yuno-design-system/assets/yuno-wordmark-white.png`,
    merchantLogo: `${REPO}/yuno-sales-pitch-maker/public/merchants/adidas.png`,
  });

  // 2. At a glance
  let s = Y.slide(d, {
    kicker: "At a glance",
    title: "Four of the five providers you named are live on Yuno today; PayPlus would be a new connection",
    source: SRC,
    notes: "PayPlus does not appear in Yuno's public catalog (Payment Type list or Integrations Directory). Confirm with the integrations team before positioning a timeline.",
  });
  Y.table(s, ["Provider", "Region", "Status on Yuno", "Countries", "Payment methods through Yuno"], [
    ["Mercado Pago", "LATAM", { text: "Live", bold: true, color: C.green }, "7", "Cards (Checkout API), Checkout Pro, Mercado Pago Wallet, Wallet Connect, QR, PIX, Boleto, PSE"],
    ["dLocal", "LATAM + SEA", { text: "Live", bold: true, color: C.green }, "17 LATAM, 5 SEA", "Cards, bank transfer, real time payments (PIX, SPEI, PSE, FPX...), cash vouchers (OXXO, Boleto, Efecty...), wallets (Nequi, Yape, OVO, TrueMoney...)"],
    ["PayU", "LATAM", { text: "Live", bold: true, color: C.green }, "6", "Cards, PSE"],
    ["2C2P", "SEA", { text: "Live", bold: true, color: C.green }, "7 SEA", "Cards"],
    ["PayPlus", "Israel", { text: "New connection", bold: true, color: C.amber }, "1", "Scoped on request. Israel is covered today through other providers (slide 6)"],
  ], { colW: [1.7, 1.45, 1.65, 1.5, 5.83], rowH: 0.62, fontSize: 11 });
  Y.callout(s, "How it works", "adidas integrates once with Yuno. Every connection in this deck sits behind the same API and checkout, so you can route, retry and fail over between providers in the same country without new development.", { y: 5.55, h: 0.95 });

  // 3. LATAM core markets
  s = Y.slide(d, {
    kicker: "LATAM · core markets",
    title: "In the seven core LATAM markets, every country has at least two of your providers live on Yuno",
    source: `${SRC}. ${ACT}`,
  });
  const MP = "Cards · Checkout Pro · MP Wallet";
  Y.table(s, ["Country", "Mercado Pago", "dLocal", "PayU"], [
    ["Argentina", MP, "Cards · Pago Fácil · Rapipago · MODO", "Cards"],
    ["Brazil", `${MP} · PIX · Boleto`, "Cards · PIX · Smart PIX · Boleto · NuPay", "Cards"],
    ["Chile", MP, "Cards · Khipu", "Cards"],
    ["Colombia", `${MP} · PSE`, "Cards · PSE · Bre-B QR · Efecty · Nequi", "Cards · PSE"],
    ["Mexico", MP, "Cards · SPEI · CoDi · OXXO · Paynet · 7-Eleven", "Cards"],
    ["Peru", MP, "Cards · PagoEfectivo · Yape", "Cards"],
    ["Uruguay", MP, "Cards", { text: "Not available", color: C.gray }],
  ], { colW: [1.55, 3.6, 4.6, 2.38], rowH: 0.56, fontSize: 11 });
  tx(s, "Mercado Pago also offers Wallet Connect and QR through Yuno. Checkout Pro is Mercado Pago's hosted checkout (cards, wallet and local methods in one redirect).",
    { x: MX, y: 6.3, w: CW, h: 0.4, fontSize: 9.5, italic: true, color: C.gray });

  // 4. LATAM rest of region
  s = Y.slide(d, {
    kicker: "LATAM · rest of region",
    title: "dLocal extends coverage to ten more LATAM markets with cards and local cash and wallet methods",
    source: `${SRC}. ${ACT}`,
  });
  Y.table(s, ["Country", "dLocal through Yuno", "Country", "dLocal through Yuno"], [
    ["Bolivia", "Cards · Pago al Paso", { text: "Guatemala", bold: true, color: C.navy }, "Cards"],
    ["Costa Rica", "Cards · Banco Nacional (cash) · PuntoXpress", { text: "Honduras", bold: true, color: C.navy }, "Cards"],
    ["Dominican Rep.", "Cards · Banco Popular Dominicano", { text: "Nicaragua", bold: true, color: C.navy }, "Cards · PuntoXpress"],
    ["Ecuador", "Cards · Deuna", { text: "Panama", bold: true, color: C.navy }, "Cards · Clave · Punto Pago"],
    ["El Salvador", "Cards · PuntoXpress", { text: "Paraguay", bold: true, color: C.navy }, "Cards"],
  ], { colW: [1.8, 4.265, 1.8, 4.265], rowH: 0.62, fontSize: 11 });
  Y.callout(s, "Good to know", "Mercado Pago and PayU are not live in these ten countries through Yuno. If adidas sells in any of them, dLocal is the route today, and a second provider can be added for redundancy from Yuno's wider catalog.", { y: 5.75, h: 0.85 });

  // 5. Southeast Asia
  s = Y.slide(d, {
    kicker: "Southeast Asia",
    title: "In Southeast Asia, 2C2P covers cards in seven markets and dLocal adds wallets, QR and bank methods in five",
    source: `${SRC}. ${ACT}`,
  });
  Y.table(s, ["Country", "2C2P", "dLocal"], [
    ["Indonesia", "Cards", "Cards · Virtual Account · QRIS · OVO · ShopeePay · Alfamart"],
    ["Malaysia", "Cards", "Cards · FPX · Touch 'n Go · Boost · ShopeePay · 7-Eleven"],
    ["Philippines", "Cards", "Cards · ShopeePay"],
    ["Singapore", "Cards", { text: "Not available", color: C.gray }],
    ["Thailand", "Cards", "Cards · Thai QR (PromptPay) · TrueMoney · ShopeePay · Big C"],
    ["Vietnam", "Cards", "Cards · ShopeePay"],
    ["Myanmar", "Cards", { text: "Not available", color: C.gray }],
  ], { colW: [1.9, 1.6, 8.63], rowH: 0.56, fontSize: 11 });
  tx(s, "Through Yuno, 2C2P is connected for card processing. 2C2P's own local methods can be scoped as an extension of the existing connection.",
    { x: MX, y: 6.3, w: CW, h: 0.4, fontSize: 9.5, italic: true, color: C.gray });

  // 6. Israel
  s = Y.slide(d, {
    kicker: "Israel",
    title: "PayPlus is not yet in Yuno's catalog; Israel is live today through global acquirers and wallets",
    source: SRC,
    notes: "Do not commit a PayPlus delivery date on the slide. Confirm scope and timeline with Yuno's integrations team first.",
  });
  Y.twoColumn(s,
    { header: "PayPlus: new connection", items: [
      { bold: "Status.", text: "Not in Yuno's current catalog. Built as a new connection on request." },
      { bold: "What we need.", text: "adidas's PayPlus account setup, the methods you want on it, and expected volume in Israel." },
      { bold: "Same integration.", text: "Once built, PayPlus sits behind the same Yuno API and routing as every other provider. No extra work on the adidas side." },
    ] },
    { header: "Live in Israel through Yuno today", items: [
      { bold: "Card processing.", text: "Cybersource, Nuvei, Worldline, Ecommpay" },
      { bold: "Wallets.", text: "Apple Pay, Google Pay, PayPal" },
      { bold: "Fraud and 3DS.", text: "Clearsale, Netcetera (3DS)" },
    ] },
    { y: 1.85, h: 3.2 });
  Y.callout(s, "Good to know", "While PayPlus is scoped, adidas can process in Israel through any of the live providers on the right, and move volume to PayPlus through routing once it is connected.", { y: 5.45, h: 0.95 });

  // 7. Next step
  Y.ask(d, {
    kicker: "Next step",
    title: "Share the country list and we will narrow this to your markets",
    asks: [
      { bold: "Countries.", text: "The exact markets in LATAM, Southeast Asia and Israel where adidas needs coverage." },
      { bold: "Confirm per country.", text: "Yuno confirms method activation with each provider for those markets and flags any gap." },
      { bold: "PayPlus scope.", text: "We align on PayPlus requirements and come back with a delivery plan." },
    ],
    footer: "Contact: German Tatis · german.tatis@y.uno",
    source: SRC,
  });

  const out = `${REPO}/Deals/Adidas/Yuno x adidas - Connections & Payment Methods (LATAM, SEA, Israel).pptx`;
  await Y.save(d, out);
  console.log(out);
})();
