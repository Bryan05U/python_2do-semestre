# 18 de noviembre de 2024

class Animal:
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        return "Ladra"

class Gato(Animal):
    def hablar(self):
        return "Maulla"
    
class Loro(Animal):
    def hablar(self):
        return "Habla"
    
# Ejemplo de polimorfismo
animales = [Perro(), Gato(), Loro()]
for animal in animales:
    print(animal.hablar())