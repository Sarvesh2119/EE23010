import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Set the rate parameter for the exponential distribution to 1
lambda_param = 1

# Generate a large sample of random numbers from an exponential distribution
sample_size = 10000
exponential_samples = np.random.exponential(scale=1/lambda_param, size=sample_size)

# Calculate e^(-X) for each sample
e_minus_X = np.exp(-exponential_samples)

# Generate a sample of random numbers from a uniform distribution between 0 and 1
uniform_samples_0_to_1 = np.random.uniform(0, 1, size=sample_size)

# Calculate 1 - e^(-X)
one_minus_e_minus_X = 1 - e_minus_X

# Generate a sample of random numbers from a uniform distribution between -1 and 1
uniform_samples_minus_1_to_1 = np.random.uniform(-1, 1, size=sample_size)

# Calculate 2e^(-X) - 1
two_e_minus_X_minus_1 = 2 * e_minus_X - 1

# Calculate the CDFs
ecdf_e_minus_X = np.arange(1, len(e_minus_X) + 1) / len(e_minus_X)
ecdf_uniform_0_to_1 = np.arange(1, len(uniform_samples_0_to_1) + 1) / len(uniform_samples_0_to_1)
ecdf_one_minus_e_minus_X = np.arange(1, len(one_minus_e_minus_X) + 1) / len(one_minus_e_minus_X)
ecdf_uniform_minus_1_to_1 = np.arange(1, len(uniform_samples_minus_1_to_1) + 1) / len(uniform_samples_minus_1_to_1)
ecdf_two_e_minus_X_minus_1 = np.arange(1, len(two_e_minus_X_minus_1) + 1) / len(two_e_minus_X_minus_1)

# Create subplots for three comparisons
fig, axs = plt.subplots(1, 3, figsize=(25, 10))

# Plot the CDF of e^(-X) vs. Uniform (0 to 1)
axs[0].plot(np.sort(e_minus_X), ecdf_e_minus_X, color='blue', label='CDF of e^(-X)')
axs[0].plot(np.sort(uniform_samples_0_to_1), ecdf_uniform_0_to_1, color='red', linestyle='--', label='CDF of Uniform (0 to 1)')
axs[0].set_title('Comparison of CDF: e^(-X) vs. Uniform (0 to 1)')
axs[0].set_xlabel('Value')
axs[0].set_ylabel('Cumulative Probability')
axs[0].legend()
axs[0].grid(True)

# Plot the CDF of 1 - e^(-X) vs. Uniform (0 to 1)
axs[1].plot(np.sort(one_minus_e_minus_X), ecdf_one_minus_e_minus_X, color='blue', label='CDF of 1 - e^(-X)')
axs[1].plot(np.sort(uniform_samples_0_to_1), ecdf_uniform_0_to_1, color='red', linestyle='--', label='CDF of Uniform (0 to 1)')
axs[1].set_title('Comparison of CDF: 1 - e^(-X) vs. Uniform (0 to 1)')
axs[1].set_xlabel('Value')
axs[1].set_ylabel('Cumulative Probability')
axs[1].legend()
axs[1].grid(True)

# Plot the CDF of 2e^(-X) - 1 vs. Uniform (-1 to 1)
axs[2].plot(np.sort(two_e_minus_X_minus_1), ecdf_two_e_minus_X_minus_1, color='blue', label='CDF of 2e^(-X) - 1')
axs[2].plot(np.sort(uniform_samples_minus_1_to_1), ecdf_uniform_minus_1_to_1, color='red', linestyle='--', label='CDF of Uniform (-1 to 1)')
axs[2].set_title('Comparison of CDF: 2e^(-X) - 1 vs. Uniform (-1 to 1)')
axs[2].set_xlabel('Value')
axs[2].set_ylabel('Cumulative Probability')
axs[2].legend()
axs[2].grid(True)

plt.tight_layout()
plt.savefig("cdf_comp.png")
