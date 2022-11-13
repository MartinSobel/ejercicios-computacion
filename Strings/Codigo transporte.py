# 3.	Escribir un programa que le solicite al usuario ingresar cada uno de los siguientes 5 códigos de transportes, usando un ciclo
#       BUS31, FLE31, FLE42, BUS12, BUS03 
#       En cada código leído se interpretan los 3 primeros caracteres como la empresa de transporte (FLE es empresa FLECHA y BUS es empresa SafeBUS )
#       y los 2 últimos caracteres son la cantidad de pasajeros que transportaron 
#       Se pide:
# a)	mostrar los datos en forma de oración. Por ejemplo para el código BUS31 mostrar: ‘BUS31 : Viaje de empresa SafeBUS con 31 pasajeros’.
# b)	Mostrar luego de leer todos los códigos cuantos pasajeros transportó cada una de las 2 empresas.

FLE = 0
BUS = 0

for i in range(5):
    codigo = input('ingrese codigo de transporte: ')
    empresa = codigo[0:3]
    pasajeros = codigo[3:5]

    if(empresa == 'FLE'):
        print(f"{codigo}: Viaje de empresa FLECHA con {pasajeros} pasajeros")
        FLE += 1
    elif(empresa == 'BUS'):
        print(f"{codigo}: Viaje de empresa SafeBUS con {pasajeros} pasajeros")
        BUS += 1

print(f"Total FLE: {FLE} - Total BUS: {BUS}")