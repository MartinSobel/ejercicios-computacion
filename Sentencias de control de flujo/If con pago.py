# Ingresar el valor de una compra. Hasta $1000 inclusive mostrar “pago en efectivo”.
# Si el gasto está comprendido entre 1000 y 3000 inclusivo mostrar “pago con tarjeta de débito”,
# de lo contrario mostrar “pago con tarjeta de crédito”.

gasto = int(input("Ingrese el valor de la compra: "))
if gasto <= 1000:
    print("Pago en efectivo")
elif gasto <= 3000:
    print("Pago con tarjeta de débito")
else:
    print("Pago con tarjeta de crédito")