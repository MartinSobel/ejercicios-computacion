# 1.	Crear e imprimir un diccionario de n elementos: clave y valor. Ingresar ambos con input()
# Clave: “fecha” (ingresando un string con formato “dd/mm/aa”
# Valor: temperatura promedio de ese dia.

temperaturas = {}
fecha = ''
def ingreso():
    fecha = input('Ingrese fecha: ')
    temperatura = input('Ingrese temperatura: ')
    temperaturas[fecha] = temperatura
    print(temperaturas)

ingreso()




# 2.	Escribí un programa que le solicite al usuario ingresar un código de almacenamiento de un producto formado por un string cuyos caracteres tienen el siguiente significado:
# •	los primeros 2 representan el nro de depósito
# •	los siguientes 2 representan el sector dentro del depósito
# •	el 5to representa la góndola
# •	los dos últimos el nro de estante.
# Se pide:
# a)	mostrar los datos en forma de oración, en solo print: ‘El artículo se encuentra en el depósito XX, del sector XX, en la góndola X y en el estante XX.
# b)	Si el depósito es 12 mostrar un mensaje “transferir a deposito 15, si el depósito es 55 mostras la salida “transferir a sector 30 y sino mostrar “tranferencia postergada”. 
# Uso de slicing de string, condicional if con elif y else

codigo = input('ingrese codigo: ')
deposito = codigo[0:2]
sector = codigo[2:4]
gondola = codigo[5]
estante = codigo[6:7]

print(f'El artículo se encuentra en el depósito {deposito}, del sector {sector}, en la góndola {gondola} y en el estante {estante}')
if(deposito == 12):
    print('transferir a deposito 15')
elif(deposito == 55):
    print('transferir a sector 30')
else:
    print('transferencia postergada')




# 3.	Generar en el código una matriz Numpy de 3 x 4 con valores numéricos enteros random entre un rango 0 a 5. Se pide:
# •	la suma de los valores impares que sean menores a un valor ingresado
# •	el máximo de la columna 1
# •	el mínimo de la fila 1
# •	el promedio de todas sus filas
# •	la suma de todas sus columnas

import numpy as np
matriz = np.random.randint(0, 5, size=(3,4))
print(matriz)

print(f"Minimo primera fila: {np.min(matriz[0])}")
print(f"Maximo segunda columna: {np.max(matriz[:,1])}")
print(f"Promedio de todas las filas: {np.mean(matriz)}")
print(f"Suma de todas las columnas: {np.sum(matriz)}")




# 4.	Ingresar los importes de facturas en una lista hasta ingresar un cero. Definir una función que cuente las facturas que superen los 5000 pesos.
# Hallar el promedio de las mismas.

importes = []
total = 0
cantidad = 0
promedio = 0

importe = int(input('Ingrese importe: '))
while (importe != 0):
    importe = int(input('Ingrese importe: '))
    if (importe > 5000):
        total += importe
        cantidad += 1
else:
    promedio = total/cantidad
    print(f"Promedio: {promedio}")




# 5.	Generar en el código un vector Numpy con valores numéricos enteros random entre 500 y 800 que simulan los precios de los n productos de una empresa.
#       Se pide mostrar los precios y luego aquellos que sean menores al promedio general de los precios. Pruebe la salida con n = 6.

import numpy as np
precios = np.random.randint(500, 800, size=(6))
print(precios)

menores = []
promedio = np.mean(precios)
for precio in precios:
    if(precio < promedio):
        menores.append(precio)
print(menores)




# 6.	Crear una tupla de 5 elementos ingresando por teclado valores enteros, positivos y negativos. Recordar que se genera una lista y luego se convierte a tupla.
# Ingresar un valor x e indicar cuantas veces aparece en la lista. Si no aparece indicar con una salida “valor no encontrado”. Mostrar también el tipo tuple de la tupla generada.

valores = []

for n in range(5):
    valor =  int(input('Ingrese un numero: '))
    valores.append(valor)

valor = int(input('Ingrese el valor a buscar: '))
cantidad = valores.count(valor)

tupla = tuple(valores)
print(f"Valores: {tupla}")
if(cantidad > 0):
    print(f"Cantiodad apariciones del valor: {cantidad}")
else:
    print("Valor no encontrado")