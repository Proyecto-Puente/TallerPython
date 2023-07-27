# Ejercicio 5
# Taller: introducción a python
# Día 5

# Consigna:
#   Escribir un programa que guarde en un diccionario los precios de las
#   frutas, pregunte al usuario por una fruta, un número de kilos y muestre
#   por pantalla el precio de ese número de kilos de fruta. Si la fruta no
#   está en el diccionario debe mostrar un mensaje informando de ello.

frutas = {"naranja":987,
          "mandarina":693.75,
          "frutilla":1892.99}

eleccion = (input("ingrese el nombre de la fruta:")).lower()
if eleccion in frutas.keys():
    kg = float(input("ingrese los kg:"))
    print("Precio:", frutas[eleccion] * kg)
else:
    print("Fruta no encontrada.")