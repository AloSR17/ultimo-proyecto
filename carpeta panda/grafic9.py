import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*3.1416, 100)
y = np.linspace(0, 2*3.1416, 100)
fx = np.cos(x)*np.cos(x)*np.cos(x)
fy = np.sin(y)*np.sin(y)*np.sin(y)
plt.plot(fy, fx, '.', linewidth=3, color='c', markersize = 10)
#plt.plot(y, fy, '.', linewidth=3, color='m', markersize = 10)
plt.title(' x = cos3(t) y = sin3(t)')
plt.xlabel('Eje X', fontsize = 14)
plt.ylabel('Eje Y', fontsize = 14)
a = plt.gca()
plt.grid(True)
plt.show()