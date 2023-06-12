import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-6, 2, 200)
fx = x*np.exp(-2*x)
plt.plot(x, fx, '.', linewidth=3, color='k', markersize = 10)
plt.title('t.exp(-2t)')
#plt.title('$F(x) = 5 -4x -x2$')
plt.xlabel('Eje X', fontsize = 14)
a = plt.gca()
plt.grid(True)
plt.show()