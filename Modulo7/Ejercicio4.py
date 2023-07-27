# Ejercicio 4
# Taller: introducción a python
# Día 10

# Consigna:
#   Crea una clase abstracta llamada "FiguraGeometrica" con un método
#   abstracto "calcular_area()". Luego, crea clases derivadas para
#   representar círculos, rectángulos y triángulos, cada una implementando
#   el método para calcular el área correspondiente.

import abc
from math import pi

class FiguraGeometrica(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def calcular_area(self):
        pass

class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return pi * self.radio ** 2

class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura / 2

class Triangulo(FiguraGeometrica):
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_area(self):
        s = (self.lado1 + self.lado2 + self.lado3) / 2
        return (s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3)) ** 0.5
