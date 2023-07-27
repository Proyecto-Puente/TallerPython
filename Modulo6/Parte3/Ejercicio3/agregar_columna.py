# Ejercicio 3
# Taller: introducción a python
# Día 9

# Consigna:
# Modificar un archivo CSV agregando una nueva columna calculada a
# partir de datos existentes.

import csv

ruta = input("Ingrese la ruta del archivo:")

# En el siguiente ejemplo añadire el nro de fila como una nueva columna.
with open(ruta, "r", newline="") as archivo:
    lector = csv.reader(archivo)
    # almaceno los datos del csv para luego escribirlos. Ademas añado el nuevo dato a cada fila.
    datos = [linea + [contador] for contador, linea in enumerate(lector)]

with open(ruta, "w", newline="") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(datos)
