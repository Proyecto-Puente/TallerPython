# Ejercicio 3
# Taller: introducción a python
# Día 5

# Consigna:
#   Escribir un programa que cree un diccionario de traducción español-inglés. El
#   usuario introducirá las palabras en español e inglés separadas por dos
#   puntos, y cada par "palabra":"traducción" separados por comas. El
#   programa debe crear un diccionario con las palabras y sus traducciones

# Este permite:
#   Asignar palabras
#   Buscar traduccion de palabras

def separar_traducciones(palabras, separador_def = ":" , separador_palabras = ","):
    '''Genera un diccionario de definiciones.

    Separa un texto con formato: "clave1:valor1, ... ,claveN:valorN".
    Muestra de entrada (palabras): mesa:table,hola:hello,adios:goodbye
    '''
    return dict([tuple(par.split(separador_def)) for par in palabras.split(separador_palabras)])

def mostrar_definiciones(diccionario, orden = True):
    '''Imprime todas las definiciones.

    Dado un diccionario, imprime todas las definiciones del diccionario segun su orden.
    Si orden es falso, entonces imprime ingles a español, sino español a ingles.
    '''
    print("Diccionario:", "\n\t Español -> Ingles" if orden else "\n\t Ingles -> Español")
    for esp, ing in diccionario.items():
        print("\t", (esp + " -> " + ing) if orden else (ing + " -> " + esp))

def tiene_separadores(palabras, separador_def = ":" , separador_palabras = ","):
    '''Retorna si un texto tiene los caracteres especificados'''
    return palabras.find(separador_def) != -1 or palabras.find(separador_palabras) != -1

def buscar_clave(diccionario, valor):
    try:
        pos = list(diccionario.values()).index(valor)
        return list(diccionario.keys())[pos]
    except ValueError:
        return None

diccionario = {}
while True:
    entrada = (input(">>> ")).upper()
    if entrada == "SALIR":
        break
    elif not tiene_separadores(entrada):
        busqueda = diccionario.get(entrada)
        print(entrada, "->", busqueda if diccionario.get(entrada) != None else buscar_clave(diccionario, entrada))
    else:
        diccionario.update(separar_traducciones(entrada))
        mostrar_definiciones(diccionario)