import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import sys
sys.path.insert(0,'/home/sarvesh/random_vec/CoordGeo')
from line.funcs import *
#random vertices generated
A=np.array([2,-1])
B=np.array([4,3])
C=np.array([2,1])

omat = np.array([[0,1],[-1,0]])

m_AB=dir_vec(A,B)
m_BC=dir_vec(B,C)
m_CA=dir_vec(C,A)

#1.1.1 and 1.1.4
print(f"the direction vectors are {m_AB},{m_BC},{m_CA}")

#1.1.2 side length
len_BC=np.linalg.norm(m_BC)
len_AB=np.linalg.norm(m_AB)
len_CA=np.linalg.norm(m_CA)
print(f"the length of BC is {len_BC}")
print(f"the length of AB is {len_AB}")
print(f"the length of CA is {len_CA}")

#1.1.3 collinearity check
Mat = np.array([[1,1,1],[A[0],B[0],C[0]],[A[1],B[1],C[1]]])

rank = np.linalg.matrix_rank(Mat)
print(f"the rank is {rank}")
if (rank<=2):
	print("Hence proved that points A,B,C in a triangle are collinear")
else:
	print("The given points are not collinear")

#1.1.5
#normal_vectors 
n_AB=norm_vec(A,B)
n_BC=norm_vec(B,C)
n_CA=norm_vec(C,A)
#c
c_AB=n_AB@A
c_BC=n_BC@B
c_CA=n_CA@C
print(f"the normal vectors are {n_AB},{n_BC},{n_CA}")
print(f"the constant are {c_AB},{c_BC},{c_CA}")

#1.1.6 Area
cross_product = np.cross(m_AB,m_CA)
magnitude = np.linalg.norm(cross_product)
area = 0.5 * magnitude
print(f"area of triangle is{area}")

#1.1.7 angles
dotA=((B-A).T)@(C-A)
NormA=(np.linalg.norm(B-A))*(np.linalg.norm(C-A))
print('value of angle A: ', np.degrees(np.arccos((dotA)/NormA)))


dotB=(A-B).T@(C-B)
NormB=(np.linalg.norm(A-B))*(np.linalg.norm(C-B))
print('value of angle B: ', np.degrees(np.arccos((dotB)/NormB)))

dotC=(A-C).T@(B-C)
NormC=(np.linalg.norm(A-C))*(np.linalg.norm(B-C))
print('value of angle C: ', np.degrees(np.arccos((dotC)/NormC)))
#plot 
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')

A = A.reshape(-1,1)
B = B.reshape(-1,1)
C = C.reshape(-1,1)

tri_coords = np.block([[A,B,C]])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.savefig("Triangle.png",bbox_inches='tight')
