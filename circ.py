import matplotlib.pyplot as plt
import numpy as np
import math

def circle(radio, a, b):
    theta = np.linspace(0, 2*np.pi, 100)
    r = np.sqrt(radio)
    x1 = r*np.cos(theta) + a
    x2 = r*np.sin(theta) + b
    return (x1, x2)

x, y = circle(2, 0 , 0)
x1, y1 = circle(.15, .8, .25)
x2, y2 = circle(.15, -.7, .25)
plt.plot(x, y)
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.show()