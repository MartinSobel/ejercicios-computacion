# Escribir un programa que cree un diccionario simulando una compra en un supermercado.
# El programa debe preguntar el artículo y su precio y añadir el par al diccionario,
# hasta que el usuario decida terminar. Después se debe mostrar
# por pantalla la lista de la compra y el costo total.

compra = {}

while True:
    articulo = input('Introduce el nombre del artículo: ')
    if articulo == '':
        break
    precio = float(input('Introduce el precio del artículo: '))
    compra[articulo] = precio

print('Lista de la compra:')
for articulo, precio in compra.items():
    print(articulo, precio)

print('Costo total:', sum(compra.values()))