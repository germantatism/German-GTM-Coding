# -*- coding: utf-8 -*-
"""Single source of truth for the Carry1st business case inputs. build_model.py (xlsx), mirror_check.py (JSON) and gen_docs.py (markdown) all import this.
Pricing v4 (German, 15 Oct 2026, authoritative; see Deals/Carry1st/build/model.py): pay-ins billed in bps on monthly Net TPV, so the included block is in TPV,
never in transactions. Platform fee $7,500 flat includes the first $500K of monthly Net TPV; ladder 40 / 30 / 20 / 10 bps with steps at $2M, $5M and $10M.
Change a number here and re-run: python3 build_model.py && python3 mirror_check.py && python3 gen_docs.py"""

INP = dict(
    ticket=10.0,              # Carry1st, Cordel, 15 Oct 2026 (estimate)
    median=5.0,               # Carry1st, Cordel, 15 Oct 2026 (estimate)
    tiers=[50000, 100000, 200000, 450000],
    take=0.15,                # ESTIMATE, to validate with Cordel
    netflag=1,                # 1 = contribution on incremental GMV nets the Option B processing cost
    base_cost=0.045, base_lo=0.03, base_hi=0.06,   # EBANX direct all-in, ESTIMATE, range 3 to 6%
    appr=0.75,                # baseline approval on a single MoR route, ESTIMATE
    wk_cost=2500.0, horizon=24,   # loaded cost per engineer-week, integrations lever only (senior payments engineer, $130K a year; Justo 15 Oct 2026: dev cost above $150K a year)
    markets=5,                # LatAm launch markets EBANX must enable, test and certify one by one (BR, AR, MX, CO, BO)
    fte_weeks=52,             # engineer-weeks in one FTE year: 52 x $2,500 = $130K a year loaded (senior payments engineer)
    # ---- Yuno cost line, pricing v4 ----
    pf=7500.0,                # platform fee a month, flat
    incl_tpv=500_000.0,       # monthly Net TPV included in the platform fee (single month, no rollover)
    t1_up=2_000_000.0, t1=0.0040,   # included block to $2M at 40 bps
    t2_up=5_000_000.0, t2=0.0030,   # $2M to $5M at 30 bps
    t3_up=10_000_000.0, t3=0.0020,  # $5M to $10M at 20 bps
    t4=0.0010,                      # above $10M at 10 bps
    fixA=0.05, fixB=0.10,     # hypothetical fixed fees for the small-ticket argument
    ramp_m=13,                # Dec 2026 to Dec 2027 (going direct: linear $0.5M to $4.5M, markets enabled one by one; also the time-to-market baseline)
    # ---- INTERNAL launch lever (never on the customer slide) ----
    credit=3750.0, credit_months=3, credit_on=0,   # $3,750 credit against the platform fee, Dec 2026 to Feb 2027, default OFF
)
SCEN = {
    # Integrations lever: mkt_weeks = engineer-weeks per market for EBANX direct (country enablement, per-country sandbox tests and certification,
    # local methods), one-time; integ x weeks = later direct integrations avoided, one-time; fte = ongoing maintenance of the direct integrations a year.
    # Time-to-market lever (model L5, deck L3): rr_m = months after Dec 2026 in which the Yuno route reaches the run rate (all five markets
    # live together on one integration); 9 = Sep 2027, 6 = Jun 2027, 4 = Apr 2027. Going direct reaches it in Dec 2027 (ramp_m - 1 = 12).
    "Conservative": dict(mdr=25, uplift=0.015, local=0.02,  mkt_weeks=3, integ=2, weeks=6, fte=1.0, rr_m=9),
    "Base":         dict(mdr=50, uplift=0.03,  local=0.04,  mkt_weeks=4, integ=3, weeks=8, fte=1.5, rr_m=6),
    "Optimistic":   dict(mdr=75, uplift=0.05,  local=0.06,  mkt_weeks=6, integ=4, weeks=10, fte=2.5, rr_m=5),
}
MONTHS = ["Dec 2026", "Jan 2027", "Feb 2027", "Mar 2027", "Apr 2027", "May 2027", "Jun 2027", "Jul 2027", "Aug 2027", "Sep 2027", "Oct 2027", "Nov 2027", "Dec 2027"]
# INTERNAL pocket concessions (kept off every slide; mirror_check.py prices them for pricing_internal.md)
ALT_INCL_TPV = 1_000_000.0    # included block widened to $1M
ALT_T1_UP = 2_000_000.0       # v3 pocket concession (30 to 25 bps step moved from $3M to $2M) is already inside v4: no-op, kept for the file layout
