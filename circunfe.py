import matplotlib.pyplot as plt
import numpy as np
import math

def f(x):
    y = np.sqrt(4-((x-2)**2))
    return y
x = np.linspace(0, 4, 100)
print(x)
print(f(x))

plt.plot(x, f(x))
plt.show