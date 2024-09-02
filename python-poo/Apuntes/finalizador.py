# 2 de septiembre de 2024
class Items:
    def __init__(self, nombre):
        self.nombre = nombre
        print(f"{self.nombre} ha sido creado")

    def __del__(self):
        print(f"{self.nombre} se está destruyendo")