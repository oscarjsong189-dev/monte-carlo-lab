import numpy as np
import matplotlib.pyplot as plt

n = 1000  # Number of samples

flips = np.random.choice([0, 1], size=n)  # Simulate n  coin flips (0 = tails, 1 = heads)
running_estimate = np.cumsum(flips) / np.arange(1, n + 1)  # Calculate the running estimate of the probability of heads

plt.figure(figsize=(10, 5))
plt.plot(running_estimate, label='Estimated P(heads)')
plt.axhline(y=0.5, color='red', linestyle='--', label='True value (0.5)')
plt.xlabel('Number of flips')
plt.ylabel('Estimated probability')
plt.title('Law of Large Numbers — Coin Flip')
plt.legend()
plt.savefig('stage1_coin.png')
plt.show()






k=1000 # number of rolls of dice
rolls = np.random.randint(1, 7, size=k)
number_of_rolls_1 = np.cumsum(rolls == 1)  # Calculate the number of times a 1 is rolled
running_estimate_dice = number_of_rolls_1/np.arange(1, k + 1)  #Calculate the running estimate of the average roll

plt.figure(figsize=(10, 5))
plt.plot(running_estimate_dice, label='Estimated Average Roll')
plt.axhline(y=1/6, color='red', linestyle='--', label
='True value (1/6)')
plt.xlabel('Number of rolls')
plt.ylabel('Estimated average')
plt.title('Law of Large Numbers — Dice Roll')
plt.legend()
plt.savefig('stage1_dice.png')
plt.show()
