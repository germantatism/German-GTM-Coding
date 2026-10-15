#!/usr/bin/env python3
"""
Carry1st LatAm Shop launch: business case model (Option A EBANX direct vs Option B EBANX + dLocal through Yuno).
Builds bc_model.xlsx with openpyxl. Every output is a formula; every assumption lives on the Inputs sheet.
Run: python3 build_model.py
"""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.comments import Comment

OUT = "/Users/germantatis/Desktop/GTMCoding/Deals/Carry1st/build/model/bc_model.xlsx"

# ---------- design system ----------
NAVY, SUB, BLUEH, GREENH, KPI, ALT = "1B3A5C", "2C4F72", "2E75B6", "375623", "F0F4FA", "F5F5F5"
WHITE, BLACK, INPUT_BLUE, LINK_GREEN, YELLOW = "FFFFFF", "000000", "0000FF", "008000", "FFFF00"
F_TITLE = Font(name="Arial", size=15, bold=True, color=WHITE)
F_SUB = Font(name="Arial", size=9, italic=True, color=WHITE)
F_HDR = Font(name="Arial", size=10, bold=True, color=WHITE)
F_LBL = Font(name="Arial", size=9)
F_LBL_B = Font(name="Arial", size=9, bold=True)
F_VAL = Font(name="Arial", size=10)
F_VAL_B = Font(name="Arial", size=10, bold=True)
F_IN = Font(name="Arial", size=10, color=INPUT_BLUE)
F_LINK = Font(name="Arial", size=10, color=LINK_GREEN)
F_KPI = Font(name="Arial", size=16, bold=True, color=NAVY)
F_KPI_LBL = Font(name="Arial", size=8, color=SUB)
F_NOTE = Font(name="Arial", size=8, italic=True, color="595959")
FILL = lambda c: PatternFill("solid", start_color=c, end_color=c)
THIN = Side(style="thin", color="BFBFBF")
BORDER = Border(top=THIN, bottom=THIN, left=THIN, right=THIN)
FMT_USD = '$#,##0;($#,##0);-'
FMT_USD1 = '$#,##0.0;($#,##0.0);-'
FMT_USD3 = '$#,##0.000;($#,##0.000);-'
FMT_PCT = '0.0%;-0.0%;-'
FMT_PCT2 = '0.00%;-0.00%;-'
FMT_INT = '#,##0;(#,##0);-'
FMT_X = '0.0"x"'

wb = Workbook()
ws_sum = wb.active
ws_sum.title = "Summary"
ws_in = wb.create_sheet("Inputs")
ws_pr = wb.create_sheet("Pricing")
ws_md = wb.create_sheet("Model")
ws_be = wb.create_sheet("BreakEven")
ws_rp = wb.create_sheet("Ramp")
ws_se = wb.create_sheet("Sensitivity")
ws_so = wb.create_sheet("Sources")


def title_bar(ws, title, subtitle, last_col):
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=last_col)
    c = ws.cell(row=1, column=1, value=title)
    c.font, c.fill, c.alignment = F_TITLE, FILL(NAVY), Alignment(vertical="center", indent=1)
    ws.row_dimensions[1].height = 36
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=last_col)
    c = ws.cell(row=2, column=1, value=subtitle)
    c.font, c.fill, c.alignment = F_SUB, FILL(SUB), Alignment(vertical="center", indent=1)
    ws.row_dimensions[2].height = 15.75
    ws.row_dimensions[3].height = 9.75


def hdr(ws, row, col, text, color=BLUEH, span=1):
    if span > 1:
        ws.merge_cells(start_row=row, start_column=col, end_row=row, end_column=col + span - 1)
    c = ws.cell(row=row, column=col, value=text)
    c.font, c.fill = F_HDR, FILL(color)
    c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[row].height = 18
    return c


def put(ws, row, col, value, font=F_VAL, fmt=None, fill=None, align=None, border=False):
    c = ws.cell(row=row, column=col, value=value)
    c.font = font
    if fmt:
        c.number_format = fmt
    if fill:
        c.fill = FILL(fill)
    if align:
        c.alignment = align
    if border:
        c.border = BORDER
    return c


# =====================================================================
# INPUTS
# =====================================================================
title_bar(ws_in, "Carry1st x Yuno · LatAm Shop launch · Inputs (single source of truth)",
          "Blue = input you can change. Yellow = ESTIMATE to validate. Green = linked. Every value carries its source or an ESTIMATE tag and an owner. USD only. 15 Oct 2026.", 8)
widths = {"A": 2, "B": 46, "C": 9, "D": 15, "E": 15, "F": 15, "G": 88, "H": 26}
for k, v in widths.items():
    ws_in.column_dimensions[k].width = v
for i, t in enumerate(["", "Assumption", "Unit", "Conservative", "Base", "Optimistic", "Source · tag", "Owner to validate"]):
    if t:
        hdr(ws_in, 4, i + 1, t)

R = {}  # key -> row on Inputs
row = 5


def section(text):
    global row
    c = put(ws_in, row, 2, text, F_LBL_B, fill="DDE6F0")
    for col in range(3, 9):
        ws_in.cell(row=row, column=col).fill = FILL("DDE6F0")
    row += 1


def inp(key, label, unit, cons, base=None, opt=None, source="", owner="", fmt=FMT_USD, estimate=False, formula=False):
    """kind: const (same in all scenarios, E/F link to D), scen (three values), derived (formula in D)."""
    global row
    R[key] = row
    put(ws_in, row, 2, label, F_LBL)
    put(ws_in, row, 3, unit, F_LBL, align=Alignment(horizontal="center"))
    if base is None and opt is None:
        c = put(ws_in, row, 4, cons, F_VAL if formula else F_IN, fmt, border=True)
        put(ws_in, row, 5, f"=D{row}", F_VAL, fmt, border=True)
        put(ws_in, row, 6, f"=D{row}", F_VAL, fmt, border=True)
        if estimate:
            c.fill = FILL(YELLOW)
    else:
        for col, v in zip((4, 5, 6), (cons, base, opt)):
            c = put(ws_in, row, col, v, F_IN, fmt, border=True)
            if estimate:
                c.fill = FILL(YELLOW)
    put(ws_in, row, 7, source, F_LBL, align=Alignment(wrap_text=True, vertical="top"))
    put(ws_in, row, 8, owner, F_LBL, align=Alignment(wrap_text=True, vertical="top"))
    ws_in.row_dimensions[row].height = 15 if len(source) < 95 else (30 if len(source) < 190 else 45)
    row += 1


section("1 · Volume and ticket (Carry1st)")
inp("ticket", "Average ticket", "USD", 10, source="Carry1st, Cordel, discovery call 15 Oct 2026 (estimate). Drives TPV = transactions x ticket.", owner="Cordel (written volumes owed)", fmt=FMT_USD1)
inp("median", "Median ticket (small-ticket sensitivity)", "USD", 5, source="Carry1st, Cordel, 15 Oct 2026 (estimate). Used on the Pricing and Sensitivity sheets only.", owner="Cordel", fmt=FMT_USD1)
inp("tier1", "Tier 1 · successful transactions a month (launch)", "tx", 50000, source="Modeling tier agreed with Justo Benetti (CRO), 15 Oct 2026. Launch volume unknown; Cordel owes volumes by country.", owner="Cordel", fmt=FMT_INT)
inp("tier2", "Tier 2 · successful transactions a month", "tx", 100000, source="Modeling tier (ramp step).", owner="", fmt=FMT_INT)
inp("tier3", "Tier 3 · successful transactions a month", "tx", 200000, source="Modeling tier (ramp step).", owner="", fmt=FMT_INT)
inp("tier4", "Tier 4 · successful transactions a month (run rate)", "tx", 450000, source="Carry1st estimate, Cordel, Oct 2026, not yet aligned internally: $4 to 5M a month in LatAm by end 2027, about 450K transactions at a $10 ticket.", owner="Cordel", fmt=FMT_INT)
inp("tpv_rr", "Run-rate TPV a month (derived)", "USD", f"=D{R['tier4']}*D{R['ticket']}", source="Derived: tier 4 x average ticket. Compare with Cordel's $4 to 5M a month (Carry1st estimate, Oct 2026).", owner="", formula=True)
inp("take", "Carry1st take rate on GMV (contribution per $1 of ticket)", "%", 0.15, source="ESTIMATE, TO VALIDATE with Cordel. Carry1st Shop resells third-party top-ups and gift cards, so its economics are a margin on GMV, not the full ticket. Public reseller benchmarks: 5 to 15% above wholesale for mainstream gift cards, 3 to 8% workable range on Google Play cards (marix.app guides, 2026).", owner="German with Cordel", fmt=FMT_PCT, estimate=True)
inp("netflag", "Net incremental GMV of processing cost? (1 = yes, 0 = no)", "flag", 1, source="Yuno modeling choice. With 1, contribution on incremental GMV = GMV x (take rate minus Option B all-in processing %). With 0, contribution = GMV x take rate (the simpler, higher view).", owner="German", fmt="0")

section("2 · Baseline provider cost (EBANX direct, cross-border MoR all-in incl. FX and local taxes passed through)")
inp("base_cost", "Baseline provider all-in cost, % of TPV  <<< REPLACE FIRST with EBANX's quote to Carry1st", "%", 0.045, source="ESTIMATE, range 3 to 6% of TPV. Anchors: dLocal FY2025 revenue / TPV = 2.68% (2.92% in 2024), a blended figure across pay-ins, pay-outs and very large merchants, so a low anchor for a $0.5 to 4.5M a month digital-goods merchant (FXC Intelligence, 26 Mar 2026, on dLocal's results of 18 Mar 2026). EBANX reviewer: about 5% per transaction plus a $200 monthly fee (Capterra, Nov 2021). FX spread of 1 to 3% on top of processing (Nuvei, 2026). Brazil IOF on FX 3.5% (Decree 12,466/2025, PayPro Global).", owner="Cordel (EBANX quote) · Justo", fmt=FMT_PCT2, estimate=True)
inp("base_cost_lo", "Baseline provider cost · low end (sensitivity)", "%", 0.03, source="Low end of the sourced range (dLocal blended take rate, large-merchant pricing).", owner="", fmt=FMT_PCT2)
inp("base_cost_hi", "Baseline provider cost · high end (sensitivity)", "%", 0.06, source="High end of the sourced range (small-ticket digital goods, FX spread and taxes passed through).", owner="", fmt=FMT_PCT2)

section("3 · Lever 1 · MDR reduction with a second provider in play")
inp("mdr_bps", "MDR reduction on total TPV (second MoR in play + routing share to the cheaper route)", "bps", 25, 50, 75, source="Yuno estimate. Brief from Justo Benetti, 15 Oct 2026. Reference ranges: multi-acquirer negotiating leverage 7.5 to 12.5 bps mid-market; cross-border to local reclassification about 60 bps (Yuno value model). 100% contribution: a cost saving, not a GMV effect.", owner="Justo · EBANX and dLocal rates through Yuno (open)", fmt="0", estimate=True)

section("4 · Lever 2 · Retries and routing recovery")
inp("appr", "Baseline approval rate on a single MoR route (blended methods)", "%", 0.75, source="ESTIMATE, range 70 to 85%. Public anchors: Mexico local acquiring 80%+ vs cross-border 50 to 60% (Nuvei, 2026); Brazil cross-border card authorization under 60% vs 90%+ on local rails (Antom, 2025); approval gap of 10 to 20 points by processing setup (Rapyd LatAm playbook, May 2026). A MoR processes locally, so 75% sits between the cross-border and local figures.", owner="Cordel (Saudi/Africa approval as proxy) · EBANX", fmt=FMT_PCT, estimate=True)
inp("uplift", "Approval uplift on attempted volume (soft-decline retries, outage failover, second-provider retry)", "pp", 0.015, 0.03, 0.05, source="Yuno estimate. Ceiling = Yuno published 7% authorization uplift (y.uno); the optimistic case stays below it. Soft declines are 80 to 90% of failed payments (Paddle); 20 to 40% of soft declines are recoverable with retries (vendor benchmarks, 2025). On a 75% baseline that supports 4 to 8 points; the model uses 1.5 / 3 / 5.", owner="Yuno (routing data after launch)", fmt=FMT_PCT, estimate=True)

section("5 · Lever 3 · Local-method coverage uplift")
inp("local", "Incremental GMV from local methods the single-provider route lacks, % of TPV", "%", 0.005, 0.01, 0.02, source="ESTIMATE. Methods carried through Yuno via dLocal and not on the EBANX connection (docs.y.uno Payment Type list, 14 Oct 2026): Argentina MODO, Rapipago, Pago Facil; Colombia Bre-B, Nequi, PSE, Efecty; Bolivia Multipago, Pago al Paso; Mexico CoDi, Paynet, 7-Eleven. Context: Pix = 42% of Brazil e-commerce value in 2025 (Worldpay GPR 2026 via Poder360); account-to-account 15% and wallets 39% of Argentina e-commerce value 2025 (GPR 2026 via LetsMoney); QR = 36% of payments in Bolivia in 2025 (Banco Central de Bolivia via Los Tiempos, Jun 2026). EBANX direct coverage per country TO VALIDATE against its quote.", owner="German · research agent (coverage)", fmt=FMT_PCT, estimate=True)

section("6 · Lever 4 · Engineering saved (one integration for five countries)")
inp("integ", "Direct integrations avoided over the horizon (dLocal as second provider, then local-entity processors)", "count", 1, 2, 3, source="Yuno estimate. Option A needs a second direct integration (dLocal) for failover and leverage, then re-integration to local processors when Phase 2 (local entities) lands. Under Option B each is a routing change. The launch integration itself is not counted (both options need one).", owner="Fatih (Carry1st tech)", fmt="0", estimate=True)
inp("weeks", "Engineer-weeks per direct PSP integration (build, certification, QA)", "weeks", 4, 6, 8, source="Server-to-server PSP integration 4 to 8 weeks; orchestration or direct acquiring 8 to 12+ weeks (spd.tech, 2026). Razorpay: 2 to 3 developer-weeks per gateway for code alone (dev.to, 2025). Gateway migration 2 to 4 weeks (mctaba.com).", owner="Fatih", fmt="0", estimate=True)
inp("wk_cost", "Loaded cost per engineer-week", "USD", 2000, source="ESTIMATE, about $104K a year loaded. Sits between Cape Town senior engineer market pay (PayScale, 2026; Carry1st engineers are in Cape Town) and LatAm loaded cost of $87.5K to $100.8K a year (Second Talent, 2026); US fully loaded is $200K to $280K (Revelo, 2026).", owner="Fatih", fmt=FMT_USD, estimate=True)
inp("maint", "Annual maintenance, % of build cost per integration", "%", 0.20, 0.25, 0.30, source="Yuno estimate; 20 to 30% upkeep is the convention used in Yuno business cases (Oct 2026).", owner="", fmt=FMT_PCT, estimate=True)
inp("horizon", "Horizon to spread one-time engineering (months)", "months", 24, source="Yuno modeling choice: build cost plus maintenance spread over 24 months, shown as a monthly equivalent.", owner="", fmt="0")

section("7 · Yuno cost line (the proposal)")
inp("pf", "Platform fee a month", "USD", 7500, source="Justo Benetti, 15 Oct 2026: $7.5K a month platform commitment with a block of transactions included.", owner="Justo · Finance (approval pending)", fmt=FMT_USD)
inp("N", "Successful transactions included in the platform fee each month", "tx", 50000, source="Proposal: equals the launch tier, so at 50K a month Carry1st pays the platform fee and nothing else. Billable TPV = TPV x max(0, 1 minus N / transactions), i.e. the TPV of the transactions above the block at the month's average ticket.", owner="Justo · Finance", fmt=FMT_INT)
inp("t1_up", "Tranche 1 · monthly TPV ceiling", "USD", 2000000, source="Proposal (ladder: each tranche applies only to the TPV inside it).", owner="Justo", fmt=FMT_USD)
inp("t1_rate", "Tranche 1 · usage rate, % of billable TPV", "%", 0.0045, source="Proposal. At a $10 ticket this is $0.045 per successful transaction; at $5, $0.0225.", owner="Justo · Finance", fmt=FMT_PCT2)
inp("t2_up", "Tranche 2 · monthly TPV ceiling", "USD", 4000000, source="Proposal.", owner="Justo", fmt=FMT_USD)
inp("t2_rate", "Tranche 2 · usage rate, % of billable TPV", "%", 0.0035, source="Proposal. $0.035 per transaction at a $10 ticket.", owner="Justo · Finance", fmt=FMT_PCT2)
inp("t3_rate", "Tranche 3 · usage rate above tranche 2, % of billable TPV", "%", 0.0030, source="Proposal. $0.030 per transaction at a $10 ticket.", owner="Justo · Finance", fmt=FMT_PCT2)
inp("fixA", "Hypothetical fixed fee A (comparison only)", "USD/tx", 0.05, source="Illustrative fixed per-transaction fee for the small-ticket argument. Not a Yuno quote.", owner="", fmt=FMT_USD3)
inp("fixB", "Hypothetical fixed fee B (comparison only)", "USD/tx", 0.10, source="Illustrative fixed per-transaction fee for the small-ticket argument. Not a Yuno quote.", owner="", fmt=FMT_USD3)

section("8 · Ramp (for payback)")
inp("ramp_m", "Ramp months, Dec 2026 (Black Friday launch) to Dec 2027", "months", 13, source="Yuno ESTIMATE: linear ramp from tier 1 at launch to tier 4 by end 2027 (Cordel's run-rate date). Replace with Cordel's written projections by country.", owner="Cordel", fmt="0", estimate=True)

ws_in.freeze_panes = "C5"
put(ws_in, row + 1, 2, "Published Yuno figures used as guardrails only (never as inputs): 7% authorization uplift and 30% recovered revenue (y.uno). Treat 7% as the ceiling for the optimistic case.", F_NOTE)
put(ws_in, row + 2, 2, "Labels: CONFIRMED (docs.y.uno or y.uno) · PUBLIC DOCS (third-party page, dated) · OPEN (not confirmed in writing, with owner) · ESTIMATE (modeled; assumption stated) · Carry1st estimate (Cordel, Oct 2026).", F_NOTE)

I = lambda key, col="E": f"Inputs!${col}${R[key]}"  # absolute reference into Inputs
SCEN_COLS = {"Conservative": "D", "Base": "E", "Optimistic": "F"}
TIERS = ["tier1", "tier2", "tier3", "tier4"]


# ---------- shared formula builders (so BreakEven, Ramp and Model use identical logic) ----------
def f_incl(tx, tpv):
    """Included TPV = min(tx, N) x TPV / tx."""
    return f"MIN({tx},{I('N')})*{tpv}/{tx}"


def f_t1(tpv, incl):
    return f"MAX(0,MIN({tpv},{I('t1_up')})-MAX(0,{incl}))"


def f_t2(tpv, incl):
    return f"MAX(0,MIN({tpv},{I('t2_up')})-MAX({I('t1_up')},{incl}))"


def f_t3(tpv, incl):
    return f"MAX(0,{tpv}-MAX({I('t2_up')},{incl}))"


def f_yuno(tpv, incl):
    return f"={I('pf')}+{f_t1(tpv, incl)}*{I('t1_rate')}+{f_t2(tpv, incl)}*{I('t2_rate')}+{f_t3(tpv, incl)}*{I('t3_rate')}"


def f_optb_pct(tpv, yuno, sc):
    return f"=({tpv}*({I('base_cost', sc)}-{I('mdr_bps', sc)}/10000)+{yuno})/{tpv}"


def f_l4(sc):
    return f"{I('integ', sc)}*{I('weeks', sc)}*{I('wk_cost', sc)}*(1+{I('maint', sc)}*{I('horizon', sc)}/12)/{I('horizon', sc)}"


def f_gross_contrib(tpv, optb, sc):
    margin = f"({I('take', sc)}-{I('netflag', sc)}*{optb})"
    return (f"={tpv}*{I('mdr_bps', sc)}/10000"
            f"+({tpv}/{I('appr', sc)}*{I('uplift', sc)}+{tpv}*{I('local', sc)})*{margin}"
            f"+{f_l4(sc)}")


# =====================================================================
# MODEL  (3 scenarios x 4 tiers = 12 columns)
# =====================================================================
title_bar(ws_md, "Model · Option A (EBANX direct) vs Option B (EBANX + dLocal through Yuno) · monthly, USD",
          "Columns = scenario x volume tier. All cells are formulas on Inputs. Contribution view = GMV levers x (take rate minus processing %) when the net flag is 1; GMV view counts the full incremental GMV.", 13)
ws_md.column_dimensions["A"].width = 58
for c in range(2, 14):
    ws_md.column_dimensions[get_column_letter(c)].width = 14
cols = []  # (col_index, scenario, tier_key)
ci = 2
for sc_name in SCEN_COLS:
    hdr(ws_md, 4, ci, sc_name, span=4, color=BLUEH if sc_name != "Base" else GREENH)
    for tk in TIERS:
        cols.append((ci, sc_name, tk))
        ci += 1
put(ws_md, 5, 1, "Successful transactions a month", F_LBL_B)
M = {}  # row keys


def mrow(key, label, bold=False, fmt=FMT_USD, section_fill=None):
    r = mrow.r
    M[key] = r
    put(ws_md, r, 1, label, F_LBL_B if bold else F_LBL, fill=section_fill)
    mrow.r += 1
    return r


mrow.r = 5
rows_spec = [
    ("tx", "Successful transactions a month", FMT_INT, True),
    ("tpv", "TPV a month (transactions x average ticket)", FMT_USD, True),
    ("hA", "OPTION A · EBANX direct", None, "section"),
    ("a_pct", "Provider all-in cost, % of TPV", FMT_PCT2, False),
    ("a_cost", "Option A total cost a month", FMT_USD, True),
    ("a_per_k", "Option A cost per $1,000 TPV", FMT_USD1, False),
    ("hB", "OPTION B · EBANX + dLocal through Yuno", None, "section"),
    ("mdr", "MDR reduction, bps of TPV", "0", False),
    ("b_prov_pct", "Provider cost after reduction, % of TPV", FMT_PCT2, False),
    ("b_prov", "Provider cost a month", FMT_USD, False),
    ("incl", "Yuno · TPV inside the included block", FMT_USD, False),
    ("t1", "Yuno · billable TPV in tranche 1", FMT_USD, False),
    ("t2", "Yuno · billable TPV in tranche 2", FMT_USD, False),
    ("t3", "Yuno · billable TPV in tranche 3", FMT_USD, False),
    ("usage", "Yuno · usage fee", FMT_USD, False),
    ("pf", "Yuno · platform fee", FMT_USD, False),
    ("yuno", "Yuno total cost a month", FMT_USD, True),
    ("yuno_pct", "Yuno cost, % of TPV", FMT_PCT2, False),
    ("yuno_tx", "Yuno cost per successful transaction", FMT_USD3, False),
    ("b_cost", "Option B total cost a month (provider + Yuno)", FMT_USD, True),
    ("b_per_k", "Option B cost per $1,000 TPV", FMT_USD1, False),
    ("b_pct", "Option B all-in, % of TPV", FMT_PCT2, False),
    ("hL", "LEVERS (monthly)", None, "section"),
    ("l1", "L1 · MDR saving (100% contribution)", FMT_USD, False),
    ("att", "Attempted volume (TPV / baseline approval)", FMT_USD, False),
    ("l2g", "L2 · retries and routing · incremental GMV", FMT_USD, False),
    ("l2c", "L2 · retries and routing · contribution", FMT_USD, False),
    ("l3g", "L3 · local methods · incremental GMV", FMT_USD, False),
    ("l3c", "L3 · local methods · contribution", FMT_USD, False),
    ("l4", "L4 · engineering saved, monthly equivalent over the horizon", FMT_USD, False),
    ("gross_c", "Gross benefit · contribution view", FMT_USD, True),
    ("gross_g", "Gross benefit · GMV view", FMT_USD, True),
    ("net_c", "Net benefit · contribution view (gross minus Yuno cost)", FMT_USD, True),
    ("net_g", "Net benefit · GMV view (gross minus Yuno cost)", FMT_USD, True),
    ("b_after_k", "Option B cost per $1,000 TPV after levers (contribution)", FMT_USD1, False),
    ("delta_k", "Advantage vs Option A per $1,000 TPV (contribution)", FMT_USD1, False),
    ("roi", "Gross contribution / Yuno cost", FMT_X, False),
    ("hY", "ANNUAL (x12 at this volume)", None, "section"),
    ("a_cost_y", "Option A cost a year", FMT_USD, False),
    ("b_cost_y", "Option B cost a year (provider + Yuno)", FMT_USD, False),
    ("yuno_y", "Yuno cost a year", FMT_USD, False),
    ("gross_c_y", "Gross benefit a year · contribution", FMT_USD, False),
    ("net_c_y", "Net benefit a year · contribution", FMT_USD, True),
    ("net_g_y", "Net benefit a year · GMV view", FMT_USD, True),
]
for key, label, fmt, kind in rows_spec:
    if kind == "section":
        r = mrow(key, label, bold=True, section_fill="DDE6F0")
        for cc in range(2, 14):
            ws_md.cell(row=r, column=cc).fill = FILL("DDE6F0")
    else:
        mrow(key, label, bold=kind)

for (c, sc_name, tk) in cols:
    sc = SCEN_COLS[sc_name]
    L = get_column_letter(c)
    cell = lambda k: f"{L}{M[k]}"
    F = {}
    F["tx"] = f"={I(tk, sc)}"
    F["tpv"] = f"={cell('tx')}*{I('ticket', sc)}"
    F["a_pct"] = f"={I('base_cost', sc)}"
    F["a_cost"] = f"={cell('tpv')}*{cell('a_pct')}"
    F["a_per_k"] = f"={cell('a_cost')}/{cell('tpv')}*1000"
    F["mdr"] = f"={I('mdr_bps', sc)}"
    F["b_prov_pct"] = f"={cell('a_pct')}-{cell('mdr')}/10000"
    F["b_prov"] = f"={cell('tpv')}*{cell('b_prov_pct')}"
    F["incl"] = "=" + f_incl(cell('tx'), cell('tpv'))
    F["t1"] = "=" + f_t1(cell('tpv'), cell('incl'))
    F["t2"] = "=" + f_t2(cell('tpv'), cell('incl'))
    F["t3"] = "=" + f_t3(cell('tpv'), cell('incl'))
    F["usage"] = f"={cell('t1')}*{I('t1_rate', sc)}+{cell('t2')}*{I('t2_rate', sc)}+{cell('t3')}*{I('t3_rate', sc)}"
    F["pf"] = f"={I('pf', sc)}"
    F["yuno"] = f"={cell('usage')}+{cell('pf')}"
    F["yuno_pct"] = f"={cell('yuno')}/{cell('tpv')}"
    F["yuno_tx"] = f"={cell('yuno')}/{cell('tx')}"
    F["b_cost"] = f"={cell('b_prov')}+{cell('yuno')}"
    F["b_per_k"] = f"={cell('b_cost')}/{cell('tpv')}*1000"
    F["b_pct"] = f"={cell('b_cost')}/{cell('tpv')}"
    F["l1"] = f"={cell('a_cost')}-{cell('b_prov')}"
    F["att"] = f"={cell('tpv')}/{I('appr', sc)}"
    F["l2g"] = f"={cell('att')}*{I('uplift', sc)}"
    F["l2c"] = f"={cell('l2g')}*({I('take', sc)}-{I('netflag', sc)}*{cell('b_pct')})"
    F["l3g"] = f"={cell('tpv')}*{I('local', sc)}"
    F["l3c"] = f"={cell('l3g')}*({I('take', sc)}-{I('netflag', sc)}*{cell('b_pct')})"
    F["l4"] = "=" + f_l4(sc)
    F["gross_c"] = f"={cell('l1')}+{cell('l2c')}+{cell('l3c')}+{cell('l4')}"
    F["gross_g"] = f"={cell('l1')}+{cell('l2g')}+{cell('l3g')}+{cell('l4')}"
    F["net_c"] = f"={cell('gross_c')}-{cell('yuno')}"
    F["net_g"] = f"={cell('gross_g')}-{cell('yuno')}"
    F["b_after_k"] = f"=({cell('b_cost')}-{cell('l2c')}-{cell('l3c')}-{cell('l4')})/{cell('tpv')}*1000"
    F["delta_k"] = f"={cell('a_per_k')}-{cell('b_after_k')}"
    F["roi"] = f"={cell('gross_c')}/{cell('yuno')}"
    F["a_cost_y"] = f"={cell('a_cost')}*12"
    F["b_cost_y"] = f"={cell('b_cost')}*12"
    F["yuno_y"] = f"={cell('yuno')}*12"
    F["gross_c_y"] = f"={cell('gross_c')}*12"
    F["net_c_y"] = f"={cell('net_c')}*12"
    F["net_g_y"] = f"={cell('net_g')}*12"
    for key, label, fmt, kind in rows_spec:
        if kind == "section":
            continue
        font = F_LINK if key in ("tx", "a_pct", "mdr", "pf") else (F_VAL_B if kind else F_VAL)
        put(ws_md, M[key], c, F[key], font, fmt, fill=(ALT if M[key] % 2 == 0 else None), border=True)
ws_md.freeze_panes = "B6"

# =====================================================================
# PRICING (the proposal, at the average and at the median ticket)
# =====================================================================
title_bar(ws_pr, "Pricing · Yuno proposal: $7,500 a month with a block of transactions included, usage above as % of TPV in tranches",
          "Billable event = successful transaction. Declines are not billed. Each tranche applies only to the TPV inside it. Add-ons (network tokens, 3DS) billed on usage and not in these totals.", 10)
ws_pr.column_dimensions["A"].width = 44
for c in range(2, 11):
    ws_pr.column_dimensions[get_column_letter(c)].width = 15
hdr(ws_pr, 4, 1, "Proposal terms", span=3)
P = 5
terms = [("Platform fee a month", f"={I('pf')}", FMT_USD),
         ("Successful transactions included each month", f"={I('N')}", FMT_INT),
         ("Tranche 1 · TPV ceiling", f"={I('t1_up')}", FMT_USD),
         ("Tranche 1 · rate", f"={I('t1_rate')}", FMT_PCT2),
         ("Tranche 2 · TPV ceiling", f"={I('t2_up')}", FMT_USD),
         ("Tranche 2 · rate", f"={I('t2_rate')}", FMT_PCT2),
         ("Tranche 3 · rate above tranche 2", f"={I('t3_rate')}", FMT_PCT2),
         ("Tranche 1 rate, $ per transaction at the average ticket", f"={I('t1_rate')}*{I('ticket')}", FMT_USD3),
         ("Tranche 2 rate, $ per transaction at the average ticket", f"={I('t2_rate')}*{I('ticket')}", FMT_USD3),
         ("Tranche 3 rate, $ per transaction at the average ticket", f"={I('t3_rate')}*{I('ticket')}", FMT_USD3),
         ("Tranche 1 rate, $ per transaction at the median ticket", f"={I('t1_rate')}*{I('median')}", FMT_USD3),
         ("Tranche 2 rate, $ per transaction at the median ticket", f"={I('t2_rate')}*{I('median')}", FMT_USD3),
         ("Tranche 3 rate, $ per transaction at the median ticket", f"={I('t3_rate')}*{I('median')}", FMT_USD3)]
for i, (lbl, f, fmt) in enumerate(terms):
    put(ws_pr, P + i, 1, lbl, F_LBL)
    put(ws_pr, P + i, 2, f, F_LINK, fmt, border=True)
PR = {}


def pricing_block(start_row, ticket_key, title):
    hdr(ws_pr, start_row, 1, title, span=5, color=GREENH)
    hdr(ws_pr, start_row + 1, 1, "Line")
    for j, tk in enumerate(TIERS):
        hdr(ws_pr, start_row + 1, 2 + j, f"={I(tk)}")
        ws_pr.cell(row=start_row + 1, column=2 + j).number_format = FMT_INT
    lines = [("tx", "Successful transactions a month", FMT_INT),
             ("tpv", "TPV a month", FMT_USD),
             ("incl", "TPV inside the included block", FMT_USD),
             ("t1", "Billable TPV · tranche 1", FMT_USD),
             ("t2", "Billable TPV · tranche 2", FMT_USD),
             ("t3", "Billable TPV · tranche 3", FMT_USD),
             ("usage", "Usage fee", FMT_USD),
             ("pf", "Platform fee", FMT_USD),
             ("total", "Yuno total a month", FMT_USD),
             ("total_y", "Yuno total a year", FMT_USD),
             ("pct", "Yuno cost, % of TPV", FMT_PCT2),
             ("per_tx", "Yuno cost per successful transaction", FMT_USD3),
             ("fixA", "Hypothetical fixed fee A a month (comparison)", FMT_USD),
             ("fixA_pct", "Fixed fee A, % of TPV", FMT_PCT2),
             ("fixB", "Hypothetical fixed fee B a month (comparison)", FMT_USD),
             ("fixB_pct", "Fixed fee B, % of TPV", FMT_PCT2),
             ("vsA", "Yuno proposal vs fixed fee A, $ a month (negative = Yuno cheaper)", FMT_USD),
             ("vsB", "Yuno proposal vs fixed fee B, $ a month (negative = Yuno cheaper)", FMT_USD)]
    rr = {}
    r = start_row + 2
    for key, lbl, fmt in lines:
        rr[key] = r
        put(ws_pr, r, 1, lbl, F_LBL_B if key in ("total", "pct", "per_tx") else F_LBL)
        r += 1
    for j, tk in enumerate(TIERS):
        L = get_column_letter(2 + j)
        c = lambda k: f"{L}{rr[k]}"
        F = {
            "tx": f"={I(tk)}",
            "tpv": f"={c('tx')}*{I(ticket_key)}",
            "incl": "=" + f_incl(c('tx'), c('tpv')),
            "t1": "=" + f_t1(c('tpv'), c('incl')),
            "t2": "=" + f_t2(c('tpv'), c('incl')),
            "t3": "=" + f_t3(c('tpv'), c('incl')),
            "usage": f"={c('t1')}*{I('t1_rate')}+{c('t2')}*{I('t2_rate')}+{c('t3')}*{I('t3_rate')}",
            "pf": f"={I('pf')}",
            "total": f"={c('usage')}+{c('pf')}",
            "total_y": f"={c('total')}*12",
            "pct": f"={c('total')}/{c('tpv')}",
            "per_tx": f"={c('total')}/{c('tx')}",
            "fixA": f"={c('tx')}*{I('fixA')}",
            "fixA_pct": f"={c('fixA')}/{c('tpv')}",
            "fixB": f"={c('tx')}*{I('fixB')}",
            "fixB_pct": f"={c('fixB')}/{c('tpv')}",
            "vsA": f"={c('total')}-{c('fixA')}",
            "vsB": f"={c('total')}-{c('fixB')}",
        }
        for key, lbl, fmt in lines:
            put(ws_pr, rr[key], 2 + j, F[key], F_VAL_B if key in ("total", "pct", "per_tx") else F_VAL, fmt,
                fill=(ALT if rr[key] % 2 == 0 else None), border=True)
    return rr, r


PR["avg"], nxt = pricing_block(P + len(terms) + 1, "ticket", "What it means for Carry1st at the AVERAGE ticket ($10)")
PR["med"], nxt = pricing_block(nxt + 1, "median", "Small-ticket view at the MEDIAN ticket ($5): same transactions, half the TPV")
put(ws_pr, nxt + 1, 1, "Reading: a fixed fee per transaction is blind to the ticket. At a $5 median, $0.05 a transaction is 1.0% of TPV and $0.10 is 2.0%. A % of TPV keeps the cost proportional to what Carry1st actually sells.", F_NOTE)

# =====================================================================
# BREAK-EVEN grid
# =====================================================================
title_bar(ws_be, "Break-even · successful transactions a month where the net benefit covers the Yuno cost (platform fee included)",
          "Grid of 5,000-transaction steps at the average ticket; break-even interpolated between the last negative and first non-negative row. Contribution view.", 18)
ws_be.column_dimensions["A"].width = 16
ws_be.column_dimensions["B"].width = 14
ws_be.column_dimensions["C"].width = 14
for c in range(4, 19):
    ws_be.column_dimensions[get_column_letter(c)].width = 13
BE_TOP = 12
STEP, NSTEP = 5000, 100
hdr(ws_be, BE_TOP - 1, 1, "Transactions")
hdr(ws_be, BE_TOP - 1, 2, "TPV")
hdr(ws_be, BE_TOP - 1, 3, "Included TPV")
be_cols = {}
c0 = 4
for sc_name in SCEN_COLS:
    hdr(ws_be, BE_TOP - 2, c0, sc_name, span=5, color=BLUEH if sc_name != "Base" else GREENH)
    for k, t in enumerate(["Yuno cost", "Option B %", "Gross contribution", "Net benefit", "Net >= 0"]):
        hdr(ws_be, BE_TOP - 1, c0 + k, t)
    be_cols[sc_name] = c0
    c0 += 5
for i in range(NSTEP):
    r = BE_TOP + i
    put(ws_be, r, 1, STEP * (i + 1), F_IN if i == 0 else F_VAL, FMT_INT)
    if i > 0:
        ws_be.cell(row=r, column=1).value = f"=A{r-1}+{STEP}"
    put(ws_be, r, 2, f"=A{r}*{I('ticket')}", F_VAL, FMT_USD)
    put(ws_be, r, 3, "=" + f_incl(f"A{r}", f"B{r}"), F_VAL, FMT_USD)
    for sc_name, sc in SCEN_COLS.items():
        c = be_cols[sc_name]
        Ly, Lp, Lg, Ln, Lf = [get_column_letter(c + k) for k in range(5)]
        put(ws_be, r, c, f_yuno(f"B{r}", f"C{r}"), F_VAL, FMT_USD)
        put(ws_be, r, c + 1, f_optb_pct(f"B{r}", f"{Ly}{r}", sc), F_VAL, FMT_PCT2)
        put(ws_be, r, c + 2, f_gross_contrib(f"B{r}", f"{Lp}{r}", sc), F_VAL, FMT_USD)
        put(ws_be, r, c + 3, f"={Lg}{r}-{Ly}{r}", F_VAL_B, FMT_USD)
        put(ws_be, r, c + 4, f"=IF({Ln}{r}>=0,1,0)", F_VAL, "0")
# summary block at top
hdr(ws_be, 4, 1, "Scenario", span=2)
hdr(ws_be, 4, 3, "Break-even tx / month", span=2)
hdr(ws_be, 4, 5, "Break-even TPV / month", span=2)
hdr(ws_be, 4, 7, "Net at tier 1", span=2)
hdr(ws_be, 4, 9, "Net at tier 4", span=2)
BE_SUM = {}
first, last = BE_TOP, BE_TOP + NSTEP - 1
for i, (sc_name, sc) in enumerate(SCEN_COLS.items()):
    r = 5 + i
    BE_SUM[sc_name] = r
    c = be_cols[sc_name]
    Ln, Lf = get_column_letter(c + 3), get_column_letter(c + 4)
    put(ws_be, r, 1, sc_name, F_LBL_B)
    idx = f"MATCH(1,{Lf}{first}:{Lf}{last},0)"
    txr = f"$A${first}:$A${last}"
    netr = f"{Ln}{first}:{Ln}{last}"
    be_formula = (f'=IFERROR(IF({idx}=1,INDEX({txr},1),'
                  f'INDEX({txr},{idx}-1)+(INDEX({txr},{idx})-INDEX({txr},{idx}-1))*(0-INDEX({netr},{idx}-1))/(INDEX({netr},{idx})-INDEX({netr},{idx}-1))),'
                  f'"above {STEP*NSTEP:,}")')
    put(ws_be, r, 3, be_formula, F_VAL_B, FMT_INT, border=True)
    put(ws_be, r, 5, f'=IFERROR(C{r}*{I("ticket")},"n/a")', F_VAL, FMT_USD, border=True)
    # net at tiers from Model
    mc1 = [cc for (cc, s, tk) in cols if s == sc_name and tk == "tier1"][0]
    mc4 = [cc for (cc, s, tk) in cols if s == sc_name and tk == "tier4"][0]
    put(ws_be, r, 7, f"=Model!{get_column_letter(mc1)}{M['net_c']}", F_LINK, FMT_USD, border=True)
    put(ws_be, r, 9, f"=Model!{get_column_letter(mc4)}{M['net_c']}", F_LINK, FMT_USD, border=True)
put(ws_be, 9, 1, "Break-even = first monthly transaction count at which L1 + L2 + L3 + L4 (contribution view) >= Yuno platform fee + usage. Below the included block, usage is zero, so the test is simply gross benefit >= $7,500.", F_NOTE)
ws_be.freeze_panes = f"B{BE_TOP}"

# =====================================================================
# RAMP (payback along Cordel's ramp)
# =====================================================================
title_bar(ws_rp, "Ramp · month by month from Black Friday 2026 to the end-2027 run rate (linear ESTIMATE) and 12 months at run rate",
          "Payback month = first month in which the cumulative net benefit (contribution view) is non-negative. No upfront fee: the only cost is the monthly Yuno bill.", 19)
ws_rp.column_dimensions["A"].width = 12
ws_rp.column_dimensions["B"].width = 14
ws_rp.column_dimensions["C"].width = 14
for c in range(4, 20):
    ws_rp.column_dimensions[get_column_letter(c)].width = 13
RP_TOP = 12
hdr(ws_rp, RP_TOP - 1, 1, "Month")
hdr(ws_rp, RP_TOP - 1, 2, "Transactions")
hdr(ws_rp, RP_TOP - 1, 3, "TPV")
rp_cols = {}
c0 = 4
for sc_name in SCEN_COLS:
    hdr(ws_rp, RP_TOP - 2, c0, sc_name, span=5, color=BLUEH if sc_name != "Base" else GREENH)
    for k, t in enumerate(["Yuno cost", "Gross contribution", "Net benefit", "Cumulative net", "Cum >= 0"]):
        hdr(ws_rp, RP_TOP - 1, c0 + k, t)
    rp_cols[sc_name] = c0
    c0 += 5
months = ["Dec 2026", "Jan 2027", "Feb 2027", "Mar 2027", "Apr 2027", "May 2027", "Jun 2027", "Jul 2027", "Aug 2027", "Sep 2027", "Oct 2027", "Nov 2027", "Dec 2027"]
NM = len(months)
for i, mlabel in enumerate(months):
    r = RP_TOP + i
    put(ws_rp, r, 1, mlabel, F_LBL)
    put(ws_rp, r, 2, f"={I('tier1')}+({I('tier4')}-{I('tier1')})*{i}/({I('ramp_m')}-1)", F_VAL, FMT_INT)
    put(ws_rp, r, 3, f"=B{r}*{I('ticket')}", F_VAL, FMT_USD)
    for sc_name, sc in SCEN_COLS.items():
        c = rp_cols[sc_name]
        Ly, Lg, Ln, Lc, Lf = [get_column_letter(c + k) for k in range(5)]
        incl = f_incl(f"B{r}", f"C{r}")
        yuno = f_yuno(f"C{r}", f"({incl})")
        put(ws_rp, r, c, yuno, F_VAL, FMT_USD)
        optb = f"(C{r}*({I('base_cost', sc)}-{I('mdr_bps', sc)}/10000)+{Ly}{r})/C{r}"
        put(ws_rp, r, c + 1, f_gross_contrib(f"C{r}", f"({optb})", sc), F_VAL, FMT_USD)
        put(ws_rp, r, c + 2, f"={Lg}{r}-{Ly}{r}", F_VAL_B, FMT_USD)
        put(ws_rp, r, c + 3, f"={Ln}{r}" if i == 0 else f"={Lc}{r-1}+{Ln}{r}", F_VAL_B, FMT_USD)
        put(ws_rp, r, c + 4, f"=IF({Lc}{r}>=0,1,0)", F_VAL, "0")
rT = RP_TOP + NM
put(ws_rp, rT, 1, "Total ramp", F_LBL_B, fill=KPI)
put(ws_rp, rT, 2, f"=SUM(B{RP_TOP}:B{rT-1})", F_VAL_B, FMT_INT, fill=KPI)
put(ws_rp, rT, 3, f"=SUM(C{RP_TOP}:C{rT-1})", F_VAL_B, FMT_USD, fill=KPI)
for sc_name in SCEN_COLS:
    c = rp_cols[sc_name]
    for k in range(3):
        L = get_column_letter(c + k)
        put(ws_rp, rT, c + k, f"=SUM({L}{RP_TOP}:{L}{rT-1})", F_VAL_B, FMT_USD, fill=KPI)
# summary
hdr(ws_rp, 4, 1, "Scenario", span=2)
hdr(ws_rp, 4, 3, "Payback month (cumulative >= 0)", span=2)
hdr(ws_rp, 4, 5, "Cumulative net over the ramp", span=2)
hdr(ws_rp, 4, 7, "Yuno cost over the ramp", span=2)
hdr(ws_rp, 4, 9, "Net a year at run rate (x12)", span=2)
RP_SUM = {}
for i, (sc_name, sc) in enumerate(SCEN_COLS.items()):
    r = 5 + i
    RP_SUM[sc_name] = r
    c = rp_cols[sc_name]
    Ly, Lg, Ln, Lc, Lf = [get_column_letter(c + k) for k in range(5)]
    put(ws_rp, r, 1, sc_name, F_LBL_B)
    put(ws_rp, r, 3, f'=IFERROR(INDEX($A${RP_TOP}:$A${rT-1},MATCH(1,{Lf}{RP_TOP}:{Lf}{rT-1},0)),"not within the ramp")', F_VAL_B, None, border=True)
    put(ws_rp, r, 5, f"={Lc}{rT-1}", F_VAL, FMT_USD, border=True)
    put(ws_rp, r, 7, f"={Ly}{rT}", F_VAL, FMT_USD, border=True)
    mc4 = [cc for (cc, s, tk) in cols if s == sc_name and tk == "tier4"][0]
    put(ws_rp, r, 9, f"=Model!{get_column_letter(mc4)}{M['net_c_y']}", F_LINK, FMT_USD, border=True)
put(ws_rp, 9, 1, "Ramp is a Yuno ESTIMATE (linear from tier 1 to tier 4 over the ramp months on Inputs). Replace the Transactions column with Cordel's written projections when they arrive.", F_NOTE)

# =====================================================================
# SENSITIVITY
# =====================================================================
title_bar(ws_se, "Sensitivity · ticket size, take rate, baseline provider cost",
          "Base scenario unless stated. Each block recomputes from Inputs; nothing typed.", 10)
ws_se.column_dimensions["A"].width = 46
for c in range(2, 11):
    ws_se.column_dimensions[get_column_letter(c)].width = 14
SE = {}
# --- A: ticket size x tier: Yuno cost, % TPV, $/tx, vs fixed fees
r = 4
hdr(ws_se, r, 1, "A · Ticket size: Yuno proposal vs hypothetical fixed fees (all tiers)", span=10, color=GREENH)
r += 1
tickets = [("$5 (median)", f"={I('median')}"), ("$10 (average)", f"={I('ticket')}"), ("$15", "=15")]
hdr(ws_se, r, 1, "Ticket · line")
for j, tk in enumerate(TIERS):
    hdr(ws_se, r, 2 + j, f"={I(tk)}")
    ws_se.cell(row=r, column=2 + j).number_format = FMT_INT
r += 1
SE["ticket_rows"] = {}
for tlabel, tform in tickets:
    put(ws_se, r, 1, f"Ticket {tlabel}", F_LBL_B, fill=KPI)
    tcell = f"$B${r}"
    put(ws_se, r, 2, tform, F_IN if tlabel == "$15" else F_LINK, FMT_USD1, fill=KPI)
    for cc in range(3, 6):
        ws_se.cell(row=r, column=cc).fill = FILL(KPI)
    ticket_row = r
    r += 1
    sub = [("tpv", "TPV a month", FMT_USD), ("yuno", "Yuno total a month", FMT_USD), ("pct", "Yuno, % of TPV", FMT_PCT2), ("ptx", "Yuno, $ per transaction", FMT_USD3),
           ("fa", "Fixed fee A a month", FMT_USD), ("fa_pct", "Fixed fee A, % of TPV", FMT_PCT2), ("fb", "Fixed fee B a month", FMT_USD), ("fb_pct", "Fixed fee B, % of TPV", FMT_PCT2)]
    rows_here = {}
    for key, lbl, fmt in sub:
        rows_here[key] = r
        put(ws_se, r, 1, "   " + lbl, F_LBL)
        r += 1
    SE["ticket_rows"][tlabel] = rows_here
    for j, tk in enumerate(TIERS):
        L = get_column_letter(2 + j)
        tx = f"{I(tk)}"
        tpv = f"{L}{rows_here['tpv']}"
        incl = f"({f_incl(tx, tpv)})"
        put(ws_se, rows_here["tpv"], 2 + j, f"={tx}*{tcell}", F_VAL, FMT_USD, border=True)
        put(ws_se, rows_here["yuno"], 2 + j, f_yuno(tpv, incl), F_VAL_B, FMT_USD, border=True)
        put(ws_se, rows_here["pct"], 2 + j, f"={L}{rows_here['yuno']}/{tpv}", F_VAL_B, FMT_PCT2, border=True)
        put(ws_se, rows_here["ptx"], 2 + j, f"={L}{rows_here['yuno']}/{tx}", F_VAL, FMT_USD3, border=True)
        put(ws_se, rows_here["fa"], 2 + j, f"={tx}*{I('fixA')}", F_VAL, FMT_USD, border=True)
        put(ws_se, rows_here["fa_pct"], 2 + j, f"={L}{rows_here['fa']}/{tpv}", F_VAL, FMT_PCT2, border=True)
        put(ws_se, rows_here["fb"], 2 + j, f"={tx}*{I('fixB')}", F_VAL, FMT_USD, border=True)
        put(ws_se, rows_here["fb_pct"], 2 + j, f"={L}{rows_here['fb']}/{tpv}", F_VAL, FMT_PCT2, border=True)
    r += 1

# --- B: take rate 10 / 15 / 25 at tier 1 and tier 4, base
hdr(ws_se, r, 1, "B · Take rate on GMV: net benefit a month, base scenario (contribution view)", span=10, color=GREENH)
r += 1
hdr(ws_se, r, 1, "Take rate")
hdr(ws_se, r, 2, "Net at tier 1")
hdr(ws_se, r, 3, "Net at tier 4")
hdr(ws_se, r, 4, "Net a year at tier 4")
hdr(ws_se, r, 5, "Gross / Yuno at tier 4")
r += 1
mcB1 = get_column_letter([cc for (cc, s, tk) in cols if s == "Base" and tk == "tier1"][0])
mcB4 = get_column_letter([cc for (cc, s, tk) in cols if s == "Base" and tk == "tier4"][0])
SE["take_rows"] = {}
for tr_label, tr_val in [("10%", 0.10), ("15% (default)", f"={I('take')}"), ("25%", 0.25)]:
    put(ws_se, r, 1, tr_val, F_LINK if isinstance(tr_val, str) else F_IN, FMT_PCT, border=True)
    SE["take_rows"][tr_label] = r
    for j, mc in enumerate([mcB1, mcB4]):
        f = (f"=Model!{mc}{M['l1']}+(Model!{mc}{M['l2g']}+Model!{mc}{M['l3g']})*($A{r}-{I('netflag')}*Model!{mc}{M['b_pct']})"
             f"+Model!{mc}{M['l4']}-Model!{mc}{M['yuno']}")
        put(ws_se, r, 2 + j, f, F_VAL_B, FMT_USD, border=True)
    put(ws_se, r, 4, f"=C{r}*12", F_VAL, FMT_USD, border=True)
    put(ws_se, r, 5, f"=(C{r}+Model!{mcB4}{M['yuno']})/Model!{mcB4}{M['yuno']}", F_VAL, FMT_X, border=True)
    r += 1
r += 1

# --- C: baseline provider cost 3 / 4.5 / 6 at tier 4, base
hdr(ws_se, r, 1, "C · Baseline provider cost: cost per $1,000 TPV and net benefit at tier 4, base scenario", span=10, color=GREENH)
r += 1
for j, t in enumerate(["Baseline cost", "Option A $/1,000", "Option B $/1,000 (provider + Yuno)", "Option B $/1,000 after levers", "Net benefit a month", "Net a year"]):
    hdr(ws_se, r, 1 + j, t)
r += 1
SE["base_rows"] = {}
for lbl, val in [("3%", f"={I('base_cost_lo')}"), ("4.5% (default)", f"={I('base_cost')}"), ("6%", f"={I('base_cost_hi')}")]:
    put(ws_se, r, 1, val, F_LINK, FMT_PCT2, border=True)
    SE["base_rows"][lbl] = r
    tpv = f"Model!{mcB4}{M['tpv']}"
    yuno = f"Model!{mcB4}{M['yuno']}"
    optb_pct = f"(($A{r}-{I('mdr_bps')}/10000)+{yuno}/{tpv})"
    put(ws_se, r, 2, f"=$A{r}*1000", F_VAL, FMT_USD1, border=True)
    put(ws_se, r, 3, f"={optb_pct}*1000", F_VAL, FMT_USD1, border=True)
    lev = f"((Model!{mcB4}{M['l2g']}+Model!{mcB4}{M['l3g']})*({I('take')}-{I('netflag')}*{optb_pct})+Model!{mcB4}{M['l4']})"
    put(ws_se, r, 4, f"=({optb_pct}*{tpv}-{lev})/{tpv}*1000", F_VAL, FMT_USD1, border=True)
    put(ws_se, r, 5, f"=Model!{mcB4}{M['l1']}+{lev}-{yuno}", F_VAL_B, FMT_USD, border=True)
    put(ws_se, r, 6, f"=E{r}*12", F_VAL, FMT_USD, border=True)
    r += 1
put(ws_se, r + 1, 1, "L1 (MDR reduction in bps) does not move with the baseline: the saving is the gap between the two routes, not the level. The baseline changes the all-in cost of both options and, through netting, the contribution on incremental GMV.", F_NOTE)

# =====================================================================
# SOURCES
# =====================================================================
title_bar(ws_so, "Sources · public benchmarks and client inputs (accessed 15 Oct 2026)", "Vendor-published figures are marked as such. Nothing here is a Yuno-negotiated rate for any merchant.", 4)
ws_so.column_dimensions["A"].width = 6
ws_so.column_dimensions["B"].width = 60
ws_so.column_dimensions["C"].width = 70
ws_so.column_dimensions["D"].width = 70
for j, t in enumerate(["#", "Source (publisher, title, date)", "What it supports", "URL"]):
    hdr(ws_so, 4, 1 + j, t)
sources = [
    ("Carry1st, discovery call with Cordel and Fatih, 15 Oct 2026 (German Tatis's summary)", "Average ticket $10, median $5; $4 to 5M a month in LatAm by end 2027 (Cordel's estimate, not aligned internally); Brazil first, then AR, MX, BO, CO; Black Friday 27 Nov 2026.", "internal"),
    ("Justo Benetti (Yuno CRO), brief for the business case, 15 Oct 2026", "$7,500 a month platform commitment with a block of transactions included; usage as % of TPV; levers MDR 25/50/75 bps; numbers tied to a low transaction count.", "internal"),
    ("FXC Intelligence, 'dLocal earnings Q4 2025', 26 Mar 2026 (on dLocal's results release of 18 Mar 2026)", "dLocal FY2025 TPV about $41B, revenue about $1.1B; revenue / TPV 2.68% in 2025 vs 2.92% in 2024 (blended pay-ins and pay-outs, all merchant sizes). Low anchor of the 3 to 6% MoR range.", "https://www.fxcintel.com/research/reports/ct-dlocal-earnings-q4-2025"),
    ("dLocal, 'dLocal Reports 2025 Fourth Quarter Financial Results', 18 Mar 2026", "Primary release behind the figures above (Q4 2025 TPV $13.1B; gross profit over TPV 0.88% in Q4 2025).", "https://dlocal.gcs-web.com/news-releases/news-release-details/dlocal-reports-2025-fourth-quarter-financial-results"),
    ("Capterra, EBANX pricing and reviews (verified review, Nov 2021)", "One merchant reports about 5% per transaction plus a $200 monthly fee; EBANX publishes no rate card. High anchor of the MoR range (vendor review, dated).", "https://www.capterra.com/p/178524/Online-Payments-in-Latin-America/pricing/"),
    ("Nuvei, 'Strategic considerations for minimizing international payment gateway fees in cross-border commerce', 2026 (vendor)", "FX spread of 1 to 3% added on top of processing; a $0.30 fixed fee is 3% of a $10 ticket.", "https://www.nuvei.com/posts/strategic-considerations-for-minimizing-international-payment-gateway-fees-in-cross-border-commerce"),
    ("PayPro Global, 'What is IOF Brazil', 2025/2026", "Decree 12,466/2025 (effective 23 May 2025) sets a flat 3.5% IOF on most FX operations; IOF is deducted in the conversion, reducing net USD per transaction.", "https://payproglobal.com/answers/what-is-iof-brazil/"),
    ("Nuvei, 'Evaluating payment strategies for the Mexican market: direct acquiring versus cross-border models', 2026 (vendor)", "Local acquiring authorization typically 80%+ vs 50 to 60% cross-border in Mexico; 20 to 30% higher with direct local acquiring.", "https://www.nuvei.com/posts/evaluating-payment-strategies-for-the-mexican-market-direct-acquiring-versus-cross-border-models"),
    ("Rapyd, 'LatAm payments playbook', May 2026 (vendor)", "Approval rates differ by 10 to 20% depending on processing setup; cross-border routing increases declines, especially on domestic debit.", "https://www.rapyd.net/wp-content/uploads/2026/05/latam-payments-playbook.pdf"),
    ("Antom, Brazil market page, 2025 (vendor)", "Brazil cross-border card authorization under 60% vs 90%+ on local rails such as Pix.", "https://www.antom.com/markets/brazil"),
    ("Paddle, 'How to prevent soft declines' (vendor)", "Soft declines are 80 to 90% of failed payments; retry timing and extra retries lift recovery.", "https://www.paddle.com/blog/how-to-prevent-soft-declines-fltr"),
    ("Spark.money glossary, 'Soft decline' (vendor)", "Smart retry and dunning recover 20 to 40% of soft-declined charges.", "https://www.spark.money/glossary/soft-decline"),
    ("Yuno, published figures (y.uno)", "7% authorization uplift; 30% recovered revenue. Used only as the ceiling for the optimistic approval case.", "https://y.uno"),
    ("Yuno docs, Payment Type list (docs.y.uno), pulled 14 Oct 2026", "Methods per provider per country as carried through Yuno: dLocal carries MODO, Rapipago, Pago Facil (AR); Bre-B, Nequi, PSE, Efecty (CO); Multipago, Pago al Paso (BO); CoDi, Paynet, 7-Eleven, OXXO, SPEI (MX); PIX, Boleto, NuPay (BR). EBANX connection: Checkout Pro (AR), PagosNet (BO), OXXO Pay, SPEI (MX), PIX, Boleto, PicPay (BR).", "https://docs.y.uno"),
    ("Poder360 citing Worldpay Global Payments Report 2026", "Pix 42% of Brazil e-commerce transaction value in 2025; cards 40%.", "https://www.poder360.com.br/poder-economia/pix-chega-a-42-dos-pagamentos-on-line-no-brasil/"),
    ("LetsMoney citing Worldpay Global Payments Report 2026", "Argentina account-to-account 15% and digital wallets 39% of e-commerce value in 2025; Mexico and Peru A2A 6%.", "https://www.letsmoney.com.br/pix/pix-lidera-conta-a-conta-america-latina/"),
    ("Los Tiempos citing Banco Central de Bolivia, 14 Jun 2026", "QR share of payments in Bolivia 36% in 2025 (15% in 2020); cash down from 85% to 64%.", "https://www.lostiempos.com/actualidad/economia/20260614/banco-central-bolivia-resalta-uso-del-qr-28-veces-segundo-pais"),
    ("spd.tech, 'Fintech payment integration timeline', 2026 (vendor)", "Hosted checkout 1 to 3 days; server-to-server integration 4 to 8 weeks; orchestration or direct acquiring 8 to 12+ weeks; approvals and credentials often take longer than the code.", "https://spd.tech/fintech-development/fintech-payment-integration-timeline/"),
    ("Razorpay engineering on dev.to, 'Gateway integration agent', 2025", "Each new gateway took 2 to 3 weeks of developer time before automation.", "https://dev.to/razorpaytech/gateway-integration-agent-how-we-cut-payment-gateway-integration-time-from-weeks-to-days-4cfk"),
    ("mctaba.com, 'Total cost of ownership: gateway fees vs engineering time'", "Migrating to a new gateway takes 2 to 4 weeks of engineering plus token migration and webhook rewrites.", "https://mctaba.com/learn/paystack/total-cost-of-ownership-gateway-fees-vs-engineering-time"),
    ("Revelo, 'Senior engineer cost benchmarks: US vs abroad', 2026 (vendor)", "US fully loaded senior engineer $200K to $280K a year; LatAm seniors working for US companies $45K to $95K.", "https://www.revelo.com/blog/senior-engineer-cost-benchmarks-us-vs-abroad"),
    ("Second Talent, 'LATAM vs CEE vs APAC for hiring AI engineers', 2026 (vendor)", "LatAm loaded cost about $87.5K a year; Brazil $100.8K; Mexico $87.8K (statutory costs in).", "https://www.secondtalent.com/latam-vs-cee-vs-apac-ai-talent/"),
    ("PayScale, 'Senior Software Engineer salary, Cape Town', 2026", "Market pay reference for Carry1st's Cape Town engineering base (below the LatAm loaded figures once converted).", "https://www.payscale.com/research/ZA/Job=Senior_Software_Engineer/Salary/2eb077be/Cape-Town"),
    ("marix.app guides, gift-card reselling margins, 2026 (vendor)", "Mainstream gift cards resell at 5 to 15% above wholesale; Google Play cards 3 to 8% workable range. Context for the 15% take-rate ESTIMATE.", "https://marix.app/library/guides/google-play-pricing-strategy"),
    ("Yuno value model (internal reference, yuno-sales-deck skill)", "Multi-acquirer leverage 7.5 to 12.5 bps mid-market; cross-border to local reclassification about 60 bps; 20 to 30% maintenance convention.", "internal"),
]
for i, (s, w, u) in enumerate(sources):
    r = 5 + i
    put(ws_so, r, 1, i + 1, F_VAL, "0", align=Alignment(horizontal="center", vertical="top"))
    put(ws_so, r, 2, s, F_LBL, align=Alignment(wrap_text=True, vertical="top"))
    put(ws_so, r, 3, w, F_LBL, align=Alignment(wrap_text=True, vertical="top"))
    put(ws_so, r, 4, u, F_LBL, align=Alignment(wrap_text=True, vertical="top"))
    ws_so.row_dimensions[r].height = 42

# =====================================================================
# SUMMARY (built last; everything linked)
# =====================================================================
title_bar(ws_sum, "Carry1st x Yuno · LatAm Shop launch · Business case summary",
          "Brazil, Argentina, Mexico, Bolivia, Colombia · EBANX direct vs EBANX + dLocal through Yuno · $10 average ticket, $5 median · USD · Confidential, prepared for Carry1st, 15 Oct 2026", 8)
for k, v in {"A": 2, "B": 30, "C": 18, "D": 14, "E": 14, "F": 14, "G": 14, "H": 2}.items():
    ws_sum.column_dimensions[k].width = v
mB = {tk: get_column_letter([cc for (cc, s, t) in cols if s == "Base" and t == tk][0]) for tk in TIERS}
mC = {tk: get_column_letter([cc for (cc, s, t) in cols if s == "Conservative" and t == tk][0]) for tk in TIERS}
mO = {tk: get_column_letter([cc for (cc, s, t) in cols if s == "Optimistic" and t == tk][0]) for tk in TIERS}
kpis = [("Run-rate transactions / month", f"=Model!{mB['tier4']}{M['tx']}", FMT_INT),
        ("Run-rate TPV / year", f"=Model!{mB['tier4']}{M['tpv']}*12", FMT_USD),
        ("Option A cost / year (run rate)", f"=Model!{mB['tier4']}{M['a_cost_y']}", FMT_USD),
        ("Option B cost / year (provider + Yuno)", f"=Model!{mB['tier4']}{M['b_cost_y']}", FMT_USD),
        ("Net benefit / year, base (contribution)", f"=Model!{mB['tier4']}{M['net_c_y']}", FMT_USD),
        ("Break-even tx / month, base", f"=BreakEven!C{BE_SUM['Base']}", FMT_INT)]
for j, (lbl, f, fmt) in enumerate(kpis):
    c = 2 + j
    put(ws_sum, 4, c, lbl, F_KPI_LBL, fill=KPI, align=Alignment(wrap_text=True, horizontal="center", vertical="center"))
    put(ws_sum, 5, c, f, F_KPI, fmt, fill=KPI, align=Alignment(horizontal="center"))
ws_sum.row_dimensions[4].height = 26
ws_sum.row_dimensions[5].height = 28
# section: four tiers, base
hdr(ws_sum, 7, 2, "Base scenario by volume tier (monthly)", span=2)
for j, tk in enumerate(TIERS):
    hdr(ws_sum, 7, 4 + j, f"=Inputs!$D${R[tk]}")
    ws_sum.cell(row=7, column=4 + j).number_format = FMT_INT
lines = [("TPV a month", "tpv", FMT_USD), ("Option A cost", "a_cost", FMT_USD), ("Option B cost (provider + Yuno)", "b_cost", FMT_USD),
         ("of which Yuno", "yuno", FMT_USD), ("Yuno, % of TPV", "yuno_pct", FMT_PCT2), ("Option A, $ per $1,000 TPV", "a_per_k", FMT_USD1),
         ("Option B, $ per $1,000 TPV", "b_per_k", FMT_USD1), ("Option B after levers, $ per $1,000", "b_after_k", FMT_USD1),
         ("Gross benefit (contribution)", "gross_c", FMT_USD), ("Net benefit (contribution)", "net_c", FMT_USD), ("Net benefit (GMV view)", "net_g", FMT_USD)]
r = 8
for lbl, key, fmt in lines:
    put(ws_sum, r, 2, lbl, F_LBL_B if key.startswith("net") else F_LBL, fill=(ALT if r % 2 == 0 else None))
    ws_sum.merge_cells(start_row=r, start_column=2, end_row=r, end_column=3)
    for j, tk in enumerate(TIERS):
        put(ws_sum, r, 4 + j, f"=Model!{mB[tk]}{M[key]}", F_VAL_B if key.startswith("net") else F_VAL, fmt, fill=(ALT if r % 2 == 0 else None), border=True)
    r += 1
r += 1
hdr(ws_sum, r, 2, "Three scenarios (contribution view)", span=2, color=GREENH)
for j, t in enumerate(["Conservative", "Base", "Optimistic"]):
    hdr(ws_sum, r, 4 + j, t, color=GREENH)
r += 1
scen_lines = [("Net a month at launch (tier 1)", "tier1", "net_c", FMT_USD, False),
              ("Net a month at run rate (tier 4)", "tier4", "net_c", FMT_USD, False),
              ("Net a year at run rate", "tier4", "net_c_y", FMT_USD, True),
              ("Gross / Yuno cost at run rate", "tier4", "roi", FMT_X, False)]
for lbl, tk, key, fmt, bold in scen_lines:
    put(ws_sum, r, 2, lbl, F_LBL_B if bold else F_LBL)
    ws_sum.merge_cells(start_row=r, start_column=2, end_row=r, end_column=3)
    for j, mm in enumerate([mC, mB, mO]):
        put(ws_sum, r, 4 + j, f"=Model!{mm[tk]}{M[key]}", F_VAL_B if bold else F_VAL, fmt, border=True)
    r += 1
put(ws_sum, r, 2, "Break-even transactions a month", F_LBL_B)
ws_sum.merge_cells(start_row=r, start_column=2, end_row=r, end_column=3)
for j, sc_name in enumerate(SCEN_COLS):
    put(ws_sum, r, 4 + j, f"=BreakEven!C{BE_SUM[sc_name]}", F_VAL_B, FMT_INT, border=True)
r += 1
put(ws_sum, r, 2, "Payback month on the ramp", F_LBL)
ws_sum.merge_cells(start_row=r, start_column=2, end_row=r, end_column=3)
for j, sc_name in enumerate(SCEN_COLS):
    put(ws_sum, r, 4 + j, f"=Ramp!C{RP_SUM[sc_name]}", F_VAL, None, border=True)
r += 2
put(ws_sum, r, 2, "How to read: Option A = EBANX direct at the baseline all-in cost (ESTIMATE until EBANX's quote replaces Inputs row for the baseline). Option B = EBANX primary + dLocal second MoR through Yuno; its provider cost is the baseline minus the MDR reduction, plus Yuno's platform fee and usage. Levers: L1 MDR saving (100% contribution), L2 retries and routing, L3 local methods, L4 engineering saved. Contribution view nets the take rate and processing cost on incremental GMV. Yuno-wide figures used only as guardrails: 7% authorization uplift, 30% recovered revenue (y.uno).", F_NOTE, align=Alignment(wrap_text=True, vertical="top"))
ws_sum.merge_cells(start_row=r, start_column=2, end_row=r + 3, end_column=7)
ws_sum.row_dimensions[r].height = 15

wb.calculation.fullCalcOnLoad = True  # openpyxl writes no cached values; force Excel / Sheets to compute on open
wb.save(OUT)
print("saved", OUT)
print("INPUT_ROWS", R)
print("MODEL_ROWS", M)
print("BE_SUM", BE_SUM, "RP_SUM", RP_SUM, "BE_TOP", BE_TOP, "RP_TOP", RP_TOP)
print("PRICING_ROWS", PR)
print("SENS", SE)
