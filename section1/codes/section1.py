import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#random vertices generated
A=np.array([2,-1])
B=np.array([4,3])
C=np.array([2,1])

def dir_vec(A,B):
    return B-A

omat = np.array([[0,1],[-1,0]])

def norm_vec(A,B):
  return omat@dir_vec(A,B)

m_AB=dir_vec(A,B)
m_BC=dir_vec(B,C)
m_CA=dir_vec(C,A)

#normal_vectors 
n_AB=norm_vec(A,B)
n_BC=norm_vec(B,C)
n_CA=norm_vec(C,A)

#c
c_AB=n_AB@A
c_BC=n_BC@B
c_CA=n_CA@C

print(f"the direction vectors are {m_AB},{m_BC},{m_CA}")
print(f"the normal vectors are {n_AB},{n_BC},{n_CA}")
print(f"the constant are {c_AB},{c_BC},{c_CA}")

#plot
def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB
  
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
