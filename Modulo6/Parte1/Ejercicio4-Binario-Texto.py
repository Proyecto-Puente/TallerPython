# Ejercicio 4
# Taller: introducción a python
# Día 7

# Consigna:
#   Escribe un programa que tome un archivo de texto
#   y lo convierta en un archivo binario con el mismo contenido. Luego,
#   crea otro programa para revertir el proceso y obtener el archivo de
#   texto original.

# Para revertir el proceso y obtener el archivo de texto original a partir del 
# archivo binario, puedes leer los bytes del archivo binario y luego
# convertirlos a caracteres utilizando la función chr()

with open('archivo.bin', 'rb') as f:
    binario = f.read()

texto = ''.join(chr(int(binario[i:i+8], 2)) for i in range(0, len(binario), 8))

with open('archivo.txt', 'w') as f:
    f.write(texto)

