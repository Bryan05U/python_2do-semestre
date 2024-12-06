# 2 de septiembre de 2024
"""
Crear una clase 'Items' que tenga un constructor y un destructor.
El constructor debe imprimir un mensaje cuando se cree un objeto, y el destructor debe imprimir un mensaje cuando el objeto sea destruido.

1. Crea una clase llamada Items.
2. Define un método __init__ que reciba un parámetro 'nombre' y asigne este nombre como atributo de la instancia.
3. Define un método __del__
4. Crea al menos dos intancias de la clase Items
5. Usa el comando del para eliminar las instancias
"""

class Items:
    def __init__(self, nombre):
        self.nombre = nombre
        print(f"{self.nombre} ha sido creado")

    def __del__(self):
        print(f"{self.nombre} se está destruyendo")

# Se crean los objetos para ver el comportamiento
item1 = Items("Primer objeto")
item2 = Items("Segundo objeto")

# Borrar los objetos para el llamado de __del__
del item1
del item2