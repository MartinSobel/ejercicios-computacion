#Leer 3 números. Guardarlos en una lista
#Imprimir el menor y el mayor.

ingresos=list()
for i in range(3):
    a=float(input(f'Ingrese el número {i+1}: '))
    ingresos.append(a)
    print(f'La lista generada hasta ahora es : {ingresos}')
print('La lista completa con los 3 elementos es :')
print(ingresos)
print(f'El máximo número ingresado es {max(ingresos)}')
print(f'El mínimo número ingresado es {min(ingresos)}')
