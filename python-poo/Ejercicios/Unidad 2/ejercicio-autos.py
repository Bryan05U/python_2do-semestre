"""
Implementar un sistema de gestión de vehículos para una concesionaria utilizando POO.
El objetivo es que practicar la creación de clases, constructores, métodos mágicos y el uso de atributos privados y públicos,
aplicando el concepto de encapsulamiento y visibilidad.

Tareas:
1. Crear la clase Vehiculo:
• Definir los atributos privados marca, modelo, año y disponible. El atributo __disponible debe estar inicialmente en True.
• Crear el método marcar_vendido() para cambiar el estado del vehículo a "no disponible".
• Crear el método __str__() para mostrar los detalles del vehículo.
2. Crear la clase Concesionaria:
• Implementar un sistema de gestión de vehículos en la concesionaria mediante una lista pública de vehículos.
• Definir el método agregar_vehiculo() para añadir nuevos vehículos a la concesionaria.
• Definir el método mostrar_vehiculos() para listar todos los vehículos disponibles en la concesionaria.
• Implementar el método vender_vehiculo() para cambiar el estado de disponibilidad de un vehículo a "no disponible"
cuando sea vendido. Si el vehículo ya fue vendido, muestra un mensaje indicando que no está disponible.

Interacción:
1. Crear una instancia de la clase Concesionaria y agregar varios vehículos.
2. Mostrar la lista de vehículos disponibles.
3. Realizar la venta de un vehículo y cambiar su estado de disponibilidad.
4. Volver a mostrar la lista de vehículos, verificando que el vehículo vendido ya no está disponible.
"""

class Vehículo:
    def __init__(self, marca, modelo, año):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.__disponible = True

    def marcar_vendido(self):
        self.__disponible = False

    def __str__(self):
        estado = "Disponible" if self.__disponible else "No disponible"
        return f"Marca: {self.__marca} Modelo: {self.__modelo} Año: ({self.__año}) Estado: {estado}"
    
class Consecionaria:
    def __init__(self):
        self.vehículos = []

    def agregar_vehículo(self, vehículo):
        self.vehículos.append(vehículo)

    def mostrar_vehículos(self):
        print("----- Vehículos disponibles en la concesionaria -----")
        for vehículo in self.vehículos:
            if vehículo._Vehículo__disponible:
                 print(vehículo)

    def vender_vehículo(self, vehículo):
        if vehículo in self.vehículos:
            if vehículo._Vehículo__disponible:
                vehículo.marcar_vendido()
                print(f"Vehículo vendido: {vehículo}")
            else:
                print(f"El vehículo {vehículo} ya no se encuentra disponible")
        else:
            print(f"El vehículo {vehículo} no está en la consecionaria")

consecionaria = Consecionaria()

primer_vehículo = Vehículo("Nissan", "Qashqai", 2024)
segundo_vehículo = Vehículo("Kia", "Soul", 2024)
tercer_vehículo = Vehículo("Volkswagen", "T-Cross", 2019)
cuarto_vehículo = Vehículo("Chevrolet", "Sonic", 2017)

consecionaria.agregar_vehículo(primer_vehículo)
consecionaria.agregar_vehículo(segundo_vehículo)
consecionaria.agregar_vehículo(tercer_vehículo)
consecionaria.agregar_vehículo(cuarto_vehículo)

consecionaria.mostrar_vehículos()

consecionaria.vender_vehículo(primer_vehículo)

consecionaria.mostrar_vehículos()