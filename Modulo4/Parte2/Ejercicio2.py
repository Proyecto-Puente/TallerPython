# Ejercicio 2
# Taller: introducción a python
# Día 5

# Consigna:
#   Escribe un programa que lea una cadena y devuelva un diccionario con
#   la cantidad de apariciones de cada letra en la cadena

cadena =  input("Ingrese un texto:")
apariciones = {}
for caracter in cadena:
    apariciones[caracter] = cadena.count(caracter)

print(apariciones)

# Otra forma, utilizando compresion
cadena =  input("Ingrese un texto:")
apariciones = {caracter: cadena.count(caracter) for caracter in cadena}
print(apariciones)