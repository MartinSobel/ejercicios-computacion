# Ingresar un conjunto de valores naturales hasta ingresar un cero e imprimir la cantidad de los mayores a 10. (Usamos conjunto).

valores = []

while True:
    valor = int(input("Ingrese un valor: "))
    if valor == 0:
        break
    valores.append(valor)

mayores = 0
for valor in valores:
    if valor > 10:
        mayores += 1

print("Hay", mayores, "valores mayores a 10")