#Leer 3 números. Guardarlos en una lista
#Imprimir el menor y el mayor.

a=float(input('Ingrese el número 1: '))
b=float(input('Ingrese el número 2: '))
c=float(input('Ingrese el número 3: '))

ingresos=[a,b,c]
print(ingresos)
print(f'El máximo número ingresado es {max(ingresos)}')
print(f'El mínimo número ingresado es {min(ingresos)}')