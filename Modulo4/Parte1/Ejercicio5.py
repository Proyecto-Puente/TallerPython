# Ejercicio 5
# Taller: introducción a python
# Día 4

# Consigna:
#   Crea un programa que solicite al usuario una lista de
#   números separados por comas. Luego, utiliza una función para sumar todos
#   los elementos de la lista y mostrar el resultado por pantalla. Puedes utilizar
#   la función `split()` para dividir la cadena ingresada por el usuario en una lista de números.

cadena = input("Ingrese elementos separados por ',': ")
numeros = [float(caracter) for caracter in cadena.split(',')]
print(sum(numeros))