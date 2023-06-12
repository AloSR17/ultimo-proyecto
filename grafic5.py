import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 4*3.1416, 200)
y = np.linspace(0, 4*3.1416, 200)
fx = np.cos(2*x) + np.sin(2*x)
fy = -2*np.sin(2*y) + 3*np.cos(3*y)
plt.plot(x, fx, '.', linewidth=3, color='r', markersize = 10)
plt.plot(y, fy, '.', linewidth=3, color='b', markersize = 10)
plt.title('$F(x) = cos(2x) + sin(2x), F(y) = -2sin(2x) + 3Cos(3x)')
plt.xlabel('Eje X', fontsize = 14)
plt.ylabel('Eje Y', fontsize = 14)
a = plt.gca()
plt.grid(True)
plt.show()