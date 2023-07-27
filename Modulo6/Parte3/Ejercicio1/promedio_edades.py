# Ejercicio 1
# Taller: introducción a python
# Día 9

# Contador de palabras: Desarrolla un programa que lea un archivo de
# texto y cuente cuántas veces aparece cada palabra. Luego, imprime el
# resultado en orden alfabético.

from os.path import isfile, exists

ruta = input("Ingrese la ruta del archivo de texto:")

if not exists(ruta):
    print("La ruta no es valida.")
elif not isfile(ruta):
    print("Debe ingresar un archivo.")
else:
    palabras = []
    with open(ruta, "rt") as txt:
        # Separo cada palabra por cada linea del archivo de texto
        for linea in txt:
            # Almaceno las palabras en la lista "palabras"
            palabras.extend(linea.split(" "))
    # Ordeno alfabeticamente las palabras
    palabras.sort()
    # Cuenta las repeticiones y las muestra
    print({palabra: palabras.count(palabra) for palabra in palabras})
    