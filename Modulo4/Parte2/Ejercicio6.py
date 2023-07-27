# Ejercicio 6
# Taller: introducción a python
# Día 5

# Consigna:
#   Escribir un programa que cree un diccionario vacío y lo vaya llenado
#   con información sobre una persona (por ejemplo nombre, edad, sexo,
#   teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez
#   que se añada un nuevo dato debe imprimirse el contenido del
#   diccionario.

persona = {}
while True:
    clave = input("Ingrese el nombre del atributo: ")
    valor = input("Ingrese el valor del atributo: ")
    persona[clave] = valor

    if input("¿Desea continuar?, ('s' o 'n')").lower().strip() != "s":
        break

print(persona)