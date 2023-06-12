import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 25, 300)
fx = np.sin(2*x)*np.exp(-.1*x) 
plt.plot(x, fx, '.', linewidth=3, color='r', markersize = 10)
plt.title('$F(x) = 2x - 8x - 11$')
plt.xlabel('Eje X', fontsize = 14)
plt.ylabel('Eje Y', fontsize = 14)
a = plt.gca()
plt.grid(True)
plt.show()