# Ejercicio 4
# Taller: introducción a python
# Día 2

# Consigna:
#   Escribir un programa que pida al usuario un número entero positivo y muestre
#   por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

numero = int(input("Ingrese un numero: "))
if numero >= 1:
  for n in reversed(range(numero+1)):
    print(n)


# Este agrega una funcion que duerme por un segundo al hilo.
from time import sleep

numero = int(input("Ingrese un numero: "))
if numero >= 1:
  for n in reversed(range(numero+1)):
    print(n)
    sleep(1)