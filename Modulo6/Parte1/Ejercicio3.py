# Ejercicio 3
# Taller: introducción a python
# Día 7

# Concatenar archivos: Diseña un programa que tome varios archivos de
# texto y los combine en un solo archivo. El usuario debe poder
# especificar el orden de concatenación.

def archivo_valido(ruta):
    from os.path import isfile, exists
    return isfile(ruta) and exists(ruta)

def combinar_archivos(archivo_combinado, archivo_copiar):
    # Abrimos los archivos, uno para lectura y el otro para extenderlo
    archivo1 = open(archivo_combinado, "rt")
    archivo2 = open(archivo_copiar, "at")

    aux = archivo1.readlines()
    archivo2.writelines(aux)

    archivo1.close()
    archivo2.close()
    
# El usuario ingresa la ruta del archivo que combinara el conjunto
continuar = True
while continuar:
    archivo_combinado = input("Ingrese la ruta del archivo de texto:")
    continuar = not archivo_valido(archivo_combinado)

# El usuario ingresa las rutas de los archivos a copiar
archivos = []
while True:
    # Añadir rutas de archivos a copiar
    ruta_archivo = input("Ingrese la ruta del archivo de texto:")
    if archivo_valido(ruta_archivo):
        archivos.append(ruta_archivo)
    else:
        print("Verifique la ruta.")
    
    # Verificar si continua el ingreso...
    # Nota: si ingresa un valor incorrecto, la ejecucion continua
    match (input("¿Desea agregar archivos? (si-no)").strip()).lower():
        case "si":
            continue
        case "no":
            break
        case _:
            print("Valor incorrecto.")
    
for archivo in archivos:
    combinar_archivos(archivo_combinado, archivo)