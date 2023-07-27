# Ejercicio 6
# Taller: introducción a python
# Día 2

# Consigna:
#   Escribir un programa que pida al usuario un número entero y muestre por pantalla
#   un triángulo rectángulo como el de más abajo, de altura el número introducido.
#
#   *
#   **
#   ***
#   ****

filas = int(input("Ingrese el numero de filas: "))
if filas > 0:
  for f in range(filas + 1):
    print("*" * f)