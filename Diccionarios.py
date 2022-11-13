# 1.	Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
#        pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

diccionario = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

divisa = input('Ingrese divisa:')

if (divisa == "Euro"):
    print(diccionario['Euro'])
elif (divisa == "Dollar"):
    print(divisa['Dollar'])
elif (divisa == "Yen"):
    print(divisa["Yen"])
else:
    print('Divisa not found')


# 2.	Escribir un programa que genere un diccionario donde las claves serán las estaciones del año (VERANO , OTOÑO, INVIERNO, PRIMAVERA)
#       y ponga para cada clave un  texto con sus fechas de inicio - fecha fin como valor. 
# a.	Hacer un ciclo que pida una estación y muestre su información. El ciclo termina cuando ingresa la palabra fin.

estaciones = {'VERANO':'1', 'OTOÑO':'2', 'INVIERNO':'3', 'PRIMAVERA':'4'}
estacion = input('Ingrese estacion:')

while(estacion != 'fin'):
    estacion = input('Ingrese estacion:')
    print(estaciones[estacion])
else:
    print('fin')