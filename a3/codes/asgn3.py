import numpy as np
A=np.array([1,-1])
B=np.array([-4,6])
C=np.array([-3,-5])
omat = np.array([[0,1],[-1,0]]) 

#direction vector
def dir_vec(A,B):
  return B-A
  
#normal vector 
def norm_vec(A,B):
  return omat@dir_vec(A,B)

#normal vectors to BE and CF 
n_BE=A-C
n_CF=B-A

#Intersection of two lines 
def line_intersect(n1,A1,n2,A2):
  N=np.block([[n1],[n2]])
  p = np.zeros(2)
  p[0] = n1@A1
  p[1] = n2@A2
  #Intersection
  P=np.linalg.solve(N,p)
  return P
  
H=line_intersect(n_BE,B,n_CF,C)

verify=((A-H).T)@(B-C)
print(verify)
