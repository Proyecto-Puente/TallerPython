# Ejercicio 1
# Taller: introducción a python
# Día 8

# Consigna:
#   Desarrolla un programa que permita al usuario copiar todos los
#   archivos desde una ubicación a otra. Si el archivo ya existe en el
#   destino, el programa debe solicitar al usuario que ingrese un nuevo
#   nombre para el archivo y copiarlo con el nuevo nombre.

import os
import shutil

def copy_files(src_dir, dst_dir):
    for file_name in os.listdir(src_dir):
        src_file = os.path.join(src_dir, file_name)
        dst_file = os.path.join(dst_dir, file_name)
        if os.path.exists(dst_file):
            new_file_name = input(f"El archivo {file_name} ya existe en {dst_dir}. Por favor ingrese un nuevo nombre para el archivo: ")
            dst_file = os.path.join(dst_dir, new_file_name)
        shutil.copy(src_file, dst_file)

if __name__ == "__main__":
    while True:
        origen = input("Ruta de origen:")
        destino = input("Ruta de destino:")
        if os.path.exists(origen) and os.path.exists(destino):
            copy_files(origen, destino)
            break
        else:
            print("Verifique las rutas. Deben ser directorios.")