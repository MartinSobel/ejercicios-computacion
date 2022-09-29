# Escribe un programa que solicite al usuario que introduzca números enteros
# hasta ingresar un cero y muestre por pantalla cuántos de ellos son
# pares mayores que 20 y cuántos son impares menores a -2.

lista = []

numero = int(input("Introduzca un numero para la lista: "))

while numero != 0:
    lista.append(numero)
    numero = int(input("Introduzca un numero para la lista: "))

pares = 0
impares = 0

for numero in lista:
    if numero % 2 == 0 and numero > 20:
        pares += 1
    elif numero % 2 != 0 and numero < -2:
        impares += 1

print("Hay", pares, "numeros pares mayores a 20")
print("Hay", impares, "numeros impares menores a -2")