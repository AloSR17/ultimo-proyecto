import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 4*3.1416, 600)
y = np.linspace(0, 4*3.1416, 600)
fx = np.sin(3*x)*np.cos(2*x)
fy = (1/2)*np.cos(y) + (5/2)*np.cos(5*y)
plt.plot(x, fx, '.', linewidth=3, color='r', markersize = 10)
plt.plot(y, fy, '.', linewidth=3, color='g', markersize = 10)
plt.title('$F(x) = sin(3x)*cos(2x), F(y) = .5cos(y) + 2.5cos(5y)')
plt.xlabel('Eje X', fontsize = 14)
plt.ylabel('Eje Y', fontsize = 14)
a = plt.gca()
plt.grid(True)
plt.show()