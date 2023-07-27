# Ejercicio 6
# Taller: introducción a python
# Día 4

# Consigna:
#   Escribe un programa que solicite al usuario una
#   lista de números separados por comas. Utiliza una función para ordenar los
#   números de forma ascendente y muestra la lista ordenada por pantalla.
#   Puedes utilizar la función `split()` y la función `sort()` para ordenar los
#   elementos de la lista.

cadena = input("Ingrese elementos separados por ',': ")
numeros = [float(caracter) for caracter in cadena.split(',')]
numeros.sort()
print(numeros)