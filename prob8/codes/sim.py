import numpy as np

# Set the probabilities
a_fail= 0.2
b_fail= 0.3

# Number of simulations
num_sim = 1000

# Generate the entries
value_red = np.random.choice([0, 1], size=num_sim, p=[1 - a_fail, a_fail])
value_king = np.random.choice([0, 1], size=num_sim, p=[1 -b_fail, b_fail])

simulation = np.block([value_red[:, np.newaxis], value_king[:, np.newaxis]])

# Count the number of simulations with both elements as zeroes
zero_zero_count = np.count_nonzero((simulation == [0, 0]).all(axis=1))

desired_prob=(num_sim-zero_zero_count)/num_sim

print(f"probabaility that atleast one fail:{desired_prob}")
