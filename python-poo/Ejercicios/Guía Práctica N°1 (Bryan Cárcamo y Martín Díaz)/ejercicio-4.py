"""
4. Implementar una clase Pedido que represente un pedido en un restaurante.
Cada pedido tiene un número de mesa, una lista de platos pedidos y el total del costo del pedido.
Clase Pedido:
   ● Atributos:
     ○ Número de mesa, lista de platos, y el total del pedido.
   ● Métodos:
     ○ Crear método para añadir platos al pedido (cada plato tiene un nombre y un precio).
     ○ Crear método para calcular el total del pedido.
     ○ Implementar un método mágico para contar el número de platos en el pedido.
     ○ Implementar un método mágico para combinar dos pedidos de la misma mesa (sumar platos y total).
   ● Finalizador:
     ○ Al eliminar un pedido, mostrar un mensaje indicando que el pedido ha sido completado.
"""

# Creando una clase Pedido y añadiendo sus atributos
class Pedido:
    def __init__(self, n_mesa):
        self.n_mesa = n_mesa
        self.list_platos = [] # Lista para almacenar los platos como tuplas (nombre, precio)
        self.pedido_total = 0.0

    # Método para añadir platos al pedido (cada plato tiene un nombre y un precio)
    def añadir_platos(self, nombre, precio):
        # Añade un plato al pedido y actualiza el total
        self.list_platos.append((nombre, precio))
        self.calcular_total()
    
    # Método para calcular el total del pedido sumando los precios de todos los platos
    def calcular_total(self):
        self.pedido_total = sum(precio for _, precio in self.list_platos)

    # Método mágico para contar el número de platos en el pedido
    def __len__(self):
        return len(self.list_platos)
    
    # Método mágico para combinar dos pedidos de la misma mesa (sumar platos y total)
    def __add__(self, otro_pedido):
        if self.n_mesa == otro_pedido.n_mesa:
            pedido_nuevo = Pedido(self.n_mesa)
            pedido_nuevo.list_platos = self.list_platos + otro_pedido.list_platos
            pedido_nuevo.calcular_total()
            return pedido_nuevo
        else:
            raise ValueError("Inválido combinar pedidos de distintas mesas")
        
    # Finalizador que muestra un mensaje indicando que el pedido ha sido completado
    def __del__(self):
        print(f"El pedido de la mesa {self.n_mesa} ha sido completado")

    # Representa una cadena del pedido para una visualización más fácil
    def __repr__(self):
        platos_str = ','.join(f"{nombre} (${precio:.2f}))" for nombre, precio in self.list_platos)
        return f"Pedido(mesa={self.n_mesa}, platos=[{platos_str}], total=${self.pedido_total:.2f})"
    
pedido1 = Pedido(1)
pedido1.añadir_platos("Pichanga", 10.5)
pedido1.añadir_platos("Ensalada rusa", 5.5)

pedido2 = Pedido(1)
pedido2.añadir_platos("Salmón", 8.0)

pedido_combinado = pedido1 + pedido2
print(pedido_combinado)
del pedido_combinado