import numpy as np
import matplotlib.pyplot as plt

# Simulate coin flips and track running estimate of P(heads)
n = 10000
flips = np.random.choice([0, 1], size=n)
running_estimate = np.cumsum(flips) / np.arange(1, n + 1)

# Plot
plt.figure(figsize=(10, 5))
plt.plot(running_estimate, label='Estimated P(heads)')
plt.axhline(y=0.5, color='red', linestyle='--', label='True value (0.5)')
plt.xlabel('Number of flips')
plt.ylabel('Estimated probability')
plt.title('Law of Large Numbers — Coin Flip')
plt.legend()
plt.savefig('stage1_coin.png')
plt.show()

print(f"Final estimate after {n} flips: {running_estimate[-1]:.4f}")