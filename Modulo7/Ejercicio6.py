# Ejercicio 6
# Taller: introducción a python
# Día 10

# Consigna:
#   Define una clase Circulo con un atributo radio. Agrega métodos para
#   calcular el área. Luego, crea una clase Cilindro que herede de Circulo 
#   y tenga un atributo adicional altura. Sobrescribe
#   los métodos de cálculo de área y volumen para el cilindro.

from Ejercicio4 import Circulo

class Cilindro(Circulo):
    def __init__(self, radio, altura):
        super().__init__(radio)
        self.altura = altura

    def calcular_volumen(self):
        return super().calcular_area() * self.altura
    