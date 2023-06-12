import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2, 2, 0.2)
y = np.arange(-2, 2, 0.2)
a, b  = np.meshgrid(x,y)
z = a*np.exp(-(a*a)-(b*b))

#plt.plot(a, b, z, '-', linewidth=3, color='c', markersize = 10)
#plt.plot(y, fy, '.', linewidth=3, color='m', markersize = 10)
k = plt.axes(projection = '3d')
k = plt.gca()
k.plot_surface(a, b, z, color= 'red', linewidth = 0)
plt.show()