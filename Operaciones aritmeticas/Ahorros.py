# Acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año.
# Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden
# al balance final de tu cuenta de ahorros. Dejás el dinero por 3 años.
# Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros,
# introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de
# ahorros tras el primer, segundo y tercer año. Redondear cada cantidad a dos decimales

valor = float(input("Introduzca cantidad de dinero depositada en la cuenta de ahorros: "))
interes = 0.04

print("Ahorros tras el primer año: ", round(valor * (1 + interes), 2))
print("Ahorros tras el segundo año: ", round(valor * (1 + interes) ** 2, 2))
print("Ahorros tras el tercer año: ", round(valor * (1 + interes) ** 3, 2))