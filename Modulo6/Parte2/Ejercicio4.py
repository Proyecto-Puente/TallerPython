# Ejercicio 4
# Taller: introducción a python
# Día 8

# Consigna:
#   Escribe un programa que tome una ruta de origen, en base a la
#   extensión de los archivos que se encuentra en la ruta(ej. .EXE, .DOCX,
#   .JPEG, etc.), los moverá en carpetas dependiendo de su extensión (ej.
#   Documentos, Imágenes, Videos, Ejecutables, etc.)

# Como puedo mejorarlo:
#   - Admitir parametros para modificar la forma de ordenado, el renombrado, etc. (sys.args)
#   - Uso de archivo de configuracion para ingresar las extensiones (configparser)
#   - Generar logs (logging)
#   - Brindar informacion estadistica
#   - GUI (tkinter)
#   - Admitir expresiones regulares
#   Mejoralo en base a tus necesidades...

import os, shutil
from datetime import datetime

def ordenar(src_dir, dst_dir):
    contador = 0
    inicio = datetime.now()

    carpetas = {
        'Ejecutables': ['.exe'],
        'Documentos': ['.docx', '.txt', '.doc', 'xls', 'xlsx', 'pptx', '.pdf'],
        'Imágenes': ['.jpg', '.png', '.svg', '.raw'],
        'Videos': ['.mp4', '.avi'],
        'Audio': ['.mp3', '.wav', '.ogg']
    }

    for nombre_archivo in os.listdir(src_dir):
        # obtengo la ruta completa de origen del archivo
        src_archivo = os.path.join(src_dir, nombre_archivo)
        # evaluo si es un archivo
        if os.path.isfile(src_archivo):
            # obtengo su extension
            extension = os.path.splitext(nombre_archivo)[1]
            # verifico si la extension esta en una lista que contiente todas las extensiones soportadas.
            if extension in [extension for lista in carpetas.values() for extension in lista]:
                for carpeta, extensiones in carpetas.items():
                    if extension in extensiones:
                        dst_directorio = os.path.join(dst_dir, carpeta)
                        
                        # si no existe la carpeta, la crea
                        if not os.path.exists(dst_directorio):
                            print(datetime.now(),"Informacion", f"Creando carpeta - {dst_directorio}.", sep=" - ")
                            os.makedirs(dst_directorio)
                        
                        # verifico si el archivo existe, si es así, solicita un cambio de nombre
                        dst_archivo = os.path.join(dst_directorio, nombre_archivo)
                        if os.path.exists(dst_archivo):
                            print(datetime.now(), "Advertencia", f"El archivo {nombre_archivo} existe en {dst_directorio}.", sep=" - ")
                            # new_nombre_archivo = input(f"El archivo {nombre_archivo} ya existe en {dst_directorio}. Por favor ingrese un nuevo nombre para el archivo: ")
                            # dst_archivo = os.path.join(dst_directorio, new_nombre_archivo)
                        
                        # mueve el archivo
                        print(datetime.now(), "Informacion", f"Moviendo - Archivo: {src_archivo} -> {dst_archivo}.", sep=" - ")
                        shutil.move(src_archivo, dst_archivo)
                        contador += 1
    print("Archivos:", contador, "Tiempo:", datetime.now() - inicio)

if __name__ == "__main__":
    while True:
        origen = input("Ruta de origen:")
        destino = input("Ruta de destino:")
        if os.path.exists(origen):
            ordenar(origen, destino)
            break
        else:
            print("Verifique las rutas. Deben ser directorios.")