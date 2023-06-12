import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*3.1416, 100)
y = np.linspace(0, 2*3.1416, 100)
fx = (1 + np.sin(x))*np.cos(x)
fy = (1 + 2*np.sin(y))*np.sin(y)
plt.plot(x, fx, '.', linewidth=3, color='c', markersize = 10)
plt.plot(y, fy, '.', linewidth=3, color='m', markersize = 10)
plt.title('$F(x) = (1+sin(x))*cos(x), F(y) = (1 + 2sin(y))*(sin(y))')
plt.xlabel('Eje X', fontsize = 14)
plt.ylabel('Eje Y', fontsize = 14)
a = plt.gca()
plt.grid(True)
plt.show()