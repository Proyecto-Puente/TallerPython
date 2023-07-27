# Ejercicio 2
# Taller: introducción a python
# Día 6

# Consigna:
#   Crea un paquete llamado geometria que contenga dos módulos:
#   • circulo.py: Contiene una función area(radio) que reciba el radio de un
#     círculo y devuelva su área.
#   • rectangulo.py: Contiene una función area(base, altura) que reciba la base y
#     la altura de un rectángulo y devuelva su área.
#   Luego, en otro archivo llamado main.py, importa los módulos del paquete
#   geometria y utiliza las funciones para calcular áreas de círculos y rectángulos.

from geometria import circulo, rectangulo

print(round(circulo.area(5.75), 3))
print(round(rectangulo.area(21.0, 29.7), 3))