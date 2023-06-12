import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 4*3.1416, 250)
y = np.linspace(0, 4*3.1416, 250)
r = 105+100*np.sin(4.5*x)
h = x-(np.cos(10*x)/10)
fx = 320+r*np.cos(h)
fy = -240-r*np.sin(h)
plt.plot(fx, fy, '-', linewidth=3, color='c', markersize = 10)
#plt.plot(y, fy, '.', linewidth=3, color='m', markersize = 10)
plt.title('')
plt.xlabel('Eje X', fontsize = 14)
plt.ylabel('Eje Y', fontsize = 14)
#plt.fill_between(fx, fy, color='red')
plt.axis('equal')
plt.axis('off')
a = plt.gca()
plt.grid(True)
plt.show()