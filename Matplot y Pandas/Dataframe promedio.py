# Leer el archivo materias.csv y cargarlo en un dataframe.
# Agregar al dataframe una columna que contenga el promedio de ambas notas. Lamarla “Promedio”
# Graficar para cada edad el promedio calculado. 

# NOTA: Verá que como los datos no están ordenados por edad, antes debe ordenar el dataframe utilizando:
# df.sort_values((by=['Edad'], inplace=True) ó
# data_sort= df.sort_values(['Edad'])
# y recién graficarlo.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('materias.csv', index_col=0)
df['Promedio'] = (df['Matemáticas'] + df['Geografía'])/2
df.sort_values(by=['Edad'], inplace=True)
df.plot(kind='bar', x='Edad', y='Promedio')
plt.show()