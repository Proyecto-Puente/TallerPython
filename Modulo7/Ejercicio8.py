# Ejercicio 8
# Taller: introducción a python
# Día 10

# Consigna:
#   Define una clase Vehiculo con atributos como marca, modelo y año.
#   Luego, crea una clase Garaje que contenga una lista de vehículos.
#   Implementa métodos para agregar un vehículo al garaje, buscar
#   vehículos por marca y mostrar todos los vehículos en el garage

class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
    
    def __str__(self) -> str:
        return f"{self.marca} {self.modelo} ({self.anio})"

class Garaje:

    capacidad = 3

    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        if len(self.vehiculos) <= self.capacidad:
            self.vehiculos.append(vehiculo)

    def buscar_por_marca(self, marca):
        vehiculos_encontrados = []
        for vehiculo in self.vehiculos:
            if vehiculo.marca == marca:
                vehiculos_encontrados.append(vehiculo)
        return vehiculos_encontrados

    def mostrar_vehiculos(self):
        print("Vehículos en el garaje:")
        for vehiculo in self.vehiculos:
            print(vehiculo)
