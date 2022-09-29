# Recorrer una tupla de 8 valores numéricos, ingresar un valor k,
# si está el valor k en la tupla cortar el ciclo
# sino mostrar la leyenda “no se encontró el valor”

tupla = (1, 2, 3, 4, 5, 6, 7, 8)
k = int(input("Ingrese un valor: "))

for valor in tupla:
    if valor == k:
        print("Se encontró el valor")
        break
else:
    print("No se encontró el valor")