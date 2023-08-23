import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import sys
sys.path.insert(0,'/home/sarvesh/random_vec/CoordGeo')
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

omat = np.array([[0, 1], [-1, 0]])

#random vertices generated
A=np.array([2,-1])
B=np.array([4,3])
C=np.array([2,1])

# Midpoint of each line
def midpoint(P, Q):
    return (P + Q) / 2 
    
D=midpoint(B,C)
E=midpoint(C,A)
F=midpoint(A,B) 
    
def perp_bisec(B, C):
    midBC=midpoint(B,C)
    n=dir_vec(B,C)
    m=norm_vec(B,C)
    c= n@midBC
    return m,n,c

#parameters of perpendicular bisectors
m_OD,n_OD,c_OD=perp_bisec(B,C)
print(f"m,n,c of OD : {m_OD},{n_OD},{c_OD}")
m_OE,n_OE,c_OE=perp_bisec(A,C)
print(f"m,n,c of OE : {m_OE},{n_OE},{c_OE}")
m_OF,n_OF,c_OF=perp_bisec(B,A)
print(f"m,n,c of OF : {m_OF},{n_OF},{c_OF}")

#point O 
O=line_intersect(n_OE,E,n_OF,F)
print(f"O:{O}")

#distance from vertices 
len_OA=np.linalg.norm(dir_vec(O,A))
len_OB=np.linalg.norm(dir_vec(O,B))
len_OC=np.linalg.norm(dir_vec(O,C))

print(f"the distance from vertices are OA:{len_OA},OB:{len_OB},OC:{len_OC}")

def find_Angle(O,B,C):
    dot_pt_O = (B - O) @ ((C - O).T)
    norm_pt_O = np.linalg.norm(B - O) * np.linalg.norm(C - O)
    cos_theta_O = dot_pt_O / norm_pt_O
    angle_BOC = round(np.degrees(np.arccos(cos_theta_O)),5)  #Round is used to round of number till 5 decimal places
    return angle_BOC

angle_BOC=find_Angle(O,B,C)
angle_BAC=find_Angle(A,B,C)
angle_AOC=find_Angle(O,A,C)
angle_ABC=find_Angle(B,A,C)
angle_AOB=find_Angle(O,A,B)
angle_BCA=find_Angle(C,B,A)
print(f"BOC={angle_BOC},BAC={angle_BAC}")
print(f"AOC={angle_AOC},ABC={angle_ABC}")
print(f"AOB={360-angle_AOB},BCA={angle_BCA}")
[O,r] = ccircle(A,B,C)
x_ccirc= circ_gen(O,r)
#plot
plt.plot(x_ccirc[0,:],x_ccirc[1,:],label='$circumcircle$')
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
x_OD = line_gen(O,D)
x_OE = line_gen(O,E)
x_OF = line_gen(O,F)
#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_OD[0,:],x_OD[1,:],label='$OD$')
plt.plot(x_OE[0,:],x_OE[1,:],label='$OE$')
plt.plot(x_OF[0,:],x_OF[1,:],label='$OF$')

A = A.reshape(-1,1)
B = B.reshape(-1,1)
C = C.reshape(-1,1)
D = D.reshape(-1,1)
E = E.reshape(-1,1)
F = F.reshape(-1,1)
O = O.reshape(-1,1)
tri_coords = np.block([[A,B,C,D,E,F,O]])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C','D','E','F','O']
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

plt.savefig("perp_bisec.png",bbox_inches='tight')
