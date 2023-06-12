import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-1, 1, 1)
y = np.arange(-1, 1, 1)
a, b  = np.meshgrid(x,y)
z = np.cos(abs(a))
z = np.cos(abs(a)+abs(z))

#plt.plot(a, b, z, '-', linewidth=3, color='c', markersize = 10)
#plt.plot(y, fy, '.', linewidth=3, color='m', markersize = 10)
k = plt.axes(projection = '3d')
k = plt.gca()
k.plot_surface(a, b, z, color= 'red', linewidth = 0)
plt.show()