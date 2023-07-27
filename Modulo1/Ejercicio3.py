# Ejercicio 3
# Taller: introducción a python
# Día 1

# Consigna:
#   Desarrolla un programa que solicite al usuario dos números y realice las cuatro 
#   operaciones aritméticas básicas (suma, resta, multiplicación y división) con 
#   esos números. Imprime los resultados por pantalla.

# 1ra Forma
num1 = float(input("ingrese un numero:"))
num2 = float(input("ingrese un numero:"))

print("Suma: ", num1 + num2)
print("Resta: ", num1 - num2)
print("Producto: ", num1 * num2)
print("Division: ", num1 / num2)

# 2da Forma
num1 = float(input("ingrese un numero:"))
num2 = float(input("ingrese un numero:"))

print(num1 + num2, num1 - num2, num1 * num2, num1 / num2, sep="\n")