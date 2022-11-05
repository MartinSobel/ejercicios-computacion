# La empresa dispone de 10 sucursales (numeradas del 01 al 10). 
# Al final de cada día se procesan todas las ventas, ingresando cada código
# de venta en un string de 5 caracteres de la siguiente forma:
# 01023 ( es factura número 01 de la sucursal 02 por ventas del servicio 3)
# 02021 (es factura número 02 de la sucursal 02 por ventas del servicio 1)
# 03014 (es factura número 03 de la sucursal 01 por ventas del servicio 4)
# 04083 ( es factura número 04 de la sucursal 08 por ventas del servicio

# Codificar un algoritmo que pida los códigos de venta, determinando el servicio
# que se factura (slicing de String), y calcule cuantas facturas hubo para cada
# uno de los 4 servicios que se brindan
# El ciclo termina cuando en lugar de un código se ingresa la palabra fin
# Mostrar cantidad de facturas ingresadas por servicio.

# Nro. De Factura	los dos primeros caracteres
# Nro. De sucursal (1 a 10)	los dos caracteres siguientes
# Código del servicio (1 a 4) el 5to caracter


venta = input('Ingrese venta:')
s1 = s2 = s3 = s4 = 0

while (venta != 'fin'):
    servicio = venta[4]

    if(servicio == '1'):
        s1 += 1
    elif (servicio == '2'):
        s2 += 1
    elif (servicio == '3'):
        s3 += 1
    elif (servicio == '4'):
        s4 += 1

    venta = input('Ingrese venta:')

print(f'Encomienda 1: {s1}')
print(f'Encomienda 2: {s2}')
print(f'Encomienda 3: {s3}')
print(f'Encomienda 4: {s4}')
