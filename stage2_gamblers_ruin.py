import numpy as np
import matplotlib.pyplot as plt

rounds_to_ruin = []
outcomes = []  # 0 for ruined, 1 for won

for i in range(10000):
    balance = 10
    count = 0
    while balance > 0 and balance < 20:
        count += 1
        balance += np.random.choice([-1, 1])
    
    rounds_to_ruin.append(count)
    outcomes.append(1 if balance == 20 else 0)

# Calculate statistics
win_rate = np.sum(outcomes) / len(outcomes)
avg_rounds = np.mean(rounds_to_ruin)

print(f"Win Rate (reached $20): {win_rate:.4f}")
print(f"Average Rounds to Outcome: {avg_rounds:.2f}")

# Plot results
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Histogram of rounds
axes[0].hist(rounds_to_ruin, bins=50, edgecolor='black', alpha=0.7)
axes[0].set_xlabel('Number of Rounds')
axes[0].set_ylabel('Frequency')
axes[0].set_title("Gambler's Ruin: Rounds Until Outcome")
axes[0].axvline(x=avg_rounds, color='red', linestyle='--', label=f'Mean: {avg_rounds:.2f}')
axes[0].legend()

# Win/Loss pie chart
axes[1].pie([1-win_rate, win_rate], labels=['Ruined', 'Won'], autopct='%1.1f%%', colors=['red', 'green'])
axes[1].set_title(f"Gambler's Ruin: Outcomes")

plt.tight_layout()
plt.savefig('stage2_gamblers_ruin.png')
plt.show()