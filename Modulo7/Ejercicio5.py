# Ejercicio 5
# Taller: introducción a python
# Día 10

# Consigna:
#   Crea una clase Libro con atributos como título, autor y año de
#   publicación. Luego, crea una clase Biblioteca que contenga una lista de
#   libros. Implementa métodos para agregar un libro a la biblioteca,
#   buscar un libro por título y mostrar todos los libros.

import datetime

class Libro:
    def __init__(self, titulo, autor, publicacion, isbn):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.publicacion = publicacion

    def __str__(self) -> str:
        return f"{self.isbn} {self.titulo} {self.autor} \t{self.publicacion}"

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__libros = []

    def getLibros(self):
        return sorted(self.__libros, key = lambda obj: obj.titulo)
    
    def getLibro(self, titulo):
        busqueda = list(filter(lambda obj: obj.titulo == titulo,self.__libros))
        return busqueda[0] if len(busqueda) > 0 else -1

    def addLibro(self, libro: Libro):
        self.__libros.append(libro)

    def mostrarLibros(self):
        print("NRO", "ISBN", "NOMBRE", "\t\tPUBLICACION", sep = "\t")
        for nro, libro in enumerate(self.getLibros()):
            print(nro + 1, libro)

if __name__ == "__main__":
    biblioteca = Biblioteca("Musacchio")

    biblioteca.addLibro(Libro("UML y Patrones", "Larman", 2005, 9788420534381))
    biblioteca.addLibro(Libro("ING. Software", "Pressman", 2006, 9786071503145))
    biblioteca.addLibro(Libro("Clean code", "R. Martin", 2008, 9780132350884))

    print("busqueda:", biblioteca.getLibro("UML y Patrones"))

    biblioteca.mostrarLibros()