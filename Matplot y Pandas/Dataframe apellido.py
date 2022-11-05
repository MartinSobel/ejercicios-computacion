# Leer el archivo materias.csv y cargarlo en un dataframe.
# Graficar Por Apellido en el mismo gráfico, acomodandolos 2 por fila,
# el promedio de notas de Matemáticas en amarillo, resaltando los puntos
# con triángulo hacia abajo y línea continua, 
# y el de Geografía en rojo, con línea y punto. Coloque la leyenda. Muestrelo

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('materias.csv', index_col=0)
graph = df.groupby('Apellido').mean()
graph.plot(kind='bar', subplots=True, layout=(2,2), sharex=False, sharey=False, color=['yellow','red'], marker='v', linestyle='--')