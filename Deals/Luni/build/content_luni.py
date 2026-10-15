# -*- coding: utf-8 -*-
"""Luni proposal: text per element ID on the Drive copy of 'Proposal - FlightHub + Yuno' (24 slides; Build vs. Buy section removed here).
Markup: **x** = bold run of the original element. Numbers come from model.py.
Client data: call 15-oct-2026 (Artsiom Kalianchuk). Pricing: German, 15-oct-2026."""
from model import *
K1 = 'g3c99cf7678e_0_'      # cover, S11, close
A = 'g3caca0138e4_0_'       # agenda, S5
B = 'g3fa1128e0cb_1_'       # business case S13, S14
R = 'g3f8f3224ab6_2_'       # pricing S16
H = 'h4623285e90de4e9f_0_'  # proposal title, footer, build vs buy
c50, c60, cfull = SCEN['50%'], SCEN['60%'], SCEN['full']
v50, t50 = monthly(c50); v60, t60 = monthly(c60); vf, tf = monthly(cfull); v0, t0 = monthly(APPROVED)
T = {
# S1 cover
K1+'1': 'POWERING SEAMLESS GLOBAL MONEY MOVEMENT FOR LUNI',
# S5 why partner
A+'2155': 'Why we believe Yuno is the right partner for Luni',
A+'2160': 'A DEDICATED TEAM FOR LUNI',
# S11 key advantages
K1+'28715': 'Yuno is the global payment partner to scale Luni',
K1+'28719': '**Global payment method coverage** and **leading capabilities for payment routing and orchestration** position Yuno as a best-in-class partner for Luni',
K1+'28722': 'Stripe and Paddle stay, Yuno routes across them',
K1+'28726': 'Local routes for European cards and new methods',
# S13 value levers
B+'2704': f'On {ATTEMPTS:,} monthly payment attempts at an ${TICKET} ticket, every 10 points of approval are worth about ${L1[0]/1e6:.1f}M a year',
B+'1941': 'Approval uplift', B+'1945': 'Checkout & methods', B+'1949': 'Processing cost', B+'1953': 'Integrations avoided',
B+'1958': f'+{int(L1_PTS[0]*100)} to +{int(L1_PTS[1]*100)} pts', B+'1961': f'+{int(L2_PCT[0]*100)}% to +{int(L2_PCT[1]*100)}%',
B+'1964': f'{L3_BPS[0]} to {L3_BPS[1]} bps', B+'1967': f'{NEW[0]} to {NEW[1]} integrations',
B+'1959': 'Every attempt goes to one Stripe account today, and European cards are processed cross-border from it. Routing by issuer country and card type, a local route for EU cards and a second provider for recoverable declines lift approvals, while unrecoverable ones are no longer retried.',
B+'1962': 'The checkout is a basic card form with Apple Pay and Google Pay. PayPal, now being built, local methods for the markets Luni wants to open and a checkout that shows each customer the methods that work for them turn more sessions into approved payments.',
B+'1965': 'Cross-border processing adds international and currency fees on top of the base rate. Routing European cards through the French entity or a local acquirer, and picking the cheapest provider at equal approval, lowers the blended cost per transaction.',
B+'1968': f'PayPal US is being built in-house today; a European acquirer, local processing and the methods for new markets would follow, each 8 to 12 engineering weeks plus upkeep. On Yuno they are connections switched on from the dashboard, not projects.',
B+'1972': f'+{K(L1[0])}/yr', B+'1975': f'+{K(L2[0])}/yr', B+'1978': f'+{K(L3[0])}/yr', B+'1981': f'+{K(L4[0])}/yr',
B+'1984': f'+{K(L1[1])}/yr', B+'1986': f'+{K(L2[1])}/yr', B+'1988': f'+{K(L3[1])}/yr', B+'1990': f'+{K(L4[1])}/yr',
B+'1992': f'**Assumptions** All figures in USD. Base case {ATTEMPTS:,} monthly payment attempts (September, as shared by Luni) at a blended {int(APPROVAL*100)}% approval, about {APPROVED:,} approved payments a month, and an ${TICKET} average ticket, about ${TPV/1e6:.1f}M a year of approved volume. L1: +{int(L1_PTS[0]*100)} points conservative and +{int(L1_PTS[1]*100)} optimistic, {L1_PAY[0]:,} to {L1_PAY[1]:,} more approved payments a month at full ticket; part of the measured lift comes from no longer retrying unrecoverable declines. L2: +{int(L2_PCT[0]*100)}% to +{int(L2_PCT[1]*100)}% more approved payments from new methods and checkout. L3: {L3_BPS[0]} to {L3_BPS[1]} bps on approved volume. L4: {NEW[0]} to {NEW[1]} integrations at 8 to 12 engineering weeks each plus 20% to 30% yearly upkeep, at ${FTE//1000}K per engineer. Ranges are Yuno modelling assumptions, to be recalibrated with the decline breakdown by category Luni is sharing.',
# S14 total impact
B+'2174': f'On {ATTEMPTS:,} monthly payment attempts at an ${TICKET} average ticket, with approval moving from {int(APPROVAL*100)}% to 50% and 60%.',
B+'2462': 'L1 Approval', B+'2464': 'L2 Checkout', B+'2466': 'L3 Cost', B+'2468': 'L4 Integrations',
B+'2474': K(L1[0]), B+'2476': K(L2[0]), B+'2478': K(L3[0]), B+'2480': K(L4[0]), B+'2483': T(cons),
B+'2487': K(avg[0]), B+'2489': K(avg[1]), B+'2491': K(avg[2]), B+'2493': K(avg[3]), B+'2495': T(mid),
B+'2499': K(L1[1]), B+'2501': K(L2[1]), B+'2503': K(L3[1]), B+'2505': K(L4[1]), B+'2508': T(opt),
B+'2510': T(mid),
B+'2512': f'of average identifiable **annual value** across the four levers, within a {T(cons)} to {T(opt)} range, on {ATTEMPTS:,} monthly attempts at an ${TICKET} ticket, against about ${t0*12/1e3:.0f}K to ${t60*12/1e3:.0f}K a year on the proposal that follows.',
B+'2513': 'The approval lever carries it',
B+'2514': f'L1 is {avg[0]/mid:.0%} of the value. It is measured one way: approved payments divided by attempts, per provider and per market, before and after.',
B+'2515': 'Nothing here needs a rebuild',
B+'2516': 'Stripe US, Stripe France and Paddle stay. Yuno sits in front of them, and PayPal, a European acquirer or local methods become connections, live in 4 to 6 weeks.',
B+'2517': 'The baseline is yours to set',
B+'2518': f'{int(APPROVAL*100)}% is the September blended rate across the three accounts. We recalibrate every lever with the decline breakdown by category before anything is committed.',
# S16 pricing
R+'114': f'A rate per successful transaction of {int(P1*100)} cents on the first {CUT1:,} a month and {int(P2*100)} cents on the next {CUT2-CUT1:,}, with orchestration, smart routing, monitors and the PCI token vault included, on a flat platform fee of **${PLATFORM:,} a month**. You are charged only on transactions that get approved.',
R+'117': 'Tranche pricing: each tranche is billed at its own rate within the month. Declines cost nothing.',
R+'121': 'TRANCHE 1', R+'122': f'0 to {CUT1:,}',
R+'125': 'TRANCHE 2', R+'126': f'{CUT1+1:,} to {CUT2:,}',
R+'129': f'50% APPROVAL · {c50:,} SUCCESSFUL / MONTH', R+'130': f'+{c50-APPROVED:,} payments, +${(c50-APPROVED)*TICKET//1000}K a month',
R+'133': f'60% APPROVAL · {c60:,} SUCCESSFUL / MONTH', R+'134': f'+{c60-APPROVED:,} payments, +${(c60-APPROVED)*TICKET//1000}K a month',
R+'137': f'TRANCHE 2 FULLY USED · {cfull:,} SUCCESSFUL', R+'138': f'${tf/cfull:.2f} all-in per successful trx',
R+'141': f"No setup fee. Above {CUT2:,} successful transactions a month, the next tranche is set together as Luni's volume grows.",
R+'173': f'${PLATFORM:,} / month flat',
R+'176': 'WHAT IT MEANS FOR LUNI',
R+'177': f"At {APPROVED:,} successful trx / month, today's {ATTEMPTS:,} attempts at {int(APPROVAL*100)}%",
R+'182': f'{APPROVED:,} trx, all in Tranche 1 at ${P1:.2f}', R+'183': f'${v0:,.0f}', R+'184': f'${v0*12:,.0f}',
R+'187': f'${v0:,.0f}', R+'188': f'${v0*12:,.0f}',
R+'191': f'${PLATFORM:,}', R+'192': f'${PLATFORM*12:,}',
R+'195': f'${t0:,.0f}', R+'196': f'${t0*12:,.0f}',
R+'197': f'${t0:,.0f}',
R+'198': f"per month, all-in at today's volume: ${t0*12:,.0f} a year. The platform fee is {PLATFORM/t0:.0%} of it, so the bill barely moves as approvals climb.",
R+'200': 'Subscriptions engine and reconciliation below are not in these totals.',
R+'203': 'SUBSCRIPTIONS ENGINE', R+'204': "Pending review, depending on Luni's interest",
R+'206': "Recurring billing on Yuno's engine: plans and trials, **smart retries on failed renewals** and past-due recovery, on top of the routing above.",
R+'207': 'Scope and pricing to be reviewed together once Luni decides it wants it. **Not included** in the totals above.',
R+'209': 'RECONCILIATION',
R+'212': 'Automated reconciliation across **Stripe US, Stripe France, Paddle and PayPal** into one view, instead of four dashboards and settlement cycles.',
R+'213': 'Scope, timing and pricing to be reviewed together. **Not included** in the totals above.',
H+'206': 'Rates locked, tranches reviewed annually as volume grows',
}
# big number + small suffix (two runs)
T2 = {R+'123': (f'${P1:.2f}', '/trx'), R+'127': (f'${P2:.2f}', '/trx'),
      R+'131': (f'${t50:,.0f}', '/mo'), R+'135': (f'${t60:,.0f}', '/mo'), R+'139': (f'${tf:,.0f}', '/mo')}
# duplicated objects: new_id -> (source_id, (x, y, w, h), markup)
DUP = {'lu_h1': (R+'118', (42.7, 211.0, 146.3, 9.8), 'AS APPROVALS CLIMB'),
       'lu_h2': (R+'119', (178.0, 211.0, 60.8, 9.8), 'MONTHLY BILL'),
       'lu_sep0': (R+'120', (42.7, 220.5, 196.0, 0.6), None),
       'lu_tag2': (R+'204', (572.4, 347.3, 110.5, 10.7), 'Pending review')}
DELETE = [B+'1469', B+'1996', H+'948', H+'949']
SLIDES_DELETE = [H+'951', H+'956', H+'1221']          # Build vs. Buy divider + two slides
# objectId -> (x, y, w, h) pt; None keeps the current value
MOVE = {
 # S13 lever titles: wider so the full name shows; bodies taller
 B+'1941': (None, None, 100, None), B+'1945': (None, None, 100, None), B+'1949': (None, None, 100, None), B+'1953': (None, None, 100, None),
 B+'1959': (None, None, None, 68), B+'1965': (None, None, None, 68), B+'1992': (None, None, None, 32),
 # S16 left card: tranche table (rows 1 and 2 stay), scenario rows re-spaced below the second header
 R+'129': (None, 227.0, None, None), R+'130': (None, 233.2, None, None), R+'131': (165.0, 226.5, 73.8, None),
 R+'132': (None, 249.0, None, None),
 R+'133': (None, 254.0, None, None), R+'134': (None, 260.2, None, None), R+'135': (165.0, 253.5, 73.8, None),
 R+'136': (None, 276.0, None, None),
 R+'137': (None, 281.0, None, None), R+'138': (None, 287.2, None, None), R+'139': (165.0, 280.5, 73.8, None),
 R+'140': (None, 305.0, None, 24.0), R+'141': (None, 308.0, None, 18.0),
 # S16 right card: sub-line taller, bottom note wider
 R+'177': (None, None, None, 10.7), R+'198': (None, None, None, 22.0), R+'200': (None, None, 204.2, 9.6),
 # S16 bottom boxes: titles wide enough
 R+'203': (None, None, 190.0, None), R+'209': (None, None, 190.0, None),
}
LOGO = ('https://images.weserv.nl/?url=https%3A%2F%2Fimages.teamtailor-cdn.com%2Fimages%2Fs3%2Fteamtailor-production%2Flogotype-v3'
        '%2Fimage_uploads%2Fd3e15b79-1983-4c84-ad5b-d48d17b2fe7c%2Foriginal.png&filt=negate&output=png&cx=38&cy=35&cw=155&ch=60')
# (old image id, new id, box) ; logo crop 155x60 -> aspect 2.58
LOGOS = [(B+'928', 'lu_cover_logo', (123.0, 24.0, 49.0, 19.0)), (B+'929', 'lu_close_logo', (627.0, 196.0, 52.0, 20.0))]
FORBID = ['FlightHub', 'FLIGHTHUB', 'Flighthub', 'Wex', 'seven provider', 'travel', 'Travel', ' OTA', '$580', '700,000', 'Nick', 'Anna',
          'CPD', 'airline', 'Airline', 'booking', 'Nova', 'Ethoca', 'Verifi', 'Tier', 'TIER', 'tier',
          'Build vs', 'BUILD VS', 'run-ops', 'Run-ops', '$10,000', '$24,500', '$34,500', '4.87', '$26M', '$43M', '34.65', ' — ', ' - ']
# appendix S21 numeric ranges: en-dash -> 'to' (replaceAllText restricted to that slide)
RANGES = [('4–16%', '4 to 16%'), ('8–12%', '8 to 12%'), ('20–40', '20 to 40')]
RANGES_SLIDE = B+'56'
