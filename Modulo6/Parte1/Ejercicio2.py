# Ejercicio 2
# Taller: introducción a python
# Día 7

# Copiar archivos: Crea un programa que copie el contenido de un
# archivo de texto a otro archivo nuevo. Asegúrate de manejar
# correctamente el cierre de ambos archivos.

from os.path import isfile, exists

ruta_archivo_1  = input("Ingrese la ruta del archivo de texto:")
ruta_archivo_2  = input("Ingrese la ruta del archivo de texto:")

# Ley de Morgan:
#   no (p y q) = (no p) o (no q)
#
if not exists(ruta_archivo_1) or not exists(ruta_archivo_2):
    print("La ruta no es valida.")
elif not (isfile(ruta_archivo_1) and isfile(ruta_archivo_2)):
    print("Debe ingresar un archivo.")
else:
    # Abrimos los archivos, uno para lectura y el otro para extenderlo
    archivo1 = open(ruta_archivo_1, "rt")
    archivo2 = open(ruta_archivo_2, "at")

    aux = archivo1.readlines()
    archivo2.writelines(aux)

    archivo1.close()
    archivo2.close()