# Mostrar el cuadrado de los valores de una lista de n valores, ingresados por teclado.

valores = []

n = int(input("Ingrese la cantidad de valores: "))

for i in range(n):
    valor = int(input("Ingrese un valor: "))
    valores.append(valor)
    
for valor in valores:
    print(valor ** 2)