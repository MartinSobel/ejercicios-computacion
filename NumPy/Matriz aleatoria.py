# Matrices ejercicio 3 – 
# Genera en el código una matriz mat de 3x4 con números enteros aleatorios entre 10 y 20. 
# Usar la función: matriz = np.random.randint(10,20,size=(3,4))
# Se pide imprimir: 
# a) la matriz 
# b) la suma de los valores de la fila i (El número de la fila será ingresada por teclado con input() definiendo una función y siendo llamada por el módulo principal). 
# c) el elemento mat(3,2) 

import numpy as np
mat = np.random.randint(10,20,size=(3,4))
print(mat)
def suma_fila(mat, fila):
    return sum(mat[fila])
print(suma_fila(mat, int(input('fila: '))))
print(mat[3,2])