import numpy as np
V=np.zeros((3,2))
m=np.zeros((3,2))
c=np.zeros(3)
n=np.zeros((3,2))
#vertices
V[0]=np.array([1,-1])
V[1]=np.array([-4,6])
V[2]=np.array([-3,-5])
#slopes
m[0]=V[1]-V[0]
m[1]=V[2]-V[1]
m[2]=V[0]-V[2]
#finding a vector normal to slope
for i in range(3):
	n[i][0]=-m[i][1]
	n[i][1]=m[i][0]

for i in range(3):
	c[i]=n[i] @ V[i]

A=np.zeros((2,2))
A[0]=n[1]/np.linalg.norm(n[1]) - n[0]/np.linalg.norm(n[0])
A[1]=n[1]/np.linalg.norm(n[1]) - n[2]/np.linalg.norm(n[2])
B=np.zeros((2,1))
B[0]=c[1]/np.linalg.norm(n[1]) - c[0]/np.linalg.norm(n[0])
B[1]=c[1]/np.linalg.norm(n[1])-c[2]/np.linalg.norm(n[2])

A_inv=np.linalg.inv(A)
soln=np.zeros((2,1))
soln=np.matmul(A_inv,B)

print(soln)	
	
	
