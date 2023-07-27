# Ejercicio 4
# Taller: introducción a python
# Día 4

# Consigna:
#   Promedio de calificaciones: Crea un programa que solicite al usuario
#   ingresar una serie de calificaciones separadas por comas. Luego,
#   convierte esas calificaciones en una lista y calcula el promedio de las
#   mismas. Muestra el resultado por pantalla.

# El modulo statistics cuenta con multiples funciones estadisticas
# esta es su documentacion: https://docs.python.org/es/3/library/statistics.html

# La funcion "mean" permite obtener la media a partir de una colleccion de numeros
from statistics import mean

while True:
    try:
        cadena = input("Ingrese elementos separados por ',': ")
        print("Promedio:", mean([float(caracter) for caracter in cadena.split(',')]))
        break
    except ValueError as e:
        print("valores incorrectos. Error:",e)