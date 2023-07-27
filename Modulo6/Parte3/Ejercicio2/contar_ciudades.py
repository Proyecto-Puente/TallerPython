# Ejercicio 2
# Taller: introducción a python
# Día 9

# Consigna:
#   Dado un archivo CSV con una lista de personas y sus ciudades de origen, cuente
#   cuántas personas provienen de cada ciudad.

import csv

ruta = "personas.csv"

with open(ruta) as personas:
    lector = csv.reader(personas)
    # Obtengo una lista con cada ciudad (columna 1), ademas se remueve el encabezado
    # de la tabla, tambien se quitan los espacios del dato y se lo lleva a mayuscula.
    ciudades = [(fila[1].upper()).strip() for nro, fila in enumerate(lector) if nro != 0]

# Por cada ciudad obtengo las veces que se repite en la lista ciudades y lo muestro.
print({ciudad: ciudades.count(ciudad) for ciudad in ciudades})