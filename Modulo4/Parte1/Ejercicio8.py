# Ejercicio 8
# Taller: introducción a python
# Día 4

# Consigna:
#   Escribir un programa que pida al usuario una palabra y muestre por
#   pantalla si es un palíndromo (se lee igual al revés).

palabra = list(input("Ingrese una palabra:"))
reves = list(reversed(palabra))
print("Es palindromo." if palabra == reves else "No es palindromo.")