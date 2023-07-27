# Ejercicio 1
# Taller: introducción a python
# Día 6

# Consigna:
#   Crea un módulo llamado funciones.py que contenga las siguientes funciones
#   matemáticas:
#   • raiz(argumento, radicando): devuelve argumento**(1/radicando).
#   • divisible(a, b): devuelve a % b == 0.
#   • cuadrado(a): devuelve el cuadrado de a.
#   • cubo(a): devuelve el cubo de a.
#   Luego, en otro archivo llamado main.py, importa el módulo funciones y utiliza las
#   funciones para realizar operaciones matemáticas.

from funciones import *

print(raiz(256,8), divisible(-5, 3), cuadrado(-9), cubo(2.71))