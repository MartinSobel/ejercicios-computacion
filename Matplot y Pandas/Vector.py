# Genere un vector con 1000 posiciones entre -1 y 1.
# Haga un ciclo para generar otro vector “y” utilizando una función , tal que y=NX**2,
# Donde N toma el valor en el rango (-5,0)
# Grafique cada una de las funciones y luego muestrelo.

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1,1,1000)
y = np.linspace(-5,0,1000)

for i in y:
    y = i*x**2
    plt.plot(x,y)
    plt.show()