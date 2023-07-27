# Ejercicio 3
# Taller: introducción a python
# Día 5

# Consigna:
#   Escribir un programa que cree un diccionario de traducción español-inglés. El
#   usuario introducirá las palabras en español e inglés separadas por dos
#   puntos, y cada par "palabra":"traducción" separados por comas. El
#   programa debe crear un diccionario con las palabras y sus traducciones

palabras = input(">>>")

diccionario = {}
for par in palabras.split(","):
    diccionario.update([tuple(par.split(":"))])

# update([(k,v),...,(k,v)])
print("Palabras en español:")
for palabra in diccionario.keys():
    print("\t",palabra)

print("Palabras en Ingles:")
for palabra in diccionario.values():
    print("\t",palabra)
