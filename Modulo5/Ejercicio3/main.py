# Ejercicio 3
# Taller: introducción a python
# Día 6

# Consigna:
#   Crea un paquete llamado utils que contenga los siguientes módulos:
#   • string.py: Contiene una función reverse_string(texto) que reciba un texto y
#     devuelva el texto invertido.
#   • list.py: Contiene una función find_max(lista) que reciba una lista de
#     números y devuelva el valor máximo.
#   Luego, en otro archivo llamado main.py, importa los módulos del paquete
#   utils y utiliza las funciones para realizar operaciones con cadenas y listas.

from utils import string, list

print(string.reverse_string(input("Ingrese algo:")))
print(list.find_max([4, -1, 9.4, 4.1]))