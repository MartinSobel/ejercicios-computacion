# Genere un vector x, con 1000 puntos entre 1 y 5.
# Genere un vector aplicando ln(x)
# Genere otro vector aplicando e-x 
# Páselo a un dataframe y guárdelo en formato .csv
# Grafique los 2 vectores de funciones en el mismo gráfico con su leyenda correspondiente.

# NOTA:
# Para generar un dataframe a partir de vectores utilice el  método Dataframe como se muestra:
# df=pd.DataFrame({'col1':vect1,'col2':vect2})                donde ‘coln’  es el nombre de la columna y vecn es el vector que se le asigna a esa columna


# x=np.linspace(1,5,1000)
# y1=math.e**-x
# y2=np.log(x)
# plt.plot(x,y1,label='e**-x')
# plt.plot(x,y2,label='ln(x)')
# plt.legend(loc=1)
# plt.title("Cálculos")
# plt.show()

# datacalc=pd.DataFrame({'X':x,'ln(x)':y1,'e**-x':y2 })
# datacalc.to_csv('calculos.csv',index=0)
