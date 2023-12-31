import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-6, 2, 200)
fx = 5 - 4*x - x**2
plt.plot(x, fx, '.', linewidth=3, color='g', markersize = 10)
plt.title('$F(x) = 5 -4x -x2$')
plt.xlabel('Eje X', fontsize = 14)
a = plt.gca()
plt.grid(True)
plt.show()