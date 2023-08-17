import numpy as np
from scipy.stats import bernoulli

#Number of samples is 100, 1 denotes even number and 0 denotes odd number
simlen=int(100)

#Probability of the number being even i.e., X=1 is 1/2
prob = 1/2

#Generating sample date using Bernoulli r.v.
data_bern = bernoulli.rvs(size=simlen,p=prob)
#Calculating the number of even outcomes
even_num = np.nonzero(data_bern == 1)
#calculating the probability 
even_prob = np.size(even_num)/simlen
odd_prob = 1-even_prob
#Theory vs simulation
print("Even Probability-simulation,actual:",even_prob,prob)
print("Odd Probability-simulation,actual:",odd_prob,prob)
print("Samples generated:",data_bern)
