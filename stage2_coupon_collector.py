import numpy as np
import matplotlib.pyplot as plt
count = 0
counts=[]
toys = set()
for i in range(10000):
    toys = set()
    count = 0
    while len(toys) < 6:
        toys.add(np.random.randint(1, 7))
        count += 1
    counts.append(count)
np.mean(counts)
print("Average number of rolls to collect all 6 toys:", np.mean(counts))
plt.hist(counts, bins=50)

plt.xlabel('Number of Rolls')
plt.ylabel('Frequency')
plt.title('Distribution of Rolls to Collect All 6 Toys')

plt.savefig('stage2_coupon_collector.png')
plt.show()
