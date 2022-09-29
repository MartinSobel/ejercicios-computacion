# Escribir un programa que pregunte al usuario su nombre, apellido, edad, estudios y trabajo y lo guarde en un diccionario.
# Después debe mostrar por pantalla un mensaje completando una oración con todos sus datos

nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
edad = input('Ingrese su edad: ')
estudios = input('Ingrese sus estudios: ')
trabajo = input('Ingrese su trabajo: ')

datos = {'nombre': nombre, 'apellido': apellido, 'edad': edad, 'estudios': estudios, 'trabajo': trabajo}
print(datos)