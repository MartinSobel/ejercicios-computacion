# Realiza una función llamada relacion(a, b) que a partir de dos números cumpla lo siguiente:
# •	Si el primer número es mayor que el segundo, debe devolver 1.
# •	Si el primer número es menor que el segundo, debe devolver -1.
# •	Si ambos números son iguales, debe devolver un 0.
# Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'.

def relacion(a,b):
    """Compara a con b y devuelve 1 si es mayor, -1 si es menor y 0 si es igual"""
    if (a==b):
        estado=0
    elif (a<b):
        estado=-1
    else:
        estado=1
    return estado

comparac={1:" es Mayor que ",-1:" es Menor que ",0:" es Igual que "}

print("5",comparac[relacion(5,10)],"10")
print("10",comparac[relacion(10,5)],"5")
print("5",comparac[relacion(5,5)],"5")