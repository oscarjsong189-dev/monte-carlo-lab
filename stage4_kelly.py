import numpy as np
import matplotlib.pyplot as plt

p = 0.55              # probability of winning each bet
b = 1                 # payout odds — win 1x your stake, lose 1x your stake
n_bets = 200           # number of bets in a sequence
starting_bankroll = 100
stake_fractions = [0.05, 0.1, 0.25, 0.5]   # % of current bankroll staked each bet

def simulate_bankroll(f, p, b, n_bets, start):
    bankroll = np.zeros(n_bets + 1)
    bankroll[0] = start
    for i in range(1, n_bets + 1):
        if np.random.random() < p:
            bankroll[i] = bankroll[i-1] * (1 + f * b)
        else:
            bankroll[i] = bankroll[i-1] * (1 - f)
    return bankroll

plt.figure(figsize=(10, 6))
colors = plt.cm.viridis(np.linspace(0, 1, len(stake_fractions)))

for idx, f in enumerate(stake_fractions):
    for j in range(10):
        path = simulate_bankroll(f, p, b, n_bets, starting_bankroll)
        label = f"f = {f}" if j == 0 else None
        plt.plot(path, linewidth=0.7, alpha=0.6, color=colors[idx], label=label)

plt.yscale("log")
plt.xlabel("Bet number")
plt.ylabel("Bankroll (log scale)")
plt.legend()
plt.title("Bankroll paths at different stake fractions")
plt.savefig("kelly_paths.png")
plt.show()

f_kelly = p - (1 - p) / b
print(f"Kelly-optimal stake fraction: {f_kelly:.3f}")

n_sims = 2000
ruin_threshold = 1   # count as "ruined" if bankroll falls below £1

for f in stake_fractions:
    ending_bankrolls = []
    ruin_count = 0
    for _ in range(n_sims):
        path = simulate_bankroll(f, p, b, n_bets, starting_bankroll)
        ending_bankrolls.append(path[-1])
        if path.min() < ruin_threshold:
            ruin_count += 1
    print(f"f={f}: median ending bankroll = £{np.median(ending_bankrolls):.2f}, "
          f"ruin rate = {ruin_count/n_sims*100:.1f}%")