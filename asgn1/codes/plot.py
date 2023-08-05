import numpy as np
import matplotlib.pyplot as plt
from asgn1 import *
A=np.array([1,-1])
B=np.array([-4,6])
C=np.array([-3,-5])

t = norm_vec(B,C)
n1 = t/np.linalg.norm(t)
t = norm_vec(C,A)
n2 = t/np.linalg.norm(t)
t = norm_vec(A,B)
n3 = t/np.linalg.norm(t)

I=line_intersect(n1-n3,B,n1-n2,C)

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

x = np.linspace(-6,2,100)

tri_coords = np.vstack((A,B,C,I)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C','I']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), 
                 textcoords="offset points", 
                 xytext=(0,10), 
                 ha='center')
m_b,c_b=-(n1-n3)[0]/(n1-n3)[1] , ((n1-n3)@B)/(n1-n3)[1]
m_c,c_c=-(n1-n2)[0]/(n1-n2)[1] , ((n1-n2)@C)/(n1-n2)[1]
y_b = (m_b * x) + c_b
plt.plot(x, y_b,linewidth=2, label='1.81x+0.67y+3.21=0')
y_c = (m_c * x) + c_c
plt.plot(x, y_c,linewidth=2, label='1.7x-0.62y+2.03=0')
plt.legend()
plt.show()
