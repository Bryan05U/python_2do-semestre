"""
5. Desarrollar un sistema de gestión de una biblioteca donde se pueda agregar y administrar libros.
Cada libro tiene un título, autor, año de publicación, y cantidad disponible del libro.
La biblioteca es responsable de gestionar los libros y permitir la búsqueda de libros por título.
Considerar crear la clase Biblioteca que debe manejar múltiples instancias de la clase Libro utilizando un diccionario.
Los libros se pueden agregar, buscar y actualizar
"""

# Creando una clase Libro y añadiendo sus atributos
class Libro:
    def __init__(self, título, autor, año_publicación, cantidad):
        self.título = título
        self.autor = autor
        self.año_publicación = año_publicación
        self.cantidad = cantidad

    # Método mágico que muestra la información del libro
    def __str__(self):
        return (f"Título: {self.título}, Autor: {self.autor}, "
                f"Año de Publicación: {self.año_publicación}, Cantidad: {self.cantidad}")
    
# Creando otra clase llamada "Biblioteca"
# Usar un diccionario donde la clave sería almacenar los libros con el título
class Bibloteca:
    def __init__(self):
        self.libros = {}

    def add_libro(self, libro):
        if libro.título in self.libros:
            # Se actualiza la cantidad si ya hay un libro existente
            self.libros[libro.título].cantidad += libro.cantidad
        else:
            # En caso contrario, se agrega al diccionario
            self.libros[libro.título] = libro
            
    # Buscar el libro por título en el diccionario
    def search_libro(self, título):
        libro = self.libros.get(título)
        if libro:
           return libro
        else:
           return "No se encuentra el libro"
        
    # Actualizar la cantidad del libro si existe
    def update_libro(self, título, cantidad):
        libro = self.libros.get(título)
        if libro:
           libro.cantidad = cantidad
        else:
            return "No se encuentra el libro para actualizar"
        
bookshelf = Bibloteca()
book_1 = Libro("1984", "George Orwell", 1949, 5)
book_2 = Libro("El Padrino", "Mario Puzo", 1969, 3)

bookshelf.add_libro(book_1)
bookshelf.add_libro(book_2)

# Buscar libros
print(bookshelf.search_libro("1984"))
print(bookshelf.search_libro("El Padrino"))

# Actualizar cantidad de libros
bookshelf.update_libro("El Padrino", 5)

# Verificar si el libro se actualizó
print(bookshelf.search_libro("El Padrino"))