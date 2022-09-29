'''Este ejemplo parte de una variable string multilinea
Separa cada línea creando una lista
Separa la 1er línea en Nombre y Apellido
Separa la 2da línea  en Dirección - Localidad - Cod.Postal
Usamos los métodos split y splitline
Luego lo guarda en un diccionario
'''

Datos_alumnos="""Ezequiel Rosales
Pirámides 3821 - Pcia Buenos Aires -14777"""

print("Se recibe un único dato Multilinea:\n",Datos_alumnos)
a=input("\nSe van a separar por línea(Enter para continuar)\n")
ListaDatos=Datos_alumnos.splitlines()
for linea in ListaDatos:
        print(f'Esta es una línea : {linea}')

Nom,Ape=ListaDatos[0].split()
Direcc, Pcia, CP = ListaDatos[1].split("-")

Alumno=dict()
Alumno={"Nombre":Nom,
        "Apellido":Ape,
        "Direccion":Direcc,
        "Provincia":Pcia,
        "CodPostal":CP
        }
a=input("\nSe pasaron los datos en el diccionario y se muestran (Enter para continuar) ")
print("\n******\nDatos del alumno de apellido",Alumno["Apellido"],"y nombre",Alumno["Nombre"],":")
print(f'Dirección: {Alumno["Direccion"]}')
print(f'en : {Alumno["Provincia"]}')
print(f'cuyo cód. postal es {Alumno["CodPostal"]}\n******')
