from scipy.stats import norm
from scipy.stats import binom
import numpy as np
from matplotlib import pyplot as plt
p = 0.2
n = 4
k = 4
sig = np.sqrt(n*p*(1-p))
print((((k-0.5)-n*p)/sig),((k+0.5)-n*p)/sig)
print("Probability from Gaussian approximation: ",norm.cdf(((k+0.5)-n*p)/sig)-norm.cdf((((k-0.5)-n*p)/sig)))
print("Probability from Binomial: ",(binom.pmf(k,n,p)))
mean = n*p
variance = np.sqrt(n*p*(1-p))

std_deviation = np.sqrt(variance)

k_values = np.arange(0, n + 1)

binom_pmf = binom.pmf(k_values, n, p)

x = np.linspace(mean - 5 * std_deviation, mean + 5 * std_deviation, 1000)

norm_pdf = norm.pdf(x, loc=mean, scale=std_deviation)

plt.figure(figsize=(10, 6))

plt.scatter(k_values, binom_pmf, label=f'Binomial (n={n}, p={p})', alpha=0.6)

plt.plot(x, norm_pdf, label=f'Normal (μ={mean}, σ²={variance})', linewidth=2)

plt.xlabel('X (Number of Successes / X-values)')
plt.ylabel('Probability / Probability Density')
plt.title('Comparison of Binomial and Normal Distributions')
plt.xticks(k_values)
plt.legend()
plt.grid(True)
plt.savefig('figure.png')
