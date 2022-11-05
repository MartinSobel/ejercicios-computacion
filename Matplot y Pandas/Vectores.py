# Genere un vector x, con 1000 puntos entre 1 y 5.
# Genere un vector aplicando ln(x)
# Genere otro vector aplicando e-x 
# Páselo a un dataframe y guárdelo en formato .csv
# Grafique los 2 vectores de funciones en el mismo gráfico con su leyenda correspondiente.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x = np.linspace(1,5,1000)
y = np.log(x)
z = np.exp(-x)

df = pd.DataFrame({'x':x,'y':y,'z':z})
df.to_csv('data.csv')

plt.plot(x,y,label='ln(x)')
plt.plot(x,z,label='e^-x')
plt.legend()
plt.show()