import pandas as pd
import matplotlib.pyplot as plt

# Leer el stock.csv y mostrar el total por Proveedor. Graficar
# Agrupar por Proveedor y Graficar la cantidad de productos por entregar con grafico de barras
# Guardar la agrupación en un csv con el nombre stock1 

# stock = pd.read_csv("STOCK.csv")
# sum = stock.groupby("Proveedor").sum()
# print(sum)
# sum.plot(kind="bar")
# plt.show()
# sum.to_csv("stock1.csv")




# Leer stock csv y mostrar las funciones estadísticas básicas.
#  Agrupar por Deposito y Graficar la cantidad de productos por entregar con grafico de líneas
# Guardar la agrupación en un csv con el nombre stock2 

# stock = pd.read_csv("STOCK.csv")
# print(stock.describe())

# depositos = stock.groupby('Deposito').sum()
# print(depositos)

# depositos.plot()
# plt.show()

# depositos.to_csv('stock2.csv')




# Leer el csv stock y filtrar las filas cuyo stock sea mayor a 50. Mostrar el filtro
#  Agrupar por Proveedor y Graficar la cantidad de productos por entregar con grafico de barras
# Guardar la agrupación en un csv con el nombre stock3

# stock = pd.read_csv("STOCK.csv")
# stock = stock[stock['PorEntregar'] > 50]
# print(stock)

# proveedores = stock.groupby("Proveedor").sum()
# print(proveedores)

# proveedores.plot(kind="bar")
# plt.show()

# proveedores.to_csv('stock3.csv')





# Leer STOCK.csv y filtrar las filas del Deposito III ( buscar el string “III” en esa columna)
# Mostrar el filtro
#  Graficar la cantidad de productos por entregar con grafico de líneas y Guardar el filtro en un
# csv con el nombre stock4

stock = pd.read_csv("STOCK.csv")
d3 = stock[stock['Deposito'] == "III"]
print(d3)

d3.plot()
plt.show()
d3.to_csv("stock4.csv")