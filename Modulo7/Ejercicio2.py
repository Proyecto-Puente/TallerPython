# Ejercicio 2
# Taller: introducción a python
# Día 10

# Consigna:
#   Crea una clase "Vehiculo" con atributos como "marca" y "modelo".
#   Luego, crea dos clases derivadas, por ejemplo, "Auto" y "Motocicleta",
#   que hereden de la clase "Vehiculo". Implementa un método en cada
#   clase para mostrar información específica de cada vehículo.

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def __str__(self):
        return self.marca + " " + str(self.modelo)
    
    def arrancar(self):
        pass

class Moto(Vehiculo):
    def arrancar(self):
        print("tutututu")

class Auto(Vehiculo):
    def __init__(self, marca, modelo, auxilio = 1):
        super().__init__(marca, modelo)
        self.auxilio = auxilio
        
    def __str__(self):
        return super().__str__() + " " + str(self.auxilio)

    def arrancar(self):
        print("brummm")

a1 = Auto("ford", 2010, 2)
m1 = Moto("Harley", 1990)
v1 = Vehiculo("skyhawk", 1990)

print(a1,m1,v1, sep="\n")
a1.arrancar()
m1.arrancar()
print(v1.arrancar())