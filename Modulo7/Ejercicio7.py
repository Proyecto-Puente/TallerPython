# Ejercicio 7
# Taller: introducción a python
# Día 10

# Consigna:
#   Crea una clase Inventario con una lista de productos. Cada producto debe
#   tener un nombre, precio y cantidad en stock. Implementa métodos
#   para agregar productos, actualizar el stock y mostrar el inventario de la
#   tienda.

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self) -> str:
        return f"{self.nombre} - Precio: {self.precio}, Cantidad: {self.cantidad}"

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def actualizar_stock(self, nombre_producto, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                producto.cantidad += cantidad

    def mostrar_inventario(self):
        print("Inventario:")
        for producto in self.productos:
            print(producto)
