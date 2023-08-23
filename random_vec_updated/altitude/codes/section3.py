import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import sys
sys.path.insert(0,'/home/sarvesh/random_vec/CoordGeo')
from line.funcs import *
from triangle.funcs import alt_foot

omat = np.array([[0, 1], [-1, 0]])

#random vertices generated
A=np.array([2,-1])
B=np.array([4,3])
C=np.array([2,1])

D =  alt_foot(A,B,C)
E =  alt_foot(B,C,A)
F =  alt_foot(C,A,B)
print(f"D:{D},E:{E},F:{F}")
#parameters of altitudes
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

#point H  
H=line_intersect(n_BE,B,n_CF,C)
print(f"H:{H}")

#plot
#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
x_AD = line_gen(D,A)
x_BE = line_gen(B,E)
x_CF = line_gen(C,F)
x_CE = line_gen(C,E)
x_CD = line_gen(C,D)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_AD[0,:],x_AD[1,:],label='$AD_1$')
plt.plot(x_BE[0,:],x_BE[1,:],label='$BE_1$')
plt.plot(x_CF[0,:],x_CF[1,:],label='$CF_1$')
plt.plot(x_CE[0,:],x_CE[1,:],linestyle='dotted')
plt.plot(x_CD[0,:],x_CD[1,:],linestyle='dotted')

A = A.reshape(-1,1)
B = B.reshape(-1,1)
C = C.reshape(-1,1)
D = D.reshape(-1,1)
E = E.reshape(-1,1)
F = F.reshape(-1,1)
H = H.reshape(-1,1)
tri_coords = np.block([[A,B,C,D,E,F,H]])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C','$D_1$','$E_1$','$F_1$','H']
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

plt.savefig("altitude.png",bbox_inches='tight')
