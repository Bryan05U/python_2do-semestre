"""
Aprender a usar los métodos setters y getters para controlar el acceso a los atributos de una clase.
1. Crea una clase llamada Producto
2. La clase Producto debe tener los siguientes atributos privados:
   - nombre (una cadena de texto)
   - precio (un número flotante)
3. Define:
   - Un getter para obtener el valor del atributo 'nombre'.
   - Un setter para modificar el atributo 'nombre'. El setter debe asegurarse de que el nombre no sea vacío.
   - Un getter para obtener el valor del atributo 'precio'.
   - Un setter para modificar el atributo 'precio'. El setter debe asegurarse de que el precio sea positivo.
4. Luego crea un objeto de tipo Producto y realiza lo siguiente:
   - Establece un nombre y un precio usando los setters.
   - Obtén el nombre y el precio usando los getters.
"""

class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio

    # Getter para el nombre
    def get_nombre(self):
        return self.__nombre
    
    # Setter para el nombre
    def set_nombre(self, nombre):
        if nombre:
            self.__nombre = nombre
        else:
            print(f"El nombre no puede estar vacío.")

    # Getter para el precio
    def get_precio(self):
        return self.__precio
    
    # Setter para el precio
    def set_precio(self, precio):
        if precio > 0:
            self.__precio = precio
        else:
            print(f"Precio inválido")

# Crear objetos de la clase Producto
producto_1 = Producto("Collar", 15000)
producto_2 = Producto("Lentes de sol", 7500)

# Obtener el nombre y precio usando los getters
print(f"Producto 1 - Nombre: {producto_1.get_nombre()}, Precio: {producto_1.get_precio()}")
print(f"Producto 2 - Nombre: {producto_2.get_nombre()}, Precio: {producto_2.get_precio()}")

# Modificar el nombre y el precio usando los setters
producto_1.set_nombre("Chaqueta")
producto_1.set_precio(90000)

#producto_2.set_nombre("")
#producto_2.set_precio(-999)

# Obtener los valores actualizados usando los getters
print("\nDespués de la modificación:")
print(f"Producto 1 - Nombre: {producto_1.get_nombre()}, Precio: {producto_1.get_precio()}")
print(f"Producto 2 - Nombre: {producto_2.get_nombre()}, Precio: {producto_2.get_precio()}")