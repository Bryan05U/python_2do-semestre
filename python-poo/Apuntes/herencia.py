# 13 de noviembre de 2024

# Superclase Animal
class Animal:
    def __init__(self, nombre, edad, peso, comida):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.comida = comida

    def hacer_sonido(self):
        print(f"El animal {self.nombre} hace un sonido")

    def comer(self):
        print(f"{self.nombre} está comiendo")

    def __str__(self):
        return f"{self.nombre} tiene {self.edad} años y pesa {self.peso} kg."

# Subclase Perro
class Perro(Animal):
    def __init__(self, nombre, edad, peso, raza, comida):
        super().__init__(nombre, edad, peso, comida)
        self.raza = raza
        self.comida = comida

    def hacer_sonido(self):
        print(f"{self.nombre} dice: 'Guau'")

    def ladrar(self):
        print(f"{self.nomnbre} está ladrando")

    def comer(self):
        print(f"{self.nombre} está comiendo {self.comida}")

    def mostrar_datos(self):
        print(f"{self} Es un perro de raza {self.raza}")

# Subclase Gato
class Gato(Animal):
    def __init__(self, nombre, edad, peso, color_pelaje, comida):
        super().__init__(nombre, edad, peso, comida)
        self.color_pelaje = color_pelaje
        self.comida = comida

    def hacer_sonido(self):
        print(f"{self.nombre} dice: 'Miau'")

    def maullar(self):
        print(f"{self.nombre} está maullando")

    def comer(self):
        print(f"{self.nombre} está comiendo {self.comida}")

    def mostrar_datos(self):
        print(f"{self} Es un gato de color de pelaje {self.color_pelaje}")

# Subclase Pájaro
class Pájaro(Animal):
    def __init__(self, nombre, edad, peso, especie, comida):
        super().__init__(nombre, edad, peso, comida)
        self.especie = especie
        self.comida = comida

    def hacer_sonido(self):
        print(f"{self.nombre} dice: 'Pío'")

    def cantar(self):
        print(f"{self.nombre} está cantando")

    def comer(self):
        print(f"{self.nombre} está comiendo {self.comida}")

    def mostrar_datos(self):
        print(f"{self} Es un pájaro de especie {self.especie}")

# Subclase Pez
class Pez(Animal):
    def __init__(self, nombre, edad, peso, tipo, comida):
        super().__init__(nombre, edad, peso, comida)
        self.tipo = tipo
        self.comida = comida

    def hacer_sonido(self):
        print(f"{self.nombre} hace burbujeas bajo el agua")

    def comer(self):
        print(f"{self.nombre} está comiendo {self.comida}")

    def mostrar_datos(self):
        print(f"{self} Es un pez {self.tipo}")

# Creación de las instancias de clases para cada animal
mi_perro = Perro('Apolo', 4, 60, 'Gran Danés', 'Carne')
mi_gato = Gato('Luis', 6, 4, 'Negro', 'Pescado')
mi_pájaro = Pájaro('Jorge', 3, 3, "Loro", 'Semillas')
mi_pez = Pez('Pedro', 2, 0.4, 'Globo', 'Algas')

# Imprimir los sonidos
mi_perro.hacer_sonido()
mi_gato.hacer_sonido()
mi_pájaro.hacer_sonido()
mi_pez.hacer_sonido()

# Mostrar los datos completos de cada animal
mi_perro.mostrar_datos()
mi_gato.mostrar_datos()
mi_pájaro.mostrar_datos()
mi_pez.mostrar_datos()

# Imprimir las acciones de comer de cada animal
mi_perro.comer()
mi_gato.comer()
mi_pájaro.comer()
mi_pez.comer()