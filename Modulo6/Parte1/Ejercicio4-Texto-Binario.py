# Ejercicio 4
# Taller: introducción a python
# Día 7

# Consigna:
#   Escribe un programa que tome un archivo de texto
#   y lo convierta en un archivo binario con el mismo contenido. Luego,
#   crea otro programa para revertir el proceso y obtener el archivo de
#   texto original.

# Puedes utilizar la función ord() para obtener el valor ASCII de cada carácter
# del archivo de texto y luego convertirlo a binario utilizando la función bin().

with open('archivo.txt', 'r') as f:
    texto = f.read()

binario = ''.join(format(ord(i), '08b') for i in texto)

with open('archivo.bin', 'wb') as f:
    f.write(bytes(int(binario[i:i+8], 2) for i in range(0, len(binario), 8)))