# Ejercicio 4
# Taller: introducción a python
# Día 3

# Consigna:
#   Escribir una función recursiva que reciba un número entero positivo y devuelva su factorial.
#
#   > Caso base: 1, si numero == 0
#   >
#   > Caso general: numero * factorial(numero - 1)

def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero-1)

#factorial(5) -> 5! = 1*2*3*4*5 = 120
numero = int(input("num:"))
print(factorial(numero))