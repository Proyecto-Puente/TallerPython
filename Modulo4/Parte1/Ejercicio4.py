# Ejercicio 4
# Taller: introducción a python
# Día 4

# Consigna:
#   Promedio de calificaciones: Crea un programa que solicite al usuario
#   ingresar una serie de calificaciones separadas por comas. Luego,
#   convierte esas calificaciones en una lista y calcula el promedio de las
#   mismas. Muestra el resultado por pantalla.

while True:
    try:
        cadena = input("Ingrese elementos separados por ',': ")
        lst = [float(caracter) for caracter in cadena.split(',')]
        print("Promedio:", sum(lst)/len(lst))
        break
    except ValueError as e:
        print(dir(e))
        print("valores incorrectos")