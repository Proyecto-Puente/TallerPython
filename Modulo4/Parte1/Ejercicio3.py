# Ejercicio 3
# Taller: introducción a python
# Día 4

# Consigna:
#   Piense en al menos cinco lugares del mundo que te gustaría visitar, almacenar las
#   ubicaciones en una lista. Imprima su lista en su orden original.
#       1. Use sorted() para imprimir su lista en orden alfabético 
#          sin modificar la lista real. Muestre que su lista todavía está en su orden
#          original imprimiéndola.
#
#       2. Use sorted() para imprimir su lista en orden alfabético 
#          inverso sin cambiar el orden de la lista original. Muestre que su lista 
#          todavía está en su orden original imprimiéndola de nuevo.
#
#       3. Use reverse() para cambiar el orden de su lista. Imprima
#          la lista para mostrar que su el orden ha cambiado.
#
#       4. Use sort() para cambiar su lista para que se almacene en
#          orden alfabético. Imprime la lista para mostrar que su orden ha sido cambiado.
#
#       5. Use sort() para cambiar su lista para que se almacene en
#          orden alfabético inverso. Imprima la lista para mostrar que su orden ha cambiado.

lugares = ["Ushuaia", "Antartida", "Jujuy", "Misiones", "Dinamarca", "Holanda"]
# 1
print("Lugares (sorted) :", sorted(lugares))
print("Lugares (original) :", lugares, "\n")
# 2
print("Lugares (sorted [reverse]) :", sorted(lugares, reverse = True))
print("Lugares (original) :", lugares, "\n")
# 3
lugares.reverse()
print("Lugares (reverse) :", lugares, "\n")
# 4
lugares.sort()
print("Lugares ordenados (A, ..., Z) :",lugares, "\n")
# 5
lugares.sort(reverse = True)
print("Lugares ordenados (Z, ..., A) :",lugares, "\n")