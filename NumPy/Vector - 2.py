# Genera en el código un vector de 7 elementos con números enteros e imprimir: 

# a) Cantidad de números positivos 
# b) Cantidad de números negativos 
# c) Cantidad de ceros

import numpy as np
x = np.array([8,7,-1,-2,6,0,7])
ceros, pos, neg = 0,0,0
for i in range(7):
    if x[i] == 0:
        ceros += 1
    else:
        if x[i] > 0:
            pos += 1
        else:
            neg += 1
print(x)
print(f'cantidad de positivos = {pos}')
print(f'cantidad de negativos = {neg}')
print(f'cantidad de ceros = {ceros}')
