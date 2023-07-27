# Ejercicio 4
# Taller: introducción a python
# Día 6

# Consigna:
#   Crea un subpaquete para utils, debe llamarse “validacion”, este incluye
#   un módulo llamado numbers.py que contenga las siguientes funciones:
#   • is_positive_integer(num): Recibe un número y devuelve True si es un
#       entero positivo, de lo contrario, devuelve False.

from utils.validacion.number import is_positive_integer as is_positivo

print(is_positivo(9.24))