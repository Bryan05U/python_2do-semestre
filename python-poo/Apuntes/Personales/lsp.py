# 02 de diciembre de 2024

class Animal:
    def run(self):
        print(f"El animal está corriendo")

class FlyingAnimal:
    def fly(Animal):
        print(f"El animal está volando")

# Clase Gaviota (puede volar, hereda de FlyingAnimal)
class Gaviota(FlyingAnimal):
    pass

# Clase Leopardo (no puede volar, hereda de Animal)
class Leopardo(Animal):
    pass

# Función que admite solo animales capaces de volar
def run_hole(animal: FlyingAnimal):
    animal.run()
    animal.fly()
    animal.run()