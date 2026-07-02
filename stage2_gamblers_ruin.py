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

win_rate = np.sum(outcomes) / len(outcomes)
avg_rounds = np.mean(rounds_to_ruin)



print(f"Ruin probability: {1 - win_rate:.4f}")



plt .figure(figsize=(10, 5))
plt.hist(rounds_to_ruin, bins=50, alpha=0.7, color='blue')
plt.xlabel('Number of Rounds')
plt.ylabel('Frequency')
plt.title('Gamblers Ruin — Distribution of Game Length')
plt.savefig('stage2_gamblers_ruin.png')
plt.show()