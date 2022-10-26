# Vectores ejercicio 1 – 
# Genera en el código un vector de 7 elementos e imprimir: 
# a)	El cuarto elemento 
# b)	El segundo elemento 
# c)	Los elementos en orden invertido 
# d)	El producto entre el primer elemento y el último 
# e)	Los elementos de índice par 
# f)	Los elementos de índice impar. 
# g)	Promedio de valores positivos.

import numpy as np
x = np.array([8,7,-1,-2,6,0,7])
print(x[4])
print(x[2])
print(x[::-1])
print(x[0]*x[-1])
print(x[::2])
print(x[1::2])
pos = 0
sum = 0
for i in range(7):
    if x[i] > 0:
        pos += 1
        sum += x[i]
print(pos)
print(sum)
print(sum/pos)