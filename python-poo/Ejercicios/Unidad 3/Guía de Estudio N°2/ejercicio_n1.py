"""
Una empresa de eventos desea implementar un sistema que gestione la venta de tickets,
calcule los ingresos y administre un descuento especial para tickets comprados

Requisitos:

1. Variables de Clase
Crear un descuento por compras en grupo, inicializado en 20%

2. Encapsulación y Atributos Privados
● Crear un diccionario que guarda el tipo de ticket y su precio.
● Crear una lista de ventas registradas.

3. Interfaz y Métodos
● Crear un método que agregue un tipo de ticket al sistema.
● Crear un método que registra la venta de tickets. Se debe asegurar de que el tipo de ticket exista (utilizando asertos)

4. Métodos Estáticos y Asertos
● Crear un método estático que calcule el total de la venta considerando el descuento de grupo.

5. Especificación e Invariantes
● Asegurar que todos los precios sean positivos y que el tipo de ticket exista antes de la venta.

Aplicar los conceptos de variables de clase, encapsulación, asertos y métodos estáticos
en un sistema de venta de tickets para eventos.
"""

# 1)
# Variable de clase para el descuento por compras en grupo
class Sistema_Venta_de_Tickets:
    GRUPO_DE_DESCUENTO = 0.2 # 20% de descuento
    
    # 2)
    def __init__(self):
        # Diccionario que guarda el tipo de ticket y su precio
        self._tipos_tickets = {}
        # Lista de registro de ventas
        self._ventas = []

    # 3)
    def añadir_tipo_ticket(self, tipo, precio):
        # Asegure que el precio no sea un valor negativo
        assert precio > 0, "El precio debe ser positivo"
        self._tipos_tickets[tipo] = precio

    def registrar_venta(self, tipo, cantidad):
        # Asegure que el tipo de precio exista
        assert tipo in self._tipos_tickets, f"El tipo de ticket '{tipo}' es inexistente"
        # Asegure que la cantidad no sea un valor negativo
        assert cantidad > 0, "La cantidad debe ser positiva"
        
        precio_unitario = self._tipos_tickets[tipo]
        ventas_totales = self.calcular_ventas_totales(precio_unitario, cantidad)
        self._ventas.append({"Tipo": tipo, "Cantidad": cantidad, "Total": ventas_totales})

    # 4)
    @staticmethod
    def calcular_ventas_totales(precio_unitario, cantidad):
        total = precio_unitario * cantidad
        # Comprar más de 5 tickets se le aplica descuento
        if cantidad > 5:
            total -= total * Sistema_Venta_de_Tickets.GRUPO_DE_DESCUENTO
        return total

    def obtener_ventas(self):
        return self._ventas

    def obtener_tipos_tickets(self):
        return self._tipos_tickets


# Ejemplo de uso del sistema
sistema = Sistema_Venta_de_Tickets()
sistema.añadir_tipo_ticket("Premium", 100)
sistema.añadir_tipo_ticket("Normal", 50)

# Registro de ventas
sistema.registrar_venta("Premium", 8) # Descuento aplicado
sistema.registrar_venta("Normal", 4)

# Ver ventas registradas
print(sistema.obtener_ventas())
# Ver tipos de tickets
print(sistema.obtener_tipos_tickets())