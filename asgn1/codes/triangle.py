import matplotlib.pyplot as plt

# Coordinates of the two points
plt.annotate("A", (1, -1),color='red',size='18')
plt.annotate("B", (-4, 6),color='red',size='18')
plt.annotate("C", (-3, -5),color='red',size='18')
plt.annotate("I (-1.48,-0.75)", (-1.48, -0.75),color='black',size='18')
x1,y1 = [1, -4],[-1,6]
x2,y2 = [-4, -3],[6,-5]
x3,y3 =[1,-3],[-1,-5]
x4,y4 =[-4,-1.48],[6,-0.75]
x5,y5=[-3,-1.48],[-5,-0.75]	
plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5)

# Turn off the axis
plt.axis('off')


plt.show()

