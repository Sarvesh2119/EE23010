import numpy as np
import matplotlib.pyplot as plt

A=np.array([1,-1])
B=np.array([-4,6])
C=np.array([-3,-5])
I=np.array([-1.48,-0.79])

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
x_BI = line_gen(B,I)
x_CI = line_gen(C,I)
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_CI[0,:],x_CI[1,:],label='$CI$')
plt.plot(x_BI[0,:],x_BI[1,:],label='$BI$')

tri_coords = np.vstack((A,B,C,I)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C','I']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), 
                 textcoords="offset points", 
                 xytext=(0,10), 
                 ha='center')
plt.show()
