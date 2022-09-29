# Escribir un programa que guarde en un diccionario las estaciones del año
# y ponga para cada una de ellas fechas de inicio y fin.
# Pedir una estación y mostrar su información.

estaciones = {'verano': {'inicio': '21/12', 'fin': '21/03'}, 'otoño': {'inicio': '21/03', 'fin': '21/06'}, 'invierno': {'inicio': '21/06', 'fin': '21/09'}, 'primavera': {'inicio': '21/09', 'fin': '21/12'}}
estacion = input('Ingrese una estacion: ')
print(estaciones[estacion])