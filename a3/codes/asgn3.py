import numpy as np

omat = np.array([[0,1],[-1,0]])
A=np.array([1,-1])
B=np.array([-4,6])
C=np.array([-3,-5])

def dir_vec(A,B):
  return B-A

def norm_vec(A,B):
  return omat@dir_vec(A,B)
  
I=(1/(np.sqrt(37) + 4 + np.sqrt(61)))*np.array([[np.sqrt(61) - 16 - 3*np.sqrt(37)],[-np.sqrt(61) + 24 - 5*np.sqrt(37)]])

n1=norm_vec(A,B)
c1=A@norm_vec(A,B)

n2=norm_vec(A,C)
c2=A@norm_vec(A,C)

def distance(I,n,c):
	r = abs((n @ I) - c)/(np.linalg.norm(n))
	return r

dist_AB=distance(I,n1,c1)
dist_AC=distance(I,n2,c2)
	
