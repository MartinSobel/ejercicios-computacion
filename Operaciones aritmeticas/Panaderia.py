# Una panadería vende flautas de pan a 30.49$ cada una. El pan que no es del día tiene un descuento del 60%.
# Escribir un programa que comience leyendo el número de flautas vendidas que no son del día.
# Después el programa debe mostrar el precio habitual de una flauta,
# el descuento que se le hace por no ser fresca y el coste final por el total de flautas vendidas.

precio = 30.49
descuento = 0.6

cantidad = int(input("Ingrese total de flautas que no son del dia: "))
totalSinDescuento = precio * cantidad
descuento = totalSinDescuento * descuento
totalConDescuento = totalSinDescuento - descuento

print('Precio sin descuento: ', totalSinDescuento)
print('Descuento: ', descuento)
print('Total con descuento: ', totalConDescuento)