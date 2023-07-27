# Ejercicio 1
# Taller: introducción a python
# Día 5

# Consigna:
#   Escribe un programa que pida un número por teclado y que cree un
#   diccionario cuyas claves sean desde el número 1 hasta el número indicado,
#   y los valores sean los cuadrados de las claves.

num = int(input("Ingrese un numero:"))

cuadrados = {}
for i in range(num):
    cuadrados.update({i: i**2})
    #cuadrados[i] = i**2
print(cuadrados)

# Otra forma, utilizando compresion
numero = int(input("Ingrese un numero:"))
diccionario = {x: x**2 for x in range(numero) if numero > 0}
print(diccionario)