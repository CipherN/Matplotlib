from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

x = np.arange(-5, 5, 0.2)
y = np.arange(-5, 5, 0.2)
x, y = np.meshgrid(x, y)
print(x)
z = x ** 2 - y ** 2

ax1.plot_wireframe(x, y, z)

ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')

plt.show()
