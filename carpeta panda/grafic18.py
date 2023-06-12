import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 10, 5)
y = np.arange(-10, 10, 5)
a, b  = np.meshgrid(x,y)
z = np.sin(abs(a)-abs(b))

#plt.plot(a, b, z, '-', linewidth=3, color='c', markersize = 10)
#plt.plot(y, fy, '.', linewidth=3, color='m', markersize = 10)
k = plt.axes(projection = '3d')
k = plt.gca()
k.plot_surface(a, b, z, color= 'red', linewidth = 0)
plt.show()