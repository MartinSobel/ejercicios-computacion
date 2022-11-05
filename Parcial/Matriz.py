# Generar una matriz Numpy con valores enteros ramdon entre 100 y 200
# simulando las cantidades vendidas por servicio postal y sucursal. (fila y columna en ese orden).
# a.	Imprimir la matriz
# b.	Calcular la máxima cantidad vendida por sucursal. 
# c.	Graficar los valores máximos calculados en el punto anterior.
# d.	Mostrar las cantidades vendidas en la sucursal 7

import numpy as np
# import matplotlib.pyplot as plt

matriz = np.random.randint(100, 200, size = (4, 10))
print(matriz)

max = np.max(matriz, axis = 0)
print(max)

# plt.plot(max) 
# plt.title("Maximos por Sucursal")
# plt.show()

s7 = matriz[:,6]
print(s7)