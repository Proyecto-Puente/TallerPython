# Ejercicio 5
# Taller: introducción a python
# Día 7

# Logging es un medio de rastrear los eventos que ocurren cuando se ejecuta algún software. 
# El desarrollador del software agrega llamadas de registro a su código para indicar que 
# ciertos eventos han ocurrido. Un evento se describe mediante un mensaje descriptivo que 
# puede contener opcionalmente datos variables (es decir, datos que son potencialmente diferentes
# para cada ocurrencia del evento). Los eventos también tienen una importancia que el 
# desarrollador atribuye al evento.

# Este ejercicio no tiene fines practicos, la solucion a este tipo de requerimientos suele solucionarse de otra forma.

# Consigna:
#   Registro de acceso: Crea un programa que registre las horas de acceso
#   de los usuarios a una plataforma en un archivo de texto. Cada línea
#   debe contener el nombre de usuario y la fecha y hora de acceso.

import logging, time, sys

def registrar(nombre_usuario):
    logging.basicConfig(filename='registro.log', level=logging.INFO)
    logging.info(f'{time.strftime("%Y/%m/%d - %H:%M:%S")} - {nombre_usuario}')

def main():
    registrar(sys.argv[1])

if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.argv.append("LuisPerez")
    main()