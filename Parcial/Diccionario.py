# Definir una función que recibe 2 parámetros: un diccionario y un decimal como
# % de aumento. La función actualiza los valores del diccionario que recibe
# incrementándolos en el % indicado por su 2do parámetro. 

# b.	Programa:
# i.	Definir un diccionario de 4 elementos cuya clave es el servicio
#       y el valor su precio (cualquier valor entero). Imprimir el diccionario
# ii.	Pedir un % de aumento (un decimal entre 0 y 1)
# iii.	Llamar a la función para actualizar el diccionario

def aumentador(diccionario, aumento):
    for d in diccionario:
        diccionario[d] += diccionario[d] * aumento
    return diccionario

diccionario = {1: 1, 2: 2, 3: 3, 4: 4}
print(diccionario)

aumento = float(input('dame el aumento crack: '))
print(aumento)

resultado = aumentador(diccionario, aumento)
print(f'crack tu resultado es: {resultado}')
