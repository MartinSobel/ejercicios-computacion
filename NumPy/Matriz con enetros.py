# Matrices ejercicio 4
# Genera en el código una matriz mat de 2x4 con números enteros entre 10 y 20. 
# Se pide imprimir: 
# a) El valor máximo de toda la matriz 
# b) El valor mínimo de toda la matriz 
# c) Verificar si el valor n existe en la matriz, ingresado por teclado con input(). Definir una función para este item, siendo llamada por el modulo principal.

import numpy as np
mat = np.random.randint(10,20,size=(2,4))
print(mat)
print(mat.max())
print(mat.min())

def existe(mat, n):
    for i in range(2):
        for j in range(4):
            if mat[i,j] == n:
                return True
    return False
    
print(existe(mat, int(input('n: '))))