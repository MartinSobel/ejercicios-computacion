# Escribe un programa que solicite al usuario 5 números y, tras ello, muestre cuál es el mayor y cuál es el menor

numeros = []

for i in range(5):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)

print("El mayor es", max(numeros))
print("El menor es", min(numeros))