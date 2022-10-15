# Realiza una función separar(lista) que tome una lista de números enteros\
# y devuelva dos listas ordenadas. La primera con los números pares y la segunda con los números impares.
# Por ejemplo:
# pares, impares = separar([6,5,2,1,7])
# print(pares)
# print(impares)
# [2, 6]
# [1, 5, 7]

def separar(lista):
    pares=[]
    impares=[]
    for i in lista:
        if i%2==0:
            pares.append(i)
        else:
            impares.append(i)
    return pares, impares

test = separar([6,5,2,1,7])
print(test[0])
print(test[1])