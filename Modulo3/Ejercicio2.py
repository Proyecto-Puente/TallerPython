# Ejercicio 2
# Taller: introducción a python
# Día 3

# Consigna:
#   Cálculo del volumen de un cilindro: Crea una función llamada “volumen_cilindro"
#   que reciba como argumento el radio y la altura del cilindro, debe retornar el volumen.
#   Luego, pida al usuario que ingrese los datos y muestra el volumen.
#
#   > Formula: `Volumen = area x altura`

# 1.ingresar el radio
# 2.ingresar la altura
# 3.calcular volumen
# 4.mostrar volumen

# La funcion area_circulo esta declarada arriba...

from Ejercicio1 import area_circulo

def volumen_cilindro(radio, altura):
    """Calcula el volumen de un cilindro"""
    if altura > 0:
        return area_circulo(radio) * altura
    else:
        return 0

radio = float(input("Ingrese el radio: "))
altura = float(input("Ingrese la altura: "))
print("Volumen:", round(volumen_cilindro(radio, altura), 3))