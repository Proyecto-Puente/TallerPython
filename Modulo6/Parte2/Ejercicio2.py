# Ejercicio 2
# Taller: introducción a python
# Día 8

# Consigna:
#   Crea un programa que lea un archivo desde el usuario y lo elimine.
#   Antes de eliminarlo, el programa debe solicitar una confirmación del
#   usuario. Si el usuario confirma la eliminación, el archivo debe
#   eliminarse. Si el usuario cancela la operación, el programa debe
#   mostrar un mensaje indicando que la eliminación fue cancelada.

import os

def eliminar_archivo(ruta_archivo):
    confirmacion = input(f"¿Está seguro de que desea eliminar el archivo {ruta_archivo}? (s/n): ")
    match confirmacion.lower():
        case "s":
            os.remove(ruta_archivo)
            print(f"El archivo {ruta_archivo} ha sido eliminado.")
        case "n":
            print("La eliminación ha sido cancelada.")
        case _:
            print("Valor incorrecto. La eliminación ha sido cancelada.")

def get_ruta_archivo():
    while True:
        ruta_archivo = input("Ruta del archivo a eliminar:")
        if os.path.exists(ruta_archivo):
            if os.path.isfile(ruta_archivo):
                return ruta_archivo
        print("La ruta no es valida.")

if __name__ == "__main__":
    eliminar_archivo(get_ruta_archivo())