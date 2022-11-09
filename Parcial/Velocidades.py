# 1.	Generar un vector con 20 velocidades entre 60 y 150 (genérelo con números aleatorios) simulando tomas de radar en una ruta nacional. 
# a.	Imprimir el vector generado.
# b.	Graficarlo con título “Velocidad en Ruta Nacional”. 
# 2.	Si Se sabe que la velocidad máxima permitida en una ruta nacional es 110 km. Mostrar cuantas mediciones del vector excedieron la velocidad máxima y cuantas no.

import numpy as np
import matplotlib.pyplot as plt

veolcidades = np.random.randint(60, 150, size=(20))

print(veolcidades)

plt.plot(veolcidades)
plt.title("Velocidad en Ruta Nacional")
plt.show()

mayores = np.count_nonzero(veolcidades > 110)
print(f'Mayores: {mayores}')

menores = np.count_nonzero(veolcidades <= 110)
print(f'Menores: {menores}')



# 2.	Multas (ciclo for, acumulador, if/elif)
#       Cálculo de multas por exceso de velocidad: Si excede hasta 10 km, la multa es de 15000$, si excede más de 10 km y menos de 20 km la multa es de 25000$
#       y si excede más de 20 km es de 30000$.
# i.	En un ciclo, pedir 5 velocidades capturadas por radar entre 100 y 150 km. Si la velocidad leída excede la velocidad máxima (110). Calcular la multa y mostrarla 
# ii.	calcular el monto total que se cobró en multas.

multas = 0
for i in range(5):
    velocidad = int(input('Ingrese velocidad: '))
    if velocidad > 110:
        exceso = velocidad - 110
        print(exceso)
        multa = 0
        if exceso > 20:
            multa = 30000
        elif exceso > 10:
            multa = 25000
        elif exceso <= 10:
            multa = 15000
        print(f'Exceso de velocidad. Multa: {multa} ')
        multas += multa

print(f'Total multas: {multas}')


# 3.	Códigos
#       Se tiene el siguiente código de las velocidades mínimas y máximas en las carreteras nacionales:
# i.	Los 2 primeros caracteres del código indican:
# 1.	Si es NA indica que la carretera es Nacional
# 2.	Si es AU indica que la carretera es Autopista
# ii.	Los siguientes 3 caracteres son la velocidad máxima
# iii.	Los últimos 2 caracteres son la velocidad mínima
#        Ejemplo: Si el código es AU15080 debe traducir “Autopista - Velocidad máxima es 130 y mínima 80”
# # a.	Se pide: Traducir el código: NA11030 y guardarlo en un diccionario donde la clave es el código y el valor es la traducción generada. 

codigo = input('Ingrese el código de velocidad: ')
carretera = ""

if codigo[0:2] == "NA":
    carretera = "Nacional"
elif codigo[0:2] == "AU":
    carretera = "Autopista"

maxima = codigo[2:5]
minima = codigo[5:7]


traduccion = carretera + " - Velocidad máxima es " + maxima + " y minima " + minima
print(traduccion)

diccionario = {codigo: traduccion}
print(diccionario)


# 4.	Muestra
#       Se tiene una matriz que represente la velocidad máxima registrada en los últimos 8 meses en 10 rutas. Las velocidades pueden tener un valor entre 80 y 150,
#       y en la matriz se tiene por filas las rutas y por columnas los meses. Se pide:
# c.	Generar la matriz con números aleatorios que representen las velocidades con valores entre 80 y 150.
# d.	Mostrar Máximo, Mínimo y Promedio de toda la matriz.
# e.	Mostrar para el último mes en cuantas rutas superó la velocidad máxima permitida (130). Si no lo superó indicar en el mensaje “No superó la velocidad máxima”  

matriz = np.random.randint(80, 150, size=(10, 8))
print(matriz)

max = np.max(matriz)
min = np.min(matriz)
promedio = np.mean(matriz)

print(f'max: {max}, min: {min}, promedio: {promedio}')

rutas_excedidas = 0

for ruta in matriz:
    if ruta[7] > 130:
        rutas_excedidas += 1

if(rutas_excedidas > 0):
    print(f'Rutas exedidas en el ultimo mes: {rutas_excedidas}')
else:
    print('No superó la velocidad máxima')



# 5.	Excesos por ruta.
#       Se tiene en un archivo las rutas y velocidades excedidas durante el 1er día de temporada alta.  Leer el archivo rutas.csv (con Pandas) e imprimirlo.
# a.	Agrupar por nro de ruta la velocidad promedio por ruta.
# b.	Mostrar la agupación
# c.	Graficar con barras la agrupación.

import pandas as pd

df = pd.read_csv('rutas.csv')
promedio_por_ruta = df.groupby("Ruta")
promedio_por_ruta = promedio_por_ruta.agg({"VelExcedida":"mean"})
print('Promedio por ruta: ', promedio_por_ruta)

df.plot(kind='bar')
plt.show()