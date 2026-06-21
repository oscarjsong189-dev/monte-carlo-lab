import numpy as np
import matplotlib.pyplot as plt

matches = 0
probabilities = []
for group_size in range(1, 101):
    matches = 0
    for i in range(10000):
        birthdays = np.random.randint(1, 366, size=group_size)
        if len(np.unique(birthdays)) < len(birthdays):
            matches += 1
    estimated_probability = matches / 10000
    probabilities.append(estimated_probability)


plt.plot(probabilities)
plt.axhline(y=0.5, color='red', linestyle='--', label='50% Probability')
plt.axvline(x=23, color='green', linestyle='--', label='23 people')
plt.xlabel('Group Size')
plt.ylabel('Estimated Probability of Shared Birthday')
plt.title('Birthday Paradox Simulation')
plt.legend()
plt.savefig('stage2_birthday_paradox.png')
plt.show()
