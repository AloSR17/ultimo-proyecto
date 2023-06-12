import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*3.1416, 250)
y = np.linspace(0, 2*3.1416, 250)
r = 2-2*np.sin(x)+np.sin(x)*np.sqrt(abs(np.cos(x)))/(np.sin(x)+1.4)
fx = r*np.cos(x)
fy = r*np.sin(x)
#plt.plot(fy, fx, '.', linewidth=3, color='c', markersize = 10)
#plt.plot(y, fy, '.', linewidth=3, color='m', markersize = 10)
plt.title('')
plt.xlabel('Eje X', fontsize = 14)
plt.ylabel('Eje Y', fontsize = 14)
plt.fill_between(fx, fy, color='red')
plt.axis('equal')
plt.axis('off')
a = plt.gca()
plt.grid(True)
plt.show()