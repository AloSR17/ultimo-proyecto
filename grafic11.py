import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*3.1416, 250)
y = np.linspace(0, 2*3.1416, 250)
fx = np.sin(3*x)
fy = np.sin(4*x)
plt.plot(fy, fx, '.', linewidth=3, color='c', markersize = 10)
#plt.plot(y, fy, '.', linewidth=3, color='m', markersize = 10)
plt.title(' x = sin(3t) y = sin(4t)')
plt.xlabel('Eje X', fontsize = 14)
plt.ylabel('Eje Y', fontsize = 14)
a = plt.gca()
plt.grid(True)
plt.show()