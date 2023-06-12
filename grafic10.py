import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*3.1416, 2*3.1416, 250)
y = np.linspace(-2*3.1416, 2*3.1416, 250)
fx = x + 2*np.sin(2*x)
fy = y + 2*np.cos(5*y)
plt.plot(fy, fx, '.', linewidth=3, color='c', markersize = 10)
#plt.plot(y, fy, '.', linewidth=3, color='m', markersize = 10)
plt.title(' x = t + 2sin(2t) y = t + 2cos(5t)')
plt.xlabel('Eje X', fontsize = 14)
plt.ylabel('Eje Y', fontsize = 14)
a = plt.gca()
plt.grid(True)
plt.show()