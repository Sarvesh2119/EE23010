import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#vertices
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
  
t = norm_vec(B,C) 
n1 = t/np.linalg.norm(t) #unit normal vector
t = norm_vec(C,A)
n2 = t/np.linalg.norm(t)
t = norm_vec(A,B)
n3 = t/np.linalg.norm(t)

#slopes of angle bisectors
m_a=norm_vec(n2,n3)
m_b=norm_vec(n1,n3)
m_c=norm_vec(n1,n2)

#generating line using slope and point
def line_dir_pt(m,A,k1,k2):
  len = 10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB

def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB
  
#generating sides of triangle
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)

#generating angle bisectors
k1=[-6,-6]
k2=[6,6]  
x_A = line_dir_pt(m_a,A,k1,k2)
x_B = line_dir_pt(m_b,B,k1,k2)
x_C = line_dir_pt(m_c,C,k1,k2)

#plotting Angle bisectors
plt.plot(x_A[0,:],x_A[1,:],label='angle bisector of A')
plt.plot(x_B[0,:],x_B[1,:],label='angle bisector of B')
plt.plot(x_C[0,:],x_C[1,:],label='angle bisector of C')

#plotting sides
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')

tri_coords = np.block([[A],[B],[C]])
plt.scatter(tri_coords[:,0], tri_coords[:,1])
vert_labels = ['A','B','C']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[i,0], tri_coords[i,1]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.savefig("anglebisector.png",bbox_inches='tight')

