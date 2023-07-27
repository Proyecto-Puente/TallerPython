# Ejercicio 5
# Taller: introducción a python
# Día 3

# Consigna:
#   Escribir una función recursiva que reciba un número entero positivo y devuelva
#   el valor de la sucesión de Fibonacci para ese valor.
#
#   > Caso base: num, si (num == 0) o (num == 1)
#   >
#   > Caso gral: fibonacci(n - 1) + fibonacci(n - 2)

def fib(numero):
    if numero == 0 or numero == 1:
        return numero
    else:
        return fib(numero - 1) + fib(numero - 2)

for n in range(10):
    print(fib(n), end= " ")