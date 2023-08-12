import numpy as np
A=np.array([1,-1])
B=np.array([-4,6])
C=np.array([-3,-5])
 
#direction vector
def dir_vec(A,B):
  return B-A
  
#normal vectors to BE and CF 
n_BE=dir_vec(C,A)
n_CF=dir_vec(B,A)

#Intersection of two lines 
def line_intersect(n1,A1,n2,A2):
  N=np.block([[n1],[n2]])
  p = np.zeros(2)
  p[0] = n1@A1
  p[1] = n2@A2
  #Intersection
  P=np.linalg.solve(N,p)
  return P

#point H  
H=line_intersect(n_BE,B,n_CF,C)

#verification
verify=((A-H).T)@(B-C)
print(verify)
