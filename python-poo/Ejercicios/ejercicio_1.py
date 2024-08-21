# 21 de agosto de 2024
import math

class Persona():
    # Constructor de Clase
    def __init__(self, nombre, apellido, edad, estatura, peso):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.estatura = estatura
        self.peso = peso

    # Métodos (Comportamientos)
    def hablar(self):
        print(f"{self.nombre} está hablando sobre política")

    def caminar(self):
        print(f"{self.nombre} está caminando por las calles")

    def comer(self):
        print(f"{self.nombre} está comiendo pizza")

    def calcularIMC(self):
        print(f"El IMC es de: ", (math.trunc(self.peso / self.estatura **2)))

# Creación de un objeto de la clase Persona y agregando los atributos
persona1 = Persona("Bryan", "Cárcamo", 18, 1.75, 90)

# Acceso a los atributos y métodos del objeto
print(f"Nombre: {persona1.nombre}")
print(f"Apellido: {persona1.apellido}")
print(f"Edad: {persona1.edad} años")
print(f"Estatura: {persona1.estatura}")
print(f"Peso: {persona1.peso}")

# Llamando a los métodos de la Clase
persona1.hablar()
persona1.caminar()
persona1.comer()
persona1.calcularIMC()