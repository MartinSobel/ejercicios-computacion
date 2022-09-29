# Escribe un programa que muestre una pirámide como la que se muestra a continuación:
# *
# **
# ***
# ****
# *****
# ******
# *******

altura = int(input('Introduce la altura de la pirámide: '))
for i in range(1, altura + 1):
    print('*' * i)
