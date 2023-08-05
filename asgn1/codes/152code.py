import numpy as np

#vertices
A=np.array([1,-1])
B=np.array([-4,6])
C=np.array([-3,-5])
omat = np.array([[0,1],[-1,0]]) 

def dir_vec(A,B):
  return B-A
  
def norm_vec(A,B):
  return np.matmul(omat, dir_vec(A,B))
  
t = norm_vec(B,C)
n1 = t/np.linalg.norm(t)
t = norm_vec(C,A)
n2 = t/np.linalg.norm(t)
t = norm_vec(A,B)
n3 = t/np.linalg.norm(t)

def line_intersect(n1,A1,n2,A2):
  N=np.vstack((n1,n2))
  p = np.zeros(2)
  p[0] = n1@A1
  p[1] = n2@A2
  #Intersection
  P=np.linalg.inv(N)@p
  return P

I=line_intersect(n1-n3,B,n1-n2,C)
print(I)	
	
	
