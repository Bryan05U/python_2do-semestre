from datetime import datetime # Esta implementación permite operaciones aritméticas con fechas y horas
"""
1. Se solicita crear una clase ReservaHostal que permita a los usuarios crear reservas de habitaciones en un hostal.
Cada reserva tendrá atributos como el nombre del cliente, la fecha de entrada, la fecha de salida, y el número de habitación.
Implementar los siguientes requerimientos:
Métodos:
● Un método para calcular la duración de la estadía del cliente.
● Un método mágico para mostrar la información de la reserva.
● Un método para cambiar la fecha de salida.
Se debe eliminar un objeto ReservaHostal, además de imprimir un mensaje indicando que la reserva ha sido cancelada.
"""

# Creando una clase ReservaHostal y añadiendo sus atributos
class ReservaHostal:
    def __init__(self, nombre_cliente, fecha_entrada, fecha_salida, número_habitación):
        self.nombre_cliente = nombre_cliente
        self.fecha_entrada = datetime.strptime(fecha_entrada, '%Y-%m-%d')
        self.fecha_salida = datetime.strptime(fecha_salida, '%Y-%m-%d')
        self.número_habitación = número_habitación

    # Método que permite calcular la duración de la estadia del cliente
    def calcular_duración_estadia(self):
        duración = (self.fecha_salida - self.fecha_entrada).days
        return duración

    # Método mágico que permite mostrar la información de la reserva
    def __str__(self):
        return(f"---Reserva Hostal---\n"
               f"Nombre del Cliente: {self.nombre_cliente}\n"
               f"Fecha de Entrada: {self.fecha_entrada.strftime('%Y-%m-%d')}\n"
               f"Fecha de Salida: {self.fecha_salida.strftime('%Y-%m-%d')}\n"
               f"Número de Habitación: {self.número_habitación}\n"
               f"Duración de Estadia: {self.calcular_duración_estadia()} días")
    
    # Método que cambia la fecha de salida
    def cambiar_fecha_salida(self, nueva_fecha_salida):
        self.fecha_salida= datetime.strptime(nueva_fecha_salida, '%Y-%m-%d')
    
    # Método que elimina el nombre de la reserva
    def __del__(self):
        print(f"La reserva de {self.nombre_cliente} fue cancelada")

reserva = ReservaHostal('Bryan Cárcamo', '2024-01-23', '2024-01-30', 45)
print(reserva) # Muestra la información de la reserva

reserva.cambiar_fecha_salida('2024-01-27') # Cambia la fecha de la salida
print(reserva) # Muestra la información actualizada de la reserva

del reserva # Elimina el objeto y muestra el mensaje de cancelación