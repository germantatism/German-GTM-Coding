#!/usr/bin/env python3
"""Generates bc_numbers.md, proposal_slide_content.md and pricing_internal.md from model_numbers*.json and params.py.
Every number in the three files comes from the JSON written by mirror_check.py (which matches bc_model.xlsx). Re-run after any input change."""
import json
from decimal import Decimal, ROUND_HALF_UP
from params import INP, SCEN, ALT_INCL_TPV, ALT_T1_UP

BASE = "/Users/germantatis/Desktop/GTMCoding/Deals/Carry1st/build/model/"
J = json.load(open(BASE + "model_numbers.json"))
JA = json.load(open(BASE + "model_numbers_alt.json"))
JS = json.load(open(BASE + "model_numbers_alt_step2m.json"))
T = [str(t) for t in INP["tiers"]]
SC = ["Conservative", "Base", "Optimistic"]


def r_(x, nd=0):
    return float(Decimal(repr(round(float(x), 9))).quantize(Decimal(1).scaleb(-nd), rounding=ROUND_HALF_UP))


def usd(x, nd=0):
    s = f"${abs(r_(x, nd)):,.{nd}f}"
    return f"({s})" if x < 0 else s


def K(x, plus=False):
    v = r_(x / 1000, 1)
    s = f"${abs(v):,.1f}K"
    return f"({s})" if x < 0 else (f"+{s}" if plus else s)


def Mn(x):
    s = f"{x/1e6:.2f}".rstrip("0").rstrip(".")
    if "." not in s:
        s += ".0"
    return f"${s}M"


def band(x):
    return f"${x/1e3:.0f}K" if x < 1e6 else f"${x/1e6:g}M"


P2 = lambda x: f"{r_(x*100, 2):.2f}%"
P1 = lambda x: f"{r_(x*100, 1):.1f}%"
PK = lambda x: f"${r_(x, 1):.1f}"
TX = lambda x: f"${r_(x, 3):.3f}"
X = lambda x: f"{r_(x, 1):.1f}x"
BPS = lambda x: f"{r_(x*1e4, 1):.1f} bps"
INT = lambda x: f"{r_(x, 0):,.0f}"


def PC(x):
    """Percent with no decimals when whole (15%), one decimal otherwise (4.5%)."""
    v = r_(x * 100, 1)
    return f"{v:.0f}%" if abs(v - round(v)) < 1e-9 else f"{v:.1f}%"


def TX4(x):
    """$ per transaction with 3 decimals, or 4 when the 4th is significant ($0.030, $0.0125, $0.0075)."""
    s = f"{r_(x, 4):.4f}"
    return "$" + (s[:-1] if s.endswith("0") else s)


def BE(x):
    if not isinstance(x, (int, float)):
        return x
    return f"about {r_(x/1000, 0):,.0f}K" if x >= 100000 else f"about {r_(x/1000, 1):.1f}K"


m = J["model"]
pr = J["pricing"]
be = J["breakeven"]
rp = J["ramp"]
rpc = J["ramp_credit"]
se = J["sensitivity"]
b4, b1 = m["Base"][T[3]], m["Base"][T[0]]
pa = pr["avg"]
pm = pr["med"]
t1r, t2r, t3r, t4r = INP["t1"], INP["t2"], INP["t3"], INP["t4"]
incl, t1up, t2up, t3up, pf = INP["incl_tpv"], INP["t1_up"], INP["t2_up"], INP["t3_up"], INP["pf"]
tick, med = INP["ticket"], INP["median"]
rr_bps = pa[T[3]]["total"] / pa[T[3]]["tpv"]  # all-in share of TPV at run rate

# =====================================================================
# bc_numbers.md
# =====================================================================
L = []
A = L.append
A(f"# Carry1st x Yuno · LatAm Shop launch · deck-ready numbers (15 Oct 2026, pricing v4)\n")
A(f"Source model: `bc_model.xlsx` (formula-linked; every figure here is generated from `model_numbers.json`, the Python mirror of the workbook). All figures USD, monthly unless stated. Option A = EBANX direct. Option B = EBANX primary + dLocal second MoR through Yuno. Average ticket ${tick:.0f} (Carry1st, Cordel, Oct 2026, estimate). Contribution view nets the take rate ({PC(INP['take'])}, ESTIMATE) and the Option B processing cost on every dollar of incremental GMV; the GMV view counts the full incremental GMV. Rounding: $ in K with one decimal; cost per $1,000 TPV with one decimal; Yuno share of TPV with two decimals because the figures sit under 1%.\n")
A("## Section A · Four tiers, both options, three scenarios\n")
A(f"Option A is the same in every scenario: {P1(INP['base_cost'])} of TPV (ESTIMATE, range 3 to 6%, to be replaced by EBANX's quote), i.e. {PK(b4['a_per_k'])} per $1,000 TPV: " + ", ".join(f"{K(m['Base'][t]['a_cost'])} at {INT(int(t))}" for t in T) + " transactions a month.\n")
A(f"Yuno line (identical in every scenario; $7,500 flat including the first {band(incl)} of monthly Net TPV, then {t1r*1e4:.0f} / {t2r*1e4:.0f} / {t3r*1e4:.0f} / {t4r*1e4:.0f} bps on the Net TPV above it with steps at {band(t1up)}, {band(t2up)} and {band(t3up)}): "
  + " · ".join(f"{K(pa[t]['total'])} at {INT(int(t))}" for t in T) + " (" + " · ".join(P2(pa[t]['pct']) for t in T) + " of TPV; " + " · ".join(TX(pa[t]['per_tx']) for t in T) + " per transaction).\n")


def scen_table(sn, full=False):
    s = SCEN[sn]
    A(f"### {sn} scenario (MDR {s['mdr']} bps · approval +{s['uplift']*100:.1f} pts · local methods +{s['local']*100:.1f}% of TPV · {INP['markets']} markets x {s['mkt_weeks']} weeks + {s['integ']} integration{'s' if s['integ']>1 else ''} avoided + {s['fte']:.2f} FTE maintenance)\n")
    if full:
        A("| Tx / month | TPV | Option A cost | Option A per $1,000 | Option B cost (provider + Yuno) | of which Yuno | Option B per $1,000 | Option B per $1,000 after levers | Net benefit, contribution | Net benefit, GMV view |")
        A("|---|---|---|---|---|---|---|---|---|---|")
        for t in T:
            x = m[sn][t]
            A(f"| {INT(int(t))} | {Mn(x['tpv'])} | {K(x['a_cost'])} | {PK(x['a_per_k'])} | {K(x['b_cost'])} | {K(x['yuno'])} | {PK(x['b_per_k'])} | {PK(x['b_after_k'])} | {K(x['net_c'], True)} | {K(x['net_g'], True)} |")
    else:
        A("| Tx / month | Option A per $1,000 | Option B cost | Option B per $1,000 | Option B per $1,000 after levers | Net benefit, contribution | Net benefit, GMV view |")
        A("|---|---|---|---|---|---|---|")
        for t in T:
            x = m[sn][t]
            A(f"| {INT(int(t))} | {PK(x['a_per_k'])} | {K(x['b_cost'])} | {PK(x['b_per_k'])} | {PK(x['b_after_k'])} | {K(x['net_c'], True)} | {K(x['net_g'], True)} |")
    A("")


scen_table("Base", full=True)
A(f"Break-even: {BE(be['Base'])} successful transactions a month (about {Mn(be['Base']*tick) if isinstance(be['Base'], (int, float)) else 'n/a'} TPV).\n")
scen_table("Conservative")
A(f"Break-even: {BE(be['Conservative'])} transactions a month. Reading: in the conservative case Yuno is cost-neutral well before the run rate; what Carry1st buys for {K(-m['Conservative'][T[0]]['net_c'])} a month net at launch is failover, a second provider in play and the local-method coverage.\n")
scen_table("Optimistic")
A(f"Break-even: {BE(be['Optimistic'])} transactions a month. The approval uplift of {SCEN['Optimistic']['uplift']*100:.0f} points stays under Yuno's published 7% authorization uplift.\n")

A("## Section B · Scenario summary at launch (50K) and at run rate (450K)\n")
A("### Monthly\n")
A("| | Conservative | Base | Optimistic |")
A("|---|---|---|---|")
rows = [("Gross benefit at 50K", lambda s: K(m[s][T[0]]['gross_c'])), ("Yuno cost at 50K", lambda s: K(m[s][T[0]]['yuno'])),
        ("Net at 50K (contribution)", lambda s: K(m[s][T[0]]['net_c'], True)), ("Net at 50K (GMV view)", lambda s: K(m[s][T[0]]['net_g'], True)),
        ("Gross benefit at 450K", lambda s: K(m[s][T[3]]['gross_c'])), ("Yuno cost at 450K", lambda s: K(m[s][T[3]]['yuno'])),
        ("Net at 450K (contribution)", lambda s: K(m[s][T[3]]['net_c'], True)), ("Net at 450K (GMV view)", lambda s: K(m[s][T[3]]['net_g'], True)),
        ("Gross benefit / Yuno cost at 450K", lambda s: X(m[s][T[3]]['roi'])), ("Break-even, tx a month", lambda s: BE(be[s])),
        ("Payback month on the ramp (cumulative net turns positive)", lambda s: rp[s]['payback'])]
for lbl, f in rows:
    A(f"| {lbl} | " + " | ".join(f(s) for s in SC) + " |")
A("")
A("### Annual (x12 at the volume shown)\n")
A("| | Conservative | Base | Optimistic |")
A("|---|---|---|---|")
rows = [("Net a year at 50K (contribution)", lambda s: K(m[s][T[0]]['net_c']*12, True)), ("Net a year at 450K (contribution)", lambda s: K(m[s][T[3]]['net_c']*12, True)),
        ("Net a year at 450K (GMV view)", lambda s: Mn(m[s][T[3]]['net_g']*12) if m[s][T[3]]['net_g']*12 >= 1e6 else K(m[s][T[3]]['net_g']*12, True)),
        ("Yuno cost a year at 450K", lambda s: K(m[s][T[3]]['yuno']*12)), ("Option A cost a year at 450K", lambda s: Mn(m[s][T[3]]['a_cost']*12)),
        ("Option B cost a year at 450K (provider + Yuno)", lambda s: Mn(m[s][T[3]]['b_cost']*12)),
        (f"Cumulative net over the {INP['ramp_m']}-month ramp (Dec 2026 to Dec 2027, linear 50K to 450K, ESTIMATE)", lambda s: K(rp[s]['cum'], True)),
        (f"Yuno cost over the {INP['ramp_m']}-month ramp", lambda s: K(rp[s]['yuno_total']))]
for lbl, f in rows:
    A(f"| {lbl} | " + " | ".join(f(s) for s in SC) + " |")
A("")
A("### Lever breakdown (monthly, contribution view; GMV in brackets where the lever is a GMV effect)\n")
A("| Lever | Cons. 50K | Base 50K | Opt. 50K | Cons. 450K | Base 450K | Opt. 450K |")
A("|---|---|---|---|---|---|---|")
cells = [(s, t) for t in (T[0], T[3]) for s in SC]
A("| L1 · MDR reduction (100% contribution) | " + " | ".join(K(m[s][t]['l1']) for s, t in cells) + " |")
A("| L2 · retries and routing recovery | " + " | ".join(f"{K(m[s][t]['l2c'])} [{K(m[s][t]['l2g'])} GMV]" for s, t in cells) + " |")
A("| L3 · local-method coverage | " + " | ".join(f"{K(m[s][t]['l3c'])} [{K(m[s][t]['l3g'])}]" for s, t in cells) + " |")
A("| L4 (deck L5) · integrations avoided (per-market EBANX work and later integrations over 24 months, plus maintenance), monthly | " + " | ".join(K(m[s][t]['l4']) for s, t in cells) + " |")
A("| Gross benefit | " + " | ".join(K(m[s][t]['gross_c']) for s, t in cells) + " |")
A("")
tt = J["ttm"]
A("### L5 (deck L3) · Time to market: 2027 value from reaching run rate sooner (kept apart from the recurring levers)\n")
A("Going direct with EBANX, markets are enabled one by one, so sales ramp linearly from $0.5M a month in Dec 2026 to $4.5M in Dec 2027. Through Yuno, all five markets go live together on one integration, each with its local methods and more than one provider, so the run rate is reached sooner and then holds flat. Value = extra 2027 sales x (take rate minus the Yuno route's all-in processing cost at run rate), the same contribution logic as the other sales levers. It is a first-year value, not a recurring one.\n")
A("| | Conservative | Base | Optimistic |")
A("|---|---|---|---|")
for lbl, f in [("Through Yuno: run rate reached in", lambda s: tt[s]['rr_month']), ("Extra sales in 2027 (GMV)", lambda s: Mn(tt[s]['extra'])),
               ("Contribution per $1 of extra sales", lambda s: P2(tt[s]['margin'])), ("L5 · 2027 value from reaching run rate sooner", lambda s: Mn(tt[s]['l5'])),
               ("Recurring levers a year at run rate (L1 to L4)", lambda s: Mn(tt[s]['rec']) if tt[s]['rec'] >= 1e6 else K(tt[s]['rec'])),
               ("2027 value including time to market", lambda s: Mn(tt[s]['tot27'])), ("Yuno cost a year at run rate", lambda s: K(tt[s]['yuno_y'])),
               ("Net a year, recurring levers", lambda s: K(tt[s]['net_rec'], True) if abs(tt[s]['net_rec']) < 1e6 else "+" + Mn(tt[s]['net_rec'])),
               ("Net, 2027 including time to market", lambda s: "+" + Mn(tt[s]['net27'])),
               ("Multiple, recurring levers / Yuno", lambda s: X(tt[s]['x_rec'])), ("Multiple, 2027 including time to market / Yuno", lambda s: X(tt[s]['x27']))]:
    A(f"| {lbl} | " + " | ".join(f(s) for s in SC) + " |")
A("")
A(f"L1 is the lever that matters most for a reseller: a processing saving is 100% contribution, while incremental GMV is worth take rate minus processing cost (about {r_((INP['take']-b4['b_pct'])*100,0):.0f} cents per dollar at a {PC(INP['take'])} take rate). In the base case L1 is {P1(b4['l1']/b4['gross_c'])} of the gross benefit at 450K.\n")

A("## Section C · Small-ticket sensitivity (why bps on Net TPV is the right shape)\n")
A(f"Same transactions, three tickets. Yuno total = $7,500 platform fee (first {band(incl)} of monthly Net TPV included) + usage on the Net TPV above the block ({P2(t1r)} to {band(t1up)}, {P2(t2r)} {band(t1up)} to {band(t2up)}, {P2(t3r)} {band(t2up)} to {band(t3up)}, {P2(t4r)} above {band(t3up)}).\n")
A("| Ticket · line | " + " | ".join(f"{INT(int(t))} tx" for t in T) + " |")
A("|---|---|---|---|---|")
s5, s10, s15 = se["ticket"]["5.0"], se["ticket"]["10.0"], se["ticket"]["15.0"]
A("| $5 (median) · TPV | " + " | ".join(Mn(s5[t]['tpv']) for t in T) + " |")
A("| $5 · Yuno total | " + " | ".join(K(s5[t]['yuno']) for t in T) + " |")
A("| $5 · Yuno, % of TPV | " + " | ".join(P2(s5[t]['pct']) for t in T) + " |")
A("| $5 · Yuno, $ per transaction | " + " | ".join(TX(s5[t]['ptx']) for t in T) + " |")
A("| $5 · Yuno usage only, $ per transaction | " + " | ".join(TX4(s5[t]['uptx']) for t in T) + " |")
A("| $5 · a fixed $0.05 per transaction | " + " | ".join(f"{K(s5[t]['fa'])} ({P2(s5[t]['fa_pct'])})" for t in T) + " |")
A("| $5 · a fixed $0.10 per transaction | " + " | ".join(f"{K(s5[t]['fb'])} ({P2(s5[t]['fb_pct'])})" for t in T) + " |")
A("| $10 (average) · Yuno total | " + " | ".join(K(s10[t]['yuno']) for t in T) + " |")
A("| $10 · Yuno, % of TPV | " + " | ".join(P2(s10[t]['pct']) for t in T) + " |")
A("| $10 · Yuno, $ per transaction | " + " | ".join(TX(s10[t]['ptx']) for t in T) + " |")
A("| $10 · a fixed $0.05 / $0.10 per transaction, % of TPV | " + " | ".join(f"{P2(s10[t]['fa_pct'])} / {P2(s10[t]['fb_pct'])}" for t in T) + " |")
A("| $15 · Yuno total | " + " | ".join(K(s15[t]['yuno']) for t in T) + " |")
A("| $15 · Yuno, % of TPV | " + " | ".join(P2(s15[t]['pct']) for t in T) + " |")
A("| $15 · a fixed $0.05 / $0.10 per transaction, % of TPV | " + " | ".join(f"{P2(s15[t]['fa_pct'])} / {P2(s15[t]['fb_pct'])}" for t in T) + " |")
A("")
A(f"Reading for the slide: a fixed fee is blind to the ticket, so when the ticket halves the fee doubles as a share of what Carry1st sells ($0.05 becomes 1.0% of TPV at a $5 median, $0.10 becomes 2.0%). Yuno's usage is a share of Net TPV, so at a $5 median the usage rate is {TX4(t1r*med)} per transaction in tranche 1, {TX4(t2r*med)} in tranche 2, {TX4(t3r*med)} in tranche 3 and {TX4(t4r*med)} in tranche 4, and the all-in cost at 450K is {P2(pm[T[3]]['pct'])} of TPV against 1.0% or 2.0% for the fixed fees. The platform fee is the one fixed element, which is why the first {band(incl)} of monthly volume sits inside it: at launch Carry1st pays $7,500 and nothing per transaction. Be upfront that at 50K transactions and a $5 ticket the platform fee alone is {P2(pm[T[0]]['pct'])} of TPV; the structure pays off as volume ramps, not in month one.\n")
A("### Take rate sensitivity (base scenario, contribution view)\n")
A("| Take rate on GMV | Net at 50K / month | Net at 450K / month | Net at 450K / year | Gross / Yuno at 450K |")
A("|---|---|---|---|---|")
for tr, lbl in (("0.1", "10%"), ("0.15", f"{PC(INP['take'])} (default, ESTIMATE)"), ("0.25", "25%")):
    n1, n4 = se["take"][tr][T[0]], se["take"][tr][T[3]]
    A(f"| {lbl} | {K(n1, True)} | {K(n4, True)} | {K(n4*12, True)} | {X((n4 + b4['yuno'])/b4['yuno'])} |")
A("")
A("### Baseline provider cost sensitivity (base scenario, 450K)\n")
A("| Baseline all-in cost | Option A per $1,000 | Option B per $1,000 (provider + Yuno) | Option B per $1,000 after levers | Net a month | Net a year |")
A("|---|---|---|---|---|---|")
for bc, lbl in (("0.03", "3.0%"), ("0.045", "4.5% (default, ESTIMATE)"), ("0.06", "6.0%")):
    x = se["base_cost"][bc]
    A(f"| {lbl} | {PK(x['a_per_k'])} | {PK(x['b_per_k'])} | {PK(x['b_after_k'])} | {K(x['net_c'], True)} | {K(x['net_c_y'], True)} |")
A("")
A("The MDR lever is a gap between two routes (bps), so the baseline level moves both options together; the net benefit changes only through the processing cost netted on incremental GMV.\n")

A("## Section D · Assumptions, as they should appear on the \"Risks and assumptions\" slide\n")
A(f"1. Volumes: 50K, 100K, 200K and 450K successful transactions a month at a ${tick:.0f} average ticket ($0.5M to $4.5M TPV). Run rate: Carry1st estimate, Cordel, Oct 2026, not yet aligned internally. Launch volume: OPEN, owner Cordel.")
A("2. Baseline provider cost (EBANX direct, cross-border MoR all-in incl. FX and local taxes passed through): 4.5% of TPV, ESTIMATE, range 3 to 6%. Public anchors: dLocal revenue / TPV 2.68% in 2025 (blended, FXC Intelligence, Mar 2026); EBANX merchant review about 5% per transaction (Capterra, 2021); FX spread 1 to 3% (Nuvei, 2026); Brazil IOF 3.5% on FX (Decree 12,466/2025). Replaced by EBANX's quote to Carry1st as soon as it arrives.")
A(f"3. Carry1st take rate on GMV: {PC(INP['take'])}, ESTIMATE, TO VALIDATE with Cordel (reseller margins on mainstream gift cards 5 to 15% above wholesale, public guides 2026). Contribution on incremental GMV = GMV x (take rate minus Option B processing cost).")
A("4. L1 MDR reduction with a second MoR in play and routing share to the cheaper route: 25 / 50 / 75 bps of TPV (Yuno estimate; EBANX and dLocal rates through Yuno OPEN, owner Justo).")
A("5. L2 baseline approval on a single MoR route: 75% blended, ESTIMATE, range 70 to 85% (Mexico local 80%+ vs cross-border 50 to 60%, Nuvei 2026; Brazil cross-border cards under 60%, Antom 2025; 10 to 20 point gap by setup, Rapyd 2026). Uplift from retries, failover and second-provider routing: +1.5 / +3.0 / +5.0 points on attempted volume (Yuno estimate; ceiling = Yuno published 7% authorization uplift). Proxy to validate: Carry1st's Saudi and Africa approval rates, owner Cordel.")
A("6. L3 local-method coverage: +2% / +4% / +6% of TPV as incremental GMV, ESTIMATE (German, 15 Oct 2026: LatAm is APM-driven; Pix is 42% of online purchases in Brazil, PSE 64% of e-commerce transactions in Colombia, wallets 46% of e-commerce in Argentina). Through Yuno the checkout adds the methods a single provider does not carry (MODO and interoperable QR in Argentina, Bre-B and Nequi in Colombia, cards and QR in Bolivia) and optimizes the method mix per market. Methods carried through Yuno via dLocal and not on the EBANX connection (docs.y.uno, 14 Oct 2026): MODO, Rapipago, Pago Facil (Argentina); Bre-B, Nequi, PSE, Efecty (Colombia); Multipago, Pago al Paso (Bolivia); CoDi, Paynet, 7-Eleven (Mexico). EBANX direct coverage per country TO VALIDATE against its quote.")
A("7. L4 integrations avoided (deck lever L5), three parts at $2,500 per loaded engineer-week ($130K a year, a senior payments engineer; ESTIMATE, Justo 15 Oct 2026: dev cost avoided above $150K a year): (a) per-market EBANX direct work, 5 markets x 3 / 4 / 6 engineer-weeks (country enablement, per-country sandbox tests and certification, local methods; EBANX enables countries during onboarding, each country passes sandbox tests and an Integration Review before production), one-time; (b) later direct integrations avoided, 2 / 3 / 4 (second MoR, local acquirer, later local processors) x 6 / 8 / 10 engineer-weeks (4 to 8 weeks per server-to-server PSP integration, spd.tech 2026), one-time; (c) ongoing maintenance of the direct integrations (API changes, certifications, incident handling), 1.0 / 1.5 / 2.5 FTE a year at $130K (52 x $2,500). One-time items spread over 24 months, so the yearly value is one-time / 2 + maintenance. Through Yuno: one integration ready for every market, Yuno maintains the connections. The launch integration itself is not counted.")
A(f"8. Yuno cost: $7,500 a month flat platform fee that includes the first {band(incl)} of monthly Net TPV (successful transactions only, no declines, no chargebacks; single month, no rollover); usage on the Net TPV above it at {P2(t1r)} ({band(incl)} to {band(t1up)}), {P2(t2r)} ({band(t1up)} to {band(t2up)}), {P2(t3r)} ({band(t2up)} to {band(t3up)}), {P2(t4r)} (above {band(t3up)}), each band on the volume inside it. Declines not billed. Add-ons (network tokens, 3DS) on usage, not in these totals.")
A("9. Ramp for payback: linear from 50K at Black Friday 2026 to 450K by Dec 2027, Yuno ESTIMATE; replaced by Cordel's written projections by country.")
A("9b. L5 time to market (deck lever L3): going direct, a linear ramp from $0.5M a month in Dec 2026 to $4.5M in Dec 2027 (markets enabled one by one); through Yuno, $4.5M reached in Sep 2027 / Jun 2027 / Apr 2027 (conservative / base / optimistic), then flat. Value = extra 2027 sales x (take rate minus Option B all-in at run rate). A one-off 2027 value, shown apart from the recurring totals, Yuno ESTIMATE.")
A("10. Levers L1 to L4 are modeled on the same TPV and are additive by construction (a cost saving, two GMV effects netted of processing cost, one engineering saving); nothing is double counted. L5 is a 2027 value on the ramp and is never added to the recurring totals. Yuno-wide figures are used only as guardrails: 7% authorization uplift and 30% recovered revenue (y.uno).\n")

A("## Section E · The 12 numbers for the executive summary\n")
A(f"1. {Mn(b4['tpv'])} a month of TPV at the end-2027 run rate (450K transactions at a ${tick:.0f} ticket), Carry1st estimate, Cordel, Oct 2026.")
A(f"2. Option A (EBANX direct) at run rate: {K(b4['a_cost'])} a month, {PK(b4['a_per_k'])} per $1,000 TPV ({P1(INP['base_cost'])} all-in, ESTIMATE until EBANX's quote).")
A(f"3. Option B (EBANX + dLocal through Yuno) at run rate, base: {K(b4['b_cost'])} a month, {PK(b4['b_per_k'])} per $1,000 TPV, i.e. {'a lower cost line' if b4['b_per_k'] < b4['a_per_k'] - 0.5 else ('the same cost line' if abs(b4['b_per_k']-b4['a_per_k']) <= 0.5 else 'about the same cost line')} with failover, a second provider and local methods included.")
A(f"4. Yuno at run rate: {usd(b4['yuno'])} a month, {P2(b4['yuno_pct'])} of TPV, {TX(b4['yuno_tx'])} per successful transaction ({usd(b4['yuno']*12)} a year).")
A(f"5. Yuno at launch (50K): {usd(b1['yuno'])} a month and nothing per transaction; the first {band(incl)} of monthly volume is inside the platform fee.")
A(f"6. Base net benefit at run rate: {K(b4['net_c'])} a month, {K(b4['net_c']*12)} a year (contribution view, net of Yuno's fee).")
A(f"7. Base gross benefit {K(b4['gross_c']*12)} a year against {K(b4['yuno']*12)} of Yuno fees: {X(b4['roi'])}.")
A(f"8. Break-even: {BE(be['Base'])} successful transactions a month ({Mn(be['Base']*tick) if isinstance(be['Base'], (int, float)) else 'n/a'} TPV), base case.")
_pb = lambda s: (f"turns positive in {rp[s]['payback']}" if rp[s]['payback'] != "not within the ramp" else "does not turn positive within the ramp")
A(f"9. Payback on the ramp: cumulative net benefit turns positive in {rp['Base']['payback']} (base); the optimistic case {_pb('Optimistic')}; the conservative case {_pb('Conservative')}.")
A(f"10. GMV view at run rate, base: {Mn(b4['net_g']*12)} a year of incremental GMV and savings ({K(b4['net_g'])} a month).")
A(f"11. Small ticket: at the $5 median, Yuno's usage is {TX4(t1r*med)} per transaction in tranche 1, {TX4(t2r*med)} in tranche 2, {TX4(t3r*med)} in tranche 3 and {TX4(t4r*med)} in tranche 4 against $0.05 or $0.10 for a fixed fee; at 450K transactions Yuno all-in is {P2(pm[T[3]]['pct'])} of TPV against 1.0% or 2.0%.")
A(f"12. Scenario range at run rate: conservative {K(m['Conservative'][T[3]]['net_c'], True)} a month, base {K(b4['net_c'], True)}, optimistic {K(m['Optimistic'][T[3]]['net_c'], True)} a month ({K(m['Optimistic'][T[3]]['net_c']*12, True)} a year).\n")

A("## Section F · Break-even by gross margin (run rate)\n")
A(f"All-in Yuno cost at the {Mn(b4['tpv'])} run rate: {usd(b4['yuno'])} a month = {BPS(rr_bps)} of TPV ({P2(rr_bps)}). The question a CFO asks: how much more approved volume does Carry1st need for the fee to pay for itself out of its own margin? Incremental approved sales needed = all-in bps / gross margin.\n")
A("| Carry1st gross margin on GMV | Incremental approved sales needed to cover the Yuno fee |")
A("|---|---|")
for gm in (0.10, 0.15, 0.20, 0.30):
    A(f"| {P1(gm)[:-1].rstrip('0').rstrip('.')}% | about +{P1(rr_bps/gm)} |")
A("")
A(f"Yuno's published authorization uplift of 7% (y.uno) covers every one of these thresholds; the base case in this deck uses +3 points on a 75% baseline, i.e. +4.0% more approved volume, before the MDR and local-method levers.\n")
A(f"Marginal Yuno usage on a median $5 purchase: {TX4(t1r*med)} in tranche 1 ({t1r*1e4:.0f} bps), {TX4(t2r*med)} in tranche 2 ({t2r*1e4:.0f} bps), {TX4(t3r*med)} in tranche 3 ({t3r*1e4:.0f} bps), {TX4(t4r*med)} in tranche 4 ({t4r*1e4:.0f} bps). On the $10 average purchase: {TX4(t1r*tick)}, {TX4(t2r*tick)}, {TX4(t3r*tick)}, {TX4(t4r*tick)}.\n")

A("## Inputs to swap when Carry1st's data arrives (Inputs sheet, yellow cells)\n")
A("| Input | Today | Replace with | Owner |")
A("|---|---|---|---|")
A("| Baseline provider all-in cost | 4.5% ESTIMATE | EBANX's quoted all-in rate to Carry1st by country (incl. FX and taxes) | Cordel |")
A("| Volumes by tier and ramp | 50K / 100K / 200K / 450K, linear ramp | Written volume projections by country | Cordel |")
A(f"| Average and median ticket | ${tick:.0f} / ${med:.0f} | Shop data by country | Cordel |")
A(f"| Take rate on GMV | {PC(INP['take'])} | Carry1st Shop margin on top-ups and gift cards | Cordel |")
A("| Baseline approval | 75% | Saudi / Africa approval and method mix as proxy, then LatAm actuals | Cordel, Yuno |")
A("| Local-method uplift | 2 / 4 / 6% | Method mix by country once live; EBANX direct coverage per country | German, research |")
A("| Engineer-weeks, maintenance and loaded cost | 3 / 4 / 6 weeks per market, 6 / 8 / 10 weeks per later integration, 1.0 / 1.5 / 2.5 FTE maintenance, $2,500 a week | Fatih's estimate for EBANX per-market work, a direct PSP integration, upkeep and his team cost | Fatih |")
A(f"| Net incremental GMV of processing cost | 1 (yes) | Keep at 1 for a CFO audience; 0 shows the simpler GMV x take rate view (base break-even moves to {BE(J['netflag0_base_breakeven'])}) | German |")
open(BASE + "bc_numbers.md", "w").write("\n".join(L) + "\n")

# =====================================================================
# proposal_slide_content.md
# =====================================================================
p50, p200, p450 = pa[T[0]], pa[T[2]], pa[T[3]]
L = []
A = L.append
A("# Proposal slide · Carry1st + Yuno (customer-facing text, one slide, three-card format)\n")
A("Eyebrow: **06 · Proposal**")
A(f"Title (action title): **One platform fee that already covers the first {band(incl)} of monthly volume, then a share of volume that falls as Carry1st grows**")
A(f"Sub-line (grey, one line): \"A $7,500 monthly platform fee that covers the first {band(incl)} of monthly volume, plus a percentage of the volume above it: {usd(p450['total'])} a month at 450,000 transactions, {P2(p450['pct'])} of TPV, {TX(p450['per_tx'])} per transaction.\"\n")
A("## Left card · TRANSACTION FEE\n")
A("Sub-line (grey): \"A percentage of the month's volume above the included block, pooled across Brazil, Argentina, Mexico, Bolivia and Colombia\"\n")
A("| Label | Range (monthly volume) | Rate |")
A("|---|---|---|")
A(f"| INCLUDED | First {band(incl)} of monthly volume | **$0** |")
A(f"| TRANCHE 1 | {band(incl)} to {band(t1up)} | **{P2(t1r)}** |")
A(f"| TRANCHE 2 | {band(t1up)} to {band(t2up)} | **{P2(t2r)}** |")
A(f"| TRANCHE 3 | {band(t2up)} to {band(t3up)} | **{P2(t3r)}** |")
A(f"| TRANCHE 4 | Above {band(t3up)} | **{P2(t4r)}** |\n")
A(f"Note box (light grey): \"No setup fee. No fixed amount per transaction. Volume means successful transactions only: declines and card verification attempts are not billed. Each tranche applies only to the volume inside it, so Carry1st's highest volume always pays the lowest rate. At a $10 ticket, {P2(t1r)} is {TX4(t1r*tick)} per transaction; at a $5 ticket, {TX4(t1r*med)}.\"\n")
A("## Middle card · PLATFORM FEE\n")
A("Big figure (Yuno blue): **$7,500** with \"/ month\" in grey.")
A(f"Sub-line: \"$90,000 / year. Covers the first {band(incl)} of monthly volume. This is what covers the stack.\"\n")
A("**WHAT IT INCLUDES**\n")
A("| Label | Value |")
A("|---|---|")
A("| Orchestration & rules engine | **Included** |")
A("| Smart routing & retries | **Included** |")
A("| Monitors & auto-failover | **Included** |")
A("| Payment methods, PSPs and fraud solutions | **1,000+** |")
A("| Checkout & SDKs (web, iOS, Android) | **Included** |")
A("| PCI token vault | **Included** |")
A("| Dashboard & insights | **Included** |")
A("| Dedicated KAM and TAM | **Included** |\n")
A("**ADD-ONS** box (white inner box; grey sub-line \"Billed on usage, quoted separately, not in the totals on this slide.\"):\n")
A("| Label | Value |")
A("|---|---|")
A("| Network tokens | On usage |")
A("| 3DS authentication | On usage |\n")
A("Last line (small grey): \"Every integration maintained by Yuno. Adding dLocal, a local acquirer or a new local method later is a routing change, not a new project.\"\n")
A("## Right card (blue) · WHAT IT MEANS FOR CARRY1ST\n")
A(f"Sub-line: \"At a ${tick:.0f} average ticket, across the five markets\"\n")
A("| LINE | 50,000 tx / month | 200,000 tx / month | 450,000 tx / month |")
A("|---|---|---|---|")
A(f"| Volume a month | {Mn(p50['tpv'])} | {Mn(p200['tpv'])} | {Mn(p450['tpv'])} |")
A(f"| Platform fee | {usd(p50['pf'])} | {usd(p200['pf'])} | {usd(p450['pf'])} |")
A(f"| Usage · tranche 1 | {usd(p50['t1']*t1r)} | {usd(p200['t1']*t1r)} | {usd(p450['t1']*t1r)} |")
A(f"| Usage · tranche 2 | {usd(p50['t2']*t2r)} | {usd(p200['t2']*t2r)} | {usd(p450['t2']*t2r)} |")
A(f"| **Total a month** | **{usd(p50['total'])}** | **{usd(p200['total'])}** | **{usd(p450['total'])}** |")
A(f"| Total a year | {usd(p50['total']*12)} | {usd(p200['total']*12)} | {usd(p450['total']*12)} |")
A(f"| Share of volume | {P2(p50['pct'])} | {P2(p200['pct'])} | {P2(p450['pct'])} |")
A(f"| Per successful transaction | {TX(p50['per_tx'])} | {TX(p200['per_tx'])} | {TX(p450['per_tx'])} |\n")
A(f"Callout box (darker blue, bold white): \"At launch Carry1st pays the platform fee and nothing per transaction. At the run rate the all-in cost is {P2(p450['pct'])} of volume, falling as volume grows.\"\n")
A(f"Paragraph under it: \"Usage at the $5 median ticket is {TX4(t1r*med)} per transaction in tranche 1 and {TX4(t4r*med)} in tranche 4, where a fixed fee would stay at the same dollar amount whatever the ticket. The business case in this deck returns about {K(b4['gross_c'])} a month in savings and contribution at the run rate (base case), {X(b4['roi'])} this cost.\"\n")
A("## Footer (small grey, bottom left)\n")
A("\"Platform fee billed annually. Usage billed monthly in arrears on successful transactions, net 30. Rates locked for the term, tranches reviewed annually as volume grows. All figures in USD.\"\n")
A("## Build notes for the content agent (not on the slide)\n")
A("- Three cards: left white with light border (about 28% of content width), middle light panel (about 30%), right solid Yuno blue with white text (about 32%), the same card language as German's previous three-card proposal slides.")
A("- Only the quoted price appears. Apply the forbidden-word rule in CONTEXT.md to every figure on the slide. The platform fee is simply the platform fee, never phrased as a commitment threshold. Nothing beyond the quoted structure goes on the slide: no alternative block size, no term length, no launch-month variation.")
A("- If the eight rows plus the add-ons box do not fit at body size, merge \"Monitors & auto-failover\" and \"PCI token vault\" into one row \"Monitors, auto-failover & PCI token vault · Included\". Never go below the body size used on the business-case slides.")
A(f"- Numbers must match `bc_model.xlsx` Pricing sheet (average-ticket block) exactly: {usd(p50['total'])} / {usd(p200['total'])} / {usd(p450['total'])}; {P2(p50['pct'])} / {P2(p200['pct'])} / {P2(p450['pct'])}; {TX(p50['per_tx'])} / {TX(p200['per_tx'])} / {TX(p450['per_tx'])}; at 200K tranche 1 = {Mn(p200['t1'])} x {P2(t1r)} = {usd(p200['t1']*t1r)}; at 450K tranche 1 {Mn(p450['t1'])} x {P2(t1r)} = {usd(p450['t1']*t1r)} + tranche 2 {Mn(p450['t2'])} x {P2(t2r)} = {usd(p450['t2']*t2r)}.")
A("- \"1,000+\" is the y.uno figure for payment methods, PSPs and fraud solutions combined; do not split it into separate provider and method counts.")
A("- No em dashes and no spaced hyphens as punctuation anywhere. Use \"·\", commas, colons.")
open(BASE + "proposal_slide_content.md", "w").write("\n".join(L) + "\n")

# =====================================================================
# pricing_internal.md
# =====================================================================
L = []
A = L.append
ma, mb = JA["model"]["Base"], JS["model"]["Base"]
A("# INTERNAL · Pricing approval memo · Carry1st LatAm Shop (for Justo Benetti and Finance, 15 Oct 2026, pricing v4)\n")
A("Never in the deck, never shared with Carry1st. Prepared by German Tatis with the numbers agent. Policy references: Yuno Products Pricing Policy (Finance, Laura Galan, DRAFT WIP, read 21 Sep 2026), the Finance cheatsheet and the Pricing Calculator. Re-check the live documents before Salesforce.\n")
A("## 0. Caveats relayed from German's other session (read first)\n")
A("- The Finance Pricing Calculator (Google Sheet 1YtGixylPmxoZPe0v1YZnNlejFFcUUfcrrAZPUHofKR0) refused access to the agent. German must run V3 x gaming margin band (M3) himself before any number is quoted; the zone table in section 2 is a pre-check from the policy's own example, not the calculator's output.")
A("- The Finance cheatsheet lists pay-ins at list $0.10 / minimum $0.08 per transaction overall, which contradicts the $0.01 minimum recorded from the pricing-policy document. Section 2 shows the zones under both readings; which one Finance applies decides whether this ladder is yellow or red. Resolve with Laura Galan before quoting.")
A("- An included-TPV allotment on the platform fee is a listed but \"not preferred\" structure in the policy. It needs Salesforce approval before the quote goes out; do not send the proposal slide before that approval.")
A(f"- Pocket concessions, kept off every slide: included block widened to {band(ALT_INCL_TPV)} (worth {usd((ALT_INCL_TPV-incl)*t1r)} a month once volume passes it); launch credit {usd(INP['credit'])} x {INP['credit_months']} months (Dec 2026 to Feb 2027, {usd(INP['credit']*INP['credit_months'])} in total, billing start 1 Dec 2026); a 3-year rate lock (the v3 concession that moved the first step to $2M is already inside v4). Section 7 prices each one.\n")
A("## 1. The structure we want to quote (v4, German's decision 15 Oct 2026, authoritative)\n")
A(f"- Platform fee: $7,500 a month flat, billed annually ($90,000), including the first {band(incl)} of monthly Net TPV (single month, no rollover). Net TPV = successful transactions only, no declines, no chargebacks.")
A(f"- Usage on monthly Net TPV above the block, ladder (each band on the volume inside it): {t1r*1e4:.0f} bps from {band(incl)} to {band(t1up)}; {t2r*1e4:.0f} bps from {band(t1up)} to {band(t2up)}; {t3r*1e4:.0f} bps from {band(t2up)} to {band(t3up)}; {t4r*1e4:.0f} bps above {band(t3up)}.")
A("- Billable event: successful pay-in. Declines, verification attempts and sandbox never billed. Usage monthly in arrears, net 30. Add-ons (network tokens, 3DS) on usage, quoted separately.")
A("- Segmentation: gaming = M3 (healthy margin). Volume: V2 at launch (50K a month), V3 by the opportunity (450K a month by end 2027). Policy says size by the opportunity, so treat as V3.")
A(f"- Check figures at a ${tick:.0f} ticket: " + "; ".join(f"{INT(int(t))} tx / {Mn(pa[t]['tpv'])} = {usd(pa[t]['total'])} ({P2(pa[t]['pct'])}, {TX(pa[t]['per_tx'])} per tx)" for t in T) + f". Annual at 450K: {usd(pa[T[3]]['total']*12)}.\n")
A("## 2. Equivalent $ per transaction by tranche, and the zone it lands in\n")
A("Reading A (pricing-policy document): list $0.10, minimum $0.01. Using the proportions of the policy's own example (list $0.030, minimum $0.020: green $0.030 to $0.024, yellow $0.023 to $0.020), green runs from $0.10 down to about $0.046 and yellow from about $0.045 to $0.01. Reading B (Finance cheatsheet): list $0.10, minimum $0.08, so green about $0.10 to $0.088 and yellow $0.087 to $0.080; anything under $0.08 is red.\n")
A("| Tranche | Rate (bps) | $ per tx at $10 avg | Zone A ($0.01 min) | Zone B ($0.08 min) | $ per tx at $5 median | Zone A | Zone B | Ticket at which the rate equals $0.01 |")
A("|---|---|---|---|---|---|---|---|---|")
for name, rate in (("1 (" + band(incl) + " to " + band(t1up) + ")", t1r), ("2 (" + band(t1up) + " to " + band(t2up) + ")", t2r), ("3 (" + band(t2up) + " to " + band(t3up) + ")", t3r), ("4 (above " + band(t3up) + ")", t4r)):
    za10 = "yellow" if rate*tick > 0.01 + 1e-12 else ("on the minimum" if abs(rate*tick-0.01) < 1e-9 else "red"); za5 = "yellow" if rate*med > 0.01 else ("on the minimum" if abs(rate*med-0.01) < 1e-9 else "red")
    A(f"| {name} | {rate*1e4:.0f} | {TX4(rate*tick)} | {za10} | red | {TX4(rate*med)} | {za5} | red | ${0.01/rate:.2f} |")
A("")
A(f"Blended all-in per successful transaction (platform fee + usage): at a ${tick:.0f} ticket " + ", ".join(f"{TX4(pa[t]['per_tx'])} at {INT(int(t))}" for t in T) + f"; at a $5 ticket " + ", ".join(f"{TX4(pm[t]['per_tx'])} at {INT(int(t))}" for t in T) + f". Usage-only per transaction at the $5 median: " + ", ".join(f"{TX4(pm[t]['usage_tx'])} at {INT(int(t))}" for t in T) + ".\n")
A(f"Exposure under reading A: the {t4r*1e4:.0f} bps band (above {band(t3up)}) equals $0.010 per transaction exactly at a $10 ticket and falls under $0.01 whenever the average ticket of the billable volume is below $10.00; the {t3r*1e4:.0f} bps band crosses at ${0.01/t3r:.2f}, the {t2r*1e4:.0f} bps band at ${0.01/t2r:.2f} and the {t1r*1e4:.0f} bps band at ${0.01/t1r:.2f}. Carry1st's median is $5, so tranche 3 sits on the minimum at the median and tranche 4 under it; neither band is reached before {band(t2up)} a month. The contract therefore needs the safeguard in section 6 (option F2): usage billed at the tranche rate or $0.01 per successful transaction, whichever is higher. Under reading B every tranche is under the $0.08 minimum per transaction and the whole ladder is red (Global Controller / CFO + CRO, 5 business days), unless Finance evaluates a bps-on-TPV price against a TPV-based minimum instead; ask Laura Galan which scale applies to the % basis.\n")
A("## 3. Platform fee against the catalog\n")
A("| Reading | Figure | Comparison | Zone |")
A("|---|---|---|---|")
A("| V2 sizing (launch, 25K to 100K tx) | $7,500 | List $7,000, minimum $4,000 | above list, green |")
A("| V3 sizing (opportunity, 100K to 1M tx) | $7,500 | List $10,000, minimum $4,000 | below list, above minimum, yellow |")
A(f"| Included {band(incl)} valued at the tranche 1 rate | {usd(incl*t1r)} a month | Platform fee net of the allotment: {usd(pf-incl*t1r)} | above the $4,000 minimum, below V2 list |")
A(f"| Pocket concession: included {band(ALT_INCL_TPV)} valued at the tranche 1 rate | {usd(ALT_INCL_TPV*t1r)} a month | Platform fee net of the allotment: {usd(pf-ALT_INCL_TPV*t1r)} | above the $4,000 minimum, below V2 list |\n")
A("The policy accepts an allotment on the platform fee (\"not preferred, single-month, no rollover\"), so the structure is inside the toolkit but needs the manual review that yellow implies and Salesforce approval before the quote leaves Yuno. Billing annual upfront is standard; monthly billing of the platform fee, if Carry1st asks, is a second yellow item.\n")
A(f"Deal size check: \"overall deal size cannot be under 10k\" (the draft does not say monthly or annual). At launch the monthly bill is $7,500 ($90,000 a year); the monthly bill crosses $10,000 at about {INT((10000-pf)/t1r/tick + incl/tick)} transactions ({Mn((10000-pf)/t1r + incl)} TPV). If Finance reads the rule as monthly, ask for the exception on the strength of the ramp to {usd(pa[T[3]]['total'])} a month.\n")
A("## 4. Why bps on Net TPV is within policy as the price basis\n")
A("- Pay-ins page: price basis may be fixed $ or % of TPV; models Flat, Tranches (default) or Tiers; ranges in transactions or in TPV. We use % of TPV with tranches by TPV: the default model on an allowed basis.")
A("- TPV definition matches the policy: Net TPV of successful transactions, no declines, no chargebacks.")
A("- Units match (Justo's rule): the included block is in TPV because the usage is in bps on TPV. An allotment in transactions on a bps price is not billable without an average-ticket conversion, which is why v1 was dropped.")
A(f"- Why we need it for this merchant: average ticket ${tick:.0f}, median ${med:.0f}, with a reseller margin on GMV (take rate about {PC(INP['take'])}, to validate). A fixed $0.05 per transaction is 1.0% of TPV at the median ticket and about 7% of Carry1st's contribution on that sale; $0.10 is 2.0% and about 13%. Cordel named fixed fees as the sensitivity on the discovery call (15 Oct 2026).")
A(f"- Where it lands against the brief's corridor: Justo asked for about 0.5 to 0.7% of TPV all-in at 450K. v4 lands at {P2(pa[T[3]]['pct'])} ({BPS(rr_bps)}), below the corridor, which is what makes the conservative business case break even at {BE(be['Conservative'])} transactions a month instead of only at the run rate.\n")
A("## 5. What needs sign-off\n")
A("| Item | Why | Approver per policy | SLA |")
A("|---|---|---|---|")
A(f"| Platform fee $7,500 with a {band(incl)} Net TPV allotment | Allotment is \"not preferred\"; fee below V3 list; Salesforce approval required before the quote | RevOps / Sales Ops / GM (yellow) | 2 business days |")
A(f"| Usage rates {t1r*1e4:.0f} / {t2r*1e4:.0f} / {t3r*1e4:.0f} / {t4r*1e4:.0f} bps | Equivalent {TX4(t1r*tick)} / {TX4(t2r*tick)} / {TX4(t3r*tick)} / {TX4(t4r*tick)} at $10 and {TX4(t1r*med)} / {TX4(t2r*med)} / {TX4(t3r*med)} / {TX4(t4r*med)} at $5: yellow under the $0.01 reading, red under the $0.08 reading | RevOps / Sales Ops / GM (yellow) or Global Controller / CFO + CRO (red) | 2 or 5 business days |")
A("| bps-on-TPV basis with tranches by TPV | Allowed basis, default model; confirm the calculator reads it the same way for V3 x M3 and which per-transaction minimum applies | Finance (Laura Galan) | with the above |")
A(f"| Small-ticket exposure above {band(t2up)} a month | {t3r*1e4:.0f} bps = $0.010 at $5; {t4r*1e4:.0f} bps = $0.005 at $5 and $0.010 at $10 | Finance: contract-side safeguard (section 6, F2) | with the above |")
A("| Monthly instead of annual platform billing (only if Carry1st asks) | Yellow by policy | RevOps / Sales Ops / GM | 2 business days |")
A("| Deal size under $10K a month at launch (if read monthly) | $7,500 a month at launch | Finance | with the above |")
A(f"| Launch credit {usd(INP['credit'])} x {INP['credit_months']} months (only if used) | Credits allowed against the platform fee for named months, written in contract, no rollover; above a size threshold needs sign-off | Finance | with the above |\n")
A("## 6. Fallback if the % basis is refused\n")
A(f"Option F1, fixed $ tranches with the same yield at the ${tick:.0f} ticket (on a fixed-$ price the allotment must also be a transaction count, Justo's unit rule): the {band(incl)} block converted at the ${tick:.0f} ticket ({INT(incl/tick)} tx) as the allotment on the $7,500 platform fee; {TX4(t1r*tick)} per successful transaction to {INT(t1up/tick)}; {TX4(t2r*tick)} to {INT(t2up/tick)}; {TX4(t3r*tick)} to {INT(t3up/tick)}; {TX4(t4r*tick)} above. At 450K this bills the same {usd(pa[T[3]]['total'])} a month. The cost: at the $5 median the fee becomes {P2(t1r*tick/med)} / {P2(t2r*tick/med)} / {P2(t3r*tick/med)} / {P2(t4r*tick/med)} of TPV, exactly the fixed-fee shape Cordel objected to; expect pushback and a request for lower cents.")
A(f"Option F2, bps on Net TPV with an internal per-transaction safeguard: the same {t1r*1e4:.0f} / {t2r*1e4:.0f} / {t3r*1e4:.0f} / {t4r*1e4:.0f} bps, with the contract defining usage as \"the tranche rate, or $0.01 per successful transaction, whichever is higher\". Customer-facing text stays as in the proposal slide; the clause appears only in the contract's billing definitions. This answers the $0.01 reading; it does not answer the $0.08 reading.")
A("Option F3, tiers (cliff) instead of tranches: not recommended; the policy says tiers cede more margin and the small-ticket argument does not need them.")
A(f"Option F4, if Finance wants the allotment out: platform fee $7,000 (V2 list) with no included block, usage from the first dollar at the same rates. At 50K that bills $7,000 + {usd(incl*t1r)} = {usd(7000+incl*t1r)} a month ({P2((7000+incl*t1r)/pa[T[0]]['tpv'])} of TPV), worse for the launch story Justo asked for; use only as a last resort.\n")
A("## 7. Pocket concessions, priced (internal only)\n")
A("| Concession | Yuno revenue given a month | Where it bites | Carry1st base net at 450K | Base break-even |")
A("|---|---|---|---|---|")
A(f"| As quoted (v4): {band(incl)} included, steps at {band(t1up)}, {band(t2up)}, {band(t3up)} | 0 | reference | {K(b4['net_c'], True)} | {BE(be['Base'])} |")
A(f"| Included block to {band(ALT_INCL_TPV)} | {usd((ALT_INCL_TPV-incl)*t1r)} once TPV passes {band(ALT_INCL_TPV)} | 100K tier: Yuno {usd(JA['pricing']['avg'][T[1]]['total'])} instead of {usd(pa[T[1]]['total'])}; 450K: {usd(JA['pricing']['avg'][T[3]]['total'])} | {K(ma[T[3]]['net_c'], True)} | {BE(JA['breakeven']['Base'])} |")
A(f"| Launch credit {usd(INP['credit'])} x {INP['credit_months']} months | {usd(INP['credit']*INP['credit_months'])} in total (Dec 2026 to Feb 2027) | ramp only; Yuno over the ramp {K(rpc['Base']['yuno_total'])} instead of {K(rp['Base']['yuno_total'])} | " + (f"payback {rpc['Base']['payback']} instead of {rp['Base']['payback']}" if rpc['Base']['payback'] != rp['Base']['payback'] else f"payback unchanged ({rp['Base']['payback']}); conservative {rpc['Conservative']['payback']} instead of {rp['Conservative']['payback']}") + " | n/a |")
A("| 3-year rate lock | none today; forgoes the annual tranche review | contract term | n/a | n/a |\n")
A("## 8. Business case numbers Finance will ask about (base case, contribution view)\n")
A(f"- Yuno revenue: " + "; ".join(f"{usd(pa[t]['total'])} a month at {INT(int(t))}" for t in T) + f" ({usd(pa[T[3]]['total']*12)} a year). Over the modeled {INP['ramp_m']}-month ramp (Dec 2026 to Dec 2027, linear): {usd(rp['Base']['yuno_total'])}.")
A(f"- Carry1st net benefit after Yuno's fee: " + "; ".join(f"{usd(m['Base'][t]['net_c'])} at {INT(int(t))}" for t in T) + f" ({usd(b4['net_c']*12)} a year at 450K). Break-even {BE(be['Base'])} transactions a month; cumulative payback {rp['Base']['payback']} on the linear ramp. Conservative: break-even {BE(be['Conservative'])}, payback {rp['Conservative']['payback']}. Optimistic: break-even {BE(be['Optimistic'])}, payback {rp['Optimistic']['payback']}.")
A(f"- Switch \"Net incremental GMV of processing cost\" to 0 (GMV x take rate, the simpler view) and the base case covers the $7,500 at {BE(J['netflag0_base_breakeven'])} transactions, {usd(J['netflag0_base'][T[0]])} a month at 50K and {usd(J['netflag0_base'][T[3]])} a month at 450K. We keep the netted view as the default because a CFO-type buyer will net it anyway.")
A(f"- Option A vs Option B all-in at 450K, base: {usd(b4['a_cost'])} vs {usd(b4['b_cost'])} a month ({PK(b4['a_per_k'])} vs {PK(b4['b_per_k'])} per $1,000 TPV). The pitch to Carry1st is \"a lower cost line with failover, a second provider and local methods included; the revenue levers are on top\".\n")
A("## 9. Open items before Salesforce\n")
A("- Run the Pricing Calculator for V3 x M3 (German, access refused to the agent) and confirm the per-transaction minimum that applies to a bps-on-TPV price.")
A("- EBANX and dLocal rates through Yuno in BR, AR, MX, CO; Bolivia pay-in coverage (owner Justo / partnerships). Never quote them to Carry1st.")
A("- Cordel's EBANX direct quote: replaces the 4.5% baseline on the Inputs sheet (first thing to swap).")
A("- Volumes by country and launch scope (BR only vs all five) change the V-segment and the ramp.")
A("- Confirm with Laura Galan that an included block expressed in Net TPV on a bps price is acceptable as written, and that the allotment is approved in Salesforce before the slide is shown.")
A("- If bc_model.xlsx ever leaves Yuno, delete Inputs section 9 (launch credit switch) and this memo stays internal.")
open(BASE + "pricing_internal.md", "w").write("\n".join(L) + "\n")
print("docs generated")
