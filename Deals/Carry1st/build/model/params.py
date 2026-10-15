# -*- coding: utf-8 -*-
"""Single source of truth for the Carry1st business case inputs. build_model.py (xlsx), mirror_check.py (JSON) and gen_docs.py (markdown) all import this.
Pricing v3 (German's decision, 15 Oct 2026, see Deals/Carry1st/build/model.py): pay-ins billed in bps on monthly Net TPV, so the included block is in TPV,
never in transactions. Platform fee $7,500 flat includes the first $500K of monthly Net TPV; ladder 30 / 25 / 20 bps with steps at $3M and $6M.
Change a number here and re-run: python3 build_model.py && python3 mirror_check.py && python3 gen_docs.py"""

INP = dict(
    ticket=10.0,              # Carry1st, Cordel, 15 Oct 2026 (estimate)
    median=5.0,               # Carry1st, Cordel, 15 Oct 2026 (estimate)
    tiers=[50000, 100000, 200000, 450000],
    take=0.15,                # ESTIMATE, to validate with Cordel
    netflag=1,                # 1 = contribution on incremental GMV nets the Option B processing cost
    base_cost=0.045, base_lo=0.03, base_hi=0.06,   # EBANX direct all-in, ESTIMATE, range 3 to 6%
    appr=0.75,                # baseline approval on a single MoR route, ESTIMATE
    wk_cost=2000.0, horizon=24,
    # ---- Yuno cost line, pricing v3 ----
    pf=7500.0,                # platform fee a month, flat
    incl_tpv=500_000.0,       # monthly Net TPV included in the platform fee (single month, no rollover)
    t1_up=3_000_000.0, t1=0.0030,   # included block to $3M at 30 bps
    t2_up=6_000_000.0, t2=0.0025,   # $3M to $6M at 25 bps
    t3=0.0020,                      # above $6M at 20 bps
    fixA=0.05, fixB=0.10,     # hypothetical fixed fees for the small-ticket argument
    ramp_m=13,                # Dec 2026 to Dec 2027
    # ---- INTERNAL launch lever (never on the customer slide) ----
    credit=3750.0, credit_months=3, credit_on=0,   # $3,750 credit against the platform fee, Dec 2026 to Feb 2027, default OFF
)
SCEN = {
    "Conservative": dict(mdr=25, uplift=0.015, local=0.005, integ=1, weeks=4, maint=0.20),
    "Base":         dict(mdr=50, uplift=0.03,  local=0.01,  integ=2, weeks=6, maint=0.25),
    "Optimistic":   dict(mdr=75, uplift=0.05,  local=0.02,  integ=3, weeks=8, maint=0.30),
}
MONTHS = ["Dec 2026", "Jan 2027", "Feb 2027", "Mar 2027", "Apr 2027", "May 2027", "Jun 2027", "Jul 2027", "Aug 2027", "Sep 2027", "Oct 2027", "Nov 2027", "Dec 2027"]
# INTERNAL pocket concessions (kept off every slide; mirror_check.py prices them for pricing_internal.md)
ALT_INCL_TPV = 1_000_000.0    # included block widened to $1M
ALT_T1_UP = 2_000_000.0       # 30 to 25 bps step moved from $3M to $2M
