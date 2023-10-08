import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Set the rate parameter for the exponential distribution to 1
lambda_param = 1

# Generate a large sample of random numbers from an exponential distribution
sample_size = 10000
exponential_samples = np.loadtxt("random_x.txt")

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

# Create subplots for three comparisons with larger plot size
fig, axs = plt.subplots(1, 3, figsize=(20, 10))

plt.figure(figsize=(10, 10))
plt.plot(np.sort(e_minus_X), ecdf_e_minus_X, color='blue', label='CDF of e^(-X)')
plt.plot(np.sort(uniform_samples_0_to_1), ecdf_uniform_0_to_1, color='red', linestyle='--', label='CDF of Uniform (0 to 1)')
plt.xlabel('Value')
plt.ylabel('Cumulative Probability')
plt.legend()
plt.grid(True)
plt.savefig("cdf_comp_1.png")

#plt.figure(figsize=(10, 10))
plt.plot(np.sort(one_minus_e_minus_X), ecdf_one_minus_e_minus_X, color='blue', label='CDF of 1 - e^(-X)')
plt.plot(np.sort(uniform_samples_0_to_1), ecdf_uniform_0_to_1, color='red', linestyle='--', label='CDF of Uniform (0 to 1)')
plt.xlabel('Value')
plt.ylabel('Cumulative Probability')
plt.legend()
plt.grid(True)
plt.savefig("cdf_comp_2.png")

plt.figure(figsize=(10, 10))
plt.plot(np.sort(two_e_minus_X_minus_1), ecdf_two_e_minus_X_minus_1, color='blue', label='CDF of 2e^(-X) - 1')
plt.plot(np.sort(uniform_samples_minus_1_to_1), ecdf_uniform_minus_1_to_1, color='red', linestyle='--', label='CDF of Uniform (-1 to 1)')
plt.xlabel('Value')
plt.ylabel('Cumulative Probability')
plt.legend()
plt.grid(True)
plt.savefig("cdf_comp_3.png")

plt.tight_layout()


