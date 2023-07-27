# Ejercicio 1
# Taller: introducción a python
# Día 10

# Consigna:
#   Define una clase llamada "Persona" con atributos como "nombre" y
#   "edad". Crea un objeto a partir de la clase y muestra los detalles de la
#   persona.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return self.nombre + " " + str(self.edad)

p1 = Persona("Juan", 39)
p2 = Persona("Pedro", 57)
print(str(p1), p2, sep="\n")