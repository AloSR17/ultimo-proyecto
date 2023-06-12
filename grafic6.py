import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 100)
y = np.linspace(0, 2, 100)
fx = x*np.exp(-3*x)
fy = 1 - 3*y*np.exp(-3*y)
plt.plot(x, fx, '.', linewidth=3, color='c', markersize = 10)
plt.plot(y, fy, '.', linewidth=3, color='m', markersize = 10)
plt.title('$F(x) = xe(-3x, F(y) = 1 - 3xe(-3x)')
plt.xlabel('Eje X', fontsize = 14)
plt.ylabel('Eje Y', fontsize = 14)
a = plt.gca()
plt.grid(True)
plt.show()