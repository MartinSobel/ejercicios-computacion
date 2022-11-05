# Generar un vector Numpy con 10 valores enteros random entre 100 y 200 simulando
# las cantidades vendidas del Servicio casillas de correo en cada sucursal. 
# a. Imprimir el vector
# b. Mostrar cuantas ventas menores a 150 hubo en todas las sucursales. 
# c. Si el valor por el Servicio Casilla de correo es $300.20, cuanto se facturó por este servicio?

import numpy as np

vector = np.random.randint(100, 200, size = (10))
print(f'vector: {vector}')

c = 0
tc = 0

for v in vector:
    if(v < 150):
        c += 1
        tc = tc + v

print(f'hay: {c} ventas menores a 150')
total = 300.20 * tc

print(f'se facturo: {total}')