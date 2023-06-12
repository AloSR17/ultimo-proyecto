import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-6, 2, 200)
fx = 5-4*x-x*x
    
plt.plot(x, fx, '<', linewidth = 3, color = 'g', markersize = 10)
#plt.title('$F(x) = 5 - 4x - x')
plt.xlabel('Eje x', fontsize = 14)
a = plt.gca()
a.set_axes_locator('k')
plt.grid(True)
plt.savefig('Grafica1a.png')
#200 puntos, en el eje de las x debe alir eje x y de color verde con lins space y titulo eje x
# La 2 es de -1 a 5 y van a ser 100 puntos de color rojo con tamaño de marcador de 10, debe de decir eje x y eje y
# De -1 a -5 con 300 puntos, el color de la linea va a ser k y el marc ador de 10 y de ahi para adelante debe de llevar la expresin de la grafica 
# plt.title('titulo, para que se vea matematica se le pone '$xelevado2$')
# si es en y lleva plt.ylabel('cualquier cosa'), si es en x plt.xlabel('cualquier cosa)
# debe tener un lins sapce de 0 a 24 de 200 puntos, la 5 dos lineas en una misma grafica una de color azul y loa otra de color rojo
# la 5 la primera grafica en azul, la segunda en rojo, va de 0 a 4pi con plt.leyend
# la 6, la x va de color cian y la y de color magenta con ejes titulos y leyendas de 0 a 2 y son 100 puntos 
# la 7 con 100 puntos  de primer
#La 8 100 puntos de 0 a 2pi la primera de color cian y la segunda en color magenta