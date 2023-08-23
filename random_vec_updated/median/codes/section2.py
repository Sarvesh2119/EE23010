import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import sys
sys.path.insert(0,'/home/sarvesh/random_vec/CoordGeo')
from line.funcs import *

omat = np.array([[0, 1], [-1, 0]])

#random vertices generated
A=np.array([2,-1])
B=np.array([4,3])
C=np.array([2,1])

#mid points
D=(B+C)/2
E=(C+A)/2
F=(A+B)/2
print(f"D,E,F are {D},{E},{F}")

#line parameters of AD,BE,CF
m_AD=dir_vec(A,D)
n_AD=norm_vec(A,D)
c_AD=norm_vec(A,D)@A
print(f"AD-m:{m_AD},n:{n_AD},c:{c_AD}")
m_BE=dir_vec(B,E)
n_BE=norm_vec(B,E)
c_BE=norm_vec(B,E)@B
print(f"BE-m:{m_BE},n:{n_BE},c:{c_BE}")
m_CF=dir_vec(C,F)
n_CF=norm_vec(C,F)
c_CF=norm_vec(C,F)@C
print(f"CF-m:{m_CF},n:{n_CF},c:{c_CF}")

#centroid
G=(A+B+C)/3
print(f"centroid is {G}")

#rank to check collinearity
Mat_AD = np.array([[1,1,1],[A[0],D[0],G[0]],[A[1],D[1],G[1]]])
rank_AD = np.linalg.matrix_rank(Mat_AD)
Mat_BE = np.array([[1,1,1],[B[0],E[0],G[0]],[B[1],E[1],G[1]]])
rank_BE = np.linalg.matrix_rank(Mat_BE)
Mat_CF= np.array([[1,1,1],[C[0],F[0],G[0]],[C[1],F[1],G[1]]])
rank_CF= np.linalg.matrix_rank(Mat_CF)
print(f"ranks are AD:{rank_AD},BE:{rank_BE},CF:{rank_CF}")

#division ratio by centroid 
r_AD=np.linalg.norm(A-G)/np.linalg.norm(G-D)
r_BE=np.linalg.norm(B-G)/np.linalg.norm(G-E)
r_CF=np.linalg.norm(C-G)/np.linalg.norm(G-F)
print(f"Ratio: {r_AD}={r_BE}={r_CF}")

#plot
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
x_AD = line_gen(A,D)
x_BE = line_gen(B,E)
x_CF = line_gen(C,F)
#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_AD[0,:],x_AD[1,:],label='$AD$')
plt.plot(x_BE[0,:],x_BE[1,:],label='$BE$')
plt.plot(x_CF[0,:],x_CF[1,:],label='$CF$')

A = A.reshape(-1,1)
B = B.reshape(-1,1)
C = C.reshape(-1,1)
D = D.reshape(-1,1)
E = E.reshape(-1,1)
F = F.reshape(-1,1)
G = G.reshape(-1,1)
tri_coords = np.block([[A,B,C,D,E,F,G]])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C','D','E','F','G']
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

plt.savefig("median.png",bbox_inches='tight')
