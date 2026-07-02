import numpy as np
import matplotlib.pyplot as plt

S0 = 100        # starting stock price
mu = 0.05       # expected annual return (drift)
sigma = 0.2     # annual volatility
T = 1.0         # time horizon in years
N = 252         # number of steps (trading days in a year)
dt = T / N      # size of each time step

def simulate_gbm_path(S0, mu, sigma, T, N):
    dt = T / N
    prices = np.zeros(N + 1)
    prices[0] = S0
    for t in range(1, N + 1):
        Z = np.random.normal()
        prices[t] = prices[t-1] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z)
    return prices

plt.figure(figsize=(10, 6))
for i in range(20):
    path = simulate_gbm_path(S0, mu, sigma, T, N)
    plt.plot(path, linewidth=0.8)
plt.xlabel("Day")
plt.ylabel("Price")
plt.title("Simulated GBM price paths")
plt.savefig("stage3_gbm_paths.png")
plt.show()

#prices a call by averaging discounted payoffs across simulated end prices
def price_call_option(S0, K, r, sigma, T, n_sims):
    Z = np.random.normal(size=n_sims)
    ST = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)
    payoffs = np.maximum(ST - K, 0)
    price = np.exp(-r * T) * np.mean(payoffs)
    return price

K = 105
r = 0.03
n_sims = 100000

price = price_call_option(S0, K, r, sigma, T, n_sims)
print(f"Estimated call option price: £{price:.2f}")