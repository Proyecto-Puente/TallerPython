# Ejercicio 1
# Taller: introducción a python
# Día 3

# Consigna:
#   Cálculo del área de un círculo: Crea una función llamada "area_circulo" que reciba 
#   como argumento el radio de un círculo y retorne el área correspondiente. 
#   Luego, pide al usuario que ingrese el radio y muestra el área calculada.
#
#   > Para utilizar el número pi, deberá importarlo con `from math import pi`
#   >
#   > Formula: `area = pi x radio^2`

# 1.ingresar el radio
# 2.calcular area
# 3.mostrar area

def area_circulo(radio):
    """Calcula el area de un ciculo"""
    if radio > 0:
        from math import pi
        return pi * radio ** 2
    else:
        return 0

radio = float(input("Ingrese el radio: "))
print("Area:", round(area_circulo(radio), 3))