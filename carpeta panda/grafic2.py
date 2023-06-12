import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 5, 100)
fx = 2*x*x - 8*x -11
plt.plot(x, fx, '.', linewidth=3, color='r', markersize = 10)
plt.title('$F(x) = 2x*x - 8x - 11$')
plt.xlabel('Eje X', fontsize = 14)
plt.ylabel('Eje Y', fontsize = 14)
a = plt.gca()
plt.grid(True)
plt.show()