import matplotlib.pyplot as plt
import numpy as np
import math
from numpy import sin, cos

x = np.arange(-1, 1, 0.1)
y = np.arange(-1, 1, 0.1)
xM, yM = np.meshgrid(x, y)
z = cos(abs(xM) + abs(yM)) * (abs(xM) + abs(yM))
a = plt.axes(projection = '3d')
plt.title('$z = cos(|x| + |y|) * (|x| + |y|)$')
a = plt.gca()
a.plot_surface(xM, yM, z, color = '#38B7A9', linewidth = 2)
plt.show()
