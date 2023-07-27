# Ejercicio 3
# Taller: introducción a python
# Día 8

# Consigna:
#   Escribe un programa que tome dos archivos, muestre y compare
#   información acerca de su tamaño (bytes) y fecha de modificación. Para
#   obtener la fecha de modificación y el tamaño puede utilizar os.stats y
#   para formatear la fecha time.ctime.

import os,time

archivo1 = input("ingrese la ruta: ")
archivo2 = input("ingrese la ruta: ")

if not os.path.exists(archivo1) or not os.path.exists(archivo2):
    print("Alguna ruta no es correcta.")
else:
    # Tamaño
    tamaño_arc_1 = os.path.getsize(archivo1)
    tamaño_arc_2 = os.path.getsize(archivo2)

    print("Tamaño (B):", tamaño_arc_1, tamaño_arc_2, sep="\n")

    if tamaño_arc_1 > tamaño_arc_2:
        print("El 1er archivo es mas grande.")
    else:
        print("El 2do archivo es mas grande.")

    #   Tiempo
    mod_arc_1 = os.path.getatime(archivo1)
    mod_arc_2 = os.path.getatime(archivo2)
    print("Ultima modificacion:", time.ctime(mod_arc_1), time.ctime(mod_arc_2), sep="\n")
    #   datetime
    if mod_arc_1 > mod_arc_2:
        print("El 1er archivo fue accedido recientemente.")
    else:
        print("El 2do archivo fue accedido recientemente.")