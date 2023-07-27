# Ejercicio 3
# Taller: introducción a python
# Día 3

# Consigna:
#   Elabore una función que retorne la letra más utilizada en un texto que obtenga como 
#   parámetro, luego permita al usuario ingresar una cadena e imprima la letra más utilizada.

# 1. El usuario ingresa una cadena
# 2. Buscar la letra que más veces aparece en la cadena
# 3. mostrar letra


def letra_mas_utilizada(texto: str) -> str:
    """Busca la letra mas utilizada.

    No considera si los caracteres aparecen la misma cantidad de veces.
    """

    # Evaluo si la cadena esta vacia
    if len(texto) == 0:
        return ""
    else:
        # Suponemos que el primer caracter es el que mas aparece
        chrMasUtilizado = texto[0]
        chrApariciones = texto.count(texto[0])
        for caracter in texto:
            # Buscamos un caracter que aparezca mas veces
            apariciones = texto.count(caracter)
            if apariciones > chrApariciones:
                # Hay un caracter que aparece mas veces, reemplazo el caracter mas utilizado
                chrMasUtilizado = caracter
                chrApariciones = apariciones
        # Retornamos el caracter mas utilizado
        return chrMasUtilizado

txt = input("Ingrese algo:")
print("caracter:", '"' + letra_mas_utilizada(txt) + '"')