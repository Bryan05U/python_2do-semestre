"""
3. Diseñar un sistema de gestión de inventario utilizando una clase Inventario que gestione múltiples objetos de tipo Producto.
Este inventario debe ser un diccionario donde las claves serán los códigos de los productos, y los valores serán instancias de cada Producto.
Además cada producto tendrá un historial de cambios en el stock utilizando una lista.
Clase Producto:
   ● Atributos:
     ○ El nombre del producto.
     ○ El precio por unidad.
     ○ La cantidad disponible del producto.
     ○ El código único (Código de Barra) del producto.
     ○ Una lista que registre el historial de cambios en el stock (incrementos o decrementos).
   ● Métodos de la clase Producto:
     ○ Crear método que actualice el stock del producto y añada el cambio al historial de stock.
     ○ Implementar método que calcule el valor total de los productos disponibles
     ○ Crear método mágico para mostrar el estado actual del producto en formato texto.
Clase Inventario:
   ● Atributos:
     ○ Un diccionario de productos donde la clave es el código del producto y el valor es una instancia de la clase Producto.
   ● Métodos de la clase Inventario:
     ○ Crear método que agregue un nuevo producto al inventario.
     ○ Implementar un método que actualice el stock de un producto en el inventario.
     ○ Crear método que muestre todos los productos del inventario y sus detalles.
     ○ Implementar un método que calcule el valor total de todos los productos en el inventario.
Se debe considerar en este ejercicio, la clase Inventario contiene productos (instancias de la clase  Producto), pero no hereda de Producto.
"""

# Creando una clase Producto y añadiendo sus atributos
class Producto:
    def __init__(self, name_producto, precio_x_unidad, cantidad, código):
        self.name_producto = name_producto
        self.precio_x_unidad = precio_x_unidad
        self.cantidad = cantidad
        self.código = código
        self.historial_stock = []

    # Método que actualiza el stock del producto y añade el cambio al historial de stock
    def update_stock(self, cantidad):
        if cantidad != 0:
            self.historial_stock.append(self.cantidad)
            self.cantidad += cantidad

    # Método que calcula el valor total de los productos disponibles
    def valor_total(self):
        return self.cantidad * self.precio_x_unidad
    
    # Método mágico que permite mostrar el estado actual del producto en formato texto
    def __str__(self):
        return (f"Nombre: {self.name_producto}\n"
                f"Precio por unidad: ${self.precio_x_unidad:.2f}\n"
                f"Cantidad disponible: {self.cantidad}\n"
                f"Código: {self.código}\n"
                f"Historial de stock: {self.historial_stock}")

# Creando una nueva clase llamado "Inventario"
# Colocando un atributo de diccionario de productos donde la clave es el código del producto y el valor es una instancia de la clase Producto.
class Inventario:
    def __init__(self):
        self.productos = {}
    
    # Método que agrega un nuevo producto al inventario
    def add_producto(self, producto):
        if producto.código not in self.productos:
            self.productos[producto.código] = producto
        else:
            print("Ya existe el producto con este código")

    # Método que actualiza el stock de un producto en el inventario
    def update_stock_producto(self, código, cantidad):
        if código in self.productos:
          self.productos[código].update_stock(cantidad)
        else:
            print("El producto con este coódigo es inexistente")

    # Método que muestre todos los productos del inventario detalladamente
    def show_productos(self):
        for producto in self.productos.values():
            print(producto)
            print("-" * 40)

    # Método que calcula el valor total de todos los productos en el inventario
    def valor_total_inventario(self):
        return sum(producto.valor_total() for producto in self.productos.values())
    
# Crear productos
product_1 = Producto("Tablet", 900, 8, "24681012")
product_2 = Producto("Laptop", 1100, 13, "21018642")

# Crear inventario
inventory = Inventario()

# Añadir productos al inventario
inventory.add_producto(product_1)
inventory.add_producto(product_2)

# Mostrar productos
inventory.show_productos()

# Actualizar stock de un producto
inventory.update_stock_producto("24681012", 4)

# Mostrar productos después de actualizar stock
inventory.show_productos()

# Calcular valor total del inventario
print(f"Valor total del inventario: ${inventory.valor_total_inventario():.2f}")