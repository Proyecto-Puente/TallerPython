# Ejercicio 7
# Taller: introducción a python
# Día 4

# Consigna:
#   Escribir un programa que almacene el abecedario en una lista, elimine de la
#   lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

# Con compresion
abc = "abcdefghijklmnopqrstuvwxyz"
abc = [letra for posicion, letra in enumerate(abc) if posicion % 3 == 0 and posicion != 0]
print(abc)

# Sin compresion
abc = "abcdefghijklmnopqrstuvwxyz"
for posicion, letra in enumerate(abc):
  if posicion % 3 == 0 and posicion != 0:
    print(letra, end=" ")