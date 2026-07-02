# monte-carlo-lab
Summer project

Stage 1 — Law of large numbers:
Simulated coin flips and dice rolls; estimated P(heads) and P(each face) converge to the true values (0.5, 1/6) as sample size grows.

Stage 2 — Classic interview problems:
Simulated birthday paradox, coupon collector, and gambler's ruin — all three matched analytic theory (coupon collector: 14.6 simulated vs. 14.7 theoretical; gambler's ruin: 50.3% ruin rate on a fair coin, as expected).

Stage 3 — Markets flavour:
Simulated GBM price paths and priced a European call option by Monte Carlo — result converges to the Black-Scholes closed-form price (£7.13) within ~£0.05 across repeated runs.

Stage 4 — Bet sizing & ruin:
Simulated repeated favourable bets (55% edge) at varying stake sizes — Kelly-optimal fraction (0.10) maximised median outcome (£272 vs. £100 start), while over-betting at f=0.5 gave 98% ruin despite identical edge.