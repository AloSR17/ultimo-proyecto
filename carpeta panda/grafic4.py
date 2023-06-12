import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 25, 300)
fx = np.sin(2*x)*np.exp(-.1*x) 
plt.plot(x, fx, '.', linewidth=3, color='r', markersize = 10)
plt.title('$F(x) = sin(2x).e(-0.1x)')
plt.xlabel('Eje X', fontsize = 14)
plt.ylabel('Eje Y', fontsize = 14)
a = plt.gca()
plt.grid(True)
plt.show()