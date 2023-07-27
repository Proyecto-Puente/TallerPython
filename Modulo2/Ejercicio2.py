# Ejercicio 2
# Taller: introducción a python
# Día 2

# Consigna:
#   Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

numero = int(input("Ingrese un numero: "))
if numero != 0:
  print(numero, "es par") if numero % 2 == 0 else print(numero, "es impar")
else:
  print("El numero es nulo")